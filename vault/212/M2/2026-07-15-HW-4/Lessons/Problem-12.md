# Angular Momentum About a Combined Center of Mass

<!--
lesson-id: 212-M2-048
topic-code: MTH212.M2.48
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Easier Instant](#choose-the-easier-instant)
- [Locate the Combined Center of Mass](#locate-the-combined-center-of-mass)
- [Measure Position From the New Origin](#measure-position-from-the-new-origin)
- [Use the Cross Product for Magnitude and Direction](#use-the-cross-product-for-magnitude-and-direction)
- [Ignore Position Components Parallel to Momentum](#ignore-position-components-parallel-to-momentum)
- [Summary](#summary)

## Prerequisites

- Compute a center-of-mass coordinate with a mass-weighted average.
- Write linear momentum as $\vec p=m\vec v$.
- Use $\vec L=\vec r\times\vec p$ for a particle's angular momentum about an origin.
- Use the right-hand rule for Cartesian unit vectors.

---

<a id="introduction"></a>
## Introduction

When a collision problem asks for angular momentum **about the combined center of mass**, use this cue-and-rule sequence:

1. Evaluate the angular momentum at the easiest instant, often just before impact.
2. Find the combined center of mass and use it as the origin.
3. Measure each moving object's position from that origin.
4. Compute $\vec L=\sum \vec r_i\times\vec p_i$ in the stated order.

For an isolated collision, total angular momentum about the system's center of mass is conserved. Sticking changes how the system moves, but it does not change the total angular momentum during the collision.

---

<a id="choose-the-easier-instant"></a>
## Choose the Easier Instant

**Example:** A stationary rod is struck by a nonspinning ball. Which instant makes the system's angular momentum easiest to calculate: just before or just after the ball sticks?

**Explanation**

Use the instant just before impact. The rod is at rest, so every part of it has zero linear momentum and contributes zero angular momentum. The ball is not spinning, so it contributes only orbital angular momentum:

$$
\vec L_{\text{before}}=\vec r_{\text{ball}}\times\vec p_{\text{ball}}.
$$

Conservation then gives

$$
\vec L_{\text{after}}=\vec L_{\text{before}}.
$$

There is no need to find the final angular speed or moment of inertia.

```quiz
type: radio
id: p12-q1
content: |-
  A stationary rod is struck by a nonspinning particle in an isolated collision. Why is the instant just before impact convenient for finding the total angular momentum about the system's center of mass?
options:
- id: p12-q1-a
  content: |-
    Only the moving particle has nonzero momentum, and the total angular momentum is conserved through the collision.
  correct: true
- id: p12-q1-b
  content: |-
    Angular momentum is always zero before objects touch.
- id: p12-q1-c
  content: |-
    The particle's linear momentum is destroyed when it sticks.
- id: p12-q1-d
  content: |-
    The rod contributes angular momentum even though it is stationary.
- id: p12-q1-e
  content: |-
    Sticking guarantees that the final angular speed is zero.
```

---

<a id="locate-the-combined-center-of-mass"></a>
## Locate the Combined Center of Mass

**Example:** Put the center of a uniform rod of mass $m$ at $y=0$. A ball of mass $m/2$ has its center at the rod's lower end, $y=-L/2$. Find the vertical coordinate of the combined center of mass.

**Explanation**

Use the mass-weighted average:

$$
y_{\text{CM}}
=\frac{m(0)+(m/2)(-L/2)}{m+m/2}
=-\frac{L}{6}.
$$

The combined center of mass lies below the rod's center, toward the ball, but it does not lie at the ball's center.

```quiz
type: radio
id: p12-q2
content: |-
  A rod of mass $M$ has its center at $y=0$. A particle of mass $M$ is at $y=-D$. What is the combined center-of-mass coordinate?
options:
- id: p12-q2-a
  content: |-
    $-2D$
- id: p12-q2-b
  content: |-
    $-D$
- id: p12-q2-c
  content: |-
    $-\dfrac{D}{2}$
  correct: true
- id: p12-q2-d
  content: |-
    $0$
- id: p12-q2-e
  content: |-
    $\dfrac{D}{2}$
```

---

<a id="measure-position-from-the-new-origin"></a>
## Measure Position From the New Origin

**Example:** In the rod-ball system above, find the ball's vertical position relative to the combined center of mass.

**Explanation**

Subtract the origin coordinate from the object's coordinate:

$$
y_{\text{rel}}
=y_{\text{ball}}-y_{\text{CM}}
=-\frac{L}{2}-\left(-\frac{L}{6}\right)
=-\frac{L}{3}.
$$

The ball is therefore $L/3$ below the new origin. A common mistake is to use $L/2$, which is the distance from the rod's center rather than from the combined center of mass.

```quiz
type: radio
id: p12-q3
content: |-
  A rod of mass $M$ has its center at $y=0$, and a particle of mass $M$ is at $y=-L/2$. What is the particle's vertical coordinate relative to the combined center of mass?
options:
- id: p12-q3-a
  content: |-
    $-\dfrac{L}{2}$
- id: p12-q3-b
  content: |-
    $-\dfrac{L}{4}$
  correct: true
- id: p12-q3-c
  content: |-
    $0$
- id: p12-q3-d
  content: |-
    $\dfrac{L}{4}$
- id: p12-q3-e
  content: |-
    $\dfrac{L}{2}$
```

---

<a id="use-the-cross-product-for-magnitude-and-direction"></a>
## Use the Cross Product for Magnitude and Direction

**Example:** The ball of mass $m/2$ is $L/3$ below the origin and moves right with speed $v$. Find its angular momentum about the origin.

**Explanation**

The relevant vectors are

$$
\vec r_{\text{ball}}=-\frac{L}{3}\,\hat y,
\qquad
\vec p_{\text{ball}}=\frac{m}{2}v\,\hat x.
$$

Keep the order $\vec r\times\vec p$. Since $\hat y\times\hat x=-\hat z$,

$$
\begin{aligned}
\vec L
&=\left(-\frac{L}{3}\hat y\right)
\times\left(\frac{mv}{2}\hat x\right)\\
&=-\frac{mLv}{6}(\hat y\times\hat x)\\
&=\frac{1}{6}mLv\,\hat z.
\end{aligned}
$$

A point below the origin moving right tends to rotate counterclockwise, which is $+\hat z$ when $+z$ points out of the screen.

For vectors in the $xy$-plane, the same sign check can be written in component form:

$$
L_z=xp_y-yp_x.
$$

Here $p_y=0$, $y=-L/3$, and $p_x=mv/2$, so $L_z=-(-L/3)(mv/2)>0$. This is a quick safeguard against reversing the cross product.

```quiz
type: radio
id: p12-q4
content: |-
  A particle is at $\vec r=-d\,\hat y$ and has momentum $\vec p=p\,\hat x$, where $d,p>0$. What is its angular momentum about the origin?
options:
- id: p12-q4-a
  content: |-
    $dp\,\hat x$
- id: p12-q4-b
  content: |-
    $-dp\,\hat x$
- id: p12-q4-c
  content: |-
    $dp\,\hat z$
  correct: true
- id: p12-q4-d
  content: |-
    $-dp\,\hat z$
- id: p12-q4-e
  content: |-
    $\vec 0$
```

---

<a id="ignore-position-components-parallel-to-momentum"></a>
## Ignore Position Components Parallel to Momentum

**Example:** The ball has radius $r$, so its center is horizontally displaced from the rod at contact. Why does $r$ not appear in the angular momentum?

**Explanation**

At contact, take the rod's center as $(0,0)$. The ball's center is then at $(-r,-L/2)$, so the full combined center of mass is

$$
\begin{aligned}
x_{\text{CM}}&=\frac{m(0)+(m/2)(-r)}{m+m/2}=-\frac r3,\\
y_{\text{CM}}&=-\frac L6.
\end{aligned}
$$

Therefore, the ball's position relative to the combined center of mass is

$$
\vec r_{\text{ball}}
=\left(-r+\frac r3\right)\hat x
+\left(-\frac L2+\frac L6\right)\hat y
=-\frac{2r}{3}\hat x-\frac L3\hat y.
$$

Because its momentum is parallel to $\hat x$,

$$
\begin{aligned}
\vec r_{\text{ball}}\times\vec p_{\text{ball}}
&=\left(-\frac{2r}{3}\hat x-\frac{L}{3}\hat y\right)
\times\left(\frac{mv}{2}\hat x\right)\\
&=-\frac{rmv}{3}(\hat x\times\hat x)
-\frac{mLv}{6}(\hat y\times\hat x).
\end{aligned}
$$

The first term is zero because $\hat x\times\hat x=\vec 0$. Only the perpendicular distance $L/3$ matters, so the ball's radius cancels from the result.

**Final check:**

![](<../Source/2026-07-15-HW-4/Images/rod-ball-inelastic-collision.png>)

```quiz
type: radio
id: p12-q5
shuffle: true
content: |-
  A thin uniform rod of mass $m$ and length $L$ is initially at rest in outer space. A nonspinning uniform ball of mass $m/2$ and radius $r$ strikes one end of the rod with speed $v$ and sticks to it.

  Use a right-handed coordinate system with $+x$ to the right, $+y$ upward, and $+z$ out of the screen. Place the origin at the center of mass of the combined system.

  What is the angular momentum of the combined system about this origin after the collision?
options:
- id: p12-q5-a
  content: |-
    $-\dfrac{1}{6}mrv\,\hat{z}$
- id: p12-q5-b
  content: |-
    $\dfrac{1}{6}mLv\,\hat{z}$
  correct: true
```

---

<a id="summary"></a>
## Summary

For a collision about the combined center of mass:

1. Use conservation to evaluate angular momentum at the easiest instant.
2. Find the combined center of mass with a weighted average.
3. Re-measure the moving object's position from that origin.
4. Compute $\vec r\times\vec p$, not $\vec p\times\vec r$.
5. Keep only the position component perpendicular to the momentum.

Here the ball is $L/3$ below the combined center of mass and moves to the right, so

$$
\boxed{\vec L_{\text{after}}=\frac{1}{6}mLv\,\hat z}.
$$

The main traps are using $L/2$ instead of $L/3$, reversing the cross-product order, and including the radius even though its displacement is parallel to the momentum.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
