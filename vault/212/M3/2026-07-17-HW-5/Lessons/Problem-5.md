# Scaling Orbital Period with Orbital Radius

<!--
lesson-id: 212-M3-015
topic-code: MTH212.M3.15
-->

## Table of Contents

- [Introduction](#introduction)
- [Compare Two Circular Orbits](#compare-two-circular-orbits)
- [Simplify the Radius Scale Factor](#simplify-the-radius-scale-factor)
- [Move to a Smaller Orbit](#move-to-a-smaller-orbit)
- [Avoid Linear and Cubic Scaling Traps](#avoid-linear-and-cubic-scaling-traps)

## Prerequisites

- Form ratios from two versions of the same equation.
- Apply powers and simplify square roots.

---

<a id="introduction"></a>
## Introduction

For circular orbits around the same central body, Kepler's third law can be written as

$$
T^2=Cr^3,
$$

where $T$ is the orbital period, $r$ is the orbital radius, and $C$ is the same constant for both orbits.

The recognition cue is a change in orbital radius with the central body unchanged. Compare the old and new orbits so that $C$ cancels, then take the positive square root because a period is positive.

**Orbital-period scale rule:** If $k=r_2/r_1$, then

$$
\frac{T_2}{T_1}=k^{3/2}=\sqrt{k^3}.
$$

---

<a id="compare-two-circular-orbits"></a>
## Compare Two Circular Orbits

**Example:** A satellite's circular-orbit radius changes from $r$ to $4r$. If its original period is $T$, find the new period $T_2$.

**Explanation**

Write Kepler's law for the new and old orbits and divide:

$$
\frac{T_2^2}{T^2}=\frac{C(4r)^3}{Cr^3}=4^3.
$$

Now take the positive square root:

$$
\frac{T_2}{T}=\sqrt{4^3}=4^{3/2}=8.
$$

Therefore, $T_2=8T$.

```quiz
type: radio
id: p5-q1
content: |-
  A satellite's circular-orbit radius changes from $r$ to $9r$. If its original period is $T$, what is its new period?
options:
- id: a
  content: |-
    $9T$
- id: b
  content: |-
    $18T$
- id: c
  content: |-
    $27T$
  correct: true
- id: d
  content: |-
    $81T$
- id: e
  content: |-
    $729T$
```

---

<a id="simplify-the-radius-scale-factor"></a>
## Simplify the Radius Scale Factor

**Example:** A satellite's orbital radius increases from $r$ to $5r$. Find the period scale factor.

**Explanation**

If the radius is multiplied by $k$, then

$$
\frac{T_2}{T_1}=k^{3/2}=\sqrt{k^3}=k\sqrt{k}.
$$

With $k=5$,

$$
\frac{T_2}{T_1}=\sqrt{5^3}=\sqrt{25\cdot5}=5\sqrt5.
$$

The new period is $5\sqrt5$ times the original period.

```quiz
type: radio
id: p5-q2
content: |-
  A satellite in a circular orbit of radius $r$ has period $T$.

  If the satellite is moved to a new circular orbit of radius $2r$, what is its new period?
options:
- id: a
  content: |-
    $2T$
  feedback: |-
    This treats period as directly proportional to radius and ignores the exponents in Kepler's law.
- id: b
  content: |-
    $2\sqrt{2}\,T$
  correct: true
  feedback: |-
    The radius factor is $2$, so the period factor is $2^{3/2}=2\sqrt2$.
- id: c
  content: |-
    $4T$
  feedback: |-
    This squares the radius factor; Kepler's law instead gives a period factor of $2^{3/2}$.
```

---

<a id="move-to-a-smaller-orbit"></a>
## Move to a Smaller Orbit

**Example:** A satellite moves from radius $r$ to radius $r/4$. Find its new period in terms of $T$.

**Explanation**

Here the radius scale factor is $k=1/4$. Use the same rule:

$$
\frac{T_2}{T}=\left(\frac14\right)^{3/2}
=\left(\frac12\right)^3
=\frac18.
$$

Therefore, $T_2=T/8$. A smaller orbit has a shorter period, which agrees with the result.

```quiz
type: radio
id: p5-q3
content: |-
  A satellite's circular-orbit radius decreases from $r$ to $r/9$. What is its new period in terms of its original period $T$?
options:
- id: a
  content: |-
    $T/9$
- id: b
  content: |-
    $T/18$
- id: c
  content: |-
    $T/27$
  correct: true
- id: d
  content: |-
    $T/81$
- id: e
  content: |-
    $T/729$
```

---

<a id="avoid-linear-and-cubic-scaling-traps"></a>
## Avoid Linear and Cubic Scaling Traps

**Example:** The orbital radius triples. Decide whether the new period is $3T$, $9T$, $27T$, or another value.

**Explanation**

Kepler's law relates the *squares* of periods to the *cubes* of radii:

$$
\left(\frac{T_2}{T}\right)^2=3^3=27.
$$

Taking the square root gives

$$
\frac{T_2}{T}=\sqrt{27}=3\sqrt3.
$$

The linear answer $3T$ ignores the exponents. The cubic answer $27T$ forgets to take the square root.

For a quick check when $k>1$, the exponent $3/2$ lies between $1$ and $2$, so $k^{3/2}$ must lie between $k$ and $k^2$. For $k=3$, the factor $3\sqrt3$ is between $3$ and $9$.

```quiz
type: radio
id: p5-q4
content: |-
  If a circular-orbit radius is multiplied by a positive factor $k$, which expression gives the new period in terms of the old period $T$?
options:
- id: a
  content: |-
    $kT$
- id: b
  content: |-
    $k^2T$
- id: c
  content: |-
    $k^{3/2}T$
  correct: true
- id: d
  content: |-
    $k^3T$
- id: e
  content: |-
    $k^{2/3}T$
```

---

## Summary

When two circular orbits are around the same central body:

1. Find the radius scale factor $k=r_2/r_1$.
2. Apply $T_2/T_1=k^{3/2}=\sqrt{k^3}$.
3. Take the positive root because orbital period is positive.
4. Check direction: a larger radius must give a longer period. When $k>1$, the factor $k^{3/2}$ should also lie between $k$ and $k^2$.

The main trap is using $k$ or $k^3$ instead of $k^{3/2}$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
