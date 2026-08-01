# Finding Orbital Distance From Orbital Period

## Table of Contents

- [Introduction](#introduction)
- [Use the Normalized Form of Kepler's Third Law](#use-the-normalized-form-of-keplers-third-law)
- [Solve the Cubic Relationship for Distance](#solve-the-cubic-relationship-for-distance)
- [Evaluate the Fractional Power Correctly](#evaluate-the-fractional-power-correctly)
- [Check Scale, Units, and Precision](#check-scale-units-and-precision)
- [Apply the Procedure to the Hypothetical Planet](#apply-the-procedure-to-the-hypothetical-planet)
- [Summary](#summary)

## Prerequisites

- Solve $x^3=b$ by taking the cube root of both sides.
- Rewrite $\sqrt[3]{x^2}$ as $x^{2/3}$ for positive $x$.
- Evaluate fractional exponents with a scientific calculator.
- Round a result using significant figures.

---

<a id="introduction"></a>
## Introduction

For an object orbiting the Sun, Kepler's third law can be written in a normalized form:

$$
T^2=a^3,
$$

provided that

- $T$ is measured in **Earth years**, and
- $a$ is measured in **astronomical units**, or AU.

When the period is given and the distance is requested, isolate $a$:

$$
a=\sqrt[3]{T^2}=T^{2/3}.
$$

The recognition cue is an orbit around the Sun with period in Earth years and requested distance in AU. The task is not to square the period and stop; the cube root is required to undo $a^3$.

The normalized equation has a strict input/output contract:

| Numerical input | Formula | Numerical output |
|---|---|---|
| $T$ in Earth years | $a=T^{2/3}$ | $a$ in AU |
| $a$ in AU | $T=a^{3/2}$ | $T$ in Earth years |

Choose the row that matches the given quantity and the requested quantity.

---

<a id="use-the-normalized-form-of-keplers-third-law"></a>
## Use the Normalized Form of Kepler's Third Law

**Example:** Which form of Kepler's third law should be used when a planet's period is stated in Earth years and its orbital distance is requested in AU?

**Explanation**

Use

$$
T^2=a^3.
$$

This compact form is a ratio to Earth's orbit. Earth itself has

$$
T=1\ \text{Earth year}
\qquad\text{and}\qquad
a=1\ \mathrm{AU},
$$

so $1^2=1^3$.

The normalized formula should not be used with seconds and meters. Those units require the gravitational-constant form of the orbital law.

```quiz
type: radio
id: problem-1-form-q1
content: |-
  A planet orbiting the Sun has period $T$ in Earth years. Its orbital distance $a$ is requested in AU. Which relation is appropriate?
options:
- id: a
  content: |-
    $T^2=a^3$
  correct: true
  feedback: |-
    Earth-year and AU units make the solar-orbit relation take this normalized form.
- id: b
  content: |-
    $T=a$
  feedback: |-
    Period and orbital distance are not directly proportional.
- id: c
  content: |-
    $T^3=a^2$
  feedback: |-
    This reverses the exponents in Kepler's third law.
```

---

<a id="solve-the-cubic-relationship-for-distance"></a>
## Solve the Cubic Relationship for Distance

**Example:** A planet has an orbital period of $8$ Earth years. Solve for its distance without a calculator.

**Explanation**

Start with

$$
T^2=a^3.
$$

Substitute $T=8$:

$$
8^2=a^3,
$$

so

$$
64=a^3.
$$

Take the cube root of both sides:

$$
a=\sqrt[3]{64}=4\ \mathrm{AU}.
$$

Equivalently,

$$
a=8^{2/3}=4\ \mathrm{AU}.
$$

The denominator $3$ in the exponent means “take a cube root,” while the numerator $2$ means “square.”

| Part of $T^{2/3}$ | Operation |
|---|---|
| Numerator $2$ | Raise $T$ to the second power |
| Denominator $3$ | Take the cube root |

```quiz
type: radio
id: problem-1-isolate-q1
content: |-
  A planet takes $27$ Earth years to orbit the Sun. According to $a=T^{2/3}$, what is its orbital distance?
options:
- id: a
  content: |-
    $9\ \mathrm{AU}$
  correct: true
  feedback: |-
    $27^{2/3}=(\sqrt[3]{27})^2=3^2=9$.
- id: b
  content: |-
    $3\ \mathrm{AU}$
  feedback: |-
    This takes the cube root but omits the square.
- id: c
  content: |-
    $729\ \mathrm{AU}$
  feedback: |-
    This squares the period but does not take the cube root.
```

---

<a id="evaluate-the-fractional-power-correctly"></a>
## Evaluate the Fractional Power Correctly

**Example:** Evaluate the orbital distance for $T=2.0$ Earth years.

**Explanation**

Use the exponent as a single grouped quantity:

$$
a=(2.0)^{2/3}.
$$

A calculator gives

$$
a=1.5874\ldots\ \mathrm{AU}.
$$

Since the period has two significant figures,

$$
a=1.6\ \mathrm{AU}.
$$

Useful equivalent entries are

$$
T^{2/3},
\qquad
(T^2)^{1/3},
\qquad
\sqrt[3]{T^2}.
$$

On a calculator, enter the exponent with parentheses: `T^(2/3)`. After evaluating, check the result by confirming that $a^3$ is approximately $T^2$.

**Watch Out!** Do not use $T^{3/2}$. That exponent solves the relationship in the opposite direction: it gives period from distance.

```quiz
type: radio
id: problem-1-evaluate-q1
content: |-
  A planet's orbital period is $4.0$ Earth years. What is $a=(4.0)^{2/3}$ to two significant figures?
options:
- id: a
  content: |-
    $2.5\ \mathrm{AU}$
  correct: true
  feedback: |-
    $(4.0)^{2/3}=2.5198\ldots$, which rounds to $2.5\ \mathrm{AU}$.
- id: b
  content: |-
    $8.0\ \mathrm{AU}$
  feedback: |-
    This uses $T^{3/2}$, the inverse direction of the relationship.
- id: c
  content: |-
    $16\ \mathrm{AU}$
  feedback: |-
    This computes $T^2$ but omits the cube root.
```

---

<a id="check-scale-units-and-precision"></a>
## Check Scale, Units, and Precision

**Example:** Without detailed calculation, should a planet with $T=0.125$ Earth years orbit inside or outside Earth's orbit? Then find its distance.

**Explanation**

Because $T<1$ and $a=T^{2/3}$ is increasing for positive $T$, the planet should have $a<1\ \mathrm{AU}$.

Now calculate:

$$
a=(0.125)^{2/3}
=\left(\frac18\right)^{2/3}
=\left(\frac12\right)^2
=0.25\ \mathrm{AU}.
$$

The value passes the scale check: a shorter orbital period corresponds to a smaller orbital distance.

For the normalized formula, the numerical input is in Earth years and the numerical output is in AU. Keep those unit conventions attached to the equation.

```quiz
type: radio
id: problem-1-scale-q1
content: |-
  A planet orbiting the Sun has a period longer than one Earth year. What must the normalized law $a=T^{2/3}$ predict?
options:
- id: a
  content: |-
    $a>1\ \mathrm{AU}$
  correct: true
  feedback: |-
    The positive power $T^{2/3}$ increases with $T$, so a period above $1$ gives a distance above $1$ AU.
- id: b
  content: |-
    $a<1\ \mathrm{AU}$
  feedback: |-
    This reverses the direction of the increasing power relationship.
- id: c
  content: |-
    $a=1\ \mathrm{AU}$ for every period
  feedback: |-
    Only $T=1$ Earth year produces $a=1\ \mathrm{AU}$ in this normalized relation.
```

---

<a id="apply-the-procedure-to-the-hypothetical-planet"></a>
## Apply the Procedure to the Hypothetical Planet

**Example:** A hypothetical planet takes $6.0$ Earth years to orbit the Sun. Find its orbital distance.

**Explanation**

The period is already in Earth years, and the requested distance is in AU, so use

$$
T^2=a^3.
$$

Solve for $a$ and substitute:

$$
\begin{aligned}
a
&=T^{2/3} \\
&=(6.0)^{2/3} \\
&=3.3019\ldots\ \mathrm{AU} \\
&=3.3\ \mathrm{AU}.
\end{aligned}
$$

The period has two significant figures, so the final distance is reported with two significant figures.

A quick back-substitution confirms the scale:

$$
(3.3)^3=35.937\approx36=(6.0)^2.
$$

```quiz
type: radio
id: m3-2pre-q1
content: |-
  **Question 1**

  A hypothetical planet takes $6.0$ Earth years to orbit the Sun. How far is it from the Sun?

  Enter the orbital distance in astronomical units as a number only:
options:
- id: a
  content: 3.3
  correct: true
- id: b
  content: 36
- id: c
  content: 1.8
- id: d
  content: 15
feedback: |-
  Relative to Earth's orbit, Kepler's third law is

  $$
  T^2=a^3,
  $$

  with $T$ in Earth years and $a$ in astronomical units. Therefore,

  $$
  a=T^{2/3}=(6.0)^{2/3}=3.3019\ldots\ \mathrm{AU}.
  $$

  The period has two significant figures, so $a=3.3\ \mathrm{AU}$.
```

---

<a id="summary"></a>
## Summary

For a solar orbit stated in Earth years and AU:

1. Start with $T^2=a^3$.
2. Isolate distance: $a=\sqrt[3]{T^2}=T^{2/3}$.
3. Enter the fractional exponent as a grouped exponent.
4. Check that a period above $1$ year gives a distance above $1$ AU, and vice versa.
5. Keep guard digits and round only the final distance to the precision of the measured period.

The main traps are stopping at $T^2$, omitting the square in $T^{2/3}$, or using the inverse exponent $3/2$.
