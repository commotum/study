# Validation Rubric

Use this before final response.

## Lesson Quality

- The lesson teaches one core move.
- The recognition cue is visible early.
- Prerequisites are minimal.
- The first example is canonical.
- Each later section changes one wrinkle.
- Practice is attached to the relevant section.
- Summary gives a reusable procedure.

## Quiz-Block Quality

- Every practice item is inside a fenced `quiz` block.
- No raw checklist MCQ remains, such as `- [ ] A.`.
- Normal multiple-choice practice uses `type: radio`.
- Every radio block has exactly one `correct: true`.
- Every generated quiz block has an `id`.
- Every generated radio option has an `id`.
- Distractors represent real mistakes.

## Required Command

For ordinary generated lessons, run:

```bash
python3 /Users/jake/Developer/study/util/skills/core-move-lesson/scripts/validate_quiz_blocks.py \
  /path/to/lesson.md \
  --require-radio-practice \
  --strict-ids
```

Fix every error before reporting completion.

## Optional Math Academy Comparison

When the user asks for refinement, compare against 3-4 random files from `/Users/jake/Developer/MA/DATA/Lessons/*/*.md` and look for:

- table of contents and prerequisites
- example/explanation/question loops
- section-level practice
- controlled progression
- representation/image use
- concise worked-example language

Incorporate structural improvements, not topic-specific content.
