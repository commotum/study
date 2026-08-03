# Finding the Smallest Torque From a Force Diagram

<!--
lesson-id: 212-M2-012
topic-code: MTH212.M2.12
-->

## Table of Contents

- [Introduction](#introduction)
- [Use the Angle Between Position and Force](#use-the-angle-between-position-and-force)
- [Detect Zero Torque From the Line of Action](#detect-zero-torque-from-the-line-of-action)
- [Compare Equal Forces With Perpendicular Lever Arms](#compare-equal-forces-with-perpendicular-lever-arms)
- [Apply the Test to the Door](#apply-the-test-to-the-door)
- [Summary](#summary)

## Prerequisites

- Identifying a rotation axis or pivot
- Reading vector directions from a diagram
- Evaluating sine at common angles
- Comparing nonnegative quantities

---

## Introduction

The torque magnitude produced by a force is

$$
\tau=rF\sin\phi,
$$

where $r$ is the distance from the pivot to the force's application point and $\phi$ is the angle between the position vector $\vec r$ and the force $\vec F$.

To identify $\phi$, imagine the tails of $\vec r$ and $\vec F$ placed at the force's application point. Use the angle between their directions.

An equivalent form is

$$
\tau=F r_\perp,
$$

where $r_\perp$ is the shortest perpendicular distance from the pivot to the force's line of action.

| Geometry | Sine factor | Torque magnitude |
|---|---:|---:|
| Parallel, $\phi=0^\circ$ | $0$ | $0$ |
| Oblique, $0^\circ<\phi<180^\circ$ | Between $0$ and $1$ | Between $0$ and $rF$ |
| Perpendicular, $\phi=90^\circ$ | $1$ | $rF$ |
| Antiparallel, $\phi=180^\circ$ | $0$ | $0$ |

**Recognition cue:** When equal forces act on a rigid object and the question asks for the smallest torque magnitude, compare their perpendicular lever arms first. Any force whose line of action passes through the pivot produces zero torque and must be the minimum.

---

## Use the Angle Between Position and Force

**Example:** A $12\ \mathrm{N}$ force acts $0.50\ \mathrm{m}$ from a pivot at angle $\phi=30^\circ$ to the position vector. Find its torque magnitude.

**Explanation**

Substitute into the magnitude formula:

$$
\begin{aligned}
\tau
&=rF\sin\phi\\
&=(0.50)(12)\sin30^\circ\\
&=3.0\ \mathrm{N\,m}.
\end{aligned}
$$

Only the component of force perpendicular to $\vec r$ contributes. For fixed $r$ and $F$, the torque is largest at $90^\circ$ and decreases as $\sin\phi$ decreases.

```quiz
type: radio
id: problem-2-angle-q1
content: |-
  A $10\ \mathrm{N}$ force acts $0.40\ \mathrm{m}$ from a pivot and is perpendicular to the position vector. What is the torque magnitude?
options:
- id: a
  content: |-
    $4.0\ \mathrm{N\,m}$
  correct: true
  feedback: |-
    $\tau=rF\sin90^\circ=(0.40)(10)(1)=4.0\ \mathrm{N\,m}$.
- id: b
  content: |-
    $0\ \mathrm{N\,m}$
  feedback: |-
    A perpendicular force has the maximum sine factor, not a zero sine factor.
- id: c
  content: |-
    $2.0\ \mathrm{N\,m}$
  feedback: |-
    This incorrectly inserts an extra factor of $\frac12$.
- id: d
  content: |-
    $10\ \mathrm{N\,m}$
  feedback: |-
    This omits the $0.40\ \mathrm{m}$ lever arm.
- id: e
  content: |-
    $25\ \mathrm{N\,m}$
  feedback: |-
    This divides by the lever arm instead of multiplying by it.
```

---

## Detect Zero Torque From the Line of Action

**Example:** A force at the end of a horizontal bar points directly back along the bar toward its pivot. What torque magnitude does it produce?

**Explanation**

The force is antiparallel to the position vector, so $\phi=180^\circ$. Therefore,

$$
\tau=rF\sin180^\circ=0.
$$

Geometrically, extend the force arrow in both directions to form its full line of action. The shortest distance from the pivot to that line is measured along a perpendicular segment. Here the line passes through the pivot, so

$$
r_\perp=0,
$$

which again gives $\tau=F r_\perp=0$.

```quiz
type: radio
id: problem-2-zero-line-q1
content: |-
  Which force direction produces zero torque about a pivot when the force is applied away from the pivot?
options:
- id: a
  content: |-
    Directly toward the pivot along the position-vector line
  correct: true
  feedback: |-
    The force's line of action passes through the pivot, so $r_\perp=0$ and $\tau=0$.
- id: b
  content: |-
    Perpendicular to the position vector
  feedback: |-
    A perpendicular force has $\sin90^\circ=1$ and produces the largest torque for fixed $r$ and $F$.
- id: c
  content: |-
    At $60^\circ$ to the position vector
  feedback: |-
    Since $\sin60^\circ\ne0$, this force produces nonzero torque.
- id: d
  content: |-
    At $45^\circ$ to the position vector
  feedback: |-
    Since $\sin45^\circ\ne0$, this force produces nonzero torque.
- id: e
  content: |-
    At $30^\circ$ to the position vector
  feedback: |-
    Since $\sin30^\circ\ne0$, this force produces nonzero torque.
```

---

## Compare Equal Forces With Perpendicular Lever Arms

**Example:** Three equal forces have perpendicular lever arms $0.30\ \mathrm{m}$, $0.10\ \mathrm{m}$, and $0.25\ \mathrm{m}$. Which gives the smallest torque magnitude?

**Explanation**

Because every force has the same magnitude $F$,

$$
\tau=F r_\perp
$$

shows that torque magnitude is ordered exactly like $r_\perp$. The force with $r_\perp=0.10\ \mathrm{m}$ produces the smallest torque.

Do not compare only the application-point distances $r$. An oblique force applied far from the pivot can have a small perpendicular lever arm, and a radial force can have $r_\perp=0$ even when applied at the far edge.

```quiz
type: radio
id: problem-2-lever-arm-q1
content: |-
  Four equal forces have perpendicular lever arms from the pivot as shown. Which force produces the smallest torque magnitude?

  | Force | $r_\perp$ |
  |---|---:|
  | A | $0.40\ \mathrm{m}$ |
  | B | $0.15\ \mathrm{m}$ |
  | C | $0\ \mathrm{m}$ |
  | D | $0.25\ \mathrm{m}$ |
options:
- id: a
  content: |-
    Force A
  feedback: |-
    This force has the largest listed perpendicular lever arm.
- id: b
  content: |-
    Force B
  feedback: |-
    Its torque is nonzero because $r_\perp=0.15\ \mathrm{m}$.
- id: c
  content: |-
    Force C
  correct: true
  feedback: |-
    $r_\perp=0$ gives $\tau=F r_\perp=0$, the smallest possible magnitude.
- id: d
  content: |-
    Force D
  feedback: |-
    Its torque is nonzero because $r_\perp=0.25\ \mathrm{m}$.
```

---

## Apply the Test to the Door

**Example:** Compare the four equal forces in the door diagram.

**Explanation**

The hinge at the left edge is the pivot. Force $F_2$ points along the door toward the hinge. Its line of action passes through the hinge, so

$$
\tau_2=rF\sin180^\circ=0.
$$

The line-of-action audit is:

| Force | Relationship to hinge | Torque status |
|---|---|---:|
| $F_1$ | Perpendicular force at the far edge | Nonzero |
| $F_2$ | Line passes through hinge | Zero |
| $F_3$ | Oblique line misses hinge | Nonzero |
| $F_4$ | Perpendicular line away from hinge | Nonzero |

Therefore, $F_2$ gives the smallest torque magnitude.

```quiz
type: radio
id: m2-3lec-q1
shuffle: true
content: |-
  **Question 1**

  Four forces of equal magnitude act on a door as shown. Which force produces the smallest torque magnitude about the hinge? Explain.

  ![](<../Source/Images/door-force-torque-comparison-full.png>)
options:
- id: a
  content: $F_1$
- id: b
  content: $F_2$
  correct: true
  feedback: $F_2$ acts along the door toward the hinge, so its line of action passes through the rotation axis. Therefore, $\tau=rF\sin(180^\circ)=0$, the smallest possible magnitude.
- id: c
  content: $F_3$
- id: d
  content: $F_4$
```

---

## Summary

To find the smallest torque magnitude in a force diagram:

1. Mark the pivot.
2. For each force, identify the position vector from the pivot to the application point.
3. Trace the force's line of action.
4. Compare either $\tau=rF\sin\phi$ or $\tau=F r_\perp$.
5. Check first for a line of action through the pivot; it gives $\tau=0$.

For equal forces, the smallest perpendicular lever arm produces the smallest torque. The main trap is choosing the force closest to the hinge or most nearly horizontal without checking whether its line of action actually passes through the pivot.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
