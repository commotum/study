# Integration by Substitution With Inverse Trigonometric Functions

<!--
lesson-id: 315
topic-code: MF3.10.1.10
-->

## Table of Contents

- [Introduction](#introduction)
- [Calculating Indefinite Integrals Using Substitution with Inverse Sine](#calculating-indefinite-integrals-using-substitution-with-inverse-sine)
- [Calculating Indefinite Integrals Using Substitution with Inverse Tangent](#calculating-indefinite-integrals-using-substitution-with-inverse-tangent)
- [Calculating Indefinite Integrals Using Substitution with Inverse Secant](#calculating-indefinite-integrals-using-substitution-with-inverse-secant)
- [Calculating Definite Integrals Using Substitution with Inverse Trigonometric Functions](#calculating-definite-integrals-using-substitution-with-inverse-trigonometric-functions)
- [Summary of Key Results](#summary-of-key-results)

## Prerequisites

- [Evaluating Expressions Containing Inverse Trigonometric Functions](<../../../../MA/Mathematical-Foundations/MF3/5. Trigonometry/5.1. The Inverse Trigonometric Functions/Lessons/5.1.4. Evaluating Expressions Containing Inverse Trigonometric Functions.md>)
- [Calculating Definite Integrals Using Substitution](<../../../../MA/Mathematical-Foundations/MF3/10. Integration Techniques/10.1. Integration Using Substitution/Lessons/10.1.4. Calculating Definite Integrals Using Substitution.md>)

---

<a id="introduction"></a>
## Introduction

Consider the integral

$$
\int \dfrac{1}{\sqrt{1-4x^2}} \, \textrm{d}x
$$

This integral, apart from the coefficient of $4$ in the denominator, resembles the basic integral

$$
\int \frac{1}{\sqrt{1-u^2}}\textrm{d}u = \arcsin(u)+C
$$

In fact, they look almost the same, but instead of $u^2$ as the variable, we have

$$
4x^2 = (2x)^2
$$

So, let's substitute $u=2x$. Differentiating, we get

$$
\dfrac{\textrm{d}u}{\textrm{d}x}=2\quad\Longrightarrow\quad \dfrac 1 2 \textrm d u = \textrm d x
$$

We can now write the integral in terms of $u$, and evaluate:

$$
\begin{aligned}
∫\frac{1}{\sqrt{1 - 4x^{2}}}dx &= ∫(1)/(\sqrt{1 - (2x)^{2}})dx \\
&= ∫\frac{1}{\sqrt{1 - u^{2}}} \cdot \frac{1}{2}du \\
&= \frac{1}{2}∫\frac{1}{\sqrt{1 - u^{2}}}du \\
&= \frac{1}{2}\arcsin (u) + C \\
&= \frac{1}{2}\arcsin (2x) + C
\end{aligned}
$$

We can often use this trick whenever we see an integral that closely resembles an integral for an inverse trigonometric function.

**Note:** As always, after solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$
\begin{aligned}
\frac{d}{dx}[\frac{1}{2}\arcsin (2x) + C] &= \frac{1}{2} \cdot \frac{d}{dx}[\arcsin (2x)] + \frac{d}{dx}(C) \\
&= \frac{1}{2} \cdot (1)/(\sqrt{1 - (2x)^{2}}) \cdot \frac{d}{dx}(2x) + 0 \\
&= \frac{1}{2} \cdot \frac{1}{\sqrt{1 - 4x^{2}}} \cdot 2 \\
&= \frac{1}{\sqrt{1 - 4x^{2}}}✓
\end{aligned}
$$

---

<a id="calculating-indefinite-integrals-using-substitution-with-inverse-sine"></a>
## Calculating Indefinite Integrals Using Substitution with Inverse Sine

**Example:** Calculate the integral $\displaystyle \int \dfrac{9}{4\sqrt{1-9x^2}} \, \textrm{d}x$.

**Explanation**

This integral resembles the basic integral for inverse sine,

$$
\int \frac{1}{\sqrt{1-u^2}}\textrm{d}u = \arcsin(u)+C
$$

The only difference is that instead of $u^2$ as the variable, we have

$$
9x^2 = (3x)^2
$$

So, let's substitute $u=3x$. Differentiating, we get

$$
\dfrac{\textrm{d}u}{\textrm{d}x}=3\quad\Longrightarrow\quad \dfrac 1 3 \,\textrm d u=\textrm d x
$$

We can now write the integral in terms of $u$, and evaluate:

$$
\begin{aligned}
∫\frac{9}{4\sqrt{1 - 9x^{2}}}dx &= \frac{9}{4}∫(1)/(\sqrt{1 - (3x)^{2}})dx \\
&= \frac{9}{4}∫\frac{1}{\sqrt{1 - u^{2}}} \cdot \frac{1}{3}du \\
&= \frac{9}{12}∫\frac{1}{\sqrt{1 - u^{2}}}du \\
&= \frac{3}{4} \cdot \arcsin u + C \\
&= \frac{3}{4}\arcsin 3x + C
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  What is $∫\frac{1}{\sqrt{1 - 4x^{2}}}dx$?
options:
- id: a
  content: |-
    $(\arcsin (2x))/(2) + C$
  correct: true
- id: b
  content: |-
    $(\arccos (2x))/(2) + C$
- id: c
  content: |-
    $(\arcsin (4x))/(4) + C$
- id: d
  content: |-
    $2\arcsin (2x) + C$
- id: e
  content: |-
    $(\arccos (4x))/(4) + C$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  What is $∫\frac{3}{\sqrt{49 - x^{2}}}dx$?
options:
- id: a
  content: |-
    $3\arctan (\frac{x}{7}) + C$
- id: b
  content: |-
    $(\arcsin (\frac{x}{7}))/(3) + C$
- id: c
  content: |-
    $(3\arcsin (\frac{x}{7}))/(7) + C$
- id: d
  content: |-
    $3\arctan (7x) + C$
- id: e
  content: |-
    $3\arcsin (\frac{x}{7}) + C$
  correct: true
```

---

<a id="calculating-indefinite-integrals-using-substitution-with-inverse-tangent"></a>
## Calculating Indefinite Integrals Using Substitution with Inverse Tangent

**Example:** Calculate the integral $\displaystyle{\int \dfrac{3}{2 + 50x^2} \, \textrm{d}x}$.

**Explanation**

Note that we can rewrite this integral as

$$
\int \dfrac{3}{2 + 50x^2} \, \textrm{d}x = \int \dfrac{3}{2(1 + 25x^2)} = \dfrac 3 2 \int \dfrac{1}{1+25x^2}\,\textrm d x
$$

This integral resembles the basic integral for inverse tangent,

$$
\int \frac{1}{1+u^2}\textrm{d}u =\arctan u +C
$$

The only difference is that instead of $u^2$ as the variable, we have

$$
25x^2 = (5x)^2
$$

So, let's substitute $u=5x$. Differentiating, we get

$$
\dfrac{\textrm{d}u}{\textrm{d}x}=5\quad\Longrightarrow\quad \dfrac 1 5\,\textrm d u = \textrm d x
$$

We can now write the integral in terms of $u$, and evaluate:

$$
\begin{aligned}
∫\frac{3}{2 + 50x^{2}}dx &= \frac{3}{2}∫\frac{1}{1 + 25x^{2}}dx \\
&= \frac{3}{2}∫(1)/(1 + (5x)^{2})dx \\
&= \frac{3}{2}∫\frac{1}{1 + u^{2}} \cdot \frac{1}{5}du \\
&= \frac{3}{10}∫\frac{1}{1 + u^{2}}du \\
&= \frac{3}{10} \cdot \arctan u + C \\
&= \frac{3}{10}\arctan 5x + C
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  What is $∫\frac{6}{1 + 9x^{2}}dx$?
options:
- id: a
  content: |-
    $6\arctan (3x) + C$
- id: b
  content: |-
    $(\arcsin (3x))/(3) + C$
- id: c
  content: |-
    $2\arctan (3x) + C$
  correct: true
- id: d
  content: |-
    $2\arcsin (3x) + C$
- id: e
  content: |-
    $(\arctan (3x))/(3) + C$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  What is $∫\frac{1}{9 + x^{2}}dx$?
options:
- id: a
  content: |-
    $\frac{1}{3}\arctan (\frac{x}{3}) + C$
  correct: true
- id: b
  content: |-
    $\arctan (\frac{x}{9}) + C$
- id: c
  content: |-
    $\arctan (\frac{x}{3}) + C$
- id: d
  content: |-
    $\frac{1}{3}\arctan (\frac{x}{9}) + C$
- id: e
  content: |-
    $\frac{1}{9}\arctan (\frac{x}{9}) + C$
```

---

<a id="calculating-indefinite-integrals-using-substitution-with-inverse-secant"></a>
## Calculating Indefinite Integrals Using Substitution with Inverse Secant

**Example:** ${\displaystyle \int \dfrac{5\, \textrm{d}x}{\mid 5x \mid \sqrt{(5x)^2-1}} =}$

**Explanation**

This resembles the basic integral for $\textrm{arcsec}$,

$$
\int \frac{1}{\mid u \mid \sqrt{u^2-1}} \textrm{d}u = \textrm{arcsec}(u)+C
$$

Let $u = 5x$. Then

$$
\dfrac{\textrm{d}u}{\textrm{d}x}=5 \quad\Longrightarrow\quad 5\,\textrm{d}x = \textrm{d}u
$$

Therefore,

$$
\begin{aligned}
∫(5dx)/(\begin{vmatrix}5x & \sqrt{(5x)^{2} - 1}) &= ∫\frac{du}{\mid u\end{vmatrix}\sqrt{u^{2} - 1}} \\
&= arcsec(u) + C \\
&= arcsec(5x) + C
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  What is $∫(8dx)/(\mid 8x \mid \sqrt{(8x)^{2} - 1})$?
options:
- id: a
  content: |-
    $4arcsec(8x) + C$
- id: b
  content: |-
    $arcsec(8x) + C$
  correct: true
- id: c
  content: |-
    $(arcsec(4x))/(4) + C$
- id: d
  content: |-
    $arcsec(64x) + C$
- id: e
  content: |-
    $(arcsec(8x))/(8) + C$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  What is $∫\frac{2}{\mid x \mid \sqrt{4x^{2} - 1}}dx$?
options:
- id: a
  content: |-
    $arcsec(2x) + C$
- id: b
  content: |-
    $4arcsec(2x) + C$
- id: c
  content: |-
    $2arcsec(2x) + C$
  correct: true
- id: d
  content: |-
    $(arcsec(2x))/(2) + C$
- id: e
  content: |-
    $(arcsec(2x))/(4) + C$
```

---

<a id="calculating-definite-integrals-using-substitution-with-inverse-trigonometric-functions"></a>
## Calculating Definite Integrals Using Substitution with Inverse Trigonometric Functions

**Example:** Evaluate the integral $\displaystyle{\int_{0}^{\sqrt 2} \dfrac{1}{2+x^2}\, \textrm{d}x}$.

**Explanation**

First, we rewrite the integral as

$$
\begin{aligned}
∫_{0}^{\sqrt{2}}\frac{1}{2 + x^{2}}dx &= ∫_{0}^{\sqrt{2}}(1)/(2(1 + x^{2}/2))dx \\
&= ∫_{0}^{\sqrt{2}}(1)/(2(1 + (x/\sqrt{2})^{2}))dx \\
&= \frac{1}{2}∫_{0}^{\sqrt{2}}(1)/(1 + (x/\sqrt{2})^{2})dx
\end{aligned}
$$

We see that this integral now resembles the basic integral for the inverse tangent,

$$
\int\dfrac{1}{1+u^2}\,\textrm d u = \arctan{u} + C
$$

We make the substitution

$$
u=\dfrac{x}{\sqrt 2}
$$

Differentiating, we get

$$
\dfrac{\textrm d u}{\textrm d x} = \dfrac{1}{\sqrt 2}\quad\Longrightarrow\quad \sqrt 2 \,\textrm d u = \textrm d x
$$

Before substituting, we use the table below to change the limits from $x$ to $u$.

| $x$ | $0$ | $\sqrt2$ |
| --- | ---: | ---: |
| $u$ | $0$ | $1$ |

Using the above, we can now write the integral in terms of $u$, and evaluate:

$$
\begin{aligned}
∫_{0}^{\sqrt{2}}\frac{1}{2 + x^{2}}dx &= \frac{1}{2}∫_{0}^{1}\frac{1}{1 + u^{2}} \cdot \sqrt{2}du \\
&= \frac{\sqrt{2}}{2}∫_{0}^{1}\frac{1}{1 + u^{2}}du \\
&= \frac{\sqrt{2}}{2}\arctan u \mid _{0}^{1} \\
&= \frac{\sqrt{2}}{2}(\arctan 1 - \arctan 0) \\
&= \frac{\sqrt{2}}{2}(\frac{π}{4} - 0) \\
&= \frac{π\sqrt{2}}{8}
\end{aligned}
$$

---

**Question 7:**

```quiz
type: radio
id: q-7
content: |-
  Evaluate the integral $∫_{0}^{7}\frac{9}{2 + 8x^{2}}dx$.
options:
- id: a
  content: |-
    $\frac{9}{4}\arctan (14)$
  correct: true
- id: b
  content: |-
    $\frac{9}{4}\arctan (7)$
- id: c
  content: |-
    $\frac{9}{2}\arctan (14)$
- id: d
  content: |-
    $9\arctan (14)$
- id: e
  content: |-
    $\frac{9}{2}\arctan (7)$
```

---

**Question 8:**

```quiz
type: radio
id: q-8
content: |-
  Evaluate the integral $∫_{0}^{1}\frac{2}{\sqrt{2 - x^{2}}}dx$.
options:
- id: a
  content: |-
    $\frac{3π}{2}$
- id: b
  content: |-
    $\frac{π}{3}$
- id: c
  content: |-
    $\frac{π}{2}$
  correct: true
- id: d
  content: |-
    $\frac{π}{4}$
- id: e
  content: |-
    $\frac{π}{6}$
```

---

<a id="summary-of-key-results"></a>
## Summary of Key Results

In this lesson, we learned how to use substitution to evaluate integrals that give rise to inverse trigonometric functions.

Although you can always solve these integrals by going through the substitution process, it is convenient to remember the following key results:

$$
\begin{aligned}
∫(1)/(\sqrt{1 - (ax)^{2}})dx &= \frac{1}{a}\arcsin (ax) + C \\
∫\frac{1}{\sqrt{a^{2} - x^{2}}}dx &= \arcsin (\frac{x}{a}) + C \\
∫(1)/(1 + (ax)^{2})dx &= \frac{1}{a}\arctan (ax) + C \\
∫\frac{1}{a^{2} + x^{2}}dx &= \frac{1}{a}\arctan (\frac{x}{a}) + C \\
∫(1)/(\mid ax \mid \sqrt{(ax)^{2} - 1})dx &= \frac{1}{a}arcsec(ax) + C
\end{aligned}
$$

To remember the results above, note the following:

- Whenever the integrand has an $ax$ term, the argument of the resulting inverse trigonometric function is $ax$.
- Otherwise, if the $a$ and $x$ are separated, then the argument of the resulting inverse trigonometric function is $\dfrac{x}{a}$.
- All the results are multiplied by $\dfrac{1}{a}$, except for $\arcsin \left(\dfrac{x}{a} \right) + C$.

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
