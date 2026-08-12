# Identifying a Material from Refraction

<!--
lesson-id: 212-M7-002
topic-code: MTH212.M7.02
-->
## Table of Contents

- [Introduction](#introduction)
- [Put the Angles into Snell's Law](#put-the-angles-into-snells-law)
- [Calculate the Unknown Index](#calculate-the-unknown-index)
- [Measure Every Angle from the Normal](#measure-every-angle-from-the-normal)
- [Compare with a Reference Material](#compare-with-a-reference-material)
- [Summary](#summary)

## Prerequisites

- Evaluate sine in degree mode.
- Rearrange an equation to isolate one variable.
- Identify the normal as the line perpendicular to an interface.

---

<a id="introduction"></a>
## Introduction

When a ray crosses from a known medium into an unknown material and both ray angles are given, use Snell's law to infer the unknown refractive index:

$$
n_1\sin\theta_1=n_2\sin\theta_2.
$$

Both angles are measured from the **normal**, not from the surface. Solving for the second material gives

$$
n_2=n_1\frac{\sin\theta_1}{\sin\theta_2}.
$$

For light arriving from air, $n_1\approx1.00$. After calculating $n_2$, compare it with a reference value for the proposed material.

Use the same order each time:

1. Pair each medium's index with its angle from the normal.
2. Isolate the unknown index symbolically.
3. Evaluate the sines in degree mode, keeping guard digits.
4. Round to the precision supported by the measured angles and compare with the reference value.

---

<a id="put-the-angles-into-snells-law"></a>
## Put the Angles into Snell's Law

**Example:** A ray travels from air into a clear material. Its incident angle is $50^\circ$, and its refracted angle is $30^\circ$. Find the material's refractive index.

**Explanation**

The incident ray is in medium 1, so $n_1=1.00$ and $\theta_1=50^\circ$. The refracted ray is in medium 2, so $\theta_2=30^\circ$:

$$
n_2=(1.00)\frac{\sin50^\circ}{\sin30^\circ}=1.532\ldots\approx1.53.
$$

The ray bends toward the normal because $30^\circ<50^\circ$, so an index greater than the air's index is also the expected physical result.

```quiz
type: radio
id: p2-snells-ratio
content: |-
  A ray travels from air into an unknown material. The incident angle is $40^\circ$, and the refracted angle is $25^\circ$. Which expression correctly gives the unknown index $n$?
options:
- id: incident-over-refracted
  content: |-
    $n=\dfrac{\sin40^\circ}{\sin25^\circ}$
  correct: true
  feedback: |-
    Snell's law pairs each index with the sine of its ray angle. With $n_{\text{air}}\approx1$, isolating the unknown gives incident sine over refracted sine, so $n=\sin40^\circ/\sin25^\circ$.
- id: refracted-over-incident
  content: |-
    $n=\dfrac{\sin25^\circ}{\sin40^\circ}$
  feedback: |-
    This reverses the ratio when isolating the unknown index. It would give $n<1$ even though the ray bends toward the normal on entering the material; the needed ratio is $\sin40^\circ/\sin25^\circ$.
- id: complementary-angles
  content: |-
    $n=\dfrac{\sin50^\circ}{\sin65^\circ}$
  feedback: |-
    Complementary angles would be needed only if the given angles were measured from the surface. These angles are already measured from the normal, so use $40^\circ$ and $25^\circ$ directly.
- id: raw-angle-ratio
  content: |-
    $n=\dfrac{40^\circ}{25^\circ}$
  feedback: |-
    Snell's law relates the sines of the angles, not the angles themselves. Dividing $40$ by $25$ replaces the governing trigonometric relationship with a raw angle ratio.
```

---

<a id="calculate-the-unknown-index"></a>
## Calculate the Unknown Index

**Example:** Light enters an unknown material from air with $\theta_1=40^\circ$ and $\theta_2=25^\circ$. Calculate the index.

**Explanation**

Keep the calculator in degree mode and retain guard digits until the last step:

$$
n=(1.00)\frac{\sin40^\circ}{\sin25^\circ}
=1.520965\ldots\approx1.52.
$$

A refractive index is dimensionless because it is a ratio of wave speeds. The measured angles limit the useful precision, so reporting many extra decimal places would overstate the measurement.

```quiz
type: radio
id: p2-calculate-index
content: |-
  A ray travels from air into an unknown material with $\theta_1=55^\circ$ and $\theta_2=32^\circ$. What is the material's refractive index to three significant figures?
options:
- id: index-1-55
  content: |-
    $1.55$
  correct: true
  feedback: |-
    For air-to-material refraction, $n=\sin\theta_1/\sin\theta_2$. Substitution in degree mode gives $\sin55^\circ/\sin32^\circ=1.545805\ldots$, which rounds to $1.55$.
- id: index-0-647
  content: |-
    $0.647$
  feedback: |-
    This is the reciprocal $\sin32^\circ/\sin55^\circ$. The unknown index is isolated with the incident sine in the numerator, giving $1.55$, not its reciprocal.
- id: index-1-72
  content: |-
    $1.72$
  feedback: |-
    This comes from the raw angle ratio $55/32$. Snell's law uses $\sin55^\circ/\sin32^\circ$, which gives $1.55$.
- id: index-negative-1-81
  content: |-
    $-1.81$
  feedback: |-
    This results from evaluating 55 and 32 as radians. The angles carry degree symbols, so degree mode is required; it gives a positive index of $1.55$.
```

---

<a id="measure-every-angle-from-the-normal"></a>
## Measure Every Angle from the Normal

**Example:** A diagram labels the incident ray as $35^\circ$ above the surface and the refracted ray as $30^\circ$ from the normal. Find the material's index when the ray begins in air.

**Explanation**

Snell's-law angles must be measured from the normal. Since the surface and normal are perpendicular,

$$
\theta_1=90^\circ-35^\circ=55^\circ,
\qquad
\theta_2=30^\circ.
$$

Then

$$
n=(1.00)\frac{\sin55^\circ}{\sin30^\circ}
=1.638\ldots\approx1.64.
$$

```quiz
type: radio
id: p2-angle-from-normal
content: |-
  A ray in air makes a $60^\circ$ angle with the surface. Inside the material, the refracted ray makes a $20^\circ$ angle with the normal. What is the material's refractive index?
options:
- id: converted-index-1-46
  content: |-
    $1.46$
  correct: true
  feedback: |-
    The incident Snell angle is $90^\circ-60^\circ=30^\circ$. Therefore $n=\sin30^\circ/\sin20^\circ=1.4619\ldots\approx1.46$.
- id: unconverted-index-2-53
  content: |-
    $2.53$
  feedback: |-
    This uses the $60^\circ$ surface angle directly. Snell's law requires the complementary angle from the normal, $30^\circ$, which gives $n\approx1.46$.
- id: reciprocal-index-0-684
  content: |-
    $0.684$
  feedback: |-
    This is the reciprocal of the correct sine ratio after converting the incident angle. Isolating the material's index requires $\sin30^\circ/\sin20^\circ$, not the reverse.
- id: raw-angle-index-1-50
  content: |-
    $1.50$
  feedback: |-
    This divides the corrected angles, $30/20$, instead of their sines. The Snell's-law calculation is $\sin30^\circ/\sin20^\circ\approx1.46$.
```

---

<a id="compare-with-a-reference-material"></a>
## Compare with a Reference Material

**Example:** A sample gives $\theta_1=48^\circ$ in air and $\theta_2=29^\circ$ in the sample. Is it consistent with crown glass, whose visible-light refractive index is about $1.52$?

**Explanation**

First infer the measured index:

$$
n_{\text{sample}}=rac{\sin48^\circ}{\sin29^\circ}
=1.5329\ldots\approx1.53.
$$

The measured value is close to $1.52$, so the optical evidence is consistent with crown glass. This supports a likely identification; a single refractive-index measurement is not a complete chemical test.

The comparison should match the quality of the measurements. Whole-degree angles do not justify treating every calculator digit as exact: use the unrounded value for the calculation, but make the material decision from a sensibly rounded index.

For visible light, useful comparison values are approximately:

| Material | Refractive index |
|---|---:|
| Quartz | $1.46$ |
| Crown glass | $1.52$ |
| Diamond | $2.42$ |

```quiz
type: radio
id: p2-diamond-check
shuffle: true
content: |-
  A green laser travels from air into the crystal shown. The incident angle is $45^\circ$, and the refracted angle is $17^\circ$.

  ![](<../Source/2026-08-12-HW-10/Images/green-laser-crystal-refraction-diagram.png>)

  Is the crystal likely a diamond?
options:
- id: yes
  content: |-
    Yes
  correct: true
  feedback: |-
    Snell's law gives $n_{\text{crystal}}=\sin45^\circ/\sin17^\circ=2.4185\ldots$. At the precision of the measured angles this is about $2.4$, consistent with diamond's approximate visible-light index of $2.42$, so the measurement supports “likely diamond.”
- id: no
  content: |-
    No
  feedback: |-
    The measured bending does not rule out diamond. It gives $n_{\text{crystal}}=2.4185\ldots$, or about $2.4$ at the measurement precision, which agrees closely with diamond's visible-light refractive index of about $2.42$.
- id: not-enough-information
  content: |-
    Not enough information
  feedback: |-
    The two normal-referenced angles and $n_{\text{air}}\approx1$ are enough to infer an optical index. The result is about $2.4$, consistent with diamond's value of about $2.42$, so the evidence is sufficient for the question's “likely” conclusion, though not for absolute material certification.
```

---

<a id="summary"></a>
## Summary

When a ray crosses from a known medium into an unknown one:

1. Measure both angles from the normal.
2. Write $n_1\sin\theta_1=n_2\sin\theta_2$.
3. Isolate the unknown index before substituting.
4. Evaluate sines in degree mode and round only at the end.
5. Check the bending direction, then compare the result with the proposed material's reference index.

The main traps are swapping the sine ratio, using angles from the surface, and comparing raw angles instead of first calculating the refractive index.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
