# Finding Wave Speed from a Traveling-Wave Equation

<!--
lesson-id: 212-M5-023
topic-code: MTH212.M5.23
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Two Phase Coefficients](#read-the-two-phase-coefficients)
- [Divide Angular Frequency by Wave Number](#divide-angular-frequency-by-wave-number)
- [Use Units to Check the Quotient](#use-units-to-check-the-quotient)
- [Ignore Features That Do Not Set the Speed](#ignore-features-that-do-not-set-the-speed)
- [Summary](#summary)

## Prerequisites

- Identify the numerical coefficient of a variable in an expression.
- Divide positive decimals.

---

<a id="introduction"></a>
## Introduction

When a traveling sinusoidal wave is written in the form

$$
y(x,t)=A\sin(kx\pm\omega t+\phi_0)
$$

or with cosine, the expression inside the sine or cosine is the **phase**. If the question asks for the wave's speed, read two positive magnitudes from that phase:

- $k$ is the coefficient of $x$, usually measured in $\mathrm{rad}/\mathrm{m}$.
- $\omega$ is the coefficient of $t$, usually measured in $\mathrm{rad}/\mathrm{s}$.

Then compute

$$
v_{\mathrm{wave}}=\frac{\omega}{k}.
$$

| Part of the equation                                 | What to read | Role in the speed |
| ---------------------------------------------------- | ------------ | ----------------- |
| $A$ outside sine or cosine                           | Amplitude    | Do not use        |
| Coefficient of $x$ inside the phase                  | $k$          | Denominator       |
| Magnitude of the coefficient of $t$ inside the phase | $\omega$     | Numerator         |

A point that stays on the same crest or trough has constant phase. For the minus-sign form,

$$
kx-\omega t=C
\quad\Longrightarrow\quad
x=\frac{\omega}{k}t+\frac{C}{k},
$$

so the pattern's speed has magnitude $\omega/k$.

The amplitude $A$ is outside the phase, so it does not enter this quotient. The plus or minus sign between the phase terms determines direction, but not the magnitude of the speed.

---

<a id="read-the-two-phase-coefficients"></a>
## Read the Two Phase Coefficients

**Example:** Identify $k$ and $\omega$ in

$$
y(x,t)=(0.07\ \mathrm{m})\sin\left[(4\ \mathrm{rad}/\mathrm{m})x-(12\ \mathrm{rad}/\mathrm{s})t\right].
$$

**Explanation**

Look only inside the sine. The coefficient multiplying $x$ is the wave number,

$$
k=4\ \mathrm{rad}/\mathrm{m},
$$

and the magnitude of the coefficient multiplying $t$ is the angular frequency,

$$
\omega=12\ \mathrm{rad}/\mathrm{s}.
$$

The value $0.07\ \mathrm{m}$ is the amplitude, not either phase coefficient.

```quiz
type: radio
id: p10-coefficients-q1
content: |-
  A wave is

  $y(x,t)=(0.08\ \mathrm{m})\cos\left[(6\ \mathrm{rad}/\mathrm{m})x+(15\ \mathrm{rad}/\mathrm{s})t\right]$.

  Which pair correctly identifies $k$ and $\omega$?
options:
- id: p10-coefficients-q1-a
  content: |-
    $k=6\ \mathrm{rad}/\mathrm{m}$ and $\omega=15\ \mathrm{rad}/\mathrm{s}$
  correct: true
  feedback: |-
    In a traveling-wave phase, $k$ measures phase change per distance and therefore multiplies $x$, while $\omega$ measures phase change per time and multiplies $t$. Thus $k=6\ \mathrm{rad}/\mathrm{m}$ and $\omega=15\ \mathrm{rad}/\mathrm{s}$.
- id: p10-coefficients-q1-b
  content: |-
    $k=15\ \mathrm{rad}/\mathrm{m}$ and $\omega=6\ \mathrm{rad}/\mathrm{s}$
  feedback: |-
    This swaps the spatial and temporal roles. The coefficient of position $x$ is the wave number $k=6\ \mathrm{rad}/\mathrm{m}$, while the coefficient of time $t$ is the angular frequency $\omega=15\ \mathrm{rad}/\mathrm{s}$.
- id: p10-coefficients-q1-c
  content: |-
    $k=0.08\ \mathrm{rad}/\mathrm{m}$ and $\omega=15\ \mathrm{rad}/\mathrm{s}$
  feedback: |-
    This mistakes the maximum displacement for a phase coefficient. The outside factor $0.08\ \mathrm{m}$ is the amplitude $A$; $k$ is read from the coefficient multiplying $x$ inside the cosine, so $k=6\ \mathrm{rad}/\mathrm{m}$.
- id: p10-coefficients-q1-d
  content: |-
    $k=6\ \mathrm{rad}/\mathrm{m}$ and $\omega=0.08\ \mathrm{rad}/\mathrm{s}$
  feedback: |-
    This assigns the displacement amplitude to angular frequency. Amplitude sits outside the trigonometric function, while $\omega$ is the coefficient of $t$ inside the phase: $\omega=15\ \mathrm{rad}/\mathrm{s}$.
- id: p10-coefficients-q1-e
  content: |-
    $k=21\ \mathrm{rad}/\mathrm{m}$ and $\omega=9\ \mathrm{rad}/\mathrm{s}$
  feedback: |-
    This combines coefficients with different physical roles and units. Wave number and angular frequency are read separately from the multipliers of $x$ and $t$, giving $k=6\ \mathrm{rad}/\mathrm{m}$ and $\omega=15\ \mathrm{rad}/\mathrm{s}$ without addition or subtraction.
```

---

<a id="divide-angular-frequency-by-wave-number"></a>
## Divide Angular Frequency by Wave Number

**Example:** A transverse wave travels along a long, taut string. The transverse component of the displacement of the string from its resting configuration satisfies

$$
y(x,t)=(0.1\ \mathrm{m})\sin\left[(2.5\ \mathrm{rad}/\mathrm{m})x-(5\ \mathrm{rad}/\mathrm{s})t\right].
$$

Here, $x$ is the position along the string when at rest and $t$ is the time relative to a reference time $t=0$. Its possible speeds are $1\ \mathrm{m}/\mathrm{s}$, $2\ \mathrm{m}/\mathrm{s}$, $3\ \mathrm{m}/\mathrm{s}$, and $4\ \mathrm{m}/\mathrm{s}$. Find the wave's speed.

**Explanation**

The phase coefficients are

$$
k=2.5\ \mathrm{rad}/\mathrm{m}
\qquad\text{and}\qquad
\omega=5\ \mathrm{rad}/\mathrm{s}.
$$

Put the time coefficient over the position coefficient:

$$
v_{\mathrm{wave}}=\frac{\omega}{k}
=\frac{5}{2.5}\ \mathrm{m}/\mathrm{s}
=2\ \mathrm{m}/\mathrm{s}.
$$

Therefore, the correct choice is $\boxed{2\ \mathrm{m}/\mathrm{s}}$.

```quiz
type: radio
id: p10-speed-q1
content: |-
  A wave is

  $y(x,t)=(0.04\ \mathrm{m})\sin\left[(6\ \mathrm{rad}/\mathrm{m})x-(18\ \mathrm{rad}/\mathrm{s})t\right]$.

  What is the speed of the wave?
options:
- id: p10-speed-q1-a
  content: |-
    $\dfrac{1}{3}\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This takes the reciprocal of the propagation speed. Holding the phase $kx-\omega t$ constant gives $dx/dt=\omega/k$; $k/\omega$ has units of time per distance, not speed.
- id: p10-speed-q1-b
  content: |-
    $3\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    A point of constant phase satisfies $kx-\omega t=\text{constant}$, so the pattern speed is $v_{\mathrm{wave}}=\omega/k$. Here $\omega=18\ \mathrm{rad}/\mathrm{s}$ and $k=6\ \mathrm{rad}/\mathrm{m}$, giving $v_{\mathrm{wave}}=3\ \mathrm{m}/\mathrm{s}$.
- id: p10-speed-q1-c
  content: |-
    $12\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This subtracts angular frequency and wave number, quantities with different units that cannot be subtracted. Constant phase relates distance traveled to elapsed time through the quotient $\omega/k=3\ \mathrm{m}/\mathrm{s}$.
- id: p10-speed-q1-d
  content: |-
    $24\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This adds coefficients with incompatible units, $\mathrm{rad}/\mathrm{s}$ and $\mathrm{rad}/\mathrm{m}$. Wave speed is the rate at which constant phase moves, so the needed operation is $\omega/k=18/6=3\ \mathrm{m}/\mathrm{s}$.
- id: p10-speed-q1-e
  content: |-
    $108\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    Multiplication produces units that are not velocity and does not follow the constant-phase condition. Dividing angular frequency by wave number cancels radians and gives $v_{\mathrm{wave}}=18/6=3\ \mathrm{m}/\mathrm{s}$.
```

---

<a id="use-units-to-check-the-quotient"></a>
## Use Units to Check the Quotient

**Example:** Check the units when $\omega=8\ \mathrm{rad}/\mathrm{s}$ and $k=2\ \mathrm{rad}/\mathrm{m}$.

**Explanation**

Keep the units in the speed calculation:

$$
\begin{aligned}
v_{\mathrm{wave}}
&=\frac{8\ \mathrm{rad}/\mathrm{s}}{2\ \mathrm{rad}/\mathrm{m}} \\
&=4\left(\frac{\mathrm{rad}}{\mathrm{s}}\right)
  \left(\frac{\mathrm{m}}{\mathrm{rad}}\right) \\
&=4\ \mathrm{m}/\mathrm{s}.
\end{aligned}
$$

Radians cancel, leaving distance per time. If a calculation instead produces $\mathrm{s}/\mathrm{m}$, the quotient was reversed.

```quiz
type: radio
id: p10-units-q1
content: |-
  Which units result from

  $\dfrac{20\ \mathrm{rad}/\mathrm{s}}{5\ \mathrm{rad}/\mathrm{m}}$?
options:
- id: p10-units-q1-a
  content: |-
    $\mathrm{s}/\mathrm{m}$
  feedback: |-
    This reverses the quotient. Seconds per meter would describe the reciprocal of a speed, $k/\omega$; the stated expression is $\omega/k$ and therefore has units of meters per second.
- id: p10-units-q1-b
  content: |-
    $\mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    Dividing by $5\ \mathrm{rad}/\mathrm{m}$ means multiplying by $\mathrm{m}/\mathrm{rad}$. The radians cancel in $(\mathrm{rad}/\mathrm{s})(\mathrm{m}/\mathrm{rad})$, leaving the speed unit $\mathrm{m}/\mathrm{s}$.
- id: p10-units-q1-c
  content: |-
    $\mathrm{rad}/\mathrm{s}$
  feedback: |-
    These are only the numerator's units. Division by wave number multiplies by $\mathrm{m}/\mathrm{rad}$, canceling radians and introducing meters, so the final unit is $\mathrm{m}/\mathrm{s}$ rather than $\mathrm{rad}/\mathrm{s}$.
- id: p10-units-q1-d
  content: |-
    $\mathrm{rad}/\mathrm{m}$
  feedback: |-
    These are the denominator's units copied unchanged. In the quotient, $\mathrm{rad}/\mathrm{m}$ is inverted to $\mathrm{m}/\mathrm{rad}$; combining it with $\mathrm{rad}/\mathrm{s}$ leaves $\mathrm{m}/\mathrm{s}$.
- id: p10-units-q1-e
  content: |-
    $\mathrm{m}\cdot\mathrm{s}$
  feedback: |-
    This inverts the spatial unit correctly but also moves seconds out of the denominator. The numerator remains per second, so $(\mathrm{rad}/\mathrm{s})(\mathrm{m}/\mathrm{rad})=\mathrm{m}/\mathrm{s}$, not $\mathrm{m\,s}$.
```

---

<a id="ignore-features-that-do-not-set-the-speed"></a>
## Ignore Features That Do Not Set the Speed

**Example:** Find the speed of

$$
y(x,t)=-(0.25\ \mathrm{m})
\cos\left[(3\ \mathrm{rad}/\mathrm{m})x+(7.5\ \mathrm{rad}/\mathrm{s})t+\frac{\pi}{4}\right].
$$

**Explanation**

The negative amplitude flips the displacement, cosine replaces sine, and $\pi/4$ shifts the phase. None changes the magnitudes of the $x$- and $t$-coefficients:

$$
k=3\ \mathrm{rad}/\mathrm{m},
\qquad
\omega=7.5\ \mathrm{rad}/\mathrm{s}.
$$

The plus sign changes the direction of travel, but speed is a magnitude. Therefore,

$$
v_{\mathrm{wave}}=\frac{\omega}{k}
=\frac{7.5}{3}\ \mathrm{m}/\mathrm{s}
=2.5\ \mathrm{m}/\mathrm{s}.
$$

```quiz
type: radio
id: p10-features-q1
content: |-
  A wave is

  $y(x,t)=-(0.20\ \mathrm{m})\cos\left[(4\ \mathrm{rad}/\mathrm{m})x+(10\ \mathrm{rad}/\mathrm{s})t-\frac{\pi}{3}\right]$.

  What is the speed of the wave?
options:
- id: p10-features-q1-a
  content: |-
    $0.20\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This mistakes the displacement amplitude for a propagation speed. The outside factor $0.20\ \mathrm{m}$ controls the wave's vertical size; speed comes from the spatial and temporal phase coefficients, $v_{\mathrm{wave}}=\omega/k$.
- id: p10-features-q1-b
  content: |-
    $0.40\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This reverses the phase-coefficient quotient: $k/\omega=4/10=0.40$, but $k/\omega$ has units of $\mathrm{s}/\mathrm{m}$, not speed. A fixed phase instead gives $v_{\mathrm{wave}}=\omega/k=10/4=2.5\ \mathrm{m}/\mathrm{s}$.
- id: p10-features-q1-c
  content: |-
    $2.5\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    Wave speed is set by the rate at which a fixed phase moves, so its magnitude is $v_{\mathrm{wave}}=\omega/k$. The phase gives $\omega=10\ \mathrm{rad}/\mathrm{s}$ and $k=4\ \mathrm{rad}/\mathrm{m}$, hence $v_{\mathrm{wave}}=2.5\ \mathrm{m}/\mathrm{s}$.
- id: p10-features-q1-d
  content: |-
    $6\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This subtracts coefficients with incompatible units. The plus sign in $kx+\omega t$ sets the propagation direction, while the requested speed magnitude comes from the quotient $\omega/k=10/4=2.5\ \mathrm{m}/\mathrm{s}$.
- id: p10-features-q1-e
  content: |-
    $14\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This adds a temporal rate to a spatial rate, so the operation is not physically meaningful. Holding $4x+10t-\pi/3$ constant gives a speed magnitude $|dx/dt|=\omega/k=2.5\ \mathrm{m}/\mathrm{s}$.
```

---

<a id="summary"></a>
## Summary

When a traveling wave is written as $y=A\sin(kx\pm\omega t+\phi_0)$ or with cosine:

1. Look inside the sine or cosine.
2. Read $k$ from the coefficient of $x$.
3. Read $\omega$ from the magnitude of the coefficient of $t$.
4. Compute $v_{\mathrm{wave}}=\omega/k$.
5. Check that $(\mathrm{rad}/\mathrm{s})/(\mathrm{rad}/\mathrm{m})$ simplifies to $\mathrm{m}/\mathrm{s}$.

Do not use the amplitude, reverse the quotient, or let sine versus cosine or a constant phase shift distract you. The sign between the phase terms affects direction, not the speed's magnitude.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Wave Speed in a Wire Tensioned by a Hanging Mass](../../2026-07-27-M5-2/Lessons/Problem-2.md)

Study guide index: 10/28

---
<!-- lesson-nav:end -->
