# Comparing Sound Levels for Spherical and Tube Spreading

<!--
lesson-id: 212-M5-019
topic-code: MTH212.M5.19
-->

## Table of Contents

- [Introduction](#introduction)
- [Compare Intensity Using Carrying Area](#compare-intensity-using-carrying-area)
- [Turn an Intensity Ratio Into a Level Change](#turn-an-intensity-ratio-into-a-level-change)
- [Build the Sphere-to-Tube Area Ratio](#build-the-sphere-to-tube-area-ratio)
- [Use the Logarithm Power Rule](#use-the-logarithm-power-rule)
- [Summary](#summary)

## Prerequisites

- Use intensity as power per area: $I=P/A$.
- Recall the areas $4\pi d^2$ for a sphere of radius $d$ and $\pi r^2$ for a circle of radius $r$.
- Use $\beta=(10\ \mathrm{dB})\log_{10}(I/I_0)$ and the power rule $\log_{10}(x^a)=a\log_{10}x$.

---

<a id="introduction"></a>
## Introduction

When the same sound source sends the same acoustic power through two different areas, the smaller carrying area has the greater intensity. The recognition cue is a comparison between sound spreading freely at distance $d$ and sound confined to a lossless tube of radius $r$.

Do not try to determine the acoustic power or the reference intensity $I_0$. Compare the two intensities directly, then convert their ratio into a change in sound intensity level:

$$
\frac{I_2}{I_1}=\frac{A_1}{A_2},
\qquad
\beta_2=\beta_1+(10\ \mathrm{dB})\log_{10}\left(\frac{I_2}{I_1}\right).
$$

For free spherical spreading and confinement to a cylindrical tube,

| Situation | Area carrying the power | Intensity |
| --- | --- | --- |
| Free sound at distance $d$ | $4\pi d^2$ | $P/(4\pi d^2)$ |
| Sound in a tube of radius $r$ | $\pi r^2$ | $P/(\pi r^2)$ |

The procedure is to reverse the area ratio, put that intensity ratio inside the base-$10$ logarithm, and simplify the square with the logarithm power rule.

---

<a id="compare-intensity-using-carrying-area"></a>
## Compare Intensity Using Carrying Area

**Example:** The same source power $P$ is distributed first across an area of $12\ \mathrm{m^2}$ and then across an area of $3\ \mathrm{m^2}$. Find the second intensity relative to the first.

**Explanation**

Write one intensity for each area:

$$
I_1=\frac{P}{12\ \mathrm{m^2}},
\qquad
I_2=\frac{P}{3\ \mathrm{m^2}}.
$$

In the ratio, the common power cancels:

$$
\begin{aligned}
\frac{I_2}{I_1}
&=\frac{P/(3\ \mathrm{m^2})}{P/(12\ \mathrm{m^2})} \\
&=\frac{12}{3} \\
&=4.
\end{aligned}
$$

The second area is one-quarter as large, so the second intensity is four times larger. The area ratio reverses because intensity is power divided by area.

| Area change at fixed power | Intensity change |
| --- | --- |
| $A_2=A_1$ | $I_2=I_1$ |
| $A_2=A_1/2$ | $I_2=2I_1$ |
| $A_2=A_1/k$ | $I_2=kI_1$ |

```quiz
type: radio
id: p6-area-q1
content: |-
  The same acoustic power is spread across an area of $80\ \mathrm{m^2}$ in one situation and confined to an area of $5\ \mathrm{m^2}$ in a second situation. What is $I_2/I_1$?
options:
- id: p6-area-q1-a
  content: |-
    $\dfrac{1}{16}$
- id: p6-area-q1-b
  content: |-
    $5$
- id: p6-area-q1-c
  content: |-
    $16$
  correct: true
- id: p6-area-q1-d
  content: |-
    $75$
- id: p6-area-q1-e
  content: |-
    $400$
```

---

<a id="turn-an-intensity-ratio-into-a-level-change"></a>
## Turn an Intensity Ratio Into a Level Change

**Example:** A sound has intensity level $\beta_1$. A second sound has $100$ times the intensity of the first. Express the second intensity level in terms of $\beta_1$.

**Explanation**

Sound intensity level is

$$
\beta=(10\ \mathrm{dB})\log_{10}\left(\frac{I}{I_0}\right).
$$

Subtracting the first level from the second and using the quotient rule gives

$$
\begin{aligned}
\beta_2-\beta_1
&=(10\ \mathrm{dB})
\left[
\log_{10}\left(\frac{I_2}{I_0}\right)
-\log_{10}\left(\frac{I_1}{I_0}\right)
\right] \\
&=(10\ \mathrm{dB})\log_{10}\left(\frac{I_2}{I_1}\right).
\end{aligned}
$$

Keep the ratio in new-over-old order. Reversing the ratio reverses the sign of the level change.

Since $I_2/I_1=100=10^2$,

$$
\beta_2-\beta_1
=(10\ \mathrm{dB})\log_{10}(10^2)
=20\ \mathrm{dB}.
$$

Therefore,

$$
\beta_2=\beta_1+20\ \mathrm{dB}.
$$

A multiplicative change in intensity becomes an additive change in decibels.

```quiz
type: radio
id: p6-level-q1
content: |-
  A second sound has $1000$ times the intensity of a first sound whose intensity level is $\beta_1$. What is the second sound's intensity level?
options:
- id: p6-level-q1-a
  content: |-
    $\beta_1+3\ \mathrm{dB}$
- id: p6-level-q1-b
  content: |-
    $\beta_1+10\ \mathrm{dB}$
- id: p6-level-q1-c
  content: |-
    $\beta_1+30\ \mathrm{dB}$
  correct: true
- id: p6-level-q1-d
  content: |-
    $30\beta_1$
- id: p6-level-q1-e
  content: |-
    $1000\beta_1$
```

---

<a id="build-the-sphere-to-tube-area-ratio"></a>
## Build the Sphere-to-Tube Area Ratio

**Example:** A source emits power $P$. Compare its intensity at distance $d$ under free spherical spreading with its intensity when the same power is carried without loss by a tube of radius $r$.

**Explanation**

In free space, the power is spread across the surface of a sphere of radius $d$:

$$
A_{\mathrm{free}}=4\pi d^2,
\qquad
I_{\mathrm{free}}=\frac{P}{4\pi d^2}.
$$

In the tube, no energy passes through the walls, so the same power crosses the tube's circular cross section:

$$
A_{\mathrm{tube}}=\pi r^2,
\qquad
I_{\mathrm{tube}}=\frac{P}{\pi r^2}.
$$

Divide the tube intensity by the free intensity. The common power and $\pi$ cancel:

$$
\begin{aligned}
\frac{I_{\mathrm{tube}}}{I_{\mathrm{free}}}
&=\frac{P/(\pi r^2)}{P/(4\pi d^2)} \\
&=\frac{4\pi d^2}{\pi r^2} \\
&=\frac{4d^2}{r^2} \\
&=\left(\frac{2d}{r}\right)^2.
\end{aligned}
$$

This ratio is dimensionless because $d$ and $r$ are both lengths.

Use the tube's stated radius directly in $\pi r^2$. The tube length $d$ sets the comparison distance, but it does not set the tube's cross-sectional area.

```quiz
type: radio
id: p6-geometry-q1
content: |-
  The same sound power is either spread freely to a distance $d=8\ \mathrm{m}$ or carried without loss through a tube of radius $r=2\ \mathrm{m}$. What is $I_{\mathrm{tube}}/I_{\mathrm{free}}$?
options:
- id: p6-geometry-q1-a
  content: |-
    $4$
- id: p6-geometry-q1-b
  content: |-
    $8$
- id: p6-geometry-q1-c
  content: |-
    $16$
- id: p6-geometry-q1-d
  content: |-
    $64$
  correct: true
- id: p6-geometry-q1-e
  content: |-
    $256$
```

---

<a id="use-the-logarithm-power-rule"></a>
## Use the Logarithm Power Rule

**Example:** A freely spreading sound has intensity level $\beta$, and confinement to a tube makes the intensity ratio $\left(2d/r\right)^2$. Express the tube's level without a square inside the logarithm.

**Explanation**

First place the intensity ratio inside the level-change formula:

$$
\beta_{\mathrm{tube}}
=\beta+(10\ \mathrm{dB})
\log_{10}\left[\left(\frac{2d}{r}\right)^2\right].
$$

Now use $\log_{10}(x^2)=2\log_{10}x$:

$$
\beta_{\mathrm{tube}}
=\beta+(20\ \mathrm{dB})
\log_{10}\left(\frac{2d}{r}\right).
$$

The factor $20\ \mathrm{dB}$ appears because the area ratio contains a square. It does not mean that the definition of sound intensity level changed from a factor of $10\ \mathrm{dB}$.

For an ordinary narrow tube, $2d/r>1$, so the logarithm is positive and the confined sound level is greater than the freely spread sound level. This is a useful direction check.

```quiz
type: radio
id: p6-homework-q1
shuffle: true
content: |-
  You perceive a sound intensity level $\beta$ when a person shouts from a distance $d$.

  If the person were instead to shout just as loud into a cylindrical tube of length $d$ and radius $r$, what would the sound intensity level of their shout be at the opposite end of the tube?

  Assume the sound propagates along the tube without transferring energy through the walls of the tube.

  Hint: Remember that $\log_{10}(x^a)=a\log_{10}x$.
options:
- id: p6-homework-q1-a
  content: |-
    $\beta+(20\ \mathrm{dB})\log_{10}\left(\dfrac{2d}{r}\right)$
  correct: true
- id: p6-homework-q1-b
  content: |-
    $\beta+(10\ \mathrm{dB})\log_{10}\left(\dfrac{r}{d+r}\right)$
- id: p6-homework-q1-c
  content: |-
    $\beta-(10\ \mathrm{dB})\log_{10}\left(\dfrac{r+d}{d}\right)$
- id: p6-homework-q1-d
  content: |-
    $\beta+(10\ \mathrm{dB})\left(\dfrac{r}{2d}\right)^2$
```

---

<a id="summary"></a>
## Summary

**Recognition cue:** The same sound power is compared after free spherical spreading and after lossless confinement to a tube.

**Procedure:**

1. Write $I=P/A$ for both situations.
2. Reverse the carrying-area ratio to get the intensity ratio.
3. Convert the ratio to a level change with $(10\ \mathrm{dB})\log_{10}(I_2/I_1)$.
4. Use the logarithm power rule when the area ratio contains a square.

For a free sound at distance $d$ and a tube of radius $r$,

$$
\frac{I_{\mathrm{tube}}}{I_{\mathrm{free}}}
=\frac{4\pi d^2}{\pi r^2}
=\left(\frac{2d}{r}\right)^2,
$$

so

$$
\boxed{
\beta_{\mathrm{tube}}
=\beta+(20\ \mathrm{dB})\log_{10}\left(\frac{2d}{r}\right)
}.
$$

**Main traps:** Do not use the area ratio in the wrong direction, omit the square from the geometric areas, or multiply $\beta$ by the intensity ratio. A multiplicative intensity ratio produces an additive decibel change.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
