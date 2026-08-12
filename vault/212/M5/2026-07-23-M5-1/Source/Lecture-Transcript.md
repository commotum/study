# Physics 212: From Oscillations to Wave Motion

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

The Quiz 1X assignment has been graded, and the scores are now posted on Canvas. Quiz 2 is still being graded.

Quiz 3 will open next Saturday and will be administered during the Zoom sessions on the following Monday. It will use the same format as the previous quizzes.

There is no class tomorrow. We will continue our study of waves on Monday.

## Connecting Oscillations and Waves

Today, we are beginning our study of waves.

Oscillations and waves are closely related, but they are not the same thing.

An **oscillation** is repeated motion about an equilibrium position. Examples include:

- A pendulum swinging back and forth
- A mass moving on a spring
- A particle in a string moving up and down

A **wave** is a disturbance that propagates through space. A wave can often be understood as a system of many connected oscillators.

For example, when a wave travels along a string, each small element of the string oscillates about its equilibrium position. The individual elements do not travel along the string with the wave. Instead, the disturbance passes from one element to the next.

Before discussing waves in detail, we will review the major properties of oscillating systems.

## Review: The Simple Pendulum

For a simple pendulum undergoing small-angle oscillations, the period is

$$
T=2\pi\sqrt{\frac{L}{g}}
$$

and the frequency is

$$
f=\frac{1}{T}
=
\frac{1}{2\pi}\sqrt{\frac{g}{L}},
$$

where:

- $L$ is the length of the pendulum
- $g$ is the acceleration due to gravity
- $T$ is the period
- $f$ is the frequency

The mass of the pendulum does not appear in either expression. Therefore, the frequency of an ideal simple pendulum does not depend on its mass.

The pendulum’s length does affect its frequency:

- A shorter pendulum has a higher frequency.
- A longer pendulum has a lower frequency.

For a pendulum, the tangential component of gravity supplies the restoring force:

$$
F_{\mathrm{restoring}}=-mg\sin\theta.
$$

For small angular displacements,

$$
\sin\theta\approx\theta,
$$

so the restoring force is approximately proportional to the angular displacement.

## Stable and Unstable Equilibrium

Oscillations occur around a position of stable equilibrium.

Imagine placing a marble at the bottom of a bowl. If the marble is placed exactly at the bottom, it remains at rest. If it is displaced slightly, a restoring force causes it to roll back toward the bottom. It may then oscillate around that equilibrium position.

This is **stable equilibrium**.

Now imagine placing the marble at the top of an overturned bowl. If it is positioned perfectly at the center, it may remain there momentarily. However, if it is displaced even slightly, it rolls away rather than returning.

This is **unstable equilibrium**.

The important distinction is that a system in stable equilibrium experiences a restoring force after a small displacement. That restoring force points back toward equilibrium.

## Simple Harmonic Motion and Circular Motion

Simple harmonic motion can be understood through its relationship to uniform circular motion.

Imagine a point moving at constant speed around a circle. Although its speed is constant, its velocity is not constant because the direction of motion continually changes.

If the circular motion is projected onto either the horizontal or vertical axis, the projection moves back and forth sinusoidally.

The resulting one-dimensional motion can be described by

$$
x(t)=A\cos(\omega t+\phi_0),
$$

where:

- $A$ is the amplitude
- $\omega$ is the angular frequency
- $\phi_0$ is the initial phase
- $x(t)$ is the displacement from equilibrium

The projection of uniform circular motion is therefore an example of simple harmonic motion.

## Review: A Mass on a Spring

For an ideal mass–spring oscillator,

$$
\omega=\sqrt{\frac{k}{m}},
$$

where $k$ is the spring constant and $m$ is the oscillating mass.

The ordinary frequency is

$$
f=\frac{\omega}{2\pi}
=
\frac{1}{2\pi}\sqrt{\frac{k}{m}},
$$

and the period is

$$
T=2\pi\sqrt{\frac{m}{k}}.
$$

These equations show that:

