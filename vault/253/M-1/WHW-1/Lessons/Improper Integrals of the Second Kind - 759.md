# Improper Integrals of the Second Kind

## Table of Contents

- [Introduction](#introduction)
- [Identifying Improper Integrals of the Second Kind](#identifying-improper-integrals-of-the-second-kind)
- [Improper Integrals of the Second Kind: Rewriting the Lower Limit](#improper-integrals-of-the-second-kind-rewriting-the-lower-limit)
- [Improper Integrals of the Second Kind: Rewriting the Upper Limit](#improper-integrals-of-the-second-kind-rewriting-the-upper-limit)
- [Rewriting One of the Limits of an Improper Integral](#rewriting-one-of-the-limits-of-an-improper-integral)
- [Evaluating Improper Integrals of the Second Kind](#evaluating-improper-integrals-of-the-second-kind)
- [Evaluating an Improper Integral of the Second Kind](#evaluating-an-improper-integral-of-the-second-kind)

## Prerequisites

- [Integration by Substitution With Inverse Trigonometric Functions](../315/315.md)
- [Integrating Trigonometric Functions Using Substitution](../478/478.md)
- [Integrating Exponential Functions Using Substitution](../3770/3770.md)

---

<a id="introduction"></a>
## Introduction

An **improper integral of the second kind** is the integral of the form

$$
\displaystyle \int_{\color{red}{a}}^{\color{blue}{b}} f(x)\,dx
$$

where the integration limits $\color{red}a$ and $\color{blue}b$ are both finite, and the function $f(x)$ is unbounded as we approach one of these limits.

For instance, the definite integral

$$
\int_{\color{red}{0}}^{\color{blue}{1}}\frac{1}{\sqrt{x}}\,dx
$$

is an improper integral of the second kind because

- both limits ($\color{red}0$ and $\color{blue}1$) are finite, and
- the function under the integral is unbounded as we approach one of the limits (the *lower* limit in this case):
$f(x) = \frac{1}{\sqrt{x}} \to \infty \quad\text{as}\quad x\to {\color{red}0}^+$

Let's look at some examples of integrals that are *not* improper integrals of the second kind:

- For the integral
$\int_1^\infty \frac{1}{\sqrt{x}}\,dx$
the upper limit is infinite. Therefore, it is *not* an improper integral of the second kind.
- For the integral
$\int_{\color{red}{1}}^{\color{blue}{2}} \frac{1}{\sqrt{x}}\,dx$
the function $f(x)$ under the integral is finite at both limits:
$f(1) = \frac{1}{\sqrt{1}} = 1 \ne \pm \infty; f(2) = \frac{1}{\sqrt{2}} \ne \pm \infty$
Therefore, it is *not* an improper integral of the second kind.

---

<a id="identifying-improper-integrals-of-the-second-kind"></a>
## Identifying Improper Integrals of the Second Kind

**Example:** Which of the following is an improper integral of the second kind?

1. $\displaystyle \int_{0}^{\infty} \frac{1}{x - 2}\,dx\qquad$ II. $\displaystyle \int_{-2}^{0} \frac{1}{x + 2}\,dx\qquad$ III. $\displaystyle \int_{2}^{3} \frac{1}{x^2 - 1}\,dx$

**Explanation**

Let's examine each of the given integrals.

- Integral I is an improper integral over an *infinite* domain since its upper limit is infinite. So, it is not an improper integral of the second kind.
- Integral II is an improper integral of the second kind since it has finite limits, and
$f(x) = \dfrac{1}{x+2} \to \infty \quad \text{as}\quad x\to (-2)^+$.
- Integral III is not an improper integral since it has finite limits, and the function under the integral is finite at every point $x\in[2,3]$.

Therefore, the correct answer is "II only."

---

**Question 1:**

```quiz
type: radio
id: MA253-WHW1-759-q001
content: |-
  Which of the following is an improper integral of the second kind?
  
  1. $\int_{2}^{6}\frac{1}{x}\,dx$ II. $\int_{2}^{6}\frac{1}{x - 6}\,dx$ III. $\int_{2}^{\infty}\frac{1}{x - 6}\,dx$

options:
- id: a
  content: |-
    I and II only

- id: b
  content: |-
    III only

- id: c
  content: |-
    I and III only

- id: d
  content: |-
    I, II, and III

- id: e
  content: |-
    II only
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: MA253-WHW1-759-q002
content: |-
  Which of the following is an improper integral of the second kind?
  
  1. $\int_{\pi/4}^{\infty}\tan x\,dx$ II. $\int_{0}^{\pi/2}\frac{1}{1 - \sin x}\,dx$ III. $\int_{\pi/4}^{\pi/2}\csc x\,dx$

options:
- id: a
  content: |-
    III only

- id: b
  content: |-
    II and III only

- id: c
  content: |-
    I and II only

- id: d
  content: |-
    II only
  correct: true

- id: e
  content: |-
    I only
```

---

<a id="improper-integrals-of-the-second-kind-rewriting-the-lower-limit"></a>
## Improper Integrals of the Second Kind: Rewriting the Lower Limit

Let's once again consider the following improper integral:

$$
I = \int_{\color{red}{0}}^{\color{blue}1}\frac{1}{\sqrt{x}}\,dx
$$

The function under the integral is unbounded as we approach the *lower* integration limit from any point that lies in the interval $x\in ({\color{red}{0}},{\color{blue}{1}})$:

$$
f(x) = \frac{1}{\sqrt{x}} \to \infty \quad\text{as}\quad x\to {\color{red}0}^+
$$

We can attempt to evaluate this integral by integrating $f(x)$ over the interval $x\in [a, 1]$ for some parameter $a\in ({\color{red}{0}},{\color{blue}{1}})$ and taking the limit as $a\to{\color{red}0}^+$:

$$
I = \lim_{a \to {\color{red}0}^+} \int_a^1 \frac{1}{\sqrt{x}}\,dx
$$

---

<a id="improper-integrals-of-the-second-kind-rewriting-the-upper-limit"></a>
## Improper Integrals of the Second Kind: Rewriting the Upper Limit

Now let's consider the following improper integral:

$$
I = \int_{\color{red}0}^{\color{blue}{2}}\frac{1}{\sqrt[3]{x-2}}\,dx
$$

The function under the integral is unbounded as we approach the *upper* integration limit from any point that lies in the interval $x\in ({\color{red}{0}},{\color{blue}{2}})$

$$
f(x) = \frac{1}{\sqrt[3]{x-2}} \to -\infty \quad\text{as}\quad x\to {\color{blue}2}^-
$$

We can attempt to evaluate this integral by integrating $f(x)$ over the interval $x\in [0, b]$ for some parameter $b\in ({\color{red}{0}},{\color{blue}{2}})$ and taking the limit as $b\to{\color{blue}2}^-$:

$$
I = \lim_{b \to {\color{blue}2}^-} \int_{0}^b \frac{1}{\sqrt[3]{x-2}}\,dx
$$

---

<a id="rewriting-one-of-the-limits-of-an-improper-integral"></a>
## Rewriting One of the Limits of an Improper Integral

**Example:** Rewrite the improper integral $\displaystyle \int_{0}^{1} \frac{1}{x^2 - 1}\,dx$ as the limit of definite integral.

**Explanation**

This is an improper integral of the second kind because the function under the integral is unbounded as we approach the *upper* integration limit from any point that lies in the interval $x\in (0,{\color{blue}{1}})$:

$$
f(x) = \dfrac{1}{x^2-1} \to -\infty\quad \text{as}\quad x\to {\color{blue}{1}} ^-
$$

We can attempt to evaluate this integral by integrating $f(x)$ over the interval $x\in [0, b]$ and taking the limit as $b\to{\color{blue}1}^-$:

$$
\displaystyle \int_{0}^{1} \frac{1}{x^2 - 1}\,dx = \lim_{b \to {\color{blue}{1}}^-} \left(\displaystyle \int_{0}^{b} \frac{1}{x^2 - 1}\,dx \right)
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-WHW1-759-q003
content: |-
  Which of the following is equivalent to
  $\int_{2}^{5}\frac{1}{\sqrt{x^{2} - 4}}\,dx$?

options:
- id: a
  content: |-
    $\lim_{a \to -\infty} \int_{a}^{5}\frac{1}{\sqrt{x^{2} - 4}}\,dx$

- id: b
  content: |-
    $\lim_{a \to 4^+} \int_{a}^{5}\frac{1}{\sqrt{x^{2} - 4}}\,dx$

- id: c
  content: |-
    $\lim_{a \to 5^-} \int_{a}^{5}\frac{1}{\sqrt{x^{2} - 4}}\,dx$

- id: d
  content: |-
    $\lim_{a \to +\infty} \int_{2}^{a}\frac{1}{\sqrt{x^{2} - 4}}\,dx$

- id: e
  content: |-
    $\lim_{a \to 2^+} \int_{a}^{5}\frac{1}{\sqrt{x^{2} - 4}}\,dx$
  correct: true
```

---

**Question 4:**

```quiz
type: radio
id: MA253-WHW1-759-q004
content: |-
  Which of the following is equivalent to
  $\int_{-6}^{-3}\frac{1}{\sqrt{x^{2} - 9}}\,dx$?

options:
- id: a
  content: |-
    $\lim_{b \to \infty} \int_{-6}^{b}\frac{1}{\sqrt{x^{2} - 9}}\,dx$

- id: b
  content: |-
    $\lim_{b \to 3^-} \int_{-6}^{b}\frac{1}{\sqrt{x^{2} - 9}}\,dx$

- id: c
  content: |-
    $\lim_{b \to -3^-} \int_{-6}^{b}\frac{1}{\sqrt{x^{2} - 9}}\,dx$
  correct: true

- id: d
  content: |-
    $\lim_{b \to -6^+} \int_{b}^{-3}\frac{1}{\sqrt{x^{2} - 9}}\,dx$

- id: e
  content: |-
    $\lim_{b \to -\infty} \int_{b}^{-3}\frac{1}{\sqrt{x^{2} - 9}}\,dx$
```

---

<a id="evaluating-improper-integrals-of-the-second-kind"></a>
## Evaluating Improper Integrals of the Second Kind

We've seen how to construct improper integrals of the second kind. Now, let's learn how to evaluate them.

As an example, let's consider the following integral:

$$
\int_0^1 \frac{1}{\sqrt{1 - x^2}}\,dx
$$

This is an improper integral of the second kind because the function is unbounded at the upper limit of integration:

$$
f(x) = \frac{1}{\sqrt{1-x^2}} \to \infty \quad\text{as}\quad x\to 1^-
$$

Nonetheless, it is possible to evaluate the integral by setting the upper bound equal to some parameter $b$, integrating as usual, and then taking the limit as $b\to 1^-$.

$$
\begin{aligned}
\int_{0}^{1}\frac{1}{\sqrt{1 - x^{2}}}\,dx &= \lim_{b \to 1^-}\int_{0}^{b}\frac{1}{\sqrt{1 - x^{2}}}\,dx \\
&= \lim_{b \to 1^-}\arcsin x\bigg|_{0}^{b} \\
&= \lim_{b \to 1^-}[\arcsin b - \arcsin 0] \\
&= \lim_{b \to 1^-}[\arcsin b - 0] \\
&= \lim_{b \to 1^-}\arcsin b \\
&= \arcsin (1) \\
&= \frac{\pi}{2}
\end{aligned}
$$

Therefore, we conclude that

$$
\int_0^1 \frac{1}{\sqrt{1 - x^2}}\,dx = \dfrac{\pi}{2}
$$

If the limit is infinite or does not exist, we say that the integral is **divergent**. Let's see an example.

---

<a id="evaluating-an-improper-integral-of-the-second-kind"></a>
## Evaluating an Improper Integral of the Second Kind

**Example:** Evaluate $\displaystyle \int_0^{\pi/2}\tan x\,dx$.

**Explanation**

First, let's rewrite the integral using a substitution. Let $u = \cos x$. Then, we have

$$
\dfrac{du}{dx} = -\sin x \quad\Longrightarrow\quad -du = \sin x\,dx
$$

We use the table below to change the limits:

| $x$ | $0$ | $\dfrac{\pi}{2}$ |
| --- | ---: | ---: |
| $u$ | $1$ | $0$ |

Carrying out the change of variable, we have

$$
\begin{aligned}
\int_{0}^{\pi/2}\tan x\,dx &= \int_{0}^{\pi/2}\frac{\sin x}{\cos x}\,dx \\
&= \int_{1}^{0}-\frac{1}{u}\,du \\
&= \int_{0}^{1}\frac{1}{u}\,du
\end{aligned}
$$

This is an improper integral of the second kind because the function under the integral is unbounded at the *lower* limit of integration.

$$
f(u) = \dfrac{1}{u} \to \infty \quad\text{as}\quad u\to 0^+
$$

Nonetheless, it is possible to calculate the integral by setting the *lower* bound equal to some parameter $a$, integrating as usual, and then taking the limit as $a\to0^+$.

$$
\begin{aligned}
\int_{0}^{1}\frac{1}{u}\,du &= \lim_{a \to 0^+}\int_{a}^{1}\frac{1}{u}\,du \\
&= \lim_{a \to 0^+}\ln|u|\bigg|_{a}^{1} \\
&= \lim_{a \to 0^+}\left[\ln|1| - \ln|a|\right] \\
&= \lim_{a \to 0^+}\left[0 - \ln|a|\right] \\
&= - (-\infty) \\
&= \infty
\end{aligned}
$$

Therefore, we conclude that the integral is divergent.

---

**Question 5:**

```quiz
type: radio
id: MA253-WHW1-759-q005
content: |-
  What is $\int_{0}^{16}\frac{1}{\sqrt{x}}\,dx$?

options:
- id: a
  content: |-
    $16$

- id: b
  content: |-
    $4$

- id: c
  content: |-
    The integral is divergent

- id: d
  content: |-
    $8$
  correct: true

- id: e
  content: |-
    $\frac{1}{4}$
```

---

**Question 6:**

```quiz
type: radio
id: MA253-WHW1-759-q006
content: |-
  What is $\int_{1}^{4}\frac{1}{\sqrt{4 - t}}\,dt$?

options:
- id: a
  content: |-
    $2\sqrt{3}$
  correct: true

- id: b
  content: |-
    $\frac{1}{2\sqrt{3}}$

- id: c
  content: |-
    $4$

- id: d
  content: |-
    $2\sqrt{3} - 2\sqrt{2}$

- id: e
  content: |-
    The integral is divergent
```

---

## Navigation

- [Next: WHW-1 Problems](253/M-1/WHW-1/WHW-1.md)
- [Back to WHW-1](253/M-1/WHW-1/WHW-1.md)
