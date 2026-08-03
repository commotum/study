# Finding Frequency from Adjacent Antinode Spacing

<!--
lesson-id: 212-M5-043
topic-code: MTH212.M5.43
-->

## Table of Contents

- [Introduction](#introduction)
- [Turn Antinode Spacing into Wavelength](#turn-antinode-spacing-into-wavelength)
- [Use Wave Speed to Find Frequency](#use-wave-speed-to-find-frequency)
- [Keep the Length Units Consistent](#keep-the-length-units-consistent)
- [Avoid the Half-Wavelength Trap](#avoid-the-half-wavelength-trap)
- [Summary](#summary)

## Prerequisites

- Recognize wavelength $\lambda$ as the distance between repeating points on a wave.
- Use the wave-speed relation $v=f\lambda$ and solve it as $f=v/\lambda$.
- Divide quantities whose length units match.

---

<a id="introduction"></a>
## Introduction

When a standing-wave problem gives the distance $d$ between **adjacent antinodes**, that distance is only half of a wavelength:

$$
d=\frac{\lambda}{2}.
$$

One full wavelength spans two adjacent-antinode gaps, so

$$
\lambda=2d.
$$

After finding the full wavelength, use $v=f\lambda$ to find the frequency:

$$
f=\frac{v}{\lambda}
=\frac{v}{2d}.
$$

The recognition cue is the phrase **adjacent antinodes**. The essential move is to double their separation before dividing the wave speed by a wavelength.

At a fixed wave speed, a larger antinode spacing means a larger wavelength and therefore a lower frequency. This direction gives a useful check on the final result.

---

<a id="turn-antinode-spacing-into-wavelength"></a>
## Turn Antinode Spacing into Wavelength

**Example:** Adjacent antinodes of a standing wave are $15\ \mathrm{cm}$ apart. Find the wavelength.

**Explanation**

The given spacing is $d=15\ \mathrm{cm}$. Because adjacent antinodes are separated by $\lambda/2$,

$$
\lambda=2d=2(15\ \mathrm{cm})=30\ \mathrm{cm}.
$$

```quiz
type: radio
id: p3-antinode-spacing-q1
content: |-
  Adjacent antinodes of a standing wave are $18\ \mathrm{cm}$ apart. What is the wavelength?
options:
- id: p3-antinode-spacing-q1-a
  content: |-
    $9\ \mathrm{cm}$
- id: p3-antinode-spacing-q1-b
  content: |-
    $18\ \mathrm{cm}$
- id: p3-antinode-spacing-q1-c
  content: |-
    $36\ \mathrm{cm}$
  correct: true
- id: p3-antinode-spacing-q1-d
  content: |-
    $54\ \mathrm{cm}$
- id: p3-antinode-spacing-q1-e
  content: |-
    $72\ \mathrm{cm}$
```

---

<a id="use-wave-speed-to-find-frequency"></a>
## Use Wave Speed to Find Frequency

**Example:** Adjacent antinodes are $25\ \mathrm{cm}$ apart, and the traveling waves move at $150\ \mathrm{cm/s}$. Find the vibration frequency.

**Explanation**

First convert the adjacent-antinode spacing to a full wavelength:

$$
\lambda=2d=2(25\ \mathrm{cm})=50\ \mathrm{cm}.
$$

Then use $f=v/\lambda$:

$$
f=\frac{150\ \mathrm{cm/s}}{50\ \mathrm{cm}}
=3\ \mathrm{s}^{-1}
=3\ \mathrm{Hz}.
$$

Writing the formula before substituting keeps the target quantity clear. The centimeters then cancel, leaving inverse seconds, which is hertz.

```quiz
type: radio
id: p3-wave-frequency-q1
content: |-
  Adjacent antinodes are $30\ \mathrm{cm}$ apart, and the waves forming the standing wave travel at $240\ \mathrm{cm/s}$. What is the vibration frequency?
options:
- id: p3-wave-frequency-q1-a
  content: |-
    $2\ \mathrm{Hz}$
- id: p3-wave-frequency-q1-b
  content: |-
    $4\ \mathrm{Hz}$
  correct: true
- id: p3-wave-frequency-q1-c
  content: |-
    $8\ \mathrm{Hz}$
- id: p3-wave-frequency-q1-d
  content: |-
    $30\ \mathrm{Hz}$
- id: p3-wave-frequency-q1-e
  content: |-
    $60\ \mathrm{Hz}$
```

---

<a id="keep-the-length-units-consistent"></a>
## Keep the Length Units Consistent

**Example:** Adjacent antinodes are $0.30\ \mathrm{m}$ apart, and the wave speed is $120\ \mathrm{cm/s}$. Find the vibration frequency.

**Explanation**

The speed uses centimeters, so first convert the spacing:

$$
d=0.30\ \mathrm{m}=30\ \mathrm{cm}.
$$

Now find the full wavelength and then the frequency:

$$
\lambda=2d=60\ \mathrm{cm},
$$

$$
f=\frac{v}{\lambda}
=\frac{120\ \mathrm{cm/s}}{60\ \mathrm{cm}}
=2\ \mathrm{Hz}.
$$

Do not divide numerical values expressed in different length units.

```quiz
type: radio
id: p3-consistent-units-q1
content: |-
  Adjacent antinodes are $0.25\ \mathrm{m}$ apart, and the wave speed is $150\ \mathrm{cm/s}$. What is the vibration frequency?
options:
- id: p3-consistent-units-q1-a
  content: |-
    $0.75\ \mathrm{Hz}$
- id: p3-consistent-units-q1-b
  content: |-
    $1.5\ \mathrm{Hz}$
- id: p3-consistent-units-q1-c
  content: |-
    $3\ \mathrm{Hz}$
  correct: true
- id: p3-consistent-units-q1-d
  content: |-
    $6\ \mathrm{Hz}$
- id: p3-consistent-units-q1-e
  content: |-
    $300\ \mathrm{Hz}$
```

---

<a id="avoid-the-half-wavelength-trap"></a>
## Avoid the Half-Wavelength Trap

**Example:** Adjacent antinodes are $10\ \mathrm{cm}$ apart, and the wave speed is $80\ \mathrm{cm/s}$. A student calculates $80/10=8\ \mathrm{Hz}$. Explain and correct the mistake.

**Explanation**

The student treated the adjacent-antinode spacing as a full wavelength. It is actually half a wavelength:

$$
\lambda=2(10\ \mathrm{cm})=20\ \mathrm{cm}.
$$

Therefore,

$$
f=\frac{80\ \mathrm{cm/s}}{20\ \mathrm{cm}}
=4\ \mathrm{Hz}.
$$

Using $v/d$ instead of $v/(2d)$ makes the frequency twice as large as it should be.

A quick check reaches the same conclusion: because $\lambda=2d$, the correct frequency must be half of $v/d$. Here, $v/d=8\ \mathrm{Hz}$, so the frequency must be $4\ \mathrm{Hz}$.

```quiz
type: radio
id: p3-homework-q1
shuffle: true
content: |-
  For a standing wave mode on a string fixed at both ends, adjacent antinodes are separated by a distance of $20\ \mathrm{cm}$.

  If the waves constituting the standing wave travel on this string with a speed of $100\ \mathrm{cm/s}$, at what frequency is the string being vibrated?
options:
- id: p3-homework-q1-a
  content: |-
    $1\ \mathrm{Hz}$
- id: p3-homework-q1-b
  content: |-
    $2.5\ \mathrm{Hz}$
  correct: true
- id: p3-homework-q1-c
  content: |-
    $8\ \mathrm{Hz}$
- id: p3-homework-q1-d
  content: |-
    $20\ \mathrm{Hz}$
```

---

<a id="summary"></a>
## Summary

**Recognition cue:** The problem gives the separation $d$ between adjacent antinodes and asks for the frequency.

**Rule:**

$$
d=\frac{\lambda}{2}
\qquad\Longrightarrow\qquad
\lambda=2d,
$$

so

$$
\boxed{f=\frac{v}{2d}}.
$$

**Procedure:**

1. Double the adjacent-antinode separation to get the full wavelength.
2. Make sure the speed and wavelength use the same length unit.
3. Divide the wave speed by the full wavelength.
4. Report the result in hertz, where $\mathrm{Hz}=\mathrm{s}^{-1}$.
5. Check that the result is half of $v/d$; at fixed speed, a larger spacing should give a lower frequency.

**Main trap:** Adjacent antinodes are half a wavelength apart, not one full wavelength apart.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
