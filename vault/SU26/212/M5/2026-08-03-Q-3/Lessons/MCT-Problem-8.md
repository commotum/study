# Turn a String Description into Wave Speed

<!--
lesson-id: 212-M5-066
topic-code: MTH212.M5.66
-->

## Table of Contents

- [Introduction](#introduction)
- [Source-Video Problem 1: From String Mass to Frequency](#source-mass-to-frequency)
- [Source-Video Problem 2: Chain Wave Speed into Wavelength or Frequency](#source-speed-chain)
- [Source-Video Problem 3: Work Backward to Tension](#source-tension)
- [Source-Video Problem 4: Find End-to-End Travel Time](#source-travel-time)
- [Lecture Transfer: A Hanging Mass Supplies the Tension](#lecture-hanging-mass)
- [Lecture Transfer: Separate Wave Speed from Particle Speed](#lecture-particle-speed)
- [Summary](#summary)

## Prerequisites

- Compute a unit rate such as mass per length.
- Convert centimeters to meters.
- Rearrange a formula for one requested variable.
- Evaluate a square root with the full quotient inside the radical.
- Use $v=f\lambda$ and constant-speed travel, $d=vt$.

---

<a id="introduction"></a>
## Introduction

A string or wire description supplies two inputs for the propagation-speed calculation:

$$
\boxed{\mu=\frac{m_s}{L_s}}
\qquad\text{and}\qquad
\boxed{F_T=\text{actual tension in the string}}.
$$

Here $m_s$ and $L_s$ are the **string's** mass and length. Once those inputs are identified, the disturbance's propagation speed is

$$
\boxed{v=\sqrt{\frac{F_T}{\mu}}}.
$$

Assign each description to its role before entering numbers:

| Description | Quantity | Where it goes |
|---|---:|---|
| mass and length of the vibrating string | $\mu=m_s/L_s$ | denominator of the speed formula |
| stated applied tension | $F_T$ | numerator of the speed formula |
| separate stationary hanging mass $M$ | $F_T\approx Mg$ | numerator after converting mass to force |
| frequency or wavelength | $f$ or $\lambda$ | follow-up relation $v=f\lambda$ |

Then take only the step the question requests:

$$
f=\frac{v}{\lambda},
\qquad
\lambda=\frac{v}{f},
\qquad
t=\frac{d}{v},
\qquad
F_T=\mu v^2.
$$

Keep the roles separate. The medium properties $F_T$ and $\mu$ set the wave speed. A source frequency does not independently set the speed in the same ideal, nondispersive string; the wavelength adjusts through $v=f\lambda$.

The units provide a quick check:

$$
\left[\frac{F_T}{\mu}\right]
=\frac{\mathrm{kg\,m/s^2}}{\mathrm{kg/m}}
=\mathrm{m^2/s^2},
$$

so its square root has units of $\mathrm{m/s}$. Standing-wave boundary conditions are not needed for any problem in this lesson.

On a calculator, keep the complete quotient grouped: enter $\sqrt{(F_T)/(\mu)}$. The expression $\sqrt{F_T}/\mu$ is a different calculation.

---

<a id="source-mass-to-frequency"></a>
## Source-Video Problem 1: From String Mass to Frequency

The first source problem (`qm1hDJrIYwE`, 00:05:23–00:07:32) gives

$$
L_s=2.0\ \mathrm m,
\qquad
m_s=0.10\ \mathrm{kg},
\qquad
F_T=500\ \mathrm N.
$$

Find the string's mass per unit length first:

$$
\mu=\frac{m_s}{L_s}
=\frac{0.10\ \mathrm{kg}}{2.0\ \mathrm m}
=\boxed{0.050\ \mathrm{kg/m}}.
$$

Now use the tension and linear density:

$$
v=\sqrt{\frac{500\ \mathrm N}{0.050\ \mathrm{kg/m}}}
=\sqrt{10\,000\ \mathrm{m^2/s^2}}
=\boxed{100\ \mathrm{m/s}}.
$$

For the source wavelength $\lambda=0.25\ \mathrm m$,

$$
f=\frac{v}{\lambda}
=\frac{100\ \mathrm{m/s}}{0.25\ \mathrm m}
=\boxed{400\ \mathrm{Hz}}.
$$

The $0.10\ \mathrm{kg}$ belongs in $\mu$ because it is the string's mass. It is not a hanging mass and does not determine the tension in this problem.

```quiz
type: radio
id: mct-p8-string-mass-frequency
shuffle: true
content: |-
  A $3.0\ \mathrm m$ string has mass $0.24\ \mathrm{kg}$ and tension $320\ \mathrm N$. A wave on it has wavelength $0.20\ \mathrm m$. What is the wave frequency?
options:
- id: mct-p8-string-mass-frequency-a
  content: |-
    $316\ \mathrm{Hz}$
  correct: true
  feedback: |-
    The string supplies $\mu=m_s/L_s=0.24/3.0=0.080\ \mathrm{kg/m}$. Thus $v=\sqrt{320/0.080}=63.25\ \mathrm{m/s}$ and $f=v/\lambda=63.25/0.20=316\ \mathrm{Hz}$.
- id: mct-p8-string-mass-frequency-b
  content: |-
    $20\,000\ \mathrm{Hz}$
  feedback: |-
    This uses $F_T/\mu$ as the speed without taking its square root. The quotient has units of $\mathrm{m^2/s^2}$; its square root is $63.25\ \mathrm{m/s}$, which gives $316\ \mathrm{Hz}$.
- id: mct-p8-string-mass-frequency-c
  content: |-
    $12.6\ \mathrm{Hz}$
  feedback: |-
    This multiplies $v$ by $\lambda$. Since $v=f\lambda$, isolate frequency by dividing: $f=v/\lambda$, not $v\lambda$.
- id: mct-p8-string-mass-frequency-d
  content: |-
    $105\ \mathrm{Hz}$
  feedback: |-
    This treats $m_sL_s=0.72$ as the linear density. Linear density is a unit rate, mass **per** length: $\mu=m_s/L_s=0.080\ \mathrm{kg/m}$.
- id: mct-p8-string-mass-frequency-e
  content: |-
    $25.3\ \mathrm{Hz}$
  feedback: |-
    This reverses the mass-per-length ratio and uses $L_s/m_s$. The required density is kilograms per meter, so divide $0.24\ \mathrm{kg}$ by $3.0\ \mathrm m$.
```

---

<a id="source-speed-chain"></a>
## Source-Video Problem 2: Chain Wave Speed into Wavelength or Frequency

The second source problem (`vEzftaDL7fM`, 00:10:09–00:12:43) gives

$$
F_T=1500\ \mathrm N,
\qquad
m_s=0.50\ \mathrm{kg},
\qquad
L_s=10\ \mathrm m,
\qquad
\lambda=0.15\ \mathrm m.
$$

The string density is again

$$
\mu=\frac{0.50\ \mathrm{kg}}{10\ \mathrm m}
=\boxed{0.050\ \mathrm{kg/m}}.
$$

Therefore,

$$
v=\sqrt{\frac{1500}{0.050}}
=\sqrt{30\,000}
=\boxed{173.2\ \mathrm{m/s}},
$$

and

$$
f=\frac{v}{\lambda}
=\frac{173.2}{0.15}
=\boxed{1154.7\ \mathrm{Hz}}.
$$

Meters cancel in the final division, leaving $\mathrm{s^{-1}}=\mathrm{Hz}$. If a nearby problem instead supplies $f$ and asks for $\lambda$, keep the same first two steps and use $\lambda=v/f$.

```quiz
type: radio
id: mct-p8-find-wavelength
shuffle: true
content: |-
  A $4.5\ \mathrm m$ wire has mass $0.36\ \mathrm{kg}$ and tension $500\ \mathrm N$. A source drives it at $250\ \mathrm{Hz}$. What wavelength travels along the wire?
options:
- id: mct-p8-find-wavelength-a
  content: |-
    $0.316\ \mathrm m$
  correct: true
  feedback: |-
    $\mu=0.36/4.5=0.080\ \mathrm{kg/m}$ and $v=\sqrt{500/0.080}=79.06\ \mathrm{m/s}$. Since $v=f\lambda$, $\lambda=v/f=79.06/250=0.316\ \mathrm m$.
- id: mct-p8-find-wavelength-b
  content: |-
    $3.16\ \mathrm m$
  feedback: |-
    This reverses the last division and uses $f/v$. Wavelength is speed divided by frequency: $\lambda=v/f=79.06/250=0.316\ \mathrm m$.
- id: mct-p8-find-wavelength-c
  content: |-
    $25.0\ \mathrm m$
  feedback: |-
    This omits the square root and treats $F_T/\mu=6250\ \mathrm{m^2/s^2}$ as a speed. Use $v=\sqrt{6250}=79.06\ \mathrm{m/s}$ before dividing by frequency.
- id: mct-p8-find-wavelength-d
  content: |-
    $0.0703\ \mathrm m$
  feedback: |-
    This multiplies the string mass and length to form $\mu$. Linear density is $m_s/L_s=0.080\ \mathrm{kg/m}$, not $m_sL_s$.
- id: mct-p8-find-wavelength-e
  content: |-
    $0.0253\ \mathrm m$
  feedback: |-
    This uses the inverse quantity $L_s/m_s$ in the speed formula. The denominator must be the string's mass per length, $\mu=m_s/L_s$.
```

---

<a id="source-tension"></a>
## Source-Video Problem 3: Work Backward to Tension

The prompt frame in the third source segment (`vEzftaDL7fM`, 00:14:55–00:17:15) shows

$$
\lambda=15\ \mathrm{cm}=0.15\ \mathrm m,
\qquad
f=13\ \mathrm{Hz},
\qquad
\mu=0.75\ \mathrm{kg/m}.
$$

First recover the propagation speed:

$$
v=f\lambda
=(13\ \mathrm{s^{-1}})(0.15\ \mathrm m)
=\boxed{1.95\ \mathrm{m/s}}.
$$

Then square the string-speed formula and isolate tension:

$$
\begin{aligned}
v&=\sqrt{\frac{F_T}{\mu}},\\
v^2&=\frac{F_T}{\mu},\\
\boxed{F_T=\mu v^2}.
\end{aligned}
$$

Thus

$$
F_T=(0.75\ \mathrm{kg/m})(1.95\ \mathrm{m/s})^2
=2.851875\ \mathrm N
\approx\boxed{2.85\ \mathrm N}.
$$

The displayed prompt resolves a caption error: the auto-captions drop the decimal and say $75\ \mathrm{kg/m}$, but the frame reads $0.75\ \mathrm{kg/m}$. Only $0.75\ \mathrm{kg/m}$ gives the displayed $2.85\ \mathrm N$ result. The narration first calls $2.85$ “hertz” and then immediately corrects the unit to newtons. The unit calculation confirms that correction:

$$
[\mu v^2]
=\frac{\mathrm{kg}}{\mathrm m}\frac{\mathrm{m^2}}{\mathrm{s^2}}
=\mathrm N.
$$

```quiz
type: radio
id: mct-p8-find-tension
shuffle: true
content: |-
  A wave on a string has wavelength $0.20\ \mathrm m$, frequency $30\ \mathrm{Hz}$, and linear density $0.50\ \mathrm{kg/m}$. What tension is required?
options:
- id: mct-p8-find-tension-a
  content: |-
    $18\ \mathrm N$
  correct: true
  feedback: |-
    The wave speed is $v=f\lambda=(30)(0.20)=6.0\ \mathrm{m/s}$. Squaring $v=\sqrt{F_T/\mu}$ gives $F_T=\mu v^2=(0.50)(6.0)^2=18\ \mathrm N$.
- id: mct-p8-find-tension-b
  content: |-
    $3.0\ \mathrm N$
  feedback: |-
    This uses $\mu v$ and leaves the speed unsquared. Tension follows $F_T=\mu v^2$, so the full $6.0\ \mathrm{m/s}$ speed must be squared.
- id: mct-p8-find-tension-c
  content: |-
    $72\ \mathrm N$
  feedback: |-
    This divides $v^2$ by $\mu$. After squaring $v=\sqrt{F_T/\mu}$, multiply by $\mu$: $F_T=\mu v^2$, not $v^2/\mu$.
- id: mct-p8-find-tension-d
  content: |-
    $11\,250\ \mathrm N$
  feedback: |-
    This first uses $v=f/\lambda=150\ \mathrm{m/s}$. The wave relation is $v=f\lambda$, so the correct speed is $6.0\ \mathrm{m/s}$ before tension is calculated.
- id: mct-p8-find-tension-e
  content: |-
    $6.0\ \mathrm N$
  feedback: |-
    The value $6.0$ is the propagation speed in meters per second, not the tension. Convert that speed with $F_T=\mu v^2$ to obtain newtons.
```

---

<a id="source-travel-time"></a>
## Source-Video Problem 4: Find End-to-End Travel Time

The fourth source problem (`vEzftaDL7fM`, 00:17:24–00:20:06) describes an $85\ \mathrm m$ wire with mass $5.0\ \mathrm{kg}$ under $300\ \mathrm N$ of tension. Its density is

$$
\mu=\frac{5.0\ \mathrm{kg}}{85\ \mathrm m}
=0.0588235\ldots\ \mathrm{kg/m}
\approx\boxed{0.05882\ \mathrm{kg/m}}.
$$

The propagation speed is

$$
v=\sqrt{\frac{300}{0.0588235\ldots}}
=\sqrt{5100}
=71.414\ldots\ \mathrm{m/s}
\approx\boxed{71.4\ \mathrm{m/s}}.
$$

For one end-to-end trip, the distance is the wire length, $d=85\ \mathrm m$:

$$
t=\frac{d}{v}
=\frac{85\ \mathrm m}{71.4\ \mathrm{m/s}}
=1.190\ldots\ \mathrm s
\approx\boxed{1.19\ \mathrm s}.
$$

No frequency or wavelength is needed because the requested follow-up is travel time.

```quiz
type: radio
id: mct-p8-travel-time
shuffle: true
content: |-
  A $60\ \mathrm m$ cable has mass $1.5\ \mathrm{kg}$ and tension $240\ \mathrm N$. How long does a pulse take to travel once from one end to the other?
options:
- id: mct-p8-travel-time-a
  content: |-
    $0.612\ \mathrm s$
  correct: true
  feedback: |-
    $\mu=1.5/60=0.025\ \mathrm{kg/m}$, so $v=\sqrt{240/0.025}=97.98\ \mathrm{m/s}$. One end-to-end trip covers $60\ \mathrm m$, giving $t=d/v=60/97.98=0.612\ \mathrm s$.
- id: mct-p8-travel-time-b
  content: |-
    $0.025\ \mathrm s$
  feedback: |-
    The value $0.025$ is the linear density in kilograms per meter, not a time. Use it inside $v=\sqrt{F_T/\mu}$, then divide distance by speed.
- id: mct-p8-travel-time-c
  content: |-
    $98.0\ \mathrm s$
  feedback: |-
    The value $98.0$ is the wave speed in meters per second, not the travel time. The requested time is $d/v$.
- id: mct-p8-travel-time-d
  content: |-
    $4.74\ \mathrm s$
  feedback: |-
    This uses the cable's total $1.5\ \mathrm{kg}$ as though it were $\mu$. The speed formula needs mass per length: $\mu=1.5/60=0.025\ \mathrm{kg/m}$.
- id: mct-p8-travel-time-e
  content: |-
    $1.63\ \mathrm s$
  feedback: |-
    This reverses the final rate and computes $v/d$. Time is distance divided by speed, $t=d/v$, which also leaves seconds after the units cancel.
```

---

<a id="lecture-hanging-mass"></a>
## Lecture Transfer: A Hanging Mass Supplies the Tension

If a separate block of mass $M$ hangs from an ideal string over a frictionless pulley and remains stationary, the block sets the tension:

$$
F_T=Mg.
$$

If the wire segment has mass $m_w$ and length $L$, then

$$
\mu=\frac{m_w}{L}.
$$

The hanging mass and wire mass enter different equations. Substituting both into the wave-speed formula gives the M5-2 lecture chain

$$
\boxed{
v=\sqrt{\frac{Mg}{m_w/L}}
=\sqrt{\frac{MgL}{m_w}}
}.
$$

The lecture example uses

$$
M=0.82\ \mathrm{kg},
\quad
m_w=0.018\ \mathrm{kg},
\quad
L=1.4\ \mathrm m,
\quad
g=9.8\ \mathrm{m/s^2},
$$

so

$$
v=\sqrt{\frac{(0.82)(9.8)(1.4)}{0.018}}
=24.999\ldots\ \mathrm{m/s}
\approx\boxed{25\ \mathrm{m/s}}.
$$

The hanging block does not belong in $\mu$, and the wire's mass does not replace $M$ in $Mg$.

```quiz
type: radio
id: mct-p8-hanging-mass
shuffle: true
content: |-
  A stationary $0.60\ \mathrm{kg}$ block hangs over an ideal pulley and tensions a wire segment of length $0.80\ \mathrm m$ and mass $0.012\ \mathrm{kg}$. Using $g=9.8\ \mathrm{m/s^2}$, what is the wave speed in the wire?
options:
- id: mct-p8-hanging-mass-a
  content: |-
    $19.8\ \mathrm{m/s}$
  correct: true
  feedback: |-
    The block sets $F_T=Mg=(0.60)(9.8)=5.88\ \mathrm N$, while the wire sets $\mu=m_w/L=0.012/0.80=0.015\ \mathrm{kg/m}$. Thus $v=\sqrt{5.88/0.015}=19.8\ \mathrm{m/s}$.
- id: mct-p8-hanging-mass-b
  content: |-
    $392\ \mathrm{m/s}$
  feedback: |-
    This reports $F_T/\mu=392\ \mathrm{m^2/s^2}$ without taking the square root. Wave speed is $\sqrt{F_T/\mu}=19.8\ \mathrm{m/s}$.
- id: mct-p8-hanging-mass-c
  content: |-
    $6.32\ \mathrm{m/s}$
  feedback: |-
    This treats the numerical mass $0.60$ as a tension in newtons. A stationary hanging block supplies $F_T=Mg=5.88\ \mathrm N$, not $0.60\ \mathrm N$.
- id: mct-p8-hanging-mass-d
  content: |-
    $2.80\ \mathrm{m/s}$
  feedback: |-
    This puts the hanging-block mass into the linear density. The wire's $0.012\ \mathrm{kg}$ determines $\mu$; the separate $0.60\ \mathrm{kg}$ block determines the tension.
- id: mct-p8-hanging-mass-e
  content: |-
    $0.297\ \mathrm{m/s}$
  feedback: |-
    This multiplies tension by linear density under the radical. The string-speed model uses their quotient, $v=\sqrt{F_T/\mu}$.
```

---

<a id="lecture-particle-speed"></a>
## Lecture Transfer: Separate Wave Speed from Particle Speed

The symbol $v$ above is the speed at which the **disturbance propagates along the string**. A point on the string moves transversely around equilibrium instead of traveling with the disturbance. For a sinusoidal wave, its maximum transverse particle speed is

$$
\boxed{u_{\max}=\omega A=2\pi fA}.
$$

Using $f=v/\lambda$ gives

$$
\boxed{u_{\max}=\frac{2\pi A}{\lambda}v}.
$$

The M5-2 lecture example has propagation speed

$$
v=24.261\ldots\ \mathrm{m/s},
$$

amplitude $A=0.85\ \mathrm{cm}=0.0085\ \mathrm m$, and wavelength $\lambda=0.65\ \mathrm{cm}=0.0065\ \mathrm m$. Therefore,

$$
u_{\max}
=\frac{2\pi(0.0085)}{0.0065}(24.261\ldots)
=199.3\ldots\ \mathrm{m/s}
\approx\boxed{200\ \mathrm{m/s}}.
$$

The particle speed can exceed the propagation speed; they describe different motions. Do not substitute $u_{\max}$ for $v$ in $v=\sqrt{F_T/\mu}$ or $v=f\lambda$.

```quiz
type: radio
id: mct-p8-particle-speed
shuffle: true
content: |-
  A sinusoidal wave propagates along a string at $80\ \mathrm{m/s}$ with wavelength $0.40\ \mathrm m$ and amplitude $4.0\ \mathrm{mm}$. What is the maximum transverse speed of a string particle?
options:
- id: mct-p8-particle-speed-a
  content: |-
    $5.03\ \mathrm{m/s}$
  correct: true
  feedback: |-
    Convert $A=0.0040\ \mathrm m$. Then $u_{\max}=(2\pi A/\lambda)v=[2\pi(0.0040)/0.40](80)=5.03\ \mathrm{m/s}$.
- id: mct-p8-particle-speed-b
  content: |-
    $80\ \mathrm{m/s}$
  feedback: |-
    This is the disturbance's propagation speed along the string. The particle moves transversely, with maximum speed $u_{\max}=2\pi fA$.
- id: mct-p8-particle-speed-c
  content: |-
    $0.800\ \mathrm{m/s}$
  feedback: |-
    This calculates $fA$ but omits $2\pi$. For sinusoidal motion, angular frequency is $\omega=2\pi f$, so $u_{\max}=2\pi fA$.
- id: mct-p8-particle-speed-d
  content: |-
    $50.3\ \mathrm{m/s}$
  feedback: |-
    This converts $4.0\ \mathrm{mm}$ as $0.040\ \mathrm m$. Since $1000\ \mathrm{mm}=1\ \mathrm m$, the amplitude is $0.0040\ \mathrm m$.
- id: mct-p8-particle-speed-e
  content: |-
    $0.503\ \mathrm{m/s}$
  feedback: |-
    This converts $4.0\ \mathrm{mm}$ as $0.00040\ \mathrm m$, one power of ten too small. The correct amplitude is $0.0040\ \mathrm m$.
```

---

<a id="summary"></a>
## Summary

Read a string description in this order:

1. Put the string's own mass into
   $$
   \mu=\frac{m_s}{L_s}.
   $$
2. Identify the actual tension. If a separate stationary hanging mass $M$ supplies it, use $F_T=Mg$.
3. Compute the propagation speed:
   $$
   v=\sqrt{\frac{F_T}{\mu}}.
   $$
4. Isolate the requested follow-up symbol before substituting:
   $$
   f=\frac{v}{\lambda},
   \qquad
   \lambda=\frac{v}{f},
   \qquad
   t=\frac{d}{v},
   \qquad
   F_T=\mu v^2.
   $$

Check that $F_T/\mu$ has units $\mathrm{m^2/s^2}$ before taking its square root. In a fixed ideal string, tension and linear density set $v$; changing the source frequency changes wavelength instead of setting a new propagation speed. Finally, keep propagation speed $v$ distinct from a string particle's transverse speed $u$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
