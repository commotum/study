# Comparing Translational and Rotational Kinetic Energy in Rolling

<!--
lesson-id: 212-M3-020
topic-code: MTH212.M3.20
-->

## Table of Contents

- [Introduction](#introduction)
- [Put Both Energies in Terms of Speed](#put-both-energies-in-terms-of-speed)
- [Apply the Comparison to a Uniform Hoop](#apply-the-comparison-to-a-uniform-hoop)
- [Use the Inertia Factor to Compare Other Shapes](#use-the-inertia-factor-to-compare-other-shapes)
- [Avoid the Total-Energy Trap](#avoid-the-total-energy-trap)
- [Summary](#summary)

## Prerequisites

- Translational kinetic energy: $K_{\mathrm{trans}}=\frac12 Mv^2$
- Rotational kinetic energy about the center of mass: $K_{\mathrm{rot}}=\frac12 I_{\mathrm{cm}}\omega^2$
- Rolling-without-slipping condition: $v=\omega R$
- Moments of inertia for common rigid bodies

---

<a id="introduction"></a>
## Introduction

When a rigid body rolls without slipping, it has both translational and rotational kinetic energy. The cue is the phrase **rolls without slipping**: it lets you connect the center-of-mass speed and angular speed with $v=\omega R$.

To compare the two energies, form the ratio in the fixed order

$$
\frac{K_{\mathrm{rot}}}{K_{\mathrm{trans}}},
$$

then write the moment of inertia as

$$
I_{\mathrm{cm}}=\beta MR^2,
$$

where the dimensionless factor $\beta$ describes how the mass is distributed. Then use $v=\omega R$ to express both energies with the same speed. The comparison reduces to the value of $\beta$.

---

<a id="put-both-energies-in-terms-of-speed"></a>
## Put Both Energies in Terms of Speed

**Example:** A rigid body with $I_{\mathrm{cm}}=\beta MR^2$ rolls without slipping at speed $v$. Find the ratio $K_{\mathrm{rot}}/K_{\mathrm{trans}}$.

**Explanation**

Use $\omega=v/R$ in the rotational energy:

$$
K_{\mathrm{rot}}
=\frac12(\beta MR^2)\left(\frac{v}{R}\right)^2
=\frac12\beta Mv^2.
$$

Since $K_{\mathrm{trans}}=\frac12 Mv^2$,

$$
\frac{K_{\mathrm{rot}}}{K_{\mathrm{trans}}}=\beta.
$$

Because rotational energy is in the numerator, the decision rule is

$$
\begin{aligned}
\beta<1 &\implies K_{\mathrm{rot}}<K_{\mathrm{trans}},\\
\beta=1 &\implies K_{\mathrm{rot}}=K_{\mathrm{trans}},\\
\beta>1 &\implies K_{\mathrm{rot}}>K_{\mathrm{trans}}.
\end{aligned}
$$

Keeping the ratio in this order prevents the common mistake of using the reciprocal.

```quiz
type: radio
id: p2-q1
content: |-
  A rolling body has $I_{\mathrm{cm}}=0.40MR^2$. What is $K_{\mathrm{rot}}/K_{\mathrm{trans}}$?
options:
- id: a
  content: |-
    $0.40$
  correct: true
  feedback: |-
    Correct. The ratio $K_{\mathrm{rot}}/K_{\mathrm{trans}}$ equals the inertia factor $\beta$.
- id: b
  content: |-
    $1.00$
  feedback: |-
    The energies are equal only when $\beta=1$.
- id: c
  content: |-
    $2.50$
  feedback: |-
    This is the reciprocal of the requested ratio.
- id: d
  content: |-
    $0.16$
  feedback: |-
    The factor $0.40$ is not squared again; the speed squared is already included in both energies.
```

---

<a id="apply-the-comparison-to-a-uniform-hoop"></a>
## Apply the Comparison to a Uniform Hoop

**Example:** A uniform hoop rolls without slipping. Compare its translational and rotational kinetic energies.

**Explanation**

For a uniform hoop about its center,

$$
I_{\mathrm{cm}}=MR^2,
$$

so $\beta=1$. Therefore,

$$
K_{\mathrm{rot}}
=\frac12MR^2\omega^2
=\frac12M(\omega R)^2
=\frac12Mv^2
=K_{\mathrm{trans}}.
$$

The translational and rotational kinetic energies are equal. This conclusion does not depend on the hoop's mass, radius, or speed as long as it rolls without slipping.

```quiz
type: radio
id: p2-q2
content: |-
  A uniform hoop rolls without slipping. What can be said about its kinetic energy?
options:
- id: a
  content: |-
    Its translational kinetic energy is greater than its rotational kinetic energy.
  feedback: |-
    For a hoop, $I_{\mathrm{cm}}=MR^2$, so the energy ratio is $1$, not less than $1$.
- id: b
  content: |-
    Its translational kinetic energy is less than its rotational kinetic energy.
  feedback: |-
    For a hoop, $I_{\mathrm{cm}}=MR^2$, so the energy ratio is $1$, not greater than $1$.
- id: c
  content: |-
    Its translational kinetic energy is equal to its rotational kinetic energy.
  correct: true
  feedback: |-
    Correct. Substituting $v=\omega R$ makes both energies $\frac12Mv^2$.
```

---

<a id="use-the-inertia-factor-to-compare-other-shapes"></a>
## Use the Inertia Factor to Compare Other Shapes

**Example:** A uniform solid cylinder rolls without slipping. Its moment of inertia is $I_{\mathrm{cm}}=\frac12MR^2$. Compare its rotational and translational kinetic energies.

**Explanation**

Here $\beta=\frac12$, so

$$
\frac{K_{\mathrm{rot}}}{K_{\mathrm{trans}}}=\frac12.
$$

The rotational kinetic energy is half the translational kinetic energy. The same method works for any rolling body once its moment of inertia is written as a multiple of $MR^2$.

```quiz
type: radio
id: p2-q3
content: |-
  A uniform solid sphere rolls without slipping. Since $I_{\mathrm{cm}}=\frac25MR^2$, which comparison is correct?
options:
- id: a
  content: |-
    $K_{\mathrm{rot}}=\frac25K_{\mathrm{trans}}$
  correct: true
  feedback: |-
    Correct. The energy ratio equals the coefficient of $MR^2$ in the moment of inertia.
- id: b
  content: |-
    $K_{\mathrm{rot}}=K_{\mathrm{trans}}$
  feedback: |-
    Equality is the hoop case, for which the inertia factor is $1$.
- id: c
  content: |-
    $K_{\mathrm{rot}}=\frac52K_{\mathrm{trans}}$
  feedback: |-
    This reverses the requested ratio.
- id: d
  content: |-
    $K_{\mathrm{rot}}=\frac45K_{\mathrm{trans}}$
  feedback: |-
    The factor $\frac25$ is not doubled when comparing the two energy formulas.
```

---

<a id="avoid-the-total-energy-trap"></a>
## Avoid the Total-Energy Trap

**Example:** A uniform hoop rolls without slipping with $K_{\mathrm{trans}}=12\ \mathrm{J}$. Find its rotational kinetic energy and its total kinetic energy.

**Explanation**

For a hoop, $K_{\mathrm{rot}}=K_{\mathrm{trans}}$, so

$$
K_{\mathrm{rot}}=12\ \mathrm{J}.
$$

The total kinetic energy is the sum of the two parts:

$$
K_{\mathrm{total}}
=K_{\mathrm{trans}}+K_{\mathrm{rot}}
=24\ \mathrm{J}.
$$

Equal translational and rotational energies do not mean that either one equals the total energy. Each is half of the total for a rolling hoop.

```quiz
type: radio
id: p2-q4
content: |-
  A uniform hoop rolls without slipping with total kinetic energy $30\ \mathrm{J}$. What is its rotational kinetic energy?
options:
- id: a
  content: |-
    $15\ \mathrm{J}$
  correct: true
  feedback: |-
    Correct. The two equal parts split the $30\ \mathrm{J}$ total in half.
- id: b
  content: |-
    $30\ \mathrm{J}$
  feedback: |-
    This treats one energy part as the total of both parts.
- id: c
  content: |-
    $60\ \mathrm{J}$
  feedback: |-
    This doubles the total instead of splitting it into two equal parts.
- id: d
  content: |-
    The answer depends on the hoop's radius.
  feedback: |-
    The radius cancels when $I=MR^2$ and $v=\omega R$ are combined.
```

---

## Summary

When an object **rolls without slipping**:

1. Write $I_{\mathrm{cm}}=\beta MR^2$.
2. Substitute $\omega=v/R$ into $K_{\mathrm{rot}}=\frac12I_{\mathrm{cm}}\omega^2$.
3. Form the ratio in the order $K_{\mathrm{rot}}/K_{\mathrm{trans}}=\beta$.
4. Compare $\beta$ with $1$.

For a uniform hoop, $\beta=1$, so $K_{\mathrm{rot}}=K_{\mathrm{trans}}$. The main trap is confusing either equal part with the total: for the hoop, each part is one-half of $K_{\mathrm{total}}$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Finding Angular Speed After a Bullet Embeds in a Rotor](../../../M2/2026-07-14-M2-5/Lessons/Problem-5.md)

Study guide index: 10/20

---

<!-- lesson-nav:end -->
