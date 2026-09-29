# Integrating $\sin^2(4x)\cos^2(4x)$ With Double Angles

## Table of Contents

- [Introduction](#introduction)
- [Compress the Product Into One Sine Square](#compress-the-product-into-one-sine-square)
- [Reduce the Remaining Square](#reduce-the-remaining-square)
- [Integrate the Linear-Angle Form](#integrate-the-linear-angle-form)
- [Evaluate and Check the Assigned Integral](#evaluate-and-check-the-assigned-integral)
- [Summary](#summary)

## Prerequisites

- Use the double-angle identity $\sin(2\theta)=2\sin\theta\cos\theta$.
- Use the power-reduction identity $\sin^2\theta=\dfrac{1-\cos(2\theta)}2$.
- Integrate $\cos(ax)$ and apply the chain rule.

---

<a id="introduction"></a>
## Introduction

The recognition cue is a product in which sine and cosine of the **same angle are both squared**:

$$
\sin^2(\theta)\cos^2(\theta).
$$

Neither factor has an odd power to save for a direct substitution. Instead, square the sine double-angle identity:

$$
\sin(2\theta)=2\sin\theta\cos\theta
\quad\Longrightarrow\quad
\sin^2\theta\cos^2\theta=\frac14\sin^2(2\theta).
$$

This turns a product into one squared trigonometric function. A power-reduction identity then turns that square into a constant minus a cosine, which can be integrated directly.

---

<a id="compress-the-product-into-one-sine-square"></a>
## Compress the Product Into One Sine Square

**Example:** Rewrite $\sin^2(3x)\cos^2(3x)$ as one sine square.

**Explanation**

Take $\theta=3x$ in

$$
\sin^2\theta\cos^2\theta=\frac14\sin^2(2\theta).
$$

Doubling the angle gives

$$
\sin^2(3x)\cos^2(3x)=\frac14\sin^2(6x).
$$

The factor is $1/4$, not $1/2$, because the entire identity was squared:

$$
\left(\frac{\sin(2\theta)}2\right)^2
=\frac{\sin^2(2\theta)}4.
$$

```quiz
type: radio
id: ohw9-p6-q1
content: |-
  Which expression equals $\sin^2(5x)\cos^2(5x)$?
options:
- id: ohw9-p6-q1-a
  content: |-
    $\dfrac14\sin^2(10x)$
  correct: true
- id: ohw9-p6-q1-b
  content: |-
    $\dfrac12\sin^2(10x)$
- id: ohw9-p6-q1-c
  content: |-
    $\dfrac14\sin^2(5x)$
- id: ohw9-p6-q1-d
  content: |-
    $4\sin^2(10x)$
- id: ohw9-p6-q1-e
  content: |-
    $\dfrac14\sin(10x)$
```

---

<a id="reduce-the-remaining-square"></a>
## Reduce the Remaining Square

**Example:** Rewrite $\sin^2(3x)\cos^2(3x)$ as a constant minus a cosine.

**Explanation**

The first identity gives

$$
\sin^2(3x)\cos^2(3x)=\frac14\sin^2(6x).
$$

Start with the cosine double-angle identity

$$
\cos(2\phi)=1-2\sin^2(\phi).
$$

Rearranging it gives the needed power-reduction form:

$$
\sin^2(\phi)=\frac{1-\cos(2\phi)}2
$$

with $\phi=6x$:

$$
\begin{aligned}
\sin^2(3x)\cos^2(3x)
&=\frac14\left(\frac{1-\cos(12x)}2\right)\\
&=\frac18\left(1-\cos(12x)\right).
\end{aligned}
$$

The original angle has been doubled twice: $3x$ becomes $6x$, then $12x$.

```quiz
type: radio
id: ohw9-p6-q2
content: |-
  Which expression equals $\sin^2(7x)\cos^2(7x)$ after both identity steps?
options:
- id: ohw9-p6-q2-a
  content: |-
    $\dfrac18\left(1-\cos(28x)\right)$
  correct: true
- id: ohw9-p6-q2-b
  content: |-
    $\dfrac18\left(1-\cos(14x)\right)$
- id: ohw9-p6-q2-c
  content: |-
    $\dfrac14\left(1-\cos(28x)\right)$
- id: ohw9-p6-q2-d
  content: |-
    $\dfrac18\left(1+\cos(28x)\right)$
- id: ohw9-p6-q2-e
  content: |-
    $\dfrac18\sin(28x)$
```

---

<a id="integrate-the-linear-angle-form"></a>
## Integrate the Linear-Angle Form

For $a\ne0$, the two identity steps give the reusable rewrite

$$
\sin^2(ax)\cos^2(ax)=\frac18\left(1-\cos(4ax)\right).
$$

**Example:** Evaluate $\int\sin^2(3x)\cos^2(3x)\,dx$.

**Explanation**

Rewrite the integrand and integrate term by term:

$$
\begin{aligned}
\int\sin^2(3x)\cos^2(3x)\,dx
&=\frac18\int\left(1-\cos(12x)\right)\,dx\\
&=\frac18\left(x-\frac{\sin(12x)}{12}\right)+C\\
&=\frac{x}{8}-\frac{\sin(12x)}{96}+C.
\end{aligned}
$$

The factor $1/12$ comes from integrating $\cos(12x)$. It multiplies the existing factor $1/8$.

```quiz
type: radio
id: ohw9-p6-q3
content: |-
  Which expression is an antiderivative of $\sin^2(5x)\cos^2(5x)$?
options:
- id: ohw9-p6-q3-a
  content: |-
    $\dfrac{x}{8}-\dfrac{\sin(20x)}{160}+C$
  correct: true
- id: ohw9-p6-q3-b
  content: |-
    $\dfrac{x}{8}-\dfrac{\sin(10x)}{80}+C$
- id: ohw9-p6-q3-c
  content: |-
    $\dfrac{x}{4}-\dfrac{\sin(20x)}{80}+C$
- id: ohw9-p6-q3-d
  content: |-
    $\dfrac{x}{8}+\dfrac{\sin(20x)}{160}+C$
- id: ohw9-p6-q3-e
  content: |-
    $\dfrac{x}{8}-\dfrac{\cos(20x)}{160}+C$
```

---

<a id="evaluate-and-check-the-assigned-integral"></a>
## Evaluate and Check the Assigned Integral

**Example:** Evaluate

$$
\int\sin^2(4x)\cos^2(4x)\,dx.
$$

**Explanation**

Compress the product:

$$
\sin^2(4x)\cos^2(4x)=\frac14\sin^2(8x).
$$

Reduce the remaining square:

$$
\frac14\sin^2(8x)
=\frac18\left(1-\cos(16x)\right).
$$

At this checkpoint, the coefficient has changed from $1/4$ to $1/8$, and the original angle $4x$ has been doubled twice to $16x$.

Now integrate:

$$
\begin{aligned}
\int\sin^2(4x)\cos^2(4x)\,dx
&=\frac18\int\left(1-\cos(16x)\right)\,dx\\
&=\frac18\left(x-\frac{\sin(16x)}{16}\right)+C\\
&=\boxed{\frac{x}{8}-\frac{\sin(16x)}{128}+C}.
\end{aligned}
$$

The sine coefficient is $1/128$ because the outside $1/8$ multiplies the reciprocal chain factor $1/16$.

Differentiate to check:

$$
\begin{aligned}
\frac{d}{dx}\left(\frac{x}{8}-\frac{\sin(16x)}{128}\right)
&=\frac18-\frac18\cos(16x)\\
&=\frac18\left(1-\cos(16x)\right)\\
&=\sin^2(4x)\cos^2(4x).
\end{aligned}
$$

```quiz
type: radio
id: ohw9-p6-q4
content: |-
  Which expression is an antiderivative of $\sin^2(6x)\cos^2(6x)$?
options:
- id: ohw9-p6-q4-a
  content: |-
    $\dfrac{x}{8}-\dfrac{\sin(24x)}{192}+C$
  correct: true
- id: ohw9-p6-q4-b
  content: |-
    $\dfrac{x}{8}-\dfrac{\sin(12x)}{96}+C$
- id: ohw9-p6-q4-c
  content: |-
    $\dfrac{x}{8}-\dfrac{\sin(24x)}{24}+C$
- id: ohw9-p6-q4-d
  content: |-
    $\dfrac{x}{8}+\dfrac{\sin(24x)}{192}+C$
- id: ohw9-p6-q4-e
  content: |-
    $\dfrac{x}{4}-\dfrac{\sin(24x)}{96}+C$
```

---

<a id="summary"></a>
## Summary

For matching squared sine and cosine factors:

1. Compress the product:
   $\sin^2\theta\cos^2\theta=\dfrac14\sin^2(2\theta)$.
2. Reduce the sine square:
   $\dfrac14\sin^2(2\theta)=\dfrac18\left(1-\cos(4\theta)\right)$.
3. Integrate the constant and cosine terms separately.
4. Track both angle doublings and the reciprocal chain factor.
5. Include $C$ and differentiate to check.

For $a\ne0$,

$$
\int\sin^2(ax)\cos^2(ax)\,dx
=\frac{x}{8}-\frac{\sin(4ax)}{32a}+C.
$$
