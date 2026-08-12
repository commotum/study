# Revolutions While A Disk Stops

<!--
lesson-id: 212-M1-036
topic-code: MTH212.M1.36
-->

## Table of Contents

- [Introduction](#introduction)
- [Read The Stopping Cue](#read-the-stopping-cue)
- [Find The Angular Displacement](#find-the-angular-displacement)
- [Convert Radians To Revolutions](#convert-radians-to-revolutions)
- [Avoid The Constant-Speed Trap](#avoid-the-constant-speed-trap)
- [Summary](#summary)

## Prerequisites

- Know that angular velocity is measured in radians per second.
- Know that constant angular acceleration makes angular velocity change at a constant rate.
- Know that one full revolution is $2\pi$ radians.

---

<a id="introduction"></a>
## Introduction

When a rotating object starts with angular velocity, comes to a stop, and has constant angular acceleration, its angular velocity decreases linearly from the starting value to $0$. The angular displacement is the area under the angular-velocity-versus-time graph.

To find how many revolutions the object makes while stopping, find the average angular velocity, multiply by the stopping time to get angular displacement in radians, and then convert radians to revolutions.

The cue is the phrase "comes to a stop" together with "constant angular acceleration." That tells you the final angular velocity is $0$ and the average angular velocity is halfway between the initial and final values.

---

<a id="read-the-stopping-cue"></a>
## Read The Stopping Cue

**Example:** A wheel starts at $10\ \mathrm{rad}/\mathrm{s}$ and comes to a stop in $8\ \mathrm{s}$ with constant angular acceleration. What average angular velocity should be used during the stop?

**Explanation**

The wheel starts with

$$
\omega_0=10\ \mathrm{rad}/\mathrm{s}
$$

and comes to a stop, so

$$
\omega_f=0.
$$

With constant angular acceleration, angular velocity changes linearly. The average angular velocity is the average of the starting and ending values:

$$
\omega_{\mathrm{avg}}=\frac{\omega_0+\omega_f}{2}
=\frac{10+0}{2}
=5\ \mathrm{rad}/\mathrm{s}.
$$

This is the same as using the area of the triangle under the $\omega$-versus-$t$ graph: the height is $10\ \mathrm{rad}/\mathrm{s}$, the base is $8\ \mathrm{s}$, and the factor $\frac{1}{2}$ comes from the steady drop to zero.

```quiz
type: radio
id: p4-q1
shuffle: true
content: |-
  A disk starts at $18\ \mathrm{rad}/\mathrm{s}$ and comes to a stop with constant angular acceleration. What average angular velocity should be used while it stops?
options:
- id: p4-q1-a
  content: |-
    $18\ \mathrm{rad}/\mathrm{s}$
- id: p4-q1-b
  content: |-
    $9\ \mathrm{rad}/\mathrm{s}$
  correct: true
- id: p4-q1-c
  content: |-
    $0\ \mathrm{rad}/\mathrm{s}$
- id: p4-q1-d
  content: |-
    $36\ \mathrm{rad}/\mathrm{s}$
```

---

<a id="find-the-angular-displacement"></a>
## Find The Angular Displacement

**Example:** A disk starts at $10\ \mathrm{rad}/\mathrm{s}$ and stops in $8\ \mathrm{s}$ with constant angular acceleration. How many radians does it turn through while stopping?

**Explanation**

From the previous section, the average angular velocity is

$$
\omega_{\mathrm{avg}}=5\ \mathrm{rad}/\mathrm{s}.
$$

Angular displacement is average angular velocity times time:

$$
\Delta\theta=\omega_{\mathrm{avg}}t.
$$

Substitute the values:

$$
\Delta\theta=(5\ \mathrm{rad}/\mathrm{s})(8\ \mathrm{s})=40\ \mathrm{rad}.
$$

Equivalently, for a constant stop from $\omega_0$ to $0$,

$$
\Delta\theta=\frac{1}{2}\omega_0t.
$$

```quiz
type: radio
id: p4-q2
shuffle: true
content: |-
  A disk starts at $14\ \mathrm{rad}/\mathrm{s}$ and stops in $12\ \mathrm{s}$ with constant angular acceleration. What is its angular displacement while stopping?
options:
- id: p4-q2-a
  content: |-
    $168\ \mathrm{rad}$
- id: p4-q2-b
  content: |-
    $84\ \mathrm{rad}$
  correct: true
- id: p4-q2-c
  content: |-
    $7\ \mathrm{rad}$
- id: p4-q2-d
  content: |-
    $26\ \mathrm{rad}$
```

---

<a id="convert-radians-to-revolutions"></a>
## Convert Radians To Revolutions

**Example:** A disk turns through $40\ \mathrm{rad}$ while stopping. How many revolutions is this, to two significant figures?

**Explanation**

One revolution is $2\pi$ radians:

$$
1\ \mathrm{rev}=2\pi\ \mathrm{rad}.
$$

Use a conversion factor that cancels radians:

$$
n_{\mathrm{rev}}
=40\ \mathrm{rad}\cdot \frac{1\ \mathrm{rev}}{2\pi\ \mathrm{rad}}
\approx 6.4\ \mathrm{rev}.
$$

```quiz
type: radio
id: p4-q3
shuffle: true
content: |-
  A disk turns through $156\ \mathrm{rad}$ while stopping. How many revolutions is this, to two significant figures?
options:
- id: p4-q3-a
  content: |-
    $25\ \mathrm{rev}$
  correct: true
- id: p4-q3-b
  content: |-
    $50\ \mathrm{rev}$
- id: p4-q3-c
  content: |-
    $156\ \mathrm{rev}$
- id: p4-q3-d
  content: |-
    $12\ \mathrm{rev}$
```

---

<a id="avoid-the-constant-speed-trap"></a>
## Avoid The Constant-Speed Trap

**Example:** A disk is spinning at $12\ \mathrm{rad}/\mathrm{s}$ and comes to a stop in $26\ \mathrm{s}$ with constant angular acceleration. How many revolutions does it make as it stops?

**Explanation**

Because the disk stops, its final angular velocity is

$$
\omega_f=0.
$$

Use the average angular velocity, not the initial angular velocity:

$$
\omega_{\mathrm{avg}}=\frac{12+0}{2}=6\ \mathrm{rad}/\mathrm{s}.
$$

Then find the angular displacement:

$$
\begin{aligned}
\Delta\theta
&=\omega_{\mathrm{avg}}t \\
&=(6\ \mathrm{rad}/\mathrm{s})(26\ \mathrm{s}) \\
&=156\ \mathrm{rad}.
\end{aligned}
$$

Convert radians to revolutions:

$$
\begin{aligned}
n_{\mathrm{rev}}
&=156\ \mathrm{rad}\cdot \frac{1\ \mathrm{rev}}{2\pi\ \mathrm{rad}} \\
&\approx 24.8\ \mathrm{rev}.
\end{aligned}
$$

To two significant figures, the disk makes

$$
25\ \mathrm{rev}.
$$

The common trap is multiplying $12$ by $26$ as if the disk kept spinning at $12\ \mathrm{rad}/\mathrm{s}$ the whole time. That would double the angular displacement because it ignores the slowdown.

```quiz
type: radio
id: p4-q4
shuffle: true
content: |-
  A disk is spinning at $16\ \mathrm{rad}/\mathrm{s}$ and comes to a stop in $10\ \mathrm{s}$ with constant angular acceleration. How many revolutions does it make as it stops, to two significant figures?
options:
- id: p4-q4-a
  content: |-
    $25\ \mathrm{rev}$
- id: p4-q4-b
  content: |-
    $13\ \mathrm{rev}$
  correct: true
- id: p4-q4-c
  content: |-
    $80\ \mathrm{rev}$
- id: p4-q4-d
  content: |-
    $6.4\ \mathrm{rev}$
```

---

## Summary

For a constant-angular-acceleration stop, the final angular velocity is $0$, so

$$
\omega_{\mathrm{avg}}=\frac{\omega_0+0}{2}.
$$

Then compute

$$
\Delta\theta=\omega_{\mathrm{avg}}t
$$

and convert radians to revolutions with

$$
n_{\mathrm{rev}}=\frac{\Delta\theta}{2\pi}.
$$

The reusable checklist is:

- "Comes to a stop" means $\omega_f=0$.
- Constant angular acceleration makes the $\omega$-versus-$t$ graph a straight line.
- The angular displacement is $\omega_{\mathrm{avg}}t$ or, for a stop, $\frac{1}{2}\omega_0t$.
- Convert radians to revolutions with $\frac{1\ \mathrm{rev}}{2\pi\ \mathrm{rad}}$.

The main trap is using $\omega_0t$ as if the disk never slowed down. For a uniform stop, that gives twice the correct angular displacement.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
