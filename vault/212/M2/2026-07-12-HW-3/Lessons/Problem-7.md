# Comparing Rotational Kinetic Energies About Parallel Axes

<!--
lesson-id: 212-M2-023
topic-code: MTH212.M2.23
-->

## Table of Contents

- [Introduction](#introduction)
- [Cancel the Shared Angular-Speed Factor](#cancel-the-shared-angular-speed-factor)
- [Shift One Disk's Moment of Inertia](#shift-one-disks-moment-of-inertia)
- [Add the Two Disks About One Axis](#add-the-two-disks-about-one-axis)
- [Compare the Contact and Center Axes](#compare-the-contact-and-center-axes)
- [Summary](#summary)

## Prerequisites

- Rotational kinetic energy: $K=\frac12 I\omega^2$
- A uniform disk about its central perpendicular axis: $I_{\mathrm{cm}}=\frac12 MR^2$
- The parallel-axis theorem: $I=I_{\mathrm{cm}}+Md^2$
- The centers of two identical tangent disks are $2R$ apart

---

<a id="introduction"></a>
## Introduction

When the same rigid system spins at the same angular speed about two different parallel axes, the only changing factor in $K=\frac12 I\omega^2$ is the moment of inertia. The task is therefore to compute the system's total moment of inertia about each axis and take the ratio in the requested order.

Read ratio notation from left to right: in $K_Q/K_P$, the $Q$ quantity goes on top and the $P$ quantity goes on the bottom. After canceling the shared factors, that order stays the same:

$$
\frac{K_Q}{K_P}=\frac{I_Q}{I_P}.
$$

For a composite object, treat each piece separately. Measure each piece's own center-of-mass distance $d$ from the chosen axis, apply $I=I_{\mathrm{cm}}+Md^2$, and then add the results.

---

<a id="cancel-the-shared-angular-speed-factor"></a>
## Cancel the Shared Angular-Speed Factor

**Example:** A rigid body has moments of inertia $I_A=2mL^2$ and $I_B=5mL^2$ about two axes. It spins about either axis at the same angular speed. Find $K_B/K_A$.

**Explanation**

Write the ratio before substituting:

$$
\frac{K_B}{K_A}
=\frac{\frac12 I_B\omega^2}{\frac12 I_A\omega^2}
=\frac{I_B}{I_A}.
$$

The common factors $\frac12$ and $\omega^2$ cancel because they have the same values in both trials, so

$$
\frac{K_B}{K_A}=\frac{5mL^2}{2mL^2}=\frac52.
$$

```quiz
type: radio
id: p7-same-speed-ratio
content: |-
  A body has $I_C=3mL^2$ and $I_D=7mL^2$. It spins about either axis at the same angular speed. What is $K_D/K_C$?
options:
- id: a
  content: |-
    $\dfrac{7}{3}$
  correct: true
- id: b
  content: |-
    $\dfrac{3}{7}$
- id: c
  content: |-
    $\dfrac{49}{9}$
- id: d
  content: |-
    $\dfrac{7}{6}$
- id: e
  content: |-
    $1$
```

---

<a id="shift-one-disks-moment-of-inertia"></a>
## Shift One Disk's Moment of Inertia

**Example:** Find the moment of inertia of a uniform disk about an axis perpendicular to the disk and a distance $2R$ from its center.

**Explanation**

The central moment of inertia is $\frac12 MR^2$. The parallel-axis distance $d$ is measured from the disk's center of mass to the new axis. Here $d=2R$, so

$$
I=\frac12 MR^2+M(2R)^2
=\frac12 MR^2+4MR^2
=\frac92 MR^2.
$$

Square the entire distance. The shift term is $M(2R)^2$, not $M(2R)$ and not $2MR^2$.

```quiz
type: radio
id: p7-shift-one-disk
content: |-
  A uniform disk has mass $M$ and radius $R$. What is its moment of inertia about a perpendicular axis a distance $R$ from its center?
options:
- id: a
  content: |-
    $\dfrac12 MR^2$
- id: b
  content: |-
    $MR^2$
- id: c
  content: |-
    $\dfrac32 MR^2$
  correct: true
- id: d
  content: |-
    $2MR^2$
- id: e
  content: |-
    $\dfrac52 MR^2$
```

---

<a id="add-the-two-disks-about-one-axis"></a>
## Add the Two Disks About One Axis

**Example:** Two identical uniform disks are tangent. Find their total moment of inertia about an axis through their contact point and perpendicular to the disks.

**Explanation**

Each disk's center is a distance $R$ from the contact axis. Therefore, each disk contributes

$$
I_{\text{one disk}}
=\frac12 MR^2+M(R)^2
=\frac32 MR^2.
$$

Add both contributions:

$$
I_{\text{contact}}
=2\left(\frac32 MR^2\right)
=3MR^2.
$$

```quiz
type: radio
id: p7-two-disk-center-axis
content: |-
  Two identical uniform disks of mass $M$ and radius $R$ are tangent. An axis passes through the center of the left disk and is perpendicular to both disks. What is the total moment of inertia?
options:
- id: a
  content: |-
    $MR^2$
- id: b
  content: |-
    $3MR^2$
- id: c
  content: |-
    $4MR^2$
- id: d
  content: |-
    $5MR^2$
  correct: true
- id: e
  content: |-
    $6MR^2$
```

The left disk contributes $\frac12 MR^2$. The right disk's center is $2R$ from the axis, so it contributes $\frac12 MR^2+M(2R)^2=\frac92 MR^2$. Their sum is $5MR^2$.

---

<a id="compare-the-contact-and-center-axes"></a>
## Compare the Contact and Center Axes

**Example:** Two identical uniform disks, each with mass $M$ and radius $R$, are joined at contact point $P$. Point $Q$ is the center of the left disk. The system spins at angular speed $\omega$ first about a perpendicular axis through $P$ and then about a parallel axis through $Q$. Find $K_Q/K_P$.

![](<../Source/2026-07-12-HW-3/Images/two-disks-rotation-axes.png>)

**Explanation**

Organize the center-to-axis distances before using the parallel-axis theorem:

| Chosen axis | Left disk's $d$ | Right disk's $d$ |
|---|---:|---:|
| Through $P$ | $R$ | $R$ |
| Through $Q$ | $0$ | $2R$ |

Each entry is measured from the center of the individual disk to the chosen axis.

About $P$, both disk centers are a distance $R$ from the axis:

$$
I_P=2\left(\frac12 MR^2+MR^2\right)=3MR^2.
$$

About $Q$, the left disk has $d=0$ and the right disk has $d=2R$:

$$
\begin{aligned}
I_Q
&=\frac12 MR^2+\left(\frac12 MR^2+M(2R)^2\right)\\
&=\frac12 MR^2+\frac92 MR^2\\
&=5MR^2.
\end{aligned}
$$

Because the angular speed is the same,

$$
\boxed{\frac{K_Q}{K_P}=\frac{I_Q}{I_P}=\frac{5MR^2}{3MR^2}=\frac53}.
$$

The essential distance check is $(R,R)$ about $P$ but $(0,2R)$ about $Q$.

```quiz
type: radio
id: p7-reverse-ratio
content: |-
  For the same two-disk system and axes, what is $K_P/K_Q$ if the angular speed is unchanged?
options:
- id: a
  content: |-
    $\dfrac35$
  correct: true
- id: b
  content: |-
    $\dfrac53$
- id: c
  content: |-
    $\dfrac59$
- id: d
  content: |-
    $\dfrac95$
- id: e
  content: |-
    $1$
```

---

<a id="summary"></a>
## Summary

When the system and angular speed are unchanged, use this checklist:

1. Copy the requested order, then reduce the energy ratio to a moment-of-inertia ratio: $K_B/K_A=I_B/I_A$.
2. For each component and each axis, identify the distance $d$ from that component's center of mass.
3. Apply $I=I_{\mathrm{cm}}+Md^2$ to each component.
4. Add the component moments of inertia about the same axis.
5. Form the ratio in the requested order.

The main trap is using one distance for the whole composite object. About the center axis of one disk, the two center distances are $0$ and $2R$, and the distance must be squared in the parallel-axis term.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
