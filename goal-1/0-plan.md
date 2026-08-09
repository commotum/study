# Optional Live Math Editor for Blank Quiz Blocks

Shorthand goal: **MATH-BLANKS**

## Big-Picture Objective

Add an opt-in visual math editor to `type: blank` quiz blocks in the Obsidian Quiz Blocks plugin. In math mode, ordinary keyboard input such as `2/3`, `sqrt(x+1)`, and `x^2` should immediately become structured, typeset mathematics while retaining predictable checking, answer reveal, reset, persistence, accessibility, feedback, and existing Markdown authoring conventions.

The feature must be additive. Existing blank blocks must remain plain-text inputs unless the author explicitly enables math input.

## Non-Negotiable Constraints and No-Cheating Rules

- Work on the existing `master` line; do not require a separate feature branch.
- Preserve the existing behavior of every blank block that does not opt into math input.
- Keep `type: blank`, `==answer==` markers, `require_exact`, and root-level `feedback` as the underlying authoring model.
- Add one explicit block-level math-input setting. The proposed contract is `input_mode: math`, with omitted or `input_mode: text` preserving current behavior; finalize the exact name in Stage 1 before implementation.
- Answers inside `==...==` must remain keyboard-friendly source text. Authors must not be forced to write LaTeX merely to enable visual input.
- A detached preview beside a normal text field does not count as a live visual editor. The editable control itself must support structured visual math entry, caret movement, selection, deletion, and correction.
- Do not claim symbolic equivalence unless the grader actually proves it. Define and document exact grading separately from mathematical equivalence.
- Do not silently weaken `require_exact: true`. If math-mode exact matching uses normalization, that normalization must be deterministic, documented, and tested against explicit accepted and rejected pairs.
- Preserve `require_exact: false` as reveal-only behavior: the input remains neutral and the expected answer is shown after checking.
- Preserve root `feedback` and show it after checking in both text and math modes.
- Do not corrupt or invalidate saved blank-answer state. Existing string-array state must continue to load safely.
- Avoid global web-component or CSS side effects that interfere with Obsidian or other plugins.
- Pin any new dependency and evaluate bundle size, license, maintenance, desktop compatibility, and Obsidian integration before committing to it.
- Update the plugin runtime, documentation, examples, local authoring schema/validator, and tests together. The runtime must not accept a field the authoring tools reject, or vice versa.
- The standalone checkout at `/Users/jake/Developer/obsidian-quiz-blocks` is the implementation source of truth. The study repo submodule follows a tested committed revision.

## Current Facts

- The standalone plugin checkout was fetched on 2026-08-08 and is clean on `master` at `cea53b0`, with `HEAD...origin/master` at `0 0`.
- The study submodule intentionally remains at the prior tested revision `24d59b7` until a new plugin revision passes the final verification stage.
- The plugin uses Svelte 5, TypeScript, Zod, and Vite.
- `src/schemas.ts` defines a strict `QuizBlankSchema` with `type`, shared fields, `require_exact`, and root-level `feedback`.
- `src/ui/QuizPrompt.svelte` finds `==...==` markers and renders native `type="text"` inputs in both ordinary Markdown and display-math layout paths.
- Blank answers are stored as `string[]`; saved blank state contains `answers` and `checked`.
- Current exact checking trims both strings and compares them case-insensitively.
- `require_exact: false` reveals the expected answer without marking the input correct or wrong.
- Root-level blank `feedback` is already rendered after checking.
- The study vault's quiz-block factory schema, validator, tests, and references live under `util/skills/quiz-block-factory/` and currently treat keyboard-friendly `==...==` text as authoritative.
- Math Academy repair/conversion utilities and answer registries under `util/` provide a real corpus of existing exact-match blanks that must remain compatible.
- The Mathematical Foundations corpus contains 622 exact blank blocks, 774 answer markers, 143 multi-blank blocks, and 408 unique keyboard-friendly answers. Representative forms include `2/3`, `x^2`, `sqrt(2)`, `2sqrt(5)`, `2pi/5`, mixed numbers such as `1 1/2`, equations, and relation symbols.
- The full vault contains 1,007 blank blocks and 1,231 answer markers, including 16 explicit reveal-only blocks, 165 blocks with root feedback, 197 multi-blank blocks, and 2 display-math blank layouts.
- MathLive `0.110.0` is the current npm release as of 2026-08-08, is MIT licensed, and has a 5,748,726-byte unpacked package. Its first-party API provides an editable `<math-field>`, per-keystroke `input` events, `value`, ASCIIMath/LaTeX conversion functions, keyboard navigation, disabled/read-only behavior, and accessibility support.
- `npm run lint` currently passes with zero TypeScript, ESLint, or Svelte errors or warnings.

