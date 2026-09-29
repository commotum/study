# Amplitude and the Period of a Spring Oscillator

<!--
lesson-id: 212-M4-016
topic-code: MTH212.M4.16
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Period Formula](#read-the-period-formula)
- [Separate Motion Size from Cycle Time](#separate-motion-size-from-cycle-time)
- [Avoid the Proportionality Trap](#avoid-the-proportionality-trap)

## Prerequisites

- Recognize the period $T$ as the time for one complete oscillation.
- Identify $m$ as the block's mass, $k$ as the spring constant, and $A$ as the amplitude.
- Read a formula to determine which quantities its result depends on.

---

<a id="introduction"></a>
## Introduction

When an ideal block–spring oscillator changes amplitude while its mass and spring remain the same, use

$$
T=2\pi\sqrt{\frac{m}{k}}.
$$

The recognition cue is **an amplitude-only change**. The formula contains $m$ and $k$, but not $A$, so changing $A$ alone does not change the period:

$$
A\longrightarrow cA
\qquad\Rightarrow\qquad
T\longrightarrow T.
$$

The position form makes the roles of the parameters visible:

$$
x(t)=A\cos(\omega t+\phi),
\qquad
T=\frac{2\pi}{\omega}.
$$

- $A$ sets the vertical size of the motion: the amplitude.
- $\omega$ sets the horizontal repeat time: the period.
- For a block and spring, $\omega=\sqrt{k/m}$, so the amplitude does not set $\omega$.

This conclusion assumes the spring continues to obey Hooke's law.

---

<a id="read-the-period-formula"></a>
## Read the Period Formula

**Example:** A block of mass $m$ oscillates on an ideal spring with spring constant $k$. Its amplitude changes from $A$ to $3A$, while $m$ and $k$ stay fixed. What happens to its period?

**Explanation**

Compare the period before and after the change:

$$
T_{\mathrm{old}}=2\pi\sqrt{\frac{m}{k}},
\qquad
T_{\mathrm{new}}=2\pi\sqrt{\frac{m}{k}}.
$$

Use a short dependency check:

1. The changed quantity is $A$.
2. The requested quantity is $T$.
3. The formula for $T$ contains $m$ and $k$, but not $A$.

Therefore,

$$
T_{\mathrm{new}}=T_{\mathrm{old}}.
$$

```quiz
type: radio
id: p1-period-formula
content: |-
  An ideal block–spring oscillator has period $T$. Its amplitude changes from $A$ to $A/2$, with the same block and spring. What is the new period?
options:
- id: p1-period-formula-a
  content: |-
    $T/2$
- id: p1-period-formula-b
  content: |-
    $T$
  correct: true
- id: p1-period-formula-c
  content: |-
    $2T$
- id: p1-period-formula-d
  content: |-
    The amplitude cannot be halved.
```

---

<a id="separate-motion-size-from-cycle-time"></a>
## Separate Motion Size from Cycle Time

**Example:** A block's position is

$$
x(t)=(0.10\ \mathrm{m})\cos\left((4\ \mathrm{rad}/\mathrm{s})t\right).
$$

The amplitude is doubled without changing the block or spring. Find the new position function and compare the periods.

**Explanation**

In

$$
x(t)=A\cos(\omega t+\phi),
$$

$A$ controls the maximum displacement, while $\omega$ controls how quickly a cycle repeats. Doubling only the amplitude gives

$$
x_{\mathrm{new}}(t)=(0.20\ \mathrm{m})\cos\left((4\ \mathrm{rad}/\mathrm{s})t\right).
$$

The angular frequency is still $4\ \mathrm{rad}/\mathrm{s}$, so both motions have

$$
T=\frac{2\pi}{\omega}
=\frac{2\pi}{4\ \mathrm{rad}/\mathrm{s}}
=\frac{\pi}{2}\ \mathrm{s}.
$$

The block travels farther during each cycle, but the ideal spring also produces larger speeds and accelerations. The cycle time stays the same.

```quiz
type: radio
id: p1-position-function
content: |-
  A block moves according to
  $$
  x(t)=(0.30\ \mathrm{m})\cos\left((5\ \mathrm{rad}/\mathrm{s})t+\frac{\pi}{3}\right).
  $$
  If only the amplitude is tripled, which quantity remains unchanged?
options:
- id: p1-position-function-a
  content: |-
    The maximum displacement
- id: p1-position-function-b
  content: |-
    The maximum speed
- id: p1-position-function-c
  content: |-
    The period
  correct: true
- id: p1-position-function-d
  content: |-
    The total distance traveled in one cycle
```

```quiz
type: radio
id: p1-parameter-location
content: |-
  An oscillator has position $x(t)=A\cos(\omega t+\phi)$. Which new function doubles its amplitude without changing its period?
options:
- id: p1-parameter-location-a
  content: |-
    $x_{\mathrm{new}}(t)=2A\cos(\omega t+\phi)$
  correct: true
- id: p1-parameter-location-b
  content: |-
    $x_{\mathrm{new}}(t)=A\cos(2\omega t+\phi)$
- id: p1-parameter-location-c
  content: |-
    $x_{\mathrm{new}}(t)=A\cos(\omega t+2\phi)$
- id: p1-parameter-location-d
  content: |-
    $x_{\mathrm{new}}(t)=2A\cos(2\omega t+\phi)$
```

---

<a id="avoid-the-proportionality-trap"></a>
## Avoid the Proportionality Trap

**Example:** An ideal oscillator's amplitude is doubled. A student argues, “The block travels twice as far, so one cycle must take twice as long.” Identify the error.

**Explanation**

The argument changes distance but assumes speed stays fixed. In simple harmonic motion, doubling $A$ also doubles the maximum speed:

$$
v_{\max}=\omega A.
$$

Because the same factor changes the distance scale and the speed scale, the time scale $T=2\pi/\omega$ is unchanged. Do not decide how the period changes by matching it to the amplitude's factor; check the period formula instead.

For an amplitude-change question, ask:

1. Is this the ideal Hooke's-law model?
2. Did the prompt leave $m$ and $k$ unchanged?
3. Is $A$ absent from $T=2\pi\sqrt{m/k}$?

If all three answers are yes, the period is unchanged. Changing the initial displacement can double the amplitude, so “the amplitude cannot be doubled” is not a valid conclusion within the model.

```quiz
type: radio
id: p1-homework-check
content: |-
  The period of a block-spring system undergoing simple harmonic motion is $T$.

  If the amplitude of the oscillations in the system were doubled, what would be the new period?
options:
- id: p1-homework-check-a
  content: |-
    $T/4$
- id: p1-homework-check-b
  content: |-
    $T/2$
- id: p1-homework-check-c
  content: |-
    $T$
  correct: true
- id: p1-homework-check-d
  content: |-
    The amplitude cannot be doubled.
```

---

## Summary

For an ideal block–spring oscillator:

1. Recognize an amplitude-only change.
2. Separate the parameter roles: $A$ sets motion size, while $\omega$ sets cycle time.
3. Write $T=2\pi/\omega=2\pi\sqrt{m/k}$.
4. Check that $m$ and $k$ are unchanged.
5. Since $A$ does not appear in the period formula, conclude $T_{\mathrm{new}}=T_{\mathrm{old}}$.

The main trap is assuming that a larger travel distance automatically means a longer period. In ideal simple harmonic motion, amplitude changes the size of the motion, not its cycle time.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
