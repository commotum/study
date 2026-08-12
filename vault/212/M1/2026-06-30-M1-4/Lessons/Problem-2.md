# Free-Body Diagrams for Level Circular Motion

<!--
lesson-id: 212-M1-012
topic-code: MTH212.M1.12
-->

## Table of Contents

- [Introduction](#introduction)
- [Balance the Vertical Forces](#balance-the-vertical-forces)
- [Point the Sideways Force Toward the Center](#point-the-sideways-force-toward-the-center)
- [Use the View to Choose Left or Right](#use-the-view-to-choose-left-or-right)
- [Reject Extra or Outward Forces](#reject-extra-or-outward-forces)
- [Choose Among the Diagrams](#choose-among-the-diagrams)
- [Summary](#summary)

## Prerequisites

- Weight $mg$ points downward.
- The normal force $N$ from a level road points upward.
- A free-body diagram includes real forces acting on the object.
- For circular motion, the net force points toward the center of the circle.

---

<a id="introduction"></a>
## Introduction

A car travels at constant speed around a level circular track. The drawing shows the track from above and the car from the side; the question is which side-view free-body diagram correctly represents the forces on the car.

![](<../Source/Images/level-curve-free-body-diagrams.png>)

The word *constant* describes the car's speed, not its velocity. As the car turns, the velocity changes direction, so the car accelerates toward the center of the circle. In the side view, that center is to the right of the car.

The road pushes upward on the car while gravity pulls downward. Those two forces balance because the car has no vertical acceleration. Static friction from the road points horizontally toward the center and turns the car. A correct diagram therefore has $N$ upward, $mg$ downward, and $f_s$ to the right—without a separate centripetal-force arrow.

---

<a id="balance-the-vertical-forces"></a>
## Balance the Vertical Forces

**Example:** A car moves around a flat circular track. Which vertical forces should appear in its free-body diagram?

**Explanation**

The road pushes up on the car with the normal force $N$. Gravity pulls down with weight $mg$.

Because the road is level and the car is not accelerating vertically, the vertical forces balance:

$$
N = mg
$$

So the diagram should show an upward normal force and a downward weight force with equal lengths.

```quiz
type: radio
id: level-curve-fbd-q1
shuffle: true
content: |-
  A car moves at constant speed on a level circular track. Which vertical-force pair belongs in the free-body diagram?
options:
- id: q1-a
  content: |-
    Upward $N$ and downward $mg$ with equal lengths
  correct: true
  feedback: |-
    Correct. There is no vertical acceleration, so the vertical forces balance.
- id: q1-b
  content: |-
    Upward $N$ longer than downward $mg$
  feedback: |-
    That would mean an upward vertical net force.
- id: q1-c
  content: |-
    Downward $mg$ only
  feedback: |-
    The road is in contact with the car, so a normal force is present.
- id: q1-d
  content: |-
    Upward $N$ and downward $mg$ with a sideways velocity arrow
  feedback: |-
    A velocity arrow is not a force arrow in a free-body diagram.
```

---

<a id="point-the-sideways-force-toward-the-center"></a>
## Point the Sideways Force Toward the Center

**Example:** A car turns left while moving around a level circular path. What horizontal force should appear in the car's free-body diagram?

**Explanation**

For circular motion, the net horizontal force must point toward the center of the circle. On a level road, the road can provide this sideways force through static friction. A useful counterfactual fixes the direction: without tire-road friction, the car would continue approximately along the instantaneous tangent rather than follow the curve. Friction must therefore point inward to bend the path.

The label "centripetal force" describes the net inward force requirement:

$$
\sum F_r=m a_r=m\frac{v^2}{r}
$$

It is not an additional force arrow. For a car on a level road, the real inward force is static friction $f_s$.

```quiz
type: radio
id: level-curve-fbd-q2
shuffle: true
content: |-
  A car on a level road turns around a circular path whose center is to the left of the car. Which horizontal force belongs in the free-body diagram?
options:
- id: q2-a
  content: |-
    Static friction to the left
  correct: true
  feedback: |-
    Correct. The inward direction is toward the center, so friction points left.
- id: q2-b
  content: |-
    Static friction to the right
  feedback: |-
    That points away from the center in this situation.
- id: q2-c
  content: |-
    A separate "centripetal force" arrow to the left
  feedback: |-
    Centripetal force is the net inward result, not an extra force.
- id: q2-d
  content: |-
    No horizontal force because the speed is constant
  feedback: |-
    Constant speed around a circle still requires inward acceleration.
```

---

<a id="use-the-view-to-choose-left-or-right"></a>
## Use the View to Choose Left or Right

**Example:** In a side-view drawing, the radius line from the car to the center of the circle points to the right. Which way should the friction arrow point?

**Explanation**

The radius line points from the car toward the center of the circle. Since the inward force must point toward the center, the friction arrow points in the same direction as that radius line.

If the radius line points right, static friction points right. If the radius line points left, static friction points left. The velocity direction does not choose the force direction here; velocity is tangent to the circle, while the net force points inward along the radius.

```quiz
type: radio
id: level-curve-fbd-q3
shuffle: true
content: |-
  In a side-view diagram, the center of the car's circular path is to the right of the car. Which free-body diagram description matches the situation?
options:
- id: q3-a
  content: |-
    $N$ up, $mg$ down, and $f_s$ right
  correct: true
  feedback: |-
    Correct. The vertical forces balance, and friction points toward the center.
- id: q3-b
  content: |-
    $N$ up, $mg$ down, and $f_s$ left
  feedback: |-
    That friction arrow points away from the center.
- id: q3-c
  content: |-
    $N$ up, $mg$ down, and both leftward and rightward horizontal forces
  feedback: |-
    The diagram should show the real horizontal contact force, not a balanced pair.
- id: q3-d
  content: |-
    $mg$ down and $f_s$ right, with no normal force
  feedback: |-
    A level road in contact with the car exerts a normal force.
```

---

<a id="reject-extra-or-outward-forces"></a>
## Reject Extra or Outward Forces

**Example:** A student chooses a diagram with $N$ up, $mg$ down, friction inward, and another horizontal arrow outward. What is wrong with that diagram?

**Explanation**

The car does not need an outward force to move in a circle. The inward net force is what changes the direction of the velocity. Audit a proposed free-body diagram in this order: list the real interactions, check that $N=mg$ vertically, and then require the remaining horizontal force to point toward the marked center.

An outward arrow is a common mistake because the rider may feel pushed outward. That feeling comes from inertia in the turning car's frame, not from a real outward force acting on the car in the road frame.

```quiz
type: radio
id: level-curve-fbd-q4
shuffle: true
content: |-
  A diagram for a car turning on a level road already has $N$ up, $mg$ down, and $f_s$ right toward the center. Which added feature would make the diagram wrong?
options:
- id: q4-a
  content: |-
    An extra leftward horizontal force arrow
  correct: true
  feedback: |-
    Correct. That extra outward force is not a real force on the car.
- id: q4-b
  content: |-
    The label $f_s$ on the rightward horizontal arrow
  feedback: |-
    Static friction is the real inward horizontal force on a level curve.
- id: q4-c
  content: |-
    Equal lengths for the $N$ and $mg$ arrows
  feedback: |-
    Equal vertical arrows are correct because there is no vertical acceleration.
- id: q4-d
  content: |-
    The label $mg$ on the downward arrow
  feedback: |-
    The downward force is the car's weight.
```

---

<a id="choose-among-the-diagrams"></a>
## Choose Among the Diagrams

**Example:** Compare choices A–D for the car shown in the introduction.

**Explanation**

Reject any choice that omits a contact force, points friction away from the center, or adds a second horizontal force. Choice A shows the three real forces with the required directions: $N$ up, $mg$ down, and $f_s$ to the right.

```quiz
type: radio
id: level-curve-fbd-q5
content: |-
  A car travels around a level circle at constant speed. The center of the circle is to the right in the side view.

  ![](<../Source/Images/level-curve-free-body-diagrams.png>)

  Which choice from A-D is the correct free-body diagram?
options:
- id: q5-a
  content: |-
    A
  correct: true
  feedback: |-
    Correct. It shows balanced vertical forces and one rightward inward force.
- id: q5-b
  content: |-
    B
  feedback: |-
    This is missing the horizontal inward force needed for circular motion.
- id: q5-c
  content: |-
    C
  feedback: |-
    The horizontal force points away from the center.
- id: q5-d
  content: |-
    D
  feedback: |-
    This adds an extra outward horizontal force that should not be in the diagram.
```

---

<a id="summary"></a>
## Summary

For a car on a level circular track, $N$ and $mg$ balance vertically. Static friction is the real horizontal force that points toward the center and changes the direction of the car's velocity. “Centripetal” describes this inward net force; it is not another arrow to add to the free-body diagram.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Finding Static Friction on a Flat Curve](Problem-3.md)

Study guide index: 12/35

---
<!-- lesson-nav:end -->
