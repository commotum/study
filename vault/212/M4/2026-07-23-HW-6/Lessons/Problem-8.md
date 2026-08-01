# Speed Immediately After a Mass Sticks to a Moving Block

## Table of Contents

- [Introduction](#introduction)
- [Build the Horizontal Momentum Equation](#build-the-horizontal-momentum-equation)
- [Solve for the Shared Speed](#solve-for-the-shared-speed)
- [Check the Mass Fraction](#check-the-mass-fraction)
- [Do Not Conserve Kinetic Energy](#do-not-conserve-kinetic-energy)
- [Apply the Rule to the Spring–Block Collision](#apply-the-rule-to-the-spring-block-collision)
- [Summary](#summary)

## Prerequisites

- Use one-dimensional momentum, $p_x=mv_x$.
- Add the momenta of every object in a chosen system.
- Solve a one-step symbolic equation.

---

<a id="introduction"></a>
## Introduction

The recognition cue is **sticks at the instant after impact**. Sticking means the objects share one velocity after the collision, so treat them as one combined mass.

For the brief collision, choose the block and clay as the system and work in the horizontal direction. A ball dropped straight down has zero horizontal velocity, so it contributes no initial horizontal momentum. The reusable move is to conserve horizontal momentum across the collision:

$$
p_{x,\text{before}}=p_{x,\text{after}}.
$$

For a block of mass $M$ moving at speed $v_0$ and vertically dropped clay of mass $m$, the cue translates directly to

$$
\underbrace{Mv_0}_{\substack{\text{moving mass}\\\text{before}}}
=
\underbrace{(M+m)v_f}_{\substack{\text{stuck pair}\\\text{after}}},
$$

where $v_f$ is their shared speed immediately after impact.

This rule applies during the short impact when the external horizontal impulse is negligible. It does not say that kinetic energy is conserved.

---

<a id="build-the-horizontal-momentum-equation"></a>
## Build the Horizontal Momentum Equation

**Example:** A $3\,\mathrm{kg}$ block moves right at $4\,\mathrm{m/s}$. A $1\,\mathrm{kg}$ lump of clay falls vertically onto it and sticks. Write the horizontal momentum equation for the collision.

**Explanation**

Before impact, only the block has horizontal momentum:

$$
p_{x,\text{before}}
=(3\,\mathrm{kg})(4\,\mathrm{m/s})+(1\,\mathrm{kg})(0)
=12\,\mathrm{kg\,m/s}.
$$

After impact, the block and clay move together. If their shared velocity is $v_f$, then

$$
p_{x,\text{after}}=(3+1)\,\mathrm{kg}\,v_f.
$$

Therefore, the collision equation is

$$
12=(4)v_f.
$$

Solving gives

$$
v_f=3\,\mathrm{m/s}.
$$

The block slows because the same horizontal momentum is carried by more mass after the clay sticks.

```quiz
type: radio
id: p8-horizontal-momentum
content: |-
  A block of mass $5\,\mathrm{kg}$ moves horizontally at speed $u$. A $2\,\mathrm{kg}$ clay ball drops straight down and sticks to it. What is the system's horizontal momentum immediately before impact?
options:
- id: p8-horizontal-momentum-a
  content: |-
    $5u$
  correct: true
- id: p8-horizontal-momentum-b
  content: |-
    $7u$
- id: p8-horizontal-momentum-c
  content: |-
    $2u$
- id: p8-horizontal-momentum-d
  content: |-
    $\dfrac{5}{7}u$
- id: p8-horizontal-momentum-e
  content: |-
    $0$
```

---

<a id="solve-for-the-shared-speed"></a>
## Solve for the Shared Speed

**Example:** A block of mass $M$ moves horizontally at speed $v_0$. Clay of mass $m$ drops vertically, sticks, and the pair moves at speed $v_f$. Find $v_f$.

**Explanation**

The block supplies the initial horizontal momentum $Mv_0$. After impact, the moving mass is $M+m$:

$$
Mv_0=(M+m)v_f.
$$

Divide by the combined mass:

$$
\begin{aligned}
Mv_0&=(M+m)v_f,\\
\frac{Mv_0}{M+m}&=v_f,\\
v_f&=\boxed{\frac{M}{M+m}v_0}.
\end{aligned}
$$

Here, $M+m>0$ because both masses are positive.

```quiz
type: radio
id: p8-solve-shared-speed
content: |-
  A $4\,\mathrm{kg}$ block moves at $10\,\mathrm{m/s}$. A $1\,\mathrm{kg}$ clay ball drops vertically and sticks to it. What is their speed immediately after impact?
options:
- id: p8-solve-shared-speed-a
  content: |-
    $8\,\mathrm{m/s}$
  correct: true
- id: p8-solve-shared-speed-b
  content: |-
    $2\,\mathrm{m/s}$
- id: p8-solve-shared-speed-c
  content: |-
    $10\,\mathrm{m/s}$
- id: p8-solve-shared-speed-d
  content: |-
    $12.5\,\mathrm{m/s}$
- id: p8-solve-shared-speed-e
  content: |-
    $50\,\mathrm{m/s}$
```

---

<a id="check-the-mass-fraction"></a>
## Check the Mass Fraction

**Example:** Suppose the dropped clay has the same mass as the moving block, so $m=M$. What fraction of the original speed remains?

**Explanation**

Substitute $m=M$ into the speed factor:

$$
\frac{v_f}{v_0}
=\frac{M}{M+m}
=\frac{M}{M+M}
=\frac{1}{2}.
$$

The factor $\dfrac{M}{M+m}$ must lie between $0$ and $1$ for positive masses. Thus, the pair keeps the block's direction but moves more slowly. This also shows why the numerator is $M$: $M$ is the mass that carried the initial horizontal momentum.

```quiz
type: radio
id: p8-mass-fraction
content: |-
  A clay ball of mass $2M$ drops vertically onto a block of mass $M$ moving at speed $v_0$ and sticks. What is the shared speed immediately after impact?
options:
- id: p8-mass-fraction-a
  content: |-
    $\dfrac{1}{3}v_0$
  correct: true
- id: p8-mass-fraction-b
  content: |-
    $\dfrac{2}{3}v_0$
- id: p8-mass-fraction-c
  content: |-
    $2v_0$
- id: p8-mass-fraction-d
  content: |-
    $3v_0$
- id: p8-mass-fraction-e
  content: |-
    $v_0$
```

---

<a id="do-not-conserve-kinetic-energy"></a>
## Do Not Conserve Kinetic Energy

**Example:** In the earlier collision, a $3\,\mathrm{kg}$ block moving at $4\,\mathrm{m/s}$ sticks to $1\,\mathrm{kg}$ of vertically dropped clay and leaves at $3\,\mathrm{m/s}$. Compare the kinetic energy immediately before and after impact.

**Explanation**

Before impact,

$$
K_{\text{before}}
=\frac12(3)(4^2)
=24\,\mathrm{J}.
$$

After impact,

$$
K_{\text{after}}
=\frac12(3+1)(3^2)
=18\,\mathrm{J}.
$$

The kinetic energies are not equal. Because the clay sticks, the collision is perfectly inelastic: some kinetic energy becomes deformation, thermal energy, and sound. Horizontal momentum is conserved during the brief impact, but kinetic energy generally is not.

The spring does not change this collision rule. Its position is essentially unchanged during the instant of impact, and its short horizontal impulse is negligible. Use the spring motion to find the pre-impact speed if needed; then use momentum for the collision itself.

```quiz
type: radio
id: p8-conservation-choice
content: |-
  During the brief sticking collision, which quantity should be set equal immediately before and immediately after impact?
options:
- id: p8-conservation-choice-a
  content: |-
    The horizontal momentum of the block–clay system
  correct: true
- id: p8-conservation-choice-b
  content: |-
    The kinetic energy of the block–clay system
- id: p8-conservation-choice-c
  content: |-
    The momentum of the block alone
- id: p8-conservation-choice-d
  content: |-
    The speed of the block alone
- id: p8-conservation-choice-e
  content: |-
    The spring's elastic potential energy and the block's kinetic energy
```

---

<a id="apply-the-rule-to-the-spring-block-collision"></a>
## Apply the Rule to the Spring–Block Collision

**Example:** A block of mass $M$ attached to an ideal spring of spring constant $k$ oscillates with amplitude $A$ over a frictionless horizontal surface. A ball of clay of mass $m$ lands on the block while it is at $x=A/2$ and sticks. If the block's speed immediately before impact is $v_0$, find its speed immediately after impact.

**Explanation**

The location $x=A/2$ was needed to determine the pre-impact speed $v_0$. Once $v_0$ is known, freeze the motion at the collision:

$$
\underbrace{Mv_0}_{\text{before}}
=\underbrace{(M+m)v_f}_{\text{after}}.
$$

Therefore,

$$
\boxed{v_f=\frac{M}{M+m}v_0}.
$$

```quiz
type: radio
id: p8-assignment-check
content: |-
  A block of mass $M$ attached to an ideal spring of spring constant $k$ oscillates with amplitude $A$ over a frictionless horizontal surface.

  A ball of clay lands on the block while it's at $x=A/2$ (assume a conventional $x$-axis pointing to the right with $x=0$ at equilibrium) and sticks to the block's surface.

  Let your answer to the previous question equal $v_0$.

  What is the speed of the block at the instant after the clay lands?

  ![](<../Source/2026-07-23-HW-6/Images/mass-dropped-onto-spring-block.png>)
options:
- id: p8-assignment-check-a
  content: |-
    $\dfrac{m}{m+M}v_0$
- id: p8-assignment-check-b
  content: |-
    $\dfrac{M}{m+M}v_0$
  correct: true
- id: p8-assignment-check-c
  content: |-
    $\dfrac{m}{M}v_0$
- id: p8-assignment-check-d
  content: |-
    $\dfrac{M}{m}v_0$
```

---

<a id="summary"></a>
## Summary

**Cue:** A mass drops vertically and **sticks**; the question asks for the speed **immediately after** impact.

**Procedure:**

1. Choose the block and dropped mass as the system.
2. Keep only horizontal velocity components.
3. Write $Mv_0=(M+m)v_f$.
4. Solve $v_f=\dfrac{M}{M+m}v_0$.

**Check:** For positive added mass, $\dfrac{M}{M+m}$ lies between $0$ and $1$, so $0<v_f<v_0$.

**Main trap:** Do not conserve kinetic energy across a sticking collision. Conserve the system's horizontal momentum during impact.
