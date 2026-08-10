
---
title: "Phase Difference"
source: "http://khadley.com/Courses/Physics/ph_212/topics/superposition/phase_difference.html"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
## [PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Phase difference

- The phase constant tells what the wave is doing at t = 0, x = 0
- The phase difference: difference between the phases of two waves

![[Images/slide13.png]]

These two waves are completely out of phase. Where one has a crest, the other has a trough, so they exhibit completely destructive interference.

![[Images/slide15.png]] ![[Images/u47833-21.png|The path-length difference is $\Delta x$.]] ![[Images/u47864-10.png|Completely constructive interference occurs for an even multiple of $\pi$.]] ![[Images/eqn2-1.jpg]] ![[Images/u53176-8.png|For identical in-phase sources, $\Delta x=m\lambda$.]] ![[Images/u53157-10.png|Completely destructive interference occurs for an odd multiple of $\pi$.]] ![[Images/phaseeqn-out.jpg]]

## Practice Questions

```quiz
type: checkbox
id: khadley-phase-q1
content: |-
  **Question 1**

  Two in-phase speakers emit waves with $\lambda=2.0\ \mathrm m$. Speaker 2 is $1.0\ \mathrm m$ in front of Speaker 1. Which changes make their forward waves completely constructive? Select all that apply.

  ![[Images/speakers.jpg]]
options:
- id: forward-1
  content: Move Speaker 1 forward $1.0\ \mathrm m$.
  correct: true
  feedback: |-
    This makes the path-length difference zero, an integer multiple of the wavelength, so the in-phase sources interfere constructively.
- id: forward-half
  content: Move Speaker 1 forward $0.5\ \mathrm m$.
  feedback: |-
    The remaining $0.5\ \mathrm m$ offset is one quarter wavelength, which is neither completely constructive nor completely destructive.
- id: backward-half
  content: Move Speaker 1 backward $0.5\ \mathrm m$.
  feedback: |-
    The new $1.5\ \mathrm m$ offset is three quarters wavelength, not an integer wavelength.
- id: backward-1
  content: Move Speaker 1 backward $1.0\ \mathrm m$.
  correct: true
  feedback: |-
    This makes the path-length difference $2.0\ \mathrm m=\lambda$, so the in-phase waves again arrive completely constructively.
- id: unchanged
  content: Do not move either speaker.
  feedback: |-
    The existing $1.0\ \mathrm m$ offset is half a wavelength, so the in-phase sources are completely out of phase in the forward direction.
```

```quiz
type: checkbox
id: khadley-phase-q2
shuffle: true
content: |-
  **Question 2**

  The blue circles represent crests from two in-phase sources. Which labeled points show complete constructive interference? Select all that apply.

  ![[Images/ex21-23-figure.jpg]]
options:
- id: p
  content: Point P
  correct: true
  feedback: |-
    At P, a crest from Source 1 intersects a crest from Source 2, so the waves arrive in phase.
- id: q
  content: Point Q
  correct: true
  feedback: |-
    At Q, crest lines from the two sources intersect, giving crest-on-crest constructive interference.
- id: r
  content: Point R
  feedback: |-
    Point R is not at an intersection of the two sources' crest lines, so the diagram does not show complete constructive interference there.
```

<iframe src="https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_en.html" width="800" height="600" allowfullscreen=""></iframe>

Use this interactive [PhET simulation](https://phet.colorado.edu/en/simulation/wave-interference) to explore superposition, and find locations of completely constructive interference and completely destructive interference for waves emanating from two sources.

## Practice Problems

```quiz
type: radio
id: khadley-phase-q3
shuffle: true
content: |-
  **Question 3**

  Two completely out-of-phase antennas at $x=\pm300\ \mathrm m$ emit $3.0\ \mathrm{MHz}$ waves. Classify the interference at $(300\ \mathrm m,800\ \mathrm m)$.

  ![[Images/antennas.jpg]]
options:
- id: constructive
  content: Completely constructive
  feedback: |-
    The path difference is $200\ \mathrm m=2\lambda$, which preserves the sources' initial half-cycle phase offset rather than canceling it.
- id: destructive
  content: Completely destructive
  correct: true
  feedback: |-
    The wavelength is $100\ \mathrm m$, and the two path lengths are $800\ \mathrm m$ and $1000\ \mathrm m$. Their $2\lambda$ difference adds a whole number of cycles, leaving the sources' initial out-of-phase condition destructive.
- id: neither
  content: Neither
  feedback: |-
    The path difference is exactly two wavelengths, so the relative phase is not partial; it remains the sources' exact half-cycle offset.
```

```quiz
type: blank
id: khadley-phase-q4
input_mode: math
require_exact: true
content: |-
  **Question 4**

  In-phase speakers emit $686\ \mathrm{Hz}$ sound with $\lambda=0.50\ \mathrm m$. Speaker A is at $(0,0)$ and Speaker B at $(0,-2.2\ \mathrm m)$. Find the first positive $x$-coordinate with maximum intensity. Enter meters: ==0.21==

  ![[Images/superplot.jpg]]
feedback: |-
  Along the positive axis, the path difference is $\sqrt{x^2+2.2^2}-x$. The first constructive value reached is $4\lambda=2.0\ \mathrm m$. Solving $\sqrt{x^2+2.2^2}-x=2.0$ gives $x=0.21\ \mathrm m$.
```

## Amplitude Function

![[Images/eqn5-1.jpg]]

The amplitude function is useful for the special case where the two sources have the same amplitude, and their displacement from each other is known, as well as their initial phase difference.

![[Images/21-32-figure.jpg]]

The black dots in the images above represent two sources of sound waves

- in phase (left)
- out of phase (right)

The colors indicate the amplitude of the superposed sound.

The pale green lines show where destructive interference occurs in space.

## Thin-film optical coatings

![[Images/17-23-figure.jpg]]

[![[Images/hard-1.gif]]](http://www.acs.psu.edu/drussell/Demos/reflect/hard.html)

[![[Images/soft-1.gif]]](http://www.acs.psu.edu/drussell/Demos/reflect/soft2.html)

[Animations courtesy of Dr. Dan Russell, Grad. Prog. Acoustics, Penn State](http://www.acs.psu.edu/drussell/Demos/reflect/reflect.html)

When light strikes a surface from a lower index of refraction to a higher index of refraction, the light wave undergoes a phase shift of pi radians.

When light comes from a higher index of refraction to a lower index of refraction, there is no phase shift.

You can think of this in terms of the wave on a string encountering a hard or soft boundary. Reflecting from the hard boundary causes a phase shift, where reflecting from the soft boundary does not.

In thin-film coatings, the phase-shifted, light reflected from the outer boundary interferes with the light reflected from the inner boundary.

If the interfering waves are in phase, they produce a "strong reflection" because they undergo constructive interference. However, the thickness of the film can be adjusted such that the waves undergo destructive interference, by ensuring that the waves are out of phase when they interfere. Thin-film coatings can be used to create anti-reflective coatings for optical lenses.
