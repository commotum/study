# Finding the Fundamental Frequency from a Harmonic

<!--
lesson-id: 212-M5-041
topic-code: MTH212.M5.41
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Harmonic Number as a Multiplier](#read-the-harmonic-number-as-a-multiplier)
- [Recover the Fundamental by Dividing](#recover-the-fundamental-by-dividing)
- [Check the Direction of the Scaling](#check-the-direction-of-the-scaling)
- [Summary](#summary)

## Prerequisites

- Interpret frequency in hertz, where $1\ \mathrm{Hz}$ means one cycle per second.
- Multiply and divide positive numbers.

---

<a id="introduction"></a>
## Introduction

When a problem names an air-column resonance as the **$m$th harmonic**, the harmonic frequency $f_m$ is $m$ times the fundamental frequency $f_1$:

$$
f_m=mf_1.
$$

The fundamental is the first harmonic, so it corresponds to $m=1$. Higher harmonics have higher frequencies.

| Resonance | Harmonic number | Frequency |
| --- | ---: | ---: |
| Fundamental | $1$ | $f_1$ |
| Second harmonic | $2$ | $2f_1$ |
| Fourth harmonic | $4$ | $4f_1$ |
| $m$th harmonic | $m$ | $mf_1$ |

When the higher-harmonic frequency is known and the fundamental is requested, solve backward:

$$
\boxed{f_1=\frac{f_m}{m}}.
$$

---

<a id="read-the-harmonic-number-as-a-multiplier"></a>
## Read the Harmonic Number as a Multiplier

**Example:** An air column has a fundamental frequency of $45\ \mathrm{Hz}$. What is its fifth-harmonic frequency?

**Explanation**

The phrase **fifth harmonic** gives the multiplier $m=5$. Substitute into $f_m=mf_1$:

$$
f_5=5f_1=5(45\ \mathrm{Hz})=225\ \mathrm{Hz}.
$$

The harmonic number multiplies the fundamental frequency.

```quiz
type: radio
id: p1-harmonic-multiplier-q1
content: |-
  An air column has a fundamental frequency of $30\ \mathrm{Hz}$. What is its third-harmonic frequency?
options:
- id: p1-harmonic-multiplier-q1-a
  content: |-
    $10\ \mathrm{Hz}$
- id: p1-harmonic-multiplier-q1-b
  content: |-
    $30\ \mathrm{Hz}$
- id: p1-harmonic-multiplier-q1-c
  content: |-
    $60\ \mathrm{Hz}$
- id: p1-harmonic-multiplier-q1-d
  content: |-
    $90\ \mathrm{Hz}$
  correct: true
- id: p1-harmonic-multiplier-q1-e
  content: |-
    $120\ \mathrm{Hz}$
```

---

<a id="recover-the-fundamental-by-dividing"></a>
## Recover the Fundamental by Dividing

**Example:** An air column resonates at $300\ \mathrm{Hz}$ in its fifth harmonic. Find its fundamental frequency.

**Explanation**

The known frequency is $f_5=300\ \mathrm{Hz}$, and the harmonic number is $m=5$. Write the harmonic relation:

$$
f_5=5f_1.
$$

Now divide by the harmonic number:

$$
f_1=\frac{f_5}{5}
=\frac{300\ \mathrm{Hz}}{5}
=60\ \mathrm{Hz}.
$$

```quiz
type: radio
id: p1-recover-fundamental-q1
content: |-
  An air column resonates at $360\ \mathrm{Hz}$ in its sixth harmonic. What is its fundamental frequency?
options:
- id: p1-recover-fundamental-q1-a
  content: |-
    $45\ \mathrm{Hz}$
- id: p1-recover-fundamental-q1-b
  content: |-
    $60\ \mathrm{Hz}$
  correct: true
- id: p1-recover-fundamental-q1-c
  content: |-
    $72\ \mathrm{Hz}$
- id: p1-recover-fundamental-q1-d
  content: |-
    $360\ \mathrm{Hz}$
- id: p1-recover-fundamental-q1-e
  content: |-
    $2160\ \mathrm{Hz}$
```

---

<a id="check-the-direction-of-the-scaling"></a>
## Check the Direction of the Scaling

**Example:** An air column's seventh harmonic has frequency $350\ \mathrm{Hz}$. A student multiplies by $7$ and reports the fundamental as $2450\ \mathrm{Hz}$. What went wrong?

**Explanation**

The seventh harmonic is already seven times the fundamental:

$$
f_7=7f_1.
$$

Therefore, finding the smaller fundamental requires division, not multiplication:

$$
f_1=\frac{350\ \mathrm{Hz}}{7}=50\ \mathrm{Hz}.
$$

Two quick checks confirm the direction:

1. The fundamental must be lower than a higher harmonic.
2. Rebuilding the given harmonic gives $7(50\ \mathrm{Hz})=350\ \mathrm{Hz}$.

```quiz
type: radio
id: p1-homework-q1
shuffle: true
content: |-
  When a speaker creating a sinusoidal sound wave of frequency $100\ \mathrm{Hz}$ is placed near the open end of a column of air, the air column resonates at its 4th harmonic.

  What frequency should the speaker play if instead we wanted the column to vibrate at its fundamental frequency?
options:
- id: p1-homework-q1-a
  content: |-
    $25\ \mathrm{Hz}$
  correct: true
- id: p1-homework-q1-b
  content: |-
    $100\ \mathrm{Hz}$
- id: p1-homework-q1-c
  content: |-
    $300\ \mathrm{Hz}$
- id: p1-homework-q1-d
  content: |-
    $400\ \mathrm{Hz}$
```

---

<a id="summary"></a>
## Summary

**Recognition cue:** A problem gives an $m$th-harmonic frequency and asks for the fundamental frequency.

**Rule:**

$$
f_m=mf_1
\qquad\Longrightarrow\qquad
f_1=\frac{f_m}{m}.
$$

**Procedure:**

1. Read the harmonic number as the multiplier $m$.
2. Divide the given harmonic frequency by $m$.
3. Keep the frequency unit, usually hertz.
4. Check that the fundamental is lower than the higher harmonic and that $mf_1$ rebuilds the given frequency.

**Main trap:** Multiplying by $m$ moves from the fundamental to the $m$th harmonic. To move backward from the $m$th harmonic to the fundamental, divide by $m$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
