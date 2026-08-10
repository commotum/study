# Deriving Kepler's Third Law

<!--
lesson-id: 212-M3-034
topic-code: MTH212.M3.34
-->

## Table of Contents

- [Introduction](#introduction)
- [Match Gravity to Radial Force](#match-gravity-to-radial-force)
- [Replace Orbital Speed with Period](#replace-orbital-speed-with-period)
- [Isolate and Check the Period](#isolate-and-check-the-period)
- [Match the Source Problem](#match-the-source-problem)
- [Summary](#summary)

## Prerequisites

- Use Newtonian gravity, $F_g=GMm/r^2$.
- Use the radial-force requirement, $F_r=mv^2/r$.
- Recognize that one circular orbit covers circumference $2\pi r$ in one period $T$.
- Isolate a requested variable in a symbolic equation.

---

<a id="introduction"></a>
## Introduction

For a small satellite in a circular orbit of radius $r$ around a much more massive central body $M$, gravity supplies the entire inward force required for circular motion. That recognition cue connects Newton's law of gravity to the orbital period. The target is $T^2$; treat $G$ and $M$ as constants while isolating it.

Determine the period law with this sequence:

1. Set gravitational force equal to the radial-force requirement.
2. Cancel the satellite mass.
3. Replace $v$ with one circumference per period, $2\pi r/T$.
4. Isolate $T^2$.

The result will have the form $T^2=Cr^3$, which turns Kepler's proportionality $T^2\propto r^3$ into an equation.

---

<a id="match-gravity-to-radial-force"></a>
## Match Gravity to Radial Force

"Centripetal force" is not an additional force. It is the name for the net inward force. In this orbit, Newtonian gravity is that inward force.

**Example:** A satellite of mass $\mu$ moves in a circular orbit of radius $R$ around a central mass $P$. Write the radial force equation.

**Explanation**

Set the gravitational-force magnitude equal to the required radial-force magnitude:

$$
\frac{GP\mu}{R^2}=\frac{\mu u^2}{R}.
$$

The satellite mass $\mu$ appears on both sides and cancels:

$$
\frac{GP}{R}=u^2.
$$

```quiz
type: radio
id: kepler-force-balance
shuffle: true
content: |-
  A small satellite of mass $m$ travels in a circular orbit of radius $r$ around a central mass $M$. Which equation correctly states that gravity supplies the radial force?
options:
- id: kepler-force-balance-correct
  content: |-
    $\displaystyle \frac{GMm}{r^2}=\frac{mv^2}{r}$
  correct: true
  feedback: |-
    Newtonian gravity has magnitude $GMm/r^2$, and circular motion requires net inward force $mv^2/r$. Gravity is the inward force here, so these two expressions are equal.
- id: kepler-force-balance-gravity-power
  content: |-
    $\displaystyle \frac{GMm}{r}=\frac{mv^2}{r}$
  feedback: |-
    The radial-force side is correct, but Newtonian gravity follows an inverse-square law. Its magnitude is $GMm/r^2$, not $GMm/r$.
- id: kepler-force-balance-radial-power
  content: |-
    $\displaystyle \frac{GMm}{r^2}=\frac{mv^2}{r^2}$
  feedback: |-
    Gravity uses $1/r^2$, but the acceleration for circular motion is $v^2/r$. Multiplying by $m$ gives radial force $mv^2/r$, with only one power of $r$ in that denominator.
- id: kepler-force-balance-mass-one-side
  content: |-
    $\displaystyle \frac{GM}{r^2}=\frac{mv^2}{r}$
  feedback: |-
    The satellite mass can cancel only after it appears in both force expressions. This equation removes $m$ from gravity but keeps it in radial force, so its two sides do not even have the same units.
- id: kepler-force-balance-add-force
  content: |-
    $\displaystyle \frac{GMm}{r^2}+\frac{mv^2}{r}=0$
  feedback: |-
    The radial term $mv^2/r$ is not a second physical force to add to gravity. It is the net inward-force requirement that gravity itself must equal.
```

---

<a id="replace-orbital-speed-with-period"></a>
## Replace Orbital Speed with Period

The force equation contains speed, but Kepler's law uses the orbital period. A circular orbit covers distance $2\pi r$ during time $T$, so

$$
v=\frac{2\pi r}{T}.
$$

**Example:** Express $u^2$ in terms of the orbit radius $R$ and period $\tau$.

**Explanation**

Square the entire speed expression:

$$
u^2=\left(\frac{2\pi R}{\tau}\right)^2
=\frac{4\pi^2R^2}{\tau^2}.
$$

Every factor in the numerator and denominator is squared.

```quiz
type: radio
id: kepler-square-orbital-speed
shuffle: true
content: |-
  A satellite completes a circular orbit of radius $r$ in period $T$. Which expression correctly replaces $v^2$?
options:
- id: kepler-square-orbital-speed-correct
  content: |-
    $\displaystyle v^2=\frac{4\pi^2r^2}{T^2}$
  correct: true
  feedback: |-
    One orbit covers $2\pi r$ in time $T$, so $v=2\pi r/T$. Squaring the entire quotient gives $v^2=4\pi^2r^2/T^2$.
- id: kepler-square-orbital-speed-unsquared
  content: |-
    $\displaystyle v^2=\frac{2\pi r}{T}$
  feedback: |-
    The right side is the expression for $v$, not $v^2$. Because the force balance contains $v^2$, the full speed expression must be squared.
- id: kepler-square-orbital-speed-pi-not-squared
  content: |-
    $\displaystyle v^2=\frac{4\pi r^2}{T^2}$
  feedback: |-
    Squaring $2\pi r/T$ squares $\pi$ as well as $2$, $r$, and $T$. The numerator must contain $4\pi^2r^2$.
- id: kepler-square-orbital-speed-period-not-squared
  content: |-
    $\displaystyle v^2=\frac{4\pi^2r^2}{T}$
  feedback: |-
    The period is part of the quotient being squared. The denominator is therefore $T^2$, not $T$.
- id: kepler-square-orbital-speed-no-circumference
  content: |-
    $\displaystyle v^2=\frac{r^2}{T^2}$
  feedback: |-
    This treats the orbital distance as one radius. The satellite travels the full circumference $2\pi r$ each period, so squaring introduces the missing factor $4\pi^2$.
```

---

<a id="isolate-and-check-the-period"></a>
## Isolate and Check the Period

After the satellite mass cancels, combine

$$
\frac{GM}{r}=v^2
$$

with

$$
v^2=\frac{4\pi^2r^2}{T^2}.
$$

**Example:** Solve the combined equation for $T^2$.

**Explanation**

Set the two expressions for $v^2$ equal:

$$
\frac{GM}{r}=\frac{4\pi^2r^2}{T^2}.
$$

Multiply by $rT^2$:

$$
GMT^2=4\pi^2r^3.
$$

Then divide by $GM$:

$$
T^2=\frac{4\pi^2}{GM}r^3.
$$

For satellites orbiting the same central mass, the coefficient

$$
C=\frac{4\pi^2}{GM}
$$

is constant. Thus $T^2=Cr^3$ explicitly shows the direct variation $T^2\propto r^3$.

The units also check. Since

$$
[G]=\frac{\mathrm m^3}{\mathrm{kg}\,\mathrm s^2},
$$

the factor $r^3/(GM)$ has units

$$
\frac{\mathrm m^3}{(\mathrm m^3/(\mathrm{kg}\,\mathrm s^2))\mathrm{kg}}
=\mathrm s^2,
$$

which matches $T^2$.

```quiz
type: radio
id: kepler-radius-scaling
shuffle: true
content: |-
  Satellite $B$ orbits the same central mass at twice the circular-orbit radius of satellite $A$. According to Kepler's third law, what is $T_B/T_A$?
options:
- id: kepler-radius-scaling-correct
  content: |-
    $2\sqrt{2}$
  correct: true
  feedback: |-
    For the same central mass, $T^2\propto r^3$, so $T\propto r^{3/2}$. Doubling the radius multiplies the period by $2^{3/2}=2\sqrt2$.
- id: kepler-radius-scaling-two
  content: |-
    $2$
  feedback: |-
    This assumes period is directly proportional to radius. Kepler's law gives $T\propto r^{3/2}$, so doubling $r$ produces the larger factor $2\sqrt2$.
- id: kepler-radius-scaling-four
  content: |-
    $4$
  feedback: |-
    A factor of $4$ would follow from $T\propto r^2$. The actual exponent is $3/2$ after taking the square root of $T^2\propto r^3$.
- id: kepler-radius-scaling-eight
  content: |-
    $8$
  feedback: |-
    The factor $2^3=8$ applies to the ratio $T_B^2/T_A^2$, not directly to the period ratio. Taking the square root gives $T_B/T_A=\sqrt8=2\sqrt2$.
- id: kepler-radius-scaling-root-two
  content: |-
    $\sqrt2$
  feedback: |-
    This uses an exponent of $1/2$ and omits the cubic radius dependence. Kepler's law gives the period exponent $3/2$, so the factor is $2\sqrt2$.
```

---

<a id="match-the-source-problem"></a>
## Match the Source Problem

Keep the physical and algebraic roles separate: gravity supplies the force, circular motion supplies the required inward acceleration, and circumference over period replaces speed.

**Example:** A small moon orbits a planet of mass $P$ at circular radius $R$. Derive its period-squared equation.

**Explanation**

Use

$$
\frac{GP\mu}{R^2}=\frac{\mu u^2}{R},
\qquad
u=\frac{2\pi R}{\tau}.
$$

Cancel $\mu$, substitute the speed, and isolate $\tau^2$:

$$
\tau^2=\frac{4\pi^2R^3}{GP}.
$$

```quiz
type: radio
id: khadley-gravity-q1
shuffle: true
content: |-
  **Question 1**

  Use Newtonian gravity and circular motion to write Kepler's third law, $T^2\propto r^3$, as an equation for a small satellite orbiting mass $M$.
options:
- id: khadley-gravity-q1-correct
  content: |-
    $\displaystyle T^2=\frac{4\pi^2}{GM}r^3$
  correct: true
  feedback: |-
    Gravity supplies the radial force: $GMm/r^2=mv^2/r$. Cancel $m$, substitute $v=2\pi r/T$, and isolate $T^2$ to obtain $T^2=4\pi^2r^3/(GM)$.
- id: khadley-gravity-q1-inverted
  content: |-
    $\displaystyle T^2=\frac{GM}{4\pi^2r^3}$
  feedback: |-
    This inverts the relationship. From $GM/r=4\pi^2r^2/T^2$, multiplying by $T^2$ and dividing by $GM$ places $r^3$ in the numerator and $GM$ in the denominator.
- id: khadley-gravity-q1-radius-square
  content: |-
    $\displaystyle T^2=\frac{4\pi^2r^2}{GM}$
  feedback: |-
    Squaring the circumference contributes $r^2$, but the gravity equation contributes one additional factor of $r$ when denominators are cleared. The final radius dependence is $r^3$, as Kepler's law requires.
- id: khadley-gravity-q1-pi-unsquared
  content: |-
    $\displaystyle T^2=\frac{4\pi r^3}{GM}$
  feedback: |-
    Orbital speed is $2\pi r/T$, and the force equation uses $v^2$. Squaring the speed makes $(2\pi)^2=4\pi^2$, not $4\pi$.
- id: khadley-gravity-q1-satellite-mass
  content: |-
    $\displaystyle T^2=\frac{4\pi^2r^3}{GMm}$
  feedback: |-
    The satellite mass multiplies both gravitational force and radial force, so it cancels. For a small satellite, the period depends on the central mass $M$, not on the satellite mass $m$.
```

---

<a id="summary"></a>
## Summary

To derive Kepler's third law for a small satellite in a circular orbit:

1. Set $GMm/r^2=mv^2/r$.
2. Cancel $m$ to obtain $GM/r=v^2$.
3. Substitute $v=2\pi r/T$ and square the entire expression.
4. Isolate $T^2$:

$$
T^2=\frac{4\pi^2}{GM}r^3.
$$

The coefficient $4\pi^2/(GM)$ is fixed for one central mass, so $T^2\propto r^3$, and $r^3/(GM)$ has units of time squared. The main traps are treating centripetal force as an extra force, forgetting to square every factor in $2\pi r/T$, losing one power of $r$, or keeping the satellite mass after it cancels.
