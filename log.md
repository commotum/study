# Failure Mode Log

## [LOG_ENTRY_ID] — [FAILURE_MODE_ID] — [LESSON_ITEM_ID]

**Date:** [YYYY-MM-DD]
**Lesson ID:** `[LESSON_ID]`
**Step ID:** `[LESSON_ITEM_ID]`
**Failure Mode:** `[FAILURE_MODE_ID]` — [FAILURE_MODE_NAME]

**Diagnostic:** [In 1–2 sentences, describe the step item’s specific structure, its attributes, how it's constructed, and which distinct dimensions it varies across. Then explain how that structure activates the failure mode.]


## LOG-2026-06-08-001 — FM-DB-MCQ — EE01-M13-04-L02-q003

**Date:** 2026-06-08  
**Lesson ID:** `EE01-M13-04-L02`  
**Step ID:** `EE01-M13-04-L02-q003`  
**Failure Mode:** `FM-DB-MCQ` — Double-Barreled MCQ  

**Diagnostic:** The question stem asks for two outputs at once—the **support** and the **zero regions**—and each answer choice bundles both interval sets into a single all-or-nothing option. Because the distractors vary across multiple dimensions at the same time, including swapped support/zero regions, missing internal zero intervals, overgeneralized support, and incorrect endpoint inclusion, a wrong answer does not isolate which specific skill or misconception caused the error.