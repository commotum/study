# Absolute and Conditional Convergence

<!--
lesson-id: 748
topic-code: CA2.4.5.10
-->

## Table of Contents

- [Introduction](#introduction)
- [Determining Absolute Convergence](#determining-absolute-convergence)
- [Determining Conditional Convergence](#determining-conditional-convergence)
- [Rearranging the Terms of Infinite Series](#rearranging-the-terms-of-infinite-series)
- [Rearranging Terms of an Absolutely Convergent Series](#rearranging-terms-of-an-absolutely-convergent-series)
- [Rearranging Terms of a Conditionally Convergent Series](#rearranging-terms-of-a-conditionally-convergent-series)

## Prerequisites

- [The Ratio Test](<../../../../../../MA/DATA/Lessons/746/746.md>)
- [The Alternating Series Test](<../../../../../../MA/DATA/Lessons/747/747.md>)
- [The Limit Comparison Test](<../../../../../../MA/DATA/Lessons/750/750.md>)

---

<a id="introduction"></a>
## Introduction

Let's consider the alternating series

$$
\sum_{n=1}^\infty b_n
$$

where

$$
b_n = (-1)^n a_n \quad \textrm{or}\quad b_n = (-1)^{n+1} a_n, \quad a_n > 0
$$

We have the following:

- If $\displaystyle \sum_{n =1}^\infty \mid b_n \mid$ is convergent, then $\displaystyle \sum_{n =1}^\infty b_n$ is also convergent. We say that $\displaystyle \sum_{n =1}^\infty b_n$ is **absolutely convergent**.
- If $\displaystyle \sum_{n =1}^\infty \mid b_n \mid$ is divergent yet $\displaystyle \sum_{n =1}^\infty b_n$ is convergent, we say that $\displaystyle \sum_{n =1}^\infty b_n$ is **conditionally convergent**.

We can summarize this in one diagram, shown below.

![](<../Source/Absolute and Conditional Convergence - 748/Images/0515e11fdff6eb72f3c13458b5c263c8.png>)

Note the following:

- If a series is absolutely convergent, we say it **converges absolutely.**
- Likewise, if a series is conditionally convergent, we say it **converges conditionally.**
- Since absolute convergence of an alternating series implies convergence, we usually check for absolute convergence first.

---

<a id="determining-absolute-convergence"></a>
## Determining Absolute Convergence

**Example:** Given the series $\displaystyle\sum_{n = 1}^\infty \dfrac {(-1) ^ {n+1}} {n^2}$, which of the following statements are true?

1. The series is absolutely convergent
2. The series is conditionally convergent
3. The series is convergent

**Explanation**

We can summarize the test for the *absolute* and *conditional* convergence in the following diagram.

![](<../Source/Absolute and Conditional Convergence - 748/Images/1655d13f93713d788d29828257ff7763.png>)

With that in mind, let's check each statement in turn.

- Statement I is true. Checking for absolute convergence, we have
$∑_(n = 1)^(∞) \mid ((-1)^{n + 1})/(n^{2}) \mid |= ∑_(n = 1)^(∞)\frac{1}{n^{2}}$,
which is a $p$-series with $p = 2 > 1$. Therefore, the series converges absolutely.
- Statement II is false. Since the series is absolutely convergent, it cannot be conditionally convergent.
- Statement III is true. Since the series is absolutely convergent, it is also convergent.

Therefore, the correct answer is "I and III only."

---

**Question 1**

```quiz
type: radio
id: ma-16050
content: |-
  Given the series $∑_(n = 1)^(∞)((-1)^{n})/(6\sqrt{n^{5}})$, which of the following statements are true?

  1. The series is absolutely convergent
  2. The series is conditionally convergent
  3. The series is divergent
options:
- id: a
  content: |-
    II only
- id: b
  content: |-
    I and III only
- id: c
  content: |-
    I only
  correct: true
- id: d
  content: |-
    II and III only
- id: e
  content: |-
    I and II only
```

---

**Question 2**

```quiz
type: radio
id: ma-15991
content: |-
  Given the series $∑_(n = 1)^(∞)((-1)^{n + 1})/(\sqrt{n^{3}})$, which of the following statements are true?

  1. The series is absolutely convergent
  2. The series is conditionally convergent
  3. The series is convergent
options:
- id: a
  content: |-
    III only
- id: b
  content: |-
    II and III only
- id: c
  content: |-
    I and III only
  correct: true
- id: d
  content: |-
    II only
- id: e
  content: |-
    I and II only
```

---

<a id="determining-conditional-convergence"></a>
## Determining Conditional Convergence

**Example:** For the series $\displaystyle \sum_{n = 1} ^ \infty \dfrac {(-1) ^ {n+1}} {n}$, which of the following statements are true?

1. The series is absolutely convergent
2. The series is conditionally convergent
3. The series is divergent

**Explanation**

We can summarize the test for the *absolute* and *conditional* convergence in the following diagram.

![](<../Source/Absolute and Conditional Convergence - 748/Images/9a01ae0f40b55395ce9a10b3f84a0c16.png>)

With that in mind, let's check each statement in turn.

- Statement I is false. Checking for absolute convergence, we have
$∑_(n = 1)^(∞) \mid ((-1)^{n + 1})/(n) \mid |= ∑_(n = 1)^(∞)\frac{1}{n}$
which is a $p$-series with $p = 1$. Therefore, the series does not converge absolutely.
- Statement II is true while statement III is false. Clearly, the sequence $a_n = \dfrac{1}{n}$ is positive and decreasing for all $n \geq 1$, and $a_n \to 0$ as $n\to\infty$. Hence, $\displaystyle\sum\limits_{n = 1}^\infty\dfrac{(-1)^{n+1}}{n}$ converges by the alternating series test.

Therefore, the correct answer is "II only."

---

**Question 3**

```quiz
type: radio
id: ma-16041
content: |-
  For the series $∑_(n = 1)^(∞)((-1)^{n})/(\sqrt{n})$, which of the following statements are true?

  1. The series is absolutely convergent
  2. The series is conditionally convergent
  3. The series is divergent
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    II and III only
- id: c
  content: |-
    II only
  correct: true
- id: d
  content: |-
    I and II only
- id: e
  content: |-
    III only
```

---

**Question 4**

```quiz
type: radio
id: ma-125471
content: |-
  For the series $∑_(n = 1)^(∞)((-1)^{n}\sqrt{n})/(n + 3)$, which of the following statements are true?

  1. The series is absolutely convergent
  2. The series is conditionally convergent
  3. The series is divergent
options:
- id: a
  content: |-
    III only
- id: b
  content: |-
    I only
- id: c
  content: |-
    II and III only
- id: d
  content: |-
    II only
  correct: true
- id: e
  content: |-
    I and III only
```

---

<a id="rearranging-the-terms-of-infinite-series"></a>
## Rearranging the Terms of Infinite Series

When we permute the terms in a *finite* series, the result is always the same.

For example, if we compute the sum of the first $100$ integers, we get

$$
1+2+3+\cdots+100 = 5\,050
$$

Now, if we sum the same terms but group them according to whether they're even or odd, we get the same answer:

$$
(1 + 3 + 5+\cdots + 99) + (2+4+6+\cdots + 100) = 5\,050
$$

For *infinite* series, things are not so simple!

Whether or not we can rearrange the order of the terms depends on whether our infinite series converges absolutely or conditionally.

Let's consider an example of each case:

- If a series is absolutely convergent, we can permute the terms, and the sum of the series will remain the same.For example, it can be shown that
$\frac{1}{1!} - \frac{1}{2!} + \frac{1}{3!} - \frac{1}{4!} + ⋯ = \frac{e - 1}{e}$.
This series is absolutely convergent. So, if we rearrange the terms by grouping the even and odd factorials, we'll get the same result:
$(\frac{1}{1!} + \frac{1}{3!} + ⋯) - (\frac{1}{2!} + \frac{1}{4!} + ⋯) = \frac{e - 1}{e}$.

- If a series is *conditionally* convergent, then we *cannot* rearrange the terms and be guaranteed to get the same result!For example, consider the following alternating series:
$1-1+\dfrac12-\dfrac12+\dfrac13-\dfrac13+\dfrac14-\dfrac14\cdots = 0$
The sum of this series is zero since the partial sums become arbitrarily small as we increase the number of terms.However, suppose we rearrange the terms of this series by taking the first two positive terms, followed by the first negative term, then the next two positive terms, followed by the second negative term, etc. It can be shown that
$\left(1+\dfrac12 - 1\right) + \left(\dfrac13+\dfrac14 - \dfrac12\right) + \cdots = \ln 2$
which is different from zero!Moreover, if a series converges conditionally, then given any real number, there exists a rearrangement of the terms such that the new series converges to that number! We can even rearrange the terms of a conditionally convergent series so that the new (permuted) series is *divergent*!

The key takeaway is that we can *only* permute the terms in an infinite series if it is absolutely convergent.

---

<a id="rearranging-terms-of-an-absolutely-convergent-series"></a>
## Rearranging Terms of an Absolutely Convergent Series

**Example:** Let $S = \displaystyle \sum_{n=1}^\infty a_n$, where $a_n= \dfrac{(-1)^{n}}{n^2\sqrt[3]{n}}$. Which of the following statements are true?

1. $\displaystyle \sum_{n=1}^\infty \mid a_n \mid$ is convergent
2. $\displaystyle \sum_{n=1}^\infty a_n$ is convergent
3. The terms of the series $\displaystyle \sum_{n=1}^\infty a_n$ can be rearranged so that the new series converges to $\dfrac{S}{3}$

**Explanation**

We can summarize the test for the *absolute* and *conditional* convergence in the following diagram.

![](<../Source/Absolute and Conditional Convergence - 748/Images/01bee406fd8ad2860ead6c2fe1c4267f.png>)

Let's check each statement in turn.

- Statement I is true. Indeed, we have
$\sum_{n=1}^\infty \left|\dfrac{(-1)^{n}}{n^2\sqrt[3]{n}}\right| =\sum_{n=1}^\infty \dfrac{1}{n^{7/3}}$,
which is a $p$-series with $p = \dfrac{7}{3} > 1$. Therefore, the series is absolutely convergent.
- Statement II is true. Since the series is absolutely convergent, it is also convergent.
- Statement III is false. Since the series converges absolutely, any rearrangement of its terms results in a series that converges to the same value as the original arrangement.

Therefore, the correct answer is "I and II only."

---

**Question 5**

```quiz
type: radio
id: ma-51782
content: |-
  Let $S = ∑_(n = 1)^(∞)a_{n}$, where $a_{n} = ((-1)^{n})/(5^{n})$. Which of the following statements are true?

  1. $∑_(n = 1)^(∞) \mid a_{n} \mid$ is convergent
  2. $∑_(n = 1)^(∞)a_{n}$ is divergent
  3. The terms of the series $∑_(n = 1)^(∞)a_{n}$ can be rearranged so that the new series converges to $S + 2$
options:
- id: a
  content: |-
    I only
  correct: true
- id: b
  content: |-
    II and III only
- id: c
  content: |-
    III only
- id: d
  content: |-
    II only
- id: e
  content: |-
    I and III only
```

---

**Question 6**

```quiz
type: radio
id: ma-51788
content: |-
  Let $S = ∑_(n = 1)^(∞)a_{n}$, where $a_{n} = ((-1)^{n})/((n + 1)^{2})$. Which of the following statements are true?

  1. $∑_(n = 1)^(∞) \mid a_{n} \mid$ is divergent
  2. $∑_(n = 1)^(∞)a_{n}$ is convergent
  3. The terms of the series $∑_(n = 1)^(∞)a_{n}$ can be rearranged so that the new series converges to $S - 5$
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    II only
  correct: true
- id: c
  content: |-
    I and II only
- id: d
  content: |-
    III only
- id: e
  content: |-
    I and III only
```

---

<a id="rearranging-terms-of-a-conditionally-convergent-series"></a>
## Rearranging Terms of a Conditionally Convergent Series

**Example:** Let $a_n= \dfrac{(-1)^n}{\sqrt[3] {n}}$. Which of the following statements are true?

1. $\displaystyle \sum_{n=1}^\infty \mid a_n \mid$ is convergent
2. $\displaystyle \sum_{n=1}^\infty a_n$ is convergent
3. The terms of the series $\displaystyle \sum_{n=1}^\infty a_n$ can be rearranged so that the new series converges to $5$

**Explanation**

We can summarize the test for the *absolute* and *conditional* convergence in the following diagram.

![](<../Source/Absolute and Conditional Convergence - 748/Images/e06c75b353eaa7bf195a5190ff2d43ed.png>)

Let's check each statement in turn.

- Statement I is false. Indeed, we have
$\begin{aligned} \sum_{n=1}^\infty \left|\dfrac{(-1)^{n}}{\sqrt[3]{n}}\right| & = \sum_{n=1}^\infty \dfrac{1}{\sqrt[3] {n}} \\[5pt] &= \sum_{n=1}^\infty \dfrac{1}{n^{1/3}}, \end{aligned}$
which is a $p$-series with $p = \dfrac{1}{3} < 1$. Therefore, the series does not converge absolutely.
- Statement II is true. The sequence $\mid a_n|=\dfrac{1}{\sqrt[3] {n}}$ is positive and decreasing for all $n\geq1$, and $\mid a_n \mid \to0$ as $n\to\infty$. Hence, $\displaystyle \sum_{n=1}^\infty a_n$ converges by the alternating series test.
- Statement III is true. Since the series converges but not absolutely, it is conditionally convergent. Therefore, given any number $S$, there exists a rearrangement of the terms such that the new series converges to $S$.

Therefore, the correct answer is "II and III only."

---

**Question 7**

```quiz
type: radio
id: ma-51781
content: |-
  Let $a_{n} = ((-1)^{n})/(\sqrt[5]{n^{2}})$. Which of the following statements are true?

  1. $∑_(n = 1)^(∞) \mid a_{n} \mid$ is convergent
  2. $∑_(n = 1)^(∞)a_{n}$ is convergent
  3. The terms of the series $∑_(n = 1)^(∞)a_{n}$ can be rearranged so that the new series converges to $3$
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    II and III only
  correct: true
- id: c
  content: |-
    III only
- id: d
  content: |-
    I and III only
- id: e
  content: |-
    I and II only
```

---

**Question 8**

```quiz
type: radio
id: ma-82924
content: |-
  Let $a_{n} = (3(-1)^{n})/(\sqrt{n + 2})$. Which of the following statements are true?

  1. $∑_(n = 1)^(∞) \mid a_{n} \mid$ is convergent
  2. $∑_(n = 1)^(∞)a_{n}$ is convergent
  3. The terms of the series $∑_(n = 1)^(∞)a_{n}$ can be rearranged so that the new series converges to $\sqrt{3}$
options:
- id: a
  content: |-
    III only
- id: b
  content: |-
    I and II only
- id: c
  content: |-
    I and III only
- id: d
  content: |-
    II and III only
  correct: true
- id: e
  content: |-
    II only
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
