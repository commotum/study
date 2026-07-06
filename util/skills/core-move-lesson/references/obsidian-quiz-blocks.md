# Obsidian Quiz Blocks

The local study vault uses the `quiz-blocks` Obsidian plugin. Final core-move lessons should use fenced `quiz` code blocks for practice.

Source examples:

- `/Users/jake/Developer/study/vault/Old/admin/quiz-test.md`
- `/Users/jake/Developer/study/vault/.obsidian/plugins/quiz-blocks/manifest.json`

## Supported Types

- `radio`: one correct option.
- `checkbox`: multiple correct options.
- `select`: several prompts sharing one top-level option bank.
- `multi-select`: several prompts with separate option banks.
- `noodle`: matching pairs.
- `free`: free text response with optional reference answer.
- `blank`: fill in hidden answers wrapped in `==double equals==`.

For this skill, use `radio` unless another type is clearly better. The validator can validate all supported types, but normal generated practice should pass `--require-radio-practice`.

## Radio Format

```quiz
type: radio
id: q-1
content: |-
  What are the units of $B$ if $\alpha(t)=Bt^2+C$ and $\alpha(t)$ has units $\mathrm{rad}/\mathrm{s}^2$?
options:
- id: a
  content: |-
    $\mathrm{rad}/\mathrm{s}^2$
- id: b
  content: |-
    $\mathrm{rad}/\mathrm{s}^4$
  correct: true
- id: c
  content: |-
    $\mathrm{m}/\mathrm{s}^2$
```

## Other Type Examples

### Checkbox

```quiz
type: checkbox
id: q-checkbox
content: |-
  Which statements are true?
options:
- id: a
  content: |-
    Like terms in a sum must have matching units.
  correct: true
- id: b
  content: |-
    A coefficient always has the same units as the whole term.
```

### Blank

```quiz
type: blank
id: q-blank
require_exact: false
content: |-
  If $[A]\mathrm{s}^2=\mathrm{m}$, then $[A]==\mathrm{m}/\mathrm{s}^2==$.
```

## Formatting Rules

- Fence must open with exactly ```` ```quiz ```` and close with ```` ``` ````.
- Use YAML-style keys.
- Use block scalars for multi-line content:
  - `content: |-`
  - then indent content lines by two spaces.
- For `radio`, include `options`, at least two options, and exactly one `correct: true`.
- For generated core-move lessons, include ids on quiz blocks and options.
- Do not use old aliases: use `free`, not `text`; use `blank`, not `prompt`; use `select`, not `choice`.
