# Finding a Rolling Hoop's Speed From Energy

<!--
lesson-id: 212-M2-055
topic-code: MTH212.M2.55
-->

## Table of Contents

- [Introduction](#introduction)
- [Keep Both Parts of Rolling Kinetic Energy](#keep-both-parts-of-rolling-kinetic-energy)
- [Use the No-Slip Constraint](#use-the-no-slip-constraint)
- [Insert the Hoop's Moment of Inertia](#insert-the-hoops-moment-of-inertia)
- [Recognize What Does Not Affect the Final Speed](#recognize-what-does-not-affect-the-final-speed)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Use conservation of mechanical energy when rolling is lossless.
- Know the translational kinetic energy $K_{\mathrm{trans}}=\frac12mv^2$.
- Know the rotational kinetic energy $K_{\mathrm{rot}}=\frac12I\omega^2$.
- Use the rolling-without-slipping constraint $v=r\omega$.
- Solve a symbolic equation for a nonnegative speed.

---

<a id="introduction"></a>
## Introduction

A hoop of mass $m$ and radius $r$ rolls without slipping down a slope through vertical height $h$, and the problem asks for the speed of its center of mass at the bottom. The supplied answer uses the standard implied condition that the hoop starts from rest and that the rolling is lossless.

The recognition cues are **rolls without slipping**, **starts from rest**, and **vertical height**. Lossless rolling conserves mechanical energy, but the final kinetic energy has two parts:

$$
K_f=\frac12mv^2+\frac12I\omega^2.
$$

Use $v=r\omega$ to express both parts in terms of the requested center-of-mass speed. Then insert the hoop's moment of inertia $I=mr^2$ and solve for the positive value of $v$.

Keep the substitutions in this order:

1. Write $mgh=\frac12mv^2+\frac12I\omega^2$.
2. Replace $omega$ with $v/r$ and $I$ with $mr^2$.
3. Simplify to an equation for $v^2$, then take the physically valid root.

---

<a id="keep-both-parts-of-rolling-kinetic-energy"></a>
## Keep Both Parts of Rolling Kinetic Energy

**Example:** Write the energy equation for a rigid object that starts from rest and rolls without slipping through vertical height $h$.

**Explanation**

Choose zero gravitational potential energy at the bottom. The object begins with energy $mgh$ and no kinetic energy. At the bottom, its center of mass translates while the object rotates about its center:

$$
mgh=\frac12mv^2+\frac12I\omega^2.
$$

The translational term describes motion of the center of mass. The rotational term describes motion about the center of mass. Omitting either term assigns the gravitational energy to the wrong physical model.

```quiz
type: radio
id: rolling-energy-accounting
shuffle: true
content: |-
  An object starts from rest and rolls without slipping through vertical height $H$. Which energy equation includes all of its final kinetic energy?
options:
- id: translation-plus-rotation
  content: |-
    $mgH=\dfrac12mv^2+\dfrac12I\omega^2$
  correct: true
  feedback: |-
    Lossless rolling converts the gravitational decrease $mgH$ into both center-of-mass translation and rotation about the center. Therefore the final energy is $\frac12mv^2+\frac12I\omega^2$.
- id: translation-only
  content: |-
    $mgH=\dfrac12mv^2$
  feedback: |-
    This is the energy equation for a nonrotating particle or an object sliding without rotation. A rolling rigid body also has rotational kinetic energy, so this equation would predict too large a speed.
- id: rotation-only
  content: |-
    $mgH=\dfrac12I\omega^2$
  feedback: |-
    Rotation is present, but the center of mass also moves down the slope with speed $v$. The translational term $\frac12mv^2$ must be included alongside the rotational term.
- id: missing-rotational-half
  content: |-
    $mgH=\dfrac12mv^2+I\omega^2$
  feedback: |-
    Rotational kinetic energy has the same one-half structure as translational kinetic energy: $K_{\mathrm{rot}}=\frac12I\omega^2$. Omitting that factor overcounts the energy stored in rotation.
- id: subtract-rotation
  content: |-
    $mgH=\dfrac12mv^2-\dfrac12I\omega^2$
  feedback: |-
    Translational and rotational kinetic energies are both nonnegative stores of the released potential energy. Rotation does not subtract from the total kinetic energy; the two terms add.
```

---

<a id="use-the-no-slip-constraint"></a>
## Use the No-Slip Constraint

**Example:** Rewrite the rotational kinetic energy in terms of the center-of-mass speed when the object rolls without slipping.

**Explanation**

Rolling without slipping connects the linear and angular speeds:

$$
v=r\omega
\qquad\Longrightarrow\qquad
\omega=\frac{v}{r}.
$$

Substitute this into the rotational term:

$$
K_{\mathrm{rot}}
=\frac12I\omega^2
=\frac12I\left(\frac{v}{r}\right)^2.
$$

The square applies to both $v$ and $r$. This substitution is what lets the energy equation be solved for the requested variable $v$.

```quiz
type: radio
id: rolling-hoop-rotational-energy
shuffle: true
content: |-
  A hoop has $I=mr^2$ and rolls without slipping with center-of-mass speed $v$. What is its rotational kinetic energy in terms of $m$ and $v$?
options:
- id: half-mv-squared
  content: |-
    $\dfrac12mv^2$
  correct: true
  feedback: |-
    No slipping gives $\omega=v/r$. Thus $K_{\mathrm{rot}}=\frac12(mr^2)(v^2/r^2)=\frac12mv^2$, because the two powers of $r$ cancel.
- id: mv-squared
  content: |-
    $mv^2$
  feedback: |-
    The radius cancellation is correct, but rotational kinetic energy still contains its factor of one-half. For a hoop, the result is $\frac12mv^2$.
- id: half-mr-squared-v-squared
  content: |-
    $\dfrac12mr^2v^2$
  feedback: |-
    This inserts the linear speed $v$ directly where the angular speed $\omega$ belongs. Using $\omega=v/r$ supplies a factor $1/r^2$ that cancels the $r^2$ in the hoop's inertia.
- id: half-mv-squared-over-r-squared
  content: |-
    $\dfrac12m\dfrac{v^2}{r^2}$
  feedback: |-
    This uses the $1/r^2$ from $\omega^2$ but drops the hoop inertia's matching factor $r^2$. Both factors are present and cancel, leaving $\frac12mv^2$.
- id: zero-rotation
  content: |-
    $0$
  feedback: |-
    No slipping does not mean no rotation; it fixes the nonzero relation $\omega=v/r$. Rotational kinetic energy is zero only when the hoop's speed is also zero.
```

---

<a id="insert-the-hoops-moment-of-inertia"></a>
## Insert the Hoop's Moment of Inertia

**Example:** Find the center-of-mass speed of the hoop after it rolls through vertical height $h$.

**Explanation**

Start with energy conservation and substitute both hoop relationships:

$$
\begin{aligned}
mgh
&=\frac12mv^2+\frac12I\omega^2\\
&=\frac12mv^2+\frac12(mr^2)\left(\frac{v}{r}\right)^2\\
&=\frac12mv^2+\frac12mv^2\\
&=mv^2.
\end{aligned}
$$

Cancel the common mass and solve for the nonnegative speed:

$$
v^2=gh
\qquad\Longrightarrow\qquad
\boxed{v=\sqrt{gh}}.
$$

Only the positive root is used because the question asks for speed, a magnitude.

A compact check is to write a rolling object's inertia as $I=\kappa mr^2$. The same steps give

$$
mgh=\frac12(1+\kappa)mv^2
\qquad\Longrightarrow\qquad
v=\sqrt{\frac{2gh}{1+\kappa}}.
$$

For a hoop, $\kappa=1$, so this immediately reduces to $v=\sqrt{gh}$.

```quiz
type: radio
id: rolling-hoop-symbolic-speed
shuffle: true
content: |-
  A hoop rolls without slipping from rest through vertical height $H$. What is its center-of-mass speed at the bottom?
options:
- id: square-root-gh
  content: |-
    $\sqrt{gH}$
  correct: true
  feedback: |-
    For a hoop, translation and rotation each contribute $\frac12mv^2$, so the total final kinetic energy is $mv^2$. Setting $mgH=mv^2$ gives the speed $\sqrt{gH}$.
- id: square-root-two-gh
  content: |-
    $\sqrt{2gH}$
  feedback: |-
    This assigns all of $mgH$ to translational kinetic energy and omits the hoop's rotation. Because half the final kinetic energy is rotational, the hoop's speed is $\sqrt{gH}$ instead.
- id: gh
  content: |-
    $gH$
  feedback: |-
    Energy conservation gives $v^2=gH$, not $v=gH$. Taking the positive square root produces both the correct equation and the correct speed units.
- id: square-root-gh-over-two
  content: |-
    $\sqrt{\dfrac{gH}{2}}$
  feedback: |-
    This treats the two one-half kinetic-energy terms as though they total $2mv^2$. In fact, $\frac12mv^2+\frac12mv^2=mv^2$, so $v^2=gH$.
- id: square-root-two-gh-over-three
  content: |-
    $\sqrt{\dfrac{2gH}{3}}$
  feedback: |-
    This overcounts the hoop's rotational energy as $mv^2$ instead of $\frac12mv^2$. Using $I=mr^2$ and $\omega=v/r$ makes the two kinetic terms equal, giving $v=\sqrt{gH}$.
```

---

<a id="recognize-what-does-not-affect-the-final-speed"></a>
## Recognize What Does Not Affect the Final Speed

**Example:** Decide whether the hoop's mass, radius, or incline angle remains in the final speed after a fixed vertical drop.

**Explanation**

The mass cancels between $mgh$ and the two kinetic-energy terms. The radius cancels between $I=mr^2$ and $\omega^2=v^2/r^2$. The incline angle never enters the energy change because gravity supplies potential energy according to the vertical height $h$, not the distance or angle along the slope.

Therefore, for hoops that start from rest and roll losslessly through the same vertical height,

$$
v=\sqrt{gh}
$$

regardless of their mass, radius, or slope angle. These quantities can affect forces or travel time, but not this requested final speed.

```quiz
type: radio
id: rolling-hoop-same-height-comparison
shuffle: true
content: |-
  Two hoops start from rest and roll without slipping through the same vertical height. They have different masses and radii and use slopes with different angles. How do their center-of-mass speeds at the bottom compare?
options:
- id: same-speed
  content: |-
    They have the same speed.
  correct: true
  feedback: |-
    For any hoop, $I=mr^2$ and no slipping gives $v=\sqrt{gh}$. With the same vertical height $h$, mass, radius, and incline angle cancel or never enter, so the final speeds match.
- id: heavier-faster
  content: |-
    The heavier hoop is faster.
  feedback: |-
    A heavier hoop starts with more potential energy, but its translational and rotational inertias increase by the same mass factor. Mass cancels from the energy equation, so greater mass does not increase the final speed.
- id: larger-radius-faster
  content: |-
    The hoop with larger radius is faster.
  feedback: |-
    A larger radius raises $I=mr^2$, but no slipping lowers $\omega=v/r$ by the matching factor. The radius factors cancel from the rotational energy, so radius does not decide the final speed.
- id: steeper-faster
  content: |-
    The hoop on the steeper slope is faster.
  feedback: |-
    A steeper slope can change the acceleration and travel time along a particular path, but the final energy depends on the vertical drop. Equal $h$ gives equal final speed for lossless rolling hoops.
- id: lighter-faster
  content: |-
    The lighter hoop is faster.
  feedback: |-
    Lower mass reduces both the available potential energy and the hoop's kinetic-energy scale by the same factor. Since mass cancels, neither the lighter nor the heavier hoop has a speed advantage.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the original symbolic problem before checking the choices.

**Explanation**

> A hoop of mass $m$ and radius $r$ rolls without slipping down a slope through vertical height $h$. Find the speed of its center of mass at the bottom.

Keep the response symbolic. Include both final kinetic-energy terms, then use $I=mr^2$ and $v=r\omega$ before solving for the speed.

```quiz
type: radio
id: khadley-rolling-q2
shuffle: true
content: |-
  Which expression gives the center-of-mass speed for the original hoop problem?
options:
- id: original-square-root-gh
  content: |-
    $\sqrt{gh}$
  correct: true
  feedback: |-
    Conservation of energy includes translation and rotation. With $I=mr^2$ and $\omega=v/r$, the two kinetic terms total $mv^2$, so $mgh=mv^2$ and $v=\sqrt{gh}$.
- id: original-square-root-two-gh
  content: |-
    $\sqrt{2gh}$
  feedback: |-
    This is the result when the final energy is only $\frac12mv^2$. The hoop also rotates, so another $\frac12mv^2$ is present and the correct speed is $\sqrt{gh}$.
- id: original-gh
  content: |-
    $gh$
  feedback: |-
    The quantity $gh$ has units of speed squared. Energy conservation gives $v^2=gh$, so the requested speed requires the positive square root.
- id: original-square-root-gh-over-r
  content: |-
    $\sqrt{\dfrac{gh}{r}}$
  feedback: |-
    The radius appears in both $I=mr^2$ and $\omega^2=v^2/r^2$, so it cancels. Leaving $r$ in this expression also gives incorrect dimensions for speed.
- id: original-square-root-gh-over-two
  content: |-
    $\sqrt{\dfrac{gh}{2}}$
  feedback: |-
    Translation and rotation each contribute $\frac12mv^2$; together they make $mv^2$, not $2mv^2$. Therefore $v^2=gh$, without an extra factor of two in the denominator.
```

---

<a id="summary"></a>
## Summary

When an object rolls without slipping from rest through vertical height $h$:

1. Write both final kinetic-energy terms:
   $$
   mgh=\frac12mv^2+\frac12I\omega^2.
   $$
2. Use $\omega=v/r$ so the equation contains only the requested speed.
3. Insert the object's moment of inertia before simplifying.
4. For a hoop, $I=mr^2$, so
   $$
   mgh=\frac12mv^2+\frac12mv^2=mv^2.
   $$
5. Keep the positive root:
   $$
   \boxed{v=\sqrt{gh}}.
   $$

The dimensions confirm the result:

$$
[gh]
=\left(\frac{\mathrm{m}}{\mathrm{s}^2}\right)(\mathrm{m})
=\frac{\mathrm{m}^2}{\mathrm{s}^2},
\qquad
[\sqrt{gh}]=\frac{\mathrm{m}}{\mathrm{s}}.
$$

The main trap is using the sliding-particle result $\sqrt{2gh}$ and forgetting that some gravitational energy becomes rotational kinetic energy. For a hoop, mass and radius cancel, and the final speed depends on the vertical drop rather than the incline angle.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
