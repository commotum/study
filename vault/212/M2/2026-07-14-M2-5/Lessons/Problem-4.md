# Mechanical Energy Lost When Rotating Cups Capture Rain

<!--
lesson-id: 212-M2-034
topic-code: MTH212.M2.34
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Post-Capture Rotation](#find-the-post-capture-rotation)
- [Compare Initial and Final Kinetic Energy](#compare-initial-and-final-kinetic-energy)
- [Derive the Energy-Loss Formula](#derive-the-energy-loss-formula)
- [Apply the Method to Problem 4](#apply-the-method-to-problem-4)

## Prerequisites

- Angular momentum: $L=I\omega$
- Rotational kinetic energy: $K=\frac12I\omega^2$
- Point-mass moment of inertia: $I=mr^2$
- Conservation of angular momentum when external torque is negligible

---

<a id="introduction"></a>
## Introduction

Capturing rain is an inelastic process. With negligible external torque, angular momentum is conserved, but mechanical energy is not. First use angular momentum to determine the final angular speed, then subtract the final rotational kinetic energy from the initial rotational kinetic energy:

$$
\Delta E_{\mathrm{lost}}=K_i-K_f.
$$

The recognition cue is mass being captured by a rotating system at a fixed radius, followed by a request for energy lost. Because $K=\frac12I\omega^2$, any change in angular speed must be **squared** when comparing energies.

---

<a id="find-the-post-capture-rotation"></a>
## Find the Post-Capture Rotation

**Example:** Each of two identical cups captures water equal to its own mass while remaining at the same radius. Find the changes in moment of inertia and angular speed.

**Explanation**

At fixed radius, doubling each rotating mass doubles the total moment of inertia:

$$
I_f=2I_i.
$$

Conserve angular momentum and make $\omega_f$ the subject:

$$
\begin{aligned}
I_i\omega_0&=I_f\omega_f\\
\omega_f&=\frac{I_i}{I_f}\omega_0\\
&=\frac12\omega_0.
\end{aligned}
$$

The increase in $I$ and the decrease in $\omega$ are reciprocal changes.

```quiz
type: radio
id: p4-post-capture-state
content: |-
  A rotating system captures mass at a fixed radius, causing its moment of inertia to become $3I_i$. External torque is negligible. What is its final angular speed?
options:
- id: p4-state-a
  content: |-
    $\omega_f=\dfrac13\omega_i$
  correct: true
  feedback: |-
    From $I_i\omega_i=I_f\omega_f$, increasing $I$ by a factor of $3$ decreases $\omega$ by the reciprocal factor: $\omega_f=\omega_i/3$.
- id: p4-state-b
  content: |-
    $\omega_f=3\omega_i$
- id: p4-state-c
  content: |-
    $\omega_f=\dfrac19\omega_i$
- id: p4-state-d
  content: |-
    $\omega_f=\sqrt3\omega_i$
- id: p4-state-e
  content: |-
    $\omega_f=\omega_i$
```

---

<a id="compare-initial-and-final-kinetic-energy"></a>
## Compare Initial and Final Kinetic Energy

**Example:** If $I_f=2I_i$ and $\omega_f=\omega_0/2$, what fraction of the initial rotational kinetic energy remains?

**Explanation**

Use a ratio so the common factors cancel:

$$
\begin{aligned}
\frac{K_f}{K_i}
&=\frac{\frac12I_f\omega_f^2}{\frac12I_i\omega_0^2}\\
&=\frac{I_f}{I_i}\left(\frac{\omega_f}{\omega_0}\right)^2\\
&=2\left(\frac12\right)^2\\
&=\frac12.
\end{aligned}
$$

Half the initial kinetic energy remains, so half is lost from mechanical energy:

$$
\Delta E_{\mathrm{lost}}
=K_i-K_f
=\frac12K_i.
$$

Equivalently, the percentage loss is

$$
\frac{K_i-K_f}{K_i}\times100\%
=\frac12\times100\%
=50\%.
$$

The lost mechanical energy is converted to internal energy and other nonmechanical forms during the capture.

```quiz
type: radio
id: p4-energy-fraction
content: |-
  Angular momentum is conserved while a system's moment of inertia becomes $4I_i$, so its angular speed becomes $\omega_i/4$. What fraction of the initial rotational kinetic energy remains?
options:
- id: p4-fraction-a
  content: |-
    $\dfrac14$
  correct: true
  feedback: |-
    $K_f/K_i=(I_f/I_i)(\omega_f/\omega_i)^2=4(1/4)^2=1/4$. The angular-speed factor must be squared.
- id: p4-fraction-b
  content: |-
    $\dfrac12$
- id: p4-fraction-c
  content: |-
    $\dfrac1{16}$
- id: p4-fraction-d
  content: |-
    $4$
- id: p4-fraction-e
  content: |-
    $1$
```

---

<a id="derive-the-energy-loss-formula"></a>
## Derive the Energy-Loss Formula

**Example:** Express the energy lost in terms of one cup's mass $m$, the rod length $d$, and the initial angular speed $\omega_0$.

**Explanation**

Each cup is at radius $d/2$, so the two initial cups have moment of inertia

$$
I_i=2m\left(\frac d2\right)^2=\frac{md^2}{2}.
$$

The initial rotational kinetic energy is

$$
K_i=\frac12I_i\omega_0^2
=\frac{md^2\omega_0^2}{4}.
$$

The capture loses half of this initial kinetic energy:

$$
\Delta E_{\mathrm{lost}}
=\frac12K_i
=\frac{md^2\omega_0^2}{8}.
$$

The units check:

$$
[m d^2\omega_0^2]
=\mathrm{kg\,m^2/s^2}
=\mathrm J.
$$

For numerical work, square $d$ and $\omega_0$ first, then multiply by $m$ and divide by $8$.

```quiz
type: radio
id: p4-loss-formula
content: |-
  Two cups, each of mass $m$, lie at the ends of a negligible-mass rod of length $d$. Each captures an additional mass $m$ while the system rotates initially at $\omega_0$. Which expression gives the mechanical energy lost?
options:
- id: p4-formula-a
  content: |-
    $\Delta E_{\mathrm{lost}}=\dfrac{md^2\omega_0^2}{8}$
  correct: true
  feedback: |-
    First $I_i=md^2/2$, then $K_i=\frac12I_i\omega_0^2=md^2\omega_0^2/4$. Since half remains, the other half is lost: $\Delta E_{\mathrm{lost}}=md^2\omega_0^2/8$.
- id: p4-formula-b
  content: |-
    $\Delta E_{\mathrm{lost}}=\dfrac{md^2\omega_0^2}{4}$
- id: p4-formula-c
  content: |-
    $\Delta E_{\mathrm{lost}}=\dfrac{md\omega_0^2}{8}$
- id: p4-formula-d
  content: |-
    $\Delta E_{\mathrm{lost}}=\dfrac{md^2\omega_0}{8}$
- id: p4-formula-e
  content: |-
    $\Delta E_{\mathrm{lost}}=2md^2\omega_0^2$
```

---

<a id="apply-the-method-to-problem-4"></a>
## Apply the Method to Problem 4

**Example:** For the same rotating cups, how much mechanical energy is lost when each cup of mass $m$ captures a water mass $m$? Use $m=0.46\ \mathrm{kg}$, $d=0.68\ \mathrm{m}$, and $\omega_0=4.2\ \mathrm{rad/s}$.

![](<../Source/Images/rotating-cups-collecting-rain.png>)

**Explanation**

The initial moment of inertia is $I_i=md^2/2$. After the capture, $I_f=2I_i$ and angular momentum conservation gives $\omega_f=\omega_0/2$. Therefore,

$$
\Delta E_{\mathrm{lost}}
=\frac12I_i\omega_0^2-\frac12I_f\omega_f^2
=\frac14I_i\omega_0^2
=\frac{md^2\omega_0^2}{8}.
$$

Substitution gives

$$
\Delta E_{\mathrm{lost}}
=\frac{(0.46)(0.68)^2(4.2)^2}{8}
=0.4689\ldots\ \mathrm{J}.
$$

The measured givens have two significant figures, so $\Delta E_{\mathrm{lost}}=0.47\ \mathrm{J}$.

The answer choices diagnose common mistakes:

- $0.94$ is the initial rotational kinetic energy, not the energy lost.
- $0.23$ applies an extra factor of $\frac12$ after the loss has already been halved.
- $2.1$ is the final angular speed from the previous problem, not an energy.
- $4.2$ is the initial angular speed, also not an energy.

```quiz
type: radio
id: p4-source-check
content: |-
  **Question 3**

  For the same rotating cups, how much mechanical energy is lost when each cup of mass $m$ captures a water mass $m$? Use $m=0.46\ \mathrm{kg}$, $d=0.68\ \mathrm{m}$, and $\omega_0=4.2\ \mathrm{rad/s}$.

  ![](<../Source/Images/rotating-cups-collecting-rain.png>)

  Enter the energy lost in joules as a number only:
options:
- id: p4-source-a
  content: |-
    $0.47$
  correct: true
  feedback: |-
    The initial moment of inertia is $I_i=md^2/2$. After the capture, $I_f=2I_i$ and angular momentum conservation gives $\omega_f=\omega_0/2$. Therefore,

    $$
    \Delta E_{\mathrm{lost}}
    =\frac12I_i\omega_0^2-\frac12I_f\omega_f^2
    =\frac14I_i\omega_0^2
    =\frac{md^2\omega_0^2}{8}.
    $$

    Substitution gives

    $$
    \Delta E_{\mathrm{lost}}
    =\frac{(0.46)(0.68)^2(4.2)^2}{8}
    =0.4689\ldots\ \mathrm{J}.
    $$

    The measured givens have two significant figures, so $\Delta E_{\mathrm{lost}}=0.47\ \mathrm{J}$.
- id: p4-source-b
  content: |-
    $0.94$
- id: p4-source-c
  content: |-
    $0.23$
- id: p4-source-d
  content: |-
    $2.1$
- id: p4-source-e
  content: |-
    $4.2$
```

---

## Summary

- Cue: a rotating system captures mass at fixed radius, and the mechanical energy lost is requested.
- Conserve angular momentum first to find the final angular speed.
- Compare energies with $K_f/K_i=(I_f/I_i)(\omega_f/\omega_i)^2$.
- For equal captured and cup masses, $I_f=2I_i$, $\omega_f=\omega_0/2$, and $50\%$ of $K_i$ is lost.
- Use $\Delta E_{\mathrm{lost}}=md^2\omega_0^2/8$ and round only after substitution.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
