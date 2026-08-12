# Physics 212: Traveling Waves, Refraction, and Intensity

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 2 is nearly finished being graded. The grades should be posted by the end of today, along with the Quiz 2X assignment.

Quiz 2X will close on Thursday rather than Friday because the Wormhole is not open on Fridays during the summer term. This will give students an opportunity to receive help before the assignment closes.

A sign-up sheet for evening TA assistance will be available in the TA Information module. Please sign up at least 24 hours in advance whenever possible so that the TAs have sufficient notice.

## Review: Mechanical Waves

In the previous lecture, we introduced several fundamental properties of waves.

A **wave** is a disturbance that propagates through space. A mechanical wave can be understood as a collection of coupled oscillators. Each particle of the medium oscillates locally while the overall disturbance travels through the medium.

We discussed two principal types of mechanical waves.

### Transverse Waves

In a transverse wave, the particles of the medium oscillate perpendicular to the direction of wave propagation.

A wave traveling along a horizontal string is a common example. The wave may propagate horizontally while each small element of the string moves vertically.

### Longitudinal Waves

In a longitudinal wave, the particles of the medium oscillate parallel and antiparallel to the direction of wave propagation.

Sound in air is a longitudinal wave. Air molecules oscillate back and forth along the same axis on which the sound wave propagates, producing alternating regions of compression and rarefaction.

We also discussed waves traveling along strings. For a string, tension supplies the restoring force that allows a disturbance to propagate.

## From an Oscillator to a Traveling Wave

The position of a simple harmonic oscillator can be written as

$$
x(t)=A\cos(\omega t+\phi_0),
$$

where:

- $A$ is the amplitude,
- $\omega$ is the angular frequency,
- $\phi_0$ is the initial phase, and
- $x(t)$ is the displacement from equilibrium.

This function depends only on time. It describes the motion of one oscillator.

A sinusoidal traveling wave depends on both position and time. A wave traveling in the positive $x$-direction can be written as

$$
y(x,t)=A\sin(kx-\omega t+\phi_0),
$$

where:

- $y(x,t)$ is the displacement of the medium,
- $A$ is the wave amplitude,
- $k$ is the wave number,
- $\omega$ is the angular frequency, and
- $\phi_0$ is the initial phase.

Sine and cosine functions describe the same general type of wave. They differ only by a phase shift.

## Wave Number and Angular Frequency

The wave number is

$$
\boxed{
k=\frac{2\pi}{\lambda}
},
$$

where $\lambda$ is the wavelength.

The wave number may be interpreted as a spatial angular frequency. It describes how rapidly the wave’s phase changes with position and has units of radians per meter.

The angular frequency is

$$
\boxed{
\omega=2\pi f=\frac{2\pi}{T}
},
$$

where:

- $f$ is the frequency,
- $T$ is the period, and
- $\omega$ has units of radians per second.

The frequency describes how rapidly the oscillation repeats in time, while the wave number describes how rapidly the wave pattern repeats in space.

## Wave Speed

During one period, a traveling wave advances by one wavelength. Therefore,

$$
v_{\mathrm{wave}}=\frac{\lambda}{T}.
$$

Because

$$
f=\frac{1}{T},
$$

we can also write

$$
\boxed{
v_{\mathrm{wave}}=f\lambda
}.
$$

Using

$$
\omega=\frac{2\pi}{T}
$$

and

$$
k=\frac{2\pi}{\lambda},
$$

the wave speed may also be written as

$$
\boxed{
v_{\mathrm{wave}}=\frac{\omega}{k}
}.
$$

These are equivalent forms of the wave-speed relationship:

$$
\boxed{
v_{\mathrm{wave}}
=
\frac{\lambda}{T}
=
f\lambda
=
\frac{\omega}{k}
}.
$$

## Direction of a Traveling Wave

Consider the phase of the wave

$$
\phi=kx-\omega t+\phi_0.
$$

