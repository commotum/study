# Special Limits Involving Cosine


<!--
lesson-id: 292
-->
## Table of Contents

- [Introduction](#introduction)
- [Evaluating a Limit of a Function Involving the Special Limit With Cosine](#evaluating-a-limit-of-a-function-involving-the-special-limit-with-cosine)
- [Evaluating a Limit of a Function Involving the Special Limit With Cosine: Advanced Cases](#evaluating-a-limit-of-a-function-involving-the-special-limit-with-cosine-advanced-cases)
- [Special Limits Involving Cosine Using a Substitution](#special-limits-involving-cosine-using-a-substitution)
- [Using the Special Limit With Cosine and Substitution to Evaluate a Limit](#using-the-special-limit-with-cosine-and-substitution-to-evaluate-a-limit)
- [Proof of the Limit](#proof-of-the-limit)

## Prerequisites

- [Simplifying Expressions Using the Pythagorean Identity](../207/207.md)
- [Calculating Limits of Rational Functions by Factoring](../1813/1813.md)
- [Evaluating Special Limits Involving Sine Using a Substitution](../3678/3678.md)

---

<a id="introduction"></a>
## Introduction

Consider the following limit:

$$
\lim_{x \to 0} \dfrac{1- \cos x}{x}
$$

Notice that direct substitution of $x=0$ leads to the indeterminate form

$$
\begin{aligned}
\lim_{x \to 0}\frac{1 - \cos x}{x} &= \frac{1 - \cos 0}{0} \\
&= \frac{1 - 1}{0} \\
&= \frac{0}{0}
\end{aligned}
$$

However, if we plot the graph of

$$
y=\dfrac{1-\cos x}{x}
$$

we get the following picture.

![](<b7d40e7f3039dc93da4554157fa1cc56.png>)

While

$$
y = \dfrac{1 - \cos{x}}{x}
$$

is undefined at $x=0$, it does appear from the graph that

$$
\lim_{x \to 0} \dfrac{1-\cos x}{x}=0
$$

This is indeed the case. Moreover, it's possible to prove this result rigorously. However, we will assume that it is true and use it to calculate other limits.

---

<a id="evaluating-a-limit-of-a-function-involving-the-special-limit-with-cosine"></a>
## Evaluating a Limit of a Function Involving the Special Limit With Cosine

**Example:** Evaluate $\lim_{y \to 0} \dfrac{\cos^2 y-1}{y}$.

**Explanation**

Notice that as $y \to 0$, both numerator and denominator approach $0$.

So, if we attempt to evaluate the limit directly, we get

$$
\lim_{y \to 0}\frac{\cos^{2} y - 1}{y} = (\cos^{2} (0) - 1)/(0) = \frac{0}{0}
$$

which is an indeterminate form.

Instead, let's recall the following special limit:

$$
\lim_{y \to 0} \dfrac{1-\cos y}{y} = 0
$$

Rewriting the given limit using the algebra of limits and applying our special limit, we obtain the following:

$$
\begin{aligned}
\lim_{y \to 0}\frac{\cos^{2} y - 1}{y} &= \lim_{y \to 0}((\cos y - 1)(\cos y + 1))/(y) \\
&= \lim_{y \to 0}\frac{\cos y - 1}{y} \cdot \lim_{y \to 0}(\cos y + 1) \\
&=-\lim_{y \to 0}\frac{1 - \cos y}{y} \cdot \lim_{y \to 0}(\cos y + 1) \\
&=-0 \cdot (\cos 0 + 1) \\
&= 0 \cdot 2 \\
&= 0
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-292-q001
content: |-
  Evaluate $\lim_{x \to 0}(1 - \cos^{2} x)/(x(1 + \cos x))$.
options:
- id: a
  content: |-
    $2$
- id: b
  content: |-
    $5$
- id: c
  content: |-
    $0$
  correct: true
- id: d
  content: |-
    $DNE$
- id: e
  content: |-
    $∞$
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-292-q002
content: |-
  What is $\lim_{x \to 0}\frac{1 - \cos x}{x\cos x}$?
options:
- id: a
  content: |-
    $-1$
- id: b
  content: |-
    $DNE$
- id: c
  content: |-
    $∞$
- id: d
  content: |-
    $1$
- id: e
  content: |-
    $0$
  correct: true
```
---

<a id="evaluating-a-limit-of-a-function-involving-the-special-limit-with-cosine-advanced-cases"></a>
## Evaluating a Limit of a Function Involving the Special Limit With Cosine: Advanced Cases

**Example:** Calculate $\lim_{x \to 0} \dfrac{\sec x -1}{x}$.

**Explanation**

Notice that as $x \to 0$, both numerator and denominator approach $0$.

So, if we attempt to evaluate the limit directly, we get

$$
\lim_{x \to 0}\dfrac{\sec x -1}{x} = \dfrac{\sec 0-1}{0} = \dfrac 00
$$

which is an indeterminate form.

Instead, let's recall the following special limit:

$$
\lim_{x \to 0} \dfrac{1-\cos x}{x} = 0
$$

Now, multiplying both the numerator and denominator by $\cos x$, we can rewrite the expression and evaluate the limit:

$$
\begin{aligned}
\lim_{x \to 0}\frac{\sec x - 1}{x} &= \lim_{x \to 0}((\sec x - 1)\cos x)/(x\cos x) \\
&= \lim_{x \to 0}((\frac{1}{\cos x} - 1)\cos x)/(x\cos x) \\
&= \lim_{x \to 0}\frac{1 - \cos x}{x\cos x} \\
&= \lim_{x \to 0}\frac{1 - \cos x}{x} \cdot \lim_{x \to 0}\frac{1}{\cos x} \\
&= 0 \cdot (1)/(\cos (0)) \\
&= 0 \cdot 1 \\
&= 0
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-292-q003
content: |-
  Calculate $\lim_{t \to 0}\frac{1 - \sec t}{t\sec t}$.
options:
- id: a
  content: |-
    $0$
  correct: true
- id: b
  content: |-
    $-1$
- id: c
  content: |-
    $1$
- id: d
  content: |-
    $DNE$
- id: e
  content: |-
    $∞$
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-292-q004
content: |-
  What is $\lim_{x \to 0}\frac{\cos x - 1 + \sin^{2} x}{x}$?
options:
- id: a
  content: |-
    $∞$
- id: b
  content: |-
    $1$
- id: c
  content: |-
    $DNE$
- id: d
  content: |-
    $-1$
- id: e
  content: |-
    $0$
  correct: true
```
---

<a id="special-limits-involving-cosine-using-a-substitution"></a>
## Special Limits Involving Cosine Using a Substitution

We can use our special limit with cosine to evaluate other limits, such as

$$
\lim_{x \to 3} \dfrac{1-\cos(x-3)}{2x-6}
$$

For this limit, notice that as $x\to3$, both the numerator and denominator approach $0$. So, if we attempt to evaluate the limit directly, we get

$$
%\lim_{x \to 0} \: \dfrac{\sin 2x}{x} = \dfrac00
$$

which is an indeterminate form.

Instead, we rewrite the limit using the algebra of limits, as follows:

$$
\begin{aligned}
\lim_{x \to 3}(1 - \cos (x - 3))/(2x - 6) &= \lim_{x \to 3}(1 - \cos (x - 3))/(2(x - 3)) \\
&= \lim_{x \to 3}(\frac{1}{2} \cdot (1 - \cos (x - 3))/(x - 3)) \\
&= \frac{1}{2} \cdot \lim_{x \to 3}(1 - \cos (x - 3))/((x - 3))
\end{aligned}
$$

Now, this limit looks very similar to our special limit for cosine. So, if we make the substitution

$$
\theta = x-3
$$

then, since $\theta \to 0$ as $x \to 3$, we have

$$
\lim_{x \to 3} \dfrac{1-\cos{\color{blue}(x-3)}}{\color{blue}(x-3)} = \lim_{\theta \to 0} \: \dfrac{1-\cos {\color{blue}\theta}}{\color{blue}\theta} = 0
$$

Therefore,

$$
\begin{aligned}
\lim_{x \to 3}(1 - \cos (x - 3))/(2x - 6) &= \frac{1}{2} \cdot \lim_{x \to 3}(1 - \cos (x - 3))/((x - 3)) \\
&= \frac{1}{2} \cdot 0 \\
&= 0
\end{aligned}
$$

---

<a id="using-the-special-limit-with-cosine-and-substitution-to-evaluate-a-limit"></a>
## Using the Special Limit With Cosine and Substitution to Evaluate a Limit

**Example:** Evaluate $\lim_{x \to 0} \dfrac{1-\cos{3x}}{x}$.

**Explanation**

Notice that as $x \to 0$, both numerator and denominator approach $0$.

So, if we attempt to evaluate the limit directly, we get

$$
\lim_{x \to 0}\dfrac{1-\cos{3x}}{x} = \dfrac{1-\cos(3\cdot 0)}{0} = \dfrac 00
$$

which is an indeterminate form.

Instead, let's recall the following special limit:

$$
\lim_{\theta \to 0} \dfrac{1-\cos \theta}{\theta} = 0
$$

Rewriting the given limit using the algebra of limits and applying our special limit, we get the following:

$$
\begin{aligned}
\lim_{x \to 0}\frac{1 - \cos 3x}{x} &= \lim_{x \to 0}(3 \cdot \frac{1 - \cos 3x}{3 \cdot x}) \\
&= 3 \cdot \lim_{x \to 0}\frac{1 - \cos 3x}{3x}
\end{aligned}
$$

Let $\theta=3x$. Then, since $\theta \to 0$ as $x \to 0$, we have

$$
\lim_{x \to 0} \dfrac{1-\cos {\color{blue}3x}}{\color{blue}3x} = \lim_{\theta \to 0} \dfrac{1-\cos {\color{blue}\theta}}{\color{blue}\theta} = 0
$$

Therefore,

$$
3\cdot\lim_{x \to 0} \dfrac{1-\cos{\color{black}3x}}{\color{black}3x}= 3\cdot 0 = 0
$$

---

**Question 5:**

```quiz
type: radio
id: MA253-UQ1-292-q005
content: |-
  Evaluate $\lim_{x \to 1}(1 - \cos (x - 1))/(1 - x)$.
options:
- id: a
  content: |-
    $-1$
- id: b
  content: |-
    $0$
  correct: true
- id: c
  content: |-
    $DNE$
- id: d
  content: |-
    $∞$
- id: e
  content: |-
    $1$
```
---

**Question 6:**

```quiz
type: radio
id: MA253-UQ1-292-q006
content: |-
  What is $\lim_{x \to 0}\frac{1 - \cos^{2} 2x}{3x}$?
options:
- id: a
  content: |-
    $\frac{4}{3}$
- id: b
  content: |-
    $DNE$
- id: c
  content: |-
    $\frac{2}{3}$
- id: d
  content: |-
    $∞$
- id: e
  content: |-
    $0$
  correct: true
```
---

<a id="proof-of-the-limit"></a>
## Proof of the Limit

We can prove the result

$$
\displaystyle \lim_{x \to 0} \dfrac{1-\cos x}{x}=0
$$

using the limit

$$
\lim_{x \to 0} \dfrac{\sin x}{x}=1
$$

First, we multiply the numerator and the denominator of

$$
\dfrac{1-\cos x}{x}
$$

by $1+\cos x$, and get

$$
\begin{aligned}
\frac{1 - \cos x}{x} &= ((1 - \cos x)(1 + \cos x))/(x(1 + \cos x)) \\
&= (1 - \cos^{2} x)/(x(1 + \cos x)) \\
&= (\sin^{2} x)/(x(1 + \cos x))
\end{aligned}
$$

We now take the limit as $x\to 0$, and obtain

$$
\begin{aligned}
\lim_{x \to 0}\frac{1 - \cos x}{x} &= \lim_{x \to 0}(\sin^{2} x)/(x(1 + \cos x)) \\
&= \lim_{x \to 0}(\frac{\sin x}{x} \cdot \frac{\sin x}{1 + \cos x}) \\
&= (\lim_{x \to 0}\frac{\sin x}{x}) \cdot (\lim_{x \to 0}\frac{\sin x}{1 + \cos x}) \\
&= 1 \cdot \frac{\sin 0}{1 + \cos 0} \\
&= \frac{0}{1 + 1} \\
&= 0
\end{aligned}
$$
---

## Navigation

- [Next: Limits Involving the Exponential Function](<253/M-1/UQ-1/Prerequisites/Limits Involving the Exponential Function - 2610.md>)
- [Back to UQ-1](UQ-1.md)

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
