# Physics 212: Circular Motion, Ferris Wheels, and Static Friction

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Course Announcements

We are beginning the second week of the summer term. We are currently working through Chapter 8 and should finish it by Tuesday or Wednesday before beginning Chapter 12.

Homework 1 has already closed. Homework 2, covering Chapter 8, is due July 3.

## Proctorio Practice Quiz

Students who plan to take every quiz during a live Zoom session do not need to complete the Proctorio practice quiz.

Students who may use Proctorio must:

1. Read the Proctorio setup and troubleshooting information in the Course Information module.
2. Install and configure Proctorio on the device they will use.
3. Complete the Proctorio practice quiz before Quiz 1.

The practice quiz is intended to verify that the software works correctly before an actual graded assessment.

## Quiz 1 Note Sheet

Every student must submit a handwritten note sheet for Quiz 1.

The note sheet must:

- Be between one-half page and one full page
- Be written entirely by hand on physical paper
- Include relevant equations, diagrams, and other course material
- Be submitted to Gradescope
- Be photographed or scanned with a photo ID placed on top of it

Credit for Quiz 1 cannot be awarded until the required note sheet has been submitted.

The listed due date for the note sheet corresponds to the first opening of the quiz. However, the note sheet will be accepted as long as it is submitted before you begin your quiz.

One of the upcoming pre-lecture assignments will also require a Gradescope upload so that everyone has an opportunity to practice the upload process before taking the quiz.

## Quiz 1 Format

Quiz 1 contains two required parts. Both parts must be completed.

### Part A

Part A contains:

- Three multiple-choice questions
- One short written-response question

### Part B

Part B contains:

- One longer written-response question

Each part allows:

- $20$ minutes to complete the questions
- $5$ additional minutes to upload handwritten work

The two parts may be completed in either order when using the asynchronous version.

### Asynchronous Proctorio Version

The asynchronous version will be available from Saturday at 5:00 p.m. until Monday at 5:00 p.m.

Students will complete the Canvas quiz and then upload their handwritten work to the corresponding Gradescope assignment.

The asynchronous quiz uses banks of equivalent questions, so students may receive different versions. The questions will be designed to have the same general level of difficulty.

### Live Zoom Versions

Live Zoom-proctored sessions will be available Monday at:

- 11:00 a.m.
- 6:00 p.m.

For the 11:00 a.m. session:

- Part A will run from 11:00 to 11:25 a.m.
- A five-minute break will follow.
- Part B will run from 11:30 to 11:55 a.m.

For the 6:00 p.m. session:

- Part A will run from 6:00 to 6:25 p.m.
- A five-minute break will follow.
- Part B will run from 6:30 to 6:55 p.m.

Students using Zoom proctoring must be present in the meeting and remain visible on a functioning webcam throughout the quiz.

## Practice Quiz

A practice quiz will be posted before Quiz 1 is administered.

It will use the same general format as the graded quiz:

- Three multiple-choice questions
- One short written-response problem
- One longer written-response problem

The practice quiz will be provided as a document rather than as a Canvas quiz. A separate document containing worked solutions will also be posted.

## Quiz 1X Extra Credit

The optional Quiz 1X assignment will open after Quiz 1 has been graded.

For Quiz 1X, select the complete Quiz 1 question on which you lost the most points. The assignment will contain four parts.

### Part A: Analyze Your Original Reasoning

Explain why you produced your original answer.

The explanation should focus on the physics concepts and reasoning that were present in your mind when you made each decision. It should not focus on external factors such as stress or time constraints.

### Part B: Explain the Correct Reasoning

Explain what you should have done differently and why.

Identify the relevant physical principles and how they should have guided your solution.

### Part C: Provide a Corrected Solution

Give a complete correct solution.

For written-response questions, this should include:

- A symbolic derivation
- Explicit unit analysis
- Covariational reasoning about how the result depends on the variables

### Part D: Discuss the Problem

Discuss the selected problem with an instructor, teaching assistant, laboratory TA, or another physics staff member.

The assignment will not open until the quiz scores have been released. An announcement will be posted when it becomes available.

## Dropped Scores

The course includes several dropped scores to provide flexibility.

The lowest Quiz Part A score and the lowest Quiz Part B score will be dropped independently. The course also drops:

- Three pre-lecture-question scores
- Three participation-question scores
- One homework score

Laboratory assignments are not dropped.

# Review of Circular Motion

We have been studying circular-motion kinematics and the relationship between rotational and translational quantities.

## Uniform and Nonuniform Circular Motion

In **uniform circular motion**, an object travels around a circle at constant speed.

Its velocity is not constant because the direction of the velocity continually changes. The object therefore accelerates even though the magnitude of its velocity remains constant.

