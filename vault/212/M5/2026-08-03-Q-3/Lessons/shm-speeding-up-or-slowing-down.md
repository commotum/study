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
    Since $a=-\omega^2x$ and $x<0$, the acceleration is positive.
- id: q3-shm-speed-acceleration-sign-b
  content: |-
    $a<0$
  feedback: |-
    Acceleration has the sign opposite displacement in SHM.
- id: q3-shm-speed-acceleration-sign-c
  content: |-
    $a=0$
  feedback: |-
    Acceleration is zero at equilibrium, not at a nonzero displacement.
- id: q3-shm-speed-acceleration-sign-d
  content: |-
    The sign of $a$ depends on the sign of $v$.
  feedback: |-
    The relation $a=-\omega^2x$ fixes the acceleration sign from $x$ alone.
- id: q3-shm-speed-acceleration-sign-e
  content: |-
    The sign of $a$ depends on the amplitude.
  feedback: |-
    Amplitude can affect the possible magnitude of $x$, but not the restoring direction at a given $x$.
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
    Positive $x$ gives negative $a$. Velocity and acceleration are both negative, so speed increases.
- id: q3-shm-speed-same-signs-b
  content: |-
    Slowing down, because $x$ and $v$ have opposite signs
  feedback: |-
    Opposite signs of $x$ and $v$ mean motion toward equilibrium. Compare $v$ with $a$, not $v$ with $x$.
- id: q3-shm-speed-same-signs-c
  content: |-
    Slowing down, because $a>0$ and $v<0$
  feedback: |-
    For $x>0$, the restoring acceleration is negative, not positive.
- id: q3-shm-speed-same-signs-d
  content: |-
    Moving at constant speed, because $x$ is fixed at this instant
  feedback: |-
    An instantaneous position does not imply constant speed; here the nonzero acceleration changes the speed.
- id: q3-shm-speed-same-signs-e
  content: |-
    There is not enough information without knowing $\omega$
  feedback: |-
    The value of $\omega$ affects magnitude, but $\omega^2>0$ is enough to determine the acceleration sign.
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
    Negative $x$ gives positive $a$. Opposite signs of $v$ and $a$ mean decreasing speed.
- id: q3-shm-speed-opposite-signs-b
  content: |-
    It is speeding up because both $x$ and $v$ are negative.
  feedback: |-
    Compare velocity with acceleration. Here $a$ is positive, opposite the negative velocity.
- id: q3-shm-speed-opposite-signs-c
  content: |-
    It is speeding up because $a<0$ points with $v<0$.
  feedback: |-
    The acceleration is positive when the displacement is negative.
- id: q3-shm-speed-opposite-signs-d
  content: |-
    It moves at constant speed because $x$ and $v$ have the same sign.
  feedback: |-
    Same signs of $x$ and $v$ mean motion away from equilibrium, not constant speed.
- id: q3-shm-speed-opposite-signs-e
  content: |-
    It is stopped because its displacement is negative.
  feedback: |-
    The given velocity is nonzero, so the oscillator is moving.
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
    At $x=0$, $a=-\omega^2x=0$. An ideal SHM oscillator has maximum speed at equilibrium.
- id: q3-shm-speed-zero-case-b
  content: |-
    $a<0$, so it is speeding up.
  feedback: |-
    At equilibrium, displacement and acceleration are both zero.
- id: q3-shm-speed-zero-case-c
  content: |-
    $a>0$, so it is slowing down.
  feedback: |-
    The acceleration is zero when $x=0$.
- id: q3-shm-speed-zero-case-d
  content: |-
    $v=0$ because every oscillator stops at equilibrium.
  feedback: |-
    An SHM oscillator stops at its turning points and reaches maximum speed at equilibrium.
- id: q3-shm-speed-zero-case-e
  content: |-
    Both $v$ and $a$ are zero.
  feedback: |-
    The velocity is explicitly nonzero, while the acceleration is zero at equilibrium.
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

---

<!-- lesson-nav:end -->
