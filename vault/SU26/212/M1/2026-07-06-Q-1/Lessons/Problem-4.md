# Resolving Vertical-Circle Motion with r-t Axes

<!--
lesson-id: 212-M1-070
topic-code: MTH212.M1.70
-->
## Table of Contents

- [Introduction](#introduction)
- [Draw the Axes and Real Forces](#draw-the-axes-and-real-forces)
- [Resolve Weight onto the r-t Axes](#resolve-weight-onto-the-r-t-axes)
- [Write the Component Equations](#write-the-component-equations)
- [Combine Components for Total Acceleration](#combine-components-for-total-acceleration)
- [Use Radial Acceleration to Find Angular Speed](#use-radial-acceleration-to-find-angular-speed)
- [Summary](#summary)

## Prerequisites

- Resolve a vector into components with sine and cosine.
- Apply Newton's second law along a chosen axis.
- Use $v=r\omega$ and $a_r=v^2/r=r\omega^2$ for motion along a circle of radius $r$.

---

<a id="introduction"></a>
## Introduction

When an object moves on a curved path, choose axes that follow the path at the instant of interest:

- $+r$ points inward, toward the center of curvature.
- $+t$ is tangent to the path and points in the direction of motion.

The key move is to resolve every real force onto these signed axes, apply $\sum F_r=m a_r$ and $\sum F_t=m a_t$, and keep the two acceleration components in their separate roles. Use both components to find $|\vec{a}|$, but use only $a_r$ in the circular-motion relation $a_r=r\omega^2$.

Match the requested output to the right operation:

| Requested output | Use |
|---|---|
| Signed radial acceleration | $\sum F_r=m a_r$ |
| Signed tangential acceleration | $\sum F_t=m a_t$ |
| Total acceleration magnitude | $|\vec{a}|=\sqrt{a_r^2+a_t^2}$ |
| Angular speed | $a_r=r\omega^2$ |

For the key in the source problem, the geometry is:

![](../Source/2026-07-06-Q-1/Images/quiz-1a-q4-vertical-rotation-key.png)

The key is below and left of the center, and it is moving generally upward. Thus $+r$ points up-right and $+t$ points up-left.

---

<a id="draw-the-axes-and-real-forces"></a>
## Draw the Axes and Real Forces

**Example:** Draw the free-body diagram for the key at the instant shown.

**Explanation**

Draw forces first, then resolve them:

- Tension $T_{\mathrm{tens}}$ points along the string toward the center, exactly in the $+r$ direction.
- Weight $mg$ points vertically downward.

There is no additional "centripetal force." The inward radial acceleration is produced here by the radial components of the real forces.

```quiz
type: radio
id: p4-fbd
content: |-
  Which description gives the complete free-body diagram for the key at the instant shown?
options:
- id: p4-fbd-a
  content: |-
    Tension points inward along $+r$, and weight points vertically downward.
  correct: true
  feedback: |-
    A free-body diagram contains only real interactions. The string pulls the key inward along $+r$, and Earth pulls it vertically downward, so these are the two force vectors to draw.
- id: p4-fbd-b
  content: |-
    Tension points inward, weight points downward, and a separate centripetal force points inward.
  feedback: |-
    "Centripetal" names the inward net-force requirement $m a_r$, not a third interaction. Adding it as a separate force would count the radial effect of tension and gravity twice.
- id: p4-fbd-c
  content: |-
    Tension points tangent to the circle in the direction of motion, and weight points downward.
  feedback: |-
    Tension acts along the string, not along the velocity. At this instant the string lies on the radial axis, so tension points toward the center along $+r$; the tangent direction instead defines $+t$.
- id: p4-fbd-d
  content: |-
    Tension points inward, and weight points directly outward along $-r$.
  feedback: |-
    Weight remains vertically downward regardless of the chosen axes. It has an outward radial component here, but it also has a tangential component, so replacing the whole weight vector by a purely radial vector loses part of the force.
- id: p4-fbd-e
  content: |-
    Only tension points inward because the key's weight is already included in its mass.
  feedback: |-
    Mass measures inertia; it does not replace the gravitational force. Near Earth's surface, gravity still exerts the separate real force $mg$ downward in addition to the string tension.
```

---

<a id="resolve-weight-onto-the-r-t-axes"></a>
## Resolve Weight onto the r-t Axes

**Example:** Determine the signed radial and tangential components of the key's weight when the string is at angle $\theta$ below the leftward horizontal, as shown.

**Explanation**

Predict the signs before choosing sine or cosine. Gravity points neither inward nor with the motion at this snapshot, so its projections must satisfy $F_{g,r}<0$ and $F_{g,t}<0$. Trigonometry then determines the two magnitudes.

The inward unit vector points up-right, so it may be written as

$$
\hat{r}=\langle \cos\theta,\sin\theta\rangle.
$$

The tangent unit vector in the direction of motion is $90^\circ$ counterclockwise from $\hat{r}$:

$$
\hat{t}=\langle-\sin\theta,\cos\theta\rangle.
$$

Since $m\vec{g}=\langle0,-mg\rangle$, dot products give

$$
F_{g,r}=m\vec{g}\cdot\hat{r}=-mg\sin\theta,
\qquad
F_{g,t}=m\vec{g}\cdot\hat{t}=-mg\cos\theta.
$$

The signs also follow from the picture: gravity points partly opposite $+r$ and partly opposite $+t$.

```quiz
type: radio
id: p4-weight-components
content: |-
  For the axes and angle shown, what are the signed components $(F_{g,r},F_{g,t})$ of the key's gravitational force?
options:
- id: p4-weight-components-a
  content: |-
    $(-mg\sin\theta,-mg\cos\theta)$
  correct: true
  feedback: |-
    Gravity points partly outward, opposite $+r$, and partly opposite the upward tangential direction $+t$. The angle projection therefore gives $F_{g,r}=-mg\sin\theta$ and $F_{g,t}=-mg\cos\theta$.
- id: p4-weight-components-b
  content: |-
    $(mg\sin\theta,mg\cos\theta)$
  feedback: |-
    These magnitudes match the two projections, but both signs conflict with the axes. A positive radial component would point toward the center and a positive tangential component would point with the motion; gravity points opposite both directions here.
- id: p4-weight-components-c
  content: |-
    $(-mg\cos\theta,-mg\sin\theta)$
  feedback: |-
    This swaps the projections. Because $\theta$ is measured from the horizontal, the downward component perpendicular to that horizontal contributes $mg\sin\theta$ radially, while the adjacent projection $mg\cos\theta$ is tangential.
- id: p4-weight-components-d
  content: |-
    $(mg\sin\theta,-mg\cos\theta)$
  feedback: |-
    The tangential sign is consistent with gravity opposing $+t$, but the radial sign is not. Gravity has an outward component at the lower-left position, so its radial component is negative: $F_{g,r}=-mg\sin\theta$.
- id: p4-weight-components-e
  content: |-
    $(-mg\sin\theta,mg\cos\theta)$
  feedback: |-
    The radial component is outward as written, but gravity also points opposite the up-left $+t$ direction. Its tangential component must therefore be negative, not positive.
```

---

<a id="write-the-component-equations"></a>
## Write the Component Equations

**Example:** Use Newton's second law to find the key's signed radial and tangential acceleration components.

**Explanation**

Tension contributes only in the radial direction. Using the gravitational-force components just found,

$$
\sum F_r=m a_r=m\frac{v^2}{r}=T_{\mathrm{tens}}+F_{g,r}=T_{\mathrm{tens}}-mg\sin\theta,
$$

so

$$
a_r=\frac{T_{\mathrm{tens}}}{m}-g\sin\theta.
$$

Only gravity contributes tangentially:

$$
\sum F_t=m a_t=F_{g,t}=-mg\cos\theta,
$$

so

$$
a_t=-g\cos\theta.
$$

The negative $a_t$ means that the tangential acceleration is opposite the direction of motion at this instant; it does not make the radial acceleration negative.

```quiz
type: radio
id: p4-acceleration-components
content: |-
  A mass $m$ has inward tension $T_{\mathrm{tens}}$ at the same kind of lower-left snapshot, with the string at angle $\theta$ below the horizontal. What are $(a_r,a_t)$?
options:
- id: p4-acceleration-components-a
  content: |-
    $\left(\dfrac{T_{\mathrm{tens}}}{m}-g\sin\theta,-g\cos\theta\right)$
  correct: true
  feedback: |-
    Radially, inward tension competes with the outward projection $mg\sin\theta$, so division by $m$ gives $a_r=T_{\mathrm{tens}}/m-g\sin\theta$. Tangentially, gravity opposes $+t$, giving $a_t=-g\cos\theta$.
- id: p4-acceleration-components-b
  content: |-
    $\left(T_{\mathrm{tens}}-mg\sin\theta,-mg\cos\theta\right)$
  feedback: |-
    These are the net force components, not acceleration components. Newton's second law requires dividing each net force by $m$, which changes them to $T_{\mathrm{tens}}/m-g\sin\theta$ and $-g\cos\theta$.
- id: p4-acceleration-components-c
  content: |-
    $\left(\dfrac{T_{\mathrm{tens}}}{m}+g\sin\theta,-g\cos\theta\right)$
  feedback: |-
    The tangential component is correct, but gravity does not reinforce the inward tension at this lower-left position. Its radial projection points outward, so it subtracts from $T_{\mathrm{tens}}/m$.
- id: p4-acceleration-components-d
  content: |-
    $\left(\dfrac{T_{\mathrm{tens}}}{m}-g\cos\theta,-g\sin\theta\right)$
  feedback: |-
    This interchanges the radial and tangential gravity projections. With $\theta$ measured below the horizontal, the outward radial magnitude is $g\sin\theta$ and the opposing tangential magnitude is $g\cos\theta$.
- id: p4-acceleration-components-e
  content: |-
    $\left(\dfrac{T_{\mathrm{tens}}}{m},-g\right)$
  feedback: |-
    Gravity is vertical, while the $r$-$t$ axes are tilted. Except at a special axis-aligned position, gravity contributes to both equations, so its radial and tangential projections cannot be omitted.
```

---

<a id="combine-components-for-total-acceleration"></a>
## Combine Components for Total Acceleration

**Example:** Find the magnitude of the key's total acceleration.

**Explanation**

Radial and tangential directions are perpendicular, so use the Pythagorean magnitude:

$$
|\vec{a}|=\sqrt{a_r^2+a_t^2}.
$$

Substituting the signed components gives

$$
|\vec{a}|
=\sqrt{\left(\frac{T_{\mathrm{tens}}}{m}-g\sin\theta\right)^2+
\left(-g\cos\theta\right)^2}
=\sqrt{\left(\frac{T_{\mathrm{tens}}}{m}-g\sin\theta\right)^2+
\left(g\cos\theta\right)^2}.
$$

Keep the signs while finding the components. Squaring removes the signs only when the perpendicular components are combined into a magnitude.

This component-to-magnitude step works for any rotated pair of perpendicular axes; the axes need not be horizontal and vertical.

```quiz
type: radio
id: p4-total-acceleration
content: |-
  Using $a_r=T_{\mathrm{tens}}/m-g\sin\theta$ and $a_t=-g\cos\theta$, which expression is the total acceleration magnitude?
options:
- id: p4-total-acceleration-a
  content: |-
    $\sqrt{\left(\dfrac{T_{\mathrm{tens}}}{m}-g\sin\theta\right)^2+\left(g\cos\theta\right)^2}$
  correct: true
  feedback: |-
    The radial and tangential components are perpendicular, so their squared magnitudes add. Substitution into $|\vec{a}|=\sqrt{a_r^2+a_t^2}$ gives the stated expression.
- id: p4-total-acceleration-b
  content: |-
    $\left(\dfrac{T_{\mathrm{tens}}}{m}-g\sin\theta\right)^2+\left(g\cos\theta\right)^2$
  feedback: |-
    This is $|\vec{a}|^2$, not $|\vec{a}|$. The Pythagorean sum of squares must be followed by a square root to recover an acceleration magnitude.
- id: p4-total-acceleration-c
  content: |-
    $\dfrac{T_{\mathrm{tens}}}{m}-g\sin\theta-g\cos\theta$
  feedback: |-
    Radial and tangential components lie on perpendicular axes, so they cannot be added as signed scalars. Their vector magnitude is found from the square root of the sum of their squares.
- id: p4-total-acceleration-d
  content: |-
    $\left|\dfrac{T_{\mathrm{tens}}}{m}-g\sin\theta\right|$
  feedback: |-
    This is only the magnitude of the radial component. The total acceleration also has the nonzero tangential component $-g\cos\theta$, which must be included in the Pythagorean magnitude.
- id: p4-total-acceleration-e
  content: |-
    $\sqrt{\left(\dfrac{T_{\mathrm{tens}}}{m}+g\sin\theta\right)^2+\left(g\cos\theta\right)^2}$
  feedback: |-
    This uses the correct magnitude structure but the wrong radial sign. Gravity's radial projection is outward at this position, so it subtracts from the inward tension term before the component is squared.
```

---

<a id="use-radial-acceleration-to-find-angular-speed"></a>
## Use Radial Acceleration to Find Angular Speed

**Example:** Find the key's angular speed at that instant.

**Explanation**

For motion on a circle of radius $r$, the inward radial acceleration is

$$
v=r\omega,
\qquad
a_r=\frac{v^2}{r}=r\omega^2.
$$

Use the radial component from Newton's second law—not the total magnitude and not the tangential component:

$$
r\omega^2=\frac{T_{\mathrm{tens}}}{m}-g\sin\theta.
$$

Therefore,

$$
\omega
=\sqrt{\frac{T_{\mathrm{tens}}/m-g\sin\theta}{r}}
=\sqrt{\frac{T_{\mathrm{tens}}-mg\sin\theta}{mr}}.
$$

The roles stay distinct: $a_r$ turns the velocity vector, while $a_t$ changes its magnitude. That is why $a_t$ contributes to $|\vec{a}|$ but not to $r\omega^2$.

**Sanity checks:** Because $a_r=r\omega^2\ge 0$, a physically consistent taut-string snapshot must satisfy $T_{\mathrm{tens}}/m-g\sin\theta\ge 0$. Also, $(a_r/r)$ has units of $1/\mathrm{s}^2$, so its square root has the angular-speed unit $\mathrm{rad}/\mathrm{s}$.

```quiz
type: radio
id: p4-angular-speed
content: |-
  If $a_r=T_{\mathrm{tens}}/m-g\sin\theta$ for a mass moving on a circle of radius $r$, which expression gives its angular speed?
options:
- id: p4-angular-speed-a
  content: |-
    $\sqrt{\dfrac{T_{\mathrm{tens}}/m-g\sin\theta}{r}}$
  correct: true
  feedback: |-
    Circular motion relates the inward component to angular speed through $a_r=r\omega^2$. Substituting $a_r=T_{\mathrm{tens}}/m-g\sin\theta$ and taking the nonnegative square root gives this angular speed.
- id: p4-angular-speed-b
  content: |-
    $\sqrt{\dfrac{|\vec{a}|}{r}}$
  feedback: |-
    The curvature relation uses only inward radial acceleration. Tangential acceleration changes the speed but does not supply the instantaneous $r\omega^2$ term, so $|\vec{a}|$ cannot replace $a_r$ here.
- id: p4-angular-speed-c
  content: |-
    $\sqrt{\dfrac{T_{\mathrm{tens}}/m+g\sin\theta}{r}}$
  feedback: |-
    This treats gravity's radial projection as inward. At the lower-left position it points outward, so the radial acceleration is $T_{\mathrm{tens}}/m-g\sin\theta$ before using $a_r=r\omega^2$.
- id: p4-angular-speed-d
  content: |-
    $\sqrt{r\left(\dfrac{T_{\mathrm{tens}}}{m}-g\sin\theta\right)}$
  feedback: |-
    This multiplies by the radius instead of dividing by it. From $a_r=r\omega^2$, isolating $\omega^2$ requires $a_r/r$; the units then become $1/\mathrm{s}^2$.
- id: p4-angular-speed-e
  content: |-
    $\dfrac{T_{\mathrm{tens}}/m-g\sin\theta}{r}$
  feedback: |-
    This expression equals $\omega^2$, not $\omega$. Angular speed is the nonnegative square root of $a_r/r$.
```

---

<a id="summary"></a>
## Summary

For a vertical-circle snapshot with inward $+r$ and motion-directed $+t$:

1. Draw only the real forces, then resolve them onto the tilted axes.
2. Use the picture to assign signs before using trigonometry.
3. Apply $\sum F_r=m a_r$ and $\sum F_t=m a_t$ separately.
4. Find total acceleration from $|\vec{a}|=\sqrt{a_r^2+a_t^2}$.
5. Find angular speed from the radial component alone: $a_r=r\omega^2$.

For the key shown,

$$
a_r=\frac{T_{\mathrm{tens}}}{m}-g\sin\theta,
\qquad
a_t=-g\cos\theta,
$$

$$
|\vec{a}|=\sqrt{\left(\frac{T_{\mathrm{tens}}}{m}-g\sin\theta\right)^2+
\left(g\cos\theta\right)^2},
\qquad
\omega=\sqrt{\frac{T_{\mathrm{tens}}/m-g\sin\theta}{r}}.
$$

The main traps are inventing a separate centripetal force, swapping the sine and cosine projections, losing the component signs, or inserting total acceleration into the radial circular-motion relation.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
