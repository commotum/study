# Limits at Infinity from Graphs

<!--
lesson-id: 1873
topic-code: MF2.11.1.4
-->

## Table of Contents

- [Introduction](#introduction)
- [The Limit at Infinity for a Bounded Function](#the-limit-at-infinity-for-a-bounded-function)
- [Infinite Limits](#infinite-limits)
- [The Limit at Infinity for an Unbounded Function](#the-limit-at-infinity-for-an-unbounded-function)

## Prerequisites

- [The Finite Limit of a Function](<../../../../MA/Mathematical-Foundations/MF2/11. Limits & Continuity/11.1. Estimating Limits from Graphs/Lessons/11.1.1. The Finite Limit of a Function.md>)
- [End Behavior of Functions](<../../../../MA/Mathematical-Foundations/MF1/8. Functions/8.1. Functions/Lessons/8.1.6. End Behavior of Functions.md>)

---

<a id="introduction"></a>
## Introduction

Until now, we have considered limits at individual points:

> $\lim\limits_{x \to a} f(x)$ is the value that $f(x)$ approaches as $x$ approaches the point $a$.

However, the idea of a limit extends beyond individual points. For instance, it might also be the case that $f(x)$ approaches some value as $x$ gets bigger and bigger, growing without bound.

To illustrate, consider the function

$$
f(x)=\dfrac{1}{x} + 1
$$

whose graph is shown below.

![](<../Source/Limits at Infinity from Graphs - 1873/Images/b75a6c31450c66be56a6b52cb5ebd2aa.png>)

On the right side of the graph, we see that as $x$ gets bigger and bigger, $f(x)$ approaches the horizontal asymptote $y=1$. In other words, as $x$ increases to infinity ($\infty$), the value of $f(x)$ approaches a limit of $1$. We can write this symbolically as

$$
\lim_\limits{x\to \infty} f(x) = 1
$$

Likewise, on the left side of the graph, as $x$ decreases to negative infinity ($-\infty$), the value of $f(x)$ approaches the same horizontal asymptote $y=1$. Consequently, we also have that

$$
\lim_\limits{x\to -\infty} f(x) = 1
$$

---

<a id="the-limit-at-infinity-for-a-bounded-function"></a>
## The Limit at Infinity for a Bounded Function

**Example:** The figure below shows the graph of $f(x)$. Find the limit $\lim_\limits{x \rightarrow \infty} f(x)$.

![](<../Source/Limits at Infinity from Graphs - 1873/Images/c659f3cdd50fa6ce5f0169025175ce30.png>)

**Explanation**

From the graph, we see that as $x$ increases to $\infty$, the graph of the function moves closer to the horizontal asymptote $y=4$.

Therefore, as $x$ approaches $\infty$, the function $f(x)$ approaches $4$, and we have

$$
\lim_\limits{x\rightarrow \infty} f(x) = 4
$$

---

**Question 1**

```quiz
type: radio
id: ma-35817
content: |-
  ![](<../Source/Limits at Infinity from Graphs - 1873/Images/q-35817.png>)
  
  Which of the following statements are true concerning the function $y = f(x)$ whose graph is shown above?
  
  1. $lim_(x → ∞)f(x) =-3$
  2. $lim_(x → ∞)f(x) = 0$
  3. $lim_(x → - ∞)f(x) =-3$
options:
- id: a
  content: |-
    I and II
- id: b
  content: |-
    II only
  correct: true
- id: c
  content: |-
    I and III
- id: d
  content: |-
    III only
- id: e
  content: |-
    II and III
```

---

**Question 2**

```quiz
type: radio
id: ma-35042
content: |-
  ![](<../Source/Limits at Infinity from Graphs - 1873/Images/q-35042.png>)
  
  The figure above shows the graph of $f(x)$. Find $lim_(x → ∞)f(x)$.
options:
- id: a
  content: |-
    $DNE$
- id: b
  content: |-
    $∞$
- id: c
  content: |-
    $-5$
  correct: true
- id: d
  content: |-
    $5$
- id: e
  content: |-
    $0$
```

---

<a id="infinite-limits"></a>
## Infinite Limits

Not every function $f(x)$ levels off to approach an asymptote as $x$ approaches infinity.

Instead, a function $f(x)$ might get bigger and bigger, increasing without bound, as shown in the graph below.

![](<../Source/Limits at Infinity from Graphs - 1873/Images/becd77bf46b950b8beb0c6fa4c39844e.png>)

In this case, we say that the limit of the function is infinity:

$$
\lim_\limits{x \rightarrow \infty} f(x) = \infty
$$

---

<a id="the-limit-at-infinity-for-an-unbounded-function"></a>
## The Limit at Infinity for an Unbounded Function

**Example:** The figure below shows the graph of $f(x)$. Find $\lim_\limits{x \rightarrow \infty} f(x)$ and $\lim_\limits{x \rightarrow -\infty} f(x)$.

![](<../Source/Limits at Infinity from Graphs - 1873/Images/f290350a1a1eb74c4a8d9a837f8578e0.png>)

**Explanation**

On the left side of the graph, we see that as the values of $x$ decrease and approach $-\infty$, the graph of the function moves closer and closer to the horizontal asymptote $y=2$.

Consequently, $f(x)$ approaches the value $2$ as $x$ approaches $-\infty$, and we have

$$
\lim_\limits{x\rightarrow -\infty} f(x) = 2
$$

On the right side of the graph, as the values of $x$ increase and approach $\infty$, the graph of the function grows without bound to $\infty$ as well. Therefore,

$$
\lim_\limits{x\to \infty} f(x) = \infty
$$

---

**Question 3**

```quiz
type: radio
id: ma-47580
content: |-
  ![](<../Source/Limits at Infinity from Graphs - 1873/Images/q-47580.png>)
  
  Which of the following statements are true concerning the function $y = f(x)$ whose graph is shown above?
  
  1. $lim_(x → - ∞)f(x) = - ∞$
  2. $lim_(x → ∞)f(x) = ∞$
  3. $lim_(x → ∞)f(x) = - ∞$
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    II only
- id: c
  content: |-
    III only
  correct: true
- id: d
  content: |-
    II and III
- id: e
  content: |-
    I and III
```

---

**Question 4**

```quiz
type: radio
id: ma-35809
content: |-
  ![](<../Source/Limits at Infinity from Graphs - 1873/Images/q-35809.png>)
  
  The figure above shows the graph of $f(x)$. Find $lim_(x → ∞)f(x)$ and $lim_(x → - ∞)f(x)$.
options:
- id: a
  content: |-
    $lim_(x → ∞)f(x) = ∞$ and $lim_(x → - ∞)f(x) = - ∞$
- id: b
  content: |-
    $lim_(x → ∞)f(x) = 0$ and $lim_(x → - ∞)f(x) = DNE$
- id: c
  content: |-
    $lim_(x → ∞)f(x) = ∞$ and $lim_(x → - ∞)f(x) = 0$
  correct: true
- id: d
  content: |-
    $lim_(x → ∞)f(x) = 0$ and $lim_(x → - ∞)f(x) = 0$
- id: e
  content: |-
    $lim_(x → ∞)f(x) = ∞$ and $lim_(x → - ∞)f(x) = DNE$
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
