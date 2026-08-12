# Resolving Banked-Track Forces Along the Centripetal Direction

<!--
lesson-id: 212-M1-061
topic-code: MTH212.M1.61
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Inward Axis](#choose-the-inward-axis)
- [Resolve the Normal Force](#resolve-the-normal-force)
- [Resolve Friction Pointing Up the Track](#resolve-friction-pointing-up-the-track)
- [Write the Centripetal Force Equation](#write-the-centripetal-force-equation)
- [Summary](#summary)

## Prerequisites

- Use $a_r=\dfrac{v^2}{r}$ for constant-speed circular motion.
- Resolve a tilted vector into perpendicular components using sine and cosine.
- Assign a positive or negative sign from the chosen axis direction.

---

<a id="introduction"></a>
## Introduction

An F1 car travels at constant speed $v$ around a circular track of radius $r$. In the side view, the track is banked at angle $\theta$ from the horizontal and rises away from the center of the circle. The road exerts a normal force of magnitude $N$, while static friction of magnitude $f_s$ points up the track. What equation describes the net force along the inward $r$ direction?

![](<../Source/Images/banked-track-car-diagram.png>)

The car's acceleration points horizontally toward the center, so the radial force components must add to $mv^2/r$. The tilted normal force points partly inward. Friction points up the bank and therefore partly outward, opposite the chosen $r$ direction. Weight is vertical and has no component along this horizontal radial axis.

The trigonometric function gives each component's magnitude; its physical direction gives the sign.

---

<a id="choose-the-inward-axis"></a>
## Choose the Inward Axis

**Example:** A car moves at constant speed $v$ around a circular track of radius $r$. In the side view, the center of the circle is to the left of the car. What should the net force equal along the inward $r$ direction?

**Explanation**

The inward direction is the direction of centripetal acceleration. For constant-speed circular motion,

$$
a_r=\dfrac{v^2}{r}.
$$

So the force equation along the inward direction is

$$
\sum F_r=ma_r=m\dfrac{v^2}{r}.
$$

This axis choice is doing real work. Axes parallel and perpendicular to the bank are legal, but the horizontal circular acceleration would then have components along both axes. Choosing $+r$ horizontally inward puts the full known acceleration $v^2/r$ on one axis, so every sign on the left can be read simply as inward or outward.

This equation uses only the components of real forces along the inward axis. There is no extra force called "centripetal force" to add to the diagram.

```quiz
type: radio
id: p7-q1-axis
shuffle: true
content: |-
  A car moves around a circular track at constant speed $v$. The positive $r$ direction is radially inward. What should $\sum F_r$ equal?
options:
- id: p7-q1-a
  content: |-
    $0$, because the speed is constant
- id: p7-q1-b
  content: |-
    $m\dfrac{v^2}{r}$
  correct: true
- id: p7-q1-c
  content: |-
    $mg$
- id: p7-q1-d
  content: |-
    $mvr$
```

---

<a id="resolve-the-normal-force"></a>
## Resolve the Normal Force

**Example:** A road is banked at angle $\theta$ above the horizontal. The normal force $N$ is perpendicular to the road and leans inward. What is its component along the inward $r$ direction?

**Explanation**

First identify the reference angle for the force you are resolving. Because the road is tilted by $\theta$ from the horizontal, the normal force is tilted by $\theta$ from the vertical.

That means the vertical component is adjacent to the angle:

$$
N_y=N\cos\theta.
$$

The inward horizontal component is opposite that same angle:

$$
N_r=N\sin\theta.
$$

Now attach the sign. The normal force leans toward the center, so $N\sin\theta$ is positive in the $r$ direction.

```quiz
type: radio
id: p7-q2-normal
shuffle: true
content: |-
  A banked road makes angle $\theta$ with the horizontal. The normal force $N$ leans inward. Which term is the normal force's component along the inward $r$ direction?
options:
- id: p7-q2-a
  content: |-
    $N\cos\theta$
- id: p7-q2-b
  content: |-
    $N\sin\theta$
  correct: true
- id: p7-q2-c
  content: |-
    $-N\sin\theta$
- id: p7-q2-d
  content: |-
    $-N\cos\theta$
```

---

<a id="resolve-friction-pointing-up-the-track"></a>
## Resolve Friction Pointing Up the Track

**Example:** On the same banked track, friction has magnitude $f_s$ and points up the track in the side view. What is its component along the inward $r$ direction?

**Explanation**

Friction points along the surface of the road. Since the surface is at angle $\theta$ above the horizontal, its horizontal component is adjacent to the angle, so the magnitude of the horizontal component is

$$
f_s\cos\theta.
$$

That gives the magnitude only. Now attach the sign.

"Up the track" points outward in the side view, away from the center of the circle. The positive $r$ direction points inward, so the friction component along $r$ is negative:

$$
f_{s,r}=-f_s\cos\theta.
$$

The vertical component $f_s\sin\theta$ is useful for the $y$ equation, but it is not the centripetal component.

```quiz
type: radio
id: p7-q3-friction
shuffle: true
content: |-
  A banked road rises outward from the center of the curve. Static friction of magnitude $f_s$ points up the track. If positive $r$ is inward, what is friction's $r$ component?
options:
- id: p7-q3-a
  content: |-
    $+f_s\cos\theta$
- id: p7-q3-b
  content: |-
    $-f_s\cos\theta$
  correct: true
- id: p7-q3-c
  content: |-
    $+f_s\sin\theta$
- id: p7-q3-d
  content: |-
    $-f_s\sin\theta$
```

---

<a id="write-the-centripetal-force-equation"></a>
## Write the Centripetal Force Equation

**Example:** A car of mass $m$ travels at constant speed $v$ around a banked circular track of radius $r$. The normal force has magnitude $N$, and friction of magnitude $f_s$ points up the track. Write the net-force equation along the inward $r$ direction.

**Explanation**

List only the components along the inward $r$ direction:

$$
N_r=+N\sin\theta
$$

and

$$
f_{s,r}=-f_s\cos\theta.
$$

Weight points vertically downward, so it has no component along the horizontal inward direction in this side view.

Therefore,

$$
\sum F_r=N\sin\theta-f_s\cos\theta.
$$

For circular motion at constant speed,

$$
\sum F_r=ma_r=m\dfrac{v^2}{r}.
$$

So the correct equation is

$$
\dfrac{mv^2}{r}=ma_r=\sum F_r=N\sin\theta-f_s\cos\theta.
$$

```quiz
type: radio
id: p7-q4-equation
shuffle: true
content: |-
  The figure below shows an F1 sports car of mass $m$ traversing a circular track banked at angle $\theta$ from the horizontal with constant speed $v$.

  The track has radius $r$ and there is friction between the tires and the track. Assume the friction points up the track in the side-view.

  Which of the following options is the correct equation for the component of the net force along the centripetal $r$ direction, pointing radially inward toward the circle's center?

  Take $N$ to be the magnitude of the normal force on the car and $f_s$ the magnitude of the frictional force.

  ![](<../Source/Images/banked-track-car-diagram.png>)
options:
- id: p7-q4-a
  content: |-
    $\dfrac{mv^2}{r}=ma_r=\sum F_r=N\sin\theta+f_s\cos\theta$
- id: p7-q4-b
  content: |-
    $\dfrac{mv^2}{r}=ma_r=\sum F_r=N\sin\theta-f_s\cos\theta$
  correct: true
- id: p7-q4-c
  content: |-
    $\dfrac{mv^2}{r}=ma_r=\sum F_r=N\cos\theta+f_s\sin\theta$
- id: p7-q4-d
  content: |-
    $\dfrac{mv^2}{r}=ma_r=\sum F_r=N\cos\theta-f_s\sin\theta$
```

---

<a id="summary"></a>
## Summary

For a car moving around a banked track, the net radial force points inward:

$$
\sum F_r=m\dfrac{v^2}{r}.
$$

Then resolve the real forces onto that axis. For each force, find the component magnitude from the reference angle, then choose the sign from the component direction.

For a track banked at angle $\theta$ with friction pointing up the track:

$$
N_r=+N\sin\theta
$$

and

$$
f_{s,r}=-f_s\cos\theta.
$$

The sign on friction is negative because up the track points outward in the side view, opposite the inward centripetal direction. Therefore,

$$
\dfrac{mv^2}{r}=ma_r=\sum F_r=N\sin\theta-f_s\cos\theta.
$$

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Maximum Speed on a Frictional Banked Curve](../../2026-06-30-M1-4/Lessons/Problem-6.md)

Study guide index: 26/35

---
<!-- lesson-nav:end -->
