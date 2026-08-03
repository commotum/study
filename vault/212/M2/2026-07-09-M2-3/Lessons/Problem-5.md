# Finding a Spool's Angular Acceleration From Tension

<!--
lesson-id: 212-M2-015
topic-code: MTH212.M2.15
-->

## Table of Contents

- [Introduction](#introduction)
- [Draw the Force and Torque Diagrams](#draw-the-force-and-torque-diagrams)
- [Combine Torque With Rotational Inertia](#combine-torque-with-rotational-inertia)
- [Convert the Radius Before Substitution](#convert-the-radius-before-substitution)
- [Calculate Magnitude and Direction](#calculate-magnitude-and-direction)
- [Apply the Method to the Spool](#apply-the-method-to-the-spool)
- [Summary](#summary)

## Prerequisites

- Use $\sum\tau=I\alpha$ for rotation about a fixed axle.
- Recognize that a tangential force at radius $r$ has torque magnitude $rF$.
- Use the solid-cylinder moment of inertia $I=\frac12mr^2$.
- Convert centimeters to meters and round a final result to the precision of measured data.

---

<a id="introduction"></a>
## Introduction

When a cord is pulled tangent to a solid-cylinder spool, find the torque about the axle, pair it with the spool's rotational inertia, and simplify before inserting numbers:

$$
\sum\tau=I\alpha,
\qquad
\tau_T=Tr,
\qquad
I=\frac12mr^2.
$$

These equations give the reusable result

$$
\alpha=\frac{\tau_T}{I}
=\frac{Tr}{\frac12mr^2}
=\frac{2T}{mr}.
$$

The important recognition cue is a tangential force applied at the rim while the other forces act through the axle. Only the tangential tension contributes torque about that axle.

---

<a id="draw-the-force-and-torque-diagrams"></a>
## Draw the Force and Torque Diagrams

**Example:** A cord pulls tangentially on a spool mounted on a freely spinning axle. Identify the forces and decide which ones produce torque about the axle.

**Explanation**

The ordinary free-body diagram contains:

- the cord tension $T$, tangent to the spool;
- the weight $mg$, acting through the center; and
- the axle or support force, acting through the center.

The extended free-body diagram records each force's line of action and perpendicular lever arm:

| Force | Lever arm about axle | Torque about axle |
|---|---:|---:|
| Tension $T$ | $r$ | $Tr$ |
| Weight $mg$ | $0$ | $0$ |
| Axle/support force | $0$ | $0$ |

The center-acting forces matter for translational force balance, but they do not appear in the torque sum about the axle.

```quiz
type: radio
id: m2-3-p5-torque-source
shuffle: true
content: |-
  A cord pulls tangentially at the rim of a spool on a fixed, frictionless axle. The spool's weight and the axle force both act through its center. Which force contributes a nonzero torque about the axle?
options:
- id: a
  content: |-
    The tension only
  correct: true
  feedback: |-
    The tension has perpendicular lever arm $r$. The weight and axle force pass through the rotation axis, so each has zero lever arm.
- id: b
  content: |-
    The weight only
- id: c
  content: |-
    The axle force only
- id: d
  content: |-
    The weight and axle force only
- id: e
  content: |-
    All three forces
```

---

<a id="combine-torque-with-rotational-inertia"></a>
## Combine Torque With Rotational Inertia

**Example:** Derive the angular acceleration of a solid-cylinder spool of mass $m$ and radius $r$ pulled by a tangential cord tension $T$.

**Explanation**

Start from rotational Newton's second law and substitute the expressions for torque and inertia:

$$
Tr=\left(\frac12mr^2\right)\alpha.
$$

Solve for $\alpha$ and expose the common radius factor:

$$
\begin{aligned}
\alpha
&=\frac{Tr}{\frac12mr^2}\\
&=\frac{2Tr}{mr^2}\\
&=\frac{2T}{mr}.
\end{aligned}
$$

Only one factor of $r$ cancels. One remains in the denominator because the inertia contains $r^2$ while the torque contains $r$.

```quiz
type: radio
id: m2-3-p5-derive
shuffle: true
content: |-
  A tangential tension $T$ pulls a solid-cylinder spool of mass $m$ and radius $r$. Which expression gives the spool's angular acceleration magnitude?
options:
- id: a
  content: |-
    $\dfrac{Tr}{m}$
- id: b
  content: |-
    $\dfrac{2T}{mr}$
  correct: true
  feedback: |-
    Use $Tr=(\frac12mr^2)\alpha$. Dividing by $\frac12mr^2$ and canceling one factor of $r$ gives $\alpha=2T/(mr)$.
- id: c
  content: |-
    $\dfrac{T}{2mr}$
- id: d
  content: |-
    $\dfrac{2T}{m}$
- id: e
  content: |-
    $\dfrac{T}{mr^2}$
```

---

<a id="convert-the-radius-before-substitution"></a>
## Convert the Radius Before Substitution

**Example:** Convert a spool radius of $2.4\ \mathrm{cm}$ to meters.

**Explanation**

Use a conversion factor whose centimeter units cancel:

$$
2.4\ \mathrm{cm}
\left(\frac{1\ \mathrm{m}}{100\ \mathrm{cm}}\right)
=0.024\ \mathrm{m}.
$$

The formula $\alpha=2T/(mr)$ produces SI units only when the radius is in meters. Dividing by $100$ changes centimeters to meters.

```quiz
type: radio
id: m2-3-p5-radius-conversion
shuffle: true
content: |-
  What value should replace $r=3.5\ \mathrm{cm}$ when using $\alpha=2T/(mr)$ with force in newtons and mass in kilograms?
options:
- id: a
  content: |-
    $0.0035\ \mathrm{m}$
- id: b
  content: |-
    $0.035\ \mathrm{m}$
  correct: true
  feedback: |-
    Multiply by $1\ \mathrm{m}/(100\ \mathrm{cm})$. The centimeter units cancel and $3.5/100=0.035$.
- id: c
  content: |-
    $0.35\ \mathrm{m}$
- id: d
  content: |-
    $35\ \mathrm{m}$
- id: e
  content: |-
    $350\ \mathrm{m}$
```

---

<a id="calculate-magnitude-and-direction"></a>
## Calculate Magnitude and Direction

**Example:** A $0.48\ \mathrm{N}$ tension pulls tangentially on a solid-cylinder spool with $m=3.0\ \mathrm{kg}$ and $r=2.0\ \mathrm{cm}$. Find the angular acceleration magnitude.

**Explanation**

First convert $r=0.020\ \mathrm{m}$, then substitute into the simplified formula:

$$
\begin{aligned}
\alpha
&=\frac{2T}{mr}\\
&=\frac{2(0.48\ \mathrm{N})}{(3.0\ \mathrm{kg})(0.020\ \mathrm{m})}\\
&=16\ \mathrm{rad/s^2}.
\end{aligned}
$$

The unit check is

$$
\frac{\mathrm{N}}{\mathrm{kg}\cdot\mathrm{m}}
=\frac{\mathrm{kg}\cdot\mathrm{m}/\mathrm{s^2}}{\mathrm{kg}\cdot\mathrm{m}}
=\mathrm{s^{-2}},
$$

which is written as $\mathrm{rad/s^2}$ for angular acceleration. Determine the rotation direction separately with the right-hand rule. A rightward pull at the top of the spool produces clockwise rotation, with angular acceleration into the page.

The simplified formula also gives a fast reasonableness check:

| Change, with other quantities fixed | Prediction from $\alpha=2T/(mr)$ |
|---|---|
| Increase $T$ | $\alpha$ increases in direct proportion |
| Increase $m$ | $\alpha$ decreases in inverse proportion |
| Increase $r$ | $\alpha$ decreases in inverse proportion |

The last row may seem surprising because the torque $Tr$ grows with radius. However, the solid cylinder's inertia grows as $r^2$, so inertia grows faster than torque and the net result is $\alpha\propto1/r$.

```quiz
type: radio
id: m2-3-p5-calculate
shuffle: true
content: |-
  A cord is pulled to the right at the top of a solid-cylinder spool. If $T=0.60\ \mathrm{N}$, $m=4.0\ \mathrm{kg}$, and $r=2.5\ \mathrm{cm}$, what are the angular acceleration magnitude and direction?
options:
- id: a
  content: |-
    $12\ \mathrm{rad/s^2}$, clockwise into the page
  correct: true
  feedback: |-
    Convert $r=0.025\ \mathrm{m}$. Then $\alpha=2(0.60)/[(4.0)(0.025)]=12\ \mathrm{rad/s^2}$. The rightward tangential pull at the top produces clockwise rotation, into the page.
- id: b
  content: |-
    $12\ \mathrm{rad/s^2}$, counterclockwise out of the page
- id: c
  content: |-
    $6.0\ \mathrm{rad/s^2}$, clockwise into the page
- id: d
  content: |-
    $1200\ \mathrm{rad/s^2}$, clockwise into the page
- id: e
  content: |-
    $0.030\ \mathrm{rad/s^2}$, counterclockwise out of the page
```

---

<a id="apply-the-method-to-the-spool"></a>
## Apply the Method to the Spool

**Example:** Use the force diagram and extended force diagram to calculate the angular acceleration for the given spool.

**Explanation**

The tension is tangent to the rim, so its lever arm is $r$ and its torque magnitude is $Tr$. The weight and axle/support force act through the center and contribute no torque about the axle. For a solid cylinder,

$$
\alpha=\frac{Tr}{\frac12mr^2}=\frac{2T}{mr}.
$$

Convert the radius before substitution:

$$
1.6\ \mathrm{cm}=0.016\ \mathrm{m}.
$$

Then

$$
\begin{aligned}
\alpha
&=\frac{2(0.35\ \mathrm{N})}{(2.8\ \mathrm{kg})(0.016\ \mathrm{m})}\\
&=15.625\ \mathrm{rad/s^2}\\
&\approx16\ \mathrm{rad/s^2}.
\end{aligned}
$$

Keep the calculation value and the reported value distinct:

| Stage | Value |
|---|---:|
| Calculator result | $15.625\ \mathrm{rad/s^2}$ |
| Reported to two significant figures | $16\ \mathrm{rad/s^2}$ |

The final answer is $16\ \mathrm{rad/s^2}$, clockwise and into the page. This is consistent with the formula: a modest force acting on a very small radius can produce a sizable angular acceleration.

```quiz
type: radio
id: m2-3lec-q4
shuffle: true
content: |-
  **Question 4**

  A person pulls a cord with constant tension $T$. The cord is wrapped around a freely spinning solid-cylinder spool of radius $r$ and mass $m$. Find the spool's angular acceleration. Begin by drawing a free-body diagram and an extended free-body diagram.

  Use $T=0.35\ \mathrm{N}$, $r=1.6\ \mathrm{cm}$, and $m=2.8\ \mathrm{kg}$.

  ![](<../Source/Images/cord-pulled-solid-cylinder-spool.png>)

  Enter the angular acceleration magnitude in radians per second squared as a number only:
options:
- id: a
  content: |-
    `16`
  correct: true
  feedback: |-
    The free-body diagram should include the tangential tension, the weight through the center, and the axle/support force through the center. The extended diagram should show tension acting with perpendicular lever arm $r$; the other forces produce no torque about the axle.

    Thus,

    $$
    \tau=Tr,
    \qquad
    I=\frac12mr^2,
    \qquad
    \alpha=\frac{\tau}{I}=\frac{2T}{mr}.
    $$

    With $r=0.016\ \mathrm{m}$,

    $$
    \alpha=\frac{2(0.35\ \mathrm{N})}{(2.8\ \mathrm{kg})(0.016\ \mathrm{m})}
    =15.625\ \mathrm{rad/s^2}.
    $$

    The measured givens have two significant figures, so $\alpha=16\ \mathrm{rad/s^2}$. The angular acceleration is clockwise, into the page.
- id: b
  content: |-
    `15.625`
- id: c
  content: |-
    `7.8`
- id: d
  content: |-
    `1600`
- id: e
  content: |-
    `0.016`
```

---

<a id="summary"></a>
## Summary

- Draw both diagrams and take torque about the axle so center-acting forces drop out.
- For tangential tension, use $\tau=Tr$; for a solid cylinder, use $I=\frac12mr^2$.
- Simplify to $\alpha=2T/(mr)$ before substituting, canceling only one factor of $r$.
- Convert the radius from centimeters to meters, carry extra digits, and round only the final result.
- Use the right-hand rule separately to report clockwise/into-page or counterclockwise/out-of-page direction.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
