# Physics 212: Nonuniform Circular Motion and Tangential Projectile Motion

Welcome back to Physics 212.

## Announcements

There is no class on Friday. Quiz 1 will be administered on Monday, and the entire Monday class period will be devoted to the quiz.

### Quiz Format

Quiz 1 contains two required parts.

Part A contains:

- Three multiple-choice questions
- One short written-response question

Part B contains one longer written-response problem.

The quiz covers the material from Chapters 4 and 8, including rotational kinematics and forces in circular motion. A detailed coverage announcement and a practice quiz will be posted before the quiz.

Each part allows approximately:

- $20$ minutes to complete the questions
- $5$ additional minutes to upload written work

There will be a short break between Parts A and B. The two parts may be completed in either order, and the proctoring methods may be mixed if necessary, although most students use the same method for both parts.

### Zoom Proctoring

Zoom-proctored sessions will be available Monday at 11:00 a.m. and 6:00 p.m.

Students using Zoom proctoring must:

- Have a functioning webcam
- Keep the webcam on throughout the quiz
- Keep the microphone muted unless communicating with the instructor
- Upload written work during the designated upload periods

### Proctorio

The Proctorio version will open Saturday at 5:00 p.m. and close Monday at 5:00 p.m.

The Canvas portions of Quiz 1A and Quiz 1B will close at 4:55 p.m. The corresponding Gradescope work assignments will remain open until 5:00 p.m., providing five additional minutes for uploading written work.

Complete the Proctorio practice quiz before Quiz 1 to confirm that the software is working correctly.

While using Proctorio:

- Do not open additional browser tabs.
- Do not use keyboard shortcuts to leave the quiz.
- Use a handheld calculator or the calculator built into Proctorio.
- Do not use an online calculator such as Desmos.
- Looking down at the authorized physical note sheet is permitted, even if Proctorio flags it as looking away from the screen.

### Required Note Sheet

A handwritten note sheet must be submitted to the Quiz 1 Notes assignment in Gradescope.

The note sheet must:

- Be between one-half page and one full page
- Be written entirely by hand on paper
- Be submitted with a photo ID visible on top of it

An Oregon State University ID or another valid photo ID may be used. Sensitive information, such as an address, may be covered before the image is taken.

For ordinary handwritten assignments, writing with a stylus on a tablet is acceptable. The quiz note sheet, however, must be written on physical paper.

The deadline for uploading the M2-1 assignment to Gradescope has been extended until 10:00 p.m. tonight.

# Review of Translational and Rotational Kinematics

Before studying nonuniform circular motion, we will briefly review the relationships among position, velocity, and acceleration.

## Translational Motion

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

These relationships may be reversed using integration:

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

When acceleration is constant, the familiar kinematic equations are

$$
v_f=v_i+a\Delta t,
$$

$$
x_f
=
x_i
+
v_i\Delta t
+
\frac{1}{2}a(\Delta t)^2,
$$

and

$$
v_f^2
=
v_i^2
+
2a(x_f-x_i).
$$

## Rotational Motion

The angular equivalents of position, velocity, and acceleration are $\theta$, $\omega$, and $\alpha$.

Angular velocity is

$$
\omega(t)=\frac{d\theta}{dt},
$$

and angular acceleration is

$$
\alpha(t)
=
\frac{d\omega}{dt}
=
\frac{d^2\theta}{dt^2}.
$$

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

For constant angular acceleration,

$$
\omega_f
=
\omega_i+\alpha\Delta t,
$$

$$
\theta_f
=
\theta_i
+
\omega_i\Delta t
+
\frac{1}{2}\alpha(\Delta t)^2,
$$

and

$$
\omega_f^2
=
\omega_i^2
+
2\alpha(\theta_f-\theta_i).
$$

The translational and rotational variables correspond as follows:

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

# Radial and Tangential Acceleration

Acceleration is a vector. It can be resolved into ordinary Cartesian components,

$$
\vec{a}
=
a_x\hat{x}
+
a_y\hat{y},
$$

