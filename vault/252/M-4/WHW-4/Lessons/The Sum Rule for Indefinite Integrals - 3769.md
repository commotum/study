# The Sum Rule for Indefinite Integrals

<!--
lesson-id: 3769
topic-code: MF2.12.4.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Computing an Integral Using the Sum Rule](#computing-an-integral-using-the-sum-rule)
- [Combining the Constant Factor and Sum Rules](#combining-the-constant-factor-and-sum-rules)
- [Computing an Integral Using the Sum and Constant Factor Rules](#computing-an-integral-using-the-sum-and-constant-factor-rules)
- [Integrating Sums of Power Functions](#integrating-sums-of-power-functions)

## Prerequisites

- [The Constant Multiple Rule for Indefinite Integrals](<../../../../MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.4. Indefinite Integrals/Lessons/12.4.2. The Constant Multiple Rule for Indefinite Integrals.md>)

---

<a id="introduction"></a>
## Introduction

How can we calculate the integral of a sum of functions, like $\displaystyle \int (x+x^3)\,\textrm d x$?

According to the **sum rule**, the integral of the sum of functions is equal to the sum of the integrals of each function:

$$
\int (f(x) \pm g(x))\,\textrm d x = \int f(x) \,\textrm d x \pm \int g(x) \,\textrm d x
$$

In our case, we have

$$
\begin{aligned}
\int(x + x^{3})dx &= \intxdx + \intx^{3}dx \\
&= (\frac{x^{2}}{2} + c_{1}) + (\frac{x^{4}}{4} + c_{2}) \\
&= \frac{1}{2}x^{2} + \frac{1}{4}x^{4} + (c_{1} + c_{2}) \\
&= \frac{1}{2}x^{2} + \frac{1}{4}x^{4} + C
\end{aligned}
$$

where we renamed

$$
c_1+c_2=C
$$

(The sum of two arbitrary constants is itself an arbitrary constant.)

---

<a id="computing-an-integral-using-the-sum-rule"></a>
## Computing an Integral Using the Sum Rule

**Example:** Find the integral of $x^2 + 1$.

**Explanation**

Applying the sum rule, we compute the sum of the integrals of each function:

$$
\begin{aligned}
\intx^{2} + 1dx &= \intx^{2}dx + \int1dx \\
&= \intx^{2}dx + \intx^{0}dx \\
&= (\frac{x^{2 + 1}}{2 + 1}) + x + C \\
&= \frac{1}{3}x^{3} + x + C
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-2159
content: |-
  What is $\displaystyle \int\sqrt{x} - 3dx$?
options:
- id: a
  content: |-
    $\frac{3\sqrt[3]{x^{2}}}{2} - 3x$
- id: b
  content: |-
    $\frac{\sqrt{x^{3}}}{3} - 3x + C$
- id: c
  content: |-
    $\frac{3x\sqrt{x^{3}}}{2} - 3x + C$
- id: d
  content: |-
    $\frac{2x\sqrt[3]{x}}{3} + 3 + C$
- id: e
  content: |-
    $\frac{2\sqrt{x^{3}}}{3} - 3x + C$
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: ma-29828
content: |-
  Find the antiderivative of $\sqrt{x^{5}} + \frac{1}{\sqrt{x^{5}}}$.
options:
- id: a
  content: |-
    $\frac{4\sqrt{x^{5}}}{7} - \frac{7}{5\sqrt{x^{3}}} + C$
- id: b
  content: |-
    $\frac{2\sqrt{x^{7}}}{7} - \frac{2}{3\sqrt{x^{3}}} + C$
  correct: true
- id: c
  content: |-
    $\frac{2\sqrt{x^{3}}}{7} + \frac{2}{3\sqrt{x^{5}}} + C$
- id: d
  content: |-
    $\frac{2\sqrt{x^{7}}}{3} + \frac{5}{3\sqrt{x^{3}}} + C$
- id: e
  content: |-
    $\frac{3\sqrt{x^{3}}}{7} - \frac{11}{3\sqrt{x^{7}}} + C$
```

---

<a id="combining-the-constant-factor-and-sum-rules"></a>
## Combining the Constant Factor and Sum Rules

For more complicated functions consisting of the sum of functions multiplied by constants, we can combine the constant factor and sum rules as follows:

$$
\int k_1 f(x) \pm k_2 g(x)\,\textrm d x = k_1\int f(x) \,\textrm d x \pm k_2\int g(x) \,\textrm d x
$$

---

<a id="computing-an-integral-using-the-sum-and-constant-factor-rules"></a>
## Computing an Integral Using the Sum and Constant Factor Rules

**Example:** Calculate $\displaystyle \int 2 x^3 - x \,\textrm d x$.

**Explanation**

Using the sum and constant factor rules, we get

$$
\begin{aligned}
\int2x^{3} - xdx &= 2\intx^{3}dx - \intxdx \\
&= 2(\frac{x^{3 + 1}}{3 + 1}) - (\frac{x^{1 + 1}}{1 + 1}) + C \\
&= 2(\frac{x^{4}}{4}) - (\frac{x^{2}}{2}) + C \\
&= \frac{x^{4}}{2} - \frac{x^{2}}{2} + C
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: ma-211
content: |-
  What is $\displaystyle \int12x^{3} + 5xdx$?
options:
- id: a
  content: |-
    $12x^{2} + \frac{5x^{2}}{2} + C$
- id: b
  content: |-
    $3x^{2} + \frac{5x^{2}}{2} + C$
- id: c
  content: |-
    $3x^{4} + \frac{5x^{2}}{2} + C$
  correct: true
- id: d
  content: |-
    $3x^{4} + \frac{5x^{3}}{2} + C$
- id: e
  content: |-
    $6x^{4} + \frac{5x^{4}}{2} + C$
```

---

**Question 4:**

```quiz
type: radio
id: ma-2166
content: |-
  What is $\displaystyle \int\frac{1}{x^{2}} - 3xdx$?
options:
- id: a
  content: |-
    $-\frac{2x^{2}}{3} - \frac{1}{x} + C$
- id: b
  content: |-
    $\frac{3x^{2}}{2} - \frac{1}{x} + C$
- id: c
  content: |-
    $-\frac{3x}{2} - \frac{1}{x^{2}} + C$
- id: d
  content: |-
    $-\frac{3x^{2}}{2} - \frac{1}{x} + C$
  correct: true
- id: e
  content: |-
    $-\frac{3x}{2} + \frac{1}{x} + C$
```

---

<a id="integrating-sums-of-power-functions"></a>
## Integrating Sums of Power Functions

**Example:** Calculate $\displaystyle \int \left(5(\sqrt{x})^{3} - 4 x^2 + 5\right) \,\textrm d x$.

**Explanation**

Using the sum and constant factor rules, we get

$$
\begin{aligned}
\int(5(\sqrt{x})^{3} - 4x^{2} + 5)dx &= \int(5x^{3/2} - 4x^{2} + 5)dx \\
&= 5\intx^{3/2}dx - 4\intx^{2}dx + 5\int1dx \\
&= 5(\frac{x^{5/2}}{\frac{5}{2}}) - 4(\frac{x^{3}}{3}) + 5(x) + C \\
&= 5 \cdot \frac{2}{5}x^{5/2} - \frac{4}{3}x^{3} + 5x + C \\
&= 2\sqrt{x^{5}} - \frac{4}{3}x^{3} + 5x + C
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: ma-2250
content: |-
  What is $\displaystyle \int(x^{2} - \sqrt{x} + 2)dx$?
options:
- id: a
  content: |-
    $\frac{x^{3} - 3\sqrt{x^{3}} + 6x}{3} + C$
- id: b
  content: |-
    $\frac{x^{3} - 2\sqrt{x^{3}} + 6x}{3} + C$
  correct: true
- id: c
  content: |-
    $\frac{x^{3} + 2\sqrt[3]{x^{2}} + 2x}{3} + C$
- id: d
  content: |-
    $\frac{x^{3} + 3\sqrt{x^{3}} + 6x}{3} + C$
- id: e
  content: |-
    $\frac{x^{3} - 2\sqrt{x^{3}} + 2x}{3} + C$
```

---

**Question 6:**

```quiz
type: radio
id: ma-29830
content: |-
  Find the antiderivative of
  $4x^{7} + \sqrt[5]{x} - \frac{1}{\sqrt[7]{x^{13}}}$.
options:
- id: a
  content: |-
    $\frac{x^{8}}{2} - \frac{5\sqrt[5]{x^{6}}}{3} + \frac{7}{6\sqrt[7]{x^{6}}} + C$
- id: b
  content: |-
    $\frac{x^{8}}{2} + \frac{6\sqrt[5]{x^{6}}}{5} + \frac{7}{6\sqrt[7]{x^{6}}} + C$
- id: c
  content: |-
    $\frac{x^{8}}{8} + \frac{5\sqrt[5]{x^{6}}}{6} + \frac{7}{6\sqrt[7]{x^{6}}} + C$
- id: d
  content: |-
    $\frac{x^{8}}{2} + \frac{5\sqrt[5]{x^{6}}}{6} + \frac{7}{6\sqrt[7]{x^{6}}} + C$
  correct: true
- id: e
  content: |-
    $\frac{x^{8}}{4} + \frac{5\sqrt[6]{x^{5}}}{6} + \frac{7}{6\sqrt[7]{x^{6}}} + C$
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
