# Vertical Asymptotes of Rational Functions

<!--
lesson-id: 807
topic-code: MF2.6.3.8
-->

## Table of Contents

- [Introduction](#introduction)
- [Calculating the Vertical Asymptotes of a Rational Function](#calculating-the-vertical-asymptotes-of-a-rational-function)
- [Calculating Vertical Asymptotes With Common Factors in the Numerator and Denominator](#calculating-vertical-asymptotes-with-common-factors-in-the-numerator-and-denominator)
- [Calculating Vertical Asymptotes When the Denominator Has Complex Roots](#calculating-vertical-asymptotes-when-the-denominator-has-complex-roots)
- [Calculating Vertical Asymptotes With Common Factors When the Denominator Has Complex Roots](#calculating-vertical-asymptotes-with-common-factors-when-the-denominator-has-complex-roots)

## Prerequisites

- [The Discriminant of a Quadratic Equation](<../../../1. Quadratics/1.1. Quadratic Equations/Lessons/1.1.15. The Discriminant of a Quadratic Equation.md>)
- [Factoring Cubic Expressions by Grouping](<../../../2. Polynomials/2.2. Factoring Polynomials/Lessons/2.2.3. Factoring Cubic Expressions by Grouping.md>)
- [Factoring Sums and Differences of Cubes](<../../../2. Polynomials/2.2. Factoring Polynomials/Lessons/2.2.4. Factoring Sums and Differences of Cubes.md>)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](<../../../1. Quadratics/1.1. Quadratic Equations/Lessons/1.1.8. Solving Quadratic Equations with Leading Coefficients by Factoring.md>)
- [Simplifying Rational Expressions Using Polynomial Factorization](<../../6.1. Rational Expressions/Lessons/6.1.1. Simplifying Rational Expressions Using Polynomial Factorization.md>)

---

<a id="introduction"></a>
## Introduction

A **vertical asymptote** is a vertical line to which a function gets very close but never touches.

For example, let's consider the rational function

$$
f(x) = \dfrac{1}{(x-2)(x+2)}
$$

The graph of $y=f(x)$ is shown below.

![](<../Source/Vertical Asymptotes of Rational Functions - 807/Images/5f5826d19b1d277374ccb3488a6692af.png>)

The two dotted lines $x=2$ and $x=-2$ are the vertical asymptotes of the function. The function gets closer and closer to these lines but never touches them.

But how can we calculate the vertical asymptotes of a function without using a graph?

In general, we can find the vertical asymptotes of a rational function using the following procedure:

1. Factor the numerator and denominator and cancel any common factors.
2. Set the denominator equal to zero and solve for $x$.

In our case, the function is already factored, and there are no common factors in the numerator and denominator. So, to find the vertical asymptotes, we set the denominator equal to zero and solve for $x{:}$

$$
(x-2)(x+2) = 0
$$

The solutions to this equation are $x=2$ and $x=-2$. Therefore, the equations of the vertical asymptotes are $x=-2$ and $x=2$. This matches up with what we saw in the graph.

---

<a id="calculating-the-vertical-asymptotes-of-a-rational-function"></a>
## Calculating the Vertical Asymptotes of a Rational Function

**Example:** Determine the vertical asymptotes of $f(x) = \dfrac{1}{x^2-x-6}$.

**Explanation**

To find the vertical asymptotes of a rational function, we factor the numerator and denominator and cancel any common factors. Then, we set the denominator equal to zero and solve for $x$.

Factoring the numerator and denominator, we get

$$
f(x) = (1)/((x + 2)(x - 3))
$$

There are no common factors in the numerator and denominator, so we set the denominator equal to zero and solve for $x$:

$$
\begin{aligned}
(x + 2)(x - 3) &= 0
\end{aligned}
$$

This gives the two solutions $x = -2$ and $x = 3$. Therefore, the equations of the vertical asymptotes are $x = -2$ and $x = 3$.

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Determine the vertical asymptotes of $f(x) = \frac{1}{x^{2} + 6x - 16}$.
options:
- id: a
  content: |-
    $x =-12, x = 3$
- id: b
  content: |-
    $x =-5, x = 1$
- id: c
  correct: true
  content: |-
    $x =-8, x = 2$
- id: d
  content: |-
    $x =-2, x = \frac{1}{4}$
- id: e
  content: |-
    $x = 3, x = \frac{1}{2}$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Calculate the vertical asymptotes of $f(x) = \frac{3x^{2} - 12x}{x^{2} - 2x - 3}$.
options:
- id: a
  content: |-
    No vertical asymptotes
- id: b
  correct: true
  content: |-
    $x =-1, x = 3$
- id: c
  content: |-
    $x = 3$ only
- id: d
  content: |-
    $x =-1$ only
- id: e
  content: |-
    $x = 1, x = 4$
```

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Calculate the vertical asymptotes of $f(x) = \frac{2}{2 - x} + \frac{3}{2 + x}$.
options:
- id: a
  content: |-
    $x = 0, x = 2$
- id: b
  content: |-
    $x = 2$ only
- id: c
  content: |-
    $x =-2, x = 1$
- id: d
  correct: true
  content: |-
    $x =-2, x = 2$
- id: e
  content: |-
    $x =-2, x = 0, x = 2$
```

---

<a id="calculating-vertical-asymptotes-with-common-factors-in-the-numerator-and-denominator"></a>
## Calculating Vertical Asymptotes With Common Factors in the Numerator and Denominator

**Example:** Determine the vertical asymptotes of $f(x) = \dfrac{x-2}{x^2-6x+8}$.

**Explanation**

To find the vertical asymptotes of a rational function, we factor the numerator and denominator and cancel any common factors. Then, we set the denominator equal to zero and solve for $x$.

Factoring the numerator and denominator and canceling any common factors, we get

$$
\begin{aligned}
f(x) &= \frac{x - 2}{x^{2} - 6x + 8} \\
&= (x - 2)/((x - 2)(x - 4)) \\
&= (x - 2)/((x - 2)(x - 4)) \\
&= \frac{1}{x - 4}
\end{aligned}
$$

Next, we set the denominator equal to zero and solve for $x$:
$x - 4 = 0$

This gives the solution $x = 4$. Therefore, $x = 4$ is the only vertical asymptote.

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Calculate the vertical asymptotes of $f(x) = (x)/(x(x - 2))$.
options:
- id: a
  content: |-
    $x = 0, x = 2$
- id: b
  content: |-
    $x = 0$ only
- id: c
  correct: true
  content: |-
    $x = 2$ only
- id: d
  content: |-
    The function has no vertical asymptotes
- id: e
  content: |-
    $x =-2, x = 2$
```

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  Determine the vertical asymptotes of $f(x) = \frac{x - 2}{x^{2} + 2x - 8}$.
options:
- id: a
  content: |-
    $x =-4, x = 2$
- id: b
  correct: true
  content: |-
    $x =-4$ only
- id: c
  content: |-
    $x = 2, x = 4$
- id: d
  content: |-
    $x =-2, x = 0$
- id: e
  content: |-
    $x = 2$ only
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Calculate the vertical asymptotes of $f(x) = \frac{x^{2} - 3x + 2}{x^{2} + x - 2}$.
options:
- id: a
  content: |-
    $x = 2$ only
- id: b
  correct: true
  content: |-
    $x =-2$ only
- id: c
  content: |-
    $x = 1$ only
- id: d
  content: |-
    $x = ± 2, x = 1$
- id: e
  content: |-
    $x =-2, x = 1$
```

---

<a id="calculating-vertical-asymptotes-when-the-denominator-has-complex-roots"></a>
## Calculating Vertical Asymptotes When the Denominator Has Complex Roots

**Example:** Find the vertical asymptotes of the function $f(x)=\dfrac{2}{x^3+x^2+4x}$.

**Explanation**

To find the vertical asymptotes of a rational function, we factor the numerator and denominator and cancel any common factors. Then, we set the denominator equal to zero and solve for $x$.

Factoring the numerator and denominator, we get

$$
\begin{aligned}
f(x) &= \frac{2}{x^{3} + x^{2} + 4x} \\
&= (2)/(x(x^{2} + x + 4))
\end{aligned}
$$

There are no common factors in the numerator and denominator, so we set the denominator equal to zero. This gives

$$
x(x^2 +x+ 4) = 0
$$

We now solve the above equation using the zero product property:

- Solving $x = 0$ gives the solution $x = 0$.
- The equation $x^2 +x+ 4 = 0$ has no real solutions because the discriminant $\mathcal D$ is negative:
$D|= b^{2} - 4ac; = (1)^{2} - 4(1)(4); = 1 - 16; =-15$

Therefore, the only vertical asymptote is $x = 0$.

---

**Question 7:**

```quiz
type: radio
id: q-7
content: |-
  Calculate the vertical asymptotes of $f(x) = \frac{1}{x^{2} - 4x + 5}$.
options:
- id: a
  content: |-
    $x = 1, x = 5$
- id: b
  content: |-
    $x = 5$ only
- id: c
  correct: true
  content: |-
    The function has no vertical asymptotes
- id: d
  content: |-
    $x =-1, x = 5$
- id: e
  content: |-
    $x = 1$ only
```

---

**Question 8:**

```quiz
type: radio
id: q-8
content: |-
  Calculate the vertical asymptotes of $f(x) = \frac{5}{x^{3} + x^{2} + x}$.
options:
- id: a
  content: |-
    $x = 1, x =-1$
- id: b
  content: |-
    $x = 1, x = 0$
- id: c
  content: |-
    $x = \frac{1}{2}$ only
- id: d
  correct: true
  content: |-
    $x = 0$ only
- id: e
  content: |-
    $x =-1, x =-\frac{1}{2}$
```

---

**Question 9:**

```quiz
type: radio
id: q-9
content: |-
  Calculate the vertical asymptotes of $f(x) = \frac{2x}{x^{3} - 27}$.
options:
- id: a
  correct: true
  content: |-
    $x = 3$ only
- id: b
  content: |-
    $x =-3, x = 0, x = 3$
- id: c
  content: |-
    $x =-3$ only
- id: d
  content: |-
    $x = 9$ only
- id: e
  content: |-
    No vertical asymptotes
```

---

<a id="calculating-vertical-asymptotes-with-common-factors-when-the-denominator-has-complex-roots"></a>
## Calculating Vertical Asymptotes With Common Factors When the Denominator Has Complex Roots

**Example:** Determine the vertical asymptotes of $f(x) = \dfrac{x^2-x-6}{x^3 - 3 x^2 + x - 3}$.

**Explanation**

To find the vertical asymptotes of a rational function, we factor the numerator and denominator and cancel any common factors. Then, we set the denominator equal to zero and solve for $x$.

Factoring the numerator and denominator and canceling any common factors, we get

$$
\begin{aligned}
f(x) &= \frac{x^{2} - x - 6}{x^{3} - 3x^{2} + x - 3} \\
&= ((x + 2)(x - 3))/(x^{2}(x - 3) + (x - 3)) \\
&= ((x + 2)(x - 3))/((x^{2} + 1)(x - 3)) \\
&= ((x + 2)(x - 3))/((x^{2} + 1)(x - 3)) \\
&= \frac{x + 2}{x^{2} + 1}
\end{aligned}
$$

Next, we set the denominator equal to zero:

$$
x^2 + 1 = 0
$$

This equation does not have any real solutions because the discriminant $\mathcal D$ is negative:

$$
\begin{aligned}
D &= b^{2} - 4ac \\
&= (0)^{2} - 4(1)(1) \\
&= 0 - 4 \\
&=-4
\end{aligned}
$$

Therefore, $f(x)$ has no vertical asymptotes.

---

**Question 10:**

```quiz
type: radio
id: q-10
content: |-
  Calculate the vertical asymptotes of $f(x) = \frac{x}{x^{3} + x^{2} + x}$.
options:
- id: a
  content: |-
    $x =-1, x = 1$
- id: b
  correct: true
  content: |-
    The function has no vertical asymptotes
- id: c
  content: |-
    $x =-1, x = 0, x = 1$
- id: d
  content: |-
    $x =-\frac{1}{2}$ only
- id: e
  content: |-
    $x = 0$ only
```

---

**Question 11:**

```quiz
type: radio
id: q-11
content: |-
  Determine the vertical asymptotes of the function $f(x) = \frac{x^{2} - 1}{x^{3} - x^{2} + x - 1}$.
options:
- id: a
  content: |-
    $x = 1$ only
- id: b
  correct: true
  content: |-
    The function has no vertical asymptotes
- id: c
  content: |-
    $x =-1$ only
- id: d
  content: |-
    $x = 0$ only
- id: e
  content: |-
    $x =-1, x = 1$
```

```update-progress
```

[[MA/Mathematical-Foundations/MF2/Home|Home]]
[[MA/Mathematical-Foundations/MF2/0. Table of Contents/TOC|Table of Contents]]
