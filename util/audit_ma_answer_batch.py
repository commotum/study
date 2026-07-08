#!/usr/bin/env python3
"""Audit a batch applied by apply_ma_answer_batch.py.

Checks topic-scoped markdown copies from vault/MA/catalog.csv plus global/group
ledgers. Skipped questions are expected to remain unresolved but documented.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


ROOT = Path("vault/MA")
QUEUE = Path("util/ma_missing_answer_queue.csv")
SKIPS = Path("util/ma_answer_skips.csv")


def parse_answer(raw: str) -> tuple[tuple[str, str], str]:
    left, label = raw.split("=", 1)
    topic_id, question_id = left.split(":", 1)
    return (topic_id, question_id), label.lower()


def parse_key(raw: str) -> tuple[str, str]:
    topic_id, question_id = raw.split(":", 1)
    return topic_id, question_id


def read_queue() -> set[tuple[str, str]]:
    with QUEUE.open(newline="") as f:
        return {(r["topic-id"], r["question-id"]) for r in csv.DictReader(f)}


def read_skip_rows() -> set[tuple[str, str]]:
    if not SKIPS.exists():
        return set()
    with SKIPS.open(newline="") as f:
        return {(r["topic-id"], r["question-id"]) for r in csv.DictReader(f)}


def catalog_paths(topic_ids: set[str]) -> dict[str, list[Path]]:
    paths = {topic_id: [] for topic_id in topic_ids}
    with (ROOT / "catalog.csv").open(newline="") as f:
        for row in csv.DictReader(f):
            topic_id = row["topic-id"]
            lesson_path = row.get("lesson-path") or ""
            if topic_id not in paths or not lesson_path:
                continue
            path = Path(lesson_path)
            if not path.is_absolute():
                path = Path.cwd() / path
            paths[topic_id].append(path)
    return paths


def quiz_block(text: str, question_id: str) -> str | None:
    needle = f"id: ma-{question_id}"
    pos = text.find(needle)
    if pos < 0:
        return None
    start = text.rfind("```quiz", 0, pos)
    end = text.find("```", pos)
    if start < 0 or end < 0:
        return None
    return text[start:end]


def correct_labels(block: str) -> list[str]:
    current: str | None = None
    labels: list[str] = []
    for line in block.splitlines():
        match = re.match(r"\s*- id:\s*([A-Za-z])\s*$", line)
        if match:
            current = match.group(1).lower()
        elif re.match(r"\s*correct:\s*true\s*$", line) and current:
            labels.append(current)
    return labels


def ledger_paths_for(paths_by_topic: dict[str, list[Path]]) -> set[Path]:
    ledgers = {ROOT / "questions.csv"}
    for paths in paths_by_topic.values():
        for path in paths:
            parts = path.parts
            if "MA" not in parts:
                continue
            index = parts.index("MA")
            if index + 1 < len(parts):
                ledgers.add(Path(*parts[: index + 2]) / "questions.csv")
    return ledgers


def audit_markdown(
    answers: dict[tuple[str, str], str],
    skips: set[tuple[str, str]],
    paths_by_topic: dict[str, list[Path]],
) -> tuple[list[str], int]:
    errors: list[str] = []
    block_checks = 0
    for (topic_id, question_id), label in answers.items():
        paths = paths_by_topic.get(topic_id) or []
        if not paths:
            errors.append(f"No catalog lesson paths for topic {topic_id}")
            continue
        for path in paths:
            if not path.exists():
                errors.append(f"Catalog path missing for {topic_id}: {path}")
                continue
            block = quiz_block(path.read_text(errors="ignore"), question_id)
            if block is None:
                errors.append(f"No quiz block for {topic_id}:{question_id} in {path}")
                continue
            block_checks += 1
            if "MA_ANSWER_MISSING" in block:
                errors.append(f"MA_ANSWER_MISSING remains for {topic_id}:{question_id} in {path}")
            labels = correct_labels(block)
            if labels != [label]:
                errors.append(
                    f"Wrong correct labels for {topic_id}:{question_id} in {path}: "
                    f"{labels}, expected {[label]}"
                )
    for topic_id, question_id in skips:
        for path in paths_by_topic.get(topic_id, []):
            if not path.exists():
                errors.append(f"Catalog path missing for skipped {topic_id}: {path}")
                continue
            block = quiz_block(path.read_text(errors="ignore"), question_id)
            if block is None:
                errors.append(f"No skipped quiz block for {topic_id}:{question_id} in {path}")
                continue
            if "MA_ANSWER_MISSING" not in block:
                errors.append(f"Skipped block lacks marker for {topic_id}:{question_id} in {path}")
            if correct_labels(block):
                errors.append(f"Skipped block still has correct label for {topic_id}:{question_id} in {path}")
    return errors, block_checks


def audit_ledgers(
    answers: dict[tuple[str, str], str],
    skips: set[tuple[str, str]],
    ledger_paths: set[Path],
) -> tuple[list[str], int]:
    errors: list[str] = []
    checks = 0
    for path in sorted(ledger_paths):
        if not path.exists():
            continue
        with path.open(newline="") as f:
            for row in csv.DictReader(f):
                key = (row.get("topic-id", ""), row.get("question-id", ""))
                if key in answers:
                    checks += 1
                    expected = {
                        "quiz-block-format": "obsidian-quiz-blocks",
                        "quiz-block-type": "radio",
                        "quiz-answer-labels": answers[key],
                        "quiz-status": "converted-and-verified",
                        "quiz-answer-source": "manual",
                        "quiz-answer-rule": "label",
                    }
                elif key in skips:
                    expected = {
                        "quiz-block-format": "obsidian-quiz-blocks",
                        "quiz-block-type": "radio",
                        "quiz-answer-labels": "",
                        "quiz-status": "needs-answer",
                        "quiz-answer-source": "",
                        "quiz-answer-rule": "",
                    }
                else:
                    continue
                for column, value in expected.items():
                    if row.get(column) != value:
                        errors.append(
                            f"{path} {key} {column}={row.get(column)!r}, expected {value!r}"
                        )
    return errors, checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--answer", action="append", default=[], help="TOPIC:QUESTION=label")
    parser.add_argument("--skip", action="append", default=[], help="TOPIC:QUESTION")
    args = parser.parse_args()

    answers = dict(parse_answer(raw) for raw in args.answer)
    skips = {parse_key(raw) for raw in args.skip}
    queue = read_queue()
    skip_rows = read_skip_rows()
    errors: list[str] = []

    remaining = sorted(set(answers) & queue)
    if remaining:
        errors.append(f"Answered IDs still in queue: {remaining[:20]} total={len(remaining)}")
    skip_remaining = sorted(skips & queue)
    if skip_remaining:
        errors.append(f"Skipped IDs still in queue: {skip_remaining}")
    missing_skip_rows = sorted(skips - skip_rows)
    if missing_skip_rows:
        errors.append(f"Skip rows missing from util/ma_answer_skips.csv: {missing_skip_rows}")

    topic_ids = {topic_id for topic_id, _ in set(answers) | skips}
    paths_by_topic = catalog_paths(topic_ids)
    markdown_errors, block_checks = audit_markdown(answers, skips, paths_by_topic)
    errors.extend(markdown_errors)
    ledger_errors, ledger_checks = audit_ledgers(answers, skips, ledger_paths_for(paths_by_topic))
    errors.extend(ledger_errors)

    if ledger_checks < len(answers) * 2:
        errors.append(f"Only {ledger_checks} answer ledger checks for {len(answers)} answers")

    if errors:
        print("AUDIT FAIL")
        for error in errors[:120]:
            print(f"- {error}")
        if len(errors) > 120:
            print(f"... more errors: {len(errors) - 120}")
        return 1
    print(
        f"AUDIT OK: {len(answers)} ids absent from queue; {len(skips)} skips excluded; "
        f"{block_checks} topic-scoped block checks; {ledger_checks} answer ledger checks"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
