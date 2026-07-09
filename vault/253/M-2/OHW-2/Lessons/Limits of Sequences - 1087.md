# Limits of Sequences

<!--
lesson-id: 1087
topic-code: MF3.7.1.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Determining the Limit of a Convergent Rational Sequence](#determining-the-limit-of-a-convergent-rational-sequence)
- [Identifying Divergent Sequences](#identifying-divergent-sequences)
- [Finding the Limit of a Factored Rational Sequence](#finding-the-limit-of-a-factored-rational-sequence)

## Prerequisites

- [Limits at Infinity and Horizontal Asymptotes of Rational Functions](<../../../../MA/Mathematical-Foundations/MF3/7. Limits & Continuity/7.1. Limits/Lessons/7.1.6. Limits at Infinity and Horizontal Asymptotes of Rational Functions.md>)
- [Introduction to Sequences](<../../../../MA/Mathematical-Foundations/MF2/7. Sequences/7.1. Introduction to Sequences/Lessons/7.1.1. Introduction to Sequences.md>)

---

<a id="introduction"></a>
## Introduction

Let's consider the sequence $a_n$, given by

$$
a_n = \dfrac {n^3 + 5 n}{2 n^3 - n^2}, \qquad\ n\geq 1
$$

and suppose that we want to determine the **limit of the sequence** $a_n$. In the context of sequences, this means to work out $\displaystyle\lim_{n\to\infty} a_n$.

Finding the limit of a rational sequence $a_n$ is very similar to finding the horizontal asymptotes of a rational function. We divide the numerator and the denominator by the variable part of the dominant term in the denominator.

In our case, the variable part of the dominant term in the denominator is $n^3$, so we divide the numerator and denominator by $n^3$ and get

$$
\begin{aligned}
lim_(n → ∞)a_{n} &= lim_(n → ∞)\frac{n^{3} + 5n}{2n^{3} - n^{2}} \\
&= lim_(n → ∞)((\frac{n^{3}}{n^{3}} + \frac{5n}{n^{3}}))/((\frac{2n^{3}}{n^{3}} - \frac{n^{2}}{n^{3}})) \\
&= lim_(n → ∞)((1 + \frac{5}{n^{2}}))/((2 - \frac{1}{n})) \\
&= \frac{1 + 0}{2 - 0} \\
&= \frac{1}{2}
\end{aligned}
$$

Since the finite limit exists, we say that the sequence **converges** and its limit is

$$
\dfrac 1 2
$$

If the limit of a sequence does *not* exist, then we say that the sequence **diverges**.

---

<a id="determining-the-limit-of-a-convergent-rational-sequence"></a>
## Determining the Limit of a Convergent Rational Sequence

**Example:** Does the sequence $a_n = \dfrac {3 n ^ 5 - n} {5 n ^ 6 - n}$ for $n\geq 1$ converge or diverge? If the sequence converges, what is its limit?

**Explanation**

To determine whether the sequence converges or diverges, we need to determine the limit of the sequence as $n$ approaches infinity:

$$
\lim_{n \to \infty} a_n = \lim_{n \to \infty}\dfrac {3 n ^ 5 - n} {5 n ^ 6 - n}
$$

The dominant term in the denominator is $5n^6$, so we divide the numerator and the denominator by $n^6$ and get

$$
\begin{aligned}
lim_(n → ∞)\frac{3n^{5} - n}{5n^{6} - n} &= lim_(n → ∞)((\frac{3n^{5}}{n^{6}} - \frac{n}{n^{6}}))/((\frac{5n^{6}}{n^{6}} - \frac{n}{n^{6}})) \\
&= lim_(n → ∞)((\frac{3}{n} - \frac{1}{n^{5}}))/((5 - \frac{1}{n^{5}})) \\
&= \frac{0 - 0}{5 - 0} \\
&= 0
\end{aligned}
$$

Since the limit exists, the sequence converges, and its limit is $0$.

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  What is the limit of the sequence $a_{n} = \frac{7n^{3} + 3}{5n^{3} + 3n^{2}}$ for $n \ge 1$?
options:
- id: a
  content: |-
    $7$
- id: b
  content: |-
    $\frac{2}{5}$
- id: c
  content: |-
    $0$
- id: d
  correct: true
  content: |-
    $\frac{7}{5}$
- id: e
  content: |-
    The sequence diverges.
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  What is the limit of the sequence $a_{n} = \frac{2n + 3}{4n}$ for $n \ge 1$?
options:
- id: a
  correct: true
  content: |-
    $\frac{1}{2}$
- id: b
  content: |-
    $\frac{3}{4}$
- id: c
  content: |-
    The sequence diverges.
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $0$
```

---

<a id="identifying-divergent-sequences"></a>
## Identifying Divergent Sequences

**Example:** Which of the following sequences diverge?

1. $a_n = \dfrac{1}{n^2}$ for $n \geq 1$
2. $a_n = \dfrac{n^4}{2n^3+1}$ for $n \geq 1$
3. $a_n = \dfrac {3 n ^ 5 + 7} {5 n ^ 4 - 3 n ^ 3}$ for $n\geq 1$?

**Explanation**

Let's analyze each sequence in turn. We need to calculate the limit of each sequence as $n$ approaches at infinity.

- In sequence I, the limit is
$\lim_{n \to \infty} a_n = \lim_{n \to \infty}\dfrac {1}{n^2} = 0$.
The limit exists, so the sequence converges.
- In sequence II, the dominant term in the denominator is $2n^3$, so we divide the numerator and the denominator by $n^3$ and get
$lim_(n → ∞)a_{n}|= lim_(n → ∞)\frac{n^{4}}{2n^{3} + 1}; = lim_(n → ∞)((\frac{n^{4}}{n^{3}}))/((\frac{2n^{3}}{n^{3}} + \frac{1}{n^{3}})); = lim_(n → ∞)(n)/((2 + \frac{1}{n^{3}})); = lim_(n → ∞)\frac{n}{2 + 0}; = ∞$.
The limit does not exist, so the sequence diverges.
- In sequence III, the dominant term in the denominator is $5n^4$, so we divide the numerator and the denominator by $n^4$ and get
$lim_(n → ∞)a_{n}|= lim_(n → ∞)\frac{3n^{5} + 7}{5n^{4} - 3n^{3}}; = lim_(n → ∞)((\frac{3n^{5}}{n^{4}} + \frac{7}{n^{4}}))/((\frac{5n^{4}}{n^{4}} - \frac{3n^{3}}{n^{4}})); = lim_(n → ∞)((3n + \frac{7}{n^{4}}))/((5 - \frac{3}{n})); = lim_(n → ∞)\frac{3n + 0}{5 - 0}; = ∞$.
The limit does not exist, so the sequence diverges.

In conclusion, sequences II and III diverge.

---

**Question 3**

```quiz
type: radio
id: q-3
content: |-
  Which of the following sequences diverge?
  
  1. $a_{n} = \frac{n^{3} - 1}{n^{2} + 1}$ for $n \ge 1$
  2. $a_{n} = \frac{n^{5} - n}{n^{4} - 2}$ for $n \ge 1$
  3. $a_{n} = \frac{1}{n^{2} + 8}$ for $n \ge 1$
options:
- id: a
  content: |-
    II and III only
- id: b
  correct: true
  content: |-
    I and II only
- id: c
  content: |-
    II only
- id: d
  content: |-
    I, II and III
- id: e
  content: |-
    I only
```

---

**Question 4**

```quiz
type: radio
id: q-4
content: |-
  Which of the following sequences diverge?
  
  1. $a_{n} = \frac{n - 1}{n^{3} + 1}$ for $n \ge 1$
  2. $a_{n} = \frac{2}{n^{3}}$ for $n \ge 1$
  3. $a_{n} = \frac{n^{3} + 3}{3n^{2} - n}$ for $n \ge 1$
options:
- id: a
  content: |-
    I and II only
- id: b
  content: |-
    II and III only
- id: c
  content: |-
    I, II, and III
- id: d
  correct: true
  content: |-
    III only
- id: e
  content: |-
    None
```

---

<a id="finding-the-limit-of-a-factored-rational-sequence"></a>
## Finding the Limit of a Factored Rational Sequence

**Example:** What is the limit of the sequence $a_n = \dfrac {n(3n-7)} {(3n-1)(3n+1)}$ for $n\geq 1$?

**Explanation**

First, we multiply out the numerator and denominator of the sequence and get

$$
a_n=\dfrac {n(3n-7)} {(3n-1)(3n+1)}=\dfrac {3 n ^ 2 - 7 n} {9 n ^ 2-1}
$$

So to find the limit, we will need to compute

$$
\lim_{n \to \infty} a_n = \lim_{n \to \infty} \dfrac {3 n ^ 2 - 7 n} {9 n ^ 2-1}
$$

The dominant term in the denominator is $n^2$, so we divide the numerator and the denominator by $n^2$ and get

$$
\begin{aligned}
lim_(n → ∞)\frac{3n^{2} - 7n}{9n^{2} - 1} &= lim_(n → ∞)((\frac{3n^{2}}{n^{2}} - \frac{7n}{n^{2}}))/((\frac{9n^{2}}{n^{2}} - \frac{1}{n^{2}})) \\
&= lim_(n → ∞)((3 - \frac{7}{n}))/((9 - \frac{1}{n^{2}})) \\
&= \frac{3 - 0}{9 - 0} \\
&= \frac{1}{3}
\end{aligned}
$$

Consequently, the sequence converges and its limit is

$$
\dfrac 1 3
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  What is the limit of the sequence $a_{n} = (3n^{3}(2n^{3} - 1))/((2n^{3} - 3)(2n^{3} + 3))$ for $n \ge 1$?
options:
- id: a
  correct: true
  content: |-
    $\frac{3}{2}$
- id: b
  content: |-
    $0$
- id: c
  content: |-
    $6$
- id: d
  content: |-
    $\frac{3}{5}$
- id: e
  content: |-
    The sequence diverges.
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  What is the limit of the sequence $a_{n} = ((3n^{2} + 2)(3n^{2} - 2))/(n^{2}(2n^{3} - 5))$ for $n \ge 1$?
options:
- id: a
  content: |-
    $-4$
- id: b
  content: |-
    $3$
- id: c
  content: |-
    The sequence diverges
- id: d
  content: |-
    $\frac{1}{2}$
- id: e
  correct: true
  content: |-
    $0$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
