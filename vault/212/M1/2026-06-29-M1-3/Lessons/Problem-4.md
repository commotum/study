# Finding the Normal Force at the Bottom of a Ferris Wheel

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

When a rider is at the bottom of a Ferris wheel, the center of the circle is above the rider. That means the required radial acceleration points upward.

The seat's normal force points upward, while gravity points downward. Since the inward direction is upward at the bottom, the radial force balance is

$$
N-mg=m\omega^2r.
$$

So the normal force is

$$
N=mg+m\omega^2r.
$$

The key cue is the word **bottom**: the seat must support the rider's weight and also provide the extra inward force needed for circular motion.

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
content: |-
  A rider is at the bottom of a Ferris wheel. Taking inward as positive, which equation correctly relates the normal force $N$ to the radial acceleration?
options:
- id: p4-q1-a
  content: |-
    $N-mg=m\omega^2r$
  correct: true
- id: p4-q1-b
  content: |-
    $mg-N=m\omega^2r$
- id: p4-q1-c
  content: |-
    $N+mg=0$
- id: p4-q1-d
  content: |-
    $N=m\omega r$
- id: p4-q1-e
  content: |-
    $mg=m\omega^2r$
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
content: |-
  A $70\ \mathrm{kg}$ rider is on a Ferris wheel with radius $30\ \mathrm{m}$ and angular speed $0.20\ \mathrm{rad}/\mathrm{s}$. What is $m\omega^2r$?
options:
- id: p4-q2-a
  content: |-
    $14\ \mathrm{N}$
- id: p4-q2-b
  content: |-
    $84\ \mathrm{N}$
  correct: true
- id: p4-q2-c
  content: |-
    $420\ \mathrm{N}$
- id: p4-q2-d
  content: |-
    $686\ \mathrm{N}$
- id: p4-q2-e
  content: |-
    $2100\ \mathrm{N}$
```

---

<a id="solve-for-the-normal-force"></a>
## Solve for the Normal Force

**Example:** A Ferris wheel has radius $42\ \mathrm{m}$ and angular velocity $0.16\ \mathrm{rad}/\mathrm{s}$. Find the magnitude of the normal force on a $68\ \mathrm{kg}$ rider at the bottom of the wheel.

**Explanation**

At the bottom, use

$$
N-mg=m\omega^2r.
$$

Solve for $N$:

$$
N=mg+m\omega^2r.
$$

Now substitute the values:

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

```quiz
type: radio
id: p4-q3
content: |-
  A $60\ \mathrm{kg}$ rider is at the bottom of a Ferris wheel with radius $25\ \mathrm{m}$ and angular speed $0.40\ \mathrm{rad}/\mathrm{s}$. Using $g=9.8\ \mathrm{m}/\mathrm{s}^2$, what is the normal force from the seat?
options:
- id: p4-q3-a
  content: |-
    $204\ \mathrm{N}$
- id: p4-q3-b
  content: |-
    $384\ \mathrm{N}$
- id: p4-q3-c
  content: |-
    $588\ \mathrm{N}$
- id: p4-q3-d
  content: |-
    $972\ \mathrm{N}$
  correct: true
- id: p4-q3-e
  content: |-
    $1176\ \mathrm{N}$
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
content: |-
  A rider is at the bottom of a Ferris wheel. Which expression gives the magnitude of the normal force from the seat?
options:
- id: p4-q4-a
  content: |-
    $N=mg-m\omega^2r$
- id: p4-q4-b
  content: |-
    $N=mg+m\omega^2r$
  correct: true
- id: p4-q4-c
  content: |-
    $N=m\omega^2r-mg$
- id: p4-q4-d
  content: |-
    $N=m\omega r+mg$
- id: p4-q4-e
  content: |-
    $N=mg$
```

---

<a id="summary"></a>
## Summary

For a rider at the bottom of a Ferris wheel:

1. The center is above the rider, so inward is upward.
2. The normal force points inward, and weight points opposite inward.
3. The radial force equation is

$$
N-mg=m\omega^2r.
$$

4. Solve for the normal force:

$$
N=mg+m\omega^2r.
$$

The main trap is using the top-of-the-wheel equation $N=mg-m\omega^2r$. At the bottom, the normal force must be larger than the rider's weight.
