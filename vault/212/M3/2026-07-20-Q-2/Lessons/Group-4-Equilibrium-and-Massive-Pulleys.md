# Solve Coupled Equilibrium and Massive-Pulley Systems

<!--
lesson-id: 212-M3-027
topic-code: MTH212.M3.27
-->

## Table of Contents

- [Introduction](#introduction)
- [Use Both Force and Torque Balance](#use-both-force-and-torque-balance)
- [Recognize the Tipping Threshold](#recognize-the-tipping-threshold)
- [Choose a Pivot for a Ladder](#choose-a-pivot-for-a-ladder)
- [Separate the Tensions of a Massive Pulley](#separate-the-tensions-of-a-massive-pulley)
- [Connect Translation and Rotation](#connect-translation-and-rotation)
- [Check Limiting Cases](#check-limiting-cases)
- [Summary](#summary)

## Prerequisites

- Draw point and extended free-body diagrams.
- Calculate signed torques about a chosen pivot.
- Use $\sum\vec F=m\vec a$ and $\sum\tau=I\alpha$.
- Use the no-slip relation $a=\alpha r$.

---

<a id="introduction"></a>
## Introduction

Equilibrium and massive-pulley problems both require equations from more than one motion channel.

For static equilibrium,

$$
\sum\vec F=0,\qquad \sum\tau=0.
$$

For coupled translation and rotation,

$$
\sum\vec F=m\vec a,\qquad \sum\tau=I\alpha,\qquad a=\alpha r.
$$

The governing move is to isolate each body, write the equation appropriate to that body, and then connect the equations through contact forces or kinematic constraints.

**Recognition cue:** “At rest,” “just begins to tip,” and “threshold of slipping” lead to force and torque balance. A massive pulley that accelerates requires separate block equations, a pulley torque equation, and the no-slip relation.

---

<a id="use-both-force-and-torque-balance"></a>
## Use Both Force and Torque Balance

**Example:** A stationary uniform board rests on two supports and carries a box. What equations describe its static equilibrium?

**Explanation**

Zero net force prevents translational acceleration:

$$
\sum F_x=0,\qquad \sum F_y=0.
$$

Zero net torque prevents angular acceleration:

$$
\sum\tau=0.
$$

Neither condition replaces the other. A body can have zero net force but a nonzero torque, or zero net torque but a nonzero net force.

Choose a pivot that makes inconvenient unknown forces pass through the pivot. Those forces then have zero moment arm and disappear from the torque equation.

```quiz
type: radio
id: equilibrium-pulley-q1
shuffle: true
content: |-
  Which conditions must a rigid body satisfy to remain in static equilibrium?
options:
- id: equilibrium-pulley-q1-a
  content: |-
    Only $\sum\vec F=0$
- id: equilibrium-pulley-q1-b
  content: |-
    Only $\sum\tau=0$
- id: equilibrium-pulley-q1-c
  content: |-
    Both $\sum\vec F=0$ and $\sum\tau=0$
  correct: true
  feedback: |-
    The first prevents translation; the second prevents rotation.
- id: equilibrium-pulley-q1-d
  content: |-
    $\sum\vec F=\sum\tau$
```

---

<a id="recognize-the-tipping-threshold"></a>
## Recognize the Tipping Threshold

**Example:** A uniform plank of mass $M$ rests on supports $A$ and $B$. Its center of mass lies a distance $L/6$ to the left of $B$. A box of mass $m$ is placed a distance $x$ to the right of $B$. Find $x$ when the plank just begins to tip.

**Explanation**

At the tipping threshold, the plank is about to rotate around support $B$. It has just lost contact with support $A$, so

$$
N_A=0.
$$

Use $B$ as the pivot. The remaining support force acts at the pivot and creates no torque. Balance the box and plank torques:

$$
mgx=Mg\frac{L}{6}.
$$

Therefore,

$$
x_{\max}=\frac{ML}{6m}.
$$

The cue “just begins to tip” always means that one contact force has fallen to zero and the other contact point becomes the pivot.

```quiz
type: radio
id: equilibrium-pulley-q2
shuffle: true
content: |-
  A uniform board of mass $M$ is about to tip around support B. Its center of mass is $L/4$ to the left of B, and a box of mass $m$ is $x$ to the right of B. What is the largest allowed $x$?
options:
- id: equilibrium-pulley-q2-a
  content: |-
    $\dfrac{mL}{4M}$
- id: equilibrium-pulley-q2-b
  content: |-
    $\dfrac{ML}{4m}$
  correct: true
  feedback: |-
    Set $mgx=Mg(L/4)$.
- id: equilibrium-pulley-q2-c
  content: |-
    $\dfrac{ML}{2m}$
- id: equilibrium-pulley-q2-d
  content: |-
    $\dfrac{(M+m)L}{4m}$
  feedback: |-
    The box's own weight already appears in its torque and should not be added to the board mass.
```

---

<a id="choose-a-pivot-for-a-ladder"></a>
## Choose a Pivot for a Ladder

**Example:** A uniform ladder of mass $m$ and length $L$ leans at angle $\theta$ against a frictionless wall. The floor is rough, and the ladder is just about to slip. Find the required $\mu_s$.

**Explanation**

At the floor,

$$
N_F=mg,\qquad f_s=\mu_sN_F=\mu_smg.
$$

Horizontal balance gives $N_W=f_s$. Choose the bottom of the ladder as the pivot so $N_F$ and $f_s$ produce no torque. Then

$$
N_WL\sin\theta=mg\frac{L}{2}\cos\theta.
$$

Substitute $N_W=\mu_smg$ and cancel $mgL$:

$$
\mu_s\sin\theta=\frac12\cos\theta.
$$

Therefore,

$$
\mu_s=\frac{1}{2\tan\theta}.
$$

This formula assumes a uniform ladder, a frictionless wall, and impending slip at the floor.

```quiz
type: radio
id: equilibrium-pulley-q3
shuffle: true
content: |-
  A uniform ladder rests against a frictionless wall at $\theta=45^\circ$ and is at the threshold of slipping. What minimum coefficient of static friction is required at the floor?
options:
- id: equilibrium-pulley-q3-a
  content: |-
    $1/4$
- id: equilibrium-pulley-q3-b
  content: |-
    $1/2$
  correct: true
  feedback: |-
    $\mu_s=1/(2\tan45^\circ)=1/2$.
- id: equilibrium-pulley-q3-c
  content: |-
    $1$
- id: equilibrium-pulley-q3-d
  content: |-
    $2$
```

---

<a id="separate-the-tensions-of-a-massive-pulley"></a>
## Separate the Tensions of a Massive Pulley

**Example:** Masses $m_1<m_2$ hang on opposite sides of a massive pulley. The heavier mass moves down with acceleration magnitude $a$. Write the force equations.

**Explanation**

Choose positive along each mass's motion. For $m_1$, which moves upward,

$$
T_1-m_1g=m_1a.
$$

For $m_2$, which moves downward,

$$
m_2g-T_2=m_2a.
$$

Because the pulley must accelerate rotationally, the tensions cannot be equal. Their difference supplies net torque:

$$
(T_2-T_1)r=I\alpha.
$$

For this motion, $T_2>T_1$. Assuming $T_1=T_2$ would force the pulley torque to zero.

```quiz
type: radio
id: equilibrium-pulley-q4
shuffle: true
content: |-
  In an Atwood machine with a massive pulley, $m_2>m_1$ and $m_2$ accelerates downward. Which tension relation is correct?
options:
- id: equilibrium-pulley-q4-a
  content: |-
    $T_1=T_2$
  feedback: |-
    Equal tensions would produce no net pulley torque.
- id: equilibrium-pulley-q4-b
  content: |-
    $T_1>T_2$
- id: equilibrium-pulley-q4-c
  content: |-
    $T_2>T_1$
  correct: true
  feedback: |-
    The torque $(T_2-T_1)r$ accelerates the pulley in the direction of $m_2$'s descent.
- id: equilibrium-pulley-q4-d
  content: |-
    Both tensions must equal $m_2g$.
```

---

<a id="connect-translation-and-rotation"></a>
## Connect Translation and Rotation

**Example:** The pulley has radius $r$ and moment of inertia $I$. Find the acceleration of the two-mass system.

**Explanation**

No slipping gives

$$
a=\alpha r
\quad\Rightarrow\quad
\alpha=\frac{a}{r}.
$$

Substitute this into the torque equation:

$$
T_2-T_1=\frac{I}{r^2}a.
$$

Keep the substitution order visible:

1. Solve each block equation for its own tension.
2. Replace $\alpha$ by $a/r$ in the pulley equation.
3. Substitute both tensions into that pulley equation.

Using

$$
T_1=m_1g+m_1a,\qquad T_2=m_2g-m_2a,
$$

gives

$$
(m_2-m_1)g
=
\left(m_1+m_2+\frac{I}{r^2}\right)a.
$$

Thus,

$$
a=\frac{(m_2-m_1)g}{m_1+m_2+I/r^2}.
$$

The term $I/r^2$ acts like extra inertial mass. For a solid-disk pulley, $I/r^2=M_p/2$.

```quiz
type: radio
id: equilibrium-pulley-q5
shuffle: true
content: |-
  An Atwood machine has $m_1=m$, $m_2=3m$, and a solid-disk pulley of mass $M_p=2m$. What is the acceleration magnitude?
options:
- id: equilibrium-pulley-q5-a
  content: |-
    $\dfrac{g}{5}$
- id: equilibrium-pulley-q5-b
  content: |-
    $\dfrac{2g}{5}$
  correct: true
  feedback: |-
    The numerator is $2mg$; the denominator is $m+3m+M_p/2=5m$.
- id: equilibrium-pulley-q5-c
  content: |-
    $\dfrac{g}{2}$
  feedback: |-
    This is the massless-pulley result and ignores rotational inertia.
- id: equilibrium-pulley-q5-d
  content: |-
    $\dfrac{2g}{3}$
```

---

<a id="check-limiting-cases"></a>
## Check Limiting Cases

**Example:** What happens to the Atwood acceleration as the pulley inertia approaches zero?

**Explanation**

Start from

$$
a=\frac{(m_2-m_1)g}{m_1+m_2+I/r^2}.
$$

If $I\to0$,

$$
a\to\frac{(m_2-m_1)g}{m_1+m_2},
$$

the massless-pulley result. Increasing $I$ makes the denominator larger and the acceleration smaller because some of the available energy goes into rotational motion.

The same reasoning applies to a falling block attached to a flywheel: a flywheel with appreciable $I$ makes the block descend more slowly than a negligible-mass flywheel.

```quiz
type: radio
id: equilibrium-pulley-q6
shuffle: true
content: |-
  Two otherwise identical falling-block systems use flywheels with $I_A<I_B$. The cord does not slip. Which block has the greater acceleration magnitude?
options:
- id: equilibrium-pulley-q6-a
  content: |-
    The block connected to flywheel A
  correct: true
  feedback: |-
    Less rotational inertia leaves a larger acceleration for the translating block.
- id: equilibrium-pulley-q6-b
  content: |-
    The block connected to flywheel B
- id: equilibrium-pulley-q6-c
  content: |-
    Their accelerations are equal because the blocks are identical.
- id: equilibrium-pulley-q6-d
  content: |-
    The answer depends only on the flywheel radii, never on $I$.
```

---

<a id="summary"></a>
## Summary

For static systems:

1. Draw an extended free-body diagram.
2. Require both $\sum\vec F=0$ and $\sum\tau=0$.
3. At impending tip, set the lost support force to zero and pivot about the remaining contact.
4. At impending slip, use $f_s=\mu_sN$.

For massive pulleys:

1. Draw a separate free-body diagram for each translating mass.
2. Keep the two tensions distinct.
3. Write $(T_2-T_1)r=I\alpha$ for the pulley.
4. Connect the motions with $a=\alpha r$.
5. Check the $I\to0$ limit and whether increasing $I$ correctly reduces $a$.

The main trap is trying to solve the entire coupled system with only a force equation or only a torque equation.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
