# Finding Torque from a Force at an Angle

<!--
lesson-id: 212-M2-013
topic-code: MTH212.M2.13
-->

## Table of Contents

- [Introduction](#introduction)
- [Identify the Two Torque Vectors](#identify-the-two-torque-vectors)
- [Calculate the Torque Magnitude](#calculate-the-torque-magnitude)
- [Determine the Rotation Direction](#determine-the-rotation-direction)
- [Apply the Method to the Wrench](#apply-the-method-to-the-wrench)
- [Summary](#summary)

## Prerequisites

- Convert centimeters to meters.
- Evaluate the sine of a special angle.
- Recognize clockwise and counterclockwise rotation about a pivot.

---

<a id="introduction"></a>
## Introduction

When a force is applied at an angle to a handle, only the part of the force perpendicular to the position vector produces torque. Use

$$
\vec{\tau}=\vec{r}\times\vec{F},
\qquad
\tau=rF\sin\theta,
$$

where $\theta$ is the angle **between the position vector $\vec{r}$ and the force $\vec{F}$ when their tails are placed together**.

**Recognition cue:** If a diagram gives the handle's angle from a reference line rather than the angle between $\vec{r}$ and $\vec{F}$, find the actual vector-to-vector angle before substituting.

---

<a id="identify-the-two-torque-vectors"></a>
## Identify the Two Torque Vectors

The position vector $\vec{r}$ begins at the pivot and ends where the force is applied. The force vector $\vec{F}$ points in the direction of the applied force. To read $\theta$, mentally slide one vector without rotating it until the vectors have a common tail. This is the same tail-to-tail setup used to define a cross product.

**Example:** A handle points $25^\circ$ above the positive horizontal direction, and a force points straight down. Find the angle between $\vec{r}$ and $\vec{F}$.

**Explanation**

The downward force points at $-90^\circ$ from the positive horizontal direction. Therefore, the smaller angle between the two vectors is

$$
\theta=25^\circ-(-90^\circ)=115^\circ.
$$

The labeled $25^\circ$ is not the angle to use in the torque formula.

Because $115^\circ=180^\circ-65^\circ$,

$$
\sin(115^\circ)=\sin(65^\circ).
$$

This explains why either the obtuse vector-to-vector angle or its acute supplement gives the same torque **magnitude**. The obtuse angle remains the direct answer to “what is the angle between $\vec{r}$ and $\vec{F}$?”

```quiz
type: radio
id: p3-vector-angle
content: |-
  A wrench points $40^\circ$ above the positive horizontal direction. A force at its end points straight down. What angle belongs in $\tau=rF\sin\theta$?
options:
- id: p3-vector-angle-a
  content: |-
    $40^\circ$
- id: p3-vector-angle-b
  content: |-
    $50^\circ$
- id: p3-vector-angle-c
  content: |-
    $130^\circ$
  correct: true
- id: p3-vector-angle-d
  content: |-
    $140^\circ$
```

---

<a id="calculate-the-torque-magnitude"></a>
## Calculate the Torque Magnitude

**Example:** A $60\ \mathrm{N}$ downward force acts $30\ \mathrm{cm}$ from a pivot along a handle that points $20^\circ$ above horizontal. Find the torque magnitude.

**Explanation**

First convert the distance and determine the vector-to-vector angle:

$$
r=0.30\ \mathrm{m},
\qquad
\theta=20^\circ+90^\circ=110^\circ.
$$

Then

$$
\tau
=(0.30\ \mathrm{m})(60\ \mathrm{N})\sin(110^\circ)
\approx16.9\ \mathrm{N}\,\mathrm{m}.
$$

Torque has units of newton meters, not newtons.

The sine factor has a geometric meaning. The perpendicular lever arm is

$$
r_\perp=r\sin\theta,
$$

so the same calculation can be written as $\tau=Fr_\perp$. This makes the limiting cases visible: a force parallel to the handle has $r_\perp=0$ and no torque, while a perpendicular force gives the maximum magnitude $rF$.

```quiz
type: radio
id: p3-torque-magnitude
content: |-
  An $80\ \mathrm{N}$ force acts $25\ \mathrm{cm}$ from a pivot. The angle between $\vec{r}$ and $\vec{F}$ is $120^\circ$. What is the torque magnitude?
options:
- id: p3-torque-magnitude-a
  content: |-
    $10.0\ \mathrm{N}\,\mathrm{m}$
- id: p3-torque-magnitude-b
  content: |-
    $17.3\ \mathrm{N}\,\mathrm{m}$
  correct: true
- id: p3-torque-magnitude-c
  content: |-
    $20.0\ \mathrm{N}\,\mathrm{m}$
- id: p3-torque-magnitude-d
  content: |-
    $173\ \mathrm{N}\,\mathrm{m}$
```

---

<a id="determine-the-rotation-direction"></a>
## Determine the Rotation Direction

Torque magnitude does not tell you the rotation direction. Imagine the pivot fixed and ask which way the force would turn the handle. Equivalently, curl the fingers of your right hand from $\vec{r}$ toward $\vec{F}$; your thumb gives the direction of $\vec{r}\times\vec{F}$.

- A downward force on a point to the right of the pivot turns the handle clockwise.
- A downward force on a point to the left of the pivot turns the handle counterclockwise.

In the plane of the page, counterclockwise torque points out of the page and clockwise torque points into the page. If counterclockwise is positive, clockwise torque is negative. Reversing the cross-product order reverses this direction, just as $\vec{r}\times\vec{F}=-\vec{F}\times\vec{r}$. When a problem asks only for magnitude, report the positive magnitude and state the direction separately if useful.

```quiz
type: radio
id: p3-torque-direction
content: |-
  A force points straight down at the right end of a wrench whose pivot is at the left end. Which direction is the torque about the pivot?
options:
- id: p3-torque-direction-a
  content: |-
    Clockwise
  correct: true
- id: p3-torque-direction-b
  content: |-
    Counterclockwise
- id: p3-torque-direction-c
  content: |-
    No torque because the force is vertical
- id: p3-torque-direction-d
  content: |-
    The direction cannot be determined from the force direction
```

---

<a id="apply-the-method-to-the-wrench"></a>
## Apply the Method to the Wrench

**Source problem**

A $100\ \mathrm{N}$ force is applied straight down on a wrench $50\ \mathrm{cm}$ from its pivot, as shown. Calculate the torque magnitude about the pivot.

![](<../Source/Images/wrench-force-torque.png>)

Enter the torque in newton meters as a number only.

**Explanation**

The position vector follows the wrench at $30^\circ$ above horizontal, while the force points straight down. Thus,

$$
\theta=30^\circ+90^\circ=120^\circ.
$$

An angle-and-value ledger prevents the two common substitutions:

| Quantity | Value | Why |
|---|---:|---|
| Handle angle from horizontal | $30^\circ$ | Labeled in the diagram |
| Angle between $\vec{r}$ and $\vec{F}$ | $120^\circ$ | $30^\circ+90^\circ$ |
| Sine factor | $\sin120^\circ=\sin60^\circ=\sqrt3/2$ | Supplementary angles have equal sine |

After converting $50\ \mathrm{cm}=0.50\ \mathrm{m}$,

$$
\tau=rF\sin\theta
=(0.50\ \mathrm{m})(100\ \mathrm{N})\sin(120^\circ)
=43.301\ldots\ \mathrm{N}\,\mathrm{m}.
$$

A second route uses the perpendicular lever arm:

$$
r_\perp=(0.50\ \mathrm{m})\sin(120^\circ)
=(0.50\ \mathrm{m})\cos(30^\circ)
=0.433\ldots\ \mathrm{m},
$$

so

$$
\tau=Fr_\perp
=(100\ \mathrm{N})(0.433\ldots\ \mathrm{m})
=43.301\ldots\ \mathrm{N}\,\mathrm{m}.
$$

Both routes agree. Also, $43.301\ldots<rF=50\ \mathrm{N}\,\mathrm{m}$, as required because the force is not perpendicular to the wrench.

The diagram values support two significant figures, so the requested number-only answer is

$$
\boxed{43}.
$$

The force turns the wrench clockwise.

```quiz
type: radio
id: p3-source-check
content: |-
  Which conclusion matches the source problem?
options:
- id: p3-source-check-a
  content: |-
    $25\ \mathrm{N}\,\mathrm{m}$, clockwise
- id: p3-source-check-b
  content: |-
    $43\ \mathrm{N}\,\mathrm{m}$, clockwise
  correct: true
- id: p3-source-check-c
  content: |-
    $50\ \mathrm{N}\,\mathrm{m}$, clockwise
- id: p3-source-check-d
  content: |-
    $43\ \mathrm{N}\,\mathrm{m}$, counterclockwise
```

---

<a id="summary"></a>
## Summary

1. Draw $\vec{r}$ from the pivot to the force application point.
2. Find the angle between $\vec{r}$ and $\vec{F}$.
3. Convert the distance to meters and calculate $\tau=rF\sin\theta$.
4. Report the magnitude in $\mathrm{N}\,\mathrm{m}$ and determine clockwise or counterclockwise direction separately.

For the source wrench, $\theta=120^\circ$, so the torque magnitude is $43\ \mathrm{N}\,\mathrm{m}$ and the rotation is clockwise.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../../M3/2026-07-20-Q-2/Study-Guide.md)
Next: [Finding Atwood-Machine Acceleration With a Massive Pulley](../../2026-07-13-M2-4/Lessons/Problem-4.md)

Study guide index: 04/20

---
<!-- lesson-nav:end -->
