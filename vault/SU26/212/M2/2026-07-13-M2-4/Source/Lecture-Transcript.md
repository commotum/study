# Physics 212: Static Equilibrium and Rotational Dynamics

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 1 grading is nearly complete, and the scores will be posted this afternoon.

If you completed the asynchronous version of Quiz 1, you may see separate Gradescope work assignments for Quiz 1A and Quiz 1B listed in Canvas. Those entries are provided so that you can view your submitted work and grading details, but they do not contribute separately to your course grade. The score entered in the primary Canvas quiz assignment is the score used in the grade calculation.

If you completed the Zoom version of the quiz, your Gradescope score will be transferred into Canvas.

To see how an individual question was graded, open the assignment in Gradescope and select the question name in the upper-right corner. This will display the grading rubric and show how points were awarded.

If you believe a question was graded incorrectly, submit a regrade request through Gradescope. Regrade requests will remain available for 15 days. Be specific in your request and refer directly to the relevant physics concepts.

The optional Quiz 1X assignment will open when the Quiz 1 scores are posted. For Quiz 1X, select only the question on which you lost the most points.

The assignment has four parts:

1. Explain the reasoning that led to your original answer.
2. Explain what you should have done differently and identify the relevant physics concepts.
3. Provide a complete corrected solution, including explicit unit analysis and covariational reasoning.
4. Discuss the problem with an instructor, teaching assistant, or another physics staff member.

Part 4 may be completed during office hours, after a lab session if time permits, or in the Wormhole. If the regular daytime hours do not fit your schedule, consult the TA schedules in the Course Information module and contact a TA to arrange another meeting time.

Quiz 1X is due Friday at 6:00 p.m. Late submissions will not be accepted, so leave enough time to upload your written work to Gradescope.

Quiz 2 will open for the Proctorio version at 5:00 p.m. Saturday and close at 5:00 p.m. Monday. The Zoom versions will be administered Monday at 11:00 a.m. and 6:00 p.m.

You should be preparing your handwritten note sheet for Quiz 2. All material on the note sheet must be handwritten.

## Review of Rotational Mechanics

We began this unit by discussing center of mass. For a system of discrete particles, the center-of-mass position is

$$
\vec{r}_{\mathrm{cm}}
=
\frac{\sum_i m_i\vec{r}_i}{\sum_i m_i}.
$$

We then introduced rotational kinetic energy:

$$
K_{\mathrm{rot}}
=
\frac{1}{2}I\omega^2,
$$

where $I$ is the moment of inertia about the chosen rotation axis and $\omega$ is the angular velocity.

For a collection of point masses,

$$
I=\sum_i m_ir_{\perp,i}^2.
$$

For a continuous object,

$$
I=\int r_\perp^2\,dm.
$$

The standard moments of inertia for common objects are important enough to include on your Quiz 2 note sheet.

We also introduced the parallel-axis theorem:

$$
I_p
=
I_{\mathrm{cm}}+Md^2,
$$

where:

- $I_p$ is the moment of inertia about the desired pivot,
- $I_{\mathrm{cm}}$ is the moment of inertia about a parallel axis through the center of mass,
- $M$ is the object’s mass, and
- $d$ is the distance between the two axes.

Finally, we began studying torque.

Torque is defined by the cross product

$$
\vec{\tau}
=
\vec{r}\times\vec{F}.
$$

Its magnitude is

$$
\tau
=
rF\sin\theta,
$$

where $\theta$ is the angle between the position vector $\vec{r}$ and the force vector $\vec{F}$.

The rotational form of Newton’s second law is

$$
\sum\vec{\tau}
=
I\vec{\alpha}.
$$

For a system in static equilibrium,

$$
\sum\vec{F}=0
$$

and

$$
\sum\vec{\tau}=0.
$$

## Extended Free-Body Diagrams

An ordinary point-particle free-body diagram shows all forces acting on an object, but it does not show where those forces act.

An **extended free-body diagram** includes:

- The shape and orientation of the object
- The point of application of each force
- The selected pivot
- The distance from the pivot to each force
- The angle between each force and its position vector

This information is necessary for calculating torque.

It is also important to distinguish the gravitational force on an object from the contact force that the object exerts on something else.

For example, suppose a mouse stands on a horizontal rod. The gravitational force $mg$ acts on the mouse. The mouse then exerts a downward normal force on the rod. The force appearing on the rod’s free-body diagram is that normal force, not the gravitational force acting directly on the mouse.

