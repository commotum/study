# Finding Angular Velocity From Angular Acceleration

<!--
lesson-id: 212-M1-046
topic-code: MTH212.M1.46
-->

## Table of Contents

- [Introduction](#introduction)
- [Integrating Angular Acceleration](#integrating-angular-acceleration)
- [Separating Given Constants From the Integration Constant](#separating-given-constants-from-the-integration-constant)
- [Using the Initial Angular Velocity](#using-the-initial-angular-velocity)
- [Matching the Homework Form](#matching-the-homework-form)
- [Summary](#summary)

## Prerequisites

- Angular acceleration is the time derivative of angular velocity: $\alpha_z(t)=\dfrac{\mathrm{d}\omega_z}{\mathrm{d}t}$
- The power rule for integration: $\displaystyle \int t^n\,\mathrm{d}t=\dfrac{t^{n+1}}{n+1}+K$ for $n\neq -1$
- The integral of a constant $c$ with respect to $t$ is $ct$
- An initial condition is used by substituting the given time into the general formula

---

<a id="introduction"></a>
## Introduction

The problem gives angular acceleration,

$$
\alpha_z(t)=Bt^2+C,
$$

and asks for angular velocity $\omega_z(t)$, with

$$
\omega_z(0\ \mathrm{s})=\omega_0.
$$

The recognition cue is: acceleration is given, velocity is requested, and an initial velocity is supplied. That means integrate angular acceleration with respect to time, then use the initial condition to find the integration constant.

Because

$$
\alpha_z(t)=\frac{\mathrm{d}\omega_z}{\mathrm{d}t},
$$

we reverse that derivative:

$$
\omega_z(t)=\int \alpha_z(t)\,\mathrm{d}t.
$$

---

<a id="integrating-angular-acceleration"></a>
## Integrating Angular Acceleration

**Example:** Suppose

$$
\alpha_z(t)=6t^2+4.
$$

Find the general formula for $\omega_z(t)$.

**Explanation**

Integrate each term of $\alpha_z(t)$ with respect to $t$:

$$
\omega_z(t)=\int (6t^2+4)\,\mathrm{d}t.
$$

For the power term, increase the exponent from $2$ to $3$ and divide by $3$:

$$
\int 6t^2\,\mathrm{d}t=6\cdot \frac{t^3}{3}=2t^3.
$$

For the constant term, multiply by $t$:

$$
\int 4\,\mathrm{d}t=4t.
$$

Add an integration constant, written here as $K$:

$$
\omega_z(t)=2t^3+4t+K.
$$

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  If $\alpha_z(t)=9t^2-5$, what is the general formula for $\omega_z(t)$?
options:
- id: a
  content: |-
    $\omega_z(t)=18t-5+K$
- id: b
  content: |-
    $\omega_z(t)=3t^3-5t+K$
  correct: true
- id: c
  content: |-
    $\omega_z(t)=9t^3-5t+K$
- id: d
  content: |-
    $\omega_z(t)=3t^3-5+K$
- id: e
  content: |-
    $\omega_z(t)=3t^3-5t$
```

---

<a id="separating-given-constants-from-the-integration-constant"></a>
## Separating Given Constants From the Integration Constant

**Example:** Suppose

$$
\alpha_z(t)=At^2+D,
$$

where $A$ and $D$ are constants. Find the general formula for $\omega_z(t)$.

**Explanation**

Treat $A$ and $D$ as fixed coefficients while integrating with respect to $t$:

$$
\omega_z(t)=\int (At^2+D)\,\mathrm{d}t.
$$

The coefficient $A$ stays attached to the power term:

$$
\int At^2\,\mathrm{d}t=A\cdot \frac{t^3}{3}=\frac{A}{3}t^3.
$$

The constant term $D$ becomes $Dt$:

$$
\int D\,\mathrm{d}t=Dt.
$$

Then add the integration constant $K$:

$$
\omega_z(t)=\frac{A}{3}t^3+Dt+K.
$$

The given constant in the acceleration formula is not the same thing as the integration constant. In this lesson, the integration constant is called $K$ to keep the roles separate.

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  If $\alpha_z(t)=Pt^2+Q$, where $P$ and $Q$ are constants, what is the general formula for $\omega_z(t)$?
options:
- id: a
  content: |-
    $\omega_z(t)=2Pt+K$
- id: b
  content: |-
    $\omega_z(t)=\dfrac{P}{3}t^3+Qt+K$
  correct: true
- id: c
  content: |-
    $\omega_z(t)=Pt^3+Qt^2+K$
- id: d
  content: |-
    $\omega_z(t)=\dfrac{P}{3}t^3+Q+K$
- id: e
  content: |-
    $\omega_z(t)=\dfrac{P}{3}t^3+Qt$
```

---

<a id="using-the-initial-angular-velocity"></a>
## Using the Initial Angular Velocity

**Example:** Suppose

$$
\alpha_z(t)=12t^2-3
$$

and

$$
\omega_z(0)=\omega_0.
$$

Find $\omega_z(t)$.

**Explanation**

First integrate the angular acceleration:

$$
\omega_z(t)=\int (12t^2-3)\,\mathrm{d}t=4t^3-3t+K.
$$

Now use the initial condition. Substitute $t=0$ and $\omega_z(0)=\omega_0$:

$$
\omega_0=4(0)^3-3(0)+K.
$$

The terms with $t$ become $0$, so

$$
K=\omega_0.
$$

Therefore,

$$
\omega_z(t)=4t^3-3t+\omega_0.
$$

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  If $\alpha_z(t)=6t^2+8$ and $\omega_z(0)=\omega_0$, what is $\omega_z(t)$?
options:
- id: a
  content: |-
    $\omega_z(t)=12t+8+\omega_0$
- id: b
  content: |-
    $\omega_z(t)=2t^3+8t+\omega_0$
  correct: true
- id: c
  content: |-
    $\omega_z(t)=2t^3+8+\omega_0$
- id: d
  content: |-
    $\omega_z(t)=2t^3+8t+\omega_0t$
- id: e
  content: |-
    $\omega_z(t)=6t^3+8t+\omega_0$
```

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  If $\alpha_z(t)=3t^2-10$ and $\omega_z(0)=7$, what is $\omega_z(t)$?
options:
- id: a
  content: |-
    $\omega_z(t)=6t-10+7$
- id: b
  content: |-
    $\omega_z(t)=t^3-10t+7$
  correct: true
- id: c
  content: |-
    $\omega_z(t)=t^3-10t+7t$
- id: d
  content: |-
    $\omega_z(t)=t^3-10+7$
- id: e
  content: |-
    $\omega_z(t)=3t^3-10t+7$
```

---

<a id="matching-the-homework-form"></a>
## Matching the Homework Form

**Example:** For the homework problem,

$$
\alpha_z(t)=Bt^2+C
$$

and

$$
\omega_z(0\ \mathrm{s})=\omega_0.
$$

Find $\omega_z(t)$.

**Explanation**

Integrate the angular acceleration term by term:

$$
\omega_z(t)=\int (Bt^2+C)\,\mathrm{d}t.
$$

The $Bt^2$ term becomes

$$
\frac{B}{3}t^3.
$$

The constant acceleration term $C$ becomes

$$
Ct.
$$

So the general form is

$$
\omega_z(t)=\frac{B}{3}t^3+Ct+K.
$$

Use $\omega_z(0\ \mathrm{s})=\omega_0$:

$$
\omega_0=\frac{B}{3}(0)^3+C(0)+K.
$$

Thus,

$$
K=\omega_0.
$$

Therefore,

$$
\omega_z(t)=\frac{B}{3}t^3+Ct+\omega_0.
$$

The most common traps are forgetting the factor $\dfrac{1}{3}$, leaving $C$ as a constant instead of integrating it to $Ct$, or writing $\omega_0t$ even though the initial angular velocity becomes the constant term.

You can check the answer two ways:

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{B}{3}t^3+Ct+\omega_0\right)=Bt^2+C
$$

and

$$
\omega_z(0)=\frac{B}{3}(0)^3+C(0)+\omega_0=\omega_0.
$$

```quiz
type: radio
id: q-5
shuffle: true
content: |-
  The $z$-component of the angular acceleration of an object moving along a circular trajectory has $\alpha_z(t)=Bt^2+C$, where $B$ and $C$ are constants of the appropriate dimension.

  Let $\omega_z(t)$ denote the $z$-component of the object's angular velocity. If $\omega_z(0\ \mathrm{s})=\omega_0$, what is $\omega_z(t)$?
options:
- id: a
  content: |-
    $Bt^3+Ct^2+\omega_0t$
- id: b
  content: |-
    $Bt^3+Ct+\omega_0$
- id: c
  content: |-
    $2Bt+\omega_0$
- id: d
  content: |-
    $2Bt$
- id: e
  content: |-
    $\dfrac{B}{3}t^3+Ct+\omega_0$
  correct: true
- id: f
  content: |-
    $\dfrac{B}{3}t^3+Ct+\omega_0t$
```

---

<a id="summary"></a>
## Summary

When angular acceleration is given and angular velocity is requested, integrate with respect to time:

$$
\omega_z(t)=\int \alpha_z(t)\,\mathrm{d}t.
$$

For

$$
\alpha_z(t)=Bt^2+C,
$$

the antiderivative is

$$
\omega_z(t)=\frac{B}{3}t^3+Ct+K.
$$

Then substitute the initial condition. If $\omega_z(0)=\omega_0$, the $t$-terms vanish and $K=\omega_0$, so

$$
\omega_z(t)=\frac{B}{3}t^3+Ct+\omega_0.
$$

The key trap is mixing up constants: the given $C$ in $\alpha_z(t)$ integrates to $Ct$, while the initial angular velocity determines the separate integration constant.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
