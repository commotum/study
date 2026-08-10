# Total Gravitational Potential Energy: Sum Every Pair Once

<!--
lesson-id: 212-M3-031
topic-code: MTH212.M3.31
-->
## Table of Contents

- [Introduction](#introduction)
- [One Pair Gives One Energy Term](#one-pair-gives-one-energy-term)
- [List Every Unique Pair](#list-every-unique-pair)
- [Use the Separation Between the Two Objects](#use-the-separation-between-the-two-objects)
- [Compare Negative Totals](#compare-negative-totals)
- [Summary](#summary)

## Prerequisites

- Use the two-body gravitational potential energy formula $U=-Gm_1m_2/d$.
- Find distances between objects in a simple diagram.
- Compare negative quantities on a number line.

---

<a id="introduction"></a>
## Introduction

When a problem asks for the **total gravitational potential energy** of several bodies, the cue is the word *total*. Every unordered pair of bodies contributes its own potential-energy term, so list each pair once, use the distance between those two bodies, and add the terms. Order does not matter: $AB$ and $BA$ name the same pair, not two interactions.

For bodies labeled $i$ and $j$,

$$
U_{ij}=-\frac{Gm_im_j}{r_{ij}}.
$$

Because gravity is attractive and the usual zero is chosen at infinite separation, every finite pair contributes a negative term.

---

<a id="one-pair-gives-one-energy-term"></a>
## One Pair Gives One Energy Term

**Example:** Two objects have masses $2m$ and $3m$ and are separated by $4r$. Find their gravitational potential energy.

**Explanation**

There is one pair, so there is one term. Substitute both masses and their separation:

$$
U=-\frac{G(2m)(3m)}{4r}
=-\frac{3Gm^2}{2r}.
$$

The minus sign belongs to the gravitational potential energy; it is not determined by the objects' positions on a diagram.

```quiz
type: radio
id: p3-one-pair
content: |-
  Two objects have masses $m$ and $4m$ and are separated by $2r$. What is their gravitational potential energy?
options:
- id: positive-two
  content: |-
    $\dfrac{2Gm^2}{r}$
  feedback: |-
    This has the correct magnitude but loses the gravitational minus sign. A finite attractive pair has $U=-Gm_1m_2/d$, so substituting $m$, $4m$, and $2r$ gives $U=-2Gm^2/r$.
- id: negative-two
  content: |-
    $-\dfrac{2Gm^2}{r}$
  correct: true
  feedback: |-
    One pair contributes $-Gm_1m_2/d$. Here $m_1m_2=4m^2$ and $d=2r$, so $U=-G(4m^2)/(2r)=-2Gm^2/r$.
- id: negative-four
  content: |-
    $-\dfrac{4Gm^2}{r}$
  feedback: |-
    This uses the mass product but omits the factor $2$ in the separation. Since distance divides the mass product, $4m^2/(2r)=2m^2/r$, giving $U=-2Gm^2/r$.
- id: negative-half
  content: |-
    $-\dfrac{Gm^2}{2r}$
  feedback: |-
    This treats both objects as if their masses were $m$. The product is $m(4m)=4m^2$, so the numerator must include the factor $4$ before dividing by $2r$.
- id: negative-eight
  content: |-
    $-\dfrac{8Gm^2}{r}$
  feedback: |-
    This multiplies by the separation instead of dividing by it. The pair formula is inverse in distance: $U=-G(4m^2)/(2r)=-2Gm^2/r$.
```

---

<a id="list-every-unique-pair"></a>
## List Every Unique Pair

**Example:** A star $S$ of mass $M$ and planets $P$ and $Q$ of masses $m$ and $2m$ have separations $SP=a$, $SQ=b$, and $PQ=c$. Write the system's total gravitational potential energy.

**Explanation**

The three unique pairs are $SP$, $SQ$, and $PQ$. A short pair ledger keeps the mass product and separation attached to the correct interaction:

| Pair | Mass product | Separation | Contribution |
|---|---:|---:|---:|
| $SP$ | $Mm$ | $a$ | $-GMm/a$ |
| $SQ$ | $M(2m)$ | $b$ | $-2GMm/b$ |
| $PQ$ | $m(2m)$ | $c$ | $-2Gm^2/c$ |

Now add those three signed terms:

$$
\begin{aligned}
U_{\text{tot}}
&=U_{SP}+U_{SQ}+U_{PQ}\\
&=-\frac{GMm}{a}-\frac{G(M)(2m)}{b}-\frac{G(m)(2m)}{c}\\
&=-\frac{GMm}{a}-\frac{2GMm}{b}-\frac{2Gm^2}{c}.
\end{aligned}
$$

The pair $PQ$ counts even if both planets orbit the star. Also, $SP$ and $PS$ name the same interaction, so that pair is counted only once.

```quiz
type: radio
id: p3-unique-pairs
content: |-
  A star $S$ has mass $M$, and two planets $P$ and $Q$ each have mass $m$. Their separations are $SP=r$, $SQ=2r$, and $PQ=3r$. Which expression is the total gravitational potential energy?
options:
- id: star-pairs-only
  content: |-
    $-\dfrac{GMm}{r}-\dfrac{GMm}{2r}$
  feedback: |-
    This includes both star–planet pairs but omits the planet–planet interaction. Total energy includes the unique pair $PQ$ as well, adding $-Gm^2/(3r)$.
- id: all-three-pairs
  content: |-
    $-\dfrac{GMm}{r}-\dfrac{GMm}{2r}-\dfrac{Gm^2}{3r}$
  correct: true
  feedback: |-
    Total energy is the sum over the three unique pairs. Using $SP=r$, $SQ=2r$, and $PQ=3r$ gives exactly these two star–planet terms and one planet–planet term.
- id: doubled-planet-mass
  content: |-
    $-\dfrac{GMm}{r}-\dfrac{GMm}{2r}-\dfrac{2Gm^2}{3r}$
  feedback: |-
    The planet–planet numerator is the product of the two planet masses, $m\cdot m=m^2$, not their sum $2m$. Its contribution is therefore $-Gm^2/(3r)$.
- id: swapped-distances
  content: |-
    $-\dfrac{GMm}{r}-\dfrac{GMm}{3r}-\dfrac{Gm^2}{2r}$
  feedback: |-
    Each denominator must be the separation of the pair in that term. The $SQ$ pair uses $2r$, while the $PQ$ pair uses $3r$; swapping them changes both interactions.
- id: positive-total
  content: |-
    $\dfrac{GMm}{r}+\dfrac{GMm}{2r}+\dfrac{Gm^2}{3r}$
  feedback: |-
    This lists all three pairs but makes every contribution positive. With zero potential at infinity, each finite gravitational pair contributes $-Gm_im_j/r_{ij}$, so all three terms are negative.
```

---

<a id="use-the-separation-between-the-two-objects"></a>
## Use the Separation Between the Two Objects

**Example:** A star of mass $M$ is at the origin. A planet of mass $m$ is at $x=R$, and a planet of mass $2m$ is at $x=-2R$. Find the total gravitational potential energy.

**Explanation**

The star–planet separations are $R$ and $2R$. Because the planets are on opposite sides of the origin, their separation is

$$
R+2R=3R.
$$

Thus,

$$
\begin{aligned}
U_{\text{tot}}
&=-\frac{GMm}{R}-\frac{G(M)(2m)}{2R}-\frac{G(m)(2m)}{3R}\\
&=-\frac{2GMm}{R}-\frac{2Gm^2}{3R}.
\end{aligned}
$$

An orbital radius is a star–planet distance. It is not automatically the distance between two planets.

```quiz
type: radio
id: p3-opposite-sides
content: |-
  Two planets of mass $m$ are on opposite sides of a star of mass $M$. Each planet is a distance $r$ from the star. Which expression is the total gravitational potential energy of the three-body system?
options:
- id: correct-opposite-total
  content: |-
    $-\dfrac{2GMm}{r}-\dfrac{Gm^2}{2r}$
  correct: true
  feedback: |-
    There are two star–planet pairs at separation $r$ and one planet–planet pair at separation $2r$. Summing their negative contributions gives $U_{\text{tot}}=-2GMm/r-Gm^2/(2r)$.
- id: planet-distance-r
  content: |-
    $-\dfrac{2GMm}{r}-\dfrac{Gm^2}{r}$
  feedback: |-
    This uses the orbital radius $r$ for the planet–planet pair. Opposite planets are $r+r=2r$ apart, so that pair contributes $-Gm^2/(2r)$.
- id: one-star-pair
  content: |-
    $-\dfrac{GMm}{r}-\dfrac{Gm^2}{2r}$
  feedback: |-
    This includes the planet–planet pair but only one of the two star–planet pairs. Each planet interacts with the star, so the star contribution is $-2GMm/r$.
- id: no-planet-pair
  content: |-
    $-\dfrac{2GMm}{r}$
  feedback: |-
    This counts both star–planet interactions but treats the planets as if they did not interact. The planet–planet pair is separated by $2r$ and adds $-Gm^2/(2r)$.
- id: positive-planet-pair
  content: |-
    $-\dfrac{2GMm}{r}+\dfrac{Gm^2}{2r}$
  feedback: |-
    Being on opposite sides changes the separation, not the sign of gravitational potential energy. The planet–planet interaction is attractive and contributes $-Gm^2/(2r)$.
```

---

<a id="compare-negative-totals"></a>
## Compare Negative Totals

**Example:** Suppose one system has $U_A=-K$ and another has $U_B=-2K-L$, where $K>0$ and $L>0$. Compare the energies.

**Explanation**

System $B$ contains the negative amount $-K$ plus the additional negative amount $-(K+L)$, so it lies farther left on the number line. To check the inequality without relying only on intuition, subtract in the order being compared:

$$
U_A-U_B=(-K)-(-2K-L)=K+L>0.
$$

Therefore, $U_A>U_B$. A total with greater magnitude can be **more negative** and therefore numerically smaller.

```quiz
type: radio
id: p3-source-comparison
shuffle: true
content: |-
  In System I, one planet of mass $m$ orbits a star of mass $M$ at radius $r$. System II has two planets of mass $m$ orbiting the same star at the same radius, on opposite sides as shown. What can be said about the total gravitational potential energy of the two systems?

  ![](<../Source/2026-07-20-Q-2/Images/problem-3-one-vs-two-planet-systems.png>)
options:
- id: system-i-less
  content: |-
    $U_{\mathrm I}<U_{\mathrm{II}}$
  feedback: |-
    This reverses the order of negative values. System II has two star–planet terms and one planet–planet term, so $U_{\mathrm I}-U_{\mathrm{II}}=GMm/r+Gm^2/(2r)>0$; therefore $U_{\mathrm I}>U_{\mathrm{II}}$.
- id: systems-equal
  content: |-
    $U_{\mathrm I}=U_{\mathrm{II}}$
  feedback: |-
    Equal orbital radii make each star–planet term equal, but System II has two such terms and an additional planet–planet term. Those extra negative contributions make $U_{\mathrm{II}}$ smaller, not equal to $U_{\mathrm I}$.
- id: system-i-greater
  content: |-
    $U_{\mathrm I}>U_{\mathrm{II}}$
  correct: true
  feedback: |-
    Sum each unique pair once: $U_{\mathrm I}=-GMm/r$, while $U_{\mathrm{II}}=-2GMm/r-Gm^2/(2r)$. The extra negative contributions put System II farther left on the number line, so $U_{\mathrm I}>U_{\mathrm{II}}$.
```

---

<a id="summary"></a>
## Summary

When a system contains several gravitating bodies:

1. List every unordered pair once; reversing the labels does not create a new pair.
2. For each pair, use $U_{ij}=-Gm_im_j/r_{ij}$.
3. Use that pair's actual separation, not a convenient radius from another pair.
4. Add all pair contributions.
5. Compare the signed totals on the number line, or subtract them: if $U_A-U_B>0$, then $U_A>U_B$.

The main trap is counting only the star–planet interactions. Planets also interact with one another, and each missing pair means a missing negative term.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
