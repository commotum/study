# The Recursive Formula for a Geometric Sequence

<!--
lesson-id: 1818
topic-code: MF2.7.3.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Constructing a Recursive Formula for a Geometric Sequence](#constructing-a-recursive-formula-for-a-geometric-sequence)
- [Calculating a Term of a Geometric Sequence Given Its Recursive Formula](#calculating-a-term-of-a-geometric-sequence-given-its-recursive-formula)
- [Calculating a Term of a Geometric Sequence Given a Recursive Formula in Function Notation](#calculating-a-term-of-a-geometric-sequence-given-a-recursive-formula-in-function-notation)
- [Identifying Geometric Sequences](#identifying-geometric-sequences)

## Prerequisites

- [Introduction to Geometric Sequences](<../../../../MA/Mathematical-Foundations/MF2/7. Sequences/7.3. Geometric Sequences/Lessons/7.3.1. Introduction to Geometric Sequences.md>)
- [Recursive Sequences](<../../../../MA/Mathematical-Foundations/MF2/7. Sequences/7.1. Introduction to Sequences/Lessons/7.1.2. Recursive Sequences.md>)

---

<a id="introduction"></a>
## Introduction

The **recursive formula for a geometric sequence** with common ratio $r$ takes the form

$$
a_{n+1} = r \cdot a_{n}
$$

The above formula states that to get to the next term in the sequence, we multiply the previous term by $r$.

To illustrate, consider the geometric sequence below:

$$
1, \: 3, \: 9, \: 27, \: \dots
$$

The first term is $a_1=1$, and we can calculate the common ratio $r$ as

$$
r = \dfrac{a_2}{a_1} = \dfrac 3 1 = 3
$$

Therefore, the recursive formula is

$$
a_{n+1} = 3 \cdot a_{n}, \qquad a_1 = 1, \qquad n\geq 1
$$

When writing out our final answer for the recursive formula, we should also state the first term and the range for $n$.

To check that the recursive formula is correct, we can use it to generate the next few terms of the series:

$$
\begin{aligned}
a_{2} &= 3 \cdot a_{1} = 3 \cdot 1 = 30✓ \\
a_{3} &= 3 \cdot a_{2} = 3 \cdot 3 = 90✓ \\
a_{4} &= 3 \cdot a_{3} = 3 \cdot 9 = 27✓
\end{aligned}
$$

---

<a id="constructing-a-recursive-formula-for-a-geometric-sequence"></a>
## Constructing a Recursive Formula for a Geometric Sequence

**Example:** What is the recursive formula for the following geometric sequence?
$1, \: 4, \: 16, \: \ldots$

**Explanation**

The recursive formula for a geometric sequence with common ratio $r$ takes the form

$$
a_{n+1} = r \cdot a_{n}
$$

In this case, the first term is

$$
a_1={\color{blue}1}
$$

and we can calculate the common ratio $r$ as

$$
r = \dfrac{a_2}{a_1} = \dfrac 4 1 = {\color{red}4}
$$

Therefore, the recursive formula is

$$
a_{n+1} = {\color{red}4} \cdot a_{n}, \qquad a_1 = {\color{blue}1}, \qquad n\geq 1
$$

---

**Question 1:**

```quiz
type: radio
id: ma-44818
content: |-
  What is the recursive formula for the following geometric sequence?
  
  $2, 6, 18, …$
options:
- id: a
  content: |-
    $a_{n + 1} = 2a_{n}, a_{1} = 1, n \ge 1$
- id: b
  content: |-
    $a_{n + 1} = \frac{a_{n}}{3}, a_{1} = 2, n \ge 1$
- id: c
  content: |-
    $a_{n + 1} = a_{n} + 2, a_{1} = 1, n \ge 1$
- id: d
  content: |-
    $a_{n + 1} = a_{n} + 3, a_{1} = 2, n \ge 1$
- id: e
  content: |-
    $a_{n + 1} = 3a_{n}, a_{1} = 2, n \ge 1$
  correct: true
```

---

**Question 2**

```quiz
type: free
id: ma-249792
content: |-
  Consider the following geometric sequence:
  $100, 80, 64, …$
  
  The recursive formula for this geometric sequence is

  Enter the expression to the right of $a_{n+1}=$ and the value of $a_1$, separated by a comma.
correct: |-
  (4/5)a_n, 100
```

---

**Question 3**

```quiz
type: free
id: ma-249795
content: |-
  Consider the following geometric sequence:
  $243,-162, 108, …$
  
  The recursive formula for this geometric sequence is

  Enter the expression to the right of $a_{n+1}=$ and the value of $a_1$, separated by a comma.
correct: |-
  (-2/3)a_n, 243
```

---

<a id="calculating-a-term-of-a-geometric-sequence-given-its-recursive-formula"></a>
## Calculating a Term of a Geometric Sequence Given Its Recursive Formula

**Example:** What is the $4$th term of the geometric sequence given below?
$a_{n+1} = -3 a_n,\qquad a_1 = 2,\qquad n \geq 1$

**Explanation**

We use the recursive formula to compute the terms of the sequence up to the $4$th term:

$$
\begin{aligned}
a_{1} &= 2 \\
a_{2} &= -3a_{1} =-3(2) =-6 \\
a_{3} &= -3a_{2} =-3(-6) = 18 \\
a_{4} &= -3a_{3} =-3(18) =-54
\end{aligned}
$$

Therefore, $a_4 = -54$.

---

**Question 4**

```quiz
type: free
id: ma-233046
content: |-
  Consider the following geometric sequence:
  $a_{n + 1} = \frac{5}{2}a_{n}, a_{1} = 4, n \ge 1$The $3$rd term of this geometric sequence is $a_{3} =$
correct: |-
  25
```

---

**Question 5**

```quiz
type: free
id: ma-249805
content: |-
  Consider the following geometric sequence:
  $a_{n + 1} = \frac{1}{4}a_{n}, a_{1} = 256, n \ge 1$The $4$th term of this geometric sequence is $a_{4} =$
correct: |-
  4
```

---

**Question 6:**

```quiz
type: radio
id: ma-44819
content: |-
  What is the $4$th term of the geometric sequence given below?
  
  $a_{n + 1} =-2a_{n}, a_{1} = 1, n \ge 1$
options:
- id: a
  content: |-
    $16$
- id: b
  content: |-
    $8$
- id: c
  content: |-
    $4$
- id: d
  content: |-
    $-8$
  correct: true
- id: e
  content: |-
    $-4$
```

---

<a id="calculating-a-term-of-a-geometric-sequence-given-a-recursive-formula-in-function-notation"></a>
## Calculating a Term of a Geometric Sequence Given a Recursive Formula in Function Notation

**Example:** What is the $5$th term of the geometric sequence given below?

$f(n+1) = -5f(n),\quad f(1) = -1,\quad n\geq 1$

**Explanation**

We use the recursive formula to compute the terms of the sequence up to the $4$th term:

$$
\begin{aligned}
f(1) &= -1 \\
f(2) &= -5f(1) =-5(-1) = 5 \\
f(3) &= -5f(2) =-5(5) =-25 \\
f(4) &= -5f(3) =-5(-25) = 125 \\
f(5) &= -5f(4) =-5(125) =-625
\end{aligned}
$$

Therefore,

$$
f(5)=-625
$$

---

**Question 7:**

```quiz
type: radio
id: ma-44957
content: |-
  What is the $3$rd term of the geometric sequence given below?
  
  $f(n + 1) = \frac{2}{3}f(n), f(1) =-36, n \ge 1$
options:
- id: a
  content: |-
    $16$
- id: b
  content: |-
    $-24$
- id: c
  content: |-
    $4$
- id: d
  content: |-
    $-4$
- id: e
  content: |-
    $-16$
  correct: true
```

---

**Question 8**

```quiz
type: free
id: ma-233070
content: |-
  Consider the following geometric sequence:
  
  $f(n + 1) =-2f(n), f(1) = \frac{1}{2}, n \ge 1$
  
  The $4$th term of this geometric sequence is $f(4) =$
correct: |-
  -4
```

---

**Question 9**

```quiz
type: radio
id: ma-44958
content: |-
  What is the $5$th term of the geometric sequence given below?
  
  $f(n + 1) =-2f(n), f(1) =-5, n \ge 1$
options:
- id: a
  content: |-
    $-80$
  correct: true
- id: b
  content: |-
    $40$
- id: c
  content: |-
    $160$
- id: d
  content: |-
    $-40$
- id: e
  content: |-
    $80$
```

---

<a id="identifying-geometric-sequences"></a>
## Identifying Geometric Sequences

**Example:** Which of the three sequences below are geometric sequences?

1. $10, \: 20, \: 30, \: 40, \: \dots$
2. $a_{n+1} = \dfrac{1}{6}a_n,\quad a_1 = 36,\quad n\geq 1$
3. $f(n+1) = 2f(n)-1,\quad f(1) =2,\quad n\geq 1$

**Explanation**

A sequence is geometric if there is a common ratio between its terms. Let's check each sequence in turn.

- Sequence I is not geometric because not every pair of consecutive terms has the same ratio. To see this, we only need to go up to the third term:
$\frac{a_{2}}{a_{1}} = \frac{20}{10}|= 2; \frac{a_{3}}{a_{2}} = \frac{30}{20}|= \frac{3}{2}$
- Sequence II is a geometric sequence. The recursive rule $a_{n+1} = \dfrac{1}{6}a_n$ tells us that each term is $\dfrac{1}{6}$ times the previous term, so the common ratio is $r=\dfrac{1}{6}$.
- Sequence III is not a geometric sequence. To see this, we can calculate the first $3$ terms of the sequence and then compute the ratios of consecutive terms.
$f(1)|= 2; f(2)|= 2 \cdot f(1) - 1 = 2 \cdot 2 - 1 = 3; f(3)|= 2 \cdot f(2) - 1 = 2 \cdot 3 - 1 = 5$
The first two pairs of consecutive terms have different ratios:
$(f(2))/(f(1)) = \frac{3}{2}; (f(3))/(f(2)) = \frac{5}{3}$

In conclusion, only sequence II is a geometric sequence.

---

**Question 10**

```quiz
type: radio
id: ma-39313
content: |-
  Which of the three sequences below are geometric sequences?
  
  1. $-2,-16,-64, …$
  2. $5, 23, 41, …$
  3. $a_{n + 1} =-6a_{n}, a_{1} = 3, n \ge 1$
options:
- id: a
  content: |-
    I and III only
- id: b
  content: |-
    III only
  correct: true
- id: c
  content: |-
    II and III only
- id: d
  content: |-
    None
- id: e
  content: |-
    I only
```

---

**Question 11**

```quiz
type: radio
id: ma-44824
content: |-
  Which of the three sequences below are geometric sequences?
  
  1. $5, 10, 15, …$
  2. $a_{n + 1} = 6a_{n}, a_{1} = 18, n \ge 1$
  3. $f(n + 1) = 2f(n) + 3, f(1) = 1, n \ge 1$
options:
- id: a
  content: |-
    I and II
- id: b
  content: |-
    II and III
- id: c
  content: |-
    I only
- id: d
  content: |-
    II only
  correct: true
- id: e
  content: |-
    III only
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
