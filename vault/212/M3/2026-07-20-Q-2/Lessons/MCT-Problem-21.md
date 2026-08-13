# Use Kepler's Third Law for Period, Radius, or Central Mass

<!--
lesson-id: 212-M3-057
topic-code: MTH212.M3.57
-->

## Table of Contents

- [Introduction](#introduction)
- [Derive the Circular-Orbit Form](#derive-circular-form)
- [Match the Two Orbits Before Taking a Ratio](#match-orbits)
- [Source-Video Problem 1: Find Mars's Period](#source-video-mars-period)
- [Source-Video Problem 2: Find Venus's Orbital Size](#source-video-venus-distance)
- [Source-Video Problems 3–4: Infer the Attracting Mass](#source-video-central-mass)
- [Summary](#summary)

## Prerequisites

- Use Newton's law of gravitation and $a_r=v^2/r$ for circular motion.
- Use $v=2\pi r/T$ for one circular revolution.
- Rearrange proportions while keeping corresponding quantities paired.
- Solve equations by taking square roots, cube roots, or fractional powers.
- Convert days to seconds with unit-canceling conversion factors.
- Distinguish altitude above a body from center-to-center orbital distance.

---

<a id="introduction"></a>
## Introduction

Kepler's third law connects an orbital period $T$ with an orbit's size. For a general two-body orbit,

$$
\boxed{T^2=\frac{4\pi^2a^3}{G(M+m)}},
$$

where $a$ is the semi-major axis of the relative orbit and $M+m$ is the total mass of the two bodies. When the orbiter's mass $m$ is negligible compared with the attracting mass $M$,

$$
T^2\approx\frac{4\pi^2a^3}{GM}.
$$

For a circular orbit, $a=r$, the center-to-center orbital radius. The source examples use nearly circular planetary or lunar orbits, so their stated mean distances are used as $a$.

Choose the form from the data:

- **Two negligible-mass orbiters around the same central body:** use a ratio, so $G$, $4\pi^2$, and the shared $M$ cancel.
- **One orbit used to infer the attracting mass:** use the absolute formula, convert $T$ to seconds and $a$ to meters, then solve for $M+m$.

For the same central body,

$$
\boxed{\left(\frac{T_2}{T_1}\right)^2
=\left(\frac{a_2}{a_1}\right)^3}.
$$

Equivalently, each orbit has the same proportionality constant:

$$
\boxed{\frac{T^2}{a^3}=\frac{4\pi^2}{G(M+m)}}.
$$

The right side is shared only when the relevant mass sum is shared or the orbiters are negligible compared with the same central mass.

From this one equation,

$$
T_2=T_1\left(\frac{a_2}{a_1}\right)^{3/2},
\qquad
a_2=a_1\left(\frac{T_2}{T_1}\right)^{2/3}.
$$

The ratio form may use days, years, meters, or astronomical units as long as both periods use the same time unit and both semi-major axes use the same distance unit. The absolute formula must match the SI units built into

$$
G=6.67\times10^{-11}\ \mathrm{m^3/(kg\,s^2)}.
$$

---

<a id="derive-circular-form"></a>
## Derive the Circular-Orbit Form

The source video `CCsbSq9wlyI` at 0:00-4:38 derives the relation for a small mass $m$ in a circular orbit of radius $r$ about a much larger mass $M$. Gravity supplies the inward radial force:

$$
\frac{GMm}{r^2}=m\frac{v^2}{r}.
$$

Cancel $m$ and one factor of $r$:

$$
\frac{GM}{r}=v^2.
$$

One circular revolution covers $2\pi r$ in one period, so

$$
v=\frac{2\pi r}{T},
\qquad
v^2=\frac{4\pi^2r^2}{T^2}.
$$

Substitute and rearrange:

$$
\begin{aligned}
\frac{GM}{r}&=\frac{4\pi^2r^2}{T^2},\\
GMT^2&=4\pi^2r^3,\\
T^2&=\frac{4\pi^2r^3}{GM}.
\end{aligned}
$$

Dividing this equation for orbit 2 by the equation for orbit 1 cancels the shared $4\pi^2/(GM)$ and produces the ratio form.

**Caption repair.** The automatic captions repeatedly render “centripetal” as “triple.” The written derivation and the physics both set the gravitational force equal to the required centripetal net force.

**Model correction.** The displayed derivation assumes a circular orbit and $M\gg m$. The general law uses the semi-major axis $a$ and the mass sum $M+m$. Thus the simple ratio is not valid for two orbits around different central masses, and it is not exact when the orbiters' masses make different non-negligible contributions to $M+m$.

```quiz
type: radio
id: mct-p21-ratio-condition
shuffle: true
content: |-
  Which comparison can use $\left(T_2/T_1\right)^2=\left(a_2/a_1\right)^3$ directly, without inserting $G$ or either mass?
options:
- id: mct-p21-ratio-condition-a
  content: |-
    Two negligible-mass satellites orbit the same planet, and each period is paired with its own center-to-center semi-major axis.
  correct: true
  feedback: |-
    Both orbits share the same dominant central mass, so $4\pi^2/(GM)$ cancels. Pairing each $T_i$ with its own $a_i$ gives the stated ratio directly.
- id: mct-p21-ratio-condition-b
  content: |-
    One moon orbits Earth and another moon orbits Mars.
  feedback: |-
    Each moon obeys Kepler's law, but the central masses differ. The $GM$ factors do not cancel, so the simple same-center ratio cannot be used.
- id: mct-p21-ratio-condition-c
  content: |-
    Two binary systems have the same semi-major axis but different total masses.
  feedback: |-
    The exact law contains $M+m$. Different total masses give different proportionality constants, so equal $a$ does not support the simple ratio.
- id: mct-p21-ratio-condition-d
  content: |-
    Two satellites orbit the same planet, but their altitudes $h_1$ and $h_2$ are substituted directly for $a_1$ and $a_2$.
  feedback: |-
    The shared central mass is suitable, but altitude is not orbital radius. For circular orbits use $a=r=R+h$ before forming the ratio.
- id: mct-p21-ratio-condition-e
  content: |-
    Two planets orbit the same star, but $T_1$ is paired with $a_2$ and $T_2$ with $a_1$.
  feedback: |-
    Sharing a star lets the constants cancel, but corresponding quantities must stay together. Orbit 1 requires the pair $(T_1,a_1)$ and orbit 2 requires $(T_2,a_2)$.
```

---

<a id="match-orbits"></a>
## Match the Two Orbits Before Taking a Ratio

The ratio subscripts are labels, not a required inside/outside order. Choose orbit 1, keep its $T_1$ with its $a_1$, then place every orbit-2 quantity in the same numerator position:

| Orbit label | Period | Matching semi-major axis | Ratio position |
| --- | ---: | ---: | --- |
| Orbit 1 | $T_1$ | $a_1$ | denominator |
| Orbit 2 | $T_2$ | $a_2$ | numerator |

$$
\frac{T_2^2}{T_1^2}=\frac{a_2^3}{a_1^3}.
$$

Before arithmetic, compare $a_2$ with $a_1$:

- If $a_2>a_1$, then $T_2>T_1$.
- If $a_2<a_1$, then $T_2<T_1$.

The M3-1 lecture notes choose a period ratio that can be evaluated without a calculator. A planet around the same star as Earth has

$$
T_p=8T_E.
$$

Then

$$
\left(\frac{T_p}{T_E}\right)^2
=\left(\frac{a_p}{a_E}\right)^3
\quad\Longrightarrow\quad
8^2=\left(\frac{a_p}{a_E}\right)^3.
$$

Taking the cube root gives

$$
\frac{a_p}{a_E}=\sqrt[3]{64}=4.
$$

Thus $a_p=4a_E$, or $4.0\ \mathrm{AU}$ when $a_E=1\ \mathrm{AU}$.

```quiz
type: radio
id: mct-p21-lecture-ratio-warmup
shuffle: true
content: |-
  Two low-mass planets orbit the same star. Planet B's period is $27$ times planet A's period. What is the ratio $a_B/a_A$?
options:
- id: mct-p21-lecture-ratio-warmup-a
  content: |-
    $9$
  correct: true
  feedback: |-
    For the same central mass, $(T_B/T_A)^2=(a_B/a_A)^3$. Thus $(a_B/a_A)^3=27^2=729$, so $a_B/a_A=\sqrt[3]{729}=9$.
- id: mct-p21-lecture-ratio-warmup-b
  content: |-
    $3$
  feedback: |-
    This takes only the cube root of the period ratio. Kepler's law first squares $T_B/T_A$, so the required calculation is $\sqrt[3]{27^2}=9$.
- id: mct-p21-lecture-ratio-warmup-c
  content: |-
    $27$
  feedback: |-
    This assumes period and semi-major axis scale linearly. Kepler's law instead gives $a_B/a_A=(T_B/T_A)^{2/3}=9$.
- id: mct-p21-lecture-ratio-warmup-d
  content: |-
    $729$
  feedback: |-
    Squaring the period ratio gives the cube of the distance ratio, not the distance ratio itself. Take the cube root of $729$ to obtain $9$.
- id: mct-p21-lecture-ratio-warmup-e
  content: |-
    $1/9$
  feedback: |-
    This reverses the distance ratio. Because $T_B>T_A$, the direction check requires $a_B>a_A$, so $a_B/a_A$ must exceed $1$.
```

---

<a id="source-video-mars-period"></a>
## Source-Video Problem 1: Find Mars's Period

At 4:38-9:06, the source gives the Earth–Sun orbit as reference orbit 1:

$$
a_1=1.50\times10^{11}\ \mathrm m,
\qquad
T_1=365\ \mathrm d.
$$

Mars is orbit 2:

$$
a_2=2.287\times10^{11}\ \mathrm m,
\qquad
T_2=?
$$

Both planets orbit the Sun and their masses are negligible compared with the Sun, so use the ratio form. Mars has the larger semi-major axis, so its period must be longer than $365\ \mathrm d$:

$$
T_2^2=T_1^2\left(\frac{a_2}{a_1}\right)^3.
$$

Take the nonnegative square root because an orbital period is positive:

$$
\begin{aligned}
T_2
&=T_1\left(\frac{a_2}{a_1}\right)^{3/2}\\
&=(365\ \mathrm d)
\left(\frac{2.287\times10^{11}}{1.50\times10^{11}}\right)^{3/2}\\
&=687.16\ldots\ \mathrm d\\
&\approx\boxed{687\ \mathrm d}.
\end{aligned}
$$

There is no need to convert days to seconds because $T_2/T_1$ is a ratio of like units. Likewise, the shared factor $10^{11}\ \mathrm m$ cancels from $a_2/a_1$.

```quiz
type: radio
id: mct-p21-period-mirror
shuffle: true
content: |-
  Two low-mass planets orbit the same star. Planet 1 has $a_1=5.0\times10^{11}\,\mathrm m$ and $T_1=500\,\mathrm d$. Planet 2 has $a_2=3.2\times10^{11}\,\mathrm m$. What is $T_2$?
options:
- id: mct-p21-period-mirror-a
  content: |-
    $256\,\mathrm d$
  correct: true
  feedback: |-
    The same-star ratio gives $T_2=T_1(a_2/a_1)^{3/2}=500(3.2/5.0)^{3/2}=256\,\mathrm d$. The smaller orbit correctly has the shorter period.
- id: mct-p21-period-mirror-b
  content: |-
    $400\,\mathrm d$
  feedback: |-
    This scales period linearly by $a_2/a_1=0.64$. Kepler's law requires the power $3/2$, giving $500(0.64)^{3/2}=256\,\mathrm d$.
- id: mct-p21-period-mirror-c
  content: |-
    $204.8\,\mathrm d$
  feedback: |-
    This uses the square of the distance ratio, $500(0.64)^2$. Solving $T^2\propto a^3$ for $T$ gives exponent $3/2$, not $2$.
- id: mct-p21-period-mirror-d
  content: |-
    $976.6\,\mathrm d$
  feedback: |-
    This uses the inverted ratio $(a_1/a_2)^{3/2}$. Since planet 2's orbit is smaller, its period must be less than $500\,\mathrm d$, not greater.
- id: mct-p21-period-mirror-e
  content: |-
    $131\,\mathrm d$
  feedback: |-
    This cubes the distance ratio directly, $500(0.64)^3$. The cube belongs to $a$ before comparing with $T^2$; after solving for $T$, the exponent is $3/2$.
```

---

<a id="source-video-venus-distance"></a>
## Source-Video Problem 2: Find Venus's Orbital Size

At 9:06-12:06, Earth remains orbit 1:

$$
T_1=365\ \mathrm d,
\qquad
a_1=1.50\times10^{11}\ \mathrm m.
$$

For Venus,

$$
T_2=225\ \mathrm d,
\qquad
a_2=?
$$

Venus has the shorter period, so its semi-major axis must be smaller than Earth's. Isolate the cubed distance ratio, then take the cube root:

$$
\begin{aligned}
a_2^3
&=a_1^3\left(\frac{T_2}{T_1}\right)^2,\\
a_2
&=\sqrt[3]{a_1^3\left(\frac{T_2}{T_1}\right)^2}
=a_1\left(\frac{T_2}{T_1}\right)^{2/3}.
\end{aligned}
$$

$$
\begin{aligned}
a_2
&=(1.50\times10^{11}\ \mathrm m)
\left(\frac{225}{365}\right)^{2/3}\\
&=1.08647\ldots\times10^{11}\ \mathrm m\\
&\approx\boxed{1.086\times10^{11}\ \mathrm m}.
\end{aligned}
$$

This agrees with the source's direction check: Venus's orbit is inside Earth's, and $1.086\times10^{11}\ \mathrm m<1.50\times10^{11}\ \mathrm m$.

**Distance correction.** Kepler's general third law uses semi-major axis, not an arbitrary time-average distance or instantaneous separation. The video's “mean distance” values serve as semi-major-axis approximations for these nearly circular examples. For a circular satellite at altitude $h$, use $a=r=R+h$, not $h$.

```quiz
type: radio
id: mct-p21-radius-variation
shuffle: true
content: |-
  Two negligible-mass satellites orbit the same planet. Satellite 1 has $T_1=24\,\mathrm d$ and $a_1=9.0\times10^8\,\mathrm m$. Satellite 2 has $T_2=3.0\,\mathrm d$. What is $a_2$?
options:
- id: mct-p21-radius-variation-a
  content: |-
    $2.25\times10^8\,\mathrm m$
  correct: true
  feedback: |-
    For a shared central mass, $a_2=a_1(T_2/T_1)^{2/3}$. Here $T_2/T_1=1/8$, so the distance factor is $(1/8)^{2/3}=1/4$ and $a_2=2.25\times10^8\,\mathrm m$.
- id: mct-p21-radius-variation-b
  content: |-
    $1.125\times10^8\,\mathrm m$
  feedback: |-
    This scales distance linearly by the period ratio $1/8$. Solving $T^2\propto a^3$ for $a$ requires the power $2/3$, which gives a factor of $1/4$.
- id: mct-p21-radius-variation-c
  content: |-
    $5.625\times10^7\,\mathrm m$
  feedback: |-
    This squares the period ratio: $9.0\times10^8(1/8)^2$. The squared period ratio equals the cubed distance ratio, so take a cube root and use exponent $2/3$.
- id: mct-p21-radius-variation-d
  content: |-
    $4.50\times10^8\,\mathrm m$
  feedback: |-
    This takes only the cube root of $1/8$ and omits the square on the period ratio. The full factor is $(1/8)^{2/3}=1/4$, not $1/2$.
- id: mct-p21-radius-variation-e
  content: |-
    $3.60\times10^9\,\mathrm m$
  feedback: |-
    This reverses the period ratio before applying the $2/3$ power. Because $T_2<T_1$, the direction check requires $a_2<a_1$.
```

---

<a id="source-video-central-mass"></a>
## Source-Video Problems 3–4: Infer the Attracting Mass

For an absolute calculation, rearrange the general form:

$$
\boxed{M+m=\frac{4\pi^2a^3}{GT^2}}.
$$

If $m\ll M$, the measured value is reported as the central mass:

$$
M\approx\frac{4\pi^2a^3}{GT^2}.
$$

The dimensions confirm that this expression returns mass:

$$
\left[\frac{a^3}{GT^2}\right]
=\frac{\mathrm{m^3}}
{\left(\mathrm{m^3/(kg\,s^2)}\right)\mathrm{s^2}}
=\mathrm{kg}.
$$

### Problem 3: Earth Orbit Used to Infer the Sun's Mass

At 12:06-16:11, the source uses

$$
a=1.50\times10^{11}\ \mathrm m,
\qquad
T=365\ \mathrm d.
$$

Because $G$ is in SI units, convert the period:

$$
T=(365\ \mathrm d)
\left(\frac{24\ \mathrm h}{1\ \mathrm d}\right)
\left(\frac{60\ \mathrm{min}}{1\ \mathrm h}\right)
\left(\frac{60\ \mathrm s}{1\ \mathrm{min}}\right)
=31{,}536{,}000\ \mathrm s.
$$

Then

$$
\begin{aligned}
M_S+M_E
&=\frac{4\pi^2(1.50\times10^{11})^3}
{(6.67\times10^{-11})(31{,}536{,}000)^2}\\
&=2.0086\ldots\times10^{30}\ \mathrm{kg}.
\end{aligned}
$$

Since $M_E\ll M_S$, the source reports

$$
\boxed{M_S\approx2.01\times10^{30}\ \mathrm{kg}}.
$$

### Problem 4: Moon Orbit Used to Infer Earth's Mass

At 16:11-18:43, the source uses

$$
a=3.84\times10^8\ \mathrm m,
\qquad
T=27.4\ \mathrm d
=2{,}367{,}360\ \mathrm s.
$$

Using the source's rounded orbital size and period, substitution gives

$$
\begin{aligned}
M_E+M_M
&=\frac{4\pi^2(3.84\times10^8)^3}
{(6.67\times10^{-11})(2{,}367{,}360)^2}\\
&=5.97997\ldots\times10^{24}\ \mathrm{kg}\\
&\approx\boxed{5.98\times10^{24}\ \mathrm{kg}}.
\end{aligned}
$$

**Source correction.** An orbit determines the mass sum $M_E+M_M$, not $M_E$ alone. Calling this result Earth's mass uses the approximation $M_M\ll M_E$. The late Problem 4 frames also retain the written Problem 3 header about the Sun; the narration and Moon data identify the calculation as Problem 4.

The absolute formula also requires the orbital semi-major axis measured center to center. If a circular satellite's altitude is supplied, first use $a=R+h$.

```quiz
type: radio
id: mct-p21-mass-variation
shuffle: true
content: |-
  Two bodies orbit their common center of mass with relative-orbit semi-major axis $a=2.00\times10^8\,\mathrm m$ and period $T=10.0\,\mathrm d$. What total mass $M+m$ follows from Kepler's third law?
options:
- id: mct-p21-mass-variation-a
  content: |-
    $6.34\times10^{24}\,\mathrm{kg}$
  correct: true
  feedback: |-
    The absolute law gives $M+m=4\pi^2a^3/(GT^2)$. With $T=10.0(86400)=864000\,\mathrm s$, substitution gives $6.343\ldots\times10^{24}\,\mathrm{kg}$, or $6.34\times10^{24}\,\mathrm{kg}$.
- id: mct-p21-mass-variation-b
  content: |-
    $4.74\times10^{34}\,\mathrm{kg}$
  feedback: |-
    This inserts $T=10.0$ directly while using SI $G$. The period must be $864000\,\mathrm s$ before it is squared; days are not compatible with the units of $G$.
- id: mct-p21-mass-variation-c
  content: |-
    $5.48\times10^{30}\,\mathrm{kg}$
  feedback: |-
    This converts the period to seconds but divides by $T$ rather than $T^2$. Kepler's law contains the square of the complete period, $(864000)^2$.
- id: mct-p21-mass-variation-d
  content: |-
    $1.59\times10^{24}\,\mathrm{kg}$
  feedback: |-
    This drops the factor $4$ from $4\pi^2$. The circular-orbit substitution $v=2\pi a/T$ produces $(2\pi)^2=4\pi^2$.
- id: mct-p21-mass-variation-e
  content: |-
    $6.34\times10^{24}\,\mathrm N$
  feedback: |-
    The number matches, but the requested quantity is mass. The units of $a^3/(GT^2)$ reduce to kilograms, not newtons.
```

---

<a id="summary"></a>
## Summary

- Use semi-major axis $a$; for a circular orbit, $a=r$ measured center to center. Do not substitute altitude directly.
- Pair each period with its own orbit size before forming a ratio.
- For two negligible-mass orbiters around the same central body,
  $$
  \left(\frac{T_2}{T_1}\right)^2
  =\left(\frac{a_2}{a_1}\right)^3.
  $$
- Predict first: the larger orbit has the longer period.
- Solve for period with a $3/2$ power and for semi-major axis with a $2/3$ power.
- Ratios need only matching units. Absolute mass calculations require meters and seconds.
- An orbit determines
  $$
  M+m=\frac{4\pi^2a^3}{GT^2}.
  $$
  Reporting this as $M$ assumes $m\ll M$.
- The simple same-center ratio does not apply to different central masses.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
