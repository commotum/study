# Physics 212: Course Framework and Introduction to Rotational Kinematics

Welcome back to Physics 212.

## Course Questions and Logistics

Because we are only on the second day of the term, we will begin by clarifying several aspects of how the course operates.

### Laboratory TA Meetings

Regular laboratory meetings with teaching assistants will generally begin during the second week of the term. Because laboratory groups and meeting schedules are still being organized, students automatically receive the associated meeting credit during the first week.

A group that has already arranged a meeting may contact its TA and ask to meet during the first week, but doing so is not required.

### Office Hours and Questions

An office hour is held immediately after each lecture. Additional meetings may be arranged by appointment.

Questions about the course may also be sent by email. If something appears incorrect or inconsistent in Canvas, notify the instructor so that it can be reviewed and corrected.

### Course Announcements and Notifications

Important course information will frequently be distributed through Canvas announcements. Check the notification settings for this course and make sure that announcements are enabled.

Canvas allows notification preferences to be configured either for the entire account or separately for each course. At a minimum, enable announcement notifications for Physics 212 so that you receive information about assignments, quizzes, schedule changes, and corrections.

### Participation Scores in Canvas

Students attending a live Zoom lecture receive participation credit by responding to the Poll Everywhere questions used during class.

Students completing the lecture asynchronously submit the corresponding asynchronous participation assignment instead. Until that assignment is graded, Canvas may temporarily display a zero in the participation column. That zero lowers the calculated Canvas grade even though the asynchronous work may already have been submitted.

After the asynchronous submissions are graded, the temporary zero is removed or replaced with the appropriate score.

Asynchronous participation assignments generally remain available for $48$ hours, followed by an additional grace period. A late submission does not lose a point until it is a full day late, and the score does not fall below $50\%$ solely because of lateness.

Because the course drops three participation scores, missing a single participation activity will not necessarily affect the final grade.

Participation activities collectively account for only $5\%$ of the course grade. Early in the term, the Canvas grade may appear unusually high or low because it is being calculated from a very small number of assignments. Continue checking the gradebook for accuracy, but do not treat the first few calculated percentages as reliable indicators of your eventual course performance.

### Assignment Due Dates

The PDF syllabus posted in the Course Information module contains the authoritative course schedule.

The page labeled “Syllabus” in the Canvas navigation menu is generated from the Canvas calendar. It may display tentative dates for unpublished assignments that have not yet been updated. Until those entries are finalized, follow the dates in the posted PDF syllabus.

If an assignment date still appears inconsistent after the course has been underway for a while, contact the instructor for clarification.

# Course Roadmap

Physics 212 covers several topics that may initially appear separate but are connected through common physical and mathematical principles.

We will begin with **rotational motion**.

First, we will develop rotational kinematics by comparing it directly with translational kinematics. Rotational motion is not an entirely new form of mechanics; it is translational motion expressed using variables that are more convenient for circular and rotational systems.

We will then move from kinematics to dynamics.

In translational mechanics, Newton’s second law is

$$
\sum \vec{F}=m\vec{a}.
$$

For rotation about a fixed axis, the analogous relationship is

$$
\sum \tau=I\alpha,
$$

where $I$ is the moment of inertia and $\alpha$ is the angular acceleration.

The momentum relationships also have rotational analogues. In translational motion,

$$
\sum \vec{F}_{\mathrm{ext}}
=
\frac{d\vec{p}}{dt}.
$$

In rotational motion,

$$
\sum \vec{\tau}_{\mathrm{ext}}
=
\frac{d\vec{L}}{dt},
$$

where $\vec{L}$ is angular momentum.

We will study:

- Rotational kinematics
- Torque and rotational dynamics
- Rotational kinetic energy
- Angular momentum
- Conservation of angular momentum
- Oscillations
- Mechanical and electromagnetic waves
- Wave optics
- Geometrical, or ray, optics

Oscillations are closely related mathematically to rotational motion. Even when nothing appears to be rotating, sinusoidal oscillations can be understood through the projection of circular motion onto an axis.

