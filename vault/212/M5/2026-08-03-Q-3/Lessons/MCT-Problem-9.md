# Chain Energy, Power, Area, and Intensity

<!--
lesson-id: 212-M5-067
topic-code: MTH212.M5.67
-->

## Table of Contents

- [Introduction](#introduction)
- [Source-Video Worked Problem: Energy Rate to Lamp Intensity](#source-lamp-chain)
- [Source-Video Worked Problem: Intensity on a Rectangular Receiver](#source-receiver-power)
- [Source-Video Worked Problem: Power over a Month](#source-month-energy)
- [Controlled Variation: Choose Area Before Calculating](#choose-area)
- [Summary](#summary)

## Prerequisites

- Interpret “per second” as division by time.
- Calculate the area of a rectangle and the surface area of a sphere.
- Convert days, hours, and minutes to seconds with conversion factors.
- Rearrange a one-step equation and track compound units.

---

<a id="introduction"></a>
## Introduction

Energy, power, and intensity answer different questions:

| Quantity | Meaning | SI unit |
|---|---|---|
| Energy $E$ | total amount transferred | joule, $\mathrm J$ |
| Power $P$ | energy transferred per time | watt, $\mathrm W=\mathrm{J/s}$ |
| Intensity $I$ | power crossing each unit area | $\mathrm{W/m^2}$ |

The governing chain is

$$
P=\frac{E}{t},
\qquad
I=\frac{P}{A}.
$$

Read the requested unit to decide which direction to move. At each arrow, the denominator names the quantity that must be divided out to form a rate:

$$
E\xleftrightarrow[\,E=Pt\,]{\,P=E/t\,}P
\xleftrightarrow[\,P=IA\,]{\,I=P/A\,}I.
$$

| Requested unit | Operation from the quantity to its left |
|---|---|
| $\mathrm{J/s}=\mathrm W$ | divide energy by time |
| $\mathrm{W/m^2}$ | divide power by area |
| $\mathrm W$ from $\mathrm{W/m^2}$ | multiply intensity by area |
| $\mathrm J$ from $\mathrm{J/s}$ | multiply power by time |

The area is not automatically $4\pi r^2$. Choose it from the physical situation:

| Situation | Area in $I=P/A$ |
|---|---|
| isotropic point source at radius $r$ | entire spherical wavefront, $A=4\pi r^2$ |
| uniform beam incident normally on a flat receiver | illuminated receiver area |

For a tilted receiver, the relevant area would be its projected area perpendicular to the beam. The source receiver in this lesson is presented as fully illuminated, so its stated rectangular area is used directly.

Use this order:

1. Convert an energy transfer over time to power if needed.
2. Identify which surface shares or receives that power.
3. Divide by area to find intensity, or multiply by area to find received power.
4. Multiply power by elapsed time to recover total energy.
5. Cancel units at every step; the remaining unit should match the requested quantity.

---

<a id="source-lamp-chain"></a>
## Source-Video Worked Problem: Energy Rate to Lamp Intensity

The lamp problem in `vEzftaDL7fM` at 0:30:33-0:32:06 states that a lamp emits

$$
E=500\,\mathrm J
$$

every

$$
t=4\,\mathrm s.
$$

### Convert energy per time to power

Power is the energy-transfer rate:

$$
P=\frac{E}{t}
=\frac{500\,\mathrm J}{4\,\mathrm s}
=\boxed{125\,\mathrm W}.
$$

The units show the meaning of the result:

$$
\frac{\mathrm J}{\mathrm s}=\mathrm W.
$$

Thus the lamp transfers $125\,\mathrm J$ each second.

### Spread that power over the spherical wavefront

For the source's isotropic-lamp model, the emitted power is spread uniformly over a sphere. At

$$
r=1.0\,\mathrm m,
$$

the wavefront area is

$$
A=4\pi r^2
=4\pi(1.0\,\mathrm m)^2
=4\pi\,\mathrm{m^2}.
$$

Therefore,

$$
I=\frac{P}{A}
=\frac{125\,\mathrm W}{4\pi\,\mathrm{m^2}}
=\boxed{9.95\,\mathrm{W/m^2}}.
$$

The lamp's $2\,\mathrm m$ and $3\,\mathrm m$ parts belong to the distance-ratio lesson. This lesson uses the $1.0\,\mathrm m$ result only to establish the energy-to-power-to-intensity chain.

```quiz
type: radio
id: mct-p9-lamp-chain
shuffle: true
content: |-
  An isotropic lamp emits $900\,\mathrm J$ in $6.0\,\mathrm s$. What are its power and intensity at $r=1.5\,\mathrm m$?
options:
- id: mct-p9-lamp-chain-a
  content: |-
    $P=150\,\mathrm W$ and $I=5.31\,\mathrm{W/m^2}$
  correct: true
  feedback: |-
    Energy per time gives $P=900/6.0=150\,\mathrm W$. Isotropic spreading uses the spherical area $4\pi(1.5)^2$, so $I=150/[4\pi(1.5)^2]=5.31\,\mathrm{W/m^2}$.
- id: mct-p9-lamp-chain-b
  content: |-
    $P=5400\,\mathrm W$ and $I=191\,\mathrm{W/m^2}$
  feedback: |-
    Multiplying energy by time does not produce an energy rate. Power is energy divided by elapsed time, so begin with $900\,\mathrm J/6.0\,\mathrm s=150\,\mathrm W$.
- id: mct-p9-lamp-chain-c
  content: |-
    $P=150\,\mathrm W$ and $I=10.6\,\mathrm{W/m^2}$
  feedback: |-
    This uses $2\pi r^2$, the area of a hemisphere. The model states that the lamp radiates isotropically in all directions, so the power is shared by the full sphere $4\pi r^2$.
- id: mct-p9-lamp-chain-d
  content: |-
    $P=150\,\mathrm W$ and $I=7.96\,\mathrm{W/m^2}$
  feedback: |-
    This divides by $4\pi r$ and leaves the wrong area dimension. Spherical area depends on radius squared: $A=4\pi r^2$.
- id: mct-p9-lamp-chain-e
  content: |-
    $P=150\,\mathrm W$ and $I=150\,\mathrm{W/m^2}$
  feedback: |-
    Intensity equals the source power only when the sharing area is exactly $1\,\mathrm{m^2}$. Here the spherical area is $4\pi(1.5)^2\,\mathrm{m^2}$, so the numerical intensity is smaller.
```

---

<a id="source-receiver-power"></a>
## Source-Video Worked Problem: Intensity on a Rectangular Receiver

The frame-verified solar problem in `vEzftaDL7fM` at 0:33:51-0:36:13 gives a uniform incident intensity

$$
I=1200\,\mathrm{W/m^2}
$$

on a rectangular plot measuring

$$
30\,\mathrm m\times40\,\mathrm m.
$$

**Source correction.** One automatic-caption cue renders the intensity as $12{,}200\,\mathrm{W/m^2}$. The visible prompt is $1200\,\mathrm{W/m^2}$, and the source's area, power, and energy calculations all use $1200\,\mathrm{W/m^2}$.

The illuminated area is the plot area, not the surface area of a sphere:

$$
A=(30\,\mathrm m)(40\,\mathrm m)
=\boxed{1200\,\mathrm{m^2}}.
$$

Because intensity is power per area, the received power is

$$
P=IA.
$$

Substitute and cancel area units:

$$
\begin{aligned}
P
&=\left(1200\,\frac{\mathrm W}{\mathrm{m^2}}\right)
  \left(1200\,\mathrm{m^2}\right)\\
&=1{,}440{,}000\,\mathrm W\\
&=\boxed{1.44\times10^6\,\mathrm W}.
\end{aligned}
$$

Here $\mathrm{m^2}$ cancels, leaving watts. Using $4\pi r^2$ would answer a different question about power spread across a spherical wavefront; no radius is given or needed for the rectangular receiver.

```quiz
type: radio
id: mct-p9-rectangular-receiver
shuffle: true
content: |-
  A uniform beam with intensity $750\,\mathrm{W/m^2}$ falls normally across an entire $12\,\mathrm m\times20\,\mathrm m$ rectangular receiver. What power reaches the receiver?
options:
- id: mct-p9-rectangular-receiver-a
  content: |-
    $1.80\times10^5\,\mathrm W$
  correct: true
  feedback: |-
    The illuminated area is the receiver area, $A=(12)(20)=240\,\mathrm{m^2}$. Since $I=P/A$, the received power is $P=IA=(750)(240)=1.80\times10^5\,\mathrm W$.
- id: mct-p9-rectangular-receiver-b
  content: |-
    $2.40\times10^4\,\mathrm W$
  feedback: |-
    This uses $12+20=32\,\mathrm m$ rather than the rectangular area. Intensity is per square meter, so multiply by $12\times20=240\,\mathrm{m^2}$.
- id: mct-p9-rectangular-receiver-c
  content: |-
    $4.80\times10^4\,\mathrm W$
  feedback: |-
    This uses the rectangle's perimeter, $2(12+20)=64\,\mathrm m$, which is a length. Received power requires the illuminated area in square meters.
- id: mct-p9-rectangular-receiver-d
  content: |-
    $3.125\,\mathrm{W/m^4}$
  feedback: |-
    Dividing intensity by area moves away from power and produces $\mathrm{W/m^4}$. Rearrange $I=P/A$ as $P=IA$, so the square meters cancel.
- id: mct-p9-rectangular-receiver-e
  content: |-
    $9.00\times10^4\,\mathrm W$
  feedback: |-
    Halving the result would apply only if half the stated rectangle were illuminated. The prompt says the entire receiver is covered normally, so use all $240\,\mathrm{m^2}$.
```

---

<a id="source-month-energy"></a>
## Source-Video Worked Problem: Power over a Month

The solar problem continues at 0:36:16-0:39:04 by asking for the energy received during a $30$-day month. Convert the time to seconds so it matches watts, or joules per second:

$$
\begin{aligned}
t
&=30\,\mathrm{day}
\left(\frac{24\,\mathrm h}{1\,\mathrm{day}}\right)
\left(\frac{60\,\mathrm{min}}{1\,\mathrm h}\right)
\left(\frac{60\,\mathrm s}{1\,\mathrm{min}}\right)\\
&=\boxed{2.592\times10^6\,\mathrm s}.
\end{aligned}
$$

Since $P=E/t$, multiply by time:

$$
\begin{aligned}
E
&=Pt\\
&=\left(1.44\times10^6\,\frac{\mathrm J}{\mathrm s}\right)
  \left(2.592\times10^6\,\mathrm s\right)\\
&=3.73248\times10^{12}\,\mathrm J\\
&\approx\boxed{3.73\times10^{12}\,\mathrm J}.
\end{aligned}
$$

The seconds cancel, leaving joules. This is incident energy under the source's stated constant-intensity idealization; usable electrical energy would require an efficiency factor, which the problem does not supply.

```quiz
type: radio
id: mct-p9-full-chain
shuffle: true
content: |-
  A constant intensity of $600\,\mathrm{W/m^2}$ illuminates an entire $5.0\,\mathrm m\times5.0\,\mathrm m$ collector for $8.0\,\mathrm h$. How much incident energy reaches it?
options:
- id: mct-p9-full-chain-a
  content: |-
    $4.32\times10^8\,\mathrm J$
  correct: true
  feedback: |-
    The collector area is $25\,\mathrm{m^2}$, so $P=IA=(600)(25)=15{,}000\,\mathrm W$. Convert $8.0\,\mathrm h$ to $28{,}800\,\mathrm s$ and use $E=Pt$ to obtain $4.32\times10^8\,\mathrm J$.
- id: mct-p9-full-chain-b
  content: |-
    $1.20\times10^5\,\mathrm J$
  feedback: |-
    This multiplies the received power by $8.0$ as though the power were joules per hour. Watts are joules per second, so convert $8.0\,\mathrm h$ to seconds before using $E=Pt$.
- id: mct-p9-full-chain-c
  content: |-
    $6.91\times10^5\,\mathrm J$
  feedback: |-
    This divides intensity by collector area before multiplying by time. To obtain received power, multiply intensity by illuminated area: $P=IA$.
- id: mct-p9-full-chain-d
  content: |-
    $7.20\times10^6\,\mathrm J$
  feedback: |-
    This converts hours to minutes but stops before seconds. Because watts are joules per second, use $8.0\times60\times60=28{,}800\,\mathrm s$.
- id: mct-p9-full-chain-e
  content: |-
    $1.08\times10^{10}\,\mathrm J$
  feedback: |-
    This squares the collector area after already computing it as $5.0\times5.0=25\,\mathrm{m^2}$. Intensity is multiplied once by the physical area, not by area squared.
```

---

<a id="choose-area"></a>
## Controlled Variation: Choose Area Before Calculating

The equation $I=P/A$ does not select the area. The description does.

- “Radiates isotropically” and “at distance $r$” identify a spherical wavefront: $A=4\pi r^2$.
- “Falls uniformly on an entire rectangular plot” identifies the receiving face: $A=LW$.
- If only part of a receiver is illuminated, use only that illuminated part.

Do not combine the source and receiver areas. For example, if an intensity has already been specified at a plot, multiply that local intensity by the plot's illuminated area. Reconstructing a sphere around the original source is unnecessary and may require information the question never gives.

```quiz
type: radio
id: mct-p9-choose-area
shuffle: true
content: |-
  Which area should be used in each intensity calculation?

  1. Find the intensity $3.0\,\mathrm m$ from an isotropic point source of known power.
  2. Find the power received by a fully illuminated $8.0\,\mathrm m\times15\,\mathrm m$ flat panel when the local intensity is known.
options:
- id: mct-p9-choose-area-a
  content: |-
    1. $4\pi(3.0\,\mathrm m)^2$; 2. $(8.0\,\mathrm m)(15\,\mathrm m)$
  correct: true
  feedback: |-
    Isotropic source power is shared across the full spherical wavefront at the stated radius. A known local intensity on a fully covered panel is multiplied by that panel's illuminated rectangular area.
- id: mct-p9-choose-area-b
  content: |-
    1. $\pi(3.0\,\mathrm m)^2$; 2. $(8.0\,\mathrm m)(15\,\mathrm m)$
  feedback: |-
    The panel area is right, but $\pi r^2$ is the area of a flat disk. An isotropic point source spreads through all directions, so its wavefront is a sphere with area $4\pi r^2$.
- id: mct-p9-choose-area-c
  content: |-
    1. $4\pi(3.0\,\mathrm m)^2$; 2. $4\pi(15\,\mathrm m)^2$
  feedback: |-
    The source area is right, but the second problem already gives intensity at a rectangular receiver. Use the physical illuminated panel area, not a sphere built from one side length.
- id: mct-p9-choose-area-d
  content: |-
    1. $4\pi(3.0\,\mathrm m)$; 2. $2(8.0\,\mathrm m+15\,\mathrm m)$
  feedback: |-
    Both expressions have units of length, not area. Intensity is power per square meter, so the divisor or multiplier must have square-meter units.
- id: mct-p9-choose-area-e
  content: |-
    Use $4\pi r^2$ in both cases because all intensity problems require a sphere.
  feedback: |-
    A sphere applies only when the relevant power is distributed across an isotropic spherical wavefront. A specified local intensity incident on a flat receiver uses the receiver's illuminated area.
```

---

<a id="summary"></a>
## Summary

- Convert total energy over time to power:
  $$
  P=\frac{E}{t},
  \qquad
  \frac{\mathrm J}{\mathrm s}=\mathrm W.
  $$
- Intensity is power per illuminated or spreading area:
  $$
  I=\frac{P}{A}.
  $$
- Use $A=4\pi r^2$ only when an isotropic point source shares its power across a spherical wavefront.
- For uniform intensity on a flat receiver, use the illuminated receiver area and calculate $P=IA$.
- Convert elapsed time to seconds before combining it with watts, then calculate $E=Pt$.
- Follow the units: $\mathrm J\to\mathrm W\to\mathrm{W/m^2}$ uses division by time and area; reversing the chain uses multiplication.
- Keep distance-ratio comparisons separate from this chain; they belong to the next lesson.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
