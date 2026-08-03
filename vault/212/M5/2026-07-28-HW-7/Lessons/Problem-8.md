# Time for a Traveling Wave to Move One Wavelength

<!--
lesson-id: 212-M5-021
topic-code: MTH212.M5.21
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Wave Parameters](#read-the-wave-parameters)
- [Convert Angular Frequency to Period](#convert-angular-frequency-to-period)
- [Verify With Wavelength and Speed](#verify-with-wavelength-and-speed)
- [Avoid Coefficient and Unit Traps](#avoid-coefficient-and-unit-traps)
- [Apply the Method to Problem 8](#apply-the-method-to-problem-8)
- [Summary](#summary)

## Prerequisites

- Recognize coefficients in an expression of the form $A\sin(kx-\omega t+\phi)$.
- Know that sine and cosine complete one cycle after a phase change of $2\pi$ radians.
- Simplify a quotient while keeping track of units.

---

<a id="introduction"></a>
## Introduction

A traveling sinusoidal wave is commonly written as

$$
y(x,t)=A\sin(kx-\omega t+\phi).
$$

When a question asks how long the wave takes to travel **one wavelength**, it is asking for the time needed for the entire wave pattern to advance by one full cycle. That time is the **period** $T$.

The recognition cue is therefore:

> one wavelength of travel $\longleftrightarrow$ one period of time.

Read the angular frequency $\omega$ from the coefficient of $t$, and then compute

$$
\boxed{T=\frac{2\pi}{\omega}}.
$$

This is the shortest route. Computing the wavelength and wave speed is useful as a check, but it is not required when $\omega$ is already visible.

---

<a id="read-the-wave-parameters"></a>
## Read the Wave Parameters

Match each part of

$$
y(x,t)=A\sin(kx-\omega t+\phi)
$$

to its job:

| Symbol | Where to read it | What it controls |
|---|---|---|
| $A$ | Factor outside sine or cosine | Maximum displacement |
| $k$ | Magnitude of the coefficient of $x$ | Wavelength, $\lambda=2\pi/k$ |
| $\omega$ | Magnitude of the coefficient of $t$ | Period, $T=2\pi/\omega$ |

For a time question, focus first on $\omega$.

**Example:** Identify $k$ and $\omega$ in

$$
y(x,t)=(0.04\ \mathrm{m})\cos\left[(3\ \mathrm{rad/m})x-(12\ \mathrm{rad/s})t\right].
$$

**Explanation**

Compare the phase with $kx-\omega t$:

$$
k=3\ \mathrm{rad/m},
\qquad
\omega=12\ \mathrm{rad/s}.
$$

The amplitude $0.04\ \mathrm{m}$ does not determine how long a cycle lasts.

```quiz
type: radio
id: p8-read-omega
content: |-
  For
  $$
  y(x,t)=(0.03\ \mathrm{m})\sin\left[(2\ \mathrm{rad/m})x-(18\ \mathrm{rad/s})t\right],
  $$
  what is the angular frequency $\omega$?
options:
- id: p8-read-omega-a
  content: |-
    $2\ \mathrm{rad/m}$
- id: p8-read-omega-b
  content: |-
    $18\ \mathrm{rad/s}$
  correct: true
- id: p8-read-omega-c
  content: |-
    $0.03\ \mathrm{m}$
- id: p8-read-omega-d
  content: |-
    $9\ \mathrm{rad/s}$
- id: p8-read-omega-e
  content: |-
    $-18\ \mathrm{rad/s}$
```

---

<a id="convert-angular-frequency-to-period"></a>
## Convert Angular Frequency to Period

At a fixed position, the phase changes at a rate of $\omega$ radians per second. One complete cycle requires a phase change of $2\pi$ radians, so

$$
\omega T=2\pi
\qquad\Longrightarrow\qquad
T=\frac{2\pi}{\omega}.
$$

**Example:** A wave has angular frequency

$$
\omega=8\ \mathrm{rad/s}.
$$

How much time does it take the wave to travel one wavelength?

**Explanation**

One wavelength of travel takes one period:

$$
T=\frac{2\pi}{\omega}
=\frac{2\pi}{8}\ \mathrm{s}
=\frac{\pi}{4}\ \mathrm{s}.
$$

The radians cancel, leaving seconds, as a time answer should.

```quiz
type: radio
id: p8-period-direct
content: |-
  A traveling wave has angular frequency $\omega=6\ \mathrm{rad/s}$. How long does it take the wave to travel one wavelength?
options:
- id: p8-period-direct-a
  content: |-
    $\dfrac{\pi}{3}\ \mathrm{s}$
  correct: true
- id: p8-period-direct-b
  content: |-
    $\dfrac{1}{6}\ \mathrm{s}$
- id: p8-period-direct-c
  content: |-
    $3\pi\ \mathrm{s}$
- id: p8-period-direct-d
  content: |-
    $12\pi\ \mathrm{s}$
- id: p8-period-direct-e
  content: |-
    $\dfrac{3}{\pi}\ \mathrm{s}$
```

---

<a id="verify-with-wavelength-and-speed"></a>
## Verify With Wavelength and Speed

As an optional verification, compute the wavelength and wave speed:

$$
\lambda=\frac{2\pi}{k},
\qquad
v=\frac{\omega}{k}.
$$

Then

$$
\frac{\lambda}{v}
=\frac{2\pi/k}{\omega/k}
=\frac{2\pi}{\omega}
=T.
$$

This also shows why $k$ cancels from the one-wavelength travel time.

**Example:** Suppose

$$
k=4\ \mathrm{rad/m},
\qquad
\omega=10\ \mathrm{rad/s}.
$$

**Explanation**

First find the wavelength and speed:

$$
\lambda=\frac{2\pi}{4}\ \mathrm{m}
=\frac{\pi}{2}\ \mathrm{m},
$$

$$
v=\frac{10}{4}\ \mathrm{m/s}
=\frac{5}{2}\ \mathrm{m/s}.
$$

Now divide distance by speed:

$$
\frac{\lambda}{v}
=\frac{\pi/2}{5/2}\ \mathrm{s}
=\frac{\pi}{5}\ \mathrm{s}.
$$

The direct method gives the same value: $2\pi/10=\pi/5$ seconds.

```quiz
type: radio
id: p8-period-check
content: |-
  A wave has $k=6\ \mathrm{rad/m}$ and $\omega=9\ \mathrm{rad/s}$. What is the time required to travel one wavelength?
options:
- id: p8-period-check-a
  content: |-
    $\dfrac{2\pi}{9}\ \mathrm{s}$
  correct: true
- id: p8-period-check-b
  content: |-
    $\dfrac{\pi}{3}\ \mathrm{s}$
- id: p8-period-check-c
  content: |-
    $\dfrac{3}{2}\ \mathrm{s}$
- id: p8-period-check-d
  content: |-
    $\dfrac{\pi}{3}\ \mathrm{m}$
- id: p8-period-check-e
  content: |-
    $\dfrac{2}{3}\ \mathrm{s}$
```

---

<a id="avoid-coefficient-and-unit-traps"></a>
## Avoid Coefficient and Unit Traps

Keep these roles separate:

- $\omega$ controls the period: $T=2\pi/\omega$.
- $k$ controls the wavelength: $\lambda=2\pi/k$.
- The amplitude $A$ controls maximum displacement, not travel time.
- The sign between $kx$ and $\omega t$ controls direction of travel, not the period.
- A constant phase $\phi$ changes the starting point in the cycle, not the period.
- Because $\omega$ is in radians per second, $1/\omega$ is not a full cycle; a full cycle requires $2\pi$ radians.

**Example:** Find the one-wavelength travel time for

$$
y(x,t)=(0.12\ \mathrm{m})\cos\left[(5\ \mathrm{rad/m})x+(4\ \mathrm{rad/s})t+\frac{\pi}{6}\right].
$$

**Explanation**

The plus sign indicates the opposite direction from $kx-\omega t$, but the magnitude of the angular frequency is still

$$
\omega=4\ \mathrm{rad/s}.
$$

Therefore,

$$
T=\frac{2\pi}{4}\ \mathrm{s}
=\frac{\pi}{2}\ \mathrm{s}.
$$

Neither $A$, $k$, the direction sign, nor the phase constant changes this result.

```quiz
type: radio
id: p8-trap-check
content: |-
  For
  $$
  y(x,t)=(0.20\ \mathrm{m})\sin\left[(7\ \mathrm{rad/m})x+(15\ \mathrm{rad/s})t\right],
  $$
  how long does the wave take to travel one wavelength?
options:
- id: p8-trap-check-a
  content: |-
    $\dfrac{2\pi}{15}\ \mathrm{s}$
  correct: true
- id: p8-trap-check-b
  content: |-
    $\dfrac{1}{15}\ \mathrm{s}$
- id: p8-trap-check-c
  content: |-
    $\dfrac{2\pi}{7}\ \mathrm{s}$
- id: p8-trap-check-d
  content: |-
    $-\dfrac{2\pi}{15}\ \mathrm{s}$
- id: p8-trap-check-e
  content: |-
    $15\ \mathrm{s}$
```

---

<a id="apply-the-method-to-problem-8"></a>
## Apply the Method to Problem 8

**Example:** A wave is described by

$$
y(x,t)=(0.06\ \mathrm{m})\sin\left[(4\ \mathrm{rad/m})x-(10\ \mathrm{rad/s})t\right].
$$

How long does it take to travel one wavelength?

**Explanation**

Read the time coefficient:

$$
\omega=10\ \mathrm{rad/s}.
$$

Then use one wavelength of travel $=$ one period:

$$
T=\frac{2\pi}{10}\ \mathrm{s}
=\frac{\pi}{5}\ \mathrm{s}.
$$

Now apply the same two-line method to the assignment problem.

```quiz
type: radio
id: p8-assignment
shuffle: true
content: |-
  A transverse wave travels along a long, taut string.

  The transverse component of the displacement of the string from its resting configuration satisfies

  $y(x,t)=(0.1\ \mathrm{m})\sin\left[(2.5\ \mathrm{rad/m})x-(5\ \mathrm{rad/s})t\right],$

  where $x$ is the position along the string when at rest and $t$ is the time relative to some reference time $t=0$.

  How much time does it take the wave to traverse a distance of one wavelength?
options:
- id: p8-assignment-a
  content: |-
    $\dfrac{2\pi}{7}\ \mathrm{s}$
- id: p8-assignment-b
  content: |-
    $\dfrac{3\pi}{5}\ \mathrm{s}$
- id: p8-assignment-c
  content: |-
    $\dfrac{2\pi}{5}\ \mathrm{s}$
  correct: true
- id: p8-assignment-d
  content: |-
    $\dfrac{\pi}{2}\ \mathrm{s}$
```

---

<a id="summary"></a>
## Summary

When a traveling-wave question asks for the time to move one wavelength:

1. Match the phase to $kx\pm\omega t+\phi$.
2. Read $\omega$ as the magnitude of the coefficient of $t$.
3. Compute $T=2\pi/\omega$.
4. Confirm that the units reduce to seconds.

The main trap is confusing $k$ with $\omega$ or using $1/\omega$. The wavenumber $k$ sets the wavelength, while the angular frequency $\omega$ sets the period, and one full cycle contains $2\pi$ radians.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
