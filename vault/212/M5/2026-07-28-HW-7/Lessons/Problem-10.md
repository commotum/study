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
y(x,t)=A\sin(kx\pm\omega t+\phi)
$$

or with cosine, the expression inside the sine or cosine is the **phase**. If the question asks for the wave's speed, read two positive magnitudes from that phase:

- $k$ is the coefficient of $x$, usually measured in $\mathrm{rad/m}$.
- $\omega$ is the coefficient of $t$, usually measured in $\mathrm{rad/s}$.

Then compute

$$
v=\frac{\omega}{k}.
$$

| Part of the equation | What to read | Role in the speed |
| --- | --- | --- |
| $A$ outside sine or cosine | Amplitude | Do not use |
| Coefficient of $x$ inside the phase | $k$ | Denominator |
| Magnitude of the coefficient of $t$ inside the phase | $\omega$ | Numerator |

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
y(x,t)=(0.07\ \mathrm{m})\sin\left[(4\ \mathrm{rad/m})x-(12\ \mathrm{rad/s})t\right].
$$

**Explanation**

Look only inside the sine. The coefficient multiplying $x$ is the wave number,

$$
k=4\ \mathrm{rad/m},
$$

and the magnitude of the coefficient multiplying $t$ is the angular frequency,

$$
\omega=12\ \mathrm{rad/s}.
$$

The value $0.07\ \mathrm{m}$ is the amplitude, not either phase coefficient.

```quiz
type: radio
id: p10-coefficients-q1
content: |-
  A wave is

  $y(x,t)=(0.08\ \mathrm{m})\cos\left[(6\ \mathrm{rad/m})x+(15\ \mathrm{rad/s})t\right]$.

  Which pair correctly identifies $k$ and $\omega$?
options:
- id: p10-coefficients-q1-a
  content: |-
    $k=6\ \mathrm{rad/m}$ and $\omega=15\ \mathrm{rad/s}$
  correct: true
- id: p10-coefficients-q1-b
  content: |-
    $k=15\ \mathrm{rad/m}$ and $\omega=6\ \mathrm{rad/s}$
- id: p10-coefficients-q1-c
  content: |-
    $k=0.08\ \mathrm{rad/m}$ and $\omega=15\ \mathrm{rad/s}$
- id: p10-coefficients-q1-d
  content: |-
    $k=6\ \mathrm{rad/m}$ and $\omega=0.08\ \mathrm{rad/s}$
- id: p10-coefficients-q1-e
  content: |-
    $k=21\ \mathrm{rad/m}$ and $\omega=9\ \mathrm{rad/s}$
```

---

<a id="divide-angular-frequency-by-wave-number"></a>
## Divide Angular Frequency by Wave Number

**Example:** A transverse wave travels along a long, taut string. The transverse component of the displacement of the string from its resting configuration satisfies

$$
y(x,t)=(0.1\ \mathrm{m})\sin\left[(2.5\ \mathrm{rad/m})x-(5\ \mathrm{rad/s})t\right].
$$

Here, $x$ is the position along the string when at rest and $t$ is the time relative to a reference time $t=0$. Its possible speeds are $1\ \mathrm{m/s}$, $2\ \mathrm{m/s}$, $3\ \mathrm{m/s}$, and $4\ \mathrm{m/s}$. Find the wave's speed.

**Explanation**

The phase coefficients are

$$
k=2.5\ \mathrm{rad/m}
\qquad\text{and}\qquad
\omega=5\ \mathrm{rad/s}.
$$

Put the time coefficient over the position coefficient:

$$
v=\frac{\omega}{k}
=\frac{5}{2.5}\ \mathrm{m/s}
=2\ \mathrm{m/s}.
$$

Therefore, the correct choice is $\boxed{2\ \mathrm{m/s}}$.

```quiz
type: radio
id: p10-speed-q1
content: |-
  A wave is

  $y(x,t)=(0.04\ \mathrm{m})\sin\left[(6\ \mathrm{rad/m})x-(18\ \mathrm{rad/s})t\right]$.

  What is the speed of the wave?
options:
- id: p10-speed-q1-a
  content: |-
    $\dfrac{1}{3}\ \mathrm{m/s}$
- id: p10-speed-q1-b
  content: |-
    $3\ \mathrm{m/s}$
  correct: true
- id: p10-speed-q1-c
  content: |-
    $12\ \mathrm{m/s}$
- id: p10-speed-q1-d
  content: |-
    $24\ \mathrm{m/s}$
- id: p10-speed-q1-e
  content: |-
    $108\ \mathrm{m/s}$
```

