# Graphing General Polynomials

<!--
lesson-id: 2049
topic-code: MF2.2.5.4
-->

## Table of Contents

- [Introduction](#introduction)
- [Identifying Multiplicity of a Root Given a Graph](#identifying-multiplicity-of-a-root-given-a-graph)
- [Identifying True Statements Regarding the Graph of a Given Polynomial](#identifying-true-statements-regarding-the-graph-of-a-given-polynomial)
- [Identifying the Factored Polynomial Shown in a Graph](#identifying-the-factored-polynomial-shown-in-a-graph)
- [Identifying the Graph of a Factored Polynomial](#identifying-the-graph-of-a-factored-polynomial)

## Prerequisites

- [End Behavior of Polynomials](<../../../../MA/Mathematical-Foundations/MF2/2. Polynomials/2.1. Polynomials/Lessons/2.1.8. End Behavior of Polynomials.md>)

---

<a id="introduction"></a>
## Introduction

It's possible to determine information regarding the multiplicities of the roots of a polynomial from its graph. We summarize all possible cases in the table below:

| Multiplicity | Case 1 | Case 2 |
| --- | ---: | ---: |
| $1$<br><br>(Simple root) | ![](<../Source/Graphing General Polynomials - 2049/Images/63f2b30ad86b6ceefb17b5b76e1e38f3.png>) | ![](<../Source/Graphing General Polynomials - 2049/Images/6af2266b7f91657145ef859c5179437f.png>) |
| $>1$<br><br>(Multiple root)<br><br>Even | ![](<../Source/Graphing General Polynomials - 2049/Images/08d94ca599486704a0a0697c9017fe5c.png>) | ![](<../Source/Graphing General Polynomials - 2049/Images/924f678e629b3fa5049889ad9c49dee1.png>) |
| $>1$<br><br>(Multiple root)<br><br>Odd | ![](<../Source/Graphing General Polynomials - 2049/Images/da9c4a44954a55288964d4a4b74c43f7.png>) | ![](<../Source/Graphing General Polynomials - 2049/Images/4c989dbb408b4ef6e6765cfaa9c4bb7f.png>) |

Note the following:

- The graph is **tangent** to the $x$-axis at multiple roots. This means that if $x=a$ is a multiple root, then the graph of the polynomial is parallel to the $x$-axis at this point.
- If the multiplicity of a root $x=a$ is *even*, the graph just touches the $x$-axis and reverses direction at $x=a$.
- If the multiplicity of a root $x=a$ is *odd* (including a simple root of multiplicity $1$), the graph crosses the $x$-axis at $x=a$.
- The graph of the polynomial is *never* tangent to the $x$-axis at simple roots.

---

<a id="identifying-multiplicity-of-a-root-given-a-graph"></a>
## Identifying Multiplicity of a Root Given a Graph

**Example:** A part of the graph of a polynomial $p(x)$ is given above. Which of the following statements is true?

![](<../Source/Graphing General Polynomials - 2049/Images/ead16b30a111439d43b0f0b8024f158c.png>)

- $x=-4$ is a multiple root of odd multiplicity
- $x=-4$ is a multiple root of even multiplicity
- $x=-4$ is a simple root

**Explanation**

| Multiplicity | Sketch | Sketch |
| --- | ---: | ---: |
| $1$<br><br>(Simple Root) | ![](<../Source/Graphing General Polynomials - 2049/Images/8d4fa6772f455694bd3de3902a20aeeb.png>) | ![](<../Source/Graphing General Polynomials - 2049/Images/70231eae4f8dd6d1843bad449fc2e7c3.png>) |
| $>1$<br><br>(Multiple Root)<br><br>Even | ![](<../Source/Graphing General Polynomials - 2049/Images/858c9a8ff00003e7465a1ff3ed7c096b.png>) | ![](<../Source/Graphing General Polynomials - 2049/Images/53e2a4b825235fd256356c80c61c67cd.png>) |
| $>1$<br><br>(Multiple Root)<br><br>Odd | ![](<../Source/Graphing General Polynomials - 2049/Images/3d1237ff3984c61c337993fffbfe9a3b.png>) | ![](<../Source/Graphing General Polynomials - 2049/Images/b341a19379dc575c8b225b2b99d79689.png>) |

It's possible to determine information regarding the multiplicities of the roots of a polynomial from its graph.

- If the graph intersects the $x$-axis but is *not* tangent to the $x$-axis at $x=a$, we have a *simple* root $x=a$.
- If the graph is *tangent* to the $x$-axis at $x=a$, we have a *multiple* root $x=a$. Furthermore:If the graph touches the $x$-axis and reverses direction at $x=a$, the multiplicity of a root $x=a$ is *even*. If the graph crosses the $x$-axis at $x=a$, the multiplicity of a root $x=a$ is *odd*.

In our case, the graph is *tangent* to the $x$-axis at $x=-4$. So, $x=-4$ is a *multiple* root.

Furthermore, the graph touches the $x$-axis and reverses direction at $x=-4$. So, $x=-4$ has *even* multiplicity.

Therefore, $x=-4$ is a multiple root of even multiplicity.

---

**Question 1**

```quiz
type: radio
id: ma-140411
content: |-
  ![](<../Source/Graphing General Polynomials - 2049/Images/q-140411.png>)
  
  A part of the graph of a polynomial $p(x)$ is given above. Which of the following statements is true?
options:
- id: a
  content: |-
    $x = 3$ is a multiple root of even multiplicity
- id: b
  correct: true
  content: |-
    $x = 3$ is a simple root
- id: c
  content: |-
    $x = 3$ is not a root of $p(x)$
- id: d
  content: |-
    $x = 3$ is a simple root of even multiplicity
- id: e
  content: |-
    $x = 3$ is a multiple root of odd multiplicity
```

---

**Question 2**

```quiz
type: radio
id: ma-140414
content: |-
  ![](<../Source/Graphing General Polynomials - 2049/Images/q-140414.png>)
  
  A part of the graph of a polynomial $p(x)$ is shown above. Which of the following statements is true?
options:
- id: a
  content: |-
    $x =-2$ is not a root of $p(x)$
- id: b
  correct: true
  content: |-
    $x =-2$ is a multiple root of even multiplicity
- id: c
  content: |-
    $x =-2$ is a simple root of even multiplicity
- id: d
  content: |-
    $x =-2$ is a multiple root of odd multiplicity
- id: e
  content: |-
    $x =-2$ is a simple root
```

---

<a id="identifying-true-statements-regarding-the-graph-of-a-given-polynomial"></a>
## Identifying True Statements Regarding the Graph of a Given Polynomial

**Example:** The graph of a polynomial $p(x)$ is shown above. Which of the following statements are true?

![](<../Source/Graphing General Polynomials - 2049/Images/9cfc8c5b4d8ae817c96c52ab32266bc9.png>)

1. $x = -1$ is a root of even multiplicity.
2. $x=-3$ and $x=2$ are simple roots.
3. $p(x)\to-\infty$ as $x\to-\infty$.

**Explanation**

Let's analyze each statement in turn.

- Statement I is true. The root $x = -1$ has an even multiplicity because at $x = -1$ the graph just touches the $x$-axis and reverses direction.
- Statement II is true. The roots $x = -3$ and $x=2$ are simple roots because the graph crosses the $x$-axis at the points, but the curve isn't tangent to the $x$-axis at these points.
- Statement III is false. As $x$ moves left in the negative direction towards $-\infty$, the $y$ value moves up in the positive direction towards $\infty$.

Therefore, the correct answer is "I and II only".

---

**Question 3**

```quiz
type: radio
id: ma-38768
content: |-
  ![](<../Source/Graphing General Polynomials - 2049/Images/q-38768.png>)
  
  The graph of a polynomial $p(x)$ is shown above. Which of the following statements are true?
  
  1. $x = 0$ is a root of even multiplicity.
  2. $x =-1$ and $x = 2$ are roots of even multiplicity.
  3. $p(x) → ∞$ as $x → ∞$.
options:
- id: a
  content: |-
    II only
- id: b
  correct: true
  content: |-
    II and III only
- id: c
  content: |-
    I only
- id: d
  content: |-
    I, II, and III
- id: e
  content: |-
    I and II only
```

---

**Question 4**

```quiz
type: radio
id: ma-38762
content: |-
  ![](<../Source/Graphing General Polynomials - 2049/Images/q-38762.png>)
  
  The graph of a polynomial $p(x)$ is shown above. Which of the following statements are true?
  
  1. $x = 2$ is a root of even multiplicity.
  2. $x = ± 1$ are roots of odd multiplicity.
  3. $p(0) = 2$.
options:
- id: a
  correct: true
  content: |-
    I and II only
- id: b
  content: |-
    III only
- id: c
  content: |-
    II and III only
- id: d
  content: |-
    None
- id: e
  content: |-
    I only
```

---

<a id="identifying-the-factored-polynomial-shown-in-a-graph"></a>
## Identifying the Factored Polynomial Shown in a Graph

**Example:** Which of the following could be the equation of the polynomial above?

![](<../Source/Graphing General Polynomials - 2049/Images/d979178b10acbe0ddfed255dad253c61.png>)

1. $y=(x+2)(x+1)^2(x-2)$
2. $y=(x+2)^3(x+1)^2(x-2)$
3. $y=(x+2)(x+1)^2(x-2)^3$

**Explanation**

First, we notice that the function has precisely three distinct roots, $x=-2$, $x=-1$, and $x=2$.

Based on the graph, we can make the following conclusions about the multiplicities:

- Since the graph is *not* tangent to the $x$-axis at $x =-2$, this root is a simple root (the multiplicity equals $1$).
- Since the graph just touches the $x$-axis and reverses direction at $x =-1$, this root has even multiplicity.
- Since the graph passes through $x = 2$, this root has odd multiplicity, and since the graph is tangent to the $x$-axis at $x=2$, the multiplicity must be greater than one.

From the given options, the only possible equation is

$$
y= (x+2)(x+1)^2(x-2)^3
$$

---

**Question 5**

```quiz
type: radio
id: ma-38671
content: |-
  ![](<../Source/Graphing General Polynomials - 2049/Images/q-38671.png>)
  
  Which of the following could be the equation of the polynomial curve shown above?
options:
- id: a
  content: |-
    $y = 3(x + 3)(x + 1)(x - 2)$
- id: b
  correct: true
  content: |-
    $y = (x + 3)(x + 1)^{2}(x - 2)$
- id: c
  content: |-
    $y = 3(x + 2)(x + 1)(x - 2)$
- id: d
  content: |-
    $y = 2(x + 3)(x + 1)(x - 2)$
- id: e
  content: |-
    $y = 5x^{2}(x + 1)(x - 2)$
```

---

**Question 6**

```quiz
type: radio
id: ma-38668
content: |-
  ![](<../Source/Graphing General Polynomials - 2049/Images/q-38668.png>)
  
  Which of the following could be the equation of the polynomial curve shown above?
options:
- id: a
  correct: true
  content: |-
    $y =-x(x + 1)(x - 1)$
- id: b
  content: |-
    $y =-x^{2}(x + 1)(x - 1)^{2}$
- id: c
  content: |-
    $y =-x(x + 1)(x - 1)(x + 2)$
- id: d
  content: |-
    $y =-x(x + 1)^{2}(x - 1)$
- id: e
  content: |-
    $y =-x(x + 1)^{2}(x - 1)(x + 2)$
```

---

<a id="identifying-the-graph-of-a-factored-polynomial"></a>
## Identifying the Graph of a Factored Polynomial

**Example:** Which of the above could be the graph of $y = (x+2)(x+1)^2(x-2)$?

![](<../Source/Graphing General Polynomials - 2049/Images/4ca45f72e9238f127f4f2fb3f6072708.png>)

**Explanation**

Based on the factored equation, we can make the following conclusions about the graph:

- Since the multiplicity of the roots $x=\pm 2$ is $1$, which is odd, the graph must cross the $x$-axis at these points. Moreover, because $x=\pm 2$ are simple roots, the graph must *not* be tangent to the $x$-axis at these points.
- Since the multiplicity of the root $x=-1$ is $2$, which is even, the graph just touches the $x$-axis and reverses direction at this point.

Only the graphs $\textbf{I}$ and $\textbf{III}$ satisfy these conditions.

To choose between these two graphs, we need to consider the end behavior. Since the leading coefficient is positive, as $x$ approaches $\infty$, $y$ approaches $\infty$.

Only graph $\textbf{III}$ displays this end behavior. Therefore, the correct answer is **$\textbf{III}$**.

---

**Question 7**

```quiz
type: radio
id: ma-38632
content: |-
  ![](<../Source/Graphing General Polynomials - 2049/Images/q-38632.png>)
  
  Which of the above could be the graph of $y =-5x^{2}(x - 1)^{2}(x - 2)$?
options:
- id: a
  content: |-
    $III$
- id: b
  content: |-
    $I$
- id: c
  correct: true
  content: |-
    $IV$
- id: d
  content: |-
    None of the given graphs are correct
- id: e
  content: |-
    $II$
```

---

**Question 8**

```quiz
type: radio
id: ma-38630
content: |-
  ![](<../Source/Graphing General Polynomials - 2049/Images/q-38630.png>)
  
  Which of the above could be the graph of $y = x(x + 1)(x - 1)$?
options:
- id: a
  content: |-
    $II$
- id: b
  correct: true
  content: |-
    $I$
- id: c
  content: |-
    None of the given graphs are correct
- id: d
  content: |-
    $III$
- id: e
  content: |-
    $IV$
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
