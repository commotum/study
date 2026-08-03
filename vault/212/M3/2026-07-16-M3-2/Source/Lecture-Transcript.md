# Physics 212: Binary Stars and Three-Body Gravitational Orbits

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 1X is currently open and is due Friday at 6:00 p.m. Complete it early enough to leave time to upload your written work to Gradescope.

Part D of Quiz 1X requires you to work with an instructor, a teaching assistant, or a physics staff member in the Wormhole. If the regularly scheduled assistance times do not work for you, consult the TA schedules in the Course Information module and email one of the listed TAs to arrange another time.

Quiz 2 will open Saturday and close Monday. The Zoom versions of Quiz 2 will be administered on Monday.

Check your Quiz 1 score to ensure that you have received credit. A handwritten note sheet with your photo ID visible must be submitted before Quiz 1 credit can be awarded. You should also be preparing your note sheet for Quiz 2.

## Review of Gravitation

In the previous lecture, we began studying gravitating and orbiting systems.

Any two massive objects exert equal-magnitude, opposite-direction gravitational forces on one another. The magnitude of the force between two point masses is

$$
F_g
=
G\frac{m_1m_2}{r_{12}^2},
$$

where:

- $G$ is the universal gravitational constant,
- $m_1$ and $m_2$ are the two masses, and
- $r_{12}$ is the distance between them.

The force is attractive and points along the line connecting the two masses.

If the radial unit vector points outward, the gravitational force may be written as

$$
\vec{F}_g
=
-G\frac{m_1m_2}{r_{12}^2}\hat{r}.
$$

The negative sign indicates that gravity points inward, opposite the outward radial direction.

## Gravitational Potential Energy

Force and potential energy are related by

$$
F_r=-\frac{dU}{dr}.
$$

For gravity,

$$
F_r
=
-G\frac{m_1m_2}{r^2}.
$$

Therefore,

$$
-\frac{dU}{dr}
=
-G\frac{m_1m_2}{r^2},
$$

so

$$
\frac{dU}{dr}
=
G\frac{m_1m_2}{r^2}.
$$

Integrating gives

$$
U(r)
=
-\frac{Gm_1m_2}{r}+C.
$$

We conventionally choose the potential energy to be zero when the masses are infinitely far apart:

$$
U(\infty)=0.
$$

This makes $C=0$, giving

$$
\boxed{
U(r)
=
-\frac{Gm_1m_2}{r}
}.
$$

The negative potential energy indicates that a gravitational system is bound relative to infinitely separated masses.

## Review of Kepler’s Laws

Kepler’s laws describe the motion of planets and other gravitationally bound systems.

### Kepler’s First Law

A planet follows an elliptical orbit, with the Sun located at one focus of the ellipse.

A circular orbit is a special case of an ellipse.

### Kepler’s Second Law

A line connecting a planet to the Sun sweeps out equal areas during equal intervals of time.

This reflects conservation of angular momentum.

### Kepler’s Third Law

The square of the orbital period is proportional to the cube of the orbit’s semimajor axis:

$$
T^2\propto a^3.
$$

For a circular orbit, the semimajor axis is simply the orbital radius:

$$
T^2\propto r^3.
$$

Today, we will apply these ideas to systems in which more than one object moves appreciably. In these systems, all of the objects orbit a common center of mass.

# Binary Star Systems

Consider two stars with masses $M$ and $m$, separated by a distance $d$.

Neither star remains stationary. Instead, both stars orbit their common center of mass.

The center of mass lies closer to the more massive star. The two stars remain on opposite sides of the center of mass and complete each orbit in the same amount of time.

They therefore have:

- The same orbital period
- The same angular velocity
- Different orbital radii
- Different linear speeds

## Center of Mass of a Binary System

Suppose the larger star has mass

$$
M=5.0\times10^{30}\ \mathrm{kg},
$$

and the smaller star has mass

$$
m=2.5\times10^{30}\ \mathrm{kg}.
$$

The larger star therefore has twice the mass of the smaller star:

$$
M=2m.
$$

Let the distance between the stars be

$$
d=3.0\times10^{12}\ \mathrm{m}.
$$

Choose the larger star as the origin:

$$
x_M=0,
$$

and place the smaller star at

$$
x_m=d.
$$

The center-of-mass position is

$$
x_{\mathrm{cm}}
=
\frac{Mx_M+mx_m}{M+m}.
$$

Substituting the positions,

$$
x_{\mathrm{cm}}
=
\frac{M(0)+m(d)}{M+m}.
$$

Since $M=2m$,

$$
x_{\mathrm{cm}}
=
\frac{md}{2m+m}.
$$

