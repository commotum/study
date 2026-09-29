# Identifying Monotonic Sequences Using Ratios

<!--
lesson-id: 3861
topic-code: CA2.4.2.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Testing Whether a Sequence Is Monotonic](#testing-whether-a-sequence-is-monotonic)
- [Identifying Monotonic Polynomial and Rational Sequences](#identifying-monotonic-polynomial-and-rational-sequences)
- [Identifying Monotonic Geometric Sequences](#identifying-monotonic-geometric-sequences)
- [Identifying Monotonic Sequences Containing Factorials](#identifying-monotonic-sequences-containing-factorials)

## Prerequisites

- [Fractions of Fractions](<../../../../MA/Mathematical-Foundations/MF1/3. The Number System/3.2. Multiplication and Division of Rational Numbers/Lessons/3.2.8. Fractions of Fractions.md>)
- [Monotonic Sequences](<../../../../MA/Single-Variable-Calculus/CA2/4. Sequences & Series/4.2. Monotonic Sequences/Lessons/4.2.1. Monotonic Sequences.md>)
- [The Power of Quotient Rule With Algebraic Expressions](<../../../../MA/Mathematical-Foundations/MF1/10. Exponential Functions/10.1. Rules of Exponents/Lessons/10.1.5. The Power of Quotient Rule With Algebraic Expressions.md>)
- [Factorials in Variable Expressions](<../../../../MA/Mathematical-Foundations/MF2/14. Probability & Combinatorics/14.3. Combinatorics/Lessons/14.3.3. Factorials in Variable Expressions.md>)

---

<a id="introduction"></a>
## Introduction

There are several ways to check whether a sequence is increasing or decreasing. One way is to consider the ratio between two successive terms.

- A sequence $a_n$ is *increasing* if every term is greater than or equal to the previous term. That is, for all $n\geq 1$, we have
$a_{n+1} \geq a_{n}$.
If $a_n$ is positive for all $n$, we can divide the above inequality by $a_n$, which gives
$\dfrac{a_{n+1}}{a_n} \geq 1$.
- Similarly, if a sequence $a_n$ is *decreasing* if every term is less than or equal to the previous term. That is, for all $n\geq 1$, we have
$a_{n+1} \leq a_{n}$.
If $a_n$ is positive for all $n$, we can divide the above inequality by $a_n$, which gives
$\dfrac{a_{n+1}}{a_n} \leq 1$.

Let's now formulate our findings into a single test.

---

<a id="testing-whether-a-sequence-is-monotonic"></a>
## Testing Whether a Sequence Is Monotonic

Suppose $a_n$ is a positive sequence defined for

$$
n \geq 1
$$

and that the positive real number $L$ is defined as

$$
L = \dfrac{a_{n+1}}{a_n}
$$

Then,

- if $L \geq 1$ for all $n \geq 1$, then $a_n$ is *increasing,* and
- if $0 < L \leq 1$ for all $n \geq1$, then $a_n$ is *decreasing.*

Let's take a look at some examples of how to apply this test.

---

<a id="identifying-monotonic-polynomial-and-rational-sequences"></a>
## Identifying Monotonic Polynomial and Rational Sequences

**Example:** Given that $a_n = \dfrac{3}{2n^2}$ for $n\geq 1$, which of the following statements are true?

1. $\dfrac{a_{n+1}}{a_n} \leq 1$ for all $n \geq 1$
2. $a_n$ is an increasing sequence
3. $a_n$ is a decreasing sequence

**Explanation**

Suppose $a_n$ is a positive sequence defined for

$$
n \geq 1
$$

and that

$$
L = \dfrac{a_{n+1}}{a_n}
$$

Then,

- if $L \geq 1$ for all $n \geq 1$, then $a_n$ is *increasing,* and
- if $0 < L \leq 1$ for all $n \geq1$, then $a_n$ is *decreasing.*

Notice that, in this case,

$$
a_n = \dfrac{3}{2n^2}
$$

is positive for all

$$
n \geq 1
$$

With that in mind, let's analyze each statement.

- Statement I is true. Computing the ratio $L$, we get
$L= \frac{a_{n + 1}}{a_{n}} = \frac{(\frac{3}{2(n + 1)^{2}})}{(\frac{3}{2n^{2}})} = \frac{n^{2}}{(n + 1)^{2}} = (\frac{n}{n + 1})^{2}$.
Now, since $n \geq 1$, it follows that
$\dfrac{n}{n + 1} < 1$,
since the numerator is always smaller than the denominator. Therefore
$L = \left(\dfrac{n}{n + 1}\right)^2 < 1$.
Since the sequence is positive for all $n$, we can conclude that
$0 < L < 1$.
- Statement II is false, whereas statement III is true. Since $0< L \leq 1$ for all $n\geq 1$, we can conclude that the sequence $a_n$ is decreasing.

Therefore, the correct answer is "I and III only."

---

**Question 1**

```quiz
type: radio
id: ma-81066
content: |-
  Given that $a_{n} = n^{3}$ for $n \ge 1$, which of the following statements are true?

  1. $\frac{a_{n + 1}}{a_{n}} \ge 1$ for all $n \ge 1$
  2. $a_{n}$ is an increasing sequence
  3. $a_{n}$ is a decreasing sequence
options:
- id: a
  content: |-
    II only
- id: b
  content: |-
    III only
- id: c
  content: |-
    I and III only
- id: d
  content: |-
    I only
- id: e
  correct: true
  content: |-
    I and II only
```

---

**Question 2**

```quiz
type: radio
id: ma-81067
content: |-
  Given that $a_{n} = \frac{1}{n}$ for $n \ge 1$, which of the following statements are true?

  1. $\frac{a_{n + 1}}{a_{n}} \le 1$ for all $n \ge 1$
  2. $a_{n}$ is an increasing sequence
  3. $a_{n}$ is a decreasing sequence
options:
- id: a
  content: |-
    I and II only
- id: b
  content: |-
    I only
- id: c
  correct: true
  content: |-
    I and III only
- id: d
  content: |-
    II only
- id: e
  content: |-
    III only
```

---

<a id="identifying-monotonic-geometric-sequences"></a>
## Identifying Monotonic Geometric Sequences

**Example:** Given that $a_n = 3^{n}$ for $n\geq 1$, which of the following statements are true?

1. $\dfrac{a_{n+1}}{a_n} \leq 1$ for all $n\geq 1$
2. $a_n$ is an increasing sequence
3. $a_n$ is a decreasing sequence

**Explanation**

Suppose $a_n$ is a positive sequence defined for

$$
n \geq 1
$$

and that

$$
L = \dfrac{a_{n+1}}{a_n}
$$

Then,

- if $L \geq 1$ for all $n \geq 1$, then $a_n$ is *increasing,* and
- if $0 < L \leq 1$ for all $n \geq 1$, then $a_n$ is *decreasing.*

Notice that, in this case, $a_n = 3^{n}$ is positive for all

$$
n \geq 1
$$

With that in mind, let's analyze each statement.

- Statement I is false. Computing the ratio $L$, we get
$\frac{a_{n + 1}}{a_{n}}= \frac{3^{n + 1}}{3^{n}} = 3^{n + 1 - n} = 3^{1} = 3; \ge 1$.
- Statement II is true, whereas statement III is false. Since $L \geq 1$ for all $n \geq 1$, we can conclude that the sequence $a_n$ is increasing.

Therefore, the correct answer is "II only."

---

**Question 3**

```quiz
type: radio
id: ma-80992
content: |-
  Given that $a_{n} = e^{2n}$ for $n \ge 1$, which of the following statements are true?

  1. $\frac{a_{n + 1}}{a_{n}} \ge 1$ for all $n \ge 1$
  2. $a_{n}$ is an increasing sequence
  3. $a_{n}$ is a decreasing sequence
options:
- id: a
  content: |-
    II only
- id: b
  content: |-
    III only
- id: c
  content: |-
    I and III only
- id: d
  content: |-
    I only
- id: e
  correct: true
  content: |-
    I and II only
```

---

**Question 4**

```quiz
type: radio
id: ma-81072
content: |-
  Given that $a_{n} = \frac{1}{e^{n}}$ for $n \ge 1$, which of the following statements are true?

  1. $\frac{a_{n + 1}}{a_{n}} \ge 1$ for all $n \ge 1$
  2. $a_{n}$ is an increasing sequence
  3. $a_{n}$ is a decreasing sequence
options:
- id: a
  content: |-
    II only
- id: b
  correct: true
  content: |-
    III only
- id: c
  content: |-
    I and III only
- id: d
  content: |-
    I and II only
- id: e
  content: |-
    I only
```

---

<a id="identifying-monotonic-sequences-containing-factorials"></a>
## Identifying Monotonic Sequences Containing Factorials

**Example:** Given that $a_n = \dfrac{6^n}{(n+4)!}$ for $n\geq 1$, which of the following statements are true?

1. $\dfrac{a_{n+1}}{a_n} \leq 1$ for all $n\geq 1$
2. $a_n$ is an increasing sequence
3. $a_n$ is a decreasing sequence

**Explanation**

Suppose $a_n$ is a positive sequence defined for

$$
n\geq 1
$$

and that

$$
L = \dfrac{a_{n+1}}{a_n}
$$

Then,

- if $L \geq 1$ for all $n \geq 1$, then $a_n$ is *increasing,* and
- if $0 < L \leq 1$ for all $n \geq1$, then $a_n$ is *decreasing.*

Notice that, in this case,

$$
a_n = \dfrac{6^n}{(n+4)!}
$$

is positive for all

$$
n\geq 1
$$

With that in mind, let's analyze each statement.

- Statement I is true. Computing the ratio $L$, we get
$\frac{a_{n+1}}{a_n}=\frac{\frac{6^{n+1}}{(n+5)!}}{\frac{6^n}{(n+4)!}}=\frac{6}{n+5}\le 1$.
- Statement II is false, whereas statement III is true. Since $0< L\leq 1$ for all $n\geq 1$, we can conclude that the sequence $a_n$ is decreasing.

Therefore, the correct answer is "I and III only."

---

**Question 5**

```quiz
type: radio
id: ma-123831
content: |-
  Given that $a_{n} = \frac{1}{(2n)!}$ for $n \ge 1$, which of the following statements are true?

  1. $\frac{a_{n + 1}}{a_{n}} \ge 1$ for all $n \ge 1$
  2. $a_{n}$ is an increasing sequence
  3. $a_{n}$ is a decreasing sequence
options:
- id: a
  content: |-
    I and II only
- id: b
  content: |-
    II only
- id: c
  content: |-
    I and III only
- id: d
  content: |-
    I only
- id: e
  correct: true
  content: |-
    III only
```

---

**Question 6**

```quiz
type: radio
id: ma-81152
content: |-
  Given that $a_{n} = \frac{(n + 1)!}{3^{n}}$ for $n \ge 1$, which of the following statements are true?

  1. $\frac{a_{n + 1}}{a_{n}} \le 1$ for all $n \ge 1$
  2. $a_{n}$ is an increasing sequence
  3. $a_{n}$ is a decreasing sequence
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    I and III only
- id: c
  content: |-
    III only
- id: d
  correct: true
  content: |-
    II only
- id: e
  content: |-
    I and II only
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
