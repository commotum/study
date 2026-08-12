# Shifting Moment of Inertia to the Center-of-Mass Axis

<!--
lesson-id: 212-M2-047
topic-code: MTH212.M2.47
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Direction of the Axis Shift](#choose-the-direction-of-the-axis-shift)
- [Square the Center-of-Mass Displacement](#square-the-center-of-mass-displacement)
- [Apply the Shift to the Rod-Ball System](#apply-the-shift-to-the-rod-ball-system)
- [Avoid the Mass and Sign Traps](#avoid-the-mass-and-sign-traps)
- [Summary](#summary)

## Prerequisites

- Use the parallel-axis theorem, $I_{\mathrm{off}}=I_{\mathrm{cm}}+Md^2$.
- Add the masses of a composite system.
- Square a square root and combine fractional coefficients.

---

<a id="introduction"></a>
## Introduction

After the ball sticks to the rod in free space, the combined object rotates about an axis through its center of mass. The given earlier result, however, is the moment of inertia about a parallel axis through the rod's center.

The recognition cue is an inertia about one axis together with the distance to a parallel center-of-mass axis. Use

$$
I_{\mathrm{off}}=I_{\mathrm{cm}}+M_{\mathrm{tot}}d^2.
$$

Here, $M_{\mathrm{tot}}$ is the mass of the entire stuck-together object and $d$ is the perpendicular distance between the two parallel axes.

Because the known rod-center axis is the offset axis, solve this relation as

$$
I_{\mathrm{cm}}=I_{\mathrm{rod center}}-M_{\mathrm{tot}}d^2.
$$

---

<a id="choose-the-direction-of-the-axis-shift"></a>
## Choose the Direction of the Axis Shift

**Example:** A composite object has moment of inertia $11\ \mathrm{kg}\,\mathrm{m}^2$ about an axis that is $0.50\ \mathrm m$ from its center of mass. If its total mass is $4.0\ \mathrm{kg}$, find its inertia about the parallel center-of-mass axis.

**Explanation**

The offset-axis inertia is the larger one, so subtract the shift term:

$$
\begin{aligned}
I_{\mathrm{cm}}
&=I_{\mathrm{off}}-M_{\mathrm{tot}}d^2\\
&=11-(4.0)(0.50)^2\\
&=10\ \mathrm{kg}\,\mathrm{m}^2.
\end{aligned}
$$

```quiz
type: radio
id: p11-axis-direction
content: |-
  A $3\ \mathrm{kg}$ object has $I_{\mathrm{off}}=8\ \mathrm{kg}\,\mathrm{m}^2$ about an axis $1\ \mathrm m$ from its center of mass. What is $I_{\mathrm{cm}}$ for the parallel center-of-mass axis?
options:
- id: a
  content: |-
    $5\ \mathrm{kg}\,\mathrm{m}^2$
  correct: true
- id: b
  content: |-
    $11\ \mathrm{kg}\,\mathrm{m}^2$
- id: c
  content: |-
    $7\ \mathrm{kg}\,\mathrm{m}^2$
- id: d
  content: |-
    $24\ \mathrm{kg}\,\mathrm{m}^2$
```

---

<a id="square-the-center-of-mass-displacement"></a>
## Square the Center-of-Mass Displacement

**Example:** For the rod-ball system, the center of mass is a distance

$$
d=\sqrt{\left(\frac{L}{6}\right)^2+\left(\frac{r}{3}\right)^2}
$$

from the rod's center. Find $d^2$ and then calculate $M_{\mathrm{tot}}d^2$.

**Explanation**

Squaring cancels the square root:

$$
d^2=\frac{L^2}{36}+\frac{r^2}{9}.
$$

The ball has mass $m/2$, so the combined mass is

$$
M_{\mathrm{tot}}=m+\frac m2=\frac{3m}{2}.
$$

Therefore,

$$
\begin{aligned}
M_{\mathrm{tot}}d^2
&=\frac{3m}{2}\left(\frac{L^2}{36}+\frac{r^2}{9}\right)\\
&=\frac{mL^2}{24}+\frac{mr^2}{6}.
\end{aligned}
$$

```quiz
type: radio
id: p11-shift-term
content: |-
  If a composite system has total mass $2M$ and its center of mass is a distance $d=\sqrt{a^2/16+b^2/4}$ from a parallel reference axis, what is the shift term $M_{\mathrm{tot}}d^2$?
options:
- id: a
  content: |-
    $\dfrac{Ma^2}{8}+\dfrac{Mb^2}{2}$
  correct: true
- id: b
  content: |-
    $\dfrac{Ma}{8}+\dfrac{Mb}{2}$
- id: c
  content: |-
    $\dfrac{Ma^2}{16}+\dfrac{Mb^2}{4}$
- id: d
  content: |-
    $2M\sqrt{\dfrac{a^2}{16}+\dfrac{b^2}{4}}$
```

---

<a id="apply-the-shift-to-the-rod-ball-system"></a>
## Apply the Shift to the Rod-Ball System

**Example:** The moment of inertia about the axis through the rod's center is

$$
I_{\mathrm{rod center}}=\frac{5}{24}mL^2+\frac{7}{10}mr^2.
$$

Find the inertia about the axis through the combined center of mass.

**Explanation**

First separate the supplied result from the shift term already calculated:

$$
I_{\mathrm{rod center}}=\frac{5}{24}mL^2+\frac{7}{10}mr^2,
\qquad
M_{\mathrm{tot}}d^2=\frac{1}{24}mL^2+\frac{1}{6}mr^2.
$$

Now substitute both expressions into the rearranged parallel-axis theorem:

$$
\begin{aligned}
I_{\mathrm{cm}}
&=I_{\mathrm{rod center}}-M_{\mathrm{tot}}d^2\\
&=\left(\frac{5}{24}mL^2+\frac{7}{10}mr^2\right)
-\left(\frac{1}{24}mL^2+\frac{1}{6}mr^2\right).
\end{aligned}
$$

Combine only like terms:

$$
\begin{aligned}
I_{\mathrm{cm}}
&=\left(\frac{5}{24}-\frac{1}{24}\right)mL^2
+\left(\frac{7}{10}-\frac{1}{6}\right)mr^2\\
&=\frac{1}{6}mL^2+\frac{8}{15}mr^2.
\end{aligned}
$$

```quiz
type: radio
id: p11-homework-check
content: |-
  A thin uniform rod of mass $m$ and length $L$ is initially at rest in outer space. A nonspinning uniform ball of mass $m/2$ and radius $r$ strikes one end of the rod with speed $v$ and sticks to it.

  What is the moment of inertia of the combined system about the axis around which it rotates after the collision?
options:
- id: a
  content: |-
    $\dfrac{1}{6}mL^2+\dfrac{8}{15}mr^2$
  correct: true
- id: b
  content: |-
    $\dfrac{1}{16}mL^2+\dfrac{2}{3}mr^2$
```

---

<a id="avoid-the-mass-and-sign-traps"></a>
## Avoid the Mass and Sign Traps

**Example:** Suppose $I_A$ is known about a parallel axis $A$ that does not pass through the combined center of mass. Which expression gives the center-of-mass inertia?

**Explanation**

Use the mass of the entire composite object, not the mass of only one piece. Also subtract when moving from the offset axis to the center-of-mass axis:

$$
I_{\mathrm{cm}}=I_A-(m_1+m_2)d^2.
$$

The sign provides a useful check: among parallel axes, the center-of-mass axis has the smallest moment of inertia.

```quiz
type: radio
id: p11-trap-check
content: |-
  Two stuck-together pieces have masses $m$ and $m/2$. Their center-of-mass axis is a distance $d$ from a parallel axis $A$. If $I_A$ is known, which formula is correct?
options:
- id: a
  content: |-
    $I_{\mathrm{cm}}=I_A-\dfrac{3m}{2}d^2$
  correct: true
- id: b
  content: |-
    $I_{\mathrm{cm}}=I_A+\dfrac{3m}{2}d^2$
- id: c
  content: |-
    $I_{\mathrm{cm}}=I_A-\dfrac{m}{2}d^2$
- id: d
  content: |-
    $I_{\mathrm{cm}}=I_A-md^2$
```

---

<a id="summary"></a>
## Summary

When a free composite object rotates after a collision, use the axis through its combined center of mass. If the known inertia is about a parallel offset axis:

1. Write $I_{\mathrm{cm}}=I_{\mathrm{off}}-M_{\mathrm{tot}}d^2$.
2. Square the full displacement before substituting.
3. Use the total mass of every stuck-together part.
4. Combine $L^2$ terms only with $L^2$ terms and $r^2$ terms only with $r^2$ terms.

The quick reasonableness check is $I_{\mathrm{cm}}<I_{\mathrm{off}}$: shifting an axis away from the center of mass adds the nonnegative quantity $M_{\mathrm{tot}}d^2$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
