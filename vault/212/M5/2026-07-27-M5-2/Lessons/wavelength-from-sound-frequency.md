# Wavelength from Sound Frequency

<!--
lesson-id: 212-M5-053
topic-code: MTH212.M5.53
-->

## Table of Contents

- [Introduction](#introduction)
- [Connect Speed, Frequency, and Wavelength](#connect-speed-frequency-and-wavelength)
- [Divide Before Substituting](#divide-before-substituting)
- [Check Units and Frequency Changes](#check-units-and-frequency-changes)
- [Match the Source Problem](#match-the-source-problem)
- [Summary](#summary)

## Prerequisites

- Interpret frequency in hertz, where $1\ \mathrm{Hz}=1\ \mathrm{s}^{-1}$.
- Divide positive quantities and track units through a calculation.
- Recognize $v$ as wave speed, $f$ as frequency, and $\lambda$ as wavelength.

---

<a id="introduction"></a>
## Introduction

When a problem gives a wave's speed and frequency and asks for its wavelength, begin with

$$
v=f\lambda.
$$

The requested quantity, $\lambda$, is the **subject** to isolate. Treat the given $v$ and $f$ as fixed quantities. Because a physical frequency is positive, $f\ne 0$, so dividing both sides by $f$ is valid:

$$
\boxed{\lambda=\frac{v}{f}}.
$$

This division has a physical meaning. At a fixed wave speed, the product $f\lambda=v$ stays constant. More wave cycles passing each second therefore means each cycle occupies less distance, so a higher frequency gives a shorter wavelength.

---

<a id="connect-speed-frequency-and-wavelength"></a>
## Connect Speed, Frequency, and Wavelength

**Example:** A wave travels at speed $v$ and has frequency $f$. Which expression gives its wavelength?

**Explanation**

The relation $v=f\lambda$ says that speed equals cycles per second times distance per cycle. To make $\lambda$ the subject, treat $v$ and $f$ as known and undo multiplication by $f$ with division:

$$
\lambda=\frac{v}{f}.
$$

```quiz
type: radio
id: wavelength-rearrange-relation
content: |-
  A sound wave travels at speed $v$ and has frequency $f$. Which expression gives its wavelength $\lambda$?
options:
- id: wavelength-rearrange-v-over-f
  content: |-
    $\displaystyle \lambda=\frac{v}{f}$
  correct: true
  feedback: |-
    Wave speed is $v=f\lambda$. Dividing by the frequency isolates the distance per cycle, so $\lambda=v/f$.
- id: wavelength-rearrange-f-over-v
  content: |-
    $\displaystyle \lambda=\frac{f}{v}$
  feedback: |-
    This reverses the required quotient. Dividing $v=f\lambda$ by $f$, rather than by $v$, gives $\lambda=v/f$; moreover, $f/v$ has units of inverse length.
- id: wavelength-rearrange-v-times-f
  content: |-
    $\lambda=vf$
  feedback: |-
    Multiplication does not isolate $\lambda$ from $v=f\lambda$. Since $f$ multiplies $\lambda$, undo that multiplication by dividing the speed by $f$.
- id: wavelength-rearrange-root
  content: |-
    $\displaystyle \lambda=\sqrt{\frac{v}{f}}$
  feedback: |-
    No wavelength is squared in $v=f\lambda$, so taking a square root introduces an operation the relation does not contain. One division gives $\lambda=v/f$.
```

---

<a id="divide-before-substituting"></a>
## Divide Before Substituting

**Example:** A sound wave travels at $330\ \mathrm{m/s}$ and has frequency $30\ \mathrm{Hz}$. Find its wavelength.

**Explanation**

First isolate wavelength, then substitute:

$$
\lambda=\frac{v}{f}
=\frac{330\ \mathrm{m/s}}{30\ \mathrm{Hz}}
=11\ \mathrm m.
$$

Writing the symbolic quotient first makes it harder to accidentally multiply the two givens or reverse their order.

```quiz
type: radio
id: wavelength-numerical-division
content: |-
  A sound wave travels at $340\ \mathrm{m/s}$ and has frequency $40\ \mathrm{Hz}$. What is its wavelength?
options:
- id: wavelength-numerical-8-5
  content: |-
    $8.5\ \mathrm m$
  correct: true
  feedback: |-
    Wavelength is wave speed divided by frequency. Substituting gives $\lambda=(340\ \mathrm{m/s})/(40\ \mathrm{Hz})=8.5\ \mathrm m$.
- id: wavelength-numerical-13600
  content: |-
    $13{,}600\ \mathrm m$
  feedback: |-
    This multiplies $340$ by $40$, but frequency multiplies wavelength in $v=f\lambda$ and must be divided out. The required calculation is $340/40=8.5\ \mathrm m$.
- id: wavelength-numerical-0-118
  content: |-
    $0.118\ \mathrm m$
  feedback: |-
    This comes from reversing the quotient to $f/v$. Wavelength is distance per cycle, so divide speed by cycles per second: $v/f=340/40=8.5\ \mathrm m$.
- id: wavelength-numerical-380
  content: |-
    $380\ \mathrm m$
  feedback: |-
    Adding speed and frequency mixes unlike quantities and does not follow $v=f\lambda$. Isolate wavelength by division, giving $340/40=8.5\ \mathrm m$.
```

---

<a id="check-units-and-frequency-changes"></a>
## Check Units and Frequency Changes

A unit check substitutes the unit of each quantity into the same quotient. Because hertz means inverse seconds,

$$
[\lambda]
=\frac{[v]}{[f]}
=\frac{\mathrm{m/s}}{\mathrm{s}^{-1}}
=\mathrm m.
$$

The reversed quotient $f/v$ would have units of $1/\mathrm m$, so it cannot be a wavelength. With $v$ fixed, the equivalent forms

$$
f\lambda=v
\qquad\text{and}\qquad
\lambda\propto\frac{1}{f}
$$

show the inverse relationship directly. If $f$ is multiplied by a factor, $\lambda$ is divided by that same factor.

**Example:** A wave has wavelength $3.0\ \mathrm m$. Its frequency doubles while its speed stays constant. The new wavelength is $3.0\ \mathrm m/2=1.5\ \mathrm m$.

```quiz
type: radio
id: wavelength-inverse-frequency
content: |-
  A sound wave has wavelength $2.0\ \mathrm m$. Its frequency triples while the wave speed stays constant. What is its new wavelength?
options:
- id: wavelength-inverse-two-thirds
  content: |-
    $\displaystyle \frac{2.0}{3}\ \mathrm m$
  correct: true
  feedback: |-
    At fixed wave speed, $\lambda=v/f$, so wavelength varies inversely with frequency. Tripling $f$ divides the original wavelength by $3$, giving $2.0/3\ \mathrm m$.
- id: wavelength-inverse-six
  content: |-
    $6.0\ \mathrm m$
  feedback: |-
    This treats wavelength as directly proportional to frequency. At fixed speed their product $f\lambda$ must remain constant, so tripling $f$ makes $\lambda$ one-third as large, not three times as large.
- id: wavelength-inverse-two
  content: |-
    $2.0\ \mathrm m$
  feedback: |-
    The wavelength would stay $2.0\ \mathrm m$ only if the frequency did not change or if the speed changed by the same factor. With fixed speed and triple frequency, $\lambda$ becomes $2.0/3\ \mathrm m$.
- id: wavelength-inverse-one-third
  content: |-
    $\displaystyle \frac{1}{3}\ \mathrm m$
  feedback: |-
    The factor $1/3$ describes how the wavelength changes, not its final value. Apply that factor to the original $2.0\ \mathrm m$: $(1/3)(2.0\ \mathrm m)=2.0/3\ \mathrm m$.
```

---

<a id="match-the-source-problem"></a>
## Match the Source Problem

Use the same sequence on the original numbers: write $\lambda=v/f$, substitute the sound speed and frequency with their units, then report the requested numerical entry in meters.

```quiz
type: radio
id: khadley-sound-waves-q1
content: |-
  **Question 1**

  Using $v_{\mathrm{sound}}=343\ \mathrm{m/s}$, find the wavelength of a $20\ \mathrm{Hz}$ sound. Enter meters:
options:
- id: khadley-sound-waves-q1-17
  content: |-
    $17$
  correct: true
  feedback: |-
    The wave relation gives $\lambda=v/f=(343\ \mathrm{m/s})/(20\ \mathrm{Hz})=17.15\ \mathrm m$, which rounds to the requested entry $17$ meters.
- id: khadley-sound-waves-q1-6860
  content: |-
    $6860$
  feedback: |-
    This multiplies $343$ by $20$, but $f$ must be divided out of $v=f\lambda$. Multiplication also gives units of $\mathrm{m/s^2}$ rather than meters; use $343/20$.
- id: khadley-sound-waves-q1-0-058
  content: |-
    $0.058$
  feedback: |-
    This reverses the quotient to $f/v$, whose units are inverse meters. Wavelength is speed divided by frequency, so compute $343/20=17.15\ \mathrm m$ and enter $17$.
- id: khadley-sound-waves-q1-0-017
  content: |-
    $0.017$
  feedback: |-
    This treats the stated $20\ \mathrm{Hz}$ as though it were $20\ \mathrm{kHz}$. No prefix conversion is needed: use $f=20\ \mathrm{Hz}$ in $\lambda=v/f$ to obtain about $17\ \mathrm m$.
```

---

<a id="summary"></a>
## Summary

- Cue: wave speed and frequency are known, and wavelength is the subject to isolate.
- Procedure: write $v=f\lambda$, divide by the nonzero frequency, and then substitute into $\lambda=v/f$.
- Unit check: $(\mathrm{m/s})/(\mathrm{s}^{-1})=\mathrm m$; the reversed quotient does not produce length.
- Trend check: at fixed speed, $f\lambda$ is constant, so frequency and wavelength vary inversely.
- Main trap: do not multiply the givens or reverse their order; speed must be divided by frequency.
