# Solve a Simple-Pendulum Target from Period Data

<!--
lesson-id: 212-M5-063
topic-code: MTH212.M5.63
-->

## Table of Contents

- [Introduction](#introduction)
- [Translate Timing Data into Period and Frequency](#timing-data)
- [Source-Video Problem 1: Period on Earth and the Moon](#source-earth-moon)
- [Source-Video Problem 2: Find Length from a Cycle Count](#source-length)
- [Source-Video Problem 3: Find an Unknown Gravitational Field](#source-gravity)
- [Source-Video Problem 4: Read a Clock's Half-Cycle Timing](#source-clock)
- [Source-Video Problem 5: Compare the Same Pendulum on Two Planets](#source-comparison)
- [Source-Video Problem 6 and Lecture Transfer: Why Mass Cancels](#source-mass)
- [Summary](#summary)

## Prerequisites

- Interpret frequency as cycles per second and period as seconds per cycle.
- Rearrange an equation for one requested variable.
- Square both sides of an equation containing a square root.
- Evaluate ratios and square roots with a calculator.
- Use SI units: meters, seconds, and meters per second squared.

---

<a id="introduction"></a>
## Introduction

A **point-like bob**, a **light string**, and a **small release angle** signal the simple-pendulum model

$$
T=2\pi\sqrt{\frac{L}{g}}.
$$

Here $T$ is the time for one complete oscillation, $L$ is the pivot-to-bob length, and $g$ is the local gravitational-field magnitude. The model neglects friction and assumes the angle is small enough that $\sin\theta\approx\theta$ when $\theta$ is measured in radians.

Use one move throughout this lesson:

1. Translate the timing information into $T$ or $f$.
2. Rearrange the pendulum formula for the requested variable.
3. Substitute, then check the direction of the result.

The bob's mass is deliberately absent. Large-angle corrections and the moments of inertia of physical pendulums are different topics and are not used here.

---

<a id="timing-data"></a>
## Translate Timing Data into Period and Frequency

If $N$ **complete oscillations** take a total time $\Delta t$, divide in the order set by the units:

$$
\boxed{T=\frac{\Delta t}{N}}
\qquad\text{and}\qquad
\boxed{f=\frac{N}{\Delta t}=\frac{1}{T}}.
$$

Period has units of seconds per cycle. Frequency has units of cycles per second, or hertz. One complete oscillation returns the bob to the same position while moving in the same direction; motion from one extreme to the other is only half an oscillation.

The opening source segment (`1Q15fgz-lUk`, 00:00:00–00:05:14) uses the trip from one extreme to the other and back again as one cycle. That convention controls every later calculation.

```quiz
type: radio
id: mct-p5-period-frequency
shuffle: true
content: |-
  A pendulum completes $36$ full oscillations in $54.0\ \mathrm s$. What are its period and frequency?
options:
- id: mct-p5-period-frequency-a
  content: |-
    $T=0.667\ \mathrm s$ and $f=1.50\ \mathrm{Hz}$
  feedback: |-
    These two rates are reversed. Seconds per cycle is $54.0/36=1.50\ \mathrm s$, while cycles per second is $36/54.0=0.667\ \mathrm{Hz}$.
- id: mct-p5-period-frequency-b
  content: |-
    $T=1.50\ \mathrm s$ and $f=0.667\ \mathrm{Hz}$
  correct: true
  feedback: |-
    Divide total time by cycles for period: $T=54.0/36=1.50\ \mathrm s$. Its reciprocal is $f=36/54.0=0.667\ \mathrm{Hz}$.
- id: mct-p5-period-frequency-c
  content: |-
    $T=54.0\ \mathrm s$ and $f=36\ \mathrm{Hz}$
  feedback: |-
    These are the totals, not per-cycle rates. Divide one total by the other so the units become seconds per cycle or cycles per second.
- id: mct-p5-period-frequency-d
  content: |-
    $T=1.50\ \mathrm s$ and $f=1.50\ \mathrm{Hz}$
  feedback: |-
    Period and frequency are reciprocals, not generally equal. With $T=1.50\ \mathrm s$, $f=1/T=0.667\ \mathrm{Hz}$.
- id: mct-p5-period-frequency-e
  content: |-
    $T=0.0278\ \mathrm s$ and $f=36.0\ \mathrm{Hz}$
  feedback: |-
    The value $1/36$ ignores the measured $54.0\ \mathrm s$. Use both totals: $T=\Delta t/N$ and $f=N/\Delta t$.
```

---

<a id="source-earth-moon"></a>
## Source-Video Problem 1: Period on Earth and the Moon

The first numerical source problem (`1Q15fgz-lUk`, 00:05:15–00:10:14) uses the same $0.70\ \mathrm m$ pendulum in two gravitational fields.

On Earth, with $g=9.8\ \mathrm{m/s^2}$,

$$
T_E=2\pi\sqrt{\frac{0.70}{9.8}}
=1.679\ldots\ \mathrm s
\approx\boxed{1.68\ \mathrm s},
$$

$$
f_E=\frac{1}{T_E}=0.5955\ldots\ \mathrm{Hz}
\approx\boxed{0.60\ \mathrm{Hz}}.
$$

On the Moon, with $g=1.6\ \mathrm{m/s^2}$,

$$
T_M=2\pi\sqrt{\frac{0.70}{1.6}}
=4.1559\ldots\ \mathrm s
\approx\boxed{4.16\ \mathrm s},
$$

$$
f_M=\frac{1}{T_M}=0.2406\ldots\ \mathrm{Hz}
\approx\boxed{0.24\ \mathrm{Hz}}.
$$

The smaller lunar $g$ produces a longer period and a lower frequency. More precisely, at fixed length,

$$
T\propto g^{-1/2},
$$

so period is **inverse-square-root** in $g$, not proportional to $1/g$. Calling the relationship merely “inverse” gets the direction right but misses the exponent.

```quiz
type: radio
id: mct-p5-known-length
shuffle: true
content: |-
  A small-angle simple pendulum has $L=1.20\ \mathrm m$ where $g=9.80\ \mathrm{m/s^2}$. What are its period and frequency?
options:
- id: mct-p5-known-length-a
  content: |-
    $T=0.455\ \mathrm s$ and $f=2.20\ \mathrm{Hz}$
  feedback: |-
    This swaps period and frequency. The formula $2\pi\sqrt{L/g}$ gives $T=2.20\ \mathrm s$; its reciprocal is $0.455\ \mathrm{Hz}$.
- id: mct-p5-known-length-b
  content: |-
    $T=17.95\ \mathrm s$ and $f=0.0557\ \mathrm{Hz}$
  feedback: |-
    This effectively uses $2\pi\sqrt{g/L}$ for period. Length belongs over gravity in $T=2\pi\sqrt{L/g}$.
- id: mct-p5-known-length-c
  content: |-
    $T=0.350\ \mathrm s$ and $f=2.86\ \mathrm{Hz}$
  feedback: |-
    This takes $\sqrt{L/g}$ but omits the factor $2\pi$. One full oscillation takes $2\pi\sqrt{L/g}$.
- id: mct-p5-known-length-d
  content: |-
    $T=2.20\ \mathrm s$ and $f=0.455\ \mathrm{Hz}$
  correct: true
  feedback: |-
    $T=2\pi\sqrt{1.20/9.80}=2.1987\ldots\ \mathrm s$, and $f=1/T=0.4548\ldots\ \mathrm{Hz}$.
- id: mct-p5-known-length-e
  content: |-
    $T=0.769\ \mathrm s$ and $f=1.30\ \mathrm{Hz}$
  feedback: |-
    This uses $2\pi L/g$ without taking the square root of $L/g$. Keep the entire ratio under the radical.
```

---

<a id="source-length"></a>
## Source-Video Problem 2: Find Length from a Cycle Count

The next source problem (`1Q15fgz-lUk`, 00:10:16–00:15:04) records $42$ complete oscillations in $63\ \mathrm s$ on Earth. Translate the count first:

$$
T=\frac{63\ \mathrm s}{42}=1.50\ \mathrm s,
\qquad
f=\frac{42}{63\ \mathrm s}=0.667\ \mathrm{Hz}.
$$

Then isolate $L$ before entering numbers:

$$
\begin{aligned}
T&=2\pi\sqrt{\frac{L}{g}},\\
\frac{T}{2\pi}&=\sqrt{\frac{L}{g}},\\
\left(\frac{T}{2\pi}\right)^2&=\frac{L}{g},\\
\boxed{L=\frac{gT^2}{4\pi^2}}.
\end{aligned}
$$

Because $T$, $L$, and $g$ are nonnegative physical quantities, squaring the isolated principal square root does not create a separate negative branch.

Using $g=9.8\ \mathrm{m/s^2}$,

$$
L=\frac{(9.8)(1.50)^2}{4\pi^2}
=0.5585\ldots\ \mathrm m
\approx\boxed{0.559\ \mathrm m}.
$$

Parentheses matter on a calculator: the entire $4\pi^2$ is the denominator.

```quiz
type: radio
id: mct-p5-find-length
shuffle: true
content: |-
  On Earth, a small-angle pendulum completes $25$ oscillations in $45.0\ \mathrm s$. What is its length?
options:
- id: mct-p5-find-length-a
  content: |-
    $0.804\ \mathrm m$
  correct: true
  feedback: |-
    First $T=45.0/25=1.80\ \mathrm s$. Then $L=gT^2/(4\pi^2)=(9.80)(1.80)^2/(4\pi^2)=0.804\ \mathrm m$.
- id: mct-p5-find-length-b
  content: |-
    $7.94\ \mathrm m$
  feedback: |-
    This divides by $4$ but omits $\pi^2$. Squaring $T/(2\pi)$ squares both $2$ and $\pi$, producing the full denominator $4\pi^2$.
- id: mct-p5-find-length-c
  content: |-
    $0.0766\ \mathrm m$
  feedback: |-
    This substitutes the frequency $25/45.0=0.5556\ \mathrm{Hz}$ where the length formula requires period. Use $T=45.0/25=1.80\ \mathrm s$.
- id: mct-p5-find-length-d
  content: |-
    $31.8\ \mathrm m$
  feedback: |-
    This omits the denominator $4\pi^2$. The isolated formula is $L=gT^2/(4\pi^2)$.
- id: mct-p5-find-length-e
  content: |-
    $0.447\ \mathrm m$
  feedback: |-
    This leaves the period unsquared. Once the square root is isolated, square both sides, so length depends on $T^2$.
```

---

<a id="source-gravity"></a>
## Source-Video Problem 3: Find an Unknown Gravitational Field

In the third source problem (`1Q15fgz-lUk`, 00:15:05–00:19:07), a pendulum of length $0.80\ \mathrm m$ completes $28$ oscillations in $45\ \mathrm s$. Its period is

$$
T=\frac{45\ \mathrm s}{28}=1.6071\ldots\ \mathrm s.
$$

Starting from the length form,

$$
L=\frac{gT^2}{4\pi^2},
$$

isolate $g$:

$$
\boxed{g=\frac{4\pi^2L}{T^2}}.
$$

Therefore,

$$
g=\frac{4\pi^2(0.80\ \mathrm m)}{(1.6071\ldots\ \mathrm s)^2}
=12.227\ldots\ \mathrm{m/s^2}
\approx\boxed{12.2\ \mathrm{m/s^2}}.
$$

The source obtains $1.24g_E$ by dividing its rounded $12.2\ \mathrm{m/s^2}$ by $9.8\ \mathrm{m/s^2}$. Retaining the unrounded value gives $1.2477\ldots g_E\approx1.25g_E$. Either way, the field is about $24$–$25\%$ stronger than Earth's. The source phrase “$1.24$ times greater” should be read as **$1.24$ times as large**, not $124\%$ greater.

```quiz
type: radio
id: mct-p5-find-gravity
shuffle: true
content: |-
  A $0.650\ \mathrm m$ simple pendulum completes $15$ full oscillations in $36.0\ \mathrm s$ on an unknown moon. What is the local gravitational-field magnitude?
options:
- id: mct-p5-find-gravity-a
  content: |-
    $0.0948\ \mathrm{m/s^2}$
  feedback: |-
    This places $4\pi^2$ in the denominator. Isolating gravity gives $g=4\pi^2L/T^2$, with $4\pi^2$ in the numerator.
- id: mct-p5-find-gravity-b
  content: |-
    $148\ \mathrm{m/s^2}$
  feedback: |-
    This uses frequency, $15/36.0$, in the place of period. The period is time per cycle: $T=36.0/15=2.40\ \mathrm s$.
- id: mct-p5-find-gravity-c
  content: |-
    $25.7\ \mathrm{m/s^2}$
  feedback: |-
    This omits the period denominator entirely. The isolated formula is $g=4\pi^2L/T^2$, so divide by $(2.40\ \mathrm s)^2$.
- id: mct-p5-find-gravity-d
  content: |-
    $10.7\ \mathrm{m/s^2}$
  feedback: |-
    This uses $T=36.0/15$ but leaves that period unsquared. In $g=4\pi^2L/T^2$, divide by the square of the full $2.40\ \mathrm s$ period.
- id: mct-p5-find-gravity-e
  content: |-
    $4.46\ \mathrm{m/s^2}$
  correct: true
  feedback: |-
    $T=36.0/15=2.40\ \mathrm s$, so $g=4\pi^2(0.650)/(2.40)^2=4.455\ldots\ \mathrm{m/s^2}\approx4.46\ \mathrm{m/s^2}$.
```

---

<a id="source-clock"></a>
## Source-Video Problem 4: Read a Clock's Half-Cycle Timing

The clock problem (`1Q15fgz-lUk`, 00:19:08–00:21:25) says that one second passes from **tick to tock** as the bob moves from one side to the other. That motion is half an oscillation:

$$
\frac{T}{2}=1.0\ \mathrm s
\qquad\Longrightarrow\qquad
T=2.0\ \mathrm s.
$$

On Earth,

$$
L=\frac{gT^2}{4\pi^2}
=\frac{(9.8)(2.0)^2}{4\pi^2}
=0.9929\ldots\ \mathrm m
\approx\boxed{0.993\ \mathrm m}.
$$

Do not automatically treat every reported “swing” as a full cycle. Identify the start and end positions first.

```quiz
type: radio
id: mct-p5-half-cycle-clock
shuffle: true
content: |-
  A clock pendulum takes $0.800\ \mathrm s$ to travel from its left extreme to its right extreme. Assume a small angle and $g=9.80\ \mathrm{m/s^2}$. What is its length?
options:
- id: mct-p5-half-cycle-clock-a
  content: |-
    $0.159\ \mathrm m$
  feedback: |-
    This treats the one-way trip as a full period. Left extreme to right extreme is half a cycle, so the period is $1.60\ \mathrm s$, not $0.800\ \mathrm s$.
- id: mct-p5-half-cycle-clock-b
  content: |-
    $2.54\ \mathrm m$
  feedback: |-
    This doubles the one-way time twice, using $T=3.20\ \mathrm s$. A complete cycle contains two such trips, so $T=1.60\ \mathrm s$.
- id: mct-p5-half-cycle-clock-c
  content: |-
    $1.27\ \mathrm m$
  feedback: |-
    This places $2\pi^2$ rather than $4\pi^2$ in the denominator. The entire factor $2\pi$ is squared when solving for length.
- id: mct-p5-half-cycle-clock-d
  content: |-
    $0.397\ \mathrm m$
  feedback: |-
    This uses $L=gT/(4\pi^2)$ and leaves the period unsquared. Once the square root is isolated, $L$ depends on $T^2$.
- id: mct-p5-half-cycle-clock-e
  content: |-
    $0.635\ \mathrm m$
  correct: true
  feedback: |-
    The one-way time is $T/2$, so $T=2(0.800)=1.60\ \mathrm s$. Then $L=(9.80)(1.60)^2/(4\pi^2)=0.635\ \mathrm m$.
```

---

<a id="source-comparison"></a>
## Source-Video Problem 5: Compare the Same Pendulum on Two Planets

For the same pendulum, $L$ and $2\pi$ do not change. The source comparison (`1Q15fgz-lUk`, 00:21:26–00:25:19) starts with

$$
T_1=1.7\ \mathrm s,
\qquad
g_1=9.8\ \mathrm{m/s^2},
\qquad
g_2=15\ \mathrm{m/s^2}.
$$

Divide the two period equations before substituting:

$$
\frac{T_2}{T_1}
=
\frac{2\pi\sqrt{L/g_2}}{2\pi\sqrt{L/g_1}}
=\sqrt{\frac{g_1}{g_2}}.
$$

Thus

$$
T_2=T_1\sqrt{\frac{g_1}{g_2}}
=(1.7)\sqrt{\frac{9.8}{15}}
=1.374\ldots\ \mathrm s
\approx\boxed{1.37\ \mathrm s}.
$$

This ratio route avoids solving for $L$ when the length is unchanged. The order $g_1/g_2$ also passes a quick check: because $g_2>g_1$, the new period must be shorter.

```quiz
type: radio
id: mct-p5-gravity-comparison
shuffle: true
content: |-
  A pendulum's period is $1.90\ \mathrm s$ where $g_1=9.80\ \mathrm{m/s^2}$. The same-length pendulum is moved to a planet where $g_2=3.70\ \mathrm{m/s^2}$, and its bob is replaced by one with twice the mass. What is the new small-angle period?
options:
- id: mct-p5-gravity-comparison-a
  content: |-
    $1.17\ \mathrm s$
  feedback: |-
    This reverses the gravity ratio. The weaker second field must make the period longer, so use $T_2=T_1\sqrt{g_1/g_2}$.
- id: mct-p5-gravity-comparison-b
  content: |-
    $5.03\ \mathrm s$
  feedback: |-
    This applies the gravity ratio linearly. Period scales with the inverse square root of $g$, so the ratio belongs under a square root.
- id: mct-p5-gravity-comparison-c
  content: |-
    $3.09\ \mathrm s$
  correct: true
  feedback: |-
    Bob mass does not enter the simple-pendulum period. $T_2=(1.90)\sqrt{9.80/3.70}=3.092\ldots\ \mathrm s\approx3.09\ \mathrm s$.
- id: mct-p5-gravity-comparison-d
  content: |-
    $4.37\ \mathrm s$
  feedback: |-
    This incorrectly multiplies the correct gravity-scaled result by $\sqrt2$ for the doubled mass. The bob mass cancels from the simple-pendulum model.
- id: mct-p5-gravity-comparison-e
  content: |-
    $1.90\ \mathrm s$
  feedback: |-
    Changing the bob mass alone would leave the period unchanged, but the gravitational field also changes. A weaker $g$ makes the period longer.
```

---

<a id="source-mass"></a>
## Source-Video Problem 6 and Lecture Transfer: Why Mass Cancels

The final source problem (`1Q15fgz-lUk`, 00:25:21–00:26:24) replaces a bob of mass $m$ with one of mass $2m$ while keeping the same string length and location. Since

$$
T=2\pi\sqrt{\frac{L}{g}}
$$

contains no mass,

$$
\boxed{T_{2m}=T_m}.
$$

The M4-2 lecture supplies the reason. For a point mass on a light string, the gravitational torque at small angle and the moment of inertia about the pivot are

$$
\tau\approx-mgL\theta,
\qquad
I=mL^2.
$$

Using $I\ddot\theta=\tau$ gives

$$
mL^2\ddot\theta=-mgL\theta
\qquad\Longrightarrow\qquad
\ddot\theta=-\frac{g}{L}\theta.
$$

The same $m$ multiplies inertia and gravitational torque, so it cancels. The lecture's $11^\circ$ release is used only to justify the small-angle approximation; within that approximation, the period does not depend on the release angle. For an extended body, do not reuse this point-mass reduction: a physical pendulum requires its moment of inertia and center-of-mass distance instead.

---

<a id="summary"></a>
## Summary

For a small-angle simple pendulum,

$$
\boxed{T=2\pi\sqrt{\frac{L}{g}}},
\qquad
\boxed{f=\frac{1}{T}}.
$$

If $N$ full cycles take time $\Delta t$,

$$
\boxed{T=\frac{\Delta t}{N}},
\qquad
\boxed{f=\frac{N}{\Delta t}}.
$$

The two useful rearrangements are

$$
\boxed{L=\frac{gT^2}{4\pi^2}},
\qquad
\boxed{g=\frac{4\pi^2L}{T^2}}.
$$

For the same length in two gravitational fields,

$$
\boxed{\frac{T_2}{T_1}=\sqrt{\frac{g_1}{g_2}}}.
$$

Before calculating, check three details:

1. Is the reported motion a complete cycle or only a one-way half-cycle?
2. Is the requested quantity $T$, $f$, $L$, or $g$?
3. Does the trend make sense: longer $L$ means longer $T$, while larger $g$ means shorter $T$?

Bob mass is irrelevant to this model because it cancels from the equation of motion. The formula is restricted to a light string, a point-like bob, and a sufficiently small oscillation angle.

<!-- lesson-nav:start -->
---
```update-progress
```
[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]
---
<!-- lesson-nav:end -->
