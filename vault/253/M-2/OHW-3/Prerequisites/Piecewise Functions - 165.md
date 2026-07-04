# Piecewise Functions

<!--
lesson-id: 165
topic-code: MF1.8.1.11
-->

## Table of Contents

- [Introduction](#introduction)
- [Evaluating Piecewise Functions](#evaluating-piecewise-functions)
- [Graphing a Piecewise Step Function](#graphing-a-piecewise-step-function)
- [Graphing a Piecewise Function](#graphing-a-piecewise-function)
- [The Domain of a Piecewise Function](#the-domain-of-a-piecewise-function)

## Prerequisites

- [Equations of Lines in Point-Slope Form](<../../../6. Two-Variable Equations/6.1. Graphs of Linear Equations/Lessons/6.1.9. Equations of Lines in Point-Slope Form.md>)
- [The Domain of a Function](<8.1.4. The Domain of a Function.md>)

---

<a id="introduction"></a>
## Introduction

A **piecewise function** is a function that is defined differently in different parts of the function's domain.

For example, consider the piecewise function $f(x)$, defined as follows:

$$
{-2x,\begin{vmatrix}x \le 0 \\ \frac{1}{2}x,\end{vmatrix}x > 0
$$

A plot of the function is given below:

![](<../Source/Piecewise Functions - 165/Images/3ec3909ca0441a873e1289e20fc7d3ea.png>)

The function has two distinct branches, one for

$$
\color{red}{x\leq 0}
$$

and one for $\color{blue}{x>0}$. The function is a piecewise function because it has different definitions depending on where we are in the domain.

Suppose that we want to calculate $f(-1)$. For this, we'd use the left branch

$$
x \leq 0
$$

because

$$
-1 \leq 0
$$

On this branch, the function definition is

$$
f(x) = -2x
$$

so we have

$$
f(-1) = -2(-1) = 2
$$

Similarly, if we want to calculate $f(1)$, we'd use the right branch $x > 0$ because $1 > 0$. On this branch, the function definition is

$$
f(x) = \dfrac{1}{2}x
$$

so we have

$$
f(1) = \dfrac 1 2 \cdot 1 = \dfrac 1 2
$$

---

<a id="evaluating-piecewise-functions"></a>
## Evaluating Piecewise Functions

**Example:** For the function $g(x)$ defined on the set of integers, find $g(-12)$ and $g(3)$, where $g(x)$ is the following piecewise function:
${2x,\begin{vmatrix}x < 1 \\ 3x,\end{vmatrix}x \ge 1$

**Explanation**

- First, we compute $g(-12)$. Since $-12 < 1$, we use the first branch:
$g(x)|= 2x; g(-12)|= 2(-12); =-24$
- Next, we compute $g(3)$. Since $3 \geq 1$, we use the second branch:
$g(x)|= 3x; g(3)|= 3(3); = 9$

---

**Question 1:**

```quiz
type: radio
id: ma-7301
# MA_ANSWER_MISSING: set exactly one options[].correct=true for radio, or all correct options for checkbox
content: |-
  Given the following piecewise function $f(x)$, what is $f(3)$?
  $f(x) = {\frac{1}{4}x,\begin{vmatrix}x \le 3 \\ 5,\end{vmatrix}x > 3$
options:
- id: a
  content: |-
    $5$
- id: b
  content: |-
    Undefined
- id: c
  content: |-
    $\frac{1}{4}$
- id: d
  content: |-
    $3$
- id: e
  content: |-
    $\frac{3}{4}$
```

---

**Question 2:**

```quiz
type: radio
id: ma-6975
# MA_ANSWER_MISSING: set exactly one options[].correct=true for radio, or all correct options for checkbox
content: |-
  Given the following piecewise function $f(x)$, what is $f(-2)$?
  $f(x) = {2x,\begin{vmatrix}x < 0 \\ x + 3,\end{vmatrix}x \ge 0$
options:
- id: a
  content: |-
    $-5$
- id: b
  content: |-
    $-4$
- id: c
  content: |-
    $4$
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $5$
```

---

<a id="graphing-a-piecewise-step-function"></a>
## Graphing a Piecewise Step Function

**Example:** Given that
${3,\begin{vmatrix}x < - 3 \\ 1,\end{vmatrix}x \ge - 3$
what is the graph of $y=f(x)$?

**Explanation**

We will graph each branch separately.

- On the interval $(-\infty, -3)$, we have $f(x) = 3$, so the graph is a horizontal line that ends at $(-3,3)$, excluding this point.
- On the interval $[MATH: [-3, \infty)]$, we have $f(x) = 1$, so the graph is a horizontal line that begins at $(-3,1)$, including this point.

Therefore, the graph of the given function is as follows:

![](<../Source/Piecewise Functions - 165/Images/b3579687b947e6c3f02b536a294ed366.png>)

---

**Question 3:**

```quiz
type: radio
id: ma-46318
# MA_ANSWER_MISSING: set exactly one options[].correct=true for radio, or all correct options for checkbox
content: |-
  Given that
  $f(x) = {-1,\begin{vmatrix}x < 0 \\ 2,\end{vmatrix}x \ge 0$,
  which of the following is the graph of $y = f(x)$?
options:
- id: a
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46318-a-3.png>)
- id: b
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46318-a-4.png>)
- id: c
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46318-a-1.png>)
- id: d
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46318-a-2.png>)
- id: e
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46318-a-5.png>)
```

---

**Question 4:**

```quiz
type: radio
id: ma-46887
# MA_ANSWER_MISSING: set exactly one options[].correct=true for radio, or all correct options for checkbox
content: |-
  Given that
  $f(x) = {1,\begin{vmatrix}x \le - 2 \\ -1,\end{vmatrix}- 2 < x \le 2; 2, \mid x > 2$,
  which of the following is the graph of $y = f(x)$?
options:
- id: a
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46887-a-2.png>)
- id: b
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46887-a-5.png>)
- id: c
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46887-a-3.png>)
- id: d
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46887-a-4.png>)
- id: e
  content: |-
    ![](<../Source/Piecewise Functions - 165/Images/q-46887-a-1.png>)
```

---

<a id="graphing-a-piecewise-function"></a>
## Graphing a Piecewise Function

**Example:** If $f$ is the piecewise function
${-1,\begin{vmatrix}x \le 0 \\ -x + 2,\end{vmatrix}x > 0$
what is the graph of $y=f(x)$?

**Explanation**

We will graph each branch separately.

- On the interval $[MATH: (-\infty, 0],]$ we have $f(x) = -1$, so the graph is a horizontal line that ends at $(0,-1)$, including this point.
- On the interval $(0, \infty)$, we have $f(x) =-x+2$, so the graph is a straight line of slope $-1$ that starts from $(0,2)$, not including this point.

Therefore, the graph of the given function is as follows:

![](<../Source/Piecewise Functions - 165/Images/a8f5c97b849c224eef3cbcf0cb61b55b.png>)

---

**Question 5:**

```quiz
type: radio
id: ma-34540
# MA_ANSWER_MISSING: set exactly one options[].correct=true for radio, or all correct options for checkbox
content: |-
  ![](<../Source/Piecewise Functions - 165/Images/q-34540.png>)
  
  What is the definition of the function $y = f(x)$ shown above?
options:
- id: a
  content: |-
    $f(x) = {2,\begin{vmatrix}x \le 0 \\ x + 1,\end{vmatrix}x > 0$
- id: b
  content: |-
    $f(x) = {-1,\begin{vmatrix}x \le 0 \\ -x + 3,\end{vmatrix}x > 0$
- id: c
  content: |-
    $f(x) = {2,\begin{vmatrix}x \le 0 \\ -x + 1,\end{vmatrix}x > 0$
- id: d
  content: |-
    $f(x) = {1,\begin{vmatrix}x \le 0 \\ x - 1,\end{vmatrix}x > 0$
- id: e
  content: |-
    $f(x) = {-2,\begin{vmatrix}x \le 0 \\ x + 1,\end{vmatrix}x > 0$
```

---

**Question 6:**

```quiz
type: radio
id: ma-19304
# MA_ANSWER_MISSING: set exactly one options[].correct=true for radio, or all correct options for checkbox
content: |-
  ![](<../Source/Piecewise Functions - 165/Images/q-19304.png>)
  
  What is the definition of the function $y = f(x)$ shown above?
options:
- id: a
  content: |-
    $f(x) = {1 - x,\begin{vmatrix}x \le 1 \\ x - 1,\end{vmatrix}x > 1$
- id: b
  content: |-
    $f(x) = {2x + 1,\begin{vmatrix}x \le 1 \\ -2 - 2x,\end{vmatrix}x > 1$
- id: c
  content: |-
    $f(x) = {2x + 1,\begin{vmatrix}x \le 1 \\ 2 - 2x,\end{vmatrix}x > 1$
- id: d
  content: |-
    The graph is not a function
- id: e
  content: |-
    $f(x) = {2x - 1,\begin{vmatrix}x \le 1 \\ 1 - 2x,\end{vmatrix}x > 1$
```

---

<a id="the-domain-of-a-piecewise-function"></a>
## The Domain of a Piecewise Function

**Example:** What is the domain of the function shown below?

![](<../Source/Piecewise Functions - 165/Images/ed6823064c5202df8080ced29cdd2f96.png>)

**Explanation**

The function is defined for values between $-4$ and $1$.

- Since there is an open circle at $x=-4$, this point is not included in the domain.
- Since there is a closed circle at $x=-1$, this point is included in the domain.
- Since there is an open circle at $x=1$, this point is not included in the domain.

So, the function $f(x)$ above is defined for values between $x=-4$ and $x=1$, not including $x=-4$ and $x=1$ but including $x=-1$.

Therefore, the domain is
$x\in (-4,1)$

Note that the function is defined at the point $x=-1$, even though the function jumps at that point. The function value at $x=-1$ is $2$.

---

**Question 7:**

```quiz
type: radio
id: ma-34605
# MA_ANSWER_MISSING: set exactly one options[].correct=true for radio, or all correct options for checkbox
content: |-
  ![](<../Source/Piecewise Functions - 165/Images/q-34605.png>)
  
  What is the domain of the function $f(x)$, shown above?
options:
- id: a
  content: |-
    $[- 1, 3)∪(3, 5]$
- id: b
  content: |-
    $[MATH: [- 1, 5)]$
- id: c
  content: |-
    $(-1, 5)$
- id: d
  content: |-
    $[- 1, 5]$
- id: e
  content: |-
    $[MATH: (-1, 5]]$
```

---

**Question 8:**

```quiz
type: radio
id: ma-34612
# MA_ANSWER_MISSING: set exactly one options[].correct=true for radio, or all correct options for checkbox
content: |-
  ![](<../Source/Piecewise Functions - 165/Images/q-34612.png>)
  
  What is the domain of the function shown above?
options:
- id: a
  content: |-
    $[MATH: (- ∞,-1)∪(-1, 4]]$
- id: b
  content: |-
    $(- ∞,-1)∪(-1, 4)$
- id: c
  content: |-
    $[MATH: (- ∞, 4]]$
- id: d
  content: |-
    $[MATH: (-4,-1)∪(-1, 4]]$
- id: e
  content: |-
    $(- ∞,-1)∪(-1, ∞)$
```

```update-progress
```

[[MA/Mathematical-Foundations/MF1/Home|Home]]
[[MA/Mathematical-Foundations/MF1/0. Table of Contents/TOC|Table of Contents]]
