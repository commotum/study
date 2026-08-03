# Build the Moment of Inertia About a Chosen Axis

<!--
lesson-id: 212-M3-025
topic-code: MTH212.M3.25
-->

## Table of Contents

- [Introduction](#introduction)
- [Measure Every Mass from the Axis](#measure-every-mass-from-the-axis)
- [Integrate a Continuous Distribution](#integrate-a-continuous-distribution)
- [Shift to a Parallel Axis](#shift-to-a-parallel-axis)
- [Add Rigidly Connected Pieces](#add-rigidly-connected-pieces)
- [Treat a Hole as Removed Mass](#treat-a-hole-as-removed-mass)
- [Connect Moment of Inertia to Rotational Energy](#connect-moment-of-inertia-to-rotational-energy)
- [Summary](#summary)

## Prerequisites

- Compute a center of mass and write $dm$ from a density.
- Evaluate polynomial integrals.
- Identify the shortest perpendicular distance from a mass to a rotation axis.
- Use $K_{\mathrm{rot}}=\frac12I\omega^2$.

---

<a id="introduction"></a>
## Introduction

When a problem asks how difficult a body is to rotate, first identify the rotation axis. Then weight every mass element by the square of its perpendicular distance from that axis:

$$
I=\sum_i m_ir_i^2
\qquad\text{or}\qquad
I=\int r^2\,dm.
$$

Unlike mass, moment of inertia belongs to an **object-axis pair**. The same object has different moments of inertia about different axes.

**Recognition cue:** Circle the requested axis before using any memorized shape formula. If the object is composite, every added or subtracted contribution must be expressed about that same axis.

---

<a id="measure-every-mass-from-the-axis"></a>
## Measure Every Mass from the Axis

**Example:** A point mass $m$ is at distance $R$ from an axis, and a point mass $2m$ is at distance $2R$. Find the total moment of inertia.

**Explanation**

Square each perpendicular distance before multiplying by mass:

$$
I=mR^2+(2m)(2R)^2.
$$

Therefore,

$$
I=mR^2+8mR^2=9mR^2.
$$

The second object contributes eight times as much as the first: twice the mass and four times the squared distance.

```quiz
type: radio
id: inertia-q1
shuffle: true
content: |-
  A point mass $3m$ is at distance $R$ from an axis, and a point mass $m$ is at distance $3R$. What is the system's moment of inertia?
options:
- id: inertia-q1-a
  content: |-
    $6mR^2$
  feedback: |-
    This uses distance linearly instead of squaring it.
- id: inertia-q1-b
  content: |-
    $9mR^2$
- id: inertia-q1-c
  content: |-
    $12mR^2$
  correct: true
  feedback: |-
    $I=(3m)R^2+m(3R)^2=3mR^2+9mR^2$.
- id: inertia-q1-d
  content: |-
    $18mR^2$
```

---

<a id="integrate-a-continuous-distribution"></a>
## Integrate a Continuous Distribution

**Example:** A rod occupies $0\le x\le L$ and has density $\lambda(x)=Cx$. Its total mass is $M$. Find its moment of inertia about the left end.

**Explanation**

The axis is at $x=0$, so the perpendicular distance is $r=x$. First normalize the density:

$$
M=\int_0^L Cx\,dx=\frac{CL^2}{2}
\quad\Rightarrow\quad
C=\frac{2M}{L^2}.
$$

Then insert the squared distance into the inertia integral:

$$
I=\int_0^L x^2\,dm
=
\int_0^L x^2(Cx\,dx)
=
C\int_0^Lx^3\,dx.
$$

Thus,

$$
I=\frac{CL^4}{4}=\frac12ML^2.
$$

Do not confuse the center-of-mass integrand $x\,dm$ with the inertia integrand $x^2\,dm$.

```quiz
type: radio
id: inertia-q2
shuffle: true
content: |-
  A rod lies on $0\le x\le L$, has total mass $M$, and has density $\lambda(x)=Cx^2$. Which integral gives its moment of inertia about the left end after writing $dm=Cx^2\,dx$?
options:
- id: inertia-q2-a
  content: |-
    $\displaystyle I=C\int_0^L x^2\,dx$
  feedback: |-
    This omits the additional $x^2$ distance factor from $I=\int r^2dm$.
- id: inertia-q2-b
  content: |-
    $\displaystyle I=C\int_0^L x^3\,dx$
  feedback: |-
    This uses only one additional power of $x$.
- id: inertia-q2-c
  content: |-
    $\displaystyle I=C\int_0^L x^4\,dx$
  correct: true
  feedback: |-
    Multiply the density factor $x^2$ by the squared distance $r^2=x^2$.
- id: inertia-q2-d
  content: |-
    $\displaystyle I=\frac{C}{M}\int_0^L x^3\,dx$
  feedback: |-
    The factor $1/M$ belongs to a center-of-mass calculation, not moment of inertia.
```

---

<a id="shift-to-a-parallel-axis"></a>
## Shift to a Parallel Axis

**Example:** A uniform disk has mass $M$, radius $R$, and central moment of inertia $I_{\mathrm{cm}}=\frac12MR^2$. Find its moment of inertia about a parallel axis through its rim.

**Explanation**

The new axis is a distance $d=R$ from the center-of-mass axis. Apply the parallel-axis theorem:

$$
I=I_{\mathrm{cm}}+Md^2.
$$

Therefore,

$$
I_{\mathrm{rim}}=\frac12MR^2+MR^2=\frac32MR^2.
$$

The shift term is always added. Moving a parallel axis away from the center of mass cannot reduce $I$.

**Boundary case:** The parallel-axis theorem connects parallel axes only. It does not convert a known inertia into the inertia about a tilted axis.

```quiz
type: radio
id: inertia-q3
shuffle: true
content: |-
  A thin rod has $I_{\mathrm{cm}}=\frac{1}{12}ML^2$. What is its moment of inertia about a perpendicular axis through one end?
options:
- id: inertia-q3-a
  content: |-
    $\dfrac{1}{48}ML^2$
- id: inertia-q3-b
  content: |-
    $\dfrac{1}{12}ML^2$
- id: inertia-q3-c
  content: |-
    $\dfrac{1}{6}ML^2$
- id: inertia-q3-d
  content: |-
    $\dfrac{1}{3}ML^2$
  correct: true
  feedback: |-
    Add $M(L/2)^2$ to $I_{\mathrm{cm}}$.
```

---

<a id="add-rigidly-connected-pieces"></a>
## Add Rigidly Connected Pieces

**Example:** A uniform rod of mass $M$ and length $L$ rotates about one end. A point mass $2M$ is attached at the other end. Find the total moment of inertia.

**Explanation**

Every piece must be evaluated about the same axis:

$$
I_{\mathrm{rod}}=\frac13ML^2,\qquad
I_{\mathrm{point}}=(2M)L^2.
$$

Add the contributions:

$$
I_{\mathrm{total}}
=
\frac13ML^2+2ML^2
=
\frac73ML^2.
$$

Do not average component moments of inertia. Moment of inertia is additive about a common axis.

```quiz
type: radio
id: inertia-q4
shuffle: true
content: |-
  A uniform rod of mass $M$ and length $L$ rotates about one end. A point mass $3M$ is attached at the other end. What is $I_{\mathrm{total}}$?
options:
- id: inertia-q4-a
  content: |-
    $\dfrac{10}{3}ML^2$
  correct: true
  feedback: |-
    Add $\frac13ML^2$ for the rod and $3ML^2$ for the point mass.
- id: inertia-q4-b
  content: |-
    $\dfrac{5}{3}ML^2$
- id: inertia-q4-c
  content: |-
    $3ML^2$
  feedback: |-
    This omits the rod's own moment of inertia.
- id: inertia-q4-d
  content: |-
    $\dfrac{1}{3}ML^2$
  feedback: |-
    This omits the attached mass.
```

---

<a id="treat-a-hole-as-removed-mass"></a>
## Treat a Hole as Removed Mass

**Example:** A disk originally has mass $M$ and radius $R$. A circular hole of radius $R/2$ is cut with its center a distance $R/2$ from the original center. Find the remaining moment of inertia about the original center.

**Explanation**

The removed area is one quarter of the original area, so its mass is

$$
M_h=\frac{M}{4}.
$$

Find the hole's inertia about the original axis. First use its own center, then shift by $d=R/2$:

$$
I_h
=
\frac12M_h\left(\frac{R}{2}\right)^2
+
M_h\left(\frac{R}{2}\right)^2
=
\frac{3}{32}MR^2.
$$

Subtract it from the original disk:

$$
I_{\mathrm{remaining}}
=
\frac12MR^2-\frac{3}{32}MR^2
=
\frac{13}{32}MR^2.
$$

The trap is subtracting the hole's central inertia without shifting it to the requested axis.

```quiz
type: radio
id: inertia-q5
shuffle: true
content: |-
  To find the moment of inertia of an off-center hole about the original object's axis, which procedure is correct?
options:
- id: inertia-q5-a
  content: |-
    Subtract the hole's moment of inertia about its own center directly.
- id: inertia-q5-b
  content: |-
    Shift the hole's inertia to the requested axis with the parallel-axis theorem, then subtract it.
  correct: true
  feedback: |-
    Every contribution must refer to the same rotation axis before addition or subtraction.
- id: inertia-q5-c
  content: |-
    Add the shifted inertia of the hole because the hole is away from the center.
- id: inertia-q5-d
  content: |-
    Ignore the hole's location and subtract only its mass.
```

---

<a id="connect-moment-of-inertia-to-rotational-energy"></a>
## Connect Moment of Inertia to Rotational Energy

**Example:** The same disk rotates at angular speed $\omega$ first about its center and then about a parallel axis through its rim. Compare the two rotational kinetic energies.

**Explanation**

At fixed angular speed,

$$
K_{\mathrm{rot}}=\frac12I\omega^2
$$

means that kinetic energy is proportional to $I$. Since

$$
I_{\mathrm{cm}}=\frac12MR^2,\qquad
I_{\mathrm{rim}}=\frac32MR^2,
$$

the ratio is

$$
\frac{K_{\mathrm{rim}}}{K_{\mathrm{cm}}}
=
\frac{I_{\mathrm{rim}}}{I_{\mathrm{cm}}}
=3.
$$

This comparison works only because the angular speeds are equal.

```quiz
type: radio
id: inertia-q6
shuffle: true
content: |-
  Objects A and B rotate at the same angular speed. If $I_B=4I_A$, what is $K_B/K_A$?
options:
- id: inertia-q6-a
  content: |-
    $1/4$
- id: inertia-q6-b
  content: |-
    $1$
- id: inertia-q6-c
  content: |-
    $2$
- id: inertia-q6-d
  content: |-
    $4$
  correct: true
  feedback: |-
    At equal $\omega$, rotational kinetic energy is directly proportional to $I$.
```

---

<a id="summary"></a>
## Summary

To build a moment of inertia:

1. Name the rotation axis before doing any calculation.
2. Measure the perpendicular distance $r$ from that axis.
3. Use $I=\sum m_ir_i^2$ or $I=\int r^2dm$.
4. Shift a known center-of-mass result with $I=I_{\mathrm{cm}}+Md^2$.
5. Add rigid components about a common axis; shift and subtract removed pieces.
6. Use $K_{\mathrm{rot}}=\frac12I\omega^2$ to translate inertia comparisons into energy comparisons when $\omega$ is fixed.

The main trap is using a correct shape formula about the wrong axis.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