To follow a particular point of constant phase, set

$$
kx-\omega t+\phi_0=C,
$$

where $C$ is a constant.

Solving for $x$ gives

$$
x
=
\frac{\omega}{k}t
+
\frac{C-\phi_0}{k}.
$$

The velocity of this constant-phase point is

$$
\frac{dx}{dt}
=
\frac{\omega}{k}.
$$

Because both $\omega$ and $k$ are positive,

$$
\frac{dx}{dt}>0.
$$

Therefore,

$$
\boxed{
y(x,t)=A\sin(kx-\omega t+\phi_0)
}
$$

describes a wave traveling in the positive $x$-direction.

A wave traveling in the negative $x$-direction has the form

$$
\boxed{
y(x,t)=A\sin(kx+\omega t+\phi_0)
}.
$$

The sign between the spatial and temporal terms determines the propagation direction:

- $kx-\omega t$: motion in the positive $x$-direction
- $kx+\omega t$: motion in the negative $x$-direction

## Wave Speed on a String

For a wave traveling along an ideal stretched string,

$$
\boxed{
v_{\mathrm{wave}}
=
\sqrt{\frac{F_T}{\mu}}
},
$$

where:

- $F_T$ is the tension in the string, and
- $\mu$ is the string’s linear mass density.

The linear mass density is

$$
\boxed{
\mu=\frac{m_{\mathrm{string}}}{L}
}.
$$

Increasing the tension strengthens the restoring force and increases the wave speed:

$$
F_T\uparrow
\quad\Longrightarrow\quad
v_{\mathrm{wave}}\uparrow.
$$

Increasing the linear mass density gives the string greater inertia and decreases the wave speed:

$$
\mu\uparrow
\quad\Longrightarrow\quad
v_{\mathrm{wave}}\downarrow.
$$

## Wave Speed Versus Particle Speed

It is essential to distinguish the speed of the wave from the speed of an individual particle in the medium.

The **wave speed** describes how rapidly the disturbance propagates through space:

$$
v_{\mathrm{wave}}
=
\sqrt{\frac{F_T}{\mu}}.
$$

The **particle velocity** describes how rapidly one small element of the medium moves about its equilibrium position.

For a particle undergoing simple harmonic motion,

$$
x(t)=A\cos(\omega t).
$$

Its velocity is

$$
u(t)=\frac{dx}{dt}
=
-\omega A\sin(\omega t),
$$

and its acceleration is

$$
a(t)=\frac{du}{dt}
=
-\omega^2A\cos(\omega t).
$$

The maximum particle speed is therefore

$$
\boxed{
u_{\max}=\omega A
}.
$$

For a sinusoidal transverse wave,

$$
y(x,t)=A\sin(kx-\omega t+\phi_0),
$$

the vertical velocity of a string element is

$$
u_y(x,t)
=
\frac{\partial y}{\partial t}
=
-\omega A\cos(kx-\omega t+\phi_0).
$$

Its maximum magnitude is again

$$
\boxed{
u_{y,\max}=\omega A
}.
$$

Thus:

- $v_{\mathrm{wave}}$ is the propagation speed of the wave pattern.
- $u_y$ is the velocity of an individual string element.

They represent different physical motions and should not be confused.

## Worked Example: Wave Speed on a String

Consider a horizontal wire passing over an ideal pulley and supporting a stationary hanging block of mass $M$.

Let:

- $M$ be the hanging mass,
- $m_w$ be the mass of the wire,
- $L$ be the wire’s length, and
- $\mu$ be its linear mass density.

Because the hanging block is stationary, the net force on it is zero:

$$
\sum F_y=0.
$$

Taking upward as positive,

$$
F_T-Mg=0.
$$

Therefore,

$$
F_T=Mg.
$$

The wire’s linear mass density is

$$
\mu=\frac{m_w}{L}.
$$

Substituting into the wave-speed equation gives

