# Finding Static Friction on a Flat Curve

<!--
lesson-id: 212-M1-013
topic-code: MTH212.M1.13
-->

## Table of Contents

- [Introduction](#introduction)
- [Identify the Inward Force](#identify-the-inward-force)
- [Set the Limiting-Speed Equation](#set-the-limiting-speed-equation)
- [Cancel Mass and Solve for the Coefficient](#cancel-mass-and-solve-for-the-coefficient)
- [Substitute the Values](#substitute-the-values)
- [Check Mass and Units](#check-mass-and-units)
- [Summary](#summary)

## Prerequisites

- Identify forces on a car on a level road: weight $mg$, normal force $N$, and static friction $f_s$.
- Use the radial force balance for the required net inward force: $\sum F_r=mv^2/r$.
- Use maximum static friction as $f_{s,\max}=\mu_s N$.
- Recognize that on a level road with no vertical acceleration, $N=mg$.

---

<a id="introduction"></a>
## Introduction

A $1800\ \mathrm{kg}$ car rounds a level circular curve of radius $49\ \mathrm{m}$ at $16\ \mathrm{m}/\mathrm{s}$. It is traveling as fast as it can without sliding. What coefficient of static friction is needed between the tires and the road?

![](<../Source/Images/level-curve-car-diagram.png>)

The normal force points upward on a level road, so it cannot turn the car. The horizontal force that bends the car's path is static friction from the road. As the speed increases, the required inward force increases; at the fastest speed that avoids sliding, static friction has reached its maximum value. This is why “as fast as it can go without sliding” matters.

At that limit,

$$
f_{s,\max}=\frac{mv^2}{r}
$$

Because the car has no vertical acceleration, $N=mg$ and $f_{s,\max}=\mu_smg$. Equating the available friction to the required inward force gives

$$
\mu_s=\frac{v^2}{rg}.
$$

---

<a id="identify-the-inward-force"></a>
## Identify the Inward Force

**Example:** A car moves around a level circular curve at constant speed. Which force points toward the center of the circle?

**Explanation**

The car has weight $mg$ downward and normal force $N$ upward. Those vertical forces balance because the road is level and the car is not accelerating vertically.

The only horizontal force available is static friction. Static friction points toward the center of the circle, so it supplies the centripetal force.

```quiz
type: radio
id: p3-q1
shuffle: true
content: |-
  A car travels around a level circular curve without sliding. Which force supplies the inward, centripetal force?
options:
- id: a
  content: |-
    Static friction, pointing toward the center of the circle
  correct: true
- id: b
  content: |-
    The normal force, pointing upward
- id: c
  content: |-
    Gravity, pointing downward
- id: d
  content: |-
    A separate force called "centripetal force"
```

---

<a id="set-the-limiting-speed-equation"></a>
## Set the Limiting-Speed Equation

**Example:** A car of mass $m$ moves around a level curve of radius $r$ at speed $v$. It is just about to slide outward. Write the force equation that finds the required coefficient of static friction.

**Explanation**

"Just about to slide" means static friction is at its maximum. Below that boundary, the actual friction is only the value needed, $f_s=mv^2/r$, and need not equal $\mu_sN$. At the boundary,

$$
f_{s,\max}=\mu_s N.
$$

On a level road, $N=mg$, so

$$
f_{s,\max}=\mu_s mg.
$$

The tires are still rolling without sideways slipping at this instant, so the force is static rather than kinetic. That maximum friction must equal the required inward force. A clean setup is:

$$
\begin{aligned}
\text{maximum static friction}&=\text{required inward force} \\
\mu_s N&=\frac{mv^2}{r} \\
\mu_s mg&=\frac{mv^2}{r}.
\end{aligned}
$$

```quiz
type: radio
id: p3-q2
shuffle: true
content: |-
  A car is going around a level circular curve as fast as it can without sliding. Which equation correctly connects static friction to the required inward force?
options:
- id: a
  content: |-
    $\mu_s mg=\dfrac{mv^2}{r}$
  correct: true
- id: b
  content: |-
    $mg=\dfrac{mv^2}{r}$
- id: c
  content: |-
    $\mu_s mg=\dfrac{mv}{r}$
- id: d
  content: |-
    $\mu_s N=mg$
- id: e
  content: |-
    $N=\dfrac{mv^2}{r}$
```

---

<a id="cancel-mass-and-solve-for-the-coefficient"></a>
## Cancel Mass and Solve for the Coefficient

**Example:** Solve

$$
\mu_s mg=\frac{mv^2}{r}
$$

for $\mu_s$.

**Explanation**

Divide both sides by $mg$:

$$
\begin{aligned}
\mu_s mg&=\frac{mv^2}{r} \\
\frac{\mu_s mg}{mg}&=\frac{mv^2/r}{mg} \\
\mu_s&=\frac{v^2}{rg}.
\end{aligned}
$$

The mass cancels. For a level curve, the required coefficient depends on speed, radius, and gravity, not on the car's mass.

```quiz
type: radio
id: p3-q3
shuffle: true
content: |-
  A $1500\ \mathrm{kg}$ car goes around a level curve of radius $30\ \mathrm{m}$ at $12\ \mathrm{m}/\mathrm{s}$ at the limiting speed before sliding. Which expression gives $\mu_s$?
options:
- id: a
  content: |-
    $\dfrac{12^2}{(30)(9.8)}$
  correct: true
- id: b
  content: |-
    $\dfrac{(1500)(12^2)}{(30)(9.8)}$
- id: c
  content: |-
    $\dfrac{12}{(30)(9.8)}$
- id: d
  content: |-
    $\dfrac{(30)(9.8)}{12^2}$
- id: e
  content: |-
    $\dfrac{(1500)(9.8)}{30}$
```

---

<a id="substitute-the-values"></a>
## Substitute the Values

**Example:** A $1800\ \mathrm{kg}$ car is going around a level circular curve of radius $49\ \mathrm{m}$ at a speed of $16\ \mathrm{m}/\mathrm{s}$. What coefficient of static friction keeps it from sliding, assuming it is going as fast as it can without sliding?

**Explanation**

Use

$$
\mu_s=\frac{v^2}{rg}.
$$

Then substitute $v=16\ \mathrm{m}/\mathrm{s}$, $r=49\ \mathrm{m}$, and $g=9.8\ \mathrm{m}/\mathrm{s}^2$:

$$
\begin{aligned}
\mu_s&=\frac{16^2}{(49)(9.8)} \\
&=\frac{256}{480.2} \\
&\approx 0.53.
\end{aligned}
$$

The $1800\ \mathrm{kg}$ mass is not used in the final calculation because it cancels out of the force equation. The coefficient has no units, so the answer is

$$
\mu_s\approx 0.53.
$$

```quiz
type: radio
id: p3-q4
shuffle: true
content: |-
  A car goes around a level circular curve of radius $75\ \mathrm{m}$ at $18\ \mathrm{m}/\mathrm{s}$ at the limiting speed before sliding. Using $g=9.8\ \mathrm{m}/\mathrm{s}^2$, what coefficient of static friction is required, rounded to two decimal places?
options:
- id: a
  content: |-
    $0.44$
  correct: true
- id: b
  content: |-
    $0.24$
- id: c
  content: |-
    $2.27$
- id: d
  content: |-
    $0.024$
- id: e
  content: |-
    $4.41$
```

---

<a id="check-mass-and-units"></a>
## Check Mass and Units

**Example:** Two cars take the same level curve at the same limiting speed. One car has twice the mass of the other. Which car needs the larger coefficient of static friction?

**Explanation**

Neither car needs a larger coefficient just because of mass. A heavier car needs more inward force, but it also has a larger normal force, so maximum static friction increases by the same factor.

The cancellation in

$$
\mu_s mg=\frac{mv^2}{r}
$$

is the algebraic reason mass does not affect $\mu_s$ here. The units also cancel:

$$
\frac{v^2}{rg}
=\frac{\mathrm{m}^2/\mathrm{s}^2}{(\mathrm{m})(\mathrm{m}/\mathrm{s}^2)}
=1.
$$

So a coefficient of static friction should be a plain number, not a number with $\mathrm{N}$, $\mathrm{kg}$, or $\mathrm{m}/\mathrm{s}$ attached. The symbolic result also supplies a behavior check: $\mu_s=v^2/(rg)$ must rise with $v^2$, fall when the curve radius grows, and remain independent of mass.

```quiz
type: radio
id: p3-q5
shuffle: true
content: |-
  A $1000\ \mathrm{kg}$ car and a $2000\ \mathrm{kg}$ car both take the same level curve at the same limiting speed. Which statement is correct?
options:
- id: a
  content: |-
    They require the same $\mu_s$ because mass cancels from $\mu_s mg=\dfrac{mv^2}{r}$.
  correct: true
- id: b
  content: |-
    The $2000\ \mathrm{kg}$ car requires twice the $\mu_s$ because it has twice the mass.
- id: c
  content: |-
    The $1000\ \mathrm{kg}$ car requires twice the $\mu_s$ because it is lighter.
- id: d
  content: |-
    The coefficient cannot be found unless the mass is known.
- id: e
  content: |-
    The coefficient is always $1$ at the limiting speed.
```

---

<a id="summary"></a>
## Summary

At the maximum speed before a car slides on a level curve, static friction has reached its limit and supplies the inward net force:

$$
\mu_s mg=\frac{mv^2}{r}.
$$

Cancel $m$ and solve:

$$
\mu_s=\frac{v^2}{rg}.
$$

The normal force cannot turn the car because it is vertical. The required coefficient is dimensionless and independent of the car's mass; using $v$ instead of $v^2$ breaks both the circular-motion equation and the unit check.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Threshold Angular Speed Before Slipping](../../2026-06-29-M1-3/Lessons/Problem-6.md)

Study guide index: 13/35

---
<!-- lesson-nav:end -->
