# Maclaurin Series

<!--
lesson-id: 340
topic-code: CA2.4.7.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Finding the First Few Terms of the Maclaurin Series of a Function](#finding-the-first-few-terms-of-the-maclaurin-series-of-a-function)
- [Expressing the Maclaurin Series of a Function in Sigma Notation](#expressing-the-maclaurin-series-of-a-function-in-sigma-notation)

## Prerequisites

- [Convergent and Divergent Infinite Series](<../../../../MA/Mathematical-Foundations/MF3/1. Sequences and Series/1.4. Infinite Series/Lessons/1.4.4. Convergent and Divergent Infinite Series.md>)
- [Higher-Degree Taylor Polynomials](<../../../../MA/Mathematical-Foundations/MF3/8. Differentiation/8.4. Taylor Series/Lessons/8.4.4. Higher-Degree Taylor Polynomials.md>)

---

<a id="introduction"></a>
## Introduction

The $n$th-degree Taylor polynomial of

$$
f(x)=e^x
$$

about $x=0$ is

$$
P_n(x) = 1 + x + \dfrac{x^2}{2!}+ \dfrac{x^3}{3!} + \cdots \dfrac{x^n}{n!}
$$

or in sigma notation,

$$
P_n(x)=\sum_{k=0}^n \dfrac{x^k}{k!}
$$

If we let $n\to\infty$, we get an **infinite power series,** and the series *converges to* $f(x)$. Therefore, we can write

$$
e^x = \sum_{k=0}^\infty \dfrac{x^k}{k!}
$$

The infinite series above is called the **Maclaurin series** (or **Maclaurin expansion**) of $e^x$.

This particular Maclaurin series converges for any $x\in(-\infty,\infty)$. We call this the **interval of convergence** of the series.

In general, for a function $f(x)$ that's infinitely differentiable at $x=0$, the Maclaurin series of that function is

$$
\begin{aligned}
f(x) &= f(0) + f^{′}(0)x + (f^{″}(0))/(2!)x^{2} + (f^{‴}(0))/(3!)x^{3} + ⋯ \\
&= ∑_(k = 0)^(∞)(f^{(k)}(0))/(k!)x^{k}
\end{aligned}
$$

The series converges to $f(x)$ provided that $x$ lies within the interval of convergence of the series.

In this lesson, we will state the interval of convergence for a given Maclaurin series. We will discuss how to calculate intervals of convergence in separate lessons.

---

<a id="finding-the-first-few-terms-of-the-maclaurin-series-of-a-function"></a>
## Finding the First Few Terms of the Maclaurin Series of a Function

**Example:** Find the first three non-zero terms of the Maclaurin expansion of the function $f(x) = \ln(1+x)$, valid for $[MATH: x\in(-1,1].]$

**Explanation**

The Maclaurin expansion is

$$
f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3+\cdots
$$

Computing the necessary derivatives, we get

$$
\begin{aligned}
\begin{bmatrix}f(x) &= \ln (1 + x) & ⟹ & f(0)|= \ln (1 + 0) = 0 \\ f^{′}(x)|= \frac{1}{1 + x} = (1 + x)^{-1} & ⟹ & f^{′}(0)|= (1 + 0)^{-1} = 1 \\ f^{″}(x)|= - (1)/((1 + x)^{2}) = - (1 + x)^{-2} & ⟹ & f^{″}(0)|= - (1 + 0)^{-2} =-1 \\ f^{‴}(x)|= (2)/((1 + x)^{3}) = 2(1 + x)^{-3} & ⟹ & f^{‴}(0)|= 2(1 + 0)^{-3} = 2\end{bmatrix}
\end{aligned}
$$

Therefore, the Maclaurin expansion is

$$
\begin{aligned}
\ln (1 + x) &= (0) + (1)x + ((-1))/(2!)x^{2} + ((2))/(3!)x^{3} + ⋯ \\
&= x - \frac{1}{2}x^{2} + \frac{1}{3}x^{3} + ⋯
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-12231
content: |-
  Find the first three non-zero terms of the Maclaurin expansion of the function $f(x) = \sin (πx)$.
options:
- id: a
  content: |-
    $\sin (πx) = πx - \frac{π^{3}x^{3}}{3} + \frac{π^{5}x^{5}}{5}⋯$
- id: b
  content: |-
    $\sin (πx) = x - \frac{x^{2}}{2} + \frac{x^{4}}{24}⋯$
- id: c
  content: |-
    $\sin (πx) = π - \frac{π^{2}x^{2}}{2} + \frac{π^{4}x^{4}}{24}⋯$
- id: d
  content: |-
    $\sin (πx) = πx - \frac{π^{3}x^{3}}{6} + \frac{π^{5}x^{5}}{120}⋯$
  correct: true
- id: e
  content: |-
    $\sin (πx) = x - \frac{x^{3}}{6} + \frac{x^{5}}{120}⋯$
```

---

**Question 2:**

```quiz
type: radio
id: ma-8207
content: |-
  Find the first four non-zero terms of the Maclaurin expansion of the function $f(x) = \frac{1}{1 + x}$.
options:
- id: a
  content: |-
    $\frac{1}{1 + x} = 1 - 2x + 4x^{2} - 6x^{3} + ⋯$
- id: b
  content: |-
    $\frac{1}{1 + x} = 1 + x + x^{2} + x^{3} + ⋯$
- id: c
  content: |-
    $\frac{1}{1 + x} = 1 + 2x - 3x^{2} + 6x^{3} + ⋯$
- id: d
  content: |-
    $\frac{1}{1 + x} = 1 - 2x + \frac{x^{2}}{2} - 3x^{3} + ⋯$
- id: e
  content: |-
    $\frac{1}{1 + x} = 1 - x + x^{2} - x^{3} + ⋯$
  correct: true
```

---

<a id="expressing-the-maclaurin-series-of-a-function-in-sigma-notation"></a>
## Expressing the Maclaurin Series of a Function in Sigma Notation

**Example:** Express the Maclaurin series expansion for $\cos{x}$, given by
$\cos{x} = 1 - \frac{x^2}{2} + \frac{x^4}{4!}- \frac{x^6}{6!}+\cdots$,
using sigma notation.

**Explanation**

The first four terms of the series are

$$
\begin{aligned}
a_{0} &= 1 \\
a_{1} &= -\frac{x^{2}}{2} \\
a_{2} &= \frac{x^{4}}{4!} \\
a_{3} &= -\frac{x^{6}}{6!}
\end{aligned}
$$

Notice that we can express these terms using a common format, as follows:

$$
\begin{aligned}
a_{0} &= ((-1)^{0}x^{2 \cdot 0})/((2 \cdot 0)!) \\
a_{1} &= ((-1)^{1}x^{2 \cdot 1})/((2 \cdot 1)!) \\
a_{2} &= ((-1)^{2}x^{2 \cdot 2})/((2 \cdot 2)!) \\
a_{3} &= ((-1)^{3}x^{2 \cdot 3})/((2 \cdot 3)!)
\end{aligned}
$$

We deduce that the general formula for the $n$th term is

$$
a_n = \dfrac{(-1)^n x^{2n}}{(2n)!} \,
$$

Therefore, we have

$$
\begin{aligned}
\cos x &= ∑_(n = 0)^(∞)((-1)^{n}x^{2n})/((2n)!)
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: ma-9949
content: |-
  Express the Maclaurin series expansion for $\sin x$, given by

  $\sin x = x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + ⋯$
  using sigma notation.
options:
- id: a
  content: |-
    $\sin x = ∑_(n = 1)^(∞)((-1)^{n}x^{2n - 1})/((2n - 1)!)$
- id: b
  content: |-
    $\sin x = ∑_(n = 0)^(∞)((-1)^{n}x^{2n})/((2n)!)$
- id: c
  content: |-
    $\sin x = ∑_(n = 1)^(∞)((-1)^{n + 1}x^{2n})/((2n)!)$
- id: d
  content: |-
    $\sin x = ∑_(n = 0)^(∞)((-1)^{n}x^{2n + 1})/((2n + 1)!)$
  correct: true
- id: e
  content: |-
    $\sin x = ∑_(n = 0)^(∞)((-1)^{n + 1}x^{n + 1})/((n + 1)!)$
```

---

**Question 4:**

```quiz
type: radio
id: ma-11715
content: |-
  Express the Maclaurin series expansion for $\frac{1}{1 - x}$, given by

  $\frac{1}{1 - x} = 1 + x + x^{2} + x^{3} + ⋯, x ∈ (-1, 1)$
  using sigma notation.
options:
- id: a
  content: |-
    $\frac{1}{1 - x} = ∑_(n = 1)^(∞)(-1)^{n}x^{n}$
- id: b
  content: |-
    $\frac{1}{1 + x} = ∑_(n = 0)^(∞)x^{2n}$
- id: c
  content: |-
    $\frac{1}{1 - x} = ∑_(n = 0)^(∞)\frac{x^{n}}{n}$
- id: d
  content: |-
    $\frac{1}{1 - x} = ∑_(n = 1)^(∞)\frac{x^{2n}}{n!}$
- id: e
  content: |-
    $\frac{1}{1 - x} = ∑_(n = 0)^(∞)x^{n}$
  correct: true
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
