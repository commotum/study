# The Sum of a Finite Geometric Series

<!--
lesson-id: 1016
topic-code: MF3.1.3.1
-->

## Table of Contents

- [Introduction](#introduction)
- [Calculating the Sum of a Geometric Series](#calculating-the-sum-of-a-geometric-series)
- [Calculating the Sum of a Geometric Series With a Negative Common Ratio](#calculating-the-sum-of-a-geometric-series-with-a-negative-common-ratio)
- [Calculating the Sum of a Geometric Series Given the Last Term of the Series](#calculating-the-sum-of-a-geometric-series-given-the-last-term-of-the-series)
- [Calculating the Sum of a Geometric Series Given Two Consecutive Terms of the Series](#calculating-the-sum-of-a-geometric-series-given-two-consecutive-terms-of-the-series)
- [Proof of the Formula for the Sum of a Geometric Series](#proof-of-the-formula-for-the-sum-of-a-geometric-series)

## Prerequisites

- [Determining Indexes of Terms in Geometric Sequences](<../../../../AG1/11. Sequences/11.3. Geometric Sequences/Lessons/11.3.6. Determining Indexes of Terms in Geometric Sequences.md>)

---

<a id="introduction"></a>
## Introduction

A **geometric series** is a sum of terms of a geometric sequence. For example, given the following seven terms of a geometric sequence,

$$
2, \: 6, \: 18, \: 54, \: 162, \: 486, \: 1\, 458
$$

the corresponding geometric series is

$$
S_7 = 2 + 6 +18 + 54 + 162 + 486 + 1\, 458
$$

To compute the sum of the series, one way is to add up the terms individually. But that would take a long time.

Instead, we can use the formula for the sum of the first $N$ terms of a geometric series, given by

$$
S_N = a_1\dfrac{(1-r^N)}{1-r}
$$

where $a_1$ is the first term of the series and $r$ is the common ratio.

Let's apply this formula to find $S_7$. First, we determine the common ratio $r$:

$$
r = \dfrac {a_2}{a_1} = \dfrac 6 2 = 3
$$

Now, we can determine $S_7$:

$$
\begin{aligned}
S_{7} &= a_{1}((1 - r^{7}))/(1 - r) \\
&= 2((1 - 3^{7}))/(1 - 3) \\
&= 2((1 - 2187))/(-2) \\
&= 2186
\end{aligned}
$$

---

<a id="calculating-the-sum-of-a-geometric-series"></a>
## Calculating the Sum of a Geometric Series

**Example:** Compute the sum of the first $7$ terms of the geometric series $3+6+12+\cdots$

**Explanation**

Given a geometric series, the sum of the first $N$ terms is given by the formula

$$
S_N = a_1\dfrac{(1-r^N)}{1-r}
$$

where $a_1$ is the first term of the series and $r$ is the common ratio.

In our case, $a_1 = 3$. To find the value of $r$, we find the ratio of the first two terms in the series:

$$
r = \dfrac{a_2}{a_1} = \dfrac{6}{3} = 2
$$

If we substitute $a_1 = 3$, $N = 7$, and $r = 2$ into our formula, we obtain

$$
\begin{aligned}
S_{7} &= 3 \cdot \frac{1 - 2^{7}}{1 - 2} \\
&= 3 \cdot \frac{1 - 2^{7}}{-1} \\
&=-3(-127) \\
&= 381
\end{aligned}
$$

---

**Question 1**

> A scientific calculator is required to answer this question.

Compute the sum of the first $6$ terms of the geometric series $5 + 25 + 125 + ⋯$

- [ ] A. $18305$
- [ ] B. $20520$
- [ ] C. $19530$
- [ ] D. $22005$
- [ ] E. $21505$

---

**Question 2**

> A scientific calculator is required to answer this question.

If $k(1 - 3^{6})$ is the sum of the first $6$ terms of the geometric series $1 + 3 + 9 + ⋯$, then $k =$

- [ ] A. $1$
- [ ] B. $2$
- [ ] C. $-1$
- [ ] D. $-\frac{1}{2}$
- [ ] E. $\frac{1}{2}$

---

**Question 3**

> A scientific calculator is required to answer this question.

If $k(1 - (\frac{1}{3})^{10})$ is the sum of the first $10$ terms of the geometric series $\frac{4}{3} + \frac{4}{9} + \frac{4}{27} + ⋯$, then $k =$

- [ ] A. $\frac{4}{3}$
- [ ] B. $\frac{2}{3}$
- [ ] C. $4$
- [ ] D. $2$
- [ ] E. $\frac{1}{6}$

---

<a id="calculating-the-sum-of-a-geometric-series-with-a-negative-common-ratio"></a>
## Calculating the Sum of a Geometric Series With a Negative Common Ratio

**Example:** Compute the sum of the first $6$ terms of the geometric series $2 -8 + 32 - 128 + \cdots$

**Explanation**

Given a geometric series, the sum of the first $N$ terms is given by the formula

$$
S_N = a_1\dfrac{(1-r^N)}{1-r}
$$

where $a_1$ is the first term of the series and $r$ is the common ratio.

In our case, $a_1 = 2$. To find the value of $r$, we find the ratio of the first two terms in the series:

$$
r = \dfrac{a_2}{a_1} = \dfrac{-8}{2} = -4
$$

If we substitute $a_1 = 2$ and $r = -4$ in the formula, we obtain

$$
\begin{aligned}
S_{6} &= 2 \cdot (1 - (-4)^{6})/(1 - (-4)) \\
&= 2 \cdot \frac{1 - 4^{6}}{1 + 4} \\
&= 2 \cdot \frac{-4095}{5} \\
&=-1638
\end{aligned}
$$

---

**Question 4**

> A scientific calculator is required to answer this question.

Compute the sum of the first $6$ terms of the geometric series $8 - 4 + 2 - ⋯$

- [ ] A. $\frac{11}{2}$
- [ ] B. $\frac{21}{4}$
- [ ] C. $\frac{43}{8}$
- [ ] D. $\frac{51}{10}$
- [ ] E. $\frac{19}{6}$

---

**Question 5**

> A scientific calculator is required to answer this question.

If $k(1 - 4^{12})$ is the sum of the first $12$ terms of the geometric series $10 - 40 + 160 - ⋯$, then $k =$

- [ ] A. $5$
- [ ] B. $2$
- [ ] C. $1$
- [ ] D. $10$
- [ ] E. $8$

---

**Question 6**

> A scientific calculator is required to answer this question.

If $k(1 - (\frac{1}{5})^{10})$ is the sum of the first $10$ terms of the geometric series $\frac{8}{5} - \frac{8}{25} + \frac{8}{125} - ⋯$, then $k =$

- [ ] A. $\frac{4}{3}$
- [ ] B. $\frac{8}{5}$
- [ ] C. $-\frac{5}{3}$
- [ ] D. $\frac{1}{3}$
- [ ] E. $-\frac{1}{5}$

---

<a id="calculating-the-sum-of-a-geometric-series-given-the-last-term-of-the-series"></a>
## Calculating the Sum of a Geometric Series Given the Last Term of the Series

**Example:** What is the sum of the geometric series $1 + 6 + 36 + \cdots + 46\,656$?

*Hint: You may wish to make use of the fact that $46\,656 = 6^6$.*

**Explanation**

The sum of the first $N$ terms of a geometric series is given by the formula

$$
S_N = a_1\dfrac{(1-r^N)}{1-r}
$$

where $a_1$ is the first term of this series, and $r$ is the common ratio. In our case, we have $a_1 = 1$.

To find $r$, we find the ratio of the consecutive terms $a_1$ and $a_2$:

$$
r = \dfrac{a_2}{a_1} = \dfrac{6}{1} = 6
$$

Now we must determine $N$ (the index of the last term). To do this, we use the fact that

$$
a_N = a_1 \cdot r^{N-1}
$$

Therefore, using the hint, we get

$$
\begin{aligned}
46656 &= 1 \cdot 6^{N - 1} \\
46656 &= 6^{N - 1} \\
6^{6} &= 6^{N - 1} \\
6 &= N - 1 \\
N &= 7
\end{aligned}
$$

Finally, if we substitute $a_1 = 1$, $r = 6$, and $N = 7$ in the formula for $S_N$, we get

$$
\begin{aligned}
S_{7} &= 1 \cdot \frac{1 - 6^{7}}{1 - 6} \\
&= \frac{6^{7} - 1}{5} \\
&= \frac{279935}{5} \\
&= 55987
\end{aligned}
$$

---

**Question 7**

> A scientific calculator is required to answer this question.

$4 + 20 + 100 + ⋯ + 12500 =$

*Hint: You may wish to make use of the fact that $3125 = 5^{5}$.*

- [ ] A. $16004$
- [ ] B. $15928$
- [ ] C. $15624$
- [ ] D. $14662$
- [ ] E. $16782$

---

**Question 8**

> A scientific calculator is required to answer this question.

The first term of a geometric series is $4$, the last term is $8748$, and the common ratio is $3$. What is the sum of this series?

*Hint: You may wish to make use of the fact that $2187 = 3^{7}$.*

- [ ] A. $14190$
- [ ] B. $13120$
- [ ] C. $12025$
- [ ] D. $14850$
- [ ] E. $13785$

---

<a id="calculating-the-sum-of-a-geometric-series-given-two-consecutive-terms-of-the-series"></a>
## Calculating the Sum of a Geometric Series Given Two Consecutive Terms of the Series

**Example:** The second term of a geometric series is $20$ and the third term is $100$. What is the sum of the first $6$ terms?

**Explanation**

The sum of the first $N$ terms of a geometric series is given by the formula

$$
S_N = a_1\dfrac{(1-r^N)}{1-r}
$$

where $a_1$ is the first term of the series, and $r$ is the common ratio.

To find $r$, we find the ratio of the consecutive terms $a_2$ and $a_3$:

$$
r = \dfrac{a_3}{a_2} = \dfrac{100}{20} = 5
$$

Now we must determine the value of $a_1$. To do this, we use the formula for the $n$th term, which states that

$$
a_n = a_1 \cdot r^{n-1}
$$

For $n = 2$, we get

$$
\begin{aligned}
a_{2} &= a_{1} \cdot 5^{2 - 1} \\
20 &= a_{1} \cdot 5 \\
a_{1} &= 4
\end{aligned}
$$

Finally, if we substitute $a_1 = 4$, $N = 6$, and $r = 5$ into the formula for $S_N$, we obtain

$$
\begin{aligned}
S_{6} &= 4 \cdot \frac{1 - 5^{6}}{1 - 5} \\
&= 4 \cdot \frac{1 - 5^{6}}{-4} \\
&= 5^{6} - 1 \\
&= 15624
\end{aligned}
$$

---

**Question 9**

> A scientific calculator is required to answer this question.

The third term of the geometric series is $12$ and the fourth term is $24$. What is the sum of the first $7$ terms?

- [ ] A. $326$
- [ ] B. $292$
- [ ] C. $433$
- [ ] D. $519$
- [ ] E. $381$

---

**Question 10**

> A scientific calculator is required to answer this question.

The second term of a geometric series is $\frac{1}{12}$ and the third term is $\frac{1}{36}$. What is the sum of the first $6$ terms?

- [ ] A. $\frac{91}{243}$
- [ ] B. $\frac{62}{243}$
- [ ] C. $\frac{16}{81}$
- [ ] D. $\frac{114}{729}$
- [ ] E. $\frac{252}{729}$

---

<a id="proof-of-the-formula-for-the-sum-of-a-geometric-series"></a>
## Proof of the Formula for the Sum of a Geometric Series

Let's now prove the formula. We want to find the sum

$$
S_N = a_1 + a_2 + a_3 + \dots + a_N
$$

The formula for the $n$th term is

$$
a_n = a_1 \cdot r^{n - 1}
$$

Plugging this expression into $S_N$, we get

$$
S_N = a_1 + a_1 \cdot r + a_1 \cdot r ^2 + \dots + a_1 \cdot r ^ {N - 1}
$$

Now, let's write down $-r S_N$ underneath the expression for $S_N$:

$$
\begin{aligned}
S_{N} &= a_{1} + a_{1} \cdot r + a_{1} \cdot r^{2} + a_{1} \cdot r^{3} + ⋯ + a_{1} \cdot r^{N - 1} \\
- r \cdot S_{N} &= -a_{1} \cdot r - a_{1} \cdot r^{2} - a_{1} \cdot r^{3} - ⋯ - a_{1} \cdot r^{N - 1} - a_{1} \cdot r^{N}
\end{aligned}
$$

Summing the two equations above, we get

$$
\begin{aligned}
S_{N} - r \cdot S_{N} &= a_{1} + (a_{1} \cdot r - a_{1} \cdot r) + (a_{1} \cdot r^{2} - a_{1} \cdot r^{2}) + ⋯ \\
&= + (a_{1} \cdot r^{N - 1} - a_{1} \cdot r^{N - 1}) - a_{1} \cdot r^{N}
\end{aligned}
$$

We see that all terms of $S_N$ are canceled but the first and the last. So we get

$$
\begin{aligned}
S_{N} - r \cdot S_{N} &= a_{1} - a_{1} \cdot r^{N} \\
S_{N}(1 - r) &= a_{1}(1 - r^{N}) \\
S_{N} &= a_{1}((1 - r^{N}))/(1 - r)
\end{aligned}
$$

```update-progress
```

[[MA/Mathematical-Foundations/MF3/Home|Home]]
[[MA/Mathematical-Foundations/MF3/0. Table of Contents/TOC|Table of Contents]]
