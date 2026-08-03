# Calculating a Rod's Moment of Inertia from Linear Density

<!--
lesson-id: 212-M2-021
topic-code: MTH212.M2.21
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Inertia Element](#build-the-inertia-element)
- [Combine the Distance and Density Powers](#combine-the-distance-and-density-powers)
- [Use the Rod's Bounds](#use-the-rods-bounds)
- [Keep Mass and Moment of Inertia Distinct](#keep-mass-and-moment-of-inertia-distinct)
- [Summary](#summary)

## Prerequisites

- Review [[Problem-1|Interpreting the Moment of Inertia Integral]]: understand $I=\int r^2\,dm$ as mass weighted by squared distance.
- Use $dm=\lambda(x)\,dx$ for a thin rod with linear mass density $\lambda(x)$.
- Apply the power rule for definite integrals.

---

<a id="introduction"></a>
## Introduction

When a thin rod has a position-dependent linear density and the problem asks for its moment of inertia, first turn the mass integral into an $x$-integral. For a rod on the $x$-axis rotating about a perpendicular axis through the origin,

$$
r=x
\qquad\text{and}\qquad
dm=\lambda(x)\,dx.
$$

Therefore,

$$
I=\int r^2\,dm
=\int x^2\lambda(x)\,dx.
$$

The key recognition cue is the combination of a **density function** and a **specified rotation axis**. The density supplies the mass element, while the axis supplies the distance factor.

Before doing any arithmetic, translate the problem in this order:

| Problem information | Integral ingredient |
| --- | --- |
| Axis location | Perpendicular distance $r$ |
| Linear density | Mass element $dm=\lambda(x)\,dx$ |
| Rod's coordinate interval | Lower and upper bounds |

For a rod on $0\le x\le L$ about the origin, this produces the reusable setup line

$$
\boxed{I=\int_0^L \underbrace{x^2}_{r^2}\underbrace{\lambda(x)\,dx}_{dm}}.
$$

---

<a id="build-the-inertia-element"></a>
## Build the Inertia Element

**Example:** A rod extends from $x=0$ to $x=L$, has constant linear density $k$, and rotates about a perpendicular axis through the origin. Find its moment of inertia.

**Explanation**

A piece at coordinate $x$ is distance $x$ from the axis, and its mass is $dm=k\,dx$. Thus,

$$
dI=x^2\,dm=kx^2\,dx.
$$

Accumulating these contributions gives

$$
I=\int_0^L kx^2\,dx
=k\left[\frac{x^3}{3}\right]_0^L
=\frac{kL^3}{3}.
$$

The factor $x^2$ must be present before integrating. Integrating only $k\,dx$ would find the rod's mass, not its moment of inertia.

```quiz
type: radio
id: p5-build-element
content: |-
  A thin rod lies from $x=0$ to $x=A$, has linear density $\lambda(x)=q$, and rotates about a perpendicular axis through the origin. Which integral gives its moment of inertia?
options:
- id: a
  content: |-
    $\displaystyle \int_0^A qx^2\,dx$
  correct: true
- id: b
  content: |-
    $\displaystyle \int_0^A q\,dx$
- id: c
  content: |-
    $\displaystyle \int_0^A qx\,dx$
- id: d
  content: |-
    $\displaystyle \int_0^A \frac{q}{x^2}\,dx$
- id: e
  content: |-
    $\displaystyle qA^2$
```

---

<a id="combine-the-distance-and-density-powers"></a>
## Combine the Distance and Density Powers

**Example:** A rod extends from $x=0$ to $x=B$ with linear density $\lambda(x)=ax^2$. Find its moment of inertia about a perpendicular axis through the origin.

**Explanation**

Substitute the density into $x^2\lambda(x)$ **before** integrating:

$$
x^2\lambda(x)=x^2(ax^2)=ax^4.
$$

Then

$$
I=\int_0^B ax^4\,dx
=a\left[\frac{x^5}{5}\right]_0^B
=\frac{aB^5}{5}.
$$

There are two separate power changes: the distance weighting raises $x^2$ to $x^4$ after multiplication by the density, and integration raises $x^4$ to $x^5$ while dividing by $5$.

A units check supports the result. Since $\lambda(x)=ax^2$ has units of mass per length, $a$ has units of mass per length cubed. Therefore, $aB^5$ has units

$$
\frac{\text{mass}}{\text{length}^3}\cdot\text{length}^5
=\text{mass}\cdot\text{length}^2,
$$

as a moment of inertia must.

```quiz
type: radio
id: p5-combine-powers
content: |-
  A rod lies from $x=0$ to $x=R$ and has linear density $\lambda(x)=bx^3$. What is its moment of inertia about a perpendicular axis through the origin?
options:
- id: a
  content: |-
    $\displaystyle \frac{bR^6}{6}$
  correct: true
- id: b
  content: |-
    $\displaystyle \frac{bR^4}{4}$
- id: c
  content: |-
    $\displaystyle \frac{bR^5}{5}$
- id: d
  content: |-
    $\displaystyle bR^6$
- id: e
  content: |-
    $\displaystyle 6bR^6$
```

---

<a id="use-the-rods-bounds"></a>
## Use the Rod's Bounds

**Example:** A rod occupies the interval $a\le x\le b$, has density $\lambda(x)=cx^2$, and rotates about a perpendicular axis through the origin. Find its moment of inertia.

**Explanation**

The axis is still at the origin, so a point at coordinate $x$ has distance $r=x$. The rod begins at $a$, however, so its geometric bounds are $a$ and $b$:

$$
I=\int_a^b x^2(cx^2)\,dx
=c\left[\frac{x^5}{5}\right]_a^b
=\frac{c}{5}\left(b^5-a^5\right).
$$

The integration limits describe where the rod is. They do not automatically begin at zero unless the rod does.

```quiz
type: radio
id: p5-use-bounds
content: |-
  A rod occupies $L\le x\le 2L$, has density $\lambda(x)=kx^2$, and rotates about a perpendicular axis through the origin. Which expression is its moment of inertia?
options:
- id: a
  content: |-
    $\displaystyle \frac{31kL^5}{5}$
  correct: true
- id: b
  content: |-
    $\displaystyle \frac{32kL^5}{5}$
- id: c
  content: |-
    $\displaystyle \frac{kL^5}{5}$
- id: d
  content: |-
    $\displaystyle \frac{7kL^3}{3}$
- id: e
  content: |-
    $\displaystyle 31kL^5$
```

---

<a id="keep-mass-and-moment-of-inertia-distinct"></a>
## Keep Mass and Moment of Inertia Distinct

**Example:** A rod from $x=0$ to $x=L$ has density $\lambda(x)=cx^2$ and total mass $M$. Express its moment of inertia first in terms of $c$ and $L$, then in terms of $M$ and $L$.

**Explanation**

The moment of inertia comes directly from the squared-distance weighting:

$$
I=\int_0^L x^2(cx^2)\,dx=\frac{cL^5}{5}.
$$

The total mass uses a different integral:

$$
M=\int_0^L cx^2\,dx=\frac{cL^3}{3}.
$$

If the requested answer must use $M$ instead of $c$, solve $c=3M/L^3$ and substitute:

$$
I=\frac{1}{5}\left(\frac{3M}{L^3}\right)L^5
=\frac{3}{5}ML^2.
$$

Do not eliminate $c$ merely because the total mass is stated. Let the requested answer form decide: keep $c$ when the choices use $c$ and $L$, and substitute for $c$ only when the answer must use $M$ and $L$.

```quiz
type: radio
id: p5-mass-versus-inertia
content: |-
  A rod from $x=0$ to $x=L$ has density $\lambda(x)=cx^2$. The requested answer should be in terms of $c$ and $L$. Which result is the moment of inertia about a perpendicular axis through the origin?
options:
- id: a
  content: |-
    $\displaystyle \frac{cL^5}{5}$
  correct: true
- id: b
  content: |-
    $\displaystyle \frac{cL^3}{3}$
- id: c
  content: |-
    $\displaystyle cL^5$
- id: d
  content: |-
    $\displaystyle \frac{cL^4}{4}$
- id: e
  content: |-
    $\displaystyle 5cL^5$
```

---

<a id="summary"></a>
## Summary

For a thin rod with density $\lambda(x)$:

1. Use the rotation axis to write the perpendicular distance $r$.
2. Replace $dm$ with $\lambda(x)\,dx$.
3. Form the full contribution $dI=r^2\lambda(x)\,dx$.
4. Integrate over the rod's actual coordinate interval.
5. Check that the result has units of mass times length squared.

For a rod on $0\le x\le L$ rotating about a perpendicular axis through the origin, $r=x$, so

$$
I=\int_0^L x^2\lambda(x)\,dx.
$$

The main trap is computing $\int\lambda(x)\,dx$, which gives mass, and forgetting the extra squared-distance factor needed for moment of inertia.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