## Stage Status

| Stage | Status | Evidence |
| --- | --- | --- |
| `1-CONTRACT` | Complete | `goal-1/1-CONTRACT.md` |
| `2-PROTOTYPE` | Complete | `goal-1/2-PROTOTYPE.md` |
| `3-COMPONENT` | Complete | `goal-1/3-COMPONENT.md` |
| `4-GRADING` | In progress | `goal-1/4-GRADING.md` |
| `5-AUTHORING` | Pending | — |
| `6-VERIFY-DEPLOY` | Pending | — |

## Assumptions To Verify

- MathLive is the leading candidate because it provides an editable visual math field and keyboard-friendly structured entry; Stage 2 must confirm it works inside Obsidian and Svelte rather than accepting this on reputation alone.
- One block-level input mode is sufficient for the current authoring workflow; mixed text and math blanks within one block are out of scope unless corpus inspection proves they are required.
- Expected answers can continue to be authored in the existing keyboard-friendly form and converted into a canonical comparison representation in math mode.
- Deterministic structural normalization is sufficient for the first release. Full computer-algebra equivalence is not required unless Stage 1 explicitly adds it to the contract.
- Existing persisted answer strings can store either a documented source representation or canonical representation without a persistence schema migration; this must be proven.
- The plugin's present desktop target is acceptable for the first implementation, but keyboard, paste, and focus behavior must still be tested carefully.

## Success Metrics and Final Verification

The original objective is achieved only when all of the following are true:

1. A documented opt-in blank block renders a real visual math editor, while an otherwise identical block without the setting still renders the existing text input.
2. Typing representative keyboard forms such as `2/3`, `sqrt(x+1)`, `x^2`, subscripts, grouping, negatives, decimals, and common constants produces editable structured notation in the input itself.
3. Multiple blanks, display-math blanks, surrounding Markdown, reset, check, disabled state, focus order, and saved-state restoration all work in math mode.
4. `require_exact: true` follows a documented, deterministic comparison contract with unit tests for accepted and rejected cases; it does not pretend to provide unimplemented symbolic equivalence.
5. `require_exact: false` remains reveal-only and root `feedback` remains visible after checking.
6. Existing text-mode blank behavior and existing saved state pass regression tests unchanged.
7. Existing Math Academy quiz blocks require no mass rewrite and the quiz-block factory validator continues to accept the corpus.
8. The runtime Zod schema, README/examples, quiz-block factory JSON schema, validator, validator tests, and authoring references agree on the new field and answer convention.
9. Plugin lint/type/Svelte checks, production build, focused automated tests, authoring-validator tests, corpus validation, `git diff --check`, and manual Obsidian smoke tests pass.
10. The tested plugin revision is committed and pushed, the study submodule points at that revision, and installed build artifacts are refreshed and verified when deployment is part of the stage.

## Indexed Stages

### 1-CONTRACT

#### Big Picture Objective

Define the user-visible authoring and grading contract before selecting implementation details.

#### Detailed Implementation Plan

