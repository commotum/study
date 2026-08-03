# Deciding Whether an SHM Oscillator Is Speeding Up or Slowing Down

<!--
lesson-id: 212-M5-050
topic-code: MTH212.M5.50
-->

## Table of Contents

- [Introduction](#introduction)
- [Find Acceleration From Displacement](#find-acceleration-from-displacement)
- [Same Signs Mean Speeding Up](#same-signs-mean-speeding-up)
- [Opposite Signs Mean Slowing Down](#opposite-signs-mean-slowing-down)
- [Handle Equilibrium and Turning Points](#handle-equilibrium-and-turning-points)
- [Summary](#summary)

## Prerequisites

- Interpret positive and negative directions on a one-dimensional axis.
- Distinguish displacement $x$ from velocity $v$.
- Know that $\omega^2$ is positive for a nonzero angular frequency.

---

<a id="introduction"></a>
## Introduction

When a simple harmonic oscillator's displacement and velocity are known at one instant, you can decide whether it is speeding up or slowing down without finding any magnitudes.

The recognition cue is a request to interpret the motion from the signs of $x$ and $v$. Use the SHM restoring-acceleration relation

$$
a=-\omega^2x.
$$

Because $\omega^2>0$, acceleration always has the sign opposite displacement. Then compare the signs of velocity and acceleration:

| Signs of $v$ and $a$ | Motion |
| --- | --- |
| Same | Speeding up |
| Opposite | Slowing down |

Velocity tells which way the oscillator moves. Acceleration tells which way its velocity is changing. Motion and acceleration in the same direction increase speed; opposite directions decrease speed.

---

<a id="find-acceleration-from-displacement"></a>
## Find Acceleration From Displacement

First use $a=-\omega^2x$ to determine the acceleration sign. The value of $\omega$ changes the acceleration's magnitude, but not its sign.

**Example:** An oscillator is at $x=+0.15\ \mathrm{m}$. What is the sign of its acceleration?

**Explanation**

The displacement is positive, so

$$
a=-\omega^2(+0.15\ \mathrm{m})<0.
$$

The oscillator is to the right of equilibrium, and its restoring acceleration points left. This alone does not say whether it is speeding up; velocity is still needed.

```quiz
type: radio
id: q3-shm-speed-acceleration-sign
content: |-
  A simple harmonic oscillator is at $x=-0.20\ \mathrm{m}$. What can you conclude about its acceleration?
options:
- id: q3-shm-speed-acceleration-sign-a
  content: |-
    $a>0$
  correct: true
  feedback: |-
    An SHM acceleration always points back toward equilibrium. Here the oscillator is left of equilibrium because $x<0$, so "back" is the positive direction. Therefore, $a>0$.
- id: q3-shm-speed-acceleration-sign-b
  content: |-
    $a<0$
  feedback: |-
    This copies the displacement sign instead of using the restoring direction. A negative acceleration would point left and is correct when $x>0$; here $x<0$, so equilibrium lies to the right and $a=-\omega^2x>0$.
- id: q3-shm-speed-acceleration-sign-c
  content: |-
    $a=0$
  feedback: |-
    Zero restoring acceleration occurs only at equilibrium, where $x=0$. The oscillator is displaced by $0.20\ \mathrm{m}$, so the restoring force is nonzero and $a=-\omega^2(-0.20\ \mathrm{m})>0$.
- id: q3-shm-speed-acceleration-sign-d
  content: |-
    The sign of $a$ depends on the sign of $v$.
  feedback: |-
    Velocity tells which way the oscillator is moving; displacement tells which way the restoring acceleration points. The oscillator can pass this same $x$ with either sign of $v$, but in both cases $a=-\omega^2x>0$ because $x<0$.
- id: q3-shm-speed-acceleration-sign-e
  content: |-
    The sign of $a$ depends on the amplitude.
  feedback: |-
    Amplitude $A$ sets the turning points and the maximum acceleration $\omega^2A$; it does not choose the restoring direction at a given position. Once $x<0$ is known, $a=-\omega^2x$ is positive for any allowed $A\ge |x|$.
```

---

<a id="same-signs-mean-speeding-up"></a>
## Same Signs Mean Speeding Up

If velocity and acceleration have the same sign, they point in the same direction. The magnitude of the velocity is increasing, so the oscillator is speeding up.

**Example:** At one instant, $x=-0.08\ \mathrm{m}$ and $v=+0.45\ \mathrm{m/s}$. Is the oscillator speeding up or slowing down?

**Explanation**

Negative displacement gives positive acceleration:

$$
x<0 \quad\Longrightarrow\quad a>0.
$$

Both $v$ and $a$ are positive. The oscillator moves right and accelerates right, so it is speeding up. It is also moving toward equilibrium, which is a useful check.

```quiz
type: radio
id: q3-shm-speed-same-signs
content: |-
  At one instant, a simple harmonic oscillator has $x=+0.11\ \mathrm{m}$ and $v=-0.32\ \mathrm{m/s}$. What is it doing?
options:
- id: q3-shm-speed-same-signs-a
  content: |-
    Speeding up, because $a<0$ and $v<0$
  correct: true
  feedback: |-
    A restoring acceleration points toward equilibrium. From $x>0$, that direction is left, so $a=-\omega^2x<0$; the given $v<0$ is also leftward. Because $v$ and $a$ have the same sign, $va>0$ and the oscillator is speeding up.
- id: q3-shm-speed-same-signs-b
  content: |-
    Slowing down, because $x$ and $v$ have opposite signs
  feedback: |-
    Opposite signs of $x$ and $v$ mean the oscillator is moving toward equilibrium, where its speed is greatest. Here $x>0$ makes $a<0$, matching the given $v<0$, so it speeds up. Slowing would require $v$ and $a$ to have opposite signs.
- id: q3-shm-speed-same-signs-c
  content: |-
    Slowing down, because $a>0$ and $v<0$
  feedback: |-
    The stated sign of acceleration is the failed step. Positive acceleration would point right and applies on the $x<0$ side; at $x>0$, the restoring direction is left, so $a=-\omega^2x<0$. Thus $a$ and $v$ agree and the oscillator speeds up.
- id: q3-shm-speed-same-signs-d
  content: |-
    Moving at constant speed, because $x$ is fixed at this instant
  feedback: |-
    A position given at one instant is a snapshot, not a statement that $x$ remains fixed. Because $x\ne0$, the restoring acceleration is nonzero; here $a<0$ acts with $v<0$, so the speed is increasing. Constant speed over an interval would require zero acceleration throughout that interval.
- id: q3-shm-speed-same-signs-e
  content: |-
    There is not enough information without knowing $\omega$
  feedback: |-
    The value of $\omega$ is needed for the magnitude $|a|=\omega^2|x|$, but not for the direction test. For any nonzero angular frequency, $\omega^2>0$; therefore $x>0\Rightarrow a<0$, and with $v<0$ the oscillator is speeding up.
```

---

<a id="opposite-signs-mean-slowing-down"></a>
## Opposite Signs Mean Slowing Down

If velocity and acceleration have opposite signs, acceleration points against the motion. The magnitude of the velocity is decreasing, so the oscillator is slowing down.

**Example:** At one instant, $x=+0.06\ \mathrm{m}$ and $v=+0.28\ \mathrm{m/s}$. Is the oscillator speeding up or slowing down?

**Explanation**

Positive displacement gives negative acceleration:

$$
x>0 \quad\Longrightarrow\quad a<0.
$$

The velocity is positive while the acceleration is negative. The oscillator moves right but accelerates left, so it is slowing down. It is moving away from equilibrium and toward a turning point.

```quiz
type: radio
id: q3-shm-speed-opposite-signs
content: |-
  A simple harmonic oscillator has $x=-0.09\ \mathrm{m}$ and $v=-0.40\ \mathrm{m/s}$ at one instant. Which description is correct?
options:
- id: q3-shm-speed-opposite-signs-a
  content: |-
    It is slowing down because $a>0$ points opposite $v<0$.
  correct: true
  feedback: |-
    The restoring acceleration points toward equilibrium. From $x<0$, equilibrium is to the right, so $a=-\omega^2x>0$ while the given $v<0$ points left. Because $va<0$, acceleration opposes the motion and the oscillator is slowing down.
- id: q3-shm-speed-opposite-signs-b
  content: |-
    It is speeding up because both $x$ and $v$ are negative.
  feedback: |-
    Matching signs of $x$ and $v$ mean the oscillator is moving away from equilibrium; they do not mean velocity and acceleration match. Since acceleration has the sign opposite $x$, here $a>0$ opposes $v<0$, so the speed decreases. At this same $x<0$, it would speed up if $v>0$ toward equilibrium.
- id: q3-shm-speed-opposite-signs-c
  content: |-
    It is speeding up because $a<0$ points with $v<0$.
  feedback: |-
    The misconception is assigning acceleration the same sign as displacement. A restoring acceleration points right when the oscillator is left of equilibrium: $x<0\Rightarrow a=-\omega^2x>0$. Therefore $a$ opposes the negative velocity and the oscillator slows.
- id: q3-shm-speed-opposite-signs-d
  content: |-
    It moves at constant speed because $x$ and $v$ have the same sign.
  feedback: |-
    Same signs of $x$ and $v$ diagnose motion away from equilibrium, not constant speed. Here $a>0$ opposes $v<0$, so speed decreases. Constant speed over an interval would require $a=0$ throughout; a nontrivial SHM oscillator has $a=0$ only momentarily as it crosses $x=0$.
- id: q3-shm-speed-opposite-signs-e
  content: |-
    It is stopped because its displacement is negative.
  feedback: |-
    Displacement tells location, while velocity tells motion; a negative $x$ does not mean stopped. The problem explicitly gives $v=-0.40\ \mathrm{m/s}\ne0$. An SHM oscillator stops only at a turning point, where $v=0$ and $x=\pm A$.
```

---

<a id="handle-equilibrium-and-turning-points"></a>
## Handle Equilibrium and Turning Points

The same-sign/opposite-sign test assumes both $v$ and $a$ are nonzero. At equilibrium or a turning point, one of them is zero, so describe the boundary instant separately.

**Example:** An oscillator is at its right turning point, where $x=+A$ and $v=0$. Is it speeding up or slowing down at that exact instant?

**Explanation**

At the turning point,

$$
a=-\omega^2A<0,
$$

but $v=0$, so velocity has no direction to compare with acceleration at that instant. The oscillator arrived while slowing down, stops momentarily, and then departs left while speeding up.

At equilibrium, $x=0$ gives $a=0$ and the speed is maximum. The oscillator arrives while speeding up and leaves while slowing down.

```quiz
type: radio
id: q3-shm-speed-zero-case
content: |-
  A simple harmonic oscillator passes through equilibrium with $v<0$. Which statement best describes that exact instant?
options:
- id: q3-shm-speed-zero-case-a
  content: |-
    $a=0$ and the speed is maximum; the oscillator is at the transition from speeding up to slowing down.
  correct: true
  feedback: |-
    At equilibrium $x=0$, so the restoring force and acceleration are zero. The oscillator's potential energy is minimum and its speed is maximum. With $v<0$, this is the instant between speeding up on the $x>0$ side and slowing down on the $x<0$ side.
- id: q3-shm-speed-zero-case-b
  content: |-
    $a<0$, so it is speeding up.
  feedback: |-
    A negative restoring acceleration applies just before this crossing, while the oscillator is still on the $x>0$ side. At the exact boundary $x=0$, however, $a=-\omega^2x=0$. The speed is maximum there, so this instant separates speeding up from slowing down.
- id: q3-shm-speed-zero-case-c
  content: |-
    $a>0$, so it is slowing down.
  feedback: |-
    A positive restoring acceleration applies just after the oscillator enters the $x<0$ side. At the exact equilibrium crossing, $x=0$ makes $a=0$. The oscillator is at maximum speed and only begins slowing immediately after the crossing.
- id: q3-shm-speed-zero-case-d
  content: |-
    $v=0$ because every oscillator stops at equilibrium.
  feedback: |-
    This swaps the roles of equilibrium and a turning point. The oscillator stops where all energy is potential, at $x=\pm A$; at $x=0$, spring potential is minimum and speed is maximum. The stated $v<0$ also confirms motion through equilibrium.
- id: q3-shm-speed-zero-case-e
  content: |-
    Both $v$ and $a$ are zero.
  feedback: |-
    Equilibrium makes $a=0$, but the prompt explicitly gives $v<0$, so both quantities are not zero. If $v=0$ and $a=0$ simultaneously, then $a=-\omega^2x$ also forces $x=0$; that is the trivial $A=0$ state, not an oscillator passing through equilibrium.
```

---

<a id="summary"></a>
## Summary

When an SHM problem gives the signs of displacement and velocity and asks whether the oscillator is speeding up or slowing down:

1. Use $a=-\omega^2x$ to make the acceleration sign opposite the displacement sign.
2. Compare velocity with acceleration.
3. Same signs of $v$ and $a$ mean **speeding up**.
4. Opposite signs of $v$ and $a$ mean **slowing down**.

For nonzero $x$ and $v$, this also gives a quick check:

$$
xv<0 \Rightarrow \text{moving toward equilibrium and speeding up},
$$

$$
xv>0 \Rightarrow \text{moving away from equilibrium and slowing down}.
$$

The main trap is treating the sign of $x$ as the direction of motion. Position tells which side of equilibrium the oscillator occupies; velocity tells which way it moves.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../Study-Guide.md)
Next: [Speed of a Spring Oscillator at a Given Position](../../../M4/2026-07-23-HW-6/Lessons/Problem-7.md)

Study guide index: 04/28

---
<!-- lesson-nav:end -->
