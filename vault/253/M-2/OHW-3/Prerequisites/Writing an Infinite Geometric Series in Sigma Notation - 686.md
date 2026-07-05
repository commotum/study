# Writing an Infinite Geometric Series in Sigma Notation

<!--
lesson-id: 686
topic-code: MF3.1.4.8
-->

## Table of Contents

- [Introduction](#introduction)
- [Expressing an Infinite Series Using Sigma Notation Given The First Few Terms](#expressing-an-infinite-series-using-sigma-notation-given-the-first-few-terms)
- [Expressing an Infinite Series Using Sigma Notation Given Its First Term and Common Ratio](#expressing-an-infinite-series-using-sigma-notation-given-its-first-term-and-common-ratio)

## Prerequisites

- [Infinite Series and Partial Sums](<1.4.3. Infinite Series and Partial Sums.md>)

---

<a id="introduction"></a>
## Introduction

Suppose we want to write down the infinite geometric series

$$
S = 1+ \dfrac 1 2 + \dfrac 1 4 + \dfrac 1 8 + \dfrac{1}{16} + \dots
$$

in a compact way. We can express this using sigma notation with summation to infinity, as follows:

$$
S = \displaystyle\sum_{n = 1}^\infty a_n
$$

Let us define $a_n$. The common ratio for the given series is

$$
r = \dfrac 1 2
$$

and the first term is $a_1 = 1$. Therefore, we have

$$
\begin{aligned}
a_{n} &= a_{1} \cdot r^{n - 1} \\
&= (\frac{1}{2})^{n - 1} \\
&= (\frac{1}{2})^{n} \cdot (\frac{1}{2})^{-1} \\
&= 2(\frac{1}{2})^{n}
\end{aligned}
$$

Finally, the infinite geometric series can be written in sigma notation as

$$
S = \displaystyle\sum_{n =1}^\infty 2\left(\dfrac 1 2\right)^{n}
$$

---

<a id="expressing-an-infinite-series-using-sigma-notation-given-the-first-few-terms"></a>
## Expressing an Infinite Series Using Sigma Notation Given The First Few Terms

**Example:** Express the sum to infinity of the following geometric series using sigma notation:
$\dfrac{5}{3}-\dfrac{5}{9}+\dfrac{5}{27}-\dfrac{5}{81}+\cdots$

**Explanation**

The first term

$$
a_1 = \dfrac{5}{3}
$$

and the second term

$$
a_2 =-\dfrac{5}{9}
$$

Using these two terms, we compute
the common ratio:

$$
r = \frac{a_2}{a_1} = \frac{\left(-\dfrac{5}{9} \right)}{\left(\dfrac{5}{3} \right)} =-\dfrac{1}{3}
$$

Therefore, the general term $a_n$ can be expressed as

$$
\begin{aligned}
a_{n} &= a_{1}(r)^{n - 1} \\
&= \frac{5}{3}(-\frac{1}{3})^{n - 1} \\
&= \frac{5}{3}(-\frac{1}{3})^{-1}(-\frac{1}{3})^{n} \\
&= (-5)(-\frac{1}{3})^{n}
\end{aligned}
$$

Finally, the infinite geometric series can be written in sigma notation as

$$
\begin{aligned}
\frac{5}{3} - \frac{5}{9} + \frac{5}{27} - \frac{5}{81} + ⋯ &= ∑_(n = 1)^(∞)a_{n} \\
&= ∑_(n = 1)^(∞)(-5)(-\frac{1}{3})^{n}
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Express the sum to infinity of the following geometric series using sigma notation:
  
  $-2.4 + 7.2 - 21.6 + ⋯$
options:
- id: a
  content: |-
    $∑_(n = 1)^(∞)(-2.4)(-3)^{n}$
- id: b
  content: |-
    $∑_(n = 1)^(∞)7.2(-3)^{n}$
- id: c
  content: |-
    $∑_(n = 1)^(∞)0.8(-3)^{n}$
  correct: true
- id: d
  content: |-
    $∑_(n = 1)^(∞)(-0.8)(-3)^{n}$
- id: e
  content: |-
    $∑_(n = 1)^(∞)2.4(-3)^{n}$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Express the sum to infinity of the following geometric series using sigma notation:
  
  $16 - 4 + 1 + ⋯$
options:
- id: a
  content: |-
    $∑_(n = 1)^(∞)4(-\frac{1}{4})^{n}$
- id: b
  content: |-
    $∑_(n = 1)^(∞)(-4)(-\frac{1}{4})^{n}$
- id: c
  content: |-
    $∑_(n = 1)^(∞)(-64)(-\frac{1}{4})^{n}$
  correct: true
- id: d
  content: |-
    $∑_(n = 1)^(∞)64(-\frac{1}{4})^{n}$
- id: e
  content: |-
    $∑_(n = 1)^(∞)16(-\frac{1}{4})^{n}$
```

---

<a id="expressing-an-infinite-series-using-sigma-notation-given-its-first-term-and-common-ratio"></a>
## Expressing an Infinite Series Using Sigma Notation Given Its First Term and Common Ratio

**Example:** Consider the sequence starting from $a_1=-20$ with the property $\dfrac{a_{n+1}}{a_n}=-\dfrac{1}{5}$ for all $n\geq 1$. Write the sum to infinity of the terms of this sequence using sigma notation.

**Explanation**

Notice that the sequence is a geometric sequence since the ratio of any two successive terms is constant.

The first term of the sequence is $a_1 =-20$, and the common ratio is

$$
r = \dfrac{a_{n+1}}{a_n} =-\dfrac{1}{5}
$$

Therefore, the general term $a_n$ can be expressed as

$$
\begin{aligned}
a_{n} &= a_{1}(r)^{n - 1} \\
&= (-20)(-\frac{1}{5})^{n - 1} \\
&= (-20)(-\frac{1}{5})^{-1}(-\frac{1}{5})^{n} \\
&= 100(-\frac{1}{5})^{n}
\end{aligned}
$$

Finally, the infinite geometric series can be written in sigma notation as

$$
\sum_{n=1}^\infty a_n=\sum_{n=1}^\infty 100\left(-\frac{1}{5}\right)^{n}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Consider the sequence starting from $a_{1} =-30$ with the property $\frac{a_{n + 1}}{a_{n}} = \frac{5}{9}$ for all $n \ge 1$. Write the sum to infinity of the terms of this sequence using sigma notation.
options:
- id: a
  content: |-
    $∑_(n = 1)^(∞)(\frac{50}{3})(\frac{5}{9})^{n}$
- id: b
  content: |-
    $∑_(n = 1)^(∞)(-54)(\frac{5}{9})^{n}$
  correct: true
- id: c
  content: |-
    $∑_(n = 1)^(∞)56(\frac{5}{9})^{n}$
- id: d
  content: |-
    $∑_(n = 1)^(∞)(-\frac{50}{3})(\frac{5}{9})^{n}$
- id: e
  content: |-
    $∑_(n = 1)^(∞)54(\frac{5}{9})^{n}$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Consider the sequence starting from $a_{1} = 6$ with the property $\frac{a_{n + 1}}{a_{n}} = \frac{1}{6}$ for all $n \ge 1$. Write the sum to infinity of the terms of this sequence using sigma notation.
options:
- id: a
  content: |-
    $∑_(n = 1)^(∞)(\frac{1}{6})^{n}$
- id: b
  content: |-
    $∑_(n = 1)^(∞)12(\frac{1}{6})^{n}$
- id: c
  content: |-
    $∑_(n = 1)^(∞)36(\frac{1}{6})^{n}$
  correct: true
- id: d
  content: |-
    $∑_(n = 1)^(∞)\frac{1}{36}(\frac{1}{6})^{n}$
- id: e
  content: |-
    $∑_(n = 1)^(∞)42(\frac{1}{6})^{n}$
```

```update-progress
```

[[MA/Mathematical-Foundations/MF3/Home|Home]]
[[MA/Mathematical-Foundations/MF3/0. Table of Contents/TOC|Table of Contents]]
