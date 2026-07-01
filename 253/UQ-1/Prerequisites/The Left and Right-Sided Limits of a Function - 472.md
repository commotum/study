# The Left and Right-Sided Limits of a Function

## Table of Contents

- [Introduction](#introduction)
- [Evaluating Left and Right Limits at an Interior Point](#evaluating-left-and-right-limits-at-an-interior-point)
- [Evaluating Left and Right Limits at Endpoints](#evaluating-left-and-right-limits-at-endpoints)
- [Comparing Limits that Do Not Exist](#comparing-limits-that-do-not-exist)
- [Identifying True Equalities Involving Limits](#identifying-true-equalities-involving-limits)

## Prerequisites

- [The Finite Limit of a Function](../461/461.md)

---

<a id="introduction"></a>
## Introduction

We already know that $\lim\limits_{x \to \, a} f(x)$ represents the limit of $f(x)$ as $x$ approaches $a$. However, there are really two ways that $x$ can approach $a$ -- from the left side or from the right side -- and sometimes, it matters which direction we choose.

For example, consider the function below.

- As $x \to -1$ from the left, we have $f(x) \to -4$, but
- as $x \to -1$ from the right, we have $f(x) \to -3$.

![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/0534081fc0f62990bfa81fdb4df01629.png>)

To be more precise about the direction in which $x$ approaches $a$, we use superscripts. The minus sign $(-)$ means "from the left" and the plus sign $(+)$ means "from the right."

- **Left-sided limit:** $\lim\limits_{x \to \, a^-} f(x)$ represents the limit of $f(x)$ as $x$ approaches $a$ *from the left.*
- **Right-sided limit:** $\lim\limits_{x \to \, a^+} f(x)$ represents the limit of $f(x)$ as $x$ approaches $a$ *from the right.*

For the function graphed above, the left-sided limit is

$$
\lim_\limits{x\rightarrow \,-1^{-}}f(x)=-4
$$

and the right-sided limit is

$$
\lim_\limits{x\rightarrow \,-1^{+}}f(x)=-3 \,
$$

At the same time, if we consider the point $x=-5$, we note that the left-sided limit at this point does not exist because the function to the left of $x=-5$ is not defined. If the limit does not exist, we usually denote it using the abbreviation $\textrm{DNE}{:}$

$$
\lim_\limits{x\rightarrow \,-5^{-}}f(x)=\textrm{DNE}
$$

**Note:** The "minus" superscript $(-)$ indicates "left" because the left direction is the negative direction on the number line, and the "plus" superscript $(+)$ indicates "right" because the right direction is the positive direction on the number line.

---

<a id="evaluating-left-and-right-limits-at-an-interior-point"></a>
## Evaluating Left and Right Limits at an Interior Point

**Example:** Find $\displaystyle\lim_{x\rightarrow 0^-} f(x)$ and $\displaystyle\lim_{x\rightarrow 0^+} f(x)$ for the function given below.

![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/7881705e8f8e124182a5d25f6266bbeb.png>)

**Explanation**

As $x$ approaches $0$ from the *left*, the function $f(x)$ approaches $1$. Therefore,

$$
\lim_\limits{x\rightarrow \,0^{-}}f(x) = 1 \,
$$

Likewise, as $x$ approaches $0$ from the *right*, the function $f(x)$ approaches $1$. Therefore,

$$
\lim_\limits{x\rightarrow \,0^{+}}f(x) = 1 \,
$$

In conclusion, we have

$$
\lim_\limits{x\rightarrow \,0^{-}}f(x)=\lim_\limits{x\rightarrow \,0^{+}}f(x)=1 \,
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-472-q001
content: |-
  ![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/q-16340.png>)
  
  Find $lim_(x → - \frac{π}{2}^{-})f(x)$ and $lim_(x → - \frac{π}{2}^{+})f(x)$ for the function given above.
options:
- id: a
  content: |-
    $lim_(x → - \frac{π}{2}^{-})f(x) = lim_(x → - \frac{π}{2}^{+})f(x) = \frac{π}{2}$
  correct: true
- id: b
  content: |-
    $lim_(x → - \frac{π}{2}^{-})f(x) = lim_(x → - \frac{π}{2}^{+})f(x) =-\frac{π}{2}$
- id: c
  content: |-
    $lim_(x → - \frac{π}{2}^{-})f(x) = lim_(x → - \frac{π}{2}^{+})f(x) = 0$
- id: d
  content: |-
    $lim_(x → - \frac{π}{2}^{-})f(x) = π, lim_(x → - \frac{π}{2}^{+})f(x) = \frac{π}{2}$
- id: e
  content: |-
    $lim_(x → - \frac{π}{2}^{-})f(x) = \frac{π}{2}, lim_(x → - \frac{π}{2}^{+})f(x) = π$
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-472-q002
content: |-
  ![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/q-300664.png>)
  
  If the figure above shows the graph of $f(x)$, what are $\lim_{x \to 1^-} f(x)$ and $\lim_{x \to 1^+} f(x)$?

options:
- id: a
  content: |-
    $\lim_{x \to 1^-} f(x) = 2$, and $\lim_{x \to 1^+} f(x) = 2$
  correct: true

- id: b
  content: |-
    $\lim_{x \to 1^-} f(x) = 1$, and $\lim_{x \to 1^+} f(x) = 2$

- id: c
  content: |-
    $\lim_{x \to 1^-} f(x) = 2$, and $\lim_{x \to 1^+} f(x) = 1$

- id: d
  content: |-
    $\lim_{x \to 1^-} f(x) = 0$, and $\lim_{x \to 1^+} f(x) = 2$

- id: e
  content: |-
    $\lim_{x \to 1^-} f(x) = \textrm{DNE}$, and $\lim_{x \to 1^+} f(x) = 2$
```
---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-472-q003
content: |-
  ![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/q-16545.png>)
  
  Find $lim_(x → \frac{π}{2}^{-})f(x)$ and $lim_(x → \frac{π}{2}^{+})f(x)$ for the function given above.
options:
- id: a
  content: |-
    $lim_(x → \frac{π}{2}^{-})f(x) = \frac{π}{2}, lim_(x → \frac{π}{2}^{+})f(x) = π$
  correct: true
- id: b
  content: |-
    $lim_(x → \frac{π}{2}^{-})f(x) = 2π, lim_(x → \frac{π}{2}^{+})f(x) = π$
- id: c
  content: |-
    $lim_(x → \frac{π}{2}^{-})f(x) = \frac{π}{2}, lim_(x → \frac{π}{2}^{+})f(x) = DNE$
- id: d
  content: |-
    $lim_(x → \frac{π}{2}^{-})f(x) = π, lim_(x → \frac{π}{2}^{+})f(x) = \frac{π}{2}$
- id: e
  content: |-
    $lim_(x → \frac{π}{2}^{-})f(x) = π, lim_(x → \frac{π}{2}^{+})f(x) = DNE$
```
---

<a id="evaluating-left-and-right-limits-at-endpoints"></a>
## Evaluating Left and Right Limits at Endpoints

**Example:** The function $y=f(x)$ (shown below) is defined on $x\in [-2,2]$. Find the left-sided and right-sided limits for the function at $x=-2$ and $x=2$.

![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/642bd4dd0c367ada1c65ec90cdb9a0a0.png>)

**Explanation**

We see from the graph that, approaching $x=-2$ from the right, the function approaches the value $y=4$. However, we cannot approach $x=-2$ from the left, because the function is not defined left of $x=-2$. Consequently,

$$
\lim_\limits{x\rightarrow \,-2^{-}}f(x)=\text{DNE}\,,\quad\lim_\limits{x\rightarrow \,-2^{+}}f(x)=4 \,
$$

On the other hand, approaching $x=2$ from the left, the function approaches the value $y=2$. However, we cannot approach $x=2$ from the right, because the function is not defined right of $x=2$. So we have

$$
\lim_\limits{x\rightarrow 2^{-}}f(x)=2\,,\quad\lim_\limits{x\rightarrow \,2^{+}}f(x)=\text{DNE} \,
$$

**Note:** Here, $\text{DNE}$ is simply short for "does not exist".

---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-472-q004
content: |-
  ![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/q-16384.png>)
  
  The function $y = f(x)$ (shown above) is defined on $[MATH: x ∈ (- ∞,-1)∪(-1, 2].]$ Find the left-sided limit at $x =-1$ and the right-sided limit at $x = 2$.
options:
- id: a
  content: |-
    $lim_(x → - 1^{-})f(x) = 2, lim_(x → 2^{+})f(x) = 1$
- id: b
  content: |-
    $lim_(x → - 1^{-})f(x) = 1, lim_(x → 2^{+})f(x) = 2$
- id: c
  content: |-
    $lim_(x → - 1^{-})f(x) = DNE, lim_(x → 2^{+})f(x) = DNE$
- id: d
  content: |-
    $lim_(x → - 1^{-})f(x) = 1, lim_(x → 2^{+})f(x) = DNE$
  correct: true
- id: e
  content: |-
    $lim_(x → - 1^{-})f(x) = DNE, lim_(x → 2^{+})f(x) = 2$
```
---

**Question 5:**

```quiz
type: radio
id: MA253-UQ1-472-q005
content: |-
  ![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/q-16602.png>)
  
  The function $y = f(x)$ (shown above) is defined on $[MATH: x ∈ (- ∞, \frac{1}{2}]∪(1, ∞).]$ Find the right-sided limit at $x = \frac{1}{2}$ and the left-sided limit at $x = 1$.
options:
- id: a
  content: |-
    $lim_(x → (1/2)^{+})f(x) = 0, lim_(x → 1^{-})f(x) = 0$
- id: b
  content: |-
    $lim_(x → (1/2)^{+})f(x) = 0, lim_(x → 1^{-})f(x) = DNE$
- id: c
  content: |-
    $lim_(x → (1/2)^{+})f(x) = DNE, lim_(x → 1^{-})f(x) = DNE$
  correct: true
- id: d
  content: |-
    $lim_(x → (1/2)^{+})f(x) = DNE, lim_(x → 1^{-})f(x) = 0$
- id: e
  content: |-
    $lim_(x → (1/2)^{+})f(x) = \frac{1}{2}, lim_(x → 1^{-})f(x) = 1$
```
---

<a id="comparing-limits-that-do-not-exist"></a>
## Comparing Limits that Do Not Exist

If two limits *do not exist*, then we *cannot* say that they are equal because we can't compare the undefined values.

So, if

$$
\lim\limits_{x \to a} f(x) = \text{DNE}, \qquad \lim\limits_{x \to b} g(x) = \text{DNE}
$$

then

$$
\lim\limits_{x \to a} f(x) \neq \lim\limits_{x \to b} g(x) \,
$$

---

<a id="identifying-true-equalities-involving-limits"></a>
## Identifying True Equalities Involving Limits

**Example:** Which of the following statements are true concerning the function $y=f(x)$ whose graph is shown below?

1. $\lim_\limits{x\rightarrow \,0^-}f(x)=\lim_\limits{x\rightarrow \,1^+}f(x)$
2. $\lim_\limits{x\rightarrow \,0^+}f(x)=\lim_\limits{x\rightarrow \,1^+}f(x)$
3. $\lim_\limits{x\rightarrow \,0^+}f(x)=\lim_\limits{x\rightarrow \,1^-}f(x)$

![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/159bff05b4056d41855a5746156d573a.png>)

**Explanation**

First, let's compute the limits in question.

Looking at the graph, as $x$ approaches $0$ from the left, the function value $f(x)$ approaches $0$. However, as $x$ approaches $0$ from the right, the function value $f(x)$ is undefined. So we have

$$
\lim_\limits{x\rightarrow \,0^-}f(x)=0, \qquad \lim_\limits{x\rightarrow \,0^+}f(x)=\text{DNE} \,
$$

On the other hand, as $x$ approaches $1$ from the left, the function value $f(x)$ is undefined, and as $x$ approaches $1$ from the right, the function value $f(x)$ approaches $0$. So we have

$$
\lim_\limits{x\rightarrow \,1^-}f(x)=\text{DNE}, \qquad \lim_\limits{x\rightarrow \,1^+}f(x)=0 \,
$$

Now, let's look at each statement in turn.

I.

$$
\lim_\limits{x\rightarrow \,0^-}f(x)=\lim_\limits{x\rightarrow \,1^+}f(x)
$$

becomes $0=0$, which is true.

II.

$$
\lim_\limits{x\rightarrow \,0^+}f(x)=\lim_\limits{x\rightarrow \,1^+}f(x)
$$

becomes

$$
\text{DNE}=0
$$

which is false.

III.

$$
\lim_\limits{x\rightarrow \,0^+}f(x)=\lim_\limits{x\rightarrow \,1^-}f(x)
$$

becomes

$$
\text{DNE}=\text{DNE}
$$

which is false because we can't compare the undefined values.

Therefore, only statement I is true.

---

**Question 6:**

```quiz
type: radio
id: MA253-UQ1-472-q006
content: |-
  ![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/q-47600.png>)
  
  Which of the following statements are true concerning the function $y = f(x)$ whose graph is shown above?
  
  1. $lim_(x → 1^{+})f(x) = 1$
  2. $lim_(x → 2^{+})f(x) = 1$
  3. $lim_(x → (-1)^{-})f(x) = lim_(x → (-1)^{+})f(x)$
options:
- id: a
  content: |-
    II only
- id: b
  content: |-
    II and III only
  correct: true
- id: c
  content: |-
    I and II only
- id: d
  content: |-
    I only
- id: e
  content: |-
    I and III only
```
---

**Question 7:**

```quiz
type: radio
id: MA253-UQ1-472-q007
content: |-
  ![](<../Source/The Left and Right-Sided Limits of a Function - 472/Images/q-54183.png>)
  
  Which of the following statements are true concerning the function $y = f(x)$ whose graph is shown above?
  
  1. $lim_(x → - 1^{+})f(x) = lim_(x → 0^{-})f(x)$
  2. $lim_(x → - 1^{+})f(x) = lim_(x → 0^{+})f(x)$
  3. $lim_(x → 2^{+})f(x) = lim_(x → 2^{-})f(x)$
options:
- id: a
  content: |-
    None
  correct: true
- id: b
  content: |-
    I, II, and III
- id: c
  content: |-
    II only
- id: d
  content: |-
    I only
- id: e
  content: |-
    I and II
```
---

## Navigation

- [Next: Finding the Existence of a Limit Using One-Sided Limits](<Finding the Existence of a Limit Using One-Sided Limits - 625.md>)
- [Back to UQ-1](../UQ-1.md)
