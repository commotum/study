# Resolving Banked-Track Forces Along the Centripetal Direction

## Table of Contents

- [Introduction](#introduction)
- [Choose the Inward Axis](#choose-the-inward-axis)
- [Resolve the Normal Force](#resolve-the-normal-force)
- [Resolve Friction Pointing Up the Track](#resolve-friction-pointing-up-the-track)
- [Write the Centripetal Force Equation](#write-the-centripetal-force-equation)
- [Summary](#summary)

## Prerequisites

- Use $a_c=\dfrac{v^2}{r}$ for constant-speed circular motion.
- Resolve a tilted vector into perpendicular components using sine and cosine.
- Assign a positive or negative sign from the chosen axis direction.

---

<a id="introduction"></a>
## Introduction

The cue in this problem is a car moving around a banked circular track, with the $c$ direction defined as radially inward toward the center of the circle. The task is to determine the component of the net force along that inward direction.

The useful move is to resolve each real force into its inward component and then attach the sign. Keep those as two separate checks:

1. Which side of the component triangle is along the $c$ direction?
2. Does that component point with positive $c$ or against it?

The normal force has an inward component $n\sin\theta$. Friction points up the track in the side view, so its horizontal component points away from the center, opposite the positive $c$ direction. That gives a contribution of $-f\cos\theta$.

The main trap is treating every horizontal-looking component as positive. The sign comes from the direction of the component, not from whether the force exists.

---

<a id="choose-the-inward-axis"></a>
## Choose the Inward Axis

**Example:** A car moves at constant speed $v$ around a circular track of radius $r$. In the side view, the center of the circle is to the left of the car. What should the net force equal along the inward $c$ direction?

**Explanation**

The inward direction is the direction of centripetal acceleration. For constant-speed circular motion,

$$
a_c=\dfrac{v^2}{r}.
$$

So the force equation along the inward direction is

$$
\sum F_c=ma_c=m\dfrac{v^2}{r}.
$$

This equation uses only the components of real forces along the inward axis. There is no extra force called "centripetal force" to add to the diagram.

```quiz
type: radio
id: p7-q1-axis
shuffle: true
content: |-
  A car moves around a circular track at constant speed $v$. The positive $c$ direction is radially inward. What should $\sum F_c$ equal?
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

**Example:** A road is banked at angle $\theta$ above the horizontal. The normal force $n$ is perpendicular to the road and leans inward. What is its component along the inward $c$ direction?

**Explanation**

First identify the reference angle for the force you are resolving. Because the road is tilted by $\theta$ from the horizontal, the normal force is tilted by $\theta$ from the vertical.

That means the vertical component is adjacent to the angle:

$$
n_y=n\cos\theta.
$$

The inward horizontal component is opposite that same angle:

$$
n_c=n\sin\theta.
$$

Now attach the sign. The normal force leans toward the center, so $n\sin\theta$ is positive in the $c$ direction.

```quiz
type: radio
id: p7-q2-normal
shuffle: true
content: |-
  A banked road makes angle $\theta$ with the horizontal. The normal force $n$ leans inward. Which term is the normal force's component along the inward $c$ direction?
options:
- id: p7-q2-a
  content: |-
    $n\cos\theta$
- id: p7-q2-b
  content: |-
    $n\sin\theta$
  correct: true
- id: p7-q2-c
  content: |-
    $-n\sin\theta$
- id: p7-q2-d
  content: |-
    $-n\cos\theta$
```

---

<a id="resolve-friction-pointing-up-the-track"></a>
## Resolve Friction Pointing Up the Track

**Example:** On the same banked track, friction has magnitude $f$ and points up the track in the side view. What is its component along the inward $c$ direction?

**Explanation**

Friction points along the surface of the road. Since the surface is at angle $\theta$ above the horizontal, its horizontal component is adjacent to the angle, so the magnitude of the horizontal component is

$$
f\cos\theta.
$$

That gives the magnitude only. Now attach the sign.

"Up the track" points outward in the side view, away from the center of the circle. The positive $c$ direction points inward, so the friction component along $c$ is negative:

$$
f_c=-f\cos\theta.
$$

The vertical component $f\sin\theta$ is useful for the $y$ equation, but it is not the centripetal component.

```quiz
type: radio
id: p7-q3-friction
shuffle: true
content: |-
  A banked road rises outward from the center of the curve. Static friction of magnitude $f$ points up the track. If positive $c$ is inward, what is friction's $c$ component?
options:
- id: p7-q3-a
  content: |-
    $+f\cos\theta$
- id: p7-q3-b
  content: |-
    $-f\cos\theta$
  correct: true
- id: p7-q3-c
  content: |-
    $+f\sin\theta$
- id: p7-q3-d
  content: |-
    $-f\sin\theta$
```

---

<a id="write-the-centripetal-force-equation"></a>
## Write the Centripetal Force Equation

**Example:** A car of mass $m$ travels at constant speed $v$ around a banked circular track of radius $r$. The normal force has magnitude $n$, and friction of magnitude $f$ points up the track. Write the net-force equation along the inward $c$ direction.

![](<../Source/Images/banked-track-car-diagram.png>)

**Explanation**

List only the components along the inward $c$ direction:

$$
n_c=+n\sin\theta
$$

and

$$
f_c=-f\cos\theta.
$$

Weight points vertically downward, so it has no component along the horizontal inward direction in this side view.

Therefore,

$$
\sum F_c=n\sin\theta-f\cos\theta.
$$

For circular motion at constant speed,

$$
\sum F_c=ma_c=m\dfrac{v^2}{r}.
$$

So the correct equation is

$$
\dfrac{mv^2}{r}=ma_c=\sum F_c=n\sin\theta-f\cos\theta.
$$

```quiz
type: radio
id: p7-q4-equation
shuffle: true
content: |-
  The figure below shows an F1 sports car of mass $m$ traversing a circular track banked at angle $\theta$ from the horizontal with constant speed $v$.

  The track has radius $r$ and there is friction between the tires and the track. Assume the friction points up the track in the side-view.

  Which of the following options is the correct equation for the component of the net force along the centripetal $c$ direction, pointing radially inward toward the circle's center?

  Take $n$ to be the magnitude of the normal force on the car and $f$ the magnitude of the frictional force.

  ![](<../Source/Images/banked-track-car-diagram.png>)
options:
- id: p7-q4-a
  content: |-
    $\dfrac{mv^2}{r}=ma_c=\sum F_c=n\sin\theta+f\cos\theta$
- id: p7-q4-b
  content: |-
    $\dfrac{mv^2}{r}=ma_c=\sum F_c=n\sin\theta-f\cos\theta$
  correct: true
- id: p7-q4-c
  content: |-
    $\dfrac{mv^2}{r}=ma_c=\sum F_c=n\cos\theta+f\sin\theta$
- id: p7-q4-d
  content: |-
    $\dfrac{mv^2}{r}=ma_c=\sum F_c=n\cos\theta-f\sin\theta$
```

---

<a id="summary"></a>
## Summary

When a banked-track problem asks for the net force along the centripetal direction, use the inward axis:

$$
\sum F_c=m\dfrac{v^2}{r}.
$$

Then resolve the real forces onto that axis. For each force, find the component magnitude from the reference angle, then choose the sign from the component direction.

For a track banked at angle $\theta$ with friction pointing up the track:

$$
n_c=+n\sin\theta
$$

and

$$
f_c=-f\cos\theta.
$$

The sign on friction is negative because up the track points outward in the side view, opposite the inward centripetal direction. Therefore,

$$
\dfrac{mv^2}{r}=ma_c=\sum F_c=n\sin\theta-f\cos\theta.
$$
