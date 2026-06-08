#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


COURSE_ROOT = Path(__file__).resolve().parent
VAULT_ROOT = COURSE_ROOT.parent
TOC_PATH = COURSE_ROOT / "0. Table of Contents" / "TOC.md"
HOME_PATH = COURSE_ROOT / "Home.md"
PLUGIN_DATA_PATH = VAULT_ROOT / ".obsidian" / "plugins" / "obsidian-update-progress" / "data.json"
LAYERS_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/"
    "3-Wire-Graph/1-Prerequisite-Identification/5-Publish-Graph/1-Outputs/"
    "Continuous-Time-Signal-Processing/Layers.csv"
)
PREREQUISITES_PATH = Path(
    "/home/jake/Developer/MA/COURSES/Electrical-and-Computer-Engineering/"
    "Continuous-Time-Signal-Processing/GRAPH-Continuous-Time-Signal-Processing/"
    "Prerequisites.csv"
)

QUEUE_SIZE = 5

LESSON_ID_RE = re.compile(r"lesson-id:\s*(EE01-M\d{2}-\d{2}-L\d{2})")
TOC_LESSON_RE = re.compile(r"^\s*-\s+\[([ xX])\]\s+\[\[([^|\]]+)(?:\|[^\]]+)?\]\]")
TOPIC_NUMBER_PREFIX_RE = re.compile(r"^\d+(?:\.\d+)*\.\s*")
TOPIC_ID_RE = re.compile(r"^EE01-T(\d{2})-(\d{2})-(\d{2})$")


@dataclass(frozen=True)
class Lesson:
    lesson_id: str
    topic_id: str
    topic_number: str
    path: Path
    name: str
    layer: int
    course_index: int
    coordinate: int


def topic_id_to_lesson_id(topic_id: str) -> str:
    match = TOPIC_ID_RE.match(topic_id)
    if not match:
        raise ValueError(f"Unexpected topic id: {topic_id}")
    unit, module, lesson = match.groups()
    return f"EE01-M{unit}-{module}-L{lesson}"


def lesson_id_to_topic_id(lesson_id: str) -> str:
    match = re.match(r"^EE01-M(\d{2})-(\d{2})-L(\d{2})$", lesson_id)
    if not match:
        raise ValueError(f"Unexpected lesson id: {lesson_id}")
    unit, module, lesson = match.groups()
    return f"EE01-T{unit}-{module}-{lesson}"


