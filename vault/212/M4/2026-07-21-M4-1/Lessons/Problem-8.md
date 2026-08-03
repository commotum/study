
# Finding Instantaneous SHM Velocity From Cycle Data

<!--
lesson-id: 212-M4-008
topic-code: MTH212.M4.08
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Amplitude From the Setup](#find-the-amplitude-from-the-setup)
- [Convert Oscillation Count to Angular Frequency](#convert-oscillation-count-to-angular-frequency)
- [Build the Velocity Function From the Release Condition](#build-the-velocity-function-from-the-release-condition)
- [Evaluate Velocity and Interpret Its Sign](#evaluate-velocity-and-interpret-its-sign)
- [Apply the Procedure to the Spring-Block System](#apply-the-procedure-to-the-spring-block-system)
- [Summary](#summary)

## Prerequisites

- Measure displacement from the equilibrium position.
- Compute a unit rate as quantity divided by elapsed time.
- Use $\omega=2\pi f$.
- Differentiate $A\cos(\omega t)$ with the chain rule.
- Evaluate trigonometric functions in radian mode.

---

<a id="introduction"></a>
## Introduction

When a spring-block oscillator is released from rest at maximum positive displacement, its position can be modeled by

$$
x(t)=A\cos(\omega t).
$$

Differentiating gives the velocity:

$$
v(t)=-A\omega\sin(\omega t).
$$

If the setup gives an equilibrium coordinate $x_0$, release coordinate $x_f$, and $N$ oscillations during a time interval $\Delta t$, use

$$
A=x_f-x_0,
\qquad
f=\frac{N}{\Delta t},
\qquad
\omega=2\pi f.
$$

The recognition cue is a block released from rest at one extreme, a cycle count over a measured time, and a request for velocity at a specified instant.

Map each given to its role before calculating:

| Given                                   | Produces                        | Used in                                         |
| --------------------------------------- | ------------------------------- | ----------------------------------------------- |
| $x_0$ and $x_f$                         | $A=\lvert x_f-x_0\rvert$       | Velocity amplitude $A\omega$                   |
| $N$ oscillations in $\Delta t$          | $f=N/\Delta t$                  | $\omega=2\pi f$                                |
| Released from rest at the right extreme | Zero-phase cosine model         | Sign and trigonometric form of $v(t)$           |
| Evaluation time $t$                     | Phase $\omega t$                | Instantaneous velocity                          |
| Mass $m$                                | No needed quantity here         | Does not enter after $A$ and $\omega$ are known |

---

<a id="find-the-amplitude-from-the-setup"></a>
## Find the Amplitude From the Setup

**Example:** A spring is unstretched at $x_0=0.20\ \mathrm{m}$. The block is pulled right to $x_f=0.32\ \mathrm{m}$ and released. What is the amplitude?

**Explanation**

The unstretched position is the equilibrium position. Amplitude is the magnitude of the release displacement from equilibrium:

$$
A=|x_f-x_0|.
$$

Because the block is released to the right,

$$
A=0.32\ \mathrm{m}-0.20\ \mathrm{m}
=0.12\ \mathrm{m}.
$$

The coordinate $x_f$ is not itself the amplitude because the coordinate origin lies to the left of equilibrium.

```quiz
type: radio
id: problem-8-amplitude-q1
content: |-
  A spring is unstretched at $x_0=0.41\ \mathrm{m}$, and the block is pulled right to $x_f=0.56\ \mathrm{m}$. What is the oscillation amplitude?
options:
- id: a
  content: |-
    $0.15\ \mathrm{m}$
  correct: true
  feedback: |-
    Amplitude is measured from equilibrium, not from the coordinate origin. The release point is $0.56\ \mathrm{m}-0.41\ \mathrm{m}=0.15\ \mathrm{m}$ to the right of equilibrium, so $A=0.15\ \mathrm{m}$.
- id: b
  content: |-
    $0.56\ \mathrm{m}$
  feedback: |-
    This is the release coordinate measured from the diagram's origin. Amplitude is the block's displacement from the equilibrium coordinate $x_0=0.41\ \mathrm{m}$, so $A=|0.56-0.41|=0.15\ \mathrm{m}$.
- id: c
  content: |-
    $0.97\ \mathrm{m}$
  feedback: |-
    Adding the two coordinates measures neither a separation nor a displacement from equilibrium. The distance between the equilibrium and release positions is their absolute difference: $A=|0.56-0.41|=0.15\ \mathrm{m}$.
```

---

<a id="convert-oscillation-count-to-angular-frequency"></a>
## Convert Oscillation Count to Angular Frequency

**Example:** An oscillator completes $9$ oscillations in $6.0\ \mathrm{s}$. Find $f$ and $\omega$.

**Explanation**

Frequency is the cycle rate:

$$
f=\frac{N}{\Delta t}
=\frac{9}{6.0\ \mathrm{s}}
=1.5\ \mathrm{Hz}.
$$

The order of the ratio matters: use oscillations divided by seconds, not seconds divided by oscillations.

Each cycle is $2\pi$ radians, so

$$
\omega=2\pi f
=2\pi(1.5\ \mathrm{s^{-1}})
=3\pi\ \mathrm{rad/s}.
$$

Thus the conversion chain is

$$
\frac{\text{oscillations}}{\mathrm{s}}
\times
\frac{2\pi\ \mathrm{rad}}{\text{oscillation}}
=\frac{\mathrm{rad}}{\mathrm{s}}.
$$

Keep the exact expression $2\pi N/\Delta t$ or several guard digits until the final velocity is calculated.

```quiz
type: radio
id: problem-8-frequency-q1
content: |-
  A block completes $5$ oscillations in $4.0\ \mathrm{s}$. Which angular frequency is correct?
options:
- id: a
  content: |-
    $1.25\ \mathrm{rad/s}$
  feedback: |-
    The value $5/4.0=1.25$ is the frequency in cycles per second. Angular frequency counts radians per second, so multiply by $2\pi\ \mathrm{rad/cycle}$ to obtain $\omega=2.5\pi\ \mathrm{rad/s}$.
- id: b
  content: |-
    $2.5\pi\ \mathrm{rad/s}$
  correct: true
  feedback: |-
    Frequency is cycles divided by elapsed time, so $f=5/(4.0\ \mathrm{s})=1.25\ \mathrm{Hz}$. Each cycle is $2\pi$ radians, giving $\omega=2\pi f=2.5\pi\ \mathrm{rad/s}$.
- id: c
  content: |-
    $8\pi\ \mathrm{rad/s}$
  feedback: |-
    This treats the elapsed time $4.0\ \mathrm{s}$ as though it were the frequency in cycles per second. The relevant rate is the cycle count divided by time, $f=5/4.0=1.25\ \mathrm{Hz}$, so $\omega=2.5\pi\ \mathrm{rad/s}$.
```

---

<a id="build-the-velocity-function-from-the-release-condition"></a>
## Build the Velocity Function From the Release Condition

**Example:** A block is released from rest at $x(0)=+A$. Write its position and velocity functions.

**Explanation**

Cosine matches the initial state because

$$
x(0)=A\cos(0)=A.
$$

Thus,

$$
x(t)=A\cos(\omega t).
$$

Differentiate with the chain rule:

$$
\begin{aligned}
v(t)
&=\frac{dx}{dt} \\
&=A[-\sin(\omega t)]\frac{d}{dt}(\omega t) \\
&=-A\omega\sin(\omega t).
\end{aligned}
$$

The factor $\omega$ comes from differentiating the angle. The negative sign makes the initial motion leftward just after release from the rightmost point.

```quiz
type: radio
id: problem-8-model-q1
content: |-
  A block is released from rest at maximum positive displacement. Which velocity function matches $x(t)=A\cos(\omega t)$?
options:
- id: a
  content: |-
    $v(t)=-A\omega\sin(\omega t)$
  correct: true
  feedback: |-
    Velocity is the time derivative of position. Differentiating $A\cos(\omega t)$ gives negative sine and a chain-rule factor of $\omega$, so $v(t)=-A\omega\sin(\omega t)$.
- id: b
  content: |-
    $v(t)=A\cos(\omega t)$
  feedback: |-
    This copies the position function instead of finding its rate of change. It also predicts $v(0)=A$ even though the block is released from rest; differentiating gives $v(t)=-A\omega\sin(\omega t)$ and $v(0)=0$.
- id: c
  content: |-
    $v(t)=-A\sin(\omega t)$
  feedback: |-
    This has the correct sine phase and sign but omits the chain-rule factor from differentiating $\omega t$. Without $\omega$, the expression has units of length rather than speed; the velocity is $-A\omega\sin(\omega t)$.
```

---

<a id="evaluate-velocity-and-interpret-its-sign"></a>
## Evaluate Velocity and Interpret Its Sign

**Example:** An oscillator has $A=0.10\ \mathrm{m}$, completes $2$ cycles in $4.0\ \mathrm{s}$, and starts at $x=+A$. Find its velocity at $t=0.50\ \mathrm{s}$.

**Explanation**

First find angular frequency:

$$
\omega=2\pi\left(\frac{2}{4.0\ \mathrm{s}}\right)
=\pi\ \mathrm{rad/s}.
$$

Then evaluate the velocity function:

$$
\begin{aligned}
v(0.50\ \mathrm{s})
&=-(0.10\ \mathrm{m})(\pi\ \mathrm{rad/s})
\sin[(\pi\ \mathrm{rad/s})(0.50\ \mathrm{s})] \\
&=-0.3141\ldots\ \mathrm{m/s} \\
&=-0.31\ \mathrm{m/s}.
\end{aligned}
$$

Calculator checkpoint:

1. Use radian mode.
2. Evaluate the entire phase $\omega t$ inside the sine.
3. Apply the leading negative sign outside the sine.
4. Keep guard digits until the final rounding step.

The negative sign means the block is moving left. It does not mean the speed is negative.

```quiz
type: radio
id: problem-8-sign-q1
content: |-
  With right defined as positive, an SHM calculation gives $v=+0.62\ \mathrm{m/s}$. What does the sign mean?
options:
- id: a
  content: |-
    The block is to the right of equilibrium.
  feedback: |-
    Positive velocity describes the direction of motion, not the side of equilibrium. A block can move right while it is on either side of equilibrium, so $v>0$ means moving right, not necessarily being right of equilibrium.
- id: b
  content: |-
    The block is moving right.
  correct: true
  feedback: |-
    The sign of velocity gives the direction of motion. Since right is defined as positive, $v=+0.62\ \mathrm{m/s}$ means the block is moving right.
- id: c
  content: |-
    The block's speed is negative.
  feedback: |-
    Speed is the magnitude $|v|$ and is never negative. The positive sign belongs to velocity and indicates direction, so the block moves right with speed $0.62\ \mathrm{m/s}$.
```

---

<a id="apply-the-procedure-to-the-spring-block-system"></a>
## Apply the Procedure to the Spring-Block System

**Example:** Find the block's velocity at $t=3.9\ \mathrm{s}$ for the given setup and cycle data.

![](<../Source/Images/spring-block-displacement-setup.png>)

**Explanation**

The amplitude is the release displacement from equilibrium:

$$
A=x_f-x_0
=0.48\ \mathrm{m}-0.35\ \mathrm{m}
=0.13\ \mathrm{m}.
$$

The angular frequency is

$$
\omega=2\pi\left(\frac{12}{7.0\ \mathrm{s}}\right).
$$

Because the block begins at maximum positive displacement,

$$
v(t)=-A\omega\sin(\omega t).
$$

Keeping guard digits through the trigonometric evaluation,

$$
\begin{aligned}
v(3.9\ \mathrm{s})
&=-(0.13\ \mathrm{m})\omega
\sin[\omega(3.9\ \mathrm{s})] \\
&=1.2876\ldots\ \mathrm{m/s} \\
&=1.3\ \mathrm{m/s}.
\end{aligned}
$$

The answer is positive, so the block is moving right at that instant. The mass $m$ is not needed because $A$ and $\omega$ are already determined from the geometry and cycle data.

```quiz
type: radio
id: m4-1lec-q7
content: |-
  **Question 7**

  For the same spring–block system, what is the block's velocity at $t=3.9\ \mathrm{s}$? Define right as positive.

  Use $m=0.18\ \mathrm{kg}$, $x_0=0.35\ \mathrm{m}$, $x_f=0.48\ \mathrm{m}$, and 12 oscillations in $7.0\ \mathrm{s}$.

  ![](<../Source/Images/spring-block-displacement-setup.png>)

  Enter the velocity in meters per second as a number only:
options:
- id: a
  content: 1.3
  correct: true
  feedback: |-
    The release displacement gives $A=0.48-0.35=0.13\ \mathrm{m}$, and the cycle rate gives $\omega=2\pi\frac{12}{7.0\ \mathrm{s}}$. Because the block starts at $+A$, $v=-A\omega\sin(\omega t)$; at $t=3.9\ \mathrm{s}$ this is $+1.2876\ldots\ \mathrm{m/s}$, or $+1.3\ \mathrm{m/s}$ to two significant figures. The positive sign means motion to the right.
- id: b
  content: -1.3
  feedback: |-
    This has the correct speed but reverses the direction. At $t=3.9\ \mathrm{s}$, $\sin(\omega t)<0$, and the leading minus sign in $v=-A\omega\sin(\omega t)$ therefore makes $v$ positive: $+1.3\ \mathrm{m/s}$, toward the right.
- id: c
  content: 1.4
  feedback: |-
    This is the maximum speed $A\omega\approx1.4\ \mathrm{m/s}$, which occurs only when $|\sin(\omega t)|=1$. The question asks for the velocity at a particular phase, so the factor $-\sin(\omega t)$ is required and gives $v=+1.3\ \mathrm{m/s}$.
- id: d
  content: -0.051
  feedback: |-
    This comes from the position function $x=A\cos(\omega t)$, so it describes where the block is and has units of meters. Velocity is the slope of position, $v=-A\omega\sin(\omega t)$, which gives $+1.3\ \mathrm{m/s}$ here.
```

---

<a id="summary"></a>
## Summary

For a block released from rest at maximum positive displacement:

1. Find amplitude from the setup: $A=|x_f-x_0|$.
2. Convert the cycle count to frequency: $f=N/\Delta t$.
3. Convert to angular frequency: $\omega=2\pi f$.
4. Use $x(t)=A\cos(\omega t)$ and $v(t)=-A\omega\sin(\omega t)$.
5. Evaluate in radian mode, keep guard digits, and round only the final result.
6. Interpret the velocity sign using the stated positive direction.

The main traps are treating $x_f$ as the amplitude, omitting $2\pi$ or the chain-rule factor $\omega$, and reporting speed instead of signed velocity.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../../M5/2026-08-03-Q-3/Study-Guide.md)
Next: [Ranking Acceleration Magnitudes from an SHM Position Graph](../../2026-07-23-HW-6/Lessons/Problem-5.md)

Study guide index: 02/28

---
<!-- lesson-nav:end -->
