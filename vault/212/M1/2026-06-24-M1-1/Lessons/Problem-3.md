# Finding Angular Acceleration Direction While Stopping

## Table of Contents

- [Introduction](#introduction)
- [Finding the Angular Velocity Direction](#finding-the-angular-velocity-direction)
- [Reversing Direction When Rotation Stops](#reversing-direction-when-rotation-stops)
- [Checking the Direction With Signs](#checking-the-direction-with-signs)
- [Separating Slowing Down From Speeding Up](#separating-slowing-down-from-speeding-up)

## Prerequisites

- Clockwise and counterclockwise rotation as seen on the page
- The right-hand rule for angular velocity direction
- Angular acceleration as the rate of change of angular velocity

---

<a id="introduction"></a>
## Introduction

The question shows a disk initially spinning counterclockwise and then coming to a stop.

![](<../Source/Images/stopping-disk-rotation-direction.png>)

To choose the direction of angular acceleration, use this rule:

- Find the angular velocity direction with the right-hand rule.
- If the disk is slowing down, angular acceleration points opposite the angular velocity.
- If the disk is speeding up, angular acceleration points in the same direction as the angular velocity.

For the pictured disk, counterclockwise rotation gives angular velocity out of the page. Since the disk stops, its angular acceleration points into the page.

---

<a id="finding-the-angular-velocity-direction"></a>
## Finding the Angular Velocity Direction

**Example:** A disk is viewed from the front and rotates counterclockwise. What is the direction of its angular velocity vector?

**Explanation**

Use the right-hand rule: curl the fingers of your right hand in the direction of the rotation. Your thumb points in the direction of the angular velocity vector.

For counterclockwise rotation as viewed from the front, the thumb points out of the page. Therefore, the angular velocity vector points out of the page.

```quiz
type: radio
id: p3-q1
content: |-
  A wheel is viewed from the front and rotates counterclockwise. What is the direction of its angular velocity vector?
options:
- id: a
  content: |-
    into the page
- id: b
  content: |-
    out of the page
  correct: true
- id: c
  content: |-
    clockwise, because that is the opposite spin direction
- id: d
  content: |-
    counterclockwise, because that is the visible spin direction
```

---

<a id="reversing-direction-when-rotation-stops"></a>
## Reversing Direction When Rotation Stops

**Example:** A disk is rotating counterclockwise and slows uniformly to rest. What is the direction of its angular acceleration?

**Explanation**

Counterclockwise rotation means the angular velocity points out of the page.

Because the disk is slowing to rest, the angular acceleration must reduce that angular velocity. So the angular acceleration points opposite the angular velocity:

$$
\text{out of the page} \quad \longrightarrow \quad \text{angular acceleration into the page}.
$$

```quiz
type: radio
id: p3-q2
content: |-
  A disk is rotating counterclockwise as viewed from the front. It slows uniformly until it stops. What is the direction of its angular acceleration?
options:
- id: a
  content: |-
    into the page
  correct: true
- id: b
  content: |-
    out of the page
- id: c
  content: |-
    counterclockwise, because that is the visible spin direction
- id: d
  content: |-
    zero, because the disk eventually stops
```

---

<a id="checking-the-direction-with-signs"></a>
## Checking the Direction With Signs

**Example:** A disk spins counterclockwise at $12\ \mathrm{rad/s}$ and comes to rest in $26\ \mathrm{s}$. If out of the page is positive, what is the sign of its angular acceleration?

**Explanation**

Since the rotation is counterclockwise, choose

$$
\vec{\omega}_i = 12\ \mathrm{rad/s}.
$$

The disk stops, so

$$
\vec{\omega}_f = 0.
$$

Angular acceleration is

$$
\vec{\alpha}=\frac{\vec{\omega}_f-\vec{\omega}_i}{\Delta t}
=\frac{0-12}{26}.
$$

This is negative. Since out of the page was chosen as positive, a negative angular acceleration points into the page.

The $26\ \mathrm{s}$ affects the magnitude of $\vec{\alpha}$, but not its direction. The direction comes from the sign of $\vec{\omega}_f-\vec{\omega}_i$.

```quiz
type: radio
id: p3-q3
content: |-
  A disk spins counterclockwise at $8\ \mathrm{rad/s}$ and stops in $4\ \mathrm{s}$. If out of the page is positive, what is the sign of its angular acceleration?
options:
- id: a
  content: |-
    positive, so it points out of the page
- id: b
  content: |-
    negative, so it points into the page
  correct: true
- id: c
  content: |-
    zero, because the final angular speed is zero
- id: d
  content: |-
    positive, because the disk originally spins counterclockwise
```

---

<a id="separating-slowing-down-from-speeding-up"></a>
## Separating Slowing Down From Speeding Up

**Example:** A disk is rotating clockwise and slows uniformly to rest. What is the direction of its angular acceleration?

**Explanation**

Clockwise rotation gives angular velocity into the page.

The disk is slowing down, so angular acceleration points opposite the angular velocity. Opposite of into the page is out of the page.

The common trap is to pick the direction of rotation. Angular acceleration does not point with the spin when the disk is stopping; it points against the angular velocity.

```quiz
type: radio
id: p3-q4
content: |-
  A disk is rotating clockwise as viewed from the front. It slows uniformly until it stops. What is the direction of its angular acceleration?
options:
- id: a
  content: |-
    into the page
- id: b
  content: |-
    out of the page
  correct: true
- id: c
  content: |-
    clockwise, because that is the visible spin direction
- id: d
  content: |-
    zero because the disk eventually stops
```

```quiz
type: radio
id: p3-q5
content: |-
  A disk is rotating counterclockwise as viewed from the front and is speeding up. What is the direction of its angular acceleration?
options:
- id: a
  content: |-
    into the page
- id: b
  content: |-
    out of the page
  correct: true
- id: c
  content: |-
    zero because the direction of rotation is not changing
- id: d
  content: |-
    counterclockwise, because that is the visible spin direction
```

---

## Summary

Use the right-hand rule to turn the visible spin direction into the angular velocity direction. Counterclockwise rotation points out of the page, and clockwise rotation points into the page. Then compare the initial and final angular velocity:

- Slowing down: angular acceleration points opposite the angular velocity.
- Speeding up: angular acceleration points in the same direction as the angular velocity.

For the pictured disk, counterclockwise rotation gives angular velocity out of the page, and stopping reverses the acceleration direction to into the page.