The two may have the same magnitude when the mouse has no vertical acceleration, but they act on different objects.

# Static Equilibrium and Tipping

A rigid object remains in static equilibrium when both its net force and its net torque are zero:

$$
\sum\vec{F}=0
$$

and

$$
\sum\vec{\tau}=0.
$$

When an object is just about to tip, one of its contact forces becomes zero. The remaining contact point becomes the effective pivot.

Immediately before tipping begins, the object is still in static equilibrium, so

$$
\alpha=0
$$

and

$$
\sum\tau=0.
$$

# Worked Example 1: Box on a Supported Plank

Consider a uniform plank with:

- Length $L$
- Mass $M$
- A left support at $L/5$ from the left end
- A right support, labeled $B$, at $2L/3$ from the left end

A box of mass $m$ is placed a distance $x$ to the right of support $B$.

We want to determine the value of $x$ for which the plank is just about to tip clockwise around support $B$.

## Tipping Condition

As the box is moved to the right, the normal force from the left support decreases.

At the tipping threshold,

$$
N_A=0.
$$

Support $B$ becomes the pivot.

The normal force from support $B$ does not contribute to the torque equation because its line of action passes directly through the pivot.

## Free-Body Diagram of the Box

The forces on the box are:

- The gravitational force $mg$ downward
- The normal force from the plank, $N_{P\rightarrow b}$, upward

Because the box has no vertical acceleration,

$$
\sum F_y=0.
$$

Therefore,

$$
N_{P\rightarrow b}-mg=0,
$$

so

$$
N_{P\rightarrow b}=mg.
$$

By Newton’s third law, the box exerts an equal-magnitude downward force on the plank:

$$
N_{b\rightarrow P}=mg.
$$

This downward normal force is the force that should appear on the plank’s free-body diagram.

## Forces on the Plank

At the tipping threshold, the forces on the plank are:

- The plank’s weight $Mg$, acting at its center
- The downward normal force $mg$ from the box
- The upward normal force $N_B$ from support $B$
- No force from support $A$, because $N_A=0$

The vertical-force equation is

$$
N_B-Mg-mg=0.
$$

Therefore,

$$
N_B=(M+m)g.
$$

This result is not required to find $x$, but it confirms the vertical-force balance.

## Lever Arms About Support B

The plank’s center of mass is at

$$
\frac{L}{2}
$$

from the left end.

Support $B$ is at

$$
\frac{2L}{3}
$$

from the left end.

The distance between the plank’s center of mass and support $B$ is therefore

$$
\frac{2L}{3}-\frac{L}{2}.
$$

Using a common denominator,

$$
\frac{2L}{3}-\frac{L}{2}
=
\frac{4L}{6}-\frac{3L}{6}
=
\frac{L}{6}.
$$

Thus, the plank’s weight acts a distance $L/6$ to the left of the pivot.

The box acts a distance $x$ to the right of the pivot.

## Torque Balance

Choose clockwise torque to be positive.

The box produces a clockwise torque:

$$
\tau_{\mathrm{box}}=mgx.
$$

The plank’s weight produces a counterclockwise torque:

$$
\tau_{\mathrm{plank}}
=
-Mg\left(\frac{L}{6}\right).
$$

At the tipping threshold,

$$
\sum\tau_B=0.
$$

Therefore,

$$
mgx
-
Mg\left(\frac{L}{6}\right)
=
0.
$$

Rearranging,

$$
mgx
=
Mg\frac{L}{6}.
$$

Canceling $g$,

$$
mx
=
M\frac{L}{6}.
$$

Solving for $x$ gives

$$
\boxed{
x=\frac{M}{m}\frac{L}{6}
}.
$$

For

$$
M=2.4\ \mathrm{kg},
$$

$$
m=1.6\ \mathrm{kg},
$$

and

$$
L=1.4\ \mathrm{m},
$$

we obtain

$$
x
=
\frac{2.4\ \mathrm{kg}}{1.6\ \mathrm{kg}}
\frac{1.4\ \mathrm{m}}{6}.
$$

The mass units cancel:

$$
x
=
1.5
\left(
\frac{1.4\ \mathrm{m}}{6}
\right).
$$

Therefore,

$$
\boxed{
x=0.35\ \mathrm{m}
}.
$$

The result is physically reasonable. The box must be placed to the right of support $B$, but it remains on the plank because the available distance from $B$ to the right end is

$$
L-\frac{2L}{3}
=
\frac{L}{3}.
$$

For $L=1.4\ \mathrm{m}$,

