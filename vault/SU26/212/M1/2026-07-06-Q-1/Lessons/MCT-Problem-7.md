# Turning Circular Motion into a Radial Force Equation

<!--
lesson-id: 212-M1-081
topic-code: MTH212.M1.81
-->

## Table of Contents

- [Introduction](#introduction)
- [Draw the Real Forces](#draw-the-real-forces)
- [Check How the Radial Requirement Scales](#check-how-the-radial-requirement-scales)
- [Choose Inward Separately at a Dip and a Hill](#choose-inward-separately-at-a-dip-and-a-hill)
- [Compare the Bottom and Top of a Ferris Wheel](#compare-the-bottom-and-top-of-a-ferris-wheel)
- [Summary](#summary)

## Prerequisites

- Draw weight, normal force, tension, and friction as interactions with other objects.
- Apply Newton's second law along one chosen axis.
- Use $a_r=v^2/r=\omega^2r$ for the inward component of acceleration.
- Use $v=r|\omega|$ to convert angular speed to tangential speed.

---

<a id="introduction"></a>
## Introduction

When an object follows a circular arc and a force is requested, choose the radial axis before writing Newton's second law. Take **inward as positive**, project each real force onto that axis, and write

$$
\boxed{\sum F_r=m a_r=m\frac{v^2}{r}=m\omega^2r}.
$$

The right side is the required **net inward component**. It is not another force to add to the free-body diagram. Tension, normal force, friction, gravity, or components of those forces must produce that net result.

For each case:

1. Draw only real interaction forces.
2. Mark the direction toward the circle's center as positive.
3. Give each radial force component a plus or minus sign.
4. Set the signed sum equal to $mv^2/r$ or $m\omega^2r$.
5. Check the result against the force directions and the $mv^2/r$ scaling.

If an assumed normal force comes out negative, the algebra is not asking the surface to pull. It says the assumed contact model has failed. Stop at that flag here; Problem 8 determines whether contact can be maintained.

---

<a id="draw-the-real-forces"></a>
## Draw the Real Forces

**Source-video recognition examples:** Compare the net force with the instantaneous velocity, then identify the interaction that bends the path.

**Explanation**

A net force component parallel to the velocity increases speed; an opposite component decreases speed. A net force that is perpendicular to the instantaneous velocity changes the velocity's direction without changing its magnitude at that instant. In uniform circular motion, the net force remains inward and perpendicular to the velocity, so the speed stays constant while the direction changes continuously.

The source video uses three circular-motion cases:

| Situation | Real inward contributor | What belongs in the radial equation |
| --- | --- | --- |
| A ball is swung on a rope | Tension or its inward component | The tension component, not tension plus a second centripetal-force arrow |
| A car turns on a level road | Static friction | The actual static friction needed for the turn; do not automatically replace it with $\mu_sN$ unless the car is at the slipping threshold |
| Earth follows its nearly circular orbit around the Sun | Gravity | The inward component of the Sun's gravitational force |

“Centripetal” describes the direction of the net force here: center-seeking. It does not name an additional interaction.

```quiz
type: radio
id: mct-p7-real-force-cue
content: |-
  A puck moves at constant speed in a horizontal circle on a frictionless table while a cord connects it to a post at the center. Which free-body and radial-force statement is correct?
options:
- id: mct-p7-real-force-cue-a
  content: |-
    Tension is the only horizontal force, and $T=mv^2/r$.
  correct: true
  feedback: |-
    The cord's tension is the real horizontal interaction and points toward the post. With inward positive, it is the complete radial sum, so $T=mv^2/r$.
- id: mct-p7-real-force-cue-b
  content: |-
    Tension and a separate centripetal force both point inward, so $T+F_c=mv^2/r$.
  feedback: |-
    The quantity $mv^2/r$ is the required net inward force, not an extra interaction. Tension already supplies that radial net force, so adding a second arrow counts the same requirement twice.
- id: mct-p7-real-force-cue-c
  content: |-
    The puck's velocity points inward, so $mv=mv^2/r$.
  feedback: |-
    Velocity is tangent to the circular path, not inward, and momentum is not a force. The cord's inward tension changes the direction of that tangent velocity according to $T=mv^2/r$.
- id: mct-p7-real-force-cue-d
  content: |-
    The normal force from the table points inward, so $N=mv^2/r$.
  feedback: |-
    The table's normal force is vertical and balances weight; it has no horizontal radial component. The horizontal cord tension, not $N$, points toward the post.
- id: mct-p7-real-force-cue-e
  content: |-
    No force is required because the puck's speed is constant.
  feedback: |-
    Constant speed does not mean constant velocity. The velocity direction changes around the circle, so an inward acceleration and an inward net force are required even though the speed does not change.
```

---

<a id="check-how-the-radial-requirement-scales"></a>
## Check How the Radial Requirement Scales

**Source-video worked example:** Starting from $F_{\mathrm{net},r}=mv^2/r$, predict how the required inward net force changes when mass, speed, or radius changes.

**Explanation**

Read each change on its own before combining factors:

$$
m\to am\Rightarrow F_{\mathrm{net},r}\to aF_{\mathrm{net},r},
\qquad
v\to bv\Rightarrow F_{\mathrm{net},r}\to b^2F_{\mathrm{net},r},
\qquad
r\to cr\Rightarrow F_{\mathrm{net},r}\to \frac{1}{c}F_{\mathrm{net},r}.
$$

Compare the new requirement with the original one:

$$
\frac{F'_{\mathrm{net},r}}{F_{\mathrm{net},r}}
=\frac{m'}{m}
\left(\frac{v'}{v}\right)^2
\frac{r}{r'}.
$$

The mass factor enters to the first power, the speed factor is squared, and the radius factor is inverted.

| Change from the source video | Factor calculation | New inward-force requirement |
| --- | --- | --- |
| Double the mass | $2$ | $2F_{\mathrm{net},r}$ |
| Double the speed | $2^2$ | $4F_{\mathrm{net},r}$ |
| Divide the radius by four | $1/(1/4)$ | $4F_{\mathrm{net},r}$ |
| Triple $m$, quadruple $v$, and halve $r$ | $3(4^2)/(1/2)$ | $96F_{\mathrm{net},r}$ |

This ratio checks only the magnitude on the right side of the radial equation. Return to the free-body diagram to decide which real force or signed combination supplies that magnitude.

```quiz
type: radio
id: mct-p7-scaling-check
content: |-
  An object moves in a circle. Its mass stays fixed, its speed is tripled, and its path radius is doubled. By what factor does the required inward net force change?
options:
- id: mct-p7-scaling-check-a
  content: |-
    $\dfrac{9}{2}$
  correct: true
  feedback: |-
    The radial requirement is proportional to $v^2$ and inversely proportional to $r$. Tripling speed contributes $3^2=9$, while doubling radius contributes $1/2$, so the total factor is $9/2$.
- id: mct-p7-scaling-check-b
  content: |-
    $\dfrac{3}{2}$
  feedback: |-
    This treats speed as a first-power factor. Speed is squared in $mv^2/r$, so tripling it contributes $9$, not $3$; the doubled radius then gives $9/2$.
- id: mct-p7-scaling-check-c
  content: |-
    $18$
  feedback: |-
    This makes the force grow with radius. Radius is in the denominator, so doubling $r$ halves the $9$-fold speed contribution instead of doubling it.
- id: mct-p7-scaling-check-d
  content: |-
    $9$
  feedback: |-
    This includes the squared speed factor but ignores the radius change. A path twice as wide requires half as much inward force at a fixed speed, leaving the combined factor $9/2$.
- id: mct-p7-scaling-check-e
  content: |-
    $\dfrac{2}{9}$
  feedback: |-
    This is the reciprocal comparison, original force divided by new force. The question asks for new divided by original, which is $3^2/2=9/2$.
```

---

<a id="choose-inward-separately-at-a-dip-and-a-hill"></a>
## Choose Inward Separately at a Dip and a Hill

**Source-video worked example:** A $5\,\mathrm{kg}$ box moves at $15\,\mathrm{m/s}$ at point A, the bottom of a dip, and point B, the top of a hill. The radius of curvature is $2\,\mathrm m$ at both points. Write the radial force equation at each point and find the formal normal-force values. Use $g=9.8\,\mathrm{m/s^2}$.

**Explanation**

At A, the center of curvature is above the box. Inward is upward, so $N_A$ is positive and weight is negative:

$$
N_A-mg=\frac{mv^2}{r}.
$$

The required inward net force is

$$
\frac{mv^2}{r}
=\frac{(5)(15^2)}{2}
=562.5\,\mathrm N.
$$

Therefore,

$$
N_A=mg+\frac{mv^2}{r}
=(5)(9.8)+562.5
=611.5\,\mathrm N.
$$

At B, the center of curvature is below the box. Choose inward again, now downward. Weight is positive and the upward normal force is negative:

$$
mg-N_B=\frac{mv^2}{r}.
$$

Solving the assumed-contact equation gives

$$
N_B=mg-\frac{mv^2}{r}
=49.0-562.5
=-513.5\,\mathrm N.
$$

A surface cannot exert a negative normal force because it cannot pull the box toward itself. The negative value flags a failed contact assumption; it is not a physical downward normal force. Determining when contact is lost belongs to Problem 8.

```quiz
type: radio
id: mct-p7-dip-hill-signs
content: |-
  A cart moves through the bottom of a dip and then over the top of a hill. At each location the road's normal force is upward and weight is downward. Which pair of radial equations correctly takes inward as positive at each location?
options:
- id: mct-p7-dip-hill-signs-a
  content: |-
    Bottom: $N-mg=mv^2/r$; top: $mg-N=mv^2/r$
  correct: true
  feedback: |-
    The center is above the cart at the bottom, so upward $N$ is inward there. The center is below the cart at the top, so downward $mg$ is inward there; the signs must switch with the inward direction.
- id: mct-p7-dip-hill-signs-b
  content: |-
    Bottom: $N-mg=mv^2/r$; top: $N-mg=mv^2/r$
  feedback: |-
    This keeps upward positive instead of choosing inward separately. Upward is inward at the bottom but outward at the top, where the radial sum must be $mg-N$.
- id: mct-p7-dip-hill-signs-c
  content: |-
    Bottom: $mg-N=mv^2/r$; top: $N-mg=mv^2/r$
  feedback: |-
    Both inward directions are reversed. At the bottom the center is above, giving $N-mg$; at the top the center is below, giving $mg-N$.
- id: mct-p7-dip-hill-signs-d
  content: |-
    Bottom: $N+mg=mv^2/r$; top: $N+mg=mv^2/r$
  feedback: |-
    Normal force and weight point in opposite directions at both locations, so their radial components cannot both have the same sign. Which one is positive depends on which direction points toward the center.
- id: mct-p7-dip-hill-signs-e
  content: |-
    Bottom: $N-mg+F_c=mv^2/r$; top: $mg-N+F_c=mv^2/r$
  feedback: |-
    This adds a separate centripetal-force term. The signed sum of $N$ and $mg$ is already the net radial force, and $mv^2/r$ is its required value rather than another force arrow.
```

---

<a id="compare-the-bottom-and-top-of-a-ferris-wheel"></a>
## Compare the Bottom and Top of a Ferris Wheel

**Lecture worked example:** A $68\,\mathrm{kg}$ rider sits in an upright gondola on a Ferris wheel of radius $42\,\mathrm m$. The wheel's angular speed is $0.16\,\mathrm{rad/s}$. Find the rider's tangential speed and the seat's normal force at the bottom and top. Use $g=9.8\,\mathrm{m/s^2}$.

**Explanation**

First convert angular speed to tangential speed:

$$
v=r|\omega|
=(42)(0.16)
=6.72\,\mathrm{m/s}.
$$

The same radial requirement can be calculated without rounding $v$:

$$
\frac{mv^2}{r}
=m\omega^2r
=(68)(0.16)^2(42)
=73.1136\,\mathrm N.
$$

At the bottom, inward is upward. The seat's normal force is inward and weight is outward:

$$
\begin{aligned}
N_{\mathrm{bottom}}-mg&=m\omega^2r,\\
N_{\mathrm{bottom}}
&=m(g+\omega^2r)\\
&=(68)\left(9.8+(0.16)^2(42)\right)\\
&=739.5\,\mathrm N\approx740\,\mathrm N.
\end{aligned}
$$

At the top, inward is downward. Weight is inward, while the upright seat's normal force remains upward and is therefore outward:

$$
\begin{aligned}
mg-N_{\mathrm{top}}&=m\omega^2r,\\
N_{\mathrm{top}}
&=m(g-\omega^2r)\\
&=(68)\left(9.8-(0.16)^2(42)\right)\\
&=593.3\,\mathrm N\approx590\,\mathrm N.
\end{aligned}
$$

Both normal forces are positive, and the comparison follows directly from their signs in the radial sums:

$$
N_{\mathrm{bottom}}>mg>N_{\mathrm{top}}.
$$

```quiz
type: radio
id: mct-p7-ferris-variation
content: |-
  A $60\,\mathrm{kg}$ rider sits in an upright Ferris-wheel gondola. The wheel has radius $25\,\mathrm m$ and angular speed $0.20\,\mathrm{rad/s}$. Using $g=9.8\,\mathrm{m/s^2}$, which pair gives the seat's normal forces at the bottom and top?
options:
- id: mct-p7-ferris-variation-a
  content: |-
    $N_{\mathrm{bottom}}=648\,\mathrm N$ and $N_{\mathrm{top}}=528\,\mathrm N$
  correct: true
  feedback: |-
    The inward requirement is $m\omega^2r=60(0.20)^2(25)=60\,\mathrm N$, while $mg=588\,\mathrm N$. Add the radial requirement at the bottom and subtract it at the top, giving $648\,\mathrm N$ and $528\,\mathrm N$.
- id: mct-p7-ferris-variation-b
  content: |-
    $N_{\mathrm{bottom}}=588\,\mathrm N$ and $N_{\mathrm{top}}=588\,\mathrm N$
  feedback: |-
    These values set $N=mg$ and omit the inward acceleration. The rider's direction is changing, so the seat force must be $60\,\mathrm N$ above $mg$ at the bottom and $60\,\mathrm N$ below $mg$ at the top.
- id: mct-p7-ferris-variation-c
  content: |-
    $N_{\mathrm{bottom}}=528\,\mathrm N$ and $N_{\mathrm{top}}=648\,\mathrm N$
  feedback: |-
    This swaps the inward directions. At the bottom, the upward normal force must exceed weight to produce an upward net force; at the top, inward is downward, so the upward normal force is smaller than weight.
- id: mct-p7-ferris-variation-d
  content: |-
    $N_{\mathrm{bottom}}=60\,\mathrm N$ and $N_{\mathrm{top}}=60\,\mathrm N$
  feedback: |-
    The value $60\,\mathrm N$ is the required radial net force $m\omega^2r$, not the seat force. The normal force must combine with the rider's $588\,\mathrm N$ weight to leave that net result.
- id: mct-p7-ferris-variation-e
  content: |-
    $N_{\mathrm{bottom}}=708\,\mathrm N$ and $N_{\mathrm{top}}=468\,\mathrm N$
  feedback: |-
    These values use twice the stated radius, making $m\omega^2r=120\,\mathrm N$. The given radius is already $25\,\mathrm m$, so the radial requirement is $60\,\mathrm N$ and the normal-force pair is $588\pm60\,\mathrm N$.
```

---

<a id="summary"></a>
## Summary

For a force question on a circular arc:

1. Draw only the real interactions.
2. Point the radial positive axis inward at the object's current location.
3. Project the real forces onto that axis and write $\sum F_r=mv^2/r=m\omega^2r$.
4. Solve the signed equation, then check that the result matches the force directions.
5. Check scale: the inward requirement is direct in $m$, direct in $v^2$, and inverse in $r$.

Do not add a separate centripetal-force arrow. A negative normal force means the assumed contact cannot occur; it does not mean the surface pulls.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
