# Doppler Shift from Wavelength

<!--
lesson-id: 212-M5-054
topic-code: MTH212.M5.54
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Direction from the Wavelength Shift](#read-the-direction-from-the-wavelength-shift)
- [Turn the Fractional Shift into Radial Velocity](#turn-the-fractional-shift-into-radial-velocity)
- [Keep Units and Precision Under Control](#keep-units-and-precision-under-control)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Use the wave relation $c=f\lambda$ to connect wavelength and frequency for light.
- Interpret a negative signed velocity as motion in the direction opposite the chosen positive direction.
- Form a dimensionless ratio from two quantities measured in the same units.
- Round only after completing the calculation.

---

<a id="introduction"></a>
## Introduction

A spectral line has a known laboratory wavelength $\lambda_0$. If the same line from a galaxy is observed at a different wavelength $\lambda_{\mathrm{obs}}$, the shift reveals the galaxy's radial motion.

The source places the full wavelength Doppler representation beside the problem:

![[../Source/Images/waveeqn8.jpg]]

The problem specifically asks for the **nonrelativistic Doppler approximation**. With positive radial velocity defined as motion away from Earth, use

$$
\frac{v_r}{c}\approx
\frac{\lambda_{\mathrm{obs}}-\lambda_0}{\lambda_0}.
$$

The core move has two parts:

1. Compute the signed fractional wavelength shift using **observed minus laboratory**.
2. Multiply that dimensionless shift by $c$ and interpret the sign.

It helps to name the fraction

$$
z=\frac{\Delta\lambda}{\lambda_0}
=\frac{\lambda_{\mathrm{obs}}-\lambda_0}{\lambda_0}.
$$

The quantities have distinct roles:

- $\lambda_{\mathrm{obs}}$ is the measured wavelength,
- $\lambda_0$ is the fixed laboratory reference,
- $z$ is the dimensionless fractional comparison,
- $c$ is the proportionality constant with velocity units, and
- $v_r$ is the requested signed radial velocity.

The denominator must be the reference wavelength $\lambda_0$, not the observed wavelength. It sets the scale of the comparison: for a fixed wavelength change, a larger reference wavelength gives a smaller fractional shift.

Once $z$ is known, radial velocity varies directly with it:

$$
v_r\approx cz.
$$

Thus $c$ converts the dimensionless shift into a velocity while preserving its sign.

---

<a id="read-the-direction-from-the-wavelength-shift"></a>
## Read the Direction from the Wavelength Shift

**Example:** A line has laboratory wavelength $500.0\ \mathrm{nm}$ and observed wavelength $504.0\ \mathrm{nm}$. Determine the direction of the galaxy's motion.

**Explanation**

Compare the observed wavelength with the laboratory wavelength:

$$
\Delta\lambda
=\lambda_{\mathrm{obs}}-\lambda_0
=504.0\ \mathrm{nm}-500.0\ \mathrm{nm}
=+4.0\ \mathrm{nm}.
$$

The observed wavelength is longer, so the light is **redshifted**. The fractional shift is positive, which means $v_r>0$ under the chosen convention. The galaxy is receding.

The direction rules are therefore

$$
\begin{array}{ccl}
\lambda_{\mathrm{obs}}>\lambda_0
&\Longrightarrow&
\text{redshift, receding, }v_r>0,\\[4pt]
\lambda_{\mathrm{obs}}<\lambda_0
&\Longrightarrow&
\text{blueshift, approaching, }v_r<0.
\end{array}
$$

```quiz
type: radio
id: wavelength-shift-direction
shuffle: true
content: |-
  A spectral line is observed at $504.0\ \mathrm{nm}$, while its laboratory wavelength is $500.0\ \mathrm{nm}$. Which signed fractional shift and direction are correct?
options:
- id: positive-receding
  content: |-
    $z=+0.0080$; the galaxy is receding.
  correct: true
  feedback: |-
    A longer observed wavelength is a redshift. Here $z=(504.0-500.0)/500.0=+0.0080$, so $v_r\approx cz$ is positive and the galaxy is receding.
- id: negative-approaching
  content: |-
    $z=-0.0080$; the galaxy is approaching.
  feedback: |-
    This subtracts in the reverse order. The convention is observed minus laboratory: $(504.0-500.0)/500.0=+0.0080$. The positive redshift corresponds to recession.
- id: positive-approaching
  content: |-
    $z=+0.0080$; the galaxy is approaching.
  feedback: |-
    The fractional-shift calculation is correct, but its direction is not. A positive shift means the observed wavelength is longer, so the line is redshifted and the galaxy is receding.
- id: negative-receding
  content: |-
    $z=-0.0080$; the galaxy is receding.
  feedback: |-
    Recession does correspond to a positive redshift, but the stated sign is negative. Using observed minus laboratory gives $z=+0.0080$, consistent with recession.
```

---

<a id="turn-the-fractional-shift-into-radial-velocity"></a>
## Turn the Fractional Shift into Radial Velocity

**Example:** A galaxy's spectral line has fractional shift $z=-2.0\times10^{-3}$. Find its radial velocity using $c=3.00\times10^8\ \mathrm{m/s}$.

**Explanation**

Start from the nonrelativistic approximation and isolate the requested variable. Treat $c$ and $z$ as known quantities, then multiply both sides by $c$:

$$
\begin{aligned}
\frac{v_r}{c}&\approx z\\
c\left(\frac{v_r}{c}\right)&\approx cz\\
v_r&\approx cz.
\end{aligned}
$$

Now substitute the given fractional shift:

$$
\begin{aligned}
v_r&\approx cz\\
&=(3.00\times10^8\ \mathrm{m/s})
(-2.0\times10^{-3})\\
&=-6.0\times10^5\ \mathrm{m/s}.
\end{aligned}
$$

The negative sign is part of the answer: it indicates motion toward Earth. Thus the galaxy is approaching at a speed of $6.0\times10^5\ \mathrm{m/s}$, or equivalently has radial velocity $-6.0\times10^5\ \mathrm{m/s}$.

```quiz
type: radio
id: radial-velocity-from-fractional-shift
shuffle: true
content: |-
  A galaxy has fractional wavelength shift $z=-2.0\times10^{-3}$. Using $c=3.00\times10^8\ \mathrm{m/s}$, which radial velocity and direction are correct?
options:
- id: negative-six-e-five-approaching
  content: |-
    $v_r=-6.0\times10^5\ \mathrm{m/s}$; approaching.
  correct: true
  feedback: |-
    In the nonrelativistic limit, $v_r\approx cz$. Multiplying $-2.0\times10^{-3}$ by $3.00\times10^8\ \mathrm{m/s}$ gives $-6.0\times10^5\ \mathrm{m/s}$; the negative sign means approaching.
- id: positive-six-e-five-receding
  content: |-
    $v_r=+6.0\times10^5\ \mathrm{m/s}$; receding.
  feedback: |-
    This drops the negative sign of the wavelength shift. Since $c$ is positive, $v_r=cz$ must have the same sign as $z$, so the radial velocity is negative and the galaxy is approaching.
- id: negative-six-e-five-receding
  content: |-
    $v_r=-6.0\times10^5\ \mathrm{m/s}$; receding.
  feedback: |-
    The numerical velocity is correct, but its interpretation is reversed. With positive defined as away from Earth, a negative radial velocity indicates approach, not recession.
- id: fractional-shift-as-speed
  content: |-
    $v_r=-2.0\times10^{-3}\ \mathrm{m/s}$; approaching.
  feedback: |-
    The value $-2.0\times10^{-3}$ is the dimensionless fractional shift, not a velocity. Multiplying it by $c$ supplies velocity units and gives $-6.0\times10^5\ \mathrm{m/s}$.
- id: divide-by-light-speed
  content: |-
    $v_r=-6.7\times10^{-12}\ \mathrm{m/s}$; approaching.
  feedback: |-
    This divides the fractional shift by $c$. The relationship is $v_r/c\approx z$, so solving for velocity requires multiplication: $v_r\approx cz=-6.0\times10^5\ \mathrm{m/s}$.
```

---

<a id="keep-units-and-precision-under-control"></a>
## Keep Units and Precision Under Control

**Example:** A line is observed at $478.8\ \mathrm{nm}$ instead of its laboratory value $480.0\ \mathrm{nm}$. Find the radial velocity.

**Explanation**

Both wavelengths use nanometers, so their units cancel in the fractional shift:

$$
\begin{aligned}
z
&=\frac{478.8\ \mathrm{nm}-480.0\ \mathrm{nm}}
{480.0\ \mathrm{nm}}\\
&=\frac{-1.2}{480.0}\\
&=-2.5\times10^{-3}.
\end{aligned}
$$

There is no need to convert each wavelength to meters because the ratio is dimensionless. Now multiply by $c$:

$$
\begin{aligned}
v_r
&\approx (3.00\times10^8\ \mathrm{m/s})
(-2.5\times10^{-3})\\
&=-7.5\times10^5\ \mathrm{m/s}.
\end{aligned}
$$

The subtraction gives $-1.2\ \mathrm{nm}$, which supports two significant figures. Keep guard digits in the ratio, then round the final velocity.

```quiz
type: radio
id: wavelength-shift-units-and-precision
shuffle: true
content: |-
  A line is observed at $478.8\ \mathrm{nm}$ rather than $480.0\ \mathrm{nm}$. Using $c=3.00\times10^8\ \mathrm{m/s}$, which result is correct?
options:
- id: negative-seven-five-e-five
  content: |-
    $v_r=-7.5\times10^5\ \mathrm{m/s}$; approaching.
  correct: true
  feedback: |-
    The shift is $z=(478.8-480.0)/480.0=-2.5\times10^{-3}$. Multiplying by $c$ gives $-7.5\times10^5\ \mathrm{m/s}$, and the negative sign identifies approach.
- id: positive-seven-five-e-five
  content: |-
    $v_r=+7.5\times10^5\ \mathrm{m/s}$; receding.
  feedback: |-
    This loses the sign of the blueshift. Because the observed wavelength is shorter, observed minus laboratory is negative, so the radial velocity must be $-7.5\times10^5\ \mathrm{m/s}$ and the galaxy is approaching.
- id: negative-two-five-e-three
  content: |-
    $v_r=-2.5\times10^{-3}\ \mathrm{m/s}$; approaching.
  feedback: |-
    The number $-2.5\times10^{-3}$ is $z$, the dimensionless wavelength ratio. It must be multiplied by $c$ to become the velocity $-7.5\times10^5\ \mathrm{m/s}$.
- id: negative-seven-five-e-eight
  content: |-
    $v_r=-7.5\times10^8\ \mathrm{m/s}$; approaching.
  feedback: |-
    This introduces an extra factor of $10^3$ even though the nanometer units already cancel between numerator and denominator. The dimensionless shift is $-0.0025$, so the speed is well below $c$: $-7.5\times10^5\ \mathrm{m/s}$.
- id: negative-seven-five-e-five-receding
  content: |-
    $v_r=-7.5\times10^5\ \mathrm{m/s}$; receding.
  feedback: |-
    The magnitude and sign are correct, but the direction label conflicts with the convention. A negative radial velocity is motion toward Earth, so the galaxy is approaching.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the source problem in its original open-response form before using the multiple-choice check.

> A galaxy's hydrogen-alpha line is observed at $654.0\ \mathrm{nm}$, compared with $656.3\ \mathrm{nm}$ in the laboratory. Is the galaxy approaching or receding, and what is its radial velocity? Use the nonrelativistic Doppler approximation.

The answer form asks for both a direction and a signed radial velocity.

**Explanation**

First find the signed wavelength change:

$$
\Delta\lambda
=654.0\ \mathrm{nm}-656.3\ \mathrm{nm}
=-2.3\ \mathrm{nm}.
$$

The shorter observed wavelength is a blueshift, so the galaxy is approaching. Next calculate the fractional shift and velocity:

$$
\begin{aligned}
z
&=\frac{-2.3\ \mathrm{nm}}{656.3\ \mathrm{nm}}
=-0.003504\ldots,\\
v_r
&\approx (3.00\times10^8\ \mathrm{m/s})(-0.003504\ldots)\\
&=-1.051\ldots\times10^6\ \mathrm{m/s}\\
&\approx -1.1\times10^6\ \mathrm{m/s}.
\end{aligned}
$$

Therefore, the galaxy is **approaching**, with radial velocity

$$
\boxed{v_r\approx-1.1\times10^6\ \mathrm{m/s}},
$$

where the negative sign denotes motion toward Earth.

```quiz
type: radio
id: khadley-doppler-q3
shuffle: true
content: |-
  Which response correctly gives both the direction and signed radial velocity for the hydrogen-alpha observation?
options:
- id: approaching-negative-one-one-e-six
  content: |-
    Approaching; $v_r\approx-1.1\times10^6\ \mathrm{m/s}$.
  correct: true
  feedback: |-
    A shorter observed wavelength is a blueshift. Using $v_r/c\approx(654.0-656.3)/656.3$ gives $v_r\approx-1.1\times10^6\ \mathrm{m/s}$, whose negative sign denotes motion toward Earth.
- id: receding-positive-one-one-e-six
  content: |-
    Receding; $v_r\approx+1.1\times10^6\ \mathrm{m/s}$.
  feedback: |-
    This reverses the wavelength subtraction. Since $654.0\ \mathrm{nm}<656.3\ \mathrm{nm}$, the line is blueshifted; observed minus laboratory is negative, so the galaxy is approaching with negative radial velocity.
- id: approaching-positive-one-one-e-six
  content: |-
    Approaching; $v_r\approx+1.1\times10^6\ \mathrm{m/s}$.
  feedback: |-
    The direction and speed magnitude are right, but the sign conflicts with the stated convention. Motion toward Earth is negative radial velocity, so the signed answer must be $-1.1\times10^6\ \mathrm{m/s}$.
- id: approaching-negative-one-one-e-three
  content: |-
    Approaching; $v_r\approx-1.1\times10^3\ \mathrm{m/s}$.
  feedback: |-
    This uses $3.00\times10^5$ as though it were the speed of light in meters per second. That value is $c$ in kilometers per second; using $c=3.00\times10^8\ \mathrm{m/s}$ gives $-1.1\times10^6\ \mathrm{m/s}$.
- id: approaching-negative-three-five-e-three
  content: |-
    Approaching; $v_r\approx-3.5\times10^{-3}\ \mathrm{m/s}$.
  feedback: |-
    The value near $-3.5\times10^{-3}$ is the dimensionless fractional wavelength shift, not the radial velocity. Multiplying it by $c$ gives $-1.1\times10^6\ \mathrm{m/s}$.
```

---

<a id="summary"></a>
## Summary

- Write the shift in the order $\Delta\lambda=\lambda_{\mathrm{obs}}-\lambda_0$.
- A longer observed wavelength is a redshift: the object is receding and $v_r>0$.
- A shorter observed wavelength is a blueshift: the object is approaching and $v_r<0$.
- For nonrelativistic radial motion, use
  $$
  \frac{v_r}{c}\approx
  \frac{\lambda_{\mathrm{obs}}-\lambda_0}{\lambda_0}.
  $$
- Wavelength units cancel in the fractional shift; multiplying by $c$ supplies velocity units.
- Keep the sign throughout the calculation and round only the final velocity.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
