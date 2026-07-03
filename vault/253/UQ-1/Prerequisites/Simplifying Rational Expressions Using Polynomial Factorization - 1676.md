# Simplifying Rational Expressions Using Polynomial Factorization

## Table of Contents

- [Introduction](#introduction)
- [Simplifying a Rational Expression by Factoring a Difference of Squares in the Numerator](#simplifying-a-rational-expression-by-factoring-a-difference-of-squares-in-the-numerator)
- [Simplifying a Rational Expression by Factoring a Second-Order Polynomial in the Numerator](#simplifying-a-rational-expression-by-factoring-a-second-order-polynomial-in-the-numerator)
- [Simplifying a Rational Expression by Factoring a Second-Order Polynomial in the Denominator](#simplifying-a-rational-expression-by-factoring-a-second-order-polynomial-in-the-denominator)
- [Simplifying a Rational Expression by Factoring Second-Order Polynomials in Both the Numerator and Denominator](#simplifying-a-rational-expression-by-factoring-second-order-polynomials-in-both-the-numerator-and-denominator)

## Prerequisites

- [Simplifying Rational Expressions by Factoring](../423/423.md)
- [Further Factoring Trinomials With Leading Coefficients](../4951/4951.md)

---

<a id="introduction"></a>
## Introduction

To reduce a rational expression to its lowest terms, we need to factor the numerator and denominator and then cancel out the common factors.

For example, to simplify the rational expression

$$
\dfrac{2x}{2+6x}
$$

we cancel out a factor of $2$ from the numerator and denominator:

$$
\begin{aligned}
\frac{2x}{2 + 6x} &= \frac{2x}{2(1 + 3x)} \\
&= \frac{x}{1 + 3x}
\end{aligned}
$$

Sometimes, however, we can have more complicated expressions which require **polynomial factorization** in order to be simplified.

No need to panic though! The main strategy is always the same: factor the numerator and denominator, and then cancel out common factors.

For example, to simplify the rational expression

$$
\dfrac{x^2-4}{x+2}
$$

we factor the difference of squares in the numerator and then cancel out a common factor:

$$
\begin{aligned}
\frac{x^{2} - 4}{x + 2} &= \frac{(x + 2)(x - 2)}{x + 2} \\
&= x - 2
\end{aligned}
$$

---

<a id="simplifying-a-rational-expression-by-factoring-a-difference-of-squares-in-the-numerator"></a>
## Simplifying a Rational Expression by Factoring a Difference of Squares in the Numerator

**Example:** Simplify $\dfrac{x^2 - 9}{(x + 3)(x + 2)}$.

**Explanation**

The numerator is a difference of squares. If we factor it and then cancel out any common factors that appear in both the numerator and the denominator, we get

$$
\require{cancel} \begin{aligned} \dfrac{x^2 - 9}{(x + 3)(x + 2)} \\[5pt] &= \dfrac{(x + 3)(x - 3)}{(x + 3)(x + 2)} \\[5pt] &= \dfrac{\cancel{(x + 3)}(x - 3)}{\cancel{(x + 3)}(x + 2)} \\[5pt] &= \dfrac{x - 3}{x + 2}. \end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-WHW1-1676-q001
content: |-
  Simplify $\frac{p^{2} - q^{2}}{p - q}$.

options:
- id: a
  content: |-
    $p - q$

- id: b
  content: |-
    $\frac{1}{p + q}$

- id: c
  content: |-
    $p^{2} + q^{2}$

- id: d
  content: |-
    $p + q$
  correct: true

- id: e
  content: |-
    $p^{2} - q^{2}$
```

---

**Question 2:**

```quiz
type: radio
id: MA253-WHW1-1676-q002
content: |-
  Simplify $\frac{a^{2} - 4}{2a - 4}$.

options:
- id: a
  content: |-
    $a - 1$

- id: b
  content: |-
    $\frac{a}{2}$

- id: c
  content: |-
    $\frac{a - 2}{2}$

- id: d
  content: |-
    $a + 1$

- id: e
  content: |-
    $\frac{a + 2}{2}$
  correct: true
```

---

<a id="simplifying-a-rational-expression-by-factoring-a-second-order-polynomial-in-the-numerator"></a>
## Simplifying a Rational Expression by Factoring a Second-Order Polynomial in the Numerator

**Example:** What is $\dfrac{x^2 + x - 6}{x - 2}$ reduced to lowest terms?

**Explanation**

The numerator can be factored as

$$
x^2 + x - 6 = (x + 3)(x - 2)
$$

Cancelling out any common factors that appear in the numerator and the denominator, we get

$$
\begin{aligned}
\frac{x^{2} + x - 6}{x - 2} &= \frac{(x + 3)(x - 2)}{x - 2} \\
&= \frac{x + 3}{1} \\
&= x + 3
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-WHW1-1676-q003
content: |-
  What is $\frac{7z^{2} + 21z + 14}{z + 1}$ reduced to lowest terms?

options:
- id: a
  content: |-
    $7z + 14$
  correct: true

- id: b
  content: |-
    $\frac{7(z + 1)}{z + 2}$

- id: c
  content: |-
    $z + 7$

- id: d
  content: |-
    $7z + 1$

- id: e
  content: |-
    $\frac{7(z + 2)}{z + 1}$
```

---

**Question 4:**

```quiz
type: radio
id: MA253-WHW1-1676-q004
content: |-
  What is $\frac{3z^{2} - 3z - 18}{3z - 9}$ reduced to lowest terms?

options:
- id: a
  content: |-
    $z - 2$

- id: b
  content: |-
    $\frac{1}{z + 2}$

- id: c
  content: |-
    $3z + 2$

- id: d
  content: |-
    $z + 2$
  correct: true

- id: e
  content: |-
    $3(z + 2)$
```

---

<a id="simplifying-a-rational-expression-by-factoring-a-second-order-polynomial-in-the-denominator"></a>
## Simplifying a Rational Expression by Factoring a Second-Order Polynomial in the Denominator

**Example:** Simplify $\dfrac{4(a + b)}{2a^2 + 4ab + 2b^2}$.

**Explanation**

Here, we take out a factor of $2$ from the denominator, and then use the polynomial factorization

$$
a^2 + 2ab + b^2 = (a + b)^2
$$

Cancelling out any common factors that appear in both the numerator and the denominator, we get

$$
\require{cancel} \begin{aligned} \dfrac{4(a + b)}{2a^2 + 4ab + 2b^2} &= \dfrac{4(a + b)}{2\left(a^2 + 2ab + b^2\right)} \\ &= \dfrac{2\cdot 2\cdot(a + b)}{2(a + b)(a + b)} \\ &= \dfrac{\cancel{2}\cdot 2\cdot\cancel{(a + b)}}{\cancel{2}\cancel{(a + b)}(a + b)} \\ &= \dfrac{2}{a + b}. \end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: MA253-WHW1-1676-q005
content: |-
  Simplify $\frac{8(a - b)}{2a^{2} - 4ab + 2b^{2}}$.

options:
- id: a
  content: |-
    $\frac{1}{a - b}$

- id: b
  content: |-
    $\frac{4}{a + b}$

- id: c
  content: |-
    $4(a - b)$

- id: d
  content: |-
    $\frac{1}{4(a + b)}$

- id: e
  content: |-
    $\frac{4}{a - b}$
  correct: true
```

---

**Question 6:**

```quiz
type: radio
id: MA253-WHW1-1676-q006
content: |-
  Simplify $\frac{xy - 2x}{y^{2} + 5y - 14}$.

options:
- id: a
  content: |-
    $\frac{x}{y - 2}$

- id: b
  content: |-
    $\frac{x}{y + 7}$
  correct: true

- id: c
  content: |-
    $\frac{x}{y + 2}$

- id: d
  content: |-
    $\frac{xy^{2}}{y + 7}$

- id: e
  content: |-
    $\frac{x}{y - 7}$
```

---

<a id="simplifying-a-rational-expression-by-factoring-second-order-polynomials-in-both-the-numerator-and-denominator"></a>
## Simplifying a Rational Expression by Factoring Second-Order Polynomials in Both the Numerator and Denominator

**Example:** Simplify $\dfrac{x^2-4}{x^2-5x+6}$.

**Explanation**

We factor the numerator and denominator, canceling out any common factors that appear in both.

$$
\begin{aligned}
\frac{x^{2} - 4}{x^{2} - 5x + 6} &= \frac{(x - 2)(x + 2)}{(x - 3)(x - 2)} \\
&= \frac{x + 2}{x - 3}
\end{aligned}
$$

---

**Question 7:**

```quiz
type: radio
id: MA253-WHW1-1676-q007
content: |-
  What is $\frac{x^{2} + 5x + 6}{x^{2} + 4x + 4}$ reduced to lowest terms?

options:
- id: a
  content: |-
    $\frac{x^{2} + 5x + 6}{x^{2} + 4x + 4}$

- id: b
  content: |-
    $\frac{x + 3}{x + 2}$
  correct: true

- id: c
  content: |-
    $x + 3$

- id: d
  content: |-
    $\frac{x + 2}{1}$

- id: e
  content: |-
    $\frac{1}{x + 2}$
```

---

**Question 8:**

```quiz
type: radio
id: MA253-WHW1-1676-q008
content: |-
  What is $\frac{y^{2} - 9}{y^{2} - 6y + 9}$ reduced to lowest terms?

options:
- id: a
  content: |-
    $\frac{y^{2} - 3}{y^{2} - 2y + 3}$

- id: b
  content: |-
    $\frac{y^{2} - 9}{y^{2} - 6y + 9}$

- id: c
  content: |-
    $\frac{y + 3}{y - 3}$
  correct: true

- id: d
  content: |-
    $\frac{y - 3}{y + 3}$

- id: e
  content: |-
    $y + 3$
```
---

## Navigation

- [Next: Improper Integrals](<Improper Integrals - 758.md>)
- [Back to UQ-1](../UQ-1.md)