- Increasing the spring constant increases the frequency.
- Increasing the mass decreases the frequency.
- The amplitude does not affect the frequency of an ideal spring oscillator.

### Comparing Two Masses

Suppose a $100\ \mathrm{g}$ mass and a $50\ \mathrm{g}$ mass are attached to identical springs. Each mass is pulled the same distance from its own equilibrium position and released.

Because the spring constants are the same,

$$
f\propto\frac{1}{\sqrt{m}}.
$$

Therefore,

$$
f_{50\ \mathrm{g}}>f_{100\ \mathrm{g}}.
$$

The $50\ \mathrm{g}$ mass oscillates more rapidly.

For the same displacement $A$, both springs produce restoring forces of the same magnitude:

$$
F_{\mathrm{spring}}=kA.
$$

However, Newton’s second law gives

$$
a=\frac{F}{m}.
$$

The smaller mass therefore experiences a greater acceleration from the same restoring force. It changes direction more quickly and completes each oscillation in less time.

## The Restoring Force of a Vertical Spring

For a vertically hanging mass, gravity determines the equilibrium position.

At equilibrium,

$$
kx_{\mathrm{eq}}=mg.
$$

If the mass is displaced by an additional amount $y$ from equilibrium, the net force is

$$
F_{\mathrm{net}}=-ky.
$$

Gravity continues to act downward, but it is already balanced by the spring force at equilibrium. The change in the spring force supplies the restoring behavior about that equilibrium position.

Thus, the oscillation frequency remains

$$
\omega=\sqrt{\frac{k}{m}}.
$$

Gravity shifts the equilibrium position, but it does not appear in the frequency equation.

## Restoring Force and Inertia

The pendulum and spring equations illustrate a general feature of oscillators.

The frequency is determined by a competition between:

1. A restoring effect that pulls the system toward equilibrium
2. An inertial effect that resists acceleration

For a mass on a spring,

$$
\omega=\sqrt{\frac{k}{m}}.
$$

The spring constant $k$ measures the strength of the restoring force, while the mass $m$ measures the system’s inertia.

A stronger restoring force produces a higher frequency. Greater inertia produces a lower frequency.

The same general idea will appear when we study waves.

## Waves as Systems of Oscillators

A wave is a disturbance that propagates through space and transfers energy.

In a mechanical wave, the particles of the medium oscillate locally while the disturbance travels through the medium.

Consider a crowd performing a stadium wave. Each person moves mainly up and down and remains in approximately the same location. The pattern of raised people, however, moves around the stadium.

Similarly, for a wave on a string:

- Each small part of the string oscillates about equilibrium.
- The individual string elements do not travel with the wave.
- The disturbance and its energy propagate along the string.

A wave therefore contains oscillations, but the wave is the propagating pattern rather than the motion of any single particle.

## Transverse Waves

A **transverse wave** is one in which the particles of the medium oscillate perpendicular to the direction in which the wave propagates.

A wave traveling along a horizontal string is a common example.

If the wave travels to the right, the string elements move primarily up and down:

$$
\text{particle motion}\perp\text{wave propagation}.
$$

The displacement of the string is commonly represented by $y$, while the wave propagates along the $x$-axis.

## Longitudinal Waves

A **longitudinal wave** is one in which the particles of the medium oscillate parallel to the direction of wave propagation.

Sound in air is a longitudinal wave.

As a sound wave passes through the air, individual air molecules oscillate back and forth. This motion produces alternating regions of:

- **Compression**, where the molecules are more densely packed
- **Rarefaction**, where the molecules are more widely separated

If the wave travels horizontally, the molecular oscillations are also primarily horizontal:

$$
\text{particle motion}\parallel\text{wave propagation}.
$$

The air molecules do not travel all the way from the sound source to the listener. They oscillate around their local equilibrium positions while the sound disturbance propagates through the air.

## Wave Pulses and Reflections

A single disturbance sent along a string is called a **wave pulse**.

If the string is attached to a fixed endpoint, the pulse reflects when it reaches that boundary. A pulse reflecting from a fixed end is inverted.

