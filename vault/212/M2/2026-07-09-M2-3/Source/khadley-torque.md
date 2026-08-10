
---
title: "Torque"
source: "http://khadley.com/Courses/Physics/ph_212/topics/rigidRotation/torque.html"
author:
published:
created: 2026-08-10
description: "Introduction to torque"
tags:
  - "clippings"
---
[PH 212](http://khadley.com/Courses/Physics/ph_212/topics/index.aspx)

## Torque

![[Images/torquing-trailer-wheels.jpg]]

[Image source](http://www.loveyourrv.com/carry-torque-wrench-rv-maintenance/)

![[Images/nettorqueeqn.jpg]]

Torque is the rotational equivalent of force.

![[Images/torque.jpg]]

```quiz
type: radio
id: khadley-torque-q1
shuffle: true
content: |-
  **Question 1**

  Four equal-magnitude forces act on a door. Which produces the largest torque magnitude about the hinge?

  ![[Images/12-18-figure.jpg]]
options:
- id: f1
  content: $\vec F_1$
  correct: true
  feedback: |-
    Torque magnitude is $rF\sin\phi$. Force $\vec F_1$ acts far from the hinge and perpendicular to the door, maximizing both the lever arm and $\sin\phi$.
- id: f2
  content: $\vec F_2$
  feedback: |-
    Force $\vec F_2$ acts along the door, so its line of action passes through the hinge and its torque is zero.
- id: f3
  content: $\vec F_3$
  feedback: |-
    Although $\vec F_3$ acts far from the hinge, only its component perpendicular to the door produces torque; that component is smaller than $F$.
- id: f4
  content: $\vec F_4$
  feedback: |-
    Force $\vec F_4$ is perpendicular, but it acts closer to the hinge than $\vec F_1$, giving it a smaller lever arm.
```

© 2005 Pearson Prentice Hall, Inc

The diagram above is similar to a free-body diagram but it includes more information; it shows where the forces are applied. We call this kind of diagram an extended free-body diagram and can use it to analyze systems that have applied torques.

![[Images/12-19-figure.jpg]] ![[Images/rcrossfeqn.jpg]]

© 2005 Pearson Prentice Hall, Inc

```quiz
type: blank
id: khadley-torque-q2
input_mode: math
require_exact: true
content: |-
  **Question 2**

  Calculate the signed torque about the pivot, taking counterclockwise torque as positive. Enter the value in $\mathrm{N\,m}$ as a number only: ==-43==

  ![[Images/wrenchdiagram.jpg]]
feedback: |-
  The angle between $\vec r$ and the downward force is $120^\circ$, so $|\tau|=(0.50\ \mathrm m)(100\ \mathrm N)\sin120^\circ=43\ \mathrm{N\,m}$. The force produces clockwise rotation, making the signed torque $-43\ \mathrm{N\,m}$ to two significant figures.
```

![[Images/12-21-figurea.jpg]] ![[Images/torqueeqn1.jpg]] ![[Images/12-21-figureb.jpg]] ![[Images/torqueeqn2.jpg]]

![[Images/trigid.jpg]]
