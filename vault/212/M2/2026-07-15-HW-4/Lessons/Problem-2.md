# Time for a Solid Cylinder to Roll Down a Ramp

<!--
lesson-id: 212-M2-038
topic-code: MTH212.M2.38
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Rolling Acceleration](#find-the-rolling-acceleration)
- [Convert Height to Ramp Distance](#convert-height-to-ramp-distance)
- [Solve for the Descent Time](#solve-for-the-descent-time)
- [Recognize What Cancels](#recognize-what-cancels)
- [Summary](#summary)

## Prerequisites

- Newton's second law for translation and rotation
- The solid-cylinder moment of inertia $I=\frac12 mr^2$
- The rolling-without-slipping relation $a=\alpha r$
- Constant-acceleration kinematics from rest
- Right-triangle sine: $\sin\theta=\frac{h}{L}$

---

<a id="introduction"></a>
## Introduction

When an object **rolls without slipping** down an incline, gravity must produce both translational and rotational acceleration. The cue is that the problem asks for time, gives the ramp's vertical height rather than its length, and specifies the object's shape.

For a body with $I=kmr^2$, the reusable plan is

$$
a=\frac{g\sin\theta}{1+k},
\qquad
L=\frac{h}{\sin\theta},
\qquad
L=\frac12at^2.
$$

Here $a$ is the center-of-mass acceleration along the ramp, $L$ is the distance along the ramp, and $t$ is the elapsed time. We assume $h>0$, $g>0$, and $0<\theta<\pi/2$, so $\sin\theta$ is positive.

The mass and radius may appear in the givens, but for a fixed shape they cancel from the acceleration and therefore from the descent time.

---

<a id="find-the-rolling-acceleration"></a>
## Find the Rolling Acceleration

**Example:** Find the center-of-mass acceleration of a uniform solid cylinder rolling without slipping down a ramp inclined at angle $\theta$.

**Explanation**

Take downhill as positive. Translation along the ramp gives

$$
mg\sin\theta-f=ma.
$$

Static friction supplies the torque about the center:

$$
fr=I\alpha.
$$

Using $I=\frac12mr^2$ and $\alpha=a/r$,

$$
f=\frac{I\alpha}{r}
=\frac{\frac12mr^2(a/r)}{r}
=\frac12ma.
$$

Substitute this into the translation equation:

$$
mg\sin\theta-\frac12ma=ma
\quad\Longrightarrow\quad
a=\frac23g\sin\theta.
$$

```quiz
type: radio
id: p2-rolling-acceleration
content: |-
  A uniform solid cylinder rolls without slipping down a ramp at angle $\phi$. What is its center-of-mass acceleration?
options:
- id: a
  content: |-
    $g\sin\phi$
- id: b
  content: |-
    $\dfrac{2}{3}g\sin\phi$
  correct: true
- id: c
  content: |-
    $\dfrac{1}{2}g\sin\phi$
- id: d
  content: |-
    $\dfrac{3}{2}g\sin\phi$
```

---

<a id="convert-height-to-ramp-distance"></a>
## Convert Height to Ramp Distance

**Example:** A ramp has vertical height $h$ and incline angle $\theta$. Express the distance $L$ traveled along the ramp in terms of $h$ and $\theta$.

**Explanation**

In the ramp's right triangle, $h$ is opposite $\theta$ and $L$ is the hypotenuse. Therefore,

$$
\sin\theta=\frac{h}{L}
\quad\Longrightarrow\quad
L=\frac{h}{\sin\theta}.
$$

The kinematics equation must use the distance **along the ramp**, not the vertical height by itself.

```quiz
type: radio
id: p2-ramp-distance
content: |-
  A ramp has vertical height $H$ and incline angle $\phi$. What distance does an object travel from the top to the bottom along the ramp?
options:
- id: a
  content: |-
    $H\sin\phi$
- id: b
  content: |-
    $\dfrac{H}{\cos\phi}$
- id: c
  content: |-
    $\dfrac{H}{\sin\phi}$
  correct: true
- id: d
  content: |-
    $H\cos\phi$
```

---

<a id="solve-for-the-descent-time"></a>
## Solve for the Descent Time

**Example:** A uniform solid cylinder starts from rest at the top of a ramp of height $h$ and angle $\theta$. Find the time to reach the bottom.

**Explanation**

Because the cylinder starts from rest and its acceleration is constant,

$$
L=\frac12at^2.
$$

Insert the ramp distance and rolling acceleration before solving:

$$
\frac{h}{\sin\theta}
=\frac12\left(\frac23g\sin\theta\right)t^2
=\frac13g\sin\theta\,t^2.
$$

Now isolate $t^2$:

$$
t^2=\frac{3h}{g\sin^2\theta}.
$$

The square root step first gives two algebraic roots:

$$
t=\pm\sqrt{\frac{3h}{g\sin^2\theta}}.
$$

Elapsed time after release cannot be negative, so keep only the positive root:

$$
\boxed{t=\sqrt{\frac{3h}{g\sin^2\theta}}}.
$$

```quiz
type: radio
id: p2-descent-time
content: |-
  A uniform solid cylinder is released from rest on a ramp of vertical height $H$ and angle $\phi$. It rolls without slipping. How long does it take to reach the bottom?
options:
- id: a
  content: |-
    $\sqrt{\dfrac{3H}{g\sin^2\phi}}$
  correct: true
- id: b
  content: |-
    $\sqrt{\dfrac{3H}{g\sin\phi}}$
- id: c
  content: |-
    $\sqrt{\dfrac{2H}{g\sin^2\phi}}$
- id: d
  content: |-
    $\sqrt{\dfrac{3H}{g\cos^2\phi}}$
```

---

<a id="recognize-what-cancels"></a>
## Recognize What Cancels

**Example:** One solid cylinder has mass $M$ and radius $R$; another has mass $4M$ and radius $R/2$. Both roll without slipping from rest down the same ramp. Compare their descent times.

**Explanation**

For either cylinder,

$$
\frac{I}{mr^2}
=\frac{\frac12mr^2}{mr^2}
=\frac12.
$$

Thus both have $a=\frac23g\sin\theta$ and

$$
t=\sqrt{\frac{3h}{g\sin^2\theta}}.
$$

Changing mass or radius does not change the time because the dimensionless shape factor $I/(mr^2)$ remains $1/2$. This conclusion assumes both objects are uniform solid cylinders and roll without slipping.

```quiz
type: radio
id: p2-cancellation
content: |-
  Two uniform solid cylinders are released simultaneously from rest at the top of a ramp of height $h$ inclined at angle $\theta$. One cylinder has mass $M$ and radius $R$; the other has mass $4M$ and radius $R/2$. Both roll without slipping.

  How much time does the cylinder with mass $4M$ and radius $R/2$ take to reach the bottom?
options:
- id: a
  content: |-
    $\sqrt{\dfrac{h}{2g\sin\theta}}$
- id: b
  content: |-
    $\sqrt{\dfrac{h}{g\cos\theta}}$
- id: c
  content: |-
    $\sqrt{\dfrac{10h}{g\sin\theta\cos\theta}}$
- id: d
  content: |-
    $\sqrt{\dfrac{3h}{g\sin^2\theta}}$
  correct: true
```

---

<a id="summary"></a>
## Summary

For a uniform solid cylinder released from rest and rolling without slipping down a ramp:

1. Use translation, rotation, and $a=\alpha r$ to get $a=\frac23g\sin\theta$.
2. Convert vertical height to ramp distance: $L=h/\sin\theta$.
3. Substitute into $L=\frac12at^2$ and take the positive root:

$$
t=\sqrt{\frac{3h}{g\sin^2\theta}}.
$$

The main traps are using $h$ as the along-ramp distance, forgetting rotational inertia, or assuming that mass and radius affect the time even though they cancel for cylinders of the same shape.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
