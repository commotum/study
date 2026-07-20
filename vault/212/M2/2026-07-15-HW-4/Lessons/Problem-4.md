# Total Kinetic Energy From a Loss of Height

## Table of Contents

- [Introduction](#introduction)
- [Match the Energy at the Two Endpoints](#match-the-energy-at-the-two-endpoints)
- [Treat Total Kinetic Energy as One Quantity](#treat-total-kinetic-energy-as-one-quantity)
- [Substitute the Mass Named in the Question](#substitute-the-mass-named-in-the-question)
- [Ignore Details That Do Not Affect the Energy Change](#ignore-details-that-do-not-affect-the-energy-change)
- [Summary](#summary)

## Prerequisites

- Gravitational potential energy near Earth's surface: $U_g=mgy$
- Conservation of mechanical energy when dissipative losses are negligible
- Translational and rotational kinetic energy are both parts of total kinetic energy

---

<a id="introduction"></a>
## Introduction

When an object starts from rest at height $h$, rolls without slipping, and reaches the bottom without losing mechanical energy, look first at the two endpoints. The decrease in gravitational potential energy becomes the object's **total** kinetic energy:

$$
K_{\text{total,bottom}}=mgh.
$$

Here $m$ is the mass of the particular object named in the question. The ramp angle, radius, and division between translational and rotational kinetic energy can affect other quantities, but they do not change this total.

Use this endpoint check:

1. **Starts from rest:** $K_i=0$.
2. **Drops a vertical height $h$:** the lost potential energy is $mgh$.
3. **Asks for total kinetic energy:** set $K_{\text{total},f}=mgh$ before substituting the object's mass.

---

<a id="match-the-energy-at-the-two-endpoints"></a>
## Match the Energy at the Two Endpoints

**Example:** A cylinder of mass $m$ starts from rest a vertical height $H$ above the bottom of a ramp. It rolls without slipping, and no mechanical energy is lost. Find its total kinetic energy at the bottom.

**Explanation**

Choose the bottom as the zero of gravitational potential energy. Then

$$
K_i=0, \qquad U_i=mgH, \qquad U_f=0.
$$

Conservation of mechanical energy gives

$$
K_i+U_i=K_f+U_f,
$$

so

$$
K_{\text{total},f}=mgH.
$$

```quiz
type: radio
id: p4-q1
content: |-
  A sphere of mass $2m$ starts from rest at height $H$ and rolls without slipping to the bottom with no energy loss. What is its total kinetic energy at the bottom?
options:
- id: p4-q1-a
  content: |-
    $m g H$
- id: p4-q1-b
  content: |-
    $2m g H$
  correct: true
- id: p4-q1-c
  content: |-
    $2m g H\sin\theta$
- id: p4-q1-d
  content: |-
    $4m g H$
```

---

<a id="treat-total-kinetic-energy-as-one-quantity"></a>
## Treat Total Kinetic Energy as One Quantity

**Example:** A uniform solid cylinder of mass $m$ rolls at speed $v$. Show how its kinetic energy is divided between translation and rotation.

**Explanation**

For a uniform solid cylinder, $I=\frac12mr^2$, and rolling without slipping gives $\omega=v/r$. Therefore,

$$
\begin{aligned}
K_{\text{total}}
&=K_{\text{trans}}+K_{\text{rot}} \\
&=\frac12mv^2+\frac12I\omega^2 \\
&=\frac12mv^2+\frac12\left(\frac12mr^2\right)\left(\frac{v}{r}\right)^2 \\
&=\frac34mv^2.
\end{aligned}
$$

The radius cancels. More importantly, if the question asks only for **total** kinetic energy after a loss of height, conservation of energy finds that total directly. There is no need to calculate $v$, $\omega$, or each share separately.

```quiz
type: radio
id: p4-q2
content: |-
  A rolling object has $12\,\mathrm{J}$ of translational kinetic energy and $4\,\mathrm{J}$ of rotational kinetic energy. What is its total kinetic energy?
options:
- id: p4-q2-a
  content: |-
    $8\,\mathrm{J}$
- id: p4-q2-b
  content: |-
    $12\,\mathrm{J}$
- id: p4-q2-c
  content: |-
    $16\,\mathrm{J}$
  correct: true
- id: p4-q2-d
  content: |-
    $48\,\mathrm{J}$
```

---

<a id="substitute-the-mass-named-in-the-question"></a>
## Substitute the Mass Named in the Question

**Example:** Two cylinders have masses $M$ and $4M$. Both start from rest at the same height $h$ and roll without slipping to the bottom. Find the total kinetic energy of the heavier cylinder at the bottom.

**Explanation**

Use the mass of the requested cylinder in $K_{\text{total}}=mgh$. For the heavier cylinder,

$$
m_{\text{object}}=4M.
$$

Thus,

$$
K_{\text{total,bottom}}=(4M)gh=4Mgh.
$$

The symbol $M$ is a reference mass, not the mass of this cylinder. Missing the factor of $4$ would give the energy of the other cylinder.

```quiz
type: radio
id: p4-q3
content: |-
  An object of mass $3m$ starts from rest at height $2H$ and reaches the bottom without losing mechanical energy. What is its total kinetic energy at the bottom?
options:
- id: p4-q3-a
  content: |-
    $2mgH$
- id: p4-q3-b
  content: |-
    $3mgH$
- id: p4-q3-c
  content: |-
    $5mgH$
- id: p4-q3-d
  content: |-
    $6mgH$
  correct: true
```

---

<a id="ignore-details-that-do-not-affect-the-energy-change"></a>
## Ignore Details That Do Not Affect the Energy Change

**Example:** A uniform cylinder of mass $m$ and radius $r$ rolls from rest down a ramp of vertical height $h$ and angle $\theta$. Which supplied quantities are needed to determine its total kinetic energy at the bottom?

**Explanation**

Only $m$, $g$, and the **vertical** height change $h$ appear in

$$
K_{\text{total,bottom}}=mgh.
$$

The angle $\theta$ changes the ramp length and travel time. The radius $r$ appears while splitting the energy into translation and rotation, but it cancels for rolling without slipping. Neither belongs in the final total-energy expression. A useful unit check confirms the form:

$$
[mgh]=\mathrm{kg}\left(\frac{\mathrm{m}}{\mathrm{s}^2}\right)(\mathrm{m})
=\mathrm{kg}\,\mathrm{m}^2/\mathrm{s}^2
=\mathrm{J}.
$$

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  Two uniform solid cylinders are released simultaneously from rest at the top of a ramp of height $h$ inclined at angle $\theta$. One cylinder has mass $M$ and radius $R$; the other has mass $4M$ and radius $R/2$. Both roll without slipping.

  What is the total kinetic energy of the cylinder with mass $4M$ and radius $R/2$ when it reaches the bottom?
options:
- id: a
  content: |-
    $\dfrac{Mgh}{\sin\theta}$
- id: b
  content: |-
    $4MgR\cos\theta$
- id: c
  content: |-
    $4Mgh$
  correct: true
- id: d
  content: |-
    $2MgR\sin\theta$
```

---

<a id="summary"></a>
## Summary

When an object starts from rest at height $h$ and reaches the bottom without mechanical-energy loss:

1. Write the endpoint balance $K_i+U_i=K_f+U_f$.
2. Use $K_i=0$, $U_i=mgh$, and $U_f=0$.
3. Conclude that $K_{\text{total},f}=mgh$.
4. Substitute the mass of the object actually requested.
5. Do not insert the ramp angle or radius when the question asks only for total kinetic energy.

For the cylinder of mass $4M$, the result is

$$
\boxed{4Mgh}.
$$
