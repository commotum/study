# Center of Mass of a Rod With Linearly Increasing Density

<!--
lesson-id: 212-M2-008
topic-code: MTH212.M2.08
-->

## Table of Contents

- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Build the Mass and First-Moment Integrals](#build-the-mass-and-first-moment-integrals)
- [Evaluate the Integrals](#evaluate-the-integrals)
- [Simplify the Ratio and Check the Location](#simplify-the-ratio-and-check-the-location)
- [Apply the Method to the Rod](#apply-the-method-to-the-rod)
- [Summary](#summary)

<a id="prerequisites"></a>
## Prerequisites

- Interpret linear density through $dm=\lambda(x)\,dx$.
- Use the power rule for antiderivatives.
- Evaluate definite integrals on $[0,L]$.
- Simplify a quotient of algebraic expressions.

---

<a id="introduction"></a>
## Introduction

When a rod's density changes with position, its center of mass is a weighted mean of position. A small piece of width $dx$ has mass

$$
dm=\lambda(x)\,dx,
$$

so a rod extending from $x=0$ to $x=L$ has center of mass

$$
x_{\mathrm{cm}}
=\frac{\int_0^L x\,dm}{\int_0^L dm}
=\frac{\int_0^L x\lambda(x)\,dx}
{\int_0^L \lambda(x)\,dx}.
$$

The denominator is the rod's total mass. The numerator is its first moment about the origin. The core move is to build those two integrals separately and then divide.

This is the continuous version of “weighted total divided by total weight”:

| Weighted-mean role | Discrete form | Continuous rod form |
|---|---:|---:|
| Total weight | $\sum_i w_i$ | $\int_0^L\lambda(x)\,dx$ |
| Weighted total | $\sum_i x_iw_i$ | $\int_0^Lx\lambda(x)\,dx$ |
| Center | $\dfrac{\sum_i x_iw_i}{\sum_i w_i}$ | $\dfrac{\int_0^Lx\lambda(x)\,dx}{\int_0^L\lambda(x)\,dx}$ |

The recognition cue is therefore: **varying density plus a requested center of mass means first moment divided by total mass.**

---

<a id="build-the-mass-and-first-moment-integrals"></a>
## Build the Mass and First-Moment Integrals

**Example:** A rod occupies $0\le x\le L$ and has density $\lambda(x)=kx$. Write, but do not evaluate, its total-mass and first-moment integrals.

**Explanation**

For total mass, add the small masses $dm=\lambda(x)\,dx$:

$$
M_{\mathrm{tot}}=\int_0^L kx\,dx.
$$

For the first moment, multiply each small mass by its coordinate before adding:

$$
P=\int_0^L x\,dm
=\int_0^L x(kx)\,dx
=\int_0^L kx^2\,dx.
$$

The extra factor of $x$ belongs only in the numerator. This also gives a unit check: $M_{\mathrm{tot}}$ has units of mass, while $P$ has units of mass times length.

```quiz
type: radio
id: problem-2-build-integrals-q1
content: |-
  A rod occupies $0\le x\le L$ and has density $\lambda(x)=ax^2$. Which pair gives its total mass $M_{\mathrm{tot}}$ and first moment $P$ about the origin?
options:
- id: a
  content: |-
    $M_{\mathrm{tot}}=\displaystyle\int_0^L ax^2\,dx$ and $P=\displaystyle\int_0^L ax^3\,dx$
  correct: true
  feedback: |-
    Total mass integrates $\lambda(x)$, while the first moment integrates $x\lambda(x)$.
- id: b
  content: |-
    $M_{\mathrm{tot}}=\displaystyle\int_0^L ax^3\,dx$ and $P=\displaystyle\int_0^L ax^2\,dx$
  feedback: |-
    This swaps the mass and first-moment integrands.
- id: c
  content: |-
    $M_{\mathrm{tot}}=\displaystyle\int_0^L ax^2\,dx$ and $P=\displaystyle\int_0^L a^2x^4\,dx$
  feedback: |-
    The first moment multiplies the density by position; it does not square the density.
- id: d
  content: |-
    $M_{\mathrm{tot}}=\displaystyle\int_0^L ax\,dx$ and $P=\displaystyle\int_0^L ax^2\,dx$
  feedback: |-
    These integrands correspond to the different density $\lambda(x)=ax$.
```

---

<a id="evaluate-the-integrals"></a>
## Evaluate the Integrals

**Example:** Evaluate the total mass and first moment for $\lambda(x)=kx$ on $0\le x\le L$.

**Explanation**

For each power, first raise the exponent by one, then divide by that new exponent:

$$
\int x^n\,dx=\frac{x^{n+1}}{n+1}+C
\qquad (n\ne -1).
$$

Then evaluate the antiderivative as upper endpoint minus lower endpoint:

$$
M_{\mathrm{tot}}
=k\left[\frac{x^2}{2}\right]_0^L
=k\left(\frac{L^2}{2}-\frac{0^2}{2}\right)
=\frac{kL^2}{2},
$$

and

$$
P
=k\left[\frac{x^3}{3}\right]_0^L
=k\left(\frac{L^3}{3}-\frac{0^3}{3}\right)
=\frac{kL^3}{3}.
$$

Because the lower limit is zero, both lower-limit terms vanish. Keep the two results separate until both have been evaluated.

```quiz
type: radio
id: problem-2-evaluate-integrals-q1
content: |-
  For a rod on $0\le x\le L$ with $\lambda(x)=bx^2$, what are its total mass $M_{\mathrm{tot}}$ and first moment $P$ about the origin?
options:
- id: a
  content: |-
    $M_{\mathrm{tot}}=\dfrac{bL^3}{3}$ and $P=\dfrac{bL^4}{4}$
  correct: true
  feedback: |-
    Integrating $bx^2$ gives $bL^3/3$, and integrating $x(bx^2)=bx^3$ gives $bL^4/4$.
- id: b
  content: |-
    $M_{\mathrm{tot}}=\dfrac{bL^2}{2}$ and $P=\dfrac{bL^3}{3}$
  feedback: |-
    These are the results for a density proportional to $x$, not $x^2$.
- id: c
  content: |-
    $M_{\mathrm{tot}}=\dfrac{bL^3}{2}$ and $P=\dfrac{bL^4}{3}$
  feedback: |-
    The power rule divides by the new exponent: by $3$ for $x^2$ and by $4$ for $x^3$.
- id: d
  content: |-
    $M_{\mathrm{tot}}=bL^3$ and $P=bL^4$
  feedback: |-
    This increases each exponent but omits the power-rule divisors.
```

---

<a id="simplify-the-ratio-and-check-the-location"></a>
## Simplify the Ratio and Check the Location

**Example:** Use the two evaluated integrals for $\lambda(x)=kx$ to find $x_{\mathrm{cm}}$.

**Explanation**

Substitute the first moment into the numerator and the total mass into the denominator:

$$
x_{\mathrm{cm}}
=\frac{P}{M_{\mathrm{tot}}}
=\frac{kL^3/3}{kL^2/2}
=\frac{2L}{3}.
$$

The ratio can be simplified one feature at a time:

| Feature | Simplification |
|---|---|
| Density scale | $k/k=1$ |
| Length powers | $L^3/L^2=L$ |
| Numerical fractions | $(1/3)/(1/2)=2/3$ |

The density scale $k$ cancels, so changing the rod's overall mass without changing the shape of its density profile does not move its center of mass.

Always make two physical checks:

1. **Bounds:** the result must lie on the rod, so $0<x_{\mathrm{cm}}<L$.
2. **Direction:** since $\lambda(x)=kx$ puts more mass near the right end, the result should satisfy $x_{\mathrm{cm}}>L/2$.

The result $2L/3$ passes both checks.

```quiz
type: radio
id: problem-2-simplify-ratio-q1
content: |-
  A rod occupies $0\le x\le L$ and has density $\lambda(x)=ax^2$, where $a>0$. What is its center-of-mass position?
options:
- id: a
  content: |-
    $\dfrac{3L}{4}$
  correct: true
  feedback: |-
    $\dfrac{aL^4/4}{aL^3/3}=\dfrac{3L}{4}$, which lies to the right of the midpoint as expected.
- id: b
  content: |-
    $\dfrac{2L}{3}$
  feedback: |-
    This is the result for density proportional to $x$, not $x^2$.
- id: c
  content: |-
    $\dfrac{L}{2}$
  feedback: |-
    The midpoint is the center of mass of a uniform rod; here density increases toward the right.
- id: d
  content: |-
    $\dfrac{4L}{3}$
  feedback: |-
    This reverses the ratio and places the center of mass beyond the rod.
- id: e
  content: |-
    $\dfrac{L}{4}$
  feedback: |-
    Increasing density toward the right requires the center of mass to lie to the right of $L/2$.
```

---

<a id="apply-the-method-to-the-rod"></a>
## Apply the Method to the Rod

**Example:** A rod has length $l=1.8\ \mathrm{m}$ and linear density $\lambda(x)=cx$. Find its center-of-mass position from the origin.

**Explanation**

The denominator and numerator are

$$
\int_0^l \lambda(x)\,dx
=\int_0^l cx\,dx
=\frac{cl^2}{2}
$$

and

$$
\int_0^l x\lambda(x)\,dx
=\int_0^l cx^2\,dx
=\frac{cl^3}{3}.
$$

Therefore,

$$
x_{\mathrm{cm}}
=\frac{cl^3/3}{cl^2/2}
=\frac{2l}{3}
=\frac{2(1.8\ \mathrm{m})}{3}
=1.2\ \mathrm{m}.
$$

The given mass $m=0.65\ \mathrm{kg}$ is not needed because the scale factor $c$ cancels. The answer also lies between the midpoint, $0.90\ \mathrm{m}$, and the right end, $1.8\ \mathrm{m}$.

```quiz
type: radio
id: m2-2lec-q1
content: |-
  **Question 1**

  A rod of mass $m$ and length $l$ has linear mass density $\lambda(x)=cx$. Find the center-of-mass position measured from the origin for $m=0.65\ \mathrm{kg}$ and $l=1.8\ \mathrm{m}$.

  ![](<../Source/Images/rod-with-linearly-increasing-density.png>)

  Enter the position in meters as a number only:
options:
- id: a
  content: |-
    $1.2$
  correct: true
  feedback: |-
    The center of mass is

    $$
    x_{\mathrm{cm}}
    =\frac{\int_0^l x\lambda(x)\,dx}{\int_0^l\lambda(x)\,dx}
    =\frac{cl^3/3}{cl^2/2}
    =\frac{2l}{3}.
    $$

    Thus,

    $$
    x_{\mathrm{cm}}=\frac{2(1.8\ \mathrm{m})}{3}=1.2\ \mathrm{m}.
    $$

    The mass cancels, and the measured length supports two significant figures.
- id: b
  content: |-
    $0.90$
  feedback: |-
    This is the midpoint of a uniform rod, but the density here increases toward the right.
- id: c
  content: |-
    $0.60$
  feedback: |-
    This uses $l/3$ instead of the correct ratio $2l/3$.
- id: d
  content: |-
    $2.7$
  feedback: |-
    This reverses the factor $2/3$ and places the center of mass beyond the rod.
- id: e
  content: |-
    $0.65$
  feedback: |-
    This is the rod's mass in kilograms, not a position in meters.
```

---

<a id="summary"></a>
## Summary

For a rod on $0\le x\le L$:

1. Write the total mass as $\int_0^L\lambda(x)\,dx$.
2. Write the first moment as $\int_0^L x\lambda(x)\,dx$.
3. Divide the first moment by the total mass.
4. Simplify symbolically before inserting numerical values.
5. Check that the result lies on the rod and toward the denser side.

For $\lambda(x)=kx$, this process gives

$$
\boxed{x_{\mathrm{cm}}=\frac{2L}{3}}.
$$

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
