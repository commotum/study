# Total Acceleration From Radial and Tangential Components

<!--
lesson-id: 212-M1-057
topic-code: MTH212.M1.57
-->

## Table of Contents

- [Introduction](#introduction)
- [Combine Perpendicular Acceleration Components](#combine-perpendicular-acceleration-components)
- [Find the Components First](#find-the-components-first)
- [Keep Direction Separate From Magnitude](#keep-direction-separate-from-magnitude)
- [Apply the Assignment Values](#apply-the-assignment-values)
- [Summary](#summary)

## Prerequisites

- Use radial and tangential axes for circular motion.
- Resolve weight into $mg\cos\theta$ and $mg\sin\theta$ along chosen axes.
- Use Newton's second law component by component.
- Evaluate square roots and round to the requested significant figures.

---

<a id="introduction"></a>
## Introduction

When a circular-motion problem asks for the **magnitude of the acceleration** using $r$-$t$ axes, look for two perpendicular components:

$$
\vec a = a_r\hat r + a_t\hat t
$$

The radial component points along the string or radius, and the tangential component is perpendicular to it. The cue is the word **magnitude**: the answer should be the length of the acceleration vector, not just one component.

Because the $r$ and $t$ directions are perpendicular, the total acceleration magnitude is

$$
|\vec a|=\sqrt{a_r^2+a_t^2}
$$

Use the positive square root and keep the acceleration unit, usually $\mathrm{m}/\mathrm{s}^2$. Do not add $a_r+a_t$ unless the accelerations point along the same line.

---

<a id="combine-perpendicular-acceleration-components"></a>
## Combine Perpendicular Acceleration Components

**Example:** A particle has radial acceleration $a_r=12\ \mathrm{m}/\mathrm{s}^2$ and tangential acceleration $a_t=5\ \mathrm{m}/\mathrm{s}^2$. Find the magnitude of its acceleration.

**Explanation**

The radial and tangential directions are perpendicular, so treat the two acceleration components like the legs of a right triangle:

$$
\begin{aligned}
|\vec a| &= \sqrt{a_r^2+a_t^2} \\
&= \sqrt{(12)^2+(5)^2} \\
&= \sqrt{144+25} \\
&= \sqrt{169} \\
&= 13\ \mathrm{m}/\mathrm{s}^2
\end{aligned}
$$

```quiz
type: radio
id: problem-5-q1
shuffle: true
content: |-
  A particle has $a_r=8\ \mathrm{m}/\mathrm{s}^2$ and $a_t=6\ \mathrm{m}/\mathrm{s}^2$. What is $|\vec a|$?
options:
- id: a
  content: |-
    $2\ \mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $10\ \mathrm{m}/\mathrm{s}^2$
  correct: true
  feedback: |-
    Use $\sqrt{8^2+6^2}=\sqrt{100}=10$.
- id: c
  content: |-
    $14\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    That adds the components directly, but the directions are perpendicular.
- id: d
  content: |-
    $\sqrt{14}\ \mathrm{m}/\mathrm{s}^2$
- id: e
  content: |-
    $48\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="find-the-components-first"></a>
## Find the Components First

**Example:** A ball on a string has $T=2.0\ \mathrm{N}$, $m=0.50\ \mathrm{kg}$, and $\theta=30^\circ$. With the $r$-axis inward and the $t$-axis perpendicular to the string, find the total acceleration magnitude.

**Explanation**

First write the component accelerations from the force equations:

$$
\begin{aligned}
a_r &= \frac{T}{m}+g\cos\theta \\
a_t &= g\sin\theta
\end{aligned}
$$

Now substitute the values:

$$
\begin{aligned}
a_r &= \frac{2.0}{0.50}+9.8\cos(30^\circ) \\
&= 4.0+8.49 \\
&= 12.49\ \mathrm{m}/\mathrm{s}^2
\end{aligned}
$$

$$
\begin{aligned}
a_t &= 9.8\sin(30^\circ) \\
&= 4.90\ \mathrm{m}/\mathrm{s}^2
\end{aligned}
$$

Then combine the perpendicular components:

$$
\begin{aligned}
|\vec a| &= \sqrt{(12.49)^2+(4.90)^2} \\
&= 13.42\ \mathrm{m}/\mathrm{s}^2
\end{aligned}
$$

To two significant figures, $|\vec a|=13\ \mathrm{m}/\mathrm{s}^2$.

```quiz
type: radio
id: problem-5-q2
shuffle: true
content: |-
  A ball on a string has $T=1.8\ \mathrm{N}$, $m=0.60\ \mathrm{kg}$, and $\theta=20^\circ$. Use $a_r=\frac{T}{m}+g\cos\theta$ and $a_t=g\sin\theta$.

  What is the total acceleration magnitude to two significant figures?
options:
- id: a
  content: |-
    $3.4\ \mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $12\ \mathrm{m}/\mathrm{s}^2$
- id: c
  content: |-
    $13\ \mathrm{m}/\mathrm{s}^2$
  correct: true
  feedback: |-
    $a_r=1.8/0.60+9.8\cos20^\circ=12.21$, $a_t=9.8\sin20^\circ=3.35$, so $|\vec a|=12.66\approx13$.
- id: d
  content: |-
    $16\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    That is close to adding $a_r+a_t$ instead of using perpendicular components.
- id: e
  content: |-
    $160\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="keep-direction-separate-from-magnitude"></a>
## Keep Direction Separate From Magnitude

**Example:** A ball has $a_r=10\ \mathrm{m}/\mathrm{s}^2$ and $a_t=-3\ \mathrm{m}/\mathrm{s}^2$ for a particular choice of positive tangential direction. Find the magnitude of the acceleration.

**Explanation**

The sign of $a_t$ tells which way the tangential component points. The magnitude of the total acceleration is still nonnegative:

$$
\begin{aligned}
|\vec a| &= \sqrt{a_r^2+a_t^2} \\
&= \sqrt{(10)^2+(-3)^2} \\
&= \sqrt{109} \\
&= 10.4\ \mathrm{m}/\mathrm{s}^2
\end{aligned}
$$

The negative sign does not make the components subtract inside the magnitude formula.

```quiz
type: radio
id: problem-5-q3
shuffle: true
content: |-
  For a chosen $t$-axis, a particle has $a_r=7.0\ \mathrm{m}/\mathrm{s}^2$ and $a_t=-2.0\ \mathrm{m}/\mathrm{s}^2$. What is the acceleration magnitude?
options:
- id: a
  content: |-
    $5.0\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    That subtracts the components directly. Perpendicular components combine by squaring.
- id: b
  content: |-
    $7.3\ \mathrm{m}/\mathrm{s}^2$
  correct: true
  feedback: |-
    $\sqrt{(7.0)^2+(-2.0)^2}=\sqrt{53}=7.3$.
- id: c
  content: |-
    $9.0\ \mathrm{m}/\mathrm{s}^2$
- id: d
  content: |-
    $\sqrt{45}\ \mathrm{m}/\mathrm{s}^2$
- id: e
  content: |-
    $49\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="apply-the-assignment-values"></a>
## Apply the Assignment Values

**Example:** A ball of mass $0.56\ \mathrm{kg}$ is tied to a string of length $0.88\ \mathrm{m}$ and swung in a vertical clockwise circle. At the instant shown, $T=1.2\ \mathrm{N}$ and $\theta=14^\circ$. Find the magnitude of the acceleration.

![](<../Source/Images/vertical-circle-ball-string-diagram.png>)

**Explanation**

Use the component equations first:

$$
\begin{aligned}
a_r &= \frac{T}{m}+g\cos\theta \\
&= \frac{1.2}{0.56}+9.8\cos(14^\circ) \\
&= 11.65\ \mathrm{m}/\mathrm{s}^2
\end{aligned}
$$

$$
\begin{aligned}
a_t &= g\sin\theta \\
&= 9.8\sin(14^\circ) \\
&= 2.37\ \mathrm{m}/\mathrm{s}^2
\end{aligned}
$$

The string length $L$ is not needed here because the force equations already give $a_r$ and $a_t$. It would matter in a different step if you needed to use $a_r=v^2/L$ to find a speed.

Now combine them as perpendicular components:

$$
\begin{aligned}
|\vec a| &= \sqrt{a_r^2+a_t^2} \\
&= \sqrt{(11.65)^2+(2.37)^2} \\
&= 11.89\ \mathrm{m}/\mathrm{s}^2
\end{aligned}
$$

To two significant figures, the acceleration magnitude is

$$
12\ \mathrm{m}/\mathrm{s}^2
$$

```quiz
type: radio
id: problem-5-q4
shuffle: true
content: |-
  A ball on a string has $L=0.88\ \mathrm{m}$, $T=1.2\ \mathrm{N}$, $m=0.56\ \mathrm{kg}$, and $\theta=14^\circ$. Use $a_r=\frac{T}{m}+g\cos\theta$ and $a_t=g\sin\theta$.

  What total acceleration magnitude should be reported to two significant figures?
options:
- id: a
  content: |-
    $9.3\ \mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $12\ \mathrm{m}/\mathrm{s}^2$
  correct: true
  feedback: |-
    $a_r=11.65$, $a_t=2.37$, and $\sqrt{(11.65)^2+(2.37)^2}=11.89$, which rounds to $12$.
- id: c
  content: |-
    $14\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    That is the result of adding the components directly before rounding.
- id: d
  content: |-
    $136\ \mathrm{m}/\mathrm{s}^2$
- id: e
  content: |-
    $2.4\ \mathrm{m}/\mathrm{s}^2$
```

---

<a id="summary"></a>
## Summary

When the problem asks for total acceleration magnitude in $r$-$t$ axes, use the perpendicular-component formula

$$
|\vec a|=\sqrt{a_r^2+a_t^2}
$$

For this vertical-circle setup:

$$
a_r=\frac{T}{m}+g\cos\theta
$$

and

$$
a_t=g\sin\theta
$$

Find the two components first, square them, add them, and take the positive square root. The common trap is adding $a_r+a_t$ directly, reporting only the larger radial component, or using the string length $L$ even though the force equations already gave the needed components.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
