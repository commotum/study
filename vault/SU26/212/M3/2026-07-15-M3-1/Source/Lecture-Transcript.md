# Physics 212: Newtonian Gravitation, Kepler’s Laws, and Orbital Motion

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 1X is currently open and will close Friday at 6:00 p.m. The assignment is optional, but be sure to follow its instructions carefully if you choose to complete it.

Quiz 2 will open on Saturday for the Proctorio version and close on Monday. The Zoom versions of Quiz 2 will also be administered on Monday.

You should continue preparing your handwritten note sheet for Quiz 2.

## Introduction to Newtonian Gravity

Today, we are beginning our study of gravity and orbital motion.

We will use **Newtonian gravity**, meaning that we will describe gravitational interactions using forces rather than general relativity.

Gravity is a **central force**. The force between two objects acts along the line connecting their centers, and its magnitude depends only on the distance between them.

For two point masses $m_1$ and $m_2$ separated by a distance $r$, the magnitude of the gravitational force is

$$
F_g
=
G\frac{m_1m_2}{r^2},
$$

where $G$ is the universal gravitational constant:

$$
\boxed{
G
=
6.67\times10^{-11}\ \mathrm{N}\,\mathrm{m}^2/\mathrm{kg}^2
}.
$$

If the radial unit vector $\hat{r}$ points outward from the central mass, the force on the other mass can be written as

$$
\boxed{
\vec{F}_g
=
-G\frac{m_1m_2}{r^2}\hat{r}
}.
$$

The negative sign indicates that gravity is attractive and points inward, opposite the outward radial direction.

By Newton’s third law, the two objects exert gravitational forces of equal magnitude and opposite direction on one another.

## Gravitational Acceleration Near Earth

Near Earth’s surface, the gravitational force on an object of mass $m$ is often written as

$$
F_g=mg,
$$

where $g$ is the local acceleration due to gravity.

The general gravitational-force equation gives

$$
F_g
=
G\frac{M_E m}{R_E^2},
$$

where:

- $M_E$ is the mass of Earth
- $R_E$ is the radius of Earth
- $m$ is the mass of the object

Equating the two expressions,

$$
mg
=
G\frac{M_E m}{R_E^2}.
$$

The object’s mass cancels:

$$
g
=
G\frac{M_E}{R_E^2}.
$$

Using

$$
M_E
=
5.97\times10^{24}\ \mathrm{kg}
$$

and

$$
R_E
\approx
6.37\times10^6\ \mathrm{m},
$$

we obtain

$$
g
=
\frac{
\left(
6.67\times10^{-11}\ \mathrm{N}\,\mathrm{m}^2/\mathrm{kg}^2
\right)
\left(
5.97\times10^{24}\ \mathrm{kg}
\right)
}{
\left(
6.37\times10^6\ \mathrm{m}
\right)^2
}.
$$

Therefore,

$$
\boxed{
g\approx9.81\ \mathrm{m}/\mathrm{s}^2
}.
$$

The universal gravitational constant $G$ has the same value everywhere. The local gravitational acceleration $g$, however, depends on the mass of the attracting body and the distance from its center.

In general,

$$
\boxed{
g(r)=\frac{GM}{r^2}
}.
$$

## Gravitational Acceleration at an Altitude

Consider a satellite at an altitude

$$
h=\frac{R_E}{3}
$$

above Earth’s surface.

The distance from the satellite to Earth’s center is not $h$. It is

$$
r=R_E+h.
$$

The gravitational acceleration at this altitude is

$$
g_h
=
\frac{GM_E}{(R_E+h)^2}.
$$

At Earth’s surface,

$$
g_0
=
\frac{GM_E}{R_E^2}.
$$

To compare the two values, form the ratio

$$
\frac{g_h}{g_0}
=
\frac{
GM_E/(R_E+h)^2
}{
GM_E/R_E^2
}.
$$

The factors $G$ and $M_E$ cancel:

