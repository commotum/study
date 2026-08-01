# Finding the Center of Mass of Identical Blocks

## Table of Contents

- [Introduction](#introduction)
- [Locate Each Block Center](#locate-each-block-center)
- [Average Equal-Mass Coordinates](#average-equal-mass-coordinates)
- [Count Stacked Blocks as Repeated Coordinates](#count-stacked-blocks-as-repeated-coordinates)
- [Apply the Method to the Block Arrangement](#apply-the-method-to-the-block-arrangement)
- [Summary](#summary)

## Prerequisites

- Find the midpoint of an interval.
- Compute the arithmetic mean of a list.
- Read horizontal positions from a coordinate diagram.

---

<a id="introduction"></a>
## Introduction

For discrete objects, the horizontal center-of-mass coordinate is

$$
x_{\mathrm{cm}}=\frac{\sum_i m_i x_i}{\sum_i m_i},
$$

where $x_i$ is the $x$-coordinate of object $i$'s own center of mass. If all $N$ objects have the same mass $M$, the common mass cancels:

$$
x_{\mathrm{cm}}
=\frac{M(x_1+x_2+\cdots+x_N)}{NM}
=\frac{x_1+x_2+\cdots+x_N}{N}.
$$

Thus, equal mass plays the same role as equal weight in an arithmetic mean. If several blocks share a horizontal position $x_j$, a frequency $f_j$ can replace repeated entries:

$$
x_{\mathrm{cm}}=\frac{\sum_j f_jx_j}{\sum_j f_j}.
$$

**Recognition cue:** When identical uniform blocks are arranged on a coordinate grid, list the center coordinate of every block and take the ordinary mean. A stacked block is another mass and must appear again in the list.

---

<a id="locate-each-block-center"></a>
## Locate Each Block Center

**Example:** A uniform block extends horizontally from $x=2.0\ \mathrm{cm}$ to $x=3.0\ \mathrm{cm}$. Find the $x$-coordinate of its center.

**Explanation**

The center lies at the midpoint of the left and right edges:

$$
x_{\text{center}}
=\frac{x_{\text{left}}+x_{\text{right}}}{2}
=\frac{2.0+3.0}{2}
=2.5\ \mathrm{cm}.
$$

Use the block's center, not its left edge, right edge, or label position.

Only horizontal edges are needed for $x_{\mathrm{cm}}$. The vertical coordinate can be ignored unless the problem also asks for $y_{\mathrm{cm}}$.

```quiz
type: radio
id: p3-block-center
content: |-
  A uniform block extends horizontally from $x=4.0\ \mathrm{cm}$ to $x=5.0\ \mathrm{cm}$. What is the $x$-coordinate of its center?
options:
- id: p3-block-center-a
  content: |-
    $4.0\ \mathrm{cm}$
- id: p3-block-center-b
  content: |-
    $4.5\ \mathrm{cm}$
  correct: true
- id: p3-block-center-c
  content: |-
    $5.0\ \mathrm{cm}$
- id: p3-block-center-d
  content: |-
    $9.0\ \mathrm{cm}$
```

---

<a id="average-equal-mass-coordinates"></a>
## Average Equal-Mass Coordinates

**Example:** Four identical blocks have center coordinates $0.5$, $1.5$, $2.5$, and $4.5\ \mathrm{cm}$. Find $x_{\mathrm{cm}}$.

**Explanation**

Because the blocks have equal mass, add the four center coordinates and divide by four:

$$
x_{\mathrm{cm}}
=\frac{0.5+1.5+2.5+4.5}{4}\ \mathrm{cm}
=\frac{9.0}{4}\ \mathrm{cm}
=2.25\ \mathrm{cm}.
$$

The denominator is the number of blocks, not the number of occupied columns.

```quiz
type: radio
id: p3-equal-mass-mean
content: |-
  Four identical blocks have center coordinates $1.0$, $2.0$, $3.0$, and $6.0\ \mathrm{cm}$. What is their horizontal center of mass?
options:
- id: p3-equal-mass-mean-a
  content: |-
    $2.0\ \mathrm{cm}$
- id: p3-equal-mass-mean-b
  content: |-
    $2.5\ \mathrm{cm}$
  correct: true
- id: p3-equal-mass-mean-c
  content: |-
    $3.0\ \mathrm{cm}$
- id: p3-equal-mass-mean-d
  content: |-
    $12\ \mathrm{cm}$
```

---

<a id="count-stacked-blocks-as-repeated-coordinates"></a>
## Count Stacked Blocks as Repeated Coordinates

**Example:** Three identical blocks lie side by side with centers at $0.5$, $1.5$, and $2.5\ \mathrm{cm}$. A fourth identical block is stacked directly above the block centered at $2.5\ \mathrm{cm}$. Find $x_{\mathrm{cm}}$.

**Explanation**

The upper block has the same $x$-coordinate as the block below it, but it is a separate mass. The coordinate list is

$$
0.5,\ 1.5,\ 2.5,\ 2.5.
$$

Thus,

$$
x_{\mathrm{cm}}
=\frac{0.5+1.5+2.5+2.5}{4}\ \mathrm{cm}
=1.75\ \mathrm{cm}.
$$

The height of the stacked block affects $y_{\mathrm{cm}}$, but it does not change that block's $x$-coordinate.

Equivalently, group the repeated location with a frequency:

$$
x_{\mathrm{cm}}
=\frac{1(0.5)+1(1.5)+2(2.5)}{1+1+2}\ \mathrm{cm}
=1.75\ \mathrm{cm}.
$$

```quiz
type: radio
id: p3-stacked-coordinate
content: |-
  Three identical blocks have centers at $1.0$, $3.0$, and $5.0\ \mathrm{cm}$. A fourth identical block is stacked directly above the block at $5.0\ \mathrm{cm}$. What is $x_{\mathrm{cm}}$?
options:
- id: p3-stacked-coordinate-a
  content: |-
    $3.0\ \mathrm{cm}$
- id: p3-stacked-coordinate-b
  content: |-
    $3.5\ \mathrm{cm}$
  correct: true
- id: p3-stacked-coordinate-c
  content: |-
    $4.0\ \mathrm{cm}$
- id: p3-stacked-coordinate-d
  content: |-
    $5.0\ \mathrm{cm}$
```

---

<a id="apply-the-method-to-the-block-arrangement"></a>
## Apply the Method to the Block Arrangement

**Source problem**

The blocks in the diagram are identical, have uniform density, and each have mass $M$. Find the $x$-coordinate of the system's center of mass relative to the origin. Enter your answer in centimeters.

![](<../Source/Images/identical-block-arrangement.png>)

Enter the $x$-coordinate in centimeters as a number only.

**Explanation**

The six bottom blocks have center coordinates

$$
0.5,\ 1.5,\ 2.5,\ 3.5,\ 4.5,\ 5.5\ \mathrm{cm}.
$$

The three upper blocks have center coordinates

$$
1.5,\ 2.5,\ 5.5\ \mathrm{cm}.
$$

A frequency table makes both the repetitions and the total block count explicit:

| Center position $x_j$ (cm) | $0.5$ | $1.5$ | $2.5$ | $3.5$ | $4.5$ | $5.5$ |
|---|---:|---:|---:|---:|---:|---:|
| Number of blocks $f_j$ | $1$ | $2$ | $2$ | $1$ | $1$ | $2$ |
| Contribution $f_jx_j$ (cm) | $0.5$ | $3.0$ | $5.0$ | $3.5$ | $4.5$ | $11.0$ |

The frequencies sum to $9$, and the contributions sum to $27.5\ \mathrm{cm}$.

There are nine equal masses, so

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{0.5+1.5+2.5+3.5+4.5+5.5+1.5+2.5+5.5}{9}\ \mathrm{cm}\\
&=\frac{27.5}{9}\ \mathrm{cm}\\
&=3.0555\ldots\ \mathrm{cm}.
\end{aligned}
$$

This passes a quick range check: a mean must lie between the smallest and largest entries, and

$$
0.5<3.0555\ldots<5.5.
$$

Rounded to the hundredths place, the number-only answer is

$$
\boxed{3.06}.
$$

```quiz
type: radio
id: p3-source-check
content: |-
  Which number should be entered for the source problem?
options:
- id: p3-source-check-a
  content: |-
    $2.56$
- id: p3-source-check-b
  content: |-
    $3.00$
- id: p3-source-check-c
  content: |-
    $3.06$
  correct: true
- id: p3-source-check-d
  content: |-
    $4.58$
```

---

<a id="summary"></a>
## Summary

For identical uniform blocks:

1. Locate the center of every block using the midpoint of its horizontal edges.
2. Record one $x$-coordinate for each block, including stacked blocks.
3. Add the coordinates and divide by the total number of blocks, or use $\sum f_jx_j/\sum f_j$ to group repeated positions.
4. Ignore vertical placement when only $x_{\mathrm{cm}}$ is requested.

The main traps are averaging block edges instead of centers, counting occupied columns instead of blocks, or omitting stacked blocks from the denominator and sum. The result should lie between the leftmost and rightmost block centers.
