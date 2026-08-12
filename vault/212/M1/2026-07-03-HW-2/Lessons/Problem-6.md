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

An F1 car travels at constant speed $v$ around a circular track of radius $r$. In the side view, the track is banked at angle $\theta$ from the horizontal. The road pushes on the car with normal force $N$, and static friction of magnitude $f_s$ points up the track. With the $y$-axis vertical, what equation describes the net force in the $y$ direction?

![](<../Source/Images/banked-track-car-diagram.png>)

Although the car is accelerating toward the center of the circular track, it stays at the same height. Its vertical acceleration is therefore zero. The upward parts of the normal force and friction must balance the car's weight.

The two contact forces use different reference angles. The normal force is tilted by $\theta$ from the vertical, while friction lies along the track at angle $\theta$ from the horizontal. This is why their vertical components do not use the same trigonometric function.

---

<a id="resolve-the-normal-force"></a>
## Resolve the Normal Force

**Example:** A road is banked at angle $\theta$ above the horizontal. A car experiences a normal force of magnitude $N$ perpendicular to the road. What is the vertical component of the normal force?

**Explanation**

The road is tilted $\theta$ away from the horizontal. Since the normal force is perpendicular to the road and the vertical axis is perpendicular to the horizontal, the normal force is tilted $\theta$ away from the vertical.

The vertical component is adjacent to $\theta$ in the normal-force triangle, so

$$
N\cos\theta.
$$

The plus sign is important because the normal force points upward as well as sideways.

```quiz
type: radio
id: p6-q1-normal-component
shuffle: true
content: |-
  A car is on a track banked at angle $\theta$. The normal force has magnitude $N$ and points perpendicular to the track. Which expression gives the vertical component of the normal force?
options:
- id: a
  content: |-
    $N\cos\theta$
  correct: true
- id: b
  content: |-
    $N\sin\theta$
- id: c
  content: |-
    $-N\cos\theta$
- id: d
  content: |-
    $-N\sin\theta$
```

---

<a id="resolve-friction-pointing-up-the-track"></a>
## Resolve Friction Pointing Up the Track

**Example:** On the same banked track, friction has magnitude $f_s$ and points up the track in the side view. What is the vertical component of friction?

**Explanation**

Friction points along the track surface. Since the track is tilted by angle $\theta$ above the horizontal, the friction force is also measured from the horizontal by angle $\theta$.

For a force measured from the horizontal, the vertical component is opposite the angle:

$$
f_{s,y}=f_s\sin\theta.
$$

Because friction points up the track, this vertical component is upward:

$$
+f_s\sin\theta.
$$

```quiz
type: radio
id: p6-q2-friction-component
shuffle: true
content: |-
  A friction force of magnitude $f_s$ points up a track banked at angle $\theta$ above the horizontal. Which expression gives the vertical component of friction?
options:
- id: a
  content: |-
    $f_s\cos\theta$
- id: b
  content: |-
    $f_s\sin\theta$
  correct: true
- id: c
  content: |-
    $-f_s\sin\theta$
- id: d
  content: |-
    $-f_s\cos\theta$
```

---

<a id="use-zero-vertical-acceleration"></a>
## Use Zero Vertical Acceleration

**Example:** A car moves around a horizontal circular track at constant height. The vertical force components are $N\cos\theta$, $f_s\sin\theta$, and $-mg$. Write the net force equation in the $y$ direction.

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
N\cos\theta+f_s\sin\theta-mg=m(0).
$$

So the vertical force equation can be written as

$$
0=ma_y=\sum F_y=N\cos\theta+f_s\sin\theta-mg.
$$

```quiz
type: radio
id: p6-q3-vertical-equation
shuffle: true
content: |-
  A car on a banked track has upward vertical force components $N\cos\theta$ and $f_s\sin\theta$, and weight $mg$ downward. If $a_y=0$, which equation matches the vertical direction?
options:
- id: a
  content: |-
    $0=ma_y=\sum F_y=N\cos\theta+f_s\sin\theta-mg$
  correct: true
- id: b
  content: |-
    $0=ma_y=\sum F_y=N\sin\theta+f_s\cos\theta-mg$
- id: c
  content: |-
    $0=ma_y=\sum F_y=N\cos\theta-f_s\sin\theta-mg$
- id: d
  content: |-
    $0=ma_y=\sum F_y=N\sin\theta-f_s\cos\theta-mg$
```

---

<a id="avoid-swapping-sine-and-cosine"></a>
## Avoid Swapping Sine and Cosine

**Example:** A student writes

$$
0=N\sin\theta+f_s\cos\theta-mg.
$$

What went wrong?

**Explanation**

The student used the right signs but attached the trigonometric functions to the wrong forces. Check the angle reference for each force separately instead of using the same trig function for both.

A reliable construction is to draw each component triangle with its legs parallel to the chosen $y$ and $r$ axes. If a proposed triangle side is not parallel to the axis whose component you want, it is not that component. Then choose sine or cosine from the angle between the force and that axis, and assign the sign from the arrow's physical direction.

For the normal force, the vertical component is adjacent to the bank angle, so it uses cosine:

$$
N_y=N\cos\theta.
$$

For friction pointing along the track, the vertical component is opposite the bank angle, so it uses sine:

$$
f_{s,y}=f_s\sin\theta.
$$

The corrected equation is

$$
0=N\cos\theta+f_s\sin\theta-mg.
$$

```quiz
type: radio
id: p6-q4-common-trap
shuffle: true
content: |-
  Which mistake produces the expression $N\sin\theta+f_s\cos\theta-mg$ for the vertical net force on this banked-track car?
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

- The normal force is measured from the vertical, so its vertical component is $+N\cos\theta$.
- Friction pointing up the track is measured from the horizontal, so its vertical component is $+f_s\sin\theta$.
- Weight points downward, so its vertical component is $-mg$.

Because the car's circular acceleration is horizontal, $a_y=0$. Therefore,

$$
0=ma_y=\sum F_y=N\cos\theta+f_s\sin\theta-mg.
$$

The expression $N\sin\theta+f_s\cos\theta$ swaps the two components. Each trigonometric function must follow the angle its force actually makes.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Resolving Banked-Track Forces Along the Centripetal Direction](Problem-7.md)

Study guide index: 25/35

---
<!-- lesson-nav:end -->
