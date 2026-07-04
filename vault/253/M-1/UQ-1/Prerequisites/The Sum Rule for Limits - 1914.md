# The Sum Rule for Limits


<!--
lesson-id: 1914
topic-code: MF2.11.2.2
-->
## Table of Contents

- [Introduction](#introduction)
- [Applying the Sum Rule to Compute a Limit](#applying-the-sum-rule-to-compute-a-limit)
- [Applying the Sum Rule to Compute A Limit Given a Graph](#applying-the-sum-rule-to-compute-a-limit-given-a-graph)

## Prerequisites

- [Limits of Power Functions, and the Constant Rule for Limits](../1716/1716.md)

---

<a id="introduction"></a>
## Introduction

The **sum rule** states that the limit of the sum of two functions equals the sum of the limits (provided that those limits exist).

More precisely, if

$$
\lim_{x\rightarrow a}f(x)=L
$$

and

$$
\lim_{x\rightarrow a}g(x)=K
$$

, then

$$
\begin{aligned}
\lim_{x \to a}(f(x) + g(x)) &= \lim_{x \to a}f(x) + \lim_{x \to a}g(x) \\
&= L + K
\end{aligned}
$$

For example, to compute

$$
\lim_{x \rightarrow \,-3} \left(5x^2+2x\right)
$$

we can first apply the sum rule, followed by the constant rule, and compute the limits of the power functions.

$$
\begin{aligned}
\lim_{x \to - 3}(5x^{2} + 2x) &= \lim_{x \to - 3}5x^{2} + \lim_{x \to - 3}2x \\
&= 5 \cdot \lim_{x \to - 3}x^{2} + 2 \cdot \lim_{x \to - 3}x \\
&= 5 \cdot (-3)^{2} + 2 \cdot (-3) \\
&= 45 - 6 \\
&= 39
\end{aligned}
$$

There is a shortcut: in general, to find the limit of a polynomial $f(x)$ at some point $x=c$, all we need to do is evaluate the polynomial at $c$.

$$
\lim_{x\to c} f(x) = f(c)
$$

**Warning!** If one of $\lim_{x\rightarrow a}f(x)$ or $\lim_{x\rightarrow a}g(x)$ exists while the other does not exist, then $\lim_{x\rightarrow a}\Bigl(f(x)+g(x) \Bigr)$ does not exist either.

---

<a id="applying-the-sum-rule-to-compute-a-limit"></a>
## Applying the Sum Rule to Compute a Limit

**Example:** Evaluate $\lim_{x \rightarrow \,1} \left(6x^2+x\right)$.

**Explanation**

We first apply the sum rule, and then apply the constant rule and compute the limits of the power functions.

$$
\begin{aligned}
\lim_{x \to 1}(6x^{2} + x) &= \lim_{x \to 1}6x^{2} + \lim_{x \to 1}x \\
&= 6 \cdot \lim_{x \to 1}x^{2} + \lim_{x \to 1}x \\
&= 6 \cdot 1^{2} + 1 \\
&= 6 + 1 \\
&= 7
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-1914-q001
content: |-
  Evaluate $\lim_{x \to 1}(3x^{5} - 2x^{2} - x)$.
options:
- id: a
  content: |-
    $4$
- id: b
  content: |-
    $1$
- id: c
  content: |-
    $6$
- id: d
  content: |-
    $-2$
- id: e
  content: |-
    $0$
  correct: true
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-1914-q002
content: |-
  Evaluate $\lim_{x \to 10}(\frac{x}{2} + 1)$.
options:
- id: a
  content: |-
    $1$
- id: b
  content: |-
    $10$
- id: c
  content: |-
    Does not exist
- id: d
  content: |-
    $5$
- id: e
  content: |-
    $6$
  correct: true
```
---

<a id="applying-the-sum-rule-to-compute-a-limit-given-a-graph"></a>
## Applying the Sum Rule to Compute A Limit Given a Graph

**Example:** The figure below shows the graphs of $y=f(x)$ and $y=g(x)$. Evaluate $\lim_{x \rightarrow \,-2} \Bigl(3f(x) - g(x)\Bigr)$.

![](<253/M-1/UQ-1/Source/The Sum Rule for Limits - 1914/Images/d3f30fae20e574c32a29eb3aa3c0cbae.png>)

**Explanation**

According to the sum and constant multiple rules, we can compute the required limit as follows:

$$
\lim_{x \rightarrow \,-2} \Bigl(3f(x) - g(x)\Bigr) = 3 \lim_{x \rightarrow \,-2} f(x) - \lim_{x \rightarrow \,-2} g(x)
$$

The above assumes that $\lim_{x \rightarrow \,-2} f(x)$ and $\lim_{x \rightarrow \,-2} g(x)$ both exist.

In the graph, we see that

$$
\lim_{x \rightarrow \,-2} f(x) =-1
$$

However,

$$
\lim_{x \rightarrow \,-2} g(x) = \text{DNE}
$$

because the left and right limits are not equal:

$$
\lim_{x\rightarrow {-2}^{-}}g(x)=3, \qquad \lim_{x\rightarrow -2^{+}}g(x)=2 \,
$$

Because $\lim_{x \rightarrow \,-2} f(x)$ exists while $\lim_{x \rightarrow \,-2} g(x)$ does not, the overall limit $\lim_{x \rightarrow \,-2} \Bigl(3f(x) - g(x)\Bigr)$ does not exist either:

$$
\lim_{x \rightarrow \,-2} \Bigl(3f(x) - g(x)\Bigr) = \text{DNE}
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-1914-q003
content: |-
  ![](<../Source/The Sum Rule for Limits - 1914/Images/q-54403.png>)
  
  The figure below shows the graphs of $y = f(x)$ and $y = g(x)$. Evaluate $\lim_{x \to \pi}(3f(x) - g(x))$.
options:
- id: a
  content: |-
    $DNE$
  correct: true
- id: b
  content: |-
    $-3$
- id: c
  content: |-
    $-4$
- id: d
  content: |-
    $-14$
- id: e
  content: |-
    $-10$
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-1914-q004
content: |-
  ![](<../Source/The Sum Rule for Limits - 1914/Images/q-17153.png>)
  
  The figure above shows the graph of $y = f(x)$. Evaluate $\lim_{x \to \pi/2}(2x + πf(x))$.
options:
- id: a
  content: |-
    $π$
- id: b
  content: |-
    $2π$
  correct: true
- id: c
  content: |-
    $1$
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $\frac{π}{2}$
```
---

## Navigation

- [Next: Special Limits Involving Sine](<Special Limits Involving Sine - 606.md>)
- [Back to UQ-1](UQ-1.md)

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