or into radial and tangential components:

$$
\boxed{
\vec{a}
=
a_r\hat{r}
+
a_t\hat{t}
}.
$$

The radial and tangential directions are perpendicular to one another and rotate with the moving particle.

In this lecture, the positive radial direction is chosen to point inward, toward the center of the circular path.

For motion along a circle of fixed radius $r$, the radial acceleration is

$$
\boxed{
a_r=\frac{v^2}{r}
}
$$

or equivalently,

$$
a_r=\omega^2r.
$$

The tangential acceleration describes the rate at which the speed changes:

$$
\boxed{
a_t=\frac{dv}{dt}
}.
$$

It is related to angular acceleration by

$$
\boxed{
a_t=\alpha r
}.
$$

Both $a_r$ and $a_t$ have units of acceleration, such as $\mathrm{m/s^2}$. Angular acceleration has units of $\mathrm{rad/s^2}$.

Because the two components are perpendicular, the magnitude of the total acceleration is

$$
\boxed{
a
=
\sqrt{a_r^2+a_t^2}
}.
$$

# Uniform and Nonuniform Circular Motion

In **uniform circular motion**, the particle moves at constant speed.

Its velocity is not constant because the direction of the velocity continually changes. The particle therefore has radial acceleration even though its speed is constant:

$$
a_r=\frac{v^2}{r},
$$

$$
a_t=0.
$$

The total acceleration points directly toward the center of the circle.

In **nonuniform circular motion**, the particle’s speed changes. The particle then has both radial and tangential acceleration:

$$
a_r\neq0,
$$

$$
a_t\neq0.
$$

The radial component changes the direction of the velocity, while the tangential component changes its magnitude.

# Direction of the Net Force

Newton’s second law is

$$
\vec{F}_{\mathrm{net}}=m\vec{a}.
$$

Because mass is a positive scalar, the net-force vector points in the same direction as the acceleration vector.

Consider a particle moving clockwise around a circle and speeding up.

Its radial acceleration points toward the center of the circle. Its tangential acceleration points along the clockwise direction of motion because the particle is speeding up.

The total acceleration is the vector sum

$$
\vec{a}
=
\vec{a}_r+\vec{a}_t.
$$

The resulting acceleration points partly inward and partly forward along the path.

If the same clockwise-moving particle were slowing down, the tangential acceleration would point opposite its velocity. The resultant acceleration would still point inward, but it would be tilted backward relative to the direction of motion.

This distinction is important:

- Radial acceleration determines the curvature of the path.
- Tangential acceleration determines whether the particle speeds up or slows down.

# Ball Moving in a Vertical Circle

Consider a ball of mass $m$ attached to a string of length $L$.

At the instant under consideration, the inward radial direction lies along the string and makes an angle $\theta$ with the downward vertical. The ball is moving upward along the tangent to the circle and is slowing down.

Let:

- $F_T$ be the tension in the string
- $m$ be the ball’s mass
- $L$ be the string length
- $\theta$ be the angle shown in the problem
- $+\hat{r}$ point inward toward the center
- $+\hat{t}$ point in the direction of gravity’s tangential component

The forces on the ball are:

- The tension $F_T$, directed inward along the string
- The gravitational force $mg$, directed vertically downward

The gravitational force can be resolved into radial and tangential components:

$$
F_{g,r}=mg\cos\theta,
$$

and

$$
F_{g,t}=mg\sin\theta.
$$

When resolving a force into components, the sides of the component triangle must be parallel to the selected coordinate axes. The correct sine or cosine follows from that geometry.

## Radial Acceleration

Both the tension and the radial component of gravity point inward. Therefore,

$$
\sum F_r=ma_r.
$$

Substituting the radial forces gives

$$
F_T+mg\cos\theta=ma_r.
$$

Solving for the radial acceleration,

$$
\boxed{
a_r
=
\frac{F_T}{m}
+
g\cos\theta
}.
$$

Using the values supplied in the problem gives

