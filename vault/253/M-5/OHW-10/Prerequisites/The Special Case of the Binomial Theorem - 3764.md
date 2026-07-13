# The Special Case of the Binomial Theorem

<!--
lesson-id: 3764
topic-code: MF3.1.1.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Expanding a Binomial](#expanding-a-binomial)
- [Expanding a Binomial With Negative Coefficients](#expanding-a-binomial-with-negative-coefficients)
- [Calculating a Coefficient of a Binomial Expansion](#calculating-a-coefficient-of-a-binomial-expansion)
- [Deriving the Special Case From the General Binomial Theorem](#deriving-the-special-case-from-the-general-binomial-theorem)

## Prerequisites

- [Expanding a Binomial Using Binomial Coefficients](<../../../../MA/Mathematical-Foundations/MF3/1. Sequences and Series/1.1. The Binomial Theorem/Lessons/1.1.2. Expanding a Binomial Using Binomial Coefficients.md>)

---

<a id="introduction"></a>
## Introduction

Let's recall the binomial theorem for positive integer $n$:

$$
{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \cdots + {n \choose n}{a^0}{b^n}
$$

If we substitute $a=1$ and $b=x$ into the binomial theorem, we obtain (after some manipulations)

$$
{(1 + x)^n} = 1 + nx + \dfrac{{n(n - 1)}}{{2!}}{x^2} + \dfrac{{n(n - 1)(n - 2)}}{{3!}}{x^3} +\cdots + x^n
$$

We'll derive this result at the end of the lesson.

It's often useful to use this version of the binomial formula whenever there is only one variable and the other term equals $1$.

---

<a id="expanding-a-binomial"></a>
## Expanding a Binomial

**Example:** Find the first $3$ terms in ascending powers of $a$ of the binomial expansion of $(1+3a)^5$.

**Explanation**

The first $3$ terms of the binomial expansion for ${(1 + x)^n}$ are given by

$$
{(1 + x)^n} = 1 + nx + \frac{{n(n - 1)}}{{2!}}{x^2} + \cdots
$$

By substituting $x=3a$ and $n=5$ into the above formula, we obtain

$$
\begin{aligned}
(1 + 3a)^{5} &= 1 + 5(3a) + (5(5 - 1))/(2!)(3a)^{2} + ⋯ \\
&= 1 + 5(3a) + (5(4))/(2)(9a^{2}) + ⋯ \\
&= 1 + 15a + 90a^{2} + ⋯
\end{aligned}
$$

---

**Question 1**

```quiz
type: radio
id: ma-12960
content: |-
  > A calculator is required to answer this question.
  
  $(1 + 6t)^{7} =$
options:
- id: a
  content: |-
    $1 + 42t + 728t^{2} + ⋯$
- id: b
  content: |-
    $1 + 42t + 756t^{2} + ⋯$
  correct: true
- id: c
  content: |-
    $1 + 42t + 360t^{2} + ⋯$
- id: d
  content: |-
    $1 + 42t + 724t^{2} + ⋯$
- id: e
  content: |-
    $1 + 42t + 740t^{2} + ⋯$
```

---

**Question 2**

```quiz
type: free
id: ma-234001
content: |-
  > A calculator is required to answer this question.
  
  What are the first three terms in ascending powers of $t$ of $(1 + \frac{t}{5})^{10}$?

  Enter the coefficients of $t$ and $t^2$, separated by a comma.
correct: |-
  2, 9/5
```

---

<a id="expanding-a-binomial-with-negative-coefficients"></a>
## Expanding a Binomial With Negative Coefficients

**Example:** Find the first $3$ terms in ascending powers of $m$ of the binomial expansion of $\left(1 - \dfrac{4m}{3}\right)^7$.

**Explanation**

The first $3$ terms of the binomial expansion for ${(1 + x)^n}$ are given by

$$
{(1 + x)}^n = 1 + nx + \frac{{n(n - 1)}}{{2!}}{x^2} + \cdots
$$

By substituting

$$
x=-\dfrac{4m}{3}
$$

and $n=7$ into the above formula, we obtain

$$
\begin{aligned}
(1 - \frac{4m}{3})^{7} &= 1 + 7(-\frac{4m}{3}) + (7(7 - 1))/(2!)(-\frac{4m}{3})^{2} + ⋯ \\
&= 1 + 7(-\frac{4m}{3}) + (7(6))/(2)(-\frac{4m}{3})^{2} + ⋯ \\
&= 1 + 7(-\frac{4m}{3}) + (7(6))/(2)(\frac{16m^{2}}{9}) + ⋯ \\
&= 1 - \frac{28m}{3} + \frac{112m^{2}}{3} + ⋯
\end{aligned}
$$

---

**Question 3**

```quiz
type: free
id: ma-234002
content: |-
  > A calculator is required to answer this question.
  
  Find, in ascending powers of $t$, the **first three terms** in the binomial expansion of $(1 - 8t)^{6}$.
correct: |-
  1 - 48t + 960t^2
```

---

**Question 4**

```quiz
type: radio
id: ma-18163
content: |-
  > A calculator is required to answer this question.
  
  $(1 - \frac{a}{2})^{5} =$
options:
- id: a
  content: |-
    $1 - \frac{5a}{2} + \frac{5a^{2}}{2} + ⋯$
  correct: true
- id: b
  content: |-
    $1 + \frac{5a}{2} + \frac{5a^{2}}{2} + ⋯$
- id: c
  content: |-
    $1 - \frac{5a}{2} + \frac{5a^{2}}{4} + ⋯$
- id: d
  content: |-
    $1 - \frac{5a}{2} + \frac{a^{2}}{2} + ⋯$
- id: e
  content: |-
    $1 + \frac{5a}{2} + \frac{a^{2}}{2} + ⋯$
```

---

<a id="calculating-a-coefficient-of-a-binomial-expansion"></a>
## Calculating a Coefficient of a Binomial Expansion

**Example:** Determine the coefficient of $r^3$ in the expansion of $\left(1 - 3r \right)^{10}$.

**Explanation**

The binomial expansion for $(1 + x)^n$ is given by

$$
(1 + x)^n = 1 + nx + \frac{n(n - 1)}{2!} x^2 + \cdots
$$

In particular, the $x^3$ term is given by

$$
\dfrac{n(n-1)(n-2)}{3!} x^3
$$

Replacing $x$ with $-3r$ and $n$ with $10$ in the above expression, we get

$$
\begin{aligned}
(10(10 - 1)(10 - 2))/(3!)(-3r)^{3} &= (10(9)(8))/(6) \cdot (-3)^{3} \cdot r^{3} \\
&= (10(9)(8))/(6) \cdot (-27)r^{3} \\
&=-3240r^{3}
\end{aligned}
$$

Therefore, the coefficient of $r^3$ is $-3\,240$.

---

**Question 5**

```quiz
type: radio
id: ma-18615
content: |-
  > A calculator is required to answer this question.
  
  The coefficient of $x^{3}$ in the expansion of $(1 + 2x)^{17}$ is
options:
- id: a
  content: |-
    $4575$
- id: b
  content: |-
    $5440$
  correct: true
- id: c
  content: |-
    $5250$
- id: d
  content: |-
    $5320$
- id: e
  content: |-
    $4440$
```

---

**Question 6**

```quiz
type: free
id: ma-250997
content: |-
  > A calculator is required to answer this question.
  
  What is the coefficient of $k^{4}$ in the expansion of $(1 - 4k)^{6}$?
correct: |-
  3840
```

---

<a id="deriving-the-special-case-from-the-general-binomial-theorem"></a>
## Deriving the Special Case From the General Binomial Theorem

Let's derive our special case formula from the binomial theorem for positive integer $n$:

$$
{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + {n \choose 3}{a^{n - 3}}{b^3} + \cdots + {n \choose n}{a^0}{b^n}
$$

Substituting $a=1$ and $b=x$ into the above, we get the following:

$$
\begin{aligned}
(1 + x)^{n} &= (\frac{n}{0}) \cdot 1^{n} \cdot x^{0} + (\frac{n}{1}) \cdot 1^{n - 1} \cdot x^{1} + (\frac{n}{2}) \cdot 1^{n - 2} \cdot x^{2} + ⋯ + (\frac{n}{n}) \cdot 1^{0} \cdot x^{n} \\
&= (\frac{n}{0}) + (\frac{n}{1})x + (\frac{n}{2})x^{2} + (\frac{n}{3})x^{3} + ⋯ + (\frac{n}{n})x^{n}
\end{aligned}
$$

Now, recall that

$$
{n \choose r} = \dfrac{n!}{(n-r)!\cdot r!}
$$

and the particular cases

$$
{n \choose 0} = 1, \qquad {n \choose 1} = n
$$

We can now continue to simplify our binomial expansion as follows:

$$
\begin{aligned}
(1 + x)^{n} &= (\frac{n}{0}) + (\frac{n}{1})x + (\frac{n}{2})x^{2} + (\frac{n}{3})x^{3} + ⋯ + (\frac{n}{n})x^{n} \\
&= 1 + n \cdot x + (n!)/((n - 2)! \cdot 2!) \cdot x^{2} + (n!)/((n - 3)! \cdot 3!) \cdot x^{3} + ⋯ + x^{n} \\
&= 1 + n \cdot x + (n(n - 1)(n - 2)!)/((n - 2)! \cdot 2!) \cdot x^{2} + (n(n - 1)(n - 2)(n - 3)!)/((n - 3)! \cdot 3!) \cdot x^{3} + ⋯ + x^{n} \\
&= 1 + n \cdot x + (n(n - 1)(n - 2)!)/((n - 2)! \cdot 2!) \cdot x^{2} + (n(n - 1)(n - 2)(n - 3)!)/((n - 3)! \cdot 3!) \cdot x^{3} + ⋯ + x^{n} \\
&= 1 + nx + (n(n - 1))/(2!)x^{2} + (n(n - 1)(n - 2))/(3!)x^{3} + ⋯ + x^{n}
\end{aligned}
$$

which gives the desired result.

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
