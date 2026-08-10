# Choosing a Refracted Ray at a Boundary

<!--
lesson-id: 212-M7-003
topic-code: MTH212.M7.03
-->
## Table of Contents

- [Introduction](#introduction)
- [Draw the Normal First](#draw-the-normal-first)
- [Use the Refractive-Index Change](#use-the-refractive-index-change)
- [Choose the Possible Path](#choose-the-possible-path)
- [Summary](#summary)

## Prerequisites

- Interpret a ray's arrow as its direction of travel.
- Recognize perpendicular lines and compare angle sizes.

---

<a id="introduction"></a>
## Introduction

When a ray crosses a boundary between two transparent materials, its direction is judged relative to the **normal**, the line perpendicular to the boundary at the point of incidence. The useful cue is an oblique ray entering a material with a different refractive index.

The procedure is:

1. Draw the normal at the point where the ray meets the boundary.
2. Identify whether the ray enters a larger or smaller refractive index.
3. Compare the incident and refracted angles from the normal.

Entering a larger refractive index makes the ray bend **toward the normal**, so the refracted angle is smaller. Entering a smaller refractive index makes it bend **away from the normal**, so the refracted angle is larger.

For an oblique ray entering a larger refractive index, there is a fast diagram test: extend the incident ray straight through the boundary, draw the inward normal, and look in the sector between those two lines. The refracted ray must lie inside that sector.

---

<a id="draw-the-normal-first"></a>
## Draw the Normal First

**Example:** A ray meets a horizontal air-glass boundary at an oblique angle. Which reference line should be drawn before predicting the transmitted ray?

**Explanation**

Draw a line perpendicular to the boundary through the point of incidence. For a horizontal boundary, this normal is vertical. Both the incident angle $\theta_1$ and refracted angle $\theta_2$ are measured from that normal, not from the surface.

```quiz
type: radio
id: p3-normal-reference
content: |-
  A ray strikes a slanted boundary. Which line is the correct reference for deciding whether the ray bends toward or away?
options:
- id: p3-normal-perpendicular
  content: |-
    The line perpendicular to the boundary at the point of incidence
  correct: true
  feedback: |-
    Refraction angles are defined from the normal. The line perpendicular to the boundary at the incidence point is that normal, so it is the reference for comparing the two ray directions.
- id: p3-normal-along-surface
  content: |-
    The line along the boundary
  feedback: |-
    The boundary line shows the surface orientation, but refraction angles are not measured from the surface. Construct the perpendicular normal at the incidence point and compare each ray with that line.
- id: p3-normal-along-incident
  content: |-
    The line extending the incident ray straight ahead
  feedback: |-
    A straight-ahead extension shows the no-bending path, not the angular reference. Bending toward or away is determined by angles measured from the normal to the boundary.
- id: p3-normal-prism-base
  content: |-
    A line parallel to the base of the prism
  feedback: |-
    The prism base does not control refraction at a different face. The local boundary at the incidence point determines the normal, which must be perpendicular to that face.
```

---

<a id="use-the-refractive-index-change"></a>
## Use the Refractive-Index Change

**Example:** A ray travels from air with index $n_1$ into glass with index $n_2$, where $n_2>n_1$, and $\theta_1>0$.

**Explanation**

Snell's law is

$$
n_1\sin\theta_1=n_2\sin\theta_2.
$$

Because $n_2$ is larger, $\sin\theta_2$ must be smaller than $\sin\theta_1$. For angles between $0^\circ$ and $90^\circ$, this means $\theta_2<\theta_1$: the ray turns toward the normal.

**Common trap:** "Toward the normal" does not mean up, down, left, or right on the page. It means that the transmitted ray makes a smaller angle with the perpendicular normal. When the boundary rotates, the normal rotates with it.

```quiz
type: radio
id: p3-index-direction
content: |-
  A ray travels obliquely from glass into air. How does the transmitted ray bend, assuming transmission occurs?
options:
- id: p3-index-away
  content: |-
    Away from the normal, so its angle from the normal increases
  correct: true
  feedback: |-
    Air has a smaller refractive index than glass. Entering the smaller index increases the refracted angle measured from the normal, so the transmitted ray bends away from the normal.
- id: p3-index-toward
  content: |-
    Toward the normal, so its angle from the normal decreases
  feedback: |-
    Bending toward the normal occurs when the ray enters a larger refractive index. This ray goes from glass to lower-index air, so its angle from the normal increases instead.
- id: p3-index-straight
  content: |-
    Straight ahead with no change in direction
  feedback: |-
    An oblique ray remains straight only when the refractive indices match. Glass and air have different indices, so a transmitted ray changes direction and bends away from the normal.
- id: p3-index-along-normal
  content: |-
    Exactly along the normal for every incident angle
  feedback: |-
    A refracted ray lies along the normal when the incident ray itself is normal to the surface. At oblique incidence, changing index alters the angle but does not force it to $0^\circ$.
```

---

<a id="choose-the-possible-path"></a>
## Choose the Possible Path

**Example:** Sunlight in air meets the slanted face of a glass prism. The dashed incident ray is horizontal, but the relevant normal is perpendicular to the slanted face and points into the prism.

**Explanation**

Use the three-part diagram test:

1. Extend the dashed incident ray straight into the prism to mark the no-bending direction.
2. Imagine the inward normal perpendicular to the slanted face at the incidence point.
3. Look for a candidate inside the sector from the straight-ahead line toward the inward normal.

The ray enters higher-index glass, so its direction inside the prism must be closer to the inward normal than the incident direction is. A path that continues straight does not bend, while a path on the other side of the straight-ahead direction turns the wrong way.

```quiz
type: radio
id: p3-prism-path
content: |-
  From air, sunlight is incident on the side of a glass prism, as shown by the dashed arrow.

  ![](<../Source/2026-08-12-HW-10/Images/sunlight-glass-prism-refraction-paths.png>)

  Which arrow indicates a possible path of the light upon entering the glass?
options:
- id: p3-prism-a
  content: |-
    $a$
  feedback: |-
    Path $a$ turns to the opposite side of the incident direction from the inward normal. Air-to-glass refraction must turn the transmitted ray toward that normal, so $a$ cannot be the refracted path.
- id: p3-prism-b
  content: |-
    $b$
  feedback: |-
    Path $b$ is the straight-ahead continuation of the incident ray. That is possible at normal incidence or when the indices match, but this ray is oblique and passes from air into higher-index glass.
- id: p3-prism-c
  content: |-
    $c$
  correct: true
  feedback: |-
    A ray entering higher-index glass bends toward the normal to the face. Here the inward normal points down and left into the prism, and path $c$ turns in that direction, so $c$ is a possible refracted path.
```

---

<a id="summary"></a>
## Summary

- At the incidence point, draw the line perpendicular to the local boundary.
- Measure both ray angles from this normal, never from the surface.
- Larger refractive index: bend toward the normal, so the angle decreases.
- Smaller refractive index: bend away from the normal, so the angle increases.
- For an oblique air-to-glass ray, choose the path inside the sector between the straight-ahead extension and the inward normal; reject either boundary of that sector and any path outside it.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 4 Study Guide](../../2026-08-13-Q-4/Study-Guide.md)
Next: [Identifying a Material from Refraction](Problem-2.md)

Study guide index: 02/11

---

<!-- lesson-nav:end -->
