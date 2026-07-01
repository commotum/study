#!/usr/bin/env python3
"""Create a study bundle from Math Academy lessons stored on eve.

The importer uses a manifest-oriented workflow:

1. Pull the selected numeric lesson folders from eve with one filtered rsync.
2. Transform the raw canonical layout into the local study-bundle layout.
3. Write and verify a manifest of every copied study file.

Example:
    ./import_ma_lessons.py UQ-1 463 758 4004 1382 759

This creates:
    253/UQ-1/
        UQ-1.md
        manifest.json
        Prerequisites/<Topic Title - id>.md
        Source/<Topic Title - id>/<id>.html
        Source/<Topic Title - id>/<id>.json
        Source/<Topic Title - id>/Images/...  # only when present

It intentionally excludes PDFs and Source/Sections screenshots.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path


DEFAULT_SSH_ALIAS = "eve"
DEFAULT_REMOTE_LESSONS_ROOT = "Developer/MA/DATA/Lessons"
DEFAULT_COURSE_DIR = "253"


@dataclass(frozen=True)
class Lesson:
    lesson_id: str
    title: str
    folder_name: str


@dataclass(frozen=True)
class ManifestEntry:
    lesson_id: str
    role: str
    raw_relative_path: str
    target_relative_path: str
    size_bytes: int
    sha256: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy selected Math Academy lessons from eve into a study bundle "
            "under this repo's course folder."
        )
    )
    parser.add_argument(
        "target_name",
        help="Name of the folder to create under the course directory, e.g. UQ-1.",
    )
    parser.add_argument(
        "lesson_ids",
        nargs="+",
        help="Math Academy lesson/topic IDs to copy, e.g. 1813 1903 759.",
    )
    parser.add_argument(
        "--course-dir",
        default=DEFAULT_COURSE_DIR,
        help=f"Course directory under this repo. Default: {DEFAULT_COURSE_DIR}.",
    )
    parser.add_argument(
        "--ssh-alias",
        default=DEFAULT_SSH_ALIAS,
        help=f"SSH alias for the machine containing MA/DATA/Lessons. Default: {DEFAULT_SSH_ALIAS}.",
    )
    parser.add_argument(
        "--remote-lessons-root",
        default=DEFAULT_REMOTE_LESSONS_ROOT,
        help=(
            "Remote path, relative to the SSH login directory, containing numeric lesson "
            f"folders. Default: {DEFAULT_REMOTE_LESSONS_ROOT}."
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace generated files in an existing target folder.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the rsync plan without writing the target folder.",
    )
    parser.add_argument(
        "--keep-raw",
        action="store_true",
        help="Keep the temporary raw rsync copy under the target folder for debugging.",
    )
    return parser.parse_args()


def run_command(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=False, text=True)


def require_success(result: subprocess.CompletedProcess[str], action: str) -> None:
    if result.returncode == 0:
        return
    raise RuntimeError(f"{action} failed with exit code {result.returncode}")


def safe_path_segment(value: str, *, field_name: str) -> str:
    if not value or value in {".", ".."}:
        raise ValueError(f"{field_name} must not be empty, '.' or '..'.")
    if "/" in value or "\\" in value:
        raise ValueError(f"{field_name} must be a folder name, not a path.")
    return value


def safe_filename(value: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" .-")
    return cleaned or "Untitled Lesson"


def normalize_lesson_ids(raw_ids: list[str]) -> list[str]:
    seen: set[str] = set()
    lesson_ids: list[str] = []
    for raw_id in raw_ids:
        lesson_id = raw_id.strip()
        if not lesson_id.isdigit():
            raise ValueError(f"Lesson IDs must be numeric: {raw_id!r}")
        if lesson_id not in seen:
            seen.add(lesson_id)
            lesson_ids.append(lesson_id)
    return lesson_ids


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def write_rsync_filter(path: Path, lesson_ids: list[str]) -> None:
    lines: list[str] = []
    for lesson_id in lesson_ids:
        lines.extend(
            [
                f"+ /{lesson_id}/",
                f"+ /{lesson_id}/{lesson_id}.md",
                f"+ /{lesson_id}/Source/",
                f"+ /{lesson_id}/Source/{lesson_id}.html",
                f"+ /{lesson_id}/Source/{lesson_id}.json",
                f"+ /{lesson_id}/Source/Images/",
                f"+ /{lesson_id}/Source/Images/***",
            ]
        )
    lines.append("- *")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_filtered_rsync(
    *,
    ssh_alias: str,
    remote_lessons_root: str,
    raw_dir: Path,
    lesson_ids: list[str],
    dry_run: bool,
) -> None:
    if shutil.which("rsync") is None:
        raise RuntimeError("rsync is required for bulk import but was not found on this Mac.")

    raw_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as filter_file:
        filter_path = Path(filter_file.name)
    try:
        write_rsync_filter(filter_path, lesson_ids)
        remote_source = f"{ssh_alias}:{remote_lessons_root.rstrip('/')}/"
        cmd = [
            "rsync",
            "-a",
            "--prune-empty-dirs",
            f"--include-from={filter_path}",
            remote_source,
            str(raw_dir) + "/",
        ]
        if dry_run:
            cmd.insert(2, "--dry-run")
            cmd.insert(3, "--itemize-changes")
            print("dry-run rsync command:")
            print(" ".join(cmd))
        result = run_command(cmd)
        require_success(result, "Bulk rsync import")
    finally:
        filter_path.unlink(missing_ok=True)


def lesson_title_from_raw(raw_lesson_dir: Path, lesson_id: str) -> str:
    metadata_path = raw_lesson_dir / "Source" / f"{lesson_id}.json"
    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        title = metadata.get("topic_title")
        if title:
            return str(title)

    md_path = raw_lesson_dir / f"{lesson_id}.md"
    if md_path.exists():
        for line in md_path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped:
                return stripped.lstrip("# ").strip()

    return f"Lesson {lesson_id}"


def load_lessons(raw_dir: Path, lesson_ids: list[str]) -> list[Lesson]:
    lessons: list[Lesson] = []
    missing: list[str] = []
    for lesson_id in lesson_ids:
        raw_lesson_dir = raw_dir / lesson_id
        required = [
            raw_lesson_dir / f"{lesson_id}.md",
            raw_lesson_dir / "Source" / f"{lesson_id}.html",
            raw_lesson_dir / "Source" / f"{lesson_id}.json",
        ]
        missing.extend(str(path) for path in required if not path.exists())
        title = lesson_title_from_raw(raw_lesson_dir, lesson_id)
        lessons.append(
            Lesson(
                lesson_id=lesson_id,
                title=title,
                folder_name=safe_filename(f"{title} - {lesson_id}"),
            )
        )

    if missing:
        raise FileNotFoundError(
            "Missing required lesson files after rsync:\n" + "\n".join(f"- {path}" for path in missing)
        )
    return lessons


def add_manifest_entry(
    entries: list[ManifestEntry],
    *,
    lesson_id: str,
    role: str,
    raw_file: Path,
    raw_dir: Path,
    target_file: Path,
    target_dir: Path,
) -> None:
    stat = raw_file.stat()
    entries.append(
        ManifestEntry(
            lesson_id=lesson_id,
            role=role,
            raw_relative_path=relative_posix(raw_file, raw_dir),
            target_relative_path=relative_posix(target_file, target_dir),
            size_bytes=stat.st_size,
            sha256=sha256_file(raw_file),
        )
    )


def build_manifest_entries(raw_dir: Path, target_dir: Path, lessons: list[Lesson]) -> list[ManifestEntry]:
    entries: list[ManifestEntry] = []
    for lesson in lessons:
        lesson_id = lesson.lesson_id
        raw_lesson_dir = raw_dir / lesson_id
        target_source_dir = target_dir / "Source" / lesson.folder_name

        add_manifest_entry(
            entries,
            lesson_id=lesson_id,
            role="markdown",
            raw_file=raw_lesson_dir / f"{lesson_id}.md",
            raw_dir=raw_dir,
            target_file=target_dir / "Prerequisites" / f"{lesson.folder_name}.md",
            target_dir=target_dir,
        )
        add_manifest_entry(
            entries,
            lesson_id=lesson_id,
            role="html",
            raw_file=raw_lesson_dir / "Source" / f"{lesson_id}.html",
            raw_dir=raw_dir,
            target_file=target_source_dir / f"{lesson_id}.html",
            target_dir=target_dir,
        )
        add_manifest_entry(
            entries,
            lesson_id=lesson_id,
            role="json",
            raw_file=raw_lesson_dir / "Source" / f"{lesson_id}.json",
            raw_dir=raw_dir,
            target_file=target_source_dir / f"{lesson_id}.json",
            target_dir=target_dir,
        )

        images_dir = raw_lesson_dir / "Source" / "Images"
        if images_dir.exists():
            for raw_image in sorted(path for path in images_dir.rglob("*") if path.is_file()):
                add_manifest_entry(
                    entries,
                    lesson_id=lesson_id,
                    role="image",
                    raw_file=raw_image,
                    raw_dir=raw_dir,
                    target_file=target_source_dir / "Images" / raw_image.relative_to(images_dir),
                    target_dir=target_dir,
                )
    return entries


def copy_manifest_entries(raw_dir: Path, target_dir: Path, entries: list[ManifestEntry]) -> None:
    for entry in entries:
        source = raw_dir / entry.raw_relative_path
        target = target_dir / entry.target_relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def write_index(target_dir: Path, target_name: str, lessons: list[Lesson]) -> None:
    index_path = target_dir / f"{target_name}.md"
    lines = [
        f"# {target_name}",
        "",
        "## Prerequisites",
        "",
    ]
    for lesson in lessons:
        lines.append(f"- [{lesson.title}](<Prerequisites/{lesson.folder_name}.md>)")
    lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")


def write_manifest(
    target_dir: Path,
    *,
    target_name: str,
    course_dir: str,
    ssh_alias: str,
    remote_lessons_root: str,
    lessons: list[Lesson],
    entries: list[ManifestEntry],
) -> Path:
    manifest_path = target_dir / "manifest.json"
    manifest = {
        "schema_version": 1,
        "target_name": target_name,
        "course_dir": course_dir,
        "ssh_alias": ssh_alias,
        "remote_lessons_root": remote_lessons_root,
        "lesson_count": len(lessons),
        "file_count": len(entries),
        "lessons": [asdict(lesson) for lesson in lessons],
        "files": [asdict(entry) for entry in entries],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest_path


def verify_manifest(target_dir: Path, entries: list[ManifestEntry]) -> None:
    failures: list[str] = []
    for entry in entries:
        target = target_dir / entry.target_relative_path
        if not target.exists():
            failures.append(f"missing: {entry.target_relative_path}")
            continue
        if target.stat().st_size != entry.size_bytes:
            failures.append(f"size mismatch: {entry.target_relative_path}")
            continue
        if sha256_file(target) != entry.sha256:
            failures.append(f"sha256 mismatch: {entry.target_relative_path}")

    if failures:
        raise RuntimeError("Manifest verification failed:\n" + "\n".join(f"- {failure}" for failure in failures))


def prepare_target_dir(target_dir: Path, target_name: str, *, overwrite: bool) -> None:
    if target_dir.exists() and any(target_dir.iterdir()) and not overwrite:
        raise FileExistsError(
            f"Target folder already exists and is not empty: {target_dir}\n"
            "Use --overwrite to replace generated files in that folder."
        )

    if overwrite and target_dir.exists():
        for child in [
            target_dir / "Prerequisites",
            target_dir / "Source",
            target_dir / ".ma-import-raw",
            target_dir / "manifest.json",
            target_dir / f"{target_name}.md",
        ]:
            if child.is_dir():
                shutil.rmtree(child)
            elif child.exists():
                child.unlink()

    target_dir.mkdir(parents=True, exist_ok=True)


def main() -> int:
    args = parse_args()
    try:
        target_name = safe_path_segment(args.target_name, field_name="target_name")
        course_dir_name = safe_path_segment(args.course_dir, field_name="course_dir")
        lesson_ids = normalize_lesson_ids(args.lesson_ids)

        repo_root = Path(__file__).resolve().parent
        target_dir = repo_root / course_dir_name / target_name
        raw_dir = target_dir / ".ma-import-raw"

        print(f"target: {target_dir}")
        print(f"lessons: {', '.join(lesson_ids)}")

        if args.dry_run:
            with tempfile.TemporaryDirectory(prefix="ma-import-dry-run-") as tmp:
                run_filtered_rsync(
                    ssh_alias=args.ssh_alias,
                    remote_lessons_root=args.remote_lessons_root,
                    raw_dir=Path(tmp),
                    lesson_ids=lesson_ids,
                    dry_run=True,
                )
            return 0

        prepare_target_dir(target_dir, target_name, overwrite=args.overwrite)
        if raw_dir.exists():
            shutil.rmtree(raw_dir)

        run_filtered_rsync(
            ssh_alias=args.ssh_alias,
            remote_lessons_root=args.remote_lessons_root,
            raw_dir=raw_dir,
            lesson_ids=lesson_ids,
            dry_run=False,
        )

        lessons = load_lessons(raw_dir, lesson_ids)
        entries = build_manifest_entries(raw_dir, target_dir, lessons)
        copy_manifest_entries(raw_dir, target_dir, entries)
        write_index(target_dir, target_name, lessons)
        manifest_path = write_manifest(
            target_dir,
            target_name=target_name,
            course_dir=course_dir_name,
            ssh_alias=args.ssh_alias,
            remote_lessons_root=args.remote_lessons_root,
            lessons=lessons,
            entries=entries,
        )
        verify_manifest(target_dir, entries)

        if not args.keep_raw:
            shutil.rmtree(raw_dir)

        print(f"imported {len(lessons)} lessons and verified {len(entries)} files")
        print(f"manifest: {manifest_path}")
        return 0
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
