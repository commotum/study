# Compound AND Inequalities

<!--
lesson-id: 350
topic-code: MF1.5.6.14
-->

## Table of Contents

- [Introduction](#introduction)
- [Finding the Intersection of Two Inequalities](#finding-the-intersection-of-two-inequalities)
- [Solving Systems of Inequalities](#solving-systems-of-inequalities)
- [Flipping the Sign of an Inequality in a System](#flipping-the-sign-of-an-inequality-in-a-system)
- [Systems Containing Compound Inequalities](#systems-containing-compound-inequalities)

## Prerequisites

- [Intersections of Intervals](<../../../../MA/Mathematical-Foundations/MF1/5. Equations & Inequalities/5.6. Solving Linear Inequalities/Lessons/5.6.12. Intersections of Intervals.md>)
- [Solving Compound Inequalities](<../../../../MA/Mathematical-Foundations/MF1/5. Equations & Inequalities/5.6. Solving Linear Inequalities/Lessons/5.6.8. Solving Compound Inequalities.md>)

---

<a id="introduction"></a>
## Introduction

Suppose we want to find all of the values of $x$ that satisfy *both*

$$
3x+9 \geq 0
$$

*and*

$$
2x \leq -2
$$

simultaneously.

To do this, we solve each inequality individually and then compute the intersection of the two solutions.

- We start by solving $3x + 9 \geq 0$:
$\begin{bmatrix}3x + 9 & \ge 0 \\ 3x + 9 - 9 & \ge 0 - 9 \\ 3x & \ge - 9 \\ \frac{3x}{3} & \ge \frac{-9}{3} \\ x & \ge - 3\end{bmatrix}$
The solution to this inequality is shown on the number line below.![](<../Source/Compound AND Inequalities - 350/Images/30920650a46bfc93ee5e011c8efd5984.png>)

- Then, we solve $2x \leq -2$:
$\begin{bmatrix}2x & \le - 2 \\ \frac{2x}{2} & \le \frac{-2}{2} \\ x & \le - 1\end{bmatrix}$
The solution to this inequality is shown on the number line below.

![](<../Source/Compound AND Inequalities - 350/Images/cbd11e3c7e4794d3e255b7956ac308f7.png>)

To find the values of $x$ that satisfy both inequalities, we find where the two solutions overlap:

![](<../Source/Compound AND Inequalities - 350/Images/52f64062ce2e596fecab5cf9954b9b59.png>)

Thus, the final solution is

$$
\color{blue}-3 \leq x \leq -1
$$

---

<a id="finding-the-intersection-of-two-inequalities"></a>
## Finding the Intersection of Two Inequalities

**Example:** Find the values of $x$ that satisfy $2x - 5 \leq 1$ and $7x +11 < -3$.

**Explanation**

To solve compound "and" inequalities, we solve each inequality separately and then find their intersection.

- We start by solving $2x - 5 \leq 1$:
$\begin{bmatrix}2x - 5 & \le 1 \\ 2x - 5 + 5 & \le 1 + 5 \\ 2x & \le 6 \\ \frac{2x}{2} & \le \frac{6}{2} \\ x & \le 3\end{bmatrix}$

![](<../Source/Compound AND Inequalities - 350/Images/9d46a4a3b9bc085c610c11ea73fcd8e6.png>)

- Then, we solve $7x +11 < -3$:
$\begin{bmatrix}7x + 11 & < - 3 \\ 7x + 11 - 11 & < - 3 - 11 \\ 7x & < - 14 \\ \frac{7x}{7} & < \frac{-14}{7} \\ x & < - 2\end{bmatrix}$

![](<../Source/Compound AND Inequalities - 350/Images/3a8e22a4e538383d4309676749f57d55.png>)

To find the values of $x$ that satisfy both inequalities, we find where the two solutions overlap:

![](<../Source/Compound AND Inequalities - 350/Images/69726bd8e2fa576d7855c0b173151044.png>)

Thus, the final solution is $x < -2$.

---

**Question 1**

```quiz
type: radio
id: ma-218675
content: |-
  Find the values of $x$ that satisfy $9x - 17 \ge 10$ and $6x + 21 < 45$.
options:
- id: a
  content: |-
    $3 \le x < 4$
  correct: true
- id: b
  content: |-
    $3 < x < 4$
- id: c
  content: |-
    $x \ge 3$
- id: d
  content: |-
    $x < 4$
- id: e
  content: |-
    $4 \le x < 3$
```

---

**Question 2**

```quiz
type: radio
id: ma-25588
content: |-
  Which number line shows the values of $x$ that satisfy $3x - 1 \le 2$ and $4x - 1 \le - 9$?
options:
- id: a
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-25588-a-5.png>)
- id: b
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-25588-a-3.png>)
- id: c
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-25588-a-2.png>)
- id: d
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-25588-a-1.png>)
  correct: true
- id: e
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-25588-a-4.png>)
```

---

**Question 3:**

```quiz
type: radio
id: ma-102300
content: |-
  Find the set of values of $x$ that satisfy $3x + 1 \le 4$ and $2x - 3 \ge 3$.
options:
- id: a
  content: |-
    $2 \le x \le 5$
- id: b
  content: |-
    There is no solution
  correct: true
- id: c
  content: |-
    $x \ge 3$
- id: d
  content: |-
    $x \le 3$
- id: e
  content: |-
    $1 \le x \le 3$
```

---

<a id="solving-systems-of-inequalities"></a>
## Solving Systems of Inequalities

**Example:** What is the solution to the following system of inequalities?
${5x - 35 \ge 0; 7x > 21$

**Explanation**

To solve the system, we need to find the values of $x$ that satisfy both

$$
5x-35 \geq 0
$$

and $7x > 21$ simultaneously.

- First, we solve $5x-35 \geq 0$:
$\begin{bmatrix}5x - 35 & \ge 0 \\ 5x - 35 + 35 & \ge 0 + 35 \\ 5x & \ge 35 \\ \frac{5x}{5} & \ge \frac{35}{5} \\ x & \ge 7\end{bmatrix}$

![](<../Source/Compound AND Inequalities - 350/Images/baf667424ead9a250fc3a182978bde2a.png>)

- Then, we solve $7x > 21$:
$\begin{bmatrix}7x & > 21 \\ \frac{7x}{7} & > \frac{21}{7} \\ x & > 3\end{bmatrix}$

![](<../Source/Compound AND Inequalities - 350/Images/33cbebe89d32697d4d1c185e22455510.png>)

To find the values of $x$ that satisfy both inequalities, we find where the two solutions overlap:

![](<../Source/Compound AND Inequalities - 350/Images/d407eb9eeb513a2974b00914e8d15bda.png>)

Thus, the final solution is

$$
x \geq 7
$$

---

**Question 4**

```quiz
type: radio
id: ma-218740
content: |-
  What is the solution to the following system of inequalities?
  ${x + 5 \le 6; 5x - 4 < 6$

  The solution is
options:
- id: a
  content: |-
    $x \le 1$
  correct: true
- id: b
  content: |-
    $x < 2$
- id: c
  content: |-
    $1 \le x < 2$
- id: d
  content: |-
    $x \ge 1$
- id: e
  content: |-
    There is no solution.
```

---

**Question 5**

```quiz
type: radio
id: ma-51736
content: |-
  Which number line represents the solution to the following system of inequalities?
  ${4x \le 16; 3x + 5 \ge - 4$
options:
- id: a
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-51736-a-1.png>)
  correct: true
- id: b
  content: |-
    No solutions
- id: c
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-51736-a-4.png>)
- id: d
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-51736-a-2.png>)
- id: e
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-51736-a-3.png>)
```

---

**Question 6**

```quiz
type: radio
id: ma-25455
content: |-
  Which number line shows the solution of the following system of inequalities?
  ${7k + 18 \le - 3; 4k - 6 \ge 2$
options:
- id: a
  content: |-
    There is no solution
  correct: true
- id: b
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-25455-a-3.png>)
- id: c
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-25455-a-5.png>)
- id: d
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-25455-a-2.png>)
- id: e
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-25455-a-4.png>)
```

---

<a id="flipping-the-sign-of-an-inequality-in-a-system"></a>
## Flipping the Sign of an Inequality in a System

**Example:** What is the solution to the following system of inequalities?
${2 - 7x \ge 2; 10x - 3 \ge 7$

**Explanation**

To solve the system, we need to find the values of $x$ that satisfy both

$$
2-7x \geq 2
$$

and

$$
10x-3 \geq 7
$$

simultaneously.

- First, we solve $2-7x \geq 2$:
$\begin{bmatrix}2 - 7x & \ge 2 \\ 2 - 7x - 2 & \ge 2 - 2 \\ -7x & \ge 0 \\ (-1) \cdot (-7x) & \le (-1) \cdot 0 \\ 7x & \le 0 \\ \frac{7x}{7} & \le \frac{0}{7} \\ x & \le 0\end{bmatrix}$

![](<../Source/Compound AND Inequalities - 350/Images/0884f6ef95b762b67df4d43f303b59b4.png>)

- Then, we solve $10x-3 \geq 7$:
$\begin{bmatrix}10x - 3 & \ge 7 \\ 10x - 3 + 3 & \ge 7 + 3 \\ 10x & \ge 10 \\ \frac{10x}{10} & \ge \frac{10}{10} \\ x & \ge 1\end{bmatrix}$

![](<../Source/Compound AND Inequalities - 350/Images/7574b2bbe2aca4fbdc54f2fa8247bc74.png>)

To find the values of $x$ that satisfy both inequalities, we find where the two solutions overlap:

![](<../Source/Compound AND Inequalities - 350/Images/8df3636faeff77e8b0c0747ab3aa7474.png>)

It turns out that the solutions do not overlap at all. Therefore, no values of $x$ satisfy both inequalities simultaneously. So, there is no solution.

---

**Question 7**

```quiz
type: radio
id: ma-218794
content: |-
  What is the solution to the following system of inequalities?
  ${3y - 5 \le 4; 1 - 6y \le - 5$

  The solution is
options:
- id: a
  content: |-
    $1 \le y \le 3$
  correct: true
- id: b
  content: |-
    $y \le 3$
- id: c
  content: |-
    $y \ge 1$
- id: d
  content: |-
    $3 \le y \le 1$
- id: e
  content: |-
    There is no solution.
```

---

**Question 8**

```quiz
type: radio
id: ma-102305
content: |-
  Which number line represents the solution to the following system of inequalities?
  ${x + 2 \ge 2; 4 - x < 2$
options:
- id: a
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-102305-a-1.png>)
  correct: true
- id: b
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-102305-a-4.png>)
- id: c
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-102305-a-2.png>)
- id: d
  content: |-
    There is no solution
- id: e
  content: |-
    ![](<../Source/Compound AND Inequalities - 350/Images/q-102305-a-3.png>)
```

---

**Question 9:**

```quiz
type: radio
id: ma-59506
content: |-
  Find the set of values of $x$ that satisfy $6 - x > 7$ and $5x + 3 > 8$.
options:
- id: a
  content: |-
    There is no solution
  correct: true
- id: b
  content: |-
    $x ∈ (-2, 2)$
- id: c
  content: |-
    $x ∈ (1, ∞)$
- id: d
  content: |-
    $x ∈ (- ∞,-1)$
- id: e
  content: |-
    $x ∈ (-1, 1)$
```

---

<a id="systems-containing-compound-inequalities"></a>
## Systems Containing Compound Inequalities

**Example:** Find the set of values of $x$ that satisfy $1 \lt 3x-2 \leq 7$ and $2-3x \leq -4$.

**Explanation**

To solve compound "and" inequalities, we solve each inequality separately and then find their intersection.

- First, we solve $1 \lt 3x-2 \leq 7 \,$:
$\begin{bmatrix}1 & < 3x - 2 \le 7 \\ 1 + 2 & < 3x - 2 + 2 \le 7 + 2 \\ 3 & < 3x \le 9 \\ \frac{3}{3} & < \frac{3x}{3} \le \frac{9}{3} \\ 1 & < x \le 3\end{bmatrix}$

![](<../Source/Compound AND Inequalities - 350/Images/2884cabcbd2d62824f13bee340ceb456.png>)

- Then, we solve $2-3x \leq -4 \,$:
$\begin{bmatrix}2 - 3x & \le - 4 \\ 2 - 3x - 2 & \le - 4 - 2 \\ -3x & \le - 6 \\ (-1) \cdot (-3x) & \ge (-1) \cdot (-6) \\ 3x & \ge 6 \\ \frac{3x}{3} & \ge \frac{6}{3} \\ x & \ge 2\end{bmatrix}$

![](<../Source/Compound AND Inequalities - 350/Images/0a46b546c4a69d5765e1474ff4b8c430.png>)

To find the values of $x$ that satisfy both inequalities, we find where the two solutions overlap:

![](<../Source/Compound AND Inequalities - 350/Images/3e6987cb88b0209e3010a263dcaff3f1.png>)

Thus, the final solution is $x \in [2,3]$.

---

**Question 10:**

```quiz
type: radio
id: ma-156132
content: |-
  Find the set of values of $x$ that satisfy $3 < 1 + 2x \le 9$ and $2x - 1 > 3$.
options:
- id: a
  content: |-
    $[MATH: x ∈ (2, 4]]$
  correct: true
- id: b
  content: |-
    $x ∈ (- ∞, 2)$
- id: c
  content: |-
    $x ∈ (1, 2)$
- id: d
  content: |-
    $x ∈ (4, ∞)$
- id: e
  content: |-
    There is no solution
```

---

**Question 11**

```quiz
type: radio
id: ma-220299
content: |-
  Find the set of values of $x$ that satisfy $-1 \le 2 - x \le 3$ and $2x + 1 \ge 5$.
options:
- id: a
  content: |-
    $2 \le x \le 3$
  correct: true
- id: b
  content: |-
    $-1 \le x \le 3$
- id: c
  content: |-
    $x \ge 2$
- id: d
  content: |-
    $-1 \le x \le 2$
- id: e
  content: |-
    There is no solution.
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
