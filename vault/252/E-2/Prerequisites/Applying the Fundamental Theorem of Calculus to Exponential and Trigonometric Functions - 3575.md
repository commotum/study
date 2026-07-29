# Applying the Fundamental Theorem of Calculus to Exponential and Trigonometric Functions

<!--
lesson-id: 3575
topic-code: MF3.9.2.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Evaluating the Definite Integral of an Exponential Function](#evaluating-the-definite-integral-of-an-exponential-function)
- [Evaluating the Definite Integral of a Trigonometric Function](#evaluating-the-definite-integral-of-a-trigonometric-function)

## Prerequisites

- [The Fundamental Theorem of Calculus](<../../../MA/Mathematical-Foundations/MF3/9. Definite Integrals/9.2. Definite Integrals/Lessons/9.2.2. The Fundamental Theorem of Calculus.md>)
- [Integrating Trigonometric Functions](<../../../MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.4. Indefinite Integrals/Lessons/12.4.6. Integrating Trigonometric Functions.md>)
- [Integrating Exponential Functions](<../../../MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.4. Indefinite Integrals/Lessons/12.4.5. Integrating Exponential Functions.md>)

---

<a id="introduction"></a>
## Introduction

Besides polynomials, exponential and trigonometric functions are perhaps the most efficient functions in terms of calculating their definite integrals. Indeed, recall that the fundamental theorem of calculus states the following:

> *If $f(x)$ is a function that's continuous on an interval $[a,b]$, and there exists a function $F(x)$ such that $F'(x) = f(x)$ on $[a,b]$, then*
> $\displaystyle \int_a^b f(x)\,\textrm{d}x = F(b) - F(a)$.

To illustrate this, let's calculate
$\displaystyle \int_1^3 2^x \,\textrm{d}x$.

Recall that the antiderivative of $2^x$ is

$$
\dfrac{2^x}{\ln{2}}
$$

Therefore, evaluating the difference at the bounds, we get

$$
\begin{aligned}
\int_{1}^{3}2^{x}dx &= \left.\frac{2^{x}}{\ln 2}\right|_{1}^{3} \\
&= \frac{1}{\ln 2}(2^{3} - 2^{1}) \\
&= \frac{1}{\ln 2}(8 - 2) \\
&= \frac{6}{\ln 2}
\end{aligned}
$$

---

<a id="evaluating-the-definite-integral-of-an-exponential-function"></a>
## Evaluating the Definite Integral of an Exponential Function

**Example:** Calculate $\displaystyle \int_{0}^5 e^x \, \textrm d x$.

**Explanation**

Taking the antiderivative and evaluating the difference at the bounds, we get

$$
\begin{aligned}
\int_{0}^{5}e^{x}dx &= \left.e^{x}\right|_{0}^{5} \\
&= e^{5} - e^{0} \\
&= e^{5} - 1
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-73236
content: |-
  Calculate $\displaystyle \int_{0}^{1}5^{x}dx$.
options:
- id: a
  correct: true
  content: |-
    $\frac{4}{\ln 5}$
- id: b
  content: |-
    $4$
- id: c
  content: |-
    $4\ln 5$
- id: d
  content: |-
    $\ln 5 - \ln 1$
- id: e
  content: |-
    $\ln 1 - \ln 0$
```

---

**Question 2:**

```quiz
type: radio
id: ma-73235
content: |-
  What is $\displaystyle \int_{0}^{2}e^{x}dx$?
options:
- id: a
  content: |-
    $e^{2} - e$
- id: b
  content: |-
    $e^{2}$
- id: c
  content: |-
    $e$
- id: d
  correct: true
  content: |-
    $e^{2} - 1$
- id: e
  content: |-
    $1$
```

---

<a id="evaluating-the-definite-integral-of-a-trigonometric-function"></a>
## Evaluating the Definite Integral of a Trigonometric Function

**Example:** Evaluate $\displaystyle \int_{0}^{\pi/2} \cos x \,\textrm{d} x$.

**Explanation**

Taking the antiderivative and evaluating the difference at the bounds, we get

$$
\begin{aligned}
\int_{0}^{π/2}\cos xdx &= \left.\sin x\right|_{0}^{π/2} \\
&= \sin (\frac{π}{2}) - \sin (0) \\
&= 1 - 0 \\
&= 1
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: ma-17821
content: |-
  Calculate $\displaystyle \int_{- π/6}^{π/4}\sec^{2} xdx$.
options:
- id: a
  correct: true
  content: |-
    $\frac{\sqrt{3} + 1}{\sqrt{3}}$
- id: b
  content: |-
    $\frac{3}{2}$
- id: c
  content: |-
    $\frac{1}{2}$
- id: d
  content: |-
    $\frac{\sqrt{2} + 1}{\sqrt{2}}$
- id: e
  content: |-
    $\frac{2}{3}$
```

---

**Question 4:**

```quiz
type: radio
id: ma-17818
content: |-
  What is $\displaystyle \int_{0}^{π/3}\cos xdx$?
options:
- id: a
  content: |-
    $\frac{1}{2}$
- id: b
  content: |-
    $\frac{\sqrt{3} - 1}{2}$
- id: c
  correct: true
  content: |-
    $\frac{\sqrt{3}}{2}$
- id: d
  content: |-
    $\frac{1 - \sqrt{3}}{2}$
- id: e
  content: |-
    $-\frac{\sqrt{3}}{2}$
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
