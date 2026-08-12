# Solving Circular Binary-Star Systems from Their Separation

<!--
lesson-id: 212-M3-033
topic-code: MTH212.M3.33
-->
## Table of Contents

- [Introduction](#introduction)
- [Locate the Center of Mass from a Chosen Origin](#locate-the-center-of-mass-from-a-chosen-origin)
- [Use the Relative Orbit to Find the Period](#use-the-relative-orbit-to-find-the-period)
- [Use the Circular-Orbit Energy Shortcut](#use-the-circular-orbit-energy-shortcut)
- [Carry One Mass Ratio Through the Full System](#carry-one-mass-ratio-through-the-full-system)
- [Summary](#summary)

## Prerequisites

- Compute a one-dimensional center of mass with $x_{\mathrm{cm}}=\sum m_ix_i/\sum m_i$.
- Use Newton's gravitational force and the inward radial-acceleration form $a_r=\omega^2r$.
- Convert between angular speed and period with $T=2\pi/\omega$.
- Use $U=-Gm_1m_2/r$ and $E=K+U$.
- Substitute and simplify symbolic mass ratios.

---

<a id="introduction"></a>
## Introduction

When two masses orbit their common center of mass, each mass has its own orbital radius, but the gravitational interaction is controlled by the **separation between the masses**. The recognition cue is a circular two-body system whose separation and mass relation are given.

Place mass $M$ at $x=0$ and mass $m$ at $x=d$. The center of mass divides the separation into

$$
r_M=\frac{m}{M+m}d,
\qquad
r_m=\frac{M}{M+m}d,
\qquad
r_M+r_m=d.
$$

Use $r_M$ or $r_m$ only when locating a particular mass relative to the center of mass. Use the full separation $d$ in the gravitational force, potential energy, period formula, and total-energy formula.

Sort the requested quantity before choosing a formula:

| Requested quantity | Distance role | Mass role |
|---|---|---|
| Center measured from $M$ | Coordinate span $d$ from $0$ to $d$ | Opposite mass $m$ weights the numerator; $M+m$ normalizes |
| Common period | Full separation $d$ | Total mass $M+m$ |
| Total mechanical energy | Full separation $d$ | Mass product $Mm$, followed by the circular-orbit factor $1/2$ |

The three reusable results are

$$
x_{\mathrm{cm}}=\frac{md}{M+m}
\quad\text{measured from }M,
$$

$$
T=2\pi\sqrt{\frac{d^3}{G(M+m)}},
$$

and

$$
E=-\frac{GMm}{2d}.
$$

The main trap is replacing $d$ in the last two formulas with one star's distance from the center of mass.

---

<a id="locate-the-center-of-mass-from-a-chosen-origin"></a>
## Locate the Center of Mass from a Chosen Origin

**Example:** Two masses $2m$ and $m$ are separated by $s$. Find the center of mass measured from the mass $2m$.

**Explanation**

Put $2m$ at $x=0$ and $m$ at $x=s$. Then

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{(2m)(0)+m(s)}{2m+m}\\
&=\frac{s}{3}.
\end{aligned}
$$

The center of mass lies closer to the larger mass. It would be at $s/2$ only if the masses were equal.

Two checks expose most setup errors: the answer must lie between $0$ and $s$, and it must lie on the larger mass's side of the midpoint.

```quiz
type: radio
id: p5-center-of-mass
shuffle: true
content: |-
  Masses $4m$ and $m$ are separated by a distance $L$. What is the center-of-mass position measured from the mass $4m$?
options:
- id: p5-center-of-mass-a
  content: |-
    $\dfrac{L}{5}$
  correct: true
  feedback: |-
    Put $4m$ at $x=0$ and $m$ at $x=L$. The weighted position is $x_{\mathrm{cm}}=[(4m)(0)+mL]/(5m)=L/5$, which is closer to the larger mass.
- id: p5-center-of-mass-b
  content: |-
    $\dfrac{4L}{5}$
  feedback: |-
    This is the distance from the center of mass to the smaller mass, not the requested distance measured from the larger mass. From the $4m$ mass, the position is $mL/(4m+m)=L/5$.
- id: p5-center-of-mass-c
  content: |-
    $\dfrac{L}{2}$
  feedback: |-
    The midpoint is the center of mass only when the masses are equal. The $4m$ mass pulls the weighted position toward its end, giving $x_{\mathrm{cm}}=L/5$ from that mass.
- id: p5-center-of-mass-d
  content: |-
    $\dfrac{L}{4}$
  feedback: |-
    Dividing the separation by the larger mass ratio omits the smaller mass from the total. The denominator must be $4m+m=5m$, so the position is $L/5$.
- id: p5-center-of-mass-e
  content: |-
    $\dfrac{5L}{4}$
  feedback: |-
    A center of mass of two positive masses must lie between them, so a position beyond $L$ is impossible here. The weighted-coordinate calculation gives $L/5$ from the $4m$ mass.
```

---

<a id="use-the-relative-orbit-to-find-the-period"></a>
## Use the Relative Orbit to Find the Period

**Example:** Masses $A$ and $B$ move in circular orbits about their common center of mass while remaining a fixed distance $s$ apart. Find their common period.

**Explanation**

Let $r_A$ and $r_B$ be their individual orbital radii. Both masses have the same angular speed $\omega$. Taking inward as positive, Newton's gravitational force supplies the radial acceleration of each mass:

$$
a_{r,A}=\omega^2r_A=\frac{GB}{s^2},
\qquad
a_{r,B}=\omega^2r_B=\frac{GA}{s^2}.
$$

Add the equations and use $r_A+r_B=s$:

$$
\begin{aligned}
\omega^2(r_A+r_B)
&=\frac{G(A+B)}{s^2},\\
\omega^2s
&=\frac{G(A+B)}{s^2},\\
\omega^2
&=\frac{G(A+B)}{s^3}.
\end{aligned}
$$

Therefore,

$$
T=\frac{2\pi}{\omega}
=2\pi\sqrt{\frac{s^3}{G(A+B)}}.
$$

The total mass $A+B$ belongs in the formula, and $s$ is the full separation.

As checks, $G(A+B)$ has units of length cubed per time squared, so $s^3/[G(A+B)]$ has units of time squared. Also, increasing $A+B$ at fixed $s$ must shorten the period; this confirms that total mass belongs in the denominator.

```quiz
type: radio
id: p5-orbital-period
shuffle: true
content: |-
  Stars of masses $2m$ and $m$ have circular orbits about their common center of mass and remain a distance $d$ apart. What is their orbital period?
options:
- id: p5-orbital-period-a
  content: |-
    $2\pi\sqrt{\dfrac{d^3}{3Gm}}$
  correct: true
  feedback: |-
    A circular two-body orbit obeys $T=2\pi\sqrt{d^3/[G(M+m)]}$. Here the full separation is $d$ and the total mass is $2m+m=3m$, so $T=2\pi\sqrt{d^3/(3Gm)}$.
- id: p5-orbital-period-b
  content: |-
    $2\pi\sqrt{\dfrac{d^3}{2Gm}}$
  feedback: |-
    This uses only the larger star's mass. Both stars accelerate about the center of mass, so their relative orbit is controlled by the total mass $2m+m=3m$, not by $2m$ alone.
- id: p5-orbital-period-c
  content: |-
    $2\pi\sqrt{\dfrac{d^3}{Gm}}$
  feedback: |-
    This treats the smaller star as orbiting a fixed central mass $m$. In a two-body system neither star is fixed; adding their radial-acceleration equations makes the controlling mass $2m+m=3m$.
- id: p5-orbital-period-d
  content: |-
    $2\pi\sqrt{\dfrac{(d/3)^3}{3Gm}}$
  feedback: |-
    The distance $d/3$ is the larger star's radius about the center of mass, but the two-body period formula uses the separation between the stars. Keeping the full separation gives $2\pi\sqrt{d^3/(3Gm)}$.
- id: p5-orbital-period-e
  content: |-
    $2\pi\sqrt{\dfrac{3d^3}{Gm}}$
  feedback: |-
    Total mass makes the gravitational acceleration stronger and therefore shortens the period, so it belongs in the denominator inside the square root. Using $M+m=3m$ gives $d^3/(3Gm)$, not $3d^3/(Gm)$.
```

---

<a id="use-the-circular-orbit-energy-shortcut"></a>
## Use the Circular-Orbit Energy Shortcut

**Example:** Masses $A$ and $B$ move in a circular orbit with separation $s$. Find the total mechanical energy.

**Explanation**

The gravitational potential energy uses the separation between the masses:

$$
U=-\frac{GAB}{s}.
$$

For a circular orbit, the total kinetic energy of both masses is

$$
K=\frac{GAB}{2s}.
$$

One way to verify this is to use

$$
r_A=\frac{B}{A+B}s,
\qquad
r_B=\frac{A}{A+B}s
$$

with $\omega^2=G(A+B)/s^3$:

$$
\begin{aligned}
K
&=\frac12\omega^2\left(Ar_A^2+Br_B^2\right)\\
&=\frac12\frac{G(A+B)}{s^3}
\left(\frac{AB}{A+B}s^2\right)\\
&=\frac{GAB}{2s}.
\end{aligned}
$$

Thus the total mechanical energy is

$$
E=K+U=-\frac{GAB}{2s}.
$$

The factor $1/2$ distinguishes total energy from gravitational potential energy. A bound circular system has $E<0$.

The expression also passes two quick checks: $GAB/s$ has units of energy, and as $s\to\infty$, the bound-state energy approaches zero from below.

```quiz
type: radio
id: p5-total-energy
shuffle: true
content: |-
  Stars of masses $2m$ and $m$ move in a circular orbit with separation $d$. What is the total mechanical energy of the two-star system?
options:
- id: p5-total-energy-a
  content: |-
    $-\dfrac{Gm^2}{d}$
  correct: true
  feedback: |-
    Circular-orbit energy is $E=-GMm/(2d)$. The mass product is $(2m)(m)=2m^2$, so the factor $2$ cancels the denominator $2$ and gives $E=-Gm^2/d$.
- id: p5-total-energy-b
  content: |-
    $-\dfrac{2Gm^2}{d}$
  feedback: |-
    This is the gravitational potential energy $U=-G(2m)(m)/d$, not the total mechanical energy. Circular motion has positive kinetic energy $K=-U/2$, leaving $E=U/2=-Gm^2/d$.
- id: p5-total-energy-c
  content: |-
    $\dfrac{Gm^2}{d}$
  feedback: |-
    This is the positive total kinetic energy for the circular orbit. Total mechanical energy also includes $U=-2Gm^2/d$, so $E=K+U=-Gm^2/d$ and remains negative for the bound system.
- id: p5-total-energy-d
  content: |-
    $-\dfrac{Gm^2}{2d}$
  feedback: |-
    This applies the circular-energy factor $1/2$ but treats both masses as $m$. The numerator uses the product $(2m)(m)=2m^2$, so $E=-G(2m^2)/(2d)=-Gm^2/d$.
- id: p5-total-energy-e
  content: |-
    $0$
  feedback: |-
    Zero total energy is the boundary between bound and unbound motion, not a circular gravitational orbit at finite separation. Here $E=-G(2m)(m)/(2d)=-Gm^2/d<0$.
```

---

<a id="carry-one-mass-ratio-through-the-full-system"></a>
## Carry One Mass Ratio Through the Full System

**Example:** Two stars of masses $M$ and $m$ orbit their common center of mass in circular orbits. Their separation is $d$, and $M=\tfrac32m$.

![](<../Source/2026-07-20-Q-2/Images/problem-5-binary-star-system.png>)

Find the center of mass measured from $M$, the orbital period, and the total mechanical energy.

**Explanation**

Keep the general formulas visible, identify the needed mass combination, and only then substitute the mass ratio:

| Quantity | General formula | With $M=\tfrac32m$ |
|---|---|---|
| Position from $M$ | $\dfrac{md}{M+m}$ | $M+m=\tfrac52m$ |
| Period | $2\pi\sqrt{\dfrac{d^3}{G(M+m)}}$ | $M+m=\tfrac52m$ |
| Total energy | $-\dfrac{GMm}{2d}$ | $Mm=\tfrac32m^2$ |

For the center of mass, place $M$ at $x=0$ and $m$ at $x=d$:

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{md}{M+m}\\
&=\frac{md}{(3/2)m+m}\\
&=\boxed{\frac{2d}{5}}.
\end{aligned}
$$

For the period, use the total mass:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{d^3}{G(M+m)}}\\
&=2\pi\sqrt{\frac{d^3}{G(5m/2)}}\\
&=\boxed{2\pi\sqrt{\frac{2d^3}{5Gm}}}.
\end{aligned}
$$

For the total energy, use the mass product and the full separation:

$$
\begin{aligned}
E
&=-\frac{GMm}{2d}\\
&=-\frac{G(3m/2)m}{2d}\\
&=\boxed{-\frac{3Gm^2}{4d}}.
\end{aligned}
$$

These results use different combinations of the same givens: a weighted coordinate for location, total mass for period, and mass product for energy.

```quiz
type: radio
id: p5-full-system
shuffle: true
content: |-
  Two stars of masses $M=3m$ and $m$ move in circular orbits with separation $d$. Which ordered triple gives $(x_{\mathrm{cm}}\text{ measured from }M,\ T,\ E)$?
options:
- id: p5-full-system-a
  content: |-
    $\left(\dfrac{d}{4},\ 2\pi\sqrt{\dfrac{d^3}{4Gm}},\ -\dfrac{3Gm^2}{2d}\right)$
  correct: true
  feedback: |-
    From the $3m$ star, $x_{\mathrm{cm}}=md/(3m+m)=d/4$. The period uses total mass $4m$, and the energy uses product $3m^2$, giving the displayed triple.
- id: p5-full-system-b
  content: |-
    $\left(\dfrac{3d}{4},\ 2\pi\sqrt{\dfrac{d^3}{4Gm}},\ -\dfrac{3Gm^2}{2d}\right)$
  feedback: |-
    The period and energy are consistent, but $3d/4$ is the smaller star's distance from the center of mass. Measured from the $3m$ star at $x=0$, the center is at $md/(4m)=d/4$.
- id: p5-full-system-c
  content: |-
    $\left(\dfrac{d}{4},\ 2\pi\sqrt{\dfrac{d^3}{3Gm}},\ -\dfrac{3Gm^2}{2d}\right)$
  feedback: |-
    This period uses only the larger mass $3m$. The relative orbit is controlled by the total mass $3m+m=4m$, so the period must contain $4Gm$ in the denominator.
- id: p5-full-system-d
  content: |-
    $\left(\dfrac{d}{4},\ 2\pi\sqrt{\dfrac{d^3}{4Gm}},\ -\dfrac{3Gm^2}{d}\right)$
  feedback: |-
    The last entry is the potential energy $U=-G(3m)(m)/d$. Total circular-orbit energy is half of $U$, so the correct energy is $-3Gm^2/(2d)$.
- id: p5-full-system-e
  content: |-
    $\left(\dfrac{d}{4},\ 2\pi\sqrt{\dfrac{(d/4)^3}{4Gm}},\ -\dfrac{6Gm^2}{d}\right)$
  feedback: |-
    This reuses the center-of-mass distance where the formulas require the star-to-star separation. The force, relative period, and pair energy use $d$, while $d/4$ is only the $3m$ star's individual orbital radius.
```

---

<a id="summary"></a>
## Summary

For two masses $M$ and $m$ in a circular orbit with separation $d$:

1. Choose an origin before locating the center of mass. From $M$ at $x=0$,
   $x_{\mathrm{cm}}=md/(M+m)$.
2. Use the **full separation** and **total mass** for the period:
   $T=2\pi\sqrt{d^3/[G(M+m)]}$.
3. Use the **full separation** and **mass product** for total energy:
   $E=-GMm/(2d)$.
4. Substitute a stated mass ratio only after writing the general formula.
5. Check that the center lies between the masses, the period has units of time, and the energy of the bound circular system is negative.

The main trap is treating one star's center-of-mass radius as though it were the separation between the stars.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
