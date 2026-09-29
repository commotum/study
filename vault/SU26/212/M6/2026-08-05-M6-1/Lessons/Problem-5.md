# Finding Wavelength from a Diffraction-Grating Pattern

<!--
lesson-id: 212-M6-005
topic-code: MTH212.M6.05
-->
## Table of Contents

- [Introduction](#introduction)
- [Turn Screen Position into an Angle](#turn-screen-position-into-an-angle)
- [Use the Bright-Fringe Order](#use-the-bright-fringe-order)
- [Combine the Geometry and Grating Equation](#combine-the-geometry-and-grating-equation)
- [Know When the Small-Angle Shortcut Fails](#know-when-the-small-angle-shortcut-fails)
- [Variant: First-Order Grating Data](#variant-first-order-grating-data)
- [Summary](#summary)

## Prerequisites

- Use right-triangle ratios and inverse tangent.
- Convert among centimeters, meters, micrometers, and nanometers.
- Recognize that the central maximum has order $m=0$, so the first, second, and third bright fringes have $m=1,2,3$.

---

<a id="introduction"></a>
## Introduction

When a problem gives a diffraction grating, a screen distance, and a bright fringe's displacement from the center, use the screen geometry to find the diffraction angle before applying the grating equation.

**Recognition cue:** the fringe is located by a displacement $y$ on a screen a perpendicular distance $L$ from the grating, while the question asks for the wavelength.

For a screen distance $L$ and perpendicular fringe displacement $y$,

$$
\tan\theta=\frac{y}{L}.
$$

For the bright fringe of order $m$ produced by grating spacing $d$,

$$
d\sin\theta=m\lambda.
$$

The reusable calculation chain is

$$
\theta=\tan^{-1}\left(\frac{y}{L}\right),
\qquad
\lambda=\frac{d\sin\theta}{m}.
$$

Keep $y$ and $L$ in the same length unit, use the fringe number for $m$, and convert the final wavelength to the requested unit.

---

<a id="turn-screen-position-into-an-angle"></a>
## Turn Screen Position into an Angle

Name the sides relative to the diffraction angle $\theta$ before choosing a ratio:

- opposite side: fringe displacement $y$;
- adjacent side: perpendicular screen distance $L$;
- hypotenuse: grating-to-fringe distance $\sqrt{L^2+y^2}$.

Because $y$ and $L$ are the opposite and adjacent sides, tangent is the direct geometric ratio.

**Example:** A bright fringe is $0.80\ \mathrm{m}$ above the central maximum on a screen $2.40\ \mathrm{m}$ from a grating. Find its diffraction angle.

**Explanation**

Use the perpendicular screen distance and the displacement from the central maximum:

$$
\theta
=\tan^{-1}\left(\frac{0.80}{2.40}\right)
=18.4^\circ.
$$

**Calculator check:** use degree mode, and keep the unrounded angle in the calculator if another operation follows.

The ratio $y/L$ is the tangent of the angle, not the angle itself and not its sine.

```quiz
type: radio
id: p5-screen-angle
content: |-
  A bright fringe is $0.50\ \mathrm{m}$ above the central maximum on a screen $1.50\ \mathrm{m}$ from a diffraction grating. What is the diffraction angle?
options:
- id: p5-screen-angle-a
  content: |-
    $0.333^\circ$
  feedback: |-
    The quotient $y/L=0.333$ is the value of $\tan\theta$, not an angle measured in degrees. Apply inverse tangent to the ratio: $\theta=\tan^{-1}(0.333)=18.4^\circ$.
- id: p5-screen-angle-b
  content: |-
    $18.4^\circ$
  correct: true
  feedback: |-
    The fringe displacement is opposite the angle and the screen distance is adjacent, so $\tan\theta=y/L$. Thus $\theta=\tan^{-1}(0.50/1.50)=18.4^\circ$.
- id: p5-screen-angle-c
  content: |-
    $19.5^\circ$
  feedback: |-
    This comes from applying inverse sine directly to $y/L$. The screen distance $L$ is the adjacent side, not the hypotenuse, so the geometric relation is $\tan\theta=y/L$, which gives $18.4^\circ$.
- id: p5-screen-angle-d
  content: |-
    $71.6^\circ$
  feedback: |-
    This swaps the opposite and adjacent sides and uses $\tan^{-1}(L/y)$. The angle is measured from the central axis, so the correct ratio is $y/L$ and the angle is $18.4^\circ$.
```

---

<a id="use-the-bright-fringe-order"></a>
## Use the Bright-Fringe Order

For normal incidence, bright diffraction-grating fringes obey

$$
d\sin\theta=m\lambda.
$$

Solve for wavelength by dividing by the order:

$$
\lambda=\frac{d\sin\theta}{m}.
$$

Since $|\sin\theta|\leq 1$, any result must satisfy $\lambda\leq d/m$. This is a quick check for a lost fringe order or an incorrect unit conversion.

**Example:** A grating has spacing $d=2.4\ \mu\mathrm{m}$. Its second-order bright fringe is at $\theta=30.0^\circ$. Find the wavelength.

**Explanation**

The second-order fringe means $m=2$:

$$
\lambda
=\frac{(2.4\ \mu\mathrm{m})\sin 30.0^\circ}{2}
=0.60\ \mu\mathrm{m}
=600\ \mathrm{nm}.
$$

```quiz
type: radio
id: p5-fringe-order
content: |-
  A grating has spacing $d=3.2\ \mu\mathrm{m}$. A second-order bright fringe occurs at $30.0^\circ$. What wavelength produced it?
options:
- id: p5-fringe-order-a
  content: |-
    $0.80\ \mathrm{nm}$
  feedback: |-
    The calculation gives $0.80\ \mu\mathrm{m}$, but this option labels that number as nanometers. Since $1\ \mu\mathrm{m}=1000\ \mathrm{nm}$, the requested wavelength is $800\ \mathrm{nm}$.
- id: p5-fringe-order-b
  content: |-
    $400\ \mathrm{nm}$
  feedback: |-
    This divides by the order twice. The equation $d\sin\theta=m\lambda$ requires one division by $m=2$, giving $0.80\ \mu\mathrm{m}=800\ \mathrm{nm}$.
- id: p5-fringe-order-c
  content: |-
    $800\ \mathrm{nm}$
  correct: true
  feedback: |-
    A grating maximum satisfies $d\sin\theta=m\lambda$. With $m=2$, $\lambda=(3.2\ \mu\mathrm{m})(0.500)/2=0.80\ \mu\mathrm{m}=800\ \mathrm{nm}$.
- id: p5-fringe-order-d
  content: |-
    $1600\ \mathrm{nm}$
  feedback: |-
    The value $d\sin\theta=1.6\ \mu\mathrm{m}$ equals $m\lambda$, not $\lambda$. Dividing by the second-order value $m=2$ gives $0.80\ \mu\mathrm{m}=800\ \mathrm{nm}$.
- id: p5-fringe-order-e
  content: |-
    $3200\ \mathrm{nm}$
  feedback: |-
    This multiplies by $m$ after applying the sine. Because $m\lambda=d\sin\theta$, wavelength is found by dividing by $m$, not multiplying: $\lambda=800\ \mathrm{nm}$.
```

---

<a id="combine-the-geometry-and-grating-equation"></a>
## Combine the Geometry and Grating Equation

The grating equation needs $\sin\theta$. In the screen triangle, the Pythagorean theorem gives the hypotenuse $\sqrt{L^2+y^2}$, so opposite over hypotenuse gives

$$
\sin\left(\tan^{-1}\frac{y}{L}\right)
=\frac{y}{\sqrt{L^2+y^2}}.
$$

Therefore, the two-step calculation can be compressed without making an approximation:

$$
\lambda
=\frac{d}{m}\sin\left(\tan^{-1}\frac{y}{L}\right)
=\frac{dy}{m\sqrt{L^2+y^2}}.
$$

**Example:** A second-order bright fringe is $1.50\ \mathrm{m}$ from the center on a screen $2.00\ \mathrm{m}$ away. The grating spacing is $4.0\ \mu\mathrm{m}$. Find the wavelength.

**Explanation**

The right triangle has hypotenuse

$$
\sqrt{(2.00)^2+(1.50)^2}=2.50\ \mathrm{m},
$$

so $\sin\theta=1.50/2.50=0.600$. Then

$$
\lambda
=\frac{(4.0\ \mu\mathrm{m})(0.600)}{2}
=1.2\ \mu\mathrm{m}
=1.2\times10^3\ \mathrm{nm}.
$$

```quiz
type: radio
id: p5-combined-chain
content: |-
  A second-order bright fringe is $4.0\ \mathrm{m}$ from the center on a screen $3.0\ \mathrm{m}$ from a grating. The grating spacing is $2.5\ \mu\mathrm{m}$. What is the wavelength?
options:
- id: p5-combined-chain-a
  content: |-
    $500\ \mathrm{nm}$
  feedback: |-
    This divides by the order twice. The $3$-$4$-$5$ geometry gives $\sin\theta=4/5$, and the grating equation requires only one division by $m=2$, producing $1000\ \mathrm{nm}$.
- id: p5-combined-chain-b
  content: |-
    $750\ \mathrm{nm}$
  feedback: |-
    This uses the adjacent-side ratio $3/5=\cos\theta$. The grating equation requires $\sin\theta$, which is opposite over hypotenuse: $4/5$. That gives $1000\ \mathrm{nm}$.
- id: p5-combined-chain-c
  content: |-
    $1000\ \mathrm{nm}$
  correct: true
  feedback: |-
    Exact screen geometry gives $\sin\theta=y/\sqrt{L^2+y^2}=4/5$. Then $\lambda=(2.5\ \mu\mathrm{m})(4/5)/2=1.0\ \mu\mathrm{m}=1000\ \mathrm{nm}$.
- id: p5-combined-chain-d
  content: |-
    $1667\ \mathrm{nm}$
  feedback: |-
    This substitutes $y/L=4/3$ for $\sin\theta$. The ratio $y/L$ is $\tan\theta$; exact geometry gives $\sin\theta=4/5$, so the wavelength is $1000\ \mathrm{nm}$.
- id: p5-combined-chain-e
  content: |-
    $2000\ \mathrm{nm}$
  feedback: |-
    The value $d\sin\theta=(2.5\ \mu\mathrm{m})(4/5)=2.0\ \mu\mathrm{m}$ equals $m\lambda$. Since this is a second-order fringe, divide by $m=2$ to obtain $1000\ \mathrm{nm}$.
```

---

<a id="know-when-the-small-angle-shortcut-fails"></a>
## Know When the Small-Angle Shortcut Fails

The shortcut $\sin\theta\approx\tan\theta\approx y/L$ is useful only when the angle is small. If $y$ is not much smaller than $L$, keep the exact geometry.

**Example:** A laser illuminates a grating with spacing $3.0\ \mu\mathrm{m}$. A screen is $1.8\ \mathrm{m}$ away, and the third bright fringe is $120\ \mathrm{cm}$ above the central maximum. Find the wavelength in nanometers.

**Explanation**

First put the screen measurements in the same unit: $120\ \mathrm{cm}=1.20\ \mathrm{m}$. Because $y/L=1.20/1.8=0.667$ is not small, find the exact angle:

$$
\theta_3
=\tan^{-1}\left(\frac{1.20}{1.8}\right)
=33.690\ldots^\circ.
$$

The third bright fringe has $m=3$. Keep the full calculator value of the angle—or enter the inverse tangent inside the sine—so intermediate rounding does not shift the final wavelength:

$$
\lambda
=\frac{(3.0\times10^{-6}\ \mathrm{m})
\sin\left(\tan^{-1}(1.20/1.8)\right)}{3}
=5.547\ldots\times10^{-7}\ \mathrm{m}.
$$

Since $1\ \mathrm{m}=10^9\ \mathrm{nm}$,

$$
\lambda=554.7\ldots\ \mathrm{nm}\approx 5.5\times10^2\ \mathrm{nm}.
$$

Entered as a number only, the answer is $550$.

```quiz
type: radio
id: p5-large-angle-check
content: |-
  A screen is $2.4\ \mathrm{m}$ from a grating. A third-order bright fringe is $1.0\ \mathrm{m}$ from the center, and the grating spacing is $3.9\ \mu\mathrm{m}$. What wavelength produced the fringe?
options:
- id: p5-large-angle-check-a
  content: |-
    $167\ \mathrm{nm}$
  feedback: |-
    This divides by the third-order value twice. Exact geometry gives $\sin\theta=1.0/2.6=5/13$, and one division by $m=3$ gives $500\ \mathrm{nm}$.
- id: p5-large-angle-check-b
  content: |-
    $385\ \mathrm{nm}$
  feedback: |-
    The number $0.385$ is the exact value of $\sin\theta$, not the wavelength in micrometers or nanometers. It must still be multiplied by $d=3.9\ \mu\mathrm{m}$ and divided by $m=3$, giving $500\ \mathrm{nm}$.
- id: p5-large-angle-check-c
  content: |-
    $500\ \mathrm{nm}$
  correct: true
  feedback: |-
    The $1.0$-$2.4$-$2.6$ screen triangle gives $\sin\theta=1.0/2.6=5/13$. For $m=3$, $\lambda=(3.9\ \mu\mathrm{m})(5/13)/3=0.50\ \mu\mathrm{m}=500\ \mathrm{nm}$.
- id: p5-large-angle-check-d
  content: |-
    $542\ \mathrm{nm}$
  feedback: |-
    This uses $y/L=0.417$ as though it were $\sin\theta$. That small-angle substitution is reliable only when $y\ll L$; here exact geometry gives $\sin\theta=1.0/2.6=0.385$, so the wavelength is $500\ \mathrm{nm}$.
- id: p5-large-angle-check-e
  content: |-
    $1200\ \mathrm{nm}$
  feedback: |-
    This uses $L/\sqrt{L^2+y^2}=2.4/2.6$, which is $\cos\theta$. The grating equation uses $\sin\theta=y/\sqrt{L^2+y^2}=1.0/2.6$, leading to $500\ \mathrm{nm}$.
- id: p5-large-angle-check-f
  content: |-
    $1500\ \mathrm{nm}$
  feedback: |-
    The value $d\sin\theta=(3.9\ \mu\mathrm{m})(5/13)=1.5\ \mu\mathrm{m}$ equals $m\lambda$, not $\lambda$. Divide by the third-order value $m=3$ to obtain $500\ \mathrm{nm}$.
```

---

<a id="variant-first-order-grating-data"></a>
## Variant: First-Order Grating Data

For a first-order maximum, set $m=1$ rather than dividing by a higher order. The screen geometry still determines the exact sine of the angle.

```quiz
type: blank
id: khadley-wave-optics-q3
input_mode: math
require_exact: true
content: |-
  A grating with line spacing $3.0\ \mu\mathrm{m}$ produces a first-order bright fringe $32\ \mathrm{cm}$ from the center on a screen $1.8\ \mathrm m$ away. Find the wavelength in nanometers: ==530==
feedback: |-
  The angle is $\theta=\tan^{-1}(0.32/1.8)$. The exact grating relation gives $\lambda=d\sin\theta=5.25\times10^{-7}\ \mathrm m$, or $5.3\times10^2\ \mathrm{nm}$ to two significant figures.
```

---

<a id="summary"></a>
## Summary

When a grating problem locates a bright fringe on a screen:

1. Convert $y$ and $L$ to the same unit.
2. In degree mode, use $\theta=\tan^{-1}(y/L)$, or equivalently $\sin\theta=y/\sqrt{L^2+y^2}$.
3. Translate the fringe number into its order $m$.
4. Solve $\lambda=d\sin\theta/m$.
5. Convert the wavelength to the requested unit and round only at the end.

Check that $\lambda\leq d/m$. The main trap is replacing $\sin\theta$ with $y/L$: that is only a small-angle approximation, so for a visibly displaced fringe, use the exact triangle.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 4 Study Guide](../../../M7/2026-08-13-Q-4/Study-Guide.md)
Next: [Finding Diffraction-Grating Line Density from Symmetric Fringes](../../2026-08-06-M6-2/Lessons/Problem-2.md)

Study guide index: 04/8

---
<!-- lesson-nav:end -->