Therefore,

$$
\boxed{
x_{\mathrm{cm}}=\frac{d}{3}
}.
$$

The center of mass is one-third of the distance from the larger star toward the smaller star.

The larger star’s orbital radius is therefore

$$
\boxed{
r_M=\frac{d}{3}
},
$$

while the smaller star’s orbital radius is

$$
r_m=d-r_M.
$$

Thus,

$$
\boxed{
r_m=\frac{2d}{3}
}.
$$

These radii also satisfy

$$
Mr_M=mr_m.
$$

Because $M=2m$, the smaller star must orbit at twice the radius of the larger star.

## Orbital Period of the Binary System

We can find the period by analyzing either star. We will use the larger star.

The gravitational force supplies the centripetal force:

$$
F_g=F_c.
$$

The gravitational force between the stars is

$$
F_g
=
G\frac{Mm}{d^2}.
$$

The centripetal force on the larger star is

$$
F_c
=
M\frac{v_M^2}{r_M}.
$$

Setting these equal,

$$
G\frac{Mm}{d^2}
=
M\frac{v_M^2}{r_M}.
$$

Canceling $M$ gives

$$
G\frac{m}{d^2}
=
\frac{v_M^2}{r_M}.
$$

Using

$$
r_M=\frac{d}{3},
$$

we obtain

$$
G\frac{m}{d^2}
=
\frac{v_M^2}{d/3}.
$$

Solving for the speed,

$$
v_M^2
=
\frac{Gm}{3d}.
$$

Therefore,

$$
\boxed{
v_M=\sqrt{\frac{Gm}{3d}}
}.
$$

The larger star travels around a circle of radius $d/3$, so its speed is also

$$
v_M
=
\frac{2\pi r_M}{T}.
$$

Substituting $r_M=d/3$,

$$
v_M
=
\frac{2\pi d}{3T}.
$$

Squaring both sides gives

$$
v_M^2
=
\frac{4\pi^2d^2}{9T^2}.
$$

Equating the two expressions for $v_M^2$,

$$
\frac{4\pi^2d^2}{9T^2}
=
\frac{Gm}{3d}.
$$

Solving for $T^2$ gives

$$
T^2
=
\frac{4\pi^2d^3}{3Gm}.
$$

Therefore,

$$
\boxed{
T
=
2\pi\sqrt{\frac{d^3}{3Gm}}
}.
$$

Because

$$
M+m=3m,
$$

this can also be written as

$$
\boxed{
T
=
2\pi\sqrt{\frac{d^3}{G(M+m)}}
}.
$$

This is the two-body form of Kepler’s third law.

Substituting the numerical values,

$$
T
=
2\pi
\sqrt{
\frac{
\left(3.0\times10^{12}\ \mathrm{m}\right)^3
}{
3
\left(6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}\right)
\left(2.5\times10^{30}\ \mathrm{kg}\right)
}
}.
$$

This gives approximately

$$
T\approx1.46\times10^9\ \mathrm{s}.
$$

Converting to years,

$$
\boxed{
T\approx46\ \mathrm{years}
}.
$$

Both stars have this same period, even though their orbital radii and linear speeds are different.

# Three Equal Masses in an Equilateral Triangle

Now consider three identical objects, each with mass $m$, positioned at the corners of an equilateral triangle.

Let the distance between each pair of masses be $L$.

The masses are not physically connected. They are held in the triangular arrangement by their mutual gravitational attraction and orbit their common center of mass.

Because the masses and geometry are symmetric, the center of mass is at the geometric center of the triangle.

Each mass follows a circular path around that point.

## Distance from Each Mass to the Center

The altitude of an equilateral triangle is

$$
h=\frac{\sqrt{3}}{2}L.
$$

The centroid lies two-thirds of the way from a vertex along a median. Therefore, the orbital radius of each mass is

$$
R=\frac{2}{3}h.
$$

Substituting the altitude,

$$
R
=
\frac{2}{3}
\left(
\frac{\sqrt{3}}{2}L
\right).
$$

Thus,

$$
R=\frac{\sqrt{3}}{3}L,
$$

or equivalently,

$$
\boxed{
R=\frac{L}{\sqrt{3}}
}.
$$

## Net Gravitational Force on One Mass

Choose the mass at the top vertex.

Each of the other two masses exerts a gravitational force of magnitude

$$
F_g
=
G\frac{m^2}{L^2}.
$$

The two forces are symmetric.

Their tangential components cancel, while their inward radial components add. Each force makes an angle of $30^\circ$ with the inward radial direction.

The net force is therefore

