# Physics 212: Rotational Kinematics, Angular Acceleration, and the Right-Hand Rule

Welcome back to Physics 212.

## Announcements and Course Resources

The Lab 1 group-formation discussion is due tomorrow. Make sure that you have:

- Posted an introduction in the course discussion
- Contacted potential laboratory partners
- Joined or formed a laboratory group
- Identified a time when your group can meet with a teaching assistant

If other students have not responded to your messages, continue contacting potential group members and complete as much of the group-selection process as possible before the deadline.

You also have access to the Physics 211 course webpages through the Course Information module. These pages contain material used in Physics 211 and may be useful for reviewing translational kinematics. Physics 211 tutorial videos are also available in the module.

## Review of Translational Kinematics

In translational motion, position, velocity, and acceleration are related through differentiation.

Velocity is the time derivative of position:

$$
v(t)=\frac{dx}{dt}.
$$

Acceleration is the time derivative of velocity:

$$
a(t)=\frac{dv}{dt}
=
\frac{d^2x}{dt^2}.
$$

These relationships can be reversed through integration:

$$
v(t)
=
v_0
+
\int_{t_0}^{t}a(t')\,dt',
$$

and

$$
x(t)
=
x_0
+
\int_{t_0}^{t}v(t')\,dt'.
$$

If the acceleration is constant, these integrals produce the familiar translational kinematic equations:

$$
x_f
=
x_0
+
v_0\Delta t
+
\frac{1}{2}a(\Delta t)^2,
$$

$$
v_f=v_0+a\Delta t,
$$

and

$$
v_f^2
=
v_0^2
+
2a(x_f-x_0).
$$

The third equation does not contain new information. It is obtained by eliminating time from the first two equations.

## Rotational Kinematics

The rotational equivalents of position, velocity, and acceleration are:

- Angular position $\theta$
- Angular velocity $\omega$
- Angular acceleration $\alpha$

Arc length and angular displacement are related by

$$
s=r\theta,
$$

where $r$ is the distance from the rotation axis.

Angular velocity is the time derivative of angular position:

$$
\boxed{
\omega=\frac{d\theta}{dt}
}.
$$

Angular acceleration is the time derivative of angular velocity:

$$
\boxed{
\alpha=\frac{d\omega}{dt}
=
\frac{d^2\theta}{dt^2}
}.
$$

For a point at a fixed distance $r$ from the rotation axis, differentiating $s=r\theta$ gives

$$
v_t=r\omega,
$$

where $v_t$ is the tangential speed.

Differentiating again gives

$$
a_t=r\alpha,
$$

where $a_t$ is the tangential acceleration.

The integral relationships are

$$
\omega(t)
=
\omega_0
+
\int_{t_0}^{t}\alpha(t')\,dt',
$$

and

$$
\theta(t)
=
\theta_0
+
\int_{t_0}^{t}\omega(t')\,dt'.
$$

For constant angular acceleration, the rotational kinematic equations are

$$
\boxed{
\theta_f
=
\theta_0
+
\omega_0\Delta t
+
\frac{1}{2}\alpha(\Delta t)^2
},
$$

$$
\boxed{
\omega_f
=
\omega_0
+
\alpha\Delta t
},
$$

and

$$
\boxed{
\omega_f^2
=
\omega_0^2
+
2\alpha(\theta_f-\theta_0)
}.
$$

These have exactly the same mathematical form as the translational kinematic equations:

$$
x\longleftrightarrow\theta,
$$

$$
v\longleftrightarrow\omega,
$$

and

$$
a\longleftrightarrow\alpha.
$$

## Acceleration Components in Circular Motion

Acceleration is a vector and may be resolved into perpendicular components.

In Cartesian coordinates,

$$
\vec{a}
=
a_x\hat{x}
+
a_y\hat{y},
$$

with magnitude

$$
a
=
\sqrt{a_x^2+a_y^2}.
$$

For circular motion, it is often more convenient to use radial and tangential coordinates:

$$
\boxed{
\vec{a}
=
a_r\hat{r}
+
a_t\hat{t}
}.
$$

The magnitude is then

$$
\boxed{
a
=
\sqrt{a_r^2+a_t^2}
}.
$$

The two components have different physical meanings:

- The radial acceleration $a_r$ changes the direction of the velocity.
- The tangential acceleration $a_t$ changes the magnitude of the velocity.

Both $a_r$ and $a_t$ have units of linear acceleration:

$$
[a_r]=[a_t]=\mathrm{m/s^2}.
$$

Angular acceleration has different units:

$$
[\alpha]=\mathrm{rad/s^2}.
$$

For circular-motion problems, it is often convenient to choose the positive radial direction inward, toward the center of the circle.

# Worked Example: A Disk Slowing to Rest

Consider a disk with initial angular speed

$$
\omega_0=12\ \mathrm{rad/s}.
$$

The disk comes to rest after

$$
\Delta t=26\ \mathrm{s}
$$

while undergoing constant angular acceleration.

We want to determine the magnitude and direction of the angular acceleration.

## Known Quantities

The known quantities are

$$
\omega_0=12\ \mathrm{rad/s},
$$

$$
\omega_f=0,
$$

and

$$
\Delta t=26\ \mathrm{s}.
$$

The angular acceleration is constant:

$$
\alpha=\text{constant}.
$$

## Interpreting the Kinematic Graphs

Before performing the calculation, consider the graphs of $\alpha$, $\omega$, and $\theta$ as functions of time.

### Angular Acceleration

If the disk’s initial direction of rotation is defined as positive, then a disk that is slowing down has negative angular acceleration.

Because the angular acceleration is constant, the graph of $\alpha$ versus time is a horizontal line below zero.

### Angular Velocity

The angular velocity begins at $\omega_0$ and decreases linearly to zero.

The slope of an angular-velocity graph is the angular acceleration:

$$
\frac{d\omega}{dt}=\alpha.
$$

Because $\alpha$ is constant and negative, $\omega(t)$ is a straight line with negative slope.

### Angular Position

The slope of the angular-position graph is the angular velocity:

$$
\frac{d\theta}{dt}=\omega.
$$

The disk continues rotating in the positive direction until it stops, so $\theta(t)$ continues increasing.

However, its slope becomes progressively smaller because $\omega$ decreases. The $\theta$ graph is therefore increasing and concave downward. Its slope reaches zero at the instant the disk stops.

Graphically:

- $\alpha(t)$ is constant and negative.
- $\omega(t)$ decreases linearly from $12\ \mathrm{rad/s}$ to zero.
- $\theta(t)$ increases with a decreasing slope.

## Calculating the Angular Acceleration

Use the constant-angular-acceleration equation

$$
\omega_f
=
\omega_0
+
\alpha\Delta t.
$$

Substituting the known values,

$$
0
=
12\ \mathrm{rad/s}
+
\alpha(26\ \mathrm{s}).
$$

Solving for $\alpha$,

$$
\alpha
=
-\frac{12\ \mathrm{rad/s}}{26\ \mathrm{s}}.
$$

Therefore,

$$
\boxed{
\alpha=-0.46\ \mathrm{rad/s^2}
}.
$$

The negative sign indicates that the angular acceleration points opposite the chosen positive direction of rotation.

The magnitude is

$$
\boxed{
|\alpha|=0.46\ \mathrm{rad/s^2}
}.
$$

# Signs of Velocity and Acceleration

The sign of acceleration depends on both the direction of motion and whether the object is speeding up or slowing down.

For one-dimensional translational motion:

| Velocity | Motion | Acceleration |
|---|---|---|
| $v>0$ | Speeding up | $a>0$ |
| $v>0$ | Slowing down | $a<0$ |
| $v<0$ | Speeding up | $a<0$ |
| $v<0$ | Slowing down | $a>0$ |

Acceleration has the same sign as velocity when an object is speeding up. It has the opposite sign when the object is slowing down.

The same reasoning applies to rotational motion:

| Angular velocity | Motion | Angular acceleration |
|---|---|---|
| $\omega>0$ | Speeding up | $\alpha>0$ |
| $\omega>0$ | Slowing down | $\alpha<0$ |
| $\omega<0$ | Speeding up | $\alpha<0$ |
| $\omega<0$ | Slowing down | $\alpha>0$ |

The signs are meaningful only after a positive angular direction has been defined.

# Angular Velocity as a Vector

Describing a rotation as clockwise or counterclockwise is incomplete unless the observer’s viewpoint is specified.

A disk that appears to rotate counterclockwise from above appears to rotate clockwise when viewed from below. The physical rotation has not changed; only the observer’s viewpoint has changed.

To describe rotation unambiguously, angular velocity is treated as a vector directed along the rotation axis.

For circular motion, the tangential velocity is related to angular velocity and position by

$$
\boxed{
\vec{v}
=
\vec{\omega}\times\vec{r}
}.
$$

Here:

- $\vec{r}$ points from the rotation axis to the particle.
- $\vec{v}$ is tangent to the circular path.
- $\vec{\omega}$ points along the rotation axis.
- The three vectors are mutually perpendicular for planar circular motion.

The magnitude of the cross product is

$$
v
=
\omega r\sin\beta,
$$

where $\beta$ is the angle between $\vec{\omega}$ and $\vec{r}$.

For planar circular motion,

$$
\beta=90^\circ,
$$

so

$$
\sin\beta=1.
$$

Therefore,

$$
\boxed{
v=\omega r
}.
$$

The vector $\vec{\omega}$ does not point in the direction that the particle travels. The particle travels tangentially in the plane of rotation. The angular-velocity vector instead identifies:

- The rotation axis
- The sense of rotation about that axis

# The Right-Hand Rule

The direction of a cross product is determined using the right-hand rule.

For a right-handed Cartesian coordinate system,

$$
\boxed{
\hat{x}\times\hat{y}=\hat{z}
}.
$$

One way to apply the rule is:

1. Point the fingers of your right hand along the first vector.
2. Curl them toward the second vector.
3. Your thumb points in the direction of the cross product.

For

$$
\vec{v}
=
\vec{\omega}\times\vec{r},
$$

the first vector is $\vec{\omega}$ and the second is $\vec{r}$. The resulting direction is the tangential velocity $\vec{v}$.

For a rotating disk, a second version of the rule is often convenient:

1. Curl the fingers of your right hand in the direction of rotation.
2. Your thumb points in the direction of $\vec{\omega}$.

If a disk rotates counterclockwise as viewed from above the page, the right-hand rule gives

$$
\vec{\omega}
\text{ directed out of the page}.
$$

If it rotates clockwise as viewed from above, then

$$
\vec{\omega}
\text{ is directed into the page}.
$$

The standard symbols are:

- $\odot$ for a vector pointing out of the page
- $\otimes$ for a vector pointing into the page

## Right-Handed Coordinate System

Suppose the positive $x$- and $y$-axes lie in the plane of the page.

The direction of the positive $z$-axis is defined by

$$
\hat{x}\times\hat{y}=\hat{z}.
$$

Using the right-hand rule, this places the positive $z$-axis out of the page.

If the $z$-axis were instead directed into the page while $x$ and $y$ remained unchanged, the coordinate system would be left-handed.

Physics conventionally uses right-handed coordinate systems.

# Direction of the Disk’s Angular Acceleration

Return to the disk that begins with

$$
\omega_0=12\ \mathrm{rad/s}
$$

and slows to rest.

Suppose the disk is initially rotating counterclockwise as viewed from above. Define that direction as positive.

The right-hand rule then gives

$$
\vec{\omega}_0
\text{ directed out of the page}.
$$

Because the disk is slowing down, the angular acceleration points opposite the angular velocity:

$$
\vec{\alpha}
\text{ directed into the page}.
$$

Thus,

$$
\boxed{
\vec{\alpha}
\text{ points into the page}
}.
$$

Equivalently, if out of the page is the positive $z$-direction,

$$
\boxed{
\alpha<0
}.
$$

If the same counterclockwise rotation were speeding up instead, $\vec{\alpha}$ would point out of the page.

The important sequence is:

1. Define the positive angular direction.
2. Use the right-hand rule to determine the corresponding vector direction.
3. Decide whether $\alpha$ points with or against $\omega$ based on whether the rotation is speeding up or slowing down.

# Worked Example: Total Revolutions Before the Disk Stops

We now want to determine how many revolutions the disk completes while slowing from

$$
\omega_0=12\ \mathrm{rad/s}
$$

to rest over

$$
\Delta t=26\ \mathrm{s}.
$$

The angular-acceleration magnitude is

$$
|\alpha|
=
\frac{\omega_0}{\Delta t}.
$$

Because the acceleration points opposite the rotation,

$$
\alpha=-|\alpha|.
$$

Use the rotational kinematic equation

$$
\omega_f^2
=
\omega_0^2
+
2\alpha\Delta\theta.
$$

The final angular velocity is zero:

$$
0
=
\omega_0^2
-
2|\alpha|\Delta\theta.
$$

Therefore,

$$
2|\alpha|\Delta\theta
=
\omega_0^2.
$$

Solving for the angular displacement,

$$
\Delta\theta
=
\frac{\omega_0^2}{2|\alpha|}.
$$

Using

$$
|\alpha|
=
\frac{\omega_0}{\Delta t},
$$

we obtain

$$
\Delta\theta
=
\frac{
\omega_0^2
}{
2\left(\frac{\omega_0}{\Delta t}\right)
}.
$$

One factor of $\omega_0$ cancels:

$$
\boxed{
\Delta\theta
=
\frac{\omega_0\Delta t}{2}
}.
$$

Substituting the values,

$$
\Delta\theta
=
\frac{
(12\ \mathrm{rad/s})(26\ \mathrm{s})
}{
2
}.
$$

Therefore,

$$
\boxed{
\Delta\theta=156\ \mathrm{rad}
}.
$$

To convert from radians to revolutions, use

$$
1\ \mathrm{rev}=2\pi\ \mathrm{rad}.
$$

The number of revolutions is

$$
N
=
\Delta\theta
\left(
\frac{
1\ \mathrm{rev}
}{
2\pi\ \mathrm{rad}
}
\right).
$$

Thus,

$$
N
=
\frac{
156
}{
2\pi
}.
$$

Equivalently,

$$
N
=
\frac{
\omega_0\Delta t
}{
4\pi
}.
$$

Substituting directly,

$$
N
=
\frac{
(12\ \mathrm{rad/s})(26\ \mathrm{s})
}{
4\pi\ \mathrm{rad/rev}
}.
$$

This gives

$$
N\approx24.8\ \mathrm{rev}.
$$

To two significant figures,

$$
\boxed{
N=25\ \mathrm{revolutions}
}.
$$

## Graphical Check Using Average Angular Velocity

Because the angular acceleration is constant, the average angular velocity is

$$
\omega_{\mathrm{avg}}
=
\frac{\omega_0+\omega_f}{2}.
$$

Therefore,

$$
\omega_{\mathrm{avg}}
=
\frac{
12\ \mathrm{rad/s}
+
0
}{
2
}
=
6.0\ \mathrm{rad/s}.
$$

The angular displacement is

$$
\Delta\theta
=
\omega_{\mathrm{avg}}\Delta t.
$$

Thus,

$$
\Delta\theta
=
(6.0\ \mathrm{rad/s})(26\ \mathrm{s})
=
156\ \mathrm{rad},
$$

which agrees with the kinematic derivation.

Geometrically, this is also the area beneath the angular-velocity-versus-time graph. That graph forms a triangle with base $26\ \mathrm{s}$ and height $12\ \mathrm{rad/s}$:

$$
\Delta\theta
=
\frac{1}{2}
(26\ \mathrm{s})
(12\ \mathrm{rad/s})
=
156\ \mathrm{rad}.
$$

# General Strategy for Rotational-Kinematics Problems

## 1. Define the Positive Angular Direction

Choose whether positive rotation corresponds to clockwise or counterclockwise motion from a stated viewpoint.

Use the right-hand rule to associate that rotation with a vector direction along the rotation axis.

## 2. Identify the Known Quantities

List quantities such as

$$
\theta_0,
\qquad
\theta_f,
\qquad
\omega_0,
\qquad
\omega_f,
\qquad
\alpha,
\qquad
\Delta t.
$$

Do not substitute numbers immediately.

## 3. Sketch the Kinematic Graphs

Draw qualitative graphs of

$$
\alpha(t),
\qquad
\omega(t),
\qquad
\theta(t).
$$

Check that:

- The slope of $\omega(t)$ agrees with $\alpha(t)$.
- The slope of $\theta(t)$ agrees with $\omega(t)$.
- The concavity of $\theta(t)$ agrees with the sign of $\alpha$.

## 4. Select an Equation Containing the Known and Unknown Quantities

For constant angular acceleration, choose among

$$
\theta_f
=
\theta_0
+
\omega_0\Delta t
+
\frac{1}{2}\alpha(\Delta t)^2,
$$

$$
\omega_f
=
\omega_0
+
\alpha\Delta t,
$$

and

$$
\omega_f^2
=
\omega_0^2
+
2\alpha(\theta_f-\theta_0).
$$

## 5. Solve Symbolically

Isolate the requested variable before inserting numerical values.

A symbolic solution makes it easier to:

- Track signs
- Check dimensions
- Identify cancellations
- Interpret how the result depends on each variable
- Detect algebraic errors

## 6. Check the Direction and Magnitude Separately

A vector quantity may have a negative component even though its magnitude is positive.

For the slowing disk,

$$
\alpha=-0.46\ \mathrm{rad/s^2},
$$

while

$$
|\alpha|=0.46\ \mathrm{rad/s^2}.
$$

## 7. Convert Angular Units Carefully

Use

$$
1\ \mathrm{rev}=2\pi\ \mathrm{rad}
$$

when converting between radians and revolutions.

# Summary

Translational and rotational kinematics have parallel mathematical structures:

$$
x\longleftrightarrow\theta,
$$

$$
v\longleftrightarrow\omega,
$$

and

$$
a\longleftrightarrow\alpha.
$$

Angular velocity and angular acceleration are

$$
\boxed{
\omega=\frac{d\theta}{dt}
}
$$

and

$$
\boxed{
\alpha=\frac{d\omega}{dt}
}.
$$

For constant angular acceleration,

$$
\boxed{
\theta_f
=
\theta_0
+
\omega_0\Delta t
+
\frac{1}{2}\alpha(\Delta t)^2
},
$$

$$
\boxed{
\omega_f
=
\omega_0
+
\alpha\Delta t
},
$$

and

$$
\boxed{
\omega_f^2
=
\omega_0^2
+
2\alpha(\theta_f-\theta_0)
}.
$$

For planar circular motion,

$$
\boxed{
\vec{v}
=
\vec{\omega}\times\vec{r}
}.
$$

When $\vec{\omega}$ and $\vec{r}$ are perpendicular,

$$
\boxed{
v=\omega r
}.
$$

Angular velocity points along the rotation axis, with its direction determined by the right-hand rule.

For the disk that slows from $12\ \mathrm{rad/s}$ to rest in $26\ \mathrm{s}$,

$$
\boxed{
\alpha=-0.46\ \mathrm{rad/s^2}
}.
$$

Its angular-acceleration magnitude is

$$
\boxed{
|\alpha|=0.46\ \mathrm{rad/s^2}
}.
$$

If the disk initially rotates counterclockwise as viewed from above, then $\vec{\omega}$ points out of the page. Because the disk is slowing down, $\vec{\alpha}$ points into the page.

The disk turns through

$$
\boxed{
\Delta\theta=156\ \mathrm{rad}
}
$$

before stopping, corresponding to

$$
\boxed{
N\approx25\ \mathrm{revolutions}
}.
$$

