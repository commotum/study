# Finding a Falling Unwinding Cylinder's Speed

<!--
lesson-id: 212-M2-056
topic-code: MTH212.M2.56
-->

## Table of Contents

- [Introduction](#introduction)
- [Account for Translation and Rotation](#account-for-translation-and-rotation)
- [Use the Unwinding Constraint](#use-the-unwinding-constraint)
- [Insert the Cylinder's Moment of Inertia](#insert-the-cylinders-moment-of-inertia)
- [Check the Result Physically](#check-the-result-physically)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Use conservation of mechanical energy for an ideal falling-and-unwinding system.
- Know $K_{\mathrm{trans}}=\frac12mv^2$ and $K_{\mathrm{rot}}=\frac12I\omega^2$.
- Know that a uniform solid cylinder has $I=\frac12mr^2$ about its central axis.
- Rearrange a symbolic equation and select the nonnegative square root for speed.

---

<a id="introduction"></a>
## Introduction

A cylinder descending while a fixed string unwinds has two kinds of motion at once: its center of mass falls, and the cylinder spins. The gravitational potential energy lost through height $h$ must therefore become both translational and rotational kinetic energy.

The key constraint comes from the string unwinding without slipping on the cylinder. The point where the taut string leaves the rim is instantaneously at rest, so the center-of-mass and angular speeds satisfy

$$
v=r\omega.
$$

For the ideal model implied by the problem, use this sequence:

1. Write one energy equation with both final kinetic-energy terms.
2. Replace $\omega$ with $v/r$.
3. Insert $I=\frac12mr^2$ for a uniform solid cylinder.
4. Factor the shared $mv^2$, isolate $v^2$, and select the positive root required for a speed.

Throughout the symbolic work, $v$ is the subject of the equation. Treat $m$, $r$, $g$, and $h$ as given constants.

---

<a id="account-for-translation-and-rotation"></a>
## Account for Translation and Rotation

**Example:** Write the energy equation for a rigid cylinder that starts from rest and descends a vertical distance $h$ as a fixed string unwinds without slipping.

**Explanation**

Choose the final height as the zero of gravitational potential energy. Initially, the cylinder has gravitational potential energy $mgh$ and no kinetic energy. Finally, its center of mass translates with speed $v$ while the cylinder rotates with angular speed $\omega$:

$$
mgh=\frac12mv^2+\frac12I\omega^2.
$$

The right side needs both terms. Using only $\frac12mv^2$ would model a nonrotating falling object and would predict a speed that is too large.

```quiz
type: radio
id: unwinding-cylinder-energy-accounting
shuffle: true
content: |-
  A rigid cylinder starts from rest and falls while a fixed string unwinds without slipping. Which equation correctly accounts for its energy after descending height $H$?
options:
- id: translation-plus-rotation
  content: |-
    $mgH=\dfrac12mv^2+\dfrac12I\omega^2$
  correct: true
  feedback: |-
    The center of mass translates while the cylinder spins, so the lost gravitational potential energy becomes both $\frac12mv^2$ and $\frac12I\omega^2$.
- id: translation-only
  content: |-
    $mgH=\dfrac12mv^2$
  feedback: |-
    This omits the cylinder's rotational kinetic energy. Because some of $mgH$ goes into spin, the translation-only equation would overestimate the center-of-mass speed.
- id: rotation-only
  content: |-
    $mgH=\dfrac12I\omega^2$
  feedback: |-
    The cylinder rotates, but its center of mass also moves downward. The missing translational term is $\frac12mv^2$.
- id: subtract-rotation
  content: |-
    $mgH=\dfrac12mv^2-\dfrac12I\omega^2$
  feedback: |-
    Both kinetic-energy terms are nonnegative contributions to the final energy. Rotation adds to the energy total; it is not subtracted from translation.
- id: double-rotation
  content: |-
    $mgH=\dfrac12mv^2+I\omega^2$
  feedback: |-
    Rotational kinetic energy is $\frac12I\omega^2$. Dropping its factor of one-half overcounts the energy stored in the cylinder's spin.
```

---

<a id="use-the-unwinding-constraint"></a>
## Use the Unwinding Constraint

**Example:** Express the rotational kinetic energy entirely in terms of the center-of-mass speed $v$.

**Explanation**

No slipping between the stationary string and the rim connects the two speeds:

$$
v=r\omega
\qquad\Longrightarrow\qquad
\omega=\frac{v}{r}.
$$

Therefore,

$$
K_{\mathrm{rot}}
=\frac12I\omega^2
=\frac12I\left(\frac{v}{r}\right)^2.
$$

The square applies to both $v$ and $r$. This substitution reduces the energy equation to one unknown, the requested speed $v$.

```quiz
type: radio
id: unwinding-cylinder-constraint
shuffle: true
content: |-
  A cylinder unwinds from a stationary string without slipping. If its center-of-mass speed is $v$, which expression is its rotational kinetic energy?
options:
- id: half-i-v2-over-r2
  content: |-
    $\dfrac12I\dfrac{v^2}{r^2}$
  correct: true
  feedback: |-
    The no-slip relation gives $\omega=v/r$. Substituting into $\frac12I\omega^2$ gives $\frac12I(v/r)^2=\frac12Iv^2/r^2$.
- id: half-i-v2
  content: |-
    $\dfrac12Iv^2$
  feedback: |-
    This substitutes linear speed directly for angular speed. The relation $\omega=v/r$ supplies the required factor $1/r^2$ after squaring.
- id: half-i-v-over-r
  content: |-
    $\dfrac12I\dfrac{v}{r}$
  feedback: |-
    Rotational kinetic energy depends on $\omega^2$, not $\omega$. Both $v$ and $r$ must be squared after using $\omega=v/r$.
- id: half-i-r2-v2
  content: |-
    $\dfrac12Ir^2v^2$
  feedback: |-
    This reverses the no-slip substitution. From $v=r\omega$, the angular speed is $v/r$, so the rotational term contains $1/r^2$, not $r^2$.
- id: zero
  content: |-
    $0$
  feedback: |-
    No slipping does not mean no rotation. It constrains the nonzero angular speed to $\omega=v/r$ whenever the center of mass is moving.
```

---

<a id="insert-the-cylinders-moment-of-inertia"></a>
## Insert the Cylinder's Moment of Inertia

**Example:** Find the center-of-mass speed of a uniform solid cylinder after it starts from rest and unwinds through height $h$.

**Explanation**

Insert $I=\frac12mr^2$ and $\omega=v/r$ only after writing the full energy equation:

$$
\begin{aligned}
mgh
&=\frac12mv^2+\frac12I\omega^2\\
&=\frac12mv^2
 +\frac12\left(\frac12mr^2\right)
 \left(\frac{v}{r}\right)^2\\
&=\frac12mv^2+\frac14mv^2\\
&=mv^2\left(\frac12+\frac14\right)\\
&=\frac34mv^2.
\end{aligned}
$$

Factoring makes the common unknown factor visible. Cancel the nonzero mass and isolate $v^2$:

$$
gh=\frac34v^2
\qquad\Longrightarrow\qquad
v^2=\frac{4gh}{3}.
$$

Algebraically, taking the square root gives two possible signed values,

$$
v=\pm\sqrt{\frac{4gh}{3}}.
$$

The problem asks for speed, which is a nonnegative magnitude, so keep the positive value:

$$
\boxed{v=\sqrt{\frac{4gh}{3}}}.
$$

Notice how the $r^2$ in the moment of inertia cancels the $1/r^2$ from $\omega^2$. The cylinder's mass and radius therefore do not remain in the final speed.

```quiz
type: radio
id: unwinding-solid-cylinder-speed
shuffle: true
content: |-
  A uniform solid cylinder starts from rest and falls distance $H$ while a string unwinds without slipping. What is its center-of-mass speed?
options:
- id: sqrt-four-gh-over-three
  content: |-
    $\sqrt{\dfrac{4gH}{3}}$
  correct: true
  feedback: |-
    With $I=\frac12mr^2$ and $\omega=v/r$, the rotational energy is $\frac14mv^2$. Thus $mgH=\frac34mv^2$, so $v^2=4gH/3$ and speed is the positive square root.
- id: sqrt-two-gh
  content: |-
    $\sqrt{2gH}$
  feedback: |-
    This is the nonrotating free-fall result obtained from $mgH=\frac12mv^2$. The unwinding cylinder also has rotational kinetic energy, so its center of mass is slower.
- id: sqrt-gh
  content: |-
    $\sqrt{gH}$
  feedback: |-
    This would follow if the rotational term were $\frac12mv^2$, as for a hoop with $I=mr^2$. A solid cylinder has $I=\frac12mr^2$, so its rotational term is only $\frac14mv^2$.
- id: four-gh-over-three
  content: |-
    $\dfrac{4gH}{3}$
  feedback: |-
    The energy equation gives $v^2=4gH/3$. The question asks for $v$, so the positive square root is required.
- id: sqrt-three-gh-over-four
  content: |-
    $\sqrt{\dfrac{3gH}{4}}$
  feedback: |-
    This fails to invert the coefficient $\frac34$ when isolating $v^2$. From $gH=\frac34v^2$, multiply by $4/3$, not by $3/4$.
```

---

<a id="check-the-result-physically"></a>
## Check the Result Physically

**Example:** Compare the cylinder's speed with the speed $\sqrt{2gh}$ of a nonrotating object released from rest through the same height.

**Explanation**

The cylinder's speed satisfies

$$
\sqrt{\frac{4gh}{3}}<\sqrt{2gh}.
$$

That inequality is physically sensible: the cylinder's gravitational energy is divided between translation and rotation, so less energy is available for center-of-mass motion than in nonrotating free fall.

A useful general check writes the moment of inertia as

$$
I=\kappa mr^2.
$$

Then the same energy method gives

$$
mgh=\frac12(1+\kappa)mv^2
\qquad\Longrightarrow\qquad
v=\sqrt{\frac{2gh}{1+\kappa}}.
$$

For a uniform solid cylinder, $\kappa=\frac12$, which reproduces $\sqrt{4gh/3}$. Increasing $\kappa$ stores a larger share of the energy in rotation and lowers the translational speed.

Units provide an independent check. Numerical factors such as $4/3$ are dimensionless, so

$$
\left[\frac{4gh}{3}\right]
=\left(\frac{\mathrm m}{\mathrm s^2}\right)(\mathrm m)
=\frac{\mathrm m^2}{\mathrm s^2},
\qquad
\left[\sqrt{\frac{4gh}{3}}\right]
=\frac{\mathrm m}{\mathrm s}.
$$

The result therefore has the required units of speed.

```quiz
type: radio
id: unwinding-inertia-comparison
shuffle: true
content: |-
  Two bodies of the same mass and radius unwind from fixed strings through the same height. Body A has $I_A=\frac12mr^2$, while body B has $I_B=mr^2$. Which statement is correct?
options:
- id: a-faster
  content: |-
    Body A has the greater center-of-mass speed.
  correct: true
  feedback: |-
    The general result is $v=\sqrt{2gh/(1+\kappa)}$. Body A has the smaller inertia factor, $\kappa=\frac12$, so less energy goes into rotation and more remains for translation.
- id: b-faster
  content: |-
    Body B has the greater center-of-mass speed.
  feedback: |-
    Body B has the larger rotational inertia factor. At the same $v$, it requires more rotational energy, so conservation of energy gives it a smaller, not larger, center-of-mass speed.
- id: same-speed
  content: |-
    They have the same center-of-mass speed because mass and radius match.
  feedback: |-
    Mass and radius cancel only after the dimensionless inertia factor $\kappa=I/(mr^2)$ is retained. Different values of $\kappa$ lead to different speeds.
- id: cannot-compare-without-mass
  content: |-
    Their speeds cannot be compared without a numerical mass.
  feedback: |-
    The common mass cancels from the energy equation. The comparison depends on the inertia factors and the shared drop height, not on the numerical mass.
- id: b-free-fall-speed
  content: |-
    Body B reaches the nonrotating free-fall speed.
  feedback: |-
    Body B still rotates, so some energy is stored in $\frac12I\omega^2$. A body reaches $\sqrt{2gh}$ only in the limiting model with no rotational energy.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the original free-response problem symbolically before checking the choices.

**Explanation**

> **Question 3**
>
> A uniform solid cylinder of radius $r$ and mass $m$ starts from rest with a string wound around it. Find the center-of-mass speed after it unwinds and falls a distance $h$.
>
> ![[../Source/Images/yoyo.jpg]]

The requested answer form is a symbolic center-of-mass speed. Preserve the given variables $r$, $m$, and $h$ in the setup; after applying $I=\frac12mr^2$ and $v=r\omega$, the mass and radius cancel.

```quiz
type: radio
id: khadley-rolling-q3
shuffle: true
content: |-
  Which expression is the center-of-mass speed for the original falling, unwinding uniform solid cylinder?
options:
- id: original-sqrt-four-gh-over-three
  content: |-
    $\sqrt{\dfrac{4gh}{3}}$
  correct: true
  feedback: |-
    The cylinder has both translational and rotational energy. Using $I=mr^2/2$ and $v=r\omega$ gives $mgh=\frac12mv^2+\frac14mv^2=\frac34mv^2$, hence $v=\sqrt{4gh/3}$.
- id: original-sqrt-two-gh
  content: |-
    $\sqrt{2gh}$
  feedback: |-
    This treats the cylinder as a nonrotating falling particle. The string makes the cylinder spin, so some of the gravitational energy becomes rotational kinetic energy and the center-of-mass speed is smaller.
- id: original-sqrt-gh
  content: |-
    $\sqrt{gh}$
  feedback: |-
    This assigns $\frac12mv^2$ to rotation, which corresponds to $I=mr^2$. For the given uniform solid cylinder, $I=mr^2/2$ and the rotational term is $\frac14mv^2$.
- id: original-four-gh-over-three
  content: |-
    $\dfrac{4gh}{3}$
  feedback: |-
    This is the value of $v^2$, not the requested speed. Taking the nonnegative square root gives $\sqrt{4gh/3}$.
- id: original-sqrt-four-gh-over-three-r
  content: |-
    $\sqrt{\dfrac{4gh}{3r}}$
  feedback: |-
    The radius cancels between $I\propto r^2$ and $\omega^2=v^2/r^2$. A leftover factor of $r$ also gives the wrong dimensions for a speed.
```

---

<a id="summary"></a>
## Summary

For a uniform solid cylinder that starts from rest and falls distance $h$ while a fixed string unwinds without slipping:

1. Include translation and rotation:
   $$
   mgh=\frac12mv^2+\frac12I\omega^2.
   $$
2. Use the unwinding constraint $\omega=v/r$.
3. Insert $I=\frac12mr^2$:
   $$
   mgh=\frac12mv^2+\frac14mv^2=\frac34mv^2.
   $$
4. Solve for the nonnegative speed:
   $$
   \boxed{v=\sqrt{\frac{4gh}{3}}}.
   $$

The mass and radius cancel. When solving $v^2=4gh/3$, the algebraic roots are positive and negative, but the requested speed selects the positive one. Substituting units confirms that $gh$ has units of speed squared, and a physics check confirms that $\sqrt{4gh/3}$ is below the nonrotating free-fall speed $\sqrt{2gh}$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
