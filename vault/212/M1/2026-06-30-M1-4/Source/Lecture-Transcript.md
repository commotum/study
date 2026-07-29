# Physics 212: Circular Motion on Flat and Banked Curves

Welcome back to Physics 212.

## Announcements

Quiz 1 is approaching.

The Proctorio version will open at 5:00 p.m. Saturday and close at 5:00 p.m. Monday. Zoom-proctored versions will be offered Monday at 11:00 a.m. and 6:00 p.m. The different versions will contain different questions but will be designed to have the same level of difficulty.

Students taking a Zoom-proctored version must have a working webcam and remain visible throughout the quiz.

The Quiz 1 Notes assignment is also open. Your note sheet must:

- Be between one-half page and one full page
- Be written entirely in your own handwriting
- Contain material relevant to the quiz

The listed due date is 5:00 p.m. Saturday, when the quiz first opens. However, the note sheet will not be marked late as long as you submit it before beginning your quiz.

Today, we will continue studying circular motion in a plane, focusing on cars traveling around flat and banked curves.

# Review of Circular Motion

For an object moving in a circle of radius $r$ with speed $v$, the radial acceleration has magnitude

$$
\boxed{
a_r=\frac{v^2}{r}
}.
$$

The radial acceleration points toward the center of the circle.

Newton’s second law in the radial direction is therefore

$$
\boxed{
\sum F_r=m\frac{v^2}{r}
}.
$$

The expression

$$
m\frac{v^2}{r}
$$

is not an additional force. It is the required net inward force for circular motion. The actual physical forces acting on the object must combine to produce this net radial force.

# Car Traveling Around a Flat Curve

Consider a car traveling around a level circular curve.

Because the road is horizontal, the car has no vertical acceleration. However, it does have an inward radial acceleration because its velocity is continually changing direction.

## Free-Body Diagram

The forces acting on the car are:

- The gravitational force $mg$, directed downward
- The normal force $N$, directed upward
- Static friction $f_s$, directed horizontally toward the center of the curve

The static-friction force is what causes the car to follow the circular path.

Without friction, there would be no inward horizontal force. The car would continue approximately along a straight-line path tangent to the curve rather than following the road.

It is important that the friction force point toward the center of the circle. An outward friction force would cause acceleration in the wrong direction.

Because the car does not accelerate vertically,

$$
\sum F_y=0.
$$

Therefore,

$$
N-mg=0,
$$

so

$$
\boxed{
N=mg
}.
$$

The normal-force and gravitational-force vectors must therefore have equal magnitudes.

In the radial direction,

$$
\sum F_r=m\frac{v^2}{r}.
$$

The only radial force is friction, so

$$
\boxed{
f_s=m\frac{v^2}{r}
}.
$$

# Maximum Speed on a Flat Curve

Suppose the car is moving at the greatest speed possible without sliding.

At that threshold, static friction has reached its maximum value:

$$
f_{s,\max}=\mu_sN,
$$

where $\mu_s$ is the coefficient of static friction between the tires and the road.

Because

$$
N=mg,
$$

the maximum static-friction force is

$$
f_{s,\max}=\mu_smg.
$$

The radial equation is

$$
\mu_smg=m\frac{v^2}{r}.
$$

The mass cancels:

$$
\mu_sg=\frac{v^2}{r}.
$$

Solving for the coefficient of static friction gives

$$
\boxed{
\mu_s=\frac{v^2}{rg}
}.
$$

For the values

$$
v=16\ \mathrm{m/s}
$$

and

$$
r=49\ \mathrm{m},
$$

we obtain

$$
\mu_s
=
\frac{
(16\ \mathrm{m/s})^2
}{
(49\ \mathrm{m})(9.81\ \mathrm{m/s^2})
}.
$$

Therefore,

$$
\boxed{
\mu_s\approx0.53
}.
$$

The coefficient of friction is dimensionless.

The mass of the car does not affect the required coefficient. A more massive car requires a larger inward force, but it also experiences a proportionally larger maximum friction force.

## Why the Friction Is Static

The friction is static because the tire surfaces are not sliding sideways across the road.

If the car exceeds the maximum possible speed and begins to slide, kinetic friction becomes relevant. At the threshold just before sliding, however, the appropriate relationship is

