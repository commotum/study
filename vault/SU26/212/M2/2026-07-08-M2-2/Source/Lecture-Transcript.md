# Physics 212: Center of Mass and Moment of Inertia

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 1 is currently being graded. The grading will be completed within one week of the quiz due date, and the optional Quiz 1X assignment will open when those scores are posted.

## Review: Center of Mass

In the previous lecture, we introduced the center of mass.

The name **center of mass** can be slightly misleading. It is not necessarily a point with equal amounts of mass on either side. Instead, it is a mass-weighted average position.

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

In one dimension, this becomes

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

For a continuous object, the summation becomes an integral:

$$
\boxed{
\vec{r}_{\mathrm{cm}}
=
\frac{1}{M}
\int \vec{r}\,dm
}
$$

or, in one dimension,

$$
\boxed{
x_{\mathrm{cm}}
=
\frac{1}{M}
\int x\,dm
}.
$$

Here, $M$ is the total mass of the object.

The center of mass must be measured relative to a chosen coordinate origin. Changing the origin changes the coordinate assigned to the center of mass, although it does not change the physical location of the center of mass within the object.

If a freely moving rigid object rotates, its motion can be separated into:

- Translational motion of its center of mass
- Rotational motion about its center of mass

In a uniform gravitational field, an object can also balance on a narrow support placed directly beneath its center of mass. This does not require equal masses on the two sides of the support. Instead, it requires the gravitational torques on the two sides to balance.

Torque is defined by

$$
\vec{\tau}
=
\vec{r}\times\vec{F},
$$

so the placement of the mass relative to the support is just as important as the amount of mass.

## Linear Mass Density

For a thin rod whose mass is distributed continuously along the $x$-axis, we define the linear mass density as

$$
\boxed{
\lambda(x)=\frac{dm}{dx}
}.
$$

Therefore,

$$
\boxed{
dm=\lambda(x)\,dx
}.
$$

This substitution allows us to convert integrals over mass into integrals over position.

For a uniform rod,

$$
\lambda=\frac{M}{L},
$$

where $M$ is the rod’s total mass and $L$ is its length.

For a nonuniform rod, $\lambda$ may depend on position.

# Nonuniform Rod with Linearly Increasing Density

Consider a rod extending from

$$
x=0
$$

to

$$
x=L.
$$

Its linear mass density increases linearly with position:

$$
\lambda(x)=Cx,
$$

where $C$ is a constant.

The rod is least dense near $x=0$ and most dense near $x=L$.

## Determining the Constant $C$

The total mass is

$$
M=\int dm.
$$

Using

$$
dm=\lambda(x)\,dx,
$$

we obtain

$$
M
=
\int_0^L \lambda(x)\,dx.
$$

Substituting $\lambda(x)=Cx$ gives

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
\frac{CL^2}{2}.
$$

Solving for $C$ gives

$$
\boxed{
C=\frac{2M}{L^2}
}.
$$

The units of $C$ are mass per length squared because multiplying $C$ by $x$ must produce a linear mass density:

$$
[C]
=
\frac{\mathrm{kg}}{\mathrm{m}^2}.
$$

## Center of Mass of the Nonuniform Rod

The center of mass is

$$
x_{\mathrm{cm}}
=
\frac{1}{M}
\int x\,dm.
$$

Using

$$
dm=\lambda(x)\,dx,
$$

we obtain

$$
x_{\mathrm{cm}}
=
\frac{1}{M}
\int_0^L x\lambda(x)\,dx.
$$

Substituting $\lambda(x)=Cx$,

$$
x_{\mathrm{cm}}
=
\frac{1}{M}
\int_0^L x(Cx)\,dx.
$$

Therefore,

$$
x_{\mathrm{cm}}
=
\frac{C}{M}
\int_0^L x^2\,dx.
$$

Evaluating the integral,

$$
x_{\mathrm{cm}}
=
\frac{C}{M}
\left[
\frac{x^3}{3}
\right]_0^L.
$$

Thus,

$$
x_{\mathrm{cm}}
=
\frac{CL^3}{3M}.
$$

