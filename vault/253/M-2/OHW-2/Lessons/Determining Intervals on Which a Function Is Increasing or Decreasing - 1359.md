# Determining Intervals on Which a Function Is Increasing or Decreasing

<!--
lesson-id: 1359
topic-code: MF3.8.2.6
-->

## Table of Contents

- [Introduction](#introduction)
- [Determining Intervals on Which the Derivative of a Graphed Function Is Positive or Negative](#determining-intervals-on-which-the-derivative-of-a-graphed-function-is-positive-or-negative)
- [Calculating Intervals on Which a Function Is Increasing or Decreasing Using Differentiation](#calculating-intervals-on-which-a-function-is-increasing-or-decreasing-using-differentiation)
- [Determining the Intervals on Which a Function Is Decreasing Using Differentiation](#determining-the-intervals-on-which-a-function-is-decreasing-using-differentiation)
- [Determining the Intervals on Which a Function Is Increasing Using Differentiation](#determining-the-intervals-on-which-a-function-is-increasing-using-differentiation)
- [Comparing Slopes of Functions at Different Points](#comparing-slopes-of-functions-at-different-points)

## Prerequisites

- [Using Differentiation to Calculate Critical Points](<8.2.5. Using Differentiation to Calculate Critical Points.md>)
- [Solving Polynomial Inequalities Using a Graphical Method](<../../../2. Inequalities/2.1. Single-Variable Inequalities/Lessons/2.1.7. Solving Polynomial Inequalities Using a Graphical Method.md>)
- [Solving Inequalities Involving Exponential Functions and Polynomials](<../../../2. Inequalities/2.1. Single-Variable Inequalities/Lessons/2.1.10. Solving Inequalities Involving Exponential Functions and Polynomials.md>)

---

<a id="introduction"></a>
## Introduction

Consider the graph of the continuous function $y=f(x)$ below. How can we determine the intervals where $f'(x)$ is positive or negative?

The first step is to identify the points where the derivative is zero. Here, the critical points are $x=2$ (a local maximum) and $x=4$ (a local minimum), and $f'(x) = 0$ at these points.

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/bfdeb0061b7eb2a8df91533ebecc242d.png>)

The next step is to identify where the the function is increasing and decreasing. Below, the intervals where $f(x)$ is increasing are shown in blue, and the intervals where $f(x)$ is decreasing are shown in green.

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/5de9d3b0831cd55746eafc4a9546a8a5.png>)

Since we know where the function is increasing or decreasing, we can determine where $f'(x)$ is positive or negative.

- When $f(x)$ is strictly increasing, the slopes of the tangent lines are positive, so we have $f'(x)>0$.
- When $f(x)$ is strictly decreasing, the slopes of the tangent lines are negative, so we have $f'(x)<0$.

The information about $f'(x)$ can be summarized in the following table:

$$
\begin{bmatrix}x & (- ∞, 2) & 2 & (2, 4) & 4 & (4, + ∞) \\ f & ↗ & max & ↘ & min & ↗ \\ f^{′} & + & 0 & - & 0 & +\end{bmatrix}
$$

In other words,

- $f'(x)>0$ on $(-\infty,2) \cup (4,+\infty)$, while
- $f'(x)<0$ on $(2,4)$.

---

<a id="determining-intervals-on-which-the-derivative-of-a-graphed-function-is-positive-or-negative"></a>
## Determining Intervals on Which the Derivative of a Graphed Function Is Positive or Negative

**Example:** The graph of the continuous function $y=f(x)$ is shown below. The points $A$ and $B$ lie on the curve and have $x$-coordinates $x=1$ and $x=4$. Given that $f'(x) = 0$ at both $A$ and $B$, find the intervals where $f'(x)>0$.

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/188a9a9a3d8e58ae595eacd0c7a3e567.png>)

**Explanation**

We have $f'(x)=0$ at the critical points $A$ and $B$. Note the following:

- If $f(x)$ is strictly increasing, then $f'(x)>0$.
- If $f(x)$ is strictly decreasing, then $f'(x)<0$.

The information about $f'(x)$ can be summarized in the following table:

$$
\begin{bmatrix}x & (- ∞, 1) & 1 & (1, 4) & 4 & (4, + ∞) \\ f & ↘ & min & ↗ & max & ↘ \\ f^{′} & - & 0 & + & 0 & -\end{bmatrix}
$$

Therefore, $f'(x)>0$ on the interval $(1,4)$.

---

**Question 1**

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/q-18227.png>)

The graph of the continuous function $y = f(x)$ is shown below. The points $A$ and $B$ lie on the curve and have $x$-coordinates $x = 0$ and $x = 2$. Given that $f^{′}(x) = 0$ at both $A$ and $B$, find the intervals where $f^{′}(x) < 0$.

- [ ] A. $(2, ∞)$ only
- [ ] B. $(0, 2)$
- [ ] C. $(- ∞, 0)$ and $(2, ∞)$ only
- [ ] D. $(- ∞, 0)$ only
- [ ] E. No interval exists where $f^{′}(x) < 0$

---

**Question 2**

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/q-16039.png>)

The graph of the continuous function $y = f(x)$ is shown above. The points $A$ and $B$ lie on the curve and have $x$-coordinates $x = 0$ and $x = 2$. Given that $f^{′}(x) = 0$ at both $A$ and $B$, find the intervals where $f^{′}(x) > 0$.

- [ ] A. $(- ∞, 0)$ and $(2, ∞)$
- [ ] B. $(- ∞, 0)$
- [ ] C. $(2, ∞)$
- [ ] D. No interval exists where $f^{′}(x) > 0$.
- [ ] E. $(0, 2)$

---

<a id="calculating-intervals-on-which-a-function-is-increasing-or-decreasing-using-differentiation"></a>
## Calculating Intervals on Which a Function Is Increasing or Decreasing Using Differentiation

To determine whether a function $f(x)$ is increasing or decreasing, we can calculate the derivative and then solve the appropriate inequality.

- To find where $f(x)$ is strictly increasing, we solve the inequality $f'(x)>0$.
- To find where $f(x)$ is strictly decreasing, we solve the inequality $f'(x) < 0$.

---

<a id="determining-the-intervals-on-which-a-function-is-decreasing-using-differentiation"></a>
## Determining the Intervals on Which a Function Is Decreasing Using Differentiation

**Example:** Find the values of $x$ for which the function $f(x) = x^3 + x^2 - 8x$ is strictly decreasing.

**Explanation**

To find where $f(x)$ is strictly decreasing, we need to solve the inequality $f'(x) < 0$.

Differentiating $f(x)$, we get

$$
\begin{aligned}
f^{′}(x) &= 3x^{2} + 2x - 8
\end{aligned}
$$

so we need to solve the inequality

$$
3x^{2} + 2x - 8 < 0
$$

The above inequality factors as

$$
3(x + 2)\left(x -\dfrac 4 3\right) < 0
$$

and the graph of

$$
y=3(x+2)\left(x -\dfrac 4 3\right)
$$

has roots at $x=-2$ and

$$
x=\dfrac 4 3
$$

as shown below.

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/75d6da8209635228de08be5e9bd44737.png>)

