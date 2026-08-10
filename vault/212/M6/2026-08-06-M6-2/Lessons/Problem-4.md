# Finding Screen Distance from a Single-Slit Diffraction Graph

<!--
lesson-id: 212-M6-009
topic-code: MTH212.M6.09
-->
## Table of Contents

- [Introduction](#introduction)
- [Measure the First-Minimum Distance](#measure-the-first-minimum-distance)
- [Isolate the Screen Distance](#isolate-the-screen-distance)
- [Calculate in One Unit System](#calculate-in-one-unit-system)
- [Use the Central Width Correctly](#use-the-central-width-correctly)
- [Summary](#summary)

## Prerequisites

- Reading horizontal coordinates from a graph
- Subtracting two positions to find a distance
- Converting nanometers, millimeters, and centimeters to meters
- Rearranging a one-step formula

---

<a id="introduction"></a>
## Introduction

For a single slit of width $a$, the dark minima satisfy

$$
a\sin\theta_m=m\lambda,
$$

where $m=1,2,3,\ldots$. For a distant screen and small diffraction angles, $y_m\approx L\sin\theta_m$, so

$$
y_m\approx\frac{m\lambda L}{a}.
$$

For the first minimum, $m=1$:

$$
y_1\approx\frac{\lambda L}{a}
\qquad\Longrightarrow\qquad
\boxed{L\approx\frac{ay_1}{\lambda}}.
$$

The recognition cue is an intensity-versus-position graph with a broad central peak and zero-intensity points on either side. Read the graph in this order:

- The broad central peak locates the pattern center $x_c$.
- The neighboring points where the curve reaches zero intensity locate the first minima $x_{\min}$.
- The horizontal axis supplies the positions and units used in $y_1=|x_{\min}-x_c|$.

The vertical intensity values identify the minima, but their numerical heights do not enter the calculation of $L$. The graph may place the peak at a nonzero coordinate. Therefore, $y_1$ is the **horizontal distance from the center of the central maximum to either adjacent minimum**, not the coordinate of the minimum itself.

This approximation is appropriate when $y_1\ll L$. Problem 4 gives $\lambda=633\ \mathrm{nm}$ and $a=0.15\ \mathrm{mm}$, asks for $L$ in meters, and supplies the first-minimum distance through the graph.

---

<a id="measure-the-first-minimum-distance"></a>
## Measure the First-Minimum Distance

**Example:** A diffraction graph has its central peak at $x_c=5.0\ \mathrm{cm}$ and its neighboring minima at $x=2.0\ \mathrm{cm}$ and $x=8.0\ \mathrm{cm}$. Find $y_1$.

**Explanation**

Coordinates locate points relative to the graph's origin. The diffraction formula needs the distance relative to the center of the pattern:

$$
y_1=|x_{\min}-x_c|.
$$

Using either neighboring minimum gives

$$
y_1=|2.0-5.0|\ \mathrm{cm}=3.0\ \mathrm{cm}
$$

or

$$
y_1=|8.0-5.0|\ \mathrm{cm}=3.0\ \mathrm{cm}.
$$

The matching distances on the two sides are also a useful reading check.

```quiz
type: radio
id: m6-2-p4-read-distance
content: |-
  A single-slit graph has its central peak at $x_c=8.0\ \mathrm{cm}$ and adjacent minima at $x=3.5\ \mathrm{cm}$ and $x=12.5\ \mathrm{cm}$. What value is $y_1$?
options:
- id: m6-2-p4-read-distance-a
  content: |-
    $4.5\ \mathrm{cm}$
  correct: true
  feedback: |-
    The first-minimum distance is measured from the pattern's center to either adjacent minimum. Here $y_1=|3.5-8.0|=|12.5-8.0|=4.5\ \mathrm{cm}$.
- id: m6-2-p4-read-distance-b
  content: |-
    $8.0\ \mathrm{cm}$
  feedback: |-
    $8.0\ \mathrm{cm}$ is the central peak's coordinate relative to the graph origin, not the peak-to-minimum distance. Subtract the center coordinate from a minimum coordinate to get $y_1=4.5\ \mathrm{cm}$.
- id: m6-2-p4-read-distance-c
  content: |-
    $12.5\ \mathrm{cm}$
  feedback: |-
    $12.5\ \mathrm{cm}$ locates the right minimum relative to the graph origin. The diffraction formula uses its displacement from the peak at $8.0\ \mathrm{cm}$, so $y_1=12.5-8.0=4.5\ \mathrm{cm}$.
- id: m6-2-p4-read-distance-d
  content: |-
    $9.0\ \mathrm{cm}$
  feedback: |-
    The distance between the two minima is $12.5-3.5=9.0\ \mathrm{cm}$, but that is the full central-maximum width $2y_1$. Divide it by $2$ to obtain the one-sided distance $y_1=4.5\ \mathrm{cm}$.
- id: m6-2-p4-read-distance-e
  content: |-
    $16.0\ \mathrm{cm}$
  feedback: |-
    Adding the minimum coordinates does not measure any width in the pattern. Distances come from coordinate differences; the peak-to-minimum difference is $4.5\ \mathrm{cm}$.
```

---

<a id="isolate-the-screen-distance"></a>
## Isolate the Screen Distance

**Example:** Rearrange $y_1=\lambda L/a$ to solve for $L$.

**Explanation**

Treat $a$, $y_1$, and $\lambda$ as known quantities and $L$ as the target. Multiply both sides by $a$, then divide by $\lambda$:

$$
ay_1=\lambda L
\qquad\Longrightarrow\qquad
L=\frac{ay_1}{\lambda}.
$$

This form gives two quick reasonableness checks. With $a$ and $\lambda$ fixed, a larger $y_1$ requires a larger screen distance. With $a$ and $y_1$ fixed, a longer wavelength requires a shorter screen distance.

```quiz
type: radio
id: m6-2-p4-isolate-l
content: |-
  The first-minimum relation is $y_1=\lambda L/a$. Which expression correctly isolates the screen distance $L$?
options:
- id: m6-2-p4-isolate-l-a
  content: |-
    $\dfrac{ay_1}{\lambda}$
  correct: true
  feedback: |-
    Multiplying $y_1=\lambda L/a$ by $a$ gives $ay_1=\lambda L$. Dividing by $\lambda$ then gives $L=ay_1/\lambda$.
- id: m6-2-p4-isolate-l-b
  content: |-
    $\dfrac{\lambda y_1}{a}$
  feedback: |-
    This keeps the factors in the same arrangement as the formula for $y_1$ instead of undoing them. After $ay_1=\lambda L$, divide by $\lambda$, not by $a$, to get $L=ay_1/\lambda$.
- id: m6-2-p4-isolate-l-c
  content: |-
    $\dfrac{\lambda a}{y_1}$
  feedback: |-
    This would make $L$ decrease when the measured fringe distance $y_1$ increases, contrary to $y_1\propto L$. Isolating $L$ gives $L=ay_1/\lambda$.
- id: m6-2-p4-isolate-l-d
  content: |-
    $\dfrac{\lambda}{ay_1}$
  feedback: |-
    Taking the reciprocal of every factor is not an algebraic isolation step. The product $ay_1$ equals $\lambda L$, so dividing that product by $\lambda$ gives $L$.
- id: m6-2-p4-isolate-l-e
  content: |-
    $\dfrac{y_1}{a\lambda}$
  feedback: |-
    The slit width multiplies $y_1$ after clearing the original denominator; it does not remain in the denominator. From $ay_1=\lambda L$, the result is $L=ay_1/\lambda$.
```

---

<a id="calculate-in-one-unit-system"></a>
## Calculate in One Unit System

**Example:** A $500\ \mathrm{nm}$ laser illuminates a $0.20\ \mathrm{mm}$ slit. The first minimum is $1.5\ \mathrm{cm}$ from the central peak. Find $L$.

**Explanation**

Convert every length to meters before substituting. Orient each conversion factor so the starting unit cancels:

$$
\begin{aligned}
\lambda
&=500\ \mathrm{nm}
\left(\frac{1\ \mathrm{m}}{10^9\ \mathrm{nm}}\right)
=5.00\times10^{-7}\ \mathrm{m},\\
a
&=0.20\ \mathrm{mm}
\left(\frac{1\ \mathrm{m}}{10^3\ \mathrm{mm}}\right)
=2.0\times10^{-4}\ \mathrm{m},\\
y_1
&=1.5\ \mathrm{cm}
\left(\frac{1\ \mathrm{m}}{100\ \mathrm{cm}}\right)
=1.5\times10^{-2}\ \mathrm{m}.
\end{aligned}
$$

If a starting unit does not cancel, the conversion factor is upside down.

Then

$$
L
\approx\frac{ay_1}{\lambda}
=\frac{(2.0\times10^{-4}\ \mathrm{m})(1.5\times10^{-2}\ \mathrm{m})}{5.00\times10^{-7}\ \mathrm{m}}
=6.0\ \mathrm{m}.
$$

The units reduce to meters, as required:

$$
[L]=\frac{(\mathrm{m})(\mathrm{m})}{\mathrm{m}}=\mathrm{m}.
$$

```quiz
type: radio
id: m6-2-p4-calculate
content: |-
  A $600\ \mathrm{nm}$ laser illuminates a $0.18\ \mathrm{mm}$ slit. The first minimum is $2.0\ \mathrm{cm}$ from the central peak. Using the small-angle relation, what is the screen distance?
options:
- id: m6-2-p4-calculate-a
  content: |-
    $6.0\ \mathrm{m}$
  correct: true
  feedback: |-
    Use $L=ay_1/\lambda$ with one unit system: $a=1.8\times10^{-4}\ \mathrm{m}$, $y_1=2.0\times10^{-2}\ \mathrm{m}$, and $\lambda=6.00\times10^{-7}\ \mathrm{m}$. Their substitution gives $L=6.0\ \mathrm{m}$.
- id: m6-2-p4-calculate-b
  content: |-
    $0.0060\ \mathrm{m}$
  feedback: |-
    This is too small by $10^3$, consistent with treating $0.18\ \mathrm{mm}$ as $1.8\times10^{-7}\ \mathrm{m}$. Since $1\ \mathrm{mm}=10^{-3}\ \mathrm{m}$, the slit width is $1.8\times10^{-4}\ \mathrm{m}$ and $L=6.0\ \mathrm{m}$.
- id: m6-2-p4-calculate-c
  content: |-
    $60\ \mathrm{m}$
  feedback: |-
    This is too large by a factor of $10$, consistent with converting $2.0\ \mathrm{cm}$ to $0.20\ \mathrm{m}$. A centimeter is $10^{-2}\ \mathrm{m}$, so $2.0\ \mathrm{cm}=0.020\ \mathrm{m}$ and $L=6.0\ \mathrm{m}$.
- id: m6-2-p4-calculate-d
  content: |-
    $6000\ \mathrm{m}$
  feedback: |-
    This is too large by $10^3$, consistent with treating millimeters as meters before substitution. Convert $0.18\ \mathrm{mm}$ to $1.8\times10^{-4}\ \mathrm{m}$; then $L=6.0\ \mathrm{m}$.
- id: m6-2-p4-calculate-e
  content: |-
    $6.7\times10^{-5}\ \mathrm{m}$
  feedback: |-
    This results from using $L=\lambda y_1/a$, which swaps the roles of slit width and wavelength. Isolating the first-minimum relation gives $L=ay_1/\lambda$, so the correct screen distance is $6.0\ \mathrm{m}$.
```

---

<a id="use-the-central-width-correctly"></a>
## Use the Central Width Correctly

**Example:** Apply the procedure to the graph in Problem 4.

![](<../Source/Images/single-slit-intensity-position-graph.png>)

**Explanation**

The central maximum is centered at $x_c=6.0\ \mathrm{cm}$. Its adjacent minima occur at $x=4.0\ \mathrm{cm}$ and $x=8.0\ \mathrm{cm}$, so

$$
y_1=|4.0-6.0|\ \mathrm{cm}=|8.0-6.0|\ \mathrm{cm}=2.0\ \mathrm{cm}.
$$

Equivalently, the central maximum is $8.0-4.0=4.0\ \mathrm{cm}$ wide, and $y_1$ is half that width. Convert the given quantities:

$$
y_1=2.0\times10^{-2}\ \mathrm{m},
\qquad
a=0.15\ \mathrm{mm}=1.5\times10^{-4}\ \mathrm{m},
\qquad
\lambda=633\ \mathrm{nm}=633\times10^{-9}\ \mathrm{m}.
$$

Therefore,

$$
L
\approx\frac{ay_1}{\lambda}
=\frac{(1.5\times10^{-4}\ \mathrm{m})(2.0\times10^{-2}\ \mathrm{m})}{633\times10^{-9}\ \mathrm{m}}
=4.739\ldots\ \mathrm{m}.
$$

The graph readings and slit width support two significant figures, so the requested number-only response is

$$
\boxed{4.7}
$$

for a screen distance of $4.7\ \mathrm{m}$.

As a final condition check,

$$
\frac{y_1}{L}\approx\frac{0.020}{4.7}\approx0.0043\ll1,
$$

so the small-angle approximation is self-consistent.

```quiz
type: radio
id: m6-2-p4-central-width
content: |-
  A $500\ \mathrm{nm}$ laser illuminates a $0.10\ \mathrm{mm}$ slit. A graph shows that the central maximum is $4.0\ \mathrm{cm}$ wide from its left first minimum to its right first minimum. What is the screen distance?
options:
- id: m6-2-p4-central-width-a
  content: |-
    $4.0\ \mathrm{m}$
  correct: true
  feedback: |-
    The full central width is $2y_1$, so $y_1=2.0\ \mathrm{cm}=2.0\times10^{-2}\ \mathrm{m}$. With $a=1.0\times10^{-4}\ \mathrm{m}$ and $\lambda=5.00\times10^{-7}\ \mathrm{m}$, $L=ay_1/\lambda=4.0\ \mathrm{m}$.
- id: m6-2-p4-central-width-b
  content: |-
    $8.0\ \mathrm{m}$
  feedback: |-
    This uses the full $4.0\ \mathrm{cm}$ central width as $y_1$. The formula needs the one-sided center-to-minimum distance, which is half the central width, so $y_1=2.0\ \mathrm{cm}$ and $L=4.0\ \mathrm{m}$.
- id: m6-2-p4-central-width-c
  content: |-
    $2.0\ \mathrm{m}$
  feedback: |-
    This halves the one-sided distance a second time. The $4.0\ \mathrm{cm}$ full width should be divided by $2$ exactly once, giving $y_1=2.0\ \mathrm{cm}$ and $L=4.0\ \mathrm{m}$.
- id: m6-2-p4-central-width-d
  content: |-
    $0.040\ \mathrm{m}$
  feedback: |-
    This loses a factor of $100$ by mixing centimeters with meters. Convert $y_1=2.0\ \mathrm{cm}$ to $2.0\times10^{-2}\ \mathrm{m}$ before using $L=ay_1/\lambda$, which gives $4.0\ \mathrm{m}$.
- id: m6-2-p4-central-width-e
  content: |-
    $40\ \mathrm{m}$
  feedback: |-
    This is too large by a factor of $10$, consistent with reading $2.0\ \mathrm{cm}$ as $0.20\ \mathrm{m}$. The correct conversion is $0.020\ \mathrm{m}$, leading to $L=4.0\ \mathrm{m}$.
```

---

## Summary

When a single-slit intensity graph is used to find the screen distance, use **read $\rightarrow$ measure $\rightarrow$ convert $\rightarrow$ calculate $\rightarrow$ check**:

1. Locate the center $x_c$ of the broad central maximum.
2. Locate either adjacent zero-intensity minimum $x_{\min}$.
3. Compute the one-sided distance $y_1=|x_{\min}-x_c|$. If the full central width is given, use $y_1=W_{\text{central}}/2$.
4. Convert $a$, $y_1$, and $\lambda$ to one unit system.
5. Calculate $L\approx ay_1/\lambda$, confirm $y_1/L\ll1$, and report the requested precision and units.

The main trap is confusing a coordinate or the full central width with $y_1$. The formula uses the distance from the central peak to **one** neighboring minimum.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
