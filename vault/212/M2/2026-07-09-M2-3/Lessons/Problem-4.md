# Finding the Direction of a Torque Vector

<!--
lesson-id: 212-M2-014
topic-code: MTH212.M2.14
-->

## Table of Contents

- [Introduction](#introduction)
- [Determine the Sense of Rotation](#determine-the-sense-of-rotation)
- [Map Rotation to Into or Out of the Page](#map-rotation-to-into-or-out-of-the-page)
- [Check the Direction With the Cross Product](#check-the-direction-with-the-cross-product)
- [Apply the Method to the Wrench](#apply-the-method-to-the-wrench)
- [Summary](#summary)

## Prerequisites

- Position and force vectors
- Clockwise and counterclockwise rotation
- The cross product $\vec\tau=\vec r\times\vec F$
- Positive and negative coordinate directions

---

## Introduction

Torque is a vector:

$$
\vec\tau=\vec r\times\vec F.
$$

When $\vec r$ and $\vec F$ lie in the page, their cross product is perpendicular to the page. It can point only:

- out of the page, or
- into the page.

**Recognition cue:** For a planar force diagram, first decide whether the force tends to rotate the object clockwise or counterclockwise about the pivot. Then use the right-hand rule to convert that rotation into the torque-vector direction.

| Visible rotation | Torque unit-vector direction | Page direction |
|---|---:|---|
| Counterclockwise | $+\hat{\mathbf{k}}$ | Out of the page |
| Clockwise | $-\hat{\mathbf{k}}$ | Into the page |

---

## Determine the Sense of Rotation

**Example:** A horizontal wrench extends to the right from its pivot. A force at its far end points upward. Does the force turn the wrench clockwise or counterclockwise?

**Explanation**

Imagine the wrench beginning to move under the force. Its right end rises, so the wrench rotates counterclockwise about the pivot.

This visual test should come before the right-hand rule:

1. Mark the pivot.
2. Locate the force application point.
3. Imagine a small displacement in the force direction.
4. Name the resulting rotation as clockwise or counterclockwise.

```quiz
type: radio
id: problem-4-rotation-sense-q1
content: |-
  A horizontal bar extends to the right from a pivot. A downward force acts at the bar's right end. Which way does the force tend to rotate the bar?
options:
- id: a
  content: |-
    Clockwise
  correct: true
  feedback: |-
    The right end moves downward, which is clockwise rotation about the pivot.
- id: b
  content: |-
    Counterclockwise
  feedback: |-
    Counterclockwise rotation would move the right end upward.
- id: c
  content: |-
    Into the page
  feedback: |-
    Into the page is a vector direction, not the visible sense of planar rotation.
- id: d
  content: |-
    Out of the page
  feedback: |-
    Out of the page is a vector direction, not the visible sense of planar rotation.
- id: e
  content: |-
    No rotation
  feedback: |-
    The force is not directed through the pivot, so it produces nonzero torque.
```

---

## Map Rotation to Into or Out of the Page

**Example:** What torque-vector direction corresponds to counterclockwise rotation in the page?

**Explanation**

For $\vec\tau=\vec r\times\vec F$, point your right index finger along $\vec r$, point your middle finger along $\vec F$, and read the thumb as $\vec\tau$. Equivalently, curl the fingers in the direction the object tends to rotate; the thumb gives the torque-vector direction.

- Counterclockwise rotation makes the right thumb point **out of the page**.
- Clockwise rotation makes the right thumb point **into the page**.

Using the usual axes,

$$
+\hat{\mathbf{k}}=\text{out of the page},
\qquad
-\hat{\mathbf{k}}=\text{into the page}.
$$

Thus counterclockwise rotation corresponds to $+\hat{\mathbf{k}}$.

```quiz
type: radio
id: problem-4-page-direction-q1
content: |-
  A force produces clockwise rotation in the plane of the page. Which way does the torque vector point?
options:
- id: a
  content: |-
    Into the page
  correct: true
  feedback: |-
    Curling the right-hand fingers clockwise makes the thumb point into the page.
- id: b
  content: |-
    Out of the page
  feedback: |-
    Out of the page corresponds to counterclockwise rotation.
- id: c
  content: |-
    Up
  feedback: |-
    The torque vector is perpendicular to the plane containing $\vec r$ and $\vec F$.
- id: d
  content: |-
    Down
  feedback: |-
    The torque vector is perpendicular to the plane containing $\vec r$ and $\vec F$.
- id: e
  content: |-
    Right
  feedback: |-
    The torque vector cannot lie in the same plane as both $\vec r$ and $\vec F$.
```

---

## Check the Direction With the Cross Product

**Example:** Let

$$
\vec r=(0.40,0.20,0)\ \mathrm{m},
\qquad
\vec F=(0,-10,0)\ \mathrm{N}.
$$

Find the torque direction.

**Explanation**

For vectors in the $xy$-plane, only the $z$-component of torque can be nonzero:

$$
\tau_z=r_xF_y-r_yF_x.
$$

Substitute the components:

$$
\tau_z=(0.40)(-10)-(0.20)(0)=-4.0\ \mathrm{N\,m}.
$$

The negative sign means $-\hat{\mathbf{k}}$, which points into the page. This matches the clockwise rotation seen in the diagram.

```quiz
type: radio
id: problem-4-component-check-q1
content: |-
  A force has $\vec r=(0.30,0,0)\ \mathrm{m}$ and $\vec F=(0,5.0,0)\ \mathrm{N}$. What is the torque-vector direction?
options:
- id: a
  content: |-
    Out of the page
  correct: true
  feedback: |-
    $\tau_z=r_xF_y-r_yF_x=(0.30)(5.0)=+1.5\ \mathrm{N\,m}$, so the direction is $+\hat{\mathbf{k}}$, out of the page.
- id: b
  content: |-
    Into the page
  feedback: |-
    Into the page would require a negative $z$-component.
- id: c
  content: |-
    Up
  feedback: |-
    The cross product of two vectors in the page is perpendicular to the page.
- id: d
  content: |-
    Down
  feedback: |-
    The cross product of two vectors in the page is perpendicular to the page.
- id: e
  content: |-
    Zero torque
  feedback: |-
    The position and force vectors are perpendicular, so their cross product is nonzero.
```

---

## Apply the Method to the Wrench

**Example:** Determine the torque direction for the downward force on the angled wrench.

**Explanation**

The pivot is at the bolt on the left. The force acts downward at a point to the right of the pivot, so the right end of the wrench moves downward. That is clockwise rotation.

Curling the fingers of the right hand clockwise makes the thumb point into the page. Therefore,

$$
\vec\tau\ \text{points into the page}.
$$

A component check gives the same result: $r_x>0$ and $F_y<0$, while $F_x=0$, so

$$
\tau_z=r_xF_y-r_yF_x=r_xF_y<0.
$$

The torque points in the negative $z$-direction, into the page.

| Source-diagram cue | Sign or direction |
|---|---|
| Application point is right of pivot | $r_x>0$ |
| Force points downward | $F_y<0$ |
| $\tau_z=r_xF_y$ | $\tau_z<0$ |
| Negative $z$ | Into the page |

```quiz
type: radio
id: m2-3lec-q3
shuffle: true
content: |-
  **Question 3**

  For the same downward force on the wrench, what is the direction of the torque vector? Explain.

  ![](<../Source/Images/wrench-force-torque.png>)
options:
- id: a
  content: Up
- id: b
  content: Down
- id: c
  content: Right
- id: d
  content: Left
- id: e
  content: Into the page
  correct: true
  feedback: The force turns the wrench clockwise. By the right-hand rule for $\vec\tau=\vec r\times\vec F$, a clockwise torque vector points into the page.
- id: f
  content: Out of the page
```

---

## Summary

For torque caused by forces drawn in the page:

1. Mark the pivot and imagine the motion caused by the force.
2. Decide whether the rotation is clockwise or counterclockwise.
3. Curl the fingers of your right hand in that rotation direction.
4. Read the thumb direction:
   - counterclockwise $\rightarrow$ out of the page;
   - clockwise $\rightarrow$ into the page.
5. If needed, verify with $\tau_z=r_xF_y-r_yF_x$.

Always preserve the cross-product order $\vec r\times\vec F$. Swapping the vectors reverses the torque direction.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
