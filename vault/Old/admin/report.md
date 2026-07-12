# Malformed Markdown/LaTeX Pattern Report

Generated: 2026-05-05

Scope: `203/*/*.md` files from `9.1 - Graphs of Inverse Functions - 756/756.md` onward.

## Summary

The most common malformed patterns were not isolated typos. They were systematic conversion artifacts from source math into Markdown/LaTeX. Most issues fell into a few families: placeholder math tokens, invalid piecewise notation, merged integral commands, nonstandard Fourier notation, and pseudo-annotation syntax.

## Common Patterns

### 1. `[MATH: ...]` Placeholders

Many files contained literal placeholder strings inside inline math, especially in interval, domain, codomain, periodic-extension, and Fourier-series lessons.

Example pattern:

```text
$[MATH: x \in [0,\pi)]$
```

Preferred form:

```text
$x \in [0,\pi)$
```

This was especially common in Fourier and set/function lessons, including interval statements like `$[MATH: [-\pi,\pi)]$`.

### 2. Piecewise Functions Rendered as `vmatrix`

Piecewise definitions were often converted into malformed `\begin{vmatrix}` fragments. These were usually not determinants or absolute values; they were broken cases environments.

Example pattern:

```text
$f(x) = {2^x\begin{vmatrix}x < 0 \\ \sqrt{x + 1}\end{vmatrix}x \ge 0$
```

Preferred form:

```latex
$$
f(x)=
\begin{cases}
2^x, & x < 0, \\
\sqrt{x+1}, & x \ge 0.
\end{cases}
$$
```

This was one of the most frequent malformed patterns in piecewise, continuity, jump discontinuity, point discontinuity, and Fourier extension files.

### 3. Merged Integral Tokens

Many integrals had the integrand merged directly into `\int`, producing invalid commands such as `\intx`, `\inte`, `\intu`, `\intv`, `\int3`, `\int32x`, or `\int12x`.

Example pattern:

```text
\intx^{2}e^{2x}dx
```

Preferred form:

```latex
\int x^{2}e^{2x}\,\textrm{d}x
```

This appeared across antiderivative, substitution, exponential integration, trigonometric integration, and integration by parts lessons.

### 4. Nonstandard Limit Syntax

Limits were often written in a plain-text style using `lim_(...)` and Unicode arrows.

Example pattern:

```text
lim_(x -> 0^+) f(x)
```

or with a Unicode arrow:

```text
lim_(x → 0^+) f(x)
```

Preferred form:

```latex
\lim_{x\to 0^+} f(x)
```

This was common in continuity and chain rule derivations.

### 5. Nonstandard Fourier Summation Notation

Fourier lessons frequently used plain-text summation and approximation notation.

Example pattern:

```text
f(x)∼∑_(n = 1)^(∞) a_n \cos(nx)
```

Preferred form:

```latex
f(x)\sim\sum_{n=1}^{\infty} a_n\cos(nx)
```

This was especially common in the Fourier series lessons from `21.3` onward.

### 6. Pseudo-Underbrace Syntax

Some annotated derivations used conversion artifacts for underbraces.

Example pattern:

```text
x_(⏟)_(u)
```

Preferred form:

```latex
\underbrace{x}_{u}
```

This occurred in derivative and integration-by-parts explanations.

### 7. Scalar Absolute Values as `vmatrix`

A smaller but recurring issue was scalar absolute value in logarithms being represented with `vmatrix`.

Example pattern:

```text
\ln\begin{vmatrix}u\end{vmatrix}
```

Preferred form:

```latex
\ln\left|u\right|
```

These were repaired separately from piecewise `vmatrix` errors, because the intended meaning was absolute value rather than cases.

### 8. Semicolon-Separated Equation Chains Inside Inline Math

Some derivations were compressed into long inline expressions with semicolons and malformed alignment markers.

Example pattern:

```text
$a = b; = c; = d$
```

Preferred form:

```latex
$$
\begin{aligned}
a &= b \\
  &= c \\
  &= d
\end{aligned}
$$
```

This appeared most often in Fourier and continuity explanations.

### 9. Nonstandard Conjugate and Inner Product Notation

Some complex-vector and Fourier inner-product lessons used raw symbols or conversion artifacts.

Example patterns:

```text
z^(―)
⟨f,g⟩
```

Preferred forms:

```latex
\overline{z}
\langle f,g\rangle
```

## Recommended Cleanup Rules

- Replace all `[MATH: ...]` placeholders with normal `$...$` or `$$...$$` LaTeX.
- Use `\begin{cases}...\end{cases}` for piecewise functions.
- Use `\left|...\right|` only for scalar absolute value.
- Write integrals as `\int <integrand>\,\textrm{d}<variable>`.
- Use `\lim_{x\to a}` for limits.
- Use `\sum_{n=1}^{\infty}` for series.
- Use `\sim`, not raw `∼`, inside LaTeX when consistency matters.
- Use `\underbrace{...}_{...}` for annotated factors.
- Keep math delimiters to `$inline$` and `$$display$$`.

## Final Validation From The Repair Pass

The final validation pass over the requested target slice checked:

- No remaining `MA_ANSWER_MISSING` markers.
- `506` quiz blocks found and structurally validated.
- No remaining targeted malformed patterns:
  - `[MATH:]`
  - `\eqalign`
  - `\begin{vmatrix}` / `\end{vmatrix}`
  - merged `\int...` commands
  - `lim_(...)`
  - `∑_(...)`
  - pseudo-underbrace `_(⏟)_(...)`
  - `\(...\)` or `\[...\]` delimiters

