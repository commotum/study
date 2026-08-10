# Comparing Same-Side Single-Slit Minima

<!--
lesson-id: 212-M6-013
topic-code: MTH212.M6.13
-->
## Table of Contents

- [Introduction](#introduction)
- [Locate One First Minimum](#locate-one-first-minimum)
- [Subtract Same-Side Positions](#subtract-same-side-positions)
- [Keep Length Units Consistent](#keep-length-units-consistent)
- [Distinguish Same-Side Spacing from Central Width](#distinguish-same-side-spacing-from-central-width)
- [Apply the Move to Violet and Green Light](#apply-the-move-to-violet-and-green-light)
- [Summary](#summary)

## Prerequisites

- Convert nanometers, micrometers, meters, and centimeters.
- Use the small-angle approximation $\sin\theta\approx\tan\theta\approx\theta$.
- Take the positive distance between two positions with an absolute difference.

---

<a id="introduction"></a>
## Introduction

When a problem gives one slit, two wavelengths, and asks about first-minimum positions on the **same side** of the central maximum, first express each position with the single-slit minimum rule and then subtract the positions.

Single-slit minima satisfy

$$
a\sin\theta=m\lambda,
\qquad m=1,2,3,\ldots
$$

For a distant screen and small angles, $y\approx L\tan\theta\approx L\sin\theta$, so

$$
y_m\approx\frac{mL\lambda}{a}.
$$

At fixed $m$, $L$, and $a$, a longer wavelength places its minimum farther from the center. Therefore, the distance between two same-side minima is

$$
\boxed{\Delta y\approx \left|y_m(\lambda_2)-y_m(\lambda_1)\right|
=\frac{mL\left|\lambda_2-\lambda_1\right|}{a}}.
$$

For first minima, use $m=1$. The shortcut is valid under the same small-angle condition as $y_m\approx mL\lambda/a$.

A quick direction check follows from the same formula:

$$
\Delta y\propto L,
\qquad
\Delta y\propto |\Delta\lambda|,
\qquad
\Delta y\propto \frac{1}{a}.
$$

Moving the screen farther away or increasing the wavelength gap increases the spacing; widening the slit decreases it.

---

<a id="locate-one-first-minimum"></a>
## Locate One First Minimum

**Example:** A slit has width $a=25\ \mu\mathrm{m}$. For light of wavelength $\lambda=600\ \mathrm{nm}$ and a screen distance $L=1.5\ \mathrm{m}$, locate the first minimum.

**Explanation**

“First minimum” means $m=1$. Convert both small lengths to meters and use $y_1\approx L\lambda/a$:

$$
y_1\approx
\frac{(1.5\ \mathrm{m})(600\times10^{-9}\ \mathrm{m})}
{25\times10^{-6}\ \mathrm{m}}
=0.036\ \mathrm{m}=3.6\ \mathrm{cm}.
$$

```quiz
type: radio
id: p3-locate-first-minimum
content: |-
  A slit of width $30\ \mu\mathrm{m}$ is illuminated by $450\ \mathrm{nm}$ light. A screen is $2.0\ \mathrm{m}$ away. Approximately how far from the center is the first minimum?
options:
- id: p3-locate-a
  content: |-
    $1.5\ \mathrm{cm}$
  feedback: |-
    This is what results if the factor $L=2.0\ \mathrm{m}$ is omitted. Screen position scales with the slit-to-screen distance: $y_1\approx L\lambda/a$, which gives $3.0\ \mathrm{cm}$ here.
- id: p3-locate-b
  content: |-
    $3.0\ \mathrm{cm}$
  correct: true
  feedback: |-
    A first minimum uses $m=1$ in $y_m\approx mL\lambda/a$. Substituting the converted lengths gives $y_1=(2.0)(450\times10^{-9})/(30\times10^{-6})=0.030\ \mathrm{m}=3.0\ \mathrm{cm}$.
- id: p3-locate-c
  content: |-
    $6.0\ \mathrm{cm}$
  feedback: |-
    Doubling $y_1$ gives the full distance between the two first minima on opposite sides, which is the central-maximum width. This question asks for one first-minimum position, so use $y_1=3.0\ \mathrm{cm}$.
- id: p3-locate-d
  content: |-
    $30\ \mathrm{cm}$
  feedback: |-
    This is a power-of-ten conversion error. Because $450\ \mathrm{nm}=450\times10^{-9}\ \mathrm{m}$ and $30\ \mu\mathrm{m}=30\times10^{-6}\ \mathrm{m}$, the result is $0.030\ \mathrm{m}=3.0\ \mathrm{cm}$, not $30\ \mathrm{cm}$.
```

---

<a id="subtract-same-side-positions"></a>
## Subtract Same-Side Positions

**Example:** A $30\ \mu\mathrm{m}$ slit is viewed on a screen $2.4\ \mathrm{m}$ away using $450\ \mathrm{nm}$ and $550\ \mathrm{nm}$ light. Find the distance between the first minima on the same side.

**Explanation**

Both positions have the same factors $L/a$, so subtract the wavelengths before multiplying:

$$
\Delta y\approx
\frac{L|\lambda_2-\lambda_1|}{a}
=\frac{(2.4)(100\times10^{-9})}{30\times10^{-6}}
=0.0080\ \mathrm{m}=0.80\ \mathrm{cm}.
$$

This is a distance, so the wavelength order cannot make the answer negative.

```quiz
type: radio
id: p3-subtract-same-side
content: |-
  A $24\ \mu\mathrm{m}$ slit is $1.8\ \mathrm{m}$ from a screen. What is the distance between the same-side first minima for wavelengths $480\ \mathrm{nm}$ and $640\ \mathrm{nm}$?
options:
- id: p3-subtract-a
  content: |-
    $1.2\ \mathrm{cm}$
  correct: true
  feedback: |-
    Same-side spacing is the absolute difference of the positions, so $\Delta y\approx L|\Delta\lambda|/a$. Here $\Delta y=(1.8)(160\times10^{-9})/(24\times10^{-6})=0.012\ \mathrm{m}=1.2\ \mathrm{cm}$.
- id: p3-subtract-b
  content: |-
    $3.6\ \mathrm{cm}$
  feedback: |-
    This is the first-minimum position for $480\ \mathrm{nm}$ alone. The requested spacing compares both wavelengths, so subtract the two positions, equivalently using $|640-480|\ \mathrm{nm}$, to obtain $1.2\ \mathrm{cm}$.
- id: p3-subtract-c
  content: |-
    $4.8\ \mathrm{cm}$
  feedback: |-
    This is the first-minimum position for $640\ \mathrm{nm}$ alone. A single position is measured from the center; the distance between the two same-side positions is their difference, $4.8-3.6=1.2\ \mathrm{cm}$.
- id: p3-subtract-d
  content: |-
    $8.4\ \mathrm{cm}$
  feedback: |-
    Adding $3.6\ \mathrm{cm}$ and $4.8\ \mathrm{cm}$ would be appropriate for minima on opposite sides of the center. Both minima are on the same side, so their distance is the difference, $1.2\ \mathrm{cm}$.
```

---

<a id="keep-length-units-consistent"></a>
## Keep Length Units Consistent

**Example:** Let $L=3.0\ \mathrm{m}$, $a=50\ \mu\mathrm{m}$, and $|\Delta\lambda|=150\ \mathrm{nm}$. Convert the slit width and wavelength difference to the same base unit:

$$
a=50\times10^{-6}\ \mathrm{m},
\qquad
|\Delta\lambda|=150\times10^{-9}\ \mathrm{m}.
$$

**Explanation**

The ratio $|\Delta\lambda|/a$ is dimensionless, leaving the screen distance as the result's length unit:

$$
\Delta y\approx
(3.0\ \mathrm{m})
\frac{150\times10^{-9}\ \mathrm{m}}{50\times10^{-6}\ \mathrm{m}}
=0.0090\ \mathrm{m}=0.90\ \mathrm{cm}.
$$

The unit check is

$$
[\Delta y]=\mathrm{m}\left(\frac{\mathrm{m}}{\mathrm{m}}\right)=\mathrm{m}.
$$

If the slit-width and wavelength units do not cancel, the substitution is not ready to evaluate.

```quiz
type: radio
id: p3-convert-lengths
content: |-
  For $L=2.5\ \mathrm{m}$, $a=40\ \mu\mathrm{m}$, $\lambda_1=500\ \mathrm{nm}$, and $\lambda_2=620\ \mathrm{nm}$, which substitution correctly uses the same-side spacing formula with all small lengths converted to meters?
options:
- id: p3-convert-a
  content: |-
    $\displaystyle \Delta y=(2.5)\frac{(620-500)\times10^{-9}}{40\times10^{-6}}\ \mathrm{m}$
  correct: true
  feedback: |-
    The spacing formula uses the wavelength difference, and $1\ \mathrm{nm}=10^{-9}\ \mathrm{m}$ while $1\ \mu\mathrm{m}=10^{-6}\ \mathrm{m}$. Thus this substitution consistently computes $L|\Delta\lambda|/a$.
- id: p3-convert-b
  content: |-
    $\displaystyle \Delta y=(2.5)\frac{620-500}{40}\ \mathrm{m}$
  feedback: |-
    The numerator is still expressed in nanometers while the denominator is still expressed in micrometers, so the bare ratio misses a factor of $10^{-3}$. Convert both to meters, or first convert $120\ \mathrm{nm}$ to $0.120\ \mu\mathrm{m}$.
- id: p3-convert-c
  content: |-
    $\displaystyle \Delta y=(2.5)\frac{(620-500)\times10^{-6}}{40\times10^{-9}}\ \mathrm{m}$
  feedback: |-
    This reverses the metric prefixes: nanometers carry $10^{-9}$ and micrometers carry $10^{-6}$. Using the reversed powers makes the ratio too large by $10^6$.
- id: p3-convert-d
  content: |-
    $\displaystyle \Delta y=(2.5)\frac{(620+500)\times10^{-9}}{40\times10^{-6}}\ \mathrm{m}$
  feedback: |-
    The conversions are consistent, but same-side distance uses the absolute difference of positions and therefore the wavelength difference. A wavelength sum corresponds to adding distances from the center, as for opposite-side positions.
```

---

<a id="distinguish-same-side-spacing-from-central-width"></a>
## Distinguish Same-Side Spacing from Central Width

Treat each minimum as a signed screen coordinate measured from the central maximum at $y=0$. The universal distance rule is $|y_2-y_1|$: equal signs make it a difference of magnitudes, while opposite signs make it a sum.

**Example:** Two first minima lie at $+3.0\ \mathrm{cm}$ and $+4.2\ \mathrm{cm}$. Because both coordinates have the same sign, their separation is

$$
|4.2-3.0|\ \mathrm{cm}=1.2\ \mathrm{cm}.
$$

**Explanation**

The words describing the geometry decide whether to subtract or add:

- Same side: $|y_2-y_1|$.
- Opposite sides: $|y_2-(-y_1)|=y_2+y_1$.
- Full central-maximum width for one wavelength: $2y_1$.

```quiz
type: radio
id: p3-read-the-geometry
content: |-
  On the right side of a central maximum, the blue first minimum is at $+3.2\ \mathrm{cm}$ and the red first minimum is at $+5.0\ \mathrm{cm}$. What is the distance between these same-side minima?
options:
- id: p3-geometry-a
  content: |-
    $1.8\ \mathrm{cm}$
  correct: true
  feedback: |-
    Distance between two positions on the same side is their absolute difference. Both coordinates are positive, so $|5.0-3.2|\ \mathrm{cm}=1.8\ \mathrm{cm}$.
- id: p3-geometry-b
  content: |-
    $5.0\ \mathrm{cm}$
  feedback: |-
    This is the red minimum's distance from the center, not its distance from the blue minimum. The requested interval starts at $3.2\ \mathrm{cm}$ and ends at $5.0\ \mathrm{cm}$, so subtract the coordinates.
- id: p3-geometry-c
  content: |-
    $8.2\ \mathrm{cm}$
  feedback: |-
    Adding the magnitudes would measure between $-3.2\ \mathrm{cm}$ and $+5.0\ \mathrm{cm}$, positions on opposite sides. Here both are on the right, so use $5.0-3.2=1.8\ \mathrm{cm}$.
- id: p3-geometry-d
  content: |-
    $10.0\ \mathrm{cm}$
  feedback: |-
    Doubling $5.0\ \mathrm{cm}$ gives the central-maximum width for the red light, from its left first minimum to its right first minimum. It does not compare the red and blue minima on one side.
```

---

<a id="apply-the-move-to-violet-and-green-light"></a>
## Apply the Move to Violet and Green Light

**Example:** For a $25\ \mu\mathrm{m}$ slit, $L=1.5\ \mathrm{m}$, and wavelengths $450\ \mathrm{nm}$ and $550\ \mathrm{nm}$, the same-side first-minimum spacing is

$$
\Delta y\approx
\frac{(1.5)(100\times10^{-9})}{25\times10^{-6}}
=0.0060\ \mathrm{m}=0.60\ \mathrm{cm}.
$$

**Explanation**

The calculation uses the first-minimum value $m=1$, subtracts the wavelengths because the positions are on the same side, and converts the final distance to the requested scale.

```quiz
type: radio
id: p3-violet-green-application
content: |-
  A single slit of width

  $$
  a=20\ \mu\mathrm{m}
  $$

  is illuminated separately with violet and green light:

  $$
  \lambda_v=400\ \mathrm{nm},
  \qquad
  \lambda_g=500\ \mathrm{nm}.
  $$

  A screen is located $2.0\ \mathrm{m}$ from the slit. What is the distance between the first-minimum positions for the two wavelengths, measured on the same side of the central maximum?
options:
- id: p3-application-a
  content: |-
    $1\ \mathrm{cm}$
  correct: true
  feedback: |-
    First-minimum positions obey $y_1\approx L\lambda/a$, so their same-side distance is $L|\lambda_g-\lambda_v|/a$. Substitution gives $(2.0)(100\times10^{-9})/(20\times10^{-6})=0.010\ \mathrm{m}=1.0\ \mathrm{cm}$.
- id: p3-application-b
  content: |-
    $2\ \mathrm{cm}$
  feedback: |-
    This compares full central-maximum widths: because each width is $2y_1$, their difference would be $2L|\lambda_g-\lambda_v|/a$. The question compares first-minimum positions on one side, so it uses one position difference and gives $1.0\ \mathrm{cm}$.
- id: p3-application-c
  content: |-
    $5\ \mathrm{cm}$
  feedback: |-
    This is the green first-minimum position $L\lambda_g/a$, measured from the center. The question asks for the interval from the violet position to the green position, so subtract their positions to get $1.0\ \mathrm{cm}$.
- id: p3-application-d
  content: |-
    $10\ \mathrm{cm}$
  feedback: |-
    This is twice the green first-minimum position, the approximate full central-maximum width for green light. Comparing two wavelengths on the same side instead requires the difference of their first-minimum positions.
```

---

<a id="summary"></a>
## Summary

When two wavelengths pass through the same slit and the question compares minima of the same order on the same side:

1. Use $y_m\approx mL\lambda/a$ under the small-angle condition.
2. Subtract the positions: $\Delta y=mL|\lambda_2-\lambda_1|/a$.
3. Convert wavelength and slit width to matching length units before dividing.
4. Use a difference for same-side positions; reserve a sum for opposite-side positions and $2y_1$ for one wavelength's central-maximum width.
5. Check the trend: greater $L$ or wavelength gap increases the spacing, while a wider slit decreases it.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