$$
\frac{L}{3}
\approx0.47\ \mathrm{m},
$$

which is greater than the required distance of $0.35\ \mathrm{m}$.

The symbolic result also has sensible covariational behavior:

- Increasing the plank mass $M$ requires the box to be placed farther from the pivot.
- Increasing the box mass $m$ allows the box to be placed closer to the pivot.
- Increasing the plank length $L$ increases the required distance proportionally.

# Worked Example 2: Ladder Against a Frictionless Wall

Consider a uniform ladder with:

- Length $L$
- Mass $m$
- An angle $\theta$ above the floor
- A frictionless wall
- Static friction between the ladder and the floor

The ladder is at the threshold of slipping. We want to determine the required coefficient of static friction $\mu_s$.

At the threshold of slipping, the static-friction force has its maximum possible magnitude:

$$
f_s=\mu_sN_F,
$$

where $N_F$ is the normal force from the floor.

This equality applies only because the ladder is just about to slip. In general, static friction may be less than $\mu_sN_F$.

## Forces on the Ladder

The forces are:

- The gravitational force $mg$, acting downward at the center of the ladder
- The normal force $N_F$ from the floor, acting upward at the bottom
- The static-friction force $f_s$ from the floor, acting horizontally
- The normal force $N_W$ from the wall, acting horizontally at the top

Because the wall is frictionless, it exerts no vertical force.

## Translational Equilibrium

In the vertical direction,

$$
\sum F_y=0.
$$

Therefore,

$$
N_F-mg=0,
$$

so

$$
\boxed{
N_F=mg
}.
$$

In the horizontal direction,

$$
\sum F_x=0.
$$

The wall’s normal force and the floor’s friction force must have equal magnitudes:

$$
N_W-f_s=0.
$$

Thus,

$$
N_W=f_s.
$$

At the threshold of slipping,

$$
f_s=\mu_sN_F.
$$

Using $N_F=mg$,

$$
f_s=\mu_smg.
$$

Therefore,

$$
\boxed{
N_W=\mu_smg
}.
$$

## Torque About the Bottom of the Ladder

Choose the bottom of the ladder as the pivot.

This choice eliminates both floor forces from the torque equation because they act through the pivot.

The wall’s normal force acts at the top of the ladder. Its perpendicular moment arm is

$$
L\sin\theta.
$$

The wall force therefore produces a torque of magnitude

$$
\tau_W=N_WL\sin\theta.
$$

The gravitational force acts at the ladder’s center, a distance $L/2$ from the bottom. Its perpendicular moment arm is

$$
\frac{L}{2}\cos\theta.
$$

The gravitational torque therefore has magnitude

$$
\tau_g
=
mg\frac{L}{2}\cos\theta.
$$

The two torques act in opposite rotational directions. Static equilibrium requires

$$
N_WL\sin\theta
-
mg\frac{L}{2}\cos\theta
=
0.
$$

Therefore,

$$
N_WL\sin\theta
=
mg\frac{L}{2}\cos\theta.
$$

Canceling $L$,

$$
N_W\sin\theta
=
\frac{mg}{2}\cos\theta.
$$

Solving for $N_W$,

$$
N_W
=
\frac{mg}{2}
\frac{\cos\theta}{\sin\theta}.
$$

Thus,

$$
N_W
=
\frac{mg}{2}\cot\theta.
$$

We also found that

$$
N_W=\mu_smg.
$$

Equating the expressions,

$$
\mu_smg
=
\frac{mg}{2}\cot\theta.
$$

Canceling $mg$ gives

$$
\boxed{
\mu_s
=
\frac{1}{2}\cot\theta
}.
$$

An equivalent expression is

$$
\boxed{
\mu_s
=
\frac{1}{2\tan\theta}
}.
$$

Using the angle specified in the problem gives

$$
\boxed{
\mu_s=0.34
}.
$$

The result does not depend on the ladder’s mass or length because both quantities cancel.

The limiting behavior is physically reasonable:

- As $\theta$ approaches $90^\circ$, the ladder becomes nearly vertical and the required friction approaches zero.
- As $\theta$ approaches $0^\circ$, the ladder becomes nearly horizontal and the required coefficient of friction grows very large.

The central step in this problem is constructing the extended free-body diagram correctly. Once the forces, application points, distances, and angles are identified, the torque equation follows directly.

# Rotational Dynamics with a Massive Pulley

The previous examples involved static equilibrium, so both the linear acceleration and angular acceleration were zero.

We will now consider a system that accelerates.

