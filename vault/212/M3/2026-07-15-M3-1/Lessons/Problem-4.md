# Finding Orbital Distance From Orbital Period

<!--
lesson-id: 212-M3-004
topic-code: MTH212.M3.04
-->

## Table of Contents

- [Introduction](#introduction)
- [Recognize the Solar-Unit Form of Kepler's Law](#recognize-the-solar-unit-form-of-keplers-law)
- [Isolate the Orbital Distance](#isolate-the-orbital-distance)
- [Evaluate the Fractional Exponent](#evaluate-the-fractional-exponent)
- [Keep the Required Precision](#keep-the-required-precision)
- [Apply the Method](#apply-the-method)
- [Summary](#summary)

## Prerequisites

- Evaluate squares and cube roots.
- Interpret a fractional exponent such as $x^{2/3}$.
- Round a numerical result to a stated number of significant figures.

---

<a id="introduction"></a>
## Introduction

For a planet orbiting the Sun, Kepler's third law has a convenient form when the period $T$ is measured in **Earth years** and the orbital distance $a$ is measured in **astronomical units**:

$$
T^2=a^3.
$$

The recognition cue is this matching pair of units. To find distance from period, isolate $a$ by taking the cube root:

$$
\boxed{a=T^{2/3}}.
$$

This formula returns $a$ directly in astronomical units. It does not require inserting $G$ or the Sun's mass.

---

<a id="recognize-the-solar-unit-form-of-keplers-law"></a>
## Recognize the Solar-Unit Form of Kepler's Law

**Example:** A planet orbits the Sun with period $T$ measured in Earth years. Its orbital distance $a$ is requested in astronomical units. Choose the useful form of Kepler's third law.

**Explanation**

The units have already normalized the relation to Earth's orbit, where $T=1$ and $a=1$. Therefore,

$$
T^2=a^3.
$$

This compact form is valid for objects orbiting the Sun when the period and distance use this particular unit pair.

```quiz
type: radio
id: m3-1-p4-recognize-kepler-form
content: |-
  A planet orbits the Sun. Its period $T$ is given in Earth years, and its orbital distance $a$ is requested in astronomical units. Which relation should be used?
options:
- id: a
  content: |-
    $T^2=a^3$
  correct: true
  feedback: |-
    With $T$ in Earth years and $a$ in astronomical units for an orbit around the Sun, Kepler's third law is $T^2=a^3$.
- id: b
  content: |-
    $T=a$
- id: c
  content: |-
    $T^3=a^2$
- id: d
  content: |-
    $T^2=a$
- id: e
  content: |-
    $T=a^3$
```

---

<a id="isolate-the-orbital-distance"></a>
## Isolate the Orbital Distance

**Example:** Rearrange $T^2=a^3$ to make $a$ the subject.

**Explanation**

The variable $a$ is cubed, so take the cube root of both sides:

$$
\begin{aligned}
T^2&=a^3\\
\sqrt[3]{T^2}&=\sqrt[3]{a^3}\\
T^{2/3}&=a.
\end{aligned}
$$

Thus,

$$
a=T^{2/3}.
$$

The exponent is $2/3$, not $3/2$: the square is already on $T$, and the cube root undoes the cube on $a$.

| Part of $T^{2/3}$ | Meaning |
|---|---|
| denominator $3$ | take the cube root |
| numerator $2$ | square the result |

The exponent rule also verifies the rearrangement:

$$
\left(T^{2/3}\right)^3=T^{(2/3)(3)}=T^2.
$$

```quiz
type: radio
id: m3-1-p4-isolate-distance
content: |-
  Which expression correctly gives $a$ in terms of $T$ when $T^2=a^3$?
options:
- id: a
  content: |-
    $a=T^{2/3}$
  correct: true
  feedback: |-
    Taking the cube root of $T^2=a^3$ gives $a=\sqrt[3]{T^2}=T^{2/3}$. The reciprocal exponent $3/2$ would solve for $T$ from $a$ instead.
- id: b
  content: |-
    $a=T^{3/2}$
- id: c
  content: |-
    $a=T^6$
- id: d
  content: |-
    $a=T/3$
- id: e
  content: |-
    $a=T^2/3$
```

---

<a id="evaluate-the-fractional-exponent"></a>
## Evaluate the Fractional Exponent

**Example:** Find the orbital distance for a period of $27$ Earth years.

**Explanation**

Evaluate the denominator of the fractional exponent as a root, then apply the numerator as a power:

$$
\begin{aligned}
a
&=27^{2/3}\\
&=\left(\sqrt[3]{27}\right)^2\\
&=3^2\\
&=9\ \mathrm{AU}.
\end{aligned}
$$

For a non-perfect cube, enter the full expression $T^{2/3}$ in a calculator and retain extra digits until the final rounding step.

```quiz
type: radio
id: m3-1-p4-evaluate-fractional-power
content: |-
  A planet takes $64$ Earth years to orbit the Sun. What is its orbital distance?
options:
- id: a
  content: |-
    $16\ \mathrm{AU}$
  correct: true
  feedback: |-
    Use $a=T^{2/3}$: $64^{2/3}=(\sqrt[3]{64})^2=4^2=16\ \mathrm{AU}$.
- id: b
  content: |-
    $8\ \mathrm{AU}$
- id: c
  content: |-
    $32\ \mathrm{AU}$
- id: d
  content: |-
    $256\ \mathrm{AU}$
- id: e
  content: |-
    $4096\ \mathrm{AU}$
```

---

<a id="keep-the-required-precision"></a>
## Keep the Required Precision

**Example:** A period is given as $27.0$ Earth years. Report the corresponding orbital distance to the same three significant figures.

**Explanation**

The unrounded calculation is

$$
a=(27.0)^{2/3}=9\ \mathrm{AU}.
$$

The value $27.0$ has three significant figures, so write the final distance as

$$
a=9.00\ \mathrm{AU}.
$$

Trailing zeros after a decimal point communicate precision. Writing only $9$ would not show three significant figures.

```quiz
type: radio
id: m3-1-p4-significant-figures
content: |-
  A planet's period is $27.0$ Earth years. Which answer reports its orbital distance with the precision supported by the period?
options:
- id: a
  content: |-
    $9.00\ \mathrm{AU}$
  correct: true
  feedback: |-
    Since $(27.0)^{2/3}=9$ and the measured period has three significant figures, report the result as $9.00\ \mathrm{AU}$.
- id: b
  content: |-
    $9\ \mathrm{AU}$
- id: c
  content: |-
    $9.0\ \mathrm{AU}$
- id: d
  content: |-
    $27.0\ \mathrm{AU}$
- id: e
  content: |-
    $729\ \mathrm{AU}$
```

---

<a id="apply-the-method"></a>
## Apply the Method

**Example:** A hypothetical planet takes $8.0$ Earth years to orbit the Sun. Find its orbital distance in astronomical units.

**Explanation**

Use the normalized relation and solve for $a$:

$$
\begin{aligned}
T^2&=a^3\\
a&=T^{2/3}\\
&=(8.0)^{2/3}\\
&=4.0\ \mathrm{AU}.
\end{aligned}
$$

The period $8.0$ has two significant figures, so the answer must retain the trailing zero: $4.0$, not merely $4$.

Two checks support the result:

- Since $8.0$ years is longer than Earth's $1$-year period, the distance should be greater than $1\ \mathrm{AU}$.
- Substitution gives $(4.0)^3=64$ and $(8.0)^2=64$, so $T^2=a^3$ is satisfied.

```quiz
type: radio
id: m3-1lec-q3
content: |-
  **Question 3**

  A hypothetical planet takes $8.0$ Earth years to complete one orbit around the Sun. How far is it from the Sun?

  Enter the orbital distance in astronomical units as a number only:
options:
- id: a
  content: |-
    `4.0`
  correct: true
  feedback: |-
    Relative to Earth's orbit, Kepler's third law is

    $$
    T^2=a^3,
    $$

    with $T$ in Earth years and $a$ in astronomical units. Therefore,

    $$
    a=T^{2/3}=(8.0)^{2/3}=4.0\ \mathrm{AU}.
    $$

    The period is given with two significant figures, so the distance is $4.0\ \mathrm{AU}$.
- id: b
  content: |-
    `4`
- id: c
  content: |-
    `16`
- id: d
  content: |-
    `23`
- id: e
  content: |-
    `64`
```

---

<a id="summary"></a>
## Summary

- **Cue:** the object orbits the Sun, $T$ is in Earth years, and $a$ is requested in astronomical units.
- **Relation:** $T^2=a^3$.
- **Solve:** take the cube root to get $a=T^{2/3}$.
- **Evaluate:** $T^{2/3}=(\sqrt[3]{T})^2$.
- **Precision:** keep calculator digits until the end, then match the significant figures in the measured period.
- **Check:** substitute the result back into $T^2=a^3$ and compare its direction with Earth's $T=a=1$ reference.
- **Main trap:** use $2/3$, not $3/2$, when solving for $a$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
