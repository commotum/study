#!/usr/bin/env python3
"""Refresh ledger metadata for repaired, physically imported MA questions.

Archival rows with no source JSON below ``vault/MA`` are deliberately left
unchanged.  Group question ledgers are synchronized from the global ledger
without rebuilding unrelated catalog files.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from copy import deepcopy
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MA_ROOT = REPO_ROOT / "vault" / "MA"
GLOBAL_LEDGER = MA_ROOT / "questions.csv"
FREE_MANIFEST = REPO_ROOT / "util" / "ma_imported_free_response_manifest.csv"
FREE_ANSWERS = REPO_ROOT / "util" / "ma_free_response_answer_key.csv"
OTHER_REPAIRS = REPO_ROOT / "util" / "ma_missing_answer_repairs.json"
QUIZ_RE = re.compile(r"```quiz\n(?P<body>.*?)\n```", re.DOTALL)
LESSON_ID_RE = re.compile(r"^lesson-id:\s*(?P<id>\d+)\s*$", re.MULTILINE)
QUIZ_ID_RE = re.compile(r"^id:\s*ma-(?P<id>\d+)(?:-select-\d+)?\s*$", re.MULTILINE)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def imported_source_keys() -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    for path in MA_ROOT.rglob("*.json"):
        if path.name == "_image_meta.json" or not path.name[:1].isdigit():
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for item in payload.get("lesson", {}).get("items", []):
            if not isinstance(item, dict) or item.get("question_id") is None:
                continue
            topic_id = path.stem
            keys.add((topic_id, str(item["question_id"])))
    return keys


def current_courses() -> dict[tuple[str, str], set[str]]:
    result: dict[tuple[str, str], set[str]] = defaultdict(set)
    for path in MA_ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        lesson_match = LESSON_ID_RE.search(text)
        if not lesson_match:
            continue
        topic_id = lesson_match.group("id")
        relative_parts = path.relative_to(MA_ROOT).parts
        if len(relative_parts) < 2:
            continue
        course = relative_parts[1]
        for quiz in QUIZ_RE.finditer(text):
            id_match = QUIZ_ID_RE.search(quiz.group("body"))
            if id_match:
                result[(topic_id, id_match.group("id"))].add(course)
    return result


def base_repair_rows() -> dict[tuple[str, str], dict[str, object]]:
    payload = json.loads(OTHER_REPAIRS.read_text(encoding="utf-8"))
    grouped: dict[tuple[str, str], dict[str, object]] = {}
    for raw_key, entry in payload.items():
        topic_id, raw_id = raw_key.split(":", 1)
        match = re.fullmatch(r"ma-(?P<id>\d+)(?:-select-(?P<select>\d+))?", raw_id)
        if not match:
            raise ValueError(f"Invalid repair quiz id: {raw_id}")
        key = (topic_id, match.group("id"))
        row = grouped.setdefault(
            key,
            {
                "types": set(),
                "labels": [],
                "sources": set(),
            },
        )
        row["types"].add(entry["type"])
        if entry["type"] == "radio":
            row["labels"].append((0, str(entry["correct"])))
        else:
            row["labels"].append((int(match.group("select")), str(entry["correct_option"])))
        source = (
            "manual-mathematical-repair"
            if entry.get("add_option") is not None or entry.get("content_new") is not None
            else "manual-solution"
        )
        row["sources"].add(source)
    return grouped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    fields, original_rows = read_csv(GLOBAL_LEDGER)
    rows = deepcopy(original_rows)
    by_key = {(row["topic-id"], row["question-id"]): row for row in rows}
    if len(by_key) != len(rows):
        raise ValueError("Global question ledger contains duplicate keys")

    imported = imported_source_keys()
    missing_imported = imported - set(by_key)
    if missing_imported:
        raise ValueError(f"Imported questions absent from global ledger: {len(missing_imported)}")
    archival = set(by_key) - imported
    archival_before = {key: deepcopy(by_key[key]) for key in archival}
    courses = current_courses()

    _, manifest_rows = read_csv(FREE_MANIFEST)
    _, answer_rows = read_csv(FREE_ANSWERS)
    answer_by_key = {
        (row["topic-id"], row["question-id"]): row for row in answer_rows
    }
    free_keys: set[tuple[str, str]] = set()
    for manifest_row in manifest_rows:
        key = (manifest_row["topic-id"], manifest_row["question-id"])
        free_keys.add(key)
        ledger_row = by_key.get(key)
        answer_row = answer_by_key.get(key)
        if ledger_row is None or answer_row is None:
            raise ValueError(f"Free-response registry key is absent from ledger/answers: {key}")
        if key not in imported or ledger_row["question-type"] != "free-response":
            raise ValueError(f"Refusing non-imported/non-free ledger update: {key}")
        ledger_row.update(
            {
                "quiz-block-format": "obsidian-quiz-blocks",
                "quiz-block-type": "blank",
                "quiz-answer-labels": "",
                "quiz-updated-courses": ";".join(sorted(courses[key])),
                "quiz-status": "converted-and-verified",
                "quiz-answer-source": answer_row["answer-source"],
                "quiz-answer-rule": "exact-match",
            }
        )

    repair_groups = base_repair_rows()
    for key, repair in repair_groups.items():
        ledger_row = by_key.get(key)
        if ledger_row is None or key not in imported:
            raise ValueError(f"Repair key is absent from imported ledger rows: {key}")
        types = set(repair["types"])
        if len(types) != 1:
            raise ValueError(f"Mixed repair block types for {key}: {types}")
        block_type = next(iter(types))
        labels = ";".join(label for _, label in sorted(repair["labels"]))
        sources = set(repair["sources"])
        answer_source = (
            "manual-mathematical-repair"
            if "manual-mathematical-repair" in sources
            else "manual-solution"
        )
        ledger_row.update(
            {
                "quiz-block-format": "obsidian-quiz-blocks",
                "quiz-block-type": block_type,
                "quiz-answer-labels": labels,
                "quiz-updated-courses": ";".join(sorted(courses[key])),
                "quiz-status": "converted-and-verified",
                "quiz-answer-source": answer_source,
                "quiz-answer-rule": "label" if block_type == "radio" else "correct-option",
            }
        )

    if free_keys & set(repair_groups):
        raise ValueError("Free-response and non-free repair registries overlap")
    if {key: by_key[key] for key in archival} != archival_before:
        raise ValueError("An archival/unimported ledger row changed")

    group_outputs: dict[Path, tuple[list[str], list[dict[str, str]]]] = {}
    for group_ledger in sorted(MA_ROOT.glob("*/questions.csv")):
        group_fields, group_rows = read_csv(group_ledger)
        if group_fields != fields:
            raise ValueError(f"Group ledger fields differ: {group_ledger}")
        updated_group: list[dict[str, str]] = []
        for group_row in group_rows:
            key = (group_row["topic-id"], group_row["question-id"])
            if key not in by_key:
                raise ValueError(f"Group row absent from global ledger: {key}")
            updated_group.append(deepcopy(by_key[key]))
        group_outputs[group_ledger] = (group_fields, updated_group)

    changed_global = rows != original_rows
    changed_groups = [
        path
        for path, (_, output_rows) in group_outputs.items()
        if output_rows != read_csv(path)[1]
    ]
    if args.write:
        if changed_global:
            write_csv(GLOBAL_LEDGER, fields, rows)
        for path in changed_groups:
            write_csv(path, *group_outputs[path])

    print(f"Physically imported source questions: {len(imported)}")
    print(f"Archival rows preserved: {len(archival)}")
    print(f"Free-response rows refreshed: {len(free_keys)}")
    print(f"Radio/select-list rows refreshed: {len(repair_groups)}")
    print(f"Global ledger {'changed' if args.write else 'would change'}: {int(changed_global)}")
    print(f"Group ledgers {'changed' if args.write else 'that would change'}: {len(changed_groups)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
