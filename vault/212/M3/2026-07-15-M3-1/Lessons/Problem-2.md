# Gravity at Altitude as a Fraction of Surface Gravity

<!--
lesson-id: 212-M3-002
topic-code: MTH212.M3.02
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Altitude to Distance From the Center](#convert-altitude-to-distance-from-the-center)
- [Build the Inverse-Square Ratio](#build-the-inverse-square-ratio)
- [Use a Radius Factor and Check the Result](#use-a-radius-factor-and-check-the-result)
- [Apply the Method to the Satellite](#apply-the-method-to-the-satellite)
- [Summary](#summary)

## Prerequisites

- Adding a whole number and a fraction
- Writing and simplifying ratios
- Squaring fractions
- Gravitational acceleration: $g=GM/r^2$

---

## Introduction

Outside a spherical planet, gravitational acceleration depends on distance from the planet's center:

$$
g(r)=\frac{GM}{r^2}.
$$

An altitude is measured from the surface, not from the center. Therefore, the essential first move is

$$
r=r_E+h,
$$

where $r_E$ is Earth's radius and $h$ is the altitude.

**Recognition cue:** When an altitude is given as a fraction of Earth's radius and the answer is requested in units of surface gravity, first convert the altitude to a center-to-satellite radius, then compare the two inverse-square expressions as a ratio.

---

## Convert Altitude to Distance From the Center

**Example:** A satellite's altitude is $h=\frac12r_E$. Express its distance $r$ from Earth's center in terms of $r_E$.

**Explanation**

Add Earth's radius to the altitude:

$$
\begin{aligned}
r
&=r_E+h\\
&=r_E+\frac12r_E\\
&=\left(1+\frac12\right)r_E\\
&=\frac32r_E.
\end{aligned}
$$

Writing $1=\frac22$ makes the fraction addition explicit:

$$
1+\frac12=\frac22+\frac12=\frac32.
$$

The satellite is $\frac12r_E$ above the surface but $\frac32r_E$ from the center.

```quiz
type: radio
id: problem-2-center-distance-q1
content: |-
  A satellite is at altitude $h=\frac14r_E$. What is its distance $r$ from Earth's center?
options:
- id: a
  content: |-
    $r=\dfrac54r_E$
  correct: true
  feedback: |-
    $r=r_E+h=(1+\frac14)r_E=\frac54r_E$.
- id: b
  content: |-
    $r=\dfrac14r_E$
  feedback: |-
    This is the altitude above the surface, not the distance from Earth's center.
- id: c
  content: |-
    $r=\dfrac34r_E$
  feedback: |-
    This subtracts the altitude from Earth's radius instead of adding it.
- id: d
  content: |-
    $r=\dfrac45r_E$
  feedback: |-
    This takes the reciprocal of the correct radius factor.
- id: e
  content: |-
    $r=4r_E$
  feedback: |-
    The fraction $\frac14$ does not mean the satellite is four Earth radii from the center.
```

---

## Build the Inverse-Square Ratio

**Example:** A satellite is at center-to-center distance $r=2r_E$. Find its gravitational acceleration as a fraction of surface gravity.

**Explanation**

At Earth's surface,

$$
g=\frac{GM_E}{r_E^2}.
$$

At the satellite,

$$
g_h=\frac{GM_E}{r^2}.
$$

Divide the satellite value by the surface value:

$$
\begin{aligned}
\frac{g_h}{g}
&=\frac{GM_E/r^2}{GM_E/r_E^2}\\
&=\frac{r_E^2}{r^2}\\
&=\left(\frac{r_E}{r}\right)^2.
\end{aligned}
$$

The requested order is $g_h/g$, so the satellite expression belongs in the numerator and the surface expression belongs in the denominator. Reversing those positions produces the reciprocal answer.

For $r=2r_E$,

$$
\frac{g_h}{g}
=\left(\frac{r_E}{2r_E}\right)^2
=\left(\frac12\right)^2
=\frac14.
$$

The factors $G$, $M_E$, and $r_E^2$ cancel, so their numerical values are not needed.

```quiz
type: radio
id: problem-2-inverse-square-q1
content: |-
  A spacecraft is at distance $r=3r_E$ from Earth's center. What is $g_h/g$?
options:
- id: a
  content: |-
    $\dfrac19$
  correct: true
  feedback: |-
    $\dfrac{g_h}{g}=(\frac{r_E}{3r_E})^2=(\frac13)^2=\frac19$.
- id: b
  content: |-
    $\dfrac13$
  feedback: |-
    This uses inverse variation but forgets that gravity follows an inverse-square law.
- id: c
  content: |-
    $3$
  feedback: |-
    Gravity decreases rather than increases as distance from the center increases.
- id: d
  content: |-
    $9$
  feedback: |-
    This reverses the ratio and squares it.
- id: e
  content: |-
    $\dfrac23$
  feedback: |-
    This does not follow from the inverse-square ratio.
```

---

## Use a Radius Factor and Check the Result

**Example:** Write a direct formula when the altitude is $h=\alpha r_E$.

**Explanation**

First convert altitude to radius:

$$
r=r_E+\alpha r_E=(1+\alpha)r_E.
$$

Then substitute into the gravity ratio:

$$
\begin{aligned}
\frac{g_h}{g}
&=\left(\frac{r_E}{(1+\alpha)r_E}\right)^2\\
&=\frac{1}{(1+\alpha)^2}.
\end{aligned}
$$

This produces a reusable factor chain:

| Start with | Convert to | Then compute |
|---|---|---|
| Altitude factor $\alpha$ | Radius factor $1+\alpha$ | Gravity factor $1/(1+\alpha)^2$ |

For example, if $h=\frac12r_E$, then

$$
\frac{g_h}{g}
=\frac{1}{(1+\frac12)^2}
=\left(\frac23\right)^2
=\frac49.
$$

**Check:** A positive altitude makes $r>r_E$, so the ratio must satisfy $0<g_h/g<1$. A result greater than $1$ usually means altitude was used in place of distance from the center or the ratio was reversed.

```quiz
type: radio
id: problem-2-radius-factor-q1
content: |-
  A satellite's altitude is $h=\frac32r_E$. What is $g_h/g$?
options:
- id: a
  content: |-
    $0.16$
  correct: true
  feedback: |-
    $r=(1+\frac32)r_E=\frac52r_E$, so $g_h/g=(\frac25)^2=\frac4{25}=0.16$.
- id: b
  content: |-
    $0.40$
  feedback: |-
    This correctly finds the reciprocal radius factor $\frac25$ but forgets to square it.
- id: c
  content: |-
    $0.44$
  feedback: |-
    This approximately squares $\frac23$, which incorrectly uses the altitude factor instead of the full radius factor.
- id: d
  content: |-
    $2.5$
  feedback: |-
    This is the center-distance factor, not the gravity ratio.
- id: e
  content: |-
    $6.25$
  feedback: |-
    This reverses the inverse-square ratio.
```

---

## Apply the Method to the Satellite

**Example:** A satellite is at altitude $h=\frac13r_E$. Find $g_h/g$ to two significant figures.

**Explanation**

The distance from Earth's center is

$$
r
=r_E+\frac13r_E
=\left(\frac33+\frac13\right)r_E
=\frac43r_E.
$$

Apply the inverse-square ratio:

$$
\begin{aligned}
\frac{g_h}{g}
&=\left(\frac{r_E}{r}\right)^2\\
&=\left(\frac{r_E}{\frac43r_E}\right)^2\\
&=\left(\frac34\right)^2\\
&=\frac9{16}\\
&=0.5625.
\end{aligned}
$$

The square applies to the whole fraction:

$$
\left(\frac34\right)^2=\frac{3^2}{4^2}=\frac9{16}.
$$

To two significant figures,

$$
\boxed{\frac{g_h}{g}=0.56}.
$$

```quiz
type: radio
id: m3-1lec-q1
content: |-
  **Question 1**

  A satellite is in a circular orbit at an altitude equal to one-third of Earth's radius $r_E$. What is the satellite's gravitational acceleration $g_h$ in units of the surface acceleration $g$?

  Enter $g_h/g$ using two significant figures:
options:
- id: a
  content: |-
    $0.56$
  correct: true
  feedback: |-
    The orbital radius measured from Earth's center is

    $$
    r=r_E+\frac13r_E=\frac43r_E.
    $$

    Since gravitational acceleration varies as $1/r^2$,

    $$
    \frac{g_h}{g}
    =\left(\frac{r_E}{r}\right)^2
    =\left(\frac34\right)^2
    =0.5625.
    $$

    To two significant figures, $g_h/g=0.56$.
- id: b
  content: |-
    $0.75$
  feedback: |-
    This uses the reciprocal radius factor $\frac34$ but forgets to square it.
- id: c
  content: |-
    $0.11$
  feedback: |-
    This squares the altitude fraction $\frac13$ instead of using the full radius $\frac43r_E$.
- id: d
  content: |-
    $1.8$
  feedback: |-
    This reverses the requested ratio. Gravity at positive altitude must be less than surface gravity.
- id: e
  content: |-
    $9.0$
  feedback: |-
    This takes the inverse square of the altitude fraction rather than the full center-distance factor.
```

---

## Summary

When altitude is given as $h=\alpha r_E$:

1. Convert altitude to center distance: $r=(1+\alpha)r_E$.
2. Form the requested ratio in the stated order:

   $$
   \frac{g_h}{g}=\left(\frac{r_E}{r}\right)^2.
   $$

3. Cancel $r_E$ and square the entire fraction:

   $$
   \boxed{\frac{g_h}{g}=\frac{1}{(1+\alpha)^2}}.
   $$

4. Check that a positive altitude gives a ratio between $0$ and $1$.

The main trap is treating altitude $h$ as though it were already the distance $r$ from Earth's center.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
