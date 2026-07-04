# Infinite Series and Partial Sums

<!--
lesson-id: 981
topic-code: MF3.1.4.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Finding the First Partial Sums of an Infinite Series](#finding-the-first-partial-sums-of-an-infinite-series)
- [Finding a Partial Sum of an Infinite Arithmetic Series](#finding-a-partial-sum-of-an-infinite-arithmetic-series)
- [Finding a General Partial Sum of an Infinite Arithmetic Series](#finding-a-general-partial-sum-of-an-infinite-arithmetic-series)
- [Finding a Partial Sum of an Infinite Geometric Series](#finding-a-partial-sum-of-an-infinite-geometric-series)

## Prerequisites

- [Finding the Sum of an Arithmetic Series](<../../1.2. Arithmetic Series/Lessons/1.2.2. Finding the Sum of an Arithmetic Series.md>)
- [Sums of Finite Geometric Series Given in Sigma Notation](<../../1.3. Finite Geometric Series/Lessons/1.3.4. Sums of Finite Geometric Series Given in Sigma Notation.md>)

---

<a id="introduction"></a>
## Introduction

Any series with infinitely many terms is called an **infinite series**. Infinite series are usually denoted using sigma notation as

$$
\sum_{n=1}^\infty a_n
$$

where each $a_n$ represents an individual term of the sequence that makes up the series.

For example, the **harmonic series** below is an example of an infinite series:

$$
\sum_{n=1}^\infty \dfrac{1}{n} = \dfrac{1}{1}+\dfrac{1}{2}+\dfrac{1}{3}+\cdots + \dfrac 1 k +\cdots
$$

A **partial sum** $s_k$ of an infinite series is a sum of the first $k$ terms. For example, the first, second, third, and fourth partial sums, denoted $s_1$, $s_2$, $s_3$, and $s_4$ respectively, of the harmonic series are

$$
\begin{aligned}
s_{1} = ∑_(n = 1)^(1)\frac{1}{n} &= \frac{1}{1} = 1 \\
s_{2} = ∑_(n = 1)^(2)\frac{1}{n} &= \frac{1}{1} + \frac{1}{2} = \frac{3}{2} \\
s_{3} = ∑_(n = 1)^(3)\frac{1}{n} &= \frac{1}{1} + \frac{1}{2} + \frac{1}{3} = \frac{11}{6} \\
s_{4} = ∑_(n = 1)^(4)\frac{1}{n} &= \frac{1}{1} + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} = \frac{25}{12}
\end{aligned}
$$

---

<a id="finding-the-first-partial-sums-of-an-infinite-series"></a>
## Finding the First Partial Sums of an Infinite Series

**Example:** Find the first, second, and third partial sums of the series
$\sum_{n=1}^\infty \dfrac 1 {n^2+1}$.

**Explanation**

Let's start by calculating the first three terms:

$$
\begin{aligned}
a_{1} &= \frac{1}{1^{2} + 1} = \frac{1}{2} \\
a_{2} &= \frac{1}{2^{2} + 1} = \frac{1}{5} \\
a_{3} &= \frac{1}{3^{2} + 1} = \frac{1}{10}
\end{aligned}
$$

Therefore, the first, second, and third partial sums are

$$
\begin{aligned}
s_{1} &= \frac{1}{2} \\
s_{2} &= \frac{1}{2} + \frac{1}{5} = \frac{7}{10} \\
s_{3} &= \frac{1}{2} + \frac{1}{5} + \frac{1}{10} = \frac{8}{10}
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Find the third partial sum of the series
  
  $∑_(n = 1)^(∞)((-1)^{2n}n!)/(n)$.
options:
- id: a
  content: |-
    $2$
- id: b
  content: |-
    $\frac{16}{3}$
- id: c
  content: |-
    $8$
- id: d
  content: |-
    $\frac{23}{6}$
- id: e
  correct: true
  content: |-
    $4$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Find the third partial sum of the series
  
  $∑_(n = 1)^(∞)\frac{1}{n^{2} + 2}$.
options:
- id: a
  content: |-
    $\frac{13}{11}$
- id: b
  content: |-
    $\frac{1}{2}$
- id: c
  content: |-
    $\frac{1}{11}$
- id: d
  correct: true
  content: |-
    $\frac{13}{22}$
- id: e
  content: |-
    $\frac{9}{22}$
```

---

<a id="finding-a-partial-sum-of-an-infinite-arithmetic-series"></a>
## Finding a Partial Sum of an Infinite Arithmetic Series

**Example:** Find the twelfth partial sum of the series $\displaystyle \sum_{n=1}^\infty (2n-1)$.

**Explanation**

Let $a_n = 2n-1$. If we compute the first few terms, we get

$$
\begin{aligned}
a_{1} &= 2(1) - 1 = 1 \\
a_{2} &= 2(2) - 1 = 3 \\
a_{3} &= 2(3) - 1 = 5
\end{aligned}
$$

and we notice that this is an arithmetic sequence with common difference $d=2$ and first term $a_1 = 1$.

We can compute the $k$th partial sum of an arithmetic series using the formula

$$
s_k = \dfrac{k}{2}(a_1+a_k)
$$

Since

$$
a_{12} = 2(12)-1 = 23
$$

we get

$$
s_{12} =\dfrac{12}{2}(1+23) = 144
$$

So the twelfth partial sum of

$$
\displaystyle \sum_{n=1}^\infty (2n-1)
$$

is equal to $144$.

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Find the seventh partial sum of the series
  
  $∑_(n = 1)^(∞)(3n + 1)$.
options:
- id: a
  content: |-
    $108$
- id: b
  content: |-
    $80$
- id: c
  content: |-
    $125$
- id: d
  content: |-
    $154$
- id: e
  correct: true
  content: |-
    $91$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Find the eighth partial sum of the series
  
  $∑_(n = 1)^(∞)(5n - 4)$.
options:
- id: a
  content: |-
    $130$
- id: b
  content: |-
    $184$
- id: c
  content: |-
    $166$
- id: d
  correct: true
  content: |-
    $148$
- id: e
  content: |-
    $202$
```

---

<a id="finding-a-general-partial-sum-of-an-infinite-arithmetic-series"></a>
## Finding a General Partial Sum of an Infinite Arithmetic Series

**Example:** Find the $k$th partial sum of the series $\displaystyle \sum_{n=1}^\infty (6-5n)$.

**Explanation**

Let $a_n = 6-5n$. If we compute the first few terms, we get

$$
\begin{aligned}
a_{1} &= 6 - 5(1) = 1 \\
a_{2} &= 6 - 5(2) =-4 \\
a_{3} &= 6 - 5(3) =-9
\end{aligned}
$$

and we see that this is an arithmetic sequence with common difference $d=-5$ and $a_1=1$.

We can compute the $k$th partial sum of an arithmetic series using the formula

$$
s_k = \dfrac{k}{2}(a_1+a_k)
$$

Since

$$
a_{k} = 6-5k
$$

we get

$$
\begin{aligned}
s_{k} &= \frac{k}{2}(1 + 6 - 5k) \\
&= \frac{k}{2}(7 - 5k)
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  Find the $k$th partial sum of the series
  
  $∑_(n = 1)^(∞)(n + 5)$.
options:
- id: a
  content: |-
    $(k(k + 5))/(2)$
- id: b
  content: |-
    $\frac{k + 11}{2}$
- id: c
  content: |-
    $(k(k + 1))/(2)$
- id: d
  content: |-
    $\frac{k + 5}{2}$
- id: e
  correct: true
  content: |-
    $(k(k + 11))/(2)$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Find the $k$th partial sum of the series
  
  $∑_(n = 1)^(∞)(n - 3)$.
options:
- id: a
  content: |-
    $(k(k + 5))/(2)$
- id: b
  correct: true
  content: |-
    $(k(k - 5))/(2)$
- id: c
  content: |-
    $\frac{k + 5}{2}$
- id: d
  content: |-
    $\frac{k - 5}{2}$
- id: e
  content: |-
    $(k(k - 3))/(2)$
```

---

<a id="finding-a-partial-sum-of-an-infinite-geometric-series"></a>
## Finding a Partial Sum of an Infinite Geometric Series

**Example:** Find the fifth partial sum of the series $\displaystyle \sum_{n=1}^\infty 24 \left(\dfrac{1}{2}\right)^n$.

**Explanation**

Let

$$
a_n = 24 \left(\dfrac{1}{2}\right)^n
$$

We note that this is a geometric sequence with

$$
r=\dfrac 1 2
$$

and first term given by

$$
a_1 = 24\cdot \dfrac 1 2 = 12
$$

The $k$th partial sum of a geometric series is given by

$$
s_k = a_1\left(\dfrac{1-r^k}{1-r}\right)
$$

Therefore, the fifth partial sum is

$$
\begin{aligned}
s_{5} &= 12 \cdot ((1 - (\frac{1}{2})^{5})/((1 - \frac{1}{2}))) \\
&= 24 \cdot (1 - (\frac{1}{2})^{5}) \\
&= 24 \cdot (1 - \frac{1}{32}) \\
&= 24 \cdot (\frac{31}{32}) \\
&= \frac{93}{4}
\end{aligned}
$$

---

**Question 7:**

```quiz
type: radio
id: q-7
content: |-
  Determine the seventh partial sum of the series
  
  $∑_(n = 1)^(∞)(\frac{1}{2})^{n}$.
options:
- id: a
  content: |-
    $\frac{255}{256}$
- id: b
  content: |-
    $\frac{15}{16}$
- id: c
  content: |-
    $\frac{63}{64}$
- id: d
  content: |-
    $\frac{31}{32}$
- id: e
  correct: true
  content: |-
    $\frac{127}{128}$
```

---

**Question 8:**

```quiz
type: radio
id: q-8
content: |-
  What is the seventh partial sum of the series
  
  $∑_(n = 1)^(∞)2^{n - 1}$?
options:
- id: a
  content: |-
    $63$
- id: b
  content: |-
    $255$
- id: c
  content: |-
    $126$
- id: d
  content: |-
    $254$
- id: e
  correct: true
  content: |-
    $127$
```

```update-progress
```

[[MA/Mathematical-Foundations/MF3/Home|Home]]
[[MA/Mathematical-Foundations/MF3/0. Table of Contents/TOC|Table of Contents]]
