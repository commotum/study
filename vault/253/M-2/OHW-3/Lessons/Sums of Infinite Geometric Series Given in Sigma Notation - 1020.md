# Sums of Infinite Geometric Series Given in Sigma Notation

<!--
lesson-id: 1020
topic-code: MF3.1.4.9
-->

## Table of Contents

- [Introduction](#introduction)
- [Evaluating an Infinite Geometric Series Given Its First Term and Common Ratio](#evaluating-an-infinite-geometric-series-given-its-first-term-and-common-ratio)
- [Evaluating an Infinite Geometric Series Expressed in Sigma Notation](#evaluating-an-infinite-geometric-series-expressed-in-sigma-notation)
- [Evaluating an Infinite Geometric Series Expressed in Sigma Notation With an Arbitrary Starting Index](#evaluating-an-infinite-geometric-series-expressed-in-sigma-notation-with-an-arbitrary-starting-index)
- [Evaluating an Infinite Geometric Series Expressed in Non-Standard Form Using Sigma Notation](#evaluating-an-infinite-geometric-series-expressed-in-non-standard-form-using-sigma-notation)

## Prerequisites

- [Writing an Infinite Geometric Series in Sigma Notation](<../../../../MA/Mathematical-Foundations/MF3/1. Sequences and Series/1.4. Infinite Series/Lessons/1.4.8. Writing an Infinite Geometric Series in Sigma Notation.md>)
- [Finding the Sum of an Infinite Geometric Series](<../../../../MA/Mathematical-Foundations/MF3/1. Sequences and Series/1.4. Infinite Series/Lessons/1.4.7. Finding the Sum of an Infinite Geometric Series.md>)

---

<a id="introduction"></a>
## Introduction

Suppose we want to evaluate the infinite geometric series

$$
\sum_{n = 1} ^ \infty 3 \left (\dfrac 1 4\right) ^ n
$$

The sum $S_\infty$ of an infinite geometric series is given by the formula

$$
S_{\infty} = \dfrac {\color{black}a_1} {1 - {\color{black}r}}
$$

where ${\color{black}r}$ is the common ratio and $\color{black}a_1$ is the first term. So, we need to determine $\color{black}a_1$ and $\color{black}r$ and then plug those values into this formula.

The first term is

$$
{\color{black}a_1} = 3 \left(\dfrac 1 4 \right)^1 = {\color{black}\dfrac 3 4}
$$

and the common ratio is

$$
{\color{black}r} = \dfrac {a_2}{\color{black}a_1} = \dfrac {3 \left (\dfrac 1 4 \right)^2}{3\left(\dfrac 1 4 \right)^1}= {\color{black}\dfrac 1 4}
$$

So, the sum of the series is

$$
\begin{aligned}
∑_(n = 1)^(∞)3(\frac{1}{4})^{n} &= \frac{a_{1}}{1 - r} \\
&= ((\frac{3}{4}))/((1 - \frac{1}{4})) \\
&= ((\frac{3}{4}))/((\frac{3}{4})) \\
&= 1
\end{aligned}
$$

---

<a id="evaluating-an-infinite-geometric-series-given-its-first-term-and-common-ratio"></a>
## Evaluating an Infinite Geometric Series Given Its First Term and Common Ratio

**Example:** Given that $a_1=-2$ and $\dfrac{a_{n+1}}{a_{n}} = -0.4$ for all integers $n \geq 1$, find the value of $\displaystyle\sum_{n=1}^\infty a_{n}$.

**Explanation**

Notice that the given series is a geometric series because the ratio of any two consecutive terms is constant.

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$
S_\infty = \dfrac{a_1}{1-r}, \qquad \mid r \mid < 1
$$

where $a_1$ is the first term and $r$ is the common ratio.

We're told that the first term is

$$
a_1=-2
$$

The common ratio is

$$
r = \dfrac{a_{n+1}}{a_{n}} = -0.4
$$

So, the sum of the series is

$$
\begin{aligned}
∑_(n = 1)^(∞)a_{n} &= \frac{a_{1}}{1 - r} \\
&= (-2)/(1 - (-0.4)) \\
&= \frac{-2}{1.4} \\
&=-\frac{10}{7}
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Given that $a_{1} =-18$ and $\frac{a_{n + 1}}{a_{n}} =-0.9$ for all integers $n \ge 1$, find the value of $∑_(n = 1)^(∞)a_{n}$.
options:
- id: a
  content: |-
    $-\frac{19}{2}$
- id: b
  content: |-
    $-\frac{180}{19}$
  correct: true
- id: c
  content: |-
    $-\frac{28}{3}$
- id: d
  content: |-
    $-15$
- id: e
  content: |-
    $-10$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Given that $a_{1} = 5$ and $\frac{a_{n + 1}}{a_{n}} = \frac{3}{5}$ for all integers $n \ge 1$, find the value of $∑_(n = 1)^(∞)a_{n}$.
options:
- id: a
  content: |-
    $4$
- id: b
  content: |-
    $12$
- id: c
  content: |-
    $25$
- id: d
  content: |-
    $\frac{25}{2}$
  correct: true
- id: e
  content: |-
    $\frac{27}{2}$
```

---

<a id="evaluating-an-infinite-geometric-series-expressed-in-sigma-notation"></a>
## Evaluating an Infinite Geometric Series Expressed in Sigma Notation

**Example:** Evaluate the series $\displaystyle\sum_{n=1}^\infty 2(0.5)^{n}$.

**Explanation**

Notice that the given series is a geometric series because it is in the form $\displaystyle \sum ar^n$.

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$
S_\infty = \dfrac{a_1}{1-r}, \qquad \mid r \mid < 1
$$

where $a_1$ is the first term and $r$ is the common ratio.

The first term is

$$
a_1 = 2(0.5)^{1} = 1
$$

The common ratio is

$$
r = \dfrac{a_2}{a_1} = \dfrac{2(0.5)^2}{2(0.5)^1} = 0.5
$$

So, the sum of the series is

$$
\begin{aligned}
∑_(n = 1)^(∞)2(0.5)^{n} &= \frac{a_{1}}{1 - r} \\
&= \frac{1}{1 - 0.5} \\
&= \frac{1}{0.5} \\
&= 2
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  What is $∑_(n = 1)^(∞)\frac{1}{2}(0.3)^{n}$?
options:
- id: a
  content: |-
    $\frac{2}{7}$
- id: b
  content: |-
    $\frac{3}{14}$
  correct: true
- id: c
  content: |-
    $\frac{3}{20}$
- id: d
  content: |-
    $\frac{6}{29}$
- id: e
  content: |-
    $\frac{1}{5}$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  What is $∑_(n = 1)^(∞)5(\frac{1}{4})^{n}$?
options:
- id: a
  content: |-
    $\frac{1}{2}$
- id: b
  content: |-
    $\frac{5}{3}$
  correct: true
- id: c
  content: |-
    $\frac{5}{4}$
- id: d
  content: |-
    $\frac{1}{3}$
- id: e
  content: |-
    $\frac{1}{4}$
```

---

<a id="evaluating-an-infinite-geometric-series-expressed-in-sigma-notation-with-an-arbitrary-starting-index"></a>
## Evaluating an Infinite Geometric Series Expressed in Sigma Notation With an Arbitrary Starting Index

**Example:** Evaluate the series $\displaystyle \sum_{n=2}^\infty\left(\dfrac 2 3\right)^n$.

**Explanation**

First, note that the index $n$ starts from $2$. However, it is still a geometric series because it is in the form $\displaystyle \sum ar^n$.

In this case, the first term is $a_2$, and so the sum to infinity $S_\infty$ of this geometric series is given by

$$
S_\infty = \dfrac{a_2}{1-r}, \qquad \mid r \mid < 1
$$

For the first few terms, we have:

$$
\begin{aligned}
a_{2} &= (\frac{2}{3})^{2} = \frac{4}{9} \\
a_{3} &= (\frac{2}{3})^{3} = \frac{8}{27}
\end{aligned}
$$

The common ratio is:

$$
r = \dfrac{a_3}{a_2} = \dfrac{\left(\dfrac{8}{27}\right)}{\left(\dfrac{4}{9}\right)} = \dfrac 2 3
$$

So, the sum of the series is:

$$
\begin{aligned}
∑_(n = 2)^(∞)(\frac{2}{3})^{n} &= \frac{a_{2}}{1 - r} \\
&= ((\frac{4}{9}))/((1 - \frac{2}{3})) \\
&= ((\frac{4}{9}))/((\frac{1}{3})) \\
&= \frac{4 \cdot 3}{9} \\
&= \frac{4}{3}
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  What is $∑_(n = 3)^(∞)\frac{9}{2}(\frac{1}{3})^{n}$?
options:
- id: a
  content: |-
    $\frac{1}{5}$
- id: b
  content: |-
    $\frac{1}{4}$
  correct: true
- id: c
  content: |-
    $\frac{1}{2}$
- id: d
  content: |-
    $\frac{2}{3}$
- id: e
  content: |-
    $\frac{1}{3}$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Evaluate the series $∑_(n = 2)^(∞)(\frac{1}{4})^{n}$.
options:
- id: a
  content: |-
    $\frac{7}{12}$
- id: b
  content: |-
    $\frac{5}{4}$
- id: c
  content: |-
    $\frac{1}{8}$
- id: d
  content: |-
    $\frac{1}{12}$
  correct: true
- id: e
  content: |-
    $\frac{1}{10}$
```

---

<a id="evaluating-an-infinite-geometric-series-expressed-in-non-standard-form-using-sigma-notation"></a>
## Evaluating an Infinite Geometric Series Expressed in Non-Standard Form Using Sigma Notation

**Example:** Evaluate the geometric series $\displaystyle \sum_{n=3}^\infty \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{2n}$.

**Explanation**

First, note that the index $n$ starts from $3$. In this case, the first term is $a_3$, and so the sum to infinity $S_\infty$ of this geometric series is given by

$$
S_\infty = \dfrac{a_3}{1-r}, \qquad \mid r \mid < 1
$$

Computing the first few terms, we get:

$$
a_3 = \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{2(3)} = \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{6} = 5\left(\dfrac{1}{2}\right)^{7}
$$

$$
a_4 = \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{2(4)} = \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{8} = 5\left(\dfrac{1}{2}\right)^{9}
$$

Therefore, the common ratio is

$$
r = \dfrac{a_4}{a_3} = \dfrac{5\left(\dfrac{1}{2}\right)^{9}}{5\left(\dfrac{1}{2}\right)^{7}} = \left(\dfrac{1}{2}\right)^{2} = \dfrac{1}{4}
$$

So, the sum of the series is

$$
\begin{aligned}
∑_(n = 3)^(∞)\frac{5}{2}(\frac{1}{2})^{2n} &= \frac{a_{3}}{1 - r} \\
&= (5(\frac{1}{2})^{7})/((1 - \frac{1}{4})) \\
&= ((\frac{5}{128}))/((\frac{3}{4})) \\
&= (\frac{5}{128})(\frac{4}{3}) \\
&= (5)/(3(32)) \\
&= \frac{5}{96}
\end{aligned}
$$

---

**Question 7**

```quiz
type: radio
id: q-7
content: |-
  > A scientific calculator is required to answer this question.
  
  Evaluate the geometric series $∑_(n = 2)^(∞)8(-\frac{3}{5})^{n - 1}$.
options:
- id: a
  content: |-
    $-3$
  correct: true
- id: b
  content: |-
    $\frac{1}{3}$
- id: c
  content: |-
    $-\frac{8}{5}$
- id: d
  content: |-
    $-4$
- id: e
  content: |-
    $\frac{24}{5}$
```

---

**Question 8**

```quiz
type: radio
id: q-8
content: |-
  > A scientific calculator is required to answer this question.
  
  Evaluate the geometric series $∑_(n = 1)^(∞)3(0.5)^{4n}$.
options:
- id: a
  content: |-
    $2$
- id: b
  content: |-
    $1$
- id: c
  content: |-
    $4$
- id: d
  content: |-
    $\frac{1}{5}$
  correct: true
- id: e
  content: |-
    $\frac{1}{4}$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
