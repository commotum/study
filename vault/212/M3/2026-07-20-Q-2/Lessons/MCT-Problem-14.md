# Calculate Rotational Kinetic Energy from the Correct Inertia

<!--
lesson-id: 212-M3-050
topic-code: MTH212.M3.50
-->

## Table of Contents

- [Introduction](#introduction)
- [Match the Shape and Rotation Axis](#match-shape-and-axis)
- [Why the Whole-Body Formula Uses Inertia](#why-the-formula-uses-inertia)
- [Source-Video Worked Problem: Spinning Solid Disk](#source-video-solid-disk)
- [Changing the Axis Changes the Energy](#changing-the-axis)
- [Square the Geometry and the Angular Speed](#square-geometry-and-angular-speed)
- [Convert Tangential Speed to Angular Speed](#convert-tangential-speed)
- [Summary](#summary)

## Prerequisites

- Evaluate numerical expressions with squares before multiplying.
- Distinguish radius from diameter.
- Use $v_t=\omega r$ for a point on a rotating rigid body.
- Recognize radians per second as the standard unit for angular speed.
- Read a standard moment-of-inertia table by both shape and axis.

---

<a id="introduction"></a>
## Introduction

For a rigid body spinning about a fixed axis,

$$
K_{\mathrm{rot}}=\frac12I\omega^2.
$$

The main choice is not the energy formula; it is the moment of inertia $I$. The same object can have different moments of inertia about different axes.

Use one sequence:

1. Name the rotating shape and the exact axis.
2. Select the matching moment-of-inertia formula.
3. Convert a diameter to radius or a tangential speed to angular speed if needed.
4. Calculate $I$, keeping the squared dimension.
5. Substitute $I$ and $\omega$ into $K_{\mathrm{rot}}=\frac12I\omega^2$.
6. Check that the result is positive and has joule units.

This lesson treats fixed-axis rotational kinetic energy only. It does not add translational energy or use an energy-conservation equation.

---

<a id="match-shape-and-axis"></a>
## Match the Shape and Rotation Axis

The M2-2 lecture notes organize standard inertias by shape and axis. For this calculation, a compact lookup is enough:

| Rigid body | Rotation axis | Moment of inertia |
|---|---|---|
| Point mass | Axis a perpendicular distance $r$ from the mass | $I=mr^2$ |
| Thin hoop | Symmetry axis through center | $I=MR^2$ |
| Uniform solid disk or cylinder | Symmetry axis through center | $I=\frac12MR^2$ |
| Uniform thin rod | Perpendicular axis through center | $I=\frac1{12}ML^2$ |
| Uniform thin rod | Perpendicular axis through one end | $I=\frac13ML^2$ |

The axis is part of every lookup. A solid disk about its central symmetry axis does not use the hoop formula, even though both objects have the same outer radius.

Write the axis beside the selected formula before substituting. If the problem supplies diameter $D$, first use $R=D/2$ and then square $R$; substituting $D^2$ would make a disk inertia four times too large.

```quiz
type: radio
id: mct-p14-inertia-lookup
shuffle: true
content: |-
  A uniform solid disk of mass $M$ and radius $R$ spins about its central symmetry axis. Which moment of inertia belongs in $K_{\mathrm{rot}}=\frac12I\omega^2$?
options:
- id: mct-p14-inertia-lookup-a
  content: |-
    $I=\frac12MR^2$
  correct: true
  feedback: |-
    A uniform solid disk about its central symmetry axis has $I=\frac12MR^2$. This formula already accounts for mass spread across radii from $0$ to $R$.
- id: mct-p14-inertia-lookup-b
  content: |-
    $I=MR^2$
  feedback: |-
    This is the central-axis formula for a thin hoop, whose mass is concentrated at radius $R$. A solid disk has mass inside the rim and uses $I=\frac12MR^2$.
- id: mct-p14-inertia-lookup-c
  content: |-
    $I=\frac1{12}ML^2$
  feedback: |-
    This formula belongs to a thin rod rotating about a perpendicular axis through its center. The object here is a disk, so both the shape and dimension are mismatched.
- id: mct-p14-inertia-lookup-d
  content: |-
    $I=\frac25MR^2$
  feedback: |-
    This coefficient belongs to a uniform solid sphere about a diameter. A flat solid disk about its symmetry axis uses the coefficient $1/2$.
- id: mct-p14-inertia-lookup-e
  content: |-
    $I=\frac12MR$
  feedback: |-
    Moment of inertia must contain a squared distance and have units $\mathrm{kg\,m^2}$. A single power of $R$ gives the wrong units as well as the wrong disk formula.
```

---

<a id="why-the-formula-uses-inertia"></a>
## Why the Whole-Body Formula Uses Inertia

The translation-to-rotation analogy is

| Translation | Fixed-axis rotation |
|---|---|
| $K_{\mathrm{trans}}=\frac12Mv^2$ | $K_{\mathrm{rot}}=\frac12I\omega^2$ |
| mass $M$ | moment of inertia $I$ |
| linear speed $v$ | angular speed $\omega$ |

For a collection of small masses in one rigid body, each piece has the same angular speed $\omega$ but a different tangential speed:

$$
v_i=\omega r_{\perp,i}.
$$

Add the kinetic energy of all pieces:

$$
\begin{aligned}
K_{\mathrm{rot}}
&=\sum_i\frac12m_iv_i^2,\\
&=\sum_i\frac12m_i(\omega r_{\perp,i})^2,\\
&=\frac12\left(\sum_i m_i r_{\perp,i}^2\right)\omega^2.
\end{aligned}
$$

Define

$$
I=\sum_i m_i r_{\perp,i}^2,
$$

or, for a continuous body,

$$
I=\int r_\perp^2\,dm.
$$

Then

$$
K_{\mathrm{rot}}=\frac12I\omega^2.
$$

**Source correction.** The source video motivates the formula by replacing $v$ with $\omega r$ in one term $\frac12mv^2$ and then associating $mr^2$ with inertia. The equality $I=mr^2$ is exact for one point mass at radius $r$. An extended disk contains mass at many radii, so its distribution must first be summed or integrated. The standard result $I=\frac12MR^2$ is that completed distribution calculation.

---

<a id="source-video-solid-disk"></a>
## Source-Video Worked Problem: Spinning Solid Disk

The source segment `REIP2mf6sIQ` at 0:01-3:16 gives a uniform solid disk with

$$
M=5\,\mathrm{kg},
\qquad
R=1.3\,\mathrm m,
\qquad
\omega=15\,\mathrm{rad/s}.
$$

The disk rotates about its central symmetry axis, so

$$
I=\frac12MR^2.
$$

Square the radius before multiplying:

$$
\begin{aligned}
I
&=\frac12(5)(1.3)^2,\\
&=\frac12(5)(1.69),\\
&=\boxed{4.225\,\mathrm{kg\,m^2}}.
\end{aligned}
$$

Now square the angular speed:

$$
\begin{aligned}
K_{\mathrm{rot}}
&=\frac12I\omega^2,\\
&=\frac12(4.225)(15)^2,\\
&=\frac12(4.225)(225),\\
&=475.3125\,\mathrm J,\\
&\approx\boxed{475.3\,\mathrm J}.
\end{aligned}
$$

The source briefly reports $I$ as $4.22\,\mathrm{kg\,m^2}$ and later uses $4.225\,\mathrm{kg\,m^2}$. Keeping $4.225$ as a guard-digit value produces the stated $475.3\,\mathrm J$ result.

As a calculation check, evaluate the two powers on their own lines: $(1.3)^2=1.69$ and $(15)^2=225$. This keeps either missing square from being hidden inside one calculator entry.

```quiz
type: radio
id: mct-p14-disk-mirror
shuffle: true
content: |-
  A uniform solid disk has $M=8.0\,\mathrm{kg}$, $R=0.50\,\mathrm m$, and $\omega=12\,\mathrm{rad/s}$ about its central symmetry axis. What is its rotational kinetic energy?
options:
- id: mct-p14-disk-mirror-a
  content: |-
    $72\,\mathrm J$
  correct: true
  feedback: |-
    The disk inertia is $I=\frac12(8.0)(0.50)^2=1.00\,\mathrm{kg\,m^2}$. Then $K=\frac12(1.00)(12)^2=72\,\mathrm J$.
- id: mct-p14-disk-mirror-b
  content: |-
    $144\,\mathrm J$
  feedback: |-
    This retains only one of the two factors of $1/2$. A solid disk contributes $1/2$ in $I=\frac12MR^2$, and the energy formula contributes another in $K=\frac12I\omega^2$.
- id: mct-p14-disk-mirror-c
  content: |-
    $288\,\mathrm J$
  feedback: |-
    This omits both factors of $1/2$ and evaluates $MR^2\omega^2$. The correct combined disk expression is $K=\frac14MR^2\omega^2$.
- id: mct-p14-disk-mirror-d
  content: |-
    $6\,\mathrm J$
  feedback: |-
    This uses $\omega$ rather than $\omega^2$ in the energy formula. Since $(12)^2=144$, the angular-speed factor is not $12$.
- id: mct-p14-disk-mirror-e
  content: |-
    $1.00\,\mathrm{kg\,m^2}$
  feedback: |-
    This is the disk's moment of inertia, not its energy. Insert that inertia into $K=\frac12I\omega^2$ to obtain joules.
```

---

<a id="changing-the-axis"></a>
## Changing the Axis Changes the Energy

For the same uniform rod,

$$
I_{\mathrm{center}}=\frac1{12}ML^2,
\qquad
I_{\mathrm{end}}=\frac13ML^2=4I_{\mathrm{center}}.
$$

At the same angular speed, the end-axis rotational kinetic energy is also four times the center-axis energy:

$$
K_{\mathrm{end}}
=\frac12I_{\mathrm{end}}\omega^2
=4K_{\mathrm{center}}.
$$

The energy formula did not change. The shape-and-axis lookup changed $I$.

```quiz
type: radio
id: mct-p14-rod-axis
shuffle: true
content: |-
  A uniform thin rod has $M=2.4\,\mathrm{kg}$ and $L=1.5\,\mathrm m$. It spins at $6.0\,\mathrm{rad/s}$ about a perpendicular axis through one end. What is its rotational kinetic energy?
options:
- id: mct-p14-rod-axis-a
  content: |-
    $32.4\,\mathrm J$
  correct: true
  feedback: |-
    For an end axis, $I=\frac13ML^2=\frac13(2.4)(1.5)^2=1.80\,\mathrm{kg\,m^2}$. Thus $K=\frac12(1.80)(6.0)^2=32.4\,\mathrm J$.
- id: mct-p14-rod-axis-b
  content: |-
    $8.10\,\mathrm J$
  feedback: |-
    This uses the center-axis formula $I=\frac1{12}ML^2$. The stated axis passes through an end, whose inertia and energy are four times larger.
- id: mct-p14-rod-axis-c
  content: |-
    $64.8\,\mathrm J$
  feedback: |-
    This uses the correct end-axis inertia but omits the factor $1/2$ in $K=\frac12I\omega^2$.
- id: mct-p14-rod-axis-d
  content: |-
    $5.40\,\mathrm J$
  feedback: |-
    This inserts $\omega=6.0$ without squaring it. Rotational kinetic energy depends on $\omega^2=36$, not on $\omega$ alone.
- id: mct-p14-rod-axis-e
  content: |-
    $1.80\,\mathrm{kg\,m^2}$
  feedback: |-
    This is the end-axis moment of inertia. The requested energy follows only after multiplying by $\frac12\omega^2$.
```

---

<a id="square-geometry-and-angular-speed"></a>
## Square the Geometry and the Angular Speed

For a solid disk about its symmetry axis,

$$
K_{\mathrm{rot}}
=\frac12\left(\frac12MR^2\right)\omega^2
=\frac14MR^2\omega^2.
$$

Two separate squares appear:

- $R^2$ comes from how mass is distributed about the axis.
- $\omega^2$ comes from kinetic energy's dependence on speed squared.

If $R$ doubles while $M$ and $\omega$ stay fixed, $K_{\mathrm{rot}}$ becomes four times larger. If $\omega$ triples while $I$ stays fixed, $K_{\mathrm{rot}}$ becomes nine times larger.

The unit check follows the same exponents. Radians are dimensionless, so

$$
\begin{aligned}
[K_{\mathrm{rot}}]
&=[I][\omega]^2,\\
&=(\mathrm{kg\,m^2})(\mathrm{s^{-1}})^2,\\
&=\mathrm{kg\,m^2/s^2},\\
&=\mathrm J.
\end{aligned}
$$

```quiz
type: radio
id: mct-p14-omega-scaling
shuffle: true
content: |-
  A rigid body keeps the same rotation axis and moment of inertia. Its angular speed increases from $5\,\mathrm{rad/s}$ to $15\,\mathrm{rad/s}$. By what factor does its rotational kinetic energy change?
options:
- id: mct-p14-omega-scaling-a
  content: |-
    It increases by a factor of $9$.
  correct: true
  feedback: |-
    The angular speed triples, and $K_{\mathrm{rot}}\propto\omega^2$ for fixed $I$. Therefore the energy factor is $3^2=9$.
- id: mct-p14-omega-scaling-b
  content: |-
    It increases by a factor of $3$.
  feedback: |-
    This treats rotational kinetic energy as linear in angular speed. The energy formula contains $\omega^2$, so tripling $\omega$ multiplies $K$ by $9$.
- id: mct-p14-omega-scaling-c
  content: |-
    It increases by a factor of $6$.
  feedback: |-
    The initial and final angular speeds should form a ratio before the exponent is applied. The ratio is $15/5=3$, and squaring it gives $9$, not their difference or sum.
- id: mct-p14-omega-scaling-d
  content: |-
    It decreases by a factor of $9$.
  feedback: |-
    For fixed $I$, increasing angular speed increases kinetic energy. The inverse-square relation does not apply here; $K$ is proportional to $\omega^2$.
- id: mct-p14-omega-scaling-e
  content: |-
    It does not change.
  feedback: |-
    Keeping the axis fixed keeps $I$ fixed, not the energy. The change in $\omega^2$ changes $K_{\mathrm{rot}}$ by a factor of $9$.
```

---

<a id="convert-tangential-speed"></a>
## Convert Tangential Speed to Angular Speed

Angular speed $\omega$ describes the whole rigid body's rotation. Tangential speed belongs to a particular point and depends on its distance from the axis:

$$
v_t=\omega r.
$$

Do not insert a speed in meters per second into a formula that requires radians per second. If the rim speed and radius are given, first calculate

$$
\omega=\frac{v_{\mathrm{rim}}}{R}.
$$

**Example:** A uniform solid disk has $M=6.0\,\mathrm{kg}$, $R=0.40\,\mathrm m$, and rim speed $v_{\mathrm{rim}}=3.2\,\mathrm{m/s}$. Then

$$
\omega=\frac{3.2}{0.40}=8.0\,\mathrm{rad/s},
$$

$$
I=\frac12(6.0)(0.40)^2=0.48\,\mathrm{kg\,m^2},
$$

and

$$
K_{\mathrm{rot}}=\frac12(0.48)(8.0)^2=15.36\,\mathrm J.
$$

```quiz
type: radio
id: mct-p14-tangential-conversion
shuffle: true
content: |-
  A uniform solid disk has $M=4.0\,\mathrm{kg}$ and $R=0.25\,\mathrm m$. Its rim moves at $2.0\,\mathrm{m/s}$. What is the disk's rotational kinetic energy about its central symmetry axis?
options:
- id: mct-p14-tangential-conversion-a
  content: |-
    $4.0\,\mathrm J$
  correct: true
  feedback: |-
    First, $\omega=v_{\mathrm{rim}}/R=2.0/0.25=8.0\,\mathrm{rad/s}$. With $I=\frac12(4.0)(0.25)^2=0.125\,\mathrm{kg\,m^2}$, the energy is $\frac12(0.125)(8.0)^2=4.0\,\mathrm J$.
- id: mct-p14-tangential-conversion-b
  content: |-
    $0.25\,\mathrm J$
  feedback: |-
    This inserts the rim speed $2.0\,\mathrm{m/s}$ directly as though it were $\omega$. Convert with $\omega=v_{\mathrm{rim}}/R$ before using the rotational-energy formula.
- id: mct-p14-tangential-conversion-c
  content: |-
    $8.0\,\mathrm J$
  feedback: |-
    This treats the solid disk like a hoop, or equivalently assigns the rim speed to all of its mass. A disk has mass at radii smaller than $R$ and uses $I=\frac12MR^2$.
- id: mct-p14-tangential-conversion-d
  content: |-
    $0.50\,\mathrm J$
  feedback: |-
    This converts to $\omega=8.0\,\mathrm{rad/s}$ but does not square it. The energy depends on $\omega^2=64$.
- id: mct-p14-tangential-conversion-e
  content: |-
    $0.125\,\mathrm{kg\,m^2}$
  feedback: |-
    This is the disk's moment of inertia, not its rotational kinetic energy. Multiply by $\frac12\omega^2$ to obtain joules.
```

---

<a id="summary"></a>
## Summary

- Identify both the rotating shape and the axis before choosing $I$.
- A standard inertia such as $I=\frac12MR^2$ already contains the body's integrated mass distribution.
- Use
  $$
  K_{\mathrm{rot}}=\frac12I\omega^2
  $$
  with $\omega$ in radians per second.
- Square the radius or length inside $I$, then square $\omega$ inside the energy formula.
- If tangential speed is given, convert with $\omega=v_t/r$ at the stated point.
- Check
  $$
  (\mathrm{kg\,m^2})(\mathrm{s^{-2}})=\mathrm J.
  $$
- Do not replace a disk by a point mass at its rim, and do not add translational energy to a fixed-axis spin calculation.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
