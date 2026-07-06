# Tangential Speed From Angular Velocity

<!--
lesson-id: 212-M1-002
topic-code: MTH212.M1.02
-->

## Table of Contents

- [Introduction](#introduction)
- [Use Radius Times Angular Velocity](#use-radius-times-angular-velocity)
- [Keep Units and Round the Product](#keep-units-and-round-the-product)
- [Avoid Radius and Diameter Traps](#avoid-radius-and-diameter-traps)
- [Summary](#summary)

## Prerequisites

- Know that radius is the distance from the center of a circle to its rim.
- Know that angular velocity in $\mathrm{rad}/\mathrm{s}$ tells how many radians the wheel turns each second.
- Be able to multiply decimals and round a numerical answer.

---

<a id="introduction"></a>
## Introduction

When a point moves around a circle at constant angular velocity, the point's linear speed along the rim is its **tangential speed**.

The cue for this calculation is that the problem gives a radius $r$ and an angular velocity $\omega$, then asks for a speed in distance per time. Use

$$
v=r\omega
$$

where $v$ is tangential speed. A radius of $r$ meters means each radian of rotation moves a rim point $r$ meters along the arc. Since a radian is a ratio of arc length to radius, it does not add a separate physical unit in the final speed.

---

<a id="use-radius-times-angular-velocity"></a>
## Use Radius Times Angular Velocity

**Example:** A Ferris wheel has radius $42\ \mathrm{m}$ and rotates at a constant angular velocity of $0.16\ \mathrm{rad}/\mathrm{s}$. What is the speed of a particle on the rim?

**Explanation**

The problem gives radius and angular velocity, so use $v=r\omega$.

$$
\begin{aligned}
v&=r\omega \\
&=(42\ \mathrm{m})(0.16\ \mathrm{rad}/\mathrm{s}) \\
&=6.72\ \mathrm{m}/\mathrm{s}
\end{aligned}
$$

So the particle's speed is $6.72\ \mathrm{m}/\mathrm{s}$, which is $6.7\ \mathrm{m}/\mathrm{s}$ to the nearest tenth.

```quiz
type: radio
id: p2-q1
shuffle: true
content: |-
  A wheel has radius $30\ \mathrm{m}$ and rotates at angular velocity $0.20\ \mathrm{rad}/\mathrm{s}$. What is the speed of a point on the rim?
options:
- id: a
  content: |-
    $1.5\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This divides $r$ by $\omega$. Tangential speed uses $v=r\omega$.
- id: b
  content: |-
    $6.0\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    Multiply radius by angular velocity: $(30)(0.20)=6.0$.
- id: c
  content: |-
    $30.2\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This adds the two given numbers instead of multiplying them.
- id: d
  content: |-
    $150\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This divides by $0.20$ instead of multiplying by $0.20$.
```

```quiz
type: radio
id: p2-q2
shuffle: true
content: |-
  A point is on the rim of a circular ride with radius $55\ \mathrm{m}$. The ride rotates at $0.10\ \mathrm{rad}/\mathrm{s}$. What is the point's speed?
options:
- id: a
  content: |-
    $5.5\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    Use $v=r\omega=(55)(0.10)=5.5$.
- id: b
  content: |-
    $0.55\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This moves the decimal one place too far.
- id: c
  content: |-
    $55.1\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This adds the given values instead of multiplying.
- id: d
  content: |-
    $550\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This divides by $0.10$ instead of multiplying by $0.10$.
```

---

<a id="keep-units-and-round-the-product"></a>
## Keep Units and Round the Product

**Example:** A rotating platform has radius $18\ \mathrm{m}$ and angular velocity $0.35\ \mathrm{rad}/\mathrm{s}$. Find the rim speed to the nearest tenth.

**Explanation**

Start with the same formula.

$$
\begin{aligned}
v&=r\omega \\
&=(18\ \mathrm{m})(0.35\ \mathrm{rad}/\mathrm{s}) \\
&=(18)(0.35)\ \mathrm{m}/\mathrm{s} \\
&=6.30\ \mathrm{m}/\mathrm{s}
\end{aligned}
$$

The unit is meters per second because radius contributes meters and angular velocity contributes per second. Rounding $6.30$ to the nearest tenth gives

$$
6.3\ \mathrm{m}/\mathrm{s}.
$$

```quiz
type: radio
id: p2-q3
shuffle: true
content: |-
  A Ferris wheel has radius $24\ \mathrm{m}$ and angular velocity $0.18\ \mathrm{rad}/\mathrm{s}$. What is the rim speed to the nearest tenth?
options:
- id: a
  content: |-
    $4.3\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    $(24)(0.18)=4.32$, which rounds to $4.3$.
- id: b
  content: |-
    $4.32\ \mathrm{rad}/\mathrm{s}$
  feedback: |-
    The number is right before rounding, but speed should be in $\mathrm{m}/\mathrm{s}$.
- id: c
  content: |-
    $13.3\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This divides $24$ by $0.18$ instead of multiplying.
- id: d
  content: |-
    $24.2\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This adds the given values instead of using $v=r\omega$.
```

---

<a id="avoid-radius-and-diameter-traps"></a>
## Avoid Radius and Diameter Traps

**Example:** A wheel has diameter $50\ \mathrm{m}$ and angular velocity $0.12\ \mathrm{rad}/\mathrm{s}$. What is the speed of a point on the rim?

**Explanation**

The formula $v=r\omega$ uses radius, not diameter. First divide the diameter by $2$.

$$
r=\frac{50}{2}=25\ \mathrm{m}
$$

Then multiply by angular velocity.

$$
\begin{aligned}
v&=r\omega \\
&=(25\ \mathrm{m})(0.12\ \mathrm{rad}/\mathrm{s}) \\
&=3.0\ \mathrm{m}/\mathrm{s}
\end{aligned}
$$

```quiz
type: radio
id: p2-q4
shuffle: true
content: |-
  A wheel has diameter $64\ \mathrm{m}$ and angular velocity $0.15\ \mathrm{rad}/\mathrm{s}$. What is the speed of a point on the rim?
options:
- id: a
  content: |-
    $4.8\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    The radius is $32\ \mathrm{m}$, so $v=(32)(0.15)=4.8$.
- id: b
  content: |-
    $9.6\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This uses the diameter as if it were the radius.
- id: c
  content: |-
    $32.15\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This adds the radius and angular velocity instead of multiplying.
- id: d
  content: |-
    $213\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This divides the radius by angular velocity instead of multiplying.
```

---

<a id="summary"></a>
## Summary

When a circular-motion problem gives radius and angular velocity, and asks for speed along the rim, use

$$
v=r\omega.
$$

Multiply the radius by the angular velocity, keep the final unit as distance per time, and round only after the multiplication. The main trap is using diameter in place of radius.

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Ranking Radial Accelerations](<../../2026-06-25-M1-2/Lessons/Problem-6.md>)

Study guide index: 02/30

<!-- study-guide-nav:end -->
