# Recognizing Tangential Velocity in Circular Motion

<!--
lesson-id: 212-M1-006
topic-code: MTH212.M1.06
-->

## Table of Contents

- [Introduction](#introduction)
- [Using the Radius and Tangent Directions](#using-the-radius-and-tangent-directions)
- [Checking the Relationship Without Knowing Clockwise or Counterclockwise](#checking-the-relationship-without-knowing-clockwise-or-counterclockwise)
- [Distinguishing Velocity From Acceleration](#distinguishing-velocity-from-acceleration)
- [Write the Vector Relationship](#write-the-vector-relationship)

## Prerequisites

- A radius vector $\vec{r}$ points from the center of a circle to the object
- Instantaneous velocity points in the direction the object is moving at that instant
- A tangent line touches a circle at one point
- A tangent to a circle is perpendicular to the radius at the point of contact

---

<a id="introduction"></a>
## Introduction

Picture a marked point moving around the rim of a wheel. Its position vector $\vec{r}$ starts at the center and points to the mark. Its velocity vector $\vec{v}$ points in the direction the mark is moving at that instant.

That motion is along the tangent to the circular path, while the radius points outward to the same point. A tangent to a circle is perpendicular to the radius at the point of contact, so

$$
\vec{v} \perp \vec{r}.
$$

Uniform speed means the size of $\vec{v}$ stays constant. The direction of $\vec{v}$ still changes from one tangent to the next as the point moves around the wheel.

---

<a id="using-the-radius-and-tangent-directions"></a>
## Using the Radius and Tangent Directions

**Example:** An object is at the rightmost point of a circle. The radius vector $\vec{r}$ points to the right. If the object is moving counterclockwise, what is the direction of $\vec{v}$ relative to $\vec{r}$?

**Explanation**

At the rightmost point, the tangent line is vertical. Counterclockwise motion makes the object move upward at that instant, so $\vec{v}$ points upward.

The radius vector points right, and the velocity vector points up:

$$
\vec{r} \text{ is horizontal},\qquad \vec{v} \text{ is vertical}.
$$

Horizontal and vertical directions are perpendicular, so $\vec{v}$ is perpendicular to $\vec{r}$.

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  An object is at the top of a circle, so $\vec{r}$ points upward from the center. If the object is moving clockwise, what is true about $\vec{v}$?
options:
- id: a
  content: |-
    $\vec{v}$ points tangent to the circle and is perpendicular to $\vec{r}$.
  correct: true
- id: b
  content: |-
    $\vec{v}$ points upward in the same direction as $\vec{r}$.
- id: c
  content: |-
    $\vec{v}$ points downward opposite $\vec{r}$.
- id: d
  content: |-
    $\vec{v}$ points toward the center because the object moves in a circle.
```

---

<a id="checking-the-relationship-without-knowing-clockwise-or-counterclockwise"></a>
## Checking the Relationship Without Knowing Clockwise or Counterclockwise

**Example:** An object moves in uniform circular motion, but the problem does not say whether the motion is clockwise or counterclockwise. Can you still decide whether $\vec{v}$ is perpendicular to $\vec{r}$?

**Explanation**

Clockwise and counterclockwise motion choose opposite tangent directions. At a given point, one direction goes along the tangent one way, and the other goes along the tangent the opposite way.

Both tangent directions are perpendicular to the radius:

$$
\text{clockwise tangent} \perp \vec{r},
\qquad
\text{counterclockwise tangent} \perp \vec{r}.
$$

So the exact direction of $\vec{v}$ may be unknown, but its relationship to $\vec{r}$ is known: $\vec{v}$ is perpendicular to $\vec{r}$.

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  An object moves in uniform circular motion. You are not told whether it moves clockwise or counterclockwise. Which statement is still guaranteed?
options:
- id: a
  content: |-
    $\vec{v}$ points in the same direction as $\vec{r}$.
- id: b
  content: |-
    $\vec{v}$ points opposite $\vec{r}$.
- id: c
  content: |-
    $\vec{v}$ is perpendicular to $\vec{r}$.
  correct: true
- id: d
  content: |-
    $\vec{v}$ has direction zero because the speed is constant.
```

---

<a id="distinguishing-velocity-from-acceleration"></a>
## Distinguishing Velocity From Acceleration

**Example:** In uniform circular motion, which vector points toward the center: velocity $\vec{v}$ or acceleration $\vec{a}$?

**Explanation**

The velocity vector points tangent to the circle. The acceleration vector points inward toward the center because the velocity direction is changing.

A useful direction check is to imagine the inward constraint disappearing at that instant. The object would continue along a straight line tangent to the circle, so that tangent identifies $\vec{v}$; the center-pointing arrow identifies the radial component $a_r$.

That means the two common direction facts are different:

$$
\vec{v} \perp \vec{r},
\qquad
\vec{a} \text{ points opposite } \vec{r}.
$$

The inward vector is acceleration, not velocity.

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  In uniform circular motion, which description correctly matches the vectors?
options:
- id: a
  content: |-
    $\vec{v}$ is tangent to the circle, and $\vec{a}$ points toward the center.
  correct: true
- id: b
  content: |-
    $\vec{v}$ points toward the center, and $\vec{a}$ is tangent to the circle.
- id: c
  content: |-
    Both $\vec{v}$ and $\vec{a}$ point in the same direction as $\vec{r}$.
- id: d
  content: |-
    Both $\vec{v}$ and $\vec{a}$ are zero because the speed is constant.
```

---

<a id="write-the-vector-relationship"></a>
## Write the Vector Relationship

**Example:** An object undergoes uniform circular motion. True or false: $\vec{v}$ is perpendicular to $\vec{r}$.

**Explanation**

Compare the two directions:

- $\vec{r}$ points from the center to the object
- $\vec{v}$ points tangent to the path
- tangent and radius directions are perpendicular

Therefore the statement is true:

$$
\vec{v} \perp \vec{r}.
$$

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  Consider an object undergoing uniform circular motion. Let $\vec{r}$ be the position of the object relative to the circle's center, $\vec{v}$ its velocity, $\omega$ its angular speed, and $\vec{a}$ its acceleration.
  True or false: $\vec{v}$ is perpendicular to $\vec{r}$.
options:
- id: a
  content: |-
    True
  correct: true
- id: b
  content: |-
    False
```

---

## Summary

The radius vector $\vec{r}$ points from the center to the object. The velocity vector $\vec{v}$ points tangent to the circular path. A tangent is perpendicular to the radius at the point of contact, so $\vec{v} \perp \vec{r}$.

The main trap is mixing up velocity with acceleration. In uniform circular motion, $\vec{v}$ is tangent, while $\vec{a}$ points inward toward the center.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Comparing Centripetal Acceleration with the Radius Vector](Problem-7.md)

Study guide index: 05/35

---
<!-- lesson-nav:end -->
