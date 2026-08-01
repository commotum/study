# Physics 212: Phase Difference and Two-Source Interference

Welcome back to Physics 212.

## Announcements

Quiz 2 scores have been posted, and the optional Quiz 2X assignment is available. Quiz 2X is due Tuesday at 6:00 p.m.

Quiz 3 covers the wave material presented since Quiz 2, including today’s lecture. Continue preparing your handwritten note sheet.

The Quiz 3 schedule is:

- Proctorio opens Saturday at 5:00 p.m.
- Proctorio closes Monday at 5:00 p.m.
- Zoom-proctored sessions will be offered Monday at 11:00 a.m. and 6:00 p.m.

Beats will not be covered further in lecture and will not appear on Quiz 3.

# Review: Superposition and Interference

The **principle of superposition** states that when waves overlap, their displacements add:

$$
\boxed{
D_{\mathrm{net}}
=
D_1+D_2
}.
$$

The resulting interference depends on the relative phase of the waves.

## Constructive Interference

Constructive interference occurs when corresponding parts of the waves align.

For example:

- A crest meets another crest.
- A trough meets another trough.
- A compression meets another compression.
- A rarefaction meets another rarefaction.

For two identical waves, complete constructive interference produces the maximum possible oscillation amplitude.

A point of complete constructive interference is not always located at a crest. The displacement still changes with time. Instead, the point experiences the greatest possible oscillation amplitude.

## Destructive Interference

Destructive interference occurs when opposite parts of the waves align.

For example:

- A crest meets a trough.
- A compression meets a rarefaction.

If the waves have equal amplitudes and are exactly out of phase, they undergo complete destructive interference and cancel.

# Interference from Two Sound Sources

Consider two speakers emitting sound waves with the same frequency and phase.

In a sound-wave simulation:

- A light ring may represent a compression.
- A dark ring may represent a rarefaction.
- Lines along which the waves cancel are positions of destructive interference.
- Regions halfway between those lines may represent constructive interference.

The result is a spatial interference pattern containing alternating regions of large and small oscillation amplitude.

A randomly selected position does not necessarily exhibit complete constructive or complete destructive interference. The waves may arrive with some intermediate phase difference and interfere only partially.

## Graphical Example

Suppose circular wavefronts represent crests produced by two in-phase sources.

At a particular instant:

- Point $P$ lies where two crests meet.
- Point $Q$ lies where a crest meets a trough.
- Point $R$ lies where two troughs meet.

Therefore:

$$
\boxed{
P\text{ and }R
\text{ are positions of complete constructive interference}
}
$$

and

$$
\boxed{
Q
\text{ is a position of complete destructive interference}
}.
$$

Both crest–crest and trough–trough combinations are constructive because the displacements have the same sign.

# Phase of a Sinusoidal Wave

A sinusoidal traveling wave may be written as

$$
\boxed{
D(x,t)
=
A\sin(kx-\omega t+\phi_0)
},
$$

where:

- $A$ is the amplitude,
- $k$ is the wave number,
- $\omega$ is the angular frequency, and
- $\phi_0$ is the initial phase.

The complete argument of the sine function is the wave’s phase:

$$
\boxed{
\phi(x,t)
=
kx-\omega t+\phi_0
}.
$$

The initial phase $\phi_0$ describes the phase at the origin when $t=0$.

The wave number is

$$
\boxed{
k=\frac{2\pi}{\lambda}
},
$$

where $\lambda$ is the wavelength.

# Phase Difference Along a Single Wave

Consider two positions $x_1$ and $x_2$ along the same wave.

The displacements are

$$
D(x_1,t)
=
A\sin(kx_1-\omega t+\phi_0)
$$

and

$$
D(x_2,t)
=
A\sin(kx_2-\omega t+\phi_0).
$$

The phases at the two positions are

$$
\phi_1
=
kx_1-\omega t+\phi_0
$$

and

$$
\phi_2
=
kx_2-\omega t+\phi_0.
$$

The phase difference is

$$
\Delta\phi
=
\phi_2-\phi_1.
$$

Substituting the two phases gives

