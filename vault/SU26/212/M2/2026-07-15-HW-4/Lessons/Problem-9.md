# Moment of Inertia of a Rod–Ball Composite

<!--
lesson-id: 212-M2-045
topic-code: MTH212.M2.45
-->

## Table of Contents

- [Introduction](#introduction)
- [Add the Component Inertias](#add-the-component-inertias)
- [Measure the Ball's Offset](#measure-the-balls-offset)
- [Shift the Ball's Inertia](#shift-the-balls-inertia)
- [Assemble the Given System](#assemble-the-given-system)
- [Summary](#summary)

## Prerequisites

- Moment of inertia depends on the chosen rotation axis.
- For a thin uniform rod about its center, perpendicular to the rod, $I_{\mathrm{rod,cm}}=\dfrac{1}{12}mL^2$.
- For a uniform solid sphere about its center, $I_{\mathrm{sphere,cm}}=\dfrac{2}{5}MR^2$.
- The parallel-axis theorem is $I=I_{\mathrm{cm}}+Md^2$.

---

<a id="introduction"></a>
## Introduction

When several rigid bodies stick together, the moment of inertia about a specified axis is the sum of the bodies' moments of inertia about that **same axis**. If the axis does not pass through a body's center of mass, first shift that body's center-of-mass inertia with the parallel-axis theorem.

For the rod–ball system, the requested axis passes through the rod's center but not through the ball's center. The reusable procedure is therefore:

1. compute the rod's inertia about the requested axis;
2. find the squared distance from the ball's center to that axis;
3. shift the ball's inertia with $I_{\mathrm{ball}}=I_{\mathrm{ball,cm}}+Md^2$;
4. add the two contributions.

This gives the following component inventory before any algebra begins:

| Body | Relation to the requested axis | Contribution to use |
|---|---|---|
| Rod | Axis passes through its center | $I_{\mathrm{rod}}=\dfrac{1}{12}mL^2$ |
| Ball | Center is displaced from the axis | $I_{\mathrm{ball}}=\dfrac{2}{5}\left(\dfrac{m}{2}\right)r^2+\left(\dfrac{m}{2}\right)d^2$ |

The collision speed $v$ affects the later motion, but it does not enter this moment-of-inertia calculation.

---

<a id="add-the-component-inertias"></a>
## Add the Component Inertias

**Example:** A rod and a solid sphere both have their centers on the same rotation axis. The rod has mass $m$ and length $L$; the sphere has mass $m/2$ and radius $r$. Write the combined moment of inertia.

**Explanation**

Because the axis passes through both centers of mass, no parallel-axis shift is needed:

$$
\begin{aligned}
I_{\mathrm{total}}
&=I_{\mathrm{rod,cm}}+I_{\mathrm{sphere,cm}}\\
&=\frac{1}{12}mL^2+\frac{2}{5}\left(\frac{m}{2}\right)r^2\\
&=\frac{1}{12}mL^2+\frac{1}{5}mr^2.
\end{aligned}
$$

This is the basic composite-body pattern: calculate each named piece about the common axis, then add the pieces once.

```quiz
type: radio
id: p9-add-components
content: |-
  A thin rod has moment of inertia $I_r$ and a ball has moment of inertia $I_b$, each measured about the same specified axis. What is the combined moment of inertia after they stick together?
options:
- id: a
  content: |-
    $I_r+I_b$
  correct: true
- id: b
  content: |-
    $I_r-I_b$
- id: c
  content: |-
    $I_rI_b$
- id: d
  content: |-
    $\dfrac{I_rI_b}{I_r+I_b}$
- id: e
  content: |-
    $\dfrac{I_r+I_b}{2}$
```

---

<a id="measure-the-balls-offset"></a>
## Measure the Ball's Offset

**Example:** A ball touches the lower end of a vertical rod. The requested axis is perpendicular to the page through the rod's center. The ball's center is $L/2$ below the rod's center and $r$ to the side. Find $d^2$, where $d$ is the distance between the ball's center and the requested axis.

**Explanation**

Relative to the rod's center, the ball's center has perpendicular components $r$ and $-L/2$. Just as in the distance formula or the magnitude of a two-dimensional vector, square the components and add:

$$
d^2=\left(\frac{L}{2}\right)^2+r^2
=\frac{L^2}{4}+r^2.
$$

Do not use $d=L/2+r$. The diagram's $L/2$ and $r$ offsets point in perpendicular directions, so their squares add. This also explains why the final answer has no $Lr$ cross term.

```quiz
type: radio
id: p9-offset-distance
content: |-
  A sphere's center is horizontally offset by $R$ and vertically offset by $H$ from an axis perpendicular to the page. What squared distance belongs in the parallel-axis term $Md^2$?
options:
- id: a
  content: |-
    $H^2+R^2$
  correct: true
- id: b
  content: |-
    $(H+R)^2$
- id: c
  content: |-
    $H^2-R^2$
- id: d
  content: |-
    $H+R$
- id: e
  content: |-
    $HR$
```

---

<a id="shift-the-balls-inertia"></a>
## Shift the Ball's Inertia

**Example:** For the ball of mass $m/2$ and radius $r$ in the rod–ball diagram, compute its moment of inertia about the axis through the rod's center.

**Explanation**

Keep the ball's own center-of-mass inertia, then add the parallel-axis term:

$$
\begin{aligned}
I_{\mathrm{ball}}
&=I_{\mathrm{ball,cm}}+\left(\frac{m}{2}\right)d^2\\
&=\frac{2}{5}\left(\frac{m}{2}\right)r^2
+\frac{m}{2}\left(\frac{L^2}{4}+r^2\right)\\
&=\frac{1}{5}mr^2+\frac{1}{8}mL^2+\frac{1}{2}mr^2\\
&=\frac{1}{8}mL^2+\frac{7}{10}mr^2.
\end{aligned}
$$

Both terms use the **ball's mass**, $m/2$: its own rotational inertia is $I_{\mathrm{ball,cm}}$, and the shift is $(m/2)d^2$. Treating the ball as a point mass would keep only $(m/2)d^2$ and incorrectly discard the $\frac{2}{5}(m/2)r^2$ term.

```quiz
type: radio
id: p9-shift-sphere
content: |-
  A uniform solid sphere has mass $M$, radius $R$, and center a distance $d$ from a parallel rotation axis. What is its moment of inertia about that axis?
options:
- id: a
  content: |-
    $\dfrac{2}{5}MR^2+Md^2$
  correct: true
- id: b
  content: |-
    $Md^2$
- id: c
  content: |-
    $\dfrac{2}{5}M(R+d)^2$
- id: d
  content: |-
    $\dfrac{2}{5}MR^2-Md^2$
- id: e
  content: |-
    $\dfrac{2}{5}Md^2+MR^2$
```

---

<a id="assemble-the-given-system"></a>
## Assemble the Given System

**Example:** A thin uniform rod of mass $m$ and length $L$ is initially at rest in outer space. A nonspinning uniform ball of mass $m/2$ and radius $r$ strikes one end of the rod with speed $v$ and sticks to it. Find the moment of inertia of the combined system about an axis perpendicular to the rod and passing through the rod's center.

**Explanation**

Add the rod contribution and the shifted ball contribution:

$$
\begin{aligned}
I_{\mathrm{total}}
&=I_{\mathrm{rod}}+I_{\mathrm{ball}}\\
&=\frac{1}{12}mL^2
+\left(\frac{1}{8}mL^2+\frac{7}{10}mr^2\right)\\
&=\left(\frac{2}{24}+\frac{3}{24}\right)mL^2
+\frac{7}{10}mr^2\\
&=\boxed{\frac{5}{24}mL^2+\frac{7}{10}mr^2}.
\end{aligned}
$$

```quiz
type: radio
id: p9-final-check
content: |-
  A thin uniform rod of mass $m$ and length $L$ is initially at rest in outer space. A nonspinning uniform ball of mass $m/2$ and radius $r$ strikes one end of the rod with speed $v$ and sticks to it.

  What is the moment of inertia of the combined system about an axis perpendicular to the rod and passing through the rod's center?

  Hint: Do not treat the ball as a point mass. The moment of inertia of a uniform sphere of mass $M$ and radius $R$ about its center is $\dfrac{2}{5}MR^2$.

  ![](<../Source/2026-07-15-HW-4/Images/rod-ball-inelastic-collision.png>)
options:
- id: a
  content: |-
    $\dfrac{5}{24}mL^2+\dfrac{7}{10}mr^2$
  correct: true
- id: b
  content: |-
    $\dfrac{12}{5}mL^2+\dfrac{2}{7}mr^2$
```

---

<a id="summary"></a>
## Summary

For a composite rigid body about a specified axis:

1. use one axis for every component;
2. write each component's center-of-mass inertia;
3. shift every off-center component with $I=I_{\mathrm{cm}}+Md^2$;
4. find $d^2$ from the actual geometry—perpendicular offsets contribute as a sum of squares;
5. add all component inertias.

For the rod–ball system, the cue **axis through the rod's center but not the ball's center** means “rod formula directly, sphere formula plus a parallel-axis shift.” Here $d^2=L^2/4+r^2$. The main traps are treating the ball as a point mass, using $L/2+r$ for perpendicular offsets, or using the rod's mass in the ball terms.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
