# Physics 212: Rolling Motion and Conservation of Angular Momentum

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 1 scores have been posted, and the optional Quiz 1X assignment is now available.

For Quiz 1X, select only the problem on which you lost the most points. The assignment has four parts:

1. Explain the reasoning that led to your original answer.
2. Explain what physical concepts or methods you should have used instead.
3. Provide a complete corrected solution. For written-response questions, include explicit unit analysis and covariational reasoning.
4. Discuss the problem with an instructor, teaching assistant, or another physics staff member.

You may complete Part D during office hours, at the end of a lab session if time permits, or in the Wormhole. Students who cannot attend during the regular daytime schedule may consult the TA schedules in the Course Information module and contact a TA to arrange another time.

Quiz 1X is optional and is due Friday at 6:00 p.m. Late submissions will not be accepted, so leave enough time to upload your written work to Gradescope.

Quiz 2 will open at 5:00 p.m. Saturday and close at 5:00 p.m. Monday for the Proctorio version. Zoom sessions will be offered Monday at 11:00 a.m. and 6:00 p.m. You should be preparing your handwritten note sheet for Quiz 2.

## Introduction

Today, we will study two related topics:

- Rolling motion
- Conservation of angular momentum

We will begin by connecting the translational motion of a rolling object’s center of mass to the object’s rotational motion. We will then introduce angular momentum and apply its conservation to several rotational collision problems.

# Rolling Without Slipping

Consider a wheel of radius $R$ rolling along a level surface without slipping.

A particular point on the rim traces a path called a **cycloid**. Each time that point returns to contact with the ground, the wheel has completed one full revolution.

During one complete revolution, the center of mass travels a distance equal to the wheel’s circumference:

$$
\Delta x=2\pi R.
$$

The time required for one complete revolution is the rotational period:

$$
T=\frac{2\pi}{\omega},
$$

where $\omega$ is the angular velocity.

The speed of the center of mass is therefore

$$
v_{\mathrm{cm}}
=
\frac{\Delta x}{T}.
$$

Substituting the expressions for $\Delta x$ and $T$ gives

$$
v_{\mathrm{cm}}
=
\frac{2\pi R}{2\pi/\omega}.
$$

The factors of $2\pi$ cancel, leaving

$$
\boxed{
v_{\mathrm{cm}}=\omega R
}.
$$

This is the rolling-without-slipping condition.

It can also be understood geometrically. As the wheel rotates through an angle $\theta$, the center of mass moves through a distance

$$
x_{\mathrm{cm}}=R\theta.
$$

Taking the time derivative gives

$$
v_{\mathrm{cm}}
=
R\frac{d\theta}{dt}.
$$

Because

$$
\omega=\frac{d\theta}{dt},
$$

we again obtain

$$
v_{\mathrm{cm}}=\omega R.
$$

This relationship is valid instantaneously even if the wheel’s angular velocity changes with time.

## Linear and Angular Acceleration

Taking another time derivative gives the acceleration of the center of mass:

$$
a_{\mathrm{cm}}
=
\frac{dv_{\mathrm{cm}}}{dt}.
$$

Using

$$
v_{\mathrm{cm}}=\omega R
$$

and assuming the radius is constant,

$$
a_{\mathrm{cm}}
=
R\frac{d\omega}{dt}.
$$

Angular acceleration is defined as

$$
\alpha=\frac{d\omega}{dt}.
$$

Therefore,

$$
\boxed{
a_{\mathrm{cm}}=\alpha R
}.
$$

The two central rolling relationships are thus

$$
\boxed{
v_{\mathrm{cm}}=\omega R
}
$$

and

$$
\boxed{
a_{\mathrm{cm}}=\alpha R
}.
$$

These equations apply when the object rolls without slipping.

The speed $\omega R$ can also be interpreted as the speed of a point on the rim relative to the wheel’s center. In the ground frame, the velocity of a particular rim point changes continuously as the wheel rotates.

# Worked Example: Hollow Sphere Rolling Down an Incline

Consider a hollow sphere with:

- Mass $m$
- Radius $R$
- Incline angle $\theta$
- Distance traveled along the incline $d$

The sphere begins at rest and rolls without slipping to the bottom of the incline. We want to determine the final speed of its center of mass.

We will assume that air resistance and dissipative rolling resistance are negligible, so mechanical energy is conserved.

## Vertical Displacement

