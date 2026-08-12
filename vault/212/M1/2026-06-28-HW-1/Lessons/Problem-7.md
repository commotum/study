# Comparing Centripetal Acceleration with the Radius Vector

<!--
lesson-id: 212-M1-007
topic-code: MTH212.M1.07
-->

## Table of Contents

- [Introduction](#introduction)
- [Reading the Radius Vector](#reading-the-radius-vector)
- [Finding the Acceleration Direction](#finding-the-acceleration-direction)
- [Comparing the Two Directions](#comparing-the-two-directions)
- [Separating Velocity from Acceleration](#separating-velocity-from-acceleration)
- [Decide Whether the Vectors Are Perpendicular](#decide-whether-the-vectors-are-perpendicular)

## Prerequisites

- A vector points in the direction of its arrow
- Perpendicular vectors meet at a $90^\circ$ angle
- Opposite vectors lie on the same line but point in opposite directions
- In uniform circular motion, the position vector $\vec r$ is measured from the circle's center to the object

---

<a id="introduction"></a>
## Introduction

Picture an object at the right edge of a circular path. Its position vector $\vec r$ points from the center toward the object, so it points right. Its centripetal acceleration points back toward the center, so it points left. The two vectors lie on the same line but face opposite directions.

For uniform circular motion, that relationship is written

$$
\vec a=-\omega^2\vec r.
$$

In the cheat sheet's scalar component notation, the same uniform-circular-motion result is $a_r=|\vec a|=\omega^2r$. The vector equation above adds the inward direction through its minus sign.

The positive factor $\omega^2$ sets the acceleration's magnitude, while the minus sign reverses the direction of $\vec r$. It does not turn the vector by $90^\circ$. The angle between $\vec a$ and $\vec r$ is $180^\circ$, so they are opposite rather than perpendicular.

The sign depends on the chosen radial axis. If $\hat r$ points outward, then

$$
\vec a_r=-\frac{v^2}{r}\hat r.
$$

If the positive radial direction is instead chosen inward, the scalar component is $a_r=+v^2/r$. The coordinate sign changes, but the physical acceleration remains directed toward the center.

---

<a id="reading-the-radius-vector"></a>
## Reading the Radius Vector

**Example:** An object is at the rightmost point of a circle, and $\vec r$ is measured from the center to the object. Which way does $\vec r$ point?

**Explanation**

The position vector has its tail at the center and its head at the object. If the object is at the rightmost point, the arrow from the center to the object points right.

So at the rightmost point,

$$
\vec r \text{ points right.}
$$

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  An object is at the top of a circle. The vector $\vec r$ is measured from the center to the object. Which way does $\vec r$ point?
options:
- id: q1-a
  content: |-
    Up
  correct: true
- id: q1-b
  content: |-
    Down
- id: q1-c
  content: |-
    Left
- id: q1-d
  content: |-
    Tangent to the circle
```

---

<a id="finding-the-acceleration-direction"></a>
## Finding the Acceleration Direction

**Example:** The same object is at the rightmost point of a circle and is moving with uniform circular motion. Which way does $\vec a$ point?

**Explanation**

Uniform circular motion has centripetal acceleration. "Centripetal" means toward the center.

At the rightmost point, the center is to the left of the object, so the acceleration points left:

$$
\vec a \text{ points left.}
$$

This matches the formula $\vec a=-\omega^2\vec r$: if $\vec r$ points right, then $\vec a$ points opposite it.

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  An object is at the bottom of a circle and is moving with uniform circular motion. Which way does $\vec a$ point?
options:
- id: q2-a
  content: |-
    Down, away from the center
- id: q2-b
  content: |-
    Up, toward the center
  correct: true
- id: q2-c
  content: |-
    Left, tangent to the circle
- id: q2-d
  content: |-
    Right, tangent to the circle
```

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  Suppose $\vec a=-4\vec r$ and $\vec r$ points left. Which statement correctly describes $\vec a$?
options:
- id: q3-a
  content: |-
    $\vec a$ points right, opposite $\vec r$.
  correct: true
- id: q3-b
  content: |-
    $\vec a$ points left, in the same direction as $\vec r$.
- id: q3-c
  content: |-
    $\vec a$ is perpendicular to $\vec r$ because the coefficient is negative.
- id: q3-d
  content: |-
    The direction of $\vec a$ cannot be determined from the equation.
```

---

<a id="comparing-the-two-directions"></a>
## Comparing the Two Directions

**Example:** At the rightmost point of a circle, $\vec r$ points right and $\vec a$ points left. Are $\vec r$ and $\vec a$ perpendicular?

**Explanation**

Perpendicular vectors meet at a $90^\circ$ angle. These two vectors lie on the same line:

$$
\vec r \text{ points right},
\qquad
\vec a \text{ points left}.
$$

Their angle is $180^\circ$, so they are opposite, not perpendicular.

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  At the top of a circle in uniform circular motion, $\vec r$ points up and $\vec a$ points down. Which description is correct?
options:
- id: q4-a
  content: |-
    They are perpendicular because one vector is radial.
- id: q4-b
  content: |-
    They are opposite because they lie on the same line and point in opposite directions.
  correct: true
- id: q4-c
  content: |-
    They point in the same direction because both are related to the circle.
- id: q4-d
  content: |-
    Their relationship cannot be determined without the speed.
```

---

<a id="separating-velocity-from-acceleration"></a>
## Separating Velocity from Acceleration

**Example:** In uniform circular motion, which vector is perpendicular to $\vec r$: the velocity $\vec v$ or the acceleration $\vec a$?

**Explanation**

The velocity is tangent to the circle. A tangent is perpendicular to the radius at the point of contact, so $\vec v$ is perpendicular to $\vec r$.

The acceleration is different. It points inward toward the center:

$$
\vec v \perp \vec r,
\qquad
\vec a=-\omega^2\vec r.
$$

So the common trap is to remember the tangent velocity fact and apply it to acceleration.

```quiz
type: radio
id: q-5
shuffle: true
content: |-
  In uniform circular motion, which statement correctly separates the directions of $\vec v$ and $\vec a$ relative to $\vec r$?
options:
- id: q5-a
  content: |-
    Both $\vec v$ and $\vec a$ are perpendicular to $\vec r$.
- id: q5-b
  content: |-
    $\vec v$ is perpendicular to $\vec r$, while $\vec a$ points opposite $\vec r$.
  correct: true
- id: q5-c
  content: |-
    $\vec a$ is perpendicular to $\vec r$, while $\vec v$ points opposite $\vec r$.
- id: q5-d
  content: |-
    Neither $\vec v$ nor $\vec a$ has a fixed direction relative to $\vec r$.
```

---

<a id="decide-whether-the-vectors-are-perpendicular"></a>
## Decide Whether the Vectors Are Perpendicular

**Example:** In uniform circular motion, true or false: $\vec a$ is perpendicular to $\vec r$.

**Explanation**

Use the direction rule:

$$
\vec a=-\omega^2\vec r.
$$

That means $\vec a$ points opposite $\vec r$. Opposite vectors are separated by $180^\circ$, so they are not perpendicular.

The statement is false.

```quiz
type: radio
id: q-6
shuffle: true
content: |-
  Consider an object undergoing uniform circular motion. Let $\vec r$ be the position of the object relative to the circle's center, $\vec v$ the velocity of the object, $\omega$ the angular speed of the object, and $\vec a$ its acceleration.

  True or false: $\vec a$ is perpendicular to $\vec r$.
options:
- id: q6-a
  content: |-
    True
- id: q6-b
  content: |-
    False
  correct: true
```

---

## Summary

In uniform circular motion,

$$
\vec a=-\omega^2\vec r.
$$

The radius vector $\vec r$ points from the center to the object. The acceleration $\vec a$ points from the object back toward the center. Therefore $\vec a$ is opposite $\vec r$, not perpendicular to it.

In $\vec a=-\omega^2\vec r$, the negative scalar reverses the direction of $\vec r$ instead of turning it through a right angle.

The main trap is mixing up acceleration with velocity: $\vec v$ is tangent and perpendicular to $\vec r$, but $\vec a$ is inward and opposite $\vec r$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Checking the Magnitude of Centripetal Acceleration](Problem-9.md)

Study guide index: 06/35

---
<!-- lesson-nav:end -->
