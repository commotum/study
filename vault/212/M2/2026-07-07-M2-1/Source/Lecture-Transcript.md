# Physics 212: Center of Mass, Torque Balance, and Mass Density

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 1 is complete, and grading is now underway. Quiz scores are generally returned within one week.

Make sure that you submitted your handwritten Quiz 1 note sheet to Gradescope with your photo ID visible. You will not receive credit for the quiz until the note sheet and photo ID have been submitted.

Although the listed due date for the note sheet corresponds to the time when the quiz opened, the note sheet will not be marked late as long as it was submitted before you began the quiz.

Today, we are beginning the material for Quiz 2, which focuses on rigid-body rotational motion. This is a good time to begin preparing your Quiz 2 note sheet.

The Quiz 2 note sheet must:

- Be between one-half page and one full page
- Be entirely handwritten
- Contain no photocopied or printed material
- Be submitted with your photo ID visible

You will be allowed to use your Quiz 1 note sheet while taking Quiz 2, so you do not need to copy all of the Quiz 1 material onto the new sheet. The Quiz 2 note sheet should focus on the new rotational-motion material.

Once the Quiz 1 scores are posted, the optional Quiz 1X extra-credit assignment will open. For this assignment, you will select the Quiz 1 problem on which you lost the most points. You will then:

1. Explain the reasoning that led to your original answer.
2. Explain what you should have done differently and identify the relevant physics concepts.
3. Provide a complete corrected solution.
4. Discuss the problem with an instructor or teaching assistant.

The purpose of the assignment is to analyze the physics reasoning behind your original work. The emphasis should be on why you made particular decisions, rather than on external factors such as time pressure.

Parts A through C are worth up to eight points, capped by the number of points you lost on the selected problem. Part D is worth four additional points, so the assignment can restore up to twelve points.

# Introduction to the Center of Mass

Consider a teeter-totter with a small person sitting on one side and a much larger person sitting on the other.

To balance the system, the larger person must sit closer to the fulcrum. The smaller person can sit farther away.

This illustrates an important point: a balanced system does not necessarily have equal amounts of mass on both sides of the pivot. Instead, the torques on the two sides must balance.

Torque is defined by

$$
\boxed{
\vec{\tau}=\vec{r}\times\vec{F}
}
$$

where:

- $\vec{r}$ is the position vector from the pivot to the point where the force is applied
- $\vec{F}$ is the applied force
- $\vec{\tau}$ is the resulting torque

The magnitude of the torque is

$$
\boxed{
\tau=rF\sin\theta
}
$$

where $\theta$ is the angle between $\vec{r}$ and $\vec{F}$.

For a horizontal teeter-totter, the gravitational forces are perpendicular to the position vectors. Therefore,

$$
\sin\theta=\sin 90^\circ=1,
$$

and the torque magnitude produced by a mass $m$ at distance $r$ is

$$
\tau=rmg.
$$

If two masses balance on opposite sides of the fulcrum, their torques have equal magnitudes and opposite directions:

$$
m_1gr_1=m_2gr_2.
$$

The gravitational acceleration cancels:

$$
\boxed{
m_1r_1=m_2r_2
}.
$$

A larger mass must therefore be placed at a smaller distance from the pivot.

## Physical Meaning of the Center of Mass

The **center of mass** is a mass-weighted average position.

It is not necessarily a point with equal mass on either side.

In a uniform gravitational field, an object supported directly beneath its center of mass experiences no net gravitational torque about the support point. It can therefore balance at that location.

The center of mass is also important for freely moving objects. If an extended rigid object is thrown through the air and experiences negligible external torque, the object’s translational motion can be described by the motion of its center of mass, while the object rotates about its center of mass.

For example, a hammer thrown through the air may flip end over end, but its center of mass follows the ordinary projectile trajectory.

# Mathematical Definition of Center of Mass

For a collection of discrete particles, the center-of-mass position is

$$
\boxed{
\vec{r}_{\mathrm{cm}}
=
\frac{
\sum_i m_i\vec{r}_i
}{
\sum_i m_i
}
}.
$$

