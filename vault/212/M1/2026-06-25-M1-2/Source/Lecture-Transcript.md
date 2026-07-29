# Physics 212: Covariational Reasoning and Radial Acceleration

Welcome back to Physics 212.

## Announcements

Your Lab 1 discussion submission is due today.

Make sure that you have:

- Posted an introduction in the course discussion
- Joined a laboratory group through the People section in Canvas
- Posted your availability in the linked Google document
- Contacted potential group members whose schedules are compatible with yours

You can use your browser’s search function, such as `Ctrl+F`, to search the course-introduction discussion for students in your time zone, students with compatible availability, or students in a similar academic program.

If you have not yet found a complete group, select a group and continue inviting people to join it so that you can submit the discussion assignment on time. Contact the course staff if you are unable to find a compatible group.

There is no class tomorrow. We will resume class on Monday.

# Continuing Our Study of Circular Motion

Today, we will continue studying circular motion.

We will begin with a rotating apparatus that allows us to practice **covariational reasoning**, symbolic problem solving, and explicit unit analysis. We will then derive the radial acceleration of an object undergoing uniform circular motion.

# A Bullet Passing Through Two Rotating Disks

Consider two disks rigidly attached to the same rotating shaft. The disks are separated by a distance $d$.

Each disk contains a small hole. When viewed along the shaft, the holes are separated by an angular displacement $\theta$. The entire apparatus rotates with constant angular speed and has a rotational period $T$.

A bullet travels parallel to the shaft. It passes through the hole in the first disk and must reach the second disk at exactly the moment when the second hole rotates into alignment with its path.

We want to determine the bullet’s speed $v$.

## Assumptions

For this model, we make the following assumptions:

- The bullet moves sufficiently quickly that the effect of gravity during its flight between the disks is negligible.
- Air resistance is negligible.
- The bullet can be treated as a point particle.
- The bullet travels at constant velocity.
- The two disks are rigidly connected.
- The apparatus rotates at constant angular speed.
- The holes are sufficiently large for the bullet to pass through without interacting with either disk.

The period $T$ is the time required for the apparatus to complete one full revolution.

The frequency is

$$
f=\frac{1}{T},
$$

and the angular speed is

$$
\omega=2\pi f.
$$

Therefore,

$$
\boxed{
\omega=\frac{2\pi}{T}
}.
$$

# Covariational Reasoning

Before solving the problem mathematically, we can predict how the bullet’s speed should depend on $d$, $T$, and $\theta$.

Covariational reasoning asks how the requested quantity changes when one variable changes while the others are held constant.

## Dependence on Disk Separation

Suppose the distance $d$ between the disks increases while $T$ and $\theta$ remain unchanged.

The bullet must then travel a greater distance during the same available time. Its speed must therefore increase:

$$
d\uparrow
\quad\Longrightarrow\quad
v\uparrow.
$$

We consequently expect $d$ to appear in the numerator of the final expression.

## Dependence on the Rotational Period

Suppose the period $T$ increases while $d$ and $\theta$ remain unchanged.

A larger period means the apparatus rotates more slowly. It therefore takes more time for the second hole to rotate into alignment. The bullet can travel more slowly and still pass through both holes:

$$
T\uparrow
\quad\Longrightarrow\quad
v\downarrow.
$$

We consequently expect $T$ to appear in the denominator.

## Dependence on Angular Separation

Suppose the angular separation $\theta$ increases while $d$ and $T$ remain unchanged.

The second disk must rotate through a greater angle before its hole reaches the bullet’s path. This provides the bullet with more travel time, so the required bullet speed decreases:

$$
\theta\uparrow
\quad\Longrightarrow\quad
v\downarrow.
$$

We consequently expect $\theta$ to appear in the denominator.

Before completing the derivation, we therefore expect a relationship of the general form

$$
v\propto\frac{d}{T\theta}.
$$

This prediction does not determine dimensionless numerical factors such as $2\pi$, but it establishes the correct dependence on the physical variables.

## Preliminary Unit Check

The expected combination has units

$$
\left[
\frac{d}{T\theta}
\right]
=
\frac{\mathrm{m}}{\mathrm{s}\cdot\mathrm{rad}}.
$$

Radians are dimensionless, so

$$
\left[
\frac{d}{T\theta}
\right]
=
\mathrm{m/s}.
$$

The predicted form therefore has the correct units for speed.

# Symbolic Derivation of the Bullet’s Speed

We now derive the exact expression from translational and rotational kinematics.