Suppose two masses, $m_1$ and $m_2$, are connected by a light cord passing over a massive pulley.

Let:

- $m_1<m_2$
- $M_p$ be the mass of the pulley
- $R$ be the radius of the pulley
- $T_1$ be the tension on the $m_1$ side
- $T_2$ be the tension on the $m_2$ side

Because $m_2>m_1$, mass $m_2$ accelerates downward, mass $m_1$ accelerates upward, and the pulley accelerates clockwise.

Assume:

- The cord does not slip on the pulley
- The cord has negligible mass
- The pulley is a uniform solid disk
- The axle is frictionless

Because the pulley has rotational inertia, the two tensions are not equal.

The tension difference supplies the net torque that angularly accelerates the pulley:

$$
T_2>T_1.
$$

If the tensions were equal, the net torque on the pulley would be zero.

## Free-Body Diagram of Mass $m_1$

Choose upward as positive for $m_1$.

The forces are:

- $T_1$ upward
- $m_1g$ downward

Newton’s second law gives

$$
T_1-m_1g=m_1a.
$$

Solving for $T_1$,

$$
\boxed{
T_1=m_1g+m_1a
}
$$

or

$$
\boxed{
T_1=m_1(g+a)
}.
$$

Because $m_1$ accelerates upward,

$$
T_1>m_1g.
$$

## Free-Body Diagram of Mass $m_2$

Choose downward as positive for $m_2$.

The forces are:

- $m_2g$ downward
- $T_2$ upward

Newton’s second law gives

$$
m_2g-T_2=m_2a.
$$

Solving for $T_2$,

$$
\boxed{
T_2=m_2g-m_2a
}
$$

or

$$
\boxed{
T_2=m_2(g-a)
}.
$$

Because $m_2$ accelerates downward,

$$
T_2<m_2g.
$$

## Torque on the Pulley

Choose clockwise torque to be positive.

The pulley’s weight and the axle force both act through the center of the pulley, so neither produces torque about the pulley’s axis.

The two cord tensions produce opposite torques:

$$
\sum\tau
=
T_2R-T_1R.
$$

The rotational equation of motion is

$$
T_2R-T_1R=I_p\alpha.
$$

For a uniform solid-disk pulley,

$$
I_p=\frac{1}{2}M_pR^2.
$$

Because the cord does not slip,

$$
a=\alpha R.
$$

Therefore,

$$
\alpha=\frac{a}{R}.
$$

Substituting into the torque equation,

$$
T_2R-T_1R
=
\left(
\frac{1}{2}M_pR^2
\right)
\left(
\frac{a}{R}
\right).
$$

Simplifying,

$$
(T_2-T_1)R
=
\frac{1}{2}M_pRa.
$$

Canceling $R$ gives

$$
\boxed{
T_2-T_1
=
\frac{1}{2}M_pa
}.
$$

## Solving for the Acceleration

Substitute the expressions for the two tensions:

$$
m_2(g-a)-m_1(g+a)
=
\frac{1}{2}M_pa.
$$

Expanding,

$$
m_2g-m_2a-m_1g-m_1a
=
\frac{1}{2}M_pa.
$$

Group the gravitational terms:

$$
(m_2-m_1)g
-
(m_1+m_2)a
=
\frac{1}{2}M_pa.
$$

Move all acceleration terms to the same side:

$$
(m_2-m_1)g
=
m_1a+m_2a+\frac{1}{2}M_pa.
$$

Factor out $a$:

$$
(m_2-m_1)g
=
a
\left(
m_1+m_2+\frac{1}{2}M_p
\right).
$$

Therefore,

$$
\boxed{
a
=
\frac{
(m_2-m_1)g
}{
m_1+m_2+\frac{1}{2}M_p
}
}.
$$

Using the numerical values supplied in the problem gives

$$
\boxed{
a=2.5\ \mathrm{m}/\mathrm{s}^2
}.
$$

## General Form

For a pulley with an arbitrary moment of inertia $I_p$, the torque equation gives

$$
T_2-T_1
=
\frac{I_p}{R^2}a.
$$

The acceleration is therefore

$$
\boxed{
a
=
\frac{
(m_2-m_1)g
}{
m_1+m_2+\frac{I_p}{R^2}
}
}.
$$

For a uniform solid disk,

$$
\frac{I_p}{R^2}
=
\frac{
\frac{1}{2}M_pR^2
}{
R^2
}
=
\frac{1}{2}M_p,
$$

which recovers the previous result.

## Physical Interpretation