$$
\Delta\phi
=
\left(
kx_2-\omega t+\phi_0
\right)
-
\left(
kx_1-\omega t+\phi_0
\right).
$$

The time and initial-phase terms cancel:

$$
\Delta\phi
=
kx_2-kx_1.
$$

Therefore,

$$
\Delta\phi
=
k(x_2-x_1).
$$

Defining

$$
\Delta x=x_2-x_1,
$$

we obtain

$$
\boxed{
\Delta\phi=k\Delta x
}.
$$

Using

$$
k=\frac{2\pi}{\lambda},
$$

the phase difference may also be written as

$$
\boxed{
\Delta\phi
=
\frac{2\pi\Delta x}{\lambda}
}.
$$

Thus, the phase difference between two points on the same wave depends on their separation as a fraction of the wavelength.

For example:

- If $\Delta x=\lambda$, then $\Delta\phi=2\pi$.
- If $\Delta x=\lambda/2$, then $\Delta\phi=\pi$.
- If $\Delta x=\lambda/4$, then $\Delta\phi=\pi/2$.

# Phase Difference from Two Sources

Now consider two waves produced by separate sources.

Assume the waves have the same frequency and wavelength but may have different initial phases and may travel different distances before reaching the observation point.

The first wave may be written as

$$
D_1
=
A\sin(kr_1-\omega t+\phi_{1,0}),
$$

and the second wave as

$$
D_2
=
A\sin(kr_2-\omega t+\phi_{2,0}),
$$

where:

- $r_1$ is the distance traveled by wave 1,
- $r_2$ is the distance traveled by wave 2,
- $\phi_{1,0}$ is the initial phase of source 1, and
- $\phi_{2,0}$ is the initial phase of source 2.

The phase difference at the observation point is

$$
\Delta\phi
=
\left(
kr_2-\omega t+\phi_{2,0}
\right)
-
\left(
kr_1-\omega t+\phi_{1,0}
\right).
$$

The time terms cancel:

$$
\Delta\phi
=
k(r_2-r_1)
+
\left(
\phi_{2,0}-\phi_{1,0}
\right).
$$

Define the path difference as

$$
\boxed{
\Delta r=r_2-r_1
}
$$

and the initial phase difference as

$$
\boxed{
\Delta\phi_0
=
\phi_{2,0}-\phi_{1,0}
}.
$$

The general phase-difference equation is therefore

$$
\boxed{
\Delta\phi
=
k\Delta r+\Delta\phi_0
}.
$$

Using

$$
k=\frac{2\pi}{\lambda},
$$

we obtain

$$
\boxed{
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}
+
\Delta\phi_0
}.
$$

This equation accounts for two independent sources of phase difference:

1. The waves may begin with different phases.
2. The waves may travel different distances.

Both effects must be included.

# Conditions for Complete Interference

## Complete Constructive Interference

Complete constructive interference occurs when the waves arrive with a phase difference equal to an integer multiple of $2\pi$:

$$
\boxed{
\Delta\phi=2\pi m
},
$$

where

$$
m=0,\pm1,\pm2,\ldots
$$

Equivalent constructive phase differences include

$$
0,\ 2\pi,\ 4\pi,\ 6\pi,\ldots
$$

## Complete Destructive Interference

Complete destructive interference occurs when the waves arrive with an odd multiple of $\pi$ phase difference:

$$
\boxed{
\Delta\phi=(2m+1)\pi
}.
$$

This may also be written as

$$
\boxed{
\Delta\phi
=
2\pi
\left(
m+\frac{1}{2}
\right)
}.
$$

Equivalent destructive phase differences include

$$
\pi,\ 3\pi,\ 5\pi,\ 7\pi,\ldots
$$

## Initial Phase Difference

If the sources begin in phase,

$$
\boxed{
\Delta\phi_0=0
}.
$$

If the sources begin completely out of phase,

$$
\boxed{
\Delta\phi_0=\pi
}.
$$

A source phase difference of $\pi$ reverses the usual relationship between path difference and interference.

For in-phase sources:

$$
\Delta r=m\lambda
\quad\Longrightarrow\quad
\text{constructive interference}
$$

