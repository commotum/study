# Finding Angular Speed from Angular Momentum

<!--
lesson-id: 212-M2-049
topic-code: MTH212.M2.49
-->

## Table of Contents

- [Introduction](#introduction)
- [Connect Angular Momentum and Angular Speed](#connect-angular-momentum-and-angular-speed)
- [Isolate Angular Speed](#isolate-angular-speed)
- [Check Units and Dependence](#check-units-and-dependence)
- [Apply the Rule to the Rod–Ball Collision](#apply-the-rule-to-the-rodball-collision)
- [Summary](#summary)

## Prerequisites

- Recognize angular momentum magnitude $L$ and moment of inertia $I$ about a specified axis.
- Divide both sides of a symbolic equation by the same nonzero quantity.

---

<a id="introduction"></a>
## Introduction

When a problem asks for angular speed and gives the angular momentum magnitude and moment of inertia about the same rotation axis, use

$$
L=I\omega.
$$

The reusable move is to divide the angular momentum magnitude by the moment of inertia:

$$
\omega=\frac{L}{I}.
$$

This is the recognition cue: **known $L$, known $I$, requested $\omega$**. Do not restart the collision analysis if $L$ and $I$ have already been found.

Here $L$ denotes the magnitude, so the result is the nonnegative angular speed. A vector direction would instead describe the direction of the angular velocity. The relation also requires $L$ and $I$ to refer to the same axis.

---

<a id="connect-angular-momentum-and-angular-speed"></a>
## Connect Angular Momentum and Angular Speed

**Example:** A rigid system has angular momentum magnitude $L=12\,\mathrm{kg}\,\mathrm{m}^2/\mathrm{s}$ and moment of inertia $I=3\,\mathrm{kg}\,\mathrm{m}^2$ about its rotation axis. Find its angular speed.

**Explanation**

Use $L=I\omega$ for the same axis, then divide by $I$:

$$
\omega=\frac{L}{I}
=\frac{12\,\mathrm{kg}\,\mathrm{m}^2/\mathrm{s}}{3\,\mathrm{kg}\,\mathrm{m}^2}
=4\,\mathrm{rad}/\mathrm{s}.
$$

Multiplying back checks the result:

$$
I\omega=(3)(4)=12=L.
$$

```quiz
type: radio
id: p13-connect-q1
content: |-
  A rotating system has angular momentum magnitude $18\,\mathrm{kg}\,\mathrm{m}^2/\mathrm{s}$ and moment of inertia $6\,\mathrm{kg}\,\mathrm{m}^2$ about the same axis. What is its angular speed?
options:
- id: a
  content: |-
    $3\,\mathrm{rad}/\mathrm{s}$
  correct: true
- id: b
  content: |-
    $108\,\mathrm{rad}/\mathrm{s}$
- id: c
  content: |-
    $\frac{1}{3}\,\mathrm{rad}/\mathrm{s}$
- id: d
  content: |-
    $12\,\mathrm{rad}/\mathrm{s}$
```

---

<a id="isolate-angular-speed"></a>
## Isolate Angular Speed

**Example:** An earlier calculation gives angular momentum magnitude $L_0$ and moment of inertia $I_0$. Make $\omega$ the subject of the rotational relation.

**Explanation**

Treat $L_0$ and $I_0$ as constants because $\omega$ is the quantity being isolated. Starting with the rotational relation,

$$
L_0=I_0\omega,
$$

divide both sides by $I_0$:

$$
\frac{L_0}{I_0}
=\frac{I_0\omega}{I_0}
=\omega.
$$

Therefore,

$$
\boxed{\omega=\frac{L_0}{I_0}}.
$$

```quiz
type: radio
id: p13-isolate-q1
content: |-
  If $J=K\Omega$, where $J$ and $K$ are known and $K\ne 0$, which expression gives $\Omega$?
options:
- id: a
  content: |-
    $\Omega=\dfrac{J}{K}$
  correct: true
- id: b
  content: |-
    $\Omega=JK$
- id: c
  content: |-
    $\Omega=\dfrac{K}{J}$
- id: d
  content: |-
    $\Omega=J-K$
```

---

<a id="check-units-and-dependence"></a>
## Check Units and Dependence

**Example:** At fixed angular momentum magnitude, the moment of inertia doubles. What happens to the angular speed?

**Explanation**

Since

$$
\omega=\frac{L}{I},
$$

doubling $I$ while holding $L$ fixed cuts $\omega$ in half. This inverse dependence is a useful check: a larger inertia belongs in the denominator.

The units also reduce correctly:

$$
\frac{\mathrm{kg}\,\mathrm{m}^2/\mathrm{s}}{\mathrm{kg}\,\mathrm{m}^2}
=\frac{1}{\mathrm{s}},
$$

which is written as $\mathrm{rad}/\mathrm{s}$ for angular speed.

```quiz
type: radio
id: p13-check-q1
content: |-
  Two systems have the same angular momentum magnitude. System B has three times the moment of inertia of system A. How do their angular speeds compare?
options:
- id: a
  content: |-
    $\omega_B=3\omega_A$
- id: b
  content: |-
    $\omega_B=\dfrac{\omega_A}{3}$
  correct: true
- id: c
  content: |-
    $\omega_B=\omega_A$
- id: d
  content: |-
    $\omega_B=\omega_A-3$
```

---

<a id="apply-the-rule-to-the-rodball-collision"></a>
## Apply the Rule to the Rod–Ball Collision

**Example:** A ball sticks to a rod. After the collision, the combined system has angular momentum magnitude $L_0$ and moment of inertia $I_0$ about its rotation axis. Find its angular speed.

**Explanation**

The collision details were used to obtain $L_0$ and $I_0$. Once those results are known, no additional collision factor is needed. Substitute them directly into $L=I\omega$:

$$
L_0=I_0\omega
\qquad\Longrightarrow\qquad
\boxed{\omega=\frac{L_0}{I_0}}.
$$

The alternative $L_0/(3I_0)$ inserts an unexplained extra factor of $3$. Nothing in $L_0=I_0\omega$ produces that factor.

```quiz
type: radio
id: p13-application-q1
content: |-
  A thin uniform rod of mass $m$ and length $L$ is initially at rest in outer space. A nonspinning uniform ball of mass $m/2$ and radius $r$ strikes one end of the rod with speed $v$ and sticks to it.

  Let the magnitude of the angular momentum from the previous question be $L_0$, and let the moment of inertia from the question before that be $I_0$.

  What is the angular speed of the combined system about its rotation axis after the collision?

  ![](<../Source/2026-07-15-HW-4/Images/rod-ball-inelastic-collision.png>)
options:
- id: a
  content: |-
    $\dfrac{L_0}{3I_0}$
- id: b
  content: |-
    $\dfrac{L_0}{I_0}$
  correct: true
```

---

<a id="summary"></a>
## Summary

- **Cue:** The angular momentum magnitude and moment of inertia are known about the same axis, and the question asks for angular speed.
- **Rule:** Start with $L=I\omega$.
- **Procedure:** Divide by the nonzero moment of inertia: $\omega=L/I$.
- **Checks:** The units reduce to $1/\mathrm{s}$, and at fixed $L$, a larger $I$ gives a smaller $\omega$.
- **Main trap:** Do not insert an extra mass factor or collision factor after $L_0$ and $I_0$ have already been calculated.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
