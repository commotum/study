# Calculating Refraction Between Air and Water

<!--
lesson-id: 212-M7-016
topic-code: MTH212.M7.16
-->

## Table of Contents

- [Introduction](#introduction)
- [Match Each Angle to Its Medium](#match-each-angle-to-its-medium)
- [Isolate the Sine of the Unknown Angle](#isolate-the-sine-of-the-unknown-angle)
- [Use Inverse Sine in Degree Mode](#use-inverse-sine-in-degree-mode)
- [Check the Bending Direction](#check-the-bending-direction)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Measure incidence and refraction angles from the normal.
- Rearrange a product equation for one factor.
- Evaluate sine and inverse sine on a calculator.
- Round a calculated angle to the requested precision.

---

<a id="introduction"></a>
## Introduction

When light crosses an interface, Snell's law pairs each medium's refractive index with the ray angle in that same medium:

$$
\boxed{n_1\sin\theta_1=n_2\sin\theta_2}.
$$

Every angle is measured from the normal, the line perpendicular to the boundary. For a ray traveling from water into air,

$$
n_{\text{water}}\sin\theta_{\text{water}}
=n_{\text{air}}\sin\theta_{\text{air}}.
$$

If the air angle is known, isolate the water angle:

$$
\boxed{
\theta_{\text{water}}
=\sin^{-1}\left(
\frac{n_{\text{air}}}{n_{\text{water}}}
\sin\theta_{\text{air}}
\right)}.
$$

The recognition cue is a known index in each medium, one known normal-based angle, and one requested ray angle. Match each angle to its medium, isolate the sine of the unknown, use inverse sine in degree mode, then check the result against the bending direction.

---

<a id="match-each-angle-to-its-medium"></a>
## Match Each Angle to Its Medium

**Example:** A ray travels from a liquid with $n_{\text{liquid}}=1.40$ into air with $n_{\text{air}}=1.00$. The ray angle in air is $45^\circ$. Write the correct Snell's-law equation.

**Explanation**

The given $45^\circ$ angle belongs to the air side, so it must be paired with $n_{\text{air}}$:

$$
(1.40)\sin\theta_{\text{liquid}}
=(1.00)\sin45^\circ.
$$

The order of the two sides does not matter, but each index must remain next to the sine of the angle measured in that same medium. The ray's travel direction does not change this pairing.

```quiz
type: radio
id: air-water-snell-pairing
shuffle: true
content: |-
  Light travels from water $(n=1.33)$ into air $(n=1.00)$. Its angle in air is $40^\circ$. Which equation correctly represents Snell's law?
options:
- id: water-unknown-air-forty
  content: |-
    $(1.33)\sin\theta_{\mathrm{water}}=(1.00)\sin40^\circ$
  correct: true
  feedback: |-
    Snell's law pairs each index with the angle in that medium. The unknown water angle belongs with $1.33$, while the given $40^\circ$ air angle belongs with $1.00$.
- id: water-forty-air-unknown
  content: |-
    $(1.33)\sin40^\circ=(1.00)\sin\theta_{\mathrm{water}}$
  feedback: |-
    This attaches the known air angle to the water index. The angle and index must come from the same side of the interface, so $40^\circ$ belongs with $n_{\mathrm{air}}=1.00$.
- id: indices-inside-sine
  content: |-
    $\sin(1.33\theta_{\mathrm{water}})=\sin(1.00(40^\circ))$
  feedback: |-
    Refractive index multiplies the sine value; it is not part of the sine's angle. Snell's law has the form $n\sin\theta$, not $\sin(n\theta)$.
- id: add-sine-terms
  content: |-
    $1.33+\sin\theta_{\mathrm{water}}=1.00+\sin40^\circ$
  feedback: |-
    Snell's law uses products of index and sine. Adding the index to the sine does not express refraction at the boundary.
- id: omit-air-index
  content: |-
    $(1.33)\sin\theta_{\mathrm{water}}=\sin(1.00^\circ)$
  feedback: |-
    This treats the air index as an angle and discards the given $40^\circ$. The correct air-side term is $(1.00)\sin40^\circ$.
```

---

<a id="isolate-the-sine-of-the-unknown-angle"></a>
## Isolate the Sine of the Unknown Angle

**Example:** Isolate $\theta_{\text{liquid}}$ in

$$
(1.40)\sin\theta_{\text{liquid}}
=(1.00)\sin45^\circ.
$$

**Explanation**

First divide by the coefficient multiplying the unknown sine:

$$
\sin\theta_{\text{liquid}}
=\frac{1.00}{1.40}\sin45^\circ.
$$

Then apply inverse sine to the entire right-hand side:

$$
\theta_{\text{liquid}}
=\sin^{-1}\left(
\frac{1.00}{1.40}\sin45^\circ
\right).
$$

The index ratio is air over liquid because the liquid index was divided away from the left side. Do not take the reciprocal unless the unknown angle is on the other side of the boundary.

```quiz
type: radio
id: isolate-refracted-angle
shuffle: true
content: |-
  For $(1.50)\sin\theta_{\mathrm{liquid}}=(1.00)\sin60^\circ$, which expression correctly isolates the liquid angle?
options:
- id: inverse-sine-one-over-one-point-five
  content: |-
    $\theta_{\mathrm{liquid}}=\sin^{-1}\left(\dfrac{1.00}{1.50}\sin60^\circ\right)$
  correct: true
  feedback: |-
    Divide both sides by $1.50$ to isolate $\sin\theta_{\mathrm{liquid}}$, then apply inverse sine to the full result. This gives the factor $1.00/1.50$ inside $\sin^{-1}$.
- id: inverse-sine-one-point-five-over-one
  content: |-
    $\theta_{\mathrm{liquid}}=\sin^{-1}\left(\dfrac{1.50}{1.00}\sin60^\circ\right)$
  feedback: |-
    This reverses the index ratio. The coefficient $1.50$ multiplies the unknown sine and must be divided out, so it belongs in the denominator.
- id: sine-not-inverse
  content: |-
    $\theta_{\mathrm{liquid}}=\sin\left(\dfrac{1.00}{1.50}\sin60^\circ\right)$
  feedback: |-
    After isolating $\sin\theta_{\mathrm{liquid}}$, the inverse sine function is needed to recover the angle. Applying sine again does not undo the first sine.
- id: inverse-sine-ratio-only
  content: |-
    $\theta_{\mathrm{liquid}}=\sin^{-1}\left(\dfrac{1.00}{1.50}\right)\sin60^\circ$
  feedback: |-
    Inverse sine must act on the complete value of $\sin\theta_{\mathrm{liquid}}$. Pulling $\sin60^\circ$ outside changes the expression and is not an inverse-function rule.
- id: divide-angle-directly
  content: |-
    $\theta_{\mathrm{liquid}}=\dfrac{1.00}{1.50}(60^\circ)$
  feedback: |-
    Snell's law relates sines of angles, not the angles themselves. Directly scaling $60^\circ$ is only a small-angle approximation and is not appropriate here.
```

---

<a id="use-inverse-sine-in-degree-mode"></a>
## Use Inverse Sine in Degree Mode

**Example:** Evaluate the liquid angle for

$$
(1.40)\sin\theta_{\text{liquid}}
=(1.00)\sin45^\circ.
$$

**Explanation**

Set the calculator to degree mode and keep guard digits:

$$
\begin{aligned}
\theta_{\text{liquid}}
&=\sin^{-1}\left(
\frac{1.00}{1.40}\sin45^\circ
\right)\\
&=\sin^{-1}(0.505076\ldots)\\
&=30.34^\circ\ldots
\end{aligned}
$$

To the nearest degree,

$$
\boxed{\theta_{\text{liquid}}=30^\circ}.
$$

A radian-mode calculator would display about $0.529$, which is the same angle in radians but does not match a response requested in degrees.

```quiz
type: radio
id: inverse-sine-degree-mode
shuffle: true
content: |-
  Light travels from a liquid with $n=1.50$ into air with $n=1.00$. Its angle in air is $60^\circ$. What is its angle in the liquid, rounded to the nearest degree?
options:
- id: liquid-angle-35
  content: |-
    $35^\circ$
  correct: true
  feedback: |-
    Snell's law gives $\theta_{\mathrm{liquid}}=\sin^{-1}[(1.00/1.50)\sin60^\circ]=35.26^\circ\ldots$. Keeping guard digits and rounding in degree mode gives $35^\circ$.
- id: liquid-angle-60
  content: |-
    $60^\circ$
  feedback: |-
    Equal angles would require equal indices for an oblique ray. The liquid has the higher index, so its ray angle must be smaller than the $60^\circ$ air angle.
- id: liquid-angle-90
  content: |-
    $90^\circ$
  feedback: |-
    This adds the two index values or treats the boundary as a critical-angle condition. Direct Snell's-law substitution gives a sine value below $1$ and an angle of about $35^\circ$.
- id: liquid-angle-052
  content: |-
    $0.52^\circ$
  feedback: |-
    A value near $0.62$ is the radian measure of the correct angle, not a degree value, and $0.52^\circ$ is neither. The prompt requires degree mode and nearest-degree output.
- id: liquid-angle-42
  content: |-
    $42^\circ$
  feedback: |-
    About $42^\circ$ is the critical angle for a $1.50$-to-$1.00$ boundary, which applies when the air-side ray is at $90^\circ$. Here the air angle is only $60^\circ$, so Snell's law gives $35.26^\circ\ldots$, rounded to $35^\circ$.
```

---

<a id="check-the-bending-direction"></a>
## Check the Bending Direction

**Example:** Light travels from water $(n=1.33)$ into air $(n=1.00)$. Should its air angle be larger or smaller than its water angle?

**Explanation**

Air has the lower refractive index. When light enters a lower-index medium, it bends away from the normal. Therefore,

$$
\theta_{\text{air}}>\theta_{\text{water}}.
$$

This provides a fast check on an inverse-sine calculation. If the known air angle is $50^\circ$, a computed water angle must be below $50^\circ$. A result above $50^\circ$ usually indicates that the index ratio was reversed.

The inverse-sine input also must satisfy

$$
0\le
\frac{n_{\text{air}}}{n_{\text{water}}}
\sin\theta_{\text{air}}
\le1.
$$

If a reversed ratio produces a value greater than $1$, that is an algebra or physical warning rather than a valid real angle.

```quiz
type: radio
id: air-water-bending-check
shuffle: true
content: |-
  A calculation for light traveling from water into air gives $\theta_{\mathrm{water}}=62^\circ$ when $\theta_{\mathrm{air}}=48^\circ$. What is the best diagnosis?
options:
- id: water-angle-too-large
  content: |-
    The result is inconsistent; the water angle should be smaller than the air angle.
  correct: true
  feedback: |-
    Light leaving higher-index water for lower-index air bends away from the normal, so $\theta_{\mathrm{air}}>\theta_{\mathrm{water}}$. A $62^\circ$ water angle with a $48^\circ$ air angle reverses that physical order.
- id: water-angle-larger-correct
  content: |-
    The result is consistent because water has the larger index.
  feedback: |-
    A larger index corresponds to the smaller angle in Snell's law. Water's larger index means the water angle should be smaller, not larger, than the air angle.
- id: angles-must-equal
  content: |-
    Both angles must equal $48^\circ$ because the same ray crosses the boundary.
  feedback: |-
    The ray is continuous, but its direction changes when the indices differ. Equal oblique angles would require equal indices, which air and water do not have.
- id: add-indices
  content: |-
    The angles should add to $1.33+1.00=2.33^\circ$.
  feedback: |-
    Refractive indices are dimensionless multipliers in Snell's law and are not added to obtain an angle. The physical comparison comes from bending away from the normal.
- id: cannot-check-without-wavelength
  content: |-
    The result cannot be checked without the light's wavelength.
  feedback: |-
    The supplied refractive indices already determine the bending relation for this comparison. Wavelength is unnecessary for the check that the air angle must exceed the water angle.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the original one-blank degree problem before checking the choices.

**Explanation**

> **Question 5**
>
> A fish is viewed from air along a ray that makes $50^\circ$ with the normal in air. For water with $n=1.33$, find the ray angle in the water. Enter degrees: ______
>
> ![[../Source/Images/spearfish1.jpg]]

The source requests one numerical degree entry. Pair $50^\circ$ with air, use $n_{\text{air}}=1.00$, isolate the water angle, retain calculator guard digits, and round to the nearest degree.

```quiz
type: radio
id: khadley-snells-law-q5
shuffle: true
content: |-
  Which value belongs in the original problem's “Enter degrees” blank?
options:
- id: original-35
  content: |-
    $35$
  correct: true
  feedback: |-
    Snell's law gives $1.33\sin\theta_{\mathrm{water}}=1.00\sin50^\circ$. Thus $\theta_{\mathrm{water}}=\sin^{-1}[(1.00/1.33)\sin50^\circ]=35.2^\circ\ldots$, which rounds to the required entry $35$.
- id: original-50
  content: |-
    $50$
  feedback: |-
    Equal oblique angles would require equal refractive indices. Because water has the larger index, its ray angle is smaller than the given $50^\circ$ air angle.
- id: original-65
  content: |-
    $65$
  feedback: |-
    This is approximately the complementary angle to the correct result and suggests measuring from the interface. The prompt and Snell's law use angles from the normal, giving about $35.2^\circ$.
- id: original-80
  content: |-
    $80$
  feedback: |-
    This can result from reversing the index ratio inside inverse sine. Water's larger index belongs in the denominator when isolating $\sin\theta_{\mathrm{water}}$, producing an angle below $50^\circ$.
- id: original-061
  content: |-
    $0.61$
  feedback: |-
    A value near $0.61$ is the correct angle expressed in radians. The source explicitly asks for degrees, so the calculator result must be reported as about $35^\circ$, entered as $35$.
```

---

<a id="summary"></a>
## Summary

To find a water angle from a known air angle:

1. Pair each index and angle with its medium:
   $$
   n_{\text{water}}\sin\theta_{\text{water}}
   =n_{\text{air}}\sin\theta_{\text{air}}.
   $$
2. Divide by $n_{\text{water}}$:
   $$
   \sin\theta_{\text{water}}
   =\frac{n_{\text{air}}}{n_{\text{water}}}
   \sin\theta_{\text{air}}.
   $$
3. Apply inverse sine to the complete right-hand side in degree mode.
4. Keep guard digits, then round once.
5. Check that the angle is smaller in the higher-index medium.

The main traps are pairing an angle with the wrong medium, reversing the index ratio, using sine instead of inverse sine, measuring from the interface, or reporting radians when degrees were requested.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