In one dimension,

$$
\boxed{
x_{\mathrm{cm}}
=
\frac{
\sum_i m_ix_i
}{
\sum_i m_i
}
}.
$$

For two masses, this becomes

$$
x_{\mathrm{cm}}
=
\frac{
m_1x_1+m_2x_2
}{
m_1+m_2
}.
$$

For a continuous mass distribution, the summation becomes an integral:

$$
\boxed{
\vec{r}_{\mathrm{cm}}
=
\frac{1}{M}
\int_{\text{object}}
\vec{r}\,dm
}
$$

or, in one dimension,

$$
\boxed{
x_{\mathrm{cm}}
=
\frac{1}{M}
\int_{\text{object}}
x\,dm
}.
$$

If the integral is written in terms of accumulated mass, the limits may be expressed as

$$
x_{\mathrm{cm}}
=
\frac{1}{M}
\int_0^M x\,dm.
$$

The center of mass is a position, so it has units of length, such as meters or centimeters.

The position must always be measured relative to a chosen coordinate origin.

# Worked Example 1: Two Point Masses

Consider two point masses separated by a distance $L$.

Let

$$
m_1=3m_2.
$$

Choose the position of $m_1$ as the origin:

$$
x_1=0.
$$

The second mass is located at

$$
x_2=L.
$$

The center of mass is

$$
x_{\mathrm{cm}}
=
\frac{
m_1x_1+m_2x_2
}{
m_1+m_2
}.
$$

Substituting the positions,

$$
x_{\mathrm{cm}}
=
\frac{
m_1(0)+m_2L
}{
m_1+m_2
}.
$$

Using $m_1=3m_2$,

$$
x_{\mathrm{cm}}
=
\frac{
m_2L
}{
3m_2+m_2
}.
$$

Therefore,

$$
x_{\mathrm{cm}}
=
\frac{
m_2L
}{
4m_2
}.
$$

The mass cancels:

$$
\boxed{
x_{\mathrm{cm}}=\frac{L}{4}
}.
$$

For

$$
L=0.88\ \mathrm{m},
$$

the center of mass is

$$
x_{\mathrm{cm}}
=
\frac{0.88\ \mathrm{m}}{4}.
$$

Thus,

$$
\boxed{
x_{\mathrm{cm}}=0.22\ \mathrm{m}
}.
$$

The center of mass lies closer to $m_1$, as expected, because $m_1$ is the larger mass.

## Solving the Same Problem with Torque

We can obtain the same result by requiring the torques about the center of mass to balance.

Let $x$ be the distance from $m_1$ to the center of mass. The distance from $m_2$ to the center of mass is then

$$
L-x.
$$

The torque magnitudes are

$$
\tau_1=m_1gx
$$

and

$$
\tau_2=m_2g(L-x).
$$

At equilibrium,

$$
m_1gx=m_2g(L-x).
$$

Canceling $g$ gives

$$
m_1x=m_2(L-x).
$$

Expanding the right side,

$$
m_1x=m_2L-m_2x.
$$

Collecting the terms containing $x$,

$$
(m_1+m_2)x=m_2L.
$$

Therefore,

$$
x
=
\frac{
m_2L
}{
m_1+m_2
}.
$$

Using $m_1=3m_2$ again gives

$$
\boxed{
x=\frac{L}{4}
}.
$$

This is identical to the result obtained from the center-of-mass equation.

# Torque as a Rotational Effect

A force tends to produce translational acceleration. Torque describes the tendency of a force to produce rotation about a chosen point or axis.

Both the force and its point of application matter.

Applying the same force farther from a hinge generally produces a greater torque. Applying a force directly through the hinge produces no torque about that hinge because the lever arm is zero.

For the two-mass system:

- The weight of $m_1$ tends to rotate the system in one direction.
- The weight of $m_2$ tends to rotate the system in the opposite direction.
- If the torques are equal in magnitude, the net torque is zero.

The rotational-equilibrium condition is

$$
\boxed{
\sum\vec{\tau}=0
}.
$$

