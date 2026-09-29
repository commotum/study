# Period of an Oscillator Before Its Mass Changes

<!--
lesson-id: 212-M4-021
topic-code: MTH212.M4.21
-->

## Table of Contents

- [Introduction](#introduction)
- [Freeze the System at the Requested Time](#freeze-the-system)
- [Use the Mass-Spring Period Formula](#use-the-period-formula)
- [Ignore Amplitude and Instantaneous Position](#ignore-amplitude-and-position)
- [Distinguish Period from Frequency](#distinguish-period-from-frequency)
- [Summary](#summary)

## Prerequisites

- Interpret “before” and “after” in a physical sequence of events.
- Know that period is the time required for one complete oscillation.
- Simplify square roots of fractions.

---

<a id="introduction"></a>
## Introduction

When a problem asks for an oscillator’s period **before** something collides with it or sticks to it, first freeze the story at that instant. Only the mass and spring constant that belong to the oscillator then go into the period formula.

For an ideal horizontal mass-spring oscillator,

$$
T=2\pi\sqrt{\frac{m}{k}},
$$

where $T$ is the period, $m$ is the mass attached to the spring at the requested time, and $k$ is the spring constant. Read the time phrase first, identify those two inputs, and then substitute. The amplitude and the object’s current position do not appear in this formula.

---

<a id="freeze-the-system"></a>
## Freeze the System at the Requested Time

**Example:** A block of mass $M$ oscillates on a spring. A lump of clay of mass $m_c$ will land on the block and stick to it. Which mass belongs in the period formula immediately before the clay lands?

**Explanation**

Separate the requested instant from the later event:

- Requested instant: immediately before the landing.
- Mass attached then: $M$.
- Spring constant then: $k$.

The clay has not joined the oscillator, so the oscillating mass is

$$
m_{\mathrm{osc}}=M.
$$

The combined mass $M+m_c$ would matter only for the motion after the collision.

```quiz
type: radio
id: q-p6-1
content: |-
  A cart of mass $3m$ oscillates on a spring. A second cart of mass $m$ will latch onto it. What mass should be used to find the period just before they latch?
options:
- id: q-p6-1-a
  content: |-
    $m$
- id: q-p6-1-b
  content: |-
    $2m$
- id: q-p6-1-c
  content: |-
    $3m$
  correct: true
- id: q-p6-1-d
  content: |-
    $4m$
```

---

<a id="use-the-period-formula"></a>
## Use the Mass-Spring Period Formula

**Example:** A $4\,\mathrm{kg}$ block oscillates on a spring with $k=100\,\mathrm{N}/\mathrm{m}$. Find its period.

**Explanation**

First extract the two inputs:

$$
m=4\,\mathrm{kg}
\qquad\text{and}\qquad
k=100\,\mathrm{N}/\mathrm{m}.
$$

Then substitute:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{m}{k}}\\
&=2\pi\sqrt{\frac{4}{100}}\\
&=0.4\pi\,\mathrm{s}.
\end{aligned}
$$

The units provide an independent check:

$$
\left[\frac{m}{k}\right]
=\frac{\mathrm{kg}}{\mathrm{kg}/\mathrm{s}^2}
=\mathrm{s}^2,
\qquad
\left[\sqrt{\frac{m}{k}}\right]=\mathrm{s}.
$$

```quiz
type: radio
id: q-p6-2
content: |-
  A $9\,\mathrm{kg}$ block oscillates on a spring with $k=100\,\mathrm{N}/\mathrm{m}$. What is its period?
options:
- id: q-p6-2-a
  content: |-
    $0.3\pi\,\mathrm{s}$
- id: q-p6-2-b
  content: |-
    $0.6\pi\,\mathrm{s}$
  correct: true
- id: q-p6-2-c
  content: |-
    $\dfrac{5}{3\pi}\,\mathrm{Hz}$
- id: q-p6-2-d
  content: |-
    $\dfrac{20\pi}{3}\,\mathrm{s}$
```

---

<a id="ignore-amplitude-and-position"></a>
## Ignore Amplitude and Instantaneous Position

**Example:** Two ideal oscillators have the same mass $m$ and spring constant $k$. One has amplitude $A$ and the other has amplitude $2A$. Compare their periods.

**Explanation**

Both periods are

$$
T=2\pi\sqrt{\frac{m}{k}}.
$$

For ideal simple harmonic motion, changing the amplitude does not change the period. Likewise, saying that the block is at $x=A/2$ locates it within the cycle but does not change its period.

```quiz
type: radio
id: q-p6-3
content: |-
  An ideal mass-spring oscillator is at $x=-A/3$. Which additional quantity is needed to determine its period?
options:
- id: q-p6-3-a
  content: |-
    Its velocity at that instant
- id: q-p6-3-b
  content: |-
    Its acceleration at that instant
- id: q-p6-3-c
  content: |-
    The amplitude $A$
- id: q-p6-3-d
  content: |-
    The oscillating mass and spring constant
  correct: true
```

---

<a id="distinguish-period-from-frequency"></a>
## Distinguish Period from Frequency

**Example:** Choose between

$$
2\pi\sqrt{\frac{m}{k}}
\qquad\text{and}\qquad
\frac{1}{2\pi}\sqrt{\frac{k}{m}}
$$

when a problem asks for the period.

**Explanation**

The second expression is the frequency:

$$
f=\frac{1}{2\pi}\sqrt{\frac{k}{m}}.
$$

Since $T=1/f$, the period is

$$
T=2\pi\sqrt{\frac{m}{k}}.
$$

A quick reasonableness check is that adding mass makes an oscillator slower, so the period must increase with $m$.
Likewise, a stiffer spring pulls the block back more strongly, so the period must decrease as $k$ increases. These trends agree with $m$ in the numerator and $k$ in the denominator of the period formula.

```quiz
type: radio
id: q-p6-4
content: |-
  A block of mass $M$ attached to an ideal spring of spring constant $k$ oscillates with amplitude $A$. A ball of clay will land on the block while it is at $x=A/2$ and stick to it. What is the block's period before the clay lands?
options:
- id: q-p6-4-a
  content: |-
    $2\pi\sqrt{\dfrac{M}{k}}$
  correct: true
- id: q-p6-4-b
  content: |-
    $\dfrac{1}{2\pi}\sqrt{\dfrac{M}{k}}$
- id: q-p6-4-c
  content: |-
    $\dfrac{1}{2\pi}\sqrt{\dfrac{k}{M}}$
- id: q-p6-4-d
  content: |-
    $2\pi\sqrt{\dfrac{k}{M}}$
```

---

<a id="summary"></a>
## Summary

When a period is requested **before** a collision or attachment:

1. Freeze the system at the requested time.
2. Identify the mass already oscillating and the spring constant.
3. Use

   $$
   T=2\pi\sqrt{\frac{m}{k}}.
   $$

4. Ignore amplitude and instantaneous position for an ideal spring.
5. Do not use a mass that joins the oscillator later, and do not mistake the frequency formula for the period formula.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
