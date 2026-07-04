# Solving Inequalities Involving Positive and Negative Factors

<!--
lesson-id: 2982
topic-code: MF3.2.1.5
-->

## Table of Contents

- [Introduction](#introduction)
- [Solving Inequalities Requiring Multiplication by a Positive Factor](#solving-inequalities-requiring-multiplication-by-a-positive-factor)
- [Solving Inequalities Requiring Division by a Positive Factor](#solving-inequalities-requiring-division-by-a-positive-factor)
- [Multiplying or Dividing by a Negative Factor](#multiplying-or-dividing-by-a-negative-factor)
- [Solving Inequalities Requiring Multiplication or Division by a Negative Factor](#solving-inequalities-requiring-multiplication-or-division-by-a-negative-factor)
- [Solving Inequalities Involving Domain Restrictions](#solving-inequalities-involving-domain-restrictions)

## Prerequisites

- [Compound AND Inequalities](<../../../../AG1/1. Equations & Inequalities/1.3. Linear Inequalities/Lessons/1.3.7. Compound AND Inequalities.md>)
- [Properties of Transformed Exponential Functions](<../../../../AG2/4. Exponentials & Logarithms/4.5. Graphs of Exponential Functions/Lessons/4.5.6. Properties of Transformed Exponential Functions.md>)
- [Properties of Transformed Logarithmic Functions](<../../../../AG2/4. Exponentials & Logarithms/4.6. Graphs of Logarithmic Functions/Lessons/4.6.3. Properties of Transformed Logarithmic Functions.md>)
- [Properties of Transformed Sine and Cosine Functions](<../../../../AG2/9. Trigonometric Functions/9.4. Properties of Transformed Trigonometric Functions/Lessons/9.4.1. Properties of Transformed Sine and Cosine Functions.md>)

---

<a id="introduction"></a>
## Introduction

Given an inequality, we're allowed to multiply or divide both sides by an expression if we know that the expression is always positive.

For example, suppose we want to solve the inequality

$$
\dfrac{x}{1+x^2} < 0
$$

We know that the denominator $1+x^2$ is positive for all values of $x$. So, we can multiply both sides of the inequality by $1+x^2$ as follows:

$$
\begin{bmatrix}\frac{x}{1 + x^{2}} & < 0 \\ (1 + x^{2}) \cdot \frac{x}{1 + x^{2}} & < (1 + x^{2}) \cdot 0 \\ (1 + x^{2}) \cdot \frac{x}{1 + x^{2}} & < 0 \\ x & < 0\end{bmatrix}
$$

Therefore, the solution to the inequality is $x<0$.

---

<a id="solving-inequalities-requiring-multiplication-by-a-positive-factor"></a>
## Solving Inequalities Requiring Multiplication by a Positive Factor

**Example:** Solve the inequality
$\dfrac{2}{5x^4 +2} \lt \dfrac{5-2x}{5x^4+2}$.

**Explanation**

We know that the denominator $5x^4+ 2$ is positive for all values of $x$. So, we can multiply both sides of the inequality by $5x^4+2$ and solve the resulting inequality as follows:

$$
\begin{bmatrix}\frac{2}{5x^{4} + 2} & < \frac{5 - 2x}{5x^{4} + 2} \\ (5x^{4} + 2) \cdot \frac{2}{5x^{4} + 2} & < (5x^{4} + 2) \cdot \frac{5 - 2x}{5x^{4} + 2} \\ 2 & < 5 - 2x \\ 2x & < 3 \\ x & < \frac{3}{2}\end{bmatrix}
$$

---

**Question 1:** Solve the inequality
$\frac{6 - 2x}{3^{x} + 4^{x}} > \frac{8}{3^{x} + 4^{x}}$.

- [ ] A. $x > 1$
- [ ] B. No solution
- [ ] C. $x > 0$
- [ ] D. $x < - 1$
- [ ] E. $x < 0$

---

**Question 2:** Solve the inequality
$\frac{1 - 4x}{\sin x + 4} \ge \frac{x + 5}{\sin x + 4}$.

- [ ] A. $x \ge 2$
- [ ] B. $x \ge - 4$
- [ ] C. $x \le \frac{1}{2}$
- [ ] D. $x \le - \frac{4}{5}$
- [ ] E. $x \le 5$

---

<a id="solving-inequalities-requiring-division-by-a-positive-factor"></a>
## Solving Inequalities Requiring Division by a Positive Factor

**Example:** Solve the inequality
$6x^3 + 3x \lt 0$.

**Explanation**

First, we factor:

$$
\begin{bmatrix}6x^{3} + 3x & < 0. \\ 3x(2x^{2} + 1) & < 0\end{bmatrix}
$$

Since $2x^2 + 1$ is always positive, we can divide both sides of the inequality by this quantity. By doing this, we get

$$
\begin{bmatrix}(3x(2x^{2} + 1))/(2x^{2} + 1) & < \frac{0}{2x^{2} + 1} \\ 3x & < 0 \\ x & < 0\end{bmatrix}
$$

---

**Question 3:** Solve the inequality
$7x + x\sin x \le 5x$.

- [ ] A. $x \le 0$
- [ ] B. $0 \le x \le π$
- [ ] C. $x \le π$
- [ ] D. $x \ge 2$
- [ ] E. $x \ge 0$

---

**Question 4:** Solve the inequality
$4xe^{2x} - 5e^{2x} \le 0$.

- [ ] A. $x \le 4$
- [ ] B. $x \ge \frac{2}{5}$
- [ ] C. $x \le 5$
- [ ] D. $x \ge 0$
- [ ] E. $x \le \frac{5}{4}$

---

<a id="multiplying-or-dividing-by-a-negative-factor"></a>
## Multiplying or Dividing by a Negative Factor

Given an inequality, we're also allowed to multiply or divide both sides by an expression if we know that the expression is always *negative*.

The only catch is that we have to remember to flip the sign of the inequality, like we normally do when multiplying or dividing both sides by a negative number.

For example, suppose that we have the inequality

$$
\dfrac{x}{-2-x^2} > 0
$$

We know that the denominator $-2-x^2$ is negative for all values of $x$. So, we can multiply both sides of the inequality by $-2-x^2$, provided that we flip the sign of the inequality:

$$
\begin{bmatrix}\frac{x}{-2 - x^{2}} & > 0 \\ (-2 - x^{2}) \cdot \frac{x}{-2 - x^{2}} & < (-2 - x^{2}) \cdot 0 \\ (-2 - x^{2}) \cdot \frac{x}{-2 - x^{2}} & < (-2 - x^{2}) \cdot 0 \\ x & < 0\end{bmatrix}
$$

---

<a id="solving-inequalities-requiring-multiplication-or-division-by-a-negative-factor"></a>
## Solving Inequalities Requiring Multiplication or Division by a Negative Factor

**Example:** Solve the inequality
$(2\sin{x}-9)(2x) \leq 0$.

**Explanation**

Note that the factor $2\sin{x}-9$ is always negative. We know this because

$$
-1 \leq \sin x \leq 1 \quad \Rightarrow \quad -11 \leq 2\sin x - 9 \leq -7
$$

Because $2\sin{x}-9$ is always negative, we can divide both sides of the inequality by this quantity, but we have to remember to flip the sign of the inequality. By doing this, we get

$$
\begin{bmatrix}(2\sin x - 9)(2x) & \le 0 \\ ((2\sin x - 9)(2x))/(2\sin x - 9) & \ge \frac{0}{2\sin x - 9} \\ 2x & \ge 0 \\ x & \ge 0\end{bmatrix}
$$

---

**Question 5:** Solve the inequality
$(3 + x)(\cos x - 4) < 0$.

- [ ] A. $x > 4$
- [ ] B. $x < 0$
- [ ] C. $x < - 4$
- [ ] D. $x < - 3$
- [ ] E. $x > - 3$

---

**Question 6:** Solve the inequality
$(-1 - e^{x})(4x - 1) \le 0$.

- [ ] A. $x \ge - \frac{1}{2}$
- [ ] B. $x \ge \frac{1}{4}$
- [ ] C. $x > - 2$
- [ ] D. $x \le \frac{1}{4}$
- [ ] E. $x \le 4$

---

<a id="solving-inequalities-involving-domain-restrictions"></a>
## Solving Inequalities Involving Domain Restrictions

**Example:** Solve the inequality

$\dfrac{x+5}{1-3x} \lt 2, \quad x \lt 0$.

**Explanation**

Since $x\lt 0$, we have that
$\begin{bmatrix}x & < 0 \\ -x & > 0 \\ -3x & > 0 \\ 1 - 3x & > 1\end{bmatrix}$.

This means that $1-3x$ is positive for all the values of $x$ that we are considering $(x\lt 0)$. So, we can multiply both sides by $1-3x$, and solve the resulting inequality as follows:

$$
\begin{bmatrix}\frac{x + 5}{1 - 3x} & < 2 \\ (1 - 3x) \cdot \frac{x + 5}{1 - 3x} & < (1 - 3x) \cdot 2 \\ x + 5 & < 2 - 6x \\ 7x & < - 3 \\ x & < - \frac{3}{7}\end{bmatrix}
$$

Therefore, the solution to the inequality will be the numbers that satisfy both $x \lt 0$ and

$$
x \lt -\dfrac{3}{7}
$$

So, the solution to our inequality is

$$
x \lt -\dfrac{3}{7}
$$

---

**Question 7**

Solve the inequality

$\frac{3x + 2}{1 - x} > 4, x > 2$.

- [ ] A. $x > 2$
- [ ] B. No solution
- [ ] C. $x > \frac{7}{2}$
- [ ] D. $2 < x < 6$
- [ ] E. $2 < x < \frac{5}{2}$

---

**Question 8**

Solve the inequality

$(2x - 3)/(\ln (x - 2)) \ge 0, x > 3$.

- [ ] A. $3 < x < 4$
- [ ] B. $x > 3$
- [ ] C. $x \ge \frac{7}{2}$
- [ ] D. $x \ge 5$
- [ ] E. $3 < x < \frac{7}{2}$

```update-progress
```

[[MA/MF3/Home|Home]]
[[MA/MF3/0. Table of Contents/TOC|Table of Contents]]
