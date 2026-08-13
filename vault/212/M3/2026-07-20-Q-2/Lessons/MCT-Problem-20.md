# Solve Circular-Satellite Speed, Period, and Geostationary Altitude

<!--
lesson-id: 212-M3-056
topic-code: MTH212.M3.56
-->

## Table of Contents

- [Introduction](#introduction)
- [Draw Gravity as the Inward Force](#gravity-as-inward-force)
- [Convert Altitude to Orbital Radius](#altitude-to-orbital-radius)
- [Source-Video Worked Problem 1: Speed and Period From Altitude](#source-video-speed-period)
- [Bridge Period to Radius](#period-to-radius)
- [Source-Video Worked Problem 2: Geostationary Altitude and Speed](#source-video-geostationary)
- [Lecture Transfer: Conditions and an Optional Energy Check](#lecture-transfer)
- [Summary](#summary)

## Prerequisites

- Use Newton's universal-gravitation magnitude $F_g=GMm/r^2$.
- Use the radial-acceleration magnitude $a_r=v^2/r$ for uniform circular motion.
- Rearrange an equation for one chosen variable.
- Use a circle's circumference $2\pi r$.
- Convert kilometers to meters and hours to seconds with units attached.
- Evaluate square roots, cube roots, and scientific notation on a calculator.

---

<a id="introduction"></a>
## Introduction

A circular-satellite problem usually gives either an altitude or a period. Both versions use one physical move:

$$
\boxed{\text{gravity is the inward net force}}
\qquad\Longrightarrow\qquad
\frac{GMm}{r^2}=m\frac{v^2}{r}.
$$

The geometry supplies the bridge between speed and period:

$$
\boxed{v=\frac{2\pi r}{T}}.
$$

Use the same sequence every time:

1. Convert all inputs to SI units.
2. Identify the center-to-center orbital radius $r$. If an altitude $h$ is given, write $r=R+h$.
3. Draw only the actual forces and take inward as positive.
4. Derive the needed relation symbolically.
5. Use $v=2\pi r/T$ to pass between speed and period.
6. If the question asks for height, subtract the planet's radius only after finding $r$.

That creates two directions through the same chain:

$$
h\text{ given}:\quad h\longrightarrow r\longrightarrow v\longrightarrow T,
$$

$$
T\text{ given}:\quad T\longrightarrow r\longrightarrow h
\quad\text{with }v\text{ available from either bridge relation}.
$$

The central body's mass is $M$, the satellite's mass is $m$, its radius is $R$, and the satellite's altitude is $h$.

---

<a id="gravity-as-inward-force"></a>
## Draw Gravity as the Inward Force

In the source model, Earth's gravity is the only force retained on the satellite. A useful side view is

```text
Earth center ●──────── R_E ────────|──── h ────● satellite
             <────────────── r = R_E + h ──────>
                                             ← F_g
                                             ↑ v (tangent)
```

The free-body diagram contains one arrow, $F_g$, directed toward Earth's center. The velocity is tangent to the orbit and is not a force.

Take inward as positive:

$$
\sum F_{\text{in}}=m\frac{v^2}{r}.
$$

Since gravity is the only inward force,

$$
\frac{GM_Em}{r^2}=m\frac{v^2}{r}.
$$

Cancel the satellite mass and one factor of $r$:

$$
\frac{GM_E}{r}=v^2,
\qquad
\boxed{v=\sqrt{\frac{GM_E}{r}}}.
$$

The satellite's mass cancels because both its gravitational force and its required radial net force are proportional to $m$.

**Source correction.** In the video frame near 1:38, the inward arrow is labeled $F_c$, and the narration speaks of a “centripetal force.” Centripetal is a role played by the net inward force, not a second interaction to add to the free-body diagram. Here the arrow must be labeled $F_g$, and gravity alone supplies $mv^2/r$.

```quiz
type: radio
id: mct-p20-inward-force
shuffle: true
content: |-
  A satellite of mass $m$ moves in a circular orbit of radius $r$ around a planet of mass $M$. No thrust acts. Which free-body description and radial equation are correct?
options:
- id: mct-p20-inward-force-a
  content: |-
    One inward gravity arrow, with $\dfrac{GMm}{r^2}=m\dfrac{v^2}{r}$.
  correct: true
  feedback: |-
    Gravity is the only interaction force on the satellite. Its inward resultant must equal the radial-force requirement $mv^2/r$, so $GMm/r^2=mv^2/r$.
- id: mct-p20-inward-force-b
  content: |-
    Two inward arrows, gravity and centripetal force, with $\dfrac{GMm}{r^2}+m\dfrac{v^2}{r}=m\dfrac{v^2}{r}$.
  feedback: |-
    The term $mv^2/r$ is not an additional force. It is the value the net inward force must have. Drawing both gravity and a separate centripetal force counts the same radial role twice.
- id: mct-p20-inward-force-c
  content: |-
    One outward gravity arrow, with $\dfrac{GMm}{r^2}=-m\dfrac{v^2}{r}$.
  feedback: |-
    Newtonian gravity is attractive, so the planet's force on the satellite points toward the planet's center. With inward chosen positive, both magnitudes enter positively.
- id: mct-p20-inward-force-d
  content: |-
    One inward gravity arrow, with $\dfrac{GMm}{h^2}=m\dfrac{v^2}{h}$ for altitude $h$.
  feedback: |-
    The directions are right, but both laws require the circular radius measured from the planet's center. At altitude $h$, that radius is $r=R+h$, not $h$.
- id: mct-p20-inward-force-e
  content: |-
    One inward gravity arrow, but both $m$ and $M$ cancel, so $v^2=G/r$.
  feedback: |-
    Only the satellite mass $m$ appears on both sides. The central mass $M$ remains, giving $v^2=GM/r$; a more massive central body supports a faster circular orbit at the same radius.
```

---

<a id="altitude-to-orbital-radius"></a>
## Convert Altitude to Orbital Radius

Newton's force law and the circular-motion equation both use the distance from Earth's center to the satellite:

$$
\boxed{r=R_E+h}.
$$

Altitude $h$ begins at Earth's surface. Earth's radius $R_E$ ends at that surface. They must be in the same units before they are added.

For the source values,

$$
R_E=6.38\times10^6\ \mathrm m,
\qquad
h=3800\ \mathrm{km}
\left(\frac{1000\ \mathrm m}{1\ \mathrm{km}}\right)
=3.80\times10^6\ \mathrm m.
$$

The unwanted kilometer unit cancels, leaving

$$
r=6.38\times10^6+3.80\times10^6
=1.018\times10^7\ \mathrm m.
$$

The three distances are not interchangeable:

| Quantity | Meaning | Source value |
| --- | --- | ---: |
| $R_E$ | Earth radius | $6.38\times10^6\ \mathrm m$ |
| $h$ | height above the surface | $3.80\times10^6\ \mathrm m$ |
| $r$ | circular radius from Earth's center | $1.018\times10^7\ \mathrm m$ |

---

<a id="source-video-speed-period"></a>
## Source-Video Worked Problem 1: Speed and Period From Altitude

The source-video segment `QIaAleG0Eb4` from 00:00:01–00:07:56 asks for the speed and period of a satellite at $3800\ \mathrm{km}$ above Earth. Use

$$
G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2},
\qquad
M_E=5.97\times10^{24}\ \mathrm{kg}.
$$

The radius conversion has already given $r=1.018\times10^7\ \mathrm m$. Substitute only after deriving the speed equation:

$$
\begin{aligned}
v
&=\sqrt{\frac{GM_E}{r}}\\[4pt]
&=\sqrt{
\frac{(6.67\times10^{-11})(5.97\times10^{24})}
{1.018\times10^7}
}\\[4pt]
&=6254.3\ \mathrm{m/s}.
\end{aligned}
$$

One revolution covers the circumference $2\pi r$. Therefore,

$$
v=\frac{2\pi r}{T}
\qquad\Longrightarrow\qquad
\boxed{T=\frac{2\pi r}{v}}.
$$

Then

$$
T=\frac{2\pi(1.018\times10^7)}{6254.3}
=10{,}227\ \mathrm s.
$$

Convert seconds to hours with two reciprocal factors:

$$
10{,}227\ \mathrm s
\left(\frac{1\ \mathrm{min}}{60\ \mathrm s}\right)
\left(\frac{1\ \mathrm h}{60\ \mathrm{min}}\right)
=2.84\ \mathrm h.
$$

Thus the source case gives

$$
\boxed{v=6254.3\ \mathrm{m/s}},
\qquad
\boxed{T=10{,}227\ \mathrm s=2.84\ \mathrm h}.
$$

```quiz
type: radio
id: mct-p20-altitude-speed-period
shuffle: true
content: |-
  A satellite circles Earth at an altitude of $620\ \mathrm{km}$. Use $R_E=6.38\times10^6\ \mathrm m$ and $GM_E=3.982\times10^{14}\ \mathrm{m^3/s^2}$. Which set of results is consistent?
options:
- id: mct-p20-altitude-speed-period-a
  content: |-
    $r=7.00\times10^6\ \mathrm m$, $v=7.54\times10^3\ \mathrm{m/s}$, and $T=97.2\ \mathrm{min}$.
  correct: true
  feedback: |-
    First, $620\ \mathrm{km}=6.20\times10^5\ \mathrm m$, so $r=6.38\times10^6+0.620\times10^6=7.00\times10^6\ \mathrm m$. Then $v=\sqrt{GM_E/r}=7.54\times10^3\ \mathrm{m/s}$ and $T=2\pi r/v=5831\ \mathrm s=97.2\ \mathrm{min}$.
- id: mct-p20-altitude-speed-period-b
  content: |-
    $r=6.20\times10^5\ \mathrm m$, $v=2.53\times10^4\ \mathrm{m/s}$, and $T=2.56\ \mathrm{min}$.
  feedback: |-
    This uses altitude as the circular radius. The force-law radius starts at Earth's center, so Earth's $6.38\times10^6\ \mathrm m$ radius must be added before either formula is used.
- id: mct-p20-altitude-speed-period-c
  content: |-
    $r=6.38\times10^6\ \mathrm m$, $v=7.90\times10^3\ \mathrm{m/s}$, and $T=84.6\ \mathrm{min}$.
  feedback: |-
    These are surface-radius results. The $620\ \mathrm{km}$ altitude has been omitted; the orbit radius is $R_E+h=7.00\times10^6\ \mathrm m$.
- id: mct-p20-altitude-speed-period-d
  content: |-
    $r=7.00\times10^6\ \mathrm m$, $v=7.54\times10^3\ \mathrm{m/s}$, and $T=15.5\ \mathrm{min}$.
  feedback: |-
    The radius and speed are right, but this uses $T=r/v$. One complete orbit has distance $2\pi r$, so the period must be $2\pi$ times larger: $97.2\ \mathrm{min}$.
- id: mct-p20-altitude-speed-period-e
  content: |-
    $r=7.00\times10^6\ \mathrm m$, $v=7.54\times10^3\ \mathrm{m/s}$, and $T=1.62\ \mathrm{min}$.
  feedback: |-
    The calculation gives $5831\ \mathrm s=97.2\ \mathrm{min}=1.62\ \mathrm h$. This option attaches minutes to the numerical value in hours.
```

---

<a id="period-to-radius"></a>
## Bridge Period to Radius

When the period is given, use the same force result and the same circumference bridge:

$$
v^2=\frac{GM}{r},
\qquad
v=\frac{2\pi r}{T}.
$$

Substitute the second relation into the first before inserting numbers:

$$
\left(\frac{2\pi r}{T}\right)^2=\frac{GM}{r}.
$$

Now isolate the requested subject $r$:

$$
\frac{4\pi^2r^2}{T^2}=\frac{GM}{r},
$$

$$
4\pi^2r^3=GMT^2,
$$

$$
\boxed{r=\left(\frac{GMT^2}{4\pi^2}\right)^{1/3}}.
$$

This result is the orbital radius. If the problem asks for altitude,

$$
\boxed{h=r-R}.
$$

```quiz
type: radio
id: mct-p20-period-radius-symbolic
shuffle: true
content: |-
  A satellite's circular period $T$ is known. Which expression gives its orbital radius $r$ about a central mass $M$?
options:
- id: mct-p20-period-radius-symbolic-a
  content: |-
    $r=\left(\dfrac{GMT^2}{4\pi^2}\right)^{1/3}$
  correct: true
  feedback: |-
    Combining $v^2=GM/r$ with $v=2\pi r/T$ gives $4\pi^2r^3=GMT^2$. Dividing and taking a cube root isolates the center-based orbital radius.
- id: mct-p20-period-radius-symbolic-b
  content: |-
    $r=\left(\dfrac{GMT^2}{4\pi^2}\right)^{1/2}$
  feedback: |-
    The rearrangement produces $r^3$, because $r^2$ comes from squaring $2\pi r/T$ and another $r$ comes from clearing $GM/r$. The final operation is a cube root, not a square root.
- id: mct-p20-period-radius-symbolic-c
  content: |-
    $r=\left(\dfrac{GMT}{4\pi^2}\right)^{1/3}$
  feedback: |-
    Squaring $v=2\pi r/T$ produces $T^2$ in the denominator, so the isolated expression contains $GMT^2$. Omitting the square also gives the wrong dimensions.
- id: mct-p20-period-radius-symbolic-d
  content: |-
    $r=\dfrac{GMT^2}{4\pi^2}$
  feedback: |-
    This is the expression for $r^3$, not $r$. Take the cube root after dividing by $4\pi^2$.
- id: mct-p20-period-radius-symbolic-e
  content: |-
    $r=\left(\dfrac{4\pi^2GM}{T^2}\right)^{1/3}$
  feedback: |-
    This inverts the period dependence. Longer-period circular orbits have larger radii, so $T^2$ must be in the numerator and $4\pi^2$ in the denominator.
```

---

<a id="source-video-geostationary"></a>
## Source-Video Worked Problem 2: Geostationary Altitude and Speed

The source-video segment `QIaAleG0Eb4` from 00:07:56–00:16:55 studies a satellite that remains over the same point on Earth's equator. Earth **rotates** about its own axis; the satellite **revolves** around Earth. To keep the same relative longitude, their angular rates and directions must match.

The course uses a $24\ \mathrm h$ rotational period:

$$
T=24\ \mathrm h
\left(\frac{60\ \mathrm{min}}{1\ \mathrm h}\right)
\left(\frac{60\ \mathrm s}{1\ \mathrm{min}}\right)
=86{,}400\ \mathrm s.
$$

Insert the period only after the symbolic derivation:

$$
\begin{aligned}
r
&=\left(\frac{GM_ET^2}{4\pi^2}\right)^{1/3}\\[4pt]
&=\left[
\frac{(6.67\times10^{-11})(5.97\times10^{24})(86{,}400)^2}
{4\pi^2}
\right]^{1/3}\\[4pt]
&=4.22\times10^7\ \mathrm m.
\end{aligned}
$$

That is the distance from Earth's center, not the requested height. Subtract Earth's radius:

$$
\begin{aligned}
h
&=r-R_E\\
&=4.22\times10^7-6.38\times10^6\\
&=3.58\times10^7\ \mathrm m\\
&=35{,}800\ \mathrm{km}.
\end{aligned}
$$

The speed may be checked by either relation:

$$
v=\sqrt{\frac{GM_E}{r}}
\qquad\text{or}\qquad
v=\frac{2\pi r}{T}.
$$

Using unrounded intermediate values, both give approximately

$$
v=3.07\times10^3\ \mathrm{m/s}.
$$

The video reports $3072\ \mathrm{m/s}$; the small difference comes from the rounded constants and displayed radius. The source result and a recomputation agree to about $0.04\%$.

Therefore, the source case gives

$$
\boxed{T=86{,}400\ \mathrm s},
\qquad
\boxed{r=4.22\times10^7\ \mathrm m},
$$

$$
\boxed{h=3.58\times10^7\ \mathrm m=35{,}800\ \mathrm{km}},
\qquad
\boxed{v\approx3.07\times10^3\ \mathrm{m/s}\ \text{(video: }3072\ \mathrm{m/s}\text{)}}.
$$

**Source terminology correction.** The prompt calls a same-point, equatorial satellite “geosynchronous.” Matching Earth's rotational period is the geosynchronous condition. Remaining fixed over one point requires the stronger **geostationary** conditions: a circular orbit in Earth's equatorial plane, motion in the same direction as Earth's rotation, and the matching period.

**Period note.** The source and lecture use $24\ \mathrm h$, which is the intended course approximation. A more precise geostationary calculation uses Earth's sidereal rotation period, which is slightly shorter; do not mix that period with the source's rounded result.

```quiz
type: radio
id: mct-p20-twelve-hour-altitude
shuffle: true
content: |-
  A circular Earth satellite has period $12.0\ \mathrm h$. Use $GM_E=3.982\times10^{14}\ \mathrm{m^3/s^2}$ and $R_E=6.38\times10^6\ \mathrm m$. What is its altitude above Earth's surface?
options:
- id: mct-p20-twelve-hour-altitude-a
  content: |-
    $2.02\times10^4\ \mathrm{km}$
  correct: true
  feedback: |-
    Convert $T=12.0(3600)=43{,}200\ \mathrm s$. Then $r=[GM_ET^2/(4\pi^2)]^{1/3}=2.66\times10^7\ \mathrm m$. Subtract $R_E$: $h=2.022\times10^7\ \mathrm m=2.02\times10^4\ \mathrm{km}$.
- id: mct-p20-twelve-hour-altitude-b
  content: |-
    $2.66\times10^4\ \mathrm{km}$
  feedback: |-
    This is the orbital radius $r=2.66\times10^7\ \mathrm m$ converted to kilometers. The requested altitude is $h=r-R_E$, so Earth's radius still must be subtracted.
- id: mct-p20-twelve-hour-altitude-c
  content: |-
    $3.58\times10^4\ \mathrm{km}$
  feedback: |-
    This is the course's $24\ \mathrm h$ geostationary altitude. A $12\ \mathrm h$ period must be inserted as $43{,}200\ \mathrm s$ before taking the cube root.
- id: mct-p20-twelve-hour-altitude-d
  content: |-
    $1.79\times10^4\ \mathrm{km}$
  feedback: |-
    This halves the $24\ \mathrm h$ altitude. Radius does not scale linearly with period: $r\propto T^{2/3}$, and altitude is found only after that radius is calculated.
- id: mct-p20-twelve-hour-altitude-e
  content: |-
    $1.38\times10^4\ \mathrm{km}$
  feedback: |-
    This effectively subtracts too much of Earth's radius. The cube-root formula already returns the center-based radius once; subtract $R_E$ exactly once to obtain altitude.
```

```quiz
type: radio
id: mct-p20-geostationary-conditions
shuffle: true
content: |-
  Which set of conditions is sufficient for a satellite to remain above one fixed point on Earth's surface?
options:
- id: mct-p20-geostationary-conditions-a
  content: |-
    A circular orbit in Earth's equatorial plane, in Earth's rotation direction, with period equal to Earth's rotational period.
  correct: true
  feedback: |-
    These are the geostationary conditions. The equal period matches angular rate, while the equatorial, same-direction circular orbit keeps the satellite at one longitude and latitude.
- id: mct-p20-geostationary-conditions-b
  content: |-
    Any circular orbit with a $24\ \mathrm h$ period.
  feedback: |-
    A matching period alone is only the geosynchronous condition. An orbit outside the equatorial plane does not remain over one fixed surface point.
- id: mct-p20-geostationary-conditions-c
  content: |-
    A circular equatorial orbit with any period, provided the satellite rotates once per day about its own axis.
  feedback: |-
    The satellite's own rotation is not its revolution around Earth. The orbital period must match Earth's rotation period for the relative longitude to stay fixed.
- id: mct-p20-geostationary-conditions-d
  content: |-
    A circular equatorial orbit opposite Earth's rotation direction with a $24\ \mathrm h$ period.
  feedback: |-
    Opposite-direction motion makes the satellite sweep rapidly across Earth's sky. A geostationary satellite must revolve in the same direction as Earth rotates.
- id: mct-p20-geostationary-conditions-e
  content: |-
    Any orbit whose altitude is $4.22\times10^7\ \mathrm m$.
  feedback: |-
    The number $4.22\times10^7\ \mathrm m$ is the source's orbital radius, not its altitude. A radius by itself also does not state the required plane and direction.
```

---

<a id="lecture-transfer"></a>
## Lecture Transfer: Conditions and an Optional Energy Check

The M3-1 lecture notes use the same radial balance and circumference bridge to derive

$$
T^2=\frac{4\pi^2}{GM}r^3.
$$

They also make the geostationary conditions explicit: circular, equatorial, same direction as Earth's rotation, and a period equal to Earth's rotational period. Those conditions explain why a matching period is necessary but not sufficient for a fixed point over Earth.

After a circular orbit has been solved, its energy provides a compact check:

$$
K=\frac12mv^2
=\frac12m\left(\frac{GM}{r}\right)
=\frac{GMm}{2r},
$$

$$
U=-\frac{GMm}{r},
\qquad
E=K+U=-\frac{GMm}{2r}.
$$

This is an after-solution check, not a second route for the source questions. The speed, period, radius, and altitude still come from radial force balance plus $v=2\pi r/T$.

---

<a id="summary"></a>
## Summary

- Draw the actual inward interaction $F_g$; do not add a separate centripetal-force arrow.
- Use the center-based orbital radius. If altitude is given, convert units and write
  $$
  r=R+h.
  $$
- Gravity supplying the radial net force gives
  $$
  \frac{GMm}{r^2}=m\frac{v^2}{r},
  \qquad
  v=\sqrt{\frac{GM}{r}}.
  $$
- One revolution has length $2\pi r$, so
  $$
  v=\frac{2\pi r}{T},
  \qquad
  T=\frac{2\pi r}{v}.
  $$
- If period is known, isolate the orbital radius symbolically:
  $$
  r=\left(\frac{GMT^2}{4\pi^2}\right)^{1/3}.
  $$
- If height is requested, finish with $h=r-R$. The source's $4.22\times10^7\ \mathrm m$ is orbital radius; its geostationary altitude is $3.58\times10^7\ \mathrm m=35{,}800\ \mathrm{km}$.
- Earth rotates about its axis; a satellite revolves around Earth. Remaining over one point requires the full geostationary conditions, not just a matching period.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
