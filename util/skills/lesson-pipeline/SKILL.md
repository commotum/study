---
name: lesson-pipeline
description: Generate all missing core-move lessons for a single Markdown assignment file by detecting problem sections, skipping already-associated lessons, and launching same-model sub-agents to run core-move-lesson followed by core-move-refiner for each missing problem. Use when the user gives one assignment path and wants every problem in that file to have a corresponding lesson without overwriting completed lessons.
---

# Lesson Pipeline

## Overview

Take one assignment Markdown file, identify every problem in it, skip problems that already have lesson files, and create the missing lessons by delegating one problem per same-model worker sub-agent. The pipeline is complete only when every problem in the assignment has an associated lesson file.

Required local skills:

```text
/Users/jake/Developer/study/util/skills/core-move-lesson
/Users/jake/Developer/study/util/skills/core-move-refiner
```

## Assignment Contract

- Input must be one Markdown assignment file, such as `.../HW-1/HW-1.md`.
- Problems are normally headed `## Problem N`.
- The lesson directory is `Lessons/` next to the assignment file.
- The expected lesson for problem `N` is `Lessons/Problem-N.md`.
- A problem is considered already associated when its expected lesson file exists and is non-empty.
- Do not overwrite, delete, rename, or regenerate existing associated lesson files unless the user explicitly asks for that.

## Workflow

1. Resolve and inspect the assignment.
   - Confirm the provided path is a file.
   - Read the assignment enough to identify all `## Problem N` headings.
   - Preserve problem numbering exactly as written.
   - If no `## Problem N` headings exist, stop and ask for clarification instead of guessing.

Useful commands from the study repo root:

```bash
rg -n '^## Problem [0-9]+' /path/to/assignment.md
find /path/to/assignment-parent/Lessons -maxdepth 1 -type f -name 'Problem-*.md'
```

2. Determine missing lessons.
   - Set `assignment_dir` to the assignment file's parent directory.
   - Set `lesson_dir` to `assignment_dir/Lessons`.
   - Create `lesson_dir` if it does not exist.
   - For each problem number `N`, compute `lesson_dir/Problem-N.md`.
   - Skip any expected lesson file that exists and is non-empty.
   - Treat a missing or zero-byte expected lesson file as work to do.
   - Report the total problem count, skipped count, and missing count before launching workers.
   - If no lessons are missing, do not launch sub-agents; proceed directly to the completion check.

3. Launch one worker sub-agent per missing problem.
   - If multi-agent tools are not currently exposed, use tool discovery with a query such as `multi-agent spawn subagent wait`.
   - Use `multi_agent_v1.spawn_agent` with `agent_type: "worker"`.
   - Omit the `model` field. Spawned agents inherit the parent model by default; this is the required same-model behavior.
   - Do not set `model` to a smaller or cheaper model such as mini or spark.
   - Use `fork_context: false` unless the current thread contains essential context that is not in the prompt.
   - Pass both local skills as skill items when the tool supports structured items.
   - Give each worker ownership of exactly one expected lesson file, such as `Lessons/Problem-7.md`.
   - Tell each worker that other agents may be editing different lesson files and that it must not revert unrelated files.

Example worker prompt:

```text
Use $core-move-lesson at /Users/jake/Developer/study/util/skills/core-move-lesson and $core-move-refiner at /Users/jake/Developer/study/util/skills/core-move-refiner.

Assignment file: /absolute/path/to/assignment.md
Problem number: N
Target lesson file: /absolute/path/to/Lessons/Problem-N.md

Create the missing lesson for only Problem N. First run the core-move-lesson workflow for Problem N, then run the core-move-refiner workflow on the lesson you created. Do not edit any other lesson file. Do not overwrite existing non-empty files. Validate the final quiz blocks and run git diff --check for your target file. In your final response, list the target file, whether validation passed, and any issue that prevented completion.
```

When using structured `items`, include the two skill paths explicitly:

```text
type=skill name=core-move-lesson path=/Users/jake/Developer/study/util/skills/core-move-lesson
type=skill name=core-move-refiner path=/Users/jake/Developer/study/util/skills/core-move-refiner
```

4. Manage concurrency.
   - Launch workers in parallel when the missing set is modest.
   - For large assignments, batch workers in manageable groups so tool limits and merge review stay practical.
   - Keep write scopes disjoint: one worker owns one `Problem-N.md`.
   - While workers run, do not locally edit the same target files.

5. Collect results and verify.
   - Wait for all worker agents to finish.
   - Close completed agents after collecting their final statuses.
   - For each worker, inspect whether its expected lesson file now exists and is non-empty.
   - Run the core-move lesson quiz validator on each newly created lesson:

```bash
python3 /Users/jake/Developer/study/util/skills/core-move-lesson/scripts/validate_quiz_blocks.py \
  /path/to/Lessons/Problem-N.md \
  --require-radio-practice \
  --strict-ids
```

   - Run `git diff --check -- /path/to/Lessons/Problem-N.md` for each new lesson, or for all new files together.
   - If a worker failed or a lesson is still missing, relaunch a worker for that problem or complete that single problem locally with the same `core-move-lesson` then `core-move-refiner` sequence.

6. Completion condition.
   - Recompute the full problem-to-lesson map from the assignment file.
   - The task is not complete until every `## Problem N` has a non-empty `Lessons/Problem-N.md`.
   - Existing skipped lessons count toward completion, but do not silently claim they were newly generated.

## Final Response

Report:

- Assignment path.
- Number of problems found.
- Existing lesson files skipped.
- New lesson files created.
- Any problems that could not be completed.
- Validation status for new lessons.

Keep the response focused on the pipeline outcome. Do not paste full lesson contents.