$$
v_{\mathrm{wave}}
=
\sqrt{
\frac{Mg}{m_w/L}
}.
$$

Therefore,

$$
\boxed{
v_{\mathrm{wave}}
=
\sqrt{\frac{MgL}{m_w}}
}.
$$

Using the numerical values supplied in the problem gives

$$
\boxed{
v_{\mathrm{wave}}=25\ \mathrm{m}/\mathrm{s}
}.
$$

The hanging mass and the wire mass play different roles:

- The hanging mass determines the tension.
- The wire mass determines the linear mass density.

## Worked Example: Maximum Particle Speed in the Wire

Consider the same general string-and-pulley system. Suppose we now know:

- The hanging mass $M$
- The wire length $L$
- The wire mass $m_w$
- The wave amplitude $A$
- The wavelength $\lambda$

We want the maximum speed of a particle oscillating in the wire, not the propagation speed of the wave.

The maximum particle speed is

$$
u_{\max}=\omega A.
$$

Because

$$
\omega=2\pi f,
$$

we have

$$
u_{\max}=2\pi fA.
$$

The frequency of each oscillating string element is the same as the frequency of the traveling wave. From

$$
v_{\mathrm{wave}}=f\lambda,
$$

the frequency is

$$
f=\frac{v_{\mathrm{wave}}}{\lambda}.
$$

The wave speed is

$$
v_{\mathrm{wave}}
=
\sqrt{\frac{MgL}{m_w}}.
$$

Therefore,

$$
f
=
\frac{1}{\lambda}
\sqrt{\frac{MgL}{m_w}}.
$$

Substituting into the particle-speed equation gives

$$
u_{\max}
=
2\pi A
\left(
\frac{1}{\lambda}
\sqrt{\frac{MgL}{m_w}}
\right).
$$

Thus,

$$
\boxed{
u_{\max}
=
\frac{2\pi A}{\lambda}
\sqrt{\frac{MgL}{m_w}}
}.
$$

Using the numerical values supplied in the problem gives approximately

$$
\boxed{
u_{\max}=2.0\times10^2\ \mathrm{m}/\mathrm{s}
}.
$$

This is the maximum transverse speed of a particle in the wire. It is not the speed at which the wave travels along the wire.

## Spherical Sound Wavefronts

Sound from a sufficiently small source can propagate outward in approximately spherical wavefronts.

A wavefront consists of points with the same phase. At a particular instant, every point on a spherical wavefront is the same distance from the source.

In a two-dimensional cross-section, a spherical wavefront appears as a circle.

### Example: Locating a Listener on a Circular Wavefront

Suppose a sound source lies somewhere on the $x$-axis. Two listeners located at

$$
x_1=-7\ \mathrm{m}
$$

and

$$
x_2=+3\ \mathrm{m}
$$

detect the same wavefront simultaneously.

Because the source lies on the $x$-axis and is equidistant from both listeners, its position is the midpoint:

$$
x_s
=
\frac{x_1+x_2}{2}.
$$

Substituting,

$$
x_s
=
\frac{-7\ \mathrm{m}+3\ \mathrm{m}}{2}.
$$

Therefore,

$$
\boxed{
x_s=-2\ \mathrm{m}
}.
$$

The radius of the wavefront is the distance from the source to either listener:

$$
r
=
3\ \mathrm{m}-(-2\ \mathrm{m}).
$$

Thus,

$$
\boxed{
r=5\ \mathrm{m}
}.
$$

A third listener lies on the $y$-axis, so its coordinates are $(0,y)$. Relative to the center at $(-2,0)$, its horizontal displacement is

$$
\Delta x=2\ \mathrm{m}.
$$

Using the equation of a circle,

$$
(\Delta x)^2+y^2=r^2.
$$

Therefore,

$$
(2\ \mathrm{m})^2+y^2=(5\ \mathrm{m})^2.
$$

Solving for $y$,

