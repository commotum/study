# Gravitational Potential Energy of a Three-Body System

<!--
lesson-id: 212-M3-018
topic-code: MTH212.M3.18
-->

## Table of Contents

- [Introduction](#introduction)
- [Use the pair-energy rule](#use-the-pair-energy-rule)
- [Count every pair exactly once](#count-every-pair-exactly-once)
- [Find a separation from the geometry](#find-a-separation-from-the-geometry)
- [Assemble the three-body energy](#assemble-the-three-body-energy)
- [Summary](#summary)

## Prerequisites

- Recall that gravity is attractive and that gravitational potential energy is zero at infinite separation.
- Use the Pythagorean theorem to find the hypotenuse of a right triangle.
- Add fractions whose denominators do not need to be combined.

---

<a id="introduction"></a>
## Introduction

When a problem asks for the gravitational potential energy of several point masses, look for all the **pairs** of masses. For each pair, use the separation between those two masses—not a squared distance—and add the resulting negative energies:

$$
U_{\mathrm{system}}=\sum_{i<j}-\frac{Gm_im_j}{r_{ij}}.
$$

The condition $i<j$ means that each unordered pair is counted exactly once. For three masses, the pairs are $(1,2)$, $(1,3)$, and $(2,3)$.

---

<a id="use-the-pair-energy-rule"></a>
## Use the pair-energy rule

**Example:** Two asteroids of masses $M$ and $m$ are separated by a distance $r$. Write their gravitational potential energy.

**Explanation**

For one pair of point masses,

$$
U=-\frac{GMm}{r}.
$$

The minus sign reflects attractive gravity when the zero of potential energy is chosen at infinite separation. The distance appears to the first power. The inverse-square expression belongs to the magnitude of the gravitational force, not the potential energy.

```quiz
type: radio
id: p8-pair-rule
content: |-
  Two masses $m_a$ and $m_b$ are separated by $s$. What is their gravitational potential energy?
options:
- id: pair-a
  content: |-
    $-\dfrac{Gm_am_b}{s}$
  correct: true
- id: pair-b
  content: |-
    $-\dfrac{Gm_am_b}{s^2}$
- id: pair-c
  content: |-
    $\dfrac{Gm_am_b}{s}$
- id: pair-d
  content: |-
    $\dfrac{G(m_a+m_b)}{s}$
```

---

<a id="count-every-pair-exactly-once"></a>
## Count every pair exactly once

**Example:** Three masses $m_1$, $m_2$, and $m_3$ have pairwise separations $r_{12}$, $r_{13}$, and $r_{23}$. Write the system's total gravitational potential energy.

**Explanation**

List the pairs before writing any energy terms:

$$
(1,2),\qquad (1,3),\qquad (2,3).
$$

Now add one pair-energy term for each pair:

$$
U=-G\left(\frac{m_1m_2}{r_{12}}+\frac{m_1m_3}{r_{13}}+\frac{m_2m_3}{r_{23}}\right).
$$

There are three terms, not two: the system includes the interaction between $m_2$ and $m_3$ even if neither mass is at the chosen origin.

```quiz
type: radio
id: p8-count-pairs
content: |-
  Three masses have pairwise separations $a=r_{12}$, $b=r_{13}$, and $c=r_{23}$. Which expression gives the total gravitational potential energy?
options:
- id: count-a
  content: |-
    $-G\left(\dfrac{m_1m_2}{a}+\dfrac{m_1m_3}{b}+\dfrac{m_2m_3}{c}\right)$
  correct: true
- id: count-b
  content: |-
    $-G\left(\dfrac{m_1m_2}{a}+\dfrac{m_1m_3}{b}\right)$
- id: count-c
  content: |-
    $G\left(\dfrac{m_1m_2}{a}+\dfrac{m_1m_3}{b}+\dfrac{m_2m_3}{c}\right)$
- id: count-d
  content: |-
    $-G\left(\dfrac{m_1m_2}{a^2}+\dfrac{m_1m_3}{b^2}+\dfrac{m_2m_3}{c^2}\right)$
- id: count-e
  content: |-
    $-2G\left(\dfrac{m_1m_2}{a}+\dfrac{m_1m_3}{b}+\dfrac{m_2m_3}{c}\right)$
```

---

<a id="find-a-separation-from-the-geometry"></a>
## Find a separation from the geometry

**Example:** Mass $m_2$ is a horizontal distance $d_2$ from $m_1$, while $m_3$ is a vertical distance $d_3$ from $m_1$. Find the separation between $m_2$ and $m_3$.

![](<../Source/2026-07-17-HW-5/Images/three-asteroid-geometry.png>)

**Explanation**

The horizontal and vertical segments are perpendicular, so the three masses form a right triangle. The $m_2$-to-$m_3$ separation is its hypotenuse:

$$
r_{23}^2=d_2^2+d_3^2
\qquad\Longrightarrow\qquad
r_{23}=\sqrt{d_2^2+d_3^2}.
$$

Choose the positive square root because a separation is a nonnegative length. The energy term uses $r_{23}$ itself. Therefore its denominator is $\sqrt{d_2^2+d_3^2}$, not $d_2^2+d_3^2$.

```quiz
type: radio
id: p8-diagonal-pair
content: |-
  Masses $m_b$ and $m_c$ lie distances $x$ and $y$ from the same mass along perpendicular directions. Which expression is the gravitational potential energy of the $m_b$-$m_c$ pair?
options:
- id: diagonal-a
  content: |-
    $-\dfrac{Gm_bm_c}{\sqrt{x^2+y^2}}$
  correct: true
- id: diagonal-b
  content: |-
    $-\dfrac{Gm_bm_c}{x^2+y^2}$
- id: diagonal-c
  content: |-
    $-\dfrac{Gm_bm_c}{x+y}$
- id: diagonal-d
  content: |-
    $\dfrac{Gm_bm_c}{\sqrt{x^2+y^2}}$
```

---

<a id="assemble-the-three-body-energy"></a>
## Assemble the three-body energy

**Example:** At one instant, asteroid $m_1$ is a horizontal distance $d_2$ from $m_2$ and a vertical distance $d_3$ from $m_3$. Find the gravitational potential energy stored in the three-asteroid system.

![](<../Source/2026-07-17-HW-5/Images/three-asteroid-geometry.png>)

**Explanation**

Match each pair with its separation:

| Pair | Separation | Pair energy |
|---|---:|---:|
| $(1,2)$ | $d_2$ | $-Gm_1m_2/d_2$ |
| $(1,3)$ | $d_3$ | $-Gm_1m_3/d_3$ |
| $(2,3)$ | $\sqrt{d_2^2+d_3^2}$ | $-Gm_2m_3/\sqrt{d_2^2+d_3^2}$ |

Adding the three interactions gives

$$
\boxed{U=-G\left(\frac{m_1m_2}{d_2}+\frac{m_1m_3}{d_3}+\frac{m_2m_3}{\sqrt{d_2^2+d_3^2}}\right)}.
$$

```quiz
type: radio
id: p8-assemble-system
shuffle: true
content: |-
  At one instant, three asteroids have the arrangement shown. Asteroid $m_1$ is a horizontal distance $d_2$ from $m_2$ and a vertical distance $d_3$ from $m_3$.

  How much gravitational potential energy is stored in the three-asteroid system at this instant?

  ![](<../Source/2026-07-17-HW-5/Images/three-asteroid-geometry.png>)
options:
- id: assemble-a
  content: |-
    $-G\left(\dfrac{m_1m_2}{d_2^2}+\dfrac{m_1m_3}{d_3^2}+\dfrac{m_2m_3}{d_2^2+d_3^2}\right)$
- id: assemble-b
  content: |-
    $G\left(\dfrac{m_1m_2}{d_2^2}+\dfrac{m_1m_3}{d_3^2}+\dfrac{m_2m_3}{\sqrt{d_2^2+d_3^2}}\right)$
- id: assemble-c
  content: |-
    $-G\left(\dfrac{m_1m_2}{d_2}+\dfrac{m_1m_3}{d_3}+\dfrac{m_2m_3}{\sqrt{d_2^2+d_3^2}}\right)$
  correct: true
- id: assemble-d
  content: |-
    $G\left(\dfrac{m_1m_2}{d_2^2}+\dfrac{m_1m_3}{d_3^2}+\dfrac{m_2m_3}{\sqrt{d_2^2+d_3^2}}\right)$
```

---

<a id="summary"></a>
## Summary

When asked for the gravitational potential energy of several point masses:

1. List every unordered pair exactly once.
2. Find the actual separation $r_{ij}$ for each pair from the geometry.
3. Write one term $-Gm_im_j/r_{ij}$ per pair.
4. Add all the pair terms without counting either order twice.

For a right-triangle arrangement, the diagonal separation is the positive length $\sqrt{d_2^2+d_3^2}$. The main trap is importing the inverse-square distance from the force law; gravitational potential energy uses the first power of separation.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Finding a Two-Body Center of Mass as a Fraction of Separation](../../2026-07-16-M3-2/Lessons/Problem-2.md)

Study guide index: 15/20

---
<!-- lesson-nav:end -->
