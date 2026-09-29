# Period, Frequency, and Angular Speed

<!--
lesson-id: 212-M1-077
topic-code: M1.77
-->

## Table of Contents

- [Introduction](#introduction)
- [Build Period and Frequency From Counts](#build-period-and-frequency-from-counts)
- [Apply Cycle Rates to Circular Motion](#apply-cycle-rates-to-circular-motion)
- [Use One Revolution to Find Angular Speed](#use-one-revolution-to-find-angular-speed)
- [Convert Between RPM and SI Rates](#convert-rpm-before-using-si-units)
- [Work Backward From Angular Speed](#work-backward-from-angular-speed)
- [Summary](#summary)

## Prerequisites

- Divide one measured quantity by another to form a rate.
- Take the reciprocal of a nonzero number.
- Use $1\,\mathrm{min}=60\,\mathrm{s}$ and $1\,\mathrm{rev}=2\pi\,\mathrm{rad}$ as conversion factors.

---

<a id="introduction"></a>
## Introduction

A rotating object can repeat the same motion while the prompt describes that repetition in three different ways:

| Quantity | Recognition cue | Unit meaning |
| --- | --- | --- |
| Period $T$ | “time for one revolution” | seconds per cycle |
| Frequency $f$ | “cycles or revolutions per second” | cycles per second, or hertz ($\mathrm{Hz}$) |
| Angular speed $\omega$ | “radians per second” | angular distance per second |

Translate the words into a unit ratio, identify the requested unit, and choose the shortest relationship between the given and the target. If $N$ cycles occur during time $t$, then

$$
T=\frac{t}{N},
\qquad
f=\frac{N}{t}.
$$

These ratios are reciprocals because one asks for **time per cycle** and the other asks for **cycles per time**:

$$
T=\frac{1}{f}.
$$

One full cycle is $2\pi$ radians, so

$$
\omega=2\pi f
\qquad\text{and}\qquad
\omega=\frac{2\pi}{T}.
$$

Choose the direct link that contains the given and the target:

| Given | Requested | Shortest route |
| --- | --- | --- |
| $N$ cycles in time $t$ | $f$ or $T$ | $f=N/t$ or $T=t/N$ |
| $f$ | $T$ or $\omega$ | $T=1/f$ or $\omega=2\pi f$ |
| $T$ | $f$ or $\omega$ | $f=1/T$ or $\omega=2\pi/T$ |
| $\omega$ | $f$ or $T$ | $f=\omega/(2\pi)$ or $T=2\pi/\omega$ |
| RPM | an SI rate | First convert minutes to seconds |

Throughout this lesson, $\omega$ means the nonnegative **angular speed**. If a direction is specified, angular velocity also carries a sign chosen from the stated direction convention.

---

<a id="build-period-and-frequency-from-counts"></a>
## Build Period and Frequency From Counts

**Example:** A calibration wheel completes $42$ revolutions in $14.0\,\mathrm{s}$. Find its frequency and period.

**Explanation**

The phrase “$42$ revolutions in $14.0\,\mathrm{s}$” supplies a cycle count $N=42$ and a total time $t=14.0\,\mathrm{s}$. Frequency puts cycles over time:

$$
f=\frac{N}{t}
=\frac{42\,\mathrm{rev}}{14.0\,\mathrm{s}}
=3.00\,\mathrm{Hz}.
$$

Period puts time over cycles:

$$
T=\frac{t}{N}
=\frac{14.0\,\mathrm{s}}{42\,\mathrm{rev}}
=0.333\,\mathrm{s}.
$$

The units identify each quotient. The results must also satisfy the reciprocal relationship $T=1/f$.

```quiz
type: radio
id: mct-p3-count-rate
content: |-
  A test rotor completes $45$ revolutions in $12.0\,\mathrm{s}$. Which pair gives its frequency $f$ and period $T$?
options:
- id: mct-p3-count-rate-a
  content: |-
    $f=3.75\,\mathrm{Hz}$ and $T=0.267\,\mathrm{s}$
  correct: true
  feedback: |-
    Frequency is cycle count divided by total time, so $f=45/12.0=3.75\,\mathrm{Hz}$. Period is time divided by cycle count, so $T=12.0/45=0.267\,\mathrm{s}$; the two results also satisfy $fT=1$.
- id: mct-p3-count-rate-b
  content: |-
    $f=0.267\,\mathrm{Hz}$ and $T=3.75\,\mathrm{s}$
  feedback: |-
    This swaps the two unit ratios. The quotient $12.0\,\mathrm{s}/45\,\mathrm{rev}$ is seconds per revolution, so it is the period, while $45\,\mathrm{rev}/12.0\,\mathrm{s}$ is the frequency.
- id: mct-p3-count-rate-c
  content: |-
    $f=3.75\,\mathrm{Hz}$ and $T=3.75\,\mathrm{s}$
  feedback: |-
    The frequency calculation is correct, but period is not the same numerical rate with different units. Period reverses the ratio, so $T=1/f=1/3.75=0.267\,\mathrm{s}$.
- id: mct-p3-count-rate-d
  content: |-
    $f=45\,\mathrm{Hz}$ and $T=12.0\,\mathrm{s}$
  feedback: |-
    These are the total cycle count and total elapsed time, not per-unit rates. Divide $45$ revolutions by $12.0\,\mathrm{s}$ for cycles per second and reverse that quotient for seconds per cycle.
- id: mct-p3-count-rate-e
  content: |-
    $f=540\,\mathrm{Hz}$ and $T=0.00185\,\mathrm{s}$
  feedback: |-
    Multiplying cycle count by elapsed time produces units of $\mathrm{rev}\cdot\mathrm{s}$, not a frequency. A frequency requires $N/t$, giving $3.75\,\mathrm{Hz}$, and its reciprocal gives the period.
```

---

<a id="apply-cycle-rates-to-circular-motion"></a>
## Apply Cycle Rates to Circular Motion

Later source videos use the same cycle-rate conversions inside longer circular-motion problems. Complete the period/frequency conversion first, then hand the result to the next equation.

**Source-video example:** A ball travels around a horizontal circle of radius $1.5\,\mathrm m$ at $3\,\mathrm{rev/s}$. Find its frequency, period, and tangential speed.

The stated rotation rate is already cycles per second:

$$
f=3\,\mathrm{Hz},
\qquad
T=\frac1f=\frac13\,\mathrm s.
$$

One circumference is $2\pi r$, so

$$
v=\frac{2\pi r}{T}
=\frac{2\pi(1.5\,\mathrm m)}{1/3\,\mathrm s}
=9\pi\,\mathrm{m/s}
\approx28.27\,\mathrm{m/s}.
$$

The video's next step calculates radial acceleration; that part is worked in [Radial, Tangential, and Net Acceleration](<MCT-Problem-4.md>).

**Source-video example:** A rotor of radius $8\,\mathrm m$ spins at $25\,\mathrm{rpm}$. Convert the rate and find the rim speed used later in the rotor-friction problem.

One route converts RPM to frequency and period:

$$
f=25\,\frac{\mathrm{rev}}{\mathrm{min}}
\left(\frac{1\,\mathrm{min}}{60\,\mathrm s}\right)
=0.4167\,\mathrm{Hz},
\qquad
T=\frac1f=2.4\,\mathrm s,
$$

$$
v=\frac{2\pi r}{T}
=\frac{2\pi(8\,\mathrm m)}{2.4\,\mathrm s}
=20.94\,\mathrm{m/s}.
$$

As a check, convert directly to angular speed and use $v=r\omega$:

$$
\omega=25\,\frac{\mathrm{rev}}{\mathrm{min}}
\left(\frac{2\pi\,\mathrm{rad}}{1\,\mathrm{rev}}\right)
\left(\frac{1\,\mathrm{min}}{60\,\mathrm s}\right)
=2.618\,\mathrm{rad/s},
$$

$$
v=r\omega=(8\,\mathrm m)(2.618\,\mathrm{rad/s})=20.94\,\mathrm{m/s}.
$$

Both routes must agree. The friction decision that uses this speed belongs in [Solving Static-Friction Thresholds in Circular Motion](<MCT-Problem-9.md>).

**Source-video example:** A tetherball moves around a horizontal circle of radius $1.5\,\mathrm m$ at $3.5\,\mathrm{m/s}$. Find its period and frequency.

Divide one circumference by the tangential speed:

$$
T=\frac{2\pi r}{v}
=\frac{2\pi(1.5\,\mathrm m)}{3.5\,\mathrm{m/s}}
=2.69\,\mathrm s,
\qquad
f=\frac1T=0.371\,\mathrm{Hz}.
$$

The tilted-tension calculation for this same tetherball is kept in [Resolving a Tilted Support Force in Horizontal Circular Motion](<MCT-Problem-10.md>).

---

<a id="use-one-revolution-to-find-angular-speed"></a>
## Use One Revolution to Find Angular Speed

**Source-video example:** A spinning wheel has frequency $30\,\mathrm{Hz}$ and diameter $50\,\mathrm{cm}$. Find its angular speed and period.

**Explanation**

Frequency counts complete revolutions each second. Replace every revolution with $2\pi$ radians:

$$
\begin{aligned}
\omega
&=\left(2\pi\,\frac{\mathrm{rad}}{\mathrm{rev}}\right)
  \left(30\,\frac{\mathrm{rev}}{\mathrm{s}}\right) \\
&=60\pi\,\mathrm{rad/s} \\
&\approx 188.5\,\mathrm{rad/s}.
\end{aligned}
$$

Canceling revolutions leaves radians per second, which gives $\omega=2\pi f$. The period is time per revolution, so

$$
T=\frac{1}{f}
=\frac{1}{30\,\mathrm{s^{-1}}}
=0.0333\ldots\,\mathrm{s}
\approx0.033\,\mathrm{s}.
$$

The diameter is not needed for either requested quantity. A radius would matter for tangential speed, but frequency alone determines both $\omega$ and $T$. If a problem gives the period instead, use the direct relationship

$$
\omega=2\pi\left(\frac{1}{T}\right)=\frac{2\pi}{T}.
$$

```quiz
type: radio
id: mct-p3-period-to-omega
content: |-
  A disk of radius $0.600\,\mathrm{m}$ completes one revolution every $0.250\,\mathrm{s}$. What is its angular speed?
options:
- id: mct-p3-period-to-omega-a
  content: |-
    $8\pi\,\mathrm{rad/s}\approx25.1\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    One revolution contributes $2\pi$ radians, and the period gives the time for that revolution. Thus $\omega=2\pi/T=2\pi/(0.250\,\mathrm{s})=8\pi\,\mathrm{rad/s}$; the radius is unnecessary for angular speed.
- id: mct-p3-period-to-omega-b
  content: |-
    $0.500\pi\,\mathrm{rad/s}\approx1.57\,\mathrm{rad/s}$
  feedback: |-
    This multiplies $2\pi$ by the period, producing radians times seconds rather than radians per second. Because the rotation covers $2\pi$ radians in $0.250\,\mathrm{s}$, divide by the time: $\omega=2\pi/T$.
- id: mct-p3-period-to-omega-c
  content: |-
    $4.00\,\mathrm{rad/s}$
  feedback: |-
    The reciprocal $1/T=4.00\,\mathrm{Hz}$ is the number of complete revolutions per second. Angular speed counts radians per second, so each revolution must still contribute $2\pi$ radians, giving $8\pi\,\mathrm{rad/s}$.
- id: mct-p3-period-to-omega-d
  content: |-
    $15.1\,\mathrm{rad/s}$
  feedback: |-
    This value comes from multiplying the correct angular speed by the radius. That operation finds tangential speed and would have units of meters per second; the requested angular speed is $2\pi/T=8\pi\,\mathrm{rad/s}$.
- id: mct-p3-period-to-omega-e
  content: |-
    $0.250\,\mathrm{rad/s}$
  feedback: |-
    The given $0.250\,\mathrm{s}$ is a time per revolution, not an angle per time. Convert the one revolution to $2\pi$ radians and divide by its period to obtain angular speed.
```

---

<a id="convert-rpm-before-using-si-units"></a>
## Convert Between RPM and SI Rates

**Source-video example:** A disk has angular speed $8.33\,\mathrm{rad/s}$. Express the rotation rate in revolutions per minute.

**Explanation**

RPM means revolutions per minute. Start with the given angular speed, convert radians to revolutions, and then convert the time denominator from seconds to minutes:

$$
\begin{aligned}
8.33\,\frac{\mathrm{rad}}{\mathrm{s}}
\left(\frac{1\,\mathrm{rev}}{2\pi\,\mathrm{rad}}\right)
\left(\frac{60\,\mathrm{s}}{1\,\mathrm{min}}\right)
&=79.5\,\frac{\mathrm{rev}}{\mathrm{min}} \\
&=79.5\,\mathrm{rpm}.
\end{aligned}
$$

Both unwanted units cancel, leaving the requested unit. In the reverse direction, convert RPM to hertz before using SI relationships. For example,

$$
150\,\frac{\mathrm{rev}}{\mathrm{min}}
\left(\frac{1\,\mathrm{min}}{60\,\mathrm{s}}\right)
=2.50\,\frac{\mathrm{rev}}{\mathrm{s}}
=2.50\,\mathrm{Hz}.
$$

Now use the converted frequency in the SI relationships:

$$
\omega=2\pi f=5\pi\,\mathrm{rad/s}\approx15.7\,\mathrm{rad/s},
\qquad
T=\frac{1}{f}=0.400\,\mathrm{s}.
$$

As a direction check, RPM to hertz divides the numerical value by $60$, while hertz to RPM multiplies it by $60$.

```quiz
type: radio
id: mct-p3-rpm-conversion
content: |-
  A motor shaft rotates at $360\,\mathrm{rpm}$. Which row correctly gives its frequency, angular speed, and period?
options:
- id: mct-p3-rpm-conversion-a
  content: |-
    $f=6.00\,\mathrm{Hz}$, $\omega=12\pi\,\mathrm{rad/s}$, and $T=0.167\,\mathrm{s}$
  correct: true
  feedback: |-
    Dividing $360\,\mathrm{rev/min}$ by $60\,\mathrm{s/min}$ gives $6.00\,\mathrm{rev/s}=6.00\,\mathrm{Hz}$. Therefore $\omega=2\pi f=12\pi\,\mathrm{rad/s}$ and $T=1/f=0.167\,\mathrm{s}$.
- id: mct-p3-rpm-conversion-b
  content: |-
    $f=360\,\mathrm{Hz}$, $\omega=720\pi\,\mathrm{rad/s}$, and $T=0.00278\,\mathrm{s}$
  feedback: |-
    This treats “per minute” as “per second.” A minute contains $60$ seconds, so the number of revolutions in each second is $360/60=6.00$, not $360$.
- id: mct-p3-rpm-conversion-c
  content: |-
    $f=6.00\,\mathrm{Hz}$, $\omega=6.00\,\mathrm{rad/s}$, and $T=0.167\,\mathrm{s}$
  feedback: |-
    The RPM conversion and period are correct, but $6.00\,\mathrm{Hz}$ counts full revolutions per second. Each revolution is $2\pi$ radians, so angular speed is $2\pi(6.00)=12\pi\,\mathrm{rad/s}$.
- id: mct-p3-rpm-conversion-d
  content: |-
    $f=21{,}600\,\mathrm{Hz}$, $\omega=43{,}200\pi\,\mathrm{rad/s}$, and $T=0.0000463\,\mathrm{s}$
  feedback: |-
    Multiplying RPM by $60$ converts in the wrong direction: it makes the numerical rate larger even though one second is a smaller time interval than one minute. Use $1\,\mathrm{min}/60\,\mathrm{s}$ so minutes cancel, which divides the RPM value by $60$.
- id: mct-p3-rpm-conversion-e
  content: |-
    $f=6.00\,\mathrm{Hz}$, $\omega=12\pi\,\mathrm{rad/s}$, and $T=6.00\,\mathrm{s}$
  feedback: |-
    The frequency and angular speed are correct, but a frequency of $6.00$ cycles each second cannot have a six-second period. Period is seconds per one cycle, so it is the reciprocal: $T=1/6.00=0.167\,\mathrm{s}$.
```

<a id="work-backward-from-angular-speed"></a>
## Work Backward From Angular Speed

**Example:** A shaft has angular speed $\omega=10\pi\,\mathrm{rad/s}$. Find its frequency and period.

**Explanation**

Angular speed counts radians per second. Divide by the $2\pi$ radians in each revolution to recover revolutions per second:

$$
f=\frac{\omega}{2\pi}
=\frac{10\pi}{2\pi}
=5.00\,\mathrm{Hz}.
$$

Then take the reciprocal to find seconds per revolution:

$$
T=\frac{1}{f}=0.200\,\mathrm{s}.
$$

If only the period is requested, the shortest direct relationship is the rearranged one-cycle equation

$$
T=\frac{2\pi}{\omega}.
$$

```quiz
type: radio
id: mct-p3-omega-reverse
content: |-
  A turntable has angular speed $\omega=3\pi\,\mathrm{rad/s}$. What are its frequency and period?
options:
- id: mct-p3-omega-reverse-a
  content: |-
    $f=1.50\,\mathrm{Hz}$ and $T=0.667\,\mathrm{s}$
  correct: true
  feedback: |-
    Each revolution contains $2\pi$ radians, so $f=\omega/(2\pi)=3\pi/(2\pi)=1.50\,\mathrm{Hz}$. Period is the reciprocal rate, $T=1/f=2/3\,\mathrm{s}\approx0.667\,\mathrm{s}$.
- id: mct-p3-omega-reverse-b
  content: |-
    $f=3\pi\,\mathrm{Hz}$ and $T=\dfrac{1}{3\pi}\,\mathrm{s}$
  feedback: |-
    This relabels radians per second as cycles per second. Frequency counts complete revolutions, so divide the angular speed by $2\pi\,\mathrm{rad/rev}$ before taking the reciprocal for period.
- id: mct-p3-omega-reverse-c
  content: |-
    $f=6\pi^2\,\mathrm{Hz}$ and $T=\dfrac{1}{6\pi^2}\,\mathrm{s}$
  feedback: |-
    Multiplying by $2\pi$ converts revolutions to radians, but this problem starts with radians and must convert back to revolutions. Use the reciprocal conversion factor $1\,\mathrm{rev}/(2\pi\,\mathrm{rad})$, so $f=1.50\,\mathrm{Hz}$.
- id: mct-p3-omega-reverse-d
  content: |-
    $f=1.50\,\mathrm{Hz}$ and $T=1.50\,\mathrm{s}$
  feedback: |-
    The frequency is correct, but period and frequency are reciprocal rates, not equal values with different units. Since $1.50$ revolutions occur each second, one revolution takes $1/1.50=0.667\,\mathrm{s}$.
- id: mct-p3-omega-reverse-e
  content: |-
    $f=0.667\,\mathrm{Hz}$ and $T=1.50\,\mathrm{s}$
  feedback: |-
    These numerical values have been assigned to the wrong quantities. The result $1.50$ has units of revolutions per second and is therefore $f$; its reciprocal $0.667\,\mathrm{s/rev}$ is $T$.
```

### Source-video bridge to linear speed

A wheel of radius $1.4\,\mathrm{m}$ rotates at $45\,\mathrm{rpm}$. The source video asks for the rim's linear speed in miles per hour. This is the one place in the lesson where radius is relevant: $v=r\omega$ converts an angular rate into a tangential rate.

Following the video's unit-cancellation path,

$$
\begin{aligned}
v={}&45\,\frac{\mathrm{rev}}{\mathrm{min}}
\left(\frac{60\,\mathrm{min}}{1\,\mathrm{h}}\right)
\left(\frac{2\pi\,\mathrm{rad}}{1\,\mathrm{rev}}\right)
\left(1.4\,\frac{\mathrm{m}}{\mathrm{rad}}\right) \\
&\times
\left(\frac{1\,\mathrm{km}}{1000\,\mathrm{m}}\right)
\left(\frac{0.6214\,\mathrm{mi}}{1\,\mathrm{km}}\right) \\
\approx{}&14.76\,\mathrm{mi/h}.
\end{aligned}
$$

Here $1.4\,\mathrm{m/rad}$ is a unit-tracking conversion factor supplied by $s=r\theta$; the radius itself is conventionally the length $1.4\,\mathrm{m}$, and radians are dimensionless. Convert RPM using $60$ and $2\pi$, then apply the additional relationship $v=r\omega$.

```quiz
type: radio
id: mct-p3-rpm-to-linear-speed
content: |-
  A wheel of radius $0.50\,\mathrm{m}$ rotates at $120\,\mathrm{rpm}$. What is the tangential speed of its rim in meters per second?
options:
- id: mct-p3-rpm-to-linear-speed-a
  content: |-
    $2\pi\,\mathrm{m/s}\approx6.28\,\mathrm{m/s}$
  correct: true
  feedback: |-
    Convert the rate first: $120\,\mathrm{rev/min}=2.00\,\mathrm{rev/s}=4\pi\,\mathrm{rad/s}$. Then $v=r\omega=(0.50)(4\pi)=2\pi\,\mathrm{m/s}$.
- id: mct-p3-rpm-to-linear-speed-b
  content: |-
    $4\pi\,\mathrm{m/s}\approx12.6\,\mathrm{m/s}$
  feedback: |-
    This is twice the correct value because it uses the $1.0\,\mathrm{m}$ diameter as though it were the radius. The tangential relation is $v=r\omega$, so use the stated radius $0.50\,\mathrm{m}$.
- id: mct-p3-rpm-to-linear-speed-c
  content: |-
    $2.0\,\mathrm{m/s}$
  feedback: |-
    The value $120/60=2.0$ is the frequency in revolutions per second, not a linear speed. Each revolution contains $2\pi$ radians, and the angular rate must then be multiplied by the radius.
- id: mct-p3-rpm-to-linear-speed-d
  content: |-
    $60\,\mathrm{m/s}$
  feedback: |-
    Multiplying $120$ by $0.50$ leaves the original time unit as minutes and treats revolutions as radians. Convert RPM to radians per second before applying $v=r\omega$.
- id: mct-p3-rpm-to-linear-speed-e
  content: |-
    $\dfrac{\pi}{30}\,\mathrm{m/s}\approx0.105\,\mathrm{m/s}$
  feedback: |-
    This divides by $60$ twice. The single conversion $120\,\mathrm{rev/min}\times(1\,\mathrm{min}/60\,\mathrm{s})$ already gives $2.0\,\mathrm{rev/s}$; then multiply by $2\pi\,\mathrm{rad/rev}$ and the radius.
```

---

<a id="summary"></a>
## Summary

Use the words and units to identify the quantity before choosing an equation:

1. For $N$ cycles in time $t$, use $f=N/t$ for cycles per time and $T=t/N$ for time per cycle.
2. Use $T=1/f$ only after keeping those two unit ratios straight.
3. Convert cycles to radians with $1\,\mathrm{rev}=2\pi\,\mathrm{rad}$, giving $\omega=2\pi f=2\pi/T$.
4. Convert RPM to hertz by dividing by $60$; multiply hertz by $60$ to return to RPM.
5. From angular speed, divide by $2\pi$ for frequency or use $T=2\pi/\omega$ for period.

Check that $fT=1$ and that the final units match the requested quantity. The main traps are swapping period with frequency, treating revolutions as radians, and moving the factors $60$ or $2\pi$ in the wrong direction. Let unit cancellation decide the direction.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
