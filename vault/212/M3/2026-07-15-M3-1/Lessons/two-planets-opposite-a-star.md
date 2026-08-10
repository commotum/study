# Two Planets Orbiting Opposite Sides of a Star

<!--
lesson-id: 212-M3-035
topic-code: MTH212.M3.35
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Pair Separations](#read-the-pair-separations)
- [Add the Inward Forces on One Planet](#add-the-inward-forces-on-one-planet)
- [Convert the Radial Force Into the Period](#convert-the-radial-force-into-the-period)
- [Count Each Potential-Energy Pair Once](#count-each-potential-energy-pair-once)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Use Newton's gravitational force magnitude $F=Gm_1m_2/d^2$.
- Use gravitational pair potential energy $U=-Gm_1m_2/d$.
- Apply the radial equation $F_r=mv^2/r$ for uniform circular motion.
- Relate orbital speed and period with $v=2\pi r/T$.
- Add collinear force contributions and count distinct object pairs.

---

<a id="introduction"></a>
## Introduction

Two planets of mass $m$ remain on opposite sides of a star of mass $M$, each at orbital radius $r$. The problem asks for their period and the system's total gravitational potential energy.

![](<../Source/Images/binaryplanets.jpg>)

The cue **opposite sides** determines the geometry. Each star–planet distance is $r$, but the two planets are separated by the full diameter $2r$. For either planet, both gravitational forces point inward along the same line: the star attracts it toward the center, and the other planet attracts it through the center. The two equal planets pull on the star with equal and opposite forces, so the star remains at the center of this symmetric configuration.

Use the separations in two different ledgers:

- For the period, add the inward forces acting on one planet and apply circular motion.
- For total potential energy, sum the energy of each distinct pair exactly once.

---

<a id="read-the-pair-separations"></a>
## Read the Pair Separations

**Example:** List the three interacting pairs and their separations.

**Explanation**

Call the planets $P_1$ and $P_2$. The pair ledger is

| Pair | Separation |
|---|---:|
| star–$P_1$ | $r$ |
| star–$P_2$ | $r$ |
| $P_1$–$P_2$ | $2r$ |

The factor of two must be placed inside the force law's square:

$$
(2r)^2=4r^2.
$$

Potential energy uses the first power of separation, so the same planet–planet distance appears there as $2r$, not $4r^2$.

```quiz
type: radio
id: opposite-planets-separation-ledger
shuffle: true
content: |-
  Two planets lie on opposite sides of a star, each at orbital radius $R$. Which separations belong in the gravitational formulas?
options:
- id: star-r-planets-two-r
  content: |-
    Each star–planet separation is $R$, and the planet–planet separation is $2R$.
  correct: true
  feedback: |-
    Each planet is one radius from the central star. The planets occupy opposite ends of a diameter, so their separation is $R+R=2R$.
- id: all-r
  content: |-
    Every separation is $R$.
  feedback: |-
    The orbital radius describes one planet's distance to the star, not the distance across the entire orbit. Opposite planets are separated by the diameter $2R$.
- id: star-two-r-planets-r
  content: |-
    Each star–planet separation is $2R$, and the planet–planet separation is $R$.
  feedback: |-
    This reverses radius and diameter. The star is at the center, so it is $R$ from either planet, while the two planets are $2R$ apart.
- id: all-two-r
  content: |-
    Every separation is $2R$.
  feedback: |-
    Only the distance from one planet across the center to the other spans the diameter $2R$. A star–planet segment is one radius $R$.
- id: planet-four-r
  content: |-
    Each star–planet separation is $R$, and the planet–planet separation is $4R$.
  feedback: |-
    The factor four appears only after squaring the planet separation in the force denominator: $(2R)^2=4R^2$. The geometric separation itself remains $2R$.
```

---

<a id="add-the-inward-forces-on-one-planet"></a>
## Add the Inward Forces on One Planet

**Example:** Find the net inward gravitational force on either planet.

**Explanation**

The star's attraction on one planet has magnitude

$$
F_{\star}=\frac{GMm}{r^2}.
$$

The other planet is $2r$ away, so its attraction has magnitude

$$
F_{p}=\frac{Gm^2}{(2r)^2}
=\frac{Gm^2}{4r^2}.
$$

Both forces point toward the center for the chosen planet, so their magnitudes add:

$$
F_{\mathrm{in}}
=\frac{GMm}{r^2}+\frac{Gm^2}{4r^2}
=\frac{Gm}{r^2}\left(M+\frac{m}{4}\right).
$$

Do not double this expression. It is already the complete net force on one planet, which is the object used in the radial equation.

```quiz
type: radio
id: opposite-planets-net-inward-force
shuffle: true
content: |-
  What is the net inward force magnitude on one planet in the original geometry?
options:
- id: star-plus-quarter-planet
  content: |-
    $\dfrac{GMm}{r^2}+\dfrac{Gm^2}{4r^2}$
  correct: true
  feedback: |-
    Both attractions point inward. The star is distance $r$ away, while the other planet is distance $2r$, so its inverse-square term is $Gm^2/(2r)^2=Gm^2/(4r^2)$.
- id: use-r-for-planet
  content: |-
    $\dfrac{GMm}{r^2}+\dfrac{Gm^2}{r^2}$
  feedback: |-
    This treats the other planet as one orbital radius away. It lies across the star at distance $2r$, reducing its force contribution by a factor of four.
- id: denominator-two
  content: |-
    $\dfrac{GMm}{r^2}+\dfrac{Gm^2}{2r^2}$
  feedback: |-
    The inverse-square law requires squaring the full separation: $(2r)^2=4r^2$. Using only a factor of two overstates the companion planet's force.
- id: subtract-planet-force
  content: |-
    $\dfrac{GMm}{r^2}-\dfrac{Gm^2}{4r^2}$
  feedback: |-
    Gravity is attractive, and the other planet lies through the center from the chosen planet. Its pull is therefore inward in the same direction as the star's pull, so the contributions add.
- id: double-star-force
  content: |-
    $\dfrac{2GMm}{r^2}+\dfrac{Gm^2}{4r^2}$
  feedback: |-
    There are two star–planet interactions in the whole system, but only one star force acts on the single planet whose radial equation is being written. Doubling it mixes a system count with a one-object force balance.
```

---

<a id="convert-the-radial-force-into-the-period"></a>
## Convert the Radial Force Into the Period

**Example:** Use the net inward force to find the planets' common orbital period.

**Explanation**

Apply the radial force equation to either planet:

$$
m\frac{v^2}{r}
=\frac{Gm}{r^2}\left(M+\frac{m}{4}\right).
$$

Cancel $m$ and solve for $v^2$:

$$
v^2=\frac{G}{r}\left(M+\frac{m}{4}\right).
$$

Now use $v=2\pi r/T$:

$$
\begin{aligned}
\frac{4\pi^2r^2}{T^2}
&=\frac{G}{r}\left(M+\frac{m}{4}\right),\\
T^2
&=\frac{4\pi^2r^3}{G\left(M+m/4\right)}.
\end{aligned}
$$

The positive period is

$$
\boxed{T=2\pi\sqrt{\frac{r^3}{G\left(M+m/4\right)}}}.
$$

Only the positive square root is kept because a period is a positive duration. The dimensions also check:

$$
\left[\frac{r^3}{G(M+m/4)}\right]
=\mathrm{s}^2,
\qquad
[T]=\mathrm{s}.
$$

When $m\ll M$, the companion's contribution becomes negligible and this reduces to the usual small-satellite result $T\approx2\pi\sqrt{r^3/(GM)}$.

```quiz
type: radio
id: opposite-planets-period-variant
shuffle: true
content: |-
  Two planets of mass $q$ remain opposite each other around a star of mass $S$, each at radius $R$. Which expression gives their period?
options:
- id: effective-mass-quarter
  content: |-
    $2\pi\sqrt{\dfrac{R^3}{G(S+q/4)}}$
  correct: true
  feedback: |-
    The companion is $2R$ away, so its force contributes as though $q/4$ were added to the central mass term. Circular motion then gives $T=2\pi\sqrt{R^3/[G(S+q/4)]}$.
- id: effective-mass-full
  content: |-
    $2\pi\sqrt{\dfrac{R^3}{G(S+q)}}$
  feedback: |-
    This treats the companion planet as though it were distance $R$ away. Its actual separation is $2R$, so the inverse-square force contributes $q/4$, not the full $q$.
- id: effective-mass-half
  content: |-
    $2\pi\sqrt{\dfrac{R^3}{G(S+q/2)}}$
  feedback: |-
    This applies the factor of two from the separation only once. Force depends on distance squared, so the companion contribution is reduced by $2^2=4$ and appears as $q/4$.
- id: subtract-quarter
  content: |-
    $2\pi\sqrt{\dfrac{R^3}{G(S-q/4)}}$
  feedback: |-
    The companion planet attracts the chosen planet toward the center, adding to the star's inward pull. A subtraction would apply only if its force pointed outward, which it does not in the opposite-side geometry.
- id: double-star
  content: |-
    $2\pi\sqrt{\dfrac{R^3}{G(2S+q/4)}}$
  feedback: |-
    The radial equation is for one planet and contains the force from the one star only once. The second star–planet pair belongs to the other planet's force balance, not this one.
```

---

<a id="count-each-potential-energy-pair-once"></a>
## Count Each Potential-Energy Pair Once

**Example:** Find the system's total gravitational potential energy.

**Explanation**

Potential energy belongs to an interacting pair, not to one object's free-body diagram. There are exactly three distinct pairs:

$$
\begin{aligned}
U_{\star 1}&=-\frac{GMm}{r},\\
U_{\star 2}&=-\frac{GMm}{r},\\
U_{12}&=-\frac{Gm^2}{2r}.
\end{aligned}
$$

Add each pair once:

$$
\boxed{U
=-\frac{2GMm}{r}-\frac{Gm^2}{2r}}.
$$

The planet–planet term uses $2r$ to the first power because gravitational potential energy varies as $1/d$. Counting $U_{12}$ twice would duplicate the same interaction, even though each planet feels a force from the other. Each term has units $[Gm_am_b/d]=\mathrm{kg\,m^2/s^2}=\mathrm J$, and every term is negative because every pair is gravitationally bound relative to zero energy at infinite separation.

```quiz
type: radio
id: opposite-planets-total-potential
shuffle: true
content: |-
  A star of mass $S$ has two planets of mass $q$ on opposite sides, each at radius $R$. What is the system's total gravitational potential energy?
options:
- id: two-star-one-planet-pair
  content: |-
    $-\dfrac{2GSq}{R}-\dfrac{Gq^2}{2R}$
  correct: true
  feedback: |-
    There are two star–planet pairs at separation $R$ and one planet–planet pair at separation $2R$. Summing each once gives $-2GSq/R-Gq^2/(2R)$.
- id: use-r-in-planet-energy
  content: |-
    $-\dfrac{2GSq}{R}-\dfrac{Gq^2}{R}$
  feedback: |-
    The two star–planet terms are counted correctly, but the planets are separated by $2R$, not $R$. Potential energy uses the first power of that distance, giving $-Gq^2/(2R)$.
- id: one-star-pair
  content: |-
    $-\dfrac{GSq}{R}-\dfrac{Gq^2}{2R}$
  feedback: |-
    This omits one of the two distinct star–planet interactions. Each planet forms its own pair with the star, so the star–planet contribution is $-2GSq/R$.
- id: double-planet-pair
  content: |-
    $-\dfrac{2GSq}{R}-\dfrac{2Gq^2}{2R}$
  feedback: |-
    The planet–planet interaction is one unordered pair, not one energy term per planet. Counting it twice duplicates the same shared potential energy.
- id: positive-planet-pair
  content: |-
    $-\dfrac{2GSq}{R}+\dfrac{Gq^2}{2R}$
  feedback: |-
    Gravitational potential energy is negative for every attractive pair when zero is chosen at infinite separation. The planet–planet term must therefore also be negative.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the original two-output problem before checking the choices.

**Explanation**

> Two planets of mass $m$ remain on opposite sides of a star of mass $M$, each at orbital radius $r$. Find their period and the system's total gravitational potential energy.
>
> ![](<../Source/Images/binaryplanets.jpg>)

Keep both answers symbolic. For the period, analyze the inward force on one planet. For potential energy, switch to the three-pair ledger and count each interaction once.

```quiz
type: radio
id: khadley-gravity-q5
shuffle: true
content: |-
  Which ordered pair gives (orbital period, total gravitational potential energy) for the original system?
options:
- id: correct-period-and-energy
  content: |-
    $\left(2\pi\sqrt{\dfrac{r^3}{G(M+m/4)}},\ -\dfrac{2GMm}{r}-\dfrac{Gm^2}{2r}\right)$
  correct: true
  feedback: |-
    The companion planet is $2r$ away, so its inward force contributes the effective term $m/4$ in the period. The energy ledger has two star–planet pairs and one planet–planet pair, giving the stated total.
- id: ignore-companion-force
  content: |-
    $\left(2\pi\sqrt{\dfrac{r^3}{GM}},\ -\dfrac{2GMm}{r}-\dfrac{Gm^2}{2r}\right)$
  feedback: |-
    The potential energy is complete, but the period ignores the other planet's inward attraction. That attraction adds $Gm^2/(4r^2)$ to the radial force, producing $M+m/4$ in the period denominator.
- id: unsquared-separation-period
  content: |-
    $\left(2\pi\sqrt{\dfrac{r^3}{G(M+m/2)}},\ -\dfrac{2GMm}{r}-\dfrac{Gm^2}{2r}\right)$
  feedback: |-
    The energy uses the correct first-power separation $2r$, but force uses the inverse square. Squaring $2r$ makes the companion's period contribution $m/4$, not $m/2$.
- id: double-planet-energy
  content: |-
    $\left(2\pi\sqrt{\dfrac{r^3}{G(M+m/4)}},\ -\dfrac{2GMm}{r}-\dfrac{Gm^2}{r}\right)$
  feedback: |-
    The period is correct, but this counts the single planet–planet energy twice. There is one planet pair at separation $2r$, so its one shared term is $-Gm^2/(2r)$.
- id: omit-star-pair
  content: |-
    $\left(2\pi\sqrt{\dfrac{r^3}{G(M+m/4)}},\ -\dfrac{GMm}{r}-\dfrac{Gm^2}{2r}\right)$
  feedback: |-
    The period is correct, but the total energy must include both distinct star–planet pairs. Their combined contribution is $-2GMm/r$, not $-GMm/r$.
```

---

<a id="summary"></a>
## Summary

For two equal planets on opposite sides of a central star:

1. Record the separations: $r$, $r$, and $2r$.
2. For one planet, both attractions point inward:
   $$
   F_{\mathrm{in}}
   =\frac{GMm}{r^2}+\frac{Gm^2}{4r^2}.
   $$
3. Set this equal to $mv^2/r$ and use $v=2\pi r/T$:
   $$
   \boxed{T=2\pi\sqrt{\frac{r^3}{G(M+m/4)}}}.
   $$
4. For potential energy, count the two star–planet pairs and one planet pair once:
   $$
   \boxed{U=-\frac{2GMm}{r}-\frac{Gm^2}{2r}}.
   $$

The main traps are using $r$ instead of $2r$ between the planets, forgetting to square $2r$ in the force law, subtracting an inward companion force, doubling a one-planet force balance, or counting the planet–planet potential energy twice.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
