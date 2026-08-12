# Predicting Wave-Speed Changes From a Hanging Mass

<!--
lesson-id: 212-M5-007
topic-code: MTH212.M5.07
-->

## Table of Contents

- [Introduction](#introduction)
- [Identify What Changes](#identify-what-changes)
- [Chain Mass to Tension to Wave Speed](#chain-mass-to-tension-to-wave-speed)
- [Use a Square-Root Scale Factor](#use-a-square-root-scale-factor)
- [Keep Block Mass Separate From String Density](#keep-block-mass-separate-from-string-density)
- [Apply the Reasoning to the Pulley Setup](#apply-the-reasoning-to-the-pulley-setup)
- [Summary](#summary)

## Prerequisites

- Use the wave-speed model $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$ for a wave on a string.
- Recognize that a stationary hanging mass produces tension approximately equal to its weight, $F_T\approx Mg$.
- Compare positive quantities using direct and square-root relationships.

---

<a id="introduction"></a>
## Introduction

For a wave traveling on a string,

$$
v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}},
$$

where $F_T$ is the string tension and $\mu$ is the string's linear mass density.

In the pulley setup, the hanging block supplies the tension. If the block is stationary, then

$$
F_T\approx Mg.
$$

Substituting this into the wave-speed equation gives

$$
v_{\mathrm{wave}}=\sqrt{\frac{Mg}{\mu}}.
$$

When the same string and location are used, $g$ and $\mu$ stay constant. The core move is therefore to follow the change through this chain:

$$
M\longrightarrow F_T\longrightarrow v_{\mathrm{wave}}.
$$

An increase in $M$ increases $F_T$, and an increase in $F_T$ increases $v_{\mathrm{wave}}$.

Equivalently, under these fixed-condition assumptions,

$$
F_T\propto M
\qquad\text{and}\qquad
v_{\mathrm{wave}}\propto\sqrt{M}.
$$

These proportionality statements are conditional: they apply here because $g$ and $\mu$ are held constant.

---

<a id="identify-what-changes"></a>
## Identify What Changes

**Example:** The hanging block's mass increases while everything else remains constant. Which quantities change?

**Explanation**

Start by assigning each quantity a role.

| Quantity | Role | What happens when $M$ increases? |
|---|---|---|
| Hanging-block mass $M$ | Changed input | Increases |
| Tension $F_T\approx Mg$ | Dependent quantity | Increases |
| String linear density $\mu$ | Property of the unchanged string | Stays constant |
| Wave speed $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$ | Target output | Must be determined |

The phrase **everything else remains constant** is the cue to keep $\mu$ fixed. The block's mass changes the tension; it does not change the material per unit length of the string.

```quiz
type: radio
id: problem-7-variables-q1
content: |-
  The hanging mass is increased while the same string segment is used. Which quantity should be treated as constant in $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$?
options:
- id: a
  content: |-
    The string's linear density $\mu$
  correct: true
  feedback: |-
    The string itself is unchanged, so its mass per unit length remains constant.
- id: b
  content: |-
    The tension $F_T$
  feedback: |-
    The hanging block supplies the tension, so increasing its mass changes the tension.
- id: c
  content: |-
    The hanging mass $M$
  feedback: |-
    The problem explicitly changes the hanging mass.
```

---

<a id="chain-mass-to-tension-to-wave-speed"></a>
## Chain Mass to Tension to Wave Speed

**Example:** A stationary hanging block is replaced by a heavier block. Does the wave on the horizontal string travel faster, slower, or at the same speed?

**Explanation**

First connect the block to the string tension:

$$
M\uparrow \quad\Longrightarrow\quad F_T\approx Mg\uparrow.
$$

Then connect the tension to wave speed:

$$
F_T\uparrow \quad\Longrightarrow\quad v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}}\uparrow,
$$

because $\mu$ is fixed and the square-root function increases when its positive input increases.

Therefore,

$$
M\uparrow \quad\Longrightarrow\quad F_T\uparrow \quad\Longrightarrow\quad v_{\mathrm{wave}}\uparrow.
$$

The dependency map makes every link visible:

| Stage | Relationship | Direction of change |
|---|---|---|
| Hanging mass to tension | $F_T\approx Mg$ | $M\uparrow\Rightarrow F_T\uparrow$ |
| Tension to wave speed | $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$ at fixed $\mu$ | $F_T\uparrow\Rightarrow v_{\mathrm{wave}}\uparrow$ |
| Full chain | $v_{\mathrm{wave}}\approx\sqrt{Mg/\mu}$ | $M\uparrow\Rightarrow v_{\mathrm{wave}}\uparrow$ |

```quiz
type: radio
id: problem-7-chain-q1
content: |-
  A stationary hanging block is replaced by a lighter block, while the string is unchanged. What happens to the wave speed?
options:
- id: a
  content: |-
    It decreases because the lighter block produces less tension.
  correct: true
  feedback: |-
    A smaller $M$ gives a smaller $F_T\approx Mg$, and $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$ decreases when $F_T$ decreases at fixed $\mu$.
- id: b
  content: |-
    It increases because less hanging mass always means less inertia for the wave.
  feedback: |-
    The block is not the medium carrying the wave. Its mass controls the string tension.
- id: c
  content: |-
    It stays the same because the string itself is unchanged.
  feedback: |-
    The string's linear density stays the same, but its tension changes.
```

---

<a id="use-a-square-root-scale-factor"></a>
## Use a Square-Root Scale Factor

First decide the **direction** of the change. Only calculate a factor if the question asks how many times larger or smaller the speed becomes.

**Example:** The hanging mass is quadrupled. By what factor does the wave speed change?

**Explanation**

For two versions of the same setup,

$$
\frac{v_2}{v_1}
=\sqrt{\frac{F_T_2}{F_T_1}}
=\sqrt{\frac{M_2g}{M_1g}}
=\sqrt{\frac{M_2}{M_1}}.
$$

If $M_2=4M_1$, then

$$
\frac{v_2}{v_1}=\sqrt{4}=2.
$$

The speed doubles. It does not quadruple because wave speed depends on the square root of the mass through the tension.

The function $\sqrt{x}$ is increasing for positive $x$, so a larger mass always gives a larger speed in this model. However, it grows more slowly than $x$: multiplying the mass by a factor $k$ multiplies the speed by only $\sqrt{k}$.

```quiz
type: radio
id: problem-7-scale-q1
content: |-
  The hanging mass is multiplied by $9$ while the string remains unchanged. By what factor is the wave speed multiplied?
options:
- id: a
  content: |-
    $3$
  correct: true
  feedback: |-
    Since $v_{\mathrm{wave}}\propto\sqrt{M}$, multiplying $M$ by $9$ multiplies $v_{\mathrm{wave}}$ by $\sqrt{9}=3$.
- id: b
  content: |-
    $9$
  feedback: |-
    Tension is multiplied by $9$, but speed depends on the square root of tension.
- id: c
  content: |-
    $\frac{1}{3}$
  feedback: |-
    Increasing the hanging mass increases both tension and wave speed.
```

---

<a id="keep-block-mass-separate-from-string-density"></a>
## Keep Block Mass Separate From String Density

**Example:** A student says, “Increasing the mass makes the system heavier, so $\mu$ increases and the wave slows down.” What is wrong with this reasoning?

**Explanation**

The symbols refer to different objects:

- $M$ is the mass of the block hanging from the end of the string.
- $\mu$ is the mass per unit length of the string segment carrying the wave.

Replacing the block does not replace or thicken the string, so it does not change $\mu$. Instead, a heavier block pulls harder and increases $F_T$.

**Watch Out!** Do not use the vague rule “more mass means slower.” Decide whose mass changes and identify where that quantity appears in the model.

```quiz
type: radio
id: problem-7-density-q1
content: |-
  Why does increasing the hanging block's mass not increase $\mu$ in the wave-speed equation?
options:
- id: a
  content: |-
    Because $\mu$ describes the mass per unit length of the string, not the mass of the hanging block.
  correct: true
  feedback: |-
    The unchanged string has the same linear density even when a different block supplies its tension.
- id: b
  content: |-
    Because $\mu$ always equals zero for a horizontal string.
  feedback: |-
    A physical string has nonzero mass per unit length.
- id: c
  content: |-
    Because the block changes gravity instead of tension.
  feedback: |-
    At the same location, $g$ is constant; the block's weight and the resulting tension change.
```

---

<a id="apply-the-reasoning-to-the-pulley-setup"></a>
## Apply the Reasoning to the Pulley Setup

**Example:** A block of mass $M$ hangs from a string over a pulley. A wave travels along the horizontal string segment. What happens to the wave speed when $M$ increases?

![](<../Source/Images/wire-pulley-hanging-mass.png>)

**Explanation**

The same string segment is carrying the wave, so $\mu$ remains constant. The hanging block supplies tension approximately equal to its weight:

$$
F_T\approx Mg.
$$

Thus,

$$
v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}}
\approx\sqrt{\frac{Mg}{\mu}}.
$$

With $g$ and $\mu$ constant, increasing $M$ increases the positive quantity inside the square root. The wave speed therefore **increases**.

```quiz
type: radio
id: m5-1lec-q6
shuffle: true
content: |-
  **Question 6**

  A block of mass $M$ hangs from a string over a pulley. A wave propagates along the string segment between the wall and pulley. What happens to the wave speed if the block's mass increases while everything else remains constant? Explain.

  ![](<../Source/Images/wire-pulley-hanging-mass.png>)
options:
- id: a
  content: The wave speed increases
  correct: true
  feedback: The hanging block produces tension approximately equal to $Mg$. Since $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$ and the string's linear density remains constant, increasing $M$ increases the wave speed.
- id: b
  content: The wave speed decreases
- id: c
  content: The wave speed stays the same
```

---

<a id="summary"></a>
## Summary

To predict the wave-speed change in this setup:

1. Hold the string's linear density $\mu$ constant.
2. Use $F_T\approx Mg$ to connect the hanging mass to tension.
3. Use $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$ to connect tension to wave speed.
4. Follow the direction of change: $M\uparrow\Rightarrow F_T\uparrow\Rightarrow v_{\mathrm{wave}}\uparrow$.
5. For a numerical scale factor, use $v_2/v_1=\sqrt{M_2/M_1}$.

The hanging block changes the tension, not the string's linear density. A heavier hanging block makes the wave travel faster.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
