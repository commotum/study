# Improper Integrals Involving Arctangent

<!--
lesson-id: 4005
topic-code: MF3.10.6.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Evaluating an Improper Integral by Applying the Basic Result](#evaluating-an-improper-integral-by-applying-the-basic-result)
- [A Reminder of Some Useful Results](#a-reminder-of-some-useful-results)
- [Improper Integrals Involving Arctangent Using the First Result](#improper-integrals-involving-arctangent-using-the-first-result)
- [Improper Integrals Involving Arctangent Using the Second Result](#improper-integrals-involving-arctangent-using-the-second-result)
- [Calculating Improper Integrals Involving Arctangent Using Substitution](#calculating-improper-integrals-involving-arctangent-using-substitution)

## Prerequisites

- [Integration by Substitution With Inverse Trigonometric Functions](<../../../../MA/Mathematical-Foundations/MF3/10. Integration Techniques/10.1. Integration Using Substitution/Lessons/10.1.10. Integration by Substitution With Inverse Trigonometric Functions.md>)
- [Improper Integrals](<../../../../MA/Mathematical-Foundations/MF3/10. Integration Techniques/10.6. Improper Integrals/Lessons/10.6.1. Improper Integrals.md>)
- [Limits of Inverse Trigonometric Functions](<../../../../MA/Mathematical-Foundations/MF3/5. Trigonometry/5.1. The Inverse Trigonometric Functions/Lessons/5.1.5. Limits of Inverse Trigonometric Functions.md>)

---

<a id="introduction"></a>
## Introduction

An important class of improper integrals concerns those involving arctangent.

To demonstrate, let's consider the following improper integral:

$$
\displaystyle{\int_{0}^{\infty} \dfrac{1}{1+x^2} \, \textrm{d}x}
$$

First, we recall that

$$
\int \dfrac{1}{1+x^2} \, \textrm{d}x = \arctan(x) + C
$$

So, to evaluate our improper integral, we follow the usual procedure:

- First, we set the upper bound equal to some parameter $a$.
- Then, we integrate as usual.
- Finally, we take the limit as $a \to \infty$.

So, we obtain

$$
\begin{aligned}
∫_{0}^{∞}\frac{1}{1 + x^{2}}dx &= lim_(a → ∞)∫_{0}^{a}\frac{1}{1 + x^{2}}dx \\
&= lim_(a → ∞)[\arctan (x)]_{0}^{a} \\
&= lim_(a → ∞)[\arctan (a) - \arctan (0)] \\
&= lim_(a → ∞)[\arctan (a)]
\end{aligned}
$$

Now, recall the end behavior of the function

$$
y = \arctan{x}
$$

shown in the graph below:

- $\lim\limits_{x \to -\infty} \big[\arctan(x) \big] = -\dfrac{\pi}{2}$
- $\lim\limits_{x \to \infty} \big[\arctan(x) \big] = \dfrac{\pi}{2}$

![](<../Source/Improper Integrals Involving Arctangent - 4005/Images/575e40049d40450fc0a189fd198c429d.png>)

Using this to evaluate our integral, we conclude that

$$
\int_{0}^{\infty} \dfrac{1}{1+x^2} \,\textrm{d}x = \dfrac{\pi}{2}
$$

---

<a id="evaluating-an-improper-integral-by-applying-the-basic-result"></a>
## Evaluating an Improper Integral by Applying the Basic Result

**Example:** Evaluate $\displaystyle \int_{-\infty}^0 \dfrac{4}{1+x^2} \, \textrm{d}x$.

**Explanation**

First, let's recall the following result:

$$
\int \dfrac{1}{1+x^2} \, \textrm{d}x = \arctan(x) + C
$$

We proceed by setting the lower bound equal to some parameter $a$, integrating as usual, and then taking the limit as $a \to -\infty$.

$$
\begin{aligned}
∫_{- ∞}^{0}\frac{4}{1 + x^{2}}dx &= 4 \cdot lim_(a → - ∞)∫_{a}^{0}\frac{1}{1 + x^{2}}dx \\
&= 4 \cdot lim_(a → - ∞)[\arctan (x)]_{a}^{0} \\
&= 4 \cdot lim_(a → - ∞)[\arctan (0) - \arctan (a)] \\
&= 4 \cdot (0 - lim_(a → - ∞)[\arctan (a)]) \\
&=-4lim_(a → - ∞)[\arctan (a)]
\end{aligned}
$$

Now, recall the end behavior of the function

$$
y = \arctan{x}
$$

shown in the graph below:

- $\lim\limits_{x \to -\infty} \left[\arctan{x}\right] = -\dfrac{\pi}{2}$
- $\lim\limits_{x \to \infty} \left[\arctan{x}\right] = \dfrac{\pi}{2}$

![](<../Source/Improper Integrals Involving Arctangent - 4005/Images/6c01ba2881dcb5e3c67965f2a0924e63.png>)

Using this to evaluate our integral, we conclude that

$$
\begin{aligned}
∫_{- ∞}^{0}\frac{4}{1 + x^{2}}dx &= -4lim_(a → - ∞)[\arctan (a)] \\
&=-4(-\frac{π}{2}) \\
&= 2π
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  What is $∫_{\sqrt{3}/3}^{∞}\frac{7}{1 + x^{2}}dx$?
options:
- id: a
  content: |-
    $\frac{7π}{2}$
- id: b
  correct: true
  content: |-
    $\frac{7π}{3}$
- id: c
  content: |-
    $\frac{14π}{3}$
- id: d
  content: |-
    $\frac{7π}{6}$
- id: e
  content: |-
    $7π$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  What is $∫_{- ∞}^{\sqrt{3}}\frac{2}{1 + x^{2}}dx$?
options:
- id: a
  content: |-
    $\frac{π}{3}$
- id: b
  content: |-
    The integral diverges
- id: c
  correct: true
  content: |-
    $\frac{5π}{3}$
- id: d
  content: |-
    $\frac{π}{6}$
- id: e
  content: |-
    $\frac{π}{2}$
```

---

<a id="a-reminder-of-some-useful-results"></a>
## A Reminder of Some Useful Results

We can evaluate more complex integrals involving arctangent by making use of the following results:

$$
\begin{aligned}
∫(1)/(1 + (kx)^{2})dx &= \frac{1}{k}\arctan (kx) + C \\
∫\frac{1}{k^{2} + x^{2}}dx &= \frac{1}{k}\arctan (\frac{x}{k}) + C
\end{aligned}
$$

Let's see some examples.

---

<a id="improper-integrals-involving-arctangent-using-the-first-result"></a>
## Improper Integrals Involving Arctangent Using the First Result

**Example:** Evaluate the integral $\displaystyle \int_{-1/4}^\infty \dfrac {2}{1+16x^2} \,\textrm{d}x$.

**Explanation**

First, let's recall the following result:

$$
\int \dfrac{1}{1+(kx)^2} \, \textrm dx = \dfrac{1}{k} \arctan \left(kx \right) + C
$$

We proceed by setting the upper bound equal to some parameter $a$, integrating as usual, and then taking the limit as $a\to\infty$.

$$
\begin{aligned}
∫_{-1/4}^{∞}\frac{2}{1 + 16x^{2}}dx &= 2 \cdot lim_(a → ∞)∫_{-1/4}^{a}\frac{1}{1 + 16x^{2}}dx \\
&= 2 \cdot lim_(a → ∞)∫_{-1/4}^{a}(1)/(1 + (4x)^{2})dx \\
&= 2 \cdot lim_(a → ∞)[\frac{1}{4}\arctan (4x)]_{-1/4}^{a} \\
&= \frac{1}{2} \cdot lim_(a → ∞)(\arctan (4a) - \arctan (-1)) \\
&= \frac{1}{2} \cdot (lim_(a → ∞)[\arctan (4a)] - (-\frac{π}{4})) \\
&= \frac{1}{2} \cdot (lim_(a → ∞)[\arctan (4a)] + \frac{π}{4})
\end{aligned}
$$

Now, recall the end behavior of the function

$$
y=\arctan{(4x)}
$$

shown in the graph below:

- $\lim\limits_{x \to -\infty} \left[\arctan{(4x)}\right] = -\dfrac{\pi}{2}$
- $\lim\limits_{x \to \infty} \left[\arctan{(4x)}\right] = \dfrac{\pi}{2}$

![](<../Source/Improper Integrals Involving Arctangent - 4005/Images/6f825ead10f726d4996ce7df4d607c5f.png>)

Using this to evaluate our integral, we conclude that

$$
\begin{aligned}
∫_{-1/4}^{∞}\frac{2}{1 + 16x^{2}}dx &= \frac{1}{2} \cdot (lim_(a → ∞)[\arctan (4a)] + \frac{π}{4}) \\
&= \frac{1}{2} \cdot (\frac{π}{2} + \frac{π}{4}) \\
&= \frac{3π}{8}
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Evaluate the integral $∫_{0}^{∞}\frac{2}{4x^{2} + 1}dx$.
options:
- id: a
  content: |-
    $π$
- id: b
  correct: true
  content: |-
    $\frac{π}{2}$
- id: c
  content: |-
    The integral diverges
- id: d
  content: |-
    $2π$
- id: e
  content: |-
    $\frac{π}{4}$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Evaluate the integral $∫_{- ∞}^{1/2}\frac{1}{1 + 4t^{2}}dt =$
options:
- id: a
  content: |-
    $\frac{π}{8}$
- id: b
  correct: true
  content: |-
    $\frac{3π}{8}$
- id: c
  content: |-
    $\frac{3π}{2}$
- id: d
  content: |-
    The integral diverges
- id: e
  content: |-
    $\frac{π}{4}$
```

---

<a id="improper-integrals-involving-arctangent-using-the-second-result"></a>
## Improper Integrals Involving Arctangent Using the Second Result

**Example:** Evaluate the integral $\displaystyle \int_{2\sqrt{3}}^\infty \dfrac{6}{x^2+4} \,\textrm{d}x$.

**Explanation**

First, let's recall the following result:

$$
\int \dfrac{1}{k^2 + x^2} \, \textrm dx = \dfrac{1}{k} \arctan \left(\dfrac{x}{k} \right) + C
$$

We proceed by setting the upper bound equal to some parameter $a$, integrating as usual, and then taking the limit as $a\to\infty$.

$$
\begin{aligned}
∫_{2\sqrt{3}}^{∞}\frac{6}{x^{2} + 4}dx &= 6 \cdot lim_(a → ∞)∫_{2\sqrt{3}}^{a}\frac{1}{x^{2} + 4}dx \\
&= 6 \cdot lim_(a → ∞)∫_{2\sqrt{3}}^{a}\frac{1}{x^{2} + 2^{2}}dx \\
&= 6 \cdot lim_(a → ∞)[\frac{1}{2}\arctan (\frac{x}{2})]_{2\sqrt{3}}^{a} \\
&= 3lim_(a → ∞)(\arctan (\frac{a}{2}) - \arctan (\sqrt{3})) \\
&= 3lim_(a → ∞)(\arctan (\frac{a}{2}) - \frac{π}{3}) \\
&= 3lim_(a → ∞)[\arctan (\frac{a}{2})] - π
\end{aligned}
$$

Now, recall the end behavior of the function

$$
y=\arctan\left(\dfrac{x}{2}\right)
$$

shown in the graph below:

- $\lim\limits_{x \to -\infty} \left[\arctan\left(\dfrac{x}{2}\right)\right] = -\dfrac{\pi}{2}$
- $\lim\limits_{x \to \infty} \left[\arctan\left(\dfrac{x}{2}\right)\right] = \dfrac{\pi}{2}$

![](<../Source/Improper Integrals Involving Arctangent - 4005/Images/cb07856ca51f2e4c4c57cae7ba76729b.png>)

Using this to evaluate our integral, we conclude that

$$
\begin{aligned}
∫_{2\sqrt{3}}^{∞}\frac{6}{x^{2} + 4}dx &= 3lim_(a → ∞)[\arctan (\frac{a}{2})] - π \\
&= 3 \cdot \frac{π}{2} - π \\
&= \frac{π}{2}
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  Evaluate the integral $∫_{0}^{∞}\frac{2}{z^{2} + 9}dz$.
options:
- id: a
  content: |-
    $\frac{π}{2}$
- id: b
  content: |-
    $\frac{2π}{3}$
- id: c
  correct: true
  content: |-
    $\frac{π}{3}$
- id: d
  content: |-
    The integral diverges
- id: e
  content: |-
    $\frac{3π}{2}$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  What is $∫_{- ∞}^{3}\frac{3}{9 + z^{2}}dz$?
options:
- id: a
  correct: true
  content: |-
    $\frac{3π}{4}$
- id: b
  content: |-
    $\frac{π}{4}$
- id: c
  content: |-
    The integral diverges
- id: d
  content: |-
    $\frac{π}{2}$
- id: e
  content: |-
    $\frac{3π}{2}$
```

---

<a id="calculating-improper-integrals-involving-arctangent-using-substitution"></a>
## Calculating Improper Integrals Involving Arctangent Using Substitution

**Example:** Use the substitution $u = x^2$ to evaluate $\displaystyle{\int}_{1}^{\infty} \dfrac{2x}{1 + x^4} \,\textrm{d}x$.

**Explanation**

First, we substitute $u = x^2$. Differentiating, we get

$$
\dfrac{\textrm{d}u}{\textrm{d}x} = 2x \quad\Longrightarrow\quad \textrm{d}u =2x \, \textrm{d}x
$$

Since $u \to \infty$ when $x \to \infty$, the table for the limits of integration using the rule $u = x^2$ is as follows:

| $x$ | $1$ | $\infty$ |
| --- | ---: | ---: |
| $u$ | $1$ | $\infty$ |

So, the integral in terms of the new variable $u$ is

$$
\begin{aligned}
∫_{1}^{∞}\frac{2x}{1 + x^{4}}dx &= ∫_{1}^{∞}\frac{1}{1 + u^{2}}du
\end{aligned}
$$

Now, we proceed by setting the upper bound equal to some parameter $a$, integrating as usual, and then taking the limit as $a\to\infty$.

$$
\begin{aligned}
∫_{1}^{∞}\frac{2x}{1 + x^{4}}dx &= ∫_{1}^{∞}\frac{1}{1 + u^{2}}du \\
&= lim_(a → ∞)∫_{1}^{a}\frac{1}{1 + u^{2}}du \\
&= lim_(a → ∞)[\arctan (u)]_{1}^{a} \\
&= lim_(a → ∞)[\arctan (a) - \arctan (1)] \\
&= lim_(a → ∞)[\arctan (a)] - \frac{π}{4}
\end{aligned}
$$

Finally, recall the end behavior of the function

$$
y=\arctan(x)
$$

shown in the graph below:

- $\lim\limits_{x \to -\infty} \left[\arctan(x) \right] = -\dfrac{\pi}{2}$
- $\lim\limits_{x \to \infty} \left[\arctan(x) \right] = \dfrac{\pi}{2}$

![](<../Source/Improper Integrals Involving Arctangent - 4005/Images/e22f4e5f43eb489fe5da8cd1e73d5eab.png>)

Using this to evaluate our integral, we conclude that

$$
\begin{aligned}
∫_{1}^{∞}\frac{2x}{1 + x^{4}}dx &= lim_(a → ∞)[\arctan (a)] - \frac{π}{4} \\
&= \frac{π}{2} - \frac{π}{4} \\
&= \frac{π}{4}
\end{aligned}
$$

---

**Question 7:**

```quiz
type: radio
id: q-7
content: |-
  Use the substitution $u = e^{x}$ to evaluate $∫_{0}^{∞}\frac{e^{x}}{1 + 3e^{2x}}dx$.
options:
- id: a
  content: |-
    $\frac{\sqrt{3}π}{6}$
- id: b
  content: |-
    The integral diverges
- id: c
  content: |-
    $\frac{2\sqrt{3}π}{3}$
- id: d
  correct: true
  content: |-
    $\frac{\sqrt{3}π}{18}$
- id: e
  content: |-
    $\frac{\sqrt{3}π}{3}$
```

---

**Question 8:**

```quiz
type: radio
id: q-8
content: |-
  What is $∫_{- ∞}^{1}\frac{6t}{t^{4} + 3}dt$?
options:
- id: a
  content: |-
    $-3π$
- id: b
  correct: true
  content: |-
    $-\frac{π}{\sqrt{3}}$
- id: c
  content: |-
    $\frac{3π}{2}$
- id: d
  content: |-
    The integral diverges
- id: e
  content: |-
    $-\frac{\sqrt{3}π}{2}$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
