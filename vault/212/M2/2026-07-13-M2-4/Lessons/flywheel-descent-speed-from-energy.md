# Flywheel Descent Speed from Energy

<!--
lesson-id: 212-M2-050
topic-code: MTH212.M2.50
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Energy Ledger](#build-the-energy-ledger)
- [Convert Rotation to Linear Speed](#convert-rotation-to-linear-speed)
- [Factor and Isolate the Speed](#factor-and-isolate-the-speed)
- [Audit the Result](#audit-the-result)
- [Apply the Move to the Flywheel](#apply-the-move-to-the-flywheel)
- [Summary](#summary)

## Prerequisites

- Use $K_{\mathrm{trans}}=\dfrac12mv^2$ and $K_{\mathrm{rot}}=\dfrac12I\omega^2$.
- Use $I=\dfrac12Mr^2$ for a uniform solid flywheel about its center.
- Use the no-slip relation $v=r\omega$.
- Apply conservation of mechanical energy when dissipative losses are neglected.

---

<a id="introduction"></a>
## Introduction

When a falling block unwinds a cord from a massive flywheel, the lost gravitational potential energy becomes two kinds of kinetic energy:

$$
\text{lost gravitational energy}
=
\text{block translation}
+
\text{flywheel rotation}.
$$

For a block of mass $m$ descending a distance $h$ from rest,

$$
mgh=\frac12mv^2+\frac12I\omega^2.
$$

The recognition cues are a massive rotating flywheel, a cord that does not slip, and a requested speed after a vertical drop. The target variable is $v$; treat $m$, $M$, $r$, $h$, and $g$ as fixed symbols. Determine the speed by using no slip to write the rotational energy in terms of $v$, collecting every $v^2$ term, factoring $v^2$, and taking the positive square root.

---

<a id="build-the-energy-ledger"></a>
## Build the Energy Ledger

The flywheel's axle remains fixed, so its center does not have translational kinetic energy. The falling block translates, while the flywheel rotates.

**Example:** A block of mass $\mu$ descends a distance $y$ while turning a flywheel of moment of inertia $I$. The system starts from rest and has no dissipative losses. Write the energy equation when the block's speed is $u$ and the flywheel's angular speed is $\Omega$.

**Explanation**

The block loses gravitational potential energy $\mu gy$. That energy supplies both moving parts:

$$
\mu gy=\frac12\mu u^2+\frac12I\Omega^2.
$$

The first term is the block's translational kinetic energy. The second is the flywheel's rotational kinetic energy.

```quiz
type: radio
id: flywheel-energy-ledger
shuffle: true
content: |-
  A block of mass $p$ descends a distance $y$ from rest while a cord turns a massive flywheel of moment of inertia $I$. The cord does not slip and energy losses are negligible. Which energy equation is the correct starting point?
options:
- id: flywheel-energy-ledger-translation-only
  content: |-
    $pgy=\dfrac12pu^2$
  feedback: |-
    This would apply if the rotating object had negligible moment of inertia. The flywheel is massive and turns, so some of $pgy$ must also appear as $\tfrac12I\Omega^2$.
- id: flywheel-energy-ledger-both
  content: |-
    $pgy=\dfrac12pu^2+\dfrac12I\Omega^2$
  correct: true
  feedback: |-
    Mechanical energy is conserved: the falling block loses $pgy$, the block gains translational kinetic energy $\tfrac12pu^2$, and the fixed-axis flywheel gains rotational kinetic energy $\tfrac12I\Omega^2$.
- id: flywheel-energy-ledger-rotation-only
  content: |-
    $pgy=\dfrac12I\Omega^2$
  feedback: |-
    The rotational term accounts for the flywheel, but the descending block is also moving at speed $u$. Its translational energy $\tfrac12pu^2$ must be included.
- id: flywheel-energy-ledger-wheel-potential
  content: |-
    $(p+M)gy=\dfrac12pu^2+\dfrac12I\Omega^2$
  feedback: |-
    Only the block descends through distance $y$. The flywheel's center stays at the fixed axle, so its mass $M$ contributes rotational energy but no change $Mgy$ in gravitational potential energy.
- id: flywheel-energy-ledger-two-translations
  content: |-
    $pgy=\dfrac12(p+M)u^2$
  feedback: |-
    The flywheel's center does not translate with the cord. Its energy depends on $I$ and $\Omega$, so treating the entire flywheel mass as a particle moving at speed $u$ misrepresents fixed-axis rotation.
```

---

<a id="convert-rotation-to-linear-speed"></a>
## Convert Rotation to Linear Speed

The energy equation initially contains both $v$ and $\omega$. No slip connects them:

$$
v=r\omega
\qquad\Longrightarrow\qquad
\omega=\frac vr.
$$

**Example:** Express the rotational kinetic energy of a uniform solid flywheel of mass $M$ and radius $r$ in terms of the cord speed $v$.

**Explanation**

Substitute $I=\dfrac12Mr^2$ and $\omega=\dfrac vr$ into $K_{\mathrm{rot}}=\dfrac12I\omega^2$:

$$
K_{\mathrm{rot}}
=\frac12\left(\frac12Mr^2\right)\left(\frac vr\right)^2
=\frac14Mv^2.
$$

The factors of $r^2$ cancel. A larger radius increases the moment of inertia but decreases the angular speed required for the same cord speed by the matching factor.

```quiz
type: radio
id: flywheel-rotation-in-linear-speed
shuffle: true
content: |-
  A cord unwinds without slipping from a uniform solid flywheel of mass $M$ and radius $r$. If the cord speed is $v$, what is the flywheel's rotational kinetic energy in terms of $v$?
options:
- id: flywheel-rotation-in-linear-speed-quarter
  content: |-
    $\dfrac14Mv^2$
  correct: true
  feedback: |-
    For a solid flywheel, $I=Mr^2/2$ and no slip gives $\omega=v/r$. Therefore $\tfrac12I\omega^2=\tfrac12(Mr^2/2)(v^2/r^2)=\tfrac14Mv^2$.
- id: flywheel-rotation-in-linear-speed-half
  content: |-
    $\dfrac12Mv^2$
  feedback: |-
    This is the translational kinetic energy of a particle of mass $M$, not the rotational energy of a solid flywheel. The solid-disk factor $I=Mr^2/2$ adds another factor of $1/2$, giving $Mv^2/4$.
- id: flywheel-rotation-in-linear-speed-radius-times
  content: |-
    $\dfrac14Mr^2v^2$
  feedback: |-
    This substitutes $v$ directly for angular speed. No slip requires $\omega=v/r$, so the $1/r^2$ from $\omega^2$ cancels the $r^2$ in the moment of inertia.
- id: flywheel-rotation-in-linear-speed-radius-divide
  content: |-
    $\dfrac14M\dfrac{v^2}{r^2}$
  feedback: |-
    This keeps the $1/r^2$ from $\omega^2$ but omits the $r^2$ already present in $I=Mr^2/2$. Both factors must be substituted, and they cancel.
- id: flywheel-rotation-in-linear-speed-block-mass
  content: |-
    $\dfrac12mv^2$
  feedback: |-
    This is the falling block's translational kinetic energy. The flywheel term uses the flywheel mass $M$ through $I=Mr^2/2$ and simplifies to $Mv^2/4$.
```

---

<a id="factor-and-isolate-the-speed"></a>
## Factor and Isolate the Speed

After both kinetic-energy terms use $v$, collect every term containing $v^2$ before taking a square root. This keeps the entire effective inertia in one coefficient.

**Example:** Starting from

$$
mgh=\frac12mv^2+\frac14Mv^2,
$$

solve for the physical speed $v$.

**Explanation**

Factor $v^2$:

$$
mgh=\left(\frac12m+\frac14M\right)v^2
=\frac{2m+M}{4}v^2.
$$

Divide by the full coefficient, then take a square root:

$$
v^2=\frac{4mgh}{2m+M},
\qquad
v=\sqrt{\frac{4mgh}{2m+M}}.
$$

The algebraic equation for a signed velocity permits two roots, but the requested speed is nonnegative, so use the positive root.

```quiz
type: radio
id: flywheel-speed-numerical-check
shuffle: true
content: |-
  A $2.0\,\mathrm{kg}$ block descends $3.0\,\mathrm{m}$ from rest while turning a uniform solid flywheel of mass $6.0\,\mathrm{kg}$. Use $g=10\,\mathrm{m/s^2}$ and no slip. What is the block's speed?
options:
- id: flywheel-speed-numerical-check-correct
  content: |-
    $4.90\,\mathrm{m/s}$
  correct: true
  feedback: |-
    Conservation of energy with the solid-flywheel rotation gives $v^2=4mgh/(2m+M)=240/10=24\,\mathrm{m^2/s^2}$. Taking the positive square root gives $v=4.90\,\mathrm{m/s}$.
- id: flywheel-speed-numerical-check-free-fall
  content: |-
    $7.75\,\mathrm{m/s}$
  feedback: |-
    This is $\sqrt{2gh}$, the free-fall result obtained by assigning no energy to the flywheel. Here the flywheel rotates, so the block receives less kinetic energy and moves more slowly than free fall.
- id: flywheel-speed-numerical-check-hoop-inertia
  content: |-
    $3.87\,\mathrm{m/s}$
  feedback: |-
    This results from using $I=Mr^2$, appropriate to a thin hoop. The stated flywheel is a uniform solid disk, so $I=Mr^2/2$ and the correct speed is larger.
- id: flywheel-speed-numerical-check-rotation-only
  content: |-
    $6.32\,\mathrm{m/s}$
  feedback: |-
    This assigns the lost potential energy only to flywheel rotation. The descending block also has translational kinetic energy, so including both terms lowers the speed to $4.90\,\mathrm{m/s}$.
- id: flywheel-speed-numerical-check-no-root
  content: |-
    $24.0\,\mathrm{m/s}$
  feedback: |-
    The energy algebra produces $v^2=24\,\mathrm{m^2/s^2}$. The question asks for $v$, so a square root is still required; $24$ is not a speed and its units are squared.
```

---

<a id="audit-the-result"></a>
## Audit the Result

A symbolic result should pass both a units check and a limiting-case check.

**Example:** Check

$$
v=\sqrt{\frac{4mgh}{2m+M}}.
$$

**Explanation**

The numerator has units

$$
[mgh]=\mathrm{kg}\frac{\mathrm m}{\mathrm s^2}\mathrm m
=\frac{\mathrm{kg}\,\mathrm m^2}{\mathrm s^2},
$$

and the denominator has units of mass. The quantity under the square root therefore has units $\mathrm m^2/\mathrm s^2$, so $v$ has units $\mathrm m/\mathrm s$.

If the flywheel mass approaches zero, the formula becomes

$$
v\longrightarrow\sqrt{\frac{4mgh}{2m}}=\sqrt{2gh},
$$

the expected free-fall speed. Increasing $M$ enlarges the denominator, so a heavier flywheel makes the block slower.

```quiz
type: radio
id: flywheel-formula-audit
shuffle: true
content: |-
  Which statement correctly audits $v=\sqrt{4mgh/(2m+M)}$ for a block turning a uniform solid flywheel?
options:
- id: flywheel-formula-audit-units-limit
  content: |-
    It has units of speed, and as $M\to0$ it becomes $\sqrt{2gh}$.
  correct: true
  feedback: |-
    Dividing the energy scale $mgh$ by the mass scale $2m+M$ gives $\mathrm{m^2/s^2}$, and the square root gives $\mathrm{m/s}$. Setting $M=0$ also recovers the free-fall result $\sqrt{2gh}$.
- id: flywheel-formula-audit-radius-required
  content: |-
    It must be wrong because the flywheel radius $r$ is absent.
  feedback: |-
    No slip gives $\omega=v/r$, while the solid flywheel has $I=Mr^2/2$. The $r^2$ in $I$ cancels the $1/r^2$ in $\omega^2$, so the absence of $r$ is an expected feature of this ideal model.
- id: flywheel-formula-audit-heavier-faster
  content: |-
    Increasing $M$ increases the block's speed because the flywheel has more mass.
  feedback: |-
    The flywheel mass appears in the denominator because a larger $M$ requires more rotational kinetic energy at the same cord speed. Increasing $M$ therefore lowers $v$ rather than raising it.
- id: flywheel-formula-audit-squared-speed
  content: |-
    Its units are $\mathrm{m^2/s^2}$, so it gives $v^2$ rather than $v$.
  feedback: |-
    The expression inside the radical has units $\mathrm{m^2/s^2}$. Taking the displayed square root changes those units to $\mathrm{m/s}$, so the complete expression gives speed.
- id: flywheel-formula-audit-plus-minus
  content: |-
    It needs a $\pm$ sign because every square-root step must report two speeds.
  feedback: |-
    A squared equation has two signed velocity roots, but speed is a magnitude and cannot be negative. The question asks how fast the block moves, so the positive square root is the physical answer.
```

---

<a id="apply-the-move-to-the-flywheel"></a>
## Apply the Move to the Flywheel

Use one energy ledger, convert the rotation term with the no-slip relation, and then isolate the positive speed.

**Example:** A block of mass $\mu$ unwinds a cord from a uniform solid flywheel of mass $\mathcal M$ and radius $R$. Starting from rest, the block drops a distance $y$. Find its speed $u$.

**Explanation**

Write and reduce the energy equation:

$$
\mu gy
=\frac12\mu u^2
+\frac12\left(\frac12\mathcal M R^2\right)\left(\frac uR\right)^2
=\left(\frac12\mu+\frac14\mathcal M\right)u^2.
$$

Therefore,

$$
u=\sqrt{\frac{4\mu gy}{2\mu+\mathcal M}}.
$$

```quiz
type: radio
id: khadley-equilibrium-q2
shuffle: true
content: |-
  **Question 2**

  A block of mass $m$ is attached to a cord wrapped around a uniform solid flywheel of mass $M$ and radius $r$. Starting from rest, how fast is the block moving after descending a distance $h$? Assume the cord does not slip.

  ![](<../Source/Images/torquesystem.jpg>)
options:
- id: khadley-equilibrium-q2-correct
  content: |-
    $\displaystyle v=\sqrt{\frac{4mgh}{2m+M}}$
  correct: true
  feedback: |-
    Energy conservation gives $mgh=\tfrac12mv^2+\tfrac12I\omega^2$. With $I=Mr^2/2$ and no slip $\omega=v/r$, this becomes $mgh=(2m+M)v^2/4$, so the nonnegative speed is $v=\sqrt{4mgh/(2m+M)}$.
- id: khadley-equilibrium-q2-free-fall
  content: |-
    $\displaystyle v=\sqrt{2gh}$
  feedback: |-
    This is the result when all of $mgh$ becomes the block's translational kinetic energy. The massive flywheel also gains rotational kinetic energy, so the block must move more slowly than this free-fall value.
- id: khadley-equilibrium-q2-hoop
  content: |-
    $\displaystyle v=\sqrt{\frac{2mgh}{m+M}}$
  feedback: |-
    This follows from using $I=Mr^2$, the moment of inertia of a thin hoop. The stated flywheel is uniform and solid, so $I=Mr^2/2$ and its contribution to the effective inertia is $M/2$, not $M$.
- id: khadley-equilibrium-q2-radius-remains
  content: |-
    $\displaystyle v=\sqrt{\frac{4mgh}{2m+Mr^2}}$
  feedback: |-
    The radius cannot remain in this sum: $2m$ has units of mass while $Mr^2$ has units of mass times length squared. Substituting both $I=Mr^2/2$ and $\omega=v/r$ makes the two factors of $r$ cancel.
- id: khadley-equilibrium-q2-plus-minus
  content: |-
    $\displaystyle v=\pm\sqrt{\frac{4mgh}{2m+M}}$
  feedback: |-
    Algebraically, an equation for $v^2$ has two signed velocity roots. The question asks how fast the block moves, so $v$ denotes a nonnegative speed and only the positive root is reported.
```

---

<a id="summary"></a>
## Summary

For a block descending from rest while a cord turns a uniform solid flywheel:

1. Write $mgh=\dfrac12mv^2+\dfrac12I\omega^2$.
2. Substitute $I=\dfrac12Mr^2$ and $\omega=v/r$.
3. Simplify the rotational energy to $\dfrac14Mv^2$.
4. Collect and factor every $v^2$ term.
5. Divide by the full coefficient and take the positive root:

$$
v=\sqrt{\frac{4mgh}{2m+M}}.
$$

Check that the result has speed units and approaches $\sqrt{2gh}$ as $M\to0$. The radius cancels because $I\propto r^2$ while $\omega^2\propto 1/r^2$. The main trap is omitting either kinetic-energy term.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
