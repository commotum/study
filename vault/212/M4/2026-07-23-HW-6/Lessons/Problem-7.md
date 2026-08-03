# Speed of a Spring Oscillator at a Given Position

<!--
lesson-id: 212-M4-022
topic-code: MTH212.M4.22
-->

## Table of Contents

- [Introduction](#introduction)
- [Use the System Before the Event](#use-the-system-before-the-event)
- [Turn the Energy Balance Into Speed](#turn-the-energy-balance-into-speed)
- [Square a Fractional Position](#square-a-fractional-position)
- [Separate Speed From Direction](#separate-speed-from-direction)
- [Summary](#summary)

## Prerequisites

- Use $U_s=\frac12kx^2$ for the potential energy of an ideal spring.
- Use $K=\frac12Mv^2$ for translational kinetic energy.
- Conserve mechanical energy when the surface is frictionless.
- Isolate a squared variable and take a square root.

---

<a id="introduction"></a>
## Introduction

When an ideal spring–block system oscillates without friction, its amplitude $A$ fixes its total mechanical energy. At either turning point, $x=\pm A$ and the speed is zero, so

$$
E=\frac12kA^2.
$$

At another position $x$, some of that energy is spring potential energy and the rest is kinetic energy:

$$
\frac12kA^2=\frac12Mv^2+\frac12kx^2.
$$

| State | Spring potential energy | Kinetic energy | Total energy |
|---|---:|---:|---:|
| Turning point, $x=\pm A$ | $\frac12kA^2$ | $0$ | $\frac12kA^2$ |
| Observed position, $x$ | $\frac12kx^2$ | $\frac12Mv^2$ | $\frac12kA^2$ |

Therefore, the speed at position $x$ is

$$
v=\sqrt{\frac{k}{M}\left(A^2-x^2\right)}.
$$

This form requires $|x|\le A$, as every physical position of the oscillator must. The recognition cue is an ideal, frictionless oscillator with a known amplitude and position. If another event is about to happen, use the system as it exists at the instant named in the question.

---

<a id="use-the-system-before-the-event"></a>
## Use the System Before the Event

**Example:** A block of mass $M$ is oscillating on a spring. A piece of clay of mass $m$ is about to stick to it. Which mass belongs in the kinetic-energy term at the instant before contact?

**Explanation**

Before contact, the clay has not joined the oscillator. The moving spring–block system still contains only the block, so its kinetic energy is

$$
K=\frac12Mv^2.
$$

The combined mass $M+m$ may matter after the collision, but it cannot change the block's speed just before the collision.

```quiz
type: radio
id: p7-before-event
content: |-
  A bead of mass $m$ will land on an oscillating block of mass $M$ at $x=-A/3$. Which mass should be used to find the block's speed immediately before the bead lands?
options:
- id: a
  content: |-
    $M$
  correct: true
  feedback: |-
    The system must match the instant named in the question. Immediately before contact, the bead has not joined the oscillator, so the moving oscillator mass is still $M$ and its kinetic energy is $\frac12Mv^2$.
- id: b
  content: |-
    $M+m$
  feedback: |-
    This uses the post-collision system too early. The combined mass $M+m$ describes the block and bead after they stick; immediately before contact, only $M$ belongs in the oscillator's kinetic energy.
- id: c
  content: |-
    $m$
  feedback: |-
    The bead's mass describes the incoming object, not the oscillator whose speed is requested. Before contact the bead is not part of the spring-block system, while the moving block has mass $M$.
- id: d
  content: |-
    No mass appears in the speed formula.
  feedback: |-
    Spring energy becomes the block's kinetic energy, so the block's inertia affects the resulting speed. Solving $\frac12kA^2=\frac12Mv^2+\frac12kx^2$ leaves $M$ in $v=\sqrt{(k/M)(A^2-x^2)}$.
```

---

<a id="turn-the-energy-balance-into-speed"></a>
## Turn the Energy Balance Into Speed

**Example:** Find a formula for the speed of a block of mass $M$ when it is at position $x$ during frictionless oscillation with amplitude $A$.

**Explanation**

Start with the total energy at a turning point and the energy at position $x$:

$$
\frac12kA^2=\frac12Mv^2+\frac12kx^2.
$$

Subtract the spring potential energy at $x$, cancel the factors of $\frac12$, and divide by $M$:

$$
\begin{aligned}
kA^2-kx^2&=Mv^2,\\
v^2&=\frac{k}{M}\left(A^2-x^2\right).
\end{aligned}
$$

Because speed is nonnegative, take the positive square root:

$$
v=\sqrt{\frac{k}{M}\left(A^2-x^2\right)}.
$$

Two endpoint checks make errors easy to spot:

- At equilibrium, $x=0$, so $v=A\sqrt{k/M}$, the maximum speed.
- At a turning point, $|x|=A$, so $v=0$.

```quiz
type: radio
id: p7-energy-balance
content: |-
  Which equation correctly represents energy conservation for the original block at position $x$?
options:
- id: a
  content: |-
    $\frac12kA^2=\frac12Mv^2+\frac12kx^2$
  correct: true
  feedback: |-
    With no friction, total mechanical energy is conserved. The turning point stores $\frac12kA^2$, and at position $x$ that same total is split into block kinetic energy and spring potential energy: $\frac12kA^2=\frac12Mv^2+\frac12kx^2$.
- id: b
  content: |-
    $\frac12kA^2=\frac12Mv^2-\frac12kx^2$
  feedback: |-
    This makes spring potential energy a negative contribution to the energy at $x$. Kinetic and spring potential energies are both parts of the total and therefore add; subtraction appears only after rearranging to isolate $Mv^2$.
- id: c
  content: |-
    $\frac12kA=\frac12Mv^2+\frac12kx$
  feedback: |-
    This uses the spring-force dependence $kx$ as though it were energy. Spring potential energy is $\frac12kx^2$, so both the turning-point amplitude $A$ and the current displacement $x$ must be squared.
- id: d
  content: |-
    $\frac12kx^2=\frac12Mv^2+\frac12kA^2$
  feedback: |-
    This treats the current spring energy as though it were larger than the system's total energy. The amplitude sets the fixed total $\frac12kA^2$; at $x$, the smaller spring term $\frac12kx^2$ is only one part of that total.
- id: e
  content: |-
    $\frac12kA^2=\frac12(M+m)v^2+\frac12kx^2$
  feedback: |-
    This anticipates the sticking collision. Immediately before the bead lands, the spring is accelerating only the original block, so the kinetic term uses $M$; $M+m$ becomes relevant only after contact.
```

---

<a id="square-a-fractional-position"></a>
## Square a Fractional Position

**Example:** Find the speed at $x=A/3$.

**Explanation**

Substitute the entire position into $x^2$. The fraction is squared along with $A$:

$$
x^2=\left(\frac{A}{3}\right)^2=\frac{A^2}{9}.
$$

Then

$$
\begin{aligned}
v&=\sqrt{\frac{k}{M}\left(A^2-\frac{A^2}{9}\right)}\\
&=\sqrt{\frac{k}{M}\left(\frac89A^2\right)}\\
&=A\sqrt{\frac{8k}{9M}}.
\end{aligned}
$$

The common trap is to subtract the unsquared fraction, such as $1-\frac13$. Energy depends on displacement squared.

More generally, if $x=rA$, factor out $A^2$:

$$
v=A\sqrt{\frac{k}{M}\left(1-r^2\right)}.
$$

This compact form makes the required square on the position fraction visible.

```quiz
type: radio
id: q-7
shuffle: true
content: |-
  A block of mass $M$ attached to an ideal spring of spring constant $k$ oscillates with amplitude $A$ over a frictionless horizontal surface.

  A ball of clay lands on the block while it's at $x=A/2$ (assume a conventional $x$-axis pointing to the right with $x=0$ at equilibrium) and sticks to the block's surface.

  What is the speed of the block at the instant before the clay lands?

  ![](<../Source/2026-07-23-HW-6/Images/mass-dropped-onto-spring-block.png>)
options:
- id: a
  content: |-
    $\sqrt{\dfrac{k}{M}}A$
  feedback: |-
    This is the equilibrium speed, where all the spring energy has become kinetic energy. At $x=A/2$, the spring still stores one fourth of the total energy, so the speed must be below $A\sqrt{k/M}$.
- id: b
  content: |-
    $\sqrt{\dfrac{2k}{M}}A$
  feedback: |-
    The oscillator's speed is greatest at equilibrium, where it is $A\sqrt{k/M}$. This choice is larger than that maximum, so it cannot describe the block at $x=A/2$ or anywhere else in the motion.
- id: c
  content: |-
    $\sqrt{\dfrac{3k}{4M}}A$
  correct: true
  feedback: |-
    At $x=A/2$, the spring retains the fraction $(x/A)^2=1/4$ of the total energy, leaving $3/4$ as kinetic energy. Therefore the speed is $v=A\sqrt{3k/(4M)}$.
- id: d
  content: |-
    $\sqrt{\dfrac{2k}{5M}}A$
  feedback: |-
    This uses an energy fraction that does not follow from the stated position. Before impact the moving mass is $M$, and $x=A/2$ leaves $1-(1/2)^2=3/4$ of the total energy as kinetic energy, not $2/5$.
```

---

<a id="separate-speed-from-direction"></a>
## Separate Speed From Direction

**Example:** Compare the speed at $x=A/2$ with the speed at $x=-A/2$.

**Explanation**

The formula contains $x^2$, so the two positions give the same speed:

$$
v=\sqrt{\frac{k}{M}\left(A^2-\left(\pm\frac A2\right)^2\right)}
=A\sqrt{\frac{3k}{4M}}.
$$

The velocity could point left or right, depending on which way the block is moving. Speed is only the magnitude, so it is never negative.

```quiz
type: radio
id: p7-negative-position
content: |-
  An oscillating block is at $x=-2A/3$. What is its speed?
options:
- id: a
  content: |-
    $-A\sqrt{\dfrac{5k}{9M}}$
  feedback: |-
    This transfers the sign of position to speed. Position tells which side of equilibrium the block occupies, while speed is the nonnegative magnitude of velocity, so $x<0$ cannot make the requested speed negative.
- id: b
  content: |-
    $A\sqrt{\dfrac{5k}{9M}}$
  correct: true
  feedback: |-
    Mechanical energy depends on $x^2$, so positions equally far to either side of equilibrium have the same speed. Here $(-2A/3)^2=4A^2/9$, leaving $5/9$ of the energy fraction for motion and giving $v=A\sqrt{5k/(9M)}$.
- id: c
  content: |-
    $A\sqrt{\dfrac{5k}{3M}}$
  feedback: |-
    This does not square the full fractional displacement correctly. Because energy depends on $x^2$, $x=-2A/3$ contributes $4A^2/9$, so the remaining factor is $1-4/9=5/9$, not $5/3$.
- id: d
  content: |-
    $\dfrac{2A}{3}\sqrt{\dfrac{k}{M}}$
  feedback: |-
    This treats the displacement fraction $|x|/A=2/3$ as the fraction of maximum speed. Speed instead follows the kinetic-energy remainder, $\sqrt{1-(x/A)^2}=\sqrt5/3$, so the factor is not $2/3$.
- id: e
  content: |-
    $A\sqrt{\dfrac{k}{M}}$
  feedback: |-
    This is the maximum speed attained only at equilibrium, where $x=0$ and the spring energy is zero. At $x=-2A/3$, the spring still stores energy, so the speed is smaller by the factor $\sqrt5/3$.
```

---

<a id="summary"></a>
## Summary

When an ideal, frictionless spring oscillator has amplitude $A$ and is observed at position $x$:

1. Freeze the system at the requested instant. An object that has not landed yet is not part of the oscillating mass.
2. Write $\frac12kA^2=\frac12Mv^2+\frac12kx^2$.
3. Solve for the nonnegative speed:

   $$
   v=\sqrt{\frac{k}{M}\left(A^2-x^2\right)}.
   $$

4. Square the entire position. If $x=rA$, then $x^2=r^2A^2$.
5. Do not attach a direction sign to speed; positions $x$ and $-x$ have the same speed.
6. Check the endpoints: $v=A\sqrt{k/M}$ at $x=0$ and $v=0$ at $|x|=A$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../../M5/2026-08-03-Q-3/Study-Guide.md)
Next: [Deciding What Changes a Pendulum's Frequency](../../../M5/2026-08-02-PQ-3/Lessons/Problem-1.md)

Study guide index: 05/28

---
<!-- lesson-nav:end -->
