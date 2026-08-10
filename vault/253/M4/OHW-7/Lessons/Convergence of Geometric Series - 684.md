# Convergence of Geometric Series

<!--
lesson-id: 684
topic-code: CA2.4.4.4
-->

## Table of Contents

- [Introduction](#introduction)
- [Determining Whether a Geometric Series Given in Sigma Notation Converges](#determining-whether-a-geometric-series-given-in-sigma-notation-converges)
- [Determining the Convergence of a Geometric Series With an Arbitrary Starting Index](#determining-the-convergence-of-a-geometric-series-with-an-arbitrary-starting-index)
- [Identifying Convergent Geometric Series](#identifying-convergent-geometric-series)
- [Calculating the Range of Values of a Parameter for Which a Geometric Series Converges](#calculating-the-range-of-values-of-a-parameter-for-which-a-geometric-series-converges)

## Prerequisites

- [Writing an Infinite Geometric Series in Sigma Notation](<../../../../MA/Mathematical-Foundations/MF3/1. Sequences and Series/1.4. Infinite Series/Lessons/1.4.8. Writing an Infinite Geometric Series in Sigma Notation.md>)
- [Solving Inequalities Involving Exponential Functions](<../../../../MA/Mathematical-Foundations/MF3/2. Inequalities/2.1. Single-Variable Inequalities/Lessons/2.1.12. Solving Inequalities Involving Exponential Functions.md>)
- [Further Convergence of Geometric Sequences](<../../../../MA/Mathematical-Foundations/MF3/1. Sequences and Series/1.4. Infinite Series/Lessons/1.4.2. Further Convergence of Geometric Sequences.md>)

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
r &= \frac{(-3)}{1} =-3
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
$\displaystyle S = \sum_{n=1}^\infty \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{n+1}$

**Explanation**

The series starts with $n=1$. So the common ratio is

$$
\begin{aligned}
r = \frac{a_{2}}{a_{1}} &= \frac{\frac{5}{2}(\frac{1}{2})^{2 + 1}}{\frac{5}{2}(\frac{1}{2})^{1 + 1}} \\
&= \frac{\frac{5}{2}(\frac{1}{2})^{3}}{\frac{5}{2}(\frac{1}{2})^{2}} \\
&= \frac{1}{2}
\end{aligned}
$$

Therefore, the series is convergent because $\mid r \mid <1$.

---

**Question 1:**

```quiz
type: radio
id: ma-40574
content: |-
  Which of the following statements is true regarding the series $\displaystyle \sum_{n=1}^{\infty}2(0.25)^{2n}$?
options:
- id: a
  content: |-
    The series is convergent because $\mid r \mid \ge 1$
- id: b
  content: |-
    Inconclusive because $\lvert r\rvert = 1$
- id: c
  content: |-
    The series is divergent because $\mid r \mid < 1$
- id: d
  content: |-
    The series is divergent because $\mid r \mid \ge 1$
- id: e
  content: |-
    The series is convergent because $\mid r \mid < 1$
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: ma-14101
content: |-
  Which of the following statements is true regarding the series $\displaystyle \sum_{n=1}^{\infty}9(4)^{n}$?
options:
- id: a
  content: |-
    The series is divergent because $\mid r \mid < 1$.
- id: b
  content: |-
    Inconclusive because $\lvert r\rvert = 1$.
- id: c
  content: |-
    The series is divergent because $\mid r \mid \ge 1$.
  correct: true
- id: d
  content: |-
    The series is convergent because $\mid r \mid < 1$.
- id: e
  content: |-
    The series is convergent because $\mid r \mid \ge 1$.
```

---

<a id="determining-the-convergence-of-a-geometric-series-with-an-arbitrary-starting-index"></a>
## Determining the Convergence of a Geometric Series With an Arbitrary Starting Index

**Example:** Determine whether the following geometric series converges or diverges.
$\displaystyle \sum_{n=0}^\infty {3}\left(\dfrac{3}{2}\right)^{n}$

**Explanation**

The series starts with $n=0$. So the common ratio is

$$
\begin{aligned}
r = \frac{a_{1}}{a_{0}} &= \frac{3(\frac{3}{2})^{1}}{3(\frac{3}{2})^{0}} \\
&= \frac{3}{2}
\end{aligned}
$$

Therefore, the series is divergent because

$$
\mid r \mid \geq 1
$$

---

**Question 3:**

```quiz
type: radio
id: ma-13583
content: |-
  Which of the following statements is true regarding the series $\displaystyle \sum_{n=0}^{\infty}(5)^{n}$?
options:
- id: a
  content: |-
    The series is divergent because $\mid r \mid \ge 1$.
  correct: true
- id: b
  content: |-
    Inconclusive because $\lvert r\rvert = 1$.
- id: c
  content: |-
    The series is divergent because $\mid r \mid < 1$.
- id: d
  content: |-
    The series is convergent because $\mid r \mid \ge 1$.
- id: e
  content: |-
    The series is convergent because $\mid r \mid < 1$.
```

---

**Question 4:**

```quiz
type: radio
id: ma-5456
content: |-
  Which of the following statements is true regarding the series $\displaystyle \sum_{n=2}^{\infty}(\frac{1}{4})^{n}$?
options:
- id: a
  content: |-
    The series is divergent because $\mid r \mid < 1$.
- id: b
  content: |-
    The series is convergent because $\mid r \mid < 1$.
  correct: true
- id: c
  content: |-
    The series is convergent because $\mid r \mid \ge 1$.
- id: d
  content: |-
    Inconclusive because $\lvert r\rvert = 1$.
- id: e
  content: |-
    The series is divergent because $\mid r \mid \ge 1$.
```

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
$r = \frac{a_{2}}{a_{1}}= \frac{4(-3)^{2}}{4(-3)^{1}} = -3$.
Therefore, the series is divergent because $\mid r \mid \geq 1$.
- The series $\displaystyle{\sum_{n = 6}^\infty} 32 \left(\dfrac{1}{2}\right)^{4n}$ starts with $n=6$. So the common ratio is
$r = \frac{a_{7}}{a_{6}}= \frac{32(\frac{1}{2})^{4(7)}}{32(\frac{1}{2})^{4(6)}} = \frac{32(\frac{1}{2})^{28}}{32(\frac{1}{2})^{24}} = (\frac{1}{2})^{4} = \frac{1}{16}$.
Therefore, the series is convergent because $\mid r \mid < 1$.
- The series $\displaystyle{\sum_{n=0}^{\infty}} \dfrac{4^n}{2^{n+3}}$ starts with $n=0$. So the common ratio is
$r = \frac{a_{1}}{a_{0}}= \frac{(\frac{4^{1}}{2^{1 + 3}})}{(\frac{4^{0}}{2^{0 + 3}})} = \frac{(\frac{4^{1}}{2^{4}})}{(\frac{4^{0}}{2^{3}})} = (\frac{4^{1}}{2^{4}})(\frac{2^{3}}{4^{0}}) = \frac{4}{2} = 2$.
Therefore, the series is divergent because $\mid r \mid \geq 1$.

In conclusion, only series II converges.

---

**Question 5**

```quiz
type: radio
id: ma-50487
content: |-
  Which of the following geometric series converge?

  1. $\displaystyle \sum_{n=2}^{\infty}5(\frac{3}{2})^{n}$
  2. $\displaystyle \sum_{n=1}^{\infty}\frac{1}{5}(\frac{2}{3})^{n}$
  3. $\displaystyle \sum_{n=3}^{\infty}\frac{4^{n + 2}}{2^{n - 1}}$
options:
- id: a
  content: |-
    II only
  correct: true
- id: b
  content: |-
    II and III only
- id: c
  content: |-
    I and II only
- id: d
  content: |-
    III only
- id: e
  content: |-
    I only
```

---

**Question 6**

```quiz
type: radio
id: ma-50508
content: |-
  Which of the following geometric series converge?

  1. $\displaystyle \sum_{n=6}^{\infty}(0.6)(-0.7)^{n}$
  2. $\displaystyle \sum_{n=4}^{\infty}(\frac{1}{5})(\frac{5}{3})^{n}$
  3. $\displaystyle \sum_{n=7}^{\infty}\frac{4^{2n}}{8^{n + 1}}$
options:
- id: a
  content: |-
    I and II only
- id: b
  content: |-
    II only
- id: c
  content: |-
    II and III only
- id: d
  content: |-
    I only
  correct: true
- id: e
  content: |-
    III only
```

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
\sum_{n=1}^{\infty}\frac{3(2)^{kn}}{4^{n}} &= \sum_{n=1}^{\infty}\frac{3(2^{k})^{n}}{4^{n}} \\
&= \sum_{n=1}^{\infty}3\frac{(2^{k})^{n}}{4^{n}} \\
&= \sum_{n=1}^{\infty}3(\frac{2^{k}}{4})^{n}
\end{aligned}
$$

We see that this is a geometric series with a common ratio of

$$
r = \dfrac{2^k}{4}
$$

For the series to converge, we require $\mid r \mid < 1$. Therefore, we have

$$
\left\lvert\frac{2^k}{4}\right\rvert<1
\quad\Longrightarrow\quad
\frac{2^k}{4}<1
\quad\Longrightarrow\quad
2^k<4
$$

Notice that we could remove the absolute value bars because

$$
\dfrac{2^k}{4}
$$

is always positive.

The equation $2^k = 4$ has the solution $k=2$. Now, since $2^k$ increases as $k$ increases, the solution to $2^k < 4$ must be $k < 2$.

---

**Question 7:**

```quiz
type: radio
id: ma-40667
content: |-
  For which values of $k$ does the series $\displaystyle \sum_{n=1}^{\infty}\frac{3^{2n + 1}}{9^{kn}}$ converge?
options:
- id: a
  content: |-
    $k > 0$
- id: b
  content: |-
    $k > 3$
- id: c
  content: |-
    $k > 1$
  correct: true
- id: d
  content: |-
    $k < 1$
- id: e
  content: |-
    $k < 0$
```

---

**Question 8:**

```quiz
type: radio
id: ma-50611
content: |-
  For which values of $k$ does the series $\displaystyle \sum_{n=1}^{\infty}(\frac{3^{k}}{27})^{n}$ converge?
options:
- id: a
  content: |-
    $k < 3$
  correct: true
- id: b
  content: |-
    $k > 0$
- id: c
  content: |-
    $k < 9$
- id: d
  content: |-
    $k > 3$
- id: e
  content: |-
    $k < 0$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
