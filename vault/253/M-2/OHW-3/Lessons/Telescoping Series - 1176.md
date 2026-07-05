# Telescoping Series

<!--
lesson-id: 1176
topic-code: Calc2.4.3.5
-->

## Table of Contents

- [Introduction](#introduction)
- [Calculating the Sum of a Series Whose Denominator Is the Product of N and N+1](#calculating-the-sum-of-a-series-whose-denominator-is-the-product-of-n-and-n1)
- [Calculating the Sum of a Series Whose Denominator Is the Product of Two Consecutive Expressions](#calculating-the-sum-of-a-series-whose-denominator-is-the-product-of-two-consecutive-expressions)
- [Calculating the Sum of a Series Whose Denominator Is the Product of Two Non-Consecutive Expressions (x+a)(x+a+2)](#calculating-the-sum-of-a-series-whose-denominator-is-the-product-of-two-non-consecutive-expressions-xaxa2)

## Prerequisites

- [Convergent and Divergent Infinite Series](../982/982.md)
- [Expressing Rational Functions as Sums of Partial Fractions](../1060/1060.md)

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
∑_(n = 1)^(∞)(1)/(n(n + 1)) &= lim_(N → ∞)(1 - \frac{1}{N + 1}) \\
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
∑_(n = 4)^(∞)(3)/(n(n + 1)) &= lim_(N → ∞)s_{N} \\
&= lim_(N → ∞)3[\frac{1}{4} - \frac{1}{N + 1}] \\
&= 3[\frac{1}{4} - 0] \\
&= \frac{3}{4}
\end{aligned}
$$

---

**Question 1:** Calculate
$∑_(n = 5)^(∞)(1)/(n(n + 1))$.

- [ ] A. $\frac{1}{2}$
- [ ] B. $5$
- [ ] C. $1$
- [ ] D. $\frac{1}{5}$
- [ ] E. $\frac{2}{3}$

---

**Question 2:** What is $∑_(n = 4)^(∞)(12)/(n(n + 1))$?

- [ ] A. $16$
- [ ] B. $3$
- [ ] C. $4$
- [ ] D. $12$
- [ ] E. $\frac{1}{3}$

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
∑_(n = 1)^(∞)(1)/((n + 2)(n + 3)) &= lim_(N → ∞)s_{N} \\
&= lim_(N → ∞)(\frac{1}{3} - \frac{1}{N + 3}) \\
&= \frac{1}{3} - 0 \\
&= \frac{1}{3}
\end{aligned}
$$

---

**Question 3**

Calculate
$∑_(n = 0)^(∞)(2)/((n + 1)(n + 2))$.

*Hint: Use the fact that $(1)/((n + 1)(n + 2)) = \frac{1}{n + 1} - \frac{1}{n + 2}$.*

- [ ] A. $\frac{1}{4}$
- [ ] B. $\frac{1}{2}$
- [ ] C. $2$
- [ ] D. $1$
- [ ] E. The series diverges

---

**Question 4:** Calculate $∑_(n = 2)^(∞)(5)/(n(n - 1))$.

- [ ] A. $2$
- [ ] B. $5$
- [ ] C. The series diverges
- [ ] D. $3$
- [ ] E. $4$

---

**Question 5**

Calculate
$∑_(n = 1)^(∞)\frac{1}{n^{2} + 5n + 6}$.

*Hint: Try to factor the denominator first.*

- [ ] A. $\frac{1}{3}$
- [ ] B. $1$
- [ ] C. $\frac{1}{2}$
- [ ] D. The series diverges
- [ ] E. $\frac{1}{4}$

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
lim_(N → ∞)s_{N} &= lim_(N → ∞)\frac{1}{2}[\frac{1}{1} + \frac{1}{2} - \frac{1}{N + 1} - \frac{1}{N + 2}] \\
&= \frac{1}{2}lim_(N → ∞)[\frac{1}{1} + \frac{1}{2} - \frac{1}{N + 1} - \frac{1}{N + 2}] \\
&= \frac{1}{2}[\frac{1}{1} + \frac{1}{2} - 0 - 0] \\
&= \frac{1}{2}[\frac{1}{1} + \frac{1}{2}] \\
&= \frac{1}{2} \cdot \frac{3}{2} \\
&= \frac{3}{4}
\end{aligned}
$$

---

**Question 6**

Calculate
$∑_(n = 1)^(∞)(4)/((n + 3)(n + 5))$.

*Hint: Use the fact that $(1)/((n + 3)(n + 5)) = \frac{1}{2}(\frac{1}{n + 3} - \frac{1}{n + 5})$.*

- [ ] A. The series diverges
- [ ] B. $\frac{7}{24}$
- [ ] C. $\frac{7}{12}$
- [ ] D. $\frac{9}{10}$
- [ ] E. $\frac{9}{5}$

---

**Question 7:** Calculate
$∑_(n = 3)^(∞)(5)/((n + 1)(n + 3))$.

- [ ] A. $\frac{35}{24}$
- [ ] B. $\frac{9}{8}$
- [ ] C. $\frac{25}{12}$
- [ ] D. The series is divergent
- [ ] E. $\frac{9}{4}$

---

**Question 8**

Calculate
$∑_(n = 2)^(∞)\frac{8}{n^{2} + 6n + 8}$.

*Hint: Try to factor the denominator first.*

- [ ] A. $\frac{8}{3}$
- [ ] B. $\frac{9}{5}$
- [ ] C. The series is divergent
- [ ] D. $\frac{18}{5}$
- [ ] E. $\frac{5}{3}$
