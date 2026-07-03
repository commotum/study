# Finding the Existence of a Limit Using One-Sided Limits

## Table of Contents

- [Introduction](#introduction)
- [Identifying the Limit at an Interior Point](#identifying-the-limit-at-an-interior-point)
- [Identifying the Limit at an Endpoint](#identifying-the-limit-at-an-endpoint)
- [Identifying True Statements About Limits](#identifying-true-statements-about-limits)

## Prerequisites

- [The Left and Right-Sided Limits of a Function](../472/472.md)

---

<a id="introduction"></a>
## Introduction

In general, the limit of a function $f(x)$ at a point only exists if *both* the left-sided and right-sided limits *exist* and are the *same*.

For example, suppose we want to compute $\lim_{x\rightarrow 2}f(x)$ for the function whose graph is shown below. To do this, we must first compute the left and right-sided limits.

![](<253/M-1/UQ-1/Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/5633c1581be3cf554a210e0e5736d611.png>)

As $x$ approaches $2$ from the left, $y$ approaches $0$. However, as $x$ approaches $2$ from the right, $y$ approaches $1$. Therefore, we have the following left and right-sided limits.

$$
\begin{bmatrix}Left-sided limit: & \lim_{x \to 2^{-}}f(x) = 0 \\ Right-sided limit: & \lim_{x \to 2^{+}}f(x) = 1\end{bmatrix}
$$

Both of these limits exist. However, they are *not* the same. Consequently, the overall limit at $x=2$ does not exist:

$$
\lim_{x\rightarrow 2}f(x)=\text{DNE}
$$

---

<a id="identifying-the-limit-at-an-interior-point"></a>
## Identifying the Limit at an Interior Point

**Example:** Find $\lim_{x\rightarrow 0}f(x)$ for the function $f(x)$ plotted below.

![](<253/M-1/UQ-1/Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/c8b132237879e9590da52da233c11da9.png>)

**Explanation**

From the graph, we see that as we approach $x=0$ from the left, the $y$ value approaches $2$. So the left-hand limit is

$$
\lim_{x\rightarrow \,0^{-}}f(x)=2
$$

Similarly, when we approach $x=0$ from the right, the $y$ value again approaches $2$. So the right-hand limit is

$$
\lim_{x\rightarrow \,0^{+}}f(x)=2
$$

Since both the left and right-hand limits exist and are equal to $2$, we conclude that

$$
\lim_{x\rightarrow \,0}f(x)=2
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-625-q001
content: |-
  ![](<../Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/q-54404.png>)
  
  Find $\lim_{x \to \pi/2}f(x)$ for the function $f(x)$ plotted above.
options:
- id: a
  content: |-
    $\frac{π}{2}$
- id: b
  content: |-
    $DNE$
  correct: true
- id: c
  content: |-
    $\frac{3π}{4}$
- id: d
  content: |-
    $π$
- id: e
  content: |-
    $0$
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-625-q002
content: |-
  ![](<../Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/q-16604.png>)
  
  Find $\lim_{x \to \pi}f(x)$ for the function $f(x)$ plotted above.
options:
- id: a
  content: |-
    $\lim_{x \to \pi}f(x) = DNE$
- id: b
  content: |-
    $\lim_{x \to \pi}f(x) = 0$
- id: c
  content: |-
    $\lim_{x \to \pi}f(x) = 1$
  correct: true
- id: d
  content: |-
    $\lim_{x \to \pi}f(x) = 2$
- id: e
  content: |-
    $\lim_{x \to \pi}f(x) = π$
```
---

<a id="identifying-the-limit-at-an-endpoint"></a>
## Identifying the Limit at an Endpoint

**Example:** The function $y=f(x)$ is defined on $[MATH: x\in (1,5].]$ Find $\lim_{x\rightarrow \, 1}f(x)$ for the function.

![](<253/M-1/UQ-1/Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/6bfb9a65af6c19f313aee04796643568.png>)

**Explanation**

From the graph, we see that it is not possible to approach $x=1$ from the left. Therefore,

$$
\lim_{x\rightarrow \,1^{-}}f(x)=\text{DNE}
$$

When we approach $x=1$ from the right, we have

$$
\lim_{x\rightarrow \,1^{+}}f(x)=1
$$

Since

$$
\lim_{x\rightarrow 1^-} f(x) \ne \lim_{x\rightarrow 1^+} f(x)
$$

we conclude that

$$
\lim_{x\rightarrow \,1}f(x)=\text{DNE}
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-625-q003
content: |-
  ![](<../Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/q-16785.png>)
  
  The function $y = f(x)$ is defined on $[MATH: x ∈ (- ∞,-1]∪[- \frac{1}{2}, \frac{1}{2}]∪[1, ∞).]$ Find $\lim_{x \to - 1}f(x)$.
options:
- id: a
  content: |-
    $\lim_{x \to - 1}f(x) =-1$
- id: b
  content: |-
    $\lim_{x \to - 1}f(x) = 1$
- id: c
  content: |-
    $\lim_{x \to - 1}f(x) = \frac{1}{4}$
- id: d
  content: |-
    $\lim_{x \to - 1}f(x) = \frac{1}{2}$
- id: e
  content: |-
    $\lim_{x \to - 1}f(x) = DNE$
  correct: true
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-625-q004
content: |-
  ![](<../Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/q-16784.png>)
  
  The function $y = f(x)$ is defined on $[MATH: x ∈ (- ∞, \frac{1}{2}]∪(1, ∞).]$ Find $\lim_{x \to 1}f(x)$.
options:
- id: a
  content: |-
    $\lim_{x \to 1}f(x) = 0$
- id: b
  content: |-
    $\lim_{x \to 1}f(x) = DNE$
  correct: true
- id: c
  content: |-
    $\lim_{x \to 1}f(x) = \frac{1}{2}$
- id: d
  content: |-
    $\lim_{x \to 1}f(x) = 1$
- id: e
  content: |-
    $\lim_{x \to 1}f(x) = 2$
```
---

<a id="identifying-true-statements-about-limits"></a>
## Identifying True Statements About Limits

**Example:** Which of the following statements are true concerning the function $y=f(x)$ whose graph is shown below?

1. $\lim_{x\rightarrow \,2}f(x)=0$
2. $\lim_{x\rightarrow \,1}f(x)=\text{DNE}$
3. $\lim_{x\rightarrow \,-1}f(x)=\lim_{x\rightarrow \,0}f(x)$

![](<253/M-1/UQ-1/Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/65239b582d4f27c0e7d954e49afd4996.png>)

**Explanation**

Let's analyze each statement in turn.

- Statement I is true. We see from the graph that $\lim_{x\rightarrow \,2^-}f(x)=\lim_{x\rightarrow \,2^+}f(x)=0$. Consequently, $\lim_{x\rightarrow \,2}f(x)=0$.
- Statement II is true. When approaching $x=1$ from the left and from the right, we get
$\lim_{x\rightarrow \,1^-}f(x)=0, \qquad \lim_{x\rightarrow \,1^+}f(x)=3$,
respectively. Since $\lim_{x\rightarrow \,1^-}f(x)\ne\lim_{x\rightarrow \,1^+}f(x)$, we conclude that $\lim_{x\rightarrow \,1}f(x)=\text{DNE}$.
- Statement III is false. Both limits $\lim_{x\rightarrow \,-1}f(x)$ and $\lim_{x\rightarrow \,0}f(x)$ do not exist because the function $f(x)$ is not given in the interval $[MATH: [-1,0)]$. We *cannot* say that the limits are equal because we can't compare the undefined values.

In conclusion, only statements I and II are true.

---

**Question 5:**

```quiz
type: radio
id: MA253-UQ1-625-q005
content: |-
  ![](<../Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/q-34942.png>)
  
  Which of the following statements are true concerning the function $y = f(x)$ whose graph is shown above?
  
  1. $\lim_{x \to - 1}f(x) = DNE$
  2. $\lim_{x \to 1}f(x) = 2$
  3. $\lim_{x \to 0}f(x) = \lim_{x \to 2}f(x)$
options:
- id: a
  content: |-
    I and II only
  correct: true
- id: b
  content: |-
    I and III only
- id: c
  content: |-
    III only
- id: d
  content: |-
    II and III only
- id: e
  content: |-
    I only
```
---

**Question 6:**

```quiz
type: radio
id: MA253-UQ1-625-q006
content: |-
  ![](<../Source/Finding the Existence of a Limit Using One-Sided Limits - 625/Images/q-47596.png>)
  
  Which of the following statements are true concerning the function $y = f(x)$ whose graph is shown above?
  
  1. $\lim_{x \to - 1}f(x) = 4$
  2. $\lim_{x \to 1}f(x) = DNE$
  3. $\lim_{x \to 3}f(x) = 1$
options:
- id: a
  content: |-
    II only
- id: b
  content: |-
    I and III only
- id: c
  content: |-
    I and II only
- id: d
  content: |-
    II and III only
  correct: true
- id: e
  content: |-
    III only
```
---

## Navigation

- [Next: Limits of Power Functions, and the Constant Rule for Limits](<Limits of Power Functions, and the Constant Rule for Limits - 1716.md>)
- [Back to UQ-1](UQ-1.md)
