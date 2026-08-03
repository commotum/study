# Comparing Descent Times with a Rotating Flywheel

<!--
lesson-id: 212-M3-021
topic-code: MTH212.M3.21
-->

## Table of Contents

- [Introduction](#introduction)
- [Treat Rotation as Added Inertia](#treat-rotation-as-added-inertia)
- [Turn Acceleration into a Time Comparison](#turn-acceleration-into-a-time-comparison)
- [Avoid the Equal-Weight Trap](#avoid-the-equal-weight-trap)
- [Apply the Chain to the Two Flywheels](#apply-the-chain-to-the-two-flywheels)
- [Summary](#summary)

## Prerequisites

- Apply Newton's second law to a translating mass.
- Use $\tau=I\alpha$ and the no-slip relation $a=\alpha r$.
- Use $h=\tfrac12at^2$ for motion from rest with constant acceleration.

---

<a id="introduction"></a>
## Introduction

When a falling block unwinds a cord from a flywheel, gravity must accelerate both the block and any flywheel with rotational inertia. The recognition cue is that two systems have the same falling block and drop distance but different flywheel inertia.

Assume the cord is light and taut, does not slip, and unwinds at a fixed radius $r$. Also assume negligible axle friction. Let $m$ be the block's mass, $I$ the flywheel's moment of inertia, $a$ the block's downward acceleration, and $t$ its descent time.

Use this comparison chain:

$$
\text{larger }I
\quad\Longrightarrow\quad
\text{larger effective inertia }m+\frac{I}{r^2}
\quad\Longrightarrow\quad
\text{smaller }a
\quad\Longrightarrow\quad
\text{larger }t.
$$

The task is to identify which system has greater rotational inertia and carry that direction through the chain.

---

<a id="treat-rotation-as-added-inertia"></a>
## Treat Rotation as Added Inertia

**Example:** A block of mass $m$ descends while turning a flywheel of radius $r$ and moment of inertia $I$. Find the block's acceleration in terms of $m$, $g$, $I$, and $r$.

**Explanation**

For the block,

$$
mg-T=ma.
$$

The cord tension produces the flywheel's torque. Because the cord does not slip,

$$
Tr=I\alpha,
\qquad
\alpha=\frac{a}{r}.
$$

Therefore,

$$
T=\frac{Ia}{r^2}.
$$

Substitute this into the block equation:

$$
mg-\frac{Ia}{r^2}=ma
\qquad\Longrightarrow\qquad
a=\frac{mg}{m+I/r^2}.
$$

The term $I/r^2$ behaves like extra inertia. If $I$ increases while the other quantities stay fixed, the acceleration decreases.

```quiz
type: radio
id: p3-effective-inertia
content: |-
  Two systems use identical falling blocks and flywheel radii. Flywheel X has moment of inertia $I$, while flywheel Y has moment of inertia $2I$. Which block has the larger downward acceleration?
options:
- id: p3-effective-inertia-a
  content: |-
    The block in system X
  correct: true
- id: p3-effective-inertia-b
  content: |-
    The block in system Y
- id: p3-effective-inertia-c
  content: |-
    The accelerations are equal
```

---

<a id="turn-acceleration-into-a-time-comparison"></a>
## Turn Acceleration into a Time Comparison

**Example:** Blocks start from rest and descend the same distance $h$. System 1 has acceleration $a$, while System 2 has acceleration $a/4$. Compare their descent times.

**Explanation**

For constant acceleration from rest,

$$
h=\frac12at^2
\qquad\Longrightarrow\qquad
t=\sqrt{\frac{2h}{a}}.
$$

The time is inversely related to $\sqrt a$. Thus,

$$
t_1=\sqrt{\frac{2h}{a}},
\qquad
t_2=\sqrt{\frac{2h}{a/4}}=2t_1.
$$

The smaller acceleration produces the longer descent time.

Combining the motion equation with the flywheel acceleration gives one direct comparison formula:

$$
t
=\sqrt{\frac{2h}{a}}
=\sqrt{\frac{2h}{g}}\sqrt{1+\frac{I}{mr^2}}.
$$

For otherwise identical systems, the only changing factor is $\sqrt{1+I/(mr^2)}$. A larger $I$ therefore means a larger time.

```quiz
type: radio
id: p3-time-from-acceleration
content: |-
  Two blocks start from rest and descend the same distance. Block P has a greater constant downward acceleration than block Q. Which comparison is correct?
options:
- id: p3-time-from-acceleration-a
  content: |-
    $t_P<t_Q$
  correct: true
- id: p3-time-from-acceleration-b
  content: |-
    $t_P>t_Q$
- id: p3-time-from-acceleration-c
  content: |-
    $t_P=t_Q$
```

---

<a id="avoid-the-equal-weight-trap"></a>
## Avoid the Equal-Weight Trap

**Example:** Two identical blocks fall through the same height. One unwinds a massless flywheel; the other unwinds a flywheel with $I>0$. A student says their accelerations are equal because both blocks have weight $mg$. Find the flaw.

**Explanation**

The blocks have the same weight, but they do not have the same net force. For the massive flywheel, a nonzero cord tension is needed to create angular acceleration:

$$
T=\frac{Ia}{r^2}>0.
$$

That tension pulls upward on the block, so

$$
F_{\text{net}}=mg-T<mg.
$$

For the negligible-mass flywheel, $I\approx0$, so the idealized tension needed to spin it is negligible and $a\approx g$. Equal driving weights do not imply equal accelerations when one system must also accelerate a rotating object.

```quiz
type: radio
id: p3-equal-weight-trap
content: |-
  Why does the block attached to a flywheel with $I>0$ accelerate at less than $g$ in this ideal model?
options:
- id: p3-equal-weight-trap-a
  content: |-
    Cord tension supplies torque to the flywheel and reduces the block's net downward force.
  correct: true
- id: p3-equal-weight-trap-b
  content: |-
    The block's weight becomes smaller as the flywheel rotates.
- id: p3-equal-weight-trap-c
  content: |-
    The flywheel increases the downward tension on the block.
- id: p3-equal-weight-trap-d
  content: |-
    The two systems must have equal acceleration because their blocks have equal mass.
```

---

<a id="apply-the-chain-to-the-two-flywheels"></a>
## Apply the Chain to the Two Flywheels

**Example:** System A has a flywheel whose mass is negligible, while otherwise identical System B has a flywheel of mass $M$. Compare the time required for each block to move downward through the same distance $h$.

**Explanation**

The negligible-mass flywheel has $I_A\approx0$, while the flywheel of mass $M$ has $I_B>0$. Therefore,

$$
m+\frac{I_B}{r^2}>m+\frac{I_A}{r^2},
$$

so $a_B<a_A$. Equivalently, the factor $\sqrt{1+I/(mr^2)}$ is larger in System B. Thus $t_B>t_A$, and the block in System A reaches the bottom first.

```quiz
type: radio
id: p3-assignment-check
content: |-
  A block is attached to a cord wrapped around a flywheel. System A has a flywheel whose mass is negligible, while System B has a flywheel of mass $M$. The systems are otherwise identical.

  Compare the time required for each block to move downward through a distance $h$.

  ![](<../Source/2026-07-19-PQ-2/Images/problem-3-flywheel-comparison.png>)
options:
- id: p3-assignment-check-a
  content: |-
    The block in System A moves through $h$ in less time than the block in System B.
  correct: true
- id: p3-assignment-check-b
  content: |-
    The block in System A moves through $h$ in more time than the block in System B.
- id: p3-assignment-check-c
  content: |-
    The blocks move through $h$ in the same amount of time.
```

---

<a id="summary"></a>
## Summary

When otherwise identical falling-block systems differ only in flywheel inertia:

1. Identify the flywheel with larger $I$.
2. Treat $I/r^2$ as added inertia in $a=mg/(m+I/r^2)$.
3. Conclude that larger $I$ gives smaller $a$.
4. Use $t=\sqrt{2h/g}\sqrt{1+I/(mr^2)}$ to conclude that larger $I$ gives longer time.

The main trap is comparing only the equal block weights. The massive flywheel requires torque, so cord tension reduces that block's net downward force.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Finding the Tipping Threshold With Torque Balance](Problem-4.md)

Study guide index: 07/20

---
<!-- lesson-nav:end -->
