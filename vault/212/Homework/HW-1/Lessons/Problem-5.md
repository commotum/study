# Finding Angular Position From Angular Acceleration

## Table of Contents

- [Introduction](#introduction)
- [Integrating Acceleration to Velocity](#integrating-acceleration-to-velocity)
- [Integrating Velocity to Position](#integrating-velocity-to-position)
- [Using Initial Conditions](#using-initial-conditions)
- [Keeping the Coefficients Straight](#keeping-the-coefficients-straight)
- [Matching the Requested Formula](#matching-the-requested-formula)

## Prerequisites

- The relationships $\alpha_z(t)=\dfrac{d\omega_z}{dt}$ and $\omega_z(t)=\dfrac{d\theta_z}{dt}$
- The power rule for integration
- How an initial condition determines an integration constant

---

<a id="introduction"></a>
## Introduction

When angular acceleration is given as a function of time and the question asks for angular position, use the derivative chain in reverse. Look for two cues:

- $\alpha_z(t)$ is provided.
- $\theta_z(t)$ is requested.

That means you must integrate twice:

$$
\alpha_z(t)\longrightarrow \omega_z(t)\longrightarrow \theta_z(t).
$$

Each integration creates one constant. The initial angular velocity fixes the velocity constant, and the initial angular position fixes the position constant.

---

<a id="integrating-acceleration-to-velocity"></a>
## Integrating Acceleration to Velocity

**Example:** Suppose

$$
\alpha_z(t)=6t^2+4
$$

and $\omega_z(0)=\omega_0$. Find $\omega_z(t)$.

**Explanation**

Since angular acceleration is the derivative of angular velocity,

$$
\omega_z(t)=\int \alpha_z(t)\,dt.
$$

Integrate each term:

$$
\omega_z(t)=\int (6t^2+4)\,dt=2t^3+4t+K.
$$

Use $\omega_z(0)=\omega_0$:

$$
\omega_0=2(0)^3+4(0)+K,
$$

so $K=\omega_0$. Therefore,

$$
\omega_z(t)=2t^3+4t+\omega_0.
$$

```quiz
type: radio
id: q-1
content: |-
  Suppose $\alpha_z(t)=9t^2+5$ and $\omega_z(0)=\omega_0$. What is $\omega_z(t)$?
options:
- id: a
  content: |-
    $9t^3+5t+\omega_0$
- id: b
  content: |-
    $3t^3+5t+\omega_0$
  correct: true
- id: c
  content: |-
    $18t+5+\omega_0$
- id: d
  content: |-
    $3t^3+5+\omega_0t$
- id: e
  content: |-
    $9t^2+5+\omega_0$
```

---

<a id="integrating-velocity-to-position"></a>
## Integrating Velocity to Position

**Example:** Suppose

$$
\omega_z(t)=2t^3+4t+\omega_0
$$

and $\theta_z(0)=\theta_0$. Find $\theta_z(t)$.

**Explanation**

Since angular velocity is the derivative of angular position,

$$
\theta_z(t)=\int \omega_z(t)\,dt.
$$

Integrate each term:

$$
\theta_z(t)=\int (2t^3+4t+\omega_0)\,dt
=\frac{1}{2}t^4+2t^2+\omega_0t+L.
$$

Use $\theta_z(0)=\theta_0$:

$$
\theta_0=\frac{1}{2}(0)^4+2(0)^2+\omega_0(0)+L,
$$

so $L=\theta_0$. Therefore,

$$
\theta_z(t)=\frac{1}{2}t^4+2t^2+\omega_0t+\theta_0.
$$

```quiz
type: radio
id: q-2
content: |-
  Suppose $\omega_z(t)=3t^3+5t+\omega_0$ and $\theta_z(0)=\theta_0$. What is $\theta_z(t)$?
options:
- id: a
  content: |-
    $3t^4+5t^2+\omega_0t+\theta_0$
- id: b
  content: |-
    $\dfrac{3}{4}t^4+\dfrac{5}{2}t^2+\omega_0t+\theta_0$
  correct: true
- id: c
  content: |-
    $\dfrac{3}{4}t^4+\dfrac{5}{2}t^2+\omega_0+\theta_0$
- id: d
  content: |-
    $9t^2+5+\theta_0$
- id: e
  content: |-
    $\dfrac{3}{4}t^4+\dfrac{5}{2}t^2$
```

---

<a id="using-initial-conditions"></a>
## Using Initial Conditions

**Example:** Suppose

$$
\alpha_z(t)=At+C,
$$

with $\omega_z(0)=\omega_0$ and $\theta_z(0)=\theta_0$. Find $\theta_z(t)$.

**Explanation**

First integrate acceleration to get velocity:

$$
\omega_z(t)=\int (At+C)\,dt=\frac{A}{2}t^2+Ct+K.
$$

Use $\omega_z(0)=\omega_0$:

$$
\omega_0=K.
$$

So

$$
\omega_z(t)=\frac{A}{2}t^2+Ct+\omega_0.
$$

Now integrate velocity to get position:

$$
\theta_z(t)=\int \left(\frac{A}{2}t^2+Ct+\omega_0\right)\,dt
=\frac{A}{6}t^3+\frac{C}{2}t^2+\omega_0t+L.
$$

Use $\theta_z(0)=\theta_0$, so $L=\theta_0$. Therefore,

$$
\theta_z(t)=\frac{A}{6}t^3+\frac{C}{2}t^2+\omega_0t+\theta_0.
$$

```quiz
type: radio
id: q-3
content: |-
  Suppose $\alpha_z(t)=Dt+C$, with $\omega_z(0)=\omega_0$ and $\theta_z(0)=\theta_0$. What is $\theta_z(t)$?
options:
- id: a
  content: |-
    $\dfrac{D}{2}t^2+Ct+\omega_0+\theta_0$
- id: b
  content: |-
    $\dfrac{D}{6}t^3+\dfrac{C}{2}t^2+\omega_0t+\theta_0$
  correct: true
- id: c
  content: |-
    $\dfrac{D}{2}t^3+\dfrac{C}{2}t^2+\omega_0t+\theta_0$
- id: d
  content: |-
    $\dfrac{D}{6}t^3+\dfrac{C}{2}t^2+\omega_0+\theta_0$
- id: e
  content: |-
    $Dt^3+Ct^2+\omega_0t$
```

---

<a id="keeping-the-coefficients-straight"></a>
## Keeping the Coefficients Straight

**Example:** Suppose

$$
\alpha_z(t)=Bt^2+C.
$$

Find the part of $\theta_z(t)$ that comes from $Bt^2+C$ before adding the initial-condition terms.

**Explanation**

Integrate once:

$$
\omega_z(t)=\frac{B}{3}t^3+Ct+K.
$$

Then integrate again:

$$
\theta_z(t)=\frac{B}{12}t^4+\frac{C}{2}t^2+Kt+L.
$$

Here is the same information term by term:

| Acceleration term | After one integration | After two integrations |
| --- | --- | --- |
| $Bt^2$ | $\dfrac{B}{3}t^3$ | $\dfrac{B}{12}t^4$ |
| $C$ | $Ct$ | $\dfrac{C}{2}t^2$ |
| $K$ from velocity | $K$ in $\omega_z(t)$ | $Kt$ in $\theta_z(t)$ |
| $L$ from position | not present yet | $L$ in $\theta_z(t)$ |

The common trap is to stop after one integration and use $\dfrac{B}{3}t^4$ or $Ct^2$. Each term must be integrated a second time:

$$
Bt^2\longrightarrow \frac{B}{3}t^3\longrightarrow \frac{B}{12}t^4,
$$

and

$$
C\longrightarrow Ct\longrightarrow \frac{C}{2}t^2.
$$

```quiz
type: radio
id: q-4
content: |-
  If $\alpha_z(t)=Pt^2+Q$, which expression gives the part of $\theta_z(t)$ that comes from $Pt^2+Q$, before adding initial-condition terms?
options:
- id: a
  content: |-
    $Pt^4+Qt^2$
- id: b
  content: |-
    $\dfrac{P}{3}t^4+Qt^2$
- id: c
  content: |-
    $\dfrac{P}{12}t^4+\dfrac{Q}{2}t^2$
  correct: true
- id: d
  content: |-
    $\dfrac{P}{3}t^3+Qt$
- id: e
  content: |-
    $\dfrac{P}{12}t^4+\dfrac{Q}{2}t^2+\omega_0t$
```

---

<a id="matching-the-requested-formula"></a>
## Matching the Requested Formula

**Example:** The angular acceleration is

$$
\alpha_z(t)=Bt^2+C,
$$

with $\omega_z(0)=\omega_0$ and $\theta_z(0)=\theta_0$. Find $\theta_z(t)$.

**Explanation**

Integrate once and use $\omega_z(0)=\omega_0$:

$$
\omega_z(t)=\frac{B}{3}t^3+Ct+\omega_0.
$$

Integrate again and use $\theta_z(0)=\theta_0$:

$$
\theta_z(t)=\frac{B}{12}t^4+\frac{C}{2}t^2+\omega_0t+\theta_0.
$$

The terms $\omega_0t$ and $\theta_0$ are not optional. They come from the two initial conditions.

You can check the formula quickly. Differentiate once:

$$
\frac{d}{dt}\left(\frac{B}{12}t^4+\frac{C}{2}t^2+\omega_0t+\theta_0\right)
=\frac{B}{3}t^3+Ct+\omega_0.
$$

Differentiate again:

$$
\frac{d}{dt}\left(\frac{B}{3}t^3+Ct+\omega_0\right)=Bt^2+C.
$$

At $t=0$, the derivative gives $\omega_z(0)=\omega_0$, and the position formula gives $\theta_z(0)=\theta_0$, so both initial conditions are preserved.

```quiz
type: radio
id: q-5
content: |-
  The $z$-component of the angular acceleration of an object moving along a circular trajectory has $\alpha_z(t)=Bt^2+C$, where $B$ and $C$ are constants of the appropriate dimension.

  Let $\omega_z(t)$ and $\theta_z(t)$ denote the $z$-components of the object's angular velocity and position, respectively. If $\omega_z(0\ \mathrm{s})=\omega_0$ and $\theta_z(0\ \mathrm{s})=\theta_0$, what is $\theta_z(t)$?
options:
- id: a
  content: |-
    $Bt^4+Ct^2+\omega_0t+\theta_0$
- id: b
  content: |-
    $\dfrac{B}{3}t^4+Ct^2+\omega_0t+\theta_0$
- id: c
  content: |-
    $\dfrac{B}{12}t^4+\dfrac{C}{2}t^2$
- id: d
  content: |-
    $\dfrac{B}{12}t^4+\dfrac{C}{2}t^2+\omega_0t+\theta_0$
  correct: true
- id: e
  content: |-
    $Bt^4+Ct^2+\omega_0t$
```

---

## Summary

When $\alpha_z(t)$ is given and $\theta_z(t)$ is requested, integrate twice. The first integration produces $\omega_z(t)$ and uses $\omega_z(0)$ to set its constant. The second integration produces $\theta_z(t)$ and uses $\theta_z(0)$ to set its constant. For $\alpha_z(t)=Bt^2+C$, the final position formula is

$$
\theta_z(t)=\frac{B}{12}t^4+\frac{C}{2}t^2+\omega_0t+\theta_0.
$$

The main trap is forgetting that both $Bt^2$ and $C$ must be integrated twice, and that the initial velocity contributes the term $\omega_0t$.
