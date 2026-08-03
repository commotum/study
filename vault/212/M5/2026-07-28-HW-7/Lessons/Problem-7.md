# Reading a Wave's Direction from Its Phase

<!--
lesson-id: 212-M5-020
topic-code: MTH212.M5.20
-->

## Table of Contents

- [Introduction](#introduction)
- [Track One Point of Constant Phase](#track-one-point-of-constant-phase)
- [Recognize the Plus-Sign Case](#recognize-the-plus-sign-case)
- [Ignore Amplitude and Constant Phase Shifts](#ignore-amplitude-and-constant-phase-shifts)
- [Handle Any Signed Linear Phase](#handle-any-signed-linear-phase)
- [Summary](#summary)

## Prerequisites

- Solve a linear equation for $x$.
- Interpret positive motion as travel toward increasing $x$ and negative motion as travel toward decreasing $x$.

---

<a id="introduction"></a>
## Introduction

When a traveling wave is written as

$$
y(x,t)=A\sin(kx\pm \omega t+\phi)
$$

or with cosine, the sign connecting the $x$-term and the $t$-term reveals its direction. The reliable procedure is to hold the phase—the expression inside sine or cosine—constant and solve for how $x$ changes with $t$.

A crest, trough, or other fixed point in the repeating pattern has constant phase. Its horizontal velocity is

$$
v_{\text{pattern}}=\frac{dx}{dt}.
$$

For positive $k$ and $\omega$:

- $kx-\omega t+\phi$ gives $v_{\text{pattern}}=+\omega/k$, so the wave moves toward increasing $x$.
- $kx+\omega t+\phi$ gives $v_{\text{pattern}}=-\omega/k$, so the wave moves toward decreasing $x$.

**Watch out:** The minus sign in $kx-\omega t$ does **not** mean motion in the negative direction. Solving the constant-phase equation produces a positive pattern velocity. Also, $v_{\text{pattern}}$ describes the horizontal travel of the wave shape; it is not the vertical velocity of a small piece of string.

---

<a id="track-one-point-of-constant-phase"></a>
## Track One Point of Constant Phase

**Example:** Determine the direction of the wave from Problem 7:

$$
y(x,t)=(0.1\ \mathrm{m})\sin\left[(2.5\ \mathrm{rad/m})x-(5\ \mathrm{rad/s})t\right].
$$

**Explanation**

Track one crest, trough, or any other fixed point in the pattern by setting its phase equal to a constant $C$:

$$
(2.5\ \mathrm{rad/m})x-(5\ \mathrm{rad/s})t=C.
$$

Solving for $x$ gives

$$
x=(2\ \mathrm{m/s})t+\frac{C}{2.5\ \mathrm{rad/m}}.
$$

The tracked pattern point has

$$
v_{\text{pattern}}=\frac{dx}{dt}=+2\ \mathrm{m/s}.
$$

As $t$ increases, $x$ increases. Therefore, the wave travels toward **increasing $x$**, matching the “Increasing” answer choice.

```quiz
type: radio
id: p7-q1
content: |-
  A wave is

  $y(x,t)=(0.03\ \mathrm{m})\sin\left[(4\ \mathrm{rad/m})x-(12\ \mathrm{rad/s})t\right]$.

  In which direction does it travel?
options:
- id: p7-q1-a
  content: |-
    Increasing $x$
  correct: true
- id: p7-q1-b
  content: |-
    Decreasing $x$
```

---

<a id="recognize-the-plus-sign-case"></a>
## Recognize the Plus-Sign Case

**Example:** Determine the direction of

$$
y(x,t)=(0.06\ \mathrm{m})\cos\left[(6\ \mathrm{rad/m})x+(9\ \mathrm{rad/s})t\right].
$$

**Explanation**

Hold the phase constant:

$$
6x+9t=C.
$$

Then

$$
x=-1.5t+\frac{C}{6}.
$$

The tracked point moves to smaller $x$ as time increases, so the wave travels toward **decreasing $x$**. With positive $k$ and $\omega$, a plus sign between the space and time terms means decreasing-$x$ travel.

```quiz
type: radio
id: p7-q2
content: |-
  A wave is

  $y(x,t)=(0.08\ \mathrm{m})\cos\left[(5\ \mathrm{rad/m})x+(20\ \mathrm{rad/s})t\right]$.

  In which direction does it travel?
options:
- id: p7-q2-a
  content: |-
    Increasing $x$
- id: p7-q2-b
  content: |-
    Decreasing $x$
  correct: true
```

---

<a id="ignore-amplitude-and-constant-phase-shifts"></a>
## Ignore Amplitude and Constant Phase Shifts

**Example:** Determine the direction of

$$
y(x,t)=-(0.20\ \mathrm{m})\sin\left[(3\ \mathrm{rad/m})x-(7.5\ \mathrm{rad/s})t+\frac{\pi}{4}\right].
$$

**Explanation**

The negative amplitude flips the wave vertically, and $\pi/4$ shifts the pattern's phase. Neither changes how a point of constant phase moves:

$$
3x-7.5t+\frac{\pi}{4}=C
$$

gives

$$
x=2.5t+\frac{C-\pi/4}{3}.
$$

The coefficient of $t$ is positive, so $v_{\text{pattern}}>0$ and the wave travels toward increasing $x$.

```quiz
type: radio
id: p7-q3
content: |-
  A wave is

  $y(x,t)=-(0.10\ \mathrm{m})\cos\left[(8\ \mathrm{rad/m})x+(4\ \mathrm{rad/s})t-\frac{\pi}{6}\right]$.

  In which direction does it travel?
options:
- id: p7-q3-a
  content: |-
    Increasing $x$ because the amplitude is negative
- id: p7-q3-b
  content: |-
    Decreasing $x$ because a constant-phase point has $dx/dt<0$
  correct: true
- id: p7-q3-c
  content: |-
    Increasing $x$ because the phase shift is negative
- id: p7-q3-d
  content: |-
    The direction cannot be determined because the wave uses cosine
```

---

<a id="handle-any-signed-linear-phase"></a>
## Handle Any Signed Linear Phase

**Example:** Determine the direction of a wave whose phase is

$$
(-4\ \mathrm{rad/m})x+(10\ \mathrm{rad/s})t+\phi.
$$

**Explanation**

For any linear phase $ax+bt+\phi$, hold the phase constant and solve for $x$:

$$
ax+bt+\phi=C
$$

which gives

$$
x=-\frac{b}{a}t+\frac{C-\phi}{a}.
$$

Therefore,

$$
v_{\text{pattern}}=\frac{dx}{dt}=-\frac{b}{a}.
$$

Here,

$$
v_{\text{pattern}}=-\frac{10\ \mathrm{rad/s}}{-4\ \mathrm{rad/m}}
=2.5\ \mathrm{m/s}.
$$

The positive sign means the wave travels toward increasing $x$. This signed-coefficient test prevents mistakes when the equation is not already written with positive $k$ and $\omega$.

```quiz
type: radio
id: p7-q4
content: |-
  A wave has phase

  $(-5\ \mathrm{rad/m})x-(15\ \mathrm{rad/s})t+\phi$.

  In which direction does it travel?
options:
- id: p7-q4-a
  content: |-
    Increasing $x$ at $3\ \mathrm{m/s}$
- id: p7-q4-b
  content: |-
    Decreasing $x$ at $3\ \mathrm{m/s}$
  correct: true
- id: p7-q4-c
  content: |-
    Decreasing $x$ at $\frac{1}{3}\ \mathrm{m/s}$
- id: p7-q4-d
  content: |-
    The direction cannot be determined because both coefficients are negative
```

---

<a id="summary"></a>
## Summary

To read a traveling wave's direction:

1. Identify the phase inside sine or cosine.
2. Set that phase equal to a constant.
3. Solve for $x$ as a function of $t$, or use $v_{\text{pattern}}=-b/a$ for phase $ax+bt+\phi$.
4. Read the sign: $v_{\text{pattern}}>0$ means increasing $x$, while $v_{\text{pattern}}<0$ means decreasing $x$.

For the standard form with positive $k$ and $\omega$, $kx-\omega t$ travels toward increasing $x$ and $kx+\omega t$ travels toward decreasing $x$. Amplitude, sine versus cosine, and a constant phase shift do not change the direction.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
