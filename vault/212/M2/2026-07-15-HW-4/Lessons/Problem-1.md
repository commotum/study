# Comparing Rolling Objects on an Incline

## Table of Contents

- [Introduction](#introduction)
- [Use the Rolling-Acceleration Formula](#use-the-rolling-acceleration-formula)
- [Cancel Mass and Radius for the Same Shape](#cancel-mass-and-radius-for-the-same-shape)
- [Connect Acceleration to Arrival Time](#connect-acceleration-to-arrival-time)
- [Know When Shape Changes the Result](#know-when-shape-changes-the-result)
- [Apply the Test to the Two Cylinders](#apply-the-test-to-the-two-cylinders)
- [Summary](#summary)

## Prerequisites

- Apply Newton's second law along an incline.
- Use $\tau=I\alpha$ and the rolling-without-slipping condition $a=\alpha r$.
- Recognize $I=\frac12mr^2$ for a uniform solid cylinder.
- Use $L=\frac12at^2$ for motion from rest with constant acceleration.

---

<a id="introduction"></a>
## Introduction

When two objects roll without slipping down the same ramp, do not compare their masses or radii by themselves. Instead, compare the dimensionless rotational-inertia factor

$$
\kappa=\frac{I}{mr^2}.
$$

The acceleration of a rolling object depends on $\kappa$. Objects with the same shape and mass distribution have the same $\kappa$, even when their masses and radii differ.

**Recognition cue:** The objects share a ramp and roll without slipping, but their masses or radii differ. Rewrite each moment of inertia as $I=\kappa mr^2$ and compare $\kappa$.

This model assumes rigid objects, enough static friction to maintain rolling without slipping, and negligible rolling resistance or other energy losses.

---

<a id="use-the-rolling-acceleration-formula"></a>
## Use the Rolling-Acceleration Formula

For an object of mass $m$ and radius $r$ rolling without slipping down a ramp inclined at angle $\theta$,

$$
a=\frac{g\sin\theta}{1+\dfrac{I}{mr^2}}.
$$

Here $I$ is the moment of inertia about the center of mass and $g$ is the magnitude of gravitational acceleration.

This follows by combining translation along the ramp with rotation about the center:

$$
ma=mg\sin\theta-f,
$$

$$
fr=I\alpha=I\frac{a}{r}.
$$

The symbol $f$ is the static-friction force. It supplies the torque needed for rolling.

Therefore,

$$
mg\sin\theta=a\left(m+\frac{I}{r^2}\right),
$$

which gives the acceleration formula above.

**Example:** A rolling object has $I=\frac25mr^2$. Find its acceleration down a ramp inclined at angle $\theta$.

**Explanation**

Substitute $I/(mr^2)=2/5$:

$$
a=\frac{g\sin\theta}{1+\frac25}
=\frac57g\sin\theta.
$$

```quiz
type: radio
id: p1-rolling-factor
content: |-
  A rolling object has $I=\frac34mr^2$. What is its acceleration down a ramp inclined at angle $\theta$?
options:
- id: a
  content: |-
    $\frac34g\sin\theta$
- id: b
  content: |-
    $\frac47g\sin\theta$
  correct: true
- id: c
  content: |-
    $\frac74g\sin\theta$
- id: d
  content: |-
    $g\sin\theta$
- id: e
  content: |-
    $\frac14g\sin\theta$
```

---

<a id="cancel-mass-and-radius-for-the-same-shape"></a>
## Cancel Mass and Radius for the Same Shape

**Example:** Compare two uniform solid cylinders on the same ramp. Cylinder A has mass $m$ and radius $r$. Cylinder B has mass $3m$ and radius $2r$.

**Explanation**

Every uniform solid cylinder has

$$
I=\frac12mr^2.
$$

Thus, for either cylinder,

$$
\frac{I}{mr^2}=\frac{\frac12mr^2}{mr^2}=\frac12.
$$

The mass and radius cancel. Both accelerations are

$$
a=\frac{g\sin\theta}{1+\frac12}=\frac23g\sin\theta.
$$

The larger mass does not provide an advantage because it increases both the downhill gravitational force and the object's resistance to translational and rotational acceleration in matching proportions.

```quiz
type: radio
id: p1-same-shape
content: |-
  Two uniform solid cylinders roll without slipping down the same incline. One has mass $2m$ and radius $r$; the other has mass $m$ and radius $3r$. How do their accelerations compare?
options:
- id: a
  content: |-
    The cylinder of mass $2m$ has the greater acceleration.
- id: b
  content: |-
    The cylinder of radius $3r$ has the greater acceleration.
- id: c
  content: |-
    Their accelerations are equal.
  correct: true
- id: d
  content: |-
    The comparison requires numerical values for $m$ and $r$.
- id: e
  content: |-
    The comparison requires the coefficient of static friction.
```

---

<a id="connect-acceleration-to-arrival-time"></a>
## Connect Acceleration to Arrival Time

**Example:** Two objects start from rest at the top of the same straight ramp and have equal constant accelerations. Compare their arrival times.

**Explanation**

Both objects travel the same distance $L$. Starting from rest,

$$
L=\frac12at^2,
$$

so

$$
t=\sqrt{\frac{2L}{a}}.
$$

Equal $L$ and equal $a$ give equal $t$. For a ramp of height $h$ and angle $\theta$, $L=h/\sin\theta$, which is also the same for both objects.

```quiz
type: radio
id: p1-arrival-time
content: |-
  Objects A and B start from rest at the same point on a ramp. If $a_A=a_B$, which statement is correct?
options:
- id: a
  content: |-
    The heavier object arrives first.
- id: b
  content: |-
    The object with the larger radius arrives first.
- id: c
  content: |-
    They arrive at the same time.
  correct: true
- id: d
  content: |-
    Arrival time depends only on mass.
- id: e
  content: |-
    There is not enough information because their final speeds may differ.
```

---

<a id="know-when-shape-changes-the-result"></a>
## Know When Shape Changes the Result

Mass and radius cancel only after the moment of inertia is written as

$$
I=\kappa mr^2.
$$

The value of $\kappa$ describes how mass is distributed about the axis. A smaller $\kappa$ gives a larger acceleration:

$$
a=\frac{g\sin\theta}{1+\kappa}.
$$

**Example:** A uniform solid cylinder has $\kappa=1/2$, while a thin hoop has $\kappa=1$. Which is faster on the same ramp?

**Explanation**

The cylinder has the smaller rotational-inertia factor:

$$
a_{\text{cylinder}}=\frac23g\sin\theta,
\qquad
a_{\text{hoop}}=\frac12g\sin\theta.
$$

The cylinder reaches the bottom first. Shape matters here because the two objects have different values of $\kappa$.

```quiz
type: radio
id: p1-different-shapes
content: |-
  A uniform solid sphere with $\kappa=\frac25$ and a uniform solid cylinder with $\kappa=\frac12$ roll without slipping from rest down the same ramp. Which object reaches the bottom first?
options:
- id: a
  content: |-
    The solid sphere
  correct: true
- id: b
  content: |-
    The solid cylinder
- id: c
  content: |-
    They reach the bottom at the same time
- id: d
  content: |-
    The heavier object, regardless of which one it is
- id: e
  content: |-
    The larger object, regardless of which one it is
```

---

<a id="apply-the-test-to-the-two-cylinders"></a>
## Apply the Test to the Two Cylinders

**Example:** One uniform solid cylinder has mass $M$ and radius $R$. A second has mass $4M$ and radius $R/2$. Both start from rest and roll without slipping down the same ramp. Compare their arrival times.

**Explanation**

For the first cylinder,

$$
\kappa_1=\frac{I_1}{MR^2}
=\frac{\frac12MR^2}{MR^2}
=\frac12.
$$

For the second cylinder,

$$
\begin{aligned}
\kappa_2
&=\frac{I_2}{(4M)(R/2)^2} \\
&=\frac{\frac12(4M)(R/2)^2}{(4M)(R/2)^2} \\
&=\frac12.
\end{aligned}
$$

Therefore,

$$
a_1=a_2=\frac{g\sin\theta}{1+\frac12}
=\frac23g\sin\theta.
$$

They start from rest, travel the same ramp length, and have the same acceleration, so they reach the bottom at the same time.

```quiz
type: radio
id: p1-original-check
content: |-
  Two uniform solid cylinders are released simultaneously from rest at the top of a ramp of height $h$ inclined at angle $\theta$. One cylinder has mass $M$ and radius $R$; the other has mass $4M$ and radius $R/2$. Both roll without slipping.

  Which cylinder reaches the bottom first?
options:
- id: a
  content: |-
    The cylinder with mass $M$ and radius $R$
- id: b
  content: |-
    The cylinder with mass $4M$ and radius $R/2$
- id: c
  content: |-
    They reach the bottom at the same time
  correct: true
```

---

<a id="summary"></a>
## Summary

When rolling objects are compared on the same ramp:

1. Write $I=\kappa mr^2$.
2. Substitute into $a=g\sin\theta/(1+\kappa)$.
3. Compare $\kappa$, not mass or radius separately.
4. Equal shape and mass distribution mean equal $\kappa$, equal acceleration, and equal arrival time from the same starting point.

The main trap is assuming that a heavier or smaller object must roll faster. Those details cancel for objects with the same shape; a different mass distribution is what can change the result.
