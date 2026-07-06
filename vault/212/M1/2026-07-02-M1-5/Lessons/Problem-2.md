# Choosing the Net Force Direction for Clockwise Speeding Up

## Table of Contents

- [Introduction](#introduction)
- [Convert Net Force to Acceleration Direction](#convert-net-force-to-acceleration-direction)
- [Mark the Inward Radial Component](#mark-the-inward-radial-component)
- [Mark the Forward Tangential Component](#mark-the-forward-tangential-component)
- [Combine the Components and Match the Arrow](#combine-the-components-and-match-the-arrow)
- [Summary](#summary)

## Prerequisites

- Net force and acceleration point in the same direction because $\sum \vec{F}=m\vec{a}$.
- Motion around a circle has an inward radial acceleration component.
- The tangential direction is perpendicular to the radius at the particle's position.
- If an object is speeding up, its tangential acceleration points in the direction of motion.

---

<a id="introduction"></a>
## Introduction

When a circular-motion problem asks for the direction of net force, first switch to the direction of total acceleration. The net force points the same way as acceleration, so the job is to combine the radial and tangential acceleration components.

For this problem, the cue is "clockwise direction and speeding up." That means the net force must point inward toward the center and forward along the clockwise tangent.

Read the cue in this order:

1. Moving in a circle gives an inward radial component.
2. Clockwise tells you which tangent direction is forward.
3. Speeding up makes the tangential component point forward, not backward.

---

<a id="convert-net-force-to-acceleration-direction"></a>
## Convert Net Force to Acceleration Direction

**Example:** A particle's total acceleration points down-left. What direction does the net force point?

**Explanation**

Newton's second law is

$$
\sum \vec{F}=m\vec{a}.
$$

The mass $m$ changes the size of the vector, not its direction. So the net force points down-left too.

```quiz
type: radio
id: p2-q1-force-acceleration
content: |-
  A particle's total acceleration points up-left. What direction does the net force point?
options:
- id: q1-a
  content: |-
    Up-left
  correct: true
  feedback: |-
    Net force and acceleration have the same direction.
- id: q1-b
  content: |-
    Down-right
  feedback: |-
    That would reverse the acceleration direction.
- id: q1-c
  content: |-
    Straight down
  feedback: |-
    The net force must match the acceleration direction, not just point somewhere on the page.
- id: q1-d
  content: |-
    The direction cannot be determined from acceleration
  feedback: |-
    It can be determined because $\sum \vec{F}=m\vec{a}$ and $m$ is positive.
```

---

<a id="mark-the-inward-radial-component"></a>
## Mark the Inward Radial Component

**Example:** A particle is on the lower-right side of a circle. If it is moving in a circle, which way does the radial acceleration point?

**Explanation**

Radial acceleration always points toward the center of the circle. From the lower-right side of the circle, the center is up-left from the particle.

So the radial component points up-left.

```quiz
type: radio
id: p2-q2-radial
content: |-
  A particle is on the lower-right side of a circle. Which direction is the inward radial component?
options:
- id: q2-a
  content: |-
    Up-left, toward the center
  correct: true
  feedback: |-
    The inward radial component points from the particle toward the circle's center.
- id: q2-b
  content: |-
    Down-right, away from the center
  feedback: |-
    That is outward, not inward.
- id: q2-c
  content: |-
    Down-left, tangent to the circle
  feedback: |-
    That is a tangential direction, not the inward radial direction.
- id: q2-d
  content: |-
    Straight down
  feedback: |-
    Straight down is neither toward the center nor tangent at this point.
```

---

<a id="mark-the-forward-tangential-component"></a>
## Mark the Forward Tangential Component

**Example:** A particle is on the lower-right side of a circle and moving clockwise. If it is speeding up, which way does the tangential acceleration point?

**Explanation**

The tangential direction follows the path of motion. At the lower-right side of the circle, clockwise motion points along the tangent down-left.

Because the particle is speeding up, tangential acceleration points with the motion. So the tangential component points down-left.

```quiz
type: radio
id: p2-q3-tangential
content: |-
  A particle is on the lower-right side of a circle, moving clockwise, and speeding up. Which direction is the tangential acceleration?
options:
- id: q3-a
  content: |-
    Down-left, along the clockwise tangent
  correct: true
  feedback: |-
    Speeding up means the tangential acceleration points in the direction of motion.
- id: q3-b
  content: |-
    Up-right, opposite the clockwise tangent
  feedback: |-
    That would fit counterclockwise speeding up or clockwise slowing down.
- id: q3-c
  content: |-
    Up-left, toward the center
  feedback: |-
    That is the radial component, not the tangential component.
- id: q3-d
  content: |-
    Down-right, away from the center
  feedback: |-
    That is outward, not the forward tangent.
```

---

<a id="combine-the-components-and-match-the-arrow"></a>
## Combine the Components and Match the Arrow

**Example:** A particle is on the lower-right side of a circle, moving clockwise, and speeding up. What general direction should the net force point?

**Explanation**

Use the same three-step diagram routine every time:

1. Draw the radial component toward the center. Here, that is up-left.
2. Draw the forward tangent for clockwise motion. Here, that is down-left.
3. Add the two components and choose the arrow between them.

The total acceleration is their vector sum:

$$
\vec{a}=\vec{a}_r+\vec{a}_t.
$$

That sum points between the inward direction and the forward tangent. Since both components point leftward, the net force should point leftward, tilted toward the center. In the original diagram, that is choice D.

```quiz
type: radio
id: p2-q4-original
content: |-
  A particle is moving around a circle, with an arrow depicting the magnitude and direction of the net force acting on the particle. Which diagram represents a particle moving in the clockwise direction and speeding up?

  ![](<../Source/Images/clockwise-speeding-up-net-force.png>)
options:
- id: q4-a
  content: |-
    A
  feedback: |-
    This points too much like the inward-only component and misses the forward clockwise tangent.
- id: q4-b
  content: |-
    B
  feedback: |-
    This points outward and forward, but circular motion requires an inward component.
- id: q4-c
  content: |-
    C
  feedback: |-
    This has the opposite tangential lean for clockwise speeding up.
- id: q4-d
  content: |-
    D
  correct: true
  feedback: |-
    D points inward plus forward along the clockwise tangent.
- id: q4-e
  content: |-
    E
  feedback: |-
    This points away from the center.
- id: q4-f
  content: |-
    F
  feedback: |-
    This is mainly the tangent direction and misses the inward component.
- id: q4-g
  content: |-
    G
  feedback: |-
    This points outward instead of inward.
- id: q4-h
  content: |-
    H
  feedback: |-
    This points downward, not inward plus forward.
```

---

## Summary

For a net-force diagram in circular motion, use this checklist:

1. Net force points in the same direction as total acceleration.
2. Circular motion always contributes an inward radial component.
3. Speeding up contributes a tangential component in the direction of motion.
4. Add the inward and tangential components, then choose the arrow between them.

For a particle on the lower-right side moving clockwise and speeding up, inward is up-left and the forward tangent is down-left. The sum points leftward with an inward lean, so the matching choice is D.

Do not choose the inward-only arrow unless the speed is constant. Do not choose the opposite tangential lean unless the particle is slowing down or moving the other way.
