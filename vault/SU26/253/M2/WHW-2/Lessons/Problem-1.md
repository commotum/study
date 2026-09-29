# Writing and Analyzing a Patterned Sequence Formula

## Table of Contents

- [Introduction](#introduction)
- [Encode Each Pattern with the Index](#encode-each-pattern-with-the-index)
- [Check the Formula Against the Given Terms](#check-the-formula-against-the-given-terms)
- [Compare Exponential and Linear Growth](#compare-exponential-and-linear-growth)
- [Use Even and Odd Terms to Describe End Behavior](#use-even-and-odd-terms-to-describe-end-behavior)
- [Summary](#summary)

## Prerequisites

- Evaluate powers with negative bases.
- Write the $n$th term of an arithmetic pattern.
- Interpret convergence as approaching one finite value.

---

<a id="introduction"></a>
## Introduction

When the numerator and denominator of a sequence follow different patterns, encode each pattern separately and then combine them. For

$$
\left\{-\frac{3}{5},\frac{9}{7},-\frac{27}{9},\frac{81}{11},-\frac{243}{13},\ldots\right\},
$$

the recognition cues are:

- the numerator alternates sign while its magnitude is multiplied by $3$;
- the denominator increases by $2$;
- the problem begins with $n=1$.

After finding $a_n$, determine the end behavior by studying both its magnitude and its sign. A sequence converges only if all sufficiently late terms approach the same finite number. A growing magnitude alone is therefore not enough to say the sequence tends to $+\infty$; the signs must eventually point in the same direction too.

---

<a id="encode-each-pattern-with-the-index"></a>
## Encode Each Pattern with the Index

**Example:** Write a formula for the given sequence.

**Explanation**

The numerator sequence is

$$
-3,9,-27,81,-243,\ldots
$$

Each term is obtained by multiplying by $-3$. The two component patterns can be organized as follows:

| Component | First values | Rule at index $n$ |
|---|---|---|
| Numerator | $-3,9,-27,81,\ldots$ | $(-3)^n$ |
| Denominator | $5,7,9,11,\ldots$ | $5+2(n-1)=2n+3$ |

Because the first numerator occurs at $n=1$, its rule is exactly

$$
(-3)^n.
$$

The denominator rule comes from the arithmetic pattern

$$
5,7,9,11,13,\ldots
$$

with first term $5$ and common difference $2$:

$$
5+2(n-1)=2n+3.
$$

Combining the two patterns gives

$$
\boxed{a_n=\frac{(-3)^n}{2n+3}},\qquad n\geq 1.
$$

```quiz
type: radio
id: p1-encode-patterns
content: |-
  Which formula generates the sequence
  $\left\{-\frac{2}{4},\frac{4}{7},-\frac{8}{10},\frac{16}{13},\ldots\right\}$ for $n\geq 1$?
options:
- id: a
  content: |-
    $a_n=\frac{(-2)^n}{3n+1}$
  correct: true
- id: b
  content: |-
    $a_n=\frac{2^n}{3n+1}$
- id: c
  content: |-
    $a_n=\frac{(-2)^{n-1}}{3n+1}$
- id: d
  content: |-
    $a_n=\frac{(-2)^n}{4n}$
- id: e
  content: |-
    $a_n=\frac{(-2)^n}{3n+4}$
```

---

<a id="check-the-formula-against-the-given-terms"></a>
## Check the Formula Against the Given Terms

**Example:** Verify that $a_n=\dfrac{(-3)^n}{2n+3}$ has the correct indexing.

**Explanation**

Use the same quick check for any proposed explicit formula: substitute $n=1$ first, then $n=2$.

$$
a_1=\frac{(-3)^1}{2(1)+3}=-\frac35
$$

and

$$
a_2=\frac{(-3)^2}{2(2)+3}=\frac97.
$$

These agree with the first two given terms. Checking both $n=1$ and $n=2$ catches the two most common mistakes: an exponent shifted by $1$ and a linear denominator with the wrong constant.

```quiz
type: radio
id: p1-check-indexing
content: |-
  A student proposes $b_n=\frac{(-4)^{n-1}}{n+2}$ for a sequence that should begin $-\frac43,4,\ldots$. What does evaluating $b_1$ show?
options:
- id: a
  content: |-
    The exponent is shifted: $b_1=\frac13$, so the formula does not produce the required first term.
  correct: true
- id: b
  content: |-
    The formula is correct because $b_1=-\frac43$.
- id: c
  content: |-
    Only the denominator is wrong because $b_1=-\frac12$.
- id: d
  content: |-
    The formula starts at $n=0$, but $b_1=-4$.
- id: e
  content: |-
    No conclusion can be drawn by checking the first term.
```

---

<a id="compare-exponential-and-linear-growth"></a>
## Compare Exponential and Linear Growth

**Example:** Determine what happens to the magnitude of

$$
a_n=\frac{(-3)^n}{2n+3}.
$$

**Explanation**

Ignore the sign temporarily and take the absolute value:

$$
|a_n|=\frac{3^n}{2n+3}.
$$

The relevant growth hierarchy is

$$
\text{exponential growth}\gg\text{linear growth}.
$$

Since the exponential base $3$ is greater than $1$, the numerator outgrows the denominator. Thus,

$$
\frac{3^n}{2n+3}\longrightarrow\infty.
$$

So the terms do not shrink or settle near a finite number; their distances from $0$ grow without bound.

```quiz
type: radio
id: p1-compare-growth
content: |-
  What happens to the magnitude of $c_n=\frac{(-5)^n}{4n-1}$ as $n\to\infty$?
options:
- id: a
  content: |-
    $|c_n|\to\infty$ because the exponential numerator grows faster than the linear denominator.
  correct: true
- id: b
  content: |-
    $|c_n|\to0$ because every fraction with a growing denominator tends to $0$.
- id: c
  content: |-
    $|c_n|\to\frac54$ by comparing the coefficients $5$ and $4$.
- id: d
  content: |-
    $|c_n|$ alternates between positive and negative values.
- id: e
  content: |-
    $|c_n|\to1$ because numerator and denominator both grow.
```

---

<a id="use-even-and-odd-terms-to-describe-end-behavior"></a>
## Use Even and Odd Terms to Describe End Behavior

**Example:** Determine the end behavior of $a_n=\dfrac{(-3)^n}{2n+3}$.

**Explanation**

The factor $(-3)^n$ is positive for even $n$ and negative for odd $n$. Make this precise by looking at the two subsequences.

For $n=2k$,

$$
a_{2k}=\frac{3^{2k}}{4k+3}\longrightarrow+\infty.
$$

For $n=2k-1$,

$$
a_{2k-1}=-\frac{3^{2k-1}}{4k+1}\longrightarrow-\infty.
$$

The even and odd terms head in opposite directions, so the whole sequence approaches no single value. Therefore,

$$
\boxed{\lim_{n\to\infty}a_n\text{ does not exist, so the sequence diverges.}}
$$

It is incorrect to write $a_n\to+\infty$: only the even terms do that.

```quiz
type: radio
id: p1-end-behavior
content: |-
  Determine the end behavior of $d_n=\frac{(-2)^n}{n+6}$.
options:
- id: a
  content: |-
    The sequence diverges: $d_{2k}\to+\infty$ and $d_{2k-1}\to-\infty$.
  correct: true
- id: b
  content: |-
    The sequence converges to $0$ because the denominator grows.
- id: c
  content: |-
    The sequence tends to $+\infty$ because its magnitude grows.
- id: d
  content: |-
    The sequence tends to $-\infty$ because the first term is negative.
- id: e
  content: |-
    The sequence converges to $-2$ because consecutive numerators have ratio $-2$.
```

---

<a id="summary"></a>
## Summary

For a quotient sequence whose parts have recognizable patterns:

1. Encode the numerator and denominator separately.
2. Combine them and verify $n=1$ and $n=2$ to catch indexing errors.
3. Analyze $|a_n|$ to determine whether the magnitude shrinks, settles, or grows.
4. Track the sign. If even and odd subsequences head toward different values or different infinities, the sequence diverges.

For the assigned sequence,

$$
\boxed{a_n=\frac{(-3)^n}{2n+3}},\qquad
\boxed{a_{2k}\to+\infty,\quad a_{2k-1}\to-\infty}.
$$

Hence the sequence has no limit and diverges.
