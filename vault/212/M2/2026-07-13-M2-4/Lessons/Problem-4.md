# Finding Atwood-Machine Acceleration With a Massive Pulley

<!--
lesson-id: 212-M2-030
topic-code: MTH212.M2.30
-->

## Table of Contents

- [Introduction](#introduction)
- [Write the Two Block Equations](#write-the-two-block-equations)
- [Write the Pulley Torque Equation](#write-the-pulley-torque-equation)
- [Eliminate the Tensions](#eliminate-the-tensions)
- [Use the Uniform-Disk Inertia](#use-the-uniform-disk-inertia)
- [Apply the Formula](#apply-the-formula)
- [Summary](#summary)

## Prerequisites

- Apply Newton's second law with a chosen positive direction.
- Use $\tau=I\alpha$ and the no-slip relation $\alpha=a/r$.
- Recall $I=\frac12m_pr^2$ for a uniform disk.
- Simplify rational expressions by canceling common factors.

---

<a id="introduction"></a>
## Introduction

An Atwood machine with a massive pulley accelerates more slowly than the ideal massless-pulley system because some of the gravitational drive must angularly accelerate the pulley. A frictionless axle removes axle friction, but it does not remove the pulley's rotational inertia.

For hanging masses $m_1$ and $m_2$ connected over a pulley of moment of inertia $I$ and radius $r$,

$$
\boxed{a=\frac{(m_2-m_1)g}{m_1+m_2+I/r^2}}.
$$

For a uniform-disk pulley, $I=\frac12m_pr^2$, so the radius cancels and the pulley contributes an effective inertia of $m_p/2$:

$$
\boxed{a=\frac{(m_2-m_1)g}{m_1+m_2+\frac12m_p}}.
$$

| Equation | What it accounts for |
|---|---|
| $m_2g-T_2=m_2a$ | translation of Block 2 |
| $T_1-m_1g=m_1a$ | translation of Block 1 |
| $(T_2-T_1)r=I\alpha$ | rotation of the pulley |
| $\alpha=a/r$ | no slipping between string and pulley |

---

<a id="write-the-two-block-equations"></a>
## Write the Two Block Equations

**Example:** Suppose $m_2>m_1$. Write Newton's second-law equation for each block using the direction of motion as positive for that block.

**Explanation**

Block 2 accelerates downward, so take downward as positive:

$$
m_2g-T_2=m_2a.
$$

Block 1 accelerates upward, so take upward as positive:

$$
T_1-m_1g=m_1a.
$$

Using the motion direction as positive makes both right-hand sides $+ma$. The tensions are labeled separately because a massive accelerating pulley requires a net torque.

```quiz
type: radio
id: m2-4-p4-block-equations
content: |-
  In an Atwood machine, $m_2>m_1$. Block 2 accelerates downward and Block 1 accelerates upward. Which pair of equations uses each block's motion direction as positive?
options:
- id: a
  content: |-
    $m_2g-T_2=m_2a$ and $T_1-m_1g=m_1a$
  correct: true
  feedback: |-
    For Block 2, downward weight is positive and upward tension is negative. For Block 1, upward tension is positive and downward weight is negative.
- id: b
  content: |-
    $T_2-m_2g=m_2a$ and $m_1g-T_1=m_1a$
- id: c
  content: |-
    $m_2g+T_2=m_2a$ and $T_1+m_1g=m_1a$
- id: d
  content: |-
    $m_2g-T_1=m_2a$ and $T_2-m_1g=m_1a$
- id: e
  content: |-
    $m_2g-m_1g=(m_2-m_1)a$ for each block separately
```

---

<a id="write-the-pulley-torque-equation"></a>
## Write the Pulley Torque Equation

**Example:** Relate the tension difference to the linear acceleration when the string does not slip on a pulley of radius $r$ and inertia $I$.

**Explanation**

The two tensions act at radius $r$ in opposite rotational directions, so the net torque magnitude is

$$
\tau_{\text{net}}=(T_2-T_1)r.
$$

Use $\tau=I\alpha$ and $\alpha=a/r$:

$$
\begin{aligned}
(T_2-T_1)r&=I\alpha\\
&=I\frac{a}{r}.
\end{aligned}
$$

Therefore,

$$
\boxed{T_2-T_1=\frac{I}{r^2}a}.
$$

When $I>0$ and $a>0$, the tensions cannot be equal.

```quiz
type: radio
id: m2-4-p4-pulley-torque
content: |-
  A pulley of radius $r$ and moment of inertia $I$ has string tensions $T_2>T_1$, and the string does not slip. Which equation relates the tensions to the blocks' linear acceleration $a$?
options:
- id: a
  content: |-
    $T_2-T_1=Ia/r^2$
  correct: true
  feedback: |-
    $(T_2-T_1)r=I\alpha$ and $\alpha=a/r$, so dividing by $r$ gives $T_2-T_1=Ia/r^2$.
- id: b
  content: |-
    $T_2-T_1=Iar^2$
- id: c
  content: |-
    $T_2+T_1=Ia/r^2$
- id: d
  content: |-
    $T_2-T_1=Ia/r$
- id: e
  content: |-
    $T_2=T_1$
```

---

<a id="eliminate-the-tensions"></a>
## Eliminate the Tensions

**Example:** Combine the two block equations with the pulley equation to solve for $a$.

**Explanation**

Add the two block equations:

$$
\begin{aligned}
(m_2g-T_2)+(T_1-m_1g)&=(m_1+m_2)a\\
(m_2-m_1)g-(T_2-T_1)&=(m_1+m_2)a.
\end{aligned}
$$

Substitute $T_2-T_1=(I/r^2)a$:

$$
(m_2-m_1)g-\frac{I}{r^2}a=(m_1+m_2)a.
$$

Collect every term multiplying $a$:

$$
(m_2-m_1)g=\left(m_1+m_2+\frac{I}{r^2}\right)a.
$$

Thus,

$$
a=\frac{(m_2-m_1)g}{m_1+m_2+I/r^2}.
$$

```quiz
type: radio
id: m2-4-p4-general-acceleration
content: |-
  Which formula gives the acceleration magnitude of an Atwood machine with pulley moment of inertia $I$ and radius $r$, assuming $m_2>m_1$ and no slipping?
options:
- id: a
  content: |-
    $a=\dfrac{(m_2-m_1)g}{m_1+m_2+I/r^2}$
  correct: true
  feedback: |-
    Eliminating the tensions places the pulley's positive effective inertia $I/r^2$ alongside the two block masses in the denominator.
- id: b
  content: |-
    $a=\dfrac{(m_2-m_1)g}{m_1+m_2-I/r^2}$
- id: c
  content: |-
    $a=\dfrac{(m_1+m_2)g}{m_2-m_1+I/r^2}$
- id: d
  content: |-
    $a=\dfrac{(m_2-m_1+I/r^2)g}{m_1+m_2}$
- id: e
  content: |-
    $a=\dfrac{(m_2-m_1)g}{I/r^2}$
```

---

<a id="use-the-uniform-disk-inertia"></a>
## Use the Uniform-Disk Inertia

**Example:** Simplify the pulley term $I/r^2$ for a uniform disk of mass $m_p$ and radius $r$.

**Explanation**

Substitute the uniform-disk inertia before inserting numbers:

$$
\begin{aligned}
\frac{I}{r^2}
&=\frac{\frac12m_pr^2}{r^2}\\
&=\frac12m_p.
\end{aligned}
$$

The common factor $r^2$ cancels. Therefore,

$$
\boxed{a=\frac{(m_2-m_1)g}{m_1+m_2+\frac12m_p}}.
$$

The pulley contributes half its mass to the effective inertia—not its full mass. The stated radius is not needed after this simplification.

```quiz
type: radio
id: m2-4-p4-uniform-disk-term
content: |-
  A uniform-disk pulley has $I=\frac12m_pr^2$. What does the term $I/r^2$ simplify to?
options:
- id: a
  content: |-
    $\frac12m_p$
  correct: true
  feedback: |-
    Substitute $I=\frac12m_pr^2$ into $I/r^2$ and cancel the common nonzero factor $r^2$, leaving $m_p/2$.
- id: b
  content: |-
    $m_p$
- id: c
  content: |-
    $\frac12m_pr$
- id: d
  content: |-
    $\frac12m_pr^2$
- id: e
  content: |-
    $m_p/r^2$
```

---

<a id="apply-the-formula"></a>
## Apply the Formula

**Example:** Calculate the acceleration for the given blocks and uniform-disk pulley.

**Explanation**

Substitute into the simplified formula, keeping the grouped pieces visible:

| Piece | Calculation | Value |
|---|---|---:|
| mass difference | $2.6-1.2$ | $1.4\ \mathrm{kg}$ |
| driving-force numerator | $(1.4)(9.81)$ | $13.734\ \mathrm{N}$ |
| effective-inertia denominator | $1.2+2.6+\frac12(3.3)$ | $5.45\ \mathrm{kg}$ |

$$
\begin{aligned}
a
&=\frac{(m_2-m_1)g}{m_1+m_2+\frac12m_p}\\
&=\frac{13.734}{5.45}\\
&=2.519\ldots\ \mathrm{m/s^2}.
\end{aligned}
$$

The measured givens have two significant figures, so $a=2.5\ \mathrm{m/s^2}$. Since $m_2>m_1$, Block 2 accelerates downward and Block 1 upward.

The units reduce correctly: $\mathrm{N/kg}=\mathrm{m/s^2}$. Also, a massless pulley would give

$$
a_0=\frac{(2.6-1.2)(9.81)}{1.2+2.6}=3.61\ldots\ \mathrm{m/s^2}.
$$

The massive-pulley result satisfies $0<a<a_0<g$, as expected.

```quiz
type: radio
id: m2-4lec-q3
content: |-
  **Question 3**

  Block 1 of mass $m_1$ and block 2 of mass $m_2$ are connected by a massless string over a frictionless uniform-disk pulley of mass $m_p$ and radius $r$. Find the system's acceleration for $m_1=1.2\ \mathrm{kg}$, $m_2=2.6\ \mathrm{kg}$, $m_p=3.3\ \mathrm{kg}$, and $r=0.56\ \mathrm{m}$.

  ![](<../Source/Images/massive-pulley-atwood-machine.png>)

  Enter the acceleration magnitude in meters per second squared as a number only:
options:
- id: a
  content: |-
    `2.5`
  correct: true
  feedback: |-
    The block equations and pulley torque equation combine to give

    $$
    a=\frac{(m_2-m_1)g}{m_1+m_2+I/r^2}.
    $$

    For a uniform-disk pulley, $I=\frac12m_pr^2$, so

    $$
    a=\frac{(m_2-m_1)g}{m_1+m_2+\frac12m_p}.
    $$

    Substitution gives

    $$
    a=\frac{(2.6-1.2)(9.81)}{1.2+2.6+\frac12(3.3)}
    =2.519\ldots\ \mathrm{m/s^2}.
    $$

    The measured givens have two significant figures, so $a=2.5\ \mathrm{m/s^2}$. Block 2 accelerates downward while block 1 accelerates upward.
- id: b
  content: |-
    `3.6`
- id: c
  content: |-
    `1.9`
- id: d
  content: |-
    `-2.5`
- id: e
  content: |-
    `2.52`
```

---

<a id="summary"></a>
## Summary

- **Cue:** the axle is frictionless, but the pulley has mass and rotational inertia.
- **Blocks:** $m_2g-T_2=m_2a$ and $T_1-m_1g=m_1a$.
- **Pulley:** $T_2-T_1=(I/r^2)a$.
- **Eliminate:** combine the equations to get $a=(m_2-m_1)g/(m_1+m_2+I/r^2)$.
- **Uniform disk:** $I/r^2=\frac12m_p$, so the radius cancels.
- **Direction:** the heavier block moves downward.
- **Check:** a massive pulley must give a positive acceleration smaller than the massless-pulley result and smaller than $g$.
- **Main trap:** frictionless does not mean massless, and the pulley contributes $m_p/2$, not $m_p$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../../M3/2026-07-20-Q-2/Study-Guide.md)
Next: [Comparing Atwood-Machine Accelerations With Pulley Inertia](../../2026-07-14-M2-5/Lessons/Problem-1.md)

Study guide index: 05/20

---

<!-- lesson-nav:end -->
