# Convert Rotation Frequency to Angular Speed

<!--
lesson-id: 212-M1-033
topic-code: MTH212.M1.33
-->

## Table of Contents

- [Introduction](#introduction)
- [One Revolution Is \(2\pi\) Radians](#one-revolution-is-2pi-radians)
- [Convert A Rotation Rate](#convert-a-rotation-rate)
- [Round The Angular Speed](#round-the-angular-frequency)
- [Avoid Leaving Revolutions In The Answer](#avoid-leaving-revolutions-in-the-answer)
- [Summary](#summary)

## Prerequisites

- Know that one full revolution is \(2\pi\) radians.
- Know how to multiply by a unit conversion factor.
- Know how to round a number to a given number of significant figures.

---

<a id="introduction"></a>
## Introduction

Rotation frequency $f$ counts revolutions per second. Angular speed $\omega$ measures the angle swept out per unit time:

$$
\omega=\frac{\text{angle swept out}}{\text{time}}.
$$

The two rates are related by

$$
\omega=2\pi f.
$$

When a problem gives $f$ in revolutions per second but asks for $\omega$ in radians per second, convert the angle unit from revolutions to radians.

The cue is the mismatch between the given unit and the requested unit:

$$
\mathrm{rev}/\mathrm{s} \quad \longrightarrow \quad \mathrm{rad}/\mathrm{s}
$$

Use the conversion

$$
1\ \mathrm{rev}=2\pi\ \mathrm{rad}
$$

The given rate has \(\mathrm{rev}\) in the numerator, so put \(\mathrm{rev}\) in the denominator of the conversion factor:

$$
\omega=f\left(\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}\right).
$$

---

<a id="one-revolution-is-2pi-radians"></a>
## One Revolution Is \(2\pi\) Radians

**Example:** Convert \(4\) revolutions to radians.

**Explanation**

One revolution is one full turn around a circle, and one full turn has angle \(2\pi\) radians.

$$
4\ \mathrm{rev}\cdot \frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}=8\pi\ \mathrm{rad}
$$

The revolution units cancel, leaving radians.

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  Convert \(6\) revolutions to radians.
options:
- id: q1-a
  content: |-
    \(6\pi\ \mathrm{rad}\)
- id: q1-b
  content: |-
    \(12\pi\ \mathrm{rad}\)
  correct: true
- id: q1-c
  content: |-
    \(3\pi\ \mathrm{rad}\)
- id: q1-d
  content: |-
    \(6\ \mathrm{rad}\)
```

---

<a id="convert-a-rotation-rate"></a>
## Convert A Rotation Rate

**Example:** A wheel spins with frequency $f=5$ revolutions per second. Find its angular speed in radians per second.

**Explanation**

Keep the "per second" part and convert only the revolution part.

$$
\omega=5\ \mathrm{rev}/\mathrm{s}\cdot \frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
$$

Cancel \(\mathrm{rev}\):

$$
\omega=10\pi\ \mathrm{rad}/\mathrm{s}
$$

So a frequency of $5$ revolutions per second corresponds to angular speed $\omega=10\pi\ \mathrm{rad}/\mathrm{s}$.

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  A disk spins with frequency $f=9$ revolutions per second. What is its angular speed?
options:
- id: q2-a
  content: |-
    \(9\pi\ \mathrm{rad}/\mathrm{s}\)
- id: q2-b
  content: |-
    \(18\pi\ \mathrm{rad}/\mathrm{s}\)
  correct: true
- id: q2-c
  content: |-
    \(\frac{9}{2\pi}\ \mathrm{rad}/\mathrm{s}\)
- id: q2-d
  content: |-
    \(9\ \mathrm{rad}/\mathrm{s}\)
```

---

<a id="round-the-angular-frequency"></a>
## Round The Angular Speed

**Example:** A wheel spins with frequency $f=14$ revolutions per second. What is its angular speed $\omega$ in radians per second? Give the answer to $2$ significant figures.

**Explanation**

First convert exactly:

$$
\omega=14\ \mathrm{rev}/\mathrm{s}\cdot \frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
=28\pi\ \mathrm{rad}/\mathrm{s}
$$

Then approximate. Keep \(2\pi\) until this step so the final rounding uses the full conversion factor.

$$
28\pi\approx 87.96
$$

To \(2\) significant figures,

$$
\omega\approx 88\ \mathrm{rad}/\mathrm{s}.
$$

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  A fan spins with frequency $f=11$ revolutions per second. What is its angular speed in radians per second, rounded to $2$ significant figures?
options:
- id: q3-a
  content: |-
    \(35\ \mathrm{rad}/\mathrm{s}\)
- id: q3-b
  content: |-
    \(69\ \mathrm{rad}/\mathrm{s}\)
  correct: true
- id: q3-c
  content: |-
    \(11\ \mathrm{rad}/\mathrm{s}\)
- id: q3-d
  content: |-
    \(66\ \mathrm{rad}/\mathrm{s}\)
```

---

<a id="avoid-leaving-revolutions-in-the-answer"></a>
## Avoid Leaving Revolutions In The Answer

**Example:** A turntable spins at \(7\) revolutions per second. Which setup correctly finds \(\omega\) in radians per second?

**Explanation**

The number \(7\) tells how many full turns happen each second. It is not yet in radians per second. Multiply by \(2\pi\ \mathrm{rad}/\mathrm{rev}\), not by \(\pi\), and do not divide by \(2\pi\).

$$
\omega=7\ \mathrm{rev}/\mathrm{s}\cdot \frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
=14\pi\ \mathrm{rad}/\mathrm{s}
$$

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  A motor spins with frequency $f=3$ revolutions per second. Which value is its angular speed?
options:
- id: q4-a
  content: |-
    \(3\ \mathrm{rad}/\mathrm{s}\)
- id: q4-b
  content: |-
    \(3\pi\ \mathrm{rad}/\mathrm{s}\)
- id: q4-c
  content: |-
    \(6\pi\ \mathrm{rad}/\mathrm{s}\)
  correct: true
- id: q4-d
  content: |-
    \(\frac{3}{2\pi}\ \mathrm{rad}/\mathrm{s}\)
```

---

<a id="summary"></a>
## Summary

When rotation frequency $f$ is given in revolutions per second and angular speed $\omega$ is required in radians per second, use

$$
\omega=2\pi f.
$$

The seconds stay in the denominator, and each revolution becomes \(2\pi\) radians. A quick checklist is:

1. Start with $f$ in \(\mathrm{rev}/\mathrm{s}\).
2. Multiply by \(\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}\).
3. Cancel \(\mathrm{rev}\), keep \(\mathrm{rad}/\mathrm{s}\), and round only if the problem asks for a rounded answer.

The main trap is to report the revolutions-per-second number as if it were already in radians per second.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
