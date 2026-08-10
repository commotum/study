# How Mass and Stiffness Affect SHM Frequency

<!--
lesson-id: 212-M4-031
topic-code: MTH212.M4.31
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Frequency as a Variation Formula](#read-the-frequency-as-a-variation-formula)
- [Increase the Mass](#increase-the-mass)
- [Increase the Spring Stiffness](#increase-the-spring-stiffness)
- [Recognize an Absent Parameter](#recognize-an-absent-parameter)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Know the ideal mass–spring frequency formula $f=(1/2\pi)\sqrt{k/m}$.
- Interpret a positive power as direct dependence and a negative power as inverse dependence.
- Apply the exponent rule $(ab)^p=a^pb^p$ to scaling factors.
- Hold all quantities fixed except the one named in a comparison.

---

<a id="introduction"></a>
## Introduction

For an ideal horizontal mass–spring oscillator, the frequency is

$$
f=\frac{1}{2\pi}\sqrt{\frac{k}{m}},
$$

where $k$ is the spring stiffness and $m$ is the oscillating mass. The source problem asks how frequency changes when mass increases, stiffness increases, or gravitational acceleration increases.

The recognition cue is a **change-one-parameter** question. Rewrite the formula as a variation map,

$$
f\propto k^{1/2}m^{-1/2},
$$

then use three tests:

1. A positive exponent means increasing that parameter increases $f$.
2. A negative exponent means increasing that parameter decreases $f$.
3. A parameter absent from the ideal formula does not change $f$ when the model remains the same.

For a before-and-after comparison, the same dependencies combine into one ratio:

$$
\frac{f_{\mathrm{new}}}{f_{\mathrm{old}}}
=\sqrt{\frac{k_{\mathrm{new}}}{k_{\mathrm{old}}}
\frac{m_{\mathrm{old}}}{m_{\mathrm{new}}}}.
$$

This ratio makes the variable roles visible: the stiffness factor appears in the direct order, while the mass factor appears in the inverse order.

---

<a id="read-the-frequency-as-a-variation-formula"></a>
## Read the Frequency as a Variation Formula

**Example:** Rewrite $f=(1/2\pi)\sqrt{k/m}$ so the dependence on $k$ and $m$ is visible.

**Explanation**

Use the square root as a one-half power:

$$
\begin{aligned}
f
&=\frac{1}{2\pi}\left(\frac{k}{m}\right)^{1/2}\\
&=\frac{1}{2\pi}k^{1/2}m^{-1/2}.
\end{aligned}
$$

The constant $1/(2\pi)$ does not affect increase-versus-decrease comparisons. The exponent $+1/2$ makes frequency increase with stiffness, while $-1/2$ makes frequency decrease with mass.

```quiz
type: radio
id: shm-frequency-variation-map
shuffle: true
content: |-
  Which proportionality correctly exposes how an ideal mass–spring frequency depends on $k$ and $m$?
options:
- id: k-positive-m-negative-half
  content: |-
    $f\propto k^{1/2}m^{-1/2}$
  correct: true
  feedback: |-
    The square root gives both quantities a one-half power, and division by $m$ makes its exponent negative. Thus stiffness raises frequency while mass lowers it.
- id: both-positive-half
  content: |-
    $f\propto k^{1/2}m^{1/2}$
  feedback: |-
    This turns the denominator mass into a numerator factor. Since $m$ is under the square root in the denominator, its exponent is $-1/2$, not $+1/2$.
- id: k-negative-m-positive-half
  content: |-
    $f\propto k^{-1/2}m^{1/2}$
  feedback: |-
    This reverses the ratio inside the root. The actual formula contains $k/m$, so $k$ has the positive exponent and $m$ the negative exponent.
- id: both-linear
  content: |-
    $f\propto km^{-1}$
  feedback: |-
    This preserves the ratio direction but drops the square root. Frequency responds by square-root factors, not linearly, so the exponents must be $+1/2$ and $-1/2$.
- id: include-gravity
  content: |-
    $f\propto gk^{1/2}m^{-1/2}$
  feedback: |-
    The ideal horizontal mass–spring frequency contains no $g$. Gravity affects the vertical support force, but it does not enter this horizontal restoring-frequency formula.
```

---

<a id="increase-the-mass"></a>
## Increase the Mass

**Example:** Determine how frequency changes if the mass is multiplied by a factor $a>1$ while $k$ remains fixed.

**Explanation**

Substitute $m_{\mathrm{new}}=am$:

$$
\begin{aligned}
f_{\mathrm{new}}
&=\frac{1}{2\pi}\sqrt{\frac{k}{am}}\\
&=\frac{1}{\sqrt a}\frac{1}{2\pi}\sqrt{\frac{k}{m}}\\
&=\frac{f_{\mathrm{old}}}{\sqrt a}.
\end{aligned}
$$

For $a>1$, the factor $1/\sqrt a$ is less than one, so increasing mass decreases frequency. Physically, more inertia makes the oscillator respond more slowly to the same restoring stiffness.

```quiz
type: radio
id: shm-double-mass-frequency
shuffle: true
content: |-
  The mass is doubled while the spring constant remains fixed. How does the frequency change?
options:
- id: divide-square-root-two
  content: |-
    $f_{\mathrm{new}}=\dfrac{f_{\mathrm{old}}}{\sqrt2}$
  correct: true
  feedback: |-
    Mass enters frequency as $m^{-1/2}$. Multiplying $m$ by $2$ therefore multiplies $f$ by $2^{-1/2}=1/\sqrt2$, so the frequency decreases.
- id: multiply-square-root-two
  content: |-
    $f_{\mathrm{new}}=\sqrt2\,f_{\mathrm{old}}$
  feedback: |-
    This uses a positive mass exponent, but mass appears in the denominator. Doubling inertia reduces the frequency by $1/\sqrt2$ rather than increasing it.
- id: divide-two
  content: |-
    $f_{\mathrm{new}}=\dfrac12f_{\mathrm{old}}$
  feedback: |-
    The direction is correct, but the dependence is not linear. Because mass lies under a square root, doubling it produces the factor $1/\sqrt2$, not $1/2$.
- id: multiply-two
  content: |-
    $f_{\mathrm{new}}=2f_{\mathrm{old}}$
  feedback: |-
    This is both the wrong direction and the wrong power. More mass adds inertia, and the inverse-square-root dependence gives $f_{\mathrm{new}}=f_{\mathrm{old}}/\sqrt2$.
- id: mass-unchanged
  content: |-
    The frequency remains unchanged.
  feedback: |-
    Mass appears explicitly in the frequency denominator. It would remain unchanged only if the mass were unchanged or another parameter were adjusted to keep $k/m$ fixed.
```

---

<a id="increase-the-spring-stiffness"></a>
## Increase the Spring Stiffness

**Example:** Determine how frequency changes if the spring constant is multiplied by a factor $b>1$ while $m$ remains fixed.

**Explanation**

Substitute $k_{\mathrm{new}}=bk$:

$$
\begin{aligned}
f_{\mathrm{new}}
&=\frac{1}{2\pi}\sqrt{\frac{bk}{m}}\\
&=\sqrt b\,f_{\mathrm{old}}.
\end{aligned}
$$

For $b>1$, the factor $\sqrt b$ is greater than one, so increasing stiffness increases frequency. A stiffer spring supplies a larger restoring force for the same displacement.

```quiz
type: radio
id: shm-quadruple-stiffness-frequency
shuffle: true
content: |-
  The spring constant is multiplied by $4$ while the mass remains fixed. How does the frequency change?
options:
- id: multiply-two-frequency
  content: |-
    $f_{\mathrm{new}}=2f_{\mathrm{old}}$
  correct: true
  feedback: |-
    Stiffness enters as $k^{1/2}$. Multiplying $k$ by $4$ multiplies frequency by $\sqrt4=2$, so the oscillator completes cycles twice as often.
- id: multiply-four-frequency
  content: |-
    $f_{\mathrm{new}}=4f_{\mathrm{old}}$
  feedback: |-
    This treats the stiffness dependence as linear. Since $k$ is under a square root, a factor of $4$ in stiffness produces a factor of $2$ in frequency.
- id: divide-two-frequency
  content: |-
    $f_{\mathrm{new}}=\dfrac12f_{\mathrm{old}}$
  feedback: |-
    This assigns stiffness an inverse dependence. Stiffness is in the numerator, so a larger restoring constant raises frequency rather than lowering it.
- id: divide-four-frequency
  content: |-
    $f_{\mathrm{new}}=\dfrac14f_{\mathrm{old}}$
  feedback: |-
    This reverses the direction and drops the square-root scaling. The correct factor is $\sqrt4=2$, not $1/4$.
- id: stiffness-unchanged
  content: |-
    The frequency remains unchanged.
  feedback: |-
    Stiffness appears explicitly in the numerator of $k/m$. Frequency would remain unchanged only if $k$ were unchanged or if mass changed by the same factor so the ratio stayed fixed.
```

---

<a id="recognize-an-absent-parameter"></a>
## Recognize an Absent Parameter

**Example:** Determine how increasing gravitational acceleration affects the frequency of the same ideal horizontal oscillator.

**Explanation**

The horizontal restoring force is $F_x=-kx$, so the horizontal equation of motion is

$$
ma_x=-kx.
$$

Gravity acts vertically and is balanced by the support force. It does not appear in the horizontal equation or in

$$
f=\frac{1}{2\pi}\sqrt{\frac{k}{m}}.
$$

Therefore, increasing $g$ leaves the frequency unchanged as long as the oscillator remains the same ideal horizontal mass–spring system.

```quiz
type: radio
id: shm-gravity-frequency-effect
shuffle: true
content: |-
  Gravitational acceleration increases while the same ideal horizontal mass–spring oscillator keeps the same $m$ and $k$. What happens to its frequency?
options:
- id: gravity-unchanged
  content: |-
    The frequency remains unchanged.
  correct: true
  feedback: |-
    Gravity is perpendicular to the horizontal oscillation and is balanced by the support force. Since $g$ is absent from $f=(1/2\pi)\sqrt{k/m}$, changing it does not change this frequency.
- id: gravity-increases-frequency
  content: |-
    The frequency increases.
  feedback: |-
    Greater weight changes the vertical normal force, not the horizontal spring restoring law. The frequency increases only through a larger $k/m$ ratio, which changing $g$ does not produce here.
- id: gravity-decreases-frequency
  content: |-
    The frequency decreases.
  feedback: |-
    Gravity does not add horizontal inertia or weaken the spring. With $m$ and $k$ fixed, the horizontal equation remains $ma_x=-kx$ and the frequency is unchanged.
- id: gravity-needs-amplitude
  content: |-
    The effect cannot be determined without the amplitude.
  feedback: |-
    Amplitude is not needed for the ideal mass–spring frequency, and neither is $g$. The parameter dependence is already fixed by $f=(1/2\pi)\sqrt{k/m}$.
- id: gravity-changes-mass
  content: |-
    The frequency decreases because larger $g$ increases the mass.
  feedback: |-
    Gravitational acceleration changes weight $mg$, not the object's inertial mass $m$. The mass in the frequency formula is unchanged, so the frequency remains unchanged.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Classify all three original changes before checking the ordered triple.

**Explanation**

> For an ideal horizontal mass–spring oscillator, determine how each change affects the frequency.
>
> 1. Increase the mass while holding the spring constant fixed.
> 2. Increase the spring stiffness while holding the mass fixed.
> 3. Increase gravitational acceleration for the same horizontal oscillator.

Give the classifications in that order using **increases**, **decreases**, or **remains unchanged**.

```quiz
type: radio
id: khadley-oscillations-q3
shuffle: true
content: |-
  Which ordered triple correctly classifies (increased mass, increased stiffness, increased gravitational acceleration)?
options:
- id: decreases-increases-unchanged
  content: |-
    (Decreases, Increases, Remains unchanged)
  correct: true
  feedback: |-
    Frequency varies as $k^{1/2}m^{-1/2}$. More mass lowers it, more stiffness raises it, and $g$ is absent from the ideal horizontal formula, so the ordered triple is as stated.
- id: increases-increases-unchanged
  content: |-
    (Increases, Increases, Remains unchanged)
  feedback: |-
    The stiffness and gravity classifications are correct, but mass has an inverse-square-root role. Increasing mass adds inertia and therefore decreases the frequency.
- id: decreases-decreases-unchanged
  content: |-
    (Decreases, Decreases, Remains unchanged)
  feedback: |-
    The mass and gravity classifications are correct, but stiffness is a direct-square-root factor. Increasing $k$ strengthens the restoring response and raises frequency.
- id: decreases-increases-increases
  content: |-
    (Decreases, Increases, Increases)
  feedback: |-
    The first two classifications follow the formula, but $g$ does not. For the same ideal horizontal oscillator, greater gravity changes the support force while leaving frequency unchanged.
- id: unchanged-increases-decreases
  content: |-
    (Remains unchanged, Increases, Decreases)
  feedback: |-
    Stiffness is classified correctly, but mass is present with exponent $-1/2$ and gravity is absent. Thus mass lowers frequency and gravity leaves it unchanged.
```

---

<a id="summary"></a>
## Summary

For an ideal horizontal mass–spring oscillator,

$$
f=\frac{1}{2\pi}\sqrt{\frac{k}{m}}
\propto k^{1/2}m^{-1/2}.
$$

The dimensions also verify that this is a frequency. Since $[k]=\mathrm{N/m}=\mathrm{kg/s^2}$,

$$
\left[\frac{k}{m}\right]=\mathrm{s}^{-2},
\qquad
[f]=\mathrm{s}^{-1}=\mathrm{Hz}.
$$

Use the exponent or absence test:

- Increase $m$ with $k$ fixed: $f$ decreases by the inverse square root of the mass factor.
- Increase $k$ with $m$ fixed: $f$ increases by the square root of the stiffness factor.
- Increase $g$ for the same horizontal oscillator: $f$ remains unchanged because $g$ is absent from the horizontal equation.

The main traps are reversing numerator and denominator, treating the dependence as linear instead of square-root, confusing weight with inertial mass, or assuming every changed physical quantity must appear in the frequency.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
