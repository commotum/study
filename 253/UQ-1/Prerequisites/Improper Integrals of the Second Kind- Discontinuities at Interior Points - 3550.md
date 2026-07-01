# Improper Integrals of the Second Kind: Discontinuities at Interior Points

## Table of Contents

- [Introduction](#introduction)
- [Identifying a Divergent Improper Integral With a Discontinuity at an Interior Point](#identifying-a-divergent-improper-integral-with-a-discontinuity-at-an-interior-point)
- [Calculating an Improper Integral with a Discontinuity at an Interior Point](#calculating-an-improper-integral-with-a-discontinuity-at-an-interior-point)

## Prerequisites

- [Improper Integrals of the Second Kind](../759/759.md)

---

<a id="introduction"></a>
## Introduction

Let's take a look at the integral

$$
I = \int_1^5\dfrac 1 {x-2} \,\textrm {d}x
$$

**Watch out!** In this particular case, it is *incorrect* to say

$$
\int_1^5\dfrac 1 {x-2} \,\textrm {d}x \:{\color{red}\boldsymbol{=}}\: \ln\begin{vmatrix}x-2 & \,\Big\end{vmatrix}_1^5 = \ln 3 - \ln 1 = \ln 3.\quad{\color{red}\times}
$$

This is incorrect because the integrand

$$
\dfrac{1}{x-2}
$$

has an infinite discontinuity at $x=2$, and this point lies within the domain of integration! Therefore, we cannot directly apply the first fundamental theorem of calculus.

Instead, what we can do is write the original integral as a sum of improper integrals:

$$
\int_1^5\dfrac 1 {x-2} \,\textrm {d}x = \underbrace{\int_1^2\dfrac 1 {x-2} \,\textrm {d}x}_{I_1} + \underbrace{\int_2^5\dfrac 1 {x-2} \,\textrm {d}x}_{I_2}
$$

Let's evaluate $I_1$:

$$
\begin{aligned}
∫_{1}^{2}\frac{1}{x - 2}dx &= lim_(a → 2^{-})∫_{1}^{a}\frac{1}{x - 2}dx \\
&= lim_(a → 2^{-})\ln \mid x - 2 \mid \mid _{1}^{a} \\
&= lim_(a → 2^{-})(\ln\begin{vmatrix}a - 2 & -\ln & 1 - 2\end{vmatrix}) \\
&= lim_(a → 2^{-})(\ln \mid a - 2\begin{vmatrix}-0) \\ = lim_(a → 2^{-})(\ln \mid a - 2\end{vmatrix}) \\
&= - ∞
\end{aligned}
$$

Since $I_1$ diverges, the integral $I$ also diverges. Since we know that $I$ diverges, there is no need to evaluate $I_2$.

In general, if a function $f(x)$ is continuous on $[a,b]$ *except* at some point $c \in (a,b)$ where it has an infinite discontinuity, then

$$
\int_a^b f(x)\,\textrm d x = \int_a^c f(x)\,\textrm d x + \int_c^b f(x)\,\textrm d x
$$

The integral on the left-hand side is convergent if and only if both integrals on the right-hand side are convergent. If either integral on the right-hand side diverges, then the integral on the left-hand side also diverges.

---

<a id="identifying-a-divergent-improper-integral-with-a-discontinuity-at-an-interior-point"></a>
## Identifying a Divergent Improper Integral With a Discontinuity at an Interior Point

**Example:** Given the function $f(x) = \dfrac{e^{2x}}{1-e^{2x}}$, which of the following statements are true?

1. $\displaystyle \int_{-1}^0 f(x) \,\textrm d x$ is divergent
2. $\displaystyle \int_{0}^1 f(x) \,\textrm d x$ is divergent
3. $\displaystyle \int_{-1}^1 f(x) \,\textrm d x$ is divergent

**Explanation**

Let's evaluate each integral in turn.

- Statement I is true. To compute the integral, we use the substitution
$u = e^{2x}\quad\Longrightarrow\quad \dfrac 1 2\, \textrm d u = e^{2x}\,\textrm d x$.
Calculating the integral, we get
$∫_{-1}^{0}f(x)dx|= ∫_{-1}^{0}\frac{e^{2x}}{1 - e^{2x}}dx; = \frac{1}{2}∫_{e^{-2}}^{1}\frac{1}{1 - u}du; =-\frac{1}{2}lim_(a → 1^{-})[\ln \mid 1 - u\begin{vmatrix}]_{e^{-2}}^{a} \\ =-\frac{1}{2}lim_(a → 1^{-})(\ln\begin{vmatrix}1 - a & -\ln\end{vmatrix}1 - e^{-2}\end{vmatrix}); =-\frac{1}{2}[- ∞ - \ln (1 - e^{-2})]; = ∞$.

- Statement II is true. To compute the integral in statement II, we use the same process as before.
$∫_{0}^{1}f(x)dx|= ∫_{0}^{1}\frac{e^{2x}}{1 - e^{2x}}dx; = \frac{1}{2}∫_{1}^{e^{2}}\frac{1}{1 - u}du; =-\frac{1}{2}lim_(a → 1^{+})[\ln \mid 1 - u\begin{vmatrix}]_{a}^{e^{2}} \\ =-\frac{1}{2}lim_(a → 1^{+})(\ln\begin{vmatrix}1 - e^{2} & -\ln\end{vmatrix}1 - a\end{vmatrix}); =-\frac{1}{2}[\ln (e^{2} - 1) - (- ∞)]; = - ∞$.
- Statement III is true. We can write down this integral by splitting it over the discontinuity at $x=0$, as follows:
$\displaystyle \int_{-1}^1 f(x) \,\textrm d x = \displaystyle \int_{-1}^0 f(x) \,\textrm d x + \displaystyle \int_{0}^1 f(x) \,\textrm d x$.
Since both integrals on the right-hand side are divergent, the integral on the left-hand side is divergent, too.

In conclusion, statements I, II, and III are all true.

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-3550-q001
content: |-
  Given the function $f(x) = \frac{\cos x}{1 - \sin x}$, which of the following statements are true?
  
  1. $∫_{0}^{π/2}f(x)dx$ is divergent
  2. $∫_{π/2}^{π}f(x)dx$ is divergent
  3. $∫_{0}^{π}f(x)dx$ is divergent
options:
- id: a
  content: |-
    None of the statements are true
- id: b
  content: |-
    II and III only
- id: c
  content: |-
    I, II, and III
  correct: true
- id: d
  content: |-
    I and II only
- id: e
  content: |-
    I and III only
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-3550-q002
content: |-
  Given the function $f(x) = \frac{x}{1 - x^{2}}$, which of the following statements are true?
  
  1. $∫_{0}^{1}f(x)dx$ is divergent
  2. $∫_{1}^{2}f(x)dx$ is convergent
  3. $∫_{0}^{2}f(x)dx$ is divergent
options:
- id: a
  content: |-
    I, II, and III
- id: b
  content: |-
    I and II only
- id: c
  content: |-
    I only
- id: d
  content: |-
    II only
- id: e
  content: |-
    I and III only
  correct: true
```
---

<a id="calculating-an-improper-integral-with-a-discontinuity-at-an-interior-point"></a>
## Calculating an Improper Integral with a Discontinuity at an Interior Point

**Example:** Find the value of $\displaystyle\int_{-2}^2\frac{1}{\sqrt[3]{x-1}}\textrm{d}x$.

**Explanation**

Notice that the denominator of the integrand vanishes at $x=1$. Therefore, to evaluate the integral, we need to split it up over the point of discontinuity:

$$
\begin{aligned}
∫_{-2}^{2}\frac{1}{\sqrt[3]{x - 1}}dx &= ∫_{-2}^{1}\frac{1}{\sqrt[3]{x - 1}}dx_(⏟)_(I_{1}) + ∫_{1}^{2}\frac{1}{\sqrt[3]{x - 1}}dx_(⏟)_(I_{2})
\end{aligned}
$$

Let's evaluate the first integral. Using the substitution $u = x-1$, we get

$$
\begin{aligned}
I_{1} &= ∫_{-2}^{1}\frac{1}{\sqrt[3]{x - 1}}dx \\
&= ∫_{-3}^{0}\frac{1}{\sqrt[3]{u}}du \\
&= lim_(a → 0^{-})∫_{-3}^{a}u^{-1/3}du \\
&= lim_(a → 0^{-})[\frac{3}{2}u^{2/3}]_{-3}^{a} \\
&= lim_(a → 0^{-})\frac{3}{2}[a^{2/3} - (-3)^{2/3}] \\
&= \frac{3}{2}[(0)^{2/3} - \sqrt[3]{(-3)^{2}}] \\
&=-\frac{3}{2}\sqrt[3]{9}
\end{aligned}
$$

Similarly, for $I_2$, we have

$$
\begin{aligned}
I_{2} &= ∫_{1}^{2}\frac{1}{\sqrt[3]{x - 1}}dx \\
&= ∫_{0}^{1}\frac{1}{\sqrt[3]{u}}du \\
&= lim_(a → 0^{+})∫_{a}^{1}u^{-1/3}du \\
&= lim_(a → 0^{+})[\frac{3}{2}u^{2/3}]_{a}^{1} \\
&= lim_(a → 0^{+})\frac{3}{2}[1^{2/3} - a^{2/3}] \\
&= \frac{3}{2}[1 - 0] \\
&= \frac{3}{2}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
∫_{-2}^{2}\frac{1}{\sqrt[3]{x - 1}}dx &= I_{1} + I_{2} \\
&=-\frac{3}{2}\sqrt[3]{9} + \frac{3}{2} \\
&= \frac{3}{2}(1 - \sqrt[3]{9})
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-3550-q003
content: |-
  What is $∫_{-27}^{1}\frac{1}{\sqrt[3]{x}}dx$?
options:
- id: a
  content: |-
    The integral is divergent
- id: b
  content: |-
    $\frac{3}{2}$
- id: c
  content: |-
    $-12$
  correct: true
- id: d
  content: |-
    $-\frac{9}{2}$
- id: e
  content: |-
    $-\frac{27}{2}$
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-3550-q004
content: |-
  Evaluate the integral $∫_{-8}^{1}\frac{1}{\sqrt[3]{x}}dx$.
options:
- id: a
  content: |-
    $6$
- id: b
  content: |-
    $-6$
- id: c
  content: |-
    The integral is divergent
- id: d
  content: |-
    $\frac{3}{2}$
- id: e
  content: |-
    $-\frac{9}{2}$
  correct: true
```
---

## Navigation

- [Next: Limits at Infinity and Horizontal Asymptotes of Rational Functions](<Limits at Infinity and Horizontal Asymptotes of Rational Functions - 1903.md>)
- [Back to UQ-1](../UQ-1.md)