$$
f_s=\mu_sN.
$$

# Car Traveling Around a Frictionless Banked Curve

Now consider a circular road banked at an angle $\theta$ above the horizontal.

Assume that the surface is icy and effectively frictionless.

On a flat road, friction supplies the radial force. On a frictionless banked road, the inward component of the normal force supplies the radial force.

## Choosing the Coordinate Axes

Choose:

- The positive $y$-axis vertically upward
- The positive radial axis horizontally inward toward the center of the curve

The radial axis must point toward the center of the circular path.

Axes aligned with the banked road are possible, but then the circular acceleration would have components along both axes. Using vertical and radial axes allows us to write

$$
a_r=\frac{v^2}{r}
$$

directly in the radial direction.

## Free-Body Diagram

The only forces acting on the car are:

- The gravitational force $mg$, vertically downward
- The normal force $N$, perpendicular to the road

Because the road is banked at angle $\theta$, the normal force is tilted inward by angle $\theta$ from the vertical.

Its components are therefore:

$$
N_y=N\cos\theta
$$

and

$$
N_r=N\sin\theta.
$$

## Vertical Equation

There is no vertical acceleration, so

$$
\sum F_y=0.
$$

Therefore,

$$
N\cos\theta-mg=0.
$$

Thus,

$$
\boxed{
N\cos\theta=mg
}
$$

and

$$
\boxed{
N=\frac{mg}{\cos\theta}
}.
$$

## Radial Equation

The inward component of the normal force supplies the radial acceleration:

$$
\sum F_r=m\frac{v^2}{r}.
$$

Therefore,

$$
N\sin\theta=m\frac{v^2}{r}.
$$

Substitute

$$
N=\frac{mg}{\cos\theta}:
$$

$$
\frac{mg}{\cos\theta}\sin\theta
=
m\frac{v^2}{r}.
$$

The mass cancels:

$$
g\frac{\sin\theta}{\cos\theta}
=
\frac{v^2}{r}.
$$

Because

$$
\frac{\sin\theta}{\cos\theta}=\tan\theta,
$$

we obtain

$$
g\tan\theta=\frac{v^2}{r}.
$$

Therefore,

$$
v^2=rg\tan\theta,
$$

and the speed for which no friction is required is

$$
\boxed{
v=\sqrt{rg\tan\theta}
}.
$$

This is sometimes called the **design speed** of the banked curve.

For

$$
r=48\ \mathrm{m}
$$

and

$$
\theta=6.2^\circ,
$$

the speed is

$$
v
=
\sqrt{
(48\ \mathrm{m})
(9.81\ \mathrm{m/s^2})
\tan(6.2^\circ)
}.
$$

Therefore,

$$
\boxed{
v\approx7.2\ \mathrm{m/s}
}.
$$

Once again, the car’s mass cancels.

# Friction on a Banked Curve

Suppose the ice melts and there is now static friction between the tires and the road.

Friction allows the car to travel either faster or slower than the frictionless design speed without sliding.

The direction of static friction depends on the direction in which the car would otherwise tend to slide.

Let

$$
v_0=\sqrt{rg\tan\theta}
$$

be the speed for which no friction is required.

## Car Moving Slower Than the Design Speed

If the car is stopped or moving slowly, gravity tends to make it slide down the bank.

Static friction therefore points up the slope.

Thus, when

$$
v<v_0,
$$

the friction force points up the bank.

## Car Moving Faster Than the Design Speed

If the car is moving faster than the design speed, its straight-line tendency would carry it toward the outside of the curve. Relative to the banked road, the car tends to slide up the slope.

Static friction therefore points down the slope.

Thus, when

$$
v>v_0,
$$

the friction force points down the bank.

## Car Moving at the Design Speed

When

$$
v=v_0,
$$

the inward component of the normal force alone supplies exactly the required radial force.

No friction is necessary.

# Maximum Speed on a Banked Curve with Friction

We now want to determine the maximum speed at which the car can travel without sliding.

At the maximum speed:

- The car tends to slide up the bank.
- Static friction points down the bank.
- Static friction has reached its maximum value.

Therefore,

$$
f_s=\mu_sN.
$$

## Force Components

The normal force has components

$$
N_y=N\cos\theta
$$

and

$$
N_r=N\sin\theta.
$$

