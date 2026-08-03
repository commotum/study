# Finding the Maximum Speed of a String Element

<!--
lesson-id: 212-M5-022
topic-code: MTH212.M5.22
-->

## Table of Contents

- [Introduction](#introduction)
- [Differentiate at a Fixed Position](#differentiate-at-a-fixed-position)
- [Use the Velocity Amplitude](#use-the-velocity-amplitude)
- [Separate Element Speed from Wave Speed](#separate-element-speed-from-wave-speed)
- [Ignore Phase and Direction Signs](#ignore-phase-and-direction-signs)
- [Summary](#summary)

## Prerequisites

- Differentiate sine and cosine with the chain rule.
- Use the bounds $|\sin \theta|\leq 1$ and $|\cos \theta|\leq 1$.
- Read amplitude and angular frequency from a traveling-wave equation.

---

<a id="introduction"></a>
## Introduction

When a problem asks for the speed of an **element of the string**, it asks how fast one fixed piece of string moves transversely. Hold its position $x$ constant and differentiate the displacement with respect to time:

$$
v_y(x,t)=\frac{\partial y}{\partial t}.
$$

For

$$
y(x,t)=A\sin(kx-\omega t+\phi),
$$

the transverse velocity is

$$
v_y(x,t)=-A\omega\cos(kx-\omega t+\phi).
$$

Because the magnitude of cosine can reach $1$,

$$
v_{\max}=|A\omega|.
$$

If $A$ and $\omega$ are listed as positive magnitudes, this becomes the shortcut

$$
\boxed{v_{\max}=A\omega}.
$$

The wave number $k$ does not enter this result. It controls how the pattern varies with position, not how rapidly a fixed string element moves up and down.

---

<a id="differentiate-at-a-fixed-position"></a>
## Differentiate at a Fixed Position

**Example:** Find the maximum speed of a string element for the wave in Problem 9:

$$
y(x,t)=(0.1\ \mathrm{m})\sin\left[(2.5\ \mathrm{rad/m})x-(5\ \mathrm{rad/s})t\right].
$$

The provided choices are $0.5\ \mathrm{m/s}$, $0.8\ \mathrm{m/s}$, $1.0\ \mathrm{m/s}$, and $1.3\ \mathrm{m/s}$.

**Explanation**

Let the phase be

$$
\theta=(2.5\ \mathrm{rad/m})x-(5\ \mathrm{rad/s})t.
$$

The string element stays at one fixed $x$, so the $x$-term is constant while differentiating with respect to $t$:

$$
\frac{\partial \theta}{\partial t}=-(5\ \mathrm{rad/s}).
$$

Apply the chain rule:

$$
\begin{aligned}
v_y(x,t)
&=\frac{\partial y}{\partial t} \\
&=(0.1\ \mathrm{m})\cos\theta\,
  \frac{\partial\theta}{\partial t} \\
&=-(0.5\ \mathrm{m/s})\cos\theta.
\end{aligned}
$$

Thus the speed is

$$
|v_y|=(0.5\ \mathrm{m/s})|\cos\theta|.
$$

Its largest possible value occurs when $|\cos\theta|=1$:

$$
\boxed{v_{\max}=0.5\ \mathrm{m/s}}.
$$

```quiz
type: radio
id: p9-q1
content: |-
  A wave on a string is

  $y(x,t)=(0.06\ \mathrm{m})\sin\left[(4\ \mathrm{rad/m})x-(8\ \mathrm{rad/s})t\right]$.

  What is the maximum speed of a string element?
options:
- id: p9-q1-a
  content: |-
    $0.48\ \mathrm{m/s}$
  correct: true
- id: p9-q1-b
  content: |-
    $2.0\ \mathrm{m/s}$
- id: p9-q1-c
  content: |-
    $0.24\ \mathrm{m/s}$
- id: p9-q1-d
  content: |-
    $0.06\ \mathrm{m/s}$
- id: p9-q1-e
  content: |-
    $32\ \mathrm{m/s}$
```

---

<a id="use-the-velocity-amplitude"></a>
## Use the Velocity Amplitude

**Example:** Find the maximum element speed for

$$
y(x,t)=(0.08\ \mathrm{m})\cos\left[(3\ \mathrm{rad/m})x-(12\ \mathrm{rad/s})t\right].
$$

**Explanation**

Let

$$
\theta=(3\ \mathrm{rad/m})x-(12\ \mathrm{rad/s})t.
$$

Differentiating cosine changes it to negative sine. The derivative of the phase supplies another negative sign:

$$
\begin{aligned}
v_y(x,t)
&=\frac{\partial y}{\partial t} \\
&=(0.08\ \mathrm{m})
  (-\sin\theta)(-12\ \mathrm{s}^{-1}) \\
&=(0.96\ \mathrm{m/s})\sin\theta.
\end{aligned}
$$

The velocity ranges from $-0.96\ \mathrm{m/s}$ to $+0.96\ \mathrm{m/s}$. Speed is the magnitude of velocity, so its maximum is the amplitude of the velocity function:

$$
\boxed{v_{\max}=0.96\ \mathrm{m/s}}.
$$

The same shortcut works for either a sine or cosine displacement.

```quiz
type: radio
id: p9-q2
content: |-
  A wave on a string is

  $y(x,t)=(0.05\ \mathrm{m})\cos\left[(6\ \mathrm{rad/m})x+(14\ \mathrm{rad/s})t\right]$.

  What is the maximum speed of a string element?
options:
- id: p9-q2-a
  content: |-
    $0.70\ \mathrm{m/s}$
  correct: true
- id: p9-q2-b
  content: |-
    $2.33\ \mathrm{m/s}$
- id: p9-q2-c
  content: |-
    $0.30\ \mathrm{m/s}$
- id: p9-q2-d
  content: |-
    $14\ \mathrm{m/s}$
- id: p9-q2-e
  content: |-
    $0.05\ \mathrm{m/s}$
```

---

<a id="separate-element-speed-from-wave-speed"></a>
## Separate Element Speed from Wave Speed

**Example:** A wave is

$$
y(x,t)=(0.03\ \mathrm{m})\sin\left[(6\ \mathrm{rad/m})x-(18\ \mathrm{rad/s})t\right].
$$

Find the maximum transverse speed of an element of the string, and compare it with the speed of the wave pattern.

**Explanation**

The maximum transverse speed of one element comes from the time derivative:

$$
v_{\text{element,max}}=A\omega
=(0.03\ \mathrm{m})(18\ \mathrm{s}^{-1})
=0.54\ \mathrm{m/s}.
$$

The speed at which the wave pattern moves along the string is instead

$$
v_{\text{wave}}=\frac{\omega}{k}
=\frac{18\ \mathrm{rad/s}}{6\ \mathrm{rad/m}}
=3.0\ \mathrm{m/s}.
$$

These are different motions:

- $A\omega$ describes a string element moving transversely.
- $\omega/k$ describes the wave shape traveling along the string.

The phrase **element of the string** is the cue to use $A\omega$.

```quiz
type: radio
id: p9-q3
content: |-
  A wave is

  $y(x,t)=(0.04\ \mathrm{m})\sin\left[(5\ \mathrm{rad/m})x-(20\ \mathrm{rad/s})t\right]$.

  What is the maximum transverse speed of an element of the string?
options:
- id: p9-q3-a
  content: |-
    $0.80\ \mathrm{m/s}$
  correct: true
- id: p9-q3-b
  content: |-
    $4.0\ \mathrm{m/s}$
- id: p9-q3-c
  content: |-
    $0.20\ \mathrm{m/s}$
- id: p9-q3-d
  content: |-
    $5.0\ \mathrm{m/s}$
- id: p9-q3-e
  content: |-
    $20\ \mathrm{m/s}$
```

---

<a id="ignore-phase-and-direction-signs"></a>
## Ignore Phase and Direction Signs

**Example:** Find the maximum element speed for

$$
y(x,t)=(0.07\ \mathrm{m})\sin\left[(9\ \mathrm{rad/m})x+(4\ \mathrm{rad/s})t+\frac{\pi}{3}\right].
$$

**Explanation**

Let

$$
\theta=(9\ \mathrm{rad/m})x+(4\ \mathrm{rad/s})t+\frac{\pi}{3}.
$$

Differentiate with respect to time:

$$
v_y(x,t)
=(0.28\ \mathrm{m/s})
\cos\theta.
$$

The plus sign on the time term changes the sign pattern of the velocity compared with the standard $kx-\omega t$ form. The phase shift changes when the extrema occur. Neither changes the largest magnitude:

$$
\boxed{v_{\max}=0.28\ \mathrm{m/s}}.
$$

For any sinusoidal wave written with signed coefficients, take the magnitude of the product of the displacement coefficient and the time coefficient:

$$
v_{\max}=|A\omega|.
$$

```quiz
type: radio
id: p9-q4
content: |-
  A wave is

  $y(x,t)=(0.12\ \mathrm{m})\cos\left[(2.5\ \mathrm{rad/m})x-(7\ \mathrm{rad/s})t-\frac{\pi}{6}\right]$.

  What is the maximum speed of a string element?
options:
- id: p9-q4-a
  content: |-
    $0.84\ \mathrm{m/s}$
  correct: true
- id: p9-q4-b
  content: |-
    $2.8\ \mathrm{m/s}$
- id: p9-q4-c
  content: |-
    $0.30\ \mathrm{m/s}$
- id: p9-q4-d
  content: |-
    $0.12\ \mathrm{m/s}$
- id: p9-q4-e
  content: |-
    $7.0\ \mathrm{m/s}$
```

---

<a id="summary"></a>
## Summary

When a problem asks for the maximum speed of an **element of a string**:

1. Hold $x$ fixed.
2. Compute the transverse velocity $v_y=\partial y/\partial t$.
3. Read the amplitude of the resulting sine or cosine velocity function.
4. Use

$$
\boxed{v_{\max}=|A\omega|}.
$$

For positive amplitude and angular-frequency magnitudes, this is $v_{\max}=A\omega$.

The main trap is using $\omega/k$. That is the propagation speed of the wave pattern, not the maximum transverse speed of one string element.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
