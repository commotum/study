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
- [Choose the True Igloo Statement](#choose-the-true-igloo-statement)
- [Summary](#summary)

## Prerequisites

- Use $a_r=\dfrac{v^2}{r}$ for motion along a circular path of radius $r$.
- Recognize that a normal force is a contact force that can push but cannot pull.
- Separate radial acceleration from tangential acceleration.
- Know that uniform circular motion means circular motion at constant speed.

---

<a id="introduction"></a>
## Introduction

When an object slides on the outside of a curved surface, the cue "loses contact" means the surface has stopped pushing on the object. The useful move is to identify the contact-loss condition by setting the normal force to zero, while still keeping the inward acceleration needed for circular motion.

The short test is:

$$
\text{contact is possible only while } N\ge 0,
$$

so the leaving point is the boundary case

$$
N=0.
$$

Watch out: $N=0$ does not mean $\dfrac{v^2}{r}=0$. The normal force is one possible contributor to the radial force balance, not the radial acceleration itself.

For the penguin sliding down a frictionless spherical igloo, the true statement just before losing contact is that the normal force from the igloo is negligible or zero.

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

```quiz
type: radio
id: p12-q3-acceleration-components
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

<a id="choose-the-true-igloo-statement"></a>
## Choose the True Igloo Statement

**Example:** Starting from rest, a penguin lying on its belly slides down the right side of a spherical igloo of radius $r$.

Neglecting friction, the penguin will slide off and, at some angle $\theta_c$ from the vertical, eventually lose contact with the igloo.

Which statement is true about the penguin the instant before losing contact with the igloo?

![](<../Source/Images/igloo-slide-diagram.png>)

A. The normal force on the penguin from the igloo is negligible/zero.

B. The centripetal force on the penguin is negligible/zero.

C. The penguin's acceleration was directed tangentially to the igloo's surface.

D. Prior to this instant, the penguin had been undergoing uniform circular motion.

**Explanation**

Check each statement against the contact-loss test.

| Statement | Test | Result |
| --- | --- | --- |
| A | Losing contact means the surface's push has dropped to zero. | True |
| B | The penguin still has nonzero speed and needs radial acceleration $\dfrac{v^2}{r}$. | False |
| C | The acceleration still has a radial part just before contact is lost. | False |
| D | The penguin speeds up while sliding down from rest. | False |

So the true statement is A.

```quiz
type: radio
id: p12-q5-original-check
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

For an object sliding on the outside of a curved surface, the phrase "loses contact" is a normal-force test:

$$
N=0.
$$

That does not make the radial acceleration zero. Just before the object leaves, it can still have speed, so the inward net force is still $m\dfrac{v^2}{r}$. The main traps are confusing the normal force with the whole inward net force, calling the acceleration purely tangential, or assuming that any circular path is uniform circular motion.

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Choosing a Free-Body Diagram for an Icy Banked Curve](<../../2026-06-30-M1-4/Lessons/Problem-1.md>)

Study guide index: 20/30

<!-- study-guide-nav:end -->
