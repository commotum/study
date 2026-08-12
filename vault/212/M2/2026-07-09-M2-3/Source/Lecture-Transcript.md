# Physics 212: Torque, Moment Arms, and Rotational Dynamics

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 1 is currently being graded, and scores should be available by Monday. Once the scores are posted, the optional Quiz 1X extra-credit assignment will open.

Quiz 1X must address the Quiz 1 problem on which you lost the most points. Although the lowest Quiz Part A score and the lowest Quiz Part B score are dropped at the end of the term, any extra-credit points earned through Quiz 1X are retained even if Quiz 1 is ultimately one of your dropped scores.

You should also be working on this week’s laboratory assignment.

Attendance and active participation in your scheduled laboratory meeting contribute to your discussion grade. If you cannot attend your regular meeting, contact your laboratory TA in advance and arrange to attend another meeting if possible.

Each laboratory group submits one group report. The names and email addresses included with the submission should be those of the students who actively contributed to preparing the report. Posting in the discussion area without participating in the preparation of the report is not sufficient. If a group member is not responding or contributing, contact your laboratory TA.

## Introduction to Torque

Torque describes the tendency of a force to produce rotation about a chosen point or axis.

The torque produced by a force is defined by the cross product

$$
\boxed{
\vec{\tau}=\vec{r}\times\vec{F}
}
$$

where:

- $\vec{r}$ is the position vector from the pivot to the point where the force is applied
- $\vec{F}$ is the applied force
- $\vec{\tau}$ is the resulting torque

The rotational form of Newton’s second law is

$$
\boxed{
\sum\vec{\tau}=I\vec{\alpha}
}
$$

where:

- $I$ is the moment of inertia about the selected rotation axis
- $\vec{\alpha}$ is the angular acceleration

This equation is analogous to the translational equation

$$
\sum\vec{F}=m\vec{a}.
$$

In translational motion, mass measures an object’s resistance to linear acceleration. In rotational motion, the moment of inertia measures the object’s resistance to angular acceleration. The moment of inertia depends on both the amount of mass and how that mass is distributed relative to the rotation axis.

## Magnitude of Torque

The magnitude of the cross product is

$$
\boxed{
\tau=rF\sin\theta
}
$$

where $\theta$ is the angle between $\vec{r}$ and $\vec{F}$.

This equation shows that torque depends on three factors:

- The magnitude of the force
- The distance from the pivot to the point where the force is applied
- The angle between the position vector and the force

The SI unit of torque is the newton-meter:

$$
\boxed{
[\tau]=\mathrm{N}\,\mathrm{m}
}.
$$

## The Tangential Component of Force

Only the component of force perpendicular to the position vector produces torque.

The tangential component of the force is

$$
F_{\perp}=F\sin\theta.
$$

Therefore, the torque magnitude can also be written as

$$
\tau=rF_{\perp}.
$$

A force applied perpendicular to $\vec{r}$ produces the greatest possible torque for a given force and distance:

$$
\theta=90^\circ
\quad\Longrightarrow\quad
\tau=rF.
$$

A force directed along the position vector produces no torque:

$$
\theta=0^\circ
\quad\Longrightarrow\quad
\tau=0.
$$

This explains why a door is easiest to open by pushing perpendicular to its surface near the edge farthest from the hinges. Pushing near the hinges gives a small value of $r$, while pushing at an angle reduces the tangential component of the force.

In the force comparison shown in the lecture, $F_1$ produced the greatest torque because it acted far from the hinge and in the most effective direction.

## Moment Arm and Line of Action

Torque can also be expressed using a **moment arm**.

The line of action of a force is the infinite line extending in the direction of the force. The moment arm $d$ is the shortest perpendicular distance from the pivot to that line.

From the geometry,

$$
d=r\sin\theta.
$$

The torque magnitude can therefore be written as

$$
\boxed{
\tau=Fd
}.
$$

The two forms

$$
\tau=rF\sin\theta
$$

and

$$
\tau=Fd
$$

are equivalent.

Using $rF\sin\theta$ is often the most direct method when the position vector, force, and angle are clearly shown. The moment-arm method can be convenient when the line of action is easier to identify than the angle.

