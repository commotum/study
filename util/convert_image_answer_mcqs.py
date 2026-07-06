#!/usr/bin/env python3
"""Convert and mark image-answer MA multiple-choice questions.

Image answer choices use filenames like ``q-80494-a-1.png``.  For these
questions, Math Academy's correct answer is the option whose answer image id is
1.  This script only touches questions where every option has exactly one
``q-<question-id>-a-<answer-image-id>`` image filename and an ``a-1`` option is
present.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import convert_mcq_to_quiz as base


IMAGE_ANSWER_RE = re.compile(
    r"\bq-(?P<question_id>\d+)-a-(?P<answer_id>\d+)\."
    r"(?:png|jpe?g|gif|webp|svg)\b",
    re.IGNORECASE,
)
QUIZ_BLOCK_RE = re.compile(r"```quiz\n(?P<body>.*?)\n```", re.DOTALL)
OPTION_ID_RE = re.compile(r"^- id: (?P<label>[a-z])\s*$")
QUIZ_ID_RE = re.compile(r"^id:\s*(?:ma-)?(?P<question_id>\d+)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class ImageAnswer:
    question_id: str
    correct_label: str
    option_count: int


@dataclass(frozen=True)
class Change:
    path: str
    action: str
    question_number: str
    question_id: str
    correct_label: str
    option_count: int


def image_answer_from_choices(choices: list[base.Choice]) -> ImageAnswer | None:
    parsed: list[tuple[str, str, int]] = []
    for choice in choices:
        content = "\n".join(choice.content)
        matches = list(IMAGE_ANSWER_RE.finditer(content))
        if len(matches) > 1:
            return None
        if not matches:
            continue
        match = matches[0]
        parsed.append(
            (
                choice.label,
                match.group("question_id"),
                int(match.group("answer_id")),
            )
        )

    if len(parsed) < 2:
        return None

    question_ids = {question_id for _, question_id, _ in parsed}
    if len(question_ids) != 1:
        return None

    correct_labels = [label for label, _, answer_id in parsed if answer_id == 1]
    if len(correct_labels) != 1:
        return None

    return ImageAnswer(
        question_id=parsed[0][1],
        correct_label=correct_labels[0],
        option_count=len(choices),
    )


def convert_raw_image_questions(text: str, path: Path) -> tuple[str, list[Change]]:
    lines = text.splitlines()
    output: list[str] = []
    changes: list[Change] = []
    index = 0

    while index < len(lines):
        heading_match = base.QUESTION_HEADING_RE.match(lines[index])
        if not heading_match:
            output.append(lines[index])
            index += 1
            continue

        block_start = index + 1
        block_end = base.find_question_end(lines, block_start)
        block_lines = lines[block_start:block_end]

        parsed = None
        if not any(base.QUIZ_FENCE_RE.match(line) for line in block_lines):
            parsed = base.parse_choices(block_lines) or base.parse_table_choices(block_lines)

        image_answer: ImageAnswer | None = None
        if parsed is not None:
            _, choices, _ = parsed
            image_answer = image_answer_from_choices(choices)

        if parsed is None or image_answer is None:
            output.extend(lines[index:block_end])
            index = block_end
            continue

        content_lines, choices, tail_lines = parsed
        inline_content = heading_match.group("inline_content")
        merged_content_lines = base.merge_inline_content(inline_content, content_lines)
        question_number = heading_match.group("number")
        converted = base.render_quiz_block(
            question_number=question_number,
            start_line=index + 1,
            content_lines=merged_content_lines,
            choices=choices,
            tail_lines=tail_lines,
            answer_overrides={question_number: {image_answer.correct_label}},
            quiz_type="radio",
        )

        output.append(f"**Question {question_number}:**" if inline_content.strip() else lines[index])
        output.append("")
        output.extend(converted.lines)
        if block_end < len(lines) and base.SECTION_BREAK_RE.match(lines[block_end]):
            output.append("")

        changes.append(
            Change(
                path=path.as_posix(),
                action="converted-raw-image-answer",
                question_number=question_number,
                question_id=image_answer.question_id,
                correct_label=image_answer.correct_label,
                option_count=image_answer.option_count,
            )
        )
        index = block_end

    converted_text = "\n".join(output)
    if text.endswith("\n"):
        converted_text += "\n"
    return converted_text, changes


def quiz_options(body: str) -> list[tuple[str, list[str]]]:
    lines = body.splitlines()
    options: list[tuple[str, list[str]]] = []
    current_label: str | None = None
    current_lines: list[str] = []

    for line in lines:
        match = OPTION_ID_RE.match(line)
        if match:
            if current_label is not None:
                options.append((current_label, current_lines))
            current_label = match.group("label")
            current_lines = [line]
            continue
        if current_label is not None:
            current_lines.append(line)

    if current_label is not None:
        options.append((current_label, current_lines))
    return options


def image_answer_from_quiz_body(body: str) -> ImageAnswer | None:
    parsed: list[tuple[str, str, int]] = []
    options = quiz_options(body)
    for label, option_lines in options:
        content = "\n".join(option_lines)
        matches = list(IMAGE_ANSWER_RE.finditer(content))
        if len(matches) > 1:
            return None
        if not matches:
            continue
        match = matches[0]
        parsed.append((label, match.group("question_id"), int(match.group("answer_id"))))

    if len(parsed) < 2 or len({question_id for _, question_id, _ in parsed}) != 1:
        return None

    correct_labels = [label for label, _, answer_id in parsed if answer_id == 1]
    if len(correct_labels) != 1:
        return None

    return ImageAnswer(
        question_id=parsed[0][1],
        correct_label=correct_labels[0],
        option_count=len(options),
    )


def mark_quiz_body(body: str, correct_label: str) -> str:
    lines = [
        line
        for line in body.splitlines()
        if not line.startswith("# MA_ANSWER_MISSING:")
    ]

    output: list[str] = []
    current_label: str | None = None
    inserted = False

    for line in lines:
        option_match = OPTION_ID_RE.match(line)
        if option_match and current_label == correct_label and not inserted:
            output.append("  correct: true")
            inserted = True
        if option_match:
            current_label = option_match.group("label")
        output.append(line)

    if current_label == correct_label and not inserted:
        output.append("  correct: true")

    return "\n".join(output)


def mark_existing_image_quizzes(text: str, path: Path) -> tuple[str, list[Change]]:
    changes: list[Change] = []

    def replace(match: re.Match[str]) -> str:
        body = match.group("body")
        if "MA_ANSWER_MISSING" not in body or "correct: true" in body:
            return match.group(0)

        image_answer = image_answer_from_quiz_body(body)
        if image_answer is None:
            return match.group(0)

        quiz_id_match = QUIZ_ID_RE.search(body)
        question_number = ""
        if quiz_id_match and quiz_id_match.group("question_id") != image_answer.question_id:
            return match.group(0)

        changes.append(
            Change(
                path=path.as_posix(),
                action="marked-existing-image-answer",
                question_number=question_number,
                question_id=image_answer.question_id,
                correct_label=image_answer.correct_label,
                option_count=image_answer.option_count,
            )
        )
        return "```quiz\n" + mark_quiz_body(body, image_answer.correct_label) + "\n```"

    return QUIZ_BLOCK_RE.sub(replace, text), changes


def expand_paths(paths: list[Path]) -> list[Path]:
    markdown_files: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        candidates: list[Path]
        if path.is_dir():
            lesson_candidates = sorted(path.glob("**/Lessons/*.md"))
            candidates = lesson_candidates or sorted(path.rglob("*.md"))
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
    parser = argparse.ArgumentParser(
        description="Convert/mark unambiguous MA image-answer multiple-choice questions.",
    )
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report-json", type=Path)
    parser.add_argument("--summary-only", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    files = expand_paths(args.paths)
    all_changes: list[Change] = []

    for path in files:
        original = path.read_text(encoding="utf-8")
        converted, raw_changes = convert_raw_image_questions(original, path)
        marked, quiz_changes = mark_existing_image_quizzes(converted, path)
        changes = raw_changes + quiz_changes
        if changes:
            all_changes.extend(changes)
            if not args.summary_only:
                print(f"{path}: {len(changes)} image-answer question(s)")
                for change in changes:
                    number = f" question {change.question_number}" if change.question_number else ""
                    print(
                        f"  {change.action}{number} -> ma-{change.question_id} "
                        f"correct={change.correct_label}"
                    )
            if not args.dry_run and marked != original:
                path.write_text(marked, encoding="utf-8")

    if args.report_json:
        payload = [asdict(change) for change in all_changes]
        if args.dry_run:
            args.report_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        else:
            args.report_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    action = "Would update" if args.dry_run else "Updated"
    print(f"{action} {len(all_changes)} image-answer question(s) across {len({c.path for c in all_changes})} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
