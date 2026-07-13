# Recognizing Standard Maclaurin Series

<!--
lesson-id: 884
topic-code: CA2.4.7.6
-->

## Table of Contents

- [Introduction](#introduction)
- [A List of Standard Maclaurin Series](#a-list-of-standard-maclaurin-series)
- [Recognizing a Geometric Series](#recognizing-a-geometric-series)
- [Recognizing Series That Are Similar to the Maclaurin Expansion for the Exponential Function](#recognizing-series-that-are-similar-to-the-maclaurin-expansion-for-the-exponential-function)
- [Recognizing Series That Are Similar to the Maclaurin Expansion for the Natural Logarithm](#recognizing-series-that-are-similar-to-the-maclaurin-expansion-for-the-natural-logarithm)

## Prerequisites

- [Representing Functions as Power Series](<../../../../MA/Mathematical-Foundations/MF3/8. Differentiation/8.4. Taylor Series/Lessons/8.4.7. Representing Functions as Power Series.md>)

---

<a id="introduction"></a>
## Introduction

Consider the infinite sum

$$
1 + 7 + \dfrac{7^2}{2!} + \dfrac{7^3}{3!} + \cdots + \dfrac{7^n}{n!} + \cdots\,
$$

By examining the series, we recognize that it looks similar to the Maclaurin expansion for

$$
f(x) = e^x
$$

$$
\begin{aligned}
e^{x} &= 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + ⋯ + \frac{x^{n}}{n!} + ⋯ \\
&= 1 + [math]\phantom{x}[/math] + \frac{[math]\phantom{x}[/math]^{2}}{2!} + \frac{[math]\phantom{x}[/math]^{3}}{3!} + ⋯ + \frac{[math]\phantom{x}[/math]^{n}}{n!} + ⋯
\end{aligned}
$$

Now, substituting $x=7$ into our Maclaurin expansion gives

$$
\begin{aligned}
e^{7} &= 1 + (7) + ((7)^{2})/(2!) + ((7)^{3})/(3!) + ⋯ + ((7)^{n})/(n!) + ⋯ \\
e^{7} &= 1 + 7 + \frac{7^{2}}{2!} + \frac{7^{3}}{3!} + ⋯ + \frac{7^{n}}{n!} + ⋯
\end{aligned}
$$

Therefore, the sum of the series is $e^7$.

---

<a id="a-list-of-standard-maclaurin-series"></a>
## A List of Standard Maclaurin Series

We need to recognize when a particular series looks like a standard Maclaurin series. A list of some common Maclaurin series is given below.

$\begin{bmatrix}MATH: \frac{1}{1 - x} = 1 + x + x^{2} + ⋯ + x^{n} + ⋯ = ∑_(n = 0)^(∞)x^{n}, & x ∈ (-1, 1) \\ \frac{1}{1 + x} = 1 - x + x^{2} - ⋯ + (-1)^{n}x^{n} + ⋯ = ∑_(n = 0)^(∞)(-1)^{n}x^{n}, & x ∈ (-1, 1) \\ e^{x} = 1 + x + \frac{1}{2!}x^{2} + ⋯ + \frac{x^{n}}{n!} + ⋯ = ∑_(n = 0)^(∞)\frac{x^{n}}{n!}, & x ∈ (- ∞, ∞) \\ \ln (1 + x) = x - \frac{1}{2}x^{2} + \frac{1}{3}x^{3} - ⋯ + ((-1)^{n + 1}x^{n})/(n) + ⋯ = ∑_(n = 1)^(∞)((-1)^{n + 1}x^{n})/(n), & x ∈ (-1, 1\end{bmatrix}; \sin (x) = x - \frac{1}{3!}x^{3} + \frac{1}{5!}x^{5} + ⋯ + ((-1)^{n}x^{2n + 1})/((2n + 1)!) + ⋯ = ∑_(n = 0)^(∞)((-1)^{n}x^{2n + 1})/((2n + 1)!),\begin{vmatrix}x ∈ (- ∞, ∞) \\ \cos (x) = 1 - \frac{1}{2!}x^{2} + \frac{1}{4!}x^{4} - ⋯ + ((-1)^{n}x^{2n})/((2n)!) + ⋯ = ∑_(n = 0)^(∞)((-1)^{n}x^{2n})/((2n)!),\end{vmatrix}x ∈ (- ∞, ∞)]$

In this lesson, we will focus on recognizing the standard Maclaurin series for the geometric series, the exponential function, and the natural logarithm

---

<a id="recognizing-a-geometric-series"></a>
## Recognizing a Geometric Series

**Example:** What is the sum of the series $1+\dfrac{2}{3} + \dfrac{4}{9} + \dfrac{8}{27} + \cdots + \dfrac{2^n}{3^n}+\cdots\,$?

**Explanation**

The first thing we notice is that we can rewrite the terms of the series as powers of

$$
\dfrac{2}{3}
$$

$$
\begin{aligned}
1 + \frac{2}{3} + \frac{4}{9} + \frac{8}{27} + ⋯ + \frac{2^{n}}{3^{n}} + ⋯ &= 1 + \frac{2}{3} + \frac{2^{2}}{3^{2}} + \frac{2^{3}}{3^{3}} + ⋯ + \frac{2^{n}}{3^{n}} + ⋯ \\
&= 1 + \frac{2}{3} + (\frac{2}{3})^{2} + (\frac{2}{3})^{3} + ⋯ + (\frac{2}{3})^{n} + ⋯
\end{aligned}
$$

Then, we recognize that the series looks similar to the Maclaurin expansion for

$$
f({\color{blue}x}) = \dfrac{1}{1-{\color{blue}x}}
$$

$$
\begin{aligned}
\frac{1}{1 - x} &= 1 + x + x^{2} + x^{3} + ⋯ + x^{n} + ⋯
\end{aligned}
$$

Substituting

$$
x={\color{blue}\dfrac{2}{3}}
$$

into our Maclaurin expansion gives

$$
\begin{aligned}
(1)/((1 - \frac{2}{3})) &= 1 + \frac{2}{3} + (\frac{2}{3})^{2} + (\frac{2}{3})^{3} + ⋯ + (\frac{2}{3})^{n} + ⋯ \\
3 &= 1 + \frac{2}{3} + \frac{4}{9} + \frac{8}{27} + ⋯ + \frac{2^{n}}{3^{n}} + ⋯
\end{aligned}
$$

Therefore, the sum of the series is $3$.

---

**Question 1:**

```quiz
type: radio
id: ma-50917
content: |-
  What is $1 - \frac{1}{6} + \frac{1}{36} - ⋯ + ((-1)^{n})/(6^{n}) + ⋯$?
options:
- id: a
  content: |-
    $\frac{1}{7}$
- id: b
  content: |-
    $\ln 7$
- id: c
  content: |-
    $-e^{6}$
- id: d
  content: |-
    $\frac{6}{7}$
  correct: true
- id: e
  content: |-
    $\sin (6)$
```

---

**Question 2:**

```quiz
type: radio
id: ma-50894
content: |-
  Find the sum of the series $1 + \frac{1}{3} + \frac{1}{9} + ⋯ + \frac{1}{3^{n}} + ⋯$.
options:
- id: a
  content: |-
    $\frac{3}{2}$
  correct: true
- id: b
  content: |-
    $\ln 3$
- id: c
  content: |-
    $-\ln 3$
- id: d
  content: |-
    $\frac{1}{3}$
- id: e
  content: |-
    $\sin (3)$
```

---

<a id="recognizing-series-that-are-similar-to-the-maclaurin-expansion-for-the-exponential-function"></a>
## Recognizing Series That Are Similar to the Maclaurin Expansion for the Exponential Function

**Example:** Find the sum $3 + \dfrac{4}{2!} + \dfrac{8}{3!}+ \cdots + \dfrac{2^n}{n!}+ \cdots\,$.

**Explanation**

We recognize that the series looks similar to the Maclaurin expansion for

$$
f(x) = e^x
$$

$$
e^{x} = 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + ⋯ + \frac{x^{n}}{n!} + ⋯
$$

Substituting

$$
x={\color{blue}2}
$$

into our Maclaurin expansion gives

$$
\begin{aligned}
e^{2} &= 1 + 2 + \frac{2^{2}}{2!} + \frac{2^{3}}{3!} + ⋯ + \frac{2^{n}}{n!} + ⋯ \\
e^{2} &= 3 + \frac{4}{2!} + \frac{8}{3!} + ⋯ + \frac{2^{n}}{n!} + ⋯
\end{aligned}
$$

Therefore, the sum of the series is $e^2$.

---

**Question 3:**

```quiz
type: radio
id: ma-50939
content: |-
  Find the sum $2 + \frac{1}{2!} + \frac{1}{3!} + ⋯ + \frac{1}{n!} + ⋯$.
options:
- id: a
  content: |-
    $e$
  correct: true
- id: b
  content: |-
    $e^{2}$
- id: c
  content: |-
    The series is divergent
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $1$
```

---

**Question 4:**

```quiz
type: radio
id: ma-50928
content: |-
  Find the sum $1 + \ln π + ((\ln π)^{2})/(2!) + ⋯ + ((\ln π)^{n})/(n!) + ⋯$.
options:
- id: a
  content: |-
    $π^{2}$
- id: b
  content: |-
    The series is divergent
- id: c
  content: |-
    $e$
- id: d
  content: |-
    $π$
  correct: true
- id: e
  content: |-
    $e^{2}$
```

---

<a id="recognizing-series-that-are-similar-to-the-maclaurin-expansion-for-the-natural-logarithm"></a>
## Recognizing Series That Are Similar to the Maclaurin Expansion for the Natural Logarithm

**Example:** Find the sum $\, \dfrac{2}{3} - \dfrac{(2/3)^2}{2} + \dfrac{(2/3)^3}{3} + \cdots +\dfrac{(-1)^{n+1}(2/3)^n}{n}+\cdots\,$.

**Explanation**

Notice that we can rewrite the given sum as follows:

$$
\frac{2}{3} - ((2/3)^{2})/(2) + ((2/3)^{3})/(3) + ⋯ + ((-1)^{n + 1}(2/3)^{n})/(n) + ⋯
$$

Then, we recognize that the series looks similar to the Maclaurin expansion for

$$
f(x) = \ln(1+x)
$$

$$
\begin{aligned}
\ln (1 + x) &= x - \frac{x^{2}}{2} + \frac{x^{3}}{3} + ⋯
\end{aligned}
$$

Substituting

$$
x={\color{blue}\dfrac{2}{3}}
$$

into our Maclaurin expansion gives

$$
\begin{aligned}
\ln (1 + \frac{2}{3}) &= \frac{2}{3} - ((2/3)^{2})/(2) + ((2/3)^{3})/(3) + ⋯ + ((-1)^{n + 1}(2/3)^{n})/(n) + ⋯ \\
\ln (\frac{5}{3}) &= \frac{2}{3} - ((2/3)^{2})/(2) + ((2/3)^{3})/(3) + ⋯ + ((-1)^{n + 1}(2/3)^{n})/(n) + ⋯
\end{aligned}
$$

Therefore, the sum of the series is

$$
\ln\left(\dfrac{5}{3}\right)
$$

---

**Question 5:**

```quiz
type: radio
id: ma-50965
content: |-
  What is $\frac{1}{2} - \frac{1}{8} + \frac{1}{24} + ⋯ + ((-1)^{n + 1}(1/2)^{n})/(n) + ⋯$?
options:
- id: a
  content: |-
    $\ln (\frac{2}{3})$
- id: b
  content: |-
    $\ln \ln 3$
- id: c
  content: |-
    $3\ln 2$
- id: d
  content: |-
    The series is divergent
- id: e
  content: |-
    $\ln (\frac{3}{2})$
  correct: true
```

---

**Question 6:**

```quiz
type: radio
id: ma-50961
content: |-
  Find the sum $\ln 2 - ((\ln 2)^{2})/(2) + ((\ln 2)^{3})/(3) - ⋯ + ((-1)^{n + 1}(\ln 2)^{n})/(n) + ⋯$.
options:
- id: a
  content: |-
    $\ln (1 + \ln 2)$
  correct: true
- id: b
  content: |-
    $2\ln 2$
- id: c
  content: |-
    $\ln \ln 2$
- id: d
  content: |-
    $\ln 2$
- id: e
  content: |-
    The series is divergent
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
