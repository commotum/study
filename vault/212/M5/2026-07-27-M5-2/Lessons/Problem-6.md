# Counting Wavelengths Inside a Material

<!--
lesson-id: 212-M5-013
topic-code: MTH212.M5.13
-->

## Table of Contents

- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Recognize What Changes at the Boundary](#recognize-what-changes-at-the-boundary)
- [Count Wavelengths Using Matching Units](#count-wavelengths-using-matching-units)
- [Combine the Two Steps](#combine-the-two-steps)
- [Apply the Move to Problem 6](#apply-the-move-to-problem-6)
- [Variant: A 600 nm Glass Slide](#variant-a-600-nm-glass-slide)
- [Summary](#summary)

## Prerequisites

- Use the wave relation $v=f\lambda$.
- Convert metric units with conversion factors.
- Interpret a ratio of two lengths as a dimensionless count.
- Round a result to the significant figures supported by the givens.

---

<a id="introduction"></a>
## Introduction

When a problem gives a wavelength in air, an index of refraction, and a distance traveled inside a material, the recognition cue is that the wavelength changes at the boundary while the frequency stays fixed. Use one move: divide the air wavelength by the index to find the wavelength in the material, convert the travel distance to the same unit, and divide distance by wavelength to count how many wavelengths fit.

Equivalently,

$$
N=\frac{d}{\lambda_{\text{material}}}
=\frac{nd}{\lambda_{\text{air}}},
$$

provided $d$ and $\lambda_{\text{air}}$ are expressed in matching length units.

---

## Recognize What Changes at the Boundary

**Recognition cue:** The problem gives a wavelength in air, an index of refraction, and a distance inside a material, then asks how many wavelengths fit in that distance.

When light enters a material, its **frequency stays constant**. Its speed and wavelength change. If air is treated as having index $1$, then

$$
\lambda_{\text{material}}=\frac{\lambda_{\text{air}}}{n}.
$$

Because ordinary glass has $n>1$, the wavelength in glass must be shorter than the wavelength in air.

The index tells you the direction immediately:

$$
n\uparrow \quad\Longrightarrow\quad \lambda_{\text{material}}\downarrow
\quad\Longrightarrow\quad
\text{more wavelengths fit in the same thickness}.
$$

**Example:** Light with wavelength $600\ \mathrm{nm}$ in air enters glass with $n=1.5$. Then

$$
\lambda_{\text{glass}}=\frac{600\ \mathrm{nm}}{1.5}=400\ \mathrm{nm}.
$$

```quiz
type: radio
id: p6-glass-wavelength
content: |-
  Light has wavelength $540\ \mathrm{nm}$ in air and enters a material with index $n=1.8$. What is its wavelength in the material?
options:
- id: p6-glass-wavelength-a
  content: |-
    $300\ \mathrm{nm}$
  correct: true
  feedback: |-
    Frequency stays fixed at the boundary while the wave slows, so the wavelength decreases by the index factor. Thus $\lambda_{\mathrm{material}}=540\ \mathrm{nm}/1.8=300\ \mathrm{nm}$.
- id: p6-glass-wavelength-b
  content: |-
    $540\ \mathrm{nm}$
  feedback: |-
    This leaves the wavelength unchanged along with the frequency. Only frequency stays fixed at the boundary; the lower speed in the $n=1.8$ material shortens the wavelength to $540/1.8=300\ \mathrm{nm}$.
- id: p6-glass-wavelength-c
  content: |-
    $972\ \mathrm{nm}$
  feedback: |-
    This multiplies the air wavelength by $n$, making it longer. Since the frequency is unchanged and the material slows the wave, $n>1$ must shorten the wavelength: $\lambda_{\mathrm{material}}=540/1.8=300\ \mathrm{nm}$.
- id: p6-glass-wavelength-d
  content: |-
    $3.33\ \mathrm{nm}$
  feedback: |-
    An index of $1.8$ changes the wavelength only by a factor of $1.8$, not by two orders of magnitude. Dividing $540\ \mathrm{nm}$ by $1.8$ gives $300\ \mathrm{nm}$.
```

## Count Wavelengths Using Matching Units

The number of wavelengths that fit across a thickness $d$ is

$$
N=\frac{d}{\lambda_{\text{material}}}.
$$

The numerator and denominator must use the same length unit. When they do, the length units cancel and $N$ is a pure count.

For this problem type, the useful metric relationship is

$$
1\ \mathrm{mm}=10^{-3}\ \mathrm{m}
\quad\text{and}\quad
1\ \mathrm{nm}=10^{-9}\ \mathrm{m},
$$

so

$$
1\ \mathrm{mm}=10^6\ \mathrm{nm}.
$$

Put $\mathrm{mm}$ in the denominator of the conversion factor so the original unit cancels. If it does not cancel, the factor is upside down.

**Example:** A slab is $0.80\ \mathrm{mm}$ thick, and the wavelength inside it is $400\ \mathrm{nm}$. Convert the thickness first:

$$
0.80\ \mathrm{mm}
\left(\frac{10^6\ \mathrm{nm}}{1\ \mathrm{mm}}\right)
=8.0\times10^5\ \mathrm{nm}.
$$

Then

$$
N=\frac{8.0\times10^5\ \mathrm{nm}}{400\ \mathrm{nm}}=2000.
$$

Notice that

$$
\frac{\mathrm{nm}}{\mathrm{nm}}=1,
$$

so the result has no length unit. It is a number of wavelengths.

```quiz
type: radio
id: p6-count-wavelengths
content: |-
  A material is $0.90\ \mathrm{mm}$ thick, and the wavelength inside it is $300\ \mathrm{nm}$. How many wavelengths fit across the material?
options:
- id: p6-count-wavelengths-a
  content: |-
    $3000$
  correct: true
  feedback: |-
    A wavelength count is total distance divided by wavelength, using matching units. Since $0.90\ \mathrm{mm}=9.0\times10^5\ \mathrm{nm}$, $N=(9.0\times10^5\ \mathrm{nm})/(300\ \mathrm{nm})=3000$.
- id: p6-count-wavelengths-b
  content: |-
    $0.003$
  feedback: |-
    This divides the numerical values while leaving millimeters and nanometers unmatched. Convert $0.90\ \mathrm{mm}$ to $9.0\times10^5\ \mathrm{nm}$ first; then $d/\lambda=3000$.
- id: p6-count-wavelengths-c
  content: |-
    $300$
  feedback: |-
    The $300$ labels the length of one wavelength in nanometers; it is not a count. The number that fits is the total thickness divided by that length: $(9.0\times10^5)/300=3000$.
- id: p6-count-wavelengths-d
  content: |-
    $270$
  feedback: |-
    Multiplying a thickness by a wavelength does not count repeated lengths and leaves squared-length units. A dimensionless count requires $N=d/\lambda$ after matching units, which gives $3000$.
```

## Combine the Two Steps

Substituting $\lambda_{\text{material}}=\lambda_{\text{air}}/n$ into the counting formula gives

$$
N=\frac{d}{\lambda_{\text{air}}/n}
=\frac{nd}{\lambda_{\text{air}}}.
$$

This one-line form is useful after $d$ and $\lambda_{\text{air}}$ have been put in the same unit. It also gives a direction check: at a fixed thickness and air wavelength, a larger $n$ produces more wavelengths inside the material.

**Example:** A $0.50\ \mathrm{mm}$ slab has $n=1.4$, and the light's air wavelength is $500\ \mathrm{nm}$. Since $0.50\ \mathrm{mm}=5.0\times10^5\ \mathrm{nm}$,

$$
N=\frac{(1.4)(5.0\times10^5\ \mathrm{nm})}{500\ \mathrm{nm}}=1400.
$$

```quiz
type: radio
id: p6-combined-formula
content: |-
  Light with air wavelength $600\ \mathrm{nm}$ enters a material with $n=1.5$. How many wavelengths fit across a thickness of $0.60\ \mathrm{mm}$?
options:
- id: p6-combined-formula-a
  content: |-
    $1500$
  correct: true
  feedback: |-
    The material shortens the wavelength by $n$, so the number fitting in a fixed thickness grows by $n$. With $0.60\ \mathrm{mm}=6.0\times10^5\ \mathrm{nm}$, $N=nd/\lambda_{\mathrm{air}}=(1.5)(6.0\times10^5)/600=1500$.
- id: p6-combined-formula-b
  content: |-
    $1000$
  feedback: |-
    This counts $600\ \mathrm{nm}$ air wavelengths across the slab. Inside the material each wavelength is shorter by $n=1.5$, so the count is larger by that factor: $1000(1.5)=1500$.
- id: p6-combined-formula-c
  content: |-
    $667$
  feedback: |-
    This divides the air-based count by $n$, as though the material made each wavelength longer. Since $\lambda_{\mathrm{material}}=\lambda_{\mathrm{air}}/n$, shorter wavelengths increase the count to $N=nd/\lambda_{\mathrm{air}}=1500$.
- id: p6-combined-formula-d
  content: |-
    $400$
  feedback: |-
    This is the in-material wavelength, $600/1.5=400\ \mathrm{nm}$, so it has units of length. The question asks for the dimensionless count across the slab: $(6.0\times10^5\ \mathrm{nm})/(400\ \mathrm{nm})=1500$.
```

## Apply the Move to Problem 6

**Example:** Orange light with wavelength $650\ \mathrm{nm}$ travels through air and strikes a $1.2\ \mathrm{mm}$-thick glass slide perpendicular to its surface. The glass has index of refraction $n=1.5$. How many wavelengths of the light fit inside the glass slide?

Enter the number of wavelengths as a number only.

Sort the givens by their jobs:

| Given | Job |
| --- | --- |
| $\lambda_{\mathrm{air}}=650\ \mathrm{nm}$ | Starting wavelength |
| $n=1.5$ | Shortens the wavelength in glass |
| $d=1.2\ \mathrm{mm}$ | Distance across which wavelengths are counted |

First find the wavelength in the glass:

$$
\lambda_{\mathrm{glass}}
=\frac{\lambda_{\mathrm{air}}}{n}
=\frac{650\ \mathrm{nm}}{1.5}
=433.3\ldots\ \mathrm{nm}.
$$

Convert the slide thickness so both lengths are in nanometers:

$$
1.2\ \mathrm{mm}
\left(\frac{10^6\ \mathrm{nm}}{1\ \mathrm{mm}}\right)
=1.2\times10^6\ \mathrm{nm}.
$$

Now count the wavelengths:

$$
N=\frac{1.2\times10^6\ \mathrm{nm}}{433.3\ldots\ \mathrm{nm}}
=2769.2\ldots.
$$

Here the units confirm the setup:

$$
\frac{\mathrm{nm}}{\mathrm{nm}}=1.
$$

A quick reasonableness check agrees: using the unchanged air wavelength would give about $1800$ wavelengths, so the shorter glass wavelength must produce a larger count. The value $2769.2\ldots$ does.

The measured givens have two significant figures, so

$$
N=2.8\times10^3.
$$

The requested answer form is: **Enter the number of wavelengths as a number only.** Therefore, enter **2800**.

```quiz
type: radio
id: p6-source-check
content: |-
  Orange light with wavelength $650\ \mathrm{nm}$ travels through air and strikes a $1.2\ \mathrm{mm}$-thick glass slide perpendicular to its surface. The glass has index of refraction $n=1.5$. How many wavelengths of the light fit inside the glass slide?

  Enter the number of wavelengths as a number only.
options:
- id: p6-source-check-a
  content: |-
    2800
  correct: true
  feedback: |-
    Glass shortens the wavelength to $650/1.5=433.3\ldots\ \mathrm{nm}$. The $1.2\ \mathrm{mm}=1.2\times10^6\ \mathrm{nm}$ thickness therefore contains $1.2\times10^6/433.3\ldots=2769.2\ldots$ wavelengths, which rounds to the requested entry $2800$.
- id: p6-source-check-b
  content: |-
    1800
  feedback: |-
    This counts unchanged $650\ \mathrm{nm}$ air wavelengths. Frequency stays fixed but the glass slows the light, so each glass wavelength is only $433.3\ldots\ \mathrm{nm}$ and about $2800$ fit.
- id: p6-source-check-c
  content: |-
    1200
  feedback: |-
    This changes the count in the wrong direction, as though glass lengthened the wavelength. Since $n=1.5>1$, glass shortens it to $650/1.5=433.3\ldots\ \mathrm{nm}$, increasing the count to about $2800$.
- id: p6-source-check-d
  content: |-
    433
  feedback: |-
    This reports the length of one glass wavelength, $\lambda_{\mathrm{glass}}\approx433\ \mathrm{nm}$. The requested quantity is how many such lengths span the slide: $N=d/\lambda_{\mathrm{glass}}\approx2769$, entered as $2800$.
```

<a id="variant-a-600-nm-glass-slide"></a>
## Variant: A 600 nm Glass Slide

This variant changes both the vacuum wavelength and slide thickness while preserving the same two-step calculation.

```quiz
type: blank
id: khadley-light-waves-q2
input_mode: math
require_exact: true
content: |-
  Orange light of vacuum wavelength $600\ \mathrm{nm}$ enters normally into a $1.00\ \mathrm{mm}$ glass slide with $n=1.5$. How many wavelengths fit inside the glass? ==2500==
feedback: |-
  Frequency stays constant, so $\lambda_{\mathrm{glass}}=\lambda_0/n=400\ \mathrm{nm}$. The count is $(1.00\ \mathrm{mm})/(400\ \mathrm{nm})=2.5\times10^3$ wavelengths.
```

---

## Summary

Use the chain

$$
\boxed{\text{medium wavelength}\ \longrightarrow\ \text{matching units}\ \longrightarrow\ \text{count}\ \longrightarrow\ \text{final rounding}}.
$$

In symbols:

1. Find $\lambda_{\text{material}}=\lambda_{\text{air}}/n$.
2. Convert the thickness and wavelength to the same length unit.
3. Count with $N=d/\lambda_{\text{material}}$, or equivalently $N=nd/\lambda_{\text{air}}$.
4. Confirm that the length units cancel and that $n>1$ makes the in-material wavelength shorter.
5. Round only at the end and use the requested answer form.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Scaling Wave Power and Intensity with Frequency and Amplitude](../../2026-08-03-Q-3/Lessons/wave-power-intensity-scaling.md)

Study guide index: 15/28

---
<!-- lesson-nav:end -->
