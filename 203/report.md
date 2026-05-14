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