# Worked Example 2: Arrangement of Identical Blocks

Consider a system containing ten identical blocks. Each block has uniform density and mass $m$.

Rather than treating every block separately, we can group the blocks into three subassemblies:

- Six blocks whose combined center of mass is at $x=1.5\ \mathrm{cm}$
- Two blocks whose combined center of mass is at $x=4.0\ \mathrm{cm}$
- Two blocks whose combined center of mass is at $x=5.5\ \mathrm{cm}$

Each group can be replaced by a point mass located at that group’s own center of mass.

The total center of mass is

$$
x_{\mathrm{cm}}
=
\frac{
(6m)(1.5\ \mathrm{cm})
+
(2m)(4.0\ \mathrm{cm})
+
(2m)(5.5\ \mathrm{cm})
}{
6m+2m+2m
}.
$$

The total mass is

$$
6m+2m+2m=10m.
$$

The numerator is

$$
9m\ \mathrm{cm}
+
8m\ \mathrm{cm}
+
11m\ \mathrm{cm}
=
28m\ \mathrm{cm}.
$$

Therefore,

$$
x_{\mathrm{cm}}
=
\frac{
28m\ \mathrm{cm}
}{
10m
}.
$$

The block mass cancels:

$$
\boxed{
x_{\mathrm{cm}}=2.8\ \mathrm{cm}
}.
$$

The result lies to the left of the geometric center of the full arrangement because more of the system’s mass is concentrated toward the left.

This example demonstrates that a complicated system can often be simplified by replacing each uniform subassembly with a point mass located at its own center of mass.

# Worked Example 3: Two Attached Cubes

Consider two solid cubes made from material with uniform volume mass density $\rho$.

The larger cube has side length $2L$, and the smaller cube has side length $L$. The smaller cube is attached to the right side of the larger cube.

Choose the origin at the left face of the larger cube.

We want to determine the center of mass of the combined object.

## Predicting the Result

The center of the larger cube is at

$$
x=L.
$$

The smaller cube lies to the right of the larger cube, so the combined center of mass must lie to the right of $x=L$.

However, the larger cube contains substantially more mass, so the center of mass should remain closer to the larger cube than to the center of the smaller cube.

We therefore expect

$$
L<x_{\mathrm{cm}}<2L.
$$

## Positions of the Individual Centers of Mass

The larger cube extends from $x=0$ to $x=2L$, so its center is

$$
\boxed{
x_1=L
}.
$$

The smaller cube begins at $x=2L$ and extends another distance $L$. Its center is therefore

$$
x_2
=
2L+\frac{L}{2}.
$$

Thus,

$$
\boxed{
x_2=\frac{5L}{2}
}.
$$

## Masses of the Cubes

Volume mass density is defined by

$$
\rho=\frac{m}{V}.
$$

Therefore,

$$
m=\rho V.
$$

The volume of the larger cube is

$$
V_1=(2L)^3=8L^3.
$$

Its mass is

$$
\boxed{
m_1=8\rho L^3
}.
$$

The volume of the smaller cube is

$$
V_2=L^3.
$$

Its mass is

$$
\boxed{
m_2=\rho L^3
}.
$$

The larger cube therefore has eight times the mass of the smaller cube.

## Center-of-Mass Calculation

The combined center of mass is

$$
x_{\mathrm{cm}}
=
\frac{
m_1x_1+m_2x_2
}{
m_1+m_2
}.
$$

Substituting the masses and positions,

$$
x_{\mathrm{cm}}
=
\frac{
(8\rho L^3)(L)
+
(\rho L^3)\left(\frac{5L}{2}\right)
}{
8\rho L^3+\rho L^3
}.
$$

Simplifying the numerator,

$$
x_{\mathrm{cm}}
=
\frac{
8\rho L^4
+
\frac{5}{2}\rho L^4
}{
9\rho L^3
}.
$$

Factor out $\rho L^3$:

$$
x_{\mathrm{cm}}
=
\frac{
\rho L^3
\left(
8L+\frac{5L}{2}
\right)
}{
9\rho L^3
}.
$$

