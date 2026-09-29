# Speed of a Rolling Solid Cylinder From Energy

<!--
lesson-id: 212-M2-039
topic-code: MTH212.M2.39
-->

## Table of Contents

- [Introduction](#introduction)
- [Account for Both Kinds of Kinetic Energy](#account-for-both-kinds-of-kinetic-energy)
- [Use the Solid-Cylinder Moment of Inertia](#use-the-solid-cylinder-moment-of-inertia)
- [Recognize What Cancels](#recognize-what-cancels)
- [Use Vertical Height, Not Ramp Angle](#use-vertical-height-not-ramp-angle)
- [Summary](#summary)

## Prerequisites

- Gravitational potential energy: $U_g=mgh$
- Translational kinetic energy: $K_{\mathrm{trans}}=\frac12mv^2$
- Rotational kinetic energy: $K_{\mathrm{rot}}=\frac12I\omega^2$
- Rolling without slipping: $v=\omega R$

---

<a id="introduction"></a>
## Introduction

When a rigid object rolls without slipping down a ramp and energy losses are negligible, its lost gravitational potential energy becomes **both** translational and rotational kinetic energy. The recognition cue is the phrase “rolls without slipping.”

The reusable setup is

$$
mgh=\frac12mv^2+\frac12I\omega^2,
$$

followed by $\omega=v/R$ and the moment of inertia for the object's shape. The main trap is to use only $\frac12mv^2$, which treats the object as if it were sliding without rotating.

---

<a id="account-for-both-kinds-of-kinetic-energy"></a>
## Account for Both Kinds of Kinetic Energy

**Example:** A rolling object has moment of inertia $I=k mR^2$, where $k$ depends only on its shape. Derive its speed after its center of mass drops through a vertical height $h$.

**Explanation**

Start with conservation of mechanical energy:

$$
mgh=\frac12mv^2+\frac12I\omega^2.
$$

Use $I=kmR^2$ and $\omega=v/R$:

$$
\begin{aligned}
mgh
&=\frac12mv^2+\frac12(kmR^2)\left(\frac{v}{R}\right)^2 \\
&=\frac12mv^2+\frac12kmv^2 \\
&=\frac12m(1+k)v^2.
\end{aligned}
$$

Cancel $m$ and solve for the nonnegative speed:

$$
v=\sqrt{\frac{2gh}{1+k}}.
$$

```quiz
type: radio
id: lesson-p3-q1
content: |-
  A thin hoop rolls without slipping from rest through a vertical drop $h$. Since $I=mR^2$, what speed does it reach?
options:
- id: a
  content: |-
    $\sqrt{2gh}$
- id: b
  content: |-
    $\sqrt{gh}$
  correct: true
- id: c
  content: |-
    $\sqrt{\dfrac{gh}{2}}$
- id: d
  content: |-
    $2\sqrt{gh}$
```

---

<a id="use-the-solid-cylinder-moment-of-inertia"></a>
## Use the Solid-Cylinder Moment of Inertia

**Example:** Find the bottom speed of a uniform solid cylinder released from rest through a vertical drop $h$.

**Explanation**

For a uniform solid cylinder,

$$
I=\frac12mR^2,
$$

so $k=\frac12$. Substitute into the rolling-speed formula:

$$
\begin{aligned}
v
&=\sqrt{\frac{2gh}{1+\frac12}} \\
&=\sqrt{\frac{2gh}{\frac32}} \\
&=\sqrt{\frac{4gh}{3}}.
\end{aligned}
$$

Equivalently, the energy equation becomes $mgh=\frac34mv^2$. The rotational term is essential: omitting it would incorrectly give $v=\sqrt{2gh}$.

```quiz
type: radio
id: lesson-p3-q2
content: |-
  A uniform solid cylinder rolls without slipping from rest through a vertical drop $2h$. What is its speed at the bottom?
options:
- id: a
  content: |-
    $\sqrt{\dfrac{8gh}{3}}$
  correct: true
- id: b
  content: |-
    $\sqrt{4gh}$
- id: c
  content: |-
    $\sqrt{\dfrac{4gh}{3}}$
- id: d
  content: |-
    $\sqrt{\dfrac{2gh}{3}}$
```

---

<a id="recognize-what-cancels"></a>
## Recognize What Cancels

**Example:** One solid cylinder has mass $M$ and radius $R$. A second has mass $4M$ and radius $R/2$. Both roll from rest through the same vertical drop. Compare their bottom speeds.

**Explanation**

For either solid cylinder,

$$
\begin{aligned}
mgh
&=\frac12mv^2+\frac12\left(\frac12mR^2\right)\left(\frac{v}{R}\right)^2 \\
&=\frac34mv^2.
\end{aligned}
$$

The radius cancels inside the rotational term, and the mass then cancels from the entire equation. Therefore, cylinders with the same shape and the same vertical drop reach the same speed even if their masses and radii differ:

$$
v=\sqrt{\frac{4gh}{3}}.
$$

This cancellation does **not** mean that every rolling object reaches the same speed. The shape factor in $I=kmR^2$ remains, so a hoop and a solid cylinder released from the same height generally have different bottom speeds.

```quiz
type: radio
id: lesson-p3-q3
content: |-
  Cylinder A is a uniform solid cylinder of mass $m$ and radius $R$. Cylinder B is a uniform solid cylinder of mass $3m$ and radius $2R$. They roll without slipping from rest through the same vertical drop. Which comparison is correct?
options:
- id: a
  content: |-
    Cylinder A is faster because it has less mass.
- id: b
  content: |-
    Cylinder B is faster because it has more rotational inertia.
- id: c
  content: |-
    Cylinder B is faster because it has a larger radius.
- id: d
  content: |-
    They reach the same speed because mass and radius cancel.
  correct: true
```

---

<a id="use-vertical-height-not-ramp-angle"></a>
## Use Vertical Height, Not Ramp Angle

**Example:** A solid cylinder starts at the top of a ramp of vertical height $h$ and inclination angle $\theta$. Decide whether $\theta$ belongs in its bottom-speed formula.

**Explanation**

Gravitational potential energy depends on the **vertical** change in height. Because the problem already gives that change as $h$, the energy lost is simply $mgh$. The ramp angle affects the distance traveled along the ramp and the acceleration along it, but not the final speed obtained from a fixed vertical drop under these assumptions.

The angle would be needed only if the problem gave a ramp length $L$ instead of its height; then the vertical drop would be $h=L\sin\theta$.

```quiz
type: radio
id: lesson-p3-q4
content: |-
  Two uniform solid cylinders are released simultaneously from rest at the top of a ramp of height $h$ inclined at angle $\theta$. One cylinder has mass $M$ and radius $R$; the other has mass $4M$ and radius $R/2$. Both roll without slipping.

  With what speed does the cylinder with mass $4M$ and radius $R/2$ reach the bottom?
options:
- id: a
  content: |-
    $\sqrt{\dfrac{2gh}{\cos\theta}}$
- id: b
  content: |-
    $\sqrt{\dfrac{gh\cos\theta}{4}}$
- id: c
  content: |-
    $\sqrt{\dfrac{4gh}{3}}$
  correct: true
- id: d
  content: |-
    $\sqrt{\dfrac{5gh\sin\theta}{2}}$
```

---

<a id="summary"></a>
## Summary

When an object rolls without slipping from rest through a vertical drop $h$:

1. Write $mgh=\frac12mv^2+\frac12I\omega^2$.
2. Replace $\omega$ with $v/R$.
3. Substitute the moment of inertia for the object's shape.
4. Cancel common factors, then solve for the nonnegative speed.

For a uniform solid cylinder, $I=\frac12mR^2$, so

$$
v=\sqrt{\frac{4gh}{3}}.
$$

Mass and radius cancel for cylinders of the same shape. If $h$ is already the vertical height, the ramp angle does not enter the final speed.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../../M3/2026-07-20-Q-2/Study-Guide.md)
Next: [Comparing Translational and Rotational Kinetic Energy in Rolling](../../../M3/2026-07-19-PQ-2/Lessons/Problem-2.md)

Study guide index: 09/20

---
<!-- lesson-nav:end -->
