# Further Rationalizing Denominators of Algebraic Expressions

<!--
lesson-id: 6185
topic-code: MF2.6.4.3
-->

## Table of Contents

- [Introduction](#introduction)
- [Rationalizing Denominators Containing Two Terms](#rationalizing-denominators-containing-two-terms)
- [Rationalizing Denominators Containing a Binomial Within the Radical](#rationalizing-denominators-containing-a-binomial-within-the-radical)
- [Rationalizing a Denominator With Two Radicals](#rationalizing-a-denominator-with-two-radicals)

## Prerequisites

- [Rationalizing Denominators With Two Terms](<6.4.2. Rationalizing Denominators With Two Terms.md>)
- [Rationalizing Denominators of Algebraic Expressions](<6.4.1. Rationalizing Denominators of Algebraic Expressions.md>)

---

<a id="introduction"></a>
## Introduction

Rationalizing the denominator works similarly for algebraic expressions as it does for numerical ones. When the denominator contains two terms and includes radicals, we multiply both the numerator and the denominator by the *conjugate* of the denominator to eliminate the radical.

For example, consider the following expression:

$$
\dfrac{1}{1+\sqrt{x}}
$$

To find the conjugate of the denominator $1+\sqrt{x}$, all we have to do is flip the sign between the two terms. So, the conjugate of the denominator is

$$
1\,{\color{blue}{-}}\,\sqrt{x}
$$

Now, to rationalize the denominator, we multiply both the numerator and denominator by $1-\sqrt{x}$ and simplify:

$$
\begin{aligned}
\frac{1}{1 + \sqrt{x}} &=  \\
\frac{1}{1 + \sqrt{x}} \cdot \frac{1 - \sqrt{x}}{1 - \sqrt{x}} &=  \\
(1 - \sqrt{x})/((1 + \sqrt{x})(1 - \sqrt{x})) &=  \\
(1 - \sqrt{x})/(1^{2} - (\sqrt{x})^{2}) &=  \\
&= \frac{1 - \sqrt{x}}{1 - x}
\end{aligned}
$$

---

<a id="rationalizing-denominators-containing-two-terms"></a>
## Rationalizing Denominators Containing Two Terms

**Example:** Rationalize the denominator of $\dfrac{1}{3-\sqrt a}$.

**Explanation**

First, note that the denominator's conjugate is $3+\sqrt a$.

Now, to rationalize the denominator, we multiply both the numerator and denominator by the conjugate $3+\sqrt a$, and simplify:

$$
\begin{aligned}
\frac{1}{3 - \sqrt{a}} &=  \\
\frac{1}{3 - \sqrt{a}} \cdot \frac{3 + \sqrt{a}}{3 + \sqrt{a}} &=  \\
(3 + \sqrt{a})/((3 - \sqrt{a})(3 + \sqrt{a})) &=  \\
(3 + \sqrt{a})/(3^{2} - (\sqrt{a})^{2}) &=  \\
&= \frac{3 + \sqrt{a}}{9 - a}
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Rationalize the denominator of $\frac{4a^{2}}{2 + \sqrt{a}}$.
options:
- id: a
  content: |-
    $\frac{8a^{2} - 4a^{3}}{2 - 4a}$
- id: b
  content: |-
    $\frac{4a^{2} - 4a^{2}\sqrt{a}}{a - 4}$
- id: c
  correct: true
  content: |-
    $\frac{8a^{2} - 4a^{2}\sqrt{a}}{4 - a}$
- id: d
  content: |-
    $2a + a\sqrt{a}$
- id: e
  content: |-
    $\frac{8a^{2}\sqrt{a} - 4a^{3}}{2 - 4a}$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Rationalize the denominator of $\frac{d + 1}{\sqrt{2d} + 1}$.
options:
- id: a
  content: |-
    $((2d + 1)(\sqrt{d} - 1))/(d - 1)$
- id: b
  content: |-
    $((d + 1)(\sqrt{2d} - 1))/(d - 1)$
- id: c
  content: |-
    $((2d + 1)(\sqrt{2d} - 1))/(d - 1)$
- id: d
  correct: true
  content: |-
    $((d + 1)(\sqrt{2d} - 1))/(2d - 1)$
- id: e
  content: |-
    $((d + 1)(\sqrt{d} - 1))/(2d - 1)$
```

---

<a id="rationalizing-denominators-containing-a-binomial-within-the-radical"></a>
## Rationalizing Denominators Containing a Binomial Within the Radical

**Example:** Rationalize the denominator of $\dfrac {x} {\sqrt{x+1}+1}$.

**Explanation**

First, note that the denominator's conjugate is $\sqrt{x+1}-1$.

Now, to rationalize the denominator, we multiply both the numerator and denominator by the conjugate $\sqrt{x+1}-1$, and simplify:

$$
\begin{aligned} \dfrac {x} {\sqrt{x+1}+1} \\[5pt] &= \dfrac {x} {\sqrt{x+1}+1}\cdot \dfrac{\sqrt{x+1}-1}{\sqrt{x+1}-1} \\[5pt] &= \dfrac {x(\sqrt{x+1}-1)} {(\sqrt{x+1}+1)(\sqrt{x+1}-1)} \\[5pt] &= \dfrac {x(\sqrt{x+1}-1)} {(\sqrt{x+1})^2-1^2} \\[5pt] &= \dfrac {x(\sqrt{x+1}-1)} {x+1-1} \\[5pt] &= \dfrac {x(\sqrt{x+1}-1)} {x} \\[5pt] &= \sqrt{x+1}-1 \end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Rationalize the denominator of $\frac{x}{\sqrt{x + 2} + 4}$.
options:
- id: a
  content: |-
    $(x(\sqrt{x + 2} + 4))/(x + 18)$
- id: b
  content: |-
    $(x(\sqrt{x - 2} - 4))/(x - 18)$
- id: c
  content: |-
    $\frac{x}{x - 14}$
- id: d
  correct: true
  content: |-
    $(x(\sqrt{x + 2} - 4))/(x - 14)$
- id: e
  content: |-
    $\frac{x\sqrt{x - 2} + 4}{x - 14}$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Rationalize the denominator of $-\frac{4w}{3 + \sqrt{2w + 5}}$.
options:
- id: a
  correct: true
  content: |-
    $- (2w(3 - \sqrt{2w + 5}))/(2 - w)$
- id: b
  content: |-
    $-\frac{6w + \sqrt{2w + 5}}{2 - w}$
- id: c
  content: |-
    $(2w(3 - \sqrt{2w - 5}))/(14 + w)$
- id: d
  content: |-
    $\frac{6w + \sqrt{2w + 5}}{2 + w}$
- id: e
  content: |-
    $- (2w(3 - \sqrt{2w - 5}))/(7 + w)$
```

---

<a id="rationalizing-a-denominator-with-two-radicals"></a>
## Rationalizing a Denominator With Two Radicals

**Example:** Rationalize the denominator of $\dfrac{x}{\sqrt{2}-\sqrt{x}}$.

**Explanation**

First, note that the denominator's conjugate is $\sqrt{2}+\sqrt{x}$.

Now, to rationalize the denominator, we multiply both the numerator and denominator by the conjugate $\sqrt{2}+\sqrt{x}$, and simplify:

$$
\begin{aligned} \dfrac{x}{\sqrt{2}-\sqrt{x}} \\[5pt] &= \dfrac{x}{\sqrt{2}-\sqrt{x}} \cdot \dfrac{\sqrt{2}+\sqrt{x}}{\sqrt{2}+\sqrt{x}} \\[5pt] &= \dfrac{x(\sqrt{2}+\sqrt{x})}{(\sqrt{2}-\sqrt{x})(\sqrt{2}+\sqrt{x})} \\[5pt] &= \dfrac{x(\sqrt{2}+\sqrt{x})}{(\sqrt{2})^2-(\sqrt{x})^2} \\[5pt] &= \dfrac{x(\sqrt{2}+\sqrt{x})}{2-x} \end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  Rationalize the denominator of $\frac{1}{\sqrt{w} + \sqrt{w - 3}}$.
options:
- id: a
  correct: true
  content: |-
    $\frac{\sqrt{w} - \sqrt{w - 3}}{3}$
- id: b
  content: |-
    $3(\sqrt{w} - \sqrt{w - 3})$
- id: c
  content: |-
    $\frac{\sqrt{w} - \sqrt{w - 3}}{2}$
- id: d
  content: |-
    $(2(\sqrt{w} - \sqrt{w - 3}))/(3)$
- id: e
  content: |-
    $2(\sqrt{w} - \sqrt{w - 3})$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Rationalize the denominator of $\frac{4}{\sqrt{y + 1} + \sqrt{y - 3}}$.
options:
- id: a
  content: |-
    $-2(\sqrt{y + 1} - \sqrt{y - 3})$
- id: b
  content: |-
    $\sqrt{y - 1} - \sqrt{y + 3}$
- id: c
  correct: true
  content: |-
    $\sqrt{y + 1} - \sqrt{y - 3}$
- id: d
  content: |-
    $\frac{\sqrt{y + 1} - \sqrt{y - 3}}{2}$
- id: e
  content: |-
    $\sqrt{y + 3} - \sqrt{y - 1}$
```

```update-progress
```

[[MA/Mathematical-Foundations/MF2/Home|Home]]
[[MA/Mathematical-Foundations/MF2/0. Table of Contents/TOC|Table of Contents]]
