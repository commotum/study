# Ranking Radial Accelerations

<!--
lesson-id: 212-M1-003
topic-code: MTH212.M1.03
-->

## Table of Contents

- [Introduction](#introduction)
- [Calculate Radial Acceleration From Speed and Radius](#calculate-radial-acceleration-from-speed-and-radius)
- [Use the Square on Speed](#use-the-square-on-speed)
- [Use the Radius in the Denominator](#use-the-radius-in-the-denominator)
- [Rank Several Circular Motions](#rank-several-circular-motions)
- [Check the Common Trap](#check-the-common-trap)
- [Summary](#summary)

## Prerequisites

- Recognize speed $v$ and radius $r$ in a circular-motion diagram.
- Square small whole numbers.
- Be able to compare simple numbers and fractions.

---

<a id="introduction"></a>
## Introduction

When a problem shows objects moving in circles and gives each object's speed and radius, rank radial acceleration by using

$$
a_r=\frac{v^2}{r}.
$$

The direction of the velocity arrow tells you the object is moving around the circle, but the size of radial acceleration depends on the speed squared and the radius. Faster motion raises $a_r$ a lot because $v$ is squared. A larger radius lowers $a_r$ because $r$ is in the denominator.

Use this procedure:

1. Record each object's $v$ and $r$.
2. Compute the comparison value $v^2/r$.
3. Rank those values from least to greatest.

---

<a id="calculate-radial-acceleration-from-speed-and-radius"></a>
## Calculate Radial Acceleration From Speed and Radius

**Example:** An object moves in uniform circular motion with speed $v=3\ \mathrm{m/s}$ and radius $r=2\ \mathrm{m}$. Find its radial acceleration.

**Explanation**

For circular motion, the radial acceleration magnitude is

$$
a_r=\frac{v^2}{r}.
$$

Here, $v=3$ and $r=2$, so

$$
a_r=\frac{(3\ \mathrm{m/s})^2}{2\ \mathrm{m}}
=\frac{9}{2}\ \mathrm{m/s^2}
=4.5\ \mathrm{m/s^2}.
$$

Square the speed before dividing by the radius.

```quiz
type: radio
id: radial-acceleration-calculate
content: |-
  An object moves in a circle with speed $v=4\ \mathrm{m/s}$ and radius $r=2\ \mathrm{m}$. What is its radial acceleration magnitude?
options:
- id: a
  content: |-
    $2\ \mathrm{m/s^2}$
- id: b
  content: |-
    $4\ \mathrm{m/s^2}$
- id: c
  content: |-
    $8\ \mathrm{m/s^2}$
  correct: true
- id: d
  content: |-
    $16\ \mathrm{m/s^2}$
- id: e
  content: |-
    $6\ \mathrm{m/s^2}$
```

---

<a id="use-the-square-on-speed"></a>
## Use the Square on Speed

**Example:** Objects P and Q move in circles with the same radius, $r=1\ \mathrm{m}$. Object P has $v=1\ \mathrm{m/s}$, and object Q has $v=2\ \mathrm{m/s}$. Compare their radial accelerations.

**Explanation**

Because the radii match, compare $v^2$:

$$
a_{r,P}=\frac{1^2}{1}=1,
\qquad
a_{r,Q}=\frac{2^2}{1}=4.
$$

Doubling the speed makes the radial acceleration four times as large when the radius stays the same. So $P<Q$.

```quiz
type: radio
id: radial-acceleration-same-radius
content: |-
  Objects R and S move in circles with the same radius. R has $v=2\ \mathrm{m/s}$, and S has $v=3\ \mathrm{m/s}$. Which comparison of radial accelerations is correct?
options:
- id: a
  content: |-
    $R<S$
  correct: true
- id: b
  content: |-
    $R=S$
- id: c
  content: |-
    $R>S$
- id: d
  content: |-
    There is not enough information because direction is missing.
- id: e
  content: |-
    $S$ is only $\frac{3}{2}$ times as large as $R$ because acceleration depends linearly on speed.
```

---

<a id="use-the-radius-in-the-denominator"></a>
## Use the Radius in the Denominator

**Example:** Objects M and N move with the same speed, $v=2\ \mathrm{m/s}$. Object M has radius $r=1\ \mathrm{m}$, and object N has radius $r=2\ \mathrm{m}$. Compare their radial accelerations.

**Explanation**

Because the speeds match, the numerator $v^2$ is the same for both objects:

$$
a_{r,M}=\frac{2^2}{1}=4,
\qquad
a_{r,N}=\frac{2^2}{2}=2.
$$

With the same speed, the smaller radius gives the larger radial acceleration. So $N<M$.

```quiz
type: radio
id: radial-acceleration-same-speed
content: |-
  Objects T and U move with the same speed. T has radius $r=3\ \mathrm{m}$, and U has radius $r=6\ \mathrm{m}$. Which comparison of radial accelerations is correct?
options:
- id: a
  content: |-
    $T<U$
- id: b
  content: |-
    $T=U$
- id: c
  content: |-
    $T>U$
  correct: true
- id: d
  content: |-
    Radius does not affect radial acceleration.
- id: e
  content: |-
    $U>T$ because U has the larger circle.
```

---

<a id="rank-several-circular-motions"></a>
## Rank Several Circular Motions

**Example:** Rank the radial accelerations in the diagram from least to greatest.

![](<../Source/Images/radial-acceleration-ranking.png>)

**Explanation**

The units match across all four objects, so it is enough to compute the comparison value $v^2/r$ for each object:

| Object | Speed | Radius | $v^2/r$ |
|---|---:|---:|---:|
| A | $1\ \mathrm{m/s}$ | $1\ \mathrm{m}$ | $1^2/1=1$ |
| B | $2\ \mathrm{m/s}$ | $1\ \mathrm{m}$ | $2^2/1=4$ |
| C | $2\ \mathrm{m/s}$ | $2\ \mathrm{m}$ | $2^2/2=2$ |
| D | $1\ \mathrm{m/s}$ | $2\ \mathrm{m}$ | $1^2/2=0.5$ |

Now rank the values from least to greatest:

$$
D<A<C<B.
$$

```quiz
type: radio
id: radial-acceleration-four-object-ranking
content: |-
  Four objects have these $(v,r)$ pairs, with speed in $\mathrm{m/s}$ and radius in $\mathrm{m}$: A $(1,1)$, B $(3,1)$, C $(2,2)$, and D $(1,4)$. Rank their radial accelerations from least to greatest.
options:
- id: a
  content: |-
    $D<A<C<B$
  correct: true
- id: b
  content: |-
    $A<D<C<B$
- id: c
  content: |-
    $D<A<B<C$
- id: d
  content: |-
    $A<C<D<B$
- id: e
  content: |-
    $D<C<A<B$
```

---

<a id="check-the-common-trap"></a>
## Check the Common Trap

**Example:** A student ranks the original diagram as $D<A<B<C$ because B and C both have speed $2\ \mathrm{m/s}$ and C is drawn larger. What went wrong?

**Explanation**

The larger circle does not make the radial acceleration larger. For radial acceleration,

$$
a_r=\frac{v^2}{r}.
$$

The radius is in the denominator, so a larger radius lowers $a_r$ when speed is fixed. B and C have the same speed, but B has $r=1\ \mathrm{m}$ and C has $r=2\ \mathrm{m}$:

$$
a_{r,B}=4,
\qquad
a_{r,C}=2.
$$

So B must be greater than C.

```quiz
type: radio
id: radial-acceleration-trap-check
content: |-
  Two objects have the same speed. Object X moves in a circle of radius $2\ \mathrm{m}$, and object Y moves in a circle of radius $5\ \mathrm{m}$. Which statement is true?
options:
- id: a
  content: |-
    X has the greater radial acceleration because its radius is smaller.
  correct: true
- id: b
  content: |-
    Y has the greater radial acceleration because its circle is larger.
- id: c
  content: |-
    X and Y have equal radial acceleration because their speeds match.
- id: d
  content: |-
    The object with the longer velocity arrow must have the greater radial acceleration.
- id: e
  content: |-
    The object moving clockwise has the greater radial acceleration.
```

---

<a id="summary"></a>
## Summary

When ranking radial accelerations in uniform circular motion, read each speed $v$ and radius $r$, then compare $v^2/r$.

1. Square the speed.
2. Divide by the radius.
3. Rank the resulting values.

The main trap is comparing only speed or only circle size. Speed is squared, and radius is in the denominator, so a faster object can outrank a larger-radius object even when the diagrams look similar.

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Checking the Magnitude of Centripetal Acceleration](<../../2026-06-28-HW-1/Lessons/Problem-9.md>)

Study guide index: 03/30

<!-- study-guide-nav:end -->
