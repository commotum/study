# Limits of Exponential Functions

## Table of Contents

- [Introduction](#introduction)
- [Evaluating Using Direct Substitution](#evaluating-using-direct-substitution)
- [Infinite Limits of Exponential Functions](#infinite-limits-of-exponential-functions)
- [Evaluating Infinite Limits of Exponential Functions](#evaluating-infinite-limits-of-exponential-functions)
- [Evaluating Infinite Limits Using the Laws of Exponents and the Algebra of Limits](#evaluating-infinite-limits-using-the-laws-of-exponents-and-the-algebra-of-limits)

## Prerequisites

- [The Product and Quotient Rules for Limits](../1246/1246.md)
- [Limits at Infinity from Graphs](../1873/1873.md)
- [Combining Graph Transformations of Exponential Functions](../6351/6351.md)

---

<a id="introduction"></a>
## Introduction

Consider the graph of $y=e^x$ below. We will use this graph to compute $\lim\limits_{x \to \, 1} e^x \,$.

![](<../Source/Limits of Exponential Functions - 1717/Images/10cb3b62b88394cd36f707559e61b7d5.png>)

From the graph, we see that as $x$ approaches $1$, the value of $y$ approaches $e^1$. So

$$
\lim_{x\to 1} e^x = e^1 = e
$$

The limit of the function at a point is equal to the value of the function at that point, and this is true for *any* point, not just $x=1$. If $c$ is any real number, we have

$$
\lim_{x\to c} e^x = e^c
$$

In fact, *all* exponential functions have this property. For $a \gt 0$ and any real number $c$, we have

$$
\lim_{x\to c} a^x = a^c
$$

---

<a id="evaluating-using-direct-substitution"></a>
## Evaluating Using Direct Substitution

**Example:** Find $\lim_\limits{x \to 1} (3^{2x} + 2^{3x} + 1)$.

**Explanation**

We can evaluate this limit using direct substitution, as follows:

$$
\begin{aligned}
lim_(x → 1)(3^{2x} + 2^{3x} + 1) &= 3^{2(1)} + 2^{3(1)} + 1 \\
&= 9 + 8 + 1 \\
&= 18
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-1717-q001
content: |-
  Find $lim_(x → 3)10^{3x - 7}$.
options:
- id: a
  content: |-
    $\frac{1}{10}$
- id: b
  content: |-
    $\frac{1}{100}$
- id: c
  content: |-
    $10000$
- id: d
  content: |-
    $100$
  correct: true
- id: e
  content: |-
    $10$
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-1717-q002
content: |-
  Find $lim_(x → 0)\frac{4^{x} - 5}{2^{x} - 2}$.
options:
- id: a
  content: |-
    $4$
  correct: true
- id: b
  content: |-
    $∞$
- id: c
  content: |-
    DNE
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $\frac{1}{2}$
```
---

<a id="infinite-limits-of-exponential-functions"></a>
## Infinite Limits of Exponential Functions

Consider the graphs of $y = 2^x$ and $y = 2^{-x}$ shown below. We will use these graphs to compute the limits at infinity.

![](<../Source/Limits of Exponential Functions - 1717/Images/b74353297f24c384ed5e0930e8238b73.png>)

Considering $y = 2^x$ first, we note that as $x \to \infty$, the function increases without bound, and as $x \to -\infty$, the function approaches zero. So

$$
\lim_{x\to \infty} 2^x = \infty\qquad \textrm{and}\qquad \lim_{x\to -\infty} 2^x =0
$$

The same properties hold true for any exponential function $y=a^x$ where $a \gt 1$.

Now consider the curve $y=2^{-x}$. We have

$$
\lim_{x\to \infty} 2^{-x} = 0\qquad \textrm{and}\qquad \lim_{x\to -\infty} 2^{-x} =\infty
$$

Again, the same properties are true for any exponential function $y=a^{-x}$ for $a \gt 1$.

---

<a id="evaluating-infinite-limits-of-exponential-functions"></a>
## Evaluating Infinite Limits of Exponential Functions

**Example:** Evaluate $\displaystyle\lim_{x\to-\infty} -3\left(\dfrac 1 2\right)^x$.

**Explanation**

First, we rewrite the limit using the algebra of limits, as follows:

$$
lim_(x → - ∞) - 3(\frac{1}{2})^{x} =-3 \cdot lim_(x → - ∞)(\frac{1}{2})^{x}
$$

Next, we recall the graph of

$$
y = \left(\dfrac 1 2\right)^x
$$

![](<../Source/Limits of Exponential Functions - 1717/Images/5846ea3956bb36f7b5955be3d8294c64.png>)

From the graph, we see that the function increases without bound as $x$ decreases. Therefore,

$$
\lim_{x\to-\infty} \left(\dfrac 1 2\right)^x = \infty
$$

However, the negative factor $-3$ changes the sign of the limit. Therefore, we conclude that

$$
-3\cdot \lim_{x\to-\infty} \left(\dfrac 1 2\right)^x = -\infty
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-1717-q003
content: |-
  What is $lim_(x → - ∞)(-7 \cdot 6^{x})$?
options:
- id: a
  content: |-
    $0$
  correct: true
- id: b
  content: |-
    $∞$
- id: c
  content: |-
    $7$
- id: d
  content: |-
    $- ∞$
- id: e
  content: |-
    $6$
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-1717-q004
content: |-
  What is $lim_(x → ∞)8^{-x}$?
options:
- id: a
  content: |-
    $0$
  correct: true
- id: b
  content: |-
    $8$
- id: c
  content: |-
    $- ∞$
- id: d
  content: |-
    $∞$
- id: e
  content: |-
    $DNE$
```
---

<a id="evaluating-infinite-limits-using-the-laws-of-exponents-and-the-algebra-of-limits"></a>
## Evaluating Infinite Limits Using the Laws of Exponents and the Algebra of Limits

**Example:** Compute $\lim_\limits{x \to \infty} -5 \left(\dfrac{1}{3}\right)^{1+x}$.

**Explanation**

We can use the laws of exponents and the algebra of limits to rewrite the given limit as follows:

$$
\begin{aligned}
lim_(x → ∞) - 5(\frac{1}{3})^{1 + x} &= -5lim_(x → ∞)(\frac{1}{3})^{1 + x} \\
&=-5lim_(x → ∞)(\frac{1}{3})^{1} \cdot (\frac{1}{3})^{x} \\
&=-5lim_(x → ∞)\frac{1}{3} \cdot (\frac{1}{3})^{x} \\
&=-\frac{5}{3} \cdot lim_(x → ∞)(\frac{1}{3})^{x}
\end{aligned}
$$

Next, we recall the graph of

$$
y = \left(\dfrac 1 3\right)^x
$$

![](<../Source/Limits of Exponential Functions - 1717/Images/5a86ab6087c88635878b30b98ffed525.png>)

From the graph, we see that the function decreases to zero as $x$ increases. So

$$
\lim_\limits{x \to \infty} \left(\dfrac{1}{3}\right)^{x} = 0
$$

and finally, we have

$$
-\dfrac{5}{3}\cdot \lim_\limits{x \to \infty} \left(\dfrac{1}{3}\right)^{x} = -\dfrac 5 3\cdot 0 = 0
$$

---

**Question 5:**

```quiz
type: radio
id: MA253-UQ1-1717-q005
content: |-
  What is $lim_(x → ∞)2^{2x + 4}$?
options:
- id: a
  content: |-
    $∞$
  correct: true
- id: b
  content: |-
    $- ∞$
- id: c
  content: |-
    $DNE$
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $0$
```
---

**Question 6:**

```quiz
type: radio
id: MA253-UQ1-1717-q006
content: |-
  What is $lim_(x → ∞)e^{(-3x + 1)}$?
options:
- id: a
  content: |-
    $0$
  correct: true
- id: b
  content: |-
    $- ∞$
- id: c
  content: |-
    $e$
- id: d
  content: |-
    $DNE$
- id: e
  content: |-
    $∞$
```
---

## Navigation

- [Next: Improper Integrals Involving Exponential Functions](<Improper Integrals Involving Exponential Functions - 4004.md>)
- [Back to UQ-1](../UQ-1.md)
