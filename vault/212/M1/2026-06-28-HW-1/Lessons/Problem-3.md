# Finding the Units of a Coefficient in Angular Acceleration

<!--
lesson-id: 212-M1-045
topic-code: MTH212.M1.45
-->

## Table of Contents

- [Introduction](#introduction)
- [Matching Units in a Sum](#matching-units-in-a-sum)
- [Dividing Out a Time Power](#dividing-out-a-time-power)
- [Distinguishing the Coefficient From the Constant Term](#distinguishing-the-coefficient-from-the-constant-term)
- [Checking Variants of the Same Move](#checking-variants-of-the-same-move)

## Prerequisites

- SI units for angular position, angular velocity, and angular acceleration
- Powers of time units, such as $[t^2]=\mathrm{s}^2$
- Matching units across terms that are added or subtracted

---

<a id="introduction"></a>
## Introduction

Suppose the $z$-component of angular acceleration is given by

$$
\alpha_z(t)=Bt^2+C.
$$

The question is: what SI units does $B$ have?

The core move is to make the units of each term match the units of the left-hand side. Since $\alpha_z(t)$ is angular acceleration,

$$
[\alpha_z]=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

The term $Bt^2$ must also have units $\mathrm{rad}/\mathrm{s}^2$. Since $t^2$ contributes $\mathrm{s}^2$, the coefficient $B$ must supply the remaining units:

$$
[B]\mathrm{s}^2=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

Therefore,

$$
[B]=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

---

<a id="matching-units-in-a-sum"></a>
## Matching Units in a Sum

**Example:** Suppose

$$
a(t)=Kt+a_0,
$$

where $a(t)$ is linear acceleration. What are the units of $K$?

**Explanation**

The left-hand side is acceleration, so

$$
[a(t)]=\frac{\mathrm{m}}{\mathrm{s}^2}.
$$

Because $Kt$ and $a_0$ are added to make $a(t)$, each term must have units of acceleration:

$$
[Kt]=\frac{\mathrm{m}}{\mathrm{s}^2}.
$$

Since $[t]=\mathrm{s}$,

$$
[K]\mathrm{s}=\frac{\mathrm{m}}{\mathrm{s}^2}.
$$

Divide by $\mathrm{s}$:

$$
[K]=\frac{\mathrm{m}}{\mathrm{s}^3}.
$$

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  If $v(t)=At+v_0$ and $v(t)$ has units $\mathrm{m}/\mathrm{s}$, what are the units of $A$?
options:
- id: a
  content: |-
    $\mathrm{m}$
- id: b
  content: |-
    $\mathrm{m}/\mathrm{s}$
- id: c
  content: |-
    $\mathrm{m}/\mathrm{s}^2$
  correct: true
- id: d
  content: |-
    $\mathrm{m}/\mathrm{s}^3$
- id: e
  content: |-
    $\mathrm{s}/\mathrm{m}$
```

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  If $x(t)=Pt+x_0$ and $x(t)$ has units $\mathrm{m}$, what are the units of $P$?
options:
- id: a
  content: |-
    $\mathrm{m}$
- id: b
  content: |-
    $\mathrm{m}/\mathrm{s}$
  correct: true
- id: c
  content: |-
    $\mathrm{m}/\mathrm{s}^2$
- id: d
  content: |-
    $\mathrm{s}/\mathrm{m}$
- id: e
  content: |-
    $\mathrm{m}\cdot\mathrm{s}$
```

---

<a id="dividing-out-a-time-power"></a>
## Dividing Out a Time Power

**Example:** Suppose

$$
\omega(t)=Dt^3+\omega_0,
$$

where $\omega(t)$ is angular velocity. What are the units of $D$?

**Explanation**

Angular velocity has units

$$
[\omega]=\frac{\mathrm{rad}}{\mathrm{s}}.
$$

Therefore, the term $Dt^3$ must have units $\mathrm{rad}/\mathrm{s}$:

$$
[Dt^3]=\frac{\mathrm{rad}}{\mathrm{s}}.
$$

Since $[t^3]=\mathrm{s}^3$,

$$
[D]\mathrm{s}^3=\frac{\mathrm{rad}}{\mathrm{s}}.
$$

Divide by $\mathrm{s}^3$:

$$
[D]=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  If $\theta(t)=Et^2+\theta_0$ and $\theta(t)$ has units $\mathrm{rad}$, what are the units of $E$?
options:
- id: a
  content: |-
    $\mathrm{rad}$
- id: b
  content: |-
    $\mathrm{rad}/\mathrm{s}$
- id: c
  content: |-
    $\mathrm{rad}/\mathrm{s}^2$
  correct: true
- id: d
  content: |-
    $\mathrm{rad}/\mathrm{s}^3$
- id: e
  content: |-
    $\mathrm{rad}\cdot\mathrm{s}^2$
```

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  If $\omega_z(t)=Gt^4+\omega_0$ and $\omega_z(t)$ has units $\mathrm{rad}/\mathrm{s}$, what are the units of $G$?
options:
- id: a
  content: |-
    $\mathrm{rad}/\mathrm{s}$
- id: b
  content: |-
    $\mathrm{rad}/\mathrm{s}^2$
- id: c
  content: |-
    $\mathrm{rad}/\mathrm{s}^4$
- id: d
  content: |-
    $\mathrm{rad}/\mathrm{s}^5$
  correct: true
- id: e
  content: |-
    $\mathrm{rad}\cdot\mathrm{s}^3$
```

---

<a id="distinguishing-the-coefficient-from-the-constant-term"></a>
## Distinguishing the Coefficient From the Constant Term

**Example:** Suppose

$$
\alpha_z(t)=Bt^2+C.
$$

What are the units of $B$?

**Explanation**

The left-hand side is angular acceleration, so

$$
[\alpha_z]=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

The constant term $C$ is added directly, so

$$
[C]=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

But $B$ is not added directly. The whole product $Bt^2$ is added, so

$$
[Bt^2]=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

Since $[t^2]=\mathrm{s}^2$,

$$
[B]\mathrm{s}^2=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

Therefore,

$$
[B]=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

So the correct SI units for $B$ are

$$
\boxed{\mathrm{rad}/\mathrm{s}^4}.
$$

```quiz
type: radio
id: q-5
shuffle: true
content: |-
  In $\alpha_z(t)=Bt^2+C$, which unit belongs to $C$?
options:
- id: a
  content: |-
    $\mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $\mathrm{m}/\mathrm{s}^4$
- id: c
  content: |-
    $\mathrm{rad}/\mathrm{s}^2$
  correct: true
- id: d
  content: |-
    $\mathrm{rad}/\mathrm{s}^3$
- id: e
  content: |-
    $\mathrm{rad}/\mathrm{s}^4$
```

```quiz
type: radio
id: q-6
shuffle: true
content: |-
  In $\alpha_z(t)=Bt^2+C$, why is $B$ not measured in $\mathrm{rad}/\mathrm{s}^2$?
options:
- id: a
  content: |-
    Because radians are not SI units
- id: b
  content: |-
    Because $B$ multiplies $t^2$, so $B$ must include two extra powers of $1/\mathrm{s}$
  correct: true
- id: c
  content: |-
    Because $C$ has no units
- id: d
  content: |-
    Because angular acceleration is measured in meters per second squared
- id: e
  content: |-
    Because $t^2$ has units $\mathrm{rad}^2$
```

---

<a id="checking-variants-of-the-same-move"></a>
## Checking Variants of the Same Move

The same procedure works for any formula of the form

$$
q(t)=At^n+\text{other terms}.
$$

If $q(t)$ has units $[q]$, then

$$
[A]\,\mathrm{s}^n=[q],
$$

so

$$
[A]=\frac{[q]}{\mathrm{s}^n}.
$$

```quiz
type: radio
id: q-7
shuffle: true
content: |-
  If $\alpha(t)=Ht+\alpha_0$ and $\alpha(t)$ has units $\mathrm{rad}/\mathrm{s}^2$, what are the units of $H$?
options:
- id: a
  content: |-
    $\mathrm{rad}/\mathrm{s}$
- id: b
  content: |-
    $\mathrm{rad}/\mathrm{s}^2$
- id: c
  content: |-
    $\mathrm{rad}/\mathrm{s}^3$
  correct: true
- id: d
  content: |-
    $\mathrm{rad}/\mathrm{s}^4$
- id: e
  content: |-
    $\mathrm{m}/\mathrm{s}^3$
```

```quiz
type: radio
id: q-8
shuffle: true
content: |-
  If $\alpha_z(t)=Et^4+F$ and $\alpha_z(t)$ has units $\mathrm{rad}/\mathrm{s}^2$, what are the units of $E$?
options:
- id: a
  content: |-
    $\mathrm{rad}/\mathrm{s}^2$
- id: b
  content: |-
    $\mathrm{rad}/\mathrm{s}^4$
- id: c
  content: |-
    $\mathrm{rad}/\mathrm{s}^5$
- id: d
  content: |-
    $\mathrm{rad}/\mathrm{s}^6$
  correct: true
- id: e
  content: |-
    $\mathrm{m}/\mathrm{s}^6$
```

---

## Summary

When terms are added, their units must match.

For

$$
\alpha_z(t)=Bt^2+C,
$$

the left-hand side has units $\mathrm{rad}/\mathrm{s}^2$. The product $Bt^2$ must have those same units:

$$
[B]\mathrm{s}^2=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

Dividing by $\mathrm{s}^2$ gives

$$
[B]=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

The answer is

$$
\boxed{\mathrm{rad}/\mathrm{s}^4}.
$$

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
