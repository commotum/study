# Comparing Refractive Indices Across Multiple Media

<!--
lesson-id: 212-M7-014
topic-code: MTH212.M7.14
-->

## Table of Contents

- [Introduction](#introduction)
- [Compare Index and Ray Angle](#compare-index-and-ray-angle)
- [Carry Snell's Law Across Parallel Layers](#carry-snells-law-across-parallel-layers)
- [Measure Every Angle From the Normal](#measure-every-angle-from-the-normal)
- [Match the Source Problem](#match-the-source-problem)
- [Summary](#summary)

## Prerequisites

- Identify the normal as the line perpendicular to an interface.
- Compare sines of acute angles: a larger angle from the normal has a larger sine.
- Use Snell's law, $n_a\sin\theta_a=n_b\sin\theta_b$.

---

<a id="introduction"></a>
## Introduction

When one ray crosses several parallel media, apply Snell's law at each boundary. The same product carries through the layers:

$$
n_1\sin\theta_1
=n_2\sin\theta_2
=n_3\sin\theta_3.
$$

Each label $\theta_i$ is relative to the normal at that interface, just as geometric labels such as “adjacent” depend on the chosen reference angle. For ray angles between $0^\circ$ and $90^\circ$, sine increases with angle. Therefore, along the same ray:

- a smaller angle from the normal corresponds to a larger refractive index;
- a larger angle from the normal corresponds to a smaller refractive index;
- equal angles correspond to equal indices.

This comparison often avoids calculating any sine values or solving for the intermediate index.

---

<a id="compare-index-and-ray-angle"></a>
## Compare Index and Ray Angle

**Example:** A ray crosses from medium $A$ into medium $B$. Its angles from the normal are $50^\circ$ in $A$ and $30^\circ$ in $B$. Which index is larger?

**Explanation**

Snell's law gives

$$
n_A\sin50^\circ=n_B\sin30^\circ.
$$

Because $\sin50^\circ>\sin30^\circ$, the coefficient paired with the larger sine must be smaller. Thus $n_A<n_B$. The ray's smaller angle in $B$ indicates the higher-index medium.

```quiz
type: radio
id: snell-compare-two-media
content: |-
  A ray has angle $25^\circ$ from the normal in medium $A$ and $40^\circ$ from the normal in medium $B$. Which relationship is true?
options:
- id: snell-two-media-a-greater
  content: |-
    $n_A>n_B$
  correct: true
  feedback: |-
    Snell's law gives $n_A\sin25^\circ=n_B\sin40^\circ$. Since $\sin25^\circ<\sin40^\circ$, $n_A$ must be larger to keep the products equal, so $n_A>n_B$.
- id: snell-two-media-b-greater
  content: |-
    $n_B>n_A$
  feedback: |-
    This pairs the larger angle with the larger index. Snell's law requires the opposite compensation: the larger sine in medium $B$ must multiply the smaller index, so $n_B<n_A$.
- id: snell-two-media-equal
  content: |-
    $n_A=n_B$
  feedback: |-
    Equal indices would require equal sines and therefore equal acute angles from the normal. The given angles are $25^\circ$ and $40^\circ$, so the indices are not equal.
- id: snell-two-media-indeterminate
  content: |-
    The relationship cannot be determined.
  feedback: |-
    The two normal-referenced angles are enough. Because sine increases over acute angles, Snell's law directly shows that the medium with the smaller $25^\circ$ angle has the larger index.
```

---

<a id="carry-snells-law-across-parallel-layers"></a>
## Carry Snell's Law Across Parallel Layers

For three parallel layers, apply Snell's law twice:

$$
n_1\sin\theta_1=n_2\sin\theta_2
$$

and

$$
n_2\sin\theta_2=n_3\sin\theta_3.
$$

The shared middle product links the endpoints:

$$
n_1\sin\theta_1=n_3\sin\theta_3.
$$

To make the requested comparison explicit, isolate the endpoint index ratio while treating the measured angles as fixed:

$$
\boxed{\frac{n_3}{n_1}=\frac{\sin\theta_1}{\sin\theta_3}}.
$$

This shared-ratio form plays the same role as a common denominator: both sides are now ready to compare against $1$. The intermediate product $n_2\sin\theta_2$ has canceled.

**Example:** A ray has angle $35^\circ$ in medium 1 and $15^\circ$ in medium 3. Since $\sin35^\circ>\sin15^\circ$, the endpoint equality requires $n_3>n_1$. No value of $n_2$ is needed.

```quiz
type: radio
id: snell-compare-three-media
content: |-
  A ray crosses three parallel media. Its angles from the normal are $28^\circ$ in medium 1, $17^\circ$ in medium 2, and $42^\circ$ in medium 3. Which endpoint relationship is true?
options:
- id: snell-three-media-n1-greater
  content: |-
    $n_1>n_3$
  correct: true
  feedback: |-
    Across the parallel layers, $n_1\sin28^\circ=n_3\sin42^\circ$. Since $\sin42^\circ$ is larger, $n_3$ must be smaller, so $n_1>n_3$.
- id: snell-three-media-n3-greater
  content: |-
    $n_3>n_1$
  feedback: |-
    This assigns the larger index to the larger endpoint angle. In the endpoint equation, the larger $\sin42^\circ$ must pair with the smaller index; therefore $n_3<n_1$.
- id: snell-three-media-equal
  content: |-
    $n_1=n_3$
  feedback: |-
    Equal endpoint indices would make $\sin28^\circ=\sin42^\circ$, which is false for these acute angles. The unequal endpoint angles require unequal indices.
- id: snell-three-media-need-n2
  content: |-
    $n_1$ and $n_3$ cannot be compared without knowing $n_2$.
  feedback: |-
    The middle product $n_2\sin17^\circ$ is common to both interfaces and can be eliminated. This leaves $n_1\sin28^\circ=n_3\sin42^\circ$, which is sufficient to compare the endpoints.
```

---

<a id="measure-every-angle-from-the-normal"></a>
## Measure Every Angle From the Normal

Snell's law uses angles from the normal, not angles from the surface. If a diagram labels an angle $\alpha$ from a flat interface, convert it first:

$$
\theta=90^\circ-\alpha.
$$

Use the same diagram-reading sequence every time:

1. Draw or locate the normal at each boundary.
2. Relabel each ray angle from that local normal.
3. Only then chain Snell's law and compare the endpoint sines.

**Example:** A ray is $60^\circ$ from the surface in medium 1 and $45^\circ$ from the surface in medium 3. The normal angles are $30^\circ$ and $45^\circ$. Since the endpoint angle is smaller in medium 1, $n_1>n_3$.

```quiz
type: radio
id: snell-surface-angle-comparison
content: |-
  A ray crosses parallel media. It is $70^\circ$ from the surface in medium 1 and $50^\circ$ from the surface in medium 3. Which relationship is true?
options:
- id: snell-surface-n1-greater
  content: |-
    $n_1>n_3$
  correct: true
  feedback: |-
    The normal angles are $20^\circ$ in medium 1 and $40^\circ$ in medium 3. The smaller normal angle pairs with the larger index, so $n_1>n_3$.
- id: snell-surface-n3-greater
  content: |-
    $n_3>n_1$
  feedback: |-
    This compares the labeled surface angles as though Snell's law used them directly. Their complements are $20^\circ$ and $40^\circ$, so medium 1 has the smaller normal angle and the larger index.
- id: snell-surface-equal
  content: |-
    $n_1=n_3$
  feedback: |-
    The normal angles are unequal: $90^\circ-70^\circ=20^\circ$ and $90^\circ-50^\circ=40^\circ$. Equal indices would require equal normal angles along the same ray.
- id: snell-surface-indeterminate
  content: |-
    The relationship cannot be determined.
  feedback: |-
    The surface angles determine the normal angles by complementation. Once converted to $20^\circ$ and $40^\circ$, Snell's law shows that $n_1>n_3$.
```

---

<a id="match-the-source-problem"></a>
## Match the Source Problem

At each parallel interface, preserve the product $n\sin\theta$. Then compare the endpoint angles shown relative to their normals.

```quiz
type: radio
id: khadley-snells-law-q3
shuffle: true
content: |-
  **Question 3**

  A ray crosses the three media shown. Which relationship between $n_1$ and $n_3$ is true?

  ![[../Source/Images/clicker3.jpg]]
options:
- id: n1-greater
  content: $n_1>n_3$
  feedback: |-
    Applying Snell's law at both interfaces shows that the smaller $10^\circ$ angle in medium 3 corresponds to the larger index, not the smaller one.
- id: equal
  content: $n_1=n_3$
  feedback: |-
    If $n_1=n_3$, the ray would have the same angle to the normal in those two media. The diagram shows $20^\circ$ and $10^\circ$.
- id: n3-greater
  content: $n_3>n_1$
  correct: true
  feedback: |-
    Across both boundaries, $n_1\sin20^\circ=n_3\sin10^\circ$. Since $\sin20^\circ>\sin10^\circ$, $n_3$ must exceed $n_1$.
```

---

<a id="summary"></a>
## Summary

- Cue: one ray crosses multiple parallel media, and endpoint indices must be compared.
- Read every ray angle from the normal; complement any angle measured from the surface.
- Chain Snell's law: $n_1\sin\theta_1=n_2\sin\theta_2=n_3\sin\theta_3$.
- Isolate the comparison: $n_3/n_1=\sin\theta_1/\sin\theta_3$; the middle product cancels.
- Compare acute endpoint angles without decimals: the smaller angle pairs with the larger index.
- Main trap: do not assign the larger index to the larger angle, and do not keep an intermediate index that cancels.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
