# Scaling Sound Intensity With the Inverse-Square Law

<!--
lesson-id: 212-M5-026
topic-code: MTH212.M5.26
-->

## Table of Contents

- [Introduction](#introduction)
- [Scale Intensity With a Distance Ratio](#scale-intensity-with-a-distance-ratio)
- [Reverse the Direction When Moving Closer](#reverse-the-direction-when-moving-closer)
- [Square the Entire Ratio](#square-the-entire-ratio)
- [Solve the Given Speaker Problem](#solve-the-given-speaker-problem)
- [Summary](#summary)

## Prerequisites

- Form a ratio from two distances measured in the same units.
- Square a fraction or decimal.
- Interpret $\mathrm{W/m^2}$ as a unit of sound intensity.

---

<a id="introduction"></a>
## Introduction

For sound spreading outward from the same point-like source, intensity $I$ varies inversely with the square of distance $r$:

$$
I\propto\frac{1}{r^2}.
$$

**Recognition cue:** The problem keeps the same speaker, gives one intensity-distance pair, and asks for the intensity at another distance. The inverse-square model applies when the sound can be treated as spreading outward from one point-like source without a new source or power change.

Because $Ir^2$ remains constant between the two locations,

$$
I_1r_1^2=I_2r_2^2.
$$

When an initial intensity $I_1$ is known at distance $r_1$, the intensity at a new distance $r_2$ is

$$
I_2=I_1\left(\frac{r_1}{r_2}\right)^2.
$$

The reliable move is to place the old distance over the new distance, square that entire ratio, and multiply the old intensity by the resulting scale factor.

---

<a id="scale-intensity-with-a-distance-ratio"></a>
## Scale Intensity With a Distance Ratio

**Example:** A sound intensity is $360\ \mathrm{W/m^2}$ at $5.0\ \mathrm{m}$ from a speaker. What is the intensity at $10\ \mathrm{m}$?

**Explanation**

The new distance is twice the initial distance, so the distance ratio is $5.0/10=1/2$. Apply the square to the ratio:

$$
\begin{aligned}
I_2
&=I_1\left(\frac{r_1}{r_2}\right)^2 \\
&=(360\ \mathrm{W/m^2})\left(\frac{5.0}{10}\right)^2 \\
&=(360\ \mathrm{W/m^2})\left(\frac12\right)^2 \\
&=90\ \mathrm{W/m^2}.
\end{aligned}
$$

The distance ratio is unitless because the meter units cancel. Therefore the result keeps the original intensity unit, $\mathrm{W/m^2}$.

```quiz
type: radio
id: p3-scale-farther
content: |-
  A sound intensity is $200\ \mathrm{W/m^2}$ at $4.0\ \mathrm{m}$ from a speaker. What is the intensity at $8.0\ \mathrm{m}$?
options:
- id: a
  content: |-
    $25\ \mathrm{W/m^2}$
  feedback: |-
    This applies the factor $1/2$ twice after already squaring it.
- id: b
  content: |-
    $50\ \mathrm{W/m^2}$
  correct: true
  feedback: |-
    Correct. Doubling the distance multiplies intensity by $(1/2)^2=1/4$.
- id: c
  content: |-
    $100\ \mathrm{W/m^2}$
  feedback: |-
    This uses a linear inverse ratio and forgets the square.
- id: d
  content: |-
    $400\ \mathrm{W/m^2}$
  feedback: |-
    Moving farther must lower the intensity, not double it.
- id: e
  content: |-
    $800\ \mathrm{W/m^2}$
  feedback: |-
    This reverses the distance ratio and squares it.
```

---

<a id="reverse-the-direction-when-moving-closer"></a>
## Reverse the Direction When Moving Closer

**Example:** A sound intensity is $50\ \mathrm{W/m^2}$ at $12\ \mathrm{m}$. What is the intensity at $6.0\ \mathrm{m}$?

**Explanation**

Moving closer makes $r_1/r_2$ greater than $1$, so the intensity must increase:

$$
\begin{aligned}
I_2
&=(50\ \mathrm{W/m^2})\left(\frac{12}{6.0}\right)^2 \\
&=(50\ \mathrm{W/m^2})(2)^2 \\
&=200\ \mathrm{W/m^2}.
\end{aligned}
$$

```quiz
type: radio
id: p3-scale-closer
content: |-
  A sound intensity is $30\ \mathrm{W/m^2}$ at $18\ \mathrm{m}$ from a speaker. What is the intensity at $6.0\ \mathrm{m}$?
options:
- id: a
  content: |-
    $3.3\ \mathrm{W/m^2}$
  feedback: |-
    This reverses the ratio even though moving closer must increase intensity.
- id: b
  content: |-
    $10\ \mathrm{W/m^2}$
  feedback: |-
    This uses the inverse ratio without squaring and predicts the wrong direction.
- id: c
  content: |-
    $90\ \mathrm{W/m^2}$
  feedback: |-
    This multiplies by the distance factor $3$ but does not square it.
- id: d
  content: |-
    $270\ \mathrm{W/m^2}$
  correct: true
  feedback: |-
    Correct. Moving three times closer multiplies intensity by $3^2=9$.
- id: e
  content: |-
    $810\ \mathrm{W/m^2}$
  feedback: |-
    This applies one extra factor of $3$.
```

---

<a id="square-the-entire-ratio"></a>
## Square the Entire Ratio

**Example:** A listener moves from $7.0\ \mathrm{m}$ to $21\ \mathrm{m}$ from the same speaker. If the initial intensity is $450\ \mathrm{W/m^2}$, find the new intensity.

**Explanation**

The listener moves three times as far away, so the intensity becomes $1/3^2=1/9$ as large:

$$
\begin{aligned}
I_2
&=(450\ \mathrm{W/m^2})\left(\frac{7.0}{21}\right)^2 \\
&=(450\ \mathrm{W/m^2})\left(\frac13\right)^2 \\
&=(450\ \mathrm{W/m^2})\left(\frac19\right) \\
&=50\ \mathrm{W/m^2}.
\end{aligned}
$$

Using only $1/3$ would apply an inverse law instead of an inverse-square law.

```quiz
type: radio
id: p3-square-ratio
content: |-
  A sound intensity is $80\ \mathrm{W/m^2}$ at $20\ \mathrm{m}$ from a speaker. What is the intensity at $10\ \mathrm{m}$?
options:
- id: a
  content: |-
    $20\ \mathrm{W/m^2}$
  feedback: |-
    This changes the intensity in the wrong direction when moving closer.
- id: b
  content: |-
    $40\ \mathrm{W/m^2}$
  feedback: |-
    This uses the reversed linear ratio.
- id: c
  content: |-
    $160\ \mathrm{W/m^2}$
  feedback: |-
    This uses the distance factor $2$ without squaring it.
- id: d
  content: |-
    $320\ \mathrm{W/m^2}$
  correct: true
  feedback: |-
    Correct. Halving the distance multiplies intensity by $2^2=4$.
- id: e
  content: |-
    $640\ \mathrm{W/m^2}$
  feedback: |-
    This multiplies by an extra factor of $2$ after squaring.
```

---

<a id="solve-the-given-speaker-problem"></a>
## Solve the Given Speaker Problem

**Example:** You are $12\ \mathrm{m}$ from a speaker and measure a sound intensity of $240\ \mathrm{W/m^2}$. You then move to $24\ \mathrm{m}$ from the speaker. What intensity do you measure?

**Explanation**

Label the old and new states before substituting:

| State | Distance | Intensity |
|---|---:|---:|
| initial | $r_1=12\ \mathrm{m}$ | $I_1=240\ \mathrm{W/m^2}$ |
| new | $r_2=24\ \mathrm{m}$ | $I_2=?$ |

The listener moves farther away, so predict that $I_2<I_1$. Then calculate:

$$
\begin{aligned}
I_2
&=I_1\left(\frac{r_1}{r_2}\right)^2 \\
&=(240\ \mathrm{W/m^2})\left(\frac{12}{24}\right)^2 \\
&=(240\ \mathrm{W/m^2})\left(\frac12\right)^2 \\
&=(240\ \mathrm{W/m^2})\left(\frac14\right) \\
&=60\ \mathrm{W/m^2}.
\end{aligned}
$$

The distance doubled, so the intensity should be one fourth as large; $60$ is indeed one fourth of $240$. To show two significant figures in polished notation, write $6.0\times10^1\ \mathrm{W/m^2}$. The source answer form is: **Enter the intensity in watts per square meter as a number only.** The correct entry is $60$.

```quiz
type: radio
id: p3-source-check
content: |-
  You are $12\ \mathrm{m}$ from a speaker and measure a sound intensity of $240\ \mathrm{W/m^2}$. You then move to $24\ \mathrm{m}$ from the speaker. What number should be entered for the measured intensity in watts per square meter?
options:
- id: a
  content: |-
    $60$
  correct: true
  feedback: |-
    Correct. The distance doubles, so the intensity becomes one fourth of $240\ \mathrm{W/m^2}$.
- id: b
  content: |-
    $120$
  feedback: |-
    This uses a linear inverse ratio and forgets to square $12/24$.
- id: c
  content: |-
    $240$
  feedback: |-
    This ignores the change in distance.
- id: d
  content: |-
    $480$
  feedback: |-
    This reverses the distance ratio without applying the square.
- id: e
  content: |-
    $960$
  feedback: |-
    This reverses the old-to-new distance ratio before squaring.
```

---

<a id="summary"></a>
## Summary

For the same point-like sound source:

1. **Predict:** moving farther lowers intensity; moving closer raises it.
2. **Label:** identify the known state $(I_1,r_1)$ and the new distance $r_2$.
3. **Scale:** compute $I_2=I_1(r_1/r_2)^2$, evaluating the ratio before the square.
4. **Verify:** the distance ratio is unitless, the result retains $\mathrm{W/m^2}$, and its direction agrees with the prediction.

If the listener moves farther away, the answer must be smaller. The main trap is forgetting the square and using a linear inverse ratio.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
