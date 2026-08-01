# Comparing Atwood-Machine Accelerations With Pulley Inertia

## Table of Contents

- [Introduction](#introduction)
- [Identify the Unchanged Driving Force](#identify-the-unchanged-driving-force)
- [Include the Pulley's Rotational Inertia](#include-the-pulleys-rotational-inertia)
- [Compare the Two Denominators](#compare-the-two-denominators)
- [Distinguish Frictionless From Massless](#distinguish-frictionless-from-massless)
- [Apply the Comparison](#apply-the-comparison)
- [Summary](#summary)

## Prerequisites

- Apply Newton's second law to two connected masses.
- Use $\tau=I\alpha$ and the no-slip relation $\alpha=a/r$.
- Compare positive fractions that have the same numerator.

---

<a id="introduction"></a>
## Introduction

When two Atwood machines have the same hanging masses but only one pulley has rotational inertia, the gravitational driving force is the same in both systems. The massive pulley must also be given angular acceleration, so it adds a positive effective-inertia term to the denominator of the acceleration formula.

The reusable comparison is

$$
a_A=\frac{(m_2-m_1)g}{m_1+m_2}
$$

for a massless pulley and

$$
a_B=\frac{(m_2-m_1)g}{m_1+m_2+I/r^2}
$$

for a pulley with moment of inertia $I$ and radius $r$. Since $I/r^2>0$, System B has the larger denominator and the smaller acceleration.

---

<a id="identify-the-unchanged-driving-force"></a>
## Identify the Unchanged Driving Force

**Example:** Two Atwood machines use the same masses $m_1$ and $m_2$, with $m_2>m_1$. One pulley is massless and the other is massive. Compare the net gravitational force that drives the motion.

**Explanation**

For the two hanging masses considered together, the opposing weights leave the driving force

$$
F_{\text{drive}}=m_2g-m_1g=(m_2-m_1)g.
$$

The masses are identical in the two systems, so this numerator is unchanged. The pulley mass is supported by its axle; it does not add another hanging weight to the driving force.

```quiz
type: radio
id: m2-5-p1-driving-force
content: |-
  Two Atwood machines use the same hanging masses $m_1$ and $m_2$, where $m_2>m_1$, but their pulleys have different rotational inertias. Which expression is the gravitational force that drives the motion in either system?
options:
- id: a
  content: |-
    $(m_2-m_1)g$
  correct: true
- id: b
  content: |-
    $(m_1+m_2)g$
- id: c
  content: |-
    $m_2g$
- id: d
  content: |-
    $m_1g$
- id: e
  content: |-
    $(m_2-m_1+I/r^2)g$
feedback: |-
  The weights oppose each other, leaving $(m_2-m_1)g$. Pulley inertia affects the response to this force, not the gravitational driving-force numerator.
```

---

<a id="include-the-pulleys-rotational-inertia"></a>
## Include the Pulley's Rotational Inertia

**Example:** Derive the acceleration equation when the pulley has moment of inertia $I$, radius $r$, and the string does not slip.

**Explanation**

Let the heavier mass accelerate downward with magnitude $a$. The force equations are

$$
m_2g-T_2=m_2a
$$

and

$$
T_1-m_1g=m_1a.
$$

The two tensions exert a net torque on the pulley. Using $\alpha=a/r$,

$$
\begin{aligned}
(T_2-T_1)r&=I\alpha\\
T_2-T_1&=\frac{I}{r^2}a.
\end{aligned}
$$

Adding the two mass equations combines the opposite tension terms into the exact difference needed by the torque equation:

$$
\begin{aligned}
(m_2g-T_2)+(T_1-m_1g)&=(m_1+m_2)a\\
(m_2-m_1)g-(T_2-T_1)&=(m_1+m_2)a.
\end{aligned}
$$

Substituting $T_2-T_1=(I/r^2)a$ gives

$$
(m_2-m_1)g
=\left(m_1+m_2+\frac{I}{r^2}\right)a.
$$

Therefore,

$$
\boxed{a=\frac{(m_2-m_1)g}{m_1+m_2+I/r^2}}.
$$

```quiz
type: radio
id: m2-5-p1-massive-pulley-formula
content: |-
  An Atwood machine has hanging masses $m_1$ and $m_2$, a pulley of radius $r$ and moment of inertia $I$, and no slipping. Which acceleration formula includes the pulley's rotational response?
options:
- id: a
  content: |-
    $a=\dfrac{(m_2-m_1)g}{m_1+m_2+I/r^2}$
  correct: true
- id: b
  content: |-
    $a=\dfrac{(m_2-m_1)g}{m_1+m_2-I/r^2}$
- id: c
  content: |-
    $a=\dfrac{(m_1+m_2)g}{m_2-m_1+I/r^2}$
- id: d
  content: |-
    $a=\dfrac{(m_2-m_1)g}{m_1+m_2}$
- id: e
  content: |-
    $a=\dfrac{(m_2-m_1+I/r^2)g}{m_1+m_2}$
feedback: |-
  The torque equation contributes the positive effective-inertia term $I/r^2$ to the denominator. It does not change the gravitational driving force $(m_2-m_1)g$.
```

---

<a id="compare-the-two-denominators"></a>
## Compare the Two Denominators

**Example:** Compare the acceleration with a massless pulley to the acceleration with a pulley for which $I/r^2=M$, where $M>0$.

**Explanation**

Both accelerations have the same positive numerator $N=(m_2-m_1)g$. Write them as

$$
a_A=\frac{N}{m_1+m_2}
$$

and

$$
a_B=\frac{N}{m_1+m_2+M}.
$$

Since $M>0$, the denominator of $a_B$ is larger. A positive fraction becomes smaller when its denominator increases while its numerator stays fixed. Hence

$$
a_B<a_A.
$$

The same conclusion appears directly from their ratio:

$$
\frac{a_B}{a_A}
=\frac{m_1+m_2}{m_1+m_2+I/r^2}<1.
$$

As a limiting check, setting $I=0$ in the massive-pulley formula recovers the massless-pulley result.

```quiz
type: radio
id: m2-5-p1-denominator-comparison
content: |-
  Two accelerations have the forms $a_0=N/D$ and $a_1=N/(D+q)$, where $N>0$, $D>0$, and $q>0$. Which comparison is correct?
options:
- id: a
  content: |-
    $a_1<a_0$
  correct: true
- id: b
  content: |-
    $a_1>a_0$
- id: c
  content: |-
    $a_1=a_0$
- id: d
  content: |-
    $a_1=0$
- id: e
  content: |-
    The comparison cannot be determined.
feedback: |-
  The numerator is unchanged and positive, while $D+q>D$. The larger positive denominator makes $a_1$ smaller.
```

---

<a id="distinguish-frictionless-from-massless"></a>
## Distinguish Frictionless From Massless

**Example:** A pulley has a frictionless axle but a nonzero moment of inertia. Must the tensions on the two sides of its string be equal?

**Explanation**

No. A frictionless axle means the axle contributes negligible resisting torque. The pulley still needs a net torque to acquire angular acceleration, so

$$
(T_2-T_1)r=I\alpha.
$$

When $I>0$ and $\alpha\ne0$, the tension difference is nonzero. Equal tensions are appropriate for the ideal massless pulley because $I=0$, not merely because the bearing is frictionless.

```quiz
type: radio
id: m2-5-p1-frictionless-vs-massless
content: |-
  A pulley rotates on a frictionless bearing and has $I>0$. The system accelerates without the string slipping. Which statement is true?
options:
- id: a
  content: |-
    The string tensions differ so that they provide the pulley a net torque.
  correct: true
- id: b
  content: |-
    The string tensions must be equal because the bearing is frictionless.
- id: c
  content: |-
    The pulley has no angular acceleration.
- id: d
  content: |-
    The pulley's moment of inertia has no effect on the motion.
- id: e
  content: |-
    The pulley adds its full weight to the hanging driving force.
feedback: |-
  Frictionless describes the bearing torque, not the pulley's inertia. A massive accelerating pulley requires $(T_2-T_1)r=I\alpha$, so the tensions differ.
```

---

<a id="apply-the-comparison"></a>
## Apply the Comparison

**Example:** Compare two otherwise identical Atwood machines when System A has a massless pulley and System B has a massive pulley.

**Explanation**

The image confirms that the hanging masses are the same in both systems; the filled pulley in System B is the only dynamical change. Its inertia must therefore change the denominator, not the gravitational numerator.

The same mass difference supplies the numerator in both cases. System B has the additional positive denominator term $I/r^2$:

$$
a_A=\frac{(m_2-m_1)g}{m_1+m_2},
\qquad
a_B=\frac{(m_2-m_1)g}{m_1+m_2+I/r^2}.
$$

Thus $a_B<a_A$: the heavier mass has a greater acceleration magnitude in System A.

```quiz
type: radio
id: m2-5pre-q1
shuffle: true
content: |-
  **Question 1**

  In both systems, $m_2>m_1$ and the masses are connected by a massless string. System A has a massless, frictionless pulley. System B is identical except that its pulley has mass.

  Which statement is true?

  ![](<../Source/Images/massless-vs-massive-pulley-systems.png>)
options:
- id: a
  content: |-
    The magnitude of the acceleration of $m_2$ is greater in System A than in System B.
  correct: true
  feedback: |-
    In System B, some of the gravitational energy goes into rotating the massive pulley. Equivalently, its rotational inertia adds resistance to the motion:

    $$
    a_A=\frac{(m_2-m_1)g}{m_1+m_2},
    $$

    $$
    a_B=\frac{(m_2-m_1)g}{m_1+m_2+\dfrac{I}{r^2}}.
    $$

    Because $I/r^2>0$, the acceleration satisfies $a_B<a_A$.
- id: b
  content: |-
    The magnitude of the acceleration of $m_2$ is less in System A than in System B.
- id: c
  content: |-
    The magnitude of the acceleration of $m_2$ is the same in both systems.
```

---

<a id="summary"></a>
## Summary

- **Cue:** the hanging masses are unchanged, but one pulley has rotational inertia.
- **Driving force:** $(m_2-m_1)g$ is the same in both systems.
- **Pulley effect:** no slip and $\tau=I\alpha$ contribute the positive effective inertia $I/r^2$.
- **Comparison:** the same numerator over a larger denominator gives a smaller acceleration.
- **Ratio check:** $a_B/a_A=(m_1+m_2)/(m_1+m_2+I/r^2)<1$.
- **Conclusion:** $a_B<a_A$.
- **Main trap:** a frictionless bearing does not make a massive pulley behave like a massless pulley.
