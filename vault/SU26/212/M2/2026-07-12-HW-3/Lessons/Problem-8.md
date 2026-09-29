# Mass Removed from a Uniform Disk

<!--
lesson-id: 212-M2-024
topic-code: MTH212.M2.24
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert the Radius Fraction to an Area Fraction](#convert-the-radius-fraction-to-an-area-fraction)
- [Ignore the Hole's Position When Finding Its Mass](#ignore-the-holes-position-when-finding-its-mass)
- [Avoid the Unsquared-Radius Trap](#avoid-the-unsquared-radius-trap)
- [Summary](#summary)

## Prerequisites

- The area of a circle is $A=\pi r^2$.
- A uniform disk has the same mass per unit area everywhere.
- Fractions may be squared: $\left(\frac{a}{b}\right)^2=\frac{a^2}{b^2}$.

---

<a id="introduction"></a>
## Introduction

When a smaller circular piece is removed from a **uniform** disk, the recognition cue is the word *uniform*. Equal area carries equal mass, so the fraction of the total mass removed equals the fraction of the total area removed:

$$
\frac{m_{\mathrm{removed}}}{M}
=
\frac{A_{\mathrm{hole}}}{A_{\mathrm{disk}}}.
$$

For a disk of radius $R$ and a circular hole of radius $r$,

$$
\frac{m_{\mathrm{removed}}}{M}
=
\frac{\pi r^2}{\pi R^2}
=
\left(\frac{r}{R}\right)^2.
$$

The reusable rule is therefore

$$
\boxed{m_{\mathrm{removed}}=M\left(\frac{r}{R}\right)^2}.
$$

In compact form, the reasoning chain is

$$
\boxed{\text{mass fraction}=\text{area fraction}=(\text{radius fraction})^2}.
$$

---

<a id="convert-the-radius-fraction-to-an-area-fraction"></a>
## Convert the Radius Fraction to an Area Fraction

**Example:** A uniform disk has mass $M$ and radius $R$. A circular portion of radius $R/3$ is removed. What is the mass of that portion?

**Explanation**

The radius scale factor is

$$
\frac{r}{R}=\frac{R/3}{R}=\frac13.
$$

Mass follows area, and area follows the square of the radius. Thus,

$$
m_{\mathrm{removed}}
=M\left(\frac13\right)^2
=\frac{M}{9}.
$$

```quiz
type: radio
id: p8-radius-fraction
content: |-
  A circular piece of radius $R/4$ is cut from a uniform disk of mass $M$ and radius $R$. What mass is removed?
options:
- id: a
  content: |-
    $\dfrac{M}{4}$
  feedback: This uses the radius fraction without squaring it.
- id: b
  content: |-
    $\dfrac{M}{8}$
  feedback: The mass fraction is not found by multiplying the radius fraction by an extra $1/2$.
- id: c
  content: |-
    $\dfrac{M}{16}$
  correct: true
  feedback: Squaring the radius fraction gives $(1/4)^2=1/16$.
- id: d
  content: |-
    $\dfrac{M}{\pi}$
  feedback: The factor $\pi$ cancels in the ratio of the two circular areas.
```

---

<a id="ignore-the-holes-position-when-finding-its-mass"></a>
## Ignore the Hole's Position When Finding Its Mass

**Example:** A hole of radius $R/2$ is cut from a uniform disk of mass $M$ and radius $R$. The hole's center is $R/4$ from the disk's center. What mass is removed?

**Explanation**

The offset tells us where the missing mass was located, but not how much mass was removed. For the mass alone, use the hole's radius:

$$
m_{\mathrm{removed}}
=M\left(\frac{R/2}{R}\right)^2
=M\left(\frac12\right)^2
=\frac{M}{4}.
$$

The center offset will matter in a later center-of-mass calculation, but it does not enter this mass calculation.

```quiz
type: radio
id: p8-original
content: |-
  A circular hole of radius $R/2$ is removed from a uniform disk of mass $M$ and radius $R$. The center of the hole is a distance $R/2$ from the disk's center, as shown.

  What is the mass of the removed portion?

  ![](<../Source/2026-07-12-HW-3/Images/excavated-disk-diagram.png>)
options:
- id: a
  content: |-
    $m/3$
- id: b
  content: |-
    $m/4$
  correct: true
- id: c
  content: |-
    $m/6$
```

---

<a id="avoid-the-unsquared-radius-trap"></a>
## Avoid the Unsquared-Radius Trap

**Example:** A circular hole has $60\%$ of the original disk's radius. What fraction of the disk's mass is removed?

**Explanation**

The radius fraction is $0.60$, but the mass fraction is the **square** of that number:

$$
\frac{m_{\mathrm{removed}}}{M}=(0.60)^2=0.36.
$$

So the hole removes $36\%$ of the mass, not $60\%$. The most common mistake is to use the linear radius fraction as though it were already an area fraction.

```quiz
type: radio
id: p8-square-the-scale
content: |-
  The diameter of a circular hole is one-half the diameter of a uniform disk. What fraction of the disk's mass is removed?
options:
- id: a
  content: |-
    $\dfrac12$
  feedback: This is the diameter fraction, not the area or mass fraction.
- id: b
  content: |-
    $\dfrac14$
  correct: true
  feedback: The diameter and radius have the same scale factor, so the mass fraction is $(1/2)^2=1/4$.
- id: c
  content: |-
    $\dfrac18$
  feedback: The linear scale factor is squared, not multiplied by another unrelated factor.
- id: d
  content: |-
    $\dfrac1{16}$
  feedback: This squares the scale factor twice.
```

---

<a id="summary"></a>
## Summary

For a circular hole cut from a uniform disk:

1. Find the radius fraction $r/R$.
2. Square it to get the area fraction: $(r/R)^2$.
3. Multiply by the original mass:

$$
m_{\mathrm{removed}}=M\left(\frac{r}{R}\right)^2.
$$

The hole's position does not affect its mass. The main trap is forgetting to square the radius fraction. For $r=R/2$, the removed mass is $M/4$ (written as $m/4$ in the source choices).

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
