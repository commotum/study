# Choosing a Free-Body Diagram for a Conical Pendulum

## Table of Contents

- [Introduction](#introduction)
- [List Only Real Forces](#list-only-real-forces)
- [Point Each Force in Its Physical Direction](#point-each-force-in-its-physical-direction)
- [Use Centripetal Acceleration as a Net-Force Check](#use-centripetal-acceleration-as-a-net-force-check)
- [Apply the Answer Choices](#apply-the-answer-choices)
- [Summary](#summary)

## Prerequisites

- A free-body diagram shows forces acting on one object.
- Weight points straight down with magnitude $mg$.
- Tension from a string points along the string, away from the object.
- For uniform circular motion, the acceleration points toward the center of the circle.

---

<a id="introduction"></a>
## Introduction

When an object moves in a horizontal circle while hanging from a string, the cue is that the free-body diagram must show the real forces on the object, not the acceleration or the path.

For a key on a string with no air resistance, the task is to choose the diagram that has exactly these two forces:

- weight straight down
- tension along the string toward the hand

The inward acceleration is real, but it comes from the horizontal component of tension. It is not a separate force arrow.

Use this checklist:

1. Name the real interactions with the key.
2. Draw each force from the key in the direction that interaction pulls.
3. Use the inward acceleration only to check the net force direction.

---

<a id="list-only-real-forces"></a>
## List Only Real Forces

**Example:** A key swings in a horizontal circle while attached to a string. There is no air resistance. What forces act on the key?

**Explanation**

Start by naming interactions with the key:

| Interaction | Force on the key? | Direction |
| --- | --- | --- |
| Earth pulls on the key | yes | straight down |
| String pulls on the key | yes | along the string toward the hand |
| Air pushes on the key | no | none, because air resistance is ignored |
| Circular motion itself | no | acceleration is not a force |

So the free-body diagram should contain exactly two arrows. Adding a separate "centripetal force" arrow double-counts the inward effect of tension.

```quiz
type: radio
id: p7-real-forces
content: |-
  A small ball moves in a horizontal circle at the end of a string. Ignore air resistance. Which list gives the real forces acting on the ball?
options:
- id: a
  content: |-
    weight, tension, and a separate centripetal force
- id: b
  content: |-
    weight and tension
  correct: true
  feedback: |-
    The inward acceleration is caused by the net force; it is not an extra force.
- id: c
  content: |-
    tension and a separate force in the direction of motion
- id: d
  content: |-
    weight and a separate horizontal force, but no tension
```

---

<a id="point-each-force-in-its-physical-direction"></a>
## Point Each Force in Its Physical Direction

**Example:** A key is attached to a string that slants upward and inward toward the hand. How should the tension and weight arrows be drawn?

**Explanation**

Weight always points vertically downward. It does not tilt just because the key is moving in a circle.

Tension always points along the string, away from the object. If the string slants upward and inward from the key to the hand, then the tension arrow should also slant upward and inward.

The tension arrow should not point horizontally unless the string itself is horizontal. It is not enough for the arrow to point partly inward; the tension arrow must be parallel to the string and point toward the support.

```quiz
type: radio
id: p7-force-directions
content: |-
  A mass hangs from a string that slants upward to the left toward the support while the mass moves in a horizontal circle. Which statement gives the correct force directions on the mass?
options:
- id: a
  content: |-
    Weight points downward, and tension points upward-left along the string.
  correct: true
  feedback: |-
    Tension follows the string toward the support; weight points straight down.
- id: b
  content: |-
    Weight points along the string, and tension points straight down.
- id: c
  content: |-
    Weight points downward, and tension points horizontally toward the circle's center.
- id: d
  content: |-
    Tension points in the direction the mass is moving around the circle.
```

---

<a id="use-centripetal-acceleration-as-a-net-force-check"></a>
## Use Centripetal Acceleration as a Net-Force Check

**Example:** If the only forces are weight downward and tension along a slanted string, how can the key have inward acceleration?

**Explanation**

Break the tension into components. Its vertical component balances the weight when the key stays at a constant height:

$$
T_y=mg.
$$

Its horizontal component points toward the center of the circle. That horizontal component supplies the net inward force:

$$
T_x=\frac{mv^2}{r}.
$$

This check explains why the diagram can have only two force arrows while the motion is still circular. The phrase "centripetal force" means the net inward force, not a new interaction. A separate net-force arrow can be useful in a force-sum sketch, but it does not belong as an extra force in the free-body diagram.

```quiz
type: radio
id: p7-centripetal-check
content: |-
  In a conical pendulum, what supplies the inward net force needed for circular motion?
options:
- id: a
  content: |-
    A separate centripetal-force arrow in addition to tension
- id: b
  content: |-
    The horizontal component of the string tension
  correct: true
  feedback: |-
    Tension is the real force; its horizontal component is the net inward force.
- id: c
  content: |-
    The weight of the object
- id: d
  content: |-
    A forward force in the direction of motion
```

---

<a id="apply-the-answer-choices"></a>
## Apply the Answer Choices

**Example:** A key on a string traces out a horizontal circle as shown. Assume there is no air resistance. Which free-body diagram could accurately depict the key?

![](<../Source/Images/conical-pendulum-key-free-body-diagrams.png>)

**Explanation**

Use the force list before looking at the labels:

- The diagram must include weight straight down.
- The diagram must include tension along the slanted string toward the hand.
- The diagram must not include a separate inward or horizontal "centripetal force" arrow.

Then eliminate each diagram by that checklist:

| Choice | Keep or reject? | Reason |
| --- | --- | --- |
| A | reject | It adds an extra inward arrow. |
| B | reject | It adds a horizontal force arrow that is not a real interaction. |
| C | keep | It shows weight downward and tension along the string. |
| D | reject | It omits the tension force. |

So choice C is the accurate free-body diagram.

```quiz
type: radio
id: p7-original-check
content: |-
  A key on a string traces out a horizontal circle. Assume there is no air resistance. Which free-body diagram could accurately depict the key?
  
  ![](<../Source/Images/conical-pendulum-key-free-body-diagrams.png>)
options:
- id: a
  content: |-
    A
- id: b
  content: |-
    B
- id: c
  content: |-
    C
  correct: true
  feedback: |-
    The real forces are weight downward and tension along the string toward the hand. There is no separate centripetal-force arrow.
- id: d
  content: |-
    D
```

---

## Summary

For a conical-pendulum free-body diagram, first list the real interactions with the object. With no air resistance, the object has weight downward and tension along the string toward the support.

Then use circular motion as a check: the horizontal component of tension supplies the inward net force. Do not add a separate centripetal-force arrow.