$$
\frac{g_h}{g_0}
=
\frac{R_E^2}{(R_E+h)^2}.
$$

Using

$$
h=\frac{R_E}{3},
$$

the distance from Earth’s center becomes

$$
R_E+h
=
R_E+\frac{R_E}{3}
=
\frac{4R_E}{3}.
$$

Therefore,

$$
\frac{g_h}{g_0}
=
\frac{
R_E^2
}{
\left(
\frac{4R_E}{3}
\right)^2
}.
$$

Simplifying,

$$
\frac{g_h}{g_0}
=
\frac{9}{16}.
$$

Thus,

$$
\boxed{
\frac{g_h}{g_0}
\approx0.56
}.
$$

At an altitude equal to one-third of Earth’s radius, the gravitational acceleration is approximately $56\%$ of its surface value:

$$
g_h\approx0.56g_0.
$$

This calculation illustrates that gravity does not suddenly disappear above Earth’s surface. It decreases continuously according to the inverse-square relationship.

## Gravity Compared with the Electric Force

The electric and gravitational forces between two particles both follow inverse-square laws.

For two electrons separated by a distance $r$, the electric-force magnitude is

$$
F_e
=
k_e\frac{e^2}{r^2},
$$

while the gravitational-force magnitude is

$$
F_g
=
G\frac{m_e^2}{r^2}.
$$

Their ratio is

$$
\frac{F_e}{F_g}
=
\frac{
k_e e^2/r^2
}{
Gm_e^2/r^2
}.
$$

The distance cancels:

$$
\frac{F_e}{F_g}
=
\frac{k_e e^2}{Gm_e^2}.
$$

Numerically,

$$
\boxed{
\frac{F_e}{F_g}
\approx4\times10^{42}
}.
$$

The electric force between two electrons is therefore approximately $10^{42}$ times stronger than their gravitational attraction.

Gravity nevertheless dominates many astronomical systems because ordinary matter is usually close to electrically neutral. Positive and negative charges tend to cancel on large scales, while the gravitational effects of ordinary mass add together.

Within Newtonian mechanics, gravity between ordinary masses is always attractive.

## Gravitational Potential Energy

Force and potential energy are related by

$$
F_r
=
-\frac{dU}{dr}.
$$

For gravity,

$$
F_r
=
-G\frac{Mm}{r^2}.
$$

Therefore,

$$
-\frac{dU}{dr}
=
-G\frac{Mm}{r^2}.
$$

Canceling the negative signs gives

$$
\frac{dU}{dr}
=
G\frac{Mm}{r^2}.
$$

Integrating with respect to $r$,

$$
U(r)
=
\int
G\frac{Mm}{r^2}\,dr.
$$

Because

$$
\int r^{-2}\,dr=-r^{-1},
$$

we obtain

$$
U(r)
=
-\frac{GMm}{r}+C.
$$

We conventionally choose the gravitational potential energy to be zero when the two objects are infinitely far apart:

$$
U(\infty)=0.
$$

This makes $C=0$, so

$$
\boxed{
U(r)
=
-\frac{GMm}{r}
}.
$$

The negative sign means that two gravitationally interacting objects at a finite separation form a bound system relative to the reference state in which they are infinitely far apart.

As $r$ increases,

$$
U(r)\rightarrow0.
$$

As the objects move closer together, the potential energy becomes more negative.

## Circular Orbits

Consider a satellite of mass $m$ moving in a circular orbit of radius $r$ around a much more massive body of mass $M$.

For the scalar radial equation, take inward as positive.

The gravitational force supplies the inward radial net force:

$$
\sum F_r=m a_r=m\frac{v^2}{r}=F_g.
$$

Therefore,

$$
G\frac{Mm}{r^2}
=
m\frac{v^2}{r}.
$$

The satellite’s mass cancels:

$$
G\frac{M}{r^2}
=
\frac{v^2}{r}.
$$

