# Finding Radial Acceleration From Inward Forces

<!--
lesson-id: 212-M1-055
topic-code: MTH212.M1.55
-->

## Table of Contents

- [Introduction](#introduction)
- [Set the Inward Radial Equation](#set-the-inward-radial-equation)
- [Resolve Weight Onto the Radial Axis](#resolve-weight-onto-the-radial-axis)
- [Solve for the Radial Acceleration](#solve-for-the-radial-acceleration)
- [Evaluate the Ball's Radial Acceleration](#evaluate-the-balls-radial-acceleration)
- [Summary](#summary)

## Prerequisites

- Use Newton's second law along one chosen axis: $\sum F = ma$.
- Know that weight has magnitude $mg$ and points downward.
- Use cosine for the component of a vector adjacent to the marked angle.
- Keep acceleration units in $\mathrm{m}/\mathrm{s}^2$.

---

<a id="introduction"></a>
## Introduction

A $0.56\ \mathrm{kg}$ ball is tied to a $0.88\ \mathrm{m}$ string and swung clockwise in a vertical circle. At the position shown, the string tension is $1.2\ \mathrm{N}$ and the marked angle is $14^\circ$. What is the magnitude of the ball's radial acceleration at that instant?

![](../Source/Images/vertical-circle-ball-string-diagram.png)

The inward $r$-axis lies along the string toward the center. Tension points entirely along that axis, and gravity has a component along it as well. Both contributions point inward at the shown position, so Newton's second law in the radial direction is

$$
T_{\mathrm{tens}}+mg\cos\theta=m a_r.
$$

The string length sets the path radius, $r=L$, and would connect $a_r$ to the ball's speed through $a_r=v^2/r=v^2/L$, but no speed is given. The two force components already determine the acceleration directly.

---

<a id="set-the-inward-radial-equation"></a>
## Set the Inward Radial Equation

**Example:** A ball is at the upper-left part of a vertical circle. The $r$-axis points inward along the string, and the string tension is $T_{\mathrm{tens}}$. Write the radial force equation before substituting numbers.

**Explanation**

Tension points along the string toward the center, so $T_{\mathrm{tens}}$ is positive in the inward radial direction. Gravity points downward, and at this position part of gravity also points inward.

The force directions must be correct, but the relative arrow lengths do not need to be guessed before solving. The force equations determine the needed magnitudes.

Call the inward component of gravity $F_{g,r}$. Then

$$
T_{\mathrm{tens}} + F_{g,r} = m a_r.
$$

The equation should include only radial components. Tangential components do not determine $a_r$, and the full weight $mg$ should not be placed into the radial equation unless the entire weight points along the radial axis.

```quiz
type: radio
id: p3-q1-radial-equation
shuffle: true
content: |-
  A ball is in a vertical circle, the $r$-axis points inward along the string, and the tension is $T_{\mathrm{tens}}$. If the inward component of gravity is $F_{g,r}$, which equation correctly sets up the radial direction?
options:
- id: a
  content: |-
    $T_{\mathrm{tens}} + F_{g,r} = m a_r$
  correct: true
- id: b
  content: |-
    $T_{\mathrm{tens}} - F_{g,r} = m a_r$
- id: c
  content: |-
    $mg = m a_r$
- id: d
  content: |-
    $T_{\mathrm{tens}} = m a_t$
- id: e
  content: |-
    $T_{\mathrm{tens}} + mg = m a_r$
```

---

<a id="resolve-weight-onto-the-radial-axis"></a>
## Resolve Weight Onto the Radial Axis

**Example:** The angle $\theta$ is measured between the string direction and the vertical radius in the diagram. Find the inward radial component of the ball's weight.

**Explanation**

Draw the component triangle only after the $r$- and $t$-axes are fixed, and make its sides parallel to those axes. Use the angle between $mg$ and the radial axis, not merely whichever angle happens to be labeled in the original picture.

At the shown position, the inward direction from the ball to the center is tilted by angle $\theta$ from the downward direction of $mg$. The radial side of the component triangle is adjacent to $\theta$, so

$$
F_{g,r} = mg\cos\theta.
$$

This component is positive because it points partly inward. The common check is: adjacent to the angle between the force and the chosen axis gives cosine; opposite gives sine.

```quiz
type: radio
id: p3-q2-weight-component
shuffle: true
content: |-
  A ball is in the same upper-left position, and the inward radial axis makes angle $\theta$ with the downward direction of gravity. What is the inward radial component of the ball's weight?
options:
- id: a
  content: |-
    $mg\cos\theta$
  correct: true
- id: b
  content: |-
    $mg\sin\theta$
- id: c
  content: |-
    $-mg\cos\theta$
- id: d
  content: |-
    $\dfrac{mg}{\cos\theta}$
- id: e
  content: |-
    $mg$
```

---

<a id="solve-for-the-radial-acceleration"></a>
## Solve for the Radial Acceleration

**Example:** A ball has $T_{\mathrm{tens}}=2.4\ \mathrm{N}$, $m=0.60\ \mathrm{kg}$, and $\theta=60^\circ$. Find $a_r$.

**Explanation**

Start with the inward radial equation:

$$
T_{\mathrm{tens}} + mg\cos\theta = m a_r.
$$

Divide every force term by $m$ to isolate the radial acceleration:

$$
a_r = \frac{T_{\mathrm{tens}}}{m} + g\cos\theta.
$$

Now substitute. Since the angle is given in degrees, evaluate the cosine in degree mode:

$$
a_r = \frac{2.4}{0.60} + 9.8\cos(60^\circ)
= 4.0 + 4.9
= 8.9\ \mathrm{m}/\mathrm{s}^2.
$$

```quiz
type: radio
id: p3-q3-solve-acceleration
shuffle: true
content: |-
  A ball in the same setup has $T_{\mathrm{tens}}=3.0\ \mathrm{N}$, $m=0.50\ \mathrm{kg}$, and $\theta=60^\circ$. Using $a_r=\frac{T_{\mathrm{tens}}}{m}+g\cos\theta$, what is $a_r$?
options:
- id: a
  content: |-
    $6.0\ \mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $10.9\ \mathrm{m}/\mathrm{s}^2$
  correct: true
- id: c
  content: |-
    $15.8\ \mathrm{m}/\mathrm{s}^2$
- id: d
  content: |-
    $1.1\ \mathrm{m}/\mathrm{s}^2$
- id: e
  content: |-
    $14.5\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="evaluate-the-balls-radial-acceleration"></a>
## Evaluate the Ball's Radial Acceleration

**Example:** For the ball shown at the start, $L=0.88\ \mathrm{m}$, $T_{\mathrm{tens}}=1.2\ \mathrm{N}$, $m=0.56\ \mathrm{kg}$, and $\theta=14^\circ$. Find the magnitude of the radial acceleration.

**Explanation**

The length $L$ is given, but it is not needed for this force-balance version because the speed is not given. The radial force equation already determines $a_r$:

$$
a_r = \frac{T_{\mathrm{tens}}}{m} + g\cos\theta.
$$

Substitute the values:

$$
a_r = \frac{1.2}{0.56} + 9.8\cos(14^\circ)
= 2.14 + 9.51
= 11.65\ \mathrm{m}/\mathrm{s}^2.
$$

To two significant figures, the magnitude is

$$
a_r = 12\ \mathrm{m}/\mathrm{s}^2.
$$

```quiz
type: radio
id: p3-q4-original-style
shuffle: true
content: |-
  A ball is in the same vertical-circle position with $L=1.1\ \mathrm{m}$, $T_{\mathrm{tens}}=1.8\ \mathrm{N}$, $m=0.45\ \mathrm{kg}$, and $\theta=20^\circ$. What is the radial acceleration magnitude to two significant figures?
options:
- id: a
  content: |-
    $4.0\ \mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $9.2\ \mathrm{m}/\mathrm{s}^2$
- id: c
  content: |-
    $13\ \mathrm{m}/\mathrm{s}^2$
  correct: true
- id: d
  content: |-
    $7.4\ \mathrm{m}/\mathrm{s}^2$
- id: e
  content: |-
    $5.2\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="summary"></a>
## Summary

When the $r$-axis points inward along the string, write Newton's second law in the inward radial direction:

$$
T_{\mathrm{tens}} + mg\cos\theta = m a_r.
$$

Then solve:

$$
a_r = \frac{T_{\mathrm{tens}}}{m} + g\cos\theta.
$$

The length $L$ is unnecessary when the inward forces are already known. The full weight also does not belong in the radial equation: in this diagram, the inward part of weight is the adjacent component $mg\cos\theta$. For numerical work, use degree mode when $\theta$ is given in degrees.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Testing Loop-the-Loop Statements](../../2026-07-03-HW-2/Lessons/Problem-10.md)

Study guide index: 32/35

---
<!-- lesson-nav:end -->
