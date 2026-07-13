# Intervals of Convergence for Scaled Inverse-Sine Series

## Table of Contents

- [Introduction](#introduction)
- [Start From the Standard Inverse-Sine Interval](#start-from-the-standard-inverse-sine-interval)
- [Pull the Interval Back Through a Scale](#pull-the-interval-back-through-a-scale)
- [Use Absolute Value for a Negative Scale](#use-absolute-value-for-a-negative-scale)
- [Recognize When Scaling Widens the Interval](#recognize-when-scaling-widens-the-interval)
- [Apply the Move to the Assigned Function](#apply-the-move-to-the-assigned-function)
- [Summary](#summary)

## Prerequisites

- [Maclaurin Series](<Maclaurin Series - 340.md>)
- [Representing Functions as Power Series](<Representing Functions as Power Series - 885.md>)
- [Graphing the Inverse Sine Function](<../Prerequisites/Graphing the Inverse Sine Function - 1483.md>)
- Solving absolute-value inequalities such as $|cx|\leq 1$

---

<a id="introduction"></a>
## Introduction

When a known Maclaurin series is used with a new expression inside the function, the same expression must be substituted into its convergence condition.

For a function of the form

$$
f(x)=\arcsin(cx),
$$

the recognition cue is the scaled input $cx$. Start with the interval for the standard series in a placeholder variable $u$, substitute $u=cx$, and solve the resulting inequality for $x$.

The reusable move is

$$
u\in[-1,1]
\quad\Longrightarrow\quad
cx\in[-1,1]
\quad\Longrightarrow\quad
|x|\leq \frac{1}{|c|}.
$$

Thus, for $c\neq 0$, the interval is

$$
\left[-\frac{1}{|c|},\frac{1}{|c|}\right].
$$

---

<a id="start-from-the-standard-inverse-sine-interval"></a>
## Start From the Standard Inverse-Sine Interval

**Example:** State the interval of convergence of the standard Maclaurin series for $\arcsin(u)$.

**Explanation**

The standard expansion begins

$$
\arcsin(u)
=u+\frac{u^3}{6}+\frac{3u^5}{40}+\frac{5u^7}{112}+\cdots
$$

and can be written as

$$
\arcsin(u)
=\sum_{n=0}^{\infty}
\frac{(2n)!}{4^n(n!)^2(2n+1)}u^{2n+1}.
$$

This series converges for

$$
-1\leq u\leq 1.
$$

Both endpoints are included, so the standard interval is $[-1,1]$. This is a fact about the standard inverse-sine series; in general, one should not decide a power series' endpoint behavior from the function's domain alone.

```quiz
type: radio
id: ohw8-p10-q1
content: |-
  Which condition describes the interval of convergence of the standard Maclaurin series for $\arcsin(u)$?
options:
- id: q1-a
  content: |-
    $|u|\leq 1$
  correct: true
- id: q1-b
  content: |-
    $|u|<1$
- id: q1-c
  content: |-
    $|u|\geq 1$
- id: q1-d
  content: |-
    $u\in(-\infty,\infty)$
```

---

<a id="pull-the-interval-back-through-a-scale"></a>
## Pull the Interval Back Through a Scale

**Example:** Find the interval of convergence of the Maclaurin expansion for $\arcsin(4x)$.

**Explanation**

Replace the standard input $u$ with the actual input $4x$:

$$
|u|\leq 1
\quad\Longrightarrow\quad
|4x|\leq 1.
$$

Since $|4x|=4|x|$,

$$
4|x|\leq 1
\quad\Longrightarrow\quad
|x|\leq \frac14.
$$

Therefore, the interval is

$$
\left[-\frac14,\frac14\right].
$$

The scale factor $4$ makes the interval four times narrower.

```quiz
type: radio
id: ohw8-p10-q2
content: |-
  What is the interval of convergence of the Maclaurin expansion for $\arcsin(7x)$?
options:
- id: q2-a
  content: |-
    $\left[-\dfrac17,\dfrac17\right]$
  correct: true
- id: q2-b
  content: |-
    $\left(-\dfrac17,\dfrac17\right)$
- id: q2-c
  content: |-
    $[-7,7]$
- id: q2-d
  content: |-
    $[-1,1]$
- id: q2-e
  content: |-
    $(-\infty,\infty)$
```

---

<a id="use-absolute-value-for-a-negative-scale"></a>
## Use Absolute Value for a Negative Scale

**Example:** Find the interval of convergence of the Maclaurin expansion for $\arcsin(-5x)$.

**Explanation**

The convergence condition is

$$
|-5x|\leq 1.
$$

Absolute value removes the sign of the scale:

$$
5|x|\leq 1
\quad\Longrightarrow\quad
|x|\leq \frac15.
$$

Therefore,

$$
x\in\left[-\frac15,\frac15\right].
$$

The negative sign changes the values of the series, but it does not change the size of its interval of convergence. Using $|c|$ avoids inequality-direction mistakes.

```quiz
type: radio
id: ohw8-p10-q3
content: |-
  What is the interval of convergence of the Maclaurin expansion for $\arcsin(-8x)$?
options:
- id: q3-a
  content: |-
    $\left[-\dfrac18,\dfrac18\right]$
  correct: true
- id: q3-b
  content: |-
    $\left(-\dfrac18,\dfrac18\right)$
- id: q3-c
  content: |-
    $\left[\dfrac18,-\dfrac18\right]$
- id: q3-d
  content: |-
    $[-8,8]$
- id: q3-e
  content: |-
    $[-1,1]$
```

---

<a id="recognize-when-scaling-widens-the-interval"></a>
## Recognize When Scaling Widens the Interval

**Example:** Find the interval of convergence of the Maclaurin expansion for $\arcsin\left(\dfrac{x}{3}\right)$.

**Explanation**

Here the scale is $c=\dfrac13$. Substitute the actual input into the standard condition:

$$
\left|\frac{x}{3}\right|\leq 1.
$$

Multiplying by $3$ gives

$$
|x|\leq 3.
$$

Therefore, the interval is

$$
[-3,3].
$$

A scale with magnitude less than $1$ widens the interval. The reliable rule remains $|x|\leq 1/|c|$; do not automatically place the written coefficient in the denominator of the final endpoint.

```quiz
type: radio
id: ohw8-p10-q4
content: |-
  What is the interval of convergence of the Maclaurin expansion for $\arcsin\left(\dfrac{x}{6}\right)$?
options:
- id: q4-a
  content: |-
    $[-6,6]$
  correct: true
- id: q4-b
  content: |-
    $(-6,6)$
- id: q4-c
  content: |-
    $\left[-\dfrac16,\dfrac16\right]$
- id: q4-d
  content: |-
    $[-1,1]$
- id: q4-e
  content: |-
    $(-\infty,\infty)$
```

---

<a id="apply-the-move-to-the-assigned-function"></a>
## Apply the Move to the Assigned Function

**Example:** Find the interval of convergence of the Maclaurin expansion for

$$
f(x)=\sin^{-1}(9x).
$$

**Explanation**

Here $\sin^{-1}$ means $\arcsin$, and the actual input is $u=9x$. Pull back the standard interval:

$$
-1\leq 9x\leq 1.
$$

Divide every part by $9$:

$$
-\frac19\leq x\leq \frac19.
$$

Because the standard inverse-sine series converges at $u=-1$ and $u=1$, the corresponding $x$-values stay included. In interval notation, the answer is

$$
\boxed{\left[-\frac19,\frac19\right]}.
$$

```quiz
type: radio
id: ohw8-p10-q5
content: |-
  Find the interval of convergence of the Maclaurin expansion for $f(x)=\sin^{-1}(12x)$.
options:
- id: q5-a
  content: |-
    $\left[-\dfrac1{12},\dfrac1{12}\right]$
  correct: true
- id: q5-b
  content: |-
    $\left(-\dfrac1{12},\dfrac1{12}\right)$
- id: q5-c
  content: |-
    $[-12,12]$
- id: q5-d
  content: |-
    $[-1,1]$
- id: q5-e
  content: |-
    $(-\infty,\infty)$
```

---

<a id="summary"></a>
## Summary

For a scaled inverse-sine function $\arcsin(cx)$:

1. Recall that the standard $\arcsin(u)$ Maclaurin series converges for $u\in[-1,1]$.
2. Substitute the actual input: $u=cx$.
3. Solve $|cx|\leq 1$ to get $|x|\leq 1/|c|$.
4. Keep square brackets because the standard series includes both endpoints.

Therefore,

$$
\arcsin(cx)
\quad\text{has interval}\quad
\left[-\frac1{|c|},\frac1{|c|}\right]
\qquad(c\neq 0).
$$

The main traps are multiplying by $|c|$ instead of dividing, dropping the endpoint brackets, and treating a negative scale as a different radius.
