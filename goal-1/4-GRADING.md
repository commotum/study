# 4-GRADING

## Current Facts

- Math mode stores MathLive's ASCIIMath serialization in the existing `answers: string[]` state.
- MathLive serializes a typed visual `2/3` as `(2)/(3)`, a mixed number as `1 (1)/(2)`, and typed `sqrt(x+1)` as `sqrt((x+1))` because the `sqrt` inline shortcut creates the root before the literal parentheses are entered.
- Expected author source remains keyboard-friendly: `2/3`, `1 1/2`, `sqrt(x+1)`, `2pi/5`, and similar forms.
- The current text comparator cannot grade those canonical editor strings correctly.
- Text mode must retain its existing trimmed, case-insensitive comparator exactly.
- Full symbolic equivalence remains explicitly excluded.

## Updated Assumptions

- A symmetric canonicalizer must parse both author source and editor output into the same structural representation; raw string cleanup alone is insufficient for fractions and grouping.
- The canonicalizer should be pure and independent of DOM/Mathfield instances so it is fast and unit-testable.
- MathLive's conversion functions are useful token/notation normalizers, but their ASCIIMath output still needs a small structural parser or equivalent representation to distinguish grouping from precedence without collisions.
- Vitest is the smallest appropriate test runner for TypeScript table tests and can later support component tests if needed.

## Big Picture Objective

Implement and prove deterministic structural exact matching for math blanks while preserving reveal-only, feedback, reset, and saved-state behavior and never claiming symbolic equivalence.

## Detailed Implementation Plan

- Inventory the complete 408-answer Mathematical Foundations registry against MathLive conversion functions and identify parse failures or ambiguous constructs.
- Implement a bounded ASCIIMath expression tokenizer/parser for the authoring subset, or adopt a smaller verified structural representation if evidence shows it is safer.
- Canonicalize expected and actual inputs symmetrically into a tagged tree/key that preserves operators, grouping where meaningful, signs, symbols, functions, scripts, relations, and mixed-number separation.
- Treat serializer-only wrapper parentheses around fraction operands and redundant parentheses directly inside `sqrt(...)` as presentation noise only where proven safe.
- Do not evaluate, simplify, reorder, cancel, expand, factor, solve, or approximate.
- Return a non-match for empty or unparseable input rather than guessing.
- Route `QuizPrompt.svelte` to the math comparator only in math mode; retain the current text comparator unchanged.
- Add exact table tests for every Stage 1 accepted/rejected pair plus corpus-critical implicit products, mixed numbers, negative roots/fractions, equations, and relations.
- Add tests for saved canonical editor strings, old keyboard strings, multiple blank arrays, reset normalization, and reveal-only neutrality where feasible at the pure-state layer.
- Run the canonicalizer against all 408 unique Mathematical Foundations answers and report coverage/failures.

## No-Cheating Checks

- Tests must reject `4/6` for expected `2/3`, `0.5` for `1/2`, expansions, factorizations, reordered sums, and case changes.
- Do not use numeric evaluation or computer-algebra equality as the comparator.
- Do not special-case individual question IDs or expected answer literals.
- Do not change text-mode comparison semantics.
- Do not call unparseable or empty input correct.
- Corpus coverage means every unique answer obtains a stable key, not merely that the script exits.

## Completion Requirements

- [ ] Symmetric structural canonicalization is isolated and documented.
- [ ] Every accepted/rejected contract pair has an executable test.
- [ ] All 408 unique Mathematical Foundations answers canonicalize successfully or every exception is resolved explicitly.
- [ ] Math mode uses the structural comparator; text mode retains legacy comparison.
- [ ] Empty/malformed input safely fails.
- [ ] Saved keyboard and canonical editor strings restore/compare safely.
- [ ] Reveal-only and feedback behavior remain unchanged.
- [ ] Focused tests, lint, production/prototype builds, and diff checks pass.

## Stage Results

- In progress.
