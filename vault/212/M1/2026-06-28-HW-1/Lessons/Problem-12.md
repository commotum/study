# Checking Speed From Angular Speed in Non-Uniform Circular Motion

<!--
lesson-id: 212-M1-050
topic-code: MTH212.M1.50
-->

## Table of Contents

- [Introduction](#introduction)
- [Separating Velocity Direction From Speed](#separating-velocity-direction-from-speed)
- [Using Instantaneous Angular Speed](#using-instantaneous-angular-speed)
- [Checking the Units of $r\omega$](#checking-the-units-of-r-omega)
- [Why Non-Uniform Motion Still Uses $r\omega$](#why-non-uniform-motion-still-uses-r-omega)
- [Checking the True-or-False Claim](#checking-the-true-or-false-claim)

## Prerequisites

- A point in circular motion stays a fixed distance $r$ from the center
- The velocity vector $\vec v$ is tangent to the circular path
- The magnitude $|\vec v|$ is the object's speed
- Angular speed $\omega$ measures angle swept per unit time
- For angles measured in radians, arc length satisfies $s=r\theta$
- A radian is a ratio of two lengths, so it does not add a new length unit

---

<a id="introduction"></a>
## Introduction

In non-uniform circular motion, the object still moves on a circle, but its speed may change as time passes. That means $\omega$ may change from one instant to another.

The recognition cue is a statement about the **magnitude** of the velocity vector:

$$
|\vec v| \stackrel{?}{=} r\omega.
$$

The useful check is to read $\omega$ as the angular speed at that same instant. Multiplying the radius by that instantaneous angular speed converts angle per time into arc length per time:

$$
|\vec v|=r\omega.
$$

Use three quick checks:

- $|\vec v|$ and $r\omega$ are both scalar speeds
- $r\omega$ has units of length per time
- non-uniform motion changes the value of $\omega$ over time, not the formula at one instant

The main trap is thinking that this formula only works for uniform circular motion. Uniform motion means $\omega$ stays constant over time. The speed formula itself only connects the speed and angular speed at one instant.

---

<a id="separating-velocity-direction-from-speed"></a>
## Separating Velocity Direction From Speed

**Example:** In circular motion, what is the difference between saying "$\vec v$ is tangent to the circle" and saying "$\vec v$ has magnitude $r\omega$"?

**Explanation**

The velocity vector $\vec v$ includes direction and size. In circular motion, its direction is tangent to the circle.

The magnitude $|\vec v|$ is only the size of that vector, so it is the speed. The expression $r\omega$ is also a scalar speed. So this is a correctly matched statement:

$$
|\vec v|=r\omega.
$$

This would not be a correctly matched vector equation:

$$
\vec v=r\omega.
$$

The left side is a vector, but the right side is only a scalar.

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  Which statement correctly matches the type of quantity on both sides?
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
    $\vec r=r\omega$
- id: d
  content: |-
    $\omega=|\vec v|r$
```

---

<a id="using-instantaneous-angular-speed"></a>
## Using Instantaneous Angular Speed

**Example:** An object moves on a circle of radius $2\ \mathrm{m}$. At one instant, its angular speed is $5\ \mathrm{rad/s}$. What is its speed at that instant?

**Explanation**

Use the speed relation at the instant described:

$$
|\vec v|=r\omega.
$$

Substitute $r=2\ \mathrm{m}$ and $\omega=5\ \mathrm{rad/s}$:

$$
|\vec v|=2(5)=10\ \mathrm{m/s}.
$$

The calculation does not require the angular speed to stay $5\ \mathrm{rad/s}$ forever. It only gives the speed at the instant when $\omega=5\ \mathrm{rad/s}$.

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  An object moves on a circle of radius $4\ \mathrm{m}$. At one instant, its angular speed is $3\ \mathrm{rad/s}$. What is its speed at that instant?
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

<a id="checking-the-units-of-r-omega"></a>
## Checking the Units of $r\omega$

**Example:** If $r$ is measured in meters and $\omega$ is measured in radians per second, what units does $r\omega$ have?

**Explanation**

Substitute the units into the product:

$$
[r\omega]=\mathrm{m}\cdot\frac{\mathrm{rad}}{\mathrm{s}}.
$$

A radian measures arc length divided by radius, so it is a ratio rather than a new length unit. The product has speed units:

$$
\mathrm{m}\cdot\frac{1}{\mathrm{s}}
=
\frac{\mathrm{m}}{\mathrm{s}}.
$$

That matches the meaning of $|\vec v|$.

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  If $r$ is in centimeters and $\omega$ is in radians per second, what units does $r\omega$ have?
options:
- id: a
  content: |-
    $\mathrm{cm/s}$
  correct: true
- id: b
  content: |-
    $\mathrm{s/cm}$
- id: c
  content: |-
    $\mathrm{cm^2/s}$
- id: d
  content: |-
    $\mathrm{rad/cm}$
```

---

<a id="why-non-uniform-motion-still-uses-r-omega"></a>
## Why Non-Uniform Motion Still Uses $r\omega$

**Example:** Suppose an object speeds up while moving around a circle of fixed radius $r$. Why does $|\vec v|=r\omega$ still describe its speed at an instant?

**Explanation**

The arc-length relation is geometric:

$$
s=r\theta.
$$

For a very small time interval, the small arc length is

$$
\Delta s=r\Delta\theta.
$$

Divide by the small time interval:

$$
\frac{\Delta s}{\Delta t}
=
r\frac{\Delta\theta}{\Delta t}.
$$

At an instant, the left side becomes speed $|\vec v|$, and the angular rate becomes $\omega$. Therefore,

$$
|\vec v|=r\omega.
$$

Non-uniform motion changes whether $\omega$ is constant. It does not change the instant-by-instant conversion from angular speed to linear speed.

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  An object moves in non-uniform circular motion with fixed radius $6\ \mathrm{m}$. At a particular instant, $\omega=2\ \mathrm{rad/s}$. Which statement is true at that instant?
options:
- id: a
  content: |-
    The speed is $12\ \mathrm{m/s}$.
  correct: true
- id: b
  content: |-
    The speed cannot be found from $r\omega$ because the motion is non-uniform.
- id: c
  content: |-
    The speed is $\dfrac{1}{3}\ \mathrm{m/s}$.
- id: d
  content: |-
    The speed is $8\ \mathrm{m/s}$.
```

---

<a id="checking-the-true-or-false-claim"></a>
## Checking the True-or-False Claim

**Example:** Consider an object undergoing non-uniform circular motion. Let $\vec r$ be the position of the object relative to the circle's center, $\vec v$ the velocity, and $\omega$ the angular speed. True or false: $\vec v$ has magnitude $r\omega$.

**Explanation**

The statement asks about the magnitude of $\vec v$, so it is asking about speed:

$$
|\vec v|.
$$

In circular motion, angular speed converts to speed by multiplying by the radius:

$$
|\vec v|=r\omega.
$$

The word "non-uniform" tells us the speed or angular speed may be changing. It does not make the instantaneous relation false.

So the statement is true.

```quiz
type: radio
id: q-5
shuffle: true
content: |-
  Consider an object undergoing non-uniform circular motion. Let $\vec r$ be the position of the object relative to the circle's center, $\vec v$ the velocity, and $\omega$ the angular speed.

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
id: q-6
shuffle: true
content: |-
  Why does non-uniform circular motion still satisfy $|\vec v|=r\omega$ at an instant?
options:
- id: a
  content: |-
    Because $s=r\theta$ converts angular change to arc length, and the same conversion works for instantaneous rates.
  correct: true
- id: b
  content: |-
    Because non-uniform circular motion has no tangential acceleration.
- id: c
  content: |-
    Because $\vec v$ points in the same direction as $\vec r$.
- id: d
  content: |-
    Because $\omega$ must be constant whenever the path is circular.
```

---

## Summary

For circular motion, the geometry of the path gives

$$
s=r\theta.
$$

Turning arc length per time into speed gives

$$
|\vec v|=r\omega.
$$

In non-uniform circular motion, $\omega$ may change with time, so use the value of $\omega$ at the instant being discussed. Check the claim by asking whether both sides are scalar speeds, whether the units are length per time, and whether $\omega$ refers to that same instant.

The statement "$\vec v$ has magnitude $r\omega$" is true because it describes the speed, not the full velocity vector.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
