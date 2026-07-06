#!/usr/bin/env python3
"""Build a CSV queue of MA quiz blocks that still need answers."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MA_ROOT = REPO_ROOT / "vault" / "MA"
MASS_SCRIPT_PATH = REPO_ROOT / "util" / "mass_convert_ma_mcqs.py"
SKIP_PATH = REPO_ROOT / "util" / "ma_answer_skips.csv"

QUESTION_SECTION_RE = re.compile(
    r"(?P<head>^\*\*Question\s+(?P<number>\d+):?\*\*.*?$)(?P<body>.*?)(?=^\*\*Question\s+\d+:?\*\*|^---\s*$|\Z)",
    re.MULTILINE | re.DOTALL | re.IGNORECASE,
)
QUIZ_BLOCK_RE = re.compile(r"```quiz\n(?P<body>.*?)\n```", re.DOTALL)
QUIZ_ID_RE = re.compile(r"^id:\s*(?P<id>\S+)\s*$", re.MULTILINE)
IMAGE_LINK_RE = re.compile(r"!\[[^\]]*\]\(<(?P<path>[^>]+)>\)")


FIELDS = [
    "topic-id",
    "topic-code",
    "course",
    "question-number",
    "question-id",
    "lesson-path",
    "source-path",
    "prompt",
    "options-json",
    "image-paths-json",
]


def load_mass_helpers():
    spec = importlib.util.spec_from_file_location("mass_convert_ma_mcqs", MASS_SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {MASS_SCRIPT_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_skipped_answers(path: Path) -> set[tuple[str, str]]:
    if not path.exists():
        return set()
    return {
        (row["topic-id"], row["question-id"])
        for row in read_csv(path)
        if row.get("topic-id") and row.get("question-id")
    }


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def parse_block_scalar(lines: list[str], start_index: int, content_indent: str) -> tuple[str, int]:
    content: list[str] = []
    index = start_index
    while index < len(lines):
        line = lines[index]
        if line.startswith(content_indent):
            content.append(line[len(content_indent) :])
            index += 1
            continue
        if not line.strip():
            content.append("")
            index += 1
            continue
        break
    while content and not content[0].strip():
        content.pop(0)
    while content and not content[-1].strip():
        content.pop()
    return "\n".join(content), index


def parse_quiz_body(body: str) -> tuple[str, list[dict[str, str]]]:
    lines = body.splitlines()
    prompt = ""
    options: list[dict[str, str]] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if line == "content: |-":
            prompt, index = parse_block_scalar(lines, index + 1, "  ")
            continue
        if line.startswith("- id: "):
            label = line.split(":", 1)[1].strip()
            index += 1
            content = ""
            while index < len(lines):
                if lines[index] == "  content: |-":
                    content, index = parse_block_scalar(lines, index + 1, "    ")
                    break
                if lines[index].startswith("- id: "):
                    break
                index += 1
            options.append({"id": label, "content": content})
            continue
        index += 1
    return prompt, options


def resolve_image_path(raw: str, lesson_path: Path) -> str:
    if raw.startswith("http://") or raw.startswith("https://"):
        return raw
    path = Path(raw)
    if path.is_absolute():
        return path.as_posix()
    if raw.startswith("MA/"):
        return (MA_ROOT.parent / path).resolve().as_posix()
    return (lesson_path.parent / path).resolve().as_posix()


def image_paths_from_text(text: str, lesson_path: Path) -> list[str]:
    paths: list[str] = []
    for match in IMAGE_LINK_RE.finditer(text):
        resolved = resolve_image_path(match.group("path"), lesson_path)
        if resolved not in paths:
            paths.append(resolved)
    return paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build MA missing-answer queue CSV.")
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "util" / "ma_missing_answer_queue.csv",
    )
    parser.add_argument(
        "--include-skips",
        action="store_true",
        help="Include questions documented in util/ma_answer_skips.csv.",
    )
    args = parser.parse_args(argv)

    mass = load_mass_helpers()
    catalog = mass.load_catalog()
    skipped_answers = set() if args.include_skips else load_skipped_answers(SKIP_PATH)
    question_rows = {
        (row["topic-id"], row["question-id"]): row
        for row in read_csv(MA_ROOT / "questions.csv")
    }

    rows: list[dict[str, str]] = []
    skipped_rows = 0
    for lesson_path, entries in sorted(catalog.items()):
        if not lesson_path.exists():
            continue
        topic_ids = {entry.topic_id for entry in entries}
        if len(topic_ids) != 1:
            continue
        entry = entries[0]
        question_map = mass.load_source_question_map(entry.source_path)
        text = lesson_path.read_text(encoding="utf-8")
        for section in QUESTION_SECTION_RE.finditer(text):
            question_number = section.group("number")
            for quiz in QUIZ_BLOCK_RE.finditer(section.group("body")):
                body = quiz.group("body")
                if "MA_ANSWER_MISSING" not in body:
                    continue
                question_id = mass.quiz_id_from_body(body, question_number, question_map)
                if not question_id:
                    continue
                if (entry.topic_id, question_id) in skipped_answers:
                    skipped_rows += 1
                    continue
                ledger_row = question_rows.get((entry.topic_id, question_id))
                if not ledger_row or ledger_row.get("question-type") != "multiple-choice":
                    continue
                prompt, options = parse_quiz_body(body)
                image_paths = image_paths_from_text(prompt, lesson_path)
                for option in options:
                    for image_path in image_paths_from_text(option["content"], lesson_path):
                        if image_path not in image_paths:
                            image_paths.append(image_path)
                rows.append(
                    {
                        "topic-id": entry.topic_id,
                        "topic-code": entry.topic_code,
                        "course": entry.course,
                        "question-number": question_number,
                        "question-id": question_id,
                        "lesson-path": rel(lesson_path),
                        "source-path": rel(entry.source_path) if entry.source_path else "",
                        "prompt": prompt,
                        "options-json": json.dumps(options, ensure_ascii=False),
                        "image-paths-json": json.dumps(image_paths, ensure_ascii=False),
                    }
                )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    unique = {(row["topic-id"], row["question-id"]) for row in rows}
    print(f"Wrote {len(rows)} queue rows to {args.output}")
    print(f"Unique topic/question pairs: {len(unique)}")
    if skipped_rows:
        print(f"Excluded documented skip rows: {skipped_rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
