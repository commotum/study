# Evaluating Limits at Infinity by Comparing Relative Magnitudes of Functions

## Table of Contents

- [Introduction](#introduction)
- [Comparing an Exponential Function and a Polynomial Function](#comparing-an-exponential-function-and-a-polynomial-function)
- [Comparing a Polynomial Function and a Logarithmic Function](#comparing-a-polynomial-function-and-a-logarithmic-function)
- [Comparing an Exponential Function and a Logarithmic Function](#comparing-an-exponential-function-and-a-logarithmic-function)
- [Comparing the Relative Magnitude of a Trigonometric Function](#comparing-the-relative-magnitude-of-a-trigonometric-function)

## Prerequisites

- [Limits at Infinity of Polynomials](../1263/1263.md)
- [Limits of Logarithmic Functions](../1377/1377.md)
- [Limits of Exponential Functions](../1717/1717.md)
- [Limits of Trigonometric Functions](../1719/1719.md)

---

<a id="introduction"></a>
## Introduction

Suppose that we want to calculate the following limit:

$$
\lim_{x \to \infty}\dfrac{x}{e^x}
$$

Notice that as $x \to \infty$, both the numerator and denominator approach $\infty$. Consequently, attempting direct substitution gives

$$
\dfrac{\infty}{\infty}
$$

This is called an **indeterminate form** because we are unable to determine what it means.

However, there is a trick. The trick is to realize that the numerator approaches infinity slowly, whereas the denominator approaches infinity rapidly. So for large values of $x$, we have

$$
\dfrac{x}{e^x} = \dfrac{\text{a big number}}{\text{a really really big number}}
$$

To put this in perspective: if $x=20$, then

$$
\dfrac{x}{e^x} = \dfrac{20}{e^{20}} \approx \dfrac{20}{485165195} \approx 0.00000004
$$

So, we conclude that

$$
\lim_{x \to \infty}\dfrac{x}{e^x} = 0
$$

This result is consistent with the graph of

$$
y=\dfrac{x}{e^x}
$$

![](<../Source/Evaluating Limits at Infinity by Comparing Relative Magnitudes of Functions - 607/Images/f0ac2e52e31c9080ec195b9c9a836361.png>)

In general, for large values of $x$,

$$
e^{x} \gg x^n \gg \ln(x)
$$

where $\gg$ means **much greater than**, and $n$ is *any* positive integer. We can use this to solve a variety of problems involving limits at infinity.

---

<a id="comparing-an-exponential-function-and-a-polynomial-function"></a>
## Comparing an Exponential Function and a Polynomial Function

**Example:** Evaluate $\displaystyle \lim_{x \to \infty}\dfrac{x^{100}}{e^x}$.

**Explanation**

Both the numerator and denominator approach $\infty$ as $x\to\infty$. However, since $e^x \gg x^{100}$ for large values of $x$, the denominator is growing much faster than the numerator. Consequently, we conclude that

$$
\lim_{x \to \infty}\dfrac{x^{100}}{e^x} = 0
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-WHW1-607-q001
content: |-
  Evaluate $\lim_{x \to \infty}\frac{e^{x}}{x^{9}}$.

options:
- id: a
  content: |-
    $\infty$
  correct: true

- id: b
  content: |-
    $0$

- id: c
  content: |-
    $1$

- id: d
  content: |-
    $DNE$

- id: e
  content: |-
    $e$
```

---

**Question 2:**

```quiz
type: radio
id: MA253-WHW1-607-q002
content: |-
  Evaluate $\lim_{x \to \infty}\frac{e^{x}}{x}$.

options:
- id: a
  content: |-
    $0$

- id: b
  content: |-
    $DNE$

- id: c
  content: |-
    $e$

- id: d
  content: |-
    $1$

- id: e
  content: |-
    $\infty$
  correct: true
```

---

<a id="comparing-a-polynomial-function-and-a-logarithmic-function"></a>
## Comparing a Polynomial Function and a Logarithmic Function

**Example:** Evaluate $\displaystyle \lim_{x \to \infty}\dfrac{x}{\ln{x}}$.

**Explanation**

Both the numerator and denominator approach $\infty$ as $x\to\infty$. However, since $x \gg \ln{x}$ for large values of $x$, the numerator is growing much faster than the denominator. Consequently, we conclude that

$$
\lim_{x \to \infty}\dfrac{x}{\ln{x}} = \infty
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-WHW1-607-q003
content: |-
  Evaluate $\lim_{x \to \infty}\frac{x}{\ln(2x)}$.

options:
- id: a
  content: |-
    $\infty$
  correct: true

- id: b
  content: |-
    $1$

- id: c
  content: |-
    $0$

- id: d
  content: |-
    $\ln(2)$

- id: e
  content: |-
    $DNE$
```

---

**Question 4:**

```quiz
type: radio
id: MA253-WHW1-607-q004
content: |-
  Evaluate $\lim_{x \to \infty}\frac{\ln x}{x^{2}}$.

options:
- id: a
  content: |-
    $0$
  correct: true

- id: b
  content: |-
    $1$

- id: c
  content: |-
    $DNE$

- id: d
  content: |-
    $\infty$

- id: e
  content: |-
    $2$
```

---

<a id="comparing-an-exponential-function-and-a-logarithmic-function"></a>
## Comparing an Exponential Function and a Logarithmic Function

**Example:** Evaluate $\displaystyle \lim_{x \to \infty}\dfrac{e^{2x}}{\ln{x}}$.

**Explanation**

Both the numerator and denominator approach $\infty$ as $x\to\infty$. However, since $e^{2x} \gg \ln{x}$ for large values of $x$, the numerator is growing much faster than the denominator. Consequently, we conclude that

$$
\lim_{x \to \infty}\dfrac{e^{2x}}{\ln{x}} = \infty
$$

---

**Question 5:**

```quiz
type: radio
id: MA253-WHW1-607-q005
content: |-
  Evaluate $\lim_{x \to \infty}\frac{e^{x}}{\ln(2x)}$.

options:
- id: a
  content: |-
    $1$

- id: b
  content: |-
    $0$

- id: c
  content: |-
    $\frac{e}{2}$

- id: d
  content: |-
    $\frac{1}{2}$

- id: e
  content: |-
    $\infty$
  correct: true
```

---

**Question 6:**

```quiz
type: radio
id: MA253-WHW1-607-q006
content: |-
  Evaluate $\lim_{x \to \infty}\frac{\ln(3x)}{e^{x}}$.

options:
- id: a
  content: |-
    $\infty$

- id: b
  content: |-
    $0$
  correct: true

- id: c
  content: |-
    $DNE$

- id: d
  content: |-
    $\ln(2)$

- id: e
  content: |-
    $e$
```

---

<a id="comparing-the-relative-magnitude-of-a-trigonometric-function"></a>
## Comparing the Relative Magnitude of a Trigonometric Function

**Example:** Evaluate $\displaystyle \lim_{x \to \infty}\dfrac{\cos x}{x^2+1}$.

**Explanation**

The numerator here is a bounded, oscillating function with

$$
\mid \cos x \mid \leq 1
$$

However, the denominator $x^2+1$ grows without bound as $x\to\infty$. So the denominator is growing much faster than the numerator, and we conclude that

$$
\lim_{x \to \infty}\dfrac{\cos x}{x^2+1} = 0
$$

We can see this from the graph of

$$
y=\dfrac{\cos x}{x^2+1}
$$

shown below:

![](<../Source/Evaluating Limits at Infinity by Comparing Relative Magnitudes of Functions - 607/Images/2887328aab485652d020545444662790.png>)

---

**Question 7:**

```quiz
type: radio
id: MA253-WHW1-607-q007
content: |-
  Evaluate $\lim_{x \to \infty}\frac{\sin x - 3}{x^{3} + x^{2}}$.

options:
- id: a
  content: |-
    $DNE$

- id: b
  content: |-
    $-5$

- id: c
  content: |-
    $-3$

- id: d
  content: |-
    $\infty$

- id: e
  content: |-
    $0$
  correct: true
```

---

**Question 8:**

```quiz
type: radio
id: MA253-WHW1-607-q008
content: |-
  Evaluate $\lim_{x \to \infty}\frac{3\sin x}{2x + 1}$.

options:
- id: a
  content: |-
    $\infty$

- id: b
  content: |-
    $0$
  correct: true

- id: c
  content: |-
    $3$

- id: d
  content: |-
    $DNE$

- id: e
  content: |-
    $\frac{3}{2}$
```

---

## Navigation

- [Next: Limits Involving the Exponential Function](<Limits Involving the Exponential Function - 2610.md>)
- [Back to WHW-1](../WHW-1.md)
