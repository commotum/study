# Finding the Period of a Uniform Rod About an Offset Pivot

## Table of Contents

- [Introduction](#introduction)
- [Find the Pivot-to-Center-of-Mass Distance](#find-the-pivot-to-center-of-mass-distance)
- [Shift the Moment of Inertia to the Pivot](#shift-the-moment-of-inertia-to-the-pivot)
- [Build and Simplify the Period Formula](#build-and-simplify-the-period-formula)
- [Evaluate the Period and Check the Units](#evaluate-the-period-and-check-the-units)
- [Apply the Procedure to the Offset-Pivot Rod](#apply-the-procedure-to-the-offset-pivot-rod)
- [Summary](#summary)

## Prerequisites

- Locate the center of mass of a uniform rod at its midpoint.
- Subtract fractions using a common denominator.
- Use the parallel-axis theorem $I_p=I_{\mathrm{cm}}+md^2$.
- Use the small-angle physical-pendulum formula $T=2\pi\sqrt{I_p/(mgd)}$.

---

<a id="introduction"></a>
## Introduction

A uniform rod pivoted away from its center is a **physical pendulum**. For small oscillations, its period is

$$
T=2\pi\sqrt{\frac{I_p}{mgd}},
$$

where

- $I_p$ is the rod's moment of inertia about the pivot,
- $m$ is the rod's mass,
- $g$ is gravitational acceleration, and
- $d$ is the distance from the pivot to the rod's center of mass.

When the diagram gives the pivot position rather than $d$ directly, use this procedure:

1. Locate the rod's center of mass.
2. Find the distance $d$ from the pivot to that center of mass.
3. Shift $I_{\mathrm{cm}}$ to the pivot with the parallel-axis theorem.
4. Substitute $I_p$ and $d$ into the period formula.
5. Simplify symbolically before inserting numbers.

---

<a id="find-the-pivot-to-center-of-mass-distance"></a>
## Find the Pivot-to-Center-of-Mass Distance

**Example:** A uniform rod of length $L$ has a pivot $L/6$ below its upper end. Find the distance $d$ from the pivot to the center of mass.

**Explanation**

The center of mass of a uniform rod is $L/2$ below the upper end. Both locations are measured from the same reference point, so subtract:

| Location measured from the upper end | Position |
|---|---:|
| Pivot | $L/6$ |
| Center of mass | $L/2$ |
| Separation | $d=L/2-L/6$ |

$$
d=\frac{L}{2}-\frac{L}{6}.
$$

Using a common denominator,

$$
d=\frac{3L}{6}-\frac{L}{6}
=\frac{2L}{6}
=\frac{L}{3}.
$$

**Watch Out!** The labeled distance $L/6$ runs from the upper end to the pivot. It is not the distance $d$ from the pivot to the center of mass.

```quiz
type: radio
id: problem-4-distance-q1
content: |-
  A uniform rod of length $L$ is pivoted $L/4$ below its upper end. What is the distance from the pivot to the rod's center of mass?
options:
- id: a
  content: |-
    $\dfrac{L}{4}$
  correct: true
  feedback: |-
    The center of mass is at $L/2$, so $d=L/2-L/4=L/4$.
- id: b
  content: |-
    $\dfrac{L}{2}$
  feedback: |-
    This locates the center of mass from the end, not from the pivot.
- id: c
  content: |-
    $\dfrac{3L}{4}$
  feedback: |-
    The required distance is the separation between the pivot and the center of mass, not the distance to the lower end.
```

---

<a id="shift-the-moment-of-inertia-to-the-pivot"></a>
## Shift the Moment of Inertia to the Pivot

**Example:** Find the moment of inertia about the pivot for a uniform rod when $d=L/3$.

**Explanation**

The standard moment of inertia of a uniform rod about its center is

$$
I_{\mathrm{cm}}=\frac{1}{12}mL^2.
$$

The period formula needs the inertia about the actual pivot, so apply the parallel-axis theorem:

$$
I_p=I_{\mathrm{cm}}+md^2.
$$

Substitute $d=L/3$:

$$
\begin{aligned}
I_p
&=\frac{1}{12}mL^2+m\left(\frac{L}{3}\right)^2 \\
&=\frac{1}{12}mL^2+\frac{1}{9}mL^2 \\
&=\left(\frac{3}{36}+\frac{4}{36}\right)mL^2 \\
&=\frac{7}{36}mL^2.
\end{aligned}
$$

The shift term is added because moving the axis away from the center increases the moment of inertia.

```quiz
type: radio
id: problem-4-inertia-q1
content: |-
  A uniform rod has $I_{\mathrm{cm}}=\frac{1}{12}mL^2$, and its pivot is a distance $d=L/4$ from the center of mass. What is $I_p$?
options:
- id: a
  content: |-
    $\dfrac{7}{48}mL^2$
  correct: true
  feedback: |-
    $I_p=\frac{1}{12}mL^2+m(L/4)^2=(4/48+3/48)mL^2=\frac{7}{48}mL^2$.
- id: b
  content: |-
    $\dfrac{1}{48}mL^2$
  feedback: |-
    The parallel-axis contribution is added, not subtracted.
- id: c
  content: |-
    $\dfrac{1}{3}mL^2$
  feedback: |-
    Squaring $L/4$ gives $L^2/16$, not $L^2/4$.
```

---

<a id="build-and-simplify-the-period-formula"></a>
## Build and Simplify the Period Formula

**Example:** Simplify the physical-pendulum period when $I_p=\frac{7}{36}mL^2$ and $d=L/3$.

**Explanation**

Substitute both expressions into

$$
T=2\pi\sqrt{\frac{I_p}{mgd}}:
$$

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{\frac{7}{36}mL^2}{mg\left(\frac{L}{3}\right)}} \\
&=2\pi\sqrt{\frac{7mL^2}{36}\cdot\frac{3}{mgL}} \\
&=2\pi\sqrt{\frac{7L}{12g}}.
\end{aligned}
$$

The common factors $m$ and one factor of $L$ cancel. The rod's mass does not affect the period for this fixed shape and pivot location.

The cancellation is easiest to verify after the numerator and denominator are written as products:

| Factor | Numerator | Denominator | Result |
|---|---:|---:|---|
| $m$ | $m$ | $m$ | Cancels |
| $L$ | $L^2$ | $L$ | Leaves $L$ |
| Number | $7/36$ | $1/3$ | Gives $7/12$ |

**Watch Out!** Cancel common factors, not pieces of a sum. Combine the two inertia terms first; then substitute the factored result $I_p=\frac{7}{36}mL^2$.

```quiz
type: radio
id: problem-4-formula-q1
content: |-
  Which expression results when $I_p=\frac{7}{36}mL^2$ and $d=L/3$ are substituted into $T=2\pi\sqrt{I_p/(mgd)}$ and simplified?
options:
- id: a
  content: |-
    $2\pi\sqrt{\dfrac{7L}{12g}}$
  correct: true
  feedback: |-
    The $m$ factors cancel, $L^2/L=L$, and the numerical factor is $(7/36)\cdot3=7/12$.
- id: b
  content: |-
    $2\pi\sqrt{\dfrac{7mL}{12g}}$
  feedback: |-
    The factor $m$ appears in both numerator and denominator and cancels.
- id: c
  content: |-
    $2\pi\sqrt{\dfrac{7L}{108g}}$
  feedback: |-
    Dividing by $L/3$ multiplies by $3/L$; it does not divide by another factor of $3$.
```

---

<a id="evaluate-the-period-and-check-the-units"></a>
## Evaluate the Period and Check the Units

**Example:** Evaluate $T=2\pi\sqrt{7L/(12g)}$ for $L=0.60\ \mathrm{m}$ and $g=9.81\ \mathrm{m/s^2}$.

**Explanation**

Substitute the values only after the symbolic simplification:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{7(0.60\ \mathrm{m})}{12(9.81\ \mathrm{m/s^2})}} \\
&=1.1868\ldots\ \mathrm{s} \\
&=1.2\ \mathrm{s}.
\end{aligned}
$$

The length has two significant figures, so the period is reported with two significant figures.

Keep the unrounded calculator value through the square root and the multiplication by $2\pi$. Round only the final period.

The units also verify the answer type:

$$
\sqrt{\frac{\mathrm{m}}{\mathrm{m/s^2}}}
=\sqrt{\mathrm{s^2}}
=\mathrm{s}.
$$

```quiz
type: radio
id: problem-4-numeric-q1
content: |-
  For the same pivot geometry, use $T=2\pi\sqrt{7L/(12g)}$ with $L=0.48\ \mathrm{m}$ and $g=9.81\ \mathrm{m/s^2}$. What is the period to two significant figures?
options:
- id: a
  content: |-
    $1.1\ \mathrm{s}$
  correct: true
  feedback: |-
    Substitution gives $T=1.0615\ldots\ \mathrm{s}$, which rounds to $1.1\ \mathrm{s}$ at two significant figures.
- id: b
  content: |-
    $1.06\ \mathrm{s}$
  feedback: |-
    This value has three significant figures, but the measured length has two.
- id: c
  content: |-
    $0.17\ \mathrm{s}$
  feedback: |-
    This omits the outside factor $2\pi$.
```

---

<a id="apply-the-procedure-to-the-offset-pivot-rod"></a>
## Apply the Procedure to the Offset-Pivot Rod

**Example:** A uniform rod pivots $L/6$ below its upper end. Find its small-angle period for the given length and mass.

![](<../Source/Images/uniform-rod-offset-pivot.png>)

**Explanation**

The center of mass is $L/2$ below the upper end, so

$$
d=\frac{L}{2}-\frac{L}{6}=\frac{L}{3}.
$$

The parallel-axis theorem gives

$$
I_p=\frac{1}{12}mL^2+m\left(\frac{L}{3}\right)^2
=\frac{7}{36}mL^2.
$$

Therefore,

$$
T=2\pi\sqrt{\frac{I_p}{mgd}}
=2\pi\sqrt{\frac{7L}{12g}}.
$$

For $L=0.75\ \mathrm{m}$ and $g=9.81\ \mathrm{m/s^2}$,

$$
T=1.3269\ldots\ \mathrm{s}=1.3\ \mathrm{s}
$$

to two significant figures. The value of $m$ is not needed numerically because it cancels.

```quiz
type: radio
id: m4-2lec-q3
content: |-
  **Question 3**

  A uniform rod of mass $m$ and length $L$ pivots about a point $L/6$ below its upper end. Find its small-angle oscillation period for $L=0.75\ \mathrm{m}$ and $m=0.56\ \mathrm{kg}$.

  ![](<../Source/Images/uniform-rod-offset-pivot.png>)

  Enter the period in seconds as a number only:
options:
- id: a
  content: 1.3
  correct: true
- id: b
  content: 1.4
- id: c
  content: 0.21
- id: d
  content: 0.87
feedback: |-
  The pivot lies a distance

  $$
  d=\frac{L}{2}-\frac{L}{6}=\frac{L}{3}
  $$

  from the rod's center of mass. By the parallel-axis theorem,

  $$
  I_p=\frac{1}{12}mL^2+m\left(\frac{L}{3}\right)^2
  =\frac{7}{36}mL^2.
  $$

  Therefore,

  $$
  T=2\pi\sqrt{\frac{I_p}{mgd}}
  =2\pi\sqrt{\frac{7L}{12g}}
  =1.3269\ldots\ \mathrm{s}.
  $$

  The measured length has two significant figures, so $T=1.3\ \mathrm{s}$. The rod's mass cancels.
```

---

<a id="summary"></a>
## Summary

For a uniform rod pivoted away from its center:

1. Measure $d$ from the pivot to the rod's center of mass, not from the end to the pivot.
2. Use $I_{\mathrm{cm}}=\frac{1}{12}mL^2$.
3. Shift the inertia with $I_p=I_{\mathrm{cm}}+md^2$.
4. Substitute into $T=2\pi\sqrt{I_p/(mgd)}$.
5. Simplify before inserting numbers, check for seconds, and round to the precision of the givens.

For a pivot $L/6$ below the upper end, $d=L/3$, $I_p=\frac{7}{36}mL^2$, and

$$
T=2\pi\sqrt{\frac{7L}{12g}}.
$$
