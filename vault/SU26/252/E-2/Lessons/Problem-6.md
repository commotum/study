# Splitting Absolute-Value Definite Integrals at Their Roots

## Table of Contents

- [Introduction](#introduction)
- [Use Roots to Partition the Interval](#use-roots-to-partition-the-interval)
- [When the Integrand Is Negative, Then Positive](#when-the-integrand-is-negative-then-positive)
- [When the Integrand Is Positive, Then Negative](#when-the-integrand-is-positive-then-negative)
- [Summary](#summary)

## Prerequisites

- Factor a quadratic polynomial.
- Find the zeros of a product by setting each factor equal to zero.
- Determine the sign of a product from the signs of its factors.

---

<a id="introduction"></a>
## Introduction

An integral of the form

$$
\int_a^b |g(t)|\,dt
$$

must be split wherever an interior root of $g$ can change its sign. On each resulting interval,

$$
|g(t)|=
\begin{cases}
g(t), & g(t)\ge 0,\\
-g(t), & g(t)<0.
\end{cases}
$$

If $c$ is the one interior root in $[a,b]$, first use the additive property

$$
\int_a^b |g(t)|\,dt
=
\int_a^c |g(t)|\,dt
+
\int_c^b |g(t)|\,dt.
$$

Then replace the absolute-value integrand separately on each piece. This construction is complete before any antiderivative is taken.

The reusable procedure is:

1. Find the roots of the expression inside the absolute value.
2. Keep the roots that lie in $[a,b]$ and split at the interior roots.
3. Test the sign of the original expression on each open subinterval.
4. Replace $|g(t)|$ with $g(t)$ on positive pieces and with $-g(t)$ on negative pieces.

A root at an endpoint is already a boundary, so it does not create an extra interval. If the instructions say not to evaluate, stop after rewriting the integral.

---

<a id="use-roots-to-partition-the-interval"></a>
## Use Roots to Partition the Interval

**Example:** Identify the intervals on which the sign must be checked for

$$
\int_{-3}^{2}\left|(x+1)(x-2)\right|\,dx.
$$

**Explanation**

The expression inside the absolute value is zero at

$$
x=-1
\qquad\text{and}\qquad
x=2.
$$

The root $x=-1$ is inside $[-3,2]$, so it splits the interval. The root $x=2$ is already the right endpoint. Therefore, the two sign intervals are

$$
[-3,-1]
\qquad\text{and}\qquad
[-1,2].
$$

The roots locate the boundaries, but they do not by themselves determine whether the expression is positive or negative on either side.

```quiz
type: radio
id: p6-roots
content: |-
  Before removing the absolute value in
  $$
  \int_{-4}^{3}\left|(x+2)(x-3)\right|\,dx,
  $$
  which two intervals must be checked for the sign of $(x+2)(x-3)$?
options:
- id: p6-roots-a
  content: |-
    $[-4,-2]$ and $[-2,3]$
  correct: true
- id: p6-roots-b
  content: |-
    $[-4,2]$ and $[2,3]$
- id: p6-roots-c
  content: |-
    $[-4,0]$ and $[0,3]$
- id: p6-roots-d
  content: |-
    $[-4,3]$ only
- id: p6-roots-e
  content: |-
    $[-4,-3]$ and $[-3,3]$
```

---

<a id="when-the-integrand-is-negative-then-positive"></a>
## When the Integrand Is Negative, Then Positive

**Example:** Rewrite Problem 6(a) as a sum of two integrals with no absolute values. Do not evaluate:

$$
\int_{-2}^3\left|t^2+t-2\right|\,dt.
$$

**Explanation**

First factor the expression:

$$
t^2+t-2=(t+2)(t-1).
$$

Its roots are $t=-2$ and $t=1$. The root $-2$ is the left endpoint, while $1$ splits the interval into $[-2,1]$ and $[1,3]$.

Using $t=0$ and $t=2$ as test values gives this sign table:

|  | $(-2,1)$ | $(1,3)$ |
| --- | :---: | :---: |
| $t+2$ | $+$ | $+$ |
| $t-1$ | $-$ | $+$ |
| $(t+2)(t-1)$ | $-$ | $+$ |

Thus the absolute value negates the first piece and leaves the second piece unchanged:

$$
\boxed{
\int_{-2}^{1}-(t^2+t-2)\,dt
+
\int_{1}^{3}(t^2+t-2)\,dt
}.
$$

```quiz
type: radio
id: p6-negative-positive
content: |-
  Rewrite the integral with no absolute values. Do not evaluate.
  $$
  \int_{-1}^{4}\left|x^2-2x-3\right|\,dx
  $$
options:
- id: p6-negative-positive-a
  content: |-
    $\displaystyle \int_{-1}^{3}-(x^2-2x-3)\,dx+\int_{3}^{4}(x^2-2x-3)\,dx$
  correct: true
- id: p6-negative-positive-b
  content: |-
    $\displaystyle \int_{-1}^{3}(x^2-2x-3)\,dx+\int_{3}^{4}-(x^2-2x-3)\,dx$
- id: p6-negative-positive-c
  content: |-
    $\displaystyle \int_{-1}^{3}(x^2-2x-3)\,dx+\int_{3}^{4}(x^2-2x-3)\,dx$
- id: p6-negative-positive-d
  content: |-
    $\displaystyle \int_{-1}^{0}-(x^2-2x-3)\,dx+\int_{0}^{4}(x^2-2x-3)\,dx$
- id: p6-negative-positive-e
  content: |-
    $\displaystyle \int_{-1}^{3}(-x^2-2x-3)\,dx+\int_{3}^{4}(x^2-2x-3)\,dx$
```

---

<a id="when-the-integrand-is-positive-then-negative"></a>
## When the Integrand Is Positive, Then Negative

**Example:** Rewrite Problem 6(b) as a sum of two integrals with no absolute values. Do not evaluate:

$$
\int_{-2}^2\left|(t-2)(t+1)\right|\,dt.
$$

**Explanation**

The integrand is already factored. Its roots are $t=-1$ and $t=2$. The interior root $-1$ divides the given interval into $[-2,-1]$ and $[-1,2]$; the endpoint root $2$ creates no additional piece.

Using $t=-\frac32$ and $t=0$ as test values gives:

|  | $(-2,-1)$ | $(-1,2)$ |
| --- | :---: | :---: |
| $t-2$ | $-$ | $-$ |
| $t+1$ | $-$ | $+$ |
| $(t-2)(t+1)$ | $+$ | $-$ |

This time the first piece stays unchanged and the second piece is negated:

$$
\boxed{
\int_{-2}^{-1}(t-2)(t+1)\,dt
+
\int_{-1}^{2}-(t-2)(t+1)\,dt
}.
$$

```quiz
type: radio
id: p6-positive-negative
content: |-
  Rewrite the integral with no absolute values. Do not evaluate.
  $$
  \int_{-4}^{1}\left|(x+3)(x-1)\right|\,dx
  $$
options:
- id: p6-positive-negative-a
  content: |-
    $\displaystyle \int_{-4}^{-3}(x+3)(x-1)\,dx+\int_{-3}^{1}-(x+3)(x-1)\,dx$
  correct: true
- id: p6-positive-negative-b
  content: |-
    $\displaystyle \int_{-4}^{-3}-(x+3)(x-1)\,dx+\int_{-3}^{1}(x+3)(x-1)\,dx$
- id: p6-positive-negative-c
  content: |-
    $\displaystyle \int_{-4}^{-3}(x+3)(x-1)\,dx+\int_{-3}^{1}(x+3)(x-1)\,dx$
- id: p6-positive-negative-d
  content: |-
    $\displaystyle \int_{-4}^{0}(x+3)(x-1)\,dx+\int_{0}^{1}-(x+3)(x-1)\,dx$
- id: p6-positive-negative-e
  content: |-
    $\displaystyle \int_{-4}^{3}(x+3)(x-1)\,dx+\int_{3}^{1}-(x+3)(x-1)\,dx$
```

---

<a id="summary"></a>
## Summary

For $\int_a^b |g(t)|\,dt$:

1. Find the roots of $g$ in the given interval.
2. Split at roots strictly inside the interval; an endpoint root is already a boundary.
3. Test the sign of $g$ on every resulting open subinterval.
4. Write $g$ where it is positive and $-g$ where it is negative.
5. Join consecutive pieces at the same breakpoint so there are no gaps or overlaps.
6. When negating, negate the entire expression inside the absolute value.
7. Preserve the original outer bounds and stop before evaluating when the problem asks only for a rewrite.

The main trap is assuming the sign order from the roots alone. Roots locate the boundaries; a test value or a factor-sign check decides which pieces need the minus sign.
