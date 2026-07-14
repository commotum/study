#!/usr/bin/env python3
"""Build the work manifest for imported Math Academy free-response quizzes.

The global question ledger intentionally contains topics that are not imported
into this vault.  This script therefore starts from quiz blocks physically
present below ``vault/MA`` and uses the ledger only to classify those imported
questions.  Active copies below ``vault/252`` and ``vault/253`` are then joined
by stable ``(topic-id, question-id)`` keys.

The resulting manifest distinguishes exact-answer seeds already repaired in a
course copy from canonical radio blocks whose correct option is known but still
needs a keyboard-friendly answer/layout.  It never queues ledger-only rows.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

from repair_course_free_response_quizzes import (
    BLANK_ANSWER_RE,
    LESSON_ID_RE,
    MARKER,
    OPTION_BLOCK_RE,
    QUESTION_RE,
    QUIZ_ID_RE,
    QUIZ_RE,
    QUIZ_TYPE_RE,
    correct_option_content,
    load_ledger,
    load_source_questions,
    load_topic_metadata,
    read_csv,
    rel,
    resolve_repo_path,
    topic_number_key,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
MA_ROOT = REPO_ROOT / "vault" / "MA"
ACTIVE_ROOTS = (REPO_ROOT / "vault" / "252", REPO_ROOT / "vault" / "253")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(<[^>]+>\)")
CONTENT_RE = re.compile(
    r"^content:\s*\|-\s*$\n(?P<content>.*?)(?=^options:\s*$|\Z)",
    re.MULTILINE | re.DOTALL,
)


def lesson_id(text: str) -> str | None:
    match = LESSON_ID_RE.search(text)
    return match.group("id") if match else None


def raw_quiz_id(body: str) -> str | None:
    match = QUIZ_ID_RE.search(body)
    return match.group("id") if match else None


def quiz_type(body: str) -> str:
    match = QUIZ_TYPE_RE.search(body)
    return match.group("type") if match else ""


def block_content(body: str) -> str:
    match = CONTENT_RE.search(body)
    if not match:
        return ""
    lines = match.group("content").rstrip("\n").splitlines()
    return "\n".join(line[2:] if line.startswith("  ") else line for line in lines)


def normalize_image_placeholders(layout: str) -> str:
    counter = 0

    def replace(_: re.Match[str]) -> str:
        nonlocal counter
        counter += 1
        return f"{{{{image-{counter}}}}}"

    return IMAGE_RE.sub(replace, layout)


def load_exact_seeds() -> dict[tuple[str, str], dict[str, str]]:
    result: dict[tuple[str, str], dict[str, str]] = {}
    for course in ("252", "253"):
        answer_path = REPO_ROOT / "util" / f"{course}_free_response_answer_key.csv"
        layout_path = REPO_ROOT / "util" / f"{course}_exact_blank_layouts.json"
        if not answer_path.exists() or not layout_path.exists():
            continue
        layouts = json.loads(layout_path.read_text(encoding="utf-8"))
        for row in read_csv(answer_path):
            key = (row["topic-id"].strip(), row["question-id"].strip())
            layout_key = f"{key[0]}:{key[1]}"
            candidate = {
                "answer": row["answer"],
                "layout-template": normalize_image_placeholders(layouts[layout_key]),
                "seed-course": course,
            }
            prior = result.get(key)
            if prior and (
                prior["answer"] != candidate["answer"]
                or prior["layout-template"] != candidate["layout-template"]
            ):
                raise ValueError(f"Conflicting exact seeds for {key}: {prior} vs {candidate}")
            if prior:
                prior["seed-course"] = ",".join(sorted({*prior["seed-course"].split(","), course}))
            else:
                result[key] = candidate
    return result


def canonical_number_index(
    metadata: dict[str, dict[str, object]],
) -> dict[tuple[str, int], str]:
    result: dict[tuple[str, int], str] = {}
    for topic_id, meta in metadata.items():
        for question_id, item in load_source_questions(str(meta.get("source-path", ""))).items():
            number = item.get("question_number")
            if number is None:
                continue
            key = (topic_id, int(number))
            prior = result.get(key)
            if prior and prior != question_id:
                raise ValueError(f"Conflicting source question ids for {key}: {prior}, {question_id}")
            result[key] = question_id
    return result


def identify_question(
    topic_id: str,
    number: int,
    body: str,
    number_index: dict[tuple[str, int], str],
) -> str | None:
    raw = raw_quiz_id(body)
    if raw and raw.lower().startswith("ma-"):
        return raw[3:]
    return number_index.get((topic_id, number))


def scan_placements(
    root: Path,
    number_index: dict[tuple[str, int], str],
) -> dict[tuple[str, str], list[dict[str, object]]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        topic_id = lesson_id(text)
        if not topic_id:
            continue
        for section in QUESTION_RE.finditer(text):
            number = int(section.group("number"))
            for quiz in QUIZ_RE.finditer(section.group("body")):
                body = quiz.group("body")
                question_id = identify_question(topic_id, number, body, number_index)
                if not question_id:
                    continue
                grouped[(topic_id, question_id)].append(
                    {
                        "path": rel(path),
                        "number": number,
                        "raw-id": raw_quiz_id(body) or "",
                        "type": quiz_type(body),
                        "body": body,
                        "content": block_content(body),
                        "marker": MARKER in body,
                    }
                )
    return grouped


def group_name(path: str) -> str:
    parts = Path(path).parts
    try:
        return parts[parts.index("MA") + 1]
    except (ValueError, IndexError):
        return ""


def source_prompt(item: dict[str, object] | None) -> str:
    if not item:
        return ""
    prompt = item.get("prompt")
    if isinstance(prompt, dict):
        value = prompt.get("readable_text")
        if isinstance(value, str):
            return value
    value = item.get("readable_text")
    return value if isinstance(value, str) else ""


def source_blank_count(item: dict[str, object] | None) -> int:
    if not item:
        return 0
    blanks = item.get("free_entry_blanks")
    return len(blanks) if isinstance(blanks, list) else 0


def canonical_correct(placements: list[dict[str, object]]) -> tuple[str, str]:
    candidates = {
        correct_option_content(str(item["body"]))
        for item in placements
        if correct_option_content(str(item["body"])) != ("", "")
    }
    if not candidates:
        return "", ""
    labels = {label for label, _ in candidates}
    if len(labels) > 1:
        raise ValueError(f"Divergent canonical correct labels: {sorted(candidates)}")
    # Duplicate course placements sometimes phrase the same answer differently
    # (for example, ``2 and 2`` versus two fully written one-sided limits).
    # The shorter representation is the better semantic seed for keyboard
    # normalization, while the source prompt still supplies the blank context.
    return min(candidates, key=lambda candidate: (len(candidate[1]), candidate[1]))


def canonical_exact_seed(placements: list[dict[str, object]]) -> dict[str, str] | None:
    """Return a shared exact-blank seed when every canonical placement is repaired."""
    candidates: set[tuple[str, str]] = set()
    for placement in placements:
        body = str(placement["body"])
        if placement["type"] != "blank" or not re.search(
            r"^require_exact:\s*true\s*$", body, re.MULTILINE
        ):
            return None
        layout = normalize_image_placeholders(str(placement["content"]))
        answers = BLANK_ANSWER_RE.findall(layout)
        if not answers:
            raise ValueError(
                f"Canonical exact blank has no inline answers: {placement['path']}"
            )
        candidates.add((", ".join(answers), layout))
    if len(candidates) != 1:
        raise ValueError(f"Canonical exact placements have divergent layouts: {candidates}")
    answer, layout = next(iter(candidates))
    return {"answer": answer, "layout-template": layout}


def build_rows() -> tuple[list[dict[str, str]], dict[str, str]]:
    ledger = load_ledger()
    metadata = load_topic_metadata(MA_ROOT)
    number_index = canonical_number_index(metadata)
    canonical = scan_placements(MA_ROOT, number_index)
    active: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for root in ACTIVE_ROOTS:
        for key, placements in scan_placements(root, number_index).items():
            active[key].extend(placements)
    seeds = load_exact_seeds()

    imported_keys = [
        key
        for key in canonical
        if ledger.get(key, {}).get("question-type") == "free-response"
    ]

    def order_key(key: tuple[str, str]) -> tuple[object, ...]:
        topic_id, _ = key
        meta = metadata.get(topic_id, {})
        numbers = [int(item["number"]) for item in canonical[key]]
        return (
            int(meta.get("layer", 10**9)),
            str(meta.get("course", "")),
            topic_number_key(str(meta.get("topic-number", ""))),
            int(meta.get("row-index", 10**9)),
            min(numbers),
            int(key[1]) if key[1].isdigit() else key[1],
        )

    rows: list[dict[str, str]] = []
    layout_seeds: dict[str, str] = {}
    source_cache: dict[str, dict[str, dict[str, object]]] = {}
    for study_order, key in enumerate(sorted(imported_keys, key=order_key), start=1):
        topic_id, question_id = key
        meta = metadata.get(topic_id, {})
        canonical_places = canonical[key]
        active_places = active.get(key, [])
        source_questions = source_cache.setdefault(
            topic_id,
            load_source_questions(str(meta.get("source-path", ""))),
        )
        source_item = source_questions.get(question_id)
        exact_seed = seeds.get(key)
        canonical_seed = canonical_exact_seed(canonical_places)
        correct_label, correct_content = canonical_correct(canonical_places)
        if canonical_seed:
            if exact_seed and (
                exact_seed["answer"] != canonical_seed["answer"]
                or exact_seed["layout-template"] != canonical_seed["layout-template"]
            ):
                raise ValueError(
                    f"Canonical/course exact seed conflict for {key}: "
                    f"{canonical_seed} vs {exact_seed}"
                )
            seed_state = "exact-ready"
            seed_source = "canonical-exact-blank"
            keyboard_answer = canonical_seed["answer"]
            layout_template = canonical_seed["layout-template"]
            layout_seeds[f"{topic_id}:{question_id}"] = layout_template
        elif exact_seed:
            seed_state = "exact-ready"
            seed_source = f"course-{exact_seed['seed-course']}"
            keyboard_answer = exact_seed["answer"]
            layout_template = exact_seed["layout-template"]
            layout_seeds[f"{topic_id}:{question_id}"] = layout_template
        elif correct_label:
            seed_state = "semantic-solved"
            seed_source = "canonical-correct-option"
            keyboard_answer = ""
            layout_template = ""
        else:
            seed_state = "solve-required"
            seed_source = ""
            keyboard_answer = ""
            layout_template = ""

        ledger_row = ledger[key]
        first_path = str(canonical_places[0]["path"])
        rows.append(
            {
                "study-order": str(study_order),
                "layer": str(meta.get("layer", "")),
                "group": group_name(first_path),
                "course": str(meta.get("course", "")),
                "topic-id": topic_id,
                "topic-code": str(meta.get("topic-number", "")),
                "topic-name": str(meta.get("topic-name", "")),
                "question-number": str(min(int(item["number"]) for item in canonical_places)),
                "question-numbers": ",".join(
                    str(number) for number in sorted({int(item["number"]) for item in canonical_places})
                ),
                "question-id": question_id,
                "source-blank-count": str(source_blank_count(source_item)),
                "canonical-occurrences": str(len(canonical_places)),
                "active-copy-occurrences": str(len(active_places)),
                "total-occurrences": str(len(canonical_places) + len(active_places)),
                "current-types": ",".join(
                    sorted({str(item["type"]) for item in [*canonical_places, *active_places]})
                ),
                "marker-occurrences": str(
                    sum(bool(item["marker"]) for item in [*canonical_places, *active_places])
                ),
                "ledger-status": ledger_row.get("quiz-status", ""),
                "seed-state": seed_state,
                "seed-source": seed_source,
                "keyboard-answer": keyboard_answer,
                "correct-label": correct_label,
                "correct-content": correct_content,
                "source-prompt": source_prompt(source_item),
                "current-content": str(canonical_places[0]["content"]),
                "layout-template": layout_template,
                "canonical-placements": ";".join(str(item["path"]) for item in canonical_places),
                "active-copy-placements": ";".join(str(item["path"]) for item in active_places),
            }
        )
    return rows, layout_seeds


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=REPO_ROOT / "util" / "ma_imported_free_response_manifest.csv",
    )
    parser.add_argument(
        "--seed-layouts",
        type=Path,
        default=REPO_ROOT / "util" / "ma_free_response_seed_layouts.json",
    )
    args = parser.parse_args()

    rows, layouts = build_rows()
    if not rows:
        raise ValueError("No imported MA free-response questions found")
    write_csv(args.manifest.resolve(), rows)
    args.seed_layouts.resolve().write_text(
        json.dumps(layouts, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row["seed-state"]] += 1
    print(f"Imported unique free-response questions: {len(rows)}")
    print(f"Canonical placements: {sum(int(row['canonical-occurrences']) for row in rows)}")
    print(f"Active 252/253 placements: {sum(int(row['active-copy-occurrences']) for row in rows)}")
    print(f"Exact-ready seeds: {counts['exact-ready']}")
    print(f"Semantic-solved seeds: {counts['semantic-solved']}")
    print(f"Solve-required: {counts['solve-required']}")
    print(f"Wrote {args.manifest}")
    print(f"Wrote {args.seed_layouts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
