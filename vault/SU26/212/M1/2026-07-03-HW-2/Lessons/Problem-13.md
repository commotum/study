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
- [Evaluate the Critical Angle](#evaluate-the-critical-angle)
- [Summary](#summary)

## Prerequisites

- Use $a_r=\dfrac{v^2}{r}$ for circular motion along a path of radius $r$.
- Resolve weight into a radial component when an angle is measured from the vertical.
- Use conservation of mechanical energy when friction is negligible.
- Know that a normal force can push on an object but cannot pull it into the surface.

---

<a id="introduction"></a>
## Introduction

A penguin starts from rest at the top of a spherical igloo of radius $r$ and slides down its right side. With friction neglected, the penguin eventually leaves the surface. At what angle $\theta_{\mathrm{c}}$, measured from the vertical through the top of the igloo, does contact end?

![](<../Source/Images/igloo-slide-diagram.png>)

While the penguin remains on the igloo, the surface pushes outward with a normal force. As the penguin descends, the inward component of gravity decreases while the speed—and therefore the required inward acceleration—increases. The normal force falls until the surface no longer needs to push at all. That instant has $N=0$, but the penguin still has radial acceleration.

No outward force throws the penguin off the igloo. This transfers the same inertia reasoning used for a rider cresting a hill: the penguin tends to continue along its instantaneous tangent while the surface curves away beneath it. Lift-off is the disappearance of the surface's contact push, not the disappearance of acceleration.

The contact condition relates the speed to $\theta_{\mathrm{c}}$. Conservation of energy supplies a second relation for that same speed after the penguin has dropped from the top.

---

<a id="write-the-radial-force-equation"></a>
## Write the Radial Force Equation

**Example:** A penguin slides on the outside of a frictionless spherical igloo of radius $r$. At angle $\theta$ from the vertical, while it is still in contact with the igloo, write the force equation in the radial inward direction.

**Explanation**

Choose radial inward, toward the center of the sphere, as positive. The penguin is moving along a circular path of radius $r$, so

$$
\sum F_r=m a_r=m\dfrac{v^2}{r}.
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

This equation controls only the radial component. Before lift-off, gravity also has a tangential component that changes the penguin's speed, so the motion is nonuniform. At lift-off the acceleration is neither zero nor purely tangential: with $N=0$, gravity still has both radial and tangential components at that angle.

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

<a id="evaluate-the-critical-angle"></a>
## Evaluate the Critical Angle

**Example:** A penguin lying on its belly slides down the right side of a spherical igloo, starting from rest. Neglecting friction, it loses contact at angle $\theta_{\mathrm{c}}$ from the vertical. To two significant figures, what is $\theta_{\mathrm{c}}$?

**Explanation**

The combined force-and-energy result is

$$
\cos\theta_{\mathrm{c}}=\dfrac{2}{3}.
$$

So

$$
\theta_{\mathrm{c}}=\cos^{-1}\left(\dfrac{2}{3}\right)\approx 48.2^\circ.
$$

To two significant figures, the calculator value becomes

$$
\theta_{\mathrm{c}}\approx 48^\circ.
$$

Thus the critical angle is $48^\circ$.

```quiz
type: radio
id: p13-q5-final-answer
shuffle: true
content: |-
  A penguin lying on its belly slides down the right side of a spherical igloo, starting from rest. Neglecting friction, it loses contact at angle $\theta_{\mathrm{c}}$ from the vertical. To two significant figures, what is $\theta_{\mathrm{c}}$?
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

At the instant the penguin loses contact with the frictionless igloo, the normal force is zero. The radial equation is therefore

$$
mg\cos\theta=m\dfrac{v^2}{r}.
$$

Then use energy from the top:

$$
v^2=2gr(1-\cos\theta).
$$

The two equations can be combined because they describe the same instant. At lift-off, the normal force is zero, but the penguin still has inward radial acceleration; setting the radial term to zero would describe neither its motion nor the contact condition.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: End of Quiz 1 Study Guide.

Study guide index: 35/35

---
<!-- lesson-nav:end -->
