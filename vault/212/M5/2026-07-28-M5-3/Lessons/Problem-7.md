# Solving for the Speed of a Receding Sound Source

<!--
lesson-id: 212-M5-030
topic-code: MTH212.M5.30
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Receding-Source Formula](#choose-the-receding-source-formula)
- [Isolate the Source Speed](#isolate-the-source-speed)
- [Substitute a Frequency Ratio](#substitute-a-frequency-ratio)
- [Solve the Given Bat Problem](#solve-the-given-bat-problem)
- [Summary](#summary)

## Prerequisites

- Distinguish source frequency $f_0$ from observed frequency $f_{\mathrm{obs}}$.
- Solve a proportion and isolate a variable.
- Form a unitless ratio from frequencies expressed in the same units.
- Round a calculated value to the significant figures of the measured givens.

---

<a id="introduction"></a>
## Introduction

When a source moves away from a stationary observer, the observed frequency is lower than the emitted frequency. The moving-source Doppler formula is

$$
f_{\mathrm{obs}}=f_0\frac{v}{v+v_s},
$$

where $v$ is the speed of sound and $v_s$ is the source's speed away from the observer.

**Recognition cue:** The observer is stationary, the source is moving away, and the heard frequency satisfies $f_{\mathrm{obs}}<f_0$. Those three facts select the receding moving-source formula and make $v_s$ the target variable.

The reusable move is to recognize that the source is receding, place $v_s$ in the denominator with a plus sign, and isolate it:

$$
v_s=v\left(\frac{f_0}{f_{\mathrm{obs}}}-1\right).
$$

Because $f_{\mathrm{obs}}<f_0$ for a receding source, the ratio $f_0/f_{\mathrm{obs}}$ is greater than $1$, so this formula gives a positive speed.

---

<a id="choose-the-receding-source-formula"></a>
## Choose the Receding-Source Formula

**Example:** A stationary listener hears a moving source at a lower frequency than the source emits. Which sign belongs with $v_s$?

**Explanation**

Moving away stretches the wavefronts, so the observed frequency must decrease. Using $v+v_s$ makes the fraction less than $1$:

$$
\frac{v}{v+v_s}<1.
$$

Therefore,

$$
f_{\mathrm{obs}}=f_0\frac{v}{v+v_s}.
$$

```quiz
type: radio
id: p7-choose-formula
content: |-
  A source moves away from a stationary observer at speed $v_s$. Which formula correctly gives the observed frequency $f_{\mathrm{obs}}$?
options:
- id: a
  content: |-
    $f_{\mathrm{obs}}=f_0\dfrac{v}{v+v_s}$
  correct: true
  feedback: |-
    Correct. The larger denominator makes $f_{\mathrm{obs}}<f_0$, as required for a receding source.
- id: b
  content: |-
    $f_{\mathrm{obs}}=f_0\dfrac{v}{v-v_s}$
  feedback: |-
    Subtracting $v_s$ makes the observed frequency larger, which describes an approaching source.
- id: c
  content: |-
    $f_{\mathrm{obs}}=f_0\dfrac{v+v_s}{v}$
  feedback: |-
    This factor is greater than $1$, so it predicts the wrong direction of frequency shift.
- id: d
  content: |-
    $f_{\mathrm{obs}}=f_0\dfrac{v-v_s}{v}$
  feedback: |-
    For a moving source, its speed changes the denominator because it changes wavefront spacing.
- id: e
  content: |-
    $f_{\mathrm{obs}}=f_0+v_s$
  feedback: |-
    Frequency and speed have different units and cannot be added.
```

---

<a id="isolate-the-source-speed"></a>
## Isolate the Source Speed

**Example:** Solve $f_{\mathrm{obs}}=f_0\dfrac{v}{v+v_s}$ for $v_s$.

**Explanation**

Treat $f_{\mathrm{obs}}$, $f_0$, and $v$ as constants while isolating $v_s$. First clear the denominator by multiplying both sides by $v+v_s$:

$$
\begin{aligned}
f_{\mathrm{obs}}
&=f_0\frac{v}{v+v_s}, \\
f_{\mathrm{obs}}(v+v_s)
&=f_0v.
\end{aligned}
$$

Now distribute, subtract $f_{\mathrm{obs}}v$, and divide by $f_{\mathrm{obs}}$:

$$
\begin{aligned}
f_{\mathrm{obs}}v+f_{\mathrm{obs}}v_s
&=f_0v, \\
f_{\mathrm{obs}}v_s
&=f_0v-f_{\mathrm{obs}}v, \\
v_s
&=\frac{v(f_0-f_{\mathrm{obs}})}{f_{\mathrm{obs}}} \\
&=v\left(\frac{f_0}{f_{\mathrm{obs}}}-1\right).
\end{aligned}
$$

```quiz
type: radio
id: p7-isolate-source-speed
content: |-
  For a source moving away from a stationary observer, which expression correctly isolates the source speed $v_s$?
options:
- id: a
  content: |-
    $v_s=v\left(\dfrac{f_0}{f_{\mathrm{obs}}}-1\right)$
  correct: true
  feedback: |-
    Correct. Since $f_0/f_{\mathrm{obs}}>1$ for a receding source, this gives a positive source speed.
- id: b
  content: |-
    $v_s=v\left(\dfrac{f_{\mathrm{obs}}}{f_0}-1\right)$
  feedback: |-
    This reverses the frequency ratio and produces a negative speed.
- id: c
  content: |-
    $v_s=v\dfrac{f_0}{f_{\mathrm{obs}}}$
  feedback: |-
    This omits the subtraction of the sound speed after clearing the denominator.
- id: d
  content: |-
    $v_s=v\left(1-\dfrac{f_0}{f_{\mathrm{obs}}}\right)$
  feedback: |-
    This is the negative of the correctly isolated expression.
- id: e
  content: |-
    $v_s=\dfrac{f_0-f_{\mathrm{obs}}}{v}$
  feedback: |-
    Dividing frequency by speed does not produce units of speed.
```

---

<a id="substitute-a-frequency-ratio"></a>
## Substitute a Frequency Ratio

**Example:** A source emits $30\ \mathrm{kHz}$ while moving away from a stationary observer, who hears $24\ \mathrm{kHz}$. Use $v=340\ \mathrm{m}/\mathrm{s}$ to find the source speed.

**Explanation**

Both frequencies use kilohertz, so their units cancel in the ratio:

$$
\frac{f_0}{f_{\mathrm{obs}}}=\frac{30\ \mathrm{kHz}}{24\ \mathrm{kHz}}=1.25.
$$

Now substitute:

$$
\begin{aligned}
v_s
&=v\left(\frac{f_0}{f_{\mathrm{obs}}}-1\right) \\
&=(340\ \mathrm{m}/\mathrm{s})(1.25-1) \\
&=85\ \mathrm{m}/\mathrm{s}.
\end{aligned}
$$

```quiz
type: radio
id: p7-substitute-ratio
content: |-
  A source emits $24\ \mathrm{kHz}$ while moving away from a stationary observer, who hears $18\ \mathrm{kHz}$. Use $v=342\ \mathrm{m}/\mathrm{s}$. What is the source speed?
options:
- id: a
  content: |-
    $28.5\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    The Doppler equation requires the frequency ratio, not a calculation based only on their difference.
- id: b
  content: |-
    $85.5\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This is half the needed value; use the full factor $24/18-1=1/3$.
- id: c
  content: |-
    $114\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    Correct. $342(24/18-1)=342(1/3)=114\ \mathrm{m}/\mathrm{s}$.
- id: d
  content: |-
    $342\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This reports the speed of sound rather than the source speed.
- id: e
  content: |-
    $456\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This evaluates $v(f_0/f_{\mathrm{obs}})$ but omits the $-v$ required when isolating $v_s$.
```

---

<a id="solve-the-given-bat-problem"></a>
## Solve the Given Bat Problem

**Example:** A bat chirps at $25\ \mathrm{kHz}$ while flying away from you. How fast must it fly for you to hear $20\ \mathrm{kHz}$? The source does not specify a value for the speed of sound.

**Explanation**

Using $343\ \mathrm{m}/\mathrm{s}$ for the speed of sound, organize the quantities by role:

| Quantity | Value | Role |
|---|---:|---|
| emitted frequency | $f_0=25\ \mathrm{kHz}$ | numerator of the frequency ratio |
| observed frequency | $f_{\mathrm{obs}}=20\ \mathrm{kHz}$ | denominator of the frequency ratio |
| speed of sound | $v=343\ \mathrm{m}/\mathrm{s}$ | known propagation speed |
| bat speed | $v_s=?$ | target source speed |

Then

$$
\begin{aligned}
v_s
&=v\left(\frac{f_0}{f_{\mathrm{obs}}}-1\right) \\
&=(343\ \mathrm{m}/\mathrm{s})\left(\frac{25}{20}-1\right) \\
&=(343\ \mathrm{m}/\mathrm{s})(0.25) \\
&=85.75\ \mathrm{m}/\mathrm{s}.
\end{aligned}
$$

Back-substitution checks both the sign and the arithmetic:

$$
f_0\frac{v}{v+v_s}
=(25\ \mathrm{kHz})\frac{343}{343+85.75}
=20\ \mathrm{kHz}.
$$

The frequencies have two significant figures, so the result is $86\ \mathrm{m}/\mathrm{s}$. The source answer form is: **Using $343\ \mathrm{m}/\mathrm{s}$ for the speed of sound, the bat's speed in meters per second is a number-only entry.** The correct entry is $86$.

Because the original prompt does not specify the speed of sound, using $340\ \mathrm{m}/\mathrm{s}$ would instead give $85\ \mathrm{m}/\mathrm{s}$. The source therefore disables exact string grading.

```quiz
type: radio
id: p7-source-check
content: |-
  A bat chirps at $25\ \mathrm{kHz}$ while flying away from you. How fast must it fly for you to hear $20\ \mathrm{kHz}$? Using $343\ \mathrm{m}/\mathrm{s}$ for the speed of sound, which number-only entry gives the bat's speed in meters per second?
options:
- id: a
  content: |-
    $69$
  feedback: |-
    This uses the fractional frequency decrease $1-f_{\mathrm{obs}}/f_0$ instead of the isolated Doppler expression.
- id: b
  content: |-
    $85$
  feedback: |-
    This is the rounded result if $340\ \mathrm{m}/\mathrm{s}$ is assumed; the question explicitly asks you to use $343\ \mathrm{m}/\mathrm{s}$.
- id: c
  content: |-
    $86$
  correct: true
  feedback: |-
    Correct. The unrounded value is $85.75\ \mathrm{m}/\mathrm{s}$, which rounds to $86\ \mathrm{m}/\mathrm{s}$.
- id: d
  content: |-
    $343$
  feedback: |-
    This is the assumed speed of sound, not the bat's speed.
- id: e
  content: |-
    $429$
  feedback: |-
    This computes $v(f_0/f_{\mathrm{obs}})$ but forgets to subtract $v$.
```

---

<a id="summary"></a>
## Summary

For a source moving away from a stationary observer:

1. Check that $f_{\mathrm{obs}}<f_0$.
2. Use $f_{\mathrm{obs}}=f_0\dfrac{v}{v+v_s}$.
3. Isolate the source speed: $v_s=v\left(\dfrac{f_0}{f_{\mathrm{obs}}}-1\right)$.
4. Use the same units for $f_0$ and $f_{\mathrm{obs}}$ so their ratio is unitless.
5. State the chosen speed of sound, calculate without premature rounding, and round the final speed.

The main traps are using the approaching-source sign, reversing $f_0/f_{\mathrm{obs}}$, and confusing $v$ with $v_s$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
