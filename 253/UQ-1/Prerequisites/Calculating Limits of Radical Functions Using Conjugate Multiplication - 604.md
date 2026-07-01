# Calculating Limits of Radical Functions Using Conjugate Multiplication

## Table of Contents

- [Introduction](#introduction)
- [Calculating the Limit of a Rational Function with a Radical in the Numerator](#calculating-the-limit-of-a-rational-function-with-a-radical-in-the-numerator)
- [Calculating the Limit of a Rational Function with a Radical in the Denominator](#calculating-the-limit-of-a-rational-function-with-a-radical-in-the-denominator)

## Prerequisites

- [The Power and Root Rules for Limits](../37/37.md)
- [Calculating Limits of Rational Functions by Factoring](../1813/1813.md)
- [Adding and Subtracting Radical Expressions](../3756/3756.md)
- [Further Rationalizing Denominators of Algebraic Expressions](../6185/6185.md)

---

<a id="introduction"></a>
## Introduction

Suppose that we want to calculate the following limit:

$$
\lim_{x \to 1} \frac{\sqrt{x} - 1}{x - 1}
$$

If we try to evaluate the limit by directly substituting $x=1$, we get an indeterminate form:

$$
\begin{aligned}
lim_(x → 1)\frac{\sqrt{x} - 1}{x - 1} &= \frac{\sqrt{1} - 1}{1 - 1} = \frac{0}{0}
\end{aligned}
$$

However, if we simplify the fraction before evaluating the limit, we obtain a more clear result. To simplify the fraction, we can multiply the numerator and the denominator of the function by the **conjugate** of the numerator.

To obtain the conjugate of $\sqrt{x}-1$, we simply switch the sign between the two terms to get $\sqrt{x}+ 1$.

$$
\begin{aligned} \require{cancel} \lim_{x\to 1} \frac{\sqrt{x} - 1} {x - 1} &= \lim_{x\to 1} \frac{\sqrt{x} - 1} {x - 1} \cdot\dfrac{\sqrt{x} + 1}{\sqrt{x} + 1} \\ &=\lim_{x\to 1} \dfrac{(\sqrt{x} - 1)(\sqrt{x} +1)} {(x-1)(\sqrt{x} + 1)} \\ &=\lim_{x\to 1} \dfrac{\left(\sqrt{x}\right)^2 - 1^2} {(x-1)(\sqrt{x} + 1)} \\ &=\lim_{x\to 1} \dfrac{x-1} {(x-1)(\sqrt{x} + 1)} \\ &=\lim_{x\to 1} \dfrac{\cancel{x-1}} {\cancel{(x-1)}(\sqrt{x} + 1)} \\ &=\lim_{x\to 1} \dfrac1{\sqrt{x} + 1} \\ &=\dfrac{1}{\sqrt{1} +1} \\ &=\dfrac{1}{2} \end{aligned}
$$

---

<a id="calculating-the-limit-of-a-rational-function-with-a-radical-in-the-numerator"></a>
## Calculating the Limit of a Rational Function with a Radical in the Numerator

**Example:** Evaluate $\displaystyle{\lim_{x \to 4^+} \dfrac {x - 2\sqrt{x}} {x - 4}}$.

**Explanation**

If we attempt to evaluate the limit, we get an indeterminate form:

$$
\begin{aligned}
lim_(x → 4^{+})\frac{x - 2\sqrt{x}}{x - 4} &= \frac{4 - 2\sqrt{4}}{4 - 4} = \frac{0}{0}
\end{aligned}
$$

So, we need to first simplify the limit. Since the radical is in the numerator, we can multiply the numerator and the denominator by the conjugate of the numerator. We get

$$
\begin{aligned} \lim_{x \to 4^+} \dfrac {x - 2\sqrt{x}} {x - 4} &= \lim_{x \to 4^+} \dfrac {(x -2 \sqrt{x})(x+2\sqrt x)} {(x - 4)(x+2\sqrt x)} \\ &= \lim_{x \to 4^+} \dfrac {x^2-\left(2\sqrt{x}\right)^2} {(x - 4)(x+2\sqrt x)} \\ &= \lim_{x \to 4^+} \dfrac {x^2-4x} {(x - 4)(x+2\sqrt x)} \\ &= \lim_{x \to 4^+} \dfrac {x(x-4)} {(x - 4)(x+2\sqrt x)} \\ &= \lim_{x \to 4^+} \dfrac {x} {x+2\sqrt x} \\ &= \lim_{x \to 4^+} \dfrac {4} {4+2\sqrt4} \\ &=\dfrac 1 2. \end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-604-q001
content: |-
  Evaluate $lim_(x → 0)\frac{\sqrt{x + 4} - 2}{x}$.
options:
- id: a
  content: |-
    $0$
- id: b
  content: |-
    $\frac{1}{4}$
  correct: true
- id: c
  content: |-
    $∞$
- id: d
  content: |-
    $\frac{1}{2}$
- id: e
  content: |-
    $DNE$
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-604-q002
content: |-
  Evaluate $lim_(x → 4)\frac{\sqrt{x} - 2}{x - 4}$.
options:
- id: a
  content: |-
    $\frac{1}{4}$
  correct: true
- id: b
  content: |-
    $\frac{1}{2}$
- id: c
  content: |-
    $0$
- id: d
  content: |-
    $∞$
- id: e
  content: |-
    $DNE$
```
---

<a id="calculating-the-limit-of-a-rational-function-with-a-radical-in-the-denominator"></a>
## Calculating the Limit of a Rational Function with a Radical in the Denominator

**Example:** Calculate $\displaystyle{\lim_{x \to 0} \dfrac {3x} {\sqrt{x +1} -1}}$.

**Explanation**

If we attempt to evaluate the limit by simply evaluating the function at $x=0$, we get an indeterminate form:

$$
\begin{aligned}
lim_(x → 0)\frac{3x}{\sqrt{x + 1} - 1} &= \frac{3 \cdot 0}{\sqrt{0 + 1} - 1} = \frac{0}{0}
\end{aligned}
$$

So, we need to first simplify the limit. Since the radical is in the denominator, we can multiply the numerator and the denominator by the conjugate of the denominator. We get

$$
\begin{aligned} \lim_{x \to 0} \dfrac {3x} {\sqrt{x + 1} - 1} &=\lim_{x\to 0}\frac{(3x)(\sqrt{x+1}+1)}{(\sqrt{x + 1} - 1)(\sqrt{x+1}+1)} \\ &=\lim_{x\to 0}\frac{3x(\sqrt{x+1}+1)}{\left(\sqrt{x+1}\right)^2-1^2} \\ &=\lim_{x\to 0}\frac{3x(\sqrt{x+1}+1)}{x+1-1} \\ &=\lim_{x\to 0}\frac{3x(\sqrt{x+1}+1)}{x} \\ &=\lim_{x\to 0}3(\sqrt{x+1}+1) \\ &=3(\sqrt{0+1}+1) \\ &=6. \end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-604-q003
content: |-
  Evaluate $lim_(x → 1^{-})\frac{x - 1}{\sqrt{x + 3} - 2}$.
options:
- id: a
  content: |-
    $DNE$
- id: b
  content: |-
    $\frac{1}{4}$
- id: c
  content: |-
    $4$
  correct: true
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $\frac{1}{2}$
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-604-q004
content: |-
  Evaluate $lim_(x → 1^{+})\frac{1 - x^{2}}{1 - \sqrt{x}}$.
options:
- id: a
  content: |-
    $\frac{1}{4}$
- id: b
  content: |-
    $0$
- id: c
  content: |-
    $4$
  correct: true
- id: d
  content: |-
    $\frac{1}{2}$
- id: e
  content: |-
    $DNE$
```
---

## Navigation

- [Next: The Finite Limit of a Function](<The Finite Limit of a Function - 461.md>)
- [Back to UQ-1](../UQ-1.md)
