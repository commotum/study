
---
title: "Rolling Motion"
source: "http://khadley.com/Courses/Physics/ph_212/topics/rigidRotation/rolling.html"
author:
published:
created: 2026-08-10
description: "Introduction to rolling"
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Rolling Motion

![[Images/12-40-figure.jpg]]

Rolling is a combination of rotational motion about an axis and translational motion of the object. In the image above, a point on the outer rim of the wheel traces out a cycloid shape. The distance between the points where the cycloid touches the ground equals the circumference of the wheel. This distance also equals the distance that the center of mass of the wheel traveled in one rotational period.

![[Images/rolleqn1.jpg]] ![[Images/rolleqn2.jpg]]

The kinetic energy of an object that rolls without slipping is the sum of the translational and rotational kinetic energies of the object.

![[Images/rolleqn3.jpg]]

## Practice Problems

```quiz
type: radio
id: khadley-rolling-q1
shuffle: true
content: |-
  **Question 1**

  A hoop, uniform solid cylinder, and uniform solid sphere have equal masses and radii and roll without slipping from rest down the same slope. Which reaches the bottom first?

  ![[Images/12-45-figure.jpg]]
options:
- id: hoop
  content: Hoop
  feedback: |-
    A hoop has the largest dimensionless inertia $I/(mr^2)=1$, so more gravitational energy goes into rotation and its center accelerates least.
- id: cylinder
  content: Solid cylinder
  feedback: |-
    The cylinder's $I/(mr^2)=1/2$ is smaller than the hoop's but larger than the sphere's, so its acceleration is intermediate.
- id: sphere
  content: Solid sphere
  correct: true
  feedback: |-
    Rolling acceleration increases as $I/(mr^2)$ decreases. The solid sphere has the smallest value, $2/5$, so it reaches the bottom first.
```

```quiz
type: free
id: khadley-rolling-q2
content: |-
  **Question 2**

  A hoop of mass $m$ and radius $r$ rolls without slipping down a slope through vertical height $h$. Find the speed of its center of mass at the bottom.
correct: |-
  With $I=mr^2$ and $v=r\omega$,
  $$mgh=\frac12mv^2+\frac12I\omega^2=mv^2,$$
  so $v=\sqrt{gh}$.
feedback: |-
  Include both translational and rotational kinetic energy. The incline angle does not affect the final speed when rolling is lossless.
```

```quiz
type: free
id: khadley-rolling-q3
content: |-
  **Question 3**

  A uniform solid cylinder of radius $r$ and mass $m$ starts from rest with a string wound around it. Find the center-of-mass speed after it unwinds and falls a distance $h$.

  ![[Images/yoyo.jpg]]
correct: |-
  Using $I=mr^2/2$ and the no-slip relation $v=r\omega$,
  $$mgh=\frac12mv^2+\frac14mv^2,$$
  which gives
  $$v=\sqrt{\frac{4gh}{3}}.$$
feedback: |-
  The falling cylinder has both translational and rotational kinetic energy. The string constraint connects them through $v=r\omega$.
```
