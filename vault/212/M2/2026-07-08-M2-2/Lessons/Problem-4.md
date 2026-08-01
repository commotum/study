# Moment of Inertia About an Off-Center Rod Pivot

## Table of Contents

- [Introduction](#introduction)
- [Find the Center-to-Pivot Distance](#find-the-center-to-pivot-distance)
- [Apply the Parallel-Axis Theorem](#apply-the-parallel-axis-theorem)
- [Combine the Fractional Coefficients](#combine-the-fractional-coefficients)
- [Apply the Method to the Rod](#apply-the-method-to-the-rod)
- [Summary](#summary)

## Prerequisites

- Locate the midpoint of a uniform rod at $L/2$ from either end.
- Subtract and add fractions with unlike denominators.
- Square a fraction.
- Use the center-of-mass moment of inertia of a uniform thin rod, $I_{\mathrm{cm}}=\frac{1}{12}mL^2$.

---

<a id="introduction"></a>
## Introduction

When a rigid body's rotation axis is parallel to an axis through its center of mass, use the parallel-axis theorem:

$$
I_{\text{pivot}}=I_{\mathrm{cm}}+md^2,
$$

where $d$ is the distance **between the center of mass and the new pivot**.

For a uniform thin rod, the center is at $L/2$. If a pivot is given as a fraction of $L$ from an endpoint, first find its separation from $L/2$, then square that separation and add the shift term to $I_{\mathrm{cm}}$.

---

<a id="find-the-center-to-pivot-distance"></a>
## Find the Center-to-Pivot Distance

**Example:** A uniform rod has a pivot at $L/4$ from its left end. Find the distance $d$ between the pivot and the rod's center.

**Explanation**

Place both locations on the same one-dimensional coordinate measured from the left end:

| Point | Position from left end |
|---|---:|
| Pivot | $L/4$ |
| Center of mass | $L/2$ |

The separation is the absolute difference:

$$
d=\left|\frac L2-\frac L4\right|
=\left|\frac{2L}{4}-\frac L4\right|
=\frac L4.
$$

Do not use $L/4$ merely because it labels the pivot position. In this example the two values happen to match; in general, the theorem requires the center-to-pivot separation.

```quiz
type: radio
id: m2-2-p4-offset
shuffle: true
content: |-
  A uniform rod has a pivot at $L/5$ from its left end. What distance $d$ belongs in the parallel-axis theorem?
options:
- id: a
  content: |-
    $\dfrac{L}{5}$
- id: b
  content: |-
    $\dfrac{3L}{10}$
  correct: true
  feedback: |-
    The center is at $L/2$, so $d=|L/2-L/5|=|5L/10-2L/10|=3L/10$.
- id: c
  content: |-
    $\dfrac{L}{2}$
- id: d
  content: |-
    $\dfrac{7L}{10}$
- id: e
  content: |-
    $\dfrac{L}{10}$
```

---

<a id="apply-the-parallel-axis-theorem"></a>
## Apply the Parallel-Axis Theorem

**Example:** A uniform thin rod is pivoted a distance $d=L/4$ from its center. Write its moment of inertia about the pivot.

**Explanation**

Substitute the rod's center-of-mass inertia and the offset into the theorem:

$$
\begin{aligned}
I_{\text{pivot}}
&=I_{\mathrm{cm}}+md^2\\
&=\frac{1}{12}mL^2+m\left(\frac L4\right)^2\\
&=\frac{1}{12}mL^2+\frac{1}{16}mL^2.
\end{aligned}
$$

The shift term is always added. Since $md^2\geq0$, an axis parallel to the center-of-mass axis cannot have a smaller moment of inertia than $I_{\mathrm{cm}}$.

```quiz
type: radio
id: m2-2-p4-theorem
shuffle: true
content: |-
  A uniform thin rod has $I_{\mathrm{cm}}=\frac{1}{12}mL^2$. Which expression gives its moment of inertia about a parallel pivot a distance $L/6$ from its center?
options:
- id: a
  content: |-
    $\dfrac{1}{12}mL^2-m\left(\dfrac L6\right)^2$
- id: b
  content: |-
    $\dfrac{1}{12}mL^2+m\left(\dfrac L6\right)^2$
  correct: true
  feedback: |-
    The parallel-axis theorem is $I_{\text{pivot}}=I_{\mathrm{cm}}+md^2$, so the offset term is added.
- id: c
  content: |-
    $\dfrac{1}{12}mL^2+m\left(\dfrac L6\right)$
- id: d
  content: |-
    $m\left(\dfrac L6\right)^2$
- id: e
  content: |-
    $\dfrac{1}{12}mL^2$
```

---

<a id="combine-the-fractional-coefficients"></a>
## Combine the Fractional Coefficients

**Example:** Finish the calculation for a rod whose pivot is $L/4$ from its center.

**Explanation**

First square the entire fractional distance:

$$
\left(\frac L4\right)^2=\frac{L^2}{16}.
$$

Then combine the coefficients using a common denominator:

$$
\begin{aligned}
I_{\text{pivot}}
&=\left(\frac{1}{12}+\frac{1}{16}\right)mL^2\\
&=\left(\frac{4}{48}+\frac{3}{48}\right)mL^2\\
&=\frac{7}{48}mL^2.
\end{aligned}
$$

Keeping $mL^2$ factored out makes the requested coefficient easy to see.

```quiz
type: radio
id: m2-2-p4-coefficient
shuffle: true
content: |-
  A uniform thin rod rotates about a parallel axis located $L/10$ from its center. What coefficient multiplies $mL^2$ in its moment of inertia?
options:
- id: a
  content: |-
    $\dfrac{1}{120}$
- id: b
  content: |-
    $\dfrac{7}{75}$
  correct: true
  feedback: |-
    $I=(\frac{1}{12}+\frac{1}{100})mL^2=(\frac{25}{300}+\frac{3}{300})mL^2=\frac{7}{75}mL^2$.
- id: c
  content: |-
    $\dfrac{11}{60}$
- id: d
  content: |-
    $\dfrac{1}{100}$
- id: e
  content: |-
    $\dfrac{1}{12}$
```

---

<a id="apply-the-method-to-the-rod"></a>
## Apply the Method to the Rod

**Example:** Find the coefficient of $mL^2$ when the pivot is $L/3$ from the rod's left end.

**Explanation**

The center is at $L/2$, so the center-to-pivot distance is

$$
d=\left|\frac L2-\frac L3\right|=\frac L6.
$$

Now apply the parallel-axis theorem:

$$
\begin{aligned}
I
&=\frac{1}{12}mL^2+m\left(\frac L6\right)^2\\
&=\left(\frac{1}{12}+\frac{1}{36}\right)mL^2\\
&=\left(\frac{3}{36}+\frac{1}{36}\right)mL^2\\
&=\frac19mL^2.
\end{aligned}
$$

The coefficient ledger keeps every location and fraction tied to its role:

| Quantity | Coefficient of the matching power of $L$ |
|---|---:|
| Pivot position from left end | $1/3$ |
| Center position from left end | $1/2$ |
| Center-to-pivot distance $d/L$ | $1/2-1/3=1/6$ |
| Squared offset $d^2/L^2$ | $(1/6)^2=1/36$ |
| Center-of-mass inertia coefficient | $1/12=3/36$ |
| Total coefficient | $3/36+1/36=1/9$ |

There is also a useful bound. The center axis gives the rod's minimum parallel-axis value, $I_{\mathrm{cm}}=\frac{1}{12}mL^2$, while an end axis gives $I_{\mathrm{end}}=\frac13mL^2$. Because this pivot lies between the center and an end,

$$
\frac{1}{12}mL^2<\frac19mL^2<\frac13mL^2,
$$

so the result has the expected size.

Therefore, the coefficient is `1/9`.

```quiz
type: radio
id: m2-2lec-q3
content: |-
  **Question 3**

  A uniform thin rod of mass $m$ and length $L$ rotates about a point located $L/3$ from its left end. Find its moment of inertia in terms of $mL^2$.

  Enter the coefficient multiplying $mL^2$ using ordinary keyboard notation:
options:
- id: a
  content: |-
    `1/9`
  correct: true
- id: b
  content: |-
    `1/12`
- id: c
  content: |-
    `7/36`
- id: d
  content: |-
    `1/18`
- id: e
  content: |-
    `1/3`
feedback: |-
  The rod's center is at $L/2$, so the pivot is a distance

  $$
  d=\frac{L}{2}-\frac{L}{3}=\frac{L}{6}
  $$

  from the center. By the parallel-axis theorem,

  $$
  I=I_{\mathrm{cm}}+md^2
  =\frac{1}{12}mL^2+m\left(\frac{L}{6}\right)^2
  =\frac19mL^2.
  $$
```

---

<a id="summary"></a>
## Summary

- Locate the uniform rod's center at $L/2$ from an endpoint.
- Compute $d$ as the distance from that center to the pivot, not from the endpoint to the pivot.
- Use $I_{\text{pivot}}=I_{\mathrm{cm}}+md^2$ and always add the nonnegative shift term.
- Square the entire fractional offset before combining coefficients.
- Factor out $mL^2$, use a common denominator, and report only the requested coefficient.
