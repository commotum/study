# Testing Loop-the-Loop Statements

<!--
lesson-id: 212-M1-063
topic-code: MTH212.M1.63
-->

## Table of Contents

- [Introduction](#introduction)
- [Use the Top of the Loop as the Contact Test](#use-the-top-of-the-loop-as-the-contact-test)
- [Use Energy to Connect the Entry Speed and the Top Speed](#use-energy-to-connect-the-entry-speed-and-the-top-speed)
- [Separate Energy Conservation from Uniform Circular Motion](#separate-energy-conservation-from-uniform-circular-motion)
- [Check Whether the Centripetal Force Is Constant](#check-whether-the-centripetal-force-is-constant)
- [Choose the True Statements](#choose-the-true-statements)
- [Summary](#summary)

## Prerequisites

- Use $a_r=\dfrac{v^2}{R}$ for circular motion of radius $R$.
- Read a radial force equation in the inward direction.
- Use conservation of mechanical energy when friction is neglected.
- Uniform circular motion means circular motion at constant speed.

---

<a id="introduction"></a>
## Introduction

Skateboarder Hony Tawk enters a vertical loop and completes the circle without leaving the track. Rolling friction is neglected. Does completing the loop require a minimum entry speed? What happens to the normal force at that threshold? Is the motion uniform, is the required inward force constant, and is mechanical energy conserved?

![](<../Source/Images/loop-the-loop-diagram.png>)

These questions separate three ideas that can look similar in a circular-motion diagram. Contact depends on whether the track can provide the required normal force. Energy conservation determines how speed changes with height. Uniform circular motion, by contrast, would require that speed to remain constant.

Use Newton's second law locally at the top to test contact, then use energy between the bottom and top to connect the two speeds. The force equation describes one position; the energy equation is the bridge between positions.

---

<a id="use-the-top-of-the-loop-as-the-contact-test"></a>
## Use the Top of the Loop as the Contact Test

**Example:** A rider moves through the top of a vertical loop of radius $R$ with speed $v_{\text{top}}$. What condition must hold for the rider to just maintain contact?

**Explanation**

At the top of the loop, inward points downward. Gravity points inward, and the normal force also points inward if the track is pushing on the rider:

$$
N+mg=m\dfrac{v_{\text{top}}^2}{R}.
$$

The track can push, but it cannot pull. So contact requires

$$
N\ge 0.
$$

At the exact minimum speed for contact, the normal force is just zero:

$$
mg=m\dfrac{v_{\text{top}}^2}{R}.
$$

Therefore

$$
v_{\text{top}}=\sqrt{gR}.
$$

At the threshold, this top-of-the-loop condition determines the smallest speed that still permits contact.

```quiz
type: radio
id: p10-q1-contact
shuffle: true
content: |-
  At the top of a vertical loop, a rider is just barely maintaining contact with the track. What is the normal force at that instant?
options:
- id: p10q1-a
  content: |-
    $N=0$
  correct: true
- id: p10q1-b
  content: |-
    $N=mg$
- id: p10q1-c
  content: |-
    $N=m\dfrac{v^2}{R}+mg$
- id: p10q1-d
  content: |-
    $N$ must point outward from the center.
```

---

<a id="use-energy-to-connect-the-entry-speed-and-the-top-speed"></a>
## Use Energy to Connect the Entry Speed and the Top Speed

**Example:** A rider enters the loop at the bottom with speed $v_0$. The top of the loop is $2R$ higher than the bottom. If friction is neglected, what entry speed gives the minimum top speed for contact?

**Explanation**

Use conservation of mechanical energy between the bottom and the top:

$$
\dfrac{1}{2}mv_0^2=\dfrac{1}{2}mv_{\text{top}}^2+mg(2R).
$$

At the minimum speed, the top speed satisfies

$$
v_{\text{top}}^2=gR.
$$

Substitute this into the energy equation:

$$
\dfrac{1}{2}mv_0^2=\dfrac{1}{2}m(gR)+2mgR.
$$

So

$$
v_0^2=5gR,
$$

and

$$
v_0=\sqrt{5gR}.
$$

Thus the loop has a minimum entry speed, $\sqrt{5gR}$, which grows with the square root of its radius.

The normal force does not appear in the energy equation because it points perpendicular to the rider's motion along the track. With rolling friction neglected, gravity trades kinetic energy and potential energy while their sum stays approximately constant.

```quiz
type: radio
id: p10-q2-minimum-speed
shuffle: true
content: |-
  A rider enters a frictionless vertical loop from the bottom. Which reason best explains why there is a minimum entry speed?
options:
- id: p10q2-a
  content: |-
    The rider must still have enough speed at the top so gravity can provide the needed inward acceleration without the track needing to pull.
  correct: true
- id: p10q2-b
  content: |-
    The rider must keep the same speed at every point in the loop.
- id: p10q2-c
  content: |-
    The normal force must be largest at the top of the loop.
- id: p10q2-d
  content: |-
    Mechanical energy must increase as the rider rises.
```

```quiz
type: radio
id: p10-q2-energy-conservation
shuffle: true
content: |-
  In a loop-the-loop problem with rolling friction neglected, why is kinetic plus gravitational potential energy approximately conserved?
options:
- id: p10q2e-a
  content: |-
    Gravity is conservative, and the normal force is perpendicular to the motion along the track.
  correct: true
- id: p10q2e-b
  content: |-
    The normal force always has the same magnitude as the weight.
- id: p10q2e-c
  content: |-
    The rider has constant speed throughout the loop.
- id: p10q2e-d
  content: |-
    The centripetal force is constant throughout the loop.
```

---

<a id="separate-energy-conservation-from-uniform-circular-motion"></a>
## Separate Energy Conservation from Uniform Circular Motion

**Example:** A rider moves through a vertical loop with rolling friction neglected. Is the motion uniform circular motion?

**Explanation**

Uniform circular motion requires constant speed.

In a vertical loop, the rider trades kinetic energy and gravitational potential energy. As the rider goes upward, height increases, so speed decreases. As the rider comes back down, height decreases, so speed increases.

The force view gives the same conclusion. Except at the top and bottom, gravity has a tangential component, and that component changes the rider's speed. The radial component still curves the path toward the center. Thus "circular" describes the path, whereas "uniform" additionally requires constant speed.

The path is circular, but the speed is not constant. Therefore the motion is not uniform circular motion.

This does not contradict energy conservation. Conservation of mechanical energy allows kinetic energy and potential energy to trade back and forth while their sum stays constant.

```quiz
type: radio
id: p10-q3-uniform
shuffle: true
content: |-
  A rider completes a vertical loop with friction neglected. Which statement correctly describes the motion?
options:
- id: p10q3-a
  content: |-
    The motion is uniform circular motion because every point lies on a circle.
- id: p10q3-b
  content: |-
    The motion is not uniform circular motion because the rider's speed changes with height.
  correct: true
- id: p10q3-c
  content: |-
    The motion is uniform circular motion because mechanical energy is conserved.
- id: p10q3-d
  content: |-
    The motion is not circular motion because gravity acts downward.
```

---

<a id="check-whether-the-centripetal-force-is-constant"></a>
## Check Whether the Centripetal Force Is Constant

**Example:** In the same vertical loop, is the required centripetal force constant in magnitude?

**Explanation**

For circular motion of radius $R$, the required inward net force has magnitude

$$
\sum F_r=m\dfrac{v^2}{R}.
$$

This is not a new extra force. It is the inward part of the net force required to keep the rider moving on the circular path.

The radius and mass stay the same, but the speed does not. The rider moves faster near the bottom and slower near the top.

Since $\sum F_r$ depends on $v^2$, the required inward force is not constant in magnitude.

The direction of the inward force also changes as the rider moves around the loop, because inward always points toward the center.

```quiz
type: radio
id: p10-q4-centripetal-force
shuffle: true
content: |-
  A rider moves through a vertical loop of fixed radius $R$ while speed changes with height. What happens to the required centripetal force magnitude $m\dfrac{v^2}{R}$?
options:
- id: p10q4-a
  content: |-
    It is constant because $R$ is constant.
- id: p10q4-b
  content: |-
    It is constant because the path is circular.
- id: p10q4-c
  content: |-
    It changes because it depends on $v^2$, and $v$ changes.
  correct: true
- id: p10q4-d
  content: |-
    It is zero at every point because mechanical energy is conserved.
```

---

<a id="choose-the-true-statements"></a>
## Choose the True Statements

**Example:** Skateboarder Hony Tawk completes a circular loop-the-loop and never leaves contact with the loop. Neglect rolling friction.

Which statements are true?

A. There exists a minimum speed which Hony needs to be going when entering the loop-the-loop in order to complete it.

B. At the minimum speed, the normal force on Hony goes to zero at the top of the loop.

C. Hony undergoes uniform circular motion while completing the loop-the-loop.

D. The centripetal force on Hony is constant while completing the loop-the-loop.

E. The mechanical energy, kinetic plus potential, of Hony is approximately conserved.

**Explanation**

Check each statement against the matching test:

| Statement | Test | Result |
| --- | --- | --- |
| A | Top contact plus energy requires enough entry speed. | True |
| B | At the threshold, $N=0$ at the top. | True |
| C | Uniform circular motion requires constant speed. | False |
| D | $\sum F_r=m\dfrac{v^2}{R}$ changes when $v$ changes. | False |
| E | With rolling friction neglected, mechanical energy is approximately conserved. | True |

So the true statements are A, B, and E.

```quiz
type: radio
id: p10-q5-original-check
shuffle: true
content: |-
  For Hony's loop-the-loop with rolling friction neglected, which set of statements is true?
options:
- id: p10q5-a
  content: |-
    A, B, and E
  correct: true
- id: p10q5-b
  content: |-
    A, C, and E
- id: p10q5-c
  content: |-
    B, C, and D
- id: p10q5-d
  content: |-
    A, B, C, and D
- id: p10q5-e
  content: |-
    C, D, and E
```

---

## Summary

For a vertical loop-the-loop, use the top of the loop as the contact test:

$$
N+mg=m\dfrac{v_{\text{top}}^2}{R}.
$$

At the minimum speed, $N=0$ at the top. Energy conservation connects the entry speed to that top speed when friction is neglected. Do not confuse a circular path with uniform circular motion: in a vertical loop, speed changes with height, so the required inward force $m\dfrac{v^2}{R}$ also changes.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Finding the Minimum Entry Speed for a Loop-the-Loop](Problem-11.md)

Study guide index: 33/35

---
<!-- lesson-nav:end -->
