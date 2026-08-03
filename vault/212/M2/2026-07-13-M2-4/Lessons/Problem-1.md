# Balancing a Plank With Opposing Torques

<!--
lesson-id: 212-M2-027
topic-code: MTH212.M2.27
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Fulcrum as the Pivot](#choose-the-fulcrum-as-the-pivot)
- [Compute Perpendicular Torque](#compute-perpendicular-torque)
- [Balance the Opposing Torques](#balance-the-opposing-torques)
- [Check the Mass-Distance Relationship](#check-the-mass-distance-relationship)
- [Apply the Method](#apply-the-method)
- [Summary](#summary)

## Prerequisites

- Use the torque magnitude $\tau=rF\sin\theta$.
- Use weight $F_g=mg$.
- Solve a one-variable proportion.
- Round a result to the significant figures supported by measured data.

---

<a id="introduction"></a>
## Introduction

A balanced plank is in rotational equilibrium, so the net torque about any chosen pivot is zero. Choosing the fulcrum as the pivot removes the unknown support force because its lever arm is zero.

For a horizontal plank with downward weights, each force is perpendicular to its lever arm. The two boxes balance when their opposite torque magnitudes are equal:

$$
m_1gr_1=m_2gr_2.
$$

Canceling $g$ gives the reusable relation

$$
\boxed{m_2=\frac{m_1r_1}{r_2}}.
$$

The recognition cue is a balanced object with forces on opposite sides of a pivot.

| Given information | How it is used |
|---|---|
| the system is balanced | set the net torque to zero |
| the fulcrum is at the plank's center | the uniform plank's weight has zero lever arm |
| $m_1$ and $r_1$ | form the known torque magnitude $m_1gr_1$ |
| $r_2$ | divide the known mass-distance product by $r_2$ |
| plank mass $2.6\ \mathrm{kg}$ | do not insert it; its torque about the fulcrum is zero |

---

<a id="choose-the-fulcrum-as-the-pivot"></a>
## Choose the Fulcrum as the Pivot

**Example:** A uniform plank is supported exactly at its center. Does the plank's own weight produce torque about the fulcrum?

**Explanation**

A uniform plank's weight acts at its center of mass. Here the center of mass and the fulcrum coincide, so the perpendicular lever arm is zero:

$$
\tau_{\text{plank}}=r_\perp Mg=(0)Mg=0.
$$

The plank's mass may be given, but it does not enter the torque-balance equation in this geometry. The support force also acts at the pivot and has zero torque about it.

```quiz
type: radio
id: m2-4-p1-zero-torque
content: |-
  A uniform horizontal plank is supported at its center. What torque does the plank's weight exert about that support point?
options:
- id: a
  content: |-
    Zero, because the weight's line of action passes through the pivot
  correct: true
  feedback: |-
    The uniform plank's weight acts at its center, which is the pivot. A force whose line of action passes through the pivot has zero lever arm and therefore zero torque.
- id: b
  content: |-
    $MgL$
- id: c
  content: |-
    $MgL/2$
- id: d
  content: |-
    $Mg/L$
- id: e
  content: |-
    It cannot be determined without the support force.
```

---

<a id="compute-perpendicular-torque"></a>
## Compute Perpendicular Torque

**Example:** A downward force of $4.0\ \mathrm{N}$ acts $0.75\ \mathrm{m}$ horizontally from a pivot. Find the torque magnitude.

**Explanation**

The lever arm is horizontal and the force is vertical, so the angle between them is $90^\circ$. Therefore,

$$
\begin{aligned}
\tau
&=rF\sin90^\circ\\
&=(0.75)(4.0)(1)\\
&=3.0\ \mathrm{N\,m}.
\end{aligned}
$$

For a box of mass $m$ on a horizontal plank, $F=mg$, so its torque magnitude is $mgr$.

```quiz
type: radio
id: m2-4-p1-perpendicular-torque
content: |-
  A downward force of $6.0\ \mathrm{N}$ acts $0.40\ \mathrm{m}$ horizontally from a pivot. What is the torque magnitude?
options:
- id: a
  content: |-
    $2.4\ \mathrm{N\,m}$
  correct: true
  feedback: |-
    The force is perpendicular to the lever arm, so $\tau=rF=(0.40)(6.0)=2.4\ \mathrm{N\,m}$.
- id: b
  content: |-
    $15\ \mathrm{N\,m}$
- id: c
  content: |-
    $6.4\ \mathrm{N\,m}$
- id: d
  content: |-
    $5.6\ \mathrm{N\,m}$
- id: e
  content: |-
    $0\ \mathrm{N\,m}$
```

---

<a id="balance-the-opposing-torques"></a>
## Balance the Opposing Torques

**Example:** A $2.0\ \mathrm{kg}$ box is $1.5\ \mathrm{m}$ to the left of a fulcrum. What mass placed $0.75\ \mathrm{m}$ to the right balances the plank?

**Explanation**

Choose counterclockwise as positive. The two weights create torques in opposite directions, so equilibrium requires

$$
m_1gr_1-m_2gr_2=0.
$$

Equivalently, their magnitudes are equal:

$$
m_1gr_1=m_2gr_2.
$$

Cancel $g$ and solve:

$$
\begin{aligned}
m_2
&=\frac{m_1r_1}{r_2}\\
&=\frac{(2.0)(1.5)}{0.75}\\
&=4.0\ \mathrm{kg}.
\end{aligned}
$$

```quiz
type: radio
id: m2-4-p1-balance-equation
content: |-
  A $3.0\ \mathrm{kg}$ box is $0.80\ \mathrm{m}$ from a fulcrum. What mass placed $1.2\ \mathrm{m}$ on the opposite side balances it?
options:
- id: a
  content: |-
    $2.0\ \mathrm{kg}$
  correct: true
  feedback: |-
    Equal opposing torques give $m_2=m_1r_1/r_2=(3.0)(0.80)/(1.2)=2.0\ \mathrm{kg}$.
- id: b
  content: |-
    $4.5\ \mathrm{kg}$
- id: c
  content: |-
    $3.0\ \mathrm{kg}$
- id: d
  content: |-
    $0.50\ \mathrm{kg}$
- id: e
  content: |-
    $3.8\ \mathrm{kg}$
```

---

<a id="check-the-mass-distance-relationship"></a>
## Check the Mass-Distance Relationship

**Example:** One box is farther from the fulcrum than the other. Which box must be heavier if the plank balances?

**Explanation**

Balance keeps the product $mr$ equal on the two sides:

$$
m_1r_1=m_2r_2.
$$

For a fixed balancing torque, mass varies inversely with distance. The box closer to the fulcrum must be heavier. If $r_2<r_1$, then

$$
\frac{r_1}{r_2}>1
\quad\Longrightarrow\quad
m_2=m_1\frac{r_1}{r_2}>m_1.
$$

This is a quick reasonableness check before accepting a numerical answer.

```quiz
type: radio
id: m2-4-p1-reasonableness
content: |-
  Two boxes balance on opposite sides of a fulcrum. Box 2 is half as far from the fulcrum as Box 1. How must their masses compare?
options:
- id: a
  content: |-
    $m_2=2m_1$
  correct: true
  feedback: |-
    Since $m_1r_1=m_2r_2$ and $r_2=r_1/2$, $m_2=m_1r_1/(r_1/2)=2m_1$.
- id: b
  content: |-
    $m_2=m_1/2$
- id: c
  content: |-
    $m_2=m_1$
- id: d
  content: |-
    $m_2=4m_1$
- id: e
  content: |-
    $m_2=m_1/4$
```

---

<a id="apply-the-method"></a>
## Apply the Method

**Example:** Find the mass of Box 2 for the given balanced plank.

**Explanation**

The plank is uniform and supported at its center, so its weight has zero torque about the fulcrum. Set the box torque magnitudes equal:

$$
m_1gr_1=m_2gr_2.
$$

Then

$$
m_2=\frac{m_1r_1}{r_2}.
$$

Evaluate the grouped pieces before rounding:

| Piece | Calculation | Value |
|---|---|---:|
| known mass-distance product | $(1.6)(1.7)$ | $2.72\ \mathrm{kg\,m}$ |
| unknown mass | $2.72/1.1$ | $2.4727\ldots\ \mathrm{kg}$ |

The units also check:

$$
\frac{\mathrm{kg\,m}}{\mathrm{m}}=\mathrm{kg}.
$$

Because Box 2 is closer to the fulcrum than Box 1, it should be heavier than $1.6\ \mathrm{kg}$; the calculation passes that check. The measured values have two significant figures, so report $2.5\ \mathrm{kg}$.

```quiz
type: radio
id: m2-4pre-q1
content: |-
  **Question 1**

  A $2.6\ \mathrm{kg}$ plank is balanced on a fulcrum at its center. Two boxes are placed on the plank so the system remains balanced.

  Box 1 has mass $m_1=1.6\ \mathrm{kg}$ and is placed $r_1=1.7\ \mathrm{m}$ from the fulcrum. Box 2 is placed $r_2=1.1\ \mathrm{m}$ from the fulcrum.

  ![](<../Source/Images/balanced-plank-two-boxes.png>)

  Enter the mass of Box 2 in kilograms as a number only:
options:
- id: a
  content: |-
    `2.5`
  correct: true
  feedback: |-
    The plank's weight acts through the fulcrum and therefore produces no torque about it. Balance requires equal torque magnitudes:

    $$
    m_1gr_1=m_2gr_2.
    $$

    Therefore,

    $$
    m_2=\frac{m_1r_1}{r_2}
    =\frac{(1.6)(1.7)}{1.1}
    =2.4727\ldots\ \mathrm{kg}.
    $$

    The measured givens each have two significant figures, so $m_2=2.5\ \mathrm{kg}$.
- id: b
  content: |-
    `1.0`
- id: c
  content: |-
    `6.5`
- id: d
  content: |-
    `1.6`
- id: e
  content: |-
    `2.47`
```

---

<a id="summary"></a>
## Summary

- **Cue:** a horizontal plank is balanced with weights on opposite sides of a fulcrum.
- **Choose the pivot:** use the fulcrum so the support force has zero torque.
- **Ignore zero-lever-arm forces:** here the uniform plank's weight also acts through the pivot.
- **Torque:** perpendicular weight gives $\tau=mgr$.
- **Balance:** $m_1gr_1=m_2gr_2$, so $m_2=m_1r_1/r_2$.
- **Evaluate:** group $m_1r_1$ first, divide by $r_2$, and round only the final result.
- **Check:** the box closer to the pivot must be heavier.
- **Main trap:** a given plank mass does not matter when its center of mass lies at the fulcrum.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
