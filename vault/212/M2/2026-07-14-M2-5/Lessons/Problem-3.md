# Angular Speed After Rotating Cups Collect Rain

<!--
lesson-id: 212-M2-033
topic-code: MTH212.M2.33
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose Angular Momentum Conservation](#choose-angular-momentum-conservation)
- [Compare the Moments of Inertia](#compare-the-moments-of-inertia)
- [Use the Inverse Change in Angular Speed](#use-the-inverse-change-in-angular-speed)
- [Apply the Method to Problem 3](#apply-the-method-to-problem-3)

## Prerequisites

- Angular momentum of a rigidly rotating system: $L=I\omega$
- Point-mass moment of inertia: $I=mr^2$
- Conservation of angular momentum when external torque is negligible
- Multiplicative-factor reasoning

---

<a id="introduction"></a>
## Introduction

When rain lands in rotating cups, the captured water becomes part of the rotating system. If external torque about the rotation axis is negligible, angular momentum stays constant even though the moment of inertia changes:

$$
I_i\omega_i=I_f\omega_f.
$$

The recognition cue is mass being added at a fixed distance from the axis. Compare the final moment of inertia with the initial one, then change angular speed by the reciprocal factor:

$$
\omega_f=\frac{I_i}{I_f}\omega_i.
$$

---

<a id="choose-angular-momentum-conservation"></a>
## Choose Angular Momentum Conservation

**Example:** Two cups rotate about the midpoint of their connecting rod while rain falls into them. What system quantity links the motion just before and just after the rain is captured?

**Explanation**

Take the cups, captured water, and rod as the rotating system. With negligible external torque about the axis, the system's angular momentum is conserved:

$$
L_i=L_f,
$$

or

$$
I_i\omega_i=I_f\omega_f.
$$

The angular speed need not remain constant. It changes so that the product $I\omega$ stays constant.

```quiz
type: radio
id: p3-conserved-quantity
content: |-
  Rain is captured by cups rotating about a fixed axis. External torque about the axis is negligible. Which equation should connect the states immediately before and after capture?
options:
- id: p3-conserve-a
  content: |-
    $I_i\omega_i=I_f\omega_f$
  correct: true
  feedback: |-
    Negligible external torque means angular momentum is conserved: $L=I\omega$, so $I_i\omega_i=I_f\omega_f$.
- id: p3-conserve-b
  content: |-
    $I_i=I_f$
- id: p3-conserve-c
  content: |-
    $\omega_i=\omega_f$
- id: p3-conserve-d
  content: |-
    $I_i\omega_i^2=I_f\omega_f^2$
- id: p3-conserve-e
  content: |-
    $m_i\omega_i=m_f\omega_f$
```

---

<a id="compare-the-moments-of-inertia"></a>
## Compare the Moments of Inertia

**Example:** Two identical cups of mass $m$ are connected by a negligible-mass rod of length $d$ and rotate about the rod's midpoint. Each cup then captures water of mass $m$. Compare $I_f$ with $I_i$.

**Explanation**

Each cup is at radius

$$
r=\frac d2.
$$

Initially, the two cups give

$$
I_i=2m\left(\frac d2\right)^2.
$$

After capture, each cup-plus-water combination has mass $m+m=2m$ at the same radius:

$$
\begin{aligned}
I_f
&=2(2m)\left(\frac d2\right)^2\\
&=2I_i.
\end{aligned}
$$

The ratio makes every cancellation visible:

$$
\frac{I_f}{I_i}
=\frac{2(2m)(d/2)^2}{2m(d/2)^2}
=2.
$$

Because the radius does not change, moment of inertia varies directly with the mass at each cup.

```quiz
type: radio
id: p3-inertia-factor
content: |-
  Two identical rotating cups remain at the same distance from the axis. Each initially has mass $m$ and then holds enough water that each cup-plus-water mass becomes $3m$. How does the total moment of inertia change?
options:
- id: p3-inertia-a
  content: |-
    $I_f=3I_i$
  correct: true
  feedback: |-
    With the radius fixed, every term $mr^2$ is multiplied by $3$, so the total moment of inertia is also multiplied by $3$.
- id: p3-inertia-b
  content: |-
    $I_f=9I_i$
- id: p3-inertia-c
  content: |-
    $I_f=I_i/3$
- id: p3-inertia-d
  content: |-
    $I_f=6I_i$
- id: p3-inertia-e
  content: |-
    $I_f=I_i$
```

---

<a id="use-the-inverse-change-in-angular-speed"></a>
## Use the Inverse Change in Angular Speed

**Example:** If a rotating system's moment of inertia doubles while angular momentum is conserved, how does its angular speed change?

**Explanation**

Make $\omega_f$ the subject of the conservation equation:

$$
\omega_f=\frac{I_i}{I_f}\omega_i.
$$

If $I_f=2I_i$, then

$$
\omega_f
=\frac{I_i}{2I_i}\omega_i
=\frac12\omega_i.
$$

This is an inverse relationship: multiplying $I$ by a factor multiplies $\omega$ by the reciprocal factor.

```quiz
type: radio
id: p3-inverse-factor
content: |-
  A rotating system has negligible external torque. Its moment of inertia becomes $1.5$ times its initial value. What is its final angular speed in terms of $\omega_i$?
options:
- id: p3-inverse-a
  content: |-
    $\omega_f=\dfrac23\omega_i$
  correct: true
  feedback: |-
    Conservation gives $\omega_f=(I_i/I_f)\omega_i=(1/1.5)\omega_i=(2/3)\omega_i$.
- id: p3-inverse-b
  content: |-
    $\omega_f=1.5\omega_i$
- id: p3-inverse-c
  content: |-
    $\omega_f=\dfrac12\omega_i$
- id: p3-inverse-d
  content: |-
    $\omega_f=\dfrac32\omega_i$
- id: p3-inverse-e
  content: |-
    $\omega_f=\omega_i$
```

---

<a id="apply-the-method-to-problem-3"></a>
## Apply the Method to Problem 3

**Example:** Two cups, each of mass $m$, are connected by a negligible-mass rod of length $d$ and rotate at angular speed $\omega_0$. Rain falls into the cups until each contains an additional water mass $m$. What is the final angular speed?

Use $m=0.46\ \mathrm{kg}$, $d=0.68\ \mathrm{m}$, and $\omega_0=4.2\ \mathrm{rad/s}$.

![](<../Source/Images/rotating-cups-collecting-rain.png>)

**Explanation**

Each cup is $d/2$ from the axis. Initially,

$$
I_i=2m\left(\frac d2\right)^2.
$$

After the capture, each cup's mass doubles, so $I_f=2I_i$. Conservation of angular momentum gives

$$
I_i\omega_0=I_f\omega_f,
\qquad
\omega_f=\frac{\omega_0}{2}=2.1\ \mathrm{rad/s}.
$$

The mass and rod length cancel.

The answer choices diagnose common mistakes:

- $4.2$ assumes the angular speed stays constant even though $I$ doubles.
- $8.4$ changes angular speed in the same direction as moment of inertia instead of inversely.
- $1.05$ incorrectly treats the two cups and the doubling of each cup's mass as a factor of $4$.
- $0.46$ copies the given cup mass rather than calculating an angular speed.

```quiz
type: radio
id: p3-source-check
content: |-
  **Question 2**

  Two cups, each of mass $m$, are connected by a negligible-mass rod of length $d$ and rotate at angular speed $\omega_0$. Rain falls into the cups until each contains an additional water mass $m$. What is the final angular speed?

  Use $m=0.46\ \mathrm{kg}$, $d=0.68\ \mathrm{m}$, and $\omega_0=4.2\ \mathrm{rad/s}$.

  ![](<../Source/Images/rotating-cups-collecting-rain.png>)

  Enter the final angular speed in radians per second as a number only:
options:
- id: p3-source-a
  content: |-
    $2.1$
  correct: true
  feedback: |-
    Each cup is $d/2$ from the axis. Initially,

    $$
    I_i=2m\left(\frac d2\right)^2.
    $$

    After the capture, each cup's mass doubles, so $I_f=2I_i$. Conservation of angular momentum gives

    $$
    I_i\omega_0=I_f\omega_f,
    \qquad
    \omega_f=\frac{\omega_0}{2}=2.1\ \mathrm{rad/s}.
    $$

    The mass and rod length cancel.
- id: p3-source-b
  content: |-
    $4.2$
- id: p3-source-c
  content: |-
    $8.4$
- id: p3-source-d
  content: |-
    $1.05$
- id: p3-source-e
  content: |-
    $0.46$
```

---

## Summary

- Cue: mass is captured by a rotating system at a fixed radius, with negligible external torque.
- Compare moments of inertia by their multiplicative factor before substituting numbers.
- Conserve angular momentum: $I_i\omega_i=I_f\omega_f$.
- If $I$ grows by a factor $q$, then $\omega$ shrinks by the reciprocal factor $1/q$.
- In Problem 3, $I_f/I_i=2$ because the common $m$ and $(d/2)^2$ factors cancel, so $\omega_f=\omega_0/2=2.1\ \mathrm{rad/s}$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
