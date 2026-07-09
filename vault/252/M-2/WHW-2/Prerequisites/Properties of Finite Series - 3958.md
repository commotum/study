# Properties of Finite Series

<!--
lesson-id: 3958
topic-code: MF2.7.1.5
-->

## Table of Contents

- [Introduction](#introduction)
- [Evaluating a Series Using the Constant Multiple Rule](#evaluating-a-series-using-the-constant-multiple-rule)
- [Sums of Constants](#sums-of-constants)
- [Evaluating a Sum of Constants](#evaluating-a-sum-of-constants)
- [The Sum Rule](#the-sum-rule)
- [Evaluating a Sum Using Finite Series Properties](#evaluating-a-sum-using-finite-series-properties)

## Prerequisites

- [Sigma Notation](<../../../../MA/Mathematical-Foundations/MF2/7. Sequences/7.1. Introduction to Sequences/Lessons/7.1.4. Sigma Notation.md>)

---

<a id="introduction"></a>
## Introduction

Suppose we have a sequence $a_i$ for

$$
i\geq 1
$$

and the sum of the first $10$ terms of a sequence equals $25$. We can express this using sigma notation as follows:

$$
\sum_{i=1}^{10} a_i = 25
$$

If we multiply each term of the sequence by $2$, what will be the sum of the first $10$ terms of this new sequence? In other words, what is the value of the following sum?

$$
\sum_{i=1}^{10} 2a_i
$$

We can compute this sum by expanding the summation:

$$
\begin{aligned}
∑_(i = 1)^(10)2a_{i} &= 2a_{1} + 2a_{2} + ⋯ + 2a_{10} \\
&= 2 \cdot (a_{1} + a_{2} + ⋯ + a_{10}) \\
&= 2 \cdot ∑_(i = 1)^(10)a_{i} \\
&= 2 \cdot 25 \\
&= 50
\end{aligned}
$$

In short, we found that

$$
\sum_{i=1}^{10} 2a_i = 2\cdot \sum_{i=1}^{10} a_i
$$

In general, if $a_i$ is a sequence and $c$ is any constant, then

$$
\sum_{i=1}^{n} c a_i = c \cdot \sum_{i=1}^{n} a_i
$$

---

<a id="evaluating-a-series-using-the-constant-multiple-rule"></a>
## Evaluating a Series Using the Constant Multiple Rule

**Example:** Given that
$\displaystyle{\sum_{i=1}^{10} a_i} = 5$,
find the value of
$\displaystyle{\sum_{i=1}^{10} (-2a_i)}$.

**Explanation**

Recall that for any constant $c$, we have

$$
\sum_{i=1}^{n} c a_i = c \cdot \sum_{i=1}^{n} a_i
$$

Therefore,

$$
\begin{aligned}
∑_(i = 1)^(10)(-2a_{i}) &= -2 \cdot ∑_(i = 1)^(10)a_{i} \\
&=-2 \cdot 5 \\
&=-10
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Given that
  
  $∑_(i = 1)^(17)a_{i} = 125$,
  find the value of
  $∑_(i = 1)^(17)4a_{i}$.
options:
- id: a
  content: |-
    $3125$
- id: b
  content: |-
    $(125)^{3}$
- id: c
  correct: true
  content: |-
    $500$
- id: d
  content: |-
    $600$
- id: e
  content: |-
    $400$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Given that
  
  $∑_(i = 1)^(10)a_{i} = 12$,
  find the value of
  $∑_(i = 1)^(10)(-3a_{i})$.
options:
- id: a
  correct: true
  content: |-
    $-36$
- id: b
  content: |-
    $-30$
- id: c
  content: |-
    $-26$
- id: d
  content: |-
    $-9$
- id: e
  content: |-
    $-120$
```

---

<a id="sums-of-constants"></a>
## Sums of Constants

Let's now determine the value of the following sum:

$$
\sum_{i=1}^{15} 1
$$

This is an example of a series where every term in the corresponding sequence equals $1$.

To compute this sum, let's write out the summation explicitly:

$$
\sum_{i=1}^{15} 1 = \underbrace{1+1+\cdots + 1}_{15\,\textrm{times}}
$$

Therefore,

$$
\sum_{i=1}^{15} 1 = 15\cdot 1 = 15
$$

In general, for any integer

$$
n \geq 1
$$

we have

$$
\sum_{i=1}^{n} 1 = n
$$

---

<a id="evaluating-a-sum-of-constants"></a>
## Evaluating a Sum of Constants

**Example:** Evaluate
$\displaystyle{\sum_{i=1}^{100} \dfrac14}$.

**Explanation**

Using the constant multiple rule, we can write

$$
\sum_{i=1}^{100}\dfrac14 =\dfrac14\cdot \sum_{i=1}^{100} 1
$$

Then, we note that

$$
\sum_{i=1}^{100} 1 = \underbrace{1+1+\cdots + 1}_{100\,\textrm{times}} = 100
$$

Therefore,

$$
\dfrac14\cdot \sum_{i=1}^{100} 1 = \dfrac14\cdot 100= 25
$$

---

**Question 3**

```quiz
type: radio
id: q-3
content: |-
  What is the value of $∑_(i = 1)^(43)1$?
options:
- id: a
  content: |-
    $1$
- id: b
  content: |-
    $42$
- id: c
  correct: true
  content: |-
    $43$
- id: d
  content: |-
    $44$
- id: e
  content: |-
    $86$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Evaluate
  
  $∑_(i = 1)^(12)7$.
options:
- id: a
  content: |-
    $12^{7}$
- id: b
  correct: true
  content: |-
    $84$
- id: c
  content: |-
    $98$
- id: d
  content: |-
    $70$
- id: e
  content: |-
    $19$
```

---

<a id="the-sum-rule"></a>
## The Sum Rule

If $a_i$ and $b_i$ for

$$
i\geq 1
$$

are sequences, then we have the following property:

$$
\sum_{i=1}^{n} (a_i+b_i) = \sum_{i=1}^{n} a_i + \sum_{i=1}^{n} b_i
$$

We sometimes call this property the **sum rule**.

To see how we might apply this rule, suppose we are given the following series:

$$
\sum_{i=1}^{10} a_i = 5, \qquad \sum_{i=1}^{10} b_i = 8
$$

Let's find the value of

$$
\sum_{i=1}^{10} (2a_i-3b_i)
$$

First, we apply the sum rule:

$$
\begin{aligned}
∑_(i = 1)^(10)(2a_{i} - 3b_{i}) &= ∑_(i = 1)^(10)(2a_{i} + (-3b_{i})) \\
&= ∑_(i = 1)^(10)2a_{i} + ∑_(i = 1)^(10)(-3b_{i})
\end{aligned}
$$

Now, recall that for any constant $c$, we have

$$
\sum_{i=1}^{n} c a_i = c \cdot \sum_{i=1}^{n} a_i
$$

Applying the constant multiple rule to our two series, we finally arrive at

$$
\begin{aligned}
∑_(i = 1)^(10)2a_{i} + ∑_(i = 1)^(10)(-3b_{i}) &= 2 \cdot ∑_(i = 1)^(10)a_{i} - 3 \cdot ∑_(i = 1)^(10)b_{i} \\
&= 2 \cdot 5 - 3 \cdot 8 \\
&=-14
\end{aligned}
$$

---

<a id="evaluating-a-sum-using-finite-series-properties"></a>
## Evaluating a Sum Using Finite Series Properties

**Example:** Given that
$\displaystyle{\sum_{i=1}^{20} s_i} = -7$
and
$\displaystyle{\sum_{i=1}^{20} t_i} = 9$,
find the value of
$\displaystyle{\sum_{i=1}^{20} (10s_i+12t_i+5)}$.

**Explanation**

Recall the following properties of sums:

- $\displaystyle \sum_{i=1}^{n} (s_i+t_i) = \sum_{i=1}^{n} s_i + \sum_{i=1}^{n} t_i$
- $\displaystyle \sum_{i=1}^{n} c s_i = c \cdot \sum_{i=1}^{n} s_i$
- $\displaystyle \sum_{i=1}^{n} 1 = n$

By applying each property in turn, we obtain

$$
\begin{aligned}
∑_(i = 1)^(20)(10s_{i} + 12t_{i} + 5) &= ∑_(i = 1)^(20)10s_{i} + ∑_(i = 1)^(20)12t_{i} + ∑_(i = 1)^(20)5 \\
&= 10 \cdot ∑_(i = 1)^(20)s_{i} + 12 \cdot ∑_(i = 1)^(20)t_{i} + 5 \cdot ∑_(i = 1)^(20)1 \\
&= 10 \cdot (-7) + 12 \cdot 9 + 5 \cdot 20 \\
&= 138
\end{aligned}
$$

---

**Question 5**

```quiz
type: radio
id: q-5
content: |-
  If $∑_(i = 1)^(51)a_{i} = 2$ and $∑_(i = 1)^(51)b_{i} =-5$, then$∑_(i = 1)^(51)(a_{i} + b_{i}) =$
options:
- id: a
  content: |-
    $7$
- id: b
  content: |-
    $3$
- id: c
  correct: true
  content: |-
    $-3$
- id: d
  content: |-
    $-7$
- id: e
  content: |-
    $-10$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Given that
  
  $∑_(i = 1)^(24)a_{i} =-3$
  and
  $∑_(i = 1)^(24)b_{i} =-10$,
  find the value of
  $∑_(i = 1)^(24)(4a_{i} + 3b_{i})$.
options:
- id: a
  content: |-
    $-24$
- id: b
  content: |-
    $-13$
- id: c
  content: |-
    $-48$
- id: d
  content: |-
    $-49$
- id: e
  correct: true
  content: |-
    $-42$
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