The graph is negative on the interval

$$
\left(-2, \dfrac{4}{3} \right)
$$

between the roots, so we conclude that $f'(x) < 0$ on the interval

$$
\left(-2, \dfrac{4}{3} \right)
$$

Therefore, $f(x)$ is strictly decreasing on the interval

$$
\left(-2, \dfrac{4}{3} \right)
$$

---

**Question 3:** Find the values of $x$ for which the function $f(x) = x^{3} - 3x + 2$ is strictly decreasing.

- [ ] A. $x ∈ (- ∞,-1)$
- [ ] B. $x ∈ (-3, 3)$
- [ ] C. $x ∈ (- ∞,-1)∪(1, ∞)$
- [ ] D. $x ∈ (-1, 1)$
- [ ] E. $x ∈ (1, ∞)$

---

**Question 4:** Given that $f(x) = 7x^{2} - 28x + 35$ is defined for $x ∈ (-7, 7)$, find the values of $x$ for which the function is strictly decreasing.

- [ ] A. $x ∈ (-7, 2)$
- [ ] B. $x ∈ (-2, 7)$
- [ ] C. $x ∈ (2, 7)$
- [ ] D. $x ∈ (-7,-2)$
- [ ] E. $x ∈ (-2, 2)$

---

<a id="determining-the-intervals-on-which-a-function-is-increasing-using-differentiation"></a>
## Determining the Intervals on Which a Function Is Increasing Using Differentiation

**Example:** Find the values of $x$ for which the function $f(x)=\dfrac{\ln{2x}}{x}$ (plotted below) is strictly increasing.

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/39ade411a2a5987fa7b7c2350ac26caf.png>)

**Explanation**

To find where $f(x)$ is strictly increasing, we need to solve the inequality $f'(x) > 0$.

