# Physics 212: Oscillations and Simple Harmonic Motion

Welcome back to Physics 212.

## Announcements

Quiz 2 has been completed and is currently being graded. Scores should be available by next Monday.

Quiz 1X is also being graded. Those scores should be returned within one week of the assignment’s due date.

Today, we are beginning the material for Quiz 3, which covers oscillations and waves. You should begin preparing your Quiz 3 note sheet as we work through this material.

Remember to submit your Quiz 2 note sheet if you have not already done so. Credit for Quiz 2 cannot be awarded until the note sheet has been submitted. Your photo ID should be placed on top of the note sheet so that both appear in the uploaded image.

## Oscillations and Waves

We will begin our study of waves by reviewing oscillations and simple harmonic motion.

An object undergoes **simple harmonic motion** when its position as a function of time can be described by a sine or cosine function. One of the easiest ways to visualize this relationship is through uniform circular motion.

Imagine a point moving around a circle at constant speed. Its velocity is not constant because its direction continually changes, but the magnitude of its velocity remains constant. If we project that circular motion onto a one-dimensional axis, the projected point moves back and forth sinusoidally.

In other words, the one-dimensional projection of uniform circular motion is simple harmonic motion.

This also helps us begin distinguishing an oscillation from a wave.

An **oscillation** is repeated motion about an equilibrium position. Examples include a pendulum swinging back and forth or a mass moving up and down on a spring.

A **wave** is a disturbance that propagates through space. A wave can often be viewed as a collection of many connected oscillators.

For example, when a wave travels along a string, each individual point on the string oscillates up and down while the overall disturbance propagates horizontally along the string. Similarly, a sound wave consists of many small regions of a medium oscillating as the disturbance travels through space.

Waves generally originate from oscillating sources. The frequency of the generated wave is therefore determined by the frequency of its source.

We will spend the next few class periods studying individual oscillators before extending these ideas to waves and wave propagation.

## Describing Simple Harmonic Motion

Consider a mass attached to a horizontal spring. The mass is pulled away from equilibrium and released.

If we define $t=0$ as the instant the mass is released from its maximum displacement, its position can be written as

$$
x(t)=A\cos(\omega t)
$$

where:

- $x(t)$ is the displacement from equilibrium,
- $A$ is the amplitude,
- $\omega$ is the angular frequency, and
- $t$ is time.

The amplitude $A$ is the maximum distance that the oscillator travels from equilibrium. The oscillator moves between the two endpoints

$$
x=+A
$$

and

$$
x=-A.
$$

The complete form of the position function can include a phase constant:

$$
x(t)=A\cos(\omega t+\phi)
$$

where $\phi$ describes the oscillator’s phase at $t=0$.

A sine function and a cosine function describe the same type of motion; they differ only by a phase shift. For now, we will usually choose $t=0$ so that the mass begins at maximum displacement. This makes $\phi=0$ and gives the simpler cosine expression.

## Period, Frequency, and Angular Frequency

The **period**, represented by $T$, is the amount of time required to complete one full oscillation.

On a position-versus-time graph, the period can be measured between any two consecutive points at which the motion begins to repeat. For example, it can be measured from one maximum to the next maximum or from one minimum to the next minimum.

The **frequency**, represented by $f$, is the number of complete oscillations per second. Frequency and period are reciprocals:

$$
f=\frac{1}{T}
$$

and

$$
T=\frac{1}{f}.
$$

The SI unit of frequency is the hertz:

$$
1\ \mathrm{Hz}=1\ \mathrm{cycle/s}=1\ \mathrm{s}^{-1}.
$$

The **angular frequency**, represented by $\omega$, measures how rapidly the oscillator moves through its cycle in radians per second.

Because one complete cycle corresponds to $2\pi$ radians,

$$
\omega=2\pi f.
$$

Using $f=1/T$, we can also write

$$
\omega=\frac{2\pi}{T}.
$$

Therefore, the three important relationships are

$$
f=\frac{1}{T},
$$

$$
\omega=2\pi f,
$$

and

$$
\omega=\frac{2\pi}{T}.
$$

In this context, $T$ represents the period. In other contexts, the same symbol may be used for tension, so its meaning must be determined from the situation.

## Velocity in Simple Harmonic Motion

The position of an oscillator released from maximum displacement is

$$
x(t)=A\cos(\omega t).
$$

Velocity is the time derivative of position:

$$
v(t)=\frac{dx}{dt}.
$$

Using the chain rule,

$$
v(t)=-A\omega\sin(\omega t).
$$

The sine function ranges between $-1$ and $+1$. Therefore, the maximum magnitude of the velocity is

