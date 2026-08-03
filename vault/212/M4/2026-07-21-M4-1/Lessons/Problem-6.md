# Finding Maximum SHM Speed From a Position-Time Graph

<!--
lesson-id: 212-M4-006
topic-code: MTH212.M4.06
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Amplitude From the Vertical Scale](#read-the-amplitude-from-the-vertical-scale)
- [Read the Period From Repeated Points](#read-the-period-from-repeated-points)
- [Convert Graph Readings Into Maximum Speed](#convert-graph-readings-into-maximum-speed)
- [Apply the Procedure to the Oscillator Graph](#apply-the-procedure-to-the-oscillator-graph)
- [Summary](#summary)

## Prerequisites

- Read coordinates and scale markings from a position-time graph.
- Recognize amplitude as maximum displacement from equilibrium.
- Recognize period as the time for one complete cycle.
- Use $\omega=2\pi/T$ and $v_{\max}=A\omega$ for simple harmonic motion.

---

<a id="introduction"></a>
## Introduction

For simple harmonic motion, the maximum speed is

$$
v_{\max}=A\omega.
$$

If a position-time graph gives the period $T$ rather than angular frequency, use

$$
\omega=\frac{2\pi}{T}.
$$

Combining the formulas gives the graph-ready rule

$$
v_{\max}=\frac{2\pi A}{T}.
$$

The recognition cue is a sinusoidal position-time graph together with a request for maximum speed. Read two independent features from the graph:

1. $A$ from the vertical scale.
2. $T$ from the horizontal scale.

Then substitute both into $v_{\max}=2\pi A/T$.

---

<a id="read-the-amplitude-from-the-vertical-scale"></a>
## Read the Amplitude From the Vertical Scale

**Example:** A position graph oscillates between $x=+3.0\ \mathrm{cm}$ and $x=-3.0\ \mathrm{cm}$ about the equilibrium line $x=0$. What is its amplitude?

**Explanation**

Amplitude is the largest displacement from equilibrium:

$$
A=\max|x-x_{\mathrm{eq}}|.
$$

If both graph extremes are known, the same reading can be made with

$$
x_{\mathrm{eq}}=\frac{x_{\max}+x_{\min}}{2}
\qquad\text{and}\qquad
A=\frac{x_{\max}-x_{\min}}{2}.
$$

The equilibrium is $0$, and each extreme is $3.0\ \mathrm{cm}$ from it. Therefore,

$$
A=3.0\ \mathrm{cm}.
$$

The full vertical distance from the minimum to the maximum is $6.0\ \mathrm{cm}$, but that is the peak-to-peak displacement $2A$, not the amplitude.

```quiz
type: radio
id: problem-6-amplitude-q1
content: |-
  An oscillator's position graph ranges from $-4.0\ \mathrm{cm}$ to $+4.0\ \mathrm{cm}$ about $x=0$. What is its amplitude?
options:
- id: a
  content: |-
    $4.0\ \mathrm{cm}$
  correct: true
  feedback: |-
    Amplitude is the distance from equilibrium to either extreme.
- id: b
  content: |-
    $8.0\ \mathrm{cm}$
  feedback: |-
    This is the full peak-to-peak displacement, which equals $2A$.
- id: c
  content: |-
    $2.0\ \mathrm{cm}$
  feedback: |-
    The graph's extreme is $4.0\ \mathrm{cm}$ from equilibrium, not $2.0\ \mathrm{cm}$.
```

---

<a id="read-the-period-from-repeated-points"></a>
## Read the Period From Repeated Points

**Example:** Consecutive maxima on a position-time graph occur at $t=1.0\ \mathrm{s}$ and $t=7.0\ \mathrm{s}$. What is the period?

**Explanation**

The period is the horizontal separation between consecutive points in the same phase of motion. Peak-to-peak is a reliable same-phase pair:

$$
T=7.0\ \mathrm{s}-1.0\ \mathrm{s}=6.0\ \mathrm{s}.
$$

“Same phase” means the oscillator has the same position and is moving in the same direction. Two consecutive peaks or two consecutive troughs automatically satisfy both conditions.

A maximum and the next minimum are separated by only half a cycle, so their time difference is $T/2$, not $T$.

```quiz
type: radio
id: problem-6-period-q1
content: |-
  Consecutive troughs on a position-time graph occur at $t=2.0\ \mathrm{s}$ and $t=7.0\ \mathrm{s}$. What is the period?
options:
- id: a
  content: |-
    $2.5\ \mathrm{s}$
  feedback: |-
    This is half of the full trough-to-trough interval.
- id: b
  content: |-
    $5.0\ \mathrm{s}$
  correct: true
  feedback: |-
    Consecutive troughs have the same phase, so $T=7.0-2.0=5.0\ \mathrm{s}$.
- id: c
  content: |-
    $9.0\ \mathrm{s}$
  feedback: |-
    Period is the difference between the two time coordinates, not their sum.
```

---

<a id="convert-graph-readings-into-maximum-speed"></a>
## Convert Graph Readings Into Maximum Speed

**Example:** A position-time graph gives $A=4.0\ \mathrm{cm}$ and $T=5.0\ \mathrm{s}$. Find the maximum speed.

**Explanation**

First convert period to angular frequency:

$$
\omega=\frac{2\pi}{T}
=\frac{2\pi}{5.0\ \mathrm{s}}.
$$

Then use $v_{\max}=A\omega$:

$$
\begin{aligned}
v_{\max}
&=\frac{2\pi A}{T} \\
&=(4.0\ \mathrm{cm})\frac{2\pi}{5.0\ \mathrm{s}} \\
&=5.026\ldots\ \mathrm{cm/s} \\
&=5.0\ \mathrm{cm/s}.
\end{aligned}
$$

The units follow directly:

$$
(\mathrm{cm})\left(\frac{1}{\mathrm{s}}\right)
=\mathrm{cm/s}.
$$

The factor $2\pi$ is required because one cycle corresponds to $2\pi$ radians.

```quiz
type: radio
id: problem-6-speed-q1
content: |-
  A position-time graph has amplitude $A=3.0\ \mathrm{cm}$ and period $T=2.0\ \mathrm{s}$. What is the oscillator's maximum speed to two significant figures?
options:
- id: a
  content: |-
    $1.5\ \mathrm{cm/s}$
  feedback: |-
    This uses $A/T$ and omits the factor $2\pi$.
- id: b
  content: |-
    $9.4\ \mathrm{cm/s}$
  correct: true
  feedback: |-
    $v_{\max}=2\pi A/T=2\pi(3.0)/2.0=9.424\ldots\ \mathrm{cm/s}$.
- id: c
  content: |-
    $19\ \mathrm{cm/s}$
  feedback: |-
    This effectively uses the full peak-to-peak displacement $2A$ instead of the amplitude.
```

---

<a id="apply-the-procedure-to-the-oscillator-graph"></a>
## Apply the Procedure to the Oscillator Graph

**Example:** Use the graph to find the oscillator's maximum speed.

![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

**Explanation**

Read the graph before choosing a formula:

| Graph feature | Evidence | Reading |
|---|---|---:|
| Equilibrium | The curve is centered on $x=0$ | $x_{\mathrm{eq}}=0$ |
| Vertical extrema | $x=+2.5\ \mathrm{cm}$ and $x=-2.5\ \mathrm{cm}$ | $A=2.5\ \mathrm{cm}$ |
| Repeating points | Maxima at $t=0$, $4.0\ \mathrm{s}$, and $8.0\ \mathrm{s}$ | $T=4.0\ \mathrm{s}$ |

The vertical extrema are $x=\pm2.5\ \mathrm{cm}$, so

$$
A=2.5\ \mathrm{cm}.
$$

Consecutive maxima occur at $t=0$, $4.0\ \mathrm{s}$, and $8.0\ \mathrm{s}$, so

$$
T=4.0\ \mathrm{s}.
$$

Now combine the two readings:

$$
\begin{aligned}
v_{\max}
&=A\frac{2\pi}{T} \\
&=(2.5\ \mathrm{cm})\frac{2\pi}{4.0\ \mathrm{s}} \\
&=3.927\ldots\ \mathrm{cm/s} \\
&=3.9\ \mathrm{cm/s}.
\end{aligned}
$$

```quiz
type: radio
id: m4-1lec-q5
content: |-
  **Question 5**

  The graph shows the position of a simple harmonic oscillator. What is the oscillator's maximum speed?

  ![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

  Enter the maximum speed in centimeters per second as a number only:
options:
- id: a
  content: 3.9
  correct: true
  feedback: |-
    The graph gives $A=2.5\ \mathrm{cm}$ and $T=4.0\ \mathrm{s}$. Therefore,

    $$
    v_{\max}=A\omega
    =A\frac{2\pi}{T}
    =(2.5\ \mathrm{cm})\frac{2\pi}{4.0\ \mathrm{s}}
    =3.927\ldots\ \mathrm{cm/s}.
    $$

    The graph values support two significant figures, so $v_{\max}=3.9\ \mathrm{cm/s}$.
- id: b
  content: 0.63
- id: c
  content: 7.9
- id: d
  content: 1.6
```

---

<a id="summary"></a>
## Summary

To find maximum speed from a sinusoidal position-time graph:

1. Read $A$ from the equilibrium line to one extreme, not from trough to peak.
2. Read $T$ between consecutive maxima, consecutive minima, or another same-phase pair.
3. Use $\omega=2\pi/T$.
4. Compute $v_{\max}=A\omega=2\pi A/T$.
5. Preserve the graph's distance unit, divide by seconds, and round only the final value.

For the given graph, $A=2.5\ \mathrm{cm}$ and $T=4.0\ \mathrm{s}$, so $v_{\max}=3.9\ \mathrm{cm/s}$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../../M5/2026-08-03-Q-3/Study-Guide.md)
Next: [Finding Instantaneous SHM Velocity From Cycle Data](Problem-8.md)

Study guide index: 01/20

---

<!-- lesson-nav:end -->
