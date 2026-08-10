# Choosing the Net-Force Vector in Constant-Speed Circular Motion

## Table of Contents

- [Introduction](#introduction)
- [Follow the Radius Toward the Center](#follow-the-radius-toward-the-center)
- [Remove the Tangential Direction](#remove-the-tangential-direction)
- [Recognize a Crest](#recognize-a-crest)
- [Apply the Rule to the Truck](#apply-the-rule-to-the-truck)
- [Summary](#summary)

## Prerequisites

- Read the direction of a vector from its tail toward its arrowhead.
- Distinguish an object's speed from the direction of its velocity.
- Use Newton's second law, $\vec F_{\mathrm{net}}=m\vec a$.

---

<a id="introduction"></a>
## Introduction

When an object follows a circular path, its velocity is tangent to the path while its centripetal acceleration points toward the circle's center. Newton's second law makes the net force point in the same direction as that acceleration:

$$
\vec F_{\mathrm{net}}=m\vec a_c,
\qquad
\vec a_c\text{ points toward the center.}
$$

Use the same direction chain every time:

$$
\text{location of center}
\longrightarrow
\text{inward direction of }\vec a_c
\longrightarrow
\text{same direction for }\vec F_{\mathrm{net}}.
$$

The recognition cue is a locally circular path and a request for the direction of acceleration or net force. Locate the center of the path at that instant, then point inward. If the speed is constant, there is no tangential acceleration, so the net-force vector has no component along or opposite the motion. In an arrow-choice diagram, read each arrow from its dot-shaped tail toward its arrowhead; its placement on the page does not affect its direction.

---

<a id="follow-the-radius-toward-the-center"></a>
## Follow the Radius Toward the Center

**Example:** A cart is at the rightmost point of a circular track and moves upward at constant speed. Which way does the net force point?

**Explanation**

The center of the circle is directly left of the cart. Centripetal acceleration points from the cart toward that center, so Newton's second law makes the net force point directly left. The upward velocity is tangent to the circle: it identifies the current motion, while the radius toward the center identifies how the velocity must turn.

```quiz
type: radio
id: p2-follow-radius
content: |-
  A puck is at the leftmost point of a circular path and moves downward at constant speed. Which way does the net force point?
options:
- id: p2-follow-radius-a
  content: Upward
  feedback: |-
    Upward is tangent to the path at the leftmost point. Constant speed rules out tangential acceleration; the center, which controls the net-force direction, lies to the puck's right.
- id: p2-follow-radius-b
  content: Downward
  feedback: |-
    Downward is the puck's instantaneous velocity direction, not the inward direction. The net force must point from the puck toward the center, which is to the right.
- id: p2-follow-radius-c
  content: Left
  feedback: |-
    Left points outward, away from the circle's center. Circular motion requires inward acceleration, so the net force points in the opposite direction: right.
- id: p2-follow-radius-d
  content: Right
  correct: true
  feedback: |-
    Centripetal acceleration points toward the center of the circular path. The center is directly right of the puck, so $\vec a$ and therefore $\vec F_{\mathrm{net}}$ point right.
- id: p2-follow-radius-e
  content: The net force is zero
  feedback: |-
    Constant speed does not mean constant velocity on a circle because the velocity direction keeps changing. That change requires a nonzero inward acceleration and hence a nonzero net force to the right.
```

---

<a id="remove-the-tangential-direction"></a>
## Remove the Tangential Direction

**Example:** A car is at the bottom of a circular dip and moves left at constant speed. Could its net force point up and to the left?

**Explanation**

At the bottom, the circle's center is directly above the car, so the inward component points upward. An up-left vector also has a leftward tangential component. Because left is the direction of motion, that component would increase the car's speed. Constant speed requires zero tangential acceleration, leaving a net force that points straight upward. Individual forces such as weight and the road's normal force need not point upward, but their vector sum must.

```quiz
type: radio
id: p2-remove-tangent
content: |-
  A bicycle is at the bottom of a circular dip and moves right at constant speed. Which net-force direction is possible?
options:
- id: p2-remove-tangent-a
  content: Straight upward
  correct: true
  feedback: |-
    At the bottom of the dip, inward is straight upward. Constant speed makes the tangential acceleration zero, so $\vec F_{\mathrm{net}}=m\vec a$ has only that upward component.
- id: p2-remove-tangent-b
  content: Up and to the right
  feedback: |-
    The upward part is inward, but the rightward part is tangent to the path and points with the motion. It would increase the speed, so this diagonal direction is incompatible with constant speed.
- id: p2-remove-tangent-c
  content: Up and to the left
  feedback: |-
    The upward part is inward, but the leftward part is tangential and opposite the motion. It would decrease the speed, so constant speed rules out this diagonal direction.
- id: p2-remove-tangent-d
  content: Straight right
  feedback: |-
    Right is tangent to the path and along the velocity. A force in this direction would change the speed but would not provide the required upward inward acceleration.
- id: p2-remove-tangent-e
  content: Straight downward
  feedback: |-
    Downward points outward at the bottom of the dip. The centripetal acceleration and net force must point toward the center, which is upward here.
```

---

<a id="recognize-a-crest"></a>
## Recognize a Crest

**Example:** A motorcycle travels at constant speed over the top of a circular hill. Which way does the net force point?

**Explanation**

At the top of the hill, the circle's center is below the motorcycle. Therefore, the centripetal acceleration and net force point downward. The rule is not "net force points upward"; it is "net force points inward."

```quiz
type: radio
id: p2-recognize-crest
content: |-
  A cart moves left at constant speed across the top of a circular crest. Which way does the net force point?
options:
- id: p2-recognize-crest-a
  content: Left
  feedback: |-
    Left is the tangential velocity direction. Constant speed eliminates tangential acceleration, while the center of the circular arc lies below the cart.
- id: p2-recognize-crest-b
  content: Right
  feedback: |-
    Right is tangent to the path and opposite the motion, so it would slow the cart. The inward direction is instead downward toward the circle's center.
- id: p2-recognize-crest-c
  content: Upward
  feedback: |-
    Upward is outward at the top of a crest. Centripetal acceleration points toward the center below the cart, so the net force points downward.
- id: p2-recognize-crest-d
  content: Downward
  correct: true
  feedback: |-
    The circle's center is below an object at the top of a crest. Centripetal acceleration therefore points downward, and $\vec F_{\mathrm{net}}=m\vec a$ points downward as well.
- id: p2-recognize-crest-e
  content: Zero
  feedback: |-
    Although the speed is constant, the velocity turns as the cart follows the crest. A nonzero downward acceleration and net force are required to produce that directional change.
```

---

<a id="apply-the-rule-to-the-truck"></a>
## Apply the Rule to the Truck

**Example:** The truck below moves left at constant speed at the bottom of a circular dip. Determine the net-force direction before comparing the labeled vectors.

![](<../Source/2026-07-06-Q-1/Images/quiz-1a-q2-circular-dip.png>)

**Explanation**

Apply the direction chain before looking at the answer letters:

1. **Center:** directly above the truck.
2. **Inward acceleration:** straight upward.
3. **Tangential acceleration:** zero because the speed is constant.
4. **Net force:** straight upward because $\vec F_{\mathrm{net}}=m\vec a$.

The truck's leftward velocity is tangent to the path and does not change this result. In the choices, the arrow from its dot-shaped tail straight upward is vector A.

```quiz
type: radio
id: p2-truck-source
content: |-
  A truck moves at constant speed at the bottom of a circular dip as shown. Which vector could depict the net force?

  ![](<../Source/2026-07-06-Q-1/Images/quiz-1a-q2-circular-dip.png>)

  ![](<../Source/2026-07-06-Q-1/Images/quiz-1a-q2-force-vector-options.png>)
options:
- id: p2-truck-source-a
  content: A
  correct: true
  feedback: |-
    At the bottom of the dip, the center of the circular path is directly above the truck. Constant speed removes tangential acceleration, so $\vec F_{\mathrm{net}}=m\vec a$ points straight upward, as vector A does.
- id: p2-truck-source-b
  content: B
  feedback: |-
    Vector B has the needed upward component but also points right, opposite the truck's leftward motion. That tangential component would slow the truck, contradicting its constant speed; the vector must be straight upward.
- id: p2-truck-source-c
  content: C
  feedback: |-
    Vector C is purely tangential and opposite the leftward velocity, so it would slow the truck. It also lacks the upward inward component required to bend the path.
- id: p2-truck-source-d
  content: D
  feedback: |-
    Vector D points partly downward, away from the center, and partly right, opposite the motion. Circular motion at constant speed instead requires a purely upward inward net force.
- id: p2-truck-source-e
  content: E
  feedback: |-
    Vector E points straight downward, which is outward at the bottom of the dip. The net force must point toward the center of the circular path, directly upward.
- id: p2-truck-source-f
  content: F
  feedback: |-
    Vector F points partly downward, away from the center, and partly left, along the motion. It would both curve the truck the wrong way and increase its speed.
- id: p2-truck-source-g
  content: G
  feedback: |-
    Vector G points left along the truck's velocity, so it would increase the speed. It has no upward inward component to turn the velocity along the circular dip.
- id: p2-truck-source-h
  content: H
  feedback: |-
    Vector H has an upward inward component but also a leftward tangential component along the motion. That component would increase the truck's speed, so constant speed leaves only the straight-up direction.
```

---

<a id="summary"></a>
## Summary

When a problem shows circular motion and asks for the net-force direction:

1. Locate the center of the circular path at the object's current position.
2. Point the centripetal acceleration inward, from the object toward that center.
3. Use $\vec F_{\mathrm{net}}=m\vec a$ to give the net force the same direction.
4. If the speed is constant, reject every vector with a tangential component.

The main trap is following the velocity arrow. Velocity is tangent to the path; the net force for constant-speed circular motion points inward.

"Centripetal force" names the inward net-force requirement; it is not an extra force to add to the real forces in a free-body diagram.
