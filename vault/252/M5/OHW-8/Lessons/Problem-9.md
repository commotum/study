# Integration by Parts with a Polynomial and Inverse Tangent

## Table of Contents

- [Introduction](#introduction)
- [Choose the Inverse Tangent as \(u\)](#choose-the-inverse-tangent-as-u)
- [Rewrite the Rational Remainder](#rewrite-the-rational-remainder)
- [Complete the Pattern](#complete-the-pattern)
- [Evaluate Problem 9](#evaluate-problem-9)
- [Summary](#summary)

## Prerequisites

- Use the integration-by-parts formula $\int u\,dv=uv-\int v\,du$.
- Differentiate $\tan^{-1}(x)$ as $\dfrac{1}{1+x^2}$.
- Integrate powers of $x$ and recognize $\int \dfrac{1}{1+x^2}\,dx=\tan^{-1}(x)+C$.

---

<a id="introduction"></a>
## Introduction

A product of a polynomial and an inverse trigonometric function is a cue to try integration by parts. For an integral of the form

$$
\int kx\tan^{-1}(x)\,dx,
$$

choose the inverse tangent as $u$ because it is easy to differentiate, and put the polynomial factor in $dv$ because it is easy to integrate:

$$
u=\tan^{-1}(x),
\qquad
dv=kx\,dx.
$$

This choice passes the key test for integration by parts: the new integral is simpler than the original one.

After integration by parts, the remaining rational expression is not integrated by a new method. Rewrite it as a difference whose terms have immediate antiderivatives.

---

<a id="choose-the-inverse-tangent-as-u"></a>
## Choose the Inverse Tangent as \(u\)

**Example:** Set up integration by parts for $\displaystyle\int 6x\tan^{-1}(x)\,dx$.

**Explanation**

Differentiating $\tan^{-1}(x)$ makes it rational, while integrating $6x$ raises its power:

$$
\begin{aligned}
u&=\tan^{-1}(x),
&
du&=\frac{1}{1+x^2}\,dx,\\
dv&=6x\,dx,
&
v&=3x^2.
\end{aligned}
$$

Substitute these pieces into $\int u\,dv=uv-\int v\,du$:

$$
\int 6x\tan^{-1}(x)\,dx
=3x^2\tan^{-1}(x)-3\int\frac{x^2}{1+x^2}\,dx.
$$

The choice matters: assigning $dv=\tan^{-1}(x)\,dx$ would require finding the very kind of antiderivative the method is meant to produce.

```quiz
type: radio
id: p9-choose-parts
content: |-
  Which assignment is most useful for evaluating $\displaystyle\int 8x\tan^{-1}(x)\,dx$ by parts?
options:
- id: a
  content: |-
    $u=\tan^{-1}(x)$, $du=\dfrac{1}{1+x^2}\,dx$, $dv=8x\,dx$, and $v=4x^2$
  correct: true
- id: b
  content: |-
    $u=8x$, $du=8\,dx$, $dv=\tan^{-1}(x)\,dx$, and $v=\dfrac{1}{1+x^2}$
- id: c
  content: |-
    $u=\tan^{-1}(x)$, $du=\dfrac{1}{1-x^2}\,dx$, $dv=8x\,dx$, and $v=4x^2$
- id: d
  content: |-
    $u=\tan^{-1}(x)$, $du=\dfrac{1}{1+x^2}\,dx$, $dv=8x\,dx$, and $v=8x^2$
- id: e
  content: |-
    $u=x\tan^{-1}(x)$, $du=\dfrac{1}{1+x^2}\,dx$, $dv=8\,dx$, and $v=8x$
```

---

<a id="rewrite-the-rational-remainder"></a>
## Rewrite the Rational Remainder

**Example:** Evaluate the remainder $\displaystyle\int\dfrac{x^2}{1+x^2}\,dx$.

**Explanation**

The numerator is one less than the denominator:

$$
x^2=(1+x^2)-1.
$$

Therefore,

$$
\frac{x^2}{1+x^2}
=\frac{1+x^2}{1+x^2}-\frac{1}{1+x^2}
=1-\frac{1}{1+x^2}.
$$

Now integrate term by term:

$$
\int\frac{x^2}{1+x^2}\,dx
=\int\left(1-\frac{1}{1+x^2}\right)\,dx
=x-\tan^{-1}(x)+C.
$$

```quiz
type: radio
id: p9-rewrite-remainder
content: |-
  Which rewrite makes $\displaystyle\int\dfrac{x^2}{1+x^2}\,dx$ immediate?
options:
- id: a
  content: |-
    $\dfrac{x^2}{1+x^2}=1-\dfrac{1}{1+x^2}$
  correct: true
- id: b
  content: |-
    $\dfrac{x^2}{1+x^2}=1+\dfrac{1}{1+x^2}$
- id: c
  content: |-
    $\dfrac{x^2}{1+x^2}=x-\dfrac{1}{1+x^2}$
- id: d
  content: |-
    $\dfrac{x^2}{1+x^2}=\dfrac{x}{1+x}$
- id: e
  content: |-
    $\dfrac{x^2}{1+x^2}=x^2-1$
```

The same rewrite handles a constant multiple without changing the idea:

$$
\int\frac{3x^2}{1+x^2}\,dx
=3\int\left(1-\frac{1}{1+x^2}\right)\,dx
=3x-3\tan^{-1}(x)+C.
$$

```quiz
type: radio
id: p9-integrate-remainder
content: |-
  Evaluate $\displaystyle\int\dfrac{4x^2}{1+x^2}\,dx$.
options:
- id: a
  content: |-
    $4x-4\tan^{-1}(x)+C$
  correct: true
- id: b
  content: |-
    $4x+4\tan^{-1}(x)+C$
- id: c
  content: |-
    $x-4\tan^{-1}(x)+C$
- id: d
  content: |-
    $4\tan^{-1}(x)+C$
- id: e
  content: |-
    $4x-\tan^{-1}(x)+C$
```

---

<a id="complete-the-pattern"></a>
## Complete the Pattern

**Example:** Evaluate $\displaystyle\int 6x\tan^{-1}(x)\,dx$.

**Explanation**

The integration-by-parts setup from the first section gives

$$
\int 6x\tan^{-1}(x)\,dx
=3x^2\tan^{-1}(x)-3\int\frac{x^2}{1+x^2}\,dx.
$$

Insert the rewritten remainder:

$$
\begin{aligned}
\int 6x\tan^{-1}(x)\,dx
&=3x^2\tan^{-1}(x)-3\left(x-\tan^{-1}(x)\right)+C\\
&=3x^2\tan^{-1}(x)-3x+3\tan^{-1}(x)+C\\
&=3\left((x^2+1)\tan^{-1}(x)-x\right)+C.
\end{aligned}
$$

The extra $+3\tan^{-1}(x)$ comes from distributing the negative sign across $x-\tan^{-1}(x)$.

```quiz
type: radio
id: p9-complete-pattern
content: |-
  Evaluate $\displaystyle\int 10x\tan^{-1}(x)\,dx$.
options:
- id: a
  content: |-
    $5\left((x^2+1)\tan^{-1}(x)-x\right)+C$
  correct: true
- id: b
  content: |-
    $5x^2\tan^{-1}(x)-5x+C$
- id: c
  content: |-
    $5\left((x^2+1)\tan^{-1}(x)+x\right)+C$
- id: d
  content: |-
    $10\left((x^2+1)\tan^{-1}(x)-x\right)+C$
- id: e
  content: |-
    $5x^2\tan^{-1}(x)-5\tan^{-1}(x)+C$
```

---

<a id="evaluate-problem-9"></a>
## Evaluate Problem 9

**Example:** Evaluate $\displaystyle\int 15x\tan^{-1}(x)\,dx$.

**Explanation**

Choose

$$
\begin{aligned}
u&=\tan^{-1}(x),
&
du&=\frac{1}{1+x^2}\,dx,\\
dv&=15x\,dx,
&
v&=\frac{15}{2}x^2.
\end{aligned}
$$

Apply integration by parts, then use $\dfrac{x^2}{1+x^2}=1-\dfrac{1}{1+x^2}$:

$$
\begin{aligned}
\int 15x\tan^{-1}(x)\,dx
&=\frac{15}{2}x^2\tan^{-1}(x)-\frac{15}{2}\int\frac{x^2}{1+x^2}\,dx\\
&=\frac{15}{2}x^2\tan^{-1}(x)-\frac{15}{2}\left(x-\tan^{-1}(x)\right)+C\\
&=\frac{15}{2}\left((x^2+1)\tan^{-1}(x)-x\right)+C.
\end{aligned}
$$

This answer is exact. Differentiating it makes the cancellation visible:

$$
\begin{aligned}
\frac{d}{dx}\left[
\frac{15}{2}\left((x^2+1)\tan^{-1}(x)-x\right)
\right]
&=\frac{15}{2}\left(
2x\tan^{-1}(x)+\frac{x^2+1}{1+x^2}-1
\right)\\
&=\frac{15}{2}\left(2x\tan^{-1}(x)+1-1\right)\\
&=15x\tan^{-1}(x).
\end{aligned}
$$

```quiz
type: radio
id: p9-final-check
content: |-
  Which is an exact antiderivative of $15x\tan^{-1}(x)$?
options:
- id: a
  content: |-
    $\dfrac{15}{2}\left((x^2+1)\tan^{-1}(x)-x\right)+C$
  correct: true
- id: b
  content: |-
    $\dfrac{15}{2}\left(x^2\tan^{-1}(x)-x\right)+C$
- id: c
  content: |-
    $\dfrac{15}{2}\left((x^2+1)\tan^{-1}(x)+x\right)+C$
- id: d
  content: |-
    $15\left((x^2+1)\tan^{-1}(x)-x\right)+C$
- id: e
  content: |-
    $\dfrac{15}{2}\left((x^2-1)\tan^{-1}(x)-x\right)+C$
```

---

<a id="summary"></a>
## Summary

For $\displaystyle\int kx\tan^{-1}(x)\,dx$:

1. Choose $u=\tan^{-1}(x)$ and $dv=kx\,dx$.
2. Use $du=\dfrac{1}{1+x^2}\,dx$ and $v=\dfrac{k}{2}x^2$.
3. Rewrite $\dfrac{x^2}{1+x^2}=1-\dfrac{1}{1+x^2}$.
4. Distribute the subtraction carefully; it creates a positive inverse-tangent term.

The reusable result is

$$
\int kx\tan^{-1}(x)\,dx
=\frac{k}{2}\left((x^2+1)\tan^{-1}(x)-x\right)+C.
$$