The sphere travels a distance $d$ along an incline angled at $\theta$ above the horizontal.

The corresponding vertical drop is

$$
h=d\sin\theta.
$$

## Conservation of Energy

Choose the bottom of the incline as the zero of gravitational potential energy.

Initially, the sphere is at rest, so its energy is entirely gravitational potential energy:

$$
E_i=mgh.
$$

At the bottom, its kinetic energy contains two parts:

1. Translational kinetic energy of the center of mass
2. Rotational kinetic energy about the center of mass

Therefore,

$$
E_f
=
\frac{1}{2}mv^2
+
\frac{1}{2}I\omega^2.
$$

Conservation of mechanical energy gives

$$
mgh
=
\frac{1}{2}mv^2
+
\frac{1}{2}I\omega^2.
$$

Using

$$
h=d\sin\theta,
$$

we obtain

$$
mgd\sin\theta
=
\frac{1}{2}mv^2
+
\frac{1}{2}I\omega^2.
$$

## Moment of Inertia of a Hollow Sphere

For a thin hollow sphere, or spherical shell, the moment of inertia about its center is

$$
I=\frac{2}{3}mR^2.
$$

Because the sphere rolls without slipping,

$$
v=\omega R,
$$

so

$$
\omega=\frac{v}{R}.
$$

Substituting both relationships into the energy equation gives

$$
mgd\sin\theta
=
\frac{1}{2}mv^2
+
\frac{1}{2}
\left(
\frac{2}{3}mR^2
\right)
\left(
\frac{v}{R}
\right)^2.
$$

Simplifying the rotational term,

$$
\frac{1}{2}
\left(
\frac{2}{3}mR^2
\right)
\left(
\frac{v^2}{R^2}
\right)
=
\frac{1}{3}mv^2.
$$

Therefore,

$$
mgd\sin\theta
=
\frac{1}{2}mv^2
+
\frac{1}{3}mv^2.
$$

Combining the terms,

$$
mgd\sin\theta
=
\frac{5}{6}mv^2.
$$

The mass cancels:

$$
gd\sin\theta
=
\frac{5}{6}v^2.
$$

Solving for $v^2$,

$$
v^2
=
\frac{6}{5}gd\sin\theta.
$$

Therefore, the final speed of the center of mass is

$$
\boxed{
v
=
\sqrt{
\frac{6}{5}gd\sin\theta
}
}.
$$

Using the numerical values supplied in the activity gives

$$
\boxed{
v\approx2.5\ \mathrm{m/s}
}.
$$

Notice that both the mass and radius cancel. For an ideal hollow sphere rolling from rest through a specified vertical drop, the final speed does not depend on either its mass or its radius.

The derivation is important. Rather than beginning with a memorized formula for a rolling sphere, we should be able to obtain the result from:

- Conservation of energy
- The appropriate moment of inertia
- The rolling constraint $v=\omega R$

# Angular Momentum

Angular momentum is the rotational analogue of linear momentum.

## Linear Momentum

Linear momentum is defined as

$$
\vec{p}=m\vec{v}.
$$

Newton’s second law can be written as

$$
\sum\vec{F}_{\mathrm{ext}}
=
\frac{d\vec{p}}{dt}.
$$

If the net external force on a system is zero, then

$$
\frac{d\vec{p}}{dt}=0,
$$

and the system’s linear momentum is conserved:

$$
\vec{p}_i=\vec{p}_f.
$$

## Angular Momentum of a Particle

The angular momentum of a particle about a chosen origin is

$$
\boxed{
\vec{L}
=
\vec{r}\times\vec{p}
}.
$$

Using $\vec{p}=m\vec{v}$,

$$
\vec{L}
=
\vec{r}\times m\vec{v}.
$$

Because mass is a scalar,

$$
\vec{L}
=
m\left(\vec{r}\times\vec{v}\right).
$$

The magnitude is

$$
L=mrv\sin\phi,
$$

where $\phi$ is the angle between $\vec{r}$ and $\vec{v}$.

If the position and velocity vectors are perpendicular,

$$
\phi=90^\circ
$$

and

$$
\sin\phi=1.
$$

The angular-momentum magnitude then becomes

$$
\boxed{
L=mrv
}.
$$

The direction of $\vec{L}$ is determined by the right-hand rule.

## Angular Momentum of a Rigid Body

For a rigid body rotating about a fixed axis, the angular momentum about that axis is

