# Limits of Logarithmic Functions

## Table of Contents

- [Introduction](#introduction)
- [Evaluating Using Direct Substitution](#evaluating-using-direct-substitution)
- [Infinite Limits and Limits at Infinity of Logarithmic Functions](#infinite-limits-and-limits-at-infinity-of-logarithmic-functions)
- [Evaluating Limits at Infinity of Logarithmic Functions](#evaluating-limits-at-infinity-of-logarithmic-functions)
- [Evaluating One-Sided Infinite Limits of Logarithmic Functions](#evaluating-one-sided-infinite-limits-of-logarithmic-functions)
- [Evaluating Infinite Limits of Logarithmic Functions](#evaluating-infinite-limits-of-logarithmic-functions)

## Prerequisites

- [The Product and Quotient Rules for Limits](../1246/1246.md)
- [Combining Graph Transformations of Logarithmic Functions](../1707/1707.md)
- [Infinite Limits from Graphs](../1814/1814.md)
- [Limits at Infinity from Graphs](../1873/1873.md)

---

<a id="introduction"></a>
## Introduction

Let's look at the graph of $y=\log_2{x}$ below.

![](<../Source/Limits of Logarithmic Functions - 1377/Images/066423173a38dd656fac50d96a262269.png>)

From the graph, we see that

$$
\lim_{x\to3}\log_2{x} = \log_2{3}\approx 1.58
$$

For logarithmic functions, the limit at a point is equal to the value of the function at that point, so for any base $b \gt 1$ we have

$$
\lim_{x\to c}\log_b{x} = \log_b{c}
$$

Remember that logarithms are only defined for positive inputs $x\gt 0$, so we must have $c>0$. Otherwise, the limit does not exist $\textrm{(DNE})$.

---

<a id="evaluating-using-direct-substitution"></a>
## Evaluating Using Direct Substitution

**Example:** Find $\lim_\limits{x \to 4}\log_2 (x+4)$.

**Explanation**

The function $\log_2 (x+4)$ is defined for $x>-4$, so the limit as $x \to 4$ exists.

To find this limit, we substitute $x=4$ into the expression:

$$
\begin{aligned}
lim_(x → 4)\log_{2} (x + 4) &= \log_{2} (4 + 4) \\
&= \log_{2} (8) \\
&= \log_{2} (2^{3}) \\
&= 3
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-1377-q001
content: |-
  What is $lim_(x → 7)\log (15x - 5)$?
options:
- id: a
  content: |-
    $\frac{1}{3}$
- id: b
  content: |-
    $7$
- id: c
  content: |-
    $DNE$
- id: d
  content: |-
    $2$
  correct: true
- id: e
  content: |-
    $1$
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-1377-q002
content: |-
  What is $lim_(x → 5)\log_{3} (5x + 2)$?
options:
- id: a
  content: |-
    $DNE$
- id: b
  content: |-
    $3$
  correct: true
- id: c
  content: |-
    $∞$
- id: d
  content: |-
    $5$
- id: e
  content: |-
    $- ∞$
```
---

<a id="infinite-limits-and-limits-at-infinity-of-logarithmic-functions"></a>
## Infinite Limits and Limits at Infinity of Logarithmic Functions

Let's take a look again at the function

$$
y=\log_2(x)
$$

![](<../Source/Limits of Logarithmic Functions - 1377/Images/63aca78cdf8a6e3c36e5f58b1749d9a4.png>)

As $x$ gets larger and larger, the curve increases without bound. So, we have

$$
\lim_{x\to\infty} \log_2{x}= \infty
$$

The curve is not defined for

$$
x\leq 0
$$

but as $x$ approaches zero from the right the curve *decreases* without bound. So

$$
\lim_{x\to0^+}\log_2{x} = -\infty
$$

Also, note that

$$
\lim_{x\to0^-}\log_2{x} = \textrm{DNE},\qquad\qquad \lim_{x\to0}\log_2{x} = \textrm{DNE}
$$

These properties are true for logarithms of any base $b\gt 1$.

---

<a id="evaluating-limits-at-infinity-of-logarithmic-functions"></a>
## Evaluating Limits at Infinity of Logarithmic Functions

**Example:** Find $\displaystyle{\lim_{x\to \infty} \log_2 \left(x-1\right)}$.

**Explanation**

Let's sketch the graph of

$$
y = \log_2 \left(x-1\right)
$$

![](<../Source/Limits of Logarithmic Functions - 1377/Images/8ee7297c22b0e03cd456399a9b19d715.png>)

From the graph, we see that the function increases without bound as $x$ increases. Therefore,

$$
\lim_{x\to \infty} \log_2 \left(x-1\right) = \infty
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-1377-q003
content: |-
  What is $lim_(x → ∞)\log_{2} (5 - x)$?
options:
- id: a
  content: |-
    $10$
- id: b
  content: |-
    $- ∞$
- id: c
  content: |-
    $DNE$
  correct: true
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $∞$
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-1377-q004
content: |-
  What is $lim_(x → ∞)\log (2x - 4)$?
options:
- id: a
  content: |-
    $DNE$
- id: b
  content: |-
    $∞$
  correct: true
- id: c
  content: |-
    $- ∞$
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $50$
```
---

<a id="evaluating-one-sided-infinite-limits-of-logarithmic-functions"></a>
## Evaluating One-Sided Infinite Limits of Logarithmic Functions

**Example:** Calculate $\lim_\limits{x \to (-2)^{-}} \ln (x+2)$ and $\lim_\limits{x \to (-2)^{+}} \ln (x+2)$.

**Explanation**

Let's sketch the graph of

$$
y = \ln(x+2)
$$

![](<../Source/Limits of Logarithmic Functions - 1377/Images/80d6bc19b64bd7cc0ce3de61fd9a4e3a.png>)

The function is not defined for

$$
x\leq -2
$$

Therefore,

$$
\lim_\limits{x \to (-2)^{-}} \ln (x+2) = \textrm{DNE}
$$

However, the function is defined for $x\gt -2$. Therefore,

$$
\lim_\limits{x \to (-2)^{+}} \ln (x+2) = -\infty
$$

---

**Question 5:**

```quiz
type: radio
id: MA253-UQ1-1377-q005
content: |-
  What is $lim_(x → 5^{-})\log (5 - x)$?
options:
- id: a
  content: |-
    $- ∞$
  correct: true
- id: b
  content: |-
    $2$
- id: c
  content: |-
    $∞$
- id: d
  content: |-
    $DNE$
- id: e
  content: |-
    $0$
```
---

**Question 6:**

```quiz
type: radio
id: MA253-UQ1-1377-q006
content: |-
  Calculate $lim_(x → (-3)^{+})\ln (x + 3)$.
options:
- id: a
  content: |-
    $- ∞$
  correct: true
- id: b
  content: |-
    $DNE$
- id: c
  content: |-
    $∞$
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $3$
```
---

<a id="evaluating-infinite-limits-of-logarithmic-functions"></a>
## Evaluating Infinite Limits of Logarithmic Functions

**Example:** Calculate $\lim_\limits{x \to 2} \ln (x-2)$.

**Explanation**

Let's sketch the graph of

$$
y = \ln(x-2)
$$

![](<../Source/Limits of Logarithmic Functions - 1377/Images/c31c4c5fd15fffd1e1b9661217eef36e.png>)

The function is not defined for

$$
x\leq 2
$$

Therefore,

$$
\lim_\limits{x \to 2^{-}} \ln (x-2) = \textrm{DNE}
$$

However, the function is defined for $x\gt 2$. Therefore,

$$
\lim_\limits{x \to 2^{+}} \ln (x-2) = -\infty
$$

Since the left and right-sided limits are not equal, we have

$$
\lim_\limits{x \to 2} \ln (x-2) = \textrm{DNE}
$$

---

**Question 7:**

```quiz
type: radio
id: MA253-UQ1-1377-q007
content: |-
  Calculate $lim_(x → (-4))\log_{2} (x + 4)$.
options:
- id: a
  content: |-
    $∞$
- id: b
  content: |-
    $DNE$
  correct: true
- id: c
  content: |-
    $- ∞$
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $1$
```
---

**Question 8:**

```quiz
type: radio
id: MA253-UQ1-1377-q008
content: |-
  Calculate $lim_(x → 1/2)\ln (2x - 1)$.
options:
- id: a
  content: |-
    $∞$
- id: b
  content: |-
    $DNE$
  correct: true
- id: c
  content: |-
    $\frac{1}{2}$
- id: d
  content: |-
    $- ∞$
- id: e
  content: |-
    $0$
```
---

## Navigation

- [Next: Limits of Exponential Functions](<Limits of Exponential Functions - 1717.md>)
- [Back to UQ-1](../UQ-1.md)
