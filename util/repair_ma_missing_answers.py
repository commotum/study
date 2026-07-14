#!/usr/bin/env python3
"""Repair the remaining imported MA radio/select answer metadata.

The manual registry is keyed by stable ``lesson-id:quiz-id``.  It covers
genuine select-list questions and the small set of malformed source MCQs that
need an explicit mathematically defensible option.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MA_ROOT = REPO_ROOT / "vault" / "MA"
DEFAULT_REPAIRS = REPO_ROOT / "util" / "ma_missing_answer_repairs.json"
QUIZ_RE = re.compile(r"```quiz\n(?P<body>.*?)\n```", re.DOTALL)
LESSON_ID_RE = re.compile(r"^lesson-id:\s*(?P<id>\d+)\s*$", re.MULTILINE)
QUIZ_ID_RE = re.compile(r"^id:\s*(?P<id>\S+)\s*$", re.MULTILINE)
QUIZ_TYPE_RE = re.compile(r"^type:\s*(?P<type>\S+)\s*$", re.MULTILINE)
MARKER_RE = re.compile(r"^# MA_ANSWER_MISSING:.*(?:\n|\Z)", re.MULTILINE)
OPTION_ID_RE = re.compile(r"^- id:\s*(?P<id>[a-z])\s*$", re.MULTILINE)
CORRECT_OPTION_RE = re.compile(r"^\s{2}correct_option:\s*(?P<id>\S+)\s*$", re.MULTILINE)


def lesson_id(text: str) -> str | None:
    match = LESSON_ID_RE.search(text)
    return match.group("id") if match else None


def quiz_id(body: str) -> str | None:
    match = QUIZ_ID_RE.search(body)
    return match.group("id") if match else None


def quiz_type(body: str) -> str | None:
    match = QUIZ_TYPE_RE.search(body)
    return match.group("type") if match else None


def load_repairs(path: Path) -> dict[tuple[str, str], dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Repair registry must be a JSON object")
    repairs: dict[tuple[str, str], dict[str, object]] = {}
    for raw_key, entry in payload.items():
        if not isinstance(raw_key, str) or ":" not in raw_key or not isinstance(entry, dict):
            raise ValueError(f"Invalid repair entry: {raw_key!r}")
        topic_id, raw_id = raw_key.split(":", 1)
        key = (topic_id, raw_id)
        if entry.get("type") not in {"radio", "select"}:
            raise ValueError(f"Invalid quiz type for {key}")
        if not isinstance(entry.get("expected_occurrences"), int):
            raise ValueError(f"Missing expected occurrence count for {key}")
        if entry["type"] == "radio" and not isinstance(entry.get("correct"), str):
            raise ValueError(f"Radio repair lacks correct label for {key}")
        if entry["type"] == "select" and not isinstance(entry.get("correct_option"), str):
            raise ValueError(f"Select repair lacks correct option for {key}")
        repairs[key] = entry
    return repairs


def add_radio_option(body: str, label: str, content: str) -> str:
    if re.search(rf"^- id:\s*{re.escape(label)}\s*$", body, re.MULTILINE):
        return body
    lines = content.splitlines() or [content]
    option = "\n".join(
        [f"- id: {label}", "  content: |-", *(f"    {line}" if line else "" for line in lines)]
    )
    return body.rstrip() + "\n" + option


def set_radio_correct(body: str, label: str) -> str:
    option_match = re.search(rf"^- id:\s*{re.escape(label)}\s*$", body, re.MULTILINE)
    if not option_match:
        raise ValueError(f"Radio option {label!r} does not exist")
    if re.match(r"\n  correct:\s*true\s*$", body[option_match.end() :], re.MULTILINE):
        return body
    return body[: option_match.end()] + "\n  correct: true" + body[option_match.end() :]


def set_select_correct(body: str, correct_option: str) -> str:
    option_ids = {
        match.group(1)
        for match in re.finditer(r"^- id:\s*(\S+)\s*$", body, re.MULTILINE)
        if "-option-" in match.group(1)
    }
    if correct_option not in option_ids:
        raise ValueError(f"Select option {correct_option!r} does not exist")
    question_id = correct_option.rsplit("-option-", 1)[0]
    question_match = re.search(
        rf"^(?P<line>- id:\s*{re.escape(question_id)}\s*)$", body, re.MULTILINE
    )
    if not question_match:
        raise ValueError(f"Select question {question_id!r} does not exist")
    current = CORRECT_OPTION_RE.search(body)
    if current:
        if current.group("id") != correct_option:
            raise ValueError(
                f"Existing select answer {current.group('id')!r} conflicts with {correct_option!r}"
            )
        return body
    return body[: question_match.end()] + f"\n  correct_option: {correct_option}" + body[question_match.end() :]


def apply_entry(body: str, entry: dict[str, object]) -> str:
    body = MARKER_RE.sub("", body)
    old = entry.get("content_old")
    new = entry.get("content_new")
    if old is not None or new is not None:
        if not isinstance(old, str) or not isinstance(new, str):
            raise ValueError("content_old and content_new must both be strings")
        if old in body:
            body = body.replace(old, new, 1)
        elif new not in body:
            raise ValueError("Neither old nor repaired prompt text is present")

    if entry["type"] == "radio":
        label = str(entry["correct"])
        add_option = entry.get("add_option")
        if add_option is not None:
            if not isinstance(add_option, str):
                raise ValueError("add_option must be a string")
            body = add_radio_option(body, label, add_option)
        return set_radio_correct(body, label)
    return set_select_correct(body, str(entry["correct_option"]))


def verify_body(body: str, entry: dict[str, object], key: tuple[str, str]) -> None:
    if MARKER_RE.search(body):
        raise ValueError(f"Marker remains for {key}")
    if quiz_type(body) != entry["type"]:
        raise ValueError(f"Quiz type mismatch for {key}")
    if entry["type"] == "radio":
        correct_labels: list[str] = []
        for option in re.finditer(
            r"^- id:\s*(?P<label>[a-z])\s*$\n(?P<body>.*?)(?=^- id:\s*[a-z]\s*$|\Z)",
            body,
            re.MULTILINE | re.DOTALL,
        ):
            if re.search(r"^\s{2}correct:\s*true\s*$", option.group("body"), re.MULTILINE):
                correct_labels.append(option.group("label"))
        if correct_labels != [entry["correct"]]:
            raise ValueError(f"Radio answer mismatch for {key}: {correct_labels}")
        if entry.get("add_option") is not None and str(entry["add_option"]) not in body:
            raise ValueError(f"Added option content missing for {key}")
        if entry.get("content_new") is not None and str(entry["content_new"]) not in body:
            raise ValueError(f"Repaired prompt content missing for {key}")
    else:
        matches = CORRECT_OPTION_RE.findall(body)
        if matches != [entry["correct_option"]]:
            raise ValueError(f"Select answer mismatch for {key}: {matches}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repairs", type=Path, default=DEFAULT_REPAIRS)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    repairs = load_repairs(args.repairs.resolve())

    texts = {path: path.read_text(encoding="utf-8") for path in sorted(MA_ROOT.rglob("*.md"))}
    marker_keys: set[tuple[str, str]] = set()
    occurrences: dict[tuple[str, str], int] = defaultdict(int)
    changed: list[Path] = []

    for path, original in texts.items():
        topic_id = lesson_id(original)
        if not topic_id:
            continue

        def replace(match: re.Match[str]) -> str:
            body = match.group("body")
            raw_id = quiz_id(body)
            key = (topic_id, raw_id or "")
            if MARKER_RE.search(body):
                marker_keys.add(key)
            entry = repairs.get(key)
            if entry is None:
                return match.group(0)
            occurrences[key] += 1
            new_body = apply_entry(body, entry)
            verify_body(new_body, entry, key)
            return f"```quiz\n{new_body}\n```"

        updated = QUIZ_RE.sub(replace, original)
        texts[path] = updated
        if updated != original:
            changed.append(path)

    unknown_markers = marker_keys - set(repairs)
    if unknown_markers:
        raise ValueError(f"Unregistered answer markers: {sorted(unknown_markers)}")
    for key, entry in repairs.items():
        expected = int(entry["expected_occurrences"])
        if occurrences[key] != expected:
            raise ValueError(f"Occurrence mismatch for {key}: {occurrences[key]} != {expected}")
    if any("MA_ANSWER_MISSING" in text for text in texts.values()):
        raise ValueError("At least one MA_ANSWER_MISSING marker remains after repair")

    if args.write:
        for path in changed:
            path.write_text(texts[path], encoding="utf-8")

    print(f"Repair keys verified: {len(repairs)}")
    print(f"Quiz placements verified: {sum(occurrences.values())}")
    print(f"Files {'changed' if args.write else 'that would change'}: {len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
