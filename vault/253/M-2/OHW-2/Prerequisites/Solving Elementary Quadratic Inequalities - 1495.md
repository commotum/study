# Solving Elementary Quadratic Inequalities

<!--
lesson-id: 1495
topic-code: MF3.2.1.1
-->

## Table of Contents

- [Introduction](#introduction)
- [Solving an Elementary Quadratic Inequality Using the Graphical Method](#solving-an-elementary-quadratic-inequality-using-the-graphical-method)
- [Solving an Elementary Quadratic Inequality Using the Absolute Value Method](#solving-an-elementary-quadratic-inequality-using-the-absolute-value-method)
- [Solving an Elementary Quadratic Inequality Using the Absolute Value Method](#solving-an-elementary-quadratic-inequality-using-the-absolute-value-method)
- [Solving an Elementary Quadratic Inequality by Manipulating the Inequality First](#solving-an-elementary-quadratic-inequality-by-manipulating-the-inequality-first)
- [Solving Elementary Quadratic Inequalities with No Solutions or All Real Solutions](#solving-elementary-quadratic-inequalities-with-no-solutions-or-all-real-solutions)
- [Elementary Quadratic Inequalities with No Solutions or All Real Solutions](#elementary-quadratic-inequalities-with-no-solutions-or-all-real-solutions)

## Prerequisites

- [Solving Quadratic Equations Using a Difference of Squares](<../../../../AG1/10. Quadratic Equations & Functions/10.1. Quadratic Equations/Lessons/10.1.5. Solving Quadratic Equations Using a Difference of Squares.md>)
- [Absolute Value Inequalities](<../../../../AG1/7. Absolute Value/7.1. Absolute Value Expressions, Equations & Inequalities/Lessons/7.1.8. Absolute Value Inequalities.md>)
- [Roots of Quadratic Functions](<../../../../AG1/10. Quadratic Equations & Functions/10.2. Quadratic Functions/Lessons/10.2.4. Roots of Quadratic Functions.md>)
- [Rationalizing Denominators](<../../../../PAL/3. Exponents & Radicals/3.5. Radicals/Lessons/3.5.8. Rationalizing Denominators.md>)

---

<a id="introduction"></a>
## Introduction

Suppose we need to solve the inequality

$$
x^2\geq 4
$$

Let's start by bringing all the terms to the left-hand side, so

$$
x^{2} - 4 \mid \ge 0
$$

Now, we consider the corresponding parabola given by $y = x^2-4$ and find its roots, as follows:

$$
\begin{aligned}
x^{2} - 4 &= 0 \\
x^{2} - 2^{2} &= 0 \\
(x - 2)(x + 2) &= 0
\end{aligned}
$$

So the roots are $x= \pm2$.

Solving the inequality

$$
x^2-4 \geq 0
$$

is equivalent to finding the values of $x$ for which the parabola $y=x^2-4$ is above or on the $x$-axis (where

$$
{\color{red}y \ge 0}
$$

).

Since the leading coefficient of $x^2-4$ is positive, the parabola opens upward (like $\smile$). Therefore, the solution set lies outside the roots (and includes the roots), as shown below.

![](<../Source/Solving Elementary Quadratic Inequalities - 1495/Images/830a9a66ccb717ab8b690993b7cf1d73.png>)

So, the solution to the initial inequality is $[MATH: x \in {\color{blue}(-\infty, -2] \cup [2, +\infty)}.]$

---

<a id="solving-an-elementary-quadratic-inequality-using-the-graphical-method"></a>
## Solving an Elementary Quadratic Inequality Using the Graphical Method

**Example:** Solve the inequality $x^2< 1$ using a graphical method.

**Explanation**

Bringing all the terms to the left-hand side, we have
$\begin{bmatrix}x^{2} & < 1 \\ x^{2} - 1 & < 0\end{bmatrix}$.

Now, we consider the corresponding parabola given by $y = x^2-1$ and find its roots:

$$
\begin{aligned}
x^{2} - 1 &= 0 \\
x^{2} - 1^{2} &= 0 \\
(x - 1)(x + 1) &= 0
\end{aligned}
$$

So the roots are $x= \pm 1$.

Solving the inequality $x^2-1 < 0$ is equivalent to finding the values of $x$ for which the parabola $y=x^2-1$ is below the $x$-axis (where ${\color{red}y < 0}$).

Since the leading coefficient of the quadratic expression is positive, the parabola opens upward. Therefore, the solution set lies between the roots (but it does not include them), as shown below.

![](<../Source/Solving Elementary Quadratic Inequalities - 1495/Images/c6466800210c6322a6a2ffd68100400b.png>)

Therefore, the solution is $x \in {\color{blue}(-1, 1)}$.

---

**Question 1:** Solve the inequality $x^{2} > 9$ using a graphical method.

- [ ] A. $x ∈ (- ∞,-9)∪(9, ∞)$
- [ ] B. $x ∈ (- ∞,-3)∩(1, ∞)$
- [ ] C. $x ∈ (- ∞,-3)∪(3, ∞)$
- [ ] D. $x ∈ (- ∞, ∞)$
- [ ] E. $x ∈ (- ∞,-3)$

---

**Question 2:** Solve the inequality $x^{2} < 4$ using a graphical method.

- [ ] A. $(- ∞,-2)∪(2, ∞)$
- [ ] B. $x ∈ (-4, 4)$
- [ ] C. $x ∈ (-2, 2)$
- [ ] D. $x ∈ (- ∞,-2)$
- [ ] E. $x ∈ (- ∞, ∞)$

---

<a id="solving-an-elementary-quadratic-inequality-using-the-absolute-value-method"></a>
## Solving an Elementary Quadratic Inequality Using the Absolute Value Method

We can also solve quadratic inequalities by reducing them to absolute value expressions.

For example, to solve the inequality $x^2 > 1$, we can start by taking the square root of both sides of the inequality:

$$
x^{2}\begin{vmatrix}> 1 \\ \sqrt{x^{2}}\end{vmatrix}> \sqrt{1}; \mid x \mid \mid > 1
$$

Using the definition of absolute value, we must have $x>1$ or $x<-1$.

So, the solution is $x \in (-\infty, -1) \cup (1,\infty)$.

**Remember:** For any number $a$ that is zero or positive,

- the equation $\mid x \mid < a$ has the solution $-a < x < a$,
- the equation $\mid x \mid \leq a$ has the solution $-a \leq x \leq a$,
- the equation $\mid x \mid > a$ has the solution $x > a$ or $x < -a$, and
- the equation $\mid x \mid \geq a$ has the solution $x \geq a$ or $x \leq -a$.

---

<a id="solving-an-elementary-quadratic-inequality-using-the-absolute-value-method"></a>
## Solving an Elementary Quadratic Inequality Using the Absolute Value Method

**Example:** Solve the inequality $x^2 \leq 2$ using the absolute value method.

**Explanation**

Taking the square root of both sides of the inequality, we get

$$
x^{2}\begin{vmatrix}\le 2 \\ \sqrt{x^{2}}\end{vmatrix}\le \sqrt{2}; \mid x \mid \mid \le \sqrt{2}
$$

Now, using the definition of absolute value, we must have

$$
-\sqrt 2\leq x \leq \sqrt 2
$$

Therefore, the solution is $x \in [-\sqrt 2,\sqrt 2]$.

---

**Question 3:** Solve the inequality $x^{2} \ge 1$ using the absolute value method.

- [ ] A. $x ∈ (- ∞, ∞)$
- [ ] B. $[MATH: x ∈ (- ∞, 1]]$
- [ ] C. $[MATH: x ∈ (- ∞,-1]∪[1, ∞)]$
- [ ] D. $x ∈ [- 1, 1]$
- [ ] E. $[MATH: x ∈ [- 1, ∞)]$

---

**Question 4:** Solve the inequality $x^{2} - 3 > 0$ using the absolute value method.

- [ ] A. $x ∈ (- ∞, ∞)$
- [ ] B. $x ∈ (- ∞,-\sqrt{3})$
- [ ] C. $x ∈ (- ∞,-\sqrt{3})∪(\sqrt{3}, ∞)$
- [ ] D. $x ∈ (- ∞,-3)∪(3, ∞)$
- [ ] E. $x ∈ (-\sqrt{3}, \sqrt{3})$

---

<a id="solving-an-elementary-quadratic-inequality-by-manipulating-the-inequality-first"></a>
## Solving an Elementary Quadratic Inequality by Manipulating the Inequality First

**Example:** Solve $3x^2-6 > 3+2x^2$.

**Explanation**

First, let's simplify the inequality:

$$
\begin{bmatrix}3x^{2} - 6 & > 3 + 2x^{2} \\ 3x^{2} - 2x^{2} & > 6 + 3 \\ x^{2} & > 9\end{bmatrix}
$$

Now, we can use either of two methods to solve the inequality.

*Method 1 - Solving an Absolute Value Equation*

Taking the square root of both sides of the inequality, we get

$$
\sqrt{x^{2}} \mid > \sqrt{9}; \mid x \mid \mid > 3
$$

Now, using the definition of absolute value, we must have $x>3$ or $x<-3$.

So, the solution is $x \in (-\infty,-3)\cup(3,+\infty)$.

*Method 2 - Picturing a Quadratic Curve*

Starting from $x^2>9$ and moving all terms to the left-hand side, we reach

$$
x^2-9 > 0
$$

Now, we consider the corresponding parabola given by $y=x^2-9$ and find its roots:

$$
\begin{aligned}
x^{2} - 9 &= 0 \\
(x + 3)(x - 3) &= 0
\end{aligned}
$$

So the roots are $x=\pm 3$.

Since the leading coefficient of $x^2-9$ is positive, the parabola opens upward. Therefore, the solution to the given inequality ($y>0$) lies outside of the roots (but does not include them).

![](<../Source/Solving Elementary Quadratic Inequalities - 1495/Images/ab45329cb4ffe9bd9528e09a8398de8f.png>)

Therefore, the solution is $x \in (-\infty,-3)\cup(3,+\infty)$.

---

**Question 5:** Solve $4x^{2} > 9$.

- [ ] A. $x ∈ (∞,-\frac{3}{2})∩(-\frac{9}{2}, ∞)$
- [ ] B. $x ∈ (- ∞,-\frac{3}{2})∪(\frac{3}{2}, ∞)$
- [ ] C. $x ∈ (- ∞,-\frac{1}{2})∪(\frac{1}{2}, ∞)$
- [ ] D. $x ∈ (- ∞,-\frac{9}{4})∪(\frac{9}{4}, ∞)$
- [ ] E. $x ∈ (\frac{9}{4}, ∞)$

---

**Question 6:** Solve $5x^{2} - 3 \le 3 - 4x^{2}$.

- [ ] A. $x ∈ [- \frac{2}{3}, \frac{2}{3}]$
- [ ] B. $[MATH: x ∈ [- \frac{2}{3}, ∞)]$
- [ ] C. $[MATH: x ∈ (- ∞,-\sqrt{\frac{2}{3}}]∪[\sqrt{\frac{2}{3}}, ∞)]$
- [ ] D. $[MATH: x ∈ (- ∞, \frac{2}{3}]]$
- [ ] E. $x ∈ [- \sqrt{\frac{2}{3}}, \sqrt{\frac{2}{3}}]$

---

<a id="solving-elementary-quadratic-inequalities-with-no-solutions-or-all-real-solutions"></a>
## Solving Elementary Quadratic Inequalities with No Solutions or All Real Solutions

Let's consider the inequality

$$
x^2 \geq -4
$$

We can solve this equation using either of the two methods that we've learned.

- **Method 1:** Solving an Absolute Value InequalityWe know that the square of *any* real number is greater than or equal to zero. Therefore, the square of any real number is also greater than or equal to $-4$, since $x^2 \geq 0 > -4$.Therefore, *any* real number will satisfy the inequality $x^2 \geq -4$. So, we conclude that the solution to the inequality is $x\in(-\infty,\infty)$.

- **Method 2:** Picturing a Quadratic CurveLet's bring all the terms to the left-hand side,
$x^2+4 \geq 0$,
and then plot the parabola $y = x^2+4$. The desired inequality ($y \geq 0$) is always satisfied, so the solution is $x \in (-\infty, \infty)$.

![](<../Source/Solving Elementary Quadratic Inequalities - 1495/Images/e5d17694700d6b30c54f9da0317b4bf1.png>)

---

<a id="elementary-quadratic-inequalities-with-no-solutions-or-all-real-solutions"></a>
## Elementary Quadratic Inequalities with No Solutions or All Real Solutions

**Example:** Solve the inequality $x^2< -9$.

**Explanation**

We can solve this equation using either of the two methods that we've learned.

*Method 1 - Solving an Absolute Value Inequality*

We know that the square of *any* real number is greater than or equal to zero. Therefore, it is impossible for the square of a real number to be smaller than $-9$.

So, the inequality $x^2 < -9$ has no solutions.

*Method 2 - Picturing a Quadratic Curve*

Let's bring all the terms to the left-hand side,
$x^2+9 < 0$,
and then plot the parabola

$$
y=x^2+9
$$

The desired inequality ($y<0$) is never satisfied, so there are no solutions.

![](<../Source/Solving Elementary Quadratic Inequalities - 1495/Images/d1adac9838271ebb5335c01219ac7c41.png>)

---

**Question 7:** Solve the inequality $x^{2} < - \sqrt{2}$.

- [ ] A. $-2 < x < 2$
- [ ] B. The inequality has no solution
- [ ] C. $-\sqrt{2} < x < \sqrt{2}$
- [ ] D. $x ∈ (- ∞, \sqrt{2})$
- [ ] E. $0 < x < 2$

---

**Question 8:** Solve the inequality $-x^{2} \le 9$.

- [ ] A. $x ∈ [- 3, 3]$
- [ ] B. $[MATH: x ∈ (- ∞, 3]]$
- [ ] C. $x ∈ (- ∞, ∞)$
- [ ] D. $[MATH: x ∈ [- 3, ∞)]$
- [ ] E. $[MATH: x ∈ [3, ∞)]$

```update-progress
```

[[MA/Mathematical-Foundations/MF3/Home|Home]]
[[MA/Mathematical-Foundations/MF3/0. Table of Contents/TOC|Table of Contents]]