and

$$
\Delta r
=
\left(
m+\frac{1}{2}
\right)\lambda
\quad\Longrightarrow\quad
\text{destructive interference}.
$$

For sources that begin $\pi$ radians out of phase:

$$
\Delta r=m\lambda
\quad\Longrightarrow\quad
\text{destructive interference}
$$

and

$$
\Delta r
=
\left(
m+\frac{1}{2}
\right)\lambda
\quad\Longrightarrow\quad
\text{constructive interference}.
$$

# Worked Example: Two Out-of-Phase Radio Antennas

Two radio antennas are separated by

$$
d=600\ \mathrm{m}.
$$

A point $P$ is located

$$
r_1=800\ \mathrm{m}
$$

from the first antenna.

The antennas transmit at

$$
f=3.0\times10^6\ \mathrm{Hz}
$$

and begin completely out of phase:

$$
\Delta\phi_0=\pi.
$$

Determine whether point $P$ experiences complete constructive interference, complete destructive interference, or neither.

## 1. Identify the Wave Speed

Radio waves are electromagnetic waves, so they travel at approximately the speed of light:

$$
\boxed{
c=3.0\times10^8\ \mathrm{m/s}
}.
$$

## 2. Find the Second Path Length

The geometry forms a right triangle:

$$
r_2
=
\sqrt{r_1^2+d^2}.
$$

Substituting,

$$
r_2
=
\sqrt{
(800\ \mathrm{m})^2
+
(600\ \mathrm{m})^2
}.
$$

Therefore,

$$
r_2=1000\ \mathrm{m}.
$$

## 3. Find the Path Difference

The path difference is

$$
\Delta r=r_2-r_1.
$$

Thus,

$$
\Delta r
=
1000\ \mathrm{m}
-
800\ \mathrm{m}.
$$

Therefore,

$$
\boxed{
\Delta r=200\ \mathrm{m}
}.
$$

## 4. Find the Wavelength

Using

$$
c=\lambda f,
$$

the wavelength is

$$
\lambda=\frac{c}{f}.
$$

Substituting,

$$
\lambda
=
\frac{
3.0\times10^8\ \mathrm{m/s}
}{
3.0\times10^6\ \mathrm{s^{-1}}
}.
$$

Therefore,

$$
\boxed{
\lambda=100\ \mathrm{m}
}.
$$

The path difference is therefore two wavelengths:

$$
\Delta r=2\lambda.
$$

## 5. Find the Total Phase Difference

Use

$$
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}
+
\Delta\phi_0.
$$

Substituting,

$$
\Delta\phi
=
2\pi
\left(
\frac{200\ \mathrm{m}}{100\ \mathrm{m}}
\right)
+
\pi.
$$

Therefore,

$$
\Delta\phi
=
4\pi+\pi.
$$

Thus,

$$
\boxed{
\Delta\phi=5\pi
}.
$$

Because $5\pi$ is an odd multiple of $\pi$, point $P$ experiences

$$
\boxed{
\text{complete destructive interference}
}.
$$

If the initial phase difference had been omitted, the calculation would have produced $4\pi$ and incorrectly predicted constructive interference. The initial phases of the sources must be included.

# Worked Example: Phase Difference from Two Flutes

Two in-phase flutes emit sound at

$$
f=830\ \mathrm{Hz}.
$$

The flutes are positioned on opposite sides of the $y$-axis, and point $P$ lies on the $y$-axis.

Let:

- $x_1$ be the horizontal distance from flute 1 to the $y$-axis,
- $x_2$ be the horizontal distance from flute 2 to the $y$-axis, and
- $y$ be the vertical coordinate of point $P$.

Because the sources are in phase,

$$
\Delta\phi_0=0.
$$

## 1. Find the Two Path Lengths

The distance from flute 1 to point $P$ is

$$
r_1
=
\sqrt{x_1^2+y^2}.
$$

The distance from flute 2 to point $P$ is

$$
r_2
=
\sqrt{x_2^2+y^2}.
$$

Therefore, the path difference is

$$
\Delta r
=
r_2-r_1.
$$

