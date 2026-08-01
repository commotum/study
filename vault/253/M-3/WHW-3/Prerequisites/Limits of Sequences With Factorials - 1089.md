# Limits of Sequences With Factorials

## Table of Contents

- [Introduction](#introduction)
- [Sequences Where N! is the Smallest Factorial](#sequences-where-n-is-the-smallest-factorial)
- [Sequences Where N! is the Largest Factorial](#sequences-where-n-is-the-largest-factorial)
- [Sequences Containing Ratios of Shifted Factorials](#sequences-containing-ratios-of-shifted-factorials)

## Prerequisites

- [Limits of Sequences](<../../../../MA/Mathematical-Foundations/MF3/7. Limits & Continuity/7.1. Limits/Lessons/7.1.2. Limits of Sequences.md>)
- [Factorials in Variable Expressions](<../../../../MA/Mathematical-Foundations/MF2/14. Probability & Combinatorics/14.3. Combinatorics/Lessons/14.3.3. Factorials in Variable Expressions.md>)

---

<a id="introduction"></a>
## Introduction

Sequences involving factorials often occur in advanced math. For that reason, we need to know how to analyze them.

Let's consider the sequence $a_n$ given below.

$$
a_n = \dfrac {n!}{(n + 1)!},\qquad n\geq 1
$$

Does this sequence converge or diverge? If it converges, what is its limit?

To evaluate the limit, note the following:

- The trick is to simplify $a_n$ by writing the *larger* factorial in terms of the smaller one.
- In this case, $(n+1)$! is the larger factorial, and $n$! is the smaller.
- So, we need to write $(n+1)$! in terms of $n$!

Let's remind ourselves of the definition of the factorial function:

$$
{n!} = {\color{blue}{1\cdot 2\cdot 3\cdots (n-1)\cdot n}}
$$

Using the same definition, we can write $(n+1)$! as

$$
(n+1)! = \underbrace{{\color{blue}{1\cdot 2\cdot 3\cdots (n-1)\cdot n}}}_{n!} \cdot (n+1)
$$

Replacing ${\color{blue}{1\cdot 2\cdot 3\cdots (n-1)\cdot n}}$ with $n$! in the above expression, we have

$$
(n+1)! = n!\cdot (n+1)
$$

We can now use our expression for $(n+1)$! in terms of $n$! to simplify our expression for $a_n$, as follows:

$$
\begin{aligned}
a_{n} &= (n!)/((n + 1)!) \\
&= (n!)/(n! \cdot (n + 1)) \\
&= (n!)/(n! \cdot (n + 1)) \\
&= \frac{1}{n + 1}
\end{aligned}
$$

From here, we see that $a_n\to 0$ as $n\to\infty$ because the numerator is constant, yet the denominator is a linear polynomial. So, we have

$$
\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} \left(\dfrac{1}{n+1}\right) = 0
$$

Therefore, we conclude that $a_n$ is convergent, and it converges to $0$.

---

<a id="sequences-where-n-is-the-smallest-factorial"></a>
## Sequences Where N! is the Smallest Factorial

**Example:** Determine whether the sequence
$a_n = \dfrac{3(n+2)!}{2n!}, \qquad n \geq 1$
converges or diverges. If it converges, find its limit.

**Explanation**

To evaluate the limit, note the following:

- We need to write the larger factorial in terms of the smaller one.
- In this case, $(n+2)$! is the larger factorial, and $n$! is the smaller.
- So, we need to write $(n+2)$! in terms of $n$!

Now, notice the following:

$$
(n+2)! = n! \cdot (n+1) \cdot (n+2)
$$

We use this to cancel the $n$! that occurs in both the numerator and denominator in our expression for $a_n{:}$

$$
\begin{aligned}
a_{n} &= (3(n + 2)!)/(2n!) \\
&= (3 \cdot n! \cdot (n + 1) \cdot (n + 2))/(2 \cdot n!) \\
&= (3 \cdot n! \cdot (n + 1) \cdot (n + 2))/(2 \cdot n!) \\
&= \frac{3}{2} \cdot (n + 1) \cdot (n + 2)
\end{aligned}
$$

We see that $a_n$ grows without bound as $n \to \infty$ because it's a quadratic polynomial. So, we have that

$$
\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} \dfrac32 \cdot (n+1) \cdot (n+2) = \infty
$$

We conclude that the sequence is divergent.

---

**Question 1:** Determine whether the sequence
$a_{n} = ((n + 2)!)/(n!), n \ge 1$
converges or diverges. If it converges, find the limit.

- [ ] A. The sequence converges, and its limit is $1$
- [ ] B. The sequence converges, and its limit is $\frac{3}{2}$
- [ ] C. The sequence converges, and its limit is $0$
- [ ] D. The sequence converges, and its limit is $3$
- [ ] E. The sequence diverges

---

**Question 2:** Determine whether the sequence
$a_{n} = (4n!)/((n + 3)!), n \ge 1$
converges or diverges. If it converges, find its limit.

- [ ] A. The sequence diverges
- [ ] B. The sequence converges, and its limit is $0$
- [ ] C. The sequence converges, and its limit is $4$
- [ ] D. The sequence converges, and its limit is $\frac{1}{4}$
- [ ] E. The sequence converges,and its limit is $1$

---

<a id="sequences-where-n-is-the-largest-factorial"></a>
## Sequences Where N! is the Largest Factorial

**Example:** Determine whether the sequence
$a_n = \dfrac{(n - 2)!}{n!}, \qquad n \geq 1$
converges or diverges. If it converges, find its limit.

**Explanation**

To evaluate the limit, note the following:

- We need to write the larger factorial in terms of the smaller one.
- In this case, $n$! is the larger factorial, and $(n-2)$! is the smaller.
- So, we need to write $n$! in terms of $(n-2)$!

Now, notice the following:

$$
n! = (n-2)! \cdot (n-1)\cdot n
$$

We use this to cancel the $(n-1)$! that occurs in both the numerator and denominator in our expression for $a_n{:}$

$$
\begin{aligned}
a_{n} &= ((n - 2)!)/(n!) \\
&= ((n - 2)!)/((n - 2)! \cdot (n - 1) \cdot n) \\
&= ((n - 2)!)/((n - 2)! \cdot (n - 1) \cdot n) \\
&= (1)/((n - 1) \cdot n)
\end{aligned}
$$

We see that $a_n$ shrinks to zero as $n \to \infty$ because the numerator is constant, yet the denominator is a quadratic polynomial. So, we have that

$$
\lim_{n \to \infty} a_n = \lim_{n \to \infty} \dfrac{1}{(n-1) \cdot n} = 0
$$

We conclude that the sequence is convergent, and its limit is zero.

---

**Question 3:** Determine whether the sequence
$a_{n} = (n!)/(2(n - 3)!), n \ge 3$
converges or diverges. If it converges, find the limit.

- [ ] A. The sequence diverges
- [ ] B. The sequence converges, and its limit is $0$
- [ ] C. The sequence converges, and its limit is $\frac{1}{2}$
- [ ] D. The sequence converges, and its limit is $1$
- [ ] E. The sequence converges, and its limit is $3$

---

**Question 4:** Determine whether the sequence
$a_{n} = ((n - 2)!)/(n!), n \ge 2$
converges or diverges. If it converges, find the limit.

- [ ] A. The sequence converges, and its limit is $1$
- [ ] B. The sequence converges, and its limit is $\frac{1}{2}$
- [ ] C. The sequence converges, and its limit is $0$
- [ ] D. The sequence diverges
- [ ] E. The sequence converges,and its limit is $\frac{1}{3}$

---

<a id="sequences-containing-ratios-of-shifted-factorials"></a>
## Sequences Containing Ratios of Shifted Factorials

**Example:** Determine whether the sequence

$a_n = \dfrac{2(n-1)!}{(n+1)!}$

converges or diverges. If it converges, determine its limit.

**Explanation**

To evaluate the limit, note the following:

- We need to write the larger factorial in terms of the smaller one.
- In this case, $(n+1)$! is the larger factorial, and $(n-1)$! is the smaller.
- So, we need to write $(n+1)$! in terms of $(n-1)$!

Now, notice the following:

$$
(n+1)! = (n-1)!\cdot n \cdot (n+1)
$$

We use this to cancel the $(n-1)$! that occurs in both the numerator and denominator in our expression for $a_n{:}$

$$
\begin{aligned}
a_{n} &= (2(n - 1)!)/((n + 1)!) \\
&= (2 \cdot (n - 1)!)/((n - 1)! \cdot n \cdot (n + 1)) \\
&= (2 \cdot (n - 1)!)/((n - 1)! \cdot n \cdot (n + 1)) \\
&= (2)/(n \cdot (n + 1))
\end{aligned}
$$

We see that $a_n$ shrinks to zero as $n\to\infty$ because the numerator is constant, yet the denominator is a quadratic polynomial. So, we have that

$$
\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} \dfrac{2}{n\cdot (n+1)} = 0
$$

We conclude that the sequence is convergent, and its limit is zero.

---

**Question 5:** Determine whether the sequence
$a_{n} = ((n + 4)!)/((n + 1)!), n \ge 1$
converges or diverges. If it converges, find its limit.

- [ ] A. The sequence converges, and its limit is $1$
- [ ] B. The sequence converges, and its limit is $\frac{1}{4}$
- [ ] C. The sequence converges, and its limit is $4$
- [ ] D. The sequence diverges
- [ ] E. The sequence converges, and its limit is $0$

---

**Question 6:** Determine whether the sequence
$a_{n} = ((n + 1)!)/((n + 3)!), n \ge 1$
converges or diverges. If it converges, find its limit.

- [ ] A. The sequence converges, and its limit is $\frac{1}{3}$
- [ ] B. The sequence converges, and its limit is $1$
- [ ] C. The sequence converges, and its limit is $0$
- [ ] D. The sequence diverges
- [ ] E. The sequence converges, and its limit is $3$

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
