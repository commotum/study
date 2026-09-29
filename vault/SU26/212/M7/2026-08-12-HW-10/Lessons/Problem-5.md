# Reading Thin-Lens Magnification to Identify the Image and Lens

<!--
lesson-id: 212-M7-005
topic-code: MTH212.M7.05
-->
## Table of Contents

- [Introduction](#introduction)
- [Read the Sign First](#read-the-sign-first)
- [Read the Magnitude Separately](#read-the-magnitude-separately)
- [Use the Object Position to Identify the Lens](#use-the-object-position-to-identify-the-lens)
- [Combine the Cues](#combine-the-cues)
- [Summary](#summary)

## Prerequisites

- Use the real-object sign convention $d_o>0$.
- Recognize that a real image forms on the opposite side of a lens from the object, while a virtual image appears on the object's side.
- Compare a positive number with $1$.

---

<a id="introduction"></a>
## Introduction

When a thin-lens problem gives a signed magnification, treat its **sign** and **magnitude** as two separate clues. For an ordinary real object,

$$
m=\frac{h_i}{h_o}=-\frac{d_i}{d_o}.
$$

The sign identifies orientation and image type:

| Magnification | Orientation | Image type |
|---|---|---|
| $m>0$ | upright | virtual |
| $m<0$ | inverted | real |

The magnitude compares image and object sizes:

| Magnitude | Image size |
|---|---|
| $|m|<1$ | reduced |
| $|m|=1$ | same size |
| $|m|>1$ | enlarged |

Keep $m$ signed until orientation and image type are settled; only then use $|m|$ for size. If the problem also compares $d_o$ with $|f|$, use that condition last to decide which lens can produce the image. The reusable procedure is **sign, size, lens condition**.

---

<a id="read-the-sign-first"></a>
## Read the Sign First

**Example:** A thin lens has magnification $m=-0.80$ for a real object. Determine the image's orientation and whether it is real or virtual.

**Explanation**

The negative sign means the image is inverted. Also, since $d_o>0$ and

$$
m=-\frac{d_i}{d_o}<0,
$$

the image distance must satisfy $d_i>0$. Therefore, the image is real and inverted. The number $0.80$ describes size, but it is not needed for this first classification.

```quiz
type: radio
id: p5-sign-classification
content: |-
  A single thin lens has magnification $m=+1.2$ for a real object. Which description follows from the sign of $m$?
options:
- id: p5-sign-virtual-upright
  content: |-
    The image is virtual and upright.
  correct: true
  feedback: |-
    For a real object, $d_o>0$ and $m=-d_i/d_o$. A positive magnification requires $d_i<0$, so the image is virtual; the positive height ratio means it is upright.
- id: p5-sign-real-upright
  content: |-
    The image is real and upright.
  feedback: |-
    The positive sign does indicate an upright image, but a real image has $d_i>0$ and therefore $m=-d_i/d_o<0$. A positive magnification instead identifies a virtual image for a real object.
- id: p5-sign-virtual-inverted
  content: |-
    The image is virtual and inverted.
  feedback: |-
    A virtual image has $d_i<0$, which makes $m=-d_i/d_o$ positive for a real object. Positive magnification means upright, not inverted; an inverted image would require $m<0$.
- id: p5-sign-real-inverted
  content: |-
    The image is real and inverted.
  feedback: |-
    Real and inverted is the thin-lens combination associated with negative magnification. Here $m$ is positive, so both the image type and orientation must be the opposite: virtual and upright.
```

---

<a id="read-the-magnitude-separately"></a>
## Read the Magnitude Separately

**Example:** A lens produces an image with $m=-0.35$. Compare the image's height and orientation with the object's.

**Explanation**

The sign and magnitude answer different questions. The minus sign makes the image inverted, while

$$
|m|=0.35
$$

means the image height is $0.35$ times the object height. The image is inverted and reduced to $35\%$ of the object's height.

**Watch out:** Replacing $m$ by $|m|$ too early erases the orientation clue. Absolute value is useful for size only after the sign has been interpreted.

```quiz
type: radio
id: p5-magnitude-meaning
content: |-
  A real object has a thin-lens image with $m=+0.60$. Which statement correctly interprets the magnification?
options:
- id: p5-magnitude-upright-reduced
  content: |-
    The image is upright and $0.60$ times as tall as the object.
  correct: true
  feedback: |-
    The positive sign makes the image upright, and $|m|=0.60<1$ makes it reduced. Thus its height is $0.60$ times the object's height.
- id: p5-magnitude-upright-reciprocal
  content: |-
    The image is upright and about $1.67$ times as tall as the object.
  feedback: |-
    This uses the reciprocal $1/0.60$, but magnification already equals the image-to-object height ratio $h_i/h_o$. Therefore $m=0.60$ means the image is $0.60$ times as tall, not $1.67$ times as tall.
- id: p5-magnitude-inverted-reduced
  content: |-
    The image is inverted and $0.60$ times as tall as the object.
  feedback: |-
    The magnitude $0.60$ correctly gives a reduced image, but orientation comes from the sign. Because $m$ is positive, the image is upright; an inverted image would have negative magnification.
- id: p5-magnitude-upright-complement
  content: |-
    The image is upright and $0.40$ times as tall as the object.
  feedback: |-
    Subtracting the magnification from $1$ gives a percent decrease, not the image-to-object height ratio. The ratio itself is $|m|=0.60$, so the image is $0.60$ times as tall.
```

---

<a id="use-the-object-position-to-identify-the-lens"></a>
## Use the Object Position to Identify the Lens

**Example:** A real object is farther from a thin lens than $|f|$, and the measured magnification is positive. Decide whether the lens can be converging.

**Explanation**

A real object's location produces this compact case table:

| Lens and object region | Image | Magnification |
|---|---|---|
| Converging, $d_o>f$ | real and inverted | $m<0$ |
| Converging, $0<d_o<f$ | virtual, upright, and enlarged | $m>1$ |
| Diverging, any $d_o>0$ | virtual, upright, and reduced | $0<m<1$ |

The condition $d_o>|f|$ puts a real object outside the focal length of a converging lens. Such a lens would require negative magnification there. Therefore, positive magnification under this condition rules out a converging lens. A diverging lens is consistent because it forms a virtual, upright, reduced image for a real object.

**Boundary check:** If a real object is exactly at the focal point of a converging lens, $d_o=f$, the outgoing rays are parallel and there is no finite image or finite magnification. A prompt that supplies a finite $m$ is not this boundary case.

**Watch out:** Positive magnification alone does not always identify a diverging lens. A converging lens also has $m>0$ when $d_o<f$; the object-position condition distinguishes those cases.

```quiz
type: radio
id: p5-lens-from-condition
content: |-
  A real object is placed so that $d_o>|f|$. Its image has magnification $m=+0.25$. Which lens type is consistent with both facts?
options:
- id: p5-condition-diverging
  content: |-
    A diverging lens
  correct: true
  feedback: |-
    Positive magnification means a virtual, upright image, and $|m|=0.25<1$ means it is reduced. A diverging lens produces that image for a real object, whereas a converging lens with $d_o>f$ would produce a real, inverted image with $m<0$.
- id: p5-condition-converging-outside
  content: |-
    A converging lens because the object is outside the focal length
  feedback: |-
    An object outside a converging lens's focal length does form an image, but that image is real and inverted, so its magnification is negative. The measured positive, reduced magnification is instead consistent with a diverging lens.
- id: p5-condition-converging-virtual
  content: |-
    A converging lens because positive magnification means a virtual image
  feedback: |-
    A converging lens can make a positive-magnification virtual image only when the real object is inside its focal length, $d_o<f$. The given condition $d_o>|f|$ excludes that case.
- id: p5-condition-either
  content: |-
    Either lens type; the sign of magnification does not help
  feedback: |-
    The sign is decisive when combined with object position. At $d_o>|f|$, a converging lens requires $m<0$, while a diverging lens gives $0<m<1$; the given $m=+0.25$ selects the diverging lens.
```

---

<a id="combine-the-cues"></a>
## Combine the Cues

**Example:** A real object lies farther from a thin lens than $|f|$, and $m=+0.20$. Classify the image and lens.

**Explanation**

Work in a fixed order:

1. **Sign:** $m>0$, so the image is upright and virtual.
2. **Magnitude:** $|m|=0.20<1$, so the image is reduced.
3. **Lens condition:** a converging lens with $d_o>f$ would make a real, inverted image. The lens must therefore be diverging.

The conclusion is a virtual, upright, reduced image made by a diverging lens.

```quiz
type: radio
id: p5-target-check
shuffle: true
content: |-
  An object is placed along the optical axis of a thin lens, farther from the lens than the magnitude of its focal length. The magnification is $+0.4$.

  This means:
options:
- id: p5-target-a
  content: |-
    The image is real and upright, and the lens is a converging lens.
  feedback: |-
    A real image from a single thin lens has $d_i>0$, so $m=-d_i/d_o<0$ and the image is inverted. The given positive magnification instead identifies a virtual, upright image.
- id: p5-target-b
  content: |-
    The image is real and inverted, and the lens is a converging lens.
  feedback: |-
    A converging lens with the object beyond its focal length would indeed make a real, inverted image, but that image would have $m<0$. The measured $m=+0.4$ rules out this otherwise relevant case.
- id: p5-target-c
  content: |-
    The image is virtual and upright, and the lens is a diverging lens.
  correct: true
  feedback: |-
    Positive magnification means upright and virtual, while $|m|=0.4<1$ means reduced. Because the object is farther away than $|f|$, a converging lens could not make this positive-magnification image; a diverging lens gives exactly this combination.
- id: p5-target-d
  content: |-
    The image is virtual and upright, and the lens is a converging lens.
  feedback: |-
    A converging lens makes a virtual, upright image only for a real object inside its focal length, where $d_o<f$. Here the object is explicitly farther away than $|f|$, so the converging-lens virtual case is unavailable.
- id: p5-target-e
  content: |-
    The image is virtual and inverted, and the lens is a diverging lens.
  feedback: |-
    A virtual image has $d_i<0$, making $m=-d_i/d_o>0$ for a real object; that positive magnification means upright. A virtual, inverted pairing would conflict with the thin-lens sign relation.
```

---

<a id="summary"></a>
## Summary

Use **sign, size, lens condition**:

1. Read the sign: $m>0$ means virtual and upright; $m<0$ means real and inverted for a real object.
2. Read the magnitude: $|m|<1$ means reduced, $|m|=1$ means same size, and $|m|>1$ means enlarged.
3. Apply the position condition: a converging lens gives a virtual, upright image only when $d_o<f$; a diverging lens gives a virtual, upright, reduced image for a real object.

The main trap is using only one clue. Positive magnification identifies a virtual, upright image, while the object-position condition distinguishes the lens type.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
