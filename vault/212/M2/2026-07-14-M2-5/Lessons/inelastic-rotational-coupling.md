# Shared Angular Speed After Inelastic Rotational Coupling

<!--
lesson-id: 212-M2-053
topic-code: MTH212.M2.53
-->

## Table of Contents

- [Introduction](#introduction)
- [Conserve Angular Momentum, Not Kinetic Energy](#conserve-angular-momentum-not-kinetic-energy)
- [Build the General Coupling Ratio](#build-the-general-coupling-ratio)
- [Insert the Correct Shape Inertias](#insert-the-correct-shape-inertias)
- [Apply the Ratio to the Ring and Cylinder](#apply-the-ratio-to-the-ring-and-cylinder)
- [Summary](#summary)

## Prerequisites

- Use $L=I\omega$ for rotation about a fixed axis.
- Recognize $I_{\text{cyl}}=\tfrac12Mr^2$ for a uniform solid cylinder and $I_{\text{ring}}=mr^2$ for a thin ring.
- Factor and simplify symbolic expressions containing fractions.

---

<a id="introduction"></a>
## Introduction

When two coaxial objects couple through friction and then rotate together, the recognition cues are **one shared final angular speed** and **negligible net external torque about the axle**. Friction between the objects is internal to the chosen system, so total angular momentum is conserved even though rotational kinetic energy generally is not.

Organize the two states before writing the conservation equation:

| Body | Initial angular speed | Final angular speed |
|---|---:|---:|
| Initially spinning body | $\omega_{1i}$ | $\omega_f$ |
| Added body | $\omega_{2i}$, often $0$ | $\omega_f$ |

For two objects,

$$
L_i=I_1\omega_{1i}+I_2\omega_{2i},
$$

and after they rotate together,

$$
L_f=(I_1+I_2)\omega_f.
$$

Equating these gives the reusable coupling formula

$$
\omega_f=\frac{I_1\omega_{1i}+I_2\omega_{2i}}{I_1+I_2}.
$$

If object 2 is initially at rest, then $\omega_{2i}=0$ and

$$
\omega_f=\frac{I_1}{I_1+I_2}\omega_{1i}.
$$

Use this sequence: identify which bodies initially carry angular momentum, add every final moment of inertia, isolate $\omega_f$, and only then substitute the shape formulas for $I$.

---

<a id="conserve-angular-momentum-not-kinetic-energy"></a>
## Conserve Angular Momentum, Not Kinetic Energy

**Example:** Rotor A spins at $\omega_0$. Coaxial rotor B is initially at rest, then friction makes the two rotate together. Which conservation equation determines their shared angular speed when external torque about the axle is negligible?

**Explanation**

Initially, only rotor A contributes angular momentum:

$$
L_i=I_A\omega_0+I_B(0)=I_A\omega_0.
$$

Finally, both rotors share $\omega_f$, so

$$
L_f=(I_A+I_B)\omega_f.
$$

The correct equation is therefore

$$
I_A\omega_0=(I_A+I_B)\omega_f.
$$

An equation that sets the initial and final rotational kinetic energies equal would describe an elastic energy-conserving process, not frictional sticking.

```quiz
type: radio
id: choose-rotational-coupling-equation
shuffle: true
content: |-
  A spinning disk with moment of inertia $I_d$ and initial angular speed $\omega_0$ couples to an initially stationary coaxial ring with moment of inertia $I_r$. They rotate together, and external torque about the axle is negligible. Which equation correctly relates the initial and final states?
options:
- id: angular-momentum-equation
  content: |-
    $I_d\omega_0=(I_d+I_r)\omega_f$
  correct: true
  feedback: |-
    Negligible external torque conserves total angular momentum. Only the disk rotates initially, while both disk and ring rotate finally, so $I_d\omega_0=(I_d+I_r)\omega_f$.
- id: kinetic-energy-equation
  content: |-
    $\tfrac12I_d\omega_0^2=\tfrac12(I_d+I_r)\omega_f^2$
  feedback: |-
    This equation conserves rotational kinetic energy. Frictional coupling is inelastic and converts some mechanical energy to thermal energy, while angular momentum—not kinetic energy—is conserved when external torque is negligible.
- id: ring-only-final
  content: |-
    $I_d\omega_0=I_r\omega_f$
  feedback: |-
    The ring contributes to the final inertia, but the disk does not disappear after coupling. Both bodies rotate together, so the final angular momentum uses $(I_d+I_r)\omega_f$.
- id: both-rotating-initially
  content: |-
    $(I_d+I_r)\omega_0=(I_d+I_r)\omega_f$
  feedback: |-
    This assigns the initial angular speed $\omega_0$ to the ring even though it starts at rest. Initially only the disk contributes $I_d\omega_0$; the summed inertia belongs to the shared final state.
- id: disk-only-throughout
  content: |-
    $I_d\omega_0=I_d\omega_f$
  feedback: |-
    This omits the ring from the final rotating system. Once the ring couples to the disk, its moment of inertia must be included in $I_f=I_d+I_r$.
```

---

<a id="build-the-general-coupling-ratio"></a>
## Build the General Coupling Ratio

**Example:** Rotor B is initially at rest and has moment of inertia $I_B=2I_A$. Rotor A starts at angular speed $\omega_0$. Find the shared final angular speed.

**Explanation**

Conserve angular momentum and substitute the inertia relation:

$$
I_A\omega_0=(I_A+2I_A)\omega_f
=3I_A\omega_f.
$$

Cancel $I_A$ and isolate the target:

$$
\omega_f=\frac13\omega_0.
$$

Because the initially stationary rotor adds positive inertia, the multiplier $I_A/(I_A+I_B)$ must lie between $0$ and $1$.

```quiz
type: radio
id: coupling-from-inertia-ratio
shuffle: true
content: |-
  Rotor A starts at $\omega_0$. Coaxial rotor B is initially at rest and has $I_B=3I_A$. After inelastic coupling, what is their shared angular speed?
options:
- id: omega-quarter
  content: |-
    $\omega_f=\dfrac{\omega_0}{4}$
  correct: true
  feedback: |-
    Angular momentum conservation gives $I_A\omega_0=(I_A+3I_A)\omega_f=4I_A\omega_f$. Canceling $I_A$ yields $\omega_f=\omega_0/4$.
- id: omega-third
  content: |-
    $\omega_f=\dfrac{\omega_0}{3}$
  feedback: |-
    The factor $3$ describes rotor B alone. The final system contains both rotors, so its inertia is $I_A+3I_A=4I_A$, making the final speed $\omega_0/4$.
- id: three-omega
  content: |-
    $\omega_f=3\omega_0$
  feedback: |-
    Adding an initially stationary rotor increases the rotating inertia without adding initial angular momentum. The shared speed must decrease, so a multiplier greater than $1$ fails the physical bound.
- id: four-omega
  content: |-
    $\omega_f=4\omega_0$
  feedback: |-
    The fourfold factor belongs to the final inertia $I_A+I_B=4I_A$. To keep angular momentum fixed, angular speed takes the reciprocal factor $1/4$.
- id: omega-same
  content: |-
    $\omega_f=\omega_0$
  feedback: |-
    Angular speed would remain unchanged only if no additional moment of inertia joined the motion. Here rotor B adds $3I_A$, so the shared speed must fall to $\omega_0/4$.
```

---

<a id="insert-the-correct-shape-inertias"></a>
## Insert the Correct Shape Inertias

**Example:** A uniform solid cylinder of mass $4m$ and radius $r$ spins at $\omega_0$. An initially stationary thin ring of mass $m$ and radius $r$ couples to it. Find the shared angular speed.

**Explanation**

Use the moment of inertia for each shape about the common symmetry axis:

$$
I_{\text{cyl}}=\frac12(4m)r^2=2mr^2,
\qquad
I_{\text{ring}}=mr^2.
$$

Only the cylinder carries initial angular momentum, so

$$
\omega_f
=\frac{I_{\text{cyl}}}{I_{\text{cyl}}+I_{\text{ring}}}\omega_0
=\frac{2mr^2}{2mr^2+mr^2}\omega_0
=\frac23\omega_0.
$$

The common factor $mr^2$ cancels only after it has been included in every applicable term.

This cancellation is valid because the denominator can first be factored as

$$
2mr^2+mr^2=mr^2(2+1).
$$

Cancel common **factors**, not isolated pieces of a sum.

```quiz
type: radio
id: coupling-with-shape-inertias
shuffle: true
content: |-
  A uniform solid cylinder of mass $6m$ and radius $r$ spins at $\omega_0$. An initially stationary thin ring of mass $m$ and radius $r$ couples to it. What is the shared angular speed?
options:
- id: three-quarters
  content: |-
    $\omega_f=\dfrac34\omega_0$
  correct: true
  feedback: |-
    The cylinder has $I_c=\tfrac12(6m)r^2=3mr^2$, and the ring has $I_r=mr^2$. Thus $\omega_f=I_c\omega_0/(I_c+I_r)=3mr^2\omega_0/(4mr^2)=3\omega_0/4$.
- id: six-sevenths
  content: |-
    $\omega_f=\dfrac67\omega_0$
  feedback: |-
    This treats the solid cylinder as if $I_c=6mr^2$. Its correct inertia is half that value, $3mr^2$, so the final fraction is $3/(3+1)=3/4$.
- id: one-quarter
  content: |-
    $\omega_f=\dfrac14\omega_0$
  feedback: |-
    The denominator factor $4$ is the total inertia in units of $mr^2$, but the numerator must retain the initially rotating cylinder's factor $3$. Therefore the ratio is $3/4$, not $1/4$.
- id: four-thirds
  content: |-
    $\omega_f=\dfrac43\omega_0$
  feedback: |-
    This inverts the inertia ratio. Coupling to a stationary ring adds inertia without adding initial angular momentum, so the final speed must be below $\omega_0$, specifically $3\omega_0/4$.
- id: energy-root
  content: |-
    $\omega_f=\dfrac{\sqrt3}{2}\omega_0$
  feedback: |-
    The factor $\sqrt{3/4}$ comes from equating rotational kinetic energies. Frictional coupling does not conserve mechanical energy; conserving angular momentum gives the linear ratio $3/4$.
```

---

<a id="apply-the-ratio-to-the-ring-and-cylinder"></a>
## Apply the Ratio to the Ring and Cylinder

**Example:** A uniform solid cylinder of mass $A$ and radius $R$ spins at $\Omega_0$. An initially stationary thin ring of mass $B$ and the same radius couples to it. Express the shared angular speed in terms of $A$, $B$, and $\Omega_0$.

**Explanation**

The initial rotating inertia and the added inertia are

$$
I_{\text{cyl}}=\frac12AR^2,
\qquad
I_{\text{ring}}=BR^2.
$$

Conservation of angular momentum gives

$$
\frac12AR^2\Omega_0
=\left(\frac12AR^2+BR^2\right)\Omega_f.
$$

Combine the fractional coefficients by factoring $R^2/2$ from the entire final inertia:

$$
\frac12AR^2+BR^2
=\frac{R^2}{2}(A+2B).
$$

Now cancel the common factor $R^2/2$ from the numerator and the whole factored denominator:

$$
\Omega_f
=\frac{\frac12AR^2}{\frac12AR^2+BR^2}\Omega_0
=\frac{A}{A+2B}\Omega_0.
$$

**Target problem — solve symbolically before using the self-check:**

**Question 3**

A ring of mass $m$ and radius $r$ is dropped onto a spinning uniform solid cylinder of mass $M$, radius $r$, and initial angular speed $\omega_0$. Find the shared final angular speed.

![](<../Source/Images/angmosystem2.jpg>)

```quiz
type: radio
id: khadley-angular-momentum-q3
shuffle: true
content: |-
  Which expression correctly checks the symbolic result for Question 3?
options:
- id: correct-ratio
  content: |-
    $\omega_f=\dfrac{M}{M+2m}\,\omega_0$
  correct: true
  feedback: |-
    The spinning cylinder initially has $L_i=(Mr^2/2)\omega_0$. After coupling, $I_f=Mr^2/2+mr^2$, so conserving angular momentum and canceling $r^2/2$ gives $\omega_f=M\omega_0/(M+2m)$.
- id: both-like-rings
  content: |-
    $\omega_f=\dfrac{M}{M+m}\,\omega_0$
  feedback: |-
    This assigns $I=Mr^2$ to the solid cylinder as though it were a thin ring. The cylinder's correct inertia is $Mr^2/2$, which produces the denominator $M+2m$ after simplification.
- id: energy-square-root
  content: |-
    $\omega_f=\sqrt{\dfrac{M}{M+2m}}\,\omega_0$
  feedback: |-
    The square root results from conserving rotational kinetic energy. The coupling is inelastic, so mechanical energy decreases; conserving angular momentum gives the unsquared ratio $M/(M+2m)$.
- id: inverted-ratio
  content: |-
    $\omega_f=\dfrac{M+2m}{M}\,\omega_0$
  feedback: |-
    This reverses the initial-to-final inertia ratio. The stationary ring adds final inertia without adding initial angular momentum, so the shared speed must be less than $\omega_0$, not greater.
- id: unchanged-speed
  content: |-
    $\omega_f=\omega_0$
  feedback: |-
    Angular momentum is conserved, but angular speed is not. The ring adds $mr^2$ to the final moment of inertia, requiring a smaller shared angular speed.
```

---

<a id="summary"></a>
## Summary

For coaxial objects that couple and rotate together with negligible external torque:

1. Write every initial contribution in $L_i=\sum I_j\omega_{ji}$.
2. Add every final inertia in $L_f=(\sum I_j)\omega_f$.
3. Set $L_i=L_f$ and isolate $\omega_f$.
4. Substitute the correct moment of inertia for each shape.
5. Factor the entire final-inertia sum before canceling common quantities.

Do not conserve rotational kinetic energy during frictional sticking. Cancel only factors shared by the complete numerator and denominator, never separate terms inside a sum. When an initially stationary object joins the rotation, the shared final speed should lie below the original spinning object's speed.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
