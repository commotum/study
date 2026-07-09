# The Nth Term of a Geometric Sequence

<!--
lesson-id: 680
topic-code: MF2.7.3.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Finding a Particular Term of a Geometric Sequence Given the First Term and Common Ratio](#finding-a-particular-term-of-a-geometric-sequence-given-the-first-term-and-common-ratio)
- [Finding a Formula for the Nth Term of a Geometric Sequence](#finding-a-formula-for-the-nth-term-of-a-geometric-sequence)
- [Finding a Particular Term of a Geometric Sequence Given a Term and the Common Ratio](#finding-a-particular-term-of-a-geometric-sequence-given-a-term-and-the-common-ratio)

## Prerequisites

- [The Product Rule for Exponents](<../../../../MA/Mathematical-Foundations/MF1/4. Exponents & Radicals/4.2. The Rules of Exponents/Lessons/4.2.1. The Product Rule for Exponents.md>)
- [The Recursive Formula for a Geometric Sequence](<../../../../MA/Mathematical-Foundations/MF2/7. Sequences/7.3. Geometric Sequences/Lessons/7.3.2. The Recursive Formula for a Geometric Sequence.md>)

---

<a id="introduction"></a>
## Introduction

The general formula for the $n$th term of a geometric sequence is

$$
a_n = a_1 \cdot r^{n-1}
$$

where $a_1$ is the first term and $r$ is the common ratio.

To illustrate how this works, suppose we want to find the $10$th term of the following geometric sequence:

$$
3, \: 6, \: 12, \: \ldots
$$

The first term is $a_1=3$, and the common ratio is $r=2$, so we can write the formula for the $n$th term of the sequence:

$$
\begin{aligned}
a_{n} &= a_{1} \cdot r^{n - 1} \\
&= 3 \cdot 2^{n - 1}
\end{aligned}
$$

To find the $10$th term, we can use this formula with

$$
n={\color{blue}10}
$$

$$
\begin{aligned}
a_{n} &= 3 \cdot 2^{n - 1} \\
a_{10} &= 3 \cdot 2^{10 - 1} \\
&= 3 \cdot 2^{9} \\
&= 3 \cdot 512 \\
&= 1536
\end{aligned}
$$

Therefore, the $10$th term is

$$
a_{10}=1\,536
$$

Using the formula was much quicker than writing out all $10$ terms of the sequence!

---

<a id="finding-a-particular-term-of-a-geometric-sequence-given-the-first-term-and-common-ratio"></a>
## Finding a Particular Term of a Geometric Sequence Given the First Term and Common Ratio

**Example:** The first term of a geometric sequence is $2$, and the common ratio is $3$. What is the $9$th term?

**Explanation**

The first term is $a_1=2$, and the common ratio is $r=3$, so we can write the formula for the $n$th term of the sequence:

$$
\begin{aligned}
a_{n} &= a_{1} \cdot r^{n - 1} \\
&= 2 \cdot 3^{n - 1}
\end{aligned}
$$

To find the $9$th term, we can use this formula with

$$
n={\color{blue}9}
$$

$$
\begin{aligned}
a_{n} &= 2 \cdot 3^{n - 1} \\
a_{9} &= 2 \cdot 3^{9 - 1} \\
&= 2 \cdot 3^{8} \\
&= 2 \cdot 6561 \\
&= 13122
\end{aligned}
$$

Therefore, the $9$th term is

$$
a_{9}=13\,122
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  The first term of a geometric sequence is $4$, and the common ratio is $3$. What is the $6$th term?
options:
- id: a
  content: |-
    $2916$
- id: b
  content: |-
    $1052$
- id: c
  content: |-
    $718$
- id: d
  content: |-
    $243$
- id: e
  content: |-
    $972$
  correct: true
```

---

**Question 2**

```quiz
type: radio
id: q-2
content: |-
  The first term of a geometric sequence is $32$ and the common ratio is $-\frac{1}{4}$. The $7$th term of this sequence is
options:
- id: a
  content: |-
    $\frac{1}{128}$
  correct: true
- id: b
  content: |-
    $-\frac{1}{128}$
- id: c
  content: |-
    $\frac{1}{64}$
- id: d
  content: |-
    $-\frac{1}{64}$
- id: e
  content: |-
    $\frac{1}{256}$
```

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  The first term of a geometric sequence is $5$, and the common ratio is $2$. What is the $10$th term?
options:
- id: a
  content: |-
    $512$
- id: b
  content: |-
    $1940$
- id: c
  content: |-
    $5120$
- id: d
  content: |-
    $2560$
  correct: true
- id: e
  content: |-
    $1280$
```

---

<a id="finding-a-formula-for-the-nth-term-of-a-geometric-sequence"></a>
## Finding a Formula for the Nth Term of a Geometric Sequence

**Example:** Find the formula for the $n$th term of a sequence if the $6$th term is $80$ and the common ratio is $-2$.

**Explanation**

The common ratio is $r=-2$, so we can start writing the formula for the $n$th term of the sequence:

$$
\begin{aligned}
a_{n} &= a_{1} \cdot r^{n - 1} \\
&= a_{1} \cdot (-2)^{n - 1}
\end{aligned}
$$

However, we still need to figure out the first term $a_1$. We know that the $6$th term is $a_6=80$, so we can solve for the first term as follows:

$$
\begin{aligned}
a_{6} &= a_{1} \cdot (-2)^{6 - 1} \\
80 &= a_{1} \cdot (-2)^{5} \\
80 &= a_{1} \cdot (-32) \\
- \frac{80}{32} &= a_{1} \\
- \frac{5}{2} &= a_{1}
\end{aligned}
$$

Now that we know the first term is

$$
a_1=-\dfrac{5}{2}
$$

we can complete the formula for the $n$th term of the sequence:

$$
\begin{aligned}
a_{n} &= a_{1} \cdot (-2)^{n - 1} \\
&=-\frac{5}{2} \cdot (-2)^{n - 1}
\end{aligned}
$$

We can simplify a bit further by manipulating the exponents, as follows:

$$
\begin{aligned}
a_{n} &= -\frac{5}{2}(-2)^{n - 1} \\
&= 5 \cdot (-\frac{1}{2}) \cdot (-2)^{n - 1} \\
&= 5 \cdot (-2)^{-1} \cdot (-2)^{n - 1} \\
&= 5 \cdot (-2)^{n - 2}
\end{aligned}
$$

---

**Question 4**

```quiz
type: radio
id: q-4
content: |-
  Find the formula for the $n$th term of a sequence if the $4$th term is $-135$ and the common ratio is $-3$.
options:
- id: a
  content: |-
    $a_{n} = 5(-3)^{n - 1}$
  correct: true
- id: b
  content: |-
    $a_{n} = -5(-3)^{n - 1}$
- id: c
  content: |-
    $a_{n} = 5(-3)^{n}$
- id: d
  content: |-
    $a_{n} = -135(-3)^{n - 1}$
- id: e
  content: |-
    $a_{n} = 15(-3)^{n - 1}$
```

---

**Question 5**

```quiz
type: radio
id: q-5
content: |-
  Consider the following geometric sequence.
  $6,-2, \frac{2}{3}, …$
  The formula for the $n$th term of this sequence is
options:
- id: a
  content: |-
    $a_{n} = 6\left(-\frac{1}{3}\right)^{n - 1}$
  correct: true
- id: b
  content: |-
    $a_{n} = 6\left(\frac{1}{3}\right)^{n - 1}$
- id: c
  content: |-
    $a_{n} = -2\left(-\frac{1}{3}\right)^{n - 1}$
- id: d
  content: |-
    $a_{n} = 6(-3)^{n - 1}$
- id: e
  content: |-
    $a_{n} = \frac{2}{3}\left(-\frac{1}{3}\right)^{n - 1}$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Find the formula for the $n$th term of the following geometric sequence.
  
  $\frac{1}{3},-1, 3, …$
options:
- id: a
  content: |-
    $a_{n} =-3^{n - 1}$
- id: b
  content: |-
    $a_{n} =-3^{n - 2}$
- id: c
  content: |-
    $a_{n} = (-3)^{n - 2}$
- id: d
  content: |-
    $a_{n} = - (-3)^{n - 2}$
  correct: true
- id: e
  content: |-
    $a_{n} = (-3)^{n - 1}$
```

---

<a id="finding-a-particular-term-of-a-geometric-sequence-given-a-term-and-the-common-ratio"></a>
## Finding a Particular Term of a Geometric Sequence Given a Term and the Common Ratio

**Example:** Given that the $5$th term of a geometric sequence is $9$, and the common ratio is $3$, find the second term.

**Explanation**

The common ratio is $r=3$, so we can start writing the formula for the $n$th term of the sequence:

$$
\begin{aligned}
a_{n} &= a_{1} \cdot r^{n - 1} \\
&= a_{1} \cdot 3^{n - 1}
\end{aligned}
$$

However, we still need to figure out the first term $a_1$. We know that the $5$th term is $a_5=9$, so we can solve for the first term as follows:

$$
\begin{aligned}
a_{5} &= a_{1} \cdot 3^{5 - 1} \\
9 &= a_{1} \cdot 3^{4} \\
9 &= a_{1} \cdot 81 \\
\frac{9}{81} &= a_{1} \\
\frac{1}{9} &= a_{1}
\end{aligned}
$$

Now that we know the first term is

$$
a_1=\dfrac{1}{9}
$$

we can complete the formula for the $n$th term of the sequence:

$$
\begin{aligned}
a_{n} &= a_{1} \cdot 3^{n - 1} \\
&= \frac{1}{9} \cdot 3^{n - 1}
\end{aligned}
$$

Then, we can use this formula to compute the second term:

$$
\begin{aligned}
a_{2} &= \frac{1}{9} \cdot 3^{2 - 1} \\
&= \frac{1}{9} \cdot 3 \\
&= \frac{1}{3}
\end{aligned}
$$

Therefore, the second term is

$$
a_2 = \dfrac{1}{3}
$$

---

**Question 7**

```quiz
type: radio
id: q-7
content: |-
  If the fifth term of a geometric sequence is $\frac{1}{8}$ and the common ratio is $\frac{1}{4}$, then the eighth term of this sequence is
options:
- id: a
  content: |-
    $\frac{1}{512}$
  correct: true
- id: b
  content: |-
    $\frac{1}{256}$
- id: c
  content: |-
    $\frac{1}{128}$
- id: d
  content: |-
    $\frac{1}{32}$
- id: e
  content: |-
    $\frac{1}{2048}$
```

---

**Question 8:**

```quiz
type: radio
id: q-8
content: |-
  Given that the $8$th term of a geometric sequence is $8$, and the common ratio is $\frac{1}{2}$, find the fifteenth term.
options:
- id: a
  content: |-
    $\frac{1}{32}$
- id: b
  content: |-
    $\frac{1}{16}$
  correct: true
- id: c
  content: |-
    $2$
- id: d
  content: |-
    $\frac{1}{8}$
- id: e
  content: |-
    $4$
```

---

**Question 9**

```quiz
type: radio
id: q-9
content: |-
  Find the formula for the $n$th term of a geometric sequence if the fourth term is $-\frac{2}{3}$ and the common ratio is $-2$.
options:
- id: a
  content: |-
    $a_{n} = \frac{1}{12}(-2)^{n - 1}$
  correct: true
- id: b
  content: |-
    $a_{n} = -\frac{1}{12}(-2)^{n - 1}$
- id: c
  content: |-
    $a_{n} = \frac{1}{12}(-2)^{n}$
- id: d
  content: |-
    $a_{n} = -\frac{2}{3}(-2)^{n - 1}$
- id: e
  content: |-
    $a_{n} = \frac{1}{6}(-2)^{n - 1}$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
