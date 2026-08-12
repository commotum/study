# Period of a Uniform Rod as a Physical Pendulum

<!--
lesson-id: 212-M4-012
topic-code: MTH212.M4.12
-->

## Table of Contents

- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Choose the Physical-Pendulum Quantities](#choose-the-physical-pendulum-quantities)
- [Substitute and Cancel Symbolically](#substitute-and-cancel-symbolically)
- [Evaluate and Check the Result](#evaluate-and-check-the-result)
- [Apply the Method to Problem 3](#apply-the-method-to-problem-3)
- [Summary](#summary)

## Prerequisites

- Use the small-angle physical-pendulum period formula.
- Identify a rigid body's center of mass and moment of inertia about its pivot.
- Simplify fractions and square roots.
- Round a calculated result to the precision supported by measured givens.

---

<a id="introduction"></a>
## Introduction

When a rigid rod swings through a small angle about a fixed pivot and the problem asks for its period, treat it as a physical pendulum rather than a point-mass pendulum. Determine the period by choosing the moment of inertia about the pivot and the pivot-to-center-of-mass distance, then substitute those quantities into the physical-pendulum formula and simplify.

---

<a id="choose-the-physical-pendulum-quantities"></a>
## Choose the Physical-Pendulum Quantities

**Recognition cue:** A rigid object swings about a pivot and the angle is small, so use the physical-pendulum formula

$$
T=2\pi\sqrt{\frac{I_p}{mg\ell}}.
$$

Here $I_p$ must be the moment of inertia **about the pivot**, and $\ell$ is the distance from the pivot to the center of mass.

For a uniform rod of length $L$ pivoted at one end,

$$
I_p=\frac13mL^2
\qquad\text{and}\qquad
\ell=\frac L2.
$$

The pivot location matters. The value $I_{\mathrm{cm}}=\frac1{12}mL^2$ is the rod's moment of inertia about its center, not about an end.

**Example:** A uniform rod of length $L$ swings about a pivot at one end. Which pair belongs in the physical-pendulum formula?

**Explanation**

The rod's center of mass is halfway along the rod, while the relevant moment of inertia is measured about the end pivot.

```quiz
type: radio
id: p3-rod-quantities
content: |-
  For a uniform rod of length $L$ pivoted at one end, which values should be used in $T=2\pi\sqrt{I_p/(mg\ell)}$?
options:
- id: p3-rod-quantities-a
  content: |-
    $I_p=\frac13mL^2$ and $\ell=\frac L2$
  correct: true
  feedback: |-
    A physical pendulum uses the center-of-mass lever arm and the moment of inertia about the actual pivot. For a uniform rod pivoted at one end, the center of mass is $L/2$ away and $I_p=\frac13mL^2$.
- id: p3-rod-quantities-b
  content: |-
    $I_{\mathrm{cm}}=\frac1{12}mL^2$ and $\ell=\frac L2$
  feedback: |-
    The distance $\ell=L/2$ is correct, but the inertia is about the wrong axis. $\frac1{12}mL^2$ applies through the rod's center; shifting to the end pivot gives $I_p=\frac13mL^2$.
- id: p3-rod-quantities-c
  content: |-
    $I_p=\frac13mL^2$ and $\ell=L$
  feedback: |-
    The end-pivot inertia is correct, but $\ell$ is the distance from the pivot to the center of mass, not to the rod's far end. A uniform rod balances at its midpoint, so $\ell=L/2$ rather than $L$.
- id: p3-rod-quantities-d
  content: |-
    $I_p=mL^2$ and $\ell=L$
  feedback: |-
    This replaces the distributed rod with a point mass at its far end. The actual rod has its center of mass at $L/2$ and its mass spread along its length, giving $\ell=L/2$ and $I_p=\frac13mL^2$.
```

---

<a id="substitute-and-cancel-symbolically"></a>
## Substitute and Cancel Symbolically

Insert the rod formulas before inserting numerical values:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{I_p}{mg\ell}}\\
&=2\pi\sqrt{
\frac{\frac13mL^2}{mg\left(\frac L2\right)}
}\\
&=2\pi\sqrt{
\left(\frac{mL^2}{3}\right)
\left(\frac{2}{mgL}\right)
}\\
&=2\pi\sqrt{
\frac{2}{3g}
\left(\frac{m}{m}\right)
\left(\frac{L^2}{L}\right)
}\\
&=2\pi\sqrt{\frac{2L}{3g}}.
\end{aligned}
$$

The factor $m$ cancels, and one factor of $L$ cancels. Therefore, the period is independent of the rod's mass.

**Example:** If two uniform rods have the same length and both pivot at one end, but one rod has twice the mass, their small-angle periods are equal.

**Explanation**

Both $I_p$ and the gravitational torque scale with $m$, so their ratio does not depend on mass.

```quiz
type: radio
id: p3-mass-cancels
content: |-
  Two uniform rods have the same length and pivot at one end. Rod 2 has three times the mass of Rod 1. How do their small-angle periods compare?
options:
- id: p3-mass-cancels-a
  content: |-
    Rod 2 has three times the period.
  feedback: |-
    This assumes that greater mass directly makes the oscillation slower. For geometrically identical rods, both rotational inertia and gravitational restoring torque grow by the same mass factor, so $m$ cancels from $I_p/(mg\ell)$ and the periods remain equal.
- id: p3-mass-cancels-b
  content: |-
    Rod 2 has $\sqrt{3}$ times the period.
  feedback: |-
    This keeps a factor of $3$ from the heavier rod under the square root. But $I_p$ and $mg\ell$ each acquire that same factor, so their ratio—and therefore the period—does not gain a factor of $\sqrt3$.
- id: p3-mass-cancels-c
  content: |-
    The rods have equal periods.
  correct: true
  feedback: |-
    For the same rod shape and pivot, increasing mass increases both rotational inertia and gravitational restoring torque proportionally. Thus $m$ cancels from $T=2\pi\sqrt{I_p/(mg\ell)}$, so the two rods have equal periods.
- id: p3-mass-cancels-d
  content: |-
    Rod 2 has one-third the period.
  feedback: |-
    This assumes the heavier rod swings three times faster because its weight is larger. Its rotational inertia is also three times larger, so the restoring effect and resistance to angular acceleration scale together; the period stays the same.
```

---

<a id="evaluate-and-check-the-result"></a>
## Evaluate and Check the Result

Once the rod-specific formula is simplified, substitute $L$ and $g$:

$$
T=2\pi\sqrt{\frac{2L}{3g}}.
$$

Use this calculator order:

1. Evaluate the radicand $2L/(3g)$ with parentheses around substituted values.
2. Take the positive square root.
3. Multiply by $2\pi$.
4. Round only the final result.

The units provide a quick check:

$$
\sqrt{\frac{\mathrm{m}}{\mathrm{m}/\mathrm{s}^2}}
=\sqrt{\mathrm{s}^2}
=\mathrm{s}.
$$

Also, $T\propto\sqrt L$: a longer rod has a longer period, while changing only the mass does nothing.

**Example:** For $L=0.60\ \mathrm{m}$ and $g=9.81\ \mathrm{m}/\mathrm{s}^2$,

$$
T=2\pi\sqrt{\frac{2(0.60)}{3(9.81)}}=1.27\ldots\ \mathrm{s}.
$$

**Explanation**

Keep extra calculator digits until the final rounding step.

```quiz
type: radio
id: p3-evaluate-period
content: |-
  A uniform rod of length $0.75\ \mathrm{m}$ pivots at one end. Using $g=9.81\ \mathrm{m}/\mathrm{s}^2$, what is its small-angle period?
options:
- id: p3-evaluate-period-a
  content: |-
    $1.42\ \mathrm{s}$
  correct: true
  feedback: |-
    A uniform rod about an end has $I_p=\frac13mL^2$ and $\ell=L/2$, so its period reduces to $T=2\pi\sqrt{2L/(3g)}$. With $L=0.75\ \mathrm{m}$, this gives $T=1.418\ldots\ \mathrm{s}\approx1.42\ \mathrm{s}$.
- id: p3-evaluate-period-b
  content: |-
    $1.74\ \mathrm{s}$
  feedback: |-
    This treats the rod as a point bob located a full length $L$ from the pivot. A rod is an extended object, so its end-pivot inertia and midpoint center of mass give $T=2\pi\sqrt{2L/(3g)}=1.42\ \mathrm{s}$.
- id: p3-evaluate-period-c
  content: |-
    $0.71\ \mathrm{s}$
  feedback: |-
    This is exactly half the rod's period and results from using $\pi$ instead of the required prefactor $2\pi$. The physical-pendulum formula gives $2\pi\sqrt{2(0.75)/(3(9.81))}=1.42\ \mathrm{s}$.
- id: p3-evaluate-period-d
  content: |-
    $4.02\ \mathrm{s}$
  feedback: |-
    This reflects a numerical or grouping error in the physical-pendulum calculation. Keeping the denominator grouped gives $2L/(3g)=0.05097\ \mathrm{s}^2$; its square root is $0.2258\ \mathrm{s}$, and multiplying by $2\pi$ gives $1.42\ \mathrm{s}$, not $4.02\ \mathrm{s}$.
```

---

<a id="apply-the-method-to-problem-3"></a>
## Apply the Method to Problem 3

**Example:** A uniform rod of mass $m$ and length $L$ swings about a pivot at one end. Find its small-angle oscillation period for $L=0.92\ \mathrm{m}$ and $m=0.037\ \mathrm{kg}$.

![](<../Source/Images/uniform-rod-end-pivot.png>)

**Explanation**

For a physical pendulum,

$$
T=2\pi\sqrt{\frac{I_p}{mg\ell}}.
$$

A uniform rod pivoted at one end has $I_p=\frac13mL^2$ and $\ell=L/2$, so

$$
T=2\pi\sqrt{\frac{2L}{3g}}
=2\pi\sqrt{\frac{2(0.92\ \mathrm{m})}{3(9.81\ \mathrm{m}/\mathrm{s}^2)}}
=1.5711\ldots\ \mathrm{s}.
$$

In calculator-sized stages,

$$
\frac{2(0.92)}{3(9.81)}=0.06252\ldots,
\qquad
\sqrt{0.06252\ldots}=0.2500\ldots,
$$

then $2\pi(0.2500\ldots)=1.5711\ldots$. This staging makes a missing square root or a misplaced parenthesis easier to catch.

The measured length has two significant figures, so $T=1.6\ \mathrm{s}$. The rod's mass cancels.

The requested answer form is: **Enter the period in seconds as a number only.** Enter **1.6**.

```quiz
type: radio
id: p3-source-check
content: |-
  **Question 2**

  A uniform rod of mass $m$ and length $L$ swings about a pivot at one end. Find its small-angle oscillation period for $L=0.92\ \mathrm{m}$ and $m=0.037\ \mathrm{kg}$.

  ![](<../Source/Images/uniform-rod-end-pivot.png>)

  Enter the period in seconds as a number only.
options:
- id: p3-source-check-a
  content: |-
    1.6
  correct: true
  feedback: |-
    A swinging rod is a physical pendulum, so its end-pivot inertia $I_p=\frac13mL^2$ and center-of-mass distance $\ell=L/2$ give $T=2\pi\sqrt{2L/(3g)}$. Substituting $L=0.92\ \mathrm{m}$ gives $1.5711\ldots\ \mathrm{s}$, which rounds to the number-only entry `1.6`.
- id: p3-source-check-b
  content: |-
    1.9
  feedback: |-
    This uses the simple-pendulum formula with a point bob at the rod's far end. Because the rod's mass is distributed, its end-pivot inertia must be included; $T=2\pi\sqrt{2L/(3g)}$ gives the entry `1.6`, not `1.9`.
- id: p3-source-check-c
  content: |-
    1.4
  feedback: |-
    This locates the center of mass correctly but concentrates the entire rod there as a point bob. The rod's distributed mass gives $I_p=\frac13mL^2$, so the physical-pendulum period rounds to `1.6` rather than `1.4`.
- id: p3-source-check-d
  content: |-
    0.79
  feedback: |-
    This uses the rod's center-axis inertia even though the actual pivot is at an end. The parallel-axis shift changes the axis from $I_{\mathrm{cm}}=\frac1{12}mL^2$ to $I_p=\frac13mL^2$; using the correct pivot axis gives `1.6`, not `0.79`.
```

---

## Summary

1. Recognize a rigid body swinging through a small angle as a physical pendulum.
2. Use quantities measured from the pivot: $I_p=\frac13mL^2$ and $\ell=L/2$ for a uniform rod pivoted at one end.
3. Substitute symbolically, expose the common factors, and simplify to $T=2\pi\sqrt{2L/(3g)}$.
4. Check that mass cancels and the remaining units reduce to seconds.
5. Evaluate the radicand, take the square root, multiply by $2\pi$, and round only the final answer.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../../M5/2026-08-03-Q-3/Study-Guide.md)
Next: [Finding the Period of a Rod–Disk Physical Pendulum](Problem-6.md)

Study guide index: 07/28

---
<!-- lesson-nav:end -->