Multiplying by $r$ gives

$$
v^2
=
\frac{GM}{r}.
$$

Thus, the circular orbital speed is

$$
\boxed{
v
=
\sqrt{\frac{GM}{r}}
}.
$$

The speed is independent of the satellite’s mass. At a specified orbital radius, all sufficiently small satellites orbit the same central body with the same circular-orbit speed.

A larger orbital radius corresponds to a lower orbital speed:

$$
r\uparrow
\quad\Longrightarrow\quad
v\downarrow.
$$

## Kinetic and Potential Energy in a Circular Orbit

The satellite’s kinetic energy is

$$
K
=
\frac{1}{2}mv^2.
$$

Using

$$
v^2=\frac{GM}{r},
$$

we obtain

$$
K
=
\frac{1}{2}m
\left(
\frac{GM}{r}
\right).
$$

Therefore,

$$
\boxed{
K
=
\frac{GMm}{2r}
}.
$$

The gravitational potential energy is

$$
U
=
-\frac{GMm}{r}.
$$

The total mechanical energy is therefore

$$
E=K+U.
$$

Substituting,

$$
E
=
\frac{GMm}{2r}
-
\frac{GMm}{r}.
$$

Thus,

$$
\boxed{
E
=
-\frac{GMm}{2r}
}.
$$

The total energy of a circular orbit is negative, confirming that the satellite is gravitationally bound.

The relationships among the energies are

$$
U=-2K
$$

and

$$
E=-K=\frac{U}{2}.
$$

## Newton’s Cannon and the Meaning of Orbit

Newton’s cannon is a thought experiment that illustrates what it means for an object to orbit Earth.

Imagine firing a cannonball horizontally from a sufficiently high mountain.

At a relatively low launch speed, the cannonball travels some distance before falling to Earth.

At a greater launch speed, it travels farther before reaching the surface.

At the appropriate speed, the cannonball falls toward Earth at the same rate that Earth’s curved surface falls away beneath it. The object then remains in continuous free fall around the planet.

This is an orbit.

An orbiting object is not free from gravity, and its acceleration is not zero. Gravity continually accelerates the object toward the center of Earth.

For a circular orbit, the object may move at constant **speed**, but its velocity continually changes direction. Its acceleration is the inward radial acceleration

$$
a_r
=
\frac{v^2}{r}.
$$

Using the circular-orbit speed,

$$
a_r
=
\frac{GM}{r^2},
$$

which is exactly the local gravitational acceleration.

## Kepler’s Laws of Planetary Motion

Johannes Kepler identified three empirical laws describing planetary motion.

### Kepler’s First Law

Each planet moves in an elliptical orbit, with the Sun located at one focus of the ellipse.

A circle is a special case of an ellipse. For a circular orbit, the two focal points coincide at the center.

### Kepler’s Second Law

A line connecting a planet to the Sun sweeps out equal areas during equal intervals of time.

This means that a planet does not generally move at constant speed in an elliptical orbit:

- The planet moves faster when it is closer to the Sun.
- The planet moves more slowly when it is farther from the Sun.

As the planet approaches the Sun, gravitational potential energy is converted into kinetic energy. As it moves away, kinetic energy is converted back into gravitational potential energy.

Kepler’s second law is also a consequence of conservation of angular momentum.

### Kepler’s Third Law

The square of a planet’s orbital period is proportional to the cube of the orbit’s semimajor axis:

$$
\boxed{
T^2\propto a^3
}.
$$

For a circular orbit, the semimajor axis $a$ is equal to the orbital radius $r$, so

$$
T^2\propto r^3.
$$

## Derivation of Kepler’s Third Law for a Circular Orbit

For a satellite of mass $m$ orbiting a dominant central mass $M$,

$$
G\frac{Mm}{r^2}
=
m\frac{v^2}{r}.
$$

Canceling $m$ gives

$$
v^2
=
\frac{GM}{r}.
$$

