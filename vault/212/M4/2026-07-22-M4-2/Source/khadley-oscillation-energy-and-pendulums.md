
---
title: "Oscillation Energy and Pendulums"
source: "http://khadley.com/Courses/Physics/ph_212/topics/oscillations/energy-and-pendula.html"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Simple Harmonic Oscillator Energy

![[Images/14-10-figure.jpg]]

Kinetic energy is denoted as the height between the potential energy and the total energy in an energy diagram. The turning points, where the potential energy equals the total energy, have zero kinetic energy. Where the system goes to zero potential energy, the mass moves at maximum velocity, since all of the energy is kinetic energy.

![[Images/oscileqn6.jpg]]

Using conservation of energy, and our previous definition of vmax, we can find an expression for the frequency of oscillation. Note that frequency does not depend on the amplitude and that energy goes as the square of the amplitude.

## Pendulums

<iframe src="https://phet.colorado.edu/sims/pendulum-lab/pendulum-lab_en.html" width="800" height="600" allowfullscreen=""></iframe>

[phet.colorado.edu/en/simulation/pendulum-lab](https://phet.colorado.edu/en/simulation/pendulum-lab)

- Restoring force
- Period

![[Images/pendulum.jpg]]

We can derive the period of a physical pendulum by examining the torque caused by the restoring force. Here, the torque is negative because it causes a clockwise motion for positive theta and a counterclockwise motion for negative theta.

This is the angular equivalent of the linear the SHO equation of motion:

![[Images/oscileqn8.jpg]]

Comparing these two equations, we find:

![[Images/oscileqn9a.jpg]] ![[Images/oscileqn10.jpg]] ![[Images/14-22-figure.jpg]]

For a physical pendulum, we use the general form for the period. Note that l is the distance from the pivot to the center of mass and m refers to the total mass.

![[Images/oscileqn9b.jpg]]

We use a change of variable from the simple harmonic oscillator equation to write the equation of motion for a pendulum in terms of the phase angle and maximum angle, instead of the displacement and maximum displacement.

![[Images/simplependulum.jpg]] ![[Images/oscileqn9c.jpg]]

For a simple pendulum, we can let the mass of the string go to zero and the moment of inertia takes a simple form. Substituting these values into our equation for a physical pendulum, the period for a simple pendulum reduces to the form shown above. The period of a simple pendulum only depends on the length of the string and the force due to gravity, in the limit of the small angle approximation.

## Practice Problem

```quiz
type: free
id: khadley-pendulums-q1
content: |-
  **Question 1**

  Find the small-angle period of a physical pendulum consisting of a uniform rod of mass $M$ and length $L$ with a point mass $m$ attached at its free end. The system pivots about the other end.

  ![[Images/pendulum2.jpg]]
correct: |-
  The total moment of inertia is $I=(M/3+m)L^2$, and the restoring-torque coefficient is $g(ML/2+mL)$. Therefore
  $$T=2\pi\sqrt{\frac{L(M/3+m)}{g(M/2+m)}}.$$
feedback: |-
  Add the component moments of inertia and their small-angle gravitational restoring torques about the pivot.
```

![[starlogo_jk-icon_nd 1.svg]] ![[osu-tag 11.svg]]
