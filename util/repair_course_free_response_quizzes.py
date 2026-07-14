#!/usr/bin/env python3
"""Inventory and repair MA free-response questions misrendered as MCQs.

The answer key is processed in study order.  A target quiz is converted only
when its topic/question pair is classified as ``free-response`` in the Math
Academy question ledger.  The repaired form is an exact-match ``blank`` quiz,
with inline ``==answer==`` gaps defined in a separate layout file.  Duplicate
local placements are repaired together and checked against the answer key's
expected occurrence count.
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
BLANK_ANSWER_RE = re.compile(r"==(?P<answer>.+?)==")
OPTION_BLOCK_RE = re.compile(
    r"^- id:\s*(?P<label>[a-z])\s*$\n(?P<body>.*?)(?=^- id:\s*[a-z]\s*$|\Z)",
    re.MULTILINE | re.DOTALL,
)


@dataclass(frozen=True)
class Answer:
    study_order: int
    topic_id: str
    question_number: int
    question_id: str
    answer: str
    expected_occurrences: int


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
        )
        for row in rows
    ]
    if answers != sorted(answers, key=lambda item: item.study_order):
        raise ValueError("Answer key is not in ascending study order")
    keys = [(item.topic_id, item.question_id) for item in answers]
    if len(keys) != len(set(keys)):
        raise ValueError("Answer key contains duplicate topic/question pairs")
    return answers


def load_blank_layouts(path: Path, answers: list[Answer]) -> dict[tuple[str, str], str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Blank layout file must contain a JSON object")

    layouts: dict[tuple[str, str], str] = {}
    answer_keys = {(item.topic_id, item.question_id) for item in answers}
    for raw_key, content in payload.items():
        if not isinstance(raw_key, str) or ":" not in raw_key or not isinstance(content, str):
            raise ValueError(f"Invalid blank layout entry: {raw_key!r}")
        topic_id, question_id = raw_key.split(":", 1)
        key = (topic_id, question_id)
        if key in layouts:
            raise ValueError(f"Duplicate blank layout key: {key}")
        layouts[key] = content

    if set(layouts) != answer_keys:
        missing = sorted(answer_keys - set(layouts))
        extra = sorted(set(layouts) - answer_keys)
        raise ValueError(f"Blank layout key mismatch: missing={missing}, extra={extra}")

    for item in answers:
        key = (item.topic_id, item.question_id)
        inline_answers = BLANK_ANSWER_RE.findall(layouts[key])
        if not inline_answers:
            raise ValueError(f"Blank layout contains no ==answer== gaps: {key}")
        if ", ".join(inline_answers) != item.answer:
            raise ValueError(
                f"Blank layout answers do not match answer key for {key}: {inline_answers}"
            )
    return layouts


def load_ledger() -> dict[tuple[str, str], dict[str, str]]:
    return {
        (row["topic-id"], row["question-id"]): row
        for row in read_csv(MA_QUESTIONS)
    }


def load_topic_metadata(course_root: Path) -> dict[str, dict[str, object]]:
    rows = read_csv(course_root / "topics.csv")
    if rows and "role" not in rows[0]:
        rows = read_csv(course_root / "catalog.csv")
        metadata: dict[str, dict[str, object]] = {}
        for index, row in enumerate(rows):
            topic_id = row["topic-id"].strip()
            if not row.get("lesson-path") or not row.get("source-path"):
                continue
            metadata.setdefault(
                topic_id,
                {
                    "row-index": index,
                    "role": "lesson",
                    "layer": int(row["layer"]),
                    "course": row["topic-code"].split(".", 1)[0],
                    "topic-number": row["topic-code"],
                    "topic-name": row["topic-name"],
                    "source-path": row["source-path"],
                },
            )
        return metadata
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


def load_source_questions(raw_source_path: str) -> dict[str, dict[str, object]]:
    """Load normalized source question records keyed by Math Academy question id."""
    if not raw_source_path:
        return {}
    source_path = resolve_repo_path(raw_source_path)
    if not source_path.exists():
        return {}
    result: dict[str, dict[str, object]] = {}
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
            if not isinstance(item, dict) or item.get("question_id") is None:
                continue
            result[str(item["question_id"])] = item
    return result


def print_source_details(course_root: Path, rows: list[dict[str, str]], texts: dict[Path, str]) -> None:
    """Print source blank scaffolding and one current quiz for conversion review."""
    metadata = load_topic_metadata(course_root)
    cached: dict[str, dict[str, dict[str, object]]] = {}
    for row in rows:
        if row["action"] != "convert-to-exact-blank":
            continue
        topic_id = row["topic-id"]
        questions = cached.setdefault(
            topic_id,
            load_source_questions(str(metadata.get(topic_id, {}).get("source-path", ""))),
        )
        item = questions.get(row["question-id"])
        if item is None:
            raise ValueError(
                f"Could not load source question {row['question-id']} for topic {topic_id}"
            )
        placement = resolve_repo_path(row["placements"].split(";", 1)[0])
        current_body = ""
        for quiz in QUIZ_RE.finditer(texts[placement]):
            raw_quiz_id = QUIZ_ID_RE.search(quiz.group("body"))
            if (
                quiz_id(quiz.group("body")) == row["question-id"]
                or (
                    raw_quiz_id
                    and raw_quiz_id.group("id").lower()
                    == f"q-{row['question-number']}"
                )
            ):
                current_body = quiz.group("body")
                break
        print(
            "\n".join(
                [
                    f"=== queue {row['queue-order']} | topic {topic_id} | "
                    f"question {row['question-number']} | ma-{row['question-id']} ===",
                    str(item.get("readable_text", "")),
                    "SOURCE PROMPT HTML:",
                    str(item.get("prompt", {}).get("normalized_html", "")),
                    "CURRENT QUIZ:",
                    current_body,
                ]
            )
        )


def correct_option_content(body: str) -> tuple[str, str]:
    matches: list[tuple[str, str]] = []
    for option in OPTION_BLOCK_RE.finditer(body):
        option_body = option.group("body")
        if not re.search(r"^\s*correct:\s*true\s*$", option_body, re.MULTILINE):
            continue
        content_match = re.search(
            r"^\s*content:\s*\|-\s*$\n(?P<content>(?: {4}.*(?:\n|\Z))*)",
            option_body,
            re.MULTILINE,
        )
        content = ""
        if content_match:
            content = "\n".join(
                line[4:] if line.startswith("    ") else line
                for line in content_match.group("content").rstrip("\n").splitlines()
            )
        matches.append((option.group("label"), content))
    if len(matches) != 1:
        return "", ""
    return matches[0]


def write_answer_candidates(
    path: Path,
    rows: list[dict[str, str]],
    texts: dict[Path, str],
) -> None:
    fields = [
        "queue-order",
        "topic-id",
        "question-number",
        "question-id",
        "current-quiz-type",
        "occurrences",
        "correct-label",
        "correct-content",
        "placement",
    ]
    output: list[dict[str, str]] = []
    for row in rows:
        placement = resolve_repo_path(row["placements"].split(";", 1)[0])
        target_body = ""
        for quiz in QUIZ_RE.finditer(texts[placement]):
            raw_id_match = QUIZ_ID_RE.search(quiz.group("body"))
            if not raw_id_match:
                continue
            raw_id = raw_id_match.group("id").lower()
            if quiz_id(quiz.group("body")) == row["question-id"] or raw_id == f"q-{row['question-number']}":
                target_body = quiz.group("body")
                break
        label, content = correct_option_content(target_body)
        output.append(
            {
                "queue-order": row["queue-order"],
                "topic-id": row["topic-id"],
                "question-number": row["question-number"],
                "question-id": row["question-id"],
                "current-quiz-type": row["current-quiz-type"],
                "occurrences": row["occurrences"],
                "correct-label": label,
                "correct-content": content,
                "placement": rel(placement),
            }
        )
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)


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
    *,
    missing_only: bool = True,
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
                if missing_only and MARKER not in body:
                    continue
                question_id = inventory_question_id(body, number, meta)
                if not question_id:
                    raise ValueError(f"Missing quiz id in {rel(path)} question {number}")
                key = (topic_id, question_id)
                row = grouped.setdefault(
                    key,
                    {
                        "question-number": number,
                        "question-numbers": {number},
                        "types": set(),
                        "exact-blank": True,
                        "placements": [],
                    },
                )
                row["question-numbers"].add(number)
                row["question-number"] = min(row["question-numbers"])
                row["types"].add(quiz_type(body))
                row["exact-blank"] = bool(row["exact-blank"]) and (
                    quiz_type(body) == "blank" and "require_exact: false" not in body
                )
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
        if original_type == "free-response" and bool(row["exact-blank"]):
            action = "already-exact-blank"
        elif original_type == "free-response":
            action = "convert-to-exact-blank"
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


def exact_blank_body(raw_id: str, content: str) -> str:
    content_lines = [f"  {line}" if line else "" for line in content.splitlines()]
    return "\n".join(
        [
            "type: blank",
            f"id: {raw_id}",
            "require_exact: true",
            "content: |-",
            *content_lines,
        ]
    )


def repair(
    texts: dict[Path, str],
    answers: list[Answer],
    ledger: dict[tuple[str, str], dict[str, str]],
    layouts: dict[tuple[str, str], str],
) -> tuple[dict[Path, str], list[str]]:
    changed: set[Path] = set()
    report: list[str] = []

    def matches_item(body: str, item: Answer) -> bool:
        id_match = QUIZ_ID_RE.search(body)
        if not id_match:
            return False
        raw_id = id_match.group("id")
        return (
            quiz_id(body) == item.question_id
            or raw_id.lower() == f"q-{item.question_number}"
        )

    for item in answers:
        key = (item.topic_id, item.question_id)
        ledger_row = ledger.get(key)
        if not ledger_row:
            raise ValueError(f"Answer key topic/question is absent from MA ledger: {key}")
        if ledger_row.get("question-type") != "free-response":
            raise ValueError(f"Refusing non-free-response ledger row: {key}")

        seen = 0
        converted_to_blank = 0
        already_blank = 0
        updated_blank = 0
        for path in sorted(texts):
            if lesson_id(texts[path]) != item.topic_id:
                continue

            def replace(match: re.Match[str]) -> str:
                nonlocal seen, converted_to_blank, already_blank, updated_blank
                body = match.group("body")
                id_match = QUIZ_ID_RE.search(body)
                if not id_match or not matches_item(body, item):
                    return match.group(0)
                seen += 1
                current_type = quiz_type(body)
                new_body = exact_blank_body(id_match.group("id"), layouts[key])
                if current_type == "blank":
                    if "require_exact: false" in body:
                        raise ValueError(f"Reveal-only blank found for {key} in {rel(path)}")
                    if new_body == body:
                        already_blank += 1
                        return match.group(0)
                    updated_blank += 1
                    return f"```quiz\n{new_body}\n```"
                if current_type == "free":
                    if MARKER in body or "\noptions:" in body:
                        raise ValueError(f"Malformed existing free block for {key} in {rel(path)}")
                elif current_type not in {"radio", "checkbox"}:
                    raise ValueError(f"Unexpected source block for {key} in {rel(path)}")
                converted_to_blank += 1
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
            f"(ma-{item.question_id}): answers={BLANK_ANSWER_RE.findall(layouts[key])!r}; "
            f"converted-to-blank={converted_to_blank}; updated-blank={updated_blank}; "
            f"already-blank={already_blank}; occurrences={seen}"
        )

    for item in answers:
        key = (item.topic_id, item.question_id)
        verified = 0
        for path, text in texts.items():
            if lesson_id(text) != item.topic_id:
                continue
            for match in QUIZ_RE.finditer(text):
                body = match.group("body")
                if not matches_item(body, item):
                    continue
                verified += 1
                if quiz_type(body) != "blank":
                    raise ValueError(f"Post-repair type check failed for {key} in {rel(path)}")
                desired = exact_blank_body(QUIZ_ID_RE.search(body).group("id"), layouts[key])
                if body != desired:
                    raise ValueError(f"Post-repair layout check failed for {key} in {rel(path)}")
                if MARKER in body or "\noptions:" in body or "\ncorrect:" in body:
                    raise ValueError(f"Post-repair cleanup check failed for {key} in {rel(path)}")
        if verified != item.expected_occurrences:
            raise ValueError(f"Post-repair occurrence check failed for {key}: {verified}")

    return texts, [*report, f"Files changed: {len(changed)}", *(rel(path) for path in sorted(changed))]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("course_root", type=Path)
    parser.add_argument("answer_key", type=Path)
    parser.add_argument("--blank-layouts", type=Path, required=True)
    parser.add_argument("--inventory-output", type=Path)
    parser.add_argument("--all-free-response-output", type=Path)
    parser.add_argument("--source-details", action="store_true")
    parser.add_argument("--answer-candidates-output", type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    course_root = args.course_root.resolve()
    answers = load_answers(args.answer_key.resolve())
    layouts = load_blank_layouts(args.blank_layouts.resolve(), answers)
    ledger = load_ledger()
    texts = {
        path: path.read_text(encoding="utf-8")
        for path in sorted(course_root.rglob("*.md"))
    }

    inventory = build_inventory(course_root, texts, answers, ledger)
    if args.inventory_output:
        write_inventory(args.inventory_output.resolve(), inventory)
        print(f"Wrote {len(inventory)} unique missing-question rows to {args.inventory_output}")

    if args.all_free_response_output:
        all_rows = build_inventory(
            course_root,
            texts,
            answers,
            ledger,
            missing_only=False,
        )
        free_rows = [
            row for row in all_rows
            if row["original-question-type"] == "free-response"
        ]
        write_inventory(args.all_free_response_output.resolve(), free_rows)
        print(
            f"Wrote {len(free_rows)} unique MA free-response rows to "
            f"{args.all_free_response_output}"
        )
        if args.source_details:
            print_source_details(course_root, free_rows, texts)
        if args.answer_candidates_output:
            write_answer_candidates(args.answer_candidates_output.resolve(), free_rows, texts)

    missing_free = [row for row in inventory if row["action"] == "missing-free-response-answer"]
    manual_review = [row for row in inventory if row["action"] == "manual-review"]
    if missing_free or manual_review:
        raise ValueError(
            f"Inventory is not fully classified: missing-free={len(missing_free)}, manual-review={len(manual_review)}"
        )

    repaired, report = repair(texts, answers, ledger, layouts)
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
