# Reading an Oscillation Period From a Position-Time Graph

<!--
lesson-id: 212-M4-003
topic-code: MTH212.M4.03
-->

## Table of Contents

- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Measure One Complete Repeat](#measure-one-complete-repeat)
- [Match Both Position and Phase](#match-both-position-and-phase)
- [Use Several Cycles When Available](#use-several-cycles-when-available)
- [Apply the Method to Problem 3](#apply-the-method-to-problem-3)
- [Summary](#summary)

## Prerequisites

- Read coordinates from a position-time graph.
- Subtract two time coordinates.
- Recognize maxima, minima, and equilibrium crossings.

---

<a id="introduction"></a>
## Introduction

When a position-time graph repeats and the question asks for the oscillation period, the recognition cue is a pair of landmarks with the same position and the same direction of motion. Use one move: subtract their time coordinates to measure the elapsed time, then divide by the number of complete cycles between them,

$$
T=\frac{t_{\mathrm{later}}-t_{\mathrm{earlier}}}{N_{\mathrm{cycles}}}.
$$

---

<a id="measure-one-complete-repeat"></a>
## Measure One Complete Repeat

**Recognition cue:** A position-time graph repeats the same oscillation shape, and the question asks for the period.

The period $T$ is the smallest positive time interval after which the motion repeats. On a graph, choose two consecutive matching landmarks and subtract their times:

$$
T=t_{\mathrm{later}}-t_{\mathrm{earlier}}.
$$

Equivalently, imagine sliding the entire graph horizontally. The period is the smallest positive shift that makes the shifted curve line up with the original curve.

The cleanest matching pairs are usually consecutive maxima or consecutive minima.

**Example:** Consecutive maxima occur at $t=1.5\ \mathrm{s}$ and $t=6.5\ \mathrm{s}$. Then

$$
T=6.5\ \mathrm{s}-1.5\ \mathrm{s}=5.0\ \mathrm{s}.
$$

**Explanation**

Both points represent the same place in the cycle, and there is exactly one complete repeat between them.

```quiz
type: radio
id: p3-consecutive-landmarks
content: |-
  Consecutive troughs of an oscillator occur at $t=2.0\ \mathrm{s}$ and $t=7.0\ \mathrm{s}$. What is the period?
options:
- id: p3-consecutive-landmarks-a
  content: |-
    $5.0\ \mathrm{s}$
  correct: true
  feedback: |-
    Consecutive troughs are matching phase points, so subtract their time coordinates: $T=7.0-2.0=5.0\ \mathrm{s}$. Adding the times or halving their separation does not measure one complete repeat.
- id: p3-consecutive-landmarks-b
  content: |-
    $9.0\ \mathrm{s}$
- id: p3-consecutive-landmarks-c
  content: |-
    $2.5\ \mathrm{s}$
- id: p3-consecutive-landmarks-d
  content: |-
    $3.5\ \mathrm{s}$
```

---

<a id="match-both-position-and-phase"></a>
## Match Both Position and Phase

Two points belong to the same phase only when the oscillator has the same position **and** the same direction of motion.

These pairs span one full period:

- maximum to the next maximum;
- minimum to the next minimum;
- upward equilibrium crossing to the next upward equilibrium crossing;
- downward equilibrium crossing to the next downward equilibrium crossing.

A maximum to the next minimum spans only half a period:

$$
\Delta t_{\mathrm{max\ to\ min}}=\frac T2.
$$

For a sinusoidal position graph, one cycle follows this landmark sequence:

| Elapsed fraction of a period | Landmark |
| ---: | --- |
| $0$ | Maximum |
| $T/4$ | Downward equilibrium crossing |
| $T/2$ | Minimum |
| $3T/4$ | Upward equilibrium crossing |
| $T$ | Next maximum |

Likewise, an upward crossing and a downward crossing may have the same position, but they do not have the same phase.

**Example:** A maximum occurs at $t=1\ \mathrm{s}$ and the next minimum occurs at $t=3\ \mathrm{s}$. The $2\ \mathrm{s}$ gap is half a cycle, so

$$
T=2(2\ \mathrm{s})=4\ \mathrm{s}.
$$

**Explanation**

Equal vertical positions alone are not enough; the direction through that position must also match.

```quiz
type: radio
id: p3-phase-match
content: |-
  An oscillator crosses equilibrium moving upward at $t=0.5\ \mathrm{s}$ and again moving upward at $t=3.5\ \mathrm{s}$. What is its period?
options:
- id: p3-phase-match-a
  content: |-
    $3.0\ \mathrm{s}$
  correct: true
  feedback: |-
    The two crossings have the same position and the same direction, so they are one full cycle apart: $T=3.5-0.5=3.0\ \mathrm{s}$. The value $1.5\ \mathrm{s}$ incorrectly treats the interval as two cycles.
- id: p3-phase-match-b
  content: |-
    $1.5\ \mathrm{s}$
- id: p3-phase-match-c
  content: |-
    $4.0\ \mathrm{s}$
- id: p3-phase-match-d
  content: |-
    $0.33\ \mathrm{s}$
```

---

<a id="use-several-cycles-when-available"></a>
## Use Several Cycles When Available

If a graph shows several cycles, measure across a wider interval and divide by the number of complete cycles:

$$
T=\frac{t_{\mathrm{last}}-t_{\mathrm{first}}}{N_{\mathrm{cycles}}}.
$$

Count the **gaps** between matching landmarks, not just the number of landmarks.

**Example:** Maxima occur at $t=1\ \mathrm{s}$, $5\ \mathrm{s}$, $9\ \mathrm{s}$, and $13\ \mathrm{s}$. The first and last maxima are separated by three cycles, so

$$
T=\frac{13\ \mathrm{s}-1\ \mathrm{s}}{3}=4\ \mathrm{s}.
$$

**Explanation**

Measuring several cycles can reduce the effect of small graph-reading errors.

```quiz
type: radio
id: p3-multiple-cycles
content: |-
  Four consecutive maxima occur at $t=2\ \mathrm{s}$, $7\ \mathrm{s}$, $12\ \mathrm{s}$, and $17\ \mathrm{s}$. Use the first and last maxima to find the period.
options:
- id: p3-multiple-cycles-a
  content: |-
    $5\ \mathrm{s}$
  correct: true
  feedback: |-
    Four consecutive maxima create three cycle gaps. The total time is $17-2=15\ \mathrm{s}$, so $T=15/3=5\ \mathrm{s}$. Dividing by four counts landmarks instead of intervals.
- id: p3-multiple-cycles-b
  content: |-
    $15\ \mathrm{s}$
- id: p3-multiple-cycles-c
  content: |-
    $3.75\ \mathrm{s}$
- id: p3-multiple-cycles-d
  content: |-
    $7.5\ \mathrm{s}$
```

---

<a id="apply-the-method-to-problem-3"></a>
## Apply the Method to Problem 3

**Example:** The graph shows the position of a simple harmonic oscillator. What is the period of the oscillation?

![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

**Explanation**

Consecutive maxima occur at

$$
t=0,\quad 4.0\ \mathrm{s},\quad 8.0\ \mathrm{s}.
$$

These are horizontal-axis readings. The graph's vertical scale gives position and amplitude, not period. The visible maximum-to-minimum time is $2.0\ \mathrm{s}=T/2$, which confirms a full period of $4.0\ \mathrm{s}$.

Using either adjacent pair,

$$
T=4.0\ \mathrm{s}-0=4.0\ \mathrm{s}.
$$

The same result comes from the first and third maxima, which span two cycles:

$$
T=\frac{8.0\ \mathrm{s}-0}{2}=4.0\ \mathrm{s}.
$$

The requested answer form is: **Enter the period in seconds as a number only.** Enter **4.0**.

```quiz
type: radio
id: p3-source-check
content: |-
  **Question 2**

  The graph shows the position of a simple harmonic oscillator. What is the period of the oscillation?

  ![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

  Enter the period in seconds as a number only.
options:
- id: p3-source-check-a
  content: |-
    4.0
  correct: true
  feedback: |-
    Consecutive maxima occur at $t=0$, $4.0\ \mathrm{s}$, and $8.0\ \mathrm{s}$. Therefore, the period is $T=4.0\ \mathrm{s}$.

    The value `2.0` is the maximum-to-minimum half-period. The value `8.0` spans two cycles without dividing by two. The value `0.25` is the frequency $f=1/T$ in hertz, not the period in seconds.
- id: p3-source-check-b
  content: |-
    2.0
- id: p3-source-check-c
  content: |-
    8.0
- id: p3-source-check-d
  content: |-
    0.25
```

---

## Summary

1. Choose a clear phase landmark such as a maximum, minimum, or directed equilibrium crossing.
2. Find the next occurrence of the same landmark and direction.
3. Subtract the horizontal time coordinates to get one full period; ignore the vertical amplitude when finding $T$.
4. If measuring across several repeats, divide by the number of cycle gaps.
5. Do not confuse a maximum-to-minimum gap, which is $T/2$, with a full period.
6. Keep frequency separate: $f=1/T$ has units of hertz, while period has units of seconds.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