Using

$$
C=\frac{2M}{L^2},
$$

we obtain

$$
x_{\mathrm{cm}}
=
\frac{1}{3M}
\left(
\frac{2M}{L^2}
\right)
L^3.
$$

The mass cancels, and one factor of $L$ remains:

$$
\boxed{
x_{\mathrm{cm}}=\frac{2L}{3}
}.
$$

For a rod of length

$$
L=1.8\ \mathrm{m},
$$

the center of mass is

$$
x_{\mathrm{cm}}
=
\frac{2}{3}
(1.8\ \mathrm{m}).
$$

Therefore,

$$
\boxed{
x_{\mathrm{cm}}=1.2\ \mathrm{m}
}.
$$

This result is physically reasonable. Because the rod becomes denser toward the right, the center of mass should lie to the right of the geometric midpoint:

$$
\frac{L}{2}
<
x_{\mathrm{cm}}
<
L.
$$

The result

$$
x_{\mathrm{cm}}=\frac{2L}{3}
$$

satisfies this condition.

This example also illustrates why calculations should be completed symbolically before numerical values are substituted. The symbolic expression reveals how the answer depends on the given variables and makes physical and dimensional checks much easier.

# Rotational Kinetic Energy

We now introduce another important property of an extended object: its **moment of inertia**.

Consider a rigid body rotating about a fixed axis with angular velocity $\omega$. We can imagine dividing the object into many small particles.

For three representative particles, the rotational kinetic energy would be

$$
K_{\mathrm{rot}}
=
\frac{1}{2}m_1v_1^2
+
\frac{1}{2}m_2v_2^2
+
\frac{1}{2}m_3v_3^2
+\cdots.
$$

For rigid rotation, every part of the object has the same angular velocity $\omega$. The linear speed of particle $i$ is

$$
v_i=\omega r_{\perp,i},
$$

where $r_{\perp,i}$ is the perpendicular distance from the rotation axis to the particle.

Substituting into the kinetic-energy expression gives

$$
K_{\mathrm{rot}}
=
\frac{1}{2}m_1r_{\perp,1}^2\omega^2
+
\frac{1}{2}m_2r_{\perp,2}^2\omega^2
+\cdots.
$$

The common factors may be collected:

$$
K_{\mathrm{rot}}
=
\frac{1}{2}
\left(
\sum_i m_ir_{\perp,i}^2
\right)
\omega^2.
$$

We define the quantity in parentheses as the moment of inertia:

$$
\boxed{
I=\sum_i m_ir_{\perp,i}^2
}.
$$

The rotational kinetic energy is therefore

$$
\boxed{
K_{\mathrm{rot}}
=
\frac{1}{2}I\omega^2
}.
$$

For a continuous object, the moment of inertia is

$$
\boxed{
I=\int r_\perp^2\,dm
}.
$$

The moment of inertia is the rotational analogue of mass. It measures an object’s resistance to angular acceleration about a specified axis.

However, unlike mass, the moment of inertia depends on the choice of axis. Moving the rotation axis changes the distances $r_\perp$ and therefore changes $I$.

The SI units of moment of inertia are

$$
\boxed{
[I]=\mathrm{kg}\,\mathrm{m}^2
}.
$$

The distance appears squared, so mass located far from the axis contributes much more strongly than the same amount of mass located close to the axis.

For a rigid object that is both translating and rotating, the kinetic energy can be separated into

$$
K
=
\frac{1}{2}Mv_{\mathrm{cm}}^2
+
\frac{1}{2}I_{\mathrm{cm}}\omega^2.
$$

The first term describes translation of the center of mass, while the second describes rotation about the center of mass.

# Moment of Inertia of a Uniform Thin Rod

Consider a uniform thin rod with mass $M$ and length $L$.

Its constant linear mass density is

$$
\lambda=\frac{M}{L}.
$$

Therefore,

$$
dm=\frac{M}{L}\,dx.
$$

## Rotation About the Rod’s Center

Place the origin at the rod’s center. The rod extends from

