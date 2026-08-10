
---
title: "Power, Intensity, and Decibels"
source: "http://khadley.com/Courses/Physics/ph_212/topics/waves/power.html"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Power, Intensity, and Decibels

[![[Images/wave-x-t.gif]]](http://www.acs.psu.edu/drussell/Demos/wave-x-t/wave-x-t.html)

[Animation courtesy of Dr. Dan Russell, Grad. Prog. Acoustics, Penn State](http://www.acs.psu.edu/drussell/Demos/wave-x-t/wave-x-t.html)

Consider a wave on a string. Any point along the string moves up and down as a wave passes through it. The average velocity of a point on the string is related to the amplitude of the wave and to how quickly the motion changes from up to down – thus the frequency.

![[Images/waveeqn9.jpg]]

The kinetic energy of the mass at that point depends on the square of the velocity. We can infer that the energy of the wave goes as the square of the amplitude, and the square of the frequency.

![[Images/waveeqn10.jpg]]

We define the intensity I of a wave to be the power delivered by the wave, divided by the area that the wave impinges upon. The units of intensity are Watts per square meter.

![[Images/waveeqn11.jpg]] ![[Images/inverse-square-law.jpg]]

[Image source](http://cheller.phy.georgiasouthern.edu/gears/Units/3-Galaxies/Galaxies_14_Mass_Brightness/Galaxies_14_Mass_Brightness2.html)

![[Images/u1233-8.png|For spherical waves, the area increases as the surface area of a sphere, 4pr2. ]] ![[Images/waveeqn12.jpg]] ![[Images/u1259-14.png|We measure sound intensity level b in decibels, as defined above. This is a logarithmic scale of a ratio of intensities, with I0 defined at the lowest threshold of human hearing. When the sound intensity level increases by 10 dB, the actual intensity increases by a factor of ten.]] ![[Images/waveeqn13.jpg]]

When I = I0, the sound intensity level is zero decibels. This doesn't mean that there are no sound waves present, just that humans cannot hear them.

We start to feel pain from high intensity sound level at about 130 dB.

## Practice Problems

```quiz
type: blank
id: khadley-intensity-q1
input_mode: math
require_exact: true
content: |-
  **Question 1**

  If a sound wave's amplitude doubles, what is $I_2/I_1$? ==4==
feedback: |-
  Wave intensity is proportional to amplitude squared, so $I_2/I_1=(A_2/A_1)^2=2^2=4$.
```

```quiz
type: blank
id: khadley-intensity-q2
input_mode: math
require_exact: true
content: |-
  **Question 2**

  A speaker produces $240\ \mathrm{W/m^2}$ at $12\ \mathrm m$. What intensity is measured at $24\ \mathrm m$? Enter $\mathrm{W/m^2}$: ==60==
feedback: |-
  Point-source intensity follows $I\propto1/r^2$. Doubling distance reduces intensity by four: $240/4=60\ \mathrm{W/m^2}$.
```

```quiz
type: blank
id: khadley-intensity-q3
input_mode: math
require_exact: true
content: |-
  **Question 3**

  What intensity corresponds to a sound level of $60\ \mathrm{dB}$? Use $I_0=10^{-12}\ \mathrm{W/m^2}$ and enter $\mathrm{W/m^2}$: ==1.0e-6==
feedback: |-
  From $\beta=10\log_{10}(I/I_0)$, $I=I_0\,10^{\beta/10}=10^{-12}10^6=1.0\times10^{-6}\ \mathrm{W/m^2}$.
```

```quiz
type: blank
id: khadley-intensity-q4
input_mode: math
require_exact: true
content: |-
  **Question 4**

  Two independent people each produce a $60\ \mathrm{dB}$ conversation level at the listener. What is the combined level in decibels? ==63==
feedback: |-
  Equal independent sources add intensities, not decibel values. Doubling intensity adds $10\log_{10}2=3.01\ \mathrm{dB}$, giving about $63\ \mathrm{dB}$.
```