The common factors cancel:

$$
x_{\mathrm{cm}}
=
\frac{
8L+\frac{5L}{2}
}{
9
}.
$$

Writing $8L$ as $16L/2$,

$$
x_{\mathrm{cm}}
=
\frac{
\frac{16L}{2}+\frac{5L}{2}
}{
9
}.
$$

Therefore,

$$
x_{\mathrm{cm}}
=
\frac{
21L/2
}{
9
}.
$$

Thus,

$$
\boxed{
x_{\mathrm{cm}}=\frac{7L}{6}
}.
$$

Using the numerical length supplied in the activity gives

$$
\boxed{
x_{\mathrm{cm}}=0.875\ \mathrm{m}
\approx0.88\ \mathrm{m}
}.
$$

The result satisfies the prediction

$$
L<x_{\mathrm{cm}}<2L.
$$

The common density $\rho$ cancels because both cubes are made from the same material. Their relative contributions are determined by their relative volumes.

# Continuous Mass Distributions

The previous examples involved separate objects whose masses could be added using a finite summation.

For an object whose mass varies continuously with position, we divide the object into infinitesimal mass elements $dm$ and use integration.

For a thin rod extending along the $x$-axis, the **linear mass density** is defined as

$$
\boxed{
\lambda(x)=\frac{dm}{dx}
}.
$$

The units of linear mass density are

$$
[\lambda]
=
\frac{\mathrm{kg}}{\mathrm{m}}.
$$

Solving for the mass element gives

$$
\boxed{
dm=\lambda(x)\,dx
}.
$$

This relationship allows us to convert an integral over mass into an integral over position.

For example,

$$
M=\int dm
$$

can be rewritten as

$$
M=\int\lambda(x)\,dx.
$$

Similarly, the center-of-mass equation

$$
x_{\mathrm{cm}}
=
\frac{1}{M}
\int x\,dm
$$

can be written as

$$
\boxed{
x_{\mathrm{cm}}
=
\frac{1}{M}
\int x\lambda(x)\,dx
}.
$$

The integration limits must describe the physical length of the object.

# Worked Example 4: Rod with Linearly Increasing Density

Consider a rod of total mass $M$ and length $L$ extending from

$$
x=0
$$

to

$$
x=L.
$$

Its linear mass density is

$$
\lambda(x)=Cx,
$$

where $C$ is an unknown constant.

Because $\lambda$ increases with $x$, the rod is least dense near $x=0$ and most dense near $x=L$.

A graph of $\lambda$ versus $x$ is a straight line with slope $C$.

We want to determine $C$ in terms of the rod’s total mass and length.

## Total Mass of the Rod

The total mass is

$$
M=\int_0^M dm.
$$

Using

$$
dm=\lambda(x)\,dx,
$$

we convert the integral from mass to position:

$$
M
=
\int_0^L\lambda(x)\,dx.
$$

Substituting

$$
\lambda(x)=Cx,
$$

gives

$$
M
=
\int_0^L Cx\,dx.
$$

Because $C$ is constant,

$$
M
=
C\int_0^L x\,dx.
$$

Evaluating the integral,

$$
M
=
C
\left[
\frac{x^2}{2}
\right]_0^L.
$$

Therefore,

$$
M
=
C
\left(
\frac{L^2}{2}-0
\right).
$$

Thus,

$$
M=\frac{CL^2}{2}.
$$

Solving for $C$,

$$
2M=CL^2,
$$

so

$$
\boxed{
C=\frac{2M}{L^2}
}.
$$

## Unit Check

Since

$$
\lambda(x)=Cx,
$$

the units of $C$ must satisfy

$$
[C][x]=[\lambda].
$$

Therefore,

$$
[C]
=
\frac{
[\lambda]
}{
[x]
}.
$$

Substituting the units,

$$
[C]
=
\frac{
\mathrm{kg/m}
}{
\mathrm{m}
}.
$$

Thus,

$$
\boxed{
[C]=\mathrm{kg/m^2}
}.
$$

Using the numerical mass and length supplied in the activity gives approximately

