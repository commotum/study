# Find Rolling Speed by Including Both Kinetic-Energy Terms

<!--
lesson-id: 212-M3-051
topic-code: MTH212.M3.51
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Rolling-Energy Equation](#build-the-rolling-energy-equation)
- [Solve the Source-Video Solid Sphere](#solve-the-source-video-solid-sphere)
- [Use Ramp Length Only When Height Is Unknown](#use-ramp-length-only-when-height-is-unknown)
- [Compare Shapes with the Inertia Factor](#compare-shapes-with-the-inertia-factor)
- [Summary](#summary)

## Prerequisites

- Use gravitational potential energy $U_g=mgh$.
- Use translational and rotational kinetic energy.
- Recognize the rolling-without-slipping condition $v_{\mathrm{cm}}=\omega R$.
- Select a center-of-mass moment of inertia for a specified rigid shape.
- Use $h=d\sin\theta$ when $d$ is distance along an incline.

---

<a id="introduction"></a>
## Introduction

When a rigid object starts from rest and rolls without slipping through a vertical drop $h$, its lost gravitational potential energy becomes two kinds of kinetic energy:

$$
mgh=\frac12mv^2+\frac12I\omega^2.
$$

The first term describes translation of the center of mass. The second describes rotation about the center of mass. Omitting either term changes the final speed.

Use this sequence:

1. Find the vertical drop $h$.
2. Write both final kinetic-energy terms.
3. Substitute the shape's inertia in the form $I=\beta mR^2$.
4. Use no slip: $\omega=v/R$.
5. Cancel common factors, then solve for the positive speed.

This model assumes the object starts from rest, rolls without slipping on a fixed surface, and loses negligible energy to air resistance, deformation, or rolling resistance. Static friction can enforce the rolling constraint without dissipating mechanical energy in this ideal model.

---

<a id="build-the-rolling-energy-equation"></a>
## Build the Rolling-Energy Equation

Write the center-of-mass inertia as

$$
I=\beta mR^2,
$$

where the dimensionless factor $\beta$ identifies the shape. Substitute this and $\omega=v/R$ into the energy equation:

$$
\begin{aligned}
mgh
&=\frac12mv^2+\frac12(\beta mR^2)\left(\frac vR\right)^2\\
&=\frac12mv^2+\frac12\beta mv^2\\
&=\frac12(1+\beta)mv^2.
\end{aligned}
$$

Mass cancels from every term, and the two factors of $R$ in rotational energy cancel. Therefore,

$$
\boxed{v=\sqrt{\frac{2gh}{1+\beta}}}.
$$

The positive root is selected because $v$ denotes speed. The formula also shows why neither the object's mass nor its radius affects the ideal final speed for a fixed shape and vertical drop.

The units provide a quick check. Because $\beta$ is dimensionless,

$$
\left[\frac{2gh}{1+\beta}\right]
=\frac{(\mathrm{m/s^2})(\mathrm m)}{1}
=\mathrm{m^2/s^2},
$$

so its square root has units of $\mathrm{m/s}$.

Useful shape factors are

| Rolling object | Center-of-mass inertia | $\beta$ |
| --- | --- | ---: |
| Thin hoop | $mR^2$ | $1$ |
| Solid disk or cylinder | $\frac12mR^2$ | $\frac12$ |
| Solid sphere | $\frac25mR^2$ | $\frac25$ |
| Thin hollow sphere | $\frac23mR^2$ | $\frac23$ |

```quiz
type: radio
id: mct-p15-general-form
shuffle: true
content: |-
  A rigid object starts from rest and rolls without slipping through a vertical drop $h$. Its center-of-mass inertia is $I=\beta mR^2$. Which expression gives its final center-of-mass speed?
options:
- id: mct-p15-general-form-a
  content: |-
    $v=\sqrt{\dfrac{2gh}{1+\beta}}$
  correct: true
  feedback: |-
    Rolling has both translational and rotational kinetic energy. Substituting $I=\beta mR^2$ and $\omega=v/R$ gives $mgh=\frac12(1+\beta)mv^2$, so $v=\sqrt{2gh/(1+\beta)}$.
- id: mct-p15-general-form-b
  content: |-
    $v=\sqrt{2gh}$
  feedback: |-
    This is the speed of a frictionless sliding particle or a model with $\beta=0$. A rolling rigid body has rotational kinetic energy, so its denominator contains the additional factor $1+\beta$.
- id: mct-p15-general-form-c
  content: |-
    $v=\sqrt{\dfrac{2gh}{\beta}}$
  feedback: |-
    This keeps only rotational kinetic energy, $\frac12\beta mv^2$, and omits center-of-mass translation. Rolling requires both terms, producing $1+\beta$ rather than $\beta$.
- id: mct-p15-general-form-d
  content: |-
    $v=\sqrt{\dfrac{2gh}{1-\beta}}$
  feedback: |-
    Translational and rotational kinetic energy are both positive and must be added. Their coefficients combine as $1+\beta$; subtracting rotational energy would make the speed too large.
- id: mct-p15-general-form-e
  content: |-
    $v=\sqrt{2gh(1+\beta)}$
  feedback: |-
    The factor $1+\beta$ multiplies $v^2$ in the energy ledger, so solving for $v^2$ divides by that factor. Multiplying instead predicts that adding rotational inertia makes the object faster.
```

---

<a id="solve-the-source-video-solid-sphere"></a>
## Solve the Source-Video Solid Sphere

**Source-video worked problem (`REIP2mf6sIQ`, 00:03:16–00:07:00):** A sphere starts from rest and rolls down a $20^\circ$ incline from a vertical height of $50\,\mathrm m$. Find its speed at the bottom.

**Frame check (03:24):** The $50\,\mathrm m$ label is drawn vertically. Because the vertical drop is already known, the $20^\circ$ angle is extraneous; no ramp length or trigonometric conversion is needed.

**Source clarification:** The video uses

$$
I=\frac25mR^2,
$$

which is the center-of-mass inertia of a uniform solid sphere. It is not the inertia of every spherical object; a thin hollow sphere uses $I=\frac23mR^2$.

For the solid sphere, $\beta=2/5$. The source calculation is

$$
\begin{aligned}
mgh
&=\frac12mv^2+\frac12\left(\frac25mR^2\right)\left(\frac vR\right)^2\\
&=\left(\frac12+\frac15\right)mv^2\\
&=\left(\frac5{10}+\frac2{10}\right)mv^2\\
&=\frac7{10}mv^2.
\end{aligned}
$$

Cancel $m$ and isolate $v^2$:

$$
v^2=\frac{10gh}{7}.
$$

The equation for $v^2$ has positive and negative algebraic roots, but the requested quantity is speed. Select the nonnegative root:

$$
v=\sqrt{\frac{10gh}{7}}.
$$

With $g=9.8\,\mathrm{m/s^2}$ and $h=50\,\mathrm m$,

$$
\boxed{v=\sqrt{\frac{10(9.8)(50)}7}=26.5\,\mathrm{m/s}}.
$$

The frictionless sliding speed from the same height would be

$$
v_{\mathrm{slide}}=\sqrt{2gh}=31.3\,\mathrm{m/s}.
$$

The rolling value is smaller because some of the fixed energy becomes rotational kinetic energy. This supplies a numerical upper-bound check: an ideal rolling result with $\beta>0$ must satisfy $v<v_{\mathrm{slide}}$.

```quiz
type: radio
id: mct-p15-solid-cylinder-mirror
shuffle: true
content: |-
  A uniform solid cylinder starts from rest and rolls without slipping through a vertical drop of $4.0\,\mathrm m$. Using $g=9.8\,\mathrm{m/s^2}$ and $I=\frac12mR^2$, what is its final center-of-mass speed?
options:
- id: mct-p15-solid-cylinder-mirror-a
  content: |-
    $7.23\,\mathrm{m/s}$
  correct: true
  feedback: |-
    A solid cylinder has $\beta=1/2$, so $v=\sqrt{2gh/(1+\beta)}=\sqrt{2(9.8)(4.0)/(3/2)}=7.23\,\mathrm{m/s}$.
- id: mct-p15-solid-cylinder-mirror-b
  content: |-
    $8.85\,\mathrm{m/s}$
  feedback: |-
    This is $\sqrt{2gh}$, the frictionless sliding speed. The cylinder also rotates, so including $\frac12I\omega^2$ reduces the rolling speed to $7.23\,\mathrm{m/s}$.
- id: mct-p15-solid-cylinder-mirror-c
  content: |-
    $7.48\,\mathrm{m/s}$
  feedback: |-
    This uses the solid-sphere factor $\beta=2/5$. The object is a solid cylinder, whose factor is $\beta=1/2$ and whose final speed is $7.23\,\mathrm{m/s}$.
- id: mct-p15-solid-cylinder-mirror-d
  content: |-
    $6.86\,\mathrm{m/s}$
  feedback: |-
    This uses the hollow-sphere factor $\beta=2/3$. Shape determines the inertia factor; for a solid cylinder use $\beta=1/2$, giving $7.23\,\mathrm{m/s}$.
- id: mct-p15-solid-cylinder-mirror-e
  content: |-
    $12.5\,\mathrm{m/s}$
  feedback: |-
    This equates $mgh$ only to the cylinder's rotational term. Center-of-mass translation also carries energy, so the correct ledger gives $7.23\,\mathrm{m/s}$.
```

---

<a id="use-ramp-length-only-when-height-is-unknown"></a>
## Use Ramp Length Only When Height Is Unknown

If the problem gives distance $d$ along an incline rather than vertical height, first use

$$
\sin\theta=\frac{\text{opposite}}{\text{hypotenuse}}=\frac hd,
\qquad
h=d\sin\theta.
$$

Do not substitute the path length $d$ directly into $mgh$. Gravitational potential energy depends on vertical displacement.

**Lecture-note controlled application (M2-5):** A thin hollow sphere of mass $0.65\,\mathrm{kg}$ and radius $0.28\,\mathrm m$ starts from rest and rolls without slipping $0.86\,\mathrm m$ down a $38^\circ$ incline. For a hollow sphere,

$$
I=\frac23mR^2,
\qquad
\beta=\frac23.
$$

Using $h=d\sin\theta$ in the rolling formula gives

$$
\begin{aligned}
v
&=\sqrt{\frac{2g(d\sin\theta)}{1+2/3}}\\
&=\sqrt{\frac65gd\sin\theta}\\
&=\sqrt{\frac65(9.81)(0.86)\sin38^\circ}\\
&=\boxed{2.5\,\mathrm{m/s}}.
\end{aligned}
$$

The supplied mass and radius cancel. The ramp angle matters here only because $d$ is an along-ramp distance rather than a vertical height.

```quiz
type: radio
id: mct-p15-hollow-sphere-ramp
shuffle: true
content: |-
  A thin hollow sphere starts from rest and rolls without slipping $1.2\,\mathrm m$ down a $30^\circ$ incline. Using $I=\frac23mR^2$ and $g=9.8\,\mathrm{m/s^2}$, what is its final center-of-mass speed?
options:
- id: mct-p15-hollow-sphere-ramp-a
  content: |-
    $2.66\,\mathrm{m/s}$
  correct: true
  feedback: |-
    The vertical drop is $h=(1.2)\sin30^\circ=0.60\,\mathrm m$. With $\beta=2/3$, $v=\sqrt{2gh/(1+\beta)}=\sqrt{(6/5)(9.8)(0.60)}=2.66\,\mathrm{m/s}$.
- id: mct-p15-hollow-sphere-ramp-b
  content: |-
    $3.76\,\mathrm{m/s}$
  feedback: |-
    This treats the $1.2\,\mathrm m$ path length as the vertical drop. Potential energy uses $h=d\sin30^\circ=0.60\,\mathrm m$, which gives $2.66\,\mathrm{m/s}$.
- id: mct-p15-hollow-sphere-ramp-c
  content: |-
    $3.43\,\mathrm{m/s}$
  feedback: |-
    This uses the correct vertical drop but keeps only translational kinetic energy, giving the sliding speed $\sqrt{2gh}$. A rolling hollow sphere also has rotational energy, so its speed is $2.66\,\mathrm{m/s}$.
- id: mct-p15-hollow-sphere-ramp-d
  content: |-
    $2.90\,\mathrm{m/s}$
  feedback: |-
    This uses the solid-sphere factor $\beta=2/5$. A thin hollow sphere has $\beta=2/3$, more rotational inertia per $mR^2$, and therefore the lower speed $2.66\,\mathrm{m/s}$.
- id: mct-p15-hollow-sphere-ramp-e
  content: |-
    $1.88\,\mathrm{m/s}$
  feedback: |-
    This inserts an extra factor of $\sin30^\circ$ after already converting $d$ to $h$. Apply the geometry once: $h=d\sin\theta$, then use $v=\sqrt{2gh/(1+\beta)}$.
```

---

<a id="compare-shapes-with-the-inertia-factor"></a>
## Compare Shapes with the Inertia Factor

For objects released from rest through the same vertical height,

$$
v=\sqrt{\frac{2gh}{1+\beta}}.
$$

Increasing $\beta$ increases the fraction of energy stored in rotation and lowers the center-of-mass speed. A frictionless slider corresponds to $\beta=0$ and therefore sets the upper bound. Among common rolling shapes, a solid sphere with $\beta=2/5$ is faster than a solid cylinder with $\beta=1/2$, which is faster than a hollow sphere with $\beta=2/3$, which is faster than a hoop with $\beta=1$.

This comparison assumes the objects roll without slipping and lose no mechanical energy. Static friction is part of the no-slip constraint; it is not automatically an energy-loss term.

```quiz
type: radio
id: mct-p15-shape-order
shuffle: true
content: |-
  A frictionless slider, a uniform solid sphere, and a thin hoop all start from rest at the same vertical height. The sphere and hoop roll without slipping. Which ordering of their center-of-mass speeds at the bottom is correct?
options:
- id: mct-p15-shape-order-a
  content: |-
    $v_{\mathrm{slider}}>v_{\mathrm{sphere}}>v_{\mathrm{hoop}}$
  correct: true
  feedback: |-
    The speed decreases as $\beta$ increases in $v=\sqrt{2gh/(1+\beta)}$. The slider has $\beta=0$, the solid sphere $2/5$, and the hoop $1$, so $v_{\mathrm{slider}}>v_{\mathrm{sphere}}>v_{\mathrm{hoop}}$.
- id: mct-p15-shape-order-b
  content: |-
    $v_{\mathrm{sphere}}>v_{\mathrm{slider}}>v_{\mathrm{hoop}}$
  feedback: |-
    The slider puts all lost potential energy into translation and therefore provides the upper-bound speed. The rolling sphere diverts some energy into rotation, so it cannot outrun the ideal slider from the same height.
- id: mct-p15-shape-order-c
  content: |-
    $v_{\mathrm{slider}}>v_{\mathrm{hoop}}>v_{\mathrm{sphere}}$
  feedback: |-
    The hoop has the larger inertia factor: $\beta_{\mathrm{hoop}}=1$ versus $\beta_{\mathrm{sphere}}=2/5$. A larger $\beta$ gives a larger denominator and a lower center-of-mass speed, so the sphere is faster than the hoop.
- id: mct-p15-shape-order-d
  content: |-
    $v_{\mathrm{hoop}}>v_{\mathrm{sphere}}>v_{\mathrm{slider}}$
  feedback: |-
    This reverses the role of rotational inertia. Energy stored in rotation reduces the translational speed; the slider is fastest, and the hoop's large $\beta=1$ makes it slowest of the three.
- id: mct-p15-shape-order-e
  content: |-
    $v_{\mathrm{slider}}=v_{\mathrm{sphere}}=v_{\mathrm{hoop}}$
  feedback: |-
    Equal vertical drops supply equal total energy per unit mass, but the rolling objects divide that energy between translation and rotation. Their different $\beta$ values therefore produce different center-of-mass speeds.
```

---

<a id="summary"></a>
## Summary

For a rigid object rolling without slipping from rest:

1. Identify the vertical drop. If an incline gives path length $d$, use $h=d\sin\theta$.
2. Write $mgh=\frac12mv^2+\frac12I\omega^2$.
3. Substitute $I=\beta mR^2$ and $\omega=v/R$.
4. Cancel $m$ and $R^2$, then use
   $$
   v=\sqrt{\frac{2gh}{1+\beta}}.
   $$
5. Check that the rolling speed is below the frictionless sliding bound $\sqrt{2gh}$ when $\beta>0$.

The main errors are omitting one kinetic-energy term, choosing the wrong shape factor, confusing path length with vertical height, using the incline angle after height is already known, and treating static friction as automatically dissipative.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
