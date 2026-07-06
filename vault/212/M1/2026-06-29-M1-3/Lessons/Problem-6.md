# Threshold Angular Speed Before Slipping

<!--
lesson-id: 212-M1-014
topic-code: MTH212.M1.14
-->

## Table of Contents

- [Introduction](#introduction)
- [Set Up the Threshold Equation](#set-up-the-threshold-equation)
- [Cancel Mass and Solve for Angular Speed](#cancel-mass-and-solve-for-angular-speed)
- [Compute the Threshold Speed](#compute-the-threshold-speed)
- [Avoid the Extra-Given Trap](#avoid-the-extra-given-trap)

## Prerequisites

- Static friction can adjust up to a maximum value $f_{s,\max}=\mu_s N$.
- On a horizontal surface, the normal force is $N=mg$.
- Circular motion at angular speed $\omega$ requires centripetal force $F_c=m\omega^2 r$.
- To solve $x^2=A$ for a positive physical quantity, use $x=\sqrt{A}$.

---

<a id="introduction"></a>
## Introduction

When an object rides on a horizontal turntable and is about to slip, the recognition cue is the phrase "just starts to slip." At that instant, static friction is at its maximum value and supplies the needed centripetal force.

This setup assumes the surface is horizontal and static friction is the inward horizontal force. The normal force balances weight, so the maximum static friction is $\mu_smg$.

The reusable move is:

$$
\mu_s mg=m\omega^2 r
$$

Then cancel the mass and solve for the threshold angular speed:

$$
\omega=\sqrt{\frac{\mu_s g}{r}}
$$

---

<a id="set-up-the-threshold-equation"></a>
## Set Up the Threshold Equation

**Example:** A small puck sits on a horizontal rotating platform at radius $0.60\ \mathrm{m}$. The coefficient of static friction is $\mu_s=0.40$. Write the equation that applies when the puck is just about to slip.

**Explanation**

At the threshold, static friction has reached its maximum:

$$
f_{s,\max}=\mu_s N=\mu_s mg
$$

That friction force points inward and supplies the centripetal force:

$$
F_c=m\omega^2r
$$

So the threshold equation is

$$
\mu_smg=m\omega^2r
$$

The weight $mg$ itself is not the centripetal force; it is used only to find the normal force and therefore the maximum static friction.

```quiz
type: radio
id: q6-1
content: |-
  A coin rides on a horizontal turntable at radius $0.50\ \mathrm{m}$ with coefficient of static friction $\mu_s=0.30$. Which equation matches the instant when the coin is just about to slip?
options:
- id: q6-1-a
  content: |-
    $\mu_smg=m\omega^2r$
  correct: true
- id: q6-1-b
  content: |-
    $\mu_smg=m\omega r$
- id: q6-1-c
  content: |-
    $mg=m\omega^2r$
- id: q6-1-d
  content: |-
    $\mu_smg=\dfrac{m\omega^2}{r}$
- id: q6-1-e
  content: |-
    $\mu_smgr=m\omega^2$
```

---

<a id="cancel-mass-and-solve-for-angular-speed"></a>
## Cancel Mass and Solve for Angular Speed

**Example:** A $0.080\ \mathrm{kg}$ object sits at radius $0.25\ \mathrm{m}$ on a turntable with $\mu_s=0.50$. Find a formula for the angular speed at which it is just about to slip.

**Explanation**

Start with the threshold equation:

$$
\mu_smg=m\omega^2r
$$

The mass appears on both sides, so it cancels:

$$
\mu_sg=\omega^2r
$$

Divide by $r$:

$$
\omega^2=\frac{\mu_sg}{r}
$$

Angular speed is positive here, so take the positive square root:

$$
\omega=\sqrt{\frac{\mu_sg}{r}}
$$

For this object,

$$
\omega=\sqrt{\frac{(0.50)(9.8)}{0.25}}
$$

This result assumes $r>0$. It also shows why the object's mass does not belong in the final expression.

```quiz
type: radio
id: q6-2
content: |-
  A $0.12\ \mathrm{kg}$ object is on a horizontal turntable at radius $0.40\ \mathrm{m}$ with $\mu_s=0.25$. Which expression gives the threshold angular speed?
options:
- id: q6-2-a
  content: |-
    $\sqrt{\dfrac{(0.25)(9.8)}{0.40}}$
  correct: true
- id: q6-2-b
  content: |-
    $\dfrac{(0.25)(9.8)}{0.40}$
- id: q6-2-c
  content: |-
    $\sqrt{(0.25)(9.8)(0.40)}$
- id: q6-2-d
  content: |-
    $\sqrt{\dfrac{0.40}{(0.25)(9.8)}}$
- id: q6-2-e
  content: |-
    $\sqrt{\dfrac{(0.12)(0.25)(9.8)}{0.40}}$
```

---

<a id="compute-the-threshold-speed"></a>
## Compute the Threshold Speed

**Example:** A button on a turntable is at radius $0.70\ \mathrm{m}$. The coefficient of static friction is $\mu_s=0.35$. Find the angular speed at which the button is just about to slip.

**Explanation**

Use the threshold formula:

$$
\omega=\sqrt{\frac{\mu_sg}{r}}
$$

Substitute the values:

$$
\omega=\sqrt{\frac{(0.35)(9.8)}{0.70}}
$$

Compute inside the square root first:

$$
\frac{(0.35)(9.8)}{0.70}=4.9
$$

Then take the square root:

$$
\omega=\sqrt{4.9}\approx 2.2\ \mathrm{rad}/\mathrm{s}
$$

The units also check:

$$
\frac{g}{r}=\frac{\mathrm{m}/\mathrm{s}^2}{\mathrm{m}}=\frac{1}{\mathrm{s}^2}
$$

Taking the square root gives $1/\mathrm{s}$, which is the same unit size as $\mathrm{rad}/\mathrm{s}$ because radians are dimensionless.

```quiz
type: radio
id: q6-3
content: |-
  A small object rests on a horizontal turntable at radius $0.80\ \mathrm{m}$. If $\mu_s=0.20$, what is the threshold angular speed?
options:
- id: q6-3-a
  content: |-
    $1.6\ \mathrm{rad}/\mathrm{s}$
  correct: true
- id: q6-3-b
  content: |-
    $2.5\ \mathrm{rad}/\mathrm{s}$
- id: q6-3-c
  content: |-
    $0.16\ \mathrm{rad}/\mathrm{s}$
- id: q6-3-d
  content: |-
    $0.64\ \mathrm{rad}/\mathrm{s}$
- id: q6-3-e
  content: |-
    $3.9\ \mathrm{rad}/\mathrm{s}$
```

---

<a id="avoid-the-extra-given-trap"></a>
## Avoid the Extra-Given Trap

**Example:** A $2.0\ \mathrm{g}$ bead sits at radius $0.45\ \mathrm{m}$ on a horizontal turntable. The coefficient of static friction is $\mu_s=0.15$. Find the threshold angular speed.

**Explanation**

The mass is extra information for this specific question because it cancels:

$$
\mu_smg=m\omega^2r
$$

After cancellation,

$$
\omega=\sqrt{\frac{\mu_sg}{r}}
$$

Now substitute only $\mu_s$, $g$, and $r$:

$$
\omega=\sqrt{\frac{(0.15)(9.8)}{0.45}}
$$

So

$$
\omega=\sqrt{3.27}\approx 1.8\ \mathrm{rad}/\mathrm{s}
$$

```quiz
type: radio
id: q6-4
content: |-
  A $1.3\ \mathrm{g}$ coin on a turntable at radius $0.35\ \mathrm{m}$ has maximum static friction coefficient $\mu_s=0.18$ between the coin and the surface.

  Find $\omega$ in $\mathrm{rad}/\mathrm{s}$ such that the coin just starts to slip.
options:
- id: q6-4-a
  content: |-
    $2.2\ \mathrm{rad}/\mathrm{s}$
  correct: true
- id: q6-4-b
  content: |-
    $5.0\ \mathrm{rad}/\mathrm{s}$
- id: q6-4-c
  content: |-
    $0.79\ \mathrm{rad}/\mathrm{s}$
- id: q6-4-d
  content: |-
    $0.081\ \mathrm{rad}/\mathrm{s}$
- id: q6-4-e
  content: |-
    $13\ \mathrm{rad}/\mathrm{s}$
```

---

## Summary

Use this checklist when a turntable object is "just about to slip":

1. Maximum static friction supplies the centripetal force: $\mu_smg=m\omega^2r$.
2. Cancel $m$; the mass does not affect the threshold angular speed on a horizontal surface.
3. Solve for angular speed: $\omega=\sqrt{\mu_sg/r}$.
4. Divide by $r$ before taking the square root; do not multiply by $r$ or forget the square root.

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Finding the Minimum Period Before a Coin Slips](<../../2026-07-05-PQ-1/Lessons/Problem-4.md>)

<!-- study-guide-nav:end -->

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]
