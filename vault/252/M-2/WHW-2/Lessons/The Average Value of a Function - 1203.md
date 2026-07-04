# The Average Value of a Function

<!--
lesson-id: 1203
topic-code: MF3.9.5.1
-->

## Table of Contents

- [Introduction](#introduction)
- [Finding Points That Satisfy the Mean Value Theorem for Integrals](#finding-points-that-satisfy-the-mean-value-theorem-for-integrals)
- [The Average Value of a Function](#the-average-value-of-a-function)
- [Finding the Average Value of a Function Over a Given Interval](#finding-the-average-value-of-a-function-over-a-given-interval)
- [Finding an Interval Given the Average Value of a Function](#finding-an-interval-given-the-average-value-of-a-function)
- [Finding the Average Value of a Function Given a Graph](#finding-the-average-value-of-a-function-given-a-graph)

## Prerequisites

- [Integrating Trigonometric Functions Using Substitution](<../../../10. Integration Techniques/10.1. Integration Using Substitution/Lessons/10.1.8. Integrating Trigonometric Functions Using Substitution.md>)
- [Calculating the Definite Integral of a Function Given Its Graph](<../../9.3. The Area Under a Curve/Lessons/9.3.5. Calculating the Definite Integral of a Function Given Its Graph.md>)

---

<a id="introduction"></a>
## Introduction

The region $\textrm{R}$, shown below is the area under the graph of

$$
f(x) = 2x+1
$$

over the interval $[1,3]$. What is the height of the rectangle defined over the same interval that has the same area as $\textrm{R}$?

![](<../Source/The Average Value of a Function - 1203/Images/fa186517f28f573b19724be8be817f35.png>)

Using the formula for the area of a trapezoid, we have that

$$
\begin{aligned} \textrm{Area}\,(\textrm{R}) = \dfrac{1}{2}(3+7)(3-1)= 10. \end{aligned}
$$

For the rectangle to have the same area, we must have

$$
\begin{aligned}
10 &= f(c)(3 - 1) \\
f(c) &= 5 \\
2c + 1 &= 5 \\
c &= 2
\end{aligned}
$$

We can summarize what we've just done by saying that

$$
\int_1^3 (2x +1)\, \textrm d x= f(2) \cdot (3-1)
$$

This is an example of the **mean value theorem for integrals**, which states:

> *If $f(x)$ is a continuous function on the closed interval $[a, b]$, then there exists a number $c$ in that interval such that*
> $\int_a^b f(x)\, \textrm d x = f(c) \cdot (b-a)$.

---

<a id="finding-points-that-satisfy-the-mean-value-theorem-for-integrals"></a>
## Finding Points That Satisfy the Mean Value Theorem for Integrals

**Example:** Find the values of $c$ that satisfy the mean value theorem for integrals for $f(x) = x^2-2x+2$ on the interval $[0,3]$.

**Explanation**

Applying the mean value theorem for integrals, we have

$$
\begin{aligned} f(c) (b-a) & = \int_a^b f(x) \, \textrm dx \\[5pt] f(c) & = \dfrac {1}{b-a} \int_a^b f(x) \, \textrm dx \\[5pt] & = \dfrac {1}{3-0} \int_0^3 (x^2-2x+2) \, \textrm dx \\[5pt] & = \left. \dfrac {1}{3} \cdot \left[\dfrac{x^3}{3} -x^2 +2x\right] \right|_0^3 \\[5pt] & = \dfrac {1}{3} \cdot \left[ \left(\dfrac{3^3}{3} -3^2 +2\cdot3\right) - \left(\dfrac{0^3}{3} -0^2 +2\cdot0\right)\right] \\[5pt] & = \dfrac {1}{3}\cdot6 \\[5pt] & = 2. \end{aligned}
$$

Now, we use the expression for $f(x)$ to solve for the value of $c$:

$$
\begin{aligned}
f(c) &= 2 \\
c^{2} - 2c + 2 &= 2 \\
c(c - 2) &= 0 \\
c &= 0, 2
\end{aligned}
$$

---

**Question 1:** Find the value of $c$ that satisfies the mean value theorem for integrals for $f(x) = 1 - x^{2}$ on the interval $[0, 3]$.

- [ ] A. $\sqrt{2}$
- [ ] B. $\frac{1}{2}$
- [ ] C. $\frac{1}{3}$
- [ ] D. $2$
- [ ] E. $\sqrt{3}$

---

**Question 2**

Find the **exact** value of $c$ that satisfies the mean value theorem for integrals for $f(x) = x^{3} - 3x^{2} + 4$ on the interval $[0, 2]$.$c =$
$\underline{\hspace{1.5cm}}$

---

**Question 3:** Find all values of $c$ that satisfy the mean value theorem for integrals for $f(x) = 3x^{2}$ on the interval $[- 2, 2]$.

- [ ] A. $-\frac{2}{\sqrt{3}}$
- [ ] B. $± \frac{2}{\sqrt{3}}$
- [ ] C. $\sqrt{\frac{2}{3}}$
- [ ] D. $2\sqrt{2}$
- [ ] E. $\frac{2}{\sqrt{3}}$

---

<a id="the-average-value-of-a-function"></a>
## The Average Value of a Function

The **average value** of a continuous function on a closed interval $[a,b]$ is given by

$$
f_\textrm{avg} = \dfrac{1}{b-a}\int_a^b f(x) \: \textrm{d}x
$$

---

<a id="finding-the-average-value-of-a-function-over-a-given-interval"></a>
## Finding the Average Value of a Function Over a Given Interval

**Example:** Find the average value of the function $f(x) = x - 2$ on the interval $[-2, 4]$.

**Explanation**

Applying the average value formula, we find that the average value of the function is

$$
\begin{aligned}
f_{avg} &= \frac{1}{b - a}∫_{a}^{b}f(x)dx \\
&= (1)/(4 - (-2))∫_{-2}^{4}x - 2dx \\
&= \frac{1}{6}(\frac{x^{2}}{2} - 2x) \mid _{-2}^{4} \\
&= \frac{1}{6}[(\frac{4^{2}}{2} - 2(4)) - (((-2)^{2})/(2) - 2(-2))] \\
&= \frac{1}{6}[(8 - 8) - (2 + 4)] \\
&= \frac{1}{6}(0 - 6) \\
&=-1
\end{aligned}
$$

---

**Question 4**

> A scientific calculator is required to answer this question.

Find the average value of the function $f(x) = 1 + x^{2}$ on the interval $[- 1, 2]$.

- [ ] A. $2$
- [ ] B. $0$
- [ ] C. $-\frac{1}{2}$
- [ ] D. $\frac{1}{4}$
- [ ] E. $1$

---

**Question 5**

> A scientific calculator is required to answer this question.

What is the average value of $h(x) = \sin 2x$ on the interval $[\frac{π}{4}, \frac{π}{2}]$?

- [ ] A. $\frac{1}{2π}$
- [ ] B. $-\frac{1}{2π}$
- [ ] C. $\frac{2}{π}$
- [ ] D. $-\frac{2}{π}$
- [ ] E. $0$

---

<a id="finding-an-interval-given-the-average-value-of-a-function"></a>
## Finding an Interval Given the Average Value of a Function

**Example:** Find $c$ such that the average value of $g(x) = 3 x$ on the interval $[0,c]$ is equal to $3$.

**Explanation**

To solve for $c$, we apply the average value formula:

$$
\begin{aligned}
g_{avg} &= \frac{1}{b - a}∫_{a}^{b}g(x)dx \\
3 &= \frac{1}{c - 0}∫_{0}^{c}3xdx \\
3 &= \frac{1}{c}(\frac{3x^{2}}{2}) \mid _{0}^{c} \\
3 &= \frac{1}{c}(\frac{3c^{2}}{2} - 0) \\
3 &= \frac{3c}{2} \\
c &= 2
\end{aligned}
$$

---

**Question 6:** Find $c$ such that the average value of $h(x) = 5x - 8$ on the interval $[0, c]$ is equal to $-3$.

- [ ] A. $\frac{5}{2}$
- [ ] B. $2$
- [ ] C. $\frac{3}{2}$
- [ ] D. $1$
- [ ] E. $3$

---

**Question 7:** Find the number $c > 0$ such that the average value of $f(x) = 9 + 8x - 3x^{2}$ on the interval $[0, c]$ is equal to $-3$.

- [ ] A. $5$
- [ ] B. $4$
- [ ] C. $6$
- [ ] D. $2$
- [ ] E. $7$

---

<a id="finding-the-average-value-of-a-function-given-a-graph"></a>
## Finding the Average Value of a Function Given a Graph

**Example:** The graph of the function $f(x)$, which is defined on $[1,6]$, is shown below. The areas of the regions between the graph and the $x$-axis are $5$ and $2$, respectively (from left to right). Find the average value of $f(x)$ on $[1,6]$.

![](<../Source/The Average Value of a Function - 1203/Images/348b67f3907c98dd642975d127a3ea0a.png>)

**Explanation**

The average value of a function on a given interval is

$$
f_\textrm{avg} = \dfrac{1}{b-a}\int_a^b f(x) \: \textrm{d}x
$$

Here, we see that

$$
\int_{1}^{6} f(x)\: \textrm{d}x = -5 + 2 = -3
$$

So, applying the average value formula, we find that the average value is

$$
\begin{aligned}
f_{avg} &= \frac{1}{b - a}∫_{a}^{b}f(x)dx \\
&= \frac{1}{6 - 1} \cdot (-3) \\
&=-\frac{3}{5}
\end{aligned}
$$

---

**Question 8**

![](<../Source/The Average Value of a Function - 1203/Images/q-15993.png>)

The graph of the function $f(x)$, which is defined on $[- 5, 4]$, is shown above. The areas of the regions between the graph and the $x$-axis are $22$ and $5$, respectively (from left to right). Find the average value of $f(x)$ on $[- 5, 4]$.

- [ ] A. $\frac{1}{9}$
- [ ] B. $8$
- [ ] C. $\frac{17}{9}$
- [ ] D. $3$
- [ ] E. $27$

---

**Question 9**

![](<../Source/The Average Value of a Function - 1203/Images/q-18144.png>)

The graph of the function $f(x)$, which is defined on $[- 3, 6]$, is shown above. The areas of the regions between the graph and the $x$-axis are $40$, $20$ and $10$, respectively (from left to right). Find the average value of $f(x)$ on $[- 3, 6]$.

- [ ] A. $\frac{10}{3}$
- [ ] B. $\frac{5}{3}$
- [ ] C. $\frac{2}{3}$
- [ ] D. $\frac{1}{3}$
- [ ] E. $\frac{7}{3}$

```update-progress
```

[[MA/MF3/Home|Home]]
[[MA/MF3/0. Table of Contents/TOC|Table of Contents]]