Differentiating $f(x)$ using the quotient rule, we get

$$
\begin{aligned}
f^{′}(x) &= ((\frac{1}{x}) \cdot x - \ln (2x) \cdot 1)/(x^{2}) \\
&= \frac{1 - \ln 2x}{x^{2}}
\end{aligned}
$$

so we need to solve the inequality

$$
\dfrac{1-\ln{2x}}{x^2} > 0
$$

The denominator is always positive, so this reduces to

$$
1 - \ln 2x > 0⟹\ln 2x < 1
$$

Solving $\ln{2x} = 1$ gives the critical point

$$
2x = e\quad \Longrightarrow\quad x = \dfrac{1}{2}e
$$

From the graph, we see that this critical point is a maximum. We also see that the slope of the tangent lines is positive to the left of the critical point and negative to the right of the critical point.

We summarize this information in the following table:

$$
\begin{bmatrix}x & (0, \frac{1}{2}e) & \frac{1}{2}e & (\frac{1}{2}e, ∞) \\ f & ↗ & max & ↘ \\ f^{′} & + & 0 & -\end{bmatrix}
$$

Finally, we conclude that the function is strictly increasing on the interval

$$
\left(0,\frac 1 2 e\right)
$$

which can also be written as

$$
0 < x < \dfrac 1 2 e
$$

---

**Question 5:** Find the values of $x$ for which the function $f(x) = (x^{2} - 8)e^{x}$ is strictly increasing.

- [ ] A. $-2 < x < 4$
- [ ] B. $x < - 2$ and $x > 4$
- [ ] C. $-2 < x < 2$
- [ ] D. $-4 < x < 2$
- [ ] E. $x < - 4$ and $x > 2$

---

**Question 6:** Find the values of $x$ for which the function $f(x) = 6x^{2} - 9x + 5$ is strictly increasing.

- [ ] A. $x ∈ (- ∞, \frac{3}{4})$
- [ ] B. $x ∈ (- ∞, \frac{4}{3})$
- [ ] C. $x ∈ (-\frac{3}{4}, ∞)$
- [ ] D. $x ∈ (\frac{4}{3}, ∞)$
- [ ] E. $x ∈ (\frac{3}{4}, ∞)$

---

<a id="comparing-slopes-of-functions-at-different-points"></a>
## Comparing Slopes of Functions at Different Points

**Example:** Consider the graph of $y=f(x)$ below.

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/57462b1da853695603be9e97d89cb7a4.png>)

Which of the following statements is true?

1. $f'(2.5) < f'(1) < f'(-1)$
2. $f'(-1) < f'(1) < f'(2.5)$
3. $f'(1) < f'(-1) < f'(2.5)$

**Explanation**

From the graph, we see that

- the slope of the tangent at $x=-1$ is positive, so $f'(-1) > 0$.
- the slope of the tangent at $x=1$ is zero, so $f'(1) = 0$.
- the slope of the tangent at $x=2.5$ is negative, and so $f'(2.5) < 0$.

Therefore, only statement I is correct.

---

**Question 7**

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/q-49005.png>)

Given the graph of $y = f(x)$ above, which of the following statements is true?

- [ ] A. $f^{′}(-1) < f^{′}(1) < f^{′}(0)$
- [ ] B. $f^{′}(1) < f^{′}(-1) < f^{′}(0)$
- [ ] C. $f^{′}(0) < f^{′}(1) < f^{′}(-1)$
- [ ] D. $f^{′}(-1) < f^{′}(0) < f^{′}(1)$
- [ ] E. $f^{′}(0) < f^{′}(-1) < f^{′}(1)$

---

**Question 8**

![](<../Source/Determining Intervals on Which a Function Is Increasing or Decreasing - 1359/Images/q-48996.png>)

Consider the graph of $y = f(x)$ above. Which of the following statements is true?

- [ ] A. $f^{′}(0) < f^{′}(1) < f^{′}(3)$
- [ ] B. $f^{′}(1) < f^{′}(0) < f^{′}(3)$
- [ ] C. $f^{′}(3) < f^{′}(0) < f^{′}(1)$
- [ ] D. $f^{′}(0) < f^{′}(3) < f^{′}(1)$
- [ ] E. $f^{′}(1) < f^{′}(3) < f^{′}(0)$

```update-progress
```

[[MA/Mathematical-Foundations/MF3/Home|Home]]
[[MA/Mathematical-Foundations/MF3/0. Table of Contents/TOC|Table of Contents]]
