# Radial Direction of Successive Velocity Changes

<!--
lesson-id: 212-M1-073
topic-code: MTH212.M1.73
-->

## Table of Contents

- [Introduction](#introduction)
- [Reverse the Initial Velocity](#reverse-the-initial-velocity)
- [Read the Difference From Components](#read-the-difference-from-components)
- [Recognize the Inward Result](#recognize-the-inward-result)
- [Apply the Move Around the Path](#apply-the-move-around-the-path)
- [Summary](#summary)

## Prerequisites

- Read the head of an arrow as the direction of a vector.
- Recognize that equal vector magnitudes do not make differently directed vectors equal.
- Add and subtract horizontal and vertical vector components.

---

<a id="introduction"></a>
## Introduction

In these circular-motion diagrams, an arrow's length represents speed and its arrowhead represents the velocity's direction. Equal arrow lengths therefore mean equal speeds, but differently directed arrows are still different velocities.

The recognition cue is a sequence of equal-length velocity arrows tangent to the same circular path. For two successive velocities, the change is

$$
\Delta\vec v=\vec v_{\text{final}}-\vec v_{\text{initial}}.
$$

The useful visual move is to reverse the initial velocity and then add:

$$
\Delta\vec v=\vec v_{\text{final}}+\left(-\vec v_{\text{initial}}\right).
$$

Use this visual procedure:

1. Place the initial and final velocity arrows tail to tail without rotating them.
2. Reverse the initial arrow, or equivalently draw from the head of the initial arrow to the head of the final arrow.
3. Read the direction of that resultant.
4. Repeat for the next adjacent pair.

For equal-speed tangent vectors around a circular path, this difference points radially inward. The velocity itself is tangent to the path; it is the **change in velocity** that points toward the center. This purely inward conclusion depends on the speed staying constant; a changing speed can add a tangential part to $\Delta\vec v$.

---

<a id="reverse-the-initial-velocity"></a>
## Reverse the Initial Velocity

**Example:** A particle's initial velocity points east, and its equal-magnitude final velocity points south. Determine the direction of $\Delta\vec v=\vec v_f-\vec v_i$.

**Explanation**

Rewrite subtraction as addition of the opposite vector:

$$
\Delta\vec v=\underbrace{\vec v_f}_{\text{south}}+
\underbrace{(-\vec v_i)}_{\text{west}}.
$$

Adding a southward vector and a westward vector gives a southwest result. The reversal applies to the initial vector only.

There is an equivalent tail-to-tail shortcut: once $\vec v_i$ and $\vec v_f$ share a tail, $\vec v_f-\vec v_i$ is the arrow from the head of $\vec v_i$ to the head of $\vec v_f$. Drawing that connector backward would instead give $\vec v_i-\vec v_f$.

```quiz
type: radio
id: radial-delta-v-reverse-initial
shuffle: true
content: |-
  A particle's initial velocity points north, and its equal-magnitude final velocity points east. Which direction does $\Delta\vec v=\vec v_f-\vec v_i$ point?
options:
- id: southeast
  content: |-
    Southeast
  correct: true
  feedback: |-
    Vector subtraction reverses the initial northward velocity to point south. Adding that southward vector to the eastward final velocity makes $\Delta\vec v$ point southeast.
- id: northeast
  content: |-
    Northeast
  feedback: |-
    Northeast comes from adding the final eastward velocity to the unreversed initial northward velocity. The expression is a difference, so $\vec v_i$ must first be reversed to point south.
- id: southwest
  content: |-
    Southwest
  feedback: |-
    Reversing the initial velocity supplies a southward component, but the final velocity still points east. Nothing in $\vec v_f-\vec v_i$ supplies a westward component here.
- id: northwest
  content: |-
    Northwest
  feedback: |-
    This direction reverses the final eastward component and leaves the initial northward direction unchanged. Only the initial vector is negated, so the result has eastward and southward components.
- id: zero
  content: |-
    The zero vector
  feedback: |-
    Equal speeds mean equal velocity magnitudes, not equal velocity vectors. Because north and east are different directions, subtracting the two velocities gives a nonzero change.
```

---

<a id="read-the-difference-from-components"></a>
## Read the Difference From Components

**Example:** Let $\vec v_i=\langle 4,0\rangle$ and $\vec v_f=\langle 0,-4\rangle$. Determine the direction of $\Delta\vec v$.

**Explanation**

Subtract corresponding components:

$$
\Delta\vec v
=\langle 0,-4\rangle-\langle 4,0\rangle
=\langle -4,-4\rangle.
$$

The negative horizontal component points left, and the negative vertical component points down. Therefore, $\Delta\vec v$ points southwest. Components provide a sign check for the same reverse-and-add construction.

The check is always **final minus initial in each slot**:

$$
\Delta\vec v
=\langle v_{f,x}-v_{i,x},\ v_{f,y}-v_{i,y}\rangle.
$$

```quiz
type: radio
id: radial-delta-v-component-direction
shuffle: true
content: |-
  A velocity changes from $\vec v_i=\langle 0,3\rangle$ to $\vec v_f=\langle -3,0\rangle$. Which direction does $\Delta\vec v$ point?
options:
- id: southwest
  content: |-
    Southwest
  correct: true
  feedback: |-
    Subtract component by component: $\Delta\vec v=\langle -3-0,0-3\rangle=\langle -3,-3\rangle$. Its negative horizontal and vertical components make it point southwest.
- id: northwest
  content: |-
    Northwest
  feedback: |-
    A northwest result would have a positive vertical component. Here the vertical calculation is $0-3=-3$, because the initial northward component must be subtracted.
- id: southeast
  content: |-
    Southeast
  feedback: |-
    A southeast result would require a positive horizontal component. The final horizontal component is $-3$, so $-3-0$ remains negative and points left.
- id: northeast
  content: |-
    Northeast
  feedback: |-
    Northeast is the direction of $\vec v_i-\vec v_f=\langle 3,3\rangle$, which reverses the subtraction order. The requested $\vec v_f-\vec v_i$ points in the opposite direction.
- id: west
  content: |-
    West
  feedback: |-
    West is the direction of the final velocity alone. The change also includes $-\vec v_i$, which contributes a southward component, so the result is southwest.
```

---

<a id="recognize-the-inward-result"></a>
## Recognize the Inward Result

**Example:** On the upper-right part of a clockwise circular path, an equal-speed velocity turns from eastward to southeastward. Determine the general direction of the velocity change.

**Explanation**

The final velocity has rightward and downward components. Reversing the initial eastward velocity contributes a leftward component. Because the two velocities have equal magnitudes, the rightward part of the final vector does not cancel all of the reversed initial vector. The difference points down and left, toward the center associated with the turn between the two tangent directions.

This is the circular-motion pattern:

$$
\text{successive equal-speed tangent velocities}
\quad\Longrightarrow\quad
\Delta\vec v\text{ points radially inward}.
$$

```quiz
type: radio
id: radial-delta-v-inward-cue
shuffle: true
content: |-
  At the right side of a clockwise circular path, an object's equal-speed tangent velocity turns from southeast to south. Which description best matches $\Delta\vec v$ for this turn?
options:
- id: inward
  content: |-
    It points radially inward, with a leftward component.
  correct: true
  feedback: |-
    Successive equal-speed tangent velocities differ in the inward radial direction. Here subtracting the southeast initial velocity from the southward final velocity produces a leftward component and points toward the center.
- id: tangent-forward
  content: |-
    It points tangent to the path in the same direction as the final velocity.
  feedback: |-
    The final velocity is tangent, but $\Delta\vec v$ is the difference between two tangent velocities. Reversing the initial vector and adding it leaves an inward component rather than another tangent vector.
- id: outward
  content: |-
    It points radially outward, away from the center.
  feedback: |-
    An outward result corresponds to reversing the subtraction order and finding $\vec v_i-\vec v_f$. The requested $\vec v_f-\vec v_i$ points in the opposite, inward direction.
- id: tangent-backward
  content: |-
    It points tangent to the path opposite the motion.
  feedback: |-
    $-\vec v_i$ points opposite the initial motion, but it is only one term in the sum. Adding the final velocity to it produces the inward resultant, not a backward tangent.
- id: zero
  content: |-
    It is zero because the speed is unchanged.
  feedback: |-
    Constant speed fixes only the magnitudes of the two velocities. Their directions differ, so the velocity vectors are unequal and their difference is nonzero and inward.
```

---

<a id="apply-the-move-around-the-path"></a>
## Apply the Move Around the Path

**Example:** At the upper-left part of a clockwise circular path, a tangent velocity turns from northeast to east. Determine the direction of the velocity change.

**Explanation**

Reverse the northeast initial vector so that it points southwest, then add the eastward final vector. The result points down and right, which is inward from the upper-left part of the path. The same construction can be repeated independently for every adjacent pair of velocity vectors.

**Target problem — answer in words or by drawing three arrows before using the self-check:**

**Question 2**

For the velocity vectors around the circular path, determine the directions of $\vec v_2-\vec v_1$, $\vec v_3-\vec v_2$, and $\vec v_4-\vec v_3$.

![](<../Source/Images/vectors-2.jpg>)

![](<../Source/Images/vectors-3.jpg>)

```quiz
type: radio
id: khadley-circular-motion-q2
shuffle: true
content: |-
  Which self-check matches all three directions in Question 2?
options:
- id: inward-sequence
  content: |-
    $\vec v_2-\vec v_1$ points down-left, $\vec v_3-\vec v_2$ points left and slightly down, and $\vec v_4-\vec v_3$ points left and slightly up. All three point radially inward.
  correct: true
  feedback: |-
    For every pair, $\Delta\vec v=\vec v_{\text{final}}+(-\vec v_{\text{initial}})$. Applying that construction at the three displayed positions gives the listed page directions, each toward the center of the circular path.
- id: final-velocity-sequence
  content: |-
    The three differences point southeast, south, and southwest, matching $\vec v_2$, $\vec v_3$, and $\vec v_4$.
  feedback: |-
    These are the directions of the final velocities, not of their changes. Each difference must also include the reversed initial velocity, which turns the resultant away from the tangent and toward the center.
- id: outward-sequence
  content: |-
    The three differences point outward, opposite the inward arrows shown in the second diagram.
  feedback: |-
    Outward differences result from reversing the subtraction order to $\vec v_{\text{initial}}-\vec v_{\text{final}}$. The requested final-minus-initial differences point in the opposite, inward direction.
- id: zero-sequence
  content: |-
    All three differences are zero because all four velocity arrows have the same length.
  feedback: |-
    Equal arrow lengths mean equal speeds, but the velocity directions change from one side of the path to the next. Differently directed vectors are unequal, so each successive difference is nonzero.
- id: fixed-left-sequence
  content: |-
    All three differences point directly left because the center is left of the labeled arrows.
  feedback: |-
    Inward is a local radial direction, so its page direction changes around the path. The first two resultants include downward components, while the third includes an upward component; only their inward character stays the same.
```

---

<a id="summary"></a>
## Summary

When successive equal-speed velocity arrows are tangent to a circular path:

1. Recognize the cue: equal-length tangent arrows at successive positions.
2. Keep the final velocity unchanged and reverse the initial velocity.
3. Add the arrows; tail to tail, the same result runs from the initial head to the final head.
4. Check with $\langle v_{f,x}-v_{i,x},v_{f,y}-v_{i,y}\rangle$ when components are useful.
5. Read the resultant's direction and repeat for each adjacent pair.

The repeated result is radial and inward. Do not confuse the tangent direction of $\vec v$ with the inward direction of $\Delta\vec v$, and do not reverse the subtraction order. The inward-only rule requires constant speed; if the arrow lengths change, check for a tangential component too.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
