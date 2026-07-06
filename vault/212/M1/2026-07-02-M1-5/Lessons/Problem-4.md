# Finding Tangential Acceleration in a Vertical Circle

## Table of Contents

- [Introduction](#introduction)
- [Separate Radial and Tangential Forces](#separate-radial-and-tangential-forces)
- [Choose the Tangential Component of Weight](#choose-the-tangential-component-of-weight)
- [Convert Tangential Force to Acceleration](#convert-tangential-force-to-acceleration)
- [Ignore Radial Data and Sign Traps](#ignore-radial-data-and-sign-traps)
- [Summary](#summary)

## Prerequisites

- Resolve a force into components along perpendicular axes.
- Use $\sum F = ma$ along one chosen axis.
- Use sine and cosine for right-triangle components.
- Evaluate trig functions in degree mode and round to the requested precision.

---

<a id="introduction"></a>
## Introduction

When a ball moves in a vertical circle, the radial direction points along the string and the tangential direction is perpendicular to the string. To find tangential acceleration, use only the force components along the tangent.

In this problem, the string tension is radial, so it has no tangential component. Gravity points downward, so its component perpendicular to the string determines the tangential acceleration.

![](<../Source/Images/vertical-circle-ball-string-diagram.png>)

---

<a id="separate-radial-and-tangential-forces"></a>
## Separate Radial and Tangential Forces

**Example:** A ball is attached to a string and moves in a vertical circle. At one instant, the string is not vertical. Which force contributes directly to tangential acceleration: tension, gravity, or both?

**Explanation**

Tension points along the string, which is the radial direction. A radial force changes the radial acceleration, not the tangential acceleration.

Gravity points straight down. Unless the ball is exactly at the top or bottom of the circle, gravity has a component perpendicular to the string. That perpendicular component is the tangential force.

```quiz
type: radio
id: q-p4-1
content: |-
  A ball on a string moves in a vertical circle. The $r$-axis points inward along the string, and the $t$-axis is perpendicular to the string. Which statement correctly identifies the force that can create tangential acceleration?
options:
- id: q-p4-1-a
  content: |-
    Tension creates the tangential acceleration because it is the largest force.
- id: q-p4-1-b
  content: |-
    Tension has zero tangential component, while gravity can have a tangential component.
  correct: true
- id: q-p4-1-c
  content: |-
    Both tension and gravity are entirely radial.
- id: q-p4-1-d
  content: |-
    The string length determines the tangential force directly.
```

---

<a id="choose-the-tangential-component-of-weight"></a>
## Choose the Tangential Component of Weight

**Example:** Suppose the inward radial axis is $\theta$ away from the downward direction of gravity. What is the magnitude of the tangential component of the weight $mg$?

**Explanation**

The weight vector has magnitude $mg$. Since the angle between weight and the inward radial axis is $\theta$, the radial component is adjacent to $\theta$ and the tangential component is opposite $\theta$:

$$
F_r = mg\cos\theta
$$

and

$$
F_t = mg\sin\theta.
$$

So the tangential force magnitude is $mg\sin\theta$.

Use this map before plugging in numbers:

- along the string, adjacent to $\theta$: radial component, $mg\cos\theta$;
- perpendicular to the string, opposite $\theta$: tangential component, $mg\sin\theta$.

```quiz
type: radio
id: q-p4-2
content: |-
  A ball is in a vertical circle. The angle between the weight vector and the inward radial axis is $\theta$. What is the magnitude of the tangential component of the weight?
options:
- id: q-p4-2-a
  content: |-
    $mg\cos\theta$
  feedback: |-
    This is the radial component because it is adjacent to $\theta$.
- id: q-p4-2-b
  content: |-
    $mg\sin\theta$
  correct: true
- id: q-p4-2-c
  content: |-
    $mg\tan\theta$
- id: q-p4-2-d
  content: |-
    $T\sin\theta$
  feedback: |-
    Tension is along the string, so it has no tangential component.
- id: q-p4-2-e
  content: |-
    $\dfrac{mg}{\sin\theta}$
```

---

<a id="convert-tangential-force-to-acceleration"></a>
## Convert Tangential Force to Acceleration

**Example:** If $\theta=20^\circ$, what is the magnitude of the tangential acceleration?

**Explanation**

Apply Newton's second law along the tangential axis:

$$
\sum F_t = ma_t.
$$

The tangential force magnitude is $mg\sin\theta$, so

$$
ma_t = mg\sin\theta.
$$

Cancel $m$:

$$
a_t = g\sin\theta.
$$

For $\theta=20^\circ$,

$$
a_t = 9.8\sin(20^\circ)=3.35\ \mathrm{m}/\mathrm{s}^2.
$$

So the magnitude is about $3.4\ \mathrm{m}/\mathrm{s}^2$.

```quiz
type: radio
id: q-p4-3
content: |-
  A ball is moving in a vertical circle. The angle between the weight vector and the inward radial axis is $20^\circ$. What is the magnitude of the tangential acceleration, rounded to two significant figures?
options:
- id: q-p4-3-a
  content: |-
    $3.4\ \mathrm{m}/\mathrm{s}^2$
  correct: true
- id: q-p4-3-b
  content: |-
    $9.2\ \mathrm{m}/\mathrm{s}^2$
- id: q-p4-3-c
  content: |-
    $4.9\ \mathrm{m}/\mathrm{s}^2$
- id: q-p4-3-d
  content: |-
    $0.34\ \mathrm{m}/\mathrm{s}^2$
- id: q-p4-3-e
  content: |-
    $13\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="ignore-radial-data-and-sign-traps"></a>
## Ignore Radial Data and Sign Traps

**Example:** A ball has $m=0.56\ \mathrm{kg}$, $L=0.88\ \mathrm{m}$, $T=1.2\ \mathrm{N}$, and $\theta=14^\circ$. What is the magnitude of its tangential acceleration?

**Explanation**

The mass cancels when using $\sum F_t=ma_t$. The length $L$ and tension $T$ affect radial motion, not the tangential component in this setup.

Use

$$
a_t = g\sin\theta.
$$

Then

$$
a_t = 9.8\sin(14^\circ)=2.37\ \mathrm{m}/\mathrm{s}^2.
$$

Rounded to two significant figures,

$$
a_t = 2.4\ \mathrm{m}/\mathrm{s}^2.
$$

If a signed tangential axis is specified, the sign depends on whether gravity's tangential component points with or against the positive $t$ direction. This problem asks for magnitude, so report the positive size.

```quiz
type: radio
id: q-p4-4
content: |-
  A ball in a vertical circle has $m=0.75\ \mathrm{kg}$, $L=1.2\ \mathrm{m}$, $T=3.0\ \mathrm{N}$, and $\theta=10^\circ$. What is the magnitude of the tangential acceleration, rounded to two significant figures?
options:
- id: q-p4-4-a
  content: |-
    $1.7\ \mathrm{m}/\mathrm{s}^2$
  correct: true
- id: q-p4-4-b
  content: |-
    $14\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    This uses radial data: $T/m+g\cos\theta$.
- id: q-p4-4-c
  content: |-
    $9.7\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    This is $g\cos\theta$, the gravity component along the radial axis.
- id: q-p4-4-d
  content: |-
    $4.0\ \mathrm{m}/\mathrm{s}^2$
- id: q-p4-4-e
  content: |-
    $12\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="summary"></a>
## Summary

For tangential acceleration in this vertical-circle setup, first separate the forces by direction. Tension is radial, so it does not enter $\sum F_t$. Gravity has tangential component magnitude $mg\sin\theta$ when $\theta$ is the angle between gravity and the inward radial axis.

Then apply Newton's second law along the tangent:

$$
ma_t = mg\sin\theta
$$

so

$$
a_t = g\sin\theta.
$$

The main trap is using the radial expression $T/m+g\cos\theta$ or including $L$. Those belong to radial acceleration, not tangential acceleration.
