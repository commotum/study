# Comparing Ferris-Wheel Normal Forces at the Top and Bottom

<!--
lesson-id: 212-M1-053
topic-code: MTH212.M1.53
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Inward Direction at Each Point](#choose-the-inward-direction-at-each-point)
- [Write the Two Radial Force Equations](#write-the-two-radial-force-equations)
- [Solve Each Equation for the Normal Force](#solve-each-equation-for-the-normal-force)
- [Compare the Two Normal Forces](#compare-the-two-normal-forces)
- [Summary](#summary)

## Prerequisites

- Weight points downward with magnitude $mg$.
- The seat's normal force on the rider points upward in this Ferris-wheel model.
- For circular motion with angular velocity $\omega$ and radius $r$, the inward acceleration has magnitude $\omega^2r$.
- Newton's second law in the radial direction: $\sum F_{\text{in}}=m\omega^2r$.

---

<a id="introduction"></a>
## Introduction

The problem asks how the normal force on a Ferris-wheel rider at the top compares with the normal force at the bottom. The cue is that the rider is moving in a vertical circle at constant angular velocity, so the net force must point toward the center at both positions.

The reusable procedure is:

1. Choose inward as positive at each position.
2. Give each real force a sign based on that local inward direction.
3. Set the signed net force equal to $m\omega^2r$.
4. Solve for each normal force and compare the two expressions.

Use a separate inward direction at the top and at the bottom:

- At the top, inward points downward.
- At the bottom, inward points upward.

That change in inward direction is what changes the force equation.

---

<a id="choose-the-inward-direction-at-each-point"></a>
## Choose the Inward Direction at Each Point

**Example:** A rider is at the top of a Ferris wheel. Which way is the inward direction for the radial force equation?

**Explanation**

The inward direction always points from the rider toward the center of the circle. At the top, the center is below the rider, so inward points downward.

At the bottom, the center is above the rider, so inward points upward. The forces do not switch directions: weight still points downward, and the seat's normal force still points upward. What switches is which force points inward.

```quiz
type: radio
id: p3-q1-inward-directions
shuffle: true
content: |-
  A rider is at the bottom of a Ferris wheel. Which direction is inward for the radial force equation?
options:
- id: p3q1-a
  content: |-
    Downward, because gravity points downward.
- id: p3q1-b
  content: |-
    Upward, toward the center of the wheel.
  correct: true
- id: p3q1-c
  content: |-
    Tangent to the wheel's motion.
- id: p3q1-d
  content: |-
    Zero, because the angular velocity is constant.
```

---

<a id="write-the-two-radial-force-equations"></a>
## Write the Two Radial Force Equations

**Example:** A rider of mass $m$ moves on a Ferris wheel of radius $r$ with angular velocity $\omega$. Write the radial force equation at the top and at the bottom.

**Explanation**

At the top, inward is downward. Weight points inward and the normal force points outward, so

$$
mg-N_{\text{top}}=m\omega^2r.
$$

At the bottom, inward is upward. The normal force points inward and weight points outward, so

$$
N_{\text{bottom}}-mg=m\omega^2r.
$$

The right-hand side is positive in both equations because it is the required inward net force.

| Position | Inward direction | Force pointing inward | Force pointing outward | Radial equation |
| --- | --- | --- | --- | --- |
| Top | Downward | $mg$ | $N_{\text{top}}$ | $mg-N_{\text{top}}=m\omega^2r$ |
| Bottom | Upward | $N_{\text{bottom}}$ | $mg$ | $N_{\text{bottom}}-mg=m\omega^2r$ |

```quiz
type: radio
id: p3-q2-radial-equations
shuffle: true
content: |-
  Which pair of equations correctly represents the rider at the top and bottom of a Ferris wheel?
options:
- id: p3q2-a
  content: |-
    Top: $mg-N_{\text{top}}=m\omega^2r$; bottom: $N_{\text{bottom}}-mg=m\omega^2r$
  correct: true
- id: p3q2-b
  content: |-
    Top: $N_{\text{top}}-mg=m\omega^2r$; bottom: $mg-N_{\text{bottom}}=m\omega^2r$
- id: p3q2-c
  content: |-
    Top: $mg+N_{\text{top}}=m\omega^2r$; bottom: $mg+N_{\text{bottom}}=m\omega^2r$
- id: p3q2-d
  content: |-
    Top: $N_{\text{top}}=m\omega^2r$; bottom: $N_{\text{bottom}}=m\omega^2r$
```

---

<a id="solve-each-equation-for-the-normal-force"></a>
## Solve Each Equation for the Normal Force

**Example:** Use the top and bottom equations to solve for $N_{\text{top}}$ and $N_{\text{bottom}}$.

**Explanation**

Start with the top equation:

$$
mg-N_{\text{top}}=m\omega^2r.
$$

Move $N_{\text{top}}$ to the right and $m\omega^2r$ to the left:

$$
N_{\text{top}}=mg-m\omega^2r.
$$

Now use the bottom equation:

$$
N_{\text{bottom}}-mg=m\omega^2r.
$$

Add $mg$ to both sides:

$$
N_{\text{bottom}}=mg+m\omega^2r.
$$

The same centripetal term is subtracted at the top and added at the bottom.

You can check both expressions by substituting them back into the original radial equations:

$$
mg-(mg-m\omega^2r)=m\omega^2r
$$

and

$$
(mg+m\omega^2r)-mg=m\omega^2r.
$$

```quiz
type: radio
id: p3-q3-solved-normal-forces
shuffle: true
content: |-
  If $mg-N_{\text{top}}=m\omega^2r$ and $N_{\text{bottom}}-mg=m\omega^2r$, which expressions are correct?
options:
- id: p3q3-a
  content: |-
    $N_{\text{top}}=mg+m\omega^2r$ and $N_{\text{bottom}}=mg-m\omega^2r$
- id: p3q3-b
  content: |-
    $N_{\text{top}}=mg-m\omega^2r$ and $N_{\text{bottom}}=mg+m\omega^2r$
  correct: true
- id: p3q3-c
  content: |-
    $N_{\text{top}}=N_{\text{bottom}}=mg$
- id: p3q3-d
  content: |-
    $N_{\text{top}}=N_{\text{bottom}}=m\omega^2r$
```

---

<a id="compare-the-two-normal-forces"></a>
## Compare the Two Normal Forces

**Example:** A person rides on a Ferris wheel of radius $r$ at constant angular velocity $\omega$. How does the normal force from the seat at the top compare to the normal force from the seat at the bottom?

**Explanation**

The two normal forces are

$$
N_{\text{top}}=mg-m\omega^2r
$$

and

$$
N_{\text{bottom}}=mg+m\omega^2r.
$$

For a rotating wheel, $m\omega^2r$ is positive. The top normal force is $mg$ minus that positive term, and the bottom normal force is $mg$ plus that positive term. Therefore,

$$
N_{\text{top}}<N_{\text{bottom}}.
$$

A direct comparison gives the same result:

$$
\begin{aligned}
N_{\text{bottom}}-N_{\text{top}}
&=(mg+m\omega^2r)-(mg-m\omega^2r) \\
&=2m\omega^2r.
\end{aligned}
$$

For a rotating wheel, $2m\omega^2r>0$, so $N_{\text{bottom}}$ is larger.

```quiz
type: radio
id: p3-q4-homework-comparison
shuffle: true
content: |-
  A person rides on a Ferris wheel of radius $r$ at constant angular velocity $\omega$. How does the normal force exerted on the rider from their seat at the top compare to the normal force on the rider from their seat at the bottom?
options:
- id: p3q4-a
  content: |-
    $N_{\text{top}}=N_{\text{bottom}}$
- id: p3q4-b
  content: |-
    $N_{\text{top}}>N_{\text{bottom}}$
- id: p3q4-c
  content: |-
    $N_{\text{top}}<N_{\text{bottom}}$
  correct: true
```

---

<a id="summary"></a>
## Summary

When comparing Ferris-wheel normal forces, choose the inward direction separately at each position. At the top, inward is downward, so

$$
mg-N_{\text{top}}=m\omega^2r.
$$

At the bottom, inward is upward, so

$$
N_{\text{bottom}}-mg=m\omega^2r.
$$

Solving gives $N_{\text{top}}=mg-m\omega^2r$ and $N_{\text{bottom}}=mg+m\omega^2r$, so the normal force is smaller at the top. The main trap is using the same sign pattern at both positions instead of changing the inward direction.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
