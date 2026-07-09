# The Fundamental Theorem of Calculus

<!--
lesson-id: 283
topic-code: MF3.9.2.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Evaluating the Definite Integral of a Polynomial Function](#evaluating-the-definite-integral-of-a-polynomial-function)
- [Evaluating the Definite Integral of a Rational Function](#evaluating-the-definite-integral-of-a-rational-function)
- [Evaluating the Definite Integral of a Radical Function](#evaluating-the-definite-integral-of-a-radical-function)

## Prerequisites

- [The Antiderivative](<../../../../CAB/6. Integration/6.1. Indefinite Integrals/Lessons/6.1.1. The Antiderivative.md>)
- [Continuity of Functions](<../../../7. Limits & Continuity/7.2. Continuity/Lessons/7.2.1. Continuity of Functions.md>)

---

<a id="introduction"></a>
## Introduction

Consider the function

$$
f(x) = x^2
$$

The **definite integral** **of** $\mathbf f(x)$ **between**

$$
\mathbf{x=1}
$$

and

$$
\mathbf{x=2}
$$

is denoted

$$
\int_1^2 x^2 \, \textrm d x
$$

Geometrically, this definite integral can be interpreted as the **signed area** bounded between the curve $y=f(x)$, the lines $x=1$ and $x=2$, and the $x$-axis, as shown below.

![](<../Source/The Fundamental Theorem of Calculus - 283/Images/2f9e5bf8afd908ee301b07893cfa7f12.png>)

The area is taken as positive (with a plus sign) if the corresponding region lies above the $x$-axis and as negative (with a minus sign) if the region lies below the $x$-axis.

To calculate this area, we use a theorem known as the **fundamental theorem of calculus**, which states the following:

> *If $f(x)$ is a function that's continuous on an interval $[a,b]$, and there exists a function $F(x)$ such that $F'(x) = f(x)$ on $[a,b]$, then*

$$
\int_a^b f(x)\,\textrm{d}x = F(b) - F(a)
$$

So how do we use this to calculate our definite integral $\displaystyle \int_1^2 x^2\,\textrm{d}x$? We just need to follow a few steps:

**Step 1**: Find the *indefinite* integral (also known as the antiderivative) of the function using the power rule. We can ignore the constant of integration.

$$
\int x^2 \, \textrm d x = \dfrac{x^3}{3}
$$

**Step 2**: Write the lower and upper limit next to the result.

$$
\int_1^2 x^2 \, \textrm d x = \left.\dfrac{x^3}{3}\Bigg\right|_{\color{red}1}^{\color{blue}2}
$$

**Step 3**: Evaluate the antiderivative between the upper and lower limit, and subtract them.

$$
\begin{aligned}
\int_{1}^{2}x^{2}dx &= ((2)^{3})/(3) - ((1)^{3})/(3) \\
&= \frac{8}{3} - \frac{1}{3} \\
&= \frac{7}{3}
\end{aligned}
$$

Therefore, we conclude that

$$
\int_1^2 f(x)\,\textrm{d}x = \dfrac73
$$

---

<a id="evaluating-the-definite-integral-of-a-polynomial-function"></a>
## Evaluating the Definite Integral of a Polynomial Function

**Example:** Evaluate $\displaystyle\int_0^4 x \, \textrm d x$.

**Explanation**

Taking the antiderivative and evaluating the difference at the bounds, we get

$$
\begin{aligned}
\int_{0}^{4}xdx &= \left.\frac{x^{1 + 1}}{1 + 1}\right|_{0}^{4} \\
&= \left.\frac{x^{2}}{2}\right|_{0}^{4} \\
&= \frac{4^{2}}{2} - \frac{0^{2}}{2} \\
&= \frac{16}{2} \\
&= 8
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-29634
content: |-
  What is $\displaystyle \int_{-2}^{2}x^{3}dx$?
options:
- id: a
  content: |-
    $16$
- id: b
  content: |-
    $\frac{1}{4}$
- id: c
  content: |-
    $\frac{1}{16}$
- id: d
  content: |-
    $4$
- id: e
  content: |-
    $0$
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: ma-29744
content: |-
  Evaluate $\displaystyle \int_{-5}^{4}x^{2}dx$.
options:
- id: a
  content: |-
    $\frac{125}{3}$
- id: b
  content: |-
    $189$
- id: c
  content: |-
    $\frac{189}{2}$
- id: d
  content: |-
    $\frac{64}{3}$
- id: e
  content: |-
    $63$
  correct: true
```

---

<a id="evaluating-the-definite-integral-of-a-rational-function"></a>
## Evaluating the Definite Integral of a Rational Function

**Example:** Evaluate $\displaystyle \int _{1}^2\dfrac 1 {x^3}\, \textrm d x$.

**Explanation**

Taking the antiderivative and evaluating the difference at the bounds, we get

$$
\begin{aligned}
\int_{1}^{2}\frac{1}{x^{3}}dx &= \int_{1}^{2}x^{-3}dx \\
&= \left.\frac{x^{-3 + 1}}{-3 + 1}\right|_{1}^{2} \\
&= \left.- \frac{x^{-2}}{2}\right|_{1}^{2} \\
&=-\frac{1}{2}(2^{-2} - 1^{-2}) \\
&=-\frac{1}{2}(\frac{1}{4} - 1) \\
&=-\frac{1}{2}(-\frac{3}{4}) \\
&= \frac{3}{8}
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: ma-49224
content: |-
  Evaluate $\displaystyle \int_{1/2}^{1}\frac{1}{x^{6}}dx$.
options:
- id: a
  content: |-
    $-\frac{63}{5}$
- id: b
  content: |-
    $\frac{31}{5}$
  correct: true
- id: c
  content: |-
    $-\frac{7}{5}$
- id: d
  content: |-
    $-\frac{31}{5}$
- id: e
  content: |-
    $\frac{63}{5}$
```

---

**Question 4:**

```quiz
type: radio
id: ma-49222
content: |-
  What is $\displaystyle \int_{1}^{2}\frac{1}{x^{4}}dx$?
options:
- id: a
  content: |-
    $\frac{7}{24}$
  correct: true
- id: b
  content: |-
    $-\frac{7}{12}$
- id: c
  content: |-
    $-\frac{7}{24}$
- id: d
  content: |-
    $\frac{7}{12}$
- id: e
  content: |-
    $\frac{31}{96}$
```

---

<a id="evaluating-the-definite-integral-of-a-radical-function"></a>
## Evaluating the Definite Integral of a Radical Function

**Example:** Calculate $\displaystyle\int_1^4\sqrt x\, \textrm d x$.

**Explanation**

Taking the antiderivative and evaluating the difference at the bounds, we get

$$
\begin{aligned}
\int_{1}^{4}\sqrt{x}dx &= \int_{1}^{4}x^{1/2}dx \\
&= \left.\frac{2}{3}x^{3/2}\right|_{1}^{4} \\
&= \frac{2}{3}(4^{3/2} - 1^{3/2}) \\
&= \frac{2}{3}(\sqrt{64} - 1) \\
&= \frac{2}{3}(8 - 1) \\
&= \frac{14}{3}
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: ma-29639
content: |-
  Evaluate $\displaystyle \int_{0}^{4}\sqrt{x^{5}}dx$.
options:
- id: a
  content: |-
    $448$
- id: b
  content: |-
    $\frac{256}{7}$
  correct: true
- id: c
  content: |-
    $128$
- id: d
  content: |-
    $\frac{7}{256}$
- id: e
  content: |-
    $\frac{128}{7}$
```

---

**Question 6:**

```quiz
type: radio
id: ma-49228
content: |-
  What is $\displaystyle \int_{0}^{1}\sqrt[5]{x^{3}}dx$?
options:
- id: a
  content: |-
    $\frac{5}{8}$
  correct: true
- id: b
  content: |-
    $\frac{5}{4}$
- id: c
  content: |-
    $0$
- id: d
  content: |-
    $-\frac{5}{4}$
- id: e
  content: |-
    $-\frac{5}{3}$
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