$$
v_{\max}=\omega A.
$$

The oscillator reaches maximum speed as it passes through equilibrium.

At equilibrium,

$$
x=0,
$$

and the spring is neither stretched nor compressed. At that location, the mass has converted all of its spring potential energy into kinetic energy and is moving as rapidly as possible.

At either endpoint,

$$
x=\pm A,
$$

the mass momentarily stops before reversing direction. Therefore,

$$
v=0
$$

at maximum displacement.

## Acceleration in Simple Harmonic Motion

Acceleration is the time derivative of velocity:

$$
a(t)=\frac{dv}{dt}.
$$

Differentiating the velocity function gives

$$
a(t)=-A\omega^2\cos(\omega t).
$$

Because

$$
x(t)=A\cos(\omega t),
$$

the acceleration can also be written as

$$
a(t)=-\omega^2x(t).
$$

This equation is one of the defining relationships of simple harmonic motion.

The acceleration is proportional to the displacement, but it points in the opposite direction. The negative sign indicates that acceleration is always directed toward equilibrium.

If the mass is displaced to the right, then $x>0$ and $a<0$, so the acceleration points to the left.

If the mass is displaced to the left, then $x<0$ and $a>0$, so the acceleration points to the right.

At equilibrium,

$$
x=0
$$

and therefore

$$
a=0.
$$

At maximum displacement, the magnitude of the acceleration is greatest:

$$
a_{\max}=\omega^2A.
$$

## Energy of a Mass–Spring Oscillator

For an ideal mass–spring system with no friction, the total mechanical energy is conserved.

The spring force is given by Hooke’s law:

$$
F=-kx
$$

where $k$ is the spring constant and $x$ is the displacement from equilibrium.

Force and potential energy are related by

$$
F=-\frac{dU}{dx}.
$$

Substituting the spring force gives

$$
-kx=-\frac{dU}{dx}.
$$

Therefore,

$$
\frac{dU}{dx}=kx.
$$

Choosing the potential energy to be zero at equilibrium, we integrate from $0$ to $x$:

$$
U(x)-U(0)=\int_0^x kx'\,dx'.
$$

This gives

$$
U(x)=\frac{1}{2}kx^2.
$$

The total mechanical energy is therefore

$$
E=K+U,
$$

or

$$
E=\frac{1}{2}mv^2+\frac{1}{2}kx^2.
$$

At maximum displacement, the mass is momentarily at rest. Therefore,

$$
v=0
$$

and

$$
x=\pm A.
$$

All of the energy is stored as spring potential energy:

$$
E=\frac{1}{2}kA^2.
$$

At equilibrium,

$$
x=0,
$$

and the mass is moving at maximum speed. All of the energy is kinetic:

$$
E=\frac{1}{2}mv_{\max}^2.
$$

Because the total energy is conserved,

$$
\frac{1}{2}mv_{\max}^2=\frac{1}{2}kA^2.
$$

Canceling the factors of $1/2$ gives

$$
mv_{\max}^2=kA^2.
$$

Solving for the maximum speed,

$$
v_{\max}=A\sqrt{\frac{k}{m}}.
$$

We also know from the sinusoidal velocity function that

$$
v_{\max}=\omega A.
$$

Equating the two expressions gives

$$
\omega A=A\sqrt{\frac{k}{m}}.
$$

Canceling the amplitude,

$$
\omega=\sqrt{\frac{k}{m}}.
$$

Thus, the angular frequency of an ideal mass–spring oscillator is

$$
\boxed{\omega=\sqrt{\frac{k}{m}}}.
$$

Using $\omega=2\pi f$, its ordinary frequency is

$$
\boxed{f=\frac{1}{2\pi}\sqrt{\frac{k}{m}}}.
$$

Its period is

$$
\boxed{T=2\pi\sqrt{\frac{m}{k}}}.
$$

These equations show that a stiffer spring produces a higher frequency, while a larger mass produces a lower frequency.

The amplitude does not affect the frequency of an ideal mass–spring oscillator.

## Relating Position, Velocity, and Acceleration Graphs

For an oscillator released from maximum positive displacement, the three functions are

$$
x(t)=A\cos(\omega t),
$$

$$
v(t)=-A\omega\sin(\omega t),
$$

and

$$
a(t)=-A\omega^2\cos(\omega t).
$$

The velocity is the slope of the position graph:

$$
v(t)=\frac{dx}{dt}.
$$

The acceleration is the slope of the velocity graph:

$$
a(t)=\frac{dv}{dt}.
$$

These relationships allow us to interpret the motion directly from the graphs.

