# Domain and Range of Inverse Functions

<!--
lesson-id: 3734
topic-code: MF2.4.1.9
-->

## Table of Contents

- [Introduction](#introduction)
- [Finding the Domain of an Inverse Function Using a Graph](#finding-the-domain-of-an-inverse-function-using-a-graph)
- [Finding the Range of an Inverse Function Using a Graph](#finding-the-range-of-an-inverse-function-using-a-graph)
- [Finding the Domain and Range of an Inverse Function Using a Description](#finding-the-domain-and-range-of-an-inverse-function-using-a-description)

## Prerequisites

- [Graphs of Inverse Functions](<../../../../MA/Mathematical-Foundations/MF2/4. Functions/4.1. Functions/Lessons/4.1.8. Graphs of Inverse Functions.md>)

---

<a id="introduction"></a>
## Introduction

Consider the function $y=f(x)$ whose graph is shown below.

![](<../Source/Domain and Range of Inverse Functions - 3734/Images/cae4284d30849a0ae3fbda37ea9ebe73.png>)

Notice that

- the domain of $f(x)$ is $[1,2]$, and
- the range of $f(x)$ is $[2,6]$.

Recall that each point $(a,b)$ on the graph of

$$
{\color{blue}y=f(x)}
$$

has a corresponding point $(b,a)$ on the graph of the inverse function

$$
{\color{red}y=f^{-1}(x)}
$$

That is to say, the $x$ and $y$ coordinates swap.

![](<../Source/Domain and Range of Inverse Functions - 3734/Images/ed179b10d207cd4fda4be1672f92932c.png>)

Notice that

- the domain of $f^{-1}(x)$ is $[2,6]$, and
- the range of $f^{-1}(x)$ is $[1,2]$.

In general:

- The domain of a function ${\color{blue}f(x)}$ is the range of its inverse function ${\color{red}f^{-1}(x)}$.
- The range of a function ${\color{blue}f(x)}$ is the domain of its inverse function ${\color{red}f^{-1}(x)}$.

---

<a id="finding-the-domain-of-an-inverse-function-using-a-graph"></a>
## Finding the Domain of an Inverse Function Using a Graph

**Example:** For the function $y = f(x)$ shown below, what is the domain of the inverse function $f^{-1}(x)$?

![](<../Source/Domain and Range of Inverse Functions - 3734/Images/f35034ce8e659187b6a1fca9736cfc55.png>)

**Explanation**

First, we recall the following:

- The domain of a function $f(x)$ is the range of its inverse function $f^{-1}(x)$.
- The range of a function $f(x)$ is the domain of its inverse function $f^{-1}(x)$.

From the graph, we see that the range of $f(x)$ is

$$
0 \leq f(x) \lt 9
$$

Therefore, the domain of $f^{-1}(x)$ is

$$
0 \leq x \lt 9
$$

---

**Question 1**

```quiz
type: radio
id: ma-7000
content: |-
  ![](<../Source/Domain and Range of Inverse Functions - 3734/Images/q-7000.png>)
  
  For the function $y = f(x)$ shown above, what is the domain of the inverse function $f^{-1}(x)$?
options:
- id: a
  content: |-
    $-2 \le x \le 2$
- id: b
  content: |-
    $-1 \le x \le 3$
  correct: true
- id: c
  content: |-
    $-2 < x < 3$
- id: d
  content: |-
    $- ∞ < x < ∞$
- id: e
  content: |-
    $-2 < x < 2$
```

---

**Question 2**

```quiz
type: radio
id: ma-155968
content: |-
  ![](<../Source/Domain and Range of Inverse Functions - 3734/Images/q-155968.png>)
  
  For the function $y = f(x)$ shown above, what is the domain of the inverse function $f^{-1}(x)$?
options:
- id: a
  content: |-
    $-2 \le x < 6$
- id: b
  content: |-
    $0 \le x < 6$
- id: c
  content: |-
    $0 < x \le 4$
  correct: true
- id: d
  content: |-
    $0 \le x \le 4$
- id: e
  content: |-
    $-2 \le x < 4$
```

---

<a id="finding-the-range-of-an-inverse-function-using-a-graph"></a>
## Finding the Range of an Inverse Function Using a Graph

**Example:** For the function $y = f(x)$ shown above, what is the range of the inverse function $f^{-1}(x)$?

![](<../Source/Domain and Range of Inverse Functions - 3734/Images/e47408d98ed45f1cce3e9b6982de4ce7.png>)

**Explanation**

First, we recall the following:

- The domain of a function $f(x)$ is the range of its inverse function $f^{-1}(x)$.
- The range of a function $f(x)$ is the domain of its inverse function $f^{-1}(x)$.

From the graph, we see that the domain of $f(x)$ is

$$
-1 \lt x \lt 4
$$

Therefore, the range of $f^{-1}(x)$ is

$$
-1 \lt f^{-1}(x) \lt 4
$$

---

**Question 3**

```quiz
type: radio
id: ma-7030
content: |-
  ![](<../Source/Domain and Range of Inverse Functions - 3734/Images/q-7030.png>)
  
  For the function $y = f(x)$ shown above, what is the range of the inverse function $f^{-1}(x)$?
options:
- id: a
  content: |-
    $-4 < f^{-1}(x) < 4$
- id: b
  content: |-
    $-2 < f^{-1}(x) < 4$
  correct: true
- id: c
  content: |-
    $-5 < f^{-1}(x) < 4$
- id: d
  content: |-
    $-5 < f^{-1}(x) < - 2$
- id: e
  content: |-
    $-5 < f^{-1}(x) < - 4$
```

---

**Question 4**

```quiz
type: radio
id: ma-156085
content: |-
  ![](<../Source/Domain and Range of Inverse Functions - 3734/Images/q-156085.png>)
  
  For the function $y = f(x)$ shown above, what is the range of the inverse function $f^{-1}(x)$?
options:
- id: a
  content: |-
    $-4 \le f^{-1}(x) < 2$
- id: b
  content: |-
    $-3 < f^{-1}(x) \le 4$
- id: c
  content: |-
    $-4 < f^{-1}(x) < 2$
- id: d
  content: |-
    $-3 \le f^{-1}(x) < 4$
  correct: true
- id: e
  content: |-
    $-3 < f^{-1}(x) < 4$
```

---

<a id="finding-the-domain-and-range-of-an-inverse-function-using-a-description"></a>
## Finding the Domain and Range of an Inverse Function Using a Description

**Example:** The domain of the function $f(x)$ is $-3\lt x \leq 3$ and the range of $f$ is $-2\leq f(x) \lt 2$. What is the range of the inverse function $f^{-1}(x)$?

**Explanation**

First, we recall the following:

- The domain of a function $f(x)$ is the range of its inverse function $f^{-1}(x)$.
- The range of a function $f(x)$ is the domain of its inverse function $f^{-1}(x)$.

The domain of $f(x)$ is

$$
-3\lt x \leq 3
$$

Therefore, the range of $f^{-1}(x)$ is

$$
-3\lt f^{-1}(x) \leq 3
$$

---

**Question 5:**

```quiz
type: radio
id: ma-35173
content: |-
  The domain of the function $f(x)$ is $-5 < x < 5$ and the range of $f$ is $-3 < f(x) < 4$. What is the range of the inverse function $f^{-1}(x)$?
options:
- id: a
  content: |-
    $-3 < f^{-1}(x) < 4$
- id: b
  content: |-
    $-3 < f^{-1}(x) < 5$
- id: c
  content: |-
    $-5 < f^{-1}(x) < 4$
- id: d
  content: |-
    $-\frac{1}{5} < f^{-1}(x) < \frac{1}{5}$
- id: e
  content: |-
    $-5 < f^{-1}(x) < 5$
  correct: true
```

---

**Question 6:**

```quiz
type: radio
id: ma-7029
content: |-
  Given that the function $f(x) = 1 - 9x$ is defined on the domain $1 \le x \le 2$, find the domain of the inverse function $f^{-1}(x)$.
options:
- id: a
  content: |-
    $1 \le x \le 2$
- id: b
  content: |-
    $-2 \le x \le - 1$
- id: c
  content: |-
    $-12 \le x \le - 5$
- id: d
  content: |-
    $-17 \le x \le - 8$
  correct: true
- id: e
  content: |-
    $8 \le x \le 17$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