## MTH-252 Lesson Audit (2026-07-09)

Scope: the `36` other Markdown lesson files under `vault/252/**/Lessons/`, after excluding the two copies of **Defining Definite Integrals Using Left and Right Riemann Sums** that had already been repaired. Final structural and quiz validation covered all `38` lesson files.

### Findings and Repairs

The audit found rendering defects in `16` lesson copies representing `8` distinct lesson titles:

- **Definite Integrals of Piecewise Functions** (`2` copies)
- **The Area Bounded by a Curve and the X-Axis** (`2` copies)
- **The Average Value of a Function** (`3` copies)
- **Properties of Definite Integrals Involving the Limits of Integration** (`3` copies)
- **Finding the Area Between a Curve and the X-Axis When They Intersect** (`3` copies)
- **The Fundamental Theorem of Calculus** (`1` copy)
- **The Integral as an Accumulation Function** (`1` copy)
- **The Second Fundamental Theorem of Calculus** (`1` copy)

Repairs included:

- Replacing malformed piecewise `vmatrix` fragments with `\begin{cases}...\end{cases}`.
- Removing leaked `[MATH: ...]` placeholder text.
- Replacing pseudo-underbrace syntax such as `dx_(⏟)_(A_1)` with `\underbrace{...}_{A_1}`.
- Replacing AsciiMath-style fractions such as `(1)/(b-a)` with `\frac{1}{b-a}`.
- Repairing malformed antiderivative evaluation bars.
- Replacing semicolon-separated equation chains with valid equality chains.
- Fixing a mismatched `\left.` / `\Bigg\right|` delimiter pair.

Unicode mathematical characters that MathJax supports directly, such as `∫`, `π`, and `Δ`, were not classified as errors unless they participated in a malformed conversion.

### Validation

- `249` quiz blocks passed structural validation with strict IDs.
- All `38` lesson files had balanced inline/display math delimiters, braces, and TeX environments.
- No remaining targeted `[MATH:]`, `lim_(...)`, `∑_(...)`, pseudo-underbrace, `|=`, or semicolon-chain patterns were found.
- Every extracted math span in the `16` repaired lesson copies compiled successfully with XeLaTeX using AMS Math and Unicode Math support.
- `git diff --check` reported no whitespace errors.

### Vault-Wide Propagation

The same repairs were subsequently applied to the `32` corresponding Math Academy lesson copies under `vault/MA`, bringing the repaired total to `48` copies across the vault.

- All `48` copies passed delimiter, brace, and TeX-environment validation.
- Their `318` quiz blocks passed structural validation with strict IDs.
- No targeted malformed conversion patterns remained in any copy.
- Seven lesson titles had identical extracted math across every copy. **The Average Value of a Function** had two legitimate course variants; both variants compiled successfully with XeLaTeX.
- Course-relative links, image paths, and quiz IDs were preserved.

## MTH-253 Lesson Audit (2026-07-09)

Scope: all `37` Markdown lesson files under `vault/253/**/Lessons/`.

### Findings and Repairs

The scan found systematic source-conversion defects in `36` files. The main automated repairs included:

- `345` AsciiMath-style limits such as `lim_(x → ∞)` converted to `\lim_{x\to\infty}`.
- `108` AsciiMath-style sums such as `∑_(n = 1)^(∞)` converted to `\sum_{n=1}^{\infty}`.
- `175` parenthesized fractions such as `(a)/(b)` converted to `\frac{a}{b}`.
- `41` malformed `\lim_\limits{...}` expressions converted to standard limit subscripts.
- Unicode large operators and common symbols normalized to TeX commands where they appeared in repaired expressions.
- Inline integrals, sums, and limits given `\displaystyle` where needed, including quiz content.
- Nonstandard `\gt`, `\lt`, `\ngeq`, and `\nleq` aliases replaced with supported TeX comparisons.
- Repeated `|=` and semicolon-separated equality-chain artifacts normalized.

Manual repairs included:

- Three malformed piecewise-sequence definitions replaced with `\begin{cases}...\end{cases}`.
- Six pseudo-underbrace expressions replaced with `\underbrace{...}_{...}`.
- Malformed `vmatrix` fragments replaced with absolute values, evaluation bars, or ordinary inequalities according to context.
- Two long improper-integral derivations rebuilt as valid aligned display math.

### Validation

- All `3,727` extracted math spans compiled together with XeLaTeX using AMS Math, Unicode Math, and Cancel support, with zero parser errors.
- All `37` files passed delimiter, brace, and TeX-environment validation.
- `223` existing quiz blocks passed structural validation with strict IDs. Pre-existing raw checklist questions were allowed because they are outside quiz fences and were not part of this LaTeX repair.
- No targeted malformed limit, sum, fraction, pseudo-underbrace, `vmatrix`, comparison-alias, or equation-chain patterns remained.
- `git diff --check` reported no whitespace errors.

### Vault-Wide Propagation

The same MTH-253 repairs were applied to `93` matching lesson copies elsewhere in the vault, bringing the validated total to `129` copies across `31` lesson titles.

- All `12,681` extracted math spans across the `129` copies compiled with XeLaTeX with zero parser errors.
- All copies passed targeted-pattern, delimiter, brace, and TeX-environment validation.
- Course-relative links, image paths, quiz IDs, and course-specific question sets were preserved.
- Quiz validation inspected `878` fenced quiz blocks. Three Math Academy copies of **Improper Integrals of the Second Kind** retain a pre-existing radio block with no `correct: true` option; this answer-key issue is unrelated to LaTeX and was not modified.