$$
x=-\frac{L}{2}
$$

to

$$
x=+\frac{L}{2}.
$$

The moment of inertia is

$$
I_{\mathrm{cm}}
=
\int x^2\,dm.
$$

Substituting for $dm$,

$$
I_{\mathrm{cm}}
=
\frac{M}{L}
\int_{-L/2}^{L/2}x^2\,dx.
$$

Evaluating the integral,

$$
I_{\mathrm{cm}}
=
\frac{M}{L}
\left[
\frac{x^3}{3}
\right]_{-L/2}^{L/2}.
$$

Therefore,

$$
I_{\mathrm{cm}}
=
\frac{M}{3L}
\left[
\left(
\frac{L}{2}
\right)^3
-
\left(
-\frac{L}{2}
\right)^3
\right].
$$

Because the second term is negative,

$$
I_{\mathrm{cm}}
=
\frac{M}{3L}
\left(
\frac{L^3}{8}
+
\frac{L^3}{8}
\right).
$$

Thus,

$$
I_{\mathrm{cm}}
=
\frac{M}{3L}
\left(
\frac{L^3}{4}
\right).
$$

Simplifying,

$$
\boxed{
I_{\mathrm{cm}}
=
\frac{1}{12}ML^2
}.
$$

## Rotation About One End

Now place the rotation axis at the left end of the rod. The rod extends from

$$
x=0
$$

to

$$
x=L.
$$

The moment of inertia is

$$
I_{\mathrm{end}}
=
\frac{M}{L}
\int_0^L x^2\,dx.
$$

Evaluating the integral,

$$
I_{\mathrm{end}}
=
\frac{M}{L}
\left[
\frac{x^3}{3}
\right]_0^L.
$$

Therefore,

$$
I_{\mathrm{end}}
=
\frac{M}{L}
\frac{L^3}{3}.
$$

Thus,

$$
\boxed{
I_{\mathrm{end}}
=
\frac{1}{3}ML^2
}.
$$

The moment of inertia about the end is four times the moment of inertia about the center:

$$
I_{\mathrm{end}}
=
4I_{\mathrm{cm}}.
$$

This makes physical sense. When the rod rotates about its center, no part of the rod is more than $L/2$ from the axis. When it rotates about one end, some of its mass is as far as $L$ from the axis.

Because moment of inertia weights each mass element by the square of its distance from the axis, shifting the axis toward one end substantially increases the moment of inertia.

# The Parallel-Axis Theorem

The parallel-axis theorem provides a convenient way to calculate the moment of inertia about an axis that does not pass through the center of mass.

The theorem states that

$$
\boxed{
I_p
=
I_{\mathrm{cm}}
+
Md^2
},
$$

where:

- $I_p$ is the moment of inertia about the desired axis
- $I_{\mathrm{cm}}$ is the moment of inertia about a parallel axis through the center of mass
- $M$ is the total mass of the object
- $d$ is the perpendicular distance between the two axes

This is a general formula. The value of $I_{\mathrm{cm}}$ depends on the particular object, but the relationship itself applies to any rigid body when the two axes are parallel.

## Applying the Theorem to a Uniform Rod

For a uniform rod,

$$
I_{\mathrm{cm}}
=
\frac{1}{12}ML^2.
$$

The distance from the rod’s center to one end is

$$
d=\frac{L}{2}.
$$

Therefore,

$$
I_{\mathrm{end}}
=
I_{\mathrm{cm}}
+
Md^2.
$$

Substituting,

$$
I_{\mathrm{end}}
=
\frac{1}{12}ML^2
+
M
\left(
\frac{L}{2}
\right)^2.
$$

Thus,

$$
I_{\mathrm{end}}
=
\frac{1}{12}ML^2
+
\frac{1}{4}ML^2.
$$

Using a common denominator,

$$
I_{\mathrm{end}}
=
\frac{1}{12}ML^2
+
\frac{3}{12}ML^2.
$$

Therefore,

$$
\boxed{
I_{\mathrm{end}}
=
\frac{1}{3}ML^2
}.
$$

