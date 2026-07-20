# Choosing the Rotation Axis After an Off-Center Collision

## Table of Contents

- [Introduction](#introduction)
- [Use the Center of Mass of the Whole Object](#use-the-center-of-mass-of-the-whole-object)
- [Check Whether the Impact Produces Rotation](#check-whether-the-impact-produces-rotation)
- [Locate the Combined Center of Mass](#locate-the-combined-center-of-mass)
- [Apply the Test to the Rod and Ball](#apply-the-test-to-the-rod-and-ball)
- [Keep Translation and Rotation Separate](#keep-translation-and-rotation-separate)
- [Summary](#summary)

## Prerequisites

- Interpret center of mass as a mass-weighted average position.
- Recognize that an isolated collision conserves linear momentum and angular momentum.
- Use $L=rp$ when the position vector and momentum are perpendicular.

---

<a id="introduction"></a>
## Introduction

When objects collide and stick in free space, first treat them as **one combined object**. With no external support or pivot, its center of mass moves while the object may rotate.

The recognition cue is an **isolated, off-center collision**. Use the center of mass of the combined object as the reference point, check whether the incoming momentum has a nonzero lever arm about that point, and then identify the rotation axis through that point.

**Decision rule**

1. Which center? Use the center of mass of everything that is stuck together after the collision.
2. Does it spin? If the incoming momentum line misses that point, the angular momentum about it is nonzero.

---

<a id="use-the-center-of-mass-of-the-whole-object"></a>
## Use the Center of Mass of the Whole Object

**Example:** A lump of clay sticks to the end of a freely floating bar. About what point should the motion of the new rigid object be described?

**Explanation**

After sticking, the clay and bar form one object. The natural decomposition of its motion is:

- translation of the **combined center of mass**, plus
- rotation about an axis through the **combined center of mass**.

The bar's old center of mass is no longer the center of mass of the object because the attached clay changes the mass distribution.

```quiz
type: radio
id: p7-combined-object-q1
content: |-
  A small mass sticks to one end of a freely floating uniform plank. Which point is the correct reference point for describing the rotation of the resulting object?
options:
- id: a
  content: |-
    The plank's original center of mass
- id: b
  content: |-
    The point where the small mass made contact
- id: c
  content: |-
    The center of mass of the plank–mass system
  correct: true
- id: d
  content: |-
    The small mass's original center
- id: e
  content: |-
    Any point on the plank gives the same physical axis
```

---

<a id="check-whether-the-impact-produces-rotation"></a>
## Check Whether the Impact Produces Rotation

**Example:** A particle with momentum $p$ approaches a free rigid object. Its straight-line path misses the combined center of mass by perpendicular distance $b$. Will the stuck-together object have angular momentum about its center of mass?

**Explanation**

The incoming angular momentum about the combined center of mass has magnitude

$$
L_{\mathrm{CM}}=bp.
$$

If $b\ne 0$, then $L_{\mathrm{CM}}\ne 0$. With no external torque, that angular momentum remains after the collision, so the combined object rotates. If the momentum line passes exactly through the combined center of mass, then $b=0$, and this test predicts no rotation about the center of mass.

```quiz
type: radio
id: p7-lever-arm-q1
content: |-
  A particle sticks to a free rigid object. The particle's momentum line passes a perpendicular distance $d$ from the center of mass of the final combined object. Which condition guarantees nonzero angular momentum about that center of mass?
options:
- id: a
  content: |-
    $d=0$
- id: b
  content: |-
    $d\ne 0$
  correct: true
- id: c
  content: |-
    The particle and object have equal masses
- id: d
  content: |-
    The collision is perfectly elastic
- id: e
  content: |-
    The final center of mass is stationary
```

---

<a id="locate-the-combined-center-of-mass"></a>
## Locate the Combined Center of Mass

**Example:** A uniform rod of mass $m$ and length $L$ lies along the $y$-axis with its lower end at $(0,0)$. A ball of mass $m/2$ and radius $r$ touches that end, with its center at $(-r,0)$. Where is the combined center of mass?

**Explanation**

The rod's center is at $(0,L/2)$, while the ball's center is at $(-r,0)$. Take the mass-weighted average of each coordinate:

$$
\begin{aligned}
x_{\mathrm{CM}}
&=\frac{m(0)+(m/2)(-r)}{m+m/2}
=-\frac{r}{3},\\[4pt]
y_{\mathrm{CM}}
&=\frac{m(L/2)+(m/2)(0)}{m+m/2}\\
&=\frac{L}{3}.
\end{aligned}
$$

Thus the combined center of mass is at $(-r/3,L/3)$. It is not at the rod's original center, $(0,L/2)$, and it is not at the contact point. The radius shifts the center horizontally, but the vertical distance $L/3$ is the lever arm for the ball's horizontal momentum.

```quiz
type: radio
id: p7-center-location-q1
content: |-
  A uniform rod of mass $M$ and length $D$ has a point mass $M$ attached at one end. Measured from that end, where is the center of mass of the combined system?
options:
- id: a
  content: |-
    $0$
- id: b
  content: |-
    $D/4$
  correct: true
- id: c
  content: |-
    $D/3$
- id: d
  content: |-
    $D/2$
- id: e
  content: |-
    $3D/4$
```

---

<a id="apply-the-test-to-the-rod-and-ball"></a>
## Apply the Test to the Rod and Ball

**Example:** A nonspinning ball of mass $m/2$ moves horizontally with speed $v$, strikes the lower end of a vertical rod of mass $m$, and sticks. Which point determines the axis of the system's rotational motion?

**Explanation**

Use the two-part test:

1. The rod and ball are isolated and stick, so after impact they are one free object. Describe its motion using the center of mass of the **combined system**, located at $(-r/3,L/3)$ in the coordinates above.
2. The ball's horizontal momentum line is at $y=0$, while the combined center of mass is $L/3$ above that line. Thus the perpendicular lever arm is $L/3$, so

$$
L_{\mathrm{CM}}=\left(\frac{L}{3}\right)\left(\frac{m}{2}v\right)=\frac{mvL}{6}\ne 0.
$$

The object rotates, and its rotational motion is about an axis through the combined center of mass, perpendicular to the page. Its center of mass also translates.

```quiz
type: radio
id: p7-original-application-q1
content: |-
  A thin uniform rod of mass $m$ and length $L$ is initially at rest in outer space. A nonspinning ball of mass $m/2$ and radius $r$ strikes one end of the rod with speed $v$ and sticks to it.

  Which statement is true?

  ![](<../Source/2026-07-15-HW-4/Images/rod-ball-inelastic-collision.png>)
options:
- id: a
  content: |-
    After the collision, the ball–rod system will not rotate
- id: b
  content: |-
    After the collision, the ball–rod system will rotate about an axis through the rod's center of mass
- id: c
  content: |-
    After the collision, the ball–rod system will rotate about an axis through the center of mass of the combined system
  correct: true
```

---

<a id="keep-translation-and-rotation-separate"></a>
## Keep Translation and Rotation Separate

**Example:** The combined center of mass moves after the collision. Does that mean the system cannot rotate about an axis through its center of mass?

**Explanation**

No. A free object's motion can contain both parts at once. The center of mass follows the motion set by total linear momentum, while the body changes orientation around an axis through that moving center of mass.

The phrase “rotates about its center of mass” does **not** mean the center of mass stays fixed in space.

```quiz
type: radio
id: p7-translation-rotation-q1
content: |-
  After an off-center collision in outer space, a stuck-together object has nonzero total linear momentum and nonzero angular momentum about its center of mass. Which motion is possible?
options:
- id: a
  content: |-
    Translation only, because any center-of-mass motion prevents rotation
- id: b
  content: |-
    Rotation only, because rotation prevents center-of-mass motion
- id: c
  content: |-
    Translation of the center of mass together with rotation about an axis through it
  correct: true
- id: d
  content: |-
    Rotation about the collision point, which remains fixed in space
- id: e
  content: |-
    No motion, because the objects stick
```

---

<a id="summary"></a>
## Summary

For an isolated collision in which objects stick:

1. Treat the stuck objects as one combined object.
2. Locate the center of mass of the combined system, not either object's old center.
3. Check the incoming momentum's perpendicular lever arm about that point: $L_{\mathrm{CM}}=r_\perp p$.
4. If $r_\perp\ne 0$, the combined object rotates about an axis through its center of mass while that center of mass translates.

The main traps are choosing the rod's original center or the contact point as though either were an external pivot, and assuming that sticking by itself guarantees rotation. The nonzero lever arm is what establishes the rotation.