$$
\boxed{
L=I\omega
},
$$

where:

- $I$ is the moment of inertia about the rotation axis
- $\omega$ is the angular velocity

The moment of inertia plays the same role in rotational motion that mass plays in translational motion.

## Torque and Angular Momentum

The rotational form of Newton’s second law is

$$
\boxed{
\sum\vec{\tau}_{\mathrm{ext}}
=
\frac{d\vec{L}}{dt}
}.
$$

If the net external torque about the chosen axis is zero,

$$
\sum\vec{\tau}_{\mathrm{ext}}=0,
$$

then

$$
\frac{d\vec{L}}{dt}=0.
$$

Angular momentum is therefore conserved:

$$
\boxed{
\vec{L}_i=\vec{L}_f
}.
$$

For rotation about a single fixed axis, this is commonly written as

$$
\boxed{
I_i\omega_i=I_f\omega_f
}.
$$

It is important to calculate torque and angular momentum about the same chosen axis.

# Worked Example: Rain Falling into Rotating Cups

Consider two identical cups rotating about a central vertical axis.

Initially:

- Each cup has mass $m$.
- The cups are separated by a total distance $d$.
- Each cup is therefore a distance $d/2$ from the rotation axis.
- The system rotates with angular velocity $\omega_0$.

Rain falls into the cups. The collected water has the same mass as each original cup, so the final mass at each end is $2m$.

Assume that the incoming rain has negligible angular momentum about the vertical rotation axis and that the net external torque about that axis is zero.

## Conceptual Prediction

The added water increases the system’s moment of inertia.

Because angular momentum is conserved,

$$
L=I\omega=\text{constant}.
$$

If $I$ increases, $\omega$ must decrease. We therefore expect the system to rotate more slowly after the rain is collected.

## Initial Moment of Inertia

Treating each cup as a point mass at radius $d/2$,

$$
I_0
=
m\left(\frac{d}{2}\right)^2
+
m\left(\frac{d}{2}\right)^2.
$$

Therefore,

$$
I_0
=
2m\left(\frac{d^2}{4}\right).
$$

Thus,

$$
\boxed{
I_0=\frac{1}{2}md^2
}.
$$

## Final Moment of Inertia

After the rain is collected, each end has mass $2m$:

$$
I_f
=
2m\left(\frac{d}{2}\right)^2
+
2m\left(\frac{d}{2}\right)^2.
$$

Therefore,

$$
I_f
=
4m\left(\frac{d^2}{4}\right),
$$

so

$$
\boxed{
I_f=md^2
}.
$$

The moment of inertia has doubled:

$$
I_f=2I_0.
$$

## Final Angular Velocity

Angular momentum is conserved:

$$
I_0\omega_0=I_f\omega_f.
$$

Substituting the moments of inertia,

$$
\left(
\frac{1}{2}md^2
\right)
\omega_0
=
\left(
md^2
\right)
\omega_f.
$$

The factors $m$ and $d^2$ cancel:

$$
\frac{1}{2}\omega_0=\omega_f.
$$

Therefore,

$$
\boxed{
\omega_f=\frac{\omega_0}{2}
}.
$$

If the initial angular velocity is

$$
\omega_0=4.2\ \mathrm{rad/s},
$$

then

$$
\boxed{
\omega_f=2.1\ \mathrm{rad/s}
}.
$$

Doubling the moment of inertia reduces the angular velocity by a factor of two.

# Mechanical Energy in the Rotating-Cup System

Although angular momentum is conserved, mechanical energy is not conserved during the collection of the rain.

The rain sticks to the cups in a completely inelastic process. Some of the initial rotational kinetic energy is converted into thermal energy and internal motion as the water collides with and settles inside the cups.

The rotational kinetic energy is

$$
K_{\mathrm{rot}}
=
\frac{1}{2}I\omega^2.
$$

Because the potential energy does not change,

$$
\Delta E_{\mathrm{th}}
=
K_0-K_f.
$$

## Initial Rotational Kinetic Energy

Using

$$
I_0=\frac{1}{2}md^2,
$$

the initial kinetic energy is

$$
K_0
=
\frac{1}{2}
\left(
\frac{1}{2}md^2
\right)
\omega_0^2.
$$

Therefore,

$$
K_0
=
\frac{1}{4}md^2\omega_0^2.
$$

## Final Rotational Kinetic Energy

Using

$$
I_f=md^2
$$

and

