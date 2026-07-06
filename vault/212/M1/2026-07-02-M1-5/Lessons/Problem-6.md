# Release Height from a Vertical Circle

## Table of Contents

- [Introduction](#introduction)
- [Turn Radial Forces Into Speed](#turn-radial-forces-into-speed)
- [Find the Upward Release Component](#find-the-upward-release-component)
- [Combine Speed With Projectile Height](#combine-speed-with-projectile-height)
- [Finish the Assignment Calculation](#finish-the-assignment-calculation)
- [Summary](#summary)

## Prerequisites

- Use Newton's second law along a chosen axis.
- Use centripetal acceleration in the form $a_r=\dfrac{v^2}{L}$.
- Resolve a force or velocity into a trigonometric component.
- Use the vertical projectile relation $0=v_y^2-2g\Delta y$ at maximum height.

---

<a id="introduction"></a>
## Introduction

When a ball is released from a vertical circle, the height it gains after release depends on the vertical component of its velocity at the release point. The cue in this problem is that the speed is not given directly; it must be found from the inward radial force equation first.

For the assignment diagram, the ball is above the center and to the left, and the inward $r$-axis points down and right along the string.

![](<../Source/Images/vertical-circle-ball-string-diagram.png>)

Use the order

$$
\text{radial forces}\rightarrow v^2\rightarrow v_y\rightarrow \Delta y.
$$

Because the ball is moving clockwise, the tangent velocity points up and right at release. That makes the upward velocity component

$$
v_y=v\sin\theta.
$$

---

<a id="turn-radial-forces-into-speed"></a>
## Turn Radial Forces Into Speed

**Example:** A $0.50\ \mathrm{kg}$ ball is in the same upper-left position as the assignment diagram, with the string making $\theta=20^\circ$ from vertical. The string tension is $T=1.5\ \mathrm{N}$ and the string length is $L=0.80\ \mathrm{m}$. Find $a_r$ and $v^2$ at that instant.

**Explanation**

The inward direction is along the string toward the center. Tension points inward, and the component of weight along the inward direction is $mg\cos\theta$, so

$$
\sum F_r=m a_r
$$

becomes

$$
T+mg\cos\theta=m a_r.
$$

Divide by $m$:

$$
a_r=\frac{T}{m}+g\cos\theta.
$$

Substitute the values:

$$
a_r=\frac{1.5}{0.50}+9.8\cos(20^\circ)=12.21\ \mathrm{m/s^2}.
$$

Now use $a_r=\dfrac{v^2}{L}$:

$$
v^2=a_rL=(12.21)(0.80)=9.77\ \mathrm{m^2/s^2}.
$$

Equivalently, this diagram gives the direct speed-squared formula

$$
v^2=L\left(\frac{T}{m}+g\cos\theta\right).
$$

```quiz
type: radio
id: p6-radial-force
content: |-
  A ball is in the same upper-left position as the assignment diagram, so tension and the radial component of weight both point inward. If $T=2.0\ \mathrm{N}$, $m=0.40\ \mathrm{kg}$, and $\theta=30^\circ$, which value is the radial acceleration?
options:
- id: p6-radial-a
  content: |-
    $13.49\ \mathrm{m/s^2}$
  correct: true
- id: p6-radial-b
  content: |-
    $3.49\ \mathrm{m/s^2}$
- id: p6-radial-c
  content: |-
    $10.00\ \mathrm{m/s^2}$
- id: p6-radial-d
  content: |-
    $18.49\ \mathrm{m/s^2}$
- id: p6-radial-e
  content: |-
    $11.78\ \mathrm{m/s^2}$
```

---

<a id="find-the-upward-release-component"></a>
## Find the Upward Release Component

**Example:** A ball is released from the same clockwise position with speed $v=3.0\ \mathrm{m/s}$ and angle $\theta=20^\circ$. Find the upward component of its velocity.

**Explanation**

At the release point, the velocity is tangent to the circle. The radius is $\theta$ away from vertical, so the tangent is $\theta$ away from horizontal. In the velocity-component triangle, the upward component is the side opposite $\theta$, so

$$
v_y=v\sin\theta.
$$

Thus,

$$
v_y=3.0\sin(20^\circ)=1.03\ \mathrm{m/s}.
$$

Do not use $v\cos\theta$ here. In this diagram, cosine gives the horizontal component of the tangent velocity.

```quiz
type: radio
id: p6-vertical-component
content: |-
  A ball is released from the same clockwise position with speed $4.0\ \mathrm{m/s}$ and $\theta=30^\circ$. What is its upward velocity component?
options:
- id: p6-vertical-a
  content: |-
    $2.0\ \mathrm{m/s}$
  correct: true
- id: p6-vertical-b
  content: |-
    $3.46\ \mathrm{m/s}$
- id: p6-vertical-c
  content: |-
    $4.0\ \mathrm{m/s}$
- id: p6-vertical-d
  content: |-
    $0.50\ \mathrm{m/s}$
- id: p6-vertical-e
  content: |-
    $8.0\ \mathrm{m/s}$
```

---

<a id="combine-speed-with-projectile-height"></a>
## Combine Speed With Projectile Height

**Example:** Use $m=0.50\ \mathrm{kg}$, $L=0.80\ \mathrm{m}$, $T=1.5\ \mathrm{N}$, and $\theta=20^\circ$ to find the height above the release point.

**Explanation**

From the radial-force step,

$$
a_r=\frac{T}{m}+g\cos\theta=12.21\ \mathrm{m/s^2}
$$

and

$$
v^2=a_rL=(12.21)(0.80)=9.77\ \mathrm{m^2/s^2}.
$$

After release, the vertical velocity component is $v_y=v\sin\theta$, so

$$
v_y^2=v^2\sin^2\theta.
$$

At maximum height, the vertical velocity is $0$, so

$$
0=v_y^2-2g\Delta y.
$$

Solve for $\Delta y$:

$$
\Delta y=\frac{v_y^2}{2g}=\frac{v^2\sin^2\theta}{2g}.
$$

Since $v^2=L\left(\dfrac{T}{m}+g\cos\theta\right)$, the whole calculation can be written as

$$
\Delta y=\frac{L\left(\dfrac{T}{m}+g\cos\theta\right)\sin^2\theta}{2g}.
$$

Substitute:

$$
\Delta y=\frac{(9.77)\sin^2(20^\circ)}{2(9.8)}=0.0583\ \mathrm{m}.
$$

```quiz
type: radio
id: p6-combined-height
content: |-
  A $0.40\ \mathrm{kg}$ ball is released from the same clockwise position with $L=0.60\ \mathrm{m}$, $T=2.0\ \mathrm{N}$, and $\theta=30^\circ$. Using $g=9.8\ \mathrm{m/s^2}$, how far above the release point will it rise?
options:
- id: p6-combined-a
  content: |-
    $0.103\ \mathrm{m}$
  correct: true
- id: p6-combined-b
  content: |-
    $0.413\ \mathrm{m}$
- id: p6-combined-c
  content: |-
    $0.310\ \mathrm{m}$
- id: p6-combined-d
  content: |-
    $0.052\ \mathrm{m}$
- id: p6-combined-e
  content: |-
    $0.688\ \mathrm{m}$
```

---

<a id="finish-the-assignment-calculation"></a>
## Finish the Assignment Calculation

**Example:** Use the assignment values $L=0.88\ \mathrm{m}$, $T=1.2\ \mathrm{N}$, $m=0.56\ \mathrm{kg}$, and $\theta=14^\circ$.

**Explanation**

Start with the radial equation:

$$
T+mg\cos\theta=m a_r.
$$

Then

$$
a_r=\frac{T}{m}+g\cos\theta
=\frac{1.2}{0.56}+9.8\cos(14^\circ)
=11.65\ \mathrm{m/s^2}.
$$

Use $v^2=a_rL$:

$$
v^2=(11.65)(0.88)=10.25\ \mathrm{m^2/s^2}.
$$

The release velocity points upward by the amount $v\sin\theta$, so

$$
\Delta y=\frac{v^2\sin^2\theta}{2g}
=\frac{(10.25)\sin^2(14^\circ)}{2(9.8)}
=0.0306\ \mathrm{m}.
$$

To two significant figures,

$$
\Delta y=0.031\ \mathrm{m}.
$$

```quiz
type: radio
id: p6-assignment-check
content: |-
  A ball is released from the same clockwise position with $L=0.75\ \mathrm{m}$, $T=1.0\ \mathrm{N}$, $m=0.50\ \mathrm{kg}$, and $\theta=18^\circ$. Using the same method, what is the height above the release point?
options:
- id: p6-assignment-a
  content: |-
    $0.041\ \mathrm{m}$
  correct: true
- id: p6-assignment-b
  content: |-
    $0.134\ \mathrm{m}$
- id: p6-assignment-c
  content: |-
    $0.325\ \mathrm{m}$
- id: p6-assignment-d
  content: |-
    $0.087\ \mathrm{m}$
- id: p6-assignment-e
  content: |-
    $0.020\ \mathrm{m}$
```

---

## Summary

For this diagram, use the inward radial force equation first:

$$
T+mg\cos\theta=m\frac{v^2}{L}.
$$

Then turn that speed into the upward release component:

$$
v_y=v\sin\theta.
$$

Finally, use the projectile height relation:

$$
\Delta y=\frac{v_y^2}{2g}
=\frac{v^2\sin^2\theta}{2g}.
$$

For this exact force diagram, that becomes

$$
\Delta y=\frac{L\left(\dfrac{T}{m}+g\cos\theta\right)\sin^2\theta}{2g}.
$$

The main trap is mixing up the two uses of the angle: $\cos\theta$ appears in the radial force equation for weight's inward component, while $\sin\theta$ appears in the projectile step for the upward component of the tangent velocity.
