# Finding the Center of Mass of Joined Cubes

<!--
lesson-id: 212-M2-004
topic-code: MTH212.M2.04
-->

## Table of Contents

- [Introduction](#introduction)
- [Turn Volume Into Mass Weight](#turn-volume-into-mass-weight)
- [Locate Each Cube's Center](#locate-each-cubes-center)
- [Build and Simplify the Weighted Average](#build-and-simplify-the-weighted-average)
- [Check and Round the Result](#check-and-round-the-result)
- [Apply the Method to the Composite Cubes](#apply-the-method-to-the-composite-cubes)
- [Summary](#summary)

## Prerequisites

- Use the cube-volume formula $V=s^3$.
- Use $m=\rho V$ for an object of constant density.
- Locate a cube's geometric center halfway along each dimension.
- Compute and simplify a mass-weighted average.
- Round a final measured result to the appropriate significant figures.

---

<a id="introduction"></a>
## Introduction

To find the center of mass of a composite object made from uniform pieces, replace each piece by a point mass located at that piece's geometric center. Then use

$$
x_{\mathrm{cm}}=\frac{\sum_i m_ix_i}{\sum_i m_i}.
$$

For constant-density cubes, each mass comes from

$$
m_i=\rho V_i=\rho s_i^3.
$$

The key is to build a consistent ledger of each piece's mass and center position relative to the same origin before substituting into the weighted average.

---

<a id="turn-volume-into-mass-weight"></a>
## Turn Volume Into Mass Weight

**Example:** Two solid cubes have the same density $\rho$. One has side length $2L$, and the other has side length $L$. Compare their masses.

**Explanation**

Cube volume depends on the third power of side length:

$$
V=s^3.
$$

Therefore,

$$
m_{\text{large}}=\rho(2L)^3=8\rho L^3,
\qquad
m_{\text{small}}=\rho L^3.
$$

The large cube is eight times as massive, not twice as massive. The side-length scale factor must be cubed.

```quiz
type: radio
id: m2-1-p4-volume-weight
shuffle: true
content: |-
  Two solid cubes have the same constant density. Cube A has side length $3L$, and Cube B has side length $L$. What is the mass ratio $m_A:m_B$?
options:
- id: a
  content: |-
    $3:1$
- id: b
  content: |-
    $6:1$
- id: c
  content: |-
    $9:1$
- id: d
  content: |-
    $27:1$
  correct: true
  feedback: |-
    Equal density makes the mass ratio equal the volume ratio: $(3L)^3:L^3=27:1$.
- id: e
  content: |-
    $81:1$
```

---

<a id="locate-each-cubes-center"></a>
## Locate Each Cube's Center

**Example:** A cube of side $2L$ extends from $x=0$ to $x=2L$. A cube of side $L$ is attached immediately to its right, extending from $x=2L$ to $x=3L$. Find each center position.

**Explanation**

Each center is halfway between that cube's left and right faces:

$$
x_1=\frac{0+2L}{2}=L,
$$

and

$$
x_2=\frac{2L+3L}{2}=\frac{5L}{2}.
$$

Equivalently, start at the small cube's left face and move half its side length:

$$
x_2=2L+\frac L2=\frac{5L}{2}.
$$

The position $L/2$ is the small cube's center measured from its own left face, not from the system's origin.

```quiz
type: radio
id: m2-1-p4-center-position
shuffle: true
content: |-
  The origin is at the left face of a cube of side $3L$. A second cube of side $L$ is attached immediately to its right. What is the second cube's center position?
options:
- id: a
  content: |-
    $\dfrac L2$
- id: b
  content: |-
    $3L$
- id: c
  content: |-
    $\dfrac{7L}{2}$
  correct: true
  feedback: |-
    The second cube begins at $x=3L$. Its center is another $L/2$ to the right, so $x=3L+L/2=7L/2$.
- id: d
  content: |-
    $4L$
- id: e
  content: |-
    $\dfrac{3L}{2}$
```

---

<a id="build-and-simplify-the-weighted-average"></a>
## Build and Simplify the Weighted Average

**Example:** Use the masses and positions of the adjacent $2L$ and $L$ cubes to find the composite center of mass symbolically.

**Explanation**

Organize the inputs before calculating:

| Piece | Mass | Center position |
|---|---:|---:|
| Large cube | $8\rho L^3$ | $L$ |
| Small cube | $\rho L^3$ | $5L/2$ |

Then

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{(8\rho L^3)L+(\rho L^3)(5L/2)}{8\rho L^3+\rho L^3}\\
&=\frac{\rho L^4(8+5/2)}{9\rho L^3}\\
&=\frac{21/2}{9}L\\
&=\frac76L.
\end{aligned}
$$

The common density and common power $L^3$ cancel only after the complete numerator and denominator are assembled. Their cancellation shows that the numerical density is irrelevant when both cubes have the same density.

```quiz
type: radio
id: m2-1-p4-weighted-average
shuffle: true
content: |-
  Two uniform pieces have masses $8M$ and $M$, with center positions $a$ and $4a$, respectively. What is their combined center position?
options:
- id: a
  content: |-
    $\dfrac{4a}{9}$
- id: b
  content: |-
    $\dfrac{8a}{9}$
- id: c
  content: |-
    $\dfrac{4a}{3}$
  correct: true
  feedback: |-
    $x_{\mathrm{cm}}=[(8M)a+M(4a)]/(9M)=12Ma/(9M)=4a/3$.
- id: d
  content: |-
    $\dfrac{5a}{2}$
- id: e
  content: |-
    $4a$
```

---

<a id="check-and-round-the-result"></a>
## Check and Round the Result

**Example:** Evaluate $x_{\mathrm{cm}}=7L/6$ for $L=0.75\ \mathrm{m}$ and report the result to two significant figures.

**Explanation**

Keep the exact expression until the final substitution:

$$
x_{\mathrm{cm}}
=\frac76(0.75\ \mathrm{m})
=0.875\ \mathrm{m}.
$$

The length $0.75\ \mathrm{m}$ has two significant figures, so the reported result is

$$
x_{\mathrm{cm}}=0.88\ \mathrm{m}.
$$

The result must lie between the component centers, $0.75\ \mathrm{m}$ and $1.875\ \mathrm{m}$. It should also be much closer to the large cube's center because that cube is eight times as massive. The value $0.875\ \mathrm{m}$ passes both checks.

```quiz
type: radio
id: m2-1-p4-round-check
shuffle: true
content: |-
  A symbolic calculation gives $x_{\mathrm{cm}}=5L/4$. If $L=0.62\ \mathrm{m}$ is measured to two significant figures, what value should be reported?
options:
- id: a
  content: |-
    $0.77\ \mathrm{m}$
- id: b
  content: |-
    $0.78\ \mathrm{m}$
  correct: true
  feedback: |-
    $(5/4)(0.62\ \mathrm{m})=0.775\ \mathrm{m}$, which rounds to $0.78\ \mathrm{m}$ at two significant figures.
- id: c
  content: |-
    $0.775\ \mathrm{m}$
- id: d
  content: |-
    $1.3\ \mathrm{m}$
- id: e
  content: |-
    $2.5\ \mathrm{m}$
```

---

<a id="apply-the-method-to-the-composite-cubes"></a>
## Apply the Method to the Composite Cubes

**Example:** Use the diagram's shared origin, the cube volumes, and the weighted-average formula to calculate the requested position.

**Explanation**

The large cube has side $2L$, so its mass is $8\rho L^3$ and its center is at $x=L$. The small cube has side $L$, so its mass is $\rho L^3$ and its center is at $x=2L+L/2=5L/2$. Thus,

$$
x_{\mathrm{cm}}=\frac76L
=\frac76(0.75\ \mathrm{m})
=0.875\ \mathrm{m}
\approx0.88\ \mathrm{m}.
$$

Verify the symbolic result by balancing mass times distance about $x_{\mathrm{cm}}=7L/6$:

| Cube | Distance from $7L/6$ | Mass times distance |
|---|---:|---:|
| Large, centered at $L$ | $7L/6-L=L/6$ | $(8\rho L^3)(L/6)=\frac43\rho L^4$ |
| Small, centered at $5L/2$ | $5L/2-7L/6=4L/3$ | $(\rho L^3)(4L/3)=\frac43\rho L^4$ |

The products match, confirming that the heavier cube's shorter balance arm offsets the lighter cube's longer balance arm.

```quiz
type: radio
id: m2-1lec-q3
content: |-
  **Question 3**

  The cubic blocks shown have constant density $\rho$. Find the center of mass $x_{\mathrm{cm}}$ relative to the origin at the left edge of the large block. Use $\rho=1.5\ \mathrm{kg/m^3}$ and $L=0.75\ \mathrm{m}$, and enter your answer in meters.

  ![](<../Source/Images/composite-cubes.png>)

  Enter the center-of-mass position in meters as a number only:
options:
- id: a
  content: |-
    `0.88`
  correct: true
  feedback: |-
    The large cube has mass $m_1=\rho(2L)^3=8\rho L^3$ and center $x_1=L$. The small cube has mass $m_2=\rho L^3$ and center $x_2=2L+L/2=5L/2$. Therefore,

    $$
    x_{\mathrm{cm}}
    =\frac{m_1x_1+m_2x_2}{m_1+m_2}
    =\frac{(8\rho L^3)L+(\rho L^3)(5L/2)}{9\rho L^3}
    =\frac{7L}{6}.
    $$

    With $L=0.75\ \mathrm{m}$,

    $$
    x_{\mathrm{cm}}=\frac76(0.75\ \mathrm{m})=0.875\ \mathrm{m}.
    $$

    The measured length has two significant figures, so $x_{\mathrm{cm}}=0.88\ \mathrm{m}$.
- id: b
  content: |-
    `0.875`
- id: c
  content: |-
    `0.75`
- id: d
  content: |-
    `1.31`
- id: e
  content: |-
    `1.88`
```

---

<a id="summary"></a>
## Summary

- Replace each uniform cube by a point mass at its geometric center.
- Use $m=\rho s^3$; a side-length scale factor becomes a cubed mass factor.
- Measure every component center from the same origin.
- Assemble $x_{\mathrm{cm}}=(\sum m_ix_i)/(\sum m_i)$ before canceling common factors.
- Keep the symbolic result exact, check that it lies between the component centers and closer to the heavier piece, then round once at the end.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
