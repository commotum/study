#!/usr/bin/env python3
"""Build the imported MA exact-answer registry and blank-layout templates.

Exact course seeds and canonical correct-option seeds are derived from the
filesystem manifest.  Newly solved questions live in the small manual JSON
file consumed by this script.  Output is deterministic and contains only
imported question IDs.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

from repair_course_free_response_quizzes import BLANK_ANSWER_RE


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPO_ROOT / "util" / "ma_imported_free_response_manifest.csv"
DEFAULT_MANUAL = REPO_ROOT / "util" / "ma_free_response_manual_answers.json"
DEFAULT_ANSWERS = REPO_ROOT / "util" / "ma_free_response_answer_key.csv"
DEFAULT_LAYOUTS = REPO_ROOT / "util" / "ma_free_response_layouts.json"

MULTI_SEMANTIC_OVERRIDES = {
    "529:174120": ["5", "10"],
    "2437:237516": ["4/5", "5"],
    "2437:237520": ["3", "3/8"],
    "528:222926": ["1/2", "1/8"],
    "645:175345": ["1", "1/2"],
    "33:250348": ["12", "20"],
    "33:218538": ["12", "8"],
    "33:218539": ["10", "11"],
    "33:250605": ["-1", "32"],
}

SEMANTIC_LAYOUT_OVERRIDES = {
    "4028:208734": (["-5"], "$x \\ge$ ==-5==."),
    "4028:214575": (["-1"], "$x <$ ==-1==."),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def replace_simple_fractions(value: str) -> str:
    pattern = re.compile(r"\\frac\{([^{}]+)\}\{([^{}]+)\}")
    while True:
        match = pattern.search(value)
        if not match:
            return value
        numerator, denominator = match.groups()
        numerator = numerator.strip()
        denominator = denominator.strip()
        if re.search(r"[+\-]", numerator[1:]):
            numerator = f"({numerator})"
        if re.search(r"[+\-]", denominator[1:]) or not re.fullmatch(
            r"(?:\d+|[A-Za-z])", denominator
        ):
            denominator = f"({denominator})"
        value = value[: match.start()] + f"{numerator}/{denominator}" + value[match.end() :]


def latex_to_keyboard(raw: str) -> str:
    value = raw.strip()
    value = value.replace("$", "")
    value = value.replace(r"\left", "").replace(r"\right", "")
    value = value.replace(r"\textrm{i}", "i").replace(r"\mathrm{i}", "i")
    value = value.replace(r"\infty", "infinity")
    value = value.replace(r"\geq", ">=").replace(r"\ge", ">=")
    value = value.replace(r"\leq", "<=").replace(r"\le", "<=")
    value = value.replace(r"\div", "/").replace(r"\cdot", "*").replace(r"\times", "*")
    value = value.replace(r"\approx", "")
    value = re.sub(
        r"(?P<whole>-?\d+)\\frac\{(?P<num>[^{}]+)\}\{(?P<den>[^{}]+)\}",
        lambda match: f"{match.group('whole')} {match.group('num')}/{match.group('den')}",
        value,
    )
    value = replace_simple_fractions(value)
    value = re.sub(r"\\log_\{([^{}]+)\}\s*([^\s]+)", r"log_\1(\2)", value)
    value = re.sub(r"\^\{([^{}]+)\}", r"^\1", value)
    value = re.sub(r"_\{([^{}]+)\}", r"_\1", value)
    value = value.replace(r"\,", " ").replace(r"\;", " ").replace(r"\!", "")
    value = re.sub(r"\\(?:text|textrm|mathrm)\{([^{}]*)\}", r"\1", value)
    value = value.replace("−", "-").replace("∞", "infinity")
    value = re.sub(r"\s+", " ", value).strip()
    value = re.sub(r"\s*/\s*", "/", value)
    if "=" in value:
        # A one-blank source prompt normally already supplies the variable and
        # equals sign.  Canonical options occasionally repeat them.
        value = value.rsplit("=", 1)[1].strip()
    value = re.sub(r"\s+years?$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^-\s+", "-", value)
    value = value.replace("(- ", "(-").replace("- infinity", "-infinity")
    return value


def normalize_images(layout: str) -> str:
    image_re = re.compile(r"!\[[^\]]*\]\(<[^>]+>\)")
    counter = 0

    def replace(_: re.Match[str]) -> str:
        nonlocal counter
        counter += 1
        return f"{{{{image-{counter}}}}}"

    return image_re.sub(replace, layout)


def generic_layout(row: dict[str, str], answers: list[str]) -> str:
    content = normalize_images(row["current-content"].rstrip())
    if len(answers) == 1:
        answer_line = f"Answer: =={answers[0]}==."
    else:
        rendered = ", ".join(f"=={answer}==" for answer in answers)
        answer_line = f"Enter the blanks from left to right: {rendered}."
    return f"{content}\n\n{answer_line}" if content else answer_line


def load_manual(path: Path) -> dict[str, dict[str, object]]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Manual answer registry must be a JSON object")
    result: dict[str, dict[str, object]] = {}
    for key, value in payload.items():
        if not isinstance(key, str) or ":" not in key:
            raise ValueError(f"Invalid manual answer key: {key!r}")
        if isinstance(value, list):
            value = {"answers": value}
        if not isinstance(value, dict) or not isinstance(value.get("answers"), list):
            raise ValueError(f"Invalid manual answer entry for {key}")
        answers = value["answers"]
        if not answers or not all(isinstance(answer, str) and answer for answer in answers):
            raise ValueError(f"Invalid manual answers for {key}")
        result[key] = value
    return result


def build(
    manifest: list[dict[str, str]],
    manual: dict[str, dict[str, object]],
) -> tuple[list[dict[str, str]], dict[str, str], list[str]]:
    manifest_keys = {f"{row['topic-id']}:{row['question-id']}" for row in manifest}
    extra = set(manual) - manifest_keys
    if extra:
        raise ValueError(f"Manual registry contains non-imported keys: {sorted(extra)}")

    output: list[dict[str, str]] = []
    layouts: dict[str, str] = {}
    unresolved: list[str] = []
    for row in manifest:
        key = f"{row['topic-id']}:{row['question-id']}"
        manual_entry = manual.get(key)
        if row["seed-state"] == "exact-ready":
            layout = row["layout-template"]
            answers = BLANK_ANSWER_RE.findall(layout)
            if manual_entry:
                manual_answers = list(manual_entry["answers"])
                if manual_answers != answers:
                    raise ValueError(
                        f"Manual answers differ from canonical exact blank for {key}: "
                        f"{manual_answers} != {answers}"
                    )
                manual_layout = manual_entry.get("layout")
                if manual_layout is not None:
                    if not isinstance(manual_layout, str):
                        raise ValueError(f"Manual layout for {key} must be a string")
                    layout = manual_layout
                answer_source = str(manual_entry.get("source", "manual-solution"))
            else:
                answer_source = row["seed-source"]
        elif manual_entry:
            answers = list(manual_entry["answers"])
            layout_value = manual_entry.get("layout")
            if layout_value is not None and not isinstance(layout_value, str):
                raise ValueError(f"Manual layout for {key} must be a string")
            layout = layout_value or generic_layout(row, answers)
            answer_source = str(manual_entry.get("source", "manual-solution"))
        elif row["seed-state"] == "semantic-solved":
            blank_count = int(row["source-blank-count"])
            if key in SEMANTIC_LAYOUT_OVERRIDES:
                answers, layout = SEMANTIC_LAYOUT_OVERRIDES[key]
            elif blank_count > 1:
                answers = MULTI_SEMANTIC_OVERRIDES.get(key, [])
            else:
                answers = [latex_to_keyboard(row["correct-content"])]
            if key not in SEMANTIC_LAYOUT_OVERRIDES and len(answers) != blank_count:
                raise ValueError(f"Could not normalize semantic seed {key}: {answers}")
            if not all(answers):
                raise ValueError(f"Could not normalize semantic seed {key}: {answers}")
            if key not in SEMANTIC_LAYOUT_OVERRIDES:
                layout = generic_layout(row, answers)
            answer_source = "canonical-correct-option-normalized"
        else:
            unresolved.append(key)
            continue

        inline = BLANK_ANSWER_RE.findall(layout)
        if inline != answers:
            raise ValueError(f"Layout answers differ for {key}: {inline} != {answers}")
        output.append(
            {
                "study-order": row["study-order"],
                "topic-id": row["topic-id"],
                "question-number": row["question-number"],
                "question-id": row["question-id"],
                "answer": ", ".join(answers),
                "expected-occurrences": row["total-occurrences"],
                "answer-source": answer_source,
            }
        )
        layouts[key] = layout
    return output, layouts, unresolved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--manual", type=Path, default=DEFAULT_MANUAL)
    parser.add_argument("--answers", type=Path, default=DEFAULT_ANSWERS)
    parser.add_argument("--layouts", type=Path, default=DEFAULT_LAYOUTS)
    args = parser.parse_args()

    manifest = read_csv(args.manifest.resolve())
    manual = load_manual(args.manual.resolve())
    rows, layouts, unresolved = build(manifest, manual)

    fields = [
        "study-order",
        "topic-id",
        "question-number",
        "question-id",
        "answer",
        "expected-occurrences",
        "answer-source",
    ]
    with args.answers.resolve().open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    args.layouts.resolve().write_text(
        json.dumps(layouts, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Registry rows: {len(rows)}")
    print(f"Unresolved imported questions: {len(unresolved)}")
    print(f"Wrote {args.answers}")
    print(f"Wrote {args.layouts}")
    if unresolved:
        print("Next unresolved keys: " + ", ".join(unresolved[:20]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
