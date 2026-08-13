# Update a Sound Level after the Listener Moves

<!--
lesson-id: 212-M5-072
topic-code: MTH212.M5.72
-->

## Table of Contents

- [Introduction](#introduction)
- [Set Up the Distance-Ratio Update](#distance-update)
- [Source-Video Worked Case: Double the Distance](#source-double-distance)
- [Move the Listener Closer](#move-closer)
- [Use Consistent Distance Units](#distance-units)
- [Check the Model Conditions](#model-conditions)
- [Summary](#summary)

## Prerequisites

- Use $I\propto1/r^2$ for spherical spreading from an unchanged point source.
- Use $\beta=10\log_{10}(I/I_0)$ for sound intensity level.
- Evaluate a base-10 logarithm.
- Form a ratio from two distances in the same units.

---

<a id="introduction"></a>
## Introduction

Look for one unchanged sound source, an initial level $\beta_1$ at distance $r_1$, and a new listener distance $r_2$. Predict whether the level rises or falls, then use

$$
\boxed{\beta_2=\beta_1+20\log_{10}\left(\frac{r_1}{r_2}\right)}.
$$

The distance order is tied to the level order: $\beta_2-\beta_1$ goes with $r_1/r_2$.

The formula joins two earlier results. [[MCT-Problem-10|Problem 10]] gives the inverse-square intensity ratio,

$$
\frac{I_2}{I_1}=\left(\frac{r_1}{r_2}\right)^2,
$$

and [[MCT-Problem-13|Problem 13]] gives the level difference,

$$
\beta_2-\beta_1=10\log_{10}\left(\frac{I_2}{I_1}\right).
$$

Combining them produces

$$
\beta_2-\beta_1
=10\log_{10}\left[\left(\frac{r_1}{r_2}\right)^2\right]
=20\log_{10}\left(\frac{r_1}{r_2}\right).
$$

The factor $20$ is $10$ from the decibel definition times $2$ from the inverse-square exponent.

**Quantity correction.** Intensity $I$, measured in $\mathrm{W/m^2}$, follows the inverse-square law. Sound intensity level $\beta$, measured in decibels, is logarithmic. Do not write $\beta_2/\beta_1=(r_1/r_2)^2$ or divide a decibel value by a distance-squared factor.

---

<a id="distance-update"></a>
## Set Up the Distance-Ratio Update

Use the distance comparison to predict the sign before touching the calculator:

| Listener motion | Distance ratio | Logarithm | Level change |
|---|---:|---:|---:|
| farther away: $r_2>r_1$ | $r_1/r_2<1$ | negative | $\beta_2<\beta_1$ |
| closer: $r_2<r_1$ | $r_1/r_2>1$ | positive | $\beta_2>\beta_1$ |
| no move: $r_2=r_1$ | $r_1/r_2=1$ | zero | $\beta_2=\beta_1$ |

Common distance factors provide quick checks:

| New-distance factor $r_2/r_1$ | Intensity factor $I_2/I_1$ | Level change $\beta_2-\beta_1$ |
|---:|---:|---:|
| $2$ | $1/4$ | $-6.02\ \mathrm{dB}$ |
| $1/2$ | $4$ | $+6.02\ \mathrm{dB}$ |
| $4$ | $1/16$ | $-12.04\ \mathrm{dB}$ |
| $1/4$ | $16$ | $+12.04\ \mathrm{dB}$ |

Write the old pair and new pair before substituting:

$$
(\beta_1,r_1)\longrightarrow(\beta_2,r_2).
$$

This pairing prevents the common error of reversing the distance ratio while leaving $\beta_2-\beta_1$ unchanged.

```quiz
type: radio
id: mct-p14-choose-setup
shuffle: true
content: |-
  A listener measures $64\ \mathrm{dB}$ at $5.0\ \mathrm m$ from an unchanged point source and then moves to $10.0\ \mathrm m$. Which setup and prediction are correct?
options:
- id: mct-p14-choose-setup-a
  content: |-
    $\beta_2=64+20\log_{10}(5.0/10.0)$, so $\beta_2<64\ \mathrm{dB}$
  correct: true
  feedback: |-
    The update $\beta_2-\beta_1$ pairs with $r_1/r_2$. Here $5.0/10.0<1$, so the logarithm is negative and the new level is below $64\ \mathrm{dB}$.
- id: mct-p14-choose-setup-b
  content: |-
    $\beta_2=64+20\log_{10}(10.0/5.0)$, so $\beta_2>64\ \mathrm{dB}$
  feedback: |-
    This reverses the distance ratio. Moving farther must lower the level; for $\beta_2-\beta_1$, use the old distance over the new distance, $5.0/10.0$.
- id: mct-p14-choose-setup-c
  content: |-
    $\beta_2=64(5.0/10.0)^2=16\ \mathrm{dB}$
  feedback: |-
    The inverse-square ratio updates linear intensity, not the logarithmic decibel value. Convert the intensity ratio into an additive level change with $20\log_{10}(r_1/r_2)$.
- id: mct-p14-choose-setup-d
  content: |-
    $\beta_2=64+10\log_{10}(5.0/10.0)$
  feedback: |-
    This omits the factor $2$ from spherical spreading. Since intensity varies as $1/r^2$, the distance formula uses $10\times2=20$ in front of the logarithm.
- id: mct-p14-choose-setup-e
  content: |-
    $\beta_2=64+20\log_{10}[(5.0/10.0)^2]$
  feedback: |-
    This counts the inverse-square exponent twice: once inside the logarithm and again through the coefficient $20$. Use either $10\log_{10}[(r_1/r_2)^2]$ or $20\log_{10}(r_1/r_2)$, not both together.
```

---

<a id="source-double-distance"></a>
## Source-Video Worked Case: Double the Distance

### Source-video worked case — `twppI9Eizp8`, 00:04:55–00:11:51

The source gives a level of $40\ \mathrm{dB}$ at $2\ \mathrm m$ and asks for the level at $4\ \mathrm m$. The listener moves farther, so the answer must be below $40\ \mathrm{dB}$.

Pair the data:

$$
\beta_1=40\ \mathrm{dB},
\qquad
r_1=2\ \mathrm m,
\qquad
r_2=4\ \mathrm m.
$$

Then

$$
\begin{aligned}
\beta_2
&=40+20\log_{10}\left(\frac{2}{4}\right)\\
&=40+20(-0.30103\ldots)\\
&=40-6.0206\ldots\\
&=33.9794\ldots\ \mathrm{dB}\\
&\approx33.98\ \mathrm{dB}.
\end{aligned}
$$

Doubling distance reduces intensity to one fourth, but it reduces sound level by about $6.02\ \mathrm{dB}$. It does not reduce the decibel value to one fourth.

**Precision note.** The unrounded result is $33.9794\ldots\ \mathrm{dB}$, so the source result is $33.98\ \mathrm{dB}$ to two decimal places.

```quiz
type: radio
id: mct-p14-double-distance
shuffle: true
content: |-
  A listener measures $72\ \mathrm{dB}$ at $3.0\ \mathrm m$ from an unchanged point source. What level is predicted at $6.0\ \mathrm m$?
options:
- id: mct-p14-double-distance-a
  content: |-
    $65.98\ \mathrm{dB}$
  correct: true
  feedback: |-
    Doubling distance makes $r_1/r_2=1/2$, so the change is $20\log_{10}(1/2)=-6.0206\ldots\ \mathrm{dB}$. Therefore, $\beta_2=72-6.0206\ldots=65.98\ \mathrm{dB}$.
- id: mct-p14-double-distance-b
  content: |-
    $78.02\ \mathrm{dB}$
  feedback: |-
    This uses $r_2/r_1=2$ and gives a positive change. The listener moved farther, so the level must fall; use $r_1/r_2=1/2$ for $\beta_2-\beta_1$.
- id: mct-p14-double-distance-c
  content: |-
    $68.99\ \mathrm{dB}$
  feedback: |-
    This uses $10\log_{10}(1/2)$ and misses the square in the intensity-distance law. The square supplies a second factor, so the coefficient is $20$ and the decrease is $6.02\ \mathrm{dB}$.
- id: mct-p14-double-distance-d
  content: |-
    $59.96\ \mathrm{dB}$
  feedback: |-
    This squares the distance ratio inside the logarithm while still using the already-doubled coefficient $20$. That applies the inverse-square exponent twice and doubles the correct level change.
- id: mct-p14-double-distance-e
  content: |-
    $18\ \mathrm{dB}$
  feedback: |-
    One fourth is the new intensity fraction after doubling distance. Decibel level is logarithmic, so it changes by $10\log_{10}(1/4)=-6.02\ \mathrm{dB}$ rather than being divided by $4$.
```

---

<a id="move-closer"></a>
## Move the Listener Closer

**Example:** A level is $55\ \mathrm{dB}$ at $12\ \mathrm m$. Find the level at $3.0\ \mathrm m$ for the same point source at unchanged power.

**Explanation**

The new distance is one fourth of the old distance, so the listener is closer and the level must rise:

$$
\begin{aligned}
\beta_2
&=55+20\log_{10}\left(\frac{12}{3.0}\right)\\
&=55+20\log_{10}(4)\\
&=55+12.0412\ldots\\
&=67.04\ \mathrm{dB}.
\end{aligned}
$$

Moving four times closer is two successive halvings of distance, so the increase is about $2(6.02)=12.04\ \mathrm{dB}$.

```quiz
type: radio
id: mct-p14-move-closer
shuffle: true
content: |-
  A listener measures $58\ \mathrm{dB}$ at $8.0\ \mathrm m$ from an unchanged point source and moves to $2.0\ \mathrm m$. What is the new level?
options:
- id: mct-p14-move-closer-a
  content: |-
    $70.04\ \mathrm{dB}$
  correct: true
  feedback: |-
    The listener moves four times closer, so $r_1/r_2=4$ and the change is $20\log_{10}(4)=12.0412\ldots\ \mathrm{dB}$. Adding it to $58\ \mathrm{dB}$ gives $70.04\ \mathrm{dB}$.
- id: mct-p14-move-closer-b
  content: |-
    $45.96\ \mathrm{dB}$
  feedback: |-
    This reverses the distance ratio and subtracts $12.04\ \mathrm{dB}$. Moving closer increases intensity and level, so $r_1/r_2=8/2=4$ must produce a positive change.
- id: mct-p14-move-closer-c
  content: |-
    $64.02\ \mathrm{dB}$
  feedback: |-
    This includes only one $6.02\ \mathrm{dB}$ increase. Going from $8\ \mathrm m$ to $2\ \mathrm m$ halves the distance twice, so the total increase is about $12.04\ \mathrm{dB}$.
- id: mct-p14-move-closer-d
  content: |-
    $82.08\ \mathrm{dB}$
  feedback: |-
    This squares the factor $4$ and then still uses $20\log_{10}$, applying the inverse-square exponent twice. The distance-only form already includes that exponent in its coefficient $20$.
- id: mct-p14-move-closer-e
  content: |-
    $928\ \mathrm{dB}$
  feedback: |-
    Moving four times closer raises linear intensity by $4^2=16$, but the decibel value is not multiplied by $16$. The level increase is $10\log_{10}(16)=12.04\ \mathrm{dB}$.
```

---

<a id="distance-units"></a>
## Use Consistent Distance Units

The logarithm needs a dimensionless argument. Convert $r_1$ and $r_2$ to the same unit before taking their ratio.

**Example:** A level is $50\ \mathrm{dB}$ at $50\ \mathrm{cm}$. Find the level at $2.0\ \mathrm m$ for the same source.

**Explanation**

Convert $50\ \mathrm{cm}=0.50\ \mathrm m$. Then

$$
\begin{aligned}
\beta_2
&=50+20\log_{10}\left(\frac{0.50\ \mathrm m}{2.0\ \mathrm m}\right)\\
&=50+20\log_{10}(0.25)\\
&=37.96\ \mathrm{dB}.
\end{aligned}
$$

The meters cancel. Taking $\log_{10}(50/2.0)$ without converting would attach a meaningless numerical value to a ratio of centimeters and meters.

```quiz
type: radio
id: mct-p14-distance-units
shuffle: true
content: |-
  A listener measures $64\ \mathrm{dB}$ at $0.75\ \mathrm m$ from an unchanged point source and moves to $300\ \mathrm{cm}$. What is the new level?
options:
- id: mct-p14-distance-units-a
  content: |-
    $51.96\ \mathrm{dB}$
  correct: true
  feedback: |-
    Convert $300\ \mathrm{cm}=3.00\ \mathrm m$. The distance increases by a factor of $4$, so $\beta_2=64+20\log_{10}(0.75/3.00)=51.96\ \mathrm{dB}$.
- id: mct-p14-distance-units-b
  content: |-
    $76.04\ \mathrm{dB}$
  feedback: |-
    This uses the new distance over the old distance and predicts an increase. After conversion, the listener moves from $0.75\ \mathrm m$ to $3.00\ \mathrm m$, so the level must decrease.
- id: mct-p14-distance-units-c
  content: |-
    $57.98\ \mathrm{dB}$
  feedback: |-
    This accounts for only one doubling of distance. The move from $0.75\ \mathrm m$ to $3.00\ \mathrm m$ is a factor of $4$, or two doublings, so the decrease is about $12.04\ \mathrm{dB}$.
- id: mct-p14-distance-units-d
  content: |-
    $11.96\ \mathrm{dB}$
  feedback: |-
    This forms $0.75/300$ without matching the meter and centimeter units. Convert first: $300\ \mathrm{cm}=3.00\ \mathrm m$, so the dimensionless ratio is $0.75/3.00=0.25$.
- id: mct-p14-distance-units-e
  content: |-
    $4.0\ \mathrm{dB}$
  feedback: |-
    The intensity falls by a factor of $4^2=16$, but dividing the decibel value by $16$ is not valid. Apply the logarithmic change, $10\log_{10}(1/16)=-12.04\ \mathrm{dB}$.
```

---

<a id="model-conditions"></a>
## Check the Model Conditions

The distance update cancels source power only when both measurements use the same source at unchanged power. It also assumes approximately spherical spreading with no new absorption, barrier, or strong reflection between the two positions.

If the source output changes, two different sources are compared, or the environment changes, the level difference includes more than distance and the shortcut cannot isolate that change.

```quiz
type: radio
id: mct-p14-model-conditions
shuffle: true
content: |-
  Which situation can be modeled directly with $\beta_2=\beta_1+20\log_{10}(r_1/r_2)$?
options:
- id: mct-p14-model-conditions-a
  content: |-
    The same speaker keeps the same output while a listener moves from $2\ \mathrm m$ to $5\ \mathrm m$ in an open field.
  correct: true
  feedback: |-
    The source and its power are unchanged, and the open-field description supports spherical spreading without a new barrier. Distance is the modeled cause of the level change.
- id: mct-p14-model-conditions-b
  content: |-
    A listener moves farther away while the speaker's power is doubled.
  feedback: |-
    The formula cancels source power only when that power is unchanged. Here both distance and power change, so the distance term alone cannot determine the new level.
- id: mct-p14-model-conditions-c
  content: |-
    A listener compares two different speakers at the same distance.
  feedback: |-
    Equal distance does not make different source powers cancel. The update formula compares positions around the same unchanged source, not two unrelated speakers.
- id: mct-p14-model-conditions-d
  content: |-
    A listener moves behind a sound-absorbing wall while keeping the same distance from the speaker.
  feedback: |-
    The wall adds attenuation that is not part of spherical distance spreading. With $r_1=r_2$, the formula predicts zero distance change and cannot account for the wall.
- id: mct-p14-model-conditions-e
  content: |-
    A listener moves along a long line of speakers whose sound does not spread spherically.
  feedback: |-
    The coefficient $20$ comes from the $1/r^2$ intensity law for spherical spreading. A source geometry with a different spreading law requires a different distance dependence.
```

---

<a id="summary"></a>
## Summary

For the same point source at unchanged power under spherical spreading:

1. Pair the old and new data: $(\beta_1,r_1)\to(\beta_2,r_2)$.
2. Predict the sign: farther means lower level; closer means higher level.
3. Convert distances to the same unit.
4. Calculate
   $$
   \beta_2=\beta_1+20\log_{10}\left(\frac{r_1}{r_2}\right).
   $$
5. Check that the sign agrees with the listener's motion.

Doubling distance changes intensity by a factor of $1/4$ but changes level by about $-6.02\ \mathrm{dB}$. The inverse-square law acts on intensity; the logarithm turns that multiplicative intensity ratio into an additive decibel change.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