$$
y^2
=
25\ \mathrm{m}^2-4\ \mathrm{m}^2,
$$

so

$$
y=\sqrt{21}\ \mathrm{m}.
$$

For the listener shown above the $x$-axis,

$$
\boxed{
y\approx4.58\ \mathrm{m}
}.
$$

A corresponding point below the $x$-axis would have $y\approx-4.58\ \mathrm{m}$.

## Light in a Material Medium

Light is an electromagnetic wave. In a vacuum, its speed is

$$
c\approx3.00\times10^8\ \mathrm{m}/\mathrm{s}.
$$

In a transparent material, the electromagnetic field interacts with the material’s charged particles. Their response produces a phase delay, so the wave has a lower effective propagation speed than it does in a vacuum.

The index of refraction is defined as

$$
\boxed{
n=\frac{c}{v}
},
$$

where:

- $c$ is the speed of light in a vacuum, and
- $v$ is the phase speed of light in the material.

For the ordinary transparent media considered here,

$$
v<c
$$

and therefore

$$
n>1.
$$

Solving for the speed in the material gives

$$
\boxed{
v=\frac{c}{n}
}.
$$

A larger index of refraction corresponds to a lower wave speed.

## Frequency and Wavelength at a Boundary

The wave-speed equation for light is

$$
v=f\lambda.
$$

When light passes from one stationary medium into another, its frequency remains constant. The frequency is determined by the source, and the oscillations on both sides of the boundary must remain synchronized.

The wave speed changes because the medium changes. Because

$$
v=f\lambda,
$$

the wavelength must also change.

Therefore, when light crosses a boundary:

- The frequency remains constant.
- The wave speed changes.
- The wavelength changes.

Substituting

$$
v=f\lambda
$$

into

$$
n=\frac{c}{v}
$$

gives

$$
n=\frac{c}{f\lambda}.
$$

Multiplying by $\lambda$,

$$
n\lambda=\frac{c}{f}.
$$

For the same light wave, both $c$ and $f$ are constant. Therefore,

$$
\boxed{
n\lambda=\text{constant}
}.
$$

For two media,

$$
\boxed{
n_1\lambda_1=n_2\lambda_2
}.
$$

For several media,

$$
n_1\lambda_1
=
n_2\lambda_2
=
n_3\lambda_3
=
\frac{c}{f}.
$$

A larger index of refraction therefore corresponds to a shorter wavelength:

$$
n\uparrow
\quad\Longrightarrow\quad
\lambda\downarrow.
$$

## Comparing Indices of Refraction

Suppose a snapshot shows the same light wave traveling through three media, labeled $A$, $B$, and $C$.

Because the frequency is the same in all three media,

$$
n\lambda=\frac{c}{f}
$$

is constant.

The medium with the shortest wavelength has the largest index of refraction.

For the wavelengths shown in the example,

$$
\lambda_B<\lambda_A<\lambda_C.
$$

Therefore,

$$
\boxed{
n_B>n_A>n_C
}.
$$

Medium $B$ has the lowest wave speed, while medium $C$ has the highest wave speed.

## Worked Example: Wavelengths Inside a Glass Slide

Suppose light has a wavelength in air of

$$
\lambda_{\mathrm{air}}=650\ \mathrm{nm}.
$$

The index of refraction of air is approximately

$$
n_{\mathrm{air}}=1.0,
$$

and the index of refraction of the glass is

$$
n_{\mathrm{glass}}=1.5.
$$

We first find the wavelength inside the glass.

Because

$$
n_{\mathrm{air}}\lambda_{\mathrm{air}}
=
n_{\mathrm{glass}}\lambda_{\mathrm{glass}},
$$

we have

$$
\lambda_{\mathrm{glass}}
=
\frac{n_{\mathrm{air}}}{n_{\mathrm{glass}}}
\lambda_{\mathrm{air}}.
$$

Substituting,