For uniform circular motion, the orbital speed is also

$$
v
=
\frac{2\pi r}{T},
$$

where $T$ is the orbital period.

Squaring,

$$
v^2
=
\frac{4\pi^2r^2}{T^2}.
$$

Substituting this into the gravitational-force result,

$$
\frac{4\pi^2r^2}{T^2}
=
\frac{GM}{r}.
$$

Multiplying by $rT^2$ gives

$$
4\pi^2r^3
=
GMT^2.
$$

Solving for $T^2$,

$$
\boxed{
T^2
=
\frac{4\pi^2}{GM}r^3
}.
$$

Equivalently,

$$
\boxed{
r^3
=
\frac{GM}{4\pi^2}T^2
}.
$$

For objects orbiting the same central body, the quantity

$$
\frac{T^2}{r^3}
$$

is constant.

## Worked Example: A Planet with an Eight-Year Period

Suppose a planet orbits the Sun with a period of eight Earth years:

$$
T_p=8T_E.
$$

We want to determine its orbital radius relative to Earth’s orbital radius.

For the planet,

$$
r_p^3
=
\frac{GM_\odot}{4\pi^2}T_p^2.
$$

For Earth,

$$
r_E^3
=
\frac{GM_\odot}{4\pi^2}T_E^2.
$$

Dividing the equations eliminates the common constants:

$$
\frac{r_p^3}{r_E^3}
=
\frac{T_p^2}{T_E^2}.
$$

Using

$$
T_p=8T_E,
$$

we obtain

$$
\frac{r_p^3}{r_E^3}
=
\frac{(8T_E)^2}{T_E^2}.
$$

Therefore,

$$
\frac{r_p^3}{r_E^3}=64.
$$

Taking the cube root,

$$
\frac{r_p}{r_E}=4.
$$

Thus,

$$
\boxed{
r_p=4r_E
}.
$$

Because Earth’s average orbital radius is one astronomical unit,

$$
\boxed{
r_p=4.0\ \mathrm{AU}
}.
$$

A planet with an eight-year orbital period would therefore have a circular-orbit radius four times Earth’s orbital radius.

## Geostationary Satellites

A **geostationary satellite** remains above the same point on Earth’s equator.

To do this, the satellite must:

- Move in a circular orbit
- Orbit above Earth’s equator
- Move in the same direction as Earth’s rotation
- Have an orbital period equal to Earth’s rotational period

Using the 24-hour approximation,

$$
T
=
24\ \mathrm{h}.
$$

Converting to seconds,

$$
T
=
24\ \mathrm{h}
\left(
\frac{60\ \mathrm{min}}{1\ \mathrm{h}}
\right)
\left(
\frac{60\ \mathrm{s}}{1\ \mathrm{min}}
\right).
$$

Therefore,

$$
T=86400\ \mathrm{s}.
$$

Let $h$ be the satellite’s altitude above Earth’s surface. Its orbital radius, measured from Earth’s center, is

$$
r=R_E+h.
$$

For this scalar radial equation, take inward as positive.

The gravitational force supplies the inward radial net force:

$$
\sum F_r=m a_r=m\frac{v^2}{R_E+h}=F_g.
$$

Substituting the gravitational-force magnitude gives

$$
G\frac{M_E m}{(R_E+h)^2}
=
m\frac{v^2}{R_E+h}.
$$

The satellite mass cancels:

$$
\frac{GM_E}{R_E+h}
=
v^2.
$$

The orbital speed is

$$
v
=
\frac{2\pi(R_E+h)}{T}.
$$

Squaring,

$$
v^2
=
\frac{
4\pi^2(R_E+h)^2
}{
T^2
}.
$$

Substituting into the gravitational equation gives

$$
\frac{
4\pi^2(R_E+h)^2
}{
T^2
}
=
\frac{GM_E}{R_E+h}.
$$

Multiplying by $(R_E+h)T^2$,

