# Finding Radial Acceleration From Inward Forces

<!--
lesson-id: 212-M1-055
topic-code: MTH212.M1.55
-->

## Table of Contents

- [Introduction](#introduction)
- [Set the Inward Radial Equation](#set-the-inward-radial-equation)
- [Resolve Weight Onto the Radial Axis](#resolve-weight-onto-the-radial-axis)
- [Solve for the Radial Acceleration](#solve-for-the-radial-acceleration)
- [Use the Given Numbers and Round](#use-the-given-numbers-and-round)
- [Summary](#summary)

## Prerequisites

- Use Newton's second law along one chosen axis: $\sum F = ma$.
- Know that weight has magnitude $mg$ and points downward.
- Use cosine for the component of a vector adjacent to the marked angle.
- Keep acceleration units in $\mathrm{m}/\mathrm{s}^2$.

---

<a id="introduction"></a>
## Introduction

In this problem, the ball is moving in a vertical circle and the $r$-axis is defined to point inward along the string. When the question asks for radial acceleration, use Newton's second law only along that inward radial axis:

$$
\sum F_r = ma_r.
$$

The recognition cue is the inward $r$-axis. Any force component that points toward the center is positive in the radial equation. Use this order: choose the positive radial direction, keep only radial force components, then isolate $a_r$.

![](../Source/Images/vertical-circle-ball-string-diagram.png)

---

<a id="set-the-inward-radial-equation"></a>
## Set the Inward Radial Equation

**Example:** A ball is at the upper-left part of a vertical circle. The $r$-axis points inward along the string, and the string tension is $T$. Write the radial force equation before substituting numbers.

**Explanation**

Tension points along the string toward the center, so $T$ is positive in the inward radial direction. Gravity points downward, and at this position part of gravity also points inward.

Call the inward component of gravity $F_{g,r}$. Then

$$
T + F_{g,r} = ma_r.
$$

The equation should include only radial components. Tangential components do not determine $a_r$, and the full weight $mg$ should not be placed into the radial equation unless the entire weight points along the radial axis.

```quiz
type: radio
id: p3-q1-radial-equation
shuffle: true
content: |-
  A ball is in a vertical circle, the $r$-axis points inward along the string, and the tension is $T$. If the inward component of gravity is $F_{g,r}$, which equation correctly sets up the radial direction?
options:
- id: a
  content: |-
    $T + F_{g,r} = ma_r$
  correct: true
- id: b
  content: |-
    $T - F_{g,r} = ma_r$
- id: c
  content: |-
    $mg = ma_r$
- id: d
  content: |-
    $T = ma_t$
- id: e
  content: |-
    $T + mg = ma_r$
```

---

<a id="resolve-weight-onto-the-radial-axis"></a>
## Resolve Weight Onto the Radial Axis

**Example:** The angle $\theta$ is measured between the string direction and the vertical radius in the diagram. Find the inward radial component of the ball's weight.

**Explanation**

At the shown position, the inward direction from the ball to the center is tilted by the same angle $\theta$ from the downward vertical. Weight points downward, so the inward radial component is the adjacent component of $mg$:

$$
F_{g,r} = mg\cos\theta.
$$

This component is positive because it points partly inward. The common check is: adjacent to the marked angle gives cosine; opposite to the marked angle would give sine.

```quiz
type: radio
id: p3-q2-weight-component
shuffle: true
content: |-
  A ball is in the same upper-left position, and the inward radial axis makes angle $\theta$ with the downward direction of gravity. What is the inward radial component of the ball's weight?
options:
- id: a
  content: |-
    $mg\cos\theta$
  correct: true
- id: b
  content: |-
    $mg\sin\theta$
- id: c
  content: |-
    $-mg\cos\theta$
- id: d
  content: |-
    $\dfrac{mg}{\cos\theta}$
- id: e
  content: |-
    $mg$
```

---

<a id="solve-for-the-radial-acceleration"></a>
## Solve for the Radial Acceleration

**Example:** A ball has $T=2.4\ \mathrm{N}$, $m=0.60\ \mathrm{kg}$, and $\theta=60^\circ$. Find $a_r$.

**Explanation**

Start with the inward radial equation:

$$
T + mg\cos\theta = ma_r.
$$

The target variable is $a_r$. Treat $T$, $m$, $g$, and $\theta$ as known quantities, then divide every force term by $m$:

$$
a_r = \frac{T}{m} + g\cos\theta.
$$

Now substitute. Since the angle is given in degrees, evaluate the cosine in degree mode:

$$
a_r = \frac{2.4}{0.60} + 9.8\cos(60^\circ)
= 4.0 + 4.9
= 8.9\ \mathrm{m}/\mathrm{s}^2.
$$

```quiz
type: radio
id: p3-q3-solve-acceleration
shuffle: true
content: |-
  A ball in the same setup has $T=3.0\ \mathrm{N}$, $m=0.50\ \mathrm{kg}$, and $\theta=60^\circ$. Using $a_r=\frac{T}{m}+g\cos\theta$, what is $a_r$?
options:
- id: a
  content: |-
    $6.0\ \mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $10.9\ \mathrm{m}/\mathrm{s}^2$
  correct: true
- id: c
  content: |-
    $15.8\ \mathrm{m}/\mathrm{s}^2$
- id: d
  content: |-
    $1.1\ \mathrm{m}/\mathrm{s}^2$
- id: e
  content: |-
    $14.5\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="use-the-given-numbers-and-round"></a>
## Use the Given Numbers and Round

**Example:** In the assigned problem, $L=0.88\ \mathrm{m}$, $T=1.2\ \mathrm{N}$, $m=0.56\ \mathrm{kg}$, and $\theta=14^\circ$. Find the magnitude of the radial acceleration.

**Explanation**

The length $L$ is given, but it is not needed for this force-balance version because the speed is not given. The radial force equation already determines $a_r$:

$$
a_r = \frac{T}{m} + g\cos\theta.
$$

Substitute the values:

$$
a_r = \frac{1.2}{0.56} + 9.8\cos(14^\circ)
= 2.14 + 9.51
= 11.65\ \mathrm{m}/\mathrm{s}^2.
$$

To two significant figures, the magnitude is

$$
a_r = 12\ \mathrm{m}/\mathrm{s}^2.
$$

```quiz
type: radio
id: p3-q4-original-style
shuffle: true
content: |-
  A ball is in the same vertical-circle position with $L=1.1\ \mathrm{m}$, $T=1.8\ \mathrm{N}$, $m=0.45\ \mathrm{kg}$, and $\theta=20^\circ$. What is the radial acceleration magnitude to two significant figures?
options:
- id: a
  content: |-
    $4.0\ \mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $9.2\ \mathrm{m}/\mathrm{s}^2$
- id: c
  content: |-
    $13\ \mathrm{m}/\mathrm{s}^2$
  correct: true
- id: d
  content: |-
    $7.4\ \mathrm{m}/\mathrm{s}^2$
- id: e
  content: |-
    $5.2\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="summary"></a>
## Summary

When the $r$-axis points inward along the string, write Newton's second law in the inward radial direction:

$$
T + mg\cos\theta = ma_r.
$$

Then solve:

$$
a_r = \frac{T}{m} + g\cos\theta.
$$

The main trap is using the length $L$, using the full weight $mg$, or using $mg\sin\theta$. In this diagram, $\theta$ is the angle that makes the inward part of weight the adjacent component, so the radial weight component is $mg\cos\theta$. For numerical work, keep the calculator in degree mode when $\theta$ is given in degrees.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
