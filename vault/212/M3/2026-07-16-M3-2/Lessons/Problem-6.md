# Total Mechanical Energy of a Three-Body Orbit

<!--
lesson-id: 212-M3-010
topic-code: MTH212.M3.10
-->

## Table of Contents

- [Introduction](#introduction)
- [Count Bodies and Interaction Pairs](#count-bodies-and-interaction-pairs)
- [Build the Total Kinetic and Potential Energies](#build-the-total-kinetic-and-potential-energies)
- [Use the Orbit Relation Before Adding](#use-the-orbit-relation-before-adding)
- [Evaluate and Convert to the Requested Energy Scale](#evaluate-and-convert-to-the-requested-energy-scale)
- [Summary](#summary)

## Prerequisites

- Kinetic energy: $K=\frac12mv^2$
- Gravitational potential energy of one pair: $U_{\mathrm{pair}}=-Gm_1m_2/r$
- Adding signed fractions
- Scientific notation and significant figures

---

## Introduction

The total mechanical energy of a many-body system is

$$
E=K_{\mathrm{total}}+U_{\mathrm{total}}.
$$

For three equal masses in an equilateral-triangle orbit, the key is to count two different things correctly:

- kinetic energy has one contribution from each moving mass;
- gravitational potential energy has one contribution from each distinct pair.

**Recognition cue:** When a problem asks for the energy of the whole system, total every object's kinetic energy and every unordered pair's gravitational potential energy before adding them.

---

## Count Bodies and Interaction Pairs

**Example:** Three masses are labeled $A$, $B$, and $C$. How many terms contribute to each total?

**Explanation**

There are three moving bodies, so there are three kinetic-energy terms.

The distinct gravitational pairs are

$$
AB,\qquad AC,\qquad BC.
$$

Thus there are also three potential-energy terms. A pair such as $AB$ is the same interaction as $BA$, so it must not be counted twice.

In general, $n$ objects have

$$
N_{\mathrm{pairs}}=\binom{n}{2}=\frac{n(n-1)}{2}
$$

distinct pairs. For $n=3$, this gives $\binom{3}{2}=3$.

| Quantity being totaled | What receives one term? | Number of terms |
|---|---|---:|
| Kinetic energy | Each moving body | $3$ |
| Potential energy | Each unordered pair | $3$ |

```quiz
type: radio
id: problem-6-count-pairs-q1
content: |-
  Four objects all interact with one another. How many distinct pair-potential terms belong in the system's total potential energy?
options:
- id: a
  content: |-
    $6$
  correct: true
  feedback: |-
    $\binom{4}{2}=4(3)/2=6$ distinct unordered pairs.
- id: b
  content: |-
    $4$
  feedback: |-
    This counts one term per object, but potential energy is counted once per pair.
- id: c
  content: |-
    $8$
  feedback: |-
    This does not count all distinct pairs exactly once.
- id: d
  content: |-
    $12$
  feedback: |-
    This counts ordered pairs, treating $AB$ and $BA$ as different even though they are the same interaction.
- id: e
  content: |-
    $16$
  feedback: |-
    This includes self-pairs and ordered duplicates.
```

---

## Build the Total Kinetic and Potential Energies

**Example:** Three equal masses $m$ all move at speed $v$ at the corners of an equilateral triangle of side length $L$. Write $K_{\mathrm{total}}$ and $U_{\mathrm{total}}$.

**Explanation**

Each mass contributes $\frac12mv^2$, so

$$
K_{\mathrm{total}}
=3\left(\frac12mv^2\right)
=\frac32mv^2.
$$

Each of the three pairs is separated by $L$ and contributes $-Gm^2/L$, so

$$
U_{\mathrm{total}}
=3\left(-\frac{Gm^2}{L}\right)
=-3\frac{Gm^2}{L}.
$$

The negative sign is part of gravitational potential energy. The factor $3$ in $K$ counts bodies, while the factor $3$ in $U$ counts pairs.

A contribution ledger keeps the two totals separate:

| Energy | One contribution | Count | System total |
|---|---:|---:|---:|
| Kinetic | $\frac12mv^2$ | $3$ bodies | $\frac32mv^2$ |
| Potential | $-Gm^2/L$ | $3$ pairs | $-3Gm^2/L$ |

```quiz
type: radio
id: problem-6-build-totals-q1
content: |-
  Three equal masses $m$ move at the same speed $v$ at the corners of an equilateral triangle of side length $L$. Which expressions give the system totals?
options:
- id: a
  content: |-
    $K=\dfrac32mv^2$ and $U=-3\dfrac{Gm^2}{L}$
  correct: true
  feedback: |-
    There are three moving bodies and three distinct gravitational pairs.
- id: b
  content: |-
    $K=\dfrac12mv^2$ and $U=-3\dfrac{Gm^2}{L}$
  feedback: |-
    This includes the kinetic energy of only one of the three masses.
- id: c
  content: |-
    $K=\dfrac32mv^2$ and $U=-\dfrac{Gm^2}{L}$
  feedback: |-
    This includes the potential energy of only one of the three pairs.
- id: d
  content: |-
    $K=3mv^2$ and $U=-3\dfrac{Gm^2}{L}$
  feedback: |-
    This drops the factor $\frac12$ from each kinetic-energy term.
- id: e
  content: |-
    $K=\dfrac32mv^2$ and $U=3\dfrac{Gm^2}{L}$
  feedback: |-
    Gravitational potential energy is negative when zero potential is defined at infinite separation.
```

---

## Use the Orbit Relation Before Adding

**Example:** For this equilateral-triangle orbit, the force analysis gives

$$
v^2=\frac{Gm}{L}.
$$

Use this relation to simplify the total mechanical energy symbolically.

**Explanation**

Substitute the relation into the total kinetic energy:

$$
K_{\mathrm{total}}
=\frac32m\left(\frac{Gm}{L}\right)
=\frac32\frac{Gm^2}{L}.
$$

Now $K$ and $U$ share the same scale. Let

$$
Q=\frac{Gm^2}{L},
\qquad Q>0.
$$

Then

$$
E=K+U
=\frac32Q-3Q
=-\frac32Q
=-\frac32\frac{Gm^2}{L}.
$$

Before doing arithmetic, compare magnitudes: $|U|=3Q$ is larger than $K=\frac32Q$, so $E$ must be negative. The result confirms that prediction and is physically sensible for a gravitationally bound orbit. Here, $U=-2K$, so $E=-K$.

```quiz
type: radio
id: problem-6-combine-energy-q1
content: |-
  Suppose $Q=Gm^2/L>0$, $K=\frac32Q$, and $U=-3Q$. What is the total mechanical energy?
options:
- id: a
  content: |-
    $-\dfrac32Q$
  correct: true
  feedback: |-
    $E=K+U=\frac32Q-3Q=-\frac32Q$.
- id: b
  content: |-
    $\dfrac92Q$
  feedback: |-
    This adds the magnitudes and loses the negative sign of $U$.
- id: c
  content: |-
    $-\dfrac92Q$
  feedback: |-
    This subtracts the positive kinetic energy instead of adding it to $U$.
- id: d
  content: |-
    $\dfrac32Q$
  feedback: |-
    This has the magnitude of the correct answer but not its sign.
- id: e
  content: |-
    $0$
  feedback: |-
    The positive kinetic energy cancels only half of the potential-energy magnitude.
```

---

## Evaluate and Convert to the Requested Energy Scale

**Example:** Evaluate the energy for

$$
m=2.5\times10^{30}\ \mathrm{kg},
\qquad
L=1.8\times10^{12}\ \mathrm{m},
$$

using $G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$.

**Explanation**

Substitute into the simplified expression:

$$
\begin{aligned}
E
&=-\frac32\frac{Gm^2}{L}\\
&=-\frac32
\frac{(6.67\times10^{-11})(2.5\times10^{30})^2}
{1.8\times10^{12}}\\
&=-3.4740\times10^{38}\ \mathrm{J}.
\end{aligned}
$$

To express this in units of $10^{36}\ \mathrm{J}$, divide by $10^{36}\ \mathrm{J}$:

$$
\frac{-3.4740\times10^{38}\ \mathrm{J}}
{10^{36}\ \mathrm{J}}
=-347.40\ldots.
$$

Equivalently, the powers of ten show the two-place shift directly:

$$
\frac{-3.4740\times10^{38}}{10^{36}}
=-3.4740\times10^{38-36}
=-3.4740\times10^2.
$$

The measured givens have two significant figures, so the number-only entry is

$$
\boxed{-350}.
$$

```quiz
type: radio
id: m3-2lec-q5
content: |-
  **Question 5**

  For the same three equal masses in an equilateral-triangle orbit, find the total mechanical energy of the system for $m=2.5\times10^{30}\ \mathrm{kg}$ and $L=1.8\times10^{12}\ \mathrm{m}$.

  Enter the energy in units of $10^{36}\ \mathrm{J}$ as a number only:
options:
- id: a
  content: |-
    $-350$
  correct: true
  feedback: |-
    The three mass pairs give total gravitational potential energy

    $$
    U=-3\frac{Gm^2}{L}.
    $$

    Since $v^2=Gm/L$, the total kinetic energy is

    $$
    K=3\left(\frac12mv^2\right)
    =\frac32\frac{Gm^2}{L}.
    $$

    Therefore,

    $$
    E=K+U
    =-\frac32\frac{Gm^2}{L}
    =-3.4740\times10^{38}\ \mathrm{J}
    =-347.40\ldots\times10^{36}\ \mathrm{J}.
    $$

    The measured givens have two significant figures, so $E=-3.5\times10^{38}\ \mathrm{J}$, or $-3.5\times10^2$ in units of $10^{36}\ \mathrm{J}$, entered as `-350`.
- id: b
  content: |-
    $350$
  feedback: |-
    This has the correct magnitude but loses the negative sign of the bound system's total energy.
- id: c
  content: |-
    $-3.5$
  feedback: |-
    This does not convert from $10^{38}\ \mathrm{J}$ to the requested units of $10^{36}\ \mathrm{J}$.
- id: d
  content: |-
    $-35$
  feedback: |-
    This shifts the power-of-ten scale by only one factor of $10$ instead of two.
- id: e
  content: |-
    $-3500$
  feedback: |-
    This shifts the power-of-ten scale by three factors of $10$ instead of two.
```

---

## Summary

When finding the total mechanical energy of identical orbiting bodies:

1. Count one kinetic term for each moving body.
2. Count each unordered gravitational pair exactly once.
3. Write $K_{\mathrm{total}}$ and $U_{\mathrm{total}}$ separately.
4. Substitute any orbit relation before entering numbers.
5. Add the signed energies: $E=K+U$.
6. Convert to the requested power-of-ten unit, then round using the measured givens.

For three equal masses in an equilateral-triangle orbit with $v^2=Gm/L$,

$$
\boxed{E=-\frac32\frac{Gm^2}{L}}.
$$

The main traps are double-counting pairs, omitting one of the three kinetic terms, dropping the negative sign of $U$, or mishandling the requested $10^{36}\ \mathrm{J}$ scale.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Four Stars Orbiting at the Corners of a Square](../../2026-07-19-PQ-2/Lessons/Problem-5.md)

Study guide index: 19/20

---

<!-- lesson-nav:end -->
