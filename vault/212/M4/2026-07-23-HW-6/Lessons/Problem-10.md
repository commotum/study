# Finding a New Spring-Oscillation Amplitude After an Energy Change

<!--
lesson-id: 212-M4-025
topic-code: MTH212.M4.25
-->

## Table of Contents

- [Introduction](#introduction)
- [Update the Mechanical Energy](#update-the-mechanical-energy)
- [Convert Energy to Amplitude](#convert-energy-to-amplitude)
- [Combine the Two Relations](#combine-the-two-relations)
- [Check the Sign and Physical Range](#check-the-sign-and-physical-range)
- [Summary](#summary)

## Prerequisites

- Use the ideal spring oscillator relation $E=\frac12 kA^2$.
- Interpret $\Delta E$ as $E_{\mathrm{after}}-E_{\mathrm{before}}$.
- Solve an equation for a squared variable and select a physically meaningful root.

---

<a id="introduction"></a>
## Introduction

When a collision or another sudden event changes an oscillator's mechanical energy, its old amplitude no longer describes the motion after the event. The recognition cue is that the problem gives an initial amplitude and an energy change, then asks for a new amplitude.

Use this chain:

$$
E_{\mathrm{before}}+\Delta E
=E_{\mathrm{after}}
=\frac12 kA_{\mathrm{new}}^2.
$$

The spring constant $k$ is unchanged, so updating the energy and then solving the spring-energy relation determines the new amplitude. Although the clay changes the system's mass, mass does not appear in the relation between an ideal oscillator's total energy and amplitude.

---

<a id="update-the-mechanical-energy"></a>
## Update the Mechanical Energy

**Example:** An oscillator has $E_{\mathrm{before}}=18\ \mathrm{J}$ and undergoes a change $\Delta E=-3\ \mathrm{J}$. Find its energy after the event.

**Explanation**

Start from the definition

$$
\Delta E=E_{\mathrm{after}}-E_{\mathrm{before}}.
$$

Add $E_{\mathrm{before}}$ to both sides:

$$
\begin{aligned}
E_{\mathrm{after}}
&=E_{\mathrm{before}}+\Delta E\\
&=18\ \mathrm{J}+(-3\ \mathrm{J})\\
&=15\ \mathrm{J}.
\end{aligned}
$$

A negative $\Delta E$ already accounts for an energy loss. Do not change the plus sign in the update equation.

```quiz
type: radio
id: p10-energy-update
content: |-
  An ideal spring oscillator initially has amplitude $C$. Its mechanical energy changes by $\Delta E$. Which expression gives its energy after the change?
options:
- id: p10-energy-a
  content: |-
    $\dfrac12 kC^2+\Delta E$
  correct: true
- id: p10-energy-b
  content: |-
    $\dfrac12 kC^2-\Delta E$
- id: p10-energy-c
  content: |-
    $\Delta E-\dfrac12 kC^2$
- id: p10-energy-d
  content: |-
    $\dfrac12 k(C+\Delta E)^2$
- id: p10-energy-e
  content: |-
    $\Delta E$
```

---

<a id="convert-energy-to-amplitude"></a>
## Convert Energy to Amplitude

**Example:** After an event, an ideal oscillator has total mechanical energy $12\ \mathrm{J}$ and spring constant $6\ \mathrm{N/m}$. Find its new amplitude.

**Explanation**

At a turning point, the speed is zero and all the oscillator's energy is spring potential energy:

$$
E_{\mathrm{after}}=\frac12 kA_{\mathrm{new}}^2.
$$

Isolate the squared amplitude before taking the square root:

$$
\begin{aligned}
12&=\frac12(6)A_{\mathrm{new}}^2,\\
A_{\mathrm{new}}^2&=\frac{2(12)}{6}=4\ \mathrm{m}^2,\\
A_{\mathrm{new}}&=2\ \mathrm{m}.
\end{aligned}
$$

An equation for position may have positive and negative roots, but amplitude is a nonnegative distance. Therefore, use the positive square root:

$$
A_{\mathrm{new}}=\sqrt{\frac{2E_{\mathrm{after}}}{k}}.
$$

This expression requires $E_{\mathrm{after}}\geq 0$, as mechanical energy for this ideal horizontal spring oscillator cannot be negative.

```quiz
type: radio
id: p10-energy-to-amplitude
content: |-
  An ideal spring oscillator has total energy $18\ \mathrm{J}$ and spring constant $4\ \mathrm{N/m}$. What is its amplitude?
options:
- id: p10-amplitude-a
  content: |-
    $3\ \mathrm{m}$
  correct: true
- id: p10-amplitude-b
  content: |-
    $9\ \mathrm{m}$
- id: p10-amplitude-c
  content: |-
    $\sqrt{\dfrac{18}{4}}\ \mathrm{m}$
- id: p10-amplitude-d
  content: |-
    $\pm 3\ \mathrm{m}$
- id: p10-amplitude-e
  content: |-
    $6\ \mathrm{m}$
```

---

<a id="combine-the-two-relations"></a>
## Combine the Two Relations

**Example:** An ideal spring oscillator starts with amplitude $A_0$. Its mechanical energy then changes by $\Delta E$. Express the new amplitude $A_1$ in terms of $A_0$, $\Delta E$, and $k$.

**Explanation**

Write the initial energy using the initial amplitude:

$$
E_{\mathrm{before}}=\frac12 kA_0^2.
$$

Update that energy and equate it to the energy associated with the new amplitude:

$$
\frac12 kA_1^2
=\frac12 kA_0^2+\Delta E.
$$

Treat $A_0$, $\Delta E$, and $k$ as known quantities while solving for $A_1$. First clear the factor $\frac12$, then divide by $k$:

$$
\begin{aligned}
kA_1^2&=kA_0^2+2\Delta E,\\
A_1^2&=A_0^2+\frac{2\Delta E}{k}.
\end{aligned}
$$

Because amplitude is nonnegative,

$$
\boxed{A_1=\sqrt{A_0^2+\frac{2\Delta E}{k}}}.
$$

The quantity $2\Delta E/k$ has units of length squared, so it can be added to $A_0^2$.

```quiz
type: radio
id: p10-combine-relations
content: |-
  An oscillator starts with amplitude $R$ and then undergoes the energy change
  $$\Delta E=-\dfrac38 kR^2.$$
  What is its new amplitude?
options:
- id: p10-combine-a
  content: |-
    $\dfrac{R}{2}$
  correct: true
- id: p10-combine-b
  content: |-
    $\sqrt{\dfrac58}\,R$
- id: p10-combine-c
  content: |-
    $\sqrt{\dfrac{11}{8}}\,R$
- id: p10-combine-d
  content: |-
    $-\dfrac{R}{2}$
- id: p10-combine-e
  content: |-
    $R$
```

---

<a id="check-the-sign-and-physical-range"></a>
## Check the Sign and Physical Range

**Example:** A block oscillates with amplitude $A$. At $x=A/2$, an inelastic collision gives the oscillator $\Delta E=-\frac14 kA^2$. Check whether the resulting amplitude is physically reasonable.

**Explanation**

Substitute the signed energy change:

$$
\begin{aligned}
A_{\mathrm{new}}
&=\sqrt{A^2+\frac{2(-\frac14 kA^2)}{k}}\\
&=\sqrt{\frac12 A^2}
=\frac{A}{\sqrt2}.
\end{aligned}
$$

Three checks support the result:

1. Since $\Delta E<0$, the new amplitude is less than $A$.
2. The amplitude is nonnegative, so the positive root is used.
3. The block is already at $|x|=A/2$ when the collision ends, so its new amplitude cannot be smaller than $A/2$. Indeed, $A/2<A/\sqrt2<A$.

```quiz
type: radio
id: p10-original-check
content: |-
  A block of mass $M$ attached to an ideal spring of spring constant $k$ oscillates with amplitude $A$ over a frictionless horizontal surface.

  A ball of clay lands on the block while it's at $x=A/2$ (assume a conventional $x$-axis pointing to the right with $x=0$ at equilibrium) and sticks to the block's surface.

  Let $\Delta E=E_{\mathrm{after}}-E_{\mathrm{before}}$ be the mechanical-energy change found in the previous question.

  Assuming the clay's initial kinetic energy is negligible, what is the new oscillation amplitude of the spring–block–clay system?

  ![](<../Source/2026-07-23-HW-6/Images/mass-dropped-onto-spring-block.png>)
options:
- id: p10-original-a
  content: |-
    $A$
- id: p10-original-b
  content: |-
    $A/2$
- id: p10-original-c
  content: |-
    $\sqrt{A^2+\dfrac{2\Delta E}{k}}$
  correct: true
- id: p10-original-d
  content: |-
    $\sqrt{A^2-\dfrac{\Delta E}{k}}$
```

---

<a id="summary"></a>
## Summary

When an oscillator's energy changes and the spring constant stays the same:

1. Write the initial energy: $E_{\mathrm{before}}=\frac12 kA^2$.
2. Apply the signed change: $E_{\mathrm{after}}=E_{\mathrm{before}}+\Delta E$.
3. Relate the new energy to the new amplitude: $E_{\mathrm{after}}=\frac12 kA_{\mathrm{new}}^2$.
4. Solve with the nonnegative root:

$$
A_{\mathrm{new}}=\sqrt{A^2+\frac{2\Delta E}{k}}.
$$

The main trap is replacing $+\Delta E$ with $-\Delta E$. Keep the definition $\Delta E=E_{\mathrm{after}}-E_{\mathrm{before}}$ visible and substitute the sign of $\Delta E$ only once.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
