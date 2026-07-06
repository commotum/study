#!/usr/bin/env python3
"""Mass-convert imported MA lesson MCQs to quiz blocks and repair ledgers.

This is intentionally a batch driver around ``convert_mcq_to_quiz.py``.  The
single-file converter knows how to rewrite Markdown shape; this script adds the
vault-specific bookkeeping: source JSON question-id mapping, duplicate course
copy provenance, propagation of already-known answers, and ``needs-answer``
ledger state for unresolved converted MCQs.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MA_ROOT = REPO_ROOT / "vault" / "MA"
CONVERTER_PATH = REPO_ROOT / "util" / "convert_mcq_to_quiz.py"

QUIZ_BLOCK_RE = re.compile(r"```quiz\n(?P<body>.*?)\n```", re.DOTALL)
QUIZ_ID_RE = re.compile(r"^id:\s*(?P<id>\S+)\s*$", re.MULTILINE)
QUIZ_TYPE_RE = re.compile(r"^type:\s*(?P<type>\S+)\s*$", re.MULTILINE)
OPTION_ID_RE = re.compile(r"^- id: (?P<label>[a-z])\s*$", re.MULTILINE)
CORRECT_RE = re.compile(r"^\s+correct:\s+true\s*$", re.MULTILINE)
QUESTION_SECTION_RE = re.compile(
    r"(?P<head>^\*\*Question\s+(?P<number>\d+):?\*\*.*?$)(?P<body>.*?)(?=^\*\*Question\s+\d+:?\*\*|^---\s*$|\Z)",
    re.MULTILINE | re.DOTALL | re.IGNORECASE,
)
QUESTION_ID_RE = re.compile(r"^(?:ma-|q-)?(?P<id>\d+)$", re.IGNORECASE)


@dataclass(frozen=True)
class LessonCatalog:
    topic_id: str
    topic_code: str
    course: str
    lesson_path: Path
    source_path: Path | None


@dataclass
class FileStats:
    converted_raw: int = 0
    repaired_partial: int = 0
    normalized_ids: int = 0
    propagated_answers: int = 0
    missing_blocks: int = 0
    verified_blocks: int = 0
    unresolved_ids: int = 0
    changed: bool = False


def load_converter():
    spec = importlib.util.spec_from_file_location("convert_mcq_to_quiz", CONVERTER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {CONVERTER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def course_prefix(topic_code: str) -> str:
    return topic_code.split(".", 1)[0]


def normalize_rel_path(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def load_catalog() -> dict[Path, list[LessonCatalog]]:
    _, rows = read_csv(MA_ROOT / "catalog.csv")
    by_path: dict[Path, list[LessonCatalog]] = defaultdict(list)
    for row in rows:
        lesson = row.get("lesson-path", "").strip()
        if not lesson:
            continue
        lesson_path = normalize_rel_path(lesson)
        source = row.get("source-path", "").strip()
        by_path[lesson_path].append(
            LessonCatalog(
                topic_id=row["topic-id"],
                topic_code=row["topic-code"],
                course=course_prefix(row["topic-code"]),
                lesson_path=lesson_path,
                source_path=normalize_rel_path(source) if source else None,
            )
        )
    return by_path


def load_question_ledgers() -> tuple[list[str], list[dict[str, str]], dict[tuple[str, str], dict[str, str]]]:
    fields, rows = read_csv(MA_ROOT / "questions.csv")
    by_key = {(row["topic-id"], row["question-id"]): row for row in rows}
    return fields, rows, by_key


def load_source_question_map(source_path: Path | None) -> dict[str, str]:
    if source_path is None or not source_path.exists():
        return {}
    json_files = sorted(
        path
        for path in source_path.glob("*.json")
        if path.name != "_image_meta.json" and path.name[0].isdigit()
    )
    question_map: dict[str, str] = {}
    for json_file in json_files:
        try:
            payload = json.loads(json_file.read_text(encoding="utf-8"))
        except Exception:
            continue
        items = payload.get("lesson", {}).get("items", [])
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            number = item.get("question_number")
            question_id = item.get("question_id")
            if number is None or question_id is None:
                continue
            question_map[str(number)] = str(question_id)
    return question_map


def answer_labels_by_question(
    topic_id: str,
    question_map: dict[str, str],
    question_rows: dict[tuple[str, str], dict[str, str]],
) -> dict[str, set[str]]:
    answers: dict[str, set[str]] = {}
    for number, question_id in question_map.items():
        row = question_rows.get((topic_id, question_id))
        if not row:
            continue
        if row.get("quiz-status", "").strip() != "converted-and-verified":
            continue
        labels = {
            label.strip().lower()
            for label in re.split(r"[\s,+/|]+", row.get("quiz-answer-labels", ""))
            if label.strip()
        }
        if not labels:
            continue
        answers[number] = labels
        answers[question_id] = labels
        answers[f"ma-{question_id}"] = labels
        answers[f"q-{question_id}"] = labels
    return answers


def normalize_quiz_ids(text: str, question_map: dict[str, str]) -> tuple[str, int]:
    count = 0

    def replace_section(match: re.Match[str]) -> str:
        nonlocal count
        number = match.group("number")
        question_id = question_map.get(number)
        if not question_id:
            return match.group(0)
        old_body = match.group("body")
        new_body, replacements = re.subn(
            rf"(?m)^id:\s*q-{re.escape(number)}\s*$",
            f"id: ma-{question_id}",
            old_body,
            count=1,
        )
        count += replacements
        return match.group("head") + new_body

    return QUESTION_SECTION_RE.sub(replace_section, text), count


def labels_from_body(body: str) -> set[str]:
    labels: set[str] = set()
    current_label: str | None = None
    for line in body.splitlines():
        option_match = re.match(r"^- id: (?P<label>[a-z])\s*$", line)
        if option_match:
            current_label = option_match.group("label")
            continue
        if line.strip() == "correct: true" and current_label:
            labels.add(current_label)
    return labels


def quiz_id_from_body(body: str, question_number: str | None, question_map: dict[str, str]) -> str | None:
    id_match = QUIZ_ID_RE.search(body)
    raw_id = id_match.group("id").strip() if id_match else ""
    id_match = QUESTION_ID_RE.match(raw_id)
    if id_match and raw_id.lower().startswith("ma-"):
        return id_match.group("id")
    if id_match and raw_id.lower().startswith("q-"):
        raw_number = id_match.group("id")
        return question_map.get(raw_number if question_number is None else question_number)
    if id_match and raw_id.isdigit():
        return id_match.group("id")
    if question_number:
        return question_map.get(question_number)
    return None


def mark_quiz_body(body: str, correct_labels: set[str]) -> str:
    lines = []
    for line in body.splitlines():
        if line.startswith("# MA_ANSWER_MISSING:"):
            continue
        if line.strip() == "correct: true":
            continue
        lines.append(line)

    output: list[str] = []
    current_label: str | None = None
    inserted: set[str] = set()
    for line in lines:
        option_match = re.match(r"^- id: (?P<label>[a-z])\s*$", line)
        if option_match and current_label in correct_labels and current_label not in inserted:
            output.append("  correct: true")
            inserted.add(current_label)
        if option_match:
            current_label = option_match.group("label")
        output.append(line)

    if current_label in correct_labels and current_label not in inserted:
        output.append("  correct: true")
        inserted.add(current_label)

    if correct_labels - inserted:
        return body
    return "\n".join(output)


def propagate_known_answers(
    text: str,
    question_map: dict[str, str],
    known_answers: dict[str, set[str]],
) -> tuple[str, int]:
    count = 0

    def replace_section(match: re.Match[str]) -> str:
        nonlocal count
        question_number = match.group("number")
        section_body = match.group("body")

        def replace_quiz(quiz_match: re.Match[str]) -> str:
            nonlocal count
            body = quiz_match.group("body")
            if "MA_ANSWER_MISSING" not in body or "correct: true" in body:
                return quiz_match.group(0)
            question_id = quiz_id_from_body(body, question_number, question_map)
            labels = known_answers.get(question_id or "") or known_answers.get(question_number)
            if not labels:
                return quiz_match.group(0)
            new_body = mark_quiz_body(body, labels)
            if new_body == body:
                return quiz_match.group(0)
            count += 1
            return "```quiz\n" + new_body + "\n```"

        return match.group("head") + QUIZ_BLOCK_RE.sub(replace_quiz, section_body)

    return QUESTION_SECTION_RE.sub(replace_section, text), count


def trim_blank_edges(lines: list[str]) -> list[str]:
    start = 0
    end = len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def repair_partial_quiz_tails(text: str, converter) -> tuple[str, int]:
    """Fold raw choices left after a partial quiz conversion back into the quiz."""

    repairs = 0

    def replace_section(match: re.Match[str]) -> str:
        nonlocal repairs
        section_body = match.group("body")

        def replace_quiz(quiz_match: re.Match[str]) -> str:
            nonlocal repairs
            body = quiz_match.group("body")
            tail = section_body[quiz_match.end() :]
            first_choice_index = next(
                (
                    index
                    for index, line in enumerate(tail.splitlines())
                    if converter.CHOICE_RE.match(line)
                ),
                None,
            )
            if first_choice_index is None:
                return quiz_match.group(0)

            tail_lines = tail.splitlines()
            previous_option_continuation = trim_blank_edges(tail_lines[:first_choice_index])
            parsed = converter.parse_choices(tail_lines[first_choice_index:])
            if parsed is None:
                return quiz_match.group(0)
            _, choices, remaining_tail = parsed
            if not choices:
                return quiz_match.group(0)

            existing_labels = set(OPTION_ID_RE.findall(body))
            if any(choice.label in existing_labels for choice in choices):
                return quiz_match.group(0)

            body_lines = body.splitlines()
            body_lines = trim_blank_edges(body_lines)
            for line in previous_option_continuation:
                body_lines.append(f"    {line}" if line else "")
            for choice in choices:
                body_lines.append(f"- id: {choice.label}")
                body_lines.extend(converter.block_scalar("content", choice.content, indent="  "))

            repairs += 1
            repaired_tail = "\n".join(remaining_tail)
            if repaired_tail:
                return "```quiz\n" + "\n".join(body_lines) + "\n```\n" + repaired_tail
            return "```quiz\n" + "\n".join(body_lines) + "\n```\n"

        # Only the final quiz in a question can have a tail of stray options.
        quiz_matches = list(QUIZ_BLOCK_RE.finditer(section_body))
        if not quiz_matches:
            return match.group(0)
        last_quiz = quiz_matches[-1]
        replaced = replace_quiz(last_quiz)
        if replaced == last_quiz.group(0):
            return match.group(0)
        new_body = section_body[: last_quiz.start()] + replaced
        return match.group("head") + new_body

    return QUESTION_SECTION_RE.sub(replace_section, text), repairs


def collect_quiz_state(
    text: str,
    question_map: dict[str, str],
) -> tuple[set[str], set[str], set[str]]:
    missing: set[str] = set()
    verified: set[str] = set()
    unresolved: set[str] = set()

    def inspect_section(match: re.Match[str]) -> str:
        question_number = match.group("number")
        for quiz_match in QUIZ_BLOCK_RE.finditer(match.group("body")):
            body = quiz_match.group("body")
            type_match = QUIZ_TYPE_RE.search(body)
            if type_match and type_match.group("type") != "radio":
                continue
            question_id = quiz_id_from_body(body, question_number, question_map)
            if not question_id:
                unresolved.add(question_number)
                continue
            correct_labels = labels_from_body(body)
            if "MA_ANSWER_MISSING" in body:
                missing.add(question_id)
            elif len(correct_labels) == 1:
                verified.add(question_id)
        return match.group(0)

    QUESTION_SECTION_RE.sub(inspect_section, text)
    return missing, verified, unresolved


def append_course(existing: str, course: str) -> str:
    values = [value for value in existing.split(";") if value]
    if course not in values:
        values.append(course)
    return ";".join(values)


def update_ledgers(
    question_fields: list[str],
    question_rows: list[dict[str, str]],
    missing_updates: dict[tuple[str, str], set[str]],
    verified_course_updates: dict[tuple[str, str], set[str]],
    dry_run: bool,
) -> tuple[int, int]:
    question_by_key = {(row["topic-id"], row["question-id"]): row for row in question_rows}
    needs_answer_rows = 0
    course_only_rows = 0

    for key, courses in missing_updates.items():
        row = question_by_key.get(key)
        if not row or row.get("question-type") != "multiple-choice":
            continue
        if row.get("quiz-status") == "converted-and-verified":
            continue
        before = dict(row)
        row["quiz-block-format"] = "obsidian-quiz-blocks"
        row["quiz-block-type"] = "radio"
        row["quiz-status"] = "needs-answer"
        row["quiz-answer-labels"] = ""
        row["quiz-answer-source"] = ""
        row["quiz-answer-rule"] = ""
        for course in sorted(courses):
            row["quiz-updated-courses"] = append_course(row.get("quiz-updated-courses", ""), course)
        if row != before:
            needs_answer_rows += 1

    for key, courses in verified_course_updates.items():
        row = question_by_key.get(key)
        if not row or row.get("question-type") != "multiple-choice":
            continue
        if row.get("quiz-status") != "converted-and-verified":
            continue
        before = dict(row)
        row["quiz-block-format"] = "obsidian-quiz-blocks"
        row["quiz-block-type"] = "radio"
        for course in sorted(courses):
            row["quiz-updated-courses"] = append_course(row.get("quiz-updated-courses", ""), course)
        if row != before:
            course_only_rows += 1

    if not dry_run:
        write_csv(MA_ROOT / "questions.csv", question_fields, question_rows)
        for group_dir in sorted(path for path in MA_ROOT.iterdir() if path.is_dir()):
            group_questions = group_dir / "questions.csv"
            group_catalog = group_dir / "catalog.csv"
            if not group_questions.exists() or not group_catalog.exists():
                continue
            _, group_catalog_rows = read_csv(group_catalog)
            topic_ids = {row["topic-id"] for row in group_catalog_rows}
            write_csv(
                group_questions,
                question_fields,
                [row for row in question_rows if row.get("topic-id") in topic_ids],
            )

    return needs_answer_rows, course_only_rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Mass-convert imported MA MCQs and update ledgers.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, help="Only inspect the first N catalog lesson paths.")
    parser.add_argument("--path", action="append", type=Path, help="Restrict to a lesson file or directory.")
    args = parser.parse_args(argv)

    converter = load_converter()
    catalog = load_catalog()
    question_fields, question_rows, question_by_key = load_question_ledgers()

    selected_paths = sorted(catalog)
    if args.path:
        roots = [path.resolve() for path in args.path]
        selected_paths = [
            path
            for path in selected_paths
            if any(path.resolve() == root or root in path.resolve().parents for root in roots)
        ]
    if args.limit is not None:
        selected_paths = selected_paths[: args.limit]

    total = FileStats()
    changed_files: list[Path] = []
    missing_updates: dict[tuple[str, str], set[str]] = defaultdict(set)
    verified_course_updates: dict[tuple[str, str], set[str]] = defaultdict(set)

    for lesson_path in selected_paths:
        entries = catalog[lesson_path]
        if not lesson_path.exists():
            continue
        topic_ids = {entry.topic_id for entry in entries}
        if len(topic_ids) != 1:
            print(f"Skipping ambiguous lesson path with multiple topics: {lesson_path}", file=sys.stderr)
            continue
        entry = entries[0]
        question_map = load_source_question_map(entry.source_path)
        known_answers = answer_labels_by_question(entry.topic_id, question_map, question_by_key)

        original = lesson_path.read_text(encoding="utf-8")
        converted, conversions = converter.convert_markdown(original, known_answers, "radio")
        converted, repaired = repair_partial_quiz_tails(converted, converter)
        converted, normalized = normalize_quiz_ids(converted, question_map)
        converted, propagated = propagate_known_answers(converted, question_map, known_answers)
        missing, verified, unresolved = collect_quiz_state(converted, question_map)

        stats = FileStats(
            converted_raw=len(conversions),
            repaired_partial=repaired,
            normalized_ids=normalized,
            propagated_answers=propagated,
            missing_blocks=len(missing),
            verified_blocks=len(verified),
            unresolved_ids=len(unresolved),
            changed=converted != original,
        )

        for question_id in missing:
            for catalog_entry in entries:
                missing_updates[(catalog_entry.topic_id, question_id)].add(catalog_entry.course)
        for question_id in verified:
            for catalog_entry in entries:
                verified_course_updates[(catalog_entry.topic_id, question_id)].add(catalog_entry.course)

        total.converted_raw += stats.converted_raw
        total.repaired_partial += stats.repaired_partial
        total.normalized_ids += stats.normalized_ids
        total.propagated_answers += stats.propagated_answers
        total.missing_blocks += stats.missing_blocks
        total.verified_blocks += stats.verified_blocks
        total.unresolved_ids += stats.unresolved_ids
        if stats.changed:
            total.changed = True
            changed_files.append(lesson_path)
            if not args.dry_run:
                lesson_path.write_text(converted, encoding="utf-8")

    needs_rows, verified_course_rows = update_ledgers(
        question_fields,
        question_rows,
        missing_updates,
        verified_course_updates,
        args.dry_run,
    )

    action = "Would update" if args.dry_run else "Updated"
    print(f"{action} {len(changed_files)} lesson file(s).")
    print(f"Raw questions converted: {total.converted_raw}")
    print(f"Partial quiz tails repaired: {total.repaired_partial}")
    print(f"Quiz ids normalized from q-N to ma-id: {total.normalized_ids}")
    print(f"Known answers propagated into missing blocks: {total.propagated_answers}")
    print(f"Missing-answer quiz blocks seen: {total.missing_blocks}")
    print(f"Verified radio quiz blocks seen: {total.verified_blocks}")
    print(f"Unresolved quiz ids seen: {total.unresolved_ids}")
    print(f"Ledger rows set/kept as needs-answer: {needs_rows}")
    print(f"Verified ledger rows with course provenance updated: {verified_course_rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
