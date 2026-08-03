# Speed of a Rolling Hollow Sphere From Energy

<!--
lesson-id: 212-M2-032
topic-code: MTH212.M2.32
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Ramp Distance to Vertical Drop](#convert-ramp-distance-to-vertical-drop)
- [Include Both Forms of Kinetic Energy](#include-both-forms-of-kinetic-energy)
- [Simplify Before Substituting Numbers](#simplify-before-substituting-numbers)
- [Apply the Method to the Hollow Sphere](#apply-the-method-to-the-hollow-sphere)
- [Summary](#summary)

## Prerequisites

- Conservation of mechanical energy
- Translational kinetic energy: $\frac12mv^2$
- Rotational kinetic energy: $\frac12I\omega^2$
- The no-slip condition: $\omega=v/r$
- The sine ratio in a right triangle

---

## Introduction

A rigid object rolling without slipping has both translational and rotational kinetic energy. Starting from rest and dropping through vertical height $h$, it obeys

$$
mgh=\frac12mv^2+\frac12I\omega^2.
$$

For motion a distance $d$ along a ramp inclined at angle $\theta$, the vertical drop is

$$
h=d\sin\theta.
$$

**Recognition cue:** When a rigid body starts from rest and rolls without slipping down a ramp, convert the ramp distance to vertical height, include both kinetic-energy terms, and use $\omega=v/r$ before solving for the center-of-mass speed.

---

## Convert Ramp Distance to Vertical Drop

**Example:** An object rolls $2.0\ \mathrm{m}$ down a ramp inclined at $30^\circ$. Find its vertical drop.

**Explanation**

The ramp distance is the hypotenuse of the right triangle, and the vertical drop is opposite the angle. Therefore,

$$
\sin\theta=\frac{h}{d},
$$

so

$$
h=d\sin\theta
=(2.0\ \mathrm{m})\sin30^\circ
=1.0\ \mathrm{m}.
$$

Use $d\sin\theta$, not $d\cos\theta$, because the desired side is opposite the ramp angle.

```quiz
type: radio
id: problem-2-height-q1
content: |-
  An object travels $4.0\ \mathrm{m}$ down a ramp inclined at $30^\circ$. What is its vertical drop?
options:
- id: a
  content: |-
    $2.0\ \mathrm{m}$
  correct: true
  feedback: |-
    $h=d\sin\theta=(4.0)\sin30^\circ=2.0\ \mathrm{m}$.
- id: b
  content: |-
    $3.5\ \mathrm{m}$
  feedback: |-
    This uses $d\cos\theta$, which gives the horizontal component rather than the vertical drop.
- id: c
  content: |-
    $4.0\ \mathrm{m}$
  feedback: |-
    The vertical drop equals the full ramp distance only for a vertical ramp.
- id: d
  content: |-
    $0.50\ \mathrm{m}$
  feedback: |-
    This gives $\sin30^\circ$ alone and omits the ramp distance.
- id: e
  content: |-
    $8.0\ \mathrm{m}$
  feedback: |-
    This divides by $\sin30^\circ$ instead of multiplying.
```

---

## Include Both Forms of Kinetic Energy

**Example:** Let a rolling object's moment of inertia be

$$
I=\beta mr^2.
$$

Rewrite its total kinetic energy using only $m$, $v$, and $\beta$.

**Explanation**

Begin with both contributions:

$$
K
=\frac12mv^2+\frac12I\omega^2.
$$

For rolling without slipping, $\omega=v/r$. Substitute both relations:

$$
\begin{aligned}
K
&=\frac12mv^2+\frac12(\beta mr^2)\left(\frac{v}{r}\right)^2\\
&=\frac12mv^2+\frac12\beta mv^2\\
&=\frac12(1+\beta)mv^2.
\end{aligned}
$$

An energy ledger makes the two contributions harder to mix up:

| Contribution | Before substitution | After $I=\beta mr^2$ and $\omega=v/r$ |
|---|---:|---:|
| Translation | $\frac12mv^2$ | $\frac12mv^2$ |
| Rotation | $\frac12I\omega^2$ | $\frac12\beta mv^2$ |

For a hollow sphere, $\beta=\frac23$, so

$$
\begin{aligned}
K
&=\left(\frac12+\frac12\cdot\frac23\right)mv^2\\
&=\left(\frac12+\frac13\right)mv^2\\
&=\left(\frac36+\frac26\right)mv^2\\
&=\frac56mv^2.
\end{aligned}
$$

The radius cancels because the same $r$ appears in the moment of inertia and the no-slip relation.

```quiz
type: radio
id: problem-2-kinetic-coefficient-q1
content: |-
  A rolling object has $I=\frac12mr^2$. What is its total kinetic energy in terms of its center-of-mass speed $v$?
options:
- id: a
  content: |-
    $K=\dfrac34mv^2$
  correct: true
  feedback: |-
    $K=\frac12(1+\frac12)mv^2=\frac34mv^2$.
- id: b
  content: |-
    $K=\dfrac12mv^2$
  feedback: |-
    This includes only translational kinetic energy.
- id: c
  content: |-
    $K=\dfrac14mv^2$
  feedback: |-
    This is only the rotational contribution.
- id: d
  content: |-
    $K=mv^2$
  feedback: |-
    The translational and rotational coefficients add to $\frac34$, not $1$.
- id: e
  content: |-
    $K=\dfrac32mv^2$
  feedback: |-
    This omits the overall factor $\frac12$ in both kinetic-energy terms.
```

---

## Simplify Before Substituting Numbers

**Example:** Derive the rolling speed for an object with $I=\beta mr^2$ after it travels distance $d$ down a ramp at angle $\theta$.

**Explanation**

Conservation of energy gives

$$
mgd\sin\theta
=\frac12(1+\beta)mv^2.
$$

Cancel the common mass and isolate $v^2$:

$$
v^2=\frac{2gd\sin\theta}{1+\beta}.
$$

Algebraically, taking square roots would produce two signs. The requested quantity is speed, a nonnegative magnitude, so keep the positive root:

$$
v=\sqrt{\frac{2gd\sin\theta}{1+\beta}}.
$$

For a hollow sphere, $\beta=\frac23$:

$$
v
=\sqrt{\frac{2gd\sin\theta}{1+\frac23}}
=\sqrt{\frac65gd\sin\theta}.
$$

This symbolic simplification makes two facts visible: the mass cancels for every value of $\beta$, and the radius cancels when the object rolls without slipping.

| Symbol | Why it disappears or remains |
|---|---|
| $m$ | Appears on both sides of the energy equation and cancels |
| $r$ | Cancels between $I=\beta mr^2$ and $\omega^2=v^2/r^2$ |
| $\beta$ | Remains because it measures how strongly rotation contributes |

```quiz
type: radio
id: problem-2-speed-formula-q1
content: |-
  A rolling hoop has $I=mr^2$, so $\beta=1$. Starting from rest, it rolls distance $d$ down a ramp at angle $\theta$. Which expression gives its speed?
options:
- id: a
  content: |-
    $v=\sqrt{gd\sin\theta}$
  correct: true
  feedback: |-
    Setting $\beta=1$ gives $v=\sqrt{2gd\sin\theta/(1+1)}=\sqrt{gd\sin\theta}$.
- id: b
  content: |-
    $v=\sqrt{2gd\sin\theta}$
  feedback: |-
    This is the sliding result and omits rotational kinetic energy.
- id: c
  content: |-
    $v=\sqrt{\dfrac12gd\sin\theta}$
  feedback: |-
    The factor $2$ in the numerator cancels $1+\beta=2$; it does not leave an extra factor $\frac12$.
- id: d
  content: |-
    $v=gd\sin\theta$
  feedback: |-
    This omits the square root and has units of speed squared.
- id: e
  content: |-
    $v=-\sqrt{gd\sin\theta}$
  feedback: |-
    Speed is the nonnegative magnitude, so use the positive square root.
```

---

## Apply the Method to the Hollow Sphere

**Example:** Evaluate the speed for the given hollow sphere.

**Explanation**

For a hollow sphere, $I=\frac23mr^2$. Use

$$
v=\sqrt{\frac65gd\sin\theta}.
$$

Substitute $g=9.81\ \mathrm{m/s^2}$, $d=0.86\ \mathrm{m}$, and $\theta=38^\circ$:

$$
\begin{aligned}
v
&=\sqrt{\frac65(9.81)(0.86)\sin38^\circ}\\
&=2.4966\ldots\ \mathrm{m/s}.
\end{aligned}
$$

To two significant figures, $v=2.5\ \mathrm{m/s}$. The supplied mass and radius are not needed because they cancel symbolically.

```quiz
type: radio
id: m2-5lec-q1
content: |-
  **Question 1**

  A hollow sphere of mass $m$ and radius $r$ starts from rest and rolls without slipping down a ramp inclined at angle $\theta$. How fast is its center of mass moving after traveling a distance $d$ along the ramp?

  Use $m=0.65\ \mathrm{kg}$, $r=0.28\ \mathrm{m}$, $\theta=38^\circ$, and $d=0.86\ \mathrm{m}$.

  ![](<../Source/Images/hollow-sphere-rolling-down-incline.png>)

  Enter the speed in meters per second as a number only:
options:
- id: a
  content: |-
    $2.5$
  correct: true
  feedback: |-
    For a hollow sphere, $I=\frac23mr^2$. Conservation of energy with $h=d\sin\theta$ and $\omega=v/r$ gives

    $$
    mgd\sin\theta
    =\frac12mv^2+\frac12\left(\frac23mr^2\right)\frac{v^2}{r^2}
    =\frac56mv^2.
    $$

    Therefore,

    $$
    v=\sqrt{\frac65gd\sin\theta}
    =2.503\ldots\ \mathrm{m/s}.
    $$

    The measured givens have two significant figures, so $v=2.5\ \mathrm{m/s}$. The mass and radius cancel.
- id: b
  content: |-
    $3.2$
  feedback: |-
    This uses only translational kinetic energy and omits the rotational term.
- id: c
  content: |-
    $2.8$
  feedback: |-
    This uses $d\cos\theta$ instead of the vertical drop $d\sin\theta$.
- id: d
  content: |-
    $1.8$
  feedback: |-
    This multiplies by the combined kinetic coefficient instead of solving the energy equation for $v^2$.
- id: e
  content: |-
    $6.2$
  feedback: |-
    This is approximately $v^2$; the final square root is still required.
```

---

## Summary

For a rolling object with $I=\beta mr^2$:

1. Convert ramp distance to vertical drop: $h=d\sin\theta$.
2. Write both kinetic terms:

   $$
   mgd\sin\theta=\frac12mv^2+\frac12I\omega^2.
   $$

3. Use $\omega=v/r$ and simplify before substituting numbers.
4. Solve for the nonnegative speed:

   $$
   \boxed{v=\sqrt{\frac{2gd\sin\theta}{1+\beta}}}.
   $$

For a hollow sphere, $\beta=\frac23$, so

$$
\boxed{v=\sqrt{\frac65gd\sin\theta}}.
$$

The main traps are using $d$ as the vertical drop, omitting rotational kinetic energy, or forgetting the final square root.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
