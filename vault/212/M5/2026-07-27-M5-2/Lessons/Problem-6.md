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
    Divide the air wavelength by the index: $540\ \mathrm{nm}/1.8=300\ \mathrm{nm}$. The wavelength must decrease because $n>1$. The choice $540\ \mathrm{nm}$ leaves the wavelength unchanged, while $972\ \mathrm{nm}$ multiplies by $n$ and changes it in the wrong direction.
- id: p6-glass-wavelength-b
  content: |-
    $540\ \mathrm{nm}$
- id: p6-glass-wavelength-c
  content: |-
    $972\ \mathrm{nm}$
- id: p6-glass-wavelength-d
  content: |-
    $3.33\ \mathrm{nm}$
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
    Convert $0.90\ \mathrm{mm}$ to $9.0\times10^5\ \mathrm{nm}$, then divide by $300\ \mathrm{nm}$. The units cancel and give $N=3000$. A result with a remaining length unit would not be a wavelength count.
- id: p6-count-wavelengths-b
  content: |-
    $0.003$
- id: p6-count-wavelengths-c
  content: |-
    $300$
- id: p6-count-wavelengths-d
  content: |-
    $270$
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
    Convert $0.60\ \mathrm{mm}$ to $6.0\times10^5\ \mathrm{nm}$ and use $N=nd/\lambda_{\text{air}}$. This gives $N=(1.5)(6.0\times10^5)/600=1500$. The choice $1000$ comes from using the air wavelength without accounting for the material.
- id: p6-combined-formula-b
  content: |-
    $1000$
- id: p6-combined-formula-c
  content: |-
    $667$
- id: p6-combined-formula-d
  content: |-
    $400$
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
    The glass wavelength is $650/1.5=433.3\ldots\ \mathrm{nm}$, but the question asks how many of those wavelengths fit into the slide. Converting $1.2\ \mathrm{mm}$ to $1.2\times10^6\ \mathrm{nm}$ and dividing gives $2769.2\ldots$, which rounds to two significant figures as $2800$. The choice $1800$ uses the air wavelength; $1200$ changes the wavelength in the wrong direction; and $433$ reports the glass wavelength instead of the count.
- id: p6-source-check-b
  content: |-
    1800
- id: p6-source-check-c
  content: |-
    1200
- id: p6-source-check-d
  content: |-
    433
```

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
