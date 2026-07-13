# Finding the Sum of an Arithmetic Series

<!--
lesson-id: 675
topic-code: MF3.1.2.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Finding the Sum of an Arithmetic Series Given the First and Last Terms](#finding-the-sum-of-an-arithmetic-series-given-the-first-and-last-terms)
- [Finding the Sum of an Arithmetic Series Given in Sigma Notation](#finding-the-sum-of-an-arithmetic-series-given-in-sigma-notation)
- [The Alternative Formula for the Sum of an Arithmetic Series](#the-alternative-formula-for-the-sum-of-an-arithmetic-series)
- [Finding the Sum of an Arithmetic Series Given the First Term and the Total Number of Terms](#finding-the-sum-of-an-arithmetic-series-given-the-first-term-and-the-total-number-of-terms)
- [Finding the Sum of an Arithmetic Series Given Two Terms](#finding-the-sum-of-an-arithmetic-series-given-two-terms)
- [Proof of the Sum Formula](#proof-of-the-sum-formula)

## Prerequisites

- [Expressing an Arithmetic Series in Sigma Notation](<../../../../MA/Mathematical-Foundations/MF3/1. Sequences and Series/1.2. Arithmetic Series/Lessons/1.2.1. Expressing an Arithmetic Series in Sigma Notation.md>)

---

<a id="introduction"></a>
## Introduction

Suppose we want to calculate the sum of the following arithmetic series:

$$
S_{10} = \sum_{n=1}^{10} \big(2n \big) = 2 + 4 + 6 + \cdots 16 + 18 + 20
$$

One way is to add up the terms individually, but that would take a long time.

There is an easier way. If we have an arithmetic series

$$
\displaystyle{S_N = \sum_{n=1}^N a_n}
$$

then we can calculate $S_N$ using the formula

$$
S_N = \frac{N}{2}(a_1+a_N)
$$

where $a_1$ is the first term, $a_N$ is the last term, and $N$ is the total number of terms.

For our series, we have $a_1=2$, $a_N= 20$, and $N=10$. Substituting these values into the formula for $S_N$, we obtain

$$
\begin{aligned}
S_{10} &= \frac{N}{2}(a_{1} + a_{N}) \\
&= \frac{10}{2}(2 + 20) \\
&= 5 \cdot 22 \\
&= 110
\end{aligned}
$$

**Note:** To see where the formula comes from, notice that we have $5$ pairs that add up to $22$:

$$
\begin{aligned}
a_{1} + a_{10} &= 2 + 20 = 22 \\
a_{2} + a_{9} &= 4 + 18 = 22 \\
a_{3} + a_{8} &= 6 + 16 = 22 \\
a_{4} + a_{7} &= 8 + 14 = 22 \\
a_{5} + a_{6} &= 10 + 12 = 22
\end{aligned}
$$

So, the sum is

$$
5 \cdot 22 = 110
$$

In general, the number of pairs is

$$
\dfrac{N}{2}
$$

and they all add up to the value of $(a_1 + a_N)$.

---

<a id="finding-the-sum-of-an-arithmetic-series-given-the-first-and-last-terms"></a>
## Finding the Sum of an Arithmetic Series Given the First and Last Terms

**Example:** Find the sum of the following arithmetic series:
$1+6+11+16+21+\cdots+101$

**Explanation**

To calculate the sum of an arithmetic series, we use the formula

$$
S_N = \frac{N}{2}(a_1+a_N)
$$

where $a_1$ is the first term, $a_N$ is the last term, and $N$ is the total number of terms.

For our series, we have $a_1=1$, and the common difference is

$$
\begin{aligned}
d &= a_{2} - a_{1} \\
&= 6 - 1 \\
&= 5
\end{aligned}
$$

So, the formula for the $n$th term is

$$
\begin{aligned}
a_{n} &= a_{1} + (n - 1)d \\
&= 1 + (n - 1)(5) \\
&= 1 + 5n - 5 \\
&= 5n - 4
\end{aligned}
$$

As we know, the last term is $a_N=101$. Putting this value in the formula for the $n$th term obtained above, we get

$$
\begin{aligned}
a_{N} &= 5N - 4 \\
101 &= 5N - 4 \\
105 &= 5N \\
N &= 21
\end{aligned}
$$

Finally, substituting $a_1=1$, $a_N = 101$, and $N=21$ into the formula for $S_N$, we obtain

$$
\begin{aligned} S_{21}&= \dfrac{21}{2}(1+101) \\[3pt] &= \dfrac{21}{2}\cdot 102 \\[5pt] &= 21\cdot 51 \\[5pt] &= 1\,071. \end{aligned}
$$

---

**Question 1**

```quiz
type: radio
id: q-1
content: |-
  > A calculator is required to answer this question.
  
  Find the sum of the following arithmetic series.
  $(-5) + (-2) + 1 + 4 + ⋯ + 28$
options:
- id: a
  content: |-
    $156$
- id: b
  content: |-
    $138$
  correct: true
- id: c
  content: |-
    $142$
- id: d
  content: |-
    $124$
- id: e
  content: |-
    $164$
```

---

**Question 2**

```quiz
type: radio
id: q-2
content: |-
  > A calculator is required to answer this question.
  
  The following arithmetic series has $11$ terms in total. Find the sum of the series.
  $$7 + 15 + 23 + 31 + ⋯ + 87$$
options:
- id: a
  content: |-
    $515$
- id: b
  content: |-
    $539$
- id: c
  content: |-
    $503$
- id: d
  content: |-
    $521$
- id: e
  content: |-
    $517$
  correct: true
```

---

<a id="finding-the-sum-of-an-arithmetic-series-given-in-sigma-notation"></a>
## Finding the Sum of an Arithmetic Series Given in Sigma Notation

**Example:** What is the sum of the arithmetic series $\displaystyle{\sum_{n=1}^{25} (2n + 1)}$?

**Explanation**

To calculate the sum of an arithmetic series, we use the formula

$$
S_N = \frac{N}{2}(a_1+a_N)
$$

where $a_1$ is the first term, $a_N$ is the last term, and $N$ is the total number of terms.

Given the series

$$
\displaystyle\sum_{n=1}^{25} (2n+1)
$$

in sigma notation, we note that

- the total number of terms is $N=25$,
- the first term is $a_1 = 2 \cdot 1 + 1= 3$, and
- the last term is $a_{25}= 2 \cdot 25 + 1 = 51$.

Substituting these values into the formula for the sum of an arithmetic series, we obtain

$$
\begin{aligned}
S_{25} &= \frac{25}{2}(3 + 51) \\
&= \frac{25}{2}(54) \\
&= 25 \cdot 27 \\
&= 675
\end{aligned}
$$

---

**Question 3**

```quiz
type: radio
id: q-3
content: |-
  > A calculator is required to answer this question.
  
  Calculate the sum of the arithmetic series $\displaystyle \sum_{n=0}^{10}(9n - 12)$.
options:
- id: a
  content: |-
    $432$
- id: b
  content: |-
    $816$
- id: c
  content: |-
    $224$
- id: d
  content: |-
    $363$
  correct: true
- id: e
  content: |-
    $672$
```

---

**Question 4**

```quiz
type: radio
id: q-4
content: |-
  > A calculator is required to answer this question.
  
  What is the sum of the arithmetic series $\displaystyle \sum_{n=1}^{11}(-5n)$?
options:
- id: a
  content: |-
    $-275$
- id: b
  content: |-
    $-550$
- id: c
  content: |-
    $-330$
  correct: true
- id: d
  content: |-
    $150$
- id: e
  content: |-
    $-660$
```

---

<a id="the-alternative-formula-for-the-sum-of-an-arithmetic-series"></a>
## The Alternative Formula for the Sum of an Arithmetic Series

So far, to calculate the sum of the first $N$ terms of an arithmetic series we have used the formula

$$
S_N = \frac{N}{2}(a_1 + a_N)
$$

where $a_1$ is the first term, $a_N$ is the last term, and $N$ is the number of terms.

Using the formula for the $n$th term

$$
\displaystyle{a_n = a_1 + (n-1)d}
$$

we can express the last term $a_N$ as

$$
a_N = a_1 + (N-1)d
$$

where $d$ is the common difference.

If we substitute this into our formula for $S_N$, we get

$$
\begin{aligned}
S_{N} &= \frac{N}{2}(a_{1} + a_{N}) \\
&= \frac{N}{2}(a_{1} + (a_{1} + (N - 1)d)) \\
&= \frac{N}{2}(a_{1} + a_{1} + (N - 1)d) \\
&= \frac{N}{2}(2a_{1} + (N - 1)d)
\end{aligned}
$$

This is a new formula for the sum.
So, we can also calculate $S_N$ for an arithmetic series using the formula

$$
S_N = \frac{N}{2}\big(2a_1+(N-1)d \big)
$$

With this formula, we can find the value of the sum without knowing the last term.

---

<a id="finding-the-sum-of-an-arithmetic-series-given-the-first-term-and-the-total-number-of-terms"></a>
## Finding the Sum of an Arithmetic Series Given the First Term and the Total Number of Terms

**Example:** Calculate the sum of the first $20$ terms of the following arithmetic series:
$5+11+17+23+\cdots$

**Explanation**

To calculate the sum of an arithmetic series, we use the formula

$$
S_N = \frac{N}{2}\big(2a_1+(N-1)d \big)
$$

where $a_1$ is the first term, $d$ is the common difference, and $N$ is the number of terms.

We are given that the total number of terms $N=20$ and the first term is $a_1=5$. Now, the common difference $d$ can be found as follows:

$$
\begin{aligned}
d &= a_{2} - a_{1} \\
&= 11 - 5 \\
&= 6
\end{aligned}
$$

Substituting $a_1=5$, $d=6$, and $N=20$ into the above formula for $S_N$, we obtain

$$
\begin{aligned}
S_{20} &= \frac{N}{2}(2a_{1} + (N - 1)d) \\
&= \frac{20}{2}(2 \cdot 5 + (20 - 1) \cdot 6) \\
&= 10 \cdot (10 + 114) \\
&= 10 \cdot 124 \\
&= 1240
\end{aligned}
$$

---

**Question 5**

```quiz
type: radio
id: q-5
content: |-
  > A calculator is required to answer this question.
  
  Calculate the sum of the first $30$ terms of the following arithmetic series.
  $\frac{1}{2} + \frac{3}{2} + \frac{5}{2} + \frac{7}{2} + ⋯$
options:
- id: a
  content: |-
    $460$
- id: b
  content: |-
    $452$
- id: c
  content: |-
    $448$
- id: d
  content: |-
    $455$
- id: e
  content: |-
    $450$
  correct: true
```

---

**Question 6**

```quiz
type: radio
id: q-6
content: |-
  > A calculator is required to answer this question.
  
  Calculate the sum of the first $10$ terms of the following arithmetic series.
  $2 + 7 + 12 + ⋯$
options:
- id: a
  content: |-
    $245$
  correct: true
- id: b
  content: |-
    $252$
- id: c
  content: |-
    $212$
- id: d
  content: |-
    $249$
- id: e
  content: |-
    $235$
```

---

<a id="finding-the-sum-of-an-arithmetic-series-given-two-terms"></a>
## Finding the Sum of an Arithmetic Series Given Two Terms

**Example:** An arithmetic series has $a_3=7$ and $a_{8}=17$, where $a_3$ and $a_{8}$ are the third and eighth terms of the series, respectively.
Find the sum of the first $7$ terms of the series.

**Explanation**

To calculate the sum of an arithmetic series, we use the formula

$$
S_N = \frac{N}{2}\big(2a_1+(N-1)d \big)
$$

where $a_1$ is the first term, $d$ is the common difference, and $N$ is the number of terms.

Since we know two terms of the arithmetic series, we can find its common difference as follows:

$$
\begin{aligned}
d &= \frac{a_{8} - a_{3}}{8 - 3} \\
&= \frac{17 - 7}{8 - 3} \\
&= \frac{10}{5} \\
&= 2
\end{aligned}
$$

We know that $a_{3}=7$, so we can use the formula for the $n$th term to compute $a_1$, as follows:

$$
\begin{aligned}
a_{n} &= a_{1} + (n - 1)d \\
a_{3} &= a_{1} + (3 - 1) \cdot 2 \\
7 &= a_{1} + 4 \\
a_{1} &= 3
\end{aligned}
$$

Substituting $a_1=3$, $d=2$, and $N=7$ into the above formula for $S_N$, we obtain

$$
\begin{aligned}
S_{7} &= \frac{N}{2}(2a_{1} + (N - 1)d) \\
&= \frac{7}{2}(2 \cdot 3 + (7 - 1) \cdot 2) \\
&= \frac{7}{2} \cdot (6 + 12) \\
&= \frac{7}{2} \cdot 18 \\
&= 7 \cdot 9 \\
&= 63
\end{aligned}
$$

---

**Question 7**

```quiz
type: radio
id: q-7
content: |-
  > A calculator is required to answer this question.
  
  An arithmetic series has $a_{5} = 30$ and $a_{12} = 65$, where $a_{5}$ and $a_{12}$ are the fifth and twelfth terms of the series, respectively.
  Find the sum of the first $10$ terms of the series.
options:
- id: a
  content: |-
    $260$
- id: b
  content: |-
    $365$
- id: c
  content: |-
    $325$
  correct: true
- id: d
  content: |-
    $315$
- id: e
  content: |-
    $395$
```

---

**Question 8**

```quiz
type: radio
id: q-8
content: |-
  > A calculator is required to answer this question.
  
  An arithmetic series has $a_{1} =-1$ and $a_{3} = 7$, where $a_{1}$ and $a_{3}$ are the first and third terms of the series, respectively. What is the sum of the first $12$ terms of the series?
options:
- id: a
  content: |-
    $288$
- id: b
  content: |-
    $204$
- id: c
  content: |-
    $252$
  correct: true
- id: d
  content: |-
    $512$
- id: e
  content: |-
    $342$
```

---

<a id="proof-of-the-sum-formula"></a>
## Proof of the Sum Formula

The sum of the first $N$ terms of an arithmetic series with the initial term $a_1$ and the common difference $d$ can be found as

$$
S_N = \frac{N}{2}\big(2a_1+(N-1)d \big)
$$

We'll now prove this result.

First, we recall that the $n$th term of the series is given by

$$
a_n = a_1 + (n-1)d
$$

Let's write down the sum by placing the indices

$$
n=1,2,3,\ldots, N
$$

in ascending order:

$$
\begin{aligned}
S_{N} &= a_{1} + a_{2} + ⋯ + a_{N - 1} + a_{N} \\
&= a_1+\underbrace{(a_1+d)}_{a_2}+\cdots+\underbrace{(a_1+(N-2)d)}_{a_{N-1}}+\underbrace{(a_1+(N-1)d)}_{a_N}
\end{aligned}
$$

Now, let's write down the same sum but place the indices in descending order:

$$
\begin{aligned}
S_{N} &= a_{N} + a_{N - 1} + ⋯ + a_{2} + a_{1} \\
&= \underbrace{(a_1+(N-1)d)}_{a_N}+\underbrace{(a_1+(N-2)d)}_{a_{N-1}}+\cdots+\underbrace{(a_1+d)}_{a_2}+a_1
\end{aligned}
$$

By adding the two expressions, we get the following:

$$
\begin{aligned}
\begin{bmatrix}S_{N} &= & a_{1} & + & (a_{1} + d) & + & ⋯ & + & (a_{1} + (N - 1)d) \\ S_{N}= & (a_{1} + (N - 1)d) & + & (a_{1} + (N - 2)d) & + & ⋯ & + & a_{1} \\ 2S_{N}= & (2a_{1} + (N - 1)d) & + & (2a_{1} + (N - 1)d) & + & ⋯ & + & (2a_{1} + (N - 1)d)\end{bmatrix}
\end{aligned}
$$

The expression on the right contains $N$ copies of $2a_1+(N-1)d$. Therefore,

$$
2S_{N} = N \cdot (2a_{1} + (N - 1)d)⟹S_{N} = \frac{N}{2}(2a_{1} + (N - 1)d)
$$

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