When the position graph crosses zero, its slope has maximum magnitude. Therefore, when the mass passes through equilibrium, its speed is greatest.

When the position graph reaches a maximum or minimum, its slope is zero. Therefore, at maximum displacement, the velocity is zero.

The acceleration function is the negative of the position function, apart from the scaling factor $\omega^2$:

$$
a(t)=-\omega^2x(t).
$$

Consequently:

- When position is at its maximum positive value, acceleration is at its most negative value.
- When position is at its maximum negative value, acceleration is at its most positive value.
- When position is zero, acceleration is zero.
- Acceleration always points toward equilibrium.

Position and acceleration are therefore exactly out of phase. When one is at a positive maximum, the other is at a negative maximum.

Velocity is shifted by one-quarter of a cycle relative to position.

## Worked Example: Reading an Oscillation Graph

Consider a position-versus-time graph describing a sinusoidal oscillator.

From the graph, the maximum displacement from equilibrium is

$$
A=2.5\ \mathrm{cm}.
$$

Therefore, the amplitude is

$$
\boxed{2.5\ \mathrm{cm}}.
$$

The time from one maximum to the next maximum is

$$
T=4.0\ \mathrm{s}.
$$

Therefore, the period is

$$
\boxed{4.0\ \mathrm{s}}.
$$

### Frequency

Frequency is the reciprocal of the period:

$$
f=\frac{1}{T}.
$$

Substituting the period,

$$
f=\frac{1}{4.0\ \mathrm{s}}.
$$

Therefore,

$$
\boxed{f=0.25\ \mathrm{Hz}}.
$$

This means that the oscillator completes one-quarter of a cycle each second.

### Angular Frequency

Angular frequency is

$$
\omega=2\pi f.
$$

Using $f=0.25\ \mathrm{Hz}$,

$$
\omega=2\pi(0.25\ \mathrm{s}^{-1}).
$$

Equivalently,

$$
\omega=\frac{2\pi}{4.0\ \mathrm{s}}.
$$

Therefore,

$$
\omega=\frac{\pi}{2}\ \mathrm{rad/s},
$$

or numerically,

$$
\boxed{\omega=1.57\ \mathrm{rad/s}}.
$$

### Maximum Speed

The maximum speed of an oscillator is

$$
v_{\max}=\omega A.
$$

Substituting the angular frequency and amplitude,

$$
v_{\max}
=
\left(\frac{\pi}{2}\ \mathrm{rad/s}\right)
(2.5\ \mathrm{cm}).
$$

Therefore,

$$
v_{\max}=1.25\pi\ \mathrm{cm/s},
$$

or

$$
\boxed{v_{\max}\approx3.9\ \mathrm{cm/s}}.
$$

## Worked Example: Position of a Mass on a Spring

Consider a block attached to a horizontal spring.

The positive $x$-direction is to the right. The equilibrium coordinate is

$$
x_{\mathrm{eq}}=0.35\ \mathrm{m},
$$

and the block is pulled to

$$
x_{\mathrm{release}}=0.48\ \mathrm{m}
$$

before being released from rest.

The amplitude is the distance between the release point and equilibrium:

$$
A=x_{\mathrm{release}}-x_{\mathrm{eq}}.
$$

Therefore,

$$
A=0.48\ \mathrm{m}-0.35\ \mathrm{m},
$$

so

$$
\boxed{A=0.13\ \mathrm{m}}.
$$

The block completes $12$ oscillations in $7.0$ seconds. Its frequency is therefore

$$
f=\frac{12}{7.0\ \mathrm{s}},
$$

or approximately

$$
f\approx1.71\ \mathrm{Hz}.
$$

The angular frequency is

$$
\omega=2\pi f,
$$

so

$$
\omega
=
2\pi\left(\frac{12}{7.0\ \mathrm{s}}\right)
\approx10.77\ \mathrm{rad/s}.
$$

Let $y(t)$ represent the displacement measured from equilibrium. Because the block is released at maximum positive displacement,

$$
y(t)=A\cos(\omega t).
$$

Equivalently,

$$
y(t)=A\cos(2\pi ft).
$$

We want the displacement at

$$
t=3.9\ \mathrm{s}.
$$

Substituting the known values,

$$
y(3.9\ \mathrm{s})
=
(0.13\ \mathrm{m})
\cos\left[
2\pi
\left(\frac{12}{7.0\ \mathrm{s}}\right)
(3.9\ \mathrm{s})
\right].
$$

Evaluating the cosine gives

$$
\boxed{y(3.9\ \mathrm{s})\approx-0.051\ \mathrm{m}}.
$$

