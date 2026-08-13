# Use Angular Impulse to Update Angular Momentum

<!--
lesson-id: 212-M3-052
topic-code: MTH212.M3.52
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Angular-Momentum Ledger](#build-the-angular-momentum-ledger)
- [Find Angular Momentum for Fixed-Axis Rotation](#find-angular-momentum-for-fixed-axis-rotation)
- [Recover Average Torque From a Momentum Change](#recover-average-torque-from-a-momentum-change)
- [Drive an End-Pivot Rod With Angular Impulse](#drive-an-end-pivot-rod-with-angular-impulse)
- [Check the Rod's Work](#check-the-rods-work)
- [Summary](#summary)

## Prerequisites

- Compute torque from $\tau=rF\sin\phi$.
- Use the moment of inertia for a specified shape and rotation axis.
- Treat counterclockwise and clockwise rotation as opposite signed directions.
- Use rotational kinetic energy $K_{\mathrm{rot}}=\frac12I\omega^2$.
- Distinguish an average rate of change from an instantaneous rate.

---

<a id="introduction"></a>
## Introduction

When an external torque acts for a time interval, it changes angular momentum. Choose a positive rotational direction and write the ledger

$$
\boxed{L_f=L_i+\tau_{\mathrm{avg}}\Delta t}.
$$

Use this order:

1. Choose the axis and positive direction.
2. Write signed $L_i$.
3. Find the signed angular impulse $\tau_{\mathrm{avg}}\Delta t$.
4. Add it to obtain $L_f$.
5. If angular speed is requested for a rigid body rotating about a fixed axis, use $\omega_f=L_f/I$ with the correct $I$.

**Lecture-video relation (`WzjIMuf-yuo`, 00:01:54–00:03:06; M2-5 lecture):**

$$
\sum\vec\tau_{\mathrm{ext}}=\frac{d\vec L}{dt}
$$

is the instantaneous statement. Integrating it over the interval gives

$$
\int_{t_i}^{t_f}\sum\vec\tau_{\mathrm{ext}}\,dt
=\Delta\vec L.
$$

Writing $\tau_{\mathrm{avg}}\Delta t=\Delta L$ is exact when $\tau_{\mathrm{avg}}$ is the time average. If the torque is constant, its average is simply that constant value.

Angular impulse has the same units as angular momentum:

$$
(\mathrm{N\,m})(\mathrm s)
=\frac{\mathrm{kg\,m^2}}{\mathrm s}.
$$

---

<a id="build-the-angular-momentum-ledger"></a>
## Build the Angular-Momentum Ledger

Angular momentum and torque are vectors. In a fixed-axis problem, their directions can be recorded with signs. For example, choose counterclockwise as positive:

- $L>0$ means counterclockwise angular momentum.
- $\tau>0$ means the torque changes $L$ in the counterclockwise direction.
- $\tau<0$ means the torque changes $L$ in the clockwise direction.

The change is always final minus initial:

$$
\Delta L=L_f-L_i.
$$

A negative $\Delta L$ does not necessarily mean the object ends clockwise. It means the angular-momentum change points in the negative direction. The final sign comes from the full ledger.

**Example:** An object begins with $L_i=+18\,\mathrm{kg\,m^2/s}$. An average torque of $-6\,\mathrm{N\,m}$ acts for $4\,\mathrm s$.

**Explanation**

$$
L_f=18+(-6)(4)=-6\,\mathrm{kg\,m^2/s}.
$$

The negative impulse has magnitude $24\,\mathrm{kg\,m^2/s}$, which is large enough to cancel the initial $+18$ and reverse the angular momentum.

```quiz
type: radio
id: mct-p16-signed-ledger
shuffle: true
content: |-
  Counterclockwise is positive. A wheel initially has $L_i=-30\,\mathrm{kg\,m^2/s}$. A constant torque of $+8\,\mathrm{N\,m}$ acts for $5.0\,\mathrm s$. What is the wheel's final angular momentum?
options:
- id: mct-p16-signed-ledger-a
  content: |-
    $+10\,\mathrm{kg\,m^2/s}$
  correct: true
  feedback: |-
    Angular impulse adds to the signed initial momentum: $L_f=L_i+\tau\Delta t=-30+(8)(5)=+10\,\mathrm{kg\,m^2/s}$. The positive impulse first stops the clockwise rotation and then leaves positive angular momentum.
- id: mct-p16-signed-ledger-b
  content: |-
    $-70\,\mathrm{kg\,m^2/s}$
  feedback: |-
    This subtracts a positive impulse from the initial momentum. A positive torque produces $\Delta L=+40\,\mathrm{kg\,m^2/s}$, so it must be added to $-30$, not subtracted.
- id: mct-p16-signed-ledger-c
  content: |-
    $+70\,\mathrm{kg\,m^2/s}$
  feedback: |-
    This adds magnitudes and discards the initial direction. The initial angular momentum is $-30$, so the signed ledger is $-30+40=+10\,\mathrm{kg\,m^2/s}$.
- id: mct-p16-signed-ledger-d
  content: |-
    $-10\,\mathrm{kg\,m^2/s}$
  feedback: |-
    The $+40$ impulse exceeds the magnitude of the initial $-30$ momentum. After reaching zero, $10\,\mathrm{kg\,m^2/s}$ of positive change remains, so the final sign is positive.
- id: mct-p16-signed-ledger-e
  content: |-
    $+1.6\,\mathrm{kg\,m^2/s}$
  feedback: |-
    This comes from dividing $8$ by $5$. Dividing torque by time computes neither angular impulse nor final angular momentum. Over a time interval, impulse is $\tau\Delta t=(8)(5)=40\,\mathrm{kg\,m^2/s}$.
```

---

<a id="find-angular-momentum-for-fixed-axis-rotation"></a>
## Find Angular Momentum for Fixed-Axis Rotation

**Source-video Problem 1 (`QghXDDJtJeQ`, 00:00:01–00:01:15):** A uniform disk has mass $10\,\mathrm{kg}$, radius $3\,\mathrm m$, and angular speed $15\,\mathrm{rad/s}$. Find its moment of inertia and angular momentum about its central symmetry axis.

For a uniform disk about that axis,

$$
I=\frac12MR^2
=\frac12(10)(3^2)
=45\,\mathrm{kg\,m^2}.
$$

For a rigid body rotating about a fixed principal axis,

$$
L=I\omega,
$$

so

$$
\boxed{L=(45)(15)=675\,\mathrm{kg\,m^2/s}}.
$$

**Source clarification:** The video describes angular-momentum units with a radians factor. Radians are dimensionless in SI, so the canonical unit is $\mathrm{kg\,m^2/s}$. Also, $L=I\omega$ is the fixed-axis rigid-body relation used here; a particle's angular momentum is generally $\vec L=\vec r\times\vec p$.

```quiz
type: radio
id: mct-p16-disk-mirror
shuffle: true
content: |-
  A uniform disk of mass $8.0\,\mathrm{kg}$ and radius $2.0\,\mathrm m$ rotates clockwise at $6.0\,\mathrm{rad/s}$. Taking counterclockwise as positive, what is its angular momentum about its central symmetry axis?
options:
- id: mct-p16-disk-mirror-a
  content: |-
    $-96\,\mathrm{kg\,m^2/s}$
  correct: true
  feedback: |-
    A uniform disk has $I=\frac12MR^2=\frac12(8)(2^2)=16\,\mathrm{kg\,m^2}$. Clockwise rotation gives $\omega=-6\,\mathrm{rad/s}$, so $L=I\omega=(16)(-6)=-96\,\mathrm{kg\,m^2/s}$.
- id: mct-p16-disk-mirror-b
  content: |-
    $+96\,\mathrm{kg\,m^2/s}$
  feedback: |-
    The magnitude follows from $I\omega$, but the sign omits the stated convention. Clockwise angular velocity is negative when counterclockwise is positive, so $L=-96\,\mathrm{kg\,m^2/s}$.
- id: mct-p16-disk-mirror-c
  content: |-
    $-192\,\mathrm{kg\,m^2/s}$
  feedback: |-
    This uses $I=MR^2$, the thin-hoop inertia. A uniform solid disk uses $I=\frac12MR^2=16\,\mathrm{kg\,m^2}$, giving $L=-96\,\mathrm{kg\,m^2/s}$.
- id: mct-p16-disk-mirror-d
  content: |-
    $-48\,\mathrm{kg\,m^2/s}$
  feedback: |-
    This effectively uses $I=\frac14MR^2$. The disk's factor is $1/2$, so $I=16\,\mathrm{kg\,m^2}$ and $L=(16)(-6)=-96\,\mathrm{kg\,m^2/s}$.
- id: mct-p16-disk-mirror-e
  content: |-
    $-24\,\mathrm{kg\,m^2/s}$
  feedback: |-
    Multiplying $M\omega/2$ omits the radius-squared dependence of rotational inertia. The correct disk inertia is $\frac12MR^2$, so the angular momentum is $-96\,\mathrm{kg\,m^2/s}$.
```

---

<a id="recover-average-torque-from-a-momentum-change"></a>
## Recover Average Torque From a Momentum Change

**Source-video Problem 2 (`QghXDDJtJeQ`, 00:01:15–00:04:06):** A rod's angular momentum rises from $15$ to $35\,\mathrm{kg\,m^2/s}$ in $4\,\mathrm s$. Find the average net torque.

Use final minus initial before dividing by the elapsed time:

$$
\tau_{\mathrm{avg}}
=\frac{\Delta L}{\Delta t}
=\frac{L_f-L_i}{\Delta t}
=\frac{35-15}{4}
=\boxed{5\,\mathrm{N\,m}}.
$$

The units reduce to torque:

$$
\frac{\mathrm{kg\,m^2/s}}{\mathrm s}
=\mathrm{kg\,m^2/s^2}
=\mathrm{N\,m}.
$$

The torque is positive because the angular momentum increases in the chosen positive direction. If $L_f<L_i$, the same calculation would produce a negative average torque.

```quiz
type: radio
id: mct-p16-average-torque-mirror
shuffle: true
content: |-
  An object's angular momentum changes from $-12$ to $+28\,\mathrm{kg\,m^2/s}$ during a $5.0\,\mathrm s$ interval. What is the average net torque?
options:
- id: mct-p16-average-torque-mirror-a
  content: |-
    $+8.0\,\mathrm{N\,m}$
  correct: true
  feedback: |-
    Average torque is the signed change in angular momentum per time. Here $\Delta L=L_f-L_i=28-(-12)=40\,\mathrm{kg\,m^2/s}$, so $\tau_{\mathrm{avg}}=40/5=+8.0\,\mathrm{N\,m}$.
- id: mct-p16-average-torque-mirror-b
  content: |-
    $+3.2\,\mathrm{N\,m}$
  feedback: |-
    This uses $28-12=16$ and loses the initial negative sign. Final minus initial is $28-(-12)=40$, so the average torque is $+8.0\,\mathrm{N\,m}$.
- id: mct-p16-average-torque-mirror-c
  content: |-
    $-8.0\,\mathrm{N\,m}$
  feedback: |-
    This reverses the subtraction. The change is $L_f-L_i=28-(-12)=+40$, so the torque that produces it is positive.
- id: mct-p16-average-torque-mirror-d
  content: |-
    $+200\,\mathrm{N\,m}$
  feedback: |-
    Multiplying $\Delta L$ by time gives the wrong dimensions. Torque is the rate of angular-momentum change, so divide $40\,\mathrm{kg\,m^2/s}$ by $5.0\,\mathrm s$.
- id: mct-p16-average-torque-mirror-e
  content: |-
    $+5.6\,\mathrm{N\,m}$
  feedback: |-
    Dividing the final angular momentum alone by time ignores the nonzero initial value. Torque depends on $\Delta L=L_f-L_i$, not on $L_f$ by itself.
```

---

<a id="drive-an-end-pivot-rod-with-angular-impulse"></a>
## Drive an End-Pivot Rod With Angular Impulse

**Source-video Problem 3 (`QghXDDJtJeQ`, 00:04:06–00:09:25):** A uniform $2.5\,\mathrm m$ rod is pivoted at its left end and begins at rest. A $300\,\mathrm N$ force acts perpendicular to the rod at its right end for $8\,\mathrm s$. The source later specifies that the rod's mass is $10\,\mathrm{kg}$.

**Frame check (04:12):** The rod is horizontal, the pivot is at the left end, and the force points upward at the right end. Thus the pictured force is perpendicular with a $2.5\,\mathrm m$ arm.

**Source clarification:** The displayed prompt omits the rod's mass; the narration supplies $M=10\,\mathrm{kg}$ at 06:21. The source's subsequent calculation also assumes the applied force remains perpendicular to the rod as it rotates, keeping $\tau=Fr$ constant for all $8\,\mathrm s$. A force that stayed vertically upward in the laboratory would cease to be perpendicular and would produce angle-dependent torque.

With counterclockwise positive, the constant torque is

$$
\tau=(300)(2.5)=750\,\mathrm{N\,m}.
$$

The rod begins at rest, so $L_i=0$. Its final angular momentum is

$$
L_f=L_i+\tau\Delta t
=0+(750)(8)
=\boxed{6000\,\mathrm{kg\,m^2/s}}.
$$

For a uniform rod about an end,

$$
I_{\mathrm{end}}=\frac13ML^2
=\frac13(10)(2.5^2)
=\frac{62.5}{3}
=20.83\,\mathrm{kg\,m^2}.
$$

Now convert $L_f$ to angular speed:

$$
\omega_f=\frac{L_f}{I_{\mathrm{end}}}
=\frac{6000}{62.5/3}
=\boxed{288\,\mathrm{rad/s}}.
$$

Do not invoke angular-momentum conservation here. The applied force supplies a nonzero external torque impulse; the angular momentum changes by exactly that impulse.

```quiz
type: radio
id: mct-p16-rod-mirror
shuffle: true
content: |-
  A uniform $6.0\,\mathrm{kg}$ rod of length $1.5\,\mathrm m$ is pivoted at one end and starts from rest. A $240\,\mathrm N$ force remains perpendicular at the other end for $5.0\,\mathrm s$. What is the rod's final angular speed?
options:
- id: mct-p16-rod-mirror-a
  content: |-
    $400\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    The constant torque is $(240)(1.5)=360\,\mathrm{N\,m}$, so $L_f=(360)(5)=1800\,\mathrm{kg\,m^2/s}$. For an end-pivot rod, $I=\frac13(6)(1.5^2)=4.5\,\mathrm{kg\,m^2}$; hence $\omega_f=L_f/I=400\,\mathrm{rad/s}$.
- id: mct-p16-rod-mirror-b
  content: |-
    $1600\,\mathrm{rad/s}$
  feedback: |-
    This uses the center-pivot rod inertia $I=\frac1{12}ML^2=1.125\,\mathrm{kg\,m^2}$. The specified axis is at an end, so $I=\frac13ML^2=4.5\,\mathrm{kg\,m^2}$ and $\omega_f=400\,\mathrm{rad/s}$.
- id: mct-p16-rod-mirror-c
  content: |-
    $133\,\mathrm{rad/s}$
  feedback: |-
    This uses $I=ML^2=13.5\,\mathrm{kg\,m^2}$, which overstates the inertia of a uniform end-pivot rod by a factor of three. It gives $1800/13.5=133\,\mathrm{rad/s}$; use $I=\frac13ML^2$ instead.
- id: mct-p16-rod-mirror-d
  content: |-
    $80\,\mathrm{rad/s}$
  feedback: |-
    This divides the torque by the rod inertia but omits the $5.0\,\mathrm s$ interval. The quantity $\tau/I$ is angular acceleration; multiply by time, or first form the angular impulse $\tau\Delta t$.
- id: mct-p16-rod-mirror-e
  content: |-
    $200\,\mathrm{rad/s}$
  feedback: |-
    This uses half the rod length as the force's moment arm, giving half the correct impulse. The force acts at the far end and remains perpendicular, so its arm is the full $1.5\,\mathrm m$ and the final speed is $400\,\mathrm{rad/s}$.
```

---

<a id="check-the-rods-work"></a>
## Check the Rod's Work

The source completes Problem 3 by finding the work done on the rod. This is a check on the impulse chain, not a replacement for it.

In the source model, the pivot does no work and the applied torque supplies the rod's rotational kinetic energy. Because the rod starts from rest,

$$
W=\Delta K_{\mathrm{rot}}
=\frac12I\omega_f^2
=\frac12\left(\frac{62.5}{3}\right)(288)^2
=\boxed{864000\,\mathrm J}.
$$

The source also checks the result using $W=\tau\Delta\theta$. Constant torque with fixed $I$ gives constant angular acceleration, so

$$
\omega_{\mathrm{avg}}=\frac{\omega_i+\omega_f}{2}
=\frac{0+288}{2}
=144\,\mathrm{rad/s},
$$

and

$$
\Delta\theta=\omega_{\mathrm{avg}}\Delta t=(144)(8)=1152\,\mathrm{rad}.
$$

Therefore,

$$
W=\tau\Delta\theta=(750)(1152)=864000\,\mathrm J.
$$

The average-angular-speed displacement formula used here requires constant angular acceleration. The relation $W=\tau\Delta\theta$ in this simple product form requires constant torque aligned with the angular displacement; otherwise, use $W=\int\tau\,d\theta$.

```quiz
type: radio
id: mct-p16-work-check
shuffle: true
content: |-
  For the mirrored rod above, $I=4.5\,\mathrm{kg\,m^2}$, $\omega_i=0$, $\omega_f=400\,\mathrm{rad/s}$, $\tau=360\,\mathrm{N\,m}$, and $\Delta t=5.0\,\mathrm s$. Which pair correctly gives the work by both allowed checks?
options:
- id: mct-p16-work-check-a
  content: |-
    $\frac12I\omega_f^2=360000\,\mathrm J$ and $\tau\left(\frac{\omega_i+\omega_f}{2}\Delta t\right)=360000\,\mathrm J$
  correct: true
  feedback: |-
    With constant torque and fixed inertia, angular acceleration is constant. Thus $\Delta K=\frac12(4.5)(400^2)=360000\,\mathrm J$, while $\Delta\theta=[(0+400)/2](5)=1000\,\mathrm{rad}$ and $\tau\Delta\theta=(360)(1000)=360000\,\mathrm J$.
- id: mct-p16-work-check-b
  content: |-
    $\frac12I\omega_f=900\,\mathrm J$ and $\tau\omega_f\Delta t=720000\,\mathrm J$
  feedback: |-
    Rotational kinetic energy depends on $\omega^2$, not $\omega$. The displacement check also needs average angular speed, not final angular speed, because the rod accelerates from rest.
- id: mct-p16-work-check-c
  content: |-
    $I\omega_f^2=720000\,\mathrm J$ and $\tau\left(\frac{\omega_i+\omega_f}{2}\Delta t\right)=360000\,\mathrm J$
  feedback: |-
    The torque-displacement check is right, but rotational kinetic energy is $\frac12I\omega^2$. Omitting the factor $1/2$ doubles the energy to the displayed incorrect value.
- id: mct-p16-work-check-d
  content: |-
    $\frac12I\omega_f^2=360000\,\mathrm J$ and $\tau\omega_f\Delta t=720000\,\mathrm J$
  feedback: |-
    The energy check is right. The second value uses $\omega_f$ for all $5.0\,\mathrm s$, but constant acceleration from rest gives $\omega_{\mathrm{avg}}=(0+400)/2=200\,\mathrm{rad/s}$.
- id: mct-p16-work-check-e
  content: |-
    Both methods are invalid because an external torque acts.
  feedback: |-
    The external torque prevents angular-momentum conservation, but it is exactly what does work and supplies angular impulse. Under the stated constant-torque model, both $\Delta K_{\mathrm{rot}}$ and $\tau\Delta\theta$ are valid checks.
```

---

<a id="summary"></a>
## Summary

- When a torque acts for a time, use the signed ledger $L_f=L_i+\tau_{\mathrm{avg}}\Delta t$.
- Compute $\Delta L$ as final minus initial; the sign records the direction of the change.
- Angular impulse has units $\mathrm{N\,m\,s}=\mathrm{kg\,m^2/s}$.
- Use $L=I\omega$ for the fixed-axis rigid-body cases in this lesson, with $I$ matched to both shape and axis.
- Do not conserve angular momentum while a nonzero external torque impulse acts.
- A work check using average angular speed needs constant angular acceleration; $W=\tau\Delta\theta$ as a product needs constant aligned torque.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
