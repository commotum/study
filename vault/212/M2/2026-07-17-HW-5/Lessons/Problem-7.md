# Comparing Orbital Speeds at the Apsides

## Table of Contents

- [Introduction](#introduction)
- [Turn Equal Areas Into a Product](#turn-equal-areas-into-a-product)
- [Identify the Faster Apsis](#identify-the-faster-apsis)
- [Find the Speed Factor](#find-the-speed-factor)
- [Avoid the Inverse-Square Trap](#avoid-the-inverse-square-trap)
- [Summary](#summary)

## Prerequisites

- Kepler's second law: a planet or satellite sweeps out equal areas in equal times.
- The area of a triangle is $\frac12(\text{base})(\text{height})$.
- Solving a proportion and interpreting a ratio as a multiplicative factor.

---

<a id="introduction"></a>
## Introduction

When an orbit problem compares the **closest** and **farthest** points, look for two cues: the radius points from the central body to the satellite, and the velocity is perpendicular to that radius. These points are the apsides.

![](<../Source/2026-07-17-HW-5/Images/elliptical-orbit-apsides.png>)

Let $v_1$ and $v_2$ denote the magnitudes of the two velocity vectors shown.

Over a short equal time interval $\Delta t$, Kepler's second law requires equal swept areas. At an apsis, that area is approximately a thin triangle with height $v\Delta t$. The reusable relation is therefore

$$
\frac12 r_1v_1\Delta t=\frac12 r_2v_2\Delta t
\quad\Longrightarrow\quad
r_1v_1=r_2v_2.
$$

The radius and speed have a constant product: a smaller radius goes with a larger speed.

Equivalently,

$$
rv=k
\quad\Longleftrightarrow\quad
v=\frac{k}{r}
\quad\Longleftrightarrow\quad
v\propto\frac1r.
$$

---

<a id="turn-equal-areas-into-a-product"></a>
## Turn Equal Areas Into a Product

**Example:** A satellite is at two apsides with radii $r_A$ and $r_B$ and tangential speeds $v_A$ and $v_B$. Translate equal swept areas during the same short time $\Delta t$ into an equation relating the speeds.

**Explanation**

At either apsis, the short displacement has length $v\Delta t$ and is perpendicular to the radius. The two swept areas are

$$
\Delta A_A\approx\frac12r_Av_A\Delta t,
\qquad
\Delta A_B\approx\frac12r_Bv_B\Delta t.
$$

Set them equal and cancel the common factors $\frac12$ and $\Delta t$:

$$
r_Av_A=r_Bv_B.
$$

```quiz
type: radio
id: problem-7-area-product
content: |-
  At two apsides, a satellite has radii $r_P,r_Q$ and tangential speeds $v_P,v_Q$. Which equation follows from equal swept areas in equal times?
options:
- id: a
  content: |-
    $r_Pv_P=r_Qv_Q$
  correct: true
- id: b
  content: |-
    $r_P^2v_P=r_Q^2v_Q$
- id: c
  content: |-
    $r_Pv_Q=r_Qv_P$
- id: d
  content: |-
    $v_P=v_Q$
```

---

<a id="identify-the-faster-apsis"></a>
## Identify the Faster Apsis

**Example:** Point $1$ is the closest point of an orbit and point $2$ is the farthest, so $r_1<r_2$. Which speed is larger?

**Explanation**

The product $rv$ must stay constant:

$$
r_1v_1=r_2v_2.
$$

Because $r_1$ is smaller, $v_1$ must be larger to keep the products equal. The satellite is faster at the closest point.

```quiz
type: radio
id: problem-7-faster-apsis
content: |-
  A comet has periapsis radius $r_p$ and apoapsis radius $r_a$, with $r_p<r_a$. Which comparison is correct?
options:
- id: a
  content: |-
    $v_p>v_a$
  correct: true
- id: b
  content: |-
    $v_p<v_a$
- id: c
  content: |-
    $v_p=v_a$
- id: d
  content: |-
    The speeds cannot be compared from Kepler's second law.
```

---

<a id="find-the-speed-factor"></a>
## Find the Speed Factor

**Example:** The farthest radius is four times the closest radius: $r_2=4r_1$. By what factor is the speed at point $1$ greater than the speed at point $2$?

**Explanation**

The requested factor compares the speed at point $1$ with the speed at point $2$, so write the target ratio first:

$$
\text{speed factor}=\frac{v_1}{v_2}.
$$

Now start with the constant-product relation and isolate that ratio:

$$
\begin{aligned}
r_1v_1&=r_2v_2,\\
\frac{r_1v_1}{r_1v_2}&=\frac{r_2v_2}{r_1v_2},\\
\frac{v_1}{v_2}&=\frac{r_2}{r_1}.
\end{aligned}
$$

Thus

$$
\frac{v_1}{v_2}=\frac{4r_1}{r_1}=4.
$$

The speed at the closest point is four times the speed at the farthest point. Notice that the speed ratio uses the radius ratio in the **opposite order**.

```quiz
type: radio
id: problem-7-speed-factor
content: |-
  A satellite's farthest radius is $5$ times its closest radius. How do its speeds compare?
options:
- id: a
  content: |-
    The closest-point speed is $5$ times the farthest-point speed.
  correct: true
- id: b
  content: |-
    The farthest-point speed is $5$ times the closest-point speed.
- id: c
  content: |-
    The closest-point speed is $25$ times the farthest-point speed.
- id: d
  content: |-
    The speeds are equal.
```

---

<a id="avoid-the-inverse-square-trap"></a>
## Avoid the Inverse-Square Trap

**Example:** At two apsides, the radii are $r_1$ and $r_2$, where $r_1<r_2$. Choose the correct symbolic comparison of the speeds.

**Explanation**

The governing relation tells you the exponent. Kepler's second law at the apsides gives

$$
rv=k
\quad\Longrightarrow\quad
v=\frac{k}{r}.
$$

The radius appears to the first power, so $v\propto 1/r$, not $v\propto 1/r^2$. The inverse-square law

$$
F=\frac{K}{r^2}
$$

describes the **gravitational force** as a function of distance; it is not the speed-factor relation here. Therefore,

$$
\frac{v_1}{v_2}=\frac{r_2}{r_1}.
$$

Since $r_2/r_1>1$, this ratio also confirms that point $1$, the closest point, is faster.

```quiz
type: radio
id: problem-7-symbolic-check
content: |-
  A satellite's closest and farthest distances are $r_1$ and $r_2$, respectively. At which point is it moving faster, and by what factor?
options:
- id: a
  content: |-
    It moves faster at the closest approach by a factor of $r_2/r_1$.
  correct: true
- id: b
  content: |-
    It moves faster at the farthest approach by a factor of $r_2/r_1$.
- id: c
  content: |-
    It moves faster at the closest approach by a factor of $(r_2/r_1)^2$.
- id: d
  content: |-
    It moves faster at the farthest approach by a factor of $(r_2/r_1)^2$.
- id: e
  content: |-
    It has the same speed at both points.
```

---

<a id="summary"></a>
## Summary

At the closest and farthest points of an orbit:

1. Recognize that the velocity is perpendicular to the radius.
2. Use equal swept areas in equal times to write $r_1v_1=r_2v_2$.
3. Reverse the radius ratio to get the speed ratio: $v_1/v_2=r_2/r_1$.
4. The smaller-radius point is faster.
5. Check that $r_2/r_1>1$ when point $1$ is closer; a “faster by” factor must exceed $1$.
6. Do not square the factor; orbital speed at the apsides follows $v\propto1/r$ from the area law, not the inverse-square force relation.
