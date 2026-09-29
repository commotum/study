# Solve a Pairwise Universal-Gravitation Equation

<!--
lesson-id: 212-M3-054
topic-code: MTH212.M3.54
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Pair Before Calculating](#read-the-pair)
- [Source-Video Concept: Earth–Moon Force Pair](#source-video-earth-moon)
- [Source-Video Calculation: Two Laboratory Masses](#source-video-laboratory-masses)
- [Source-Video Surface Checks: 20 kg and 25 kg Blocks](#source-video-surface-checks)
- [Source-Video Astronomical Pair: Sun and Earth](#source-video-sun-earth)
- [Source-Video Reverse Problem: Solve for Separation](#source-video-solve-separation)
- [Summary](#summary)

## Prerequisites

- Convert centimeters to meters and write large or small values in scientific notation.
- Apply exponent rules, especially $(a\times10^n)^2=a^2\times10^{2n}$.
- Rearrange a formula by multiplying or dividing both sides by the same quantity.
- Take the principal square root when the unknown represents a physical distance.
- Distinguish an object's altitude above a surface from its distance to a body's center.

---

<a id="introduction"></a>
## Introduction

For two masses treated as particles or spherically symmetric bodies, the magnitude of their mutual gravitational force is

$$
\boxed{F=G\frac{m_1m_2}{r^2}},
\qquad
G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}.
$$

Every problem in this lesson uses one move:

1. Identify the two interacting masses.
2. Find their **center-to-center** separation $r$ in meters.
3. Predict how the answer should change from $F\propto m_1m_2/r^2$.
4. Isolate the requested variable.
5. Substitute, keeping the entire distance inside the square.
6. Check the direction of change, units, and Newton's-third-law force pair.

The unit check for a force calculation is

$$
\left(\frac{\mathrm{N\,m^2}}{\mathrm{kg^2}}\right)
(\mathrm{kg})(\mathrm{kg})\frac{1}{\mathrm{m^2}}
=\mathrm N.
$$

Because $G$ is small, ordinary laboratory masses exert tiny gravitational forces. The much larger mass products in planetary and stellar pairs produce forces on an astronomical scale.

---

<a id="read-the-pair"></a>
## Read the Pair Before Calculating

The symbol $r$ never means “whatever distance appears in the prompt.” It is the distance from one mass center to the other mass center.

- Two compact objects $0.50\ \mathrm m$ apart: $r=0.50\ \mathrm m$.
- A small block resting at Earth's surface: $r\approx R_E$.
- An object at altitude $h$ above Earth: $r=R_E+h$, not $h$.
- Two spheres with radii $R_1$ and $R_2$ and a surface gap $d$: $r=R_1+d+R_2$.

This distinction also appears in the M3-1 lecture-note example with $h=R_E/3$:

$$
r=R_E+\frac{R_E}{3}=\frac{4R_E}{3}.
$$

Thus the gravitational acceleration relative to its surface value is

$$
\frac{g_h}{g_0}
=\left(\frac{R_E}{4R_E/3}\right)^2
=\left(\frac34\right)^2
=\frac{9}{16}.
$$

Before using a calculator, compare two situations with

$$
\boxed{
\frac{F'}{F}
=\frac{m_1'}{m_1}
\frac{m_2'}{m_2}
\left(\frac{r}{r'}\right)^2
}.
$$

This ratio exposes a missing square or an inverted distance factor immediately.

The same relationship can be written as a product check. When the masses stay fixed,

$$
\boxed{Fr^2=Gm_1m_2=\text{constant}}.
$$

Thus $F'r'^2=Fr^2$. This is the inverse-variation product check applied to the variable $r^2$, rather than to $r$ itself. With $r$ fixed, $F$ instead varies directly with either mass.

```quiz
type: radio
id: mct-p18-center-distance
shuffle: true
content: |-
  A $12\,\mathrm{kg}$ probe is at altitude $h=1.6\times10^6\,\mathrm m$ above a planet of radius $R=6.4\times10^6\,\mathrm m$ and mass $M$. Which substitution correctly sets up the force magnitude on the probe?
options:
- id: mct-p18-center-distance-a
  content: |-
    $\displaystyle F=\frac{GM(12)}{(8.0\times10^6)^2}$
  correct: true
  feedback: |-
    The force law needs the center-to-center distance: $r=R+h=(6.4+1.6)\times10^6=8.0\times10^6\,\mathrm m$. The entire sum is squared.
- id: mct-p18-center-distance-b
  content: |-
    $\displaystyle F=\frac{GM(12)}{(1.6\times10^6)^2}$
  feedback: |-
    This uses altitude as though it were center-to-center separation. Add the planet's radius first: $r=R+h$.
- id: mct-p18-center-distance-c
  content: |-
    $\displaystyle F=\frac{GM(12)}{(6.4\times10^6)^2}$
  feedback: |-
    The planet's radius reaches only to the surface. The probe is another $1.6\times10^6\,\mathrm m$ above that surface, so $r=R+h$.
- id: mct-p18-center-distance-d
  content: |-
    $\displaystyle F=\frac{GM(12)}{8.0\times10^{12}}$
  feedback: |-
    The center distance is correct before squaring, but $(8.0\times10^6)^2=64\times10^{12}=6.4\times10^{13}$, not $8.0\times10^{12}$.
- id: mct-p18-center-distance-e
  content: |-
    $\displaystyle F=\frac{GM(12)}{6.4\times10^6+1.6\times10^{12}}$
  feedback: |-
    This squares only the altitude term. First add the two distances, then square the entire sum: $(R+h)^2$.
```

---

<a id="source-video-earth-moon"></a>
## Source-Video Concept: Earth–Moon Force Pair

In `8CykJ3NgBQs` at 1:25-4:01, Earth and the Moon form one interacting pair. If $\hat r$ points from Earth toward the Moon, then the forces may be written

$$
\vec F_{E\leftarrow M}=+\frac{GM_EM_M}{r^2}\hat r,
\qquad
\vec F_{M\leftarrow E}=-\frac{GM_EM_M}{r^2}\hat r.
$$

Their magnitudes are equal:

$$
\left|\vec F_{E\leftarrow M}\right|
=\left|\vec F_{M\leftarrow E}\right|.
$$

The forces point in opposite directions because gravity is attractive. They act on different bodies, so they do not cancel in either body's individual force equation.

The same segment supplies two quick scaling checks:

$$
r' = 2r
\quad\Longrightarrow\quad
F'=\frac{F}{2^2}=\frac14F,
$$

and

$$
m_1'=2m_1
\quad\Longrightarrow\quad
F'=2F.
$$

**Misconception correction.** The more massive body does not feel the larger member of this force pair. Both force magnitudes are $F$. The more massive body has the smaller acceleration because $a=F/m$.

```quiz
type: radio
id: mct-p18-third-law-pair
shuffle: true
content: |-
  Planet A has five times the mass of planet B. The planets interact only with each other. Which statement about this pair is correct at a given instant?
options:
- id: mct-p18-third-law-pair-a
  content: |-
    The force magnitudes are equal and opposite, while B's acceleration magnitude is five times A's.
  correct: true
  feedback: |-
    Newton's third law gives equal-magnitude, opposite-direction forces. Since $a=F/m$ and $m_A=5m_B$, $a_B/a_A=m_A/m_B=5$.
- id: mct-p18-third-law-pair-b
  content: |-
    A feels five times the force that B feels, and their accelerations are equal.
  feedback: |-
    The shared product $Gm_Am_B/r^2$ gives the same force magnitude on each body. Different masses make their accelerations different, not their pair forces.
- id: mct-p18-third-law-pair-c
  content: |-
    B feels five times the force that A feels, so B accelerates five times as much.
  feedback: |-
    B does accelerate five times as much, but not because its force is larger. The force magnitudes are equal; B's smaller mass produces its larger acceleration.
- id: mct-p18-third-law-pair-d
  content: |-
    The forces cancel, so neither planet accelerates.
  feedback: |-
    The two forces act on different planets. They cancel only when summing internal forces for the combined two-planet system, not in either planet's individual equation of motion.
- id: mct-p18-third-law-pair-e
  content: |-
    A and B have equal acceleration magnitudes because the forces have equal magnitudes.
  feedback: |-
    Equal force does not imply equal acceleration when the masses differ. From $a=F/m$, the less massive planet B accelerates more.
```

---

<a id="source-video-laboratory-masses"></a>
## Source-Video Calculation: Two Laboratory Masses

Problem 1 in `Ep1jIhHdf2A` uses

$$
m_1=60\ \mathrm{kg},
\qquad
m_2=80\ \mathrm{kg},
\qquad
r=50\ \mathrm{cm}=0.50\ \mathrm m.
$$

The unit conversion belongs before the force calculation. Then square the whole value $0.50\ \mathrm m$:

$$
\begin{aligned}
F
&=\frac{(6.67\times10^{-11})(60)(80)}{(0.50)^2}\\
&=1.28064\times10^{-6}\ \mathrm N\\
&\approx\boxed{1.28\times10^{-6}\ \mathrm N}.
\end{aligned}
$$

Each mass experiences this magnitude, toward the other mass.

For scientific notation, separate coefficients from powers of ten:

$$
\frac{(a\times10^p)(b\times10^q)}{(c\times10^s)^2}
=\frac{ab}{c^2}\times10^{p+q-2s}.
$$

**Caption repair.** The automatic captions in both source videos flatten or garble several powers of ten. The written formulas and problem frames show $G=6.67\times10^{-11}$ and the exponents used below; those are the values retained here.

```quiz
type: radio
id: mct-p18-lab-mirror
shuffle: true
content: |-
  Two compact masses, $75\,\mathrm{kg}$ and $40\,\mathrm{kg}$, have centers $0.30\,\mathrm m$ apart. What is the gravitational force magnitude between them?
options:
- id: mct-p18-lab-mirror-a
  content: |-
    $2.22\times10^{-6}\,\mathrm N$
  correct: true
  feedback: |-
    $F=(6.67\times10^{-11})(75)(40)/(0.30)^2=2.223\ldots\times10^{-6}\,\mathrm N$, which rounds to $2.22\times10^{-6}\,\mathrm N$.
- id: mct-p18-lab-mirror-b
  content: |-
    $6.67\times10^{-7}\,\mathrm N$
  feedback: |-
    This divides by $0.30$ rather than $(0.30)^2$. The inverse-square law requires the entire center distance to be squared.
- id: mct-p18-lab-mirror-c
  content: |-
    $2.22\times10^{-10}\,\mathrm N$
  feedback: |-
    This is the result of treating $0.30\,\mathrm m$ as $30\,\mathrm m$. The supplied separation is already in meters; do not convert it again.
- id: mct-p18-lab-mirror-d
  content: |-
    $1.80\times10^{-8}\,\mathrm N$
  feedback: |-
    This multiplies by $r^2$ instead of dividing by it. Gravitational force is inversely proportional to the square of the separation.
- id: mct-p18-lab-mirror-e
  content: |-
    $4.45\times10^{-6}\,\mathrm N$
  feedback: |-
    This doubles the answer to account for two bodies. $F$ is already the magnitude on each body; Newton's-third-law partners are equal, not added into one body's force.
```

---

<a id="source-video-surface-checks"></a>
## Source-Video Surface Checks: 20 kg and 25 kg Blocks

The second segment of `8CykJ3NgBQs`, at 4:01-6:58, checks a $20\ \mathrm{kg}$ block at Earth's surface using

$$
M_E=5.98\times10^{24}\ \mathrm{kg},
\qquad
R_E=6.38\times10^6\ \mathrm m.
$$

The block is tiny compared with Earth, so its center-to-center separation from Earth is approximated by $R_E$:

$$
\begin{aligned}
F
&=\frac{(6.67\times10^{-11})(5.98\times10^{24})(20)}{(6.38\times10^6)^2}\\
&=\boxed{195.98\ \mathrm N}.
\end{aligned}
$$

The near-surface model $F=mg$ gives

$$
F=(20)(9.8)=196\ \mathrm N,
$$

so the two calculations agree to the precision of the rounded constants.

Problem 2 in `Ep1jIhHdf2A` repeats the check with

$$
m=25\ \mathrm{kg},
\qquad
M_E=5.97\times10^{24}\ \mathrm{kg},
\qquad
R_E=6.38\times10^6\ \mathrm m.
$$

The video frame gives

$$
\begin{aligned}
F
&=\frac{(6.67\times10^{-11})(25)(5.97\times10^{24})}{(6.38\times10^6)^2}\\
&=\boxed{244.6\ \mathrm N}.
\end{aligned}
$$

This is about $25(9.8)=245\ \mathrm N$. The first calculation uses $5.98\times10^{24}\ \mathrm{kg}$ for Earth and the second uses $5.97\times10^{24}\ \mathrm{kg}$; preserving those source values explains the slightly different rounded results.

**Distance warning.** If a block were at altitude $h$, the denominator would be $(R_E+h)^2$. Substituting $h^2$ would make the force much too large.

```quiz
type: radio
id: mct-p18-scaling-control
shuffle: true
content: |-
  In a second trial, one mass is tripled, the other mass is unchanged, and the center-to-center separation is doubled. What is the new gravitational force in terms of the original force $F$?
options:
- id: mct-p18-scaling-control-a
  content: |-
    $\displaystyle \frac34F$
  correct: true
  feedback: |-
    The mass change supplies a factor of $3$, while doubling distance supplies $1/2^2=1/4$. Their product is $3/4$.
- id: mct-p18-scaling-control-b
  content: |-
    $\displaystyle \frac32F$
  feedback: |-
    This treats force as inverse in $r$ rather than inverse in $r^2$. Doubling separation contributes a factor of $1/4$, not $1/2$.
- id: mct-p18-scaling-control-c
  content: |-
    $\displaystyle \frac14F$
  feedback: |-
    This accounts for the doubled separation but ignores that one mass was tripled. Multiply the distance factor $1/4$ by the mass factor $3$.
- id: mct-p18-scaling-control-d
  content: |-
    $6F$
  feedback: |-
    This multiplies by the distance factor instead of dividing by its square. Greater separation weakens the gravitational force.
- id: mct-p18-scaling-control-e
  content: |-
    $12F$
  feedback: |-
    This multiplies the mass factor by $2^2$. Because distance is in the denominator, the correct distance factor is $1/2^2$.
```

---

<a id="source-video-sun-earth"></a>
## Source-Video Astronomical Pair: Sun and Earth

Problem 3 in `Ep1jIhHdf2A` uses

$$
M_S=1.99\times10^{30}\ \mathrm{kg},
\qquad
M_E=5.97\times10^{24}\ \mathrm{kg},
\qquad
r=1.496\times10^{11}\ \mathrm m.
$$

Predict first: the immense mass product overcomes the small value of $G$, so an astronomical force is reasonable. Now calculate:

$$
\begin{aligned}
F
&=\frac{(6.67\times10^{-11})(1.99\times10^{30})(5.97\times10^{24})}
{(1.496\times10^{11})^2}\\
&=3.5407\ldots\times10^{22}\ \mathrm N\\
&\approx\boxed{3.54\times10^{22}\ \mathrm N}.
\end{aligned}
$$

The Sun pulls on Earth with this magnitude toward the Sun. Earth pulls on the Sun with the same magnitude toward Earth. The Sun's acceleration is much smaller because its mass is much larger.

The M3-1 lecture notes compare gravity with the electric force between two electrons and find $F_e/F_g\approx4\times10^{42}$. That comparison changes the scale, not the calculation here: for a gravitational pair, the same $Gm_1m_2/r^2$ move still applies.

---

<a id="source-video-solve-separation"></a>
## Source-Video Reverse Problem: Solve for Separation

Problem 4 in `Ep1jIhHdf2A`, whose prompt is visible at 7:15, asks for the separation of planets with

$$
m_1=3.0\times10^{24}\ \mathrm{kg},
\qquad
m_2=4.5\times10^{25}\ \mathrm{kg},
\qquad
F=3.6\times10^{20}\ \mathrm N.
$$

Isolate $r^2$ before substituting:

$$
\begin{aligned}
F&=\frac{Gm_1m_2}{r^2},\\
Fr^2&=Gm_1m_2,\\
r^2&=\frac{Gm_1m_2}{F},\\
r&=\sqrt{\frac{Gm_1m_2}{F}}.
\end{aligned}
$$

Algebraically, an equation containing $r^2$ can produce positive and negative roots. Physical separation is nonnegative, so retain the principal root:

$$
\left[\frac{Gm_1m_2}{F}\right]
=\frac{(\mathrm{N\,m^2/kg^2})(\mathrm{kg^2})}{\mathrm N}
=\mathrm{m^2},
$$

which confirms that its square root has units of meters.

$$
\begin{aligned}
r
&=\sqrt{\frac{(6.67\times10^{-11})(3.0\times10^{24})(4.5\times10^{25})}
{3.6\times10^{20}}}\\
&=5.001\ldots\times10^9\ \mathrm m\\
&\approx\boxed{5.0\times10^9\ \mathrm m}.
\end{aligned}
$$

A useful direction check is built into the rearranged formula: for fixed masses, a smaller specified force must correspond to a larger separation.

```quiz
type: radio
id: mct-p18-separation-variation
shuffle: true
content: |-
  Two planets have masses $6.0\times10^{24}\,\mathrm{kg}$ and $4.0\times10^{25}\,\mathrm{kg}$. Their mutual gravitational force has magnitude $1.00\times10^{21}\,\mathrm N$. What is their center-to-center separation?
options:
- id: mct-p18-separation-variation-a
  content: |-
    $4.00\times10^9\,\mathrm m$
  correct: true
  feedback: |-
    $r=\sqrt{Gm_1m_2/F}=\sqrt{1.6008\times10^{19}}=4.001\ldots\times10^9\,\mathrm m$, which rounds to $4.00\times10^9\,\mathrm m$.
- id: mct-p18-separation-variation-b
  content: |-
    $1.60\times10^{19}\,\mathrm m$
  feedback: |-
    This is the value of $r^2$ before taking the square root. The requested separation is $r$, so take the principal square root and check that the result has units of meters.
- id: mct-p18-separation-variation-c
  content: |-
    $2.50\times10^{-10}\,\mathrm m$
  feedback: |-
    This inverts the rearranged expression. From $Fr^2=Gm_1m_2$, the correct relation is $r^2=Gm_1m_2/F$.
- id: mct-p18-separation-variation-d
  content: |-
    $-4.00\times10^9\,\mathrm m$
  feedback: |-
    A negative algebraic root cannot represent a center-to-center distance. Physical separation uses the nonnegative principal square root.
- id: mct-p18-separation-variation-e
  content: |-
    $1.27\times10^9\,\mathrm m$
  feedback: |-
    This computes $\sqrt{1.6008}\times10^9$ and effectively drops the extra factor from the odd exponent $10^{19}$. Rewrite $1.6008\times10^{19}$ as $16.008\times10^{18}$ before taking the square root; the result is about $4.00\times10^9\,\mathrm m$.
```

---

<a id="summary"></a>
## Summary

- For one gravitational pair,
  $$
  F=G\frac{m_1m_2}{r^2}.
  $$
- Use the center-to-center separation. At altitude $h$ above a spherical body, $r=R+h$.
- Convert every distance to meters before squaring the entire value.
- Predict with $F\propto m_1m_2/r^2$: doubling one mass doubles $F$, while doubling $r$ quarters $F$.
- Carry units through the formula; a force result must reduce to newtons.
- The two bodies feel equal-magnitude, opposite-direction forces. Different masses cause different accelerations, not different pair-force magnitudes.
- When solving for separation,
  $$
  r=\sqrt{\frac{Gm_1m_2}{F}},
  $$
  and physical distance uses the nonnegative root.
- Use scientific-notation exponents as a magnitude check before trusting a calculator result.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
