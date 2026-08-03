# Finding the Tipping Threshold With Torque Balance

<!--
lesson-id: 212-M3-022
topic-code: MTH212.M3.22
-->

## Table of Contents

- [Introduction](#introduction)
- [Recognize the Tipping Pivot](#recognize-the-tipping-pivot)
- [Draw the Forces and Measure Lever Arms](#draw-the-forces-and-measure-lever-arms)
- [Balance Torques at the Threshold](#balance-torques-at-the-threshold)
- [Decide Whether a Placement Is Stable](#decide-whether-a-placement-is-stable)
- [Summary](#summary)

## Prerequisites

- Compute a torque magnitude with $\tau=r_\perp F$.
- Identify the center of mass of a uniform board.
- Distinguish clockwise from counterclockwise torque.
- Solve a one-step equation for an unknown distance.

---

<a id="introduction"></a>
## Introduction

When a load moves toward the end of a supported object, the object begins to tip when it is just about to lose contact with one support. The recognition cue is a question asking for the **farthest placement without tipping**.

At that limiting position:

1. Choose the support that remains in contact as the pivot.
2. Set the normal force at the support that is about to lift to zero.
3. Measure every lever arm from the tipping pivot.
4. Balance the clockwise and counterclockwise torques.

For the uniform board in Problem 4, support B is the tipping pivot. The board's weight acts $L/4$ to the left of B, and the box's downward contact force acts a distance $x$ to the right of B.

---

<a id="recognize-the-tipping-pivot"></a>
## Recognize the Tipping Pivot

**Example:** A person walks to the right on a board supported at A and B. As the person reaches the limiting position, the left end of the board starts to rise. Which support is the tipping pivot, and what happens to the force at A?

**Explanation**

The board is about to rotate around the support that stays in contact: support B. At the threshold, support A can no longer pull downward on the board, so its normal force has fallen to zero:

$$
N_A=0.
$$

The force at B does not appear in a torque equation taken about B because its lever arm is zero.

```quiz
type: radio
id: p4-tipping-pivot
content: |-
  A box is moved to the right of support B until the left support A is just about to lose contact with a board. Which statement describes the tipping threshold?
options:
- id: a
  content: |-
    The board pivots about A, and $N_B=0$.
- id: b
  content: |-
    The board pivots about B, and $N_A=0$.
  correct: true
  feedback: |-
    The board turns about the support that remains in contact, while the lifting support's normal force reaches zero.
- id: c
  content: |-
    The board pivots about its center of mass, and $N_A=N_B$.
- id: d
  content: |-
    Both support forces become zero before the board tips.
```

---

<a id="draw-the-forces-and-measure-lever-arms"></a>
## Draw the Forces and Measure Lever Arms

**Example:** A uniform board of mass $M$ and length $L$ rests on supports at $L/4$ and $3L/4$ from its left end. A box of mass $m$ is placed a distance $x$ to the right of support B. Draw separate free-body diagrams and identify the forces and lever arms needed for torque balance about B.

![](<../Source/2026-07-19-PQ-2/Images/problem-4-board-tipping.png>)

**Explanation**

On the **board**, draw:

- $N_A$ upward at support A,
- $N_B$ upward at support B,
- $Mg$ downward at the board's center,
- $N$ downward at the box's location, exerted by the box on the board.

On the **box**, draw $N$ upward from the board and $mg$ downward. Since the box is at rest vertically,

$$
N=mg.
$$

The board is uniform, so its center of mass is at $L/2$ from the left end. Support B is at $3L/4$, giving the board weight a lever arm

$$
\frac{3L}{4}-\frac{L}{2}=\frac{L}{4}.
$$

The box force has lever arm $x$. About B, $Mg$ produces counterclockwise torque and $mg$ produces clockwise torque.

```quiz
type: radio
id: p4-lever-arms
content: |-
  A uniform board has its center of mass at $L/2$, and the right support B is at $3L/4$. A box sits a distance $x$ to the right of B. Which pair gives the correct lever arms about B?
options:
- id: a
  content: |-
    Board weight: $L/4$; box force: $x$
  correct: true
  feedback: |-
    The board's arm is $3L/4-L/2=L/4$, and $x$ is already measured from B.
- id: b
  content: |-
    Board weight: $L/2$; box force: $x$
- id: c
  content: |-
    Board weight: $3L/4$; box force: $3L/4+x$
- id: d
  content: |-
    Board weight: $L/4$; box force: $3L/4+x$
- id: e
  content: |-
    Board weight: $L/2$; box force: $L-x$
```

---

<a id="balance-torques-at-the-threshold"></a>
## Balance Torques at the Threshold

**Example:** Find the farthest distance $x$ to the right of support B at which the box can be placed without tipping the board.

**Explanation**

At the threshold, take torques about B. With counterclockwise positive,

$$
\sum \tau_B
=Mg\left(\frac{L}{4}\right)-mgx_{\max}=0.
$$

The factor $g$ cancels. Solving for the distance gives

$$
\begin{aligned}
M\left(\frac{L}{4}\right)&=mx_{\max},\\
\frac{ML}{4}&=mx_{\max},\\
x_{\max}&=\frac{ML}{4m}.
\end{aligned}
$$

This is the limiting value: $x=x_{\max}$ is just on the verge of tipping, so any placement with $x\le x_{\max}$ does not tip the board.

The formula also gives a quick reasonableness check. Increasing $M$ or $L$ increases the stabilizing torque and allows a larger $x_{\max}$. Increasing the box mass $m$ increases the tipping torque, so it decreases $x_{\max}$.

```quiz
type: radio
id: p4-threshold-equation
content: |-
  A uniform board of mass $6\ \mathrm{kg}$ is supported so that its center of mass is $0.40\ \mathrm{m}$ left of the tipping pivot. A $3\ \mathrm{kg}$ box is placed to the right of that pivot. What is the farthest stable box distance?
options:
- id: a
  content: |-
    $0.20\ \mathrm{m}$
- id: b
  content: |-
    $0.40\ \mathrm{m}$
- id: c
  content: |-
    $0.80\ \mathrm{m}$
  correct: true
  feedback: |-
    Balance torques: $(6g)(0.40)=(3g)x$, so $x=0.80\ \mathrm{m}$.
- id: d
  content: |-
    $1.20\ \mathrm{m}$
- id: e
  content: |-
    $2.40\ \mathrm{m}$
```

---

<a id="decide-whether-a-placement-is-stable"></a>
## Decide Whether a Placement Is Stable

**Example:** For the same board-and-box arrangement, suppose the box is placed at

$$
x=\frac{ML}{5m}.
$$

Will the board tip?

**Explanation**

Compare the placement with the threshold:

$$
\frac{ML}{5m}<\frac{ML}{4m}=x_{\max}.
$$

The board's counterclockwise torque is still larger than the box's clockwise torque, so the board remains stable. The support at A still supplies an upward normal force.

Do not reverse this comparison: a larger $x$ gives the box a larger tipping torque.

The formula predicts the same direction. For example, doubling the box mass changes the threshold from $ML/(4m)$ to $ML/(8m)$, cutting the farthest stable distance in half.

```quiz
type: radio
id: p4-stability-check
content: |-
  A board-and-box system has tipping threshold $x_{\max}=0.60\ \mathrm{m}$. Which placement is stable and not exactly at the threshold?
options:
- id: a
  content: |-
    $x=0.45\ \mathrm{m}$
  correct: true
  feedback: |-
    A placement below the threshold leaves a restoring torque and a positive support force at A.
- id: b
  content: |-
    $x=0.60\ \mathrm{m}$
- id: c
  content: |-
    $x=0.75\ \mathrm{m}$
- id: d
  content: |-
    Every positive value of $x$ causes tipping.
```

---

<a id="summary"></a>
## Summary

For a **farthest placement without tipping**:

1. Use the support that remains in contact as the pivot.
2. Set the lifting support's normal force equal to zero.
3. Measure all lever arms from the pivot, not from the end of the object.
4. Balance the opposing torques and solve for the limiting distance.

For this uniform board, the board's weight acts $L/4$ left of B and the box's force acts $x$ right of B:

$$
Mg\left(\frac{L}{4}\right)=mgx_{\max}
\quad\Longrightarrow\quad
x_{\max}=\frac{ML}{4m}.
$$

The main trap is keeping the force from support A in the threshold equation. At the instant tipping begins, $N_A=0$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Speed of a Rolling Solid Cylinder From Energy](../../../M2/2026-07-15-HW-4/Lessons/Problem-3.md)

Study guide index: 08/20

---
<!-- lesson-nav:end -->
