# Finding a Geostationary Satellite's Altitude

<!--
lesson-id: 212-M3-003
topic-code: MTH212.M3.03
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert the Period to Seconds](#convert-the-period-to-seconds)
- [Solve the Period Formula for Orbital Radius](#solve-the-period-formula-for-orbital-radius)
- [Convert Orbital Radius to Altitude](#convert-orbital-radius-to-altitude)
- [Apply the Method to Problem 3](#apply-the-method-to-problem-3)

## Prerequisites

- Circular-orbit period equation
- Rearranging formulas with several variables
- Taking a cube root
- Converting hours to seconds and meters to kilometers

---

<a id="introduction"></a>
## Introduction

A geostationary satellite has a $24\ \mathrm h$ orbital period. The circular-orbit period equation uses SI units and returns the satellite's distance $r$ from Earth's **center**:

$$
T^2=\frac{4\pi^2r^3}{GM_E}.
$$

The recognition cue is a satellite period together with Earth's mass and radius, followed by a request for **altitude**. Convert the period to seconds, solve for $r$, subtract Earth's radius, and convert the remaining height to kilometers:

$$
r=\left(\frac{GM_ET^2}{4\pi^2}\right)^{1/3},
\qquad
h=r-r_E.
$$

Track the quantity and unit at each stage:

$$
T\text{ in hours}
\longrightarrow T\text{ in seconds}
\longrightarrow r\text{ in meters}
\longrightarrow h=r-r_E\text{ in meters}
\longrightarrow h\text{ in kilometers}.
$$

---

<a id="convert-the-period-to-seconds"></a>
## Convert the Period to Seconds

**Example:** Convert a $24\ \mathrm h$ orbital period to seconds.

**Explanation**

Use conversion factors whose unwanted units cancel:

$$
\begin{aligned}
24\ \mathrm h
\left(\frac{60\ \mathrm{min}}{1\ \mathrm h}\right)
\left(\frac{60\ \mathrm s}{1\ \mathrm{min}}\right)
&=24(60)(60)\ \mathrm s\\
&=86400\ \mathrm s.
\end{aligned}
$$

Using $24$ as though it were already in seconds would make the orbital radius far too small.

```quiz
type: radio
id: p3-time-to-seconds
content: |-
  A circular-orbit formula requires time in seconds. What value should be used for a $12\ \mathrm h$ period?
options:
- id: p3-time-a
  content: |-
    $43200\ \mathrm s$
  correct: true
  feedback: |-
    Multiply by $60\ \mathrm{min/h}$ and $60\ \mathrm{s/min}$: $12(60)(60)=43200\ \mathrm s$.
- id: p3-time-b
  content: |-
    $720\ \mathrm s$
- id: p3-time-c
  content: |-
    $12\ \mathrm s$
- id: p3-time-d
  content: |-
    $12000\ \mathrm s$
- id: p3-time-e
  content: |-
    $4.32\times10^6\ \mathrm s$
```

---

<a id="solve-the-period-formula-for-orbital-radius"></a>
## Solve the Period Formula for Orbital Radius

**Example:** Make $r$ the subject of $T^2=4\pi^2r^3/(GM_E)$.

**Explanation**

Treat $T$, $G$, $M_E$, and $\pi$ as known quantities. First isolate $r^3$:

$$
\begin{aligned}
T^2&=\frac{4\pi^2r^3}{GM_E}\\
GM_ET^2&=4\pi^2r^3\\
\frac{GM_ET^2}{4\pi^2}&=r^3.
\end{aligned}
$$

Now take the cube root of both sides. A cube is an odd power, so there is one real root:

$$
r=\sqrt[3]{\frac{GM_ET^2}{4\pi^2}}
=\left(\frac{GM_ET^2}{4\pi^2}\right)^{1/3}.
$$

The entire fraction belongs inside the cube root.

```quiz
type: radio
id: p3-isolate-radius
content: |-
  Which expression correctly solves $T^2=4\pi^2r^3/(GM)$ for the orbital radius $r$?
options:
- id: p3-radius-a
  content: |-
    $r=\left(\dfrac{GMT^2}{4\pi^2}\right)^{1/3}$
  correct: true
  feedback: |-
    Multiply by $GM$, divide by $4\pi^2$, and then take the cube root of the entire result.
- id: p3-radius-b
  content: |-
    $r=\left(\dfrac{4\pi^2T^2}{GM}\right)^{1/3}$
- id: p3-radius-c
  content: |-
    $r=\dfrac{GMT^2}{4\pi^2}$
- id: p3-radius-d
  content: |-
    $r=\left(\dfrac{GMT}{4\pi^2}\right)^{1/3}$
- id: p3-radius-e
  content: |-
    $r=\left(\dfrac{GMT^2}{4\pi}\right)^{1/2}$
```

---

<a id="convert-orbital-radius-to-altitude"></a>
## Convert Orbital Radius to Altitude

**Example:** A calculation gives an orbital radius $r=2.10\times10^7\ \mathrm m$ for a planet with radius $r_P=6.0\times10^6\ \mathrm m$. Find the satellite's altitude in kilometers.

**Explanation**

Orbital radius is measured from the planet's center; altitude is measured from its surface. Subtract first while both lengths use meters:

$$
\begin{aligned}
h&=r-r_P\\
&=2.10\times10^7-6.0\times10^6\\
&=1.50\times10^7\ \mathrm m.
\end{aligned}
$$

Then convert meters to kilometers with a factor whose meters cancel:

$$
(1.50\times10^7\ \mathrm m)
\left(\frac{1\ \mathrm{km}}{1000\ \mathrm m}\right)
=1.50\times10^4\ \mathrm{km}.
$$

```quiz
type: radio
id: p3-radius-to-altitude
content: |-
  A satellite's orbital radius is $3.2\times10^7\ \mathrm m$, measured from a planet's center. The planet's radius is $7.0\times10^6\ \mathrm m$. What is the satellite's altitude in kilometers?
options:
- id: p3-altitude-a
  content: |-
    $2.5\times10^4\ \mathrm{km}$
  correct: true
  feedback: |-
    Subtract the planet's radius, then divide by $1000$: $(3.2\times10^7-7.0\times10^6)\ \mathrm m=2.5\times10^7\ \mathrm m=2.5\times10^4\ \mathrm{km}$.
- id: p3-altitude-b
  content: |-
    $3.2\times10^4\ \mathrm{km}$
- id: p3-altitude-c
  content: |-
    $2.5\times10^7\ \mathrm{km}$
- id: p3-altitude-d
  content: |-
    $3.9\times10^4\ \mathrm{km}$
- id: p3-altitude-e
  content: |-
    $7.0\times10^3\ \mathrm{km}$
```

---

<a id="apply-the-method-to-problem-3"></a>
## Apply the Method to Problem 3

**Example:** Find the altitude of a geostationary satellite. Use $G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$, $M_E=5.97\times10^{24}\ \mathrm{kg}$, $r_E=6.38\times10^6\ \mathrm{m}$, and a $24\ \mathrm{h}$ orbital period.

**Explanation**

For a circular orbit,

$$
T^2=\frac{4\pi^2r^3}{GM_E},
\qquad
r=\left(\frac{GM_ET^2}{4\pi^2}\right)^{1/3}.
$$

With $T=86400\ \mathrm{s}$,

$$
r=4.2227\times10^7\ \mathrm{m}.
$$

Subtracting Earth's radius gives

$$
h=r-r_E
=3.5847\times10^7\ \mathrm{m}
=3.5847\times10^4\ \mathrm{km}.
$$

The supplied constants support three significant figures, so $h=3.58\times10^4\ \mathrm{km}$, entered as `35800`.

The answer choices diagnose common mistakes:

- `42200` is the center-to-center orbital radius in kilometers; Earth's radius was not subtracted.
- `35847000` is the altitude in meters; it was not converted to kilometers.
- `35847` keeps more digits than the supplied constants support.
- `6380` is Earth's radius in kilometers, not the satellite's altitude.

```quiz
type: radio
id: p3-source-check
content: |-
  **Question 2**

  Find the altitude of a geostationary satellite. Use $G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$, $M_E=5.97\times10^{24}\ \mathrm{kg}$, $r_E=6.38\times10^6\ \mathrm{m}$, and a $24\ \mathrm{h}$ orbital period.

  Enter the altitude in kilometers as a number only:
options:
- id: p3-source-a
  content: |-
    $35800$
  correct: true
  feedback: |-
    For a circular orbit,

    $$
    T^2=\frac{4\pi^2r^3}{GM_E},
    \qquad
    r=\left(\frac{GM_ET^2}{4\pi^2}\right)^{1/3}.
    $$

    With $T=86400\ \mathrm{s}$,

    $$
    r=4.2227\times10^7\ \mathrm{m}.
    $$

    Subtracting Earth's radius gives

    $$
    h=r-r_E
    =3.5847\times10^7\ \mathrm{m}
    =3.5847\times10^4\ \mathrm{km}.
    $$

    The supplied constants support three significant figures, so $h=3.58\times10^4\ \mathrm{km}$, entered as `35800`.
- id: p3-source-b
  content: |-
    $42200$
- id: p3-source-c
  content: |-
    $35847000$
- id: p3-source-d
  content: |-
    $35847$
- id: p3-source-e
  content: |-
    $6380$
```

---

## Summary

- Cue: a circular-orbit period is given, but altitude above the surface is requested.
- Convert the period to seconds before using SI constants.
- Make orbital radius the subject: $r=[GM_ET^2/(4\pi^2)]^{1/3}$.
- Convert radius to altitude with $h=r-r_E$ while both quantities are in meters.
- Convert meters to kilometers with a factor whose meters cancel, and round only at the end; for Problem 3, enter `35800`.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
