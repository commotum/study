# Limits Involving the Exponential Function

<!--
lesson-id: 2610
topic-code: MF3.7.1.4
-->

## Table of Contents

- [Introduction](#introduction)
- [Evaluating a Limit Using the Limit Definition of Euler's Number](#evaluating-a-limit-using-the-limit-definition-of-eulers-number)
- [Evaluating a Limit Using the Limit Definition of Euler's Number: Limits Containing Variables](#evaluating-a-limit-using-the-limit-definition-of-eulers-number-limits-containing-variables)
- [Another Definition of the Exponential Function](#another-definition-of-the-exponential-function)
- [Applying the Limit Definition of the Exponential Function](#applying-the-limit-definition-of-the-exponential-function)

## Prerequisites

- [The Power and Root Rules for Limits](<../../../../CAB/1. Limits and Continuity/1.2. The Algebra of Limits/Lessons/1.2.4. The Power and Root Rules for Limits.md>)
- [Limits of Exponential Functions](<../../../../CAB/1. Limits and Continuity/1.3. Limits of Functions/Lessons/1.3.3. Limits of Exponential Functions.md>)

---

<a id="introduction"></a>
## Introduction

Let's consider the following limit:

$$
\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n}
$$

Notice that as $n \to \infty$,

- the expression inside the parentheses approaches $1$, while
- the exponent approaches $\infty$.

If we attempt to evaluate the limit directly, we get

$$
\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n} = 1^\infty
$$

which is an indeterminate form (i.e., its meaning is ambiguous and therefore cannot be used to determine the true value of the limit). So, if we want to evaluate this limit, we need to find another way to do it.

To get a feel for how this limit behaves, we create a table of values, as follows:

| $n$ | $\left(1+\dfrac{1}{n}\right)^{n}$ |
| --- | ---: |
| $1$ | $2.000\,00$ |
| $10$ | $2.593\,74$ |
| $100$ | $2.704\,81$ |
| $1\,000$ | $2.716\,92$ |
| $10\,000$ | $2.718\,15$ |
| $100\,000$ | $2.718\,27$ |
| $1\,000\,000$ | $2.718\,28$ |

Now, recall Euler's number

$$
e\approx 2.718\,28
$$

to five decimal places. It appears that our expression converges to $e$ as $n\to\infty$. It can be shown that this is indeed the case.

Therefore, we have the following important result:

$$
e = \lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n}
$$

---

<a id="evaluating-a-limit-using-the-limit-definition-of-eulers-number"></a>
## Evaluating a Limit Using the Limit Definition of Euler's Number

**Example:** Calculate $\displaystyle{\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{3n}}$.

**Explanation**

Recall the following special limit:

$$
e = \lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n}
$$

Now, we rewrite the given limit using the algebra of limits, as follows:

$$
\begin{aligned}
lim_(n → ∞)(1 + \frac{1}{n})^{3n} &= lim_(n → ∞)[(1 + \frac{1}{n})^{n}]^{3} \\
&= [lim_(n → ∞)(1 + \frac{1}{n})^{n}]^{3} \\
&= e^{3}
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  What is $lim_(n → ∞)(1 + \frac{1}{n})^{-2n}$?
options:
- id: a
  content: |-
    $\frac{e}{2}$
- id: b
  content: |-
    $e^{2}$
- id: c
  correct: true
  content: |-
    $\frac{1}{e^{2}}$
- id: d
  content: |-
    $2e$
- id: e
  content: |-
    $e$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  What is $lim_(n → ∞)(1 + \frac{1}{n})^{n/2}$?
options:
- id: a
  content: |-
    $\frac{2}{e}$
- id: b
  content: |-
    $e^{2}$
- id: c
  content: |-
    $2e$
- id: d
  correct: true
  content: |-
    $\sqrt{e}$
- id: e
  content: |-
    $\frac{e}{2}$
```

---

<a id="evaluating-a-limit-using-the-limit-definition-of-eulers-number-limits-containing-variables"></a>
## Evaluating a Limit Using the Limit Definition of Euler's Number: Limits Containing Variables

**Example:** Calculate $\displaystyle{\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{nx/3}}$.

**Explanation**

Recall the following special limit:

$$
e = \lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n}
$$

Now, we rewrite the given limit using the algebra of limits, as follows:

$$
\begin{aligned}
lim_(n → ∞)(1 + \frac{1}{n})^{nx/3} &= lim_(n → ∞)[(1 + \frac{1}{n})^{n}]^{x/3} \\
&= [lim_(n → ∞)(1 + \frac{1}{n})^{n}]^{x/3} \\
&= e^{x/3} \\
&= \sqrt[3]{e^{x}}
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  What is $lim_(n → ∞)(1 + \frac{1}{n})^{4nx}$?
options:
- id: a
  content: |-
    $4e^{-4x}$
- id: b
  content: |-
    $4e^{x}$
- id: c
  content: |-
    $4e^{4x}$
- id: d
  content: |-
    $e^{-4x}$
- id: e
  correct: true
  content: |-
    $e^{4x}$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  What is $lim_(n → ∞)(1 + \frac{1}{n})^{nx/2}$?
options:
- id: a
  content: |-
    $\frac{\sqrt{e}}{2}$
- id: b
  content: |-
    $x\sqrt{e}$
- id: c
  correct: true
  content: |-
    $\sqrt{e^{x}}$
- id: d
  content: |-
    $\frac{e^{x}}{\sqrt{2}}$
- id: e
  content: |-
    $\frac{e^{x}}{2}$
```

---

<a id="another-definition-of-the-exponential-function"></a>
## Another Definition of the Exponential Function

Let's now consider the limit

$$
\lim_{n \to \infty} \left(1+\dfrac{x}{n}\right)^{n}
$$

where $x$ is a real number.

First, we rewrite the given limit using the algebra of limits, as follows:

$$
\begin{aligned}
lim_(n → ∞)(1 + \frac{x}{n})^{n} &= lim_(n → ∞)(1 + \frac{1}{n/x})^{n} \\
&= lim_(n → ∞)(1 + \frac{1}{n/x})^{(n/x) \cdot x} \\
&= [lim_(n → ∞)(1 + \frac{1}{n/x})^{n/x}]^{x}
\end{aligned}
$$

Let's now perform the substitution

$$
m=n/x
$$

Since $m\to\infty$ as $n\to\infty$, we obtain

$$
\begin{aligned}
[lim_(n → ∞)(1 + \frac{1}{n/x})^{n/x}]^{x} &= [lim_(m → ∞)(1 + \frac{1}{m})^{m}_(⏟)_(e)]^{x} \\
&= e^{x}
\end{aligned}
$$

Therefore, we conclude that

$$
e^{x} = lim_(n → ∞)(1 + \frac{x}{n})^{n}
$$

---

<a id="applying-the-limit-definition-of-the-exponential-function"></a>
## Applying the Limit Definition of the Exponential Function

**Example:** Calculate $\displaystyle{\lim_{n \to \infty} \left(1+\dfrac{x}{n}\right)^{-n/2}}$.

**Explanation**

Recall the following special limit:

$$
e^x = \lim_{n \to \infty} \left(1+\dfrac{x}{n}\right)^{n}
$$

Now, we rewrite the given limit using the algebra of limits, as follows:

$$
\begin{aligned}
lim_(n → ∞)(1 + \frac{x}{n})^{-n/2} &= lim_(n → ∞)[(1 + \frac{x}{n})^{n}]^{-1/2} \\
&= [lim_(n → ∞)(1 + \frac{x}{n})^{n}]^{-1/2} \\
&= (e^{x})^{-1/2} \\
&= \sqrt{\frac{1}{e^{x}}}
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  What is $lim_(n → ∞)(1 + \frac{x}{n})^{-3n}$?
options:
- id: a
  content: |-
    $e^{3x}$
- id: b
  content: |-
    $e^{-1/3x}$
- id: c
  content: |-
    $e^{3}$
- id: d
  content: |-
    $e^{1/3x}$
- id: e
  correct: true
  content: |-
    $e^{-3x}$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  What is $lim_(n → ∞)(1 + \frac{x}{n})^{2nx}$?
options:
- id: a
  content: |-
    $e^{2}$
- id: b
  correct: true
  content: |-
    $e^{2x^{2}}$
- id: c
  content: |-
    $e^{2/x^{2}}$
- id: d
  content: |-
    $e^{2x}$
- id: e
  content: |-
    $e^{2/x}$
```

```update-progress
```

[[MA/Mathematical-Foundations/MF3/Home|Home]]
[[MA/Mathematical-Foundations/MF3/0. Table of Contents/TOC|Table of Contents]]
