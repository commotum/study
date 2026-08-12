# Converting Angular Acceleration to Tangential Acceleration

<!--
lesson-id: 212-M1-066
topic-code: MTH212.M1.66
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Angular Change into Tangential Change](#convert-angular-change-into-tangential-change)
- [Solve Backward for Angular Acceleration](#solve-backward-for-angular-acceleration)
- [Carry the Sign into the Tangential Direction](#carry-the-sign-into-the-tangential-direction)
- [Keep Tangential and Radial Acceleration Separate](#keep-tangential-and-radial-acceleration-separate)
- [Summary](#summary)

## Prerequisites

- Interpret $\omega$ as angular velocity and $\alpha$ as angular acceleration.
- Multiply and divide quantities with units.
- Use a chosen positive direction for rotation.

---

<a id="introduction"></a>
## Introduction

When a point stays at a fixed radius $r$ while a rigid object changes its angular velocity, its speed along the circular path changes too. The conversion between those angular and linear changes is

$$
\boxed{a_t=r\alpha}.
$$

Here $a_t$ is the **signed tangential component** of acceleration. It describes the change in the point's signed tangential velocity, not the inward turning of its velocity.

Use this relation when the cue is:

- a point is a known distance $r$ from the rotation axis;
- the radius stays fixed; and
- the problem gives either $\alpha$ or $a_t$ and asks for the other.

The radius must be in a linear unit such as meters, and the angular acceleration should be in radians per second squared. A degree measure must first be converted to radians.

---

<a id="convert-angular-change-into-tangential-change"></a>
## Convert Angular Change into Tangential Change

At fixed radius, arc length and angle are related by

$$
s=r\theta.
$$

Differentiating once gives the tangential relation $v=r\omega$, with signs interpreted using the chosen positive directions. Differentiating again gives

$$
a_t=r\alpha.
$$

Thus every point on a rigid object shares the same $\alpha$, but a point farther from the axis has a larger $a_t$.

**Example:** A point on a wheel is $0.35\ \mathrm{m}$ from the axis. The wheel has angular acceleration $4.0\ \mathrm{rad}/\mathrm{s}^2$. Find the point's tangential acceleration.

**Explanation**

The point remains at a fixed radius, so multiply the angular acceleration by that radius:

$$
\begin{aligned}
a_t&=r\alpha\\
&=(0.35\ \mathrm{m})(4.0\ \mathrm{rad}/\mathrm{s}^2)\\
&=1.4\ \mathrm{m}/\mathrm{s}^2.
\end{aligned}
$$

Radians are dimensionless, leaving the linear-acceleration unit $\mathrm{m}/\mathrm{s}^2$.

```quiz
type: radio
id: m1-ta-direct
shuffle: true
content: |-
  A mark on a disk is $0.40\ \mathrm{m}$ from the rotation axis. The disk has angular acceleration $6.0\ \mathrm{rad}/\mathrm{s}^2$. What is the mark's tangential acceleration?
options:
- id: m1-ta-direct-a
  content: |-
    $15\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    This divides $\alpha$ by $r$. At fixed radius, angular acceleration is converted to tangential acceleration by multiplying: $a_t=r\alpha=(0.40)(6.0)=2.4\ \mathrm{m}/\mathrm{s}^2$.
- id: m1-ta-direct-b
  content: |-
    $2.4\ \mathrm{m}/\mathrm{s}^2$
  correct: true
  feedback: |-
    A fixed-radius point obeys $a_t=r\alpha$. Multiplying $0.40\ \mathrm{m}$ by $6.0\ \mathrm{rad}/\mathrm{s}^2$ gives $2.4\ \mathrm{m}/\mathrm{s}^2$ because radians are dimensionless.
- id: m1-ta-direct-c
  content: |-
    $2.4\ \mathrm{rad}/\mathrm{s}^2$
  feedback: |-
    The numerical product is right, but the unit is still angular. Multiplication by the radius converts the angular quantity to a linear one, so $a_t$ must be reported in $\mathrm{m}/\mathrm{s}^2$.
- id: m1-ta-direct-d
  content: |-
    $6.0\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    This copies the angular acceleration's number and ignores the point's radius. Since $a_t=r\alpha$, the factor $0.40$ changes the result to $2.4\ \mathrm{m}/\mathrm{s}^2$.
- id: m1-ta-direct-e
  content: |-
    $0.067\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    This forms $r/\alpha$, which is not the fixed-radius conversion and does not have acceleration units. Use the direct product $r\alpha$ to obtain $2.4\ \mathrm{m}/\mathrm{s}^2$.
```

---

<a id="solve-backward-for-angular-acceleration"></a>
## Solve Backward for Angular Acceleration

If the tangential acceleration is given, isolate $\alpha$ by dividing by the radius:

$$
\boxed{\alpha=\frac{a_t}{r}},\qquad r>0.
$$

**Example:** At a radius of $0.60\ \mathrm{m}$, a point has tangential acceleration $3.6\ \mathrm{m}/\mathrm{s}^2$. Find the object's angular acceleration.

**Explanation**

Treat the radius as the conversion factor and divide it out:

$$
\begin{aligned}
\alpha&=\frac{a_t}{r}\\
&=\frac{3.6\ \mathrm{m}/\mathrm{s}^2}{0.60\ \mathrm{m}}\\
&=6.0\ \mathrm{rad}/\mathrm{s}^2.
\end{aligned}
$$

The meters cancel. The resulting $\mathrm{s}^{-2}$ is conventionally written $\mathrm{rad}/\mathrm{s}^2$ for angular acceleration.

```quiz
type: radio
id: m1-ta-inverse
shuffle: true
content: |-
  A point $0.25\ \mathrm{m}$ from a rotation axis has tangential acceleration $2.0\ \mathrm{m}/\mathrm{s}^2$. What is the angular acceleration?
options:
- id: m1-ta-inverse-a
  content: |-
    $0.50\ \mathrm{rad}/\mathrm{s}^2$
  feedback: |-
    This multiplies $a_t$ by $r$, which would apply the conversion in the wrong direction. To recover angular acceleration, divide out the radius: $\alpha=2.0/0.25=8.0\ \mathrm{rad}/\mathrm{s}^2$.
- id: m1-ta-inverse-b
  content: |-
    $2.0\ \mathrm{rad}/\mathrm{s}^2$
  feedback: |-
    This copies the tangential acceleration's number without removing the radius factor. Since $a_t=r\alpha$, divide by $0.25\ \mathrm{m}$ to obtain $8.0\ \mathrm{rad}/\mathrm{s}^2$.
- id: m1-ta-inverse-c
  content: |-
    $2.25\ \mathrm{rad}/\mathrm{s}^2$
  feedback: |-
    Adding the radius to the acceleration does not isolate $\alpha$, and the quantities have different units. Divide $a_t$ by $r$: $2.0/0.25=8.0\ \mathrm{rad}/\mathrm{s}^2$.
- id: m1-ta-inverse-d
  content: |-
    $8.0\ \mathrm{rad}/\mathrm{s}^2$
  correct: true
  feedback: |-
    The fixed-radius relation is $a_t=r\alpha$, so the inverse move is $\alpha=a_t/r$. Dividing $2.0\ \mathrm{m}/\mathrm{s}^2$ by $0.25\ \mathrm{m}$ gives $8.0\ \mathrm{rad}/\mathrm{s}^2$.
- id: m1-ta-inverse-e
  content: |-
    $0.125\ \mathrm{rad}/\mathrm{s}^2$
  feedback: |-
    This reverses the quotient and computes $r/a_t$. The requested angular acceleration is the tangential acceleration per unit radius, so $\alpha=a_t/r=8.0\ \mathrm{rad}/\mathrm{s}^2$.
```

---

<a id="carry-the-sign-into-the-tangential-direction"></a>
## Carry the Sign into the Tangential Direction

First choose a positive rotational direction. The positive tangential direction at each point is the direction that positive rotation would carry that point.

Because $r$ is a positive distance, $a_t=r\alpha$ has the same sign as $\alpha$:

- $\alpha>0$ gives tangential acceleration in the positive tangential direction;
- $\alpha<0$ gives tangential acceleration in the negative tangential direction.

The sign of $\alpha$ alone does **not** determine whether the rotation is speeding up. Compare $\omega$ and $\alpha$:

- same signs $\Rightarrow$ the magnitude $|\omega|$ increases;
- opposite signs $\Rightarrow$ the magnitude $|\omega|$ decreases.

**Example:** Counterclockwise is positive. A wheel currently has $\omega=+7.0\ \mathrm{rad}/\mathrm{s}$ and $\alpha=-4.0\ \mathrm{rad}/\mathrm{s}^2$. For a point at $r=0.50\ \mathrm{m}$,

$$
a_t=r\alpha=(0.50)(-4.0)=-2.0\ \mathrm{m}/\mathrm{s}^2.
$$

The tangential acceleration is in the negative tangential direction. Since $\omega$ and $\alpha$ have opposite signs, the wheel is slowing down at this instant.

```quiz
type: radio
id: m1-ta-sign
shuffle: true
content: |-
  Counterclockwise rotation is positive. A disk currently has $\omega=+5.0\ \mathrm{rad}/\mathrm{s}$ and $\alpha=-3.0\ \mathrm{rad}/\mathrm{s}^2$. What describes a point at radius $0.80\ \mathrm{m}$?
options:
- id: m1-ta-sign-a
  content: |-
    $a_t=+2.4\ \mathrm{m}/\mathrm{s}^2$, and the disk is speeding up.
  feedback: |-
    This uses the correct magnitude but drops the sign of $\alpha$. Since $r>0$, $a_t$ has the same sign as $\alpha$, so $a_t=-2.4\ \mathrm{m}/\mathrm{s}^2$; its sign opposes $\omega$, so the disk is slowing down.
- id: m1-ta-sign-b
  content: |-
    $a_t=-2.4\ \mathrm{m}/\mathrm{s}^2$, and the disk is speeding up.
  feedback: |-
    The tangential acceleration is computed correctly, but speeding up depends on the signs of both $\omega$ and $\alpha$. Here they are opposite, so $|\omega|$ is decreasing and the disk is slowing down.
- id: m1-ta-sign-c
  content: |-
    $a_t=-2.4\ \mathrm{m}/\mathrm{s}^2$, and the disk is slowing down.
  correct: true
  feedback: |-
    Fixed-radius conversion gives $a_t=r\alpha=(0.80)(-3.0)=-2.4\ \mathrm{m}/\mathrm{s}^2$. Because $\omega$ is positive while $\alpha$ is negative, the angular speed $|\omega|$ is decreasing.
- id: m1-ta-sign-d
  content: |-
    $a_t=-3.75\ \mathrm{m}/\mathrm{s}^2$, and the disk is slowing down.
  feedback: |-
    The speeding/slowing conclusion is right, but $3.75$ comes from dividing $\alpha$ by $r$. To convert angular acceleration to tangential acceleration, multiply: $(0.80)(-3.0)=-2.4\ \mathrm{m}/\mathrm{s}^2$.
- id: m1-ta-sign-e
  content: |-
    $a_t=0$, because the radius is constant.
  feedback: |-
    Holding $r$ fixed means the point does not move toward or away from the axis; it does not force tangential speed to be constant. Since $\alpha=-3.0\ \mathrm{rad}/\mathrm{s}^2$, the point has $a_t=r\alpha=-2.4\ \mathrm{m}/\mathrm{s}^2$.
```

---

<a id="keep-tangential-and-radial-acceleration-separate"></a>
## Keep Tangential and Radial Acceleration Separate

Circular motion has two different acceleration jobs:

| Component | Governing quantity | Fixed-radius relation | What it changes |
|---|---|---|---|
| Tangential | $\alpha$ | $a_t=r\alpha$ | Speed along the path |
| Radial | $\omega$ | $a_r=r\omega^2$ in magnitude | Direction of the velocity |

An object can therefore have $\alpha=0$ and $a_t=0$ while still having nonzero radial acceleration. Constant angular speed does not mean zero total acceleration.

**Example:** A point at $r=0.30\ \mathrm{m}$ moves with $\omega=4.0\ \mathrm{rad}/\mathrm{s}$ and $\alpha=0$. Then

$$
a_t=r\alpha=0,
$$

while the inward radial acceleration has magnitude

$$
a_r=r\omega^2=(0.30)(4.0)^2=4.8\ \mathrm{m}/\mathrm{s}^2.
$$

The point's speed is constant, but the direction of its velocity is changing.

```quiz
type: radio
id: m1-ta-components
shuffle: true
content: |-
  A point on a wheel is $0.20\ \mathrm{m}$ from the axis. At one instant, $\omega=5.0\ \mathrm{rad}/\mathrm{s}$ and $\alpha=0$. Which statement correctly separates its acceleration components?
options:
- id: m1-ta-components-a
  content: |-
    $a_t=0$, while $a_r=5.0\ \mathrm{m}/\mathrm{s}^2$ inward.
  correct: true
  feedback: |-
    Tangential acceleration follows $\alpha$, so $a_t=r\alpha=0$. Radial acceleration follows angular speed, so $a_r=r\omega^2=(0.20)(5.0)^2=5.0\ \mathrm{m}/\mathrm{s}^2$ inward.
- id: m1-ta-components-b
  content: |-
    $a_t=5.0\ \mathrm{m}/\mathrm{s}^2$ inward, while $a_r=0$.
  feedback: |-
    This swaps the two components. The inward component is radial and depends on $\omega^2$; the tangential component depends on $\alpha$, which is zero here.
- id: m1-ta-components-c
  content: |-
    Both $a_t$ and $a_r$ are zero because $\alpha=0$.
  feedback: |-
    Zero angular acceleration makes the angular speed constant, so $a_t=0$. The velocity direction still changes around the circle, producing $a_r=r\omega^2=5.0\ \mathrm{m}/\mathrm{s}^2$ inward.
- id: m1-ta-components-d
  content: |-
    $a_t=1.0\ \mathrm{m}/\mathrm{s}^2$, while $a_r=5.0\ \mathrm{m}/\mathrm{s}^2$ inward.
  feedback: |-
    The product $r\omega=(0.20)(5.0)=1.0\ \mathrm{m}/\mathrm{s}$ is tangential speed, not tangential acceleration. Since $\alpha=0$, $a_t=0$; the radial value is $5.0\ \mathrm{m}/\mathrm{s}^2$.
- id: m1-ta-components-e
  content: |-
    $a_t=0$, while $a_r=1.0\ \mathrm{m}/\mathrm{s}^2$ inward.
  feedback: |-
    The tangential component is correctly zero, but $1.0$ comes from $r\omega$, which is the tangential speed in $\mathrm{m}/\mathrm{s}$. Radial acceleration requires $r\omega^2$, giving $5.0\ \mathrm{m}/\mathrm{s}^2$.
```

---

<a id="summary"></a>
## Summary

For a point held at a fixed radius:

1. Identify whether the problem asks for the speed-changing tangential component.
2. Convert angular to tangential acceleration with
   $$
   a_t=r\alpha.
   $$
3. If $\alpha$ is requested, divide out the radius:
   $$
   \alpha=\frac{a_t}{r}.
   $$
4. Keep the sign: because $r>0$, $a_t$ and $\alpha$ have the same sign.
5. Check the units: $\mathrm{m}\cdot\mathrm{rad}/\mathrm{s}^2$ becomes $\mathrm{m}/\mathrm{s}^2$.

The main trap is swapping the components. Angular acceleration $\alpha$ controls $a_t$ and changes speed; angular velocity $\omega$ controls the inward radial acceleration $a_r=r\omega^2$ and changes direction.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