$$
a_r=11.7\ \mathrm{m/s^2}.
$$

To two significant figures,

$$
\boxed{
a_r\approx12\ \mathrm{m/s^2}
}.
$$

## Tangential Acceleration

The tension points entirely in the radial direction, so it has no tangential component.

The only tangential force is the tangential component of gravity:

$$
\sum F_t=ma_t.
$$

Therefore,

$$
mg\sin\theta=ma_t.
$$

The mass cancels, giving

$$
\boxed{
a_t=g\sin\theta
}.
$$

Using the given angle,

$$
\boxed{
a_t=2.4\ \mathrm{m/s^2}
}.
$$

The positive tangential direction was chosen to point along gravity’s tangential component. Because the ball’s velocity points in the opposite direction, the tangential acceleration opposes the velocity. The ball is therefore slowing down.

## Total Acceleration

The radial and tangential accelerations are perpendicular, so the total magnitude is

$$
a
=
\sqrt{a_r^2+a_t^2}.
$$

Substituting the component expressions,

$$
a
=
\sqrt{
\left(
\frac{F_T}{m}
+
g\cos\theta
\right)^2
+
\left(
g\sin\theta
\right)^2
}.
$$

Thus,

$$
\boxed{
a
=
\sqrt{
\left(
\frac{F_T}{m}
+
g\cos\theta
\right)^2
+
g^2\sin^2\theta
}
}.
$$

Using the numerical values gives

$$
a=11.9\ \mathrm{m/s^2}.
$$

To two significant figures,

$$
\boxed{
a\approx12\ \mathrm{m/s^2}
}.
$$

The total acceleration is slightly larger than the radial acceleration alone because it also includes the tangential component.

# Speed of the Ball

For circular motion,

$$
a_r=\frac{v^2}{r}.
$$

The radius of the ball’s path is the string length:

$$
r=L.
$$

Therefore,

$$
a_r=\frac{v^2}{L}.
$$

Substituting the radial-acceleration expression,

$$
\frac{v^2}{L}
=
\frac{F_T}{m}
+
g\cos\theta.
$$

Multiplying by $L$ gives

$$
v^2
=
L
\left(
\frac{F_T}{m}
+
g\cos\theta
\right).
$$

Therefore,

$$
\boxed{
v^2
=
\frac{F_TL}{m}
+
gL\cos\theta
}
$$

and

$$
\boxed{
v
=
\sqrt{
\frac{F_TL}{m}
+
gL\cos\theta
}
}.
$$

This is the ball’s instantaneous speed immediately before the string is cut.

# Cutting the String

Suppose the string is cut at the instant described above.

Immediately after the cut:

- The tension force disappears.
- The ball’s position does not change instantaneously.
- The ball’s velocity does not change instantaneously.
- The ball continues with the velocity it had at the moment of release.
- That velocity is tangent to the circular path.

After the cut, the ball becomes a projectile acted on only by gravity.

Because the tangent makes an angle $\theta$ above the horizontal, the initial velocity components are

$$
v_{0x}=v_0\cos\theta
$$

and

$$
v_{0y}=v_0\sin\theta.
$$

We want to determine the ball’s maximum height above its release point.

## Maximum-Height Calculation

The vertical kinematic equation that does not contain time is

$$
v_y^2
=
v_{0y}^2
+
2a_y\Delta y.
$$

At the maximum height,

$$
v_y=0.
$$

The vertical acceleration is

$$
a_y=-g.
$$

The initial vertical velocity is

$$
v_{0y}=v_0\sin\theta.
$$

Substituting,

$$
0
=
v_0^2\sin^2\theta
-
2g\Delta y_{\max}.
$$

Therefore,

$$
2g\Delta y_{\max}
=
v_0^2\sin^2\theta.
$$

Solving for the maximum vertical displacement,

$$
\boxed{
\Delta y_{\max}
=
\frac{
v_0^2\sin^2\theta
}{
2g
}
}.
$$

From the circular-motion analysis,

