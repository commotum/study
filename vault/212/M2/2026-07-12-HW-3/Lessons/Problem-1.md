# Interpreting the Moment of Inertia Integral

<!--
lesson-id: 212-M2-017
topic-code: MTH212.M2.17
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Integrand](#read-the-integrand)
- [Changing the Axis Changes the Inertia](#changing-the-axis-changes-the-inertia)
- [Replace Mass Elements with Geometry](#replace-mass-elements-with-geometry)
- [Choose an Integral or a Sum](#choose-an-integral-or-a-sum)
- [Connect the Ideas](#connect-the-ideas)
- [Summary](#summary)

## Prerequisites

- Interpret a definite integral as adding infinitesimal contributions.
- Identify the shortest distance from a point to a line.
- Recognize linear, surface, and volume mass density.

---

<a id="introduction"></a>
## Introduction

The formula

$$
I=\int r^2\,dm
$$

adds the rotational contribution of every infinitesimal mass element in an object. The recognition cue is a request to explain the symbols or meaning of this integral. Read it as: for each tiny mass $dm$, square its **perpendicular distance** $r$ from the chosen rotation axis, multiply by $dm$, and add the results over the whole object.

The reusable move is to connect each part of the notation to the object's mass distribution and the specified axis.

Read the notation one piece at a time:

| Symbol | Meaning |
| --- | --- |
| $dm$ | one infinitesimal piece of mass |
| $r$ | that piece's shortest perpendicular distance to the chosen axis |
| $r^2dm$ | that piece's contribution to $I$ |
| $\int$ | add the contributions over all mass in the object or system |

---

<a id="read-the-integrand"></a>
## Read the Integrand

**Example:** A small mass element $dm$ lies near a vertical rotation axis. Its position is connected to the axis by a slanted segment of length $s$, while the shortest segment from the axis to the mass has length $r$. Which distance belongs in $I=\int r^2\,dm$?

**Explanation**

Use $r$, the shortest perpendicular distance to the axis. The element's contribution is

$$
dI=r^2\,dm.
$$

The integral then adds $dI$ over **all** mass elements in the specified object or system. A larger $r$ matters strongly because the distance is squared. The units also confirm the meaning:

$$
[I]=[r^2][m]=\text{mass}\cdot\text{length}^2.
$$

```quiz
type: radio
id: p1-read-integrand
content: |-
  A mass element lies $0.20\,\mathrm{m}$ from an axis by the shortest perpendicular path. A different slanted path from the axis to the element is $0.35\,\mathrm{m}$. Which factor multiplies $dm$ in the moment of inertia integral?
options:
- id: a
  content: |-
    $(0.20\,\mathrm{m})^2$
  correct: true
- id: b
  content: |-
    $(0.35\,\mathrm{m})^2$
- id: c
  content: |-
    $0.20\,\mathrm{m}$
- id: d
  content: |-
    $0.35\,\mathrm{m}$
- id: e
  content: |-
    $(0.35-0.20)\,\mathrm{m}$
```

---

<a id="changing-the-axis-changes-the-inertia"></a>
## Changing the Axis Changes the Inertia

**Example:** Two point masses, each of mass $m$, are at $x=-a$ and $x=a$. About an axis through $x=0$, both are distance $a$ away, so

$$
I_0=ma^2+ma^2=2ma^2.
$$

Move the parallel axis to $x=a$. One mass is now on the axis and the other is distance $2a$ away:

$$
I_a=m(2a)^2+m(0)^2=4ma^2.
$$

**Explanation**

Moment of inertia is not a property of the object alone. It is a property of the object's mass distribution **relative to a chosen axis**. Changing the axis changes the perpendicular distances and therefore can change $I$.

```quiz
type: radio
id: p1-axis-choice
content: |-
  The mass distribution of a rigid object stays fixed, but the rotation axis is changed. Why can the object's moment of inertia change?
options:
- id: a
  content: |-
    The object's total mass changes when the axis moves.
- id: b
  content: |-
    The perpendicular distances $r$ from the mass elements to the axis can change.
  correct: true
- id: c
  content: |-
    The exponent on $r$ changes with the axis.
- id: d
  content: |-
    The mass elements $dm$ stop covering the whole object.
- id: e
  content: |-
    Moment of inertia is independent of the axis, so it cannot change.
```

---

<a id="replace-mass-elements-with-geometry"></a>
## Replace Mass Elements with Geometry

**Example:** A thin rod lies along the $x$-axis from $x=0$ to $x=L$ and rotates about an axis through $x=0$ perpendicular to the rod. If its linear mass density is $\lambda(x)$, then

$$
dm=\lambda(x)\,dx
$$

and the perpendicular distance is $r=x$. Therefore,

$$
I=\int_0^L x^2\lambda(x)\,dx.
$$

**Explanation**

The abstract mass integral becomes a geometric integral after replacing $dm$ with the appropriate density element:

$$
dm=\lambda\,ds,\qquad dm=\sigma\,dA,\qquad dm=\rho\,dV.
$$

Use linear density for a wire or rod, surface density for a thin sheet, and volume density for a three-dimensional body.

```quiz
type: radio
id: p1-density-substitution
content: |-
  A thin plate has surface mass density $\sigma(x,y)$. Which substitution converts $I=\int r^2\,dm$ into an integral over the plate's geometry?
options:
- id: a
  content: |-
    $dm=\sigma(x,y)\,dA$
  correct: true
- id: b
  content: |-
    $dm=\sigma(x,y)\,dx$
- id: c
  content: |-
    $dm=\sigma(x,y)\,dV$
- id: d
  content: |-
    $dm=r^2\,dA$
- id: e
  content: |-
    $dm=\dfrac{dA}{\sigma(x,y)}$
```

---

<a id="choose-an-integral-or-a-sum"></a>
## Choose an Integral or a Sum

**Example:** Three point-like objects have masses $m_1,m_2,m_3$ and perpendicular distances $r_1,r_2,r_3$ from an axis. Their moment of inertia is

$$
I=m_1r_1^2+m_2r_2^2+m_3r_3^2
=\sum_{i=1}^{3}m_i r_i^2.
$$

**Explanation**

Use $I=\int r^2\,dm$ when mass is treated as continuously distributed. Use

$$
I=\sum_{i=1}^{N}m_i r_i^2
$$

for $N$ discrete point-like objects. Both formulas implement the same idea: add every mass contribution weighted by squared perpendicular distance.

For a continuous object, imagine first dividing the mass into many small pieces $\Delta m_k$:

$$
I\approx\sum_k r_k^2\Delta m_k.
$$

As the pieces become infinitesimal, this sum becomes $\int r^2\,dm$. The sum and integral are therefore two versions of the same accumulation rule, not unrelated formulas.

```quiz
type: radio
id: p1-integral-or-sum
content: |-
  A system consists of four point-like masses $m_i$ at perpendicular distances $r_i$ from the chosen axis. Which expression directly gives its moment of inertia?
options:
- id: a
  content: |-
    $\displaystyle I=\sum_{i=1}^{4}m_i r_i^2$
  correct: true
- id: b
  content: |-
    $\displaystyle I=\sum_{i=1}^{4}m_i r_i$
- id: c
  content: |-
    $\displaystyle I=\int_1^4 r_i^2\,dm_i$
- id: d
  content: |-
    $\displaystyle I=\left(\sum_{i=1}^{4}m_i\right)\left(\sum_{i=1}^{4}r_i\right)^2$
- id: e
  content: |-
    $\displaystyle I=\sum_{i=1}^{4}\frac{m_i}{r_i^2}$
```

---

<a id="connect-the-ideas"></a>
## Connect the Ideas

**Example:** Consider these claims about $I=\int r^2\,dm$:

1. The variable $r$ represents the shortest (perpendicular) distance from the axis of rotation to the position of the infinitesimal mass element $dm$.
2. The value of the integral (moment of inertia) depends on the choice of the axis of rotation.
3. The integration is over all mass elements $dm$ of the specified object or system.
4. If $dm$ is expressed in terms of an object's linear, surface, or volume density, the integration becomes an integral over the object's geometry.
5. This formula applies to continuous objects or systems. For discrete point-like objects, use $I=\sum_{i=1}^{N}m_i r_i^2$, where the sum is over the $N$ objects, $m_i$ is each object's mass, and $r_i$ is its perpendicular distance from the axis.

**Explanation**

All five claims are true. They describe the distance, axis, domain, density substitution, and discrete counterpart of the defining integral.

```quiz
type: radio
id: p1-connected-meaning
content: |-
  Which statement does **not** correctly describe $I=\int r^2\,dm$?
options:
- id: a
  content: |-
    The integral adds contributions from all mass elements in the specified object or system.
- id: b
  content: |-
    The distance $r$ is measured perpendicular to the chosen axis.
- id: c
  content: |-
    The value of $I$ can depend on the chosen axis.
- id: d
  content: |-
    A density relation can express $dm$ in terms of a geometric element.
- id: e
  content: |-
    The distance $r$ is always measured from the object's center of mass, regardless of the axis.
  correct: true
```

---

<a id="summary"></a>
## Summary

**Cue:** You are asked what $I=\int r^2\,dm$ means or how its pieces relate to an object's mass distribution.

**Rule:** Add every mass contribution $r^2dm$, where $r$ is measured perpendicular to the chosen axis.

**Procedure:**

1. Identify the chosen rotation axis.
2. Measure $r$ as each mass element's shortest perpendicular distance to that axis.
3. Add $r^2dm$ over every mass element in the object or system.
4. Replace $dm$ with $\lambda\,ds$, $\sigma\,dA$, or $\rho\,dV$ when a density describes a continuous object.
5. Replace the integral with $\sum m_i r_i^2$ for discrete point-like masses.

**Check:** The units of $I$ are mass·length². The main trap is using a slanted distance, a distance from the center of mass, or a familiar object dimension instead of the perpendicular distance to the specified axis.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
