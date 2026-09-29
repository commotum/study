# Exact Diffraction-Grating Positions on a Screen

<!--
lesson-id: 212-M6-017
topic-code: MTH212.M6.17
-->
## Table of Contents

- [Introduction](#introduction)
- [Turn the Order Into a Sine Ratio](#turn-the-order-into-a-sine-ratio)
- [Convert Sine to Tangent](#convert-sine-to-tangent)
- [Use Tangent for the Screen Position](#use-tangent-for-the-screen-position)
- [Keep the Geometry Exact](#keep-the-geometry-exact)
- [Summary](#summary)

## Prerequisites

- Use the diffraction-grating maximum condition $d\sin\theta=m\lambda$.
- Recognize sine and tangent as right-triangle side ratios.
- Find a missing side with the Pythagorean theorem.

---

<a id="introduction"></a>
## Introduction

When a problem gives a grating order and asks for a **linear distance on a flat screen**, two different triangles are involved in the reasoning:

1. The grating condition determines the angle through

   $$
   d\sin\theta=m\lambda.
   $$

2. The screen geometry turns that angle into a vertical distance through

   $$
   \tan\theta=\frac{y}{L}
   \qquad\Longrightarrow\qquad
   y=L\tan\theta.
   $$

The key cue is the phrase **distance from the central maximum on a screen**. The grating equation supplies $\sin\theta$, but the requested screen coordinate uses $\tan\theta$. Unless a small-angle approximation is explicitly justified, do not replace $\tan\theta$ with $\sin\theta$.

Keep these roles separate:

- $m\lambda/d$ is the **sine ratio** fixed by interference.
- $L$ is the **adjacent leg** of the screen triangle.
- $y$ is the **opposite leg**, so $y/L$ is the tangent ratio.

---

<a id="turn-the-order-into-a-sine-ratio"></a>
## Turn the Order Into a Sine Ratio

**Example:** A grating has spacing $d=13\lambda$. Find $\sin\theta$ for its fifth-order maximum.

**Explanation**

For a bright maximum of order $m$,

$$
d\sin\theta=m\lambda.
$$

Here $m=5$ and $d=13\lambda$, so

$$
13\lambda\sin\theta=5\lambda
\qquad\Longrightarrow\qquad
\sin\theta=\frac{5}{13}.
$$

The wavelength cancels. At this stage, the result is an angular ratio, not yet a distance on the screen.

```quiz
type: radio
id: p7-order-sine
shuffle: true
content: |-
  A diffraction grating has spacing $d=10\lambda$. What is $\sin\theta$ for the sixth-order maximum?
options:
- id: p7-order-sine-a
  content: |-
    $\dfrac{3}{5}$
  correct: true
  feedback: |-
    A grating maximum obeys $d\sin\theta=m\lambda$. Substituting $d=10\lambda$ and $m=6$ gives $\sin\theta=6\lambda/(10\lambda)=3/5$.
- id: p7-order-sine-b
  content: |-
    $\dfrac{5}{3}$
  feedback: |-
    This reverses the grating ratio. Solving $d\sin\theta=m\lambda$ gives $m\lambda/d$, not $d/(m\lambda)$; the reversed value also exceeds the allowed range of sine.
- id: p7-order-sine-c
  content: |-
    $\dfrac{1}{10}$
  feedback: |-
    The ratio $\lambda/d=1/10$ describes the first-order maximum. The order number multiplies the wavelength, so the sixth order requires $6\lambda/d=3/5$.
- id: p7-order-sine-d
  content: |-
    $\dfrac{4}{5}$
  feedback: |-
    The value $4/5$ is the cosine associated with a $3$-$4$-$5$ triangle after $\sin\theta=3/5$ is known. The grating equation itself fixes the sine ratio at $3/5$.
```

---

<a id="convert-sine-to-tangent"></a>
## Convert Sine to Tangent

**Example:** An acute diffraction angle satisfies $\sin\theta=5/13$. Find $\tan\theta$ exactly.

**Explanation**

Interpret $\sin\theta=5/13$ as a right triangle with opposite side $5$ and hypotenuse $13$. The adjacent side is

$$
\sqrt{13^2-5^2}=\sqrt{169-25}=12.
$$

The diffraction angle is acute for a finite positive-order maximum on one side of the screen, so the adjacent length is the positive root.

Therefore,

$$
\tan\theta
=\frac{\text{opposite}}{\text{adjacent}}
=\frac{5}{12}.
$$

Equivalently, first find $\cos\theta=12/13$ and then use $\tan\theta=\sin\theta/\cos\theta$.

```quiz
type: radio
id: p7-sine-tangent
shuffle: true
content: |-
  A diffraction angle is acute and satisfies $\sin\theta=\dfrac{8}{17}$. What is $\tan\theta$?
options:
- id: p7-sine-tangent-a
  content: |-
    $\dfrac{8}{17}$
  feedback: |-
    This repeats the sine ratio, opposite over hypotenuse. Tangent needs opposite over adjacent, so first use the Pythagorean theorem to find the adjacent side $15$.
- id: p7-sine-tangent-b
  content: |-
    $\dfrac{15}{8}$
  feedback: |-
    With opposite side $8$ and adjacent side $15$, the ratio $15/8$ is $\cot\theta$. Tangent keeps the opposite side in the numerator, giving $8/15$.
- id: p7-sine-tangent-c
  content: |-
    $\dfrac{15}{17}$
  feedback: |-
    The Pythagorean theorem does give the adjacent side $15$, but $15/17$ is $\cos\theta$, adjacent over hypotenuse. Tangent compares the two legs instead.
- id: p7-sine-tangent-d
  content: |-
    $\dfrac{8}{15}$
  correct: true
  feedback: |-
    Since $8^2+15^2=17^2$, $\sin\theta=8/17$ corresponds to opposite side $8$ and adjacent side $15$. Thus $\tan\theta=8/15$.
```

---

<a id="use-tangent-for-the-screen-position"></a>
## Use Tangent for the Screen Position

**Example:** A grating has $d=13\lambda$, and a screen is a distance $L$ away. Find the fifth-order maximum's distance from the central maximum.

**Explanation**

First use the grating equation:

$$
\sin\theta=\frac{m\lambda}{d}=\frac{5}{13}.
$$

The corresponding right triangle has side ratio $5$-$12$-$13$, so $\tan\theta=5/12$. On the screen, the opposite side is $y$ and the adjacent side is $L$:

$$
\tan\theta=\frac{y}{L}
\qquad\Longrightarrow\qquad
y=L\tan\theta=\frac{5L}{12}.
$$

```quiz
type: radio
id: p7-source-check
shuffle: true
content: |-
  **Question 7**

  A diffraction grating has slit spacing

  $$
  d=5\lambda.
  $$

  A screen is located a distance $L$ from the grating. What is the distance $y$ from the central maximum to the third-order maximum?
options:
- id: p7-source-check-a
  content: |-
    $\dfrac{3L}{5}$
  feedback: |-
    The grating equation gives $\sin\theta=3/5$, but $3L/5$ treats that sine ratio as the screen slope. A flat screen uses $y/L=\tan\theta$, so the adjacent side must be found before computing $y$.
- id: p7-source-check-b
  content: |-
    $\dfrac{4L}{5}$
  feedback: |-
    From $\sin\theta=3/5$, the ratio $4/5$ is $\cos\theta$, adjacent over hypotenuse. The screen displacement is the opposite leg $y$, and $y/L$ is tangent rather than cosine.
- id: p7-source-check-c
  content: |-
    $\dfrac{5L}{4}$
  feedback: |-
    The factor $5/4$ is $\sec\theta$, the reciprocal of $\cos\theta=4/5$. Screen geometry instead requires $\tan\theta=3/4$, which compares the vertical displacement with the horizontal distance $L$.
- id: p7-source-check-d
  content: |-
    $\dfrac{3L}{4}$
  correct: true
  feedback: |-
    The third-order maximum obeys $d\sin\theta=3\lambda$, so $d=5\lambda$ gives $\sin\theta=3/5$. The resulting $3$-$4$-$5$ triangle has $\tan\theta=3/4$, and therefore $y=L\tan\theta=3L/4$.
```

---

<a id="keep-the-geometry-exact"></a>
## Keep the Geometry Exact

**Example:** A grating with $d=10\lambda$ produces an eighth-order maximum. Compare its exact screen position with the small-angle shortcut $y\approx L\sin\theta$.

**Explanation**

The grating equation gives

$$
\sin\theta=\frac{8}{10}=\frac{4}{5}.
$$

An acute angle with sine $4/5$ has cosine $3/5$, so

$$
\tan\theta=\frac{4/5}{3/5}=\frac{4}{3}.
$$

Thus the exact location is

$$
y=L\tan\theta=\frac{4L}{3},
$$

whereas the shortcut would give only $4L/5$. The two are close only when $\theta$ is small enough that $\tan\theta\approx\sin\theta$.

For the useful form $d=k\lambda$, the exact calculation can be compressed to

$$
\sin\theta=\frac{m}{k},
\qquad
\cos\theta=\frac{\sqrt{k^2-m^2}}{k},
\qquad
\tan\theta=\frac{m}{\sqrt{k^2-m^2}},
\qquad
y=\frac{mL}{\sqrt{k^2-m^2}}.
$$

The positive cosine is chosen because the screen-facing diffraction angle is acute. This finite-screen formula requires $m<k$. If $m>k$, the proposed order cannot exist because it would require $\sin\theta>1$; if $m=k$, the ray is parallel to the screen and has no finite screen coordinate.

```quiz
type: radio
id: p7-exact-geometry
shuffle: true
content: |-
  A grating has spacing $d=17\lambda$, and a screen is a distance $L$ away. What is the exact distance from the central maximum to the eighth-order maximum?
options:
- id: p7-exact-geometry-a
  content: |-
    $\dfrac{8L}{17}$
  feedback: |-
    The grating equation does give $\sin\theta=8/17$, but multiplying that sine by $L$ is only a small-angle shortcut. The exact screen coordinate uses $L\tan\theta$.
- id: p7-exact-geometry-b
  content: |-
    $\dfrac{15L}{17}$
  feedback: |-
    Completing the $8$-$15$-$17$ triangle makes $15/17$ the cosine ratio. Cosine compares the horizontal leg with the ray path; it does not give the vertical screen displacement per horizontal distance.
- id: p7-exact-geometry-c
  content: |-
    $\dfrac{17L}{15}$
  feedback: |-
    The factor $17/15$ is $\sec\theta$, which compares the ray path with the horizontal leg. The screen position instead uses tangent, opposite over adjacent.
- id: p7-exact-geometry-d
  content: |-
    $\dfrac{8L}{15}$
  correct: true
  feedback: |-
    The eighth-order condition gives $\sin\theta=8/17$. Completing the $8$-$15$-$17$ triangle gives $\tan\theta=8/15$, so the exact screen distance is $y=L\tan\theta=8L/15$.
```

---

<a id="summary"></a>
## Summary

For an order-$m$ diffraction maximum on a flat screen:

1. Use $d\sin\theta=m\lambda$ to find $\sin\theta$.
2. Complete the right triangle, or use $\cos\theta=\sqrt{1-\sin^2\theta}$, to find $\tan\theta$.
3. Use $y=L\tan\theta$ for the exact screen coordinate.
4. Check that $m\lambda<d$ for a maximum at a finite location on the screen.

The main trap is using $L\sin\theta$. That is a small-angle approximation, not the exact flat-screen geometry.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