The negative sign means that the block is approximately $5.1\ \mathrm{cm}$ to the left of equilibrium.

If we want its absolute coordinate rather than its displacement from equilibrium,

$$
x(t)=x_{\mathrm{eq}}+y(t).
$$

Therefore,

$$
x(3.9\ \mathrm{s})
=
0.35\ \mathrm{m}-0.051\ \mathrm{m},
$$

which gives

$$
\boxed{x(3.9\ \mathrm{s})\approx0.299\ \mathrm{m}}.
$$

## Velocity of the Block

The velocity is the derivative of the displacement function:

$$
v(t)=-\omega A\sin(\omega t).
$$

In terms of frequency,

$$
v(t)=-2\pi fA\sin(2\pi ft).
$$

At $t=3.9\ \mathrm{s}$,

$$
v(3.9\ \mathrm{s})
=
-2\pi
\left(\frac{12}{7.0\ \mathrm{s}}\right)
(0.13\ \mathrm{m})
\sin\left[
2\pi
\left(\frac{12}{7.0\ \mathrm{s}}\right)
(3.9\ \mathrm{s})
\right].
$$

Evaluating this expression gives

$$
\boxed{v(3.9\ \mathrm{s})\approx+1.29\ \mathrm{m/s}}.
$$

The velocity is positive, so the block is moving to the right.

At this instant:

- The displacement is negative, so the block is to the left of equilibrium.
- The velocity is positive, so the block is moving toward the right.
- The acceleration is positive because $a=-\omega^2y$ and $y<0$.
- The velocity and acceleration point in the same direction, so the block is speeding up.

The block will continue speeding up until it reaches equilibrium, where its speed will be greatest.

## Determining Whether an Oscillator Is Speeding Up

The motion of an oscillator can be interpreted by comparing the signs of its position, velocity, and acceleration.

Because

$$
a=-\omega^2x,
$$

acceleration always points opposite the displacement.

### To the Right of Equilibrium

If $x>0$, then $a<0$, so acceleration points to the left.

- If $v>0$, the mass is moving to the right while accelerating to the left. It is slowing down.
- If $v<0$, the mass is moving to the left while accelerating to the left. It is speeding up.

### To the Left of Equilibrium

If $x<0$, then $a>0$, so acceleration points to the right.

- If $v<0$, the mass is moving to the left while accelerating to the right. It is slowing down.
- If $v>0$, the mass is moving to the right while accelerating to the right. It is speeding up.

At equilibrium, the speed is maximum. At either endpoint, the speed is zero.

## Worked Example: Maximum Speed from Energy

Suppose the mass $m$, spring constant $k$, and amplitude $A$ of an oscillator are known.

At maximum displacement, all of the system’s energy is spring potential energy:

$$
E=\frac{1}{2}kA^2.
$$

At equilibrium, all of the energy is kinetic:

$$
E=\frac{1}{2}mv_{\max}^2.
$$

Equating these expressions gives

$$
\frac{1}{2}mv_{\max}^2
=
\frac{1}{2}kA^2.
$$

Canceling the factors of $1/2$,

$$
mv_{\max}^2=kA^2.
$$

Dividing by $m$,

$$
v_{\max}^2=\frac{k}{m}A^2.
$$

Taking the square root,

$$
\boxed{v_{\max}=A\sqrt{\frac{k}{m}}}.
$$

For the numerical values given in the problem, this produces

$$
\boxed{v_{\max}=8.8\ \mathrm{m/s}}.
$$

This is equivalent to using

$$
v_{\max}=\omega A
$$

because

$$
\omega=\sqrt{\frac{k}{m}}.
$$

## Summary

Simple harmonic motion is sinusoidal motion about a stable equilibrium position.

For an oscillator released from maximum displacement,

$$
x(t)=A\cos(\omega t),
$$

$$
v(t)=-A\omega\sin(\omega t),
$$

and

$$
a(t)=-A\omega^2\cos(\omega t).
$$

The acceleration is related directly to position by

$$
a=-\omega^2x.
$$

The relationships among period, frequency, and angular frequency are

$$
f=\frac{1}{T},
$$

$$
\omega=2\pi f,
$$

and

$$
\omega=\frac{2\pi}{T}.
$$

For an ideal mass–spring oscillator,

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

The maximum speed is

$$
v_{\max}=\omega A
$$

or, equivalently,

$$
v_{\max}=A\sqrt{\frac{k}{m}}.
$$

These principles provide the foundation for our study of waves. A wave can be understood as a propagating pattern produced by many connected oscillators, with the oscillation frequency determined by the wave’s source.