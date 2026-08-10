# Limits of Reciprocal Functions

<!--
lesson-id: 1905
topic-code: MF2.11.3.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Limits at Infinity of Reciprocal Functions](#limits-at-infinity-of-reciprocal-functions)
- [Limits at Infinity of Reciprocals of Polynomials](#limits-at-infinity-of-reciprocals-of-polynomials)
- [Limits at Infinity of Reciprocals of Polynomials](#limits-at-infinity-of-reciprocals-of-polynomials)
- [Infinite Limits of Reciprocal Functions Where the Leading Term Has an Odd Power](#infinite-limits-of-reciprocal-functions-where-the-leading-term-has-an-odd-power)
- [Infinite Limits of Reciprocal Functions Where the Leading Term Has an Odd Power](#infinite-limits-of-reciprocal-functions-where-the-leading-term-has-an-odd-power)
- [Infinite Limits of Reciprocal Functions Where the Leading Term Has an Even Power](#infinite-limits-of-reciprocal-functions-where-the-leading-term-has-an-even-power)
- [Infinite Limits of Reciprocal Functions Where the Leading Term Has an Even Power](#infinite-limits-of-reciprocal-functions-where-the-leading-term-has-an-even-power)

## Prerequisites

- [Limits at Infinity of Polynomials](<../../../../MA/Mathematical-Foundations/MF2/11. Limits & Continuity/11.3. Limits of Functions/Lessons/11.3.1. Limits at Infinity of Polynomials.md>)
- [Infinite Limits from Graphs](<../../../../MA/Mathematical-Foundations/MF2/11. Limits & Continuity/11.1. Estimating Limits from Graphs/Lessons/11.1.5. Infinite Limits from Graphs.md>)
- [Graphing Reciprocal Functions](<../../../../MA/Mathematical-Foundations/MF2/6. Radical & Rational Functions/6.3. Rational Functions/Lessons/6.3.1. Graphing Reciprocal Functions.md>)

---

<a id="introduction"></a>
## Introduction

How do we calculate

$$
\displaystyle \lim_{x\to\infty}\left(\dfrac{1}{x}\right)
$$

and

$$
\displaystyle \lim_{x\to-\infty}\left(\dfrac{1}{x}\right)
$$

To find out, let's look at the graph of

$$
y=\dfrac{1}{x}
$$

![](<../Source/Limits of Reciprocal Functions - 1905/Images/b6a797f2a07b1cb03ccd7b86bac613ca.png>)

We see that the curve approaches zero as $x$ approaches positive infinity. The same is true as $x$ approaches negative infinity. So, we write

$$
\lim_\limits{x \to \infty} \left(\dfrac{1}{x}\right)=0 \qquad \textrm{and} \qquad \lim_\limits{x \to -\infty} \left(\dfrac{1}{x}\right)=0
$$

The same is true for

$$
\dfrac{1}{x^n}
$$

where $n$ is *any* positive integer. For example,

$$
lim_(x → ∞)(\frac{1}{x^{2}}) = 0\begin{vmatrix}andlim_(x → - ∞)(\frac{1}{x^{2}}) = 0 \\ lim_(x → ∞)(\frac{1}{x^{3}}) = 0\end{vmatrix}andlim_(x → - ∞)(\frac{1}{x^{3}}) = 0; ⋮
$$

and so on. This is because as the size of $x$ increases, the size of

$$
\dfrac{1}{x^n}
$$

decreases.

---

<a id="limits-at-infinity-of-reciprocal-functions"></a>
## Limits at Infinity of Reciprocal Functions

**Example:** Compute $\lim_\limits{x \to \infty} \dfrac{1}{4x^4}$.

**Explanation**

First, we use the algebra of limits to pull out the constant factor of

$$
\dfrac 1 4
$$

$$
\begin{aligned}
lim_(x → ∞)\frac{1}{4x^{4}} &= lim_(x → ∞)\frac{1}{4} \cdot \frac{1}{x^{4}} \\
&= \frac{1}{4} \cdot lim_(x → ∞)\frac{1}{x^{4}}
\end{aligned}
$$

Now, using the fact that

$$
\lim_\limits{x \to \infty} \left(\dfrac{1}{x^4}\right)=0
$$

we can evaluate our limit as follows:

$$
\dfrac{1}{4} \cdot\lim_\limits{x \to \infty} \dfrac{1}{x^4} = \dfrac 1 4\cdot 0 = 0
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Compute $lim_(x → ∞)\frac{24x^{5}}{3x^{9}}$.
options:
- id: a
  content: |-
    $DNE$
- id: b
  content: |-
    $0$
  correct: true
- id: c
  content: |-
    $∞$
- id: d
  content: |-
    $- ∞$
- id: e
  content: |-
    $8$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  What is $lim_(x → ∞)(\frac{2}{x^{3}})$?
options:
- id: a
  content: |-
    $2$
- id: b
  content: |-
    $- ∞$
- id: c
  content: |-
    $0$
  correct: true
- id: d
  content: |-
    $1$
- id: e
  content: |-
    $∞$
```

---

<a id="limits-at-infinity-of-reciprocals-of-polynomials"></a>
## Limits at Infinity of Reciprocals of Polynomials

For any non-constant polynomial $P(x)$, we have

$$
\lim_{x\to\pm\infty}\left(\dfrac{1}{P(x)}\right) = 0
$$

This is because as $x$ increases, any polynomial $P(x)$ will grow without bound, and therefore its reciprocal shrinks to zero.

For example, the expression $x^3 - x^2 + 1$ is a non-constant polynomial, so we have

$$
\lim_{x\to\pm\infty}\left(\dfrac{1}{x^3 - x^2 + 1}\right) = 0
$$

Likewise, the expression $(2x-5)^4$ can be multiplied out to become a non-constant polynomial, so we have

$$
\lim_{x\to\pm\infty}\left(\dfrac{1}{(2x-5)^4}\right) = 0
$$

---

<a id="limits-at-infinity-of-reciprocals-of-polynomials"></a>
## Limits at Infinity of Reciprocals of Polynomials

**Example:** Compute $\lim_\limits{x \to -\infty} \dfrac{1}{(1-x)^4} \,$.

**Explanation**

For any non-constant polynomial $P(x)$, we have

$$
\lim_{x\to\pm\infty}\left(\dfrac{1}{P(x)}\right) = 0
$$

Therefore, since $(1-x)^4$ is a non-constant polynomial, we have

$$
\lim_\limits{x \to -\infty} \dfrac{1}{(1-x)^4} = 0
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Evaluate $lim_(x → ∞)\frac{1}{x^{2} + 1}$.
options:
- id: a
  content: |-
    $1$
- id: b
  content: |-
    $- ∞$
- id: c
  content: |-
    $0$
  correct: true
- id: d
  content: |-
    $-1$
- id: e
  content: |-
    $∞$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Evaluate $lim_(x → ∞)(9)/((2 - x)^{5})$.
options:
- id: a
  content: |-
    $DNE$
- id: b
  content: |-
    $- ∞$
- id: c
  content: |-
    $0$
  correct: true
- id: d
  content: |-
    $∞$
- id: e
  content: |-
    $4.5$
```

---

<a id="infinite-limits-of-reciprocal-functions-where-the-leading-term-has-an-odd-power"></a>
## Infinite Limits of Reciprocal Functions Where the Leading Term Has an Odd Power

Let's again look at the graph of

$$
y=\dfrac{1}{x}
$$

![](<../Source/Limits of Reciprocal Functions - 1905/Images/b6993678c5aa3e224e42b0167620a04a.png>)

From the graph, we see that

$$
\lim_\limits{x\rightarrow 0^-} \left(\dfrac{1}{x}\right) = -\infty \qquad \textrm{and} \qquad \lim_\limits{x\rightarrow 0^+} \left(\dfrac{1}{x}\right) = \infty
$$

Since the left and right-sided limits are not the same, we conclude that

$$
\lim_\limits{x\rightarrow 0} \left(\dfrac{1}{x}\right) = \textrm{DNE}
$$

Any function of the form

$$
y = \dfrac{1}{x^n}
$$

where $n$ is an *odd* natural number, has the same shape as

$$
y = \dfrac{1}{x}
$$

and consequently the limit behavior is the same. For example,

$$
lim_(x → 0^{-})(\frac{1}{x^{3}}) = - ∞,\begin{vmatrix}lim_(x → 0^{+})(\frac{1}{x^{3}}) = ∞, \\ lim_(x → 0^{-})(\frac{1}{x^{5}}) = - ∞,\end{vmatrix}lim_(x → 0^{+})(\frac{1}{x^{5}}) = ∞,; ⋮
$$

and so on. For all of the above, the limit of the function does not exist at $x=0$ because the left and right limits are not the same.

---

<a id="infinite-limits-of-reciprocal-functions-where-the-leading-term-has-an-odd-power"></a>
## Infinite Limits of Reciprocal Functions Where the Leading Term Has an Odd Power

**Example:** Compute $\lim_\limits{x \to (-1)} \dfrac{1}{(x+1)^3} \,$.

**Explanation**

We can sketch the graph of

$$
y = \dfrac{1}{(x+1)^3}
$$

as follows:

1. Take the graph of $y = \dfrac 1 {x^3}$.
2. Translate it to the left by $1$ unit. This gives $y = \dfrac{1}{(x+1)^3}$, as shown below.

![](<../Source/Limits of Reciprocal Functions - 1905/Images/9c39cd90f5afc7f335f062275373bc61.png>)

From the graph, we see that

$$
\lim_\limits{x \to (-1^-)} \dfrac{1}{(x+1)^3} = -\infty, \qquad \lim_\limits{x \to (-1^+)} \dfrac{1}{(x+1)^3} = \infty
$$

and therefore

$$
\lim_\limits{x \to (-1)} \dfrac{1}{(x+1)^3}= \textrm{DNE}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  Compute $lim_(x → 2)\frac{1}{x - 2}$.
options:
- id: a
  content: |-
    $DNE$
  correct: true
- id: b
  content: |-
    $∞$
- id: c
  content: |-
    $0$
- id: d
  content: |-
    $- ∞$
- id: e
  content: |-
    $6$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  What is $lim_(x → 0^{-})\frac{2}{3x}$?
options:
- id: a
  content: |-
    $DNE$
- id: b
  content: |-
    $∞$
- id: c
  content: |-
    $\frac{2}{3}$
- id: d
  content: |-
    $- ∞$
  correct: true
- id: e
  content: |-
    $0$
```

---

<a id="infinite-limits-of-reciprocal-functions-where-the-leading-term-has-an-even-power"></a>
## Infinite Limits of Reciprocal Functions Where the Leading Term Has an Even Power

Now let's look at the graph of

$$
y = \dfrac{1}{x^2}
$$

![](<../Source/Limits of Reciprocal Functions - 1905/Images/78df45f8e96cd361e6b34a23b6a4c28e.png>)

We see that as we approach $0$ from both sides, the function grows rapidly without bound. So

$$
\lim_\limits{x\rightarrow 0^-}\left(\dfrac{1}{x^2}\right) = \lim_\limits{x\rightarrow 0^+} \left(\dfrac{1}{x^2}\right)= \infty
$$

which implies that

$$
\lim_\limits{x\rightarrow 0} \left(\dfrac{1}{x^2}\right)= \infty
$$

Any function of the form

$$
y = \dfrac{1}{x^n}
$$

(where $n$ is an *even* natural number) has the same shape as

$$
y = \dfrac{1}{x^2}
$$

Therefore,

$$
\lim_\limits{x\rightarrow 0} \left(\dfrac{1}{x^n}\right)= \infty, \qquad n=2,4,6,\ldots
$$

---

<a id="infinite-limits-of-reciprocal-functions-where-the-leading-term-has-an-even-power"></a>
## Infinite Limits of Reciprocal Functions Where the Leading Term Has an Even Power

**Example:** Calculate $\lim_\limits {x\rightarrow -1} \dfrac{1}{(x+1)^4}$.

**Explanation**

We can sketch the graph of

$$
y = \dfrac{1}{(x+1)^4}
$$

as follows:

1. Take the graph of $y = \dfrac 1 {x^4}$.
2. Translate it to the left by $1$ unit. This gives $y = \dfrac{1}{(x+1)^4}$, as shown below.

![](<../Source/Limits of Reciprocal Functions - 1905/Images/46ea10487aa5d06d4ce251fffd830dc2.png>)

From the graph, we see that

$$
\lim_\limits{x \to (-1^-)} \dfrac{1}{(x+1)^4} = \infty, \qquad \lim_\limits{x \to (-1^+)} \dfrac{1}{(x+1)^4} = \infty
$$

and therefore

$$
\lim_\limits{x \to (-1)} \dfrac{1}{(x+1)^4}= \infty
$$

---

**Question 7:**

```quiz
type: radio
id: q-7
content: |-
  Compute $lim_(x → 2)(5)/(2(x - 2)^{8})$.
options:
- id: a
  content: |-
    $\frac{5}{2}$
- id: b
  content: |-
    $- ∞$
- id: c
  content: |-
    $0$
- id: d
  content: |-
    $∞$
  correct: true
- id: e
  content: |-
    $DNE$
```

---

**Question 8:**

```quiz
type: radio
id: q-8
content: |-
  Compute $lim_(x → 1)(1)/((x - 1)^{2})$.
options:
- id: a
  content: |-
    $- ∞$
- id: b
  content: |-
    $DNE$
- id: c
  content: |-
    $∞$
  correct: true
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $1$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
