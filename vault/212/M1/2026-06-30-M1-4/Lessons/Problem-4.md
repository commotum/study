# Finding the Speed for a Frictionless Banked Curve

## Table of Contents

- [Introduction](#introduction)
- [Resolve the Normal Force](#resolve-the-normal-force)
- [Derive the No-Friction Speed Formula](#derive-the-no-friction-speed-formula)
- [Compute the Speed from Radius and Bank Angle](#compute-the-speed-from-radius-and-bank-angle)
- [Check the Original Problem](#check-the-original-problem)

## Prerequisites

- Know that uniform circular motion requires inward acceleration $a_c=\dfrac{v^2}{r}$.
- Resolve a tilted force into horizontal and vertical components.
- Use $\tan\theta=\dfrac{\sin\theta}{\cos\theta}$.
- Solve $v^2=A$ as $v=\sqrt{A}$ when speed is positive.

---

<a id="introduction"></a>
## Introduction

The cue is an icy banked curve with no friction. Since the road is frictionless, the only forces on the car are gravity $mg$ downward and the normal force $N$ perpendicular to the road.

Find the no-friction speed by resolving the normal force into vertical and inward components, dividing the two force equations to eliminate $N$ and $m$, and then making $v$ the subject of the equation.

For a bank angle $\theta$ and radius $r$, the final speed should depend on $r$, $g$, and $\theta$, but not on the car's mass. Since speed is a magnitude, use the positive square root.

![](<../Source/Images/banked-curve-car-diagram.png>)

---

<a id="resolve-the-normal-force"></a>
## Resolve the Normal Force

**Example:** A car is on a frictionless road banked at angle $\theta$ from the horizontal. The normal force has magnitude $N$. Write the vertical and inward components of $N$.

**Explanation**

The normal force is perpendicular to the road. When the road is banked by $\theta$, the normal force tilts inward by $\theta$ from vertical.

That means the vertical component is adjacent to $\theta$:

$$
N_y=N\cos\theta.
$$

The inward horizontal component is opposite $\theta$:

$$
N_{\text{in}}=N\sin\theta.
$$

Gravity has no inward component; it points straight down.

```quiz
type: radio
id: p4-q1-normal-components
content: |-
  A frictionless road is banked at angle $\theta$ from the horizontal. The normal force has magnitude $N$ and leans inward. Which pair of components is correct?
options:
- id: a
  content: |-
    Vertical: $N\cos\theta$; inward: $N\sin\theta$
  correct: true
  feedback: |-
    The normal force is tilted by $\theta$ from vertical, so cosine gives the vertical component and sine gives the inward component.
- id: b
  content: |-
    Vertical: $N\sin\theta$; inward: $N\cos\theta$
  feedback: |-
    This swaps the sine and cosine components.
- id: c
  content: |-
    Vertical: $N$; inward: $mg$
  feedback: |-
    Gravity is vertical, not inward. The inward component comes from the tilted normal force.
- id: d
  content: |-
    Vertical: $N\cos\theta$; inward: $mg\sin\theta$
  feedback: |-
    Gravity points straight down, so it does not get an inward component.
```

---

<a id="derive-the-no-friction-speed-formula"></a>
## Derive the No-Friction Speed Formula

**Example:** A car of mass $m$ moves around a frictionless banked curve of radius $r$ and bank angle $\theta$. Derive the speed that lets the car move without sliding.

**Explanation**

There is no vertical acceleration, so the upward component of the normal force balances the weight:

$$
N\cos\theta=mg.
$$

The inward component of the normal force supplies the centripetal force:

$$
N\sin\theta=\frac{mv^2}{r}.
$$

Divide the inward equation by the vertical equation:

$$
\frac{N\sin\theta}{N\cos\theta}
=
\frac{\frac{mv^2}{r}}{mg}.
$$

Cancel $N$ and $m$:

$$
\tan\theta=\frac{v^2}{rg}.
$$

Now make $v$ the subject. Multiply by $rg$, then take the positive square root:

$$
v^2=rg\tan\theta.
$$

$$
v=\sqrt{rg\tan\theta}.
$$

The mass cancels because a heavier car has proportionally more weight and proportionally more required centripetal force.

```quiz
type: radio
id: p4-q2-formula
content: |-
  A car moves on a frictionless banked curve of radius $r$ and bank angle $\theta$. Which formula gives the speed that requires no friction?
options:
- id: a
  content: |-
    $v=\sqrt{rg\tan\theta}$
  correct: true
  feedback: |-
    Dividing $N\sin\theta=\dfrac{mv^2}{r}$ by $N\cos\theta=mg$ gives $\tan\theta=\dfrac{v^2}{rg}$.
- id: b
  content: |-
    $v=\sqrt{\dfrac{rg}{\tan\theta}}$
  feedback: |-
    This inverts the tangent factor.
- id: c
  content: |-
    $v=\sqrt{mg\tan\theta}$
  feedback: |-
    The mass cancels; the radius is needed.
- id: d
  content: |-
    $v=rg\tan\theta$
  feedback: |-
    This forgets to take the square root after solving for $v$.
- id: e
  content: |-
    $v=\pm\sqrt{rg\tan\theta}$
  feedback: |-
    Solving $v^2=rg\tan\theta$ gives two algebraic roots, but speed is a positive magnitude.
```

---

<a id="compute-the-speed-from-radius-and-bank-angle"></a>
## Compute the Speed from Radius and Bank Angle

**Example:** A frictionless banked curve has radius $60\ \mathrm{m}$ and bank angle $8.0^\circ$. Find the no-friction speed.

**Explanation**

Use the formula:

$$
v=\sqrt{rg\tan\theta}.
$$

Before evaluating, make sure the calculator is using degree mode, because the angle is written in degrees.

Substitute $r=60\ \mathrm{m}$, $g=9.8\ \mathrm{m}/\mathrm{s}^2$, and $\theta=8.0^\circ$:

$$
v=\sqrt{(60)(9.8)\tan(8.0^\circ)}.
$$

Compute the inside:

$$
(60)(9.8)\tan(8.0^\circ)\approx 82.6.
$$

Then take the square root:

$$
v\approx \sqrt{82.6}\approx 9.1\ \mathrm{m}/\mathrm{s}.
$$

```quiz
type: radio
id: p4-q3-numeric-speed
content: |-
  A frictionless banked curve has radius $50\ \mathrm{m}$ and bank angle $10.0^\circ$. Using $g=9.8\ \mathrm{m}/\mathrm{s}^2$, what is the no-friction speed?
options:
- id: a
  content: |-
    $9.3\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    $v=\sqrt{(50)(9.8)\tan(10.0^\circ)}\approx 9.3\ \mathrm{m}/\mathrm{s}$.
- id: b
  content: |-
    $2.9\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This is too small; it is close to taking the square root before multiplying all factors correctly.
- id: c
  content: |-
    $86\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This is the value inside the square root, not the speed.
- id: d
  content: |-
    $53\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This uses the wrong trigonometric factor or an inverted tangent relationship.
- id: e
  content: |-
    $18\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This is consistent with evaluating the degree angle as if it were in radians.
```

---

<a id="check-the-original-problem"></a>
## Check the Original Problem

**Example:** How fast does a $1800\ \mathrm{kg}$ car need to go to navigate an icy, no-friction banked curve of radius $48\ \mathrm{m}$ and banking angle $6.2^\circ$ without sliding?

**Explanation**

The mass is included in the problem statement, but it cancels during the derivation. Use

$$
v=\sqrt{rg\tan\theta}.
$$

Substitute $r=48\ \mathrm{m}$, $g=9.8\ \mathrm{m}/\mathrm{s}^2$, and $\theta=6.2^\circ$:

$$
v=\sqrt{(48)(9.8)\tan(6.2^\circ)}.
$$

Compute the value inside the square root:

$$
(48)(9.8)\tan(6.2^\circ)\approx 51.0.
$$

Then take the positive square root:

$$
v\approx \sqrt{51.0}\approx 7.15\ \mathrm{m}/\mathrm{s}.
$$

Rounded to match the assignment answer, this is about

$$
7.2\ \mathrm{m}/\mathrm{s}.
$$

```quiz
type: radio
id: p4-q4-original
content: |-
  An icy, no-friction banked curve has radius $48\ \mathrm{m}$ and bank angle $6.2^\circ$. Which speed is closest to the no-friction speed?
options:
- id: a
  content: |-
    $7.2\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    $v=\sqrt{(48)(9.8)\tan(6.2^\circ)}\approx 7.2\ \mathrm{m}/\mathrm{s}$.
- id: b
  content: |-
    $51\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This is approximately the value of $rg\tan\theta$, before taking the square root.
- id: c
  content: |-
    $21\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This is too large and does not match the small bank angle.
- id: d
  content: |-
    $1800\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    The mass cancels from the equations and should not appear in the final speed.
- id: e
  content: |-
    $-7.2\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    The algebraic negative root is not a valid speed.
```

---

## Summary

For an icy banked curve, no friction acts along the road. The normal force alone must balance weight vertically and supply the inward centripetal force horizontally:

$$
N\cos\theta=mg,
\qquad
N\sin\theta=\frac{mv^2}{r}.
$$

Dividing the radial equation by the vertical equation gives

$$
\tan\theta=\frac{v^2}{rg},
\qquad
v=\sqrt{rg\tan\theta}.
$$

The main traps are swapping sine and cosine, leaving the mass in the final formula, using radians mode for a degree angle, keeping the negative square-root branch, and forgetting the square root.

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Choosing Friction Direction on a Banked Curve](<Problem-5.md>)

<!-- study-guide-nav:end -->
