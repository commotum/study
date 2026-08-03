# Combining Equal Gravitational Forces in an Equilateral Triangle

<!--
lesson-id: 212-M3-008
topic-code: MTH212.M3.08
-->

## Table of Contents

- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Calculate One Pairwise Gravitational Force](#calculate-one-pairwise-gravitational-force)
- [Use the Triangle Geometry to Set the Angle](#use-the-triangle-geometry-to-set-the-angle)
- [Add the Two Equal Force Vectors](#add-the-two-equal-force-vectors)
- [Convert to Yottanewtons and Round](#convert-to-yottanewtons-and-round)
- [Apply the Method](#apply-the-method)
- [Summary](#summary)

## Prerequisites

- Apply Newton's law of gravitation to two point masses.
- Read side lengths, angles, and symmetry from an equilateral triangle.
- Resolve and add vector components, then convert scientific-notation units and round to the given precision.

<a id="introduction"></a>

## Introduction

The recognition cue is a mass pulled by two equal gravitational forces along two sides of an equilateral triangle, so the vectors have equal magnitude and are separated by $60^\circ$. The single vector-addition move is to use the angle bisector as the symmetry axis: the perpendicular components cancel and the parallel components add, giving $F_{\text{net}}=2F_{\text{pair}}\cos30^\circ=\sqrt3F_{\text{pair}}$.

When several masses attract one another, the forces must be added as **vectors**. For one mass at a corner of an equilateral triangle, the other two masses pull with equal force magnitudes in directions separated by $60^\circ$.

The efficient path is:

1. calculate the force from either one of the other masses;
2. use the triangle geometry to identify the angle between the two forces;
3. add the two force vectors along their symmetry axis;
4. convert units and round at the end.

## Calculate One Pairwise Gravitational Force

For two masses $m_1$ and $m_2$ separated by distance $r$, Newton's law of gravitation gives

$$
F=\frac{Gm_1m_2}{r^2}.
$$

Here, every mass is $m$ and every side has length $L$, so either one of the other masses exerts a force of magnitude

$$
F_{\text{pair}}=\frac{Gm^2}{L^2}.
$$

Both pairwise forces have this same magnitude, but they point in different directions. Calculating $F_{\text{pair}}$ is therefore only the first step.

**Practice 1**

```quiz
type: radio
id: m3-2-p4-pairwise-force
content: |-
  Three equal masses $m$ lie at the corners of an equilateral triangle of side length $L$. What is the magnitude of the gravitational force that either one of the other masses exerts on a chosen mass?
options:
- id: a
  content: |-
    $\dfrac{Gm^2}{L^2}$
  correct: true
  feedback: |-
    Apply Newton's law to one pair of equal masses separated by one side length: $F_{\text{pair}}=Gm^2/L^2$. The other mass produces a second force of the same magnitude, which must be combined later as a vector.
- id: b
  content: |-
    $\dfrac{2Gm^2}{L^2}$
- id: c
  content: |-
    $\dfrac{Gm^2}{L}$
- id: d
  content: |-
    $\dfrac{Gm}{L^2}$
```

## Use the Triangle Geometry to Set the Angle

At the chosen corner, each gravitational force points from the chosen mass toward one of the other two corners. The force directions therefore follow the two sides that meet at that corner.

An equilateral triangle has an interior angle of $60^\circ$ at every corner, so the angle **between the force vectors** is $60^\circ$. The line from the chosen corner to the center of the triangle bisects that angle, placing each force $30^\circ$ from the bisector.

| Geometric fact | Force consequence |
|---|---|
| The two adjacent sides both have length $L$ | The two pairwise force magnitudes are equal |
| The sides meet at $60^\circ$ | The force vectors are separated by $60^\circ$ |
| The figure is symmetric about the angle bisector | The resultant lies on that bisector, toward the center |

**Practice 2**

```quiz
type: radio
id: m3-2-p4-force-angle
content: |-
  Two equal gravitational forces act on a mass at one vertex of an equilateral triangle. Relative to the angle bisector through that vertex, which angle description is correct?
options:
- id: a
  content: |-
    The forces are $60^\circ$ apart, and each is $30^\circ$ from the bisector.
  correct: true
  feedback: |-
    Each force follows a side of the equilateral triangle. The sides meet at the $60^\circ$ interior angle, and symmetry divides that angle into two $30^\circ$ angles.
- id: b
  content: |-
    The forces are $30^\circ$ apart, and each is $15^\circ$ from the bisector.
- id: c
  content: |-
    The forces are $120^\circ$ apart, and each is $60^\circ$ from the bisector.
- id: d
  content: |-
    The forces are $180^\circ$ apart and cancel.
```

## Add the Two Equal Force Vectors

Choose an axis along the $60^\circ$ angle bisector. For each force:

- the component along the bisector is $F_{\text{pair}}\cos 30^\circ$;
- the component perpendicular to the bisector has the same magnitude as the other perpendicular component but the opposite direction.

The perpendicular components cancel, while the two components along the bisector add:

$$
\begin{aligned}
F_{\text{net}}
&=2F_{\text{pair}}\cos 30^\circ\\
&=2F_{\text{pair}}\left(\frac{\sqrt3}{2}\right)\\
&=\sqrt3F_{\text{pair}}.
\end{aligned}
$$

Combining this with Newton's law gives the reusable result

$$
\boxed{F_{\text{net}}=\sqrt3\frac{Gm^2}{L^2}}.
$$

The net force points along the angle bisector toward the common center of mass.

As a check, the vector triangle gives the same magnitude through the Law of Cosines:

$$
F_{\text{net}}^2
=F_{\text{pair}}^2+F_{\text{pair}}^2
+2F_{\text{pair}}^2\cos60^\circ
=3F_{\text{pair}}^2.
$$

Also, the two forces are neither parallel nor opposite, so a sensible result must satisfy

$$
F_{\text{pair}}<F_{\text{net}}<2F_{\text{pair}}.
$$

The factor $\sqrt3\approx1.732$ passes this reasonableness check.

**Practice 3**

```quiz
type: radio
id: m3-2-p4-equal-vector-resultant
content: |-
  Two forces of $10.0\ \mathrm{N}$ act at an angle of $60^\circ$ to one another. What is the magnitude of their resultant?
options:
- id: a
  content: |-
    $17.3\ \mathrm{N}$
  correct: true
  feedback: |-
    For equal forces separated by $60^\circ$, $F_{\text{net}}=\sqrt3F=(1.732)(10.0\ \mathrm{N})=17.3\ \mathrm{N}$. Adding the magnitudes to get $20.0\ \mathrm{N}$ would incorrectly treat the forces as parallel.
- id: b
  content: |-
    $20.0\ \mathrm{N}$
- id: c
  content: |-
    $10.0\ \mathrm{N}$
- id: d
  content: |-
    $0\ \mathrm{N}$
```

## Convert to Yottanewtons and Round

Because

$$
1\ \mathrm{YN}=10^{24}\ \mathrm{N},
$$

convert newtons to yottanewtons by dividing the numerical value by $10^{24}$:

$$
F(\mathrm{YN})=\frac{F(\mathrm{N})}{10^{24}}.
$$

Keep extra digits through the force calculation and unit conversion. Then round the final result to the precision supported by the measured inputs.

**Practice 4**

```quiz
type: radio
id: m3-2-p4-yottanewton-conversion
content: |-
  A calculated force is $4.56\times10^{26}\ \mathrm{N}$. Express it in yottanewtons and round to two significant figures.
options:
- id: a
  content: |-
    $460\ \mathrm{YN}$
  correct: true
  feedback: |-
    Dividing by $10^{24}$ gives $456\ \mathrm{YN}$. Rounded to two significant figures, this is $4.6\times10^2\ \mathrm{YN}=460\ \mathrm{YN}$.
- id: b
  content: |-
    $4.6\ \mathrm{YN}$
- id: c
  content: |-
    $46\ \mathrm{YN}$
- id: d
  content: |-
    $4.6\times10^{50}\ \mathrm{YN}$
```

## Apply the Method

Keep the powers of ten visible so that the arithmetic and unit conversion can be checked independently:

| Quantity | Calculation | Value kept for the next step |
|---|---|---|
| $m^2$ | $(2.5\times10^{30})^2$ | $6.25\times10^{60}\ \mathrm{kg^2}$ |
| $L^2$ | $(1.8\times10^{12})^2$ | $3.24\times10^{24}\ \mathrm{m^2}$ |
| $F_{\text{pair}}$ | $Gm^2/L^2$ | $1.2867\times10^{26}\ \mathrm{N}$ |
| $F_{\text{net}}$ | $\sqrt3F_{\text{pair}}$ | $2.2285\times10^{26}\ \mathrm{N}$ |
| Converted force | $F_{\text{net}}/10^{24}$ | $222.85\ldots\ \mathrm{YN}$ |

In equation form, start with one pairwise force:

$$
\begin{aligned}
F_{\text{pair}}
&=\frac{(6.67\times10^{-11})(2.5\times10^{30})^2}{(1.8\times10^{12})^2}\\
&\approx1.2867\times10^{26}\ \mathrm{N}.
\end{aligned}
$$

Then combine the two equal forces:

$$
\begin{aligned}
F_{\text{net}}
&=\sqrt3F_{\text{pair}}\\
&\approx2.2285\times10^{26}\ \mathrm{N}\\
&=222.85\ldots\ \mathrm{YN}.
\end{aligned}
$$

The measured givens have two significant figures, so the final result is $2.2\times10^2\ \mathrm{YN}$, entered as `220`.

Before committing to that result, check that $222.85\ldots\ \mathrm{YN}$ lies between the one-force estimate, about $129\ \mathrm{YN}$, and the parallel-force maximum, about $257\ \mathrm{YN}$. It does.

**Problem 4**

```quiz
type: radio
id: m3-2lec-q3
content: |-
  **Question 3**

  Three equal masses occupy the corners of an equilateral triangle of side length $L$ and move in a stable circular orbit about their common center of mass. Find the net gravitational force on each mass for $m=2.5\times10^{30}\ \mathrm{kg}$ and $L=1.8\times10^{12}\ \mathrm{m}$.

  Enter the force in yottanewtons, where $1\ \mathrm{YN}=10^{24}\ \mathrm{N}$, as a number only:
options:
- id: a
  content: |-
    `220`
  correct: true
  feedback: |-
    Each mass experiences two forces of magnitude

    $$
    F_{\mathrm{pair}}=\frac{Gm^2}{L^2}
    $$

    separated by $60^\circ$. Their resultant is

    $$
    F_{\mathrm{net}}
    =\sqrt{3}\frac{Gm^2}{L^2}
    =2.2285\times10^{26}\ \mathrm{N}
    =222.85\ldots\ \mathrm{YN}.
    $$

    The measured givens have two significant figures, so $F_{\mathrm{net}}=2.2\times10^2\ \mathrm{YN}$, entered as `220`.
- id: b
  content: |-
    `130`
- id: c
  content: |-
    `260`
- id: d
  content: |-
    `2.2`
```

## Summary

- Find one pairwise magnitude with $F_{\text{pair}}=Gm^2/L^2$.
- Read the $60^\circ$ angle between the forces from the equilateral triangle.
- Use symmetry to add the vectors: $F_{\text{net}}=2F_{\text{pair}}\cos30^\circ=\sqrt3F_{\text{pair}}$.
- Convert from newtons to yottanewtons by dividing by $10^{24}$.
- Keep guard digits and round only the final result.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
