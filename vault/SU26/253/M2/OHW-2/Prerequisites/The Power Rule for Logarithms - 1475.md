# The Power Rule for Logarithms

<!--
lesson-id: 1475
topic-code: MF2.5.2.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Simplifying the Logarithm of a Power Function Using the Power Rule](#simplifying-the-logarithm-of-a-power-function-using-the-power-rule)
- [Writing an Expression as the Logarithm of a Power Function Using the Power Rule](#writing-an-expression-as-the-logarithm-of-a-power-function-using-the-power-rule)
- [Evaluating an Expression Using the Power Rule](#evaluating-an-expression-using-the-power-rule)

## Prerequisites

- [Simplifying Logarithmic Expressions](<../../../../MA/Mathematical-Foundations/MF2/5. Exponentials & Logarithms/5.1. Introduction to Logarithms/Lessons/5.1.6. Simplifying Logarithmic Expressions.md>)

---

<a id="introduction"></a>
## Introduction

The **power rule** allows us to simplify logarithms of exponentiated expressions. It states that

$$
\log_{n}\left(c^{\color{blue}m} \right) = {\color{blue}m}\log_{n}{c}
$$

In other words, the logarithm has the effect of "bringing down the power."

For example, let's use the rule to simplify

$$
\log\left(125\right)
$$

$$
\begin{aligned}
\log (125) &= \log (5^{3}) \\
&= 3\log (5)
\end{aligned}
$$

**Note:** To understand why the power rule works, notice that we can reach the same result using the product rule:

$$
\begin{aligned}
\log (125) &= \log (5^{3}) \\
&= \log (5 \cdot 5 \cdot 5) \\
&= \log (5) + \log (5) + \log (5) \\
&= 3\log (5)
\end{aligned}
$$

The power rule is just a shortcut for the above procedure.

---

<a id="simplifying-the-logarithm-of-a-power-function-using-the-power-rule"></a>
## Simplifying the Logarithm of a Power Function Using the Power Rule

**Example:** By expressing $\ln\left(x^2\right)$ in the form $k\ln x$, determine the value of $k$.

**Explanation**

First, let's recall the power rule for logarithms:

$$
\log_n(c^m)= m\log_n\left(c \right)
$$

Using the power rule for logarithms, we get

$$
\begin{aligned}
\ln (x^{2}) &= 2\ln x
\end{aligned}
$$

Therefore, $k =2$.

---

**Question 1:**

```quiz
type: radio
id: ma-47223
content: |-
  By expressing $\log (81)$ in the form $k\log (3)$, determine the value of $k$.
options:
- id: a
  content: |-
    $9$
- id: b
  content: |-
    $\frac{1}{2}$
- id: c
  content: |-
    $2$
- id: d
  content: |-
    $\frac{1}{4}$
- id: e
  content: |-
    $4$
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: ma-66865
content: |-
  What is $\log (x^{3})$?
options:
- id: a
  content: |-
    $-\frac{1}{3}\log (3x)$
- id: b
  content: |-
    $\frac{1}{3}\log x$
- id: c
  content: |-
    $3\log x$
  correct: true
- id: d
  content: |-
    $\log (3x)$
- id: e
  content: |-
    $-3\log x$
```

---

<a id="writing-an-expression-as-the-logarithm-of-a-power-function-using-the-power-rule"></a>
## Writing an Expression as the Logarithm of a Power Function Using the Power Rule

**Example:** By expressing $\dfrac{1}{2}\log_3{x}$ in the form $\log_3 \left(x^k\right)$, determine the value of $k$.

**Explanation**

First, let's recall the power rule for logarithms:

$$
\log_n(c^m)= m\log_n\left(c \right)
$$

Using the power rule for logarithms, we get

$$
\begin{aligned}
\frac{1}{2}\log_{3} x &= \log_{3} (x^{1/2})
\end{aligned}
$$

Therefore,

$$
k = \dfrac{1}{2}
$$

---

**Question 3:**

```quiz
type: radio
id: ma-47222
content: |-
  By expressing $3\ln (4)$ in the form $\ln (N)$, determine the value of $N$.
options:
- id: a
  content: |-
    $256$
- id: b
  content: |-
    $64$
  correct: true
- id: c
  content: |-
    $12$
- id: d
  content: |-
    $48$
- id: e
  content: |-
    $96$
```

---

**Question 4:**

```quiz
type: radio
id: ma-47220
content: |-
  By expressing $\frac{5}{2}\log_{2} t$ in the form $\log_{2} (t^{k})$, determine the value of $k$.
options:
- id: a
  content: |-
    $\frac{5}{2}$
  correct: true
- id: b
  content: |-
    $-\frac{2}{5}$
- id: c
  content: |-
    $\frac{5}{4}$
- id: d
  content: |-
    $\frac{2}{5}$
- id: e
  content: |-
    $-\frac{5}{2}$
```

---

<a id="evaluating-an-expression-using-the-power-rule"></a>
## Evaluating an Expression Using the Power Rule

**Example:** Find the value of $\ln\left(x^3\right)$ if $\ln(x) = 0.2$.

**Explanation**

First, let's recall the power rule for natural logarithms:

$$
\ln\left(c^m \right) = m\ln{c}
$$

Using the power rule for logarithms and the information given, we get

$$
\begin{aligned}
\ln (x^{3}) &= 3 \cdot \ln (x) \\
&= 3 \cdot 0.2 \\
&= 0.6
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: ma-25946
content: |-
  Find the value of $\log_{z} (\frac{1}{4})$ if $\log_{z} (4) = 0.6$.
options:
- id: a
  content: |-
    $-1.2$
- id: b
  content: |-
    $-0.6$
  correct: true
- id: c
  content: |-
    $0.6$
- id: d
  content: |-
    $0.3$
- id: e
  content: |-
    $-1.8$
```

---

**Question 6:**

```quiz
type: radio
id: ma-47238
content: |-
  If $\log (x) = 3$, what is $\log (x^{3})$?
options:
- id: a
  content: |-
    $18$
- id: b
  content: |-
    $81$
- id: c
  content: |-
    $6$
- id: d
  content: |-
    $27$
- id: e
  content: |-
    $9$
  correct: true
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