- Inventory representative Math Academy `type: blank` blocks, including plain prose, inline math, display-math rows, multiple blanks, exact grading, reveal-only grading, and feedback.
- Decide and document the opt-in field. Start from `input_mode: text | math`, defaulting to `text`, and record why the final field name and scope are appropriate.
- Define how keyboard-friendly expected answers inside `==...==` are parsed in math mode.
- Define the stored answer representation and the exact-matching normalization boundary.
- Write an accepted/rejected behavior matrix covering whitespace, case, grouping, fraction syntax, multiplication, signs, decimals, constants, functions, and syntactically invalid input.
- Explicitly decide whether semantic equivalence is excluded, deferred, or included with a real verifier.
- Define expected behavior for `require_exact: false`, feedback, blank counts, reset, disabled fields, persistence, accessibility, and mixed text/math content.
- Record dependency acceptance criteria: license, pinned version, bundle impact, lifecycle, Obsidian compatibility, and whether web components require global registration.

#### Completion Requirements

- The authoring syntax and default behavior are unambiguous and backward-compatible.
- The grading matrix names both accepted and intentionally rejected examples.
- Persistence and reveal-only semantics are specified.
- Dependency acceptance criteria and measurable prototype checks exist.
- Open design questions are resolved or promoted into explicit Stage 2 experiments; implementation does not begin on an undefined contract.

### 2-PROTOTYPE

#### Big Picture Objective

Prove that the chosen visual math editor can satisfy the contract inside this Obsidian/Svelte plugin with acceptable integration cost.

#### Detailed Implementation Plan

- Prototype MathLive first, using a pinned version and the smallest isolated integration possible.
- Test keyboard entry, visual restructuring, caret movement, selection, backspace/delete, paste, focus/blur, Enter/Tab behavior, disabled/read-only behavior, and programmatic value restoration.
- Determine the reliable event and value APIs for Svelte 5 and establish whether values should be stored as keyboard source, LaTeX, or another canonical representation.
- Measure production bundle-size change and inspect emitted assets/CSS.
- Check styling in Obsidian themes and ensure the editor does not inject conflicting globals.
- Exercise at least one ordinary blank, one display-math blank, and two blanks in a single block.
- If MathLive fails a required check, record the failure and evaluate a bounded alternative rather than weakening the objective.

#### Completion Requirements

- A real editable math field works inside the plugin test vault, not just a standalone webpage.
- All required interaction APIs and lifecycle behavior are demonstrated.
- Bundle, licensing, styling, and registration findings are recorded.
- A go/no-go decision names the chosen library and representation with evidence.
- Prototype-only shortcuts are identified and are not mistaken for production completion.

### 3-COMPONENT

#### Big Picture Objective

Build a reusable production math-blank input that cleanly fits both blank-rendering paths.

#### Detailed Implementation Plan

- Add the finalized strict schema field with a backward-compatible default.
- Create a focused Svelte math-input component or action that owns editor initialization, value synchronization, events, focus, disabled state, accessibility labeling, and cleanup.
- Keep plain text inputs on their current path; route only opted-in blank blocks through the math component.
- Integrate the component into both ordinary inline blanks and display-math blank slots without duplicating editor logic.
- Add scoped styling for width, baseline, overflow, correct/wrong states, answer reveal, themes, and responsive layout.
- Preserve multiple-blank indexing and blank-count/check-button behavior.
- Add focused component or DOM tests for initialization, typing events, external state restoration, disabling, and teardown.

#### Completion Requirements

- Text mode is observably unchanged when the new field is absent.
- Math mode uses the reusable editor in every supported blank layout.
- Multiple instances do not share or leak state.
- Focus, labels, disabled state, cleanup, and theme styling are verified.
- Focused automated tests and plugin lint checks pass.

### 4-GRADING

#### Big Picture Objective

Integrate deterministic checking, reveal, reset, and persistence without overstating mathematical equivalence.

#### Detailed Implementation Plan

