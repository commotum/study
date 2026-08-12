# Refraction Invariants Across a Boundary

<!--
lesson-id: 212-M7-012
topic-code: MTH212.M7.12
-->

## Table of Contents

- [Introduction](#introduction)
- [Keep Frequency Fixed at the Boundary](#keep-frequency-fixed-at-the-boundary)
- [Change Speed with Refractive Index](#change-speed-with-refractive-index)
- [Change Wavelength to Match the New Speed](#change-wavelength-to-match-the-new-speed)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Use the wave relation $v=f\lambda$.
- Use the refractive-index relation $n=c/v$.
- Distinguish frequency, wavelength, and propagation speed.
- Read angles in a refraction diagram from the normal to the boundary.

---

<a id="introduction"></a>
## Introduction

When light crosses a stationary boundary between two transparent media, several visible features may change: the ray can bend, its speed changes, and its wavelength changes. One wave quantity stays fixed:

$$
\boxed{f_1=f_2}.
$$

The source determines how many oscillations arrive each second. The electromagnetic fields on both sides of a stationary boundary must oscillate together, so the transmitted light keeps the incident frequency.

Use two relationships to track the other quantities:

$$
v=\frac{c}{n}
\qquad\text{and}\qquad
v=f\lambda.
$$

Their variable roles are:

- $f$ is fixed by the source and remains invariant at the stationary boundary,
- $n$ is the dimensionless material property that controls propagation speed,
- $v$ is the medium-dependent speed, and
- $\lambda$ adjusts so that $v=f\lambda$ still holds at the unchanged frequency.

Once $f$ is fixed, the dependencies become especially clear:

$$
v\propto\frac1n,
\qquad
\lambda=\frac{v}{f}\propto v,
\qquad
\lambda=\frac{c}{nf}\propto\frac1n.
$$

For light entering glass from air, the refractive index increases. Therefore the speed decreases; because frequency stays fixed, the wavelength must also decrease.

This reasoning assumes ordinary refraction at a stationary, time-independent boundary. A moving boundary or a time-varying medium can shift frequency, but that is a different situation.

---

<a id="keep-frequency-fixed-at-the-boundary"></a>
## Keep Frequency Fixed at the Boundary

**Example:** Monochromatic light of frequency $5.0\times10^{14}\ \mathrm{Hz}$ travels from air into water. What is its frequency in the water?

**Explanation**

The source fixes the temporal oscillation rate. At a stationary interface, the incident and transmitted fields must match their oscillations at every instant, so

$$
f_{\mathrm{water}}=f_{\mathrm{air}}
=5.0\times10^{14}\ \mathrm{Hz}.
$$

The material changes how fast the phase propagates through space; it does not make this light oscillate more or fewer times per second.

```quiz
type: radio
id: boundary-frequency-invariant
shuffle: true
content: |-
  Light of frequency $6.0\times10^{14}\ \mathrm{Hz}$ passes from air into a stationary acrylic block. What frequency does the transmitted light have inside the acrylic?
options:
- id: same-six-e-fourteen
  content: |-
    $6.0\times10^{14}\ \mathrm{Hz}$
  correct: true
  feedback: |-
    The source fixes the oscillation rate, and fields on both sides of a stationary boundary must remain synchronized. Therefore the transmitted light keeps the incident frequency, $6.0\times10^{14}\ \mathrm{Hz}$.
- id: lower-because-slower
  content: |-
    Less than $6.0\times10^{14}\ \mathrm{Hz}$ because light travels more slowly in acrylic.
  feedback: |-
    Speed describes how quickly a wave pattern moves through space, while frequency counts oscillations per second at a point. Acrylic lowers the speed, but the boundary preserves the source-set frequency.
- id: higher-because-index
  content: |-
    Greater than $6.0\times10^{14}\ \mathrm{Hz}$ because acrylic has a larger refractive index.
  feedback: |-
    A larger index lowers propagation speed through $v=c/n$; it does not raise the temporal frequency. The transmitted field must oscillate at the same $6.0\times10^{14}\ \mathrm{Hz}$ as the incident field.
- id: zero-at-boundary
  content: |-
    $0\ \mathrm{Hz}$ at the boundary, followed by a new frequency in acrylic.
  feedback: |-
    The wave does not stop oscillating and restart at an ordinary interface. Its fields remain continuous in time, so the same frequency extends across the boundary while speed and wavelength adjust.
- id: depends-on-angle
  content: |-
    It cannot be determined without the incidence angle.
  feedback: |-
    Incidence angle helps determine the refracted direction through Snell's law, not the transmitted frequency. At a stationary boundary, frequency is unchanged for every allowed incidence angle.
```

---

<a id="change-speed-with-refractive-index"></a>
## Change Speed with Refractive Index

**Example:** Compare the speed of light in air, $n_1=1.00$, with its speed in glass, $n_2=1.50$.

**Explanation**

Solve the definition of refractive index for speed, treating $c$ as a constant:

$$
\begin{aligned}
n&=\frac{c}{v}\\
nv&=c\\
v&=\frac{c}{n}.
\end{aligned}
$$

Because refractive index is dimensionless, dividing $c$ by $n$ preserves the speed unit $\mathrm{m/s}$.

The speed ratio is

$$
\frac{v_2}{v_1}
=\frac{c/n_2}{c/n_1}
=\frac{n_1}{n_2}
=\frac{1.00}{1.50}
=\frac23.
$$

Light therefore propagates at two-thirds of its air speed in the glass. Its frequency is still unchanged; speed is the quantity controlled by the medium's index.

```quiz
type: radio
id: refractive-index-speed-ratio
shuffle: true
content: |-
  Light crosses from a medium with $n_1=1.20$ into a medium with $n_2=1.60$. What is the transmitted-to-incident speed ratio $v_2/v_1$?
options:
- id: ratio-three-fourths
  content: |-
    $\dfrac34$
  correct: true
  feedback: |-
    Propagation speed varies as $v=c/n$. Thus $v_2/v_1=n_1/n_2=1.20/1.60=3/4$, so light moves more slowly in the higher-index second medium.
- id: ratio-four-thirds
  content: |-
    $\dfrac43$
  feedback: |-
    This places the refractive indices in the speed order instead of the inverse order. Since $v=c/n$, the ratio is $n_1/n_2=1.20/1.60=3/4$, not $4/3$.
- id: ratio-one
  content: |-
    $1$
  feedback: |-
    Frequency remains unchanged, but speed does not. The indices differ, so $v=c/n$ gives different speeds and specifically $v_2/v_1=3/4$.
- id: ratio-two-five
  content: |-
    $\dfrac25$
  feedback: |-
    The speed ratio comes from dividing the two indices, not subtracting or combining them over a new total. Using $v=c/n$ gives $v_2/v_1=1.20/1.60=3/4$.
- id: ratio-index-product
  content: |-
    $1.92$
  feedback: |-
    Multiplying the indices does not compare the speeds. The common factor $c$ cancels in $(c/n_2)/(c/n_1)$, leaving the inverse ratio $n_1/n_2=3/4$.
```

---

<a id="change-wavelength-to-match-the-new-speed"></a>
## Change Wavelength to Match the New Speed

**Example:** Light has wavelength $600\ \mathrm{nm}$ in air and enters glass with $n=1.50$. Treat $n_{\mathrm{air}}=1.00$. Find the wavelength in glass.

**Explanation**

Frequency remains fixed, so wavelength must vary in the same ratio as speed:

$$
\begin{aligned}
v&=f\lambda\\
\frac{v}{f}&=\lambda\\
\lambda&=\frac{v}{f}.
\end{aligned}
$$

Here $f$ is the fixed constant of direct variation between $\lambda$ and $v$: if speed is multiplied by a factor, wavelength is multiplied by the same factor. Therefore,

$$
\frac{\lambda_2}{\lambda_1}
=\frac{v_2/f}{v_1/f}
=\frac{v_2}{v_1}
=\frac{n_1}{n_2}.
$$

Therefore,

$$
\begin{aligned}
\lambda_{\mathrm{glass}}
&=\lambda_{\mathrm{air}}
\frac{n_{\mathrm{air}}}{n_{\mathrm{glass}}}\\
&=(600\ \mathrm{nm})\frac{1.00}{1.50}\\
&=400\ \mathrm{nm}.
\end{aligned}
$$

The wavelength becomes shorter because the same number of wave cycles per second must fit into a smaller distance traveled per second.

The units also confirm the roles in $v=f\lambda$:

$$
\frac{\mathrm m}{\mathrm s}
=\left(\frac{1}{\mathrm s}\right)(\mathrm m).
$$

```quiz
type: radio
id: boundary-wavelength-change
shuffle: true
content: |-
  Light has wavelength $520\ \mathrm{nm}$ in air and enters a medium with $n=1.30$. Treat $n_{\mathrm{air}}=1.00$. What are its wavelength and frequency changes?
options:
- id: wavelength-four-hundred-frequency-same
  content: |-
    The wavelength becomes $400\ \mathrm{nm}$, and the frequency remains unchanged.
  correct: true
  feedback: |-
    The stationary boundary preserves frequency. Since wavelength follows the speed ratio, $\lambda_2=520(1.00/1.30)=400\ \mathrm{nm}$; the shorter wavelength accompanies the lower speed at the same frequency.
- id: wavelength-six-seventy-six-frequency-same
  content: |-
    The wavelength becomes $676\ \mathrm{nm}$, and the frequency remains unchanged.
  feedback: |-
    The frequency statement is correct, but this multiplies wavelength by the higher index. Speed and wavelength both decrease when index increases, so use $520/1.30=400\ \mathrm{nm}$.
- id: wavelength-five-twenty-frequency-lower
  content: |-
    The wavelength remains $520\ \mathrm{nm}$, and the frequency decreases.
  feedback: |-
    This assigns the invariant to wavelength instead of frequency. Frequency is source-set and unchanged; the reduced speed appears as a shorter wavelength of $400\ \mathrm{nm}$.
- id: wavelength-four-hundred-frequency-lower
  content: |-
    The wavelength becomes $400\ \mathrm{nm}$, and the frequency decreases by the same factor.
  feedback: |-
    The wavelength calculation is correct, but frequency does not share the speed change. At a stationary boundary, frequency stays fixed while wavelength shortens to match the lower speed.
- id: wavelength-five-twenty-speed-same
  content: |-
    The wavelength and frequency both remain unchanged because the speed of light is always $c$.
  feedback: |-
    The vacuum speed is $c$, but the propagation speed in a medium is $c/n$. With $n=1.30$, speed decreases; frequency stays fixed and wavelength shortens to $400\ \mathrm{nm}$.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Use the source diagram to identify the invariant at the air--glass boundary.

The ray changes direction at the boundary, but bending does not identify the invariant by itself. Ask which quantity is fixed by the source and must remain continuous in time.

```quiz
type: radio
id: khadley-snells-law-q1
shuffle: true
content: |-
  **Question 1**

  Which quantity remains unchanged when light passes from air into glass?

  ![[../Source/Images/clicker4.jpg]]
options:
- id: wavelength
  content: Wavelength
  feedback: |-
    The wave speed changes in glass while frequency is fixed by the source, so $\lambda=v/f$ must change. Because glass slows the light, its wavelength becomes shorter.
- id: frequency
  content: Frequency
  correct: true
  feedback: |-
    Frequency is fixed by the source and must remain continuous across the stationary boundary. The change in speed therefore appears as a change in wavelength, so frequency is the unchanged quantity.
- id: speed
  content: Effective speed
  feedback: |-
    Glass has a larger refractive index than air, so the effective speed $v=c/n$ is smaller in glass. Frequency—not propagation speed—is preserved across the boundary.
```

---

<a id="summary"></a>
## Summary

- At a stationary, time-independent boundary, light keeps the source-set frequency: $f_1=f_2$.
- The medium controls propagation speed through $v=c/n$; a larger index means a smaller speed.
- Since $v=f\lambda$ and $f$ is unchanged, wavelength changes in the same ratio as speed.
- Across two media,
  $$
  \frac{v_2}{v_1}
  =\frac{\lambda_2}{\lambda_1}
  =\frac{n_1}{n_2}.
  $$
- For air into glass, speed decreases and wavelength decreases, while frequency remains unchanged.
- Do not confuse the invariant frequency with the ray angle, wavelength, or effective speed, all of which can change at refraction.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
