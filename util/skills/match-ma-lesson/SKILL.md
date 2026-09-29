---
name: match-ma-lesson
description: Find and verify the Math Academy lesson or lessons that best match a given math problem, classify whether a genuine question-level equivalent exists, and explicitly signal when the problem needs a generated core-move fallback. Use when the user gives a single math problem, assignment problem, or problem excerpt and asks which Math Academy lessons cover the same skills, knowledge, or question type, including assignment workflows that must distinguish true matches from unmatched problems.
---

# Match MA Lesson

## Overview

Match a given math problem to Math Academy lessons in the study vault. Use the scoped indices to find candidate lessons, but choose matches only after inspecting the candidate lesson markdown and comparing its examples/questions to the given problem.

## Course Routing

For Fall 2026, search Mathematical Foundations I, II, and III (`MF1`, `MF2`, `MF3`) first, then the subject course selected below. The shared `vault/MA/Mathematical-Foundations/catalog.csv` covers all three foundations courses; their individual `topics.csv` files provide course-local detail.

| OSU course | Assignment folder | Second-pass Math Academy course | Course-local index |
| --- | --- | --- | --- |
| MTH 255 — Vector Calculus II | `vault/F26/255` | Multivariable Calculus (`MVC`) | `vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv` |
| MTH 256 — Applied Differential Equations | `vault/F26/256` | Differential Equations (`DEQ`) | `vault/MA/Mathematical-Analysis-&-Modeling/DEQ/topics.csv` |
| MTH 341 — Linear Algebra | `vault/F26/341` | Linear Algebra (`LAL`) | `vault/MA/Mathematical-Analysis-&-Modeling/LAL/topics.csv` |

Determine the OSU course from the user's explicit context or the assignment's course folder, accepting forms such as `255`, `MTH 255`, and `MTH-255`. For a standalone problem with no course context, infer the subject route from its mathematical task; ask only if the route remains ambiguous. Do not search all three subject courses by default.

Search order does not override question-level equivalence: retain genuine foundations matches and useful prerequisites, then inspect the relevant subject-course candidates. Prefer a foundations lesson when it is equally close to the actual task; never substitute a foundations prerequisite for an equivalent subject-course lesson.

## Workflow

1. Identify the problem's mathematical task.
   - Extract the topic, operation, requested output, givens, constraints, notation, and needed prerequisite facts.
   - If the user provides a file path, inspect the exact problem text and cite the line number.
   - Keep the problem atomic; do not broaden to nearby assignment problems unless the user asks for a whole assignment.

2. Search the scoped Math Academy indices first.
   - First search `vault/MA/Mathematical-Foundations/catalog.csv` across `MF1`, `MF2`, and `MF3`, and inspect promising lesson questions/examples.
   - Second search and inspect the course-local `topics.csv` selected by Course Routing: `MVC` for MTH 255, `DEQ` for MTH 256, or `LAL` for MTH 341.
   - For archived MTH-252/MTH-253 review, retain the foundations-first search followed by `vault/MA/Single-Variable-Calculus/CA2/topics.csv`. Do not use CA2 as the default subject course for Fall 2026.
   - The useful group catalog columns are `layer`, `topic-id`, `topic-code`, `topic-name`, `lesson-path`, and `source-path`.
   - The useful course topics columns are `topic-id`, `topic-code`, `topic-number`, `topic-name`, `unit`, `module`, `lesson-path`, `source-path`, and `layer`.
   - Use `layer` for study-order and prerequisite-readiness decisions. Unit/module order is structural navigation, not the study queue order.
   - In course-local `topics.csv`, `lesson-path` and `source-path` are relative to that course folder. For MVC, for example, prefix them with `vault/MA/Mathematical-Analysis-&-Modeling/MVC/`. Group catalog paths already start with `vault/` and are relative to the study repo root.
   - Search topic names with the problem's core concepts and synonyms.
   - Prefer `rg` for local search.

```bash
# MTH 255 example: inspect foundations candidates before the MVC search.
rg -n -i "vector|dot product|cross product|integral" vault/MA/Mathematical-Foundations/catalog.csv
rg -n -i "line integral|surface integral|stokes|divergence" 'vault/MA/Mathematical-Analysis-&-Modeling/MVC/topics.csv'
```

3. Expand the candidate set when the index is too broad or too sparse.
   - Search lesson markdown under the relevant scoped course folders for exact terms, notation, and distinctive objects from the problem.
   - Use the global `vault/MA/catalog.csv` only as a broad fallback after both the foundations and routed subject-course searches fail to provide a genuine equivalent. State when a match comes from outside the normal course route.
   - Include prerequisite candidates when the problem requires a separate skill, such as special-angle trig values, exponent rules, factoring, or interpreting a graph.
   - Keep the working candidate list small enough to inspect carefully, usually 5-12 lessons.

