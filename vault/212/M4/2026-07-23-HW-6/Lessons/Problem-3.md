# Choosing an SHM Cosine Equation from a Position–Time Graph

## Table of Contents

- [Introduction](#introduction)
- [Read the Amplitude and Period](#read-the-amplitude-and-period)
- [Convert the Period to Angular Frequency](#convert-the-period-to-angular-frequency)
- [Use the Initial Motion to Choose the Phase](#use-the-initial-motion-to-choose-the-phase)
- [Assemble and Check the Equation](#assemble-and-check-the-equation)
- [Summary](#summary)

## Prerequisites

- Read maximum, minimum, and repeated landmarks from a graph.
- Use the period relation $\omega=2\pi/T$.
- Know the cosine values at $\pm\pi/4$.
- Interpret a rising position graph as positive velocity and a falling graph as negative velocity.

---

<a id="introduction"></a>
## Introduction

A smooth, repeating position graph centered on $x=0$ can be modeled in the form

$$
x(t)=A\cos(\omega t+\phi).
$$

Match each visible feature to only one model parameter:

| Graph feature | Quantity it determines | Rule |
| --- | --- | --- |
| Maximum and minimum position | Amplitude $A$ | $A=(x_{\max}-x_{\min})/2$ |
| Time between consecutive matching landmarks | Period $T$ | $T=t_2-t_1$ |
| One full cycle | Angular frequency $\omega$ | $\omega=2\pi/T$ |
| Initial height and rising/falling direction | Phase $\phi$ | $\cos\phi=x(0)/A$ and $v(0)=-A\omega\sin\phi$ |

This one-parameter-at-a-time approach lets you eliminate wrong equation choices without trying to visualize every complete formula at once.

---

<a id="read-the-amplitude-and-period"></a>
## Read the Amplitude and Period

**Example:** A position graph is centered on $x=0$, reaches $2\ \mathrm{cm}$ and $-2\ \mathrm{cm}$, and has consecutive peaks at $t=1\ \mathrm{s}$ and $t=7\ \mathrm{s}$. Find its amplitude and period.

**Explanation**

The amplitude is half the vertical distance from minimum to maximum:

$$
A=\frac{x_{\max}-x_{\min}}{2}
  =\frac{2\ \mathrm{cm}-(-2\ \mathrm{cm})}{2}
  =2\ \mathrm{cm}.
$$

The period is the horizontal distance between matching points on consecutive cycles:

$$
T=7\ \mathrm{s}-1\ \mathrm{s}=6\ \mathrm{s}.
$$

Use peak-to-peak or trough-to-trough. A peak-to-trough interval is only half a period.

```quiz
type: radio
id: p3-read-a-t
content: |-
  A position graph is centered on zero, has $x_{\max}=3\ \mathrm{cm}$ and $x_{\min}=-3\ \mathrm{cm}$, and has consecutive troughs at $t=2\ \mathrm{s}$ and $t=10\ \mathrm{s}$.

  What are the amplitude $A$ and period $T$?
options:
- id: a
  content: |-
    $A=3\ \mathrm{cm}$ and $T=8\ \mathrm{s}$
  correct: true
- id: b
  content: |-
    $A=6\ \mathrm{cm}$ and $T=8\ \mathrm{s}$
- id: c
  content: |-
    $A=3\ \mathrm{cm}$ and $T=4\ \mathrm{s}$
- id: d
  content: |-
    $A=1.5\ \mathrm{cm}$ and $T=8\ \mathrm{s}$
- id: e
  content: |-
    $A=6\ \mathrm{cm}$ and $T=4\ \mathrm{s}$
```

---

<a id="convert-the-period-to-angular-frequency"></a>
## Convert the Period to Angular Frequency

**Example:** A sinusoidal position graph has period $T=6\ \mathrm{s}$. Find the coefficient of $t$ in a cosine model.

**Explanation**

The coefficient of $t$ is the angular frequency:

$$
\omega=\frac{2\pi}{T}
      =\frac{2\pi}{6\ \mathrm{s}}
      =\frac{\pi}{3\ \mathrm{s}}.
$$

Thus the cosine argument begins as

$$
\frac{\pi}{3\ \mathrm{s}}t+\phi.
$$

The factor $2\pi$ represents one complete cycle. Using $\pi/T$ instead would mistake a half-cycle for a full cycle.

```quiz
type: radio
id: p3-period-to-omega
content: |-
  A position graph has period $T=8\ \mathrm{s}$. What is its angular frequency?
options:
- id: a
  content: |-
    $\dfrac{\pi}{4\ \mathrm{s}}$
  correct: true
- id: b
  content: |-
    $\dfrac{\pi}{8\ \mathrm{s}}$
- id: c
  content: |-
    $\dfrac{4\pi}{\mathrm{s}}$
- id: d
  content: |-
    $\dfrac{8\pi}{\mathrm{s}}$
- id: e
  content: |-
    $\dfrac{16\pi}{\mathrm{s}}$
```

---

<a id="use-the-initial-motion-to-choose-the-phase"></a>
## Use the Initial Motion to Choose the Phase

**Example:** A motion has the form $x(t)=A\cos(\omega t+\phi)$. At $t=0$, the block is at $x(0)=A/\sqrt{2}$ and the position graph is rising. Choose between $\phi=\pi/4$ and $\phi=-\pi/4$.

**Explanation**

First use the initial position:

$$
\frac{x(0)}{A}=\cos\phi=\frac{1}{\sqrt{2}}.
$$

Both $\phi=\pi/4$ and $\phi=-\pi/4$ have this cosine, so the initial height alone cannot choose the sign.

Now use the direction of motion. Differentiating position gives

$$
v(t)=-A\omega\sin(\omega t+\phi),
$$

so

$$
v(0)=-A\omega\sin\phi.
$$

The graph is rising, so $v(0)>0$. Because $A\omega>0$, this requires $\sin\phi<0$. Therefore,

$$
\phi=-\frac{\pi}{4}.
$$

For the convention $x(t)=A\cos(\omega t+\phi)$, the direction test is:

| Initial trend | Sign of $v(0)$ | Required sign of $\sin\phi$ |
| --- | --- | --- |
| Rising | Positive | Negative |
| Falling | Negative | Positive |

The sign inside the cosine is easy to reverse, so use this test instead of guessing from the apparent horizontal shift.

```quiz
type: radio
id: p3-phase-direction
content: |-
  A motion has the form $x(t)=A\cos(\omega t+\phi)$. At $t=0$, $x(0)=A/\sqrt{2}$ and the position graph is falling.

  Which phase is consistent with the graph?
options:
- id: a
  content: |-
    $\phi=\dfrac{\pi}{4}$
  correct: true
- id: b
  content: |-
    $\phi=-\dfrac{\pi}{4}$
- id: c
  content: |-
    $\phi=\dfrac{3\pi}{4}$
- id: d
  content: |-
    $\phi=-\dfrac{3\pi}{4}$
- id: e
  content: |-
    $\phi=0$
```

```quiz
type: radio
id: p3-phase-negative-position
content: |-
  A motion has the form $x(t)=A\cos(\omega t+\phi)$. At $t=0$, $x(0)=-A/\sqrt{2}$ and the position graph is rising.

  Which phase in the interval $[-\pi,\pi]$ is consistent with the graph?
options:
- id: a
  content: |-
    $\phi=-\dfrac{3\pi}{4}$
  correct: true
- id: b
  content: |-
    $\phi=\dfrac{3\pi}{4}$
- id: c
  content: |-
    $\phi=-\dfrac{\pi}{4}$
- id: d
  content: |-
    $\phi=\dfrac{\pi}{4}$
- id: e
  content: |-
    $\phi=\pi$
```

---

<a id="assemble-and-check-the-equation"></a>
## Assemble and Check the Equation

**Example:** A position graph is centered on zero with amplitude $2\ \mathrm{m}$ and period $8\ \mathrm{s}$. At $t=0$, it has $x(0)=2/\sqrt{2}\ \mathrm{m}$ and is rising. Write a cosine model.

**Explanation**

Read and combine the three parameters:

$$
A=2\ \mathrm{m},
\qquad
\omega=\frac{2\pi}{8\ \mathrm{s}}=\frac{\pi}{4\ \mathrm{s}},
\qquad
\phi=-\frac{\pi}{4}.
$$

Therefore,

$$
x(t)=(2\ \mathrm{m})\cos\left(\frac{\pi}{4\ \mathrm{s}}t-\frac{\pi}{4}\right).
$$

For multiple-choice equations, check the candidates in this order:

1. Eliminate any coefficient outside the cosine that disagrees with the amplitude.
2. Eliminate any coefficient of $t$ that disagrees with $\omega=2\pi/T$.
3. Among the remaining choices, use both $x(0)$ and the initial direction to select the phase.

A quick substitution check then confirms that the model has the stated amplitude and period, begins at $2/\sqrt{2}\ \mathrm{m}$, and initially rises.

```quiz
type: radio
id: p3-original-check
content: |-
  The plot below shows the $x$-component of the position of a block undergoing simple harmonic motion.

  According to this plot, which of the following is $x(t)$ for $t$ measured in seconds?

  ![](<../Source/2026-07-23-HW-6/Images/simple-harmonic-motion-position-time-graph.png>)
options:
- id: a
  content: |-
    $(1.5\ \mathrm{m})\cos\left(\dfrac{2\pi}{5\ \mathrm{s}}t-\dfrac{\pi}{4}\right)$
  correct: true
- id: b
  content: |-
    $(1.5\ \mathrm{m})\cos\left(\dfrac{2\pi}{5\ \mathrm{s}}t+\dfrac{\pi}{4}\right)$
- id: c
  content: |-
    $(1.5\ \mathrm{m})\cos\left(\dfrac{4\pi}{5\ \mathrm{s}}t-\dfrac{\pi}{4}\right)$
- id: d
  content: |-
    $(1.5\ \mathrm{m})\cos\left(\dfrac{4\pi}{5\ \mathrm{s}}t+\dfrac{\pi}{4}\right)$
```

**Check**

The graph has extrema at approximately $\pm1.5\ \mathrm{m}$, so $A=1.5\ \mathrm{m}$. Consecutive peaks are $5\ \mathrm{s}$ apart, so

$$
\omega=\frac{2\pi}{5\ \mathrm{s}}.
$$

At $t=0$, the position is approximately $1.5/\sqrt{2}\ \mathrm{m}$ and the curve is rising. The position allows $\phi=\pm\pi/4$, while the rising direction requires $\sin\phi<0$. Thus $\phi=-\pi/4$, which selects option A.

---

<a id="summary"></a>
## Summary

For a graph modeled by $x(t)=A\cos(\omega t+\phi)$:

1. Read $A$ from the vertical extent.
2. Measure $T$ between matching landmarks one full cycle apart.
3. Compute $\omega=2\pi/T$.
4. Use $x(0)/A=\cos\phi$ to find candidate phases.
5. Use the initial direction to choose the phase: in the $+\phi$ convention, a rising graph requires $-\sin\phi>0$.

The main traps are treating peak-to-trough as a full period and choosing the phase sign from the initial height without checking whether the graph is rising or falling.
