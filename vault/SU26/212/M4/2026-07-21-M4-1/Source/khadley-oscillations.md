
---
title: "Oscillations"
source: "http://khadley.com/Courses/Physics/ph_212/topics/oscillations/"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

Oscillations

[![[Images/pendulum-a.jpg]]](https://pixabay.com/photos/pendulum-map-compass-yellow-guide-1934311/)

- Simple harmonic motion
- Oscillator vs. wave
- Simple harmonic oscillators
- Energy
- Damping
- Driven oscillations
- Resonance

## Simple Harmonic Motion

![[Images/sinewave.jpg]] ![[Images/oscileqn1.jpg]] ![[Images/oscileqn2.jpg]] ![[Images/pasted-20image-20195x71.jpg]] ![[Images/oscildata.jpg]]

An undamped mass oscillating on a spring produces a sine wave. Note that a maximum or minimum value of position corresponds with a zero in velocity. Acceleration is not constant, but varies out of phase with position vs. time.

## Practice Problems

A block of mass m is on a frictionless surface as shown, attached to an ideal spring. The spring is initially unstretched at length x0. The block is pulled to the right to the position xf as shown and released. The block then makes 12 oscillations in 7.0 seconds.

Consider the case where m = 0.18 kg, x0 = 0.35 m and xf = 0.48 m.

![[Images/spring-block-displacement-setup.png]]

```quiz
type: blank
id: khadley-oscillations-q1
input_mode: math
require_exact: true
content: |-
  **Question 1**

  What is the block's position at $t=3.5\ \mathrm s$? Enter meters: ==0.48==
feedback: |-
  The block completes $12$ oscillations in $7.0\ \mathrm s$, so $3.5\ \mathrm s$ is exactly six periods. It returns to its release position, $x=0.48\ \mathrm m$.
```

```quiz
type: blank
id: khadley-oscillations-q2
input_mode: math
require_exact: true
content: |-
  **Question 2**

  What is the block's velocity at $t=3.5\ \mathrm s$? Enter meters per second: ==0==
feedback: |-
  After six complete periods the block is again at its turning point, where its velocity is $0\ \mathrm{m/s}$.
```

## Rotation and Simple Harmonic Oscillation

![[Images/sinewave.gif]]

[Image source](http://i.imgur.com/c9P9FPl.gif)

A rotating object can also be considered a simple harmonic oscillator. Its projection produces a sine wave.

![[Images/circle.jpg]] ![[Images/oscileqn3.jpg]]

The phase is the argument of the sine function. The phase constant provides initial conditions for the oscillation, when t = 0.

## Mass–Spring Simple Harmonic Oscillator

<iframe src="https://phet.colorado.edu/sims/html/masses-and-springs/latest/masses-and-springs_en.html" width="800" height="600" allowfullscreen=""></iframe>

[https://phet.colorado.edu/en/simulation/masses-and-springs](https://phet.colorado.edu/en/simulation/masses-and-springs)

## Practice Questions

```quiz
type: select
id: khadley-oscillations-q3
content: |-
  For an ideal horizontal mass–spring oscillator, determine how each change affects the frequency.
options:
- id: increases
  content: Increases
- id: decreases
  content: Decreases
- id: unchanged
  content: Remains unchanged
questions:
- id: khadley-oscillations-q3a
  content: Increase the mass while holding the spring constant fixed.
  correct_option: decreases
  feedback: |-
    Since $f=(1/2\pi)\sqrt{k/m}$, increasing inertia lowers the frequency.
- id: khadley-oscillations-q3b
  content: Increase the spring stiffness while holding the mass fixed.
  correct_option: increases
  feedback: |-
    Since $f=(1/2\pi)\sqrt{k/m}$, a larger restoring-force constant raises the frequency.
- id: khadley-oscillations-q3c
  content: Increase gravitational acceleration for the same horizontal oscillator.
  correct_option: unchanged
  feedback: |-
    Gravity changes the support force but does not appear in the horizontal oscillator frequency $f=(1/2\pi)\sqrt{k/m}$.
```
