# Identifying the Restoring Force in a Transverse String Wave

<!--
lesson-id: 212-M5-004
topic-code: MTH212.M5.04
-->

## Table of Contents

- [Introduction](#introduction)
- [Add the Tension Forces on a Curved Segment](#add-the-tension-forces-on-a-curved-segment)
- [Use Curvature to Find the Restoring Direction](#use-curvature-to-find-the-restoring-direction)
- [Test Gravity Against the Restoring-Force Requirement](#test-gravity-against-the-restoring-force-requirement)
- [Separate the Driver From the Restoring Interaction](#separate-the-driver-from-the-restoring-interaction)
- [Apply the Reasoning to the String Diagram](#apply-the-reasoning-to-the-string-diagram)
- [Summary](#summary)

## Prerequisites

- Treat a force as a vector with magnitude and direction.
- Split a force into horizontal and vertical components.
- Recognize that a restoring force points back toward equilibrium.

---

<a id="introduction"></a>
## Introduction

A restoring force must change direction with the displacement so that it points back toward equilibrium.

For a transverse wave on a taut string, each small string element is pulled by the neighboring string on both sides. These pulls are tension forces directed along the local tangents to the string.

If the left and right tension vectors are $\vec T_L$ and $\vec T_R$, their resultant is

$$
\vec F_{\mathrm{net}}=\vec T_L+\vec T_R.
$$

- On a straight equilibrium segment, the two tension forces oppose and cancel.
- On a curved segment, their transverse components do not cancel.
- The resulting transverse force points toward the inside of the curve and pulls the element back toward equilibrium.

The recognition cue is a curved, taut string carrying a transverse disturbance. The restoring interaction is **tension**, acting through the geometry of neighboring string segments.

---

<a id="add-the-tension-forces-on-a-curved-segment"></a>
## Add the Tension Forces on a Curved Segment

**Example:** Consider a small string element centered at the top of a crest. The left neighbor pulls down and left along the string, while the right neighbor pulls down and right. What is the direction of the net force?

**Explanation**

The two forces have equal and opposite horizontal components, so those components cancel. Both forces have downward vertical components, so those components add.

For a symmetric crest with tension magnitude $T$ and local angle $\theta$,

$$
F_x=-T\cos\theta+T\cos\theta=0,
$$

while

$$
F_y=-T\sin\theta-T\sin\theta=-2T\sin\theta<0.
$$

The net force is downward, toward the equilibrium line.

**Watch Out!** Equal tension magnitudes do not automatically give zero resultant. Two vectors cancel only when they have equal magnitudes and exactly opposite directions; a curved string changes those directions.

```quiz
type: radio
id: problem-4-components-q1
content: |-
  A small string element lies at the bottom of a trough. The tension forces from its two neighbors point up-left and up-right. What is the net transverse force direction?
options:
- id: a
  content: |-
    Upward
  correct: true
  feedback: |-
    The horizontal components cancel, while both upward components add and pull the element toward equilibrium.
- id: b
  content: |-
    Downward
  feedback: |-
    A downward force would pull the trough farther from equilibrium rather than restore it.
- id: c
  content: |-
    Zero
  feedback: |-
    The horizontal components cancel, but the upward components reinforce each other.
```

---

<a id="use-curvature-to-find-the-restoring-direction"></a>
## Use Curvature to Find the Restoring Direction

**Example:** Compare a string element at a crest, at a trough, and on a locally straight section. How does the transverse tension force change?

**Explanation**

The tension force follows the local shape:

| Local shape | Net transverse tension force |
|---|---|
| Crest, above equilibrium | Downward |
| Trough, below equilibrium | Upward |
| Locally straight segment | Zero transverse resultant |

The force reverses between a crest and a trough, which is exactly what a restoring force must do.

```quiz
type: radio
id: problem-4-curvature-q1
content: |-
  A displaced string element is above equilibrium, and the string curves downward on both sides of it. Which statement best describes the net force from tension?
options:
- id: a
  content: |-
    It points downward, back toward equilibrium.
  correct: true
  feedback: |-
    The neighboring string segments provide downward transverse components that add.
- id: b
  content: |-
    It points upward, farther from equilibrium.
  feedback: |-
    A restoring force must oppose the displacement from equilibrium.
- id: c
  content: |-
    It is always zero because the tension magnitudes are equal.
  feedback: |-
    Equal magnitudes do not cancel when the two tension vectors point in different directions.
```

---

<a id="test-gravity-against-the-restoring-force-requirement"></a>
## Test Gravity Against the Restoring-Force Requirement

**Example:** Could gravity be the restoring interaction for both crests and troughs of a horizontal string wave?

**Explanation**

No. Gravity points downward whether a string element is above or below equilibrium. A transverse restoring force must point downward at a crest but upward at a trough.

Gravity may affect the string's overall sag or equilibrium shape, but it does not reverse direction with the local wave displacement. The transverse components of tension do reverse because the local string geometry reverses.

```quiz
type: radio
id: problem-4-gravity-q1
content: |-
  Why is gravity not the restoring interaction responsible for a transverse wave on the taut string?
options:
- id: a
  content: |-
    Gravity has no magnitude.
  feedback: |-
    Gravity has a nonzero magnitude; the issue is its unchanging direction.
- id: b
  content: |-
    Gravity always points downward and does not reverse between crests and troughs.
  correct: true
  feedback: |-
    The restoring force must change direction to point toward equilibrium on both sides.
- id: c
  content: |-
    Gravity acts only on the supports, not on the string.
  feedback: |-
    Gravity acts on the string too, but it does not supply the alternating restoring interaction.
```

---

<a id="separate-the-driver-from-the-restoring-interaction"></a>
## Separate the Driver From the Restoring Interaction

**Example:** A mechanical driver at one end starts a wave on a string. Does the driver directly restore every string element after the wave has begun traveling?

**Explanation**

No. The driver supplies the initial or continuing disturbance at the boundary. Away from the driver, each element interacts locally with its neighboring elements through tension.

Those local tension forces transmit the disturbance and provide the transverse force back toward equilibrium.

```quiz
type: radio
id: problem-4-driver-q1
content: |-
  After a pulse leaves the hand that created it, what local interaction continues to restore displaced elements of a taut string?
options:
- id: a
  content: |-
    Tension from neighboring string segments
  correct: true
  feedback: |-
    The transverse components of the neighboring tension forces pull curved elements toward equilibrium.
- id: b
  content: |-
    A direct push from the hand on every element
  feedback: |-
    The hand acts only at the boundary; the disturbance is transmitted by local string tension.
- id: c
  content: |-
    Gravity alone
  feedback: |-
    Gravity does not reverse direction with the transverse displacement.
```

---

<a id="apply-the-reasoning-to-the-string-diagram"></a>
## Apply the Reasoning to the String Diagram

**Example:** A transverse wave propagates along the string shown. What provides the restoring force? Explain.

![](<../Source/Images/transverse-wave-string-particles.png>)

**Explanation**

The diagram shows curved portions of a taut string. For any small particle or segment, the string on each side pulls along its local tangent. On a curved segment, the transverse components of those tension forces do not cancel. Their resultant points toward equilibrium.

| Evidence in the diagram | Force interpretation |
|---|---|
| The string is taut | Neighboring segments exert tension |
| The string is locally curved | The two tension directions are not opposite |
| Transverse components point toward the inside of the curve | Their resultant restores the segment toward equilibrium |

Gravity may influence the string's overall sag, but it does not switch direction between crests and troughs. Therefore, tension provides the restoring force.

```quiz
type: radio
id: m5-1lec-q3
shuffle: true
content: |-
  **Question 3**

  A transverse wave propagates along the string shown. What provides the restoring force? Explain.

  ![](<../Source/Images/transverse-wave-string-particles.png>)
options:
- id: a
  content: Gravity
  feedback: Gravity can affect the string's overall sag, but it is not the restoring interaction responsible for the transverse wave.
- id: b
  content: Tension
  correct: true
  feedback: On a curved string segment, the transverse components of the tension forces do not cancel. Their net force pulls the segment toward equilibrium.
- id: c
  content: Other
```

---

<a id="summary"></a>
## Summary

To identify the restoring force for a transverse wave on a string:

1. Isolate a small curved string element.
2. Draw the two tension forces along the local string directions.
3. Cancel opposing longitudinal components and add the transverse components.
4. Verify that the net transverse force points back toward equilibrium.
5. Reject forces such as gravity that do not reverse direction between crests and troughs.

The restoring interaction is **tension**. Curvature makes its transverse components fail to cancel, producing the net force toward equilibrium.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
