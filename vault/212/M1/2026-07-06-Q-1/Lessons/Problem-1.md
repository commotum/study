# Acceleration in Constant-Speed Circular Motion

## Table of Contents

- [Introduction](#introduction)
- [Constant Speed Can Still Mean Acceleration](#constant-speed-can-still-mean-acceleration)
- [Pair Tangent Velocity with Inward Acceleration](#pair-tangent-velocity-with-inward-acceleration)
- [Apply the Constant-Speed Circle Test](#apply-the-constant-speed-circle-test)
- [Summary](#summary)

## Prerequisites

- Recognize that a vector has both magnitude and direction.
- Recognize the radius from an object to the center of a circle.
- Recognize the tangent direction at a point on a circle.

---

<a id="introduction"></a>
## Introduction

The recognition cue is **constant speed along a circular path**. A velocity vector carries two pieces of information: magnitude (speed) and direction. Constant speed fixes the magnitude, but the velocity vector still turns as the object moves. Acceleration describes that change in velocity, so it is not zero:

$$
|\vec v|=\text{constant}
\qquad\text{but}\qquad
\frac{d\vec v}{dt}\ne \vec 0.
$$

For constant-speed circular motion, use this direction rule:

$$
\boxed{\text{velocity is tangent to the circle, while acceleration points inward toward the center}}
$$

A tangent is perpendicular to the radius at the point of contact. Therefore, the acceleration is perpendicular to the instantaneous velocity.

Use a three-question check:

1. Is the path curved? Then the velocity direction changes.
2. Is the speed constant? Then there is no tangential acceleration.
3. Where is the center? The remaining acceleration points there.

---

<a id="constant-speed-can-still-mean-acceleration"></a>
## Constant Speed Can Still Mean Acceleration

**Example:** An object moves clockwise around a circle at constant speed. At the top of the circle, its velocity points to the right. A moment later, its velocity points slightly downward as well as to the right. What changed?

**Explanation**

The two velocity vectors have the same magnitude because the speed is constant, but they have different directions. Subtracting the earlier velocity vector from the later one gives a change $\Delta\vec v$ that points inward in the short-time limit. Since $\vec a$ has the direction of $\Delta\vec v/\Delta t$, the acceleration is nonzero and points toward the center.

```quiz
type: radio
id: p1-speed-direction
content: |-
  A cyclist follows a circular track at constant speed. Which part of the cyclist's velocity changes?
options:
- id: p1-speed-direction-speed-only
  content: |-
    Its magnitude only
  feedback: |-
    The magnitude of velocity is the speed, and the prompt says that speed is constant. The part that changes on the curved path is the velocity's direction, not its magnitude.
- id: p1-speed-direction-direction-only
  content: |-
    Its direction only
  correct: true
  feedback: |-
    Constant speed keeps the velocity's magnitude fixed, while motion around the circle continually turns the velocity vector. Therefore, only its direction changes.
- id: p1-speed-direction-neither
  content: |-
    Neither its magnitude nor its direction
  feedback: |-
    An unchanged velocity would produce straight-line motion. The cyclist stays on a circle only because the velocity direction continually changes, even though its magnitude stays fixed.
- id: p1-speed-direction-both
  content: |-
    Both its magnitude and its direction
  feedback: |-
    Circular motion does change the velocity's direction, but constant speed rules out a change in its magnitude. Thus only the direction changes here.
```

---

<a id="pair-tangent-velocity-with-inward-acceleration"></a>
## Pair Tangent Velocity with Inward Acceleration

**Example:** An object is at the bottom of a circle and moves clockwise at constant speed. Determine the directions of its velocity and acceleration.

**Explanation**

At the bottom, clockwise motion makes the tangent velocity point left. The center of the circle is above the object, so the acceleration points up. The direction of motion chooses between the two possible tangent directions, but it never changes which way is inward. Left and up are perpendicular directions.

Use the geometry in this order:

1. Locate the center.
2. Draw the acceleration from the object toward the center.
3. Draw the velocity tangent to the path in the stated direction of motion.
4. Check that the two directions are perpendicular.

```quiz
type: radio
id: p1-left-side-direction
content: |-
  An object is at the leftmost point of a circle and moves clockwise at constant speed. Which direction does its acceleration point?
options:
- id: p1-left-side-direction-up
  content: |-
    Upward
  feedback: |-
    Upward is the clockwise tangent direction at the leftmost point, so it is the velocity direction. Acceleration instead follows the inward radius, which points right toward the center.
- id: p1-left-side-direction-down
  content: |-
    Downward
  feedback: |-
    Downward is tangent to the circle but opposite the stated clockwise motion. Neither tangent direction is centripetal; the acceleration points inward, to the right.
- id: p1-left-side-direction-left
  content: |-
    Leftward
  feedback: |-
    Leftward points away from the circle's center at this location. Centripetal acceleration points toward the center, so at the leftmost point it points rightward.
- id: p1-left-side-direction-right
  content: |-
    Rightward
  correct: true
  feedback: |-
    Centripetal acceleration always points from the object toward the circle's center. The center is to the right of the leftmost point, so the acceleration points rightward.
- id: p1-left-side-direction-zero
  content: |-
    The acceleration is zero
  feedback: |-
    Constant speed removes a change in velocity magnitude, but the velocity direction still changes around the circle. That turning requires nonzero inward acceleration, which points right here.
```

---

<a id="apply-the-constant-speed-circle-test"></a>
## Apply the Constant-Speed Circle Test

**Example:** A runner rounds a circular bend at constant speed. Decide whether the acceleration can point along or opposite the velocity.

**Explanation**

Split acceleration into tangent and radial roles:

$$
a_t=\frac{d(\text{speed})}{dt},
\qquad
a_r=\frac{v^2}{r}.
$$

Constant speed gives $a_t=0$. The radial acceleration remains nonzero and points inward, so the total acceleration is perpendicular to the tangent velocity. A forward tangential component would increase the speed; a backward tangential component would decrease it. Either would contradict the constant-speed condition.

```quiz
type: radio
id: p1-source-check
shuffle: true
content: |-
  If an object travels at a constant speed in a circular path, the acceleration of the object is
options:
- id: p1-source-check-same
  content: |-
    in the same direction as the velocity of the object.
  feedback: |-
    Acceleration along the velocity is a forward tangential acceleration, which increases speed. The speed is constant here, so the acceleration has no forward tangential component and instead points inward.
- id: p1-source-check-opposite
  content: |-
    in the opposite direction from the velocity of the object.
  feedback: |-
    Acceleration opposite the velocity is a backward tangential acceleration, which decreases speed. Constant speed rules that out; the needed acceleration changes direction by pointing inward.
- id: p1-source-check-perpendicular
  content: |-
    perpendicular to the velocity of the object.
  correct: true
  feedback: |-
    Constant speed eliminates tangential acceleration. The remaining centripetal acceleration points along the inward radius, while velocity is tangent to the circle, so the two vectors are perpendicular.
```

If the speed were changing, a tangential acceleration component could also be present. Then the total acceleration would generally not be perpendicular to the velocity. The perpendicular conclusion depends on the phrase **constant speed**.

---

<a id="summary"></a>
## Summary

When an object moves at constant speed on a circular path, ask **curve, speed, center**:

1. **Curve:** The curved path changes the velocity direction, so acceleration is not zero.
2. **Speed:** Constant speed removes the tangential acceleration component.
3. **Center:** The remaining acceleration points inward while velocity is tangent, so they are perpendicular.

The main trap is choosing a direction along the velocity. Along would speed the object up, and opposite would slow it down; neither fits constant-speed motion.
