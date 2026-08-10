# Classifying a Plane-Mirror Image

<!--
lesson-id: 212-M7-004
topic-code: MTH212.M7.04
-->
## Table of Contents

- [Introduction](#introduction)
- [Place the Image Behind the Mirror](#place-the-image-behind-the-mirror)
- [Classify the Image](#classify-the-image)
- [Audit Every Part of a Description](#audit-every-part-of-a-description)
- [Summary](#summary)

## Prerequisites

- Distinguish a physical light ray from the backward extension of a ray.
- Measure the shortest distance from a point to a flat surface along a perpendicular line.

---

<a id="introduction"></a>
## Introduction

When a problem gives an object in front of a **plane mirror**, use the same four facts every time:

- The image is **virtual**.
- The image is **upright**.
- The image is the **same size** as the object.
- The image appears as far **behind** the mirror as the object is in front.

The recognition cue is the phrase *plane mirror*. Picture the mirror as a line of reflection: each image point lies directly opposite its object point, with the mirror halfway between them. Once that cue appears, classify the image and place it using these fixed properties; the object's particular distance changes only the numerical location.

---

<a id="place-the-image-behind-the-mirror"></a>
## Place the Image Behind the Mirror

**Example:** A coin is $1.5\ \mathrm{m}$ in front of a plane mirror. Where does its image appear?

**Explanation**

For each object point, the mirror plane perpendicularly bisects the segment from that point to its image. If $d_o$ is the object's distance from the mirror and $d_i$ is the image's apparent distance from it, then

$$
d_i=d_o.
$$

The two distances are equal but lie on opposite sides. Since the coin is $1.5\ \mathrm{m}$ in front, its image appears $1.5\ \mathrm{m}$ behind the mirror. The full object-to-image separation is $d_o+d_i=2d_o$, but that doubled distance is not the image's distance from the mirror.

```quiz
type: radio
id: p4-equal-distance
content: |-
  A candle is $0.80\ \mathrm{m}$ in front of a plane mirror. Where does its image appear?
options:
- id: p4-distance-equal-behind
  content: |-
    $0.80\ \mathrm{m}$ behind the mirror
  correct: true
  feedback: |-
    A plane mirror places an image the same perpendicular distance from the mirror as the object, but on the opposite side. The candle is $0.80\ \mathrm{m}$ in front, so its image appears $0.80\ \mathrm{m}$ behind.
- id: p4-distance-double-behind
  content: |-
    $1.60\ \mathrm{m}$ behind the mirror
  feedback: |-
    $1.60\ \mathrm{m}$ is the full separation between the candle and its image: $0.80+0.80\ \mathrm{m}$. Image distance is measured from the mirror itself, so it is $0.80\ \mathrm{m}$ behind the mirror.
- id: p4-distance-equal-front
  content: |-
    $0.80\ \mathrm{m}$ in front of the mirror
  feedback: |-
    Equal distance is only half of the reflection rule; the image must also be on the opposite side of the mirror. An object in front of a plane mirror has its apparent image behind the mirror.
- id: p4-distance-on-mirror
  content: |-
    On the mirror surface
  feedback: |-
    The image lies on the mirror only when the object also lies on it. Here the object is $0.80\ \mathrm{m}$ away, so symmetry places the image $0.80\ \mathrm{m}$ behind the surface.
```

---

<a id="classify-the-image"></a>
## Classify the Image

**Example:** Reflected rays from the top of an arrow reach an observer after spreading apart. Their backward extensions meet behind a plane mirror. Is the image real or virtual, and is it upright or inverted?

**Explanation**

The reflected rays do not actually meet behind the mirror; only their backward extensions do. That makes the image **virtual**. Those extensions preserve which point is the top and which is the bottom, so the image is **upright**. The familiar left-right reversal of a mirror does not make the image vertically inverted.

Keep the labels separate: **virtual** describes how the rays form the image, while **behind the mirror** describes its apparent location. Neither label can replace the other.

```quiz
type: radio
id: p4-type-orientation
content: |-
  Which pair always describes the image of an ordinary object in a plane mirror?
options:
- id: p4-properties-virtual-upright
  content: |-
    Virtual and upright
  correct: true
  feedback: |-
    Reflected rays only appear to originate behind a plane mirror, so the image is virtual. Their backward extensions preserve the object's vertical orientation, so the image is upright.
- id: p4-properties-virtual-inverted
  content: |-
    Virtual and inverted
  feedback: |-
    The rays do only appear to originate behind the mirror, so “virtual” is right. However, a plane mirror preserves top and bottom; apparent left-right reversal is not vertical inversion, so the image is upright.
- id: p4-properties-real-upright
  content: |-
    Real and upright
  feedback: |-
    Upright gives the correct orientation, but a real image requires actual light rays to converge at the image location. Behind a plane mirror only backward ray extensions meet, so the image is virtual.
- id: p4-properties-real-inverted
  content: |-
    Real and inverted
  feedback: |-
    Neither property matches a plane mirror. Actual reflected rays do not converge behind it, making the image virtual, and the reflected construction preserves top and bottom, making the image upright.
```

---

<a id="audit-every-part-of-a-description"></a>
## Audit Every Part of a Description

**Example:** A toy is $3\ \mathrm{m}$ in front of a plane mirror. Which description is complete and correct?

1. virtual, upright, and $3\ \mathrm{m}$ behind the mirror
2. real, upright, and $3\ \mathrm{m}$ behind the mirror
3. virtual, inverted, and $3\ \mathrm{m}$ behind the mirror
4. virtual, upright, and $3\ \mathrm{m}$ in front of the mirror

**Explanation**

Check each choice in three passes, rejecting it as soon as one claim fails:

1. **Type:** virtual.
2. **Orientation:** upright.
3. **Location:** equal distance behind the mirror.

Description 1 passes all three checks. Description 2 fails the ray test, description 3 fails the orientation test, and description 4 fails the opposite-side test. A choice with two correct claims is still wrong if its third claim fails. If no listed description passes all three checks, choose “none of the above.”

```quiz
type: radio
id: p4-compound-audit
content: |-
  An object is $2.4\ \mathrm{m}$ in front of a plane mirror. Its image is
options:
- id: p4-audit-inverted-behind
  content: |-
    virtual, inverted, and $2.4\ \mathrm{m}$ behind the mirror
  feedback: |-
    “Virtual” and “$2.4\ \mathrm{m}$ behind” satisfy the plane-mirror rules, but “inverted” does not. A plane-mirror image preserves top and bottom, so the missing correct description would say upright.
- id: p4-audit-upright-front
  content: |-
    virtual, upright, and $2.4\ \mathrm{m}$ in front of the mirror
  feedback: |-
    The type and orientation are correct, but the side is not. A plane-mirror image appears opposite the object, so an object in front produces an image the equal distance behind the mirror.
- id: p4-audit-real-behind
  content: |-
    real, upright, and $2.4\ \mathrm{m}$ behind the mirror
  feedback: |-
    The orientation and location are correct, but “real” is not. Only backward extensions of the reflected rays meet behind a plane mirror, so the image there is virtual.
- id: p4-audit-none
  content: |-
    None of the above
  correct: true
  feedback: |-
    A plane mirror forms a virtual, upright image the same distance behind the mirror as the object is in front. That full description would be “virtual, upright, and $2.4\ \mathrm{m}$ behind,” and none of the listed descriptions states it.
```

---

<a id="summary"></a>
## Summary

For a plane mirror, use the checklist **V-U-S-E**:

- **V**irtual: actual reflected rays do not meet behind the mirror.
- **U**pright: top and bottom keep their orientation.
- **S**ame size as the object.
- **E**qual perpendicular distance on the opposite side: object in front, image behind.

For a compound answer choice, test type, orientation, and location separately. Select a description only if every part passes; otherwise, “none of the above” may be the correct choice.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
