# Angle Turned Before Reversal

<!--
lesson-id: 212-M1-042
topic-code: MTH212.M1.42
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Reversal Time](#find-the-reversal-time)
- [Integrate Angular Velocity](#integrate-angular-velocity)
- [Use the Correct Bounds](#use-the-correct-bounds)
- [Match the Target Problem](#match-the-target-problem)
- [Summary](#summary)

## Prerequisites

- Solve an equation of the form $A-Bt^2=0$ by isolating $t^2$.
- Use the power rule for antiderivatives: $\int t^n\,dt=\dfrac{t^{n+1}}{n+1}$.
- Evaluate a definite integral by subtracting the antiderivative at the lower bound from the upper bound.

---

<a id="introduction"></a>
## Introduction

When a problem gives angular velocity $\omega(t)$ and asks how far a disk turns before it reverses, use two steps:

1. Find the reversal time by solving $\omega(t)=0$.
2. Integrate angular velocity from the starting time to that reversal time.

For

$$
\omega(t)=A-Bt^2,
$$

with $A>0$ and $B>0$, the angular velocity starts positive and decreases as $t$ grows. The first reversal after $t_0=0$ occurs when

$$
A-Bt^2=0.
$$

After that time is found, the angle turned is

$$
\Delta\theta=\int_{t_0}^{t_{\text{rev}}}\omega(t)\,dt.
$$

Do not stop after finding the time. The requested answer is an angle in radians, so the final step must accumulate angular velocity over time.

---

<a id="find-the-reversal-time"></a>
## Find the Reversal Time

**Example:** A spinning disk has angular velocity

$$
\omega(t)=20-0.80t^2.
$$

Find the time when it reverses direction, starting from $t_0=0$.

**Explanation**

The disk reverses when angular velocity changes sign, so set $\omega(t)=0$:

$$
20-0.80t^2=0.
$$

Isolate $t^2$:

$$
0.80t^2=20
$$

$$
t^2=25.
$$

The square-root equation gives $t=\pm 5$, but the reversal after $t_0=0$ happens at the future time

$$
t_{\text{rev}}=5\ \mathrm{s}.
$$

```quiz
type: radio
id: angle-reversal-time
shuffle: true
content: |-
  A disk has angular velocity $\omega(t)=12-0.75t^2$. Starting from $t_0=0$, when does it first reverse direction?
options:
- id: a
  content: |-
    $t=4\ \mathrm{s}$
  correct: true
- id: b
  content: |-
    $t=-4\ \mathrm{s}$
- id: c
  content: |-
    $t=16\ \mathrm{s}$
- id: d
  content: |-
    $t=9\ \mathrm{s}$
- id: e
  content: |-
    It reverses immediately at $t=0$.
```

---

<a id="integrate-angular-velocity"></a>
## Integrate Angular Velocity

**Example:** A disk has angular velocity

$$
\omega(t)=12-0.75t^2.
$$

It reverses at $t=4\ \mathrm{s}$. How far does it turn from $t=0$ to $t=4$?

**Explanation**

The angle turned is the definite integral of angular velocity:

$$
\Delta\theta=\int_0^4 (12-0.75t^2)\,dt.
$$

Take the antiderivative term by term:

$$
F(t)=\int (12-0.75t^2)\,dt=12t-\frac{0.75}{3}t^3.
$$

Since $0.75/3=0.25$,

$$
F(t)=12t-0.25t^3.
$$

Evaluate upper minus lower:

$$
\Delta\theta=F(4)-F(0).
$$

$$
\Delta\theta=(12(4)-0.25(4)^3)-(12(0)-0.25(0)^3).
$$

$$
\Delta\theta=48-16=32.
$$

The disk turns through $32\ \mathrm{rad}$ before reversing.

```quiz
type: radio
id: angle-integrate-velocity
shuffle: true
content: |-
  A disk has angular velocity $\omega(t)=15-0.60t^2$. It reverses at $t=5\ \mathrm{s}$. How far does it turn from $t=0$ to $t=5$?
options:
- id: a
  content: |-
    $75\ \mathrm{rad}$
- id: b
  content: |-
    $50\ \mathrm{rad}$
  correct: true
- id: c
  content: |-
    $25\ \mathrm{rad}$
- id: d
  content: |-
    $0\ \mathrm{rad}$
- id: e
  content: |-
    $5\ \mathrm{rad}$
```

---

<a id="use-the-correct-bounds"></a>
## Use the Correct Bounds

**Example:** A disk has angular velocity

$$
\omega(t)=9-t^2.
$$

Which integral gives the angle turned from $t=0$ until the disk first reverses?

**Explanation**

First solve for the reversal time:

$$
9-t^2=0
$$

$$
t^2=9
$$

$$
t=\pm 3.
$$

Starting from $t=0$, the future reversal time is $t=3$, not $t=-3$. The correct angle setup is

$$
\Delta\theta=\int_0^3 (9-t^2)\,dt.
$$

If you integrate from $-3$ to $3$, you are using a time interval that starts before the motion interval in the problem. If you report $3$, you are reporting the reversal time, not the angle. If you use $9$ as the upper bound, you are using the value of $t^2$ instead of the time.

```quiz
type: radio
id: angle-correct-bounds
shuffle: true
content: |-
  A disk has angular velocity $\omega(t)=25-t^2$. Starting from $t_0=0$, which setup gives the angle turned before the disk first reverses?
options:
- id: a
  content: |-
    $\displaystyle \int_0^5 (25-t^2)\,dt$
  correct: true
- id: b
  content: |-
    $\displaystyle \int_{-5}^{5} (25-t^2)\,dt$
- id: c
  content: |-
    $t=5$
- id: d
  content: |-
    $\displaystyle \int_0^{25} (25-t^2)\,dt$
- id: e
  content: |-
    $\displaystyle \int_0^{-5} (25-t^2)\,dt$
```

---

<a id="match-the-target-problem"></a>
## Match the Target Problem

**Example:** The angular velocity of a spinning disk is

$$
\omega(t)=A-Bt^2,
$$

where $A=18\ \mathrm{s}^{-1}$ and $B=0.50\ \mathrm{s}^{-3}$. Through what angle does the disk turn between $t_0=0.0\ \mathrm{s}$ and the time at which it reverses its direction of rotation?

**Explanation**

First find the reversal time:

$$
18-0.50t^2=0.
$$

Move the $t^2$ term to the other side and divide:

$$
0.50t^2=18
$$

$$
t^2=36.
$$

Starting from $t_0=0$, the future reversal time is

$$
t_{\text{rev}}=6\ \mathrm{s}.
$$

Now integrate angular velocity from $0$ to $6$:

$$
\Delta\theta=\int_0^6 (18-0.50t^2)\,dt.
$$

Take the antiderivative:

$$
\int (18-0.50t^2)\,dt=18t-\frac{0.50}{3}t^3.
$$

Evaluate at the bounds:

$$
\Delta\theta=\left[18t-\frac{0.50}{3}t^3\right]_0^6.
$$

$$
\Delta\theta=\left(18(6)-\frac{0.50}{3}(6)^3\right)-0.
$$

$$
\Delta\theta=108-\frac{0.50}{3}(216).
$$

$$
\Delta\theta=108-36=72.
$$

The disk turns through

$$
72\ \mathrm{rad}.
$$

```quiz
type: radio
id: angle-target-match
shuffle: true
content: |-
  A disk has angular velocity $\omega(t)=24-1.5t^2$. Through what angle does it turn from $t_0=0$ until it first reverses?
options:
- id: a
  content: |-
    $4\ \mathrm{rad}$
- id: b
  content: |-
    $24\ \mathrm{rad}$
- id: c
  content: |-
    $64\ \mathrm{rad}$
  correct: true
- id: d
  content: |-
    $96\ \mathrm{rad}$
- id: e
  content: |-
    $0\ \mathrm{rad}$
```

---

<a id="summary"></a>
## Summary

When $\omega(t)=A-Bt^2$ and the disk starts at $t_0=0$, the cue is the phrase "until it reverses." A reversal happens when $\omega(t)=0$, so first solve

$$
A-Bt^2=0
$$

and keep the future positive time. Then compute

$$
\Delta\theta=\int_0^{t_{\text{rev}}}(A-Bt^2)\,dt.
$$

The main trap is stopping at $t_{\text{rev}}$. The reversal time is measured in seconds; the requested angle is found by integrating angular velocity and is measured in radians.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