In **nonuniform circular motion**, the object travels around a circle while its speed also changes.

The acceleration may be separated into radial and tangential components:

$$
\vec{a}=a_r\hat{r}+a_t\hat{t}.
$$

The radial component points toward the center of the circle and changes the direction of the velocity.

The tangential component points along or opposite the direction of motion and changes the object’s speed.

## Translational and Rotational Relationships

For a point moving through an angular displacement $\theta$ at a radius $r$, the arc length is

$$
s=r\theta.
$$

Taking the time derivative gives the tangential speed:

$$
v=\frac{ds}{dt}.
$$

Because

$$
\omega=\frac{d\theta}{dt},
$$

we obtain

$$
\boxed{
v=\omega r
}.
$$

Taking another time derivative gives the tangential acceleration:

$$
a_t=\frac{dv}{dt}.
$$

For a constant radius,

$$
\boxed{
a_t=\alpha r
},
$$

where

$$
\alpha=\frac{d\omega}{dt}.
$$

The radial acceleration is

$$
\boxed{
a_r=\frac{v^2}{r}
}.
$$

Using $v=\omega r$, this may also be written as

$$
\boxed{
a_r=\omega^2r
}.
$$

The radial acceleration always points toward the center of the circular path.

## Period and Speed

The distance traveled during one complete revolution is the circumference:

$$
\Delta s=2\pi r.
$$

If the period is $T$, then the speed is

$$
\boxed{
v=\frac{2\pi r}{T}
}.
$$

Equivalently,

$$
\boxed{
T=\frac{2\pi r}{v}
}.
$$

## Constant Angular-Acceleration Equations

When angular acceleration is constant, the rotational kinematic equations are analogous to the ordinary constant-acceleration equations:

$$
\omega_f=\omega_i+\alpha\Delta t,
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

# Worked Example 1: Speed of a Ferris-Wheel Rider

Consider a Ferris wheel with radius

$$
r=42\ \mathrm{m}
$$

rotating at a constant angular speed

$$
\omega=0.16\ \mathrm{rad/s}.
$$

We want to determine the speed of a person riding on the rim.

The relationship between tangential speed and angular speed is

$$
v=\omega r.
$$

Substituting the given values,

$$
v
=
(0.16\ \mathrm{rad/s})
(42\ \mathrm{m}).
$$

Because radians are dimensionless,

$$
v=6.72\ \mathrm{m/s}.
$$

Using two significant figures,

$$
\boxed{
v=6.7\ \mathrm{m/s}
}.
$$

Although the rider’s speed is constant, the rider is accelerating because the direction of the velocity changes continually.

# Normal Force at the Top and Bottom of a Ferris Wheel

Now consider a rider of mass $m$ seated on the Ferris wheel.

The two forces acting on the rider are:

- The gravitational force $mg$, directed downward
- The normal force from the seat, directed away from the seat

The rider’s acceleration must point toward the center of the Ferris wheel.

At the top, the center of the wheel is below the rider. At the bottom, the center is above the rider.

Consequently, the normal force is larger at the bottom than it is at the top:

$$
\boxed{
N_{\mathrm{bottom}}>N_{\mathrm{top}}
}.
$$

The normal force is what the rider experiences as apparent weight.

A similar effect occurs while driving over a hill or through a dip:

- At the top of a hill, the seat pushes on you less strongly, so you feel lighter.
- At the bottom of a dip, the seat pushes on you more strongly, so you feel heavier.

There is no actual upward force lifting you out of the seat at the top of the hill. Instead, your body tends to continue along its instantaneous tangent while the road or seat curves downward beneath you.

## Free-Body Diagram at the Bottom

At the bottom of the Ferris wheel:

- The inward radial direction is upward.
- The normal force points upward.
- Gravity points downward.

Choose the inward direction as positive.

Newton’s second law in the radial direction is

$$
\sum F_r=ma_r.
$$

Therefore,

$$
N_{\mathrm{bottom}}-mg
=
m\frac{v^2}{r}.
$$

Solving for the normal force,

$$
N_{\mathrm{bottom}}
=
mg+m\frac{v^2}{r}.
$$

Using

$$
v=\omega r,
$$

we have

$$
\frac{v^2}{r}
=
\frac{\omega^2r^2}{r}
=
\omega^2r.
$$

Thus,

$$
\boxed{
N_{\mathrm{bottom}}
=
m(g+\omega^2r)
}.
$$

For a rider with mass

$$
m=68\ \mathrm{kg},
$$

the normal force is

$$
N_{\mathrm{bottom}}
=
(68\ \mathrm{kg})
\left[
9.81\ \mathrm{m/s^2}
+
(0.16\ \mathrm{rad/s})^2
(42\ \mathrm{m})
\right].
$$

