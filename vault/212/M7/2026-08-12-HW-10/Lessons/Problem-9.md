# Why Convex-Mirror Images Are Always Virtual

## Table of Contents

- [Introduction](#introduction)
- [Read the Diverging-Ray Pattern](#read-the-diverging-ray-pattern)
- [Use Backward Extensions to Locate the Image](#use-backward-extensions-to-locate-the-image)
- [Check Every Real-Object Distance](#check-every-real-object-distance)
- [Separate Image Type From Size](#separate-image-type-from-size)
- [Apply the Universal Rule](#apply-the-universal-rule)
- [Summary](#summary)

## Prerequisites

- Distinguish a real object in front of a mirror from an image behind it.
- Recognize the principal axis and focal point of a spherical mirror.
- Know that light follows the reflected rays, not their backward extensions.

---

<a id="introduction"></a>
## Introduction

The recognition cue is a **real object in front of a convex mirror**. A convex mirror is a diverging mirror: after reflection, neighboring rays spread apart on the object's side of the mirror.

Use this rule:

> If the reflected rays diverge and only their backward extensions meet behind the mirror, the image is virtual.

This gives a two-case image test:

| What meets at the image point? | Image type |
|---|---|
| Physical reflected rays | Real |
| Only backward extensions of reflected rays | Virtual |

For a convex mirror, that pattern occurs for every real-object distance. The distance changes where the image appears, but it does not change the image from virtual to real.

---

<a id="read-the-diverging-ray-pattern"></a>
## Read the Diverging-Ray Pattern

**Example:** A ray from the top of a real object travels parallel to the principal axis and strikes a convex mirror. What does the reflected ray do?

**Explanation**

A parallel incident ray reflects outward. Its reflected path points away from the axis, but its backward extension passes through the focal point $F$ behind the mirror. The ray does not actually travel through $F$.

This is the crucial geometry: the physical reflected ray remains in front of the mirror and diverges, while the dashed backward extension identifies where the ray appears to have come from.

```quiz
type: radio
id: p9-diverging-ray-cue
content: |-
  A ray approaches a convex mirror parallel to the principal axis. Which description of the reflected ray is correct?
options:
- id: p9-diverges-as-if-from-focus
  content: |-
    It diverges and appears to come from the focal point behind the mirror.
  correct: true
  feedback: |-
    A convex mirror is a diverging mirror. A parallel incident ray reflects outward, and extending that reflected ray backward places its apparent origin at the focal point behind the mirror.
- id: p9-passes-through-focus
  content: |-
    It physically passes through the focal point behind the mirror.
  feedback: |-
    The focal point of a convex mirror is behind the reflecting surface, where the reflected ray does not travel. Only the ray's backward extension passes through that point; the physical ray diverges in front of the mirror.
- id: p9-converges-in-front
  content: |-
    It bends toward the axis and passes through a focal point in front of the mirror.
  feedback: |-
    Convergence toward a front-side focus is the parallel-ray rule for a concave mirror. A convex mirror has its focal point behind the mirror and sends the reflected ray outward instead.
- id: p9-continues-into-mirror
  content: |-
    It continues straight through the mirror along the same horizontal line.
  feedback: |-
    A mirror reflects rather than transmits the incident ray. The parallel direction selects a principal-ray rule: after striking a convex mirror, the ray reflects outward as if it originated at the back-side focus.
```

---

<a id="use-backward-extensions-to-locate-the-image"></a>
## Use Backward Extensions to Locate the Image

**Example:** Two rays from the top of a real object reflect from a convex mirror and spread apart. Their backward extensions intersect behind the mirror. Is the image real or virtual?

**Explanation**

An image is **real** only where physical rays actually meet. Here the reflected rays move apart, so no light reaches the point behind the mirror. An observer traces the rays backward and perceives them as coming from that point. The image is therefore virtual.

The test is about the physical rays:

$$
\begin{aligned}
\text{physical rays meet} &\Longrightarrow \text{real image},\\
\text{only backward extensions meet} &\Longrightarrow \text{virtual image}.
\end{aligned}
$$

```quiz
type: radio
id: p9-real-versus-virtual-test
content: |-
  Reflected rays from a mirror do not meet, but their backward extensions intersect behind the mirror. What kind of image is located there?
options:
- id: p9-virtual-backward-extensions
  content: |-
    A virtual image
  correct: true
  feedback: |-
    Image type is decided by whether physical light reaches the image point. Only backward extensions intersect behind this mirror, so the apparent image at that intersection is virtual.
- id: p9-real-reflected-light
  content: |-
    A real image, because the rays were produced by reflection
  feedback: |-
    Reflection produces real light rays, but that fact does not make their image real. A real image requires those physical reflected rays to converge at the image point; here only their backward extensions meet.
- id: p9-real-behind-mirror
  content: |-
    A real image, because the intersection is behind the mirror
  feedback: |-
    Location alone is not the definition of a real image. No reflected light passes behind an ordinary mirror to reach this intersection, so the back-side intersection of extensions is virtual.
- id: p9-no-image
  content: |-
    No image, because the reflected rays never cross
  feedback: |-
    Physical crossing is required for a real image, not for every image. The backward extensions have a common apparent origin, so an observer sees a virtual image even though the reflected rays diverge.
```

---

<a id="check-every-real-object-distance"></a>
## Check Every Real-Object Distance

**Example:** Could moving a real object closer to a convex mirror eventually make its image real?

**Explanation**

No. Moving the object changes the angles of the incident rays and shifts the virtual image, but the convex surface still makes the reflected rays diverge.

The mirror equation confirms the same conclusion. With the usual mirror sign convention, a real object has $d_o>0$ and a convex mirror has $f<0$:

$$
\frac{1}{f}=\frac{1}{d_o}+\frac{1}{d_i}
\quad\Longrightarrow\quad
\frac{1}{d_i}=\frac{1}{f}-\frac{1}{d_o}.
$$

Both terms on the right are negative, so $d_i<0$ for every $d_o>0$. A negative image distance places the image behind the mirror, where it is virtual.

The familiar “inside versus outside the focal point” switch applies to a **concave** mirror, whose reflected rays can converge. A convex mirror has a virtual focal point behind the surface, so no real-object position makes its reflected rays converge.

```quiz
type: radio
id: p9-object-distance-invariance
content: |-
  A real object is moved from far away to very close to a convex mirror. Which image property remains unchanged throughout the motion?
options:
- id: p9-always-virtual
  content: |-
    The image remains virtual.
  correct: true
  feedback: |-
    A convex mirror keeps the reflected rays divergent for every real-object distance. Their backward extensions, rather than the rays themselves, locate the image behind the mirror, so the image remains virtual as the object moves.
- id: p9-always-same-position
  content: |-
    The image remains at the same position.
  feedback: |-
    Object distance changes the reflected-ray angles and therefore changes where their backward extensions intersect. Virtuality remains fixed, but the image position shifts behind the mirror.
- id: p9-becomes-real-inside-focus
  content: |-
    The image becomes real when the object is closer than the focal-length magnitude.
  feedback: |-
    The inside-the-focus switch belongs to a concave mirror, which can converge reflected rays. A convex mirror stays diverging; with $f<0$ and $d_o>0$, the mirror equation always gives $d_i<0$, so its image stays virtual.
- id: p9-becomes-real-far-away
  content: |-
    The image becomes real when the object is sufficiently far away.
  feedback: |-
    Increasing object distance moves the image toward the focal point, but it does not reverse the reflected rays from divergence to convergence. Even for a very distant real object, the convex-mirror image is virtual.
```

---

<a id="separate-image-type-from-size"></a>
## Separate Image Type From Size

**Example:** A convex-mirror image is upright and smaller than its real object. Which fact determines that the image is virtual: its orientation, its size, or the ray intersection?

**Explanation**

The ray intersection determines image type. For a real object, a convex mirror also produces an upright, reduced image behind the mirror, but those are separate properties:

| Property | Convex-mirror result for a real object | Deciding cue |
|---|---|---|
| Type | Virtual | Only backward extensions meet |
| Orientation | Upright | Magnification is positive |
| Size | Reduced | $0<m<1$ |
| Location | Behind the mirror | $d_i<0$ |

Do not answer a question about **real versus virtual** by using only a statement about **magnified versus reduced**.

```quiz
type: radio
id: p9-separate-image-properties
content: |-
  A convex mirror forms a smaller image of a real object. Which observation directly establishes that the image is virtual?
options:
- id: p9-only-extensions-meet
  content: |-
    Only the backward extensions of the reflected rays meet at the image location.
  correct: true
  feedback: |-
    Image type depends on whether physical rays reach the image point. Since only backward extensions meet, the image is virtual; its reduced size is an additional property, not the defining test.
- id: p9-image-smaller
  content: |-
    The image is smaller than the object.
  feedback: |-
    Smaller size establishes reduced magnification, not image type. Real images can also be reduced; virtuality here follows because the physical reflected rays diverge and only their backward extensions meet.
- id: p9-image-upright
  content: |-
    The image is upright.
  feedback: |-
    Upright orientation is consistent with this convex-mirror image, but orientation and image type are distinct labels. The decisive evidence for a virtual image is that no physical reflected rays pass through the image point.
- id: p9-image-behind
  content: |-
    The image is drawn behind the mirror.
  feedback: |-
    A back-side location is a useful cue under the usual mirror setup, but the physical reason is more precise: only backward extensions can intersect there because the reflected rays remain in front of the mirror.
```

---

<a id="apply-the-universal-rule"></a>
## Apply the Universal Rule

**Example:** Complete the statement: “The images of real objects formed by convex mirrors ____.”

**Explanation**

First translate the setup:

1. **real objects** gives $d_o>0$;
2. **convex mirrors** gives a diverging reflected-ray pattern and $f<0$;
3. therefore only backward extensions meet, so $d_i<0$ and the images are always virtual.

Then audit each proposed property against its own deciding test:

| Proposed description | Deciding test | Verdict |
|---|---|---|
| May be real or virtual | Do physical reflected rays ever converge? | No; they always diverge. |
| May be magnified or demagnified | Can the magnification cross $m=1$? | No; for real objects, $0<m<1$. |
| Always virtual | Do only backward extensions meet? | Yes. |
| Always magnified | Is $m>1$? | No; the image is reduced. |

The word **always** is justified by the unchanging divergence pattern for the full condition $d_o>0$, not by one special object placement.

```quiz
type: radio
id: p9-target-convex-mirror-images
shuffle: true
content: |-
  The images of real objects formed by convex mirrors
options:
- id: p9-target-real-or-virtual
  content: |-
    may be either real or virtual
  feedback: |-
    A switch between real and virtual images requires the reflected rays to switch between convergence and divergence. A convex mirror keeps them divergent for every real-object distance, so only backward extensions form the image and it never becomes real.
- id: p9-target-magnified-or-demagnified
  content: |-
    may be either magnified or demagnified
  feedback: |-
    This choice varies image size, but a convex mirror does not cross a magnification threshold for real objects. Its image lies behind the mirror and is reduced; more importantly for image type, it is formed by backward extensions and remains virtual.
- id: p9-target-always-virtual
  content: |-
    are always virtual
  correct: true
  feedback: |-
    A convex mirror makes reflected rays diverge for every real-object position. Because only their backward extensions intersect behind the mirror, every resulting image is virtual.
- id: p9-target-always-magnified
  content: |-
    are always magnified
  feedback: |-
    Convex-mirror images of real objects are reduced rather than magnified. Their virtual type follows separately from the diverging reflected rays whose backward extensions meet behind the mirror.
```

---

## Summary

When the prompt says **real object + convex mirror**, use this checklist:

1. A convex mirror makes reflected rays diverge.
2. Extend those rays backward behind the mirror to locate their apparent intersection.
3. Because no physical reflected ray reaches that point, the image is virtual.
4. Changing the real-object distance changes image location and size, not image type.

The reusable conclusion is:

$$
\boxed{\text{A convex mirror always forms a virtual image of a real object.}}
$$
