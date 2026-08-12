# Finding the Normal Force at the Bottom of a Ferris Wheel

<!--
lesson-id: 212-M1-017
topic-code: MTH212.M1.17
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Radial Direction](#choose-the-radial-direction)
- [Compute the Centripetal Force Term](#compute-the-centripetal-force-term)
- [Solve for the Normal Force](#solve-for-the-normal-force)
- [Avoid the Top-Bottom Sign Mix-Up](#avoid-the-top-bottom-sign-mix-up)
- [Summary](#summary)

## Prerequisites

- Radial acceleration points toward the center of circular motion.
- For constant angular velocity, $a_r=\omega^2r$.
- Weight has magnitude $mg$ and points downward.
- Newton's second law in the radial direction is $\sum F_r=ma_r$.

---

<a id="introduction"></a>
## Introduction

A $68\ \mathrm{kg}$ rider sits in an upright gondola at the bottom of a Ferris wheel. The wheel has radius $42\ \mathrm{m}$ and rotates at $0.16\ \mathrm{rad}/\mathrm{s}$. How strongly does the seat push upward on the rider?

That upward seat force is the normal force and determines the rider's apparent weight. At the bottom, riders feel heavier than they do at rest: the center of the wheel is above them, so their acceleration is upward even though gravity pulls downward. The seat must push upward strongly enough to support their weight and still leave an upward net force.

With inward chosen as positive, the force balance is

$$
N-mg=m\omega^2r,
$$

so the normal force is

$$
N=mg+m\omega^2r.
$$

The $m\omega^2r$ term is the required net inward force, not a third force acting on the rider.

---

<a id="choose-the-radial-direction"></a>
## Choose the Radial Direction

**Example:** A $50\ \mathrm{kg}$ rider is at the bottom of a Ferris wheel. Which radial force equation should be used to find the normal force from the seat?

**Explanation**

At the bottom, the center of the wheel is above the rider, so inward is upward.

- $N$ points upward, so it is positive in the inward direction.
- $mg$ points downward, so it is negative in the inward direction.
- The radial acceleration has magnitude $\omega^2r$.

Therefore,

$$
\sum F_r=ma_r
$$

becomes

$$
N-mg=m\omega^2r.
$$

```quiz
type: radio
id: p4-q1
shuffle: true
content: |-
  A rider is at the bottom of a Ferris wheel. Taking inward as positive, which equation correctly relates the normal force $N$ to the radial acceleration?
options:
- id: p4-q1-a
  content: |-
    $N-mg=m\omega^2r$
  correct: true
  feedback: |-
    At the bottom, inward is upward, so $N$ is positive and $mg$ is negative.
- id: p4-q1-b
  content: |-
    $mg-N=m\omega^2r$
  feedback: |-
    This is the top-of-the-wheel sign pattern.
- id: p4-q1-c
  content: |-
    $N+mg=0$
  feedback: |-
    The net radial force is not zero because the rider is accelerating toward the center.
- id: p4-q1-d
  content: |-
    $N=m\omega r$
  feedback: |-
    The radial acceleration uses $\omega^2r$, not $\omega r$.
- id: p4-q1-e
  content: |-
    $mg=m\omega^2r$
  feedback: |-
    This ignores the normal force from the seat.
```

---

<a id="compute-the-centripetal-force-term"></a>
## Compute the Centripetal Force Term

**Example:** For a $68\ \mathrm{kg}$ rider on a Ferris wheel with $r=42\ \mathrm{m}$ and $\omega=0.16\ \mathrm{rad}/\mathrm{s}$, compute $m\omega^2r$.

**Explanation**

Use the radial acceleration formula $a_r=\omega^2r$:

$$
\begin{aligned}
m\omega^2r
&=68(0.16)^2(42) \\
&=68(0.0256)(42) \\
&=73.1136\ \mathrm{N}.
\end{aligned}
$$

So the extra inward force required for circular motion is about

$$
73\ \mathrm{N}.
$$

This is not the normal force yet. It is only the net inward force.

```quiz
type: radio
id: p4-q2
shuffle: true
content: |-
  A $70\ \mathrm{kg}$ rider is on a Ferris wheel with radius $30\ \mathrm{m}$ and angular speed $0.20\ \mathrm{rad}/\mathrm{s}$. What is $m\omega^2r$?
options:
- id: p4-q2-a
  content: |-
    $14\ \mathrm{N}$
  feedback: |-
    This uses $m\omega$ and misses both squaring $\omega$ and multiplying by $r$.
- id: p4-q2-b
  content: |-
    $84\ \mathrm{N}$
  correct: true
  feedback: |-
    $70(0.20)^2(30)=70(0.04)(30)=84$.
- id: p4-q2-c
  content: |-
    $420\ \mathrm{N}$
  feedback: |-
    This uses $m\omega r$ instead of $m\omega^2r$.
- id: p4-q2-d
  content: |-
    $686\ \mathrm{N}$
  feedback: |-
    This is approximately the rider's weight, not the centripetal-force term.
- id: p4-q2-e
  content: |-
    $2100\ \mathrm{N}$
  feedback: |-
    This multiplies $mr$ without the $\omega^2$ factor.
```

---

<a id="solve-for-the-normal-force"></a>
## Solve for the Normal Force

**Example:** A Ferris wheel has radius $42\ \mathrm{m}$ and angular velocity $0.16\ \mathrm{rad}/\mathrm{s}$. Find the magnitude of the normal force on a $68\ \mathrm{kg}$ rider at the bottom of the wheel.

**Explanation**

First list the quantities that matter:

- Bottom of the wheel: use $N-mg=m\omega^2r$.
- Mass: $m=68\ \mathrm{kg}$.
- Radius: $r=42\ \mathrm{m}$.
- Angular speed: $\omega=0.16\ \mathrm{rad}/\mathrm{s}$.
- Gravitational field strength: $g=9.8\ \mathrm{m}/\mathrm{s}^2$.

Before calculating, predict the result: at the bottom, the seat must support the rider against gravity and still leave an upward inward net force. Therefore $N$ must be greater than $mg$. This prediction will catch a top-of-the-wheel sign pattern used by mistake.

At the bottom, use

$$
N-mg=m\omega^2r.
$$

Solve for $N$:

$$
N=mg+m\omega^2r.
$$

Only after isolating $N$ symbolically should you substitute the values:

$$
\begin{aligned}
N
&=(68)(9.8)+(68)(0.16)^2(42) \\
&=666.4+73.1136 \\
&=739.5136\ \mathrm{N}.
\end{aligned}
$$

Rounded to two significant figures, the normal force is

$$
740\ \mathrm{N}.
$$

As predicted, this is larger than the rider's weight, $mg=666.4\ \mathrm{N}$.

```quiz
type: radio
id: p4-q3
shuffle: true
content: |-
  A $60\ \mathrm{kg}$ rider is at the bottom of a Ferris wheel with radius $25\ \mathrm{m}$ and angular speed $0.40\ \mathrm{rad}/\mathrm{s}$. Using $g=9.8\ \mathrm{m}/\mathrm{s}^2$, what is the normal force from the seat?
options:
- id: p4-q3-a
  content: |-
    $348\ \mathrm{N}$
  feedback: |-
    This subtracts the centripetal term from the weight: $588-240$.
- id: p4-q3-b
  content: |-
    $240\ \mathrm{N}$
  feedback: |-
    This is only $m\omega^2r$, not the normal force.
- id: p4-q3-c
  content: |-
    $588\ \mathrm{N}$
  feedback: |-
    This is only the rider's weight, $mg$.
- id: p4-q3-d
  content: |-
    $828\ \mathrm{N}$
  correct: true
  feedback: |-
    At the bottom, $N=mg+m\omega^2r=588+240=828\ \mathrm{N}$.
- id: p4-q3-e
  content: |-
    $1176\ \mathrm{N}$
  feedback: |-
    This doubles the weight instead of adding the centripetal-force term.
```

---

<a id="avoid-the-top-bottom-sign-mix-up"></a>
## Avoid the Top-Bottom Sign Mix-Up

**Example:** A rider has mass $68\ \mathrm{kg}$ on the same Ferris wheel with $r=42\ \mathrm{m}$ and $\omega=0.16\ \mathrm{rad}/\mathrm{s}$. How would the force equation change if the rider were at the top instead of the bottom?

**Explanation**

At the bottom, inward is upward, so

$$
N-mg=m\omega^2r
$$

and

$$
N=mg+m\omega^2r.
$$

At the top, inward is downward. Gravity points inward, but the seat's normal force points upward, away from the center. The equation becomes

$$
mg-N=m\omega^2r,
$$

so

$$
N=mg-m\omega^2r.
$$

For the bottom problem, do not subtract the centripetal term. The rider needs more normal force than their weight, not less.

```quiz
type: radio
id: p4-q4
shuffle: true
content: |-
  A rider is at the bottom of a Ferris wheel. Which expression gives the magnitude of the normal force from the seat?
options:
- id: p4-q4-a
  content: |-
    $N=mg-m\omega^2r$
  feedback: |-
    This is the top-of-the-wheel formula.
- id: p4-q4-b
  content: |-
    $N=mg+m\omega^2r$
  correct: true
  feedback: |-
    At the bottom, the seat must provide weight support plus the inward centripetal-force term.
- id: p4-q4-c
  content: |-
    $N=m\omega^2r-mg$
  feedback: |-
    This solves $N-mg=m\omega^2r$ with the sign of $mg$ moved the wrong way.
- id: p4-q4-d
  content: |-
    $N=m\omega r+mg$
  feedback: |-
    The centripetal-force term is $m\omega^2r$, not $m\omega r$.
- id: p4-q4-e
  content: |-
    $N=mg$
  feedback: |-
    This would mean zero radial acceleration, but circular motion requires an inward net force.
```

---

<a id="summary"></a>
## Summary

At the bottom of a Ferris wheel, the center is above the rider. The normal force points inward and weight points outward, so

$$
N-mg=m\omega^2r.
$$

Solving for the normal force gives

$$
N=mg+m\omega^2r.
$$

The normal force is therefore larger than the rider's weight. The subtraction $N=mg-m\omega^2r$ belongs to the top of an upright gondola, where gravity points inward instead.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Normal Force at the Top of a Ferris Wheel](Problem-5.md)

Study guide index: 18/35

---
<!-- lesson-nav:end -->
