# Writing the Vertical Force Equation on a Banked Track

<!--
lesson-id: 212-M1-060
topic-code: MTH212.M1.60
-->

## Table of Contents

- [Introduction](#introduction)
- [Resolve the Normal Force](#resolve-the-normal-force)
- [Resolve Friction Pointing Up the Track](#resolve-friction-pointing-up-the-track)
- [Use Zero Vertical Acceleration](#use-zero-vertical-acceleration)
- [Avoid Swapping Sine and Cosine](#avoid-swapping-sine-and-cosine)
- [Summary](#summary)

## Prerequisites

- Resolve a vector into horizontal and vertical components.
- Use $\sin\theta$ for the component opposite $\theta$ and $\cos\theta$ for the component adjacent to $\theta$.
- Write Newton's second law in one direction as $\sum F_y=ma_y$.
- Recognize that circular motion on a level-height track has no vertical acceleration.

---

<a id="introduction"></a>
## Introduction

The cue in this problem is a banked track with the $y$-axis pointing vertically upward. The car moves in a horizontal circle, so its acceleration is horizontal toward the center of the track, not vertical.

![](<../Source/Images/banked-track-car-diagram.png>)

Choose the vertical force equation by resolving the normal force and the friction force into their $y$-components, then setting their upward components against the weight.

Here the friction force points up the track in the side view. That makes both the normal force and friction have upward vertical components. The main trap is swapping $\sin\theta$ and $\cos\theta$, or giving friction a negative vertical component even though it points up the track.

Use the same three checks for each force:

1. Which angle is the force measured from?
2. Is the vertical component opposite or adjacent to that angle?
3. Does the vertical component point up or down?

---

<a id="resolve-the-normal-force"></a>
## Resolve the Normal Force

**Example:** A road is banked at angle $\theta$ above the horizontal. A car experiences a normal force of magnitude $n$ perpendicular to the road. What is the vertical component of the normal force?

**Explanation**

The road is tilted $\theta$ away from the horizontal. Since the normal force is perpendicular to the road and the vertical axis is perpendicular to the horizontal, the normal force is tilted $\theta$ away from the vertical.

That means the vertical component is adjacent to $\theta$ in the normal-force triangle:

So the vertical component of the normal force is

$$
n\cos\theta.
$$

The plus sign is important because the normal force points upward as well as sideways.

```quiz
type: radio
id: p6-q1-normal-component
shuffle: true
content: |-
  A car is on a track banked at angle $\theta$. The normal force has magnitude $n$ and points perpendicular to the track. Which expression gives the vertical component of the normal force?
options:
- id: a
  content: |-
    $n\cos\theta$
  correct: true
- id: b
  content: |-
    $n\sin\theta$
- id: c
  content: |-
    $-n\cos\theta$
- id: d
  content: |-
    $-n\sin\theta$
```

---

<a id="resolve-friction-pointing-up-the-track"></a>
## Resolve Friction Pointing Up the Track

**Example:** On the same banked track, friction has magnitude $f$ and points up the track in the side view. What is the vertical component of friction?

**Explanation**

Friction points along the track surface. Since the track is tilted by angle $\theta$ above the horizontal, the friction force is also measured from the horizontal by angle $\theta$.

For a force measured from the horizontal, the vertical component is opposite the angle:

$$
f_y=f\sin\theta.
$$

Because friction points up the track, this vertical component is upward:

$$
+f\sin\theta.
$$

```quiz
type: radio
id: p6-q2-friction-component
shuffle: true
content: |-
  A friction force of magnitude $f$ points up a track banked at angle $\theta$ above the horizontal. Which expression gives the vertical component of friction?
options:
- id: a
  content: |-
    $f\cos\theta$
- id: b
  content: |-
    $f\sin\theta$
  correct: true
- id: c
  content: |-
    $-f\sin\theta$
- id: d
  content: |-
    $-f\cos\theta$
```

---

<a id="use-zero-vertical-acceleration"></a>
## Use Zero Vertical Acceleration

**Example:** A car moves around a horizontal circular track at constant height. The vertical force components are $n\cos\theta$, $f\sin\theta$, and $-mg$. Write the net force equation in the $y$ direction.

**Explanation**

The car is not accelerating upward or downward, so

$$
a_y=0.
$$

Newton's second law in the vertical direction is

$$
\sum F_y=ma_y.
$$

Substitute the vertical components:

$$
n\cos\theta+f\sin\theta-mg=m(0).
$$

So the vertical force equation can be written as

$$
0=ma_y=\sum F_y=n\cos\theta+f\sin\theta-mg.
$$

```quiz
type: radio
id: p6-q3-vertical-equation
shuffle: true
content: |-
  A car on a banked track has upward vertical force components $n\cos\theta$ and $f\sin\theta$, and weight $mg$ downward. If $a_y=0$, which equation matches the vertical direction?
options:
- id: a
  content: |-
    $0=ma_y=\sum F_y=n\cos\theta+f\sin\theta-mg$
  correct: true
- id: b
  content: |-
    $0=ma_y=\sum F_y=n\sin\theta+f\cos\theta-mg$
- id: c
  content: |-
    $0=ma_y=\sum F_y=n\cos\theta-f\sin\theta-mg$
- id: d
  content: |-
    $0=ma_y=\sum F_y=n\sin\theta-f\cos\theta-mg$
```

---

<a id="avoid-swapping-sine-and-cosine"></a>
## Avoid Swapping Sine and Cosine

**Example:** A student writes

$$
0=n\sin\theta+f\cos\theta-mg.
$$

What went wrong?

**Explanation**

The student used the right signs but attached the trigonometric functions to the wrong forces. Check the angle reference for each force separately instead of using the same trig function for both.

For the normal force, the vertical component is adjacent to the bank angle, so it uses cosine:

$$
n_y=n\cos\theta.
$$

For friction pointing along the track, the vertical component is opposite the bank angle, so it uses sine:

$$
f_y=f\sin\theta.
$$

The corrected equation is

$$
0=n\cos\theta+f\sin\theta-mg.
$$

```quiz
type: radio
id: p6-q4-common-trap
shuffle: true
content: |-
  Which mistake produces the expression $n\sin\theta+f\cos\theta-mg$ for the vertical net force on this banked-track car?
options:
- id: a
  content: |-
    It swaps the sine and cosine components for the normal force and friction.
  correct: true
- id: b
  content: |-
    It treats friction as pointing down the track.
- id: c
  content: |-
    It includes a vertical acceleration even though $a_y=0$.
- id: d
  content: |-
    It leaves out the weight of the car.
```

---

## Summary

For a banked-track force equation in the vertical direction, first ask which forces have vertical components. Then decide each component from its own angle reference:

- The normal force is measured from the vertical, so its vertical component is $+n\cos\theta$.
- Friction pointing up the track is measured from the horizontal, so its vertical component is $+f\sin\theta$.
- Weight points downward, so its vertical component is $-mg$.

Because the car's circular acceleration is horizontal, $a_y=0$. Therefore,

$$
0=ma_y=\sum F_y=n\cos\theta+f\sin\theta-mg.
$$

The main trap is using $n\sin\theta$ and $f\cos\theta$. Check each force against the angle it actually makes before choosing sine or cosine.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
