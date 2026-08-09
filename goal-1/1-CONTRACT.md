# 1-CONTRACT

## Current Facts

- The implementation source is `/Users/jake/Developer/obsidian-quiz-blocks`, clean on `master` at `cea53b0` after fetching `origin` on 2026-08-08.
- `QuizBlankSchema` is strict. Its current blank-only fields are `require_exact` and `feedback`.
- `QuizPrompt.svelte` has two rendering paths—ordinary Markdown and display-math rows—and both currently use native text inputs.
- Blank saved state is `{ type: "blank", answers: string[], checked: boolean }`.
- Text-mode exact grading trims and compares case-insensitively.
- The Mathematical Foundations corpus has 622 exact blank blocks, 774 markers, 143 multi-blank blocks, and 408 unique answers. It includes fractions, powers, roots, implicit products, pi, mixed numbers, equations, and relation symbols.
- The full vault has 1,007 blank blocks, 1,231 markers, 16 explicit reveal-only blocks, 165 feedback-bearing blocks, 197 multi-blank blocks, and 2 display-math blank layouts.
- MathLive `0.110.0` is the current npm release, MIT licensed, and 5,748,726 bytes unpacked. First-party documentation exposes editable math fields, `input`/`change` events, `value`, ASCIIMath/LaTeX conversion, disabled/read-only states, physical and virtual keyboard input, selection, commands, and accessibility behavior.

## Updated Assumptions

- **Confirmed:** One block-level opt-in is sufficient for the current corpus. Existing blocks can remain text mode; no mass migration is required for compatibility.
- **Confirmed:** `input_mode` is the clearest extensible field name. Its allowed values will be `text` and `math`, and it defaults to `text`.
- **Confirmed:** Math mode is a visual-entry mode, not a promise of computer-algebra equivalence.
- **Confirmed:** The existing `string[]` persistence shape can remain. Math-mode entries will be stored as normalized ASCIIMath strings so they remain portable, inspectable, and convertible back to structured display.
- **To prove in Stage 2:** MathLive's physical-keyboard behavior for every corpus-critical form, especially `sqrt(x)`, implicit products such as `2sqrt(5)`, mixed numbers such as `1 1/2`, Tab/Enter, and paste.
- **To prove in Stage 2:** Import/registration is idempotent under Obsidian plugin reload, generated CSS/fonts work offline, and production bundle impact is acceptable.
- **To prove in Stage 4:** The exact output of the ASCIIMath → MathLive → ASCIIMath round trip for the complete comparison matrix.

## Big Picture Objective

Define a backward-compatible authoring, interaction, persistence, and grading contract for a real opt-in visual math editor before writing production code.

## Detailed Implementation Plan

### Authoring Contract

The finalized field is block-level `input_mode`:

```yaml
type: blank
input_mode: math
require_exact: true
content: |-
  Enter the reduced fraction: ==2/3==
feedback: |-
  Divide the numerator and denominator by their greatest common factor.
```

- `input_mode` is optional and accepts only `text` or `math`.
- Omitted `input_mode` is identical to `input_mode: text` and preserves the current native text control and grading behavior.
- `input_mode` is legal only for `type: blank`; strict schemas and validators reject it elsewhere.
- The setting applies to every `==...==` marker in that block. Mixed text and math editors within one block are not part of this contract.
- `==...==` continues to contain the literal keyboard-friendly answer. In math mode that source uses the existing ASCIIMath-like convention: `2/3`, `sqrt(x+1)`, `x^2`, `2pi/5`, or `2sqrt(5)`. Authors are not required to write LaTeX.
- Math-mode exact answers must not include Markdown math delimiters such as `$...$` or raw display markup. Reveal-only legacy blocks may retain display markup in text mode; a math-mode reveal block uses keyboard math source so the expected result can be rendered by the editor engine.
- Existing blank IDs, content Markdown, `require_exact`, and root-level `feedback` remain unchanged.

### Interaction Contract