## Worked Example: Torque Applied to a Wrench

Consider a wrench with a force applied at its end.

The given quantities are

$$
r=52\ \mathrm{cm}=0.52\ \mathrm{m},
$$

$$
F=120\ \mathrm{N},
$$

and a marked angle

$$
\phi=33^\circ.
$$

The marked $33^\circ$ angle is not the angle between the position vector and the force. The angle needed in the torque equation is

$$
\theta=90^\circ-\phi.
$$

Therefore,

$$
\theta=90^\circ-33^\circ=57^\circ.
$$

The torque magnitude is

$$
\tau=rF\sin\theta.
$$

Substituting the known values,

$$
\tau
=
(0.52\ \mathrm{m})
(120\ \mathrm{N})
\sin(57^\circ).
$$

This gives

$$
\boxed{
\tau\approx52\ \mathrm{N}\,\mathrm{m}
}.
$$

Using the supplementary angle would give the same result because

$$
\sin(123^\circ)=\sin(57^\circ).
$$

The important point is that the angle in

$$
\tau=rF\sin\theta
$$

must be an angle between $\vec{r}$ and $\vec{F}$, not simply whichever angle happens to be labeled in the diagram.

## Direction of Torque

Torque is a vector. Its direction is determined by the cross product

$$
\vec{\tau}=\vec{r}\times\vec{F}.
$$

The vectors $\vec{r}$ and $\vec{F}$ lie in a plane. The torque vector must be perpendicular to that plane.

When $\vec{r}$ and $\vec{F}$ lie in the plane of the page, the torque must point either:

- Out of the page
- Into the page

The right-hand rule determines which direction applies.

Point the fingers of your right hand along $\vec{r}$ and curl them toward $\vec{F}$. Your thumb points in the direction of $\vec{\tau}$.

For the wrench example, the right-hand rule gives a torque directed into the page:

$$
\boxed{
\vec{\tau}\text{ points into the page}
}.
$$

The usual diagram symbols are:

- $\odot$ for a vector directed out of the page
- $\otimes$ for a vector directed into the page

The downward direction of the applied force is not the direction of the torque. The force lies in the plane of the page, while the torque is perpendicular to that plane.

## Point and Extended Free-Body Diagrams

A point-particle free-body diagram is sufficient for translational motion because the sum of the forces does not depend on where the forces are applied.

Torque does depend on the point of application. Rotational problems therefore require an **extended free-body diagram**.

An extended free-body diagram should show:

- The physical shape of the object
- The selected pivot or rotation axis
- Every force acting on the object
- The point where each force is applied
- The distance from the pivot to each force
- The angle between each position vector and force

A force may be present on the free-body diagram but contribute no torque. This occurs when its line of action passes through the pivot.

In that situation, the force is not zero. Its lever arm is zero:

$$
r_{\perp}=0
\quad\Longrightarrow\quad
\tau=0.
$$

## Worked Example: Spool Pulled by a Constant Tension

Consider a solid cylindrical spool of mass $m$ and radius $r$ mounted on a frictionless fixed spindle.

A cord is wrapped around the spool and pulled with a constant tension $F_T$. Because the tension and moment of inertia are constant, the torque and angular acceleration are also constant.

The spool rotates faster and faster, but its center does not translate because the spindle holds it in place.

### Translational Free-Body Diagram

From the side view, the forces include:

- The gravitational force $mg$ downward
- An upward support force $N_1$
- The cord tension $F_T$ horizontally
- A horizontal spindle reaction $N_2$

Because the spool’s center does not accelerate,

$$
\sum F_x=0
$$

and

$$
\sum F_y=0.
$$

In the horizontal direction,

$$
F_T-N_2=0.
$$

Therefore,

$$
N_2=F_T.
$$

In the vertical direction,

$$
N_1-mg=0.
$$

Therefore,

$$
N_1=mg.
$$

These force equations describe the lack of translational acceleration, but they do not determine the angular acceleration.

### Extended Free-Body Diagram

Viewed along the rotation axis, the cord tension acts tangentially at the rim.

The angle between the radius and tension is

