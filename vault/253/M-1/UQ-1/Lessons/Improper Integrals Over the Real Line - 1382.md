# Improper Integrals Over the Real Line


<!--
lesson-id: 1382
topic-code: MF3.10.6.4
-->
## Table of Contents

- [Introduction](#introduction)
- [Identifying Convergent or Divergent Integrals With Unbounded Limits](#identifying-convergent-or-divergent-integrals-with-unbounded-limits)
- [Improper Integrals of Even and Odd Functions](#improper-integrals-of-even-and-odd-functions)
- [Calculating an Improper Integral With Unbounded Limits](#calculating-an-improper-integral-with-unbounded-limits)
- [Finding the Area of an Unbounded Region](#finding-the-area-of-an-unbounded-region)

## Prerequisites

- [The Area Bounded by a Curve and the X-Axis](../1040/1040.md)
- [Improper Integrals Involving Exponential Functions](../4004/4004.md)
- [Improper Integrals Involving Arctangent](../4005/4005.md)

---

<a id="introduction"></a>
## Introduction

Consider an improper integral in which both the left and right endpoints are unbounded:

$$
\int_{-\infty}^{\infty} f(x) \, \textrm{d}x
$$

If the integrand $f(x)$ is continuous on $(-\infty, \infty)$, then we can break the integral up into two improper integrals, each with a single unbounded endpoint:

$$
\int_{-\infty}^{\infty} f(x) \, \textrm{d}x = \int_{-\infty}^{0} f(x) \, \textrm{d}x + \int_{0}^{\infty} f(x) \, \textrm{d}x
$$

Then, we can compute each of the two integrals separately and combine their results.

**Watch out!** If either of the two integrals on the right-hand side is divergent, then the integral on the left-hand side is also divergent.

---

<a id="identifying-convergent-or-divergent-integrals-with-unbounded-limits"></a>
## Identifying Convergent or Divergent Integrals With Unbounded Limits

**Example:** Consider the function $f(x) = e^{-x}$. Which of the following statements are true?

1. $\displaystyle \int_0^\infty f(x) \, \textrm dx$ is convergent
2. $\displaystyle \int_{-\infty}^0 f(x) \, \textrm dx$ is divergent
3. $\displaystyle \int_{-\infty}^\infty f(x) \, \textrm dx$ is divergent

**Explanation**

Suppose we have an improper integral in which both the left and right endpoints are unbounded:

$$
\int_{-\infty}^{\infty} f(x) \, \textrm{d}x
$$

If the integrand $f(x)$ is continuous on $(-\infty, \infty)$, then we can break the integral up into two improper integrals, each with a single unbounded endpoint:

$$
\int_{-\infty}^{\infty} f(x) \, \textrm{d}x = \int_{-\infty}^{0} f(x) \, \textrm{d}x + \int_{0}^{\infty} f(x) \, \textrm{d}x
$$

Then, we can compute each of the two integrals separately and combine their results.

**Watch out!** If either of the two integrals on the right-hand side is divergent, then the integral on the left-hand side is also divergent.

With that in mind, let's examine our integrals.

- Computing the integral in statement I, we get
$\begin{aligned} \int_{0}^{\infty} e^{-x}\, \textrm{d}x &= \lim_{a \to \infty} \int_{0}^{a} e^{-x}\, \textrm{d}x \\ &= \lim_{a \to \infty} \left[-e^{-x}\right]_0^a \\ &= -\lim_{a \to \infty} \left({e^{-a}}-1\right) \\ &= 1. \end{aligned}$
So the integral converges, and statement I is true.
- Computing the integral in statement II, we get
$∫_{- ∞}^{0}e^{-x}dx|= \lim_{a \to -\infty}∫_{a}^{0}e^{-x}dx; = \lim_{a \to -\infty}[- e^{-x}]_{a}^{0}; = \lim_{a \to -\infty}(e^{-a} - 1); = + ∞$.
So the integral diverges, and statement II is true.
- The integral in statement III can be expressed as
$\displaystyle \int_{-\infty}^\infty f(x) \, \textrm dx= \int_{-\infty}^0 f(x) \, \textrm dx + \int_0^\infty f(x) \, \textrm dx$.
However, the first integral on the right-hand side is divergent. Therefore, the integral on the left-hand side is also divergent, and statement III is true.

In conclusion, statements I, II, and III are all true.

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-1382-q001
content: |-
  Consider the function
  $$
  f(x) = 3x^{2}
  $$
  Which of the following statements are true?
  
  $$
  \begin{aligned}
  \text{I.}\quad &\int_{0}^{\infty}f(x)\,dx \text{ is convergent} \\
  \text{II.}\quad &\int_{-\infty}^{0}f(x)\,dx \text{ is divergent} \\
  \text{III.}\quad &\int_{-\infty}^{\infty}f(x)\,dx \text{ is divergent}
  \end{aligned}
  $$
options:
- id: a
  content: |-
    II and III only
  correct: true
- id: b
  content: |-
    I only
- id: c
  content: |-
    I, II, and III
- id: d
  content: |-
    III only
- id: e
  content: |-
    I and III only
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-1382-q002
content: |-
  Consider the function
  $$
  f(x) = e^{2x}
  $$
  Which of the following statements are true?
  
  $$
  \begin{aligned}
  \text{I.}\quad &\int_{0}^{\infty}f(x)\,dx \text{ is convergent} \\
  \text{II.}\quad &\int_{-\infty}^{0}f(x)\,dx \text{ is divergent} \\
  \text{III.}\quad &\int_{-\infty}^{\infty}f(x)\,dx \text{ is divergent}
  \end{aligned}
  $$
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    III only
  correct: true
- id: c
  content: |-
    I, II, and III
- id: d
  content: |-
    II and III only
- id: e
  content: |-
    I and II only
```
---

<a id="improper-integrals-of-even-and-odd-functions"></a>
## Improper Integrals of Even and Odd Functions

Computing the definite integral of a function over the entire real line requires us to break the integral into two parts and separately evaluate each one.

$$
\int_{-\infty}^{\infty} f(x) \, \textrm{d}x = \int_{-\infty}^{0} f(x) \, \textrm{d}x + \int_{0}^{\infty} f(x) \, \textrm{d}x
$$

Evaluating two improper integrals can be quite time-consuming. However, we can shorten the process if we see that $f(x)$ is an even or odd function.

- Recall that $f(x)$ is an even function if $f(-x) = f(x)$. Even functions are symmetrical about the $y$-axis. Therefore, if $f(x)$ is even, we have
$\int_{-\infty}^{0} f(x) \, \textrm{d}x = \int_{0}^{\infty} f(x) \, \textrm{d}x$,
provided that the integrals are convergent. Moreover, if $f(x)$ is even and the above integrals are convergent, then
$\int_{-\infty}^{\infty} f(x) \, \textrm{d}x = 2\int_{0}^{\infty} f(x) \, \textrm{d}x$.
- Recall that $f(x)$ is an odd function if $f(-x) = -f(x)$. Therefore, if $f(x)$ is odd, we have
$\int_{-\infty}^{0} f(x) \, \textrm{d}x = -\int_{0}^{\infty} f(x) \, \textrm{d}x$,
provided that the integrals are convergent. Moreover, if $f(x)$ is odd and the above integrals are convergent, then
$\int_{-\infty}^{\infty} f(x) \, \textrm{d}x = 0$.

---

<a id="calculating-an-improper-integral-with-unbounded-limits"></a>
## Calculating an Improper Integral With Unbounded Limits

**Example:** Evaluate $\displaystyle \int_{-\infty}^{\infty} \dfrac{1}{x^2+1} \, \textrm{d}x$.

**Explanation**

We break up the integral as follows:

$$
\int_{-\infty}^{\infty} \dfrac{1}{x^2+1} \, \textrm{d}x = \int_{-\infty}^{0} \dfrac{1}{x^2+1} \, \textrm{d}x + \int_{0}^{\infty} \dfrac{1}{x^2+1} \, \textrm{d}x
$$

Evaluating the first of these integrals, we get

$$
\begin{aligned} \int_{-\infty}^0 \dfrac {1}{x^2+1} \,\textrm{d}x &= \lim_{a \to -\infty} \int_{a}^0 \dfrac {1}{x^2+1} \,\textrm{d}x \\[5pt] & = \lim_{a \to -\infty}\left(\arctan (x) \Big \mid _a^0 \right) \\[5pt] & = \lim_{a \to -\infty} \left[\arctan \left(0 \right) - \arctan \left(a \right) \right] \\[5pt] & = 0 - \lim_{a \to -\infty} \arctan \left(a \right) \\[5pt] &=-\left(-\dfrac \pi 2 \right) \\[5pt] & = \dfrac{\pi}{2}. \end{aligned}
$$

Now, notice that the integrand is an **even** function (i.e., it is symmetrical about the $y$-axis). This means that we can immediately deduce that

$$
\int_{0}^\infty \dfrac {1}{x^2+1} \,\textrm{d}x =\dfrac{\pi}{2}
$$

Therefore, since both improper integrals exist, we conclude that

$$
\begin{aligned} \int_{-\infty}^{\infty} \dfrac{1}{x^2+1} \, \textrm{d}x &= \int_{-\infty}^{0} \dfrac{1}{x^2+1} \, \textrm{d}x + \int_{0}^{\infty} \dfrac{1}{x^2+1} \, \textrm{d}x \\[5pt] &=\dfrac{\pi}{2}+ \dfrac{\pi}{2} \\[5pt] &= \pi. \end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-1382-q003
content: |-
  Evaluate
  $$
  \int_{-\infty}^{\infty}\frac{1}{4 + x^{2}}\,dx
  $$
options:
- id: a
  content: |-
    The integral is divergent
- id: b
  content: |-
    $\frac{π}{3}$
- id: c
  content: |-
    $\frac{π}{6}$
- id: d
  content: |-
    $\frac{2π}{3}$
- id: e
  content: |-
    $\frac{π}{2}$
  correct: true
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-1382-q004
content: |-
  Evaluate the integral
  $$
  \int_{-\infty}^{\infty}\frac{6x^{5}}{(3 + x^{6})^{2}}\,dx
  $$
options:
- id: a
  content: |-
    $-\frac{1}{3}$
- id: b
  content: |-
    The integral is divergent
- id: c
  content: |-
    $\frac{1}{3}$
- id: d
  content: |-
    $1$
- id: e
  content: |-
    $0$
  correct: true
```
---

<a id="finding-the-area-of-an-unbounded-region"></a>
## Finding the Area of an Unbounded Region

**Example:** Find the area of the region bounded by the graph of the curve $y = \dfrac{9}{1+4x^2}$ and the $x$-axis.

**Explanation**

Let's sketch a graph of the region.

![](<253/M-1/UQ-1/Source/Improper Integrals Over the Real Line - 1382/Images/12de9a29b2f0e4eaad17166bc9fc3b49.png>)

In this case, we must calculate the improper integral

$$
\displaystyle \int_{-\infty}^{\infty} \dfrac{9}{4x^2+1}\,\textrm{d}x
$$

As usual, we break up the integral as follows:

$$
\displaystyle \int_{-\infty}^{\infty} \dfrac{9}{4x^2+1}\,\textrm{d}x = \displaystyle \int_{-\infty}^{0} \dfrac{9}{4x^2+1}\,\textrm{d}x + \displaystyle \int_{0}^{\infty} \dfrac{9}{4x^2+1}\,\textrm{d}x
$$

Evaluating the first of these integrals, we get

$$
\begin{aligned} \int_{-\infty}^0 \dfrac {9}{4x^2+1} \,\textrm{d}x & = 9\lim_{a \to -\infty}\left(\left[\dfrac{1}{2}\arctan \left(2x \right) \right]_a^0 \right) \\[5pt] & = \dfrac{9}{2} \lim_{a \to -\infty} \left[\arctan \left(0 \right) - \arctan \left(2a \right) \right] \\[5pt] & = 0 - \dfrac{9}{2}\lim_{a \to -\infty} \arctan \left(2a \right) \\[5pt] & = -\dfrac{9}{2} \left(-\dfrac \pi 2 \right) \\[5pt] & = \dfrac{9\pi}{4}. \end{aligned}
$$

Now, notice that the integrand is an **even** function. Therefore, we can immediately deduce that

$$
\displaystyle \int_{0}^\infty\dfrac {9}{4x^2+1} \,\textrm{d}x = \dfrac{9\pi}{4}
$$

Therefore, since both improper integrals exist, we conclude that

$$
\int_{-\infty}^{\infty} \dfrac{9}{4x^2+1}\,\textrm{d}x = \dfrac{9\pi}{4}+ \dfrac{9\pi}{4}= \dfrac{9\pi}{2}
$$

So, the required area is equal to

$$
\dfrac{9\pi}{2}
$$

square units.

---

**Question 5:**

```quiz
type: radio
id: MA253-UQ1-1382-q005
content: |-
  ![](<../Source/Improper Integrals Over the Real Line - 1382/Images/q-81168.png>)
  
  Find the total area of the region bounded by the graph of the curve $y = \frac{1}{9 + x^{2}}$ and the $x$-axis, as shown above.
options:
- id: a
  content: |-
    $\frac{π}{6}$
- id: b
  content: |-
    $\frac{π}{2}$
- id: c
  content: |-
    $0$
- id: d
  content: |-
    $\frac{π}{3}$
  correct: true
- id: e
  content: |-
    $π$
```
---

**Question 6:**

```quiz
type: radio
id: MA253-UQ1-1382-q006
content: |-
  Find the total area of the region bounded by the graph of the curve $y = \mid x \mid e^{-x^{2}}$ and the $x$-axis.
options:
- id: a
  content: |-
    $1$
  correct: true
- id: b
  content: |-
    $\frac{π}{3}$
- id: c
  content: |-
    $\frac{5π}{6}$
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $\frac{π}{2}$
```
---

## Navigation

- [Next: Improper Integrals of the Second Kind: Discontinuities at Interior Points](<Improper Integrals of the Second Kind- Discontinuities at Interior Points - 3550.md>)
- [Back to UQ-1](UQ-1.md)

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
