# Comparing Ferris Wheel Normal Forces

<!--
lesson-id: 212-M1-016
topic-code: MTH212.M1.16
-->

## Table of Contents

- [Introduction](#introduction)
- [Aim the Radial Equation Inward](#aim-the-radial-equation-inward)
- [Top of the Wheel](#top-of-the-wheel)
- [Bottom of the Wheel](#bottom-of-the-wheel)
- [Compare the Two Normal Forces](#compare-the-two-normal-forces)
- [Summary](#summary)

## Prerequisites

- Draw a free-body diagram with weight $mg$ downward and a seat's normal force perpendicular to the seat.
- Use radial acceleration $a_r=\frac{v^2}{r}$ for motion at constant speed around a circle.
- Solve a two-term force equation for an unknown force.

---

<a id="introduction"></a>
## Introduction

Riders often feel lighter at the top of a Ferris wheel and heavier at the bottom, even though their mass and the force of gravity have not changed. What changes is how strongly the seat pushes on them. This supporting force—the normal force—is the rider's apparent weight.

A person rides in an upright Ferris-wheel gondola while the wheel rotates at constant angular speed. How does the seat's normal force at the top compare with its normal force at the bottom?

![](<../Source/Images/ferris-wheel-top-bottom-normal-force.png>)

At the top, the center of the wheel is below the rider. Gravity points toward the center and supplies part of the required downward net force, so the seat pushes upward less strongly than it would at rest. At the bottom, the center is above the rider. The seat must push upward strongly enough both to oppose gravity and to produce an upward net force. The radial equations below make this difference precise.

---

<a id="aim-the-radial-equation-inward"></a>
## Aim the Radial Equation Inward

**Example:** A rider moves at constant speed on a vertical circle. What should the radial side of Newton's second law equal at the top or bottom of the circle?

**Explanation**

For circular motion, the radial acceleration points toward the center and has magnitude $\frac{v^2}{r}$. If we choose the inward direction as positive, then both the top and bottom equations use

$$
\sum F_r=m a_r=m\frac{v^2}{r}.
$$

Only the force signs change from top to bottom, because "inward" points downward at the top and upward at the bottom.

| Position | Inward direction | Force pointing inward |
| --- | --- | --- |
| Top | Downward | $mg$ |
| Bottom | Upward | $N_{\mathrm{bottom}}$ |

```quiz
type: radio
id: normal-force-top-bottom-q1
shuffle: true
content: |-
  A rider is at the bottom of a Ferris wheel. Which direction is inward, toward the center of the circle?
options:
- id: q1-a
  content: |-
    Upward
  correct: true
  feedback: |-
    At the bottom, the center of the circle is above the rider.
- id: q1-b
  content: |-
    Downward
  feedback: |-
    Downward points away from the center at the bottom.
- id: q1-c
  content: |-
    Tangent to the wheel
  feedback: |-
    The radial direction points toward the center, not along the motion.
- id: q1-d
  content: |-
    Horizontally outward
  feedback: |-
    Outward is opposite the radial acceleration.
```

---

<a id="top-of-the-wheel"></a>
## Top of the Wheel

**Example:** At the top of the Ferris wheel, write the equation for $N_{\mathrm{top}}$.

**Explanation**

At the top, inward points downward. Weight $mg$ points inward, while the seat's normal force $N_{\mathrm{top}}$ points upward, away from the center.

So the radial force equation is

$$
mg-N_{\mathrm{top}}=m a_r=m\frac{v^2}{r}.
$$

Solving for the normal force gives

$$
N_{\mathrm{top}}=mg-m\frac{v^2}{r}.
$$

Gravity already supplies part of the needed inward force, so the seat does not need to push as hard at the top.

```quiz
type: radio
id: normal-force-top-bottom-q2
shuffle: true
content: |-
  At the top of a Ferris wheel, inward is downward. Which equation correctly describes the rider's radial force balance?
options:
- id: q2-a
  content: |-
    $mg-N_{\mathrm{top}}=m a_r=m\frac{v^2}{r}$
  correct: true
  feedback: |-
    Weight points inward and the normal force points away from the center.
- id: q2-b
  content: |-
    $N_{\mathrm{top}}-mg=m\frac{v^2}{r}$
  feedback: |-
    This gives the bottom equation, where inward is upward.
- id: q2-c
  content: |-
    $N_{\mathrm{top}}+mg=0$
  feedback: |-
    The rider has radial acceleration, so the net radial force is not zero.
- id: q2-d
  content: |-
    $N_{\mathrm{top}}=mg+m\frac{v^2}{r}$
  feedback: |-
    That makes the top normal force larger than weight, but gravity is already helping at the top.
```

---

<a id="bottom-of-the-wheel"></a>
## Bottom of the Wheel

**Example:** At the bottom of the Ferris wheel, write the equation for $N_{\mathrm{bottom}}$.

**Explanation**

At the bottom, inward points upward. The normal force $N_{\mathrm{bottom}}$ points inward, while weight $mg$ points downward, away from the center.

So the radial force equation is

$$
N_{\mathrm{bottom}}-mg=m a_r=m\frac{v^2}{r}.
$$

Solving for the normal force gives

$$
N_{\mathrm{bottom}}=mg+m\frac{v^2}{r}.
$$

The seat must both overcome weight and provide the inward acceleration, so the bottom normal force is larger than $mg$.

```quiz
type: radio
id: normal-force-top-bottom-q3
shuffle: true
content: |-
  At the bottom of a Ferris wheel, which expression gives the normal force from the seat on the rider?
options:
- id: q3-a
  content: |-
    $N_{\mathrm{bottom}}=mg-m\frac{v^2}{r}$
  feedback: |-
    That is the top result, where gravity points inward.
- id: q3-b
  content: |-
    $N_{\mathrm{bottom}}=m\frac{v^2}{r}-mg$
  feedback: |-
    This subtracts weight in the wrong step after $N_{\mathrm{bottom}}-mg=m a_r=m\frac{v^2}{r}$.
- id: q3-c
  content: |-
    $N_{\mathrm{bottom}}=mg+m\frac{v^2}{r}$
  correct: true
  feedback: |-
    At the bottom, the normal force must exceed weight by the needed inward net force.
- id: q3-d
  content: |-
    $N_{\mathrm{bottom}}=mg$
  feedback: |-
    That would give zero radial acceleration.
```

---

<a id="compare-the-two-normal-forces"></a>
## Compare the Two Normal Forces

**Example:** A person rides a Ferris wheel at constant angular speed. Compare the magnitude of the normal force at the top with the magnitude at the bottom.

**Explanation**

Use the two solved expressions:

$$
N_{\mathrm{top}}=mg-m\frac{v^2}{r}
$$

and

$$
N_{\mathrm{bottom}}=mg+m\frac{v^2}{r}.
$$

For a rotating wheel, the inward net-force term $m\frac{v^2}{r}$ is positive. That means $N_{\mathrm{top}}$ is $mg$ minus a positive amount, while $N_{\mathrm{bottom}}$ is $mg$ plus the same positive amount. Therefore,

$$
N_{\mathrm{top}}<N_{\mathrm{bottom}}.
$$

The normal force is also the rider's apparent weight. Gravity already supplies part of the inward force at the top, so the seat pushes less strongly; at the bottom, the seat must overcome gravity and still leave an inward net force. This gives the stronger check

$$
N_{\mathrm{bottom}}>mg>N_{\mathrm{top}}.
$$

There is no extra upward force lifting the rider at the top. The rider tends to continue along the instantaneous tangent while the wheel curves beneath them. If an algebraic result violates the ordering above for an upright gondola, recheck the inward direction and the force signs.

If angular speed is given instead of speed, use $v=r\omega$, so $\frac{v^2}{r}=r\omega^2$. The comparison stays the same:

$$
N_{\mathrm{top}}=m(g-\omega^2 r),\qquad N_{\mathrm{bottom}}=m(g+\omega^2 r).
$$

```quiz
type: radio
id: normal-force-top-bottom-q4
shuffle: true
content: |-
  A person is riding on a Ferris wheel which is rotating at constant angular speed. How does the magnitude of the normal force of the Ferris wheel on the person at the top compare to the magnitude of the normal force of the wheel on the person at the bottom?
options:
- id: q4-a
  content: |-
    $N_{\mathrm{top}} > N_{\mathrm{bottom}}$
  feedback: |-
    This reverses the signs: the inward net-force term is subtracted at the top and added at the bottom.
- id: q4-b
  content: |-
    $N_{\mathrm{top}} = N_{\mathrm{bottom}}$
  feedback: |-
    Constant speed keeps the size of $\frac{v^2}{r}$ the same, but the force signs change at the top and bottom.
- id: q4-c
  content: |-
    $N_{\mathrm{top}} < N_{\mathrm{bottom}}$
  correct: true
  feedback: |-
    At the top gravity helps provide the inward force; at the bottom the seat must exceed weight.
```

---

<a id="summary"></a>
## Summary

At the top of an upright Ferris-wheel gondola, gravity points inward while the seat's normal force points outward, so

$$
mg-N_{\mathrm{top}}=m a_r=m\frac{v^2}{r}
$$

and

$$
N_{\mathrm{top}}=mg-m\frac{v^2}{r}.
$$

At the bottom, the directions reverse:

$$
N_{\mathrm{bottom}}-mg=m a_r=m\frac{v^2}{r}
$$

and

$$
N_{\mathrm{bottom}}=mg+m\frac{v^2}{r}.
$$

Constant speed gives the same value of $\frac{v^2}{r}$ at both positions, but it does not make the normal forces equal. Gravity helps supply the inward net force at the top; at the bottom, the seat must overcome gravity before producing that same inward net force. Thus $N_{\mathrm{top}}<N_{\mathrm{bottom}}$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Finding the Normal Force at the Bottom of a Ferris Wheel](Problem-4.md)

Study guide index: 17/35

---
<!-- lesson-nav:end -->
