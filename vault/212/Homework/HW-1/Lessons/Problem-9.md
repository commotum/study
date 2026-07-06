# Checking the Magnitude of Centripetal Acceleration

## Table of Contents

- [Introduction](#introduction)
- [Recognizing the Direction of Circular Acceleration](#recognizing-the-direction-of-circular-acceleration)
- [Using the Speed Formula for the Magnitude](#using-the-speed-formula-for-the-magnitude)
- [Rewriting the Magnitude With Angular Speed](#rewriting-the-magnitude-with-angular-speed)
- [Checking a True-or-False Statement](#checking-a-true-or-false-statement)

## Prerequisites

- In uniform circular motion, the object moves at constant speed around a circle
- Velocity is tangent to the circle
- Acceleration points toward the center of the circle
- The magnitude of a vector $\vec{a}$ is written $|\vec{a}|$
- Linear speed and angular speed are related by $v=\omega r$

---

<a id="introduction"></a>
## Introduction

In uniform circular motion, the speed stays constant, but the velocity vector keeps changing direction. That change in direction gives the object an acceleration toward the center of the circle.

The recognition cue is a statement about the magnitude of $\vec{a}$ for an object moving in a circle. The reusable check is:

$$
|\vec{a}|=\frac{v^2}{r}.
$$

If the problem also gives angular speed $\omega$, use

$$
v=\omega r.
$$

Then

$$
\frac{v^2}{r}
=
\frac{(\omega r)^2}{r}
=
\omega^2r.
$$

So the magnitude of centripetal acceleration can be written either way:

$$
|\vec{a}|=\frac{v^2}{r}=\omega^2r.
$$

The main trap is mixing up the vector direction with the magnitude. The acceleration vector points inward, but its magnitude is the positive scalar $\dfrac{v^2}{r}$.

That means the statement

$$
|\vec{a}|=\frac{v^2}{r}
$$

is different from a statement about the whole vector $\vec{a}$.

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

**Example:** An object moves in a circle of radius $4\ \mathrm{m}$ with speed $6\ \mathrm{m/s}$. What is the magnitude of its acceleration?

**Explanation**

Use the centripetal acceleration magnitude formula:

$$
|\vec{a}|=\frac{v^2}{r}.
$$

Here $v=6\ \mathrm{m/s}$ and $r=4\ \mathrm{m}$, so

$$
|\vec{a}|=\frac{6^2}{4}
=
\frac{36}{4}
=
9\ \mathrm{m/s^2}.
$$

The units also check:

$$
\frac{(\mathrm{m/s})^2}{\mathrm{m}}
=
\frac{\mathrm{m^2/s^2}}{\mathrm{m}}
=
\mathrm{m/s^2}.
$$

```quiz
type: radio
id: q-2
content: |-
  An object moves in a circle of radius $3\ \mathrm{m}$ with speed $12\ \mathrm{m/s}$. What is $|\vec{a}|$?
options:
- id: a
  content: |-
    $4\ \mathrm{m/s^2}$
- id: b
  content: |-
    $36\ \mathrm{m/s^2}$
- id: c
  content: |-
    $48\ \mathrm{m/s^2}$
  correct: true
- id: d
  content: |-
    $144\ \mathrm{m/s^2}$
```

---

<a id="rewriting-the-magnitude-with-angular-speed"></a>
## Rewriting the Magnitude With Angular Speed

**Example:** Show that $\dfrac{v^2}{r}$ becomes $\omega^2r$ when $v=\omega r$.

**Explanation**

Start with the speed form:

$$
\frac{v^2}{r}.
$$

Substitute $v=\omega r$:

$$
\frac{v^2}{r}
=
\frac{(\omega r)^2}{r}.
$$

Square both factors in the numerator:

$$
\frac{(\omega r)^2}{r}
=
\frac{\omega^2r^2}{r}.
$$

Cancel one factor of $r$:

$$
\frac{\omega^2r^2}{r}
=
\omega^2r.
$$

```quiz
type: radio
id: q-3
content: |-
  If $v=\omega r$, which expression is equal to $\dfrac{v^2}{r}$?
options:
- id: a
  content: |-
    $\omega r$
- id: b
  content: |-
    $\omega r^2$
- id: c
  content: |-
    $\omega^2r$
  correct: true
- id: d
  content: |-
    $\dfrac{\omega^2}{r}$
```

---

<a id="checking-a-true-or-false-statement"></a>
## Checking a True-or-False Statement

**Example:** True or false: for an object in uniform circular motion, $\vec{a}$ has magnitude $\dfrac{v^2}{r}$.

**Explanation**

This statement is true because it asks for the magnitude of $\vec{a}$, not the full vector direction. The full acceleration points inward, but its size is

$$
|\vec{a}|=\frac{v^2}{r}.
$$

If angular speed is included, the same magnitude can also be written as

$$
|\vec{a}|=\omega^2r.
$$

So the combined magnitude statement

$$
|\vec{a}|=\frac{v^2}{r}=\omega^2r
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
content: |-
  Consider an object undergoing uniform circular motion. Let $\vec{r}$ be the position of the object relative to the circle's center, $\vec{v}$ the velocity, $\omega$ the angular speed, and $\vec{a}$ the acceleration.

  True or false: $\vec{a}$ has magnitude $\dfrac{v^2}{r}=\omega^2r$.
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

If the problem uses angular speed, substitute $v=\omega r$:

$$
\frac{v^2}{r}
=
\frac{(\omega r)^2}{r}
=
\omega^2r.
$$

The statement "$\vec{a}$ has magnitude $\dfrac{v^2}{r}=\omega^2r$" is true. It describes the size of the acceleration, not the direction of the acceleration vector. Since $\vec{r}$ points outward from the center, the acceleration vector points opposite $\vec{r}$; that direction detail does not change the magnitude.
