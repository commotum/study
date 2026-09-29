# Mechanical-Energy Change During a Sticking Collision

<!--
lesson-id: 212-M4-024
topic-code: MTH212.M4.24
-->

## Table of Contents

- [Introduction](#introduction)
- [Write the Two Energy Snapshots](#write-the-two-energy-snapshots)
- [Subtract and Cancel Unchanged Energy](#subtract-and-cancel-unchanged-energy)
- [Apply the Homework Notation](#apply-the-homework-notation)
- [Check the Sign of the Change](#check-the-sign-of-the-change)
- [Summary](#summary)

## Prerequisites

- Mechanical energy is the sum of kinetic and potential energy: $E=K+U$.
- Translational kinetic energy is $K=\frac12 mv^2$.
- Spring potential energy is $U_s=\frac12 kx^2$.
- A change is final minus initial: $\Delta E=E_{\mathrm{after}}-E_{\mathrm{before}}$.

---

<a id="introduction"></a>
## Introduction

The cue is a sticking collision that begins and ends at essentially the same spring position. Mechanical energy is generally **not** conserved during the collision, so compare two snapshots instead of setting their energies equal:

$$
\Delta E=E_{\mathrm{after}}-E_{\mathrm{before}}.
$$

For Problem 9, map the symbols before writing any energy:

| Snapshot | Moving mass | Speed | Spring position |
| --- | ---: | ---: | ---: |
| Before | $M$ | $v_0$ | $A/2$ |
| After | $M+m$ | $v_f$ | $A/2$ |

The spring potential energy must appear in both energy expressions. Because the position is unchanged across the two snapshots, those equal potential-energy terms cancel only after the subtraction is written.

---

<a id="write-the-two-energy-snapshots"></a>
## Write the Two Energy Snapshots

**Example:** A block of mass $B$ moves at speed $u$ while a spring is at position $x_c$. A piece of putty of mass $p$ is dropped with negligible initial kinetic energy and sticks to the block. The joined mass moves at speed $w$. Write the mechanical energy immediately before and immediately after the collision.

**Explanation**

Before the collision, only the block contributes kinetic energy. Afterward, the block and putty move together, so their moving mass is $B+p$. The spring is at the same position $x_c$ in both snapshots:

$$
E_{\mathrm{before}}
=\frac12 Bu^2+\frac12 kx_c^2,
$$

$$
E_{\mathrm{after}}
=\frac12(B+p)w^2+\frac12 kx_c^2.
$$

Do not give the putty an initial kinetic-energy term when the problem says that its initial kinetic energy is negligible.

```quiz
type: radio
id: p9-snapshots-q1
content: |-
  A cart of mass $C$ has speed $u_i$ at spring position $x_*$ when clay of mass $c$ lands with negligible initial kinetic energy and sticks. The joined cart and clay have speed $u_f$. Which pair of energy snapshots is correct?
options:
- id: p9-snapshots-q1-a
  content: |-
    $E_{\mathrm{before}}=\frac12 Cu_i^2+\frac12 kx_*^2$ and $E_{\mathrm{after}}=\frac12(C+c)u_f^2+\frac12 kx_*^2$
  correct: true
- id: p9-snapshots-q1-b
  content: |-
    $E_{\mathrm{before}}=\frac12(C+c)u_i^2+\frac12 kx_*^2$ and $E_{\mathrm{after}}=\frac12(C+c)u_f^2+\frac12 kx_*^2$
- id: p9-snapshots-q1-c
  content: |-
    $E_{\mathrm{before}}=\frac12 Cu_i^2$ and $E_{\mathrm{after}}=\frac12(C+c)u_f^2+\frac12 kx_*^2$
- id: p9-snapshots-q1-d
  content: |-
    $E_{\mathrm{before}}=\frac12 Cu_i^2+\frac12 kx_*^2$ and $E_{\mathrm{after}}=\frac12 Cu_f^2+\frac12 kx_*^2$
```

---

<a id="subtract-and-cancel-unchanged-energy"></a>
## Subtract and Cancel Unchanged Energy

**Example:** Use the two snapshots above to find the mechanical-energy change.

**Explanation**

Subtract the entire before expression from the entire after expression. Treat the second bracket as one group:

$$
\begin{aligned}
\Delta E
&=E_{\mathrm{after}}-E_{\mathrm{before}}\\
&=\left[\frac12(B+p)w^2+\frac12kx_c^2\right]
-\left[\frac12Bu^2+\frac12kx_c^2\right].
\end{aligned}
$$

Now distribute the negative sign to every term in the before bracket:

$$
\Delta E
=\frac12(B+p)w^2+\frac12kx_c^2
-\frac12Bu^2-\frac12kx_c^2.
$$

The two spring-energy terms are like terms with opposite signs, so they cancel:

$$
\boxed{\Delta E=\frac12(B+p)w^2-\frac12Bu^2}.
$$

The spring energy is not zero. Its **change** is zero because the spring has the same position in both snapshots. Writing only one copy of the spring term would incorrectly leave an extra $-\frac12kx_c^2$.

```quiz
type: radio
id: p9-cancel-q1
content: |-
  Immediately before a collision,
  $E_i=\frac12 Ru_i^2+\frac12 kx_c^2$.
  Immediately after it,
  $E_f=\frac12(R+r)u_f^2+\frac12 kx_c^2$.
  What is $\Delta E=E_f-E_i$?
options:
- id: p9-cancel-q1-a
  content: |-
    $\frac12(R+r)u_f^2-\frac12Ru_i^2$
  correct: true
- id: p9-cancel-q1-b
  content: |-
    $\frac12(R+r)u_f^2-\frac12Ru_i^2-\frac12kx_c^2$
- id: p9-cancel-q1-c
  content: |-
    $\frac12Ru_i^2-\frac12(R+r)u_f^2$
- id: p9-cancel-q1-d
  content: |-
    $\frac12Ru_f^2-\frac12Ru_i^2$
```

```quiz
type: radio
id: p9-cancel-q2
content: |-
  At one spring position, a system has $10\ \mathrm{J}$ of kinetic energy and $3\ \mathrm{J}$ of spring potential energy just before a collision. At that same position just after the collision, it has $6\ \mathrm{J}$ of kinetic energy and $3\ \mathrm{J}$ of spring potential energy. What is $\Delta E=E_{\mathrm{after}}-E_{\mathrm{before}}$?
options:
- id: p9-cancel-q2-a
  content: |-
    $-4\ \mathrm{J}$
  correct: true
- id: p9-cancel-q2-b
  content: |-
    $-7\ \mathrm{J}$
- id: p9-cancel-q2-c
  content: |-
    $4\ \mathrm{J}$
- id: p9-cancel-q2-d
  content: |-
    $0\ \mathrm{J}$
```

---

<a id="apply-the-homework-notation"></a>
## Apply the Homework Notation

**Example:** A block of mass $M$ attached to a spring is at $x=A/2$ when clay of mass $m$ lands and sticks. The block’s speed is $v_0$ just before the collision, and the joined mass’s speed is $v_f$ just after it. Find $\Delta E$ during the collision.

**Explanation**

Write both snapshots before simplifying:

$$
E_{\mathrm{before}}
=\frac12Mv_0^2+\frac12k\left(\frac A2\right)^2,
$$

$$
E_{\mathrm{after}}
=\frac12(M+m)v_f^2+\frac12k\left(\frac A2\right)^2.
$$

Then subtract:

$$
\begin{aligned}
\Delta E
&=\left[\frac12(M+m)v_f^2+\frac12k\left(\frac A2\right)^2\right]\\
&\quad-\left[\frac12Mv_0^2+\frac12k\left(\frac A2\right)^2\right]\\
&=\boxed{\frac12(M+m)v_f^2-\frac12Mv_0^2}.
\end{aligned}
$$

Therefore, the correct answer is the expression that keeps the total moving mass $M+m$, uses final minus initial kinetic energy, and has no leftover spring term.

```quiz
type: radio
id: p9-homework-q1
content: |-
  A block of mass $M$ attached to an ideal spring of spring constant $k$ oscillates with amplitude $A$ over a frictionless horizontal surface.

  A ball of clay of mass $m$ lands on the block while it is at $x=A/2$ and sticks. The block's speed just before the collision is $v_0$, and the joined block and clay have speed $v_f$ just after it. The clay's initial kinetic energy is negligible.

  What is $\Delta E=E_{\mathrm{after}}-E_{\mathrm{before}}$ during the collision?
options:
- id: p9-homework-q1-a
  content: |-
    $\dfrac12(M+m)v_f^2-\dfrac12Mv_0^2-\dfrac12k(A/2)^2$
- id: p9-homework-q1-b
  content: |-
    $\dfrac12(M+m)v_f^2-\dfrac12Mv_0^2$
  correct: true
- id: p9-homework-q1-c
  content: |-
    $\dfrac12M\left(v_f^2-v_0^2\right)$
- id: p9-homework-q1-d
  content: |-
    $-\dfrac12(M+m)v_f^2-\dfrac12Mv_0^2-\dfrac12k(A/2)^2$
```

---

<a id="check-the-sign-of-the-change"></a>
## Check the Sign of the Change

**Example:** From momentum conservation during the brief collision, suppose

$$
v_f=\frac{M}{M+m}v_0.
$$

Use this relation to check the sign of the mechanical-energy change. This is a verification step; the answer in terms of $v_f$ was already obtained without substituting for it.

**Explanation**

Substitute into the kinetic-energy difference:

$$
\begin{aligned}
\Delta E
&=\frac12(M+m)\left(\frac{M}{M+m}v_0\right)^2-\frac12Mv_0^2\\
&=\frac12\frac{M^2}{M+m}v_0^2-\frac12Mv_0^2\\
&=-\frac12\frac{Mm}{M+m}v_0^2.
\end{aligned}
$$

For positive masses, $\Delta E<0$. This is physically sensible: sticking is an inelastic collision, so some mechanical energy becomes internal energy even though momentum is conserved during the collision.

```quiz
type: radio
id: p9-sign-q1
content: |-
  A moving block collides with clay initially at rest, and the clay sticks. Which statement is the correct sign check for the collision?
options:
- id: p9-sign-q1-a
  content: |-
    $\Delta E>0$ because adding mass creates mechanical energy.
- id: p9-sign-q1-b
  content: |-
    $\Delta E=0$ because momentum conservation guarantees kinetic-energy conservation.
- id: p9-sign-q1-c
  content: |-
    $\Delta E<0$ because a sticking collision converts some mechanical energy into internal energy.
  correct: true
- id: p9-sign-q1-d
  content: |-
    The sign cannot be checked because spring potential energy was omitted from both snapshots.
```

---

<a id="summary"></a>
## Summary

When a collision happens at one fixed spring position:

1. Write $E_{\mathrm{before}}=K_{\mathrm{before}}+U_{\mathrm{before}}$.
2. Write $E_{\mathrm{after}}=K_{\mathrm{after}}+U_{\mathrm{after}}$.
3. Form $\Delta E=E_{\mathrm{after}}-E_{\mathrm{before}}$, keeping parentheses around the full before expression.
4. Cancel energy terms that are identical in both snapshots.
5. Check that a sticking collision gives $\Delta E<0$.

For Problem 9,

$$
\boxed{\Delta E=\frac12(M+m)v_f^2-\frac12Mv_0^2}.
$$

The main trap is subtracting the spring potential only once. Because the spring remains at $x=A/2$ throughout the brief collision, its potential energy appears in both snapshots and cancels.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