Because friction points down the slope, its components are:

- A downward vertical component $f_s\sin\theta$
- An inward radial component $f_s\cos\theta$

## Vertical Force Equation

The car has no vertical acceleration:

$$
\sum F_y=0.
$$

Therefore,

$$
N\cos\theta-f_s\sin\theta-mg=0.
$$

Substituting

$$
f_s=\mu_sN
$$

gives

$$
N\cos\theta-\mu_sN\sin\theta-mg=0.
$$

Factor out $N$:

$$
N
\left(
\cos\theta-\mu_s\sin\theta
\right)
=
mg.
$$

Therefore,

$$
\boxed{
N
=
\frac{
mg
}{
\cos\theta-\mu_s\sin\theta
}
}.
$$

## Radial Force Equation

The inward radial components of both the normal force and friction contribute to the circular motion:

$$
\sum F_r=m\frac{v^2}{r}.
$$

Therefore,

$$
N\sin\theta+f_s\cos\theta
=
m\frac{v^2}{r}.
$$

Using

$$
f_s=\mu_sN,
$$

we obtain

$$
N\sin\theta+\mu_sN\cos\theta
=
m\frac{v^2}{r}.
$$

Factor out $N$:

$$
N
\left(
\sin\theta+\mu_s\cos\theta
\right)
=
m\frac{v^2}{r}.
$$

Substitute the vertical-equation result for $N$:

$$
\frac{
mg
}{
\cos\theta-\mu_s\sin\theta
}
\left(
\sin\theta+\mu_s\cos\theta
\right)
=
m\frac{v^2}{r}.
$$

The mass cancels:

$$
\frac{
g
\left(
\sin\theta+\mu_s\cos\theta
\right)
}{
\cos\theta-\mu_s\sin\theta
}
=
\frac{v^2}{r}.
$$

Multiplying by $r$ gives

$$
v^2
=
rg
\frac{
\sin\theta+\mu_s\cos\theta
}{
\cos\theta-\mu_s\sin\theta
}.
$$

Therefore, the maximum speed is

$$
\boxed{
v_{\max}
=
\sqrt{
rg
\frac{
\sin\theta+\mu_s\cos\theta
}{
\cos\theta-\mu_s\sin\theta
}
}
}.
$$

Using the numerical values supplied in the problem gives approximately

$$
\boxed{
v_{\max}=25\ \mathrm{m/s}
}.
$$

This is approximately

$$
\boxed{
v_{\max}\approx55\ \mathrm{mph}
}.
$$

The car’s mass and the normal force both cancel from the final result.

# Comparing the Three Curve Situations

## Flat Curve

On a flat curve, static friction supplies the entire inward force:

$$
f_s=m\frac{v^2}{r}.
$$

At the maximum speed,

$$
\boxed{
v_{\max}=\sqrt{\mu_srg}
}.
$$

## Frictionless Banked Curve

On a frictionless banked curve, the inward component of the normal force supplies the radial force:

$$
N\sin\theta=m\frac{v^2}{r}.
$$

The design speed is

$$
\boxed{
v_0=\sqrt{rg\tan\theta}
}.
$$

## Banked Curve with Friction

At the maximum speed, friction points down the bank and contributes to the inward radial force:

$$
\boxed{
v_{\max}
=
\sqrt{
rg
\frac{
\sin\theta+\mu_s\cos\theta
}{
\cos\theta-\mu_s\sin\theta
}
}
}.
$$

# Conical Pendulum

Consider a small object attached to a string and moving in a horizontal circle.

The string remains at a constant angle $\theta$ from the vertical, producing a shape similar to a cone. This system is called a **conical pendulum**.

## Free-Body Diagram

Only two physical forces act on the object:

- The gravitational force $mg$, directed downward
- The tension force $F_T$, directed along the string toward the pivot

There is no separate force called “centripetal force.” The inward component of the tension supplies the required net radial force.

If $\theta$ is measured from the vertical, the tension components are

$$
F_{T,y}=F_T\cos\theta
$$

and

$$
F_{T,r}=F_T\sin\theta.
$$

Because the object has no vertical acceleration,

$$
F_T\cos\theta=mg.
$$

The inward component produces the circular motion:

$$
F_T\sin\theta=m\frac{v^2}{r}.
$$

