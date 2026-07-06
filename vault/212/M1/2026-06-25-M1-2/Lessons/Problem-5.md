# Bullet Speed from Rotating Disk Alignment

## Table of Contents

- [Introduction](#introduction)
- [Turn Angular Separation Into Flight Time](#turn-angular-separation-into-flight-time)
- [Use Flight Time to Find Speed](#use-flight-time-to-find-speed)
- [Build the Symbolic Formula](#build-the-symbolic-formula)
- [Substitute the Given Values](#substitute-the-given-values)
- [Avoid the Full-Period Trap](#avoid-the-full-period-trap)
- [Summary](#summary)

## Prerequisites

- Constant speed means $v=\dfrac{\text{distance}}{\text{time}}$.
- One full rotation is $2\pi$ radians.
- A period $T$ is the time for one full rotation.

---

<a id="introduction"></a>
## Introduction

A bullet passes through two disks attached to the same rotating shaft. The disks are separated by distance $D$, and the holes are separated by an angle $\theta$ around the shaft.

![](<../Source/Images/bullet-through-rotating-disks.png>)

The useful cue is that the bullet travels from the first disk to the second while the shaft turns through the angle between the holes. Convert that angular turn into a flight time, then use $v=\dfrac{D}{\Delta t}$. For this problem, the stated angle $\theta$ is the rotation during the bullet's flight.

---

<a id="turn-angular-separation-into-flight-time"></a>
## Turn Angular Separation Into Flight Time

**Example:** A shaft has period $T=0.30\ \mathrm{s}$. Two holes are separated by $\theta=\dfrac{\pi}{4}$ radians. How long does it take the shaft to rotate through that angle?

**Explanation**

One full rotation is $2\pi$ radians and takes $T$ seconds. The angle $\theta$ is the fraction

$$
\dfrac{\theta}{2\pi}
$$

of a full rotation. So the matching time is

$$
\Delta t=\dfrac{\theta}{2\pi}T.
$$

This is the whole move: time for part of a rotation equals the fraction of the rotation times the time for a full rotation.

Substitute the values:

$$
\begin{aligned}
\Delta t
&=\dfrac{\pi/4}{2\pi}(0.30) \\
&=\dfrac{1}{8}(0.30) \\
&=0.0375\ \mathrm{s}.
\end{aligned}
$$

```quiz
type: radio
id: q-flight-time
content: |-
  A rotating shaft has period $T=0.40\ \mathrm{s}$. Two holes are separated by $\theta=\dfrac{\pi}{5}$ radians. What is the time for the shaft to rotate through that angle?
options:
- id: a
  content: |-
    $0.040\ \mathrm{s}$
  correct: true
- id: b
  content: |-
    $0.080\ \mathrm{s}$
- id: c
  content: |-
    $0.20\ \mathrm{s}$
- id: d
  content: |-
    $0.40\ \mathrm{s}$
- id: e
  content: |-
    $2.0\ \mathrm{s}$
```

---

<a id="use-flight-time-to-find-speed"></a>
## Use Flight Time to Find Speed

**Example:** Two rotating disks are $D=1.2\ \mathrm{m}$ apart. The shaft period is $T=0.30\ \mathrm{s}$, and the hole separation is $\theta=\dfrac{\pi}{4}$. Find the bullet speed.

**Explanation**

From the previous calculation, the flight time is

$$
\Delta t=0.0375\ \mathrm{s}.
$$

The bullet travels distance $D$ during that time, so

$$
\begin{aligned}
v&=\dfrac{D}{\Delta t} \\
&=\dfrac{1.2}{0.0375} \\
&=32\ \mathrm{m/s}.
\end{aligned}
$$

The unit check is meters divided by seconds, so the result should be in $\mathrm{m/s}$.

```quiz
type: radio
id: q-use-flight-time
content: |-
  Two rotating disks are $D=0.90\ \mathrm{m}$ apart. The shaft period is $T=0.40\ \mathrm{s}$, and the holes are separated by $\theta=\dfrac{\pi}{5}$. Using $\Delta t=0.040\ \mathrm{s}$, what is the bullet speed?
options:
- id: a
  content: |-
    $0.036\ \mathrm{m/s}$
- id: b
  content: |-
    $2.25\ \mathrm{m/s}$
- id: c
  content: |-
    $9.0\ \mathrm{m/s}$
- id: d
  content: |-
    $22.5\ \mathrm{m/s}$
  correct: true
- id: e
  content: |-
    $36.0\ \mathrm{m/s}$
```

---

<a id="build-the-symbolic-formula"></a>
## Build the Symbolic Formula

**Example:** Write a formula for the bullet speed using the disk separation $D$, angular separation $\theta$, and shaft period $T$.

**Explanation**

First write the flight time:

$$
\Delta t=\dfrac{\theta}{2\pi}T=\dfrac{\theta T}{2\pi}.
$$

Then divide the disk separation by that time:

$$
\begin{aligned}
v&=\dfrac{D}{\Delta t} \\
&=\dfrac{D}{\theta T/(2\pi)} \\
&=\dfrac{2\pi D}{\theta T}.
\end{aligned}
$$

The fraction flips because $D$ is divided by $\dfrac{\theta T}{2\pi}$.

```quiz
type: radio
id: q-symbolic-formula
content: |-
  A bullet travels distance $D$ while a shaft with period $T$ rotates through angle $\theta$. Which formula gives the bullet speed?
options:
- id: a
  content: |-
    $v=\dfrac{D\theta T}{2\pi}$
- id: b
  content: |-
    $v=\dfrac{2\pi D}{\theta T}$
  correct: true
- id: c
  content: |-
    $v=\dfrac{D\theta}{2\pi T}$
- id: d
  content: |-
    $v=\dfrac{\theta T}{2\pi D}$
- id: e
  content: |-
    $v=\dfrac{2\pi\theta}{DT}$
```

---

<a id="substitute-the-given-values"></a>
## Substitute the Given Values

**Example:** For the assignment values $D=0.86\ \mathrm{m}$, $\theta=\dfrac{\pi}{6}$, and $T=0.22\ \mathrm{s}$, find the bullet speed.

**Explanation**

Use

$$
v=\dfrac{2\pi D}{\theta T}.
$$

Then substitute:

$$
\begin{aligned}
v
&=\dfrac{2\pi(0.86)}{(\pi/6)(0.22)} \\
&=\dfrac{2(0.86)(6)}{0.22} \\
&=\dfrac{10.32}{0.22} \\
&\approx 46.9\ \mathrm{m/s}.
\end{aligned}
$$

Rounded to two significant figures, the bullet speed is

$$
v\approx 47\ \mathrm{m/s}.
$$

```quiz
type: radio
id: q-substitute-values
content: |-
  Two disks are $D=0.75\ \mathrm{m}$ apart. The hole separation is $\theta=\dfrac{\pi}{3}$, and the shaft period is $T=0.25\ \mathrm{s}$. What is $v=\dfrac{2\pi D}{\theta T}$?
options:
- id: a
  content: |-
    $4.5\ \mathrm{m/s}$
- id: b
  content: |-
    $9.0\ \mathrm{m/s}$
- id: c
  content: |-
    $18\ \mathrm{m/s}$
  correct: true
- id: d
  content: |-
    $24\ \mathrm{m/s}$
- id: e
  content: |-
    $57\ \mathrm{m/s}$
```

---

<a id="avoid-the-full-period-trap"></a>
## Avoid the Full-Period Trap

**Example:** Why is $v=\dfrac{D}{T}$ not the right setup for the assignment values?

**Explanation**

The period $T$ is the time for a full rotation. The bullet does not need the shaft to make a full rotation; it needs the shaft to turn only through the hole separation $\theta$.

For $\theta=\dfrac{\pi}{6}$,

$$
\dfrac{\theta}{2\pi}=\dfrac{\pi/6}{2\pi}=\dfrac{1}{12}.
$$

So the bullet's flight time is only

$$
\Delta t=\dfrac{1}{12}T,
$$

not $T$. Using $D/T$ would make the time too large and the speed too small.

Only include extra full rotations if the problem explicitly says the bullet waits through one or more additional alignments. Otherwise, use the stated separation angle.

```quiz
type: radio
id: q-full-period-trap
content: |-
  Two disks are $D=3.0\ \mathrm{m}$ apart. The shaft period is $T=0.60\ \mathrm{s}$, and the holes are separated by $\theta=\dfrac{\pi}{2}$. Which calculation correctly finds the bullet speed?
options:
- id: a
  content: |-
    $v=\dfrac{3.0}{0.60}=5.0\ \mathrm{m/s}$ because the period is always the flight time.
- id: b
  content: |-
    $v=\dfrac{3.0}{0.15}=20\ \mathrm{m/s}$ because $\dfrac{\pi/2}{2\pi}=\dfrac14$, so $\Delta t=\dfrac14(0.60)=0.15\ \mathrm{s}$.
  correct: true
- id: c
  content: |-
    $v=\dfrac{0.60}{3.0}=0.20\ \mathrm{s/m}$ because speed is time divided by distance.
- id: d
  content: |-
    $v=\dfrac{3.0}{2\pi(0.60)}\approx 0.80\ \mathrm{m/s}$ because every angle adds a factor of $2\pi$ to the time.
- id: e
  content: |-
    $v=3.0(0.60)=1.8\ \mathrm{m/s}$ because distance and period should be multiplied.
```

---

<a id="summary"></a>
## Summary

When a rotating shaft has period $T$, an angular turn of $\theta$ radians takes the fraction $\dfrac{\theta}{2\pi}$ of one period:

$$
\Delta t=\dfrac{\theta T}{2\pi}.
$$

For a bullet traveling distance $D$ during that time,

$$
v=\dfrac{D}{\Delta t}=\dfrac{2\pi D}{\theta T}.
$$

Use this checklist:

- Identify the angular turn during flight: $\theta$.
- Convert it to a fraction of a full rotation: $\dfrac{\theta}{2\pi}$.
- Multiply by the period: $\Delta t=\dfrac{\theta T}{2\pi}$.
- Divide distance by flight time: $v=\dfrac{2\pi D}{\theta T}$.

The main trap is using the full period $T$ as the flight time. Use $T$ only after scaling it by the fraction of a rotation.
