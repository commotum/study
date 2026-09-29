# Integrating an Odd Power of Sine

## Table of Contents

- [Introduction](#introduction)
- [Separate One Sine Factor](#separate-sine)
- [Substitute for the Cosine](#cosine-substitution)
- [Evaluate the Original Integral](#original-integral)
- [Verify the Antiderivative](#verify)
- [Summary](#summary)

## Prerequisites

- The identity $\sin^2\theta=1-\cos^2\theta$
- Substitution in indefinite integrals
- The power rule for antiderivatives
- The chain rule

---

<a id="introduction"></a>
## Introduction

When sine has a positive odd power, saving one sine factor leaves an even power that can be rewritten with

$$
\sin^2\theta=1-\cos^2\theta.
$$

For a cubic power, the rewrite is

$$
\sin^3(kx)
=
\sin(kx)\bigl(1-\cos^2(kx)\bigr).
$$

This creates a polynomial in cosine multiplied by a sine factor. Then $u=\cos(kx)$ works because

$$
du=-k\sin(kx)\,dx.
$$

This method depends on the sine exponent being odd. The main coefficient trap is forgetting the negative reciprocal factor $-1/k$.

---

<a id="separate-sine"></a>
## Separate One Sine Factor

**Example:** Rewrite $\sin^5(2x)$ in a form prepared for cosine substitution.

**Explanation**

Because the exponent $5$ is odd, split off one factor of $\sin(2x)$:

$$
\sin^5(2x)=\sin(2x)\bigl(\sin^2(2x)\bigr)^2.
$$

Now use $\sin^2(2x)=1-\cos^2(2x)$:

$$
\sin^5(2x)
=
\sin(2x)\bigl(1-\cos^2(2x)\bigr)^2.
$$

The remaining sine factor will become part of $du$ when $u=\cos(2x)$.

```quiz
type: radio
id: ohw9-p1-rewrite-1
content: |-
  Which rewrite prepares $\sin^7(4x)$ for the substitution $u=\cos(4x)$?
options:
- id: a
  content: |-
    $\sin(4x)\bigl(1-\cos^2(4x)\bigr)^3$
  correct: true
- id: b
  content: |-
    $\sin(4x)\bigl(1-\cos(4x)\bigr)^3$
- id: c
  content: |-
    $\cos(4x)\bigl(1-\sin^2(4x)\bigr)^3$
- id: d
  content: |-
    $\sin(4x)\bigl(1+\cos^2(4x)\bigr)^3$
- id: e
  content: |-
    $\sin^2(4x)\bigl(1-\cos^2(4x)\bigr)^2$
```

---

<a id="cosine-substitution"></a>
## Substitute for the Cosine

**Example:** Evaluate

$$
\int\sin^3(2x)\,dx.
$$

**Explanation**

Save one sine factor and rewrite the other two:

$$
\int\sin^3(2x)\,dx
=
\int\sin(2x)\bigl(1-\cos^2(2x)\bigr)\,dx.
$$

Let

$$
u=\cos(2x),
\qquad
du=-2\sin(2x)\,dx,
\qquad
\sin(2x)\,dx=-\frac12\,du.
$$

Then

$$
\begin{aligned}
\int\sin^3(2x)\,dx
&=-\frac12\int(1-u^2)\,du \\
&=-\frac12\left(u-\frac{u^3}{3}\right)+C \\
&=-\frac{u}{2}+\frac{u^3}{6}+C.
\end{aligned}
$$

Substitute back:

$$
\int\sin^3(2x)\,dx
=
\frac{\cos^3(2x)}{6}-\frac{\cos(2x)}{2}+C.
$$

```quiz
type: radio
id: ohw9-p1-substitute-1
content: |-
  Evaluate
  $$
  \int\sin^3(5x)\,dx.
  $$
options:
- id: a
  content: |-
    $\dfrac{\cos^3(5x)}{15}-\dfrac{\cos(5x)}{5}+C$
  correct: true
- id: b
  content: |-
    $\dfrac{\cos^3(5x)}{3}-\cos(5x)+C$
- id: c
  content: |-
    $\dfrac{\cos^3(5x)}{15}+\dfrac{\cos(5x)}{5}+C$
- id: d
  content: |-
    $\dfrac{\sin^3(5x)}{15}-\dfrac{\sin(5x)}{5}+C$
- id: e
  content: |-
    $\dfrac{\cos^3(5x)}{5}-\dfrac{\cos(5x)}{15}+C$
```

---

<a id="original-integral"></a>
## Evaluate the Original Integral

**Example:** Evaluate

$$
\int\sin^3(3x)\,dx.
$$

**Explanation**

First rewrite the odd power:

$$
\int\sin^3(3x)\,dx
=
\int\sin(3x)\bigl(1-\cos^2(3x)\bigr)\,dx.
$$

Let $u=\cos(3x)$. Then

$$
du=-3\sin(3x)\,dx,
\qquad
\sin(3x)\,dx=-\frac13\,du.
$$

Therefore,

$$
\begin{aligned}
\int\sin^3(3x)\,dx
&=-\frac13\int(1-u^2)\,du \\
&=-\frac13\left(u-\frac{u^3}{3}\right)+C \\
&=-\frac{u}{3}+\frac{u^3}{9}+C.
\end{aligned}
$$

Substitute $u=\cos(3x)$:

$$
\boxed{\frac{\cos^3(3x)}{9}-\frac{\cos(3x)}{3}+C}.
$$

```quiz
type: radio
id: ohw9-p1-original-1
content: |-
  After $u=\cos(3x)$, which transformed integral correctly represents
  $$
  \int\sin^3(3x)\,dx?
  $$
options:
- id: a
  content: |-
    $-\dfrac13\int(1-u^2)\,du$
  correct: true
- id: b
  content: |-
    $\dfrac13\int(1-u^2)\,du$
- id: c
  content: |-
    $-3\int(1-u^2)\,du$
- id: d
  content: |-
    $-\dfrac13\int(1+u^2)\,du$
- id: e
  content: |-
    $-\dfrac13\int(1-u)^2\,du$
```

---

<a id="verify"></a>
## Verify the Antiderivative

**Example:** Differentiate

$$
F(x)=\frac{\cos^3(3x)}{9}-\frac{\cos(3x)}{3}.
$$

**Explanation**

Apply the chain rule to both terms:

$$
\begin{aligned}
F'(x)
&=\frac19\left(3\cos^2(3x)\right)\left(-3\sin(3x)\right)
  -\frac13\left(-3\sin(3x)\right) \\
&=-\cos^2(3x)\sin(3x)+\sin(3x) \\
&=\sin(3x)\bigl(1-\cos^2(3x)\bigr) \\
&=\sin^3(3x).
\end{aligned}
$$

The derivative restores both the original inner coefficient $3$ and the original odd power.

```quiz
type: radio
id: ohw9-p1-verify-1
content: |-
  What is the derivative of
  $$
  \frac{\cos^3(6x)}{18}-\frac{\cos(6x)}{6}?
  $$
options:
- id: a
  content: |-
    $\sin^3(6x)$
  correct: true
- id: b
  content: |-
    $-\sin^3(6x)$
- id: c
  content: |-
    $6\sin^3(6x)$
- id: d
  content: |-
    $\sin(6x)\bigl(1+\cos^2(6x)\bigr)$
- id: e
  content: |-
    $\cos^3(6x)$
```

---

<a id="summary"></a>
## Summary

For an integral of an odd sine power such as $\int\sin^3(kx)\,dx$:

1. Save one factor of $\sin(kx)$.
2. Rewrite the remaining $\sin^2(kx)$ as $1-\cos^2(kx)$.
3. Let $u=\cos(kx)$, so $\sin(kx)\,dx=-du/k$.
4. Integrate the resulting polynomial and substitute back.

In particular,

$$
\int\sin^3(3x)\,dx
=
\frac{\cos^3(3x)}{9}-\frac{\cos(3x)}{3}+C.
$$

The main traps are using $1+\cos^2(kx)$ instead of $1-\cos^2(kx)$ and losing the negative reciprocal factor $-1/k$.
