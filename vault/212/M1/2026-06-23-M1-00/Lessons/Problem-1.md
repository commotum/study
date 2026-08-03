# Finding When Angular Velocity Reverses Direction

<!--
lesson-id: 212-M1-031
topic-code: MTH212.M1.31
-->

## Table of Contents

- [Introduction](#introduction)
- [Turn Reversal into a Zero-Velocity Equation](#turn-reversal-into-a-zero-velocity-equation)
- [Isolate the Squared Time](#isolate-the-squared-time)
- [Choose the Nonnegative Time](#choose-the-nonnegative-time)
- [Compute the Given Reversal Time](#compute-the-given-reversal-time)

## Prerequisites

- Solving an equation by isolating a squared variable
- Taking the square root of a perfect square
- Knowing that the sign of angular velocity gives rotation direction

---

<a id="introduction"></a>
## Introduction

A spinning disk reverses direction when its angular velocity changes sign. The instant of reversal occurs where the angular velocity is zero.

For a model of the form

$$
\omega(t)=A-Bt^2
$$

with $A>0$ and $B>0$, set $\omega(t)=0$, solve for $t^2$, and keep the nonnegative time because the question asks for a time after the start.

The reusable rule is

$$
t=\sqrt{\frac{A}{B}}
$$

for motion starting at $t_0=0$. Since $A-Bt^2$ starts positive and decreases as $t$ grows, crossing $0$ marks the change in rotation direction.

---

<a id="turn-reversal-into-a-zero-velocity-equation"></a>
## Turn Reversal into a Zero-Velocity Equation

**Example:** A disk has angular velocity $\omega(t)=12-3t^2$. What equation should you solve to find when it reverses direction?

**Explanation**

Reversal happens when the angular velocity is zero, so replace $\omega(t)$ with $0$:

$$
0=12-3t^2
$$

That equation finds the time when the disk momentarily stops before rotating the other way.

```quiz
type: radio
id: p1-q1
shuffle: true
content: |-
  A disk has angular velocity $\omega(t)=20-5t^2$. Which equation should you solve to find when it reverses direction?
options:
- id: a
  content: |-
    $0=20-5t^2$
  correct: true
- id: b
  content: |-
    $5t^2=0$
- id: c
  content: |-
    $\omega(t)=20$
- id: d
  content: |-
    $t=20-5t^2$
- id: e
  content: |-
    $0=20+5t^2$
```

---

<a id="isolate-the-squared-time"></a>
## Isolate the Squared Time

**Example:** Solve $0=12-3t^2$ until the equation has $t^2$ alone.

**Explanation**

Move the $3t^2$ term to the other side, then divide by $3$:

$$
\begin{aligned}
0 &= 12-3t^2 \\
3t^2 &= 12 \\
t^2 &= 4
\end{aligned}
$$

This step does not give the time yet. It gives the square of the time.

In the general form $0=A-Bt^2$, the same isolation gives

$$
t^2=\frac{A}{B}
$$

```quiz
type: radio
id: p1-q2
shuffle: true
content: |-
  Solve $0=45-5t^2$ until $t^2$ is isolated. What is $t^2$?
options:
- id: a
  content: |-
    $t^2=40$
- id: b
  content: |-
    $t^2=9$
  correct: true
- id: c
  content: |-
    $t^2=50$
- id: d
  content: |-
    $t^2=225$
- id: e
  content: |-
    $t^2=\dfrac{1}{9}$
```

---

<a id="choose-the-nonnegative-time"></a>
## Choose the Nonnegative Time

**Example:** If solving a reversal-time equation gives $t^2=4$, what time should be reported?

**Explanation**

Taking the square root gives two algebraic solutions:

$$
t=\pm 2
$$

But the question asks for the time after starting at $t_0=0$. A negative time would be before the start, so the reversal time is

$$
t=2
$$

```quiz
type: radio
id: p1-q3
shuffle: true
content: |-
  A reversal-time equation gives $t^2=25$. The motion starts at $t_0=0$. Which time should be reported?
options:
- id: a
  content: |-
    $t=\pm 5$
- id: b
  content: |-
    $t=-5$
- id: c
  content: |-
    $t=25$
- id: d
  content: |-
    $t=5$
  correct: true
- id: e
  content: |-
    $t=\sqrt{25^2}$
```

---

<a id="compute-the-given-reversal-time"></a>
## Compute the Given Reversal Time

**Example:** The angular velocity of a spinning disk is

$$
\omega(t)=A-Bt^2
$$

where $A=18\ \mathrm{rad}/\mathrm{s}$ and $B=0.50\ \mathrm{rad}/\mathrm{s}^3$. Starting from $t_0=0.0\ \mathrm{s}$, at what time does the disk reverse direction?

**Explanation**

Set $\omega(t)=0$:

$$
0=18-0.50t^2
$$

Isolate $t^2$:

$$
\begin{aligned}
0.50t^2 &= 18 \\
t^2 &= \frac{18}{0.50} \\
t^2 &= 36
\end{aligned}
$$

Take the nonnegative square root:

$$
t=\sqrt{36}=6
$$

The units also check out:

$$
\frac{\mathrm{rad}/\mathrm{s}}{\mathrm{rad}/\mathrm{s}^3}=\mathrm{s}^2
$$

so the square root is measured in seconds.

The disk reverses direction at $6$ seconds.

```quiz
type: radio
id: p1-q4
shuffle: true
content: |-
  The angular velocity of a spinning disk is $\omega(t)=A-Bt^2$, with $A=32\ \mathrm{rad}/\mathrm{s}$ and $B=2.0\ \mathrm{rad}/\mathrm{s}^3$. Starting from $t_0=0$, at what time does the disk reverse direction?
options:
- id: a
  content: |-
    $2$
- id: b
  content: |-
    $4$
  correct: true
- id: c
  content: |-
    $8$
- id: d
  content: |-
    $16$
- id: e
  content: |-
    $64$
```

---

## Summary

To find when $\omega(t)=A-Bt^2$ reverses direction, use the cue "reverses direction" to set $\omega(t)=0$:

$$
0=A-Bt^2
$$

Then solve

$$
t^2=\frac{A}{B}
$$

and report

$$
t=\sqrt{\frac{A}{B}}
$$

for a motion starting at $t_0=0$. The main trap is stopping at $t^2$ or reporting both $\pm$ roots even though the requested answer is a time after the start.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
