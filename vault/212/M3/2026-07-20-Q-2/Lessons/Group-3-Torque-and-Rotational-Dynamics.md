# Turn Applied Forces into Angular Acceleration

<!--
lesson-id: 212-M3-026
topic-code: MTH212.M3.26
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Perpendicular Turning Effect](#find-the-perpendicular-turning-effect)
- [Assign a Torque Direction](#assign-a-torque-direction)
- [Choose an Axis That Removes Unknown Torques](#choose-an-axis-that-removes-unknown-torques)
- [Apply Rotational Newton's Second Law](#apply-rotational-newtons-second-law)
- [Combine the Inertia of Rigidly Attached Bodies](#combine-the-inertia-of-rigidly-attached-bodies)
- [Predict Changes Before Calculating](#predict-changes-before-calculating)
- [Summary](#summary)

## Prerequisites

- Resolve a force into perpendicular components.
- Use the right-hand rule for a cross product.
- Calculate common moments of inertia about a stated axis.
- Distinguish a force from the torque that force produces.

---

<a id="introduction"></a>
## Introduction

When a force acts on an extended object, determine its turning effect about a chosen axis and then relate the net torque to angular acceleration:

$$
\vec\tau=\vec r\times\vec F,
\qquad
|\tau|=rF\sin\phi=Fd_\perp,
$$

$$
\sum\tau=I\alpha.
$$

The reusable sequence is: choose the axis, find each moment arm, assign signs, add torques, build $I$ about the same axis, and solve for $\alpha$.

**Recognition cue:** If the question asks whether a force turns an object, start with the force’s line of action—not with the force magnitude alone. If it asks how quickly the rotation changes, continue from net torque to $I\alpha$.

Two boundary cases are worth recognizing immediately: a force whose line of action passes through the pivot produces zero torque, while a perpendicular force produces the largest torque available for fixed $r$ and $F$.

---

<a id="find-the-perpendicular-turning-effect"></a>
## Find the Perpendicular Turning Effect

**Example:** A $120\text{ N}$ force acts on the end of a $0.52\text{ m}$ wrench. The angle between $\vec r$ and $\vec F$ is $57^\circ$. Find the torque magnitude.

**Explanation**

Use the angle between the position vector and the force, not an angle measured from some unrelated line:

$$
\tau=rF\sin\phi.
$$

Therefore,

$$
\tau=(0.52)(120)\sin57^\circ\approx52\text{ N}\cdot\text{m}.
$$

Equivalently, first find the perpendicular moment arm $d_\perp=r\sin\phi$ and use $\tau=Fd_\perp$.

```quiz
type: radio
id: torque-dynamics-q1
shuffle: true
content: |-
  A $50\text{ N}$ force acts $0.40\text{ m}$ from a pivot. The angle between $\vec r$ and $\vec F$ is $30^\circ$. What is the torque magnitude?
options:
- id: torque-dynamics-q1-a
  content: |-
    $10\text{ N}\cdot\text{m}$
  correct: true
  feedback: |-
    $\tau=(0.40)(50)\sin30^\circ=10\text{ N}\cdot\text{m}$.
- id: torque-dynamics-q1-b
  content: |-
    $17.3\text{ N}\cdot\text{m}$
  feedback: |-
    This uses cosine instead of the component perpendicular to $\vec r$.
- id: torque-dynamics-q1-c
  content: |-
    $20\text{ N}\cdot\text{m}$
  feedback: |-
    This treats the force as perpendicular even though $\phi=30^\circ$.
- id: torque-dynamics-q1-d
  content: |-
    $125\text{ N}\cdot\text{m}$
```

---

<a id="assign-a-torque-direction"></a>
## Assign a Torque Direction

**Example:** From a pivot at the origin, $\vec r$ points right and $\vec F$ points upward. Determine the torque direction.

**Explanation**

Apply the right-hand rule to

$$
\vec\tau=\vec r\times\vec F.
$$

Point your fingers along $\vec r$ and curl them toward $\vec F$. Your thumb points out of the page, so

$$
\vec\tau=+\tau\hat z.
$$

In a planar problem, you may use counterclockwise as positive and clockwise as negative, provided you remain consistent.

```quiz
type: radio
id: torque-dynamics-q2
shuffle: true
content: |-
  A position vector points right from a pivot, and the applied force points downward. What is the torque direction?
options:
- id: torque-dynamics-q2-a
  content: |-
    Out of the page, corresponding to counterclockwise rotation
- id: torque-dynamics-q2-b
  content: |-
    Into the page, corresponding to clockwise rotation
  correct: true
  feedback: |-
    Right crossed with down points into the page.
- id: torque-dynamics-q2-c
  content: |-
    To the right, along $\vec r$
- id: torque-dynamics-q2-d
  content: |-
    Downward, along $\vec F$
```

---

<a id="choose-an-axis-that-removes-unknown-torques"></a>
## Choose an Axis That Removes Unknown Torques

**Example:** A spool is mounted on a frictionless spindle through its center. A cord pulls tangentially at radius $r$. Which forces contribute torque about the spindle axis?

**Explanation**

Draw an extended free-body diagram so the application point of each force is visible. Any force whose line of action passes through the chosen axis has

$$
d_\perp=0
\quad\Rightarrow\quad
\tau=0.
$$

The spindle force acts at the axis, so it produces no torque about that axis. The tangential cord tension has moment arm $r$, so

$$
\tau_T=Tr.
$$

Choosing the spindle axis removes the unknown spindle force from the torque equation.

```quiz
type: radio
id: torque-dynamics-q3
shuffle: true
content: |-
  Which force necessarily produces zero torque about a selected pivot?
options:
- id: torque-dynamics-q3-a
  content: |-
    Any force smaller than the object's weight
- id: torque-dynamics-q3-b
  content: |-
    Any horizontal force
- id: torque-dynamics-q3-c
  content: |-
    A force whose line of action passes through the pivot
  correct: true
  feedback: |-
    Its perpendicular moment arm is zero.
- id: torque-dynamics-q3-d
  content: |-
    Any force acting on the object's center of mass
  feedback: |-
    It is zero only if the chosen pivot lies on that force's line of action.
```

---

<a id="apply-rotational-newtons-second-law"></a>
## Apply Rotational Newton's Second Law

**Example:** A tangential tension $T$ pulls a uniform solid cylinder of mass $m$ and radius $r$ about its fixed central axis. Find $\alpha$.

**Explanation**

The applied torque is

$$
\tau=Tr.
$$

For a solid cylinder,

$$
I=\frac12mr^2.
$$

Apply $\sum\tau=I\alpha$:

$$
Tr=\frac12mr^2\alpha.
$$

Solving gives

$$
\alpha=\frac{2T}{mr}.
$$

The radius appears in both the applied torque and the rotational inertia; simplify only after writing both correctly.

```quiz
type: radio
id: torque-dynamics-q4
shuffle: true
content: |-
  A tangential force $F$ acts at the rim of a uniform solid disk of mass $M$ and radius $R$, rotating about its center. What is its angular acceleration?
options:
- id: torque-dynamics-q4-a
  content: |-
    $\dfrac{F}{MR}$
- id: torque-dynamics-q4-b
  content: |-
    $\dfrac{2F}{MR}$
  correct: true
  feedback: |-
    Set $FR=(\frac12MR^2)\alpha$.
- id: torque-dynamics-q4-c
  content: |-
    $\dfrac{FR}{2M}$
- id: torque-dynamics-q4-d
  content: |-
    $\dfrac{2FR}{M}$
```

---

<a id="combine-the-inertia-of-rigidly-attached-bodies"></a>
## Combine the Inertia of Rigidly Attached Bodies

**Example:** Two solid cylinders are rigidly attached along a common axis. Their masses and radii are $(m,r)$ and $(M,R)$. A tangential force $F$ acts at radius $R$. Find the angular acceleration.

**Explanation**

Rigid attachment means both cylinders share the same $\alpha$. Add their moments of inertia about the common axis:

$$
I_{\mathrm{total}}=\frac12mr^2+\frac12MR^2.
$$

The external torque is $FR$, so

$$
FR=\left(\frac12mr^2+\frac12MR^2\right)\alpha.
$$

Therefore,

$$
\alpha=\frac{2FR}{mr^2+MR^2}.
$$

Do not apply $\sum\tau=I\alpha$ to each rigidly attached piece as though it had an independent angular acceleration.

```quiz
type: radio
id: torque-dynamics-q5
shuffle: true
content: |-
  Two solid disks, each of mass $M$, have radii $R$ and $2R$ and are rigidly attached about a common axis. A tangential force $F$ acts at radius $2R$. What is $\alpha$?
options:
- id: torque-dynamics-q5-a
  content: |-
    $\dfrac{F}{MR}$
- id: torque-dynamics-q5-b
  content: |-
    $\dfrac{4F}{5MR}$
  correct: true
  feedback: |-
    The torque is $2FR$, while $I_{\mathrm{total}}=\frac12MR^2+\frac12M(2R)^2=\frac52MR^2$.
- id: torque-dynamics-q5-c
  content: |-
    $\dfrac{2F}{MR}$
  feedback: |-
    This ignores most of the rotational inertia.
- id: torque-dynamics-q5-d
  content: |-
    $\dfrac{5F}{4MR}$
```

---

<a id="predict-changes-before-calculating"></a>
## Predict Changes Before Calculating

**Example:** The same perpendicular force is moved from radius $r$ to radius $2r$ on an object whose moment of inertia remains fixed. How does $\alpha$ change?

**Explanation**

For a perpendicular force,

$$
\tau=rF.
$$

Doubling $r$ doubles $\tau$. Since

$$
\alpha=\frac{\sum\tau}{I},
$$

the angular acceleration also doubles when $I$ is unchanged.

This conclusion would not follow if moving the force also changed the object's mass distribution or rotation axis.

```quiz
type: radio
id: torque-dynamics-q6
shuffle: true
content: |-
  The net torque on a rigid body is tripled while its moment of inertia stays fixed. What happens to its angular acceleration?
options:
- id: torque-dynamics-q6-a
  content: |-
    It becomes one third as large.
- id: torque-dynamics-q6-b
  content: |-
    It is unchanged.
- id: torque-dynamics-q6-c
  content: |-
    It doubles.
- id: torque-dynamics-q6-d
  content: |-
    It triples.
  correct: true
  feedback: |-
    From $\alpha=\sum\tau/I$, $\alpha$ scales directly with torque at fixed $I$.
```

---

<a id="summary"></a>
## Summary

For a rotational-dynamics problem:

1. Choose and label the rotation axis.
2. Draw where every force acts.
3. Use $\tau=rF\sin\phi=Fd_\perp$ and assign a sign with the right-hand rule.
4. Drop forces whose lines of action pass through the axis.
5. Build the total $I$ about that same axis.
6. Apply $\sum\tau=I\alpha$ and check how the answer scales with $F$, $r$, and $I$.

The main traps are using the wrong angle, forgetting torque direction, or computing $I$ about a different axis from the torque equation.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
