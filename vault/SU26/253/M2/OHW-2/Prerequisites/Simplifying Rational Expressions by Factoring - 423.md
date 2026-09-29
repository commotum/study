# Simplifying Rational Expressions by Factoring

<!--
lesson-id: 423
topic-code: MF1.7.2.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Simplifying Rational Expressions With Common Constant Factors](#simplifying-rational-expressions-with-common-constant-factors)
- [Simplifying Rational Expressions With Common Factors](#simplifying-rational-expressions-with-common-factors)
- [Identifying Irreducible Rational Expressions](#identifying-irreducible-rational-expressions)
- [Simplifying Rational Expressions With Longer Numerators and Denominators](#simplifying-rational-expressions-with-longer-numerators-and-denominators)

## Prerequisites

- [Simplifying Rational Expressions](<../../../../MA/Mathematical-Foundations/MF1/7. Radical & Rational Expressions/7.2. Rational Expressions/Lessons/7.2.2. Simplifying Rational Expressions.md>)
- [Factoring Linear Expressions](<../../../../MA/Mathematical-Foundations/MF1/5. Equations & Inequalities/5.2. Simplifying Linear Expressions/Lessons/5.2.9. Factoring Linear Expressions.md>)

---

<a id="introduction"></a>
## Introduction

To simplify a rational expression, we cancel out the largest common factor from the numerator and denominator. To do this, we sometimes need to factor the numerator and denominator before canceling.

For example, suppose that we wish to simplify

$$
\dfrac {4x - 12} {10x + 4}
$$

To do this, we factor the numerator and denominator and cancel any factors that they have in common.

$$
\begin{aligned} \dfrac {4x - 12} {10x + 4} &=\dfrac {4(x - 3)} {2(5x + 2)} \\[5pt] &=\dfrac {2 \cdot 2 \cdot (x - 3)} {2(5x + 2)} \\[5pt] &=\dfrac {\cancel{2} \cdot 2(x - 3)} {\cancel{2}(5x + 2)} \\[5pt] &=\dfrac {2(x - 3)} {5x + 2} \end{aligned}
$$

---

<a id="simplifying-rational-expressions-with-common-constant-factors"></a>
## Simplifying Rational Expressions With Common Constant Factors

**Example:** What is $\dfrac {2x + 4} {2}$ reduced to lowest terms?

**Explanation**

We factor the numerator and denominator and cancel any factors that they have in common.

$$
\begin{aligned}
\frac{2x + 4}{2} &= (2(x + 2))/(2) \\
&= (2(x + 2))/(2 \cdot 1) \\
&= \frac{x + 2}{1} \\
&= x + 2
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  What is $\frac{4z - 8x}{2z - 4y}$ reduced to its lowest terms?
options:
- id: a
  content: |-
    $\frac{z + 2x}{z + 2y}$
- id: b
  content: |-
    $\frac{z - 2x}{z - 2y}$
- id: c
  content: |-
    $2$
- id: d
  content: |-
    $4$
- id: e
  content: |-
    $(2(z - 2x))/(z - 2y)$
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  What is $\frac{6b + 6a}{6a}$?
options:
- id: a
  content: |-
    $6b$
- id: b
  content: |-
    $b + a$
- id: c
  content: |-
    $b$
- id: d
  content: |-
    $b + 1$
- id: e
  content: |-
    $\frac{b + a}{a}$
  correct: true
```

---

<a id="simplifying-rational-expressions-with-common-factors"></a>
## Simplifying Rational Expressions With Common Factors

**Example:** Simplify the expression $\dfrac {6y + 2} {3xy + x}$.

**Explanation**

We factor the numerator and denominator and cancel any factors that they have in common.

$$
\require{cancel} \begin{aligned} \dfrac {6y + 2} {3xy + x} &= \dfrac {6y + 2} {x(3y + 1)} \\[5pt] &=\dfrac {2(3y + 1)} {x(3y + 1)} \\[5pt] &=\dfrac {2\cancel{(3y + 1)}} {x \cancel{(3y + 1)}} \\[5pt] &=\dfrac {2} {x} \end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  What is $\frac{4xy - x}{4y - 1}$?
options:
- id: a
  content: |-
    Not reducible
- id: b
  content: |-
    $xy$
- id: c
  content: |-
    $\frac{1}{y}$
- id: d
  content: |-
    $\frac{x}{y}$
- id: e
  content: |-
    $x$
  correct: true
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  What is $\frac{ab - b}{3a - 3}$?
options:
- id: a
  content: |-
    $\frac{b}{a}$
- id: b
  content: |-
    Not reducible
- id: c
  content: |-
    $\frac{b}{3}$
  correct: true
- id: d
  content: |-
    $\frac{3}{b}$
- id: e
  content: |-
    $\frac{a}{b}$
```

---

<a id="identifying-irreducible-rational-expressions"></a>
## Identifying Irreducible Rational Expressions

**Example:** What is $\dfrac{x+2}{2x}$ reduced to lowest terms?

**Explanation**

The numerator and denominator have no common factors, so the expression can not be reduced. The expression

$$
\dfrac{x+2}{2x}
$$

is already in lowest terms.

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  What is $\frac{7x + 1}{7x}$?
options:
- id: a
  content: |-
    $7$
- id: b
  content: |-
    $1$
- id: c
  content: |-
    $7x$
- id: d
  content: |-
    $\frac{7x + 1}{7x}$
  correct: true
- id: e
  content: |-
    $7x + 1$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  What is $\frac{3a + 4}{2}$?
options:
- id: a
  content: |-
    $2$
- id: b
  content: |-
    $3a + 2$
- id: c
  content: |-
    $3a + 4$
- id: d
  content: |-
    $\frac{3a + 4}{2}$
  correct: true
- id: e
  content: |-
    $\frac{3a}{2}$
```

---

<a id="simplifying-rational-expressions-with-longer-numerators-and-denominators"></a>
## Simplifying Rational Expressions With Longer Numerators and Denominators

**Example:** Simplify $\dfrac{5c + 10p - 20}{5p+15}$.

**Explanation**

We factor the numerator and denominator and cancel any factors that they have in common.

$$
\begin{aligned}
\frac{5c + 10p - 20}{5p + 15} &= (5(c + 2p - 4))/(5(p + 3)) \\
&= (5(c + 2p - 4))/(5(p + 3)) \\
&= \frac{c + 2p - 4}{p + 3}
\end{aligned}
$$

---

**Question 7:**

```quiz
type: radio
id: q-7
content: |-
  What is $\frac{4ab - 8 + 10x}{10x + 8 - 2ab}$ reduced to its lowest terms?
options:
- id: a
  content: |-
    $-2$
- id: b
  content: |-
    $\frac{ab - 2 + 5x}{5x + 2 - ab}$
- id: c
  content: |-
    $\frac{ab - 4 + 5x}{5x + 4 - ab}$
- id: d
  content: |-
    $\frac{2ab - 4 + 5x}{5x + 4 - ab}$
  correct: true
- id: e
  content: |-
    $2$
```

---

**Question 8:**

```quiz
type: radio
id: q-8
content: |-
  What is $\frac{8a - 4b + 12}{20b + 8a}$ reduced to its lowest terms?
options:
- id: a
  content: |-
    $\frac{2a - b + 3}{5b + 2a}$
  correct: true
- id: b
  content: |-
    $\frac{2a - b}{5b + 2a}$
- id: c
  content: |-
    $\frac{-b + 5}{4b}$
- id: d
  content: |-
    $\frac{-4b + 12}{20b}$
- id: e
  content: |-
    $\frac{2a + b - 3}{5b - 2a}$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
