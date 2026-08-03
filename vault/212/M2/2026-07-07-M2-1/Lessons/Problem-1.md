# Finding the Center of Mass of Two Point Masses

<!--
lesson-id: 212-M2-001
topic-code: MTH212.M2.01
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Mass-Position Ledger](#build-the-mass-position-ledger)
- [Cancel a Common Mass Scale](#cancel-a-common-mass-scale)
- [Check the Location and Direction](#check-the-location-and-direction)
- [Apply the Method to the Two Blocks](#apply-the-method-to-the-two-blocks)
- [Summary](#summary)

## Prerequisites

- Read signed positions on the $x$-axis.
- Multiply each mass by its position.
- Add algebraic terms and simplify rational expressions.
- Convert a terminating decimal ratio to an equivalent fraction.

---

<a id="introduction"></a>
## Introduction

For point masses on the $x$-axis, the center-of-mass position is the mass-weighted average

$$
x_{\mathrm{cm}}=rac{\sum_i m_i x_i}{\sum_i m_i}.
$$

For two masses, this becomes

$$
x_{\mathrm{cm}}=rac{m_1x_1+m_2x_2}{m_1+m_2}.
$$

The numerator pairs each mass with its own position. The denominator is the total mass. When both masses are positive, the result must lie between their positions and closer to the heavier mass.

---

<a id="build-the-mass-position-ledger"></a>
## Build the Mass-Position Ledger

**Example:** Equal point masses $m$ are located at $x_1=0$ and $x_2=d$. Find their center of mass.

**Explanation**

Write one row per object before substituting:

| Object | Mass | Position | Mass-position product |
|---|---:|---:|---:|
| 1 | $m$ | $0$ | $0$ |
| 2 | $m$ | $d$ | $md$ |

Then divide the sum of the products by the total mass:

$$
x_{\mathrm{cm}}
=\frac{0+md}{m+m}
=\frac d2.
$$

The origin contributes zero to the numerator, but its mass still belongs in the denominator.

```quiz
type: radio
id: m2-1-p1-ledger
shuffle: true
content: |-
  A mass $2m$ is at $x=0$, and a mass $m$ is at $x=d$. Which expression correctly sets up the center-of-mass position?
options:
- id: a
  content: |-
    $\dfrac{(2m)(0)+m(d)}{2m+m}$
  correct: true
  feedback: |-
    Pair each mass with its own position in the numerator and divide by the total mass. The mass at the origin contributes zero above the fraction bar but still counts below it.
- id: b
  content: |-
    $\dfrac{(2m)(d)+m(0)}{2m+m}$
- id: c
  content: |-
    $\dfrac{(2m)(0)+m(d)}{m}$
- id: d
  content: |-
    $\dfrac{2m+m}{0+d}$
- id: e
  content: |-
    $\dfrac{0+d}{2}$
```

---

<a id="cancel-a-common-mass-scale"></a>
## Cancel a Common Mass Scale

**Example:** A mass $m$ is at $x=0$, and a mass $3m$ is at $x=d$. Find $x_{\mathrm{cm}}$.

**Explanation**

Substitute first, then factor out the common mass scale:

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{m(0)+(3m)d}{m+3m}\\
&=\frac{3md}{4m}\\
&=\frac34d.
\end{aligned}
$$

The common factor $m$ cancels from the complete numerator and denominator. This shows that multiplying every mass by the same positive factor does not move the center of mass.

```quiz
type: radio
id: m2-1-p1-cancel-mass
shuffle: true
content: |-
  A mass $m$ is at $x=0$, and a mass $4m$ is at $x=d$. What is the center-of-mass position?
options:
- id: a
  content: |-
    $\dfrac15d$
- id: b
  content: |-
    $\dfrac12d$
- id: c
  content: |-
    $\dfrac45d$
  correct: true
  feedback: |-
    $x_{\mathrm{cm}}=[m(0)+(4m)d]/(m+4m)=4md/(5m)=4d/5$.
- id: d
  content: |-
    $4d$
- id: e
  content: |-
    $5d$
```

---

<a id="check-the-location-and-direction"></a>
## Check the Location and Direction

**Example:** A mass $2m$ is at $x=-d$, and a mass $m$ is at $x=d$. Find and check the center of mass.

**Explanation**

Signed positions remain signed in the numerator:

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{(2m)(-d)+m(d)}{2m+m}\\
&=\frac{-md}{3m}\\
&=-\frac d3.
\end{aligned}
$$

The answer lies between $-d$ and $d$ and is on the negative side, closer to the heavier mass at $-d$. Both checks agree with the calculation.

For masses at $0$ and $d$, it is useful to write

$$
x_{\mathrm{cm}}=\frac{m_{\text{right}}}{m_{\text{left}}+m_{\text{right}}}d.
$$

The coefficient must be between $0$ and $1$. It is greater than $1/2$ exactly when the right-hand mass is heavier.

```quiz
type: radio
id: m2-1-p1-position-check
shuffle: true
content: |-
  A mass $m$ is at $x=0$, and a heavier mass $2m$ is at $x=d$. Which candidate could be the center-of-mass position?
options:
- id: a
  content: |-
    $-\dfrac23d$
- id: b
  content: |-
    $\dfrac13d$
- id: c
  content: |-
    $\dfrac23d$
  correct: true
  feedback: |-
    The center must lie between $0$ and $d$ and closer to the heavier right-hand mass. Direct calculation gives $[m(0)+(2m)d]/(3m)=2d/3$.
- id: d
  content: |-
    $d$
- id: e
  content: |-
    $\dfrac32d$
```

---

<a id="apply-the-method-to-the-two-blocks"></a>
## Apply the Method to the Two Blocks

**Example:** Find the center of mass for a block of mass $m$ at $x=0$ and a block of mass $1.8m$ at $x=d$.

**Explanation**

Substitute the masses and positions into the weighted-average formula:

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{m(0)+(1.8m)d}{m+1.8m}\\
&=\frac{1.8}{2.8}d\\
&=\frac{18}{28}d\\
&=\frac{9}{14}d.
\end{aligned}
$$

Since $9/14\approx0.643$, the result lies between $0$ and $d$ and to the right of the midpoint, as expected because the mass at $d$ is heavier.

The coefficient has a direct ratio meaning:

$$
\frac{x_{\mathrm{cm}}}{d}
=\frac{m_{\text{right}}}{m_{\text{left}}+m_{\text{right}}}
=\frac{1.8}{2.8}
=\frac{9}{14}.
$$

An independent balance check uses distances measured from the proposed center of mass:

| Block | Distance from $x_{\mathrm{cm}}=9d/14$ | Mass times distance |
|---|---:|---:|
| Left block | $9d/14$ | $m(9d/14)$ |
| Right block | $d-9d/14=5d/14$ | $1.8m(5d/14)=m(9d/14)$ |

The two mass-distance products match, so the proposed point balances the system. This check also explains why the center lies closer to the heavier right-hand block.

```quiz
type: radio
id: m2-1pre-q1
content: |-
  **Question 1**

  Block 1, with mass $m$, is at the origin. Block 2, with mass $1.8m$, is a distance $d$ to the right along the $x$-axis. Find the location of the system's center of mass on the $x$-axis. Solve symbolically and show your work.

  ![](<../Source/Images/two-point-masses-on-x-axis.png>)

  Enter the center-of-mass position using $d$ and ordinary keyboard notation:
options:
- id: a
  content: |-
    `9d/14`
  correct: true
  feedback: |-
    For two point masses on the $x$-axis,

    $$
    x_{\mathrm{cm}}=\frac{m_1x_1+m_2x_2}{m_1+m_2}.
    $$

    Here, $m_1=m$ at $x_1=0$ and $m_2=1.8m$ at $x_2=d$. Therefore,

    $$
    x_{\mathrm{cm}}
    =\frac{m(0)+(1.8m)d}{m+1.8m}
    =\frac{1.8}{2.8}d
    =\frac{9d}{14}.
    $$
- id: b
  content: |-
    `d/2`
- id: c
  content: |-
    `5d/14`
- id: d
  content: |-
    `9d/5`
- id: e
  content: |-
    `1.8d`
```

---

<a id="summary"></a>
## Summary

- Use $x_{\mathrm{cm}}=(\sum m_ix_i)/(\sum m_i)$.
- Pair each mass with its own signed position in the numerator.
- Include every mass in the denominator, even when its position is zero.
- Cancel only common factors of the complete numerator and denominator.
- Check that the answer lies between the masses and closer to the heavier one.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../../M3/2026-07-20-Q-2/Study-Guide.md)
Next: [Finding a Two-Object Center of Mass in the Plane](../../2026-07-15-HW-4/Lessons/Problem-10.md)

Study guide index: 01/20

---

<!-- lesson-nav:end -->
