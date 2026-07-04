#!/usr/bin/env python3
"""Convert MA-style Markdown multiple-choice questions into quiz blocks."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


QUESTION_HEADING_RE = re.compile(r"^\*\*Question\s+(?P<number>\d+):?\*\*\s*$", re.IGNORECASE)
SECTION_BREAK_RE = re.compile(r"^---\s*$")
CHOICE_RE = re.compile(r"^\s*-\s+\[(?P<mark>[ xX])\]\s+(?P<label>[A-Za-z])\.\s*(?P<content>.*)$")
QUIZ_FENCE_RE = re.compile(r"^\s*```quiz\s*$")
QUESTION_ID_RE = re.compile(r"\bq-(?P<id>\d+)(?:-a-\d+)?\.(?:png|jpe?g|gif|webp|svg)\b", re.IGNORECASE)
ANSWER_SPLIT_RE = re.compile(r"[\s,+/|]+")

MISSING_ANSWER_COMMENT = (
    "# MA_ANSWER_MISSING: set exactly one options[].correct=true for radio, "
    "or all correct options for checkbox"
)


@dataclass(frozen=True)
class Choice:
    label: str
    content: list[str]
    checked: bool


@dataclass(frozen=True)
class Conversion:
    question_number: str
    quiz_id: str
    start_line: int
    choice_count: int
    correct_labels: tuple[str, ...]


@dataclass(frozen=True)
class ConvertedBlock:
    lines: list[str]
    conversion: Conversion


def trim_blank_edges(lines: list[str]) -> list[str]:
    start = 0
    end = len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def block_scalar(key: str, value_lines: list[str], indent: str = "") -> list[str]:
    lines = [f"{indent}{key}: |-"]
    for line in value_lines or [""]:
        lines.append(f"{indent}  {line}" if line else f"{indent}  ")
    return lines


def detect_question_id(lines: list[str]) -> str | None:
    for line in lines:
        match = QUESTION_ID_RE.search(line)
        if match:
            return match.group("id")
    return None


def parse_answer_value(value: object) -> set[str]:
    if isinstance(value, str):
        pieces = ANSWER_SPLIT_RE.split(value)
    elif isinstance(value, list):
        pieces = [str(piece) for piece in value]
    else:
        pieces = [str(value)]
    return {piece.strip().lower() for piece in pieces if piece.strip()}


def normalize_answer_key(key: object) -> str:
    text = str(key).strip().lower()
    if text.startswith("ma-"):
        text = text[3:]
    return text


def parse_answer_overrides(raw_answers: list[str], answer_key_file: Path | None) -> dict[str, set[str]]:
    answers: dict[str, set[str]] = {}

    if answer_key_file:
        with answer_key_file.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        if not isinstance(payload, dict):
            raise ValueError("--answer-key-file must contain a JSON object")
        for key, value in payload.items():
            answers[normalize_answer_key(key)] = parse_answer_value(value)

    for raw_answer in raw_answers:
        if "=" in raw_answer:
            key, value = raw_answer.split("=", 1)
        elif ":" in raw_answer:
            key, value = raw_answer.split(":", 1)
        else:
            raise ValueError(f"Invalid --answer value {raw_answer!r}; use QUESTION=LABELS")
        labels = parse_answer_value(value)
        if not labels:
            raise ValueError(f"Invalid --answer value {raw_answer!r}; no labels found")
        answers[normalize_answer_key(key)] = labels

    return answers


def answer_labels_for(
    answer_overrides: dict[str, set[str]],
    question_number: str,
    question_id: str | None,
) -> set[str]:
    keys = [normalize_answer_key(question_number), f"q{question_number}"]
    if question_id:
        keys.extend([normalize_answer_key(question_id), f"q-{question_id}", f"q{question_id}"])

    for key in keys:
        if key in answer_overrides:
            return answer_overrides[key]
    return set()


def find_question_end(lines: list[str], start: int) -> int:
    index = start
    while index < len(lines):
        if QUESTION_HEADING_RE.match(lines[index]) or SECTION_BREAK_RE.match(lines[index]):
            return index
        index += 1
    return len(lines)


def parse_choices(block_lines: list[str]) -> tuple[list[str], list[Choice], list[str]] | None:
    first_choice_index = next(
        (index for index, line in enumerate(block_lines) if CHOICE_RE.match(line)),
        None,
    )
    if first_choice_index is None:
        return None

    content_lines = trim_blank_edges(block_lines[:first_choice_index])
    choices: list[Choice] = []
    index = first_choice_index

    while index < len(block_lines):
        if not block_lines[index].strip():
            index += 1
            continue

        match = CHOICE_RE.match(block_lines[index])
        if not match:
            break

        label = match.group("label").lower()
        checked = match.group("mark").lower() == "x"
        choice_lines = [match.group("content").rstrip()]
        index += 1

        while index < len(block_lines):
            if CHOICE_RE.match(block_lines[index]):
                break
            if not block_lines[index].strip():
                choice_lines.append("")
                index += 1
                continue
            if block_lines[index].startswith((" ", "\t")):
                choice_lines.append(block_lines[index].strip())
                index += 1
                continue
            break

        choices.append(Choice(label=label, content=trim_blank_edges(choice_lines), checked=checked))

    tail_lines = block_lines[index:]
    if len(choices) < 2:
        return None
    return content_lines, choices, tail_lines


def render_quiz_block(
    question_number: str,
    start_line: int,
    content_lines: list[str],
    choices: list[Choice],
    tail_lines: list[str],
    answer_overrides: dict[str, set[str]],
    quiz_type: str,
) -> ConvertedBlock:
    question_id = detect_question_id(content_lines + [line for choice in choices for line in choice.content])
    quiz_id = f"ma-{question_id}" if question_id else f"q-{question_number}"

    checked_labels = {choice.label for choice in choices if choice.checked}
    override_labels = answer_labels_for(answer_overrides, question_number, question_id)
    correct_labels = override_labels or checked_labels

    effective_type = quiz_type
    if quiz_type == "auto":
        effective_type = "checkbox" if len(correct_labels) > 1 else "radio"

    lines = [
        "```quiz",
        f"type: {effective_type}",
        f"id: {quiz_id}",
    ]
    if not correct_labels:
        lines.append(MISSING_ANSWER_COMMENT)
    lines.extend(block_scalar("content", content_lines))
    lines.append("options:")

    for choice in choices:
        lines.append(f"- id: {choice.label}")
        lines.extend(block_scalar("content", choice.content, indent="  "))
        if choice.label in correct_labels:
            lines.append("  correct: true")

    lines.append("```")

    tail = trim_blank_edges(tail_lines)
    if tail:
        lines.append("")
        lines.extend(tail)

    return ConvertedBlock(
        lines=lines,
        conversion=Conversion(
            question_number=question_number,
            quiz_id=quiz_id,
            start_line=start_line,
            choice_count=len(choices),
            correct_labels=tuple(sorted(correct_labels)),
        ),
    )


def convert_markdown(text: str, answer_overrides: dict[str, set[str]], quiz_type: str) -> tuple[str, list[Conversion]]:
    lines = text.splitlines()
    output: list[str] = []
    conversions: list[Conversion] = []
    index = 0

    while index < len(lines):
        heading_match = QUESTION_HEADING_RE.match(lines[index])
        if not heading_match:
            output.append(lines[index])
            index += 1
            continue

        block_start = index + 1
        block_end = find_question_end(lines, block_start)
        block_lines = lines[block_start:block_end]

        parsed = None if any(QUIZ_FENCE_RE.match(line) for line in block_lines) else parse_choices(block_lines)
        if parsed is None:
            output.extend(lines[index:block_end])
            index = block_end
            continue

        content_lines, choices, tail_lines = parsed
        converted = render_quiz_block(
            question_number=heading_match.group("number"),
            start_line=index + 1,
            content_lines=content_lines,
            choices=choices,
            tail_lines=tail_lines,
            answer_overrides=answer_overrides,
            quiz_type=quiz_type,
        )

        output.append(lines[index])
        output.append("")
        output.extend(converted.lines)
        if block_end < len(lines) and SECTION_BREAK_RE.match(lines[block_end]):
            output.append("")
        conversions.append(converted.conversion)
        index = block_end

    converted_text = "\n".join(output)
    if text.endswith("\n"):
        converted_text += "\n"
    return converted_text, conversions


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert checklist multiple-choice questions in an MA lesson markdown file to quiz blocks.",
    )
    parser.add_argument("markdown_file", type=Path)
    parser.add_argument(
        "--answer",
        action="append",
        default=[],
        metavar="QUESTION=LABELS",
        help="Set correct choices by question number or MA question id, e.g. --answer 1=a --answer 24633=d.",
    )
    parser.add_argument(
        "--answer-key-file",
        type=Path,
        help='JSON object mapping question numbers or ids to labels, e.g. {"1": "a", "24633": ["d"]}.',
    )
    parser.add_argument(
        "--type",
        choices=("auto", "radio", "checkbox"),
        default="auto",
        help="Quiz type to emit. auto uses checkbox only when multiple correct labels are known.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print a summary without modifying the file.")
    parser.add_argument("--diff", action="store_true", help="Print a unified diff of the proposed changes.")
    parser.add_argument("--backup", action="store_true", help="Write a .bak copy before modifying the file.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    markdown_file = args.markdown_file
    original_text = markdown_file.read_text(encoding="utf-8")
    answer_overrides = parse_answer_overrides(args.answer, args.answer_key_file)
    converted_text, conversions = convert_markdown(original_text, answer_overrides, args.type)

    if args.diff:
        sys.stdout.writelines(
            difflib.unified_diff(
                original_text.splitlines(keepends=True),
                converted_text.splitlines(keepends=True),
                fromfile=str(markdown_file),
                tofile=str(markdown_file),
            )
        )

    missing_count = sum(1 for conversion in conversions if not conversion.correct_labels)
    action = "Would convert" if args.dry_run else "Converted"
    print(f"{action} {len(conversions)} question(s) in {markdown_file}")
    if conversions:
        for conversion in conversions:
            correct = ",".join(conversion.correct_labels) if conversion.correct_labels else "missing"
            print(
                f"  line {conversion.start_line}: Question {conversion.question_number} "
                f"-> {conversion.quiz_id} ({conversion.choice_count} options, correct={correct})"
            )
    if missing_count:
        print(f"  {missing_count} question(s) need correct-answer metadata.")

    if args.dry_run or converted_text == original_text:
        return 0

    if args.backup:
        backup_file = markdown_file.with_suffix(markdown_file.suffix + ".bak")
        shutil.copy2(markdown_file, backup_file)

    markdown_file.write_text(converted_text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
