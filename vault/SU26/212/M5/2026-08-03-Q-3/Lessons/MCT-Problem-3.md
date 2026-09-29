# Infer and Scale a Mass–Spring Frequency

<!--
lesson-id: 212-M5-061
topic-code: MTH212.M5.61
-->

## Table of Contents

- [Introduction](#introduction)
- [Source-Video Worked Problem: Infer the Spring Constant First](#source-static-spring)
- [Source-Video Worked Problem: Separate the Calibration Load from the Moving Mass](#source-car)
- [Source-Video Worked Problem: Change the Mass on the Same Spring](#source-mass-scaling)
- [Source-Video Worked Problem: Change the Spring for the Same Mass](#source-spring-scaling)
- [Lecture Graph and Source-Video Cycle Accounting](#graph-and-cycles)
- [Summary](#summary)

## Prerequisites

- Use Hooke's-law magnitudes in a static measurement: $F=kx$.
- Convert centimeters and grams to meters and kilograms.
- Evaluate square roots and expressions containing $2\pi$.
- Read the period as the time between equivalent points in consecutive cycles.
- Distinguish displacement from total distance traveled.

---

<a id="introduction"></a>
## Introduction

For an ideal mass–spring oscillator,

$$
\boxed{f=\frac{1}{2\pi}\sqrt{\frac{k}{m}}},
\qquad
\boxed{T=\frac1f=2\pi\sqrt{\frac{m}{k}}}.
$$

Use the full formula when $k$ and the moving mass $m$ are known. If a static force $F$ produces an extension or compression $x$, first infer

$$
k=\frac{F}{x}.
$$

For a before-and-after comparison, divide the two frequency equations:

$$
\boxed{
\frac{f_2}{f_1}
=\sqrt{\frac{k_2/m_2}{k_1/m_1}}
=\sqrt{\frac{k_2m_1}{k_1m_2}}
}.
$$

The same comparison can be written as two visible scale factors:

$$
\boxed{f_2=f_1\sqrt{\frac{k_2}{k_1}}\sqrt{\frac{m_1}{m_2}}}.
$$

This form keeps the direct stiffness effect and inverse mass effect separate. Each ratio is dimensionless, and the subscripts keep every new value paired with state 2.

Cross out what stays fixed before inserting numbers:

| Fixed quantity | Frequency comparison |
|---|---|
| same spring, so $k_2=k_1$ | $\displaystyle \frac{f_2}{f_1}=\sqrt{\frac{m_1}{m_2}}$ |
| same mass, so $m_2=m_1$ | $\displaystyle \frac{f_2}{f_1}=\sqrt{\frac{k_2}{k_1}}$ |

Frequency is not linearly proportional to stiffness or inversely proportional to mass. The square root makes a fourfold change in $k$ or $m$ produce only a twofold change in $f$.

For a vertical spring, gravity fixes the equilibrium position. Once displacement is measured from that equilibrium, the spring force supplies the restoring term and the frequency remains $(2\pi)^{-1}\sqrt{k/m}$; do not insert $mg$ as an additional restoring force.

---

<a id="source-static-spring"></a>
## Source-Video Worked Problem: Infer the Spring Constant First

The problem in `iubb3eFBQ9U` at 1:09:22-1:12:06 uses a $0.25\,\mathrm{kg}$ block. A static applied force of $200\,\mathrm N$ stretches the spring $0.25\,\mathrm m$.

The static data determine the spring constant:

$$
k=\frac{F}{x}
=\frac{200\,\mathrm N}{0.25\,\mathrm m}
=800\,\mathrm{N/m}.
$$

Now use the block's mass in the frequency equation:

$$
\begin{aligned}
f
&=\frac{1}{2\pi}\sqrt{\frac{k}{m}}\\
&=\frac{1}{2\pi}\sqrt{\frac{800}{0.25}}\\
&=9.003\ldots\,\mathrm{Hz}\\
&\approx\boxed{9.0\,\mathrm{Hz}}.
\end{aligned}
$$

The period is the reciprocal:

$$
T=\frac1f
=0.111\ldots\,\mathrm s
\approx\boxed{0.111\,\mathrm s}.
$$

Thus the block completes about nine cycles each second, and each cycle takes about $0.111\,\mathrm s$.

**Caption correction.** The automatic captions drop the decimal point and render the period as roughly $1$ or $111$ seconds. The calculation and the stated $9\,\mathrm{Hz}$ frequency require $T\approx0.111\,\mathrm s$.

```quiz
type: radio
id: mct-p3-static-inference
shuffle: true
content: |-
  A $96\,\mathrm N$ static force stretches a spring $0.12\,\mathrm m$. A $0.32\,\mathrm{kg}$ block then oscillates on that spring. What is the frequency, to two significant figures?
options:
- id: mct-p3-static-inference-a
  content: |-
    $8.0\,\mathrm{Hz}$
  correct: true
  feedback: |-
    The static data give $k=F/x=96/0.12=800\,\mathrm{N/m}$. With the moving mass $m=0.32\,\mathrm{kg}$, $f=(2\pi)^{-1}\sqrt{800/0.32}=7.96\,\mathrm{Hz}$, which rounds to $8.0\,\mathrm{Hz}$.
- id: mct-p3-static-inference-b
  content: |-
    $50\,\mathrm{Hz}$
  feedback: |-
    This is $\sqrt{k/m}$, which is the angular frequency in radians per second. Ordinary frequency requires division by $2\pi$, giving $8.0\,\mathrm{Hz}$.
- id: mct-p3-static-inference-c
  content: |-
    $4.0\times10^2\,\mathrm{Hz}$
  feedback: |-
    This divides $k/m$ by $2\pi$ without taking the square root. The mass–spring frequency depends on $\sqrt{k/m}$, not directly on $k/m$.
- id: mct-p3-static-inference-d
  content: |-
    $0.96\,\mathrm{Hz}$
  feedback: |-
    This uses $Fx$ instead of $F/x$ for the spring constant. Hooke's-law magnitudes give $k=F/x=800\,\mathrm{N/m}$; $Fx$ has energy units and is not a stiffness.
- id: mct-p3-static-inference-e
  content: |-
    $0.13\,\mathrm{Hz}$
  feedback: |-
    The number $0.13$ comes from taking the reciprocal of $7.96\,\mathrm{Hz}$. That reciprocal is the period and must carry seconds; the requested frequency is about $8.0$ cycles per second.
```

---

<a id="source-car"></a>
## Source-Video Worked Problem: Separate the Calibration Load from the Moving Mass

The problem in `iubb3eFBQ9U` at 1:12:20-1:14:45 says that a $70\,\mathrm{kg}$ person adds $2\,\mathrm{cm}$ of compression to a $1200\,\mathrm{kg}$ car's springs. The car and person then vibrate together after the car hits a bump.

Two different masses have two different jobs:

| Stage | Mass to use | Reason |
|---|---:|---|
| infer $k$ from the **additional** $2\,\mathrm{cm}$ compression | $70\,\mathrm{kg}$ | the person's added weight caused the measured change |
| find the vibration frequency | $1200+70=1270\,\mathrm{kg}$ | the car and person move together |

Convert the added compression and infer the combined stiffness of the car's springs:

$$
x=2\,\mathrm{cm}=0.020\,\mathrm m,
$$

$$
k=\frac{m_pg}{x}
=\frac{(70)(9.8)}{0.020}
=\boxed{34{,}300\,\mathrm{N/m}}.
$$

Then use the total moving mass:

$$
\begin{aligned}
f
&=\frac1{2\pi}\sqrt{\frac{34{,}300}{1270}}\\
&=0.827\ldots\,\mathrm{Hz}\\
&\approx\boxed{0.83\,\mathrm{Hz}}.
\end{aligned}
$$

At the new static equilibrium, the person's added weight is balanced by the added spring force:

$$
m_pg=k\,\Delta x.
$$

That is why the $70\,\mathrm{kg}$ load and the additional $0.020\,\mathrm m$ compression determine $k$. After the bump, gravity does not become an extra oscillating restoring force; it has already shifted the equilibrium position.

```quiz
type: radio
id: mct-p3-car-mass-roles
shuffle: true
content: |-
  An $80\,\mathrm{kg}$ passenger adds $2.5\,\mathrm{cm}$ of compression to the springs of a $950\,\mathrm{kg}$ car. If the passenger remains in the car when it bounces, what is the vibration frequency? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p3-car-mass-roles-a
  content: |-
    $0.88\,\mathrm{Hz}$
  correct: true
  feedback: |-
    The added load gives $k=(80)(9.8)/0.025=31{,}360\,\mathrm{N/m}$. The moving mass is $950+80=1030\,\mathrm{kg}$, so $f=(2\pi)^{-1}\sqrt{31{,}360/1030}=0.878\,\mathrm{Hz}$, or $0.88\,\mathrm{Hz}$.
- id: mct-p3-car-mass-roles-b
  content: |-
    $3.15\,\mathrm{Hz}$
  feedback: |-
    This uses only the passenger as the moving mass. The passenger's weight calibrates $k$, but the car and passenger bounce together, so the frequency denominator must contain $1030\,\mathrm{kg}$.
- id: mct-p3-car-mass-roles-c
  content: |-
    $0.91\,\mathrm{Hz}$
  feedback: |-
    This uses only the car's $950\,\mathrm{kg}$ in the frequency calculation. The passenger remains aboard and moves with the car, so the oscillating mass is $1030\,\mathrm{kg}$.
- id: mct-p3-car-mass-roles-d
  content: |-
    $0.28\,\mathrm{Hz}$
  feedback: |-
    This treats $2.5\,\mathrm{cm}$ as $0.25\,\mathrm m$. Dividing centimeters by $100$ gives $0.025\,\mathrm m$; the tenfold compression error makes $k$ ten times too small and $f$ smaller by $\sqrt{10}$.
- id: mct-p3-car-mass-roles-e
  content: |-
    $4.85\,\mathrm{Hz}$
  feedback: |-
    This uses $(k/m)/(2\pi)$ instead of $\sqrt{k/m}/(2\pi)$. Frequency has a square-root dependence on the stiffness-to-mass ratio.
```

---

<a id="source-mass-scaling"></a>
## Source-Video Worked Problem: Change the Mass on the Same Spring

The frame-verified insect/web problem in `iubb3eFBQ9U` at 1:14:50-1:20:50 gives an insect mass of $0.25\,\mathrm g$ and frequency $20\,\mathrm{Hz}$. To infer the web's effective spring constant, first convert the mass:

$$
0.25\,\mathrm g=0.25\times10^{-3}\,\mathrm{kg}=2.5\times10^{-4}\,\mathrm{kg}.
$$

Rearrange the frequency equation:

$$
2\pi f=\sqrt{\frac{k}{m}}
\quad\Longrightarrow\quad
\boxed{k=m(2\pi f)^2}.
$$

Therefore,

$$
\begin{aligned}
k
&=(2.5\times10^{-4})[2\pi(20)]^2\\
&=3.9478\ldots\,\mathrm{N/m}\\
&\approx\boxed{3.95\,\mathrm{N/m}}.
\end{aligned}
$$

When a $0.10\,\mathrm g$ insect is caught in the same web, $k$ stays fixed. A ratio avoids recalculating it:

$$
\begin{aligned}
\frac{f_2}{f_1}
&=\sqrt{\frac{m_1}{m_2}},\\
f_2
&=(20)\sqrt{\frac{0.25}{0.10}}\\
&=\boxed{31.6\,\mathrm{Hz}}.
\end{aligned}
$$

Because this is a ratio of masses, both masses may remain in grams; the shared unit cancels. Kilograms are required in the absolute calculation of $k$.

**Source corrections.** The captions garble both the gram conversion and the second insect mass. Use $1\,\mathrm g=10^{-3}\,\mathrm{kg}$ and the frame-verified $0.10\,\mathrm g$. When isolating $k$, square the entire product $2\pi f$: $k=m(2\pi f)^2$, not $m(2\pi)f^2$ or $m(2\pi f^2)$.

```quiz
type: radio
id: mct-p3-same-spring-mass
shuffle: true
content: |-
  An $0.18\,\mathrm g$ insect makes a web vibrate at $18\,\mathrm{Hz}$. What frequency would an $0.080\,\mathrm g$ insect produce on the same web?
options:
- id: mct-p3-same-spring-mass-a
  content: |-
    $27\,\mathrm{Hz}$
  correct: true
  feedback: |-
    The same web means $k$ is fixed, so $f_2=f_1\sqrt{m_1/m_2}=18\sqrt{0.18/0.080}=27\,\mathrm{Hz}$. The smaller mass produces the higher frequency.
- id: mct-p3-same-spring-mass-b
  content: |-
    $40.5\,\mathrm{Hz}$
  feedback: |-
    This applies a linear inverse-mass factor, $18(0.18/0.080)$. Frequency varies with the inverse square root of mass, so take the square root of the mass ratio.
- id: mct-p3-same-spring-mass-c
  content: |-
    $12\,\mathrm{Hz}$
  feedback: |-
    This uses the square-root mass ratio in the wrong direction. A smaller mass has less inertia and must produce a frequency above $18\,\mathrm{Hz}$, not below it.
- id: mct-p3-same-spring-mass-d
  content: |-
    $8.0\,\mathrm{Hz}$
  feedback: |-
    This scales frequency directly with mass. For a fixed spring, frequency is proportional to $1/\sqrt m$, so reducing mass raises the frequency.
- id: mct-p3-same-spring-mass-e
  content: |-
    $18\,\mathrm{Hz}$
  feedback: |-
    The spring is unchanged, but the moving mass is not. Frequency would remain $18\,\mathrm{Hz}$ only if both $k$ and $m$ stayed fixed.
```

---

<a id="source-spring-scaling"></a>
## Source-Video Worked Problem: Change the Spring for the Same Mass

The problem in `iubb3eFBQ9U` at 1:20:55-1:22:40 keeps the block fixed. With $k_1=200\,\mathrm{N/m}$, its frequency is $f_1=15\,\mathrm{Hz}$. The block is moved to a spring with $k_2=500\,\mathrm{N/m}$.

The mass cancels from the comparison:

$$
\frac{f_2}{f_1}=\sqrt{\frac{k_2}{k_1}}.
$$

Hence

$$
\begin{aligned}
f_2
&=15\sqrt{\frac{500}{200}}\\
&=23.717\ldots\,\mathrm{Hz}\\
&\approx\boxed{23.7\,\mathrm{Hz}}.
\end{aligned}
$$

The stiffer spring produces a higher frequency, but increasing $k$ by a factor of $2.5$ increases $f$ only by $\sqrt{2.5}\approx1.58$.

**Source correction.** The narration briefly says that increasing $k$ increases the force, then corrects the requested quantity to frequency. For the same displacement, a larger $k$ does increase the spring-force magnitude, but this comparison asks how the oscillator's **frequency** changes.

```quiz
type: radio
id: mct-p3-same-mass-spring
shuffle: true
content: |-
  A block vibrates at $12\,\mathrm{Hz}$ on a $200\,\mathrm{N/m}$ spring. What is its frequency on a $450\,\mathrm{N/m}$ spring?
options:
- id: mct-p3-same-mass-spring-a
  content: |-
    $18\,\mathrm{Hz}$
  correct: true
  feedback: |-
    The same block means the mass cancels. Thus $f_2=12\sqrt{450/200}=12(1.5)=18\,\mathrm{Hz}$.
- id: mct-p3-same-mass-spring-b
  content: |-
    $27\,\mathrm{Hz}$
  feedback: |-
    This uses the linear stiffness factor $450/200=2.25$. Frequency scales with $\sqrt{k}$, so the frequency factor is $\sqrt{2.25}=1.5$.
- id: mct-p3-same-mass-spring-c
  content: |-
    $8.0\,\mathrm{Hz}$
  feedback: |-
    This reverses the square-root stiffness ratio. The second spring is stiffer, so the second frequency must be greater than $12\,\mathrm{Hz}$.
- id: mct-p3-same-mass-spring-d
  content: |-
    $5.3\,\mathrm{Hz}$
  feedback: |-
    This divides by the full stiffness factor. A stiffer spring raises frequency, and the dependence is a square root rather than a linear inverse relation.
- id: mct-p3-same-mass-spring-e
  content: |-
    $12\,\mathrm{Hz}$
  feedback: |-
    The mass stays fixed, but the stiffness changes. Frequency remains unchanged only when the ratio $k/m$ remains unchanged.
```

---

<a id="graph-and-cycles"></a>
## Lecture Graph and Source-Video Cycle Accounting

### Lecture graph: translate one period into frequency

The M4-1 lecture graph has

$$
A=2.5\,\mathrm{cm},
\qquad
T=4.0\,\mathrm s.
$$

The period is the shortest positive time over which the motion repeats. On a graph, measure between equivalent states such as one crest and the next crest; crest to trough is only half a period.

Frequency and angular frequency follow from the period:

$$
f=\frac1T=\boxed{0.25\,\mathrm{Hz}},
$$

$$
\omega=2\pi f
=\boxed{\frac\pi2\,\mathrm{rad/s}}
\approx1.57\,\mathrm{rad/s}.
$$

The maximum speed is

$$
v_{\max}=\omega A
=\left(\frac\pi2\right)(2.5\,\mathrm{cm})
\approx\boxed{3.9\,\mathrm{cm/s}}.
$$

Amplitude does not enter the ideal mass–spring frequency formula. It enters the maximum-speed calculation after $f$ or $\omega$ has been found.

### Source-video capstone: convert periods to path length

The final assigned problem in `iubb3eFBQ9U` at 1:22:55-1:24:23 gives amplitude $A=0.40\,\mathrm m$ and asks for total distance traveled in eight periods.

During one complete cycle, the block travels from one turning point to the other and back. That path contains four amplitude-length segments:

$$
d_{\text{one cycle}}=4A.
$$

Therefore,

$$
\begin{aligned}
d_{8\text{ cycles}}
&=8(4A)\\
&=8(4)(0.40\,\mathrm m)\\
&=\boxed{12.8\,\mathrm m}.
\end{aligned}
$$

This is total distance, not displacement. After eight complete periods the block returns to its starting position, so its net displacement is zero even though it has traveled $12.8\,\mathrm m$.

```quiz
type: radio
id: mct-p3-cycle-distance
shuffle: true
content: |-
  A mass–spring oscillator has amplitude $0.18\,\mathrm m$. What total distance does it travel in six complete periods?
options:
- id: mct-p3-cycle-distance-a
  content: |-
    $4.32\,\mathrm m$
  correct: true
  feedback: |-
    One complete cycle contains four amplitude-length segments, so $d=N(4A)=6(4)(0.18)=4.32\,\mathrm m$.
- id: mct-p3-cycle-distance-b
  content: |-
    $1.08\,\mathrm m$
  feedback: |-
    This counts one amplitude per cycle. A full cycle goes from the starting turning point to the opposite turning point and back, totaling $4A$ per cycle.
- id: mct-p3-cycle-distance-c
  content: |-
    $2.16\,\mathrm m$
  feedback: |-
    This counts $2A$ per cycle, which reaches the opposite turning point but does not return to the starting state. A complete period covers $4A$.
- id: mct-p3-cycle-distance-d
  content: |-
    $0.72\,\mathrm m$
  feedback: |-
    $4A=0.72\,\mathrm m$ is the distance in one period. The prompt asks for six complete periods, so multiply by six.
- id: mct-p3-cycle-distance-e
  content: |-
    $0\,\mathrm m$
  feedback: |-
    The displacement after six full periods is zero because the mass returns to its starting position. Total distance adds every part of the path and is $4.32\,\mathrm m$.
```

---

<a id="summary"></a>
## Summary

- For an ideal mass–spring oscillator,
  $$
  f=\frac1{2\pi}\sqrt{\frac{k}{m}},
  \qquad
  T=\frac1f.
  $$
- If static force/displacement data are supplied, first infer $k=F/x$ using compatible units.
- In a load-calibration problem, use the load responsible for the **change** in compression to infer $k$, then use every mass that moves in the oscillation.
- For the same spring,
  $$
  f_2=f_1\sqrt{\frac{m_1}{m_2}}.
  $$
  Less mass means higher frequency.
- For the same mass,
  $$
  f_2=f_1\sqrt{\frac{k_2}{k_1}}.
  $$
  Greater stiffness means higher frequency.
- Use kilograms in absolute formulas. A ratio may retain grams when the same mass unit appears in numerator and denominator.
- For vertical oscillation, gravity shifts equilibrium; it is not an extra restoring term after displacement is measured from equilibrium.
- Read $T$ between equivalent points in successive cycles. Then $f=1/T$ and $\omega=2\pi f$.
- One full cycle covers distance $4A$. After an integer number of cycles, net displacement is zero but total distance is not.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
