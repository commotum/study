# Radial, Tangential, and Net Acceleration

<!--
lesson-id: 212-M1-078
topic-code: M1.78
-->

## Table of Contents

- [Introduction](#introduction)
- [Decide Which Components Are Present](#decide-which-components-are-present)
- [Find Tangential Acceleration From Changing Angular Velocity](#find-tangential-acceleration-from-changing-angular-velocity)
- [Find Radial Acceleration From Linear Speed](#find-radial-acceleration-from-linear-speed)
- [Find Radial Acceleration From Angular Speed](#find-radial-acceleration-from-angular-speed)
- [Combine Perpendicular Components](#combine-perpendicular-components)
- [Work Through the Later Source-Video Cases](#work-through-the-later-source-video-cases)
- [Summary](#summary)

## Prerequisites

- Compute a signed change as final minus initial.
- Distinguish angular speed $|\omega|$ from angular acceleration $\alpha$.
- Use the Pythagorean theorem and inverse tangent in a right triangle.

---

<a id="introduction"></a>
## Introduction

Acceleration records any change in the velocity vector. On a circular path, the velocity's direction changes even when its speed is constant, producing an inward radial component. If the speed also changes, the velocity's magnitude changes too, producing a tangential component.

Before choosing an equation for circular motion, determine which acceleration components are present:

1. Is it moving along the circular path? If so, it has inward **radial acceleration**.
2. Is its speed changing? If so, it also has **tangential acceleration**.

The component magnitudes are

$$
a_r=\frac{v^2}{r}=\omega^2r,
\qquad
a_t=r\alpha.
$$

Radial acceleration, also called centripetal acceleration, points toward the circle's center and changes the velocity's direction. Tangential acceleration lies along the tangent and changes the speed. The two directions are perpendicular.

For constant-speed circular motion, $a_t=0$ but $a_r\ne0$. When the speed changes, first add the components as vectors and then find the resultant's magnitude:

$$
\vec a=\vec a_r+\vec a_t,
\qquad
|\vec a|=\sqrt{a_r^2+a_t^2}.
$$

---

<a id="decide-which-components-are-present"></a>
## Decide Which Components Are Present

**Example (source video):** At the rightmost point of a circular path, an object is moving north and speeding up. What directions do its radial, tangential, and net acceleration point?

**Explanation**

The circle's center is west of the object, so the inward radial component points west. Because the object is moving north and speeding up, the tangential component points north, with the velocity. The two components are perpendicular, and their vector sum points northwest. This is the same right-triangle structure used later to calculate its magnitude.

The direction of $\vec a_t$ depends on the speed change:

- If the object is speeding up, $\vec a_t$ points with the velocity.
- If the object is slowing down, $\vec a_t$ points opposite the velocity.
- If the speed is constant, $\vec a_t=0$.

```quiz
type: radio
id: mct-p4-components
content: |-
  A rider is at the top of a circular track, moving west and slowing down. Which directions describe the rider's acceleration components and net acceleration?
options:
- id: mct-p4-components-a
  content: |-
    $\vec a_r$ points south, $\vec a_t$ points east, and $\vec a$ points southeast.
  correct: true
  feedback: |-
    Radial acceleration always points toward the center, which is south from the top of the circle. Because the rider is slowing while moving west, tangential acceleration points east, opposite the velocity; their sum points southeast.
- id: mct-p4-components-b
  content: |-
    $\vec a_r$ points south, $\vec a_t$ points west, and $\vec a$ points southwest.
  feedback: |-
    A westward tangential component would make a westward-moving rider speed up. Here the rider is slowing, so $\vec a_t$ must point east while $\vec a_r$ still points south.
- id: mct-p4-components-c
  content: |-
    $\vec a_r$ points north, $\vec a_t$ points east, and $\vec a$ points northeast.
  feedback: |-
    The tangential direction correctly opposes the westward velocity, but radial acceleration is reversed. At the top of the track, the center lies south, so $\vec a_r$ points south rather than outward to the north.
- id: mct-p4-components-d
  content: |-
    Only $\vec a_t$ is present, so $\vec a$ points east.
  feedback: |-
    Tangential acceleration accounts for slowing, but following a curved path also changes the velocity's direction. The rider therefore has an inward radial component in addition to the eastward tangential component.
- id: mct-p4-components-e
  content: |-
    Only $\vec a_r$ is present, so $\vec a$ points south.
  feedback: |-
    Radial acceleration alone describes constant-speed circular motion. Because the rider's speed is decreasing, an eastward tangential component is also present.
```

---

<a id="find-tangential-acceleration-from-changing-angular-velocity"></a>
## Find Tangential Acceleration From Changing Angular Velocity

The relation $a_t=r\alpha$ applies instant by instant. When a problem instead gives endpoint angular velocities over a finite interval, use the corresponding average quantities. Average angular acceleration is the signed change in angular velocity per elapsed time:

$$
\alpha_{\mathrm{avg}}=\frac{\Delta\omega}{\Delta t}
=\frac{\omega_f-\omega_i}{\Delta t}.
$$

At a fixed radius, the corresponding average tangential acceleration is

$$
a_{t,\mathrm{avg}}=r\alpha_{\mathrm{avg}}.
$$

The sign of $\alpha$ tells how signed angular velocity changes. When $\alpha$ and $\omega$ have the same sign, angular speed increases; when their signs are opposite, angular speed decreases. Thus $a_t=r\alpha$ gives the tangential component, not the radial or total acceleration.

**Example (source video):** A disk of radius $0.30\,\mathrm{m}$ increases its angular velocity from $20\,\mathrm{rad/s}$ to $40\,\mathrm{rad/s}$ in $5\,\mathrm{s}$. Find its average angular acceleration and the average tangential acceleration at its rim.

**Explanation**

First compute final minus initial and divide by the elapsed time:

$$
\alpha_{\mathrm{avg}}
=\frac{40\,\mathrm{rad/s}-20\,\mathrm{rad/s}}{5\,\mathrm{s}}
=4\,\mathrm{rad/s^2}.
$$

Then multiply by the radius to find the tangential acceleration at the rim:

$$
a_{t,\mathrm{avg}}
=(0.30\,\mathrm{m})(4\,\mathrm{rad/s^2})
=1.2\,\mathrm{m/s^2}.
$$

The disk is speeding up, so the tangential acceleration points in the same tangential direction as the rim's velocity.

```quiz
type: radio
id: mct-p4-tangential
content: |-
  A wheel of radius $0.40\,\mathrm{m}$ increases its angular velocity from $12\,\mathrm{rad/s}$ to $22\,\mathrm{rad/s}$ in $5.0\,\mathrm{s}$. Which pair gives $\alpha_{\mathrm{avg}}$ and the rim's $a_{t,\mathrm{avg}}$?
options:
- id: mct-p4-tangential-a
  content: |-
    $\alpha_{\mathrm{avg}}=2.0\,\mathrm{rad/s^2}$ and $a_{t,\mathrm{avg}}=0.80\,\mathrm{m/s^2}$
  correct: true
  feedback: |-
    Angular acceleration is change in angular velocity per time: $(22-12)/5.0=2.0\,\mathrm{rad/s^2}$. Multiplying by the $0.40\,\mathrm{m}$ radius gives $a_{t,\mathrm{avg}}=0.80\,\mathrm{m/s^2}$.
- id: mct-p4-tangential-b
  content: |-
    $\alpha_{\mathrm{avg}}=6.8\,\mathrm{rad/s^2}$ and $a_{t,\mathrm{avg}}=2.72\,\mathrm{m/s^2}$
  feedback: |-
    This adds the endpoint angular velocities before dividing. Acceleration uses the change $\omega_f-\omega_i=10\,\mathrm{rad/s}$, not the sum $34\,\mathrm{rad/s}$.
- id: mct-p4-tangential-c
  content: |-
    $\alpha_{\mathrm{avg}}=10\,\mathrm{rad/s^2}$ and $a_{t,\mathrm{avg}}=4.0\,\mathrm{m/s^2}$
  feedback: |-
    $10\,\mathrm{rad/s}$ is the change in angular velocity, not the angular acceleration. Divide by the $5.0\,\mathrm{s}$ interval before multiplying by the radius.
- id: mct-p4-tangential-d
  content: |-
    $\alpha_{\mathrm{avg}}=2.0\,\mathrm{rad/s^2}$ and $a_{t,\mathrm{avg}}=5.0\,\mathrm{m/s^2}$
  feedback: |-
    The angular acceleration is correct, but tangential acceleration is $r\alpha$, not $\alpha/r$. A point farther from the axis has a larger tangential acceleration for the same $\alpha$.
- id: mct-p4-tangential-e
  content: |-
    $\alpha_{\mathrm{avg}}=-2.0\,\mathrm{rad/s^2}$ and $a_{t,\mathrm{avg}}=-0.80\,\mathrm{m/s^2}$
  feedback: |-
    This reverses final minus initial. Since the signed angular velocity rises from $12$ to $22\,\mathrm{rad/s}$, $\omega_f-\omega_i$ and therefore $\alpha_{\mathrm{avg}}$ are positive.
```

---

<a id="find-radial-acceleration-from-linear-speed"></a>
## Find Radial Acceleration From Linear Speed

When the tangential speed $v$ and radius $r$ are given, use

$$
a_r=\frac{v^2}{r}.
$$

**Example:** A cart moves at $6.0\,\mathrm{m/s}$ around a circular path of radius $2.0\,\mathrm{m}$. Find its radial acceleration.

**Explanation**

Square the speed before dividing by the radius:

$$
a_r=\frac{(6.0\,\mathrm{m/s})^2}{2.0\,\mathrm{m}}
=18\,\mathrm{m/s^2}.
$$

This $18\,\mathrm{m/s^2}$ component points inward. Even if the cart's speed is constant, its velocity changes direction and the inward acceleration remains.

The radial and tangential formulas both produce acceleration units because radians are dimensionless:

$$
[a_r]=\frac{(\mathrm{m/s})^2}{\mathrm m}
=\mathrm{m/s^2},
\qquad
[a_t]=(\mathrm m)(\mathrm{rad/s^2})
=\mathrm{m/s^2}.
$$

```quiz
type: radio
id: mct-p4-radial-linear
content: |-
  A puck moves at a constant $8.0\,\mathrm{m/s}$ on a circular path of radius $4.0\,\mathrm{m}$. What is its acceleration?
options:
- id: mct-p4-radial-linear-a
  content: |-
    $16\,\mathrm{m/s^2}$ inward
  correct: true
  feedback: |-
    Circular motion requires inward radial acceleration. Using $a_r=v^2/r$ gives $(8.0)^2/4.0=16\,\mathrm{m/s^2}$ toward the center.
- id: mct-p4-radial-linear-b
  content: |-
    $2.0\,\mathrm{m/s^2}$ inward
  feedback: |-
    This uses $v/r$ and omits the square on speed. Radial acceleration depends on $v^2$, so doubling speed would quadruple—not double—the inward acceleration.
- id: mct-p4-radial-linear-c
  content: |-
    $256\,\mathrm{m/s^2}$ inward
  feedback: |-
    This multiplies $v^2$ by $r$. The governing relationship divides by radius: $a_r=64/4.0=16\,\mathrm{m/s^2}$.
- id: mct-p4-radial-linear-d
  content: |-
    $16\,\mathrm{m/s^2}$ tangent to the path
  feedback: |-
    The magnitude is correct, but $v^2/r$ is the radial component, which points toward the center. A tangential component would require the speed to change.
- id: mct-p4-radial-linear-e
  content: |-
    $0\,\mathrm{m/s^2}$ because the speed is constant
  feedback: |-
    Constant speed removes tangential acceleration, not radial acceleration. The puck's velocity direction changes continuously, requiring $16\,\mathrm{m/s^2}$ inward.
```

---

<a id="find-radial-acceleration-from-angular-speed"></a>
## Find Radial Acceleration From Angular Speed

When angular speed $|\omega|$ and radius are given, use

$$
a_r=\omega^2r.
$$

This is the same radial rule because $v=r|\omega|$:

$$
\frac{v^2}{r}
=\frac{(r|\omega|)^2}{r}
=\omega^2r.
$$

**Example:** A point on a rotor is $0.40\,\mathrm{m}$ from the axis and has angular speed $5.0\,\mathrm{rad/s}$. Find its radial acceleration.

**Explanation**

$$
a_r=(5.0\,\mathrm{rad/s})^2(0.40\,\mathrm{m})
=10\,\mathrm{m/s^2}.
$$

The sign of angular velocity does not reverse the inward direction because it is squared. Clockwise and counterclockwise motion at the same angular speed and radius have the same radial-acceleration magnitude.

```quiz
type: radio
id: mct-p4-radial-angular
content: |-
  A sensor is $0.80\,\mathrm{m}$ from a rotation axis and has angular speed $3.0\,\mathrm{rad/s}$. What is its radial acceleration?
options:
- id: mct-p4-radial-angular-a
  content: |-
    $7.2\,\mathrm{m/s^2}$ inward
  correct: true
  feedback: |-
    With angular speed given, $a_r=\omega^2r$. Substituting gives $(3.0)^2(0.80)=7.2\,\mathrm{m/s^2}$ toward the axis.
- id: mct-p4-radial-angular-b
  content: |-
    $2.4\,\mathrm{m/s^2}$ inward
  feedback: |-
    The product $r\omega=2.4\,\mathrm{m/s}$ is tangential speed, not acceleration. Radial acceleration requires another factor of $\omega$: $a_r=\omega^2r$.
- id: mct-p4-radial-angular-c
  content: |-
    $11.25\,\mathrm{m/s^2}$ inward
  feedback: |-
    This divides $\omega^2$ by $r$, but the angular-speed form multiplies by radius. The division form is $v^2/r$ when linear speed—not angular speed—is given.
- id: mct-p4-radial-angular-d
  content: |-
    $7.2\,\mathrm{m/s^2}$ outward
  feedback: |-
    The calculation has the right magnitude, but radial acceleration for circular motion points inward, toward the rotation axis, rather than outward.
- id: mct-p4-radial-angular-e
  content: |-
    $0\,\mathrm{m/s^2}$ unless the angular speed is changing
  feedback: |-
    Changing angular speed controls tangential acceleration. A nonzero angular speed on a circle already changes the velocity's direction, so it produces nonzero inward radial acceleration.
```

---

<a id="combine-perpendicular-components"></a>
## Combine Perpendicular Components

When both components are present, do not add their magnitudes directly. The resultant is $\vec a=\vec a_r+\vec a_t$. Because the two components are perpendicular, their magnitudes form the legs of a right triangle and $|\vec a|$ is its hypotenuse.

**Example:** At one instant, a vehicle has radial acceleration $a_r=12\,\mathrm{m/s^2}$ inward and tangential acceleration $a_t=5.0\,\mathrm{m/s^2}$. Find the net acceleration magnitude and its direction relative to inward.

**Explanation**

Use the Pythagorean theorem for the magnitude:

$$
|\vec a|
=\sqrt{(12\,\mathrm{m/s^2})^2+(5.0\,\mathrm{m/s^2})^2}
=13\,\mathrm{m/s^2}.
$$

If $\phi$ is measured from the inward radial direction toward the tangential component, then

$$
\tan\phi=\frac{|a_t|}{a_r}
=\frac{5.0}{12},
\qquad
\phi\approx22.6^\circ.
$$

Thus the net acceleration is $13\,\mathrm{m/s^2}$, directed $22.6^\circ$ away from inward toward $\vec a_t$.

```quiz
type: radio
id: mct-p4-net
content: |-
  At one instant, an object has $a_r=9.0\,\mathrm{m/s^2}$ inward and $a_t=12\,\mathrm{m/s^2}$. What are the net acceleration magnitude and the angle measured from inward toward $\vec a_t$?
options:
- id: mct-p4-net-a
  content: |-
    $15\,\mathrm{m/s^2}$ at $53.1^\circ$
  correct: true
  feedback: |-
    The components are perpendicular, so $|\vec a|=\sqrt{9.0^2+12^2}=15\,\mathrm{m/s^2}$. Measured from inward, $\tan\phi=12/9$, giving $\phi=53.1^\circ$ toward $\vec a_t$.
- id: mct-p4-net-b
  content: |-
    $21\,\mathrm{m/s^2}$ at $53.1^\circ$
  feedback: |-
    The direction ratio is appropriate, but $9.0+12$ adds perpendicular magnitudes as if they were parallel. Perpendicular components combine through $\sqrt{a_r^2+a_t^2}$.
- id: mct-p4-net-c
  content: |-
    $15\,\mathrm{m/s^2}$ at $36.9^\circ$
  feedback: |-
    The magnitude is correct, but $36.9^\circ$ is measured from the tangential component. Because the requested reference is inward, use opposite-over-adjacent $a_t/a_r=12/9$ to get $53.1^\circ$.
- id: mct-p4-net-d
  content: |-
    $3.0\,\mathrm{m/s^2}$ at $53.1^\circ$
  feedback: |-
    Subtracting the component magnitudes is not valid because the components are perpendicular, not opposite. Their vector sum is the hypotenuse, so it is larger than either component.
- id: mct-p4-net-e
  content: |-
    $225\,\mathrm{m/s^2}$ at $53.1^\circ$
  feedback: |-
    The sum $9.0^2+12^2=225$ is the square of the net magnitude and has squared units. Taking the square root gives $15\,\mathrm{m/s^2}$.
```

---

<a id="work-through-the-later-source-video-cases"></a>
## Work Through the Later Source-Video Cases

The later videos reuse the same decision sequence with different givens: determine whether the rate change produces $a_t$, determine whether circular motion produces $a_r$, and combine the two only when both are present.

### Signed angular acceleration

**Source-video Problem 1:** A wheel starts from rest and reaches $30\,\mathrm{rad/s}$ in $5\,\mathrm s$. Its average angular acceleration is

$$
\alpha_{\mathrm{avg}}
=\frac{30-0}{5}
=6\,\mathrm{rad/s^2}.
$$

**Source-video Problem 2:** With counterclockwise chosen positive, a wheel changes from $+85$ to $+25\,\mathrm{rad/s}$ in $4\,\mathrm s$:

$$
\alpha_{\mathrm{avg}}
=\frac{25-85}{4}
=-15\,\mathrm{rad/s^2}.
$$

The wheel still rotates counterclockwise because $\omega$ remains positive, but it slows because $\omega$ and $\alpha$ have opposite signs. The four sign cases are:

| $\omega$ | $\alpha$ | What happens to angular speed? |
| --- | --- | --- |
| positive | positive | increases |
| positive | negative | decreases |
| negative | negative | increases |
| negative | positive | decreases |

The sign of $\omega$ gives rotation direction. Comparing the signs of $\omega$ and $\alpha$ tells whether the magnitude $|\omega|$ grows or shrinks.

### Radial-acceleration checks

From $a_r=v^2/r$, doubling $v$ multiplies $a_r$ by $4$, tripling $v$ multiplies it by $9$, doubling $r$ halves it, and halving $r$ doubles it. If $v$ is tripled while $r$ is divided by four, then

$$
\frac{a_{r,f}}{a_{r,i}}
=\frac{(3v)^2/(r/4)}{v^2/r}
=36.
$$

**Source-video Problem 3:** A $30\,\mathrm{cm}$-diameter wheel has the rim speed $v=6\,\mathrm{m/s}$ found in Lesson 2. Its radius is $0.15\,\mathrm m$, so

$$
a_r=\frac{v^2}{r}
=\frac{(6\,\mathrm{m/s})^2}{0.15\,\mathrm m}
=240\,\mathrm{m/s^2}.
$$

**Source-video penny problem:** A penny $45\,\mathrm{cm}$ from a disk's center moves at $2.5\,\mathrm{m/s}$. After converting $r=0.45\,\mathrm m$,

$$
a_r=\frac{2.5^2}{0.45}
=13.9\,\mathrm{m/s^2}.
$$

**Source-video ball problem:** A ball moves on a circle of radius $1.5\,\mathrm m$ with period $T=1/3\,\mathrm s$. Starting from $v=2\pi r/T$ gives

$$
a_r=\frac{v^2}{r}
=\frac{4\pi^2r}{T^2}
=\frac{4\pi^2(1.5)}{(1/3)^2}
\approx533\,\mathrm{m/s^2}.
$$

**Source-video Earth–Sun problem:** Use $r=150\times10^6\,\mathrm{km}=1.5\times10^{11}\,\mathrm m$ and $T=31{,}536{,}000\,\mathrm s$:

$$
a_r=\frac{4\pi^2r}{T^2}
=5.95\times10^{-3}\,\mathrm{m/s^2}.
$$

**Source-video jet problem:** A jet moving at $400\,\mathrm{m/s}$ turns with radius $4\,\mathrm{km}=4000\,\mathrm m$:

$$
a_r=\frac{400^2}{4000}
=40\,\mathrm{m/s^2}
=4.08g.
$$

This compares acceleration with $g$; it does not by itself establish a force model or literal apparent weight.

### Both components at once

**Source-video Problem 4:** A point at $r=1.5\,\mathrm{cm}=0.015\,\mathrm m$ changes from $20$ to $100\,\mathrm{rad/s}$ in $2\,\mathrm s$, so

$$
\alpha_{\mathrm{avg}}=\frac{100-20}{2}=40\,\mathrm{rad/s^2}.
$$

At the instant when its angular speed is $60\,\mathrm{rad/s}$—not its average angular speed—the two components are

$$
a_r=\omega^2r=(60)^2(0.015)=54\,\mathrm{m/s^2},
$$

$$
a_t=r\alpha=(0.015)(40)=0.60\,\mathrm{m/s^2}.
$$

Therefore

$$
a_{\mathrm{net}}
=\sqrt{54^2+0.60^2}
=54.003\,\mathrm{m/s^2}.
$$

**Source-video nonuniform-circle problem:** A $1200\,\mathrm{kg}$ car goes from rest to $40\,\mathrm{m/s}$ in $5\,\mathrm s$ while following a circular path of radius $800\,\mathrm m$. Its tangential and final radial accelerations are

$$
a_t=\frac{40-0}{5}=8\,\mathrm{m/s^2},
\qquad
a_r=\frac{40^2}{800}=2\,\mathrm{m/s^2}.
$$

Thus

$$
a_{\mathrm{net}}=\sqrt{8^2+2^2}=8.25\,\mathrm{m/s^2},
$$

$$
F_{\mathrm{net}}=ma_{\mathrm{net}}
\approx(1200)(8.246)
\approx9899\,\mathrm N.
$$

The force components are $F_t=1200(8)=9600\,\mathrm N$ and $F_r=1200(2)=2400\,\mathrm N$. Measured inward from the forward tangent, the resultant points at

$$
\phi=\tan^{-1}\left(\frac{a_r}{a_t}\right)
=\tan^{-1}\left(\frac{2}{8}\right)
=14.04^\circ.
$$

The $9899\,\mathrm N$ result follows from the displayed components; inconsistent nearby spoken values in the source do not.

---

<a id="summary"></a>
## Summary

Use this checklist for circular-motion acceleration:

1. If the object is moving on a circle, include inward radial acceleration. Use $a_r=v^2/r$ when $v$ is given or $a_r=\omega^2r$ when $\omega$ is given.
2. If angular velocity changes, find $\alpha_{\mathrm{avg}}=(\omega_f-\omega_i)/\Delta t$ and then $a_{t,\mathrm{avg}}=r\alpha_{\mathrm{avg}}$.
3. Point $\vec a_t$ with the velocity when speed increases and opposite the velocity when speed decreases. Constant speed means $a_t=0$, not zero total acceleration.
4. When both components are present, use $|\vec a|=\sqrt{a_r^2+a_t^2}$ because the components are perpendicular.
5. For a direction measured from inward toward the tangent, use $\tan\phi=|a_t|/a_r$.

The main traps are omitting radial acceleration at constant speed, forgetting the square in $v^2/r$ or $\omega^2r$, treating $a_t=r\alpha$ as the total acceleration, and adding perpendicular component magnitudes directly.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
