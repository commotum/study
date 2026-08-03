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
- [Answering the True-or-False Claim](#answering-the-true-or-false-claim)

## Prerequisites

- A vector points in the direction of its arrow
- Perpendicular vectors meet at a $90^\circ$ angle
- Opposite vectors lie on the same line but point in opposite directions
- In uniform circular motion, the position vector $\vec r$ is measured from the circle's center to the object

---

<a id="introduction"></a>
## Introduction

In uniform circular motion, the object moves around a circle at constant speed. The speed is constant, but the velocity direction keeps changing, so the object still has acceleration.

The recognition cue is a question comparing $\vec a$ with the radius vector $\vec r$. For uniform circular motion,

$$
\vec a=-\omega^2\vec r.
$$

The factor $\omega^2$ is positive, so $-\omega^2$ is a negative scalar. A negative scalar reverses a vector's direction; it does not turn the vector by $90^\circ$.

So $\vec a$ points opposite $\vec r$. Since opposite directions form a $180^\circ$ angle, not a $90^\circ$ angle, $\vec a$ is not perpendicular to $\vec r$.

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

<a id="answering-the-true-or-false-claim"></a>
## Answering the True-or-False Claim

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

When a uniform circular motion problem asks how $\vec a$ compares with $\vec r$, use

$$
\vec a=-\omega^2\vec r.
$$

The radius vector $\vec r$ points from the center to the object. The acceleration $\vec a$ points from the object back toward the center. Therefore $\vec a$ is opposite $\vec r$, not perpendicular to it.

The sign in $\vec a=-\omega^2\vec r$ is the deciding cue: a negative scalar reverses direction instead of making a right angle.

The main trap is mixing up acceleration with velocity: $\vec v$ is tangent and perpendicular to $\vec r$, but $\vec a$ is inward and opposite $\vec r$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Choosing the Acceleration Direction When Circular Motion Speeds Up](Problem-13.md)

Study guide index: 07/30

---

<!-- lesson-nav:end -->
