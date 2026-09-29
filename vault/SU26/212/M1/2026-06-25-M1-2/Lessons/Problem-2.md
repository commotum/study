# Deciding Where Distance Belongs in a Speed Formula

<!--
lesson-id: 212-M1-038
topic-code: MTH212.M1.38
-->

## Table of Contents

- [Introduction](#introduction)
- [Hold The Timing Condition Fixed](#hold-the-timing-condition-fixed)
- [Match Increase To Numerator Or Denominator](#match-increase-to-numerator-or-denominator)
- [Avoid Letting Two Things Change At Once](#avoid-letting-two-things-change-at-once)
- [Connect The Reasoning To The Disk Formula](#connect-the-reasoning-to-the-disk-formula)
- [Summary](#summary)

## Prerequisites

- Speed relates distance and time by $v=\dfrac{\text{distance}}{\text{time}}$.
- A factor in the numerator makes the target quantity increase when that factor increases.
- A factor in the denominator makes the target quantity decrease when that factor increases.
- To test one variable, hold the other givens fixed.

---

<a id="introduction"></a>
## Introduction

In the rotating-disk setup, a bullet travels from the first disk to the second disk. The disk separation is $D$, the rotation period is $T$, and the angular separation between the holes is $\theta$.

The question asks whether $D$ should appear in the numerator or denominator of the formula for bullet speed $v$. The useful cue is that only $D$ is being tested. Keep $T$ and $\theta$ fixed, then ask what happens to the required speed when $D$ increases.

---

<a id="hold-the-timing-condition-fixed"></a>
## Hold The Timing Condition Fixed

**Example:** One bullet must travel $0.8\ \mathrm{m}$ in a fixed time. Another bullet must travel $1.6\ \mathrm{m}$ in that same fixed time. Which bullet must have the larger speed?

**Explanation**

The second bullet must have the larger speed because it covers more distance in the same time. For example, if the fixed time is $\Delta t=0.2\ \mathrm{s}$, then

$$
v=\frac{0.8}{0.2}=4\ \mathrm{m}/\mathrm{s}
$$

$$
v=\frac{1.6}{0.2}=8\ \mathrm{m}/\mathrm{s}
$$

The rotating disks create the same kind of comparison. The rotation controls the timing condition: the second hole lines up after a fixed angular rotation. If $T$ and $\theta$ stay fixed, the bullet has the same amount of travel time available. Only the distance it must cover has changed.

```quiz
type: radio
id: q-hold-fixed
shuffle: true
content: |-
  In the rotating-disk setup, suppose $T$ and $\theta$ are held fixed while $D$ increases. What should you treat as unchanged when deciding where $D$ belongs in the formula for $v$?
options:
- id: a
  content: |-
    The timing condition set by the rotating disks
  correct: true
- id: b
  content: |-
    The distance the bullet travels
- id: c
  content: |-
    The bullet speed
- id: d
  content: |-
    The answer choice for $D$
```

---

<a id="match-increase-to-numerator-or-denominator"></a>
## Match Increase To Numerator Or Denominator

**Example:** A runner must cover distance $L$ in a fixed time $\Delta t$. Should $L$ appear in the numerator or denominator of the speed formula?

**Explanation**

Use the basic speed relation:

$$
v=\frac{L}{\Delta t}
$$

If $L$ increases while $\Delta t$ stays fixed, $v$ increases. A variable that makes the target quantity increase when it increases belongs in the numerator.

For the disks, $D$ plays the role of the distance $L$. If the bullet has the same travel time but must cover a larger $D$, the required $v$ is larger. Therefore, $D$ belongs in the numerator.

With $T$ and $\theta$ fixed, the relationship is direct:

$$
v \propto D
$$

```quiz
type: radio
id: q-distance-position
shuffle: true
content: |-
  A cart must travel a track length $L$ in the same fixed time no matter which track is used. If the formula gives the required speed $v$, where should $L$ appear?
options:
- id: a
  content: |-
    In the numerator
  correct: true
- id: b
  content: |-
    In the denominator
- id: c
  content: |-
    Neither, because distance does not affect speed
- id: d
  content: |-
    It cannot be decided unless $L$ has a number
```

---

<a id="avoid-letting-two-things-change-at-once"></a>
## Avoid Letting Two Things Change At Once

**Example:** A student says, "If the disks are farther apart, the bullet takes more time, so $D$ should go in the denominator." What is wrong with that reasoning?

**Explanation**

That reasoning lets the travel time change while testing $D$. But the numerator-or-denominator question asks for the effect of one variable at a time. In this setup, $T$ and $\theta$ determine the timing condition. When they are fixed, the available travel time is fixed.

The clean comparison is not:

$$
\text{larger distance and larger time}
$$

The clean comparison is:

$$
\text{larger distance in the same time}
$$

That requires a larger speed, so $D$ is a numerator factor.

```quiz
type: radio
id: q-common-trap
shuffle: true
content: |-
  Which explanation correctly avoids the common trap when deciding where $D$ belongs?
options:
- id: a
  content: |-
    Increasing $D$ means the bullet has more time, so $D$ belongs in the denominator.
- id: b
  content: |-
    Hold $T$ and $\theta$ fixed; a larger $D$ must be covered in the same timing condition, so $v$ increases and $D$ belongs in the numerator.
  correct: true
- id: c
  content: |-
    Since $D$ is a distance, it always cancels out of a speed formula.
- id: d
  content: |-
    Since $D$ is measured in meters, it must belong in the denominator to make units of meters per second.
```

---

<a id="connect-the-reasoning-to-the-disk-formula"></a>
## Connect The Reasoning To The Disk Formula

**Example:** The bullet travels distance $D$ while the disks rotate through angle $\theta$. The bullet travel time is $\Delta t$, so

$$
D=v\Delta t
$$

The rotation condition is

$$
\theta=\omega \Delta t
$$

How does this confirm the placement of $D$?

**Explanation**

The first equation gives

$$
v=\frac{D}{\Delta t}
$$

The second equation tells you that $\Delta t$ is set by the rotation. Holding $T$ and $\theta$ fixed holds that travel time fixed. In the expression for $v$, $D$ is divided by a time, so $D$ is in the numerator.

Using $\omega=\dfrac{2\pi}{T}$ gives the full form

$$
v=\frac{2\pi D}{T\theta}
$$

The full formula agrees with the reasoning: $D$ is in the numerator.

```quiz
type: radio
id: q-original-form
shuffle: true
content: |-
  A bullet passes through two holes in rotating disks a distance $D$ apart. The period $T$ and angular separation $\theta$ are fixed. In the formula for the bullet speed $v$, where should $D$ appear?
options:
- id: a
  content: |-
    numerator
  correct: true
- id: b
  content: |-
    denominator
- id: c
  content: |-
    neither
```

---

## Summary

To decide where one variable belongs, hold the other givens fixed and ask how increasing that variable changes the target quantity. For Problem 2, keep $T$ and $\theta$ fixed. A larger disk separation $D$ means the bullet must travel farther under the same timing condition, so the required speed $v$ increases. That means $D$ appears in the numerator.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
