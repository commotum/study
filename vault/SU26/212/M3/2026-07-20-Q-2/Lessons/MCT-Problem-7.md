# Shift a Known Center-of-Mass Inertia to a Parallel Axis

<!--
lesson-id: 212-M3-043
topic-code: MTH212.M3.43
-->

## Table of Contents

- [Introduction](#introduction)
- [Shift the Two-Block System](#shift-the-two-block-system)
- [Separate the Theorem Conditions from Symmetry](#separate-the-theorem-conditions-from-symmetry)
- [Use the Total Mass of the Four-Block System](#use-the-total-mass-of-the-four-block-system)
- [Move a Uniform Rod's Axis](#move-a-uniform-rods-axis)
- [Summary](#summary)

## Prerequisites

- Identify the rotation axis and perpendicular distances from it.
- Use $I=\sum_i m_i r_{\perp,i}^2$ for point masses.
- Recognize $I_{\mathrm{cm}}=\frac{1}{12}ML^2$ for a uniform thin rod about a perpendicular axis through its center.
- Add fractions and check units of $\mathrm{kg\,m^2}$.

---

<a id="introduction"></a>
## Introduction

When the same rigid body rotates about a new axis parallel to a known axis through its center of mass, use the parallel-axis theorem:

$$
\boxed{I_{\mathrm{new}}=I_{\mathrm{cm}}+M_{\mathrm{total}}d^2}.
$$

Here $d$ is the perpendicular distance between the axes, and $M_{\mathrm{total}}$ is the mass of the entire rigid body. If parallel-axis locations are measured from one reference line, compute

$$
d=\left|x_{\mathrm{new}}-x_{\mathrm{cm}}\right|.
$$

Before substituting, verify all three conditions:

1. The known inertia is about an axis through the center of mass.
2. The new axis is parallel to that center-of-mass axis.
3. Both inertias describe the same rigid mass distribution, shifted as one body without changing shape.

Then measure $d$, square it, use the total mass, and add the shift term to $I_{\mathrm{cm}}$. The quick check is

$$
I_{\mathrm{new}}-I_{\mathrm{cm}}=M_{\mathrm{total}}d^2\ge0.
$$

For a genuine shift with $d>0$, the new inertia must be larger. Symmetry and identical component masses are not required.

The units also expose a missing square:

$$
[M_{\mathrm{total}}d^2]=\mathrm{kg\,m^2},
$$

which matches the units of moment of inertia. The expression $Md$ would have units of $\mathrm{kg\,m}$ and cannot be added to $I_{\mathrm{cm}}$.

---

<a id="shift-the-two-block-system"></a>
## Shift the Two-Block System

**Source-video worked check (`JrkimXqnCLw`, 00:02:45–00:04:17):** Two $10\,\mathrm{kg}$ point masses are $10\,\mathrm m$ apart. About the center-of-mass axis, each mass is $5\,\mathrm m$ away, so

$$
I_{\mathrm{cm}}
=10(5)^2+10(5)^2
=500\,\mathrm{kg\,m^2}.
$$

Move the parallel axis $5\,\mathrm m$ so that it passes through the left mass.

**Explanation**

The body has total mass

$$
M_{\mathrm{total}}=10+10=20\,\mathrm{kg},
$$

and the separation between the old and new axes is $d=5\,\mathrm m$. Therefore,

$$
\begin{aligned}
I_{\mathrm{new}}
&=I_{\mathrm{cm}}+M_{\mathrm{total}}d^2\\
&=500+20(5)^2\\
&=\boxed{1000\,\mathrm{kg\,m^2}}.
\end{aligned}
$$

The direct calculation gives the same result. Relative to the new axis, the masses are at distances $0$ and $10\,\mathrm m$:

$$
I_{\mathrm{direct}}=10(0)^2+10(10)^2=1000\,\mathrm{kg\,m^2}.
$$

This comparison fixes the roles in the theorem: $I_{\mathrm{cm}}$ is retained, $20\,\mathrm{kg}$ is the whole-body mass, and $5\,\mathrm m$ is the distance between axes—not the distance of every mass from the new axis.

```quiz
type: radio
id: mct-p7-two-block-mirrored
shuffle: true
content: |-
  A rigid assembly consists of four $3.0\,\mathrm{kg}$ pieces, so its total mass is $12\,\mathrm{kg}$. Its moment of inertia about a parallel center-of-mass axis is $240\,\mathrm{kg\,m^2}$. What is its moment of inertia about an axis $3.0\,\mathrm m$ away?
options:
- id: mct-p7-two-block-mirrored-a
  content: |-
    $348\,\mathrm{kg\,m^2}$
  correct: true
  feedback: |-
    For parallel axes with the known axis through the center of mass, add $M_{\mathrm{total}}d^2$. Here $I_{\mathrm{new}}=240+(12)(3.0)^2=240+108=348\,\mathrm{kg\,m^2}$, which is larger than $I_{\mathrm{cm}}$ as required.
- id: mct-p7-two-block-mirrored-b
  content: |-
    $267\,\mathrm{kg\,m^2}$
  feedback: |-
    This uses the $3.0\,\mathrm{kg}$ mass of one piece in the shift term. The theorem shifts the inertia of the entire assembly, so use $M_{\mathrm{total}}=4(3.0)=12\,\mathrm{kg}$, giving $348\,\mathrm{kg\,m^2}$.
- id: mct-p7-two-block-mirrored-c
  content: |-
    $276\,\mathrm{kg\,m^2}$
  feedback: |-
    This adds $M_{\mathrm{total}}d$ instead of $M_{\mathrm{total}}d^2$. Axis separation enters as a squared distance, so the added term is $(12)(3.0)^2=108\,\mathrm{kg\,m^2}$.
- id: mct-p7-two-block-mirrored-d
  content: |-
    $108\,\mathrm{kg\,m^2}$
  feedback: |-
    This is only the shift term $M_{\mathrm{total}}d^2$. The theorem adds that term to the known $I_{\mathrm{cm}}=240\,\mathrm{kg\,m^2}$, producing $348\,\mathrm{kg\,m^2}$.
- id: mct-p7-two-block-mirrored-e
  content: |-
    $240\,\mathrm{kg\,m^2}$
  feedback: |-
    A nonzero parallel shift changes every mass element's squared distance in the combined inertia. Since $d=3.0\,\mathrm m>0$, the shift adds $108\,\mathrm{kg\,m^2}$; the inertia cannot remain at its center-of-mass value.
```

---

<a id="separate-the-theorem-conditions-from-symmetry"></a>
## Separate the Theorem Conditions from Symmetry

**Source correction (`JrkimXqnCLw`, about 00:03:21–00:03:29):** The transcript says that the system must be symmetric and its masses identical. That claim is false. The theorem applies to an asymmetric rigid body with unequal component masses as long as the known axis passes through the center of mass and the new axis is parallel to it.

**Explanation**

Choose the $x$-direction along the shortest line between two parallel axes. Let each mass have signed coordinate $x_i$ relative to the center-of-mass axis. Shifting the axis by $d$ gives

$$
\begin{aligned}
I_{\mathrm{new}}
&=\sum_i m_i\left[(x_i-d)^2+y_i^2\right]\\
&=I_{\mathrm{cm}}-2d\sum_i m_i x_i+d^2\sum_i m_i.
\end{aligned}
$$

The center-of-mass condition makes $\sum_i m_i x_i=0$, whether or not the body is symmetric. Thus the cross term vanishes and

$$
I_{\mathrm{new}}=I_{\mathrm{cm}}+M_{\mathrm{total}}d^2.
$$

**Controlled unequal-mass check:** Put $2\,\mathrm{kg}$ at $x=-3\,\mathrm m$ and $6\,\mathrm{kg}$ at $x=1\,\mathrm m$. Their center of mass is at the origin because $2(-3)+6(1)=0$. About that axis,

$$
I_{\mathrm{cm}}=2(3)^2+6(1)^2=24\,\mathrm{kg\,m^2}.
$$

For a parallel axis at $x=2\,\mathrm m$, $d=2\,\mathrm m$ and $M_{\mathrm{total}}=8\,\mathrm{kg}$, so

$$
I_{\mathrm{new}}=24+8(2)^2=56\,\mathrm{kg\,m^2}.
$$

The direct distances are $5$ and $1\,\mathrm m$, giving $2(5)^2+6(1)^2=56\,\mathrm{kg\,m^2}$. Unequal masses do not obstruct the theorem.

```quiz
type: radio
id: mct-p7-theorem-conditions
shuffle: true
content: |-
  In which situation can $I_{\mathrm{new}}=I_{\mathrm{cm}}+M_{\mathrm{total}}d^2$ be applied directly?
options:
- id: mct-p7-theorem-conditions-a
  content: |-
    An asymmetric rigid plate has known inertia about a vertical axis through its center of mass; the requested vertical axis is $0.30\,\mathrm m$ away.
  correct: true
  feedback: |-
    The same rigid body is used, the known axis passes through its center of mass, and the new axis is parallel. The plate need not be symmetric; use its total mass and $d=0.30\,\mathrm m$.
- id: mct-p7-theorem-conditions-b
  content: |-
    A rigid plate has known inertia about an offset vertical axis, but its center-of-mass-axis inertia is unknown; a second vertical axis is requested.
  feedback: |-
    Parallel axes alone are not enough for this direct form: the starting value must be $I_{\mathrm{cm}}$. An inertia about an arbitrary offset axis cannot simply be relabeled as $I_{\mathrm{cm}}$ and increased by another $Md^2$.
- id: mct-p7-theorem-conditions-c
  content: |-
    A rigid plate has known inertia about a vertical center-of-mass axis; the requested axis is horizontal.
  feedback: |-
    The requested axis is perpendicular rather than parallel to the known axis. Changing axis direction changes how mass is distributed around it, so the parallel-axis theorem in this form does not apply.
- id: mct-p7-theorem-conditions-d
  content: |-
    A multipart rigid body meets the axis conditions, but $M$ is taken as the mass of only the nearest component.
  feedback: |-
    The axis conditions are suitable, but the mass in $Md^2$ must be the total mass of the same body whose $I_{\mathrm{cm}}$ is known. Using one component's mass undercounts the shift.
- id: mct-p7-theorem-conditions-e
  content: |-
    A body changes shape after its center-of-mass inertia is measured, and the new shape rotates about a displaced parallel axis.
  feedback: |-
    A shape change alters the underlying mass distribution, so the old $I_{\mathrm{cm}}$ and the requested inertia do not describe the same rigid body. Recalculate the new shape's center-of-mass inertia before applying any axis shift.
```

---

<a id="use-the-total-mass-of-the-four-block-system"></a>
## Use the Total Mass of the Four-Block System

**Source-video worked check (`JrkimXqnCLw`, 00:07:45–00:08:41):** Four $4\,\mathrm{kg}$ blocks are each $5\,\mathrm m$ from the center-of-mass axis. Their known inertia is

$$
I_{\mathrm{cm}}=4\left[4(5)^2\right]=400\,\mathrm{kg\,m^2}.
$$

The new parallel axis is shifted $9\,\mathrm m$.

**Explanation**

Use all four blocks in the total mass:

$$
M_{\mathrm{total}}=4+4+4+4=16\,\mathrm{kg}.
$$

Then

$$
\begin{aligned}
I_{\mathrm{new}}
&=400+16(9)^2\\
&=400+1296\\
&=\boxed{1696\,\mathrm{kg\,m^2}}.
\end{aligned}
$$

The direct calculation again agrees. After the shift, two blocks are $4\,\mathrm m$ from the new axis and two are $14\,\mathrm m$ away:

$$
I_{\mathrm{direct}}
=2(4)(4)^2+2(4)(14)^2
=128+1568
=1696\,\mathrm{kg\,m^2}.
$$

**Caption clarification:** The automatic captions say “five minutes” once and later render the $14\,\mathrm m$ distance as “40 meters.” The preceding geometry gives $5\,\mathrm m$ from the center axis and a $9\,\mathrm m$ shift, so the new distances are $|9-5|=4\,\mathrm m$ and $9+5=14\,\mathrm m$; the arithmetic then uses $14^2$.

```quiz
type: radio
id: mct-p7-four-block-controlled
shuffle: true
content: |-
  A rigid assembly contains five $2.0\,\mathrm{kg}$ pieces and has $I_{\mathrm{cm}}=80\,\mathrm{kg\,m^2}$. What is its inertia about a parallel axis $3.0\,\mathrm m$ from the center-of-mass axis?
options:
- id: mct-p7-four-block-controlled-a
  content: |-
    $170\,\mathrm{kg\,m^2}$
  correct: true
  feedback: |-
    The shift uses the full $10\,\mathrm{kg}$ assembly: $I_{\mathrm{new}}=80+(10)(3.0)^2=80+90=170\,\mathrm{kg\,m^2}$. The positive shift term makes the result exceed $I_{\mathrm{cm}}$.
- id: mct-p7-four-block-controlled-b
  content: |-
    $98\,\mathrm{kg\,m^2}$
  feedback: |-
    This uses one piece's $2.0\,\mathrm{kg}$ mass in $Md^2$. All five pieces belong to the known $I_{\mathrm{cm}}$, so $M_{\mathrm{total}}=10\,\mathrm{kg}$ and the result is $170\,\mathrm{kg\,m^2}$.
- id: mct-p7-four-block-controlled-c
  content: |-
    $110\,\mathrm{kg\,m^2}$
  feedback: |-
    This adds $M_{\mathrm{total}}d=(10)(3.0)$ instead of squaring the axis separation. The correct shift term is $(10)(3.0)^2=90\,\mathrm{kg\,m^2}$.
- id: mct-p7-four-block-controlled-d
  content: |-
    $90\,\mathrm{kg\,m^2}$
  feedback: |-
    This keeps only $M_{\mathrm{total}}d^2$. That is the increase in inertia, not the new total; add it to $I_{\mathrm{cm}}=80\,\mathrm{kg\,m^2}$ to obtain $170\,\mathrm{kg\,m^2}$.
- id: mct-p7-four-block-controlled-e
  content: |-
    $80\,\mathrm{kg\,m^2}$
  feedback: |-
    The center-of-mass value is the minimum among axes parallel to it. Because the new axis is $3.0\,\mathrm m$ away, the inertia increases by $90\,\mathrm{kg\,m^2}$ rather than staying at $80\,\mathrm{kg\,m^2}$.
```

---

<a id="move-a-uniform-rods-axis"></a>
## Move a Uniform Rod's Axis

**Source-video rod derivation (`JrkimXqnCLw`, 00:08:41–00:11:07):** A uniform thin rod of mass $M$ and length $L$ has

$$
I_{\mathrm{cm}}=\frac{1}{12}ML^2
$$

about a perpendicular axis through its center. Move the parallel axis to an end of the rod.

**Explanation**

The center is $L/2$ from either end, so $d=L/2$. Apply the theorem:

$$
\begin{aligned}
I_{\mathrm{end}}
&=\frac{1}{12}ML^2+M\left(\frac L2\right)^2\\
&=\left(\frac{1}{12}+\frac14\right)ML^2\\
&=\boxed{\frac13ML^2}.
\end{aligned}
$$

Direct integration about the end confirms the result:

$$
I_{\mathrm{end}}
=\frac ML\int_0^L x^2\,dx
=\frac13ML^2.
$$

**Lecture-note controlled application:** Move the rod's axis to a point $L/3$ from the left end. The center lies at $L/2$, so the axis separation is

$$
d=\left|\frac L2-\frac L3\right|=\frac L6.
$$

Therefore,

$$
\begin{aligned}
I_{L/3}
&=\frac{1}{12}ML^2+M\left(\frac L6\right)^2\\
&=\left(\frac{1}{12}+\frac{1}{36}\right)ML^2\\
&=\boxed{\frac19ML^2}.
\end{aligned}
$$

Measuring $u$ from the new axis, the rod spans $-L/3\le u\le2L/3$. The direct check is

$$
\frac ML\int_{-L/3}^{2L/3}u^2\,du=\frac19ML^2.
$$

The location $L/3$ is measured from the end, but $d$ is measured from the center-of-mass axis. Confusing those two distances would produce the wrong shift term.

```quiz
type: radio
id: mct-p7-rod-offset
shuffle: true
content: |-
  A uniform thin rod of mass $M$ and length $L$ rotates about a perpendicular axis located $L/4$ from its left end. What is its moment of inertia?
options:
- id: mct-p7-rod-offset-a
  content: |-
    $\dfrac{7}{48}ML^2$
  correct: true
  feedback: |-
    The rod's center is at $L/2$, so $d=|L/2-L/4|=L/4$. Starting from $I_{\mathrm{cm}}=ML^2/12$, the theorem gives $I=ML^2/12+M(L/4)^2=(4/48+3/48)ML^2=7ML^2/48$.
- id: mct-p7-rod-offset-b
  content: |-
    $\dfrac{1}{16}ML^2$
  feedback: |-
    This is only the shift term $M(L/4)^2$. The rod already has $I_{\mathrm{cm}}=ML^2/12$; adding both contributions gives $7ML^2/48$.
- id: mct-p7-rod-offset-c
  content: |-
    $\dfrac{1}{48}ML^2$
  feedback: |-
    This subtracts the shift term: $1/12-1/16=1/48$. A parallel shift away from the center adds $Md^2$, so the inertia is $7ML^2/48$, not smaller than $I_{\mathrm{cm}}$.
- id: mct-p7-rod-offset-d
  content: |-
    $\dfrac{1}{3}ML^2$
  feedback: |-
    The value $ML^2/3$ applies when the axis is at an end, where $d=L/2$. Here the axis is $L/4$ from the end and only $L/4$ from the center, so the smaller shift gives $7ML^2/48$.
- id: mct-p7-rod-offset-e
  content: |-
    $\dfrac{1}{12}ML^2$
  feedback: |-
    This is the center-axis inertia. It would apply only at $L/2$ from the left end; the requested axis is displaced by $L/4$, so add $M(L/4)^2$ to obtain $7ML^2/48$.
```

---

<a id="summary"></a>
## Summary

When a known center-of-mass inertia must be transferred to a parallel axis:

1. Confirm that the known axis passes through the center of mass.
2. Confirm that the requested axis is parallel and belongs to the same rigid body.
3. Measure the perpendicular axis separation $d$.
4. Use the body's total mass in $I_{\mathrm{new}}=I_{\mathrm{cm}}+M_{\mathrm{total}}d^2$.
5. Check that $I_{\mathrm{new}}\ge I_{\mathrm{cm}}$ and verify with $\sum mr_\perp^2$ or direct integration when the geometry is simple.

The main traps are treating symmetry as a requirement, starting from an inertia about a non-center axis, using one component's mass instead of the total mass, failing to square $d$, and measuring $d$ from an end or mass rather than between the two axes.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
