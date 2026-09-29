# Angular Position, Displacement, and Average Angular Velocity

<!--
lesson-id: 212-M1-075
topic-code: M1.75
-->

## Table of Contents

- [Introduction](#introduction)
- [Separate Position From Displacement](#separate-position-from-displacement)
- [Carry Direction With the Sign](#carry-direction-with-the-sign)
- [Divide the Angular Change by Elapsed Time](#divide-the-angular-change-by-elapsed-time)
- [Convert the Time Unit Before Dividing](#convert-the-time-unit-before-dividing)
- [Convert Revolutions to Radians](#convert-revolutions-to-radians)
- [Summary](#summary)

## Prerequisites

- Subtract signed numbers.
- Divide a change by a positive elapsed time.
- Use $1\,\mathrm{min}=60\,\mathrm{s}$ as a conversion equality.

---

<a id="introduction"></a>
## Introduction

Motion along a straight line can be described by a starting position, an ending position, and the time between them. Rotational motion uses the same idea, but it tracks orientation instead of location. Imagine marking one spoke on a wheel and measuring its angle from a fixed reference line. That angle is the spoke's **angular position** $\theta$. Comparing its initial and final angular positions gives its **angular displacement** $\Delta\theta$; dividing that change by the elapsed time gives its **average angular velocity** $\omega_{\mathrm{avg}}$.

To distinguish the two possible rotation directions, choose a sign convention before calculating. In this lesson, counterclockwise is positive and clockwise is negative. If $\theta_i$ is the initial angular position and $\theta_f$ is the final angular position, the signed angular displacement is

$$
\Delta\theta=\theta_f-\theta_i.
$$

If a prompt gives the angle swept instead of two angular positions, assign that angle a sign from its direction and use it as $\Delta\theta$.

To find average angular velocity, divide the signed angular displacement by the positive elapsed time:

$$
\omega_{\mathrm{avg}}=\frac{\Delta\theta}{\Delta t}.
$$

Because elapsed time is positive, the sign of $\omega_{\mathrm{avg}}$ gives the direction of the net rotation. Angles in this lesson are measured in radians ($\mathrm{rad}$), so angular velocity is measured in $\mathrm{rad/s}$: signed angular change per second.

For motion that does not reverse direction during the interval, the magnitude of $\omega_{\mathrm{avg}}$ is also the average angular speed. If the object reverses, average speed instead uses the total angle traveled divided by time.

Start by identifying the target. For $\Delta\theta$, subtract the endpoint angles or sign the stated swept angle. For $\omega_{\mathrm{avg}}$, find that signed angular displacement and then divide by $\Delta t$.

---

<a id="separate-position-from-displacement"></a>
## Separate Position From Displacement

**Example:** A pointer begins at $\theta_i=0.7\,\mathrm{rad}$ and ends at $\theta_f=2.9\,\mathrm{rad}$. Find its angular displacement.

**Explanation**

Both given values are angular positions, so subtract them to find the angular displacement:

$$
\Delta\theta=\theta_f-\theta_i
=2.9\,\mathrm{rad}-0.7\,\mathrm{rad}
=2.2\,\mathrm{rad}.
$$

The result is positive, so the net change is counterclockwise under the stated convention.

```quiz
type: radio
id: mct-p1-position
content: |-
  A dial begins at $\theta_i=-0.4\,\mathrm{rad}$ and ends at $\theta_f=1.1\,\mathrm{rad}$. What is its angular displacement?
options:
- id: mct-p1-position-a
  content: |-
    $1.5\,\mathrm{rad}$
  correct: true
  feedback: |-
    Angular displacement is final position minus initial position. Here $1.1-(-0.4)=1.5$, so $\Delta\theta=1.5\,\mathrm{rad}$.
- id: mct-p1-position-b
  content: |-
    $-1.5\,\mathrm{rad}$
  feedback: |-
    This reverses the subtraction. The order is $\theta_f-\theta_i$, not $\theta_i-\theta_f$; using $1.1-(-0.4)$ gives a positive change.
- id: mct-p1-position-c
  content: |-
    $0.7\,\mathrm{rad}$
  feedback: |-
    This treats subtracting $-0.4$ as subtracting $0.4$. Subtracting a negative adds its magnitude: $1.1-(-0.4)=1.5$.
- id: mct-p1-position-d
  content: |-
    $1.1\,\mathrm{rad}$
  feedback: |-
    $1.1\,\mathrm{rad}$ is the final angular position, not the change in position. Displacement compares both endpoints through $\theta_f-\theta_i$.
- id: mct-p1-position-e
  content: |-
    $-0.4\,\mathrm{rad}$
  feedback: |-
    $-0.4\,\mathrm{rad}$ is the initial angular position. The requested displacement is the difference between final and initial positions.
```

---

<a id="carry-direction-with-the-sign"></a>
## Carry Direction With the Sign

**Example:** A wheel moves from $\theta_i=1.6\,\mathrm{rad}$ to $\theta_f=-0.2\,\mathrm{rad}$. Find its angular displacement and interpret its sign.

**Explanation**

$$
\Delta\theta=-0.2\,\mathrm{rad}-1.6\,\mathrm{rad}
=-1.8\,\mathrm{rad}.
$$

The negative sign means the wheel's net rotation is clockwise. It does not mean the wheel moved a “negative amount”; the magnitude of the angular displacement is $1.8\,\mathrm{rad}$.

```quiz
type: radio
id: mct-p1-direction
content: |-
  Counterclockwise is positive. A marker starts at $\theta_i=1.20\,\mathrm{rad}$ and then turns $0.75\,\mathrm{rad}$ clockwise. Which pair gives its angular displacement and final angular position?
options:
- id: mct-p1-direction-a
  content: |-
    $\Delta\theta=-0.75\,\mathrm{rad}$ and $\theta_f=0.45\,\mathrm{rad}$
  correct: true
  feedback: |-
    Clockwise motion is negative, so $\Delta\theta=-0.75\,\mathrm{rad}$. Then $\theta_f=\theta_i+\Delta\theta=1.20-0.75=0.45\,\mathrm{rad}$.
- id: mct-p1-direction-b
  content: |-
    $\Delta\theta=0.75\,\mathrm{rad}$ and $\theta_f=1.95\,\mathrm{rad}$
  feedback: |-
    This assigns a positive sign to clockwise motion. With counterclockwise positive, clockwise displacement is negative, so the final position must decrease from $1.20\,\mathrm{rad}$.
- id: mct-p1-direction-c
  content: |-
    $\Delta\theta=-0.75\,\mathrm{rad}$ and $\theta_f=1.95\,\mathrm{rad}$
  feedback: |-
    The displacement sign is correct, but the final position was found by adding its magnitude. Add the signed displacement: $1.20+(-0.75)=0.45\,\mathrm{rad}$.
- id: mct-p1-direction-d
  content: |-
    $\Delta\theta=0.75\,\mathrm{rad}$ and $\theta_f=0.45\,\mathrm{rad}$
  feedback: |-
    The final position reflects a clockwise decrease, but the displacement sign contradicts that direction. A decrease of $0.75\,\mathrm{rad}$ is $\Delta\theta=-0.75\,\mathrm{rad}$.
```

---

<a id="divide-the-angular-change-by-elapsed-time"></a>
## Divide the Angular Change by Elapsed Time

**Example:** A rotor changes from $\theta_i=-0.5\,\mathrm{rad}$ to $\theta_f=3.1\,\mathrm{rad}$ in $0.80\,\mathrm{s}$. Find its average angular velocity.

**Explanation**

First find the signed angular displacement:

$$
\Delta\theta=3.1-(-0.5)=3.6\,\mathrm{rad}.
$$

Then divide by the elapsed time:

$$
\omega_{\mathrm{avg}}
=\frac{3.6\,\mathrm{rad}}{0.80\,\mathrm{s}}
=4.5\,\mathrm{rad/s}.
$$

The positive result means the net rotation during the interval is counterclockwise.

```quiz
type: radio
id: mct-p1-average-rate
content: |-
  A wheel moves from $\theta_i=2.4\,\mathrm{rad}$ to $\theta_f=-1.2\,\mathrm{rad}$ in $1.5\,\mathrm{s}$. What is its average angular velocity?
options:
- id: mct-p1-average-rate-a
  content: |-
    $-2.4\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    Final minus initial gives $\Delta\theta=-1.2-2.4=-3.6\,\mathrm{rad}$. Dividing by $1.5\,\mathrm{s}$ gives $\omega_{\mathrm{avg}}=-2.4\,\mathrm{rad/s}$.
- id: mct-p1-average-rate-b
  content: |-
    $2.4\,\mathrm{rad/s}$
  feedback: |-
    This loses the direction by using only the displacement's magnitude. The signed change is $-3.6\,\mathrm{rad}$, so dividing by positive elapsed time preserves the negative sign.
- id: mct-p1-average-rate-c
  content: |-
    $-3.6\,\mathrm{rad/s}$
  feedback: |-
    $-3.6\,\mathrm{rad}$ is the angular displacement. Average angular velocity requires one more step: divide that change by the $1.5\,\mathrm{s}$ interval.
- id: mct-p1-average-rate-d
  content: |-
    $-0.8\,\mathrm{rad/s}$
  feedback: |-
    This divides the final position by time, but a rate over an interval uses the change in position. Use $(-1.2-2.4)/1.5$, not $-1.2/1.5$.
- id: mct-p1-average-rate-e
  content: |-
    $-0.42\,\mathrm{s/rad}$
  feedback: |-
    This inverts the quotient and produces time per angle. Angular velocity is angular displacement divided by time, so its units are $\mathrm{rad/s}$.
```

---

<a id="convert-the-time-unit-before-dividing"></a>
## Convert the Time Unit Before Dividing

**Example (source video):** A disk turns through $5000\,\mathrm{rad}$ in $10\,\mathrm{min}$. Taking the stated rotation as positive, find its average angular velocity in radians per second.

**Explanation**

Convert the elapsed time so its unit matches the requested denominator:

$$
10\,\mathrm{min}
\left(\frac{60\,\mathrm{s}}{1\,\mathrm{min}}\right)
=600\,\mathrm{s}.
$$

The minutes cancel and seconds remain. Now divide:

$$
\omega_{\mathrm{avg}}
=\frac{5000\,\mathrm{rad}}{600\,\mathrm{s}}
\approx 8.33\,\mathrm{rad/s}.
$$

```quiz
type: radio
id: mct-p1-time-conversion
content: |-
  A drum sweeps $540\,\mathrm{rad}$ clockwise in $1.5\,\mathrm{min}$. What is its average angular velocity in radians per second? Use counterclockwise as positive.
options:
- id: mct-p1-time-conversion-a
  content: |-
    $-6.0\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    Clockwise makes $\Delta\theta=-540\,\mathrm{rad}$, and $1.5\,\mathrm{min}=90\,\mathrm{s}$. Thus $\omega_{\mathrm{avg}}=-540/90=-6.0\,\mathrm{rad/s}$.
- id: mct-p1-time-conversion-b
  content: |-
    $6.0\,\mathrm{rad/s}$
  feedback: |-
    The magnitude uses the correct $90\,\mathrm{s}$ interval, but the sign was dropped. Clockwise is negative under the stated convention, so the average angular velocity is negative.
- id: mct-p1-time-conversion-c
  content: |-
    $-360\,\mathrm{rad/s}$
  feedback: |-
    Dividing by $1.5$ gives radians per minute, not radians per second. Convert $1.5\,\mathrm{min}$ to $90\,\mathrm{s}$ before dividing.
- id: mct-p1-time-conversion-d
  content: |-
    $-9.0\,\mathrm{rad/s}$
  feedback: |-
    This uses $60\,\mathrm{s}$ but omits the factor of $1.5$. The full interval is $1.5(60)=90\,\mathrm{s}$, so the quotient's magnitude is $540/90=6.0$.
```

---

<a id="convert-revolutions-to-radians"></a>
## Convert Revolutions to Radians

One full revolution is an angular displacement of $2\pi\,\mathrm{rad}$:

$$
1\,\mathrm{rev}=2\pi\,\mathrm{rad}.
$$

**Example:** A wheel makes $2.5$ revolutions clockwise in $10\,\mathrm{s}$. Find its average angular velocity in radians per second.

**Explanation**

Give the clockwise displacement a negative sign, then use a conversion factor whose revolutions cancel:

$$
\Delta\theta
=-2.5\,\mathrm{rev}
\left(\frac{2\pi\,\mathrm{rad}}{1\,\mathrm{rev}}\right)
=-5\pi\,\mathrm{rad}.
$$

Now divide by the elapsed time:

$$
\omega_{\mathrm{avg}}
=\frac{-5\pi\,\mathrm{rad}}{10\,\mathrm{s}}
=-\frac{\pi}{2}\,\mathrm{rad/s}.
$$

If a problem gives only the initial and final visible orientations, it cannot reveal unreported complete turns. When the problem states a number of swept revolutions, use that signed swept angle as $\Delta\theta$.

```quiz
type: radio
id: mct-p1-revolution-conversion
content: |-
  A turntable completes $1.5$ revolutions counterclockwise in $6.0\,\mathrm{s}$. What is its average angular velocity?
options:
- id: mct-p1-revolution-conversion-a
  content: |-
    $\dfrac{\pi}{2}\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    Counterclockwise is positive, and $1.5\,\mathrm{rev}=1.5(2\pi)=3\pi\,\mathrm{rad}$. Dividing by $6.0\,\mathrm{s}$ gives $\pi/2\,\mathrm{rad/s}$.
- id: mct-p1-revolution-conversion-b
  content: |-
    $-\dfrac{\pi}{2}\,\mathrm{rad/s}$
  feedback: |-
    The magnitude follows from converting $1.5$ revolutions and dividing by $6.0\,\mathrm{s}$, but the direction sign is reversed. Counterclockwise is positive here.
- id: mct-p1-revolution-conversion-c
  content: |-
    $3\pi\,\mathrm{rad/s}$
  feedback: |-
    $3\pi\,\mathrm{rad}$ is the converted angular displacement, not the rate. Divide that displacement by the $6.0\,\mathrm{s}$ interval.
- id: mct-p1-revolution-conversion-d
  content: |-
    $0.25\,\mathrm{rad/s}$
  feedback: |-
    This divides $1.5$ by $6.0$ while treating revolutions as radians. Convert with $2\pi\,\mathrm{rad}$ per revolution before dividing by time.
- id: mct-p1-revolution-conversion-e
  content: |-
    $\dfrac{\pi}{12}\,\mathrm{rad/s}$
  feedback: |-
    This effectively uses too small a radian conversion. One full revolution is $2\pi\,\mathrm{rad}$, so $1.5$ revolutions is $3\pi\,\mathrm{rad}$, not $\pi/2\,\mathrm{rad}$.
```

---

<a id="summary"></a>
## Summary

Use this procedure whenever a prompt supplies two angular positions or a signed angle swept over an interval:

1. State the sign convention: here counterclockwise is positive and clockwise is negative.
2. Find the signed angular displacement with $\Delta\theta=\theta_f-\theta_i$, or assign a sign to the stated swept angle.
3. Convert revolutions to radians with $1\,\mathrm{rev}=2\pi\,\mathrm{rad}$ when needed.
4. Convert the elapsed time to the unit requested in the denominator.
5. For an average angular velocity, compute $\omega_{\mathrm{avg}}=\Delta\theta/\Delta t$.

Do not substitute the final angular position for the displacement, reverse final-minus-initial, discard the direction sign, or divide before making the units consistent.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
