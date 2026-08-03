# Maximum Transverse Particle Speed on a Tensioned Wire

<!--
lesson-id: 212-M5-010
topic-code: MTH212.M5.10
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Wave Propagation Speed](#find-the-wave-propagation-speed)
- [Convert Wave Speed to Maximum Particle Speed](#convert-wave-speed-to-maximum-particle-speed)
- [Handle Amplitude and Wavelength Units](#handle-amplitude-and-wavelength-units)
- [Solve the Given Wire-and-Pulley Problem](#solve-the-given-wire-and-pulley-problem)
- [Summary](#summary)

## Prerequisites

- Compute tension from a stationary hanging mass with $T=Mg$.
- Compute linear mass density with $\mu=m_w/L$.
- Use $v_{\mathrm{wave}}=\sqrt{T/\mu}$ for a transverse wave on a wire.
- Relate frequency and wavelength with $f=v_{\mathrm{wave}}/\lambda$.

---

<a id="introduction"></a>
## Introduction

A sinusoidal wave has two different speeds in this problem:

- $v_{\mathrm{wave}}$ is the speed at which the wave pattern travels along the wire.
- $v_{\mathrm{particle,max}}$ is the maximum transverse speed of one particle of the wire as it oscillates.

**Recognition cue:** The problem gives both a tensioned-wire setup and sinusoidal-wave data $(A,\lambda)$, then asks for a particle's transverse speed rather than the propagation speed. That means the wire-speed calculation is an intermediate step, not the final answer.

For a wave written as $y=A\sin(kx-\omega t)$, the quantities play different roles:

| Quantity | Meaning | Useful relation |
|---|---|---|
| $A$ | maximum transverse displacement | supplied by the wave description |
| $v_{\mathrm{wave}}$ | propagation speed along the wire | $\sqrt{T/\mu}$ |
| $\omega$ | angular rate of particle oscillation | $2\pi v_{\mathrm{wave}}/\lambda$ |
| $v_{\mathrm{particle,max}}$ | maximum transverse particle speed | $A\omega$ |

For a sinusoidal displacement, the maximum particle speed is $A\omega$. Since

$$
\omega=2\pi f=\frac{2\pi v_{\mathrm{wave}}}{\lambda},
$$

the needed relation is

$$
v_{\mathrm{particle,max}}
=\frac{2\pi A}{\lambda}v_{\mathrm{wave}}.
$$

The reusable procedure is to calculate the wire's propagation speed from its tension and linear density, then multiply it by the dimensionless factor $2\pi A/\lambda$.

---

<a id="find-the-wave-propagation-speed"></a>
## Find the Wave Propagation Speed

**Example:** A stationary $0.50\ \mathrm{kg}$ block tensions a $2.0\ \mathrm{m}$ wire segment of mass $0.020\ \mathrm{kg}$. Use $g=9.8\ \mathrm{m/s^2}$. Find $v_{\mathrm{wave}}$.

**Explanation**

The block supplies tension $T=Mg$, and the wire segment has linear density $\mu=m_w/L$. Therefore,

$$
\begin{aligned}
v_{\mathrm{wave}}
&=\sqrt{\frac{T}{\mu}} \\
&=\sqrt{\frac{Mg}{m_w/L}} \\
&=\sqrt{\frac{MgL}{m_w}} \\
&=\sqrt{\frac{(0.50)(9.8)(2.0)}{0.020}} \\
&=22.1\ldots\ \mathrm{m/s}.
\end{aligned}
$$

```quiz
type: radio
id: p3-wave-speed
content: |-
  A stationary $0.50\ \mathrm{kg}$ block tensions a $2.0\ \mathrm{m}$ wire segment of mass $0.010\ \mathrm{kg}$. Use $g=9.8\ \mathrm{m/s^2}$. What is the wave propagation speed?
options:
- id: a
  content: |-
    $9.8\ \mathrm{m/s}$
  feedback: |-
    This copies the numerical value of $g$ instead of evaluating $\sqrt{MgL/m_w}$.
- id: b
  content: |-
    $22.1\ \mathrm{m/s}$
  feedback: |-
    This is the result for a wire mass of $0.020\ \mathrm{kg}$, not the given $0.010\ \mathrm{kg}$.
- id: c
  content: |-
    $31.3\ \mathrm{m/s}$
  correct: true
  feedback: |-
    Correct. $\sqrt{(0.50)(9.8)(2.0)/0.010}=31.3\ldots\ \mathrm{m/s}$.
- id: d
  content: |-
    $49.0\ \mathrm{m/s}$
  feedback: |-
    Here $T=4.9\ \mathrm N$ and $\mu=0.0050\ \mathrm{kg/m}$, so $T/\mu=980\ \mathrm{m^2/s^2}$; $49.0$ does not result from the required quotient and square root.
- id: e
  content: |-
    $98.0\ \mathrm{m/s}$
  feedback: |-
    The correct radicand is $980$, not $98$; after dividing by $m_w=0.010\ \mathrm{kg}$, take $\sqrt{980}=31.3\ \mathrm{m/s}$.
```

---

<a id="convert-wave-speed-to-maximum-particle-speed"></a>
## Convert Wave Speed to Maximum Particle Speed

**Example:** A sinusoidal wave travels at $12\ \mathrm{m/s}$ with amplitude $A=0.010\ \mathrm{m}$ and wavelength $\lambda=0.060\ \mathrm{m}$. Find the maximum transverse particle speed.

**Explanation**

First compute the angular frequency from the wave speed and wavelength:

$$
\omega=\frac{2\pi v_{\mathrm{wave}}}{\lambda}.
$$

Then multiply by the amplitude:

$$
\begin{aligned}
v_{\mathrm{particle,max}}
&=A\omega \\
&=\frac{2\pi A}{\lambda}v_{\mathrm{wave}} \\
&=\frac{2\pi(0.010\ \mathrm{m})}{0.060\ \mathrm{m}}(12\ \mathrm{m/s}) \\
&=12.57\ldots\ \mathrm{m/s}.
\end{aligned}
$$

```quiz
type: radio
id: p3-particle-speed
content: |-
  A sinusoidal wave travels at $18\ \mathrm{m/s}$ with amplitude $A=0.0050\ \mathrm{m}$ and wavelength $\lambda=0.030\ \mathrm{m}$. What is the maximum transverse particle speed?
options:
- id: a
  content: |-
    $3.0\ \mathrm{m/s}$
  feedback: |-
    This uses $(A/\lambda)v_{\mathrm{wave}}$ but omits the factor $2\pi$.
- id: b
  content: |-
    $6.0\ \mathrm{m/s}$
  feedback: |-
    This replaces the angular factor $2\pi$ with $2$.
- id: c
  content: |-
    $18\ \mathrm{m/s}$
  feedback: |-
    This reports the propagation speed rather than the maximum transverse particle speed.
- id: d
  content: |-
    $18.85\ \mathrm{m/s}$
  correct: true
  feedback: |-
    Correct. $(2\pi A/\lambda)v_{\mathrm{wave}}=2\pi(0.0050/0.030)(18)$.
- id: e
  content: |-
    $113.1\ \mathrm{m/s}$
  feedback: |-
    This multiplies $v_{\mathrm{wave}}$ by $2\pi$ but omits the ratio $A/\lambda$.
```

---

<a id="handle-amplitude-and-wavelength-units"></a>
## Handle Amplitude and Wavelength Units

**Example:** A wave has $A=0.40\ \mathrm{cm}$, $\lambda=2.0\ \mathrm{cm}$, and $v_{\mathrm{wave}}=30\ \mathrm{m/s}$. Find $v_{\mathrm{particle,max}}$.

**Explanation**

Amplitude and wavelength may remain in centimeters because only their ratio appears:

$$
\frac{A}{\lambda}
=\frac{0.40\ \mathrm{cm}}{2.0\ \mathrm{cm}}
=0.20.
$$

Therefore,

$$
v_{\mathrm{particle,max}}
=2\pi(0.20)(30\ \mathrm{m/s})
=37.7\ldots\ \mathrm{m/s}.
$$

The units must match within $A/\lambda$. Converting only one of them would create a factor-of-$100$ error.

Because $2\pi A/\lambda$ is unitless, $v_{\mathrm{particle,max}}$ inherits the $\mathrm{m/s}$ unit of $v_{\mathrm{wave}}$. The multiplier can be greater than $1$, so the numerical particle speed can exceed the propagation speed in this sinusoidal model.

```quiz
type: radio
id: p3-length-ratio
content: |-
  A wave has $A=0.30\ \mathrm{cm}$, $\lambda=1.5\ \mathrm{cm}$, and $v_{\mathrm{wave}}=25\ \mathrm{m/s}$. What is the maximum transverse particle speed?
options:
- id: a
  content: |-
    $5.0\ \mathrm{m/s}$
  feedback: |-
    This uses $(A/\lambda)v_{\mathrm{wave}}$ without the factor $2\pi$.
- id: b
  content: |-
    $15.7\ \mathrm{m/s}$
  feedback: |-
    This uses $\pi$ instead of $2\pi$.
- id: c
  content: |-
    $25\ \mathrm{m/s}$
  feedback: |-
    This is the wave propagation speed, not the transverse particle speed.
- id: d
  content: |-
    $31.4\ \mathrm{m/s}$
  correct: true
  feedback: |-
    Correct. Since $A/\lambda=0.20$, the multiplier is $2\pi(0.20)$.
- id: e
  content: |-
    $157\ \mathrm{m/s}$
  feedback: |-
    This introduces a factor-of-$10$ unit or decimal error in $A/\lambda$.
```

---

<a id="solve-the-given-wire-and-pulley-problem"></a>
## Solve the Given Wire-and-Pulley Problem

**Example:** A block of mass $M$ hangs from a wire over a pulley. The wire segment between the wall and pulley has length $L$ and mass $m_w$. A sinusoidal wave with amplitude $A$ and wavelength $\lambda$ propagates along the wire. Find the maximum transverse speed of a particle in the wire. Disregard reflections.

Use $M=0.75\ \mathrm{kg}$, $m_w=0.015\ \mathrm{kg}$, $A=0.85\ \mathrm{cm}$, $\lambda=0.65\ \mathrm{cm}$, $L=1.2\ \mathrm{m}$, and $g=9.81\ \mathrm{m/s^2}$.

![](<../Source/Images/wire-pulley-hanging-mass.png>)

**Explanation**

Sort the givens by the stage in which they are used:

| Stage | Givens |
|---|---|
| wire propagation | $M=0.75\ \mathrm{kg}$, $m_w=0.015\ \mathrm{kg}$, $L=1.2\ \mathrm{m}$, $g=9.81\ \mathrm{m/s^2}$ |
| particle oscillation | $A=0.85\ \mathrm{cm}$, $\lambda=0.65\ \mathrm{cm}$ |

First find the wave speed:

$$
\begin{aligned}
v_{\mathrm{wave}}
&=\sqrt{\frac{MgL}{m_w}} \\
&=\sqrt{\frac{(0.75)(9.81)(1.2)}{0.015}} \\
&=24.261\ldots\ \mathrm{m/s}.
\end{aligned}
$$

Convert the amplitude and wavelength:

$$
A=0.0085\ \mathrm{m},\qquad \lambda=0.0065\ \mathrm{m}.
$$

Then calculate the maximum particle speed without rounding the wave speed:

$$
\begin{aligned}
\frac{2\pi A}{\lambda}
&=\frac{2\pi(0.0085\ \mathrm{m})}{0.0065\ \mathrm{m}} \\
&=8.216\ldots, \\
v_{\mathrm{particle,max}}
&=\frac{2\pi A}{\lambda}v_{\mathrm{wave}} \\
&=\frac{2\pi(0.0085)}{0.0065}(24.261\ldots) \\
&=199.3\ldots\ \mathrm{m/s}.
\end{aligned}
$$

The dimensionless multiplier is about $8.22$, so a result much larger than $24.261\ldots\ \mathrm{m/s}$ is expected and should not be replaced by the wave speed. The measured givens have two significant figures, so $v_{\mathrm{particle,max}}=2.0\times10^2\ \mathrm{m/s}$. The source answer form is: **Enter the maximum particle speed in meters per second as a number only.** The correct entry is $200$.

```quiz
type: radio
id: p3-source-check
content: |-
  For the wire-and-pulley setup shown, use $M=0.75\ \mathrm{kg}$, $m_w=0.015\ \mathrm{kg}$, $A=0.85\ \mathrm{cm}$, $\lambda=0.65\ \mathrm{cm}$, $L=1.2\ \mathrm{m}$, and $g=9.81\ \mathrm{m/s^2}$. Disregard reflections.

  ![](<../Source/Images/wire-pulley-hanging-mass.png>)

  Which number-only entry gives the maximum transverse particle speed in meters per second?
options:
- id: a
  content: |-
    $2.0$
  feedback: |-
    This does not include the propagation speed and is far below the calculated result.
- id: b
  content: |-
    $24$
  feedback: |-
    This is the wave propagation speed, only the first stage of the calculation.
- id: c
  content: |-
    $32$
  feedback: |-
    This is approximately $(A/\lambda)v_{\mathrm{wave}}$ and omits $2\pi$.
- id: d
  content: |-
    $200$
  correct: true
  feedback: |-
    Correct. The unrounded particle speed is $199.3\ldots\ \mathrm{m/s}$, which rounds to the number-only entry $200$.
- id: e
  content: |-
    $2400$
  feedback: |-
    This results from an inconsistent centimeter-to-meter or decimal conversion.
```

---

<a id="summary"></a>
## Summary

For a sinusoidal wave on a wire tensioned by a stationary hanging mass:

1. Compute $T=Mg$ and $\mu=m_w/L$.
2. Find $v_{\mathrm{wave}}=\sqrt{T/\mu}=\sqrt{MgL/m_w}$.
3. Use $\omega=2\pi v_{\mathrm{wave}}/\lambda$.
4. Find $v_{\mathrm{particle,max}}=A\omega=(2\pi A/\lambda)v_{\mathrm{wave}}$.
5. Keep $A$ and $\lambda$ in matching length units, retain unrounded intermediate values, and round only the final result.

The main trap is reporting $v_{\mathrm{wave}}$ instead of the maximum transverse particle speed.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Deriving Wave Speed on a Load-Bearing Wire](../../2026-08-02-PQ-3/Lessons/Problem-4.md)

Study guide index: 12/28

---
<!-- lesson-nav:end -->
