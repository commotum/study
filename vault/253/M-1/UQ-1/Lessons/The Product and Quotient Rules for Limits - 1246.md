# The Product and Quotient Rules for Limits


<!--
lesson-id: 1246
topic-code: MF2.11.2.3
-->
## Table of Contents

- [Introduction](#introduction)
- [Applying the Product Rule to Compute a Limit](#applying-the-product-rule-to-compute-a-limit)
- [Applying the Product Rule to Compute a Limit Given a Graph](#applying-the-product-rule-to-compute-a-limit-given-a-graph)
- [The Quotient Rule for Limits](#the-quotient-rule-for-limits)
- [Applying the Quotient Rule to Compute a Limit](#applying-the-quotient-rule-to-compute-a-limit)
- [Applying the Quotient Rule to Compute a Limit Given a Graph](#applying-the-quotient-rule-to-compute-a-limit-given-a-graph)

## Prerequisites

- [The Sum Rule for Limits](../1914/1914.md)

---

<a id="introduction"></a>
## Introduction

The **product rule** states that the limit of the product of two functions equals the product of the limits.

More precisely, if

$$
\lim_{x\rightarrow \, a}f(x)=L
$$

and

$$
\lim_{x\rightarrow \, a}g(x)=K
$$

then

$$
\begin{aligned}
\lim_{x \to a}(f(x) \cdot g(x)) &= \lim_{x \to a}f(x) \cdot \lim_{x \to a}g(x) \\
&= L \cdot K
\end{aligned}
$$

For example, we can evaluate

$$
\lim_{x \rightarrow \,2} \left[ (x^2 +2x +3)(x^3-2x-1) \right]
$$

by evaluating the limit of each polynomial separately, and then multiplying the results together:

$$
\begin{aligned}
\lim_{x \to 2}[(x^{2} + 2x + 3)(x^{3} - 2x - 1)] &= \lim_{x \to 2}(x^{2} + 2x + 3) \cdot \lim_{x \to 2}(x^{3} - 2x - 1) \\
&= (2^{2} + 2 \cdot 2 + 3) \cdot (2^{3} - 2 \cdot 2 - 1) \\
&= (4 + 4 + 3) \cdot (8 - 4 - 1) \\
&= (11) \cdot (3) \\
&= 33
\end{aligned}
$$

---

<a id="applying-the-product-rule-to-compute-a-limit"></a>
## Applying the Product Rule to Compute a Limit

**Example:** Find $\lim_{x\rightarrow -2}(x^2-3x)(x+1)^{3}$.

**Explanation**

Applying the product rule, followed by the sum and constant multiple rules, we have

$$
\begin{aligned}
\lim_{x \to - 2}(x^{2} - 3x)(x + 1)^{3} &= \lim_{x \to - 2}(x^{2} - 3x) \cdot \lim_{x \to - 2}(x + 1)^{3} \\
&= (\lim_{x \to - 2}x^{2} - 3\lim_{x \to - 2}x)(\lim_{x \to - 2}(x^{3} + 3x^{2} + 3x + 1)) \\
&= ((-2)^{2} - 3(-2))((-2)^{3} + 3(-2)^{2} + 3(-2) + 1) \\
&= (4 + 6)(-8 + 12 - 6 + 1) \\
&= (10)(-1) \\
&=-10
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: MA253-UQ1-1246-q001
content: |-
  Find $\lim_{y \to 2}(2y - 5)(y^{2} + 6y + 9)$.
options:
- id: a
  content: |-
    $-25$
  correct: true
- id: b
  content: |-
    $-70$
- id: c
  content: |-
    $-29$
- id: d
  content: |-
    $-174$
- id: e
  content: |-
    $-150$
```
---

**Question 2:**

```quiz
type: radio
id: MA253-UQ1-1246-q002
content: |-
  Find $\lim_{x \to 1/6}(2x + 1)(3x - 1)$.
options:
- id: a
  content: |-
    $-\frac{3}{2}$
- id: b
  content: |-
    $-\frac{1}{6}$
- id: c
  content: |-
    $\frac{4}{6}$
- id: d
  content: |-
    $\frac{16}{9}$
- id: e
  content: |-
    $-\frac{2}{3}$
  correct: true
```
---

<a id="applying-the-product-rule-to-compute-a-limit-given-a-graph"></a>
## Applying the Product Rule to Compute a Limit Given a Graph

**Example:** Find $\lim_{x\rightarrow 2}\left(\dfrac{x^3 f(x)}{4}\right)$ for the function $f(x)$ plotted below.

![](<253/M-1/UQ-1/Source/The Product and Quotient Rules for Limits - 1246/Images/a35e10a88fdb149d50b059d5b09e7c9b.png>)

**Explanation**

From the graph, we get that

$$
\lim_{x\rightarrow 2} f(x)=4
$$

So, applying the product rule, we have

$$
\begin{aligned}
\lim_{x \to 2}((x^{3}f(x))/(4)) &= \frac{1}{4} \cdot \lim_{x \to 2}x^{3} \cdot \lim_{x \to 2}f(x) \\
&= \frac{1}{4} \cdot 2^{3} \cdot 4 \\
&= 8
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: MA253-UQ1-1246-q003
content: |-
  ![](<../Source/The Product and Quotient Rules for Limits - 1246/Images/q-35443.png>)
  
  Find $\lim_{x \to 1}(x^{2} + 2)f(x)$ for the function $f(x)$ plotted above.
options:
- id: a
  content: |-
    $1$
- id: b
  content: |-
    $2$
- id: c
  content: |-
    $DNE$
  correct: true
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $3$
```
---

**Question 4:**

```quiz
type: radio
id: MA253-UQ1-1246-q004
content: |-
  ![](<../Source/The Product and Quotient Rules for Limits - 1246/Images/q-35441.png>)
  
  Find $\lim_{x \to 0}((2x + 3)f(x))/(9)$ for the function $f(x)$ plotted above.
options:
- id: a
  content: |-
    $\frac{2}{3}$
- id: b
  content: |-
    $0$
- id: c
  content: |-
    $3$
- id: d
  content: |-
    $\frac{1}{3}$
  correct: true
- id: e
  content: |-
    $DNE$
```
---

<a id="the-quotient-rule-for-limits"></a>
## The Quotient Rule for Limits

The **quotient rule** states that the limit of the quotient of two functions equals the quotient of the limits (provided that the limit of the denominator is not zero).

More precisely, if

$$
\lim_{x\rightarrow a}f(x)=L
$$

and

$$
\lim_{x\rightarrow a}g(x)= K \neq 0
$$

, then

$$
\lim_{x\rightarrow a} \dfrac{f(x)}{g(x)} = \dfrac{\lim_{x\rightarrow a}f(x)}{\lim_{x\rightarrow a}g(x)}=\dfrac{L}{K}
$$

For example, we can evaluate

$$
\lim_{x \rightarrow \,2} \dfrac{x^2+4x}{x+1}
$$

by evaluating the limits of the numerator and denominator separately, and then dividing the results:

$$
\begin{aligned}
\lim_{x \to 2}\frac{x^{2} + 4x}{x + 1} &= (\lim_{x \to 2}(x^{2} + 4x))/(\lim_{x \to 2}(x + 1)) \\
&= \frac{2^{2} + 4 \cdot 2}{2 + 1} \\
&= \frac{12}{3} \\
&= 4
\end{aligned}
$$

---

<a id="applying-the-quotient-rule-to-compute-a-limit"></a>
## Applying the Quotient Rule to Compute a Limit

**Example:** Calculate $\lim_{x\rightarrow 2} x^{-5}$.

**Explanation**

First, we will express the negative exponent as a quotient:

$$
\lim_{x\rightarrow 2} x^{-5}= \lim_{x\rightarrow 2} \dfrac{1}{x^5}
$$

Then, we apply the quotient rule:

$$
\begin{aligned}
\lim_{x \to 2}x^{-5} &= (\lim_{x \to 2}1)/(\lim_{x \to 2}x^{5}) \\
&= \frac{1}{2^{5}} \\
&= \frac{1}{32}
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: MA253-UQ1-1246-q005
content: |-
  Find $\lim_{x \to - 3}\frac{2x}{x + 2}$.
options:
- id: a
  content: |-
    $-6$
- id: b
  content: |-
    $-2$
- id: c
  content: |-
    $6$
  correct: true
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $-3$
```
---

**Question 6:**

```quiz
type: radio
id: MA253-UQ1-1246-q006
content: |-
  Find $\lim_{x \to - 2} - 4x^{-3}$.
options:
- id: a
  content: |-
    $\frac{1}{32}$
- id: b
  content: |-
    $-1$
- id: c
  content: |-
    $\frac{1}{2}$
  correct: true
- id: d
  content: |-
    $-32$
- id: e
  content: |-
    $-8$
```
---

<a id="applying-the-quotient-rule-to-compute-a-limit-given-a-graph"></a>
## Applying the Quotient Rule to Compute a Limit Given a Graph

**Example:** Find $\lim_{x\rightarrow 2} \dfrac{xf(x)+x^2}{2+f(x)}$ for the function $f(x)$ plotted below.

![](<253/M-1/UQ-1/Source/The Product and Quotient Rules for Limits - 1246/Images/f9617550bea4c667507864cf1dccfa51.png>)

**Explanation**

Using the quotient rule, we have

$$
\begin{aligned}
\lim_{x \to 2}(xf(x) + x^{2})/(2 + f(x)) &= (\lim_{x \to 2}(xf(x) + x^{2}))/(\lim_{x \to 2}(2 + f(x)))
\end{aligned}
$$

We find from the graph that

$$
\lim_{x\rightarrow 2} f(x)=3
$$

Calculating the limits of the numerator and denominator separately, we have

$$
\begin{aligned}
\lim_{x \to 2}(xf(x) + x^{2}) &= 2(3) + 2^{2} = 10, \\
\lim_{x \to 2}(2 + f(x)) &= 2 + 3 = 5
\end{aligned}
$$

Taking the quotient of these limits, we have

$$
\begin{aligned}
\lim_{x \to 2}(xf(x) + x^{2})/(2 + f(x)) &= (\lim_{x \to 2}(xf(x) + x^{2}))/(\lim_{x \to 2}(2 + f(x))) \\
&= \frac{10}{5} \\
&= 2
\end{aligned}
$$

---

**Question 7:**

```quiz
type: radio
id: MA253-UQ1-1246-q007
content: |-
  ![](<../Source/The Product and Quotient Rules for Limits - 1246/Images/q-17283.png>)
  
  Find $\lim_{x \to 1}(3f(x) + 3x)/(6x^{2} + 4)$ for the function $f(x)$ plotted above.
options:
- id: a
  content: |-
    $0$
  correct: true
- id: b
  content: |-
    Does not exist
- id: c
  content: |-
    $10$
- id: d
  content: |-
    $3$
- id: e
  content: |-
    $-1$
```
---

**Question 8:**

```quiz
type: radio
id: MA253-UQ1-1246-q008
content: |-
  ![](<../Source/The Product and Quotient Rules for Limits - 1246/Images/q-17281.png>)
  
  Find $\lim_{x \to - \pi/2}(4x + π)/(f(x))$ for the function $f(x)$ plotted above.
options:
- id: a
  content: |-
    $-\frac{2π}{3}$
- id: b
  content: |-
    $\frac{π}{3}$
- id: c
  content: |-
    $\frac{2π}{3}$
- id: d
  content: |-
    $-\frac{π}{3}$
  correct: true
- id: e
  content: |-
    $\frac{3}{π}$
```
---

## Navigation

- [Next: Improper Integrals of the Second Kind](<253/M-1/UQ-1/Prerequisites/Improper Integrals of the Second Kind - 759.md>)
- [Back to UQ-1](UQ-1.md)

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