$$
\lambda_{\mathrm{glass}}
=
\frac{1.0}{1.5}
(650\ \mathrm{nm}).
$$

Therefore,

$$
\boxed{
\lambda_{\mathrm{glass}}
\approx433\ \mathrm{nm}
}.
$$

The light’s wavelength is shorter in the glass because its speed is lower while its frequency remains unchanged.

Let the slide width be $d$. If $N$ complete wavelengths fit within that width, then

$$
N\lambda_{\mathrm{glass}}=d.
$$

Therefore,

$$
N=\frac{d}{\lambda_{\mathrm{glass}}}.
$$

Substituting the expression for the glass wavelength gives

$$
N
=
\frac{d}{
\left(
\frac{n_{\mathrm{air}}}{n_{\mathrm{glass}}}
\right)
\lambda_{\mathrm{air}}
}.
$$

Thus,

$$
\boxed{
N
=
\frac{d}{\lambda_{\mathrm{air}}}
\frac{n_{\mathrm{glass}}}{n_{\mathrm{air}}}
}.
$$

For the slide width shown in the problem,

$$
d=1.4\ \mathrm{mm}.
$$

Converting the width to meters,

$$
d=1.4\times10^{-3}\ \mathrm{m}.
$$

The wavelength in glass is

$$
\lambda_{\mathrm{glass}}
=
433\times10^{-9}\ \mathrm{m}.
$$

Therefore,

$$
N
=
\frac{
1.4\times10^{-3}\ \mathrm{m}
}{
433\times10^{-9}\ \mathrm{m}
}.
$$

This gives

$$
\boxed{
N\approx3.23\times10^3
}.
$$

Approximately $3230$ wavelengths fit across the glass slide.

## Energy Carried by a Wave

A traveling mechanical wave transports energy through the medium.

Consider a small particle in the medium undergoing simple harmonic motion. Its kinetic energy is

$$
K=\frac{1}{2}mu^2.
$$

The maximum particle speed is

$$
u_{\max}=\omega A.
$$

Because

$$
\omega=2\pi f,
$$

the characteristic particle speed is proportional to both frequency and amplitude:

$$
u\propto fA.
$$

Since kinetic energy depends on the square of the speed,

$$
K\propto u^2,
$$

and therefore

$$
K\propto f^2A^2.
$$

A mechanical wave also contains potential energy associated with deformation of the medium. For a sinusoidal wave in a fixed linear medium, the total transported energy has the same dependence on frequency and amplitude.

Thus, for fixed properties of the medium,

$$
\boxed{
P_{\mathrm{avg}}\propto f^2A^2
}
$$

and

$$
\boxed{
I\propto f^2A^2
}.
$$

The exact proportionality constant depends on the type of wave and the properties of the medium.

These proportionalities show that:

- Increasing the amplitude substantially increases the energy carried by the wave.
- Increasing the frequency also increases the energy-transfer rate.
- Doubling the amplitude produces four times the intensity, provided the other relevant properties remain unchanged.

## Power

Power is the rate at which energy is transferred:

$$
\boxed{
P=\frac{\Delta E}{\Delta t}
}.
$$

Its SI unit is the watt:

$$
1\ \mathrm{W}=1\ \mathrm{J}/\mathrm{s}.
$$

For a continuous wave, we generally use the average power transported over many oscillation cycles.

## Intensity

Intensity is the average power transmitted per unit area:

$$
\boxed{
I=\frac{P}{A_s}
},
$$

where $A_s$ represents the area through which the wave’s power passes.

The SI unit of intensity is

$$
\boxed{
\mathrm{W}/\mathrm{m}^2
}.
$$

The symbol $A_s$ is used here for surface area so that it is not confused with the wave amplitude $A$.

## Intensity from an Isotropic Point Source

Consider an ideal point source that radiates power uniformly in all directions.

At a distance $r$ from the source, the wave’s power is distributed over the surface of a sphere. The surface area of that sphere is

