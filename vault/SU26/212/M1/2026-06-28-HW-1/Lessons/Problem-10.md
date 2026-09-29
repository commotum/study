# Identifying Velocity Direction in Non-Uniform Circular Motion

<!--
lesson-id: 212-M1-048
topic-code: MTH212.M1.48
-->

## Table of Contents

- [Introduction](#introduction)
- [Reading the Circular-Motion Cue](#reading-the-circular-motion-cue)
- [Separating Speed Changes From Velocity Direction](#separating-speed-changes-from-velocity-direction)
- [Checking Perpendicularity With Components](#checking-perpendicularity-with-components)
- [Checking the Homework Claim](#checking-the-homework-claim)

## Prerequisites

- A position vector $\vec{r}$ points from the circle's center to the object
- Velocity $\vec{v}$ points in the instantaneous direction of motion
- A tangent line to a circle is perpendicular to the radius at the point of contact
- Non-uniform circular motion means the speed or angular speed can change

---

<a id="introduction"></a>
## Introduction

In circular motion, the object stays on a circular path. The recognition cue is a question about the **direction** of the velocity vector $\vec{v}$ compared with the radius vector $\vec{r}$.

The reusable rule is:

$$
\vec{v} \text{ points tangent to the circle, while } \vec{r} \text{ points radially outward.}
$$

At the point where the object is located, the tangent direction is perpendicular to the radius direction. So for circular motion,

$$
\vec{v} \perp \vec{r}.
$$

The same check can be written with a dot product:

$$
\vec{r} \cdot \vec{v} = 0.
$$

Use this test in order:

1. Check that the path is circular.
2. Identify $\vec{r}$ as the radial direction.
3. Identify $\vec{v}$ as the tangent direction.

This remains true in non-uniform circular motion. Non-uniform motion changes how large $\vec{v}$ is, and it can change the acceleration direction, but the velocity still points along the tangent to the circular path.

---

<a id="reading-the-circular-motion-cue"></a>
## Reading the Circular-Motion Cue

**Example:** An object is on the right side of a circle, so its radius vector $\vec{r}$ points to the right. If the object is moving counterclockwise, what direction does $\vec{v}$ point?

**Explanation**

Velocity points in the direction the object is moving at that instant. On the right side of the circle, counterclockwise motion carries the object upward along the circle.

So $\vec{v}$ points upward. The radius points right, and the tangent points upward, so the two directions are perpendicular.

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  An object is at the top of a circle, so $\vec{r}$ points upward from the center to the object. Which direction could $\vec{v}$ point if the object is moving along the circle?
options:
- id: q1-a
  content: |-
    Upward, in the same direction as $\vec{r}$
- id: q1-b
  content: |-
    Downward, opposite $\vec{r}$
- id: q1-c
  content: |-
    Horizontally, tangent to the circle
  correct: true
- id: q1-d
  content: |-
    Toward the center of the circle
```

---

<a id="separating-speed-changes-from-velocity-direction"></a>
## Separating Speed Changes From Velocity Direction

**Example:** An object moves around a circle and speeds up as it passes through a point. Does speeding up make $\vec{v}$ point partly outward or inward?

**Explanation**

No. The velocity vector gives the instantaneous direction of motion along the path. Since the path is still a circle, that direction is tangent to the circle.

Speeding up means the magnitude $|\vec{v}|$ is increasing. It does not add an inward or outward component to $\vec{v}$, because an inward or outward velocity component would move the object off the circle.

The acceleration is different. In non-uniform circular motion, acceleration can have both:

- a radial part, which changes the direction of $\vec{v}$
- a tangential part, which changes the size of $\vec{v}$

That extra tangential acceleration is why the motion is non-uniform, but the velocity itself is still tangent.

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  In non-uniform circular motion, the object's speed is increasing. What is still true about $\vec{v}$?
options:
- id: q2-a
  content: |-
    $\vec{v}$ points tangent to the circular path.
  correct: true
- id: q2-b
  content: |-
    $\vec{v}$ points toward the center because the object is speeding up.
- id: q2-c
  content: |-
    $\vec{v}$ points outward because the object is speeding up.
- id: q2-d
  content: |-
    $\vec{v}$ must be zero because the motion is not uniform.
```

---

<a id="checking-perpendicularity-with-components"></a>
## Checking Perpendicularity With Components

**Example:** At one instant, an object's radius direction is represented by $\vec{r}=\langle 3,4\rangle$. Which velocity direction would be perpendicular to $\vec{r}$: $\langle 3,4\rangle$ or $\langle 4,-3\rangle$?

**Explanation**

Two vectors are perpendicular when their dot product is zero.

Check $\langle 3,4\rangle$ with itself:

$$
\langle 3,4\rangle \cdot \langle 3,4\rangle
=3(3)+4(4)
=25.
$$

That is not zero, so $\langle 3,4\rangle$ is not perpendicular to $\vec{r}$.

Now check $\langle 4,-3\rangle$:

$$
\langle 3,4\rangle \cdot \langle 4,-3\rangle
=3(4)+4(-3)
=12-12
=0.
$$

So $\langle 4,-3\rangle$ is perpendicular to $\vec{r}$ and could be a tangent velocity direction.

The opposite direction, $\langle -4,3\rangle$, would also be perpendicular. The sign depends on whether the object is moving clockwise or counterclockwise; perpendicularity only checks the right angle.

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  At one instant in circular motion, $\vec{r}=\langle 5,12\rangle$. Which vector is perpendicular to $\vec{r}$ and could point tangent to the circle?
options:
- id: q3-a
  content: |-
    $\langle 5,12\rangle$
- id: q3-b
  content: |-
    $\langle 12,-5\rangle$
  correct: true
- id: q3-c
  content: |-
    $\langle -5,-12\rangle$
- id: q3-d
  content: |-
    $\langle 12,5\rangle$
```

---

<a id="checking-the-homework-claim"></a>
## Checking the Homework Claim

**Example:** Now consider an object undergoing non-uniform circular motion. Let $\vec{r}$ be the position of the object relative to the circle's center, $\vec{v}$ the velocity of the object, $\omega$ the angular speed of the object, and $\vec{a}$ its acceleration.

True or false: $\vec{v}$ is perpendicular to $\vec{r}$.

**Explanation**

The statement is about velocity direction, not acceleration direction.

In circular motion, $\vec{r}$ points from the center to the object. The velocity $\vec{v}$ points tangent to the circle. A radius and tangent at the same point are perpendicular, so

$$
\vec{v} \perp \vec{r}.
$$

The word "non-uniform" does not change that. It only says the speed or angular speed may vary as the object moves.

Therefore, the statement is true.

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  Now consider an object undergoing non-uniform circular motion. Let $\vec{r}$ be the position of the object relative to the circle's center, $\vec{v}$ the velocity of the object, $\omega$ the angular speed of the object, and $\vec{a}$ its acceleration.

  True or false: $\vec{v}$ is perpendicular to $\vec{r}$.
options:
- id: q4-a
  content: |-
    True
  correct: true
- id: q4-b
  content: |-
    False
```

```quiz
type: radio
id: q-5
shuffle: true
content: |-
  Which statement best explains why the answer stays the same for uniform and non-uniform circular motion?
options:
- id: q5-a
  content: |-
    Uniformity controls whether the path is a circle.
- id: q5-b
  content: |-
    The tangent direction comes from the circular path, not from whether the speed is constant.
  correct: true
- id: q5-c
  content: |-
    Non-uniform circular motion has no acceleration.
- id: q5-d
  content: |-
    The velocity points radially outward whenever angular speed changes.
```

---

## Summary

When a problem asks whether $\vec{v}$ is perpendicular to $\vec{r}$ in circular motion, use the path geometry:

$$
\vec{r} \text{ is radial}, \qquad \vec{v} \text{ is tangent}.
$$

A tangent to a circle is perpendicular to the radius at the point of contact, so

$$
\vec{v} \perp \vec{r}.
$$

Equivalently,

$$
\vec{r} \cdot \vec{v}=0.
$$

The main trap is treating "non-uniform" as if it changes the direction of velocity. It does not. Non-uniform circular motion changes the speed and the acceleration structure, but the velocity direction remains tangent to the circle.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
