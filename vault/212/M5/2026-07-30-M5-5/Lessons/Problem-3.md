# Classifying Interference from Completely Out-of-Phase Sources

<!--
lesson-id: 212-M5-038
topic-code: MTH212.M5.38
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Frequency to Wavelength](#convert-frequency-to-wavelength)
- [Find the Path Difference](#find-the-path-difference)
- [Include the Sources' Starting Phase](#include-the-sources-starting-phase)
- [Classify the Antenna Interference](#classify-the-antenna-interference)
- [Recognize the Neither Case](#recognize-the-neither-case)
- [Summary](#summary)

## Prerequisites

- Use $v=f\lambda$ to relate wave speed, frequency, and wavelength.
- Find straight-line distances with the Pythagorean theorem.
- Recognize that a phase difference of $0$ modulo $2\pi$ is in phase, while $\pi$ modulo $2\pi$ is completely out of phase.

---

<a id="introduction"></a>
## Introduction

The cue **completely out of phase** means the sources start with a phase difference of $\pi$. Because of that starting difference, the usual path-difference rule for in-phase sources is reversed.

Use the same three-part procedure each time:

1. Convert the frequency to a wavelength.
2. Compute both source-to-point distances and their path difference.
3. Compare the path difference with the wavelength, while accounting for the initial $\pi$ phase difference.

For a path difference $\Delta r$, the propagation phase difference is

$$
\Delta\phi_{\text{path}}=2\pi\frac{\Delta r}{\lambda}.
$$

For the out-of-phase sources in this lesson, combine that path contribution with the initial $\pi$ difference:

$$
\Delta\phi_{\text{arrival}}\equiv\pi+2\pi\frac{\Delta r}{\lambda}\pmod{2\pi}.
$$

A result of $0$ modulo $2\pi$ means completely constructive interference, a result of $\pi$ means completely destructive interference, and any other result means neither. For these three classifications, the magnitude $\Delta r=|r_2-r_1|$ is sufficient.

---

<a id="convert-frequency-to-wavelength"></a>
## Convert Frequency to Wavelength

Radio waves in air travel at approximately $3.0\times10^8\ \mathrm{m/s}$. Convert megahertz to hertz before using $\lambda=v/f$.

**Example:** Find the wavelength of a $6.0\ \mathrm{MHz}$ radio wave.

**Explanation**

Since $6.0\ \mathrm{MHz}=6.0\times10^6\ \mathrm{Hz}=6.0\times10^6\ \mathrm{s^{-1}}$,

$$
\lambda
=\frac{3.0\times10^8\ \mathrm{m/s}}{6.0\times10^6\ \mathrm{s^{-1}}}
=50\ \mathrm{m}.
$$

```quiz
type: radio
id: problem-3-wavelength
content: |-
  What is the wavelength of a $2.0\ \mathrm{MHz}$ radio wave traveling at $3.0\times10^8\ \mathrm{m/s}$?
options:
- id: a
  content: |-
    $0.0067\ \mathrm{m}$
- id: b
  content: |-
    $1.5\ \mathrm{m}$
- id: c
  content: |-
    $150\ \mathrm{m}$
  correct: true
- id: d
  content: |-
    $6.0\times10^{14}\ \mathrm{m}$
- id: e
  content: |-
    $600\ \mathrm{m}$
```

---

<a id="find-the-path-difference"></a>
## Find the Path Difference

Compute each full source-to-point path before subtracting. Do not subtract only the sources' horizontal coordinates. The path difference is the nonnegative quantity

$$
\Delta r=|r_2-r_1|.
$$

**Example:** One source is directly $600\ \mathrm{m}$ below a detector, so $r_1=600\ \mathrm{m}$. A second source is $800\ \mathrm{m}$ horizontally from the first. Its path $r_2$ to the detector is the hypotenuse of a right triangle. Find $\Delta r$.

**Explanation**

The horizontal and vertical legs are $800\ \mathrm{m}$ and $600\ \mathrm{m}$, so the diagonal path is

$$
r_2=\sqrt{(800\ \mathrm{m})^2+(600\ \mathrm{m})^2}=1000\ \mathrm{m}.
$$

Therefore,

$$
\Delta r=|1000\ \mathrm{m}-600\ \mathrm{m}|=400\ \mathrm{m}.
$$

```quiz
type: radio
id: problem-3-path-difference
content: |-
  A detector is $400\ \mathrm{m}$ directly above one source. A second source is $300\ \mathrm{m}$ horizontally from the first. What is the path difference at the detector?
options:
- id: a
  content: |-
    $100\ \mathrm{m}$
  correct: true
- id: b
  content: |-
    $300\ \mathrm{m}$
- id: c
  content: |-
    $400\ \mathrm{m}$
- id: d
  content: |-
    $500\ \mathrm{m}$
- id: e
  content: |-
    $700\ \mathrm{m}$
```

---

<a id="include-the-sources-starting-phase"></a>
## Include the Sources' Starting Phase

An integer-wavelength path difference contributes whole cycles, so it preserves the starting relationship. A half-integer-wavelength path difference contributes an odd number of half-cycles, so it reverses the starting relationship.

| $\Delta r/\lambda$ | Arrival relationship | Classification |
|---|---|---|
| Integer: $n$ | Still out of phase | Completely destructive |
| Half-integer: $n+\tfrac12$ | Now in phase | Completely constructive |
| Any other value | Neither exact relationship | Neither |

**Watch the reversal:** this table applies because the sources begin completely out of phase. For in-phase sources, the constructive and destructive rows would switch.

**Example:** Two sources begin completely out of phase, and their path difference at a point is $3\lambda$. Classify the interference.

**Explanation**

The path contribution is $2\pi(3)=6\pi$. Thus

$$
\Delta\phi_{\text{arrival}}=\pi+6\pi=7\pi\equiv\pi\pmod{2\pi}.
$$

The waves arrive completely out of phase, so the interference is completely destructive.

```quiz
type: radio
id: problem-3-initial-phase
content: |-
  Two sources begin completely out of phase. At an observation point, their path difference is $2.5\lambda$. What kind of interference occurs there?
options:
- id: a
  content: |-
    Completely constructive interference
  correct: true
  feedback: |-
    A half-integer path difference contributes an odd multiple of $\pi$, reversing the sources' initial out-of-phase relationship.
- id: b
  content: |-
    Completely destructive interference
  feedback: |-
    That would occur for an integer-wavelength path difference when the sources begin out of phase.
- id: c
  content: |-
    Neither
  feedback: |-
    A half-integer wavelength is an exact reversal, so the waves arrive completely in phase.
```

---

<a id="classify-the-antenna-interference"></a>
## Classify the Antenna Interference

**Example:** Two completely out-of-phase radio antennas at $x=+300\ \mathrm{m}$ and $x=-300\ \mathrm{m}$ emit $3.0\ \mathrm{MHz}$ waves. At $P=(300\ \mathrm{m},800\ \mathrm{m})$, determine whether the interference is completely constructive, completely destructive, or neither.

![](<../Source/Images/out-of-phase-antennas-path-difference.png>)

**Explanation**

First find the wavelength:

$$
\lambda=\frac{3.0\times10^8\ \mathrm{m/s}}{3.0\times10^6\ \mathrm{s^{-1}}}=100\ \mathrm{m}.
$$

The right antenna and $P$ have the same $x$-coordinate. Its vertical path is therefore

$$
r_1=800\ \mathrm{m}.
$$

For the left antenna, label the legs before finding the diagonal path:

$$
\Delta x=|300-(-300)|=600\ \mathrm{m},
\qquad
\Delta y=|800-0|=800\ \mathrm{m}.
$$

Thus,

$$
r_2=\sqrt{(600\ \mathrm{m})^2+(800\ \mathrm{m})^2}=1000\ \mathrm{m}.
$$

Therefore,

$$
\Delta r=1000\ \mathrm{m}-800\ \mathrm{m}=200\ \mathrm{m}=2\lambda.
$$

The integer-wavelength path difference contributes $4\pi$, which does not reverse the antennas' initial $\pi$ phase difference:

$$
\Delta\phi_{\text{arrival}}=\pi+4\pi=5\pi\equiv\pi\pmod{2\pi}.
$$

The interference at $P$ is **completely destructive**.

```quiz
type: radio
id: problem-3-antennas
content: |-
  Two completely out-of-phase antennas emit $3.0\ \mathrm{MHz}$ waves. At a point where the source-to-point distances are $700\ \mathrm{m}$ and $1000\ \mathrm{m}$, is the interference completely constructive, completely destructive, or neither? Use $3.0\times10^8\ \mathrm{m/s}$ for the wave speed.
options:
- id: a
  content: |-
    Completely constructive interference
  feedback: |-
    The path difference is $300\ \mathrm{m}=3\lambda$, not a half-integer multiple of the wavelength.
- id: b
  content: |-
    Completely destructive interference
  correct: true
  feedback: |-
    Here $\lambda=100\ \mathrm{m}$ and $\Delta r=300\ \mathrm{m}=3\lambda$, so the waves retain their initial out-of-phase relationship.
- id: c
  content: |-
    Neither
  feedback: |-
    An integer-wavelength path difference preserves an exact out-of-phase relationship.
```

---

<a id="recognize-the-neither-case"></a>
## Recognize the Neither Case

Do not force every result into constructive or destructive interference. For sources that begin completely out of phase, integer values of $\Delta r/\lambda$ are destructive and half-integer values are constructive. Other fractional values give neither extreme.

**Example:** Completely out-of-phase sources have $\Delta r=1.25\lambda$. Classify the interference.

**Explanation**

The total phase difference is

$$
\Delta\phi_{\text{arrival}}=\pi+2\pi(1.25)=3.5\pi\equiv1.5\pi\pmod{2\pi}.
$$

This is neither $0$ nor $\pi$ modulo $2\pi$, so the interference is neither completely constructive nor completely destructive.

```quiz
type: radio
id: problem-3-neither
content: |-
  Two completely out-of-phase sources produce a path difference of $0.80\lambda$ at a detector. What kind of interference occurs there?
options:
- id: a
  content: |-
    Completely constructive interference
  feedback: |-
    Constructive interference requires a half-integer value of $\Delta r/\lambda$ for sources that begin out of phase.
- id: b
  content: |-
    Completely destructive interference
  feedback: |-
    Destructive interference requires an integer value of $\Delta r/\lambda$ for sources that begin out of phase.
- id: c
  content: |-
    Neither
  correct: true
  feedback: |-
    Since $0.80$ is neither an integer nor a half-integer, the waves are at neither exact phase relationship.
```

---

<a id="summary"></a>
## Summary

For two sources that begin completely out of phase:

1. Find the wavelength with $\lambda=v/f$.
2. Compute both path lengths and set $\Delta r=|r_2-r_1|$.
3. Compute $\Delta r/\lambda$.
4. Classify: integer means destructive, half-integer means constructive, and any other value means neither.

For completely out-of-phase sources, remember the reversal: an integer-wavelength path difference is destructive, while a half-integer-wavelength path difference is constructive. The main trap is to ignore the initial $\pi$ phase difference and classify from $\Delta r$ alone.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
