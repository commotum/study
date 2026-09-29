# Physics 212: Simple and Physical Pendula

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 2 and Quiz 1X are currently being graded.

Quiz 3 will begin near the end of next week and will follow the same format as the first two quizzes. It will cover oscillations and waves, so you should begin preparing your Quiz 3 note sheet.

Because this is an accelerated summer course, we will not spend class time on damping or driven oscillations. Those topics will not appear on Quiz 3 or the final exam. Damping is addressed briefly in the homework.

## From Oscillations to Pendula

In the previous lecture, we introduced simple harmonic motion. Today, we will apply those ideas to pendula.

We will examine two general types of pendulum:

- A **simple pendulum**, in which all of the mass is treated as a point mass suspended from a massless string.
- A **physical pendulum**, in which the oscillating object has an extended mass distribution and therefore has a nontrivial moment of inertia.

Both systems can undergo simple harmonic motion when their angular displacements are sufficiently small.

## Notation

Several similar symbols appear in pendulum problems, so it is important to interpret each one from its context:

- $\tau$ represents torque.
- $T$ represents the period of oscillation.
- $F_T$ represents the tension force.
- $I_p$ represents the moment of inertia about the pivot.
- $M$ represents the total mass of the oscillating system.
- $L$ represents the length of a string, rod, or other object.
- $\ell$ represents the distance from the pivot to the system’s center of mass.
- $\theta$ represents the angular displacement from equilibrium.
- $\omega$ represents angular frequency.

The symbols themselves are less important than the physical quantities and relationships they represent.

## The Restoring Torque of a Pendulum

Consider an object suspended from a fixed pivot. Let $\theta$ be the angle between the pendulum and the downward vertical direction.

The equilibrium position is directly beneath the pivot. If the pendulum is displaced from this position and released, gravity produces a torque that pulls it back toward equilibrium.

The gravitational force is

$$
F_g=Mg.
$$

The tension or support force acts along a line passing through the pivot, so it produces no torque about the pivot.

The tangential component of gravity is

$$
F_{g,t}=-Mg\sin\theta.
$$

The negative sign indicates that this force points opposite the angular displacement. It is therefore a restoring force.

If the center of mass is a distance $\ell$ from the pivot, the torque about the pivot is

$$
\tau_p=-Mg\ell\sin\theta.
$$

The torque is negative because it always acts to reduce $\theta$:

- If $\theta>0$, the torque is negative.
- If $\theta<0$, the torque is positive.

In either case, the torque points toward equilibrium.

## The Small-Angle Approximation

The exact pendulum equation contains $\sin\theta$, which makes the equation nonlinear. For sufficiently small angles measured in radians, however,

$$
\sin\theta\approx\theta.
$$

Using this approximation, the restoring torque becomes

$$
\tau_p\approx-Mg\ell\theta.
$$

The sum of the torques about the pivot is related to angular acceleration by

$$
\sum\tau_p=I_p\alpha,
$$

where

$$
\alpha=\frac{d^2\theta}{dt^2}.
$$

Therefore,

$$
I_p\frac{d^2\theta}{dt^2}
=
-Mg\ell\theta.
$$

Dividing by $I_p$ gives

$$
\frac{d^2\theta}{dt^2}
=
-\frac{Mg\ell}{I_p}\theta.
$$

This has the standard form of the simple harmonic motion equation:

$$
\frac{d^2\theta}{dt^2}
=
-\omega^2\theta.
$$

Comparing the two equations gives

$$
\omega^2=\frac{Mg\ell}{I_p}.
$$

Therefore, the angular frequency of a physical pendulum is

$$
\boxed{
\omega=\sqrt{\frac{Mg\ell}{I_p}}
}.
$$

Because

$$
T=\frac{2\pi}{\omega},
$$

the period is

$$
\boxed{
T=2\pi\sqrt{\frac{I_p}{Mg\ell}}
}.
$$

The ordinary frequency is

$$
\boxed{
f=\frac{1}{2\pi}\sqrt{\frac{Mg\ell}{I_p}}
}.
$$

These formulas assume:

- A small angular displacement
- A rigid oscillating body
- A fixed pivot
- Negligible friction and damping
- A uniform gravitational field

## Angular Simple Harmonic Motion

The angular position of the pendulum may be written as

$$
\theta(t)=\theta_{\max}\cos(\omega t+\phi),
$$

where $\theta_{\max}$ is the maximum angular displacement and $\phi$ is the phase constant.

Differentiating twice gives the angular acceleration:

$$
\alpha(t)
=
\frac{d^2\theta}{dt^2}
=
-\omega^2\theta(t).
$$