To avoid confusing the apparatus’s rotational period $T$ with the bullet’s travel time, let $\Delta t$ represent the time required for the bullet to travel from the first disk to the second.

## Translational Motion of the Bullet

The general constant-acceleration kinematic equation is

$$
x_f
=
x_0
+
v_0\Delta t
+
\frac{1}{2}a(\Delta t)^2.
$$

The bullet’s acceleration is zero, so

$$
a=0.
$$

Its displacement between the disks is

$$
x_f-x_0=d.
$$

Therefore,

$$
\boxed{
d=v\Delta t
}.
$$

## Rotational Motion of the Disks

The corresponding rotational kinematic equation is

$$
\theta_f
=
\theta_0
+
\omega_0\Delta t
+
\frac{1}{2}\alpha(\Delta t)^2.
$$

The apparatus rotates at constant angular speed, so

$$
\alpha=0.
$$

The angular displacement required to bring the second hole into alignment is $\theta$. Therefore,

$$
\boxed{
\theta=\omega\Delta t
}.
$$

## Eliminating the Travel Time

Divide the translational equation by the rotational equation:

$$
\frac{d}{\theta}
=
\frac{v\Delta t}{\omega\Delta t}.
$$

The travel time cancels:

$$
\frac{d}{\theta}
=
\frac{v}{\omega}.
$$

Solving for $v$ gives

$$
v=\frac{\omega d}{\theta}.
$$

Using

$$
\omega=\frac{2\pi}{T},
$$

we obtain

$$
v
=
\frac{d}{\theta}
\left(
\frac{2\pi}{T}
\right).
$$

Therefore,

$$
\boxed{
v=\frac{2\pi d}{T\theta}
}.
$$

This expression agrees with our covariational prediction:

- $d$ appears in the numerator.
- $T$ appears in the denominator.
- $\theta$ appears in the denominator.
- The remaining factor $2\pi$ is dimensionless.

The angle $\theta$ must be expressed in radians when it is used with angular speed in radians per second.

# Numerical Example

Suppose

$$
d=0.86\ \mathrm{m},
$$

$$
\theta=\frac{\pi}{6}\ \mathrm{rad},
$$

and

$$
T=0.22\ \mathrm{s}.
$$

The bullet speed is

$$
v
=
\frac{
2\pi(0.86\ \mathrm{m})
}{
(0.22\ \mathrm{s})
\left(
\frac{\pi}{6}
\right)
}.
$$

The factor of $\pi$ cancels:

$$
v
=
\frac{
12(0.86\ \mathrm{m})
}{
0.22\ \mathrm{s}
}.
$$

Therefore,

$$
v\approx46.9\ \mathrm{m/s}.
$$

Using two significant figures,

$$
\boxed{
v\approx47\ \mathrm{m/s}
}.
$$

A result near $7.5\ \mathrm{m/s}$ would arise from omitting the factor of $2\pi$ that relates angular speed to rotational period.

# Explicit Unit Analysis

Starting from

$$
v=\frac{2\pi d}{T\theta},
$$

the factor $2\pi$ is dimensionless, and angles measured in radians are also dimensionless. Therefore,

$$
[v]
=
\frac{
\mathrm{m}
}{
\mathrm{s}
}
.
$$

Thus,

$$
\boxed{
[v]=\mathrm{m/s}
},
$$

as required for a speed.

# Uniform Circular Motion

We now turn to the acceleration of an object undergoing uniform circular motion.

An object is in **uniform circular motion** when it moves along a circular path at constant speed.

Constant speed does not mean constant velocity. Velocity is a vector, and its direction changes continuously as the object moves around the circle.

Therefore, an object moving at constant speed around a circle is accelerating even though the magnitude of its velocity remains unchanged.

In **nonuniform circular motion**, both the magnitude and direction of the velocity may change. Such motion can include both radial and tangential acceleration.

# Derivation of Radial Acceleration

Consider an object moving around a circle of radius $r$ at constant speed $v$.

At two nearby points on the path, let the velocity vectors be $\vec v_1$ and $\vec v_2$. Because the speed is constant,

$$
|\vec v_1|=|\vec v_2|=v.
$$

The directions of the vectors differ by a small angle $\Delta\theta$.

The change in velocity is

$$
\Delta\vec v
=
\vec v_2-\vec v_1.
$$

Although the speed does not change, the velocity changes because its direction changes.

## Similar-Triangle Relationship

The two radius vectors and the arc between them form a geometric figure with angle $\Delta\theta$.

