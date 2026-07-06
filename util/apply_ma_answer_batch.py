#!/usr/bin/env python3
"""Apply manually solved MA quiz answers from the missing-answer queue."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
from collections import defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MA_ROOT = REPO_ROOT / "vault" / "MA"
QUEUE_PATH = REPO_ROOT / "util" / "ma_missing_answer_queue.csv"
MARK_SCRIPT_PATH = REPO_ROOT / "util" / "mark_quiz_answers.py"


def load_marker():
    spec = importlib.util.spec_from_file_location("mark_quiz_answers", MARK_SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {MARK_SCRIPT_PATH}")
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


def parse_answer(raw: str) -> tuple[tuple[str, str], str]:
    if "=" not in raw:
        raise ValueError(f"Invalid --answer {raw!r}; use TOPIC_ID:QUESTION_ID=LABEL")
    key_raw, label = raw.split("=", 1)
    if ":" not in key_raw:
        raise ValueError(f"Invalid --answer {raw!r}; use TOPIC_ID:QUESTION_ID=LABEL")
    topic_id, question_id = key_raw.split(":", 1)
    label = label.strip().lower()
    if not re.fullmatch(r"[a-z]", label):
        raise ValueError(f"Invalid answer label in {raw!r}")
    return (topic_id.strip(), question_id.strip()), label


def append_courses(existing: str, courses: set[str]) -> str:
    values = [value for value in existing.split(";") if value]
    for course in sorted(courses):
        if course not in values:
            values.append(course)
    return ";".join(values)


def resolve_lesson_path(raw: str) -> Path:
    path = Path(raw)
    return path if path.is_absolute() else REPO_ROOT / path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Apply solved MA quiz answers.")
    parser.add_argument("--answer", action="append", default=[], metavar="TOPIC_ID:QUESTION_ID=LABEL")
    parser.add_argument("--queue", type=Path, default=QUEUE_PATH)
    parser.add_argument("--source", choices=("manual", "image-id"), default="manual")
    parser.add_argument("--rule", default="label")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    answers = dict(parse_answer(raw) for raw in args.answer)
    if not answers:
        raise ValueError("No --answer values provided")

    marker = load_marker()
    _, queue_rows = read_csv(args.queue)
    by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in queue_rows:
        by_key[(row["topic-id"], row["question-id"])].append(row)

    paths_to_answers: dict[Path, dict[str, list[str]]] = defaultdict(dict)
    courses_by_key: dict[tuple[str, str], set[str]] = defaultdict(set)
    missing_keys: list[tuple[str, str]] = []

    for key, label in answers.items():
        rows = by_key.get(key)
        if not rows:
            missing_keys.append(key)
            continue
        for row in rows:
            lesson_path = resolve_lesson_path(row["lesson-path"])
            paths_to_answers[lesson_path][f"ma-{key[1]}"] = [label]
            courses_by_key[key].add(row["course"])

    all_changes = []
    for path, file_answers in sorted(paths_to_answers.items()):
        marked, changes = marker.mark_file(path, file_answers)
        all_changes.extend(changes)
        if changes and not args.dry_run:
            path.write_text(marked, encoding="utf-8")

    question_fields, question_rows = read_csv(MA_ROOT / "questions.csv")
    by_question_key = {(row["topic-id"], row["question-id"]): row for row in question_rows}
    ledger_changed = 0
    for key, label in answers.items():
        row = by_question_key.get(key)
        if not row:
            missing_keys.append(key)
            continue
        before = dict(row)
        row["quiz-block-format"] = "obsidian-quiz-blocks"
        row["quiz-block-type"] = "radio"
        row["quiz-answer-labels"] = label
        row["quiz-updated-courses"] = append_courses(row.get("quiz-updated-courses", ""), courses_by_key[key])
        row["quiz-status"] = "converted-and-verified"
        row["quiz-answer-source"] = args.source
        row["quiz-answer-rule"] = args.rule
        if row != before:
            ledger_changed += 1

    if not args.dry_run:
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

    action = "Would mark" if args.dry_run else "Marked"
    print(f"{action} {len(all_changes)} quiz block(s) across {len(paths_to_answers)} file(s).")
    print(f"Ledger rows changed: {ledger_changed}")
    if missing_keys:
        print(f"Missing queue/ledger keys: {sorted(set(missing_keys))[:20]} (count {len(set(missing_keys))})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
