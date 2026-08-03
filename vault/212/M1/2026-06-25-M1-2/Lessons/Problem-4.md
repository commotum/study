# Placing Angular Separation in a Speed Formula

<!--
lesson-id: 212-M1-040
topic-code: MTH212.M1.40
-->

## Table of Contents

- [Introduction](#introduction)
- [Relate Angle to Fraction of a Turn](#relate-angle-to-fraction-of-a-turn)
- [Turn Rotation Time Into Bullet Speed](#turn-rotation-time-into-bullet-speed)
- [Decide Whether an Angle Belongs Upstairs or Downstairs](#decide-whether-an-angle-belongs-upstairs-or-downstairs)
- [Avoid the Angle Trap](#avoid-the-angle-trap)
- [Summary](#summary)

## Prerequisites

- Know that one full rotation is $2\pi$ radians.
- Know that a period $T$ is the time for one full rotation.
- Know that speed is distance divided by time: $v=\dfrac{\text{distance}}{\text{time}}$.

---

<a id="introduction"></a>
## Introduction

In the rotating-disk setup, a bullet travels distance $D$ while the shaft rotates through the angular separation $\theta$ between the holes. The useful cue is that $\theta$ describes how much of one rotation must happen before the second hole lines up.

To decide whether $\theta$ belongs in the numerator or denominator of the speed formula, first decide how $\theta$ affects the bullet's travel time. Then use $v=D/t$.

The reusable rule is:

$$
\text{rotation time}=\text{fraction of a turn}\cdot \text{period}
=\dfrac{\theta}{2\pi}T.
$$

---

<a id="relate-angle-to-fraction-of-a-turn"></a>
## Relate Angle to Fraction of a Turn

**Example:** A shaft has period $T=0.80\ \mathrm{s}$. How long does it take the shaft to rotate through an angle $\theta=\dfrac{\pi}{2}$?

**Explanation**

One full rotation is $2\pi$ radians, so the fraction of a full turn is

$$
\dfrac{\theta}{2\pi}
=
\dfrac{\pi/2}{2\pi}
=
\dfrac14.
$$

Since the shaft takes $T=0.80\ \mathrm{s}$ for a full turn, the time for one quarter-turn is

$$
t=\dfrac14T=\dfrac14(0.80\ \mathrm{s})=0.20\ \mathrm{s}.
$$

Here is the same relationship in table form:

| Angle turned | Fraction of a full turn | Time required |
| --- | ---: | ---: |
| $2\pi$ | $1$ | $T$ |
| $\pi$ | $\dfrac12$ | $\dfrac12T$ |
| $\dfrac{\pi}{2}$ | $\dfrac14$ | $\dfrac14T$ |

The angle $\theta$ multiplies the time because a larger angular gap takes a larger fraction of the rotation.

```quiz
type: radio
id: q-p4-1
shuffle: true
content: |-
  A shaft has period $T=0.60\ \mathrm{s}$. How long does it take the shaft to rotate through $\theta=\pi$ radians?
options:
- id: q-p4-1-a
  content: |-
    $0.15\ \mathrm{s}$
- id: q-p4-1-b
  content: |-
    $0.30\ \mathrm{s}$
  correct: true
- id: q-p4-1-c
  content: |-
    $0.60\ \mathrm{s}$
- id: q-p4-1-d
  content: |-
    $1.20\ \mathrm{s}$
```

---

<a id="turn-rotation-time-into-bullet-speed"></a>
## Turn Rotation Time Into Bullet Speed

**Example:** Two disks are $D=1.2\ \mathrm{m}$ apart. The shaft has period $T=0.60\ \mathrm{s}$, and the holes are separated by $\theta=\pi$ radians. What bullet speed lets the bullet pass through both holes?

**Explanation**

First find the time for the shaft to rotate through the hole separation:

$$
t=\dfrac{\theta}{2\pi}T
=
\dfrac{\pi}{2\pi}(0.60\ \mathrm{s})
=
0.30\ \mathrm{s}.
$$

The bullet must travel distance $D$ during that time, so

$$
v=\dfrac{D}{t}
=
\dfrac{1.2\ \mathrm{m}}{0.30\ \mathrm{s}}
=
4.0\ \mathrm{m}/\mathrm{s}.
$$

Because the rotation time contains $\theta$, the speed formula divides by a quantity containing $\theta$.

For a numerator-or-denominator question, the unitless constant $2\pi$ is not the main issue. The key structure is

$$
v=\dfrac{D}{\text{time}},
\qquad
\text{time}\propto \theta.
$$

```quiz
type: radio
id: q-p4-2
shuffle: true
content: |-
  Two disks are $D=0.90\ \mathrm{m}$ apart. The shaft has period $T=0.40\ \mathrm{s}$, and the holes are separated by $\theta=\dfrac{\pi}{2}$ radians. What bullet speed lets the bullet pass through both holes?
options:
- id: q-p4-2-a
  content: |-
    $2.25\ \mathrm{m}/\mathrm{s}$
- id: q-p4-2-b
  content: |-
    $4.5\ \mathrm{m}/\mathrm{s}$
- id: q-p4-2-c
  content: |-
    $9.0\ \mathrm{m}/\mathrm{s}$
  correct: true
- id: q-p4-2-d
  content: |-
    $18\ \mathrm{m}/\mathrm{s}$
```

---

<a id="decide-whether-an-angle-belongs-upstairs-or-downstairs"></a>
## Decide Whether an Angle Belongs Upstairs or Downstairs

**Example:** In the same rotating-disk setup, would you expect the angular separation $\theta$ to appear in the numerator or denominator of the bullet-speed formula?

**Explanation**

Use the chain of dependence:

$$
\text{larger }\theta
\text{ with }D\text{ and }T\text{ fixed}
\quad\Longrightarrow\quad
\text{more time before the second hole lines up}
\quad\Longrightarrow\quad
\text{smaller required speed}.
$$

A variable that makes the required speed smaller belongs in the denominator. Algebra gives the same conclusion:

$$
t=\dfrac{\theta}{2\pi}T,
\qquad
v=\dfrac{D}{t}
=
\dfrac{D}{(\theta T)/(2\pi)}
=
\dfrac{2\pi D}{\theta T}.
$$

So $\theta$ belongs in the denominator.

```quiz
type: radio
id: q-p4-3
shuffle: true
content: |-
  Consider the system pictured: a bullet is shot through two holes in disks a distance $D$ apart, attached to a shaft that rotates at constant angular speed with period $T$. The angle $\theta$ describes the fixed angular separation of the holes.

  ![](<../Source/Images/bullet-through-rotating-disks.png>)

  For the formula for the bullet speed $v$ in terms of the given variables, would you expect to find $\theta$ in the numerator or denominator?

  Explain your reasoning in your submitted work.
options:
- id: q-p4-3-a
  content: |-
    numerator
- id: q-p4-3-b
  content: |-
    denominator
  correct: true
- id: q-p4-3-c
  content: |-
    neither
```

---

<a id="avoid-the-angle-trap"></a>
## Avoid the Angle Trap

**Example:** A student says, "A bigger angle means more rotation, so the bullet must move faster. Therefore $\theta$ should be in the numerator." What is the mistake?

**Explanation**

The bullet is not rotating through the angle. The disks are rotating through the angle while the bullet travels straight across the distance $D$.

A bigger $\theta$ gives the bullet more travel time before the second hole arrives. More available time means the bullet can be slower:

$$
v=\dfrac{D}{t}.
$$

So the angle is part of the time in the denominator, not part of the distance in the numerator.

```quiz
type: radio
id: q-p4-4
shuffle: true
content: |-
  In the rotating-disk setup, $\theta$ is doubled while $D$ and $T$ stay fixed. What happens to the required bullet speed?
options:
- id: q-p4-4-a
  content: |-
    It doubles, because the angle is larger.
- id: q-p4-4-b
  content: |-
    It is cut in half, because the bullet has twice as much travel time.
  correct: true
- id: q-p4-4-c
  content: |-
    It stays the same, because the disk period has not changed.
- id: q-p4-4-d
  content: |-
    It becomes zero, because the angle cancels out.
```

---

## Summary

When an angle $\theta$ is the angular separation between two rotating holes, it tells you what fraction of a full period must pass:

$$
t=\dfrac{\theta}{2\pi}T.
$$

The bullet speed is distance divided by that time:

$$
v=\dfrac{D}{t}=\dfrac{2\pi D}{\theta T}.
$$

The main trap is treating $\theta$ like extra bullet distance. In this setup, a larger $\theta$ gives the bullet more time, so $\theta$ belongs in the denominator of the speed formula.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
