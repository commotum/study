# Free-Body Diagrams for Level Circular Motion

## Table of Contents

- [Introduction](#introduction)
- [Balance the Vertical Forces](#balance-the-vertical-forces)
- [Point the Sideways Force Toward the Center](#point-the-sideways-force-toward-the-center)
- [Use the View to Choose Left or Right](#use-the-view-to-choose-left-or-right)
- [Reject Extra or Outward Forces](#reject-extra-or-outward-forces)
- [Match the Original Diagram](#match-the-original-diagram)
- [Summary](#summary)

## Prerequisites

- Weight $mg$ points downward.
- The normal force $N$ from a level road points upward.
- A free-body diagram includes real forces acting on the object.
- For circular motion, the net force points toward the center of the circle.

---

<a id="introduction"></a>
## Introduction

When a car travels around a level circle at constant speed, its speed is constant but its direction is changing. That means the car has centripetal acceleration toward the center of the circle.

To choose the correct free-body diagram, first handle the vertical forces, then decide which real horizontal force points toward the center. On a level road, the horizontal inward force is static friction.

Use this three-check test:

1. Include the contact and gravity forces: $N$ up and $mg$ down.
2. Balance the vertical forces because the road is level and there is no vertical acceleration.
3. Add exactly one real horizontal force, static friction, pointing toward the center of the circle.

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

For circular motion, the net horizontal force must point toward the center of the circle. On a level road, the road can provide this sideways force through static friction.

The label "centripetal force" describes the net inward force requirement:

$$
\sum F_{\text{inward}} = \frac{mv^2}{r}
$$

It is not an additional force arrow. For a car on a level road, the real inward force is static friction $f_s$.

```quiz
type: radio
id: level-curve-fbd-q2
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

The car does not need an outward force to move in a circle. The inward net force is what changes the direction of the velocity.

An outward arrow is a common mistake because the rider may feel pushed outward. That feeling comes from inertia in the turning car's frame, not from a real outward force acting on the car in the road frame.

```quiz
type: radio
id: level-curve-fbd-q4
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

<a id="match-the-original-diagram"></a>
## Match the Original Diagram

**Example:** A car travels around a level circle at constant speed. The center of the circle is to the right of the car in the side view. Choose the correct free-body diagram from choices A-D.

![](<../Source/Images/level-curve-free-body-diagrams.png>)

**Explanation**

The car has no vertical acceleration, so $N$ and $mg$ should be equal and opposite. The center of the circle is to the right, so static friction points right.

Choice A shows those three forces: $N$ up, $mg$ down, and a single rightward horizontal force.

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

For a car moving at constant speed around a level circle, use this three-check test:

1. Put $mg$ downward.
2. Put $N$ upward.
3. Since there is no vertical acceleration, make $N$ and $mg$ balance.
4. Point static friction toward the center of the circle.
5. Do not add a separate centripetal-force arrow or an outward force arrow.

The main trap is thinking that constant speed means no acceleration. In circular motion, the speed can stay constant while the direction changes, so the net force points inward.
