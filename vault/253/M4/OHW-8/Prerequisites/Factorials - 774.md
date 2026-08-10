# Factorials

<!--
lesson-id: 774
topic-code: MF2.14.3.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Evaluating Factorials](#evaluating-factorials)
- [Evaluating the Factorial of Zero](#evaluating-the-factorial-of-zero)
- [Simplifying Rational Expressions that Contain Factorials](#simplifying-rational-expressions-that-contain-factorials)
- [Evaluating a Quotient of Factorials](#evaluating-a-quotient-of-factorials)

## Prerequisites

- [Simplifying Rational Expressions](<../../../../MA/Mathematical-Foundations/MF1/7. Radical & Rational Expressions/7.2. Rational Expressions/Lessons/7.2.2. Simplifying Rational Expressions.md>)

---

<a id="introduction"></a>
## Introduction

The **factorial** of a natural number is the product of the number and all of the natural numbers below it. The factorial of a number is denoted by placing an exclamation point after the number.

For example, the factorial of $4$ is written as $4$! (with an exclamation point after the $4$), and is computed as

$$
4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24
$$

So, we say that "four factorial is twenty-four".

The factorials of the natural numbers $1$ through $5$ are as follows:

$$
\begin{aligned} 1! &= 1 \\[5pt] 2! &= 2 \cdot 1 = 2 \\[5pt] 3! &= 3 \cdot 2 \cdot 1 = 6 \\[5pt] 4! &= 4 \cdot 3 \cdot 2 \cdot 1 = 24 \\[5pt] 5! &= 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120 \end{aligned}
$$

Note that the factorial of $0$ is defined to be equal to $1$:

$$
0! = 1
$$

---

<a id="evaluating-factorials"></a>
## Evaluating Factorials

**Example:** $5!\,2!=$

**Explanation**

The given expression is a product of two factorials.

- Computing $5$! using the definition, we get
$5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$.
- Computing $2$! using the definition, we get
$2! = 2 \cdot 1 = 2$.

Finally, we can evaluate the given expression:

$$
\begin{aligned}
5!2! &= 5! \cdot 2! \\
&= 120 \cdot 2 \\
&= 240
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-5370
content: |-
  What is $5!$?
options:
- id: a
  correct: true
  content: |-
    $120$
- id: b
  content: |-
    $5$
- id: c
  content: |-
    $40$
- id: d
  content: |-
    $60$
- id: e
  content: |-
    $25$
```

---

**Question 2:**

```quiz
type: radio
id: ma-73002
content: |-
  What is $2!3!$?
options:
- id: a
  correct: true
  content: |-
    $12$
- id: b
  content: |-
    $8$
- id: c
  content: |-
    $24$
- id: d
  content: |-
    $18$
- id: e
  content: |-
    $6$
```

---

<a id="evaluating-the-factorial-of-zero"></a>
## Evaluating the Factorial of Zero

**Example:** Calculate $\dfrac{5!}{0!}$.

**Explanation**

The given expression is a quotient of two factorials.

- Computing $5$! using the definition, we get
$5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$.
- By definition, the factorial of zero equals one:
$0! = 1$

Finally, we can evaluate the given expression:

$$
\begin{aligned}
\frac{5!}{0!} &= \frac{120}{1} = 120
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: ma-124137
content: |-
  What is $3! + 0!$?
options:
- id: a
  content: |-
    $3$
- id: b
  content: |-
    Undefined
- id: c
  content: |-
    $6$
- id: d
  content: |-
    $4$
- id: e
  correct: true
  content: |-
    $7$
```

---

**Question 4:**

```quiz
type: radio
id: ma-124138
content: |-
  What is $\frac{2!}{0!}$?
options:
- id: a
  content: |-
    $0$
- id: b
  content: |-
    $6$
- id: c
  correct: true
  content: |-
    $2$
- id: d
  content: |-
    $1$
- id: e
  content: |-
    Undefined
```

---

<a id="simplifying-rational-expressions-that-contain-factorials"></a>
## Simplifying Rational Expressions that Contain Factorials

One way to simplify a rational expression containing factorials is to calculate the numerator and denominator separately, and then divide the results.

For example, computing

$$
\dfrac{10!}{8!}
$$

using this method, we get

$$
\begin{aligned} \dfrac {10!}{8!} &= \dfrac {10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} {8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = \dfrac {3\,628\,800} {40\,320} = 90. \end{aligned}
$$

However, the method above involves lots of computations. Thankfully, there's an easier way!

Before we multiply, we can cancel out any numbers that appear in both the numerator and denominator, thereby reducing the amount of computation that's needed. Using this method, we get the same result with far fewer computations:

$$
\require{cancel} \begin{aligned} \dfrac {10!}{8!} &= \dfrac {10 \cdot 9 \cdot \cancel{8} \cdot \cancel{7} \cdot \cancel{6} \cdot \cancel{5} \cdot \cancel{4} \cdot \cancel{3} \cdot \cancel{2} \cdot \cancel{1}} {\cancel{8} \cdot \cancel{7} \cdot \cancel{6} \cdot \cancel{5} \cdot \cancel{4} \cdot \cancel{3} \cdot \cancel{2} \cdot \cancel{1}} = \dfrac{10 \cdot 9}{1} = 90 \end{aligned}
$$

Even quicker, we could just realize that

$$
10! = 10 \cdot 9 \cdot 8
$$

and then cancel the $8$! that appears in both the numerator and the denominator:

$$
\require{cancel} \dfrac {10!}{8!} = \dfrac {10 \cdot 9 \cdot \cancel{8!}} {\cancel{8!}} = \dfrac {10 \cdot 9} {1} = 90
$$

---

<a id="evaluating-a-quotient-of-factorials"></a>
## Evaluating a Quotient of Factorials

**Example:** Evaluate $\dfrac {5!} {2!}$.

**Explanation**

First, notice that

$$
5! = 5 \cdot 4 \cdot 3 \cdot 2! \,
$$

Then, we can cancel the $2$! that occurs in both the numerator and the denominator:

$$
\require{cancel} \begin{aligned} \dfrac {5!} {2!} &= \dfrac {5 \cdot 4 \cdot 3 \cdot 2!} {2!} \\[5pt] &= \dfrac {5 \cdot 4 \cdot 3 \cdot \cancel{2!}} {\cancel{2!}} \\[5pt] &= \dfrac {5 \cdot 4 \cdot 3} {1} \\[5pt] &= 60 \end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: ma-19838
content: |-
  Simplify $\frac{7!3!}{4!2!}$.
options:
- id: a
  content: |-
    $90$
- id: b
  content: |-
    $145$
- id: c
  content: |-
    $210$
- id: d
  correct: true
  content: |-
    $630$
- id: e
  content: |-
    $126$
```

---

**Question 6:**

```quiz
type: radio
id: ma-5371
content: |-
  Evaluate $\frac{6!}{3!}$.
options:
- id: a
  correct: true
  content: |-
    $120$
- id: b
  content: |-
    $9$
- id: c
  content: |-
    $18$
- id: d
  content: |-
    $20$
- id: e
  content: |-
    $2$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
