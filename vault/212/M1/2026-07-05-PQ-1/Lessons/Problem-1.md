# Comparing Centripetal Acceleration At Fixed Speed

<!--
lesson-id: 212-M1-064
topic-code: MTH212.M1.64
-->

## Table of Contents

- [Introduction](#introduction)
- [Recognize Acceleration In Circular Motion](#recognize-acceleration-in-circular-motion)
- [Compare Radii At The Same Speed](#compare-radii-at-the-same-speed)
- [Translate Smaller Circle To Smaller Radius](#translate-smaller-circle-to-smaller-radius)
- [Compare Radius Changes By Factors](#compare-radius-changes-by-factors)
- [Summary](#summary)

## Prerequisites

- Know that velocity includes direction, not just speed.
- Know that acceleration means a change in velocity.
- Be able to compare fractions with the same numerator.

---

<a id="introduction"></a>
## Introduction

When an object moves in a circle at constant speed, its velocity keeps changing direction. That direction change requires an inward, or centripetal, acceleration.

The cue is a constant speed in a circular path. The useful comparison is

$$
a_c=\frac{v^2}{r}
$$

where $v$ is the speed and $r$ is the radius of the circular path.

To compare accelerations, first decide what stays fixed. If the speed stays the same, then $v^2$ stays the same. Only the radius changes, and radius is in the denominator. That means a smaller circle gives a larger acceleration.

---

<a id="recognize-acceleration-in-circular-motion"></a>
## Recognize Acceleration In Circular Motion

**Example:** A cart moves around a circular track at constant speed. Is its acceleration zero?

**Explanation**

No. The speed is constant, but the velocity is not constant because the direction of motion keeps changing. Acceleration measures change in velocity, so the cart has acceleration even though its speed is not changing.

For circular motion at constant speed, the acceleration points toward the center of the circle.

```quiz
type: radio
id: q-recognize-direction-change
shuffle: true
content: |-
  A ball moves at constant speed around a horizontal circle. Which statement is true?
options:
- id: a
  content: |-
    Its acceleration is zero because its speed is constant.
- id: b
  content: |-
    Its acceleration is nonzero because its velocity changes direction.
  correct: true
- id: c
  content: |-
    Its acceleration points in the direction of motion because the ball is moving.
```

---

<a id="compare-radii-at-the-same-speed"></a>
## Compare Radii At The Same Speed

**Example:** Two objects move at the same constant speed. Object A moves in a circle of radius $2\text{ m}$, and object B moves in a circle of radius $6\text{ m}$. Which object has the larger acceleration?

**Explanation**

Use

$$
a_c=\frac{v^2}{r}
$$

The speed is the same for both objects, so $v^2$ is the same. Only the radius changes. A smaller denominator makes the fraction larger, so object A has the larger acceleration.

```quiz
type: radio
id: q-smaller-radius-larger-acceleration
shuffle: true
content: |-
  Two runners move at the same constant speed around circular tracks. Runner A is on a track with radius $10\text{ m}$, and runner B is on a track with radius $25\text{ m}$. Which runner has the larger centripetal acceleration?
options:
- id: a
  content: |-
    Runner A, because the smaller radius makes $\frac{v^2}{r}$ larger.
  correct: true
- id: b
  content: |-
    Runner B, because the larger radius gives more room to accelerate.
- id: c
  content: |-
    Neither runner, because constant speed means zero acceleration.
```

---

<a id="translate-smaller-circle-to-smaller-radius"></a>
## Translate Smaller Circle To Smaller Radius

**Example:** An object travels at a constant speed in a circular path. If the circle gets smaller while the speed stays the same, what happens to the magnitude of the acceleration?

**Explanation**

Translate "smaller circle" into "smaller radius." Then use the fixed-speed comparison:

$$
a_c=\frac{\text{same }v^2}{\text{smaller }r}
$$

A smaller denominator makes the fraction larger, so the acceleration magnitude increases.

This does not conflict with constant speed. Constant speed means the speed is not changing; it does not mean the velocity direction is constant.

```quiz
type: radio
id: q-constant-speed-smaller-circle
shuffle: true
content: |-
  If an object travels at a constant speed in a circular path, the acceleration of the object is
options:
- id: a
  content: |-
    larger in magnitude for a smaller circle.
  correct: true
- id: b
  content: |-
    smaller in magnitude for a smaller circle.
- id: c
  content: |-
    zero.
```

---

<a id="compare-radius-changes-by-factors"></a>
## Compare Radius Changes By Factors

**Example:** A car goes around two circular tracks at the same speed. Track A has radius $4\text{ m}$, and track B has radius $12\text{ m}$. How does the acceleration on track A compare with the acceleration on track B?

**Explanation**

The speed is the same, so compare only the radii:

$$
a_c=\frac{v^2}{r}
$$

Track A's radius is one-third of track B's radius:

$$
4=\frac{1}{3}\cdot 12
$$

Since the radius is in the denominator, one-third as much radius gives three times as much centripetal acceleration. Track A has the larger acceleration.

```quiz
type: radio
id: q-radius-factor-comparison
shuffle: true
content: |-
  A scooter moves at the same constant speed around two circles. Circle A has radius $5\text{ m}$, and circle B has radius $20\text{ m}$. How does the acceleration in circle A compare with the acceleration in circle B?
options:
- id: a
  content: |-
    It is $4$ times as large.
  correct: true
- id: b
  content: |-
    It is $\frac{1}{4}$ as large.
- id: c
  content: |-
    It is the same because the speed is the same.
- id: d
  content: |-
    It is zero because the speed is constant.
```

---

## Summary

For constant-speed circular motion, look for the radius of the path and use

$$
a_c=\frac{v^2}{r}
$$

Use this checklist:

- Constant speed in a circular path still has acceleration because velocity changes direction.
- The centripetal acceleration magnitude is $a_c=\frac{v^2}{r}$.
- If $v$ is fixed, compare only the radius.
- Smaller radius means larger acceleration because $r$ is in the denominator.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