$$
\omega_f=\frac{\omega_0}{2},
$$

the final kinetic energy is

$$
K_f
=
\frac{1}{2}
\left(
md^2
\right)
\left(
\frac{\omega_0}{2}
\right)^2.
$$

Therefore,

$$
K_f
=
\frac{1}{2}md^2
\left(
\frac{\omega_0^2}{4}
\right),
$$

so

$$
K_f
=
\frac{1}{8}md^2\omega_0^2.
$$

## Thermal Energy Produced

The mechanical energy converted into thermal and internal energy is

$$
\Delta E_{\mathrm{th}}
=
K_0-K_f.
$$

Substituting,

$$
\Delta E_{\mathrm{th}}
=
\frac{1}{4}md^2\omega_0^2
-
\frac{1}{8}md^2\omega_0^2.
$$

Therefore,

$$
\boxed{
\Delta E_{\mathrm{th}}
=
\frac{1}{8}md^2\omega_0^2
}.
$$

Using the numerical values from the activity gives

$$
\boxed{
\Delta E_{\mathrm{th}}
=
0.47\ \mathrm{J}
}.
$$

This example demonstrates an important distinction:

- Angular momentum is conserved because the net external torque is zero.
- Mechanical energy is not conserved because the process is inelastic.
- Total energy is still conserved; the missing mechanical energy appears as thermal and internal energy.

# Worked Example: Bullet Embedding in a Rotating Cylinder

Consider a uniform solid cylinder viewed from above.

The cylinder has:

- Mass $M$
- Radius $R$
- An initially stationary, frictionless central spindle

A bullet has:

- Mass $m$
- Initial speed $v$

The bullet travels tangent to the cylinder’s rim and embeds in it. We want to determine the final angular velocity of the combined system.

Because the collision occurs over a short time and the spindle force acts through the rotation axis, the external torque about the spindle is negligible. Angular momentum about the spindle is therefore conserved.

The collision is completely inelastic, so mechanical energy is not conserved.

## Initial Angular Momentum

The cylinder is initially at rest, so its initial angular momentum is zero.

The bullet’s initial angular momentum about the spindle is

$$
\vec{L}_i
=
\vec{R}\times m\vec{v}.
$$

The bullet’s velocity is perpendicular to the radial vector at impact, so

$$
L_i=mRv.
$$

Thus,

$$
\boxed{
L_i=mRv
}.
$$

Although the bullet is not initially rotating about its own center, it has angular momentum about the cylinder’s spindle because its line of motion does not pass through the spindle.

## Final Moment of Inertia

After the collision, the cylinder and embedded bullet rotate together.

The moment of inertia of a uniform solid cylinder about its central axis is

$$
I_{\mathrm{cyl}}
=
\frac{1}{2}MR^2.
$$

The embedded bullet can be treated as a point mass at radius $R$:

$$
I_{\mathrm{bullet}}
=
mR^2.
$$

The total final moment of inertia is therefore

$$
I_f
=
\frac{1}{2}MR^2
+
mR^2.
$$

Thus,

$$
\boxed{
I_f
=
\frac{1}{2}MR^2+mR^2
}.
$$

## Conservation of Angular Momentum

The final angular momentum is

$$
L_f=I_f\omega_f.
$$

Conservation of angular momentum gives

$$
L_i=L_f.
$$

Therefore,

$$
mRv
=
\left(
\frac{1}{2}MR^2+mR^2
\right)
\omega_f.
$$

Solving for $\omega_f$,

$$
\omega_f
=
\frac{
mRv
}{
\frac{1}{2}MR^2+mR^2
}.
$$

Factoring $R^2$ from the denominator,

$$
\omega_f
=
\frac{
mRv
}{
R^2\left(\frac{M}{2}+m\right)
}.
$$

Canceling one factor of $R$ gives

$$
\boxed{
\omega_f
=
\frac{
mv
}{
R\left(\frac{M}{2}+m\right)
}
}.
$$

An equivalent form is

$$
\boxed{
\omega_f
=
\frac{2mv}{R(M+2m)}
}.
$$

Using the numerical values supplied in the activity gives

$$
\boxed{
\omega_f
=
0.95\ \mathrm{rad/s}
}.
$$

The spindle may exert a substantial external force during the collision, so the total linear momentum of the bullet–cylinder system is not necessarily conserved. However, because that force acts through the spindle, it produces no torque about the spindle. Angular momentum about that axis is conserved.

