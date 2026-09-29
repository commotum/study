# Finding Maximum Speed in a Spring Oscillation

<!--
lesson-id: 212-M4-009
topic-code: MTH212.M4.09
-->

## Table of Contents

- [Introduction](#introduction)
- [Match the Two Energy States](#match-the-two-energy-states)
- [Solve for the Positive Speed](#solve-for-the-positive-speed)
- [Check Units and Scaling](#check-units-and-scaling)
- [Apply the Method to Problem 9](#apply-the-method-to-problem-9)

## Prerequisites

- Spring potential energy: $U_s=\frac12kx^2$
- Kinetic energy: $K=\frac12mv^2$
- Conservation of mechanical energy on a frictionless surface
- Solving an equation by taking a square root

---

<a id="introduction"></a>
## Introduction

For a block attached to an ideal spring on a frictionless surface, mechanical energy moves back and forth between spring potential energy and kinetic energy.

The recognition cue is a block that is released from its maximum displacement and a request for its maximum speed. At maximum displacement, the block is momentarily at rest. At equilibrium, the spring is unstretched and the block moves fastest. Equate the energies at those two positions:

$$
\frac12kA^2=\frac12mv_{\max}^2.
$$

Then solve for the nonnegative speed:

$$
v_{\max}=A\sqrt{\frac{k}{m}}.
$$

Here $A$ is the amplitude, the distance from equilibrium to the release point.

---

<a id="match-the-two-energy-states"></a>
## Match the Two Energy States

**Example:** A $2.0\ \mathrm{kg}$ block is released from rest $0.40\ \mathrm{m}$ from equilibrium on a spring with $k=50\ \mathrm{N}/\mathrm{m}$. Find its maximum speed.

**Explanation**

At the release point, $v=0$ and the energy is entirely spring potential:

$$
E=\frac12kA^2.
$$

At equilibrium, $x=0$ and the energy is entirely kinetic:

$$
E=\frac12mv_{\max}^2.
$$

Equating the two energies gives

$$
\frac12(50)(0.40)^2=\frac12(2.0)v_{\max}^2,
$$

so

$$
v_{\max}=0.40\sqrt{\frac{50}{2.0}}=2.0\ \mathrm{m}/\mathrm{s}.
$$

```quiz
type: radio
id: p9-match-energy-states
content: |-
  A $2.0\ \mathrm{kg}$ block is released from rest at amplitude $0.50\ \mathrm{m}$ on a spring with $k=18\ \mathrm{N}/\mathrm{m}$. What is its maximum speed?
options:
- id: p9-match-a
  content: |-
    $1.5\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    Use the full amplitude and equate the endpoint energies: $v_{\max}=A\sqrt{k/m}=(0.50)\sqrt{18/2.0}=1.5\ \mathrm{m}/\mathrm{s}$.
- id: p9-match-b
  content: |-
    $4.5\ \mathrm{m}/\mathrm{s}$
- id: p9-match-c
  content: |-
    $0.75\ \mathrm{m}/\mathrm{s}$
- id: p9-match-d
  content: |-
    $3.0\ \mathrm{m}/\mathrm{s}$
- id: p9-match-e
  content: |-
    $9.0\ \mathrm{m}/\mathrm{s}$
```

---

<a id="solve-for-the-positive-speed"></a>
## Solve for the Positive Speed

**Example:** Isolate $v_{\max}$ before substituting numbers.

**Explanation**

Treat $k$, $A$, and $m$ as known quantities and make $v_{\max}$ the subject of the equation. Start with the energy equation and cancel the common factor $\frac12$:

$$
\begin{aligned}
\frac12kA^2&=\frac12mv_{\max}^2\\
kA^2&=mv_{\max}^2\\
\frac{kA^2}{m}&=v_{\max}^2.
\end{aligned}
$$

Taking a square root of the equation for velocity gives the algebraic possibilities $v=\pm\sqrt{kA^2/m}$. The direction of the velocity can be positive or negative during the motion, but **speed** is its nonnegative magnitude. Since $A$ is also a nonnegative distance,

$$
v_{\max}=\sqrt{\frac{kA^2}{m}}=A\sqrt{\frac{k}{m}}.
$$

```quiz
type: radio
id: p9-isolate-speed
content: |-
  Which expression correctly solves $\frac12kA^2=\frac12mv_{\max}^2$ for the maximum speed?
options:
- id: p9-isolate-a
  content: |-
    $v_{\max}=A\sqrt{\frac{k}{m}}$
  correct: true
  feedback: |-
    First isolate $v_{\max}^2=kA^2/m$, then take the nonnegative square root. The square root changes $A^2$ into $A$.
- id: p9-isolate-b
  content: |-
    $v_{\max}=A\frac{k}{m}$
- id: p9-isolate-c
  content: |-
    $v_{\max}=\sqrt{\frac{Ak}{m}}$
- id: p9-isolate-d
  content: |-
    $v_{\max}=A^2\sqrt{\frac{k}{m}}$
- id: p9-isolate-e
  content: |-
    $v_{\max}=\frac{1}{A}\sqrt{\frac{k}{m}}$
```

---

<a id="check-units-and-scaling"></a>
## Check Units and Scaling

**Example:** Verify that $A\sqrt{k/m}$ has units of speed and use the formula to predict how mass affects the answer.

**Explanation**

Because $1\ \mathrm{N}=1\ \mathrm{kg}\,\mathrm{m}/\mathrm{s}^2$,

$$
\begin{aligned}
\left[\sqrt{\frac{k}{m}}\right]
&=\sqrt{\frac{\mathrm{N}/\mathrm{m}}{\mathrm{kg}}}\\
&=\sqrt{\frac{(\mathrm{kg}\,\mathrm{m}/\mathrm{s}^2)/\mathrm{m}}{\mathrm{kg}}}\\
&=\sqrt{\frac{1}{\mathrm{s}^2}}\\
&=\frac1{\mathrm{s}}.
\end{aligned}
$$

Multiplying by $A$ in meters gives $\mathrm{m}/\mathrm{s}$, as required. The formula also shows that $v_{\max}$ is proportional to $A$ and $\sqrt{k}$, but inversely proportional to $\sqrt{m}$.

```quiz
type: radio
id: p9-mass-scaling
content: |-
  Two spring oscillators have the same amplitude and spring constant. The second block has four times the mass of the first. How does its maximum speed compare with the first block's maximum speed?
options:
- id: p9-scale-a
  content: |-
    It is half as large.
  correct: true
  feedback: |-
    Since $v_{\max}\propto 1/\sqrt m$, multiplying the mass by $4$ multiplies the speed by $1/\sqrt4=1/2$.
- id: p9-scale-b
  content: |-
    It is one-fourth as large.
- id: p9-scale-c
  content: |-
    It is twice as large.
- id: p9-scale-d
  content: |-
    It is four times as large.
- id: p9-scale-e
  content: |-
    It is unchanged.
```

---

<a id="apply-the-method-to-problem-9"></a>
## Apply the Method to Problem 9

**Example:** A block of mass $m=0.86\ \mathrm{kg}$ on a frictionless surface is attached to an ideal spring with constant $k=78\ \mathrm{N}/\mathrm{m}$. The block is pulled $0.92\ \mathrm{m}$ from equilibrium and released. What is its maximum speed?

![](<../Source/Images/spring-block-displacement-setup.png>)

**Explanation**

The release distance is the amplitude, so $A=0.92\ \mathrm{m}$. At maximum displacement, the energy is entirely spring potential; at equilibrium, it is entirely kinetic:

$$
\frac12kA^2=\frac12mv_{\max}^2.
$$

Thus,

$$
v_{\max}=A\sqrt{\frac{k}{m}}
=(0.92\ \mathrm{m})\sqrt{\frac{78\ \mathrm{N}/\mathrm{m}}{0.86\ \mathrm{kg}}}
=8.7617\ldots\ \mathrm{m}/\mathrm{s}.
$$

Keep the unrounded calculator value until the final step. The measured givens have two significant figures, so $v_{\max}=8.8\ \mathrm{m}/\mathrm{s}$. The requested answer is a number only: **8.8**.

The answer choices diagnose common mistakes:

- $8.7617$ keeps too many digits instead of matching the givens' precision.
- $83$ comes from using $A(k/m)$ and omitting the square root.
- $4.4$ incorrectly leaves an extra factor of $\frac12$ after the halves should cancel.
- $9.6$ is approximately $\sqrt{k/m}$ and omits the amplitude $A$.

```quiz
type: radio
id: p9-source-check
content: |-
  **Question 8**

  A block of mass $m=0.86\ \mathrm{kg}$ on a frictionless surface is attached to an ideal spring with constant $k=78\ \mathrm{N}/\mathrm{m}$. The block is pulled $0.92\ \mathrm{m}$ from equilibrium and released. What is its maximum speed?

  ![](<../Source/Images/spring-block-displacement-setup.png>)

  Enter the maximum speed in meters per second as a number only:
options:
- id: p9-source-a
  content: |-
    $8.8$
  correct: true
  feedback: |-
    At maximum displacement, the energy is entirely spring potential; at equilibrium, it is entirely kinetic:

    $$
    \frac12kA^2=\frac12mv_{\max}^2.
    $$

    Thus,

    $$
    v_{\max}=A\sqrt{\frac{k}{m}}
    =(0.92\ \mathrm{m})\sqrt{\frac{78\ \mathrm{N}/\mathrm{m}}{0.86\ \mathrm{kg}}}
    =8.7617\ldots\ \mathrm{m}/\mathrm{s}.
    $$

    The measured givens have two significant figures, so $v_{\max}=8.8\ \mathrm{m}/\mathrm{s}$.
- id: p9-source-b
  content: |-
    $8.7617$
- id: p9-source-c
  content: |-
    $83$
- id: p9-source-d
  content: |-
    $4.4$
- id: p9-source-e
  content: |-
    $9.6$
```

---

## Summary

- Cue: an ideal spring-block system is released from amplitude $A$, and the maximum speed is requested.
- Match the energy at release to the energy at equilibrium: $\frac12kA^2=\frac12mv_{\max}^2$.
- Make speed the subject, then choose its nonnegative magnitude: $v_{\max}=A\sqrt{k/m}$.
- Check that the result has units of $\mathrm{m}/\mathrm{s}$ and round only after the full calculation.
- Main trap: the release distance is the full amplitude, and the square root must apply to $k/m$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
