# Telescoping Series

<!--
lesson-id: 1176
topic-code: CA2.4.3.5
-->

## Table of Contents

- [Introduction](#introduction)
- [Calculating the Sum of a Series Whose Denominator Is the Product of N and N+1](#calculating-the-sum-of-a-series-whose-denominator-is-the-product-of-n-and-n1)
- [Calculating the Sum of a Series Whose Denominator Is the Product of Two Consecutive Expressions](#calculating-the-sum-of-a-series-whose-denominator-is-the-product-of-two-consecutive-expressions)
- [Calculating the Sum of a Series Whose Denominator Is the Product of Two Non-Consecutive Expressions (x+a)(x+a+2)](#calculating-the-sum-of-a-series-whose-denominator-is-the-product-of-two-non-consecutive-expressions-xaxa2)

## Prerequisites

- [Convergent and Divergent Infinite Series](<../../../../MA/Mathematical-Foundations/MF3/1. Sequences and Series/1.4. Infinite Series/Lessons/1.4.4. Convergent and Divergent Infinite Series.md>)
- [Expressing Rational Functions as Sums of Partial Fractions](<../../../../MA/Mathematical-Foundations/MF2/6. Radical & Rational Functions/6.1. Rational Expressions/Lessons/6.1.6. Expressing Rational Functions as Sums of Partial Fractions.md>)

---

<a id="introduction"></a>
## Introduction

Let's see a trick that can be used to compute the sum of the following series:

$$
\sum_{n = 1}^\infty \dfrac 1 {n (n + 1)}
$$

First, we can use partial fractions to write

$$
\dfrac{1}{n(n+1)} = \dfrac{1}{n} - \dfrac{1}{n+1}
$$

Then the sum is given by

$$
\sum_{n = 1}^\infty \dfrac 1 {n (n + 1)} = \sum_{n = 1}^\infty\left(\dfrac{1}{n} - \dfrac{1}{n+1}\right)
$$

Computing the first few partial sums, *without* simplifying, notice that many terms cancel:

$\require{cancel}$

$$
\begin{aligned}
s_{1} &= (1- \frac{1}{2}) \\
s_{2} &= (1 - \frac{1}{2}) + (\frac{1}{2}- \frac{1}{3}) \\
s_{3} &= (1 - \frac{1}{2}) + (\frac{1}{2} - \frac{1}{3}) + (\frac{1}{3}- \frac{1}{4}) \\
s_{4} &= (1 - \frac{1}{2}) + (\frac{1}{2} - \frac{1}{3}) + (\frac{1}{3} - \frac{1}{4}) + (\frac{1}{4}- \frac{1}{5})
\end{aligned}
$$

For each partial sum, we always end up canceling all terms except for the first and last terms. We say that this infinite series is a **telescoping series**, meaning that it consists of only a finite number of terms after canceling.

So, if $s_N$ is the $N$th partial sum of the series, we have

$$
s_N = {\color{blue}{1}} {\color{red}{\,-\, \dfrac 1 {N + 1}}}
$$

Finally, we can determine the sum of the series by computing the limit of $s_N$ as $N\to\infty$. We get

$$
\begin{aligned}
\sum_{n=1}^{\infty}\frac{1}{n(n + 1)} &= \lim_{N \to \infty}(1 - \frac{1}{N + 1}) \\
&= 1 - 0 \\
&= 1
\end{aligned}
$$

---

<a id="calculating-the-sum-of-a-series-whose-denominator-is-the-product-of-n-and-n1"></a>
## Calculating the Sum of a Series Whose Denominator Is the Product of N and N+1

**Example:** Calculate $\displaystyle \sum\limits_{n = 4}^\infty {\dfrac{3}{{n(n + 1)}}}$.

**Explanation**

First, note that the series can be written as

$$
3\sum\limits_{n = 4}^\infty {\dfrac{1}{{n(n + 1)}}}
$$

Using partial fractions, we can write the series as

$$
\displaystyle 3\sum\limits_{n = 4}^\infty \left(\dfrac 1 n - \dfrac 1 {n+1}\right)
$$

Computing the first few partial sums, starting with $n=4$, gives

$\require{cancel}$

$$
\begin{aligned}
s_{4} &= 3[(\frac{1}{4} - \frac{1}{5})] \\
s_{5} &= 3[(\frac{1}{4} - \frac{1}{5}) + (\frac{1}{5} - \frac{1}{6})] \\
s_{6} &= 3[(\frac{1}{4} - \frac{1}{5}) + (\frac{1}{5} - \frac{1}{6}) + (\frac{1}{6} - \frac{1}{7})] \\
s_{7} &= 3[(\frac{1}{4} - \frac{1}{5}) + (\frac{1}{5} - \frac{1}{6}) + (\frac{1}{6} - \frac{1}{7}) + (\frac{1}{7} - \frac{1}{8})]
\end{aligned}
$$

Notice that in each partial sum, we always end up canceling all terms except for the first and last terms. Therefore, the $N$th partial sum is

$$
s_N = 3\left[\dfrac 1 4 - \dfrac{1}{N+1}\right]
$$

Finally, we can determine the sum of the series by taking the limit of $s_N$:

$$
\begin{aligned}
\sum_{n=4}^{\infty}\frac{3}{n(n + 1)} &= \lim_{N \to \infty}s_{N} \\
&= \lim_{N \to \infty}3[\frac{1}{4} - \frac{1}{N + 1}] \\
&= 3[\frac{1}{4} - 0] \\
&= \frac{3}{4}
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-53560
content: |-
  Calculate

  $\displaystyle \sum_{n=5}^{\infty}\frac{1}{n(n + 1)}$.
options:
- id: a
  content: |-
    $\frac{1}{2}$
- id: b
  content: |-
    $5$
- id: c
  content: |-
    $1$
- id: d
  correct: true
  content: |-
    $\frac{1}{5}$
- id: e
  content: |-
    $\frac{2}{3}$
```

---

**Question 2:**

```quiz
type: radio
id: ma-53570
content: |-
  What is $\displaystyle \sum_{n=4}^{\infty}\frac{12}{n(n + 1)}$?
options:
- id: a
  content: |-
    $16$
- id: b
  correct: true
  content: |-
    $3$
- id: c
  content: |-
    $4$
- id: d
  content: |-
    $12$
- id: e
  content: |-
    $\frac{1}{3}$
```

---

<a id="calculating-the-sum-of-a-series-whose-denominator-is-the-product-of-two-consecutive-expressions"></a>
## Calculating the Sum of a Series Whose Denominator Is the Product of Two Consecutive Expressions

**Example:** Calculate $\displaystyle \sum\limits_{n = 1}^\infty \dfrac{1}{(n+2)(n+3)}$.

**Explanation**

Using partial fractions, we have

$$
\dfrac{1}{(n+2)(n+3)} = \dfrac{1}{n+2} - \dfrac{1}{n+3}
$$

So, our series can be written as

$$
\displaystyle \sum\limits_{n = 1}^\infty \left(\dfrac{1}{n+2} - \dfrac{1}{n+3}\right)
$$

Let's now compute the first few partial sums:

$$
\begin{aligned}
s_{1} &= (\frac{1}{3} - \frac{1}{4}) \\
s_{2} &= (\frac{1}{3} - \frac{1}{4}) + (\frac{1}{4} - \frac{1}{5}) \\
s_{3} &= (\frac{1}{3} - \frac{1}{4}) + (\frac{1}{4} - \frac{1}{5}) + (\frac{1}{5} - \frac{1}{6}) \\
s_{4} &= (\frac{1}{3} - \frac{1}{4}) + (\frac{1}{4} - \frac{1}{5}) + (\frac{1}{5} - \frac{1}{6}) + (\frac{1}{6} - \frac{1}{7})
\end{aligned}
$$

Notice that in each partial sum, we always end up canceling all terms except for the first and last terms. Therefore, the $N$th partial sum is

$$
s_N = \dfrac{1}{3} - \dfrac{1}{N+3}
$$

Finally, we can determine the sum of the series by taking the limit of $s_N$:

$$
\begin{aligned}
\sum_{n=1}^{\infty}\frac{1}{(n + 2)(n + 3)} &= \lim_{N \to \infty}s_{N} \\
&= \lim_{N \to \infty}(\frac{1}{3} - \frac{1}{N + 3}) \\
&= \frac{1}{3} - 0 \\
&= \frac{1}{3}
\end{aligned}
$$

---

**Question 3**

```quiz
type: radio
id: ma-49675
content: |-
  Calculate
  $\displaystyle \sum_{n=0}^{\infty}\frac{2}{(n + 1)(n + 2)}$.

  *Hint: Use the fact that $\frac{1}{(n + 1)(n + 2)} = \frac{1}{n + 1} - \frac{1}{n + 2}$.*
options:
- id: a
  content: |-
    $\frac{1}{4}$
- id: b
  content: |-
    $\frac{1}{2}$
- id: c
  correct: true
  content: |-
    $2$
- id: d
  content: |-
    $1$
- id: e
  content: |-
    The series diverges
```

---

**Question 4:**

```quiz
type: radio
id: ma-16122
content: |-
  Calculate $\displaystyle \sum_{n=2}^{\infty}\frac{5}{n(n - 1)}$.
options:
- id: a
  content: |-
    $2$
- id: b
  correct: true
  content: |-
    $5$
- id: c
  content: |-
    The series diverges
- id: d
  content: |-
    $3$
- id: e
  content: |-
    $4$
```

---

**Question 5**

```quiz
type: radio
id: ma-49685
content: |-
  Calculate
  $\displaystyle \sum_{n=1}^{\infty}\frac{1}{n^{2} + 5n + 6}$.

  *Hint: Try to factor the denominator first.*
options:
- id: a
  correct: true
  content: |-
    $\frac{1}{3}$
- id: b
  content: |-
    $1$
- id: c
  content: |-
    $\frac{1}{2}$
- id: d
  content: |-
    The series diverges
- id: e
  content: |-
    $\frac{1}{4}$
```

---

<a id="calculating-the-sum-of-a-series-whose-denominator-is-the-product-of-two-non-consecutive-expressions-xaxa2"></a>
## Calculating the Sum of a Series Whose Denominator Is the Product of Two Non-Consecutive Expressions (x+a)(x+a+2)

**Example:** Calculate $\displaystyle \sum_{m = 1}^\infty \dfrac 1 {m(m +2)}$.

**Explanation**

We can use partial fractions to show that

$$
\dfrac{1}{m(m+2)} = \dfrac{1}{2}\left(\dfrac{1}{m} - \dfrac{1}{m+2}\right)
$$

So, our series can be written as

$$
\sum_{m = 1}^\infty \dfrac 1 2\left(\dfrac 1 m - \dfrac 1 {m + 2}\right) = \dfrac{1}{2} \sum_{m = 1}^\infty \left(\dfrac 1 m - \dfrac 1 {m + 2}\right)
$$

Let's compute the first few partial sums:

$$
\begin{aligned}
s_{1} &= \frac{1}{2}(\frac{1}{1} - \frac{1}{3}) \\
s_{2} &= \frac{1}{2}[(\frac{1}{1} - \frac{1}{3}) + (\frac{1}{2} - \frac{1}{4})] \\
s_{3} &= \frac{1}{2}[(\frac{1}{1} - \frac{1}{3}) + (\frac{1}{2}- \frac{1}{4}) + (\frac{1}{3}- \frac{1}{5})] \\
s_{4} &= \frac{1}{2}[(\frac{1}{1} - \frac{1}{3}) + (\frac{1}{2} - \frac{1}{4}) + (\frac{1}{3}- \frac{1}{5}) + (\frac{1}{4}- \frac{1}{6})] \\
s_{5} &= \frac{1}{2}[(\frac{1}{1} - \frac{1}{3}) + (\frac{1}{2} - \frac{1}{4}) + (\frac{1}{3} - \frac{1}{5}) + (\frac{1}{4} - \frac{1}{6}) + (\frac{1}{5} - \frac{1}{7})]
\end{aligned}
$$

We notice that all of the terms cancel except the

$$
{\color{blue}{\dfrac 1 1}}, {\color{blue}{\dfrac 1 2}}
$$

and the

$$
{\color{red}{-\dfrac 1 {N+1}}}
$$

and

$$
{\color{red}{-\dfrac 1 {N+2}}}
$$

terms. Therefore, the $N$th partial sum is

$$
s_N = \dfrac 1 2\left[{\color{blue}{\dfrac 1 1}} + {\color{blue}{\dfrac 1 2}} {\color{red}{-\dfrac 1 {N+1}}} {\color{red}{-\dfrac 1 {N+2}}}\right]
$$

Finally, we can determine the sum of the series by taking the limit of $s_N$:

$$
\begin{aligned}
\lim_{N \to \infty}s_{N} &= \lim_{N \to \infty}\frac{1}{2}[\frac{1}{1} + \frac{1}{2} - \frac{1}{N + 1} - \frac{1}{N + 2}] \\
&= \frac{1}{2}\lim_{N \to \infty}[\frac{1}{1} + \frac{1}{2} - \frac{1}{N + 1} - \frac{1}{N + 2}] \\
&= \frac{1}{2}[\frac{1}{1} + \frac{1}{2} - 0 - 0] \\
&= \frac{1}{2}[\frac{1}{1} + \frac{1}{2}] \\
&= \frac{1}{2} \cdot \frac{3}{2} \\
&= \frac{3}{4}
\end{aligned}
$$

---

**Question 6**

```quiz
type: radio
id: ma-83586
content: |-
  Calculate
  $\displaystyle \sum_{n=1}^{\infty}\frac{4}{(n + 3)(n + 5)}$.

  *Hint: Use the fact that $\frac{1}{(n + 3)(n + 5)} = \frac{1}{2}(\frac{1}{n + 3} - \frac{1}{n + 5})$.*
options:
- id: a
  content: |-
    The series diverges
- id: b
  content: |-
    $\frac{7}{24}$
- id: c
  content: |-
    $\frac{7}{12}$
- id: d
  correct: true
  content: |-
    $\frac{9}{10}$
- id: e
  content: |-
    $\frac{9}{5}$
```

---

**Question 7:**

```quiz
type: radio
id: ma-83567
content: |-
  Calculate

  $\displaystyle \sum_{n=3}^{\infty}\frac{5}{(n + 1)(n + 3)}$.
options:
- id: a
  content: |-
    $\frac{35}{24}$
- id: b
  correct: true
  content: |-
    $\frac{9}{8}$
- id: c
  content: |-
    $\frac{25}{12}$
- id: d
  content: |-
    The series is divergent
- id: e
  content: |-
    $\frac{9}{4}$
```

---

**Question 8**

```quiz
type: radio
id: ma-83570
content: |-
  Calculate
  $\displaystyle \sum_{n=2}^{\infty}\frac{8}{n^{2} + 6n + 8}$.

  *Hint: Try to factor the denominator first.*
options:
- id: a
  content: |-
    $\frac{8}{3}$
- id: b
  correct: true
  content: |-
    $\frac{9}{5}$
- id: c
  content: |-
    The series is divergent
- id: d
  content: |-
    $\frac{18}{5}$
- id: e
  content: |-
    $\frac{5}{3}$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
