# Locate a Center of Mass from a Coordinate Ledger

<!--
lesson-id: 212-M3-039
topic-code: MTH212.M3.39
-->

## Table of Contents

- [Introduction](#introduction)
- [Weight Positions on One Axis](#weight-positions-on-one-axis)
- [Compute Two Coordinates Separately](#compute-two-coordinates-separately)
- [Compress Identical Blocks into Groups](#compress-identical-blocks-into-groups)
- [Replace Uniform Pieces by Masses at Their Centers](#replace-uniform-pieces-by-masses-at-their-centers)
- [Summary](#summary)

## Prerequisites

- Choose an origin and positive coordinate directions.
- Add signed numbers and multiply mass by position.
- Locate the geometric center of a uniform block or cube.
- Use $m=\rho V$ for a uniform object of density $\rho$.

---

<a id="introduction"></a>
## Introduction

When several masses have known positions and the question asks for their combined center, make a coordinate ledger. For total mass

$$
M=\sum_i m_i,
$$

the center-of-mass coordinates are

$$
\boxed{x_{\mathrm{cm}}=\frac{\sum_i m_i x_i}{M}},
\qquad
\boxed{y_{\mathrm{cm}}=\frac{\sum_i m_i y_i}{M}}.
$$

Each numerator is a weighted-position total, while the denominator is the mass total. Keep the axes separate: the $m_i x_i$ products determine $x_{\mathrm{cm}}$, and the $m_i y_i$ products determine $y_{\mathrm{cm}}$.

Use this procedure:

1. Choose one origin and positive directions.
2. Predict the region containing the answer.
3. Record every mass with its signed coordinates.
4. Form the $m_i x_i$ and, when needed, $m_i y_i$ columns.
5. Divide each product sum by the same total mass $M$.
6. Check that each coordinate lies between the smallest and largest occupied coordinate and that the point is pulled toward the heavier concentration.

A coordinate may be negative; mass is not. A point at $x=-2\,\mathrm m$ contributes a negative $m_i x_i$ term. The center is a mass-weighted position, so it need not be the geometric midpoint and it does not split the total mass into equal halves.

---

<a id="weight-positions-on-one-axis"></a>
## Weight Positions on One Axis

**Source-video worked problem 1 (`2uszSnvzBEU`, 00:00:01–00:02:04):** A $5\,\mathrm{kg}$ mass is at $x=0$, and a $9\,\mathrm{kg}$ mass is at $x=2\,\mathrm m$. Find the center of mass.

**Explanation**

Before calculating, the center must lie between $0$ and $2\,\mathrm m$. Since the $9\,\mathrm{kg}$ mass is heavier, the result should be closer to $2\,\mathrm m$, hence somewhere between $1$ and $2\,\mathrm m$.

| $i$ | $m_i$ | $x_i$ | $m_i x_i$ |
|---:|---:|---:|---:|
| 1 | $5\,\mathrm{kg}$ | $0$ | $0$ |
| 2 | $9\,\mathrm{kg}$ | $2\,\mathrm m$ | $18\,\mathrm{kg\,m}$ |
| total | $14\,\mathrm{kg}$ |  | $18\,\mathrm{kg\,m}$ |

Therefore,

$$
x_{\mathrm{cm}}
=\frac{18\,\mathrm{kg\,m}}{14\,\mathrm{kg}}
=1.2857\ldots\,\mathrm m
\approx\boxed{1.29\,\mathrm m}.
$$

The unit reduces to length, and $1.29\,\mathrm m$ passes the predicted-region check.

```quiz
type: radio
id: mct-p3-one-axis-mirrored
shuffle: true
content: |-
  A $6\,\mathrm{kg}$ mass is at $x=0$, and a $10\,\mathrm{kg}$ mass is at $x=3.00\,\mathrm m$. Where is the center of mass?
options:
- id: mct-p3-one-axis-mirrored-a
  content: |-
    $1.88\,\mathrm m$
  correct: true
  feedback: |-
    A center of mass is the mass-weighted position. Here $M=16\,\mathrm{kg}$ and $\sum m_i x_i=(6)(0)+(10)(3.00)=30.0\,\mathrm{kg\,m}$, so $x_{\mathrm{cm}}=30.0/16=1.875\,\mathrm m\approx1.88\,\mathrm m$, between the masses and closer to the $10\,\mathrm{kg}$ mass.
- id: mct-p3-one-axis-mirrored-b
  content: |-
    $1.50\,\mathrm m$
  feedback: |-
    This is the geometric midpoint of $0$ and $3.00\,\mathrm m$, which would apply to equal masses. The $10\,\mathrm{kg}$ mass carries more weight in the average, so the center shifts right to $1.88\,\mathrm m$.
- id: mct-p3-one-axis-mirrored-c
  content: |-
    $3.00\,\mathrm m$
  feedback: |-
    The center would coincide with $x=3.00\,\mathrm m$ only if all of the system's mass were there. The $6\,\mathrm{kg}$ mass at the origin pulls the weighted position left, giving $1.88\,\mathrm m$.
- id: mct-p3-one-axis-mirrored-d
  content: |-
    $30.0\,\mathrm{kg\,m}$
  feedback: |-
    This is the weighted-position numerator $\sum m_i x_i$, not a location. Divide it by the total mass $16\,\mathrm{kg}$; the mass units cancel and the coordinate is $1.88\,\mathrm m$.
- id: mct-p3-one-axis-mirrored-e
  content: |-
    $1.13\,\mathrm m$
  feedback: |-
    This results from attaching $x=3.00\,\mathrm m$ to the $6\,\mathrm{kg}$ mass and $x=0$ to the $10\,\mathrm{kg}$ mass. Keep each coordinate on the same ledger row as its mass: $(6)(0)+(10)(3.00)$, not $(6)(3.00)+(10)(0)$.
```

---

<a id="compute-two-coordinates-separately"></a>
## Compute Two Coordinates Separately

**Source-video worked problem 3 (`2uszSnvzBEU`, 00:04:19–00:09:26):** Four masses occupy the following positions:

$$
4\,\mathrm{kg}\text{ at }(0,0),\quad
6\,\mathrm{kg}\text{ at }(4,0)\,\mathrm m,
$$

$$
7\,\mathrm{kg}\text{ at }(0,5)\,\mathrm m,\quad
10\,\mathrm{kg}\text{ at }(5,6)\,\mathrm m.
$$

Find $(x_{\mathrm{cm}},y_{\mathrm{cm}})$.

**Explanation**

Use one row per mass and separate product columns for $x$ and $y$:

$$
M(x_{\mathrm{cm}},y_{\mathrm{cm}})
=\left(\sum_i m_i x_i,\sum_i m_i y_i\right).
$$

This identity is a bookkeeping check: an $x$-coordinate never enters the $y$-sum, and a $y$-coordinate never enters the $x$-sum.

| $m_i$ ($\mathrm{kg}$) | $x_i$ ($\mathrm m$) | $m_i x_i$ ($\mathrm{kg\,m}$) | $y_i$ ($\mathrm m$) | $m_i y_i$ ($\mathrm{kg\,m}$) |
|---:|---:|---:|---:|---:|
| $4$ | $0$ | $0$ | $0$ | $0$ |
| $6$ | $4$ | $24$ | $0$ | $0$ |
| $7$ | $0$ | $0$ | $5$ | $35$ |
| $10$ | $5$ | $50$ | $6$ | $60$ |
| **$M=27$** |  | **$74$** |  | **$95$** |

The total mass is

$$
M=4+6+7+10=27\,\mathrm{kg}.
$$

Use that same $27\,\mathrm{kg}$ denominator for both coordinates:

$$
x_{\mathrm{cm}}=\frac{74}{27}\,\mathrm m
=2.7407\ldots\,\mathrm m
\approx\boxed{2.74\,\mathrm m},
$$

$$
y_{\mathrm{cm}}=\frac{95}{27}\,\mathrm m
=3.5185\ldots\,\mathrm m
\approx\boxed{3.519\,\mathrm m}.
$$

Thus,

$$
\boxed{(x_{\mathrm{cm}},y_{\mathrm{cm}})=(2.74,3.519)\,\mathrm m}.
$$

Both coordinates lie inside the occupied ranges, $0\le x\le5$ and $0\le y\le6$, and the result is shifted toward the $10\,\mathrm{kg}$ mass in the upper-right region.

**Source correction:** The automatic caption calls the third mass “70 kilograms” once, but the stated data, the $7(5)=35\,\mathrm{kg\,m}$ product, and the $27\,\mathrm{kg}$ denominator all require $7\,\mathrm{kg}$. The closing caption also garbles the last digits of the $y$-coordinate; the ledger gives $95/27=3.5185\ldots\,\mathrm m$, reported as $3.519\,\mathrm m$.

```quiz
type: radio
id: mct-p3-two-axis-signed
shuffle: true
content: |-
  Three point masses have the following positions: $2\,\mathrm{kg}$ at $(-3,1)\,\mathrm m$, $4\,\mathrm{kg}$ at $(1,-2)\,\mathrm m$, and $6\,\mathrm{kg}$ at $(2,3)\,\mathrm m$. What is their center of mass?
options:
- id: mct-p3-two-axis-signed-a
  content: |-
    $(0.833,1.00)\,\mathrm m$
  correct: true
  feedback: |-
    Keep the coordinate signs in separate ledgers. With $M=12\,\mathrm{kg}$, $\sum m_i x_i=2(-3)+4(1)+6(2)=10$ and $\sum m_i y_i=2(1)+4(-2)+6(3)=12$, so the center is $(10/12,12/12)\,\mathrm m=(0.833,1.00)\,\mathrm m$.
- id: mct-p3-two-axis-signed-b
  content: |-
    $(1.83,2.33)\,\mathrm m$
  feedback: |-
    These values come from replacing negative coordinates by their absolute values. Coordinates encode direction from the chosen origin, so the terms $2(-3)$ and $4(-2)$ must remain negative in their respective product sums.
- id: mct-p3-two-axis-signed-c
  content: |-
    $(0,0.667)\,\mathrm m$
  feedback: |-
    This averages the three coordinate pairs without using their masses. An ordinary coordinate average applies only when all masses are equal; weighting by $2$, $4$, and $6\,\mathrm{kg}$ gives $(0.833,1.00)\,\mathrm m$.
- id: mct-p3-two-axis-signed-d
  content: |-
    $(10,12)\,\mathrm m$
  feedback: |-
    The numbers $10$ and $12$ are the signed product sums $\sum m_i x_i$ and $\sum m_i y_i$. Divide both by the full $12\,\mathrm{kg}$ total mass to convert those weighted sums into coordinates.
- id: mct-p3-two-axis-signed-e
  content: |-
    $(0.833,-1.00)\,\mathrm m$
  feedback: |-
    A negative $y$-coordinate contributes a negative term, but it does not force the final coordinate to be negative. Here the signed $y$-sum is $2-8+18=12>0$, so $y_{\mathrm{cm}}=+1.00\,\mathrm m$.
```

---

<a id="compress-identical-blocks-into-groups"></a>
## Compress Identical Blocks into Groups

**Lecture-note worked example: ten identical blocks in three groups.** Six blocks are represented by mass $6m$ at $x=1.5\,\mathrm{cm}$, two by $2m$ at $x=4.0\,\mathrm{cm}$, and two by $2m$ at $x=5.5\,\mathrm{cm}$.

**Explanation**

If a group of identical uniform blocks has a known center, replace that group by its total mass at that center:

$$
m_{\text{group}}=(\text{number of blocks in the group})m.
$$

The grouped ledger is

| group | represented mass | group center | mass-position product |
|:---|---:|---:|---:|
| 1 | $6m$ | $1.5\,\mathrm{cm}$ | $9m\,\mathrm{cm}$ |
| 2 | $2m$ | $4.0\,\mathrm{cm}$ | $8m\,\mathrm{cm}$ |
| 3 | $2m$ | $5.5\,\mathrm{cm}$ | $11m\,\mathrm{cm}$ |
| **total** | **$10m$** |  | **$28m\,\mathrm{cm}$** |

Therefore,

$$
x_{\mathrm{cm}}
=\frac{6m(1.5\,\mathrm{cm})+2m(4.0\,\mathrm{cm})+2m(5.5\,\mathrm{cm})}{10m}
=\boxed{2.8\,\mathrm{cm}}.
$$

The factor $m$ cancels, but the block counts do not. The three group centers must be weighted by $6$, $2$, and $2$; averaging the three centers equally would treat the groups as if they contained the same number of blocks.

**Source-note count clarification:** The required lecture example contains $6+2+2=10$ blocks, so its denominator is $10m$. It is not the separate nine-block exercise in the prepared lecture quiz, which has different block centers and a different result.

```quiz
type: radio
id: mct-p3-grouped-blocks
shuffle: true
content: |-
  Identical blocks are compressed into three groups: $4m$ at $x=1.0\,\mathrm{cm}$, $3m$ at $x=5.0\,\mathrm{cm}$, and $m$ at $x=9.0\,\mathrm{cm}$. What is the combined center of mass?
options:
- id: mct-p3-grouped-blocks-a
  content: |-
    $3.50\,\mathrm{cm}$
  correct: true
  feedback: |-
    Each group acts as its total mass at its own center. The weighted sum is $4m(1.0)+3m(5.0)+m(9.0)=28m\,\mathrm{cm}$, and the total mass is $8m$, so $x_{\mathrm{cm}}=28m/(8m)=3.50\,\mathrm{cm}$.
- id: mct-p3-grouped-blocks-b
  content: |-
    $5.00\,\mathrm{cm}$
  feedback: |-
    This equally averages the three group centers: $(1+5+9)/3$. The groups do not have equal mass; their centers must carry weights $4$, $3$, and $1$, which shifts the result toward the four-block group at $1.0\,\mathrm{cm}$.
- id: mct-p3-grouped-blocks-c
  content: |-
    $28.0\,\mathrm{cm}$
  feedback: |-
    The value $28m\,\mathrm{cm}$ is the mass-position numerator. Divide by the full grouped mass $4m+3m+m=8m$ to obtain the position $3.50\,\mathrm{cm}$.
- id: mct-p3-grouped-blocks-d
  content: |-
    $4.00\,\mathrm{cm}$
  feedback: |-
    This divides the numerator $28m\,\mathrm{cm}$ by $7m$, omitting the one-block group from the denominator while still keeping its product in the numerator. Every represented group belongs in both the weighted sum and the total mass.
- id: mct-p3-grouped-blocks-e
  content: |-
    $2.71\,\mathrm{cm}$
  feedback: |-
    This drops the group at $9.0\,\mathrm{cm}$ entirely and computes $19m/(7m)$. The rightmost block is still part of the system; including its mass and product gives $28m/(8m)=3.50\,\mathrm{cm}$.
```

---

<a id="replace-uniform-pieces-by-masses-at-their-centers"></a>
## Replace Uniform Pieces by Masses at Their Centers

**Lecture-note worked example: two attached cubes.** A uniform cube of side $2L$ occupies $0\le x\le2L$. A cube of side $L$, made from material with the same density $\rho$, is attached on its right and occupies $2L\le x\le3L$. Find the combined center of mass.

**Explanation**

Treat each uniform cube as a point mass at its geometric center. Because both pieces have the same density, their mass ratio is their volume ratio:

$$
m_1:m_2=(2L)^3:L^3=8:1.
$$

The large cube has

$$
m_1=\rho(2L)^3=8\rho L^3,
\qquad
x_1=L.
$$

The small cube has

$$
m_2=\rho L^3,
\qquad
x_2=2L+\frac L2=\frac{5L}{2}.
$$

The small cube adds mass to the right of $x=L$, so the result must move right of $L$. The large cube is eight times as massive, so the center should remain inside it, between $L$ and $2L$. Now use the same coordinate ledger:

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{(8\rho L^3)(L)+(\rho L^3)(5L/2)}{8\rho L^3+\rho L^3}\\
&=\frac{8L+5L/2}{9}\\
&=\boxed{\frac{7L}{6}}.
\end{aligned}
$$

The density and the common factor $L^3$ cancel because both cubes have the same density. With the lecture value $L=0.75\,\mathrm m$,

$$
x_{\mathrm{cm}}=\frac76(0.75\,\mathrm m)=0.875\,\mathrm m\approx0.88\,\mathrm m.
$$

```quiz
type: radio
id: mct-p3-composite-cubes
shuffle: true
content: |-
  A uniform cube of side $3L$ occupies $0\le x\le3L$. A cube of side $L$, made from material with the same density, is attached on the right and occupies $3L\le x\le4L$. Where is the combined center of mass?
options:
- id: mct-p3-composite-cubes-a
  content: |-
    $\dfrac{11L}{7}$
  correct: true
  feedback: |-
    Equal density makes the masses proportional to volume: $m_1=27\rho L^3$ at $x_1=3L/2$, and $m_2=\rho L^3$ at $x_2=7L/2$. Thus $x_{\mathrm{cm}}=[27(3L/2)+7L/2]/28=44L/28=11L/7$, just right of the large cube's center.
- id: mct-p3-composite-cubes-b
  content: |-
    $\dfrac{5L}{2}$
  feedback: |-
    This equally averages the two cube centers, $3L/2$ and $7L/2$. Their masses are not equal: the $3L$-side cube has $3^3=27$ times the volume and mass, so the result must lie much closer to $3L/2$.
- id: mct-p3-composite-cubes-c
  content: |-
    $\dfrac{3L}{2}$
  feedback: |-
    This is the large cube's center by itself. Adding the smaller cube to its right shifts the combined center to the right, from $3L/2$ to $11L/7$.
- id: mct-p3-composite-cubes-d
  content: |-
    $2L$
  feedback: |-
    This is the geometric midpoint of the full $4L$ span, which would require a mass distribution symmetric about $2L$. Most of the mass lies in the $3L$-side cube, so the weighted center is $11L/7<2L$.
- id: mct-p3-composite-cubes-e
  content: |-
    $\dfrac{44L}{27}$
  feedback: |-
    The numerator includes both cubes, but this denominator includes only the large cube's $27\rho L^3$. The total mass is $28\rho L^3$, so the coordinate is $44L/28=11L/7$.
```

---

<a id="summary"></a>
## Summary

For discrete masses or uniform pieces with known individual centers:

1. Choose one origin and keep every coordinate signed.
2. Predict the answer region from the occupied coordinates and heavier concentration.
3. Build $m_i x_i$ and, in two dimensions, $m_i y_i$ columns.
4. Divide every product sum by the same total mass $M=\sum_i m_i$.
5. Replace a uniform piece or a group of identical objects by its total mass at its own center.
6. Reject a result outside the occupied coordinate range or on the wrong side of the heavier concentration.

The main traps are using an unweighted geometric midpoint, dropping negative coordinate signs, changing the denominator between $x$ and $y$, and averaging group centers without weighting them by group mass.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
