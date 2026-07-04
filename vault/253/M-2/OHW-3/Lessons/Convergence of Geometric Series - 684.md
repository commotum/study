# Convergence of Geometric Series

<!--
lesson-id: 684
topic-code: MF3.1.4.10
-->

## Table of Contents

- [Introduction](#introduction)
- [Determining Whether a Geometric Series Given in Sigma Notation Converges](#determining-whether-a-geometric-series-given-in-sigma-notation-converges)
- [Determining the Convergence of a Geometric Series With an Arbitrary Starting Index](#determining-the-convergence-of-a-geometric-series-with-an-arbitrary-starting-index)
- [Identifying Convergent Geometric Series](#identifying-convergent-geometric-series)
- [Calculating the Range of Values of a Parameter for Which a Geometric Series Converges](#calculating-the-range-of-values-of-a-parameter-for-which-a-geometric-series-converges)

## Prerequisites

- [Writing an Infinite Geometric Series in Sigma Notation](<1.4.8. Writing an Infinite Geometric Series in Sigma Notation.md>)
- [Solving Inequalities Involving Exponential Functions](<../../../2. Inequalities/2.1. Single-Variable Inequalities/Lessons/2.1.12. Solving Inequalities Involving Exponential Functions.md>)
- [Further Convergence of Geometric Sequences](<1.4.2. Further Convergence of Geometric Sequences.md>)

---

<a id="introduction"></a>
## Introduction

In general, a geometric series with common ratio $r$ is

- convergent if $\mid r \mid <1$, and
- divergent if $\mid r \mid \geq 1$.

For example, consider the series

$$
4+2+1+\dfrac 12+ \cdots
$$

The common ratio is

$$
\begin{aligned}
r &= \frac{2}{4} = \frac{1}{2}
\end{aligned}
$$

so $\mid r \mid <1$ and therefore the series converges. (This makes sense intuitively, because the magnitude of the terms keeps getting smaller.)

On the other hand, consider the series

$$
1-3+9-27+\cdots
$$

The common ratio is

$$
\begin{aligned}
r &= ((-3))/(1) =-3
\end{aligned}
$$

so $\mid r \mid >1$ and therefore the series diverges. (This makes sense intuitively, because the magnitude of the terms keeps getting bigger.)

**Note:** If

$$
\begin{aligned}
\mid r &= 1
\end{aligned}
$$

then the series diverges. For example, consider the series

$$
0.001+0.001+0.001+0.001+\cdots
$$

The common ratio is

$$
\begin{aligned}
r &= \frac{0.001}{0.001} = 1
\end{aligned}
$$

so

$$
\begin{aligned}
\mid r &= 1
\end{aligned}
$$

and therefore the series diverges. (This makes sense intuitively, because the terms are not approaching $0$.)

---

<a id="determining-whether-a-geometric-series-given-in-sigma-notation-converges"></a>
## Determining Whether a Geometric Series Given in Sigma Notation Converges

**Example:** Determine whether the following geometric series converges or diverges.
$S = \sum_{n=1}^\infty \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{n+1}$

**Explanation**

The series starts with $n=1$. So the common ratio is

$$
\begin{aligned}
r = \frac{a_{2}}{a_{1}} &= (\frac{5}{2}(\frac{1}{2})^{2 + 1})/(\frac{5}{2}(\frac{1}{2})^{1 + 1}) \\
&= (\frac{5}{2}(\frac{1}{2})^{3})/(\frac{5}{2}(\frac{1}{2})^{2}) \\
&= \frac{1}{2}
\end{aligned}
$$

Therefore, the series is convergent because $\mid r \mid <1$.

---

**Question 1:** Which of the following statements is true regarding the series $∑_(n = 1)^(∞)2(0.25)^{2n}$?

- [ ] A. The series is convergent because $\mid r \mid \ge 1$
- [ ] B. Inconclusive because $\mid r|= 1$
- [ ] C. The series is divergent because $\mid r \mid < 1$
- [ ] D. The series is divergent because $\mid r \mid \ge 1$
- [ ] E. The series is convergent because $\mid r \mid < 1$

---

**Question 2:** Which of the following statements is true regarding the series $∑_(n = 1)^(∞)9(4)^{n}$?

- [ ] A. The series is divergent because $\mid r \mid < 1$.
- [ ] B. Inconclusive because $\mid r|= 1$.
- [ ] C. The series is divergent because $\mid r \mid \ge 1$.
- [ ] D. The series is convergent because $\mid r \mid < 1$.
- [ ] E. The series is convergent because $\mid r \mid \ge 1$.

---

<a id="determining-the-convergence-of-a-geometric-series-with-an-arbitrary-starting-index"></a>
## Determining the Convergence of a Geometric Series With an Arbitrary Starting Index

**Example:** Determine whether the following geometric series converges or diverges.
$\sum_{n=0}^\infty {3}\left(\dfrac{3}{2}\right)^{n}$

**Explanation**

The series starts with $n=0$. So the common ratio is

$$
\begin{aligned}
r = \frac{a_{1}}{a_{0}} &= (3(\frac{3}{2})^{1})/(3(\frac{3}{2})^{0}) \\
&= \frac{3}{2}
\end{aligned}
$$

Therefore, the series is divergent because

$$
\mid r \mid \geq 1
$$

---

**Question 3:** Which of the following statements is true regarding the series $∑_(n = 0)^(∞)(5)^{n}$?

- [ ] A. The series is divergent because $\mid r \mid \ge 1$.
- [ ] B. Inconclusive because $\mid r|= 1$.
- [ ] C. The series is divergent because $\mid r \mid < 1$.
- [ ] D. The series is convergent because $\mid r \mid \ge 1$.
- [ ] E. The series is convergent because $\mid r \mid < 1$.

---

**Question 4:** Which of the following statements is true regarding the series $∑_(n = 2)^(∞)(\frac{1}{4})^{n}$?

- [ ] A. The series is divergent because $\mid r \mid < 1$.
- [ ] B. The series is convergent because $\mid r \mid < 1$.
- [ ] C. The series is convergent because $\mid r \mid \ge 1$.
- [ ] D. Inconclusive because $\mid r|= 1$.
- [ ] E. The series is divergent because $\mid r \mid \ge 1$.

---

<a id="identifying-convergent-geometric-series"></a>
## Identifying Convergent Geometric Series

**Example:** Which of the following geometric series converge?

1. $\displaystyle{\sum_{n = 1}^ \infty} 4 (-3)^{n}$
2. $\displaystyle{\sum_{n = 6}^\infty} 32 \left(\dfrac{1}{2}\right)^{4n}$
3. $\displaystyle{\sum_{n=0}^{\infty}} \dfrac{4^n}{2^{n+3}}$

**Explanation**

Let's look at each series in turn.

- The series $\displaystyle{\sum_{n = 1}^ \infty} 4 (-3)^{n}$ starts with $n=1$. So the common ratio is
$r = \frac{a_{2}}{a_{1}}|= (4(-3)^{2})/(4(-3)^{1}); =-3$.
Therefore, the series is divergent because $\mid r \mid \geq 1$.
- The series $\displaystyle{\sum_{n = 6}^\infty} 32 \left(\dfrac{1}{2}\right)^{4n}$ starts with $n=6$. So the common ratio is
$r = \frac{a_{7}}{a_{6}}|= (32(\frac{1}{2})^{4(7)})/(32(\frac{1}{2})^{4(6)}); = (32(\frac{1}{2})^{28})/(32(\frac{1}{2})^{24}); = (\frac{1}{2})^{4}; = \frac{1}{16}$.
Therefore, the series is convergent because $\mid r \mid < 1$.
- The series $\displaystyle{\sum_{n=0}^{\infty}} \dfrac{4^n}{2^{n+3}}$ starts with $n=0$. So the common ratio is
$r = \frac{a_{1}}{a_{0}}|= ((\frac{4^{1}}{2^{1 + 3}}))/((\frac{4^{0}}{2^{0 + 3}})); = ((\frac{4^{1}}{2^{4}}))/((\frac{4^{0}}{2^{3}})); = (\frac{4^{1}}{2^{4}})(\frac{2^{3}}{4^{0}}); = \frac{4}{2}; = 2$.
Therefore, the series is divergent because $\mid r \mid \geq 1$.

In conclusion, only series II converges.

---

**Question 5**

Which of the following geometric series converge?

1. $∑_(n = 2)^(∞)5(\frac{3}{2})^{n}$
2. $∑_(n = 1)^(∞)\frac{1}{5}(\frac{2}{3})^{n}$
3. $∑_(n = 3)^(∞)\frac{4^{n + 2}}{2^{n - 1}}$

- [ ] A. II only
- [ ] B. II and III only
- [ ] C. I and II only
- [ ] D. III only
- [ ] E. I only

---

**Question 6**

Which of the following geometric series converge?

1. $∑_(n = 6)^(∞)(0.6)(-0.7)^{n}$
2. $∑_(n = 4)^(∞)(\frac{1}{5})(\frac{5}{3})^{n}$
3. $∑_(n = 7)^(∞)\frac{4^{2n}}{8^{n + 1}}$

- [ ] A. I and II only
- [ ] B. II only
- [ ] C. II and III only
- [ ] D. I only
- [ ] E. III only

---

<a id="calculating-the-range-of-values-of-a-parameter-for-which-a-geometric-series-converges"></a>
## Calculating the Range of Values of a Parameter for Which a Geometric Series Converges

**Example:** For which values of $k$ does the series $\displaystyle\sum_{n=1}^\infty\dfrac{3(2)^{kn}}{4^n}$ converge?

**Explanation**

First, we rewrite the series so that it's in the form

$$
\displaystyle\sum_{n=1}^\infty a r^n
$$

as follows:

$$
\begin{aligned}
∑_(n = 1)^(∞)(3(2)^{kn})/(4^{n}) &= ∑_(n = 1)^(∞)(3(2^{k})^{n})/(4^{n}) \\
&= ∑_(n = 1)^(∞)3((2^{k})^{n})/(4^{n}) \\
&= ∑_(n = 1)^(∞)3(\frac{2^{k}}{4})^{n}
\end{aligned}
$$

We see that this is a geometric series with a common ratio of

$$
r = \dfrac{2^k}{4}
$$

For the series to converge, we require $\mid r \mid < 1$. Therefore, we have

$$
\mid \frac{2^{k}}{4} \mid \mid < 1; \frac{2^{k}}{4}\begin{vmatrix}< 1 \\ 2^{k}\end{vmatrix}< 4
$$

Notice that we could remove the absolute value bars because

$$
\dfrac{2^k}{4}
$$

is always positive.

The equation $2^k = 4$ has the solution $k=2$. Now, since $2^k$ increases as $k$ increases, the solution to $2^k < 4$ must be $k < 2$.

---

**Question 7:** For which values of $k$ does the series $∑_(n = 1)^(∞)\frac{3^{2n + 1}}{9^{kn}}$ converge?

- [ ] A. $k > 0$
- [ ] B. $k > 3$
- [ ] C. $k > 1$
- [ ] D. $k < 1$
- [ ] E. $k < 0$

---

**Question 8:** For which values of $k$ does the series $∑_(n = 1)^(∞)(\frac{3^{k}}{27})^{n}$ converge?

- [ ] A. $k < 3$
- [ ] B. $k > 0$
- [ ] C. $k < 9$
- [ ] D. $k > 3$
- [ ] E. $k < 0$

```update-progress
```

[[MA/Mathematical-Foundations/MF3/Home|Home]]
[[MA/Mathematical-Foundations/MF3/0. Table of Contents/TOC|Table of Contents]]
