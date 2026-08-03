# Finding the Critical Angle Where a Slider Leaves a Sphere

<!--
lesson-id: 212-M1-030
topic-code: MTH212.M1.30
-->

## Table of Contents

- [Introduction](#introduction)
- [Write the Radial Force Equation](#write-the-radial-force-equation)
- [Set the Normal Force to Zero at Lift-Off](#set-the-normal-force-to-zero-at-lift-off)
- [Use Energy to Find the Speed at an Angle](#use-energy-to-find-the-speed-at-an-angle)
- [Combine the Two Equations](#combine-the-two-equations)
- [Match the Critical Angle to the Choices](#match-the-critical-angle-to-the-choices)
- [Summary](#summary)

## Prerequisites

- Use $a_r=\dfrac{v^2}{r}$ for circular motion along a path of radius $r$.
- Resolve weight into a radial component when an angle is measured from the vertical.
- Use conservation of mechanical energy when friction is negligible.
- Know that a normal force can push on an object but cannot pull it into the surface.

---

<a id="introduction"></a>
## Introduction

The cue in this problem is an object sliding without friction on the outside of a sphere, then losing contact with the surface. The useful move is to solve for the angle by combining two equations that describe the same instant:

1. A radial force equation, because losing contact is a force condition.
2. An energy equation, because the speed changes as the object drops in height.

For the igloo problem, the angle $\theta$ is measured from the vertical through the top of the sphere.

![](<../Source/Images/igloo-slide-diagram.png>)

At the critical angle, the surface is just about to stop pushing on the penguin. That means $N=0$, not that the radial acceleration is zero. The target variable is $\theta_c$, and the algebra will eventually reduce to solving for $\cos\theta_c$.

---

<a id="write-the-radial-force-equation"></a>
## Write the Radial Force Equation

**Example:** A penguin slides on the outside of a frictionless spherical igloo of radius $r$. At angle $\theta$ from the vertical, while it is still in contact with the igloo, write the force equation in the radial inward direction.

**Explanation**

Choose radial inward, toward the center of the sphere, as positive. The penguin is moving along a circular path of radius $r$, so

$$
\sum F_r=m\dfrac{v^2}{r}.
$$

Weight points straight down. At angle $\theta$ from the vertical, the inward radial component of weight is

$$
mg\cos\theta.
$$

The normal force points outward from the surface, opposite the inward direction, so its radial contribution is $-N$.

Therefore the radial force equation is

$$
mg\cos\theta-N=m\dfrac{v^2}{r}.
$$

The main sign check is that the normal force subtracts because the igloo pushes outward, away from the center.

```quiz
type: radio
id: p13-q1-radial-equation
shuffle: true
content: |-
  A penguin slides on the outside of a frictionless sphere of radius $r$. At angle $\theta$ from the vertical, it is still in contact with the surface. If radial inward is positive, which equation is correct?
options:
- id: p13-q1-a
  content: |-
    $mg\cos\theta-N=m\dfrac{v^2}{r}$
  correct: true
- id: p13-q1-b
  content: |-
    $N-mg\cos\theta=m\dfrac{v^2}{r}$
- id: p13-q1-c
  content: |-
    $mg\sin\theta-N=m\dfrac{v^2}{r}$
- id: p13-q1-d
  content: |-
    $mg+N=m\dfrac{v^2}{r}$
```

---

<a id="set-the-normal-force-to-zero-at-lift-off"></a>
## Set the Normal Force to Zero at Lift-Off

**Example:** At the instant the penguin is just about to lose contact with the igloo, what does the radial force equation become?

**Explanation**

The surface can push outward on the penguin, but it cannot pull the penguin inward. Losing contact happens at the boundary where the normal force has dropped to zero:

$$
N=0.
$$

Start with the radial equation:

$$
mg\cos\theta-N=m\dfrac{v^2}{r}.
$$

Substitute $N=0$:

$$
mg\cos\theta=m\dfrac{v^2}{r}.
$$

Cancel $m$ and multiply by $r$:

$$
v^2=gr\cos\theta.
$$

This is only the contact condition. It does not yet tell you the angle because the speed $v$ also depends on how far the penguin has slid down. Keep it as one expression for $v^2$:

$$
v^2=gr\cos\theta.
$$

```quiz
type: radio
id: p13-q2-contact-condition
shuffle: true
content: |-
  At the instant a slider loses contact with the outside of a frictionless sphere, what condition should be used in the radial force equation?
options:
- id: p13-q2-a
  content: |-
    $N=0$
  correct: true
- id: p13-q2-b
  content: |-
    $m\dfrac{v^2}{r}=0$
- id: p13-q2-c
  content: |-
    $mg\cos\theta=0$
- id: p13-q2-d
  content: |-
    $v=0$
```

---

<a id="use-energy-to-find-the-speed-at-an-angle"></a>
## Use Energy to Find the Speed at an Angle

**Example:** The penguin starts from rest at the top of the igloo. If it has slid to angle $\theta$ from the vertical, find $v^2$ using conservation of mechanical energy.

**Explanation**

The penguin starts from rest, so the kinetic energy at the top is zero. At angle $\theta$, its vertical height above the center of the sphere is $r\cos\theta$ instead of $r$.

So the height drop is

$$
\Delta h=r-r\cos\theta=r(1-\cos\theta).
$$

With friction neglected, lost gravitational potential energy becomes kinetic energy:

$$
mg\,r(1-\cos\theta)=\dfrac{1}{2}mv^2.
$$

Cancel $m$ and multiply by $2$:

$$
v^2=2gr(1-\cos\theta).
$$

The normal force does not appear in the energy equation because it is perpendicular to the motion along the surface while the penguin is still sliding on the igloo.

```quiz
type: radio
id: p13-q3-energy-speed
shuffle: true
content: |-
  A slider starts from rest at the top of a frictionless sphere of radius $r$. At angle $\theta$ from the vertical, what does energy conservation give for $v^2$?
options:
- id: p13-q3-a
  content: |-
    $2gr(1-\cos\theta)$
  correct: true
- id: p13-q3-b
  content: |-
    $gr\cos\theta$
- id: p13-q3-c
  content: |-
    $2gr\cos\theta$
- id: p13-q3-d
  content: |-
    $gr(1-\sin\theta)$
```

---

<a id="combine-the-two-equations"></a>
## Combine the Two Equations

**Example:** Use the contact condition and the energy equation to solve for the critical angle.

**Explanation**

At the critical angle, the contact condition gives

$$
v^2=gr\cos\theta.
$$

Energy gives

$$
v^2=2gr(1-\cos\theta).
$$

Both expressions equal the same $v^2$ at the same angle, so set them equal:

$$
gr\cos\theta=2gr(1-\cos\theta).
$$

Cancel $gr$. This is why the final angle does not depend on the penguin's mass, the igloo radius, or the value of $g$:

$$
\cos\theta=2(1-\cos\theta).
$$

Now solve. If the algebra looks crowded, treat $\cos\theta$ as the unknown quantity:

$$
\cos\theta=2-2\cos\theta
$$

$$
3\cos\theta=2
$$

$$
\cos\theta=\dfrac{2}{3}.
$$

Therefore

$$
\theta=\cos^{-1}\left(\dfrac{2}{3}\right)\approx 48.2^\circ.
$$

```quiz
type: radio
id: p13-q4-combine
shuffle: true
content: |-
  At the critical angle for a frictionless slider leaving the outside of a sphere, the two speed equations are $v^2=gr\cos\theta$ and $v^2=2gr(1-\cos\theta)$. What equation for $\cos\theta$ follows?
options:
- id: p13-q4-a
  content: |-
    $\cos\theta=\dfrac{2}{3}$
  correct: true
- id: p13-q4-b
  content: |-
    $\cos\theta=\dfrac{1}{2}$
- id: p13-q4-c
  content: |-
    $\cos\theta=\dfrac{3}{2}$
- id: p13-q4-d
  content: |-
    $\cos\theta=\dfrac{1}{3}$
```

---

<a id="match-the-critical-angle-to-the-choices"></a>
## Match the Critical Angle to the Choices

**Example:** A penguin lying on its belly slides down the right side of a spherical igloo, starting from rest. Neglecting friction, it loses contact at angle $\theta_c$ from the vertical. To two significant figures, what is $\theta_c$?

**Explanation**

The combined force-and-energy result is

$$
\cos\theta_c=\dfrac{2}{3}.
$$

So

$$
\theta_c=\cos^{-1}\left(\dfrac{2}{3}\right)\approx 48.2^\circ.
$$

Since the answer choices are given as whole degrees, round the calculator value to two significant figures:

$$
\theta_c\approx 48^\circ.
$$

Among the given choices, the matching answer is $48^\circ$.

```quiz
type: radio
id: p13-q5-final-answer
shuffle: true
content: |-
  A penguin lying on its belly slides down the right side of a spherical igloo, starting from rest. Neglecting friction, it loses contact at angle $\theta_c$ from the vertical. To two significant figures, what is $\theta_c$?
options:
- id: p13-q5-a
  content: |-
    $39^\circ$
- id: p13-q5-b
  content: |-
    $42^\circ$
- id: p13-q5-c
  content: |-
    $44^\circ$
- id: p13-q5-d
  content: |-
    $48^\circ$
  correct: true
- id: p13-q5-e
  content: |-
    $51^\circ$
```

---

## Summary

For an object sliding without friction on the outside of a sphere, the cue is "loses contact." Use the radial force equation and set $N=0$ at the critical angle:

$$
mg\cos\theta=m\dfrac{v^2}{r}.
$$

Then use energy from the top:

$$
v^2=2gr(1-\cos\theta).
$$

Combine the two equations only after they describe the same instant. The main trap is setting the centripetal term to zero; at lift-off, the normal force is zero, but the object still has inward radial acceleration.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: End of Quiz 1 Study Guide.

Study guide index: 30/30

---
<!-- lesson-nav:end -->
