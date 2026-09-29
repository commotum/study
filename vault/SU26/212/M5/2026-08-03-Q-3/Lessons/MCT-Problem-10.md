# Rescale Wave Intensity or Amplitude with Distance

<!--
lesson-id: 212-M5-068
topic-code: MTH212.M5.68
-->

## Table of Contents

- [Introduction](#introduction)
- [Source-Video Problem 1: Intensity at Two Larger Distances](#source-basic-intensity)
- [Source-Video Problem 2: Rescale the Lamp Intensity](#source-lamp-intensity)
- [Source-Video Problem 3: Move Closer Using One Distance Unit](#source-closer-intensity)
- [Source-Video Problem 4: Amplitude Uses the First Power](#source-amplitude)
- [Lecture Transfer: Speaker Intensity after Doubling Distance](#lecture-speaker)
- [Connect Intensity and Amplitude Ratios](#intensity-amplitude-connection)
- [Summary](#summary)

## Prerequisites

- Write and evaluate equivalent ratios.
- Square whole numbers and fractions.
- Distinguish a quantity from the square of that quantity.
- Keep paired values under consistent subscripts.
- Recognize intensity units, $\mathrm{W/m^2}$.

---

<a id="introduction"></a>
## Introduction

For the **same isotropic source with unchanged power**, intensity spreads over spherical area $4\pi r^2$. Between two distances,

$$
\boxed{
\frac{I_2}{I_1}
=\left(\frac{r_1}{r_2}\right)^2
}
\qquad\Longrightarrow\qquad
\boxed{
I_2=I_1\left(\frac{r_1}{r_2}\right)^2
}.
$$

Wave amplitude uses one power of the same reversed distance ratio:

$$
\boxed{
\frac{A_2}{A_1}=\frac{r_1}{r_2}
}
\qquad\Longrightarrow\qquad
\boxed{
A_2=A_1\left(\frac{r_1}{r_2}\right)
}.
$$

Before calculating, predict the direction:

- moving farther away makes intensity and amplitude smaller;
- moving closer makes both larger.

Then pair each measurement with its distance and reverse the distance ratio. The only remaining choice is the exponent: square the ratio for intensity, but not for amplitude.

The subscripts preserve those pairs:

| State | Measured quantity | Distance from source |
|---|---:|---:|
| initial | $I_1$ or $A_1$ | $r_1$ |
| new | $I_2$ or $A_2$ | $r_2$ |

In the scale factor $r_1/r_2$, the subscripts reverse because the relationship is inverse. In $I_2/I_1=(A_2/A_1)^2$, the amplitude and intensity subscripts match because that relationship is direct.

| Requested quantity | Scaling law | If distance doubles |
|---|---:|---:|
| intensity $I$ | $I\propto 1/r^2$ | $I$ becomes $1/4$ as large |
| amplitude $A$ | $A\propto 1/r$ | $A$ becomes $1/2$ as large |

These laws assume the source power and spreading geometry do not change between positions. Absorption, obstacles, reflections, directional emission, or a changed source power would break the simple ratio model.

---

<a id="source-basic-intensity"></a>
## Source-Video Problem 1: Intensity at Two Larger Distances

The first source segment (`vEzftaDL7fM`, 00:21:35–00:26:59) starts with

$$
I_1=900\ \mathrm{W/m^2}
\qquad\text{at}\qquad
r_1=1\ \mathrm m.
$$

At $r_2=2\ \mathrm m$, predict a decrease because the observation point is farther away. Then

$$
I_2=(900)\left(\frac{1}{2}\right)^2
=(900)\left(\frac14\right)
=\boxed{225\ \mathrm{W/m^2}}.
$$

At $r_2=3\ \mathrm m$,

$$
I_2=(900)\left(\frac{1}{3}\right)^2
=(900)\left(\frac19\right)
=\boxed{100\ \mathrm{W/m^2}}.
$$

Doubling distance divides intensity by $2^2=4$; tripling distance divides it by $3^2=9$.

```quiz
type: radio
id: mct-p10-intensity-farther
shuffle: true
content: |-
  The intensity from an isotropic source is $640\ \mathrm{W/m^2}$ at $8.0\ \mathrm m$. The source power stays fixed. What is the intensity at $16.0\ \mathrm m$?
options:
- id: mct-p10-intensity-farther-a
  content: |-
    $160\ \mathrm{W/m^2}$
  correct: true
  feedback: |-
    Distance doubles, so intensity falls by the square of $2$. Equivalently, $I_2=(640)(8.0/16.0)^2=(640)(1/4)=160\ \mathrm{W/m^2}$.
- id: mct-p10-intensity-farther-b
  content: |-
    $320\ \mathrm{W/m^2}$
  feedback: |-
    This uses the first power of the distance ratio. That is the amplitude rule; intensity uses $(r_1/r_2)^2$, so doubling distance leaves one-fourth, not one-half.
- id: mct-p10-intensity-farther-c
  content: |-
    $2560\ \mathrm{W/m^2}$
  feedback: |-
    This reverses the distance ratio. Moving farther from the same source must reduce intensity, so use old distance over new distance: $(8.0/16.0)^2$.
- id: mct-p10-intensity-farther-d
  content: |-
    $1280\ \mathrm{W/m^2}$
  feedback: |-
    This multiplies by the distance factor $2$. Spherical area grows as $r^2$, so the unchanged power is spread over four times the area and intensity decreases.
- id: mct-p10-intensity-farther-e
  content: |-
    $640\ \mathrm{W/m^2}$
  feedback: |-
    Unchanged source power does not mean unchanged intensity. Intensity is power per area, and the spherical area is larger at $16.0\ \mathrm m$.
```

---

<a id="source-lamp-intensity"></a>
## Source-Video Problem 2: Rescale the Lamp Intensity

The lamp calculation (`vEzftaDL7fM`, 00:32:07–00:33:43) begins with the Problem 9 result

$$
I_1=9.95\ \mathrm{W/m^2}
\qquad\text{at}\qquad
r_1=1\ \mathrm m.
$$

At $2\ \mathrm m$,

$$
I_2=(9.95)\left(\frac12\right)^2
=2.4875\ \mathrm{W/m^2}
\approx\boxed{2.49\ \mathrm{W/m^2}}.
$$

At $3\ \mathrm m$,

$$
I_2=(9.95)\left(\frac13\right)^2
=1.1055\ldots\ \mathrm{W/m^2}
\approx\boxed{1.1\ \mathrm{W/m^2}}.
$$

The absolute source power is unnecessary once one intensity–distance pair is known. The ratio works because the same power and $4\pi$ appear in both states and cancel.

This can also be viewed as a constant-product check for inverse-square variation:

$$
I_1r_1^2=I_2r_2^2.
$$

```quiz
type: radio
id: mct-p10-intensity-closer
shuffle: true
content: |-
  A lamp produces intensity $75\ \mathrm{W/m^2}$ at $24\ \mathrm{cm}$. What intensity is measured at $8.0\ \mathrm{cm}$ if the lamp output is unchanged?
options:
- id: mct-p10-intensity-closer-a
  content: |-
    $675\ \mathrm{W/m^2}$
  correct: true
  feedback: |-
    The new point is three times closer, so intensity grows by $3^2=9$. Using the paired ratio, $I_2=(75)(24/8.0)^2=(75)(9)=675\ \mathrm{W/m^2}$.
- id: mct-p10-intensity-closer-b
  content: |-
    $225\ \mathrm{W/m^2}$
  feedback: |-
    This uses first-power distance scaling. Amplitude scales that way, but intensity scales with the square, so becoming three times closer multiplies intensity by $9$.
- id: mct-p10-intensity-closer-c
  content: |-
    $8.33\ \mathrm{W/m^2}$
  feedback: |-
    This uses $(8.0/24)^2$ and predicts a decrease while moving closer. Reverse the distance ratio: the old distance belongs above the new distance.
- id: mct-p10-intensity-closer-d
  content: |-
    $25\ \mathrm{W/m^2}$
  feedback: |-
    This divides by the distance factor $3$. Moving closer increases intensity, and inverse-square scaling multiplies it by $3^2=9$.
- id: mct-p10-intensity-closer-e
  content: |-
    $75\ \mathrm{W/m^2}$
  feedback: |-
    The lamp's power stays fixed, but the same power passes through a smaller spherical area closer to the lamp. The local intensity therefore increases.
```

---

<a id="source-closer-intensity"></a>
## Source-Video Problem 3: Move Closer Using One Distance Unit

In the third source problem (`vEzftaDL7fM`, 00:39:10–00:41:46),

$$
I_1=48\ \mathrm{W/m^2},
\qquad
r_1=30\ \mathrm{cm},
\qquad
r_2=15\ \mathrm{cm}.
$$

The new point is closer, so the answer must exceed $48\ \mathrm{W/m^2}$. Because both distances use centimeters, that unit cancels in the ratio:

$$
I_2=(48)\left(\frac{30\ \mathrm{cm}}{15\ \mathrm{cm}}\right)^2
=(48)(2)^2
=\boxed{192\ \mathrm{W/m^2}}.
$$

Distance units may remain unconverted only when the same unit appears in both parts of this dimensionless ratio. A ratio such as $30\ \mathrm{cm}/0.15\ \mathrm m$ must first be put in one unit.

```quiz
type: radio
id: mct-p10-distance-units
shuffle: true
content: |-
  Intensity is $36\ \mathrm{W/m^2}$ at $45\ \mathrm{cm}$ from a source. What is the intensity at $15\ \mathrm{cm}$, assuming unchanged isotropic output?
options:
- id: mct-p10-distance-units-a
  content: |-
    $324\ \mathrm{W/m^2}$
  correct: true
  feedback: |-
    Both distances are in centimeters, so their units cancel. The new point is three times closer: $I_2=(36)(45/15)^2=(36)(9)=324\ \mathrm{W/m^2}$.
- id: mct-p10-distance-units-b
  content: |-
    $108\ \mathrm{W/m^2}$
  feedback: |-
    This uses only the first power of the distance factor. Intensity uses inverse-square scaling, so the factor $45/15=3$ must be squared.
- id: mct-p10-distance-units-c
  content: |-
    $4\ \mathrm{W/m^2}$
  feedback: |-
    This reverses the ratio and makes intensity smaller at the closer point. Use old distance over new distance: $(45/15)^2=9$.
- id: mct-p10-distance-units-d
  content: |-
    $12\ \mathrm{W/m^2}$
  feedback: |-
    This divides by $3$ rather than multiplying by $3^2$. Moving from $45\ \mathrm{cm}$ to $15\ \mathrm{cm}$ increases intensity.
- id: mct-p10-distance-units-e
  content: |-
    $32\,400\ \mathrm{W/m^2}$
  feedback: |-
    This inserts an unnecessary centimeter-to-meter factor into only one distance. The ratio already has matching centimeter units, so use $45/15=3$ directly.
```

---

<a id="source-amplitude"></a>
## Source-Video Problem 4: Amplitude Uses the First Power

The amplitude segment (`vEzftaDL7fM`, 00:27:03–00:30:26 and 00:42:13–00:44:21) uses

$$
A_1=30
\qquad\text{at}\qquad
r_1=2\ \mathrm{cm}.
$$

Because $A\propto1/r$, the amplitude at $1\ \mathrm{cm}$ is

$$
A_2=(30)\left(\frac{2}{1}\right)=\boxed{60}.
$$

At $4\ \mathrm{cm}$,

$$
A_2=(30)\left(\frac{2}{4}\right)=\boxed{15},
$$

and at $6\ \mathrm{cm}$,

$$
A_2=(30)\left(\frac{2}{6}\right)=\boxed{10}.
$$

The prompt frame explicitly labels $1\ \mathrm{cm}$, $4\ \mathrm{cm}$, and $6\ \mathrm{cm}$. Near the end, the narration briefly says “$6\ \mathrm m$” but continues to substitute $6\ \mathrm{cm}$; the frame and calculation show that centimeters are intended.

Do not square the ratio in an amplitude question. Intensity and amplitude are related by $I\propto A^2$, so inverse-square intensity spreading corresponds to first-power amplitude spreading.

```quiz
type: radio
id: mct-p10-amplitude-farther
shuffle: true
content: |-
  A wave amplitude is $28$ units at $3.0\ \mathrm m$ from the same isotropic source. What is the amplitude at $12.0\ \mathrm m$?
options:
- id: mct-p10-amplitude-farther-a
  content: |-
    $7$ units
  correct: true
  feedback: |-
    Amplitude scales with the first power of inverse distance. The new point is four times farther, so $A_2=(28)(3.0/12.0)=7$ units.
- id: mct-p10-amplitude-farther-b
  content: |-
    $1.75$ units
  feedback: |-
    This squares the ratio and applies the intensity law. Amplitude uses $A_2/A_1=r_1/r_2$ without a square.
- id: mct-p10-amplitude-farther-c
  content: |-
    $112$ units
  feedback: |-
    This reverses the distance ratio. Moving farther from the same source reduces amplitude, so use $3.0/12.0$, not $12.0/3.0$.
- id: mct-p10-amplitude-farther-d
  content: |-
    $448$ units
  feedback: |-
    This both reverses and squares the distance ratio. The amplitude law is first-power inverse distance: $A_2=(28)(3.0/12.0)$.
- id: mct-p10-amplitude-farther-e
  content: |-
    $28$ units
  feedback: |-
    The source stays the same, but amplitude at the observation point changes with distance. At four times the distance it is one-fourth as large.
```

---

<a id="lecture-speaker"></a>
## Lecture Transfer: Speaker Intensity after Doubling Distance

The M5-3 lecture checks the same inverse-square move with a speaker:

$$
I_1=240\ \mathrm{W/m^2}
\qquad\text{at}\qquad
r_1=12\ \mathrm m.
$$

The listener moves to $r_2=24\ \mathrm m$, twice the original distance. Predict a decrease, then calculate:

$$
I_2=(240)\left(\frac{12}{24}\right)^2
=(240)\left(\frac14\right)
=\boxed{60\ \mathrm{W/m^2}}.
$$

The ratio is the same for a lamp, speaker, or other isotropic emitter when its power is unchanged and the wave spreads spherically without appreciable absorption.

```quiz
type: radio
id: mct-p10-speaker-intensity
shuffle: true
content: |-
  A listener measures $180\ \mathrm{W/m^2}$ at $10\ \mathrm m$ from a speaker. The listener moves to $30\ \mathrm m$ while the speaker output stays fixed. What intensity is measured?
options:
- id: mct-p10-speaker-intensity-a
  content: |-
    $20\ \mathrm{W/m^2}$
  correct: true
  feedback: |-
    The distance triples, so inverse-square spreading reduces intensity by $3^2=9$. Thus $I_2=(180)(10/30)^2=20\ \mathrm{W/m^2}$.
- id: mct-p10-speaker-intensity-b
  content: |-
    $60\ \mathrm{W/m^2}$
  feedback: |-
    This divides by the distance factor $3$ only. Intensity—not amplitude—is requested, so square the factor and divide by $9$.
- id: mct-p10-speaker-intensity-c
  content: |-
    $1620\ \mathrm{W/m^2}$
  feedback: |-
    This uses the distance ratio in the wrong direction and predicts an increase farther from the source. Use $(10/30)^2$.
- id: mct-p10-speaker-intensity-d
  content: |-
    $540\ \mathrm{W/m^2}$
  feedback: |-
    This multiplies by $3$. With fixed output, the power is spread over a larger spherical area, so intensity must decrease.
- id: mct-p10-speaker-intensity-e
  content: |-
    $180\ \mathrm{W/m^2}$
  feedback: |-
    The source output is unchanged, but intensity is power per area. Tripling radius makes the spherical area nine times larger.
```

---

<a id="intensity-amplitude-connection"></a>
## Connect Intensity and Amplitude Ratios

For the same kind of wave in the same medium,

$$
I\propto A^2.
$$

Therefore,

$$
\frac{I_2}{I_1}
=\left(\frac{A_2}{A_1}\right)^2.
$$

Combining this with distance scaling gives

$$
\left(\frac{A_2}{A_1}\right)^2
=\left(\frac{r_1}{r_2}\right)^2
\qquad\Longrightarrow\qquad
\frac{A_2}{A_1}=\frac{r_1}{r_2},
$$

where amplitudes and distances are nonnegative magnitudes. This is why an intensity ratio has the square while an amplitude ratio does not.

```quiz
type: radio
id: mct-p10-intensity-to-amplitude
shuffle: true
content: |-
  At a second point, a wave's intensity is $25/225=1/9$ of its intensity at the first point. Under the same wave conditions, what is $A_2/A_1$?
options:
- id: mct-p10-intensity-to-amplitude-a
  content: |-
    $1/3$
  correct: true
  feedback: |-
    Intensity is proportional to amplitude squared, so $A_2/A_1=\sqrt{I_2/I_1}=\sqrt{1/9}=1/3$.
- id: mct-p10-intensity-to-amplitude-b
  content: |-
    $1/9$
  feedback: |-
    This treats the intensity ratio as the amplitude ratio. Because $I\propto A^2$, take the square root of the intensity ratio.
- id: mct-p10-intensity-to-amplitude-c
  content: |-
    $3$
  feedback: |-
    This takes the reciprocal of the correct square root. Since $I_2<I_1$, the second amplitude must also be smaller, so its ratio must be below $1$.
- id: mct-p10-intensity-to-amplitude-d
  content: |-
    $9$
  feedback: |-
    This reverses the intensity ratio and also skips the square root. The smaller second intensity corresponds to a smaller second amplitude.
- id: mct-p10-intensity-to-amplitude-e
  content: |-
    $1/81$
  feedback: |-
    This squares the intensity ratio. To recover an amplitude ratio from $I\propto A^2$, use the inverse operation and take a square root.
```

---

<a id="summary"></a>
## Summary

For the same isotropic source with unchanged power:

$$
\boxed{I_2=I_1\left(\frac{r_1}{r_2}\right)^2}
\qquad\text{and}\qquad
\boxed{A_2=A_1\left(\frac{r_1}{r_2}\right)}.
$$

Use this sequence:

1. Predict whether the new value should increase or decrease.
2. Pair $I_1$ or $A_1$ with $r_1$, and the requested value with $r_2$.
3. Use the reversed distance ratio $r_1/r_2$.
4. Square the ratio for intensity; leave it first-power for amplitude.

As a final check, the squared distance times intensity should stay constant:

$$
I_1r_1^2=I_2r_2^2.
$$

Matching distance units cancel inside the ratio. If the units differ, convert one before dividing. A same-source statement is essential: these ratios do not apply unchanged if power, spreading geometry, absorption, or obstruction changes.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
