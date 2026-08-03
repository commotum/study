# Net Gravitational Force from a Right-Triangle Arrangement

<!--
lesson-id: 212-M3-013
topic-code: MTH212.M3.13
-->

## Table of Contents

- [Introduction](#introduction)
- [Point Each Force Toward Its Source](#point-each-force-toward-its-source)
- [Resolve a Diagonal Gravitational Force](#resolve-a-diagonal-gravitational-force)
- [Add Matching Components](#add-matching-components)
- [Find the Net-Force Magnitude](#find-the-net-force-magnitude)
- [Summary](#summary)

## Prerequisites

- Newton's law of gravitation: $F=Gm_am_b/r^2$
- The Pythagorean theorem
- Adding vectors by components

---

<a id="introduction"></a>
## Introduction

When several masses attract one object, the net force is a **vector sum**, not a sum of force magnitudes. The cue in this problem is that one force on $m_2$ is horizontal while the other points diagonally toward $m_3$.

The reusable rule is

$$
\mathbf F_{\text{net}}=\sum_i \mathbf F_i,
\qquad
F_{\text{net}}=\sqrt{F_{\text{net},x}^2+F_{\text{net},y}^2}.
$$

Use this sequence:

1. Draw each force on the object of interest.
2. Find every separation distance.
3. Resolve each diagonal force into $x$- and $y$-components.
4. Add the $x$-components and the $y$-components separately.
5. Compute $F_{\text{net}}=\sqrt{F_{\text{net},x}^2+F_{\text{net},y}^2}$.

---

<a id="point-each-force-toward-its-source"></a>
## Point Each Force Toward Its Source

Gravity is attractive. A force on $m_2$ due to another mass points from $m_2$ **toward** that mass.

Predict the component signs from the picture before substituting into a formula. This separates the direction decision from the algebra.

**Example:** Put $m_1$ at $(0,0)$, $m_2$ at $(a,0)$, and $m_3$ at $(0,b)$, where $a,b>0$. Determine the signs of the two forces on $m_2$.

**Explanation**

The force from $m_1$ points left, so its component signs are $(-,0)$. The force from $m_3$ points up and left, so its component signs are $(-,+)$. Therefore, both forces reinforce each other horizontally; they do not cancel.

```quiz
type: radio
id: p3-direction-signs
content: |-
  A test mass is at $(5,0)$ and an attracting mass is at $(0,12)$. What are the signs of the gravitational force components on the test mass?
options:
- id: a
  content: |-
    $F_x>0$ and $F_y>0$
- id: b
  content: |-
    $F_x<0$ and $F_y>0$
  correct: true
- id: c
  content: |-
    $F_x<0$ and $F_y<0$
- id: d
  content: |-
    $F_x>0$ and $F_y<0$
```

---

<a id="resolve-a-diagonal-gravitational-force"></a>
## Resolve a Diagonal Gravitational Force

For a diagonal separation with horizontal change $-a$ and vertical change $b$,

$$
r=\sqrt{a^2+b^2}
$$

and the unit vector toward the attracting mass is

$$
\hat{\mathbf r}=\left\langle -\frac{a}{r},\frac{b}{r}\right\rangle.
$$

Multiplying the force magnitude $GmM/r^2$ by this unit vector gives

$$
\mathbf F
=\frac{GmM}{r^2}\hat{\mathbf r}
=\left\langle
-\frac{GmMa}{(a^2+b^2)^{3/2}},
\frac{GmMb}{(a^2+b^2)^{3/2}}
\right\rangle.
$$

**Example:** A mass $M$ is $3$ units left and $4$ units above a mass $m$. Write the gravitational force on $m$ in component form.

**Explanation**

Here $r=\sqrt{3^2+4^2}=5$. The force magnitude is $GmM/25$, and the unit direction is $\langle-3/5,4/5\rangle$. Thus

$$
\mathbf F=\left\langle-\frac{3GmM}{125},\frac{4GmM}{125}\right\rangle.
$$

The power $r^3$ in the component denominators comes from $1/r^2$ for the force magnitude and another $1/r$ from the unit vector.

As a check, the numerator of either component contains one distance factor, so a denominator of $r^3$ leaves the expected inverse-square dependence overall.

```quiz
type: radio
id: p3-diagonal-components
content: |-
  An attracting mass $M$ is a horizontal distance $u$ left and a vertical distance $v$ above a mass $m$. Which vector is the gravitational force on $m$?
options:
- id: a
  content: |-
    $\left\langle-\dfrac{GmMu}{(u^2+v^2)^{3/2}},\dfrac{GmMv}{(u^2+v^2)^{3/2}}\right\rangle$
  correct: true
- id: b
  content: |-
    $\left\langle-\dfrac{GmM}{u^2},\dfrac{GmM}{v^2}\right\rangle$
- id: c
  content: |-
    $\left\langle\dfrac{GmMu}{u^2+v^2},\dfrac{GmMv}{u^2+v^2}\right\rangle$
- id: d
  content: |-
    $\left\langle-\dfrac{GmMu}{(u^2+v^2)^2},\dfrac{GmMv}{(u^2+v^2)^2}\right\rangle$
```

---

<a id="add-matching-components"></a>
## Add Matching Components

Add horizontal components only to horizontal components, and vertical components only to vertical components.

**Example:** Suppose the two forces on an object are

$$
\mathbf F_1=\langle-A,0\rangle
\qquad\text{and}\qquad
\mathbf F_2=\langle-B,C\rangle,
$$

where $A,B,C>0$. Find the net-force components.

**Explanation**

Componentwise addition gives

$$
\mathbf F_{\text{net}}
=\mathbf F_1+\mathbf F_2
=\langle-(A+B),C\rangle.
$$

The two leftward contributions add. Writing $-A+B$ would incorrectly treat the diagonal force as rightward.

```quiz
type: radio
id: p3-component-sum
content: |-
  Two forces are $\mathbf F_1=\langle-7,0\rangle\,\mathrm N$ and $\mathbf F_2=\langle-3,4\rangle\,\mathrm N$. What is their vector sum?
options:
- id: a
  content: |-
    $\langle-10,4\rangle\,\mathrm N$
  correct: true
- id: b
  content: |-
    $\langle-4,4\rangle\,\mathrm N$
- id: c
  content: |-
    $\langle-10,0\rangle\,\mathrm N$
- id: d
  content: |-
    $\langle-7,4\rangle\,\mathrm N$
```

---

<a id="find-the-net-force-magnitude"></a>
## Find the Net-Force Magnitude

Once the net force is in component form, its magnitude follows from the right triangle formed by its perpendicular components.

**Example:** Find the magnitude of $\mathbf F_{\text{net}}=\langle-10,4\rangle\,\mathrm N$.

**Explanation**

$$
F_{\text{net}}=\sqrt{(-10)^2+4^2}=\sqrt{116}=2\sqrt{29}\,\mathrm N.
$$

The sign of a component records direction. Squaring removes that sign when computing magnitude.

For the asteroid arrangement, the force from $m_1$ on $m_2$ is purely leftward:

$$
\mathbf F_{21}
=\left\langle-\frac{Gm_1m_2}{d_2^2},0\right\rangle.
$$

The separation between $m_2$ and $m_3$ is $\sqrt{d_2^2+d_3^2}$, and the direction from $m_2$ toward $m_3$ is proportional to $\langle-d_2,d_3\rangle$. Therefore,

$$
\mathbf F_{23}
=\left\langle
-\frac{Gm_2m_3d_2}{(d_2^2+d_3^2)^{3/2}},
\frac{Gm_2m_3d_3}{(d_2^2+d_3^2)^{3/2}}
\right\rangle.
$$

For a compact final calculation, define

$$
A=\frac{Gm_1m_2}{d_2^2},\qquad
B=\frac{Gm_2m_3d_2}{(d_2^2+d_3^2)^{3/2}},\qquad
C=\frac{Gm_2m_3d_3}{(d_2^2+d_3^2)^{3/2}}.
$$

Then $\mathbf F_{\text{net}}=\langle-(A+B),C\rangle$, so

$$
F_{\text{net}}=\sqrt{(A+B)^2+C^2}.
$$

This magnitude must be larger than either nonzero component magnitude by itself. That gives a quick check on the final expression.

```quiz
type: radio
id: p3-original-application
content: |-
  At one instant, three asteroids have the arrangement shown. Asteroid $m_1$ is a horizontal distance $d_2$ from $m_2$ and a vertical distance $d_3$ from $m_3$.

  What is the magnitude of the net gravitational force on $m_2$ at this instant?

  ![](<../Source/2026-07-17-HW-5/Images/three-asteroid-geometry.png>)
options:
- id: a
  content: |-
    $\sqrt{\left(\dfrac{Gm_1m_2}{d_2^2}\right)^2+\left(\dfrac{Gm_2m_3}{(d_2^2+d_3^2)^2}\right)^2}$
- id: b
  content: |-
    $\sqrt{\left(\dfrac{Gm_1m_2}{d_2^2}+\dfrac{Gm_2m_3d_2}{(d_2^2+d_3^2)^{3/2}}+\dfrac{Gm_2m_3d_3}{(d_2^2+d_3^2)^{3/2}}\right)^2}$
- id: c
  content: |-
    $\sqrt{\left(\dfrac{Gm_1m_2}{d_2^2}-\dfrac{Gm_2m_3d_2}{(d_2^2+d_3^2)^{3/2}}\right)^2+\left(\dfrac{Gm_2m_3d_3}{(d_2^2+d_3^2)^{3/2}}\right)^2}$
- id: d
  content: |-
    $\sqrt{\left(\dfrac{Gm_1m_2}{d_2^2}+\dfrac{Gm_2m_3d_2}{(d_2^2+d_3^2)^{3/2}}\right)^2+\left(\dfrac{Gm_2m_3d_3}{(d_2^2+d_3^2)^{3/2}}\right)^2}$
  correct: true
```

---

<a id="summary"></a>
## Summary

- **Cue:** More than one mass attracts the same object in different directions.
- **Direction:** Draw each gravitational force toward its source mass before doing algebra.
- **Diagonal component rule:** Multiply $GmM/r^2$ by the unit direction vector; this produces component denominators of $r^3$.
- **Procedure:** Add $x$-components, add $y$-components, then use $\sqrt{F_x^2+F_y^2}$.
- **Main trap:** Forces that point left have negative $x$-components. If two forces both point left, their horizontal magnitudes reinforce even though the component sum is negative.
- **Check:** The net magnitude cannot be smaller than the absolute value of either of its perpendicular components.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Gravitational Potential Energy of a Three-Body System](Problem-8.md)

Study guide index: 14/20

---

<!-- lesson-nav:end -->