A positive pulse therefore returns as a negative pulse.

The inversion occurs because the displacement of the fixed endpoint must remain zero. The reflected wave combines with the incident wave so that the boundary condition is satisfied.

If a continuous sequence of waves is sent along the string, the right-moving and reflected left-moving waves overlap. Their displacements add according to the principle of superposition.

Under the appropriate conditions, this interference can produce a standing wave. We will study standing waves and superposition in greater detail later.

## Restoring Force in a String

Each small element of a stretched string behaves like an oscillator.

Suppose one section of the string is displaced above equilibrium. Tension acts along the string on both sides of that section.

The horizontal components of the tension approximately cancel. The vertical components produce a net force that points back toward equilibrium.

If the string element is above equilibrium, the net force points downward. If the element is below equilibrium, the net force points upward.

The restoring force for a transverse wave on a string therefore arises from the string tension.

## Wave Speed on a String

For a wave traveling along an ideal stretched string, the wave speed is

$$
\boxed{
v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}}
},
$$

where:

- $F_T$ is the tension in the string
- $\mu$ is the string’s linear mass density

The linear mass density is

$$
\mu=\frac{m}{L},
$$

where $m$ is the mass of a length $L$ of string.

The equation

$$
v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}}
$$

has the same general structure as the frequency equation for an oscillator:

- The restoring effect, tension, appears in the numerator.
- The inertial effect, linear mass density, appears in the denominator.

Therefore:

- Greater tension produces a greater wave speed.
- Greater linear mass density produces a lower wave speed.

A tightly stretched string transmits a disturbance more rapidly than a loosely stretched string. A light string transmits a disturbance more rapidly than a heavier string under the same tension.

The equation determines the speed of the wave, not its frequency. The source determines the frequency, while the properties of the string determine the wave speed.

## Describing a Wave in Space and Time

A traveling wave depends on both position and time:

$$
y=y(x,t).
$$

There are two different ways to graph this function.

### Displacement Versus Position

A graph of $y$ versus $x$ at a fixed time is a snapshot of the entire wave.

Mathematically, we hold time constant:

$$
y(x,t_0).
$$

This graph shows the displacement of many different particles at one instant.

### Displacement Versus Time

A graph of $y$ versus $t$ at a fixed position shows the motion of one particular particle as the wave passes.

Mathematically, we hold position constant:

$$
y(x_0,t).
$$

This graph shows how one location in the medium oscillates over time.

These graphs may both appear sinusoidal, but they describe different aspects of the wave:

- $y$ versus $x$ compares many particles at one time.
- $y$ versus $t$ follows one particle through many times.

## The Form of a Right-Moving Wave

A wave with a fixed shape traveling to the right can be written in the general form

$$
y(x,t)=F(x-vt),
$$

where $F$ describes the shape of the wave.

For a sinusoidal wave,

$$
y(x,t)=A\sin(kx-\omega t+\phi_0),
$$

where

$$
k=\frac{2\pi}{\lambda}
$$

is the wave number and

$$
\omega=2\pi f
$$

is the angular frequency.

The quantity $x-vt$ means that, as time increases, the entire shape shifts toward larger values of $x$.

A wave traveling to the left instead has the form

$$
y(x,t)=F(x+vt).
$$

## Determining a Particle’s Direction of Motion

Consider a snapshot of a transverse wave traveling to the right.

The wave itself moves horizontally, but an individual string element moves vertically. To determine whether that element is moving up or down, imagine shifting the entire wave slightly to the right and observing the displacement at the same horizontal position.

For a right-moving wave,

$$
\frac{\partial y}{\partial t}
=
-v_{\mathrm{wave}}\frac{\partial y}{\partial x}.
$$

This provides a useful rule:

- If the spatial slope is positive, the particle is moving downward.
- If the spatial slope is negative, the particle is moving upward.
- If the spatial slope is zero, the particle is momentarily at rest.

At the point considered in the lecture, the wave had a positive spatial slope and was moving to the right. Therefore,

$$
\frac{\partial y}{\partial t}<0,
$$

