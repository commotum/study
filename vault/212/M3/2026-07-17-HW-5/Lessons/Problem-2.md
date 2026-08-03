# Balancing Opposing Inverse-Square Forces

<!--
lesson-id: 212-M3-012
topic-code: MTH212.M3.12
-->

## Table of Contents

- [Introduction](#introduction)
- [Write the Two Distances](#write-the-two-distances)
- [Equate the Force Magnitudes](#equate-the-force-magnitudes)
- [Take the Physical Square Root](#take-the-physical-square-root)
- [Simplify and Check the Position](#simplify-and-check-the-position)
- [Summary](#summary)

## Prerequisites

- Newton's law of gravitation, $F=Gm_1m_2/r^2$
- Solving a linear equation with the variable on both sides
- Simplifying square roots and rationalizing a denominator

---

<a id="introduction"></a>
## Introduction

When a test mass lies between two attracting masses, the two gravitational forces point in opposite directions. The net force is zero exactly when their **magnitudes are equal**.

The recognition cue is a point between two sources governed by an inverse-square law. The reusable move is:

1. Write the two distances using the total separation.
2. Equate the two force magnitudes.
3. Cancel common positive factors.
4. Take the positive square root because distances are positive.
5. Solve the resulting linear equation and check that the answer lies between the sources.

---

<a id="write-the-two-distances"></a>
## Write the Two Distances

**Example:** Two source masses are separated by a distance $L$. A test mass is between them, a distance $x$ from the left source. Write its distance from the right source.

**Explanation**

The two smaller distances fill the whole segment, so

$$
x+r_{\text{right}}=L.
$$

Therefore,

$$
r_{\text{right}}=L-x.
$$

Using $L+x$ would place the test mass outside the segment rather than between the sources.

```quiz
type: radio
id: p2-distance-1
content: |-
  Two masses are $D$ apart. A test mass lies between them, $y$ from the left mass. What is its distance from the right mass?
options:
- id: a
  content: |-
    $D-y$
  correct: true
- id: b
  content: |-
    $D+y$
- id: c
  content: |-
    $y-D$
- id: d
  content: |-
    $D/y$
```

---

<a id="equate-the-force-magnitudes"></a>
## Equate the Force Magnitudes

**Example:** A mass $4M$ is on the left and a mass $M$ is on the right, separated by $L$. A test mass $m$ is placed between them at distance $x$ from the left mass. Find the balance equation after canceling common factors.

**Explanation**

The left source pulls left with magnitude

$$
F_L=\frac{G(4M)m}{x^2},
$$

and the right source pulls right with magnitude

$$
F_R=\frac{G(M)m}{(L-x)^2}.
$$

Set $F_L=F_R$ and cancel the shared positive factor $GMm$:

$$
\frac{4}{x^2}=\frac{1}{(L-x)^2}.
$$

Only common factors cancel. The source-mass factors $4$ and $1$ must remain because they determine the balance point.

```quiz
type: radio
id: p2-balance-1
content: |-
  A mass $5M$ is on the left and a mass $2M$ is on the right, separated by $D$. A test mass lies between them at distance $y$ from the left mass. After common factors are canceled, which equation gives zero net force?
options:
- id: a
  content: |-
    $\dfrac{5}{y^2}=\dfrac{2}{(D-y)^2}$
  correct: true
- id: b
  content: |-
    $\dfrac{5}{y^2}=\dfrac{2}{(D+y)^2}$
- id: c
  content: |-
    $\dfrac{5}{y}=\dfrac{2}{D-y}$
- id: d
  content: |-
    $\dfrac{1}{y^2}=\dfrac{1}{(D-y)^2}$
```

---

<a id="take-the-physical-square-root"></a>
## Take the Physical Square Root

**Example:** Solve the balance equation

$$
\frac{4}{x^2}=\frac{1}{(L-x)^2}, \qquad 0<x<L.
$$

**Explanation**

Because $x$ and $L-x$ are distances inside the segment, both are positive. Take the positive square root:

$$
\frac{2}{x}=\frac{1}{L-x}.
$$

In general, the square-root step turns the inverse-square balance into a distance ratio:

$$
\frac{x}{L-x}=\sqrt{\frac{M_L}{M_R}}.
$$

Thus the distance from a source grows with the square root of that source's mass. The balance point must be farther from the larger source and closer to the smaller one.

Cross-multiply and solve:

$$
\begin{aligned}
2(L-x)&=x,\\
2L&=3x,\\
x&=\frac{2L}{3}.
\end{aligned}
$$

The balance point is closer to the smaller mass: its distance from the right-hand mass is only $L/3$.

```quiz
type: radio
id: p2-root-1
content: |-
  A mass $M$ is on the left and a mass $9M$ is on the right, separated by $L$. A test mass is between them at distance $x$ from the left mass. Where is the balance point?
options:
- id: a
  content: |-
    $x=\dfrac{L}{4}$
  correct: true
- id: b
  content: |-
    $x=\dfrac{3L}{4}$
- id: c
  content: |-
    $x=\dfrac{L}{10}$
- id: d
  content: |-
    $x=\dfrac{9L}{10}$
```

---

<a id="simplify-and-check-the-position"></a>
## Simplify and Check the Position

**Example:** A mass $3m$ is on the left and a mass $2m$ is on the right, separated by $d$. A test mass $m$ is between them at distance $x$ from the left mass. Find $x$.

**Explanation**

Set the opposing force magnitudes equal:

$$
\frac{G(3m)m}{x^2}=\frac{G(2m)m}{(d-x)^2}.
$$

Cancel $Gm^2$, take the positive square root, and solve:

$$
\begin{aligned}
\frac{3}{x^2}&=\frac{2}{(d-x)^2},\\
\frac{\sqrt{3}}{x}&=\frac{\sqrt{2}}{d-x},\\
\sqrt{3}(d-x)&=\sqrt{2}x,\\
x&=\frac{\sqrt{3}}{\sqrt{3}+\sqrt{2}}d.
\end{aligned}
$$

Rationalize the denominator:

$$
\begin{aligned}
x&=\frac{\sqrt{3}(\sqrt{3}-\sqrt{2})}{(\sqrt{3}+\sqrt{2})(\sqrt{3}-\sqrt{2})}d\\
&=(3-\sqrt{6})d.
\end{aligned}
$$

Since $3-\sqrt{6}\approx 0.551$, the result satisfies $0<x<d$ and is closer to the smaller right-hand mass, as expected.

```quiz
type: radio
id: p2-final-1
content: |-
  Three masses lie on a line. The left mass is $3m$, the right mass is $2m$, and their separation is $d$. A mass $m$ is between them at distance $x$ from the left mass. What must $x$ be so that the net gravitational force on $m$ is zero?
options:
- id: a
  content: |-
    $(3+\sqrt{6})d$
- id: b
  content: |-
    $(3-\sqrt{6})d$
  correct: true
- id: c
  content: |-
    $(2+\sqrt{3})d$
- id: d
  content: |-
    $(2-\sqrt{3})d$
```

---

## Summary

For a test mass between left and right source masses $M_L$ and $M_R$ separated by $L$:

$$
\frac{M_L}{x^2}=\frac{M_R}{(L-x)^2}.
$$

Use this checklist:

1. Use $x$ and $L-x$ for the two distances.
2. Equate force magnitudes and cancel only common factors.
3. Take the positive square root, giving $x/(L-x)=\sqrt{M_L/M_R}$.
4. Solve the linear equation.
5. Verify $0<x<L$ and confirm the point is closer to the smaller source mass.

The main traps are using $L+x$, dropping a source-mass factor, forgetting the square on distance, or keeping a nonphysical square-root branch.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
