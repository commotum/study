# Maximum Kinetic Energy from an SHM Position–Time Graph

## Table of Contents

- [Introduction](#introduction)
- [Read Amplitude and Period](#read-amplitude-and-period)
- [Turn Period into Angular Frequency](#turn-period-into-angular-frequency)
- [Connect the Graph to Maximum Kinetic Energy](#connect-the-graph-to-maximum-kinetic-energy)
- [Avoid the Peak-to-Peak Trap](#avoid-the-peak-to-peak-trap)
- [Solve the Given Graph](#solve-the-given-graph)
- [Summary](#summary)

## Prerequisites

- Read coordinates and repeated features from a position–time graph.
- Use $K=\dfrac12 mv^2$.
- Square fractions and quantities with units.

---

<a id="introduction"></a>
## Introduction

When a problem gives a sinusoidal position–time graph, a mass, and asks for the maximum kinetic energy, read the graph's **amplitude** $A$ and **period** $T$. Then use

$$
\omega=\frac{2\pi}{T},
\qquad
v_{\max}=\omega A,
\qquad
K_{\max}=\frac12 m(\omega A)^2.
$$

The maximum kinetic energy occurs as the block passes through equilibrium, where its speed is greatest. The graph supplies $A$ and $T$ even when neither is stated in the text.

| Use | Read |
| --- | --- |
| Position–time graph | Amplitude $A$ and period $T$ |
| Problem text | Mass $m$ |
| Not needed for $K_{\max}$ | Starting position, direction of motion, and phase |

---

<a id="read-amplitude-and-period"></a>
## Read Amplitude and Period

**Example:** Read $A$ and $T$ from the graph used in the assignment.

![](<../Source/2026-07-23-HW-6/Images/simple-harmonic-motion-position-time-graph.png>)

**Explanation**

The equilibrium line is $x=0$. The graph reaches about $+1.5\ \mathrm{m}$ and $-1.5\ \mathrm{m}$, so the amplitude—the maximum distance from equilibrium—is

$$
A=1.5\ \mathrm{m}.
$$

Two consecutive crests occur about $5.0\ \mathrm{s}$ apart. This is the smallest positive time shift that repeats the motion, so

$$
T=5.0\ \mathrm{s}.
$$

Measure the period between matching points moving in the same direction, such as crest to crest. A crest-to-trough interval is only half a period. The height of the graph gives $A$; where the cycle happens to begin does not affect $K_{\max}$.

```quiz
type: radio
id: p4-read-graph
content: |-
  A position–time graph oscillates between $+0.80\ \mathrm{m}$ and $-0.80\ \mathrm{m}$. Consecutive crests occur at $t=1.2\ \mathrm{s}$ and $t=4.2\ \mathrm{s}$. What are the amplitude and period?
options:
- id: a
  content: |-
    $A=0.80\ \mathrm{m}$ and $T=3.0\ \mathrm{s}$
  correct: true
- id: b
  content: |-
    $A=1.60\ \mathrm{m}$ and $T=3.0\ \mathrm{s}$
- id: c
  content: |-
    $A=0.80\ \mathrm{m}$ and $T=1.5\ \mathrm{s}$
- id: d
  content: |-
    $A=1.60\ \mathrm{m}$ and $T=1.5\ \mathrm{s}$
- id: e
  content: |-
    $A=0.80\ \mathrm{m}$ and $T=5.4\ \mathrm{s}$
```

---

<a id="turn-period-into-angular-frequency"></a>
## Turn Period into Angular Frequency

**Example:** For a period of $5.0\ \mathrm{s}$, find the angular frequency.

**Explanation**

One cycle covers $2\pi$ radians of phase, so divide $2\pi$ by the time for one cycle:

$$
\omega=\frac{2\pi}{T}
=\frac{2\pi}{5.0\ \mathrm{s}}
=\frac{2\pi}{5}\ \mathrm{rad/s}.
$$

Ordinary frequency is $f=1/T$, but the speed relation uses angular frequency $\omega=2\pi f$. Omitting $2\pi$ changes the energy by a factor of $4\pi^2$.

```quiz
type: radio
id: p4-angular-frequency
content: |-
  An oscillator has period $T=8.0\ \mathrm{s}$. What is its angular frequency?
options:
- id: a
  content: |-
    $\dfrac{1}{8}\ \mathrm{rad/s}$
- id: b
  content: |-
    $\dfrac{\pi}{8}\ \mathrm{rad/s}$
- id: c
  content: |-
    $\dfrac{\pi}{4}\ \mathrm{rad/s}$
  correct: true
- id: d
  content: |-
    $4\pi\ \mathrm{rad/s}$
- id: e
  content: |-
    $8\pi\ \mathrm{rad/s}$
```

---

<a id="connect-the-graph-to-maximum-kinetic-energy"></a>
## Connect the Graph to Maximum Kinetic Energy

**Example:** A $1.5\ \mathrm{kg}$ block oscillates with $A=0.40\ \mathrm{m}$ and $T=2.0\ \mathrm{s}$. Find its maximum kinetic energy.

**Explanation**

At equilibrium, the speed and kinetic energy are greatest. First find

$$
\omega=\frac{2\pi}{2.0\ \mathrm{s}}=\pi\ \mathrm{rad/s},
\qquad
v_{\max}=\omega A=(\pi)(0.40)=0.40\pi\ \mathrm{m/s}.
$$

Then

$$
K_{\max}
=\frac12(1.5)(0.40\pi)^2
=0.12\pi^2\ \mathrm{J}.
$$

The same steps can be compressed into one graph-to-energy formula:

$$
\boxed{K_{\max}=\frac12m\left(\frac{2\pi A}{T}\right)^2}.
$$

```quiz
type: radio
id: p4-compute-energy
content: |-
  A $2.0\ \mathrm{kg}$ block has amplitude $0.50\ \mathrm{m}$ and period $4.0\ \mathrm{s}$. What is its maximum kinetic energy?
options:
- id: a
  content: |-
    $\dfrac{\pi^2}{64}\ \mathrm{J}$
- id: b
  content: |-
    $\dfrac{\pi^2}{32}\ \mathrm{J}$
- id: c
  content: |-
    $\dfrac{\pi^2}{16}\ \mathrm{J}$
  correct: true
- id: d
  content: |-
    $\dfrac{\pi^2}{4}\ \mathrm{J}$
- id: e
  content: |-
    $\dfrac{1}{4}\ \mathrm{J}$
```

---

<a id="avoid-the-peak-to-peak-trap"></a>
## Avoid the Peak-to-Peak Trap

**Example:** A graph ranges from $-2.0\ \mathrm{m}$ to $+2.0\ \mathrm{m}$. Which length belongs in $K_{\max}=\dfrac12m(2\pi A/T)^2$?

**Explanation**

The total peak-to-peak range is $4.0\ \mathrm{m}$, but amplitude is measured from equilibrium to one extreme:

$$
A=2.0\ \mathrm{m}.
$$

Because $A$ is squared, using the $4.0\ \mathrm{m}$ peak-to-peak range would make the computed energy four times too large. Also square the entire speed $\omega A$, not just one factor.

```quiz
type: radio
id: p4-peak-to-peak
content: |-
  A student reads a graph whose extrema are $-1.5\ \mathrm{m}$ and $+1.5\ \mathrm{m}$. The student's calculated $K_{\max}$ is four times the correct value. Which mistake most directly produces that result?
options:
- id: a
  content: |-
    Using $3.0\ \mathrm{m}$ instead of $1.5\ \mathrm{m}$ for the amplitude
  correct: true
- id: b
  content: |-
    Using the time between consecutive crests for the period
- id: c
  content: |-
    Converting the mass from kilograms to grams before substituting
- id: d
  content: |-
    Using the equilibrium position $x=0$ when locating maximum speed
- id: e
  content: |-
    Keeping the factor $\dfrac12$ in the kinetic-energy formula
```

---

<a id="solve-the-given-graph"></a>
## Solve the Given Graph

**Example:** A position–time graph has extrema at $\pm 0.60\ \mathrm{m}$ and consecutive crests $3.0\ \mathrm{s}$ apart. If the block has mass $1.2\ \mathrm{kg}$, find $K_{\max}$.

**Explanation**

Read $A=0.60\ \mathrm{m}$ and $T=3.0\ \mathrm{s}$, then chain the same three quantities:

$$
\begin{aligned}
\omega&=\frac{2\pi}{3.0\ \mathrm{s}}=\frac{2\pi}{3}\ \mathrm{rad/s},\\
v_{\max}&=\omega A
=\left(\frac{2\pi}{3}\right)(0.60)
=0.40\pi\ \mathrm{m/s},\\
K_{\max}&=\frac12(1.2)(0.40\pi)^2
=0.096\pi^2\ \mathrm{J}.
\end{aligned}
$$

```quiz
type: radio
id: p4-given-problem
shuffle: true
content: |-
  The plot below shows the $x$-component of the position of a block undergoing simple harmonic motion.

  Suppose the block has mass $2\ \mathrm{kg}$. What is its maximum kinetic energy?

  ![](<../Source/2026-07-23-HW-6/Images/simple-harmonic-motion-position-time-graph.png>)
options:
- id: a
  content: |-
    $\dfrac{3\pi^2}{25}\ \mathrm{J}$
- id: b
  content: |-
    $\dfrac{4\pi^2}{25}\ \mathrm{J}$
- id: c
  content: |-
    $\dfrac{9\pi^2}{25}\ \mathrm{J}$
  correct: true
- id: d
  content: |-
    $\dfrac{18\pi^2}{25}\ \mathrm{J}$
```

For the assignment graph, $A=1.5\ \mathrm{m}$ and $T=5.0\ \mathrm{s}$. Thus

$$
\begin{aligned}
K_{\max}
&=\frac12m\left(\frac{2\pi A}{T}\right)^2\\
&=\frac12(2)\left(\frac{2\pi(1.5)}{5}\right)^2\\
&=\left(\frac{3\pi}{5}\right)^2\\
&=\boxed{\frac{9\pi^2}{25}\ \mathrm{J}}.
\end{aligned}
$$

The units follow the formula:

$$
[K_{\max}]
=(\mathrm{kg})\left(\frac{\mathrm{m}}{\mathrm{s}}\right)^2
=\frac{\mathrm{kg}\cdot\mathrm{m}^2}{\mathrm{s}^2}
=\mathrm{J}.
$$

---

<a id="summary"></a>
## Summary

For an SHM position–time graph and a known mass:

1. Read $A$ from equilibrium to an extreme, not from minimum to maximum.
2. Read $T$ between matching points one full cycle apart.
3. Compute $\omega=2\pi/T$.
4. Use

   $$
   K_{\max}=\frac12m(\omega A)^2
   =\frac12m\left(\frac{2\pi A}{T}\right)^2.
   $$

Maximum kinetic energy occurs at equilibrium. The most common traps are using the peak-to-peak distance as $A$, using $1/T$ in place of $2\pi/T$, or failing to square all of $\omega A$.
