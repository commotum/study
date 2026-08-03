# Center of Mass of an Object with a Hole

<!--
lesson-id: 212-M2-026
topic-code: MTH212.M2.26
-->

## Table of Contents

- [Introduction](#introduction)
- [Represent a Hole as Negative Mass](#represent-a-hole-as-negative-mass)
- [Find the Removed Mass from Area](#find-the-removed-mass-from-area)
- [Use the Remaining Mass in the Denominator](#use-the-remaining-mass-in-the-denominator)
- [Check the Direction of the Shift](#check-the-direction-of-the-shift)
- [Apply the Method to the Excavated Disk](#apply-the-method-to-the-excavated-disk)
- [Summary](#summary)

## Prerequisites

- Use $x_{\mathrm{cm}}=\dfrac{\sum m_i x_i}{\sum m_i}$ for discrete masses.
- Know that a uniform lamina's mass is proportional to its area.
- Use the area formula $A=\pi r^2$ for a circle.

---

<a id="introduction"></a>
## Introduction

When a uniform object has a simple piece removed, calculate the center of mass by treating the removed piece as a **negative mass**. The recognition cue is a hole whose shape and center of mass are known.

Keep two signed entries in the center-of-mass sum:

- the original body contributes mass $+M$ at $x_0$;
- the hole contributes bookkeeping mass $-m_h$ at $x_h$.

For an original body of mass $M$ centered at $x_0$ and a removed piece of mass $m_h$ centered at $x_h$,

$$
x_{\mathrm{cm}}
=\frac{Mx_0+(-m_h)x_h}{M-m_h}
=\frac{Mx_0-m_hx_h}{M-m_h}.
$$

The denominator is the mass that remains, not the original mass. If the hole is on the right, the remaining center of mass must shift left.

---

<a id="represent-a-hole-as-negative-mass"></a>
## Represent a Hole as Negative Mass

**Example:** A uniform plate of mass $10\text{ kg}$ is centered at $x=0$. A $2\text{ kg}$ piece centered at $x=3\text{ m}$ is removed. Find the center of mass of the remaining plate.

**Explanation**

Represent the original plate by $(M,x_0)=(10,0)$ and the hole by $(-m_h,x_h)=(-2,3)$. Then

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{(10)(0)+(-2)(3)}{10+(-2)}\\
&=\frac{-6}{8}\\
&=-0.75\text{ m}.
\end{aligned}
$$

Removing mass at positive $x$ leaves the plate balanced to the left of the origin.

```quiz
type: radio
id: p10-negative-mass
content: |-
  A uniform plate of mass $12\text{ kg}$ is centered at $x=0$. A $3\text{ kg}$ piece centered at $x=2\text{ m}$ is removed. What is the remaining plate's $x$-coordinate of center of mass?
options:
- id: a
  content: |-
    $-2/3\text{ m}$
  correct: true
- id: b
  content: |-
    $-1/2\text{ m}$
- id: c
  content: |-
    $0$
- id: d
  content: |-
    $1/2\text{ m}$
- id: e
  content: |-
    $2/3\text{ m}$
```

---

<a id="find-the-removed-mass-from-area"></a>
## Find the Removed Mass from Area

**Example:** A circular hole of radius $R/3$ is cut from a uniform disk of mass $M$ and radius $R$. Find the mass $m_h$ of the removed material.

**Explanation**

Uniform surface density means that the mass fraction equals the area fraction:

$$
\frac{m_h}{M}
=\frac{\pi(R/3)^2}{\pi R^2}
=\left(\frac{1}{3}\right)^2
=\frac{1}{9}.
$$

Thus,

$$
m_h=\frac{M}{9}.
$$

More generally, if the hole and disk have radii $r_h$ and $R$, define the removed fraction

$$
f=\frac{m_h}{M}=\left(\frac{r_h}{R}\right)^2.
$$

Finding $f$ first keeps the later center-of-mass calculation compact.

The radius ratio must be squared. A hole with one-third the radius has one-ninth the mass, not one-third.

```quiz
type: radio
id: p10-area-ratio
content: |-
  A circular hole of radius $R/2$ is removed from a uniform disk of mass $M$ and radius $R$. What mass is removed?
options:
- id: a
  content: |-
    $M/8$
- id: b
  content: |-
    $M/4$
  correct: true
- id: c
  content: |-
    $M/2$
- id: d
  content: |-
    $3M/4$
- id: e
  content: |-
    $M$
```

---

<a id="use-the-remaining-mass-in-the-denominator"></a>
## Use the Remaining Mass in the Denominator

**Example:** An object of mass $M$ centered at $x=0$ loses a piece of mass $M/5$ centered at $x=d$. Write the remaining center of mass in terms of $d$.

**Explanation**

The signed moment is

$$
M(0)-\frac{M}{5}d=-\frac{Md}{5},
$$

and the remaining mass is

$$
M-\frac{M}{5}=\frac{4M}{5}.
$$

Therefore,

$$
x_{\mathrm{cm}}
=\frac{-Md/5}{4M/5}
=-\frac{d}{4}.
$$

Dividing by $M$ instead would incorrectly give $-d/5$.

```quiz
type: radio
id: p10-remaining-denominator
content: |-
  A body of mass $M$ centered at $x=0$ loses a piece of mass $M/3$ centered at $x=d$. What is the remaining body's $x_{\mathrm{cm}}$?
options:
- id: a
  content: |-
    $-d/2$
  correct: true
- id: b
  content: |-
    $-d/3$
- id: c
  content: |-
    $0$
- id: d
  content: |-
    $d/3$
- id: e
  content: |-
    $d/2$
```

---

<a id="check-the-direction-of-the-shift"></a>
## Check the Direction of the Shift

**Example:** A hole is cut from the left side of a uniform plate whose original center is at the origin. Without calculating, determine the sign of $x_{\mathrm{cm}}$ for the remaining plate.

**Explanation**

The hole has $x_h<0$. Its contribution to the numerator is $-m_hx_h$, which is positive because it is the product of two negative factors. Therefore, $x_{\mathrm{cm}}>0$: removing mass from the left shifts the balance point right.

Use this direction check before accepting a numerical result:

- hole on the right $\Rightarrow x_{\mathrm{cm}}<0$;
- hole on the left $\Rightarrow x_{\mathrm{cm}}>0$.

The remaining center of mass shifts **away from** the hole, so its coordinate has the opposite sign when the original center is at the origin.

```quiz
type: radio
id: p10-direction-check
content: |-
  A hole centered at $x=+4\text{ cm}$ is removed from a uniform plate originally centered at the origin. Which sign must the remaining plate's $x_{\mathrm{cm}}$ have?
options:
- id: a
  content: |-
    Negative
  correct: true
- id: b
  content: |-
    Zero
- id: c
  content: |-
    Positive
- id: d
  content: |-
    The sign must match the hole's coordinate.
- id: e
  content: |-
    The sign cannot be predicted.
```

---

<a id="apply-the-method-to-the-excavated-disk"></a>
## Apply the Method to the Excavated Disk

**Example:** A circular hole of radius $R/2$ is removed from a uniform disk of mass $M$ and radius $R$. The hole's center is at $x=R/2$. Find the $x$-coordinate of the remaining disk's center of mass.

![](<../Source/2026-07-12-HW-3/Images/excavated-disk-diagram.png>)

**Explanation**

First find the removed mass from the circle-area ratio:

$$
m_h=M\left(\frac{R/2}{R}\right)^2=\frac{M}{4}.
$$

The original disk is centered at $x_0=0$, and the hole is centered at $x_h=R/2$. Treating the hole as negative mass gives

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{M(0)-\left(\frac{M}{4}\right)\left(\frac{R}{2}\right)}{M-\frac{M}{4}}\\
&=\frac{-\left(\frac{1}{4}\right)\left(\frac{R}{2}\right)}{1-\frac{1}{4}}\\
&=\frac{-R/8}{3/4}\\
&=-\frac{R}{6}.
\end{aligned}
$$

The negative sign passes the direction check: the hole is to the right, so the remaining mass balances to the left.

```quiz
type: radio
id: p10-excavated-disk
shuffle: true
content: |-
  A circular hole of radius $R/2$ is removed from a uniform disk of mass $M$ and radius $R$. The center of the hole is a distance $R/2$ from the disk's center.

  Place the origin at the center of the original disk, with $+x$ pointing right and $+y$ pointing upward. What is the $x$-coordinate of the center of mass of the excavated disk?

  ![](<../Source/2026-07-12-HW-3/Images/excavated-disk-diagram.png>)
options:
- id: a
  content: |-
    $-2R/3$
- id: b
  content: |-
    $-R/3$
- id: c
  content: |-
    $-R/6$
  correct: true
- id: d
  content: |-
    $0$
- id: e
  content: |-
    $R/3$
```

---

<a id="summary"></a>
## Summary

When a simple piece is removed from a uniform body:

1. Locate the original body's center $x_0$ and the hole's center $x_h$.
2. Find the hole's mass. For similar uniform regions, mass follows area, so radius ratios are squared.
3. Treat the hole as negative mass:

   $$
   x_{\mathrm{cm}}=\frac{Mx_0-m_hx_h}{M-m_h}.
   $$

4. Divide by the **remaining** mass $M-m_h$.
5. Check the sign: the center of mass shifts away from the removed material.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
