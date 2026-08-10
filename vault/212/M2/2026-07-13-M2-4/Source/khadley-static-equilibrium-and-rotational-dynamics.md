
---
title: "Static Equilibrium and Rotational Dynamics"
source: "http://khadley.com/Courses/Physics/ph_212/topics/rigidRotation/static-equilibrium.html"
author:
published:
created: 2026-08-10
description: "Introduction to static equilibrium"
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Static Equilibrium

![[Images/balancing-act1.jpg]]

[Image source](http://www.matchpoint.nyc/4-quick-snacks-to-keep-you-productive-during-your-daily-balancing-act/)

A rigid object is in static equilibrium if the net torque is zero at every point on the object, and the net force on the object is zero.

Step 1: Draw an extended free-body diagram representing the forces and their locations on the object.

![[Images/staticequil.jpg]]

Step 2: Translate the diagram into its mathematical equivalent, beginning with writing the equation for net force.

![[Images/stateqn1.jpg]] ![[Images/u807-6.png|Step 3: Choose a pivot point and write the equation for net torque about that point. Torques that would produce counterclockwise rotation are positive, and torques that would produce clockwise rotation are negative. In this example, all of the forces are perpendicular to the beam, so the sin q factors are just 1.]] ![[Images/stateqn2.jpg]]

Step 4: Algebraically solve for the unknown quantity.

## Practice Problems

```quiz
type: free
id: khadley-equilibrium-q1
content: |-
  **Question 1**

  A uniform ladder of mass $m$ and length $L$ leans against a frictionless wall at angle $\theta$. Find the minimum coefficient of static friction between the ladder and the ground that prevents slipping.

  ![[Images/ladderdiagram.jpg]]
correct: |-
  Taking torques about the bottom gives $N_wL\sin\theta=mg(L/2)\cos\theta$, so $N_w=mg/(2\tan\theta)$. Horizontal and vertical force balance give $f_s=N_w$ and $N_g=mg$. Therefore,
  $$\mu_{s,\min}=\frac{f_s}{N_g}=\frac{1}{2\tan\theta}.$$
feedback: |-
  Use the bottom contact as the pivot so the ground forces produce no torque. Then combine torque balance with horizontal and vertical force balance.
```

## Rotational Dynamics

If the net torque is not zero, the system will exhibit angular acceleration. This is the rotational equivalent of Newton's second law.

![[Images/nettorqueeqn-1.jpg]]

The mass is replaced with the moment of inertia denoting that the mass distribution is now important, and the acceleration is replaced with angular acceleration.

```quiz
type: free
id: khadley-equilibrium-q2
content: |-
  **Question 2**

  A block of mass $m$ is attached to a cord wrapped around a uniform solid flywheel of mass $M$ and radius $r$. Starting from rest, how fast is the block moving after descending a distance $h$? Assume the cord does not slip.

  ![[Images/torquesystem.jpg]]
correct: |-
  Energy conservation gives
  $$mgh=\frac12mv^2+\frac12I\omega^2,$$
  with $I=Mr^2/2$ and $\omega=v/r$. Thus
  $$v=\sqrt{\frac{4mgh}{2m+M}}.$$
feedback: |-
  Include both the block's translational kinetic energy and the flywheel's rotational kinetic energy, then apply the no-slip relation $v=r\omega$.
```

```quiz
type: free
id: khadley-equilibrium-q3
content: |-
  **Question 3**

  Masses $m_1$ and $m_2$ are connected over a massless, frictionless pulley, with $m_2>m_1$. Find the acceleration magnitude.

  ![[Images/atwood1.jpg]]
correct: |-
  Adding the two mass equations cancels the common tension:
  $$a=\frac{(m_2-m_1)g}{m_1+m_2}.$$
feedback: |-
  Write one force equation for each mass using the shared acceleration magnitude. A massless pulley permits equal tension on both sides.
```

```quiz
type: free
id: khadley-equilibrium-q4
content: |-
  **Question 4**

  Repeat Question 3 for a uniform solid pulley of mass $m_p$ and radius $r$. Assume the string does not slip.

  ![[Images/atwood2.jpg]]
correct: |-
  The unequal tensions provide the pulley's torque. With $I=m_pr^2/2$ and $a=r\alpha$,
  $$a=\frac{(m_2-m_1)g}{m_1+m_2+m_p/2}.$$
feedback: |-
  A massive pulley requires separate tensions. Combine both translational force equations with $(T_2-T_1)r=I\alpha$ and the no-slip condition.
```
