# Shifting a Moment of Inertia to a Parallel Axis

<!--
lesson-id: 212-M2-022
topic-code: MTH212.M2.22
-->

## Table of Contents

- [Introduction](#introduction)
- [Identify the Axis Separation](#identify-the-axis-separation)
- [Apply the Parallel-Axis Theorem](#apply-the-parallel-axis-theorem)
- [Avoid the Main Traps](#avoid-the-main-traps)
- [Check the Result](#check-the-result)
- [Summary](#summary)

## Prerequisites

- Recognize an axis through an object's center of mass.
- Interpret the radius as the center-to-rim distance.
- Square a symbolic distance and combine like terms.

---

<a id="introduction"></a>
## Introduction

When a problem gives the moment of inertia about an axis through the center of mass and asks about a **parallel** axis, use the parallel-axis theorem:

$$
I_{\text{new}}=I_{\text{cm}}+Md^2.
$$

Here, $d$ is the perpendicular distance between the two axes. Before substituting, check both conditions: the known axis passes through the center of mass, and the requested axis is parallel to it. Then identify $d$ from the geometry, square it, and add $Md^2$ to the known moment of inertia.

Because $Md^2\ge 0$, shifting away from the center-of-mass axis cannot make the moment of inertia smaller.

---

<a id="identify-the-axis-separation"></a>
## Identify the Axis Separation

**Example:** A uniform disk has radius $R$. One axis passes through its center and is perpendicular to the disk. A second, parallel axis passes through a point on the rim. Find the separation $d$ between the axes.

**Explanation**

Both axes pierce the plane of the disk. Their separation is therefore the distance in the plane from the center to the rim point. Translate the geometry before touching the theorem:

- reference axis: through the center;
- new axis: through the rim;
- center-to-rim distance: one radius.

Therefore,

$$
d=R.
$$

It is not $2R$: the diameter measures from one rim point through the center to the opposite rim, but the required distance starts at the center.

```quiz
type: radio
id: p6-axis-separation
content: |-
  A circular plate has radius $a$. Its center-of-mass axis is perpendicular to the plate through its center. A parallel axis passes through a point on the rim. What value of $d$ belongs in the parallel-axis theorem?
options:
- id: a
  content: |-
    $0$
- id: b
  content: |-
    $a$
  correct: true
- id: c
  content: |-
    $2a$
- id: d
  content: |-
    $a^2$
```

---

<a id="apply-the-parallel-axis-theorem"></a>
## Apply the Parallel-Axis Theorem

**Example:** A thin hoop of mass $M$ and radius $R$ has

$$
I_{\text{cm}}=MR^2
$$

about the axis through its center and perpendicular to its plane. Find its moment of inertia about a parallel axis through the rim.

**Explanation**

The new axis is one radius from the center axis, so $d=R$. Substitute both known expressions into the theorem:

$$
\begin{aligned}
I_{\text{rim}}
&=I_{\text{cm}}+Md^2\\
&=MR^2+M(R)^2\\
&=MR^2+MR^2\\
&=2MR^2.
\end{aligned}
$$

This models the full sequence: verify the axes are parallel, read $d=R$ from the geometry, substitute, and combine like terms. The disk question below changes only the supplied center-of-mass coefficient.

```quiz
type: radio
id: p6-original-disk
content: |-
  The moment of inertia of a uniform disk of mass $M$ and radius $R$, about an axis through its center and perpendicular to its plane, is $\dfrac{1}{2}MR^2$.

  What is the moment of inertia about a parallel axis passing through a point on the rim?
options:
- id: a
  content: |-
    $\dfrac{1}{4}MR^2$
- id: b
  content: |-
    $MR^2$
- id: c
  content: |-
    $\dfrac{3}{2}MR^2$
  correct: true
- id: d
  content: |-
    $2MR^2$
```

---

<a id="avoid-the-main-traps"></a>
## Avoid the Main Traps

**Example:** An object has $I_{\text{cm}}=kML^2$. Find its moment of inertia about a parallel axis a distance $L/2$ away.

**Explanation**

Use the separation itself for $d$, and square it inside the added term:

$$
\begin{aligned}
I_{\text{new}}
&=kML^2+M\left(\frac{L}{2}\right)^2\\
&=kML^2+\frac14ML^2\\
&=\left(k+\frac14\right)ML^2.
\end{aligned}
$$

Do not replace $I_{\text{cm}}$ with $Md^2$, and do not forget that the entire distance is squared.

```quiz
type: radio
id: p6-fractional-shift
content: |-
  A rigid object has $I_{\text{cm}}=\dfrac{2}{5}ML^2$. What is its moment of inertia about a parallel axis a distance $L/2$ from the center-of-mass axis?
options:
- id: a
  content: |-
    $\dfrac{1}{10}ML^2$
- id: b
  content: |-
    $\dfrac{1}{4}ML^2$
- id: c
  content: |-
    $\dfrac{13}{20}ML^2$
  correct: true
- id: d
  content: |-
    $\dfrac{9}{10}ML^2$
```

---

<a id="check-the-result"></a>
## Check the Result

**Example:** Decide whether $I_{\text{new}}=\frac14MR^2$ can be the result of shifting a disk away from a center-of-mass axis for which $I_{\text{cm}}=\frac12MR^2$.

**Explanation**

No. The parallel-axis theorem adds the nonnegative quantity $Md^2$:

$$
I_{\text{new}}-I_{\text{cm}}=Md^2\ge 0.
$$

For a genuine shift with $d>0$, the new moment of inertia must be strictly greater than $I_{\text{cm}}$. Units provide another check: both $I_{\text{cm}}$ and $Md^2$ have units of mass times length squared.

```quiz
type: radio
id: p6-magnitude-check
content: |-
  An object's moment of inertia about its center-of-mass axis is $6\,\mathrm{kg\,m^2}$. Which value could be its moment of inertia about a distinct parallel axis?
options:
- id: a
  content: |-
    $2\,\mathrm{kg\,m^2}$
- id: b
  content: |-
    $5\,\mathrm{kg\,m^2}$
- id: c
  content: |-
    $6\,\mathrm{kg\,m^2}$
- id: d
  content: |-
    $9\,\mathrm{kg\,m^2}$
  correct: true
```

---

<a id="summary"></a>
## Summary

When the requested axis is parallel to a known center-of-mass axis:

1. Verify that the known axis passes through the center of mass and the new axis is parallel to it.
2. Find the perpendicular separation $d$ between the axes.
3. Use $I_{\text{new}}=I_{\text{cm}}+Md^2$.
4. Square the full distance before simplifying.
5. Check that the answer has units of mass times length squared and is no smaller than $I_{\text{cm}}$.

For a disk shifted from its central perpendicular axis to a parallel axis through the rim, $d=R$, not $2R$. Thus

$$
I_{\text{rim}}=\frac12MR^2+MR^2=\frac32MR^2.
$$

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
