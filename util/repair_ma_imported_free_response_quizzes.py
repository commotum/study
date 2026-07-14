#!/usr/bin/env python3
"""Propagate exact blank quizzes to every imported MA lesson placement.

The filesystem-derived manifest is authoritative for scope.  Each imported
``(topic-id, question-id)`` is repaired in its canonical Math Academy lesson
and in active MTH-252/MTH-253 copies.  Layout templates use ``{{image-N}}``
tokens so every placement keeps its own local image path.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

from build_ma_imported_free_response_manifest import (
    IMAGE_RE,
    block_content,
    canonical_number_index,
    identify_question,
)
from repair_course_free_response_quizzes import (
    BLANK_ANSWER_RE,
    LESSON_ID_RE,
    MARKER,
    QUESTION_RE,
    QUIZ_ID_RE,
    QUIZ_RE,
    exact_blank_body,
    load_topic_metadata,
    quiz_type,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
MA_ROOT = REPO_ROOT / "vault" / "MA"
DEFAULT_MANIFEST = REPO_ROOT / "util" / "ma_imported_free_response_manifest.csv"
DEFAULT_ANSWERS = REPO_ROOT / "util" / "ma_free_response_answer_key.csv"
DEFAULT_LAYOUTS = REPO_ROOT / "util" / "ma_free_response_layouts.json"
IMAGE_TOKEN_RE = re.compile(r"\{\{image-(?P<number>\d+)\}\}")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def repo_path(raw: str) -> Path:
    path = Path(raw)
    return path if path.is_absolute() else REPO_ROOT / path


def relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def lesson_id(text: str) -> str | None:
    match = LESSON_ID_RE.search(text)
    return match.group("id") if match else None


def placement_paths(row: dict[str, str]) -> list[str]:
    values: list[str] = []
    for field in ("canonical-placements", "active-copy-placements"):
        values.extend(item for item in row[field].split(";") if item)
    return values


def load_registry(
    manifest_path: Path,
    answers_path: Path,
    layouts_path: Path,
) -> tuple[
    list[tuple[str, str]],
    dict[tuple[str, str], set[str]],
    dict[tuple[str, str], str],
]:
    manifest = read_csv(manifest_path)
    answers = read_csv(answers_path)
    raw_layouts = json.loads(layouts_path.read_text(encoding="utf-8"))

    keys = [(row["topic-id"], row["question-id"]) for row in manifest]
    if len(keys) != len(set(keys)):
        raise ValueError("Manifest contains duplicate topic/question keys")

    answer_keys = [(row["topic-id"], row["question-id"]) for row in answers]
    if answer_keys != keys:
        raise ValueError("Answer registry order/keys differ from the imported manifest")

    layout_keys = {tuple(key.split(":", 1)) for key in raw_layouts}
    if layout_keys != set(keys):
        raise ValueError("Layout registry keys differ from the imported manifest")

    expected: dict[tuple[str, str], set[str]] = {}
    layouts: dict[tuple[str, str], str] = {}
    for row, answer_row in zip(manifest, answers, strict=True):
        key = (row["topic-id"], row["question-id"])
        paths = placement_paths(row)
        expected_count = int(row["total-occurrences"])
        if len(paths) != expected_count or len(paths) != len(set(paths)):
            raise ValueError(
                f"Manifest placement mismatch for {key}: "
                f"paths={len(paths)}, expected={expected_count}"
            )
        if int(answer_row["expected-occurrences"]) != expected_count:
            raise ValueError(f"Answer occurrence mismatch for {key}")
        layout = raw_layouts[f"{key[0]}:{key[1]}"]
        inline = BLANK_ANSWER_RE.findall(layout)
        if ", ".join(inline) != answer_row["answer"]:
            raise ValueError(f"Inline answers differ from registry for {key}")
        expected[key] = set(paths)
        layouts[key] = layout
    return keys, expected, layouts


def render_layout(template: str, current_body: str, key: tuple[str, str], path: Path) -> str:
    images = IMAGE_RE.findall(block_content(current_body))
    token_numbers = [int(match.group("number")) for match in IMAGE_TOKEN_RE.finditer(template)]
    expected_numbers = list(range(1, len(token_numbers) + 1))
    if token_numbers != expected_numbers:
        raise ValueError(f"Nonsequential image tokens for {key}: {token_numbers}")
    if len(images) != len(token_numbers):
        raise ValueError(
            f"Image count mismatch for {key} in {relative(path)}: "
            f"template={len(token_numbers)}, placement={len(images)}"
        )
    rendered = template
    for number, image in enumerate(images, start=1):
        rendered = rendered.replace(f"{{{{image-{number}}}}}", image)
    if IMAGE_TOKEN_RE.search(rendered):
        raise ValueError(f"Unresolved image token for {key} in {relative(path)}")
    return rendered


def collect_targets(
    keys: list[tuple[str, str]],
    expected: dict[tuple[str, str], set[str]],
    number_index: dict[tuple[str, int], str],
) -> tuple[
    dict[Path, str],
    dict[tuple[str, str], list[tuple[Path, int, int, str, str]]],
]:
    texts: dict[Path, str] = {}
    targets: dict[tuple[str, str], list[tuple[Path, int, int, str, str]]] = defaultdict(list)
    by_path: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for key in keys:
        for raw_path in expected[key]:
            by_path[raw_path].add(key)

    for raw_path, path_keys in sorted(by_path.items()):
        path = repo_path(raw_path)
        if not path.exists():
            raise ValueError(f"Manifest placement is missing: {raw_path}")
        text = path.read_text(encoding="utf-8")
        texts[path] = text
        topic_id = lesson_id(text)
        if not topic_id:
            raise ValueError(f"Manifest placement lacks lesson-id: {raw_path}")
        if {key[0] for key in path_keys} != {topic_id}:
            raise ValueError(f"Manifest topic does not match lesson-id in {raw_path}")

        for section in QUESTION_RE.finditer(text):
            number = int(section.group("number"))
            section_offset = section.start("body")
            for quiz in QUIZ_RE.finditer(section.group("body")):
                body = quiz.group("body")
                question_id = identify_question(topic_id, number, body, number_index)
                key = (topic_id, question_id or "")
                if key not in path_keys:
                    continue
                start = section_offset + quiz.start()
                end = section_offset + quiz.end()
                targets[key].append((path, start, end, quiz.group(0), body))

    for key in keys:
        found_paths = [relative(item[0]) for item in targets[key]]
        if len(found_paths) != len(set(found_paths)):
            raise ValueError(f"Multiple target quizzes in one placement for {key}: {found_paths}")
        if set(found_paths) != expected[key]:
            raise ValueError(
                f"Target placement mismatch for {key}: "
                f"missing={sorted(expected[key] - set(found_paths))}, "
                f"extra={sorted(set(found_paths) - expected[key])}"
            )
    return texts, targets


def repair(
    keys: list[tuple[str, str]],
    layouts: dict[tuple[str, str], str],
    texts: dict[Path, str],
    targets: dict[tuple[str, str], list[tuple[Path, int, int, str, str]]],
) -> tuple[dict[Path, str], int, int, int]:
    replacements: dict[Path, list[tuple[int, int, str]]] = defaultdict(list)
    converted = updated = unchanged = 0

    for key in keys:
        for path, start, end, whole, body in targets[key]:
            id_match = QUIZ_ID_RE.search(body)
            if not id_match:
                raise ValueError(f"Target quiz lacks id for {key} in {relative(path)}")
            content = render_layout(layouts[key], body, key, path)
            new_body = exact_blank_body(id_match.group("id"), content)
            new_whole = f"```quiz\n{new_body}\n```"
            if whole == new_whole:
                unchanged += 1
            else:
                if quiz_type(body) == "blank":
                    updated += 1
                else:
                    converted += 1
                replacements[path].append((start, end, new_whole))

    for path, items in replacements.items():
        text = texts[path]
        for start, end, replacement in sorted(items, reverse=True):
            text = text[:start] + replacement + text[end:]
        texts[path] = text
    return texts, converted, updated, unchanged


def verify(
    keys: list[tuple[str, str]],
    expected: dict[tuple[str, str], set[str]],
    layouts: dict[tuple[str, str], str],
    texts: dict[Path, str],
    number_index: dict[tuple[str, int], str],
) -> None:
    seen: dict[tuple[str, str], set[str]] = defaultdict(set)
    wanted = set(keys)
    for path, text in texts.items():
        topic_id = lesson_id(text)
        if not topic_id:
            continue
        for section in QUESTION_RE.finditer(text):
            number = int(section.group("number"))
            for quiz in QUIZ_RE.finditer(section.group("body")):
                body = quiz.group("body")
                question_id = identify_question(topic_id, number, body, number_index)
                key = (topic_id, question_id or "")
                if key not in wanted or relative(path) not in expected[key]:
                    continue
                seen[key].add(relative(path))
                if quiz_type(body) != "blank" or "require_exact: true" not in body:
                    raise ValueError(f"Post-repair type mismatch for {key} in {relative(path)}")
                if MARKER in body or "\noptions:" in body or "\ncorrect:" in body:
                    raise ValueError(f"Post-repair debris for {key} in {relative(path)}")
                desired = render_layout(layouts[key], body, key, path)
                id_match = QUIZ_ID_RE.search(body)
                if body != exact_blank_body(id_match.group("id"), desired):
                    raise ValueError(f"Post-repair layout mismatch for {key} in {relative(path)}")
    for key in keys:
        if seen[key] != expected[key]:
            raise ValueError(f"Post-repair occurrence mismatch for {key}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--answers", type=Path, default=DEFAULT_ANSWERS)
    parser.add_argument("--layouts", type=Path, default=DEFAULT_LAYOUTS)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    keys, expected, layouts = load_registry(
        args.manifest.resolve(), args.answers.resolve(), args.layouts.resolve()
    )
    number_index = canonical_number_index(load_topic_metadata(MA_ROOT))
    texts, targets = collect_targets(keys, expected, number_index)
    texts, converted, updated, unchanged = repair(keys, layouts, texts, targets)
    verify(keys, expected, layouts, texts, number_index)

    changed_paths = [
        path for path, text in texts.items() if text != path.read_text(encoding="utf-8")
    ]
    if args.write:
        for path in changed_paths:
            path.write_text(texts[path], encoding="utf-8")

    print(f"Imported free-response keys: {len(keys)}")
    print(f"Placements verified: {sum(len(paths) for paths in expected.values())}")
    print(f"Converted to blank: {converted}")
    print(f"Existing blanks updated: {updated}")
    print(f"Already exact/current: {unchanged}")
    print(f"Files {'changed' if args.write else 'that would change'}: {len(changed_paths)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
