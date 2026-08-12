# Putting Period in the Denominator for Rotating-Disk Speed

<!--
lesson-id: 212-M1-039
topic-code: MTH212.M1.39
-->

## Table of Contents

- [Introduction](#introduction)
- [Change Period Into Angular Speed](#change-period-into-angular-speed)
- [Find the Time for a Fixed Angle](#find-the-time-for-a-fixed-angle)
- [Place the Period in the Speed Formula](#place-the-period-in-the-speed-formula)
- [Check the Direction of the Relationship](#check-the-direction-of-the-relationship)
- [Summary](#summary)

## Prerequisites

- Speed is distance divided by time: $v=\dfrac{\text{distance}}{\text{time}}$.
- One full revolution is $2\pi$ radians.
- Period $T$ is the time for one full revolution.
- Angular speed is angle divided by time.

---

<a id="introduction"></a>
## Introduction

Two disks are fixed to the same rotating shaft, separated by a distance $D$. A bullet passes through a hole in the first disk and must reach the second disk just as its hole rotates into the bullet's path. The holes have a fixed angular separation $\theta$, and the shaft completes one revolution in period $T$.

![](<../Source/Images/bullet-through-rotating-disks.png>)

Should $T$ appear in the numerator or denominator of the formula for the required bullet speed?

The bullet and the shaft share the same interval $\Delta t$: while the bullet crosses the distance $D$, the shaft rotates through $\theta$. Keep this travel time distinct from the rotation period $T$. A longer period means the shaft rotates more slowly, so the second hole takes longer to reach the bullet's path. The bullet can then cover the same distance more slowly. Therefore, increasing $T$ must decrease the required bullet speed.

Before deriving anything, vary one quantity at a time. A larger disk spacing requires a faster bullet, while a larger period or a larger angular separation gives the bullet more time and requires a slower bullet:

$$
D\uparrow\Rightarrow v\uparrow,
\qquad
T\uparrow\Rightarrow v\downarrow,
\qquad
\theta\uparrow\Rightarrow v\downarrow.
$$

The final formula should therefore have the form $v\propto D/(T\theta)$, apart from a dimensionless factor.

The equations below turn that physical relationship into the speed formula, beginning with

$$
v=\dfrac{D}{\Delta t}.
$$

---

<a id="change-period-into-angular-speed"></a>
## Change Period Into Angular Speed

**Example:** A shaft completes one revolution in period $T$. What is its angular speed?

**Explanation**

One revolution is $2\pi$ radians, and the time for one revolution is $T$. Since angular speed is angle divided by time,

$$
\omega=\dfrac{2\pi}{T}.
$$

The period is in the denominator because a longer period means fewer radians per second.

```quiz
type: radio
id: p3-q1
shuffle: true
content: |-
  A wheel completes one revolution in $0.50\ \mathrm{s}$. Which expression represents its angular speed?
options:
- id: p3-q1-a
  content: |-
    $\dfrac{2\pi}{0.50}\ \mathrm{rad}/\mathrm{s}$
  correct: true
- id: p3-q1-b
  content: |-
    $2\pi(0.50)\ \mathrm{rad}/\mathrm{s}$
- id: p3-q1-c
  content: |-
    $\dfrac{0.50}{2\pi}\ \mathrm{rad}/\mathrm{s}$
```

---

<a id="find-the-time-for-a-fixed-angle"></a>
## Find the Time for a Fixed Angle

**Example:** A shaft completes one revolution in period $T$. If it must rotate through angle $\theta$, how long does that take?

**Explanation**

Think of the period $T$ as the time for one complete revolution. One complete revolution is $2\pi$ radians. For constant angular speed, the fraction of a full rotation equals the fraction of a full period:

$$
\dfrac{\text{angle rotated}}{\text{full rotation}}
=
\dfrac{\text{time needed}}{\text{time for a full rotation}}.
$$

Substitute the angle $\theta$, the full-rotation angle $2\pi$, the rotation time $\Delta t$, and the period $T$:

$$
\dfrac{\theta}{2\pi}=\dfrac{\Delta t}{T}.
$$

Multiplying both sides by $T$ gives

$$
\boxed{\Delta t=\dfrac{\theta}{2\pi}T}.
$$

The factor $\theta/(2\pi)$ is the fraction of a full turn the shaft must complete. For example, if the shaft rotates halfway around, then $\theta=\pi$ and

$$
\Delta t=\dfrac{\pi}{2\pi}T=\dfrac{T}{2}.
$$

That makes sense: half a rotation takes half a period. The main idea is

$$
\boxed{\text{rotation time}=(\text{fraction of a full turn})(T)}.
$$

This is equivalent to using $\Delta t=\theta/\omega$ with $\omega=2\pi/T$, but the proportion shows the physical relationship directly. The bullet's travel time is proportional to $T$: a slower rotation gives the bullet more time to cross from one disk to the other.

```quiz
type: radio
id: p3-q2
shuffle: true
content: |-
  A disk has period $T$ and must rotate through angle $\phi$ before the next hole lines up. Which expression gives that rotation time?
options:
- id: p3-q2-a
  content: |-
    $\dfrac{\phi T}{2\pi}$
  correct: true
- id: p3-q2-b
  content: |-
    $\dfrac{2\pi T}{\phi}$
- id: p3-q2-c
  content: |-
    $\dfrac{2\pi}{\phi T}$
```

---

<a id="place-the-period-in-the-speed-formula"></a>
## Place the Period in the Speed Formula

**Example:** A bullet travels distance $D$ while the shaft rotates through angle $\theta$. The shaft period is $T$. Where does $T$ belong in the formula for the bullet speed?

**Explanation**

The bullet speed is distance divided by travel time:

$$
v=\dfrac{D}{\Delta t}.
$$

From the previous section,

$$
\Delta t=\dfrac{\theta T}{2\pi}.
$$

So

$$
v=\dfrac{D}{\theta T/(2\pi)}
 =\dfrac{2\pi D}{\theta T}.
$$

Therefore, $T$ belongs in the denominator of the bullet-speed formula. The period first makes the travel time larger, and that whole travel time is then divided into $D$.

```quiz
type: radio
id: p3-q3
shuffle: true
content: |-
  A bullet crosses two rotating disks separated by distance $L$. The holes are separated by angle $\alpha$, and the shaft period is $P$. In the formula for the bullet speed, where should $P$ appear?
options:
- id: p3-q3-a
  content: |-
    In the numerator, because $P$ is a time and time should be multiplied by distance.
- id: p3-q3-b
  content: |-
    In the denominator, because $P$ is part of the travel time being divided into the distance.
  correct: true
- id: p3-q3-c
  content: |-
    Neither, because period cancels when converting from angle to time.
```

---

<a id="check-the-direction-of-the-relationship"></a>
## Check the Direction of the Relationship

**Example:** Two identical rotating-disk setups have the same $D$ and $\theta$. Setup A has period $T$, and Setup B has period $2T$. Which setup requires the faster bullet?

**Explanation**

Doubling the period halves the angular speed. That means the shaft takes twice as long to rotate through the same angle $\theta$. If the bullet has twice as much travel time for the same distance $D$, its required speed is half as large.

| Change | Travel time $\Delta t$ | Required speed $v$ |
| --- | ---: | ---: |
| $T\to 2T$ | $\Delta t\to 2\Delta t$ | $v\to \dfrac{v}{2}$ |

So Setup A requires the faster bullet. This direction check agrees with $T$ being in the denominator: increasing $T$ decreases $v$.

```quiz
type: radio
id: p3-q4
shuffle: true
content: |-
  In the same rotating-disk setup, suppose only the period changes from $T$ to $3T$. What should happen to the required bullet speed?
options:
- id: p3-q4-a
  content: |-
    It should triple.
- id: p3-q4-b
  content: |-
    It should become one third as large.
  correct: true
- id: p3-q4-c
  content: |-
    It should stay the same because the disk spacing did not change.
```

---

## Summary

The bullet crosses the gap during the same time that the shaft rotates through the holes' angular separation:

$$
\omega=\dfrac{2\pi}{T}, \qquad
\Delta t=\dfrac{\theta}{\omega}=\dfrac{\theta T}{2\pi}, \qquad
v=\dfrac{D}{\Delta t}=\dfrac{2\pi D}{\theta T}.
$$

The period belongs in the denominator of $v$ because increasing the period makes the rotation slower, gives the bullet more time to travel, and therefore lowers the required speed. The main trap is to treat $T$ as if it directly increases speed; it directly increases the travel time instead.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Finding the Minimum Period Before a Coin Slips](../../2026-07-05-PQ-1/Lessons/Problem-4.md)

Study guide index: 15/35

---
<!-- lesson-nav:end -->