The two velocity vectors and their difference $\Delta\vec v$ form a similar figure because each velocity vector is perpendicular to its corresponding radius vector. The angle between the velocity vectors is therefore also $\Delta\theta$.

For a sufficiently small time interval, the arc length $\Delta s$ is approximately a straight segment. The similar triangles then give

$$
\frac{\Delta v}{v}
=
\frac{\Delta s}{r},
$$

where $\Delta v$ is the magnitude of the change in velocity.

Solving for $\Delta v$,

$$
\Delta v
=
\frac{v\Delta s}{r}.
$$

## Taking the Limit

Acceleration is the rate of change of velocity:

$$
a_r
=
\lim_{\Delta t\to0}
\frac{\Delta v}{\Delta t}.
$$

Substituting the similar-triangle result,

$$
a_r
=
\lim_{\Delta t\to0}
\frac{
v\Delta s
}{
r\Delta t
}.
$$

Because $v$ and $r$ are constant for uniform circular motion,

$$
a_r
=
\frac{v}{r}
\lim_{\Delta t\to0}
\frac{\Delta s}{\Delta t}.
$$

The limit

$$
\lim_{\Delta t\to0}
\frac{\Delta s}{\Delta t}
$$

is the speed $v$. Therefore,

$$
a_r
=
\frac{v}{r}v.
$$

Thus, the magnitude of the radial acceleration is

$$
\boxed{
a_r=\frac{v^2}{r}
}.
$$

Using

$$
v=\omega r,
$$

we may also write

$$
a_r
=
\frac{
(\omega r)^2
}{
r
}.
$$

Therefore,

$$
\boxed{
a_r=\omega^2r
}.
$$

# Direction of Radial Acceleration

The vector

$$
\Delta\vec v
=
\vec v_2-\vec v_1
$$

points approximately toward the center of the circle.

As the time interval approaches zero, the direction of $\Delta\vec v$ becomes exactly radial and inward. Because acceleration points in the direction of the change in velocity, radial acceleration always points toward the center of the circular path.

Therefore, radial acceleration has:

- Magnitude

$$
a_r=\frac{v^2}{r}
$$

- Direction toward the center of the circle

If the unit vector $\hat r$ is defined to point outward, the vector form is

$$
\boxed{
\vec a_r
=
-\frac{v^2}{r}\hat r
}.
$$

The negative sign indicates that the acceleration points opposite the outward radial direction.

If the positive radial axis is instead defined to point inward, then the radial component is simply

$$
a_r=+\frac{v^2}{r}.
$$

# Uniform and Nonuniform Circular Motion

For uniform circular motion,

$$
a_t=0,
$$

and the total acceleration is entirely radial:

$$
\vec a=\vec a_r.
$$

It points directly toward the center of the circle.

For nonuniform circular motion, the speed changes, so the object also has tangential acceleration:

$$
\boxed{
a_t=\frac{dv}{dt}
}.
$$

The total acceleration is

$$
\boxed{
\vec a
=
\vec a_r+\vec a_t
}.
$$

Because the radial and tangential directions are perpendicular,

$$
\boxed{
a
=
\sqrt{
a_r^2+a_t^2
}
}.
$$

In this case, the total acceleration does not generally point directly toward the center. The radial component still points inward, while the tangential component points along or opposite the direction of motion.

# Ranking Radial Accelerations

Consider four objects undergoing uniform circular motion.

Their speeds and radii are:

| Object | Speed $v$ | Radius $r$ |
|---|---:|---:|
| A | $1\ \mathrm{m/s}$ | $1\ \mathrm{m}$ |
| B | $2\ \mathrm{m/s}$ | $1\ \mathrm{m}$ |
| C | $2\ \mathrm{m/s}$ | $2\ \mathrm{m}$ |
| D | $1\ \mathrm{m/s}$ | $2\ \mathrm{m}$ |

The radial acceleration is

$$
a_r=\frac{v^2}{r}.
$$

## Object A

$$
a_{r,A}
=
\frac{
(1\ \mathrm{m/s})^2
}{
1\ \mathrm{m}
}.
$$

Therefore,

$$
a_{r,A}=1\ \mathrm{m/s^2}.
$$

## Object B

$$
a_{r,B}
=
\frac{
(2\ \mathrm{m/s})^2
}{
1\ \mathrm{m}
}.
$$

Therefore,

$$
a_{r,B}=4\ \mathrm{m/s^2}.
$$

## Object C

$$
a_{r,C}
=
\frac{
(2\ \mathrm{m/s})^2
}{
2\ \mathrm{m}
}.
$$

