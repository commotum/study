# Period After Mass Sticks to a Spring Oscillator

## Table of Contents

- [Introduction](#introduction)
- [Identify the Moving Mass](#identify-the-moving-mass)
- [Substitute Into the Period Formula](#substitute-into-the-period-formula)
- [Check Whether the Period Should Increase](#check-whether-the-period-should-increase)
- [Ignore Details That Do Not Set the Period](#ignore-details-that-do-not-set-the-period)
- [Summary](#summary)

## Prerequisites

- Know the period formula for an ideal horizontal mass-spring oscillator.
- Interpret “sticks” to mean that the two masses move together afterward.
- Simplify sums inside square roots.

---

<a id="introduction"></a>
## Introduction

When an object lands on an oscillating block and sticks, first identify the mass that the spring must move after the collision. Then use that combined mass in

$$
T=2\pi\sqrt{\frac{m_{\mathrm{eff}}}{k}},
$$

where $m_{\mathrm{eff}}$ is the total mass moving with the spring.

The recognition cue is the word **sticks**: after the collision, the block and clay are one oscillating system. Read the formula before substituting:

- $m_{\mathrm{eff}}$ is the post-collision moving mass.
- $k$ is the spring constant, which is unchanged.
- Neither amplitude nor collision position appears in the formula.

---

<a id="identify-the-moving-mass"></a>
## Identify the Moving Mass

**Example:** A block of mass $B$ is attached to a spring. Putty of mass $p$ lands on the block and sticks. What mass belongs in the period formula after the collision?

**Explanation**

Because the block and putty move together after the collision, the spring accelerates both masses. Therefore,

$$
m_{\mathrm{eff}}=B+p.
$$

Do not replace $B$ by $p$, multiply the masses, or use only the original block mass.

```quiz
type: radio
id: p11-effective-mass
content: |-
  A $6\,\mathrm{kg}$ block oscillates on a spring. A $1.5\,\mathrm{kg}$ lump of clay sticks to it. What is the effective oscillating mass afterward?
options:
- id: p11-em-a
  content: |-
    $1.5\,\mathrm{kg}$
- id: p11-em-b
  content: |-
    $4.5\,\mathrm{kg}$
- id: p11-em-c
  content: |-
    $6\,\mathrm{kg}$
- id: p11-em-d
  content: |-
    $7.5\,\mathrm{kg}$
  correct: true
- id: p11-em-e
  content: |-
    $9\,\mathrm{kg}$
```

---

<a id="substitute-into-the-period-formula"></a>
## Substitute Into the Period Formula

**Example:** A block of mass $Q$ oscillates on a spring of constant $\kappa$. An object of mass $r$ sticks to the block. Find the new period.

**Explanation**

The spring constant remains $\kappa$, while the moving mass changes from $Q$ to $Q+r$. Substitute these post-collision quantities:

$$
\begin{aligned}
T_{\mathrm{new}}
&=2\pi\sqrt{\frac{m_{\mathrm{eff}}}{\kappa}}\\
&=2\pi\sqrt{\frac{Q+r}{\kappa}}.
\end{aligned}
$$

```quiz
type: radio
id: p11-period-substitution
content: |-
  A cart of mass $C$ oscillates on an ideal spring of constant $s$. A package of mass $p$ lands on the cart and sticks. What is the new period?
options:
- id: p11-ps-a
  content: |-
    $2\pi\sqrt{\dfrac{C+p}{s}}$
  correct: true
- id: p11-ps-b
  content: |-
    $2\pi\sqrt{\dfrac{C}{s}}$
- id: p11-ps-c
  content: |-
    $2\pi\sqrt{\dfrac{p}{s}}$
- id: p11-ps-d
  content: |-
    $2\pi\sqrt{\dfrac{s}{C+p}}$
- id: p11-ps-e
  content: |-
    $2\pi\sqrt{\dfrac{Cp}{s}}$
```

---

<a id="check-whether-the-period-should-increase"></a>
## Check Whether the Period Should Increase

**Example:** A clay mass $3M$ sticks to a block of mass $M$. By what factor does the period change?

**Explanation**

Compare the new and old periods before doing any detailed calculation:

$$
\begin{aligned}
\frac{T_{\mathrm{new}}}{T_{\mathrm{old}}}
&=
\frac{2\pi\sqrt{(M+3M)/k}}{2\pi\sqrt{M/k}}\\
&=\sqrt{\frac{4M}{M}}\\
&=2.
\end{aligned}
$$

The total moving mass is four times as large, so the period is twice as large. In general,

$$
\frac{T_{\mathrm{new}}}{T_{\mathrm{old}}}
=\sqrt{\frac{M+m}{M}}>1
$$

for $m>0$. This direction check catches the common error of writing $k/(M+m)$ under the square root, which would incorrectly predict a shorter period when mass is added.

```quiz
type: radio
id: p11-period-ratio
content: |-
  A lump of clay of mass $8M$ sticks to a spring-mounted block of mass $M$. The spring is unchanged. What is $\dfrac{T_{\mathrm{new}}}{T_{\mathrm{old}}}$?
options:
- id: p11-pr-a
  content: |-
    $\dfrac{1}{3}$
- id: p11-pr-b
  content: |-
    $1$
- id: p11-pr-c
  content: |-
    $3$
  correct: true
- id: p11-pr-d
  content: |-
    $8$
- id: p11-pr-e
  content: |-
    $9$
```

---

<a id="ignore-details-that-do-not-set-the-period"></a>
## Ignore Details That Do Not Set the Period

**Example:** Clay sticks to a spring-mounted block at $x=A/3$. Must $A/3$ be substituted into the period formula?

**Explanation**

No. The position can matter when finding the velocity, energy, or new amplitude immediately after the collision, but it is not an input to the ideal-spring period formula. For the period, use only the effective mass and the spring constant.

Now apply that test to the original situation.

```quiz
type: radio
id: p11-original-check
content: |-
  A block of mass $M$ attached to an ideal spring of spring constant $k$ oscillates with amplitude $A$ over a frictionless horizontal surface.

  A ball of clay lands on the block while it's at $x=A/2$ (assume a conventional $x$-axis pointing to the right with $x=0$ at equilibrium) and sticks to the block's surface.

  What is the new period of the block's oscillations after the clay lands and sticks to it?

  ![](<../Source/2026-07-23-HW-6/Images/mass-dropped-onto-spring-block.png>)
options:
- id: p11-oc-a
  content: |-
    $2\pi\sqrt{\dfrac{M+m}{k}}$
  correct: true
- id: p11-oc-b
  content: |-
    $2\pi\sqrt{\dfrac{M}{m}\dfrac{k}{M+m}}$
- id: p11-oc-c
  content: |-
    $2\pi\sqrt{\dfrac{m}{M}\dfrac{k}{M+m}}$
- id: p11-oc-d
  content: |-
    $2\pi\sqrt{\dfrac{k}{M+m}}$
```

---

<a id="summary"></a>
## Summary

When an added object sticks to a spring oscillator:

1. Add the masses that move together: $m_{\mathrm{eff}}=M+m$.
2. Keep the unchanged spring constant $k$.
3. Substitute into $T=2\pi\sqrt{m_{\mathrm{eff}}/k}$.
4. Check that adding mass makes the period longer.
5. Ignore amplitude and collision position when the question asks only for the ideal-spring period.

The main trap is reversing the fraction. More moving mass makes the period longer, so the mass belongs in the numerator.