$$
4\pi^2(R_E+h)^3
=
GM_ET^2.
$$

Therefore,

$$
(R_E+h)^3
=
\frac{GM_ET^2}{4\pi^2}.
$$

Taking the cube root,

$$
R_E+h
=
\left(
\frac{GM_ET^2}{4\pi^2}
\right)^{1/3}.
$$

Solving for altitude,

$$
\boxed{
h
=
\left(
\frac{GM_ET^2}{4\pi^2}
\right)^{1/3}
-
R_E
}.
$$

Using

$$
G
=
6.67\times10^{-11}\ \mathrm{N}\,\mathrm{m}^2/\mathrm{kg}^2,
$$

$$
M_E
=
5.97\times10^{24}\ \mathrm{kg},
$$

$$
T
=
86400\ \mathrm{s},
$$

and

$$
R_E
\approx
6.37\times10^6\ \mathrm{m},
$$

the orbital radius is approximately

$$
R_E+h
\approx
4.22\times10^7\ \mathrm{m}.
$$

Subtracting Earth’s radius gives

$$
h
\approx
3.58\times10^7\ \mathrm{m}.
$$

Therefore,

$$
\boxed{
h\approx3.58\times10^4\ \mathrm{km}
}
$$

or

$$
\boxed{
h\approx35{,}800\ \mathrm{km}
}.
$$

A geostationary satellite is therefore much farther from Earth than a spacecraft in low Earth orbit. For comparison, the International Space Station orbits at an altitude of roughly $400\ \mathrm{km}$.

It is important to distinguish between:

- The **orbital radius**, measured from Earth’s center
- The **altitude**, measured from Earth’s surface

For a geostationary satellite,

$$
r_{\mathrm{orbit}}
\approx42{,}200\ \mathrm{km},
$$

while

$$
h
\approx35{,}800\ \mathrm{km}.
$$

## Summary

The gravitational force between two point masses is

$$
\boxed{
F_g
=
G\frac{m_1m_2}{r^2}
}.
$$

In vector form, with $\hat{r}$ directed outward,

$$
\boxed{
\vec{F}_g
=
-G\frac{m_1m_2}{r^2}\hat{r}
}.
$$

The gravitational acceleration produced by a mass $M$ is

$$
\boxed{
g(r)
=
\frac{GM}{r^2}
}.
$$

Near Earth’s surface,

$$
\boxed{
g\approx9.81\ \mathrm{m}/\mathrm{s}^2
}.
$$

The gravitational potential energy of two masses is

$$
\boxed{
U(r)
=
-\frac{GMm}{r}
}.
$$

For a circular orbit,

$$
\boxed{
v
=
\sqrt{\frac{GM}{r}}
}.
$$

The kinetic, potential, and total energies are

$$
\boxed{
K
=
\frac{GMm}{2r}
},
$$

$$
\boxed{
U
=
-\frac{GMm}{r}
},
$$

and

$$
\boxed{
E
=
-\frac{GMm}{2r}
}.
$$

Kepler’s third law for a circular orbit around a dominant central mass is

$$
\boxed{
T^2
=
\frac{4\pi^2}{GM}r^3
}.
$$

For two objects orbiting the same central mass,

$$
\boxed{
\frac{T_1^2}{r_1^3}
=
\frac{T_2^2}{r_2^3}
}.
$$

A geostationary satellite has an orbital period equal to Earth’s rotational period and an altitude of approximately

$$
\boxed{
h\approx35{,}800\ \mathrm{km}
}.
$$

An orbiting object remains in continuous free fall. Its acceleration is not zero; gravity continually changes the direction of its velocity and holds it in orbit.

---

Up Next: [Binary Stars and Three-Body Gravitational Orbits](../../2026-07-16-M3-2/Source/Lecture-Transcript.md)
Previous: [Rolling Motion and Conservation of Angular Momentum](../../../M2/2026-07-14-M2-5/Source/Lecture-Transcript.md)

---
