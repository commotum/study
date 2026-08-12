# Escape Speed from Energy

<!--
lesson-id: 212-M3-036
topic-code: MTH212.M3.36
-->

## Table of Contents

- [Introduction](#introduction)
- [Set the Escape Threshold at Infinity](#set-the-escape-threshold-at-infinity)
- [Write the Starting Energy](#write-the-starting-energy)
- [Isolate the Physical Speed](#isolate-the-physical-speed)
- [Match the Source Problem](#match-the-source-problem)
- [Summary](#summary)

## Prerequisites

- Use $K=\dfrac12mv^2$.
- Use gravitational potential energy $U=-GMm/r$ with $U(\infty)=0$.
- Apply conservation of mechanical energy.
- Isolate a squared variable and take a square root.

---

<a id="introduction"></a>
## Introduction

Escape speed is the minimum launch speed that lets an object get arbitrarily far from a planet without falling back. At this threshold, the object reaches infinity with zero remaining speed.

The recognition cue is the phrase "just escapes" or "escape speed." The immediate algebraic target is $v^2$; treat $G$, $M$, and $r$ as fixed quantities while isolating it. First translate the threshold into an energy condition:

$$
E_{\mathrm{final}}=K_{\infty}+U_{\infty}=0+0=0.
$$

Then set the launch energy equal to zero, isolate $v^2$, and report the positive square root. For a launch from a planet of mass $M$ at distance $r$ from its center,

$$
v_{\mathrm{esc}}=\sqrt{\frac{2GM}{r}}.
$$

The units confirm the result. Since $[G]=\mathrm{m^3/(kg\,s^2)}$,

$$
\left[\frac{GM}{r}\right]
=\frac{(\mathrm{m^3/(kg\,s^2)})\,\mathrm{kg}}{\mathrm m}
=\frac{\mathrm m^2}{\mathrm s^2}.
$$

Thus $2GM/r$ has units of speed squared, and its square root has units of speed.

This ideal model neglects atmosphere, planetary rotation, propulsion after launch, and gravity from other bodies.

---

<a id="set-the-escape-threshold-at-infinity"></a>
## Set the Escape Threshold at Infinity

Because gravitational potential energy is defined to approach zero at infinity, the threshold object's final kinetic and potential energies are both zero. A faster launch would leave positive kinetic energy at infinity; a slower launch would have negative total energy and remain bound.

**Example:** A probe is launched from radius $R$ around a planet. What is its total mechanical energy at the exact escape threshold?

**Explanation**

At infinity the threshold probe has $v_{\infty}=0$ and $U_{\infty}=0$. Therefore,

$$
E=E_{\infty}=0.
$$

Mechanical energy is conserved, so the probe's launch energy must also equal zero.

```quiz
type: radio
id: escape-threshold-energy
shuffle: true
content: |-
  Which final-state condition defines the exact escape threshold for an object launched from a planet, using $U(\infty)=0$?
options:
- id: escape-threshold-energy-zero
  content: |-
    At infinity, $K_f=0$, $U_f=0$, and $E_f=0$.
  correct: true
  feedback: |-
    At the minimum escape speed, the object just reaches infinity with zero speed. Since gravitational potential is also zero there, both contributions vanish and the conserved total energy is exactly zero.
- id: escape-threshold-energy-positive-kinetic
  content: |-
    At infinity, $K_f>0$, $U_f=0$, and $E_f>0$.
  feedback: |-
    This describes a launch faster than escape speed: the object still has kinetic energy at infinity. The threshold is the minimum speed, for which the final kinetic energy is zero.
- id: escape-threshold-energy-negative
  content: |-
    At infinity, $E_f<0$.
  feedback: |-
    Negative total energy describes a bound gravitational system. An object with $E<0$ cannot reach infinity, so this is below the escape threshold.
- id: escape-threshold-energy-initial-potential
  content: |-
    At infinity, $U_f=-GMm/r$.
  feedback: |-
    The expression $-GMm/r$ is the potential energy at the finite launch radius $r$. With the stated reference, gravitational potential approaches zero at infinity.
- id: escape-threshold-energy-rest-at-surface
  content: |-
    At the planet's surface, $K_i=0$ and $E_i=0$.
  feedback: |-
    The object must launch with nonzero kinetic energy to offset its negative surface potential energy. Starting at rest leaves negative total energy and does not produce escape.
```

---

<a id="write-the-starting-energy"></a>
## Write the Starting Energy

At launch, the object has positive kinetic energy and negative gravitational potential energy. Set their sum equal to the threshold total energy, zero.

**Example:** A projectile of mass $\mu$ is launched at speed $u$ from distance $R$ from the center of a planet of mass $P$. Write the escape-threshold equation.

**Explanation**

The launch energy is

$$
E_i=\frac12\mu u^2-\frac{GP\mu}{R}.
$$

At the exact escape threshold, $E_i=E_f=0$, so

$$
\frac12\mu u^2-\frac{GP\mu}{R}=0.
$$

```quiz
type: radio
id: escape-starting-energy
shuffle: true
content: |-
  An object of mass $m$ is launched at escape speed $v$ from a nonrotating planet of mass $M$ and radius $r$. Which equation correctly represents its launch energy at the escape threshold?
options:
- id: escape-starting-energy-correct
  content: |-
    $\displaystyle \frac12mv^2-\frac{GMm}{r}=0$
  correct: true
  feedback: |-
    At launch, kinetic energy is $mv^2/2$ and gravitational potential energy is $-GMm/r$. Their sum must equal the threshold total energy zero.
- id: escape-starting-energy-positive-potential
  content: |-
    $\displaystyle \frac12mv^2+\frac{GMm}{r}=0$
  feedback: |-
    With the zero of potential at infinity, gravitational potential energy at finite radius is negative. Using a positive sign would make both launch-energy terms positive and unable to sum to zero.
- id: escape-starting-energy-force-power
  content: |-
    $\displaystyle \frac12mv^2-\frac{GMm}{r^2}=0$
  feedback: |-
    The inverse-square expression belongs to gravitational force. Gravitational potential energy varies as $-1/r$, so the energy term is $-GMm/r$.
- id: escape-starting-energy-no-potential
  content: |-
    $\displaystyle \frac12mv^2=0$
  feedback: |-
    This omits the negative gravitational potential energy that the launch kinetic energy must overcome. At a finite launch radius, the threshold object has nonzero launch speed.
- id: escape-starting-energy-planet-kinetic
  content: |-
    $\displaystyle \frac12Mv^2-\frac{GMm}{r}=0$
  feedback: |-
    The moving projectile has mass $m$, so its kinetic energy is $mv^2/2$. The planet mass $M$ determines the gravitational field but is not the launched object's kinetic-energy mass.
```

---

<a id="isolate-the-physical-speed"></a>
## Isolate the Physical Speed

The projectile mass multiplies every term and cancels. After cancellation, isolate $v^2$ before taking a square root.

**Example:** Solve

$$
\frac12mv^2-\frac{GMm}{r}=0
$$

for escape speed.

**Explanation**

Move the potential-energy magnitude to the other side and cancel $m$:

$$
\frac12mv^2=\frac{GMm}{r}
\qquad\Longrightarrow\qquad
v^2=\frac{2GM}{r}.
$$

The algebraic equation has two signed velocity roots, but speed is a nonnegative magnitude. Therefore,

$$
v_{\mathrm{esc}}=\sqrt{\frac{2GM}{r}}.
$$

```quiz
type: radio
id: escape-speed-scaling
shuffle: true
content: |-
  Planet $B$ has eight times the mass and twice the radius of planet $A$. What is $v_{\mathrm{esc},B}/v_{\mathrm{esc},A}$?
options:
- id: escape-speed-scaling-two
  content: |-
    $2$
  correct: true
  feedback: |-
    Escape speed scales as $\sqrt{M/r}$. Substituting the ratios gives $\sqrt{8/2}=\sqrt4=2$, so planet $B$ has twice the escape speed.
- id: escape-speed-scaling-four
  content: |-
    $4$
  feedback: |-
    The mass-to-radius ratio increases by $8/2=4$, but that ratio is $v^2$'s scaling. Escape speed is its square root, so the speed ratio is $2$, not $4$.
- id: escape-speed-scaling-root-two
  content: |-
    $\sqrt2$
  feedback: |-
    This would follow from a mass-to-radius ratio of $2$. Here the ratio is $8/2=4$, whose square root is $2$.
- id: escape-speed-scaling-eight
  content: |-
    $8$
  feedback: |-
    This uses the mass ratio alone and ignores both the doubled radius and the square root in $v_{\mathrm{esc}}=\sqrt{2GM/r}$.
- id: escape-speed-scaling-one-half
  content: |-
    $\dfrac12$
  feedback: |-
    Although the larger radius alone would lower escape speed, planet $B$'s mass increases by the larger factor. Its $M/r$ ratio is four times as large, so its escape speed is twice as large.
```

For comparisons between two planets, keep the substitutions grouped before simplifying:

$$
\frac{v_{\mathrm{esc},B}}{v_{\mathrm{esc},A}}
=\sqrt{\frac{M_B/r_B}{M_A/r_A}}.
$$

This makes it clear that mass appears in the numerator, radius appears in the denominator, and the entire ratio remains under one square root.

---

<a id="match-the-source-problem"></a>
## Match the Source Problem

Use the threshold statement first, then solve the resulting energy equation.

**Example:** A small object is launched from the surface of a spherical body of mass $P$ and radius $R$. Find its minimum escape speed.

**Explanation**

At the threshold, the object reaches infinity with zero kinetic and potential energy. Thus

$$
\frac12\mu u^2-\frac{GP\mu}{R}=0,
$$

which gives

$$
u=\sqrt{\frac{2GP}{R}}.
$$

```quiz
type: radio
id: khadley-gravitational-energy-q1
shuffle: true
content: |-
  **Question 1**

  Find the escape speed from a planet of mass $M$ and radius $r$.
options:
- id: khadley-gravitational-energy-q1-correct
  content: |-
    $\displaystyle v_{\mathrm{esc}}=\sqrt{\frac{2GM}{r}}$
  correct: true
  feedback: |-
    At the escape threshold, total energy is zero: $mv^2/2-GMm/r=0$. The projectile mass cancels, and taking the nonnegative root gives $v_{\mathrm{esc}}=\sqrt{2GM/r}$.
- id: khadley-gravitational-energy-q1-circular
  content: |-
    $\displaystyle v_{\mathrm{esc}}=\sqrt{\frac{GM}{r}}$
  feedback: |-
    This is the circular-orbit speed at radius $r$. Escape requires enough kinetic energy to raise total energy from $-GMm/(2r)$ to zero, producing the additional factor of $2$ under the square root.
- id: khadley-gravitational-energy-q1-no-root
  content: |-
    $\displaystyle v_{\mathrm{esc}}=\frac{2GM}{r}$
  feedback: |-
    Energy conservation gives $v^2=2GM/r$. The displayed expression is the value of $v^2$ and has units of speed squared; a square root is still required to obtain speed.
- id: khadley-gravitational-energy-q1-radius-numerator
  content: |-
    $\displaystyle v_{\mathrm{esc}}=\sqrt{2GMr}$
  feedback: |-
    Gravitational potential energy has magnitude $GMm/r$, so increasing launch radius weakens the binding and lowers escape speed. The radius must remain in the denominator, not the numerator.
- id: khadley-gravitational-energy-q1-plus-minus
  content: |-
    $\displaystyle v_{\mathrm{esc}}=\pm\sqrt{\frac{2GM}{r}}$
  feedback: |-
    The squared equation has two signed velocity roots, but escape speed is a nonnegative magnitude. Report only the positive root.
```

---

<a id="summary"></a>
## Summary

To find escape speed from radius $r$:

1. Interpret "just escapes" as $K_{\infty}=U_{\infty}=0$.
2. Conserve energy: $\dfrac12mv^2-\dfrac{GMm}{r}=0$.
3. Cancel the projectile mass and isolate $v^2=2GM/r$.
4. Report the nonnegative speed:

$$
v_{\mathrm{esc}}=\sqrt{\frac{2GM}{r}}.
$$

Check that $GM/r$ has units of speed squared before taking the root. The main traps are using a positive potential-energy sign, confusing the $1/r$ potential with the $1/r^2$ force, omitting the square root, or reporting both signed roots when the question asks for speed.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
