# The Finite Limit of a Function


<!--
lesson-id: 461
topic-code: MF2.11.1.1
-->
## Table of Contents

- [Introduction](#introduction)
- [Finding a Limit When the Function Value is Not Defined](#finding-a-limit-when-the-function-value-is-not-defined)
- [Limit Has Nothing to Do with Function Value](#limit-has-nothing-to-do-with-function-value)
- [Finding a Limit When the Limit is Not Equal to the Function Value](#finding-a-limit-when-the-limit-is-not-equal-to-the-function-value)
- [Identifying True Statements About Limits](#identifying-true-statements-about-limits)

## Prerequisites

- [Piecewise Functions](../165/165.md)

---

<a id="introduction"></a>
## Introduction

The **limit** of a function is the value that the function approaches. For example, the function $y=f(x)$ shown below is not defined at $x=2$, as represented by the open circle there $-$ but when we *approach* $x=2$, we see that $f(x)$ *approaches* the value $y=1$.

![](<253/M-1/UQ-1/Source/The Finite Limit of a Function - 461/Images/771b75fb2f377e3f83070583105136a1.png>)

As $x$ approaches $2$, the value of $f(x)$ approaches $1$. In other words, the limit of $f(x)$, as $x$ approaches $2$, is $1$. We can express this mathematically as

$$
\lim_{x\rightarrow 2}f(x)=1 \,
$$

---

<a id="finding-a-limit-when-the-function-value-is-not-defined"></a>
## Finding a Limit When the Function Value is Not Defined

**Example:** Find $\lim_{x\rightarrow \,-1}f(x)$ for the function $f(x)$ whose graph is shown below.

![](<253/M-1/UQ-1/Source/The Finite Limit of a Function - 461/Images/b6347eacfd36c53c6aaae5603a25de44.png>)

**Explanation**

As $x$ approaches $-1$, the value of $f(x)$ approaches $2$. Consequently,

$$
\lim_{x\rightarrow \,-1}f(x)=2\,
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-461-q001
content: |-
  ![](<../Source/The Finite Limit of a Function - 461/Images/q-16220.png>)
  
  Find $\lim_{x \to 1}f(x)$ for the function $f(x)$ whose graph is shown above.
options:
- id: a
  content: |-
    $2$
- id: b
  content: |-
    $0$
  correct: true
- id: c
  content: |-
    $1$
- id: d
  content: |-
    $\frac{3}{2}$
- id: e
  content: |-
    $\frac{1}{2}$
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-461-q002
content: |-
  ![](<../Source/The Finite Limit of a Function - 461/Images/q-16218.png>)
  
  Find $\lim_{x \to 0}f(x)$ for the function $f(x)$ whose graph is shown above.
options:
- id: a
  content: |-
    $1$
- id: b
  content: |-
    $0.5$
- id: c
  content: |-
    $2$
  correct: true
- id: d
  content: |-
    $1.5$
- id: e
  content: |-
    $0$
```
---

<a id="limit-has-nothing-to-do-with-function-value"></a>
## Limit Has Nothing to Do with Function Value

The limit of a function at some point has **nothing to do** with the value of the function at that point.

For example, the following functions $g(x)$ and $h(x)$ have *different values* at $x=2$, but they have the *same limit* at $x=2$.

![](<253/M-1/UQ-1/Source/The Finite Limit of a Function - 461/Images/9208247688dd7857b2e51d760265a2e6.png>)

![](<253/M-1/UQ-1/Source/The Finite Limit of a Function - 461/Images/5a2a74794da6b4b944a16d85db96f388.png>)

The actual values of $g(2)$ and $h(2)$ are irrelevant for determining the limit at $x=2$. All that matters is what values the functions *look like* they are approaching as $x$ approaches $2$.

Near $x=2$, both $g(x)$ and $h(x)$ appear to be approaching $y=1$. Therefore,

$$
\lim_{x\rightarrow 2}g(x)=1
$$

and

$$
\lim_{x\rightarrow 2}h(x)=1 \,
$$

---

<a id="finding-a-limit-when-the-limit-is-not-equal-to-the-function-value"></a>
## Finding a Limit When the Limit is Not Equal to the Function Value

**Example:** Find $\lim_{x\rightarrow \,0} f(x)$ for the function below.

![](<253/M-1/UQ-1/Source/The Finite Limit of a Function - 461/Images/44f08bb51e4cdb3911ee54733d69b8b5.png>)

**Explanation**

As $x$ approaches $0$, the value of $f(x)$ approaches $1$. Consequently,

$$
\lim_{x\rightarrow \,0}f(x)= 1\,
$$

Remember, it does not matter that the actual value of $f(0)$ is $2$. All that matters is that as $x$ approaches $0$, the function $f(x)$ *looks like* it is getting closer and closer to $1$.

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-461-q003
content: |-
  ![](<../Source/The Finite Limit of a Function - 461/Images/q-16261.png>)
  
  Find $\lim_{x \to 3}f(x)$ for the function above.
options:
- id: a
  content: |-
    $-4$
- id: b
  content: |-
    $1$
- id: c
  content: |-
    $3$
- id: d
  content: |-
    $0$
  correct: true
- id: e
  content: |-
    $-1$
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-461-q004
content: |-
  ![](<../Source/The Finite Limit of a Function - 461/Images/q-16266.png>)
  
  Find $\lim_{x \to 2}f(x)$ for the function above.
options:
- id: a
  content: |-
    $0$
- id: b
  content: |-
    $3$
- id: c
  content: |-
    $4$
- id: d
  content: |-
    $1$
- id: e
  content: |-
    $2$
  correct: true
```
---

<a id="identifying-true-statements-about-limits"></a>
## Identifying True Statements About Limits

**Example:** Which of the following statements are true concerning the function $y=f(x)$ whose graph is shown below?

1. $\lim_{x\rightarrow \,0}f(x)=0$
2. $\lim_{x\rightarrow \,3}f(x)=0$
3. $\lim_{x\rightarrow \,-1}f(x)=\lim_{x\rightarrow \,1}f(x)$

![](<253/M-1/UQ-1/Source/The Finite Limit of a Function - 461/Images/42148299c32a941ad027d9e49c2933f7.png>)

**Explanation**

Let's analyze each statement in turn.

- Statement I is false. As $x$ approaches $0$, the function $f(x)$ approaches the value $y=-1$. Consequently,
$\lim_{x\rightarrow \,0}f(x)=-1$.
- Statement II is true. As $x$ approaches $3$, the function $f(x)$ approaches the value $y=0$. Consequently,
$\lim_{x\rightarrow \,3}f(x)=0$.
- Statement III is false. As $x$ approaches $-1$ the function $f(x)$ approaches the value $y=2$, and consequently
$\lim_{x\rightarrow \,-1}f(x)=2$.
Similiarly, as $x$ approaches $1$, the function $f(x)$ approaches the value $y=-2$, and consequently
$\lim_{x\rightarrow \,1}f(x)=-2$.
As a result,
$\lim_{x\rightarrow \,-1}f(x)\ne\lim_{x\rightarrow \,1}f(x)$.

In conclusion, only statement II is true.

---

**Question 5:**

```quiz
type: radio
id: MA253-UQ1-461-q005
content: |-
  ![](<../Source/The Finite Limit of a Function - 461/Images/q-34932.png>)
  
  Which of the following statements are true concerning the function $y = f(x)$ whose graph is shown above?
  
  1. $\lim_{x \to - 2}f(x) = 0$
  2. $\lim_{x \to - 3}f(x) =-2$
  3. $\lim_{x \to - 2}f(x) = \lim_{x \to 2}f(x)$
options:
- id: a
  content: |-
    II and III only
  correct: true
- id: b
  content: |-
    I and II only
- id: c
  content: |-
    III only
- id: d
  content: |-
    I and III only
- id: e
  content: |-
    II only
```
---

**Question 6:**

```quiz
type: radio
id: MA253-UQ1-461-q006
content: |-
  ![](<../Source/The Finite Limit of a Function - 461/Images/q-34840.png>)
  
  Which of the following statements are true concerning the function $y = f(x)$ whose graph is shown above?
  
  1. $\lim_{x \to - 1}f(x) = 2$
  2. $\lim_{x \to 0}f(x) = 2$
  3. $\lim_{x \to 1}f(x) = \lim_{x \to 3}f(x)$
options:
- id: a
  content: |-
    I and II only
- id: b
  content: |-
    I and III only
- id: c
  content: |-
    II and III only
  correct: true
- id: d
  content: |-
    II only
- id: e
  content: |-
    III only
```
---

## Navigation

- [Next: The Left and Right-Sided Limits of a Function](<The Left and Right-Sided Limits of a Function - 472.md>)
- [Back to UQ-1](UQ-1.md)

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
