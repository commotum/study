# Inferring Lens Type from a Magnified Image

## Table of Contents

- [Introduction](#introduction)
- [Translate “Larger” into Magnification](#translate-larger-into-magnification)
- [Eliminate a Diverging Lens](#eliminate-a-diverging-lens)
- [Map the Two Magnifying Regions](#map-the-two-magnifying-regions)
- [Make Only the Guaranteed Inference](#make-only-the-guaranteed-inference)
- [Summary](#summary)

## Prerequisites

- Use the real-object convention $d_o>0$.
- Recognize $f>0$ as a converging lens and $f<0$ as a diverging lens.
- Use $m=-d_i/d_o$ and interpret the sign and magnitude of $m$ separately.

---

<a id="introduction"></a>
## Introduction

When a real object is placed in front of one thin lens and the only clue is that the image is **larger**, begin with

$$
|m|>1.
$$

That clue is strong enough to determine the sign of the focal length: a diverging lens cannot magnify a real object, so the lens must be converging and $f>0$.

However, “larger” gives only the **magnitude** of $m$. It does not give the sign of $m$, so it does not by itself decide whether the image is real or virtual. Treat these as two independent classification axes:

- use $|m|$ to classify size;
- use the sign of $m$ (or $d_i$) to classify image type.

A converging lens has two different magnifying regions:

- $0<d_o<f$: virtual, upright, magnified image;
- $f<d_o<2f$: real, inverted, magnified image.

The key is to eliminate the impossible lens type first, then keep every converging-lens case that still fits the evidence.

---

<a id="translate-larger-into-magnification"></a>
## Translate “Larger” into Magnification

**Example:** One image has $m=+1.8$, and another has $m=-1.8$. Which image is larger than its object?

**Explanation**

Image size depends on $|m|$, not on the sign of $m$. Both images have

$$
|m|=1.8>1,
$$

so both are magnified. For a real object, the sign supplies different information:

| Magnification clue | Meaning |
| --- | --- |
| $|m|>1$ | image is larger than the object |
| $m>0$ | image is upright and virtual |
| $m<0$ | image is inverted and real |

Thus “larger” alone does not reveal the image type because it does not distinguish $+1.8$ from $-1.8$.

```quiz
type: radio
id: p6-q1-size-only
content: |-
  A thin lens produces an image with $|m|=2.3$, but the sign of $m$ is not given. What follows from this information alone?
options:
- id: p6-q1-a
  content: |-
    The image is magnified, but it may be real or virtual.
  correct: true
  feedback: |-
    Image size is controlled by $|m|$, so $|m|=2.3>1$ makes the image magnified. Image type depends on the sign of $m$ (or $d_i$), which is missing, so either a real or a virtual image remains possible.
- id: p6-q1-b
  content: |-
    The image is magnified and must be real.
  feedback: |-
    The magnitude $|m|=2.3$ establishes magnification, but a real image would additionally require $m<0$ for a real object. Because the sign is not given, a positive-$m$ virtual image has not been excluded.
- id: p6-q1-c
  content: |-
    The image is magnified and must be virtual.
  feedback: |-
    A virtual image would require $m>0$ for a real object, while the absolute value hides that sign. The image is magnified, but $m=-2.3$ would instead describe a real, inverted image.
- id: p6-q1-d
  content: |-
    Nothing can be inferred about the image size until the sign of $m$ is known.
  feedback: |-
    The sign of $m$ controls orientation and, for a real object, image type; it does not control relative size. Since $|m|=2.3>1$, the image is definitely larger even though its type is undecided.
```

---

<a id="eliminate-a-diverging-lens"></a>
## Eliminate a Diverging Lens

**Example:** A real object is $15\ \mathrm{cm}$ from a lens with $f=-10\ \mathrm{cm}$. Can this diverging lens make a larger image?

**Explanation**

Apply the thin-lens equation:

$$
\frac{1}{d_i}
=\frac{1}{f}-\frac{1}{d_o}
=-\frac{1}{10}-\frac{1}{15}
=-\frac{1}{6},
$$

so $d_i=-6\ \mathrm{cm}$ and

$$
m=-\frac{d_i}{d_o}=+\frac{6}{15}=0.40.
$$

The image is virtual because $d_i<0$, upright because $m>0$, and reduced because $|m|<1$.

This is not a coincidence. Write a diverging focal length as $f=-F$, where $F>0$. Then

$$
d_i=-\frac{Fd_o}{F+d_o}
\qquad\text{and}\qquad
|m|=\frac{F}{F+d_o}<1.
$$

For every real object with $d_o>0$, the denominator $F+d_o$ exceeds $F$. Therefore a single diverging lens always gives a virtual, upright, reduced image. Seeing a larger image rules out $f<0$ immediately.

```quiz
type: radio
id: p6-q2-diverging-check
content: |-
  A real object is placed $24\ \mathrm{cm}$ from a diverging lens with $f=-8\ \mathrm{cm}$. Which result is consistent with the thin-lens equation?
options:
- id: p6-q2-a
  content: |-
    $d_i=-6\ \mathrm{cm}$ and $m=+0.25$: the image is virtual, upright, and reduced.
  correct: true
  feedback: |-
    The lens equation gives $1/d_i=-1/8-1/24=-1/6$, so $d_i=-6\ \mathrm{cm}$. Then $m=-d_i/d_o=+6/24=+0.25$: negative $d_i$ means virtual, positive $m$ means upright, and $|m|<1$ means reduced.
- id: p6-q2-b
  content: |-
    $d_i=-6\ \mathrm{cm}$ and $m=+4$: the image is virtual, upright, and magnified.
  feedback: |-
    The image distance is negative, but this choice reverses the magnification ratio. Magnification is image distance divided by object distance in magnitude, so $|m|=6/24=0.25$, not $24/6=4$; the image is reduced.
- id: p6-q2-c
  content: |-
    $d_i=+6\ \mathrm{cm}$ and $m=-0.25$: the image is real, inverted, and reduced.
  feedback: |-
    With $f<0$ and $d_o>0$, both terms in $1/d_i=1/f-1/d_o$ are negative, so $d_i$ must be negative. A diverging lens therefore makes a virtual image here, not the real image asserted by this option.
- id: p6-q2-d
  content: |-
    $d_i=-12\ \mathrm{cm}$ and $m=+0.50$: the image is virtual, upright, and reduced.
  feedback: |-
    This classification matches a diverging lens, but the numbers do not satisfy the lens equation. The reciprocal calculation gives $1/d_i=-1/6$, so $d_i=-6\ \mathrm{cm}$ and $m=+0.25$ for the stated distances.
```

---

<a id="map-the-two-magnifying-regions"></a>
## Map the Two Magnifying Regions

**Example:** A converging lens has $f=12\ \mathrm{cm}$. Compare an object at $d_o=8\ \mathrm{cm}$ with an object at $d_o=18\ \mathrm{cm}$.

**Explanation**

For the object inside the focal length,

$$
\frac{1}{d_i}=\frac{1}{12}-\frac{1}{8}=-\frac{1}{24},
$$

so $d_i=-24\ \mathrm{cm}$ and $m=+3$. This image is virtual, upright, and magnified.

For the object between $f$ and $2f$,

$$
\frac{1}{d_i}=\frac{1}{12}-\frac{1}{18}=\frac{1}{36},
$$

so $d_i=+36\ \mathrm{cm}$ and $m=-2$. This image is real, inverted, and magnified.

Both placements use the same positive focal length and both produce $|m|>1$. The object distance decides which image type occurs:

| Object position for $f>0$ | Image type | Relative size |
| --- | --- | --- |
| $0<d_o<f$ | virtual and upright | magnified |
| $f<d_o<2f$ | real and inverted | magnified |
| $d_o=2f$ | real and inverted | same size |
| $d_o>2f$ | real and inverted | reduced |

Test the object-distance condition first, then use only the matching row. The set of positions that produce a finite magnified image is the union of two branches:

$$
(0<d_o<f)\quad\text{or}\quad(f<d_o<2f).
$$

The boundaries matter: at $d_o=f$, the emerging rays are parallel and there is no finite image position; at $d_o=2f$, the image is the same size rather than larger.

```quiz
type: radio
id: p6-q3-two-regions
content: |-
  A converging lens has $f=10\ \mathrm{cm}$. One real object is placed at $d_o=6\ \mathrm{cm}$ and another at $d_o=15\ \mathrm{cm}$. Which comparison is correct?
options:
- id: p6-q3-a
  content: |-
    Both images are magnified; the $6\ \mathrm{cm}$ placement gives a virtual image, while the $15\ \mathrm{cm}$ placement gives a real image.
  correct: true
  feedback: |-
    The first object lies inside $f$, so the converging lens gives $d_i<0$ and a virtual magnified image. The second lies between $f$ and $2f$, so it gives $d_i>0$ and a real magnified image; these are the two allowed magnifying regions.
- id: p6-q3-b
  content: |-
    Both images are magnified and real because the focal length is positive.
  feedback: |-
    Positive focal length identifies a converging lens, but image type also depends on object position. The $6\ \mathrm{cm}$ object is inside the $10\ \mathrm{cm}$ focal length, so its magnified image is virtual rather than real.
- id: p6-q3-c
  content: |-
    Both images are magnified and virtual because both objects are closer than $2f$.
  feedback: |-
    Being closer than $2f$ predicts magnification only after the focal point is checked. The $15\ \mathrm{cm}$ object lies beyond $f=10\ \mathrm{cm}$, so its rays converge to a real image; only the $6\ \mathrm{cm}$ placement is virtual.
- id: p6-q3-d
  content: |-
    Only the $6\ \mathrm{cm}$ placement is magnified; the $15\ \mathrm{cm}$ placement is reduced.
  feedback: |-
    A converging lens reduces a real image only when $d_o>2f$. Here $15\ \mathrm{cm}$ lies between $f=10\ \mathrm{cm}$ and $2f=20\ \mathrm{cm}$, so that real image is magnified, just as the inside-$f$ virtual image is.
```

---

<a id="make-only-the-guaranteed-inference"></a>
## Make Only the Guaranteed Inference

**Example:** A real object in front of an unknown thin lens forms an image twice as tall as the object. No orientation, image distance, or screen information is provided. What can be concluded?

**Explanation**

Use an evidence ladder:

1. “Twice as tall” means $|m|=2>1$.
2. A diverging lens would require $|m|<1$, so eliminate $f<0$.
3. Therefore $f>0$.
4. The missing sign of $m$ leaves both magnifying branches available: $0<d_o<f$ gives a virtual image, while $f<d_o<2f$ gives a real image.
5. Exclude the boundaries: $d_o=f$ gives no finite image, and $d_o=2f$ gives $|m|=1$.

Do not promote a possibility into a certainty. Magnification alone guarantees a converging lens, but it does not guarantee one image type.

```quiz
type: radio
id: p6-q4-guaranteed-inference
shuffle: true
content: |-
  An object is placed in front of a thin glass lens. The image formed by the lens is larger than the object.

  Which statement is correct, consistent with the sign convention used in the thin-lens equation?
options:
- id: p6-q4-a
  content: |-
    The focal length is positive and the image could be either virtual or real.
  correct: true
  feedback: |-
    A magnified image of a real object requires a converging lens, so $f>0$. That lens gives a magnified virtual image when $d_o<f$ and a magnified real image when $f<d_o<2f$, so either image type is possible.
- id: p6-q4-b
  content: |-
    The focal length is negative and the image must be virtual.
  feedback: |-
    A negative focal length identifies a diverging lens. Although its image of a real object is virtual, that image always has $|m|<1$, so it cannot satisfy the stated magnification.
- id: p6-q4-c
  content: |-
    The focal length is positive and the image must be real.
  feedback: |-
    Positive focal length is required, but a converging lens also produces a magnified virtual image when $d_o<f$. Without an orientation or image-distance clue, the image need not be real.
- id: p6-q4-d
  content: |-
    The focal length may be either positive or negative and the image must be virtual.
  feedback: |-
    A diverging lens with a real object cannot produce $|m|>1$, so a negative focal length is excluded. The surviving positive-focal-length lens can make either a virtual or a real magnified image, depending on $d_o$.
- id: p6-q4-e
  content: |-
    The lens could be either converging or diverging. If it is converging, the image is real. If it is diverging, the image is virtual.
  feedback: |-
    This choice assigns image type from lens type alone and overlooks size. A diverging lens cannot magnify a real object, while a converging lens can magnify in both its inside-$f$ virtual region and its between-$f$-and-$2f$ real region.
```

---

<a id="summary"></a>
## Summary

When a single thin lens makes a larger image of a real object:

1. Translate “larger” as $|m|>1$.
2. Eliminate a diverging lens because $f<0$ always gives $0<m<1$ for a real object.
3. Conclude that the lens is converging, so $f>0$.
4. Keep both magnifying regions unless another clue is supplied:
   - $d_o<f$: virtual, upright, magnified;
   - $f<d_o<2f$: real, inverted, magnified.

The main trap is treating **magnified** as a synonym for **real**. Size comes from $|m|$; real versus virtual comes from the sign of $m$ or $d_i$.