- A math blank is an actual editable visual math field. The field itself must restructure `/`, `^`, `_`, grouping, common functions, and shortcuts into typeset math while preserving caret movement, selection, deletion, undo/redo, and correction.
- Each field receives the existing `Blank N` accessible label and participates in document Tab order.
- Check remains disabled until every blank has a nonempty normalized value.
- After Check, fields become disabled and non-focusable. Reset clears every value, reenables the editors, removes grading state, and preserves existing reset callbacks.
- Multiple blank instances have independent state. Inline and display-math layouts use the same editor component.
- The plugin must work offline; no CDN or runtime network fetch is allowed.
- A virtual keyboard may remain available according to MathLive's default device policy, but physical keyboard entry is mandatory.

### Persistence Contract

- The saved-state schema remains version 1 and retains `answers: string[]`.
- Text mode continues storing the literal typed text exactly as it does now.
- Math mode stores the editor value serialized as normalized ASCIIMath, not DOM, MathJSON objects, or opaque editor state.
- On restoration, the saved ASCIIMath string is converted to LaTeX and assigned to the visual field.
- An old plain string restored into a newly math-enabled block is treated as keyboard math source. Failure to parse must leave an editable visible value or a recoverable empty field; it must not throw or corrupt the quiz store.
- Checked state, answer count normalization, and reset continue to use the existing persistence callbacks.

### Exact Grading Contract

- Text mode keeps the existing trimmed, case-insensitive comparison with no behavior change.
- Math mode performs **structural exact matching after deterministic serialization**, not symbolic equivalence.
- The expected `==...==` source and student answer are each normalized through the same supported conversion pipeline. The target pipeline is ASCIIMath → MathLive LaTeX parse/serialization → ASCIIMath; Stage 2/4 must confirm or adjust the precise functions while retaining symmetry.
- Normalization may remove presentation-only whitespace and serializer noise. It must not simplify arithmetic, cancel factors, reorder terms, expand/factor expressions, infer units, or solve equations.
- Empty or syntactically invalid input is never correct.
- Case remains significant for mathematical symbols (`x` and `X` are different).

### Comparison Matrix

The following is the required behavioral contract. Stage 4 must encode it as table-driven tests and record any MathLive serializer behavior that requires an explicit normalization rule.

| Expected source | Student structure/source | Result | Reason |
| --- | --- | --- | --- |
| `2/3` | visual fraction `2` over `3` | Accept | Same parsed structure |
| `sqrt(x+1)` | visual square root of `x+1` | Accept | Same parsed structure |
| `x^2` | visual `x` squared | Accept | Same parsed structure |
| `x_1` | visual `x` subscript `1` | Accept | Same parsed structure |
| `2pi/5` | visual fraction with `2π` over `5` | Accept | Same parsed structure |
| `2sqrt(5)` | visual `2√5` | Accept | Same parsed structure |
| `1 1/2` | visual mixed number `1 1/2` | Accept | Corpus-critical keyboard form; prototype must prove entry |
| `-sqrt(2)/2` | matching signed visual fraction | Accept | Same sign and structure |
| `x^2 + y^2` | same terms with presentation whitespace differences | Accept | Presentation whitespace is ignored |
| `2/3` | `4/6` | Reject | Mathematically equal but structurally different |
| `1/2` | `0.5` | Reject | Numerically equal but structurally different |
| `x+x` | `2x` | Reject | Algebraic simplification is not performed |
| `(x+1)^2` | `x^2+2x+1` | Reject | Expansion is not performed |
| `2*x` | `2x` | Reject unless the common serializer produces the same explicit structure for both | Multiplication normalization must be measured and documented, not guessed |
| `sqrt(x^2)` | `x` | Reject | Domain-dependent simplification is not performed |
| `pi` | `3.14159` | Reject | Approximation is not exact structure |
| `x` | `X` | Reject | Mathematical symbol case is significant |
| `-x` | `0-x` | Reject | Different structure |
| `x+1` | `(x+1)` | Reject unless the common serializer removes only redundant outer grouping | Any grouping normalization must be symmetric and documented |
| `2/3` | empty or incomplete fraction | Reject | Empty/invalid input cannot pass |

### Reveal and Feedback Contract