This agrees with the result obtained by direct integration.

The parallel-axis theorem is often much faster than performing a new integral whenever the moment of inertia about the center of mass is already known.

# Moment of Inertia of the Nonuniform Rod

Return to the nonuniform rod described by

$$
\lambda(x)=Cx,
$$

with

$$
C=\frac{2M}{L^2}.
$$

The rod extends from $x=0$ to $x=L$, and we want its moment of inertia about the axis at $x=0$.

The moment of inertia is

$$
I_0
=
\int x^2\,dm.
$$

Using

$$
dm=\lambda(x)\,dx,
$$

we obtain

$$
I_0
=
\int_0^L x^2\lambda(x)\,dx.
$$

Substituting $\lambda(x)=Cx$,

$$
I_0
=
\int_0^L x^2(Cx)\,dx.
$$

Therefore,

$$
I_0
=
C\int_0^L x^3\,dx.
$$

Evaluating the integral,

$$
I_0
=
C
\left[
\frac{x^4}{4}
\right]_0^L.
$$

Thus,

$$
I_0
=
\frac{CL^4}{4}.
$$

Substituting

$$
C=\frac{2M}{L^2},
$$

we obtain

$$
I_0
=
\frac{1}{4}
\left(
\frac{2M}{L^2}
\right)
L^4.
$$

Simplifying,

$$
\boxed{
I_0
=
\frac{1}{2}ML^2
}.
$$

For

$$
M=0.65\ \mathrm{kg}
$$

and

$$
L=1.8\ \mathrm{m},
$$

the moment of inertia is

$$
I_0
=
\frac{1}{2}
(0.65\ \mathrm{kg})
(1.8\ \mathrm{m})^2.
$$

Therefore,

$$
I_0
\approx
1.1\ \mathrm{kg}\,\mathrm{m}^2.
$$

Thus,

$$
\boxed{
I_0\approx1.1\ \mathrm{kg}\,\mathrm{m}^2
}.
$$

This value is larger than the moment of inertia of a uniform rod of the same mass and length about one end:

$$
I_{\mathrm{uniform,end}}
=
\frac{1}{3}ML^2.
$$

That is physically reasonable because the nonuniform rod contains a greater fraction of its mass near the far end, where the distance from the axis is greatest.

# Uniform Rod Pivoted One-Third of the Way from One End

Consider a uniform thin rod with mass $M$ and length $L$. The rotation axis is located a distance

$$
\frac{L}{3}
$$

from the left end.

We want the moment of inertia about this axis.

## Method 1: Direct Integration

Choose a coordinate $u$ measured from the pivot.

The left end is located at

$$
u=-\frac{L}{3},
$$

and the right end is located at

$$
u=\frac{2L}{3}.
$$

Because the rod is uniform,

$$
dm=\frac{M}{L}\,du.
$$

The moment of inertia is

$$
I_p
=
\int u^2\,dm.
$$

Therefore,

$$
I_p
=
\frac{M}{L}
\int_{-L/3}^{2L/3}u^2\,du.
$$

Evaluating the integral,

$$
I_p
=
\frac{M}{L}
\left[
\frac{u^3}{3}
\right]_{-L/3}^{2L/3}.
$$

Thus,

$$
I_p
=
\frac{M}{3L}
\left[
\left(
\frac{2L}{3}
\right)^3
-
\left(
-\frac{L}{3}
\right)^3
\right].
$$

Simplifying the terms inside the brackets,

$$
I_p
=
\frac{M}{3L}
\left(
\frac{8L^3}{27}
+
\frac{L^3}{27}
\right).
$$

Therefore,

$$
I_p
=
\frac{M}{3L}
\left(
\frac{9L^3}{27}
\right).
$$

Since

$$
\frac{9}{27}=\frac{1}{3},
$$

we obtain

$$
I_p
=
\frac{M}{3L}
\frac{L^3}{3}.
$$

Thus,

$$
\boxed{
I_p=\frac{1}{9}ML^2
}.
$$

Numerically, the coefficient is

$$
\frac{1}{9}\approx0.11.
$$