The pulley’s rotational inertia reduces the acceleration of the system.

For a massless pulley,

$$
I_p=0,
$$

so the acceleration becomes

$$
a
=
\frac{
(m_2-m_1)g
}{
m_1+m_2
}.
$$

This is the standard result for an ideal Atwood machine.

For a massive pulley, some of the gravitational potential energy released by the descending mass must become rotational kinetic energy of the pulley. The linear acceleration is therefore smaller than it would be with a massless pulley.

The symbolic result passes several useful checks:

- If $m_1=m_2$, then $a=0$.
- Increasing $m_2-m_1$ increases the acceleration.
- Increasing the pulley mass decreases the acceleration.
- If $M_p\rightarrow0$, the massless-pulley result is recovered.
- The acceleration remains less than $g$.
- The denominator has units of mass, so the result has units of acceleration.

# General Strategy for Torque Problems

## 1. Identify the System

Decide which object or collection of objects is being analyzed.

A force should appear on a free-body diagram only if it acts directly on the chosen system.

## 2. Draw a Point-Particle Free-Body Diagram

Use this diagram to write the translational equations:

$$
\sum F_x=ma_x
$$

and

$$
\sum F_y=ma_y.
$$

## 3. Draw an Extended Free-Body Diagram

Show:

- The shape of the object
- Every force
- The point where each force acts
- The pivot
- Every relevant distance and angle

## 4. Choose the Pivot Strategically

A force whose line of action passes through the pivot produces zero torque about that pivot.

Choosing the pivot at an unknown support force can eliminate that force from the torque equation.

## 5. Choose a Rotational Sign Convention

State whether clockwise or counterclockwise torque is positive.

Then apply the sign convention consistently.

## 6. Write the Torque Equation

Use

$$
\sum\tau=I\alpha.
$$

For static equilibrium,

$$
\alpha=0,
$$

so

$$
\sum\tau=0.
$$

## 7. Apply the Appropriate Constraint

Examples include:

- At impending tipping, one support force becomes zero.
- At impending slipping, $f_s=\mu_sN$.
- For rolling or a non-slipping cord, $a=\alpha R$.
- For a massless ideal cord, connected objects have the same acceleration magnitude.

## 8. Solve Symbolically Before Substituting Numbers

A symbolic result makes it easier to:

- Check dimensions
- Identify cancellations
- Analyze how variables affect the result
- Test limiting cases
- Detect algebraic mistakes

# Summary

Torque is

$$
\boxed{
\vec{\tau}
=
\vec{r}\times\vec{F}
}
$$

with magnitude

$$
\boxed{
\tau=rF\sin\theta
}.
$$

Rotational dynamics is governed by

$$
\boxed{
\sum\tau=I\alpha
}.
$$

For static equilibrium,

$$
\boxed{
\sum\vec{F}=0
}
$$

and

$$
\boxed{
\sum\tau=0
}.
$$

For the tipping plank, the left support force becomes zero and support $B$ becomes the pivot. The required box position is

$$
\boxed{
x=\frac{M}{m}\frac{L}{6}
}.
$$

For the values used in the problem,

$$
\boxed{
x=0.35\ \mathrm{m}
}.
$$

For a uniform ladder against a frictionless wall at the threshold of slipping,

$$
\boxed{
\mu_s
=
\frac{1}{2}\cot\theta
=
\frac{1}{2\tan\theta}
}.
$$

For the angle supplied in the problem,

$$
\boxed{
\mu_s=0.34
}.
$$

For two masses connected over a uniform solid-disk pulley,

$$
T_1=m_1(g+a),
$$

$$
T_2=m_2(g-a),
$$

and

$$
T_2-T_1=\frac{1}{2}M_pa.
$$

The acceleration is

$$
\boxed{
a
=
\frac{
(m_2-m_1)g
}{
m_1+m_2+\frac{1}{2}M_p
}
}.
$$

For the numerical values supplied in the problem,

$$
\boxed{
a=2.5\ \mathrm{m}/\mathrm{s}^2
}.
$$

The central skill in all of these problems is constructing a correct extended free-body diagram. Once the forces, application points, lever arms, and rotational directions are identified, the equations of force and torque follow systematically.

---

Up Next: [Rolling Motion and Conservation of Angular Momentum](../../2026-07-14-M2-5/Source/Lecture-Transcript.md)
Previous: [Torque, Moment Arms, and Rotational Dynamics](../../2026-07-09-M2-3/Source/Lecture-Transcript.md)

---
