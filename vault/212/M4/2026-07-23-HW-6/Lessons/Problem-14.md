# Finding the Period of a Rod-and-Sphere Physical Pendulum

<!--
lesson-id: 212-M4-029
topic-code: MTH212.M4.29
-->

## Table of Contents

- [Introduction](#introduction)
- [Locate Each Center of Mass](#locate-each-center-of-mass)
- [Move Each Moment of Inertia to the Pivot](#move-each-moment-of-inertia-to-the-pivot)
- [Assemble the Period Formula](#assemble-the-period-formula)
- [Apply the Method to the Portland Pendulum](#apply-the-method-to-the-portland-pendulum)
- [Summary](#summary)

## Prerequisites

- Locate the center of mass of a uniform rod and a uniform sphere.
- Use $I_P=I_{\mathrm{cm}}+md^2$ to shift a moment of inertia to a parallel axis.
- Evaluate a formula containing squares and a square root.

---

<a id="introduction"></a>
## Introduction

The recognition cue is a pendulum made from extended objects whose masses are not concentrated at one point. A massive cable and a finite-size bob form a **physical pendulum**, so their mass distribution matters.

For small oscillations of a rigid assembly about a fixed pivot,

$$
T=2\pi\sqrt{\frac{I_P}{g\sum_i m_i d_i}},
$$

where

- $I_P=\sum_i I_{i,P}$ is the total moment of inertia about the pivot, and
- $d_i$ is the distance from the pivot to component $i$'s center of mass.

The denominator uses $\sum_i m_i d_i$ because

$$
M_{\mathrm{tot}}d_{\mathrm{cm}}=\sum_i m_i d_i.
$$

Use one component ledger for both sums:

| Component | Mass | Center distance | Moment about the pivot |
|---|---:|---:|---:|
| uniform rod | $M$ | $L/2$ | $\dfrac13 ML^2$ |
| uniform sphere at the rod's end | $m$ | $L+r$ | $\dfrac25mr^2+m(L+r)^2$ |

The sphere's center is at $L+r$, not at $L$: the rod reaches the sphere's surface, and the center lies another radius away.

---

<a id="locate-each-center-of-mass"></a>
## Locate Each Center of Mass

**Example:** A uniform rod has length $L=6.0\ \mathrm{m}$ and mass $M=4.0\ \mathrm{kg}$. A uniform sphere of radius $r=0.50\ \mathrm{m}$ and mass $m=2.0\ \mathrm{kg}$ is attached to its lower end. Find the mass-distance sum $\sum_i m_i d_i$.

**Explanation**

The rod's center is halfway down the rod:

$$
d_{\mathrm{rod}}=\frac{L}{2}=3.0\ \mathrm{m}.
$$

The sphere's center is one radius beyond the rod's lower end:

$$
d_{\mathrm{sphere}}=L+r=6.5\ \mathrm{m}.
$$

Therefore,

$$
\begin{aligned}
\sum_i m_i d_i
&=M\frac{L}{2}+m(L+r)\\
&=(4.0)(3.0)+(2.0)(6.5)\\
&=25\ \mathrm{kg\,m}.
\end{aligned}
$$

```quiz
type: radio
id: p14-q1
content: |-
  A uniform rod has $L=4.0\ \mathrm{m}$ and $M=6.0\ \mathrm{kg}$. A uniform sphere with $r=1.0\ \mathrm{m}$ and $m=2.0\ \mathrm{kg}$ is attached to its end. What is $\sum_i m_i d_i$ about the pivot at the rod's top?
options:
- id: p14-q1-a
  content: |-
    $8\ \mathrm{kg\,m}$
- id: p14-q1-b
  content: |-
    $14\ \mathrm{kg\,m}$
- id: p14-q1-c
  content: |-
    $20\ \mathrm{kg\,m}$
- id: p14-q1-d
  content: |-
    $22\ \mathrm{kg\,m}$
  correct: true
- id: p14-q1-e
  content: |-
    $34\ \mathrm{kg\,m}$
```

---

<a id="move-each-moment-of-inertia-to-the-pivot"></a>
## Move Each Moment of Inertia to the Pivot

**Example:** Find the total pivot moment of inertia for the $6.0\ \mathrm{m}$ rod and $0.50\ \mathrm{m}$-radius sphere from the previous section.

**Explanation**

Every contribution must use the same axis: the pendulum's pivot.

For the rod,

$$
\begin{aligned}
I_{\mathrm{rod},P}
&=I_{\mathrm{rod,cm}}+M\left(\frac L2\right)^2\\
&=\frac{1}{12}ML^2+M\left(\frac L2\right)^2\\
&=\frac13ML^2\\
&=\frac13(4.0)(6.0)^2\\
&=48.0\ \mathrm{kg\,m^2}.
\end{aligned}
$$

For the sphere, shift its center-of-mass moment through the distance $L+r$:

$$
\begin{aligned}
I_{\mathrm{sphere},P}
&=I_{\mathrm{sphere,cm}}+m(L+r)^2\\
&=\frac25mr^2+m(L+r)^2\\
&=\frac25(2.0)(0.50)^2+(2.0)(6.5)^2\\
&=84.7\ \mathrm{kg\,m^2}.
\end{aligned}
$$

Add the contributions:

$$
I_P=48.0+84.7=132.7\ \mathrm{kg\,m^2}.
$$

```quiz
type: radio
id: p14-q2
content: |-
  A uniform rod has $L=4.0\ \mathrm{m}$ and $M=6.0\ \mathrm{kg}$. A uniform sphere with $r=1.0\ \mathrm{m}$ and $m=2.0\ \mathrm{kg}$ is attached to its end. What is the assembly's moment of inertia about the pivot at the rod's top?
options:
- id: p14-q2-a
  content: |-
    $32.8\ \mathrm{kg\,m^2}$
- id: p14-q2-b
  content: |-
    $58.8\ \mathrm{kg\,m^2}$
- id: p14-q2-c
  content: |-
    $64.8\ \mathrm{kg\,m^2}$
- id: p14-q2-d
  content: |-
    $82.0\ \mathrm{kg\,m^2}$
- id: p14-q2-e
  content: |-
    $82.8\ \mathrm{kg\,m^2}$
  correct: true
```

The nearby answers encode common mistakes: using a center-of-mass moment without shifting it, using $L$ instead of $L+r$, or omitting the sphere's own $\frac25mr^2$.

---

<a id="assemble-the-period-formula"></a>
## Assemble the Period Formula

**Example:** The rod-and-sphere assembly from the first two sections has

$$
I_P=132.7\ \mathrm{kg\,m^2}
\quad\text{and}\quad
\sum_i m_i d_i=25\ \mathrm{kg\,m}.
$$

Find its small-angle period using $g=9.81\ \mathrm{m/s^2}$.

**Explanation**

Substitute the two assembled quantities first:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{I_P}{g\sum_i m_i d_i}}\\
&=2\pi\sqrt{
\frac{132.7}
{(9.81)(25)}
}.
\end{aligned}
$$

Evaluate from the inside out:

$$
\begin{aligned}
\frac{I_P}{g\sum_i m_i d_i}
&\approx 0.5411\ \mathrm{s^2},\\
\sqrt{0.5411\ \mathrm{s^2}}
&\approx 0.7356\ \mathrm{s},\\
T&=2\pi(0.7356\ \mathrm{s})
\approx 4.62\ \mathrm{s}.
\end{aligned}
$$

The units provide a quick check:

$$
\frac{\mathrm{kg\,m^2}}
{(\mathrm{m/s^2})(\mathrm{kg\,m})}
=\mathrm{s^2}.
$$

The square root therefore has units of seconds.

```quiz
type: radio
id: p14-q3
content: |-
  A composite physical pendulum has $I_P=72\ \mathrm{kg\,m^2}$ and $\sum_i m_i d_i=18\ \mathrm{kg\,m}$. Using $g=9.81\ \mathrm{m/s^2}$, what is its small-angle period?
options:
- id: p14-q3-a
  content: |-
    about $0.408\ \mathrm{s}$
- id: p14-q3-b
  content: |-
    about $0.639\ \mathrm{s}$
- id: p14-q3-c
  content: |-
    about $4.01\ \mathrm{s}$
  correct: true
- id: p14-q3-d
  content: |-
    about $6.28\ \mathrm{s}$
- id: p14-q3-e
  content: |-
    about $25.2\ \mathrm{s}$
```

---

<a id="apply-the-method-to-the-portland-pendulum"></a>
## Apply the Method to the Portland Pendulum

**Example:** Model the Portland pendulum as a thin uniform rod of length $L=27\ \mathrm{m}$ and mass $M=400\ \mathrm{kg}$ with a uniform spherical bob of radius $r=1.5\ \mathrm{m}$ and mass $m=100\ \mathrm{kg}$ attached to its end. Find its small-angle period.

**Explanation**

First inventory the centers:

$$
d_{\mathrm{rod}}=\frac{L}{2}=13.5\ \mathrm{m},
\qquad
d_{\mathrm{sphere}}=L+r=28.5\ \mathrm{m}.
$$

The restoring mass-distance sum is

$$
\begin{aligned}
\sum_i m_i d_i
&=M\frac L2+m(L+r)\\
&=(400)(13.5)+(100)(28.5)\\
&=8250\ \mathrm{kg\,m}.
\end{aligned}
$$

Now calculate both pivot moments:

$$
\begin{aligned}
I_{\mathrm{rod},P}
&=\frac13ML^2
=\frac13(400)(27)^2
=97\,200\ \mathrm{kg\,m^2},\\
I_{\mathrm{sphere},P}
&=\frac25mr^2+m(L+r)^2\\
&=\frac25(100)(1.5)^2+(100)(28.5)^2\\
&=81\,315\ \mathrm{kg\,m^2}.
\end{aligned}
$$

Thus,

$$
I_P=97\,200+81\,315
=178\,515\ \mathrm{kg\,m^2}.
$$

Finally,

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{178\,515}{(9.81)(8250)}}\\
&\approx 9.33\ \mathrm{s}.
\end{aligned}
$$

This model assumes a rigid rod-and-sphere assembly, a fixed pivot, and small oscillation angles.

```quiz
type: radio
id: p14-q4
content: |-
  In Portland at the Oregon Convention Center is one of the longest pendulums in the world (in terms of both cable length and oscillation period).

  It has a cable of length $L=27\ \mathrm{m}$ (about as tall as a building with 8 floors) and a spherical bob of mass $m=100\ \mathrm{kg}$ and radius $r=1.5\ \mathrm{m}$ attached to the end of the cable of mass $M=400\ \mathrm{kg}$.

  A more accurate model of the pendulum would be as a uniform sphere (the bob) attached to the end of a thin uniform rod (the cable).

  Under this model, what is the period of the pendulum?
options:
- id: p14-q4-a
  content: |-
    about 9-10 seconds
  correct: true
- id: p14-q4-b
  content: |-
    about 10-11 seconds
- id: p14-q4-c
  content: |-
    about 11-12 seconds
- id: p14-q4-d
  content: |-
    about 12-13 seconds
```

The computed value $9.33\ \mathrm{s}$ matches **about 9-10 seconds**.

---

<a id="summary"></a>
## Summary

When a pendulum contains several extended masses:

1. Locate every center of mass: here $d_{\mathrm{rod}}=L/2$ and $d_{\mathrm{sphere}}=L+r$.
2. Put every moment of inertia about the pivot: here
   $I_{\mathrm{rod},P}=\frac13ML^2$ and
   $I_{\mathrm{sphere},P}=\frac25mr^2+m(L+r)^2$.
3. Add the contributions and use
   $T=2\pi\sqrt{I_P/(g\sum_i m_i d_i)}$.
4. Check that the expression inside the square root has units of $\mathrm{s^2}$.

The main trap is using $L$ as the sphere-center distance or omitting one of the parallel-axis terms.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
