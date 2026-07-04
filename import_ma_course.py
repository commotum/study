#!/usr/bin/env python3
"""Import a Math Academy course into the local study/vault/MA layout.

Example:
    ./import_ma_course.py MF1 --dry-run
    ./import_ma_course.py MF1 --overwrite
    ./import_ma_course.py MF1 MF2 MF3 --overwrite

The importer reads the canonical Math Academy data under
/Users/jake/Developer/MA/DATA and creates a categorized course folder like:

    vault/MA/Mathematical-Foundations/MF1/
        Home.md
        0. Table of Contents/TOC.md
        1. Unit Name/
            1.1. Module Name/
                Lessons/1.1.1. Lesson Name.md
                Source/1.1.1. Lesson Name/<id>.html
                Source/1.1.1. Lesson Name/<id>.json
                Source/1.1.1. Lesson Name/Images/...
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import sys
from collections import defaultdict, deque
from dataclasses import asdict, dataclass, field
from pathlib import Path


DEFAULT_MA_DATA_ROOT = Path("/Users/jake/Developer/MA/DATA")
DEFAULT_TARGET_ROOT = Path("/Users/jake/Developer/study/vault/MA")
QUEUE_SIZE = 5
DEFAULT_QUEUE_PREREQUISITE_SCOPE = "course"
COURSE_CATEGORIES = {
    "MF1": "Mathematical-Foundations",
    "MF2": "Mathematical-Foundations",
    "MF3": "Mathematical-Foundations",
    "CA1": "Single-Variable-Calculus",
    "CA2": "Single-Variable-Calculus",
    "CAB": "Single-Variable-Calculus",
    "CBC": "Single-Variable-Calculus",
    "DEQ": "Mathematical-Analysis-&-Modeling",
    "LAL": "Mathematical-Analysis-&-Modeling",
    "MVC": "Mathematical-Analysis-&-Modeling",
    "PAS": "Mathematical-Analysis-&-Modeling",
    "DSM": "Mathematical-Structures-&-Proof",
    "MOP": "Mathematical-Structures-&-Proof",
    "MML": "Mathematical-Methods-for-Machine-Learning",
    "PS1": "Mathematical-Methods-for-the-Physical-Sciences",
    "PS2": "Mathematical-Methods-for-the-Physical-Sciences",
}

UNIT_RE = re.compile(r"^###\s+(\d+)\.\s+(.+?)(?:\s+\d+\s+topics?)?\s*$")
MODULE_RE = re.compile(r"^\*\*(\d+\.\d+)\.\s+(.+?)\*\*\s*$")
TOPIC_RE = re.compile(r"^-\s+(\d+(?:\.\d+)+)\.\s+(.+?)\s*$")
IMAGE_LINK_RE = re.compile(r"!\[([^\]]*)\]\(<?Source/Images/([^)>]+)>?\)")
LESSON_MD_LINK_RE = re.compile(r"\]\(\.\./(\d+)/(\d+)\.md\)")
LESSON_FOOTER_RE = re.compile(
    r"\n+```update-progress\s*\n```\s*"
    r"(?:\n+\[\[[^\]\n]+\|Home\]\]\s*)?"
    r"(?:\n+\[\[[^\]\n]+\|Table of Contents\]\]\s*)?$",
    re.MULTILINE,
)


@dataclass(frozen=True)
class CourseInfo:
    code: str
    course_id: str
    name: str


@dataclass(frozen=True)
class Unit:
    number: str
    name: str
    folder_name: str
    modules: list["Module"] = field(default_factory=list)


@dataclass(frozen=True)
class Module:
    number: str
    name: str
    folder_name: str
    topics: list["Topic"] = field(default_factory=list)


@dataclass(frozen=True)
class Topic:
    topic_id: str
    topic_code: str
    number: str
    name: str
    lesson_file_name: str
    source_folder_name: str
    unit_folder_name: str
    module_folder_name: str


@dataclass(frozen=True)
class Placement:
    course_code: str
    topic_id: str
    topic_code: str
    number: str
    name: str
    lesson_relative_path: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a CTS-style study/vault/MA course folder from Math Academy source data."
    )
    parser.add_argument(
        "course_codes",
        nargs="*",
        help="Course code(s), e.g. MF1 MF2 MF3, CA1 CA2, DEQ, PS1 PS2.",
    )
    parser.add_argument(
        "--target-root",
        type=Path,
        default=DEFAULT_TARGET_ROOT,
        help=f"Destination root. Default: {DEFAULT_TARGET_ROOT}",
    )
    parser.add_argument(
        "--ma-data-root",
        type=Path,
        default=DEFAULT_MA_DATA_ROOT,
        help=f"Math Academy DATA root. Default: {DEFAULT_MA_DATA_ROOT}",
    )
    parser.add_argument("--overwrite", action="store_true", help="Replace an existing generated course folder.")
    parser.add_argument(
        "--indexes-only",
        action="store_true",
        help="Only refresh topics.csv, prerequisites.csv, Home.md, and manifest metadata.",
    )
    parser.add_argument(
        "--refresh-lesson-nav",
        action="store_true",
        help="Refresh lesson footers with update-progress, Home, and Table of Contents links.",
    )
    parser.add_argument(
        "--queue-prerequisite-scope",
        choices=("course", "global"),
        default=DEFAULT_QUEUE_PREREQUISITE_SCOPE,
        help=(
            "Prerequisite scope for the generated Home queue. "
            "Default: course, which ignores prerequisites not present in the course."
        ),
    )
    parser.add_argument("--dry-run", action="store_true", help="Validate and print the plan without writing files.")
    parser.add_argument("--list-courses", action="store_true", help="List supported course codes and exit.")
    return parser.parse_args()


def safe_filename(value: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" .-")
    return cleaned or "Untitled"


def markdown_path(path: Path) -> str:
    value = path.as_posix()
    return f"<{value}>" if any(char in value for char in " ()[]'") else value


def markdown_relpath(from_dir: Path, to_file: Path) -> str:
    rel = Path(os.path.relpath(to_file, start=from_dir))
    return markdown_path(rel)


def course_dir_for_code(target_root: Path, course_code: str) -> Path:
    category = COURSE_CATEGORIES.get(course_code.upper())
    return target_root / category / course_code if category else target_root / course_code


def course_vault_prefix(target_root: Path, course_dir: Path) -> Path:
    try:
        return course_dir.relative_to(target_root.parent)
    except ValueError:
        return Path(target_root.name) / course_dir.name


def load_courses(ma_data_root: Path) -> dict[str, CourseInfo]:
    courses_path = ma_data_root / "Courses.csv"
    with courses_path.open(newline="", encoding="utf-8") as handle:
        return {
            row["course-code"].upper(): CourseInfo(
                code=row["course-code"].upper(),
                course_id=row["course-id"],
                name=row["course-name"],
            )
            for row in csv.DictReader(handle)
        }


def load_catalog(ma_data_root: Path) -> dict[str, str]:
    catalog_path = ma_data_root / "Catalog.csv"
    with catalog_path.open(newline="", encoding="utf-8") as handle:
        return {row["topic-code"]: row["topic-id"] for row in csv.DictReader(handle)}


def numeric_id_key(value: str) -> tuple[int, str]:
    return (int(value), value) if value.isdigit() else (sys.maxsize, value)


def compute_global_topic_layers(ma_data_root: Path) -> dict[str, int]:
    """Return prerequisite DAG layers for every known topic id."""
    topic_ids: set[str] = set()
    for csv_name in ("Catalog.csv", "Topics.csv"):
        path = ma_data_root / csv_name
        with path.open(newline="", encoding="utf-8") as handle:
            topic_ids.update(row["topic-id"] for row in csv.DictReader(handle))

    prerequisites: dict[str, set[str]] = defaultdict(set)
    dependents: dict[str, set[str]] = defaultdict(set)
    with (ma_data_root / "Prerequisites.csv").open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            topic_id = row["topic"]
            required_id = row["requires"]
            topic_ids.update((topic_id, required_id))
            prerequisites[topic_id].add(required_id)
            dependents[required_id].add(topic_id)

    remaining_prerequisites = {topic_id: len(prerequisites[topic_id]) for topic_id in topic_ids}
    layers = {topic_id: 0 for topic_id, count in remaining_prerequisites.items() if count == 0}
    queue = deque(sorted(layers, key=numeric_id_key))
    seen_count = 0

    while queue:
        topic_id = queue.popleft()
        seen_count += 1
        for dependent_id in sorted(dependents[topic_id], key=numeric_id_key):
            layers[dependent_id] = max(layers.get(dependent_id, 0), layers[topic_id] + 1)
            remaining_prerequisites[dependent_id] -= 1
            if remaining_prerequisites[dependent_id] == 0:
                queue.append(dependent_id)

    if seen_count != len(topic_ids):
        cycle_count = len(topic_ids) - seen_count
        raise ValueError(f"Prerequisite graph contains {cycle_count} topic(s) in cycles")

    return layers


def find_course_map(ma_data_root: Path, course_name: str) -> Path:
    maps_dir = ma_data_root / "Course-Maps"
    candidates: list[Path] = []
    for path in sorted(maps_dir.glob("*.md")):
        first_heading = ""
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                first_heading = line[2:].strip()
                break
        if first_heading == course_name:
            return path
        if normalize_title(first_heading) == normalize_title(course_name):
            candidates.append(path)

    if len(candidates) == 1:
        return candidates[0]

    expected_stem = safe_filename(course_name.replace("&", "And")).replace(" ", "-")
    expected_path = maps_dir / f"{expected_stem}.md"
    if expected_path.exists():
        return expected_path

    raise FileNotFoundError(f"No course map found for {course_name!r} under {maps_dir}")


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def parse_course_map(course_code: str, map_path: Path, catalog: dict[str, str]) -> tuple[list[Unit], list[Topic]]:
    in_course_content = False
    current_unit: Unit | None = None
    current_module: Module | None = None
    units: list[Unit] = []
    topics: list[Topic] = []

    for line_number, line in enumerate(map_path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped == "## Course Content":
            in_course_content = True
            continue
        if not in_course_content:
            continue

        unit_match = UNIT_RE.match(stripped)
        if unit_match:
            number, name = unit_match.groups()
            current_unit = Unit(
                number=number,
                name=name,
                folder_name=safe_filename(f"{number}. {name}"),
                modules=[],
            )
            units.append(current_unit)
            current_module = None
            continue

        module_match = MODULE_RE.match(stripped)
        if module_match:
            if current_unit is None:
                raise ValueError(f"Module before unit in {map_path}:{line_number}")
            number, name = module_match.groups()
            current_module = Module(
                number=number,
                name=name,
                folder_name=safe_filename(f"{number}. {name}"),
                topics=[],
            )
            current_unit.modules.append(current_module)
            continue

        topic_match = TOPIC_RE.match(stripped)
        if topic_match:
            if current_unit is None or current_module is None:
                raise ValueError(f"Topic before module in {map_path}:{line_number}: {stripped}")
            number, name = topic_match.groups()
            topic_code = f"{course_code}.{number}"
            topic_id = catalog.get(topic_code)
            if topic_id is None:
                raise KeyError(f"{map_path}:{line_number}: no topic-id found in Catalog.csv for {topic_code}")
            topic = Topic(
                topic_id=topic_id,
                topic_code=topic_code,
                number=number,
                name=name,
                lesson_file_name=safe_filename(f"{number}. {name}.md"),
                source_folder_name=safe_filename(f"{number}. {name}"),
                unit_folder_name=current_unit.folder_name,
                module_folder_name=current_module.folder_name,
            )
            current_module.topics.append(topic)
            topics.append(topic)
            continue

    if not units:
        raise ValueError(f"No course content parsed from {map_path}")
    if not topics:
        raise ValueError(f"No topics parsed from {map_path}")

    return units, topics


def topic_lesson_relpath(topic: Topic) -> Path:
    return (
        Path(topic.unit_folder_name)
        / topic.module_folder_name
        / "Lessons"
        / topic.lesson_file_name
    )


def topic_source_relpath(topic: Topic) -> Path:
    return (
        Path(topic.unit_folder_name)
        / topic.module_folder_name
        / "Source"
        / topic.source_folder_name
    )


def build_all_placements(
    *,
    ma_data_root: Path,
    courses: dict[str, CourseInfo],
    catalog: dict[str, str],
) -> dict[str, list[Placement]]:
    placements: dict[str, list[Placement]] = {}

    for course_code, course in courses.items():
        map_path = find_course_map(ma_data_root, course.name)
        _, topics = parse_course_map(course_code, map_path, catalog)
        for topic in topics:
            placement = Placement(
                course_code=course_code,
                topic_id=topic.topic_id,
                topic_code=topic.topic_code,
                number=topic.number,
                name=topic.name,
                lesson_relative_path=topic_lesson_relpath(topic).as_posix(),
            )
            placements.setdefault(topic.topic_id, []).append(placement)

    return placements


def choose_placement(
    topic_id: str,
    *,
    current_course_code: str,
    placements: dict[str, list[Placement]],
) -> Placement | None:
    choices = placements.get(topic_id, [])
    if not choices:
        return None
    for placement in choices:
        if placement.course_code == current_course_code:
            return placement
    return choices[0]


def rewrite_markdown(
    *,
    text: str,
    topic: Topic,
    target_root: Path,
    target_course_dir: Path,
    current_course_code: str,
    placements: dict[str, list[Placement]],
    unresolved_links: list[dict[str, str]],
) -> str:
    source_rel = Path("..") / "Source" / topic.source_folder_name / "Images"

    def replace_image(match: re.Match[str]) -> str:
        alt_text, image_name = match.groups()
        return f"![{alt_text}]({markdown_path(source_rel / image_name)})"

    text = IMAGE_LINK_RE.sub(replace_image, text)

    lesson_parent = target_course_dir / topic_lesson_relpath(topic).parent

    def replace_lesson_link(match: re.Match[str]) -> str:
        display_id, target_id = match.groups()
        if display_id != target_id:
            unresolved_links.append(
                {
                    "topic_id": topic.topic_id,
                    "target_id": target_id,
                    "reason": f"mismatched raw link ids: {display_id} != {target_id}",
                }
            )
            return match.group(0)
        placement = choose_placement(target_id, current_course_code=current_course_code, placements=placements)
        if placement is None:
            unresolved_links.append(
                {
                    "topic_id": topic.topic_id,
                    "target_id": target_id,
                    "reason": "no placement found in Course-Maps/Catalog.csv",
                }
            )
            return match.group(0)
        target_file = course_dir_for_code(target_root, placement.course_code) / placement.lesson_relative_path
        return f"]({markdown_relpath(lesson_parent, target_file)})"

    text = LESSON_MD_LINK_RE.sub(replace_lesson_link, text)
    return ensure_lesson_metadata(text, topic)


def ensure_lesson_metadata(text: str, topic: Topic) -> str:
    if re.search(r"lesson-id:\s*" + re.escape(topic.topic_id), text):
        return text

    lines = text.splitlines()
    metadata = [
        "",
        "<!--",
        f"lesson-id: {topic.topic_id}",
        f"topic-code: {topic.topic_code}",
        "-->",
    ]
    if lines and lines[0].startswith("# "):
        return "\n".join([lines[0], *metadata, *lines[1:]]) + "\n"
    return "\n".join([*metadata, "", text]).strip() + "\n"


def lesson_nav_footer(course: CourseInfo, target_root: Path, course_dir: Path) -> str:
    course_prefix = course_vault_prefix(target_root, course_dir)
    home_target = (course_prefix / "Home").as_posix()
    toc_target = (course_prefix / "0. Table of Contents" / "TOC").as_posix()
    return "\n\n```update-progress\n```\n\n" f"[[{home_target}|Home]]\n[[{toc_target}|Table of Contents]]\n"


def ensure_lesson_nav_footer(text: str, course: CourseInfo, target_root: Path, course_dir: Path) -> str:
    without_footer = LESSON_FOOTER_RE.sub("", text.rstrip())
    return without_footer + lesson_nav_footer(course, target_root, course_dir)


def copy_lesson_source(
    *,
    raw_lesson_dir: Path,
    topic: Topic,
    target_source_dir: Path,
    copied_files: list[str],
) -> None:
    source_dir = raw_lesson_dir / "Source"
    for suffix in ("html", "json"):
        source_file = source_dir / f"{topic.topic_id}.{suffix}"
        target_file = target_source_dir / f"{topic.topic_id}.{suffix}"
        if not source_file.exists():
            raise FileNotFoundError(f"Missing source file: {source_file}")
        target_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, target_file)
        copied_files.append(target_file.as_posix())

    images_source = source_dir / "Images"
    if images_source.exists():
        images_target = target_source_dir / "Images"
        shutil.copytree(images_source, images_target, dirs_exist_ok=True)
        for image in sorted(path for path in images_target.rglob("*") if path.is_file()):
            copied_files.append(image.as_posix())


def write_toc(course: CourseInfo, course_dir: Path, units: list[Unit]) -> Path:
    toc_path = course_dir / "0. Table of Contents" / "TOC.md"
    lines = [
        f"# {course.name}",
        "",
        "```check-progress",
        "```",
        "",
        "## Course Content",
        "",
    ]
    for unit in units:
        lines.append(f"- [ ] {unit.number}. {unit.name}")
        for module in unit.modules:
            lines.append(f"\t- [ ] {module.number}. {module.name}")
            for topic in module.topics:
                rel_stem = topic_lesson_relpath(topic).with_suffix("").as_posix()
                label = f"{topic.number}. {topic.name}"
                lines.append(f"\t\t- [ ] [[{rel_stem}|{label}]]")
    lines.append("")
    toc_path.parent.mkdir(parents=True, exist_ok=True)
    toc_path.write_text("\n".join(lines), encoding="utf-8")
    return toc_path


def build_prerequisite_map(rows: list[dict[str, str]]) -> dict[str, set[str]]:
    prerequisites: dict[str, set[str]] = {}
    for row in rows:
        prerequisites.setdefault(row["topic"], set()).add(row["requires"])
    return prerequisites


def select_available_topics(
    topics: list[Topic],
    *,
    topic_layers: dict[str, int],
    prerequisites: dict[str, set[str]],
    completed_topic_ids: set[str],
    limit: int,
    prerequisite_scope: str = DEFAULT_QUEUE_PREREQUISITE_SCOPE,
) -> list[Topic]:
    course_map_index = {topic.topic_id: index for index, topic in enumerate(topics)}
    local_topic_ids = set(course_map_index)
    available = [
        topic
        for topic in topics
        if topic.topic_id not in completed_topic_ids
        and (
            prerequisites.get(topic.topic_id, set())
            if prerequisite_scope == "global"
            else prerequisites.get(topic.topic_id, set()) & local_topic_ids
        ).issubset(completed_topic_ids)
    ]
    return sorted(
        available,
        key=lambda topic: (
            topic_layers.get(topic.topic_id, sys.maxsize),
            course_map_index[topic.topic_id],
            topic.number,
        ),
    )[:limit]


def write_home(
    course: CourseInfo,
    course_dir: Path,
    units: list[Unit],
    topics: list[Topic],
    *,
    topic_layers: dict[str, int],
    prerequisites: dict[str, set[str]],
    prerequisite_scope: str,
) -> Path:
    home_path = course_dir / "Home.md"
    next_topics = select_available_topics(
        topics,
        topic_layers=topic_layers,
        prerequisites=prerequisites,
        completed_topic_ids=set(),
        limit=QUEUE_SIZE,
        prerequisite_scope=prerequisite_scope,
    )
    lines = [
        f"# {course.name} Home",
        "",
        "## Next Topics",
        "",
    ]

    if next_topics:
        for index, topic in enumerate(next_topics, start=1):
            label = f"{topic.number}. {topic.name}"
            lines.append(f"{index}. [{label}]({markdown_path(topic_lesson_relpath(topic))})")
    else:
        lines.append("No eligible next lessons found.")

    lines.extend(
        [
            "",
            "## Progress",
            "",
            f"- Course: 0% (0/{len(topics)})",
            "",
        ]
    )

    for unit in units:
        unit_topic_count = sum(len(module.topics) for module in unit.modules)
        lines.append(f"- {unit.number}. {unit.name}: 0% (0/{unit_topic_count})")

    lines.extend(
        [
            "",
            "## History",
            "",
            "- No completed lessons yet.",
            "",
            "## Summary",
            "",
            f"- Completed lessons: 0 / {len(topics)}",
            f"- Queue size: {len(next_topics)} / {QUEUE_SIZE}",
            "",
            "<!--",
            "Generated by import_ma_course.py.",
            "Initial queue uses the lowest available prerequisite layer.",
            "External prerequisites are ignored for the queue."
            if prerequisite_scope == "course"
            else "External prerequisites are required for the queue.",
            "-->",
            "",
        ]
    )
    home_path.write_text("\n".join(lines), encoding="utf-8")
    return home_path


def load_course_prerequisite_rows(
    *,
    ma_data_root: Path,
    topic_ids: set[str],
) -> list[dict[str, str]]:
    source_path = ma_data_root / "Prerequisites.csv"
    with source_path.open(newline="", encoding="utf-8") as source_handle:
        return [row for row in csv.DictReader(source_handle) if row["topic"] in topic_ids]


def write_course_prerequisites(*, course_dir: Path, rows: list[dict[str, str]]) -> Path:
    target_path = course_dir / "prerequisites.csv"
    with target_path.open("w", newline="", encoding="utf-8") as target_handle:
        writer = csv.DictWriter(target_handle, fieldnames=["topic", "requires"])
        writer.writeheader()
        writer.writerows(rows)
    return target_path


def write_course_topics(
    *,
    course_dir: Path,
    topics: list[Topic],
    topic_layers: dict[str, int],
) -> Path:
    target_path = course_dir / "topics.csv"
    fieldnames = [
        "topic-id",
        "topic-code",
        "topic-number",
        "topic-name",
        "unit",
        "module",
        "lesson-path",
        "source-path",
        "layer",
        "nearest-integer-layer",
        "course-map-index",
    ]
    with target_path.open("w", newline="", encoding="utf-8") as target_handle:
        writer = csv.DictWriter(target_handle, fieldnames=fieldnames)
        writer.writeheader()
        for index, topic in enumerate(topics, start=1):
            layer = topic_layers[topic.topic_id]
            writer.writerow(
                {
                    "topic-id": topic.topic_id,
                    "topic-code": topic.topic_code,
                    "topic-number": topic.number,
                    "topic-name": topic.name,
                    "unit": topic.unit_folder_name,
                    "module": topic.module_folder_name,
                    "lesson-path": topic_lesson_relpath(topic).as_posix(),
                    "source-path": topic_source_relpath(topic).as_posix(),
                    "layer": layer,
                    "nearest-integer-layer": layer,
                    "course-map-index": index,
                }
            )
    return target_path


def validate_sources(ma_data_root: Path, topics: list[Topic]) -> None:
    lessons_root = ma_data_root / "Lessons"
    missing: list[str] = []
    for topic in topics:
        raw_lesson_dir = lessons_root / topic.topic_id
        required = [
            raw_lesson_dir / f"{topic.topic_id}.md",
            raw_lesson_dir / "Source" / f"{topic.topic_id}.html",
            raw_lesson_dir / "Source" / f"{topic.topic_id}.json",
        ]
        missing.extend(path.as_posix() for path in required if not path.exists())
    if missing:
        raise FileNotFoundError("Missing required lesson files:\n" + "\n".join(f"- {path}" for path in missing))


def validate_unique_paths(topics: list[Topic]) -> None:
    seen: dict[str, str] = {}
    seen_sources: dict[str, str] = {}
    collisions: list[str] = []
    for topic in topics:
        rel = topic_lesson_relpath(topic).as_posix()
        existing = seen.setdefault(rel, topic.topic_id)
        if existing != topic.topic_id:
            collisions.append(f"{rel}: {existing} and {topic.topic_id}")
        source_rel = topic_source_relpath(topic).as_posix()
        existing_source = seen_sources.setdefault(source_rel, topic.topic_id)
        if existing_source != topic.topic_id:
            collisions.append(f"{source_rel}: {existing_source} and {topic.topic_id}")
    if collisions:
        raise ValueError("Generated path collisions:\n" + "\n".join(f"- {item}" for item in collisions))


def prepare_target(course_dir: Path, *, overwrite: bool) -> None:
    if course_dir.exists() and any(course_dir.iterdir()) and not overwrite:
        raise FileExistsError(f"Target folder already exists and is not empty: {course_dir}")
    if course_dir.exists() and overwrite:
        shutil.rmtree(course_dir)
    course_dir.mkdir(parents=True, exist_ok=True)


def import_course(
    *,
    course: CourseInfo,
    ma_data_root: Path,
    target_root: Path,
    overwrite: bool,
    indexes_only: bool,
    refresh_lesson_nav: bool,
    queue_prerequisite_scope: str,
    dry_run: bool,
) -> dict[str, object]:
    catalog = load_catalog(ma_data_root)
    topic_layers = compute_global_topic_layers(ma_data_root)
    course_map = find_course_map(ma_data_root, course.name)
    units, topics = parse_course_map(course.code, course_map, catalog)
    validate_unique_paths(topics)
    if not indexes_only:
        validate_sources(ma_data_root, topics)
    placements = build_all_placements(
        ma_data_root=ma_data_root,
        courses=load_courses(ma_data_root),
        catalog=catalog,
    )

    course_dir = course_dir_for_code(target_root, course.code)
    topic_ids = {topic.topic_id for topic in topics}
    prerequisite_rows = load_course_prerequisite_rows(ma_data_root=ma_data_root, topic_ids=topic_ids)
    prerequisites = build_prerequisite_map(prerequisite_rows)
    initial_available = select_available_topics(
        topics,
        topic_layers=topic_layers,
        prerequisites=prerequisites,
        completed_topic_ids=set(),
        limit=QUEUE_SIZE,
        prerequisite_scope=queue_prerequisite_scope,
    )
    course_layers = [topic_layers[topic.topic_id] for topic in topics]

    plan = {
        "course_code": course.code,
        "course_name": course.name,
        "course_map": course_map.as_posix(),
        "target_dir": course_dir.as_posix(),
        "unit_count": len(units),
        "module_count": sum(len(unit.modules) for unit in units),
        "topic_count": len(topics),
        "prerequisite_edge_count": len(prerequisite_rows),
        "min_layer": min(course_layers),
        "max_layer": max(course_layers),
        "initial_available_count": len(initial_available),
        "refresh_lesson_nav": refresh_lesson_nav,
        "queue_prerequisite_scope": queue_prerequisite_scope,
    }
    if dry_run:
        return plan

    if indexes_only:
        course_dir.mkdir(parents=True, exist_ok=True)
    else:
        prepare_target(course_dir, overwrite=overwrite)
    copied_files: list[str] = []
    unresolved_links: list[dict[str, str]] = []
    lessons_root = ma_data_root / "Lessons"

    if not indexes_only:
        for topic in topics:
            raw_lesson_dir = lessons_root / topic.topic_id
            target_lesson_path = course_dir / topic_lesson_relpath(topic)
            target_source_dir = course_dir / topic_source_relpath(topic)
            target_lesson_path.parent.mkdir(parents=True, exist_ok=True)

            raw_text = (raw_lesson_dir / f"{topic.topic_id}.md").read_text(encoding="utf-8")
            rewritten = rewrite_markdown(
                text=raw_text,
                topic=topic,
                target_root=target_root,
                target_course_dir=course_dir,
                current_course_code=course.code,
                placements=placements,
                unresolved_links=unresolved_links,
            )
            rewritten = ensure_lesson_nav_footer(rewritten, course, target_root, course_dir)
            target_lesson_path.write_text(rewritten, encoding="utf-8")
            copied_files.append(target_lesson_path.as_posix())
            copy_lesson_source(
                raw_lesson_dir=raw_lesson_dir,
                topic=topic,
                target_source_dir=target_source_dir,
                copied_files=copied_files,
            )
    elif refresh_lesson_nav:
        for topic in topics:
            target_lesson_path = course_dir / topic_lesson_relpath(topic)
            if not target_lesson_path.exists():
                raise FileNotFoundError(f"Missing lesson file for nav refresh: {target_lesson_path}")
            original = target_lesson_path.read_text(encoding="utf-8")
            updated = ensure_lesson_nav_footer(original, course, target_root, course_dir)
            if updated != original:
                target_lesson_path.write_text(updated, encoding="utf-8")
                copied_files.append(target_lesson_path.as_posix())

    toc_path = course_dir / "0. Table of Contents" / "TOC.md"
    if not indexes_only:
        toc_path = write_toc(course, course_dir, units)
    topics_path = write_course_topics(course_dir=course_dir, topics=topics, topic_layers=topic_layers)
    home_path = write_home(
        course,
        course_dir,
        units,
        topics,
        topic_layers=topic_layers,
        prerequisites=prerequisites,
        prerequisite_scope=queue_prerequisite_scope,
    )
    prerequisites_path = write_course_prerequisites(course_dir=course_dir, rows=prerequisite_rows)

    manifest_path = course_dir / "manifest.json"
    existing_manifest: dict[str, object] = {}
    if indexes_only and manifest_path.exists():
        existing_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest = {
        **existing_manifest,
        **plan,
        "toc": toc_path.as_posix(),
        "home": home_path.as_posix(),
        "topics_csv": topics_path.as_posix(),
        "prerequisites": prerequisites_path.as_posix(),
        "file_count": existing_manifest.get("file_count", len(copied_files) + 5)
        if indexes_only
        else len(copied_files) + 5,
        "lesson_nav_footer_count": existing_manifest.get("lesson_nav_footer_count", len(copied_files))
        if indexes_only and not refresh_lesson_nav
        else len(topics),
        "unresolved_link_count": existing_manifest.get("unresolved_link_count", len(unresolved_links))
        if indexes_only
        else len(unresolved_links),
        "unresolved_links": existing_manifest.get("unresolved_links", unresolved_links)
        if indexes_only
        else unresolved_links,
        "topics": [
            {
                **asdict(topic),
                "layer": topic_layers[topic.topic_id],
                "course_map_index": index,
            }
            for index, topic in enumerate(topics, start=1)
        ],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def list_courses(courses: dict[str, CourseInfo]) -> None:
    for code in sorted(courses):
        course = courses[code]
        print(f"{course.code:>4}  {course.name}")


def normalize_course_codes(raw_codes: list[str]) -> list[str]:
    seen: set[str] = set()
    codes: list[str] = []
    for raw_code in raw_codes:
        for part in raw_code.split(","):
            code = part.strip().upper()
            if not code or code in seen:
                continue
            seen.add(code)
            codes.append(code)
    return codes


def main() -> int:
    args = parse_args()
    try:
        courses = load_courses(args.ma_data_root)
        if args.list_courses:
            list_courses(courses)
            return 0
        course_codes = normalize_course_codes(args.course_codes)
        if not course_codes:
            raise ValueError("course_code is required unless --list-courses is used")
        unknown_codes = [code for code in course_codes if code not in courses]
        if unknown_codes:
            raise KeyError(f"Unknown course code(s): {', '.join(unknown_codes)}. Use --list-courses.")

        results = [
            import_course(
                course=courses[course_code],
                ma_data_root=args.ma_data_root,
                target_root=args.target_root,
                overwrite=args.overwrite,
                indexes_only=args.indexes_only,
                refresh_lesson_nav=args.refresh_lesson_nav,
                queue_prerequisite_scope=args.queue_prerequisite_scope,
                dry_run=args.dry_run,
            )
            for course_code in course_codes
        ]
        if args.dry_run:
            print(json.dumps(results[0] if len(results) == 1 else results, indent=2))
            return 0

        for result in results:
            verb = "refreshed indexes for" if args.indexes_only else "imported"
            print(f"{verb} {result['topic_count']} lessons into {result['target_dir']}")
            print(f"manifest: {result['target_dir']}/manifest.json")
            if result["unresolved_link_count"]:
                print(f"warning: {result['unresolved_link_count']} lesson links could not be rewritten")
        return 0
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
