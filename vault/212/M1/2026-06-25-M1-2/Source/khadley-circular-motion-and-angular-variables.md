
---
title: "Circular Motion and Angular Variables"
source: "http://khadley.com/Courses/Physics/ph_212/topics/circularMotion/"
author:
published:
created: 2026-08-10
description:
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

[Image source](http://4.bp.blogspot.com/_1Z5_frqW26w/SpHb9YGDGLI/AAAAAAAAHFk/8iBMrNs3d2U/s1600/Corkscrew_\(Cedar_Point\)_01.jpg)

## Circular Motion

![[Images/angular-position-circle.jpg]]

Theta is defined as an angle in a circle of radius r. We have defined the counterclockwise direction to be positive.

![[Images/eqnderivatives.jpg]] ![[Images/u721-5.png|w is defined as the angular velocity, the time rate of change of the angle. It has units of radians per second, so can also be viewed as a frequency. ]] ![[Images/eqn4-1.jpg]] ![[Images/u1924-28.png|The angular frequency omega equals 2 pi times the frequency f, and 2 pi divided by the period T. a is the angular acceleration, the time rate of change of w. Circular motion graphical representations are similar to those for linear kinematics. The time derivative of q gives the angular velocity w The time derivative of w gives the angular acceler ation a]] ![[Images/eqn2-2.jpg]] ![[Images/eqn3-1.jpg]]

We can relate the angular variables to the translational variables using the arclength formula. Here, we have defined the tangential acceleration at and the radial acceleration ar. To completely define acceleration in three dimensions, we can include the acceleration in the z-direction az.

![[Images/acceleration.jpg]] ![[Images/coords-crop-u1946.png]]

The acceleration vector for circular motion, in polar coordinates, is mathematically equivalent to the acceleration vector in Cartesian coordinates. In both cases, the components are independent, in that they are perpendicular to each other. Acceleration in polar coordinates is used for rotating systems as a convenience.

Here we show the same acceleration vector represented in rectangular coordinates and in polar coordinates. In rectangular coordinates the vector is resolved along the x and y-axes and can be defined using the associated unit vectors x-hat and y-hat. In polar coordinates, the same acceleration vector is resolved into coordinates in the rotated frame of the r-axis (radial axis) and t-axis (tangential axis) and can be defined using the associated unit vectors r-hat and t-hat.

It is important to note that these accelerations are two representations of translational acceleration, differing in coordinate system only. The acceleration of an object can be defined by either form. We choose the form that is most convenient for the motion of the object in question.

Angular acceleration, on the other hand, is a different kind of quantity. It defines the motion of rotation, not of translation.

## Constant Angular Acceleration

For the case of constant angular acceleration, angular kinematics correlates directly to translational kinematics. Equations for position, velocity and acceleration are similar in form to equations for angle, angular velocity and angular acceleration.

![[Images/dynamiceqns.jpg]]

The left column gives the equations for linear kinematics in one dimension for the case of constant acceleration. The equations on the right are the corresponding angular kinematic equations for circular motion for constant angular acceleration.

## Uniform Circular Motion

Uniform circular motion is the special case where the speed of the particle is constant. The velocity is not constant, as the direction is changing.

### Vector Review

## Practice Problem

```quiz
type: radio
id: khadley-circular-motion-q1
shuffle: true
content: |-
  **Question 1**

  Which direction does $\vec v_2-\vec v_1$ point?

  ![[Images/vectors-1.jpg]]

  ![[Images/nsew.jpg]]
options:
- id: ne
  content: Northeast
  feedback: |-
    Subtraction means adding $-\vec v_1$. Combining a southward $\vec v_2$ with a westward $-\vec v_1$ cannot produce a northeast result.
- id: se
  content: Southeast
  feedback: |-
    The eastward component belongs to $\vec v_1$, but subtraction reverses it. The horizontal component of $\vec v_2-\vec v_1$ points west, not east.
- id: sw
  content: Southwest
  correct: true
  feedback: |-
    Write $\vec v_2-\vec v_1=\vec v_2+(-\vec v_1)$. The first vector points south and the second points west, so their sum points southwest.
- id: nw
  content: Northwest
  feedback: |-
    The vertical contribution comes from the southward vector $\vec v_2$, so the result cannot point north.
- id: none
  content: None of the above
  feedback: |-
    The difference has both a westward and a southward component, which is exactly the southwest direction.
```

```quiz
type: free
id: khadley-circular-motion-q2
content: |-
  **Question 2**

  For the velocity vectors around the circular path, determine the directions of $\vec v_2-\vec v_1$, $\vec v_3-\vec v_2$, and $\vec v_4-\vec v_3$.

  ![[Images/vectors-2.jpg]]

  ![[Images/vectors-3.jpg]]
correct: |-
  Each change-in-velocity vector points radially inward, toward the center of the circular path.
feedback: |-
  Place each pair of velocity vectors tail to tail and form $\Delta\vec v=\vec v_{\text{final}}-\vec v_{\text{initial}}$. The resulting vector points inward; in the continuous limit this gives centripetal acceleration.
```

## Deriving Radial Acceleration

![[Images/radial-acceleration-derivation-1.jpg]] ![[Images/circle-2.jpg]] ![[Images/circle-3.jpg]]

For uniform circular motion, the magnitudes of the velocity vectors are equal: v1 = v2. The velocity vectors are at right angles to the radial vectors, so the triangle made by the velocity vectors is similar (in the geometric sense) to the triangle made by the radial vectors.

These similar triangles provide a method for deriving a convenient form of the radial acceleration. For circular motion, the direction of the radial acceleration always points toward the center of the circle.

![[Images/omegadirection.jpg]]

We find the direction of the angular velocity by using the more rigorous definition of velocity as the cross product of the angular velocity and the radial vector.

The particle moves in a circular path, defining a plane. The velocity is tangential to the circle, so it is perpendicular to the radial vector. The motion can be clockwise or counterclockwise. The angular velocity is a vector so it needs to have magnitude and direction. We would like to describe the three vectors in a common orthogonal basis.

We define the direction of omega as perpendicular to the plane and choose the direction (upward or downward) using the right-hand rule for cross products.

The direction of angular acceleration is related to the direction of angular velocity similarly to the way translational acceleration (in 1-D) is related to translational velocity.

The angular velocity defines the direction as out of the plane or into the plane. If the angular speed is increasing, the angular acceleration has the same direction. If the angular speed is decreasing, the angular acceleration has the opposite direction.

![[starlogo_jk-icon_fix 9.png]] ![[osu_logo_poster_ 1.png]]
