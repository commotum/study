# Writing Geometric Series in Sigma Notation

<!--
lesson-id: 1017
topic-code: MF3.1.3.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Writing a Geometric Series Using Sigma Notation](#writing-a-geometric-series-using-sigma-notation)
- [Writing a Geometric Series Using Sigma Notation With Simplifications](#writing-a-geometric-series-using-sigma-notation-with-simplifications)
- [Writing a Geometric Series With a Negative Common Ratio Using Sigma Notation](#writing-a-geometric-series-with-a-negative-common-ratio-using-sigma-notation)
- [Writing a Geometric Series Using Sigma Notation by Calculating the Number of Terms](#writing-a-geometric-series-using-sigma-notation-by-calculating-the-number-of-terms)

## Prerequisites

- [Sigma Notation](<../../../../IM3/8. Probability & Statistics/8.3. Analyzing Data/Lessons/8.3.2. Sigma Notation.md>)
- [Determining Indexes of Terms in Geometric Sequences](<../../../../AG1/11. Sequences/11.3. Geometric Sequences/Lessons/11.3.6. Determining Indexes of Terms in Geometric Sequences.md>)

---

<a id="introduction"></a>
## Introduction

We can write down a geometric series in a compact way using the sigma notation

$$
S = \displaystyle\sum_{n=1}^N a_1r^{n-1}
$$

where $a_1$ is the first term of the series, $r$ is the common ratio, and $N$ is the number of terms in the series.

For instance, suppose we wish to write the following geometric series in sigma notation:

$$
S= 2+4+8+16+32+64+128
$$

In this case, $a_1 = 2$ and $N = 7$. To find $r$, we calculate the ratio of the first two terms in the series:

$$
r = \dfrac{a_2}{a_1} = \dfrac{4}{2} = 2
$$

Therefore, expressing the geometric series given in sigma notation, we obtain

$$
2+4+8+16+32+64+128 = \sum_{n=1}^{7} 2\cdot 2^{n-1}
$$

Finally, we can simplify the above series using the laws of exponents, as follows:

$$
\begin{aligned}
∑_(n = 1)^(7)2 \cdot 2^{n - 1} &= ∑_(n = 1)^(7)2 \cdot 2^{n} \cdot 2^{-1} \\
&= ∑_(n = 1)^(7)2 \cdot 2^{n} \cdot \frac{1}{2} \\
&= ∑_(n = 1)^(7)2 \cdot \frac{1}{2} \cdot 2^{n} \\
&= ∑_(n = 1)^(7)2^{n}
\end{aligned}
$$

---

<a id="writing-a-geometric-series-using-sigma-notation"></a>
## Writing a Geometric Series Using Sigma Notation

**Example:** Write the geometric series $4+ 12 + 36 +108+324$ using sigma notation.

**Explanation**

We must express the given series in the form

$$
\sum_{n=1}^{N}a_1 r^{n-1}
$$

where $a_1$ is the first term of the series, $r$ is the common ratio, and $N$ is the number of terms in the series. In this case, $a_1 = 4$ and $N = 5$.

To find $r$, we calculate the ratio of the first two terms in the series:

$$
r = \dfrac{a_2}{a_1} = \dfrac{12}{4} = 3
$$

Therefore, expressing the geometric series given in sigma notation, we obtain

$$
\begin{aligned}
4 + 12 + 36 + 108 + 324 &= ∑_(n = 1)^(5)4 \cdot 3^{n - 1}
\end{aligned}
$$

---

**Question 1:** The geometric series $1 + 3 + 9 + 27$ can be written using sigma notation as

- [ ] A. $∑_(n = 1)^(4)(\frac{1}{3})^{n - 1}$
- [ ] B. $∑_(n = 1)^(4)3^{n - 1}$
- [ ] C. $∑_(n = 1)^(4)3 \cdot 2^{n - 1}$
- [ ] D. $∑_(n = 1)^(4)(\frac{1}{9})^{n - 1}$
- [ ] E. $∑_(n = 1)^(4)\frac{1}{3} \cdot 9^{n - 1}$

---

**Question 2:** The geometric series $5 + 10 + 20 + 40 + 80 + 160$ can be written using sigma notation as

- [ ] A. $∑_(n = 1)^(6)10^{n - 1}$
- [ ] B. $∑_(n = 1)^(6)5 \cdot 4^{n - 1}$
- [ ] C. $∑_(n = 1)^(6)4 \cdot 2^{n - 1}$
- [ ] D. $∑_(n = 1)^(6)5 \cdot 2^{n - 1}$
- [ ] E. $∑_(n = 1)^(6)2 \cdot 5^{n - 1}$

---

<a id="writing-a-geometric-series-using-sigma-notation-with-simplifications"></a>
## Writing a Geometric Series Using Sigma Notation With Simplifications

**Example:** Express the geometric series $4+8+16+32+64$ using sigma notation.

**Explanation**

First, we must express the given series in the form

$$
\sum_{n=1}^{N}a_1 r^{n-1}
$$

where $a_1$ is the first term of the series, $r$ is the common ratio, and $N$ is the number of terms in the series. In this case, $a_1 =4$ and $N = 5$.

To find $r$, we calculate the ratio of the first two terms in the series:

$$
r = \dfrac{a_2}{a_1} = \dfrac{8}{4} = 2
$$

Now, expressing the geometric series given in sigma notation, we obtain

$$
4+8+16+32+64 = \sum_{n=1}^{5}4 \cdot 2^{n - 1}
$$

Finally, we can simplify the above series using the laws of exponents, as follows:

$$
\begin{aligned}
∑_(n = 1)^(5)4 \cdot 2^{n - 1} &= ∑_(n = 1)^(5)4 \cdot 2^{n} \cdot 2^{-1} \\
&= ∑_(n = 1)^(5)4 \cdot 2^{n} \cdot \frac{1}{2} \\
&= ∑_(n = 1)^(5)4 \cdot \frac{1}{2} \cdot 2^{n} \\
&= ∑_(n = 1)^(5)2 \cdot 2^{n}
\end{aligned}
$$

---

**Question 3:** The geometric series $4 + 12 + 36 + 108 + 324$ can be expressed using sigma notation as

- [ ] A. $∑_(n = 1)^(5)\frac{3}{4} \cdot 3^{n}$
- [ ] B. $∑_(n = 1)^(5)\frac{3}{4} \cdot 4^{n}$
- [ ] C. $∑_(n = 1)^(5)\frac{1}{4} \cdot 3^{n}$
- [ ] D. $∑_(n = 1)^(5)\frac{1}{3} \cdot 4^{n}$
- [ ] E. $∑_(n = 1)^(5)\frac{4}{3} \cdot 3^{n}$

---

**Question 4:** The geometric series $6 + 12 + 24 + 48 + 96 + 192 + 384$ can be expressed using sigma notation as

- [ ] A. $∑_(n = 1)^(7)\frac{1}{3} \cdot 2^{n}$
- [ ] B. $∑_(n = 1)^(7)2 \cdot 3^{n}$
- [ ] C. $∑_(n = 1)^(7)\frac{1}{2} \cdot 3^{n}$
- [ ] D. $∑_(n = 1)^(7)\frac{3}{2} \cdot 2^{n}$
- [ ] E. $∑_(n = 1)^(7)3 \cdot 2^{n}$

---

<a id="writing-a-geometric-series-with-a-negative-common-ratio-using-sigma-notation"></a>
## Writing a Geometric Series With a Negative Common Ratio Using Sigma Notation

**Example:** Write the geometric series $1 - 4 + 16 - 64 + 256$ using sigma notation.

**Explanation**

First, we must express the given series in the form

$$
\sum_{n=1}^{N}a_1 r^{n-1}
$$

where $a_1$ is the first term of the series, $r$ is the common ratio, and $N$ is the number of terms in the series. In this case, $a_1 = 1$ and $N = 5$.

To find $r$, we calculate the ratio of the first two terms in the series:

$$
r = \dfrac{a_2}{a_1} = \dfrac{-4}{1} = -4
$$

So, expressing the geometric series given in sigma notation, we obtain

$$
1 - 4 + 16 - 64 + 256 = \sum_{n=1}^{5} 1 \cdot (-4)^{n - 1}
$$

Finally, we can simplify the above using the laws of exponents, as follows:

$$
\begin{aligned}
1 - 4 + 16 - 64 + 256 &= ∑_(n = 1)^(5)1 \cdot (-4)^{n - 1} \\
&= ∑_(n = 1)^(5)(-4)^{n}(-4)^{-1} \\
&= ∑_(n = 1)^(5)(-4)^{n}(-\frac{1}{4}) \\
&= ∑_(n = 1)^(5)(-\frac{1}{4})(-4)^{n}
\end{aligned}
$$

---

**Question 5:** The geometric series $3 - 6 + 12 - 24 + 48$ can be expressed using sigma notation as

- [ ] A. $∑_(n = 1)^(5)2 \cdot (-3)^{n - 1}$
- [ ] B. $∑_(n = 1)^(5)3 \cdot (-2)^{n - 1}$
- [ ] C. $∑_(n = 1)^(5)(-3) \cdot (-2)^{n - 1}$
- [ ] D. $∑_(n = 1)^(5)4 \cdot (-3)^{n - 1}$
- [ ] E. $∑_(n = 1)^(5)5 \cdot (-3)^{n - 1}$

---

**Question 6:** The geometric series $-2 + \frac{1}{3} - \frac{1}{18} + \frac{1}{108}$ can be expressed using sigma notation as

- [ ] A. $∑_(n = 1)^(4)(-2) \cdot (-\frac{1}{6})^{n}$
- [ ] B. $∑_(n = 1)^(4)(-3) \cdot (-\frac{1}{6})^{n}$
- [ ] C. $∑_(n = 1)^(4)2 \cdot (-\frac{1}{3})^{n}$
- [ ] D. $∑_(n = 1)^(4)4 \cdot (-\frac{1}{3})^{n}$
- [ ] E. $∑_(n = 1)^(4)12 \cdot (-\frac{1}{6})^{n}$

---

<a id="writing-a-geometric-series-using-sigma-notation-by-calculating-the-number-of-terms"></a>
## Writing a Geometric Series Using Sigma Notation by Calculating the Number of Terms

**Example:** Express the geometric series $1+ 3+ 9+ \cdots + 243$ using sigma notation.

**Explanation**

We must express the given series in the form

$$
\sum_{n=1}^{N}a_1 r^{n-1}
$$

where $a_1$ denotes the first term of the series, $r$ denotes the common ratio, and $N$ denotes the number of terms in the series. In this case, $a_1 = 1$.

To find $r$, we find the ratio of the consecutive terms $a_1$ and $a_2$:

$$
r = \dfrac{a_2}{a_1} = \dfrac{3}{1} = 3
$$

Now we must determine $N$ (the index of the last term). To do this, we use the fact that

$$
a_N = a_1 \cdot r^{N - 1}
$$

Therefore,

$$
\begin{aligned}
a_{N} &= a_{1} \cdot r^{N - 1} \\
243 &= 1 \cdot 3^{N - 1} \\
3^{5} &= 3^{N - 1} \\
5 &= N - 1 \\
N &= 6
\end{aligned}
$$

Expressing the geometric series in sigma notation, we obtain

$$
\begin{aligned}
1 + 3 + 9 + ⋯ + 243 &= ∑_(n = 1)^(6)1 \cdot 3^{n - 1} \\
&= ∑_(n = 1)^(6)3^{n - 1}
\end{aligned}
$$

---

**Question 7**

> A scientific calculator is required to answer this question.

The geometric series $6 + 18 + ⋯ + 1458$ can be expressed using sigma notation as

- [ ] A. $∑_(n = 1)^(6)6 \cdot 3^{n - 1}$
- [ ] B. $∑_(n = 1)^(6)3 \cdot 2^{n - 1}$
- [ ] C. $∑_(n = 1)^(5)6 \cdot 3^{n - 1}$
- [ ] D. $∑_(n = 1)^(7)6 \cdot 3^{n - 1}$
- [ ] E. $∑_(n = 1)^(5)3 \cdot 2^{n - 1}$

---

**Question 8**

> A scientific calculator is required to answer this question.

The geometric series $486 + 162 + 54⋯ + 2$ can be expressed using sigma notation as

- [ ] A. $∑_(n = 1)^(7)486 \cdot (\frac{1}{3})^{n - 1}$
- [ ] B. $∑_(n = 1)^(5)486 \cdot (\frac{1}{3})^{n - 1}$
- [ ] C. $∑_(n = 1)^(6)486 \cdot (\frac{1}{4})^{n - 1}$
- [ ] D. $∑_(n = 1)^(7)486 \cdot (\frac{1}{4})^{n - 1}$
- [ ] E. $∑_(n = 1)^(6)486 \cdot (\frac{1}{3})^{n - 1}$

```update-progress
```

[[MA/MF3/Home|Home]]
[[MA/MF3/0. Table of Contents/TOC|Table of Contents]]
