#!/usr/bin/env python3
"""Inventory and repair MA free-response questions misrendered as MCQs.

The answer key is processed in study order.  A target quiz is converted only
when its topic/question pair is classified as ``free-response`` in the Math
Academy question ledger.  Duplicate local placements are repaired together and
checked against the answer key's expected occurrence count.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MA_QUESTIONS = REPO_ROOT / "vault" / "MA" / "questions.csv"

QUIZ_RE = re.compile(r"```quiz\n(?P<body>.*?)\n```", re.DOTALL)
QUESTION_RE = re.compile(
    r"^\*\*Question\s+(?P<number>\d+):?\*\*.*?(?P<body>.*?)(?=^\*\*Question\s+\d+:?\*\*|^---\s*$|\Z)",
    re.MULTILINE | re.DOTALL | re.IGNORECASE,
)
LESSON_ID_RE = re.compile(r"^lesson-id:\s*(?P<id>\d+)\s*$", re.MULTILINE)
QUIZ_ID_RE = re.compile(r"^id:\s*(?P<id>\S+)\s*$", re.MULTILINE)
QUIZ_TYPE_RE = re.compile(r"^type:\s*(?P<type>\S+)\s*$", re.MULTILINE)
MARKER = "MA_ANSWER_MISSING"


@dataclass(frozen=True)
class Answer:
    study_order: int
    topic_id: str
    question_number: int
    question_id: str
    answer: str
    expected_occurrences: int
    response_instruction: str


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def lesson_id(text: str) -> str | None:
    match = LESSON_ID_RE.search(text)
    return match.group("id") if match else None


def quiz_id(body: str) -> str | None:
    match = QUIZ_ID_RE.search(body)
    if not match:
        return None
    return re.sub(r"^(?:ma-|q-)", "", match.group("id"), flags=re.IGNORECASE)


def quiz_type(body: str) -> str:
    match = QUIZ_TYPE_RE.search(body)
    return match.group("type") if match else ""


def load_answers(path: Path) -> list[Answer]:
    rows = read_csv(path)
    answers = [
        Answer(
            study_order=int(row["study-order"]),
            topic_id=row["topic-id"].strip(),
            question_number=int(row["question-number"]),
            question_id=row["question-id"].strip(),
            answer=row["answer"],
            expected_occurrences=int(row["expected-occurrences"]),
            response_instruction=row.get("response-instruction", "").strip(),
        )
        for row in rows
    ]
    if answers != sorted(answers, key=lambda item: item.study_order):
        raise ValueError("Answer key is not in ascending study order")
    keys = [(item.topic_id, item.question_id) for item in answers]
    if len(keys) != len(set(keys)):
        raise ValueError("Answer key contains duplicate topic/question pairs")
    return answers


def load_ledger() -> dict[tuple[str, str], dict[str, str]]:
    return {
        (row["topic-id"], row["question-id"]): row
        for row in read_csv(MA_QUESTIONS)
    }


def load_topic_metadata(course_root: Path) -> dict[str, dict[str, object]]:
    rows = read_csv(course_root / "topics.csv")
    metadata: dict[str, dict[str, object]] = {}
    for index, row in enumerate(rows):
        topic_id = row["topic-id"].strip()
        metadata.setdefault(
            topic_id,
            {
                "row-index": index,
                "role": row["role"],
                "layer": int(row["layer"]),
                "course": row["course"],
                "topic-number": row["topic-number"],
                "topic-name": row["topic-name"],
                "source-path": row["src-path"],
            },
        )
    return metadata


def resolve_repo_path(raw: str) -> Path:
    path = Path(raw)
    return path if path.is_absolute() else REPO_ROOT / path


def load_source_question_map(raw_source_path: str) -> dict[str, str]:
    if not raw_source_path:
        return {}
    source_path = resolve_repo_path(raw_source_path)
    if not source_path.exists():
        return {}
    result: dict[str, str] = {}
    for json_path in sorted(source_path.glob("*.json")):
        if json_path.name == "_image_meta.json" or not json_path.name[:1].isdigit():
            continue
        try:
            payload = json.loads(json_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        items = payload.get("lesson", {}).get("items", [])
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            number = item.get("question_number")
            question_id = item.get("question_id")
            if number is not None and question_id is not None:
                result[str(number)] = str(question_id)
    return result


def inventory_question_id(body: str, number: int, meta: dict[str, object]) -> str | None:
    match = QUIZ_ID_RE.search(body)
    if not match:
        return None
    raw = match.group("id")
    if raw.lower().startswith("ma-"):
        return raw[3:]
    source_map = meta.get("source-question-map")
    if not isinstance(source_map, dict):
        source_map = load_source_question_map(str(meta.get("source-path", "")))
        meta["source-question-map"] = source_map
    return source_map.get(str(number))


def topic_number_key(raw: str) -> tuple[int, ...]:
    parts = []
    for part in raw.split("."):
        match = re.match(r"\d+", part)
        parts.append(int(match.group(0)) if match else 10**9)
    return tuple(parts)


def build_inventory(
    course_root: Path,
    texts: dict[Path, str],
    answers: list[Answer],
    ledger: dict[tuple[str, str], dict[str, str]],
) -> list[dict[str, str]]:
    topic_metadata = load_topic_metadata(course_root)
    answer_map = {(item.topic_id, item.question_id): item.answer for item in answers}
    grouped: dict[tuple[str, str], dict[str, object]] = {}

    for path, text in texts.items():
        topic_id = lesson_id(text)
        if not topic_id:
            continue
        meta = topic_metadata.get(topic_id, {})
        for section in QUESTION_RE.finditer(text):
            number = int(section.group("number"))
            for quiz in QUIZ_RE.finditer(section.group("body")):
                body = quiz.group("body")
                if MARKER not in body:
                    continue
                question_id = inventory_question_id(body, number, meta)
                if not question_id:
                    raise ValueError(f"Missing quiz id in {rel(path)} question {number}")
                key = (topic_id, question_id)
                row = grouped.setdefault(
                    key,
                    {
                        "question-number": number,
                        "types": set(),
                        "placements": [],
                    },
                )
                if row["question-number"] != number:
                    raise ValueError(f"Question number mismatch for topic/question {key}")
                row["types"].add(quiz_type(body))
                row["placements"].append(rel(path))

    def sort_key(item: tuple[tuple[str, str], dict[str, object]]) -> tuple[object, ...]:
        (topic_id, _), row = item
        meta = topic_metadata.get(topic_id, {})
        return (
            int(meta.get("layer", 10**9)),
            str(meta.get("course", "")),
            topic_number_key(str(meta.get("topic-number", ""))),
            int(meta.get("row-index", 10**9)),
            int(row["question-number"]),
        )

    output: list[dict[str, str]] = []
    for order, (key, row) in enumerate(sorted(grouped.items(), key=sort_key), start=1):
        topic_id, question_id = key
        meta = topic_metadata.get(topic_id, {})
        ledger_row = ledger.get(key)
        original_type = ledger_row.get("question-type", "ledger-missing") if ledger_row else "ledger-missing"
        if original_type == "free-response" and key in answer_map:
            action = "convert-to-free"
        elif original_type == "multiple-choice":
            action = "retain-genuine-mcq"
        elif original_type == "free-response":
            action = "missing-free-response-answer"
        else:
            action = "manual-review"
        output.append(
            {
                "queue-order": str(order),
                "layer": str(meta.get("layer", "")),
                "role": str(meta.get("role", "")),
                "topic-id": topic_id,
                "topic-number": str(meta.get("topic-number", "")),
                "topic-name": str(meta.get("topic-name", "")),
                "question-number": str(row["question-number"]),
                "question-id": question_id,
                "original-question-type": original_type,
                "current-quiz-type": ";".join(sorted(row["types"])),
                "occurrences": str(len(row["placements"])),
                "placements": ";".join(sorted(row["placements"])),
                "action": action,
                "keyboard-answer": answer_map.get(key, ""),
            }
        )
    return output


def write_inventory(path: Path, rows: list[dict[str, str]]) -> None:
    fields = [
        "queue-order",
        "layer",
        "role",
        "topic-id",
        "topic-number",
        "topic-name",
        "question-number",
        "question-id",
        "original-question-type",
        "current-quiz-type",
        "occurrences",
        "placements",
        "action",
        "keyboard-answer",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def extract_content_lines(body: str) -> list[str]:
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"^content:\s*[>|]", line):
            end = index + 1
            while end < len(lines):
                if lines[end].startswith("  ") or not lines[end].strip():
                    end += 1
                    continue
                break
            content = lines[index:end]
            while len(content) > 1 and not content[-1].strip():
                content.pop()
            return content
    raise ValueError("Quiz block has no top-level content block scalar")


def correct_answer(body: str) -> str | None:
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"^correct:\s*[>|]", line):
            values: list[str] = []
            index += 1
            while index < len(lines) and (lines[index].startswith("  ") or not lines[index].strip()):
                values.append(lines[index][2:] if lines[index].startswith("  ") else "")
                index += 1
            return "\n".join(values).strip()
    return None


def free_body(body: str, raw_id: str, answer: str, response_instruction: str) -> str:
    content = extract_content_lines(body)
    if response_instruction:
        instruction_line = f"  {response_instruction}"
        if instruction_line not in content:
            while len(content) > 1 and not content[-1].strip():
                content.pop()
            content.extend(["", instruction_line])
        else:
            instruction_index = content.index(instruction_line)
            if instruction_index > 0 and not content[instruction_index - 1].strip():
                content[instruction_index - 1] = ""
    correct = ["correct: |-", *(f"  {line}" for line in answer.splitlines())]
    return "\n".join(["type: free", f"id: {raw_id}", *content, *correct])


def repair(
    texts: dict[Path, str],
    answers: list[Answer],
    ledger: dict[tuple[str, str], dict[str, str]],
) -> tuple[dict[Path, str], list[str]]:
    changed: set[Path] = set()
    report: list[str] = []

    for item in answers:
        key = (item.topic_id, item.question_id)
        ledger_row = ledger.get(key)
        if not ledger_row:
            raise ValueError(f"Answer key topic/question is absent from MA ledger: {key}")
        if ledger_row.get("question-type") != "free-response":
            raise ValueError(f"Refusing non-free-response ledger row: {key}")

        seen = 0
        converted = 0
        already_free = 0
        updated_free = 0
        for path in sorted(texts):
            if lesson_id(texts[path]) != item.topic_id:
                continue

            def replace(match: re.Match[str]) -> str:
                nonlocal seen, converted, already_free, updated_free
                body = match.group("body")
                id_match = QUIZ_ID_RE.search(body)
                if not id_match or quiz_id(body) != item.question_id:
                    return match.group(0)
                seen += 1
                current_type = quiz_type(body)
                if current_type == "free":
                    if MARKER in body or "\noptions:" in body:
                        raise ValueError(f"Malformed existing free block for {key} in {rel(path)}")
                    new_body = free_body(
                        body,
                        id_match.group("id"),
                        item.answer,
                        item.response_instruction,
                    )
                    if new_body == body:
                        already_free += 1
                        return match.group(0)
                    updated_free += 1
                    return f"```quiz\n{new_body}\n```"
                if current_type not in {"radio", "checkbox"} or MARKER not in body:
                    raise ValueError(f"Unexpected source block for {key} in {rel(path)}")
                converted += 1
                new_body = free_body(
                    body,
                    id_match.group("id"),
                    item.answer,
                    item.response_instruction,
                )
                return f"```quiz\n{new_body}\n```"

            new_text = QUIZ_RE.sub(replace, texts[path])
            if new_text != texts[path]:
                texts[path] = new_text
                changed.add(path)

        if seen != item.expected_occurrences:
            raise ValueError(
                f"Expected {item.expected_occurrences} occurrences for {key}; found {seen}"
            )
        report.append(
            f"{item.study_order:02d}. topic {item.topic_id} question {item.question_number} "
            f"(ma-{item.question_id}): answer={item.answer!r}; converted={converted}; "
            f"updated-free={updated_free}; already-free={already_free}; occurrences={seen}"
        )

    for item in answers:
        key = (item.topic_id, item.question_id)
        verified = 0
        for path, text in texts.items():
            if lesson_id(text) != item.topic_id:
                continue
            for match in QUIZ_RE.finditer(text):
                body = match.group("body")
                if quiz_id(body) != item.question_id:
                    continue
                verified += 1
                if quiz_type(body) != "free":
                    raise ValueError(f"Post-repair type check failed for {key} in {rel(path)}")
                if correct_answer(body) != item.answer:
                    raise ValueError(f"Post-repair answer check failed for {key} in {rel(path)}")
                if MARKER in body or "\noptions:" in body:
                    raise ValueError(f"Post-repair cleanup check failed for {key} in {rel(path)}")
                if item.response_instruction and item.response_instruction not in body:
                    raise ValueError(f"Post-repair instruction check failed for {key} in {rel(path)}")
        if verified != item.expected_occurrences:
            raise ValueError(f"Post-repair occurrence check failed for {key}: {verified}")

    return texts, [*report, f"Files changed: {len(changed)}", *(rel(path) for path in sorted(changed))]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("course_root", type=Path)
    parser.add_argument("answer_key", type=Path)
    parser.add_argument("--inventory-output", type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    course_root = args.course_root.resolve()
    answers = load_answers(args.answer_key.resolve())
    ledger = load_ledger()
    texts = {
        path: path.read_text(encoding="utf-8")
        for path in sorted(course_root.rglob("*.md"))
    }

    inventory = build_inventory(course_root, texts, answers, ledger)
    if args.inventory_output:
        write_inventory(args.inventory_output.resolve(), inventory)
        print(f"Wrote {len(inventory)} unique missing-question rows to {args.inventory_output}")

    missing_free = [row for row in inventory if row["action"] == "missing-free-response-answer"]
    manual_review = [row for row in inventory if row["action"] == "manual-review"]
    if missing_free or manual_review:
        raise ValueError(
            f"Inventory is not fully classified: missing-free={len(missing_free)}, manual-review={len(manual_review)}"
        )

    repaired, report = repair(texts, answers, ledger)
    for line in report:
        print(line)

    if args.write:
        for path, text in repaired.items():
            if path.read_text(encoding="utf-8") != text:
                path.write_text(text, encoding="utf-8")
        print("Repairs written.")
    else:
        print("Dry run only; pass --write to apply repairs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
