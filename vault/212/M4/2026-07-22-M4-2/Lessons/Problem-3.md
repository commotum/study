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
T=2\pi\sqrt{\frac{I}{mgd}}.
$$

Here $I$ must be the moment of inertia **about the pivot**, and $d$ is the distance from the pivot to the center of mass.

For a uniform rod of length $L$ pivoted at one end,

$$
I=\frac13mL^2
\qquad\text{and}\qquad
d=\frac L2.
$$

The pivot location matters. The value $I=\frac1{12}mL^2$ is the rod's moment of inertia about its center, not about an end.

**Example:** A uniform rod of length $L$ swings about a pivot at one end. Which pair belongs in the physical-pendulum formula?

**Explanation**

The rod's center of mass is halfway along the rod, while the relevant moment of inertia is measured about the end pivot.

```quiz
type: radio
id: p3-rod-quantities
content: |-
  For a uniform rod of length $L$ pivoted at one end, which values should be used in $T=2\pi\sqrt{I/(mgd)}$?
options:
- id: p3-rod-quantities-a
  content: |-
    $I=\frac13mL^2$ and $d=\frac L2$
  correct: true
  feedback: |-
    The center of mass is $L/2$ from the end, and the moment of inertia must be about that end: $I=\frac13mL^2$. The value $\frac1{12}mL^2$ belongs to an axis through the rod's center.
- id: p3-rod-quantities-b
  content: |-
    $I=\frac1{12}mL^2$ and $d=\frac L2$
- id: p3-rod-quantities-c
  content: |-
    $I=\frac13mL^2$ and $d=L$
- id: p3-rod-quantities-d
  content: |-
    $I=mL^2$ and $d=L$
```

---

<a id="substitute-and-cancel-symbolically"></a>
## Substitute and Cancel Symbolically

Insert the rod formulas before inserting numerical values:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{I}{mgd}}\\
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

Both $I$ and the gravitational torque scale with $m$, so their ratio does not depend on mass.

```quiz
type: radio
id: p3-mass-cancels
content: |-
  Two uniform rods have the same length and pivot at one end. Rod 2 has three times the mass of Rod 1. How do their small-angle periods compare?
options:
- id: p3-mass-cancels-a
  content: |-
    Rod 2 has three times the period.
- id: p3-mass-cancels-b
  content: |-
    Rod 2 has $\sqrt{3}$ times the period.
- id: p3-mass-cancels-c
  content: |-
    The rods have equal periods.
  correct: true
  feedback: |-
    In $I/(mgd)$, the factor $m$ in $I=\frac13mL^2$ cancels the factor $m$ in the denominator. Rods with the same $L$ and pivot geometry therefore have the same small-angle period regardless of mass.
- id: p3-mass-cancels-d
  content: |-
    Rod 2 has one-third the period.
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
\sqrt{\frac{\mathrm m}{\mathrm{m/s^2}}}
=\sqrt{\mathrm{s^2}}
=\mathrm s.
$$

Also, $T\propto\sqrt L$: a longer rod has a longer period, while changing only the mass does nothing.

**Example:** For $L=0.60\ \mathrm m$ and $g=9.81\ \mathrm{m/s^2}$,

$$
T=2\pi\sqrt{\frac{2(0.60)}{3(9.81)}}=1.27\ldots\ \mathrm s.
$$

**Explanation**

Keep extra calculator digits until the final rounding step.

```quiz
type: radio
id: p3-evaluate-period
content: |-
  A uniform rod of length $0.75\ \mathrm m$ pivots at one end. Using $g=9.81\ \mathrm{m/s^2}$, what is its small-angle period?
options:
- id: p3-evaluate-period-a
  content: |-
    $1.42\ \mathrm s$
  correct: true
  feedback: |-
    Substitute with parentheses: $T=2\pi\sqrt{2(0.75)/(3(9.81))}=1.418\ldots\ \mathrm s$. The value $1.74\ \mathrm s$ comes from using the simple-pendulum formula $2\pi\sqrt{L/g}$ instead of the rod formula.
- id: p3-evaluate-period-b
  content: |-
    $1.74\ \mathrm s$
- id: p3-evaluate-period-c
  content: |-
    $0.71\ \mathrm s$
- id: p3-evaluate-period-d
  content: |-
    $4.02\ \mathrm s$
```

---

<a id="apply-the-method-to-problem-3"></a>
## Apply the Method to Problem 3

**Example:** A uniform rod of mass $m$ and length $L$ swings about a pivot at one end. Find its small-angle oscillation period for $L=0.92\ \mathrm{m}$ and $m=0.037\ \mathrm{kg}$.

![](<../Source/Images/uniform-rod-end-pivot.png>)

**Explanation**

For a physical pendulum,

$$
T=2\pi\sqrt{\frac{I}{mgd}}.
$$

A uniform rod pivoted at one end has $I=\frac13mL^2$ and $d=L/2$, so

$$
T=2\pi\sqrt{\frac{2L}{3g}}
=2\pi\sqrt{\frac{2(0.92\ \mathrm{m})}{3(9.81\ \mathrm{m/s^2})}}
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
    For a physical pendulum,

    $$
    T=2\pi\sqrt{\frac{I}{mgd}}.
    $$

    A uniform rod pivoted at one end has $I=\frac13mL^2$ and $d=L/2$, so

    $$
    T=2\pi\sqrt{\frac{2L}{3g}}
    =2\pi\sqrt{\frac{2(0.92\ \mathrm{m})}{3(9.81\ \mathrm{m/s^2})}}
    =1.5711\ldots\ \mathrm{s}.
    $$

    The measured length has two significant figures, so $T=1.6\ \mathrm{s}$. The rod's mass cancels.

    The other values reflect nearby formula errors: `1.9` uses the point-mass simple-pendulum formula with length $L$; `1.4` treats the rod as a point mass at $L/2$; and `0.79` uses the rod's center-axis moment of inertia instead of its end-pivot moment of inertia.
- id: p3-source-check-b
  content: |-
    1.9
- id: p3-source-check-c
  content: |-
    1.4
- id: p3-source-check-d
  content: |-
    0.79
```

---

## Summary

1. Recognize a rigid body swinging through a small angle as a physical pendulum.
2. Use quantities measured from the pivot: $I=\frac13mL^2$ and $d=L/2$ for a uniform rod pivoted at one end.
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
