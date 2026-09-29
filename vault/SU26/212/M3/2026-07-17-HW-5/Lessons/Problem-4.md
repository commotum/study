# Scaling Surface Gravity With Mass and Radius

<!--
lesson-id: 212-M3-014
topic-code: MTH212.M3.14
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Gravity Ratio](#build-the-gravity-ratio)
- [Apply the Mass Scale Factor](#apply-the-mass-scale-factor)
- [Square the Radius Scale Factor](#square-the-radius-scale-factor)
- [Combine Both Scale Factors](#combine-both-scale-factors)
- [Summary](#summary)

## Prerequisites

- Use the surface-gravity formula $g=GM/R^2$.
- Simplify fractions and squares.
- Interpret a quantity such as $3M_E$ or $2R_E$ as a scale factor relative to Earth.

---

<a id="introduction"></a>
## Introduction

For a spherical planet, the surface-gravity magnitude is $g=GM/R^2$, where $M$ is the planet's mass and $R$ is the distance from its center to its surface. When a planet's mass and radius are given as multiples of Earth's, compare its surface gravity directly with Earth's instead of calculating with $G$, $M_E$, and $R_E$ separately.

The recognition cue is the phrase **“in terms of Earth's surface gravity $g$.”** Form the ratio

$$
\frac{g_p}{g}
=
\frac{GM_p/R_p^2}{GM_E/R_E^2}
=
\frac{M_p/M_E}{(R_p/R_E)^2}.
$$

If $M_p=aM_E$ and $R_p=bR_E$, then

$$
g_p=\frac{a}{b^2}g.
$$

Equivalently,

$$
g_p=(\text{mass factor})
\left(\frac{1}{(\text{radius factor})^2}\right)g.
$$

Mass contributes a factor of $a$, but radius contributes the inverse-square factor $1/b^2$. Increasing mass alone raises surface gravity; increasing radius alone lowers it.

---

<a id="build-the-gravity-ratio"></a>
## Build the Gravity Ratio

**Example:** A planet has mass $M_p=4M_E$ and radius $R_p=3R_E$. Write, but do not yet simplify, the ratio $g_p/g$.

**Explanation**

Substitute the mass multiple in the numerator and the radius multiple inside the square:

$$
\frac{g_p}{g}
=
\frac{M_p/M_E}{(R_p/R_E)^2}
=
\frac{4}{3^2}.
$$

Writing the ratio first cancels the common constant $G$ and prevents the mass and radius scale factors from being confused.

```quiz
type: radio
id: p4-gravity-ratio
content: |-
  A planet has mass $5M_E$ and radius $2R_E$. Which expression correctly gives its surface-gravity ratio $g_p/g$?
options:
- id: a
  content: |-
    $\dfrac{5}{2^2}$
  correct: true
  feedback: Mass contributes $5$ in the numerator, and radius contributes $2^2$ in the denominator.
- id: b
  content: |-
    $\dfrac{5}{2}$
  feedback: This forgets to square the radius factor.
- id: c
  content: |-
    $\dfrac{2^2}{5}$
  feedback: This reverses the mass and radius factors.
- id: d
  content: |-
    $\dfrac{5^2}{2}$
  feedback: Mass is not squared, and the radius belongs in the denominator.
```

---

<a id="apply-the-mass-scale-factor"></a>
## Apply the Mass Scale Factor

**Example:** Two planets have the same radius. Planet B has three times Planet A's mass. How do their surface gravities compare?

**Explanation**

With the radius unchanged, the radius ratio is $1$. Thus

$$
\frac{g_B}{g_A}=\frac{3}{1^2}=3.
$$

Surface gravity is directly proportional to mass when radius is fixed, so tripling the mass triples the surface gravity.

```quiz
type: radio
id: p4-mass-factor
content: |-
  Planet Y has four times Planet X's mass, and the planets have equal radii. If Planet X has surface gravity $g_X$, what is Planet Y's surface gravity?
options:
- id: a
  content: |-
    $4g_X$
  correct: true
  feedback: At fixed radius, surface gravity scales directly with mass.
- id: b
  content: |-
    $2g_X$
  feedback: The mass factor is not square-rooted.
- id: c
  content: |-
    $g_X/4$
  feedback: This reverses the direct mass relationship.
- id: d
  content: |-
    $16g_X$
  feedback: Mass is not squared.
```

---

<a id="square-the-radius-scale-factor"></a>
## Square the Radius Scale Factor

**Example:** Two planets have the same mass. Planet B has twice Planet A's radius. How do their surface gravities compare?

**Explanation**

The mass ratio is $1$, while the radius ratio is $2$:

$$
\frac{g_B}{g_A}=\frac{1}{2^2}=\frac14.
$$

Doubling radius does not halve surface gravity. Because radius is squared in $g=GM/R^2$, doubling radius makes surface gravity one-fourth as large.

```quiz
type: radio
id: p4-radius-factor
content: |-
  Two planets have equal masses. Planet Y has three times Planet X's radius. If Planet X has surface gravity $g_X$, what is Planet Y's surface gravity?
options:
- id: a
  content: |-
    $g_X/9$
  correct: true
  feedback: The inverse-square factor is $1/3^2=1/9$.
- id: b
  content: |-
    $g_X/3$
  feedback: This forgets to square the radius factor.
- id: c
  content: |-
    $3g_X$
  feedback: A larger radius lowers surface gravity when mass is fixed.
- id: d
  content: |-
    $9g_X$
  feedback: This both reverses the relationship and squares in the wrong direction.
```

---

<a id="combine-both-scale-factors"></a>
## Combine Both Scale Factors

**Example:** A planet has eight times Earth's mass and twice Earth's radius. Find its surface gravity in terms of $g$.

**Explanation**

Here $a=8$ and $b=2$. Substitute both scale factors into the same ratio:

$$
\frac{g_p}{g}=\frac{8}{2^2}=\frac84=2.
$$

Therefore,

$$
g_p=2g.
$$

The larger mass contributes $8$, while the doubled radius contributes $1/4$. Their product is $8(1/4)=2$.

```quiz
type: radio
id: p4-combined-factors
content: |-
  A planet has six times Earth's mass and three times Earth's radius. What is its surface gravity in terms of $g$?
options:
- id: a
  content: |-
    $2g/3$
  correct: true
  feedback: The scale factor is $6/3^2=6/9=2/3$.
- id: b
  content: |-
    $2g$
  feedback: This divides by the radius factor but forgets to square it.
- id: c
  content: |-
    $3g/2$
  feedback: This inverts the correct combined factor.
- id: d
  content: |-
    $4g$
  feedback: This result does not apply the inverse-square radius factor.
```

**Original problem:** Apply the same comparison to the given exoplanet.

```quiz
type: radio
id: p4-original-exoplanet
shuffle: true
content: |-
  NASA discovers an exoplanet with three times Earth's mass and twice Earth's radius.

  What is the magnitude of the gravitational acceleration at the planet's surface, expressed in terms of Earth's surface gravity $g$?
options:
- id: a
  content: |-
    $2g/3$
  feedback: This reverses the mass and radius factors before combining them.
- id: b
  content: |-
    $3g/4$
  correct: true
  feedback: The mass factor is $3$, and the inverse-square radius factor is $1/2^2=1/4$.
- id: c
  content: |-
    $4g/3$
  feedback: This is the reciprocal of the correct factor.
- id: d
  content: |-
    $3g/2$
  feedback: This forgets to square the radius factor.
```

---

## Summary

When mass and radius are given relative to a reference planet, use

$$
\frac{g_2}{g_1}
=
\frac{M_2/M_1}{(R_2/R_1)^2}.
$$

Use this checklist:

1. Read the mass scale factor $a$.
2. Read the radius scale factor $b$.
3. Compute $a/b^2$.
4. Multiply the reference gravity by that factor.
5. Check the direction: mass raises surface gravity, while radius lowers it through an inverse square.

The main trap is forgetting to square the radius factor. For the exoplanet in the problem, $a=3$ and $b=2$, so $g_p=(3/4)g$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