This is the rotational equivalent of the translational simple harmonic motion relationship

$$
a(t)=-\omega^2x(t).
$$

In both cases, the acceleration is proportional to the displacement and points in the opposite direction.

## The Parallel-Axis Theorem

For physical pendula, we often need the moment of inertia about a pivot that does not pass through the center of mass.

The parallel-axis theorem states that

$$
I_p=I_{\mathrm{cm}}+Md^2,
$$

where:

- $I_p$ is the moment of inertia about the pivot,
- $I_{\mathrm{cm}}$ is the moment of inertia about a parallel axis through the center of mass,
- $M$ is the object’s mass, and
- $d$ is the distance between the two axes.

We will use this theorem repeatedly when analyzing physical pendula.

## Example 1: Simple Pendulum

Consider a point mass $m$ suspended from a massless string of length $L$.

The mass is released from an angle of $11^\circ$. The value of the angle is not required in the calculation; it indicates that the small-angle approximation is appropriate.

For a point mass a distance $L$ from the pivot, the moment of inertia is

$$
I_p=mL^2.
$$

The center of mass is located at the point mass, so

$$
\ell=L.
$$

Substituting into the general physical-pendulum formula gives

$$
T
=
2\pi
\sqrt{
\frac{mL^2}{mgL}
}.
$$

The mass cancels:

$$
T
=
2\pi
\sqrt{
\frac{L}{g}
}.
$$

Therefore, the period of a simple pendulum is

$$
\boxed{
T=2\pi\sqrt{\frac{L}{g}}
}.
$$

The frequency is

$$
f=\frac{1}{T},
$$

so

$$
\boxed{
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}
}.
$$

Using the length provided in the problem gives approximately

$$
\boxed{
f=0.83\ \mathrm{Hz}
}.
$$

The mass does not appear in either expression. Under the small-angle approximation, the period and frequency of a simple pendulum are independent of both the mass and the initial angular amplitude.

## Example 2: Uniform Rod Pivoted at One End

Now consider a uniform rod of mass $m$ and length $L$, pivoted at one end.

This is a physical pendulum because the mass is distributed throughout the rod rather than concentrated at a single point.

The moment of inertia of a uniform rod about an axis through one end is

$$
I_p=\frac{1}{3}mL^2.
$$

The center of mass of the rod is located at its midpoint, so

$$
\ell=\frac{L}{2}.
$$

Substituting into the period formula gives

$$
T
=
2\pi
\sqrt{
\frac{
\frac{1}{3}mL^2
}{
mg\left(\frac{L}{2}\right)
}
}.
$$

The mass cancels, as does one factor of $L$:

$$
T
=
2\pi
\sqrt{
\frac{2L}{3g}
}.
$$

Therefore,

$$
\boxed{
T=2\pi\sqrt{\frac{2L}{3g}}
}.
$$

Using the numerical length supplied in the problem gives

$$
\boxed{
T=1.6\ \mathrm{s}
}.
$$

Although the total mass cancels, the mass distribution still matters because it determines the moment of inertia and the position of the center of mass.

## Example 3: Uniform Rod with an Offset Pivot

Consider the same uniform rod, but place the pivot a distance $L/6$ from one end.

The center of mass remains at the midpoint of the rod, a distance $L/2$ from that same end. Therefore, the distance from the pivot to the center of mass is

$$
\ell
=
\frac{L}{2}-\frac{L}{6}.
$$

Using a common denominator,

$$
\ell
=
\frac{3L}{6}-\frac{L}{6}
=
\frac{2L}{6}.
$$

Therefore,

$$
\boxed{
\ell=\frac{L}{3}
}.
$$

The moment of inertia about the rod’s center of mass is

$$
I_{\mathrm{cm}}
=
\frac{1}{12}mL^2.
$$

Using the parallel-axis theorem,

$$
I_p
=
I_{\mathrm{cm}}+m\ell^2.
$$

Substituting $\ell=L/3$ gives

$$
I_p
=
\frac{1}{12}mL^2
+
m\left(\frac{L}{3}\right)^2.
$$

Therefore,

$$
I_p
=
\frac{1}{12}mL^2
+
\frac{1}{9}mL^2.
$$

Using a common denominator of $36$,

$$
I_p
=
\frac{3}{36}mL^2
+
\frac{4}{36}mL^2.
$$

Thus,

$$
\boxed{
I_p=\frac{7}{36}mL^2
}.
$$

Substituting into the physical-pendulum formula,

