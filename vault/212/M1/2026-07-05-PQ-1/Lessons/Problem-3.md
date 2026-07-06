# Comparing Normal Force and Weight at the Top of a Hill

<!--
lesson-id: 212-M1-019
topic-code: MTH212.M1.19
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Center Direction](#choose-the-center-direction)
- [Make the Net Force Point Inward](#make-the-net-force-point-inward)
- [Compare the Opposing Forces](#compare-the-opposing-forces)
- [Reverse the Comparison When the Center Changes](#reverse-the-comparison-when-the-center-changes)
- [Avoid the Equal-Force Trap](#avoid-the-equal-force-trap)
- [Apply the Hill Question](#apply-the-hill-question)
- [Summary](#summary)

## Prerequisites

- Weight acts downward with magnitude $mg$.
- A normal force is perpendicular to the contact surface.
- For circular motion, the radial acceleration points toward the center of the circle.
- The net force points in the same direction as the acceleration.
- If $A-B>0$, then $A>B$.

---

<a id="introduction"></a>
## Introduction

When an object moves over the top of a circular hill, the center of the circular path is below the object. That means the radial acceleration points downward at the top.

Use this rule:

1. Find the direction toward the center.
2. Make the radial net force point toward the center.
3. The force pointing toward the center must be larger than the opposing force by $m\dfrac{v^2}{r}$.

At the top of a hill, gravity points toward the center and the normal force points away from the center, so gravity must be larger than the normal force.

---

<a id="choose-the-center-direction"></a>
## Choose the Center Direction

**Example:** A car is at the top of a circular hill and is still moving along the curved road. Which way is the center of the circle from the car?

**Explanation**

At the top of the hill, the circular path curves downward. The center of that circle is below the car, so the inward direction is downward.

The radial acceleration is therefore downward:

$$
a_r=\frac{v^2}{r}\quad \text{toward the center}
$$

```quiz
type: radio
id: p3-center-direction
content: |-
  A cart is at the top of a rounded track and is moving along the curve. Which direction is toward the center of the circular path at that instant?
options:
- id: a
  content: |-
    Upward
- id: b
  content: |-
    Downward
  correct: true
- id: c
  content: |-
    Horizontally forward
```

---

<a id="make-the-net-force-point-inward"></a>
## Make the Net Force Point Inward

**Example:** At the top of a circular hill, a car is moving along the road. Which way must the radial part of the net force point?

**Explanation**

The radial acceleration points toward the center of the circular path. Since net force and acceleration point in the same direction, the radial net force must also point downward.

This does not mean every force points downward. It means the combined force must point downward.

```quiz
type: radio
id: p3-net-force-direction
content: |-
  A rider is at the top of a circular hill. The center of the circular path is below the rider. What must be true about the radial part of the net force?
options:
- id: a
  content: |-
    It must point downward.
  correct: true
- id: b
  content: |-
    It must point upward.
- id: c
  content: |-
    It must be zero because the rider is at the top.
```

---

<a id="compare-the-opposing-forces"></a>
## Compare the Opposing Forces

**Example:** At the top of a hill, gravity pulls a car downward and the road's normal force pushes the car upward. If downward is the inward direction, which force must be larger while the car stays on the road?

**Explanation**

Take downward as positive for the radial direction. Gravity contributes $mg$ in the positive direction, and the normal force $N$ points opposite that direction.

So the radial force equation is

$$
mg-N=m\frac{v^2}{r}
$$

The right side is positive for a moving car on a circular path. Therefore,

$$
mg-N>0
$$

so

$$
mg>N
$$

The gravitational force is larger than the normal force.

```quiz
type: radio
id: p3-force-comparison
content: |-
  At the top of a circular hill, gravity is downward and the normal force is upward. If the car's radial net force must point downward, which comparison is required?
options:
- id: a
  content: |-
    $N>mg$
- id: b
  content: |-
    $N<mg$
  correct: true
- id: c
  content: |-
    $N=mg$
```

---

<a id="reverse-the-comparison-when-the-center-changes"></a>
## Reverse the Comparison When the Center Changes

**Example:** A car is at the bottom of a circular dip in the road. Gravity still points downward, and the normal force points upward. Which force must be larger now?

**Explanation**

At the bottom of the dip, the center of the circular path is upward. The radial net force must point upward.

Taking upward as positive, the radial force equation is

$$
N-mg=m\frac{v^2}{r}
$$

The right side is positive, so

$$
N-mg>0
$$

and therefore

$$
N>mg
$$

The comparison changes because the center direction changed.

```quiz
type: radio
id: p3-reversed-center
content: |-
  A car is moving through the bottom of a circular dip. The center of the circular path is above the car. Which comparison is required?
options:
- id: a
  content: |-
    $N>mg$
  correct: true
- id: b
  content: |-
    $N<mg$
- id: c
  content: |-
    $N=mg$
```

---

<a id="avoid-the-equal-force-trap"></a>
## Avoid the Equal-Force Trap

**Example:** A car is out of gas and rolling over the top of a circular hill. A student says, "There is no engine force, so the normal force must equal the weight." What is wrong with that reasoning?

**Explanation**

Equal upward and downward forces would give zero radial net force:

$$
mg-N=0
$$

But a moving object following a circular path needs a radial net force toward the center:

$$
mg-N=m\frac{v^2}{r}
$$

The car being out of gas does not remove the need for downward radial acceleration at the top of the hill. It only tells you there is no forward driving force from the engine.

The useful check is: if $N=mg$, then the radial net force would be $0$, so the car would not have the required inward radial acceleration at that instant.

```quiz
type: radio
id: p3-equal-force-trap
content: |-
  Why is $N=mg$ the wrong comparison for a moving car at the top of a circular hill?
options:
- id: a
  content: |-
    Equal forces would give zero radial net force, but the car needs a downward radial net force.
  correct: true
- id: b
  content: |-
    Equal forces would make the car accelerate upward toward the center.
- id: c
  content: |-
    Equal forces are impossible whenever an object is out of gas.
```

---

<a id="apply-the-hill-question"></a>
## Apply the Hill Question

**Example:** An out-of-gas car is rolling over the top of a circular hill. At this instant, compare the normal force on the car with the gravitational force on the car.

**Explanation**

At the top of the hill:

- the center of the circular path is downward,
- the radial net force must point downward,
- gravity acts downward,
- the normal force acts upward.

So gravity must be larger than the normal force:

$$
mg>N
$$

Equivalently, the normal force is less than the gravitational force.

```quiz
type: radio
id: p3-original-question
content: |-
  An out-of-gas car is rolling over the top of a circular hill. At this instant ____
options:
- id: a
  content: |-
    the normal force on the car is greater than the gravitational force on the car
- id: b
  content: |-
    the normal force on the car is less than the gravitational force on the car
  correct: true
- id: c
  content: |-
    the normal force on the car is equal to the gravitational force on the car
```

---

<a id="summary"></a>
## Summary

At the top of a circular hill, the center of the path is below the car. The radial acceleration and radial net force must point downward. Since gravity points downward and the normal force points upward,

$$
mg-N=m\frac{v^2}{r}>0
$$

so $mg>N$. The normal force is less than the gravitational force. The common trap is choosing $N=mg$ as if the car had zero vertical acceleration; circular motion requires a downward radial net force at the top.

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Recognizing Contact Loss on a Curved Surface](<../../2026-07-03-HW-2/Lessons/Problem-12.md>)

<!-- study-guide-nav:end -->

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]
