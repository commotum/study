# Finding the Net-Force Direction in Circular Motion

<!--
lesson-id: 212-M1-011
topic-code: MTH212.M1.11
-->

## Table of Contents

- [Introduction](#introduction)
- [Point Net Force Toward the Circle Center](#point-net-force-toward-the-circle-center)
- [Use the Side View to Name the Direction](#use-the-side-view-to-name-the-direction)
- [Separate Net Force From Individual Forces](#separate-net-force-from-individual-forces)
- [Check the Opposite Side](#check-the-opposite-side)
- [Summary](#summary)

## Prerequisites

- Know that uniform circular motion has centripetal acceleration directed toward the center of the circle.
- Know that net force points in the same direction as acceleration because $\sum \vec F=m\vec a$.
- Be able to read left, right, up, and down directions from a side-view diagram.

---

<a id="introduction"></a>
## Introduction

A bob suspended from a string moves at constant speed around a horizontal circle. The diagram shows that circle from above and shows the filled bob on the right in the side view.

![](<../Source/Images/conical-pendulum-diagram.png>)

Although the bob's speed is constant, its velocity keeps turning, so its acceleration and net force point toward the center of the circular path. In the side view, the center is horizontally to the left of the filled bob. The net force therefore points directly left.

This is the direction of the combined force on the bob, not the direction of the string tension by itself. The upward part of the tension balances the bob's weight, leaving a horizontal inward net force.

---

<a id="point-net-force-toward-the-circle-center"></a>
## Point Net Force Toward the Circle Center

**Example:** A ball moves at constant speed around a horizontal circle. At one instant, the ball is at the rightmost point of the circle. Where does the net force point?

**Explanation**

The net force must point in the same direction as the centripetal acceleration:

$$
\sum \vec F = m\vec a_r
$$

The centripetal direction is always from the object toward the center of the circle. The object is the tail of the direction arrow, and the center is the head of the direction arrow. From the rightmost point, the center is to the left, so the net force points left.

```quiz
type: radio
id: p4-net-force-rightmost
shuffle: true
content: |-
  A puck moves at constant speed in a horizontal circle. At the instant shown, the puck is at the rightmost point of the circle. Where does the net force point?
options:
- id: a
  content: |-
    Directly left
  correct: true
- id: b
  content: |-
    Directly right
- id: c
  content: |-
    Straight upward
- id: d
  content: |-
    Tangent to the path
```

---

<a id="use-the-side-view-to-name-the-direction"></a>
## Use the Side View to Name the Direction

**Example:** In the side view of the conical pendulum shown above, the filled bob is on the right side of its circular path. The circle's center is horizontally inward from the bob. Which direction is inward?

**Explanation**

The side view flattens the circular path into a left-right line through the center. If the bob is on the right side, inward means toward the center, which is left. The vertical forces still matter for a force diagram, but the net force has no vertical component when the bob stays at the same height.

```quiz
type: radio
id: p4-side-view-right
shuffle: true
content: |-
  The figures below show a bob of mass $m$ attached to a light string of length $L$ which traverses a circular trajectory when viewed from above/below.

  The string makes an angle $\theta$ with the horizontal and the period of the circular motion is $T$ (constant).

  Given the side-view of the filled (not dashed) bob below in Figure 2, where does the net force on the bob point?

  ![](<../Source/Images/conical-pendulum-diagram.png>)
options:
- id: a
  content: |-
    Directly to the left
  correct: true
- id: b
  content: |-
    Directly to the right
- id: c
  content: |-
    Along the string, toward the ceiling
- id: d
  content: |-
    Not listed
```

---

<a id="separate-net-force-from-individual-forces"></a>
## Separate Net Force From Individual Forces

**Example:** A conical pendulum bob has tension along the string and weight straight downward. The bob moves in a horizontal circle at constant height. Does the net force point along the string?

**Explanation**

No. The net force is the vector sum of all forces, not one individual force. For this conical pendulum, the string tension points up and inward, and weight points down. The upward part of tension balances weight, leaving only a horizontal inward net force:

$$
\sum F_y=0
$$

$$
\sum F_r=ma_r
$$

So the net force points inward toward the center, not along the string.

The free-body diagram should therefore contain only tension and weight. Do not add a third force labeled “centripetal force”: $mv^2/r$ is the required inward net result of the actual forces. This is the same reusable component pattern as a frictionless banked curve—one component of an angled physical force balances weight, while another supplies $\sum F_r$.

```quiz
type: radio
id: p4-net-force-not-string
shuffle: true
content: |-
  A conical pendulum bob is moving at constant height. The string slants upward and inward toward the pivot. Which statement best describes the net force?
options:
- id: a
  content: |-
    It points along the string because tension is the only force.
- id: b
  content: |-
    It points downward because gravity is always present.
- id: c
  content: |-
    It points horizontally inward because the vertical forces balance.
  correct: true
- id: d
  content: |-
    It points tangent to the path because the bob is moving.
```

---

<a id="check-the-opposite-side"></a>
## Check the Opposite Side

**Example:** A bob moves in the same circular path, but now the side view shows the bob on the left side of the circle. Where does the net force point?

**Explanation**

The rule does not change: point from the bob toward the center. If the bob is on the left side, the center is to its right, so the net force points right. The direction flips because the bob's position around the circle changed, not because the circular-motion rule changed.

```quiz
type: radio
id: p4-side-view-left
shuffle: true
content: |-
  A conical pendulum bob is shown on the left side of its circular path in a side view. Where does the net force point?
options:
- id: a
  content: |-
    Directly to the left
- id: b
  content: |-
    Directly to the right
  correct: true
- id: c
  content: |-
    Along the string, toward the ceiling
- id: d
  content: |-
    Tangent to the circular path
```

---

## Summary

In uniform circular motion, the net force points toward the center of the circle. In a conical pendulum, the bob stays at one height, so the vertical forces balance and the remaining net force is horizontal and inward. If the bob is on the right side of the side view, inward is left; if the bob is on the left side, inward is right. The tension points along the string, but the net force is the sum of tension and weight.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Choosing the Acceleration Direction When Circular Motion Speeds Up](../../2026-06-28-HW-1/Lessons/Problem-13.md)

Study guide index: 08/35

---
<!-- lesson-nav:end -->
