# Magnitude of Constant Angular Acceleration

## Table of Contents

- [Introduction](#introduction)
- [Use The Constant Acceleration Formula](#use-the-constant-acceleration-formula)
- [Keep The Sign Until The End](#keep-the-sign-until-the-end)
- [Find The Magnitude For A Stopping Disk](#find-the-magnitude-for-a-stopping-disk)
- [Attach The Units And Round](#attach-the-units-and-round)
- [Summary](#summary)

## Prerequisites

- Interpret "comes to a stop" as a final angular velocity of $0$.
- Subtract final value minus initial value to find a change.
- Divide a change by elapsed time to find a constant rate.
- Use radians per second as angular velocity units.
- Know that a magnitude is nonnegative.

---

<a id="introduction"></a>
## Introduction

When a rotating object has constant angular acceleration, its angular velocity changes by the same amount each second. The cue is a statement with an initial angular velocity, a final angular velocity, and an elapsed time.

Angular acceleration is a rate of change: change in angular velocity per change in time. Put the quantity that changes, $\omega$, in the numerator, and put elapsed time in the denominator.

Use

$$
\alpha=\frac{\Delta \omega}{\Delta t}
=\frac{\omega_f-\omega_i}{\Delta t}.
$$

If the question asks for the magnitude, compute the signed angular acceleration first, then take the absolute value:

$$
|\alpha|.
$$

---

<a id="use-the-constant-acceleration-formula"></a>
## Use The Constant Acceleration Formula

**Example:** A wheel speeds up from $5\ \mathrm{rad}/\mathrm{s}$ to $17\ \mathrm{rad}/\mathrm{s}$ in $4\ \mathrm{s}$ with constant angular acceleration. Find the angular acceleration.

**Explanation**

The initial angular velocity is

$$
\omega_i=5\ \mathrm{rad}/\mathrm{s},
$$

and the final angular velocity is

$$
\omega_f=17\ \mathrm{rad}/\mathrm{s}.
$$

Substitute into the constant-acceleration formula:

$$
\begin{aligned}
\alpha
&=\frac{\omega_f-\omega_i}{\Delta t} \\
&=\frac{17-5}{4} \\
&=3.
\end{aligned}
$$

So the angular acceleration is $3\ \mathrm{rad}/\mathrm{s}^2$. This example is speeding up in the positive direction, so the signed value is positive.

```quiz
type: radio
id: q-p2-1
shuffle: true
content: |-
  A disk speeds up from $6\ \mathrm{rad}/\mathrm{s}$ to $18\ \mathrm{rad}/\mathrm{s}$ in $3\ \mathrm{s}$ with constant angular acceleration. What is the angular acceleration?
options:
- id: a
  content: |-
    $2\ \mathrm{rad}/\mathrm{s}^2$
- id: b
  content: |-
    $4\ \mathrm{rad}/\mathrm{s}^2$
  correct: true
- id: c
  content: |-
    $6\ \mathrm{rad}/\mathrm{s}^2$
- id: d
  content: |-
    $8\ \mathrm{rad}/\mathrm{s}^2$
- id: e
  content: |-
    $24\ \mathrm{rad}/\mathrm{s}^2$
```

---

<a id="keep-the-sign-until-the-end"></a>
## Keep The Sign Until The End

**Example:** A wheel slows from $20\ \mathrm{rad}/\mathrm{s}$ to $8\ \mathrm{rad}/\mathrm{s}$ in $6\ \mathrm{s}$ with constant angular acceleration. Find the signed angular acceleration.

**Explanation**

The change in angular velocity is final minus initial:

$$
\Delta \omega=8-20=-12\ \mathrm{rad}/\mathrm{s}.
$$

Now divide by the elapsed time:

$$
\begin{aligned}
\alpha
&=\frac{-12}{6} \\
&=-2\ \mathrm{rad}/\mathrm{s}^2.
\end{aligned}
$$

The negative sign tells you that the angular velocity is decreasing in the chosen positive direction. Keep that sign while computing; only remove it if the question asks for a magnitude.

```quiz
type: radio
id: q-p2-2
shuffle: true
content: |-
  A wheel slows from $14\ \mathrm{rad}/\mathrm{s}$ to $2\ \mathrm{rad}/\mathrm{s}$ in $4\ \mathrm{s}$ with constant angular acceleration. What is the signed angular acceleration?
options:
- id: a
  content: |-
    $3\ \mathrm{rad}/\mathrm{s}^2$
- id: b
  content: |-
    $-3\ \mathrm{rad}/\mathrm{s}^2$
  correct: true
- id: c
  content: |-
    $4\ \mathrm{rad}/\mathrm{s}^2$
- id: d
  content: |-
    $-4\ \mathrm{rad}/\mathrm{s}^2$
- id: e
  content: |-
    $-12\ \mathrm{rad}/\mathrm{s}^2$
```

---

<a id="find-the-magnitude-for-a-stopping-disk"></a>
## Find The Magnitude For A Stopping Disk

**Example:** A disk is spinning at $12\ \mathrm{rad}/\mathrm{s}$ and comes to a stop in $26\ \mathrm{s}$ with constant angular acceleration. What is the magnitude of the angular acceleration?

**Explanation**

"Comes to a stop" means

$$
\omega_f=0.
$$

Compute the signed angular acceleration first:

$$
\begin{aligned}
\alpha
&=\frac{\omega_f-\omega_i}{\Delta t} \\
&=\frac{0-12}{26} \\
&=-\frac{12}{26} \\
&\approx -0.4615\ \mathrm{rad}/\mathrm{s}^2.
\end{aligned}
$$

The question asks for magnitude, so take the absolute value:

$$
|\alpha|\approx 0.4615\ \mathrm{rad}/\mathrm{s}^2.
$$

A magnitude works like a distance from zero, so it cannot be negative.

Rounded to two decimal places, the magnitude is

$$
0.46\ \mathrm{rad}/\mathrm{s}^2.
$$

```quiz
type: radio
id: q-p2-3
shuffle: true
content: |-
  A disk is spinning at $15\ \mathrm{rad}/\mathrm{s}$ and comes to a stop in $30\ \mathrm{s}$ with constant angular acceleration. What is the magnitude of the angular acceleration?
options:
- id: a
  content: |-
    $-0.50\ \mathrm{rad}/\mathrm{s}^2$
- id: b
  content: |-
    $0.50\ \mathrm{rad}/\mathrm{s}^2$
  correct: true
- id: c
  content: |-
    $2.00\ \mathrm{rad}/\mathrm{s}^2$
- id: d
  content: |-
    $15\ \mathrm{rad}/\mathrm{s}^2$
- id: e
  content: |-
    $30\ \mathrm{rad}/\mathrm{s}^2$
```

---

<a id="attach-the-units-and-round"></a>
## Attach The Units And Round

**Example:** A turntable slows from $9.6\ \mathrm{rad}/\mathrm{s}$ to rest in $8.0\ \mathrm{s}$. Find the magnitude of its angular acceleration.

**Explanation**

The signed angular acceleration is

$$
\begin{aligned}
\alpha
&=\frac{0-9.6}{8.0} \\
&=-1.2.
\end{aligned}
$$

The units come from dividing angular velocity by time:

$$
\frac{\mathrm{rad}/\mathrm{s}}{\mathrm{s}}
=\mathrm{rad}/\mathrm{s}^2.
$$

Since the question asks for magnitude,

$$
|\alpha|=1.2\ \mathrm{rad}/\mathrm{s}^2.
$$

```quiz
type: radio
id: q-p2-4
shuffle: true
content: |-
  A disk spins at $14\ \mathrm{rad}/\mathrm{s}$ and comes to rest in $32\ \mathrm{s}$ with constant angular acceleration. What is the magnitude of the angular acceleration, rounded to two decimal places?
options:
- id: a
  content: |-
    $0.44\ \mathrm{rad}/\mathrm{s}^2$
  correct: true
- id: b
  content: |-
    $-0.44\ \mathrm{rad}/\mathrm{s}^2$
- id: c
  content: |-
    $2.29\ \mathrm{rad}/\mathrm{s}^2$
- id: d
  content: |-
    $0.23\ \mathrm{rad}/\mathrm{s}^2$
- id: e
  content: |-
    $448\ \mathrm{rad}/\mathrm{s}^2$
```

---

<a id="summary"></a>
## Summary

For constant angular acceleration, use the cue "initial angular velocity, final angular velocity, elapsed time." Then:

1. Set $\omega_f=0$ if the object comes to a stop.
2. Compute the signed value with final minus initial:

$$
\alpha=\frac{\omega_f-\omega_i}{\Delta t}.
$$

3. Use units of $\mathrm{rad}/\mathrm{s}^2$.
4. If the problem asks for magnitude, take $|\alpha|$ and report a nonnegative answer.

The main trap is reporting the negative signed acceleration when the problem asks for the nonnegative magnitude.
