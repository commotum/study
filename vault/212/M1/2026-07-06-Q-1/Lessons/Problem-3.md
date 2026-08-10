# Choosing a Free-Body Diagram for a Rotating Bead

## Table of Contents

- [Introduction](#introduction)
- [List Physical Interactions Only](#list-physical-interactions-only)
- [Infer the Required Net-Force Direction](#infer-the-required-net-force-direction)
- [Recover the Loop's Contact Force](#recover-the-loops-contact-force)
- [Summary](#summary)

## Prerequisites

- Recognize weight as the gravitational force $mg$ directed downward.
- Recognize that a frictionless contact force has no component along the surface or wire.
- Recognize that constant-speed circular motion has inward acceleration $v^2/r$.
- Resolve a vector into horizontal and vertical components.

---

<a id="introduction"></a>
## Introduction

The recognition cue is an object that stays at a fixed height while a guide carries it around a vertical rotation axis. In an inertial frame, that object travels in a horizontal circle, so its acceleration is horizontal and points inward toward the axis.

Choose its free-body diagram with this three-part test:

1. **List interactions:** include one force for each object that pushes or pulls on the bead.
2. **Infer the net force:** use $\sum \vec F=m\vec a$ to determine the direction the real forces must add to.
3. **Recover the unknown force:** choose the contact-force direction whose components produce that required net force.

For a bead on a frictionless loop, Earth supplies weight and the loop supplies one contact force. “Centripetal force” is not a third interaction; it is the inward component of the net force.

The whole direction test can be compressed to

$$
\underbrace{\vec W+\vec N}_{\text{real forces}}
=
\underbrace{m\vec a_{\text{in}}}_{\text{horizontal inward resultant}}.
$$

---

<a id="list-physical-interactions-only"></a>
## List Physical Interactions Only

**Example:** A ball moves as a conical pendulum: a string holds it at constant height while it travels in a horizontal circle. Air resistance is negligible. Which forces belong on the ball's free-body diagram?

**Explanation**

Earth pulls downward with weight $m\vec g$, and the string pulls along itself with tension $\vec T$. Those are the only two interactions. The horizontal component of tension produces the inward acceleration, but that component is not an additional “centripetal force.”

In vector form,

$$
\vec T+m\vec g=m\vec a.
$$

The right side describes what the two real forces do; it does not add another force to the left side.

```quiz
type: radio
id: p3-force-inventory
content: |-
  A puck moves at constant speed in a circle on a frictionless horizontal table while a string tied to the puck leads toward the center. In an inertial frame, which list contains every force acting on the puck?
options:
- id: p3-force-inventory-real
  content: |-
    Weight, the table's normal force, and string tension
  correct: true
  feedback: |-
    Each force comes from a physical interaction: Earth supplies weight, the table supplies the upward normal force, and the string supplies inward tension. Their vector sum is inward, so these three real forces account for the circular acceleration.
- id: p3-force-inventory-extra-centripetal
  content: |-
    Weight, the table's normal force, string tension, and a centripetal force
  feedback: |-
    Tension already supplies the puck's inward net force. “Centripetal” describes the inward role of the net force rather than a separate interaction, so adding another centripetal arrow would double-count the cause of the circular acceleration.
- id: p3-force-inventory-centrifugal
  content: |-
    Weight, the table's normal force, and an outward centrifugal force
  feedback: |-
    In the stated inertial frame, no object pulls the puck outward. The string is the missing interaction and pulls inward; an outward centrifugal term is used only in a rotating-frame model, not as a real force on this inertial-frame diagram.
- id: p3-force-inventory-no-normal
  content: |-
    Weight and string tension only
  feedback: |-
    The table is in contact with the puck and prevents downward acceleration, so it supplies an upward normal force. Weight and tension alone would leave an unbalanced downward component and would not keep the puck on the horizontal table.
```

---

<a id="infer-the-required-net-force-direction"></a>
## Infer the Required Net-Force Direction

**Example:** An object travels at constant speed in a horizontal circle and remains at one height. Determine the vertical and horizontal directions of its acceleration.

**Explanation**

Its height does not change, so its vertical acceleration is zero. Its speed is constant, so there is no tangential acceleration. The only acceleration is horizontal and points toward the center of the horizontal circle:

$$
a_y=0,
\qquad
a_{\text{in}}=\frac{v^2}{r}.
$$

Newton's second law therefore requires

$$
\sum F_y=0,
\qquad
\sum F_{\text{in}}=m\frac{v^2}{r}.
$$

The forces must cancel vertically while leaving a horizontal inward resultant.

```quiz
type: radio
id: p3-net-direction
content: |-
  A bead is carried at constant speed around a vertical axis while remaining at a fixed height and a fixed distance from the axis. Which direction does the net force on the bead point?
options:
- id: p3-net-direction-inward
  content: |-
    Horizontally inward toward the rotation axis
  correct: true
  feedback: |-
    Fixed height gives zero vertical acceleration, and constant-speed circular motion gives acceleration toward the center of the horizontal circle. Thus $\sum\vec F=m\vec a$ points horizontally inward toward the rotation axis.
- id: p3-net-direction-down
  content: |-
    Vertically downward
  feedback: |-
    Gravity points downward, but the net force follows the acceleration rather than any one force. The bead has no vertical acceleration, so another force cancels its weight; the remaining net force is horizontal and inward.
- id: p3-net-direction-tangent
  content: |-
    Horizontally tangent to the circular path
  feedback: |-
    A tangential net force would change the bead's speed. Its speed is constant, so the tangential component is zero; the direction-changing acceleration and net force point inward instead.
- id: p3-net-direction-zero
  content: |-
    Zero, because both speed and height are constant
  feedback: |-
    Constant speed does not mean constant velocity on a curved path because the velocity direction keeps changing. That change requires nonzero inward acceleration and therefore a nonzero inward net force.
- id: p3-net-direction-outward
  content: |-
    Horizontally outward from the rotation axis
  feedback: |-
    Outward points away from the center and would not bend the velocity around the observed circle. In an inertial frame, circular acceleration and the corresponding net force point inward toward the axis.
```

---

<a id="recover-the-loops-contact-force"></a>
## Recover the Loop's Contact Force

**Example:** A bead moves in a horizontal circle at fixed height while touching a smooth guide. Suppose only its weight $m\vec g$ and the guide's contact force $\vec N$ act. Determine the direction of $\vec N$.

**Explanation**

Weight has no inward horizontal component, so the contact force must supply the entire inward force. Weight points downward while the bead has no vertical acceleration, so the contact force must also supply an upward component that cancels $mg$:

$$
N_y-mg=0,
\qquad
N_{\text{in}}=m\frac{v^2}{r}.
$$

Therefore, $\vec N$ points **upward and inward**. Draw it as one force vector. Its horizontal and vertical components are bookkeeping pieces of that vector, not extra forces.

For a frictionless wire, the contact force is perpendicular to the local tangent; there is no force along the wire. “Normal” means perpendicular to the guide, not automatically vertical. In the spinning-loop geometry below, the upward-and-inward direction is also toward the loop's center along the local normal line.

Use this elimination order on the diagrams:

1. Keep only weight plus one contact-force arrow.
2. Reject any force along the loop's tangent because there is no friction.
3. Require the contact arrow to point upward and inward so the resultant is purely inward.

```quiz
type: radio
id: p3-source-fbd
content: |-
  A circular loop of radius $R$ spins as shown. A glass bead of mass $m$ is free to slide on the loop and remains at an angle $\theta$. Assume there is no friction anywhere in the system.

  Which free-body diagram could accurately depict the bead?

  ![](<../Source/2026-07-06-Q-1/Images/quiz-1a-q3-spinning-loop-free-body-options.png>)
options:
- id: p3-source-fbd-a
  content: |-
    A
  feedback: |-
    Diagram A includes several non-gravitational arrows. The loop supplies only one resultant contact force, while “centripetal” is the inward net-force role and force components are not separate interactions. With no friction, the bead's diagram should contain only weight and one loop force.
- id: p3-source-fbd-b
  content: |-
    B
  feedback: |-
    Diagram B includes an extra force along the local tangent even though the contact is frictionless, and its outward-pointing contact component cannot provide the required inward resultant. The loop must instead exert one contact force with upward and inward components.
- id: p3-source-fbd-c
  content: |-
    C
  feedback: |-
    Diagram C includes an upward-and-inward arrow but also adds a tangent-direction arrow. A frictionless loop cannot exert that tangential force; its single contact force already both balances weight vertically and supplies the inward force.
- id: p3-source-fbd-d
  content: |-
    D
  correct: true
  feedback: |-
    Only gravity and the loop's normal force act on the bead. Gravity points downward, while the normal force points up and toward the vertical rotation axis; its vertical component balances $mg$, and its horizontal component supplies the centripetal net force. Therefore, diagram D has both the correct force count and directions.
```

---

<a id="summary"></a>
## Summary

For an object held at fixed height while circling a vertical axis, use **interactions, net, contact**:

1. **Interactions:** draw only forces from real pushes or pulls. Do not add “centripetal force” as a separate interaction.
2. **Net:** fixed height requires zero vertical net force, while circular motion requires a horizontal inward net force.
3. **Contact:** if weight is the only other force, the contact force must point upward to balance weight and inward to turn the object.

The main trap is drawing the required inward net force as an extra arrow. Instead, let the components of the real contact force produce that inward resultant.