- Implement the Stage 1 normalization/comparison contract as isolated, testable functions rather than component-local ad hoc replacements.
- Convert keyboard-friendly expected markers and editor values into the chosen comparison representation.
- Add table-driven tests for every accepted/rejected pair in the contract, malformed input, empty values, multiple blanks, and restored saved values.
- Preserve text-mode case-insensitive trimmed matching exactly unless a separately documented correction is required.
- Ensure `require_exact: false` remains neutral and reveals the expected answer in polished math form.
- Ensure feedback, result badge, correct/wrong styling, check-button enablement, reset, and saved-state restoration behave correctly in both modes.
- Verify that old persisted string-array states normalize safely and do not crash math mode or text mode.

#### Completion Requirements

- Exact math grading is deterministic and supported by the complete behavior matrix.
- Tests prove intentionally non-equivalent or merely differently expressed answers are not accidentally accepted beyond the contract.
- Reveal-only mode and feedback behavior match existing semantics.
- Reset and persistence work across reloads and old saved state.
- No test labels structural normalization as symbolic equivalence.

### 5-AUTHORING

#### Big Picture Objective

Make the runtime and the study-vault authoring/validation pipeline agree on the new optional mode.

#### Detailed Implementation Plan

- Update the plugin README, blank field reference, and test-vault examples with text-mode, exact math-mode, and reveal-only math-mode examples.
- Update `util/skills/quiz-block-factory/schemas/quiz-block.schema.json` to accept the new blank-only field and reject it on other quiz types.
- Update the Python validator and its tests for the new field, allowed values, blank-only placement, and keyboard-friendly answer rules.
- Update quiz-block factory references and any cleanup guidance whose typed-input convention needs to distinguish plain text from visual math input.
- Inspect conversion/repair scripts for strict field lists or output templates; change only those that must understand the optional mode.
- Decide whether existing Math Academy blanks should remain text mode by default or whether a separately reviewed subset should opt in. Do not mass-convert merely to demonstrate the feature.

#### Completion Requirements

- Runtime, JSON schema, procedural validator, tests, examples, and reference documentation describe the same field and semantics.
- Existing quiz blocks validate without modification.
- Validator tests cover acceptance on `blank`, rejection elsewhere, invalid values, feedback preservation, and both `require_exact` modes.
- Any proposed corpus conversion is explicit, reviewable, and separate from runtime compatibility.

### 6-VERIFY-DEPLOY

#### Big Picture Objective

Prove the complete feature against the plugin and real study corpus, then synchronize the tested result through the established repository/deployment flow.

#### Detailed Implementation Plan

- Run focused unit/component tests, the full plugin lint/type/Svelte checks, and a production build.
- Run quiz-block factory validator tests and validate representative and broad Math Academy corpus targets, including required-feedback checks where applicable.
- Perform manual Obsidian smoke tests in light and dark themes: keyboard entry, mouse editing, Tab order, multiple blanks, inline/display math, check, reveal, feedback, reset, reload, and malformed input.
- Measure final bundle impact and inspect the production console for errors or duplicate custom-element registration.
- Run `git diff --check`, review the complete diff, and confirm unrelated study-vault changes remain untouched.
- Commit and push the tested standalone plugin revision on `master` as requested.
- Update the study repo submodule to that exact revision and refresh installed plugin artifacts when authorized/in scope.
- Verify GitHub, the standalone checkout, the study submodule, Eve, and installed artifacts identify the intended tested revision or build.

#### Completion Requirements

- Every final success metric has named evidence.
- Plugin checks and build pass; authoring-validator tests and corpus validation pass.
- Manual Obsidian checks cover both the new math path and the legacy text path.
- No unresolved console, lifecycle, styling, persistence, grading, or documentation defects remain hidden behind a green build.
- The tested commit is pushed and all intended copies/deployments are synchronized.
- Any genuinely deferred enhancement, especially symbolic equivalence or mobile support, is documented as future work rather than implied to be complete.
