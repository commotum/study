# Acceleration of a Yo-Yo Pulled at Its Axle

<!--
lesson-id: 212-M2-041
topic-code: MTH212.M2.41
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose Signs From the Rolling Direction](#choose-signs-from-the-rolling-direction)
- [Couple Translation and Rotation](#couple-translation-and-rotation)
- [Let the Equations Determine Friction](#let-the-equations-determine-friction)
- [Apply the Axle Radius](#apply-the-axle-radius)
- [Summary](#summary)

## Prerequisites

- Translational Newton's second law: $\sum F_x=Ma$
- Rotational Newton's second law about the center of mass: $\sum\tau_{\mathrm{CM}}=I\alpha$
- The uniform-cylinder moment of inertia: $I=\frac12MR^2$
- The rolling-without-slipping constraint

---

<a id="introduction"></a>
## Introduction

When a horizontal string pulls a rolling yo-yo at an inner axle, the pull affects both translation and rotation. The recognition cue is a force applied away from the center together with the condition **rolls without slipping**.

The reusable move is to write one translation equation and one torque equation, connect them with the signed rolling constraint, and eliminate the unknown friction force. Do not assume the direction of static friction in advance; its solved sign will tell you its actual direction.

With rightward and counterclockwise chosen as positive, the whole setup is

$$
T+f=Ma,
\qquad
Rf-rT=I\alpha,
\qquad
\alpha=-\frac{a}{R}.
$$

These are three equations for the three signed unknowns $a$, $f$, and $\alpha$. The goal is to isolate $a$ while treating $M$, $R$, $r$, $I$, and $T$ as known quantities.

Let the outer rolling radius be $R$, the inner axle radius be $r$, and the string tension be $T$. The model assumes a massless string, no slipping between string and axle, rolling without slipping at the floor, and negligible rolling resistance.

---

<a id="choose-signs-from-the-rolling-direction"></a>
## Choose Signs From the Rolling Direction

Take rightward translation as positive and counterclockwise rotation as positive. A yo-yo accelerating to the right rotates clockwise, so its angular acceleration is negative:

$$
\alpha=-\frac{a}{R}.
$$

For a string tangent to the top of the inner axle, the rightward tension produces a clockwise torque $-rT$. If friction $f$ is temporarily drawn to the right, its torque about the center is counterclockwise, $+Rf$.

**Example:** A wheel rolls to the right without slipping with center-of-mass acceleration $a$. If counterclockwise is positive, find $\alpha$.

**Explanation**

The contact point must remain instantaneously at rest relative to the floor. Rightward acceleration therefore pairs with clockwise angular acceleration:

$$
\alpha=-\frac{a}{R}.
$$

```quiz
type: radio
id: p5-signed-rolling
content: |-
  A disk rolls without slipping and accelerates to the right. Rightward and counterclockwise are defined as positive. Which constraint is correct?
options:
- id: a
  content: |-
    $\alpha=\dfrac{a}{R}$
- id: b
  content: |-
    $\alpha=-\dfrac{a}{R}$
  correct: true
- id: c
  content: |-
    $\alpha=aR$
- id: d
  content: |-
    $\alpha=-aR$
```

---

<a id="couple-translation-and-rotation"></a>
## Couple Translation and Rotation

Write the horizontal force equation without guessing the final direction of friction:

$$
T+f=Ma.
$$

The torque equation about the center of mass is

$$
Rf-rT=I\alpha.
$$

Insert $\alpha=-a/R$:

$$
Rf-rT=-\frac{Ia}{R}.
$$

Solve this equation for $f$:

$$
f=\frac{r}{R}T-\frac{I}{R^2}a.
$$

Substitute into translation:

$$
T+\frac{r}{R}T-\frac{I}{R^2}a=Ma.
$$

Collect the acceleration terms and isolate $a$:

$$
\boxed{a=\frac{T\left(1+\frac{r}{R}\right)}{M+\frac{I}{R^2}}}.
$$

**Example:** A rolling object has $I=kMR^2$ and is pulled at an inner axle of radius $r$. Express its acceleration in terms of $k$.

**Explanation**

Since $I/R^2=kM$,

$$
a=\frac{T\left(1+\frac{r}{R}\right)}{M+kM}
=\frac{T\left(1+\frac{r}{R}\right)}{M(1+k)}.
$$

```quiz
type: radio
id: p5-general-formula
content: |-
  A rolling body has $I=\frac34MR^2$ and is pulled to the right by a string tangent to the top of an axle of radius $R/2$. What is the magnitude of its center-of-mass acceleration?
options:
- id: a
  content: |-
    $\dfrac{3T}{2M}$
- id: b
  content: |-
    $\dfrac{6T}{7M}$
  correct: true
- id: c
  content: |-
    $\dfrac{4T}{7M}$
- id: d
  content: |-
    $\dfrac{7T}{6M}$
```

---

<a id="let-the-equations-determine-friction"></a>
## Let the Equations Determine Friction

The direction of static friction is not determined merely by the direction of the pull. Keep $f$ signed. A positive result means rightward friction; a negative result means the actual friction points left.

**Example:** For a uniform cylinder pulled at an axle of radius $r=R/4$, determine the sign of friction after finding $a=5T/(6M)$.

**Explanation**

Use

$$
f=\frac{r}{R}T-\frac{I}{R^2}a.
$$

With $r/R=1/4$ and $I/R^2=M/2$,

$$
\begin{aligned}
f
&=\frac14T-\frac12M\left(\frac{5T}{6M}\right) \\
&=\frac14T-\frac{5}{12}T \\
&=-\frac16T.
\end{aligned}
$$

The negative sign means the friction force is leftward. This is consistent with having initially drawn $f$ to the right and allowing the algebra to correct the assumed direction.

```quiz
type: radio
id: p5-friction-direction
content: |-
  In a signed force equation, friction was defined as positive to the right. Solving gives $f=-T/6$. What does this mean?
options:
- id: a
  content: |-
    Friction points left with magnitude $T/6$.
  correct: true
- id: b
  content: |-
    Friction points right with magnitude $T/6$.
- id: c
  content: |-
    Friction is impossible because a force cannot be negative.
- id: d
  content: |-
    The yo-yo must be slipping.
```

---

<a id="apply-the-axle-radius"></a>
## Apply the Axle Radius

**Example:** A yo-yo is a uniform cylinder of mass $M$ and outer radius $R$. A string tangent to the top of its inner axle of radius $R/4$ is pulled rightward with force magnitude $T$. The yo-yo rolls without slipping. Find the magnitude of its center-of-mass acceleration.

**Explanation**

For a uniform cylinder,

$$
I=\frac12MR^2.
$$

Substitute $r/R=1/4$ and $I/R^2=M/2$ into the coupled formula:

$$
\begin{aligned}
a
&=\frac{T\left(1+\frac14\right)}{M+\frac12M} \\
&=\frac{\frac54T}{\frac32M} \\
&=\boxed{\frac{5T}{6M}}.
\end{aligned}
$$

The numerator contains $1+r/R$ because the pull's clockwise torque and the clockwise rolling acceleration reinforce one another in the coupled equations. Treating the pull as if it passed through the center would miss the axle torque.

A quick reasonableness check is dimensional: the factors $1+r/R$ and $I/(MR^2)$ are dimensionless, so the result has the scale $T/M$, which has units of acceleration.

```quiz
type: radio
id: p5-homework-check
shuffle: true
content: |-
  A yo-yo has mass $M$, inner axle radius $R/4$, and outer radius $R$. A massless string wrapped around the axle is pulled to the right with force magnitude $T$.

  Assume the string does not slip on the axle, rolling friction is negligible, and the yo-yo rolls without slipping. Treat the yo-yo as a uniform cylinder of mass $M$ and radius $R$.

  What is the magnitude of the acceleration of its center of mass?
options:
- id: a
  content: |-
    $\dfrac{5T}{6M}$
  correct: true
- id: b
  content: |-
    $\dfrac{T}{M}$
- id: c
  content: |-
    $\dfrac{7T}{6M}$
- id: d
  content: |-
    $\dfrac{8T}{3M}$
```

---

<a id="summary"></a>
## Summary

For a yo-yo pulled rightward by a string tangent to the top of an inner axle:

1. Take rightward and counterclockwise as positive, so rolling right gives $\alpha=-a/R$.
2. Write $T+f=Ma$ and $Rf-rT=I\alpha$.
3. Eliminate the signed friction force:

$$
a=\frac{T\left(1+\frac{r}{R}\right)}{M+\frac{I}{R^2}}.
$$

4. For $I=\frac12MR^2$ and $r=R/4$,

$$
\boxed{a=\frac{5T}{6M}}.
$$

Before choosing an answer, check that the result has units of $T/M$. The main trap is assuming friction's direction or dropping the string's torque. Keep signs consistent and let the solved value of $f$ reveal its actual direction.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
