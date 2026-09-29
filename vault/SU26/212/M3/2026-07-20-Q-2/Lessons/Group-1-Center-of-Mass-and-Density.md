# Locate a System's Center of Mass

<!--
lesson-id: 212-M3-024
topic-code: MTH212.M3.24
-->

## Table of Contents

- [Introduction](#introduction)
- [Average Positions Using Mass as the Weight](#average-positions-using-mass-as-the-weight)
- [Replace Groups by Equivalent Point Masses](#replace-groups-by-equivalent-point-masses)
- [Turn Geometry into Mass](#turn-geometry-into-mass)
- [Convert Density into a Mass Element](#convert-density-into-a-mass-element)
- [Check the Result with Balance and Bounds](#check-the-result-with-balance-and-bounds)
- [Summary](#summary)

## Prerequisites

- Solve a linear equation.
- Evaluate basic polynomial integrals.
- Find the center and volume of a uniform geometric object.
- Compute a torque magnitude when a force is perpendicular to its lever arm.

---

<a id="introduction"></a>
## Introduction

When a problem asks where a collection or distributed object balances, locate each piece of mass, weight its position by its mass, and divide by the total mass.

For discrete pieces,

$$
\vec{r}_{\mathrm{cm}}=\frac{\sum_i m_i\vec{r}_i}{\sum_i m_i}.
$$

For a continuous distribution,

$$
\vec{r}_{\mathrm{cm}}=\frac{1}{M}\int \vec{r}\,dm.
$$

The machinery changes from a sum to an integral, but the move does not change: accumulate **mass times position**, then divide by total mass.

**Recognition cue:** A finite list of masses calls for a sum. A phrase such as “density varies with position” calls for a mass element first, then an integral. Geometry is the bridge when dimensions are given but masses are not.

---

<a id="average-positions-using-mass-as-the-weight"></a>
## Average Positions Using Mass as the Weight

**Example:** Two point masses lie on the $x$-axis. Put $m_1=3m$ at $x_1=0$ and $m_2=m$ at $x_2=L$. Find $x_{\mathrm{cm}}$.

**Explanation**

Start from the one-dimensional weighted average:

$$
x_{\mathrm{cm}}=\frac{m_1x_1+m_2x_2}{m_1+m_2}.
$$

Substitute the mass and position of each object:

$$
x_{\mathrm{cm}}=\frac{(3m)(0)+(m)(L)}{3m+m}=\frac{L}{4}.
$$

The result lies closer to the larger mass. That is a required physical check, not a coincidence.

```quiz
type: radio
id: cm-density-q1
shuffle: true
content: |-
  A point mass $4m$ is at $x=0$, and a point mass $m$ is at $x=L$. Where is the center of mass?
options:
- id: cm-density-q1-a
  content: |-
    $\dfrac{L}{5}$
  correct: true
  feedback: |-
    The numerator is $mL$, while the total mass is $5m$.
- id: cm-density-q1-b
  content: |-
    $\dfrac{L}{4}$
  feedback: |-
    This divides by the larger mass instead of the total mass.
- id: cm-density-q1-c
  content: |-
    $\dfrac{4L}{5}$
  feedback: |-
    This places the center closer to the smaller mass.
- id: cm-density-q1-d
  content: |-
    $\dfrac{L}{2}$
  feedback: |-
    The midpoint applies only when the masses are equal.
```

---

<a id="replace-groups-by-equivalent-point-masses"></a>
## Replace Groups by Equivalent Point Masses

**Example:** Six identical blocks have their group center at $x=1.5\ \mathrm{cm}$, two at $x=4.0\ \mathrm{cm}$, and two at $x=5.5\ \mathrm{cm}$. Find the center of mass of all ten blocks.

**Explanation**

Replace each group by one equivalent point mass at that group's center:

$$
x_{\mathrm{cm}}
=
\frac{6m(1.5)+2m(4.0)+2m(5.5)}{10m}.
$$

The common block mass cancels:

$$
x_{\mathrm{cm}}=\frac{9+8+11}{10}\ \mathrm{cm}=2.8\ \mathrm{cm}.
$$

Grouping is valid because the center of mass of each group already captures how that group's mass is positioned.

```quiz
type: radio
id: cm-density-q2
shuffle: true
content: |-
  Four identical objects have their group center at $x=1\ \mathrm{m}$, and two identical objects have their group center at $x=5\ \mathrm{m}$. What is the center of mass of all six objects?
options:
- id: cm-density-q2-a
  content: |-
    $\dfrac{7}{3}\ \mathrm{m}$
  correct: true
  feedback: |-
    Use $[4m(1)+2m(5)]/(6m)=14/6$.
- id: cm-density-q2-b
  content: |-
    $3\ \mathrm{m}$
  feedback: |-
    This averages the two group positions without weighting their different masses.
- id: cm-density-q2-c
  content: |-
    $\dfrac{5}{3}\ \mathrm{m}$
  feedback: |-
    This underweights the group at $x=5\ \mathrm{m}$.
- id: cm-density-q2-d
  content: |-
    $4\ \mathrm{m}$
  feedback: |-
    The larger group is on the left, so the result must be closer to $1\ \mathrm{m}$ than to $5\ \mathrm{m}$.
```

---

<a id="turn-geometry-into-mass"></a>
## Turn Geometry into Mass

**Example:** A cube of side $2L$ is attached to a cube of side $L$. Both have uniform density $\rho$. Put the origin at the left face of the large cube. Find the composite center of mass.

**Explanation**

Use $m=\rho V$ to turn each volume into a mass:

$$
m_1=\rho(2L)^3=8\rho L^3,\qquad m_2=\rho L^3.
$$

The centers are at

$$
x_1=L,\qquad x_2=2L+\frac{L}{2}=\frac{5L}{2}.
$$

Now use the same discrete weighted average:

$$
x_{\mathrm{cm}}
=
\frac{(8\rho L^3)(L)+(\rho L^3)(5L/2)}{9\rho L^3}
=
\frac{7L}{6}.
$$

The density cancels because both pieces have the same density.

```quiz
type: radio
id: cm-density-q3
shuffle: true
content: |-
  Two uniform cubes made from the same material have side lengths $2L$ and $L$. What mass ratio should be used in a center-of-mass calculation?
options:
- id: cm-density-q3-a
  content: |-
    $m_{\mathrm{large}}:m_{\mathrm{small}}=8:1$
  correct: true
  feedback: |-
    For equal density, mass scales with volume, and $(2L)^3:L^3=8:1$.
- id: cm-density-q3-b
  content: |-
    $m_{\mathrm{large}}:m_{\mathrm{small}}=4:1$
  feedback: |-
    This uses area rather than volume.
- id: cm-density-q3-c
  content: |-
    $m_{\mathrm{large}}:m_{\mathrm{small}}=2:1$
  feedback: |-
    This uses side length rather than volume.
- id: cm-density-q3-d
  content: |-
    $m_{\mathrm{large}}:m_{\mathrm{small}}=1:1$
  feedback: |-
    Equal density does not imply equal mass when the volumes differ.
```

---

<a id="convert-density-into-a-mass-element"></a>
## Convert Density into a Mass Element

**Example:** A rod occupies $0\le x\le L$ and has linear density $\lambda(x)=Cx$. Its total mass is $M$. Find $C$ and $x_{\mathrm{cm}}$.

**Explanation**

1. **Build the mass element.** Translate density into a small mass:

$$
dm=\lambda(x)\,dx=Cx\,dx.
$$

2. **Normalize the density.** Use the stated total mass:

$$
M=\int_0^L dm=\int_0^L Cx\,dx=\frac{CL^2}{2},
$$

so

$$
C=\frac{2M}{L^2}.
$$

3. **Compute the weighted position.** Only now form the requested moment:

$$
x_{\mathrm{cm}}
=
\frac{1}{M}\int_0^L x\,dm
=
\frac{C}{M}\int_0^L x^2\,dx
=
\frac{CL^3}{3M}
=
\frac{2L}{3}.
$$

The order matters: normalize $C$ first, then calculate the requested moment of the distribution.

```quiz
type: radio
id: cm-density-q4
shuffle: true
content: |-
  A rod on $0\le x\le L$ has linear density $\lambda(x)=Cx^2$ and total mass $M$. Where is its center of mass?
options:
- id: cm-density-q4-a
  content: |-
    $\dfrac{3L}{4}$
  correct: true
  feedback: |-
    Normalization gives $C=3M/L^3$, and $(1/M)\int_0^L x(Cx^2)\,dx=3L/4$.
- id: cm-density-q4-b
  content: |-
    $\dfrac{2L}{3}$
  feedback: |-
    This is the result for $\lambda(x)\propto x$, not $x^2$.
- id: cm-density-q4-c
  content: |-
    $\dfrac{L}{2}$
  feedback: |-
    The density is not uniform; it increases toward $x=L$.
- id: cm-density-q4-d
  content: |-
    $\dfrac{L}{4}$
  feedback: |-
    This places the center toward the low-density end.
```

---

<a id="check-the-result-with-balance-and-bounds"></a>
## Check the Result with Balance and Bounds

**Example:** Two masses $m_1$ and $m_2$ are separated by $L$, with $m_1$ at $x=0$. Show that supporting them at their center of mass also balances their torques.

**Explanation**

If the support is at $x_{\mathrm{cm}}$, the two lever arms are $x_{\mathrm{cm}}$ and $L-x_{\mathrm{cm}}$. Balance requires

$$
m_1g x_{\mathrm{cm}}=m_2g(L-x_{\mathrm{cm}}).
$$

Solving gives

$$
x_{\mathrm{cm}}=\frac{m_2L}{m_1+m_2},
$$

which is exactly the weighted-average result. Use three quick checks:

1. The answer lies inside the occupied region.
2. It lies closer to the greater concentration of mass.
3. Clockwise and counterclockwise torques balance about it.

```quiz
type: radio
id: cm-density-q5
shuffle: true
content: |-
  A rod on $0\le x\le L$ has positive density that steadily increases with $x$. Which interval must contain its center of mass?
options:
- id: cm-density-q5-a
  content: |-
    $0<x_{\mathrm{cm}}<\dfrac{L}{2}$
- id: cm-density-q5-b
  content: |-
    $x_{\mathrm{cm}}=\dfrac{L}{2}$
- id: cm-density-q5-c
  content: |-
    $\dfrac{L}{2}<x_{\mathrm{cm}}<L$
  correct: true
  feedback: |-
    More mass lies toward the right end, so the weighted average shifts right of the midpoint while remaining inside the rod.
- id: cm-density-q5-d
  content: |-
    $x_{\mathrm{cm}}>L$
  feedback: |-
    A positive mass distribution cannot have its center of mass outside its occupied interval.
```

---

<a id="summary"></a>
## Summary

When asked where a system balances:

1. Choose one origin and measure every position from it.
2. Replace each uniform piece or group by its mass at its own center.
3. Use $\vec{r}_{\mathrm{cm}}=\sum m_i\vec{r}_i/\sum m_i$ for discrete pieces.
4. For a distribution, write $dm$ from its density, normalize with $M=\int dm$, and use $\vec{r}_{\mathrm{cm}}=(1/M)\int\vec{r}\,dm$.
5. Check that the result lies near the greater concentration of mass and gives zero net torque when used as the support point.

The main trap is averaging positions without weighting them by mass.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
