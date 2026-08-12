# Center of Mass on a Symmetry Axis

<!--
lesson-id: 212-M2-025
topic-code: MTH212.M2.25
-->

## Table of Contents

- [Introduction](#introduction)
- [Recognize the Reflection Symmetry](#recognize-the-reflection-symmetry)
- [See Why Paired Mass Cancels](#see-why-paired-mass-cancels)
- [Match the Axis to the Forced Coordinate](#match-the-axis-to-the-forced-coordinate)
- [Apply the Test to an Excavated Disk](#apply-the-test-to-an-excavated-disk)
- [Know When the Shortcut Does Not Apply](#know-when-the-shortcut-does-not-apply)
- [Summary](#summary)

## Prerequisites

- Read $x$- and $y$-coordinates from a Cartesian coordinate system.
- Recognize reflection symmetry across the coordinate axes.
- Know that the center of mass is a mass-weighted average of position.

---

<a id="introduction"></a>
## Introduction

When a uniform object is unchanged by reflection across a line, its center of mass must lie on that line. The recognition cue is not whether the object looks balanced in every direction. It is whether reflecting **all of the remaining material** across a particular line reproduces the same object.

For an excavated object, use this quick test:

1. Choose a candidate symmetry line.
2. Check that the original object maps onto itself across that line.
3. Check that the removed region also maps onto itself across that line.

If both checks pass, the remaining object has that reflection symmetry.

For a shape symmetric across the $x$-axis, every bit of mass above the axis has an equal mirror partner below it. Their contributions to the vertical center of mass cancel, so

$$
y_{\mathrm{cm}}=0.
$$

This conclusion needs no area or mass calculation.

---

<a id="recognize-the-reflection-symmetry"></a>
## Recognize the Reflection Symmetry

**Example:** A uniform rectangular plate extends from $y=-2\ \mathrm{cm}$ to $y=2\ \mathrm{cm}$. A semicircular notch is removed from its right edge, with the notch centered on the $x$-axis. What can you conclude about $y_{\mathrm{cm}}$?

**Explanation**

Reflect the entire remaining plate across the $x$-axis. In coordinates, this reflection is

$$
(x,y)\mapsto(x,-y).
$$

The rectangle maps onto itself, and the notch also maps onto itself because it is centered on the axis. Therefore, the remaining plate has reflection symmetry across the $x$-axis.

Its center of mass must lie somewhere on that axis, so

$$
y_{\mathrm{cm}}=0.
$$

The notch can shift $x_{\mathrm{cm}}$, but it cannot shift the center of mass above or below the $x$-axis.

```quiz
type: radio
id: p9-recognize-symmetry
content: |-
  A uniform plate is unchanged when reflected across the $x$-axis. Which conclusion is guaranteed?
options:
- id: a
  content: |-
    $x_{\mathrm{cm}}=0$
- id: b
  content: |-
    $y_{\mathrm{cm}}=0$
  correct: true
- id: c
  content: |-
    $x_{\mathrm{cm}}=y_{\mathrm{cm}}$
- id: d
  content: |-
    The center of mass is at the geometric origin.
- id: e
  content: |-
    The plate must also be symmetric across the $y$-axis.
```

---

<a id="see-why-paired-mass-cancels"></a>
## See Why Paired Mass Cancels

**Example:** A small mass element $dm$ is located at vertical coordinate $y$. Reflection symmetry across the $x$-axis guarantees an equal mass element at $-y$. What is this pair's contribution to the numerator of $y_{\mathrm{cm}}$?

**Explanation**

The vertical center of mass is

$$
y_{\mathrm{cm}}=\frac{\int y\,dm}{\int dm}.
$$

The mirror pair contributes

$$
y\,dm+(-y)\,dm=0
$$

to the numerator. Every off-axis mass element has such a partner, while material on the $x$-axis already has $y=0$. Thus the entire numerator vanishes and $y_{\mathrm{cm}}=0$.

```quiz
type: radio
id: p9-pair-cancellation
content: |-
  Two equal point masses $m$ are at $(4,3)$ and $(4,-3)$. A third mass $2m$ is at $(1,0)$. What is the $y$-coordinate of the system's center of mass?
options:
- id: a
  content: |-
    $-3$
- id: b
  content: |-
    $-1$
- id: c
  content: |-
    $0$
  correct: true
- id: d
  content: |-
    $1$
- id: e
  content: |-
    $3$
```

---

<a id="match-the-axis-to-the-forced-coordinate"></a>
## Match the Axis to the Forced Coordinate

**Example:** A uniform lamina is unchanged by reflection across the $y$-axis but is not symmetric across the $x$-axis. Which center-of-mass coordinate is fixed by symmetry?

**Explanation**

Reflection across the $y$-axis pairs mass at $(x,y)$ with equal mass at $(-x,y)$. The horizontal contributions cancel, so $x_{\mathrm{cm}}=0$. The pair has the same $y$-coordinate, so this symmetry alone does not determine $y_{\mathrm{cm}}$.

Use the coordinate that is **perpendicular** to the symmetry axis:

- symmetry across the $x$-axis forces $y_{\mathrm{cm}}=0$;
- symmetry across the $y$-axis forces $x_{\mathrm{cm}}=0$.

```quiz
type: radio
id: p9-axis-coordinate
content: |-
  A uniform shape is unchanged by reflection across the $y$-axis. It has more material above the $x$-axis than below it. Which statement must be true?
options:
- id: a
  content: |-
    $x_{\mathrm{cm}}=0$
  correct: true
- id: b
  content: |-
    $y_{\mathrm{cm}}=0$
- id: c
  content: |-
    Both center-of-mass coordinates are zero.
- id: d
  content: |-
    Neither center-of-mass coordinate can be inferred.
- id: e
  content: |-
    $x_{\mathrm{cm}}=y_{\mathrm{cm}}$
```

---

<a id="apply-the-test-to-an-excavated-disk"></a>
## Apply the Test to an Excavated Disk

**Example:** A circular hole of radius $R/2$ is removed from a uniform disk of mass $M$ and radius $R$. The hole's center is on the $x$-axis, a distance $R/2$ to the right of the disk's center. Find the $y$-coordinate of the excavated disk's center of mass.

![](<../Source/2026-07-12-HW-3/Images/excavated-disk-diagram.png>)

**Explanation**

Apply the two-part reflection test:

1. The full disk maps onto itself across the $x$-axis.
2. The removed circle also maps onto itself because its center lies on the $x$-axis.

Removing the second symmetric region from the first therefore leaves a shape that is still unchanged by reflection across the $x$-axis.

The hole is off-center horizontally, so the remaining center of mass shifts in the $x$-direction. However, there is still equal remaining mass at $+y$ and $-y$. Therefore,

$$
\boxed{y_{\mathrm{cm}}=0}.
$$

Neither $M$ nor $R$ is needed for this coordinate.

```quiz
type: radio
id: p9-excavated-disk
shuffle: true
content: |-
  A circular hole of radius $R/2$ is removed from a uniform disk of mass $M$ and radius $R$. The center of the hole is a distance $R/2$ from the disk's center.

  Place the origin at the center of the original disk, with $+x$ pointing right and $+y$ pointing upward. What is the $y$-coordinate of the center of mass of the excavated disk?

  Hint: No calculation is required.

  ![](<../Source/2026-07-12-HW-3/Images/excavated-disk-diagram.png>)
options:
- id: a
  content: |-
    $R/2$
- id: b
  content: |-
    $-R/3$
- id: c
  content: |-
    $0$
  correct: true
- id: d
  content: |-
    $R/3$
- id: e
  content: |-
    $R/2$
```

---

<a id="know-when-the-shortcut-does-not-apply"></a>
## Know When the Shortcut Does Not Apply

**Example:** A circular hole is cut from a uniform disk, but the hole's center is now at $(0,R/3)$. Which coordinate is fixed by symmetry?

**Explanation**

The hole is centered on the $y$-axis, so the remaining shape is unchanged by reflection across the $y$-axis. This forces $x_{\mathrm{cm}}=0$.

The hole lies above the $x$-axis, so reflection across the $x$-axis would move it to a different location. There is no top-bottom symmetry, and $y_{\mathrm{cm}}$ is not forced to be zero. In fact, removing mass from above the origin shifts the remaining center of mass downward.

```quiz
type: radio
id: p9-broken-symmetry
content: |-
  A circular hole is removed from a uniform disk. The hole's center is at $(0,-R/4)$. Which conclusion is guaranteed by symmetry?
options:
- id: a
  content: |-
    $x_{\mathrm{cm}}=0$
  correct: true
- id: b
  content: |-
    $y_{\mathrm{cm}}=0$
- id: c
  content: |-
    Both $x_{\mathrm{cm}}=0$ and $y_{\mathrm{cm}}=0$
- id: d
  content: |-
    $x_{\mathrm{cm}}=-R/4$
- id: e
  content: |-
    $y_{\mathrm{cm}}=-R/4$
```

---

<a id="summary"></a>
## Summary

1. Identify a line that reflects **all remaining material** onto itself. For a cutout, test both the original object and the removed region.
2. Pair the mass at $(x,y)$ with its reflected equal mass. The contributions perpendicular to the symmetry line cancel.
3. Conclude that the center of mass lies on the symmetry line, then translate the line into the requested coordinate:
   - $x$-axis symmetry gives $y_{\mathrm{cm}}=0$;
   - $y$-axis symmetry gives $x_{\mathrm{cm}}=0$.
4. Do not assume both coordinates vanish. An off-center hole can shift the center of mass along the symmetry axis while leaving the perpendicular coordinate equal to zero.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
