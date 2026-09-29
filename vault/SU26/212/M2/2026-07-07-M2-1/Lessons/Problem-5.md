# Bounding the Center of Mass of Two Unequal Cubes

<!--
lesson-id: 212-M2-005
topic-code: MTH212.M2.05
-->

## Table of Contents

- [Introduction](#introduction)
- [Locate the Center of Each Cube](#locate-the-center-of-each-cube)
- [Turn Side Lengths into a Mass Ratio](#turn-side-lengths-into-a-mass-ratio)
- [Measure the Shift Toward the Smaller Cube](#measure-the-shift-toward-the-smaller-cube)
- [Apply the Bound to the Composite Cubes](#apply-the-bound-to-the-composite-cubes)
- [Summary](#summary)

## Prerequisites

- Find the midpoint of an interval.
- Use $V=s^3$ for the volume of a cube.
- Interpret a weighted average on a number line.

---

<a id="introduction"></a>
## Introduction

For two objects on the $x$-axis,

$$
x_{\mathrm{cm}}=\frac{m_1x_1+m_2x_2}{m_1+m_2}.
$$

If both masses are positive and $x_1<x_2$, then their combined center of mass lies strictly between their centers:

$$
x_1<x_{\mathrm{cm}}<x_2.
$$

It lies closer to the center of the more massive object.

The normalized weights make the geometry visible:

$$
x_{\mathrm{cm}}
=\left(\frac{m_1}{m_1+m_2}\right)x_1
+\left(\frac{m_2}{m_1+m_2}\right)x_2.
$$

Both weights are positive and add to $1$, so this is a weighted point between $x_1$ and $x_2$, not a point outside them.

**Recognition cue:** When a problem asks where the center of mass lies rather than requesting a decimal value, locate the component centers, compare their masses, and use the weighted shift from the heavier component to select the correct interval.

---

<a id="locate-the-center-of-each-cube"></a>
## Locate the Center of Each Cube

**Example:** A uniform cube extends horizontally from $x=0$ to $x=2L$. Find its center coordinate.

**Explanation**

The center is the midpoint of the horizontal edges:

$$
x_1=\frac{0+2L}{2}=L.
$$

A second cube extending from $x=2L$ to $x=3L$ would have center

$$
x_2=\frac{2L+3L}{2}=\frac{5L}{2}.
$$

Use the center of each cube, not the face where the cubes meet.

```quiz
type: radio
id: p5-cube-center
content: |-
  A uniform cube extends horizontally from $x=3L$ to $x=5L$. Where is its center?
options:
- id: p5-cube-center-a
  content: |-
    $x=2L$
- id: p5-cube-center-b
  content: |-
    $x=3L$
- id: p5-cube-center-c
  content: |-
    $x=4L$
  correct: true
- id: p5-cube-center-d
  content: |-
    $x=5L$
```

---

<a id="turn-side-lengths-into-a-mass-ratio"></a>
## Turn Side Lengths into a Mass Ratio

**Example:** Two solid cubes have the same constant density $\rho$. One has side length $2L$ and the other has side length $L$. Compare their masses.

**Explanation**

At equal density, mass is proportional to volume. Since $V=s^3$,

$$
m_1=\rho(2L)^3=8\rho L^3,
\qquad
m_2=\rho L^3.
$$

Therefore,

$$
m_1:m_2=8:1.
$$

Doubling a cube's side length multiplies its mass by $2^3=8$, not by $2$.

```quiz
type: radio
id: p5-mass-ratio
content: |-
  Two solid cubes have the same density. Cube A has side length $3L$, and Cube B has side length $L$. What is $m_A:m_B$?
options:
- id: p5-mass-ratio-a
  content: |-
    $3:1$
- id: p5-mass-ratio-b
  content: |-
    $6:1$
- id: p5-mass-ratio-c
  content: |-
    $9:1$
- id: p5-mass-ratio-d
  content: |-
    $27:1$
  correct: true
```

---

<a id="measure-the-shift-toward-the-smaller-cube"></a>
## Measure the Shift Toward the Smaller Cube

**Example:** A mass $4m$ is centered at $x=L$, and a mass $m$ is centered at $x=3L$. Determine the combined center of mass.

**Explanation**

Starting from the heavier object's center, write the weighted average as a shift:

$$
x_{\mathrm{cm}}
=x_1+\frac{m_2}{m_1+m_2}(x_2-x_1).
$$

Here, the smaller mass moves the center by one-fifth of the separation:

$$
x_{\mathrm{cm}}
=L+\frac{m}{4m+m}(3L-L)
=L+\frac{2L}{5}
=\frac{7L}{5}.
$$

Thus,

$$
L<x_{\mathrm{cm}}<2L.
$$

The center moves toward the smaller cube, but only by the smaller cube's fraction of the total mass.

The shift form gives a fast interval test. If the shift from $x_1=L$ is positive but smaller than $L$, then

$$
L<x_{\mathrm{cm}}<2L.
$$

This proves the requested interval without needing a decimal approximation.

```quiz
type: radio
id: p5-weighted-shift
content: |-
  A mass $5m$ is centered at $x=L$, and a mass $m$ is centered at $x=4L$. Where is their combined center of mass?
options:
- id: p5-weighted-shift-a
  content: |-
    $x_{\mathrm{cm}}=L$
- id: p5-weighted-shift-b
  content: |-
    $x_{\mathrm{cm}}=\dfrac{3L}{2}$
  correct: true
- id: p5-weighted-shift-c
  content: |-
    $x_{\mathrm{cm}}=\dfrac{5L}{2}$
- id: p5-weighted-shift-d
  content: |-
    $x_{\mathrm{cm}}=4L$
```

---

<a id="apply-the-bound-to-the-composite-cubes"></a>
## Apply the Bound to the Composite Cubes

**Source problem**

For the same constant-density cubic blocks, where should the center of mass $x_{\mathrm{cm}}$ lie relative to the origin at the left edge of the large block?

![](<../Source/Images/composite-cubes.png>)

**Explanation**

The large cube extends from $0$ to $2L$, so its center is at

$$
x_1=L.
$$

The smaller cube extends from $2L$ to $3L$, so its center is at

$$
x_2=\frac{5L}{2}.
$$

Collect the geometry and weights before choosing an interval:

| Component | Side length | Mass | Center | Fraction of total mass |
|---|---:|---:|---:|---:|
| Large cube | $2L$ | $8\rho L^3$ | $L$ | $8/9$ |
| Small cube | $L$ | $\rho L^3$ | $5L/2$ | $1/9$ |

The normalized weights give the equivalent weighted-location calculation

$$
x_{\mathrm{cm}}
=\frac89L+\frac19\left(\frac{5L}{2}\right).
$$

At constant density, their masses are $8\rho L^3$ and $\rho L^3$. The smaller cube therefore shifts the center by one-ninth of the separation between the component centers:

$$
\begin{aligned}
x_{\mathrm{cm}}
&=L+\frac{1}{8+1}\left(\frac{5L}{2}-L\right)\\
&=L+\frac{L}{6}\\
&=\frac{7L}{6}.
\end{aligned}
$$

Before even simplifying the fraction, the shift is positive, so $x_{\mathrm{cm}}>L$. It is also

$$
\frac19\left(\frac{5L}{2}-L\right)=\frac{L}{6}<L,
$$

so $x_{\mathrm{cm}}=L+\text{shift}<2L$.

Since

$$
L<\frac{7L}{6}<2L,
$$

the correct interval is $L<x_{\mathrm{cm}}<2L$.

```quiz
type: radio
id: m2-1lec-q4
content: |-
  **Question 4**

  For the same constant-density cubic blocks, where should the center of mass $x_{\mathrm{cm}}$ lie relative to the origin at the left edge of the large block?

  ![](<../Source/Images/composite-cubes.png>)
options:
- id: a
  content: |-
    $x_{\mathrm{cm}}<L$
- id: b
  content: |-
    $x_{\mathrm{cm}}=L$
- id: c
  content: |-
    $L<x_{\mathrm{cm}}<2L$
  correct: true
  feedback: |-
    The large cube alone has its center of mass at $x=L$. Adding the smaller cube on the right shifts the combined center of mass to the right of $L$, but the much larger mass of the large cube keeps it to the left of $2L$.
- id: d
  content: |-
    $x_{\mathrm{cm}}=2L$
- id: e
  content: |-
    $2L<x_{\mathrm{cm}}<3L$
```

---

<a id="summary"></a>
## Summary

For two constant-density cubes:

1. Locate each cube's center from the midpoint of its horizontal span.
2. Convert side lengths to masses using $m=\rho s^3$.
3. Place the combined center between the two component centers and closer to the heavier cube.
4. Rewrite the masses as positive fractions of the total; the fractions must add to $1$.
5. If an interval boundary needs proof, use the shift form

$$
x_{\mathrm{cm}}=x_1+\frac{m_2}{m_1+m_2}(x_2-x_1).
$$

The main traps are using the touching face as a component center, treating the mass ratio as a side-length ratio, or placing the combined center at the midpoint when the masses are unequal.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
