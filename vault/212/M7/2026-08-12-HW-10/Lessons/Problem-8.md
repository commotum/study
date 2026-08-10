# Classifying Images Formed by Thin Lenses

<!--
lesson-id: 212-M7-008
topic-code: MTH212.M7.08
-->
## Table of Contents

- [Introduction](#introduction)
- [Run the Lens Decision](#run-the-lens-decision)
- [Use the Region Between \(f\) and \(2f\)](#use-the-region-between-f-and-2f)
- [Cross Inside the Focal Point](#cross-inside-the-focal-point)
- [Use the Diverging-Lens Invariant](#use-the-diverging-lens-invariant)
- [Test Each Statement Independently](#test-each-statement-independently)
- [Summary](#summary)

## Prerequisites

- Recognize a converging lens and a diverging lens.
- Read the real-object distance $s$ relative to the positive focal-length magnitude $f$.
- Recall that a real image is formed where outgoing rays actually meet, while a virtual image is formed where their backward extensions meet.

---

<a id="introduction"></a>
## Introduction

When a real object is placed in front of one thin lens, the fastest classification comes from two cues:

1. Is the lens **converging** or **diverging**?
2. If it is converging, is the object outside or inside the focal point?

Use this decision map before thinking about image size:

| Lens and real-object position | Ray behavior | Image type | Orientation |
|---|---|---|---|
| Converging, $s>f$ | Outgoing rays meet | Real | Inverted |
| Converging, $0<s<f$ | Only backward extensions meet | Virtual | Upright |
| Diverging, any $s>0$ | Outgoing rays spread apart | Virtual | Upright |

The boundary $s=f$ is special: the rays emerge parallel, so there is no image at a finite distance. The mark $2f$ refines the image's size and location, but it does not change the real/inverted classification on the $s>f$ side.

---

<a id="run-the-lens-decision"></a>
## Run the Lens Decision

**Example:** A real object is placed at $s=3f$ in front of a converging lens. Classify the image as real or virtual and upright or inverted.

**Explanation**

The lens is converging, so compare $s$ with $f$. Since $3f>f$, the object lies outside the focal point. The refracted rays actually meet on the far side of the lens, making the image **real**. A real image made by one converging lens from a real object is **inverted**.

```quiz
type: radio
id: p8-lens-decision
content: |-
  A real object is placed at $s=4f$ in front of a converging lens. Which pair correctly classifies the image?
options:
- id: real-inverted
  content: |-
    Real and inverted
  correct: true
  feedback: |-
    A converging lens makes its outgoing rays meet when the real object is outside the focal point. Here $4f>f$, so the image is real; that real image is inverted.
- id: real-upright
  content: |-
    Real and upright
  feedback: |-
    The rays do meet, so “real” is correct, but the orientation is not. For one converging lens with a real object at $s>f$, the real image is inverted; an upright image occurs when the object is inside $f$ and the image is virtual.
- id: virtual-upright
  content: |-
    Virtual and upright
  feedback: |-
    This pair belongs to a converging lens with $0<s<f$. Because $4f>f$, the outgoing rays actually meet, so the image is real and inverted.
- id: virtual-inverted
  content: |-
    Virtual and inverted
  feedback: |-
    The image is not virtual because a converging lens actually brings the rays together for $s>f$. In addition, the virtual image produced by a single thin lens from a real object is upright, not inverted.
```

---

<a id="use-the-region-between-f-and-2f"></a>
## Use the Region Between \(f\) and \(2f\)

**Example:** A real object is placed at $s=1.5f$ in front of a converging lens. Describe the image.

**Explanation**

First, $1.5f>f$, so the image is **real and inverted**. Next, the object lies between $f$ and $2f$. In this region the image forms beyond $2f$ on the opposite side of the lens and is magnified.

Thus,

$$
f<s<2f
\quad\Longrightarrow\quad
\text{real, inverted, magnified image beyond }2f.
$$

**Boundary check:** At $s=2f$, the image is at $2f$ and has the same size as the object. At $s=f$, the image is not at a finite distance. Because “between” means the strict interval $f<s<2f$, neither boundary case applies.

```quiz
type: radio
id: p8-between-f-and-2f
content: |-
  A real object is placed at $s=1.25f$ in front of a converging lens. Which description is correct?
options:
- id: real-inverted-magnified
  content: |-
    The image is real, inverted, magnified, and beyond $2f$.
  correct: true
  feedback: |-
    Since $1.25f$ lies between $f$ and $2f$, a converging lens brings the rays together beyond $2f$. The image is therefore real, inverted, and magnified.
- id: real-inverted-reduced
  content: |-
    The image is real, inverted, reduced, and between $f$ and $2f$.
  feedback: |-
    This reverses the two outside-focus regions. A reduced image between $f$ and $2f$ occurs when the object is beyond $2f$; an object between $f$ and $2f$ produces a magnified image beyond $2f$.
- id: virtual-upright-magnified
  content: |-
    The image is virtual, upright, magnified, and on the object's side.
  feedback: |-
    That description applies when the object is inside the focal point, $0<s<f$. Here $1.25f>f$, so the rays actually meet and form a real, inverted image.
- id: real-inverted-same-size
  content: |-
    The image is real, inverted, the same size, and at $2f$.
  feedback: |-
    Equal size at $2f$ is the boundary case $s=2f$. Because $1.25f$ is strictly between $f$ and $2f$, the image is magnified and lies beyond $2f$.
- id: no-finite-image
  content: |-
    There is no image at a finite distance.
  feedback: |-
    Parallel outgoing rays, and thus no finite image, occur only at $s=f$. Here $s=1.25f>f$, so the rays meet at a finite point beyond $2f$.
```

---

<a id="cross-inside-the-focal-point"></a>
## Cross Inside the Focal Point

**Example:** A real object is moved to $s=0.75f$ in front of the same converging lens. Describe the image.

**Explanation**

Now $s<f$. The rays leaving the lens still spread apart, but an observer can trace them backward to a common point on the object's side. Because only the backward extensions meet, the image is **virtual**. It is also **upright and magnified**.

This change across $s=f$ is why a converging lens can make both real and virtual images of real objects.

```quiz
type: radio
id: p8-inside-focus
content: |-
  A real object is placed at $s=0.60f$ in front of a converging lens. Which description is correct?
options:
- id: virtual-upright-magnified
  content: |-
    Virtual, upright, and magnified on the object's side
  correct: true
  feedback: |-
    With a converging lens and $0<s<f$, the outgoing rays do not actually meet; their backward extensions meet on the object's side. The image is therefore virtual, upright, and magnified.
- id: real-inverted-magnified
  content: |-
    Real, inverted, and magnified on the opposite side
  feedback: |-
    A real, inverted image requires the real object to be outside the focal point. Here $0.60f<f$, so the outgoing rays diverge and only their backward extensions form a virtual, upright image.
- id: virtual-inverted-magnified
  content: |-
    Virtual, inverted, and magnified on the object's side
  feedback: |-
    The image is virtual and magnified, but its orientation is upright. In this inside-focus case, tracing the diverging rays backward preserves the object's orientation rather than flipping it.
- id: real-upright-magnified
  content: |-
    Real, upright, and magnified on the opposite side
  feedback: |-
    “Real” would require the outgoing rays themselves to meet. At $s<f$ they spread apart, so only a virtual image appears on the object's side, and that image is upright.
- id: no-finite-image
  content: |-
    No image at a finite distance
  feedback: |-
    No finite image is the exact boundary case $s=f$. Since $0.60f<f$, the backward ray extensions meet at a finite virtual-image location.
```

---

<a id="use-the-diverging-lens-invariant"></a>
## Use the Diverging-Lens Invariant

**Example:** A real object is placed in front of a diverging lens. Can moving the object make the image inverted?

**Explanation**

No. A diverging lens spreads the outgoing rays for every real-object position. Their backward extensions meet between the lens and its focal point, so the image is always **virtual, upright, and reduced**. Moving the real object changes the exact image location and size, but it does not change those three properties.

Once the lens is identified as diverging and the object is real, there is no focal-region split to check.

```quiz
type: radio
id: p8-diverging-invariant
content: |-
  A real object is moved from far away to close to a diverging lens. Which property set remains true throughout the motion?
options:
- id: virtual-upright-reduced
  content: |-
    Virtual, upright, and reduced
  correct: true
  feedback: |-
    A diverging lens makes the outgoing rays spread for every real-object distance. Their backward extensions meet between the lens and its focal point, so the image remains virtual, upright, and reduced.
- id: real-inverted-reduced
  content: |-
    Real, inverted, and reduced
  feedback: |-
    A real image requires the outgoing rays to meet, but a diverging lens keeps them spreading for a real object. Only their backward extensions meet, producing a virtual, upright image.
- id: virtual-inverted-reduced
  content: |-
    Virtual, inverted, and reduced
  feedback: |-
    “Virtual” and “reduced” fit a diverging lens, but “inverted” does not. Backward extensions of the diverging rays form an upright image for every real-object position.
- id: virtual-upright-magnified
  content: |-
    Virtual, upright, and magnified
  feedback: |-
    A diverging lens does make a virtual, upright image, but for a real object the image lies between the lens and the focal point and is smaller than the object, not magnified.
- id: changes-type
  content: |-
    It changes between real/inverted and virtual/upright as the object crosses $f$.
  feedback: |-
    Crossing a positive focal point changes the behavior of a converging lens. A diverging lens has no real-object region in which its outgoing rays converge, so its image stays virtual, upright, and reduced.
```

---

<a id="test-each-statement-independently"></a>
## Test Each Statement Independently

**Example:** Decide which claims are true.

1. A converging lens with a real object at $s=2.5f$ makes a real, inverted image.
2. A converging lens with a real object at $s=0.5f$ makes a real image.
3. A diverging lens makes an upright image of a real object.

Evaluate each claim through the same short chain:

$$
\text{lens type}
\;\longrightarrow\;
\text{object region}
\;\longrightarrow\;
\text{ray behavior}
\;\longrightarrow\;
\text{image properties}.
$$

| Claim | Lens and object region | Result | Verdict |
|---|---|---|---|
| 1 | Converging, $2.5f>f$ | Real and inverted | True |
| 2 | Converging, $0.5f<f$ | Virtual and upright | False |
| 3 | Diverging, real object | Virtual, upright, and reduced | True |

Claims 1 and 3 are true. Do not stop after finding one true claim: a select-all prompt can have any number of correct responses, so give each statement its own verdict before choosing the final combination.

```quiz
type: radio
id: p8-homework-style-check
shuffle: true
content: |-
  Which of the following statements are true?

  I. A converging lens can produce both real and virtual images of real objects.

  II. An object placed at position $s$ between $f$ and $2f$ from the lens plane of a converging lens will produce a real, inverted image.

  III. A diverging lens can produce both upright and inverted images of real objects.
options:
- id: i-and-ii
  content: |-
    I and II only
  correct: true
  feedback: |-
    Statement I is true because a converging lens gives a real image for $s>f$ and a virtual image for $s<f$. Statement II is true because $f<s<2f$ is outside the focal point, so the image is real and inverted. Statement III is false because a diverging lens gives an upright image for every real-object position.
- id: i-only
  content: |-
    I only
  feedback: |-
    Statement I is true, but Statement II is also true. The condition $f<s<2f$ still has $s>f$, so a converging lens forms a real, inverted image; the $2f$ boundary changes size and location, not that classification.
- id: ii-only
  content: |-
    II only
  feedback: |-
    Statement II is true, but Statement I is also true. Moving a real object across the focal point of a converging lens changes the image from real and inverted at $s>f$ to virtual and upright at $s<f$.
- id: iii-only
  content: |-
    III only
  feedback: |-
    Statement III is false because a diverging lens keeps the outgoing rays spreading and therefore forms an upright virtual image for every real-object position. Statements I and II both follow from the converging-lens focal-point rule.
- id: all-three
  content: |-
    I, II, and III
  feedback: |-
    Statements I and II are true, but Statement III is not. Changing a real object's distance from a diverging lens changes the image's size and position, not its upright orientation.
```

---

<a id="summary"></a>
## Summary

For a real object, use this checklist:

1. **Classify the lens.** A diverging lens always gives a virtual, upright, reduced image.
2. **For a converging lens, compare $s$ with $f$.** Outside $f$ means real and inverted; inside $f$ means virtual, upright, and magnified.
3. **Use $2f$ only to refine size and location.** In particular, $f<s<2f$ gives a magnified real image beyond $2f$.
4. **Respect the boundary.** At $s=f$, the image is at infinity rather than at a finite location.
5. **On select-all questions, test every statement independently.** One true statement does not rule out another.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
