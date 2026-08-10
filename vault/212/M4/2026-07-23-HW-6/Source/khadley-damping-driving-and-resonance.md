
---
title: "Damping, Driving, and Resonance"
source: "http://khadley.com/Courses/Physics/ph_212/topics/oscillations/damping-and-driving.html"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Damped Oscillations

[![[Images/damp.gif]]](http://www.acs.psu.edu/drussell/Demos/SHO/damp.html)

Animation courtesy of Dr. Dan Russell, Grad. Prog. Acoustics, Penn State

Damping can occur in oscillating systems due to air resistance, internal friction, etc. The sources of damping are typically lumped together under the name "damping forces" and mathematically included as a linear term in the force equation. For example, the drag force -bv is included in the equation of motion of a mass on a spring:

![[Images/oscileqn11.jpg]]

We can write this as a differential equation, and confirm the solution:

![[Images/oscileqn12.jpg]] ![[Images/14-24-figure.jpg]] ![[Images/oscileqn14.jpg]] ![[Images/u878-12.png|The graph above shows the behavior of a lightly damped oscillator, or one that oscillates many times before it stops. This condition can be stated mathematically as b/2m << w0. This means that the frequency is approximately the natural frequency, or w = w0. ]] ![[Images/decayampfn.jpg]]

We can write the damped amplitude as a function of time for a lightly damped oscillator. A here is the initial amplitude.

## Practice Problem

```quiz
type: blank
id: khadley-damping-q1
input_mode: math
require_exact: true
content: |-
  **Question 1**

  A lightly damped oscillator loses $3.0\%$ of its amplitude during each cycle. If its initial amplitude is $0.25\ \mathrm m$, what is the amplitude after $30$ cycles? Enter meters: ==0.10==
feedback: |-
  Each cycle retains a factor of $0.970$, so $A_{30}=(0.25)(0.970)^{30}=0.1003\ldots\ \mathrm m$. Rounded to the two significant figures supported by the givens, the amplitude is $0.10\ \mathrm m$. The mass and period are unnecessary when the loss is specified per cycle.
```

## Driven Oscillators and Resonance

![[Images/childswinging.jpg]]

When some mechanism provides an external periodic force to an oscillator, the oscillator is said to be driven. For example, if you push a child on a swing periodically, timing the pushes to help the child swing higher, you are driving the oscillation.

If you stop driving the oscillation and just let the child keep swinging, she will swing at the natural frequency f0 for the system. The frequency at which you push the child is called the driving frequency fext. The driving frequency is independent of the natural frequency.

When you do push the child at the same frequency as the natural frequency, she goes higher and higher. This is an example of resonance. the condition of resonance is when the driving frequency equals the natural frequency.

fext = f0 resonance condition

Because of this relationship between the driving frequency and the natural frequency, the natural frequency is often called the resonance frequency.

![[starlogo_jk-icon_nd 2.svg]] ![[osu-tag 13.svg]]
