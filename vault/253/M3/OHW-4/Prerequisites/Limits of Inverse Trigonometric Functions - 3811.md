# Limits of Inverse Trigonometric Functions

<!--
lesson-id: 3811
topic-code: MF3.5.1.5
-->

## Table of Contents

- [Introduction](#introduction)
- [Limits of Inverse Cosine](#limits-of-inverse-cosine)
- [Limits of Inverse Tangent](#limits-of-inverse-tangent)
- [Finding the Limit of an Inverse Trigonometric Function at a Point](#finding-the-limit-of-an-inverse-trigonometric-function-at-a-point)
- [Limits of Inverse Trigonometric Function at Infinity](#limits-of-inverse-trigonometric-function-at-infinity)
- [Finding Limits at Infinity](#finding-limits-at-infinity)
- [Finding a Limit Involving Trigonometric Functions and Their Inverses](#finding-a-limit-involving-trigonometric-functions-and-their-inverses)

## Prerequisites

- [The Power and Root Rules for Limits](<../../../../MA/Mathematical-Foundations/MF2/11. Limits & Continuity/11.2. The Algebra of Limits/Lessons/11.2.4. The Power and Root Rules for Limits.md>)
- [Evaluating Expressions Containing Inverse Trigonometric Functions](<../../../../MA/Mathematical-Foundations/MF3/5. Trigonometry/5.1. The Inverse Trigonometric Functions/Lessons/5.1.4. Evaluating Expressions Containing Inverse Trigonometric Functions.md>)
- [Combining Graph Transformations: Two Operations](<../../../../MA/Mathematical-Foundations/MF2/4. Functions/4.2. Graph Transformations of Functions/Lessons/4.2.7. Combining Graph Transformations- Two Operations.md>)
- [Limits at Infinity from Graphs](<../../../../MA/Mathematical-Foundations/MF2/11. Limits & Continuity/11.1. Estimating Limits from Graphs/Lessons/11.1.4. Limits at Infinity from Graphs.md>)

---

<a id="introduction"></a>
## Introduction

In this lesson, we will learn how to deal with limits involving inverse trigonometric functions.

Let's begin by recalling the graph of

$$
y=\arcsin(x)
$$

![](<../Source/Limits of Inverse Trigonometric Functions - 3811/Images/cd9d90e20c36242847de8f71b7773396.png>)

Using the graph, we note the following:

- The domain of $\arcsin(x)$ is $x \in [-1,1]$.
- For every value $a \in (-1,1)$, we have
$\lim_\limits{x\to a} \arcsin(x) = \arcsin(a)$.
In other words, we can evaluate the limit using direct substitution. For example,
$lim_(x → 1/2)\arcsin (x)|= \arcsin (\frac{1}{2}); = \frac{π}{6}$.
- For any value $a$ that does *not* lie in the domain of $\arcsin(x)$, the limit
$\lim_\limits{x\to a} \arcsin(x)$
does *not* exist.
- At the point $x=-1$, the limit does *not* exist because the left-sided limit does not exist. However, the right-sided limit *does* exist and is given by
$lim_(x → (-1)^{+})\arcsin (x)|= \arcsin (-1); =-\frac{π}{2}$.
- Similarly, at the point $x=1$, the limit does *not* exist because the right-sided limit does not exist. However, the left-sided limit *does* exist and is given by
$lim_(x → 1^{-})\arcsin (x)|= \arcsin (1); = \frac{π}{2}$.

The limit properties of

$$
y=\arccos(x)
$$

are similar. Let's discuss them briefly.

---

<a id="limits-of-inverse-cosine"></a>
## Limits of Inverse Cosine

Let's recall the graph of

$$
y=\arccos(x)
$$

![](<../Source/Limits of Inverse Trigonometric Functions - 3811/Images/ef38fb874778ad596ecba64af02f5454.png>)

From the graph, we note the following:

- The domain is $x \in [-1,1]$.
- For every value $a \in (-1,1)$, we have
$\lim_\limits{x\to a} \arccos(x) = \arccos(a)$.
- For any value $a$ that does *not* lie in the domain of $\arccos(x)$, the limit
$\lim_\limits{x\to a} \arccos(x)$
does *not* exist.
- The right-sided limit at $x=-1$ is given by
$lim_(x → (-1)^{+})\arccos (x)|= \arccos (-1); = π$.
- Similarly, the left-sided limit at $x=1$ is given by
$lim_(x → 1^{-})\arccos (x)|= \arccos (1); = 0$.

Finally, let's deduce the limit properties of

$$
y = \arctan x
$$

---

<a id="limits-of-inverse-tangent"></a>
## Limits of Inverse Tangent

The graph of $y=\arctan x$ is shown below.

![](<../Source/Limits of Inverse Trigonometric Functions - 3811/Images/4ce92b75793626c1f8c51561207d581c.png>)

From the graph, we note the following:

- The domain is $x \in (-\infty, \infty)$.
- For every value $a$, we have
$\lim_\limits{x\to a} \arctan(x) = \arctan(a)$.
- The limit as $x\to-\infty$ is given by
$lim_(x → - ∞)\arctan (x)|=-\frac{π}{2}$.
- The limit as $x\to\infty$ is given by
$lim_(x → ∞)\arctan (x)|= \frac{π}{2}$.

We can use the algebra of limits to evaluate expressions involving inverse trigonometric functions. Let's see some examples.

---

<a id="finding-the-limit-of-an-inverse-trigonometric-function-at-a-point"></a>
## Finding the Limit of an Inverse Trigonometric Function at a Point

**Example:** Evaluate $\lim_\limits{x \to 0} \dfrac{\arccos(x) -\pi}{x-\pi}$.

**Explanation**

Let's sketch the graph of

$$
y=\arccos(x){:}
$$

![](<../Source/Limits of Inverse Trigonometric Functions - 3811/Images/a466fdfbf193e117a9c5e416ee47ffff.png>)

The domain of $\arccos(x)$ is $x \in [-1,1]$.

Now, substituting $x=0$ directly into the limit, we have

$$
\begin{aligned}
lim_(x → 0)((\arccos (x) - π)/(x - π)) &= (\arccos (0) - π)/(0 - π) \\
&= ((\frac{π}{2} - π))/((- π)) \\
&= ((-\frac{π}{2}))/((- π)) \\
&= \frac{1}{2}
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-149953
content: |-
  Evaluate $lim_(x → - 1)(8x\arctan (x))$.
options:
- id: a
  content: |-
    $2π$
  correct: true
- id: b
  content: |-
    $\frac{π}{2}$
- id: c
  content: |-
    $-\frac{π}{2}$
- id: d
  content: |-
    $- π$
- id: e
  content: |-
    Undefined
```

---

**Question 2:**

```quiz
type: radio
id: ma-149954
content: |-
  What is the value of $lim_(x → 2)((2\arcsin (x) - π)^{2})/(2x)$?
options:
- id: a
  content: |-
    Undefined
  correct: true
- id: b
  content: |-
    $π$
- id: c
  content: |-
    $\frac{π}{2}$
- id: d
  content: |-
    $-1$
- id: e
  content: |-
    $\frac{2}{π}$
```

---

<a id="limits-of-inverse-trigonometric-function-at-infinity"></a>
## Limits of Inverse Trigonometric Function at Infinity

We can deduce limits at infinity of transformed inverse trigonometric functions by sketching their graphs.

For example, let's consider the following limit:

$$
\lim_\limits{x \to \, \infty} \dfrac{2}{\pi}\arctan \left(x-\pi\right)
$$

To evaluate this limit, we first sketch the graph of

$$
y =\arctan \left(x-\pi\right){:}
$$

![](<../Source/Limits of Inverse Trigonometric Functions - 3811/Images/5e9f5ea27282820d36ebf191ef5f08d0.png>)

The domain of

$$
\arctan \left(x-\pi\right)
$$

is $(-\infty,\infty)$. Moreover, from the graph, we see that

$$
\lim\limits_{x\to \infty} \arctan \left(x-\pi\right)=\color{blue}{\dfrac{\pi}{2}}
$$

Therefore, by the algebra of limits, we have

$$
\begin{aligned}
lim_(x → ∞)\frac{2}{π}\arctan (x - π) &= \frac{2}{π} \cdot lim_(x → ∞)\arctan (x - π) \\
&= \frac{2}{π} \cdot (\frac{π}{2}) \\
&= 1
\end{aligned}
$$

Limits at infinity involving the inverse sine and cosine functions usually do not exist. Let's see an example.

---

<a id="finding-limits-at-infinity"></a>
## Finding Limits at Infinity

**Example:** What is the value of $\lim_\limits{x \to \, \infty} \arccos(x-1)$?

**Explanation**

First, let's sketch the graph of

$$
y = \arccos(x-1){:}
$$

![](<../Source/Limits of Inverse Trigonometric Functions - 3811/Images/0c8e05c838e67b1eaca00925fab12e20.png>)

The domain of $\arccos(x-1)$ is $x \in [0,2]$. This means that $\arccos(x-1)$ is undefined outside this interval.

Therefore, $\lim_\limits{x \to \, \infty} \arccos(x-1)$ is undefined.

---

**Question 3:**

```quiz
type: radio
id: ma-149956
content: |-
  What is $lim_(x → ∞)4\arctan (1 - x)$?
options:
- id: a
  content: |-
    $2π$
- id: b
  content: |-
    $-\frac{π}{2}$
- id: c
  content: |-
    Undefined
- id: d
  content: |-
    $-2π$
  correct: true
- id: e
  content: |-
    $- ∞$
```

---

**Question 4:**

```quiz
type: radio
id: ma-149955
content: |-
  What is the value of $lim_(x → - ∞)\arcsin (2x - 1)$?
options:
- id: a
  content: |-
    Undefined
  correct: true
- id: b
  content: |-
    $-1$
- id: c
  content: |-
    $- ∞$
- id: d
  content: |-
    $∞$
- id: e
  content: |-
    $1$
```

---

<a id="finding-a-limit-involving-trigonometric-functions-and-their-inverses"></a>
## Finding a Limit Involving Trigonometric Functions and Their Inverses

**Example:** Compute the value of $\lim_\limits{x \to \, \infty}\cos\left(\dfrac{2}{3}\arctan \left(2x+1\right)\right)$.

**Explanation**

First, let's sketch the graph of

$$
y =\arctan \left(2x+1\right){:}
$$

![](<../Source/Limits of Inverse Trigonometric Functions - 3811/Images/3e8fb5c89782322156fbf09f33393408.png>)

The domain of

$$
\arctan \left(2x+1 \right)
$$

is $(-\infty,\infty)$.

As $x$ increases to $\infty$, the graph tends to

$$
y={\color{blue}\dfrac{\pi}{2}}
$$

Therefore,

$$
\begin{aligned}
lim_(x → ∞)\cos (\frac{2}{3}\arctan (2x + 1)) &= \cos (\frac{2}{3} \cdot (\frac{π}{2})) \\
&= \cos (\frac{π}{3}) \\
&= \frac{1}{2}
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: ma-149958
content: |-
  What is $lim_(x → - 1/2)\tan (\frac{1}{2}\arccos (x))$?
options:
- id: a
  content: |-
    $\frac{\sqrt{3}}{3}$
- id: b
  content: |-
    $-1$
- id: c
  content: |-
    $∞$
- id: d
  content: |-
    $\sqrt{3}$
  correct: true
- id: e
  content: |-
    $DNE$
```

---

**Question 6:**

```quiz
type: radio
id: ma-149957
content: |-
  What is $lim_(x → - ∞)\sin (2\arctan (x))$?
options:
- id: a
  content: |-
    $DNE$
- id: b
  content: |-
    $\frac{π}{2}$
- id: c
  content: |-
    $- ∞$
- id: d
  content: |-
    $0$
  correct: true
- id: e
  content: |-
    $2π$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