---

<a id="use-units-to-check-the-quotient"></a>
## Use Units to Check the Quotient

**Example:** Check the units when $\omega=8\ \mathrm{rad/s}$ and $k=2\ \mathrm{rad/m}$.

**Explanation**

Keep the units in the speed calculation:

$$
\begin{aligned}
v
&=\frac{8\ \mathrm{rad/s}}{2\ \mathrm{rad/m}} \\
&=4\left(\frac{\mathrm{rad}}{\mathrm{s}}\right)
  \left(\frac{\mathrm{m}}{\mathrm{rad}}\right) \\
&=4\ \mathrm{m/s}.
\end{aligned}
$$

Radians cancel, leaving distance per time. If a calculation instead produces $\mathrm{s/m}$, the quotient was reversed.

```quiz
type: radio
id: p10-units-q1
content: |-
  Which units result from

  $\dfrac{20\ \mathrm{rad/s}}{5\ \mathrm{rad/m}}$?
options:
- id: p10-units-q1-a
  content: |-
    $\mathrm{s/m}$
- id: p10-units-q1-b
  content: |-
    $\mathrm{m/s}$
  correct: true
- id: p10-units-q1-c
  content: |-
    $\mathrm{rad/s}$
- id: p10-units-q1-d
  content: |-
    $\mathrm{rad/m}$
- id: p10-units-q1-e
  content: |-
    $\mathrm{m}\cdot\mathrm{s}$
```

---

<a id="ignore-features-that-do-not-set-the-speed"></a>
## Ignore Features That Do Not Set the Speed

**Example:** Find the speed of

$$
y(x,t)=-(0.25\ \mathrm{m})
\cos\left[(3\ \mathrm{rad/m})x+(7.5\ \mathrm{rad/s})t+\frac{\pi}{4}\right].
$$

**Explanation**

The negative amplitude flips the displacement, cosine replaces sine, and $\pi/4$ shifts the phase. None changes the magnitudes of the $x$- and $t$-coefficients:

$$
k=3\ \mathrm{rad/m},
\qquad
\omega=7.5\ \mathrm{rad/s}.
$$

The plus sign changes the direction of travel, but speed is a magnitude. Therefore,

$$
v=\frac{\omega}{k}
=\frac{7.5}{3}\ \mathrm{m/s}
=2.5\ \mathrm{m/s}.
$$

```quiz
type: radio
id: p10-features-q1
content: |-
  A wave is

  $y(x,t)=-(0.20\ \mathrm{m})\cos\left[(4\ \mathrm{rad/m})x+(10\ \mathrm{rad/s})t-\frac{\pi}{3}\right]$.

  What is the speed of the wave?
options:
- id: p10-features-q1-a
  content: |-
    $0.20\ \mathrm{m/s}$
- id: p10-features-q1-b
  content: |-
    $0.40\ \mathrm{m/s}$
- id: p10-features-q1-c
  content: |-
    $2.5\ \mathrm{m/s}$
  correct: true
- id: p10-features-q1-d
  content: |-
    $6\ \mathrm{m/s}$
- id: p10-features-q1-e
  content: |-
    $14\ \mathrm{m/s}$
```

---

<a id="summary"></a>
## Summary

When a traveling wave is written as $y=A\sin(kx\pm\omega t+\phi)$ or with cosine:

1. Look inside the sine or cosine.
2. Read $k$ from the coefficient of $x$.
3. Read $\omega$ from the magnitude of the coefficient of $t$.
4. Compute $v=\omega/k$.
5. Check that $(\mathrm{rad/s})/(\mathrm{rad/m})$ simplifies to $\mathrm{m/s}$.

Do not use the amplitude, reverse the quotient, or let sine versus cosine or a constant phase shift distract you. The sign between the phase terms affects direction, not the speed's magnitude.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Wave Speed in a Wire Tensioned by a Hanging Mass](../../2026-07-27-M5-2/Lessons/Problem-2.md)

Study guide index: 09/20

---

<!-- lesson-nav:end -->