# How to Approach Physics Problems

A physics course should not be treated simply as an applied mathematics course.

The mathematics is usually the final stage of a solution. Before performing algebra or calculus, we must first understand the physical system.

A productive problem-solving sequence is:

1. Identify the system.
2. Determine the physical assumptions.
3. Construct useful visual representations.
4. Write the relevant general physical principles.
5. Specialize those principles to the particular system.
6. Solve the resulting equations symbolically.
7. Substitute numerical values and evaluate the result.
8. Check the units and physical meaning of the answer.

## Identifying the System

The **system** is the object or collection of objects being analyzed.

Before writing equations, determine exactly what is included in the system and what interactions occur between the system and its surroundings.

## Making Assumptions

Every physical model contains assumptions.

For example, when calculating the flight of a golf ball, we might assume:

- The ball can be treated as a point particle.
- Air resistance is negligible.
- Earth’s gravitational acceleration is uniform.
- Earth’s curvature can be ignored over the distance traveled.

Including every microscopic physical interaction would make most problems impossible to solve exactly. The purpose of an assumption is to simplify the model while retaining the behavior most relevant to the question.

The important skill is not merely making assumptions, but understanding how each assumption affects the equations and the accuracy of the model.

## Constructing Visual Representations

Useful representations may include:

- Physical diagrams
- Coordinate systems
- Free-body diagrams
- Motion diagrams
- Graphs
- Energy bar charts
- Vector diagrams

These are not decorations added after the solution. They are tools used to construct the equations.

## Beginning with General Equations

Start with a general physical principle before substituting values.

For example, begin with