Therefore,

$$
a_{r,C}=2\ \mathrm{m/s^2}.
$$

## Object D

$$
a_{r,D}
=
\frac{
(1\ \mathrm{m/s})^2
}{
2\ \mathrm{m}
}.
$$

Therefore,

$$
a_{r,D}=0.50\ \mathrm{m/s^2}.
$$

From smallest to largest, the radial accelerations are

$$
\boxed{
a_{r,D}
<
a_{r,A}
<
a_{r,C}
<
a_{r,B}
}.
$$

Equivalently,

$$
\boxed{
D<A<C<B
}.
$$

This ranking illustrates the different effects of speed and radius:

- Radial acceleration increases with the square of the speed.
- Radial acceleration decreases as the radius increases.

Doubling the speed while holding the radius constant multiplies the radial acceleration by four:

$$
v\rightarrow2v
\quad\Longrightarrow\quad
a_r\rightarrow4a_r.
$$

Doubling the radius while holding the speed constant divides the radial acceleration by two:

$$
r\rightarrow2r
\quad\Longrightarrow\quad
a_r\rightarrow\frac{a_r}{2}.
$$

# General Problem-Solving Strategy

## 1. Define Similar Symbols Carefully

Use distinct symbols for quantities that represent different times.

For example:

- $T$ is the rotational period of the apparatus.
- $\Delta t$ is the bullet’s travel time between the disks.

This prevents the period from being confused with an ordinary elapsed-time interval.

## 2. Identify the Assumptions

Determine whether:

- Linear acceleration is zero
- Angular acceleration is zero
- Gravity can be neglected
- Air resistance can be neglected
- The object can be treated as a particle
- The system rotates rigidly

These assumptions determine which terms may be removed from the general equations.

## 3. Perform Covariational Reasoning

Before calculating, predict how the answer should depend on each given variable.

For the rotating-disk problem,

$$
v\propto\frac{d}{T\theta}.
$$

The final symbolic expression should agree with these predictions.

## 4. Begin with General Equations

For translational motion,

$$
x_f
=
x_0
+
v_0\Delta t
+
\frac{1}{2}a(\Delta t)^2.
$$

For rotational motion,

$$
\theta_f
=
\theta_0
+
\omega_0\Delta t
+
\frac{1}{2}\alpha(\Delta t)^2.
$$

Only after writing the general equations should they be specialized to the particular system.

## 5. Solve Symbolically

Do not substitute numerical values until the requested variable has been isolated.

For the bullet problem, the symbolic result is

$$
v=\frac{2\pi d}{T\theta}.
$$

## 6. Perform an Explicit Unit Check

Substitute the units of each variable and verify that the final expression has the requested dimensions.

## 7. Check Physical Behavior

Ask whether the answer behaves sensibly when each variable increases or decreases.

A mathematically correct-looking expression may still be physically incorrect if it contradicts the expected covariational behavior.

# Summary

The rotational period, frequency, and angular speed are related by

$$
\boxed{
f=\frac{1}{T}
}
$$

and

$$
\boxed{
\omega=2\pi f=\frac{2\pi}{T}
}.
$$

For a bullet passing through two rotating disks separated by distance $d$, with their holes separated by angle $\theta$, the bullet’s travel time satisfies

$$
d=v\Delta t
$$

and

$$
\theta=\omega\Delta t.
$$

Eliminating $\Delta t$ gives

$$
\boxed{
v=\frac{\omega d}{\theta}
}.
$$

Using $\omega=2\pi/T$,

$$
\boxed{
v=\frac{2\pi d}{T\theta}
}.
$$

For

$$
d=0.86\ \mathrm{m},
$$

$$
\theta=\frac{\pi}{6},
$$

and

$$
T=0.22\ \mathrm{s},
$$

the bullet speed is

$$
\boxed{
v\approx47\ \mathrm{m/s}
}.
$$

Uniform circular motion occurs at constant speed but not constant velocity. Because the velocity direction changes, the object has an inward radial acceleration.

The magnitude of radial acceleration is

$$
\boxed{
a_r=\frac{v^2}{r}
}
$$

or equivalently,

$$
\boxed{
a_r=\omega^2r
}.
$$

The radial acceleration always points toward the center of the circular path.

For nonuniform circular motion, the object also has tangential acceleration:

$$
\boxed{
a_t=\frac{dv}{dt}
}.
$$

For the four circular-motion examples considered in the lecture, the radial-acceleration ranking is

$$
\boxed{
D<A<C<B
}.
$$
