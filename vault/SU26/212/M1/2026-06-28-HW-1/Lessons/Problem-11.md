# Testing Whether Circular-Motion Acceleration Is Perpendicular to the Radius

<!--
lesson-id: 212-M1-049
topic-code: MTH212.M1.49
-->

## Table of Contents

- [Introduction](#introduction)
- [Separate Radial and Tangential Acceleration](#separate-radial-and-tangential-acceleration)
- [Use the Perpendicular Test](#use-the-perpendicular-test)
- [Handle Non-Uniform Speed](#handle-non-uniform-speed)
- [Check the True-or-False Statement](#check-the-true-or-false-statement)

## Prerequisites

- The position vector $\vec{r}$ points from the circle's center to the object
- Velocity in circular motion is tangent to the circle
- Two nonzero vectors are perpendicular when their dot product is $0$
- Angular speed $\omega$ measures how quickly the object moves around the circle

---

<a id="introduction"></a>
## Introduction

In circular motion, the velocity vector is tangent to the circle, so $\vec{v}$ is perpendicular to $\vec{r}$. That fact is easy to remember, but it does not automatically apply to acceleration.

The recognition cue is a statement asking whether $\vec{a}$ is perpendicular to $\vec{r}$. Use $+\hat{r}$ inward and choose $+\hat{t}$ tangent to the path; the signed component $a_t$ records which tangent direction the acceleration follows. The position vector $\vec{r}$ points outward, opposite $\hat{r}$. The reusable check is:

1. Separate the acceleration into a radial part and a tangential part.
2. Look for any nonzero radial part.
3. If $\vec{a}$ has a nonzero radial part, then $\vec{a}$ is not perpendicular to $\vec{r}$.

Equivalently, use the dot-product test:

$$
\vec{a}\perp\vec{r}
\quad\Longleftrightarrow\quad
\vec{a}\cdot\vec{r}=0.
$$

For circular motion with angular speed $\omega$, the radial part of acceleration points toward the center:

$$
a_r\hat{r}=-\omega^2\vec{r}.
$$

Since $|\vec{r}|=r$, the inward-positive scalar component is $a_r=r\omega^2$.

That radial part is parallel to $\vec{r}$ in the opposite direction, not perpendicular to it. For a moving object with $\omega\ne 0$, this is the part that makes the statement "$\vec{a}$ is perpendicular to $\vec{r}$" fail.

---

<a id="separate-radial-and-tangential-acceleration"></a>
## Separate Radial and Tangential Acceleration

**Example:** An object moves around a circle with changing speed. Which two directions can its acceleration have?

**Explanation**

Circular motion can change the velocity vector in two different ways:

$$
\vec{a}=a_r\hat{r}+a_t\hat{t}.
$$

The radial part points toward the center because the direction of velocity is changing. It is opposite the outward position vector $\vec{r}$:

$$
a_r\hat{r}=-\omega^2\vec{r}.
$$

Thus $a_r=r\omega^2$, while the minus sign in the position-vector form records that $\vec{r}$ points outward.

The tangential part points along the tangent direction because the speed is changing. That tangential part is perpendicular to $\vec{r}$, just like the velocity is.

So in non-uniform circular motion, the net acceleration is not purely tangential. It includes an inward radial component and may also include a tangential component.

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  In non-uniform circular motion, which statement correctly separates the possible directions of $\vec{a}$?
options:
- id: a
  content: |-
    $\vec{a}$ can have an inward radial part and a tangential part.
  correct: true
- id: b
  content: |-
    $\vec{a}$ must point only in the same direction as $\vec{v}$.
- id: c
  content: |-
    $\vec{a}$ must be zero because the object stays on a circle.
- id: d
  content: |-
    $\vec{a}$ must point outward in the same direction as $\vec{r}$.
```

---

<a id="use-the-perpendicular-test"></a>
## Use the Perpendicular Test

**Example:** Suppose an acceleration vector has the form

$$
\vec{a}=-\omega^2\vec{r}+a_t\hat{t},
$$

where $a_t\hat{t}$ is perpendicular to $\vec{r}$. Is $\vec{a}$ perpendicular to $\vec{r}$?

**Explanation**

Use the dot product test. A vector is perpendicular to $\vec{r}$ only if its dot product with $\vec{r}$ is $0$.

Start with

$$
\vec{a}\cdot\vec{r}
=
(-\omega^2\vec{r}+a_t\hat{t})\cdot\vec{r}.
$$

Distribute the dot product:

$$
\vec{a}\cdot\vec{r}
=
-\omega^2(\vec{r}\cdot\vec{r})
+(a_t\hat{t})\cdot\vec{r}.
$$

The tangential part is perpendicular to $\vec{r}$, so

$$
(a_t\hat{t})\cdot\vec{r}=0.
$$

But $\vec{r}\cdot\vec{r}=|\vec{r}|^2$, so

$$
\vec{a}\cdot\vec{r}
=
-\omega^2|\vec{r}|^2.
$$

When $\omega\ne 0$ and $|\vec{r}|\ne 0$, this is not $0$. Therefore $\vec{a}$ is not perpendicular to $\vec{r}$. The tangential piece disappears from this dot product, but the radial piece remains.

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  If $\vec{a}=-\omega^2\vec{r}+a_t\hat{t}$ and $a_t\hat{t}\perp \vec{r}$, what does $\vec{a}\cdot\vec{r}$ equal?
options:
- id: a
  content: |-
    $0$
- id: b
  content: |-
    $-\omega^2|\vec{r}|^2$
  correct: true
- id: c
  content: |-
    $\omega^2|\vec{r}|^2$
- id: d
  content: |-
    $(a_t\hat{t})\cdot\vec{r}$
```

---

<a id="handle-non-uniform-speed"></a>
## Handle Non-Uniform Speed

**Example:** An object speeds up while moving around a circle. A student says, "Since the speed is changing, the acceleration is tangent to the circle, so $\vec{a}\perp\vec{r}$." What is the mistake?

**Explanation**

Changing speed does add tangential acceleration. But it does not remove radial acceleration.

The tangential acceleration accounts for the change in speed:

$$
a_t\hat{t}\perp\vec{r}.
$$

The radial acceleration accounts for the change in direction:

$$
a_r\hat{r}=-\omega^2\vec{r}.
$$

The net acceleration is the sum:

$$
\vec{a}=a_r\hat{r}+a_t\hat{t}.
$$

A sum with a nonzero radial component is not perpendicular to $\vec{r}$, even if one piece of the sum is perpendicular to $\vec{r}$. In other words, "has a perpendicular component" is weaker than "is perpendicular."

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  In non-uniform circular motion, why is it wrong to conclude that $\vec{a}\perp\vec{r}$ just because the speed is changing?
options:
- id: a
  content: |-
    The tangential part is zero whenever the speed changes.
- id: b
  content: |-
    The radial part is still present because the velocity direction is changing.
  correct: true
- id: c
  content: |-
    The position vector $\vec{r}$ is tangent to the circle.
- id: d
  content: |-
    The acceleration vector must always point outward.
```

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  Which conclusion follows from knowing only that the tangential part of acceleration is perpendicular to $\vec{r}$?
options:
- id: a
  content: |-
    The whole acceleration vector must be perpendicular to $\vec{r}$.
- id: b
  content: |-
    The whole acceleration vector is perpendicular to $\vec{r}$ only if there is no radial component.
  correct: true
- id: c
  content: |-
    The radial component must point outward.
- id: d
  content: |-
    The object has uniform circular motion.
```

---

<a id="check-the-true-or-false-statement"></a>
## Check the True-or-False Statement

**Example:** Consider an object undergoing non-uniform circular motion. Let $\vec{r}$ be the position of the object relative to the circle's center, $\vec{v}$ the velocity of the object, $\omega$ the angular speed of the object, and $\vec{a}$ its acceleration.

True or false: $\vec{a}$ is perpendicular to $\vec{r}$.

**Explanation**

The statement is false. The acceleration in non-uniform circular motion has a tangential part, but it also has an inward radial part:

$$
a_r\hat{r}=-\omega^2\vec{r}.
$$

Because that radial part is opposite $\vec{r}$, the net acceleration has a component along $\vec{r}$. A vector with a component along $\vec{r}$ cannot be perpendicular to $\vec{r}$.

The common trap is copying the true statement about velocity:

$$
\vec{v}\perp\vec{r}.
$$

That statement is about velocity, not acceleration.

```quiz
type: radio
id: q-5
shuffle: true
content: |-
  Consider an object undergoing non-uniform circular motion. Let $\vec{r}$ be the position of the object relative to the circle's center, $\vec{v}$ the velocity of the object, $\omega$ the angular speed of the object, and $\vec{a}$ its acceleration.

  True or false: $\vec{a}$ is perpendicular to $\vec{r}$.
options:
- id: a
  content: |-
    True
- id: b
  content: |-
    False
  correct: true
```

```quiz
type: radio
id: q-6
shuffle: true
content: |-
  Which statement gives the best reason that $\vec{a}$ is not perpendicular to $\vec{r}$ in non-uniform circular motion?
options:
- id: a
  content: |-
    $\vec{v}$ is parallel to $\vec{r}$.
- id: b
  content: |-
    The acceleration has an inward radial component in addition to any tangential component.
  correct: true
- id: c
  content: |-
    The position vector $\vec{r}$ points tangent to the circle.
- id: d
  content: |-
    Non-uniform circular motion has no acceleration.
```

---

## Summary

When a problem asks whether circular-motion acceleration is perpendicular to the radius vector, do not use the tangent direction of velocity as a shortcut. Split acceleration into radial and tangential parts:

$$
\vec{a}=-\omega^2\vec{r}+a_t\hat{t}.
$$

The tangential part is perpendicular to $\vec{r}$, but the radial part is opposite $\vec{r}$. Since the net acceleration has a radial component, $\vec{a}$ is not perpendicular to $\vec{r}$. The statement "$\vec{a}$ is perpendicular to $\vec{r}$" is false.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
