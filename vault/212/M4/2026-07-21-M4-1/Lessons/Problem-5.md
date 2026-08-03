# Finding Angular Frequency From an Oscillation Graph

<!--
lesson-id: 212-M4-005
topic-code: MTH212.M4.05
-->

## Table of Contents

- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Read the Period From the Graph](#read-the-period-from-the-graph)
- [Convert Cycles to Radians](#convert-cycles-to-radians)
- [Measure Across Several Cycles](#measure-across-several-cycles)
- [Apply the Method to Problem 5](#apply-the-method-to-problem-5)
- [Summary](#summary)

## Prerequisites

- Read time coordinates from a position-time graph.
- Identify consecutive points at the same phase, such as two maxima.
- Know that one complete cycle corresponds to $2\pi$ radians.
- Round a final calculated value to the precision of the measured data.

---

<a id="introduction"></a>
## Introduction

**Recognition cue:** A position-time graph repeats, and the problem asks for the oscillator's angular frequency rather than its amplitude or ordinary frequency.

**Single move:** Measure one period $T$ between matching phase points, then convert cycles to radians with $\omega=2\pi/T$. If several cycles are measured, divide their total time span by the number of cycles before converting.

---

<a id="read-the-period-from-the-graph"></a>
## Read the Period From the Graph

**Recognition cue:** A position-time graph is given, but the requested quantity is angular frequency $\omega$.

First read the period $T$, the time for one full repeat. The cleanest method is to subtract the times of consecutive matching phase points:

$$
T=t_{\mathrm{next\ maximum}}-t_{\mathrm{maximum}}.
$$

Consecutive minima or same-direction equilibrium crossings also work.

The period is the **smallest positive** horizontal shift that reproduces the whole graph. A gap covering two or three cycles is a multiple of $T$, not the period itself.

**Example:** Consecutive maxima occur at $t=1.0\ \mathrm s$ and $t=4.0\ \mathrm s$. Therefore,

$$
T=4.0\ \mathrm s-1.0\ \mathrm s=3.0\ \mathrm s.
$$

**Explanation**

The period is a horizontal time interval. The graph's vertical amplitude is not used to find $T$ or $\omega$.

```quiz
type: radio
id: p5-read-period
content: |-
  Consecutive troughs of an oscillator occur at $t=0.5\ \mathrm s$ and $t=3.5\ \mathrm s$. What is the period?
options:
- id: p5-read-period-a
  content: |-
    $3.0\ \mathrm s$
  correct: true
  feedback: |-
    Consecutive troughs are one full cycle apart, so $T=3.5-0.5=3.0\ \mathrm s$. The value $1.5\ \mathrm s$ incorrectly halves an already complete cycle, while $0.33$ is a reciprocal rate.
- id: p5-read-period-b
  content: |-
    $4.0\ \mathrm s$
- id: p5-read-period-c
  content: |-
    $1.5\ \mathrm s$
- id: p5-read-period-d
  content: |-
    $0.33\ \mathrm s$
```

---

<a id="convert-cycles-to-radians"></a>
## Convert Cycles to Radians

Period, ordinary frequency, and angular frequency describe the same repetition in different units:

| Quantity | Meaning | Formula | Unit |
| --- | --- | --- | --- |
| $T$ | seconds per cycle | read from graph | $\mathrm s$ |
| $f$ | cycles per second | $f=1/T$ | $\mathrm{Hz}$ |
| $\omega$ | radians per second | $\omega=2\pi f=2\pi/T$ | $\mathrm{rad/s}$ |

The factor $2\pi$ appears because one full cycle is $2\pi$ radians.

For a sinusoidal position function

$$
x(t)=A\cos(\omega t+\phi),
$$

the coefficient of $t$ inside the angle is $\omega$. The graph repeats when the angle increases by $2\pi$, which gives

$$
\omega T=2\pi
\qquad\Longleftrightarrow\qquad
\omega=\frac{2\pi}{T}.
$$

**Example:** If $T=2.0\ \mathrm s$, then

$$
f=\frac1{2.0\ \mathrm s}=0.50\ \mathrm{Hz}
$$

but

$$
\omega=2\pi f=\frac{2\pi}{2.0\ \mathrm s}=3.14\ldots\ \mathrm{rad/s}.
$$

**Explanation**

Do not report $f$ when the question asks for $\omega$.

```quiz
type: radio
id: p5-convert-angular-frequency
content: |-
  An oscillator has period $T=5.0\ \mathrm s$. What is its angular frequency?
options:
- id: p5-convert-angular-frequency-a
  content: |-
    $1.26\ \mathrm{rad/s}$
  correct: true
  feedback: |-
    Use $\omega=2\pi/T$: $2\pi/(5.0\ \mathrm s)=1.26\ \mathrm{rad/s}$. The value $0.20$ is the ordinary frequency $f=1/T$ in hertz, before converting cycles to radians.
- id: p5-convert-angular-frequency-b
  content: |-
    $0.20\ \mathrm{rad/s}$
- id: p5-convert-angular-frequency-c
  content: |-
    $5.0\ \mathrm{rad/s}$
- id: p5-convert-angular-frequency-d
  content: |-
    $31.4\ \mathrm{rad/s}$
```

---

<a id="measure-across-several-cycles"></a>
## Measure Across Several Cycles

If several repeats are visible, measure a longer time span and divide by the number of complete cycles:

$$
T=\frac{t_{\mathrm{last}}-t_{\mathrm{first}}}{N_{\mathrm{cycles}}},
\qquad
\omega=\frac{2\pi}{T}.
$$

This reduces the effect of small coordinate-reading errors.

**Example:** A maximum at $t=1\ \mathrm s$ and another at $t=13\ \mathrm s$ are separated by three complete cycles. Then

$$
T=\frac{13\ \mathrm s-1\ \mathrm s}{3}=4.0\ \mathrm s
$$

and

$$
\omega=\frac{2\pi}{4.0\ \mathrm s}=1.57\ldots\ \mathrm{rad/s}.
$$

**Explanation**

Count cycle gaps between matching landmarks, then convert the period to radians per second.

```quiz
type: radio
id: p5-multiple-cycles
content: |-
  Two maxima at $t=2\ \mathrm s$ and $t=12\ \mathrm s$ are separated by five complete cycles. What is the angular frequency?
options:
- id: p5-multiple-cycles-a
  content: |-
    $3.14\ \mathrm{rad/s}$
  correct: true
  feedback: |-
    Five cycles take $12-2=10\ \mathrm s$, so $T=10/5=2.0\ \mathrm s$. Then $\omega=2\pi/2.0=3.14\ \mathrm{rad/s}$. The value $0.50$ is ordinary frequency, not angular frequency.
- id: p5-multiple-cycles-b
  content: |-
    $0.50\ \mathrm{rad/s}$
- id: p5-multiple-cycles-c
  content: |-
    $0.20\ \mathrm{rad/s}$
- id: p5-multiple-cycles-d
  content: |-
    $0.63\ \mathrm{rad/s}$
```

---

<a id="apply-the-method-to-problem-5"></a>
## Apply the Method to Problem 5

**Example:** The graph shows the position of a simple harmonic oscillator. What is its angular frequency $\omega$?

![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

**Explanation**

Consecutive maxima occur at $t=0$, $4.0\ \mathrm s$, and $8.0\ \mathrm s$, so

$$
T=4.0\ \mathrm s.
$$

Now convert one cycle per period into radians per second:

$$
\omega=\frac{2\pi}{T}
=\frac{2\pi}{4.0\ \mathrm{s}}
=1.5708\ldots\ \mathrm{rad/s}.
$$

As a unit-rate chain,

$$
\omega
=\left(\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{cycle}}\right)
\left(\frac{1\ \mathrm{cycle}}{4.0\ \mathrm s}\right)
=\frac{\pi}{2}\ \mathrm{rad/s}.
$$

The cycle units cancel, leaving the requested radians per second.

The period supports two significant figures, so $\omega=1.6\ \mathrm{rad/s}$.

The requested answer form is: **Enter the angular frequency in radians per second as a number only.** Enter **1.6**.

```quiz
type: radio
id: p5-source-check
content: |-
  **Question 4**

  The graph shows the position of a simple harmonic oscillator. What is its angular frequency $\omega$?

  ![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

  Enter the angular frequency in radians per second as a number only.
options:
- id: p5-source-check-a
  content: |-
    1.6
  correct: true
  feedback: |-
    With $T=4.0\ \mathrm{s}$,

    $$
    \omega=\frac{2\pi}{T}=\frac{2\pi}{4.0\ \mathrm{s}}=1.5708\ldots\ \mathrm{rad/s}.
    $$

    The period supports two significant figures, so $\omega=1.6\ \mathrm{rad/s}$.

    The value `0.25` is the ordinary frequency $f=1/T$ in hertz; `4.0` is the period in seconds; and `6.3` multiplies by $2\pi$ instead of dividing by the period.
- id: p5-source-check-b
  content: |-
    0.25
- id: p5-source-check-c
  content: |-
    4.0
- id: p5-source-check-d
  content: |-
    6.3
```

---

## Summary

1. Read one full repeat from matching phase points to obtain $T$.
2. Convert to ordinary frequency only if useful: $f=1/T$.
3. Convert cycles to radians: $\omega=(2\pi\ \mathrm{rad/cycle})f=2\pi/T$.
4. Check that angular frequency is reported in $\mathrm{rad/s}$, not seconds or hertz.
5. Keep calculator digits until the final rounding step.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
