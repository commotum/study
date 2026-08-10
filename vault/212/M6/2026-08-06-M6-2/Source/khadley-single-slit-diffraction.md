
---
title: "Single-Slit Diffraction"
source: "http://khadley.com/Courses/Physics/ph_212/topics/WaveOptics/single-slit.html"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
## [PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Single slit diffraction

![[Images/slide18.png]]

Light passing through a single slit also diffracts. According to Huygens' principle, every point along a wavefront can be treated as the source of a spherical wavelet.

![[Images/slide19.png]] ![[Images/slide20.png]]

The spherical wavelets interfere to produce a pattern that can be seen on a screen. Wavelets moving straight forward produce the central maximum.

![[Images/slide21.png]]

A similar treatment can be done for higher order pairs. For example, every wavelet can be paired with another wavelet a/4 away. This will provide additional points of destructive interference, for p = 1, 2, 3,...

Note that p = 0 is excluded, since it corresponds to the central maximum, not a point of destructive interference.

![[Images/slide23.png]] ![[Images/eqn9.jpg]]

The single slit mathematical derivations follow a similar method to that for double-slit diffraction. Here, instead of m (the index for double slit) we use "p" to distinguish the fact that we are using the index to measure the distance from the central maximum to the dark fringes.

![[Images/eqn10.jpg]]

The width of the central peak is just twice the distance from the central peak to the first dark fringe on either side.

Note that the width of the central bright fringe is inversely proportional to the width of the slit, a. The narrower the slit, the more the waves spread out.

## Sample Problems

```quiz
type: blank
id: khadley-single-slit-q1
input_mode: math
require_exact: true
content: |-
  **Question 1**

  A $633\ \mathrm{nm}$ laser illuminates a single slit of width $0.15\ \mathrm{mm}$. The graph shows the first minima $2.0\ \mathrm{cm}$ from the central maximum. Find the screen distance in meters: ==4.7==

  ![[Images/single-slit-intensity-position-graph.png]]
feedback: |-
  For the first minimum, $a\sin\theta=\lambda$ and $\tan\theta=y/L$. The small-angle form gives $L=ya/\lambda=4.74\ldots\ \mathrm m$, which rounds to $4.7\ \mathrm m$.
```

```quiz
type: blank
id: khadley-single-slit-q2
input_mode: math
require_exact: true
content: |-
  **Question 2**

  A single slit of width $0.15\ \mathrm{mm}$ is $5.3\ \mathrm m$ from a screen. The second secondary bright fringe is $6.2\ \mathrm{cm}$ from center. Using the midpoint approximation, find the wavelength in nanometers: ==700==
feedback: |-
  The second secondary maximum lies approximately halfway between minima $p=2$ and $p=3$, so $y\approx2.5\lambda L/a$. Thus $\lambda=ya/(2.5L)=7.0\times10^{-7}\ \mathrm m=7.0\times10^2\ \mathrm{nm}$.
```

## Double slits and single slits

![[Images/slide24.png]]

If double slits have width that is slightly smaller than the slit spacing, the fringes of the double slit are enveloped by a single slit pattern.

- The double slit sees the outer boundaries of the slit as a single slit
- The "single slit nature" of double slit diffraction is seen in the envelope of the double slit fringes
- The minima of the envelope are the same as the minima for a single slit with the same slit width as the overall width of the double slit

## Circular aperture diffraction

[![[Images/pinhole2.jpg|circular aperture diffraction image]]](http://www2.oberlin.edu/physics/catalog/demonstrations/optics/pinhole.html)

This image was produced by shining a laser through a pinhole. Light passing through the tiny hole diffracted around the edges, producing the superposition pattern shown here. The bright center is called an Airy disk, and the whole pattern with the concentric rings is called an Airy pattern, after George Biddell Airy. The Airy pattern is important in that it represents the smallest possible size to which light can be focused by a lens or mirror.
