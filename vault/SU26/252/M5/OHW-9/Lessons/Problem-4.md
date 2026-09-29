# Definite Integrals with an Odd Power of Cosine

## Table of Contents

- [Introduction](#introduction)
- [Save One Cosine Factor](#save-cosine)
- [Transform the Differential and Bounds](#transform-bounds)
- [Evaluate the Original Integral](#original-integral)
- [Summary](#summary)

## Prerequisites

- The identity $\cos^2\theta=1-\sin^2\theta$
- Substitution in definite integrals
- The power rule for antiderivatives

---

<a id="introduction"></a>
## Introduction

When a product contains an odd positive power of cosine, save one cosine factor. Rewrite the remaining even power using

$$
\cos^2\theta=1-\sin^2\theta.
$$

For an integrand containing $\cos^5(x/2)$, this gives

$$
\cos^5\left(\frac{x}{2}\right)
=
\left(1-\sin^2\left(\frac{x}{2}\right)\right)^2
\cos\left(\frac{x}{2}\right).
$$

The saved cosine factor pairs with the differential when

$$
u=\sin\left(\frac{x}{2}\right).
$$

For a definite integral, the substitution must also transform the limits. The main traps are losing the factor $2$ from the half-angle derivative or continuing to use the old $x$-limits after changing to $u$.

---

<a id="save-cosine"></a>
## Save One Cosine Factor

**Example:** Rewrite

$$
\sin^2\left(\frac{x}{2}\right)\cos^3\left(\frac{x}{2}\right)
$$

in a form prepared for sine substitution.

**Explanation**

Split the odd cosine power into an even power and one saved factor:

$$
\cos^3\left(\frac{x}{2}\right)
=
\cos^2\left(\frac{x}{2}\right)\cos\left(\frac{x}{2}\right).
$$

Then use the Pythagorean identity:

$$
\sin^2\left(\frac{x}{2}\right)
\left(1-\sin^2\left(\frac{x}{2}\right)\right)
\cos\left(\frac{x}{2}\right).
$$

Everything except the final cosine factor is now a polynomial in $\sin(x/2)$.

```quiz
type: radio
id: ohw9-p4-rewrite-1
content: |-
  Which rewrite prepares
  $$
  \sin^4\left(\frac{x}{2}\right)\cos^5\left(\frac{x}{2}\right)
  $$
  for the substitution $u=\sin(x/2)$?
options:
- id: a
  content: |-
    $\sin^4\left(\dfrac{x}{2}\right)\left(1-\sin^2\left(\dfrac{x}{2}\right)\right)^2\cos\left(\dfrac{x}{2}\right)$
  correct: true
- id: b
  content: |-
    $\sin^4\left(\dfrac{x}{2}\right)\left(1+\sin^2\left(\dfrac{x}{2}\right)\right)^2\cos\left(\dfrac{x}{2}\right)$
- id: c
  content: |-
    $\sin^4\left(\dfrac{x}{2}\right)\left(1-\sin\left(\dfrac{x}{2}\right)\right)^2\cos\left(\dfrac{x}{2}\right)$
- id: d
  content: |-
    $\sin^4\left(\dfrac{x}{2}\right)\left(1-\cos^2\left(\dfrac{x}{2}\right)\right)^2\sin\left(\dfrac{x}{2}\right)$
- id: e
  content: |-
    $\sin^4\left(\dfrac{x}{2}\right)\left(1-\sin^2\left(\dfrac{x}{2}\right)\right)\cos\left(\dfrac{x}{2}\right)$
```

---

<a id="transform-bounds"></a>
## Transform the Differential and Bounds

**Example:** Transform

$$
\int_0^\pi
\sin^2\left(\frac{x}{2}\right)
\cos^3\left(\frac{x}{2}\right)\,dx
$$

into an integral in $u$.

**Explanation**

After saving one cosine factor and rewriting the other two,

$$
\int_0^\pi
\sin^2\left(\frac{x}{2}\right)
\left(1-\sin^2\left(\frac{x}{2}\right)\right)
\cos\left(\frac{x}{2}\right)\,dx.
$$

Let

$$
u=\sin\left(\frac{x}{2}\right).
$$

Then

$$
du=\frac12\cos\left(\frac{x}{2}\right)\,dx,
\qquad
\cos\left(\frac{x}{2}\right)\,dx=2\,du.
$$

Transform the limits:

$$
\begin{array}{c|cc}
x & 0 & \pi \\
\hline
u=\sin(x/2) & 0 & 1
\end{array}
$$

The lower $x$-limit maps to the lower $u$-limit, and the upper $x$-limit maps to the upper $u$-limit. Once the limits are changed, keep the entire calculation in $u$; there is no need to substitute back to $x$.

Therefore,

$$
\int_0^\pi
\sin^2\left(\frac{x}{2}\right)
\cos^3\left(\frac{x}{2}\right)\,dx
=
2\int_0^1 u^2(1-u^2)\,du.
$$

```quiz
type: radio
id: ohw9-p4-bounds-1
content: |-
  Using $u=\sin(x/2)$, which integral is equivalent to
  $$
  \int_0^\pi
  \sin^4\left(\frac{x}{2}\right)
  \cos^3\left(\frac{x}{2}\right)\,dx?
  $$
options:
- id: a
  content: |-
    $2\displaystyle\int_0^1u^4(1-u^2)\,du$
  correct: true
- id: b
  content: |-
    $\dfrac12\displaystyle\int_0^1u^4(1-u^2)\,du$
- id: c
  content: |-
    $2\displaystyle\int_0^\pi u^4(1-u^2)\,du$
- id: d
  content: |-
    $2\displaystyle\int_0^1u^4(1+u^2)\,du$
- id: e
  content: |-
    $2\displaystyle\int_0^1u^2(1-u^4)\,du$
```

---

<a id="original-integral"></a>
## Evaluate the Original Integral

**Example:** Evaluate

$$
\int_0^\pi
\sin^2\left(\frac{x}{2}\right)
\cos^5\left(\frac{x}{2}\right)\,dx.
$$

**Explanation**

Save one cosine factor and rewrite the remaining fourth power:

$$
\cos^5\left(\frac{x}{2}\right)
=
\left(1-\sin^2\left(\frac{x}{2}\right)\right)^2
\cos\left(\frac{x}{2}\right).
$$

With $u=\sin(x/2)$, the factor and limits become

$$
\cos\left(\frac{x}{2}\right)\,dx=2\,du,
\qquad
x=0\Rightarrow u=0,
\qquad
x=\pi\Rightarrow u=1.
$$

Thus,

$$
\begin{aligned}
\int_0^\pi
\sin^2\left(\frac{x}{2}\right)
\cos^5\left(\frac{x}{2}\right)\,dx
&=2\int_0^1u^2(1-u^2)^2\,du \\
&=2\int_0^1\left(u^2-2u^4+u^6\right)\,du \\
&=2\left[\frac{u^3}{3}-\frac{2u^5}{5}+\frac{u^7}{7}\right]_0^1 \\
&=2\left(\frac13-\frac25+\frac17\right) \\
&=2\left(\frac{8}{105}\right) \\
&=\boxed{\frac{16}{105}}.
\end{aligned}
$$

The integrand is nonnegative on $[0,\pi]$, so the positive result is consistent with the original integral.

```quiz
type: radio
id: ohw9-p4-original-1
content: |-
  Evaluate
  $$
  \int_0^\pi
  \sin^4\left(\frac{x}{2}\right)
  \cos^3\left(\frac{x}{2}\right)\,dx.
  $$
options:
- id: a
  content: |-
    $\dfrac{4}{35}$
  correct: true
- id: b
  content: |-
    $\dfrac{2}{35}$
- id: c
  content: |-
    $\dfrac{4}{15}$
- id: d
  content: |-
    $-\dfrac{4}{35}$
- id: e
  content: |-
    $\dfrac{8}{35}$
```

---

<a id="summary"></a>
## Summary

For a definite integral with an odd power of cosine:

1. Save one cosine factor.
2. Rewrite the remaining even cosine power using $\cos^2\theta=1-\sin^2\theta$.
3. Substitute for the sine expression.
4. Include the reciprocal inner-derivative factor and map each $x$-limit to its corresponding $u$-limit.
5. Integrate the resulting polynomial.

For the original problem,

$$
u=\sin\left(\frac{x}{2}\right),
\qquad
\cos\left(\frac{x}{2}\right)\,dx=2\,du,
\qquad
[0,\pi]\longrightarrow[0,1],
$$

which gives

$$
\int_0^\pi
\sin^2\left(\frac{x}{2}\right)
\cos^5\left(\frac{x}{2}\right)\,dx
=
\frac{16}{105}.
$$

The main traps are using $1+\sin^2\theta$, losing the factor $2$, or mixing the new variable $u$ with the old limits $0$ and $\pi$.
