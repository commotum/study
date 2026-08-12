# Finding a Two-Object Center of Mass in the Plane

<!--
lesson-id: 212-M2-046
topic-code: MTH212.M2.46
-->

## Table of Contents

- [Introduction](#introduction)
- [Place Each Object's Center](#place-each-objects-center)
- [Average Each Coordinate by Mass](#average-each-coordinate-by-mass)
- [Turn the Displacement Into a Distance](#turn-the-displacement-into-a-distance)
- [Separate Geometry From Collision Data](#separate-geometry-from-collision-data)

## Prerequisites

- Coordinates in the plane
- The center of a uniform rod is its midpoint
- The magnitude of a vector $\langle x,y\rangle$ is $\sqrt{x^2+y^2}$

---

<a id="introduction"></a>
## Introduction

When several objects are joined, their combined center of mass is the mass-weighted average of their individual center positions:

$$
\vec{r}_{\mathrm{cm}}=
\frac{m_1\vec{r}_1+m_2\vec{r}_2}{m_1+m_2}.
$$

The recognition cue is a question asking where the center of mass lies after objects combine. In a two-dimensional picture, apply the formula separately to the $x$- and $y$-coordinates. If the question asks **how far** the center of mass is from the origin, find the magnitude only after finding those two components.

It is often helpful to rewrite the mass fractions as normalized weights:

$$
\vec{r}_{\mathrm{cm}}=w_1\vec{r}_1+w_2\vec{r}_2,
\qquad
w_1=\frac{m_1}{m_1+m_2},
\quad
w_2=\frac{m_2}{m_1+m_2}.
$$

Because $w_1+w_2=1$, the combined center must lie between the two individual centers.

---

<a id="place-each-objects-center"></a>
## Place Each Object's Center

**Example:** A vertical uniform rod has length $L$. Put the origin at the rod's center. A ball of radius $r$ touches the left side of the rod at its lower end. Where is the ball's center?

**Explanation**

The lower end of the rod is $L/2$ below its center, so its vertical coordinate is $-L/2$. The center of the ball is one radius to the left of the contact point, so its horizontal coordinate is $-r$. Therefore,

$$
\vec{r}_{\mathrm{ball}}=\left\langle-r,-\frac L2\right\rangle.
$$

Use the center of each object in the center-of-mass formula, not the point where their surfaces touch.

```quiz
type: radio
id: p10-place-centers
content: |-
  A uniform rod of length $2a$ is vertical and centered at the origin. A disk of radius $R$ touches the right side of the rod at its upper end. What is the disk center's position?
options:
- id: a
  content: |-
    $\langle R,a\rangle$
  correct: true
- id: b
  content: |-
    $\langle 0,a\rangle$
- id: c
  content: |-
    $\langle R,2a\rangle$
- id: d
  content: |-
    $\langle 2R,a\rangle$
- id: e
  content: |-
    $\langle -R,a\rangle$
```

---

<a id="average-each-coordinate-by-mass"></a>
## Average Each Coordinate by Mass

**Example:** A rod of mass $m$ has its center at the origin. A ball of mass $m/2$ has its center at $\langle-r,-L/2\rangle$. Find the combined center-of-mass position relative to the rod's center.

**Explanation**

The total mass is

$$
m+\frac m2=\frac{3m}{2}.
$$

Weight each position by its object's mass:

$$
\begin{aligned}
\frac{m}{3m/2}&=\frac23,
&
\frac{m/2}{3m/2}&=\frac13,
\\[4pt]
\vec{r}_{\mathrm{cm}}
&=\frac23\langle0,0\rangle
+\frac13\left\langle-r,-\frac L2\right\rangle\\
&=\left\langle-\frac r3,-\frac L6\right\rangle.
\end{aligned}
$$

The factor $m$ cancels only after both masses have been included in the total mass. As a check, the ball supplies one-third of the total mass, so the combined center is one-third of the way from the rod's center toward the ball's center.

```quiz
type: radio
id: p10-mass-weighted-components
content: |-
  An object of mass $m$ is centered at the origin. A second object of mass $m/3$ is centered at $\langle a,-b\rangle$. What is the combined center-of-mass position?
options:
- id: a
  content: |-
    $\left\langle\dfrac a4,-\dfrac b4\right\rangle$
  correct: true
- id: b
  content: |-
    $\left\langle\dfrac a3,-\dfrac b3\right\rangle$
- id: c
  content: |-
    $\left\langle\dfrac{3a}{4},-\dfrac{3b}{4}\right\rangle$
- id: d
  content: |-
    $\langle a,-b\rangle$
- id: e
  content: |-
    $\left\langle\dfrac a4,\dfrac b4\right\rangle$
```

---

<a id="turn-the-displacement-into-a-distance"></a>
## Turn the Displacement Into a Distance

**Example:** A combined center of mass is at $\langle-r/3,-L/6\rangle$ relative to the chosen origin. How far is it from the origin?

**Explanation**

Distance is the magnitude of the displacement vector:

$$
\begin{aligned}
d
&=\sqrt{\left(-\frac r3\right)^2+\left(-\frac L6\right)^2}\\
&=\sqrt{\left(\frac r3\right)^2+\left(\frac L6\right)^2}.
\end{aligned}
$$

The signs locate the center of mass, but squaring removes them when calculating distance.

```quiz
type: radio
id: p10-displacement-magnitude
content: |-
  A center of mass is at $\left\langle-\dfrac d5,\dfrac h5\right\rangle$ relative to an origin. How far is it from the origin?
options:
- id: a
  content: |-
    $\sqrt{\left(\dfrac d5\right)^2+\left(\dfrac h5\right)^2}$
  correct: true
- id: b
  content: |-
    $-\dfrac d5+\dfrac h5$
- id: c
  content: |-
    $\sqrt{\dfrac d5+\dfrac h5}$
- id: d
  content: |-
    $\dfrac{d+h}{25}$
- id: e
  content: |-
    $\sqrt{d^2+h^2}$
```

---

<a id="separate-geometry-from-collision-data"></a>
## Separate Geometry From Collision Data

**Example:** A stationary rod and a moving ball stick together. To locate the center of mass of their final shape, first identify the masses and final center positions. The ball's incoming speed affects the system's later motion, but it does not enter the position average.

**Explanation**

For the rod-and-ball geometry below, the rod's center is the origin and the ball's center is $\langle-r,-L/2\rangle$. The needed calculation is therefore

$$
\vec{r}_{\mathrm{cm}}
=\frac{m\langle0,0\rangle+\frac m2\left\langle-r,-\frac L2\right\rangle}{m+\frac m2}
=\left\langle-\frac r3,-\frac L6\right\rangle.
$$

Only after that component calculation do we take the magnitude.

```quiz
type: radio
id: p10-original-application
content: |-
  A thin uniform rod of mass $m$ and length $L$ is initially at rest in outer space. A nonspinning ball of mass $m/2$ and radius $r$ strikes one end of the rod with speed $v$ and sticks to it.

  How far is the center of mass of the combined system from the center of the rod? Neglect the third dimension and work in the plane of the figure.

  ![](<../Source/2026-07-15-HW-4/Images/rod-ball-inelastic-collision.png>)
options:
- id: a
  content: |-
    $\sqrt{\left(\dfrac{L}{6}\right)^2+\left(\dfrac{r}{3}\right)^2}$
  correct: true
- id: b
  content: |-
    $\sqrt{\left(\dfrac{2L}{5}\right)^2+(2r)^2}$
```

---

## Summary

Use this checklist:

1. Put the origin at the requested reference point, usually the rod's center.
2. Locate the center of each object, including any radius offset from a contact point.
3. Compute normalized mass weights and check that they sum to $1$.
4. Average the $x$-coordinates and $y$-coordinates separately.
5. If the question asks **how far**, return $\sqrt{x_{\mathrm{cm}}^2+y_{\mathrm{cm}}^2}$.

Speed does not belong in a center-of-mass position formula. The main geometry trap is using the contact point instead of the ball's center; the main algebra trap is dividing by one object's mass instead of the total mass.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../../M3/2026-07-20-Q-2/Study-Guide.md)
Next: [Comparing Moment of Inertia From Mass Distribution](../../2026-07-08-M2-2/Lessons/Problem-1.md)

Study guide index: 02/20

---
<!-- lesson-nav:end -->
