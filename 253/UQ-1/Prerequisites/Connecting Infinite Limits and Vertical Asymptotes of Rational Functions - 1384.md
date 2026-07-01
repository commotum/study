# Connecting Infinite Limits and Vertical Asymptotes of Rational Functions

## Table of Contents

- [Introduction](#introduction)
- [Evaluating the Right-Sided Limit of a Rational Function at a Vertical Asymptote](#evaluating-the-right-sided-limit-of-a-rational-function-at-a-vertical-asymptote)
- [Evaluating the Left-Sided Limit of a Rational Function at a Vertical Asymptote](#evaluating-the-left-sided-limit-of-a-rational-function-at-a-vertical-asymptote)
- [Identifying Correct Limits of a Given Rational Function](#identifying-correct-limits-of-a-given-rational-function)
- [Identifying Correct Limits of a Given Function when Simplification is Required](#identifying-correct-limits-of-a-given-function-when-simplification-is-required)

## Prerequisites

- [Vertical Asymptotes of Rational Functions](../1815/1815.md)
- [Limits of Reciprocal Functions](../1905/1905.md)

---

<a id="introduction"></a>
## Introduction

Rational functions have infinite limits when the $x$-value approaches vertical asymptotes. To find the infinite limits of a rational function $f(x)$, we first find the vertical asymptotes.

For example, consider the rational function

$$
f(x) = \dfrac{1}{x-2}
$$

This rational function has a vertical asymptote at $x=2$.

To find the one-sided limits at the asymptote $x=2$, we check the sign of $f(x)$ as $x$ approaches $2$ from the left and the right.

- To find the limit as $x \to 2^-$, we evaluate $f(x)$ at $x$-values very close to $x=2$ from the left:

| $x$ | $1.9$ | $1.99$ | $1.999$ |
| --- | ---: | ---: | ---: |
| $f(x)$ | $-10$ | $-100$ | $-1\,000$ |

The values of $f(x)$ are negative, and they get more and more negative. Therefore,

$$
\lim\limits_{x \to 2^-} f(x) = -\infty
$$

- To find the limit as $x \to 2^+$, we evaluate $f(x)$ at $x$-values very close to $x=2$ from the right:

| $x$ | $2.1$ | $2.01$ | $2.001$ |
| --- | ---: | ---: | ---: |
| $f(x)$ | $10$ | $100$ | $1\,000$ |

The values of $f(x)$ are positive, and they get larger and larger. Therefore,

$$
\lim\limits_{x \to 2^+} f(x) = +\infty
$$

These one-sided limits match up with what we see in the graph of $f(x)$, shown below.

![](<../Source/Connecting Infinite Limits and Vertical Asymptotes of Rational Functions - 1384/Images/1f0de881aee9cf164ae6f91299a59145.png>)

---

<a id="evaluating-the-right-sided-limit-of-a-rational-function-at-a-vertical-asymptote"></a>
## Evaluating the Right-Sided Limit of a Rational Function at a Vertical Asymptote

**Example:** Evaluate $\lim\limits_{x \to 3^+} \dfrac{1}{x^2-x-6}$.

**Explanation**

First, notice that we can factor the function, as follows:

$$
f(x) = \dfrac{1}{x^2-x-6} = \dfrac{1}{(x-3)(x+2)}
$$

So, the function $f(x)$ has two vertical asymptotes, $x=-2$ and $x=3$.

Since $x=3$ is a vertical asymptote, the limit as $x \to 3^+$ will be either $+\infty$ or $-\infty$.

To find the limit as $x \to 3^+$, we evaluate $f(x)$ at $x$-values very close to $x=3$ from the right:

| $x$ | $3.1$ | $3.01$ | $3.001$ |
| --- | ---: | ---: | ---: |
| $f(x)$ | $\approx 1.96$ | $\approx 19.96$ | $\approx 199.96$ |

The values of $f(x)$ are positive, and they get larger and larger. Therefore,

$$
\lim\limits_{x \to 3^+} f(x) = +\infty
$$

This matches up with what we see in the graph of $f(x)$, shown below.

![](<../Source/Connecting Infinite Limits and Vertical Asymptotes of Rational Functions - 1384/Images/699affabb0d7d5f074de07be10a3540c.png>)

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-1384-q001
content: |-
  > A calculator is required to answer this question.
  
  Evaluate $\lim_{x \to (-3)^{+}}\frac{x^{2} + 4}{3x^{2} - 27}$.
options:
- id: a
  content: |-
    $-\frac{1}{9}$
- id: b
  content: |-
    $\frac{1}{3}$
- id: c
  content: |-
    DNE
- id: d
  content: |-
    $∞$
- id: e
  content: |-
    $- ∞$
  correct: true
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-1384-q002
content: |-
  > A calculator is required to answer this question.
  
  Evaluate $\lim_{x \to 2^{+}}\frac{x^{2} + 2x - 3}{10x - 20}$.
options:
- id: a
  content: |-
    $- ∞$
- id: b
  content: |-
    DNE
- id: c
  content: |-
    $+ ∞$
  correct: true
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $-\frac{1}{2}$
```
---

<a id="evaluating-the-left-sided-limit-of-a-rational-function-at-a-vertical-asymptote"></a>
## Evaluating the Left-Sided Limit of a Rational Function at a Vertical Asymptote

**Example:** Calculate $\lim\limits_{x \to 1^-} \dfrac{1}{x^2+x - 2}$.

**Explanation**

First, let's factor the denominator.

$$
\begin{aligned}
f(x) &= \frac{1}{x^{2} + x - 2} \\
&= \frac{1}{x^{2} + 2x - x - 2} \\
&= (1)/(x(x + 2) - (x + 2)) \\
&= (1)/((x - 1)(x + 2))
\end{aligned}
$$

This implies that the function $f(x)$ has two vertical asymptotes, $x=-2$ and $x=1$.

Since $x=1$ is a vertical asymptote, the limit as $x \to 1^-$ will be either $+\infty$ or $-\infty$.

To find the limit is $x \to 1^-$, we evaluate $f(x)$ at $x$-values very close to $x=1$ from the left:

| $x$ | $0.9$ | $0.99$ | $0.999$ |
| --- | ---: | ---: | ---: |
| $f(x)$ | $\approx -3$ | $\approx -33$ | $\approx -333$ |

The values of $f(x)$ are negative, and they get more and more negative. Therefore,

$$
\lim\limits_{x \to 1^-} f(x)= -\infty
$$

This matches up with what we see in the graph of $f(x)$, shown below.

![](<../Source/Connecting Infinite Limits and Vertical Asymptotes of Rational Functions - 1384/Images/0516da9f3887ae8d8817d11c13cd2d24.png>)

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-1384-q003
content: |-
  > A calculator is required to answer this question.
  
  Calculate $\lim_{x \to (-1)^{-}}\frac{x}{2x^{2} - 2}$.
options:
- id: a
  content: |-
    $- ∞$
  correct: true
- id: b
  content: |-
    $+ ∞$
- id: c
  content: |-
    DNE
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $-\frac{1}{4}$
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-1384-q004
content: |-
  > A calculator is required to answer this question.
  
  Calculate $\lim_{x \to 4^{-}}(- (1)/(x(x - 4)))$.
options:
- id: a
  content: |-
    $+ ∞$
  correct: true
- id: b
  content: |-
    DNE
- id: c
  content: |-
    $\frac{1}{4}$
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $- ∞$
```
---

<a id="identifying-correct-limits-of-a-given-rational-function"></a>
## Identifying Correct Limits of a Given Rational Function

**Example:** Given that $f(x) = \dfrac{x}{(x-1)^2}$, which of the following statements is correct?

1. $\lim\limits_{x \to 1^-}f(x)= -\infty$
2. $\lim\limits_{x \to 1^+} f(x)= +\infty$
3. $\lim\limits_{x \to 1} f(x)= +\infty$

**Explanation**

The function

$$
f(x)= \dfrac{x}{(x-1)^2}
$$

has a vertical asymptote at $x=1$.

To compute the one-sided limits as $x \to 1$, we evaluate $f(x)$ at $x$-values very close to $x=1$ from the right and from the left.

| $x$ | $0.9$ | $0.99$ | $1$ | $1.01$ | $1.1$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $f(x)$ | $90$ | $9\,900$ | $\text{undefined}$ | $10\,100$ | $110$ |

All the values of $f(x)$ are positive, and they get larger and larger as $x\to1$ from both sides. Therefore,

$$
\lim\limits_{x \to 1^-} f(x)=\lim\limits_{x \to 1^+} f(x)= +\infty
$$

Consequently, statement I is false and II is true.

Finally, since both left and right-sided limits at $x=1$ are equal, we have

$$
\lim\limits_{x \to 1} f(x)= +\infty
$$

and therefore III is true.

In conclusion, only statements II and III are true. A plot of the function is shown below.

![](<../Source/Connecting Infinite Limits and Vertical Asymptotes of Rational Functions - 1384/Images/dffdf7de5a57d6d0adefc1ede9d7672e.png>)

---

**Question 5:**

```quiz
type: radio
id: MA253-UQ1-1384-q005
content: |-
  > A calculator is required to answer this question.
  
  Given that $f(x) = (2x)/((x - 2)^{2})$, which of the following statements is correct?
  
  1. $\lim_{x \to 2^{-}}f(x) = + ∞$
  2. $\lim_{x \to 2}f(x) = + ∞$
  3. $\lim_{x \to 2^{+}}f(x) = - ∞$
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    II only
- id: c
  content: |-
    I and II only
  correct: true
- id: d
  content: |-
    III only
- id: e
  content: |-
    I and III only
```
---

**Question 6:**

```quiz
type: radio
id: MA253-UQ1-1384-q006
content: |-
  > A calculator is required to answer this question.
  
  Given that $f(x) = (x^{2})/((x - 1)^{3})$, which of the following statements is correct?
  
  1. $\lim_{x \to 1^{-}}f(x) = + ∞$
  2. $\lim_{x \to 1}f(x) = + ∞$
  3. $\lim_{x \to 1^{+}}f(x) = + ∞$
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    II and III only
- id: c
  content: |-
    III only
  correct: true
- id: d
  content: |-
    I and II only
- id: e
  content: |-
    I, II and III
```
---

<a id="identifying-correct-limits-of-a-given-function-when-simplification-is-required"></a>
## Identifying Correct Limits of a Given Function when Simplification is Required

**Example:** Given that $f(x) = \dfrac{2-x}{x^2-4}$, which of the following statements is correct?

1. $\lim\limits_{x \to (-2)^+}f(x)= -\infty$
2. $\lim\limits_{x \to 2^+}f(x)= -\infty$
3. $\lim\limits_{x \to 2^-}f(x)= \infty$

**Explanation**

First, let's factor the numerator and denominator, as follows:

$$
\begin{aligned}
f(x) &= \frac{2 - x}{x^{2} - 4} \\
&= - ((x - 2))/((x - 2)(x + 2))
\end{aligned}
$$

Therefore, the domain is

$$
x\neq \pm 2
$$

, and we notice that the function can be simplified:

$$
f(x) =-\frac{1}{x + 2}
$$

Now we see that the function has only one vertical asymptote, $x=-2$. So statements II and III are false.

To find $\lim\limits_{x \to (-2)^+}f(x)$, we evaluate $f(x)$ at $x$-values very close to $x=-2$ from the right.

| $x$ | $-1.9$ | $-1.99$ | $-1.999$ |
| --- | ---: | ---: | ---: |
| $f(x)$ | $-10$ | $-100$ | $-1\,000$ |

All the values of $f(x)$ are negative, and they get more and more negative as $x\to-2$ from the right. Therefore,

$$
\lim\limits_{x \to (-2)^+}f(x) = -\infty
$$

and therefore statement I is correct.

In conclusion, only statement I is correct. A plot of the function is shown below.

![](<../Source/Connecting Infinite Limits and Vertical Asymptotes of Rational Functions - 1384/Images/19b67df6adf3aba2408de6918e1836f4.png>)

---

**Question 7:**

```quiz
type: radio
id: MA253-UQ1-1384-q007
content: |-
  > A calculator is required to answer this question.
  
  Given that $f(x) = \frac{x + 3}{x^{2} - 9}$, which of the following statements is correct?
  
  1. $\lim_{x \to (-3)^{-}}f(x) = - ∞$
  2. $\lim_{x \to (-3)^{+}}f(x) = + ∞$
  3. $\lim_{x \to 3^{+}}f(x) = ∞$
options:
- id: a
  content: |-
    I only
- id: b
  content: |-
    II only
- id: c
  content: |-
    I and III only
- id: d
  content: |-
    III only
  correct: true
- id: e
  content: |-
    I and II only
```
---

**Question 8:**

```quiz
type: radio
id: MA253-UQ1-1384-q008
content: |-
  > A calculator is required to answer this question.
  
  Given that $f(x) = \frac{2x + 2}{x^{2} - 1}$, which of the following statements is correct?
  
  1. $\lim_{x \to 1^{-}}f(x) = - ∞$
  2. $\lim_{x \to (-1)^{+}}f(x) = + ∞$
  3. $\lim_{x \to (-1)^{-}}f(x) = - ∞$
options:
- id: a
  content: |-
    II and III only
- id: b
  content: |-
    II only
- id: c
  content: |-
    I only
  correct: true
- id: d
  content: |-
    I and II only
- id: e
  content: |-
    I and III only
```
---

## Navigation

- [Next: Calculating Limits of Radical Functions Using Conjugate Multiplication](<Calculating Limits of Radical Functions Using Conjugate Multiplication - 604.md>)
- [Back to UQ-1](../UQ-1.md)
