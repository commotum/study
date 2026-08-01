# Finding the Load Position at the Tipping Point

## Table of Contents

- [Introduction](#introduction)
- [Identify the Tipping Pivot](#identify-the-tipping-pivot)
- [Measure Lever Arms From the Pivot](#measure-lever-arms-from-the-pivot)
- [Balance the Opposing Torques](#balance-the-opposing-torques)
- [Apply the Method to the Board and Box](#apply-the-method-to-the-board-and-box)
- [Summary](#summary)

## Prerequisites

- A uniform board's center of mass is at its midpoint
- Torque magnitude: $\tau=r_\perp F$
- Static rotational equilibrium: $\sum\tau=0$
- Subtracting fractions with unlike denominators

---

## Introduction

An object is just about to tip when it is on the verge of rotating about one remaining contact point. At that instant, the support on the lifting side exerts zero force.

For a board loaded to the right of support B:

- support B is the tipping pivot;
- the force from support A is zero;
- the board's weight and the box's weight create opposing torques about B.

**Recognition cue:** When a supported object is “just about to tip,” choose the support nearest the overhanging load as the pivot, remove the other support force, and balance the weight torques using lever arms measured from that pivot.

---

## Identify the Tipping Pivot

**Example:** A board rests on supports A and B, with B to the right of A. A box is moved farther to the right of B. Which support becomes the pivot at the tipping point?

**Explanation**

As the box moves right, the board tries to rotate around support B and lift away from support A. At the threshold of tipping,

$$
N_A=0.
$$

Support B remains in contact, so B is the pivot. Choosing B also removes the unknown force $N_B$ from the torque equation because its lever arm about B is zero.

```quiz
type: radio
id: problem-2-pivot-q1
content: |-
  A plank rests on a left support A and a right support B. A load is placed beyond B and moved farther right until the plank is about to tip. Which statement is correct at that instant?
options:
- id: a
  content: |-
    The plank pivots about B and $N_A=0$
  correct: true
  feedback: |-
    The load lifts the plank from A while contact at B remains, so B is the tipping pivot.
- id: b
  content: |-
    The plank pivots about A and $N_B=0$
  feedback: |-
    That would describe tipping caused by a load beyond the left support.
- id: c
  content: |-
    The plank pivots about its center of mass
  feedback: |-
    The pivot is the remaining contact point, not the board's center of mass.
- id: d
  content: |-
    Both support forces remain equal
  feedback: |-
    At impending tipping, the support on the lifting side has already fallen to zero.
- id: e
  content: |-
    Both support forces are zero
  feedback: |-
    Support B must still provide contact force while serving as the pivot.
```

---

## Measure Lever Arms From the Pivot

**Example:** A uniform board extends from coordinate $0$ to $L$, and support B is at $2L/3$. Find the board weight's lever arm about B.

**Explanation**

Because the board is uniform, its center of mass is at the midpoint:

$$
x_{\mathrm{cm}}=\frac{L}{2}.
$$

The pivot is at $2L/3$, so the lever-arm magnitude is the distance between these two positions:

$$
\ell_{\mathrm{board}}
=\frac{2L}{3}-\frac{L}{2}
=\frac{4L}{6}-\frac{3L}{6}
=\frac{L}{6}.
$$

| Point or force | Position from the left end | Lever arm from B |
|---|---:|---:|
| Support A | $L/5$ | Not used because $N_A=0$ |
| Board weight | $L/2$ | $L/6$ left |
| Support B | $2L/3$ | $0$ |
| Box weight | $2L/3+x$ | $x$ right |

The board's center of mass lies to the left of B. A box placed distance $x$ to the right of B has lever arm $x$. The location of support A does not appear in the torque balance once its force is zero.

```quiz
type: radio
id: problem-2-board-arm-q1
content: |-
  A uniform board extends from $0$ to $L$, and the tipping pivot is at $3L/4$. What is the lever-arm magnitude of the board's weight about the pivot?
options:
- id: a
  content: |-
    $\dfrac{L}{4}$
  correct: true
  feedback: |-
    The center of mass is at $L/2$, so the separation is $3L/4-L/2=L/4$.
- id: b
  content: |-
    $\dfrac{L}{2}$
  feedback: |-
    This is the center-of-mass position from the left end, not its distance from the pivot.
- id: c
  content: |-
    $\dfrac{3L}{4}$
  feedback: |-
    This is the pivot position from the left end, not the board's lever arm.
- id: d
  content: |-
    $\dfrac{5L}{4}$
  feedback: |-
    Lever arms are distances between the force line and pivot, so the positions should be subtracted.
- id: e
  content: |-
    $\dfrac{L}{8}$
  feedback: |-
    This halves the actual separation between $L/2$ and $3L/4$.
```

---

## Balance the Opposing Torques

**Example:** A uniform board of mass $M$ has its center of mass a distance $a$ left of the tipping pivot. A box of mass $m$ is distance $x$ right of the pivot. Solve for the tipping distance $x$.

**Explanation**

The downward board weight $Mg$ on the left and downward box weight $mg$ on the right rotate the board in opposite directions. At the threshold of tipping, their torque magnitudes are equal:

$$
Mg\,a=mg\,x.
$$

Equivalently, choosing counterclockwise torque as positive gives the signed ledger

| Force | Side of pivot | Torque about B |
|---|---|---:|
| Board weight $Mg$ | Left | $+Mga$ |
| Box weight $mg$ | Right | $-mgx$ |

and therefore

$$
\sum\tau_B=Mga-mgx=0.
$$

Cancel $g$ and divide by $m$:

$$
x=\frac{M}{m}a.
$$

This form gives a useful direction check: increasing the board mass $M$ lets the box move farther from the pivot, while increasing the box mass $m$ makes the tipping distance smaller.

```quiz
type: radio
id: problem-2-torque-balance-q1
content: |-
  A board of mass $M=3m$ has its center of mass a distance $L/8$ left of the tipping pivot. How far to the right of the pivot can a box of mass $m$ be placed at impending tipping?
options:
- id: a
  content: |-
    $x=\dfrac{3L}{8}$
  correct: true
  feedback: |-
    $x=(M/m)(L/8)=3L/8$.
- id: b
  content: |-
    $x=\dfrac{L}{24}$
  feedback: |-
    This reverses the mass ratio.
- id: c
  content: |-
    $x=\dfrac{L}{8}$
  feedback: |-
    This ignores that the board is three times as massive as the box.
- id: d
  content: |-
    $x=\dfrac{L}{3}$
  feedback: |-
    This uses the mass ratio but omits the board's lever arm.
- id: e
  content: |-
    $x=\dfrac{3L}{4}$
  feedback: |-
    This doubles the correct lever arm contribution.
```

---

## Apply the Method to the Board and Box

**Example:** Find the tipping distance for the given board and box.

**Explanation**

Support B is at $2L/3$, while the uniform board's center of mass is at $L/2$. Therefore,

$$
\ell_{\mathrm{board}}
=\frac{2L}{3}-\frac{L}{2}
=\frac{4L}{6}-\frac{3L}{6}
=\frac{L}{6}.
$$

Balance torques about B:

$$
mgx=Mg\frac{L}{6},
\qquad
x=\frac{ML}{6m}.
$$

Substitute $M=2.4\ \mathrm{kg}$, $L=1.4\ \mathrm{m}$, and $m=1.6\ \mathrm{kg}$:

$$
x
=\frac{(2.4)(1.4)}{6(1.6)}
=0.35\ \mathrm{m}.
$$

The result is less than the available right overhang, $L-2L/3=L/3\approx0.47\ \mathrm{m}$, so the stated box position fits on the board.

```quiz
type: radio
id: m2-4lec-q1
require_exact: true
content: |-
  **Question 1**

  A uniform board of mass $M$ and length $L$ rests on supports A and B. Support A is $L/5$ from the board's left end, and support B is $2L/3$ from the left end. A box of mass $m$ is placed a distance $x$ to the right of support B.

  Find the distance $x$ at which the board is just about to tip. Use $M=2.4\ \mathrm{kg}$, $L=1.4\ \mathrm{m}$, and $m=1.6\ \mathrm{kg}$.

  ![](<../Source/Images/uniform-board-tipping.png>)

  Enter the distance in meters as a number only:
options:
- id: a
  content: |-
    $0.35$
  correct: true
  feedback: |-
    At the tipping point, the board pivots about support B and the force from support A is zero. The board's center of mass is $L/2$ from the left end, so its lever arm about B is

    $$
    \frac{2L}{3}-\frac{L}{2}=\frac{L}{6}.
    $$

    Torque balance about B gives

    $$
    mgx=Mg\frac{L}{6},
    \qquad
    x=\frac{ML}{6m}.
    $$

    Therefore,

    $$
    x=\frac{(2.4\ \mathrm{kg})(1.4\ \mathrm{m})}{6(1.6\ \mathrm{kg})}
    =0.35\ \mathrm{m}.
    $$

    The measured givens have two significant figures.
- id: b
  content: |-
    $0.16$
  feedback: |-
    This reverses the board-to-box mass ratio.
- id: c
  content: |-
    $1.1$
  feedback: |-
    This uses $L/2$ as the lever arm without measuring it from support B.
- id: d
  content: |-
    $0.98$
  feedback: |-
    This incorrectly uses the separation between supports A and B as the board weight's lever arm.
- id: e
  content: |-
    $2.1$
  feedback: |-
    This omits the board's lever-arm factor $1/6$.
```

---

## Summary

For a board tipping toward a load beyond support B:

1. Set the lifting-side support force to zero: $N_A=0$.
2. Take torques about the remaining support B.
3. Place a uniform board's center of mass at $L/2$.
4. Measure every lever arm from B, not from the board's end.
5. Balance the opposing weight torques and solve for the load distance.

For support B at $2L/3$,

$$
\ell_{\mathrm{board}}=\frac{2L}{3}-\frac{L}{2}=\frac{L}{6},
$$

so

$$
\boxed{x=\frac{ML}{6m}}.
$$

The main traps are pivoting about the wrong support, including the zero force from support A, or using a position from the board's end instead of a lever arm from the pivot.