$$
F_{\mathrm{net}}
=
2F_g\cos(30^\circ).
$$

Substituting the gravitational force,

$$
F_{\mathrm{net}}
=
2
\left(
G\frac{m^2}{L^2}
\right)
\cos(30^\circ).
$$

Because

$$
\cos(30^\circ)=\frac{\sqrt{3}}{2},
$$

we obtain

$$
F_{\mathrm{net}}
=
2
\left(
G\frac{m^2}{L^2}
\right)
\left(
\frac{\sqrt{3}}{2}
\right).
$$

Therefore,

$$
\boxed{
F_{\mathrm{net}}
=
\sqrt{3}\frac{Gm^2}{L^2}
}.
$$

The force points directly toward the center of the triangle.

Using the numerical values supplied in the activity gives approximately

$$
\boxed{
F_{\mathrm{net}}
\approx2.2\times10^{26}\ \mathrm{N}
}.
$$

Because

$$
1\ \mathrm{YN}=10^{24}\ \mathrm{N},
$$

this is equivalent to approximately

$$
\boxed{
F_{\mathrm{net}}\approx220\ \mathrm{YN}
}.
$$

## Orbital Speed of Each Mass

The net gravitational force supplies the centripetal force:

$$
F_{\mathrm{net}}
=
\frac{mv^2}{R}.
$$

Using the net force found above,

$$
\sqrt{3}\frac{Gm^2}{L^2}
=
\frac{mv^2}{R}.
$$

The orbital radius is

$$
R=\frac{L}{\sqrt{3}}.
$$

Substituting,

$$
\sqrt{3}\frac{Gm^2}{L^2}
=
\frac{mv^2}{L/\sqrt{3}}.
$$

The right side may be written as

$$
\frac{mv^2}{L/\sqrt{3}}
=
\frac{\sqrt{3}mv^2}{L}.
$$

Therefore,

$$
\sqrt{3}\frac{Gm^2}{L^2}
=
\sqrt{3}\frac{mv^2}{L}.
$$

Canceling $\sqrt{3}$ and one factor of $m$ gives

$$
\frac{Gm}{L^2}
=
\frac{v^2}{L}.
$$

Multiplying by $L$,

$$
v^2=\frac{Gm}{L}.
$$

Thus,

$$
\boxed{
v=\sqrt{\frac{Gm}{L}}
}.
$$

Using the numerical values supplied in the activity gives

$$
\boxed{
v\approx9.7\times10^3\ \mathrm{m/s}
}.
$$

Each mass moves at approximately $9.7\ \mathrm{km/s}$ around the common center of mass.

# Total Energy of the Three-Mass System

The total mechanical energy is

$$
E_{\mathrm{total}}
=
K_{\mathrm{total}}
+
U_{\mathrm{total}}.
$$

We must include the kinetic energy of all three masses and the gravitational potential energy of every unique pair.

## Total Kinetic Energy

Each mass has kinetic energy

$$
K=\frac{1}{2}mv^2.
$$

Since there are three masses,

$$
K_{\mathrm{total}}
=
3\left(\frac{1}{2}mv^2\right).
$$

Therefore,

$$
K_{\mathrm{total}}
=
\frac{3}{2}mv^2.
$$

We found that

$$
v^2=\frac{Gm}{L}.
$$

Substituting,

$$
K_{\mathrm{total}}
=
\frac{3}{2}m
\left(
\frac{Gm}{L}
\right).
$$

Thus,

$$
\boxed{
K_{\mathrm{total}}
=
\frac{3Gm^2}{2L}
}.
$$

## Total Gravitational Potential Energy

There are three unique pairs of masses:

1. Mass 1 and mass 2
2. Mass 1 and mass 3
3. Mass 2 and mass 3

Each pair is separated by $L$, so each pair contributes

$$
U_{\mathrm{pair}}
=
-\frac{Gm^2}{L}.
$$

The total potential energy is therefore

$$
U_{\mathrm{total}}
=
3
\left(
-\frac{Gm^2}{L}
\right).
$$

Thus,

$$
\boxed{
U_{\mathrm{total}}
=
-\frac{3Gm^2}{L}
}.
$$

Each pair is counted only once. Counting both $U_{12}$ and $U_{21}$ would count the same interaction twice.

## Total Mechanical Energy

Combining the kinetic and potential energies,

$$
E_{\mathrm{total}}
=
\frac{3Gm^2}{2L}
-
\frac{3Gm^2}{L}.
$$

Writing both terms with a common denominator,

$$
E_{\mathrm{total}}
=
\frac{3Gm^2}{2L}
-
\frac{6Gm^2}{2L}.
$$

Therefore,

