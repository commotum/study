---
name: match-ma-lesson
description: Find the Math Academy lesson or lessons that best match a given math problem by using the study repo's global Math Academy topics index, then verifying candidates against the actual examples and questions in the lesson markdown. Use when the user gives a single math problem, assignment problem, or problem excerpt and asks which Math Academy lessons cover the same skills, knowledge, or question type.
---

# Match MA Lesson

## Overview

Match a given math problem to Math Academy lessons in the study vault. Use the index to find candidate lessons, but choose matches only after inspecting the candidate lesson markdown and comparing its examples/questions to the given problem.

## Workflow

1. Identify the problem's mathematical task.
   - Extract the topic, operation, requested output, givens, constraints, notation, and needed prerequisite facts.
   - If the user provides a file path, inspect the exact problem text and cite the line number.
   - Keep the problem atomic; do not broaden to nearby assignment problems unless the user asks for a whole assignment.

2. Search the global Math Academy index first.
   - Use `util/Mathematical-Foundations/topics.csv` as the primary index.
   - The useful columns are `course`, `topic-number`, `topic-name`, `md-path`, and `src-path`.
   - Search topic names with the problem's core concepts and synonyms.
   - Prefer `rg` for local search.

```bash
rg -n -i "right riemann|riemann sum|definite integral" util/Mathematical-Foundations/topics.csv
```

3. Expand the candidate set when the index is too broad or too sparse.
   - Search lesson markdown under `vault/MA` for exact terms, notation, and distinctive objects from the problem.
   - Include prerequisite candidates when the problem requires a separate skill, such as special-angle trig values, exponent rules, factoring, or interpreting a graph.
   - Keep the working candidate list small enough to inspect carefully, usually 5-12 lessons.

```bash
rg -n -i "Question|Example|right Riemann|cos" vault/MA/Mathematical-Foundations/MF*/**/Lessons/*.md
```

4. Inspect candidate lesson questions and examples.
   - Open each candidate `md-path`; only use `src-path` if images, tables, or source assets are needed to understand a prompt.
   - Search inside each lesson for `**Question`, `**Example`, `Problem`, and the problem's key terms.
   - Read enough surrounding lines to understand the actual question type.

```bash
rg -n "Question|Example|Problem|right Riemann|cos" "vault/MA/path/to/Lesson.md"
nl -ba "vault/MA/path/to/Lesson.md" | sed -n '80,140p'
```

5. Rank by question-level similarity.
   - Treat matching lesson questions/examples as stronger evidence than a matching lesson title.
   - Prefer lessons that match the same mathematical action, such as compute, solve, estimate, graph, simplify, prove, or interpret.
   - Prefer lessons with the same representation, such as equation, table, graph, interval, sigma notation, word problem, or exact value.
   - Prefer lessons with the same answer form and constraints, such as exact value, decimal approximation, interval notation, multiple choice, or "do not compute X".
   - Mark prerequisite lessons separately from the main lesson; do not present a prerequisite as the best match unless it is the main task.
   - Mark nearby but weaker lessons as secondary when they teach related notation or a more advanced/later version of the idea.

6. Report the result with evidence.
   - Give the best match first.
   - Include supporting/prerequisite lessons only when needed to do the problem.
   - Include line-linked file references for the index entry and for the matching lesson question/example.
   - Explain the match in terms of the task shape, not just keywords.
   - If useful, include a brief solution scaffold to show why the selected skills are necessary.
   - Do not claim an exact match unless a lesson question/example closely resembles the given problem.

## Output Shape

Use this structure unless the user asks for a different format:

```markdown
Best match: [lesson title](absolute path with line)

Why: ...
Evidence: the lesson question/example at line ... asks students to ...

Prerequisite/supporting lessons:
- [lesson title](absolute path with line): why it is needed

Near misses:
- [lesson title](absolute path with line): why it is related but not the best match
```

## Local Paths

- Study repo root: `/Users/jake/Developer/study`
- Global MA topics index: `util/Mathematical-Foundations/topics.csv`
- Math Academy vault root: `vault/MA`

If a command is run from another working directory, resolve these paths relative to the study repo root.
