# Minimum Friction for a Ladder Against a Smooth Wall

<!--
lesson-id: 212-M2-029
topic-code: MTH212.M2.29
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Bottom as the Torque Pivot](#choose-the-bottom-as-the-torque-pivot)
- [Use the Correct Lever Arms](#use-the-correct-lever-arms)
- [Turn Force Balance Into a Friction Ratio](#turn-force-balance-into-a-friction-ratio)
- [Apply the Method to Problem 3](#apply-the-method-to-problem-3)

## Prerequisites

- Static equilibrium: $\sum F_x=0$, $\sum F_y=0$, and $\sum\tau=0$
- Torque magnitude: $\tau=F r_\perp$
- Maximum static friction: $f_s=\mu_sN$ at impending slip
- Sine, cosine, and cotangent in a right triangle

---

<a id="introduction"></a>
## Introduction

A uniform ladder touching a frictionless wall is held at rest by three contact forces and its weight:

- the wall normal force $N_w$, horizontal at the top;
- the ground normal force $N_g$, vertical at the bottom;
- static friction $f_s$, horizontal at the bottom;
- the weight $mg$, downward at the ladder's midpoint.

The recognition cue is a uniform ladder in static equilibrium against a smooth wall, with the **minimum** friction coefficient requested. Take torques about the bottom, use force balance, and impose limiting friction. The result is

$$
\mu_s=\frac12\cot\theta.
$$

---

<a id="choose-the-bottom-as-the-torque-pivot"></a>
## Choose the Bottom as the Torque Pivot

**Example:** Why is the ladder's bottom the useful pivot for the torque equation?

**Explanation**

Both unknown ground forces, $N_g$ and $f_s$, act at the ladder's bottom. Their lever arm about that point is zero, so neither appears in the torque equation.

Only two forces produce torque about the bottom:

- $N_w$ at the ladder's top;
- $mg$ at the ladder's center of mass, halfway along the ladder.

This pivot choice leaves one torque equation with only one unknown force, $N_w$.

```quiz
type: radio
id: p3-pivot-choice
content: |-
  A uniform ladder rests against a frictionless wall. Which torque pivot eliminates both unknown ground contact forces from the torque equation?
options:
- id: p3-pivot-a
  content: |-
    The ladder's bottom contact point
  correct: true
  feedback: |-
    Both $N_g$ and $f_s$ act through the bottom contact point, so their torques vanish when that point is the pivot.
- id: p3-pivot-b
  content: |-
    The ladder's midpoint
- id: p3-pivot-c
  content: |-
    The ladder's top contact point
- id: p3-pivot-d
  content: |-
    Earth's center
- id: p3-pivot-e
  content: |-
    Any point gives the same number of unknown torques
```

---

<a id="use-the-correct-lever-arms"></a>
## Use the Correct Lever Arms

**Example:** Write the torque balance about the ladder's bottom.

**Explanation**

Torque uses the perpendicular distance from the pivot to a force's line of action.

The wall force $N_w$ is horizontal, so its lever arm is the top's vertical height:

$$
r_{\perp,w}=L\sin\theta.
$$

Relative to the ground angle $\theta$, this vertical height is the side opposite $\theta$.

The weight is vertical and acts at the midpoint, so its lever arm is the midpoint's horizontal distance:

$$
r_{\perp,g}=\frac L2\cos\theta.
$$

This horizontal midpoint distance is adjacent to $\theta$ and includes the factor $\frac12$ because a uniform ladder's weight acts at its center.

The torques oppose each other. Setting their magnitudes equal gives

$$
N_wL\sin\theta
=mg\frac L2\cos\theta.
$$

Solving for the wall force,

$$
N_w=\frac{mg}{2}\frac{\cos\theta}{\sin\theta}
=\frac{mg}{2}\cot\theta.
$$

Here $\cot\theta=\cos\theta/\sin\theta$, the adjacent-to-opposite ratio.

```quiz
type: radio
id: p3-torque-equation
content: |-
  Which equation correctly balances torques about the bottom of a uniform ladder of length $L$ at angle $\theta$ against a frictionless wall?
options:
- id: p3-torque-a
  content: |-
    $N_wL\sin\theta=mg\dfrac L2\cos\theta$
  correct: true
  feedback: |-
    The horizontal wall force uses vertical lever arm $L\sin\theta$; the weight acts at the midpoint and uses horizontal lever arm $(L/2)\cos\theta$.
- id: p3-torque-b
  content: |-
    $N_wL\cos\theta=mg\dfrac L2\sin\theta$
- id: p3-torque-c
  content: |-
    $N_wL\sin\theta=mgL\cos\theta$
- id: p3-torque-d
  content: |-
    $N_w\dfrac L2\sin\theta=mgL\cos\theta$
- id: p3-torque-e
  content: |-
    $N_wL=mgL$
```

---

<a id="turn-force-balance-into-a-friction-ratio"></a>
## Turn Force Balance Into a Friction Ratio

**Example:** Use force equilibrium and impending slip to obtain the minimum coefficient of static friction.

**Explanation**

Horizontal equilibrium requires friction at the floor to balance the wall's normal force:

$$
f_s=N_w.
$$

The frictionless wall supplies no vertical force, so vertical equilibrium gives

$$
N_g=mg.
$$

At the threshold of slipping, $f_s=\mu_sN_g$. Therefore,

$$
\mu_s
=\frac{f_s}{N_g}
=\frac{N_w}{mg}
=\frac12\cot\theta.
$$

This dimensionless ratio shows why the ladder's mass and length cancel.

It also gives a physical trend check: as the ladder becomes steeper, $\theta$ increases, $\cot\theta$ decreases, and less floor friction is required.

```quiz
type: radio
id: p3-friction-ratio
content: |-
  What minimum static-friction coefficient is required for a uniform ladder at $\theta=60^\circ$ against a frictionless wall?
options:
- id: p3-friction-a
  content: |-
    $0.29$
  correct: true
  feedback: |-
    Use $\mu_s=\frac12\cot\theta$: $\mu_s=\frac12\cot60^\circ=0.2887\ldots\approx0.29$. Be sure the calculator is in degree mode.
- id: p3-friction-b
  content: |-
    $0.58$
- id: p3-friction-c
  content: |-
    $0.87$
- id: p3-friction-d
  content: |-
    $1.73$
- id: p3-friction-e
  content: |-
    $0.50$
```

---

<a id="apply-the-method-to-problem-3"></a>
## Apply the Method to Problem 3

**Example:** A uniform ladder of mass $m$ and length $L$ leans against a frictionless wall at an angle $\theta$. Find the minimum coefficient of static friction between the ladder and the ground that prevents slipping.

Use $m=4.5\ \mathrm{kg}$, $L=2.8\ \mathrm{m}$, and $\theta=52^\circ$.

![](<../Source/Images/ladder-against-frictionless-wall.png>)

**Explanation**

Taking torques about the ladder's bottom gives

$$
N_wL\sin\theta=mg\frac{L}{2}\cos\theta,
\qquad
N_w=\frac{mg}{2}\cot\theta.
$$

Horizontal equilibrium requires $f_s=N_w$, while vertical equilibrium gives $N_g=mg$. At impending slip,

$$
\mu_s=\frac{f_s}{N_g}=\frac12\cot\theta.
$$

Thus,

$$
\mu_s=\frac12\cot(52^\circ)=0.39064\ldots\approx0.39.
$$

The mass and length cancel, and the angle supports two significant figures.

The answer choices diagnose common mistakes:

- $0.78$ omits the factor $\frac12$ from the ladder's midpoint center of mass.
- $0.64$ uses $\frac12\tan\theta$, swapping the sine and cosine lever arms.
- $1.28$ uses $\tan\theta$ and also omits the midpoint factor.
- $0.31$ uses $\frac12\cos\theta$ rather than the ratio $\frac12\cot\theta$.

```quiz
type: radio
id: p3-source-check
content: |-
  **Question 2**

  A uniform ladder of mass $m$ and length $L$ leans against a frictionless wall at an angle $\theta$. Find the minimum coefficient of static friction between the ladder and the ground that prevents slipping.

  Use $m=4.5\ \mathrm{kg}$, $L=2.8\ \mathrm{m}$, and $\theta=52^\circ$.

  ![](<../Source/Images/ladder-against-frictionless-wall.png>)

  Enter the coefficient as a number only:
options:
- id: p3-source-a
  content: |-
    $0.39$
  correct: true
  feedback: |-
    Taking torques about the ladder's bottom gives

    $$
    N_wL\sin\theta=mg\frac{L}{2}\cos\theta,
    \qquad
    N_w=\frac{mg}{2}\cot\theta.
    $$

    Horizontal equilibrium requires $f_s=N_w$, while vertical equilibrium gives $N_g=mg$. At impending slip,

    $$
    \mu_s=\frac{f_s}{N_g}=\frac12\cot\theta.
    $$

    Thus,

    $$
    \mu_s=\frac12\cot(52^\circ)=0.39064\ldots\approx0.39.
    $$

    The mass and length cancel, and the angle supports two significant figures.
- id: p3-source-b
  content: |-
    $0.78$
- id: p3-source-c
  content: |-
    $0.64$
- id: p3-source-d
  content: |-
    $1.28$
- id: p3-source-e
  content: |-
    $0.31$
```

---

## Summary

- Cue: a uniform ladder rests against a frictionless wall, and the minimum floor friction is requested.
- Pivot at the bottom so the ground forces produce no torque.
- Use lever arms $L\sin\theta$ for $N_w$ and $(L/2)\cos\theta$ for $mg$.
- Apply $f_s=N_w$, $N_g=mg$, and $f_s=\mu_sN_g$ at impending slip.
- The reusable result is $\mu_s=\frac12\cot\theta$; a larger $\theta$ should produce a smaller coefficient.
- Use degree mode and round only at the end.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
