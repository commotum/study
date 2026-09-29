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
    Amplitude is the distance from equilibrium to either turning point. The graph reaches $4.0\ \mathrm{cm}$ on either side of $x=0$, so $A=4.0\ \mathrm{cm}$.
- id: b
  content: |-
    $8.0\ \mathrm{cm}$
  feedback: |-
    This uses the full distance from $-4.0\ \mathrm{cm}$ to $+4.0\ \mathrm{cm}$. That peak-to-peak distance is $2A=8.0\ \mathrm{cm}$, so the amplitude is half of it: $A=4.0\ \mathrm{cm}$.
- id: c
  content: |-
    $2.0\ \mathrm{cm}$
  feedback: |-
    Halving is needed only when you start with the full peak-to-peak distance. Here the distance from equilibrium at $0$ to either extreme is already $4.0\ \mathrm{cm}$, so $A=4.0\ \mathrm{cm}$.
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
    Consecutive troughs are one full cycle apart, not half a cycle apart. A half-period would separate a trough from the next peak; the trough-to-trough interval here is $7.0-2.0=5.0\ \mathrm{s}$.
- id: b
  content: |-
    $5.0\ \mathrm{s}$
  correct: true
  feedback: |-
    A period is the time between consecutive points in the same phase. The two troughs are one full cycle apart, so $T=7.0\ \mathrm{s}-2.0\ \mathrm{s}=5.0\ \mathrm{s}$.
- id: c
  content: |-
    $9.0\ \mathrm{s}$
  feedback: |-
    The graph coordinates mark when the troughs occur; elapsed time is final time minus initial time, not their sum. Thus $T=7.0\ \mathrm{s}-2.0\ \mathrm{s}=5.0\ \mathrm{s}$.
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
&=5.026\ldots\ \mathrm{cm}/\mathrm{s} \\
&=5.0\ \mathrm{cm}/\mathrm{s}.
\end{aligned}
$$

The units follow directly:

$$
(\mathrm{cm})\left(\frac{1}{\mathrm{s}}\right)
=\mathrm{cm}/\mathrm{s}.
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
    $1.5\ \mathrm{cm}/\mathrm{s}$
  feedback: |-
    This treats one cycle as one radian by using only $A/T$. One complete SHM cycle spans $2\pi$ radians, so $v_{\max}=2\pi A/T=9.4\ \mathrm{cm}/\mathrm{s}$.
- id: b
  content: |-
    $9.4\ \mathrm{cm}/\mathrm{s}$
  correct: true
  feedback: |-
    Maximum speed is the amplitude times the angular frequency. With $A=3.0\ \mathrm{cm}$ and $\omega=2\pi/T$, $v_{\max}=2\pi(3.0\ \mathrm{cm})/(2.0\ \mathrm{s})=9.4\ \mathrm{cm}/\mathrm{s}$.
- id: c
  content: |-
    $19\ \mathrm{cm}/\mathrm{s}$
  feedback: |-
    This doubles the result by using the peak-to-peak distance $2A$ as the amplitude. Maximum speed uses the one-sided displacement $A=3.0\ \mathrm{cm}$, which gives $v_{\max}=9.4\ \mathrm{cm}/\mathrm{s}$.
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
&=3.927\ldots\ \mathrm{cm}/\mathrm{s} \\
&=3.9\ \mathrm{cm}/\mathrm{s}.
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
    Maximum SHM speed is $v_{\max}=2\pi A/T$. The graph shows a one-sided amplitude of $2.5\ \mathrm{cm}$ and a peak-to-peak period of $4.0\ \mathrm{s}$, so $v_{\max}=3.927\ldots\ \mathrm{cm}/\mathrm{s}=3.9\ \mathrm{cm}/\mathrm{s}$.
- id: b
  content: 0.63
  feedback: |-
    This is $A/T=2.5/4.0=0.625$, which treats one cycle as one radian. The velocity formula needs angular frequency $\omega=2\pi/T$, so including $2\pi$ gives $v_{\max}=3.9\ \mathrm{cm}/\mathrm{s}$.
- id: c
  content: 7.9
  feedback: |-
    This uses the full $5.0\ \mathrm{cm}$ trough-to-peak distance as $A$. That distance is $2A$; the graph's one-sided amplitude is $2.5\ \mathrm{cm}$, so the speed is half this value: $3.9\ \mathrm{cm}/\mathrm{s}$.
- id: d
  content: 1.6
  feedback: |-
    This is the angular frequency $\omega=2\pi/T\approx1.6\ \mathrm{s}^{-1}$, which is a rate rather than a linear speed. Maximum speed also depends on the amplitude: $v_{\max}=A\omega=(2.5\ \mathrm{cm})(1.57\ \mathrm{s}^{-1})=3.9\ \mathrm{cm}/\mathrm{s}$.
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

For the given graph, $A=2.5\ \mathrm{cm}$ and $T=4.0\ \mathrm{s}$, so $v_{\max}=3.9\ \mathrm{cm}/\mathrm{s}$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../../M5/2026-08-03-Q-3/Study-Guide.md)
Next: [Finding Instantaneous SHM Velocity From Cycle Data](Problem-8.md)

Study guide index: 01/28

---
<!-- lesson-nav:end -->