$$
\boxed{
E_{\mathrm{total}}
=
-\frac{3Gm^2}{2L}
}.
$$

Using the numerical values supplied in the activity gives approximately

$$
\boxed{
E_{\mathrm{total}}
\approx-3.5\times10^{38}\ \mathrm{J}
}.
$$

The negative total energy indicates that the system is gravitationally bound.

The kinetic energy is positive:

$$
K_{\mathrm{total}}
=
\frac{3Gm^2}{2L},
$$

but the magnitude of the negative potential energy is larger:

$$
\left|U_{\mathrm{total}}\right|
=
\frac{3Gm^2}{L}
=
2K_{\mathrm{total}}.
$$

Consequently,

$$
E_{\mathrm{total}}
=
-K_{\mathrm{total}}.
$$

An amount of energy equal to

$$
\left|E_{\mathrm{total}}\right|
=
\frac{3Gm^2}{2L}
$$

would have to be supplied to separate the masses infinitely far from one another with zero final kinetic energy. This magnitude is the system’s binding energy.

# General Strategy for Multi-Body Orbital Problems

When solving a gravitational orbital problem involving several moving objects, use the following approach.

## 1. Locate the Center of Mass

For discrete masses,

$$
\vec{R}_{\mathrm{cm}}
=
\frac{
\sum_i m_i\vec{r}_i
}{
\sum_i m_i
}.
$$

The objects orbit this common center of mass when no external force acts on the system.

## 2. Determine Each Orbital Radius

The orbital radius of an object is its distance from the center of mass, not necessarily its distance from another object.

In the binary system, the gravitational-force separation was $d$, while the larger star’s orbital radius was $d/3$. These distances must not be confused.

## 3. Draw a Free-Body Diagram

Include every gravitational force acting on the selected object.

Use symmetry to determine which force components cancel and which add.

## 4. Find the Net Radial Force

For circular motion,

$$
F_{\mathrm{net},r}
=
\frac{mv^2}{R}.
$$

The radial coordinate points toward the center of the circular orbit.

## 5. Relate Speed and Period

For uniform circular motion,

$$
v=\frac{2\pi R}{T}.
$$

This allows the orbital period to be found after the speed or centripetal-force equation has been determined.

## 6. Count Energy Terms Carefully

The total kinetic energy includes one term for each moving object:

$$
K_{\mathrm{total}}
=
\sum_i\frac{1}{2}m_iv_i^2.
$$

The total gravitational potential energy includes one term for each unique pair:

$$
U_{\mathrm{total}}
=
-\sum_{i<j}
\frac{Gm_im_j}{r_{ij}}.
$$

The condition $i<j$ ensures that each pair is counted only once.

# Summary

The gravitational force and potential energy between two point masses are

$$
F_g
=
G\frac{m_1m_2}{r^2}
$$

and

$$
U
=
-\frac{Gm_1m_2}{r}.
$$

In a binary system, both objects orbit their common center of mass. For two stars of masses $M$ and $m$ separated by $d$,

$$
r_M=\frac{m}{M+m}d
$$

and

$$
r_m=\frac{M}{M+m}d.
$$

The orbital period is

$$
\boxed{
T
=
2\pi\sqrt{\frac{d^3}{G(M+m)}}
}.
$$

For the binary system studied in this lecture,

$$
\boxed{
T\approx46\ \mathrm{years}
}.
$$

For three equal masses located at the corners of an equilateral triangle of side length $L$, the orbital radius of each mass is

$$
\boxed{
R=\frac{L}{\sqrt{3}}
}.
$$

The net force on each mass is

$$
\boxed{
F_{\mathrm{net}}
=
\sqrt{3}\frac{Gm^2}{L^2}
}.
$$

The orbital speed is

$$
\boxed{
v=\sqrt{\frac{Gm}{L}}
}.
$$

The total kinetic energy is

$$
\boxed{
K_{\mathrm{total}}
=
\frac{3Gm^2}{2L}
},
$$

the total potential energy is

$$
\boxed{
U_{\mathrm{total}}
=
-\frac{3Gm^2}{L}
},
$$

and the total mechanical energy is

$$
\boxed{
E_{\mathrm{total}}
=
-\frac{3Gm^2}{2L}
}.
$$

The negative total energy confirms that the three masses form a gravitationally bound system.

---

Up Next: [Oscillations and Simple Harmonic Motion](../../../M4/2026-07-21-M4-1/Source/Lecture-Transcript.md)
Previous: [Newtonian Gravitation, Kepler’s Laws, and Orbital Motion](../../2026-07-15-M3-1/Source/Lecture-Transcript.md)

---
