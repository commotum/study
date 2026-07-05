#!/usr/bin/env python3
"""Rebuild Math Academy group-level CSV indices from the vault layout."""

from __future__ import annotations

import csv
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MA_ROOT = REPO_ROOT / "vault" / "MA"

ROOT_CSV_NAMES = {
    "catalog": "catalog.csv",
    "courses": "courses.csv",
    "units": "units.csv",
    "modules": "modules.csv",
    "prerequisites": "prerequisites.csv",
    "questions": "questions.csv",
}

GROUP_TOPIC_FIELDS = [
    "topic-id",
    "topic-name",
    "layer",
    "courses",
    "topic-codes",
    "lesson-paths",
    "source-paths",
]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def course_prefix(value: str) -> str:
    return value.split(".", 1)[0]


def numeric_key(value: str) -> tuple[int, str]:
    return (int(value), value) if value.isdigit() else (10**9, value)


def append_unique(values: list[str], value: str) -> None:
    if value and value not in values:
        values.append(value)


def discover_groups() -> dict[Path, list[str]]:
    groups: dict[Path, list[str]] = {}
    for group_dir in sorted(path for path in MA_ROOT.iterdir() if path.is_dir()):
        course_codes = sorted(
            course_dir.name
            for course_dir in group_dir.iterdir()
            if course_dir.is_dir() and (course_dir / "topics.csv").exists()
        )
        if course_codes:
            groups[group_dir] = course_codes
    return groups


def collect_group_prerequisites(group_dir: Path, topic_ids: set[str]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    rows: list[dict[str, str]] = []
    for prerequisites_path in sorted(group_dir.glob("*/prerequisites.csv")):
        _, local_rows = read_csv(prerequisites_path)
        for row in local_rows:
            topic = row.get("topic", "")
            requires = row.get("requires", "")
            if not topic or not requires or topic not in topic_ids:
                continue
            key = (topic, requires)
            if key in seen:
                continue
            seen.add(key)
            rows.append({"topic": topic, "requires": requires})
    return sorted(rows, key=lambda row: (numeric_key(row["topic"]), numeric_key(row["requires"])))


def build_group_topics(catalog_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_topic: dict[str, dict[str, str | list[str]]] = {}
    for row in catalog_rows:
        topic_id = row["topic-id"]
        topic = by_topic.setdefault(
            topic_id,
            {
                "topic-name": row["topic-name"],
                "layers": [],
                "courses": [],
                "topic-codes": [],
                "lesson-paths": [],
                "source-paths": [],
            },
        )
        layer = row.get("layer", "")
        if layer:
            topic["layers"].append(layer)
        course = course_prefix(row["topic-code"])
        append_unique(topic["courses"], course)
        append_unique(topic["topic-codes"], row.get("topic-code", ""))
        append_unique(topic["lesson-paths"], row.get("lesson-path", ""))
        append_unique(topic["source-paths"], row.get("source-path", ""))

    rows: list[dict[str, str]] = []
    for topic_id, topic in by_topic.items():
        layers = topic["layers"]
        numeric_layers = [int(layer) for layer in layers if str(layer).isdigit()]
        rows.append(
            {
                "topic-id": topic_id,
                "topic-name": str(topic["topic-name"]),
                "layer": str(min(numeric_layers)) if numeric_layers else "",
                "courses": ";".join(topic["courses"]),
                "topic-codes": ";".join(topic["topic-codes"]),
                "lesson-paths": ";".join(topic["lesson-paths"]),
                "source-paths": ";".join(topic["source-paths"]),
            }
        )
    return sorted(rows, key=lambda row: (numeric_key(row["layer"]), numeric_key(row["topic-id"])))


def main() -> int:
    groups = discover_groups()
    root_data = {
        name: read_csv(MA_ROOT / csv_name)
        for name, csv_name in ROOT_CSV_NAMES.items()
        if (MA_ROOT / csv_name).exists()
    }
    catalog_fields, catalog_rows = root_data["catalog"]
    _, question_rows = root_data["questions"]

    summaries: list[str] = []
    for group_dir, course_codes in groups.items():
        course_set = set(course_codes)
        group_catalog_rows = [
            row for row in catalog_rows if course_prefix(row.get("topic-code", "")) in course_set
        ]
        group_topic_ids = {row["topic-id"] for row in group_catalog_rows}

        write_csv(group_dir / "catalog.csv", catalog_fields, group_catalog_rows)
        write_csv(group_dir / "topics.csv", GROUP_TOPIC_FIELDS, build_group_topics(group_catalog_rows))
        write_csv(
            group_dir / "prerequisites.csv",
            ["topic", "requires"],
            collect_group_prerequisites(group_dir, group_topic_ids),
        )
        write_csv(
            group_dir / "questions.csv",
            root_data["questions"][0],
            [row for row in question_rows if row.get("topic-id") in group_topic_ids],
        )

        for name, code_column in (("courses", "course-code"), ("units", "unit-code"), ("modules", "module-code")):
            fieldnames, rows = root_data[name]
            write_csv(
                group_dir / f"{name}.csv",
                fieldnames,
                [row for row in rows if course_prefix(row.get(code_column, "")) in course_set],
            )

        summaries.append(
            f"{group_dir.relative_to(REPO_ROOT).as_posix()}: "
            f"{len(course_codes)} courses, {len(group_catalog_rows)} catalog rows, {len(group_topic_ids)} topics"
        )

    print("\n".join(summaries))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
