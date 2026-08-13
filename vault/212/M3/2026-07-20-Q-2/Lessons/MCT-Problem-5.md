# Rank Rotational Inertia from Mass Distribution

<!--
lesson-id: 212-M3-041
topic-code: MTH212.M3.41
-->

## Table of Contents

- [Introduction](#introduction)
- [Compare Equal-Mass Equal-Radius Shapes](#compare-equal-mass-equal-radius-shapes)
- [Track Squared Distance from the Axis](#track-squared-distance-from-the-axis)
- [Tie Each Shape Factor to Its Axis](#tie-each-shape-factor-to-its-axis)
- [Change the Axis Without Changing the Object](#change-the-axis-without-changing-the-object)
- [Check the Ranking Through Angular Response and Energy](#check-the-ranking-through-angular-response-and-energy)
- [Summary](#summary)

## Prerequisites

- Identify a rotation axis and a perpendicular distance to that axis.
- Evaluate squares and compare simple fractions.
- Use $\tau=r_\perp F$ for a tangential force.
- Interpret $\sum\tau=I\alpha$ when the net torque is known.

---

<a id="introduction"></a>
## Introduction

Two objects can have the same mass and outer radius but respond differently to the same torque. The deciding quantity is the **moment of inertia about the stated axis**:

$$
I=\sum_i m_i r_{\perp,i}^2
\qquad\text{or}\qquad
I=\int r_\perp^2\,dm.
$$

Mass farther from the axis counts more because its perpendicular distance is squared. Use this ranking procedure:

1. Mark the rotation axis before choosing a formula.
2. Record what is held fixed and what changes: mass, dimensions, shape, axis, and applied torque.
3. Compare the $r_\perp^2$ distribution directly, or use a formula that names the correct object and axis.
4. Rank $I$ first.
5. Only then translate the ranking: under the same net torque, larger $I$ means smaller $\alpha$.

The comparison condition controls what happens after the $I$ ranking:

| Condition held fixed | Relation | Effect of larger $I$ |
| --- | --- | --- |
| Net torque $\sum\tau$ | $\alpha=(\sum\tau)/I$ | Smaller angular acceleration |
| Angular speed $\omega$ | $K_{\mathrm{rot}}=\frac12I\omega^2$ | More rotational kinetic energy |
| Neither condition stated | None yet | Rank $I$ only |

Moment of inertia has units

$$
[I]=\mathrm{kg\,m^2}.
$$

It is not a torque and it is not an energy.

**Source-video analogy: Same force, different translational mass.** A $50\,\mathrm N$ force gives a $10\,\mathrm{kg}$ object an acceleration of $5\,\mathrm{m/s^2}$ and a $100\,\mathrm{kg}$ object an acceleration of $0.5\,\mathrm{m/s^2}$. This only sets up the response pattern: more inertia gives less acceleration under the same input. In translation, mass measures inertia; in rotation, both mass distribution and the chosen axis matter.

---

<a id="compare-equal-mass-equal-radius-shapes"></a>
## Compare Equal-Mass Equal-Radius Shapes

**Source-video Problem 1: Thin hoop versus solid disk.** Both objects have mass $M=10\,\mathrm{kg}$ and radius $R=2\,\mathrm m$. Each rotates about its central symmetry axis, perpendicular to its circular face. A tangential $100\,\mathrm N$ force acts at the rim of each object.

**Explanation**

For these axes,

$$
I_{\mathrm{hoop}}=MR^2,
\qquad
I_{\mathrm{disk}}=\frac12MR^2.
$$

Substitution gives

$$
\begin{aligned}
I_{\mathrm{hoop}}&=(10\,\mathrm{kg})(2\,\mathrm m)^2
=40\,\mathrm{kg\,m^2},\\
I_{\mathrm{disk}}&=\frac12(10\,\mathrm{kg})(2\,\mathrm m)^2
=20\,\mathrm{kg\,m^2}.
\end{aligned}
$$

The force and radius are also equal, so both torques have magnitude

$$
\tau=FR=(100\,\mathrm N)(2\,\mathrm m)=200\,\mathrm{N\,m}.
$$

Therefore,

$$
\alpha_{\mathrm{hoop}}=\frac{200}{40}=5\,\mathrm{rad/s^2},
\qquad
\alpha_{\mathrm{disk}}=\frac{200}{20}=10\,\mathrm{rad/s^2}.
$$

The hoop has the larger $I$ because all its mass lies at the outer radius. The disk has mass at every radius from $0$ to $R$, so the same torque gives the disk the larger angular acceleration.

```quiz
type: radio
id: mct-q2-p5-hoop-disk
shuffle: true
content: |-
  A thin hoop and a uniform solid disk each have mass $8\,\mathrm{kg}$ and radius $0.50\,\mathrm m$. Both rotate about their central symmetry axes and receive the same net torque. Which statement is correct?
options:
- id: mct-q2-p5-hoop-disk-a
  content: |-
    $I_{\mathrm{hoop}}=2.0\,\mathrm{kg\,m^2}$, $I_{\mathrm{disk}}=1.0\,\mathrm{kg\,m^2}$, and $\alpha_{\mathrm{hoop}}=\frac12\alpha_{\mathrm{disk}}$.
  correct: true
  feedback: |-
    For the stated axes, $I_{\mathrm{hoop}}=MR^2=2.0\,\mathrm{kg\,m^2}$ and $I_{\mathrm{disk}}=\frac12MR^2=1.0\,\mathrm{kg\,m^2}$. Equal torque means $\alpha=\tau/I$, so the hoop's angular acceleration is half the disk's.
- id: mct-q2-p5-hoop-disk-b
  content: |-
    The two moments of inertia and angular accelerations are equal because $M$ and $R$ match.
  feedback: |-
    Equal mass and outer radius do not fix rotational inertia; the distribution inside that radius also matters. The hoop's coefficient is $1$, while the solid disk's is $1/2$.
- id: mct-q2-p5-hoop-disk-c
  content: |-
    $I_{\mathrm{hoop}}=1.0\,\mathrm{kg\,m^2}$, $I_{\mathrm{disk}}=2.0\,\mathrm{kg\,m^2}$, and $\alpha_{\mathrm{hoop}}=2\alpha_{\mathrm{disk}}$.
  feedback: |-
    This assigns the shape factors to the wrong objects. The hoop keeps all mass at $R$ and has $I=MR^2$; the disk has $I=\frac12MR^2$.
- id: mct-q2-p5-hoop-disk-d
  content: |-
    $I_{\mathrm{hoop}}=2.0\,\mathrm{kg\,m^2}$, $I_{\mathrm{disk}}=1.0\,\mathrm{kg\,m^2}$, and $\alpha_{\mathrm{hoop}}=2\alpha_{\mathrm{disk}}$.
  feedback: |-
    The inertia values are right, but the response is reversed. With the same torque, angular acceleration is inversely proportional to $I$, so the larger-inertia hoop accelerates less.
- id: mct-q2-p5-hoop-disk-e
  content: |-
    $I_{\mathrm{hoop}}=4.0\,\mathrm{kg\,m^2}$ and $I_{\mathrm{disk}}=2.0\,\mathrm{kg\,m^2}$ because the radius is doubled before squaring.
  feedback: |-
    The given radius is already $0.50\,\mathrm m$; it is not a diameter that must be doubled. Squaring $0.50\,\mathrm m$ gives $0.25\,\mathrm{m^2}$.
```

---

<a id="track-squared-distance-from-the-axis"></a>
## Track Squared Distance from the Axis

**Source-video particle model:** For discrete masses,

$$
I=\sum_i m_i r_{\perp,i}^2.
$$

Each $r_{\perp,i}$ is the shortest distance from the specified axis, not necessarily the distance from an object's geometric center.

Suppose two $1.5\,\mathrm{kg}$ point masses are each $0.20\,\mathrm m$ from an axis. Their total moment of inertia is

$$
I_A=2(1.5\,\mathrm{kg})(0.20\,\mathrm m)^2
=0.12\,\mathrm{kg\,m^2}.
$$

Move both masses to $0.40\,\mathrm m$ without changing their masses:

$$
I_B=2(1.5\,\mathrm{kg})(0.40\,\mathrm m)^2
=0.48\,\mathrm{kg\,m^2}.
$$

Doubling every distance multiplies $I$ by $2^2=4$.

**Source correction: Scope of the $MR^2$ argument.** For a point mass, use the tangential relations $F_t=ma_t$, $a_t=\alpha r_\perp$, and $\tau=r_\perp F_t$ to obtain $\tau=(mr_\perp^2)\alpha$. Summing those point-mass contributions gives $I=\sum m_i r_{\perp,i}^2$. This does not derive the coefficients $1/2$ for a disk or $2/5$ for a solid sphere; those come from summing or integrating each shape's actual mass distribution.

```quiz
type: radio
id: mct-q2-p5-radius-squared
shuffle: true
content: |-
  A $2.0\,\mathrm{kg}$ point mass is moved from $0.30\,\mathrm m$ to $0.90\,\mathrm m$ from a fixed axis. By what factor does its contribution to the moment of inertia change?
options:
- id: mct-q2-p5-radius-squared-a
  content: |-
    It increases by a factor of $9$.
  correct: true
  feedback: |-
    A point mass contributes $mr^2$. The distance triples, so the contribution changes by $(0.90/0.30)^2=3^2=9$.
- id: mct-q2-p5-radius-squared-b
  content: |-
    It increases by a factor of $3$.
  feedback: |-
    A factor of $3$ would follow linear distance weighting. Moment of inertia weights distance by $r^2$, so tripling $r$ multiplies the contribution by $9$.
- id: mct-q2-p5-radius-squared-c
  content: |-
    It increases by a factor of $6$.
  feedback: |-
    Multiplying the mass ratio by the distance ratio is not the comparison here because the mass does not change. Only the squared distance ratio remains, giving $9$.
- id: mct-q2-p5-radius-squared-d
  content: |-
    It increases by a factor of $81$.
  feedback: |-
    This squares the distance effect twice. The formula contains one $r^2$, so use $3^2=9$, not $(3^2)^2$.
- id: mct-q2-p5-radius-squared-e
  content: |-
    It does not change because the mass is unchanged.
  feedback: |-
    Mass is only one part of rotational inertia. Moving the same mass farther from the fixed axis changes its $mr^2$ contribution.
```

---

<a id="tie-each-shape-factor-to-its-axis"></a>
## Tie Each Shape Factor to Its Axis

**Source-video factor comparison:** The source writes common rotational inertias as

$$
I=cMR^2.
$$

The coefficient $c$ records the mass distribution for a particular object and axis:

| Object | Rotation axis | $c$ | Moment of inertia |
| --- | --- | ---: | --- |
| Thin hoop | Symmetry axis through the center, perpendicular to its plane | $1$ | $MR^2$ |
| Uniform solid disk | Symmetry axis through the center, perpendicular to its plane | $\frac12$ | $\frac12MR^2$ |
| Uniform solid sphere | A diameter through the center | $\frac25$ | $\frac25MR^2$ |

When two objects have the same $M$ and $R$, those common factors cancel in a ratio:

$$
\frac{I_1}{I_2}
=\frac{c_1MR^2}{c_2MR^2}
=\frac{c_1}{c_2}.
$$

That cancellation is what makes a coefficient-only ranking valid here.

For equal $M$ and equal $R$ about those axes,

$$
1>\frac12>\frac25,
$$

so

$$
I_{\mathrm{hoop}}>I_{\mathrm{disk}}>I_{\mathrm{sphere}}.
$$

The disk's moment of inertia is not “one half” by itself; $1/2$ is the dimensionless coefficient multiplying $MR^2$. If masses, radii, or axes differ, the $MR^2$ factors do not cancel; compare the complete formulas rather than the coefficients alone.

```quiz
type: radio
id: mct-q2-p5-shape-factor-rank
shuffle: true
content: |-
  A thin hoop, a uniform solid disk, and a uniform solid sphere have the same mass $M$ and radius $R$. Each rotates about the center axis named in the table above. Which ranking of moments of inertia is correct?
options:
- id: mct-q2-p5-shape-factor-rank-a
  content: |-
    $I_{\mathrm{hoop}}>I_{\mathrm{disk}}>I_{\mathrm{sphere}}$
  correct: true
  feedback: |-
    With $M$ and $R$ fixed, compare the shape factors: $1>1/2>2/5$. Therefore the hoop has the greatest $I$, followed by the disk and then the solid sphere.
- id: mct-q2-p5-shape-factor-rank-b
  content: |-
    $I_{\mathrm{hoop}}>I_{\mathrm{sphere}}>I_{\mathrm{disk}}$
  feedback: |-
    This reverses $1/2$ and $2/5$. Since $1/2=0.5$ and $2/5=0.4$, the disk's coefficient is larger than the solid sphere's.
- id: mct-q2-p5-shape-factor-rank-c
  content: |-
    $I_{\mathrm{sphere}}>I_{\mathrm{disk}}>I_{\mathrm{hoop}}$
  feedback: |-
    This reverses the full coefficient order. The hoop places its mass farthest from the axis and has coefficient $1$, the largest of the three.
- id: mct-q2-p5-shape-factor-rank-d
  content: |-
    $I_{\mathrm{hoop}}=I_{\mathrm{disk}}=I_{\mathrm{sphere}}$
  feedback: |-
    Equal mass and outer radius do not erase differences in mass distribution. The three axis-specific coefficients are different.
- id: mct-q2-p5-shape-factor-rank-e
  content: |-
    $I_{\mathrm{disk}}>I_{\mathrm{hoop}}>I_{\mathrm{sphere}}$
  feedback: |-
    A disk has some mass close to the axis, while a thin hoop keeps all its mass at $R$. That makes the hoop's coefficient $1$ larger than the disk's $1/2$.
```

---

<a id="change-the-axis-without-changing-the-object"></a>
## Change the Axis Without Changing the Object

**M2-2 lecture transfer: Uniform thin rod.** The rod has the same mass $M$ and length $L$ in both cases, but the axis changes. Both axes are perpendicular to the rod:

$$
I_{\mathrm{cm}}=\frac{1}{12}ML^2,
\qquad
I_{\mathrm{end}}=\frac13ML^2.
$$

Therefore,

$$
I_{\mathrm{end}}
=4I_{\mathrm{cm}}.
$$

About the center, half of the rod lies on each side and much of its mass is close to the axis. About an end, every mass element lies on the same side and more of the rod is far away. Moment of inertia belongs to an **object-axis pair**, not to the object alone.

```quiz
type: radio
id: mct-q2-p5-rod-axis
shuffle: true
content: |-
  The same uniform thin rod is rotated first about a perpendicular axis through its center and then about a parallel axis through one end. The same net torque is applied in both cases. How do the angular accelerations compare?
options:
- id: mct-q2-p5-rod-axis-a
  content: |-
    $\alpha_{\mathrm{end}}=\frac14\alpha_{\mathrm{cm}}$
  correct: true
  feedback: |-
    The end-axis inertia is four times the center-axis inertia. Since equal torque gives $\alpha=\tau/I$, the end-axis angular acceleration is one fourth as large.
- id: mct-q2-p5-rod-axis-b
  content: |-
    $\alpha_{\mathrm{end}}=4\alpha_{\mathrm{cm}}$
  feedback: |-
    This makes angular acceleration proportional to inertia. Under equal torque the relationship is inverse, so four times the inertia gives one fourth the angular acceleration.
- id: mct-q2-p5-rod-axis-c
  content: |-
    $\alpha_{\mathrm{end}}=\alpha_{\mathrm{cm}}$
  feedback: |-
    The rod is unchanged, but its distances from the rotation axis are not. The end-axis moment of inertia is four times larger, so the accelerations cannot be equal under the same torque.
- id: mct-q2-p5-rod-axis-d
  content: |-
    $\alpha_{\mathrm{end}}=\frac12\alpha_{\mathrm{cm}}$
  feedback: |-
    Moving the axis from the center to the end changes the rod's moment of inertia by a factor of $4$, not $2$. Apply that full factor inversely to $\alpha$.
- id: mct-q2-p5-rod-axis-e
  content: |-
    The comparison cannot be made because the rod's mass and length are unchanged.
  feedback: |-
    The axis is part of the moment-of-inertia specification. The known formulas give $I_{\mathrm{end}}=4I_{\mathrm{cm}}$, which is enough to rank the angular accelerations.
```

---

<a id="check-the-ranking-through-angular-response-and-energy"></a>
## Check the Ranking Through Angular Response and Energy

**Source-video dynamics connection:** Newton's second law for rotation is

$$
\sum\tau=I\alpha.
$$

For equal net torque,

$$
\alpha=\frac{\sum\tau}{I},
$$

so the larger-$I$ object has the smaller angular acceleration.

**M2-2 lecture cross-check:** In rigid rotation, each mass element has $v_i=\omega r_{\perp,i}$. The lecture therefore obtains

$$
K_{\mathrm{rot}}
=\sum_i\frac12m_i(\omega r_{\perp,i})^2
=\frac12I\omega^2.
$$

At equal angular speed, the larger-$I$ object has more rotational kinetic energy. Moment of inertia remains a property of the object-axis pair; torque and rotational kinetic energy use it in different equations.

For example, if $I_A=3I_B$, then

$$
\alpha_A=\frac13\alpha_B
\quad\text{under equal torque},
\qquad
K_A=3K_B
\quad\text{at equal }\omega.
$$

```quiz
type: radio
id: mct-q2-p5-response-energy
shuffle: true
content: |-
  Two rigid objects rotate about specified axes with $I_P=2.5I_Q$. Compare them first under the same net torque and then at the same angular speed. Which statement is correct?
options:
- id: mct-q2-p5-response-energy-a
  content: |-
    $\alpha_P=0.4\alpha_Q$ under equal torque, and $K_P=2.5K_Q$ at equal angular speed.
  correct: true
  feedback: |-
    Equal torque makes angular acceleration inverse in $I$, so $\alpha_P=\alpha_Q/2.5=0.4\alpha_Q$. Equal angular speed makes $K_{\mathrm{rot}}$ proportional to $I$, so $K_P=2.5K_Q$.
- id: mct-q2-p5-response-energy-b
  content: |-
    $\alpha_P=2.5\alpha_Q$ under equal torque, and $K_P=2.5K_Q$ at equal angular speed.
  feedback: |-
    The energy comparison is correct, but the angular-response comparison is reversed. With torque fixed, $\alpha=\tau/I$, so the larger-inertia object accelerates less.
- id: mct-q2-p5-response-energy-c
  content: |-
    $\alpha_P=0.4\alpha_Q$ under equal torque, and $K_P=0.4K_Q$ at equal angular speed.
  feedback: |-
    Angular acceleration is inverse in $I$ at fixed torque, but rotational kinetic energy is direct in $I$ at fixed $\omega$. The two comparisons use opposite proportionalities.
- id: mct-q2-p5-response-energy-d
  content: |-
    $\alpha_P=\alpha_Q$ and $K_P=K_Q$ because the applied torque and angular speed are matched.
  feedback: |-
    Matching the comparison input exposes the effect of different inertias; it does not remove it. Different $I$ values produce different $\alpha$ at equal torque and different $K$ at equal $\omega$.
- id: mct-q2-p5-response-energy-e
  content: |-
    $\alpha_P=2.5\alpha_Q$ under equal torque, and $K_P=0.4K_Q$ at equal angular speed.
  feedback: |-
    This reverses both governing relationships. Equal torque gives $\alpha\propto1/I$, whereas equal angular speed gives $K_{\mathrm{rot}}\propto I$.
```

---

<a id="summary"></a>
## Summary

To rank rotational inertia:

1. Name the object and rotation axis.
2. Hold the stated mass, dimensions, and comparison conditions fixed.
3. Compare $\sum m_i r_{\perp,i}^2$, or use the correct axis-specific shape factor in $I=cMR^2$.
4. Rank $I$ before discussing the response.
5. Under equal torque, reverse the $I$ ranking to rank $\alpha$ because $\alpha=\tau/I$.

Moving mass outward increases $I$ through the squared distance. Changing the axis can change $I$ even when the object does not change. At equal angular speed, $K_{\mathrm{rot}}=\frac12I\omega^2$ gives the same ranking as $I$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