## Method 2: Parallel-Axis Theorem

The center of mass of a uniform rod is located at

$$
x_{\mathrm{cm}}=\frac{L}{2}.
$$

The pivot is located at

$$
x_p=\frac{L}{3}.
$$

The distance between the pivot and the center of mass is therefore

$$
d
=
\frac{L}{2}
-
\frac{L}{3}.
$$

Using a common denominator,

$$
d
=
\frac{3L}{6}
-
\frac{2L}{6}.
$$

Thus,

$$
d=\frac{L}{6}.
$$

The moment of inertia about the center is

$$
I_{\mathrm{cm}}
=
\frac{1}{12}ML^2.
$$

Using the parallel-axis theorem,

$$
I_p
=
I_{\mathrm{cm}}
+
Md^2.
$$

Therefore,

$$
I_p
=
\frac{1}{12}ML^2
+
M
\left(
\frac{L}{6}
\right)^2.
$$

This becomes

$$
I_p
=
\frac{1}{12}ML^2
+
\frac{1}{36}ML^2.
$$

Using a common denominator,

$$
I_p
=
\frac{3}{36}ML^2
+
\frac{1}{36}ML^2.
$$

Thus,

$$
\boxed{
I_p
=
\frac{4}{36}ML^2
=
\frac{1}{9}ML^2
}.
$$

Both methods produce the same result.

Because this pivot lies only $L/6$ from the center of mass, the moment of inertia is only slightly larger than the center-of-mass value:

$$
\frac{1}{12}ML^2
<
\frac{1}{9}ML^2.
$$

It is also much smaller than the moment of inertia about the end:

$$
\frac{1}{9}ML^2
<
\frac{1}{3}ML^2.
$$

# Composite Object: Rod with a Point Mass

Consider a uniform thin rod with:

- Mass $M$
- Length $L$
- A pivot at its left end
- A point mass $3M$ attached to its right end

The total moment of inertia is the sum of the moments of inertia of the individual components, calculated about the same axis:

$$
I_{\mathrm{total}}
=
I_{\mathrm{rod}}
+
I_{\mathrm{point}}.
$$

The rod’s moment of inertia about one end is

$$
I_{\mathrm{rod}}
=
\frac{1}{3}ML^2.
$$

The point mass is a distance $L$ from the pivot, so

$$
I_{\mathrm{point}}
=
(3M)L^2.
$$

Therefore,

$$
I_{\mathrm{total}}
=
\frac{1}{3}ML^2
+
3ML^2.
$$

Writing the second term with a denominator of $3$,

$$
I_{\mathrm{total}}
=
\frac{1}{3}ML^2
+
\frac{9}{3}ML^2.
$$

Thus,

$$
\boxed{
I_{\mathrm{total}}
=
\frac{10}{3}ML^2
}.
$$

The point mass makes the dominant contribution because it has three times the rod’s mass and is located at the maximum possible distance from the pivot.

If the attached object had a finite size rather than being a point mass, its own rotational inertia would also have to be included. In that case, the parallel-axis theorem would be used:

$$
I_{\mathrm{attached},p}
=
I_{\mathrm{attached,cm}}
+
m_{\mathrm{attached}}d^2.
$$

The total moment of inertia would then be

$$
I_{\mathrm{total}}
=
I_{\mathrm{rod},p}
+
I_{\mathrm{attached},p}.
$$

# General Procedure for Moment-of-Inertia Problems

## 1. Choose the Rotation Axis

Moment of inertia is always defined relative to a particular axis.

Clearly identify:

- The position of the axis
- The direction of the axis
- The perpendicular distance from each mass element to the axis

## 2. Decide Whether the Object Is Discrete or Continuous

For discrete point masses, use

$$
I=\sum_i m_ir_{\perp,i}^2.
$$

For a continuous object, use

$$
I=\int r_\perp^2\,dm.
$$

## 3. Express $dm$ in Terms of Geometry

For a thin rod,

$$
dm=\lambda(x)\,dx.
$$

For a uniform rod,

