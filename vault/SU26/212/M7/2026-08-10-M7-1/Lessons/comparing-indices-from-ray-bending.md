# Comparing Refractive Indices From Ray Bending

<!--
lesson-id: 212-M7-013
topic-code: MTH212.M7.13
-->

## Table of Contents

- [Introduction](#introduction)
- [Measure Every Angle From the Normal](#measure-every-angle-from-the-normal)
- [Turn Snell's Law Into an Index Ratio](#turn-snells-law-into-an-index-ratio)
- [Translate Toward or Away From the Normal](#translate-toward-or-away-from-the-normal)
- [Recognize When No Bending Is Inconclusive](#recognize-when-no-bending-is-inconclusive)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Identify the normal as the line perpendicular to an interface.
- Compare acute angles.
- Know that $\sin\theta$ increases as $\theta$ increases from $0^\circ$ to $90^\circ$.
- Rearrange a product equation into a ratio.

---

<a id="introduction"></a>
## Introduction

Snell's law relates the refractive indices and ray angles on the two sides of a boundary:

$$
n_1\sin\theta_1=n_2\sin\theta_2.
$$

Both angles are measured from the **normal**, not from the interface. Solving for the index ratio gives

$$
\boxed{\frac{n_2}{n_1}
=\frac{\sin\theta_1}{\sin\theta_2}}.
$$

Keep the labels tied to their roles:

- medium 1 contains the incident ray and uses $n_1,\theta_1$;
- medium 2 contains the transmitted ray and uses $n_2,\theta_2$;
- each $\theta$ is the acute angle between that ray and the same perpendicular normal.

For ordinary refraction angles between $0^\circ$ and $90^\circ$, the larger angle has the larger sine. Therefore:

- if the ray bends **toward the normal**, its angle decreases and it enters the larger-index medium;
- if the ray bends **away from the normal**, its angle increases and it enters the smaller-index medium.

The recognition cue is a ray that changes direction at an interface and a request to compare indices without necessarily calculating them. Identify the normal, compare $\theta_1$ and $\theta_2$, then use the inverse pairing in Snell's law: the smaller angle belongs to the larger index.

---

<a id="measure-every-angle-from-the-normal"></a>
## Measure Every Angle From the Normal

**Example:** A horizontal interface separates two media. A ray makes an angle of $35^\circ$ with the vertical normal in medium 1 and $20^\circ$ with the normal in medium 2. Which refraction angle is smaller?

**Explanation**

Fix the reference line before comparing anything: identify the interface, draw the perpendicular normal, follow the ray from medium 1 into medium 2, and only then name $\theta_1$ and $\theta_2$.

Here the normal is perpendicular to the horizontal boundary, so it is vertical. The stated angles are already measured from that normal:

$$
\theta_1=35^\circ,
\qquad
\theta_2=20^\circ.
$$

Thus $\theta_2<\theta_1$: the transmitted ray is closer to the normal and has bent toward it.

If a diagram instead labels angles from the interface, convert them to normal-based angles using

$$
\theta_{\text{normal}}=90^\circ-\theta_{\text{interface}}.
$$

```quiz
type: radio
id: refraction-angle-from-normal
shuffle: true
content: |-
  A ray in medium 1 makes $25^\circ$ with the normal. In medium 2 it makes $50^\circ$ with the interface. What are the two angles used in Snell's law?
options:
- id: theta-one-25-theta-two-40
  content: |-
    $\theta_1=25^\circ$ and $\theta_2=40^\circ$
  correct: true
  feedback: |-
    Snell's-law angles are measured from the normal. The first is already $25^\circ$, while the second is complementary to the interface angle: $\theta_2=90^\circ-50^\circ=40^\circ$.
- id: theta-one-25-theta-two-50
  content: |-
    $\theta_1=25^\circ$ and $\theta_2=50^\circ$
  feedback: |-
    The $50^\circ$ label is measured from the interface, but Snell's law requires the angle from the perpendicular normal. Its complementary angle is $40^\circ$.
- id: theta-one-65-theta-two-40
  content: |-
    $\theta_1=65^\circ$ and $\theta_2=40^\circ$
  feedback: |-
    The first angle was already measured from the normal and should remain $25^\circ$. Only the second, interface-based angle needs the complementary-angle conversion.
- id: theta-one-65-theta-two-50
  content: |-
    $\theta_1=65^\circ$ and $\theta_2=50^\circ$
  feedback: |-
    This keeps one interface angle and converts the angle that was already normal-based. Snell's law needs both angles from the normal, giving $25^\circ$ and $40^\circ$.
- id: theta-one-25-theta-two-140
  content: |-
    $\theta_1=25^\circ$ and $\theta_2=140^\circ$
  feedback: |-
    Adding $90^\circ$ does not produce the acute angle between the ray and the normal. At a flat boundary the ray angle used in Snell's law lies between $0^\circ$ and $90^\circ$, here $40^\circ$.
```

---

<a id="turn-snells-law-into-an-index-ratio"></a>
## Turn Snell's Law Into an Index Ratio

**Example:** A ray crosses from medium 1 at $\theta_1=60^\circ$ into medium 2 at $\theta_2=30^\circ$. Compare $n_1$ and $n_2$.

**Explanation**

Make the requested index ratio the subject:

$$
\begin{aligned}
n_1\sin\theta_1&=n_2\sin\theta_2\\
\frac{n_2}{n_1}
&=\frac{\sin\theta_1}{\sin\theta_2}.
\end{aligned}
$$

Substitute the angles:

$$
\frac{n_2}{n_1}
=\frac{\sin60^\circ}{\sin30^\circ}
=\frac{\sqrt3/2}{1/2}
=\sqrt3>1.
$$

Therefore,

$$
n_2>n_1.
$$

The index and angle are paired inversely: the smaller transmitted angle $\theta_2$ must be balanced by the larger transmitted-medium index $n_2$.

Because both sines are positive, the comparison can be compressed to

$$
\frac{n_2}{n_1}>1
\iff
\sin\theta_1>\sin\theta_2
\iff
\theta_1>\theta_2
$$

for acute refraction angles. Reversing either inequality reverses the index comparison.

```quiz
type: radio
id: snells-law-index-ratio
shuffle: true
content: |-
  A ray has $\theta_1=45^\circ$ in medium 1 and $\theta_2=25^\circ$ in medium 2. Which comparison follows from Snell's law?
options:
- id: n2-greater-than-n1
  content: |-
    $n_2>n_1$
  correct: true
  feedback: |-
    Snell's law gives $n_2/n_1=\sin45^\circ/\sin25^\circ$. Since sine increases for acute angles and $45^\circ>25^\circ$, this ratio exceeds $1$, so $n_2>n_1$.
- id: n1-greater-than-n2
  content: |-
    $n_1>n_2$
  feedback: |-
    This pairs the larger angle with the larger index. Snell's law instead requires the products $n\sin\theta$ to match, so the smaller $25^\circ$ angle belongs to the larger index $n_2$.
- id: n1-equals-n2
  content: |-
    $n_1=n_2$
  feedback: |-
    Equal indices at an oblique boundary would require equal sines and therefore equal acute angles. The given angles differ, so the indices cannot be equal.
- id: n2-is-zero
  content: |-
    $n_2=0$
  feedback: |-
    Refractive indices of ordinary media are positive, and Snell's law gives a positive finite ratio of sines here. The angle comparison determines $n_2>n_1$, not a zero index.
- id: cannot-compare-without-numbers
  content: |-
    The indices cannot be compared without numerical index values.
  feedback: |-
    Numerical indices are unnecessary because the sine ratio already has a known order. Since $\sin45^\circ>\sin25^\circ$, $n_2/n_1>1$ and medium 2 has the larger index.
```

---

<a id="translate-toward-or-away-from-the-normal"></a>
## Translate Toward or Away From the Normal

**Example:** A ray enters medium 2 and bends away from the normal. Which medium has the larger refractive index?

**Explanation**

Bending away from the normal means

$$
\theta_2>\theta_1.
$$

For acute angles, this gives

$$
\sin\theta_2>\sin\theta_1.
$$

From

$$
\frac{n_2}{n_1}
=\frac{\sin\theta_1}{\sin\theta_2},
$$

the numerator is smaller than the denominator, so $n_2/n_1<1$. Therefore,

$$
n_2<n_1.
$$

The ray bends away from the normal when it enters the lower-index, faster medium.

```quiz
type: radio
id: bending-direction-index-comparison
shuffle: true
content: |-
  An oblique ray enters medium 2 and bends toward the normal. Which statement is correct?
options:
- id: medium-two-higher-index
  content: |-
    $n_2>n_1$
  correct: true
  feedback: |-
    Toward the normal means $\theta_2<\theta_1$. Snell's law then requires the medium-2 index to be larger so that $n_2\sin\theta_2$ still equals $n_1\sin\theta_1$.
- id: medium-one-higher-index
  content: |-
    $n_1>n_2$
  feedback: |-
    A lower transmitted-medium index would make the transmitted angle larger and bend the ray away from the normal. The observed bend toward the normal identifies medium 2 as the higher-index medium.
- id: indices-equal
  content: |-
    $n_1=n_2$
  feedback: |-
    Equal indices would not change the direction of an oblique ray. Because the ray visibly bends at the interface, the media have different indices, with $n_2$ larger.
- id: medium-two-faster-and-higher
  content: |-
    Medium 2 is both faster and higher-index.
  feedback: |-
    Refractive index and light speed obey $n=c/v$, so a higher index means a lower speed. The bend toward the normal indicates that medium 2 is higher-index and slower.
- id: cannot-determine-from-direction
  content: |-
    The comparison cannot be determined from bending direction.
  feedback: |-
    For an oblique ray, direction relative to the normal is sufficient. A smaller transmitted angle means a larger transmitted-medium index, so $n_2>n_1$.
```

---

<a id="recognize-when-no-bending-is-inconclusive"></a>
## Recognize When No Bending Is Inconclusive

**Example:** A ray strikes an interface along the normal and continues straight. Can the indices be compared from this observation alone?

**Explanation**

At normal incidence,

$$
\theta_1=\theta_2=0^\circ.
$$

Snell's law becomes

$$
n_1\sin0^\circ=n_2\sin0^\circ
\qquad\Longrightarrow\qquad
0=0.
$$

This is true for any pair of indices, so a straight ray at normal incidence does not reveal which index is larger.

By contrast, if an **oblique** ray continues without bending, then $\theta_1=\theta_2\ne0^\circ$. The common sine is nonzero and cancels from Snell's law, giving $n_1=n_2$.

```quiz
type: radio
id: normal-incidence-index-comparison
shuffle: true
content: |-
  A ray travels exactly along the normal into medium 2 and does not change direction. What can be concluded about $n_1$ and $n_2$ from the ray direction alone?
options:
- id: normal-incidence-indeterminate
  content: |-
    Their relative sizes cannot be determined.
  correct: true
  feedback: |-
    At normal incidence both angles are zero, so Snell's law reduces to $0=0$ for any positive indices. A straight normal ray therefore gives no index comparison.
- id: normal-incidence-equal
  content: |-
    $n_1=n_2$
  feedback: |-
    Equal indices do produce no bending, but normal incidence also produces no bending when the indices differ. Equality follows from an unbent oblique ray, not from a ray already traveling along the normal.
- id: normal-incidence-n2-greater
  content: |-
    $n_2>n_1$
  feedback: |-
    A bend toward the normal at oblique incidence would support this comparison. Here there is no nonzero angle to compare, so the direction alone does not show that $n_2$ is larger.
- id: normal-incidence-n1-greater
  content: |-
    $n_1>n_2$
  feedback: |-
    A bend away from the normal at oblique incidence would support this comparison. At zero incidence angle, however, every transmitted ray remains on the normal regardless of index order.
- id: both-indices-zero
  content: |-
    $n_1=n_2=0$
  feedback: |-
    Ordinary refractive indices are positive, and the zero in Snell's-law products comes from $\sin0^\circ=0$, not from either index being zero.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Apply the angle comparison to the original diagram before checking the choices.

**Explanation**

> **Question 2**
>
> Which index of refraction is larger?
>
> ![[../Source/Images/clicker2-1.jpg]]

The interface is horizontal, so the normal is vertical. The transmitted ray in medium 2 is closer to that normal than the incident ray in medium 1. Thus $\theta_2<\theta_1$, and Snell's law identifies the larger index.

```quiz
type: radio
id: khadley-snells-law-q2
shuffle: true
content: |-
  **Question 2**

  Which index of refraction is larger?

  ![[../Source/Images/clicker2-1.jpg]]
options:
- id: n1
  content: $n_1$
  feedback: |-
    The ray bends toward the normal after entering medium 2, which means its angle and speed decrease while its index increases there. Therefore $n_1$ is not the larger index.
- id: n2
  content: $n_2$
  correct: true
  feedback: |-
    Bending toward the normal means $\theta_2<\theta_1$. Snell's law then requires the transmitted medium to have the larger index, so $n_2>n_1$.
- id: indeterminate
  content: Cannot be determined
  feedback: |-
    This is an oblique ray with visibly different normal-based angles, so the bending direction is sufficient. The smaller angle in medium 2 identifies $n_2$ as the larger index.
```

---

<a id="summary"></a>
## Summary

To compare refractive indices from a ray diagram:

1. Draw or identify the normal, perpendicular to the interface.
2. Follow the incident ray from medium 1 to the transmitted ray in medium 2, then label $\theta_1$ and $\theta_2$ from the normal.
3. Make the desired index ratio the subject:
   $$
   \frac{n_2}{n_1}
   =\frac{\sin\theta_1}{\sin\theta_2}.
   $$
4. Compare the positive fraction with $1$: the larger sine in the numerator gives $n_2/n_1>1$, while the larger sine in the denominator gives $n_2/n_1<1$.
5. Pair the smaller acute angle with the larger refractive index.

Therefore, bending toward the normal means entering a higher-index medium, while bending away means entering a lower-index medium. The main trap is measuring angles from the interface instead of the normal. A second trap is treating an unbent normal-incidence ray as proof that the indices are equal; at $\theta=0^\circ$, the direction alone is inconclusive.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
