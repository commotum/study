# Classifying a Lens from a Ray Diagram

<!--
lesson-id: 212-M7-010
topic-code: MTH212.M7.10
-->
## Table of Contents

- [Introduction](#introduction)
- [Follow the Parallel Ray](#follow-the-parallel-ray)
- [Distinguish Actual Rays from Backward Extensions](#distinguish-actual-rays-from-backward-extensions)
- [Confirm the Classification with Both Cues](#confirm-the-classification-with-both-cues)
- [Summary](#summary)

## Prerequisites

- Identify the principal axis and the focal points of a thin lens.
- Follow a ray in its direction of travel through a diagram.
- Distinguish a drawn light ray from a backward extension used to locate a virtual image.

---

<a id="introduction"></a>
## Introduction

When a ray diagram shows a thin lens, classify the lens by what it does to the rays **after** they pass through it.

Use the same scan order every time:

1. Follow the arrow or ray from the object toward the lens.
2. Locate the point where the ray crosses the lens plane.
3. Inspect only the outgoing ray first; use backward extensions only after identifying them as extensions.
4. Match the observed path to a principal-ray rule.

The most useful cue is a ray that arrives parallel to the principal axis:

- A **converging lens** refracts that ray through the focal point on the far side.
- A **diverging lens** refracts that ray away from the axis; its backward extension passes through the focal point on the near side.

Use this decision card to keep ray behavior separate from image classification:

| Diagram cue | What the cue establishes |
| --- | --- |
| Parallel ray leaves through the far focal point | The lens is converging |
| Parallel ray leaves spreading outward and backtracks through the near focal point | The lens is diverging |
| Actual rays meet on the far side for a real object | The image is real and the rays were made to converge |
| Only backward extensions meet | The image is virtual; use a principal-ray cue to settle the lens type |

---

<a id="follow-the-parallel-ray"></a>
## Follow the Parallel Ray

**Example:** A ray travels from left to right, parallel to the principal axis. After crossing a lens, it bends toward the axis and passes through the focal point to the right of the lens. Classify the lens.

**Explanation**

Trace first, then classify: the ray begins parallel to the axis, crosses the lens plane, and leaves through the far focal point. This matches the parallel-ray rule for a converging lens.

The direction in which the line tilts is not enough by itself. The deciding feature is whether the outgoing ray heads through the far focal point or spreads away from the axis as if it came from the near focal point.

```quiz
type: radio
id: p10-q1-parallel-ray
content: |-
  A ray approaches a thin lens parallel to the principal axis. After refraction, the ray spreads away from the axis, and its backward extension passes through the focal point on the incident side. What type of lens is shown?
options:
- id: p10-q1-a
  content: |-
    Diverging
  correct: true
  feedback: |-
    A diverging lens sends a parallel incident ray away from the principal axis. The backward extension through the near focal point identifies the ray's apparent origin, so the lens is diverging.
- id: p10-q1-b
  content: |-
    Converging
  feedback: |-
    A converging lens would send the parallel incident ray through the focal point on the far side. Here the ray spreads outward and only its backward extension reaches the near focal point, which is the diverging-lens pattern.
- id: p10-q1-c
  content: |-
    Either type, because every lens has focal points
  feedback: |-
    Having focal points does not determine the type, but the way the ray uses them does. A parallel ray that diverges and backtracks to the near focal point specifically identifies a diverging lens.
- id: p10-q1-d
  content: |-
    Neither type, because the ray does not cross the axis
  feedback: |-
    A refracted ray need not cross the axis to reveal a valid lens. Spreading away from the axis with a backward extension through the near focal point is exactly the principal-ray rule for a diverging lens.
```

---

<a id="distinguish-actual-rays-from-backward-extensions"></a>
## Distinguish Actual Rays from Backward Extensions

**Example:** A real object is to the left of a lens. Two actual refracted rays intersect to the right of the lens. What does the intersection show?

**Explanation**

Actual rays carry light. When the actual refracted rays physically meet, their intersection is a **real image**. For a single thin lens and a real object, this far-side real image requires a converging lens.

A diverging lens instead spreads the rays after refraction. Their backward extensions may intersect on the object's side, but no actual light passes through that apparent point, so that image is virtual.

This check has a useful boundary condition: a converging lens can also make a virtual image when the object is inside its focal length. Therefore, a virtual image alone does not prove that a lens is diverging; return to the parallel-ray rule if the diagram supplies it.

```quiz
type: radio
id: p10-q2-ray-intersection
content: |-
  A real object is placed to the left of a single thin lens. The actual refracted rays cross to the right of the lens. Which classification matches the diagram?
options:
- id: p10-q2-a
  content: |-
    A converging lens forming a real image
  correct: true
  feedback: |-
    A real image lies where actual refracted rays meet. With a real object and a single lens, an actual far-side intersection means the lens has brought the rays together, so it is converging.
- id: p10-q2-b
  content: |-
    A diverging lens forming a real image
  feedback: |-
    A diverging lens spreads rays from a real object rather than bringing the actual rays to a far-side intersection. Its ordinary image is located by backward extensions on the object's side and is virtual.
- id: p10-q2-c
  content: |-
    A converging lens forming a virtual image
  feedback: |-
    The lens classification is consistent with convergence, but the image classification is not. Because the actual rays cross at the image location, light passes through it and the image is real, not virtual.
- id: p10-q2-d
  content: |-
    The lens type cannot be determined because the rays cross
  feedback: |-
    The crossing is useful evidence when it belongs to the actual refracted rays. Their far-side intersection shows that the lens has made rays from the real object converge, which identifies a converging lens.
```

---

<a id="confirm-the-classification-with-both-cues"></a>
## Confirm the Classification with Both Cues

**Example:** In the Problem 10 diagram, one ray from the top of the object approaches Lens 1 parallel to the principal axis. After refraction it travels through the far focal point $F_1$. A second ray passes through the lens center, and the two actual rays meet at Image 1 on the opposite side.

![](<../Source/2026-08-12-HW-10/Images/thin-lens-ray-trace-distances.png>)

**Explanation**

Apply the same left-to-right scan used in the simpler examples:

1. The parallel incident ray refracts through the far focal point $F_1$.
2. The actual refracted rays meet on the far side at Image 1.

The first observation is the defining principal-ray cue for a converging lens. The second independently confirms that the lens brings these rays to a real image. Thus Lens 1 is converging. The labels $d_0$, $d_1$, and $|f_1|$ are not needed for this qualitative classification.

```quiz
type: radio
id: p10-q3-assignment-diagram
content: |-
  An object is placed a distance $d_0$ from Lens 1, and an image is formed on the opposite side a distance $d_1$ from the lens plane. The focal points $F_1$ and $F_1'$ and the focal-length magnitude $|f_1|$ are also indicated.

  ![](<../Source/2026-08-12-HW-10/Images/thin-lens-ray-trace-distances.png>)

  According to the traced rays, is Lens 1 converging or diverging?
options:
- id: p10-q3-a
  content: |-
    converging
  correct: true
  feedback: |-
    The incident ray parallel to the principal axis refracts through the far focal point $F_1$, which is the converging-lens rule. The actual rays also meet at Image 1 on the opposite side, so Lens 1 is converging.
- id: p10-q3-b
  content: |-
    diverging
  feedback: |-
    A diverging lens would send the parallel incident ray away from the principal axis, with its backward extension passing through the near focal point $F_1'$. Here the ray instead passes through far focal point $F_1$, and the actual rays meet on the far side, so the lens is converging.
```

---

<a id="summary"></a>
## Summary

To classify a thin lens from a ray diagram:

1. Find a ray that arrives parallel to the principal axis.
2. If it leaves through the far focal point, the lens is **converging**.
3. If it leaves spreading outward and backtracks through the near focal point, the lens is **diverging**.
4. Use the ray intersection as a check: actual rays meeting form a real image; only backward extensions meeting form a virtual image.

Do not classify the lens from the ray's slope, the presence of focal-point labels, or the distance labels alone. Follow what the lens actually does to the ray.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
