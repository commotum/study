# Comparing Torque Magnitudes From a Diagram

## Table of Contents

- [Introduction](#introduction)
- [Use the Torque-Magnitude Formula](#use-the-torque-magnitude-formula)
- [Think in Perpendicular Lever Arms](#think-in-perpendicular-lever-arms)
- [Recognize Maximum and Zero Torque](#recognize-maximum-and-zero-torque)
- [Rank Equal Forces Efficiently](#rank-equal-forces-efficiently)
- [Apply the Comparison](#apply-the-comparison)
- [Summary](#summary)

## Prerequisites

- Identify the pivot and the position vector from the pivot to the point where a force is applied.
- Recognize the angle between two vectors.
- Use $\sin 0^\circ=\sin 180^\circ=0$ and $\sin 90^\circ=1$.
- Compare nonnegative quantities without computing every value exactly.

## Introduction

The torque magnitude produced by a force about a pivot is

$$
\tau=rF\sin\theta,
$$

where

- $r$ is the distance from the pivot to the force's point of application,
- $F$ is the force magnitude, and
- $\theta$ is the angle between the position vector $\vec r$ and the force vector $\vec F$.

The same formula can be written as

$$
\tau=Fr_\perp,
\qquad
r_\perp=r\sin\theta,
$$

where $r_\perp$ is the perpendicular distance from the pivot to the force's **line of action**.

When several forces have equal magnitude, $F$ is a common positive factor. The comparison therefore reduces to one core move:

> Rank the perpendicular lever arms $r_\perp=r\sin\theta$.

## Use the Torque-Magnitude Formula

The angle factor matters just as much as the distance from the pivot. A large $r$ cannot compensate for a force whose line of action passes through the pivot.

### Worked example

A $10\text{ N}$ force is applied $0.80\text{ m}$ from a hinge at an angle of $30^\circ$ to the position vector. Its torque magnitude is

$$
\tau=(0.80)(10)\sin 30^\circ
=8(0.5)
=4.0\text{ N}\cdot\text{m}.
$$

The factor $\sin\theta$ keeps only the component of the force that is perpendicular to $\vec r$.

```quiz
type: radio
id: m2-3-p1-formula
shuffle: true
content: |-
  A $12\text{ N}$ force is applied $0.50\text{ m}$ from a pivot and perpendicular to the position vector. What is the torque magnitude?
options:
- id: a
  content: |-
    $0\text{ N}\cdot\text{m}$
- id: b
  content: |-
    $6.0\text{ N}\cdot\text{m}$
  correct: true
  feedback: |-
    Perpendicular means $\theta=90^\circ$, so

    $$
    \tau=rF\sin\theta=(0.50)(12)(1)=6.0\text{ N}\cdot\text{m}.
    $$
- id: c
  content: |-
    $12\text{ N}\cdot\text{m}$
- id: d
  content: |-
    $24\text{ N}\cdot\text{m}$
```

## Think in Perpendicular Lever Arms

The lever arm is not automatically the distance to the point where the force is applied. It is the shortest, perpendicular distance from the pivot to the force's line of action.

For equal forces, define a comparison score

$$
S=r\sin\theta=r_\perp.
$$

Then

$$
\tau=FS,
$$

so the force with the largest score has the largest torque magnitude.

### Worked example

Two equal forces act about the same pivot. Force A has $r_\perp=0.60\text{ m}$, while Force B has $r_\perp=0.45\text{ m}$. Because the force magnitudes are equal,

$$
0.60>0.45
\quad\Longrightarrow\quad
\tau_A>\tau_B.
$$

No force magnitude is needed to make the comparison.

```quiz
type: radio
id: m2-3-p1-lever-arm
shuffle: true
content: |-
  Three forces have the same magnitude. Their perpendicular lever arms are $0.25\text{ m}$, $0.70\text{ m}$, and $0.55\text{ m}$. Which force produces the largest torque magnitude?
options:
- id: a
  content: |-
    The force with $r_\perp=0.25\text{ m}$
- id: b
  content: |-
    The force with $r_\perp=0.70\text{ m}$
  correct: true
  feedback: |-
    For equal force magnitudes, $\tau=Fr_\perp$ is largest when $r_\perp$ is largest.
- id: c
  content: |-
    The force with $r_\perp=0.55\text{ m}$
- id: d
  content: |-
    All three produce the same torque magnitude.
```

## Recognize Maximum and Zero Torque

Because $0\leq |\sin\theta|\leq 1$,

$$
0\leq \tau\leq rF.
$$

For fixed $r$ and $F$:

| Force direction | Angle | Torque consequence |
|---|---:|---|
| Perpendicular to $\vec r$ | $90^\circ$ | Maximum: $\tau=rF$ |
| Along $\vec r$ away from the pivot | $0^\circ$ | Zero: $\tau=0$ |
| Along $\vec r$ toward the pivot | $180^\circ$ | Zero: $\tau=0$ |
| At any other angle | between the cases above | Only the perpendicular part contributes |

A force pointing directly toward or away from the hinge has a line of action through the hinge, so its perpendicular lever arm is zero. This remains true even if the force is applied far from the hinge.

```quiz
type: radio
id: m2-3-p1-special-angle
shuffle: true
content: |-
  A force is applied to the far end of a door, but the force points directly toward the hinge. What is the torque magnitude about the hinge?
options:
- id: a
  content: |-
    Zero
  correct: true
  feedback: |-
    The force's line of action passes through the hinge. Equivalently, $\theta=180^\circ$ and $\sin 180^\circ=0$, so $\tau=0$.
- id: b
  content: |-
    $rF$
- id: c
  content: |-
    Greater than $rF$
- id: d
  content: |-
    It cannot be determined from the direction.
```

## Rank Equal Forces Efficiently

Translate the visual information into a torque consequence before trying to estimate numbers:

| Diagram cue | Torque consequence |
|---|---|
| The line of action passes through the pivot | $r_\perp=0$, so the torque magnitude is zero |
| The force is perpendicular to the position vector | $r_\perp=r$, the greatest possible lever arm for that $r$ |
| The force is angled relative to the position vector | $r_\perp=r\sin\theta<r$ unless the angle is $90^\circ$ |
| Two equal forces have parallel lines of action | The line farther from the pivot produces the larger torque magnitude |

The arrows' equal lengths indicate equal **force magnitudes**; their directions can still produce different torque magnitudes. Thus, do not treat equal force magnitudes as equal torques.

Use a two-pass scan:

1. Eliminate any force whose line of action passes through the pivot; it produces zero torque.
2. Among the remaining forces, compare $r\sin\theta$, or visually compare the perpendicular distances from the pivot to their lines of action.

### Worked example

Four equal forces have the following positions and angles:

| Force | $r$ | $\theta$ | Score $S=r\sin\theta$ |
|---|---:|---:|---:|
| A | $1.0\text{ m}$ | $90^\circ$ | $1.0\text{ m}$ |
| B | $1.2\text{ m}$ | $0^\circ$ | $0$ |
| C | $1.0\text{ m}$ | $30^\circ$ | $0.50\text{ m}$ |
| D | $0.60\text{ m}$ | $90^\circ$ | $0.60\text{ m}$ |

Force A has the largest score and therefore the largest torque magnitude. Force B is applied farthest away, but its direction makes its torque zero. Force D is perpendicular, but its shorter radius gives it a smaller lever arm than A.

```quiz
type: radio
id: m2-3-p1-rank
shuffle: true
content: |-
  Equal-magnitude forces W, X, Y, and Z have the following $(r,\theta)$ values. Which force produces the largest torque magnitude?

  - W: $(0.80\text{ m},90^\circ)$
  - X: $(1.10\text{ m},0^\circ)$
  - Y: $(1.00\text{ m},45^\circ)$
  - Z: $(0.60\text{ m},90^\circ)$
options:
- id: a
  content: |-
    Force W
  correct: true
  feedback: |-
    Compare $r\sin\theta$: W has score $0.80$, X has $0$, Y has $1.00\sin45^\circ\approx0.707$, and Z has $0.60$. W is largest.
- id: b
  content: |-
    Force X
- id: c
  content: |-
    Force Y
- id: d
  content: |-
    Force Z
```

## Apply the Comparison

In the door diagram below, all four forces have equal magnitude. Therefore, compare only their perpendicular lever arms.

- Force 1 acts far from the hinge and perpendicular to the door, so it has a large $r$ and the maximum angle factor.
- Force 2 acts along the door. Its line of action passes through the hinge, so its torque is zero.
- Force 3 acts far from the hinge but at an angle, so only part of its force is perpendicular to the door.
- Force 4 is perpendicular to the door but is applied closer to the hinge, so its lever arm is shorter than Force 1's.

```quiz
type: radio
id: m2-3pre-q1
shuffle: true
content: |-
  **Question 1**

  Four forces of equal magnitude act on a door as shown in the top-view diagram.

  Which force produces the largest torque magnitude about the hinge?

  ![](<../Source/Images/door-force-torque-comparison.png>)
options:
- id: a
  content: |-
    Force 1
  correct: true
  feedback: |-
    Torque magnitude is

    $$
    \tau=rF\sin\theta.
    $$

    Force 1 acts far from the hinge and perpendicular to the door, maximizing both the lever arm $r$ and $\sin\theta$. Force 4 is perpendicular but closer to the hinge, Force 3 is angled, and Force 2 produces zero torque because its line of action passes through the hinge.
- id: b
  content: |-
    Force 2
- id: c
  content: |-
    Force 3
- id: d
  content: |-
    Force 4
```

## Summary

- Start with $\tau=rF\sin\theta=Fr_\perp$.
- When force magnitudes are equal, rank $r\sin\theta$ or $r_\perp$.
- A perpendicular force gives the largest possible torque for fixed $r$ and $F$.
- A force whose line of action passes through the pivot gives zero torque.
- Do not compare distance alone or angle alone; compare their combined effect through the perpendicular lever arm.