def read_lesson_id(path: Path) -> str | None:
    match = LESSON_ID_RE.search(path.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def normalized_name(path: Path) -> str:
    return TOPIC_NUMBER_PREFIX_RE.sub("", path.stem).strip()


def topic_coordinate(topic_number: str) -> int:
    parts = [int(part) for part in topic_number.split(".")]
    while len(parts) < 3:
        parts.append(0)
    unit, module, lesson = parts[:3]
    return unit * 10_000 + module * 100 + lesson


def markdown_link_target(path: Path) -> str:
    rel = path.relative_to(COURSE_ROOT).as_posix()
    return f"<{rel}>" if any(char in rel for char in " ()[]") else rel


def vault_relative_path(path: Path) -> str:
    return path.relative_to(VAULT_ROOT).as_posix()


def unit_name(path: Path) -> str:
    return path.relative_to(COURSE_ROOT).parts[0]


def load_local_lesson_paths() -> dict[str, Path]:
    lessons: dict[str, Path] = {}
    for path in COURSE_ROOT.rglob("*.md"):
        if "Lessons" not in path.parts:
            continue
        lesson_id = read_lesson_id(path)
        if lesson_id:
            lessons[lesson_id] = path
    return lessons


def load_layers() -> dict[str, dict[str, str]]:
    with LAYERS_PATH.open(newline="", encoding="utf-8") as handle:
        return {row["topic-id"]: row for row in csv.DictReader(handle)}


def load_prerequisites() -> dict[str, set[str]]:
    prerequisites: dict[str, set[str]] = {}
    with PREREQUISITES_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            topic_id = row["topic"]
            required_topic_id = row["requires"]
            prerequisites.setdefault(topic_id_to_lesson_id(topic_id), set()).add(
                topic_id_to_lesson_id(required_topic_id)
            )
    return prerequisites


def load_completed_lessons(local_lessons: dict[str, Path]) -> set[str]:
    path_to_lesson_id = {
        path.relative_to(COURSE_ROOT).with_suffix("").as_posix(): lesson_id
        for lesson_id, path in local_lessons.items()
    }
    completed: set[str] = set()
    for line in TOC_PATH.read_text(encoding="utf-8").splitlines():
        match = TOC_LESSON_RE.match(line)
        if not match:
            continue
        checked, target = match.groups()
        if checked.lower() != "x":
            continue
        lesson_id = path_to_lesson_id.get(target)
        if lesson_id:
            completed.add(lesson_id)
    return completed


def build_lessons() -> dict[str, Lesson]:
    local_paths = load_local_lesson_paths()
    layers = load_layers()
    lessons: dict[str, Lesson] = {}
    for lesson_id, path in local_paths.items():
        topic_id = lesson_id_to_topic_id(lesson_id)
        row = layers.get(topic_id)
        if not row:
            continue
        lessons[lesson_id] = Lesson(
            lesson_id=lesson_id,
            topic_id=topic_id,
            topic_number=row["topic-number"],
            path=path,
            name=normalized_name(path),
            layer=int(row["nearest-integer-layer"]),
            course_index=int(row["course-map-index"]),
            coordinate=topic_coordinate(row["topic-number"]),
        )
    return lessons


def select_broadest(candidates: list[Lesson], count: int, anchors: list[Lesson]) -> list[Lesson]:
    if count <= 0:
        return []
    ordered = sorted(candidates, key=lambda lesson: (lesson.coordinate, lesson.course_index))
    if len(ordered) <= count:
        return ordered

    selected: list[Lesson] = []
    if not anchors:
        selected.extend([ordered[0], ordered[-1]])
    while len(selected) > count:
        selected.pop()

    while len(selected) < count:
        already = {lesson.lesson_id for lesson in selected}
        reference = anchors + selected
        remaining = [lesson for lesson in ordered if lesson.lesson_id not in already]
        if not reference:
            selected.append(remaining[0])
            continue

        def score(lesson: Lesson) -> tuple[int, int, int]:
            nearest_gap = min(abs(lesson.coordinate - other.coordinate) for other in reference)
            edge_gap = max(abs(lesson.coordinate - other.coordinate) for other in reference)
            return (nearest_gap, edge_gap, -lesson.course_index)

        selected.append(max(remaining, key=score))

    return sorted(selected, key=lambda lesson: (lesson.coordinate, lesson.course_index))


def select_next_lessons(
    lessons: dict[str, Lesson],
    prerequisites: dict[str, set[str]],
    completed: set[str],
) -> list[Lesson]:
    eligible = [
        lesson
        for lesson_id, lesson in lessons.items()
        if lesson_id not in completed
        and prerequisites.get(lesson_id, set()).issubset(completed)
    ]

    by_layer: dict[int, list[Lesson]] = {}
    for lesson in eligible:
        by_layer.setdefault(lesson.layer, []).append(lesson)

    selected: list[Lesson] = []
    for layer in sorted(by_layer):
        slots = QUEUE_SIZE - len(selected)
        if slots <= 0:
            break
        selected.extend(select_broadest(by_layer[layer], slots, selected))

    return selected[:QUEUE_SIZE]


def load_plugin_data() -> dict[str, object]:
    if not PLUGIN_DATA_PATH.exists():
        return {}
    try:
        data = json.loads(PLUGIN_DATA_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def save_plugin_data(data: dict[str, object]) -> None:
    PLUGIN_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    PLUGIN_DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_completion_history() -> dict[str, str]:
    history = load_plugin_data().get("completionHistory", {})
    if not isinstance(history, dict):
        return {}
    return {str(key): str(value) for key, value in history.items() if isinstance(value, str)}


def update_completion_history(
    lessons: dict[str, Lesson],
    completed: set[str],
) -> dict[str, str]:
    data = load_plugin_data()
    raw_history = data.get("completionHistory", {})
    history = raw_history if isinstance(raw_history, dict) else {}
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    changed = False

    for lesson_id in completed:
        lesson = lessons.get(lesson_id)
        if not lesson:
            continue
        key = vault_relative_path(lesson.path)
        if key not in history or not isinstance(history[key], str):
            history[key] = now
            changed = True

    if changed:
        data["completionHistory"] = history
        save_plugin_data(data)

    return {str(key): str(value) for key, value in history.items() if isinstance(value, str)}


def format_completion_time(value: str | None) -> str:
    if not value:
        return "Unknown"
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return value
    return parsed.astimezone().strftime("%Y-%m-%d %H:%M")


def render_home(
    selected: list[Lesson],
    lessons: dict[str, Lesson],
    completed: set[str],
    completion_history: dict[str, str],
) -> str:
    lines = [
        "# Continuous-Time Signal Processing Home",
        "",
        "## Next Topics",
        "",
    ]

    if selected:
        for index, lesson in enumerate(selected, start=1):
            lines.append(f"{index}. [{lesson.name}]({markdown_link_target(lesson.path)})")
    else:
        lines.append("No eligible next lessons found.")

    lines.extend(["", "## Progress", ""])
    units: dict[str, dict[str, int | str]] = {}
    for lesson in lessons.values():
        name = unit_name(lesson.path)
        unit = units.setdefault(
            name,
            {
                "name": name,
                "order": int(lesson.topic_number.split(".")[0]),
                "completed": 0,
                "total": 0,
            },
        )
        unit["total"] = int(unit["total"]) + 1
        if lesson.lesson_id in completed:
            unit["completed"] = int(unit["completed"]) + 1

    course_percent = round((len(completed) / len(lessons)) * 100) if lessons else 0
    lines.append(f"- Course: {course_percent}% ({len(completed)}/{len(lessons)})")
    lines.append("")

    for unit in sorted(units.values(), key=lambda item: int(item["order"])):
        complete_count = int(unit["completed"])
        total_count = int(unit["total"])
        percent = round((complete_count / total_count) * 100) if total_count else 0
        lines.append(f"- {unit['name']}: {percent}% ({complete_count}/{total_count})")

    lines.extend(["", "## History", ""])
    completed_lessons = [lessons[lesson_id] for lesson_id in completed if lesson_id in lessons]
    completed_lessons.sort(
        key=lambda lesson: (
            completion_history.get(vault_relative_path(lesson.path), ""),
            -lesson.course_index,
        ),
        reverse=True,
    )

    if completed_lessons:
        for lesson in completed_lessons:
            key = vault_relative_path(lesson.path)
            lines.append(
                f"- [{lesson.name}]({markdown_link_target(lesson.path)})"
                f" - {format_completion_time(completion_history.get(key))}"
            )
    else:
        lines.append("No completed lessons yet.")

    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Completed lessons: {len(completed)} / {len(lessons)}",
            f"- Queue size: {len(selected)} / {QUEUE_SIZE}",
            "",
            "<!--",
            "Generated by update_home.py.",
            "Selection uses checked lesson rows in 0. Table of Contents/TOC.md,",
            "Prerequisites.csv, and Layers.csv nearest-integer-layer values.",
            "Completion history is recorded by obsidian-update-progress.",
            "-->",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    lessons = build_lessons()
    prerequisites = load_prerequisites()
    completed = load_completed_lessons(load_local_lesson_paths())
    completion_history = update_completion_history(lessons, completed)
    selected = select_next_lessons(lessons, prerequisites, completed)
    HOME_PATH.write_text(render_home(selected, lessons, completed, completion_history), encoding="utf-8")
    print(f"Wrote {HOME_PATH}")
    print(f"Selected {len(selected)} next lessons from {len(completed)} completed lessons.")
    for lesson in selected:
        print(f"- layer {lesson.layer}: {lesson.topic_number} {lesson.name}")


if __name__ == "__main__":
    main()
