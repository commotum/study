# Relating Tangential Speed to Angular Speed

## Table of Contents

- [Introduction](#introduction)
- [Converting Angle Swept to Arc Length](#converting-angle-swept-to-arc-length)
- [Turning Arc Length per Time Into Speed](#turning-arc-length-per-time-into-speed)
- [Checking the Units](#checking-the-units)
- [Reading Magnitude Statements](#reading-magnitude-statements)
- [Checking the True-or-False Claim](#checking-the-true-or-false-claim)

## Prerequisites

- A point in circular motion stays a fixed distance $r$ from the center
- Angular speed $\omega$ measures angle swept per unit time
- For angles measured in radians, arc length satisfies $s=r\theta$
- Speed is distance traveled per unit time

---

<a id="introduction"></a>
## Introduction

In uniform circular motion, the object moves around a circle with constant radius $r$ and constant angular speed $\omega$.

The recognition cue is a statement about the **magnitude** of the velocity vector $\vec v$:

$$
|\vec v| \stackrel{?}{=} r\omega.
$$

The move is to convert angular speed into ordinary speed. Angular speed tells how much angle is swept out per unit time. Multiplying by the radius converts that angular rate into arc-length rate.

The variables are:

- $r$: radius of the circle
- $\theta$: angle swept out in radians
- $\omega$: angular speed, or angle per time
- $|\vec v|$: speed, or distance per time

The governing relationship comes from arc length:

$$
s=r\theta.
$$

Divide by time:

$$
\frac{s}{t}=r\frac{\theta}{t}.
$$

Since $\dfrac{s}{t}=|\vec v|$ and $\dfrac{\theta}{t}=\omega$, this becomes

$$
|\vec v|=r\omega.
$$

So the homework statement "$\vec v$ has magnitude $r\omega$" is true.

---

<a id="converting-angle-swept-to-arc-length"></a>
## Converting Angle Swept to Arc Length

**Example:** A point moves around a circle of radius $5$ meters and sweeps out an angle of $2$ radians. What arc length does it travel?

**Explanation**

For angles measured in radians, arc length is

$$
s=r\theta.
$$

Here $r=5$ and $\theta=2$, so

$$
s=5(2)=10.
$$

The point travels $10$ meters along the circle.

```quiz
type: radio
id: q-1
content: |-
  A point moves around a circle of radius $3$ meters and sweeps out an angle of $4$ radians. What arc length does it travel?
options:
- id: a
  content: |-
    $7$ meters
- id: b
  content: |-
    $12$ meters
  correct: true
- id: c
  content: |-
    $\dfrac{4}{3}$ meters
- id: d
  content: |-
    $\dfrac{3}{4}$ meters
```

---

<a id="turning-arc-length-per-time-into-speed"></a>
## Turning Arc Length per Time Into Speed

**Example:** A point moves on a circle of radius $6$ meters with angular speed $2$ radians per second. What is its speed?

**Explanation**

Angular speed tells us the angle swept per second:

$$
\omega=2\ \mathrm{rad/s}.
$$

Each radian corresponds to $r$ meters of arc length, so multiply by the radius:

$$
|\vec v|=r\omega=6(2)=12.
$$

The speed is $12\ \mathrm{m/s}$.

```quiz
type: radio
id: q-2
content: |-
  A point moves on a circle of radius $4$ meters with angular speed $3$ radians per second. What is its speed?
options:
- id: a
  content: |-
    $7\ \mathrm{m/s}$
- id: b
  content: |-
    $12\ \mathrm{m/s}$
  correct: true
- id: c
  content: |-
    $\dfrac{3}{4}\ \mathrm{m/s}$
- id: d
  content: |-
    $\dfrac{4}{3}\ \mathrm{m/s}$
```

---

<a id="checking-the-units"></a>
## Checking the Units

**Example:** If $r$ is measured in meters and $\omega$ is measured in radians per second, what units does $r\omega$ have?

**Explanation**

Substitute the units into the product:

$$
[r\omega]=\mathrm{m}\cdot\frac{\mathrm{rad}}{\mathrm{s}}.
$$

A radian is the ratio of arc length to radius, so it does not add a new length unit. The product has units

$$
\frac{\mathrm{m}}{\mathrm{s}}.
$$

Those are speed units, which matches the meaning of $|\vec v|$.

```quiz
type: radio
id: q-3
content: |-
  If $r$ is measured in meters and $\omega$ is measured in radians per second, what units does $r\omega$ have?
options:
- id: a
  content: |-
    $\mathrm{m/s}$
  correct: true
- id: b
  content: |-
    $\mathrm{rad/m}$
- id: c
  content: |-
    $\mathrm{m^2/s}$
- id: d
  content: |-
    $\mathrm{s/m}$
```

```quiz
type: radio
id: q-4
content: |-
  In circular motion, which expression gives the speed when the radius is $r$ and the angular speed is $\omega$?
options:
- id: a
  content: |-
    $r+\omega$
- id: b
  content: |-
    $\dfrac{r}{\omega}$
- id: c
  content: |-
    $r\omega$
  correct: true
- id: d
  content: |-
    $\dfrac{\omega}{r}$
```

---

<a id="reading-magnitude-statements"></a>
## Reading Magnitude Statements

**Example:** In circular motion, is the vector equation $\vec v=r\omega$ correct?

**Explanation**

No. The velocity $\vec v$ is a vector, but $r\omega$ is a scalar speed. The correct statement is about magnitude:

$$
|\vec v|=r\omega.
$$

This distinction matters in true-or-false questions. The velocity vector points tangent to the circle, while $r\omega$ only gives how large that velocity is.

```quiz
type: radio
id: q-5
content: |-
  In circular motion, which statement is correctly written?
options:
- id: a
  content: |-
    $\vec v=r\omega$
- id: b
  content: |-
    $|\vec v|=r\omega$
  correct: true
- id: c
  content: |-
    $\vec r=\omega v$
- id: d
  content: |-
    $|\vec v|=\dfrac{\omega}{r}$
```

---

<a id="checking-the-true-or-false-claim"></a>
## Checking the True-or-False Claim

**Example:** Consider an object undergoing uniform circular motion. Let $\vec r$ be the position of the object relative to the circle's center, $\vec v$ the velocity, and $\omega$ the angular speed. True or false: $\vec v$ has magnitude $r\omega$.

**Explanation**

The statement asks about the magnitude of $\vec v$, not its direction. In circular motion:

$$
s=r\theta.
$$

Dividing by time gives

$$
\frac{s}{t}=r\frac{\theta}{t}.
$$

The left side is speed, $|\vec v|$. The factor $\theta/t$ is angular speed, $\omega$. Therefore,

$$
|\vec v|=r\omega.
$$

So the statement is true.

```quiz
type: radio
id: q-6
content: |-
  Consider an object undergoing uniform circular motion. Let $\vec r$ be the position of the object relative to the circle's center, $\vec v$ the velocity, and $\omega$ the angular speed.

  True or false: $\vec v$ has magnitude $r\omega$.
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
id: q-7
content: |-
  A point moves in a circle with radius $r$ and angular speed $\omega$. Which statement explains why its speed is $r\omega$?
options:
- id: a
  content: |-
    The distance traveled along the circle is $s=r\theta$, so arc length per time is $r$ times angle per time.
  correct: true
- id: b
  content: |-
    The velocity vector points away from the center, so its magnitude equals the radius times the acceleration.
- id: c
  content: |-
    The angle swept equals the radius divided by time, so speed is $\omega/r$.
- id: d
  content: |-
    The radius changes at rate $\omega$, so multiplying by $r$ gives the acceleration.
```

---

## Summary

When circular motion gives a radius $r$ and angular speed $\omega$, use the radian arc-length relation

$$
s=r\theta.
$$

Turning distance into distance per time gives

$$
|\vec v|=r\omega.
$$

The unit check also points to the same answer:

$$
\mathrm{m}\cdot\frac{\mathrm{rad}}{\mathrm{s}}
=
\frac{\mathrm{m}}{\mathrm{s}}.
$$

The main trap is mixing a vector with a scalar. The velocity $\vec v$ is tangent to the circle, while $r\omega$ is only its magnitude. A statement saying "$\vec v$ has magnitude $r\omega$" is true.

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Tangential Speed From Angular Velocity](<../../2026-06-29-M1-3/Lessons/Problem-2.md>)

<!-- study-guide-nav:end -->
