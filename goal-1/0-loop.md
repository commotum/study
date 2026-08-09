# MATH-BLANKS Execution Loop

Use this protocol for every stage in `goal-1/0-plan.md`.

## Repeatable Loop

1. Sync current state with the actual standalone plugin checkout, study submodule, relevant authoring utilities, documentation, saved-state code, installed artifacts, and tests.
2. Update `goal-1/0-plan.md` with current facts before starting the next stage.
3. Select the first incomplete indexed stage.
4. Create or refresh `goal-1/[INDEX]-[SHORTHAND].md` from the stage template below.
5. Implement only that stage. Work on the existing `master` line unless the user changes that instruction.
6. Add verification and no-cheating checks that cover the stage's real requirement rather than an easier proxy.
7. Run focused tests, full verification appropriate to the stage, and whitespace/diff checks. At minimum consider plugin lint/type/Svelte checks, production build, quiz-block validator tests, representative corpus validation, `git diff --check`, and manual Obsidian behavior.
8. Record commands, outcomes, failures, evidence, and new facts in the stage file.
9. Fold the results and changed assumptions back into `goal-1/0-plan.md`.
10. Continue toward the original objective. If stopping for the session, leave the goal resumable with current evidence, the exact next experiment or edit, unblock actions, and assumptions that still need to be challenged.

## Invariants

- Do not narrow the user's objective without saying so.
- Do not mark a stage complete without evidence.
- Do not use tests or green checks as evidence unless they cover the requirement.
- Prefer small, low-complexity stages that narrow uncertainty.
- Convert blockers into work items: decompose them, route around them, or turn them into proof and verification tasks.
- Preserve the distinction between implementation, verifier, diagnostic, and fallback paths.
- Keep the math editor opt-in; absence of the new field must retain the existing text input.
- Keep keyboard-friendly answers inside `==...==`; do not make LaTeX authoring a hidden prerequisite.
- Do not present a text box plus preview as a completed visual editor.
- Do not describe normalization as symbolic equivalence.
- Preserve `require_exact: false` reveal behavior and root-level `feedback`.
- Preserve old saved states and existing Math Academy content unless an explicit migration is separately justified and reviewed.
- Keep runtime schema, authoring schema, validator, docs, tests, and examples synchronized.
- Treat `/Users/jake/Developer/obsidian-quiz-blocks` as the implementation source of truth; update the study submodule only to a tested committed revision.
- Preserve unrelated worktree changes in the study vault and on Eve.

## Verification Ladder

Use the smallest relevant checks during implementation, then climb the ladder before completing a stage:

1. Focused pure-function or component tests for the changed behavior.
2. Plugin TypeScript, ESLint, and Svelte diagnostics (`npm run lint` in the current environment, or the repository's pinned pnpm equivalent when available).
3. Production plugin build (`npm run build` or the pinned pnpm equivalent).
4. Quiz-block factory validator tests and direct validation of representative fixtures.
5. Broad existing-corpus validation proving backward compatibility.
6. Manual Obsidian smoke tests for actual editable behavior, focus, themes, check/reveal/reset, persistence, and console errors.
7. `git diff --check`, targeted diff review, repository status review, and commit/tree synchronization checks.

A lower rung cannot substitute for a higher rung when the completion requirement depends on actual Obsidian interaction or real corpus compatibility.

## Stage File Template

```markdown
# [INDEX]-[SHORTHAND]

## Current Facts

- Facts from current code, tests, docs, and previous stage results.

## Updated Assumptions

- Assumptions that still look valid.
- Assumptions that changed.
- Assumptions that need tests before being trusted.

## Big Picture Objective

- Restate the stage objective, adjusted for current facts.

## Detailed Implementation Plan

- Concrete code/doc/test changes for this stage.
- Files expected to change.
- New tests or commands required.

## No-Cheating Checks

- Explicit checks proving the implementation does not route through forbidden fallback paths.

## Completion Requirements

- Requirement-by-requirement checks.
- Required test commands.
- Documentation updates required.

## Stage Results

- Fill in at the end of the stage.
- Include tests run and outcomes.
- Include what was learned.
- Include what should change in `0-plan.md` before the next stage.
```
