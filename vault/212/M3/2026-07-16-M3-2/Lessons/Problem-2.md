# Finding a Two-Body Center of Mass as a Fraction of Separation

<!--
lesson-id: 212-M3-006
topic-code: MTH212.M3.06
-->

## Table of Contents

- [Introduction](#introduction)
- [Assign Coordinates From the Stated Origin](#assign-coordinates-from-the-stated-origin)
- [Form the Mass-Weighted Average](#form-the-mass-weighted-average)
- [Use the Mass-Ratio Shortcut and Check the Location](#use-the-mass-ratio-shortcut-and-check-the-location)
- [Apply the Method to the Binary Star System](#apply-the-method-to-the-binary-star-system)
- [Summary](#summary)

## Prerequisites

- Reading positions on a one-dimensional coordinate line
- Simplifying fractions and ratios
- Understanding an average whose terms have different weights

## Introduction

For two masses on a line, the center-of-mass coordinate is the mass-weighted average

$$
x_{\mathrm{cm}}
=\frac{m_1x_1+m_2x_2}{m_1+m_2}.
$$

Read the structure as

$$
\text{center of mass}
=\frac{\text{sum of mass-position contributions}}{\text{total mass}}.
$$

The main challenge is usually not the arithmetic. It is assigning the positions correctly from the stated origin.

**Recognition cue:** When one object is declared to be the origin and the answer is requested as a fraction of the separation, place that object at $x=0$, place the other at $x=d$, and then divide the center-of-mass formula by $d$.

## Assign Coordinates From the Stated Origin

Suppose two stars have masses $6M$ and $2M$, are separated by $d$, and the larger star is the origin. Then

$$
x_{6M}=0
\qquad\text{and}\qquad
x_{2M}=d.
$$

The number $d$ is the coordinate of the second star because it lies one full separation from the origin. The origin choice fixes the coordinates; the masses do not determine which position is zero.

```quiz
type: radio
id: problem-2-coordinates-q1
content: |-
  Two stars of masses $7M$ and $3M$ are separated by $d$. The $7M$ star is the origin. Which coordinate assignment is correct?
options:
- id: a
  content: |-
    $x_{7M}=0$ and $x_{3M}=d$
  correct: true
  feedback: |-
    The star named as the origin has coordinate $0$, and the other star is one separation $d$ away.
- id: b
  content: |-
    $x_{7M}=d$ and $x_{3M}=0$
  feedback: |-
    This reverses the stated origin.
- id: c
  content: |-
    $x_{7M}=-d$ and $x_{3M}=d$
  feedback: |-
    These positions are $2d$ apart, not $d$ apart.
- id: d
  content: |-
    $x_{7M}=0$ and $x_{3M}=d/2$
  feedback: |-
    The second star is one full separation from the origin, not half a separation.
```

---

## Form the Mass-Weighted Average

Using the $6M$ and $2M$ example,

$$
x_{\mathrm{cm}}
=\frac{(6M)(0)+(2M)(d)}{6M+2M}.
$$

Divide by $d$ to express the location as a fraction of the separation:

$$
\frac{x_{\mathrm{cm}}}{d}
=\frac{(6M)(0)+(2M)(d)}{(6M+2M)d}
=\frac{2}{8}
=0.25.
$$

The common mass scale $M$ and the separation $d$ cancel. Only the relative masses and the origin choice affect the requested fraction.

An ordinary midpoint is the equal-weight special case. If both masses are $M$, with one at $0$ and the other at $d$, then

$$
\frac{x_{\mathrm{cm}}}{d}
=\frac{M(0)+M(d)}{(M+M)d}
=\frac{1}{2}.
$$

Unequal masses pull the center away from the midpoint and toward the larger mass.

```quiz
type: radio
id: problem-2-weighted-average-q1
content: |-
  Two objects have masses $4M$ and $M$. They are separated by $d$, and the $4M$ object is at the origin. What is $x_{\mathrm{cm}}/d$?
options:
- id: a
  content: |-
    $0.20$
  correct: true
  feedback: |-
    $\dfrac{x_{\mathrm{cm}}}{d}=\dfrac{(4M)(0)+(M)(d)}{(4M+M)d}=\dfrac{1}{5}=0.20$.
- id: b
  content: |-
    $0.50$
  feedback: |-
    The midpoint is correct only when the two masses are equal.
- id: c
  content: |-
    $0.80$
  feedback: |-
    This is the result for the same masses with the origin placed at the smaller object.
- id: d
  content: |-
    $4.0$
  feedback: |-
    A mass ratio by itself is not the center-of-mass position as a fraction of the separation.
```

---

## Use the Mass-Ratio Shortcut and Check the Location

If the mass at the origin is $M$ and the mass at $x=d$ is $m$, then

$$
\frac{x_{\mathrm{cm}}}{d}
=\frac{M(0)+m(d)}{(M+m)d}
=\frac{m}{M+m}.
$$

The numerator is the mass at the far position $x=d$, not automatically the larger or smaller mass.

**Order check:** For a fraction measured from the origin, use

$$
\frac{\text{mass at }d}{\text{mass at }0+\text{mass at }d}.
$$

This form gives two quick checks:

1. The fraction must be between $0$ and $1$, because the center of mass lies between the objects.
2. The center of mass must be closer to the larger mass.

For example, if the smaller mass $M$ is the origin and a larger mass $4M$ is at $x=d$, then

$$
\frac{x_{\mathrm{cm}}}{d}
=\frac{4M}{M+4M}
=0.80.
$$

The center of mass is $0.80d$ from the smaller origin, so it is only $0.20d$ from the larger mass.

```quiz
type: radio
id: problem-2-origin-check-q1
content: |-
  Two objects have masses $M$ and $3M$. The smaller object is the origin, and the larger object is at $x=d$. What is $x_{\mathrm{cm}}/d$?
options:
- id: a
  content: |-
    $0.75$
  correct: true
  feedback: |-
    The mass at $x=d$ is $3M$, so $\dfrac{x_{\mathrm{cm}}}{d}=\dfrac{3M}{M+3M}=\dfrac{3}{4}=0.75$.
- id: b
  content: |-
    $0.25$
  feedback: |-
    This would result from putting the larger mass at the origin instead.
- id: c
  content: |-
    $0.50$
  feedback: |-
    The midpoint applies only to equal masses.
- id: d
  content: |-
    $3.0$
  feedback: |-
    This is the ratio of the masses, but a position between the objects must have $0<x_{\mathrm{cm}}/d<1$.
```

---

## Apply the Method to the Binary Star System

The larger star is the origin. Record each mass and position before substituting:

| Star | Mass | Position | Mass-position contribution |
|---|---:|---:|---:|
| Larger star | $5.0\times10^{30}\ \mathrm{kg}$ | $0$ | $0$ |
| Smaller star | $2.5\times10^{30}\ \mathrm{kg}$ | $d$ | $(2.5\times10^{30}\ \mathrm{kg})d$ |

Thus,

$$
x_{5.0\times10^{30}\,\mathrm{kg}}=0
\qquad\text{and}\qquad
x_{2.5\times10^{30}\,\mathrm{kg}}=d.
$$

Substitute these positions into the weighted-average formula:

$$
\frac{x_{\mathrm{cm}}}{d}
=\frac{(5.0\times10^{30})(0)+(2.5\times10^{30})d}
{(5.0\times10^{30}+2.5\times10^{30})d}.
$$

The factors $10^{30}\ \mathrm{kg}$ and $d$ cancel:

$$
\frac{x_{\mathrm{cm}}}{d}
=\frac{2.5}{5.0+2.5}
=\frac{2.5}{7.5}
=0.3333\ldots
\approx 0.33.
$$

The numerical value $d=3.0\times10^{12}\ \mathrm{m}$ is therefore not needed when the answer is requested as $x_{\mathrm{cm}}/d$. The given masses have two significant figures, so the result is $0.33$. It lies between $0$ and $1$, and it is closer to the larger star at the origin than to the smaller star at $x=d$.

```quiz
type: radio
id: m3-2lec-q1
content: |-
  **Question 1**

  A binary star system contains stars of masses $2.5\times10^{30}\ \mathrm{kg}$ and $5.0\times10^{30}\ \mathrm{kg}$ separated by a distance $d=3.0\times10^{12}\ \mathrm{m}$. Use the larger star's position as the origin. Find the center-of-mass position as a fraction of the separation.

  Enter $x_{\mathrm{cm}}/d$ as a number only:
options:
- id: a
  content: |-
    $0.33$
  correct: true
  feedback: |-
    Place the $5.0\times10^{30}\ \mathrm{kg}$ star at $x=0$ and the $2.5\times10^{30}\ \mathrm{kg}$ star at $x=d$. Then

    $$
    \frac{x_{\mathrm{cm}}}{d}
    =\frac{(5.0)(0)+(2.5)d}{(5.0+2.5)d}
    =\frac{2.5}{7.5}
    =0.3333\ldots.
    $$

    The masses have two significant figures, so $x_{\mathrm{cm}}/d=0.33$. The center of mass lies one-third of the separation from the larger star toward the smaller star.
- id: b
  content: |-
    $0.67$
  feedback: |-
    This reverses the origin. A value of $0.67$ would measure from the smaller star toward the larger star.
- id: c
  content: |-
    $0.50$
  feedback: |-
    The midpoint would be correct only if the stars had equal masses.
- id: d
  content: |-
    $2.0$
  feedback: |-
    This is a ratio of the larger mass to the smaller mass, not a position fraction. The center-of-mass fraction must lie between $0$ and $1$.
```

---

## Summary

To find the center of mass as a fraction of a two-object separation:

1. Put the object named as the origin at $x=0$.
2. Put the other object at $x=d$.
3. Substitute into $x_{\mathrm{cm}}=(m_1x_1+m_2x_2)/(m_1+m_2)$.
4. Divide by $d$ and cancel common scales.
5. Check that the fraction lies between $0$ and $1$ and is closer to the larger mass.

With mass $M$ at the origin and mass $m$ at $x=d$, the shortcut is

$$
\boxed{\frac{x_{\mathrm{cm}}}{d}=\frac{m}{M+m}}.
$$

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Finding the Orbital Period of a Binary Star System](Problem-3.md)

Study guide index: 16/20

---
<!-- lesson-nav:end -->