so the particle was moving downward.

For a wave traveling to the left, the relationship becomes

$$
\frac{\partial y}{\partial t}
=
+v_{\mathrm{wave}}\frac{\partial y}{\partial x},
$$

and the directional rule is reversed.

## Particle Motion Versus Wave Motion

It is essential to distinguish the motion of the wave from the motion of the medium.

For a transverse wave traveling to the right:

- The wave velocity points to the right.
- The string elements move up and down.
- A string element does not move to the right with the crest.

This distinction is similar to a stadium wave. The pattern moves around the stadium, but the people remain near their seats.

We can therefore define two different velocities:

- **Wave velocity:** the rate at which the disturbance propagates
- **Particle velocity:** the rate at which an element of the medium moves about equilibrium

For a transverse wave,

$$
u_y
=
\frac{\partial y}{\partial t}.
$$

This is different from the wave speed $v_{\mathrm{wave}}$.

## Where Does a Particle Move Fastest?

For an ideal sinusoidal wave, each point in the medium undergoes simple harmonic motion.

A particle moves fastest as it passes through equilibrium:

$$
y=0.
$$

It momentarily stops at its maximum positive and negative displacements:

$$
y=\pm A.
$$

This is exactly the same behavior as a mass on a spring:

- At maximum displacement, the speed is zero.
- At equilibrium, the speed is maximum.

On a snapshot of a sinusoidal wave, particles located at equilibrium crossings are therefore moving fastest, while particles at crests and troughs are momentarily at rest.

## Wavelength, Period, Frequency, and Wave Speed

The **wavelength**, represented by $\lambda$, is the spatial length of one complete wave cycle.

The **period**, represented by $T$, is the time required for one complete cycle to pass a fixed position.

During one period, the wave travels one wavelength. Therefore,

$$
v_{\mathrm{wave}}=\frac{\lambda}{T}.
$$

Because

$$
f=\frac{1}{T},
$$

the wave-speed equation can also be written as

$$
\boxed{
v_{\mathrm{wave}}=f\lambda
}.
$$

This equation relates wave speed, frequency, and wavelength.

For the nondispersive wave models considered here, the medium determines the wave speed. Once the source frequency is selected, the wavelength adjusts to satisfy

$$
\lambda=\frac{v_{\mathrm{wave}}}{f}.
$$

Therefore, in the same medium:

- Increasing the frequency decreases the wavelength.
- Decreasing the frequency increases the wavelength.
- The wave speed remains unchanged.

For example, different sound frequencies travel through ordinary air at approximately the same speed under the same conditions. A higher-frequency sound has a shorter wavelength, not a greater propagation speed.

## Example: Changing the Tension in a String

Consider a string attached to a wall, passing over an ideal pulley, and connected to a hanging mass $M$.

If the hanging mass is stationary, the string tension is approximately

$$
F_T=Mg.
$$

The wave speed is therefore

$$
v_{\mathrm{wave}}
=
\sqrt{\frac{Mg}{\mu}}.
$$

If the hanging mass is increased while the same string is used, the tension increases. Therefore, the wave speed increases:

$$
M\uparrow
\quad\Longrightarrow\quad
F_T\uparrow
\quad\Longrightarrow\quad
v_{\mathrm{wave}}\uparrow.
$$

The frequency of a wave sent along the string would still be set by the oscillator producing the wave. The increased tension changes the wave speed and therefore changes the wavelength associated with that frequency.

## Waves in One, Two, and Three Dimensions

A wave on a string is treated as a one-dimensional wave because the disturbance propagates along the length of the string.

A wave on the surface of water propagates across a two-dimensional surface.

Sound from a localized source can propagate outward through three-dimensional space. In an idealized uniform medium, wavefronts from a compact source may form expanding spherical surfaces.

A two-dimensional cross-section through those spherical wavefronts appears as expanding circles.

## Sound-Wave Sources

The spatial pattern produced by a wave depends on how the source oscillates.

### Monopole Source

An ideal monopole source expands and contracts uniformly. It produces approximately spherical wavefronts in a uniform medium.

