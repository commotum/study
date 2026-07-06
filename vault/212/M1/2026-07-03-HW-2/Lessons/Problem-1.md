# Recognizing Uniform Circular Motion

<!--
lesson-id: 212-M1-005
topic-code: MTH212.M1.05
-->

## Table of Contents

- [Introduction](#introduction)
- [Check the Two Required Features](#check-the-two-required-features)
- [Use Period as Evidence for Constant Speed](#use-period-as-evidence-for-constant-speed)
- [Avoid Force-Based Distractions](#avoid-force-based-distractions)
- [Choose the Best Explanation](#choose-the-best-explanation)

## Prerequisites

- Speed is the magnitude of velocity
- A period is the time for one complete cycle
- Circular motion means the path is a circle
- Uniform circular motion means motion around a circle at constant speed

---

<a id="introduction"></a>
## Introduction

Uniform circular motion has two required features:

1. The object moves on a circular path.
2. The object's speed stays constant.

The recognition cue is a question asking whether a moving object is undergoing uniform circular motion. Check the path shape and the speed first. If both are present, the motion is uniform circular motion even though the velocity direction is changing.

For the conical-pendulum question, the prompt says the bob "traverses a circular trajectory at constant speed." That phrase already matches the definition, so the answer should be yes with that exact reason.

The main trap is using extra information about forces, tension, or acceleration to avoid the definition. Those details matter later, but they are not needed to decide whether the motion is uniform circular motion.

---

<a id="check-the-two-required-features"></a>
## Check the Two Required Features

**Example:** A bead moves around a circular wire at a constant speed. Is the bead undergoing uniform circular motion?

**Explanation**

Check the definition directly.

The path is circular, and the speed is constant. Those are exactly the two features required for uniform circular motion.

So the bead is undergoing uniform circular motion.

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  A toy car moves around a circular track at constant speed. Is the toy car undergoing uniform circular motion?
options:
- id: a
  content: |-
    Yes, because it moves on a circular path at constant speed.
  correct: true
- id: b
  content: |-
    Yes, because its velocity vector is constant.
- id: c
  content: |-
    No, because the direction of its velocity changes.
- id: d
  content: |-
    No, because circular motion requires changing speed.
```

---

<a id="use-period-as-evidence-for-constant-speed"></a>
## Use Period as Evidence for Constant Speed

**Example:** A ball moves around a circle of fixed radius $r$ and completes each revolution in the same time $T$. If the motion repeats this way, what does that tell you about its speed?

**Explanation**

For one complete revolution, the distance traveled is the circumference:

$$
2\pi r.
$$

If each revolution takes the same time $T$, then the speed is

$$
v=\frac{2\pi r}{T}.
$$

With fixed $r$ and constant $T$, this speed is constant. So a fixed circular path plus a constant period is evidence of constant-speed circular motion.

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  An object travels around a circle of fixed radius $5\ \mathrm{m}$ and takes $4\ \mathrm{s}$ for each complete lap. Which statement best follows?
options:
- id: a
  content: |-
    Its speed is constant because each lap covers the same distance in the same time.
  correct: true
- id: b
  content: |-
    Its speed must be changing because the path is curved.
- id: c
  content: |-
    Its velocity vector is constant because the period is constant.
- id: d
  content: |-
    Its speed cannot be determined because the mass is not given.
```

---

<a id="avoid-force-based-distractions"></a>
## Avoid Force-Based Distractions

**Example:** A bob on a string moves in a horizontal circle at constant speed. A student says, "It might not be uniform circular motion unless the tension is constant." What is wrong with that reasoning?

**Explanation**

The question is about the type of motion, so start from the motion description.

If the bob moves in a circle and its speed is constant, then it is undergoing uniform circular motion. The forces explain how that motion happens, but the definition does not require first proving that the tension is constant.

The velocity is not constant because its direction changes. That does not make the speed nonconstant.

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  A puck moves in a circle at constant speed. Which extra fact is not needed to classify the motion as uniform circular motion?
options:
- id: a
  content: |-
    The path is circular.
- id: b
  content: |-
    The speed is constant.
- id: c
  content: |-
    The net force points inward.
  correct: true
- id: d
  content: |-
    The object keeps moving around the circle.
```

---

<a id="choose-the-best-explanation"></a>
## Choose the Best Explanation

**Example:** A bob of mass $m$ is attached to a light string of length $L$. The bob traverses a circular trajectory at constant speed when viewed from above or below. The string makes an angle $\theta$ with the horizontal, and the period of the circular motion is constant. Is the bob undergoing uniform circular motion?

![](<../Source/Images/conical-pendulum-diagram.png>)

**Explanation**

The prompt gives the two required features:

- circular trajectory
- constant speed

Therefore the bob is undergoing uniform circular motion.

The best explanation is not just "constant period" by itself. Constant period helps show constant speed only when the circular path has fixed radius. The direct reason is that the bob moves in a circular path at a constant speed.

It is also not necessary to check whether the tension is constant first. Force information explains why the bob can move that way, but the classification comes from the motion description.

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  The figures below show a bob of mass $m$ attached to a light string of length $L$ which traverses a circular trajectory at constant speed when viewed from above/below.

  The string makes an angle $\theta$ with the horizontal and the period of the circular motion is $T$ (constant).

  Is the bob undergoing uniform circular motion? Choose the correct answer with the best explanation.

  ![](<../Source/Images/conical-pendulum-diagram.png>)
options:
- id: a
  content: |-
    Yes, because the bob moves in a circular path at a constant speed
  correct: true
- id: b
  content: |-
    Not necessarily because it depends on if the tension in the string is constant
- id: c
  content: |-
    No, because even with a constant period, the bob experiences changing radial and tangential accelerations
- id: d
  content: |-
    Yes, because the bob moves in a circular path with a constant period
```

---

## Summary

To decide whether motion is uniform circular motion, check the definition first:

1. Is the path circular?
2. Is the speed constant?

If both answers are yes, the object is undergoing uniform circular motion. A constant period on a fixed circular path supports constant speed because each lap covers the same distance in the same time. Do not reject uniform circular motion just because the velocity direction changes, the object accelerates inward, or a force analysis could be done later.

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Recognizing Tangential Velocity in Circular Motion](<../../2026-06-28-HW-1/Lessons/Problem-6.md>)

Study guide index: 05/30

<!-- study-guide-nav:end -->