Thus,

$$
\boxed{
\Delta r
=
\sqrt{x_2^2+y^2}
-
\sqrt{x_1^2+y^2}
}.
$$

## 2. Write the Phase-Difference Equation

The wavelength is related to the frequency and sound speed by

$$
v=\lambda f.
$$

Therefore,

$$
\frac{1}{\lambda}
=
\frac{f}{v}.
$$

Because the sources are in phase,

$$
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}.
$$

Substituting $1/\lambda=f/v$ gives

$$
\Delta\phi
=
\frac{2\pi f}{v}\Delta r.
$$

Therefore,

$$
\boxed{
\Delta\phi
=
\frac{2\pi f}{v}
\left[
\sqrt{x_2^2+y^2}
-
\sqrt{x_1^2+y^2}
\right]
}.
$$

Using the speed of sound

$$
v=343\ \mathrm{m/s}
$$

and the coordinates supplied in the lecture diagram gives

$$
\boxed{
\Delta\phi\approx66\ \mathrm{rad}
}.
$$

Phase differences that differ by an integer multiple of $2\pi$ describe the same relative phase.

Reducing $66\ \mathrm{rad}$ to one cycle gives

$$
66\ \mathrm{rad}
\equiv
3.17\ \mathrm{rad}
\pmod{2\pi}.
$$

# Worked Example: First Maximum Along the Positive Axis

Two in-phase speakers are arranged as follows:

- Speaker $A$ is at the origin.
- Speaker $B$ is a vertical distance $y$ below the origin.
- The observation point lies a distance $x$ along the positive $x$-axis.

The speakers have wavelength

$$
\lambda=0.500\ \mathrm{m},
$$

and their vertical separation is

$$
y=2.20\ \mathrm{m}.
$$

Determine the first position encountered along the positive $x$-axis where the sound intensity is a maximum.

A maximum sound intensity requires complete constructive interference.

## 1. Write the Constructive-Interference Condition

Because the sources are in phase,

$$
\Delta\phi_0=0.
$$

The phase difference is

$$
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}.
$$

For complete constructive interference,

$$
\Delta\phi=2\pi m.
$$

Therefore,

$$
2\pi m
=
\frac{2\pi\Delta r}{\lambda}.
$$

Canceling $2\pi$ gives

$$
m=\frac{\Delta r}{\lambda}.
$$

Thus,

$$
\boxed{
\Delta r=m\lambda
}.
$$

The path difference must be an integer multiple of the wavelength.

## 2. Express the Path Difference Geometrically

The distance from speaker $A$ to the observation point is

$$
r_1=x.
$$

The distance from speaker $B$ to the observation point is

$$
r_2
=
\sqrt{x^2+y^2}.
$$

Therefore,

$$
\Delta r
=
r_2-r_1,
$$

so

$$
\Delta r
=
\sqrt{x^2+y^2}-x.
$$

Applying the constructive-interference condition,

$$
\sqrt{x^2+y^2}-x
=
m\lambda.
$$

## 3. Solve for $x$

Add $x$ to both sides:

$$
\sqrt{x^2+y^2}
=
x+m\lambda.
$$

Square both sides:

$$
x^2+y^2
=
\left(
x+m\lambda
\right)^2.
$$

Expanding,

$$
x^2+y^2
=
x^2
+
2m\lambda x
+
m^2\lambda^2.
$$

Cancel $x^2$:

$$
y^2
=
2m\lambda x
+
m^2\lambda^2.
$$

Solving for $x$ gives

$$
2m\lambda x
=
y^2-m^2\lambda^2,
$$

so

$$
\boxed{
x
=
\frac{
y^2-m^2\lambda^2
}{
2m\lambda
}
}.
$$

This can also be written as

$$
\boxed{
x
=
\frac{y^2}{2m\lambda}
-
\frac{m\lambda}{2}
}.
$$

The value $m=0$ does not produce a finite solution in this geometry, so begin with $m=1$.

## 4. Evaluate the Allowed Values of $m$

Using

$$
y=2.20\ \mathrm{m}
$$

and

