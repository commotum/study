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


QUESTION_HEADING_RE = re.compile(
    r"^\*\*Question\s+(?P<number>\d+):?\*\*(?P<inline_content>.*)$",
    re.IGNORECASE,
)
SECTION_BREAK_RE = re.compile(r"^---\s*$")
CHOICE_RE = re.compile(r"^\s*-\s+\[(?P<mark>[ xX])\]\s+(?P<label>[A-Za-z])\.\s*(?P<content>.*)$")
QUIZ_FENCE_RE = re.compile(r"^\s*```quiz\s*$")
QUESTION_ID_RE = re.compile(r"\bq-(?P<id>\d+)(?:-a-\d+)?\.(?:png|jpe?g|gif|webp|svg)\b", re.IGNORECASE)
ANSWER_SPLIT_RE = re.compile(r"[\s,+/|]+")
CHOICES_HEADING_RE = re.compile(r"^#{1,6}\s+Choices\s*$", re.IGNORECASE)
TABLE_SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")

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


@dataclass(frozen=True)
class FileResult:
    path: Path
    conversions: list[Conversion]
    changed: bool


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
        lines.append(f"{indent}  {line}" if line else "")
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


def split_table_row(line: str) -> list[str] | None:
    text = line.strip()
    if not text.startswith("|") or not text.endswith("|"):
        return None
    return [cell.strip() for cell in text.strip("|").split("|")]


def is_table_separator(cells: list[str]) -> bool:
    return bool(cells) and all(TABLE_SEPARATOR_RE.match(cell.replace(" ", "")) for cell in cells)


def render_table_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def render_table_separator(column_count: int) -> str:
    return "| " + " | ".join(["---"] * column_count) + " |"


def table_choice_content(headers: list[str], cells: list[str]) -> list[str]:
    while len(cells) < len(headers):
        cells.append("")
    return [
        render_table_row(headers),
        render_table_separator(len(headers)),
        render_table_row(cells[: len(headers)]),
    ]


def parse_table_choices(block_lines: list[str]) -> tuple[list[str], list[Choice], list[str]] | None:
    choices_heading_index = next(
        (index for index, line in enumerate(block_lines) if CHOICES_HEADING_RE.match(line.strip())),
        None,
    )
    if choices_heading_index is None:
        return None

    table_start = choices_heading_index + 1
    while table_start < len(block_lines) and not block_lines[table_start].strip():
        table_start += 1

    if table_start + 2 > len(block_lines):
        return None

    header = split_table_row(block_lines[table_start])
    separator = split_table_row(block_lines[table_start + 1])
    if not header or not separator or not is_table_separator(separator):
        return None
    if not header[0].strip().lower() == "option":
        return None

    option_headers = header[1:]
    if not option_headers:
        return None

    choices: list[Choice] = []
    index = table_start + 2
    while index < len(block_lines):
        cells = split_table_row(block_lines[index])
        if not cells:
            break
        label = cells[0].strip().lower()
        if not re.fullmatch(r"[a-z]", label):
            break
        choices.append(
            Choice(
                label=label,
                content=table_choice_content(option_headers, cells[1:]),
                checked=False,
            )
        )
        index += 1

    if len(choices) < 2:
        return None

    content_lines = trim_blank_edges(block_lines[:choices_heading_index])
    tail_lines = block_lines[index:]
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


def merge_inline_content(inline_content: str, content_lines: list[str]) -> list[str]:
    inline = inline_content.strip()
    if not inline:
        return content_lines
    if content_lines:
        return [inline, "", *content_lines]
    return [inline]


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

        parsed = None
        if not any(QUIZ_FENCE_RE.match(line) for line in block_lines):
            parsed = parse_choices(block_lines) or parse_table_choices(block_lines)
        if parsed is None:
            output.extend(lines[index:block_end])
            index = block_end
            continue

        content_lines, choices, tail_lines = parsed
        inline_content = heading_match.group("inline_content")
        merged_content_lines = merge_inline_content(inline_content, content_lines)
        converted = render_quiz_block(
            question_number=heading_match.group("number"),
            start_line=index + 1,
            content_lines=merged_content_lines,
            choices=choices,
            tail_lines=tail_lines,
            answer_overrides=answer_overrides,
            quiz_type=quiz_type,
        )

        output.append(f"**Question {heading_match.group('number')}:**" if inline_content.strip() else lines[index])
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
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Markdown files or directories. Directories are searched recursively for .md files.",
    )
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
    parser.add_argument("--summary-only", action="store_true", help="Only print the aggregate conversion summary.")
    return parser


def expand_markdown_paths(paths: list[Path]) -> list[Path]:
    markdown_files: list[Path] = []
    seen: set[Path] = set()

    for path in paths:
        if path.is_dir():
            candidates = sorted(path.rglob("*.md"))
        else:
            candidates = [path]

        for candidate in candidates:
            resolved = candidate.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            markdown_files.append(candidate)

    return markdown_files


def print_file_result(result: FileResult, dry_run: bool) -> None:
    action = "Would convert" if dry_run else "Converted"
    print(f"{action} {len(result.conversions)} question(s) in {result.path}")
    for conversion in result.conversions:
        correct = ",".join(conversion.correct_labels) if conversion.correct_labels else "missing"
        print(
            f"  line {conversion.start_line}: Question {conversion.question_number} "
            f"-> {conversion.quiz_id} ({conversion.choice_count} options, correct={correct})"
        )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    markdown_files = expand_markdown_paths(args.paths)
    if not markdown_files:
        print("No markdown files found.")
        return 0

    answer_overrides = parse_answer_overrides(args.answer, args.answer_key_file)

    results: list[FileResult] = []
    total_missing = 0

    for markdown_file in markdown_files:
        original_text = markdown_file.read_text(encoding="utf-8")
        converted_text, conversions = convert_markdown(original_text, answer_overrides, args.type)
        changed = converted_text != original_text

        if args.diff and changed:
            sys.stdout.writelines(
                difflib.unified_diff(
                    original_text.splitlines(keepends=True),
                    converted_text.splitlines(keepends=True),
                    fromfile=str(markdown_file),
                    tofile=str(markdown_file),
                )
            )

        if conversions:
            result = FileResult(path=markdown_file, conversions=conversions, changed=changed)
            results.append(result)
            if not args.summary_only:
                print_file_result(result, args.dry_run)
            total_missing += sum(1 for conversion in conversions if not conversion.correct_labels)

        if not args.dry_run and changed:
            if args.backup:
                backup_file = markdown_file.with_suffix(markdown_file.suffix + ".bak")
                shutil.copy2(markdown_file, backup_file)
            markdown_file.write_text(converted_text, encoding="utf-8")

    action = "Would convert" if args.dry_run else "Converted"
    total_conversions = sum(len(result.conversions) for result in results)
    print(f"{action} {total_conversions} question(s) across {len(results)} file(s).")
    if total_missing:
        print(f"{total_missing} question(s) need correct-answer metadata.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
