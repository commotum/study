#!/usr/bin/env python3
"""Match Physics 212 lecture notes to videos with isolated Codex CLI runs."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tqdm import tqdm


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_STUDY_ROOT = SCRIPT_DIR.parent
DEFAULT_COURSE_ROOT = DEFAULT_STUDY_ROOT / "vault" / "212"
DEFAULT_PLAYLIST_CSV = Path("/Users/jake/Developer/ytdl/playlist-titles.csv")
DEFAULT_OUTPUT_DIR = DEFAULT_COURSE_ROOT / "Video-Matches"
DEFAULT_SKIP = DEFAULT_COURSE_ROOT / "M1" / "2026-06-22-M1-0"
RUNTIME_DIR = SCRIPT_DIR / ".physics_212_video_match_runner"
SCHEMA_PATH = RUNTIME_DIR / "video-match.schema.json"
STATE_PATH = RUNTIME_DIR / "state.json"
LOG_DIR = RUNTIME_DIR / "logs"

OUTPUT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": False,
    "required": ["lecture_id", "lecture_summary", "videos", "coverage_gaps"],
    "properties": {
        "lecture_id": {"type": "string", "minLength": 1},
        "lecture_summary": {"type": "string", "minLength": 1},
        "videos": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["rank", "title", "url", "reason"],
                "properties": {
                    "rank": {"type": "integer", "minimum": 1},
                    "title": {"type": "string", "minLength": 1},
                    "url": {"type": "string", "minLength": 1},
                    "reason": {"type": "string", "minLength": 1},
                },
            },
        },
        "coverage_gaps": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
        },
    },
}

PROMPT_TEMPLATE = """Review the Physics 212 lecture notes at:
[LECTURE_NOTES_PATH]

Ignore course logistics and other administrative content. Using the video playlist at:
[PLAYLIST_CSV_PATH]

