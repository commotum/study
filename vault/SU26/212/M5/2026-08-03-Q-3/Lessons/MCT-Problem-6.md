# Assemble $I_p$ and Center of Mass for a Physical Pendulum

<!--
lesson-id: 212-M5-064
topic-code: MTH212.M5.64
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Pivot Ledger](#pivot-ledger)
- [Source-Video Uniform Rod](#source-rod)
- [Source-Video Rod with a Point Mass](#source-point-mass)
- [Lecture Offset-Pivot Rod](#lecture-offset-pivot)
- [Lecture Rod with an Attached Disk](#lecture-disk)
- [Summary](#summary)

## Prerequisites

- Use the small-angle approximation for pendulum motion.
- Recognize the center of mass of a uniform rod as its midpoint.
- Compute a weighted-average position.
- Use the parallel-axis theorem, $I_p=I_{\mathrm{cm}}+md^2$.
- Know $I_{\mathrm{cm}}=\tfrac1{12}mL^2$ for a uniform rod and $I_{\mathrm{cm}}=\tfrac12mR^2$ for a solid disk.

---

<a id="introduction"></a>
## Introduction

An extended rigid body that swings about a fixed point is a physical pendulum. For small oscillations about a stable equilibrium, its period is

$$
\boxed{T=2\pi\sqrt{\frac{I_p}{Mg\ell}}},
$$

where

- $I_p$ is the entire assembly's moment of inertia about the actual pivot,
- $M$ is the entire assembly's mass, and
- $\ell$ is the distance from that pivot to the assembly's center of mass.

The recognition cues are a rod, disk, or composite rigid body; a pivot away from the center; or a prompt that supplies or asks for moment of inertia. The reusable move is to build two ledgers about the same pivot: one for rotational inertia and one for center of mass. Only then substitute into the period formula.

This period formula assumes the motion stays in the small-angle regime.

**Source-video limiting-case context — `scIVIhChL1I`, 00:08:24–00:10:34.** If a massless support carries one point mass $M$ a distance $L$ from the pivot, then $I_p=ML^2$ and $\ell=L$. Substitution reduces the physical-pendulum formula to the simple-pendulum result. That reduction applies only to this point-mass limit.

---

<a id="pivot-ledger"></a>
## Build the Pivot Ledger

Choose the pivot as $x=0$. For every component $i$, record its mass $m_i$, center position $x_i$, center-of-mass inertia $I_{i,\mathrm{cm}}$, and pivot inertia

$$
I_{i,p}=I_{i,\mathrm{cm}}+m_ix_i^2.
$$

Give every physical component exactly one row. A point mass has $I_{i,\mathrm{cm}}=0$; an extended rod or disk does not. This keeps the component's own inertia and its pivot shift together before any rows are added.

Then add the component rows:

$$
\boxed{I_p=\sum_i I_{i,p}},
$$

$$
\boxed{M=\sum_i m_i},
$$

$$
\boxed{x_{\mathrm{cm}}=\frac{\sum_i m_ix_i}{\sum_i m_i}},
\qquad
\boxed{\ell=\left|x_{\mathrm{cm}}\right|}.
$$

When all component centers lie on the same downward ray from the pivot, simplify the period denominator before rounding:

$$
M\ell=\sum_i m_ix_i,
$$

so the same formula can be written

$$
T=2\pi\sqrt{\frac{\sum_i I_{i,p}}{g\sum_i m_ix_i}}.
$$

The combined-COM form and this torque-sum form are algebraically identical. The latter avoids inserting a rounded intermediate value of $\ell$.

For components that lie on opposite sides of the pivot, use signed $x_i$ in the center-of-mass sum and take the magnitude of the result for $\ell$. In the inertia ledger, the distance is squared, so either side contributes positively.

| Component | $m_i$ | Center position $x_i$ | Pivot inertia $I_{i,p}$ | COM numerator $m_ix_i$ |
| --- | ---: | ---: | ---: | ---: |
| component 1 | $m_1$ | $x_1$ | $I_{1,\mathrm{cm}}+m_1x_1^2$ | $m_1x_1$ |
| component 2 | $m_2$ | $x_2$ | $I_{2,\mathrm{cm}}+m_2x_2^2$ | $m_2x_2$ |
| totals | $M$ | $x_{\mathrm{cm}}=(\sum m_ix_i)/M$ | $I_p$ | $Mx_{\mathrm{cm}}$ |

Two checks catch most setup errors:

1. The assembly center of mass must lie between the component centers and closer to the heavier contribution.
2. Shifting an extended component away from its center must increase its inertia: $I_p>I_{\mathrm{cm}}$ when $d\ne0$.

For two equal point masses, the weighted COM formula reduces to the ordinary midpoint, $(x_1+x_2)/2$. If an equal-mass calculation does not, the mass-position pairs were not kept aligned.

```quiz
type: radio
id: mct-p6-ledger-roles
shuffle: true
content: |-
  A physical pendulum contains two rigid components. Which data must be assembled before using $T=2\pi\sqrt{I_p/(Mg\ell)}$?
options:
- id: mct-p6-ledger-roles-a
  content: |-
    Sum every component's inertia about the actual pivot, sum every component's mass, and find the pivot-to-assembly-COM distance.
  correct: true
  feedback: |-
    The physical-pendulum formula uses three assembly quantities: $I_p=\sum I_{i,p}$, $M=\sum m_i$, and $\ell=|\sum m_ix_i|/M$ measured from the pivot. All three must describe the same full assembly.
- id: mct-p6-ledger-roles-b
  content: |-
    Sum the center-of-mass inertias, use the heaviest component's mass, and set $\ell$ equal to the longest component.
  feedback: |-
    Center-of-mass inertias omit the parallel-axis shifts to the actual pivot. The gravitational torque also comes from every component, so the formula needs total mass and the combined COM distance, not the heaviest mass and longest length.
- id: mct-p6-ledger-roles-c
  content: |-
    Sum every component's inertia about the pivot, but use only the attached mass in $Mg\ell$.
  feedback: |-
    The inertia ledger is complete, but the torque ledger is not. Gravity acts on the rod and every attachment; their torques combine as $Mg\ell$, where $M$ is the assembly's total mass.
- id: mct-p6-ledger-roles-d
  content: |-
    Use the assembly's total mass as though it were a point mass at the farthest end.
  feedback: |-
    Replacing an extended assembly by one end point loses its mass distribution. The period requires both the true $I_p$ and the true combined center of mass; neither is generally fixed by the farthest length alone.
- id: mct-p6-ledger-roles-e
  content: |-
    Use each component's distance from the pivot as $\ell$ in a separate period formula, then add the periods.
  feedback: |-
    Periods do not add component by component. Add inertias and gravitational torque contributions first, reduce them to one $I_p$, one total $M$, and one assembly COM distance $\ell$, then calculate one period.
```

---

<a id="source-rod"></a>
## Source-Video Uniform Rod

### Source-video worked case — `scIVIhChL1I`, 00:00:03–00:02:36

A uniform rod has

$$
L=1.5\ \mathrm m,
\qquad
M=0.60\ \mathrm{kg},
$$

and pivots about one end. The rod's center is $L/2$ from the pivot, so

$$
\ell=\frac{L}{2}=0.75\ \mathrm m.
$$

The end-pivot inertia can be quoted directly,

$$
I_p=\frac13ML^2,
$$

or recovered with the parallel-axis theorem:

$$
\begin{aligned}
I_p
&=I_{\mathrm{cm}}+M\left(\frac L2\right)^2\\
&=\frac1{12}ML^2+\frac14ML^2\\
&=\frac13ML^2.
\end{aligned}
$$

Numerically,

$$
I_p=\frac13(0.60)(1.5)^2=0.45\ \mathrm{kg\,m^2}.
$$

Therefore,

$$
T=2\pi\sqrt{\frac{0.45}{(0.60)(9.8)(0.75)}}
=2.01\ \mathrm s
\approx2.0\ \mathrm s.
$$

The length $L=1.5\ \mathrm m$ sets the rod's geometry, but the torque arm in the period formula is $\ell=0.75\ \mathrm m$. The symbols are not interchangeable.

### M4-2 lecture end-pivot variant

The paired lecture uses $L=0.92\ \mathrm m$ and $g=9.81\ \mathrm{m/s^2}$ and obtains

$$
T=2\pi\sqrt{\frac{2L}{3g}}
=1.57\ \mathrm s
\approx1.6\ \mathrm s.
$$

The rod mass cancels only after its inertia and gravitational torque have both been included.

```quiz
type: radio
id: mct-p6-end-rod
shuffle: true
content: |-
  A uniform rod of length $0.84\ \mathrm m$ and mass $0.50\ \mathrm{kg}$ pivots about one end. Using $g=9.8\ \mathrm{m/s^2}$, which setup is correct?
options:
- id: mct-p6-end-rod-a
  content: |-
    $I_p=0.1176\ \mathrm{kg\,m^2}$, $\ell=0.42\ \mathrm m$, and $T=1.50\ \mathrm s$
  correct: true
  feedback: |-
    An end-pivoted uniform rod has $I_p=\tfrac13ML^2=0.1176\ \mathrm{kg\,m^2}$ and its center is at $\ell=L/2=0.42\ \mathrm m$. Substitution gives $T=2\pi\sqrt{I_p/(Mg\ell)}=1.50\ \mathrm s$.
- id: mct-p6-end-rod-b
  content: |-
    $I_p=0.0294\ \mathrm{kg\,m^2}$, $\ell=0.42\ \mathrm m$, and $T=0.75\ \mathrm s$
  feedback: |-
    The value $0.0294\ \mathrm{kg\,m^2}$ is $I_{\mathrm{cm}}=\tfrac1{12}ML^2$. Because the pivot is at an end, add $M(L/2)^2$ before calculating the period.
- id: mct-p6-end-rod-c
  content: |-
    $I_p=0.1176\ \mathrm{kg\,m^2}$, $\ell=0.84\ \mathrm m$, and $T=1.06\ \mathrm s$
  feedback: |-
    The inertia is correct, but $\ell$ is the pivot-to-COM distance rather than the rod length. A uniform rod's center of mass lies at $L/2=0.42\ \mathrm m$.
- id: mct-p6-end-rod-d
  content: |-
    $I_p=0.3528\ \mathrm{kg\,m^2}$, $\ell=0.42\ \mathrm m$, and $T=2.60\ \mathrm s$
  feedback: |-
    This uses $I_p=ML^2$, which models the entire rod as a point mass at its far end. A uniform rod spreads its mass along the length and has end-pivot inertia $\tfrac13ML^2$.
- id: mct-p6-end-rod-e
  content: |-
    $I_p=0.1176\ \mathrm{kg\,m^2}$, $\ell=0.42\ \mathrm m$, and $T$ cannot be found without the release angle.
  feedback: |-
    Under the stated small-angle model, the period is independent of the particular small release angle. The given geometry and $g$ are enough to calculate $T=1.50\ \mathrm s$.
```

---

<a id="source-point-mass"></a>
## Source-Video Rod with a Point Mass

### Source-video worked case — `scIVIhChL1I`, 00:02:39–00:08:22

The frame shows an end-pivoted uniform rod with

$$
L=1.2\ \mathrm m,
\qquad
m_r=0.50\ \mathrm{kg},
$$

and a $m_p=2.0\ \mathrm{kg}$ attachment at the lower end. Because no dimensions or center inertia are supplied for the attachment, the source treats it as a point mass at $x=L$.

Build the inertia ledger about the pivot:

| Component | Pivot inertia |
| --- | ---: |
| rod | $I_r=\tfrac13m_rL^2=0.240\ \mathrm{kg\,m^2}$ |
| point mass | $I_p^{(\mathrm{point})}=m_pL^2=2.88\ \mathrm{kg\,m^2}$ |
| total | $I_{\mathrm{tot}}=3.12\ \mathrm{kg\,m^2}$ |

For the center-of-mass ledger, the rod's mass acts at $L/2=0.60\ \mathrm m$ and the point mass acts at $L=1.2\ \mathrm m$:

$$
\ell
=\frac{m_r(L/2)+m_pL}{m_r+m_p}
=\frac{(0.50)(0.60)+(2.0)(1.2)}{2.5}
=1.08\ \mathrm m.
$$

This lies between $0.60\ \mathrm m$ and $1.2\ \mathrm m$ and closer to the heavier $2.0\ \mathrm{kg}$ attachment, as expected. The total mass is

$$
M=m_r+m_p=2.5\ \mathrm{kg}.
$$

The period is

$$
T=2\pi\sqrt{\frac{3.12}{(2.5)(9.8)(1.08)}}
=2.16\ \mathrm s.
$$

**Notation correction.** The source initially writes a capital $M$ in the point-mass term, then corrects it aloud to the lowercase mass assigned to the attachment. With unambiguous notation, the term is $m_pL^2$.

### M4-2 lecture point-mass variant

For $m_r=0.35\ \mathrm{kg}$, $m_p=0.25\ \mathrm{kg}$, $L=1.2\ \mathrm m$, and $g=9.81\ \mathrm{m/s^2}$, the paired lecture obtains

$$
I_p=\frac13m_rL^2+m_pL^2=0.528\ \mathrm{kg\,m^2},
$$

$$
\ell=\frac{m_r(L/2)+m_pL}{m_r+m_p}=0.850\ \mathrm m,
$$

$$
T=2.04\ \mathrm s\approx2.0\ \mathrm s.
$$

```quiz
type: radio
id: mct-p6-rod-point-mass
shuffle: true
content: |-
  A $0.40\ \mathrm{kg}$ uniform rod of length $1.0\ \mathrm m$ pivots about its upper end. A $0.60\ \mathrm{kg}$ point mass is attached at the lower end. Using $g=9.8\ \mathrm{m/s^2}$, which assembly values are correct?
options:
- id: mct-p6-rod-point-mass-a
  content: |-
    $I_p=0.733\ \mathrm{kg\,m^2}$, $M=1.00\ \mathrm{kg}$, $\ell=0.800\ \mathrm m$, and $T=1.92\ \mathrm s$
  correct: true
  feedback: |-
    The pivot ledger gives $I_p=\tfrac13(0.40)(1.0)^2+(0.60)(1.0)^2=0.733\ \mathrm{kg\,m^2}$. The COM ledger gives $\ell=[(0.40)(0.50)+(0.60)(1.0)]/1.00=0.800\ \mathrm m$, and these totals produce $T=1.92\ \mathrm s$.
- id: mct-p6-rod-point-mass-b
  content: |-
    $I_p=0.733\ \mathrm{kg\,m^2}$, $M=1.00\ \mathrm{kg}$, $\ell=0.500\ \mathrm m$, and $T=2.43\ \mathrm s$
  feedback: |-
    The inertia and total mass are correct, but $0.500\ \mathrm m$ is only the rod's center. The attached mass shifts the assembly COM toward the lower end, to $0.800\ \mathrm m$.
- id: mct-p6-rod-point-mass-c
  content: |-
    $I_p=0.600\ \mathrm{kg\,m^2}$, $M=1.00\ \mathrm{kg}$, $\ell=0.800\ \mathrm m$, and $T=1.74\ \mathrm s$
  feedback: |-
    The value $0.600\ \mathrm{kg\,m^2}$ includes only the point mass. The rod also rotates about the pivot and contributes $\tfrac13m_rL^2=0.133\ \mathrm{kg\,m^2}$.
- id: mct-p6-rod-point-mass-d
  content: |-
    $I_p=0.633\ \mathrm{kg\,m^2}$, $M=1.00\ \mathrm{kg}$, $\ell=0.800\ \mathrm m$, and $T=1.79\ \mathrm s$
  feedback: |-
    This uses the rod's center inertia $\tfrac1{12}m_rL^2$ without shifting it to the end pivot. The rod's pivot contribution is $\tfrac13m_rL^2$, raising the total to $0.733\ \mathrm{kg\,m^2}$.
- id: mct-p6-rod-point-mass-e
  content: |-
    $I_p=0.733\ \mathrm{kg\,m^2}$, $M=0.60\ \mathrm{kg}$, $\ell=0.800\ \mathrm m$, and $T=2.48\ \mathrm s$
  feedback: |-
    This uses only the attached point mass in the gravitational torque denominator. Gravity acts on both parts, so the physical-pendulum formula needs the total mass $M=0.40+0.60=1.00\ \mathrm{kg}$.
```

---

<a id="lecture-offset-pivot"></a>
## Lecture Offset-Pivot Rod

### M4-2 lecture worked case

A uniform rod is pivoted a distance $L/6$ from its upper end. Its center of mass is at $L/2$, so the pivot-to-COM distance is

$$
\ell=\frac L2-\frac L6=\frac L3.
$$

The tabulated rod formula $I_{\mathrm{cm}}=\tfrac1{12}ML^2$ is about the center, not this pivot. Shift it:

$$
\begin{aligned}
I_p
&=I_{\mathrm{cm}}+M\ell^2\\
&=\frac1{12}ML^2+M\left(\frac L3\right)^2\\
&=\frac7{36}ML^2.
\end{aligned}
$$

Therefore,

$$
T=2\pi\sqrt{\frac{7L}{12g}}.
$$

For the lecture values $L=0.75\ \mathrm m$ and $g=9.81\ \mathrm{m/s^2}$,

$$
T=1.33\ \mathrm s\approx1.3\ \mathrm s.
$$

Moving the pivot changes both $I_p$ and $\ell$. Replacing only one of them while leaving the other at its end-pivot value mixes two different geometries.

```quiz
type: radio
id: mct-p6-offset-pivot
shuffle: true
content: |-
  A $0.70\ \mathrm{kg}$ uniform rod of length $0.90\ \mathrm m$ is pivoted $0.225\ \mathrm m$ from one end. The pivot and center of mass lie on the rod. Using $g=9.8\ \mathrm{m/s^2}$, which result is correct?
options:
- id: mct-p6-offset-pivot-a
  content: |-
    $\ell=0.225\ \mathrm m$, $I_p=0.0827\ \mathrm{kg\,m^2}$, and $T=1.45\ \mathrm s$
  correct: true
  feedback: |-
    The rod center is at $0.450\ \mathrm m$, so its distance from the pivot is $\ell=0.450-0.225=0.225\ \mathrm m$. Then $I_p=\tfrac1{12}ML^2+M\ell^2=0.0827\ \mathrm{kg\,m^2}$ and $T=1.45\ \mathrm s$.
- id: mct-p6-offset-pivot-b
  content: |-
    $\ell=0.225\ \mathrm m$, $I_p=0.0473\ \mathrm{kg\,m^2}$, and $T=1.10\ \mathrm s$
  feedback: |-
    The value $0.0473\ \mathrm{kg\,m^2}$ is the rod's inertia about its center. The actual pivot is $0.225\ \mathrm m$ away, so the parallel-axis term $M\ell^2$ must be added.
- id: mct-p6-offset-pivot-c
  content: |-
    $\ell=0.225\ \mathrm m$, $I_p=0.189\ \mathrm{kg\,m^2}$, and $T=2.20\ \mathrm s$
  feedback: |-
    The value $0.189\ \mathrm{kg\,m^2}=\tfrac13ML^2$ belongs to a pivot at the rod's end. This pivot is inside the rod, so shift $I_{\mathrm{cm}}$ by the actual $0.225\ \mathrm m$ distance instead.
- id: mct-p6-offset-pivot-d
  content: |-
    $\ell=0.90\ \mathrm m$, $I_p=0.0827\ \mathrm{kg\,m^2}$, and $T=0.727\ \mathrm s$
  feedback: |-
    The inertia is correct, but $\ell$ is not the rod's full length. It is the distance from this pivot to the rod's center, which is $0.225\ \mathrm m$.
- id: mct-p6-offset-pivot-e
  content: |-
    $\ell=0$ because the pivot lies on the rod, so the physical-pendulum period is zero.
  feedback: |-
    A pivot lying somewhere on the rod need not coincide with the rod's center. Here the center is $0.225\ \mathrm m$ from the pivot, so gravity supplies a restoring torque and the period is finite.
```

---

<a id="lecture-disk"></a>
## Lecture Rod with an Attached Disk

### M4-2 lecture worked case

The lecture attaches a solid disk of mass $m_d$ and radius $R$ to the lower end of an end-pivoted rod of mass $m_r$ and length $L$. The diagram places the disk center at

$$
x_d=L+R.
$$

The disk is extended, so its pivot inertia has two terms:

$$
I_{d,p}
=\underbrace{\frac12m_dR^2}_{\text{rotation about its center}}
+\underbrace{m_d(L+R)^2}_{\text{shift to the pendulum pivot}}.
$$

The component ledger is therefore

$$
I_p
=\frac13m_rL^2
+\frac12m_dR^2
+m_d(L+R)^2.
$$

The assembly COM distance is

$$
\ell
=\frac{m_r(L/2)+m_d(L+R)}{m_r+m_d}.
$$

For the lecture values

$$
m_r=0.35\ \mathrm{kg},\quad
m_d=0.65\ \mathrm{kg},\quad
L=1.2\ \mathrm m,\quad
R=0.42\ \mathrm m,\quad
g=9.81\ \mathrm{m/s^2},
$$

the results are

$$
I_p=1.931\ \mathrm{kg\,m^2},
\qquad
\ell=1.263\ \mathrm m,
$$

$$
T=2.481\ \mathrm s\approx2.5\ \mathrm s.
$$

Treating the disk as a point mass at its center would omit $\tfrac12m_dR^2$. The source video uses that approximation for an attachment whose dimensions and center inertia are not supplied. It does not apply to a disk whose radius and center inertia are given.

```quiz
type: radio
id: mct-p6-rod-disk
shuffle: true
content: |-
  A $0.30\ \mathrm{kg}$ uniform rod of length $0.80\ \mathrm m$ pivots about its upper end. A solid disk of mass $0.50\ \mathrm{kg}$ and radius $0.20\ \mathrm m$ is attached below it, with its center $L+R=1.00\ \mathrm m$ from the pivot. Using $g=9.8\ \mathrm{m/s^2}$, which result is correct?
options:
- id: mct-p6-rod-disk-a
  content: |-
    $I_p=0.574\ \mathrm{kg\,m^2}$, $\ell=0.775\ \mathrm m$, and $T=1.93\ \mathrm s$
  correct: true
  feedback: |-
    The pivot ledger gives $I_p=\tfrac13(0.30)(0.80)^2+\tfrac12(0.50)(0.20)^2+(0.50)(1.00)^2=0.574\ \mathrm{kg\,m^2}$. The COM ledger gives $\ell=[(0.30)(0.40)+(0.50)(1.00)]/0.80=0.775\ \mathrm m$, producing $T=1.93\ \mathrm s$.
- id: mct-p6-rod-disk-b
  content: |-
    $I_p=0.564\ \mathrm{kg\,m^2}$, $\ell=0.775\ \mathrm m$, and $T=1.91\ \mathrm s$
  feedback: |-
    This omits the disk's $I_{\mathrm{cm}}=\tfrac12m_dR^2=0.010\ \mathrm{kg\,m^2}$. The disk's center travels around the pivot and the disk also rotates about its own center, so both terms belong in $I_p$.
- id: mct-p6-rod-disk-c
  content: |-
    $I_p=0.074\ \mathrm{kg\,m^2}$, $\ell=0.775\ \mathrm m$, and $T=0.693\ \mathrm s$
  feedback: |-
    This includes the rod and the disk's center inertia but omits the large shift term $m_d(L+R)^2=0.500\ \mathrm{kg\,m^2}$. Every component inertia must be about the pendulum pivot.
- id: mct-p6-rod-disk-d
  content: |-
    $I_p=0.510\ \mathrm{kg\,m^2}$, $\ell=0.775\ \mathrm m$, and $T=1.82\ \mathrm s$
  feedback: |-
    This includes the disk's two terms but drops the rod contribution $\tfrac13m_rL^2=0.064\ \mathrm{kg\,m^2}$. Both rigid components rotate and contribute to the total inertia.
- id: mct-p6-rod-disk-e
  content: |-
    $I_p=0.574\ \mathrm{kg\,m^2}$, $\ell=1.00\ \mathrm m$, and $T=1.70\ \mathrm s$
  feedback: |-
    The disk center is at $1.00\ \mathrm m$, but $\ell$ locates the center of mass of the rod–disk assembly. The rod pulls that weighted average upward to $0.775\ \mathrm m$.
```

---

<a id="summary"></a>
## Summary

For a small-angle physical pendulum:

1. Mark the actual pivot and measure every component center from it.
2. Shift each extended component to that pivot with $I_{i,p}=I_{i,\mathrm{cm}}+m_ix_i^2$.
3. Add the component rows to obtain $I_p=\sum I_{i,p}$.
4. Find the total mass $M=\sum m_i$ and assembly COM distance $\ell=|\sum m_ix_i|/M$.
5. Use
   $$
   T=2\pi\sqrt{\frac{I_p}{Mg\ell}}.
   $$

The main traps are using an object's full length in place of $\ell$, inserting only one component's mass in the gravitational torque, quoting $I_{\mathrm{cm}}$ without a parallel-axis shift, or treating an extended disk as a point mass. The simple-pendulum formula is recovered only in the limiting case $I_p=ML^2$ and $\ell=L$ for a point mass on a massless support.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
