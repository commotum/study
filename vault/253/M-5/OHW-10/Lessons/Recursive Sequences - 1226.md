# Recursive Sequences

<!--
lesson-id: 1226
topic-code: MF2.7.1.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Computing the Second Term of a Sequence](#computing-the-second-term-of-a-sequence)
- [Computing the Third Term of a Sequence](#computing-the-third-term-of-a-sequence)
- [Recursive Sequences in Function Notation](#recursive-sequences-in-function-notation)
- [Writing a Recursive Formula for a Sequence](#writing-a-recursive-formula-for-a-sequence)

## Prerequisites

- [Introduction to Sequences](<../Prerequisites/Introduction to Sequences - 2271.md>)
- Identifying patterns in number sequences

---

<a id="introduction"></a>
## Introduction

Some sequences are defined **recursively**, which means that there is a formula to get from one term to the next.

For example, suppose that we have the following formula:

$$
a_{n+1}=a_n+{\color{blue}{2}}, \quad a_1 = {\color{red}{3}}
$$

In this formula,

- the statement $a_{n+1} = a_n + {\color{blue}{2}}$ means "to get to the next term, we add ${\color{blue}{2}}$ to the previous term," and
- the statement $a_1 = {\color{red}{3}}$ tells us that the first term is ${\color{red}{3}}$.

So how do we calculate $a_2$, the next term in the sequence? Easy! We plug $n=1$ into the formula:

$$
\begin{aligned}
a_{n + 1} &= a_{n} + 2 \\
a_{1 + 1} &= a_{1} + 2 \\
a_{2} &= a_{1} + 2 \\
a_{2} &= 3 + 2 \\
a_{2} &= 5
\end{aligned}
$$

Now that we know $a_2$, we can find $a_3$ by plugging in $n=2$ into the formula:

$$
\begin{aligned}
a_{n + 1} &= a_{n} + 2 \\
a_{2 + 1} &= a_{2} + 2 \\
a_{3} &= a_{2} + 2 \\
a_{3} &= 5 + 2 \\
a_{3} &= 7
\end{aligned}
$$

We can keep going by substituting $n=3,4,5$, and so on. The resulting terms of the sequence are as follows:
$3,\qquad 5,\qquad 7,\qquad 9,\qquad 11,\ldots$

---

<a id="computing-the-second-term-of-a-sequence"></a>
## Computing the Second Term of a Sequence

**Example:** If $a_{n+1}=2a_n-3$ with $a_1=4$, then find the value of $a_2$.

**Explanation**

The recursive formula is

$$
a_{n+1}=2a_n - 3
$$

where

$$
a_1={\color{blue}4}
$$

We compute $a_2$ by substituting $n=1$ into the recursive formula:

$$
\begin{aligned}
a_{n + 1} &= 2a_{n} - 3 \\
a_{1 + 1} &= 2a_{1} - 3 \\
a_{2} &= 2a_{1} - 3 \\
a_{2} &= 2(4) - 3 \\
a_{2} &= 5
\end{aligned}
$$

Therefore, $a_2=5$.

---

**Question 1:**

```quiz
type: radio
id: ma-51840
content: |-
  If $a_{n + 1} = a_{n} + 3$ with $a_{1} = 4$, then $a_{2} =$
options:
- id: a
  content: |-
    $8$
- id: b
  content: |-
    $3$
- id: c
  content: |-
    $4$
- id: d
  content: |-
    $12$
- id: e
  content: |-
    $7$
  correct: true
```

---

**Question 2**

```quiz
type: blank
id: ma-217094
require_exact: true
content: |-
  If $a_{n+1}=-2a_n$ with $a_1=2$, then $a_2 =$ ==-4==.
```

---

**Question 3:**

```quiz
type: radio
id: ma-71322
content: |-
  If $a_{n + 1} = 3 - 4a_{n}$ with $a_{1} =-5$, then $a_{2} =$
options:
- id: a
  content: |-
    $33$
- id: b
  content: |-
    $11$
- id: c
  content: |-
    $-5$
- id: d
  content: |-
    $3$
- id: e
  content: |-
    $23$
  correct: true
```

---

<a id="computing-the-third-term-of-a-sequence"></a>
## Computing the Third Term of a Sequence

**Example:** Given the recursive sequence $a_{n+1} = 3a_n-2$ with $a_1=2$, what is the value of $a_3$?

**Explanation**

The recursive formula is

$$
a_{n+1} = 3a_n-2
$$

where

$$
a_1={\color{blue}2}
$$

We use this formula to compute the terms $a_2$ and $a_3$ as follows:

- We first compute $a_2$ by substituting $n=1$ into the recursive formula:
$a_{n + 1}|= 3a_{n} - 2; a_{1 + 1}|= 3a_{1} - 2; a_{2}|= 3a_{1} - 2; a_{2}|= 3(2) - 2; a_{2}|= 4$
- Then, we compute $a_3$ by substituting $n=2$ into the recursive formula:
$a_{n + 1}|= 3a_{n} - 2; a_{2 + 1}|= 3a_{2} - 2; a_{3}|= 3a_{2} - 2; a_{3}|= 3(4) - 2; a_{3}|= 10$

Therefore, $a_3=10$.

---

**Question 4:**

```quiz
type: radio
id: ma-51842
content: |-
  If $a_{n + 1} = a_{n} - 6$ with $a_{1} = 2$, then $a_{3} =$
options:
- id: a
  content: |-
    $-12$
- id: b
  content: |-
    $-10$
  correct: true
- id: c
  content: |-
    $-4$
- id: d
  content: |-
    $-16$
- id: e
  content: |-
    $-6$
```

---

**Question 5:**

```quiz
type: radio
id: ma-154918
content: |-
  If $a_{n + 1} = \frac{1}{4}a_{n}$ with $a_{1} = 8$, then $a_{3} =$
options:
- id: a
  content: |-
    $\frac{1}{4}$
- id: b
  content: |-
    $\frac{1}{2}$
  correct: true
- id: c
  content: |-
    $4$
- id: d
  content: |-
    $\frac{1}{8}$
- id: e
  content: |-
    $2$
```

---

**Question 6**

```quiz
type: blank
id: ma-217109
require_exact: true
content: |-
  If $a_{n+1}=5a_n-3$ with $a_1=1$, then $a_3 =$ ==7==.
```

---

<a id="recursive-sequences-in-function-notation"></a>
## Recursive Sequences in Function Notation

**Example:** If $f(n+1) = 2f(n) + 1$ with $f(1) = 3$, then what is $f(4)$?

**Explanation**

The recursive formula is

$$
f(n+1) = 2f(n) + 1
$$

where

$$
f(1) = {\color{blue}3}
$$

We use this formula to compute the terms $f(2), f(3)$, and $f(4)$ as follows:

- To compute $f(2)$, we substitute $n = 1$ into the recursive formula:
$f(n + 1)|= 2f(n) + 1; f(1 + 1)|= 2f(1) + 1; f(2)|= 2f(1) + 1; f(2)|= 2(3) + 1; f(2)|= 7$
- To compute $f(3)$, we substitute $n=2$ into the recursive formula:
$f(n + 1)|= 2f(n) + 1; f(2 + 1)|= 2f(2) + 1; f(3)|= 2f(2) + 1; f(3)|= 2(7) + 1; f(3)|= 15$
- To compute $f(4)$, we substitute $n=3$ into the recursive formula:
$f(n + 1)|= 2f(n) + 1; f(3 + 1)|= 2f(3) + 1; f(4)|= 2f(3) + 1; f(4)|= 2(15) + 1; f(4)|= 31$

Therefore, the fourth term of the sequence is

$$
f(4) = 31
$$

---

**Question 7:**

```quiz
type: radio
id: ma-51882
content: |-
  If $f(n + 1) = f(n) + 11$ with $f(1) =-6$, then $f(3) =$
options:
- id: a
  content: |-
    $16$
  correct: true
- id: b
  content: |-
    $5$
- id: c
  content: |-
    $10$
- id: d
  content: |-
    $-1$
- id: e
  content: |-
    $-7$
```

---

**Question 8**

```quiz
type: blank
id: ma-217120
require_exact: true
content: |-
  If $f(n+1)=f(n)+8$ with $f(1)=-6$, then $f(4) =$ ==18==.
```

---

<a id="writing-a-recursive-formula-for-a-sequence"></a>
## Writing a Recursive Formula for a Sequence

**Example:** Consider the following sequence:
$1, \quad 6, \quad 11, \quad 16, \quad 21, \quad 26, \quad \dots$
The recursive formula for this sequence is given by
$f(n+1) = f(n) + \bbox[3pt, border: 1pt solid black]{\phantom{A}}\,, \qquad f(1) = \bbox[3pt, border: 1pt solid black]{\phantom{A}}\,$.
From left to right, what are the missing values?

**Explanation**

Notice that the first term of the sequence is

$$
f(1) = {\color{blue}1}
$$

Inspecting the terms of the sequence, we see that we always get the next term by adding ${\color{red}5}$.

Therefore, the recursive rule must be the following:

$$
f(n+1) = f(n) + \bbox[3pt, border: 1pt solid black]{{\color{red}5}}\,, \qquad f(1) = \bbox[3pt, border: 1pt solid black]{{\color{blue}1}}
$$

So, the missing values are $5$ and $1$.

---

**Question 9**

```quiz
type: radio
id: ma-14435
content: |-
  Consider the following sequence:
  
  $2, 0,-2,-4,-6, …$
  The recursive formula for this sequence is given by
  $a_{n + 1} = a_{n} + A, a_{1} = A$.
  From left to right, what are the missing values?
options:
- id: a
  content: |-
    $-1$ and $2$
- id: b
  content: |-
    $2$ and $-2$
- id: c
  content: |-
    $-1$ and $-2$
- id: d
  content: |-
    $-2$ and $2$
  correct: true
- id: e
  content: |-
    $-4$ and $2$
```

---

**Question 10**

```quiz
type: blank
id: ma-217141
require_exact: true
content: |-
  Consider the following sequence:

  $$20, 10, 5, \frac{5}{2}, \frac{5}{4}, \ldots$$

  The recursive formula is

  $a_{n+1} =$ ==1/2== $\cdot a_n,\qquad a_1 =$ ==20==.
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
