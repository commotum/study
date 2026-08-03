# Bead on a Frictionless Cone

<!--
lesson-id: 212-M1-065
topic-code: MTH212.M1.65
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Forces and Axes](#choose-the-forces-and-axes)
- [Resolve the Normal Force](#resolve-the-normal-force)
- [Eliminate the Normal Force](#eliminate-the-normal-force)
- [Use the Cone Geometry](#use-the-cone-geometry)
- [Find and Interpret the Period](#find-and-interpret-the-period)
- [Summary](#summary)

## Prerequisites

- Draw a free-body diagram using only real forces.
- Resolve an angled force into components.
- Use $\sum F_r = mv^2/r$ for uniform circular motion.
- Use $T = 2\pi r/v$ for one circular orbit.

---

<a id="introduction"></a>
## Introduction

A bead sliding without friction around an inverted cone has only two real forces: gravity and the normal force from the cone. The recognition cue is that the bead stays at a constant height while moving in a circle, so the vertical forces balance and the inward radial force supplies centripetal acceleration.

The useful move is to split the angled normal force into vertical and radial components, divide the two force equations to eliminate $N$, and then use tangent as opposite over adjacent in the cone's side-view triangle.

![](<../Source/Images/problem-5-inverted-cone.png>)

---

<a id="choose-the-forces-and-axes"></a>
## Choose the Forces and Axes

**Example:** A bead moves in a horizontal circle on a frictionless cone. Which forces belong on the free-body diagram?

**Explanation**

Because the surface is frictionless, the bead has no friction force. The only real forces are:

- $mg$ downward.
- $N$ perpendicular to the cone surface, pointing up and inward.

Use a vertical $y$-axis and an inward radial $r$-axis. Do not draw a separate "centripetal force"; centripetal acceleration is caused by the inward component of the real forces.

![](<../Source/Images/problem-5-free-body-diagram.png>)

```quiz
type: radio
id: q-p5-1
shuffle: true
content: |-
  A bead slides without friction around the inside of a cone at constant height. Which force list belongs on the bead's free-body diagram?
options:
- id: q-p5-1-a
  content: |-
    $mg$ downward and $N$ perpendicular to the cone surface, pointing up and inward.
  correct: true
- id: q-p5-1-b
  content: |-
    $mg$ downward, $N$ upward, and a separate centripetal force inward.
- id: q-p5-1-c
  content: |-
    $mg$ downward and friction pointing inward.
- id: q-p5-1-d
  content: |-
    $mg$ downward and velocity pointing inward.
```

---

<a id="resolve-the-normal-force"></a>
## Resolve the Normal Force

**Example:** Suppose $\theta$ is the angle between $N$ and the inward radial axis. Write the vertical and radial force equations.

**Explanation**

With $\theta$ measured from the radial axis, the radial component is adjacent to the angle:

$$
N_r = N\cos\theta
$$

The vertical component is opposite the angle:

$$
N_y = N\sin\theta
$$

The bead has no vertical acceleration, so the vertical forces balance:

$$
\sum F_y = 0 = N\sin\theta - mg
$$

The bead does have inward radial acceleration, so the radial equation is:

$$
\sum F_r = \frac{mv^2}{r} = N\cos\theta
$$

```quiz
type: radio
id: q-p5-2
shuffle: true
content: |-
  If $\theta$ is measured between $N$ and the inward radial axis, which pair of force equations is correct?
options:
- id: q-p5-2-a
  content: |-
    $N\sin\theta = mg$ and $N\cos\theta = \dfrac{mv^2}{r}$
  correct: true
- id: q-p5-2-b
  content: |-
    $N\cos\theta = mg$ and $N\sin\theta = \dfrac{mv^2}{r}$
- id: q-p5-2-c
  content: |-
    $N\sin\theta + mg = 0$ and $N\cos\theta = 0$
- id: q-p5-2-d
  content: |-
    $N = mg$ and $mg = \dfrac{mv^2}{r}$
```

---

<a id="eliminate-the-normal-force"></a>
## Eliminate the Normal Force

**Example:** Use

$$
N\sin\theta = mg
$$

and

$$
N\cos\theta = \frac{mv^2}{r}
$$

to solve for a relationship involving $v$ and $\theta$.

**Explanation**

Divide the vertical equation by the radial equation so that $N$ cancels:

$$
\frac{N\sin\theta}{N\cos\theta}
=
\frac{mg}{mv^2/r}
$$

The left side is $\tan\theta$. On the right side, $m$ cancels:

$$
\tan\theta = \frac{gr}{v^2}
$$

This division is useful because the unknown normal force and the mass both cancel. It also creates $\tan\theta$, which can be matched to the cone's side-view triangle.

```quiz
type: radio
id: q-p5-3
shuffle: true
content: |-
  Given $N\sin\theta = mg$ and $N\cos\theta = \dfrac{mv^2}{r}$, what equation do you get after dividing the first equation by the second?
options:
- id: q-p5-3-a
  content: |-
    $\tan\theta = \dfrac{gr}{v^2}$
  correct: true
- id: q-p5-3-b
  content: |-
    $\tan\theta = \dfrac{v^2}{gr}$
- id: q-p5-3-c
  content: |-
    $\cot\theta = \dfrac{gr}{v^2}$
- id: q-p5-3-d
  content: |-
    $\tan\theta = \dfrac{Nr}{mv^2}$
```

---

<a id="use-the-cone-geometry"></a>
## Use the Cone Geometry

**Example:** The cone has radius $r$ at the bead's height and vertical height $h$. Use the cone shape to find $v$.

**Explanation**

The side view makes a right triangle. With the same angle convention used in the force diagram, the side opposite $\theta$ is the horizontal radius $r$, and the side adjacent to $\theta$ is the vertical height $h$. Therefore,

$$
\tan\theta = \frac{r}{h}
$$

Set this equal to the force result:

$$
\frac{r}{h} = \frac{gr}{v^2}
$$

Cancel $r$ and solve for $v$:

$$
\frac{1}{h} = \frac{g}{v^2}
$$

$$
v^2 = gh
$$

$$
v = \sqrt{gh}
$$

Since $v$ is a speed, use the positive square root. The mass cancels because both force equations contain $m$. The radius cancels at this stage because a wider circle also changes the cone angle.

```quiz
type: radio
id: q-p5-4
shuffle: true
content: |-
  For the same cone setup, $\tan\theta = \dfrac{r}{h}$ and $\tan\theta = \dfrac{gr}{v^2}$. What is $v$?
options:
- id: q-p5-4-a
  content: |-
    $\sqrt{gh}$
  correct: true
- id: q-p5-4-b
  content: |-
    $\sqrt{gr}$
- id: q-p5-4-c
  content: |-
    $\sqrt{\dfrac{gr}{h}}$
- id: q-p5-4-d
  content: |-
    $gh$
```

---

<a id="find-and-interpret-the-period"></a>
## Find and Interpret the Period

**Example:** Use $v=\sqrt{gh}$ to find the orbital period and decide how to decrease it.

**Explanation**

One orbit covers the circumference $2\pi r$, so

$$
T = \frac{2\pi r}{v}
$$

Substitute $v=\sqrt{gh}$:

$$
T = \frac{2\pi r}{\sqrt{gh}}
$$

This expression shows the parameter effects directly:

- Increasing $r$ increases $T$.
- Increasing $h$ decreases $T$ because $h$ is under the square root in the denominator.

So the two symbolic ways to decrease the orbital period are to decrease $r$ or increase $h$.

```quiz
type: radio
id: q-p5-5
shuffle: true
content: |-
  For $T = \dfrac{2\pi r}{\sqrt{gh}}$, which pair of changes would both decrease the orbital period?
options:
- id: q-p5-5-a
  content: |-
    Decrease $r$ and increase $h$.
  correct: true
- id: q-p5-5-b
  content: |-
    Increase $r$ and increase $h$.
- id: q-p5-5-c
  content: |-
    Decrease $r$ and decrease $h$.
- id: q-p5-5-d
  content: |-
    Increase $r$ and decrease $h$.
```

---

<a id="summary"></a>
## Summary

When a bead moves at constant height on a frictionless cone, draw only $mg$ and $N$. Choose vertical and inward radial axes, and check where $\theta$ is measured before assigning sine and cosine components. If $\theta$ is measured from the radial axis, then

$$
N\sin\theta = mg,
\qquad
N\cos\theta = \frac{mv^2}{r}
$$

Divide the equations to eliminate $N$:

$$
\tan\theta = \frac{gr}{v^2}
$$

Then use the side-view triangle, where $\tan\theta=r/h$, to get $v=\sqrt{gh}$, and substitute into $T=2\pi r/v$:

$$
T = \frac{2\pi r}{\sqrt{gh}}
$$

The main trap is treating "centripetal force" as an extra force instead of using the inward component of the normal force.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