$$
T
=
2\pi
\sqrt{
\frac{
\frac{7}{36}mL^2
}{
mg\left(\frac{L}{3}\right)
}
}.
$$

Canceling the mass and simplifying gives

$$
T
=
2\pi
\sqrt{
\frac{7L}{12g}
}.
$$

Therefore,

$$
\boxed{
T=2\pi\sqrt{\frac{7L}{12g}}
}.
$$

Using the value of $L$ supplied in the problem gives

$$
\boxed{
T=1.3\ \mathrm{s}
}.
$$

Moving the pivot changes both the moment of inertia about the pivot and the distance from the pivot to the center of mass. Both effects must be included.

## Example 4: Uniform Rod with a Point Mass

Consider a uniform rod of length $L$ and mass $m_r$, pivoted at its upper end. A point mass $m_p$ is attached to the lower end.

To calculate the period, we need:

1. The total moment of inertia about the pivot
2. The total mass
3. The location of the combined center of mass

### Total Moment of Inertia

The moment of inertia of the rod about its end is

$$
I_r=\frac{1}{3}m_rL^2.
$$

The point mass is a distance $L$ from the pivot, so its moment of inertia is

$$
I_p^{(\mathrm{point})}=m_pL^2.
$$

The total moment of inertia is

$$
I_{\mathrm{total}}
=
\frac{1}{3}m_rL^2
+
m_pL^2.
$$

Factoring gives

$$
\boxed{
I_{\mathrm{total}}
=
\frac{m_r+3m_p}{3}L^2
}.
$$

### Combined Center of Mass

Take the pivot to be the origin.

The rod’s center of mass is located at $L/2$, and the point mass is located at $L$. Therefore,

$$
\ell
=
\frac{
m_r\left(\frac{L}{2}\right)+m_pL
}{
m_r+m_p
}.
$$

Factoring out $L/2$ gives

$$
\boxed{
\ell
=
\frac{m_r+2m_p}{m_r+m_p}
\frac{L}{2}
}.
$$

The total mass is

$$
M=m_r+m_p.
$$

### Period

The physical-pendulum period is

$$
T
=
2\pi
\sqrt{
\frac{
I_{\mathrm{total}}
}{
Mg\ell
}
}.
$$

Substituting the expressions for $I_{\mathrm{total}}$, $M$, and $\ell$ gives

$$
T
=
2\pi
\sqrt{
\frac{
\frac{m_r+3m_p}{3}L^2
}{
(m_r+m_p)g
\left(
\frac{m_r+2m_p}{m_r+m_p}
\frac{L}{2}
\right)
}
}.
$$

The factor $m_r+m_p$ cancels:

$$
T
=
2\pi
\sqrt{
\frac{
\frac{m_r+3m_p}{3}L^2
}{
g(m_r+2m_p)\frac{L}{2}
}
}.
$$

Simplifying gives

$$
\boxed{
T
=
2\pi
\sqrt{
\frac{2L}{3g}
\frac{m_r+3m_p}{m_r+2m_p}
}
}.
$$

Using the masses and length supplied in the problem gives

$$
\boxed{
T=2.0\ \mathrm{s}
}.
$$

This expression has the correct limiting behavior:

- If $m_p=0$, it reduces to the period of a uniform rod pivoted at one end.
- If the rod’s mass is negligible, it reduces to the period of a simple pendulum of length $L$.

## Example 5: Uniform Rod with an Attached Disk

Now replace the point mass with a solid disk.

Consider:

- A uniform rod of mass $m_r$ and length $L$
- A solid disk of mass $m_d$ and radius $R$
- A pivot at the upper end of the rod
- A disk rigidly attached below the rod
- A distance $L+R$ from the pivot to the disk’s center

Because the disk has a finite size, we must include both its moment of inertia about its own center and the effect of its center being displaced from the pivot.

### Moment of Inertia of the Rod

The rod’s moment of inertia about the pivot is

$$
I_r=\frac{1}{3}m_rL^2.
$$

### Moment of Inertia of the Disk

The moment of inertia of a solid disk about an axis through its center is

$$
I_{d,\mathrm{cm}}
=
\frac{1}{2}m_dR^2.
$$

The disk’s center is a distance

$$
d=L+R
$$

from the pivot.

Using the parallel-axis theorem,

$$
I_{d,p}
=
I_{d,\mathrm{cm}}+m_dd^2.
$$

Therefore,

$$
I_{d,p}
=
\frac{1}{2}m_dR^2
+
m_d(L+R)^2.
$$

The total moment of inertia is

