# Carry a Ray through One or More Refracting Boundaries

<!--
lesson-id: 212-M5-070
topic-code: MTH212.M5.70
-->

## Table of Contents

- [Introduction](#introduction)
- [Map the Normal at Each Boundary](#boundary-map)
- [Source-Video Problem 5: Air to Water](#source-air-water)
- [Source-Video Problem 6: Parallel Air, Glass, and Diamond Layers](#source-parallel-layers)
- [Source-Video Problem 7: Rectangular Block with Perpendicular Faces](#source-rectangular-block)
- [Summary](#summary)

## Prerequisites

- Evaluate sine and inverse sine in degree mode.
- Rearrange a proportion to isolate one sine.
- Recognize parallel and perpendicular lines.
- Find the complement of an acute angle.

---

<a id="introduction"></a>
## Introduction

At every refracting surface, draw the **local normal**: the line perpendicular to that surface at the point where the ray crosses. Both angles in Snell's law are measured from that normal, never from the surface:

$$
\boxed{n_1\sin\theta_1=n_2\sin\theta_2}.
$$

Here, medium 1 is the medium the ray leaves and medium 2 is the medium it enters. A reliable calculation follows one sequence:

1. Draw the normal at the current boundary.
2. Label the index on each side of the boundary.
3. Measure the incident and refracted angles from that normal.
4. Solve
   $$
   \theta_2=\arcsin\!\left(\frac{n_1}{n_2}\sin\theta_1\right).
   $$
5. Before moving to another boundary, compare its normal with the previous normal.

Keep the calculator in degree mode and carry the unrounded angle to any later boundary. Round only the requested final angle.

The index change predicts the direction of bending:

| Index change | Refracted angle | Ray bends |
|---|---:|---|
| low $n$ to high $n$ | smaller | toward the normal |
| high $n$ to low $n$ | larger | away from the normal |

This prediction catches a reversed index ratio before it reaches the calculator.

---

<a id="boundary-map"></a>
## Map the Normal at Each Boundary

The ray travels in a straight line while it remains in one uniform medium. What may change at the next surface is the reference line used to measure its angle.

| Relationship between consecutive normals | Incidence angle at the next boundary |
|---|---|
| normals are parallel | reuse the ray's angle from the preceding boundary |
| normals are perpendicular | take the acute complement, $90^\circ-\theta$ |
| normals have another orientation | measure the ray from the new normal directly |

**Example:** A ray travels inside a rectangular block at $34^\circ$ to the horizontal normal drawn at its vertical entry face, then reaches the horizontal top face. What angle belongs in Snell's law at the top face?

**Explanation**

The top-face normal is vertical, so it is perpendicular to the first normal. The ray's angle to the new normal is

$$
\theta_{\text{top}}=90^\circ-34^\circ=56^\circ.
$$

The $34^\circ$ angle is now the ray's angle to the **top surface**, not to its normal.

```quiz
type: radio
id: mct-p12-normal-turn
shuffle: true
content: |-
  A ray inside a rectangular block travels at $27^\circ$ to the horizontal normal of a vertical entry face. It next reaches the horizontal top face. What incidence angle belongs in Snell's law at the top face?
options:
- id: normal-turn-a
  content: |-
    $63^\circ$
  correct: true
  feedback: |-
    The two face normals are perpendicular, so the ray's acute angles to them are complementary. Thus $\theta_{\text{top}}=90^\circ-27^\circ=63^\circ$, measured from the vertical top-face normal.
- id: normal-turn-b
  content: |-
    $27^\circ$
  feedback: |-
    The $27^\circ$ angle can be reused only when the next normal is parallel to the first. At the horizontal top face, $27^\circ$ is the ray-to-surface angle; Snell's law needs its $63^\circ$ complement from the vertical normal.
- id: normal-turn-c
  content: |-
    $90^\circ$
  feedback: |-
    The normals are $90^\circ$ apart, but the ray is not aligned with either surface. Use that right-angle turn to form a complement: $90^\circ-27^\circ=63^\circ$.
- id: normal-turn-d
  content: |-
    $117^\circ$
  feedback: |-
    This is the obtuse supplement of $63^\circ$. Snell's law here uses the acute angle between the ray and the local normal, so the incidence angle is $63^\circ$.
```

---

<a id="source-air-water"></a>
## Source-Video Problem 5: Air to Water

In the first source segment (`ohQheheySDw`, 00:05:07–00:08:05), light travels from air into water with

$$
n_{\text{air}}=1.00,
\qquad
n_{\text{water}}=1.33,
\qquad
\theta_i=30^\circ.
$$

**Example:** Find the refracted angle in the water and state which way the ray bends.

**Explanation**

Apply Snell's law at the one boundary:

$$
\begin{aligned}
n_{\text{air}}\sin\theta_i
&=n_{\text{water}}\sin\theta_r,\\
\sin\theta_r
&=\frac{1.00}{1.33}\sin30^\circ\\
&=0.37594\ldots,\\
\theta_r
&=22.082\ldots^\circ
\approx \boxed{22^\circ}.
\end{aligned}
$$

The index rises and the angle falls from $30^\circ$ to about $22^\circ$, so the ray bends toward the normal. Reversing the trip would take light from high $n$ to low $n$; the refracted angle would grow and the ray would bend away from the normal.

**Lecture check (M5-2).** The lecture notes give $n\lambda=\text{constant}$ for the same light. Thus

$$
\lambda_{\text{water}}
=\frac{n_{\text{air}}}{n_{\text{water}}}\lambda_{\text{air}}
=\frac{1}{1.33}\lambda_{\text{air}},
$$

so the higher-index medium has the shorter wavelength. This is a physical check on the index change, not another way to calculate the ray angle; Snell's law still controls the direction.

```quiz
type: radio
id: mct-p12-single-boundary
shuffle: true
content: |-
  Light travels from air $(n=1.00)$ into water $(n=1.33)$ at $45.0^\circ$ to the normal. What is the refracted angle, measured from the normal?
options:
- id: single-a
  content: |-
    $32.1^\circ$
  correct: true
  feedback: |-
    Snell's law gives $\sin\theta_r=(1.00/1.33)\sin45.0^\circ$, so $\theta_r=32.1^\circ$. The angle is smaller than $45.0^\circ$, as required when light enters the higher-index medium and bends toward the normal.
- id: single-b
  content: |-
    $57.9^\circ$
  feedback: |-
    This is the complement of the $32.1^\circ$ refracted angle, so it measures the ray from the surface. Snell's law angles are measured from the normal; the requested angle is $32.1^\circ$.
- id: single-c
  content: |-
    $70.1^\circ$
  feedback: |-
    This comes from reversing the index ratio and evaluating $\arcsin(1.33\sin45.0^\circ)$. The correct ratio is $n_{\text{air}}/n_{\text{water}}$, and entering higher $n$ must make the angle smaller, not larger.
- id: single-d
  content: |-
    $33.8^\circ$
  feedback: |-
    Dividing the angle itself by $1.33$ does not satisfy Snell's law. The index multiplies $\sin\theta$, so first compute $(1.00/1.33)\sin45.0^\circ$ and then take inverse sine to obtain $32.1^\circ$.
- id: single-e
  content: |-
    $45.0^\circ$
  feedback: |-
    A nonzero incident angle remains unchanged only when the two indices are equal. Water has the larger index here, so the ray bends toward the normal and the angle falls to $32.1^\circ$.
```

---

<a id="source-parallel-layers"></a>
## Source-Video Problem 6: Parallel Air, Glass, and Diamond Layers

The second source segment (`ohQheheySDw`, 00:08:07–00:14:15) uses parallel interfaces:

$$
\theta_{\text{air}}=60^\circ,
\qquad
n_{\text{air}}=1.00,
\qquad
n_g=1.50,
\qquad
n_d=2.42.
$$

Because the interfaces are parallel, their normals are parallel. The refracted angle in the glass at the first interface is therefore also the incidence angle at the glass-diamond interface.

**Example:** Find the ray angle in the glass and then in the diamond. Verify the diamond angle with an endpoint shortcut.

**Explanation**

At the air-glass boundary,

$$
\begin{aligned}
\theta_g
&=\arcsin\!\left(\frac{1.00}{1.50}\sin60^\circ\right)\\
&=35.264\ldots^\circ
\approx \boxed{35.3^\circ}.
\end{aligned}
$$

Reuse that angle at the second boundary because the normals are parallel:

$$
\begin{aligned}
\theta_d
&=\arcsin\!\left(\frac{1.50}{2.42}\sin35.264\ldots^\circ\right)\\
&=20.9689\ldots^\circ
\approx \boxed{21^\circ}.
\end{aligned}
$$

The two boundary equations form one chain,

$$
n_{\text{air}}\sin\theta_{\text{air}}
=n_g\sin\theta_g
=n_d\sin\theta_d.
$$

The glass term can be skipped when only the endpoint angle is requested:

$$
\begin{aligned}
\theta_d
&=\arcsin\!\left(\frac{1.00}{2.42}\sin60^\circ\right)\\
&=20.9689\ldots^\circ
\approx 21^\circ.
\end{aligned}
$$

This shortcut depends on the parallel normals. It does not apply merely because the ray crosses several layers, and it does not supply an intermediate angle when that angle is requested.

```quiz
type: radio
id: mct-p12-parallel-layers
shuffle: true
content: |-
  A ray enters parallel layers in the order air $(n=1.00)$, acrylic $(n=1.50)$, then water $(n=1.33)$. Its angle in air is $40.0^\circ$ to the common normal. What is its angle in the water?
options:
- id: parallel-a
  content: |-
    $28.9^\circ$
  correct: true
  feedback: |-
    Parallel normals allow the endpoint relation $1.00\sin40.0^\circ=1.33\sin\theta_{\text{water}}$. It gives $\theta_{\text{water}}=28.9^\circ$; the two-step route gives $25.4^\circ$ in acrylic and the same $28.9^\circ$ endpoint.
- id: parallel-b
  content: |-
    $25.4^\circ$
  feedback: |-
    This is the correct angle inside the acrylic after the first boundary, but the ray then crosses into water. Apply Snell's law once more, or use the parallel-layer endpoint relation, to obtain $28.9^\circ$ in water.
- id: parallel-c
  content: |-
    $40.0^\circ$
  feedback: |-
    Parallel normals let an angle serve as the outgoing angle at one boundary and the incoming angle at the next; they do not prevent refraction. Since water and air have different indices, the endpoint angle is $28.9^\circ$, not $40.0^\circ$.
- id: parallel-d
  content: |-
    $61.1^\circ$
  feedback: |-
    This is the complement of the $28.9^\circ$ ray angle and is measured from the layer surface. The prompt and Snell's law both require the angle from the normal.
- id: parallel-e
  content: |-
    $22.3^\circ$
  feedback: |-
    This results from reversing the acrylic-water index ratio at the second boundary. The ray goes from $n=1.50$ to $n=1.33$, so it must bend away from the normal and increase from $25.4^\circ$ to $28.9^\circ$.
```

---

<a id="source-rectangular-block"></a>
## Source-Video Problem 7: Rectangular Block with Perpendicular Faces

The final source segment (`ohQheheySDw`, 00:14:17–00:17:32) shows a rectangular block with $n=1.20$ in air. The frame fixes the geometry:

| Boundary | Surface orientation | Local normal | Angle used |
|---|---|---|---:|
| entry | vertical left face | horizontal | $70^\circ$ |
| exit | horizontal top face | vertical | complement of the internal angle |

The normal turns by $90^\circ$, so the parallel-layer shortcut is unavailable.

**Example:** Find the angle $x$ at which the ray exits the top face, measured from the vertical normal.

**Explanation**

At the left face,

$$
\begin{aligned}
\theta_2
&=\arcsin\!\left(\frac{1.00}{1.20}\sin70^\circ\right)\\
&=51.5432\ldots^\circ
\approx 51.5^\circ.
\end{aligned}
$$

At the top face, the new incidence angle is the complement:

$$
\theta_3
=90^\circ-51.5432\ldots^\circ
=38.4568\ldots^\circ.
$$

The video displays $38.45^\circ$. Keeping the unrounded value for the next boundary gives

$$
\begin{aligned}
1.20\sin\theta_3
&=1.00\sin x,\\
x
&=\arcsin\!\left(1.20\sin38.4568\ldots^\circ\right)\\
&=48.2717\ldots^\circ
\approx \boxed{48.3^\circ}.
\end{aligned}
$$

The ray bends away from the normal as it exits from the higher-index block into air, so $x$ must exceed the $38.46^\circ$ incidence angle. That direction check agrees with the calculation.

```quiz
type: radio
id: mct-p12-rectangular-block
shuffle: true
content: |-
  A ray in air enters the vertical face of a rectangular block with $n=1.30$ at $60.0^\circ$ to the horizontal normal. It then reaches the perpendicular top face and exits back into air. What is its exit angle from the vertical top-face normal?
options:
- id: block-a
  content: |-
    $75.8^\circ$
  correct: true
  feedback: |-
    The first boundary gives $\theta_{\text{block}}=\arcsin[(1.00/1.30)\sin60.0^\circ]=41.772\ldots^\circ$. The top-face incidence is $48.228\ldots^\circ$, and $\arcsin[1.30\sin48.228\ldots^\circ]=75.8^\circ$ from the vertical normal.
- id: block-b
  content: |-
    $60.0^\circ$
  feedback: |-
    This follows from reusing the $41.8^\circ$ internal angle at the second boundary, as though the two normals were parallel. It would be the exit angle for parallel entry and exit faces, but these faces are perpendicular; use the unrounded $48.228\ldots^\circ$ complement to obtain $75.8^\circ$.
- id: block-c
  content: |-
    $48.2^\circ$
  feedback: |-
    This is the correct incidence angle at the top face after taking the complement, but the ray has not yet refracted into air. Because it goes from $n=1.30$ to $n=1.00$, it bends away from the normal to $75.8^\circ$.
- id: block-d
  content: |-
    $41.8^\circ$
  feedback: |-
    This is the ray angle inside the block measured from the horizontal entry-face normal. The top-face normal is vertical, so first replace it with the $48.2^\circ$ complement and then apply Snell's law again.
- id: block-e
  content: |-
    $14.2^\circ$
  feedback: |-
    This is the complement of the $75.8^\circ$ exit angle and therefore measures the outgoing ray from the top surface. The requested Snell angle is measured from the vertical normal, so it is $75.8^\circ$.
```

---

<a id="summary"></a>
## Summary

For every refracting boundary:

1. Draw that surface's normal.
2. Measure both ray angles from the normal.
3. Predict the bend: higher $n$ means toward the normal; lower $n$ means away.
4. Apply $n_1\sin\theta_1=n_2\sin\theta_2$ and keep guard digits.
5. Before the next boundary, inspect the normals. Reuse the internal angle only for parallel normals; take a complement for perpendicular normals; otherwise remeasure from the new normal.

For parallel layers only,

$$
n_1\sin\theta_1
=n_2\sin\theta_2
=\cdots
=n_k\sin\theta_k,
$$

so intermediate layers may be skipped when only the endpoint angle is needed. A turn in the surface breaks that shortcut. The most common error is carrying an angle to a new boundary without first changing its reference normal.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
