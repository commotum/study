# Failure Mode Log

## Single-Step Template

## [LOG_ENTRY_ID] — [FAILURE_MODE_ID] — [LESSON_ID]

**Date:** [YYYY-MM-DD]
**Lesson ID:** `[LESSON_ID]`
**Step ID:** `[LESSON_ITEM_ID]`
**Failure Mode:** `[FAILURE_MODE_ID]` — [FAILURE_MODE_NAME]

**Diagnostic:** [In 1–2 sentences, describe the step item’s specific structure, its attributes, how it's constructed, and which distinct dimensions it varies across. Then explain how that structure activates the failure mode.]


## Multi-Step Template

## [LOG_ENTRY_ID] — [FAILURE_MODE_ID] — [LESSON_ID]

**Date:** [YYYY-MM-DD]
**Lesson ID:** `[LESSON_ID]`
**Step IDs:** `[LESSON_ITEM_ID_1]`, `[LESSON_ITEM_ID_2]`

**Failure Mode:** `[FAILURE_MODE_ID]` — [FAILURE_MODE_NAME]

**Diagnostic:** [In 1–2 sentences, describe the shared structure across the step items, their attributes, how they're constructed, and which distinct dimensions they vary across. Then explain how that shared structure activates the failure mode.]


## LOG-2026-06-08-001 — FM-DB-MCQ — EE01-M13-04-L02

**Date:** 2026-06-08  
**Lesson ID:** `EE01-M13-04-L02`  
**Step ID:** `EE01-M13-04-L02-q003`  
**Failure Mode:** `FM-DB-MCQ` — Double-Barreled MCQ  

**Diagnostic:** The question stem asks for two outputs at once—the **support** and the **zero regions**—and each answer choice bundles both interval sets into a single all-or-nothing option. Because the distractors vary across multiple dimensions at the same time, including swapped support/zero regions, missing internal zero intervals, overgeneralized support, and incorrect endpoint inclusion, a wrong answer does not isolate which specific skill or misconception caused the error.


## LOG-2026-06-08-002 — FM-SPF — EE01-M03-01-L01

**Date:** 2026-06-08  
**Lesson ID:** `EE01-M03-01-L01`  
**Step IDs:** `introduction-to-delaying-a-signal`, `delaying-a-single-feature-time`, `EE01-M03-01-L01-q001`, `EE01-M03-01-L01-q002`  

**Failure Mode:** `FM-SPF` — Split Plotting Failure  

**Diagnostic:** The introduction, first single-feature example, and Questions 1-2 all use delay diagrams to compare an original peak or signal feature with $y(t)=x(t-T)$, varying original feature time and delay amount while preserving height and shape. Because the learning task depends on visually aligning the original and delayed feature locations, showing the related plots separately forces learners to reconcile separate axes instead of seeing the right shift on one shared coordinate grid.


## LOG-2026-06-08-003 — FM-MLF — EE01-M01-02-L01

**Date:** 2026-06-08  
**Lesson ID:** `EE01-M01-02-L01`  
**Step ID:** `finding-a-valid-positive-shift-for-a-repeating-signal`  
**Failure Mode:** `FM-MLF` — Malformed LaTeX Formatting  

**Diagnostic:** The second worked example presents a repeating piecewise-constant block as a display-math `aligned` list whose rows combine half-open interval notation, alignment markers, colon separators, and scalar values. That pseudo-table construction mixes textual interval/value structure into LaTeX alignment syntax, activating malformed LaTeX formatting because the Markdown math environment may not render the intended interval-to-value listing cleanly.
