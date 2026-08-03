# Scaling Maximum Kinetic Energy with Amplitude

<!--
lesson-id: 212-M4-017
topic-code: MTH212.M4.17
-->

## Table of Contents

- [Introduction](#introduction)
- [Connect Amplitude to Maximum Kinetic Energy](#connect-amplitude-to-maximum-kinetic-energy)
- [Square the Whole Amplitude Factor](#square-the-whole-amplitude-factor)
- [Handle a Smaller Amplitude](#handle-a-smaller-amplitude)
- [Work Backward from an Energy Factor](#work-backward-from-an-energy-factor)
- [Summary](#summary)

## Prerequisites

- The spring potential energy is $U_s=\frac12kx^2$.
- Mechanical energy is conserved for an ideal block-spring system.
- A scale factor raised to a power must be raised to that same power in a proportional formula.

---

<a id="introduction"></a>
## Introduction

When a problem keeps the same block-spring system but changes only its amplitude, look for how maximum kinetic energy depends on amplitude:

$$
K_{\max}=\frac12kA^2.
$$

For a fixed spring, $\frac12k$ is constant. In variation notation,

$$
K_{\max}\propto A^2.
$$

If the new amplitude is $A_{\text{new}}=cA_{\text{old}}$, then

$$
K_{\max,\text{new}}=c^2K_{\max,\text{old}}.
$$

The recognition cue is that the **same block-spring system** changes amplitude. Then $k$ stays fixed, so the key action is to identify the amplitude factor and **square it**. For example, doubling the amplitude multiplies $K_{\max}$ by $2^2=4$, not by $2$.

---

<a id="connect-amplitude-to-maximum-kinetic-energy"></a>
## Connect Amplitude to Maximum Kinetic Energy

At a turning point, the block is momentarily at rest, so all the mechanical energy is spring potential energy:

$$
E=\frac12kA^2.
$$

At equilibrium, the spring is unstretched and the speed is greatest, so that same energy is maximum kinetic energy:

$$
K_{\max}=E=\frac12kA^2.
$$

**Example:** A spring has $k=50\ \mathrm{N/m}$, and a block oscillates with amplitude $0.20\ \mathrm{m}$. Find its maximum kinetic energy.

**Explanation**

Substitute the amplitude into the energy formula:

$$
K_{\max}
=\frac12(50\ \mathrm{N/m})(0.20\ \mathrm{m})^2
=1.0\ \mathrm{J}.
$$

```quiz
type: radio
id: problem-2-energy-formula
content: |-
  A block oscillates on a spring with $k=40\ \mathrm{N/m}$ and amplitude $0.30\ \mathrm{m}$. What is its maximum kinetic energy?
options:
- id: p2-energy-a
  content: |-
    $0.60\ \mathrm{J}$
- id: p2-energy-b
  content: |-
    $1.2\ \mathrm{J}$
- id: p2-energy-c
  content: |-
    $1.8\ \mathrm{J}$
  correct: true
- id: p2-energy-d
  content: |-
    $3.6\ \mathrm{J}$
```

---

<a id="square-the-whole-amplitude-factor"></a>
## Square the Whole Amplitude Factor

Write the new amplitude as $A_{\text{new}}=cA_{\text{old}}$. Because the entire amplitude is squared, the power applies to both factors:

$$
A_{\text{new}}^2=(cA_{\text{old}})^2=c^2A_{\text{old}}^2.
$$

Therefore,

$$
\begin{aligned}
K_{\max,\text{new}}
&=\frac12k(cA_{\text{old}})^2 \\
&=c^2\left(\frac12kA_{\text{old}}^2\right) \\
&=c^2K_{\max,\text{old}}.
\end{aligned}
$$

**Example:** If the amplitude is tripled, then $A_{\text{new}}/A_{\text{old}}=3$. Therefore,

$$
\frac{K_{\max,\text{new}}}{K_{\max,\text{old}}}=3^2=9,
$$

so $K_{\max,\text{new}}=9K_{\max,\text{old}}$.

**Explanation**

The energy does not merely triple. Amplitude is squared in the formula, so its scale factor must also be squared.

| Amplitude factor $c$ | Maximum-kinetic-energy factor $c^2$ |
| ---: | ---: |
| $\frac13$ | $\frac19$ |
| $\frac12$ | $\frac14$ |
| $2$ | $4$ |
| $3$ | $9$ |

```quiz
type: radio
id: problem-2-doubled-amplitude
content: |-
  The maximum kinetic energy of a block in a block-spring system undergoing simple harmonic motion is $K_{\max}$.

  If the amplitude of the oscillations in the system were doubled, what would be the new maximum kinetic energy?
options:
- id: p2-double-a
  content: |-
    $2K_{\max}$
- id: p2-double-b
  content: |-
    $4K_{\max}$
  correct: true
- id: p2-double-c
  content: |-
    $K_{\max}$
- id: p2-double-d
  content: |-
    The amplitude of the oscillations cannot be doubled.
```

---

<a id="handle-a-smaller-amplitude"></a>
## Handle a Smaller Amplitude

The same square-factor rule works when the amplitude decreases.

**Example:** Suppose the amplitude is cut in half:

$$
\frac{A_{\text{new}}}{A_{\text{old}}}=\frac12.
$$

**Explanation**

Square the entire fraction:

$$
\frac{K_{\max,\text{new}}}{K_{\max,\text{old}}}
=\left(\frac12\right)^2
=\frac14.
$$

Thus, the new maximum kinetic energy is one-fourth of the original value.

```quiz
type: radio
id: problem-2-reduced-amplitude
content: |-
  The amplitude of a block-spring oscillator is reduced to one-third of its original value. What is the new maximum kinetic energy in terms of the original $K_{\max}$?
options:
- id: p2-reduce-a
  content: |-
    $\dfrac{1}{3}K_{\max}$
- id: p2-reduce-b
  content: |-
    $\dfrac{1}{6}K_{\max}$
- id: p2-reduce-c
  content: |-
    $\dfrac{1}{9}K_{\max}$
  correct: true
- id: p2-reduce-d
  content: |-
    $3K_{\max}$
- id: p2-reduce-e
  content: |-
    $9K_{\max}$
```

---

<a id="work-backward-from-an-energy-factor"></a>
## Work Backward from an Energy Factor

Sometimes the energy factor is given and the amplitude factor is unknown. Since

$$
\text{energy factor}=(\text{amplitude factor})^2,
$$

use two steps:

1. Set $c^2$ equal to the energy factor.
2. Take the positive square root to find the amplitude factor $c$.

An equation such as $c^2=16$ has algebraic solutions $c=\pm4$, but an amplitude is a nonnegative magnitude. Therefore, the physical scale factor is $c=4$.

**Example:** If the new maximum kinetic energy is $16$ times the old maximum kinetic energy, then

$$
\left(\frac{A_{\text{new}}}{A_{\text{old}}}\right)^2=16
\quad\Longrightarrow\quad
\frac{A_{\text{new}}}{A_{\text{old}}}=4.
$$

**Explanation**

The amplitude is four times as large because $4^2=16$.

```quiz
type: radio
id: problem-2-inverse-scaling
content: |-
  A block-spring oscillator's new maximum kinetic energy is $\dfrac{1}{25}$ of its original maximum kinetic energy. What is the new amplitude in terms of the original amplitude $A$?
options:
- id: p2-inverse-a
  content: |-
    $\dfrac{1}{25}A$
- id: p2-inverse-b
  content: |-
    $\dfrac{1}{10}A$
- id: p2-inverse-c
  content: |-
    $\dfrac{1}{5}A$
  correct: true
- id: p2-inverse-d
  content: |-
    $5A$
- id: p2-inverse-e
  content: |-
    $25A$
```

---

<a id="summary"></a>
## Summary

When the same spring is used, $k$ is fixed and $K_{\max}\propto A^2$. If only the amplitude changes:

1. Start with $K_{\max}=\frac12kA^2$.
2. Find the amplitude factor $c=A_{\text{new}}/A_{\text{old}}$.
3. Square the **whole** factor: $(cA)^2=c^2A^2$.
4. Apply $K_{\max,\text{new}}=c^2K_{\max,\text{old}}$.
5. For an inverse question, solve $c^2=$ energy factor and keep the positive root.

The main trap is using $c$ instead of $c^2$. Doubling the amplitude makes the maximum kinetic energy four times as large.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
