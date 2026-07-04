# Finding the Sum of an Infinite Geometric Series

<!--
lesson-id: 691
topic-code: MF3.1.4.7
-->

## Table of Contents

- [Introduction](#introduction)
- [Calculating the Sum to Infinity of a Geometric Series Expressed Using Fractions](#calculating-the-sum-to-infinity-of-a-geometric-series-expressed-using-fractions)
- [Calculating the Sum to Infinity of a Geometric Series Expressed Using Decimals](#calculating-the-sum-to-infinity-of-a-geometric-series-expressed-using-decimals)
- [Calculating the Sum to Infinity of a Geometric Series Given Two of Its Terms](#calculating-the-sum-to-infinity-of-a-geometric-series-given-two-of-its-terms)
- [Justification of the Formula](#justification-of-the-formula)

## Prerequisites

- [Infinite Series and Partial Sums](<1.4.3. Infinite Series and Partial Sums.md>)

---

<a id="introduction"></a>
## Introduction

The sum $S_\infty$ of an infinite geometric series with first term $a_1$ and common ratio $r$ can be computed using the formula

$$
S_\infty = \dfrac{a_1}{1-r}, \qquad \mid r \mid < 1
$$

Note that $\mid r \mid < 1$ is a very important condition for the sum to exist. If the condition $\mid r \mid <1$ is *not* satisfied, then the formula does *not* work!

For example, suppose we want to calculate the sum of the infinite geometric series

$$
3 + 1 + \dfrac 1 3 + \dfrac 1 9 + \dfrac{1}{27} + \cdots\,
$$

The first term is $a_1=3$, and the common ratio is

$$
r = \dfrac{a_2}{a_1} = \dfrac{1}{3}
$$

Indeed, we have $\mid r \mid <1$. Therefore, the sum is

$$
\begin{aligned}
S_{∞} &= \frac{a_{1}}{1 - r} \\
&= (3)/((1 - \frac{1}{3})) \\
&= (3)/((\frac{2}{3})) \\
&= 3(\frac{3}{2}) \\
&= \frac{9}{2}
\end{aligned}
$$

Therefore, we conclude that

$$
3 + 1 + \dfrac 1 3 + \dfrac 1 9 + \dfrac{1}{27} + \cdots = \dfrac{9}{2}
$$

---

<a id="calculating-the-sum-to-infinity-of-a-geometric-series-expressed-using-fractions"></a>
## Calculating the Sum to Infinity of a Geometric Series Expressed Using Fractions

**Example:** Calculate the sum to infinity of the geometric series $1 - \dfrac{1}{4} + \dfrac{1}{16} - \dfrac{1}{64} + \dots$.

**Explanation**

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$
S_\infty = \dfrac{a_1}{1-r}, \qquad \mid r \mid < 1
$$

where $a_1$ is the first term and $r$ is the common ratio.

For the given geometric series, the first term is $a_1 = 1$ and the common ratio is

$$
r = \dfrac{a_2}{a_1} = \frac{\left(-\dfrac{1}{4}\right)}{1} =-\dfrac{1}{4}
$$

So, using the formula, we find that the sum to infinity is

$$
\begin{aligned}
S_{∞} &= \frac{a_{1}}{1 - r} \\
&= (1)/(1 - (-\frac{1}{4})) \\
&= (1)/((\frac{5}{4})) \\
&= \frac{4}{5}
\end{aligned}
$$

---

**Question 1:** Calculate the sum to infinity of the geometric series $-8 - 6 - \frac{9}{2} - \frac{27}{8} - ⋯$

- [ ] A. $-32$
- [ ] B. $-12$
- [ ] C. $-22$
- [ ] D. $-16$
- [ ] E. $-24$

---

**Question 2:** Calculate the sum to infinity of the geometric series $30 + 9 + \frac{27}{10} + \frac{81}{100} + ⋯$

- [ ] A. $\frac{300}{7}$
- [ ] B. $\frac{410}{8}$
- [ ] C. $32$
- [ ] D. $38$
- [ ] E. $42$

---

<a id="calculating-the-sum-to-infinity-of-a-geometric-series-expressed-using-decimals"></a>
## Calculating the Sum to Infinity of a Geometric Series Expressed Using Decimals

**Example:** Calculate the sum to infinity of the geometric series $0.25 + 0.125 + 0.062\ 5 + 0.031\ 25 + \dots$.

**Explanation**

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$
S_\infty = \dfrac{a_1}{1-r}, \qquad \mid r \mid < 1
$$

where $a_1$ is the first term and $r$ is the common ratio.

For the given geometric series, the first term is $a_1 = 0.25$ and the common ratio is

$$
r = \dfrac{a_2}{a_1} = \frac{0.125}{0.25} = 0.5
$$

So, using the formula, we find that the sum to infinity is

$$
\begin{aligned}
S_{∞} &= \frac{a_{1}}{1 - r} \\
&= \frac{0.25}{1 - 0.5} \\
&= \frac{0.25}{0.5} \\
&= 0.5
\end{aligned}
$$

---

**Question 3**

> A calculator is required to answer this question.

Calculate the sum to infinity of the geometric series $6 - 0.12 + 0.0024 - 0.000048 + ⋯$

- [ ] A. $\frac{103}{19}$
- [ ] B. $\frac{100}{17}$
- [ ] C. $\frac{153}{25}$
- [ ] D. $5$
- [ ] E. $\frac{109}{18}$

---

**Question 4**

> A calculator is required to answer this question.

Calculate the sum to infinity of the geometric series $1.8 + 0.9 + 0.45 + 0.225 + ⋯$

- [ ] A. $1.8$
- [ ] B. $3.6$
- [ ] C. $3.3$
- [ ] D. $3.9$
- [ ] E. $4.5$

---

<a id="calculating-the-sum-to-infinity-of-a-geometric-series-given-two-of-its-terms"></a>
## Calculating the Sum to Infinity of a Geometric Series Given Two of Its Terms

**Example:** Consider the infinite geometric sequence that has a first term equal to $4$ and a fourth term equal to $\dfrac{1}{16}$. What is the sum to infinity of the terms of this sequence?

**Explanation**

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$
S_\infty = \dfrac{a_1}{1-r}, \qquad \mid r \mid < 1
$$

where $a_1$ is the first term and $r$ is the common ratio.

From the question statement we have $a_1=4$ and

$$
a_4=\dfrac{1}{16}
$$

We can find the common ratio using the following formula:

$$
r^{n-m} = \dfrac{a_n}{a_m}
$$

Substituting the known information into the above gives:

$$
\begin{aligned}
r^{4 - 1} &= ((\frac{1}{16}))/(4) \\
r^{3} &= \frac{1}{64} \\
r^{3} &= (\frac{1}{4})^{3} \\
r &= \frac{1}{4}
\end{aligned}
$$

So, using the formula, we find that the sum to infinity is

$$
\begin{aligned}
S_{∞} &= \frac{a_{1}}{1 - r} \\
&= (4)/((1 - \frac{1}{4})) \\
&= (4)/((\frac{3}{4})) \\
&= 4(\frac{4}{3}) \\
&= \frac{16}{3}
\end{aligned}
$$

---

**Question 5**

> A scientific calculator is required to answer this question.

Consider the infinite geometric sequence that has a first term equal to $6$ and a fourth term equal to $\frac{3}{4}$. What is the sum to infinity of the terms of this sequence?

- [ ] A. $14$
- [ ] B. $10$
- [ ] C. $12$
- [ ] D. $22$
- [ ] E. $9$

---

**Question 6**

> A scientific calculator is required to answer this question.

Consider the positive infinite geometric sequence that has a first term equal to $18$ and a third term equal to $2$. What is the sum to infinity of the terms of this sequence?

- [ ] A. $27$
- [ ] B. $36$
- [ ] C. $18$
- [ ] D. $24$
- [ ] E. $21$

---

<a id="justification-of-the-formula"></a>
## Justification of the Formula

We've been using the following formula for the sum to infinity of a geometric series with first term $a_1$ and common ratio $r$:

$$
S_\infty = \dfrac{a_1}{1-r}, \qquad \mid r \mid < 1
$$

To see where this formula comes from, first, we remember the formula for the sum of the first $n$ terms of a geometric series is given by

$$
S_n = a_1 \cdot \dfrac {1 - r ^ n} {1 - r}
$$

Notice that if $\mid r \mid < 1$ then $r^n\to 0$ as $n\to\infty$. Therefore, as $n\to\infty$, we have:

$$
S_{n} \mid → a_{1} \cdot \frac{1 - 0}{1 - r}; = a_{1} \cdot \frac{1}{1 - r}; = \frac{a_{1}}{1 - r}; = S_{∞}
$$

```update-progress
```

[[MA/MF3/Home|Home]]
[[MA/MF3/0. Table of Contents/TOC|Table of Contents]]