$$
\lambda=\frac{M}{L}.
$$

For a nonuniform rod, substitute the given function $\lambda(x)$.

## 4. Set the Correct Integration Limits

The limits must describe the object relative to the chosen rotation axis.

For example:

- A rod centered at the origin extends from $-L/2$ to $L/2$.
- A rod pivoted at one end extends from $0$ to $L$.
- A rod pivoted at $L/3$ from the left end extends from $-L/3$ to $2L/3$ when measured from the pivot.

## 5. Use the Parallel-Axis Theorem When Appropriate

If the moment of inertia about the center of mass is known and the desired axis is parallel to it, use

$$
I_p=I_{\mathrm{cm}}+Md^2.
$$

This is usually faster than performing another integral.

## 6. Add Moments of Inertia for Composite Objects

For several rigidly connected components rotating about the same axis,

$$
I_{\mathrm{total}}
=
\sum_i I_i.
$$

Each component’s moment of inertia must be calculated about the common rotation axis.

## 7. Solve Symbolically Before Substituting Numbers

A symbolic solution makes it easier to:

- Check dimensions
- Identify cancellations
- Compare limiting cases
- Analyze how the answer changes with mass or length
- Detect unreasonable numerical results

## 8. Check Units and Physical Reasonableness

Every moment of inertia must have units of

$$
\mathrm{kg}\,\mathrm{m}^2.
$$

The result should increase when mass is moved farther from the rotation axis.

For the same object and a family of parallel axes, the moment of inertia is smallest about the axis through the center of mass.

# Summary

The center of mass of a discrete system is

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

For a continuous object,

$$
\boxed{
\vec{r}_{\mathrm{cm}}
=
\frac{1}{M}
\int \vec{r}\,dm
}.
$$

For a rod with linear mass density

$$
\lambda(x)=Cx,
$$

the constant is

$$
\boxed{
C=\frac{2M}{L^2}
}.
$$

Its center of mass, measured from the low-density end, is

$$
\boxed{
x_{\mathrm{cm}}=\frac{2L}{3}
}.
$$

For $L=1.8\ \mathrm{m}$,

$$
\boxed{
x_{\mathrm{cm}}=1.2\ \mathrm{m}
}.
$$

Rotational kinetic energy is

$$
\boxed{
K_{\mathrm{rot}}
=
\frac{1}{2}I\omega^2
}.
$$

The moment of inertia is

$$
\boxed{
I=\sum_i m_ir_{\perp,i}^2
}
$$

for discrete masses and

$$
\boxed{
I=\int r_\perp^2\,dm
}
$$

for a continuous object.

For a uniform thin rod rotating about its center,

$$
\boxed{
I_{\mathrm{cm}}
=
\frac{1}{12}ML^2
}.
$$

For the same rod rotating about one end,

$$
\boxed{
I_{\mathrm{end}}
=
\frac{1}{3}ML^2
}.
$$

The parallel-axis theorem is

$$
\boxed{
I_p
=
I_{\mathrm{cm}}
+
Md^2
}.
$$

For the nonuniform rod with $\lambda(x)=Cx$, rotating about the low-density end,

$$
\boxed{
I_0
=
\frac{1}{2}ML^2
}.
$$

For a uniform rod pivoted one-third of its length from one end,

$$
\boxed{
I_p
=
\frac{1}{9}ML^2
}.
$$

For a uniform rod of mass $M$ with a point mass $3M$ attached to its far end, rotating about the opposite end,

$$
\boxed{
I_{\mathrm{total}}
=
\frac{10}{3}ML^2
}.
$$

Moment of inertia depends on both the amount of mass and its distribution relative to the rotation axis. Because each mass element is weighted by the square of its distance from the axis, moving mass outward can greatly increase the rotational inertia of a system.

---

Up Next: [Torque, Moment Arms, and Rotational Dynamics](../../2026-07-09-M2-3/Source/Lecture-Transcript.md)
Previous: [Center of Mass, Torque Balance, and Mass Density](../../2026-07-07-M2-1/Source/Lecture-Transcript.md)

---
