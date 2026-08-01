# Period of a Rod-and-Point-Mass Pendulum

## Table of Contents

- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Build the Composite-Pendulum Formula](#build-the-composite-pendulum-formula)
- [Make a Component Ledger](#make-a-component-ledger)
- [Simplify and Evaluate the Period](#simplify-and-evaluate-the-period)
- [Apply the Method to Problem 5](#apply-the-method-to-problem-5)
- [Summary](#summary)

## Prerequisites

- Use the small-angle physical-pendulum period formula.
- Find moments of inertia about a specified pivot.
- Locate each component's center of mass.
- Evaluate a multi-variable expression and round the final result.

---

<a id="introduction"></a>
## Introduction

When several rigid components swing together about one pivot through small angles, the recognition cue is that every component contributes both rotational inertia and a gravity-torque weight. Use one move: make a component ledger, add the pivot moments $I_i$ and the paired terms $m_id_i$ separately, then substitute those two sums into

$$
T=2\pi\sqrt{\frac{\sum_i I_i}{g\sum_i m_id_i}}.
$$

---

<a id="build-the-composite-pendulum-formula"></a>
## Build the Composite-Pendulum Formula

**Recognition cue:** Several rigid components swing together about one pivot, so add their contributions before using the physical-pendulum period formula.

For a composite physical pendulum,

$$
T=2\pi\sqrt{\frac{I_{\mathrm{total}}}{g\sum_i m_i d_i}},
$$

where

$$
I_{\mathrm{total}}=\sum_i I_i
$$

and $d_i$ is the distance from the pivot to component $i$'s center of mass.

There are two separate sums:

- add each component's pivot moment of inertia in the numerator;
- add each component's $m_i d_i$ contribution in the denominator.

**Example:** A rigid assembly contains two parts with pivot moments of inertia $I_1$ and $I_2$, masses $m_1$ and $m_2$, and center-of-mass distances $d_1$ and $d_2$. Its period formula is

$$
T=2\pi\sqrt{\frac{I_1+I_2}{g(m_1d_1+m_2d_2)}}.
$$

**Explanation**

Do not average the component moments or distances. Each contribution enters its appropriate sum.

```quiz
type: radio
id: p5-composite-formula
content: |-
  Two rigid components swing together about one pivot. Which expression gives their small-angle period?
options:
- id: p5-composite-formula-a
  content: |-
    $2\pi\sqrt{\dfrac{I_1+I_2}{g(m_1d_1+m_2d_2)}}$
  correct: true
- id: p5-composite-formula-b
  content: |-
    $2\pi\sqrt{\dfrac{I_1I_2}{g(m_1d_1+m_2d_2)}}$
- id: p5-composite-formula-c
  content: |-
    $2\pi\sqrt{\dfrac{I_1+I_2}{g(m_1+m_2)(d_1+d_2)}}$
- id: p5-composite-formula-d
  content: |-
    $2\pi\sqrt{\dfrac{I_1+I_2}{g(m_1d_2+m_2d_1)}}$
feedback: |-
  Add the pivot moments and add each component's own $m_id_i$ term. Moments of inertia add; they do not multiply. Also, each mass must stay paired with the distance to its own center of mass.
```

---

<a id="make-a-component-ledger"></a>
## Make a Component Ledger

For a uniform rod of mass $m_r$ and length $L$ pivoted at its upper end, with a point mass $m_p$ at its lower end, list the two contributions before combining them.

| Component | Pivot moment of inertia $I_i$ | Distance $d_i$ | Torque contribution $m_i d_i$ |
| --- | --- | --- | --- |
| Uniform rod | $\frac13m_rL^2$ | $L/2$ | $m_rL/2$ |
| Point mass | $m_pL^2$ | $L$ | $m_pL$ |

Therefore,

$$
I_{\mathrm{total}}=\frac13m_rL^2+m_pL^2
$$

and

$$
\sum_i m_i d_i=m_r\frac L2+m_pL.
$$

**Example:** If the point mass is removed, these sums reduce to the uniform-rod expressions $I=\frac13m_rL^2$ and $m_rd=m_rL/2$.

**Explanation**

This limiting case checks that the component ledger is consistent with a rod-only physical pendulum.

```quiz
type: radio
id: p5-component-ledger
content: |-
  Which pair correctly describes a uniform rod pivoted at one end with a point mass attached at the other end?
options:
- id: p5-component-ledger-a
  content: |-
    $I_{\mathrm{total}}=\frac13m_rL^2+m_pL^2$ and $\sum m_id_i=m_r\frac L2+m_pL$
  correct: true
- id: p5-component-ledger-b
  content: |-
    $I_{\mathrm{total}}=\frac1{12}m_rL^2+m_pL^2$ and $\sum m_id_i=m_r\frac L2+m_pL$
- id: p5-component-ledger-c
  content: |-
    $I_{\mathrm{total}}=\frac13(m_r+m_p)L^2$ and $\sum m_id_i=(m_r+m_p)\frac L2$
- id: p5-component-ledger-d
  content: |-
    $I_{\mathrm{total}}=\frac13m_rL^2+m_pL$ and $\sum m_id_i=m_r+m_p$
feedback: |-
  The rod uses its end-pivot moment $\frac13m_rL^2$ and center-of-mass distance $L/2$. The point mass is distance $L$ from the pivot, so its moment is $m_pL^2$ and its torque weight is $m_pL$.
```

---

<a id="simplify-and-evaluate-the-period"></a>
## Simplify and Evaluate the Period

Substitute the component sums:

$$
T=2\pi\sqrt{
\frac{\frac13m_rL^2+m_pL^2}
{g\left[m_r(L/2)+m_pL\right]}
}.
$$

Factoring $L^2$ from the numerator and $L$ from the bracket gives the equivalent form

$$
T=2\pi\sqrt{
\frac{L\left(m_r/3+m_p\right)}
{g\left(m_r/2+m_p\right)}
}.
$$

If both masses are multiplied by the same factor, that factor cancels. The period depends on their mass ratio, not on a common scaling of the entire assembly.

This is a common-factor cancellation, not a term-by-term cancellation. You may cancel one common scale factor multiplying **both** $m_r$ and $m_p$, but you may not cancel $m_r$ or $m_p$ through the sums

$$
\frac{m_r/3+m_p}{m_r/2+m_p}.
$$

The units check:

$$
\frac{I_{\mathrm{total}}}{g\sum m_i d_i}
\sim
\frac{\mathrm{kg\,m^2}}
{(\mathrm{m/s^2})(\mathrm{kg\,m})}
=\mathrm{s^2},
$$

so the square root has units of seconds.

**Example:** For $m_r=0.30\ \mathrm{kg}$, $m_p=0.20\ \mathrm{kg}$, and $L=1.0\ \mathrm m$,

$$
T=2\pi\sqrt{
\frac{(1.0)\left(0.30/3+0.20\right)}
{(9.81)\left(0.30/2+0.20\right)}
}
=1.86\ldots\ \mathrm s.
$$

**Explanation**

Evaluate in this order:

1. Find $m_r/3+m_p$.
2. Find $m_r/2+m_p$.
3. Form the complete radicand using parentheses.
4. Take the positive square root and multiply by $2\pi$.

```quiz
type: radio
id: p5-evaluate-composite
content: |-
  A uniform rod with $m_r=0.40\ \mathrm{kg}$ and $L=0.80\ \mathrm m$ carries a point mass $m_p=0.20\ \mathrm{kg}$ at its lower end. Using $g=9.81\ \mathrm{m/s^2}$, what is the small-angle period?
options:
- id: p5-evaluate-composite-a
  content: |-
    $1.64\ \mathrm s$
  correct: true
- id: p5-evaluate-composite-b
  content: |-
    $1.79\ \mathrm s$
- id: p5-evaluate-composite-c
  content: |-
    $0.82\ \mathrm s$
- id: p5-evaluate-composite-d
  content: |-
    $2.32\ \mathrm s$
feedback: |-
  Substitute with parentheses into $T=2\pi\sqrt{L(m_r/3+m_p)/[g(m_r/2+m_p)]}$. This gives $1.637\ldots\ \mathrm s$, or $1.64\ \mathrm s$. The value $1.79\ \mathrm s$ ignores the point mass and uses the rod-only period.
```

---

<a id="apply-the-method-to-problem-5"></a>
## Apply the Method to Problem 5

**Example:** A physical pendulum consists of a uniform rod of mass $m_r$ and length $L$, with a point mass $m_p$ attached at its lower end. Find the small-angle period for $m_r=0.35\ \mathrm{kg}$, $m_p=0.25\ \mathrm{kg}$, and $L=1.2\ \mathrm{m}$.

![](<../Source/Images/rod-point-mass-pendulum.png>)

**Explanation**

The total moment of inertia about the pivot is

$$
I=\frac13m_rL^2+m_pL^2.
$$

The gravitational torque factor is $g[m_r(L/2)+m_pL]$, so

$$
T=2\pi\sqrt{\frac{\frac13m_rL^2+m_pL^2}{g[m_r(L/2)+m_pL]}}
=2.0412\ldots\ \mathrm{s}.
$$

The component ledger makes the substitution auditable:

| Contribution | Rod | Point mass | Total |
| --- | ---: | ---: | ---: |
| Pivot moment $I_i$ | $\frac13(0.35)(1.2)^2=0.168\ \mathrm{kg\,m^2}$ | $(0.25)(1.2)^2=0.360\ \mathrm{kg\,m^2}$ | $0.528\ \mathrm{kg\,m^2}$ |
| Torque weight $m_id_i$ | $(0.35)(0.60)=0.210\ \mathrm{kg\,m}$ | $(0.25)(1.2)=0.300\ \mathrm{kg\,m}$ | $0.510\ \mathrm{kg\,m}$ |

Thus,

$$
\frac{I_{\mathrm{total}}}{g\sum m_id_i}
=\frac{0.528}{(9.81)(0.510)}
=0.1055\ldots\ \mathrm{s^2},
$$

and $2\pi\sqrt{0.1055\ldots}=2.0412\ldots\ \mathrm s$.

The measured givens have two significant figures, so $T=2.0\ \mathrm{s}$.

The requested answer form is: **Enter the period in seconds as a number only.** Enter **2.0**.

```quiz
type: radio
id: p5-source-check
content: |-
  **Question 4**

  A physical pendulum consists of a uniform rod of mass $m_r$ and length $L$, with a point mass $m_p$ attached at its lower end. Find the small-angle period for $m_r=0.35\ \mathrm{kg}$, $m_p=0.25\ \mathrm{kg}$, and $L=1.2\ \mathrm{m}$.

  ![](<../Source/Images/rod-point-mass-pendulum.png>)

  Enter the period in seconds as a number only.
options:
- id: p5-source-check-a
  content: |-
    2.0
  correct: true
- id: p5-source-check-b
  content: |-
    2.2
- id: p5-source-check-c
  content: |-
    1.8
- id: p5-source-check-d
  content: |-
    1.0
feedback: |-
  The total moment of inertia about the pivot is

  $$
  I=\frac13m_rL^2+m_pL^2.
  $$

  The gravitational torque factor is $g[m_r(L/2)+m_pL]$, so

  $$
  T=2\pi\sqrt{\frac{\frac13m_rL^2+m_pL^2}{g[m_r(L/2)+m_pL]}}
  =2.0412\ldots\ \mathrm{s}.
  $$

  The measured givens have two significant figures, so $T=2.0\ \mathrm{s}$.

  The distractors encode nearby errors: `2.2` treats the whole system as a point mass at distance $L$; `1.8` ignores the attached point mass and uses the rod-only period; and `1.0` effectively loses the factor of $2$ in $2\pi$.
```

---

## Summary

1. Recognize multiple rigid components swinging together about one pivot.
2. Add pivot moments: $I_{\mathrm{total}}=\sum I_i$.
3. Add torque weights: $\sum m_i d_i$.
4. Use $T=2\pi\sqrt{I_{\mathrm{total}}/(g\sum m_i d_i)}$; never cancel through an addition sign.
5. Evaluate both sums, form the radicand, take the positive square root, then multiply by $2\pi$.
6. Check units, keep guard digits, and round only the final result.