Dividing the radial equation by the vertical equation gives

$$
\tan\theta
=
\frac{v^2}{rg}.
$$

Therefore,

$$
\boxed{
v=\sqrt{rg\tan\theta}
}.
$$

This is mathematically identical to the result for a car traveling around a frictionless banked curve.

The two systems look physically different, but their free-body diagrams have the same mathematical structure:

- Gravity acts vertically downward.
- A single angled contact force acts upward and inward.
- The vertical component balances gravity.
- The inward component supplies the radial acceleration.

This illustrates the value of beginning each problem with a correct free-body diagram. Systems that appear unrelated may be governed by the same equations.

# General Strategy for Circular-Motion Force Problems

## 1. Draw the Physical Situation

Identify:

- The circular path
- The center of the circle
- The radius
- The direction of the object’s velocity
- Any slope or banking angle

## 2. Draw a Free-Body Diagram

Include only actual physical forces acting on the object.

Possible forces include:

- Gravity
- Normal force
- Friction
- Tension

Do not add a separate “centripetal-force” arrow. Centripetal force describes the net inward result of the actual forces.

## 3. Choose Radial and Vertical Axes

For a horizontal circular path, choose:

- Positive radial direction toward the center
- Positive vertical direction upward

These axes allow the radial equation to be written directly as

$$
\sum F_r=m\frac{v^2}{r}.
$$

## 4. Resolve Angled Forces into Components

For a banked curve:

$$
N_y=N\cos\theta,
$$

$$
N_r=N\sin\theta.
$$

If friction acts along the bank, determine its vertical and radial components from the geometry.

## 5. Determine the Direction of Friction

Static friction opposes the impending relative motion between the tires and the road.

- If the car tends to slide down the bank, friction points up the bank.
- If the car tends to slide up the bank, friction points down the bank.

## 6. Apply Newton’s Second Law Separately

Use

$$
\sum F_y=ma_y
$$

and

$$
\sum F_r=m\frac{v^2}{r}.
$$

For the systems considered here,

$$
a_y=0.
$$

## 7. Use the Maximum Static-Friction Condition Only at the Threshold

In general,

$$
f_s\leq\mu_sN.
$$

Use

$$
f_s=\mu_sN
$$

only when the object is just about to slide.

## 8. Solve Symbolically Before Substituting Numbers

A symbolic solution makes it easier to:

- Identify cancellations
- Check units
- Compare related physical systems
- Analyze how the result changes when a variable changes
- Detect algebraic errors

# Summary

For circular motion,

$$
\boxed{
a_r=\frac{v^2}{r}
}
$$

and

$$
\boxed{
\sum F_r=m\frac{v^2}{r}
}.
$$

For a car traveling on a flat curve, static friction supplies the inward force:

$$
f_s=m\frac{v^2}{r}.
$$

At the maximum speed,

$$
\boxed{
\mu_s=\frac{v^2}{rg}
}
$$

or

$$
\boxed{
v_{\max}=\sqrt{\mu_srg}
}.
$$

For the flat-curve example,

$$
\boxed{
\mu_s\approx0.53
}.
$$

For a frictionless banked curve,

$$
N\cos\theta=mg
$$

and

$$
N\sin\theta=m\frac{v^2}{r}.
$$

Therefore,

$$
\boxed{
v=\sqrt{rg\tan\theta}
}.
$$

For the banked-curve example,

$$
\boxed{
v\approx7.2\ \mathrm{m/s}
}.
$$

On a banked curve with friction:

- Friction points up the slope when the car is moving below the frictionless design speed.
- Friction points down the slope when the car is moving above the frictionless design speed.

At the maximum speed,

$$
\boxed{
v_{\max}
=
\sqrt{
rg
\frac{
\sin\theta+\mu_s\cos\theta
}{
\cos\theta-\mu_s\sin\theta
}
}
}.
$$

For the values used in the problem,

$$
\boxed{
v_{\max}=25\ \mathrm{m/s}
}.
$$

A conical pendulum has the same force-component structure as a frictionless banked curve:

$$
F_T\cos\theta=mg
$$

and

$$
F_T\sin\theta=m\frac{v^2}{r}.
$$

In both systems, the inward component of an angled physical force supplies the radial acceleration. There is no additional centripetal force acting on the object.