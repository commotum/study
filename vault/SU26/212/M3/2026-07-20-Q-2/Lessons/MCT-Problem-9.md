# Solve a Two-Block System with a Massive Pulley

<!--
lesson-id: 212-M3-045
topic-code: MTH212.M3.45
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose Motion-Positive Directions](#choose-motion-positive-directions)
- [Write One Equation per Body](#write-one-equation-per-body)
- [Derive the Compact Acceleration](#derive-the-compact-acceleration)
- [Source-Video Worked Problem](#source-video-worked-problem)
- [Check the Tensions and Limits](#check-the-tensions-and-limits)
- [Lecture-Note Limit: Spool Fixed at Its Spindle](#lecture-note-fixed-spool)
- [Lecture-Note Geometry Change: Vertical Atwood Machine](#lecture-note-vertical-atwood)
- [Summary](#summary)

## Prerequisites

- Draw a separate free-body diagram for each translating object.
- Apply $\sum F=ma$ along a chosen positive direction.
- Apply $\sum\tau=I\alpha$ to a fixed-axis pulley.
- Use $I=\frac12MR^2$ for a uniform solid-disk pulley.
- Use the no-slip relation $a=\alpha R$.
- Solve simultaneous linear equations by substitution or elimination.

---

<a id="introduction"></a>
## Introduction

A massive pulley needs a net torque to rotate. The tensions on its two sides therefore differ:

$$
T_1\ne T_2.
$$

For a frictionless table, a hanging block, and an ideal string that does not slip on a massive pulley, use one procedure:

1. Draw separate free-body diagrams for block $m_1$, block $m_2$, and the pulley.
2. Give each moving object a positive direction along the actual motion.
3. Write one force equation for each block and one torque equation for the pulley.
4. Connect translation and rotation with $a=\alpha R$.
5. Solve the simultaneous system before inserting numbers.

Use distinct symbols throughout:

- $m_1$: block on the horizontal surface,
- $m_2$: hanging block,
- $M$: pulley mass,
- $R$: pulley radius,
- $T_1$: table-side tension,
- $T_2$: hanging-side tension.

Each straight massless string segment has a uniform tension magnitude. The string's contact with the accelerating massive pulley still allows the two side values to differ.

---

<a id="choose-motion-positive-directions"></a>
## Choose Motion-Positive Directions

For the surface-and-hanging geometry, choose

- right as positive for $m_1$,
- down as positive for $m_2$, and
- clockwise as positive for the pulley.

Then the same positive acceleration magnitude $a$ appears in both block equations, while the angular acceleration is positive with

$$
a=\alpha R.
$$

```text
                 clockwise +
                     ↻
 m1        T1 →       O pulley
[  ]──────────────────╮
                      │
                      │  ↑ T2
                      │ [m2]
                      │  ↓ m2 g, +
```

On the pulley, $T_2$ tends to turn it clockwise while $T_1$ tends to turn it counterclockwise. Therefore $T_2$ enters the motion-positive torque equation with a plus sign and $T_1$ with a minus sign.

---

<a id="write-one-equation-per-body"></a>
## Write One Equation per Body

The three body equations and the no-slip constraint are:

$$
\boxed{T_1=m_1a} \tag{1}
$$

$$
\boxed{m_2g-T_2=m_2a} \tag{2}
$$

$$
\boxed{(T_2-T_1)R=I\alpha} \tag{3}
$$

$$
\boxed{a=\alpha R}. \tag{4}
$$

Equation (1) comes from the horizontal free-body diagram of $m_1$. Equation (2) comes from the vertical free-body diagram of $m_2$. Equation (3) belongs to the pulley alone.

Newton's third law gives equal-and-opposite forces at each individual string contact. It does not equate $T_1$ with $T_2$; their difference is precisely what supplies the pulley's net torque.

```quiz
type: radio
id: mct-p9-equation-set
shuffle: true
content: |-
  A block $m_1$ moves right on a frictionless table while a hanging block $m_2$ moves down. The massive pulley rotates clockwise without slip. Which equation set is consistent with right, down, and clockwise all chosen positive?
options:
- id: mct-p9-equation-set-a
  content: |-
    $T_1=m_1a$, $m_2g-T_2=m_2a$, $(T_2-T_1)R=I\alpha$, and $a=\alpha R$
  correct: true
  feedback: |-
    Each equation follows its body's motion-positive direction. The hanging-side tension supplies clockwise torque, the table-side tension opposes it, and no slip gives $a=\alpha R$.
- id: mct-p9-equation-set-b
  content: |-
    $T=m_1a$, $m_2g-T=m_2a$, $TR=I\alpha$, and $a=\alpha R$
  feedback: |-
    This imposes one tension on both sides and gives the pulley only one torque. A massive rotating pulley requires the difference $(T_2-T_1)R$ and generally has $T_1\ne T_2$.
- id: mct-p9-equation-set-c
  content: |-
    $T_1=m_1a$, $T_2-m_2g=m_2a$, $(T_2-T_1)R=I\alpha$, and $a=\alpha R$
  feedback: |-
    The hanging-block equation uses upward as positive even though the question chose downward positive. With downward positive, its net force is $m_2g-T_2$.
- id: mct-p9-equation-set-d
  content: |-
    $T_1=m_1a$, $m_2g-T_2=m_2a$, $(T_2+T_1)R=I\alpha$, and $a=\alpha R$
  feedback: |-
    The two tensions turn the pulley in opposite directions, so their torque magnitudes subtract. Adding them would ignore their opposing rotational senses.
- id: mct-p9-equation-set-e
  content: |-
    $T_1=m_1a$, $m_2g-T_2=m_2a$, $(T_2-T_1)R=I\alpha$, and $a=\alpha/R$
  feedback: |-
    The force and torque equations are consistent, but the no-slip constraint is dimensionally wrong. Tangential acceleration is $a=\alpha R$, not $\alpha/R$.
```

---

<a id="derive-the-compact-acceleration"></a>
## Derive the Compact Acceleration

Use the no-slip constraint in the pulley equation:

$$
\begin{aligned}
(T_2-T_1)R&=I\alpha,\\
(T_2-T_1)R&=I\frac{a}{R},\\
T_2-T_1&=\frac{I}{R^2}a. \tag{5}
\end{aligned}
$$

Now isolate the tensions from the two block equations:

$$
T_1=m_1a,
\qquad
T_2=m_2g-m_2a.
$$

Substitute both into equation (5):

$$
(m_2g-m_2a)-m_1a=\frac{I}{R^2}a.
$$

Collect the acceleration terms:

$$
m_2g=\left(m_1+m_2+\frac{I}{R^2}\right)a.
$$

Therefore,

$$
\boxed{a=\frac{m_2g}{m_1+m_2+I/R^2}}. \tag{6}
$$

The quantity $I/R^2$ has units of mass and records how the pulley's rotational inertia reduces the linear acceleration. It is an **effective-inertia term in this equation**, not an additional physical mass hanging from the string.

For a solid-disk pulley,

$$
\frac{I}{R^2}
=\frac{\frac12MR^2}{R^2}
=\frac{M}{2}.
$$

The no-slip substitution $\alpha=a/R$ produces the general term $I/R^2$. The radius fully cancels only after the solid-disk relation $I=\frac12MR^2$ is also used. If $I$ is supplied independently, retain $I/R^2$.

```quiz
type: radio
id: mct-p9-acceleration-control
shuffle: true
content: |-
  A $4.0\,\mathrm{kg}$ block lies on a frictionless table and is connected to a hanging $6.0\,\mathrm{kg}$ block over a solid-disk pulley of mass $8.0\,\mathrm{kg}$. The string does not slip. What is the acceleration magnitude? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p9-acceleration-control-a
  content: |-
    $4.20\,\mathrm{m/s^2}$
  correct: true
  feedback: |-
    For a solid disk, $I/R^2=M/2=4.0\,\mathrm{kg}$. Thus $a=(6)(9.8)/(4+6+4)=58.8/14=4.20\,\mathrm{m/s^2}$.
- id: mct-p9-acceleration-control-b
  content: |-
    $5.88\,\mathrm{m/s^2}$
  feedback: |-
    This is the massless-pulley result $58.8/(4+6)$. The $8.0\,\mathrm{kg}$ solid disk contributes the effective-inertia term $M/2=4.0\,\mathrm{kg}$.
- id: mct-p9-acceleration-control-c
  content: |-
    $3.27\,\mathrm{m/s^2}$
  feedback: |-
    This inserts the pulley's full mass $M$ in the denominator. A solid disk contributes $I/R^2=M/2$, so the denominator is $14\,\mathrm{kg}$ rather than $18\,\mathrm{kg}$.
- id: mct-p9-acceleration-control-d
  content: |-
    $7.35\,\mathrm{m/s^2}$
  feedback: |-
    This omits the table block $m_1$ from the denominator. That block also accelerates, so its $4.0\,\mathrm{kg}$ must be included.
- id: mct-p9-acceleration-control-e
  content: |-
    $9.80\,\mathrm{m/s^2}$
  feedback: |-
    This treats the hanging block as freely falling. Both the table block and the pulley's rotation require force, so the acceleration must be less than $g$.
```

---

<a id="source-video-worked-problem"></a>
## Source-Video Worked Problem

**Source-video worked problem (`dbvr-L5rxdg`, 9:44–23:13):** A $5\,\mathrm{kg}$ block lies on a frictionless horizontal surface. It is connected over a solid-disk pulley of mass $20\,\mathrm{kg}$ and radius $3\,\mathrm m$ to a hanging $10\,\mathrm{kg}$ block. The system is released from rest.

The full motion-positive system is

$$
T_1=m_1a,
$$

$$
m_2g-T_2=m_2a,
$$

$$
(T_2-T_1)R=I\alpha,
$$

$$
a=\alpha R.
$$

For the pulley,

$$
I=\frac12MR^2
=\frac12(20)(3^2)
=90\,\mathrm{kg\,m^2},
$$

so

$$
\frac{I}{R^2}=\frac{90}{3^2}=10\,\mathrm{kg}=\frac{M}{2}.
$$

The compact result now gives

$$
\begin{aligned}
a
&=\frac{m_2g}{m_1+m_2+I/R^2}\\
&=\frac{(10)(9.8)}{5+10+10}\\
&=\frac{98}{25}\\
&=3.92\,\mathrm{m/s^2}.
\end{aligned}
$$

The pulley accelerates clockwise at

$$
\alpha=\frac{a}{R}
=\frac{3.92}{3}
\approx1.31\,\mathrm{rad/s^2}.
$$

**Source correction:** Near 20:13, the video briefly writes $T_2=m_2g+m_2a$, then explicitly corrects the sign near 20:37. With downward positive, the correct equation is

$$
m_2g-T_2=m_2a
\quad\Longrightarrow\quad
T_2=m_2g-m_2a.
$$

**Sign-convention clarification:** The video initially uses upward $y$ and counterclockwise as positive, so the actual downward and clockwise accelerations carry negative signs. This lesson instead chooses the directions of motion as positive. Both conventions give the same magnitudes when used consistently.

---

<a id="check-the-tensions-and-limits"></a>
## Check the Tensions and Limits

For the source-video values,

$$
T_1=m_1a=(5)(3.92)=19.6\,\mathrm N,
$$

$$
T_2=m_2(g-a)=(10)(9.8-3.92)=58.8\,\mathrm N.
$$

The inequality $T_2>T_1$ is required for clockwise angular acceleration. Check the pulley equation:

$$
(T_2-T_1)R=(58.8-19.6)(3)=117.6\,\mathrm{N\,m},
$$

$$
I\alpha=(90)(1.306\ldots)=117.6\,\mathrm{N\,m}.
$$

Useful limiting checks are:

- $0<a<g$ for this frictionless surface-and-hanging setup.
- If $I\to0$, equation (5) gives $T_2-T_1\to0$, so the tensions approach equality.
- The massless-pulley acceleration is
  $$
  a\to\frac{m_2g}{m_1+m_2}.
  $$
- Increasing $I$ while holding the blocks and radius fixed decreases $a$.

The video calls the solid disk's $M/2$ term an “inertial mass.” Treat that phrase only as shorthand for the derived quantity $I/R^2$; the pulley has not acquired another literal mass.

```quiz
type: radio
id: mct-p9-tension-control
shuffle: true
content: |-
  In the earlier controlled case, $m_1=4.0\,\mathrm{kg}$, $m_2=6.0\,\mathrm{kg}$, and $a=4.20\,\mathrm{m/s^2}$. What are $(T_1,T_2)$? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p9-tension-control-a
  content: |-
    $(16.8,\ 33.6)\,\mathrm N$
  correct: true
  feedback: |-
    $T_1=m_1a=(4)(4.2)=16.8\,\mathrm N$, while $T_2=m_2(g-a)=6(9.8-4.2)=33.6\,\mathrm N$. Their difference drives the pulley clockwise.
- id: mct-p9-tension-control-b
  content: |-
    $(33.6,\ 16.8)\,\mathrm N$
  feedback: |-
    These values are swapped. The hanging-side tension must exceed the table-side tension to produce the clockwise torque, so $T_2$ is $33.6\,\mathrm N$.
- id: mct-p9-tension-control-c
  content: |-
    $(16.8,\ 16.8)\,\mathrm N$
  feedback: |-
    Equal tensions would give zero net pulley torque. Because the massive pulley has angular acceleration, $T_2-T_1$ must be nonzero.
- id: mct-p9-tension-control-d
  content: |-
    $(16.8,\ 58.8)\,\mathrm N$
  feedback: |-
    The second value is the hanging block's weight $m_2g$. Since the block accelerates downward, its upward tension is smaller than its weight: $T_2=m_2(g-a)=33.6\,\mathrm N$.
- id: mct-p9-tension-control-e
  content: |-
    $(33.6,\ 58.8)\,\mathrm N$
  feedback: |-
    This assigns the hanging block's weight to $T_2$ and uses the actual $T_2$ value for $T_1$. Apply the two separate block equations rather than transferring one force value between bodies.
```

---

<a id="lecture-note-fixed-spool"></a>
## Lecture-Note Limit: Spool Fixed at Its Spindle

**Paired M2-3 lecture-note example:** A tangential cord tension $T$ turns a solid cylindrical spool of mass $m$ and radius $R$, while its spindle keeps the center fixed.

The spindle's horizontal support force can be nonzero and cancel the translational effect of $T$. Because the support force acts at the pivot, however, its moment arm and torque about that pivot are zero.

Only the tangential tension contributes to the torque equation:

$$
TR=I\alpha
=\frac12mR^2\alpha.
$$

Therefore,

$$
\boxed{\alpha=\frac{2T}{mR}}.
$$

This is the fixed-center limit of the same bookkeeping rule: a force equation handles translation, while a torque equation handles rotation.

```quiz
type: radio
id: mct-p9-fixed-spool-control
shuffle: true
content: |-
  A $12\,\mathrm N$ tangential tension turns a solid cylindrical spool of mass $4.0\,\mathrm{kg}$ and radius $0.50\,\mathrm m$. The spindle holds the center fixed. What is the angular acceleration magnitude?
options:
- id: mct-p9-fixed-spool-control-a
  content: |-
    $12\,\mathrm{rad/s^2}$
  correct: true
  feedback: |-
    Using $\alpha=2T/(mR)$ gives $\alpha=2(12)/[(4)(0.50)]=12\,\mathrm{rad/s^2}$. The spindle force has zero moment arm about the axis.
- id: mct-p9-fixed-spool-control-b
  content: |-
    $0\,\mathrm{rad/s^2}$
  feedback: |-
    The spindle force cancels translation, not the tension's torque. Since it acts at the pivot, its torque is zero and the tangential tension still spins the spool.
- id: mct-p9-fixed-spool-control-c
  content: |-
    $6.0\,\mathrm{rad/s^2}$
  feedback: |-
    This uses $I=mR^2$ instead of the solid-cylinder formula $I=\frac12mR^2$. The factor of one-half doubles the resulting angular acceleration.
- id: mct-p9-fixed-spool-control-d
  content: |-
    $24\,\mathrm{rad/s^2}$
  feedback: |-
    This makes the spool's inertia half as large again. With $I=\frac12(4)(0.50^2)=0.50\,\mathrm{kg\,m^2}$ and $\tau=6.0\,\mathrm{N\,m}$, the quotient is $12\,\mathrm{rad/s^2}$.
- id: mct-p9-fixed-spool-control-e
  content: |-
    $3.0\,\mathrm{rad/s^2}$
  feedback: |-
    This divides the tension by the mass without correctly using torque or rotational inertia. The radius appears in both $TR$ and $\frac12mR^2$ before one factor cancels.
```

---

<a id="lecture-note-vertical-atwood"></a>
## Lecture-Note Geometry Change: Vertical Atwood Machine

**Paired M2-4 lecture-note comparison:** Two hanging masses flank a massive pulley, with $m_2>m_1$. Choose upward as positive for $m_1$, downward as positive for $m_2$, and clockwise as positive for the pulley.

Only the first block equation changes:

$$
T_1-m_1g=m_1a,
$$

$$
m_2g-T_2=m_2a,
$$

$$
(T_2-T_1)R=I\alpha,
\qquad
a=\alpha R.
$$

Eliminating the tensions gives

$$
\boxed{a=\frac{(m_2-m_1)g}{m_1+m_2+I/R^2}}.
$$

The system-solving move is unchanged. The numerator changes from $m_2g$ to $(m_2-m_1)g$ because the lighter hanging block's weight now opposes the motion.

```quiz
type: radio
id: mct-p9-atwood-control
shuffle: true
content: |-
  A vertical Atwood machine has $m_1=3.0\,\mathrm{kg}$, $m_2=7.0\,\mathrm{kg}$, and a solid-disk pulley of mass $M=4.0\,\mathrm{kg}$. What is the acceleration magnitude? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p9-atwood-control-a
  content: |-
    $3.27\,\mathrm{m/s^2}$
  correct: true
  feedback: |-
    The driving numerator is $(7-3)(9.8)=39.2\,\mathrm N$, and $I/R^2=M/2=2.0\,\mathrm{kg}$. Thus $a=39.2/(3+7+2)=3.27\,\mathrm{m/s^2}$.
- id: mct-p9-atwood-control-b
  content: |-
    $3.92\,\mathrm{m/s^2}$
  feedback: |-
    This is the massless-pulley result $39.2/(3+7)$. The solid disk adds the effective-inertia term $M/2=2.0\,\mathrm{kg}$ to the denominator.
- id: mct-p9-atwood-control-c
  content: |-
    $5.72\,\mathrm{m/s^2}$
  feedback: |-
    This uses $m_2g$ alone as the driving force. In the vertical Atwood geometry, $m_1g$ opposes the motion, so the numerator is $(m_2-m_1)g$.
- id: mct-p9-atwood-control-d
  content: |-
    $2.80\,\mathrm{m/s^2}$
  feedback: |-
    This uses the pulley's full mass $M$ in the denominator. A solid disk contributes $I/R^2=M/2$, not $M$.
- id: mct-p9-atwood-control-e
  content: |-
    $-3.27\,\mathrm{m/s^2}$
  feedback: |-
    The question asks for a magnitude, which is nonnegative. With motion-positive directions, $m_2$ accelerates downward and $m_1$ upward with magnitude $3.27\,\mathrm{m/s^2}$.
```

---

<a id="summary"></a>
## Summary

- Draw separate free-body diagrams for $m_1$, $m_2$, and the pulley.
- Choose positive directions along the motion so both blocks share one positive acceleration magnitude.
- For the surface-and-hanging geometry, write
  $$
  T_1=m_1a,
  \qquad
  m_2g-T_2=m_2a.
  $$
- For clockwise-positive pulley motion, write
  $$
  (T_2-T_1)R=I\alpha,
  \qquad
  a=\alpha R.
  $$
- Derive rather than memorize
  $$
  a=\frac{m_2g}{m_1+m_2+I/R^2}.
  $$
- For a solid disk, $I/R^2=M/2$; this is an effective-inertia term, not literal added mass.
- A massive accelerating pulley generally requires $T_2\ne T_1$.
- Check $0<a<g$, the expected tension ordering, all original equations, and the massless-pulley limit.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
