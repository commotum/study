# 3-COMPONENT

## Current Facts

- Stage 2 accepted exact dependency `mathlive@0.110.0` and produced `src/ui/MathBlankInput.svelte`.
- The component already demonstrates structured physical keyboard entry, normalized ASCIIMath change events, value restoration, structured paste, disabled state, reset compatibility, focus transfer, and offline inlined fonts in a browser harness.
- The component is not yet routed from `QuizPrompt.svelte`; the plugin production bundle still behaves exactly as before.
- The strict runtime schema does not yet accept `input_mode`.
- The two existing blank render paths are ordinary inline Markdown blanks and display-math row blank slots.

## Updated Assumptions

- The prototype component is suitable for production hardening rather than replacement.
- Shared conversion and comparison logic should move out of the Svelte component before Stage 4 tests, but Stage 3 may expose the minimal helpers required for integration.
- Correct/wrong styling should be expressed as component props/classes so both rendering paths retain the current visual states.
- The prototype harness can remain as a focused interactive regression surface if it stays lint/build clean and does not enter plugin artifacts.

## Big Picture Objective

Route only opted-in blank blocks through the reusable visual math component in both prompt layouts while leaving every legacy text blank unchanged.

## Detailed Implementation Plan

- Add strict `input_mode: text | math` with default `text` to `QuizBlankSchema`.
- Derive math mode once in `QuizPrompt.svelte` and conditionally render `MathBlankInput` in both ordinary and display-math paths.
- Pass value, disabled state, accessible label, change callback, and exact grading state into the component.
- Add component props/classes for correct/wrong state without weakening reveal-only neutrality.
- Ensure math answer reveal is typeset from keyboard source rather than shown as raw ASCIIMath.
- Preserve current native text markup, classes, handlers, and comparison behavior verbatim when input mode is text.
- Ensure multiple blank indexing, blank count, Check enablement, result badge, feedback, reset, and saved-state callbacks continue to work.
- Add `input_mode: math` examples to the plugin test vault for ordinary, multiple, display-math, exact, and reveal-only cases.
- Inline MathLive fonts in the production Vite build and verify no additional asset files are required.
- Run lint, production build, prototype build, diff check, and targeted code review.

## No-Cheating Checks

- Do not auto-detect math from answer contents.
- Do not replace the existing text path with MathLive.
- Do not duplicate MathLive initialization logic in `QuizPrompt.svelte`.
- Do not mark reveal-only math fields correct or wrong.
- Do not show raw ASCIIMath as the polished reveal.
- Do not allow emitted font files or runtime fetches to escape the deployable plugin artifacts.

## Completion Requirements

- [x] Runtime schema accepts only `text` or `math` on blank blocks and defaults to text.
- [x] Both blank render paths use the component only in math mode.
- [x] Text-mode markup/behavior remains on the existing native-input branch.
- [x] Correct/wrong/reveal/feedback/reset/result behavior is wired; math structural normalization is the explicit Stage 4 task.
- [x] Multiple math fields retain independent indexed state.
- [x] Production build, prototype build, lint, and diff checks pass.
- [x] Production artifact sizes and asset set are recorded.

## Stage Results

- Added `input_mode: text | math` with default `text` to the strict blank runtime schema.
- Added shared conversion helpers in `src/math-input.ts` and the reusable `MathBlankInput.svelte` component.
- Routed both ordinary and display-math blank render paths through MathLive only when `input_mode === "math"`; the legacy native inputs remain in their existing branches.
- Wired accessible labels, normalized string state, disabled state, correct/wrong classes, structured reveal, feedback, reset, Check enablement, result badge, and indexed callbacks.
- Added exact, reveal-only, multiple-blank, and display-math examples to `_test-vault/playground.md`.
- Production Vite now inlines MathLive fonts. No `.woff2`, sound, or other runtime asset file is emitted.
- Baseline → integrated production artifacts:
  - `main.js`: 276,595 → 1,099,344 bytes; gzip 87,875 → 314,320.
  - `styles.css`: 13,553 → 363,890 bytes; gzip 2,808 → 266,424.
- `npm run lint`: passed with zero diagnostics.
- `npm run build`: passed, 296 modules transformed.
- `npm run prototype:build`: passed.
- `npm exec vite -- build --mode development`: passed and refreshed the plugin inside `_test-vault` for later Obsidian verification.
- `git diff --check`: passed.
- Remaining by design: the existing text comparator cannot yet match editor-canonical forms such as `(2)/(3)` to keyboard source `2/3`; Stage 4 owns symmetric structural normalization and its tests.
