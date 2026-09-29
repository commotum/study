# Interpreting the Graph of a Function's Derivative

<!--
lesson-id: 624
topic-code: CA1.7.2.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Determining Increasing and Decreasing Intervals Given the Graph of a Derivative](#determining-increasing-and-decreasing-intervals-given-the-graph-of-a-derivative)
- [Relative Extrema](#relative-extrema)
- [Determining Relative Extrema Given the Graph of a Derivative](#determining-relative-extrema-given-the-graph-of-a-derivative)
- [Interpreting the Graph of a Function's Derivative: Word Problem](#interpreting-the-graph-of-a-functions-derivative-word-problem)

## Prerequisites

- [Sketching the Derivative of a Function From the Function's Graph](<../../../MA/Single-Variable-Calculus/CA1/7. Analytical Applications of Differentiation/7.2. Analysis of Curves/Lessons/7.2.1. Sketching the Derivative of a Function From the Function's Graph.md>)
- [Using the First Derivative Test to Classify Local Extrema](<../../../MA/Mathematical-Foundations/MF3/8. Differentiation/8.2. Analytical Applications of Differentiation/Lessons/8.2.7. Using the First Derivative Test to Classify Local Extrema.md>)

---

<a id="introduction"></a>
## Introduction

Suppose that $f(x)$ is a differentiable function. The graph of the derivative $y=f'(x)$ is given below. Can we determine the intervals on which $f(x)$ is increasing or decreasing?

![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/328c4d6691648c740789a4955e9649f3.png>)

To solve this problem, we use the following theorem:

> *A differentiable function $f(x)$ is increasing on the interval $(a,b)$ if the derivative $f'(x)$ is positive for every value in $(a,b)$.*

We also have the following related theorem:

> *A differentiable function $f(x)$ is decreasing on the interval $(a,b)$ if the derivative $f'(x)$ is negative for every value in $(a,b)$.*

From the graph, we see that $f'(x) > 0$ on the intervals
$(0,4), \quad (7,10), \quad (10,15)$.

Also from the graph, we see that $f'(x) < 0$ on the intervals

$$
(4,7), \quad (15, \infty)
$$

Therefore, $f(x)$ is increasing for $x \in (0,4) \cup (7,10) \cup (10,15)$ and decreasing for $x \in (4,7) \cup (15, \infty)$.

---

<a id="determining-increasing-and-decreasing-intervals-given-the-graph-of-a-derivative"></a>
## Determining Increasing and Decreasing Intervals Given the Graph of a Derivative

**Example:** The graph of $y=f'(x)$, the derivative of $f(x)$, is given below. Find all the values of $x$ where the function $y=f(x)$ is decreasing.

![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/21a4b398840f1a1c023bb6a4f6be940d.png>)

**Explanation**

First, we recall the following:

- If $f'(x) = 0$ for all $x \in (a,b)$, then the slope of $f(x)$ is equal to zero on $(a,b)$.
- If $f'(x) > 0$ for all $x \in (a,b)$, then the slope of $f(x)$ is positive on $(a,b)$.
- If $f'(x) < 0$ for all $x \in (a,b)$, then the slope of $f(x)$ is negative on $(a,b)$.

From the above graph, we can see that $f'(x)$ is negative on the intervals $(-5,-2)$, $(0,2)$ and $(5,\infty)$:

![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/563c18d94ba3384f2aa7c230663efb75.png>)

Therefore, $f(x)$ is decreasing when $x\in (-5,-2) \cup (0,2) \cup (5,\infty)$.

---

**Question 1**

```quiz
type: radio
id: ma-30681
content: |-
  ![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/q-30681.png>)

  The graph of $y = f^{′}(x)$, the derivative of $f(x)$, is given above. Find all the values of $x$ where the function $y = f(x)$ is increasing.
options:
- id: a
  content: |-
    $x ∈ (-6, 0)∪(3, 6)$
  correct: true
- id: b
  content: |-
    $x ∈ (-6, 1)$
- id: c
  content: |-
    $x ∈ (0, 3)∪(6, ∞)$
- id: d
  content: |-
    $x ∈ (-6, 0)∪(0, 3)∪(3, 6)$
- id: e
  content: |-
    $x ∈ (- ∞,-4)∪(2, 4)$
```

---

**Question 2**

```quiz
type: radio
id: ma-5215
content: |-
  ![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/q-5215.png>)

  The graph of $y = f^{′}(x)$, the derivative of $f(x)$, is given above. Find all the values of $x$ where the slope of the function $y = f(x)$ is positive.
options:
- id: a
  content: |-
    $x ∈ (-1, 4)$
- id: b
  content: |-
    $x ∈ (- ∞,-5)∪(6, ∞)$
- id: c
  content: |-
    $x ∈ (- ∞,-5)∪(-1, 4)∪(6, ∞)$
  correct: true
- id: d
  content: |-
    $x ∈ (-5,-1)∪(4, 6)$
- id: e
  content: |-
    $x ∈ (-3.5, 1.5)∪(5.5, ∞)$
```

---

<a id="relative-extrema"></a>
## Relative Extrema

Recall that we can use the first derivative test to identify the relative extrema of a continuous function $f(x)$:

- $f(x)$ has a relative maximum at $x=a$ if $f'(x)$ changes its sign from *positive* to *negative* around $x=a$.![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/cd5ea6cac13140964f716a24613346a6.png>)

- $f(x)$ has a relative minimum at $x=a$ if $f'(x)$ changes its sign from *negative* to *positive* around $x=a$.![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/41cdbeff0f98192f70a09364ce697ae3.png>)

So, to determine the relative extrema of a function $f(x)$ by looking at a graph of $f'(x)$, we need to pay attention to the locations where $f'(x)$ changes sign.

---

<a id="determining-relative-extrema-given-the-graph-of-a-derivative"></a>
## Determining Relative Extrema Given the Graph of a Derivative

**Example:** The graph of $y=z'(x)$, the derivative of $z(x)$, is given below. Find all the values of $x$ where the function $z(x)$ has a relative extremum. You may assume that all of the $x$-intercepts of $y=z'(x)$ are shown in the picture.

![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/58b8a232e3b2fbfe54f6e426371204d7.png>)

**Explanation**

First, we recall the following:

- If $z'(x)=0$ or $z'(x)$ is undefined, then we have a critical point.
- If $z'(x)>0$, then $z(x)$ is increasing.
- If $z'(x)< 0$, then $z(x)$ is decreasing.

The function $z(x)$ has a relative extremum at $x=a$, if the following two conditions are satisfied:

- $z'(x)=0$ or it's undefined, and
- $z'(x)$ changes its sign (going from left to right) at that point.

We summarize the information from the graph in the table below:

| $x$ | $(-\infty,3)$ | $3$ | $(3,4)$ | $4$ | $(4,5)$ | $5$ | $(5,8)$ | $8$ | $(8,\infty)$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $z'$ | $+$ | $0$ | $-$ | $\text{not def.}$ | $+$ | $0$ | $-$ | $0$ | $-$ |
| $p$ | $\nearrow$ | $\textrm{max}$ | $\searrow$ | $\textrm{min}$ | $\nearrow$ | $\textrm{max}$ | $\searrow$ | $\textrm{not extr.}$ | $\searrow$ |

In our case, we obtain relative extrema at $x=3$, $x=4$, and $x=5$.

Notice that $x=8$ is *not* a relative extremum because the sign of $z'(x)$ does not change either side of this critical point.

---

**Question 3**

```quiz
type: radio
id: ma-5223
content: |-
  ![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/q-5223.png>)

  The graph of $y = p^{′}(x)$, the derivative of a continuous function $p(x)$, is given above. Find all the values of $x$ where the function $p(x)$ has a local extremum. You may assume that all of the $x$-intercepts of $y = p^{′}(x)$ are shown in the picture.
options:
- id: a
  content: |-
    $x =-6$ and $x =-2$
- id: b
  content: |-
    $x = 1$, $x = 2$, and $x = 3$
- id: c
  content: |-
    $x = 0$, $x = 5$, and $x = 6$
  correct: true
- id: d
  content: |-
    $x = 0$ and $x = 4$
- id: e
  content: |-
    $x =-2$ and $x = 2$
```

---

**Question 4**

```quiz
type: radio
id: ma-30678
content: |-
  ![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/q-30678.png>)

  The graph of $y = h^{′}(x)$, the derivative of $h(x)$, is given above. Find all the values of $x$ where the function $h(x)$ has a relative minimum. You may assume that all of the $x$-intercepts of $y = h^{′}(x)$ are shown in the picture.
options:
- id: a
  content: |-
    $x = 0$ only
- id: b
  content: |-
    $x =-2$ only
- id: c
  content: |-
    $x =-6$ and $x = 4$ only
  correct: true
- id: d
  content: |-
    $x =-6$, $x =-2$, and $x = 4$
- id: e
  content: |-
    $x =-2$ and $x = 2$ only
```

---

<a id="interpreting-the-graph-of-a-functions-derivative-word-problem"></a>
## Interpreting the Graph of a Function's Derivative: Word Problem

**Example:** Let $v(t)$ denote the speed (in $\textrm{km/h}$) of a hurricane at time $t$ (in hours) since the hurricane originated in the Atlantic Ocean. The graph of $y=v'(t)$, the derivative of $v(t)$, is given below. Find all the values of $t$ where the speed of the hurricane is decreasing.

![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/f7bcd852222b85761d5db669bc2c4b57.png>)

**Explanation**

First, we recall the following:

- If $v'(t) = 0$ for all $t \in (a,b)$, then $v(t)$ is constant on $(a,b)$.
- When $v'(t) > 0$ for all $t \in (a,b)$, then $v(t)$ is increasing on $(a,b)$.
- When $v'(t) < 0$ for all $t \in (a,b)$, then $v(t)$ is decreasing on $(a,b)$.

From the above graph, we can see that $v'(t)$ is negative on the intervals $[MATH: [0,2)]$ and $[MATH: (7,8]:]$

![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/441459626f4e25fe66cdba20d33d4fcb.png>)

Therefore, the speed of the hurricane is decreasing when $t \in [0,2) \cup (7,8]$.

---

**Question 5**

```quiz
type: radio
id: ma-30675
content: |-
  ![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/q-30675.png>)

  Let $g(t)$ denote the population of bears between $1980$ and $1988$ in a certain country, where $t$ is the number of years since the year $1980$. The graph of $y = g^{′}(t)$, the derivative of $y = g(t)$, is given above. In what year did the population reach a relative maximum?
options:
- id: a
  content: |-
    $1985$
- id: b
  content: |-
    $1984$
- id: c
  content: |-
    $1982$
  correct: true
- id: d
  content: |-
    $1983$
- id: e
  content: |-
    $1986$
```

---

**Question 6**

```quiz
type: radio
id: ma-30594
content: |-
  ![](<../Source/Interpreting the Graph of a Function's Derivative - 624/Images/q-30594.png>)

  Let $v(t)$ denote the speed of a car at time $t$ (in hours) since the car started its journey. The graph of $y = v^{′}(t)$, the derivative of $v(t)$, is given above. Find all the values of $t$ where the speed of a car is decreasing.
options:
- id: a
  content: |-
    $t ∈ (0, 4)∪(6, 8)$
- id: b
  content: |-
    $t ∈ (0, 4)$
- id: c
  content: |-
    $t ∈ (1, 5)$
- id: d
  content: |-
    $t ∈ (4, 6)$
  correct: true
- id: e
  content: |-
    $t ∈ (6, 8)$
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
