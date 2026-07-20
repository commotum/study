# Connect Rolling Motion to Angular-Momentum Conservation

## Table of Contents

- [Prerequisites](#prerequisites)
- [Choose the Governing Idea](#choose-the-governing-idea)
- [Apply the No-Slip Constraint](#apply-the-no-slip-constraint)
- [Build the Rolling Energy Equation](#build-the-rolling-energy-equation)
- [Use an Object's Shape to Predict Its Motion](#use-an-objects-shape-to-predict-its-motion)
- [Write Angular Momentum About a Chosen Axis](#write-angular-momentum-about-a-chosen-axis)
- [Test Whether Angular Momentum Is Conserved](#test-whether-angular-momentum-is-conserved)
- [Handle a Sticking Rotational Collision](#handle-a-sticking-rotational-collision)
- [Keep Angular Momentum and Energy Separate](#keep-angular-momentum-and-energy-separate)
- [Summary](#summary)

## Prerequisites

You should be comfortable with:

- translational kinetic energy, $K_{\mathrm{trans}}=\frac12Mv^2$,
- rotational kinetic energy, $K_{\mathrm{rot}}=\frac12I\omega^2$,
- gravitational potential energy, $U_g=Mgh$,
- moment of inertia about a specified axis,
- torque and the right-hand rule, and
- conservation laws as statements about a chosen system.

## Choose the Governing Idea

The central decision is not “Which formula contains the requested variable?” It is “What interaction controls the change?”

- For an object **rolling without slipping** through a height change, connect translation and rotation with the rolling constraint, then usually use energy.
- For a system that changes its rotation during a short interaction, choose an axis and ask whether the **external torque about that axis** is zero. If it is, use angular-momentum conservation.
- In a sticking collision, angular momentum may be conserved even though mechanical energy is not.

The two topics meet because the same object can carry both translational and rotational motion, but their conservation conditions are different.

**Recognition cue:** “Rolls without slipping” supplies a kinematic constraint. “Frictionless axle,” “negligible external torque,” or “sticks” suggests an angular-momentum test—but conservation is allowed only after the system and axis are named.

### Worked Example

A solid sphere rolls from rest down a fixed ramp without slipping. Which chain of ideas most directly determines its speed at the bottom?

1. The fixed ramp does no work at its stationary contact point when rolling is ideal.
2. Gravity changes potential energy into both translational and rotational kinetic energy.
3. The rolling constraint $v_{\mathrm{cm}}=\omega R$ connects those two kinetic-energy terms.

So the useful equation is

$$
Mgh=\frac12Mv^2+\frac12I\left(\frac{v}{R}\right)^2.
$$

This is an energy problem with a kinematic constraint, not an angular-momentum-conservation problem.

```quiz
type: radio
id: rolling-angular-q1
shuffle: true
content: |-
  A wheel rolls without slipping from rest down a stationary ramp. What is the most useful starting framework for finding its final speed?
options:
- id: rolling-angular-q1-a
  content: |-
    Conservation of mechanical energy together with $v_{\mathrm{cm}}=\omega R$
  correct: true
  feedback: |-
    Gravity trades potential energy for both kinds of kinetic energy, and the no-slip condition connects them.
- id: rolling-angular-q1-b
  content: |-
    Conservation of angular momentum about the wheel's center
  feedback: |-
    The ramp and Earth exert external forces, so momentum conservation is not the natural starting point. Rolling also includes rotational kinetic energy.
- id: rolling-angular-q1-c
  content: |-
    Translational kinetic energy only
  feedback: |-
    The ramp and Earth exert external forces, so momentum conservation is not the natural starting point. Rolling also includes rotational kinetic energy.
- id: rolling-angular-q1-d
  content: |-
    Linear momentum conservation for the wheel alone
  feedback: |-
    The ramp and Earth exert external forces, so momentum conservation is not the natural starting point. Rolling also includes rotational kinetic energy.
```

## Apply the No-Slip Constraint

For pure rolling on a stationary surface,

$$
v_{\mathrm{cm}}=\omega R,
\qquad
a_{\mathrm{cm}}=\alpha R.
$$

These are constraints, not extra force laws. They state that the distance traveled by the center equals the arc length rotated: $x=R\theta$. Differentiating once gives the velocity relation; differentiating again gives the tangential-acceleration relation.

Use the object's **rolling radius**: the distance from its rotation axis to the point of contact. Do not automatically substitute some other visible radius from a spool or stepped wheel.

**Boundary case:** If the contact point slips, the no-slip equations are invalid. Friction may then change the mechanical energy as well as the relation between translation and rotation.

### Worked Example

A wheel of radius $0.30\,\mathrm{m}$ rolls without slipping at $v_{\mathrm{cm}}=2.4\,\mathrm{m/s}$. Its angular speed is

$$
\omega=\frac{v_{\mathrm{cm}}}{R}
=\frac{2.4}{0.30}
=8.0\,\mathrm{rad/s}.
$$

If its center accelerates at $1.5\,\mathrm{m/s^2}$, then

$$
\alpha=\frac{a_{\mathrm{cm}}}{R}
=5.0\,\mathrm{rad/s^2}.
$$

```quiz
type: radio
id: rolling-angular-q2
shuffle: true
content: |-
  A wheel of radius $R$ rolls without slipping with center-of-mass speed $v$. Its angular speed is
options:
- id: rolling-angular-q2-a
  content: |-
    $vR$
  feedback: |-
    Start from $v=\omega R$ and isolate $\omega$. The result must also have units of inverse seconds.
- id: rolling-angular-q2-b
  content: |-
    $v/R$
  correct: true
  feedback: |-
    Pure rolling requires $v=\omega R$, so $\omega=v/R$.
- id: rolling-angular-q2-c
  content: |-
    $R/v$
  feedback: |-
    Start from $v=\omega R$ and isolate $\omega$. The result must also have units of inverse seconds.
- id: rolling-angular-q2-d
  content: |-
    $v/(2R)$
  feedback: |-
    Start from $v=\omega R$ and isolate $\omega$. The result must also have units of inverse seconds.
```

## Build the Rolling Energy Equation

A rolling rigid body has two kinetic-energy terms:

$$
K=\frac12Mv_{\mathrm{cm}}^2+\frac12I_{\mathrm{cm}}\omega^2.
$$

When it rolls without slipping, replace $\omega$ with $v_{\mathrm{cm}}/R$:

$$
K=\frac12Mv^2\left(1+\frac{I}{MR^2}\right).
$$

Starting from rest and dropping through a vertical height $h$, energy conservation gives

$$
Mgh=\frac12Mv^2\left(1+\frac{I}{MR^2}\right),
$$

so

$$
v=\sqrt{\frac{2gh}{1+I/(MR^2)}}.
$$

The ratio $I/(MR^2)$ is the object's rotational “cost.” A larger value sends more of the available energy into rotation and leaves less for center-of-mass speed.

### Worked Example

For a hollow sphere, $I=\frac23MR^2$. After descending through height $h$,

$$
v=\sqrt{\frac{2gh}{1+2/3}}
=\sqrt{\frac65gh}.
$$

The mass and radius cancel because the shape factor $I/(MR^2)=2/3$ is fixed.

```quiz
type: radio
id: rolling-angular-q3
shuffle: true
content: |-
  A hollow sphere with $I=\frac23MR^2$ rolls without slipping from rest through height $h$. What is its final speed?
options:
- id: rolling-angular-q3-a
  content: |-
    $\sqrt{2gh}$
  feedback: |-
    Include both translational and rotational kinetic energy. The rotational term makes the speed smaller than $\sqrt{2gh}$.
- id: rolling-angular-q3-b
  content: |-
    $\sqrt{\frac65gh}$
  correct: true
  feedback: |-
    Substitute $I/(MR^2)=2/3$ into the rolling-energy result.
- id: rolling-angular-q3-c
  content: |-
    $\sqrt{\frac23gh}$
  feedback: |-
    Include both translational and rotational kinetic energy. The rotational term makes the speed smaller than $\sqrt{2gh}$.
- id: rolling-angular-q3-d
  content: |-
    $\sqrt{\frac53gh}$
  feedback: |-
    Include both translational and rotational kinetic energy. The rotational term makes the speed smaller than $\sqrt{2gh}$.
```

## Use an Object's Shape to Predict Its Motion

For rolling without slipping down an incline at angle $\theta$,

$$
a_{\mathrm{cm}}=\frac{g\sin\theta}{1+I/(MR^2)}.
$$

At fixed $M$ and $R$, the object with the smaller moment of inertia accelerates faster. This creates a quick ranking rule:

$$
\text{smaller }\frac{I}{MR^2}
\quad\Longrightarrow\quad
\text{larger }a\text{ and }v.
$$

For common shapes,

$$
\frac{I}{MR^2}=\frac25\text{ (solid sphere)},
\qquad
\frac12\text{ (solid disk)},
\qquad
\frac23\text{ (spherical shell)},
\qquad
1\text{ (hoop)}.
$$

### Worked Example

A hoop and a solid disk start from rest at the same height on identical ramps. Since

$$
\left(\frac{I}{MR^2}\right)_{\mathrm{disk}}=\frac12
<
1=\left(\frac{I}{MR^2}\right)_{\mathrm{hoop}},
$$

the disk has the larger acceleration and reaches the bottom first. No numerical calculation is needed.

```quiz
type: radio
id: rolling-angular-q4
shuffle: true
content: |-
  A hoop and a solid sphere have the same mass and radius and roll without slipping down identical ramps. Which reaches the bottom first?
options:
- id: rolling-angular-q4-a
  content: |-
    The hoop, because more of its mass is far from the axis
  feedback: |-
    Mass cancels, but shape does not. Compare the dimensionless ratios $I/(MR^2)$.
- id: rolling-angular-q4-b
  content: |-
    The solid sphere, because its $I/(MR^2)$ is smaller
  correct: true
  feedback: |-
    A smaller rotational shape factor produces a larger rolling acceleration.
- id: rolling-angular-q4-c
  content: |-
    They tie, because gravitational acceleration is independent of mass
  feedback: |-
    Mass cancels, but shape does not. Compare the dimensionless ratios $I/(MR^2)$.
- id: rolling-angular-q4-d
  content: |-
    The result depends on their common mass
  feedback: |-
    Mass cancels, but shape does not. Compare the dimensionless ratios $I/(MR^2)$.
```

## Write Angular Momentum About a Chosen Axis

Angular momentum always refers to an origin or axis.

For a particle,

$$
\vec L=\vec r\times\vec p=\vec r\times m\vec v,
\qquad
L=rmv\sin\phi.
$$

Equivalently, $L=mv\,r_\perp$, where $r_\perp$ is the perpendicular distance from the chosen origin to the particle's line of motion.

For a rigid object rotating about a fixed principal axis,

$$
L=I\omega.
$$

When a system contains both an incoming particle and a rotating body, its total angular momentum may contain both forms.

### Worked Example

A particle of mass $m$ travels horizontally at speed $v$ along a line a perpendicular distance $b$ above a fixed pivot. Just before an interaction,

$$
L_i=mvb.
$$

The distance $b$, not the particle's straight-line distance to the pivot, is the moment arm. The sign follows from $\vec r\times m\vec v$.

```quiz
type: radio
id: rolling-angular-q5
shuffle: true
content: |-
  A particle moves at speed $v$ along a straight line whose perpendicular distance from the chosen origin is $b$. What is the magnitude of its angular momentum about that origin?
options:
- id: rolling-angular-q5-a
  content: |-
    $mv/b$
  feedback: |-
    Use $L=rmv\sin\phi=mv r_\perp$, and check for units of $\mathrm{kg\,m^2/s}$.
- id: rolling-angular-q5-b
  content: |-
    $mvb$
  correct: true
  feedback: |-
    The perpendicular lever arm gives $L=mvb$.
- id: rolling-angular-q5-c
  content: |-
    $mv^2b$
  feedback: |-
    Use $L=rmv\sin\phi=mv r_\perp$, and check for units of $\mathrm{kg\,m^2/s}$.
- id: rolling-angular-q5-d
  content: |-
    $mb^2v$
  feedback: |-
    Use $L=rmv\sin\phi=mv r_\perp$, and check for units of $\mathrm{kg\,m^2/s}$.
```

## Test Whether Angular Momentum Is Conserved

The angular-momentum equation is

$$
\sum\vec\tau_{\mathrm{ext}}=\frac{d\vec L}{dt}.
$$

Therefore,

$$
\sum\vec\tau_{\mathrm{ext}}=0
\quad\Longrightarrow\quad
\vec L_i=\vec L_f.
$$

The test must be made:

1. for a clearly chosen system,
2. about a clearly chosen origin or axis, and
3. over the time interval of interest.

A force can be external yet exert zero torque about the selected axis. For example, a frictionless axle force passes through the axle, so its lever arm about that axle is zero.

### Worked Example

Two cups are attached at radius $R$ to a freely rotating horizontal platform. Rain falls vertically and collects in the cups. About the vertical axle, gravity and the axle force produce no torque in the horizontal rotation direction. The incoming rain has no initial angular momentum about the axle if it falls vertically with no tangential speed.

Thus,

$$
I_i\omega_i=I_f\omega_f.
$$

Since collected rain increases $I$, the angular speed decreases.

```quiz
type: radio
id: rolling-angular-q6
shuffle: true
content: |-
  A freely rotating platform collects material that arrives with zero angular momentum about its axle. External torque about the axle is negligible. What happens as the platform's moment of inertia increases?
options:
- id: rolling-angular-q6-a
  content: |-
    Its angular speed increases so rotational kinetic energy stays fixed
  feedback: |-
    The conserved quantity is angular momentum, not angular speed or rotational kinetic energy.
- id: rolling-angular-q6-b
  content: |-
    Its angular speed decreases so $I\omega$ stays fixed
  correct: true
  feedback: |-
    With negligible external torque, $L=I\omega$ is conserved; increasing $I$ lowers $\omega$.
- id: rolling-angular-q6-c
  content: |-
    Its angular speed stays fixed because the axle force is external
  feedback: |-
    The conserved quantity is angular momentum, not angular speed or rotational kinetic energy.
- id: rolling-angular-q6-d
  content: |-
    Its angular momentum decreases in proportion to $I$
  feedback: |-
    The conserved quantity is angular momentum, not angular speed or rotational kinetic energy.
```

## Handle a Sticking Rotational Collision

For a short collision with negligible external torque about a pivot, write the total angular momentum immediately before and immediately after:

$$
L_i=L_f.
$$

If a particle sticks to the rim of an initially stationary rotating body,

$$
(\vec r\times m\vec v)_i
=
\left(I_{\mathrm{body}}+mR^2\right)\omega_f.
$$

The embedded particle becomes part of the final moment of inertia. Its contribution is $mR^2$ when it sticks a distance $R$ from the axis.

### Worked Example

A bullet of mass $m$ moves tangentially at speed $v$, strikes the rim of a stationary solid cylinder of mass $M$ and radius $R$, and sticks. About the axle,

$$
mRv
=
\left(\frac12MR^2+mR^2\right)\omega_f.
$$

Therefore,

$$
\omega_f
=
\frac{mv}{R\left(m+M/2\right)}.
$$

Choosing the axle is strategic: the axle's impulsive force has zero torque about that point.

```quiz
type: radio
id: rolling-angular-q7
shuffle: true
content: |-
  A mass $m$ moving tangentially at speed $v$ sticks to the rim of a stationary disk with moment of inertia $I$. What equation gives the final angular speed about the axle?
options:
- id: rolling-angular-q7-a
  content: |-
    $mv=(I+mR^2)\omega_f$
  feedback: |-
    Conserve angular momentum about the axle and include the stuck mass in the final moment of inertia.
- id: rolling-angular-q7-b
  content: |-
    $mRv=(I+mR^2)\omega_f$
  correct: true
  feedback: |-
    The incoming particle contributes $mRv$, and after sticking it contributes $mR^2$ to the final inertia.
- id: rolling-angular-q7-c
  content: |-
    $\frac12mv^2=\frac12(I+mR^2)\omega_f^2$
  feedback: |-
    Conserve angular momentum about the axle and include the stuck mass in the final moment of inertia.
- id: rolling-angular-q7-d
  content: |-
    $mRv=I\omega_f$
  feedback: |-
    Conserve angular momentum about the axle and include the stuck mass in the final moment of inertia.
```

## Keep Angular Momentum and Energy Separate

Angular momentum and mechanical energy answer different questions.

- **Angular momentum is conserved** when the net external torque about the chosen axis is zero.
- **Mechanical energy is conserved** only when no process converts mechanical energy into thermal energy, deformation, sound, or other internal forms.

A perfectly inelastic rotational collision can satisfy $L_i=L_f$ while having $K_f<K_i$.

### Worked Example

For the bullet-and-cylinder collision above,

$$
K_i=\frac12mv^2,
\qquad
K_f=\frac12\left(\frac12MR^2+mR^2\right)\omega_f^2.
$$

Substituting the angular-momentum result for $\omega_f$ gives a final kinetic energy smaller than $K_i$. The missing mechanical energy became internal energy during embedding. That loss does not contradict angular-momentum conservation.

```quiz
type: radio
id: rolling-angular-q8
shuffle: true
content: |-
  A lump of clay sticks to the rim of a freely rotating disk during a brief collision. External torque about the axle is negligible. Which statement is correct?
options:
- id: rolling-angular-q8-a
  content: |-
    Both angular momentum and mechanical energy must be conserved
  feedback: |-
    Conservation conditions are separate. Sticking is inelastic, but deformation does not prevent angular-momentum conservation.
- id: rolling-angular-q8-b
  content: |-
    Angular momentum is conserved, but mechanical energy generally is not
  correct: true
  feedback: |-
    Negligible external torque conserves angular momentum, while sticking dissipates mechanical energy.
- id: rolling-angular-q8-c
  content: |-
    Mechanical energy is conserved, but angular momentum is not
  feedback: |-
    Conservation conditions are separate. Sticking is inelastic, but deformation does not prevent angular-momentum conservation.
- id: rolling-angular-q8-d
  content: |-
    Neither can be analyzed because the clay deforms
  feedback: |-
    Conservation conditions are separate. Sticking is inelastic, but deformation does not prevent angular-momentum conservation.
```

## Summary

Use this decision process:

1. Identify the system and choose the axis.
2. If the object rolls without slipping, impose $v_{\mathrm{cm}}=\omega R$ and $a_{\mathrm{cm}}=\alpha R$.
3. For a rolling height change, include both $\frac12Mv^2$ and $\frac12I\omega^2$ in energy.
4. Use $I/(MR^2)$ to compare the rolling speeds and accelerations of different shapes.
5. Write particle angular momentum as $\vec r\times m\vec v$ and rigid-body angular momentum as $I\omega$.
6. Conserve angular momentum only after verifying that the net external torque about the chosen axis is zero.
7. In a sticking collision, include the attached mass in the final moment of inertia and do not conserve mechanical energy.