$$
v_0^2
=
\frac{F_TL}{m}
+
gL\cos\theta.
$$

Substituting this into the projectile-motion result gives

$$
\boxed{
\Delta y_{\max}
=
\frac{
\left(
\frac{F_TL}{m}
+
gL\cos\theta
\right)
\sin^2\theta
}{
2g
}
}.
$$

This expression is entirely in terms of the given quantities $F_T$, $L$, $m$, $\theta$, and $g$.

Using the numerical values supplied in the problem gives

$$
\boxed{
\Delta y_{\max}=0.031\ \mathrm{m}
}.
$$

The ball rises approximately $3.1\ \mathrm{cm}$ above its release point.

# General Strategy for Nonuniform Circular-Motion Problems

## 1. Draw the Physical Situation

Translate the written problem into a labeled diagram. Include the radius, angles, velocity direction, and relevant positions.

## 2. Draw a Free-Body Diagram

Include only forces acting directly on the selected particle.

For the ball-on-a-string problem, the forces are tension and gravity.

## 3. Choose Radial and Tangential Axes

The radial axis should be aligned with the radius of the circle. Choosing inward as positive makes the radial acceleration

$$
a_r=\frac{v^2}{r}
$$

positive.

The tangential axis must be perpendicular to the radial axis.

## 4. Resolve Forces Along the Selected Axes

Construct component triangles whose sides are parallel to the radial and tangential axes.

Do not use an angle merely because it is labeled in the original diagram. Use the angle between the force and the relevant axis.

## 5. Apply Newton’s Second Law Separately

Write

$$
\sum F_r=ma_r
$$

and

$$
\sum F_t=ma_t.
$$

The radial equation describes the curvature of the path. The tangential equation describes the change in speed.

## 6. Combine Perpendicular Components

Use

$$
a=\sqrt{a_r^2+a_t^2}
$$

to find the magnitude of the total acceleration.

## 7. Solve Symbolically First

Keep the calculation in variables until the requested quantity has been isolated.

A symbolic result makes it easier to:

- Check units
- Identify cancellations
- Analyze signs
- Interpret how variables affect the result
- Detect algebraic errors

## 8. Substitute Numerical Values Last

Insert numerical values only after obtaining a complete symbolic expression.

# Summary

Translational and rotational quantities are related by

$$
v=\frac{dx}{dt},
$$

$$
a=\frac{dv}{dt},
$$

$$
\omega=\frac{d\theta}{dt},
$$

and

$$
\alpha=\frac{d\omega}{dt}.
$$

For circular motion with inward defined as positive,

$$
\boxed{
a_r=\frac{v^2}{r}
}
$$

and

$$
\boxed{
a_t=\frac{dv}{dt}=\alpha r
}.
$$

The total acceleration magnitude is

$$
\boxed{
a=\sqrt{a_r^2+a_t^2}
}.
$$

In uniform circular motion,

$$
a_t=0,
$$

so acceleration points directly toward the center.

In nonuniform circular motion, both radial and tangential acceleration may be present.

For the ball-on-a-string system,

$$
\boxed{
a_r
=
\frac{F_T}{m}
+
g\cos\theta
},
$$

$$
\boxed{
a_t=g\sin\theta
},
$$

and

$$
\boxed{
a
=
\sqrt{
\left(
\frac{F_T}{m}
+
g\cos\theta
\right)^2
+
g^2\sin^2\theta
}
}.
$$

The ball’s instantaneous speed is determined by

$$
\boxed{
v^2
=
\frac{F_TL}{m}
+
gL\cos\theta
}.
$$

When the string is cut, the ball leaves the circular path tangent to the circle and becomes a projectile.

Its maximum height above the release point is

$$
\boxed{
\Delta y_{\max}
=
\frac{
\left(
\frac{F_TL}{m}
+
gL\cos\theta
\right)
\sin^2\theta
}{
2g
}
}.
$$

For the values used in the problem,

$$
\boxed{
\Delta y_{\max}=0.031\ \mathrm{m}
}.
$$