# General Strategy for Angular-Momentum Problems

## 1. Choose the System and Rotation Axis

State which objects are included in the system and identify the point or axis about which angular momentum will be calculated.

The torque and angular momentum must be calculated about the same axis.

## 2. Determine Whether External Torque Is Zero

Use

$$
\sum\vec{\tau}_{\mathrm{ext}}
=
\frac{d\vec{L}}{dt}.
$$

If the net external torque about the selected axis is zero or negligible during the interaction, then

$$
\vec{L}_i=\vec{L}_f.
$$

A force acting directly through the chosen axis produces no torque about that axis.

## 3. Calculate the Initial Angular Momentum

For a moving particle,

$$
\vec{L}
=
\vec{r}\times m\vec{v}.
$$

Its magnitude is

$$
L=mrv\sin\phi.
$$

For a rotating rigid body,

$$
L=I\omega.
$$

The total angular momentum is the vector sum of the angular momenta of all components.

## 4. Calculate the Final Moment of Inertia

If objects stick together, include the moment of inertia of every component about the chosen rotation axis:

$$
I_f=\sum_i I_i.
$$

Use the parallel-axis theorem when necessary:

$$
I=I_{\mathrm{cm}}+Md^2.
$$

## 5. Apply Conservation of Angular Momentum

Set

$$
L_i=L_f
$$

and solve for the unknown angular velocity or other requested quantity.

## 6. Analyze Energy Separately

Do not assume that conservation of angular momentum implies conservation of mechanical energy.

In an inelastic collision,

$$
K_i\neq K_f.
$$

The mechanical energy difference is converted into thermal energy, deformation, sound, or other internal forms:

$$
\Delta E_{\mathrm{internal}}
=
K_i-K_f.
$$

# Summary

For an object rolling without slipping,

$$
\boxed{
v_{\mathrm{cm}}=\omega R
}
$$

and

$$
\boxed{
a_{\mathrm{cm}}=\alpha R
}.
$$

For a hollow sphere rolling from rest through a vertical drop $h=d\sin\theta$,

$$
mgh
=
\frac{1}{2}mv^2
+
\frac{1}{2}I\omega^2,
$$

with

$$
I=\frac{2}{3}mR^2
$$

and

$$
\omega=\frac{v}{R}.
$$

The final speed is

$$
\boxed{
v
=
\sqrt{
\frac{6}{5}gd\sin\theta
}
}.
$$

Linear momentum is

$$
\boxed{
\vec{p}=m\vec{v}
},
$$

while angular momentum is

$$
\boxed{
\vec{L}
=
\vec{r}\times\vec{p}
}.
$$

For a particle whose velocity is perpendicular to its position vector,

$$
\boxed{
L=mrv
}.
$$

For a rigid body rotating about a fixed axis,

$$
\boxed{
L=I\omega
}.
$$

Torque changes angular momentum according to

$$
\boxed{
\sum\vec{\tau}_{\mathrm{ext}}
=
\frac{d\vec{L}}{dt}
}.
$$

If the net external torque is zero,

$$
\boxed{
\vec{L}_i=\vec{L}_f
}.
$$

For the rotating-cup system,

$$
I_0=\frac{1}{2}md^2,
$$

$$
I_f=md^2,
$$

and

$$
\boxed{
\omega_f=\frac{\omega_0}{2}
}.
$$

The mechanical energy converted into thermal and internal energy is

$$
\boxed{
\Delta E_{\mathrm{th}}
=
\frac{1}{8}md^2\omega_0^2
}.
$$

For a bullet of mass $m$ and speed $v$ embedding tangentially in the rim of a solid cylinder of mass $M$ and radius $R$,

$$
\boxed{
\omega_f
=
\frac{
mRv
}{
\frac{1}{2}MR^2+mR^2
}
}
$$

or equivalently,

$$
\boxed{
\omega_f
=
\frac{2mv}{R(M+2m)}
}.
$$

Angular momentum can remain conserved during an inelastic collision even when mechanical energy is converted into thermal energy, deformation, and other internal forms.

---

Up Next: [Newtonian Gravitation, Kepler’s Laws, and Orbital Motion](../../../M3/2026-07-15-M3-1/Source/Lecture-Transcript.md)
Previous: [Static Equilibrium and Rotational Dynamics](../../2026-07-13-M2-4/Source/Lecture-Transcript.md)

---
