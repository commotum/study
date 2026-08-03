# Finding the Period of a Rod–Disk Physical Pendulum

<!--
lesson-id: 212-M4-015
topic-code: MTH212.M4.15
-->

## Table of Contents

- [Introduction](#introduction)
- [Locate Each Center of Mass](#locate-each-center-of-mass)
- [Build the Total Moment of Inertia](#build-the-total-moment-of-inertia)
- [Build the Gravitational Torque Factor](#build-the-gravitational-torque-factor)
- [Assemble and Evaluate the Period](#assemble-and-evaluate-the-period)
- [Apply the Method to the Given Pendulum](#apply-the-method-to-the-given-pendulum)
- [Summary](#summary)

## Prerequisites

- Use the parallel-axis theorem $I=I_{\mathrm{cm}}+Md^2$.
- Know $I_{\mathrm{rod,end}}=\frac13mL^2$ and $I_{\mathrm{disk,cm}}=\frac12mr^2$.
- Substitute several quantities into a fraction containing a square root.

---

<a id="introduction"></a>
## Introduction

For a rigid physical pendulum making small oscillations,

$$
T=2\pi\sqrt{\frac{I_{\mathrm{pivot}}}{Mg\,d_{\mathrm{cm}}}}.
$$

For a composite object, it is usually safer not to calculate the combined center of mass first. Instead, build two sums:

$$
T=2\pi\sqrt{
\frac{\sum I_{\mathrm{pivot},i}}
{g\sum m_i d_i}
}.
$$

- The numerator is a sum of **moments of inertia about the pivot**.
- The denominator contains a sum of **mass times distance from the pivot**.

For a rod of length $L$ with a disk of radius $r$ attached tangentially at its lower end, the rod's center is at $L/2$ and the disk's center is at $L+r$.

| Component | Pivot distance $d_i$ | Contribution to $I_{\mathrm{pivot}}$ | Contribution to $\sum m_i d_i$ |
|---|---:|---:|---:|
| Uniform rod | $L/2$ | $\frac13m_rL^2$ | $m_r(L/2)$ |
| Solid disk | $L+r$ | $\frac12m_dr^2+m_d(L+r)^2$ | $m_d(L+r)$ |

Read each row as a translation from the object in the diagram to the two algebraic terms it contributes.

---

<a id="locate-each-center-of-mass"></a>
## Locate Each Center of Mass

**Example:** A uniform rod of length $0.90\ \mathrm{m}$ hangs from a pivot at its upper end. A disk of radius $0.20\ \mathrm{m}$ is attached at the rod's lower end as shown. How far is each center of mass from the pivot?

**Explanation**

The rod's center of mass is halfway along the rod:

$$
d_r=\frac{L}{2}=0.45\ \mathrm{m}.
$$

The rod reaches the nearest edge of the disk. The disk's center is one additional radius below that point:

$$
d_d=L+r=0.90+0.20=1.10\ \mathrm{m}.
$$

**Watch Out!** The disk's center is not at $L$. The length $L$ reaches only the disk's edge.

```quiz
type: radio
id: problem-6-distance-q1
content: |-
  A rod of length $L$ is pivoted at its upper end, and a disk of radius $r$ is attached tangentially at the rod's lower end. What is the distance from the pivot to the disk's center?
options:
- id: a
  content: |-
    $L+r$
  correct: true
  feedback: |-
    The rod reaches the disk's edge, and one more radius reaches the disk's center.
- id: b
  content: |-
    $L$
  feedback: |-
    This reaches the attachment point at the disk's edge, not the disk's center.
- id: c
  content: |-
    $L-r$
  feedback: |-
    The disk's center lies beyond the rod's lower end, so the radius must be added.
- id: d
  content: |-
    $\dfrac{L+r}{2}$
  feedback: |-
    Averaging the two lengths does not locate the disk's center relative to the pivot.
```

---

<a id="build-the-total-moment-of-inertia"></a>
## Build the Total Moment of Inertia

**Example:** Write the total moment of inertia about the pivot for the rod–disk pendulum.

**Explanation**

The rod is already described by its moment of inertia about one end:

$$
I_r=\frac13m_rL^2.
$$

The disk's known formula is about its own center. Move that axis to the pendulum pivot with the parallel-axis theorem, using $d_d=L+r$:

$$
I_d
=I_{\mathrm{disk,cm}}+m_dd_d^2
=\frac12m_dr^2+m_d(L+r)^2.
$$

Therefore,

$$
I_{\mathrm{pivot}}
=\frac13m_rL^2+\frac12m_dr^2+m_d(L+r)^2.
$$

```quiz
type: radio
id: problem-6-inertia-q1
content: |-
  Which expression is the total pivot-axis moment of inertia of the rod–disk pendulum?
options:
- id: a
  content: |-
    $\dfrac13m_rL^2+\dfrac12m_dr^2+m_d(L+r)^2$
  correct: true
  feedback: |-
    Add the rod's end-axis inertia to both the disk's center-axis inertia and its parallel-axis term.
- id: b
  content: |-
    $\dfrac13m_rL^2+\dfrac12m_dr^2$
  feedback: |-
    This omits the disk's parallel-axis term $m_d(L+r)^2$.
- id: c
  content: |-
    $\dfrac13m_rL^2+m_d(L+r)^2$
  feedback: |-
    Treating the disk only as a point mass omits its own center-axis inertia $\frac12m_dr^2$.
- id: d
  content: |-
    $\dfrac13m_rL^2+\dfrac12m_dr^2+m_d(L-r)^2$
  feedback: |-
    The disk's center is $L+r$ from the pivot, not $L-r$.
```

---

<a id="build-the-gravitational-torque-factor"></a>
## Build the Gravitational Torque Factor

**Example:** Write the small-angle restoring-torque factor for the same rod and disk.

**Explanation**

Each component contributes its weight times the distance from the pivot to its own center of mass:

$$
g\sum m_i d_i
=g\left[m_r\left(\frac{L}{2}\right)+m_d(L+r)\right].
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
    $g\left[m_r\left(\dfrac{L}{2}\right)+m_d(L+r)\right]$
  correct: true
  feedback: |-
    Each component contributes $mg$ times the distance from the pivot to that component's center of mass.
- id: b
  content: |-
    $g\left[m_rL+m_d(L+r)\right]$
  feedback: |-
    The uniform rod's center of mass is at $L/2$, not at its lower end.
- id: c
  content: |-
    $g\left[m_r\left(\dfrac{L}{2}\right)^2+m_d(L+r)^2\right]$
  feedback: |-
    Squared distances belong in parallel-axis inertia terms, not in the gravitational torque factor.
- id: d
  content: |-
    $g(m_r+m_d)(L+r)$
  feedback: |-
    The rod and disk have different center-of-mass distances and must contribute separate terms.
```

---

<a id="assemble-and-evaluate-the-period"></a>
## Assemble and Evaluate the Period

**Example:** Find the small-angle period for $m_r=0.30\ \mathrm{kg}$, $m_d=0.50\ \mathrm{kg}$, $L=1.0\ \mathrm{m}$, and $r=0.20\ \mathrm{m}$.

**Explanation**

Evaluate the two ledgers separately:

$$
\begin{aligned}
I_{\mathrm{pivot}}
&=\frac13(0.30)(1.0)^2
+\frac12(0.50)(0.20)^2
+(0.50)(1.0+0.20)^2\\
&=0.830\ \mathrm{kg\,m^2},
\end{aligned}
$$

and

$$
\begin{aligned}
\sum m_i d_i
&=(0.30)\left(\frac{1.0}{2}\right)
+(0.50)(1.0+0.20)\\
&=0.750\ \mathrm{kg\,m}.
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
\frac{\mathrm{kg\,m^2}}
{(\mathrm{m/s^2})(\mathrm{kg\,m})}
=\mathrm{s^2}.
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
  For a composite physical pendulum, $I_{\mathrm{pivot}}=0.830\ \mathrm{kg\,m^2}$ and $\sum m_i d_i=0.750\ \mathrm{kg\,m}$. Using $g=9.81\ \mathrm{m/s^2}$, what is its small-angle period to two significant figures?
options:
- id: a
  content: |-
    $2.1\ \mathrm{s}$
  correct: true
  feedback: |-
    $T=2\pi\sqrt{0.830/[9.81(0.750)]}=2.110\ldots\ \mathrm{s}$, which rounds to $2.1\ \mathrm{s}$.
- id: b
  content: |-
    $0.34\ \mathrm{s}$
  feedback: |-
    This is the square-root factor before multiplying by $2\pi$.
- id: c
  content: |-
    $7.4\ \mathrm{s}$
  feedback: |-
    This is the numerical size of $g\sum m_id_i$, not the period.
- id: d
  content: |-
    $13\ \mathrm{s}$
  feedback: |-
    This effectively multiplies by $2\pi$ twice.
```

---

<a id="apply-the-method-to-the-given-pendulum"></a>
## Apply the Method to the Given Pendulum

**Example:** Use the two-ledger method for the rod–disk pendulum shown.

![](<../Source/Images/rod-disk-pendulum.png>)

**Explanation**

The disk's center is at

$$
d_d=L+r=1.2+0.42=1.62\ \mathrm{m}.
$$

The inertia ledger is

$$
\begin{aligned}
I_{\mathrm{pivot}}
&=\frac13(0.35)(1.2)^2
+\frac12(0.65)(0.42)^2
+(0.65)(1.62)^2\\
&=1.93119\ \mathrm{kg\,m^2}.
\end{aligned}
$$

Its three contributions are $0.168$, $0.05733$, and $1.70586\ \mathrm{kg\,m^2}$. Listing them separately makes it easier to catch a missing disk term.

The mass–distance ledger is

$$
\begin{aligned}
\sum m_i d_i
&=(0.35)\left(\frac{1.2}{2}\right)+(0.65)(1.62)\\
&=1.263\ \mathrm{kg\,m}.
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

  A physical pendulum consists of a uniform rod of mass $m_r$ and length $L$, with a solid disk of mass $m_d$ and radius $r$ attached at the rod's lower end. Find the small-angle period for $m_r=0.35\ \mathrm{kg}$, $m_d=0.65\ \mathrm{kg}$, $r=0.42\ \mathrm{m}$, and $L=1.2\ \mathrm{m}$.

  ![](<../Source/Images/rod-disk-pendulum.png>)

  Enter the period in seconds as a number only:
options:
- id: a
  content: 2.5
  correct: true
  feedback: |-
    The disk's center is a distance $L+r$ from the pivot. The total moment of inertia is

    $$
    I=\frac13m_rL^2+\frac12m_dr^2+m_d(L+r)^2.
    $$

    The gravitational torque factor is $g[m_r(L/2)+m_d(L+r)]$, so

    $$
    T=2\pi\sqrt{\frac{\frac13m_rL^2+\frac12m_dr^2+m_d(L+r)^2}{g[m_r(L/2)+m_d(L+r)]}}
    =2.4806\ldots\ \mathrm{s}.
    $$

    The measured givens have two significant figures, so $T=2.5\ \mathrm{s}$.
- id: b
  content: 0.39
  feedback: |-
    This omits the leading factor $2\pi$ from the period formula.
- id: c
  content: 2.4
  feedback: |-
    This is close to the result obtained by omitting the disk's center-axis inertia $\frac12m_dr^2$.
- id: d
  content: 2.2
  feedback: |-
    This is close to the result obtained by using $L$ instead of $L+r$ for the disk's center distance.
- id: e
  content: 0.85
  feedback: |-
    This is close to the result obtained by omitting the disk's parallel-axis term $m_d(L+r)^2$.
```

---

<a id="summary"></a>
## Summary

For a rod–disk physical pendulum:

1. Locate the centers: $d_r=L/2$ and $d_d=L+r$.
2. Add pivot-axis inertias:

   $$
   I_{\mathrm{pivot}}
   =\frac13m_rL^2+\frac12m_dr^2+m_d(L+r)^2.
   $$

3. Add mass–distance terms:

   $$
   \sum m_id_i=m_r\left(\frac{L}{2}\right)+m_d(L+r).
   $$

4. Substitute into

   $$
   T=2\pi\sqrt{\frac{I_{\mathrm{pivot}}}{g\sum m_id_i}}
   $$

   Check that the radical has units of $\mathrm{s^2}$, then round only the final period.

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