$$
\lambda=0.500\ \mathrm{m},
$$

the position becomes

$$
x
=
\frac{
(2.20\ \mathrm{m})^2
}{
2m(0.500\ \mathrm{m})
}
-
\frac{
m(0.500\ \mathrm{m})
}{
2
}.
$$

Simplifying,

$$
x
=
\frac{4.84}{m}
-
0.250m
\quad\mathrm{m}.
$$

The possible positions are:

| $m$ | $x$ |
|---:|---:|
| $1$ | $4.59\ \mathrm{m}$ |
| $2$ | $1.92\ \mathrm{m}$ |
| $3$ | $0.863\ \mathrm{m}$ |
| $4$ | $0.210\ \mathrm{m}$ |
| $5$ | $-0.282\ \mathrm{m}$ |
| $6$ | $-0.693\ \mathrm{m}$ |

We want the first maximum encountered while moving from the origin in the positive $x$-direction. Therefore, we need the smallest positive value of $x$.

That occurs for

$$
m=4.
$$

Thus,

$$
\boxed{
x\approx0.21\ \mathrm{m}
}.
$$

Values $m\geq5$ produce negative positions and therefore do not apply to the requested region.

# Strategy for Two-Source Interference Problems

## 1. Identify the Type of Wave

Determine the appropriate wave speed.

For sound in air under typical conditions,

$$
\boxed{
v_{\mathrm{sound}}\approx343\ \mathrm{m/s}
}.
$$

For electromagnetic waves in vacuum or air,

$$
\boxed{
c\approx3.0\times10^8\ \mathrm{m/s}
}.
$$

## 2. Determine the Wavelength

Use

$$
\boxed{
v=\lambda f
}
$$

or

$$
\boxed{
\lambda=\frac{v}{f}
}.
$$

## 3. Find the Path Difference

Calculate the distance from each source to the observation point:

$$
r_1
\quad\text{and}\quad
r_2.
$$

Then compute

$$
\boxed{
\Delta r=r_2-r_1
}.
$$

Use the same ordering throughout the calculation.

## 4. Determine the Initial Phase Difference

For in-phase sources,

$$
\Delta\phi_0=0.
$$

For completely out-of-phase sources,

$$
\Delta\phi_0=\pi.
$$

Do not omit this term.

## 5. Calculate the Total Phase Difference

Use

$$
\boxed{
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}
+
\Delta\phi_0
}.
$$

## 6. Classify the Interference

Constructive interference occurs when

$$
\boxed{
\Delta\phi=2\pi m
}.
$$

Destructive interference occurs when

$$
\boxed{
\Delta\phi=(2m+1)\pi
}.
$$

If neither condition is satisfied, the interference is partial.

# Summary

For a sinusoidal traveling wave,

$$
\boxed{
D(x,t)
=
A\sin(kx-\omega t+\phi_0)
}.
$$

The phase is

$$
\boxed{
\phi
=
kx-\omega t+\phi_0
}.
$$

The wave number is

$$
\boxed{
k=\frac{2\pi}{\lambda}
}.
$$

The phase difference between two points on the same wave is

$$
\boxed{
\Delta\phi
=
k\Delta x
=
\frac{2\pi\Delta x}{\lambda}
}.
$$

For two separate sources, the total phase difference at an observation point is

$$
\boxed{
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}
+
\Delta\phi_0
}.
$$

The path difference is

$$
\boxed{
\Delta r=r_2-r_1
},
$$

and the initial phase difference is

$$
\boxed{
\Delta\phi_0
=
\phi_{2,0}-\phi_{1,0}
}.
$$

Complete constructive interference occurs when

$$
\boxed{
\Delta\phi=2\pi m
}.
$$

Complete destructive interference occurs when

$$
\boxed{
\Delta\phi=(2m+1)\pi
}.
$$

For in-phase sources, constructive interference requires

$$
\boxed{
\Delta r=m\lambda
}.
$$

For sources that begin $\pi$ radians out of phase, a path difference of an integer number of wavelengths instead produces destructive interference.

Both the path difference and the initial source phase must be included when determining the interference at an observation point.