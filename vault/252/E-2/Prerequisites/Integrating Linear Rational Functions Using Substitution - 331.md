# Integrating Linear Rational Functions Using Substitution

<!--
lesson-id: 331
topic-code: MF3.10.1.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Integrating a Linear Rational Function](#integrating-a-linear-rational-function)
- [Integrating a Linear Rational Function and Simplifying the Arbitrary Constant](#integrating-a-linear-rational-function-and-simplifying-the-arbitrary-constant)
- [The General Formula](#the-general-formula)
- [Integrating a Combination of Linear Rational Functions Using the General Formula](#integrating-a-combination-of-linear-rational-functions-using-the-general-formula)

## Prerequisites

- [Integrating Algebraic Functions Using Substitution](<../../../MA/Mathematical-Foundations/MF3/10. Integration Techniques/10.1. Integration Using Substitution/Lessons/10.1.1. Integrating Algebraic Functions Using Substitution.md>)
- [Integrating the Reciprocal Function](<../../../MA/Mathematical-Foundations/MF2/12. Introduction to Calculus/12.4. Indefinite Integrals/Lessons/12.4.4. Integrating the Reciprocal Function.md>)

---

<a id="introduction"></a>
## Introduction

Suppose that we want to calculate an integral like

$$
\displaystyle \int \frac{1}{2x+1}\,dx
$$

We know that

$$
\displaystyle \int \frac{1}{x}\,dx = \ln|x|
$$

but our case is different because now it's a whole function $(2x+1)$ that is in the denominator.

For integrals like the one above, we can use a substitution. First, let

$$
u=2x+1
$$

Then differentiating with respect to $x$ gives

$$
\frac{du}{dx}=2
\quad\Longrightarrow\quad
dx=\frac{1}{2}\,du
$$

We can now rewrite the integral in terms of $u$ and solve it:

$$
\begin{aligned}
\int\frac{1}{2x+1}\,dx
&=\int\frac{1}{u}\cdot\frac{1}{2}\,du \\
&=\frac{1}{2}\int\frac{1}{u}\,du \\
&=\frac{1}{2}\ln|u|+C
\end{aligned}
$$

Lastly, we write the final answer in terms of $x$:

$$
\begin{aligned}
\int\frac{1}{2x+1}\,dx
&=\frac{1}{2}\ln|2x+1|+C
\end{aligned}
$$

**Note:** After solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$
\begin{aligned}
\frac{d}{dx}\left[\frac{1}{2}\ln|2x+1|+C\right]
&=\frac{1}{2}\cdot\frac{d}{dx}\left[\ln|2x+1|\right]+\frac{d}{dx}(C) \\
&=\frac{1}{2}\cdot\frac{1}{2x+1}\cdot\frac{d}{dx}(2x+1)+0 \\
&=\frac{1}{2(2x+1)}\cdot 2 \\
&=\frac{1}{2x+1}\;\checkmark
\end{aligned}
$$

---

<a id="integrating-a-linear-rational-function"></a>
## Integrating a Linear Rational Function

**Example:** Calculate $\displaystyle \int \frac{3}{5x+2}\,dx$.

**Explanation**

First, let

$$
u=5x+2
$$

Then differentiating with respect to $x$ gives

$$
\frac{du}{dx}=5
\quad\Longrightarrow\quad
dx=\frac{1}{5}\,du
$$

We can now rewrite the integral in terms of $u$, solve it, and write the final answer in terms of $x$ as follows:

$$
\begin{aligned}
\int\frac{3}{5x+2}\,dx
&=3\int\frac{1}{5x+2}\,dx \\
&=3\int\frac{1}{u}\cdot\frac{1}{5}\,du \\
&=\frac{3}{5}\int\frac{1}{u}\,du \\
&=\frac{3}{5}\ln|u|+C \\
&=\frac{3}{5}\ln|5x+2|+C
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-49511
content: |-
  Calculate $\displaystyle \int\frac{2}{3x+5}\,dx$.
options:
- id: a
  content: |-
    $-\frac{2}{3}\ln|3x+5|+C$
- id: b
  content: |-
    $2\ln|3x+5|+C$
- id: c
  content: |-
    $6\ln|3x+5|+C$
- id: d
  content: |-
    $\frac{2}{3}\ln|3x+5|+C$
  correct: true
- id: e
  content: |-
    $-2\ln|3x+5|+C$
```

---

**Question 2:**

```quiz
type: radio
id: ma-15707
content: |-
  What is $\displaystyle \int\frac{2}{x+1}\,dx$?
options:
- id: a
  content: |-
    $\frac{1}{2}\ln|x+1|+C$
- id: b
  content: |-
    $2\ln|x+1|+C$
  correct: true
- id: c
  content: |-
    $-\frac{1}{2}\ln|x+1|+C$
- id: d
  content: |-
    $-2\ln|x+1|+C$
- id: e
  content: |-
    $\ln|x+1|+C$
```

---

<a id="integrating-a-linear-rational-function-and-simplifying-the-arbitrary-constant"></a>
## Integrating a Linear Rational Function and Simplifying the Arbitrary Constant

**Example:** Calculate $\displaystyle \int \frac{1}{1+2x}\,dx$, writing your final answer as a single function.

**Explanation**

First, let

$$
u=1+2x
$$

Then differentiating with respect to $x$ gives

$$
\frac{du}{dx}=2
\quad\Longrightarrow\quad
dx=\frac{1}{2}\,du
$$

We can now rewrite the integral in terms of $u$, solve it, and write the final answer in terms of $x$ as follows:

$$
\begin{aligned}
\int\frac{1}{1+2x}\,dx
&=\int\frac{1}{u}\cdot\frac{1}{2}\,du \\
&=\frac{1}{2}\int\frac{1}{u}\,du \\
&=\frac{1}{2}\ln|u|+C \\
&=\frac{1}{2}\ln|1+2x|+C
\end{aligned}
$$

We can further simplify the above by writing

$$
C=\frac{1}{2}\ln K
$$

for another arbitrary constant $K > 0$, and then we can combine the two terms using the laws of logarithms, as follows:

$$
\begin{aligned}
\frac{1}{2}\ln|1+2x|+C
&=\frac{1}{2}\ln|1+2x|+\frac{1}{2}\ln K \\
&=\frac{1}{2}\ln\!\left(K\cdot|1+2x|\right) \\
&=\frac{1}{2}\ln\!\left(K|1+2x|\right)
\end{aligned}
$$

So, we finally conclude that

$$
\int\frac{1}{1+2x}\,dx
=\frac{1}{2}\ln\!\left(K|1+2x|\right)
$$

---

**Question 3:**

```quiz
type: radio
id: ma-49516
content: |-
  What is $\displaystyle \int\frac{6}{5-3x}\,dx$?
options:
- id: a
  content: |-
    $-2\ln\!\left(K|5-3x|\right)$
  correct: true
- id: b
  content: |-
    $\frac{1}{2}\ln\!\left(K|5-3x|\right)$
- id: c
  content: |-
    $2\ln\!\left(K|5-3x|\right)$
- id: d
  content: |-
    $\ln\!\left(K|5-3x|\right)$
- id: e
  content: |-
    $-\frac{1}{2}\ln\!\left(K|5-3x|\right)$
```

---

**Question 4:**

```quiz
type: radio
id: ma-49513
content: |-
  Calculate $\displaystyle \int\frac{3}{2x+5}\,dx$.
options:
- id: a
  content: |-
    $\frac{5}{2}\ln\!\left(K|2x+5|\right)$
- id: b
  content: |-
    $2\ln\!\left(K|2x+5|\right)$
- id: c
  content: |-
    $\frac{2}{3}\ln\!\left(K|2x+5|\right)$
- id: d
  content: |-
    $\frac{3}{2}\ln\!\left(K|2x+5|\right)$
  correct: true
- id: e
  content: |-
    $\frac{1}{5}\ln\!\left(K|2x+5|\right)$
```

---

<a id="the-general-formula"></a>
## The General Formula

In general,

$$
\int\frac{1}{ax+b}\,dx
=\frac{1}{a}\ln|ax+b|+C
$$

These types of integrals come up quite often in calculus, so it's worth remembering this formula.

---

<a id="integrating-a-combination-of-linear-rational-functions-using-the-general-formula"></a>
## Integrating a Combination of Linear Rational Functions Using the General Formula

**Example:** Calculate $\displaystyle \int\left(\frac{1}{1+2x}+\frac{1}{1-2x}\right)\,dx$.

**Explanation**

Let's solve this using the general formula:

$$
\begin{aligned}
\int\left(\frac{1}{1+2x}+\frac{1}{1-2x}\right)\,dx
&=\int\frac{1}{1+2x}\,dx+\int\frac{1}{1-2x}\,dx \\
&=\frac{1}{2}\ln|1+2x|-\frac{1}{2}\ln|1-2x|+C \\
&=\frac{1}{2}\ln\left|\frac{1+2x}{1-2x}\right|+\frac{1}{2}\ln K \\
&=\frac{1}{2}\ln\!\left(K\left|\frac{1+2x}{1-2x}\right|\right)
\end{aligned}
$$

Notice that we used the laws of logarithms to write the result as a single logarithm.

---

**Question 5:**

```quiz
type: radio
id: ma-49524
content: |-
  Calculate $\displaystyle \int\left(\frac{1}{2+4x}+\frac{1}{2-4x}\right)\,dx$.
options:
- id: a
  content: |-
    $-4\ln\!\left(K|(2+4x)(2-4x)|\right)$
- id: b
  content: |-
    $\frac{1}{4}\ln\!\left(K\left|\frac{2+4x}{2-4x}\right|\right)$
  correct: true
- id: c
  content: |-
    $-\frac{1}{4}\ln\!\left(K\left|\frac{2+4x}{2-4x}\right|\right)$
- id: d
  content: |-
    $4\ln\!\left(K\left|\frac{2+4x}{2-4x}\right|\right)$
- id: e
  content: |-
    $\frac{1}{4}\ln\!\left(K|(2+4x)(2-4x)|\right)$
```

---

**Question 6:**

```quiz
type: radio
id: ma-49521
content: |-
  What is $\displaystyle \int\left(\frac{1}{3+x}+\frac{1}{3-x}\right)\,dx$?
options:
- id: a
  content: |-
    $\frac{1}{3}\ln\!\left(K\left|\frac{3+x}{3-x}\right|\right)$
- id: b
  content: |-
    $3\ln\!\left(K|(3+x)(3-x)|\right)$
- id: c
  content: |-
    $-\frac{1}{3}\ln\!\left(K|(3+x)(3-x)|\right)$
- id: d
  content: |-
    $-3\ln\!\left(K\left|\frac{3+x}{3-x}\right|\right)$
- id: e
  content: |-
    $\ln\!\left(K\left|\frac{3+x}{3-x}\right|\right)$
  correct: true
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