The radiation pattern is nearly the same in every direction.

### Dipole Source

A dipole source moves in a preferred direction, alternately pushing the medium on one side and pulling it on the other.

Its radiation is directional rather than spherically symmetric. It produces two primary lobes with a region of weak radiation perpendicular to the direction of motion.

A small oscillating object or vibrating element may approximate dipole behavior.

### Quadrupole Source

A quadrupole source has a still more complicated pattern involving multiple regions that oscillate with opposite phases.

Its radiation pattern contains several lobes and directional nodes. Gravitational radiation is quadrupolar because isolated monopole and dipole gravitational radiation are prohibited by conservation laws.

The important principle is that the wave retains information about the geometry and motion of its source.

## Vibrating Membranes

A stretched membrane, such as a drumhead, can oscillate in many different patterns.

The simplest mode has a relatively uncomplicated shape, with the center of the membrane moving strongly. Higher modes contain nodal lines or nodal circles where the membrane remains stationary.

A membrane can support many modes simultaneously. Their superposition produces a complicated overall motion.

The human eardrum also responds to sound by vibrating. Its motion can be much more complicated than a single sinusoidal oscillation because real sounds contain many frequencies and because the membrane can respond in multiple modes.

We will return to these ideas when discussing superposition, standing waves, and musical instruments.

## Mechanical Waves

A **mechanical wave** requires a material medium.

Examples include:

- Waves on strings
- Sound waves
- Water waves
- Seismic waves

In a string, neighboring portions interact through tension and the material’s elasticity.

In a sound wave, neighboring regions of the medium interact through pressure and elastic forces. The molecules oscillate and transfer the disturbance to nearby molecules.

Because mechanical waves require matter, sound cannot travel through an ideal vacuum.

## Electromagnetic Waves

Light is not a mechanical wave and does not require a material medium.

An electromagnetic wave consists of oscillating electric and magnetic fields. For an ideal plane wave in a vacuum:

- The electric field is perpendicular to the magnetic field.
- Both fields are perpendicular to the direction of propagation.

Symbolically,

$$
\vec{E}\perp\vec{B}
$$

and

$$
\vec{E}\perp\vec{v}_{\mathrm{wave}},
\qquad
\vec{B}\perp\vec{v}_{\mathrm{wave}}.
$$

Electromagnetic waves can therefore propagate through the vacuum of space, where sound waves cannot.

## Summary

An oscillation is repeated motion about equilibrium, while a wave is a disturbance that propagates through space.

For a simple pendulum,

$$
T=2\pi\sqrt{\frac{L}{g}}
$$

and

$$
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
$$

For a mass on a spring,

$$
\omega=\sqrt{\frac{k}{m}},
$$

$$
f=\frac{1}{2\pi}\sqrt{\frac{k}{m}},
$$

and

$$
T=2\pi\sqrt{\frac{m}{k}}.
$$

A stronger restoring effect produces a higher oscillation frequency, while greater inertia produces a lower frequency.

For a wave on a string, tension supplies the restoring force. The wave speed is

$$
v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}}.
$$

A transverse wave has particle motion perpendicular to the propagation direction. A longitudinal wave has particle motion parallel to the propagation direction.

A wave can be graphed either as displacement versus position at a fixed time or as displacement versus time at a fixed position.

Wave speed, frequency, wavelength, and period are related by

$$
v_{\mathrm{wave}}=\frac{\lambda}{T}=f\lambda.
$$

In the ideal nondispersive models considered here, the medium determines the wave speed, while the source determines the frequency. The wavelength then adjusts according to

$$
\lambda=\frac{v_{\mathrm{wave}}}{f}.
$$

Mechanical waves require a material medium. Electromagnetic waves do not and can propagate through a vacuum.

---

Up Next: [Traveling Waves, Refraction, and Intensity](../../2026-07-27-M5-2/Source/Lecture-Transcript.md)
Previous: [Simple and Physical Pendula](../../../M4/2026-07-22-M4-2/Source/Lecture-Transcript.md)

---
