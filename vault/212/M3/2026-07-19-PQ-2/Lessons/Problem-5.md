# Four Stars Orbiting at the Corners of a Square

<!--
lesson-id: 212-M3-023
topic-code: MTH212.M3.23
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Square-Geometry Ledger](#build-the-square-geometry-ledger)
- [Combine the Forces Toward the Center](#combine-the-forces-toward-the-center)
- [Use the Net Force for Circular Motion](#use-the-net-force-for-circular-motion)
- [Count Pairs for Potential Energy](#count-pairs-for-potential-energy)
- [Summary](#summary)

## Prerequisites

- Newton's law of gravitation: $F=Gm_1m_2/r^2$
- Uniform circular motion: $F_{\mathrm{net}}=mv^2/r$
- Gravitational potential energy of a pair: $U_{ij}=-Gm_im_j/r_{ij}$
- A square's diagonal is $\sqrt{2}$ times its side

---

<a id="introduction"></a>
## Introduction

When identical masses occupy the corners of a square, the cue is **symmetry**. Choose one star, list every gravitational interaction involving that star, and use the square's geometry before writing any force sum.

![](<../Source/2026-07-19-PQ-2/Images/problem-5-four-star-orbit.png>)

For a square of side length $L$:

- an adjacent corner is distance $L$ away;
- the opposite corner is distance $\sqrt{2}L$ away;
- a corner is distance $L/\sqrt{2}$ from the center.

These three distances control the entire calculation. The central habit is to build this geometry ledger once, then use it consistently for the force, orbit, and energy calculations.

There are two different counting scopes:

- For force and circular motion, focus on **one star** and the three forces acting on it.
- For total potential energy, focus on the **whole system** and count all six pairs once.

---

<a id="build-the-square-geometry-ledger"></a>
## Build the Square-Geometry Ledger

**Example:** For the top star, classify the other three stars by distance and determine its orbital radius.

**Explanation**

The two adjacent stars are each one side length away, so their separations from the top star are $L$. The opposite star lies across a diagonal, so its separation is $\sqrt{2}L$.

The square's center is halfway along a diagonal. Therefore, the radius of the top star's circular path is

$$
r_{\mathrm{orb}}=\frac{\sqrt{2}L}{2}=\frac{L}{\sqrt{2}}.
$$

The complete ledger is:

| Geometric role | Count for one star | Distance |
|---|---:|---:|
| Adjacent stars | $2$ | $L$ |
| Opposite star | $1$ | $\sqrt{2}L$ |
| Corner to center | orbital radius | $L/\sqrt{2}$ |

Keep the **interaction separation** $\sqrt{2}L$ distinct from the **orbital radius** $L/\sqrt{2}$. They come from the same diagonal but serve different roles.

```quiz
type: radio
id: p5-geometry
content: |-
  Four masses occupy the corners of a square of side length $a$. For one selected corner mass, which geometry ledger is correct?
options:
- id: p5-geometry-a
  content: |-
    Two neighbors at $a$, one opposite mass at $\sqrt{2}a$, and orbital radius $a/\sqrt{2}$
  correct: true
- id: p5-geometry-b
  content: |-
    Two neighbors at $a$, one opposite mass at $a/\sqrt{2}$, and orbital radius $\sqrt{2}a$
- id: p5-geometry-c
  content: |-
    Three neighbors at $a$, and orbital radius $a/2$
- id: p5-geometry-d
  content: |-
    Two neighbors at $\sqrt{2}a$, one opposite mass at $a$, and orbital radius $a$
- id: p5-geometry-e
  content: |-
    Two neighbors at $a/2$, one opposite mass at $a$, and orbital radius $\sqrt{2}a/2$
```

---

<a id="combine-the-forces-toward-the-center"></a>
## Combine the Forces Toward the Center

**Example:** Determine the net gravitational force on the top star.

**Explanation**

Define the force scale for either adjacent star:

$$
F_0=\frac{Gm^2}{L^2}.
$$

The opposite star is $\sqrt{2}L$ away, so the inverse-square law gives

$$
F_{\mathrm{opp}}
=\frac{Gm^2}{(\sqrt{2}L)^2}
=\frac{F_0}{2}.
$$

On the free-body diagram, draw two equal forces along the sides toward the adjacent stars and one force along the diagonal toward the opposite star. Let the inward direction be positive and the perpendicular direction be sideways. The force-component ledger is:

| Source | Sideways contribution | Inward contribution |
|---|---:|---:|
| Left adjacent star | $-F_0\sin45^\circ$ | $F_0\cos45^\circ$ |
| Right adjacent star | $+F_0\sin45^\circ$ | $F_0\cos45^\circ$ |
| Opposite star | $0$ | $F_0/2$ |

The sideways components cancel. Each adjacent force contributes $F_0\cos45^\circ=F_0/\sqrt{2}$ inward.

Thus,

$$
\begin{aligned}
F_{\mathrm{net}}
&=2F_0\cos45^\circ+\frac{F_0}{2} \\
&=\left(\sqrt{2}+\frac12\right)F_0 \\
&=\left(\sqrt{2}+\frac12\right)\frac{Gm^2}{L^2}.
\end{aligned}
$$

The net force points from the corner toward the center of the square.

```quiz
type: radio
id: p5-force
content: |-
  Two symmetric forces each have magnitude $K$ and make angles of $45^\circ$ with the inward direction. A third force of magnitude $K/2$ points inward. What is the net force?
options:
- id: p5-force-a
  content: |-
    $\left(\sqrt{2}+\dfrac12\right)K$ inward
  correct: true
- id: p5-force-b
  content: |-
    $\dfrac{5}{2}K$ inward
- id: p5-force-c
  content: |-
    $\dfrac{3}{2}K$ inward
- id: p5-force-d
  content: |-
    $\left(2+\sqrt{2}\right)K$ inward
- id: p5-force-e
  content: |-
    $K/2$ inward because the two symmetric forces cancel completely
```

---

<a id="use-the-net-force-for-circular-motion"></a>
## Use the Net Force for Circular Motion

**Example:** Determine the speed of each star in its circular orbit.

**Explanation**

The inward gravitational force supplies the centripetal force. Use the corner-to-center distance, not the side length, as the orbital radius:

$$
r_{\mathrm{orb}}=\frac{L}{\sqrt{2}}.
$$

Set $F_{\mathrm{net}}=mv^2/r_{\mathrm{orb}}$ and solve for $v^2$:

$$
\begin{aligned}
v^2
&=\frac{F_{\mathrm{net}}r_{\mathrm{orb}}}{m} \\
&=\frac{1}{m}
\left(\sqrt{2}+\frac12\right)\frac{Gm^2}{L^2}
\left(\frac{L}{\sqrt{2}}\right) \\
&=\frac{Gm}{L}\left(1+\frac{1}{2\sqrt{2}}\right).
\end{aligned}
$$

Therefore,

$$
v=\sqrt{\frac{Gm}{L}\left(1+\frac{1}{2\sqrt{2}}\right)}.
$$

```quiz
type: radio
id: p5-speed
content: |-
  Four identical masses $M$ orbit at the corners of a square of side length $a$. Their net inward force is

  $$
  F_{\mathrm{net}}=\left(\sqrt{2}+\frac12\right)\frac{GM^2}{a^2}.
  $$

  Which expression gives their speed?
options:
- id: p5-speed-a
  content: |-
    $\displaystyle \sqrt{\frac{GM}{a}\left(1+\frac{1}{2\sqrt{2}}\right)}$
  correct: true
- id: p5-speed-b
  content: |-
    $\displaystyle \sqrt{\frac{GM}{a}\left(\sqrt{2}+\frac12\right)}$
- id: p5-speed-c
  content: |-
    $\displaystyle \frac{GM}{a}\left(1+\frac{1}{2\sqrt{2}}\right)$
- id: p5-speed-d
  content: |-
    $\displaystyle \sqrt{\frac{GM}{\sqrt{2}a}}$
- id: p5-speed-e
  content: |-
    $\displaystyle \sqrt{\frac{GM}{a}\left(1+\frac{1}{\sqrt{2}}\right)}$
```

---

<a id="count-pairs-for-potential-energy"></a>
## Count Pairs for Potential Energy

**Example:** Determine the total gravitational potential energy of the four-star system.

**Explanation**

Potential energy belongs to **pairs**, so count each pair exactly once. Four objects produce

$$
\binom{4}{2}=6
$$

pairs. In the square, these are four adjacent pairs at distance $L$ and two diagonal pairs at distance $\sqrt{2}L$. Therefore,

| Pair type | Number of pairs | Energy per pair |
|---|---:|---:|
| Adjacent | $4$ | $-Gm^2/L$ |
| Diagonal | $2$ | $-Gm^2/(\sqrt{2}L)$ |

Adding the two rows gives

$$
\begin{aligned}
U
&=4\left(-\frac{Gm^2}{L}\right)
+2\left(-\frac{Gm^2}{\sqrt{2}L}\right) \\
&=-\frac{Gm^2}{L}\left(4+\sqrt{2}\right).
\end{aligned}
$$

Do not multiply a one-star result by four: that counts every pair twice.

```quiz
type: radio
id: p5-energy
content: |-
  Suppose each adjacent pair in a four-corner square has potential energy $-C$, while each diagonal pair has potential energy $-C/\sqrt{2}$. What is the system's total potential energy?
options:
- id: p5-energy-a
  content: |-
    $-(4+\sqrt{2})C$
  correct: true
- id: p5-energy-b
  content: |-
    $-(4+2\sqrt{2})C$
- id: p5-energy-c
  content: |-
    $-(2+\sqrt{2})C$
- id: p5-energy-d
  content: |-
    $-(4+1/\sqrt{2})C$
- id: p5-energy-e
  content: |-
    $-6C$
```

---

<a id="summary"></a>
## Summary

For four identical masses at the corners of a square:

1. Record the geometry: adjacent distance $L$, diagonal distance $\sqrt{2}L$, and orbital radius $L/\sqrt{2}$.
2. For one star, resolve the two adjacent forces inward; their sideways components cancel.
3. Add the opposite-star force to obtain

   $$
   F_{\mathrm{net}}=\left(\sqrt{2}+\frac12\right)\frac{Gm^2}{L^2}.
   $$

4. Set this force equal to $mv^2/(L/\sqrt{2})$ to find the orbital speed.
5. For potential energy, count four edge pairs and two diagonal pairs exactly once.

The main traps are swapping $\sqrt{2}L$ with $L/\sqrt{2}$, failing to resolve the adjacent forces, and double-counting pairs.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: End of Quiz 2 Study Guide.

Study guide index: 20/20

---
<!-- lesson-nav:end -->
