# Reading Amplitude From a Position–Time Graph

## Table of Contents

- [Introduction](#introduction)
- [Measure From Equilibrium to an Extreme](#measure-from-equilibrium-to-an-extreme)
- [Halve the Peak-to-Peak Distance](#halve-the-peak-to-peak-distance)
- [Handle a Shifted Equilibrium](#handle-a-shifted-equilibrium)
- [Apply the Rule to the Given Oscillator](#apply-the-rule-to-the-given-oscillator)
- [Summary](#summary)

## Prerequisites

- Read maximum and minimum values from a graph's vertical axis.
- Interpret distance as a nonnegative quantity.
- Distinguish the horizontal time axis from the vertical position axis.

---

<a id="introduction"></a>
## Introduction

The **amplitude** of an oscillator is its maximum distance from equilibrium. On a position-versus-time graph,

$$
A=\max_t\left|x(t)-x_{\mathrm{eq}}\right|.
$$

If the maximum and minimum positions are visible, the same quantity is

$$
A=\frac{x_{\max}-x_{\min}}{2},
\qquad
x_{\mathrm{eq}}=\frac{x_{\max}+x_{\min}}{2}.
$$

**Recognition cue:** Read amplitude vertically from the position axis. The times of the peaks tell when extrema occur, not how large the amplitude is.

| Read from the graph | Use it for |
|---|---|
| Lowest and highest positions | The vertical range $[x_{\min},x_{\max}]$ |
| Midpoint of that range | The equilibrium position $x_{\mathrm{eq}}$ |
| Half the range's width | The amplitude $A$ |

---

<a id="measure-from-equilibrium-to-an-extreme"></a>
## Measure From Equilibrium to an Extreme

**Example:** An oscillator's equilibrium is $x=0$, and its graph reaches $x=+3.0\ \mathrm{cm}$ and $x=-3.0\ \mathrm{cm}$. What is its amplitude?

**Explanation**

Amplitude is the distance from equilibrium to either extreme:

$$
A=|3.0-0|=|-3.0-0|=3.0\ \mathrm{cm}.
$$

The negative trough does not make the amplitude negative. Distance is nonnegative.

When equilibrium is zero, the shortcut is

$$
A=|x_{\max}|=|x_{\min}|.
$$

```quiz
type: radio
id: problem-2-equilibrium-q1
content: |-
  A position-time graph oscillates about $x=0$ and reaches a minimum position of $-4.0\ \mathrm{cm}$. What is the amplitude?
options:
- id: a
  content: |-
    $4.0\ \mathrm{cm}$
  correct: true
  feedback: |-
    The trough is $4.0\ \mathrm{cm}$ from equilibrium, so the amplitude is $|-4.0|=4.0\ \mathrm{cm}$.
- id: b
  content: |-
    $-4.0\ \mathrm{cm}$
  feedback: |-
    The position can be negative, but amplitude is a nonnegative distance.
- id: c
  content: |-
    $8.0\ \mathrm{cm}$
  feedback: |-
    This would be the full peak-to-peak distance if the graph also reached $+4.0\ \mathrm{cm}$.
- id: d
  content: |-
    $0\ \mathrm{cm}$
  feedback: |-
    Zero is the equilibrium position, not the maximum distance from it.
```

---

<a id="halve-the-peak-to-peak-distance"></a>
## Halve the Peak-to-Peak Distance

**Example:** A graph reaches $x_{\max}=+4.0\ \mathrm{cm}$ and $x_{\min}=-4.0\ \mathrm{cm}$. Find its peak-to-peak distance and amplitude.

**Explanation**

The full vertical span is

$$
x_{\max}-x_{\min}
=4.0-(-4.0)
=8.0\ \mathrm{cm}.
$$

That span contains two amplitudes, one above equilibrium and one below:

$$
A=\frac{8.0\ \mathrm{cm}}{2}=4.0\ \mathrm{cm}.
$$

**Watch Out!** A crest-to-trough measurement is $2A$, not $A$.

```quiz
type: radio
id: problem-2-peak-to-peak-q1
content: |-
  A position-time graph has $x_{\max}=+1.8\ \mathrm{cm}$ and $x_{\min}=-1.8\ \mathrm{cm}$. What is its amplitude?
options:
- id: a
  content: |-
    $1.8\ \mathrm{cm}$
  correct: true
  feedback: |-
    The peak-to-peak distance is $3.6\ \mathrm{cm}$, so the amplitude is half of it: $1.8\ \mathrm{cm}$.
- id: b
  content: |-
    $3.6\ \mathrm{cm}$
  feedback: |-
    This is the full peak-to-peak distance, equal to $2A$.
- id: c
  content: |-
    $-1.8\ \mathrm{cm}$
  feedback: |-
    Amplitude is a distance and cannot be negative.
- id: d
  content: |-
    $0.90\ \mathrm{cm}$
  feedback: |-
    The peak-to-peak distance must be halved once, not twice.
```

---

<a id="handle-a-shifted-equilibrium"></a>
## Handle a Shifted Equilibrium

**Example:** A sinusoidal position graph has $x_{\max}=5\ \mathrm{cm}$ and $x_{\min}=-1\ \mathrm{cm}$. Find its equilibrium position and amplitude.

**Explanation**

The equilibrium is the midpoint of the extrema:

$$
x_{\mathrm{eq}}
=\frac{5+(-1)}{2}
=2\ \mathrm{cm}.
$$

The amplitude is half their difference:

$$
A=\frac{5-(-1)}{2}=3\ \mathrm{cm}.
$$

Using $|x_{\max}|=5\ \mathrm{cm}$ would be wrong because the equilibrium is not at zero.

```quiz
type: radio
id: problem-2-shifted-q1
content: |-
  An oscillator's graph has a maximum of $7\ \mathrm{cm}$ and a minimum of $1\ \mathrm{cm}$. What is its amplitude?
options:
- id: a
  content: |-
    $3\ \mathrm{cm}$
  correct: true
  feedback: |-
    $A=(7-1)/2=3\ \mathrm{cm}$. The equilibrium is at $4\ \mathrm{cm}$.
- id: b
  content: |-
    $4\ \mathrm{cm}$
  feedback: |-
    This is the equilibrium position, the midpoint of the two extremes.
- id: c
  content: |-
    $6\ \mathrm{cm}$
  feedback: |-
    This is the peak-to-peak distance, equal to twice the amplitude.
- id: d
  content: |-
    $7\ \mathrm{cm}$
  feedback: |-
    The maximum graph value is not the amplitude when equilibrium is shifted away from zero.
```

---

<a id="apply-the-rule-to-the-given-oscillator"></a>
## Apply the Rule to the Given Oscillator

**Example:** Read the vertical extrema and equilibrium from the position-time graph below.

![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

**Explanation**

Use a three-pass read:

1. **Axis:** the vertical axis is position $x$ in centimeters.
2. **Extrema:** the highest and lowest positions are $+2.5\ \mathrm{cm}$ and $-2.5\ \mathrm{cm}$.
3. **Distance:** equilibrium is their midpoint, $x_{\mathrm{eq}}=0$, so either extreme is $2.5\ \mathrm{cm}$ away.

In symbols, the graph reaches

$$
x_{\max}=+2.5\ \mathrm{cm}
\qquad\text{and}\qquad
x_{\min}=-2.5\ \mathrm{cm}.
$$

Therefore,

$$
A=|2.5-0|
=\frac{2.5-(-2.5)}{2}
=2.5\ \mathrm{cm}.
$$

The $4.0\ \mathrm{s}$ spacing between crests is the period; it is not used to find amplitude.

```quiz
type: radio
id: m4-1lec-q1
content: |-
  **Question 1**

  The graph shows the position of a simple harmonic oscillator. What is the amplitude of the oscillation?

  ![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

  Enter the amplitude in centimeters as a number only:
options:
- id: a
  content: 2.5
  correct: true
  feedback: |-
    The amplitude is the maximum displacement from equilibrium. The graph reaches $x=\pm2.5\ \mathrm{cm}$, so $A=2.5\ \mathrm{cm}$.
- id: b
  content: 5.0
  feedback: |-
    This is the peak-to-peak distance from $-2.5$ to $+2.5$, which equals $2A$.
- id: c
  content: -2.5
  feedback: |-
    The trough position is negative, but amplitude is a nonnegative distance.
- id: d
  content: 4.0
  feedback: |-
    This is the period read from the horizontal time axis, not the amplitude.
- id: e
  content: 0
  feedback: |-
    Zero is the equilibrium position, not the greatest displacement from it.
```

---

<a id="summary"></a>
## Summary

To read amplitude from a position-time graph:

1. Read the maximum and minimum positions from the vertical axis.
2. Locate equilibrium at their midpoint.
3. Measure from equilibrium to either extreme, or calculate

   $$
   A=\frac{x_{\max}-x_{\min}}{2}.
   $$

4. Report a nonnegative value in the vertical axis's units.

**Main trap:** the full peak-to-peak distance is $2A$. Time coordinates describe timing quantities such as period, not amplitude; changing where a peak occurs horizontally does not change its vertical distance from equilibrium.
