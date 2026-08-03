# Choosing the Net Force Direction for Speeding-Up Circular Motion

<!--
lesson-id: 212-M1-009
topic-code: MTH212.M1.09
-->

## Table of Contents

- [Introduction](#introduction)
- [Split the Net Force Into Two Components](#split-the-net-force-into-two-components)
- [Find the Forward Tangent](#find-the-forward-tangent)
- [Combine Inward and Forward](#combine-inward-and-forward)
- [Avoid the Tangent-Only Trap](#avoid-the-tangent-only-trap)
- [Original-Style Check](#original-style-check)
- [Summary](#summary)

## Prerequisites

- Know that net force points in the same direction as acceleration.
- Know that circular motion has an inward radial component toward the center.
- Know that speeding up means the tangential component points in the direction of motion.

---

<a id="introduction"></a>
## Introduction

When a particle moves around a circle and changes speed, the net force is not just tangent to the circle and not just toward the center. The cue is the phrase **speeding up in the counterclockwise direction**. Use it to combine two directions:

- an inward component toward the center of the circle
- a tangential component forward along the counterclockwise motion

For each diagram choice, ask three questions:

1. Does the arrow include an inward part?
2. Does the tangential part point forward for speeding up?
3. Does the final arrow point between those two directions?

---

<a id="split-the-net-force-into-two-components"></a>
## Split the Net Force Into Two Components

**Example:** A particle is at the lower-right side of a circle and is moving counterclockwise while speeding up. Which two force-component directions must the net force combine?

**Explanation**

The inward component points from the particle toward the center. From the lower-right side of the circle, that direction is up-left.

Because the particle is speeding up, the tangential component points along the motion. Counterclockwise motion at the lower-right side has a tangent pointing up-right.

So the net force must combine:

$$
\text{inward up-left}+\text{tangential up-right}.
$$

```quiz
type: radio
id: p1-q1
shuffle: true
content: |-
  A particle is at the lower-right side of a circle and is moving counterclockwise while speeding up. Which pair of directions should you combine for the net force?
options:
- id: a
  content: |-
    Inward up-left and tangent up-right
  correct: true
  feedback: |-
    The inward component points toward the center, and speeding up makes the tangent point forward.
- id: b
  content: |-
    Inward up-left and tangent down-left
  feedback: |-
    Down-left would be opposite the counterclockwise tangent at this position.
- id: c
  content: |-
    Outward down-right and tangent up-right
  feedback: |-
    The radial component for circular motion points inward, not outward.
- id: d
  content: |-
    Tangent up-right only
  feedback: |-
    Speeding up gives a tangential component, but circular motion also needs an inward component.
```

---

<a id="find-the-forward-tangent"></a>
## Find the Forward Tangent

**Example:** A particle is at the lower-left side of a circle and is moving counterclockwise while speeding up. Which way does the tangential component point?

**Explanation**

The tangent is perpendicular to the radius. For counterclockwise motion, the forward tangent follows the direction the particle would move next around the circle.

At the lower-left side, counterclockwise motion carries the particle toward the bottom of the circle, so the tangent points down-right. Because the particle is speeding up, the tangential force component also points down-right.

```quiz
type: radio
id: p1-q2
shuffle: true
content: |-
  A particle is at the lower-left side of a circle and is moving counterclockwise while speeding up. Which way does the tangential component of the net force point?
options:
- id: a
  content: |-
    Down-right
  correct: true
  feedback: |-
    At the lower-left side, counterclockwise motion is forward along the down-right tangent.
- id: b
  content: |-
    Up-right
  feedback: |-
    Up-right is inward from that position, not the tangent.
- id: c
  content: |-
    Up-left
  feedback: |-
    That points away from the center and is not the forward tangent.
- id: d
  content: |-
    Down-left
  feedback: |-
    That points more outward, not along the counterclockwise tangent.
```

---

<a id="combine-inward-and-forward"></a>
## Combine Inward and Forward

**Example:** A particle is at the lower-left side of a circle and is moving counterclockwise while speeding up. Which way should the net force point?

**Explanation**

At the lower-left side:

- the inward component points up-right
- the forward tangential component points down-right

The net force is their vector sum, so it points between up-right and down-right. That means it points generally to the right.

If one component is larger than the other, the final arrow leans toward the larger component. It still stays between the inward and tangential directions.

```quiz
type: radio
id: p1-q3
shuffle: true
content: |-
  A particle is at the lower-left side of a circle and is moving counterclockwise while speeding up. The inward component points up-right, and the tangential component points down-right. Which direction best describes the net force?
options:
- id: a
  content: |-
    Generally right, between the two component directions
  correct: true
  feedback: |-
    A vector sum points between the inward and forward tangential components.
- id: b
  content: |-
    Straight up-right, exactly toward the center
  feedback: |-
    That ignores the tangential component from speeding up.
- id: c
  content: |-
    Straight down-right, exactly tangent to the circle
  feedback: |-
    That ignores the inward component needed for circular motion.
- id: d
  content: |-
    Generally left, opposite both components
  feedback: |-
    The sum should stay between the two component directions, not opposite them.
```

---

<a id="avoid-the-tangent-only-trap"></a>
## Avoid the Tangent-Only Trap

**Example:** A particle is at the lower-right side of a circle and is moving counterclockwise, but it is slowing down. How does the tangential component change?

**Explanation**

The inward component still points toward the center, so it points up-left.

Slowing down reverses the tangential component. At the lower-right side, the counterclockwise tangent points up-right, so the slowing-down tangential component points down-left.

This is the main trap: **speeding up** means tangent forward; **slowing down** means tangent backward. In both cases, the inward component remains present.

```quiz
type: radio
id: p1-q4
shuffle: true
content: |-
  A particle is at the lower-right side of a circle and is moving counterclockwise while slowing down. Which pair of component directions should you combine for the net force?
options:
- id: a
  content: |-
    Inward up-left and tangent down-left
  correct: true
  feedback: |-
    Slowing down makes the tangent point opposite the counterclockwise motion, while the radial component still points inward.
- id: b
  content: |-
    Inward up-left and tangent up-right
  feedback: |-
    That is the pair for counterclockwise motion while speeding up.
- id: c
  content: |-
    Outward down-right and tangent down-left
  feedback: |-
    The radial component is inward, not outward.
- id: d
  content: |-
    Tangent down-left only
  feedback: |-
    Slowing down gives a backward tangential component, but circular motion still needs an inward component.
```

---

<a id="original-style-check"></a>
## Original-Style Check

**Example:** A particle is moving around a circle, with an arrow depicting the magnitude and direction of the net force acting on the particle. Which diagram represents a particle speeding up in the counterclockwise direction?

![](<../Source/Images/counterclockwise-speeding-up-net-force.png>)

**Explanation**

The particle is on the lower-right side of the circle.

- Inward toward the center points up-left.
- Counterclockwise and speeding up gives a forward tangent up-right.
- The net force points between up-left and up-right.

Among the choices, diagram C shows that combined direction.

```quiz
type: radio
id: p1-q5
content: |-
  Which diagram represents a particle speeding up in the counterclockwise direction?

  ![](<../Source/Images/counterclockwise-speeding-up-net-force.png>)
options:
- id: a
  content: |-
    A
  feedback: |-
    A is mostly the inward direction and misses the forward tangential component.
- id: b
  content: |-
    B
  feedback: |-
    B points outward and backward for this motion.
- id: c
  content: |-
    C
  correct: true
  feedback: |-
    C points between inward up-left and forward tangent up-right.
- id: d
  content: |-
    D
  feedback: |-
    D is closer to inward-only and does not include enough forward tangent.
- id: e
  content: |-
    E
  feedback: |-
    E is tangent-forward only and misses the inward component.
- id: f
  content: |-
    F
  feedback: |-
    F points backward along the tangent, which would match slowing down.
- id: g
  content: |-
    G
  feedback: |-
    G is mostly tangent-forward and misses the inward component.
- id: h
  content: |-
    H
  feedback: |-
    H points downward, not inward plus forward.
```

---

## Summary

For circular motion with changing speed:

1. Draw the inward component toward the center.
2. Draw the tangential component.
3. If the particle is speeding up, the tangential component points forward along the motion.
4. If the particle is slowing down, the tangential component points backward against the motion.
5. Choose the net-force arrow that points between the radial and tangential components.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Reading Net Force Arrows for Circular Motion](../../2026-07-05-PQ-1/Lessons/Problem-2.md)

Study guide index: 09/30

---
<!-- lesson-nav:end -->
