# Finding SHM Displacement From Release Data

<!--
lesson-id: 212-M4-007
topic-code: MTH212.M4.07
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Coordinates to Amplitude](#convert-coordinates-to-amplitude)
- [Choose Cosine From the Release Condition](#choose-cosine-from-the-release-condition)
- [Convert Cycle Count to Angular Frequency](#convert-cycle-count-to-angular-frequency)
- [Evaluate the Phase and Interpret the Sign](#evaluate-the-phase-and-interpret-the-sign)
- [Apply the Model to the Given Spring–Block System](#apply-the-model-to-the-given-spring-block-system)
- [Summary](#summary)

## Prerequisites

- Distinguish a coordinate from displacement relative to equilibrium.
- Use \(f=N/\Delta t\) and \(\omega=2\pi f\).
- Evaluate cosine in radians with a calculator.

---

<a id="introduction"></a>
## Introduction

For simple harmonic motion, a block released from rest at its maximum positive displacement is modeled by

$$
x(t)=A\cos(\omega t).
$$

Here \(x(t)\) is displacement **from equilibrium**, \(A\) is the amplitude, and \(\omega\) is angular frequency. When the problem gives an equilibrium coordinate \(x_0\), a release coordinate \(x_f>x_0\), and \(N\) cycles completed in time \(\Delta t\), use

$$
A=x_f-x_0,
\qquad
f=\frac{N}{\Delta t},
\qquad
\omega=2\pi f.
$$

**Recognition cue:** “Pulled right and released from rest” means \(x(0)=+A\) and \(v(0)=0\), matching a cosine with zero phase.

| Given information | Derived model quantity |
|---|---|
| Coordinates \(x_0,x_f\) | \(A=x_f-x_0\) |
| \(N\) cycles in \(\Delta t\) | \(f=N/\Delta t\), then \(\omega=2\pi f\) |
| Released from rest at the rightmost point | \(x(t)=A\cos(\omega t)\) |

---

<a id="convert-coordinates-to-amplitude"></a>
## Convert Coordinates to Amplitude

**Example:** A spring is unstretched at coordinate \(x_0=0.20\ \mathrm{m}\). The block is pulled right to \(x_f=0.32\ \mathrm{m}\). What is its initial displacement from equilibrium?

**Explanation**

Displacement is the signed difference between the block's coordinate and the equilibrium coordinate:

$$
A=x_f-x_0
=0.32-0.20
=0.12\ \mathrm{m}.
$$

The amplitude is not \(0.32\ \mathrm{m}\); that is the coordinate measured from the diagram's origin.

```quiz
type: radio
id: problem-7-amplitude-q1
content: |-
  A spring is unstretched when a block is at \(x_0=0.45\ \mathrm{m}\). The block is pulled right to \(x_f=0.61\ \mathrm{m}\). What is the amplitude?
options:
- id: a
  content: |-
    \(0.16\ \mathrm{m}\)
  correct: true
  feedback: |-
    The displacement from equilibrium is \(A=x_f-x_0=0.61-0.45=0.16\ \mathrm{m}\).
- id: b
  content: |-
    \(0.61\ \mathrm{m}\)
  feedback: |-
    This is the final coordinate, not its distance from the equilibrium coordinate.
- id: c
  content: |-
    \(1.06\ \mathrm{m}\)
  feedback: |-
    Adding the two coordinates does not give their separation.
- id: d
  content: |-
    \(-0.16\ \mathrm{m}\)
  feedback: |-
    Pulling right gives positive initial displacement; amplitude itself is nonnegative.
```

---

<a id="choose-cosine-from-the-release-condition"></a>
## Choose Cosine From the Release Condition

**Example:** A block is released from rest at its rightmost position, \(x(0)=+A\). Which zero-phase SHM model matches?

**Explanation**

At \(t=0\),

$$
\cos(0)=1
\qquad\text{and}\qquad
\sin(0)=0.
$$

Therefore,

$$
x(t)=A\cos(\omega t)
$$

starts at \(x(0)=+A\). Its velocity is

$$
v(t)=-A\omega\sin(\omega t),
$$

so \(v(0)=0\), matching release from rest.

```quiz
type: radio
id: problem-7-model-q1
content: |-
  A simple harmonic oscillator is released from rest at maximum positive displacement at \(t=0\). Which model satisfies both initial conditions?
options:
- id: a
  content: |-
    \(x(t)=A\cos(\omega t)\)
  correct: true
  feedback: |-
    This gives \(x(0)=A\) and \(v(0)=0\).
- id: b
  content: |-
    \(x(t)=A\sin(\omega t)\)
  feedback: |-
    This begins at equilibrium, \(x(0)=0\), rather than at maximum displacement.
- id: c
  content: |-
    \(x(t)=-A\cos(\omega t)\)
  feedback: |-
    This begins at maximum negative displacement.
- id: d
  content: |-
    \(x(t)=-A\sin(\omega t)\)
  feedback: |-
    This also begins at equilibrium rather than at the rightmost position.
```

---

<a id="convert-cycle-count-to-angular-frequency"></a>
## Convert Cycle Count to Angular Frequency

**Example:** An oscillator completes \(10\) cycles in \(5.0\ \mathrm{s}\). Find \(f\) and \(\omega\).

**Explanation**

First find cycles per second:

$$
f=\frac{N}{\Delta t}
=\frac{10}{5.0\ \mathrm{s}}
=2.0\ \mathrm{Hz}.
$$

Each cycle contains \(2\pi\) radians, so

$$
\omega=2\pi f
=4.0\pi\ \mathrm{rad/s}.
$$

```quiz
type: radio
id: problem-7-omega-q1
content: |-
  An oscillator completes \(9\) cycles in \(6.0\ \mathrm{s}\). What is its angular frequency?
options:
- id: a
  content: |-
    \(3.0\pi\ \mathrm{rad/s}\)
  correct: true
  feedback: |-
    \(f=9/6.0=1.5\ \mathrm{Hz}\), so \(\omega=2\pi f=3.0\pi\ \mathrm{rad/s}\).
- id: b
  content: |-
    \(1.5\ \mathrm{rad/s}\)
  feedback: |-
    \(1.5\) is the ordinary frequency in hertz; multiply by \(2\pi\) for angular frequency.
- id: c
  content: |-
    \(12\pi\ \mathrm{rad/s}\)
  feedback: |-
    The elapsed time belongs in the denominator of \(f=N/\Delta t\).
- id: d
  content: |-
    \(\dfrac{4\pi}{3}\ \mathrm{rad/s}\)
  feedback: |-
    This uses the reciprocal cycle rate, \(\Delta t/N\), as though it were frequency.
```

---

<a id="evaluate-the-phase-and-interpret-the-sign"></a>
## Evaluate the Phase and Interpret the Sign

**Example:** A block has amplitude \(A=0.10\ \mathrm{m}\), frequency \(f=1.0\ \mathrm{Hz}\), and starts at \(+A\). Find its displacement at \(t=0.375\ \mathrm{s}\).

**Explanation**

Use \(\omega=2\pi f\):

$$
\omega t
=2\pi(1.0)(0.375)
=\frac{3\pi}{4}.
$$

Then

$$
\begin{aligned}
x(t)
&=A\cos(\omega t)\\
&=(0.10)\cos\left(\frac{3\pi}{4}\right)\\
&=-0.0707\ldots\ \mathrm{m}.
\end{aligned}
$$

The negative sign means the block is left of equilibrium. It does not mean the amplitude is negative.

Evaluate in this order:

1. Compute the dimensionless phase \(\omega t\).
2. Evaluate the cosine in **radian mode**.
3. Multiply by \(A\).
4. Check that \(-A\le x(t)\le A\).

```quiz
type: radio
id: problem-7-phase-q1
content: |-
  A block starts at maximum positive displacement with \(A=0.20\ \mathrm{m}\) and \(f=0.50\ \mathrm{Hz}\). What is its displacement at \(t=0.75\ \mathrm{s}\)?
options:
- id: a
  content: |-
    \(-0.14\ \mathrm{m}\)
  correct: true
  feedback: |-
    \(\omega t=2\pi(0.50)(0.75)=3\pi/4\), so \(x=0.20\cos(3\pi/4)=-0.1414\ldots\ \mathrm{m}\).
- id: b
  content: |-
    \(+0.14\ \mathrm{m}\)
  feedback: |-
    The phase \(3\pi/4\) lies where cosine is negative.
- id: c
  content: |-
    \(-0.20\ \mathrm{m}\)
  feedback: |-
    Maximum negative displacement occurs at phase \(\pi\), not \(3\pi/4\).
- id: d
  content: |-
    \(0\ \mathrm{m}\)
  feedback: |-
    Zero displacement occurs at odd multiples of \(\pi/2\), not at \(3\pi/4\).
```

---

<a id="apply-the-model-to-the-given-spring-block-system"></a>
## Apply the Model to the Given Spring–Block System

**Example:** Build and evaluate the displacement model for the spring–block setup below.

![](<../Source/Images/spring-block-displacement-setup.png>)

**Explanation**

The equilibrium coordinate is \(x_0\), so the release displacement is

$$
A=x_f-x_0
=0.48-0.35
=0.13\ \mathrm{m}.
$$

The observed cycle rate gives

$$
f=\frac{12}{7.0\ \mathrm{s}},
\qquad
\omega=2\pi\left(\frac{12}{7.0\ \mathrm{s}}\right).
$$

Because the block is released from maximum positive displacement,

$$
x(t)=A\cos(\omega t).
$$

At \(t=3.9\ \mathrm{s}\),

$$
ft
=\left(\frac{12}{7.0}\right)(3.9)
=6.6857\ldots\ \text{cycles}.
$$

Six complete cycles do not change the oscillator's position, so only the fractional part \(0.6857\ldots\) matters. Its equivalent phase is

$$
\omega t
=2\pi(0.6857\ldots)
=4.3084\ldots\ \mathrm{rad}.
$$

Now evaluate the grouped cosine expression:

$$
\begin{aligned}
x
&=(0.13\ \mathrm{m})
\cos\left[
2\pi\left(\frac{12}{7.0\ \mathrm{s}}\right)
(3.9\ \mathrm{s})
\right]\\
&=-0.05109\ldots\ \mathrm{m}\\
&=-0.051\ \mathrm{m}
\quad\text{to two significant figures.}
\end{aligned}
$$

The negative result places the block left of equilibrium. Its magnitude is below \(A=0.13\ \mathrm{m}\), as required. The mass is not needed because the measured cycle rate already determines \(\omega\).

```quiz
type: radio
id: m4-1lec-q6
content: |-
  **Question 6**

  A block of mass $m$ rests on a frictionless surface and is attached to an ideal spring. The spring is unstretched when the block is at $x_0$. The block is pulled right to $x_f$ and released from rest, after which it completes 12 oscillations in $7.0\ \mathrm{s}$.

  Use $m=0.18\ \mathrm{kg}$, $x_0=0.35\ \mathrm{m}$, and $x_f=0.48\ \mathrm{m}$. What is the block's displacement from equilibrium at $t=3.9\ \mathrm{s}$? Define right as positive.

  ![](<../Source/Images/spring-block-displacement-setup.png>)

  Enter the displacement in meters as a number only:
options:
- id: a
  content: -0.051
  correct: true
  feedback: |-
    The amplitude is $A=x_f-x_0=0.13\ \mathrm{m}$. Since the block is released from maximum positive displacement,

    $$
    x(t)=A\cos(\omega t),
    \qquad
    \omega=2\pi\left(\frac{12}{7.0\ \mathrm{s}}\right).
    $$

    Keeping guard digits through the calculation,

    $$
    x(3.9\ \mathrm{s})
    =(0.13\ \mathrm{m})\cos\left[2\pi\left(\frac{12}{7.0\ \mathrm{s}}\right)(3.9\ \mathrm{s})\right]
    =-0.05109\ldots\ \mathrm{m}.
    $$

    The measured givens support two significant figures, so $x=-0.051\ \mathrm{m}$. The negative sign places the block left of equilibrium.
- id: b
  content: 0.051
  feedback: |-
    This has the correct magnitude but loses the negative sign from the cosine value.
- id: c
  content: 0.13
  feedback: |-
    This is the amplitude; the block is not at maximum positive displacement at \(t=3.9\ \mathrm{s}\).
- id: d
  content: -0.39
  feedback: |-
    This is approximately the dimensionless cosine value before multiplication by the amplitude.
- id: e
  content: 0.097
  feedback: |-
    This is close to a degree-mode calculator result. The phase \(\omega t\) is in radians.
```

---

<a id="summary"></a>
## Summary

For a block pulled right from equilibrium and released from rest:

1. Compute \(A=x_f-x_0\).
2. Compute \(f=N/\Delta t\) and \(\omega=2\pi f\).
3. Use \(x(t)=A\cos(\omega t)\).
4. Reduce any whole cycles, evaluate the cosine in radians, and multiply by \(A\).
5. Keep guard digits, verify \(|x|\le A\), and interpret the sign relative to equilibrium.

**Main traps:** using \(x_f\) as the amplitude, choosing sine despite release at \(+A\), using \(f\) in place of \(\omega\), switching the calculator to degrees, or dropping a negative displacement sign.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
