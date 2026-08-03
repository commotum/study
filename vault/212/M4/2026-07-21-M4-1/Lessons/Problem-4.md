# Finding Frequency From a Position–Time Graph

<!--
lesson-id: 212-M4-004
topic-code: MTH212.M4.04
-->

## Table of Contents

- [Introduction](#introduction)
- [Measure One Complete Cycle](#measure-one-complete-cycle)
- [Convert Period to Frequency](#convert-period-to-frequency)
- [Avoid Half-Cycle and Axis Traps](#avoid-half-cycle-and-axis-traps)
- [Apply the Method to the Given Oscillator](#apply-the-method-to-the-given-oscillator)
- [Summary](#summary)

## Prerequisites

- Read time coordinates from a graph's horizontal axis.
- Subtract two time values.
- Take the reciprocal of a positive number.

---

<a id="introduction"></a>
## Introduction

The **period** \(T\) is the smallest positive time shift that makes the graph repeat—the time for one complete cycle. The **frequency** \(f\) is the number of cycles per second:

$$
f=\frac{1}{T}.
$$

When a position-time graph is given, first measure the horizontal spacing between two consecutive points in the same phase—for example, crest to crest or trough to trough. That spacing is \(T\). Then take its reciprocal.

**Recognition cue:** A graph with time on the horizontal axis and a request for hertz requires a horizontal cycle measurement followed by \(f=1/T\).

| Requested quantity | What to read or calculate | Unit |
|---|---|---|
| Amplitude \(A\) | Vertical distance from equilibrium to an extreme | Position unit |
| Period \(T\) | Horizontal spacing between matching-phase points | Seconds |
| Frequency \(f\) | Reciprocal of the period | Hertz |

---

<a id="measure-one-complete-cycle"></a>
## Measure One Complete Cycle

**Example:** Consecutive crests of a position-time graph occur at \(t=1.0\ \mathrm{s}\) and \(t=6.0\ \mathrm{s}\). What is the period?

**Explanation**

The two crests are matching points one full cycle apart:

$$
T=t_2-t_1
=6.0\ \mathrm{s}-1.0\ \mathrm{s}
=5.0\ \mathrm{s}.
$$

Any matching pair works: crest to next crest, trough to next trough, or an equilibrium crossing to the next crossing in the same direction.

If two marked points span \(N\) complete cycles, divide the elapsed time by \(N\):

$$
T=\frac{\Delta t}{N}.
$$

```quiz
type: radio
id: problem-4-period-q1
content: |-
  Consecutive troughs on a position-time graph occur at \(t=2.5\ \mathrm{s}\) and \(t=8.5\ \mathrm{s}\). What is the period?
options:
- id: a
  content: |-
    \(6.0\ \mathrm{s}\)
  correct: true
  feedback: |-
    The troughs are one complete cycle apart, so \(T=8.5-2.5=6.0\ \mathrm{s}\).
- id: b
  content: |-
    \(11.0\ \mathrm{s}\)
  feedback: |-
    Period is the difference between the two times, not their sum.
- id: c
  content: |-
    \(3.0\ \mathrm{s}\)
  feedback: |-
    This halves a time interval that already spans exactly one cycle.
- id: d
  content: |-
    \(8.5\ \mathrm{s}\)
  feedback: |-
    This is the time coordinate of the second trough, not the elapsed time between troughs.
```

---

<a id="convert-period-to-frequency"></a>
## Convert Period to Frequency

**Example:** An oscillator has period \(T=5.0\ \mathrm{s}\). Find its frequency.

**Explanation**

Take the reciprocal of the period:

$$
f=\frac{1}{T}
=\frac{1}{5.0\ \mathrm{s}}
=0.20\ \mathrm{s^{-1}}
=0.20\ \mathrm{Hz}.
$$

A period measured in seconds produces a frequency in inverse seconds, and \(1\ \mathrm{s^{-1}}=1\ \mathrm{Hz}\).

Equivalently,

$$
f=\frac{\text{number of cycles}}{\text{elapsed time}}.
$$

For one cycle in \(5.0\ \mathrm{s}\), this is \(1\text{ cycle}/5.0\ \mathrm{s}=0.20\ \mathrm{Hz}\).

```quiz
type: radio
id: problem-4-frequency-q1
content: |-
  A position-time graph repeats every \(2.5\ \mathrm{s}\). What is the oscillator's frequency?
options:
- id: a
  content: |-
    \(0.40\ \mathrm{Hz}\)
  correct: true
  feedback: |-
    \(f=1/T=1/(2.5\ \mathrm{s})=0.40\ \mathrm{Hz}\).
- id: b
  content: |-
    \(2.5\ \mathrm{Hz}\)
  feedback: |-
    This copies the period's numerical value instead of taking its reciprocal.
- id: c
  content: |-
    \(5.0\ \mathrm{Hz}\)
  feedback: |-
    Frequency is not twice the period; it is \(1/T\).
- id: d
  content: |-
    \(0.20\ \mathrm{Hz}\)
  feedback: |-
    This is the reciprocal of \(5.0\ \mathrm{s}\), not \(2.5\ \mathrm{s}\).
```

---

<a id="avoid-half-cycle-and-axis-traps"></a>
## Avoid Half-Cycle and Axis Traps

**Example:** A graph has a crest at \(t=1.0\ \mathrm{s}\) and the next trough at \(t=3.0\ \mathrm{s}\). What are the period and frequency?

**Explanation**

Crest to trough is only half a cycle:

$$
\frac{T}{2}=3.0-1.0=2.0\ \mathrm{s}.
$$

Therefore,

$$
T=4.0\ \mathrm{s}
\qquad\text{and}\qquad
f=\frac{1}{4.0\ \mathrm{s}}
=0.25\ \mathrm{Hz}.
$$

Also avoid using vertical distances. Amplitude comes from the position axis, while period and frequency come from horizontal time spacing.

```quiz
type: radio
id: problem-4-half-cycle-q1
content: |-
  A position-time graph has a crest at \(t=0\) and the next trough at \(t=1.5\ \mathrm{s}\). What is the frequency?
options:
- id: a
  content: |-
    \(0.33\ \mathrm{Hz}\)
  correct: true
  feedback: |-
    Crest to trough is \(T/2=1.5\ \mathrm{s}\), so \(T=3.0\ \mathrm{s}\) and \(f=1/3.0=0.33\ \mathrm{Hz}\).
- id: b
  content: |-
    \(0.67\ \mathrm{Hz}\)
  feedback: |-
    This treats the crest-to-trough interval as a full period even though it is only half a cycle.
- id: c
  content: |-
    \(1.5\ \mathrm{Hz}\)
  feedback: |-
    This copies the half-cycle time as though it were a frequency.
- id: d
  content: |-
    \(3.0\ \mathrm{Hz}\)
  feedback: |-
    \(3.0\) is the period in seconds; frequency is its reciprocal.
```

---

<a id="apply-the-method-to-the-given-oscillator"></a>
## Apply the Method to the Given Oscillator

**Example:** Read one complete cycle from the position-time graph, then convert it to frequency.

![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

**Explanation**

Consecutive crests occur at

$$
t=0,\quad 4.0\ \mathrm{s},\quad 8.0\ \mathrm{s}.
$$

Using either adjacent pair gives

$$
T=4.0\ \mathrm{s}.
$$

As a consistency check, the interval from \(0\) to \(8.0\ \mathrm{s}\) contains two complete cycles:

$$
T=\frac{8.0\ \mathrm{s}-0}{2}=4.0\ \mathrm{s}.
$$

Now take the reciprocal:

$$
f=\frac{1}{T}
=\frac{1}{4.0\ \mathrm{s}}
=0.25\ \mathrm{Hz}.
$$

The period has two significant figures, so the frequency is reported as \(0.25\ \mathrm{Hz}\).

```quiz
type: radio
id: m4-1lec-q3
content: |-
  **Question 3**

  The graph shows the position of a simple harmonic oscillator. What is the frequency $f$ of the oscillation?

  ![](<../Source/Images/simple-harmonic-motion-position-time-graph.png>)

  Enter the frequency in hertz as a number only:
options:
- id: a
  content: 0.25
  correct: true
  feedback: |-
    From the graph, $T=4.0\ \mathrm{s}$. Thus,

    $$
    f=\frac{1}{T}=\frac{1}{4.0\ \mathrm{s}}=0.25\ \mathrm{Hz}.
    $$

    The period supports two significant figures.
- id: b
  content: 4.0
  feedback: |-
    This is the period in seconds, not the frequency in hertz.
- id: c
  content: 1.6
  feedback: |-
    This is the angular frequency in radians per second, not the ordinary frequency \(f\).
- id: d
  content: 0.50
  feedback: |-
    This treats the crest-to-trough spacing of \(2.0\ \mathrm{s}\) as a full period.
- id: e
  content: 2.5
  feedback: |-
    This is the graph's amplitude in centimeters, read from the vertical axis.
```

---

<a id="summary"></a>
## Summary

To find frequency from a position-time graph:

1. Choose two matching-phase points and count the complete cycles \(N\) between them.
2. Compute \(T=\Delta t/N\).
3. Compute \(f=1/T\).
4. Report the result in hertz.

**Main trap:** crest to trough or opposite-direction equilibrium crossing to crossing spans only \(T/2\). Vertical graph values describe position or amplitude, not frequency.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