$$
v(t)=v_0+\int_{t_0}^{t}a(t')\,dt'
$$

rather than immediately inserting numerical values.

Then determine how the general relationship simplifies for the particular system.

## Focusing on the Setup

Students often spend most of their study time repeating algebra. For many students, however, algebra is not the primary source of difficulty.

The more important skill is learning how to begin:

- What is the system?
- What should the diagram contain?
- Which physical principle applies?
- Which assumptions are appropriate?
- How should the general equation be specialized?

Practicing only the calculation is similar to practicing lifting with poor technique. A light object may be manageable even with an incorrect method, but the weaknesses become serious when the problem becomes more complicated.

Use correct structure even for simple problems. That structure will remain useful when the mathematics and physics become more demanding.

## Equation Sheets

You will prepare your own handwritten equation sheets for quizzes.

An equation sheet may include:

- Equations
- Diagrams
- Definitions
- Sign conventions
- Notes to yourself
- Reminders about problem-solving procedures

The goal is not to memorize a large collection of formulas. The goal is to understand the general principles well enough to identify which relationship applies and how it must be adapted to the system.

## Levels of Learning

Physics requires more than remembering information.

A useful progression is:

1. Remembering
2. Understanding
3. Applying
4. Analyzing
5. Evaluating
6. Creating or combining ideas into a new solution

The metacognitive question is:

> Why am I doing what I am doing?

A strong understanding of physics allows you to recognize that a new problem may be structurally similar to one you have seen before, even if the physical objects or wording are different.

# Review of Translational Kinematics

In translational motion, the fundamental variables are:

- Position $x$
- Velocity $v$
- Acceleration $a$

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

If vector notation is omitted, the equation may refer to a one-dimensional component or to a magnitude, depending on the context.

The derivative relationships can be reversed using integration.

Velocity may be obtained from acceleration:

$$
v(t)
=
v(t_0)
+
\int_{t_0}^{t}a(t')\,dt'.
$$

Position may be obtained from velocity:

$$
x(t)
=
x(t_0)
+
\int_{t_0}^{t}v(t')\,dt'.
$$

These equations are general. They remain valid whether or not acceleration is constant.

# Angular Position and Arc Length

Consider a point moving along a circular path of radius $r$.

Let:

- $\theta$ be the angular position
- $s$ be the arc length traveled

The relationship between arc length and angular displacement is

$$
\boxed{
s=r\theta
}.
$$

This equation assumes that $\theta$ is measured in radians.

One radian is the angle that subtends an arc whose length is equal to the radius of the circle.

A complete revolution corresponds to

$$
\boxed{
1\ \mathrm{rev}
=
360^\circ
=
2\pi\ \mathrm{rad}
}.
$$

Half a revolution corresponds to $\pi$ radians.

# Rotational Kinematics

The rotational analogues of position, velocity, and acceleration are:

- Angular position $\theta$
- Angular velocity $\omega$
- Angular acceleration $\alpha$

Angular velocity is the time derivative of angular position:

$$
\boxed{
\omega(t)
=
\frac{d\theta}{dt}
}.
$$

Angular acceleration is the time derivative of angular velocity:

$$
\boxed{
\alpha(t)
=
\frac{d\omega}{dt}
=
\frac{d^2\theta}{dt^2}
}.
$$

The integral relationships are

$$
\boxed{
\omega(t)
=
\omega(t_0)
+
\int_{t_0}^{t}\alpha(t')\,dt'
}
$$

and

$$
\boxed{
\theta(t)
=
\theta(t_0)
+
\int_{t_0}^{t}\omega(t')\,dt'
}.
$$

These relationships have exactly the same mathematical structure as their translational counterparts:

$$
x
\longleftrightarrow
\theta,
$$

$$
v
\longleftrightarrow
\omega,
$$

and

$$
a
\longleftrightarrow
\alpha.
$$

# Relating Linear and Angular Motion

Starting with

$$
s=r\theta,
$$

take the time derivative:

$$
\frac{ds}{dt}
=
r\frac{d\theta}{dt}
$$

for a constant radius.

Because

$$
v_t=\frac{ds}{dt}
$$

and

$$
\omega=\frac{d\theta}{dt},
$$

the tangential speed is

$$
\boxed{
v_t=r\omega
}.
$$

Taking another time derivative gives

$$
\frac{dv_t}{dt}
=
r\frac{d\omega}{dt}.
$$

Therefore, the tangential acceleration is

$$
\boxed{
a_t=r\alpha
}.
$$

These relationships apply when the radius is constant.

It is important to distinguish the quantities:

- $\omega$ is angular velocity.
- $\alpha$ is angular acceleration.
- $v_t$ is tangential velocity.
- $a_t$ is tangential acceleration.

Angular acceleration and tangential acceleration are related, but they are not the same quantity and do not have the same units.

# Units of Angular Quantities

Ordinary linear velocity may be measured in units such as

$$
\mathrm{m/s},
$$

$$
\mathrm{cm/s},
$$

or

$$
\mathrm{mi/h}.
$$

Angular velocity may be measured in

$$
\mathrm{rad/s},
$$

$$
\mathrm{deg/s},
$$

or

$$
\mathrm{rev/s}.
$$

Angular acceleration is commonly measured in

$$
\mathrm{rad/s^2}.
$$

Radians are dimensionless in the formal SI dimensional system, but retaining “rad” in the written units is often helpful because it identifies the quantity as angular.

# Constant-Acceleration Kinematics

When linear acceleration is constant, the translational kinematic equations are

$$
\boxed{
x_f
=
x_0
+
v_0\Delta t
+
\frac{1}{2}a(\Delta t)^2
},
$$

$$
\boxed{
v_f
=
v_0+a\Delta t
},
$$

and

$$
\boxed{
v_f^2
=
v_0^2
+
2a(x_f-x_0)
}.
$$

The third equation does not contain additional physical information. It is obtained by eliminating time between the first two equations.

When angular acceleration is constant, the corresponding rotational equations are

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

The structures are directly analogous:

| Translational quantity | Rotational quantity |
|---|---|
| $x$ | $\theta$ |
| $v$ | $\omega$ |
| $a$ | $\alpha$ |

These constant-acceleration equations may be used only when the corresponding acceleration is constant.

# Sign Conventions

Before assigning signs to velocity or acceleration, choose a positive direction.

For one-dimensional translational motion, suppose the positive $x$-direction points to the right.

Then:

- Motion to the right has $v>0$.
- Motion to the left has $v<0$.

The sign of acceleration depends on both the direction of motion and whether the object is speeding up or slowing down.

| Velocity | Behavior | Acceleration |
|---|---|---|
| $v>0$ | Speeding up | $a>0$ |
| $v>0$ | Slowing down | $a<0$ |
| $v<0$ | Speeding up | $a<0$ |
| $v<0$ | Slowing down | $a>0$ |

Acceleration has the same sign as velocity when the object is speeding up and the opposite sign when it is slowing down.

The same logic applies to angular motion after a positive angular direction has been defined. We will later describe angular directions more precisely using the right-hand rule.

# Vector Components

Acceleration is a vector.

In two-dimensional Cartesian coordinates, it may be written as

$$
\boxed{
\vec{a}
=
a_x\hat{x}
+
a_y\hat{y}
}.
$$

Its magnitude is

$$
\boxed{
a
=
\sqrt{a_x^2+a_y^2}
}.
$$

The same vector may be resolved using a coordinate system adapted to circular motion.

Let:

- $\hat{r}$ be the radial unit vector
- $\hat{t}$ be the tangential unit vector

Then

$$
\boxed{
\vec{a}
=
a_r\hat{r}
+
a_t\hat{t}
}.
$$

Because the radial and tangential directions are perpendicular,

$$
\boxed{
a
=
\sqrt{a_r^2+a_t^2}
}.
$$

In this course, we will often choose the positive radial direction to point inward, toward the center of the circular path.

The radial–tangential coordinate system rotates with the moving particle:

- The radial axis remains aligned with the radius.
- The tangential axis remains tangent to the path.

This makes it especially convenient for circular-motion problems.

## Distinguishing Three Types of Acceleration

Three acceleration quantities appear in rotational problems:

### Radial Acceleration

$a_r$ is a linear acceleration directed along the radius. In circular motion, it is associated with the changing direction of the velocity.

Its units are

$$
\mathrm{m/s^2}.
$$

### Tangential Acceleration

$a_t$ is a linear acceleration directed tangent to the circular path. It describes the change in the object’s speed.

Its units are

$$
\mathrm{m/s^2}.
$$

### Angular Acceleration

$\alpha$ describes the rate at which angular velocity changes:

$$
\alpha=\frac{d\omega}{dt}.
$$

Its units are

$$
\mathrm{rad/s^2}.
$$

Tangential and angular acceleration are related by

$$
a_t=r\alpha,
$$

but they are distinct physical quantities.

# Worked Example: A Disk with Time-Dependent Angular Velocity

Consider a disk whose angular velocity is

$$
\omega(t)=a-bt^2,
$$

where

$$
a=18\ \mathrm{s^{-1}}
$$

and

$$
b=0.50\ \mathrm{s^{-3}}.
$$

Equivalently, when the angular velocity is explicitly interpreted in radians per second, the units may be written as

$$
a=18\ \mathrm{rad/s}
$$

and

$$
b=0.50\ \mathrm{rad/s^3}.
$$

Here, $a$ and $b$ are constant coefficients. The symbol $a$ in this equation is not linear acceleration.

We want to determine:

1. The time at which the disk reverses its direction of rotation
2. The angular displacement before the reversal

## Determining Whether Angular Acceleration Is Constant

Differentiate the angular-velocity function:

$$
\alpha(t)
=
\frac{d\omega}{dt}.
$$

Therefore,

$$
\alpha(t)
=
\frac{d}{dt}
\left(
a-bt^2
\right),
$$

so

$$
\boxed{
\alpha(t)=-2bt
}.
$$

The angular acceleration depends on time. It is therefore not constant.

Consequently, the constant-angular-acceleration equations

$$
\omega_f=\omega_0+\alpha\Delta t
$$

and

$$
\theta_f
=
\theta_0
+
\omega_0\Delta t
+
\frac{1}{2}\alpha(\Delta t)^2
$$

cannot be used for this motion.

Instead, we must work directly with the given function.

## Time at Which the Disk Reverses Direction

A reversal occurs when the angular velocity passes through zero.

At the instant of reversal,

$$
\boxed{
\omega=0
}.
$$

Set the angular-velocity function equal to zero:

$$
0=a-bt^2.
$$

Rearranging,

$$
bt^2=a.
$$

Therefore,

$$
t^2=\frac{a}{b}.
$$

Taking the positive root because we are interested in a time after $t=0$,

$$
\boxed{
t_{\mathrm{rev}}
=
\sqrt{\frac{a}{b}}
}.
$$

Substituting the values,

$$
t_{\mathrm{rev}}
=
\sqrt{
\frac{
18\ \mathrm{s^{-1}}
}{
0.50\ \mathrm{s^{-3}}
}
}.
$$

The units inside the square root are

$$
\frac{\mathrm{s^{-1}}}{\mathrm{s^{-3}}}
=
\mathrm{s^2}.
$$

Therefore,

$$
t_{\mathrm{rev}}
=
\sqrt{
36\ \mathrm{s^2}
}.
$$

Thus,

$$
\boxed{
t_{\mathrm{rev}}=6.0\ \mathrm{s}
}.
$$

At $t=6.0\ \mathrm{s}$, the disk momentarily stops. For later times, $\omega(t)$ becomes negative, indicating rotation in the opposite direction.

The crucial physical translation is:

> “The disk reverses direction” means that its angular velocity passes through zero.

# Angular Displacement Before the Reversal

Angular velocity is the time derivative of angular position:

$$
\omega(t)=\frac{d\theta}{dt}.
$$

Therefore,

$$
d\theta=\omega(t)\,dt.
$$

The angular displacement from $t=0$ to the reversal time is

$$
\Delta\theta
=
\int_0^{t_{\mathrm{rev}}}
\omega(t)\,dt.
$$

Substitute

$$
\omega(t)=a-bt^2:
$$

$$
\Delta\theta
=
\int_0^{t_{\mathrm{rev}}}
\left(
a-bt^2
\right)
dt.
$$

Integrating,

$$
\Delta\theta
=
\left[
at-\frac{b}{3}t^3
\right]_0^{t_{\mathrm{rev}}}.
$$

Therefore,

$$
\boxed{
\Delta\theta
=
at_{\mathrm{rev}}
-
\frac{b}{3}t_{\mathrm{rev}}^3
}.
$$

Using

$$
t_{\mathrm{rev}}=\sqrt{\frac{a}{b}},
$$

the symbolic result may be written as

$$
\Delta\theta
=
a\sqrt{\frac{a}{b}}
-
\frac{b}{3}
\left(
\sqrt{\frac{a}{b}}
\right)^3.
$$

Because

$$
bt_{\mathrm{rev}}^2=a,
$$

we also have

$$
bt_{\mathrm{rev}}^3
=
at_{\mathrm{rev}}.
$$

The displacement therefore simplifies to

$$
\boxed{
\Delta\theta
=
\frac{2}{3}
a
\sqrt{\frac{a}{b}}
}.
$$

Substituting the numerical values directly,

$$
\Delta\theta
=
(18\ \mathrm{rad/s})(6.0\ \mathrm{s})
-
\frac{
0.50\ \mathrm{rad/s^3}
}{3}
(6.0\ \mathrm{s})^3.
$$

The first term is

$$
108\ \mathrm{rad},
$$

and the second term is

$$
36\ \mathrm{rad}.
$$

Therefore,

$$
\boxed{
\Delta\theta=72\ \mathrm{rad}
}.
$$

The disk rotates through $72$ radians before momentarily stopping and reversing direction.

# General Strategy for Motion Defined by a Function

When velocity or angular velocity is given explicitly as a function of time, use the following approach.

## 1. Translate the Physical Event into a Mathematical Condition

Examples include:

- A translational object reverses direction when $v=0$.
- A rotating object reverses direction when $\omega=0$.
- A position reaches an extremum when its velocity is zero.
- A velocity reaches an extremum when its acceleration is zero.

For the disk,

$$
\text{reversal}
\quad\Longrightarrow\quad
\omega(t)=0.
$$

## 2. Determine Whether the Acceleration Is Constant

Differentiate the velocity function.

For the disk,

$$
\alpha(t)=-2bt,
$$

which is not constant.

Therefore, constant-angular-acceleration equations do not apply.

## 3. Use the Given Function Directly

To find a particular time, solve the function for the required condition.

To find displacement, integrate velocity:

$$
\Delta\theta
=
\int\omega(t)\,dt.
$$

To find acceleration, differentiate velocity:

$$
\alpha(t)
=
\frac{d\omega}{dt}.
$$

## 4. Solve Symbolically First

Keep $a$, $b$, and $t$ as symbols until the requested quantity has been isolated.

The reversal time is

$$
t_{\mathrm{rev}}
=
\sqrt{\frac{a}{b}},
$$

and the angular displacement is

$$
\Delta\theta
=
\frac{2}{3}
a
\sqrt{\frac{a}{b}}.
$$

## 5. Check the Units

For the reversal time,

$$
\left[
\frac{a}{b}
\right]
=
\frac{\mathrm{s^{-1}}}{\mathrm{s^{-3}}}
=
\mathrm{s^2}.
$$

Taking the square root produces seconds.

For angular displacement,

$$
[a][t]
=
\mathrm{rad/s}\cdot\mathrm{s}
=
\mathrm{rad}.
$$

## 6. Substitute Numerical Values Last

After the symbolic result has been established and checked, insert the numerical values.

# Summary

Physics problem solving begins with understanding the system, assumptions, and physical principles. The algebra should come after the physical setup.

For translational motion,

$$
v(t)=\frac{dx}{dt}
$$

and

$$
a(t)=\frac{dv}{dt}.
$$

For rotational motion,

$$
\boxed{
\omega(t)=\frac{d\theta}{dt}
}
$$

and

$$
\boxed{
\alpha(t)=\frac{d\omega}{dt}
}.
$$

Arc length and angular displacement are related by

$$
\boxed{
s=r\theta
}.
$$

For a fixed radius,

$$
\boxed{
v_t=r\omega
}
$$

and

$$
\boxed{
a_t=r\alpha
}.
$$

The constant-angular-acceleration equations are

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

These equations apply only when $\alpha$ is constant.

Acceleration may be resolved into Cartesian components,

$$
\vec{a}
=
a_x\hat{x}
+
a_y\hat{y},
$$

or radial and tangential components,

$$
\vec{a}
=
a_r\hat{r}
+
a_t\hat{t}.
$$

The corresponding magnitudes are

$$
a
=
\sqrt{a_x^2+a_y^2}
$$

and

$$
a
=
\sqrt{a_r^2+a_t^2}.
$$

For the disk with

$$
\omega(t)=a-bt^2,
$$

the angular acceleration is

$$
\boxed{
\alpha(t)=-2bt
},
$$

so it is not constant.

The disk reverses direction when

$$
\omega=0.
$$

Therefore,

$$
\boxed{
t_{\mathrm{rev}}
=
\sqrt{\frac{a}{b}}
}.
$$

For

$$
a=18\ \mathrm{s^{-1}}
$$

and

$$
b=0.50\ \mathrm{s^{-3}},
$$

the reversal time is

$$
\boxed{
t_{\mathrm{rev}}=6.0\ \mathrm{s}
}.
$$

The angular displacement before reversal is

$$
\boxed{
\Delta\theta
=
\int_0^{t_{\mathrm{rev}}}
\omega(t)\,dt
}
$$

or

$$
\boxed{
\Delta\theta
=
at_{\mathrm{rev}}
-
\frac{b}{3}t_{\mathrm{rev}}^3
}.
$$

For the given values,

$$
\boxed{
\Delta\theta=72\ \mathrm{rad}
}.
$$