Evaluating,

$$
N_{\mathrm{bottom}}
\approx
7.4\times10^2\ \mathrm{N}.
$$

Therefore,

$$
\boxed{
N_{\mathrm{bottom}}\approx740\ \mathrm{N}
}.
$$

This is greater than the rider’s ordinary weight because the seat must both support the rider against gravity and provide the net upward radial force.

## Free-Body Diagram at the Top

At the top of the Ferris wheel:

- The inward radial direction is downward.
- Gravity points downward.
- The normal force points upward.

Again choose the inward direction as positive.

The radial force equation is

$$
mg-N_{\mathrm{top}}
=
m\frac{v^2}{r}.
$$

Solving for the normal force,

$$
N_{\mathrm{top}}
=
mg-m\frac{v^2}{r}.
$$

Using $v=\omega r$,

$$
\boxed{
N_{\mathrm{top}}
=
m(g-\omega^2r)
}.
$$

Substituting the values,

$$
N_{\mathrm{top}}
=
(68\ \mathrm{kg})
\left[
9.81\ \mathrm{m/s^2}
-
(0.16\ \mathrm{rad/s})^2
(42\ \mathrm{m})
\right].
$$

This gives approximately

$$
\boxed{
N_{\mathrm{top}}\approx590\ \mathrm{N}
}.
$$

At the top, gravity already supplies part of the required inward force. The seat therefore does not need to push as strongly on the rider.

## Comparing the Two Positions

The results are

$$
N_{\mathrm{bottom}}
=
m(g+\omega^2r)
$$

and

$$
N_{\mathrm{top}}
=
m(g-\omega^2r).
$$

Therefore,

$$
\boxed{
N_{\mathrm{bottom}}>mg>N_{\mathrm{top}}
}.
$$

The rider feels heavier at the bottom and lighter at the top.

If the Ferris wheel were moving nonuniformly, a tangential acceleration would also be present. The total acceleration would no longer point directly toward the center, although the radial component would still point inward.

# Symbolic Solutions and Significant Figures

In written physics problems, solve symbolically before inserting numbers.

For example, the bottom normal force should first be written as

$$
N_{\mathrm{bottom}}
=
m(g+\omega^2r).
$$

Only after obtaining this symbolic expression should the numerical values be substituted.

A symbolic solution:

- Shows the physical reasoning clearly
- Makes algebraic errors easier to identify
- Allows unit checking
- Reveals how the result changes when a variable changes
- Remains useful even when no numerical values are supplied

Final numerical answers should generally use the same number of significant figures as the least precise given value. Keeping one additional digit during intermediate calculations is appropriate, but reporting excessive precision can produce an answer outside an automated system’s accepted range.

# Coin on a Rotating Turntable

Consider a coin of mass $m$ resting on a horizontal turntable.

The coin is located a distance $r$ from the rotation axis, and the turntable rotates with angular speed $\omega$.

The coefficient of static friction between the coin and turntable is $\mu_s$. We want to determine the greatest angular speed for which the coin does not slip.

## Forces on the Coin

The forces acting on the coin are:

- Gravity $mg$, downward
- The normal force $N$, upward
- Static friction $f_s$, horizontally inward toward the center of the turntable

Static friction supplies the radial force required for circular motion.

There is no separate force called the centripetal force. The phrase **centripetal force** refers to the net inward force, which in this case is the static-friction force.

## Vertical Force Balance

The coin has no vertical acceleration, so

$$
\sum F_y=0.
$$

Therefore,

$$
N-mg=0,
$$

which gives

$$
\boxed{
N=mg
}.
$$

## Radial Force Equation

The inward radial acceleration is

$$
a_r=\frac{v^2}{r}.
$$

Because

$$
v=\omega r,
$$

we may also write

$$
a_r=\omega^2r.
$$

Static friction is the only radial force, so

$$
f_s=m\omega^2r.
$$

This equation gives the actual static-friction force required at any angular speed below the slipping threshold.

Static friction is not automatically equal to $\mu_sN$. In general,

$$
f_s\leq\mu_sN.
$$

The equality applies only when the coin is just about to slip.

## Maximum Angular Speed

At the threshold of slipping,

$$
f_s=f_{s,\max}=\mu_sN.
$$

Using $N=mg$,

$$
f_{s,\max}=\mu_smg.
$$

Set this equal to the required radial force:

$$
m\omega_{\max}^2r
=
\mu_smg.
$$

The mass cancels:

$$
\omega_{\max}^2r
=
\mu_sg.
$$

Solving for the angular speed,

