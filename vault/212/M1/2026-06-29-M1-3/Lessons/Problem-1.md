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
- Use centripetal acceleration $a_r=\frac{v^2}{r}$ for motion at constant speed around a circle.
- Solve a two-term force equation for an unknown force.

---

<a id="introduction"></a>
## Introduction

In a Ferris-wheel comparison, the cue is that the rider is at the **top** or **bottom** of vertical circular motion. The task is to compare $N_{\text{top}}$ and $N_{\text{bottom}}$ by writing Newton's second law in the inward radial direction.

![](<../Source/Images/ferris-wheel-top-bottom-normal-force.png>)

The center of the circle is below the rider at the top and above the rider at the bottom. That one direction change decides whether gravity helps or opposes the seat's normal force.

Use the same three steps each time:

1. Point the positive radial direction inward.
2. Give each force a plus or minus sign based on whether it points inward.
3. Solve for the normal force and compare it with $mg$.

---

<a id="aim-the-radial-equation-inward"></a>
## Aim the Radial Equation Inward

**Example:** A rider moves at constant speed on a vertical circle. What should the radial side of Newton's second law equal at the top or bottom of the circle?

**Explanation**

For circular motion, the radial acceleration points toward the center and has magnitude $\frac{v^2}{r}$. If we choose the inward direction as positive, then both the top and bottom equations use

$$
\sum F_r=m\frac{v^2}{r}.
$$

Only the force signs change from top to bottom, because "inward" points downward at the top and upward at the bottom.

| Position | Inward direction | Force pointing inward |
| --- | --- | --- |
| Top | Downward | $mg$ |
| Bottom | Upward | $N_{\text{bottom}}$ |

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
    Outward is opposite the centripetal acceleration.
```

---

<a id="top-of-the-wheel"></a>
## Top of the Wheel

**Example:** At the top of the Ferris wheel, write the equation for $N_{\text{top}}$.

**Explanation**

At the top, inward points downward. Weight $mg$ points inward, while the seat's normal force $N_{\text{top}}$ points upward, away from the center.

So the radial force equation is

$$
mg-N_{\text{top}}=m\frac{v^2}{r}.
$$

Solving for the normal force gives

$$
N_{\text{top}}=mg-m\frac{v^2}{r}.
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
    $mg-N_{\text{top}}=m\frac{v^2}{r}$
  correct: true
  feedback: |-
    Weight points inward and the normal force points away from the center.
- id: q2-b
  content: |-
    $N_{\text{top}}-mg=m\frac{v^2}{r}$
  feedback: |-
    This gives the bottom equation, where inward is upward.
- id: q2-c
  content: |-
    $N_{\text{top}}+mg=0$
  feedback: |-
    The rider has radial acceleration, so the net radial force is not zero.
- id: q2-d
  content: |-
    $N_{\text{top}}=mg+m\frac{v^2}{r}$
  feedback: |-
    That makes the top normal force larger than weight, but gravity is already helping at the top.
```

---

<a id="bottom-of-the-wheel"></a>
## Bottom of the Wheel

**Example:** At the bottom of the Ferris wheel, write the equation for $N_{\text{bottom}}$.

**Explanation**

At the bottom, inward points upward. The normal force $N_{\text{bottom}}$ points inward, while weight $mg$ points downward, away from the center.

So the radial force equation is

$$
N_{\text{bottom}}-mg=m\frac{v^2}{r}.
$$

Solving for the normal force gives

$$
N_{\text{bottom}}=mg+m\frac{v^2}{r}.
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
    $N_{\text{bottom}}=mg-m\frac{v^2}{r}$
  feedback: |-
    That is the top result, where gravity points inward.
- id: q3-b
  content: |-
    $N_{\text{bottom}}=m\frac{v^2}{r}-mg$
  feedback: |-
    This subtracts weight in the wrong step after $N_{\text{bottom}}-mg=m\frac{v^2}{r}$.
- id: q3-c
  content: |-
    $N_{\text{bottom}}=mg+m\frac{v^2}{r}$
  correct: true
  feedback: |-
    At the bottom, the normal force must exceed weight by the needed centripetal force.
- id: q3-d
  content: |-
    $N_{\text{bottom}}=mg$
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
N_{\text{top}}=mg-m\frac{v^2}{r}
$$

and

$$
N_{\text{bottom}}=mg+m\frac{v^2}{r}.
$$

For a rotating wheel, the centripetal term $m\frac{v^2}{r}$ is positive. That means $N_{\text{top}}$ is $mg$ minus a positive amount, while $N_{\text{bottom}}$ is $mg$ plus the same positive amount. Therefore,

$$
N_{\text{top}}<N_{\text{bottom}}.
$$

If angular speed is given instead of speed, use $v=\omega r$, so $\frac{v^2}{r}=\omega^2r$. The comparison stays the same:

$$
N_{\text{top}}=m(g-\omega^2r),\qquad N_{\text{bottom}}=m(g+\omega^2r).
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
    $N_{\text{top}} > N_{\text{bottom}}$
  feedback: |-
    This reverses the signs: the centripetal term is subtracted at the top and added at the bottom.
- id: q4-b
  content: |-
    $N_{\text{top}} = N_{\text{bottom}}$
  feedback: |-
    Constant speed keeps the size of $\frac{v^2}{r}$ the same, but the force signs change at the top and bottom.
- id: q4-c
  content: |-
    $N_{\text{top}} < N_{\text{bottom}}$
  correct: true
  feedback: |-
    At the top gravity helps provide the inward force; at the bottom the seat must exceed weight.
```

---

<a id="summary"></a>
## Summary

For vertical circular motion, first point the radial equation inward. At the top, inward is downward, so

$$
mg-N_{\text{top}}=m\frac{v^2}{r}
$$

and

$$
N_{\text{top}}=mg-m\frac{v^2}{r}.
$$

At the bottom, inward is upward, so

$$
N_{\text{bottom}}-mg=m\frac{v^2}{r}
$$

and

$$
N_{\text{bottom}}=mg+m\frac{v^2}{r}.
$$

The main trap is thinking constant speed means equal normal forces. Constant speed keeps the size of $\frac{v^2}{r}$ the same, but the force signs change because inward points in opposite directions at the top and bottom.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Finding the Normal Force at the Bottom of a Ferris Wheel](Problem-4.md)

Study guide index: 16/30

---

<!-- lesson-nav:end -->
