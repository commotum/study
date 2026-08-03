# Finding Angular Speed After a Bullet Embeds in a Rotor

<!--
lesson-id: 212-M2-035
topic-code: MTH212.M2.35
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose Angular Momentum About the Spindle](#choose-angular-momentum-about-the-spindle)
- [Find the Bullet's Initial Angular Momentum](#find-the-bullets-initial-angular-momentum)
- [Build the Final Moment of Inertia](#build-the-final-moment-of-inertia)
- [Solve for Angular Speed](#solve-for-angular-speed)
- [Apply the Method](#apply-the-method)
- [Summary](#summary)

## Prerequisites

- Use $L=I\omega$ for a rigid body rotating about a fixed axis.
- Use $L=mvb$ for a particle whose line of motion has perpendicular distance $b$ from an axis.
- Recall $I=\frac12Mr^2$ for a solid uniform cylinder about its central axis.
- Round a final result to the significant figures supported by measured data.

---

<a id="introduction"></a>
## Introduction

When a moving object embeds in a rotor, the collision is inelastic, so mechanical energy is not conserved. During the short impact, however, the spindle force has zero lever arm about the spindle. Angular momentum about that axis is therefore conserved:

$$
L_i=L_f.
$$

For a bullet that strikes the rim tangentially and remains there, the reusable equation is

$$
mvr=\left(\frac12Mr^2+mr^2\right)\omega_f.
$$

The core task is to identify the bullet's initial angular momentum, include both objects in the final moment of inertia, and solve for $\omega_f$.

| Stage | Bullet | Cylinder |
|---|---|---|
| Before impact | contributes $mvr$ | at rest, so contributes $0$ |
| After impact | contributes $mr^2$ to $I_f$ | contributes $\frac12Mr^2$ to $I_f$ |

---

<a id="choose-angular-momentum-about-the-spindle"></a>
## Choose Angular Momentum About the Spindle

**Example:** A bullet embeds in a cylinder mounted on a fixed spindle. Which conservation law connects the motion immediately before and immediately after impact?

**Explanation**

Choose the spindle as the angular-momentum axis. The spindle can exert a large impulse, so linear momentum of the bullet-cylinder system need not be conserved. But that impulse acts at the axis and contributes no torque about it during the collision.

Thus angular momentum about the spindle is conserved. Because the bullet sticks, kinetic energy is not conserved.

```quiz
type: radio
id: m2-5-p5-conservation-law
content: |-
  A projectile embeds in a disk that can rotate about a fixed, frictionless spindle. Which quantity is conserved during the short collision?
options:
- id: a
  content: |-
    Angular momentum about the spindle
  correct: true
  feedback: |-
    The spindle impulse has zero lever arm about the spindle, so angular momentum about that axis is conserved. Embedding is inelastic, so mechanical energy is not conserved.
- id: b
  content: |-
    Linear momentum of the projectile-disk system
- id: c
  content: |-
    Mechanical energy
- id: d
  content: |-
    The projectile's speed
- id: e
  content: |-
    The disk's moment of inertia
```

---

<a id="find-the-bullets-initial-angular-momentum"></a>
## Find the Bullet's Initial Angular Momentum

**Example:** A bullet of mass $m$ and speed $v$ travels along a line tangent to a circle of radius $r$. Find its angular momentum magnitude about the circle's center.

**Explanation**

For a moving particle,

$$
L=mvb,
$$

where $b$ is the perpendicular distance from the axis to the line of motion. A tangent line at the rim has $b=r$, so

$$
\boxed{L_i=mvr}.
$$

Equivalently, $L=mvr\sin\theta$ and the tangential geometry gives $\theta=90^\circ$, so $\sin\theta=1$.

```quiz
type: radio
id: m2-5-p5-initial-angular-momentum
content: |-
  A particle of mass $m$ moves at speed $v$ along a line whose perpendicular distance from a spindle is $r/2$. What is its angular momentum magnitude about the spindle?
options:
- id: a
  content: |-
    $\dfrac12mvr$
  correct: true
  feedback: |-
    Use the perpendicular lever arm $b=r/2$: $L=mvb=mv(r/2)=mvr/2$.
- id: b
  content: |-
    $mvr$
- id: c
  content: |-
    $2mvr$
- id: d
  content: |-
    $\dfrac12mv^2$
- id: e
  content: |-
    $mr^2$
```

---

<a id="build-the-final-moment-of-inertia"></a>
## Build the Final Moment of Inertia

**Example:** A bullet of mass $m$ embeds at the rim of a solid uniform cylinder of mass $M$ and radius $r$. Find the moment of inertia of the combined final system.

**Explanation**

After impact, the cylinder and bullet rotate together. Add both contributions about the same spindle:

$$
I_f=I_{\text{cylinder}}+I_{\text{bullet}}.
$$

The solid cylinder contributes $\frac12Mr^2$. The embedded bullet is modeled as a point mass at distance $r$, so it contributes $mr^2$. Therefore,

$$
\boxed{I_f=\frac12Mr^2+mr^2}.
$$

Omitting the bullet from $I_f$ overestimates the final angular speed.

```quiz
type: radio
id: m2-5-p5-final-inertia
content: |-
  A small mass $m$ sticks to the rim of a solid uniform cylinder of mass $M$ and radius $r$. What is the combined moment of inertia about the central spindle?
options:
- id: a
  content: |-
    $\dfrac12Mr^2+mr^2$
  correct: true
  feedback: |-
    Add the solid cylinder's $\frac12Mr^2$ and the point mass's $mr^2$. The bullet remains part of the rotating final system.
- id: b
  content: |-
    $\dfrac12Mr^2$
- id: c
  content: |-
    $Mr^2+mr^2$
- id: d
  content: |-
    $\dfrac12(M+m)r^2$
- id: e
  content: |-
    $Mmr^2$
```

---

<a id="solve-for-angular-speed"></a>
## Solve for Angular Speed

**Example:** Derive the final angular speed for a tangential bullet that embeds at the cylinder's rim.

**Explanation**

Set the initial and final angular momenta equal:

$$
mvr=\left(\frac12Mr^2+mr^2\right)\omega_f.
$$

Factor $r^2$ from the final inertia and solve:

$$
\begin{aligned}
\omega_f
&=\frac{mvr}{r^2(\frac12M+m)}\\
&=\boxed{\frac{mv}{r(\frac12M+m)}}.
\end{aligned}
$$

Only one factor of $r$ cancels. The remaining $1/r$ is necessary for the result to have units of inverse seconds, equivalent to radians per second.

The dimensions verify the simplified expression:

$$
\frac{mv}{r(\frac12M+m)}
\longrightarrow
\frac{\mathrm{kg}\,\mathrm{m/s}}{\mathrm{m}\,\mathrm{kg}}
=\mathrm{s^{-1}}.
$$

There is also a useful upper bound. The bullet's tangential angular rate at the rim is $v/r$. Since the cylinder adds positive inertia,

$$
\omega_f
=\frac{m}{\frac12M+m}\frac{v}{r}
<\frac{v}{r}.
$$

```quiz
type: radio
id: m2-5-p5-calculate-angular-speed
content: |-
  A bullet with $m=0.20\ \mathrm{kg}$ and $v=3.0\ \mathrm{m/s}$ embeds tangentially at the rim of a solid cylinder with $M=1.6\ \mathrm{kg}$ and $r=0.50\ \mathrm{m}$. What is the final angular speed?
options:
- id: a
  content: |-
    $1.2\ \mathrm{rad/s}$
  correct: true
  feedback: |-
    $\omega_f=mv/[r(\frac12M+m)]=(0.20)(3.0)/[(0.50)(0.80+0.20)]=1.2\ \mathrm{rad/s}$.
- id: b
  content: |-
    $0.60\ \mathrm{rad/s}$
- id: c
  content: |-
    $2.4\ \mathrm{rad/s}$
- id: d
  content: |-
    $3.0\ \mathrm{rad/s}$
- id: e
  content: |-
    $6.0\ \mathrm{rad/s}$
```

---

<a id="apply-the-method"></a>
## Apply the Method

**Example:** Use the given bullet and cylinder data to calculate the final angular speed.

**Explanation**

The diagram shows a tangential path at the rim, so $L_i=mvr$. The final rotating system includes the cylinder and embedded bullet:

$$
I_f=\frac12Mr^2+mr^2.
$$

Thus,

$$
\omega_f=\frac{mv}{r(\frac12M+m)}.
$$

Evaluate the grouped pieces before dividing:

| Piece | Substitution | Value |
|---|---|---:|
| numerator $mv$ | $(0.35)(3.8)$ | $1.33$ |
| mass factor $\frac12M+m$ | $\frac12(2.6)+0.35$ | $1.65$ |
| denominator $r(\frac12M+m)$ | $(0.85)(1.65)$ | $1.4025$ |

Therefore,

$$
\omega_f=\frac{1.33}{1.4025}=0.9483\ldots\ \mathrm{rad/s}.
$$

The measured givens have two significant figures, so the final value is $0.95\ \mathrm{rad/s}$.

As a reasonableness check, $v/r=3.8/0.85\approx4.47\ \mathrm{rad/s}$, and the combined cylinder-bullet angular speed $0.95\ \mathrm{rad/s}$ is smaller.

```quiz
type: radio
id: m2-5lec-q4
content: |-
  **Question 4**

  A bullet of mass $m$ moving at speed $v$ embeds in the rim of a solid uniform cylinder of mass $M$ and radius $r$, initially at rest on a spindle. Find the final angular speed for $m=0.35\ \mathrm{kg}$, $M=2.6\ \mathrm{kg}$, $r=0.85\ \mathrm{m}$, and $v=3.8\ \mathrm{m/s}$.

  ![](<../Source/Images/bullet-embedding-solid-cylinder.png>)

  Enter the angular speed in radians per second as a number only:
options:
- id: a
  content: |-
    `0.95`
  correct: true
  feedback: |-
    Angular momentum about the spindle is conserved. The bullet's initial angular momentum is $mvr$, and the final moment of inertia is

    $$
    I_f=\frac12Mr^2+mr^2.
    $$

    Hence,

    $$
    \omega_f
    =\frac{mvr}{\frac12Mr^2+mr^2}
    =\frac{mv}{r(\frac12M+m)}.
    $$

    Substitution gives

    $$
    \omega_f
    =\frac{(0.35)(3.8)}{(0.85)[\frac12(2.6)+0.35]}
    =0.9483\ldots\ \mathrm{rad/s}.
    $$

    The measured givens have two significant figures, so $\omega_f=0.95\ \mathrm{rad/s}$.
- id: b
  content: |-
    `1.2`
- id: c
  content: |-
    `0.53`
- id: d
  content: |-
    `0.35`
- id: e
  content: |-
    `2.7`
```

---

<a id="summary"></a>
## Summary

- **Cue:** a moving object embeds in a rotor mounted on a fixed spindle.
- **Conserve:** angular momentum about the spindle, not linear momentum or mechanical energy.
- **Initial angular momentum:** $L_i=mvb$; for a tangential rim impact, $b=r$.
- **Final inertia:** add every rotating part, $I_f=\frac12Mr^2+mr^2$.
- **Solve:** $\omega_f=mv/[r(\frac12M+m)]$.
- **Check:** the result must have units of $\mathrm{s^{-1}}$ and use the precision of the measured inputs.
- **Bound:** because the cylinder adds inertia, $\omega_f<v/r$.
- **Main trap:** the embedded bullet contributes to both the initial angular momentum and the final moment of inertia.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../../M3/2026-07-20-Q-2/Study-Guide.md)
Next: [Comparing Angular Momentum at Equal Angular Speed](../../../M3/2026-07-19-PQ-2/Lessons/Problem-1.md)

Study guide index: 11/20

---

<!-- lesson-nav:end -->
