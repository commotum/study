# Comparing the Speeds of Rolling Objects

## Table of Contents

- [Introduction](#introduction)
- [Write All Kinetic Energy in Terms of Speed](#write-all-kinetic-energy-in-terms-of-speed)
- [Recognize When Radius Cancels](#recognize-when-radius-cancels)
- [Compare Different Shapes](#compare-different-shapes)
- [Separate Center-of-Mass Speed from Angular Speed](#separate-center-of-mass-speed-from-angular-speed)
- [Summary](#summary)

## Prerequisites

- Conservation of mechanical energy when dissipative losses are negligible
- Translational kinetic energy, $K_{\mathrm{trans}}=\tfrac12mv^2$
- Rotational kinetic energy, $K_{\mathrm{rot}}=\tfrac12I\omega^2$
- The rolling-without-slipping relation, $v=\omega R$
- The moment-of-inertia form $I=kmR^2$, where $k$ depends on how mass is distributed

---

<a id="introduction"></a>
## Introduction

When objects roll from rest down the same height, their lost gravitational potential energy becomes both translational and rotational kinetic energy. The cue is the phrase **roll without slipping**: it lets you replace $\omega$ with $v/R$ and express all final energy in terms of the center-of-mass speed $v$.

For any fixed shape whose moment of inertia can be written as $I=kmR^2$, this substitution makes the radius cancel. The resulting speed is

$$
v=\sqrt{\frac{2gh}{1+k}}.
$$

Thus, two objects descending through the same height have the same center-of-mass speed when they have the same shape factor $k$, even if their masses or radii differ. This conclusion requires pure rolling and negligible energy loss.

---

<a id="write-all-kinetic-energy-in-terms-of-speed"></a>
## Write All Kinetic Energy in Terms of Speed

**Example:** A rigid body starts from rest and rolls without slipping through a vertical drop $h$. Its moment of inertia is $I=kmR^2$. Find its center-of-mass speed at the bottom.

**Explanation**

With negligible energy loss, conservation of mechanical energy gives

$$
mgh=\frac12mv^2+\frac12I\omega^2.
$$

Use $I=kmR^2$ and the no-slip condition $\omega=v/R$ before simplifying:

$$
\begin{aligned}
mgh
&=\frac12mv^2+\frac12\left(kmR^2\right)\left(\frac{v}{R}\right)^2 \\
&=\frac12mv^2+\frac12kmv^2 \\
&=\frac12m(1+k)v^2.
\end{aligned}
$$

The factors of $R^2$ cancel in the rotational term, and the mass cancels from the whole equation. Solving for the nonnegative speed gives

$$
v=\sqrt{\frac{2gh}{1+k}}.
$$

```quiz
type: radio
id: p2-rolling-q1
content: |-
  A uniform solid cylinder starts from rest and rolls without slipping through a vertical drop $h$. For a solid cylinder, $I=\tfrac12mR^2$. Which expression gives its center-of-mass speed at the bottom?
options:
- id: ignore-rotation
  content: |-
    $v=\sqrt{2gh}$
  feedback: |-
    This treats all of $mgh$ as translational kinetic energy. A rolling cylinder also has rotational kinetic energy, so $mgh=\tfrac12m(1+\tfrac12)v^2$ and its speed is less than $\sqrt{2gh}$.
- id: correct-solid-cylinder
  content: |-
    $v=\sqrt{\dfrac{4gh}{3}}$
  correct: true
  feedback: |-
    Rolling without slipping changes the rotational term to $\tfrac12(\tfrac12mR^2)(v/R)^2=\tfrac14mv^2$. Therefore $mgh=\tfrac34mv^2$, so the center-of-mass speed is $v=\sqrt{4gh/3}$.
- id: radius-remains
  content: |-
    $v=R\sqrt{\dfrac{4gh}{3}}$
  feedback: |-
    The $R^2$ in $I=\tfrac12mR^2$ cancels the $1/R^2$ from $\omega^2=(v/R)^2$. Radius does not remain in the speed formula; this expression also has units of length squared per time rather than speed.
- id: omit-translational
  content: |-
    $v=2\sqrt{gh}$
  feedback: |-
    This effectively assigns the energy only to the cylinder's rotational term. Rolling motion has both $\tfrac12mv^2$ and $\tfrac12I\omega^2$, whose sum yields $v^2=4gh/3$, not $4gh$.
- id: lose-energy-factor
  content: |-
    $v=\sqrt{\dfrac{2gh}{3}}$
  feedback: |-
    The total kinetic energy is $\tfrac12m(1+k)v^2$, not $m(1+k)v^2$. With $k=1/2$, retaining the kinetic-energy factor of $1/2$ gives $v^2=4gh/3$.
```

---

<a id="recognize-when-radius-cancels"></a>
## Recognize When Radius Cancels

**Example:** Cylinder X has mass $m$ and radius $R$. Cylinder Y has mass $3m$ and radius $2R$. Both are uniform solid cylinders, start from rest at the same height, and roll without slipping to the bottom. Compare their center-of-mass speeds.

**Explanation**

Every uniform solid cylinder has the same shape factor:

$$
I=\frac12mR^2 \qquad\Longrightarrow\qquad k=\frac12.
$$

Both cylinders also descend through the same $h$. Substituting the shared values of $h$ and $k$ into

$$
v=\sqrt{\frac{2gh}{1+k}}
$$

gives $v_X=v_Y=\sqrt{4gh/3}$. Their different masses and radii do not matter because neither remains in the final speed formula.

```quiz
type: radio
id: p2-rolling-q2
shuffle: true
content: |-
  Two uniform solid cylinders have the same mass, but cylinder B has twice the radius of cylinder A. They start from rest at the same height on a ramp and roll to the bottom without slipping. Assume rolling friction is negligible and each cylinder has constant density. Which cylinder has the greater center-of-mass speed at the bottom?
options:
- id: cylinder-a-faster
  content: |-
    Cylinder A is moving faster.
  feedback: |-
    A smaller radius produces a larger angular speed for a given center-of-mass speed, but it does not produce a larger center-of-mass speed here. Both solid cylinders have $k=1/2$, and $R$ cancels after using $\omega=v/R$.
- id: cylinder-b-faster
  content: |-
    Cylinder B is moving faster.
  feedback: |-
    A larger radius makes $I=\tfrac12mR^2$ larger, but it simultaneously makes $\omega=v/R$ smaller for a given $v$. Those radius effects cancel in $I\omega^2$, so cylinder B gains no center-of-mass-speed advantage.
- id: same-speed
  content: |-
    They have the same speed.
  correct: true
  feedback: |-
    For each uniform solid cylinder, $k=1/2$, so energy conservation gives $v=\sqrt{2gh/(1+k)}=\sqrt{4gh/3}$. The cylinders share $h$ and $k$, while mass and radius cancel; therefore their center-of-mass speeds are equal.
```

The comparison would need to be reconsidered if the objects had different shapes, slipped, started with different speeds, descended through different heights, or lost different amounts of energy.

---

<a id="compare-different-shapes"></a>
## Compare Different Shapes

**Example:** A uniform solid sphere and a thin hoop start from rest at the same height and roll without slipping. Which reaches the bottom with the greater center-of-mass speed?

**Explanation**

Radius still cancels, but the shape factor does not. For a solid sphere, $k=2/5$; for a thin hoop, $k=1$. Therefore,

$$
v_{\mathrm{sphere}}=\sqrt{\frac{2gh}{1+2/5}}
=\sqrt{\frac{10gh}{7}},
$$

while

$$
v_{\mathrm{hoop}}=\sqrt{\frac{2gh}{1+1}}=\sqrt{gh}.
$$

The solid sphere is faster. A smaller $k$ means less of the available energy is tied up in rotation for a given center-of-mass speed.

```quiz
type: radio
id: p2-rolling-q3
content: |-
  A uniform solid cylinder and a thin hoop start from rest at the same height and roll without slipping. Their masses and radii are equal. Which object has the greater center-of-mass speed at the bottom?
options:
- id: solid-cylinder-faster
  content: |-
    The uniform solid cylinder is faster.
  correct: true
  feedback: |-
    Speed after the same drop is $v=\sqrt{2gh/(1+k)}$. The cylinder has $k=1/2$ while the hoop has $k=1$, so the cylinder has the smaller denominator and the greater center-of-mass speed.
- id: hoop-faster
  content: |-
    The thin hoop is faster.
  feedback: |-
    Equal mass and radius do not make the rotational energy shares equal. The hoop's mass lies farther from its axis, giving it the larger shape factor $k=1$; that larger rotational share leaves it with a smaller center-of-mass speed than the cylinder.
- id: different-shapes-same-speed
  content: |-
    They have the same speed.
  feedback: |-
    Radius and mass cancel, but the shape factor $k$ remains. Equal speeds follow only when the objects share the same $k$ and height; here $k_{\mathrm{cylinder}}=1/2$ and $k_{\mathrm{hoop}}=1$.
- id: cannot-determine
  content: |-
    It cannot be determined without numerical values for mass and radius.
  feedback: |-
    Numerical mass and radius values are unnecessary because both cancel from the rolling-energy equation. The supplied shape factors and common height determine the comparison, and the cylinder's smaller $k$ makes it faster.
```

---

<a id="separate-center-of-mass-speed-from-angular-speed"></a>
## Separate Center-of-Mass Speed from Angular Speed

**Example:** Two uniform solid cylinders have radii $R$ and $2R$. After rolling without slipping through the same height, they have the same center-of-mass speed $v$. Compare their angular speeds.

**Explanation**

Equal center-of-mass speeds do not imply equal angular speeds. The rolling constraint gives

$$
\omega=\frac{v}{R}.
$$

For the smaller cylinder,

$$
\omega_{\mathrm{small}}=\frac{v}{R},
$$

whereas for the larger cylinder,

$$
\omega_{\mathrm{large}}=\frac{v}{2R}=\frac12\omega_{\mathrm{small}}.
$$

The smaller cylinder turns twice as fast even though the centers of mass move equally fast.

```quiz
type: radio
id: p2-rolling-q4
content: |-
  Cylinders A and B are uniform solid cylinders that roll without slipping from rest through the same vertical drop. Cylinder B has three times the radius of cylinder A. Which statement is correct at the bottom?
options:
- id: equal-linear-equal-angular
  content: |-
    Their center-of-mass speeds and angular speeds are both equal.
  feedback: |-
    Sharing the same $h$ and $k$ makes the center-of-mass speeds equal, but angular speed also depends on radius through $\omega=v/R$. Since B has the larger radius, its angular speed is smaller.
- id: a-three-times-angular
  content: |-
    Their center-of-mass speeds are equal, and A's angular speed is three times B's.
  correct: true
  feedback: |-
    Equal shape factors and drops give $v_A=v_B$. Then $\omega=v/R$, and $R_B=3R_A$ implies $\omega_B=v/(3R_A)=\omega_A/3$, so A's angular speed is three times B's.
- id: b-three-times-angular
  content: |-
    Their center-of-mass speeds are equal, and B's angular speed is three times A's.
  feedback: |-
    For equal center-of-mass speed, angular speed varies inversely with radius, not directly with it. B's radius is three times larger, so B turns at one-third A's angular speed.
- id: a-faster-linear
  content: |-
    A has three times B's center-of-mass speed, and their angular speeds are equal.
  feedback: |-
    Radius cancels from the energy equation for two objects with the same shape factor, so A has no center-of-mass-speed advantage. Radius remains only in $\omega=v/R$, which makes their angular speeds unequal.
```

---

<a id="summary"></a>
## Summary

When an object **rolls without slipping**, use $\omega=v/R$ to write all kinetic energy in terms of $v$:

$$
mgh=\frac12mv^2+\frac12(kmR^2)\left(\frac{v}{R}\right)^2
=\frac12m(1+k)v^2.
$$

Therefore,

$$
v=\sqrt{\frac{2gh}{1+k}}.
$$

Use this checklist:

1. Confirm the objects start with the same energy conditions and roll without slipping with negligible loss.
2. Write each moment of inertia as $I=kmR^2$.
3. Substitute $\omega=v/R$ before simplifying.
4. Cancel $m$ and $R^2$; compare the remaining $h$ and $k$.
5. Do not confuse equal center-of-mass speed with equal angular speed: $\omega=v/R$ still depends on radius.

The main trap is comparing radii directly. Radius changes both $I$ and $\omega$ in opposite ways, so it cancels from the center-of-mass speed for geometrically similar rolling objects.