$$
90^\circ,
$$

so the torque magnitude is

$$
\tau=F_T r.
$$

The spindle reaction acts through the pivot. It may be nonzero, but its torque about the spindle is zero because its lever arm is zero.

The rotational equation is

$$
\sum\tau_p=I_p\alpha.
$$

Therefore,

$$
F_T r=I_p\alpha.
$$

For a uniform solid cylinder,

$$
I_p=\frac{1}{2}mr^2.
$$

Substituting,

$$
F_T r
=
\left(
\frac{1}{2}mr^2
\right)
\alpha.
$$

Solving for the angular acceleration,

$$
\alpha
=
\frac{F_T r}{
\frac{1}{2}mr^2
}.
$$

Therefore,

$$
\boxed{
\alpha=\frac{2F_T}{mr}
}.
$$

Using the numerical values supplied in the activity gives

$$
\boxed{
\alpha=2.7\ \mathrm{rad}/\mathrm{s}^2
}.
$$

The central idea is that the support force does not disappear. Its torque disappears because it acts at the pivot.

## Worked Example: Two Coaxial Solid Cylinders

Consider two solid cylinders rigidly attached along the same rotation axis.

The larger cylinder has:

- Mass $M$
- Radius $R$

The smaller cylinder has:

- Unknown mass $m$
- Radius $r$

A tangential force $F$ is applied to the outer edge of the larger cylinder. The two cylinders rotate together with angular acceleration $\alpha$.

We want to determine the mass $m$ of the smaller cylinder.

### Applied Torque

Because the force is tangential to the larger cylinder,

$$
\theta=90^\circ.
$$

The applied torque is therefore

$$
\tau=FR.
$$

### Total Moment of Inertia

The moment of inertia of the larger solid cylinder is

$$
I_M=\frac{1}{2}MR^2.
$$

The moment of inertia of the smaller solid cylinder is

$$
I_m=\frac{1}{2}mr^2.
$$

Because the cylinders are rigidly attached and rotate about the same axis, their moments of inertia add:

$$
I_{\mathrm{total}}
=
I_M+I_m.
$$

Therefore,

$$
I_{\mathrm{total}}
=
\frac{1}{2}MR^2
+
\frac{1}{2}mr^2.
$$

### Rotational Equation of Motion

Using

$$
\sum\tau=I_{\mathrm{total}}\alpha,
$$

we obtain

$$
FR
=
\left(
\frac{1}{2}MR^2
+
\frac{1}{2}mr^2
\right)
\alpha.
$$

Multiply both sides by $2/\alpha$:

$$
\frac{2FR}{\alpha}
=
MR^2+mr^2.
$$

Subtract $MR^2$:

$$
mr^2
=
\frac{2FR}{\alpha}
-
MR^2.
$$

Divide by $r^2$:

$$
\boxed{
m
=
\frac{
\frac{2FR}{\alpha}-MR^2
}{
r^2
}
}.
$$

An equivalent form is

$$
\boxed{
m
=
\frac{2FR}{\alpha r^2}
-
M\frac{R^2}{r^2}
}.
$$

Using the numerical values supplied in the activity gives

$$
\boxed{
m=2.5\ \mathrm{kg}
}.
$$

## Explicit Unit Check

The first term in the result is

$$
\frac{2FR}{\alpha r^2}.
$$

Ignoring the dimensionless factor of $2$, its units are

$$
\left[
\frac{FR}{\alpha r^2}
\right]
=
\frac{
(\mathrm{N})(\mathrm{m})
}{
(\mathrm{s}^{-2})(\mathrm{m}^2)
}.
$$

Using

$$
1\ \mathrm{N}
=
1\ \mathrm{kg}\,\mathrm{m}/\mathrm{s}^2,
$$

we obtain

$$
\left[
\frac{FR}{\alpha r^2}
\right]
=
\frac{
(\mathrm{kg}\,\mathrm{m}/\mathrm{s}^2)(\mathrm{m})
}{
(\mathrm{s}^{-2})(\mathrm{m}^2)
}.
$$

The factors of $\mathrm{m}^2/\mathrm{s}^2$ cancel:

