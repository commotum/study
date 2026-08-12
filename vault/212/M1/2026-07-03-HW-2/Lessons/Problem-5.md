# Deriving the Angle in a Conical Pendulum

<!--
lesson-id: 212-M1-028
topic-code: MTH212.M1.28
-->

## Table of Contents

- [Introduction](#introduction)
- [Use the Given Angle to Choose Components](#use-the-given-angle-to-choose-components)
- [Write the Radial and Vertical Force Equations](#write-the-radial-and-vertical-force-equations)
- [Replace the Circular Acceleration](#replace-the-circular-acceleration)
- [Solve for the Angle](#solve-for-the-angle)
- [Summary](#summary)

## Prerequisites

- Resolve a vector into horizontal and vertical components.
- Use $a_r=\dfrac{v^2}{r}=\dfrac{4\pi^2r}{T^2}$ for uniform circular motion with period $T$.
- Use inverse trig to solve equations such as $\sin\theta=k$.

---

<a id="introduction"></a>
## Introduction

A bob of mass $m$ is attached to a light string of length $L$ and travels in a horizontal circle with period $T$. The string remains at angle $\theta$ above the horizontal. What is $\theta$ in terms of $L$, $T$, and $g$?

![](<../Source/Images/conical-pendulum-diagram.png>)

The tilted string does two jobs at once. Its upward tension component supports the bob against gravity, while its horizontal component pulls the bob toward the center of the circle. The same angle also determines the circle's radius: the horizontal projection of the string is $L\cos\theta$.

Because $\theta$ is measured from the horizontal, the vertical tension component is $T_{\text{tens}}\sin\theta$, not $T_{\text{tens}}\cos\theta$. Keeping that reference line fixed connects the force diagram to the string geometry.

The cheat sheet's conical-pendulum pair $T\cos\phi=mg$ and $T\sin\phi=mv^2/r$ uses an angle $\phi$ measured from the vertical. Here $\phi=90^\circ-\theta$, so the equations are equivalent by the complementary-angle identities. Because $T$ already denotes the period in this lesson, the tension magnitude is written $T_{\text{tens}}$.

A frictionless banked curve gives a useful structural check: one angled real force does two jobs. Its vertical component balances $mg$, and its horizontal component supplies $ma_r$. Dividing or substituting between those component equations eliminates the unknown angled-force magnitude.

---

<a id="use-the-given-angle-to-choose-components"></a>
## Use the Given Angle to Choose Components

**Example:** A bob is attached to a string of length $L$. The string makes an angle $\theta$ with the horizontal while the bob moves in a horizontal circle. Write the radial component of the tension $T_{\text{tens}}$, the vertical component of the tension, and the circle radius $r$.

**Explanation**

Because the string angle is measured from the horizontal, the component next to the angle is horizontal:

$$
T_{\text{tens},r}=T_{\text{tens}}\cos\theta
$$

The component opposite the angle is vertical:

$$
T_{\text{tens},y}=T_{\text{tens}}\sin\theta
$$

The circle radius is the horizontal part of the string length:

$$
r=L\cos\theta
$$

So the useful geometry is

$$
T_{\text{tens},r}=T_{\text{tens}}\cos\theta,\qquad T_{\text{tens},y}=T_{\text{tens}}\sin\theta,\qquad r=L\cos\theta
$$

```quiz
type: radio
id: p5-q1-components
shuffle: true
content: |-
  A string of length $L$ makes an angle $\theta$ with the horizontal. Which pair correctly gives the vertical tension component and the circle radius?
options:
- id: a
  content: |-
    $T_{\text{tens}}\cos\theta$ and $L\sin\theta$
- id: b
  content: |-
    $T_{\text{tens}}\sin\theta$ and $L\cos\theta$
  correct: true
- id: c
  content: |-
    $T_{\text{tens}}\cos\theta$ and $L\cos\theta$
- id: d
  content: |-
    $T_{\text{tens}}\sin\theta$ and $L\sin\theta$
- id: e
  content: |-
    $T_{\text{tens}}$ and $L$
```

---

<a id="write-the-radial-and-vertical-force-equations"></a>
## Write the Radial and Vertical Force Equations

**Example:** For the same bob, write the force equations in the radial and vertical directions before substituting for $a_r$.

**Explanation**

The radial direction points horizontally toward the center of the circular path. The only radial force component is the horizontal component of tension, so

$$
\sum F_r=ma_r
$$

becomes

$$
T_{\text{tens}}\cos\theta=ma_r
$$

The bob has no vertical acceleration, so the vertical forces balance. The upward component of tension balances weight:

$$
\sum F_y=0
$$

$$
T_{\text{tens}}\sin\theta-mg=0
$$

or

$$
T_{\text{tens}}\sin\theta=mg
$$

Label these two equations so the later substitution is easier to see:

$$
T_{\text{tens}}\cos\theta=ma_r \tag{1}
$$

$$
T_{\text{tens}}\sin\theta=mg \tag{2}
$$

```quiz
type: radio
id: p5-q2-force-equations
shuffle: true
content: |-
  A conical pendulum has angle $\theta$ measured from the horizontal. Which force equations match the radial and vertical directions?
options:
- id: a
  content: |-
    $T_{\text{tens}}\sin\theta=ma_r$ and $T_{\text{tens}}\cos\theta=mg$
- id: b
  content: |-
    $T_{\text{tens}}\cos\theta=ma_r$ and $T_{\text{tens}}\sin\theta=mg$
  correct: true
- id: c
  content: |-
    $T_{\text{tens}}=ma_r$ and $mg=0$
- id: d
  content: |-
    $T_{\text{tens}}\cos\theta=mg$ and $T_{\text{tens}}\sin\theta=ma_r$
- id: e
  content: |-
    $mg=ma_r$ and $T_{\text{tens}}\sin\theta=0$
```

---

<a id="replace-the-circular-acceleration"></a>
## Replace the Circular Acceleration

**Example:** Substitute the period form of centripetal acceleration into the radial equation for a bob whose circular radius is $r=L\cos\theta$.

**Explanation**

For uniform circular motion with period $T$,

$$
a_r=\dfrac{4\pi^2r}{T^2}
$$

The radius is

$$
r=L\cos\theta
$$

so

$$
a_r=\dfrac{4\pi^2L\cos\theta}{T^2}
$$

Substitute this into the radial force equation:

$$
T_{\text{tens}}\cos\theta=m\left(\dfrac{4\pi^2L\cos\theta}{T^2}\right)
$$

For a nonzero circular radius, $\cos\theta\neq 0$, so this simplifies to

$$
T_{\text{tens}}=\dfrac{4\pi^2mL}{T^2}
$$

This removes both $a_r$ and $r$ from equation $(1)$, leaving tension in terms of the given quantities.

```quiz
type: radio
id: p5-q3-acceleration
shuffle: true
content: |-
  If a conical pendulum has period $T$ and radius $r=L\cos\theta$, what does $a_r$ equal?
options:
- id: a
  content: |-
    $\dfrac{4\pi^2L\cos\theta}{T^2}$
  correct: true
- id: b
  content: |-
    $\dfrac{2\pi L\cos\theta}{T}$
- id: c
  content: |-
    $\dfrac{4\pi^2L\sin\theta}{T^2}$
- id: d
  content: |-
    $\dfrac{gT^2}{4\pi^2L}$
- id: e
  content: |-
    $\dfrac{4\pi^2L}{T^2\cos\theta}$
```

---

<a id="solve-for-the-angle"></a>
## Solve for the Angle

**Example:** A bob of mass $m$ is attached to a light string of length $L$ and moves in a horizontal circle with period $T$. The string makes an angle $\theta$ with the horizontal. Find $\theta$ in terms of $g$, $T$, and $L$.

**Explanation**

From the radial equation after substituting the period acceleration,

$$
T_{\text{tens}}=\dfrac{4\pi^2mL}{T^2}
$$

From vertical force balance,

$$
T_{\text{tens}}\sin\theta=mg
$$

Substitute the expression for $T_{\text{tens}}$ into equation $(2)$:

$$
\left(\dfrac{4\pi^2mL}{T^2}\right)\sin\theta=mg
$$

Cancel $m$:

$$
\dfrac{4\pi^2L}{T^2}\sin\theta=g
$$

Solve for $\sin\theta$:

$$
\sin\theta=\dfrac{gT^2}{4\pi^2L}
$$

Now the trig function is isolated, so apply inverse sine:

$$
\theta=\arcsin\left(\dfrac{gT^2}{4\pi^2L}\right)
$$

```quiz
type: radio
id: p5-q4-final-angle
shuffle: true
content: |-
  A bob of mass $m$ is attached to a light string of length $L$ and undergoes uniform circular motion with period $T$. The string makes an angle $\theta$ with the horizontal. What is $\theta$?
options:
- id: a
  content: |-
    $\arccos\left(\dfrac{gT^2}{2\pi L}\right)$
- id: b
  content: |-
    $\arcsin\left(\dfrac{gT^2}{2\pi L}\right)$
- id: c
  content: |-
    $\arctan\left(\dfrac{gT^2}{2\pi L}\right)$
- id: d
  content: |-
    $\arccos\left(\dfrac{gT^2}{4\pi^2L}\right)$
- id: e
  content: |-
    $\arcsin\left(\dfrac{gT^2}{4\pi^2L}\right)$
  correct: true
- id: f
  content: |-
    $\arctan\left(\dfrac{gT^2}{4\pi^2L}\right)$
```

---

<a id="summary"></a>
## Summary

When a conical pendulum angle is measured from the horizontal, use

$$
T_{\text{tens},r}=T_{\text{tens}}\cos\theta,\qquad T_{\text{tens},y}=T_{\text{tens}}\sin\theta,\qquad r=L\cos\theta
$$

Then write

$$
T_{\text{tens}}\cos\theta=ma_r,\qquad T_{\text{tens}}\sin\theta=mg,\qquad a_r=\dfrac{4\pi^2r}{T^2}
$$

Substituting $r=L\cos\theta$ lets the $\cos\theta$ factors cancel from the radial equation, giving

$$
T_{\text{tens}}=\dfrac{4\pi^2mL}{T^2}
$$

Use the vertical equation to get

$$
\sin\theta=\dfrac{gT^2}{4\pi^2L}
$$

so

$$
\theta=\arcsin\left(\dfrac{gT^2}{4\pi^2L}\right)
$$

The disappearance of $m$ is physically meaningful. A heavier bob needs proportionally more tension both to support its weight and to produce its inward acceleration, so the angle for fixed $L$ and period $T$ does not depend on mass.

The angle here is measured from the horizontal. Using the component formulas for an angle measured from the vertical would incorrectly replace the final inverse sine with inverse cosine.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Finding Radial Acceleration From Inward Forces](../../2026-07-02-M1-5/Lessons/Problem-3.md)

Study guide index: 31/35

---
<!-- lesson-nav:end -->
