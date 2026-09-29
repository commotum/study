# The Ratio Test

<!--
lesson-id: 746
topic-code: CA2.4.5.8
-->

## Table of Contents

- [Introduction](#introduction)
- [Applying the Ratio Test for Convergence](#applying-the-ratio-test-for-convergence)
- [Applying the Ratio Test for Divergence](#applying-the-ratio-test-for-divergence)
- [Applying the Ratio Test in the Indeterminate Case](#applying-the-ratio-test-in-the-indeterminate-case)

## Prerequisites

- [Dividing Rational Expressions](<../../../../MA/Mathematical-Foundations/MF2/6. Radical & Rational Functions/6.1. Rational Expressions/Lessons/6.1.5. Dividing Rational Expressions.md>)
- [Convergent and Divergent Infinite Series](<../../../../MA/Mathematical-Foundations/MF3/1. Sequences and Series/1.4. Infinite Series/Lessons/1.4.4. Convergent and Divergent Infinite Series.md>)
- [Limits of Sequences With Factorials](<../../../../MA/Single-Variable-Calculus/CA2/4. Sequences & Series/4.1. Sequences/Lessons/4.1.4. Limits of Sequences With Factorials.md>)
- [Determining Limits of Sequences Using Relative Magnitudes](<../../../../MA/Mathematical-Foundations/MF3/7. Limits & Continuity/7.1. Limits/Lessons/7.1.9. Determining Limits of Sequences Using Relative Magnitudes.md>)

---

<a id="introduction"></a>
## Introduction

The **ratio test** can allow us to determine whether an infinite series converges or diverges, based on the limit of the absolute value of the ratio of consecutive terms.

Let the number

$$
L\geq 0
$$

be defined as

$$
L = \lim_{n\rightarrow\infty}\left|\frac{a_{n+1}}{a_n}\right|
$$

The ratio test states that:

- if $L<1$, then the series is convergent
- if $L>1$, then the series is divergent
- if $L=1$, then the ratio test gives no conclusion about the convergence or divergence of the series

**Note:** There is some nice intuition behind the ratio test. Loosely speaking, we can think of the series as eventually looking similar to a geometric series whose common ratio has magnitude $L$.

- If $L<1$, then the terms of the series decrease in magnitude, so it's intuitive that they would converge (rather than diverge).
- If $L>1$, then the terms of the series increase in magnitude, so it's intuitive that they would diverge.

---

<a id="applying-the-ratio-test-for-convergence"></a>
## Applying the Ratio Test for Convergence

**Example:** Use the ratio test to show that $\displaystyle \sum_{n=1}^\infty \frac{n}{3^n}$ is convergent.

**Explanation**

Let

$$
a_n = \dfrac{n}{3^n}
$$

If we replace $n$ with $n+1$, we get

$$
\begin{aligned} a_{n+1}= \frac{n+1}{3^{n+1}}= \frac{n+1}{3\cdot 3^n}. \end{aligned}
$$

Now that we have expressions for the consecutive terms $a_n$ and $a_{n+1}$, we can work out the necessary limit:

$$
\begin{aligned} L &=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n} \right| \\[5pt] &=\lim_{n\to\infty}\left(\frac{n+1}{3\cdot 3^n} \div \frac{n}{3^n}\right) \\[5pt] &= \lim_{n\to\infty}\left(\frac{n+1}{3\cdot 3^n} \cdot \frac{3^n}{n}\right) \\[5pt] &= \lim_{n\to\infty}\left(\frac{n+1}{3n} \right) \\[5pt] &= \lim_{n\to\infty}\left(\frac{1}{3}\cdot \frac{n+1}{n}\right) \\[5pt] &= \frac{1}{3}\lim_{n\to\infty}\left(1 + \frac{1}{n}\right) \\[5pt] &=\frac{1}{3}\left(1 + 0\right) \\[5pt] &=\frac{1}{3}. \end{aligned}
$$

Note that we dropped the absolute value bars because the sequence is positive for all

$$
n\geq 1
$$

Since

$$
L = \dfrac{1}{3}<1
$$

we conclude that the series is convergent by the ratio test.

---

**Question 1:**

```quiz
type: radio
id: ma-50795
content: |-
  Calculate $L = lim_(n → ∞) \mid \frac{a_{n + 1}}{a_{n}} \mid$ for the sequence $a_{n} = (n!)/((2n)!)$. According to the ratio test, does $∑_(n = 1)^(∞)a_{n}$ converge or diverge?
options:
- id: a
  content: |-
    $L = ∞$. The series is divergent
- id: b
  content: |-
    $L = \frac{1}{2}$. The series is convergent
- id: c
  content: |-
    $L = 2$. The series is divergent
- id: d
  content: |-
    $L = 1$. The ratio test gives no conclusion
- id: e
  content: |-
    $L = 0$. The series is convergent
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: ma-50727
content: |-
  Calculate $L = lim_(n → ∞) \mid \frac{a_{n + 1}}{a_{n}} \mid$ for the sequence $a_{n} = \frac{n}{2^{n}}$. According to the ratio test, does $∑_(n = 1)^(∞)a_{n}$ converge or diverge?
options:
- id: a
  content: |-
    $L = 2$. The series is convergent
- id: b
  content: |-
    $L = 1$. The ratio test gives no conclusion
- id: c
  content: |-
    $L = \frac{1}{2}$. The series is convergent
  correct: true
- id: d
  content: |-
    $L = 4$. The series is divergent
- id: e
  content: |-
    $L = 0$. The series is convergent
```

---

<a id="applying-the-ratio-test-for-divergence"></a>
## Applying the Ratio Test for Divergence

**Example:** Use the ratio test to show that $\displaystyle \sum_{n=1}^\infty \frac{(-1)^n\, n!}{3^n}$ is divergent.

**Explanation**

This is an example of an **alternating series**. The $(-1)^n$ causes the signs of the successive terms to alternate between positive and negative.

Let

$$
a_n = \dfrac{(-1)^n\,n!}{3^n}
$$

If we replace $n$ with $n+1$, we get

$$
\begin{aligned} a_{n+1}= \dfrac{(-1)^{n+1}(n+1)!}{3^{n+1}}= \frac{(-1)^{n+1}\,(n+1)!}{3\cdot 3^n}. \end{aligned}
$$

Now that we have expressions for the consecutive terms $a_n$ and $a_{n+1}$, we can work out the necessary limit:

$$
\begin{aligned} \require{cancel} L &=\lim_{n\to\infty}\left\begin{vmatrix}\frac{a_{n+1}}{a_n} \right & \\[5pt] &=\lim_{n\to\infty}\left & \dfrac{(-1)^{n+1}\,(n+1)!}{3\cdot 3^n} \div \dfrac{(-1)^n\,n!}{3^n}\right & \\[5pt] &=\lim_{n\to\infty}\left & \dfrac{(-1)^{n+1}\,(n+1)!}{3\cdot 3^n} \cdot \dfrac{3^n}{(-1)^n\,n!}\right & \\[5pt] &=\lim_{n\to\infty}\left & -\dfrac{n+1}{3}\right\end{vmatrix} \\[5pt] &=\dfrac 1 3\lim_{n\to\infty}\left(n+1\right) \\[5pt] &=\infty. \end{aligned}
$$

Since

$$
L=\infty > 1
$$

we conclude that the series is divergent by the ratio test.

---

**Question 3:**

```quiz
type: radio
id: ma-50726
content: |-
  Calculate $L = lim_(n → ∞) \mid \frac{a_{n + 1}}{a_{n}} \mid$ for the sequence $a_{n} = \frac{n!}{7^{n}}$. According to the ratio test, does $∑_(n = 1)^(∞)a_{n}$ converge or diverge?
options:
- id: a
  content: |-
    $L = 0$. The series is convergent
- id: b
  content: |-
    $L = \frac{1}{7}$. The series is convergent
- id: c
  content: |-
    $L = 1$. The ratio test is inconclusive
- id: d
  content: |-
    $L = ∞$. The series is divergent
  correct: true
- id: e
  content: |-
    $L = 7$. The series is divergent
```

---

**Question 4:**

```quiz
type: radio
id: ma-50789
content: |-
  Calculate $L = lim_(n → ∞) \mid \frac{a_{n + 1}}{a_{n}} \mid$ for the sequence $a_{n} = \frac{7^{n + 1}}{4^{n + 2}}$. According to the ratio test, does $∑_(n = 1)^(∞)a_{n}$ converge or diverge?
options:
- id: a
  content: |-
    $L = 1$. The ratio test is inconclusive
- id: b
  content: |-
    $L = \frac{4}{7}$. The series is convergent
- id: c
  content: |-
    $L = \frac{7}{4}$. The series is divergent
  correct: true
- id: d
  content: |-
    $L = \frac{7}{4}$. The series is convergent
- id: e
  content: |-
    $L = \frac{4}{7}$. The series is divergent
```

---

<a id="applying-the-ratio-test-in-the-indeterminate-case"></a>
## Applying the Ratio Test in the Indeterminate Case

**Example:** Use the ratio test to determine whether the series $\displaystyle\sum_{n=1}^\infty \frac{1}{2n+1}$ is convergent or divergent.

**Explanation**

Let

$$
a_n = \dfrac{1}{2n+1}
$$

If we replace $n$ with $n+1$, we get

$$
a_{n+1} = \frac{1}{2(n+1)+1}= \frac{1}{2n+3}
$$

Now that we have expressions for the consecutive terms $a_n$ and $a_{n+1}$, we can work out the necessary limit:

$$
\begin{aligned}
L &= lim_(n → ∞) \mid \frac{a_{n + 1}}{a_{n}} \mid \\
&= lim_(n → ∞) \mid \frac{a_{n + 1}}{a_{n}} \mid \\
&= lim_(n → ∞) \mid \frac{1}{2n + 3} \div \frac{1}{2n + 1} \mid \\
&= lim_(n → ∞)(\frac{1}{2n + 3} \cdot \frac{2n + 1}{1}) \\
&= lim_(n → ∞)(\frac{2n + 1}{2n + 3}) \\
&= lim_(n → ∞)(\frac{2 + \frac{1}{n}}{2 + \frac{3}{n}}) \\
&= \frac{2}{2} \\
&= 1
\end{aligned}
$$

Since $L=1$, the ratio test gives *no conclusion* about whether the series is convergent or divergent.

**Note:** Although the ratio test gave no conclusion, the series

$$
\displaystyle\sum_{n=1}^\infty \frac{1}{2n+1}
$$

is actually divergent.

---

**Question 5:**

```quiz
type: radio
id: ma-50725
content: |-
  Calculate $L = lim_(n → ∞) \mid \frac{a_{n + 1}}{a_{n}} \mid$ for the sequence $a_{n} = \frac{3n}{3n^{2} + 7}$. According to the ratio test, does $∑_(n = 1)^(∞)a_{n}$ converge or diverge?
options:
- id: a
  content: |-
    $L = \frac{1}{3}$. The series converges
- id: b
  content: |-
    $L = \frac{7}{3}$. The series diverges
- id: c
  content: |-
    $L = \frac{3}{7}$. The series converges
- id: d
  content: |-
    $L = 3$. The series diverges
- id: e
  content: |-
    $L = 1$. The ratio test is inconclusive
  correct: true
```

---

**Question 6:**

```quiz
type: radio
id: ma-50742
content: |-
  Calculate $L = lim_(n → ∞) \mid \frac{a_{n + 1}}{a_{n}} \mid$ for the sequence $a_{n} = (2(-1)^{n})/(3n + 1)$. According to the ratio test, does $∑_(n = 1)^(∞)a_{n}$ converge or diverge?
options:
- id: a
  content: |-
    $L = \frac{3}{2}$. The series diverges
- id: b
  content: |-
    $L = \frac{1}{3}$. The series converges
- id: c
  content: |-
    $L = 6$. The series diverges
- id: d
  content: |-
    $L = 1$. The ratio test is inconclusive
  correct: true
- id: e
  content: |-
    $L = \frac{2}{3}$. The series converges
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
