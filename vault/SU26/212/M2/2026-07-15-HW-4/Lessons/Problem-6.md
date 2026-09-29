# Balancing a Rod and Sphere About a Support

<!--
lesson-id: 212-M2-042
topic-code: MTH212.M2.42
-->

## Table of Contents

- [Introduction](#introduction)
- [Locate Each Weight](#locate-each-weight)
- [Measure Lever Arms From the Support](#measure-lever-arms-from-the-support)
- [Balance the Opposing Torques](#balance-the-opposing-torques)
- [Solve and Verify the Balance Equation](#solve-and-verify-the-balance-equation)
- [Apply the Method to the Rod and Sphere](#apply-the-method-to-the-rod-and-sphere)
- [Summary](#summary)

## Prerequisites

- The weight of an object of mass $M$ is $Mg$.
- A uniform rod's center of mass is at its midpoint.
- The magnitude of a torque is $\tau=r_\perp F$.
- Static equilibrium requires $\sum \tau=0$.

---

<a id="introduction"></a>
## Introduction

When a horizontal system rests on one support and the question asks where that support must be placed, take torques about the support. The support force then has zero lever arm and produces no torque.

**Recognition cue:** The objects remain at rest while their weights act on opposite sides of a support. Locate each object's center of mass, measure each lever arm from the support, and set the clockwise and counterclockwise torque magnitudes equal.

For a rod of length $L$ supported a distance $d$ from its left end, the important positions measured from the left end are

$$
x_{\mathrm{left object}}=0, \qquad x_{\mathrm{support}}=d, \qquad x_{\mathrm{rod}}=\frac{L}{2}.
$$

---

<a id="locate-each-weight"></a>
## Locate Each Weight

**Example:** A point object is attached at the left end of a uniform rod of length $L$. The support is between the left end and the rod's midpoint. Where do the two weights act?

**Explanation**

The attached object's weight acts at the left end, $x=0$. The rod's distributed weight can be replaced by one force acting at the rod's center of mass, $x=L/2$.

Do not place the rod's entire weight at an endpoint or at the support. Uniformity is the cue that its center of mass is exactly at the midpoint.

```quiz
type: radio
id: p6-locate-weight
content: |-
  A uniform rod extends from $x=0$ to $x=L$. At what coordinate does the rod's weight act?
options:
- id: p6-locate-weight-a
  content: |-
    $x=0$
- id: p6-locate-weight-b
  content: |-
    $x=\dfrac{L}{2}$
  correct: true
- id: p6-locate-weight-c
  content: |-
    $x=d$
- id: p6-locate-weight-d
  content: |-
    $x=L$
```

---

<a id="measure-lever-arms-from-the-support"></a>
## Measure Lever Arms From the Support

**Example:** The support is at $x=d$, with $0<d<L/2$. Find the lever arms of the object at the left end and of the uniform rod.

**Explanation**

A lever arm is the distance from the pivot to the force's line of action. Therefore,

$$
r_{\mathrm{left object}}=d-0=d,
$$

and

$$
r_{\mathrm{rod}}=\frac{L}{2}-d.
$$

The quantity $L/2$ is the rod center's coordinate, not its distance from the support. Subtract the support coordinate $d$.

A short position ledger keeps the coordinates and lever arms separate:

| Object | Position from left end | Lever arm about support |
|---|---:|---:|
| Left object | $0$ | $d$ |
| Uniform rod | $L/2$ | $L/2-d$ |

```quiz
type: radio
id: p6-lever-arm
content: |-
  A uniform rod of length $L$ is supported a distance $d$ from its left end, where $d<L/2$. What is the lever arm of the rod's weight about the support?
options:
- id: p6-lever-arm-a
  content: |-
    $d$
- id: p6-lever-arm-b
  content: |-
    $\dfrac{L}{2}$
- id: p6-lever-arm-c
  content: |-
    $\dfrac{L}{2}-d$
  correct: true
- id: p6-lever-arm-d
  content: |-
    $L-d$
```

---

<a id="balance-the-opposing-torques"></a>
## Balance the Opposing Torques

**Example:** An object of mass $M$ sits at the left end of a uniform rod of mass $2M$. The support is a distance $d$ from that end and lies left of the rod's midpoint. Write the torque-balance equation.

**Explanation**

The left object's weight produces torque in one direction, while the rod's weight produces torque in the other. Equate their magnitudes:

$$
(\text{left mass})g(\text{left arm})
=
(\text{rod mass})g(\text{rod arm}).
$$

Substituting the mass and lever arm for each side gives

$$
(Mg)d=(2Mg)\left(\frac{L}{2}-d\right).
$$

The common factor $g$ cancels. Torque balance depends on each mass multiplied by its own lever arm.

```quiz
type: radio
id: p6-torque-equation
content: |-
  An object of mass $3M$ is at the left end of a uniform rod of mass $M$. A support at distance $d<L/2$ holds the system in equilibrium. Which equation correctly balances torques about the support?
options:
- id: p6-torque-equation-a
  content: |-
    $3Mg\,d=Mg\left(\dfrac{L}{2}-d\right)$
  correct: true
- id: p6-torque-equation-b
  content: |-
    $3Mg\left(\dfrac{L}{2}-d\right)=Mg\,d$
- id: p6-torque-equation-c
  content: |-
    $3Mg\,d=Mg\dfrac{L}{2}$
- id: p6-torque-equation-d
  content: |-
    $3Mg(L-d)=Mg\dfrac{L}{2}$
```

---

<a id="solve-and-verify-the-balance-equation"></a>
## Solve and Verify the Balance Equation

**Example:** A mass $m/2$ is at the left end of a uniform rod of mass $m$. Find the equilibrium support distance $d$.

**Explanation**

Balance the torques:

$$
\left(\frac{m}{2}g\right)d=(mg)\left(\frac{L}{2}-d\right).
$$

Cancel $mg$ and solve:

$$
\frac{d}{2}=\frac{L}{2}-d,
$$

$$
\frac{3d}{2}=\frac{L}{2},
$$

$$
d=\frac{L}{3}.
$$

This support position is also the combined center of mass. It must lie between $0$ and $L/2$, and it should be closer to the heavier rod's center than to the lighter attached mass. Since $L/3$ satisfies both checks, the direction and lever arms are consistent.

Substitution checks the torque balance itself. At $d=L/3$,

$$
\tau_{\mathrm{left}}
=\left(\frac{m}{2}g\right)\frac{L}{3}
=\frac{mgL}{6},
$$

while

$$
\tau_{\mathrm{rod}}
=mg\left(\frac{L}{2}-\frac{L}{3}\right)
=\frac{mgL}{6}.
$$

The equal magnitudes confirm zero net torque.

```quiz
type: radio
id: p6-solve-balance
content: |-
  A mass $m/3$ is placed at the left end of a uniform rod of mass $m$ and length $L$. At what distance $d$ from the left end must a single support be placed for equilibrium?
options:
- id: p6-solve-balance-a
  content: |-
    $\dfrac{L}{8}$
- id: p6-solve-balance-b
  content: |-
    $\dfrac{L}{4}$
- id: p6-solve-balance-c
  content: |-
    $\dfrac{3L}{8}$
  correct: true
- id: p6-solve-balance-d
  content: |-
    $\dfrac{L}{2}$
```

---

<a id="apply-the-method-to-the-rod-and-sphere"></a>
## Apply the Method to the Rod and Sphere

**Example:** A uniform sphere of mass $m/2$ and radius $r$ has its center of mass directly above the left end of a thin uniform rod of mass $m$ and length $L$. Find the support distance $d$ that keeps the system in static equilibrium.

**Explanation**

The sphere's weight acts through its center directly above the rod's left end, so its horizontal lever arm is $d$. The rod's weight acts at $L/2$, so its lever arm is $L/2-d$. Thus,

$$
\left(\frac{m}{2}g\right)d=(mg)\left(\frac{L}{2}-d\right),
$$

which gives

$$
\boxed{d=\frac{L}{3}}.
$$

The sphere's radius $r$ is not needed. Torque from a vertical force depends on the horizontal perpendicular distance from the support to the force's line of action; that line passes through the left end regardless of the sphere's height.

```quiz
type: radio
id: q-6
shuffle: true
content: |-
  A uniform sphere of mass $m/2$ and radius $r$ is placed with its center of mass directly above the end of a thin uniform rod of mass $m$ and length $L$, as shown.

  What must the distance $d$ be for the system to remain in static equilibrium?

  ![](<../Source/2026-07-15-HW-4/Images/rod-sphere-static-equilibrium.png>)
options:
- id: a
  content: |-
    $2L/5$
- id: b
  content: |-
    $L/3$
  correct: true
- id: c
  content: |-
    $L/4$
```

---

<a id="summary"></a>
## Summary

For a horizontal rod-object system supported at one point:

1. Locate each object's center of mass.
2. Measure every lever arm from the support, not from an endpoint.
3. Set the opposing torque magnitudes equal.
4. Cancel common factors such as $g$ and solve for the support position.
5. Check that the support lies between the objects' centers of mass and closer to the heavier contribution.

For a mass $m/2$ at the rod's left end and a uniform rod of mass $m$,

$$
\left(\frac{m}{2}g\right)d=(mg)\left(\frac{L}{2}-d\right)
\quad\Longrightarrow\quad
\boxed{d=\frac{L}{3}}.
$$

The main trap is using $L/2$ as the rod's lever arm. Its correct lever arm about the support is $L/2-d$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