```bash
rg -n -i -g '*.md' "line integral|surface integral" 'vault/MA/Mathematical-Analysis-&-Modeling/MVC'
```

4. Inspect candidate lesson questions and examples.
   - Open each candidate `lesson-path`; only use `source-path` if images, tables, or source assets are needed to understand a prompt.
   - Search inside each lesson for `**Question`, `**Example`, `Problem`, and the problem's key terms.
   - Read enough surrounding lines to understand the actual question type.

```bash
rg -n "Question|Example|Problem|line integral" "vault/MA/path/to/Lesson.md"
nl -ba "vault/MA/path/to/Lesson.md" | sed -n '80,140p'
```

5. Rank by question-level similarity.
   - Treat matching lesson questions/examples as stronger evidence than a matching lesson title.
   - Prefer lessons that match the same mathematical action, such as compute, solve, estimate, graph, simplify, prove, or interpret.
   - Prefer lessons with the same representation, such as equation, table, graph, interval, sigma notation, word problem, or exact value.
   - Prefer lessons with the same answer form and constraints, such as exact value, decimal approximation, interval notation, multiple choice, or "do not compute X".
   - Mark prerequisite lessons separately from the main lesson; do not present a prerequisite as the best match unless it is the main task.
   - Mark nearby but weaker lessons as secondary when they teach related notation or a more advanced/later version of the idea.
   - Count a problem as matched only when at least one lesson question/example teaches the same core move and has substantially the same task shape. A shared topic name, prerequisite skill, or nearby technique is not enough.
   - If every candidate is only a prerequisite, near miss, broader survey, or different question type, classify the result as `No equivalent Math Academy lesson` instead of forcing a weak main match.

6. Report the result with evidence.
   - Start with exactly one match status: `Equivalent Math Academy lesson found` or `No equivalent Math Academy lesson`.
   - Give the best match first.
   - Briefly identify the foundations-first search and the subject course used, so the course routing is visible.
   - Include supporting/prerequisite lessons only when needed to do the problem.
   - Include line-linked file references for the index entry and for the matching lesson question/example.
   - Explain the match in terms of the task shape, not just keywords.
   - If useful, include a brief solution scaffold to show why the selected skills are necessary.
   - Do not claim an exact match unless a lesson question/example closely resembles the given problem.
   - For `No equivalent Math Academy lesson`, keep useful prerequisites and near misses clearly separated, and do not label either as the main lesson.
   - When the caller supplies an assignment file and problem number, include a fallback directive naming both: run `lesson-pipeline` in targeted mode for that problem. The assignment-level caller, normally `setup-lessons`, owns that invocation; do not run the full-assignment pipeline from this single-problem matcher.

## Output Shape

Use this structure unless the user asks for a different format:

```markdown
Match status: Equivalent Math Academy lesson found

Best match: [lesson title](absolute path with line)

Why: ...
Evidence: the lesson question/example at line ... asks students to ...

Prerequisite/supporting lessons:
- [lesson title](absolute path with line): why it is needed

Near misses:
- [lesson title](absolute path with line): why it is related but not the best match
```

For an unmatched problem, use:

```markdown
Match status: No equivalent Math Academy lesson

Why: ...

Prerequisite/supporting lessons:
- [lesson title](absolute path with line): why it is useful but not equivalent

Near misses:
- [lesson title](absolute path with line): the task-shape mismatch

Fallback: Run $lesson-pipeline in targeted mode for Problem N in /absolute/path/to/assignment.md.
```

## Local Paths

- Study repo root: `/home/jake/Developer/study` in this environment; on another machine, locate the checkout containing `util/skills/match-ma-lesson` and `vault/MA`.
- Primary Mathematical Foundations catalog: `vault/MA/Mathematical-Foundations/catalog.csv`
- Foundations course-local topics: `vault/MA/Mathematical-Foundations/{MF1,MF2,MF3}/topics.csv`
- Fall 2026 subject-course topics: `vault/MA/Mathematical-Analysis-&-Modeling/{MVC,DEQ,LAL}/topics.csv` (select one using Course Routing)
- Local course names/codes: `vault/MA/Mathematical-Foundations/courses.csv` and `vault/MA/Mathematical-Analysis-&-Modeling/courses.csv`
- Archived Calculus II course-local topics: `vault/MA/Single-Variable-Calculus/CA2/topics.csv`
- Broad fallback catalog: `vault/MA/catalog.csv`
- Group-local catalogs: `vault/MA/<Group>/catalog.csv`
- Course-local topics/prerequisites: `vault/MA/<Group>/<Course>/topics.csv` and `vault/MA/<Group>/<Course>/prerequisites.csv`
- Math Academy vault root: `vault/MA`

If a command is run from another working directory, resolve these paths relative to the study repo root.
