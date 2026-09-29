# Why a Pendulum Becomes Simple Harmonic Motion

<!--
lesson-id: 212-M4-030
topic-code: MTH212.M4.30
-->

## Table of Contents

- [Introduction](#introduction)
- [Read Gravity's Torque as Restoring](#read-gravitys-torque-as-restoring)
- [Linearize the Torque at Small Angles](#linearize-the-torque-at-small-angles)
- [Match the Equation to SHM](#match-the-equation-to-shm)
- [Convert the SHM Coefficient into a Period](#convert-the-shm-coefficient-into-a-period)
- [Specialize to a Simple Pendulum and Check the Model](#specialize-to-a-simple-pendulum-and-check-the-model)
- [Summary](#summary)

## Prerequisites

- Use rotational dynamics in the form $\sum\tau=I\alpha$, with $\alpha=\ddot\theta$.
- Recognize $\ell$ as the distance from the pivot to the center of mass and $I$ as the moment of inertia about the pivot.
- Recognize the SHM form $\ddot\theta+\omega^2\theta=0$ and use $T=2\pi/\omega$.
- Evaluate sine when an angle is measured in radians.

---

<a id="introduction"></a>
## Introduction

Let $\theta$ measure angular displacement from the downward equilibrium position, with a positive direction chosen once. A pendulum is not automatically a simple harmonic oscillator. Its exact gravitational torque contains $\sin\theta$, so its exact equation of motion is nonlinear. The SHM model appears only when the angular displacement is small enough that $\sin\theta\approx\theta$, with $\theta$ measured in radians.

The reusable chain is

$$
\tau=-Mg\ell\sin\theta
\;\longrightarrow\;
\tau\approx-Mg\ell\theta
\;\longrightarrow\;
\ddot\theta+\frac{Mg\ell}{I}\theta=0.
$$

The recognition cue is a pendulum oscillating through **small angles** about a **fixed pivot**. The move is to establish the restoring sign, linearize the sine, and then match the coefficient of $\theta$ to $\omega^2$.

---

<a id="read-gravitys-torque-as-restoring"></a>
## Read Gravity's Torque as Restoring

**Example:** A physical pendulum is displaced to a positive angle, $\theta>0$. What is the sign of the gravitational torque about the pivot?

**Explanation**

The support force acts through the pivot, so it produces no torque about that point. Gravity acts at the center of mass, a distance $\ell$ from the pivot, and its tangential component has magnitude $Mg\sin\theta$. Therefore,

$$
\tau=-Mg\ell\sin\theta.
$$

For $\theta>0$, we have $\sin\theta>0$, so $\tau<0$. For $\theta<0$, the sine and the torque reverse signs. In both cases, the torque points back toward $\theta=0$; that is what the minus sign means.

```quiz
type: radio
id: m4-pendulum-q1
content: |-
  A physical pendulum is at an angle $\theta<0$. What is the sign of the gravitational torque about the pivot?
options:
- id: m4-pendulum-q1-a
  content: |-
    $\tau>0$
  correct: true
  feedback: |-
    A restoring torque must point toward $\theta=0$. From $\tau=-Mg\ell\sin\theta$, a negative angle has $\sin\theta<0$, so the leading minus sign makes $\tau>0$.
- id: m4-pendulum-q1-b
  content: |-
    $\tau<0$
  feedback: |-
    This makes the torque have the same sign as the negative displacement, which would drive the pendulum farther from equilibrium. The restoring relation has the opposite sign: when $\theta<0$, $\tau>0$.
- id: m4-pendulum-q1-c
  content: |-
    $\tau=0$
  feedback: |-
    Gravity's torque is zero only at equilibrium, where $\theta=0$ and $\sin\theta=0$. A nonzero negative displacement gives a nonzero positive restoring torque.
- id: m4-pendulum-q1-d
  content: |-
    The sign cannot be known without the angular velocity.
  feedback: |-
    Angular velocity describes the current direction of motion, but displacement determines the restoring torque. The sign follows from $-\sin\theta$, so $\theta<0$ gives $\tau>0$ regardless of the current angular velocity.
- id: m4-pendulum-q1-e
  content: |-
    The support force determines the sign.
  feedback: |-
    The support force's line of action passes through the pivot, so its lever arm about the pivot is zero. Gravity supplies the torque, and $-Mg\ell\sin\theta$ is positive when $\theta<0$.
```

---

<a id="linearize-the-torque-at-small-angles"></a>
## Linearize the Torque at Small Angles

**Example:** Rewrite the gravitational torque for a pendulum whose angle remains near $\theta=0$.

**Explanation**

Near zero, the sine function is almost its tangent line:

$$
\sin\theta\approx\theta
\qquad\text{for small $|\theta|$, with $\theta$ in radians.}
$$

For example, $\sin(0.10)=0.0998\ldots$, which is close to $0.10$. Substituting this local approximation into the exact torque gives

$$
\tau=-Mg\ell\sin\theta
\approx-Mg\ell\theta.
$$

The important change is structural: the approximate torque is proportional to $\theta$. At larger amplitudes, $\sin\theta$ is not close enough to $\theta$, and the exact pendulum is not an ideal SHM system.

```quiz
type: radio
id: m4-pendulum-q2
content: |-
  A pendulum remains near $\theta=0$, with angles measured in radians. Which torque is used in the small-angle SHM model?
options:
- id: m4-pendulum-q2-a
  content: |-
    $\tau\approx-Mg\ell\theta$
  correct: true
  feedback: |-
    Near zero in radians, $\sin\theta\approx\theta$. Replacing the sine in $\tau=-Mg\ell\sin\theta$ therefore gives the linear restoring torque $\tau\approx-Mg\ell\theta$.
- id: m4-pendulum-q2-b
  content: |-
    $\tau\approx+Mg\ell\theta$
  feedback: |-
    The small-angle approximation replaces $\sin\theta$ by $\theta$ but does not remove the restoring minus sign. A positive sign would make the torque push in the same direction as the displacement.
- id: m4-pendulum-q2-c
  content: |-
    $\tau=-Mg\ell\sin\theta$
  feedback: |-
    This is the exact gravitational torque, but it still contains the nonlinear sine. The small-angle SHM model makes the additional replacement $\sin\theta\approx\theta$.
- id: m4-pendulum-q2-d
  content: |-
    $\tau\approx-\dfrac{Mg\ell}{\theta}$
  feedback: |-
    Small-angle linearization does not invert the angle. Near zero, $\sin\theta$ approaches $\theta$, so the torque is proportional to $\theta$, not to $1/\theta$.
- id: m4-pendulum-q2-e
  content: |-
    $\tau\approx-Mg\ell\theta^2$
  feedback: |-
    The first-order behavior of $\sin\theta$ near zero is linear, not quadratic. Using $\theta^2$ would also lose the sign change that makes the torque restoring on both sides of equilibrium.
```

---

<a id="match-the-equation-to-shm"></a>
## Match the Equation to SHM

**Example:** A physical pendulum has mass $M=0.80\ \mathrm{kg}$, center-of-mass distance $\ell=0.25\ \mathrm{m}$, and pivot moment of inertia $I=0.060\ \mathrm{kg}\,\mathrm{m}^2$. Find its small-angle angular frequency.

**Explanation**

Start with rotational dynamics and the linearized torque:

$$
I\ddot\theta=-Mg\ell\theta.
$$

Divide by $I$ and place every term on the left:

$$
\ddot\theta+\frac{Mg\ell}{I}\theta=0.
$$

Now compare coefficient-for-coefficient with

$$
\ddot\theta+\omega^2\theta=0.
$$

Thus,

$$
\omega^2=\frac{Mg\ell}{I},
\qquad
\omega=\sqrt{\frac{Mg\ell}{I}}.
$$

For this pendulum,

$$
\omega
=\sqrt{\frac{(0.80)(9.81)(0.25)}{0.060}}
=5.72\ \mathrm{rad}/\mathrm{s}.
$$

The coefficient $Mg\ell/I$ has units of $\mathrm{s}^{-2}$; taking its square root produces an angular frequency in $\mathrm{rad}/\mathrm{s}$.

```quiz
type: radio
id: m4-pendulum-q3
content: |-
  A physical pendulum has $M=0.60\ \mathrm{kg}$, $\ell=0.20\ \mathrm{m}$, and $I=0.048\ \mathrm{kg}\,\mathrm{m}^2$. Using $g=9.8\ \mathrm{m}/\mathrm{s}^2$, what is its small-angle angular frequency?
options:
- id: m4-pendulum-q3-a
  content: |-
    $4.95\ \mathrm{rad}/\mathrm{s}$
  correct: true
  feedback: |-
    Matching $\ddot\theta+(Mg\ell/I)\theta=0$ to SHM gives $\omega=\sqrt{Mg\ell/I}$. Here $Mg\ell/I=24.5\ \mathrm{s}^{-2}$, so $\omega=\sqrt{24.5}=4.95\ \mathrm{rad}/\mathrm{s}$.
- id: m4-pendulum-q3-b
  content: |-
    $24.5\ \mathrm{rad}/\mathrm{s}$
  feedback: |-
    The value $24.5\ \mathrm{s}^{-2}$ is the coefficient identified as $\omega^2$, not $\omega$. Taking the square root gives $\omega=4.95\ \mathrm{rad}/\mathrm{s}$.
- id: m4-pendulum-q3-c
  content: |-
    $0.202\ \mathrm{rad}/\mathrm{s}$
  feedback: |-
    This is $1/\sqrt{24.5}$, but matching the equation gives $\omega^2=24.5\ \mathrm{s}^{-2}$, not $1/\omega^2=24.5\ \mathrm{s}^{-2}$. The required frequency is $\sqrt{24.5}=4.95\ \mathrm{rad}/\mathrm{s}$.
- id: m4-pendulum-q3-d
  content: |-
    $0.0408\ \mathrm{rad}/\mathrm{s}$
  feedback: |-
    The ratio $I/(Mg\ell)=0.0408\ \mathrm{s}^2$ is the inverse of $\omega^2$ and does not itself have frequency units. Invert the ratio and take the square root to obtain $4.95\ \mathrm{rad}/\mathrm{s}$.
- id: m4-pendulum-q3-e
  content: |-
    $3.13\ \mathrm{rad}/\mathrm{s}$
  feedback: |-
    This is approximately $\sqrt{g}$ and ignores the pendulum's inertia and center-of-mass lever arm. Physical-pendulum frequency depends on the full ratio $Mg\ell/I$, which gives $4.95\ \mathrm{rad}/\mathrm{s}$ here.
```

---

<a id="convert-the-shm-coefficient-into-a-period"></a>
## Convert the SHM Coefficient into a Period

**Example:** A pendulum's small-angle equation is $\ddot\theta+16\theta=0$. Find its period.

**Explanation**

The coefficient of $\theta$ is $\omega^2$, so

$$
\omega^2=16\ \mathrm{s}^{-2},
\qquad
\omega=4\ \mathrm{rad}/\mathrm{s}.
$$

One cycle spans $2\pi$ radians of phase, so

$$
T=\frac{2\pi}{\omega}
=\frac{2\pi}{4}
=1.57\ \mathrm{s}.
$$

Applying the same two steps to a physical pendulum gives

$$
T=2\pi\sqrt{\frac{I}{Mg\ell}}.
$$

```quiz
type: radio
id: m4-pendulum-q4
content: |-
  A pendulum's small-angle equation is $\ddot\theta+9\theta=0$. What is its period?
options:
- id: m4-pendulum-q4-a
  content: |-
    $2.09\ \mathrm{s}$
  correct: true
  feedback: |-
    The SHM coefficient is $\omega^2=9\ \mathrm{s}^{-2}$, so $\omega=3\ \mathrm{rad}/\mathrm{s}$. Therefore $T=2\pi/\omega=2\pi/3=2.09\ \mathrm{s}$.
- id: m4-pendulum-q4-b
  content: |-
    $3.00\ \mathrm{s}$
  feedback: |-
    The square root gives $\omega=3\ \mathrm{rad}/\mathrm{s}$, which is an angular frequency, not a period. Convert frequency to a cycle time with $T=2\pi/\omega$, giving $2.09\ \mathrm{s}$.
- id: m4-pendulum-q4-c
  content: |-
    $0.333\ \mathrm{s}$
  feedback: |-
    This uses $1/\omega$ and omits the $2\pi$ radians in one full cycle. Angular frequency is in radians per second, so the period is $2\pi/3=2.09\ \mathrm{s}$.
- id: m4-pendulum-q4-d
  content: |-
    $18.85\ \mathrm{s}$
  feedback: |-
    This multiplies $2\pi$ by $\omega$, but faster angular frequency must produce a shorter period. The inverse relationship is $T=2\pi/\omega=2.09\ \mathrm{s}$.
- id: m4-pendulum-q4-e
  content: |-
    $0.698\ \mathrm{s}$
  feedback: |-
    This uses the coefficient $9=\omega^2$ directly in $2\pi/9$. First take the square root to get $\omega=3\ \mathrm{rad}/\mathrm{s}$, then compute $T=2\pi/3=2.09\ \mathrm{s}$.
```

---

<a id="specialize-to-a-simple-pendulum-and-check-the-model"></a>
## Specialize to a Simple Pendulum and Check the Model

**Example:** Reduce the physical-pendulum period to the simple-pendulum result for a point mass $m$ on a massless string of length $L$.

**Explanation**

For the point mass,

$$
I=mL^2,
\qquad
\ell=L.
$$

Substituting these into the physical-pendulum result gives

$$
T
=2\pi\sqrt{\frac{mL^2}{mgL}}
=2\pi\sqrt{\frac{L}{g}}.
$$

The mass cancels. The release angle also does not appear in this formula, but that does **not** make the formula exact at every amplitude: the small release angle is the condition that allowed $\sin\theta$ to be replaced by $\theta$.

Use this SHM model when the angle stays small in radians, the pivot is fixed, and damping or driving is negligible. If the angle is large, return to the exact torque $-Mg\ell\sin\theta$ rather than forcing it into the linear SHM form.

```quiz
type: radio
id: m4-pendulum-q5
content: |-
  Which statement correctly specializes the derivation to a simple pendulum and states the model's scope?
options:
- id: m4-pendulum-q5-a
  content: |-
    Since $I=mL^2$ and $\ell=L$, $T=2\pi\sqrt{L/g}$ for small-angle motion about a fixed pivot with negligible damping.
  correct: true
  feedback: |-
    Substituting $I=mL^2$ and $\ell=L$ cancels the mass and one factor of $L$, giving $T=2\pi\sqrt{L/g}$. The result inherits the small-angle, fixed-pivot, negligible-damping assumptions used in the SHM derivation.
- id: m4-pendulum-q5-b
  content: |-
    Since $I=mL^2$ and $\ell=L$, $T=2\pi\sqrt{mL/g}$ for small-angle motion.
  feedback: |-
    The mass appears in both $I=mL^2$ and the restoring factor $mgL$, so it cancels. Keeping $m$ would incorrectly predict different periods for equal-length pendulums with different bob masses.
- id: m4-pendulum-q5-c
  content: |-
    Since $I=mL^2$ and $\ell=L$, $T=2\pi\sqrt{L/g}$ exactly for every release angle.
  feedback: |-
    The algebraic specialization is correct, but its claimed scope is not. The formula came from $\sin\theta\approx\theta$, so it is an SHM approximation for small angular amplitudes rather than an exact all-amplitude result.
- id: m4-pendulum-q5-d
  content: |-
    Since $I=mL$, the period is independent of the small-angle approximation.
  feedback: |-
    A point mass a distance $L$ from the pivot has $I=mL^2$, not $mL$; the latter does not even have moment-of-inertia units. The period formula also still depends on the small-angle linearization.
- id: m4-pendulum-q5-e
  content: |-
    Since $I=mL^2$ and $\ell=L$, $T=2\pi\sqrt{g/L}$ for small-angle motion.
  feedback: |-
    The ratio is inverted. A period must have time units, and $\sqrt{L/g}$ has units of seconds, whereas $\sqrt{g/L}$ has units of inverse seconds and belongs to angular frequency.
```

---

## Summary

When a pendulum problem asks why the motion is SHM or asks you to derive its frequency or period:

1. Take torques about the pivot: the support contributes none, and gravity gives $\tau=-Mg\ell\sin\theta$.
2. Check the condition: for small $|\theta|$ measured in radians, use $\sin\theta\approx\theta$.
3. Apply rotational dynamics: $I\ddot\theta=-Mg\ell\theta$.
4. Match forms: $\ddot\theta+(Mg\ell/I)\theta=0$ implies $\omega^2=Mg\ell/I$.
5. Convert only after matching: $\omega=\sqrt{Mg\ell/I}$ and $T=2\pi\sqrt{I/(Mg\ell)}$.

For a simple pendulum, $I=mL^2$ and $\ell=L$, so $T=2\pi\sqrt{L/g}$. The main trap is treating this result as exact at large angles; without the small-angle linearization, the exact sine torque is nonlinear and the motion is not ideal SHM.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
