# Center of Mass of Two Point Masses

<!--
lesson-id: 212-M2-002
topic-code: MTH212.M2.02
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose Coordinates From the Requested Reference Point](#choose-coordinates-from-the-requested-reference-point)
- [Form the Mass-Weighted Average](#form-the-mass-weighted-average)
- [Use a Mass Ratio and Check the Result](#use-a-mass-ratio-and-check-the-result)
- [Apply the Method to the Two Blocks](#apply-the-method-to-the-two-blocks)
- [Summary](#summary)

## Prerequisites

- Interpret position on a one-dimensional coordinate axis.
- Substitute values into an algebraic formula.
- Simplify fractions with a common factor.
- Distinguish mass units from length units.

---

<a id="introduction"></a>
## Introduction

For point masses on a line, the center-of-mass coordinate is the mass-weighted average of their positions:

$$
x_{\mathrm{cm}}
=\frac{m_1x_1+m_2x_2}{m_1+m_2}.
$$

An ordinary mean gives two positions equal influence. Center of mass gives each position influence proportional to the mass located there:

| Situation | Center coordinate |
|---|---|
| Two equal masses | $\dfrac{x_1+x_2}{2}$ |
| Two unequal masses | $\dfrac{m_1x_1+m_2x_2}{m_1+m_2}$ |

Thus, the midpoint is not a competing method; it is the equal-mass special case of the same weighted-average formula.

Use this when a problem gives separate masses and positions or a distance between the masses. First choose the origin named by the question, then assign coordinates, substitute, and simplify. The main trap is using the distance between the masses as both coordinates instead of measuring each position from the chosen origin.

---

<a id="choose-coordinates-from-the-requested-reference-point"></a>
## Choose Coordinates From the Requested Reference Point

**Example:** Two masses are separated by a distance $L$. Find their coordinates relative to the position of the left mass.

**Explanation**

“Relative to the position of the left mass” means place the origin at that mass:

$$
x_1=0.
$$

If the second mass is $L$ to the right, then

$$
x_2=L.
$$

The distance $L$ becomes the second mass's coordinate only because the origin is at the first mass. If the origin changed, both coordinates would need to be reassigned.

```quiz
type: radio
id: problem-2-coordinate-setup-q1
content: |-
  Mass $m_A$ is at the left end of a massless rod of length $0.60\ \mathrm{m}$, and mass $m_B$ is at the right end. What coordinates should be used to find the center of mass relative to the position of $m_A$?
options:
- id: a
  content: |-
    $x_A=0$ and $x_B=0.60\ \mathrm{m}$
  correct: true
  feedback: |-
    The requested reference point is the origin, and the other mass is one rod length to its right.
- id: b
  content: |-
    $x_A=0.60\ \mathrm{m}$ and $x_B=0$
  feedback: |-
    These coordinates use the position of $m_B$, not $m_A$, as the origin.
- id: c
  content: |-
    $x_A=-0.60\ \mathrm{m}$ and $x_B=0.60\ \mathrm{m}$
  feedback: |-
    This makes the masses $1.20\ \mathrm{m}$ apart instead of $0.60\ \mathrm{m}$ apart.
- id: d
  content: |-
    $x_A=0.30\ \mathrm{m}$ and $x_B=0.30\ \mathrm{m}$
  feedback: |-
    The two different masses cannot occupy the same coordinate at opposite ends of the rod.
- id: e
  content: |-
    $x_A=-0.30\ \mathrm{m}$ and $x_B=0.30\ \mathrm{m}$
  feedback: |-
    These coordinates use the rod's midpoint as the origin, not the position of $m_A$.
```

---

<a id="form-the-mass-weighted-average"></a>
## Form the Mass-Weighted Average

**Example:** Mass $m_1=2m$ is at $x_1=0$, and mass $m_2=m$ is at $x_2=L$. Find the center-of-mass coordinate.

**Explanation**

Multiply each position by the mass located there, add those products, and divide by the total mass:

| Object | Mass | Position | Mass times position |
|---|---:|---:|---:|
| 1 | $2m$ | $0$ | $0$ |
| 2 | $m$ | $L$ | $mL$ |

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{m_1x_1+m_2x_2}{m_1+m_2}\\
&=\frac{(2m)(0)+(m)(L)}{2m+m}\\
&=\frac{mL}{3m}\\
&=\frac{L}{3}.
\end{aligned}
$$

The zero coordinate removes the heavier mass's term from the numerator, but its mass remains in the denominator. That denominator is what pulls the center of mass toward $x=0$.

The units provide a quick audit:

$$
[x_{\mathrm{cm}}]
=\frac{(\mathrm{kg})(\mathrm{m})}{\mathrm{kg}}
=\mathrm{m}.
$$

If the mass units do not cancel or the result does not have length units, the weighted average was assembled incorrectly.

```quiz
type: radio
id: problem-2-weighted-average-q1
content: |-
  Mass $m_1=3m$ is at $x_1=0$, and mass $m_2=m$ is at $x_2=0.80\ \mathrm{m}$. What is the center-of-mass position?
options:
- id: a
  content: |-
    $0.20\ \mathrm{m}$
  correct: true
  feedback: |-
    $\dfrac{(3m)(0)+(m)(0.80\ \mathrm{m})}{3m+m}=0.20\ \mathrm{m}$.
- id: b
  content: |-
    $0.40\ \mathrm{m}$
  feedback: |-
    The midpoint applies only when the two masses are equal.
- id: c
  content: |-
    $0.60\ \mathrm{m}$
  feedback: |-
    This places the center closer to the lighter right mass instead of the heavier left mass.
- id: d
  content: |-
    $0.80\ \mathrm{m}$
  feedback: |-
    This is the position of the second mass, not the weighted average.
- id: e
  content: |-
    $2.40\ \mathrm{m}$
  feedback: |-
    This multiplies the distance by the mass ratio instead of dividing the weighted sum by total mass.
```

---

<a id="use-a-mass-ratio-and-check-the-result"></a>
## Use a Mass Ratio and Check the Result

**Example:** Mass $m_1=rm_2$ is at $x_1=0$, and mass $m_2$ is at $x_2=L$. Express the center of mass in terms of $r$ and $L$.

**Explanation**

Substitute the mass ratio before inserting any numerical length:

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{(rm_2)(0)+m_2L}{rm_2+m_2}\\
&=\frac{m_2L}{(r+1)m_2}\\
&=\frac{L}{r+1}.
\end{aligned}
$$

The common mass scale $m_2$ cancels. For positive masses, the answer must lie between the two positions. When $r>1$, the left mass is heavier, so the center of mass must also lie left of the midpoint:

$$
0<x_{\mathrm{cm}}<\frac{L}{2}.
$$

The special case $r=1$ gives $x_{\mathrm{cm}}=L/2$, matching the midpoint formula for equal masses. As $r$ grows, $L/(r+1)$ decreases, so the center moves toward the increasingly heavy mass at the origin.

```quiz
type: radio
id: problem-2-ratio-check-q1
content: |-
  Two masses are at $x=0$ and $x=L$. The mass at $x=L$ is four times the mass at $x=0$. Which interval must contain their center of mass?
options:
- id: a
  content: |-
    $\dfrac{L}{2}<x_{\mathrm{cm}}<L$
  correct: true
  feedback: |-
    The center lies between the masses and closer to the heavier mass at $x=L$.
- id: b
  content: |-
    $0<x_{\mathrm{cm}}<\dfrac{L}{2}$
  feedback: |-
    This would place the center closer to the lighter mass at $x=0$.
- id: c
  content: |-
    $x_{\mathrm{cm}}=\dfrac{L}{2}$
  feedback: |-
    The midpoint is correct only for equal masses.
- id: d
  content: |-
    $x_{\mathrm{cm}}>L$
  feedback: |-
    A positive-mass weighted average cannot lie beyond both masses.
- id: e
  content: |-
    $x_{\mathrm{cm}}<0$
  feedback: |-
    A positive-mass weighted average cannot lie to the left of both masses.
```

---

<a id="apply-the-method-to-the-two-blocks"></a>
## Apply the Method to the Two Blocks

**Example:** Two blocks of mass $m_1=3m_2$ are separated by a massless $0.88\ \mathrm{m}$ rod. Find their center of mass relative to the position of $m_1$.

**Explanation**

Use the position of $m_1$ as the origin:

$$
x_1=0,
\qquad
x_2=0.88\ \mathrm{m}.
$$

Then

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{m_1x_1+m_2x_2}{m_1+m_2}\\
&=\frac{(3m_2)(0)+m_2(0.88\ \mathrm{m})}{3m_2+m_2}\\
&=\frac{0.88\ \mathrm{m}}{4}\\
&=0.22\ \mathrm{m}.
\end{aligned}
$$

The result is between the masses and is closer to the heavier block at the origin.

```quiz
type: radio
id: m2-1lec-q1
content: |-
  **Question 1**

  The two blocks balance in stable equilibrium. Find their center of mass relative to the position of $m_1$, where $m_1=3m_2$. Neglect the mass of the $0.88\ \mathrm{m}$ rod.

  ![](<../Source/Images/two-mass-balance.png>)

  Enter the center-of-mass position in meters as a number only:
options:
- id: a
  content: |-
    $0.22$
  correct: true
  feedback: |-
    Place $m_1$ at $x_1=0$ and $m_2$ at $x_2=0.88\ \mathrm{m}$:

    $$
    x_{\mathrm{cm}}
    =\frac{m_1x_1+m_2x_2}{m_1+m_2}
    =\frac{(3m_2)(0)+m_2(0.88\ \mathrm{m})}{3m_2+m_2}
    =0.22\ \mathrm{m}.
    $$
- id: b
  content: |-
    $0.44$
  feedback: |-
    This is the midpoint and would be correct only if the two blocks had equal masses.
- id: c
  content: |-
    $0.66$
  feedback: |-
    This places the center closer to the lighter block instead of the heavier block $m_1$.
- id: d
  content: |-
    $0.88$
  feedback: |-
    This is the position of $m_2$, not the center of mass.
- id: e
  content: |-
    $2.64$
  feedback: |-
    This multiplies the separation by the mass ratio and places the result beyond both blocks.
```

---

<a id="summary"></a>
## Summary

For two point masses on a line:

1. Put the requested reference point at $x=0$.
2. Assign both mass coordinates from that origin.
3. Use $x_{\mathrm{cm}}=(m_1x_1+m_2x_2)/(m_1+m_2)$.
4. Substitute a mass ratio symbolically and cancel the common mass scale.
5. Check that the answer lies between the masses and closer to the heavier one.

If $m_1=rm_2$ is at $x=0$ and $m_2$ is at $x=L$, then

$$
\boxed{x_{\mathrm{cm}}=\frac{L}{r+1}}.
$$

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