$$
\left[
\frac{FR}{\alpha r^2}
\right]
=
\mathrm{kg}.
$$

The second term has units

$$
\left[
M\frac{R^2}{r^2}
\right]
=
(\mathrm{kg})
\frac{\mathrm{m}^2}{\mathrm{m}^2}
=
\mathrm{kg}.
$$

Both terms have units of mass, so the final expression is dimensionally consistent.

## General Strategy for Torque Problems

### 1. Select the System

Identify the particular object or collection of objects being analyzed.

Only forces acting directly on that system belong on its free-body diagram.

### 2. Choose the Pivot or Rotation Axis

Torque and moment of inertia must be calculated about the same point or axis.

A strategic pivot choice can eliminate unknown forces from the torque equation.

### 3. Draw an Extended Free-Body Diagram

Show the object’s geometry, forces, points of application, distances, angles, and pivot.

Do not rely only on a point-particle free-body diagram when torque is involved.

### 4. Determine the Torque from Each Force

Use either

$$
\tau=rF\sin\theta
$$

or

$$
\tau=Fd.
$$

Assign signs according to a clearly stated rotational convention.

For example, you may define counterclockwise as positive and clockwise as negative.

### 5. Find the Correct Moment of Inertia

Use the moment of inertia about the selected axis.

For multiple rigidly connected objects,

$$
I_{\mathrm{total}}=\sum_i I_i.
$$

### 6. Apply Rotational Newton’s Second Law

Use

$$
\sum\tau=I\alpha.
$$

For static rotational equilibrium,

$$
\alpha=0
$$

and therefore

$$
\sum\tau=0.
$$

### 7. Solve Symbolically

Keep the calculation in variables until the requested quantity has been isolated.

A symbolic solution makes it easier to:

- Identify cancellations
- Check units
- Examine limiting behavior
- Find algebraic errors

### 8. Substitute Numerical Values

Insert numerical values only after obtaining the symbolic result.

## Summary

Torque is the rotational effect of a force:

$$
\boxed{
\vec{\tau}=\vec{r}\times\vec{F}
}.
$$

Its magnitude is

$$
\boxed{
\tau=rF\sin\theta
}.
$$

Only the component of force perpendicular to $\vec{r}$ produces torque:

$$
F_{\perp}=F\sin\theta.
$$

Using the moment arm $d$,

$$
\boxed{
\tau=Fd
}.
$$

The rotational form of Newton’s second law is

$$
\boxed{
\sum\vec{\tau}=I\vec{\alpha}
}.
$$

Torque is greatest when the force is perpendicular to the position vector:

$$
\theta=90^\circ.
$$

Torque is zero when the force acts through the pivot or along the radial direction.

For the wrench example,

$$
\boxed{
\tau\approx52\ \mathrm{N}\,\mathrm{m}
}
$$

and the torque points into the page.

For a solid cylindrical spool pulled tangentially by a tension $F_T$,

$$
F_T r=I\alpha
$$

with

$$
I=\frac{1}{2}mr^2.
$$

Therefore,

$$
\boxed{
\alpha=\frac{2F_T}{mr}
}.
$$

For two rigidly attached coaxial solid cylinders,

$$
I_{\mathrm{total}}
=
\frac{1}{2}MR^2
+
\frac{1}{2}mr^2.
$$

If a tangential force $F$ is applied at the outer radius $R$, then

$$
FR
=
\left(
\frac{1}{2}MR^2
+
\frac{1}{2}mr^2
\right)
\alpha.
$$

Solving for the smaller cylinder’s mass gives

$$
\boxed{
m
=
\frac{
\frac{2FR}{\alpha}-MR^2
}{
r^2
}
}.
$$

The most important step in a torque problem is constructing a correct extended free-body diagram. Once the forces, points of application, lever arms, angles, and pivot are clearly identified, the rotational equation follows systematically.

---

Up Next: [Static Equilibrium and Rotational Dynamics](../../2026-07-13-M2-4/Source/Lecture-Transcript.md)
Previous: [Center of Mass and Moment of Inertia](../../2026-07-08-M2-2/Source/Lecture-Transcript.md)

---
