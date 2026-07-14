# Finding the Sum of a Telescoping Series

## Table of Contents

- [Introduction](#introduction)
- [Expand Enough Terms to See the Cancellation](#expand-enough-terms-to-see-the-cancellation)
- [Keep the Two Boundary Terms](#keep-the-two-boundary-terms)
- [Take the Limit of the Partial Sums](#take-the-limit-of-the-partial-sums)
- [Track a Shifted Starting Index](#track-a-shifted-starting-index)
- [Summary](#summary)

## Prerequisites

- Substitute integer values into a formula.
- Add and subtract fractions with the same denominator.
- Evaluate limits such as $\displaystyle\lim_{n\to\infty}\frac{1}{n}=0$.

---

<a id="introduction"></a>
## Introduction

The series

$$
\sum_{k=2}^{\infty}\left(\frac{1}{k-1}-\frac{1}{k}\right)
$$

has consecutive terms that cancel. The negative fraction from one term reappears as the positive fraction in the next term. This is the recognition cue for a **telescoping series**.

To analyze it, replace $\infty$ with a finite upper index $n$, expand several terms, cancel the interior terms, and then take the limit of the resulting partial-sum formula.

Here,

$$
s_n=\sum_{k=2}^{n}\left(\frac{1}{k-1}-\frac{1}{k}\right)
$$

uses $n$ as the **last index**. Because the series starts at $k=2$, this partial sum contains $n-1$ terms. Keeping that distinction clear prevents an off-by-one error at the right boundary.

---

<a id="expand-enough-terms-to-see-the-cancellation"></a>
## Expand Enough Terms to See the Cancellation

**Example:** Expand the first four terms of

$$
s_n=\sum_{k=2}^{n}\left(\frac{1}{k-1}-\frac{1}{k}\right).
$$

**Explanation**

Substitute $k=2,3,4,5$:

$$
\left(1-\frac12\right)
+\left(\frac12-\frac13\right)
+\left(\frac13-\frac14\right)
+\left(\frac14-\frac15\right)+\cdots
$$

The pairs $-\frac12+\frac12$, $-\frac13+\frac13$, and $-\frac14+\frac14$ cancel. The same pattern continues through the finite sum.

```quiz
type: radio
id: p5-expand
content: |-
  Which is the correct beginning of
  $\displaystyle\sum_{k=3}^{n}\left(\frac{1}{k-1}-\frac{1}{k}\right)$?
options:
- id: a
  content: |-
    $\left(1-\frac12\right)+\left(\frac12-\frac13\right)+\cdots$
- id: b
  content: |-
    $\left(\frac12-\frac13\right)+\left(\frac13-\frac14\right)+\cdots$
  correct: true
- id: c
  content: |-
    $\left(\frac13-\frac12\right)+\left(\frac14-\frac13\right)+\cdots$
- id: d
  content: |-
    $\left(\frac12-\frac14\right)+\left(\frac13-\frac15\right)+\cdots$
- id: e
  content: |-
    $\left(\frac13-\frac14\right)+\left(\frac14-\frac15\right)+\cdots$
```

---

<a id="keep-the-two-boundary-terms"></a>
## Keep the Two Boundary Terms

**Example:** Find a formula for the $n$th partial sum of the assigned series.

**Explanation**

Write the finite sum with its first terms and its last term visible:

$$
\begin{aligned}
s_n
&=\sum_{k=2}^{n}\left(\frac{1}{k-1}-\frac{1}{k}\right)\\
&=\left(1-\frac12\right)
+\left(\frac12-\frac13\right)
+\cdots
+\left(\frac{1}{n-1}-\frac1n\right).
\end{aligned}
$$

The last displayed pair comes from substituting $k=n$:

$$
\frac{1}{k-1}-\frac1k
\quad\longrightarrow\quad
\frac{1}{n-1}-\frac1n.
$$

Every interior fraction cancels. Only the positive fraction at the left boundary and the negative fraction at the right boundary remain:

$$
\boxed{s_n=1-\frac1n},\qquad n\ge 2.
$$

```quiz
type: radio
id: p5-partial-sum
content: |-
  Find the partial-sum formula for
  $\displaystyle s_n=\sum_{k=4}^{n}\left(\frac{1}{k-1}-\frac{1}{k}\right)$.
options:
- id: a
  content: |-
    $s_n=\frac14-\frac1n$
- id: b
  content: |-
    $s_n=\frac13+\frac1n$
- id: c
  content: |-
    $s_n=\frac13-\frac1n$
  correct: true
- id: d
  content: |-
    $s_n=1-\frac1n$
- id: e
  content: |-
    $s_n=\frac13-\frac{1}{n+1}$
```

```quiz
type: radio
id: p5-boundaries
content: |-
  Before simplifying completely, which two boundary terms survive in
  $\displaystyle\sum_{k=6}^{n}\left(\frac{1}{k-1}-\frac{1}{k}\right)$?
options:
- id: a
  content: |-
    $1$ and $-\frac1n$
- id: b
  content: |-
    $\frac16$ and $-\frac1n$
- id: c
  content: |-
    $\frac15$ and $-\frac1n$
  correct: true
- id: d
  content: |-
    $\frac15$ and $-\frac{1}{n-1}$
- id: e
  content: |-
    $\frac16$ and $-\frac{1}{n+1}$
```

---

<a id="take-the-limit-of-the-partial-sums"></a>
## Take the Limit of the Partial Sums

**Example:** Determine whether the assigned series converges and find its sum if it does.

**Explanation**

An infinite series converges when its sequence of partial sums approaches a finite number. Using the formula above,

$$
\begin{aligned}
\sum_{k=2}^{\infty}\left(\frac{1}{k-1}-\frac{1}{k}\right)
&=\lim_{n\to\infty}s_n\\
&=\lim_{n\to\infty}\left(1-\frac1n\right)\\
&=1-0\\
&=\boxed{1}.
\end{aligned}
$$

The limit is finite, so the series **converges to $1$**.

```quiz
type: radio
id: p5-limit
content: |-
  Determine the behavior and sum of
  $\displaystyle\sum_{k=5}^{\infty}\left(\frac{1}{k-1}-\frac{1}{k}\right)$.
options:
- id: a
  content: |-
    It converges to $\frac15$.
- id: b
  content: |-
    It converges to $\frac14$.
  correct: true
- id: c
  content: |-
    It converges to $1$.
- id: d
  content: |-
    It converges to $0$.
- id: e
  content: |-
    It diverges because it has infinitely many terms.
```

---

<a id="track-a-shifted-starting-index"></a>
## Track a Shifted Starting Index

**Example:** Find the surviving left boundary of

$$
\sum_{k=m}^{n}\left(\frac{1}{k-1}-\frac{1}{k}\right),\qquad m\ge2.
$$

**Explanation**

The first term is

$$
\frac{1}{m-1}-\frac1m,
$$

not $1-\frac1m$ unless $m=2$. After the interior terms cancel, the general boundary rule is

$$
\boxed{\sum_{k=m}^{n}\left(\frac{1}{k-1}-\frac{1}{k}\right)
=\frac{1}{m-1}-\frac1n}.
$$

The main trap is to forget that the lower index determines the first surviving fraction.

```quiz
type: radio
id: p5-shifted-index
content: |-
  Which formula and conclusion are correct for
  $\displaystyle\sum_{k=3}^{\infty}\left(\frac{1}{k-1}-\frac{1}{k}\right)$?
options:
- id: a
  content: |-
    $s_n=1-\frac1n$, so the series converges to $1$.
- id: b
  content: |-
    $s_n=\frac12+\frac1n$, so the series converges to $\frac12$.
- id: c
  content: |-
    $s_n=\frac12-\frac1n$, so the series converges to $\frac12$.
  correct: true
- id: d
  content: |-
    $s_n=\frac13-\frac1n$, so the series converges to $\frac13$.
- id: e
  content: |-
    The series diverges because $s_n$ contains $n$.
```

---

<a id="summary"></a>
## Summary

For a series whose terms have the shifted-difference form

$$
\frac{1}{k-1}-\frac{1}{k},
$$

use this checklist:

1. Replace $\infty$ with $n$ to form $s_n$.
2. Expand the first few terms and the last term.
3. Cancel only the matching interior fractions.
4. Keep the two boundary terms: $\displaystyle s_n=\frac{1}{m-1}-\frac1n$ when the sum starts at $k=m$.
5. Take $\displaystyle\lim_{n\to\infty}s_n$.

Remember that $n$ is the last index, not necessarily the number of terms. Also, do not try to “cancel to infinity”; first derive the finite formula for $s_n$, then take its limit.

For the assigned series, $m=2$, so

$$
\boxed{s_n=1-\frac1n}
\qquad\text{and}\qquad
\boxed{\sum_{k=2}^{\infty}\left(\frac{1}{k-1}-\frac{1}{k}\right)=1}.
$$
