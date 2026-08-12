# Choosing the Acceleration Direction When Circular Motion Speeds Up

<!--
lesson-id: 212-M1-008
topic-code: MTH212.M1.08
-->

## Table of Contents

- [Introduction](#introduction)
- [Separate the Two Direction Cues](#separate-the-two-direction-cues)
- [Use Speeding Up to Set the Tangential Direction](#use-speeding-up-to-set-the-tangential-direction)
- [Add the Inward and Tangential Directions](#add-the-inward-and-tangential-directions)
- [Resolve the Arrow Choice](#resolve-the-arrow-choice)
- [Summary](#summary)

## Prerequisites

- Velocity in circular motion is tangent to the circle.
- Centripetal acceleration points toward the center of the circle.
- If an object is speeding up, its tangential acceleration points in the same direction as its velocity.
- The sum of two direction vectors points between the two directions being added.

---

<a id="introduction"></a>
## Introduction

The diagram below shows an object at the upper-left part of a circular path, moving counterclockwise and speeding up. Which arrow shows its acceleration?

![](<../Source/Images/problem-13-acceleration-arrows.png>)

The object's velocity is changing in two ways at once: its direction is turning around the circle, and its magnitude is increasing. Its acceleration therefore has two parts:

$$
\vec{a}=\vec{a}_r+\vec{a}_t.
$$

For an object that is speeding up:

- the centripetal part points toward the center of the circle;
- the tangential part points along the direction of motion;
- the total acceleration points between those two directions.

If the speed were constant, there would be no tangential part. If the object were slowing down, the tangential part would point opposite the motion. Here the correct arrow must include both the inward turn and the forward change in speed.

A useful functional test is that $a_r$ changes the direction of $\vec v$, while

$$
a_t=\frac{dv}{dt}
$$

changes its magnitude. Because the radial-tangential axes rotate with the particle, redraw “inward” and “forward tangent” at the particle's current location before adding the two components.

---

<a id="separate-the-two-direction-cues"></a>
## Separate the Two Direction Cues

**Example:** An object moves around a circle and is speeding up. What two direction cues must be combined to find the direction of its acceleration?

**Explanation**

First, circular motion always gives an inward acceleration component because the velocity direction is turning.

Second, the speed is increasing, so there is also a tangential acceleration component in the direction of motion.

So the full acceleration is not just inward and not just tangent. It is the vector sum:

$$
\vec{a}=\vec{a}_r+\vec{a}_t.
$$

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  An object moves around a circle and is speeding up. Which description gives the two direction parts of its acceleration?
options:
- id: q1-a
  content: |-
    Inward only
- id: q1-b
  content: |-
    Tangent in the direction of motion only
- id: q1-c
  content: |-
    Inward, plus tangent in the direction of motion
  correct: true
- id: q1-d
  content: |-
    Outward, plus tangent opposite the direction of motion
```

---

<a id="use-speeding-up-to-set-the-tangential-direction"></a>
## Use Speeding Up to Set the Tangential Direction

**Example:** At the top of a circular path, an object is moving counterclockwise and speeding up. Which way does the tangential part of the acceleration point?

**Explanation**

At the top of the circle, counterclockwise motion is toward the left. The velocity is tangent to the circle, so the tangent direction is left.

Because the object is speeding up, the tangential acceleration points with the velocity. So the tangential part points left.

If the object were slowing down, the tangential part would point opposite the velocity instead.

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  At the left side of a circular path, an object is moving clockwise and speeding up. Which way does the tangential part of its acceleration point?
options:
- id: q2-a
  content: |-
    Up
  correct: true
- id: q2-b
  content: |-
    Down
- id: q2-c
  content: |-
    Right, toward the center
- id: q2-d
  content: |-
    Left, away from the center
```

---

<a id="add-the-inward-and-tangential-directions"></a>
## Add the Inward and Tangential Directions

**Example:** At the top of a circular path, an object is moving counterclockwise and speeding up. Which general direction should its total acceleration point?

**Explanation**

At the top of the circle:

- the inward direction points down, toward the center;
- the counterclockwise tangent direction points left;
- because the object is speeding up, the tangential part points left.

The total acceleration is the resultant of the down component and the left component. Therefore, the total acceleration points down-left.

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  At the right side of a circular path, an object is moving counterclockwise and speeding up. Which general direction should its total acceleration point?
options:
- id: q3-a
  content: |-
    Left
- id: q3-b
  content: |-
    Up
- id: q3-c
  content: |-
    Up-left
  correct: true
- id: q3-d
  content: |-
    Down-right
```

---

<a id="resolve-the-arrow-choice"></a>
## Resolve the Arrow Choice

**Example:** In the diagram above, the object is at the upper-left part of the circle, moving counterclockwise and speeding up. Which arrow represents its acceleration?

**Explanation**

At the upper-left part of the circle, counterclockwise motion is tangent roughly down-left.

The inward direction points from the object toward the center of the circle, roughly down-right.

Since the object is speeding up, the tangential part points with the motion, down-left. The total acceleration must combine down-left with down-right, so it should point generally downward and inward, between those two component directions.

Among the choices, arrow C is the arrow that has both the inward component and the forward tangential component.

The other common-looking choices each omit one component:

- A is tangent-only.
- E is too close to inward-only.
- B and D do not combine a downward tangent with an inward component.

```quiz
type: radio
id: q-4
content: |-
  ![](<../Source/Images/problem-13-acceleration-arrows.png>)

  An object is moving counterclockwise along the circular trajectory shown. If the object is speeding up, which arrow represents its acceleration?
options:
- id: q4-a
  content: |-
    A
- id: q4-b
  content: |-
    B
- id: q4-c
  content: |-
    C
  correct: true
- id: q4-d
  content: |-
    D
- id: q4-e
  content: |-
    E
```

---

## Summary

For circular motion with changing speed, do not choose the acceleration direction from the tangent alone.

Build the total acceleration from its components:

1. Draw the inward component toward the center.
2. Find the tangent direction from the direction of motion.
3. If the speed is constant, stop there: the acceleration is inward only.
4. If the object is speeding up, point the tangential component with the motion.
5. If the object is slowing down, point the tangential component opposite the motion.
6. Choose the resultant arrow between the inward component and the tangential component.

In the diagram above, counterclockwise motion at the upper-left point gives a down-left tangential component, while the center is down-right. Speeding up means the acceleration is the sum of those two directions, so the correct arrow is C.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Choosing the Net Force Direction for Speeding-Up Circular Motion](../../2026-07-02-M1-5/Lessons/Problem-1.md)

Study guide index: 09/35

---
<!-- lesson-nav:end -->