$$
\boxed{
C=0.40\ \mathrm{kg/m^2}
}.
$$

This value completely specifies how the rod’s mass density changes with position.

In the next lecture, this density function can be substituted into

$$
x_{\mathrm{cm}}
=
\frac{1}{M}
\int_0^L x\lambda(x)\,dx
$$

to determine the center of mass of the nonuniform rod.

# General Strategy for Center-of-Mass Problems

## 1. Choose a Coordinate Origin

Every center-of-mass position must be measured relative to a reference point.

Choose an origin that makes the individual positions simple.

## 2. Predict the Approximate Location

Before calculating, determine where the center of mass should lie physically.

The center of mass should be shifted toward the region containing more mass.

## 3. Identify Each Mass and Position

For discrete objects, list each mass $m_i$ and the coordinate $x_i$ of its own center of mass.

Then use

$$
x_{\mathrm{cm}}
=
\frac{
\sum_i m_ix_i
}{
\sum_i m_i
}.
$$

## 4. Group Convenient Subsystems

A uniform group of objects may be replaced by a point mass located at that group’s center of mass.

This can simplify a large summation substantially.

## 5. Convert Density into Mass

For a continuous one-dimensional object,

$$
dm=\lambda(x)\,dx.
$$

For a volume with uniform density,

$$
m=\rho V.
$$

## 6. Integrate Over the Physical Object

For a continuous distribution,

$$
x_{\mathrm{cm}}
=
\frac{1}{M}
\int x\,dm.
$$

After substituting for $dm$, use limits corresponding to the object’s actual dimensions.

## 7. Check Units and Physical Reasonableness

The center of mass must have units of length.

The calculated position should also lie in a physically reasonable location relative to the mass distribution.

# Summary

The center of mass is a mass-weighted average position.

For a system of discrete particles,

$$
\boxed{
\vec{r}_{\mathrm{cm}}
=
\frac{
\sum_i m_i\vec{r}_i
}{
\sum_i m_i
}
}.
$$

In one dimension,

$$
\boxed{
x_{\mathrm{cm}}
=
\frac{
\sum_i m_ix_i
}{
\sum_i m_i
}
}.
$$

For a continuous object,

$$
\boxed{
x_{\mathrm{cm}}
=
\frac{1}{M}
\int x\,dm
}.
$$

Torque is

$$
\boxed{
\vec{\tau}=\vec{r}\times\vec{F}
}
$$

with magnitude

$$
\boxed{
\tau=rF\sin\theta
}.
$$

For rotational equilibrium,

$$
\boxed{
\sum\vec{\tau}=0
}.
$$

For two masses on opposite sides of a fulcrum,

$$
\boxed{
m_1r_1=m_2r_2
}.
$$

For two point masses separated by $L$, with $m_1=3m_2$ and the origin at $m_1$,

$$
\boxed{
x_{\mathrm{cm}}=\frac{L}{4}
}.
$$

For the ten-block arrangement considered in the lecture,

$$
\boxed{
x_{\mathrm{cm}}=2.8\ \mathrm{cm}
}.
$$

For a cube of side $2L$ attached to a cube of side $L$, with both cubes having the same density,

$$
\boxed{
x_{\mathrm{cm}}=\frac{7L}{6}
}.
$$

Linear mass density is

$$
\boxed{
\lambda(x)=\frac{dm}{dx}
}
$$

and therefore

$$
\boxed{
dm=\lambda(x)\,dx
}.
$$

For a rod whose density varies according to

$$
\lambda(x)=Cx,
$$

the total mass is

$$
M=\frac{CL^2}{2},
$$

so

$$
\boxed{
C=\frac{2M}{L^2}
}.
$$

These ideas provide the foundation for calculating the center of mass and moment of inertia of continuous and composite objects.

---

Up Next: [Center of Mass and Moment of Inertia](../../2026-07-08-M2-2/Source/Lecture-Transcript.md)
Previous: [Nonuniform Circular Motion and Tangential Projectile Motion](../../../M1/2026-07-02-M1-5/Source/Lecture-Transcript.md)

---
