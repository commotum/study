# Scaling Kinetic Energy in a Circular Orbit

<!--
lesson-id: 212-M3-016
topic-code: MTH212.M3.16
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Circular-Orbit Energy Formula](#build-the-circular-orbit-energy-formula)
- [Compare Two Orbits With a Ratio](#compare-two-orbits-with-a-ratio)
- [Read Any Radius Scale Factor](#read-any-radius-scale-factor)
- [Avoid the Inverse-Square Trap](#avoid-the-inverse-square-trap)
- [Apply the Rule to the Given Orbit](#apply-the-rule-to-the-given-orbit)
- [Summary](#summary)

## Prerequisites

- Use the inward-positive radial equation $\sum F_r=m a_r=mv^2/r$ for uniform circular motion.
- Use $F_g=GMm/r^2$ for gravitational force.
- Simplify ratios and reciprocal scale factors.

---

<a id="introduction"></a>
## Introduction

When the same satellite moves between circular orbits around the same central body, its orbital kinetic energy depends inversely on the orbital radius:

$$
K=\frac{GMm}{2r}.
$$

The recognition cues are **circular orbit**, a changed **orbital radius**, and a request for the new kinetic energy. Because $G$, $M$, and the satellite mass $m$ stay fixed, only the factor $1/r$ changes.

These three statements are equivalent for this setting:

$$
K\propto\frac1r,
\qquad
K=\frac{C}{r},
\qquad
Kr=C,
$$

where $C=GMm/2$ is constant. The product form says that the old and new orbits satisfy $K_1r_1=K_2r_2$.

If the radius is multiplied by a factor $c$, then the kinetic energy is divided by that factor:

$$
r_{\mathrm{new}}=cr_{\mathrm{old}}
\quad\Longrightarrow\quad
K_{\mathrm{new}}=\frac{1}{c}K_{\mathrm{old}}.
$$

---

<a id="build-the-circular-orbit-energy-formula"></a>
## Build the Circular-Orbit Energy Formula

**Example:** Derive the kinetic energy of a satellite of mass $m$ in a circular orbit of radius $r$ around a body of mass $M$.

**Explanation**

Take inward as positive. Gravity supplies the radial net force, so

$$
\sum F_r=m a_r=m\frac{v^2}{r}=F_g=\frac{GMm}{r^2}.
$$

Cancel $m$ and one factor of $r$:

$$
v^2=\frac{GM}{r}.
$$

Substitute this into $K=\frac12mv^2$:

$$
K=\frac12m\left(\frac{GM}{r}\right)
=\frac{GMm}{2r}.
$$

Thus $K\propto 1/r$ for circular orbits about the same central body.

```quiz
type: radio
id: p6-build-formula
content: |-
  Which expression gives the kinetic energy of a satellite of mass $m$ in a circular orbit of radius $r$ around a body of mass $M$?
options:
- id: a
  content: |-
    $\dfrac{GMm}{2r}$
  correct: true
- id: b
  content: |-
    $\dfrac{GMm}{r^2}$
- id: c
  content: |-
    $\dfrac{GMm}{2r^2}$
- id: d
  content: |-
    $\dfrac{2GMm}{r}$
- id: e
  content: |-
    $\dfrac{GM}{2mr}$
```

---

<a id="compare-two-orbits-with-a-ratio"></a>
## Compare Two Orbits With a Ratio

**Example:** A satellite has kinetic energy $K_1$ in a circular orbit of radius $r_1$. Find $K_2/K_1$ if its new circular orbit has radius $r_2$.

**Explanation**

Write the circular-orbit formula once for each orbit:

$$
K_1=\frac{GMm}{2r_1},
\qquad
K_2=\frac{GMm}{2r_2}.
$$

Divide the new value by the old value. The unchanged factors cancel:

$$
\frac{K_2}{K_1}
=\frac{GMm/(2r_2)}{GMm/(2r_1)}
=\frac{r_1}{r_2}.
$$

Equivalently, use the constant product:

$$
K_1r_1=K_2r_2
\quad\Longrightarrow\quad
K_2=K_1\frac{r_1}{r_2}.
$$

Both forms avoid computing $G$, $M$, or $m$. Put the **old radius over the new radius** so the direction of the change is built into the calculation.

```quiz
type: radio
id: p6-ratio-method
content: |-
  A satellite moves from a circular orbit of radius $r$ to one of radius $4r$. What is $K_{\mathrm{new}}/K_{\mathrm{old}}$?
options:
- id: a
  content: |-
    $\dfrac14$
  correct: true
- id: b
  content: |-
    $\dfrac1{16}$
- id: c
  content: |-
    $4$
- id: d
  content: |-
    $16$
- id: e
  content: |-
    $1$
```

---

<a id="read-any-radius-scale-factor"></a>
## Read Any Radius Scale Factor

**Example:** A satellite's circular-orbit radius changes from $r$ to $\frac35r$. Express the new kinetic energy in terms of the old kinetic energy $K$.

**Explanation**

Here the radius scale factor is $c=\frac35$. Since kinetic energy uses the reciprocal factor,

$$
K_{\mathrm{new}}
=\frac{1}{3/5}K
=\frac53K.
$$

The smaller orbit has greater kinetic energy. This direction check is useful: when $r$ decreases in $K\propto 1/r$, $K$ must increase.

```quiz
type: radio
id: p6-fractional-scale
content: |-
  A satellite in a circular orbit has kinetic energy $K$. If its orbital radius becomes $\frac23$ of its original radius, what is its new kinetic energy?
options:
- id: a
  content: |-
    $\dfrac32K$
  correct: true
- id: b
  content: |-
    $\dfrac23K$
- id: c
  content: |-
    $\dfrac94K$
- id: d
  content: |-
    $\dfrac49K$
- id: e
  content: |-
    $K$
```

---

<a id="avoid-the-inverse-square-trap"></a>
## Avoid the Inverse-Square Trap

**Example:** If a circular-orbit radius doubles, should the kinetic energy become $K/2$ or $K/4$?

**Explanation**

Gravitational force has an inverse-square dependence:

$$
F_g=\frac{GMm}{r^2}.
$$

Circular-orbit kinetic energy does not. After the circular-motion condition is used, one power of $r$ cancels, leaving

$$
K=\frac{GMm}{2r}.
$$

Therefore, doubling $r$ divides $K$ by $2$, not by $2^2$. The exponent belongs to the formula for the requested quantity.

```quiz
type: radio
id: p6-power-check
content: |-
  A satellite's circular-orbit radius triples. Which comparison is correct?
options:
- id: a
  content: |-
    Its gravitational force becomes $F/9$, while its kinetic energy becomes $K/3$.
  correct: true
- id: b
  content: |-
    Its gravitational force and kinetic energy both become one-third as large.
- id: c
  content: |-
    Its gravitational force and kinetic energy both become one-ninth as large.
- id: d
  content: |-
    Its gravitational force becomes $F/3$, while its kinetic energy becomes $K/9$.
- id: e
  content: |-
    Its gravitational force becomes $3F$, while its kinetic energy becomes $3K$.
```

---

<a id="apply-the-rule-to-the-given-orbit"></a>
## Apply the Rule to the Given Orbit

**Example:** A satellite in a circular orbit of radius $r$ has kinetic energy $K$. Find its kinetic energy in a new circular orbit of radius $2r$.

**Explanation**

Compare the new orbit with the old orbit:

$$
\frac{K_{\mathrm{new}}}{K}
=\frac{r}{2r}
=\frac12.
$$

Therefore,

$$
K_{\mathrm{new}}=\frac{K}{2}.
$$

```quiz
type: radio
id: p6-original-check
content: |-
  A satellite in a circular orbit of radius $r$ has kinetic energy $K$.

  If the satellite is moved to a new circular orbit of radius $2r$, what is its new kinetic energy?
options:
- id: a
  content: |-
    $K/2$
  correct: true
- id: b
  content: |-
    $K/4$
- id: c
  content: |-
    $2K$
- id: d
  content: |-
    $4K$
```

---

<a id="summary"></a>
## Summary

For the same satellite in circular orbits around the same central mass:

1. Start with $K=GMm/(2r)$, so $K\propto 1/r$.
2. Use the invariant $K_{\mathrm{old}}r_{\mathrm{old}}=K_{\mathrm{new}}r_{\mathrm{new}}$.
3. Compare the orbits with $K_{\mathrm{new}}/K_{\mathrm{old}}=r_{\mathrm{old}}/r_{\mathrm{new}}$.
4. If the radius is multiplied by $c$, divide the kinetic energy by $c$.
5. Check the direction: a larger circular orbit has smaller kinetic energy.
6. Do not use the $1/r^2$ scaling of gravitational force for kinetic energy.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Total Mechanical Energy of a Three-Body Orbit](../../2026-07-16-M3-2/Lessons/Problem-6.md)

Study guide index: 18/20

---
<!-- lesson-nav:end -->
