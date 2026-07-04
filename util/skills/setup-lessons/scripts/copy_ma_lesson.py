#!/usr/bin/env python3
"""Copy Math Academy lessons, direct prerequisites, and source folders locally."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sys
from pathlib import Path


KIND_DIRS = {
    "lesson": "Lessons",
    "lessons": "Lessons",
    "prerequisite": "Prerequisites",
    "prerequisites": "Prerequisites",
}

SECTION_TO_ROLE = {
    "Lessons": "lesson",
    "Prerequisites": "prerequisite",
}

ROLE_PRIORITY = {
    "prerequisite": 0,
    "lesson": 1,
}

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
LESSON_ID_RE = re.compile(r"lesson-id:\s*([^\s]+)")
COURSE_TOPIC_FIELDNAMES = [
    "role",
    "layer",
    "course",
    "topic-id",
    "topic-number",
    "topic-name",
    "md-path",
    "src-path",
    "local-md-path",
    "local-src-path",
    "assignment",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy indexed Math Academy lesson markdown and source folders."
    )
    parser.add_argument(
        "assignment_md",
        type=Path,
        help="Assignment markdown file whose sibling folders receive the copies.",
    )
    parser.add_argument(
        "--lesson-md",
        action="append",
        type=Path,
        default=[],
        help="Math Academy lesson markdown path. Repeat for multiple lessons.",
    )
    parser.add_argument(
        "--kind",
        choices=sorted(KIND_DIRS),
        default=None,
        help="Copy the explicit lesson markdown into Lessons or Prerequisites.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Study repo root. Defaults to the nearest parent with util/Mathematical-Foundations/topics.csv.",
    )
    parser.add_argument(
        "--index",
        type=Path,
        default=None,
        help="Path to topics.csv. Defaults to util/Mathematical-Foundations/topics.csv under repo root.",
    )
    parser.add_argument(
        "--prerequisites-index",
        type=Path,
        default=None,
        help="Path to prerequisites.csv. Defaults to util/Mathematical-Foundations/prerequisites.csv under repo root.",
    )
    parser.add_argument(
        "--no-direct-prerequisites",
        action="store_true",
        help="Do not copy direct prerequisites from prerequisites.csv.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned actions without copying files.",
    )
    parser.add_argument(
        "--no-update-links",
        action="store_true",
        help="Do not rewrite the assignment markdown's top lesson links.",
    )
    parser.add_argument(
        "--no-update-course-index",
        action="store_true",
        help="Do not refresh the course-level topics/prerequisites/TOC/Home indices.",
    )
    parser.add_argument(
        "--refresh-only",
        action="store_true",
        help="Normalize existing local files and refresh indices without copying a new lesson.",
    )
    args = parser.parse_args()
    if not args.refresh_only:
        if not args.lesson_md:
            parser.error("--lesson-md is required unless --refresh-only is used")
        if not args.kind:
            parser.error("--kind is required unless --refresh-only is used")
    if args.refresh_only and args.kind is None:
        args.kind = "lesson"
    return args


def find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        index = candidate / "util" / "Mathematical-Foundations" / "topics.csv"
        if index.exists():
            return candidate
    raise FileNotFoundError(
        "could not find repo root containing util/Mathematical-Foundations/topics.csv"
    )


def resolve_existing(path: Path, repo_root: Path) -> Path:
    expanded = path.expanduser()
    candidates = []
    if expanded.is_absolute():
        candidates.append(expanded)
    else:
        candidates.extend([Path.cwd() / expanded, repo_root / expanded])

    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    raise FileNotFoundError(f"path not found: {path}")


def repo_relative(path: Path, repo_root: Path) -> str | None:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return None


def vault_relative(path: Path, repo_root: Path) -> str:
    rel = repo_relative(path, repo_root)
    if rel is None:
        return path.as_posix()
    return rel.removeprefix("vault/")


def parse_lesson_id(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None
    match = LESSON_ID_RE.search(text)
    return match.group(1).strip() if match else None


def safe_filename_part(value: str) -> str:
    cleaned = re.sub(r"[/:]+", " - ", value).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or "Lesson"


def local_stem(row: dict[str, str]) -> str:
    topic_name = row.get("topic-name") or Path(row.get("md-path", "")).stem
    return f"{safe_filename_part(topic_name)} - {row['topic-id']}"


def local_markdown_name(row: dict[str, str]) -> str:
    return f"{local_stem(row)}.md"


def local_source_name(row: dict[str, str]) -> str:
    return local_stem(row)


def load_topics(index_path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with index_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])
    required = {"layer", "topic-id", "topic-number", "topic-name", "md-path", "src-path"}
    if not rows or not required.issubset(fieldnames):
        raise ValueError(f"index is missing required columns {sorted(required)}: {index_path}")
    return rows, fieldnames


def load_prerequisites(prerequisites_path: Path) -> dict[str, list[str]]:
    with prerequisites_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = set(reader.fieldnames or [])
        if not {"topic", "requires"}.issubset(fieldnames):
            raise ValueError(f"prerequisites index must contain topic,requires: {prerequisites_path}")
        prereqs: dict[str, list[str]] = {}
        for row in reader:
            prereqs.setdefault(row["topic"], []).append(row["requires"])
    return prereqs


def index_by_topic_id(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        indexed[row["topic-id"]] = row
    return indexed


def index_by_unique_filename(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    counts: dict[str, int] = {}
    for row in rows:
        filename = Path(row["md-path"]).name
        counts[filename] = counts.get(filename, 0) + 1
    return {Path(row["md-path"]).name: row for row in rows if counts[Path(row["md-path"]).name] == 1}


def find_index_row(
    lesson_md: Path,
    rows: list[dict[str, str]],
    filename_index: dict[str, dict[str, str]],
    repo_root: Path,
) -> dict[str, str] | None:
    lesson_rel = repo_relative(lesson_md, repo_root)
    if lesson_rel:
        for row in rows:
            if Path(row["md-path"]).as_posix() == lesson_rel:
                return row
    return filename_index.get(lesson_md.name)


def int_or_max(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        return 10**9


def topic_number_key(value: str) -> tuple[int | str, ...]:
    pieces: list[int | str] = []
    for part in value.split("."):
        if part.isdigit():
            pieces.append(int(part))
        else:
            pieces.append(part)
    return tuple(pieces)


def sort_key(row: dict[str, str]) -> tuple[int, str, tuple[int | str, ...], str]:
    return (
        int_or_max(row.get("layer", "")),
        row.get("course", ""),
        topic_number_key(row.get("topic-number", "")),
        row.get("topic-name", ""),
    )


def copy_file_once(source: Path, destination: Path, dry_run: bool) -> str:
    if destination.exists():
        return f"skip existing file: {destination}"
    if dry_run:
        return f"would copy file: {source} -> {destination}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return f"copied file: {source} -> {destination}"


def copy_dir_once(source: Path, destination: Path, dry_run: bool) -> str:
    if destination.exists():
        return f"skip existing source folder: {destination}"
    if dry_run:
        return f"would copy source folder: {source} -> {destination}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return f"copied source folder: {source} -> {destination}"


def find_local_markdown_by_lesson_id(section_dir: Path, topic_id: str) -> Path | None:
    if not section_dir.exists():
        return None
    for candidate in sorted(section_dir.glob("*.md")):
        if parse_lesson_id(candidate) == topic_id:
            return candidate
    return None


def find_local_source_dir(source_root: Path, row: dict[str, str], local_md: Path | None = None) -> Path | None:
    canonical = source_root / local_source_name(row)
    if canonical.exists():
        return canonical

    original = source_root / Path(row.get("src-path", "")).name
    if original.exists():
        return original

    if local_md is not None:
        from_markdown_name = source_root / local_md.stem
        if from_markdown_name.exists():
            return from_markdown_name

    suffix = f" - {row['topic-id']}"
    if source_root.exists():
        for candidate in sorted(path for path in source_root.iterdir() if path.is_dir()):
            if candidate.name.endswith(suffix):
                return candidate
    return None


def rename_path_once(source: Path, destination: Path, dry_run: bool, label: str) -> str:
    if source == destination:
        return f"skip canonical {label}: {destination}"
    if destination.exists():
        return f"skip {label} rename because destination exists: {destination}"
    if dry_run:
        return f"would rename {label}: {source} -> {destination}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    source.rename(destination)
    return f"renamed {label}: {source} -> {destination}"


def rewrite_local_source_links(markdown_path: Path, old_source_name: str, new_source_name: str, dry_run: bool) -> str:
    if old_source_name == new_source_name or not markdown_path.exists():
        return f"skip source links already canonical: {markdown_path}"
    text = markdown_path.read_text(encoding="utf-8")
    new_text = text.replace(f"../Source/{old_source_name}/", f"../Source/{new_source_name}/")
    new_text = new_text.replace(f"../Source/{old_source_name}>", f"../Source/{new_source_name}>")
    if new_text == text:
        return f"skip no source links to rewrite: {markdown_path}"
    if dry_run:
        return f"would rewrite source links: {markdown_path}"
    markdown_path.write_text(new_text, encoding="utf-8")
    return f"rewrote source links: {markdown_path}"


def parse_link_target(line: str) -> str | None:
    match = re.match(r"\s*-\s+\[[^\]]+\]\(<([^>]+)>\)\s*$", line)
    if match:
        return match.group(1)
    match = re.match(r"\s*-\s+\[[^\]]+\]\(([^)]+)\)\s*$", line)
    if match:
        return match.group(1)
    return None


def is_placeholder_link(line: str) -> bool:
    return "Lesson-Name" in line or "Lesson-Path" in line


def find_section_bounds(lines: list[str], section_name: str) -> tuple[int, int, int]:
    section_line = -1
    for index, line in enumerate(lines):
        match = SECTION_RE.match(line)
        if match and match.group(1).strip() == section_name:
            section_line = index
            break

    if section_line == -1:
        raise ValueError(f"section not found: ## {section_name}")

    start = section_line + 1
    end = len(lines)
    for index in range(start, len(lines)):
        line = lines[index]
        if SECTION_RE.match(line) or line.strip() == "---":
            end = index
            break

    return section_line, start, end


def read_local_topics(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = {}
        for row in reader:
            topic_id = row.get("topic-id", "")
            if topic_id:
                rows[topic_id] = row
        return rows


def merge_topic_row(
    local_rows: dict[str, dict[str, str]],
    row: dict[str, str],
    role: str,
    topic_fieldnames: list[str],
) -> None:
    topic_id = row["topic-id"]
    existing = local_rows.get(topic_id)
    if existing:
        existing_role = existing.get("role", "prerequisite")
        if ROLE_PRIORITY[role] > ROLE_PRIORITY.get(existing_role, 0):
            existing["role"] = role
        for fieldname in topic_fieldnames:
            existing[fieldname] = row.get(fieldname, "")
        return

    local_rows[topic_id] = {
        "role": role,
        **{fieldname: row.get(fieldname, "") for fieldname in topic_fieldnames},
    }


def write_local_topics(
    path: Path,
    local_rows: dict[str, dict[str, str]],
    topic_fieldnames: list[str],
    dry_run: bool,
) -> str:
    fieldnames = ["role", *topic_fieldnames]
    rows = sorted(local_rows.values(), key=lambda row: (row.get("role", ""), sort_key(row)))
    if dry_run:
        return f"would write local topics index: {path} ({len(rows)} rows)"

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({fieldname: row.get(fieldname, "") for fieldname in fieldnames})
    return f"wrote local topics index: {path} ({len(rows)} rows)"


def copy_indexed_lesson(
    row: dict[str, str],
    section_name: str,
    repo_root: Path,
    assignment_dir: Path,
    dry_run: bool,
) -> list[str]:
    lesson_md = repo_root / row["md-path"]
    source_path = repo_root / row["src-path"]
    if not lesson_md.exists():
        raise FileNotFoundError(f"lesson markdown not found: {lesson_md}")
    if not source_path.exists():
        raise FileNotFoundError(f"source folder not found: {source_path}")

    markdown_dir = assignment_dir / section_name
    source_root = assignment_dir / "Source"
    destination_md = markdown_dir / local_markdown_name(row)
    destination_source = source_root / local_source_name(row)

    messages: list[str] = []
    existing_md = find_local_markdown_by_lesson_id(markdown_dir, row["topic-id"])
    if existing_md is None:
        alternate_section = "Prerequisites" if section_name == "Lessons" else "Lessons"
        existing_md = find_local_markdown_by_lesson_id(assignment_dir / alternate_section, row["topic-id"])
    if existing_md is not None:
        old_source = find_local_source_dir(source_root, row, existing_md)
        messages.append(rename_path_once(existing_md, destination_md, dry_run, "lesson markdown"))
        if old_source is not None:
            messages.append(rename_path_once(old_source, destination_source, dry_run, "source folder"))
            messages.append(
                rewrite_local_source_links(
                    destination_md if not dry_run and destination_md.exists() else existing_md,
                    old_source.name,
                    destination_source.name,
                    dry_run,
                )
            )
        return messages

    messages.append(copy_file_once(lesson_md, destination_md, dry_run))
    messages.append(copy_dir_once(source_path, destination_source, dry_run))
    messages.append(rewrite_local_source_links(destination_md, source_path.name, destination_source.name, dry_run))
    return messages


def normalize_existing_copy(
    row: dict[str, str],
    section_name: str,
    assignment_dir: Path,
    dry_run: bool,
) -> list[str]:
    markdown_dir = assignment_dir / section_name
    source_root = assignment_dir / "Source"
    destination_md = markdown_dir / local_markdown_name(row)
    destination_source = source_root / local_source_name(row)
    messages: list[str] = []

    existing_md = find_local_markdown_by_lesson_id(markdown_dir, row["topic-id"])
    if existing_md is None:
        alternate_section = "Prerequisites" if section_name == "Lessons" else "Lessons"
        existing_md = find_local_markdown_by_lesson_id(assignment_dir / alternate_section, row["topic-id"])
    if existing_md is None:
        return [f"warning: local markdown not found for topic-id {row['topic-id']} in {markdown_dir}"]

    old_source = find_local_source_dir(source_root, row, existing_md)
    messages.append(rename_path_once(existing_md, destination_md, dry_run, "lesson markdown"))
    if old_source is None:
        messages.append(f"warning: local source folder not found for topic-id {row['topic-id']} in {source_root}")
        return messages

    messages.append(rename_path_once(old_source, destination_source, dry_run, "source folder"))
    messages.append(
        rewrite_local_source_links(
            destination_md if not dry_run and destination_md.exists() else existing_md,
            old_source.name,
            destination_source.name,
            dry_run,
        )
    )
    return messages


def normalize_assignment_local_copies(
    local_rows: dict[str, dict[str, str]],
    assignment_dir: Path,
    dry_run: bool,
) -> list[str]:
    messages: list[str] = []
    for row in sorted(local_rows.values(), key=sort_key):
        role = row.get("role", "prerequisite")
        section_name = "Lessons" if role == "lesson" else "Prerequisites"
        messages.extend(normalize_existing_copy(row, section_name, assignment_dir, dry_run))
    return messages


def managed_link_line(row: dict[str, str], section_name: str) -> str:
    filename = local_markdown_name(row)
    title = local_stem(row)
    return f"- [{title}](<{section_name}/{filename}>)"


def sync_section_links(
    lines: list[str],
    section_name: str,
    local_rows: dict[str, dict[str, str]],
) -> list[str]:
    _, start, end = find_section_bounds(lines, section_name)
    role = SECTION_TO_ROLE[section_name]
    section_rows = sorted(
        [row for row in local_rows.values() if row.get("role") == role],
        key=sort_key,
    )
    known_section_targets = set()
    for row in local_rows.values():
        known_section_targets.add(f"{section_name}/{Path(row['md-path']).name}")
        known_section_targets.add(f"{section_name}/{local_markdown_name(row)}")
    managed_targets = {
        f"{section_name}/{local_markdown_name(row)}" for row in section_rows
    }
    unknown_lines: list[str] = []
    for line in lines[start:end]:
        if not line.strip() or is_placeholder_link(line):
            continue
        target = parse_link_target(line)
        if target in known_section_targets or any(
            target.endswith(f"/{known_target}") for known_target in known_section_targets
        ):
            continue
        unknown_lines.append(line)

    replacement = ["", *[managed_link_line(row, section_name) for row in section_rows]]
    replacement.extend(unknown_lines)
    replacement.append("")
    return [*lines[:start], *replacement, *lines[end:]]


def sync_assignment_links(
    assignment_md: Path,
    local_rows: dict[str, dict[str, str]],
    dry_run: bool,
) -> str:
    text = assignment_md.read_text(encoding="utf-8")
    had_trailing_newline = text.endswith("\n")
    lines = text.splitlines()
    missing_sections: list[str] = []
    for section_name in ("Prerequisites", "Lessons"):
        try:
            lines = sync_section_links(lines, section_name, local_rows)
        except ValueError:
            missing_sections.append(section_name)

    new_text = "\n".join(lines)
    if had_trailing_newline:
        new_text += "\n"

    if new_text == text:
        if missing_sections:
            return f"skip assignment links missing sections {', '.join(missing_sections)}: {assignment_md}"
        return f"skip assignment links already sorted: {assignment_md}"
    if dry_run:
        return f"would rewrite sorted assignment links: {assignment_md}"

    assignment_md.write_text(new_text, encoding="utf-8")
    return f"rewrote sorted assignment links: {assignment_md}"


def read_csv_dicts(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def split_semicolon(value: str) -> list[str]:
    return [part for part in value.split(";") if part]


def add_semicolon_value(row: dict[str, str], fieldname: str, value: str) -> None:
    if not value:
        return
    values = split_semicolon(row.get(fieldname, ""))
    if value not in values:
        values.append(value)
    row[fieldname] = ";".join(values)


def find_course_root(assignment_md: Path, repo_root: Path) -> Path | None:
    vault_root = repo_root / "vault"
    try:
        relative = assignment_md.resolve().relative_to(vault_root.resolve())
    except ValueError:
        return None
    if len(relative.parts) < 3:
        return None
    return vault_root / relative.parts[0]


def assignment_key(assignment_dir: Path, course_root: Path) -> str:
    try:
        return assignment_dir.resolve().relative_to(course_root.resolve()).as_posix()
    except ValueError:
        return assignment_dir.name


def course_relative_path(path: Path, course_root: Path) -> str:
    try:
        return path.resolve().relative_to(course_root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def course_name(course_root: Path) -> str:
    return f"MTH {course_root.name}" if course_root.name.isdigit() else course_root.name


def merge_course_topic_row(
    course_rows: dict[str, dict[str, str]],
    source_row: dict[str, str],
    role: str,
    local_md: Path | None,
    local_source: Path | None,
    assignment_dir: Path,
    course_root: Path,
    repo_root: Path,
) -> None:
    topic_id = source_row.get("topic-id", "")
    if not topic_id:
        return

    row = course_rows.get(topic_id)
    if row is None:
        row = {
            "role": role,
            "layer": source_row.get("layer", ""),
            "course": source_row.get("course", ""),
            "topic-id": topic_id,
            "topic-number": source_row.get("topic-number", ""),
            "topic-name": source_row.get("topic-name", ""),
            "md-path": source_row.get("md-path", ""),
            "src-path": source_row.get("src-path", ""),
            "local-md-path": "",
            "local-src-path": "",
            "assignment": "",
        }
        course_rows[topic_id] = row
    elif ROLE_PRIORITY[role] > ROLE_PRIORITY.get(row.get("role", "prerequisite"), 0):
        row["role"] = role

    if local_md is not None:
        add_semicolon_value(row, "local-md-path", vault_relative(local_md, repo_root))
    if local_source is not None:
        add_semicolon_value(row, "local-src-path", vault_relative(local_source, repo_root))
    add_semicolon_value(row, "assignment", assignment_key(assignment_dir, course_root))


def collect_course_topic_rows(course_root: Path, repo_root: Path) -> dict[str, dict[str, str]]:
    course_rows: dict[str, dict[str, str]] = {}
    for topics_path in sorted(course_root.glob("**/Source/topics.csv")):
        assignment_dir = topics_path.parent.parent
        if assignment_dir == course_root:
            continue
        for row in read_csv_dicts(topics_path):
            topic_id = row.get("topic-id", "")
            role = row.get("role", "prerequisite")
            if not topic_id or role not in ROLE_PRIORITY:
                continue
            section_name = "Lessons" if role == "lesson" else "Prerequisites"
            local_md = find_local_markdown_by_lesson_id(assignment_dir / section_name, topic_id)
            local_source = find_local_source_dir(assignment_dir / "Source", row, local_md)
            merge_course_topic_row(
                course_rows=course_rows,
                source_row=row,
                role=role,
                local_md=local_md,
                local_source=local_source,
                assignment_dir=assignment_dir,
                course_root=course_root,
                repo_root=repo_root,
            )
    return course_rows


def write_course_topics(course_root: Path, course_rows: dict[str, dict[str, str]], dry_run: bool) -> str:
    path = course_root / "topics.csv"
    rows = sorted(course_rows.values(), key=lambda row: (0 if row.get("role") == "lesson" else 1, sort_key(row)))
    if dry_run:
        return f"would write course topics index: {path} ({len(rows)} rows)"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COURSE_TOPIC_FIELDNAMES)
        writer.writeheader()
        for row in rows:
            writer.writerow({fieldname: row.get(fieldname, "") for fieldname in COURSE_TOPIC_FIELDNAMES})
    return f"wrote course topics index: {path} ({len(rows)} rows)"


def write_course_prerequisites(
    course_root: Path,
    course_rows: dict[str, dict[str, str]],
    prerequisites: dict[str, list[str]],
    dry_run: bool,
) -> str:
    path = course_root / "prerequisites.csv"
    topic_ids = set(course_rows)
    lesson_topic_ids = {topic_id for topic_id, row in course_rows.items() if row.get("role") == "lesson"}
    rows = []
    for topic_id in sorted(lesson_topic_ids, key=lambda topic_id: sort_key(course_rows[topic_id])):
        for required_id in prerequisites.get(topic_id, []):
            if required_id in topic_ids:
                rows.append({"topic": topic_id, "requires": required_id})

    if dry_run:
        return f"would write course prerequisites index: {path} ({len(rows)} rows)"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["topic", "requires"])
        writer.writeheader()
        writer.writerows(rows)
    return f"wrote course prerequisites index: {path} ({len(rows)} rows)"


def parse_checked_toc_targets(toc_path: Path) -> set[str]:
    if not toc_path.exists():
        return set()
    checked: set[str] = set()
    for line in toc_path.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\s*-\s+\[[xX]\]\s+", line):
            continue
        match = re.search(r"\[\[([^\]|]+)", line)
        if match:
            checked.add(strip_md(match.group(1)))
    return checked


def strip_md(value: str) -> str:
    return value[:-3] if value.endswith(".md") else value


def course_lesson_entries(course_rows: dict[str, dict[str, str]], course_root: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    course_prefix = course_root.name + "/"
    for row in course_rows.values():
        if row.get("role") != "lesson":
            continue
        for local_md_path in split_semicolon(row.get("local-md-path", "")):
            if "/Lessons/" not in local_md_path:
                continue
            course_rel = local_md_path[len(course_prefix) :] if local_md_path.startswith(course_prefix) else local_md_path
            parts = course_rel.split("/")
            entries.append(
                {
                    "topic-id": row["topic-id"],
                    "topic-number": row.get("topic-number", ""),
                    "topic-name": row.get("topic-name", ""),
                    "layer": row.get("layer", ""),
                    "course-rel": course_rel,
                    "target": strip_md(course_rel),
                    "module": parts[0] if len(parts) > 0 else "",
                    "assignment": parts[1] if len(parts) > 1 else "",
                    "name": Path(course_rel).stem,
                }
            )
    return sorted(
        entries,
        key=lambda entry: (
            topic_number_key(entry["module"].removeprefix("M-")),
            topic_number_key(entry["assignment"].split("-", 1)[-1]),
            int_or_max(entry.get("layer", "")),
            topic_number_key(entry.get("topic-number", "")),
            entry["name"],
        ),
    )


def render_course_toc(course_root: Path, course_rows: dict[str, dict[str, str]], checked_targets: set[str]) -> str:
    entries = course_lesson_entries(course_rows, course_root)
    lines = [
        f"# {course_name(course_root)}",
        "",
        "```check-progress",
        "```",
        "",
        "## Course Content",
        "",
    ]
    current_module = None
    current_assignment = None
    module_entries: dict[str, list[dict[str, str]]] = {}
    assignment_entries: dict[tuple[str, str], list[dict[str, str]]] = {}
    for entry in entries:
        module_entries.setdefault(entry["module"], []).append(entry)
        assignment_entries.setdefault((entry["module"], entry["assignment"]), []).append(entry)

    for entry in entries:
        module = entry["module"]
        assignment = entry["assignment"]
        if module != current_module:
            module_done = all(item["target"] in checked_targets for item in module_entries[module])
            lines.append(f"- [{'x' if module_done and module_entries[module] else ' '}] {module}")
            current_module = module
            current_assignment = None
        if assignment != current_assignment:
            assignment_done = all(item["target"] in checked_targets for item in assignment_entries[(module, assignment)])
            lines.append(f"\t- [{'x' if assignment_done and assignment_entries[(module, assignment)] else ' '}] {assignment}")
            current_assignment = assignment
        display = f"{entry['topic-number']}. {entry['topic-name']}".strip(". ")
        checked = "x" if entry["target"] in checked_targets else " "
        lines.append(f"\t\t- [{checked}] [[{entry['target']}|{display}]]")

    return "\n".join(lines).rstrip() + "\n"


def markdown_path(value: str) -> str:
    return f"<{value}>" if re.search(r"[ ()\[\]']", value) else value


def read_plugin_data(repo_root: Path) -> dict:
    path = repo_root / "vault" / ".obsidian" / "plugins" / "obsidian-update-progress" / "data.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def completed_ids_for_course(course_root: Path, entries: list[dict[str, str]], checked_targets: set[str], repo_root: Path) -> set[str]:
    data = read_plugin_data(repo_root)
    completed: set[str] = set()
    course_index = data.get("completionByCourse", {}).get(course_root.name, {})
    if isinstance(course_index, dict):
        completed.update(topic_id for topic_id, timestamp in course_index.items() if isinstance(timestamp, str) and timestamp)
    for entry in entries:
        if entry["target"] in checked_targets:
            completed.add(entry["topic-id"])
    return completed


def render_course_home(
    course_root: Path,
    course_rows: dict[str, dict[str, str]],
    prerequisites: dict[str, list[str]],
    checked_targets: set[str],
    repo_root: Path,
) -> str:
    entries = course_lesson_entries(course_rows, course_root)
    completed = completed_ids_for_course(course_root, entries, checked_targets, repo_root)
    local_lesson_ids = {entry["topic-id"] for entry in entries}
    next_entries = []
    for entry in entries:
        if entry["topic-id"] in completed:
            continue
        blocked = False
        for required_id in prerequisites.get(entry["topic-id"], []):
            if required_id in local_lesson_ids and required_id not in completed:
                blocked = True
                break
        if not blocked:
            next_entries.append(entry)
    next_entries = next_entries[:5]

    lines = [f"# {course_name(course_root)} Home", "", "## Next Topics", ""]
    if next_entries:
        for index, entry in enumerate(next_entries, start=1):
            lines.append(f"{index}. [{entry['name']}]({markdown_path(entry['course-rel'])})")
    else:
        lines.append("No eligible next lessons found.")

    lines.extend(["", "## Progress", ""])
    total = len(entries)
    completed_total = sum(1 for entry in entries if entry["topic-id"] in completed)
    percent = round((completed_total / total) * 100) if total else 0
    lines.append(f"- Course: {percent}% ({completed_total}/{total})")
    lines.append("")

    modules: dict[str, list[dict[str, str]]] = {}
    for entry in entries:
        modules.setdefault(entry["module"], []).append(entry)
    for module, module_entries in modules.items():
        module_completed = sum(1 for entry in module_entries if entry["topic-id"] in completed)
        module_percent = round((module_completed / len(module_entries)) * 100) if module_entries else 0
        lines.append(f"- {module}: {module_percent}% ({module_completed}/{len(module_entries)})")

    lines.extend(["", "## History", ""])
    completed_entries = [entry for entry in entries if entry["topic-id"] in completed]
    if completed_entries:
        for entry in completed_entries:
            lines.append(f"- [{entry['name']}]({markdown_path(entry['course-rel'])})")
    else:
        lines.append("- No completed lessons yet.")

    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Completed lessons: {completed_total} / {total}",
            f"- Queue size: {len(next_entries)} / 5",
            "",
            "<!--",
            "Generated by setup-lessons.",
            "Course progress is keyed by local course completion; external prerequisites do not block the next-topic queue.",
            "The obsidian-update-progress plugin will refresh this page after progress checks.",
            "-->",
            "",
        ]
    )
    return "\n".join(lines)


def write_text_if_changed(path: Path, text: str, dry_run: bool, label: str) -> str:
    existing = path.read_text(encoding="utf-8") if path.exists() else None
    if existing == text:
        return f"skip {label} already current: {path}"
    if dry_run:
        return f"would write {label}: {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return f"wrote {label}: {path}"


def ensure_update_progress_course_config(course_root: Path, repo_root: Path, dry_run: bool) -> str:
    data_path = repo_root / "vault" / ".obsidian" / "plugins" / "obsidian-update-progress" / "data.json"
    if not data_path.exists():
        return f"skip update-progress config not found: {data_path}"
    data = read_plugin_data(repo_root)
    if not data:
        return f"skip update-progress config not parseable: {data_path}"

    folder = course_root.name
    data.setdefault("courseFolders", [])
    if folder not in data["courseFolders"]:
        data["courseFolders"].append(folder)

    course_config = {
        "name": course_name(course_root),
        "folder": folder,
        "tocPath": f"{folder}/0. Table of Contents/TOC.md",
        "homePath": f"{folder}/Home.md",
        "topicsPath": f"{folder}/topics.csv",
        "prerequisitesPath": f"{folder}/prerequisites.csv",
        "queuePrerequisiteScope": "course",
    }
    courses = data.setdefault("courses", [])
    for index, existing in enumerate(courses):
        if isinstance(existing, dict) and existing.get("folder") == folder:
            courses[index] = {**existing, **course_config}
            break
    else:
        courses.append(course_config)

    completion_by_course = data.setdefault("completionByCourse", {})
    completion_by_course.setdefault(folder, {})

    new_text = json.dumps(data, indent=2) + "\n"
    if data_path.read_text(encoding="utf-8") == new_text:
        return f"skip update-progress config already current: {data_path}"
    if dry_run:
        return f"would update update-progress config: {data_path}"
    data_path.write_text(new_text, encoding="utf-8")
    return f"updated update-progress config: {data_path}"


def refresh_course_indices(
    assignment_md: Path,
    repo_root: Path,
    prerequisites: dict[str, list[str]],
    dry_run: bool,
) -> list[str]:
    course_root = find_course_root(assignment_md, repo_root)
    if course_root is None:
        return [f"skip course index refresh outside vault course: {assignment_md}"]

    course_rows = collect_course_topic_rows(course_root, repo_root)
    toc_path = course_root / "0. Table of Contents" / "TOC.md"
    checked_targets = parse_checked_toc_targets(toc_path)
    toc_text = render_course_toc(course_root, course_rows, checked_targets)
    home_text = render_course_home(course_root, course_rows, prerequisites, checked_targets, repo_root)

    return [
        write_course_topics(course_root, course_rows, dry_run),
        write_course_prerequisites(course_root, course_rows, prerequisites, dry_run),
        write_text_if_changed(toc_path, toc_text, dry_run, "course TOC"),
        write_text_if_changed(course_root / "Home.md", home_text, dry_run, "course Home"),
        ensure_update_progress_course_config(course_root, repo_root, dry_run),
    ]


def choose_records_to_copy(
    explicit_rows: list[dict[str, str]],
    explicit_section: str,
    existing_rows: dict[str, dict[str, str]],
    prerequisites: dict[str, list[str]],
    topic_by_id: dict[str, dict[str, str]],
    include_direct_prerequisites: bool,
) -> dict[str, tuple[dict[str, str], str]]:
    selected: dict[str, tuple[dict[str, str], str]] = {}

    for topic_id, row in existing_rows.items():
        role = row.get("role", "prerequisite")
        if role == "lesson":
            selected[topic_id] = (row, "Lessons")

    for row in explicit_rows:
        topic_id = row["topic-id"]
        current = selected.get(topic_id)
        if current and current[1] == "Lessons" and explicit_section == "Prerequisites":
            continue
        selected[topic_id] = (row, explicit_section)

    if not include_direct_prerequisites:
        return selected

    explicit_core_topic_ids = {
        row["topic-id"] for row in explicit_rows if explicit_section == "Lessons"
    }
    for row in explicit_rows:
        for prereq_id in prerequisites.get(row["topic-id"], []):
            if prereq_id in explicit_core_topic_ids:
                continue
            prereq_row = topic_by_id.get(prereq_id)
            if not prereq_row:
                print(
                    f"warning: prerequisite topic-id {prereq_id} not found for topic-id {row['topic-id']}",
                    file=sys.stderr,
                )
                continue
            current = selected.get(prereq_id)
            if current and current[1] == "Lessons":
                continue
            selected[prereq_id] = (prereq_row, "Prerequisites")

    return selected


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.expanduser().resolve() if args.repo_root else find_repo_root(Path.cwd())
    index_path = (
        args.index.expanduser().resolve()
        if args.index
        else repo_root / "util" / "Mathematical-Foundations" / "topics.csv"
    )
    prerequisites_path = (
        args.prerequisites_index.expanduser().resolve()
        if args.prerequisites_index
        else repo_root / "util" / "Mathematical-Foundations" / "prerequisites.csv"
    )
    if not index_path.exists():
        print(f"error: index not found: {index_path}", file=sys.stderr)
        return 2
    if not prerequisites_path.exists():
        print(f"error: prerequisites index not found: {prerequisites_path}", file=sys.stderr)
        return 2

    assignment_md = resolve_existing(args.assignment_md, repo_root)
    assignment_dir = assignment_md.parent
    source_root = assignment_dir / "Source"
    local_topics_path = source_root / "topics.csv"

    topic_rows, topic_fieldnames = load_topics(index_path)
    topic_by_id = index_by_topic_id(topic_rows)
    filename_index = index_by_unique_filename(topic_rows)
    prerequisites = load_prerequisites(prerequisites_path)
    local_rows = read_local_topics(local_topics_path)

    if not args.refresh_only:
        explicit_rows: list[dict[str, str]] = []
        for raw_lesson_md in args.lesson_md:
            lesson_md = resolve_existing(raw_lesson_md, repo_root)
            row = find_index_row(lesson_md, topic_rows, filename_index, repo_root)
            if not row:
                print(f"error: lesson not found in topics index: {lesson_md}", file=sys.stderr)
                return 1
            explicit_rows.append(row)

        selected = choose_records_to_copy(
            explicit_rows=explicit_rows,
            explicit_section=KIND_DIRS[args.kind],
            existing_rows=local_rows,
            prerequisites=prerequisites,
            topic_by_id=topic_by_id,
            include_direct_prerequisites=not args.no_direct_prerequisites,
        )

        for row, section_name in sorted(selected.values(), key=lambda item: sort_key(item[0])):
            role = SECTION_TO_ROLE[section_name]
            for message in copy_indexed_lesson(row, section_name, repo_root, assignment_dir, args.dry_run):
                print(message)
            merge_topic_row(local_rows, row, role, topic_fieldnames)

    for message in normalize_assignment_local_copies(local_rows, assignment_dir, args.dry_run):
        print(message)

    print(write_local_topics(local_topics_path, local_rows, topic_fieldnames, args.dry_run))

    if not args.no_update_links:
        print(sync_assignment_links(assignment_md, local_rows, args.dry_run))

    if not args.no_update_course_index:
        for message in refresh_course_indices(assignment_md, repo_root, prerequisites, args.dry_run):
            print(message)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
