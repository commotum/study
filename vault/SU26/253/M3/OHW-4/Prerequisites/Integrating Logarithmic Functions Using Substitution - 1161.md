# Integrating Logarithmic Functions Using Substitution

<!--
lesson-id: 1161
topic-code: CA2.1.1.9
-->

## Table of Contents

- [Introduction](#introduction)
- [Integrating Functions Containing the Natural Logarithm](#integrating-functions-containing-the-natural-logarithm)
- [Integrating Functions Containing Other Logarithms](#integrating-functions-containing-other-logarithms)
- [Definite Integrals](#definite-integrals)
- [Evaluating Definite Integrals](#evaluating-definite-integrals)

## Prerequisites

- [Calculating Definite Integrals Using Substitution](<../../../../MA/Mathematical-Foundations/MF3/10. Integration Techniques/10.1. Integration Using Substitution/Lessons/10.1.4. Calculating Definite Integrals Using Substitution.md>)

---

<a id="introduction"></a>
## Introduction

Let's think about how to calculate an integral like

$$
\displaystyle \int \dfrac {\ln x} {x} \,\textrm d x
$$

Notice that this integral can be written as

$$
\int \dfrac {\ln x} {x} \,\textrm d x = \int \underbrace{\ln x}_{u} \cdot\overbrace{\dfrac {1} {x}}^{u'} \,\textrm d x
$$

We've seen integrals like this before, where the integrand consists of a function $u(x)$ multiplied by its derivative $u'(x)$. Such integrals can be solved by substitution.

So, we let $u = \ln x$, which gives

$$
\dfrac{\textrm{d}u}{\textrm{d}x}= \dfrac 1 x\quad \Longrightarrow \quad \dfrac 1 x \,\textrm{d}x={\textrm{d}u}
$$

Therefore, we can calculate our integral as follows:

$$
\begin{aligned} \int \dfrac{\ln x}{x}\, \textrm{d}x &=\int \ln x\cdot \dfrac {1} {x} \,\textrm d x \\[5pt] & = \int u \, \textrm{d} u \\[5pt] &= \dfrac{1}{2}u^2 +C \\[5pt] &= \dfrac{1}{2}\ln^2 x +C \end{aligned}
$$

After solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$
\begin{aligned}
\frac{d}{dx}(\frac{1}{2}\ln^{2} x + C) &= \frac{1}{2} \cdot \frac{d}{dx}(\ln^{2} x) + \frac{d}{dx}(C) \\
&= \frac{1}{2} \cdot \frac{d}{dx}[(\ln x)^{2}] + \frac{d}{dx}(C) \\
&= \frac{1}{2} \cdot 2\ln x \cdot \frac{d}{dx}(\ln x) + 0 \\
&= \ln x \cdot \frac{1}{x} \\
&= \frac{\ln x}{x}✓
\end{aligned}
$$

---

<a id="integrating-functions-containing-the-natural-logarithm"></a>
## Integrating Functions Containing the Natural Logarithm

**Example:** Calculate $\displaystyle{\int \dfrac{3}{x \sqrt{\ln x}} \, \textrm{d}x}$.

**Explanation**

Let's set $u = \ln x$. Then, we have

$$
\dfrac{\textrm{d}u}{\textrm{d}x}= \dfrac 1 x\quad\Longrightarrow\quad \textrm{d}u=\dfrac 1 x\,{\textrm{d}x}
$$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$
\begin{aligned}
∫\frac{3}{x\sqrt{\ln x}}dx &= 3∫\frac{1}{\sqrt{\ln x}} \cdot \frac{1}{x}dx \\
&= 3∫\frac{1}{\sqrt{u}}du \\
&= 3∫u^{-1/2}du \\
&= 3 \cdot 2u^{1/2} + C \\
&= 6\sqrt{u} + C \\
&= 6\sqrt{\ln x} + C
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-2202
content: |-
  Calculate the integral $∫\frac{4\ln x}{x}dx$.
options:
- id: a
  content: |-
    $\ln^{2} x + C$
- id: b
  content: |-
    $\frac{\ln^{2} x}{2} + C$
- id: c
  content: |-
    $2\ln x + C$
- id: d
  content: |-
    $-\ln^{2} x + C$
- id: e
  content: |-
    $2\ln^{2} x + C$
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: ma-13814
content: |-
  Calculate the integral $∫(5)/(x\ln^{2} (3x))dx$.
options:
- id: a
  content: |-
    $(5)/(\ln^{2} (3x)) + C$
- id: b
  content: |-
    $(15)/(\ln (3x)) + C$
- id: c
  content: |-
    $- (1)/(\ln (3x)) + C$
- id: d
  content: |-
    $- (5)/(\ln (3x)) + C$
  correct: true
- id: e
  content: |-
    $- (15)/(\ln^{3} (3x))$
```

---

**Question 3:**

```quiz
type: radio
id: ma-13802
content: |-
  Calculate the integral $∫(2)/(x\ln (2x))dx$.
options:
- id: a
  content: |-
    $2\ln \mid \ln (2x) \mid$
- id: b
  content: |-
    $2\ln \mid \ln x \mid + C$
- id: c
  content: |-
    $\ln \mid \ln (2x) \mid + C$
- id: d
  content: |-
    $2\ln \mid \ln (2x) \mid + C$
  correct: true
- id: e
  content: |-
    $\ln \mid \ln x \mid + C$
```

---

<a id="integrating-functions-containing-other-logarithms"></a>
## Integrating Functions Containing Other Logarithms

**Example:** Calculate the integral $\displaystyle \int \dfrac{\log^2_3 x}{x} \,\textrm d x$.

**Explanation**

Let's rewrite our integral as

$$
\int \dfrac{(\log_3 x)^2}{x} \,\textrm d x
$$

Let $u=\log_3 x$. Differentiating, we get

$$
\dfrac{\textrm d u}{\textrm d x} = \dfrac{1}{x\ln 3}\quad\Longrightarrow\quad\ln 3\,\textrm d u = \dfrac 1 x \textrm d x
$$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$
\begin{aligned}
∫((\log_{3} x)^{2})/(x)dx &= ∫(\log_{3} x)^{2} \cdot \frac{1}{x}dx \\
&= ∫u^{2} \cdot \ln 3du \\
&= \ln 3∫u^{2}du \\
&= \ln 3 \cdot \frac{1}{3}u^{3} + C \\
&= \frac{1}{3}\ln 3(\log_{3} x)^{3} + C \\
&= \frac{1}{3}\ln 3\log_{3}^{3} x + C
\end{aligned}
$$

---

**Question 4:**

```quiz
type: radio
id: ma-31329
content: |-
  What is $∫\frac{\log_{2} x}{x}dx$?
options:
- id: a
  content: |-
    $\ln 2 \cdot \frac{\log_{2} x}{2} + C$
- id: b
  content: |-
    $\ln x \cdot \frac{\log_{2}^{2} x}{x} + C$
- id: c
  content: |-
    $\ln x \cdot \frac{\log_{2}^{2} x}{2} + C$
- id: d
  content: |-
    $\ln 3 \cdot \frac{\log_{2} x}{2} + C$
- id: e
  content: |-
    $\ln 2 \cdot \frac{\log_{2}^{2} x}{2} + C$
  correct: true
```

---

**Question 5:**

```quiz
type: radio
id: ma-31401
content: |-
  What is $∫(\log_{3} (x^{2}))/(x)dx$?
options:
- id: a
  content: |-
    $(\ln (x^{2})\log_{3}^{2} (x^{2}))/(2) + C$
- id: b
  content: |-
    $(\ln 2\log_{2}^{2} (x^{2}))/(4) + C$
- id: c
  content: |-
    $(\ln 3\log_{3}^{2} (x^{2}))/(4) + C$
  correct: true
- id: d
  content: |-
    $(\ln 3\log_{3}^{2} (x^{2}))/(2) + C$
- id: e
  content: |-
    $\frac{\ln x\log_{3}^{2} x}{4} + C$
```

---

**Question 6:**

```quiz
type: radio
id: ma-73659
content: |-
  What is $∫(1)/(x\log_{7} (4x))dx$?
options:
- id: a
  content: |-
    $\frac{\ln 7}{7}\ln \mid \log_{7} (4x) \mid + C$
- id: b
  content: |-
    $\ln x^{7}\ln \mid \log_{7} (4x) \mid + C$
- id: c
  content: |-
    $x\ln 7\ln \mid \log_{7} (x^{4}) \mid + C$
- id: d
  content: |-
    $\ln 7\ln \mid \log_{7} (4x) \mid + C$
  correct: true
- id: e
  content: |-
    $\ln 4\ln \mid \log_{7} x \mid + C$
```

---

<a id="definite-integrals"></a>
## Definite Integrals

Let's evaluate the following definite integral:

$$
\displaystyle{\int_{e}^{e^4} \dfrac{3}{x \sqrt{\ln x}} \, \textrm{d}x}
$$

We'll use the change of variable method, which comprises three steps:

**Step 1:** Change the variable.

Let's introduce the new variable $u = \ln x$. Differentiating gives

$$
\dfrac{\textrm{d}u}{\textrm{d}x} = \dfrac{1}{x} \qquad\Longrightarrow\qquad \textrm{d}u = \dfrac{\textrm{d}x}{x}
$$

**Step 2:** Find the new limits of integration.

We use the table below to change our limits of integration from $x$ to $u{:}$

$$
\begin{bmatrix}x & e & e^{4} \\ u & 1 & 4\end{bmatrix}
$$

**Step 3:** Evaluate the integral in the new variable $u$.

$$
\begin{aligned}
∫_{e}^{e^{4}}\frac{3}{x\sqrt{\ln x}}dx &= ∫_{e}^{e^{4}}\frac{3}{\sqrt{\ln x}} \cdot \frac{dx}{x} \\
&= ∫_{1}^{4}\frac{3}{\sqrt{u}} \cdot du \\
&= 3∫_{1}^{4}u^{-1/2}du \\
&= 6u^{1/2} \mid _{1}^{4} \\
&= 6(\sqrt{4} - \sqrt{1}) \\
&= 6(2 - 1) \\
&= 6
\end{aligned}
$$

---

<a id="evaluating-definite-integrals"></a>
## Evaluating Definite Integrals

**Example:** Evaluate $\displaystyle{\int_{e}^{e^2} \dfrac{\ln^2 x}{x}\,\textrm{d}x}$.

**Explanation**

Let's set $u = \ln x$. Then, we have

$$
\dfrac{\textrm{d}u}{\textrm{d}x}= \dfrac 1 x\quad\Longrightarrow\quad \textrm{d}u=\dfrac 1 x\,{\textrm{d}x}
$$

Calculating the limits for $u$ gives the following:
$\begin{bmatrix}x & e & e^{2} \\ u & 1 & 2\end{bmatrix}$

We now substitute and evaluate as follows:

$$
\begin{aligned} \int_{e}^{e^2} \dfrac{\ln^2 x}{x}\,\textrm{d}x &= \int_{e}^{e^2} (\ln x)^2\cdot \dfrac{\textrm{d}x}{x} \\[5pt] &=\int_{1}^{2} u^2\,\textrm{d}u \\[5pt] &=\left.\dfrac13u^{3}\right|_{1}^{2} \\[5pt] &=\dfrac{1}{3}\left(2^3-1^3 \right) \\[5pt] &=\dfrac{1}{3}\left(8-1 \right) \\[5pt] &=\dfrac{7}{3} \end{aligned}
$$

---

**Question 7:**

```quiz
type: radio
id: ma-49605
content: |-
  What is the value of $∫_{e^{2}}^{e^{4}}\frac{8\ln x}{x}dx$?
options:
- id: a
  content: |-
    $2\ln 4$
- id: b
  content: |-
    $68$
- id: c
  content: |-
    $48$
  correct: true
- id: d
  content: |-
    $-4\ln 2$
- id: e
  content: |-
    $\ln^{2} 2$
```

---

**Question 8:**

```quiz
type: radio
id: ma-49607
content: |-
  What is the value of $∫_{e^{4}}^{e^{9}}\frac{3\sqrt{\ln x}}{2x}dx$?
options:
- id: a
  content: |-
    $\frac{1}{9}$
- id: b
  content: |-
    $3\ln (\frac{3}{2})$
- id: c
  content: |-
    $19$
  correct: true
- id: d
  content: |-
    $15$
- id: e
  content: |-
    $\ln (\frac{1}{5})$
```

---

**Question 9:**

```quiz
type: radio
id: ma-73654
content: |-
  What is the value of $∫_{2}^{4}\frac{4}{x\log_{2} x}dx$?
options:
- id: a
  content: |-
    $\ln 2$
- id: b
  content: |-
    $\frac{\ln^{2} 2}{2}$
- id: c
  content: |-
    $2\ln 2$
- id: d
  content: |-
    $8\ln 2$
- id: e
  content: |-
    $4\ln^{2} 2$
  correct: true
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
