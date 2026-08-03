# Find Angular Speed From Angular Position

<!--
lesson-id: 212-M1-037
topic-code: MTH212.M1.37
-->

## Table of Contents

- [Introduction](#introduction)
- [Differentiate the Position Formula](#differentiate-the-position-formula)
- [Evaluate at the Requested Time](#evaluate-at-the-requested-time)
- [Report Speed, Not Signed Velocity](#report-speed-not-signed-velocity)
- [Match the Target Problem](#match-the-target-problem)
- [Summary](#summary)

## Prerequisites

- Use the power rule: $\dfrac{d}{dt}(Ct^n)=nCt^{n-1}$.
- Substitute a given time into an expression.
- Recognize that angular speed is the magnitude of angular velocity.

---

<a id="introduction"></a>
## Introduction

When a problem gives angular position $\theta(t)$ and asks for angular speed at a specific time, first find angular velocity:

$$
\omega(t)=\frac{d\theta}{dt}
$$

For the common form

$$
\theta(t)=At^2-Bt^3,
$$

the derivative is

$$
\omega(t)=2At-3Bt^2.
$$

Then plug in the time. If the result is negative, the angular velocity is negative but the angular speed is positive. The units are $\mathrm{rad}/\mathrm{s}$ because angular velocity is change in radians per change in seconds.

---

<a id="differentiate-the-position-formula"></a>
## Differentiate the Position Formula

The cue is a position formula like $\theta(t)=At^2-Bt^3$. Since speed comes from how fast position is changing, differentiate the whole formula term by term using the power rule, the constant multiple rule, and the subtraction rule.

**Example:** Find $\omega(t)$ if

$$
\theta(t)=3.0t^2-0.40t^3.
$$

**Explanation**

Differentiate each power of $t$:

$$
\omega(t)=\frac{d}{dt}(3.0t^2)-\frac{d}{dt}(0.40t^3)
$$

$$
\omega(t)=6.0t-1.20t^2.
$$

The coefficient changes because the exponent comes down as a multiplier.

```quiz
type: radio
id: q-derivative-form
shuffle: true
content: |-
  If $\theta(t)=4.0t^2-0.70t^3$, which expression gives $\omega(t)$?
options:
- id: q-derivative-form-a
  content: |-
    $4.0t^2-0.70t^3$
- id: q-derivative-form-b
  content: |-
    $4.0t-0.70t^2$
- id: q-derivative-form-c
  content: |-
    $8.0t-2.10t^2$
  correct: true
- id: q-derivative-form-d
  content: |-
    $8.0t^2-2.10t^3$
```

---

<a id="evaluate-at-the-requested-time"></a>
## Evaluate at the Requested Time

After differentiating, substitute the requested time into $\omega(t)$, not into $\theta(t)$.

**Example:** Suppose

$$
\theta(t)=3.0t^2-0.50t^3.
$$

Find the angular velocity at $t=2.0$ seconds.

**Explanation**

First differentiate:

$$
\omega(t)=6.0t-1.50t^2.
$$

Then substitute $t=2.0$:

$$
\omega(2.0)=6.0(2.0)-1.50(2.0)^2
$$

$$
\omega(2.0)=12.0-6.0=6.0.
$$

The angular velocity is $6.0\ \mathrm{rad}/\mathrm{s}$.

```quiz
type: radio
id: q-evaluate-time
shuffle: true
content: |-
  If $\theta(t)=2.5t^2-0.30t^3$, what is $\omega(2.0)$?
options:
- id: q-evaluate-time-a
  content: |-
    $3.8\ \mathrm{rad}/\mathrm{s}$
- id: q-evaluate-time-b
  content: |-
    $6.4\ \mathrm{rad}/\mathrm{s}$
  correct: true
- id: q-evaluate-time-c
  content: |-
    $8.8\ \mathrm{rad}/\mathrm{s}$
- id: q-evaluate-time-d
  content: |-
    $10.0\ \mathrm{rad}/\mathrm{s}$
```

---

<a id="report-speed-not-signed-velocity"></a>
## Report Speed, Not Signed Velocity

Angular velocity can be positive or negative. Angular speed is how fast the particle is rotating, so it is the magnitude:

$$
\text{angular speed}=|\omega(t)|.
$$

**Example:** Let

$$
\theta(t)=5.0t^2-2.0t^3.
$$

Find the angular speed at $t=2.0$ seconds.

**Explanation**

Differentiate:

$$
\omega(t)=10.0t-6.0t^2.
$$

Evaluate:

$$
\omega(2.0)=10.0(2.0)-6.0(2.0)^2=20.0-24.0=-4.0.
$$

The angular velocity is $-4.0\ \mathrm{rad}/\mathrm{s}$, so the angular speed is $4.0\ \mathrm{rad}/\mathrm{s}$.

```quiz
type: radio
id: q-speed-magnitude
shuffle: true
content: |-
  If $\theta(t)=4.0t^2-1.5t^3$, what angular speed should be reported at $t=2.0$ seconds?
options:
- id: q-speed-magnitude-a
  content: |-
    $-2.0\ \mathrm{rad}/\mathrm{s}$
- id: q-speed-magnitude-b
  content: |-
    $2.0\ \mathrm{rad}/\mathrm{s}$
  correct: true
- id: q-speed-magnitude-c
  content: |-
    $16.0\ \mathrm{rad}/\mathrm{s}$
- id: q-speed-magnitude-d
  content: |-
    $18.0\ \mathrm{rad}/\mathrm{s}$
```

---

<a id="match-the-target-problem"></a>
## Match the Target Problem

Now apply the same steps to the given form $\theta(t)=At^2-Bt^3$.

**Example:** A particle moves in non-uniform circular motion according to

$$
\theta(t)=At^2-Bt^3,
$$

where $A=2.8\ \mathrm{rad}/\mathrm{s}^2$ and $B=1.1\ \mathrm{rad}/\mathrm{s}^3$. What is the angular speed at $t=1.3$ seconds?

**Explanation**

Differentiate before substituting:

$$
\omega(t)=2At-3Bt^2.
$$

Substitute $A=2.8$, $B=1.1$, and $t=1.3$:

$$
\omega(1.3)=2(2.8)(1.3)-3(1.1)(1.3)^2.
$$

Compute each term:

$$
\omega(1.3)=7.28-5.577=1.703.
$$

The velocity is positive, so the angular speed is $1.703\ \mathrm{rad}/\mathrm{s}$. Rounded to one decimal place, enter $1.7$.

```quiz
type: radio
id: q-target-like
shuffle: true
content: |-
  A particle has $\theta(t)=At^2-Bt^3$, where $A=3.2\ \mathrm{rad}/\mathrm{s}^2$ and $B=0.80\ \mathrm{rad}/\mathrm{s}^3$. What angular speed should be reported at $t=1.5$ seconds?
options:
- id: q-target-like-a
  content: |-
    $4.5\ \mathrm{rad}/\mathrm{s}$
- id: q-target-like-b
  content: |-
    $5.4\ \mathrm{rad}/\mathrm{s}$
- id: q-target-like-c
  content: |-
    $9.6\ \mathrm{rad}/\mathrm{s}$
- id: q-target-like-d
  content: |-
    $4.2\ \mathrm{rad}/\mathrm{s}$
  correct: true
```

---

<a id="summary"></a>
## Summary

When $\theta(t)$ is given and the question asks for angular speed at a time, use this checklist:

1. Differentiate $\theta(t)$ to get $\omega(t)$.
2. Substitute the requested time into $\omega(t)$.
3. Take the magnitude if $\omega(t)$ is negative.
4. Report the value in $\mathrm{rad}/\mathrm{s}$, or enter just the number if the prompt asks for no units.

The main trap is substituting into the position formula instead of its derivative.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
