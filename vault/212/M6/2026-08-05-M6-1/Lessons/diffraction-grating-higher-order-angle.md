# Finding Higher-Order Diffraction Angles

<!--
lesson-id: 212-M6-018
topic-code: MTH212.M6.18
-->

## Table of Contents

- [Introduction](#introduction)
- [Relate Two Diffraction Orders](#relate-two-diffraction-orders)
- [Use Inverse Sine in Degree Mode](#use-inverse-sine-in-degree-mode)
- [Check Whether the Order Exists](#check-whether-the-order-exists)
- [Match the Source Problem](#match-the-source-problem)
- [Summary](#summary)

## Prerequisites

- Use sine and inverse sine with angles measured in degrees.
- Recognize $m=1,2,3,\ldots$ as the order number of a bright maximum.
- Interpret the diffraction-grating relation $d\sin\theta_m=m\lambda$.

---

<a id="introduction"></a>
## Introduction

Bright maxima from a diffraction grating satisfy

$$
d\sin\theta_m=m\lambda,
$$

where $d$ is the grating spacing, $\lambda$ is the wavelength, and $m$ is the order. If one order angle is known for the same grating and wavelength, eliminate the unchanged $d$ and $\lambda$ instead of trying to find them separately.

For a known first-order angle $\theta_1$,

$$
d\sin\theta_1=\lambda
$$

and therefore

$$
\sin\theta_m=m\sin\theta_1.
$$

The higher-order angle is

$$
\boxed{\theta_m=\sin^{-1}\!\left(m\sin\theta_1\right)}.
$$

The inverse sine is essential: the sine of the angle scales with order, but the angle itself does not.

Because the given angle carries a degree symbol, evaluate both sine and inverse sine in degree mode. The positive-side diffraction angle returned by $\sin^{-1}$ lies between $0^\circ$ and $90^\circ$; the pattern also contains a symmetric maximum at the corresponding negative angle.

---

<a id="relate-two-diffraction-orders"></a>
## Relate Two Diffraction Orders

**Example:** A grating produces a first-order maximum at angle $\theta_1$. Write the fourth-order angle in terms of $\theta_1$.

**Explanation**

For the same $d$ and $\lambda$,

$$
d\sin\theta_1=\lambda,
\qquad
d\sin\theta_4=4\lambda.
$$

Dividing the two equations cancels the common grating spacing and wavelength, which have the same length units:

$$
\frac{d\sin\theta_4}{d\sin\theta_1}
=\frac{4\lambda}{\lambda}
\quad\Longrightarrow\quad
\frac{\sin\theta_4}{\sin\theta_1}=4.
$$

Thus

$$
\sin\theta_4=4\sin\theta_1,
$$

so

$$
\theta_4=\sin^{-1}\!\left(4\sin\theta_1\right),
$$

provided $4\sin\theta_1\le 1$.

```quiz
type: radio
id: grating-higher-order-expression
content: |-
  A diffraction grating has a first-order maximum at $\theta_1$. Which expression gives the third-order angle $\theta_3$, if that order exists?
options:
- id: grating-expression-inverse-sine-three
  content: |-
    $\displaystyle \theta_3=\sin^{-1}\!\left(3\sin\theta_1\right)$
  correct: true
  feedback: |-
    The grating law makes $\sin\theta_m$ proportional to order. Thus $\sin\theta_3=3\sin\theta_1$, and inverse sine gives $\theta_3=\sin^{-1}(3\sin\theta_1)$.
- id: grating-expression-three-theta
  content: |-
    $\theta_3=3\theta_1$
  feedback: |-
    Order scales the sine of the angle, not the angle itself. The relation is $\sin\theta_3=3\sin\theta_1$, so inverse sine must be applied after the multiplication.
- id: grating-expression-divide-three
  content: |-
    $\displaystyle \theta_3=\sin^{-1}\!\left(\frac{\sin\theta_1}{3}\right)$
  feedback: |-
    Higher order multiplies the path difference by $3$; it does not divide it. For fixed $d$ and $\lambda$, $d\sin\theta_3=3\lambda$ gives $\sin\theta_3=3\sin\theta_1$.
- id: grating-expression-sine-only
  content: |-
    $\theta_3=3\sin\theta_1$
  feedback: |-
    The quantity $3\sin\theta_1$ is $\sin\theta_3$, not the angle $\theta_3$. Apply inverse sine to convert that ratio into the requested angle.
```

---

<a id="use-inverse-sine-in-degree-mode"></a>
## Use Inverse Sine in Degree Mode

**Example:** A first-order maximum occurs at $15.0^\circ$. Find the second-order angle.

**Explanation**

First compute the sine value for the new order:

$$
\sin\theta_2=2\sin15.0^\circ=0.517638\ldots
$$

Then use inverse sine in degree mode:

$$
\theta_2=\sin^{-1}(0.517638\ldots)=31.2^\circ.
$$

Keep guard digits until the final rounding step.

```quiz
type: radio
id: grating-higher-order-numerical
content: |-
  A diffraction grating has a first-order maximum at $10.0^\circ$. What is its third-order angle?
options:
- id: grating-numerical-31-4
  content: |-
    $31.4^\circ$
  correct: true
  feedback: |-
    For the same grating and wavelength, $\sin\theta_3=3\sin10.0^\circ=0.520945$. Inverse sine in degree mode gives $\theta_3=31.4^\circ$.
- id: grating-numerical-30
  content: |-
    $30.0^\circ$
  feedback: |-
    This triples the angle directly. The grating equation instead triples its sine: $\theta_3=\sin^{-1}(3\sin10.0^\circ)=31.4^\circ$.
- id: grating-numerical-0-521
  content: |-
    $0.521^\circ$
  feedback: |-
    The value $0.521$ is approximately $\sin\theta_3$, a dimensionless ratio, not an angle in degrees. Applying inverse sine gives $31.4^\circ$.
- id: grating-numerical-3-33
  content: |-
    $3.33^\circ$
  feedback: |-
    Dividing the first-order angle by $3$ moves in the wrong direction. Higher-order maxima have larger $\sin\theta$, so use $\sin^{-1}(3\sin10.0^\circ)$.
```

---

<a id="check-whether-the-order-exists"></a>
## Check Whether the Order Exists

Before pressing inverse sine, check its input. A real diffraction angle requires

$$
m\sin\theta_1\le 1.
$$

On the unit circle, sine is the vertical coordinate, so it can only range from $-1$ to $1$. If the calculated value exceeds $1$, that order cannot occur because no real angle has that sine.

**Example:** If $\theta_1=25.0^\circ$, a third-order maximum would require

$$
\sin\theta_3=3\sin25.0^\circ=1.268\ldots,
$$

so no third-order maximum exists.

```quiz
type: radio
id: grating-order-existence
content: |-
  A diffraction grating has a first-order maximum at $20.0^\circ$. What can be concluded about the third-order maximum?
options:
- id: grating-existence-none
  content: |-
    No third-order maximum exists.
  correct: true
  feedback: |-
    The third order would require $\sin\theta_3=3\sin20.0^\circ=1.026\ldots$. Because a real sine cannot exceed $1$, no third-order maximum exists.
- id: grating-existence-60
  content: |-
    It occurs at $60.0^\circ$.
  feedback: |-
    This triples the angle rather than the sine. The required sine is $3\sin20.0^\circ=1.026\ldots>1$, so this order has no real diffraction angle.
- id: grating-existence-1-03
  content: |-
    It occurs at $1.03^\circ$.
  feedback: |-
    The value $1.026\ldots$ is the attempted sine value, not an angle, and it lies outside the allowed interval $[-1,1]$. Therefore inverse sine has no real result here.
- id: grating-existence-90
  content: |-
    It occurs at $90.0^\circ$.
  feedback: |-
    A $90^\circ$ maximum would require the calculated sine to equal exactly $1$. Here it is $1.026\ldots$, so the third order is beyond the physical limit rather than pinned at $90^\circ$.
```

---

<a id="match-the-source-problem"></a>
## Match the Source Problem

Use the first-order relation to eliminate $d$ and $\lambda$, verify that the third-order sine is at most $1$, and then apply inverse sine in degree mode.

```quiz
type: radio
id: khadley-wave-optics-q5
content: |-
  **Question 5**

  A diffraction grating has a first-order maximum at $18.5^\circ$. Find the third-order angle in degrees:
options:
- id: khadley-wave-optics-q5-72-2
  content: |-
    $72.2$
  correct: true
  feedback: |-
    Since $d\sin\theta_m=m\lambda$, $\sin\theta_3=3\sin18.5^\circ=0.9519\ldots$. Therefore $\theta_3=\sin^{-1}(0.9519\ldots)=72.2^\circ$.
- id: khadley-wave-optics-q5-55-5
  content: |-
    $55.5$
  feedback: |-
    This triples the first-order angle, but the grating law makes the sine proportional to order. The required calculation is $\sin^{-1}(3\sin18.5^\circ)$, which is larger than $55.5^\circ$.
- id: khadley-wave-optics-q5-18-5
  content: |-
    $18.5$
  feedback: |-
    This keeps the first-order angle unchanged. The third order has three times the first-order path difference, so $\sin\theta_3=3\sin18.5^\circ$ before inverse sine is applied.
- id: khadley-wave-optics-q5-0-952
  content: |-
    $0.952$
  feedback: |-
    The value $0.952$ is $\sin\theta_3$, not the angle in degrees. Applying inverse sine in degree mode gives the requested third-order angle.
```

---

<a id="summary"></a>
## Summary

- Cue: one diffraction-order angle is known, and another order angle is requested for the same grating and wavelength.
- Relate orders: $\sin\theta_m=(m/n)\sin\theta_n$; from first order, $\sin\theta_m=m\sin\theta_1$.
- Cancellation check: $d$ and $\lambda$ cancel between order equations, leaving a dimensionless sine ratio.
- Check existence: sine is a unit-circle coordinate, so the calculated value must lie between $-1$ and $1$.
- Find the positive-side angle: apply inverse sine in degree mode, verify it lies from $0^\circ$ to $90^\circ$, and round only at the end.
- Main trap: order multiplies $\sin\theta$, not $\theta$ itself.
