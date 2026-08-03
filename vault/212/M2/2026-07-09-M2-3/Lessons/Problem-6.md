# Finding an Unknown Mass in Rigidly Attached Cylinders

<!--
lesson-id: 212-M2-016
topic-code: MTH212.M2.16
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert the Applied Force to Total Inertia](#convert-the-applied-force-to-total-inertia)
- [Separate the Known and Unknown Inertias](#separate-the-known-and-unknown-inertias)
- [Avoid the Radius-Squared and One-Half Traps](#avoid-the-radius-squared-and-one-half-traps)
- [Apply the Inertia Budget to the Two Cylinders](#apply-the-inertia-budget-to-the-two-cylinders)
- [Summary](#summary)

## Prerequisites

- Use $\tau=I\alpha$ for rotational dynamics.
- Use $I=\tfrac12MR^2$ for a solid cylinder about its symmetry axis.
- Solve a linear equation for one unknown.

---

<a id="introduction"></a>
## Introduction

When rigid coaxial objects rotate together, they have the same angular acceleration and behave as one rotating system. Their moments of inertia add:

$$
I_{\text{total}}=I_1+I_2.
$$

For two solid cylinders with masses $M$ and $m$ and radii $R$ and $r$,

$$
I_{\text{total}}=\frac12MR^2+\frac12mr^2.
$$

**Recognition cue:** If a tangential force drives rigidly attached cylinders and the question asks for one cylinder's mass, use the applied torque to find the total inertia, subtract the known cylinder's inertia, and convert the remaining inertia into the unknown mass.

Let $m$ denote the requested mass. The entire situation becomes one linear equation in $m$:

$$
FR=\left(\frac12MR^2+\frac12mr^2\right)\alpha.
$$

Here, $M$ and $R$ belong to the known cylinder, while $m$ and $r$ belong to the unknown cylinder. Keeping those uppercase and lowercase pairs together prevents a radius swap.

---

<a id="convert-the-applied-force-to-total-inertia"></a>
## Convert the Applied Force to Total Inertia

**Example:** A tangential $3.0\ \mathrm{N}$ force acts at a radius of $0.40\ \mathrm{m}$ and produces an angular acceleration of $2.0\ \mathrm{rad/s^2}$. Find the total moment of inertia.

**Explanation**

Because the force is tangential, it is perpendicular to the radius. Therefore,

$$
\tau=FR=(3.0\ \mathrm{N})(0.40\ \mathrm{m})=1.2\ \mathrm{N\,m}.
$$

Apply $\tau=I_{\text{total}}\alpha$ to the entire rigid system:

$$
I_{\text{total}}
=\frac{\tau}{\alpha}
=\frac{1.2\ \mathrm{N\,m}}{2.0\ \mathrm{rad/s^2}}
=0.60\ \mathrm{kg\,m^2}.
$$

```quiz
type: radio
id: p6-total-inertia
content: |-
  A tangential $4.0\ \mathrm{N}$ force acts at a radius of $0.30\ \mathrm{m}$ and produces an angular acceleration of $1.5\ \mathrm{rad/s^2}$. What is the system's total moment of inertia?
options:
- id: p6-total-inertia-a
  content: |-
    $0.54\ \mathrm{kg\,m^2}$
- id: p6-total-inertia-b
  content: |-
    $0.80\ \mathrm{kg\,m^2}$
  correct: true
- id: p6-total-inertia-c
  content: |-
    $1.2\ \mathrm{kg\,m^2}$
- id: p6-total-inertia-d
  content: |-
    $1.8\ \mathrm{kg\,m^2}$
```

---

<a id="separate-the-known-and-unknown-inertias"></a>
## Separate the Known and Unknown Inertias

Before substituting numbers, isolate the unknown mass in the system equation. Divide by $\alpha$, subtract the known inertia, multiply by $2$, and divide by $r^2$:

$$
\begin{aligned}
\frac{FR}{\alpha}
&=\frac12MR^2+\frac12mr^2,\\
\frac{FR}{\alpha}-\frac12MR^2
&=\frac12mr^2,\\
m
&=\frac{2}{r^2}\left(\frac{FR}{\alpha}-\frac12MR^2\right).
\end{aligned}
$$

This symbolic form is the inertia-budget procedure in one line: total inertia minus known inertia, then convert the remainder to mass.

**Example:** Two solid cylinders are rigidly attached. Their total moment of inertia is $1.40\ \mathrm{kg\,m^2}$. The known cylinder has mass $4.0\ \mathrm{kg}$ and radius $0.60\ \mathrm{m}$. The unknown cylinder has radius $0.40\ \mathrm{m}$. Find its mass $m$.

**Explanation**

First find the known cylinder's inertia:

$$
I_{\text{known}}
=\frac12(4.0\ \mathrm{kg})(0.60\ \mathrm{m})^2
=0.72\ \mathrm{kg\,m^2}.
$$

The smaller cylinder must supply the remaining inertia:

$$
I_{\text{unknown}}
=1.40-0.72
=0.68\ \mathrm{kg\,m^2}.
$$

Now solve $I_{\text{unknown}}=\tfrac12mr^2$:

$$
m
=\frac{2I_{\text{unknown}}}{r^2}
=\frac{2(0.68)}{(0.40)^2}
=8.5\ \mathrm{kg}.
$$

```quiz
type: radio
id: p6-inertia-remainder
content: |-
  A rigid two-cylinder system has $I_{\text{total}}=0.90\ \mathrm{kg\,m^2}$. The known cylinder contributes $0.50\ \mathrm{kg\,m^2}$. The unknown solid cylinder has radius $0.50\ \mathrm{m}$. What is its mass?
options:
- id: p6-inertia-remainder-a
  content: |-
    $0.80\ \mathrm{kg}$
- id: p6-inertia-remainder-b
  content: |-
    $1.6\ \mathrm{kg}$
- id: p6-inertia-remainder-c
  content: |-
    $3.2\ \mathrm{kg}$
  correct: true
- id: p6-inertia-remainder-d
  content: |-
    $7.2\ \mathrm{kg}$
```

---

<a id="avoid-the-radius-squared-and-one-half-traps"></a>
## Avoid the Radius-Squared and One-Half Traps

**Example:** A student writes $I=MR$ for a solid cylinder. Identify both missing features.

**Explanation**

For a solid cylinder about its central axis,

$$
I=\frac12MR^2.
$$

The factor $\tfrac12$ depends on the object's shape, and the radius must be squared. These details also make the units work:

$$
[I]=\mathrm{kg\,m^2}.
$$

The rearranged mass formula must then return kilograms:

$$
[m]=\frac{[I]}{[r^2]}
=\frac{\mathrm{kg\,m^2}}{\mathrm{m^2}}
=\mathrm{kg}.
$$

After subtracting the known inertia from the total, the remaining inertia should be nonnegative. A negative remainder signals an incorrect model, formula, or substitution.

```quiz
type: radio
id: p6-cylinder-formula
content: |-
  Which expression gives the mass of a solid cylinder with moment of inertia $I$ and radius $r$?
options:
- id: p6-cylinder-formula-a
  content: |-
    $m=\dfrac{I}{2r^2}$
- id: p6-cylinder-formula-b
  content: |-
    $m=\dfrac{2I}{r^2}$
  correct: true
- id: p6-cylinder-formula-c
  content: |-
    $m=\dfrac{2I}{r}$
- id: p6-cylinder-formula-d
  content: |-
    $m=2Ir^2$
```

---

<a id="apply-the-inertia-budget-to-the-two-cylinders"></a>
## Apply the Inertia Budget to the Two Cylinders

**Source problem**

A tangential $1.4\ \mathrm{N}$ force acts at the rim of a $2.3\ \mathrm{kg}$ solid cylinder of radius $0.85\ \mathrm{m}$. A second coaxial solid cylinder of radius $0.36\ \mathrm{m}$ is rigidly attached. The system's angular acceleration is $1.2\ \mathrm{rad/s^2}$. Find the mass of the smaller cylinder.

![](<../Source/Images/coaxial-solid-cylinders.png>)

Enter the mass in kilograms as a number only.

**Explanation**

Organize the givens by their role before calculating:

| Role | Quantity |
|---|---:|
| Tangential force | $F=1.4\ \mathrm{N}$ |
| Force radius and known-cylinder radius | $R=0.85\ \mathrm{m}$ |
| Known cylinder mass | $M=2.3\ \mathrm{kg}$ |
| Unknown-cylinder radius | $r=0.36\ \mathrm{m}$ |
| Shared angular acceleration | $\alpha=1.2\ \mathrm{rad/s^2}$ |

The applied torque and total inertia are

$$
\tau=FR=(1.4)(0.85)=1.19\ \mathrm{N\,m},
$$

$$
I_{\text{total}}
=\frac{\tau}{\alpha}
=\frac{1.19}{1.2}
=0.99167\ldots\ \mathrm{kg\,m^2}.
$$

The larger cylinder contributes

$$
I_{\text{large}}
=\frac12MR^2
=\frac12(2.3)(0.85)^2
=0.830875\ \mathrm{kg\,m^2}.
$$

Therefore, the smaller cylinder contributes

$$
I_{\text{small}}
=0.99167\ldots-0.830875
=0.16079\ldots\ \mathrm{kg\,m^2}.
$$

Keep these guard digits until the mass has been found. Rounding either inertia too early changes a small difference and can noticeably shift the final mass.

Solve $I_{\text{small}}=\tfrac12mr^2$:

$$
m
=\frac{2I_{\text{small}}}{r^2}
=\frac{2(0.16079\ldots)}{(0.36)^2}
=2.4814\ldots\ \mathrm{kg}.
$$

Substitution checks the inertia budget. Using $m=2.4814\ldots\ \mathrm{kg}$,

$$
\frac12(2.3)(0.85)^2
+\frac12(2.4814\ldots)(0.36)^2
=0.99167\ldots\ \mathrm{kg\,m^2},
$$

which agrees with $FR/\alpha$. The remaining inertia is positive, and the final units are kilograms.

The measured givens have two significant figures, so the number-only answer is

$$
\boxed{2.5}.
$$

```quiz
type: radio
id: p6-source-check
content: |-
  Which number should be entered for the mass in the source problem?
options:
- id: p6-source-check-a
  content: |-
    $0.45$
- id: p6-source-check-b
  content: |-
    $1.2$
- id: p6-source-check-c
  content: |-
    $2.5$
  correct: true
- id: p6-source-check-d
  content: |-
    $15$
```

---

<a id="summary"></a>
## Summary

For rigidly attached solid cylinders driven by a tangential force:

1. Calculate $\tau=FR$.
2. Find $I_{\text{total}}=\tau/\alpha$.
3. Calculate the known cylinder's inertia with $I=\tfrac12MR^2$.
4. Subtract to find the unknown cylinder's inertia.
5. Solve $m=2I_{\text{unknown}}/r^2$ and round only at the end.

Equivalently, use the one-line result

$$
m=\frac{2}{r^2}\left(\frac{FR}{\alpha}-\frac12MR^2\right).
$$

The main traps are treating the cylinders separately even though they share one angular acceleration, swapping $R$ and $r$, or forgetting the $\tfrac12$ and the squared radius in the solid-cylinder formula. A correct result has units of kilograms and reproduces the total inertia when substituted back.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
