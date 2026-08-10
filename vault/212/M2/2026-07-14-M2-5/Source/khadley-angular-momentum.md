
---
title: "Angular Momentum"
source: "http://khadley.com/Courses/Physics/ph_212/topics/rigidRotation/angular-momentum.html"
author:
published:
created: 2026-08-10
description: "Introduction to anguar momentum"
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Angular Momentum

![[Images/z9rgxam.gif]]

[Image source](http://i.imgur.com/Z9RGXam.gif)

![[Images/nettorqueeqn2-crop-u1686.png]]

In the absence of net external forces, linear momentum is conserved.

In the absence of net external torques, angular momentum is conserved.

![[Images/angmoeqn1.jpg]] ![[Images/angmoeqn2.jpg]]

Angular momentum can take two forms. For a rotating object, angular momentum is equal to the product of the moment of inertia and the angular velocity. For a point particle, the moment of inertial is the cross product of the particle's position and momentum.

![[Images/skater.jpg]] ![[Images/angmoeqn3.jpg]]

A skater spins up when she brings her arms in toward her rotation axis, reducing her moment of inertia. To conserve angular momentum, her angular speed must increase.

## Sample Problems

```quiz
type: radio
id: khadley-angular-momentum-q1
shuffle: true
content: |-
  **Question 1**

  Two buckets rotate on frictionless bearings. Rain falls vertically into them and is captured. What happens to their angular speed?

  ![[Images/buckets.jpg]]
options:
- id: increases
  content: It increases.
  feedback: |-
    Captured rain increases the system's moment of inertia. With negligible external torque, angular momentum stays constant, so angular speed cannot increase.
- id: decreases
  content: It decreases.
  correct: true
  feedback: |-
    The rain adds mass away from the axis and increases $I$. Conservation of angular momentum, $I_i\omega_i=I_f\omega_f$, therefore requires a smaller final angular speed.
- id: unchanged
  content: It remains unchanged.
  feedback: |-
    Zero external torque conserves angular momentum, not angular speed. Because the captured rain changes the moment of inertia, $\omega$ must change.
```

```quiz
type: free
id: khadley-angular-momentum-q2
content: |-
  **Question 2**

  Two equal point masses are connected by a massless rod. If their distance from the rotation axis doubles while angular momentum is conserved, find $\omega_f$ in terms of $\omega_i$.

  ![[Images/angmosystem.jpg]]
correct: |-
  Doubling every radius multiplies the moment of inertia by four. Therefore $I_i\omega_i=4I_i\omega_f$, so
  $$\omega_f=\frac{\omega_i}{4}.$$
feedback: |-
  For point masses, $I=\sum mr^2$. Apply the radius change to $I$ before using angular-momentum conservation.
```

```quiz
type: free
id: khadley-angular-momentum-q3
content: |-
  **Question 3**

  A ring of mass $m$ and radius $r$ is dropped onto a spinning uniform solid cylinder of mass $M$, radius $r$, and initial angular speed $\omega_0$. Find the shared final angular speed.

  ![[Images/angmosystem2.jpg]]
correct: |-
  Conserving angular momentum about the axis gives
  $$\frac12Mr^2\omega_0=\left(\frac12Mr^2+mr^2\right)\omega_f,$$
  hence
  $$\omega_f=\frac{M}{M+2m}\,\omega_0.$$
feedback: |-
  Mechanical energy is not conserved during the frictional coupling, but external torque about the axle is negligible, so angular momentum is conserved.
```

```quiz
type: free
id: khadley-angular-momentum-q4
content: |-
  **Question 4**

  A projectile of mass $m$ and speed $v$ sticks to the rim of an initially stationary uniform solid cylinder of mass $M$ and radius $r$. Find the final angular speed; assume no final translational motion.

  ![[Images/bulletdisk.jpg]]
correct: |-
  About the cylinder axis, the incoming angular momentum is $mvr$. The final moment of inertia is $Mr^2/2+mr^2$, so
  $$\omega_f=\frac{mv}{r(m+M/2)}.$$
feedback: |-
  Take angular momentum about the fixed axis so the collision's unknown impulsive support force contributes no torque about that point.
```

## Rotational Motion

### Four Approaches to Problem Solving

### Putting It All Together

There are four main approaches to solving problems for systems involving rotation:

1. Forces and torques
2. Conservation of energy
3. Conservation of angular momentum
4. Rotational kinematics

![[Images/nettorqueeqn1.jpg]]

Using a net force and net torque approach involves solving vector equations. Note that the torque equation is taken about a pivot point. These fundamental equations provide a system of equations to be solved simultaneously.

For cases of static equilibrium, the net torque and the net force each equal zero. For dynamic cases, you may need to include kinematic equations.

![[Images/econseqn.jpg]]

Conservation of energy includes rotational energy as well as translational energy. Non-conservative energy such as energy lost to friction is included in the final state.

![[Images/lconseqn.jpg]]

A conservation of angular momentum approach may be used for systems involving rotation. A system may include rotating objects with moment of inertia I and translating objects of momentum p, each having and initial and final angular momentum.

![[Images/kinematiceqns.jpg]]

Kinematic equations for constant linear and rotational acceleration are shown here. For more general equations, refer to the previous chapter.

Often, a problem can be solved in multiple ways, or with a combination of approaches. Taking advantage of symmetries in the system may make one approach easier than another. Also, be careful to recognize the external forces or torques in a problem when deciding which approach to take.

![[starlogo_jk-icon_fix 10.png]] [![[osu-tag 14.svg]]](http://ecampus.oregonstate.edu/soc/ecatalog/ecourselist.htm?termcode=all&subject=PH)
