# Calculate Gravitational Field Strength at a Radius or Altitude

<!--
lesson-id: 212-M3-055
topic-code: MTH212.M3.55
-->

## Table of Contents

- [Introduction](#introduction)
- [Derive the Field Equation and Cancel the Test Mass](#derive-field-equation)
- [Source-Video Worked Problem: Field at the Moon's Surface](#source-video-moon-surface)
- [Source-Video Worked Problems: Field Above Earth's Surface](#source-video-earth-altitude)
- [Source-Video Reverse Problem: Find a Planet's Mass](#source-video-find-mass)
- [Source and Lecture Comparisons: Use an Inverse-Square Ratio](#inverse-square-ratio)
- [Summary](#summary)

## Prerequisites

- Use Newton's second law in the form $F=ma$.
- Use Newton's universal-gravitation magnitude $F_g=GMm/r^2$.
- Square a quantity written in scientific notation.
- Rearrange an equation for one unknown.
- Convert kilometers to meters using $1\,\mathrm{km}=1000\,\mathrm m$.
- Interpret a ratio as a multiplicative scale factor.

---

<a id="introduction"></a>
## Introduction

For a point outside a spherical body of mass $M$, the gravitational-field magnitude is

$$
\boxed{g(r)=\frac{GM}{r^2}},
\qquad
G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}.
$$

The distance $r$ is measured from the body's **center**, not from its surface. Therefore,

$$
r=
\begin{cases}
R, & \text{at the surface},\\[4pt]
R+h, & \text{at altitude }h.
\end{cases}
$$

Every calculation in this lesson uses the same move:

1. Translate the stated location into center-based radius $r$.
2. Convert distances to compatible units; use meters before substituting with $G$.
3. Use $g=GM/r^2$, rearrange it, or form a same-source ratio.
4. Square the entire center-based radius.
5. Check that the field decreases as the distance from the center increases.

Choose the form from the information supplied:

| Given | Requested | Use |
|---|---|---|
| $M$ and $r$ | $g$ | $g=GM/r^2$ |
| $g$ and $r$ | $M$ | $M=gr^2/G$ |
| $g_1$, $r_1$, and $r_2$ for the same source | $g_2$ | $g_2/g_1=(r_1/r_2)^2$ |

Do not insert the altitude $h$ for $r$, add the altitude after squaring, or reuse the surface value $9.8\,\mathrm{m/s^2}$ at a large altitude.

---

<a id="derive-field-equation"></a>
## Derive the Field Equation and Cancel the Test Mass

The source segment `8CykJ3NgBQs` at 6:58-9:06 equates the weight of a test mass $m$ with Newton's gravitational-force magnitude:

$$
mg=\frac{GMm}{r^2}.
$$

Cancel the test mass $m$ that appears on both sides:

$$
\boxed{g=\frac{GM}{r^2}}.
$$

The field at a location depends on the source mass $M$ and the center-based radius $r$, not on the test mass used to measure it. A heavier test object feels a proportionally larger force $F_g=mg$, but it has the same gravitational acceleration there.

**Source correction.** The segment says that it does not matter which mass is canceled. The mass that cancels is the mass of the object whose acceleration is being calculated. With $M$ defined as the source body's mass and $m$ as the test mass, only $m$ appears in both $mg$ and $GMm/r^2$; $M$ remains in the field equation. The segment then checks Earth and obtains about $9.799\,\mathrm{m/s^2}$, rounded to $9.8\,\mathrm{m/s^2}$.

The field-strength units reduce as follows:

$$
\left(\frac{\mathrm{N\,m^2}}{\mathrm{kg^2}}\right)
\frac{\mathrm{kg}}{\mathrm{m^2}}
=\frac{\mathrm N}{\mathrm{kg}}.
$$

Since $1\,\mathrm N=1\,\mathrm{kg\,m/s^2}$,

$$
\boxed{1\,\mathrm{N/kg}=1\,\mathrm{m/s^2}}.
$$

```quiz
type: radio
id: mct-p19-test-mass-cancellation
shuffle: true
content: |-
  Two small test objects, with masses $m$ and $3m$, are placed at the same radius from a spherical planet. Ignore every force except the planet's gravity. Which comparison is correct?
options:
- id: mct-p19-test-mass-cancellation-a
  content: |-
    Both objects have the same gravitational acceleration, and the force on the $3m$ object is three times as large.
  correct: true
  feedback: |-
    Dividing $F_g=GMm/r^2$ by the test mass gives $g=GM/r^2$, so both objects have the same $g$ at the same radius. Because $F_g=mg$, tripling the test mass triples the force.
- id: mct-p19-test-mass-cancellation-b
  content: |-
    The $3m$ object has three times the gravitational acceleration and three times the force.
  feedback: |-
    The force contains the test mass, but the acceleration does not after the test mass cancels. The $3m$ object has triple the force and the same acceleration.
- id: mct-p19-test-mass-cancellation-c
  content: |-
    Both objects have the same gravitational acceleration and the same force.
  feedback: |-
    Equal radius gives equal field strength, not equal force on unequal test masses. Since $F_g=mg$, the $3m$ object feels three times the force.
- id: mct-p19-test-mass-cancellation-d
  content: |-
    The $3m$ object has one-third the gravitational acceleration, so both objects feel the same force.
  feedback: |-
    Test mass does not appear in $g=GM/r^2$, so increasing it cannot reduce the acceleration. The larger test mass instead produces a proportionally larger force.
- id: mct-p19-test-mass-cancellation-e
  content: |-
    The comparison cannot be made without knowing the planet's mass.
  feedback: |-
    The planet's mass is needed for a numerical value of $g$, but not for the comparison. Both objects share the same $M$ and $r$, so their accelerations match and their forces scale with test mass.
```

---

<a id="source-video-moon-surface"></a>
## Source-Video Worked Problem: Field at the Moon's Surface

Problem 1 in `kubaJtXz0c8` at 0:01-4:25 gives

$$
M_{\text{Moon}}=7.35\times10^{22}\ \mathrm{kg},
\qquad
R_{\text{Moon}}=1.74\times10^6\ \mathrm m.
$$

The requested location is the surface, so $r=R_{\text{Moon}}$. Then

$$
\begin{aligned}
g
&=\frac{GM}{R^2}\\
&=\frac{(6.67\times10^{-11})(7.35\times10^{22})}
{(1.74\times10^6)^2}\\
&=1.619\ldots\ \mathrm{m/s^2}\\
&\approx\boxed{1.62\ \mathrm{m/s^2}}.
\end{aligned}
$$

The whole radius, including its power of ten, belongs inside the square.

```quiz
type: radio
id: mct-p19-surface-field
shuffle: true
content: |-
  A spherical planet has mass $6.40\times10^{23}\,\mathrm{kg}$ and radius $3.40\times10^6\,\mathrm m$. Using $G=6.67\times10^{-11}\,\mathrm{N\,m^2/kg^2}$, what is its surface gravitational-field strength?
options:
- id: mct-p19-surface-field-a
  content: |-
    $3.69\,\mathrm{N/kg}$
  correct: true
  feedback: |-
    At the surface, $r=R$. Substitution gives $g=(6.67\times10^{-11})(6.40\times10^{23})/(3.40\times10^6)^2=3.69\,\mathrm{N/kg}$.
- id: mct-p19-surface-field-b
  content: |-
    $0.923\,\mathrm{N/kg}$
  feedback: |-
    This uses the diameter $2R$ as the center-to-surface distance. The surface is one radius from the center; doubling the denominator distance incorrectly quarters the field.
- id: mct-p19-surface-field-c
  content: |-
    $14.8\,\mathrm{N/kg}$
  feedback: |-
    This uses $R/2$ as though the stated radius were a diameter. Halving the denominator distance makes an inverse-square result four times too large.
- id: mct-p19-surface-field-d
  content: |-
    $36.9\,\mathrm{N/kg}$
  feedback: |-
    This treats the planet's mass exponent as $10^{24}$ instead of the stated $10^{23}$. A tenfold source mass would produce this tenfold field, but the given mass does not.
- id: mct-p19-surface-field-e
  content: |-
    $1.26\times10^7\,\mathrm{N/kg}$
  feedback: |-
    This divides by $R$ instead of $R^2$. Gravitational field obeys an inverse-square law, and omitting the square also prevents the units from reducing to $\mathrm{N/kg}$.
```

---

<a id="source-video-earth-altitude"></a>
## Source-Video Worked Problems: Field Above Earth's Surface

### Earth at the Surface and at 3500 km Altitude

Problem 2 in `kubaJtXz0c8` at 4:25-9:24 uses

$$
M_E=5.97\times10^{24}\ \mathrm{kg},
\qquad
R_E=6.38\times10^6\ \mathrm m.
$$

At Earth's surface, $r=R_E$:

$$
g_0
=\frac{GM_E}{R_E^2}
=\boxed{9.78\ \mathrm{m/s^2}}.
$$

At altitude $h=3500\,\mathrm{km}$, first convert the altitude:

$$
3500\,\mathrm{km}
\left(\frac{1000\,\mathrm m}{1\,\mathrm{km}}\right)
=3.50\times10^6\ \mathrm m.
$$

Now add the radius and altitude before squaring:

$$
r=R_E+h
=6.38\times10^6+3.50\times10^6
=9.88\times10^6\ \mathrm m.
$$

Therefore,

$$
\begin{aligned}
g_h
&=\frac{GM_E}{(R_E+h)^2}\\
&=\frac{(6.67\times10^{-11})(5.97\times10^{24})}
{(9.88\times10^6)^2}\\
&=\boxed{4.08\ \mathrm{m/s^2}}.
\end{aligned}
$$

The result is below the surface value, as the inverse-square dependence requires.

### Earth at the Surface and at 5000 km Altitude

The problem in `8AUljAd_AyE` at 0:00-8:34 uses Earth's radius

$$
R_E=6380\,\mathrm{km}=6.38\times10^6\ \mathrm m
$$

and obtains the surface field

$$
g_0=\boxed{9.78\ \mathrm{N/kg}}.
$$

At altitude $5000\,\mathrm{km}$,

$$
\begin{aligned}
r&=6380\,\mathrm{km}+5000\,\mathrm{km}\\
&=11{,}380\,\mathrm{km}\\
&=1.138\times10^7\ \mathrm m.
\end{aligned}
$$

Using this center-based radius gives

$$
g_h
=\frac{GM_E}{r^2}
=3.0748\ldots\ \mathrm{N/kg}
\approx\boxed{3.07\ \mathrm{N/kg}}.
$$

This is also $3.07\,\mathrm{m/s^2}$ because the two field-strength units are equivalent.

**Source corrections.** Early in `8AUljAd_AyE`, the narration says that the field will be calculated “at the center,” but the displayed calculation uses $r=R_E$ and is therefore a **surface** calculation. The narration also gives $11{,}388\,\mathrm{km}$ while adding $6380\,\mathrm{km}$ and $5000\,\mathrm{km}$; the correct sum, used in the subsequent scientific notation, is $11{,}380\,\mathrm{km}$.

```quiz
type: radio
id: mct-p19-altitude-radius
shuffle: true
content: |-
  A planet has surface field $g_0=10.0\,\mathrm{N/kg}$ and radius $R=6000\,\mathrm{km}$. What is the field at altitude $h=3000\,\mathrm{km}$?
options:
- id: mct-p19-altitude-radius-a
  content: |-
    $4.44\,\mathrm{N/kg}$
  correct: true
  feedback: |-
    The center-based radius is $r=R+h=9000\,\mathrm{km}=1.5R$. Thus $g_h/g_0=(R/r)^2=(2/3)^2$, giving $g_h=4.44\,\mathrm{N/kg}$.
- id: mct-p19-altitude-radius-b
  content: |-
    $6.67\,\mathrm{N/kg}$
  feedback: |-
    This applies a first-power inverse factor, $10.0/1.5$. Field strength varies with the inverse **square** of center-based radius, so the factor is $1/(1.5)^2$.
- id: mct-p19-altitude-radius-c
  content: |-
    $5.00\,\mathrm{N/kg}$
  feedback: |-
    This halves the field because the altitude is half the planet's radius. The actual center distance grows from $R$ to $1.5R$, and the inverse-square factor is $1/(1.5)^2$, not $1/2$.
- id: mct-p19-altitude-radius-d
  content: |-
    $22.5\,\mathrm{N/kg}$
  feedback: |-
    This multiplies by $(1.5)^2$ instead of dividing. Increasing distance from the planet's center must decrease the field, not increase it.
- id: mct-p19-altitude-radius-e
  content: |-
    $40.0\,\mathrm{N/kg}$
  feedback: |-
    This treats the altitude $3000\,\mathrm{km}$ as the radius in the field equation. The point is $9000\,\mathrm{km}$ from the center, so using $h$ alone reverses the physical trend.
```

---

<a id="source-video-find-mass"></a>
## Source-Video Reverse Problem: Find a Planet's Mass

Problem 3 in `kubaJtXz0c8` at 9:24-11:07 gives a planet with surface field and radius

$$
g=7.5\ \mathrm{m/s^2},
\qquad
R=4.5\times10^6\ \mathrm m.
$$

At the surface, $r=R$. Rearrange before inserting the numbers:

$$
g=\frac{GM}{R^2}
\quad\Longrightarrow\quad
\boxed{M=\frac{gR^2}{G}}.
$$

Then

$$
\begin{aligned}
M
&=\frac{(7.5)(4.5\times10^6)^2}{6.67\times10^{-11}}\\
&=2.2769\ldots\times10^{24}\ \mathrm{kg}\\
&\approx\boxed{2.28\times10^{24}\ \mathrm{kg}}.
\end{aligned}
$$

```quiz
type: radio
id: mct-p19-solve-source-mass
shuffle: true
content: |-
  A planet's surface gravitational field is $12.0\,\mathrm{N/kg}$, and its radius is $6.00\times10^6\,\mathrm m$. Using $G=6.67\times10^{-11}\,\mathrm{N\,m^2/kg^2}$, what is the planet's mass?
options:
- id: mct-p19-solve-source-mass-a
  content: |-
    $6.48\times10^{24}\,\mathrm{kg}$
  correct: true
  feedback: |-
    Rearranging $g=GM/R^2$ gives $M=gR^2/G$. Substitution gives $M=(12.0)(6.00\times10^6)^2/(6.67\times10^{-11})=6.48\times10^{24}\,\mathrm{kg}$.
- id: mct-p19-solve-source-mass-b
  content: |-
    $1.08\times10^{18}\,\mathrm{kg}$
  feedback: |-
    This uses $M=gR/G$ and omits the square on the radius. The field law contains $R^2$, so solving for mass retains that square in the numerator.
- id: mct-p19-solve-source-mass-c
  content: |-
    $1.62\times10^{24}\,\mathrm{kg}$
  feedback: |-
    This substitutes $R/2$ as though the stated radius were a diameter. Because radius is squared, halving it makes the inferred mass one-fourth of the correct value.
- id: mct-p19-solve-source-mass-d
  content: |-
    $2.59\times10^{25}\,\mathrm{kg}$
  feedback: |-
    This uses the diameter $2R$ in place of the stated radius. Squaring twice the correct center-to-surface distance makes the inferred mass four times too large.
- id: mct-p19-solve-source-mass-e
  content: |-
    $4.32\times10^{14}\,\mathrm{kg}$
  feedback: |-
    This calculates $gR^2$ but does not divide by $G$. The rearranged equation is $M=gR^2/G$, so the omitted factor is $1/G\approx1.50\times10^{10}$.
```

---

<a id="inverse-square-ratio"></a>
## Source and Lecture Comparisons: Use an Inverse-Square Ratio

For two locations around the same source body,

$$
g_1=\frac{GM}{r_1^2},
\qquad
g_2=\frac{GM}{r_2^2}.
$$

Equivalently, the product

$$
gr^2=GM
$$

is constant for that source. Divide the two field equations to compare locations without first calculating $GM$:

$$
\boxed{\frac{g_2}{g_1}=\left(\frac{r_1}{r_2}\right)^2}.
$$

The source body must be the same, and both $r_1$ and $r_2$ must be measured from its center. The two radii may stay in kilometers in this ratio because identical length units cancel.

### Source-video scaling example

In `8AUljAd_AyE` at 8:34-10:37, a planet has

$$
g_1=40\ \mathrm{N/kg}
\quad\text{at}\quad
r_1=5000\ \mathrm{km}.
$$

At $r_2=10{,}000\,\mathrm{km}$, the center-based radius doubles. Therefore,

$$
g_2
=g_1\left(\frac{r_1}{r_2}\right)^2
=40\left(\frac{5000}{10{,}000}\right)^2
=\boxed{10\ \mathrm{N/kg}}.
$$

### Lecture-note altitude ratio

The paired M3-1 lecture places a satellite at altitude

$$
h=\frac{R_E}{3}.
$$

Its center-based radius is

$$
r=R_E+h=R_E+\frac{R_E}{3}=\frac{4R_E}{3}.
$$

Relative to the surface field $g_0$,

$$
\frac{g_h}{g_0}
=\left(\frac{R_E}{4R_E/3}\right)^2
=\left(\frac34\right)^2
=\boxed{\frac9{16}}
\approx0.56.
$$

The satellite experiences about $56\%$ of the surface field, not zero gravity.

```quiz
type: radio
id: mct-p19-inverse-square-scale
shuffle: true
content: |-
  A planet produces a field of $18\,\mathrm{N/kg}$ at $6000\,\mathrm{km}$ from its center. What is the field at $9000\,\mathrm{km}$ from its center?
options:
- id: mct-p19-inverse-square-scale-a
  content: |-
    $8.0\,\mathrm{N/kg}$
  correct: true
  feedback: |-
    For the same planet, $g_2/g_1=(r_1/r_2)^2$. Thus $g_2=18(6000/9000)^2=18(2/3)^2=8.0\,\mathrm{N/kg}$.
- id: mct-p19-inverse-square-scale-b
  content: |-
    $12\,\mathrm{N/kg}$
  feedback: |-
    This uses the first-power ratio $18(6000/9000)$. The field follows an inverse-square law, so the radius ratio must be squared.
- id: mct-p19-inverse-square-scale-c
  content: |-
    $27\,\mathrm{N/kg}$
  feedback: |-
    This multiplies by the direct radius factor $9000/6000$. Moving outward must weaken the field; use the reversed radius ratio and square it.
- id: mct-p19-inverse-square-scale-d
  content: |-
    $40.5\,\mathrm{N/kg}$
  feedback: |-
    This squares the ratio in the wrong direction: $18(9000/6000)^2$. The numerator must be the old radius so that a larger final radius produces a factor below one.
- id: mct-p19-inverse-square-scale-e
  content: |-
    $4.5\,\mathrm{N/kg}$
  feedback: |-
    This quarters the field as though the radius doubled. The radius grows only by a factor of $1.5$, so the field factor is $1/(1.5)^2=4/9$.
```

---

<a id="summary"></a>
## Summary

- Translate the location into distance from the source body's center:
  $$
  r=R\quad\text{at the surface},
  \qquad
  r=R+h\quad\text{at altitude }h.
  $$
- Convert kilometers to meters before using $G$, and square the complete radius only after adding $R+h$.
- Calculate field strength with
  $$
  g=\frac{GM}{r^2}.
  $$
- The test mass cancels, so it does not appear in $g$; it still controls the force through $F_g=mg$.
- Gravitational field strength may be written in either $\mathrm{N/kg}$ or $\mathrm{m/s^2}$.
- For two radii around the same source, use
  $$
  \frac{g_2}{g_1}=\left(\frac{r_1}{r_2}\right)^2.
  $$
- If $r$ increases, $g$ must decrease. A result that grows with altitude signals a radius, ratio, or exponent error.
- To infer the source mass, rearrange to
  $$
  M=\frac{gr^2}{G}.
  $$

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