$$
\boxed{
I_{\mathrm{total}}
=
\frac{1}{3}m_rL^2
+
\frac{1}{2}m_dR^2
+
m_d(L+R)^2
}.
$$

### Combined Center of Mass

The rod’s center of mass is located at $L/2$, and the disk’s center of mass is located at $L+R$.

Therefore,

$$
\ell
=
\frac{
m_r\left(\frac{L}{2}\right)
+
m_d(L+R)
}{
m_r+m_d
}.
$$

Thus,

$$
\boxed{
\ell
=
\frac{
\frac{1}{2}m_rL+m_d(L+R)
}{
m_r+m_d
}
}.
$$

### Period

The total mass is

$$
M=m_r+m_d.
$$

Substituting into the physical-pendulum formula gives

$$
T
=
2\pi
\sqrt{
\frac{
\frac{1}{3}m_rL^2
+
\frac{1}{2}m_dR^2
+
m_d(L+R)^2
}{
(m_r+m_d)g
\left[
\frac{
\frac{1}{2}m_rL+m_d(L+R)
}{
m_r+m_d
}
\right]
}
}.
$$

The total-mass factor cancels, leaving

$$
\boxed{
T
=
2\pi
\sqrt{
\frac{
\frac{1}{3}m_rL^2
+
\frac{1}{2}m_dR^2
+
m_d(L+R)^2
}{
g\left[
\frac{1}{2}m_rL+m_d(L+R)
\right]
}
}
}.
$$

Using the values supplied in the problem gives

$$
\boxed{
T=2.5\ \mathrm{s}
}.
$$

The disk cannot be treated as a point mass because it rotates with the rest of the rigid system. Its own rotational inertia,

$$
\frac{1}{2}m_dR^2,
$$

must therefore be included in addition to the parallel-axis contribution,

$$
m_d(L+R)^2.
$$

## General Procedure for Physical-Pendulum Problems

For any small-angle physical-pendulum problem, use the following procedure.

### 1. Choose the Pivot

Identify the fixed axis about which the system rotates.

### 2. Find the Total Moment of Inertia

Calculate the moment of inertia of every component about the pivot:

$$
I_p=\sum_i I_{i,p}.
$$

Use the parallel-axis theorem whenever a component’s known moment of inertia is about an axis through its center of mass rather than through the pivot:

$$
I_{i,p}=I_{i,\mathrm{cm}}+m_id_i^2.
$$

### 3. Locate the Combined Center of Mass

Measure each component’s center-of-mass position from the pivot:

$$
\ell
=
\frac{
\sum_i m_ir_i
}{
\sum_i m_i
}.
$$

### 4. Find the Total Mass

$$
M=\sum_i m_i.
$$

### 5. Calculate the Period

Substitute into

$$
\boxed{
T=2\pi\sqrt{\frac{I_p}{Mg\ell}}
}.
$$

The angular frequency and ordinary frequency can then be found from

$$
\boxed{
\omega=\sqrt{\frac{Mg\ell}{I_p}}
}
$$

and

$$
\boxed{
f=\frac{1}{2\pi}\sqrt{\frac{Mg\ell}{I_p}}
}.
$$

## Summary

For a physical pendulum undergoing small-angle oscillations, the restoring torque is

$$
\tau_p\approx-Mg\ell\theta.
$$

Its equation of motion is

$$
I_p\frac{d^2\theta}{dt^2}
=
-Mg\ell\theta.
$$

The angular frequency is

$$
\boxed{
\omega=\sqrt{\frac{Mg\ell}{I_p}}
}.
$$

The period is

$$
\boxed{
T=2\pi\sqrt{\frac{I_p}{Mg\ell}}
}.
$$

The ordinary frequency is

$$
\boxed{
f=\frac{1}{2\pi}\sqrt{\frac{Mg\ell}{I_p}}
}.
$$

For a simple pendulum,

$$
\boxed{
T=2\pi\sqrt{\frac{L}{g}}
}.
$$

For a uniform rod pivoted at one end,

$$
\boxed{
T=2\pi\sqrt{\frac{2L}{3g}}
}.
$$

The period of a physical pendulum depends on two aspects of its mass distribution:

- The moment of inertia about the pivot
- The distance between the pivot and the center of mass

Changing the pivot location, adding point masses, or attaching extended objects changes one or both of these quantities and therefore changes the oscillation period.

---

Up Next: [From Oscillations to Wave Motion](../../../M5/2026-07-23-M5-1/Source/Lecture-Transcript.md)
Previous: [Oscillations and Simple Harmonic Motion](../../2026-07-21-M4-1/Source/Lecture-Transcript.md)

---