select the smallest set of strong, nonredundant videos that collectively cover this lecture's main ideas, problem-solving strategies, and representative examples. Return them in a sensible learning order with each exact playlist title, exact URL, and a brief reason. Note any important lecture topic without a strong match. Use only these two files, do not browse the web, and do not modify files. Set lecture_id to "[LECTURE_ID]".
"""

STOP_EVENT = threading.Event()
ACTIVE_LOCK = threading.Lock()
ACTIVE_PROCESSES: dict[int, subprocess.Popen[str]] = {}


@dataclass(frozen=True)
class LectureTask:
    lecture_id: str
    notes_path: Path
    output_path: Path


@dataclass(frozen=True)
class RunResult:
    task: LectureTask
    success: bool
    attempts: int
    error: str = ""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    finally:
        temp_path.unlink(missing_ok=True)


def write_json_atomic(path: Path, payload: Any) -> None:
    atomic_write_text(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def load_playlist(path: Path) -> tuple[dict[str, str], set[tuple[str, str]]]:
    if not path.is_file():
        raise FileNotFoundError(f"Playlist CSV not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"title", "url", "description"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"Playlist CSV must contain columns: {sorted(required)}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"Playlist CSV has no data rows: {path}")
    by_url: dict[str, str] = {}
    pairs: set[tuple[str, str]] = set()
    for row_number, row in enumerate(rows, start=2):
        title = row["title"].strip()
        url = row["url"].strip()
        if not title or not url:
            raise ValueError(f"Blank title or URL in playlist CSV row {row_number}")
        if url in by_url:
            raise ValueError(f"Duplicate playlist URL in row {row_number}: {url}")
        by_url[url] = title
        pairs.add((title, url))
    return by_url, pairs


def discover_tasks(course_root: Path, output_dir: Path, skip_dir: Path) -> list[LectureTask]:
    if not course_root.is_dir():
        raise FileNotFoundError(f"Course root not found: {course_root}")
    skip_dir = skip_dir.resolve()
    notes_files = sorted(course_root.glob("M*/20*/Source/Lecture-Notes.md"))
    tasks: list[LectureTask] = []
    seen_ids: set[str] = set()
    for notes_path in notes_files:
        unit_dir = notes_path.parent.parent
        if unit_dir.resolve() == skip_dir:
            continue
        lecture_id = unit_dir.name
        if lecture_id in seen_ids:
            raise ValueError(f"Duplicate lecture ID discovered: {lecture_id}")
        seen_ids.add(lecture_id)
        tasks.append(
            LectureTask(
                lecture_id=lecture_id,
                notes_path=notes_path.resolve(),
                output_path=(output_dir / f"{lecture_id}.json").resolve(),
            )
        )
    if not tasks:
        raise ValueError(f"No Lecture-Notes.md files found beneath {course_root}")
    return tasks


def build_prompt(task: LectureTask, playlist_csv: Path) -> str:
    return (
        PROMPT_TEMPLATE.replace("[LECTURE_NOTES_PATH]", str(task.notes_path))
        .replace("[PLAYLIST_CSV_PATH]", str(playlist_csv))
        .replace("[LECTURE_ID]", task.lecture_id)
    )


def parse_json_response(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```json") and stripped.endswith("```"):
        stripped = stripped[7:-3].strip()
    elif stripped.startswith("```") and stripped.endswith("```"):
        stripped = stripped[3:-3].strip()
    payload = json.loads(stripped)
    if not isinstance(payload, dict):
        raise ValueError("Codex response is not a JSON object")
    return payload


def validate_result(
    payload: dict[str, Any],
    task: LectureTask,
    playlist_pairs: set[tuple[str, str]],
) -> None:
    if set(payload) != {"lecture_id", "lecture_summary", "videos", "coverage_gaps"}:
        raise ValueError("Result has missing or unexpected top-level fields")
    if payload["lecture_id"] != task.lecture_id:
        raise ValueError(
            f"lecture_id mismatch: expected {task.lecture_id!r}, got {payload['lecture_id']!r}"
        )
    if not isinstance(payload["lecture_summary"], str) or not payload["lecture_summary"].strip():
        raise ValueError("lecture_summary must be a nonempty string")
    videos = payload["videos"]
    if not isinstance(videos, list):
        raise ValueError("videos must be an array")
    seen_urls: set[str] = set()
    for expected_rank, video in enumerate(videos, start=1):
        if not isinstance(video, dict) or set(video) != {"rank", "title", "url", "reason"}:
            raise ValueError(f"Invalid video object at rank {expected_rank}")
        if video["rank"] != expected_rank:
            raise ValueError("Video ranks must be consecutive and start at 1")
        title = video["title"]
        url = video["url"]
        reason = video["reason"]
        if not all(isinstance(value, str) and value.strip() for value in (title, url, reason)):
            raise ValueError(f"Blank or non-string video field at rank {expected_rank}")
        if (title, url) not in playlist_pairs:
            raise ValueError(f"Video is not an exact title/URL pair from the playlist: {title!r}")
        if url in seen_urls:
            raise ValueError(f"Duplicate selected video URL: {url}")
        seen_urls.add(url)
    gaps = payload["coverage_gaps"]
    if not isinstance(gaps, list) or not all(
        isinstance(gap, str) and gap.strip() for gap in gaps
    ):
        raise ValueError("coverage_gaps must be an array of nonempty strings")


def valid_existing_result(
    task: LectureTask, playlist_pairs: set[tuple[str, str]]
) -> bool:
    if not task.output_path.is_file():
        return False
    try:
        payload = json.loads(task.output_path.read_text(encoding="utf-8"))
        validate_result(payload, task, playlist_pairs)
    except (OSError, json.JSONDecodeError, ValueError, TypeError):
        return False
    return True


def terminate_active_processes() -> None:
    with ACTIVE_LOCK:
        processes = list(ACTIVE_PROCESSES.values())
    for process in processes:
        if process.poll() is None:
            process.terminate()
    deadline = time.monotonic() + 5
    for process in processes:
        remaining = max(0.0, deadline - time.monotonic())
        try:
            process.wait(timeout=remaining)
        except subprocess.TimeoutExpired:
            process.kill()


def run_task(
    task: LectureTask,
    *,
    playlist_csv: Path,
    playlist_pairs: set[tuple[str, str]],
    study_root: Path,
    schema_path: Path,
    codex_binary: str,
    model: str | None,
    timeout_seconds: int,
    retries: int,
) -> RunResult:
    if STOP_EVENT.is_set():
        return RunResult(task, False, 0, "cancelled")

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"{task.lecture_id}.log"
    prompt = build_prompt(task, playlist_csv)
    final_error = "unknown error"

    for attempt in range(1, retries + 2):
        if STOP_EVENT.is_set():
            return RunResult(task, False, attempt - 1, "cancelled")
        response_path = RUNTIME_DIR / (
            f".{task.lecture_id}.{os.getpid()}.{uuid.uuid4().hex}.response.tmp"
        )
        command = [
            codex_binary,
            "exec",
            "--ephemeral",
            "--sandbox",
            "read-only",
            "--color",
            "never",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(response_path),
            "-C",
            str(study_root),
            "--add-dir",
            str(playlist_csv.parent),
        ]
        if model:
            command.extend(["--model", model])
        command.append(prompt)

        try:
            with log_path.open("a", encoding="utf-8") as log:
                log.write(f"\n[{utc_now()}] attempt {attempt}\n")
                log.flush()
                process = subprocess.Popen(
                    command,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    text=True,
                )
                with ACTIVE_LOCK:
                    ACTIVE_PROCESSES[process.pid] = process
                try:
                    return_code = process.wait(timeout=timeout_seconds)
                finally:
                    with ACTIVE_LOCK:
                        ACTIVE_PROCESSES.pop(process.pid, None)
            if return_code != 0:
                final_error = f"codex exec exited with status {return_code}; see {log_path}"
                continue
            if not response_path.is_file():
                final_error = "codex exec produced no final-response file"
                continue
            payload = parse_json_response(response_path.read_text(encoding="utf-8"))
            validate_result(payload, task, playlist_pairs)
            write_json_atomic(task.output_path, payload)
            return RunResult(task, True, attempt)
        except subprocess.TimeoutExpired:
            final_error = f"codex exec timed out after {timeout_seconds} seconds"
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
        except (OSError, json.JSONDecodeError, ValueError, TypeError) as exc:
            final_error = str(exc)
        finally:
            response_path.unlink(missing_ok=True)

    return RunResult(task, False, retries + 1, final_error)


def load_state() -> dict[str, Any]:
    state = load_json(STATE_PATH, {})
    if not isinstance(state, dict):
        state = {}
    state.setdefault("version", 1)
    state.setdefault("completed", {})
    state.setdefault("failures", {})
    return state


def save_state(state: dict[str, Any]) -> None:
    state["updated_at"] = utc_now()
    write_json_atomic(STATE_PATH, state)


def rebuild_combined_csv(
    tasks: list[LectureTask], playlist_pairs: set[tuple[str, str]], output_dir: Path
) -> int:
    rows: list[dict[str, Any]] = []
    for task in tasks:
        if not task.output_path.is_file():
            continue
        try:
            payload = json.loads(task.output_path.read_text(encoding="utf-8"))
            validate_result(payload, task, playlist_pairs)
        except (OSError, json.JSONDecodeError, ValueError, TypeError):
            continue
        for video in payload["videos"]:
            rows.append(
                {
                    "lecture_id": task.lecture_id,
                    "rank": video["rank"],
                    "title": video["title"],
                    "url": video["url"],
                    "reason": video["reason"],
                }
            )

    output_path = output_dir / "lecture-video-matches.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(
        prefix=f".{output_path.name}.", suffix=".tmp", dir=output_path.parent
    )
    temp_path = Path(temp_name)
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["lecture_id", "rank", "title", "url", "reason"],
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, output_path)
    finally:
        temp_path.unlink(missing_ok=True)
    return len(rows)


def clean_stale_temp_files(output_dir: Path) -> None:
    for directory in (RUNTIME_DIR, output_dir):
        if not directory.exists():
            continue
        for path in directory.glob(".*.tmp"):
            if path.is_file():
                path.unlink(missing_ok=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run one isolated Codex video-matching task per Physics 212 lecture."
    )
    parser.add_argument("--course-root", type=Path, default=DEFAULT_COURSE_ROOT)
    parser.add_argument("--playlist-csv", type=Path, default=DEFAULT_PLAYLIST_CSV)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--skip-dir", type=Path, default=DEFAULT_SKIP)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=1800, help="Seconds per Codex attempt")
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--model", help="Optional Codex model override")
    parser.add_argument("--codex-binary", default="codex")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, help="Process only the first N pending lectures")
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="LECTURE_ID",
        help="Process only this lecture ID; may be repeated",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.workers < 1:
        raise ValueError("--workers must be at least 1")
    if args.timeout < 1:
        raise ValueError("--timeout must be at least 1")
    if args.retries < 0:
        raise ValueError("--retries cannot be negative")
    if args.limit is not None and args.limit < 1:
        raise ValueError("--limit must be at least 1")

    course_root = args.course_root.expanduser().resolve()
    playlist_csv = args.playlist_csv.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()
    skip_dir = args.skip_dir.expanduser().resolve()
    study_root = DEFAULT_STUDY_ROOT.resolve()

    _, playlist_pairs = load_playlist(playlist_csv)
    all_tasks = discover_tasks(course_root, output_dir, skip_dir)
    if args.only:
        requested = set(args.only)
        known = {task.lecture_id for task in all_tasks}
        unknown = sorted(requested - known)
        if unknown:
            raise ValueError(f"Unknown --only lecture ID(s): {', '.join(unknown)}")
        all_tasks = [task for task in all_tasks if task.lecture_id in requested]

    skipped = [] if args.overwrite else [
        task for task in all_tasks if valid_existing_result(task, playlist_pairs)
    ]
    skipped_ids = {task.lecture_id for task in skipped}
    pending = [task for task in all_tasks if task.lecture_id not in skipped_ids]
    if args.limit is not None:
        pending = pending[: args.limit]

    if args.dry_run:
        print(
            f"Discovered {len(all_tasks)} lecture(s); {len(skipped)} valid result(s) would be "
            f"skipped; {len(pending)} task(s) would run with {args.workers} worker(s)."
        )
        for task in pending:
            print(f"\n--- {task.lecture_id} ---\n{build_prompt(task, playlist_csv)}")
        return 0

    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    clean_stale_temp_files(output_dir)
    write_json_atomic(SCHEMA_PATH, OUTPUT_SCHEMA)
    state = load_state()

    if not pending:
        row_count = rebuild_combined_csv(all_tasks, playlist_pairs, output_dir)
        print(
            f"Nothing to run: {len(skipped)} valid lecture result(s) already exist. "
            f"Rebuilt combined CSV with {row_count} video match row(s)."
        )
        return 0

    failures: list[RunResult] = []
    successes = 0
    progress = tqdm(
        total=len(skipped) + len(pending),
        initial=len(skipped),
        unit="lecture",
        desc="Matching videos",
        dynamic_ncols=True,
    )
    executor = ThreadPoolExecutor(max_workers=args.workers)
    futures: dict[Future[RunResult], LectureTask] = {}
    try:
        for task in pending:
            future = executor.submit(
                run_task,
                task,
                playlist_csv=playlist_csv,
                playlist_pairs=playlist_pairs,
                study_root=study_root,
                schema_path=SCHEMA_PATH,
                codex_binary=args.codex_binary,
                model=args.model,
                timeout_seconds=args.timeout,
                retries=args.retries,
            )
            futures[future] = task

        for future in as_completed(futures):
            task = futures[future]
            try:
                result = future.result()
            except Exception as exc:  # Defensive boundary around worker failures.
                result = RunResult(task, False, 0, f"unexpected worker error: {exc}")
            if result.success:
                successes += 1
                state["completed"][task.lecture_id] = {
                    "output": str(task.output_path),
                    "completed_at": utc_now(),
                    "attempts": result.attempts,
                }
                state["failures"].pop(task.lecture_id, None)
            else:
                failures.append(result)
                state["failures"][task.lecture_id] = {
                    "error": result.error,
                    "failed_at": utc_now(),
                    "attempts": result.attempts,
                }
                tqdm.write(f"FAILED {task.lecture_id}: {result.error}")
            save_state(state)
            progress.update(1)
    except KeyboardInterrupt:
        STOP_EVENT.set()
        tqdm.write("Interrupted; terminating active Codex sessions...")
        terminate_active_processes()
        for future in futures:
            future.cancel()
        return 130
    finally:
        progress.close()
        executor.shutdown(wait=not STOP_EVENT.is_set(), cancel_futures=STOP_EVENT.is_set())

    row_count = rebuild_combined_csv(all_tasks, playlist_pairs, output_dir)
    print(
        f"Completed {successes} lecture(s); skipped {len(skipped)}; "
        f"failed {len(failures)}. Combined CSV contains {row_count} video match row(s)."
    )
    return 1 if failures else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
