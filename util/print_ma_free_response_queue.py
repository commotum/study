#!/usr/bin/env python3
"""Print a compact, deterministic slice of the imported MA solve queue."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

from repair_course_free_response_quizzes import QUIZ_ID_RE, QUIZ_RE


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / "util" / "ma_imported_free_response_manifest.csv"
MANUAL = REPO_ROOT / "util" / "ma_free_response_manual_answers.json"


def quiz_body(row: dict[str, str]) -> str:
    path = REPO_ROOT / row["canonical-placements"].split(";", 1)[0]
    text = path.read_text(encoding="utf-8")
    for match in QUIZ_RE.finditer(text):
        id_match = QUIZ_ID_RE.search(match.group("body"))
        if id_match and re.sub(r"^(?:ma-|q-)", "", id_match.group("id")) == row["question-id"]:
            return match.group("body")
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1, help="One-based position in the unresolved queue")
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--include-solved", action="store_true")
    args = parser.parse_args()

    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    manual = json.loads(MANUAL.read_text(encoding="utf-8")) if MANUAL.exists() else {}
    queue = [row for row in rows if row["seed-state"] == "solve-required"]
    if not args.include_solved:
        queue = [row for row in queue if f"{row['topic-id']}:{row['question-id']}" not in manual]
    selected = queue[args.start - 1 : args.start - 1 + args.count]
    for position, row in enumerate(selected, start=args.start):
        key = f"{row['topic-id']}:{row['question-id']}"
        print(
            f"=== unresolved {position}/{len(queue)} | study {row['study-order']} | {key} | "
            f"{row['topic-code']} {row['topic-name']} | blanks={row['source-blank-count']} ==="
        )
        print("SOURCE: " + row["source-prompt"].replace("\n", " / "))
        print(quiz_body(row))
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
