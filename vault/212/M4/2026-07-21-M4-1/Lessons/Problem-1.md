# Finding Maximum Speed From a Cosine Position Function

<!--
lesson-id: 212-M4-001
topic-code: MTH212.M4.01
-->

## Table of Contents

- [Introduction](#introduction)
- [Differentiate the Position Function](#differentiate-the-position-function)
- [Extract the Maximum Speed](#extract-the-maximum-speed)
- [Evaluate the Formula With Units](#evaluate-the-formula-with-units)
- [Apply the Procedure to the Oscillator](#apply-the-procedure-to-the-oscillator)
- [Summary](#summary)

## Prerequisites

- Interpret velocity as the time derivative of position.
- Use $\frac{d}{dt}\cos(u)=-\sin(u)\frac{du}{dt}$.
- Know that $-1\leq\sin(\omega t)\leq1$.
- Distinguish velocity from speed.

---

<a id="introduction"></a>
## Introduction

A simple harmonic oscillator may have position

$$
x(t)=A\cos(\omega t),
$$

where $A$ is the position amplitude and $\omega$ is the angular frequency.

To find the oscillator's maximum speed:

1. Differentiate position to obtain velocity.
2. Take the magnitude of the velocity.
3. Replace the magnitude of the sine factor by its maximum value, $1$.

This produces the reusable result

$$
v_{\max}=A\omega.
$$

The recognition cue is a sinusoidal position function together with a request for **maximum speed**.

Track how the coefficient changes:

| Function | Sinusoidal coefficient | Physical meaning |
|---|---:|---|
| $x(t)=A\cos(\omega t)$ | $A$ | Maximum position magnitude |
| $v(t)=-A\omega\sin(\omega t)$ | $-A\omega$ | Signed velocity amplitude |
| $|v(t)|$ | $A\omega$ | Maximum speed |

The negative sign changes the velocity's direction, not its largest magnitude.

---

<a id="differentiate-the-position-function"></a>
## Differentiate the Position Function

**Example:** Find the velocity function when $x(t)=0.30\cos(4t)$ in SI units.

**Explanation**

Velocity is the derivative of position:

$$
v(t)=\frac{dx}{dt}.
$$

Let $u=4t$. The chain rule gives

$$
\frac{d}{dt}\cos(4t)
=-\sin(4t)\frac{d}{dt}(4t)
=-4\sin(4t).
$$

Therefore,

$$
v(t)=-0.30(4)\sin(4t)
=-1.2\sin(4t)\ \mathrm{m/s}.
$$

This is an outer-rule/inner-rule calculation:

| Part | Derivative |
|---|---|
| Outer function $\cos u$ | $-\sin u$ |
| Inner function $u=4t$ | $du/dt=4$ |
| Product | $-4\sin(4t)$ |

**Watch Out!** Differentiating cosine changes it to negative sine **and** produces the factor $\omega$ from the derivative of the angle $\omega t$.

```quiz
type: radio
id: problem-1-derivative-q1
content: |-
  An oscillator has position $x(t)=0.20\cos(5t)$ in SI units. Which velocity function is correct?
options:
- id: a
  content: |-
    $v(t)=-\sin(5t)\ \mathrm{m/s}$
  feedback: |-
    This omits both the position amplitude and the chain-rule factor.
- id: b
  content: |-
    $v(t)=-1.0\sin(5t)\ \mathrm{m/s}$
  correct: true
  feedback: |-
    Differentiation gives $v(t)=-A\omega\sin(\omega t)=-0.20(5)\sin(5t)$.
- id: c
  content: |-
    $v(t)=1.0\cos(5t)\ \mathrm{m/s}$
  feedback: |-
    The derivative of cosine is negative sine, not cosine.
```

---

<a id="extract-the-maximum-speed"></a>
## Extract the Maximum Speed

**Example:** If $v(t)=-A\omega\sin(\omega t)$, what is the maximum speed?

**Explanation**

Speed is the magnitude of velocity:

$$
|v(t)|=A\omega|\sin(\omega t)|.
$$

Because

$$
0\leq|\sin(\omega t)|\leq1,
$$

the largest possible value occurs when $|\sin(\omega t)|=1$. Thus,

$$
v_{\max}=A\omega.
$$

Equivalently, the velocity range is

$$
-A\omega\leq v(t)\leq A\omega.
$$

The maximum **velocity** is $+A\omega$, while the maximum **speed** is the largest magnitude, also $A\omega$.

At $t=0$, the oscillator is at $x=A$ and its speed is zero. The maximum speed occurs later, as it passes through equilibrium.

```quiz
type: radio
id: problem-1-maximum-q1
content: |-
  An oscillator has velocity $v(t)=-0.72\sin(3t)\ \mathrm{m/s}$. What is its maximum speed?
options:
- id: a
  content: |-
    $0\ \mathrm{m/s}$
  feedback: |-
    The speed is zero at some instants, but the question asks for its largest value.
- id: b
  content: |-
    $0.72\ \mathrm{m/s}$
  correct: true
  feedback: |-
    The maximum of $|\sin(3t)|$ is $1$, so the speed amplitude is $0.72\ \mathrm{m/s}$.
- id: c
  content: |-
    $2.16\ \mathrm{m/s}$
  feedback: |-
    The coefficient $0.72$ already includes the derivative's angular-frequency factor.
```

---

<a id="evaluate-the-formula-with-units"></a>
## Evaluate the Formula With Units

**Example:** Find the maximum speed for $A=0.12\ \mathrm{m}$ and $\omega=3.5\ \mathrm{rad/s}$.

**Explanation**

Use

$$
v_{\max}=A\omega.
$$

Then

$$
v_{\max}
=(0.12\ \mathrm{m})(3.5\ \mathrm{rad/s})
=0.42\ \mathrm{m/s}.
$$

Radians are dimensionless, so the units reduce to meters per second:

$$
(\mathrm{m})(\mathrm{rad/s})=\mathrm{m/s}.
$$

Both measured inputs have two significant figures, so the result is reported with two significant figures.

```quiz
type: radio
id: problem-1-evaluate-q1
content: |-
  A simple harmonic oscillator has $A=0.16\ \mathrm{m}$ and $\omega=2.5\ \mathrm{rad/s}$. What is its maximum speed?
options:
- id: a
  content: |-
    $0.40\ \mathrm{m/s}$
  correct: true
  feedback: |-
    $v_{\max}=A\omega=(0.16)(2.5)=0.40\ \mathrm{m/s}$.
- id: b
  content: |-
    $0.064\ \mathrm{m/s}$
  feedback: |-
    This divides $A$ by $\omega$ instead of multiplying.
- id: c
  content: |-
    $2.7\ \mathrm{m/s}$
  feedback: |-
    The position amplitude and angular frequency are multiplied, not added.
```

---

<a id="apply-the-procedure-to-the-oscillator"></a>
## Apply the Procedure to the Oscillator

**Example:** An oscillator moves according to $x(t)=A\cos(\omega t)$ with the given amplitude and angular frequency. Find its maximum speed.

**Explanation**

Differentiate the position:

$$
v(t)=-A\omega\sin(\omega t).
$$

Since the maximum of $|\sin(\omega t)|$ is $1$,

$$
v_{\max}=A\omega.
$$

Substitute $A=0.25\ \mathrm{m}$ and $\omega=1.8\ \mathrm{rad/s}$:

$$
v_{\max}
=(0.25\ \mathrm{m})(1.8\ \mathrm{rad/s})
=0.45\ \mathrm{m/s}.
$$

```quiz
type: radio
id: m4-1pre-q1
content: |-
  **Question 1**

  A simple harmonic oscillator moves according to $x(t)=A\cos(\omega t)$, where $A=0.25\ \mathrm{m}$ and $\omega=1.8\ \mathrm{rad/s}$. What is its maximum speed?

  Enter the maximum speed in meters per second as a number only:
options:
- id: a
  content: 0.45
  correct: true
  feedback: |-
    Differentiating the position gives

    $$
    v(t)=-A\omega\sin(\omega t).
    $$

    The maximum speed is therefore

    $$
    v_{\max}=A\omega=(0.25\ \mathrm{m})(1.8\ \mathrm{rad/s})=0.45\ \mathrm{m/s}.
    $$

    Both measured givens have two significant figures, so the result is $0.45\ \mathrm{m/s}$.
- id: b
  content: 0.14
- id: c
  content: 0.25
- id: d
  content: 1.8
```

---

<a id="summary"></a>
## Summary

When $x(t)=A\cos(\omega t)$ and the problem asks for maximum speed:

1. Differentiate to get $v(t)=-A\omega\sin(\omega t)$.
2. Use speed $|v(t)|$, not signed velocity.
3. Set the bounded factor $|\sin(\omega t)|$ to its maximum value $1$.
4. Compute $v_{\max}=A\omega$.
5. Check for distance-per-time units and round to the precision of the measured givens.

The main trap is forgetting the chain-rule factor $\omega$ when differentiating $\cos(\omega t)$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
