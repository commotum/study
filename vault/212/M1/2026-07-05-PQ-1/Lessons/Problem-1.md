# Comparing Centripetal Acceleration At Fixed Speed

## Table of Contents

- [Introduction](#introduction)
- [Recognize Acceleration In Circular Motion](#recognize-acceleration-in-circular-motion)
- [Compare Radii At The Same Speed](#compare-radii-at-the-same-speed)
- [Avoid The Constant-Speed Trap](#avoid-the-constant-speed-trap)
- [Use The Formula With Numbers](#use-the-formula-with-numbers)
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

where $v$ is the speed and $r$ is the radius of the circular path. If the speed stays the same, the radius is in the denominator, so a smaller circle gives a larger acceleration.

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

<a id="avoid-the-constant-speed-trap"></a>
## Avoid The Constant-Speed Trap

**Example:** An object travels at a constant speed in a circular path. If the circle gets smaller while the speed stays the same, what happens to the magnitude of the acceleration?

**Explanation**

Constant speed does not remove centripetal acceleration. It only means there is no tangential acceleration changing the speed.

The centripetal acceleration still has magnitude

$$
a_c=\frac{v^2}{r}
$$

With the same $v$, decreasing $r$ increases $a_c$. So the acceleration is larger in magnitude for a smaller circle.

```quiz
type: radio
id: q-constant-speed-smaller-circle
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

<a id="use-the-formula-with-numbers"></a>
## Use The Formula With Numbers

**Example:** A toy car moves at $4\text{ m/s}$ around a circle of radius $8\text{ m}$. What is the magnitude of its centripetal acceleration?

**Explanation**

Substitute into the formula:

$$
a_c=\frac{v^2}{r}=\frac{(4\text{ m/s})^2}{8\text{ m}}
$$

$$
a_c=\frac{16\text{ m}^2/\text{s}^2}{8\text{ m}}=2\text{ m/s}^2
$$

Squaring the speed is important. Do not divide $v$ by $r$.

```quiz
type: radio
id: q-compute-centripetal-acceleration
content: |-
  A puck moves at $6\text{ m/s}$ around a circle of radius $3\text{ m}$. What is the magnitude of its centripetal acceleration?
options:
- id: a
  content: |-
    $2\text{ m/s}^2$
- id: b
  content: |-
    $12\text{ m/s}^2$
  correct: true
- id: c
  content: |-
    $18\text{ m/s}^2$
- id: d
  content: |-
    $36\text{ m/s}^2$
```

---

## Summary

For constant-speed circular motion, look for the radius of the path and use

$$
a_c=\frac{v^2}{r}
$$

The speed can stay constant while acceleration is nonzero because velocity changes direction. When $v$ is fixed, a smaller $r$ makes $\frac{v^2}{r}$ larger, so the acceleration magnitude is larger for a smaller circle.
