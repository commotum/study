# Deciding True Statements About Static Friction on a Banked Turn

<!--
lesson-id: 212-M1-025
topic-code: MTH212.M1.25
-->

## Table of Contents

- [Introduction](#introduction)
- [Point the Acceleration Inward](#point-the-acceleration-inward)
- [Find the Speed That Needs No Friction](#find-the-speed-that-needs-no-friction)
- [Use Speed to Choose the Friction Direction](#use-speed-to-choose-the-friction-direction)
- [Connect Friction Magnitude to Speed Limits](#connect-friction-magnitude-to-speed-limits)
- [Check the Problem Statements](#check-the-problem-statements)
- [Summary](#summary)

## Prerequisites

- Use $a_c=\dfrac{v^2}{r}$ for circular motion.
- Resolve forces on a banked track into vertical and inward components.
- Know that static friction can point either way along a surface.
- Know that static friction has a maximum possible magnitude.

---

<a id="introduction"></a>
## Introduction

The cue in this problem is a banked circular track with static friction, followed by several true/false statements. The useful move is to evaluate each statement by separating the acceleration direction from the force components, then comparing the car's speed with the speed that would need no static friction.

For a car moving around a horizontal circle at constant speed, the acceleration points horizontally inward, toward the center of the circle:

$$
a_c=\dfrac{v^2}{r}.
$$

The bank angle helps the normal force provide some inward force. Static friction supplies whatever extra along-track force is needed, up to its maximum possible size.

![](<../Source/Images/banked-track-car-diagram.png>)

Use three checks:

1. Acceleration points inward.
2. $v_0=\sqrt{rg\tan\theta}$ is the speed that needs no friction.
3. Compare $v$ with $v_0$ to decide friction direction and size.

The main trap is treating static friction as if its direction is fixed. Static friction points whichever way prevents slipping, so its direction and magnitude can change when $v$ changes.

---

<a id="point-the-acceleration-inward"></a>
## Point the Acceleration Inward

**Example:** A car moves at constant speed around a circular track of radius $r$. In the side view, the center of the circle is directly to the left of the car. Which way does the car's acceleration point?

**Explanation**

The car is moving in a circle, so its acceleration is centripetal:

$$
\vec a=\vec a_c.
$$

Centripetal acceleration always points toward the center of the circular path. In this side view, the center is horizontally to the left, so the acceleration points directly left.

The acceleration does not point down the ramp. Forces can have components along the ramp, but the net acceleration for this constant-height circular motion is horizontal and inward.

```quiz
type: radio
id: p9-q1-acceleration
shuffle: true
content: |-
  A car moves at constant speed around a banked circular track. In the side view, the center of the circular path is directly to the left of the car. Which statement best describes the acceleration?
options:
- id: p9-q1-a
  content: |-
    It points directly to the left.
  correct: true
- id: p9-q1-b
  content: |-
    It points down the ramp.
- id: p9-q1-c
  content: |-
    It points up the ramp.
- id: p9-q1-d
  content: |-
    It points vertically upward.
```

---

<a id="find-the-speed-that-needs-no-friction"></a>
## Find the Speed That Needs No Friction

**Example:** A car moves around a frictionless banked curve of angle $\theta$ and radius $r$. Find the speed $v_0$ that lets the car maintain the circular path with no static friction.

**Explanation**

With no friction, the only contact force is the normal force $n$. Since the track is banked by angle $\theta$ from the horizontal, the normal force has components

$$
n\cos\theta \quad \text{vertical}
$$

and

$$
n\sin\theta \quad \text{inward}.
$$

The vertical acceleration is zero, so the vertical forces balance:

$$
n\cos\theta=mg.
$$

The inward component supplies the centripetal force:

$$
n\sin\theta=\dfrac{mv_0^2}{r}.
$$

Divide the inward equation by the vertical equation:

$$
\dfrac{n\sin\theta}{n\cos\theta}
=
\dfrac{mv_0^2/r}{mg}.
$$

So

$$
\tan\theta=\dfrac{v_0^2}{rg}.
$$

Therefore

$$
v_0=\sqrt{rg\tan\theta}.
$$

At exactly this speed, the normal force alone gives the needed inward force, so static friction is zero.

```quiz
type: radio
id: p9-q2-no-friction-speed
shuffle: true
content: |-
  A car moves around a banked circular track of radius $r$ and bank angle $\theta$. Which speed makes static friction unnecessary?
options:
- id: p9-q2-a
  content: |-
    $\sqrt{rg\tan\theta}$
  correct: true
- id: p9-q2-b
  content: |-
    $\sqrt{\dfrac{rg}{\tan\theta}}$
- id: p9-q2-c
  content: |-
    $\sqrt{rg\sin\theta}$
- id: p9-q2-d
  content: |-
    $\sqrt{\dfrac{g\tan\theta}{r}}$
```

---

<a id="use-speed-to-choose-the-friction-direction"></a>
## Use Speed to Choose the Friction Direction

**Example:** Let

$$
v_0=\sqrt{rg\tan\theta}.
$$

If the car's speed is greater than $v_0$, which way must static friction point?

**Explanation**

The required inward force is

$$
\dfrac{mv^2}{r}.
$$

When $v$ is greater than $v_0$, the required inward force is larger than the inward component of the normal force alone. Static friction must add more inward force.

On the banked track, friction down the ramp has an inward component. So for $v>v_0$, static friction points down the ramp.

For comparison:

| Speed comparison | What static friction does |
| --- | --- |
| $v<v_0$ | points up the ramp |
| $v=v_0$ | is zero |
| $v>v_0$ | points down the ramp |

That is why the direction of static friction depends on $v$.

```quiz
type: radio
id: p9-q3-friction-direction
shuffle: true
content: |-
  A car is on a banked circular track. The no-friction speed is $v_0=\sqrt{rg\tan\theta}$. Which comparison correctly describes the direction of static friction?
options:
- id: p9-q3-a
  content: |-
    If $v<v_0$, friction points up the ramp; if $v=v_0$, friction is zero; if $v>v_0$, friction points down the ramp.
  correct: true
- id: p9-q3-b
  content: |-
    If $v<v_0$, friction points down the ramp; if $v=v_0$, friction is zero; if $v>v_0$, friction points up the ramp.
- id: p9-q3-c
  content: |-
    Friction always points up the ramp, but its magnitude changes with $v$.
- id: p9-q3-d
  content: |-
    There is no static friction whenever the car moves in a circle.
```

---

<a id="connect-friction-magnitude-to-speed-limits"></a>
## Connect Friction Magnitude to Speed Limits

**Example:** Explain why the magnitude of static friction on a banked turn depends on the car's speed.

**Explanation**

The needed inward net force is

$$
\dfrac{mv^2}{r}.
$$

As $v$ changes, this required inward force changes. The normal force and static friction must combine to make the inward net force equal to $\dfrac{mv^2}{r}$ while still giving zero vertical acceleration.

If we choose "up the ramp" as the positive direction for friction, the force equations lead to

$$
f_s=mg\sin\theta-\dfrac{mv^2}{r}\cos\theta.
$$

This signed value changes with $v$:

- positive means friction points up the ramp;
- zero means no friction is needed;
- negative means friction points down the ramp.

The physical magnitude is $|f_s|$, so the magnitude also depends on $v$.

Static friction is limited by a maximum possible value. If the car is too fast, the required down-ramp friction becomes too large, and the car cannot maintain the circular path of radius $r$. That gives a maximum allowable speed.

```quiz
type: radio
id: p9-q4-friction-magnitude
shuffle: true
content: |-
  Why does the magnitude of the static friction force on a banked turn depend on $v$?
options:
- id: p9-q4-a
  content: |-
    Because the required centripetal force is $\dfrac{mv^2}{r}$, which changes when $v$ changes.
  correct: true
- id: p9-q4-b
  content: |-
    Because the weight $mg$ changes when $v$ changes.
- id: p9-q4-c
  content: |-
    Because the bank angle $\theta$ must change when $v$ changes.
- id: p9-q4-d
  content: |-
    Because static friction always has the same magnitude as the normal force.
```

---

<a id="check-the-problem-statements"></a>
## Check the Problem Statements

**Example:** The original problem asks which statements are true for a car of mass $m$ moving at constant speed $v$ around a banked circular track of radius $r$ and bank angle $\theta$.

**Explanation**

Use the same checks one statement at a time.

Statement A is true: the static friction direction depends on whether $v$ is below, equal to, or above $\sqrt{rg\tan\theta}$.

Statement B is true: the magnitude depends on $v$ because the required inward force is $\dfrac{mv^2}{r}$.

Statement C is true: static friction has a maximum possible size, so there is a maximum speed above which the car cannot hold the same circular path.

Statement D is true: in the side view, the acceleration points horizontally inward, directly to the left.

Statement E is false: the acceleration does not point down the ramp.

Statement F is true: when

$$
v=\sqrt{gr\tan\theta},
$$

which is the same as $\sqrt{rg\tan\theta}$, no static friction is needed.

```quiz
type: radio
id: p9-q5-problem-statements
shuffle: true
content: |-
  For the banked-track scenario in Problem 9, which group of statements is true?

  A. The direction of static friction depends on $v$.
  B. The magnitude of static friction depends on $v$.
  C. There is a maximum speed above which the car cannot maintain the circular path.
  D. In the side view, the acceleration points directly left.
  E. In the side view, the acceleration points down the ramp.
  F. If $v=\sqrt{gr\tan\theta}$, no static friction is needed.
options:
- id: p9-q5-a
  content: |-
    A, B, C, D, and F only
  correct: true
- id: p9-q5-b
  content: |-
    A, B, and D only
- id: p9-q5-c
  content: |-
    A, C, E, and F only
- id: p9-q5-d
  content: |-
    B, C, and D only
- id: p9-q5-e
  content: |-
    A, B, C, D, E, and F
```

---

## Summary

For a banked turn with static friction, start with the acceleration: it points horizontally inward, not along the ramp. Then find the no-friction speed from the normal-force equations:

$$
v_0=\sqrt{rg\tan\theta}.
$$

Compare $v$ with $v_0$. Below $v_0$, friction points up the ramp; at $v_0$, friction is zero; above $v_0$, friction points down the ramp. Since the required centripetal force is $\dfrac{mv^2}{r}$, both the direction and magnitude of static friction can depend on speed. The main trap is choosing a ramp direction for acceleration instead of the inward direction toward the circle's center.

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<Study-Guide.md>)

Next: [Choosing a Free-Body Diagram for a Conical Pendulum](<../../2026-06-30-M1-4/Lessons/Problem-7.md>)

Study guide index: 25/30

<!-- study-guide-nav:end -->
