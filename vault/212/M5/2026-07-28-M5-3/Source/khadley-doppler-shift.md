
---
title: "Doppler Shift"
source: "http://khadley.com/Courses/Physics/ph_212/topics/waves/doppler.html"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Doppler Shift

![[Images/doppler.jpg]]

The Doppler shift is an effective change in frequency or wavelength detected when the observer or source, or both, are in motion relative to each other.

![[Images/dopplerinteractive.jpg]]

[Courtesy of Astronomy Interactives: highered.mheducation.com/sites/0072482621/student\_view0/interactives.html](http://highered.mheducation.com/olcweb/cgi/pluginpop.cgi?it=swf::800::600::/sites/dl/free/0072482621/78778/Doppler_Nav.swf::Doppler%20Shift%20Interactive)

The Doppler shift arises when there is relative motion between a wave source and an observer. If the distance between the two is decreasing, the observed frequency of the wave is higher than the frequency that would be heard if the source and observer were at rest with respect to each other. If the distance between the two is increasing, the observed frequency is lower.

[Example 1](https://www.youtube.com/watch?v=-qXa9oqKL6E) [Example 2](https://www.youtube.com/watch?v=a3RfULw7aAY) [Example 3](https://exoplanets.nasa.gov/interactable/11/index.html)

## Moving Observer, Stationary Source

![[Images/u1515-22.png|First consider the case where both the observer and the source are not moving with respect to each other. During a time increment t, the wavefronts move a distance vt where v is the wave speed. The number of wavelengths detected by the observer in that distance is: vt/l. The frequency is the number of wavelengths per time.]] ![[Images/doppler-0.jpg]]

We will call this frequency f0 since the source and observer are not moving with respect to each other.

Now consider the case where the observer is moving toward the source.

![[Images/doppler-1.jpg]]

Now the waves seem to be coming faster in the frame of the observer. The observed frequency is higher, denoted by the f+. The speed of the observer is denoted by vo.

![[Images/doppler-2.jpg]]

A little algebra allows us to write the Doppler shift equation in a simpler form, in terms of the rest frame frequency.

![[Images/dopplereqn2.jpg]]

We can derive the frequency detected by the observer when the observer is moving away from the source in an identical fashion. The formula above is a compact form we can use for both cases.

Note that f+ denotes a higher frequency, corresponding to the observer moving toward the source, while f- denotes a lower frequency, corresponding to the observer moving away from the source.

These formulas can be rewritten in terms of wavelength, using the relationship between velocity, wavelength and frequency.

## Moving Source, Stationary Observer

When the source of the sound is moving, it changes the wavelength of the sound. This subtle distinction means the formula for a moving source is fundamentally different from that of a moving observer.

Consider the case where the source is moving toward the observer.

![[Images/doppler-3.jpg]] ![[Images/u1629-23.png|A period T is the time between two successive wave crests emitted by the source. The first crest W1 moves a distance vT and the second crest W2 moves a distance vsT. Here lo is the wavelength seen by the observer and vs is the speed of the source.]] ![[Images/doppler-4.jpg]]

A little algebra allows us to rewrite our formula in terms of the rest frame frequency.

![[Images/dopplereqn1.jpg]]

An identical method allows us to derive the frequency from a moving source detected by a stationary observer, and we can combine the two equations into one equation as seen above.

Note that f+ denotes a higher frequency, corresponding to the source moving toward the observer, while f- denotes a lower frequency, corresponding to the source moving away from the observer.

![[Images/dopplereqns2.jpg]]

The Doppler shift formulas can be written in terms of the ratios of the frequencies.

![[Images/bat.jpg]]

[Image source](https://www.flickr.com/photos/51013318@N06/13407118045)

## Practice Problems

```quiz
type: blank
id: khadley-doppler-q1
input_mode: math
require_exact: true
content: |-
  **Question 1**

  A bat emits $25\ \mathrm{kHz}$ while flying directly away from a stationary listener. How fast must it fly for the listener to hear $20\ \mathrm{kHz}$? Use $v_{\mathrm{sound}}=343\ \mathrm{m/s}$ and enter meters per second: ==86==
feedback: |-
  For a receding source, $f'=f\,v/(v+v_s)$. Solving gives $v_s=v(f/f'-1)=343(25/20-1)=85.75\ \mathrm{m/s}$, which rounds to $86\ \mathrm{m/s}$.
```

![[Images/adamlambert.jpg]]

```quiz
type: blank
id: khadley-doppler-q2
input_mode: math
require_exact: true
content: |-
  **Question 2**

  A stationary singer produces $880\ \mathrm{Hz}$. A bat flies toward the singer at $35\ \mathrm{m/s}$. What frequency does the bat hear? Use $v_{\mathrm{sound}}=343\ \mathrm{m/s}$ and enter hertz: ==970==
feedback: |-
  For an observer moving toward a stationary source, $f'=f(v+v_o)/v=880(343+35)/343=969.8\ldots\ \mathrm{Hz}$, which rounds to $970\ \mathrm{Hz}$.
```

![[Images/waveeqn8.jpg]]

```quiz
type: free
id: khadley-doppler-q3
content: |-
  **Question 3**

  A galaxy's hydrogen-alpha line is observed at $654.0\ \mathrm{nm}$, compared with $656.3\ \mathrm{nm}$ in the laboratory. Is the galaxy approaching or receding, and what is its radial velocity? Use the nonrelativistic Doppler approximation.
correct: |-
  The shorter observed wavelength is a blueshift, so the galaxy is approaching. Using $v/c\approx(\lambda_{\mathrm{obs}}-\lambda_0)/\lambda_0$ gives
  $$v\approx-1.1\times10^6\ \mathrm{m/s},$$
  where the negative sign denotes motion toward Earth.
feedback: |-
  First determine direction from the wavelength shift, then compute the fractional shift before multiplying by $c$. Preserve the sign convention through the calculation.
```

![[starlogo_jk-icon_fix 7.png|J&K logo]] [![[osu-tag 7.svg]]](http://ecampus.oregonstate.edu/soc/ecatalog/ecourselist.htm?termcode=all&subject=PH)
