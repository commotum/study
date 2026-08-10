# Invertible Functions

<!--
lesson-id: 1889
topic-code: MF2.4.1.10
-->

## Table of Contents

- [Introduction](#introduction)
- [Identifying an Invertible Function From Its Graph](#identifying-an-invertible-function-from-its-graph)
- [Identifying the Intervals on Which a Function is Invertible Given Its Graph](#identifying-the-intervals-on-which-a-function-is-invertible-given-its-graph)
- [Identifying the Intervals on Which a Function is Invertible Given a Description](#identifying-the-intervals-on-which-a-function-is-invertible-given-a-description)

## Prerequisites

- [Graphs of Inverse Functions](<../../../../MA/Mathematical-Foundations/MF2/4. Functions/4.1. Functions/Lessons/4.1.8. Graphs of Inverse Functions.md>)
- [One-To-One Functions](<../../../../MA/Mathematical-Foundations/MF2/4. Functions/4.1. Functions/Lessons/4.1.5. One-To-One Functions.md>)

---

<a id="introduction"></a>
## Introduction

A function is **invertible** on an interval if and only if it's one-to-one. In other words, it must pass the horizontal line test.

Not all functions have inverses! For example, consider the function

$$
f(x)=x^2-1
$$

whose graph is shown below.

![](<../Source/Invertible Functions - 1889/Images/07db21630ebae4042156d3c6f3d9340e.png>)

Notice that $f(x)$ is not a one-to-one since it does not satisfy the horizontal line test.

To find the graph of a function's inverse, we usually reflect it over the line $y=x$. However, if we reflect $f(x)$ over the line $y=x$, the result is not a function since it will not satisfy the vertical line test.

![](<../Source/Invertible Functions - 1889/Images/30d9291902e48d3995c41e57c7e4cb49.png>)

Therefore, $f(x)$ is *not* invertible.

If a function is not invertible, we can sometimes make it invertible by restricting its domain.

Here, if we take

$$
f(x)=x^2-1
$$

over the restricted interval $x \in (0,\infty)$, then it passes the horizontal line test and we can find the corresponding inverse function by reflecting the graph of $y=f(x)$ over the line $y=x$.

![](<../Source/Invertible Functions - 1889/Images/b4247b8726c9a12dfa18b535baf58435.png>)

To determine if a function is invertible over a particular domain, we need to use the horizontal line test to check if it's a one-to-one function.

---

<a id="identifying-an-invertible-function-from-its-graph"></a>
## Identifying an Invertible Function From Its Graph

**Example:** Which of the graphs below correspond to an invertible function?

![](<../Source/Invertible Functions - 1889/Images/483fa8080bd245ed3dd303ce993001d9.png>)

**Explanation**

A function is invertible if and only if it's a one-to-one function. To determine which of the functions are one-to-one, we use the horizontal line test.

![](<../Source/Invertible Functions - 1889/Images/f7e8678ffa8b2c33f49efd58711651f5.png>)

From the above, we see that:

- In graph IV, any horizontal line will intersect the curve at most once, no matter where we draw the line. Therefore, graph IV shows a one-to-one function. This means that the function is invertible.
- For graphs I, II, and III, some horizontal lines intersect the curve more than once. So, these are not one-to-one functions. As a result, they are not invertible.

Therefore, the correct answer is "IV only".

---

**Question 1:**

```quiz
type: radio
id: ma-36000
content: |-
  ![](<../Source/Invertible Functions - 1889/Images/q-36000.png>)
  
  Which of the graphs above correspond to an invertible function?
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    I and II only
  correct: true
- id: c
  content: |-
    II only
- id: d
  content: |-
    III only
- id: e
  content: |-
    I and IV only
```

---

**Question 2:**

```quiz
type: radio
id: ma-36897
content: |-
  ![](<../Source/Invertible Functions - 1889/Images/q-36897.png>)
  
  Which of the graphs above correspond to an invertible function?
options:
- id: a
  content: |-
    II and III only
- id: b
  content: |-
    I only
- id: c
  content: |-
    II only
- id: d
  content: |-
    I and III only
  correct: true
- id: e
  content: |-
    None
```

---

<a id="identifying-the-intervals-on-which-a-function-is-invertible-given-its-graph"></a>
## Identifying the Intervals on Which a Function is Invertible Given Its Graph

**Example:** On which of the following intervals is the function $f(x)$ (shown above) invertible?

![](<../Source/Invertible Functions - 1889/Images/890bcf1d83358c5e4338a6e24ffa2521.png>)

1. $[MATH: (-3,-1]]$
2. $[MATH: (0,4]]$
3. $[MATH: [-2,2)]$

**Explanation**

A function is invertible on a particular interval if and only if it's a one-to-one function on that interval. To determine the intervals on which the function is invertible, we use the horizontal line test.

- The given function is invertible on the interval $[MATH: x\in (-3,-1].]$ Indeed, any horizontal line will intersect the curve at most once, no matter where we draw the line.

![](<../Source/Invertible Functions - 1889/Images/370f99885675d6ad20854a2868c28fde.png>)

- The given function is **not** invertible on the intervals $[MATH: (0,4]]$ and $[MATH: [-2,2)]$ because some horizontal lines will intersect the curve more than once.

![](<../Source/Invertible Functions - 1889/Images/eb2025e80374eec32f3743673ee7342c.png>)

Therefore, the correct answer is "I only".

---

**Question 3:**

```quiz
type: radio
id: ma-36941
content: |-
  ![](<../Source/Invertible Functions - 1889/Images/q-36941.png>)
  
  On which of the following intervals is the function $f(x)$ (shown above) invertible?
  
  1. $[MATH: x ∈ (-2, 0]]$
  2. $[MATH: x ∈ (-2, 2]]$
  3. $x ∈ [- 4,-2]∪[2, 4]$
options:
- id: a
  content: |-
    I and III only
- id: b
  content: |-
    II and III only
- id: c
  content: |-
    I and II only
- id: d
  content: |-
    II only
- id: e
  content: |-
    I only
  correct: true
```

---

**Question 4:**

```quiz
type: radio
id: ma-36039
content: |-
  ![](<../Source/Invertible Functions - 1889/Images/q-36039.png>)
  
  On which of the following intervals is the function $f(x)$ (shown above) invertible?
  
  1. $x ∈ [- 4, 0]$
  2. $[MATH: x ∈ (-4,-2]]$
  3. $x ∈ (-3, 1)$
options:
- id: a
  content: |-
    I and III only
- id: b
  content: |-
    I and II only
  correct: true
- id: c
  content: |-
    II only
- id: d
  content: |-
    I only
- id: e
  content: |-
    III only
```

---

<a id="identifying-the-intervals-on-which-a-function-is-invertible-given-a-description"></a>
## Identifying the Intervals on Which a Function is Invertible Given a Description

**Example:** Given that $f(x)= \mid x-2 \mid -2$, on which of the following intervals is $f(x)$ invertible?

1. $[MATH: x \in (-\infty, 2]]$
2. $x \in (0, \infty)$
3. $[MATH: x \in (-1,4]]$

**Explanation**

First, let's graph the given function. The graph of the function

$$
f(x)= \mid x-2 \mid -2
$$

can be obtained in the following way:

1. Take the curve $y= \mid x \mid$.
2. Translate it by $2$ units to the right, to get $y= \mid x-2 \mid$.
3. Finally, translate $y= \mid x-2 \mid$ by $2$ units down to get $f(x)= \mid x-2 \mid -2$.

![](<../Source/Invertible Functions - 1889/Images/d0d8a9c6b3405531dde3d55701c507e1.png>)

Now, remember that a function is invertible on a particular interval if and only if it's a one-to-one function on that interval. To determine the intervals on which the function is invertible, we use the horizontal line test.

- The function $f(x)$ is invertible on the interval $[MATH: x\in(-\infty,2].]$ Indeed, on this interval, any horizontal line will intersect the curve at most once, no matter where we draw the line.

![](<../Source/Invertible Functions - 1889/Images/bd8e8f0254d6b5268fc5a78ef6f9bbb4.png>)

- The function $f(x)$ is not invertible on any of the intervals $x\in(0,\infty)$ and $[MATH: x \in (-1,4].]$ On these intervals, some horizontal lines will intersect the curve more than once.

![](<../Source/Invertible Functions - 1889/Images/2c1748b44205856a5d6b2aa9d14612ba.png>)

Therefore, the correct answer is "I only".

---

**Question 5:**

```quiz
type: radio
id: ma-66723
content: |-
  Given that $f(x) = x + 1$, on which of the following intervals is $f(x)$ invertible?
  
  1. $x ∈ (- ∞, ∞)$
  2. $x ∈ (-1, ∞)$
  3. $x ∈ (-10, 5)$
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    III only
- id: c
  content: |-
    I and II only
- id: d
  content: |-
    I, II and III
  correct: true
- id: e
  content: |-
    II only
```

---

**Question 6:**

```quiz
type: radio
id: ma-66482
content: |-
  Given that $f(x) = x^{2} + 2$, on which of the following intervals is $f(x)$ invertible?
  
  1. $x ∈ (-2, 2)$
  2. $[MATH: x ∈ [0, ∞)]$
  3. $[MATH: x ∈ (- ∞, 0]]$
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    II and III only
  correct: true
- id: c
  content: |-
    I and II only
- id: d
  content: |-
    II only
- id: e
  content: |-
    I and III only
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
