# Locate a Listener on a Circular Wavefront

<!--
lesson-id: 212-M5-011
topic-code: MTH212.M5.11
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Source and Wavefront Radius](#find-the-source-and-wavefront-radius)
- [Use the Positive-Y Right Triangle](#use-the-positive-y-right-triangle)
- [Carry the Geometry Through the Full Chain](#carry-the-geometry-through-the-full-chain)
- [Match the Source Coordinates and Answer Form](#match-the-source-coordinates-and-answer-form)
- [Summary](#summary)

## Prerequisites

- Find the midpoint of two coordinates on a number line.
- Use the Pythagorean theorem to find a missing leg.
- Evaluate and round a square root.

---

<a id="introduction"></a>
## Introduction

A wavefront from a point sound source is a circle in a two-dimensional coordinate picture. Every point on one wavefront is the same distance from the source.

When two listeners on the $x$-axis detect the same wavefront simultaneously and the source also lies on the $x$-axis:

1. The source is the midpoint between those two listeners.
2. Their distance from the source is the wavefront radius.
3. A third listener on the $y$-axis lies on the same circle.

The key cue is **the same wavefront simultaneously**, which means equal distance from the source.

| Object | Coordinate or role |
| --- | --- |
| first listener | $(x_1,0)$ |
| second listener | $(x_2,0)$ |
| source | $(x_s,0)$, the wavefront center |
| third listener | $(0,y)$ on the positive $y$-axis |
| source-to-listener distance | radius $r$ |

---

<a id="find-the-source-and-wavefront-radius"></a>
## Find the Source and Wavefront Radius

Suppose the first two listeners have coordinates $(x_1,0)$ and $(x_2,0)$. The source coordinate is

$$
x_s=\frac{x_1+x_2}{2}.
$$

The wavefront radius is the distance from the source to either listener:

$$
r=|x_1-x_s|=|x_2-x_s|.
$$

Because the source and both listeners all lie on the $x$-axis, the two listeners are opposite endpoints of a diameter. This explains why the midpoint locates the source and why the radius is half their separation.

**Example:** Listeners at $x=-8\ \mathrm{m}$ and $x=+4\ \mathrm{m}$ detect the same wavefront simultaneously. The source lies on the $x$-axis. Find the source coordinate and wavefront radius.

**Explanation**

$$
x_s=\frac{-8+4}{2}=-2\ \mathrm{m}.
$$

Then

$$
r=|-8-(-2)|=6\ \mathrm{m}.
$$

```quiz
type: radio
id: problem-4-wavefront-q1
content: |-
  Listeners at $x=-5\ \mathrm{m}$ and $x=+3\ \mathrm{m}$ detect the same wavefront simultaneously. If the source lies on the $x$-axis, what are the source coordinate and wavefront radius?
options:
- id: a
  content: |-
    $x_s=-1\ \mathrm{m}$ and $r=4\ \mathrm{m}$
  correct: true
  feedback: |-
    The midpoint is $(-5+3)/2=-1$, and each listener is $4\ \mathrm{m}$ from that point.
- id: b
  content: |-
    $x_s=-2\ \mathrm{m}$ and $r=8\ \mathrm{m}$
  feedback: |-
    The source is the midpoint, and $8\ \mathrm{m}$ is the full listener separation rather than the radius.
- id: c
  content: |-
    $x_s=+1\ \mathrm{m}$ and $r=4\ \mathrm{m}$
  feedback: |-
    Keep the sign when averaging: $(-5+3)/2=-1$, not $+1$.
- id: d
  content: |-
    $x_s=-1\ \mathrm{m}$ and $r=8\ \mathrm{m}$
  feedback: |-
    The midpoint is correct, but the radius is half the endpoint separation.
- id: e
  content: |-
    $x_s=+4\ \mathrm{m}$ and $r=2\ \mathrm{m}$
  feedback: |-
    Neither value is the midpoint-and-radius pair for the two listener coordinates.
```

---

<a id="use-the-positive-y-right-triangle"></a>
## Use the Positive-Y Right Triangle

If the source is at $(x_s,0)$ and the third listener is on the positive $y$-axis at $(0,y)$, their horizontal separation is

$$
\Delta x=|0-x_s|.
$$

The source-to-listener distance is the radius $r$, so

$$
(\Delta x)^2+y^2=r^2.
$$

Solving for a listener on the positive $y$-axis gives

$$
y=\sqrt{r^2-(\Delta x)^2}.
$$

Here $r$ is the hypotenuse, while $\Delta x$ and $y$ are the legs. Therefore the known leg is subtracted from $r^2$. The positive-$y$ condition selects the positive square root.

**Example:** A circular wavefront has center $(-3,0)$ and radius $5\ \mathrm{m}$. Find its intersection with the positive $y$-axis.

**Explanation**

The horizontal leg from $(-3,0)$ to the $y$-axis has length $3\ \mathrm{m}$:

$$
y
=\sqrt{5^2-3^2}
=\sqrt{25-9}
=4\ \mathrm{m}.
$$

```quiz
type: radio
id: problem-4-wavefront-q2
content: |-
  A circular wavefront has center $(-5,0)$ and radius $13\ \mathrm{m}$. What is the positive $y$-coordinate where it crosses the $y$-axis?
options:
- id: a
  content: |-
    $5\ \mathrm{m}$
  feedback: |-
    This is the horizontal leg, not the vertical coordinate.
- id: b
  content: |-
    $8\ \mathrm{m}$
  feedback: |-
    A leg must be found from $y=\sqrt{r^2-(\Delta x)^2}$.
- id: c
  content: |-
    $12\ \mathrm{m}$
  correct: true
  feedback: |-
    $y=\sqrt{13^2-5^2}=\sqrt{169-25}=\sqrt{144}=12\ \mathrm{m}$.
- id: d
  content: |-
    $13\ \mathrm{m}$
  feedback: |-
    This is the radius, or hypotenuse, not the vertical leg.
- id: e
  content: |-
    $18\ \mathrm{m}$
  feedback: |-
    A triangle leg cannot exceed its $13\ \mathrm{m}$ hypotenuse.
```

---

<a id="carry-the-geometry-through-the-full-chain"></a>
## Carry the Geometry Through the Full Chain

Keep the geometric quantities separate:

- midpoint $\rightarrow$ source coordinate $x_s$,
- endpoint-to-midpoint distance $\rightarrow$ radius $r$,
- source-to-$y$-axis distance $\rightarrow$ horizontal leg $\Delta x$.

**Example:** Listeners at $x=-10\ \mathrm{m}$ and $x=+2\ \mathrm{m}$ detect the same wavefront simultaneously. Find the positive $y$-coordinate of a third listener on that wavefront.

**Explanation**

First locate the source and radius:

$$
x_s=\frac{-10+2}{2}=-4\ \mathrm{m},
\qquad
r=|-10-(-4)|=6\ \mathrm{m}.
$$

The horizontal leg to the $y$-axis is $\Delta x=4\ \mathrm{m}$, so

$$
y=\sqrt{6^2-4^2}
=\sqrt{20}
=4.472\ldots\ \mathrm{m}.
$$

Keep $\sqrt{20}$ as the exact coordinate until the last step. Approximating earlier can introduce unnecessary rounding error.

```quiz
type: radio
id: problem-4-wavefront-q3
content: |-
  Listeners at $x=-9\ \mathrm{m}$ and $x=+3\ \mathrm{m}$ detect the same wavefront simultaneously. A third listener on the positive $y$-axis detects it at the same time. Which expression gives her $y$-coordinate?
options:
- id: a
  content: |-
    $\displaystyle \sqrt{6^2-3^2}=\sqrt{27}\ \mathrm{m}$
  correct: true
  feedback: |-
    The source is at $x_s=(-9+3)/2=-3$, the radius is $6$, and the horizontal leg to the $y$-axis is $3$.
- id: b
  content: |-
    $\displaystyle \sqrt{6^2+3^2}=\sqrt{45}\ \mathrm{m}$
  feedback: |-
    The radius is the hypotenuse, so solve for the missing leg by subtracting, not adding.
- id: c
  content: |-
    $\displaystyle 6-3=3\ \mathrm{m}$
  feedback: |-
    The Pythagorean relation uses squared lengths before taking a square root.
- id: d
  content: |-
    $\displaystyle \sqrt{12^2-3^2}=\sqrt{135}\ \mathrm{m}$
  feedback: |-
    $12\ \mathrm{m}$ is the full listener separation; the radius is $6\ \mathrm{m}$.
- id: e
  content: |-
    $6\ \mathrm{m}$
  feedback: |-
    This is the radius. Because the source is not on the $y$-axis, the vertical leg must be shorter.
```

---

<a id="match-the-source-coordinates-and-answer-form"></a>
## Match the Source Coordinates and Answer Form

Use the exact signs on the coordinates, keep the positive-$y$ condition, and round only the final coordinate.

**Example:** A sound source lies somewhere on the $x$-axis. Listeners at $x=-7.0\ \mathrm{m}$ and $x=+3.0\ \mathrm{m}$ detect the same wavefront simultaneously. A third listener on the positive $y$-axis also detects that wavefront at the same time. What is her $y$-coordinate?

Enter the coordinate in meters as a number only.

**Explanation**

The source is equidistant from the two listeners on the $x$-axis, so it lies at their midpoint:

$$
x_s=\frac{-7.0+3.0}{2}=-2.0\ \mathrm{m}.
$$

The wavefront radius is $5.0\ \mathrm{m}$. The third listener is at $(0,y)$, so

$$
(2.0\ \mathrm{m})^2+y^2=(5.0\ \mathrm{m})^2.
$$

Therefore,

$$
y=\sqrt{21}\ \mathrm{m}
=4.5825\ldots\ \mathrm{m}.
$$

The measured positions have two significant figures, so $y=4.6\ \mathrm{m}$. Enter $4.6$.

```quiz
type: radio
id: problem-4-wavefront-q4
content: |-
  Listeners at $x=-6.0\ \mathrm{m}$ and $x=+2.0\ \mathrm{m}$ detect the same wavefront simultaneously. A third listener is on the positive $y$-axis. Her coordinate must be entered in meters as a number only, to two significant figures. Which number should be entered?
options:
- id: a
  content: |-
    $2.0$
- id: b
  content: |-
    $3.5$
  correct: true
  feedback: |-
    The source is at $x_s=-2.0$, the radius is $4.0$, and $y=\sqrt{4.0^2-2.0^2}=\sqrt{12}=3.464\ldots\ \mathrm{m}$, which rounds to $3.5$.
- id: c
  content: |-
    $4.0$
- id: d
  content: |-
    $4.5$
- id: e
  content: |-
    $8.0$
```

---

<a id="summary"></a>
## Summary

When two $x$-axis listeners detect the same circular wavefront simultaneously:

1. Find the source:
   $$
   x_s=\frac{x_1+x_2}{2}.
   $$
2. Find the radius $r$ from the source to either listener.
3. For a third listener at $(0,y)$, use
   $$
   y=\sqrt{r^2-|x_s|^2}.
   $$
4. Choose the positive square root for the positive $y$-axis.
5. Keep the exact radical until the final numerical approximation.
6. Round only the final coordinate and follow the requested answer format.

The main traps are mishandling the negative coordinate, using the full listener separation as the radius, and adding the squared legs instead of subtracting the known leg from $r^2$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Counting Wavelengths Inside a Material](Problem-6.md)

Study guide index: 14/28

---
<!-- lesson-nav:end -->
