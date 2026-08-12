# Checking the Magnitude of Centripetal Acceleration

<!--
lesson-id: 212-M1-004
topic-code: MTH212.M1.04
-->

## Table of Contents

- [Introduction](#introduction)
- [Recognizing the Direction of Circular Acceleration](#recognizing-the-direction-of-circular-acceleration)
- [Using the Speed Formula for the Magnitude](#using-the-speed-formula-for-the-magnitude)
- [Rewriting the Magnitude With Angular Speed](#rewriting-the-magnitude-with-angular-speed)
- [Read a Magnitude Statement](#read-a-magnitude-statement)

## Prerequisites

- In uniform circular motion, the object moves at constant speed around a circle
- Velocity is tangent to the circle
- Acceleration points toward the center of the circle
- The magnitude of a vector $\vec{a}$ is written $|\vec{a}|$
- Linear speed and angular speed are related by $v=r\omega$

---

<a id="introduction"></a>
## Introduction

Imagine a car rounding a circular track while its speedometer stays fixed. The car is still accelerating because its velocity turns continuously with the road. That acceleration points toward the center of the track. A faster car or a tighter turn changes the velocity direction more rapidly, which is captured by

$$
|\vec{a}|=\frac{v^2}{r}.
$$

Because uniform circular motion has $a_t=0$, this magnitude is the radial acceleration used on the cheat sheet: $a_r=|\vec{a}|$.

If the motion is described by angular speed $\omega$, use

$$
v=r\omega.
$$

Then

$$
\frac{v^2}{r}
=
\frac{(r\omega)^2}{r}
=
r\omega^2.
$$

So the magnitude of radial acceleration can be written either way:

$$
|\vec{a}|=\frac{v^2}{r}=r\omega^2.
$$

The acceleration vector points inward, but its magnitude is the positive scalar $\dfrac{v^2}{r}$. Thus the statement

$$
|\vec{a}|=\frac{v^2}{r}
$$

describes how large the acceleration is, not which way it points.

The geometry also explains why the speed is squared. At two nearby instants, the triangle formed by the velocity vectors is similar to the triangle formed by the radius vectors, so

$$
\frac{|\Delta\vec{v}|}{v}=\frac{\Delta s}{r},
$$

where $|\Delta\vec{v}|$ is the magnitude of the change in velocity. Divide by $\Delta t$ and take the short-time limit:

$$
a_r
=\frac{v}{r}\lim_{\Delta t\to 0}\frac{\Delta s}{\Delta t}
=\frac{v^2}{r}.
$$

---

<a id="recognizing-the-direction-of-circular-acceleration"></a>
## Recognizing the Direction of Circular Acceleration

**Example:** An object moves clockwise around a circle at constant speed. At one instant, its velocity points to the right. What is true about its acceleration at that instant?

**Explanation**

For uniform circular motion, the acceleration is not in the direction of motion. The velocity is tangent to the circle, while the acceleration points toward the center.

So if the velocity points to the right, that only tells us the tangent direction. The acceleration must point along the radius toward the center of the circle.

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  In uniform circular motion, which statement correctly describes $\vec{a}$?
options:
- id: a
  content: |-
    $\vec{a}$ points in the same direction as $\vec{v}$.
- id: b
  content: |-
    $\vec{a}$ points opposite the direction of $\vec{v}$.
- id: c
  content: |-
    $\vec{a}$ points toward the center of the circle.
  correct: true
- id: d
  content: |-
    $\vec{a}$ is zero because the speed is constant.
```

---

<a id="using-the-speed-formula-for-the-magnitude"></a>
## Using the Speed Formula for the Magnitude

**Example:** An object moves in a circle of radius $4\ \mathrm{m}$ with speed $6\ \mathrm{m}/\mathrm{s}$. What is the magnitude of its acceleration?

**Explanation**

Use the radial-acceleration magnitude formula:

$$
|\vec{a}|=\frac{v^2}{r}.
$$

Here $v=6\ \mathrm{m}/\mathrm{s}$ and $r=4\ \mathrm{m}$, so

$$
|\vec{a}|=\frac{6^2}{4}
=
\frac{36}{4}
=
9\ \mathrm{m}/\mathrm{s}^2.
$$

The units also check:

$$
\frac{(\mathrm{m}/\mathrm{s})^2}{\mathrm{m}}
=
\frac{\mathrm{m}^2/\mathrm{s}^2}{\mathrm{m}}
=
\mathrm{m}/\mathrm{s}^2.
$$

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  An object moves in a circle of radius $3\ \mathrm{m}$ with speed $12\ \mathrm{m}/\mathrm{s}$. What is $|\vec{a}|$?
options:
- id: a
  content: |-
    $4\ \mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $36\ \mathrm{m}/\mathrm{s}^2$
- id: c
  content: |-
    $48\ \mathrm{m}/\mathrm{s}^2$
  correct: true
- id: d
  content: |-
    $144\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="rewriting-the-magnitude-with-angular-speed"></a>
## Rewriting the Magnitude With Angular Speed

**Example:** Show that $\dfrac{v^2}{r}$ becomes $r\omega^2$ when $v=r\omega$.

**Explanation**

Start with the speed form:

$$
\frac{v^2}{r}.
$$

Substitute $v=r\omega$:

$$
\frac{v^2}{r}
=
\frac{(r\omega)^2}{r}.
$$

Square both factors in the numerator:

$$
\frac{(r\omega)^2}{r}
=
\frac{r^2\omega^2}{r}.
$$

Cancel one factor of $r$:

$$
\frac{r^2\omega^2}{r}
=
r\omega^2.
$$

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  If $v=r\omega$, which expression is equal to $\dfrac{v^2}{r}$?
options:
- id: a
  content: |-
    $r\omega$
- id: b
  content: |-
    $r^2\omega$
- id: c
  content: |-
    $r\omega^2$
  correct: true
- id: d
  content: |-
    $\dfrac{\omega^2}{r}$
```

---

<a id="read-a-magnitude-statement"></a>
## Read a Magnitude Statement

**Example:** True or false: for an object in uniform circular motion, $\vec{a}$ has magnitude $\dfrac{v^2}{r}$.

**Explanation**

This statement is true because it asks for the magnitude of $\vec{a}$, not the full vector direction. The full acceleration points inward, but its size is

$$
|\vec{a}|=\frac{v^2}{r}.
$$

If angular speed is included, the same magnitude can also be written as

$$
|\vec{a}|=r\omega^2.
$$

So the combined magnitude statement

$$
|\vec{a}|=\frac{v^2}{r}=r\omega^2
$$

is true.

The position vector $\vec{r}$ points from the center to the object, so it points outward. The acceleration vector points inward, opposite $\vec{r}$. If $\hat{r}$ is the outward unit radial vector, then the vector direction would be written with a minus sign:

$$
\vec{a}=-\frac{v^2}{r}\hat{r}.
$$

The true-or-false statement avoids that direction issue by asking only for the magnitude.

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  Consider an object undergoing uniform circular motion. Let $\vec{r}$ be the position of the object relative to the circle's center, $\vec{v}$ the velocity, $\omega$ the angular speed, and $\vec{a}$ the acceleration.

  True or false: $\vec{a}$ has magnitude $\dfrac{v^2}{r}=r\omega^2$.
options:
- id: a
  content: |-
    True
  correct: true
- id: b
  content: |-
    False
```

```quiz
type: radio
id: q-5
shuffle: true
content: |-
  Why does the statement "$\vec{a}$ has magnitude $\dfrac{v^2}{r}$" not need a negative sign?
options:
- id: a
  content: |-
    Magnitudes are positive scalars, so the inward direction is not part of $|\vec{a}|$.
  correct: true
- id: b
  content: |-
    The acceleration points in the same direction as $\vec{r}$.
- id: c
  content: |-
    The acceleration is zero whenever the speed is constant.
- id: d
  content: |-
    The formula $\dfrac{v^2}{r}$ gives velocity instead of acceleration.
```

---

## Summary

For uniform circular motion, first notice that the acceleration points toward the center even though the velocity is tangent to the circle. Then check the magnitude with

$$
|\vec{a}|=\frac{v^2}{r}.
$$

When the motion is described by angular speed, substitute $v=r\omega$:

$$
\frac{v^2}{r}
=
\frac{(r\omega)^2}{r}
=
r\omega^2.
$$

The statement "$\vec{a}$ has magnitude $\dfrac{v^2}{r}=r\omega^2$" is true. It describes the size of the acceleration, not the direction of the acceleration vector. Since $\vec{r}$ points outward from the center, the acceleration vector points opposite $\vec{r}$; that direction detail does not change the magnitude.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Finding the Net-Force Direction in Circular Motion](../../2026-07-03-HW-2/Lessons/Problem-4.md)

Study guide index: 07/35

---
<!-- lesson-nav:end -->
