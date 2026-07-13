# Evaluating a Factorial-Over-Self-Power Limit

## Table of Contents

- [Introduction](#introduction)
- [Rewrite the Quotient as Normalized Factors](#rewrite-the-quotient-as-normalized-factors)
- [Keep One Vanishing Factor](#keep-one-vanishing-factor)
- [Handle a Shifted Index](#handle-a-shifted-index)
- [Check That Every Remaining Factor Is Bounded](#check-that-every-remaining-factor-is-bounded)
- [Summary](#summary)

## Prerequisites

- The factorial identity $m!=1\cdot 2\cdots m$
- The fact that $1/m\to 0$ as $m\to\infty$
- The Squeeze Theorem for sequences

---

<a id="introduction"></a>
## Introduction

When a factorial is divided by the same positive integer raised to its own power, expand the quotient into normalized factors. Each factor is at most $1$, and the first factor approaches $0$. That gives an upper bound that the Squeeze Theorem can use.

The key condition is that every factor left after choosing the vanishing factor must stay between $0$ and $1$.

---

<a id="rewrite-the-quotient-as-normalized-factors"></a>
## Rewrite the Quotient as Normalized Factors

**Example:** Rewrite $\dfrac{6!}{6^6}$ as a product of fractions.

**Explanation**

The denominator $6^6$ is a product of six copies of $6$, so pair one copy of $6$ with each factorial factor:

$$
\frac{6!}{6^6}
=\frac{1\cdot2\cdot3\cdot4\cdot5\cdot6}{6\cdot6\cdot6\cdot6\cdot6\cdot6}
=\frac16\cdot\frac26\cdot\frac36\cdot\frac46\cdot\frac56\cdot\frac66.
$$

In general,

$$
\frac{m!}{m^m}=\prod_{k=1}^{m}\frac{k}{m}.
$$

This expansion is essential: $m!$ is a product of changing factors, not another power $m^m$, so the factorial and the power cannot be canceled as though they were like factors.

```quiz
type: radio
id: ohw6-p15-q1
content: |-
  Which product is equal to $\dfrac{7!}{7^7}$?
options:
- id: ohw6-p15-q1-a
  content: |-
    $\displaystyle \prod_{k=1}^{7}\frac{k}{7}$
  correct: true
- id: ohw6-p15-q1-b
  content: |-
    $\displaystyle \prod_{k=1}^{7}\frac{7}{k}$
- id: ohw6-p15-q1-c
  content: |-
    $\displaystyle \prod_{k=1}^{7}\frac{k}{7^7}$
- id: ohw6-p15-q1-d
  content: |-
    $\displaystyle \prod_{k=1}^{6}\frac{k}{7}$
```

---

<a id="keep-one-vanishing-factor"></a>
## Keep One Vanishing Factor

**Example:** Find an upper bound for $\dfrac{m!}{m^m}$ that approaches $0$.

**Explanation**

For $1\le k\le m$, every normalized factor satisfies

$$
0<\frac{k}{m}\le 1.
$$

Keep the first factor $1/m$ and replace every other factor by its upper bound $1$:

$$
0<\frac{m!}{m^m}
=\frac1m\left(\frac2m\cdot\frac3m\cdots\frac{m}{m}\right)
\le \frac1m(1\cdot1\cdots1)
=\frac1m.
$$

The factor $1/m$ is useful because it approaches $0$; merely observing that the whole product is at most $1$ would not determine the limit.

```quiz
type: radio
id: ohw6-p15-q2
content: |-
  Which inequality gives a useful squeeze for $\dfrac{10!}{10^{10}}$ and mirrors the general argument?
options:
- id: ohw6-p15-q2-a
  content: |-
    $\displaystyle 0<\frac{10!}{10^{10}}\le 1$
- id: ohw6-p15-q2-b
  content: |-
    $\displaystyle 0<\frac{10!}{10^{10}}\le \frac1{10}$
  correct: true
- id: ohw6-p15-q2-c
  content: |-
    $\displaystyle \frac{10!}{10^{10}}\ge \frac1{10}$
- id: ohw6-p15-q2-d
  content: |-
    $\displaystyle \frac{10!}{10^{10}}=\frac1{10}$
```

```quiz
type: radio
id: ohw6-p15-q2b
content: |-
  Complete the useful bound: $\displaystyle 0<\frac{m!}{m^m}\le {}$.
options:
- id: ohw6-p15-q2b-a
  content: |-
    $\displaystyle \frac1m$
  correct: true
- id: ohw6-p15-q2b-b
  content: |-
    $m$
- id: ohw6-p15-q2b-c
  content: |-
    $m!$
- id: ohw6-p15-q2b-d
  content: |-
    $\displaystyle \frac{m}{m-1}$
```

---

<a id="handle-a-shifted-index"></a>
## Handle a Shifted Index

**Example:** Evaluate

$$
\lim_{n\to\infty}\frac{(n+1)!}{(n+1)^{n+1}}.
$$

**Explanation**

Set $m=n+1$. As $n\to\infty$, we also have $m\to\infty$. The quotient now has the standard form:

$$
\frac{(n+1)!}{(n+1)^{n+1}}=\frac{m!}{m^m}.
$$

The product bound gives

$$
0<\frac{m!}{m^m}\le\frac1m.
$$

Since $1/m\to0$, the Squeeze Theorem yields

$$
\boxed{\lim_{n\to\infty}\frac{(n+1)!}{(n+1)^{n+1}}=0}.
$$

The shift changes the label of the index, not the argument.

```quiz
type: radio
id: ohw6-p15-q3
content: |-
  Evaluate $\displaystyle \lim_{n\to\infty}\frac{(n+4)!}{(n+4)^{n+4}}$.
options:
- id: ohw6-p15-q3-a
  content: |-
    $0$
  correct: true
- id: ohw6-p15-q3-b
  content: |-
    $1$
- id: ohw6-p15-q3-c
  content: |-
    $4$
- id: ohw6-p15-q3-d
  content: |-
    The limit does not exist.
```

---

<a id="check-that-every-remaining-factor-is-bounded"></a>
## Check That Every Remaining Factor Is Bounded

**Example:** Decide whether the same one-factor bound immediately applies to $\dfrac{m!}{(m+1)^m}$.

**Explanation**

Rewrite the quotient:

$$
\frac{m!}{(m+1)^m}
=\frac1{m+1}\cdot\frac2{m+1}\cdots\frac{m}{m+1}.
$$

Every remaining factor is less than $1$, so

$$
0<\frac{m!}{(m+1)^m}\le\frac1{m+1}\to0.
$$

This check matters. The argument only works in this form when the denominator's repeated base is at least as large as every factorial factor.

```quiz
type: radio
id: ohw6-p15-q4
content: |-
  For which sequence does keeping the first normalized factor and bounding every remaining factor by $1$ immediately prove convergence to $0$?
options:
- id: ohw6-p15-q4-a
  content: |-
    $\displaystyle \frac{m!}{(m+2)^m}$
  correct: true
- id: ohw6-p15-q4-b
  content: |-
    $\displaystyle \frac{m!}{(m-1)^m}$
- id: ohw6-p15-q4-c
  content: |-
    $\displaystyle \frac{m^m}{m!}$
- id: ohw6-p15-q4-d
  content: |-
    $\displaystyle \frac{m!}{1^m}$
```

---

<a id="summary"></a>
## Summary

For a factorial-over-self-power limit:

1. Rename a shifted index if needed so the expression looks like $m!/m^m$.
2. Rewrite it as $\prod_{k=1}^{m}(k/m)$.
3. Keep the vanishing factor $1/m$ and verify that every other factor is at most $1$.
4. Use

$$
0<\frac{m!}{m^m}\le\frac1m\to0
$$

to conclude by the Squeeze Theorem that the limit is $0$.

The main traps are trying to cancel $m!$ against $m^m$ and stopping at the weak bound $m!/m^m\le1$. The useful bound must itself approach $0$.
