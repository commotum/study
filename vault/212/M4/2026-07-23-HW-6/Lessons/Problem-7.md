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
    Immediately before contact, only the original block is part of the oscillator, so the kinetic term is $\frac12Mv^2$.
- id: b
  content: |-
    $M+m$
  feedback: |-
    This includes the bead before it has landed. The combined mass matters only after the sticking collision.
- id: c
  content: |-
    $m$
  feedback: |-
    The bead is not yet oscillating, and this choice omits the moving block whose speed is being found.
- id: d
  content: |-
    No mass appears in the speed formula.
  feedback: |-
    Solving the energy equation gives $v=\sqrt{(k/M)(A^2-x^2)}$, so the block mass remains in the denominator.
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
    The turning-point energy $\frac12kA^2$ equals the kinetic plus spring potential energy at position $x$.
- id: b
  content: |-
    $\frac12kA^2=\frac12Mv^2-\frac12kx^2$
  feedback: |-
    Spring potential energy is a positive part of the energy at $x$; it must be added, not subtracted, on the right.
- id: c
  content: |-
    $\frac12kA=\frac12Mv^2+\frac12kx$
  feedback: |-
    Ideal-spring energy is $\frac12kx^2$, so both the amplitude and displacement must be squared.
- id: d
  content: |-
    $\frac12kx^2=\frac12Mv^2+\frac12kA^2$
  feedback: |-
    This reverses the energy ledger: $\frac12kA^2$ is the fixed total, while $\frac12kx^2$ is only the potential energy at the observed position.
- id: e
  content: |-
    $\frac12kA^2=\frac12(M+m)v^2+\frac12kx^2$
  feedback: |-
    The bead has not landed yet, so using $M+m$ inserts post-collision mass into a pre-collision energy balance.
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
    This is the maximum speed at $x=0$ and ignores the spring potential energy still present at $x=A/2$.
- id: b
  content: |-
    $\sqrt{\dfrac{2k}{M}}A$
  feedback: |-
    This exceeds the oscillator's maximum speed $A\sqrt{k/M}$, so it cannot occur at any position in this motion.
- id: c
  content: |-
    $\sqrt{\dfrac{3k}{4M}}A$
  correct: true
  feedback: |-
    Since $(A/2)^2=A^2/4$, the kinetic-energy fraction is $1-1/4=3/4$, giving $v=A\sqrt{3k/(4M)}$.
- id: d
  content: |-
    $\sqrt{\dfrac{2k}{5M}}A$
  feedback: |-
    Neither the pre-impact mass nor the energy fraction supports $2/5$; the mass is $M$ and $A^2-x^2=3A^2/4$.
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
    A negative position does not make speed negative. Speed is a magnitude and must be nonnegative.
- id: b
  content: |-
    $A\sqrt{\dfrac{5k}{9M}}$
  correct: true
  feedback: |-
    Squaring $x=-2A/3$ gives $4A^2/9$, so $A^2-x^2=5A^2/9$ and $v=A\sqrt{5k/(9M)}$.
- id: c
  content: |-
    $A\sqrt{\dfrac{5k}{3M}}$
  feedback: |-
    The fractional displacement must be squared: the remaining factor is $1-4/9=5/9$, not $5/3$.
- id: d
  content: |-
    $\dfrac{2A}{3}\sqrt{\dfrac{k}{M}}$
  feedback: |-
    This substitutes the position magnitude for the speed factor. Energy requires $\sqrt{1-(2/3)^2}=\sqrt5/3$, not $2/3$.
- id: e
  content: |-
    $A\sqrt{\dfrac{k}{M}}$
  feedback: |-
    This is the equilibrium maximum speed and ignores the spring potential energy at the nonzero position $x=-2A/3$.
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
