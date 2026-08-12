# Comparing Angular Momentum at Equal Angular Speed

<!--
lesson-id: 212-M3-019
topic-code: MTH212.M3.19
-->

## Table of Contents

- [Introduction](#introduction)
- [Cancel the Shared Angular Speed](#cancel-the-shared-angular-speed)
- [Use Distance From the Axis](#use-distance-from-the-axis)
- [Read a Posture Diagram](#read-a-posture-diagram)
- [Avoid the Equal-Mass Trap](#avoid-the-equal-mass-trap)
- [Summary](#summary)

## Prerequisites

- Recognize angular speed $\omega$ as the rate of rotation.
- Identify the perpendicular distance $r$ from a piece of mass to the rotation axis.
- Compare positive quantities and their squares.

---

<a id="introduction"></a>
## Introduction

For an object rotating about a fixed axis, angular momentum has magnitude

$$
L=I\omega,
$$

where $I$ is the object's moment of inertia and $\omega$ is its angular speed.

The recognition cue is a comparison of rotating objects that have the **same angular speed**. In that case, $\omega$ cannot decide the ranking. Compare the moments of inertia instead. The object with more of its mass farther from the axis has the larger $I$, so it also has the larger $L$.

Use this comparison chain:

$$
\text{same }\omega
\quad\Longrightarrow\quad
\text{compare }I
\quad\Longrightarrow\quad
\text{compare the mass distances }r.
$$

If the objects also have the same total mass, do **not** stop there. Ask where that mass is located relative to the rotation axis.

---

<a id="cancel-the-shared-angular-speed"></a>
## Cancel the Shared Angular Speed

**Example:** Two point masses rotate about the same axis. Mass A has $I_A=2\ \mathrm{kg}\,\mathrm{m}^2$ and mass B has $I_B=5\ \mathrm{kg}\,\mathrm{m}^2$. Both rotate with angular speed $3\ \mathrm{rad}/\mathrm{s}$. Which has the larger angular momentum?

**Explanation**

Use $L=I\omega$:

$$
L_A=(2)(3)=6\ \mathrm{kg}\,\mathrm{m}^2/\mathrm{s},
$$

$$
L_B=(5)(3)=15\ \mathrm{kg}\,\mathrm{m}^2/\mathrm{s}.
$$

Because the angular speeds are equal, the larger moment of inertia gives the larger angular momentum. Mass B has the larger $L$.

```quiz
type: radio
id: p1-equal-omega
content: |-
  Rotors P and Q spin with the same angular speed. Their moments of inertia are $I_P=7\ \mathrm{kg}\,\mathrm{m}^2$ and $I_Q=4\ \mathrm{kg}\,\mathrm{m}^2$. Which rotor has the larger angular momentum magnitude?
options:
- id: a
  content: |-
    Rotor P
  correct: true
- id: b
  content: |-
    Rotor Q
- id: c
  content: |-
    They have equal angular momentum because their angular speeds match.
- id: d
  content: |-
    There is not enough information because the common angular speed is not given numerically.
```

---

<a id="use-distance-from-the-axis"></a>
## Use Distance From the Axis

**Example:** Two identical small masses are attached to massless rods and rotate at the same angular speed. One mass is $1\ \mathrm{m}$ from its axis; the other is $2\ \mathrm{m}$ from its axis. Which system has the larger angular momentum?

**Explanation**

For a point mass,

$$
I=mr^2.
$$

The masses and angular speeds are the same, so only $r^2$ changes:

$$
I_{1}=m(1)^2=m,
$$

$$
I_{2}=m(2)^2=4m.
$$

The mass at $2\ \mathrm{m}$ has four times the moment of inertia and therefore four times the angular momentum. Distance matters through $r^2$, not just through $r$.

```quiz
type: radio
id: p1-radius-squared
content: |-
  Two identical small masses rotate with the same angular speed. Mass X is a distance $r$ from the axis, while mass Y is a distance $3r$ from the axis. How do their angular momenta compare?
options:
- id: a
  content: |-
    $L_Y=9L_X$
  correct: true
- id: b
  content: |-
    $L_Y=3L_X$
- id: c
  content: |-
    $L_Y=L_X$
- id: d
  content: |-
    $L_Y=\frac{1}{9}L_X$
- id: e
  content: |-
    $L_Y=\frac{1}{3}L_X$
```

---

<a id="read-a-posture-diagram"></a>
## Read a Posture Diagram

**Example:** Three identical droids spin with the same angular speed. Droid A holds both arms close to its body, droid B extends its arms partway, and droid C extends both arms farthest from the rotation axis.

![](<../Source/2026-07-19-PQ-2/Images/problem-1-droid-angular-momentum.png>)

Which droid has the largest angular momentum?

**Explanation**

For a distributed body, imagine splitting it into small pieces:

$$
I=\sum_i m_i r_i^2.
$$

The droids are identical, so their total masses are equal. Their shared angular speed is also equal. The difference is the distance of the arm mass from the axis. Droid C places the most arm mass at the largest radii, giving it the largest moment of inertia. Therefore,

$$
L_C>L_B>L_A.
$$

Droid C has the largest angular momentum.

```quiz
type: radio
id: p1-original-check
content: |-
  Three identical droids are spinning on a frictionless block of ice. Each droid has the same angular speed. Which droid has the largest angular momentum?

  ![](<../Source/2026-07-19-PQ-2/Images/problem-1-droid-angular-momentum.png>)
options:
- id: a
  content: |-
    Droid A
- id: b
  content: |-
    Droid B
- id: c
  content: |-
    Droid C
  correct: true
- id: d
  content: |-
    All three droids have the same angular momentum
```

```quiz
type: radio
id: p1-posture
content: |-
  Three identical skaters rotate with the same angular speed. Skater R keeps both arms against the torso, skater S extends one arm, and skater T extends both arms. Assume their other body positions match. Which skater has the largest angular momentum magnitude?
options:
- id: a
  content: |-
    Skater R, because compact objects rotate most easily.
- id: b
  content: |-
    Skater S, because an unbalanced posture creates the most angular momentum.
- id: c
  content: |-
    Skater T, because the most mass is far from the axis.
  correct: true
- id: d
  content: |-
    All three, because their masses and angular speeds are equal.
- id: e
  content: |-
    The direction of rotation is needed before their magnitudes can be compared.
```

---

<a id="avoid-the-equal-mass-trap"></a>
## Avoid the Equal-Mass Trap

**Example:** Two identical dancers turn with the same angular speed. One holds two equal hand weights next to the chest; the other holds the same weights at arm's length. A student says their angular momenta must be equal because both dancers have the same total mass. Is the student correct?

**Explanation**

No. Total mass alone does not determine moment of inertia. Moment of inertia depends on both the amount of mass and its distance from the axis:

$$
I=\sum_i m_i r_i^2.
$$

Holding the weights farther out increases their $r_i^2$ contributions. At the same angular speed, the dancer holding the weights at arm's length has the larger angular momentum.

```quiz
type: radio
id: p1-equal-mass-trap
content: |-
  Two wheels have equal total mass and spin with the same angular speed. Wheel U concentrates most of its mass near the hub. Wheel V concentrates most of its mass near the rim. Which statement is correct?
options:
- id: a
  content: |-
    Wheel U has larger angular momentum because its mass is closer to the axis.
- id: b
  content: |-
    Wheel V has larger angular momentum because its mass is farther from the axis.
  correct: true
- id: c
  content: |-
    Their angular momenta are equal because their total masses are equal.
- id: d
  content: |-
    Their angular momenta are equal because their angular speeds are equal.
- id: e
  content: |-
    Their angular momenta cannot be compared without knowing the numerical angular speed.
```

---

<a id="summary"></a>
## Summary

When rotating objects have the same angular speed:

1. Start with $L=I\omega$.
2. Check for the cue **same $\omega$**.
3. Treat the shared $\omega$ as a common positive factor, so the angular-momentum ranking is the moment-of-inertia ranking.
4. Compare mass distribution using $I=\sum_i m_i r_i^2$.
5. Choose the object with more mass farther from the axis.

The main trap is assuming that equal total mass and equal angular speed imply equal angular momentum. They do not: the radial distribution of the mass can make the moments of inertia different.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Scaling Force With an Inverse-Square Law](../../2026-07-15-M3-1/Lessons/Problem-1.md)

Study guide index: 12/20

---
<!-- lesson-nav:end -->