$$
A_s=4\pi r^2.
$$

Therefore, the intensity is

$$
\boxed{
I(r)=\frac{P}{4\pi r^2}
}.
$$

This is an inverse-square relationship:

$$
I\propto\frac{1}{r^2}.
$$

As the wave travels outward, the total power is spread over a progressively larger spherical surface.

For example, doubling the distance from the source increases the spherical area by a factor of four and decreases the intensity to one-fourth of its original value.

This equation assumes:

- An ideal point source
- Uniform radiation in every direction
- No absorption of energy by the medium
- No reflections or other sources of interference

## Sound Intensity Level

The human ear responds to an extremely wide range of sound intensities. It is therefore convenient to describe sound using a logarithmic quantity called the **sound intensity level**.

The sound intensity level is

$$
\boxed{
\beta
=
10\log_{10}
\left(
\frac{I}{I_0}
\right)
\ \mathrm{dB}
},
$$

where:

- $\beta$ is the intensity level in decibels,
- $I$ is the measured sound intensity, and
- $I_0$ is the reference intensity.

The standard reference intensity is

$$
\boxed{
I_0=1.0\times10^{-12}\ \mathrm{W}/\mathrm{m}^2
}.
$$

This value is approximately the threshold of human hearing under standard reference conditions.

The logarithmic scale is useful because audible sound intensities span many orders of magnitude. Instead of working directly with extremely small and extremely large values of $I$, we normally compare them using the decibel scale.

We will apply these intensity and intensity-level equations in the next lecture.

## Summary

A sinusoidal oscillator may be described by

$$
x(t)=A\cos(\omega t+\phi_0).
$$

A sinusoidal wave traveling in the positive $x$-direction may be described by

$$
y(x,t)=A\sin(kx-\omega t+\phi_0).
$$

A wave traveling in the negative $x$-direction may be described by

$$
y(x,t)=A\sin(kx+\omega t+\phi_0).
$$

The wave number and angular frequency are

$$
k=\frac{2\pi}{\lambda}
$$

and

$$
\omega=2\pi f=\frac{2\pi}{T}.
$$

The wave speed is

$$
\boxed{
v_{\mathrm{wave}}
=
\frac{\lambda}{T}
=
f\lambda
=
\frac{\omega}{k}
}.
$$

For an ideal wave on a string,

$$
\boxed{
v_{\mathrm{wave}}
=
\sqrt{\frac{F_T}{\mu}}
}
$$

with

$$
\mu=\frac{m_{\mathrm{string}}}{L}.
$$

The maximum speed of a particle oscillating within the medium is

$$
\boxed{
u_{\max}=\omega A
}.
$$

Wave speed and particle speed describe different motions.

The index of refraction is

$$
\boxed{
n=\frac{c}{v}
}.
$$

When light passes from one medium into another, its frequency remains constant while its speed and wavelength change. Consequently,

$$
\boxed{
n_1\lambda_1=n_2\lambda_2
}.
$$

Intensity is power per unit area:

$$
\boxed{
I=\frac{P}{A_s}
}.
$$

For an isotropic point source,

$$
\boxed{
I=\frac{P}{4\pi r^2}
}.
$$

For a sinusoidal wave in a fixed linear medium,

$$
I\propto f^2A^2.
$$

Sound intensity level is

$$
\boxed{
\beta
=
10\log_{10}
\left(
\frac{I}{I_0}
\right)
\ \mathrm{dB}
}
$$

with

$$
\boxed{
I_0=1.0\times10^{-12}\ \mathrm{W}/\mathrm{m}^2
}.
$$

---

Up Next: [Sound Intensity, Decibels, and the Doppler Effect](../../2026-07-28-M5-3/Source/Lecture-Transcript.md)
Previous: [From Oscillations to Wave Motion](../../2026-07-23-M5-1/Source/Lecture-Transcript.md)

---
