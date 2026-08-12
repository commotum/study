# Recognizing Contact Loss on a Curved Surface

<!--
lesson-id: 212-M1-020
topic-code: MTH212.M1.20
-->

## Table of Contents

- [Introduction](#introduction)
- [Use Zero Normal Force as the Contact-Loss Test](#use-zero-normal-force-as-the-contact-loss-test)
- [Keep Radial Acceleration Separate from the Normal Force](#keep-radial-acceleration-separate-from-the-normal-force)
- [Separate Radial and Tangential Acceleration](#separate-radial-and-tangential-acceleration)
- [Reject Uniform Circular Motion When Speed Changes](#reject-uniform-circular-motion-when-speed-changes)
- [Test the Four Claims](#test-the-four-claims)
- [Summary](#summary)

## Prerequisites

- Use $a_r=\dfrac{v^2}{r}$ for motion along a circular path of radius $r$.
- Recognize that a normal force is a contact force that can push but cannot pull.
- Separate radial acceleration from tangential acceleration.
- Know that uniform circular motion means circular motion at constant speed.

---

<a id="introduction"></a>
## Introduction

A penguin starts from rest and slides on its belly down the right side of a spherical igloo of radius $r$. There is no friction. At some angle $\theta_c$ from the vertical, the penguin leaves the surface. What is true in the instant just before contact is lost?

![](<../Source/Images/igloo-slide-diagram.png>)

Losing contact does not mean that the penguin stops moving or stops curving at that instant. It means the igloo can no longer push on the penguin. The normal force therefore falls to zero while gravity still supplies an inward component of force and a tangential component that changes the penguin's speed.

Contact with an ordinary surface is possible only while

$$
N\ge 0.
$$

The leaving point is the boundary case

$$
N=0.
$$

The condition $N=0$ does not imply $v^2/r=0$. The normal force is one term in the radial force balance, not another name for the radial acceleration.

---

<a id="use-zero-normal-force-as-the-contact-loss-test"></a>
## Use Zero Normal Force as the Contact-Loss Test

**Example:** A small block slides on the outside of a smooth circular dome. At some point it is just about to leave the surface. What must be true about the normal force at that instant?

**Explanation**

The normal force exists only while the surface is pushing on the object. A surface can push perpendicular to itself, but it cannot pull the object back toward itself after contact is lost.

So the boundary between "still in contact" and "not in contact" is

$$
N=0.
$$

If a force equation would require $N<0$, that would mean the surface would have to pull on the object. Since the surface cannot pull, the object has already left the surface instead.

Just before losing contact, the normal force has become negligible. It is not large, and it is not equal to the weight in general.

```quiz
type: radio
id: p12-q1-contact-loss
shuffle: true
content: |-
  A sled slides on the outside of a frictionless circular hill and is just about to leave the surface. Which statement best describes the normal force at that instant?
options:
- id: p12q1-a
  content: |-
    $N=0$ or negligibly small.
  correct: true
- id: p12q1-b
  content: |-
    $N=mg$ because the sled is still near the hill.
- id: p12q1-c
  content: |-
    $N$ must point inward and supply all of the centripetal force.
- id: p12q1-d
  content: |-
    $N$ becomes negative so the hill can pull the sled inward.
```

---

<a id="keep-radial-acceleration-separate-from-the-normal-force"></a>
## Keep Radial Acceleration Separate from the Normal Force

**Example:** A puck is still moving along a circular dome at speed $v$ at the instant when $N=0$. Is the inward, or centripetal, acceleration zero?

**Explanation**

If the puck is still following the circular surface at that instant, its radial acceleration is

$$
a_r=\dfrac{v^2}{r}.
$$

That acceleration is not zero unless $v=0$. For an object sliding down from rest, the speed has increased by the time it leaves the surface, so $v>0$.

The normal force being zero does not mean the inward net force is zero. At the contact-loss instant, the inward component of gravity supplies the required radial net force:

$$
mg\cos\theta=m\dfrac{v^2}{r}.
$$

One way to see that is to write the radial equation while the object is still in contact on the outside of the dome:

$$
mg\cos\theta-N=m\dfrac{v^2}{r}.
$$

The normal force appears with a minus sign because it pushes outward, away from the center of the dome. At the instant of losing contact, set $N=0$ in that same radial equation.

The common trap is treating "centripetal force" as if it must be a separate contact force. It is better to read $m\dfrac{v^2}{r}$ as the inward net force required by the circular path.

```quiz
type: radio
id: p12-q2-radial-acceleration
shuffle: true
content: |-
  A bead slides on the outside of a frictionless circular track. At the instant the normal force becomes zero, the bead is still moving with speed $v>0$ along a path of radius $r$. Which statement is correct?
options:
- id: p12q2-a
  content: |-
    The radial acceleration is zero because $N=0$.
- id: p12q2-b
  content: |-
    The radial acceleration is $\dfrac{v^2}{r}$, supplied by the inward component of the net force.
  correct: true
- id: p12q2-c
  content: |-
    The radial acceleration must point tangent to the track.
- id: p12q2-d
  content: |-
    The radial acceleration is $g$ at every point on the track.
```

---

<a id="separate-radial-and-tangential-acceleration"></a>
## Separate Radial and Tangential Acceleration

**Example:** A penguin slides down the side of a smooth igloo at an angle $\theta$ from the vertical. Just before leaving the surface, what directions can its acceleration have?

**Explanation**

While the penguin is still following the spherical surface, its acceleration can be split into two perpendicular parts:

- a radial part, pointing toward the center of the igloo, with magnitude $\dfrac{v^2}{r}$;
- a tangential part, pointing down along the surface, caused by the tangential component of gravity.

At the contact-loss instant, $N=0$, but the penguin still has speed and is still curving with the surface for that instant. So the acceleration is not purely tangential.

The tangential part changes the speed. The radial part changes the direction of the velocity.

The $r$-$t$ axes rotate with the penguin: $+\hat r$ keeps pointing toward the current center, and $\hat t$ stays tangent to the surface. The word *instant* is also important. Losing the contact constraint changes the force set, but it does not make position or velocity jump; the penguin retains its tangent velocity as $N$ reaches zero. Thus, $N=0$ cannot be used as evidence that either the speed or radial acceleration was already zero just before release.

```quiz
type: radio
id: p12-q3-acceleration-components
shuffle: true
content: |-
  Just before an object leaves a frictionless circular dome, it is still moving along the curved surface with nonzero speed. Which description of its acceleration is best?
options:
- id: p12q3-a
  content: |-
    It is purely tangential because the normal force is zero.
- id: p12q3-b
  content: |-
    It has a radial part toward the center and may also have a tangential part along the surface.
  correct: true
- id: p12q3-c
  content: |-
    It is zero because contact is about to be lost.
- id: p12q3-d
  content: |-
    It points outward because the object is leaving the surface.
```

---

<a id="reject-uniform-circular-motion-when-speed-changes"></a>
## Reject Uniform Circular Motion When Speed Changes

**Example:** A block starts from rest and slides without friction down the outside of a sphere. Before it leaves the surface, is it undergoing uniform circular motion?

**Explanation**

Uniform circular motion requires two things:

- the path is circular;
- the speed is constant.

The block does move along a circular arc while it remains in contact with the sphere. But it starts from rest and speeds up as gravity pulls it downward. With friction neglected, gravitational potential energy is converted into kinetic energy.

So the motion is circular for a while, but it is not uniform circular motion.

```quiz
type: radio
id: p12-q4-uniform-circular-motion
shuffle: true
content: |-
  A penguin starts from rest and slides without friction down the outside of a spherical igloo. Before leaving the igloo, why is the motion not uniform circular motion?
options:
- id: p12q4-a
  content: |-
    Because the path is not curved.
- id: p12q4-b
  content: |-
    Because the penguin's speed changes as it slides downward.
  correct: true
- id: p12q4-c
  content: |-
    Because uniform circular motion requires zero acceleration.
- id: p12q4-d
  content: |-
    Because uniform circular motion can happen only on a flat surface.
```

---

<a id="test-the-four-claims"></a>
## Test the Four Claims

**Example:** Compare the four claims in the penguin question.

**Explanation**

Check each statement against the contact-loss test.

| Statement | Test | Result |
| --- | --- | --- |
| A | Losing contact means the surface's push has dropped to zero. | True |
| B | The penguin still has nonzero speed and needs radial acceleration $\dfrac{v^2}{r}$. | False |
| C | The acceleration still has a radial part just before contact is lost. | False |
| D | The penguin speeds up while sliding down from rest. | False |

Only statement A survives all four checks: the igloo's normal force has fallen to zero.

```quiz
type: radio
id: p12-q5-original-check
shuffle: true
content: |-
  Starting from rest, a penguin slides without friction down the outside of a spherical igloo and loses contact at an angle $\theta_c$ from the vertical. Which statement is true just before contact is lost?
options:
- id: p12q5-a
  content: |-
    The normal force from the igloo is negligible or zero.
  correct: true
- id: p12q5-b
  content: |-
    The required inward net force $m\dfrac{v^2}{r}$ is negligible or zero.
- id: p12q5-c
  content: |-
    The penguin's acceleration is purely tangential to the surface.
- id: p12q5-d
  content: |-
    The penguin had been undergoing uniform circular motion before this instant.
```

---

## Summary

For an object leaving the outside of a curved surface, contact ends when the surface's normal force falls to zero:

$$
N=0.
$$

Just before the object leaves, it can still have nonzero speed, so its radial acceleration remains $v^2/r$. At the instant the normal force vanishes, the inward component of gravity supplies the required inward force. Because gravity also changes the object's speed as it descends, the motion is neither purely tangentially accelerated nor uniform circular motion.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Choosing a Free-Body Diagram for an Icy Banked Curve](../../2026-06-30-M1-4/Lessons/Problem-1.md)

Study guide index: 21/35

---
<!-- lesson-nav:end -->
