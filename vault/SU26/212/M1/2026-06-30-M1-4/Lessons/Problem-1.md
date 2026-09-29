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
- [Choose from the Diagrams](#choose-from-the-diagrams)
- [Summary](#summary)

## Prerequisites

- Know that a free-body diagram shows forces acting on one object.
- Know that weight points straight downward.
- Know that a normal force is perpendicular to the contact surface.
- Know that an icy or no-friction surface has no friction force.

---

<a id="introduction"></a>
## Introduction

A car of mass $m$ rounds an icy banked curve with no friction. Which side-view free-body diagram could represent the car?

![](<../Source/Images/icy-banked-curve-free-body-diagrams.png>)

Although the car follows a curved path, the free-body diagram contains only forces produced by real interactions. Earth pulls the car downward, and the banked road pushes perpendicular to its surface. The ice matters because it removes the tire-road friction force that would otherwise act along the road.

The car still accelerates toward the center of the curve. The tilted normal force has an inward component that supplies this acceleration; circular motion does not add a separate “centripetal force” to the diagram. The correct choice therefore has only $mg$ straight down and $N$ perpendicular to the bank, pointing up and inward.

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
shuffle: true
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
shuffle: true
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

Coordinate axes may be drawn after the force list, but they are not force arrows. For this geometry, choose $+y$ vertically upward and $+r$ horizontally inward. These axes put the known accelerations directly on the axes: $a_y=0$ and $a_r=v^2/r$. Axes rotated with the bank are possible, but they would split the circular acceleration into components.

```quiz
type: radio
id: q-p1-extra-arrow
shuffle: true
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

<a id="choose-from-the-diagrams"></a>
## Choose from the Diagrams

**Example:** Compare choices A–E in the drawing from the introduction. A correct diagram must satisfy both physical requirements:

- It has exactly two arrows: $mg$ and $N$.
- $mg$ points straight down, while $N$ points perpendicular to the banked surface, up and inward.

A diagram with a downward arrow, an up-left perpendicular arrow, and an extra leftward arrow fails because that extra arrow treats the inward net-force requirement as a third force.

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

On an icy banked curve, the car interacts only with Earth and the road. Its free-body diagram therefore has $mg$ straight down and $N$ perpendicular to the bank. The inward component of $N$ turns the car; it does not require an additional centripetal-force arrow.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Finding the Speed for a Frictionless Banked Curve](Problem-4.md)

Study guide index: 22/35

---
<!-- lesson-nav:end -->
