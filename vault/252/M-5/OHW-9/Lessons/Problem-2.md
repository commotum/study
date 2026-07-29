# Integrating $\cos^3(12x)$ by Saving One Cosine

## Table of Contents

- [Introduction](#introduction)
- [Save One Cosine Factor](#save-one-cosine-factor)
- [Match the Saved Factor to the Substitution](#match-the-saved-factor-to-the-substitution)
- [Integrate and Restore the Original Variable](#integrate-and-restore-the-original-variable)
- [Evaluate and Check the Assigned Integral](#evaluate-and-check-the-assigned-integral)
- [Summary](#summary)

## Prerequisites

- Use the Pythagorean identity $\cos^2\theta=1-\sin^2\theta$.
- Apply substitution and the chain rule.
- Integrate constants and nonnegative integer powers.

---

<a id="introduction"></a>
## Introduction

The recognition cue is an **odd positive power of cosine**. An exponent such as $3=2+1$ leaves one cosine factor after an even power is separated. Save that one factor, turn the remaining even power into sines, and let the sine of the angle be $u$:

$$
\cos^{2m+1}(ax)
=\left(\cos^2(ax)\right)^m\cos(ax)
=\left(1-\sin^2(ax)\right)^m\cos(ax).
$$

Here $m$ is a nonnegative integer and $a\ne0$. The saved factor $\cos(ax)\,dx$ matches the derivative of $\sin(ax)$. For the assigned integral, $m=1$ and $a=12$.

---

<a id="save-one-cosine-factor"></a>
## Save One Cosine Factor

**Example:** Rewrite $\cos^3(5x)$ so that substitution with $u=\sin(5x)$ will work.

**Explanation**

Because the cosine exponent is odd, reserve one cosine factor:

$$
\cos^3(5x)=\cos^2(5x)\cos(5x).
$$

Then convert only the even power:

$$
\cos^3(5x)
=\left(1-\sin^2(5x)\right)\cos(5x).
$$

The last cosine remains in place because it will become part of $du$.

```quiz
type: radio
id: ohw9-p2-q1
content: |-
  Which rewrite prepares $\cos^5(4x)$ for substitution with $u=\sin(4x)$?
options:
- id: ohw9-p2-q1-a
  content: |-
    $\left(1-\sin^2(4x)\right)^2\cos(4x)$
  correct: true
- id: ohw9-p2-q1-b
  content: |-
    $\left(1-\sin^2(4x)\right)^2$
- id: ohw9-p2-q1-c
  content: |-
    $\left(1+\sin^2(4x)\right)^2\cos(4x)$
- id: ohw9-p2-q1-d
  content: |-
    $\left(1-\cos^2(4x)\right)^2\sin(4x)$
- id: ohw9-p2-q1-e
  content: |-
    $\left(1-\sin^2(4x)\right)\cos(4x)$
```

---

<a id="match-the-saved-factor-to-the-substitution"></a>
## Match the Saved Factor to the Substitution

**Example:** Convert $\int\cos^3(7x)\,dx$ into an integral in $u$.

**Explanation**

First rewrite the integrand:

$$
\int\cos^3(7x)\,dx
=\int\left(1-\sin^2(7x)\right)\cos(7x)\,dx.
$$

Choose

$$
u=\sin(7x).
$$

Then

$$
du=7\cos(7x)\,dx,
\qquad
\cos(7x)\,dx=\frac17\,du.
$$

Replace every sine expression and the saved cosine factor:

$$
\int\cos^3(7x)\,dx
=\frac17\int(1-u^2)\,du.
$$

The reciprocal factor $1/7$ is required because the inner angle is $7x$.

```quiz
type: radio
id: ohw9-p2-q2
content: |-
  After setting $u=\sin(9x)$, which $u$-integral equals $\int\cos^3(9x)\,dx$?
options:
- id: ohw9-p2-q2-a
  content: |-
    $\dfrac19\int(1-u^2)\,du$
  correct: true
- id: ohw9-p2-q2-b
  content: |-
    $9\int(1-u^2)\,du$
- id: ohw9-p2-q2-c
  content: |-
    $\dfrac19\int(1+u^2)\,du$
- id: ohw9-p2-q2-d
  content: |-
    $\int(1-u^2)\,du$
- id: ohw9-p2-q2-e
  content: |-
    $\dfrac19\int(1-u^3)\,du$
```

---

<a id="integrate-and-restore-the-original-variable"></a>
## Integrate and Restore the Original Variable

**Example:** Evaluate $\int\cos^3(5x)\,dx$.

**Explanation**

The rewrite and substitution give

$$
\int\cos^3(5x)\,dx
=\frac15\int(1-u^2)\,du,
\qquad
u=\sin(5x).
$$

Integrate the polynomial:

$$
\frac15\int(1-u^2)\,du
=\frac15\left(u-\frac{u^3}{3}\right)+C.
$$

Restore $u=\sin(5x)$ and distribute the factor $1/5$:

$$
\int\cos^3(5x)\,dx
=\frac{\sin(5x)}5-\frac{\sin^3(5x)}{15}+C.
$$

The factor from the inner angle divides both terms.

```quiz
type: radio
id: ohw9-p2-q3
content: |-
  Which expression is an antiderivative of $\cos^3(3x)$?
options:
- id: ohw9-p2-q3-a
  content: |-
    $\dfrac{\sin(3x)}3-\dfrac{\sin^3(3x)}9+C$
  correct: true
- id: ohw9-p2-q3-b
  content: |-
    $\sin(3x)-\dfrac{\sin^3(3x)}3+C$
- id: ohw9-p2-q3-c
  content: |-
    $\dfrac{\sin(3x)}3-\dfrac{\sin^3(3x)}3+C$
- id: ohw9-p2-q3-d
  content: |-
    $\dfrac{\sin(3x)}3+\dfrac{\sin^3(3x)}9+C$
- id: ohw9-p2-q3-e
  content: |-
    $\dfrac{\cos(3x)}3-\dfrac{\cos^3(3x)}9+C$
```

---

<a id="evaluate-and-check-the-assigned-integral"></a>
## Evaluate and Check the Assigned Integral

**Example:** Evaluate

$$
\int\cos^3(12x)\,dx.
$$

**Explanation**

Save one cosine and use the Pythagorean identity:

$$
\int\cos^3(12x)\,dx
=\int\left(1-\sin^2(12x)\right)\cos(12x)\,dx.
$$

Let

$$
u=\sin(12x),
\qquad
du=12\cos(12x)\,dx.
$$

Then

$$
\begin{aligned}
\int\cos^3(12x)\,dx
&=\frac1{12}\int(1-u^2)\,du\\
&=\frac1{12}\left(u-\frac{u^3}{3}\right)+C\\
&=\boxed{\frac{\sin(12x)}{12}-\frac{\sin^3(12x)}{36}+C}.
\end{aligned}
$$

To check, differentiate the proposed antiderivative:

$$
\begin{aligned}
\frac{d}{dx}\left(
\frac{\sin(12x)}{12}-\frac{\sin^3(12x)}{36}
\right)
&=\cos(12x)-\sin^2(12x)\cos(12x)\\
&=\left(1-\sin^2(12x)\right)\cos(12x)\\
&=\cos^3(12x).
\end{aligned}
$$

The lower terms recombine through $1-\sin^2(12x)=\cos^2(12x)$.

```quiz
type: radio
id: ohw9-p2-q4
content: |-
  Which expression is an antiderivative of $\cos^3(8x)$?
options:
- id: ohw9-p2-q4-a
  content: |-
    $\dfrac{\sin(8x)}8-\dfrac{\sin^3(8x)}{24}+C$
  correct: true
- id: ohw9-p2-q4-b
  content: |-
    $\dfrac{\sin(8x)}8-\dfrac{\sin^3(8x)}8+C$
- id: ohw9-p2-q4-c
  content: |-
    $\sin(8x)-\dfrac{\sin^3(8x)}3+C$
- id: ohw9-p2-q4-d
  content: |-
    $\dfrac{\sin(8x)}8+\dfrac{\sin^3(8x)}{24}+C$
- id: ohw9-p2-q4-e
  content: |-
    $\dfrac{\cos(8x)}8-\dfrac{\cos^3(8x)}{24}+C$
```

---

<a id="summary"></a>
## Summary

For an odd cosine power:

1. Save one cosine factor.
2. Rewrite the remaining even power with $\cos^2\theta=1-\sin^2\theta$.
3. Set $u=\sin(ax)$ and replace $\cos(ax)\,dx$ with $\dfrac1a\,du$.
4. Integrate the resulting polynomial, restore $x$, and include $C$.
5. Check by differentiating; forgetting the factor $1/a$ is the main trap.

In particular, for $a\ne0$,

$$
\int\cos^3(ax)\,dx
=\frac{\sin(ax)}a-\frac{\sin^3(ax)}{3a}+C.
$$