$$
\boxed{
\omega_{\max}
=
\sqrt{\frac{\mu_sg}{r}}
}.
$$

For the coefficient given in the activity,

$$
\mu_s=0.24,
$$

the result may be written as

$$
\omega_{\max}
=
\sqrt{\frac{(0.24)g}{r}}.
$$

The coin’s mass does not affect the maximum angular speed.

## Covariational Reasoning

The symbolic result is

$$
\omega_{\max}
=
\sqrt{\frac{\mu_sg}{r}}.
$$

This immediately reveals several physical relationships.

### Effect of the Friction Coefficient

If $\mu_s$ increases, the turntable can rotate more rapidly before the coin slips:

$$
\mu_s\uparrow
\quad\Longrightarrow\quad
\omega_{\max}\uparrow.
$$

A larger coefficient of static friction allows a greater inward force.

### Effect of Radius

If the coin is moved farther from the center, the maximum angular speed decreases:

$$
r\uparrow
\quad\Longrightarrow\quad
\omega_{\max}\downarrow.
$$

At a larger radius, the required radial acceleration

$$
a_r=\omega^2r
$$

is greater for the same angular speed.

### Effect of Gravity

If $g$ increases, the normal force increases, which increases the maximum available static friction:

$$
g\uparrow
\quad\Longrightarrow\quad
\omega_{\max}\uparrow.
$$

# General Strategy for Circular-Motion Force Problems

## 1. Draw the Physical Situation

Identify:

- The circular path
- The center of the circle
- The radius
- The direction of motion
- The point being analyzed

## 2. Draw a Free-Body Diagram

Include only actual physical forces acting on the selected object.

Possible forces include:

- Gravity
- Normal force
- Tension
- Friction

Do not add a separate centripetal-force vector.

## 3. Choose the Radial Direction

It is usually convenient to choose the inward radial direction as positive.

The radial acceleration can then be written as the positive magnitude

$$
a_r=\frac{v^2}{r}=\omega^2r.
$$

## 4. Apply Newton’s Second Law

Write a separate equation for each relevant direction.

For example,

$$
\sum F_r=m\frac{v^2}{r}
$$

and

$$
\sum F_y=ma_y.
$$

## 5. Use Friction Conditions Carefully

For static friction,

$$
f_s\leq\mu_sN.
$$

Use

$$
f_s=\mu_sN
$$

only when the object is at the threshold of slipping.

## 6. Solve Symbolically

Isolate the requested variable before inserting numerical values.

## 7. Check the Result

Verify:

- Units
- Signs
- Significant figures
- Limiting behavior
- Physical reasonableness

# Summary

Uniform circular motion occurs when an object moves around a circle at constant speed. The direction of its velocity changes, so it has an inward radial acceleration.

The relationships among tangential and rotational quantities are

$$
\boxed{
v=\omega r
}
$$

and

$$
\boxed{
a_t=\alpha r
}.
$$

The radial acceleration is

$$
\boxed{
a_r=\frac{v^2}{r}=\omega^2r
}.
$$

For a Ferris wheel with angular speed $\omega$ and radius $r$, the rider’s speed is

$$
\boxed{
v=\omega r
}.
$$

For the values used in the lecture,

$$
\boxed{
v=6.7\ \mathrm{m/s}
}.
$$

At the bottom of the Ferris wheel,

$$
\boxed{
N_{\mathrm{bottom}}
=
m(g+\omega^2r)
}.
$$

For the rider in the example,

$$
\boxed{
N_{\mathrm{bottom}}\approx740\ \mathrm{N}
}.
$$

At the top,

$$
\boxed{
N_{\mathrm{top}}
=
m(g-\omega^2r)
}.
$$

For the same rider,

$$
\boxed{
N_{\mathrm{top}}\approx590\ \mathrm{N}
}.
$$

Thus,

$$
\boxed{
N_{\mathrm{bottom}}>N_{\mathrm{top}}
}.
$$

For a coin on a horizontal rotating turntable, static friction supplies the radial force:

$$
f_s=m\omega^2r.
$$

At the threshold of slipping,

$$
\mu_smg=m\omega_{\max}^2r.
$$

Therefore,

$$
\boxed{
\omega_{\max}
=
\sqrt{\frac{\mu_sg}{r}}
}.
$$

A larger coefficient of static friction permits a greater angular speed, while placing the coin farther from the rotation axis lowers the angular speed at which slipping begins.

---

Up Next: [Circular Motion on Flat and Banked Curves](../../2026-06-30-M1-4/Source/Lecture-Transcript.md)
Previous: [Covariational Reasoning and Radial Acceleration](../../2026-06-25-M1-2/Source/Lecture-Transcript.md)

---
