# Tracing a Parallel Ray Through a Converging Lens

## Table of Contents

- [Introduction](#introduction)
- [Locate the Near and Far Sides](#locate-the-near-and-far-sides)
- [Reverse the Travel Direction](#reverse-the-travel-direction)
- [Join the Lens Point to the Far Focus](#join-the-lens-point-to-the-far-focus)
- [Keep the Reverse Rule Separate](#keep-the-reverse-rule-separate)
- [Choose the Labeled Path](#choose-the-labeled-path)
- [Summary](#summary)

## Prerequisites

- Identify the optical axis and the two focal points of a thin lens.
- Follow a ray's arrow to distinguish the incident side from the outgoing side.
- Recognize the symbol for a converging lens.

---

<a id="introduction"></a>
## Introduction

The recognition cue is an incident ray that reaches a **converging lens parallel to the optical axis**. For this principal ray, use one rule:

> A ray parallel to the optical axis refracts through the focal point on the far side of a converging lens.

In shorthand,

$$
\text{parallel in}\quad\longrightarrow\quad\text{far focus out}.
$$

The far side means the side the light travels into after crossing the lens. It is determined by the ray's direction of travel, not by memorizing “left” or “right.”

Here, **parallel** describes the ray's direction. The ray can be above or below the optical axis without lying on it; if the two lines point in the same direction and never meet, the parallel-ray rule applies.

---

<a id="locate-the-near-and-far-sides"></a>
## Locate the Near and Far Sides

**Example:** Light travels from left to right toward a converging lens. A horizontal incident ray lies above the optical axis. Which focal point controls its outgoing path?

**Explanation**

The arrow of travel points toward the right, so the right side is the outgoing, or far, side. The ray therefore refracts toward the right-hand focal point. The focal point on the left is on the incident side and does not control this outgoing ray.

```quiz
type: radio
id: p7-identify-far-focus
content: |-
  Light travels from left to right through a converging lens. A ray arrives parallel to the optical axis. Which point must the refracted ray pass through?
options:
- id: p7-far-right-focus
  content: |-
    The focal point to the right of the lens
  correct: true
  feedback: |-
    A parallel incident ray through a converging lens refracts through the focal point on the outgoing side. Since the light travels left to right, the right-hand focal point is the far focus and fixes the refracted path.
- id: p7-near-left-focus
  content: |-
    The focal point to the left of the lens
  feedback: |-
    The left-hand focal point is on the incident side. An incoming ray aimed through that near focus would emerge parallel, but a ray that is already parallel must leave through the focal point on the right.
- id: p7-lens-center
  content: |-
    The center of the lens
  feedback: |-
    Passing through the lens center is a different principal-ray condition: that ray continues approximately straight. This incident ray is identified by being parallel to the axis, so its outgoing path is controlled by the far focal point.
- id: p7-object-top
  content: |-
    The top of the object
  feedback: |-
    The object top identifies where the incident ray originated, not where it goes after refraction. Once the ray reaches the converging lens parallel to the axis, the far focal point determines its outgoing direction.
```

---

<a id="reverse-the-travel-direction"></a>
## Reverse the Travel Direction

**Example:** A horizontal ray approaches a converging lens from the right and travels toward the left. Which focal point must the refracted ray cross?

**Explanation**

The optical rule has not changed; only the direction of travel has. Because the ray crosses the lens from right to left, the left side is now the outgoing side. The ray therefore leaves the lens through the left-hand focal point.

This check prevents a common shortcut error: the far focus is not always the right-hand focus.

```quiz
type: radio
id: p7-reverse-direction
content: |-
  A ray travels from right to left and reaches a converging lens parallel to the optical axis. Which description gives the refracted path?
options:
- id: p7-reverse-left-focus
  content: |-
    It leaves on the left and passes through the left-hand focal point.
  correct: true
  feedback: |-
    A parallel incident ray through a converging lens refracts through the far focus. With travel from right to left, the outgoing side and far focal point are both on the left, so the refracted ray passes through the left-hand focus.
- id: p7-reverse-right-focus
  content: |-
    It leaves on the left but passes through the right-hand focal point.
  feedback: |-
    The right-hand focal point is on the incident side in this orientation. “Far” follows the direction of light: for right-to-left travel, the refracted segment lies on the left and must pass through the left-hand focal point.
- id: p7-reverse-stays-horizontal
  content: |-
    It leaves on the left and remains parallel to the optical axis.
  feedback: |-
    Remaining parallel is the outgoing result for a ray aimed through the near focal point. This ray is parallel before reaching the lens, so it must bend through the focal point on the outgoing, left-hand side.
- id: p7-reverse-through-center
  content: |-
    It bends toward the center of the lens and then stops there.
  feedback: |-
    The ray has already reached the lens at its own contact point and continues through it; the lens center is not an endpoint. The parallel-input rule instead fixes the outgoing line through the far, left-hand focal point.
```

---

<a id="join-the-lens-point-to-the-far-focus"></a>
## Join the Lens Point to the Far Focus

**Example:** A parallel ray strikes a converging lens at a point above the optical axis. How should its refracted segment be drawn?

**Explanation**

Mark the exact point where the incident ray meets the lens. Then draw a straight outgoing segment from that point through the far focal point. Because the lens-contact point is above the axis and the far focus lies on the axis, the outgoing ray slopes toward the axis.

Do not redraw the ray from the lens center. Refraction changes the ray's direction at the point where that ray actually reaches the lens.

```quiz
type: radio
id: p7-construct-outgoing-segment
content: |-
  A horizontal ray traveling left to right strikes a converging lens above the optical axis. Which construction gives its refracted path?
options:
- id: p7-hit-point-to-far-focus
  content: |-
    Start at the ray's lens-contact point and draw through the right-hand focal point.
  correct: true
  feedback: |-
    The ray is parallel on arrival, so the converging-lens rule sends it through the far focus. Starting at its actual lens-contact point and joining that point to the right-hand focus gives the unique outgoing line.
- id: p7-center-to-far-focus
  content: |-
    Start at the center of the lens and draw through the right-hand focal point.
  feedback: |-
    The far focal point is correct, but the segment must begin where this ray strikes the lens. Moving the starting point to the lens center changes the ray and no longer continues the given incident path.
- id: p7-hit-point-horizontal
  content: |-
    Continue horizontally from the ray's lens-contact point.
  feedback: |-
    A horizontal outgoing ray is produced when the incident ray is aimed through the near focal point. Here the ray arrives parallel instead, so it bends from the contact point toward the far focal point.
- id: p7-hit-point-near-focus
  content: |-
    Draw backward from the lens-contact point through the left-hand focal point.
  feedback: |-
    That line lies on the incident side and does not trace the ray after it crosses the lens. For a parallel incident ray, the requested refracted segment is on the outgoing side and passes through the opposite focal point.
```

---

<a id="keep-the-reverse-rule-separate"></a>
## Keep the Reverse Rule Separate

**Example:** Compare these two converging-lens principal rays:

1. a ray that arrives parallel to the optical axis;
2. a ray that approaches the lens along a line through the near focal point.

**Explanation**

These rules are reverses of one another:

| Incident-ray cue | Refracted-ray result |
|---|---|
| Parallel to the optical axis | Passes through the far focal point |
| Aimed through the near focal point | Emerges parallel to the optical axis |

Read the incident segment first. If it is already horizontal and parallel, do not choose another horizontal segment after the lens. Instead, choose the segment through the far focus.

```quiz
type: radio
id: p7-distinguish-reciprocal-rules
content: |-
  A ray approaches a converging lens along a line that passes through the focal point on the incident side. What happens after refraction?
options:
- id: p7-emerges-parallel
  content: |-
    It emerges parallel to the optical axis.
  correct: true
  feedback: |-
    For a converging lens, the near-focus input rule is the reverse of the parallel-input rule. Because the incident line passes through the focal point on the incoming side, the refracted ray emerges parallel to the optical axis.
- id: p7-emerges-through-far-focus
  content: |-
    It passes through the focal point on the outgoing side.
  feedback: |-
    Passing through the far focus is the result for a ray that arrives parallel to the axis. This ray instead arrives through the near focus, so the reverse principal-ray rule makes it emerge parallel.
- id: p7-emerges-through-center
  content: |-
    It bends so that it passes through the center of the lens.
  feedback: |-
    The lens center identifies a separate ray that continues approximately straight; it is not the destination of a refracted ray. An incident ray through the near focus emerges parallel to the axis.
- id: p7-reflects-to-near-focus
  content: |-
    It reflects back through the same near focal point.
  feedback: |-
    A thin lens refracts this transmitted ray rather than reflecting it back. The near focal point describes the incoming line, and the corresponding outgoing line is parallel to the optical axis.
```

---

<a id="choose-the-labeled-path"></a>
## Choose the Labeled Path

**Example:** In the diagram below, a ray from the object top approaches the converging lens horizontally from left to right. Determine which labeled path continues that ray after refraction.

![](<../Source/2026-08-12-HW-10/Images/converging-lens-principal-ray-options.png>)

**Explanation**

Use a three-part audit:

1. **Outgoing side:** the refracted ray must lie to the right of the lens.
2. **Starting point:** it must continue from the point where the horizontal incident ray meets the lens.
3. **Far focus:** it must pass through the right-hand focal point.

Only ray $c$ satisfies all three conditions. Ray $b$ is on the outgoing side but slopes away from the far focus. Rays $a$ and $d$ lie on the incident side.

```quiz
type: radio
id: p7-target-ray-choice
content: |-
  The figure shows an object to the left of a thin, converging lens of focal length $f$.

  ![](<../Source/2026-08-12-HW-10/Images/converging-lens-principal-ray-options.png>)

  Which labeled ray shows the path taken after refraction by the paraxial ray originating at the top of the object and arriving parallel to the optical axis?
options:
- id: p7-target-a
  content: |-
    $a$
  feedback: |-
    Ray $a$ lies on the incident side of the lens, so it cannot be the path after refraction. The horizontal incident ray travels left to right and must continue on the right through the far focal point.
- id: p7-target-b
  content: |-
    $b$
  feedback: |-
    Ray $b$ is on the outgoing side, but it slopes upward and misses the right-hand focal point. A ray arriving parallel to the axis of a converging lens must refract through that far focus.
- id: p7-target-c
  content: |-
    $c$
  correct: true
  feedback: |-
    A parallel incident ray through a converging lens refracts through the focal point on the opposite side. Ray $c$ begins at the lens-contact point, lies on the outgoing side, and passes through the right-hand focal point.
- id: p7-target-d
  content: |-
    $d$
  feedback: |-
    Ray $d$ lies on the incident side and follows the line through the near focal point. That line is relevant to the reverse rule—near focus in gives parallel out—but it is not the outgoing continuation of this parallel incident ray.
```

---

<a id="summary"></a>
## Summary

When a ray reaches a converging lens parallel to the optical axis, use **parallel in, far focus out**:

1. Follow the arrow to identify the outgoing side.
2. Mark where the given ray meets the lens.
3. Draw from that contact point through the focal point on the outgoing side.

The main trap is reversing the paired principal-ray rules. **Parallel in** gives **far focus out**; **near focus in** gives **parallel out**.
