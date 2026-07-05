#!/usr/bin/env python3
"""Mark correct answers in existing obsidian-quiz-blocks fences."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


QUIZ_BLOCK_RE = re.compile(r"```quiz\n(?P<body>.*?)\n```", re.DOTALL)
QUIZ_ID_RE = re.compile(r"^id:\s*(?P<id>\S+)\s*$", re.MULTILINE)
OPTION_ID_RE = re.compile(r"^- id: (?P<label>[a-z])\s*$")
ANSWER_SPLIT_RE = re.compile(r"[\s,+/|]+")


@dataclass(frozen=True)
class Change:
    path: str
    quiz_id: str
    correct_labels: list[str]


def normalize_id(value: str) -> str:
    text = value.strip().lower()
    if text.startswith("ma-"):
        return text
    if text.isdigit():
        return f"ma-{text}"
    return text


def parse_labels(value: object) -> list[str]:
    if isinstance(value, str):
        pieces = ANSWER_SPLIT_RE.split(value)
    elif isinstance(value, list):
        pieces = [str(piece) for piece in value]
    else:
        pieces = [str(value)]
    labels = sorted({piece.strip().lower() for piece in pieces if piece.strip()})
    if not labels or any(not re.fullmatch(r"[a-z]", label) for label in labels):
        raise ValueError(f"Invalid answer labels: {value!r}")
    return labels


def parse_answers(raw_answers: list[str], answer_key_file: Path | None) -> dict[str, list[str]]:
    answers: dict[str, list[str]] = {}
    if answer_key_file:
        payload = json.loads(answer_key_file.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("--answer-key-file must contain a JSON object")
        for key, value in payload.items():
            answers[normalize_id(str(key))] = parse_labels(value)

    for raw_answer in raw_answers:
        if "=" in raw_answer:
            key, value = raw_answer.split("=", 1)
        elif ":" in raw_answer:
            key, value = raw_answer.split(":", 1)
        else:
            raise ValueError(f"Invalid --answer {raw_answer!r}; use QUIZ_ID=LABELS")
        answers[normalize_id(key)] = parse_labels(value)
    return answers


def mark_body(body: str, correct_labels: set[str]) -> str:
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
        option_match = OPTION_ID_RE.match(line)
        if option_match and current_label in correct_labels and current_label not in inserted:
            output.append("  correct: true")
            inserted.add(current_label)
        if option_match:
            current_label = option_match.group("label")
        output.append(line)

    if current_label in correct_labels and current_label not in inserted:
        output.append("  correct: true")
        inserted.add(current_label)

    missing = correct_labels - inserted
    if missing:
        raise ValueError(f"Answer label(s) not found in quiz options: {','.join(sorted(missing))}")

    return "\n".join(output)


def mark_file(path: Path, answers: dict[str, list[str]]) -> tuple[str, list[Change]]:
    original = path.read_text(encoding="utf-8")
    changes: list[Change] = []

    def replace(match: re.Match[str]) -> str:
        body = match.group("body")
        id_match = QUIZ_ID_RE.search(body)
        if not id_match:
            return match.group(0)
        quiz_id = normalize_id(id_match.group("id"))
        if quiz_id not in answers:
            return match.group(0)
        labels = answers[quiz_id]
        new_body = mark_body(body, set(labels))
        if new_body != body:
            changes.append(Change(path=path.as_posix(), quiz_id=quiz_id, correct_labels=labels))
        return "```quiz\n" + new_body + "\n```"

    return QUIZ_BLOCK_RE.sub(replace, original), changes


def expand_paths(paths: list[Path]) -> list[Path]:
    markdown_files: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        if path.is_dir():
            candidates = sorted(path.glob("**/Lessons/*.md")) or sorted(path.rglob("*.md"))
        else:
            candidates = [path]
        for candidate in candidates:
            resolved = candidate.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            markdown_files.append(candidate)
    return markdown_files


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Mark correct answers in existing quiz blocks.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--answer", action="append", default=[], metavar="QUIZ_ID=LABELS")
    parser.add_argument("--answer-key-file", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report-json", type=Path)
    parser.add_argument("--summary-only", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    answers = parse_answers(args.answer, args.answer_key_file)
    if not answers:
        raise ValueError("No answers provided")

    all_changes: list[Change] = []
    for path in expand_paths(args.paths):
        marked, changes = mark_file(path, answers)
        if not changes:
            continue
        all_changes.extend(changes)
        if not args.summary_only:
            print(f"{path}: {len(changes)} quiz answer(s)")
            for change in changes:
                print(f"  {change.quiz_id}: {','.join(change.correct_labels)}")
        if not args.dry_run:
            path.write_text(marked, encoding="utf-8")

    if args.report_json:
        args.report_json.write_text(
            json.dumps([asdict(change) for change in all_changes], indent=2) + "\n",
            encoding="utf-8",
        )

    action = "Would mark" if args.dry_run else "Marked"
    print(f"{action} {len(all_changes)} quiz answer(s) across {len({c.path for c in all_changes})} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
