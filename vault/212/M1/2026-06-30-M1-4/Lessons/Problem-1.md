# Choosing a Free-Body Diagram for an Icy Banked Curve

<!--
lesson-id: 212-M1-021
topic-code: MTH212.M1.21
-->

## Table of Contents

- [Introduction](#introduction)
- [Start With Real Forces](#start-with-real-forces)
- [Point Weight and Normal](#point-weight-and-normal)
- [Reject Extra Motion Arrows](#reject-extra-motion-arrows)
- [Match the Diagram](#match-the-diagram)
- [Summary](#summary)

## Prerequisites

- Know that a free-body diagram shows forces acting on one object.
- Know that weight points straight downward.
- Know that a normal force is perpendicular to the contact surface.
- Know that an icy or no-friction surface has no friction force.

---

<a id="introduction"></a>
## Introduction

When a car moves around an icy banked curve, the cue is the phrase **icy** or **no friction**. That cue removes friction from the free-body diagram. The diagram should include only the real forces acting on the car: weight downward and the normal force perpendicular to the road surface.

The curve still requires inward acceleration, but that does not create a new "centripetal force" arrow. The inward part of the normal force is what helps provide the inward net force.

Use a two-pass filter:

1. Count the real forces. On an icy banked curve, there should be exactly two.
2. Check the directions. Weight is vertical; the normal force is perpendicular to the road.

---

<a id="start-with-real-forces"></a>
## Start With Real Forces

**Example:** A car moves on an icy banked road. There is no friction, no rope, and no engine force shown in the side-view diagram. Which forces belong on the free-body diagram?

**Explanation**

Start by listing real interactions:

- Earth pulls on the car, so include weight $mg$ straight downward.
- The road pushes on the car, so include a normal force $N$ perpendicular to the road.
- The road is icy, so do not include friction.

So the force list is $mg$ and $N$ only.

```quiz
type: radio
id: q-p1-force-list
content: |-
  A car travels around an icy banked curve with no friction. Which list contains all the forces that should appear in the car's free-body diagram?
options:
- id: a
  content: |-
    Weight only
- id: b
  content: |-
    Weight and normal force
  correct: true
  feedback: |-
    The icy road removes friction, leaving only gravity and the road's normal force.
- id: c
  content: |-
    Weight, normal force, and friction
- id: d
  content: |-
    Weight, normal force, and a separate centripetal force
- id: e
  content: |-
    Normal force, friction, and velocity
```

---

<a id="point-weight-and-normal"></a>
## Point Weight and Normal

**Example:** In a side view, the banked road slopes upward to the right, and the center of the circular path is to the left of the car. What directions should the two force arrows have?

**Explanation**

Weight always points vertically downward, no matter how the road is tilted.

The normal force points perpendicular to the road surface, away from the road. Since the road slopes upward to the right, the perpendicular normal points upward and left. That leftward component points toward the center of the circular path.

The normal force does not point left just because the center is left. It points perpendicular to the road; in this geometry, that perpendicular arrow has an inward component.

```quiz
type: radio
id: q-p1-arrow-directions
content: |-
  A car is on an icy banked road that slopes upward to the right. The center of the circular path is to the left. Which force directions are correct?
options:
- id: a
  content: |-
    $mg$ points down, and $N$ points straight up.
- id: b
  content: |-
    $mg$ points down, and $N$ points perpendicular to the road, up and left.
  correct: true
  feedback: |-
    Weight is vertical, while the normal force is perpendicular to the tilted road.
- id: c
  content: |-
    $mg$ points down the slope, and $N$ points straight up.
- id: d
  content: |-
    $mg$ points toward the center, and $N$ points perpendicular to the road.
- id: e
  content: |-
    $mg$ points down, and $N$ points parallel to the road, up the slope.
```

---

<a id="reject-extra-motion-arrows"></a>
## Reject Extra Motion Arrows

**Example:** A proposed free-body diagram for an icy banked curve shows $mg$ downward, $N$ up and left, and one extra horizontal arrow labeled "centripetal force" pointing left. Should that extra arrow be included?

**Explanation**

No. "Centripetal" describes the direction of the net force needed for circular motion. It is not an additional interaction force. In this situation, the inward part of $N$ contributes to the inward net force.

The same test rejects a friction arrow. Since the road is icy, friction is absent.

```quiz
type: radio
id: q-p1-extra-arrow
content: |-
  A free-body diagram for an icy banked curve includes $mg$ downward, $N$ perpendicular to the road, and a friction arrow down the slope. What is wrong?
options:
- id: a
  content: |-
    The diagram should include no normal force.
- id: b
  content: |-
    The friction arrow should point up the slope instead.
- id: c
  content: |-
    The friction arrow should be removed because the surface is icy.
  correct: true
  feedback: |-
    Icy or no-friction means friction does not appear in the free-body diagram.
- id: d
  content: |-
    The weight arrow should point perpendicular to the road.
- id: e
  content: |-
    The normal force should point toward the car's velocity.
```

---

<a id="match-the-diagram"></a>
## Match the Diagram

**Example:** Suppose the answer choices show several side-view diagrams. The correct diagram must pass both tests:

- It has exactly two arrows: $mg$ and $N$.
- $mg$ points straight down, while $N$ points perpendicular to the banked surface, up and inward.

For example, a diagram with a downward arrow, an up-left perpendicular arrow, and an extra leftward arrow should be rejected. The first two arrows are correct, but the extra leftward arrow treats centripetal acceleration as if it were a separate force.

```quiz
type: radio
id: q-p1-original-match
content: |-
  ![](<../Source/Images/icy-banked-curve-free-body-diagrams.png>)

  A car of mass $m$ is going around an icy banked curve with no friction. Which free-body diagram, in side view, could represent the car?
options:
- id: a
  content: |-
    A
- id: b
  content: |-
    B
  correct: true
  feedback: |-
    The curve is icy, so there is no friction. The only forces are gravity downward and the normal force perpendicular to the surface, pointing up and toward the center of the curve.
- id: c
  content: |-
    C
- id: d
  content: |-
    D
- id: e
  content: |-
    E
```

In the given choices, the incorrect diagrams fail for specific reasons:

- A has extra horizontal arrows and no tilted normal force.
- C has the correct two main arrows, but adds an extra inward arrow.
- D adds extra horizontal arrows.
- E adds an extra rightward arrow.

Only B has exactly the two real forces with the correct directions.

---

<a id="summary"></a>
## Summary

For an icy banked curve, use this checklist:

1. Include only real forces on the car.
2. Icy means no friction.
3. Weight points straight down.
4. The normal force points perpendicular to the road, away from the surface.
5. Do not add a separate centripetal-force arrow; circular motion describes the net force direction, not a new force.

The correct side-view diagram has exactly two arrows: $mg$ downward and $N$ perpendicular to the bank, tilted inward.

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Finding the Speed for a Frictionless Banked Curve](<Problem-4.md>)

Study guide index: 21/30

<!-- study-guide-nav:end -->
