# Integrating Sine and Cosine Powers When Cosine Is Odd

## Table of Contents

- [Introduction](#introduction)
- [Save One Cosine Factor](#save-one-cosine-factor)
- [Include the Inner Derivative](#include-the-inner-derivative)
- [Complete a Nearby Integral](#complete-a-nearby-integral)
- [Evaluate Problem 3](#evaluate-problem-3)
- [Summary](#summary)

## Prerequisites

- Use the Pythagorean identity $\sin^2(\theta)+\cos^2(\theta)=1$.
- Apply substitution and integrate powers with $\int u^n\,du=\dfrac{u^{n+1}}{n+1}+C$ for $n\ne-1$.
- Differentiate $\sin(kx)$ as $k\cos(kx)$.

---

<a id="introduction"></a>
## Introduction

For a product

$$
\int \sin^m(kx)\cos^n(kx)\,dx,
$$

an odd cosine exponent is a cue to save one cosine factor for $du$. Rewrite the remaining even power of cosine using

$$
\cos^2(kx)=1-\sin^2(kx),
$$

then substitute $u=\sin(kx)$. This turns the trigonometric product into a polynomial in $u$.

For $\cos^3(kx)$, the useful split is

$$
\cos^3(kx)=\cos^2(kx)\cos(kx)
=\left(1-\sin^2(kx)\right)\cos(kx).
$$

In Problem 3, the cosine exponent is $3=2+1$: the pair is converted with the identity, and the one remaining cosine factor supplies $du$.

---

<a id="save-one-cosine-factor"></a>
## Save One Cosine Factor

**Example:** Rewrite $\sin^2(6x)\cos^3(6x)$ so it is ready for the substitution $u=\sin(6x)$.

**Explanation**

Separate one cosine factor:

$$
\sin^2(6x)\cos^3(6x)
=\sin^2(6x)\cos^2(6x)\cos(6x).
$$

Convert the remaining $\cos^2(6x)$:

$$
\sin^2(6x)\cos^3(6x)
=\sin^2(6x)\left(1-\sin^2(6x)\right)\cos(6x).
$$

Now every factor except $\cos(6x)\,dx$ can be written in terms of $u=\sin(6x)$.

```quiz
type: radio
id: p3-save-cosine
content: |-
  Which rewrite prepares $\sin^4(9x)\cos^3(9x)$ for $u=\sin(9x)$?
options:
- id: a
  content: |-
    $\sin^4(9x)\left(1-\sin^2(9x)\right)\cos(9x)$
  correct: true
- id: b
  content: |-
    $\sin^4(9x)\left(1+\sin^2(9x)\right)\cos(9x)$
- id: c
  content: |-
    $\sin^4(9x)\left(1-\cos^2(9x)\right)\sin(9x)$
- id: d
  content: |-
    $\sin^4(9x)\left(1-\sin(9x)\right)\cos^2(9x)$
- id: e
  content: |-
    $\sin^4(9x)\cos^2(9x)$
```

---

<a id="include-the-inner-derivative"></a>
## Include the Inner Derivative

**Example:** Convert $\cos(7x)\,dx$ when $u=\sin(7x)$.

**Explanation**

Differentiate the substitution:

$$
u=\sin(7x)
\quad\Longrightarrow\quad
du=7\cos(7x)\,dx.
$$

Solve for the saved factor:

$$
\cos(7x)\,dx=\frac{1}{7}\,du.
$$

The factor is $\dfrac{1}{7}$, not $7$. It must remain outside the polynomial integral.

```quiz
type: radio
id: p3-inner-derivative
content: |-
  If $u=\sin(12x)$, what replaces $\cos(12x)\,dx$?
options:
- id: a
  content: |-
    $\dfrac{1}{12}\,du$
  correct: true
- id: b
  content: |-
    $12\,du$
- id: c
  content: |-
    $-\dfrac{1}{12}\,du$
- id: d
  content: |-
    $\dfrac{1}{12}\cos(12x)\,du$
- id: e
  content: |-
    $\dfrac{1}{\cos(12x)}\,du$
```

---

<a id="complete-a-nearby-integral"></a>
## Complete a Nearby Integral

**Example:** Evaluate $\displaystyle\int\sin^2(5x)\cos^3(5x)\,dx$.

**Explanation**

Save one cosine and use $\cos^2(5x)=1-\sin^2(5x)$:

$$
\int\sin^2(5x)\cos^3(5x)\,dx
=\int\sin^2(5x)\left(1-\sin^2(5x)\right)\cos(5x)\,dx.
$$

Let $u=\sin(5x)$, so $\cos(5x)\,dx=\dfrac{1}{5}\,du$:

$$
\begin{aligned}
\int\sin^2(5x)\cos^3(5x)\,dx
&=\frac{1}{5}\int u^2(1-u^2)\,du\\
&=\frac{1}{5}\int\left(u^2-u^4\right)\,du\\
&=\frac{u^3}{15}-\frac{u^5}{25}+C\\
&=\frac{\sin^3(5x)}{15}-\frac{\sin^5(5x)}{25}+C.
\end{aligned}
$$

The minus sign comes from $1-u^2$, and each exponent increases by one during integration.

```quiz
type: radio
id: p3-nearby-integral
content: |-
  Evaluate $\displaystyle\int\sin^2(4x)\cos^3(4x)\,dx$.
options:
- id: a
  content: |-
    $\dfrac{\sin^3(4x)}{12}-\dfrac{\sin^5(4x)}{20}+C$
  correct: true
- id: b
  content: |-
    $\dfrac{\sin^3(4x)}{3}-\dfrac{\sin^5(4x)}{5}+C$
- id: c
  content: |-
    $\dfrac{\sin^3(4x)}{12}+\dfrac{\sin^5(4x)}{20}+C$
- id: d
  content: |-
    $\dfrac{\sin^2(4x)}{8}-\dfrac{\sin^4(4x)}{16}+C$
- id: e
  content: |-
    $\dfrac{\cos^3(4x)}{12}-\dfrac{\cos^5(4x)}{20}+C$
```

---

<a id="evaluate-problem-3"></a>
## Evaluate Problem 3

**Example:** Evaluate $\displaystyle\int\sin^4(18x)\cos^3(18x)\,dx$.

**Explanation**

Because the cosine exponent is odd, save one $\cos(18x)$ and rewrite the other two cosine factors:

$$
\begin{aligned}
\int\sin^4(18x)\cos^3(18x)\,dx
&=\int\sin^4(18x)\cos^2(18x)\cos(18x)\,dx\\
&=\int\sin^4(18x)\left(1-\sin^2(18x)\right)\cos(18x)\,dx.
\end{aligned}
$$

Set

$$
u=\sin(18x),
\qquad
du=18\cos(18x)\,dx,
\qquad
\cos(18x)\,dx=\frac{1}{18}\,du.
$$

Then integrate the polynomial:

$$
\begin{aligned}
\int\sin^4(18x)\cos^3(18x)\,dx
&=\frac{1}{18}\int u^4(1-u^2)\,du\\
&=\frac{1}{18}\int\left(u^4-u^6\right)\,du\\
&=\frac{1}{18}\left(\frac{u^5}{5}-\frac{u^7}{7}\right)+C\\
&=\frac{\sin^5(18x)}{90}-\frac{\sin^7(18x)}{126}+C.
\end{aligned}
$$

Differentiate to check both coefficients:

$$
\begin{aligned}
\frac{d}{dx}\left(
\frac{\sin^5(18x)}{90}-\frac{\sin^7(18x)}{126}
\right)
&=\sin^4(18x)\cos(18x)-\sin^6(18x)\cos(18x)\\
&=\sin^4(18x)\left(1-\sin^2(18x)\right)\cos(18x)\\
&=\sin^4(18x)\cos^3(18x).
\end{aligned}
$$

```quiz
type: radio
id: p3-final-answer
content: |-
  Which is an exact antiderivative of $\sin^4(18x)\cos^3(18x)$?
options:
- id: a
  content: |-
    $\dfrac{\sin^5(18x)}{90}-\dfrac{\sin^7(18x)}{126}+C$
  correct: true
- id: b
  content: |-
    $\dfrac{\sin^5(18x)}{5}-\dfrac{\sin^7(18x)}{7}+C$
- id: c
  content: |-
    $\dfrac{\sin^5(18x)}{90}+\dfrac{\sin^7(18x)}{126}+C$
- id: d
  content: |-
    $\dfrac{\sin^4(18x)}{72}-\dfrac{\sin^6(18x)}{108}+C$
- id: e
  content: |-
    $\dfrac{\cos^5(18x)}{90}-\dfrac{\cos^7(18x)}{126}+C$
```

---

<a id="summary"></a>
## Summary

When a product of sine and cosine powers has an odd cosine exponent:

1. Save one cosine factor.
2. Rewrite the remaining cosine pairs with $\cos^2(\theta)=1-\sin^2(\theta)$.
3. Substitute $u=\sin(kx)$ and use $\cos(kx)\,dx=\dfrac{1}{k}\,du$.
4. Expand, integrate the polynomial, and substitute back.

For Problem 3, remembering the factor $\dfrac{1}{18}$ gives

$$
\int\sin^4(18x)\cos^3(18x)\,dx
=\frac{\sin^5(18x)}{90}-\frac{\sin^7(18x)}{126}+C.
$$