- `require_exact: false` remains reveal-only. The entered math field stays neutral after Check; no correct/wrong input styling or result badge is shown.
- In math mode, the expected keyboard source is converted to polished typeset math for reveal.
- Root-level `feedback` is rendered after Check exactly as it is today in both exact and reveal-only modes.
- Feedback remains Markdown and may contain Obsidian-rendered LaTeX independently of the editor's stored value.

### Dependency Acceptance Criteria

MathLive `0.110.0` is the first prototype candidate and must be pinned exactly if accepted.

- License is MIT and must remain documented in the dependency lockfile/package metadata.
- All runtime code, CSS, and fonts are bundled or loaded locally; no CDN request is allowed.
- Import/custom-element registration is safe across plugin reloads and multiple quiz blocks. No duplicate-registration exception or global mutation may break other plugins.
- Svelte 5 can create and destroy multiple fields without leaked listeners, detached DOM, or cross-instance state.
- `input`, value read/write, ASCIIMath export, disabled state, accessible label, focus, Tab, Enter, paste, undo, caret, and selection behavior must be demonstrated.
- The production build must succeed and record baseline/new `main.js`, CSS, font/assets, raw bytes, and gzip bytes. A large increase requires explicit review and a bounded alternative comparison; build success alone is insufficient.
- The test vault must open and edit at least one ordinary math blank, one display-math blank, and one two-blank quiz without console errors.
- Light/dark theme styling must be readable and use scoped selectors/parts rather than broad global overrides.
- First-party sources used for the decision:
  - <https://github.com/arnog/mathlive>
  - <https://mathlive.io/mathfield/api/>
  - <https://mathlive.io/mathfield/reference/keybindings/>
  - <https://mathlive.io/mathfield/guides/virtual-keyboard/>
  - <https://mathlive.io/mathfield/guides/fill-in-the-blank/>

## No-Cheating Checks

- The opt-in field defaults to the legacy text path; no heuristic auto-detection may silently switch existing blocks.
- The editable control itself must be visually structured. A static preview beside a native input fails the contract.
- Comparison tests must include mathematically equivalent but structurally different rejected pairs.
- The implementation and docs must use “structural exact matching” and must not advertise symbolic equivalence.
- Expected answers remain keyboard-friendly and LaTeX-free in exact math mode.
- Corpus compatibility is measured by validating unchanged existing files, not by rewriting them until tests pass.

## Completion Requirements

- [x] Authoring syntax is finalized as optional `input_mode: text | math`, default `text`.
- [x] Interaction, persistence, exact grading, reveal-only, feedback, accessibility, and mixed-layout behavior are specified.
- [x] Accepted and rejected examples cover whitespace, case, grouping, fractions, multiplication, signs, decimals, constants, functions, invalid input, and non-equivalent structure.
- [x] Symbolic equivalence is explicitly excluded from this release.
- [x] MathLive `0.110.0` acceptance criteria are measurable and tied to first-party documentation/registry evidence.
- [x] Open questions are bounded Stage 2/4 experiments rather than undefined production behavior.

## Stage Results

- Commands/evidence:
  - `git fetch --prune origin` and status/log inspection: standalone source clean/current at `cea53b0`.
  - Read-only corpus inventory script over `vault/MA/Mathematical-Foundations`: 622 blocks, 774 markers, 143 multi-blank blocks, 408 unique answers.
  - The same inventory over all `vault/`: 1,007 blocks, 1,231 markers, 16 reveal-only, 165 feedback-bearing, 197 multi-blank, 2 display-math layouts.
  - `npm view mathlive version license dist.unpackedSize dist.tarball`: `0.110.0`, MIT, 5,748,726 unpacked bytes.
  - First-party MathLive API, keyboard, virtual-keyboard, fill-in-the-blank, changelog, and repository documentation reviewed on 2026-08-08.
- Learned: Existing keyboard-answer conventions align well with ASCIIMath, but mixed numbers, implicit multiplication, and redundant grouping need real editor/serializer measurements before grading code is finalized.
- Plan update: Stage 2 must prove keyboard behavior and idempotent Obsidian integration; Stage 4 must convert the comparison matrix into executable tests using the selected symmetric normalization pipeline.
