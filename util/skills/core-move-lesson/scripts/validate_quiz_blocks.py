#!/usr/bin/env python3
"""Validate Obsidian quiz blocks for core-move lesson markdown files."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SUPPORTED_TYPES = {
    "radio",
    "checkbox",
    "select",
    "multi-select",
    "noodle",
    "free",
    "blank",
}

TOP_KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*\s*:")
RAW_MCQ_RE = re.compile(r"^\s*-\s+\[[ xX]\]\s+[A-Za-z]\.\s+")
OPEN_FENCE = "```quiz"
CLOSE_FENCE = "```"


@dataclass(frozen=True)
class QuizBlock:
    start_line: int
    end_line: int
    lines: list[str]


@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    message: str

    def render(self) -> str:
        return f"{self.path}:{self.line}: {self.message}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown files to validate.")
    parser.add_argument(
        "--allow-no-quiz",
        action="store_true",
        help="Do not fail files that contain no quiz blocks.",
    )
    parser.add_argument(
        "--allow-raw-mcq",
        action="store_true",
        help="Allow raw '- [ ] A.' multiple-choice lists outside quiz blocks.",
    )
    parser.add_argument(
        "--require-radio-practice",
        action="store_true",
        help="Require every quiz block to use type: radio.",
    )
    parser.add_argument(
        "--strict-ids",
        action="store_true",
        help="Require quiz block ids and option ids where applicable.",
    )
    return parser.parse_args()


def extract_quiz_blocks(path: Path, lines: list[str]) -> tuple[list[QuizBlock], list[Issue], set[int]]:
    blocks: list[QuizBlock] = []
    issues: list[Issue] = []
    covered: set[int] = set()
    index = 0
    while index < len(lines):
        if lines[index].strip() != OPEN_FENCE:
            index += 1
            continue

        start = index
        index += 1
        body: list[str] = []
        while index < len(lines) and lines[index].strip() != CLOSE_FENCE:
            body.append(lines[index].rstrip("\n"))
            index += 1

        if index >= len(lines):
            issues.append(Issue(path, start + 1, "unclosed ```quiz fence"))
            break

        end = index
        covered.update(range(start, end + 1))
        blocks.append(QuizBlock(start_line=start + 1, end_line=end + 1, lines=body))
        index += 1
    return blocks, issues, covered


def scalar_value(lines: list[str], key: str, indent: str = "") -> str | None:
    pattern = re.compile(rf"^\s*(?:-\s*)?{re.escape(key)}\s*:\s*(.*)$")
    for line in lines:
        if indent and line.strip() and not line.startswith(indent) and not line.startswith("- "):
            continue
        match = pattern.match(line)
        if match:
            value = match.group(1).strip()
            if value in {"|-", "|", ">-", ">"}:
                return value
            return strip_quotes(value)
    return None


def has_key(lines: list[str], key: str, indent: str = "") -> bool:
    return scalar_value(lines, key, indent) is not None


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def top_block(lines: list[str], key: str) -> list[str]:
    start = None
    for index, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}\s*:", line):
            start = index + 1
            break
    if start is None:
        return []

    end = len(lines)
    for index in range(start, len(lines)):
        if TOP_KEY_RE.match(lines[index]):
            end = index
            break
    return lines[start:end]


def split_list_items(lines: list[str], indent: str = "") -> list[list[str]]:
    items: list[list[str]] = []
    current: list[str] = []
    prefix = f"{indent}- "
    for line in lines:
        if line.startswith(prefix):
            if current:
                items.append(current)
            current = [line]
        elif current:
            current.append(line)
    if current:
        items.append(current)
    return items


def nested_block(item: list[str], key: str, indent: str = "  ") -> list[str]:
    key_line = f"{indent}{key}:"
    start = None
    for index, line in enumerate(item):
        if line.startswith(key_line):
            start = index + 1
            break
    if start is None:
        return []

    end = len(item)
    for index in range(start, len(item)):
        line = item[index]
        if line and not line.startswith(indent):
            end = index
            break
    return item[start:end]


def count_correct_true(items: list[list[str]]) -> int:
    return sum(
        1
        for item in items
        if any(re.match(r"^\s*correct\s*:\s*true\s*$", line, flags=re.IGNORECASE) for line in item)
    )


def option_ids(items: list[list[str]]) -> list[str]:
    ids: list[str] = []
    for item in items:
        value = scalar_value(item, "id")
        if value:
            ids.append(value)
    return ids


def validate_options(
    path: Path,
    block: QuizBlock,
    items: list[list[str]],
    *,
    strict_ids: bool,
) -> list[Issue]:
    issues: list[Issue] = []
    seen_ids: set[str] = set()
    for index, item in enumerate(items, start=1):
        option_line = block.start_line + block.lines.index(item[0])
        if not has_key(item, "content"):
            issues.append(Issue(path, option_line, f"option {index} is missing content"))
        option_id = scalar_value(item, "id")
        if strict_ids and not option_id:
            issues.append(Issue(path, option_line, f"option {index} is missing id"))
        if option_id:
            if option_id in seen_ids:
                issues.append(Issue(path, option_line, f"duplicate option id: {option_id}"))
            seen_ids.add(option_id)
    return issues


def validate_radio_or_checkbox(
    path: Path,
    block: QuizBlock,
    quiz_type: str,
    *,
    strict_ids: bool,
) -> list[Issue]:
    issues: list[Issue] = []
    options = split_list_items(top_block(block.lines, "options"))
    if len(options) < 2:
        return [Issue(path, block.start_line, f"{quiz_type} quiz requires at least two options")]

    issues.extend(validate_options(path, block, options, strict_ids=strict_ids))
    correct_count = count_correct_true(options)
    if quiz_type == "radio" and correct_count != 1:
        issues.append(Issue(path, block.start_line, "radio quiz requires exactly one correct: true option"))
    if quiz_type == "checkbox" and correct_count < 1:
        issues.append(Issue(path, block.start_line, "checkbox quiz requires at least one correct: true option"))
    return issues


def validate_select(path: Path, block: QuizBlock, *, strict_ids: bool) -> list[Issue]:
    issues: list[Issue] = []
    options = split_list_items(top_block(block.lines, "options"))
    questions = split_list_items(top_block(block.lines, "questions"))
    if len(options) < 2:
        issues.append(Issue(path, block.start_line, "select quiz requires at least two top-level options"))
    if not questions:
        issues.append(Issue(path, block.start_line, "select quiz requires questions"))
    issues.extend(validate_options(path, block, options, strict_ids=True))
    ids = set(option_ids(options))
    for index, question in enumerate(questions, start=1):
        line = block.start_line + block.lines.index(question[0])
        if not has_key(question, "content"):
            issues.append(Issue(path, line, f"select question {index} is missing content"))
        correct = scalar_value(question, "correct_option")
        if not correct:
            issues.append(Issue(path, line, f"select question {index} is missing correct_option"))
        elif correct not in ids:
            issues.append(Issue(path, line, f"select question {index} correct_option does not match an option id"))
    return issues


def validate_multi_select(path: Path, block: QuizBlock, *, strict_ids: bool) -> list[Issue]:
    issues: list[Issue] = []
    questions = split_list_items(top_block(block.lines, "questions"))
    if not questions:
        return [Issue(path, block.start_line, "multi-select quiz requires questions")]
    for index, question in enumerate(questions, start=1):
        line = block.start_line + block.lines.index(question[0])
        if not has_key(question, "content"):
            issues.append(Issue(path, line, f"multi-select question {index} is missing content"))
        nested_options = split_list_items(nested_block(question, "options", indent="  "), indent="  ")
        if len(nested_options) < 2:
            issues.append(Issue(path, line, f"multi-select question {index} requires at least two options"))
            continue
        issues.extend(validate_options(path, block, nested_options, strict_ids=True))
        ids = set(option_ids(nested_options))
        correct = scalar_value(question, "correct_option")
        if not correct:
            issues.append(Issue(path, line, f"multi-select question {index} is missing correct_option"))
        elif correct not in ids:
            issues.append(Issue(path, line, f"multi-select question {index} correct_option does not match an option id"))
    return issues


def validate_noodle(path: Path, block: QuizBlock, *, strict_ids: bool) -> list[Issue]:
    issues: list[Issue] = []
    options = split_list_items(top_block(block.lines, "options"))
    questions = split_list_items(top_block(block.lines, "questions"))
    if len(options) < 2:
        issues.append(Issue(path, block.start_line, "noodle quiz requires at least two options"))
    if len(questions) < 2:
        issues.append(Issue(path, block.start_line, "noodle quiz requires at least two questions"))
    for index, option in enumerate(options, start=1):
        line = block.start_line + block.lines.index(option[0])
        if not has_key(option, "content"):
            issues.append(Issue(path, line, f"noodle option {index} is missing content"))
    for index, question in enumerate(questions, start=1):
        line = block.start_line + block.lines.index(question[0])
        if not has_key(question, "content"):
            issues.append(Issue(path, line, f"noodle question {index} is missing content"))
        if not has_key(question, "correct") and not has_key(question, "correct_option"):
            issues.append(Issue(path, line, f"noodle question {index} is missing correct or correct_option"))
    return issues


def validate_block(
    path: Path,
    block: QuizBlock,
    *,
    require_radio_practice: bool,
    strict_ids: bool,
) -> list[Issue]:
    issues: list[Issue] = []
    quiz_type = scalar_value(block.lines, "type")
    if not quiz_type:
        return [Issue(path, block.start_line, "quiz block is missing type")]
    if quiz_type not in SUPPORTED_TYPES:
        return [Issue(path, block.start_line, f"unsupported quiz type: {quiz_type}")]
    if require_radio_practice and quiz_type != "radio":
        issues.append(Issue(path, block.start_line, f"expected type: radio for core-move practice, found {quiz_type}"))
    if strict_ids and not scalar_value(block.lines, "id"):
        issues.append(Issue(path, block.start_line, "quiz block is missing id"))
    if not has_key(block.lines, "content"):
        issues.append(Issue(path, block.start_line, "quiz block is missing content"))

    if quiz_type in {"radio", "checkbox"}:
        issues.extend(validate_radio_or_checkbox(path, block, quiz_type, strict_ids=strict_ids))
    elif quiz_type == "select":
        issues.extend(validate_select(path, block, strict_ids=strict_ids))
    elif quiz_type == "multi-select":
        issues.extend(validate_multi_select(path, block, strict_ids=strict_ids))
    elif quiz_type == "noodle":
        issues.extend(validate_noodle(path, block, strict_ids=strict_ids))
    elif quiz_type == "blank" and "==" not in "\n".join(block.lines):
        issues.append(Issue(path, block.start_line, "blank quiz content must contain at least one ==answer== gap"))
    return issues


def validate_file(path: Path, args: argparse.Namespace) -> tuple[list[Issue], int]:
    if not path.exists():
        return [Issue(path, 1, "file not found")], 0
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks, issues, covered = extract_quiz_blocks(path, lines)
    if not blocks and not args.allow_no_quiz:
        issues.append(Issue(path, 1, "file contains no quiz blocks"))
    if not args.allow_raw_mcq:
        for index, line in enumerate(lines, start=1):
            if index - 1 not in covered and RAW_MCQ_RE.match(line):
                issues.append(Issue(path, index, "raw checklist MCQ found outside a quiz block"))
    for block in blocks:
        issues.extend(
            validate_block(
                path,
                block,
                require_radio_practice=args.require_radio_practice,
                strict_ids=args.strict_ids,
            )
        )
    return issues, len(blocks)


def main() -> int:
    args = parse_args()
    all_issues: list[Issue] = []
    block_count = 0
    for raw_path in args.paths:
        path = raw_path.expanduser()
        issues, count = validate_file(path, args)
        all_issues.extend(issues)
        block_count += count

    for issue in all_issues:
        print(issue.render(), file=sys.stderr)

    if all_issues:
        print(f"quiz block validation failed: {len(all_issues)} issue(s), {block_count} block(s) checked", file=sys.stderr)
        return 1

    print(f"quiz block validation passed: {block_count} block(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
