# Vertical Asymptotes of Rational Functions

<!--
lesson-id: 1815
topic-code: MF3.7.1.5
-->

## Table of Contents

- [Introduction](#introduction)
- [Determining Vertical Asymptotes of a Rational Function](#determining-vertical-asymptotes-of-a-rational-function)
- [Determining Vertical Asymptotes of Rational Functions by Factoring the Numerator and Denominator](#determining-vertical-asymptotes-of-rational-functions-by-factoring-the-numerator-and-denominator)
- [Identifying When a Rational Function has no Vertical Asymptotes](#identifying-when-a-rational-function-has-no-vertical-asymptotes)
- [Determining the Vertical Asymptotes for the Sum of Two Rational Functions](#determining-the-vertical-asymptotes-for-the-sum-of-two-rational-functions)

## Prerequisites

- [Combining Graph Transformations of Reciprocal Functions](<../../../../AG2/5. Rational Expressions & Functions/5.2. Reciprocal Functions/Lessons/5.2.3. Combining Graph Transformations of Reciprocal Functions.md>)
- [Simplifying Rational Expressions Using Polynomial Factorization](<../../../../AG2/5. Rational Expressions & Functions/5.1. Rational Expressions/Lessons/5.1.1. Simplifying Rational Expressions Using Polynomial Factorization.md>)
- [Adding Rational Expressions With No Common Factors in the Denominator](<../../../../AG2/5. Rational Expressions & Functions/5.1. Rational Expressions/Lessons/5.1.4. Adding Rational Expressions With No Common Factors in the Denominator.md>)

---

<a id="introduction"></a>
## Introduction

To determine the vertical asymptotes of a rational function, we first cancel any common factors in the numerator and denominator. Then, we set the denominator equal to zero and solve for $x$.

For example, let's try to find the vertical asymptotes of the rational function

$$
y=\dfrac{2}{x-5}
$$

Now, there are no common factors in the numerator and denominator, and so we set the denominator equal to zero:

$$
\begin{aligned}
0 &= x - 5 \\
x &= 5
\end{aligned}
$$

Therefore, there is a vertical asymptote at $x=5$.

This matches up with what we see in the graph of the function:

![](<../Source/Vertical Asymptotes of Rational Functions - 1815/Images/8e1e41f93fe7b66e08c20400aa5924c7.png>)

---

<a id="determining-vertical-asymptotes-of-a-rational-function"></a>
## Determining Vertical Asymptotes of a Rational Function

**Example:** Find the vertical asymptotes of $y=f(x)=\dfrac{1}{x^2-16}$.

**Explanation**

Let's simplify the expression by factoring the denominator. We get

$$
\begin{aligned}
y &= \frac{1}{x^{2} - 16} \\
&= (1)/((x^{2} - 4^{2})) \\
&= (1)/((x + 4)(x - 4))
\end{aligned}
$$

There are no common factors in the numerator and denominator. So, we find the vertical asymptotes by setting the denominator equal to zero:

$$
(x+4)(x-4) = 0\qquad \Longrightarrow\qquad x=\pm 4
$$

Consequently, both $x=4$ and $x=-4$ are vertical asymptotes of $y=f(x)$.

---

**Question 1:** Find the vertical asymptotes of $y = f(x) = \frac{2}{4x - 3}$.

- [ ] A. $x =-\frac{4}{3}$
- [ ] B. $x = \frac{3}{4}$
- [ ] C. $x =-\frac{3}{4}$
- [ ] D. $x = \frac{4}{3}$
- [ ] E. There are no vertical asymptotes.

---

**Question 2:** Find the vertical asymptotes of $y = f(x) = \frac{1}{x^{2} - x - 6}$.

- [ ] A. There are no vertical asymptotes.
- [ ] B. $x =-2$ and $x = 3$
- [ ] C. $x = 1$ and $x =-6$
- [ ] D. $x =-3$ and $x = 2$
- [ ] E. $x =-1$ and $x = 6$

---

<a id="determining-vertical-asymptotes-of-rational-functions-by-factoring-the-numerator-and-denominator"></a>
## Determining Vertical Asymptotes of Rational Functions by Factoring the Numerator and Denominator

**Example:** Find the vertical asymptotes of $y = \dfrac{x^2+x-6}{x^2-5x+6}$.

**Explanation**

We start by factoring the function as much as possible and canceling the common factors:

$$
\begin{aligned}
\frac{x^{2} + x - 6}{x^{2} - 5x + 6} &= ((x - 2)(x + 3))/((x - 2)(x - 3)) \\
&= ((x - 2)(x + 3))/((x - 2)(x - 3)) \\
&= \frac{x + 3}{x - 3}
\end{aligned}
$$

We now set the denominator equal to zero:

$$
x-3 = 0\qquad \Longrightarrow\qquad x=3
$$

So the *only* vertical asymptote is at $x=3$.

---

**Question 3:** Find the vertical asymptotes of $f(x) = \frac{2x - 6}{x^{2} - 7x + 12}$.

- [ ] A. $x = 4, x = 3$
- [ ] B. No vertical asymptotes
- [ ] C. $x = 3$
- [ ] D. $x = 4$
- [ ] E. $x = 2, x = 3$

---

**Question 4:** Find the vertical asymptotes of $f(x) = \frac{x^{2} + 3x}{2x^{2} + x}$.

- [ ] A. $x = 0$, $x = \frac{1}{2}$
- [ ] B. $x =-1$
- [ ] C. $x = 0$
- [ ] D. $x = \frac{1}{2}$, $x = 1$
- [ ] E. $x =-\frac{1}{2}$

---

<a id="identifying-when-a-rational-function-has-no-vertical-asymptotes"></a>
## Identifying When a Rational Function has no Vertical Asymptotes

**Example:** Find the vertical asymptotes of $y=f(x)=\dfrac{x^2+x}{2x+2}$.

**Explanation**

Let's simplify the expression by factoring both the numerator and the denominator:

$$
\begin{aligned}
\frac{x^{2} + x}{2x + 2} &= (x(x + 1))/(2(x + 1)) \\
&= (x(x + 1))/(2(x + 1)) \\
&= \frac{x}{2}
\end{aligned}
$$

Since the denominator is never zero, we conclude that this function has no vertical asymptotes. A plot of the function is below. Note that it is not defined at $x=-1$.

![](<../Source/Vertical Asymptotes of Rational Functions - 1815/Images/b88f58b484a9741d1c21581309c5a6c4.png>)

---

**Question 5:** Find the vertical asymptotes of $f(x) = \frac{4x^{2} - 3x}{8x - 6}$.

- [ ] A. $x = \frac{3}{2}$
- [ ] B. $x = 6$
- [ ] C. $x = \frac{3}{4}$
- [ ] D. No vertical asymptotes
- [ ] E. $x = \frac{3}{8}$

---

**Question 6:** Find the vertical asymptotes of $f(x) = ((x - 1)(x^{3} + 1))/(x^{2} - 1)$.

- [ ] A. No vertical asymptotes
- [ ] B. $x =-1$
- [ ] C. $x = 1$
- [ ] D. $x =-1, 1$
- [ ] E. $x = \frac{1}{2}$

---

<a id="determining-the-vertical-asymptotes-for-the-sum-of-two-rational-functions"></a>
## Determining the Vertical Asymptotes for the Sum of Two Rational Functions

**Example:** Find the vertical asymptotes of $y=\dfrac{1}{x}+\dfrac{1}{x+1}$.

**Explanation**

First, let's put the two terms over a common denominator:

$$
\begin{aligned}
\frac{1}{x} + \frac{1}{x + 1} &= ((x + 1))/(x(x + 1)) + (x)/(x(x + 1)) \\
&= (x + 1 + x)/(x(x + 1)) \\
&= (2x + 1)/(x(x + 1))
\end{aligned}
$$

There are no common factors in the numerator and denominator, so we proceed to set the denominator equal to zero and get

$$
x(x+1) = 0\qquad \Longrightarrow\qquad x=0,-1
$$

Therefore, the vertical asymptotes are at $x=0$ and $x=-1$.

---

**Question 7:** Find the vertical asymptotes of $f(x) = \frac{1}{3x} + \frac{1}{x + 2}$.

- [ ] A. No vertical asymptotes
- [ ] B. $x =-2$
- [ ] C. $x = 0$ and $x =-2$
- [ ] D. $x = 0$
- [ ] E. $x = \frac{1}{3}$

---

**Question 8:** Find the vertical asymptotes of $f(x) = \frac{1}{x - 1} - \frac{1}{x + 4}$.

- [ ] A. $x =-4$
- [ ] B. $x = 4$ and $x =-1$
- [ ] C. $x = 1$ and $x =-4$
- [ ] D. No vertical asymptotes
- [ ] E. $x = 1$

```update-progress
```

[[MA/Mathematical-Foundations/MF3/Home|Home]]
[[MA/Mathematical-Foundations/MF3/0. Table of Contents/TOC|Table of Contents]]
