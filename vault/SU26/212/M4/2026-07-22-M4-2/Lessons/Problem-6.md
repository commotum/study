# Finding the Period of a Rod–Disk Physical Pendulum

<!--
lesson-id: 212-M4-015
topic-code: MTH212.M4.15
-->

## Table of Contents

- [Introduction](#introduction)
- [Locate Each Center of Mass](#locate-each-center-of-mass)
- [Understand the Parallel-Axis Theorem](#understand-the-parallel-axis-theorem)
- [Build the Total Moment of Inertia](#build-the-total-moment-of-inertia)
- [Build the Gravitational Torque Factor](#build-the-gravitational-torque-factor)
- [Assemble and Evaluate the Period](#assemble-and-evaluate-the-period)
- [Apply the Method to the Given Pendulum](#apply-the-method-to-the-given-pendulum)
- [Summary](#summary)

## Prerequisites

- Know that a moment of inertia is defined relative to a particular rotation axis.
- Know $I_{\mathrm{rod,end}}=\frac13mL^2$ and $I_{d,\mathrm{cm}}=\frac12mr^2$.
- Substitute several quantities into a fraction containing a square root.

---

<a id="introduction"></a>
## Introduction

For a rigid physical pendulum making small oscillations,

$$
T=2\pi\sqrt{\frac{I_p}{Mg\,\ell}}.
$$

For a composite object, it is usually safer not to calculate the combined center of mass first. Instead, build two sums:

$$
T=2\pi\sqrt{
\frac{\sum I_{i,p}}
{g\sum m_i r_i}
}.
$$

- The numerator is a sum of **moments of inertia about the pivot**.
- The denominator contains a sum of **mass times distance from the pivot**.

For a rod of length $L$ with a disk of radius $R$ attached tangentially at its lower end, the rod's center is at $L/2$ and the disk's center is at $L+R$.

| Component | Pivot distance $r_i$ | Contribution to $I_p$ | Contribution to $\sum m_i r_i$ |
|---|---:|---:|---:|
| Uniform rod | $L/2$ | $\frac13m_rL^2$ | $m_r(L/2)$ |
| Solid disk | $L+R$ | $\frac12m_dR^2+m_d(L+R)^2$ | $m_d(L+R)$ |

Read each row as a translation from the object in the diagram to the two algebraic terms it contributes.

---

<a id="locate-each-center-of-mass"></a>
## Locate Each Center of Mass

**Example:** A uniform rod of length $0.90\ \mathrm{m}$ hangs from a pivot at its upper end. A disk of radius $0.20\ \mathrm{m}$ is attached at the rod's lower end as shown. How far is each center of mass from the pivot?

**Explanation**

The rod's center of mass is halfway along the rod:

$$
r_r=\frac{L}{2}=0.45\ \mathrm{m}.
$$

The rod reaches the nearest edge of the disk. The disk's center is one additional radius below that point:

$$
r_d=L+R=0.90+0.20=1.10\ \mathrm{m}.
$$

**Watch Out!** The disk's center is not at $L$. The length $L$ reaches only the disk's edge.

```quiz
type: radio
id: problem-6-distance-q1
content: |-
  A rod of length $L$ is pivoted at its upper end, and a disk of radius $R$ is attached tangentially at the rod's lower end. What is the distance from the pivot to the disk's center?
options:
- id: a
  content: |-
    $L+R$
  correct: true
  feedback: |-
    The rod length $L$ reaches the attachment point on the disk's near edge. The disk's center is one additional radius $R$ farther from the pivot, so the center distance is $L+R$.
- id: b
  content: |-
    $L$
  feedback: |-
    The distance $L$ ends at the rod–disk attachment point on the disk's edge. The physical-pendulum calculation needs the disk's center of mass, which lies another radius away at $L+R$.
- id: c
  content: |-
    $L-R$
  feedback: |-
    Subtracting $R$ would place the disk's center above the rod's lower end. In the diagram the disk extends beyond that end, so moving from the pivot to its center requires $L+R$, not $L-R$.
- id: d
  content: |-
    $\dfrac{L+R}{2}$
  feedback: |-
    This treats $L$ and $R$ like two endpoint coordinates to average. They are consecutive distances along the same pivot-to-center path, so they must be added: $r_d=L+R$.
```

---

<a id="understand-the-parallel-axis-theorem"></a>
## Understand the Parallel-Axis Theorem

A moment of inertia is always the moment of inertia **about a particular axis**. The subscript tells you which axis a formula uses:

$$
I_{d,\mathrm{cm}}=\frac12m_dR^2
$$

is about an axis through the disk's center of mass. But the disk in this pendulum does not rotate about its own center. The entire disk swings around the pivot at the top of the rod.

When the known axis passes through the center of mass and the required axis is parallel to it, use the **parallel-axis theorem**:

$$
\boxed{I_p=I_{\mathrm{cm}}+Md^2}.
$$

Here:

- $I_{\mathrm{cm}}$ describes how the object's mass is spread around its own center;
- $M$ is the mass of that one component;
- $d$ is the perpendicular distance from that component's center-of-mass axis to the new pivot axis;
- $Md^2$ accounts for carrying the component's center of mass around the pivot.

In this two-dimensional diagram, both rotation axes point perpendicular to the page, so they are parallel. For the disk, their separation is the pivot-to-disk-center distance

$$
r_d=L+R.
$$

Therefore,

$$
\boxed{
I_{d,p}
=\underbrace{\frac12m_dR^2}_{\mathrm{disk about its own center}}
+\underbrace{m_d(L+R)^2}_{\mathrm{disk center carried around pivot}}
}.
$$

The shift term is **added** to $I_{\mathrm{cm}}$; it does not replace it. Moving the axis away from the center of mass must increase the moment of inertia, and both terms have units $\mathrm{kg}\,\mathrm{m}^2$.

Use this decision rule for each component:

1. Name the axis you actually need: here, the top pivot.
2. Check the axis used by the formula you know.
3. If it is already the required pivot axis, use it unchanged.
4. If it is a parallel center-of-mass axis, add $Md^2$ using the distance between the two axes.

That is why the rod is treated differently. Its tabulated end-axis formula

$$
I_{R,p}=\frac13m_rL^2
$$

is already about the pendulum pivot, so shifting it again would double-count the axis change. If only the rod's center-axis formula were known, the theorem would reproduce the end-axis result:

$$
\begin{aligned}
I_{R,p}
&=I_{R,\mathrm{cm}}+m_r\left(\frac L2\right)^2\\
&=\frac1{12}m_rL^2+\frac14m_rL^2\\
&=\frac13m_rL^2.
\end{aligned}
$$

---

<a id="build-the-total-moment-of-inertia"></a>
## Build the Total Moment of Inertia

**Example:** Write the total moment of inertia about the pivot for the rod–disk pendulum.

**Explanation**

First compare the axis of each known formula with the axis the pendulum actually rotates around.

The rod is already described by its moment of inertia about one end, and that end is the pendulum pivot:

$$
I_{R,p}=\frac13m_rL^2.
$$

The disk's known formula is about its own center, not the pendulum pivot. Shift it to the parallel pivot axis using $r_d=L+R$:

$$
I_{d,p}
=I_{d,\mathrm{cm}}+m_dr_d^2
=\frac12m_dR^2+m_d(L+R)^2.
$$

Therefore,

$$
I_p
=\frac13m_rL^2+\frac12m_dR^2+m_d(L+R)^2.
$$

```quiz
type: radio
id: problem-6-inertia-q1
content: |-
  Which expression is the total pivot-axis moment of inertia of the rod–disk pendulum?
options:
- id: a
  content: |-
    $\dfrac13m_rL^2+\dfrac12m_dR^2+m_d(L+R)^2$
  correct: true
  feedback: |-
    Total pivot-axis inertia is the sum of each component's inertia about that pivot. The rod contributes $\frac13m_rL^2$, while the disk contributes its center-axis inertia $\frac12m_dR^2$ plus the parallel-axis shift $m_d(L+R)^2$.
- id: b
  content: |-
    $\dfrac13m_rL^2+\dfrac12m_dR^2$
  feedback: |-
    This uses the disk's inertia about its own center as though its center lay at the pendulum pivot. Because the center is $L+R$ away, the parallel-axis theorem requires the additional term $m_d(L+R)^2$.
- id: c
  content: |-
    $\dfrac13m_rL^2+m_d(L+R)^2$
  feedback: |-
    The term $m_d(L+R)^2$ accounts for translating the disk's center around the pivot, but the disk also rotates about its own center. Its finite radius therefore adds $I_{\mathrm{cm}}=\frac12m_dR^2$.
- id: d
  content: |-
    $\dfrac13m_rL^2+\dfrac12m_dR^2+m_d(L-R)^2$
  feedback: |-
    The inertia structure is right, but the parallel-axis distance is not. The disk's center lies beyond the rod's lower end, so its pivot distance is $L+R$ and the shift term is $m_d(L+R)^2$.
```

---

<a id="build-the-gravitational-torque-factor"></a>
## Build the Gravitational Torque Factor

**Example:** Write the small-angle restoring-torque factor for the same rod and disk.

**Explanation**

Each component contributes its weight times the distance from the pivot to its own center of mass:

$$
g\sum m_i r_i
=g\left[m_r\left(\frac{L}{2}\right)+m_d(L+R)\right].
$$

This denominator uses one power of distance. Do not copy the squared distances from the inertia sum into the torque sum.

```quiz
type: radio
id: problem-6-torque-q1
content: |-
  Which expression is the gravitational torque factor for the rod–disk pendulum in the small-angle period formula?
options:
- id: a
  content: |-
    $g\left[m_r\left(\dfrac{L}{2}\right)+m_d(L+R)\right]$
  correct: true
  feedback: |-
    Gravity acts at each component's center of mass, so the small-angle restoring-torque coefficient adds $m_i g r_i$ for the rod and disk. With $r_r=L/2$ and $r_d=L+R$, the factor is $g[m_r(L/2)+m_d(L+R)]$.
- id: b
  content: |-
    $g\left[m_rL+m_d(L+R)\right]$
  feedback: |-
    This places all of the rod's weight at its lower end. A uniform rod's weight acts at its midpoint, so its torque contribution uses $m_rg(L/2)$; only the disk center uses the larger distance $L+R$.
- id: c
  content: |-
    $g\left[m_r\left(\dfrac{L}{2}\right)^2+m_d(L+R)^2\right]$
  feedback: |-
    This confuses the inertia weighting with the gravitational lever arm. Moment of inertia contains squared distances, but torque from each weight is force times the first power of its center-of-mass distance, $m_i g r_i$.
- id: d
  content: |-
    $g(m_r+m_d)(L+R)$
  feedback: |-
    This locates both component masses at the disk's center. The rod's weight acts at $L/2$, while the disk's weight acts at $L+R$, so their torque contributions must remain $g[m_r(L/2)+m_d(L+R)]$.
```

---

<a id="assemble-and-evaluate-the-period"></a>
## Assemble and Evaluate the Period

**Example:** Find the small-angle period for $m_r=0.30\ \mathrm{kg}$, $m_d=0.50\ \mathrm{kg}$, $L=1.0\ \mathrm{m}$, and $R=0.20\ \mathrm{m}$.

**Explanation**

Evaluate the two ledgers separately:

$$
\begin{aligned}
I_p
&=\frac13(0.30)(1.0)^2
+\frac12(0.50)(0.20)^2
+(0.50)(1.0+0.20)^2\\
&=0.830\ \mathrm{kg}\,\mathrm{m}^2,
\end{aligned}
$$

and

$$
\begin{aligned}
\sum m_i r_i
&=(0.30)\left(\frac{1.0}{2}\right)
+(0.50)(1.0+0.20)\\
&=0.750\ \mathrm{kg}\,\mathrm{m}.
\end{aligned}
$$

Then assemble the period:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{0.830}{(9.81)(0.750)}}\\
&=2.110\ldots\ \mathrm{s}\\
&\approx2.1\ \mathrm{s}.
\end{aligned}
$$

The units confirm that the square root produces time:

$$
\frac{\mathrm{kg}\,\mathrm{m}^2}
{(\mathrm{m}/\mathrm{s}^2)(\mathrm{kg}\,\mathrm{m})}
=\mathrm{s}^2.
$$

For a calculator, enter the grouped expression

$$
2\pi\sqrt{\frac{0.830}{9.81(0.750)}}.
$$

Keep the complete numerator and denominator inside the radical.

```quiz
type: radio
id: problem-6-assemble-q1
content: |-
  For a composite physical pendulum, $I_p=0.830\ \mathrm{kg}\,\mathrm{m}^2$ and $\sum m_i r_i=0.750\ \mathrm{kg}\,\mathrm{m}$. Using $g=9.81\ \mathrm{m}/\mathrm{s}^2$, what is its small-angle period to two significant figures?
options:
- id: a
  content: |-
    $2.1\ \mathrm{s}$
  correct: true
  feedback: |-
    A composite pendulum's period compares pivot-axis inertia with its gravitational restoring-torque coefficient: $T=2\pi\sqrt{I_p/(g\sum m_i r_i)}$. Substitution gives $2.110\ldots\ \mathrm{s}$, which is $2.1\ \mathrm{s}$ to two significant figures.
- id: b
  content: |-
    $0.34\ \mathrm{s}$
  feedback: |-
    This stops after evaluating $\sqrt{I_p/(g\sum m_i r_i)}=0.336\ldots\ \mathrm{s}$. That quantity is the period divided by $2\pi$; including the required prefactor gives $T=2.1\ \mathrm{s}$.
- id: c
  content: |-
    $7.4\ \mathrm{s}$
  feedback: |-
    This reports $g\sum m_i r_i=9.81(0.750)=7.36$, the restoring-torque coefficient, as though it were a time. The period requires its ratio with inertia inside a square root, giving $2.1\ \mathrm{s}$.
- id: d
  content: |-
    $13\ \mathrm{s}$
  feedback: |-
    This is approximately the correct period multiplied by another factor of $2\pi$. The square-root time is multiplied by $2\pi$ only once, so the period is $2.1\ \mathrm{s}$, not about $13\ \mathrm{s}$.
```

---

<a id="apply-the-method-to-the-given-pendulum"></a>
## Apply the Method to the Given Pendulum

**Example:** Use the two-ledger method for the rod–disk pendulum shown.

![](<../Source/Images/rod-disk-pendulum.png>)

**Explanation**

The disk's center is at

$$
r_d=L+R=1.2+0.42=1.62\ \mathrm{m}.
$$

The inertia ledger is

$$
\begin{aligned}
I_p
&=\frac13(0.35)(1.2)^2
+\frac12(0.65)(0.42)^2
+(0.65)(1.62)^2\\
&=1.93119\ \mathrm{kg}\,\mathrm{m}^2.
\end{aligned}
$$

Its three contributions are $0.168$, $0.05733$, and $1.70586\ \mathrm{kg}\,\mathrm{m}^2$. Listing them separately makes it easier to catch a missing disk term.

The mass–distance ledger is

$$
\begin{aligned}
\sum m_i r_i
&=(0.35)\left(\frac{1.2}{2}\right)+(0.65)(1.62)\\
&=1.263\ \mathrm{kg}\,\mathrm{m}.
\end{aligned}
$$

Thus,

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{1.93119}{(9.81)(1.263)}}\\
&=2.4806\ldots\ \mathrm{s}\\
&=2.5\ \mathrm{s}
\quad\text{to two significant figures.}
\end{aligned}
$$

```quiz
type: radio
id: m4-2lec-q5
content: |-
  **Question 5**

  A physical pendulum consists of a uniform rod of mass $m_r$ and length $L$, with a solid disk of mass $m_d$ and radius $R$ attached at the rod's lower end. Find the small-angle period for $m_r=0.35\ \mathrm{kg}$, $m_d=0.65\ \mathrm{kg}$, $R=0.42\ \mathrm{m}$, and $L=1.2\ \mathrm{m}$.

  ![](<../Source/Images/rod-disk-pendulum.png>)

  Enter the period in seconds as a number only:
options:
- id: a
  content: 2.5
  correct: true
  feedback: |-
    The disk center is $L+R$ from the pivot, so include both its center-axis inertia and parallel-axis term in $I_p$. Using $I_p=\frac13m_rL^2+\frac12m_dR^2+m_d(L+R)^2$ and the restoring factor $g[m_rL/2+m_d(L+R)]$ gives $T=2.4806\ldots\ \mathrm{s}$, which rounds to the entry `2.5`.
- id: b
  content: 0.39
  feedback: |-
    This is the value of the square-root time factor before the angular cycle is converted to a full period. The physical-pendulum formula includes the prefactor $2\pi$, which changes $0.39\ldots\ \mathrm{s}$ to $2.5\ \mathrm{s}$.
- id: c
  content: 2.4
  feedback: |-
    This treats the disk as a point mass at its center by omitting its own rotational inertia $\frac12m_dR^2$. A solid disk has finite radius, so that term must be included; doing so raises the rounded period from `2.4` to `2.5`.
- id: d
  content: 2.2
  feedback: |-
    This places the disk's center at the rod's attachment point by using $L$ instead of $L+R$ in its inertia and torque terms. The center lies one radius farther from the pivot, and the corrected geometry gives `2.5` rather than `2.2`.
- id: e
  content: 0.85
  feedback: |-
    This includes the disk's spin about its center but omits the much larger inertia from carrying that center around the pivot. The parallel-axis term $m_d(L+R)^2$ is required; including it changes the result from about `0.85` to `2.5`.
```

---

<a id="summary"></a>
## Summary

For a rod–disk physical pendulum:

1. Locate the centers: $r_r=L/2$ and $r_d=L+R$.
2. Add pivot-axis inertias:

   - use an inertia formula unchanged if it is already about the pivot;
   - use $I_p=I_{\mathrm{cm}}+Md^2$ if the known formula is about a parallel center-of-mass axis.

   $$
   I_p
   =\frac13m_rL^2+\frac12m_dR^2+m_d(L+R)^2.
   $$

3. Add mass–distance terms:

   $$
   \sum m_i r_i=m_r\left(\frac{L}{2}\right)+m_d(L+R).
   $$

4. Substitute into

   $$
   T=2\pi\sqrt{\frac{I_p}{g\sum m_i r_i}}
   $$

   Check that the radical has units of $\mathrm{s}^2$, then round only the final period.

**Main trap:** use squared distances in the parallel-axis inertia terms, but first-power distances in the gravitational torque terms.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../../M5/2026-08-03-Q-3/Study-Guide.md)
Next: [Inferring Particle Motion From a Traveling-Wave Snapshot](../../../M5/2026-07-23-M5-1/Lessons/Problem-5.md)

Study guide index: 08/28

---
<!-- lesson-nav:end -->
