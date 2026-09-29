
---
title: "Gravity"
source: "http://khadley.com/Courses/Physics/ph_212/topics/gravity/"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
## [PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

[![[Images/black-holes-merging.jpg]]](https://www.ligo.caltech.edu/detection)

## Gravity

## Newtonian gravity

![[Images/gforce.jpg]]

The gravitational force causes massive particles to accelerate toward each other, it is proportional to the product of the masses of the particles. Unlike the electromagnetic force, which has two kinds of charge and can be attractive or repulsive, the gravitational force is only attractive, since there is only one kind of mass.

The gravitational forces felt by two particles forms a Newton's third law reaction pair. The force from mass 1 on mass 2 is equal in magnitude and opposite in direction of the force from mass 2 on mass 1. The distance between the point particles is designated as r.

Please see this [PH 211 course page](http://khadley.com/Courses/Physics/ph_211/211_topics/force/weight.html) for a discussion of mass and weight.

![[Images/inversesquare.jpg]] ![[Images/13-05-figure.jpg]] ![[Images/gravityeqn1.jpg]]

The gravitational force is an inverse square function. As you double the distance between the massive particles, the force between them decreases by a factor of one fourth.

![[Images/twoelectrons.jpg]] ![[Images/gravityeqn5.jpg]]

The gravitational force is very weak compared to the electromagnetic force.

![[Images/gravityeqn2.jpg]]

Recall that in general, force is the negative gradient of the scalar potential. Therefore, taking the integral of gravitational force, we can define the gravitational potential as an inverse function of the distance between two massive particles. The r-hat vector is a unit vector in the r-direction. Gravitational potential is defined as going to zero at infinity.

![[Images/image-2.jpg]]

[Video source](https://www.youtube.com/watch?v=3wAjpMP5eyo)

Newtonian mechanics works very well for low-gravity regions, like when you are not near a black hole or neutron star. We understand the gravitational force very well - well enough to trust our calculations regarding trajectories of massive objects in gravity fields. (No, stunt on the video did not really place as it is shown...)

![[Images/newtoncannon.jpg]]

[Newton's cannon simulator](https://physics.weber.edu/schroeder/software/NewtonsCannon.html)

Maintaining a stable circular orbit is really just a matter of being in freefall. If an object is moving at a certain velocity and at the right height, the surface of the Earth "falls away" to match the falling of the object.

## Kepler's Laws

Tycho Brahe (1546 - 1601) spent many years taking accurate measurements of the positions of the planets. Johannes Kepler (1571 - 1630) was Tycho's student, who compiled the data after Tycho's death. Kepler's analysis of the data gave rise to Kepler's laws, which Newton later used to formulate his law of gravity.

Kepler's laws can be stated as follows:

1. Planet orbits are ellipses with the sun at one focus of the ellipse.
2. A line joining a planet to the sun sweeps out equal areas in the ellipse over equal times.
3. The square of the orbital period of a planet is proportional to the cube of its semimajor axis.

![[Images/ellipse.jpg]]

@ 2014 Pearson Education, Inc.

An ellipse typically has two focal points. The farther apart the focal points, the greater the ellipticity of the ellipse. The "diameter" across the long side is called the major axis. The semi-major axis (a) is one-half the major axis. This diagram is greatly exaggerated, most planet orbits in our solar system are nearly circular. A circle is a special case of an ellipse, with only one focal point.

[![[Images/keplersecond-2.jpg]]](https://ophysics.com/f6.html)

[Kepler's second law interactive](https://ophysics.com/f6.html)

A planet moves faster when it is closer to the sun and slower when it is farther away. In the interactive simulation above from Weber State University above, the same amount of time elapsed while tracing out the black areas as the white areas.

![[Images/gravityeqn3.jpg]]

Kepler's third law gives the relationship between a planet's period and its distance from the star. If a planet's orbit is nearly spherical, the distance between the star and planet can be assumed to be a constant radius r.

![[Images/u47528-26.png|Johannes Kepler: Determined paths of planets using detailed observation Used Earth’s distance from the sun to scale relative distances to other planets Found orbital speeds by comparing planetary motions over time Summarized planets’ motions into three laws: Planet orbits are ellipses with the sun at one focus A line joining a planet to the sun sweeps out equal areas in equal times T2 a r3]] ![[Images/satellite.jpg]]

[Image source](http://www.telecanspace.com/)

![[Images/gravityeqn4.jpg]]

## Practice Problems

```quiz
type: free
id: khadley-gravity-q1
content: |-
  **Question 1**

  Use Newtonian gravity and circular motion to write Kepler's third law, $T^2\propto r^3$, as an equation for a small satellite orbiting mass $M$.
correct: |-
  Equating gravitational and radial forces and using $v=2\pi r/T$ gives
  $$T^2=\frac{4\pi^2}{GM}r^3.$$
feedback: |-
  Start with gravity as the centripetal force, then replace orbital speed with circumference divided by period.
```

```quiz
type: free
id: khadley-gravity-q2
content: |-
  **Question 2**

  Find the gravitational acceleration $g_h$ at altitude $h$ above Earth. Evaluate $g_h/g$ when $h=R_E/2$.
correct: |-
  $$g_h=\frac{GM_E}{(R_E+h)^2},\qquad \frac{g_h}{g}=\left(\frac{R_E}{R_E+h}\right)^2.$$
  At $h=R_E/2$, $g_h/g=4/9$.
feedback: |-
  Altitude is measured from the surface, but the inverse-square law uses distance from Earth's center.
```

```quiz
type: blank
id: khadley-gravity-q3
input_mode: math
require_exact: true
content: |-
  **Question 3**

  A planet takes eight Earth years to orbit the Sun. How far is it from the Sun if Earth is $1.50\times10^{11}\ \mathrm m$ away? Enter meters: ==6.0e11==
feedback: |-
  Kepler's third law gives $r/r_E=8^{2/3}=4$, so $r=4(1.50\times10^{11})=6.0\times10^{11}\ \mathrm m$.
```

```quiz
type: free
id: khadley-gravity-q4
content: |-
  **Question 4**

  Three equal masses $m$ occupy the corners of an equilateral triangle of side $L$ and orbit their common center. Find the net force on each, orbital speed, period, and total gravitational potential energy.

  ![[Images/threemasses.jpg]]
correct: |-
  $$F_{\mathrm{net}}=\sqrt3\frac{Gm^2}{L^2},\qquad v=\sqrt{\frac{Gm}{L}},$$
  $$T=2\pi\sqrt{\frac{L^3}{3Gm}},\qquad U=-\frac{3Gm^2}{L}.$$
feedback: |-
  Add the two force vectors before applying circular motion. For potential energy, count each distinct mass pair once.
```

```quiz
type: free
id: khadley-gravity-q5
content: |-
  **Question 5**

  Two planets of mass $m$ remain on opposite sides of a star of mass $M$, each at orbital radius $r$. Find their period and the system's total gravitational potential energy.

  ![[Images/binaryplanets.jpg]]
correct: |-
  $$T=2\pi\sqrt{\frac{r^3}{G(M+m/4)}},\qquad U=-\frac{2GMm}{r}-\frac{Gm^2}{2r}.$$
feedback: |-
  The planets are separated by $2r$. Include both star–planet interactions and count the planet–planet interaction only once.
```
