# 2-PROTOTYPE

## Current Facts

- Stage 1 finalized `input_mode: text | math`, default `text`.
- Math-mode expected answers use keyboard-friendly ASCIIMath-like source and saved math answers remain strings serialized as ASCIIMath.
- Exact grading will compare symmetric normalized structures and explicitly excludes symbolic equivalence.
- MathLive `0.110.0` is the pinned prototype candidate, MIT licensed, with first-party APIs for editable math fields, per-keystroke input, ASCIIMath conversion, disabled state, keyboard navigation, selection, and accessibility.
- The plugin has no automated browser/component test harness yet; current verification is TypeScript/ESLint/Svelte diagnostics plus production build and its Obsidian test vault.
- Baseline production bundle measurements must be captured before adding the dependency.

## Updated Assumptions

- MathLive should be integrated through a focused Svelte component rather than raw `<math-field>` markup duplicated in both prompt paths.
- The prototype may add temporary test-vault examples and focused scripts/tests, but it must not yet route production `type: blank` blocks through math mode until the integration gates pass.
- Importing the package may auto-register its custom element. The prototype must inspect and test actual behavior rather than call `customElements.define()` blindly.
- ASCIIMath round trips should cover most corpus answers; mixed-number and implicit-multiplication behavior remain unproven.

Final updates after prototyping:

- **Confirmed:** MathLive is suitable and will be used at exact version `0.110.0`.
- **Confirmed:** Math-mode state will use MathLive's canonical ASCIIMath serialization. Fractions serialize with explicit grouping, for example `2/3` becomes `(2)/(3)`.
- **Confirmed:** `mathModeSpace = "\\,"` is required so corpus mixed numbers such as `1 1/2` remain separated rather than becoming `11/2`.
- **Confirmed:** Plain-text paste must be intercepted and converted from ASCIIMath to LaTeX before insertion; MathLive's default paste treats `sqrt` as separate letters.
- **Confirmed:** Tab must be intercepted at the host and focus transferred after MathLive's event completes; otherwise MathLive retains the field.
- **Confirmed:** Fonts can be bundled into CSS and `fontsDirectory`/`soundsDirectory` set to `null`, avoiding runtime CDN or vault-root asset requests.

## Big Picture Objective

Prove that MathLive can provide the required editable visual math field in this Svelte/Obsidian plugin with safe lifecycle, keyboard behavior, offline assets, and acceptable build cost.

## Detailed Implementation Plan

- Capture baseline production artifact sizes and gzip sizes at `cea53b0`.
- Add exact dependency `mathlive@0.110.0` with the repository's package manager/lockfile.
- Inspect the installed package exports, element registration behavior, type declarations, CSS/font loading, and SSR-safe conversion entry points.
- Build the smallest focused Svelte prototype component with value initialization, `input` handling, ASCIIMath serialization, disabled state, accessible label, and cleanup.
- Add test-vault examples for ordinary, display-math, and two-blank cases without changing legacy default behavior.
- Add a browser-capable prototype harness or equivalent focused test that types `/`, `^`, `_`, `sqrt`, `pi`, implicit multiplication, mixed numbers, selection/deletion, paste, Tab/Enter, and value restoration.
- Test multiple components and repeated initialization for duplicate custom-element registration or shared-state failures.
- Run plugin lint/build, record new artifact sizes, and inspect all emitted assets for offline behavior.
- Exercise the prototype in the actual Obsidian test vault or, if GUI automation cannot inspect Obsidian, gather the strongest available runtime evidence and carry the missing Obsidian interaction forward explicitly to Stage 6 rather than claiming it occurred.

## No-Cheating Checks

- The prototype must edit structured math inside the control; a native input plus preview is a failure.
- The legacy blank path must remain unchanged during the prototype.
- Tests must use physical-keyboard events for representative source strings, not only assign prebuilt LaTeX programmatically.
- Programmatic conversion tests cannot substitute for caret, selection, deletion, Tab, Enter, paste, and disabled-state checks.
- No CDN or runtime network dependency is allowed.
- A successful build cannot by itself establish runtime lifecycle or keyboard behavior.

## Completion Requirements

- [x] Baseline and MathLive build sizes are recorded.
- [x] A real editable MathLive field runs through a plugin-source Svelte component and browser harness; actual Obsidian hosting is explicitly carried to Stage 6.
- [x] Required event, value, ASCIIMath, disabled, focus, keyboard, paste, selection, and cleanup behavior is demonstrated.
- [x] Ordinary, display-math, and multiple-field cases are exercised without shared value state.
- [x] Dependency registration, license, assets, CSS/fonts, and offline behavior are understood and documented.
- [x] Plugin lint and prototype production build pass.
- [x] The go decision is MathLive `0.110.0` with normalized ASCIIMath string state.
- [x] Actual Obsidian light/dark/runtime smoke testing is explicitly carried into Stage 6.

## Stage Results

- Baseline plugin build at `cea53b0`: `main.js` 276,595 bytes / 87,875 gzip; `styles.css` 13,553 bytes / 2,808 gzip.
- Final prototype bundle: JavaScript 842,396 bytes / 234,822 gzip; CSS with inlined fonts 350,832 bytes / 263,231 gzip.
- The package auto-registers `math-field` only when no existing registration is present. Repeated prototype reloads produced no duplicate-registration application error.
- Browser interaction evidence:
  - Physical `/` entry rendered a stacked fraction and serialized `2/3` as `(2)/(3)`.
  - `x^2`, `x_1`, `2pi/5`, `2sqrt(5)`, and `sqrt(x+1)` became structured visual math.
  - Default spaces caused `1 1/2` to collapse to `11/2`; setting `mathModeSpace` preserved it as `1 (1)/(2)`.
  - Programmatic `sqrt(x+1)` restoration rendered a square root immediately.
  - Plain paste was initially rendered as separate letters; the intercept now pastes `sqrt(x+1)` as one structured root.
  - Select-all + Backspace cleared `x^2`; undo restored it.
  - Disabled fields rejected focus/input; reset reenabled and cleared them.
  - Multiple fields maintained independent values. Deferred Tab focus transfer reached the second field and accepted a physical `Y` key there.
- `npm run lint`: zero TypeScript, ESLint, or Svelte errors/warnings.
- `npm run prototype:build`: passed. All KaTeX font files were inlined into CSS; the prototype has no external font/sound dependency.
- The only console error observed came from the controlling Chrome extension URL, not the prototype origin. Constructor-option warnings found during testing were removed by assigning MathLive properties after construction.
- Actual Obsidian host behavior, light/dark themes, and installed artifact packaging remain required Stage 6 evidence.
