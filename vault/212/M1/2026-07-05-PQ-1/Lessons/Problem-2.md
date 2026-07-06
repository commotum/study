# Reading Net Force Arrows for Circular Motion

<!--
lesson-id: 212-M1-010
topic-code: MTH212.M1.10
-->

## Table of Contents

- [Introduction](#introduction)
- [Split the Net Force Into Radial and Tangential Parts](#split-the-net-force-into-radial-and-tangential-parts)
- [Use Motion Direction to Find the Tangent Direction](#use-motion-direction-to-find-the-tangent-direction)
- [Use Speeding Up or Slowing Down](#use-speeding-up-or-slowing-down)
- [Choose the Matching Diagram](#choose-the-matching-diagram)
- [Summary](#summary)

## Prerequisites

- Recognize that a particle moving in a circle has an inward centripetal acceleration.
- Identify the tangent direction at a point on a circle.
- Know that a net force component in the direction of motion speeds an object up, while a component opposite the motion slows it down.

---

<a id="introduction"></a>
## Introduction

When a particle moves around a circle and changes speed, the net force must do two jobs at the same time. One component points inward, toward the center, to bend the path. The other component points along the tangent, either with the motion or against the motion.

Use the stated direction of motion and whether the particle is speeding up or slowing down to decide which way the tangential component points. Then combine it with the inward component to choose the net-force arrow.

The repeatable check is:

1. Point inward toward the center.
2. Point tangent in the direction of motion.
3. Flip the tangent part if the particle is slowing down.
4. Choose the single arrow that combines the inward part and the correct tangent part.

---

<a id="split-the-net-force-into-radial-and-tangential-parts"></a>
## Split the Net Force Into Radial and Tangential Parts

**Example:** A particle is at the left side of a circle. Which part of the net force must always point toward the center of the circle?

**Explanation**

At the left side of the circle, the center is to the right of the particle. So the radial part of the net force points right.

This inward part is needed even if the particle's speed is constant. It changes the direction of the velocity so the path curves.

If the speed is changing, the full net force is not usually straight inward. It must still include this inward part, but it also needs a tangential part.

```quiz
type: radio
id: q-radial-left
content: |-
  A particle is at the top of a circle. Which direction is the inward radial part of the net force?
options:
- id: a
  content: |-
    Up
- id: b
  content: |-
    Down
  correct: true
- id: c
  content: |-
    Left
- id: d
  content: |-
    Right
```

---

<a id="use-motion-direction-to-find-the-tangent-direction"></a>
## Use Motion Direction to Find the Tangent Direction

**Example:** A particle is at the left side of a circle and is moving clockwise. Which way is its velocity tangent to the circle?

**Explanation**

At the left side, clockwise motion carries the particle upward. The velocity is tangent to the circle, not inward or outward, so the velocity points up.

The tangent direction depends on the position on the circle and the stated direction of travel. At this same left-side point, counterclockwise motion would point downward instead.

Check the tangent before deciding whether the force points with it or against it.

```quiz
type: radio
id: q-tangent-left-clockwise
content: |-
  A particle is at the right side of a circle and is moving clockwise. Which way does its velocity point?
options:
- id: a
  content: |-
    Up
- id: b
  content: |-
    Down
  correct: true
- id: c
  content: |-
    Toward the center
- id: d
  content: |-
    Away from the center
```

---

<a id="use-speeding-up-or-slowing-down"></a>
## Use Speeding Up or Slowing Down

**Example:** A particle is at the left side of a circle, moving clockwise, and slowing down. Which way is the tangential part of the net force?

**Explanation**

At the left side, clockwise velocity points up. Since the particle is slowing down, the tangential part of the net force must point opposite the velocity.

So the tangential part points down. The full net force still needs an inward part, so it should point down and right.

```quiz
type: radio
id: q-slowing-left-clockwise
content: |-
  A particle is at the left side of a circle, moving counterclockwise, and slowing down. Which way should the tangential part of the net force point?
options:
- id: a
  content: |-
    Up
  correct: true
- id: b
  content: |-
    Down
- id: c
  content: |-
    Right, toward the center
- id: d
  content: |-
    Left, away from the center
```

```quiz
type: radio
id: q-speeding-left-clockwise
content: |-
  A particle is at the left side of a circle, moving clockwise, and speeding up. Which way should the tangential part of the net force point?
options:
- id: a
  content: |-
    Up
  correct: true
- id: b
  content: |-
    Down
- id: c
  content: |-
    Right, toward the center
- id: d
  content: |-
    Left, away from the center
```

---

<a id="choose-the-matching-diagram"></a>
## Choose the Matching Diagram

**Example:** A particle is at the left side of a circle, moving clockwise, and slowing down. Which net-force arrow direction should the correct diagram show?

**Explanation**

Work in two parts:

1. The inward radial component points right, toward the center.
2. Clockwise velocity at the left side points up, so slowing down requires a tangential component down.

Combining those gives a net-force arrow that points down and right. In the assignment's diagram set, that is choice C.

Before choosing, reject arrows that miss either requirement. A purely tangential arrow does not bend the path, and a purely inward arrow does not match a changing speed. An arrow with an outward part cannot be the net force for circular motion at that instant.

```quiz
type: radio
id: q-original-diagram-choice
content: |-
  A particle is moving around a circle. Which diagram represents a particle moving clockwise and slowing down?

  ![](<../Source/Images/problem-2-net-force-diagrams.png>)
options:
- id: a
  content: |-
    A
  feedback: |-
    This arrow has an outward part instead of the required inward part.
- id: b
  content: |-
    B
  feedback: |-
    This does not include the needed downward tangential part for slowing down.
- id: c
  content: |-
    C
  correct: true
  feedback: |-
    This combines inward toward the center with a downward tangential part.
- id: d
  content: |-
    D
  feedback: |-
    This is tangent with the clockwise motion, so it would speed the particle up.
- id: e
  content: |-
    E
  feedback: |-
    This misses the clockwise-slowing combination shown by the required inward plus downward direction.
```

---

## Summary

For a net-force diagram in circular motion, first find the inward direction toward the center. Then find the tangent direction from the stated clockwise or counterclockwise motion. If the particle is speeding up, the tangential force component points with the velocity; if it is slowing down, the tangential component points opposite the velocity. The main trap is choosing an arrow that is only tangent or only inward instead of combining both required components.

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Finding the Net-Force Direction in Circular Motion](<../../2026-07-03-HW-2/Lessons/Problem-4.md>)

<!-- study-guide-nav:end -->

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]
