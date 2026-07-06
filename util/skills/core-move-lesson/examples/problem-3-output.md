# Finding the Units of a Coefficient in Angular Acceleration

## Table of Contents

- [Introduction](#introduction)
- [Matching Units in a Sum](#matching-units-in-a-sum)
- [Dividing Out a Time Power](#dividing-out-a-time-power)
- [Distinguishing the Coefficient From the Constant Term](#distinguishing-the-coefficient-from-the-constant-term)

## Prerequisites

- SI units for angular acceleration
- Powers of time units, such as $[t^2]=\mathrm{s}^2$
- Matching units across terms that are added

---

<a id="introduction"></a>
## Introduction

Suppose the $z$-component of angular acceleration is

$$
\alpha_z(t)=Bt^2+C.
$$

The core move is to match the units of each term on the right to the units of $\alpha_z(t)$, then divide out the units contributed by $t^2$.

---

<a id="matching-units-in-a-sum"></a>
## Matching Units in a Sum

**Example:** Suppose $a(t)=Kt+a_0$, where $a(t)$ has units $\mathrm{m}/\mathrm{s}^2$. What are the units of $K$?

**Explanation**

Since $Kt$ is added to make $a(t)$, it must have units $\mathrm{m}/\mathrm{s}^2$. Because $[t]=\mathrm{s}$,

$$
[K]\mathrm{s}=\frac{\mathrm{m}}{\mathrm{s}^2},
$$

so

$$
[K]=\frac{\mathrm{m}}{\mathrm{s}^3}.
$$

```quiz
type: radio
id: q-1
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

---

<a id="dividing-out-a-time-power"></a>
## Dividing Out a Time Power

**Example:** Suppose $\omega(t)=Dt^3+\omega_0$, where $\omega(t)$ has units $\mathrm{rad}/\mathrm{s}$. What are the units of $D$?

**Explanation**

The product $Dt^3$ must have units $\mathrm{rad}/\mathrm{s}$. Since $[t^3]=\mathrm{s}^3$,

$$
[D]\mathrm{s}^3=\frac{\mathrm{rad}}{\mathrm{s}},
$$

so

$$
[D]=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

```quiz
type: radio
id: q-2
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

---

<a id="distinguishing-the-coefficient-from-the-constant-term"></a>
## Distinguishing the Coefficient From the Constant Term

**Example:** In $\alpha_z(t)=Bt^2+C$, find the units of $B$.

**Explanation**

Angular acceleration has units $\mathrm{rad}/\mathrm{s}^2$. The whole product $Bt^2$ must have those units:

$$
[B]\mathrm{s}^2=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

Therefore,

$$
[B]=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

```quiz
type: radio
id: q-3
content: |-
  The $z$-component of angular acceleration is $\alpha_z(t)=Bt^2+C$. What SI units is $B$ measured in?
options:
- id: a
  content: |-
    $\mathrm{m}/\mathrm{s}^2$
- id: b
  content: |-
    $\mathrm{m}/\mathrm{s}^3$
- id: c
  content: |-
    $\mathrm{m}/\mathrm{s}^4$
- id: d
  content: |-
    $\mathrm{rad}/\mathrm{s}^2$
- id: e
  content: |-
    $\mathrm{rad}/\mathrm{s}^3$
- id: f
  content: |-
    $\mathrm{rad}/\mathrm{s}^4$
  correct: true
```

## Summary

When terms are added, their units must match. For $\alpha_z(t)=Bt^2+C$, the product $Bt^2$ has units $\mathrm{rad}/\mathrm{s}^2$, so $B$ must have units $\mathrm{rad}/\mathrm{s}^4$.
