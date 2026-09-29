## Table of Contents

- [Problem-solving workflow](#universal-workflow)
- [How the vault and source files fit together](#vault-structure)
- [What the past three tests reveal](#past-test-comparison)
- [Module 1 — Angular and circular motion](#module-1)
  - [Angular units, calculus, and constant acceleration](#m1-angular-kinematics)
  - [Linear–angular conversion and alignment](#m1-linear-angular)
  - [Circular-motion vectors and force equations](#m1-circular-forces)
  - [Curves, banks, cones, contact, and loops](#m1-special-cases)
- [Module 2 — Center of mass and rotational mechanics](#module-2)
  - [Center of mass](#m2-center-of-mass)
  - [Moment of inertia, torque, and equilibrium](#m2-inertia-torque)
  - [Pulleys, rolling, and angular momentum](#m2-dynamics-conservation)
- [Module 3 — Gravitation and orbits](#module-3)
  - [Force, field, potential, and energy](#m3-force-energy)
  - [Circular and elliptical orbits](#m3-orbits)
  - [Binary systems and many-body synthesis](#m3-binary)
- [Module 4 — Oscillations](#module-4)
  - [SHM equations, graphs, phase, and energy](#m4-shm)
  - [Spring collisions and changing systems](#m4-collisions)
  - [Simple and physical pendula](#m4-pendula)
- [Module 5 — Traveling waves, sound, and interference](#module-5)
  - [Traveling waves and string speed](#m5-traveling-waves)
  - [Refraction, intensity, and decibels](#m5-refraction-intensity)
  - [Doppler effect](#m5-doppler)
  - [Superposition and standing waves](#m5-standing-waves)
  - [Two-source interference](#m5-interference)
- [Module 6 — Wave optics](#module-6)
  - [Double-slit interference](#m6-double-slit)
  - [Diffraction gratings](#m6-grating)
  - [Single-slit diffraction](#m6-single-slit)
- [Multi-step written-response chains](#written-chains)
- [Final error checklist](#final-checklist)

<a id="how-to-use"></a>
<a id="universal-workflow"></a>
## Problem-Solving Workflow

For each problem:

1. **Identify the problem family.** Use the wording and diagram to name the main topic: circular motion, torque, energy, SHM, Doppler, interference, and so on.
2. **Sketch the physical situation.** Add a second diagram when the problem has separate moments in time or separate subsystems.
3. **Name the unknown and givens with units.** Convert cm, mm, $\mu$m, nm, rpm, and degrees before substitution.
4. **Choose axes or a pivot deliberately.** For circular motion, make inward radial positive. For torque, choose a pivot that eliminates unknown forces.
5. **Choose the first framework.**

| Cue | First framework |
|---|---|
| position/velocity/acceleration as functions of time | derivatives, integrals, or kinematics |
| forces and acceleration | $\sum \vec F=m\vec a$ |
| rotation about a fixed axis | $\sum\tau=I\alpha$ |
| balance, support, tipping | $\sum\vec F=0$ and $\sum\tau=0$ |
| start/end speeds or heights with no requested time | energy |
| sticking or shape change with negligible external torque | momentum or angular momentum |
| orbit period/speed/energy | gravity plus circular motion or Kepler |
| oscillation timing/phase | SHM model |
| wavelength/frequency/medium | $v=f\lambda$ plus the medium relation |
| fringe or node geometry | path difference plus boundary conditions |

6. **Write the relevant equations before calculating.** Write only equations justified by the setup, and arrange multi-step problems as an equation chain. Identify which result from one framework becomes the input to the next.
7. **Solve algebraically before numbers.** If an unprovided variable remains, return to the framework table and add the equation needed to determine it.
8. **Check sign, units, limits, and scale.** Ask whether the direction is physically sensible and what happens when friction, angle, slit width, mass, radius, or distance approaches a simple limit.

When studying, use the variants and traps to test the same move after changing one feature: direction, angle convention, pivot, boundary condition, source/observer role, bright/dark order, or requested unknown.

Q1–Q3 repeatedly place a lecture or homework move in a new physical setup. Several questions also require one equation to supply an input for the next, so study the whole equation chain rather than only its last line.

Useful constants when not otherwise specified:

$$
g\approx9.80\ \mathrm{m/s^2},\qquad
G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2},
$$

$$
c=3.00\times10^8\ \mathrm{m/s},\qquad
v_{\rm sound}\approx343\ \mathrm{m/s},\qquad
I_0=10^{-12}\ \mathrm{W/m^2}.
$$

---

<a id="module-1"></a>
# Module 1 — Angular and Circular Motion

<a id="m1-angular-kinematics"></a>
## 1. Angular Units, Calculus, Graphs, and Constant Acceleration

### Family 1A: Revolutions, radians, period, and frequency

**Recognition cues:** rpm, number of turns, period, frequency, radians.

$$
1\ \mathrm{rev}=2\pi\ \mathrm{rad},\qquad
f=\frac1T,\qquad
\omega=2\pi f=\frac{2\pi}{T},\qquad
N=\frac{\Delta\theta}{2\pi}.
$$

**Walkthrough**

1. Convert time units first; rpm becomes rev/s before rad/s.
2. Convert turns to radians when using angular kinematics.
3. Use $\omega=2\pi f$ or $2\pi/T$.
4. If the answer is revolutions, divide the final angle by $2\pi$.

**Variants:** period from angular speed; rpm-to-rad/s; turns completed in a time interval; stopping angle expressed in revolutions.

### Family 1B: Derivative/integral chain and reversal

**Recognition cues:** $\theta(t)$, $\omega(t)$, $\alpha(t)$, graph matching, coefficient units, “when does it reverse?”

$$
\omega=\frac{d\theta}{dt},\qquad
\alpha=\frac{d\omega}{dt},\qquad
\Delta\theta=\int\omega\,dt,\qquad
\Delta\omega=\int\alpha\,dt.
$$

**Walkthrough**

1. Identify whether the given function is position, velocity, or acceleration.
2. Differentiate down the chain or integrate up the chain, preserving initial conditions.
3. For reversal, solve $\omega(t)=0$ and retain the physically relevant time.
4. On graphs, $\omega$ is the slope of $\theta(t)$ and $\alpha$ describes the change in that slope.
5. Every term being added must have the same dimensions; use this to infer coefficient units.

For $\omega=a-bt^2$,

$$
t_{\rm rev}=\sqrt{\frac ab},\qquad
\Delta\theta=\int_0^{t_{\rm rev}}(a-bt^2)\,dt.
$$

**Variants:** piecewise graph area; double integration of $\alpha(t)$; positive and negative roots; angle traveled versus net angular displacement.

### Family 1C: Constant angular acceleration

$$
\omega_f=\omega_0+\alpha t,
$$

$$
\Delta\theta=\omega_0t+\frac12\alpha t^2,
$$

$$
\omega_f^2=\omega_0^2+2\alpha\Delta\theta.
$$

**Walkthrough**

1. Declare a positive rotational direction.
2. Give $\omega$ and $\alpha$ signed values.
3. Inventory the known variables and choose the equation omitting the unnecessary unknown.
4. For “comes to rest,” set $\omega_f=0$.
5. Convert the final angle to turns only at the end.

**Variants:** braking disk; angular acceleration direction; rotations before stopping; solving a quadratic for the time to complete one revolution.

<a id="m1-linear-angular"></a>
## 2. Linear–Angular Conversion and Alignment

### Family 2A: Arc length, tangential speed, and tangential acceleration

$$
s=r\theta,\qquad v=r\omega,\qquad a_t=r\alpha.
$$

For a spool with time-dependent rope speed:

1. Find the unwound length:
   $$s=\int_{t_i}^{t_f}v(t)\,dt.$$
2. Use no slip: $s=r\theta$.
3. Convert to revolutions:
   $$N=\frac{s}{2\pi r}.$$

For the Quiz 1 form $v(t)=At+Bt^2$,

$$
N=\frac{\frac12At^2+\frac13Bt^3}{2\pi r}.
$$

Mass is a distractor because the problem is kinematics unless forces or energy are explicitly introduced.

**Variants:** belt drive; rope wound or unwound; a different polynomial speed; solve for time or radius instead of turns.

### Family 2B: Rotating-disk alignment

Equate the travel time of one object to the rotation time required for the opening/mark to align:

$$
\frac{D}{v}=\frac{\Delta\theta+2\pi n}{\omega},
$$

so

$$
v=\frac{D\omega}{\Delta\theta+2\pi n}.
$$

For the first alignment, $n=0$. With $\omega=2\pi/T$,

$$
v=\frac{2\pi D}{T\Delta\theta}.
$$

**Variants:** second/third possible alignment ($n=1,2$); solve for disk period; offset angles measured the opposite way.

<a id="m1-circular-forces"></a>
## 3. Circular-Motion Vectors and Force Equations

### Family 3A: Uniform and nonuniform circular vectors

Always true for circular motion:

- $\vec v$ is tangent to the path.
- $a_r=v^2/r=r\omega^2$ points inward.
- $a_t=dv/dt=r\alpha$ is tangent.
- Speeding up: $\vec a_t$ points with $\vec v$.
- Slowing down: $\vec a_t$ points opposite $\vec v$.

$$
|\vec a|=\sqrt{a_r^2+a_t^2}.
$$

**Arrow-question walkthrough**

1. Draw tangent velocity from the direction of travel.
2. Draw inward radial acceleration.
3. Add the correct tangential component from speeding/slowing.
4. Vector-add. The net force points with the total acceleration.

**Variants:** clockwise versus counterclockwise; fixed-speed radius ranking; fixed-radius speed ranking; acceleration or force direction at different clock positions.

### Family 3B: Circular-motion FBD

$$
\sum F_r=m\frac{v^2}{r}=m\omega^2r,
\qquad
\sum F_t=ma_t.
$$

**Walkthrough**

1. Draw only real interactions: gravity, normal, tension, friction, applied force.
2. Never add a separate “centripetal force.”
3. Choose $+r$ inward at the object's current position.
4. Resolve every real force into signed radial and tangential components.
5. Write separate equations in the two directions.
6. Use $a_r$ for $v$ or $\omega$; combine $a_r$ and $a_t$ only if total acceleration is requested.

### Family 3C: Vertical circle at a general angle

The exact sine/cosine assignment depends on where $\theta$ is measured. Build components from the picture. In the Quiz 1 convention,

$$
T-mg\sin\theta=ma_r,
\qquad
-mg\cos\theta=ma_t.
$$

Therefore,

$$
a_r=\frac{T}{m}-g\sin\theta,
\qquad
a_t=-g\cos\theta,
$$

$$
|\vec a|=
\sqrt{\left(\frac{T}{m}-g\sin\theta\right)^2+
\left(g\cos\theta\right)^2},
\qquad
\omega=\sqrt{\frac{a_r}{L}}.
$$

**Release variant**

1. Find $v^2=ra_r$ from the radial equation.
2. At release, velocity is tangent—not radial.
3. Resolve the tangent velocity to obtain $v_y$.
4. Use
   $$\Delta y_{\max}=\frac{v_y^2}{2g}.$$

### Family 3D: Top/bottom apparent weight

At the bottom of a dip, inward is upward:

$$
N-mg=m\frac{v^2}{r}
\quad\Rightarrow\quad
N=m\left(g+\frac{v^2}{r}\right).
$$

At the top, the sign depends on whether the contact force points inward or outward. For a Ferris-wheel seat whose normal is outward,

$$
mg-N=m\frac{v^2}{r}
\quad\Rightarrow\quad
N=m\left(g-\frac{v^2}{r}\right).
$$

**Walkthrough:** mark the center, identify the actual direction of each force, choose inward positive, and check whether $N$ should be greater or less than $mg$.

<a id="m1-special-cases"></a>
## 4. Curves, Banks, Cones, Contact, and Loops

### Family 4A: Flat curve or horizontal turntable

Static friction supplies the inward force:

$$
f_s=m\frac{v^2}{r}=m\omega^2r,
\qquad N=mg.
$$

At the threshold of slip only, $f_s=\mu_sN$, giving

$$
v_{\max}=\sqrt{\mu_sgr},
\qquad
\omega_{\max}=\sqrt{\frac{\mu_sg}{r}},
\qquad
T_{\min}=2\pi\sqrt{\frac{r}{\mu_sg}}.
$$

**Trap:** $f_s$ is not automatically $\mu_sN$; equality holds only at impending slip.

### Family 4B: Frictionless banked curve

$$
N\cos\theta=mg,
\qquad
N\sin\theta=m\frac{v^2}{r},
$$

so

$$
v=\sqrt{rg\tan\theta}.
$$

**Walkthrough:** vertical acceleration is zero; the horizontal component of $N$ supplies the radial acceleration; divide equations to eliminate $N$.

### Family 4C: Frictional banked curve

- Too fast: the tendency is uphill/outward, so friction acts downhill/inward.
- Too slow: the tendency is downhill/inward, so friction acts uphill/outward.

At the maximum-speed threshold,

$$
v_{\max}=\sqrt{
rg\frac{\sin\theta+\mu_s\cos\theta}
{\cos\theta-\mu_s\sin\theta}}.
$$

At the minimum-speed threshold,

$$
v_{\min}=\sqrt{
rg\frac{\sin\theta-\mu_s\cos\theta}
{\cos\theta+\mu_s\sin\theta}},
$$

when the numerator is positive.

**Walkthrough:** decide the impending direction first, draw friction opposite it, resolve vertical/radial components, then set $f_s=\mu_sN$ at the threshold.

If friction is initially assumed uphill, the component equations are

$$
N\cos\theta+f\sin\theta=mg,
\qquad
N\sin\theta-f\cos\theta=m\frac{v^2}{r},
$$

which combine to

$$
f=mg\sin\theta-\frac{mv^2}{r}\cos\theta.
$$

A negative result simply means friction actually points downhill.

### Family 4D: Conical pendulum, frictionless cone, or rotating bead

For a conical pendulum with angle from vertical,

$$
T\cos\theta=mg,
\qquad
T\sin\theta=m\frac{v^2}{r},
\qquad
r=L\sin\theta.
$$

**Walkthrough**

1. Identify where the angle is measured; sine and cosine swap if it is measured from horizontal.
2. Draw only gravity and tension/normal.
3. Use vertical equilibrium and horizontal radial dynamics.
4. Divide equations to eliminate the angled-force magnitude.
5. Add geometry and $v=2\pi r/T_{\rm orbit}$.

If the pendulum angle is measured above the horizontal instead, $r=L\cos\theta$ and the component equations swap sine/cosine roles. The lecture/HW form reduces to

$$
\sin\theta=\frac{gT_{\rm orbit}^2}{4\pi^2L}.
$$

For a bead on a frictionless inverted cone,

$$
N\sin\theta=mg,
\qquad
N\cos\theta=m\frac{v^2}{r},
$$

with the particular cone geometry supplying the last equation. The spinning-loop bead on Quiz 1 is the same force-counting family: gravity plus one normal force.

For the practice-quiz inverted-cone geometry, eliminating $N$ and using the cone dimensions gives

$$
v=\sqrt{gh},
\qquad
T_{\rm orbit}=\frac{2\pi r}{\sqrt{gh}}.
$$

### Family 4E: Contact loss

At the instant contact is just lost,

$$N=0,$$

but speed, radial acceleration, and net force are generally nonzero.

Inside a loop at the top:

$$
mg+N=m\frac{v_{\rm top}^2}{r}
\quad\Rightarrow\quad
v_{\rm top,min}=\sqrt{gr}.
$$

Outside a crest:

$$
mg-N=m\frac{v^2}{r},
$$

so the contact threshold is $v=\sqrt{gr}$.

**Trap:** a formal negative normal force means contact would already have failed; the surface cannot pull unless an attachment is specified.

### Family 4F: Loop-the-loop minimum entry speed

1. At the top threshold, set $N=0$:
   $$v_{\rm top}^2=gr.$$
2. Use energy over the $2r$ rise:
   $$
   \frac12mv_0^2=\frac12mv_{\rm top}^2+mg(2r).
   $$
3. Therefore,
   $$v_{0,\min}=\sqrt{5gr}.$$

**Variants:** find $N$ at the bottom/top for a larger entry speed; include a different release height; conceptual questions about energy and nonuniform speed.

### Family 4G: Slider leaving the outside of a sphere

For a slider starting from rest at the top:

1. Radial dynamics while in contact:
   $$mg\cos\theta-N=m\frac{v^2}{r}.$$
2. At lift-off:
   $$N=0\Rightarrow v^2=gr\cos\theta.$$
3. Energy from the top:
   $$v^2=2gr(1-\cos\theta).$$
4. Equate the two results:
   $$
   \cos\theta=\frac23,
   \qquad
   \theta\approx48^\circ.
   $$

[Back to table of contents](#table-of-contents)

---

<a id="module-2"></a>
# Module 2 — Center of Mass and Rotational Mechanics

<a id="m2-center-of-mass"></a>
## 5. Center of Mass

### Family 5A: Discrete, grouped, and planar center of mass

$$
\vec r_{\rm cm}=\frac{\sum_i m_i\vec r_i}{\sum_i m_i}.
$$

**Walkthrough**

1. Choose an origin and signed axes.
2. Locate the center of mass of each component—not merely its endpoint.
3. Make a mass-position ledger.
4. Compute $x_{\rm cm}$ and $y_{\rm cm}$ separately.
5. Check that the result is closer to the heavier component and lies in a plausible region.

**Variants:** point masses; groups of identical blocks; pole plus masses; two-dimensional rod/ball arrangements; an object rotating about the composite COM.

For the Quiz 2 composite-pole form,

$$
x_{\rm cm}=
\frac{m_pL/2+2m_1L/3+m_2L}{m_p+m_1+m_2}.
$$

If $m_2$ is at $x=L$, its radius about the COM is $L-x_{\rm cm}$, so

$$
v_2=\omega(L-x_{\rm cm}).
$$

### Family 5B: Continuous density and normalization

$$
dm=\lambda(x)\,dx,
\qquad
M=\int dm,
\qquad
x_{\rm cm}=\frac1M\int x\,dm.
$$

**Walkthrough**

1. Write the mass element from the density.
2. Integrate over the full object to determine any unknown density constant.
3. Use the same $dm$ in the COM integral.
4. Check that the COM shifts toward the denser end.

For $\lambda=Cx^n$ on $0\le x\le L$,

$$
C=\frac{(n+1)M}{L^{n+1}},
\qquad
x_{\rm cm}=\frac{n+1}{n+2}L.
$$

**Variants:** density increasing toward either endpoint; areal density $dm=\sigma\,dA$; solve for the density constant, total mass, or COM.

### Family 5C: Holes and removed mass

Treat missing material as negative mass:

$$
M_{\rm rem}=M_{\rm full}-M_{\rm hole},
$$

$$
\vec r_{\rm cm,rem}=
\frac{M_{\rm full}\vec r_{\rm full}-M_{\rm hole}\vec r_{\rm hole}}
{M_{\rm full}-M_{\rm hole}}.
$$

**Walkthrough**

1. Use area or volume ratio to find the removed mass.
2. Use symmetry immediately for any zero component.
3. Insert the hole with a minus sign at the hole's own center.
4. Verify that the remaining COM shifts away from the hole.

Example: a disk with an $R/2$ circular hole has removed mass $M/4$ if $M$ denotes the original full disk. In the course geometry, symmetry gave $y_{\rm cm}=0$ and $x_{\rm cm}=-R/6$.

<a id="m2-inertia-torque"></a>
## 6. Moment of Inertia, Torque, and Equilibrium

### Family 6A: Moment of inertia by sum, integral, or ranking

$$
I=\sum_i m_ir_i^2=\int r_\perp^2\,dm.
$$

**Walkthrough**

1. Identify the axis before calculating.
2. Use shortest perpendicular distance to that axis.
3. Write the correct $dm$.
4. Integrate or sum point contributions.
5. For rankings, more mass farther from the axis means larger $I$.

For $\lambda=Cx^n$ about the end,

$$
I=\frac{n+1}{n+3}ML^2.
$$

Standard central-axis values:

$$
I_{\rm hoop}=MR^2,
\qquad
I_{\rm disk/cylinder}=\frac12MR^2,
$$

$$
I_{\rm solid\ sphere}=\frac25MR^2,
\qquad
I_{\rm spherical\ shell}=\frac23MR^2,
$$

$$
I_{\rm rod,cm}=\frac1{12}ML^2,
\qquad
I_{\rm rod,end}=\frac13ML^2.
$$

### Family 6B: Parallel-axis, composite, and subtractive inertia

$$
I=I_{\rm cm}+Md^2,
\qquad
I_{\rm total}=\sum I_i.
$$

For a hole,

$$
I_{\rm remaining}=I_{\rm full}-I_{\rm hole},
$$

after shifting both terms to the same requested axis.

**Walkthrough**

1. Find each component's inertia about its own center.
2. Measure $d$ from that center to the requested axis.
3. Apply the parallel-axis theorem component by component.
4. Add present material and subtract removed material.

**Variants:** rod about an endpoint or off-center pivot; disk about a rim; rod plus point mass; attached cylinders; disk with a hole.

### Family 6C: Rotational kinetic energy and axis comparisons

$$
K_{\rm rot}=\frac12I\omega^2.
$$

- At equal $\omega$, kinetic-energy ratios equal inertia ratios.
- At equal angular momentum, use
  $$K=\frac{L^2}{2I},$$
  so the ordering reverses: larger $I$ means smaller $K$.

### Family 6D: Torque magnitude and direction

$$
\vec\tau=\vec r\times\vec F,
\qquad
|\tau|=rF\sin\phi=Fd_\perp.
$$

**Walkthrough**

1. Mark the pivot.
2. Draw $\vec r$ from pivot to the force application point.
3. Use the angle between $\vec r$ and $\vec F$, or use the perpendicular moment arm.
4. Assign clockwise/counterclockwise signs.
5. Use the right-hand rule for into/out-of-page direction.

**Variants:** wrench/door rankings; zero torque when the force acts through the pivot; force magnitude needed for a specified torque; vector direction.

### Family 6E: Fixed-axis rotational dynamics

$$
\sum\tau=I\alpha.
$$

**Walkthrough**

1. Draw an extended FBD so application points are visible.
2. Choose the axis and a positive rotation direction.
3. Compute signed torques.
4. Build total $I$ about that same axis.
5. Solve for $\alpha$, force, mass, or time using angular kinematics afterward if needed.

Tangential force on a fixed solid-cylinder spool:

$$
Fr=\frac12mr^2\alpha
\quad\Rightarrow\quad
\alpha=\frac{2F}{mr}.
$$

Rigidly attached cylinders:

$$
FR=\left(\frac12MR^2+\frac12mr^2\right)\alpha.
$$

### Family 6F: Static equilibrium

$$
\sum\vec F=0,
\qquad
\sum\tau=0.
$$

**Walkthrough**

1. Draw point and extended FBDs.
2. Choose a pivot that eliminates the most unknown forces.
3. Write horizontal and vertical force balance.
4. Write signed torque balance.
5. Solve symbolically and verify that contact forces are physically nonnegative.

**Variants:** teeter-totter; plank plus load; rod plus sphere; support-wire tension; a statics result feeding a wave-speed problem.

### Family 6G: Tipping threshold

At incipient tipping, the support that is losing contact has zero normal force. The remaining edge is the pivot.

1. Identify the tipping edge.
2. Set the far support normal to zero.
3. Take torques about the tipping edge.
4. Balance tipping and restoring moments.

General form:

$$
mgx_{\max}=Mg\,d_{\rm cm}.
$$

**Variants:** move the load; change the base width; add another object; ask which support loses contact first.

### Family 6H: Ladder against a smooth wall

For a uniform ladder at angle $\theta$, frictionless wall, and floor at impending slip:

1. Vertical force balance: $N_F=mg$.
2. Horizontal balance: $f_s=N_W$.
3. At threshold: $f_s=\mu_sN_F$.
4. Torque about the foot:
   $$
   N_WL\sin\theta=mg\frac L2\cos\theta.
   $$
5. Therefore,
   $$
   \mu_s=\frac1{2\tan\theta}.
   $$

**Variant:** add a person or load at distance $x$; include its additional weight torque before applying the friction limit.

<a id="m2-dynamics-conservation"></a>
## 7. Pulleys, Rolling, and Angular Momentum

### Family 7A: Massive-pulley Atwood machine

For $m_2>m_1$:

$$
T_1-m_1g=m_1a,
\qquad
m_2g-T_2=m_2a,
$$

$$
(T_2-T_1)R=I\alpha,
\qquad
a=\alpha R.
$$

Thus,

$$
a=\frac{(m_2-m_1)g}{m_1+m_2+I/R^2}.
$$

For a solid-disk pulley, $I/R^2=M_p/2$.

**Walkthrough**

1. Give each block its own signed translation equation.
2. Keep $T_1\ne T_2$; unequal tensions create the pulley torque.
3. Write the pulley torque equation.
4. Apply the no-slip relation $a=\alpha R$.
5. Solve the coupled system.

Quiz 2's ranking follows from the equations:

$$
m_2g>T_2>T_1>m_1g.
$$

For one falling mass coupled to a flywheel,

$$
a=\frac{mg}{m+I/R^2}.
$$

Larger rotational inertia produces smaller acceleration and a longer descent time.

### Family 7B: Rolling without slipping

$$
v_{\rm cm}=\omega R,
\qquad
a_{\rm cm}=\alpha R,
\qquad
I=\beta MR^2.
$$

Energy through a height $h$:

$$
Mgh=\frac12Mv^2+\frac12I\frac{v^2}{R^2},
$$

so

$$
v=\sqrt{\frac{2gh}{1+\beta}}.
$$

Acceleration down an incline:

$$
a=\frac{g\sin\theta}{1+\beta}.
$$

Energy partition:

$$
\frac{K_{\rm rot}}{K_{\rm trans}}=\beta.
$$

**What cancels and what controls the race**

- Same shape means same $\beta$, so mass and radius cancel from $v$ and $a$.
- Smaller $\beta$ reaches the bottom first.
- Hoop: $\beta=1$ and $K_{\rm rot}=K_{\rm trans}$.
- Solid cylinder: $\beta=1/2$ and $v=\sqrt{4gh/3}$.
- Solid sphere: $\beta=2/5$.
- Hollow sphere: $\beta=2/3$ and $v=\sqrt{6gh/5}$.

For descent time, use ramp distance $s=h/\sin\theta$ and $s=\tfrac12at^2$. For a solid cylinder,

$$
t=\sqrt{\frac{3h}{g\sin^2\theta}}.
$$

**Traps:** static friction can be nonzero even though the contact point does not slip; use $v=\omega R$ only for rolling without slipping.

### Family 7C: Coupled rolling object or yo-yo

1. Draw tension and an initially assumed static-friction direction.
2. Write $\sum F_x=Ma$.
3. Take torques about the center, using the inner axle radius for tension and outer radius for friction.
4. Apply $a=\alpha R$ with consistent signs.
5. Solve simultaneously. A negative friction result means the actual direction is opposite the assumption.

In the HW form with a solid cylinder and inner radius $R/4$,

$$a=\frac{5T}{6M}.$$

### Family 7D: Angular momentum definition and ranking

$$
\vec L=\vec r\times\vec p,
\qquad
L_{\rm particle}=mrv\sin\phi,
\qquad
L_{\rm rigid}=I\omega.
$$

**Walkthrough:** name the reference point/axis; use perpendicular distance for a particle; use $I\omega$ for a rigid body; at equal $\omega$, rank by $I$.

### Family 7E: Conservation when the distribution changes

If net external torque about the selected axis is negligible,

$$
L_i=L_f,
\qquad
I_i\omega_i=I_f\omega_f.
$$

**Walkthrough**

1. Choose the axis and audit external torques about it.
2. Compute $I_i$ and $I_f$ about that axis.
3. Include incoming particle angular momentum when present.
4. Solve for the new angular speed.
5. Do not assume mechanical energy is conserved if mass sticks or internal motion changes.

If the moment of inertia doubles, $\omega$ halves. The kinetic-energy change is found only after applying angular-momentum conservation.

### Family 7F: Off-center sticking collision

For a tangential bullet of mass $m$ and speed $v$ embedding at rotor radius $R$,

$$
mRv=\left(I_{\rm rotor}+mR^2\right)\omega_f.
$$

**Walkthrough**

1. Choose the axle as the angular-momentum reference point.
2. Compute the incoming $L=mvd_\perp$.
3. Add the embedded mass's $mR^2$ to the final inertia.
4. Conserve angular momentum during the short collision.
5. Compute energy loss separately if requested; sticking is inelastic.

[Back to table of contents](#table-of-contents)

---

<a id="module-3"></a>
# Module 3 — Gravitation and Orbits

<a id="m3-force-energy"></a>
## 8. Force, Field, Potential, and Energy

### Family 8A: Inverse-square force and field scaling

$$
F_g=\frac{Gm_1m_2}{r^2},
\qquad
g(r)=\frac{GM}{r^2}.
$$

**Walkthrough**

1. Use center-to-center separation.
2. For comparisons, form a ratio before substituting:
   $$
   \frac{F_2}{F_1}=\frac{m'_1m'_2}{m_1m_2}
   \left(\frac{r_1}{r_2}\right)^2.
   $$
3. At altitude $h$, use $r=R+h$:
   $$
   \frac{g_h}{g_{\rm surface}}=\left(\frac{R}{R+h}\right)^2.
   $$
4. For planet scaling:
   $$
   \frac{g'}g=\frac{M'/M}{(R'/R)^2}.
   $$

**Variants:** doubled separation; surface gravity of an exoplanet; solve for mass, radius, or altitude. When comparing electric and gravitational forces between the same particles,

$$
\frac{F_e}{F_g}=\frac{k|q_1q_2|}{Gm_1m_2};
$$

the common distance cancels.

### Family 8B: Zero-net-gravity point on a line

For masses $M_1$ and $M_2$ separated by $d$, with the test mass at $x$ from $M_1$,

$$
\frac{GM_1m}{x^2}=\frac{GM_2m}{(d-x)^2}.
$$

**Walkthrough**

1. Draw both attractive-force directions.
2. Set magnitudes equal only in a region where the directions oppose.
3. Cancel $Gm$, take the positive square root, and solve.
4. Retain a root satisfying $0<x<d$.
5. The balance point must be closer to the smaller source mass.

### Family 8C: Vector superposition of gravitational forces

1. Draw one force on the target toward every other mass.
2. Compute every separation.
3. Resolve each force into Cartesian components.
4. Sum:
   $$F_x=\sum_iF_{ix},\qquad F_y=\sum_iF_{iy}.$$
5. Find
   $$F_{\rm net}=\sqrt{F_x^2+F_y^2}$$
   and its direction.
6. Use symmetry before algebra.

**Variants:** right-triangle arrangement; square corners; equal forces separated by a known angle. Two equal forces $60^\circ$ apart have resultant $\sqrt3F$.

### Family 8D: Gravitational potential energy and pair counting

For one pair,

$$
U_{ij}=-\frac{Gm_im_j}{r_{ij}}.
$$

For a system,

$$
U_{\rm system}=\sum_{i<j}-\frac{Gm_im_j}{r_{ij}}.
$$

**Walkthrough**

1. List every unordered pair.
2. Count each pair exactly once.
3. Use $1/r$, not $1/r^2$.
4. Use each pair's actual separation.
5. Add scalar energies; no vector resolution is needed.
6. More negative $U$ means a more tightly bound configuration.

Quiz 2's two-planet form required three pairs:

$$
U=-\frac{2GMm}{r}-\frac{Gm^2}{2r}.
$$

**Variants:** triangle, square, unequal masses, changing one separation, or comparing binding between configurations.

### Family 8E: Escape speed and bound/unbound classification

At the escape threshold, $E_f=0$ at infinity:

$$
\frac12mv_{\rm esc}^2-\frac{GMm}{R}=0,
$$

so

$$
v_{\rm esc}=\sqrt{\frac{2GM}{R}}.
$$

**Walkthrough:** use center-based launch radius; set final $K$ and $U$ to zero at infinity; cancel projectile mass; compare with circular speed at the same radius:

$$
v_{\rm esc}=\sqrt2\,v_{\rm orb}.
$$

**Variants:** launch from altitude $R+h$; solve for planet mass/radius; classify $E<0$ bound, $E=0$ escape threshold, $E>0$ unbound.

<a id="m3-orbits"></a>
## 9. Circular and Elliptical Orbits

### Family 9A: Circular-orbit speed and acceleration

Gravity supplies the inward net force:

$$
\frac{GMm}{r^2}=m\frac{v^2}{r}.
$$

Therefore,

$$
v_{\rm orb}=\sqrt{\frac{GM}{r}},
\qquad
a_r=\frac{GM}{r^2}.
$$

**Walkthrough:** use radius from the central body's center; draw gravity as the real inward force; do not add a separate centripetal force; cancel satellite mass; check $v\propto r^{-1/2}$.

### Family 9B: Circular-orbit energy

Using $v^2=GM/r$,

$$
K=\frac{GMm}{2r},
\qquad
U=-\frac{GMm}{r},
\qquad
E=-\frac{GMm}{2r}.
$$

Higher circular orbit:

- $v$ and $K$ decrease.
- $U$ and $E$ increase, meaning they become less negative.
- Positive energy must be added to raise the orbit.

**Variants:** energy difference between two circular radii; solve mass or radius from $E$; compare binding strength.

### Family 9C: Kepler's laws and orbital scaling

- First law: an orbit is an ellipse with the central body at one focus.
- Second law: equal areas in equal times; orbital speed is greatest near periapsis.
- Third law: $T^2\propto a^3$.

For a circular orbit,

$$
T=2\pi\sqrt{\frac{r^3}{GM}},
\qquad
T^2=\frac{4\pi^2r^3}{GM}.
$$

For two orbits about the same central mass,

$$
\left(\frac{T_2}{T_1}\right)^2=
\left(\frac{a_2}{a_1}\right)^3.
$$

**Walkthrough:** confirm the central mass is shared; use semimajor axis $a$ for ellipses and $a=r$ for circles; use ratios for comparisons and SI units for absolute calculations.

Useful inversions:

$$
a\propto T^{2/3},
\qquad
M=\frac{4\pi^2a^3}{GT^2}.
$$

### Family 9D: Geostationary orbit

A geostationary satellite is circular, equatorial, prograde, and has the planet's rotation period.

1. Convert $T$ to seconds.
2. Find the center-based orbital radius:
   $$
   r=\left(\frac{GMT^2}{4\pi^2}\right)^{1/3}.
   $$
3. If altitude is requested, subtract the planet radius:
   $$h=r-R.$$

**Trap:** do not report orbital radius $r$ as altitude $h$.

### Family 9E: Elliptical-orbit apsides

At periapsis and apoapsis, velocity is perpendicular to radius, so angular momentum conservation gives

$$
mr_pv_p=mr_av_a,
$$

and therefore

$$
\frac{v_p}{v_a}=\frac{r_a}{r_p}.
$$

**Walkthrough:** identify closest and farthest points; conserve angular momentum there; the smaller-radius point is faster; check with energy because smaller $r$ means more negative $U$ and larger $K$.

<a id="m3-binary"></a>
## 10. Binary Systems and Many-Body Synthesis

### Family 10A: Binary-star center, period, speed, and energy

For masses $M$ and $m$ separated by $d$,

$$
r_M=\frac{m}{M+m}d,
\qquad
r_m=\frac{M}{M+m}d,
\qquad
r_M+r_m=d.
$$

Both bodies share angular speed and period. The larger mass has the smaller orbital radius and smaller linear speed.

$$
T=2\pi\sqrt{\frac{d^3}{G(M+m)}}.
$$

For a circular binary,

$$
U=-\frac{GMm}{d},
\qquad
K_{\rm total}=\frac{GMm}{2d},
\qquad
E=-\frac{GMm}{2d}.
$$

**Walkthrough**

1. Put one body at $0$ and the other at $d$.
2. Locate the shared COM and the two orbital radii.
3. Use full separation $d$ and total mass $M+m$ in the period formula.
4. Use $v_i=(2\pi/T)r_i$ for individual speeds.
5. Use separation $d$ in $U$ and $E$, not an individual COM radius.

Quiz 2 used $M=\tfrac32m$:

$$
x_{\rm cm}=\frac{2d}{5},
\qquad
T=2\pi\sqrt{\frac{2d^3}{5Gm}},
\qquad
E=-\frac{3Gm^2}{4d}.
$$

### Family 10B: Symmetric many-body circular orbit

**Solution chain**

1. Locate the common COM geometrically.
2. Find one body's orbital radius about the COM.
3. Vector-sum all gravitational forces on that body.
4. Set the inward resultant equal to $mv^2/r_{\rm orb}$.
5. Count every body for total kinetic energy.
6. Count every unordered pair once for potential energy.
7. Add $E=K+U$.

For three equal masses at the corners of an equilateral triangle of side $L$,

$$
r_{\rm orb}=\frac{L}{\sqrt3},
\qquad
F_{\rm net}=\sqrt3\frac{Gm^2}{L^2},
$$

$$
v=\sqrt{\frac{Gm}{L}},
\qquad
U=-3\frac{Gm^2}{L},
\qquad
E=-\frac32\frac{Gm^2}{L}.
$$

For four equal masses at square corners, side $L$,

$$
r_{\rm orb}=\frac{L}{\sqrt2},
$$

$$
F_{\rm net}=\left(\sqrt2+\frac12\right)\frac{Gm^2}{L^2},
$$

$$
v=\sqrt{\frac{Gm}{L}\left(1+\frac1{2\sqrt2}\right)},
\qquad
U=-\frac{Gm^2}{L}(4+\sqrt2).
$$

**Traps:** the force sum is a vector sum; the energy sum is a scalar pair sum; use COM radius for circular dynamics but pair separation for gravitational potential.

[Back to table of contents](#table-of-contents)

---

<a id="module-4"></a>
# Module 4 — Oscillations

<a id="m4-shm"></a>
## 11. SHM Equations, Graphs, Phase, and Energy

### Family 11A: Read or build the SHM model

$$
x(t)=A\cos(\omega t+\phi),
$$

$$
v(t)=-A\omega\sin(\omega t+\phi),
$$

$$
a(t)=-A\omega^2\cos(\omega t+\phi)=-\omega^2x(t).
$$

Also,

$$
f=\frac1T,
\qquad
\omega=2\pi f=\frac{2\pi}{T},
$$

$$
v_{\max}=A\omega,
\qquad
a_{\max}=A\omega^2.
$$

**Graph-reading walkthrough**

1. Amplitude is maximum displacement from equilibrium, not peak-to-peak height.
2. Period is the time between equivalent points moving the same direction.
3. Compute $f=1/T$ and $\omega=2\pi/T$.
4. Use slopes to determine velocity sign.
5. Acceleration always points toward equilibrium because $a=-\omega^2x$.

**State map**

| Position | Speed | Acceleration |
|---|---:|---|
| $x=+A$ | $0$ | maximum toward $-x$ |
| $x=0$ | maximum | $0$ |
| $x=-A$ | $0$ | maximum toward $+x$ |

The object speeds up when velocity and acceleration have the same sign, $va>0$, and slows when $va<0$.

### Family 11B: Phase and initial conditions

At $t=0$,

$$
x_0=A\cos\phi,
\qquad
v_0=-A\omega\sin\phi.
$$

If $x_0$ and $v_0$ are given,

$$
A=\sqrt{x_0^2+\left(\frac{v_0}{\omega}\right)^2},
$$

and a quadrant-safe phase is

$$
\phi=\operatorname{atan2}\left(-\frac{v_0}{\omega},x_0\right).
$$

**Event-time walkthrough**

1. Write the desired state as a target phase.
2. Solve $\omega t+\phi=\theta_{\rm target}+2\pi n$.
3. Choose the smallest nonnegative $t$ satisfying the requested motion direction.

Reference cycle for cosine:

- $0$: at $+A$.
- $\pi/2$: at equilibrium moving negative.
- $\pi$: at $-A$.
- $3\pi/2$: at equilibrium moving positive.

**Traps:** use radians; inverse cosine alone loses velocity-direction information; the first algebraic root may not be the first physical event.

### Family 11C: Spring period and scaling

$$
\omega=\sqrt{\frac{k}{m}},
\qquad
T=2\pi\sqrt{\frac{m}{k}},
\qquad
f=\frac1{2\pi}\sqrt{\frac{k}{m}}.
$$

For two systems,

$$
\frac{T_2}{T_1}=\sqrt{\frac{m_2/k_2}{m_1/k_1}},
\qquad
\frac{f_2}{f_1}=\sqrt{\frac{k_2/m_2}{k_1/m_1}}.
$$

**Walkthrough:** build the ratio before inserting factors; simplify under the square root; check that increasing $m$ increases $T$, while increasing $k$ decreases $T$.

**Variants:** change only $m$ or $k$; change both; solve an unknown stiffness from a measured period; vertical spring. Gravity shifts the vertical equilibrium position but does not change the ideal period about that equilibrium.

### Family 11D: Spring energy and speed at position

$$
F_s=-kx,
\qquad
U_s=\frac12kx^2,
$$

$$
E=\frac12kA^2=\frac12mv^2+\frac12kx^2.
$$

Thus,

$$
v=\pm\omega\sqrt{A^2-x^2}.
$$

**Walkthrough**

1. Measure $x$ from equilibrium.
2. Use total energy from the amplitude.
3. Subtract the spring energy at the requested position.
4. Use the motion direction to choose the sign of $v$.

At equilibrium, speed and kinetic energy are maximum. At either turning point, speed is zero and spring energy is maximum.

**Variants:** find amplitude from a speed-position pair; fraction of energy kinetic/potential; position where $K=U$ ($|x|=A/\sqrt2$); maximum speed from a graph.

<a id="m4-collisions"></a>
## 12. Spring Collisions and Changing Systems

### Family 12A: A moving mass sticks to an oscillator

Separate the short collision from the later oscillation.

1. Evaluate the original oscillator at the collision position $x$ to find $v_0$ if necessary.
2. During the short sticking event, conserve linear momentum:
   $$
   Mv_0=(M+m)v_f.
   $$
3. The spring position is effectively unchanged during the impulse. Mechanical-energy change during collision is
   $$
   \Delta E=
   \frac12(M+m)v_f^2-\frac12Mv_0^2<0.
   $$
4. Use post-collision oscillator energy to find the new amplitude:
   $$
   \frac12kA'^2=\frac12kx^2+\frac12(M+m)v_f^2.
   $$
5. The new period is
   $$
   T'=2\pi\sqrt{\frac{M+m}{k}}.
   $$

An equivalent amplitude form is

$$
A'=\sqrt{A^2+\frac{2\Delta E}{k}},
$$

provided $\Delta E$ is the energy change of the mechanical oscillator during the collision and is negative.

**Variants:** collision at equilibrium versus at general $x$; object attaches or detaches; ask energy loss, new amplitude, period, or phase.

**Traps:** momentum—not mechanical energy—is conserved during sticking; spring potential does not jump during an instantaneous collision; after sticking, use the combined mass.

<a id="m4-pendula"></a>
## 13. Simple and Physical Pendula

### Family 13A: Simple pendulum

For the small-angle approximation,

$$
T=2\pi\sqrt{\frac{L}{g}},
\qquad
f=\frac1{2\pi}\sqrt{\frac{g}{L}}.
$$

**Walkthrough**

1. Confirm the bob can be treated as a point mass and the angle is small.
2. Use length from pivot to the bob's center.
3. Form a ratio when comparing pendula.
4. Combine with the SHM phase model if position, direction, or event time is requested.

**Variants:** solve $L$ or $g$; compare lengths; change planet; combine with $\theta(t)=\theta_{\max}\cos(\omega t+\phi)$.

Mass does not affect the period. Initial angle does not affect it only within the small-angle approximation.

### Family 13B: Physical or composite pendulum

For total mass $M_{\rm tot}$, pivot-to-COM distance $d_{\rm cm}$, and moment of inertia about the actual pivot $I_p$,

$$
T=2\pi\sqrt{\frac{I_p}{M_{\rm tot}gd_{\rm cm}}}.
$$

For components, an often safer form is

$$
T=2\pi\sqrt{\frac{I_p}{g\sum_i m_ir_i}},
$$

where $r_i$ is the pivot-to-COM distance of component $i$.

**Walkthrough**

1. Identify the pivot.
2. Find each component's mass and COM distance $r_i$.
3. Shift each component inertia to the pivot:
   $$I_{p,i}=I_{{\rm cm},i}+m_ir_i^2.$$
4. Add $I_p=\sum I_{p,i}$.
5. Find $d_{\rm cm}$ or directly use $\sum m_ir_i$.
6. Insert into the physical-pendulum formula and simplify symbolically.

**Variants:** uniform rod about its end or another pivot; rod plus point mass; cable/rod plus disk or sphere; compare a point-mass approximation with the accurate extended-body model.

**Traps:** use inertia about the actual pivot; use total mass and composite COM; a shifted pivot changes both $I_p$ and $d_{\rm cm}$; do not treat an extended disk or sphere as a point mass unless instructed.

**Scope note:** The M4-2 source lecture excludes damping and driven oscillations from the final.

[Back to table of contents](#table-of-contents)

---

<a id="module-5"></a>
# Module 5 — Traveling Waves, Sound, and Interference

<a id="m5-traveling-waves"></a>
## 14. Traveling Waves and String Speed

### Family 14A: Classify the wave and its restoring mechanism

- **Transverse:** particle displacement is perpendicular to propagation; examples include ideal string waves and electromagnetic waves.
- **Longitudinal:** particle displacement is parallel to propagation; sound in air has compressions and rarefactions.
- **Mechanical:** requires a medium; speed is set by the medium.
- **Electromagnetic:** does not require a material medium; $\vec E$, $\vec B$, and propagation direction are mutually perpendicular.

**Question forms:** identify particle motion; decide whether a medium is required; identify the restoring force; distinguish one object's oscillation from a wave carrying energy through coupled oscillators.

### Family 14B: Read a sinusoidal traveling-wave equation

$$
y(x,t)=A\sin(kx-\omega t+\phi)
$$

moves in $+x$. Replacing the minus with a plus moves the wave in $-x$.

$$
\lambda=\frac{2\pi}{k},
\qquad
f=\frac{\omega}{2\pi},
\qquad
T=\frac{2\pi}{\omega},
$$

$$
v_{\rm wave}=\frac{\omega}{k}=f\lambda.
$$

**Walkthrough**

1. Match the equation to $A$, $k$, $\omega$, and $\phi$.
2. Use the sign between $kx$ and $\omega t$ for propagation direction.
3. Convert $k\leftrightarrow\lambda$ and $\omega\leftrightarrow f,T$.
4. Use $v=\omega/k=f\lambda$.

**Variants:** write the equation from a snapshot and direction; find phase at a point; compare spatial and time graphs; solve for wavelength, frequency, or speed.

### Family 14C: Particle direction from a wave snapshot

For a right-moving wave,

$$
\frac{\partial y}{\partial t}
=-v_{\rm wave}\frac{\partial y}{\partial x}.
$$

For a left-moving wave, the signs of local particle velocity and spatial slope agree.

**Snapshot algorithm**

1. Mark the local slope at the particle.
2. For a right-moving profile, particle motion has the opposite sign from that slope.
3. For a left-moving profile, particle motion has the same sign as the slope.
4. Particle speed is largest at the steepest zero crossings and zero at crests/troughs.

Quiz 3 P3 was almost a direct repeat of this lecture family.

### Family 14D: Wave speed versus particle speed

The propagation speed is not the transverse speed of a string element.

$$
u_{\rm particle,max}=A\omega=2\pi Af
=\frac{2\pi A}{\lambda}v_{\rm wave}.
$$

**Walkthrough**

1. Find propagation speed from the medium.
2. Use $f=v_{\rm wave}/\lambda$.
3. Use $u_{\max}=2\pi Af$.
4. If maximum particle speed is given, invert:
   $$
   A=\frac{u_{\max}}{2\pi f}
   =\frac{u_{\max}\lambda}{2\pi v_{\rm wave}}.
   $$

### Family 14E: Wave speed on a string

$$
\mu=\frac{m_{\rm string}}{L_{\rm actual}},
\qquad
v_{\rm wave}=\sqrt{\frac{T}{\mu}}.
$$

**Walkthrough**

1. Find string tension from the actual mechanics; a hanging mass often gives $T\approx Mg$, but only when its acceleration is negligible.
2. Find the actual string length, not a projection.
3. Compute linear density $\mu$.
4. Insert into $v=\sqrt{T/\mu}$.
5. Continue with $f=v/\lambda$ or the particle-amplitude relation as requested.

**Scaling:** $v\propto\sqrt T$ and $v\propto1/\sqrt\mu$.

### Family 14F: Statics → tension → wave chain

PQ3 P4 and Q3 P5 use this chain with different support geometries.

**Solution chain**

1. Draw the rigid object's extended FBD.
2. Use $\sum\tau=0$ and $\sum\vec F=0$ to find tension.
3. Use geometry for the wire's actual length.
4. Compute $\mu=m_{\rm wire}/L_{\rm actual}$.
5. Find $v=\sqrt{T/\mu}$.
6. Continue to $f=v/\lambda$.
7. If maximum transverse particle speed is given, use
   $$A=\frac{u_{\max}\lambda}{2\pi v}.$$

Practice-quiz shelf template:

$$
T=\frac{(m_1+2m_2)g}{2\sin\theta},
\qquad
L_w=\frac{L}{\cos\theta},
\qquad
\mu=\frac{m_w\cos\theta}{L}.
$$

Quiz 3 sphere-on-incline template:

$$
f_s=T,
\qquad
T=\frac{m_1g\sin\phi}{2},
$$

$$
v=\sqrt{\frac{m_1gL\sin\phi}{2m_2}}.
$$

The geometry changed between practice and test, while the solution chain stayed the same.

### Family 14G: Spherical wavefront geometry

**Recognition cue:** several listeners detect the same pulse simultaneously.

1. Simultaneous detection of one wavefront means equal source-to-listener distances.
2. Use symmetry or perpendicular-bisector geometry to locate the source.
3. The common distance is the wavefront radius.
4. Use the distance formula or Pythagorean theorem for another listener coordinate.

<a id="m5-refraction-intensity"></a>
## 15. Refraction, Intensity, and Decibels

### Family 15A: Index, speed, and wavelength across a boundary

$$
n=\frac{c}{v}.
$$

At a stationary boundary, frequency remains constant. Therefore,

$$
v=f\lambda,
\qquad
n_1\lambda_1=n_2\lambda_2.
$$

**Walkthrough**

1. Hold frequency constant across the boundary.
2. Larger $n$ means smaller speed and smaller wavelength.
3. Use $\lambda_{\rm medium}=\lambda_0/n$ when the other medium is vacuum/air.
4. Rank media using wavelength or speed snapshots.

Number of wavelengths across thickness $D$:

$$
N=\frac{D}{\lambda_{\rm medium}}
=\frac{nD}{\lambda_0}
=\frac{nDf}{c}.
$$

For two frequencies in the same nondispersive medium,

$$
\Delta N=\frac{nD}{c}(f_1-f_2).
$$

**Traps:** frequency does not change at the boundary; shortest wavelength at fixed frequency means largest $n$; this M5 family is wavelength/index refraction, not Module 7 Snell-angle ray optics.

### Family 15B: Power and amplitude/frequency scaling

For otherwise fixed medium conditions,

$$
P\propto f^2A^2,
\qquad
I\propto f^2A^2.
$$

Thus,

$$
\frac{P_2}{P_1}=\left(\frac{f_2}{f_1}\right)^2
\left(\frac{A_2}{A_1}\right)^2.
$$

**Variants:** hold power fixed and solve amplitude ratio; double frequency or amplitude; compare waves in the same medium.

### Family 15C: Isotropic intensity and inverse square

$$
I=\frac{P}{4\pi r^2},
\qquad
I_1r_1^2=I_2r_2^2.
$$

Useful inversion:

$$
r_2=r_1\sqrt{\frac{I_1}{I_2}}.
$$

**Walkthrough:** identify whether total power stays constant; use a ratio; remember that doubling distance makes intensity one fourth.

For sound redirected into a tube of radius $r$ instead of spreading over a sphere of radius $d$, compare $4\pi d^2$ with $\pi r^2$.

### Family 15D: Decibels

$$
\beta=10\log_{10}\left(\frac{I}{I_0}\right),
\qquad
I_0=10^{-12}\ \mathrm{W/m^2}.
$$

Invert with

$$
I=I_0\,10^{\beta/10}.
$$

For a change,

$$
\Delta\beta=10\log_{10}\left(\frac{I_2}{I_1}\right).
$$

For $N$ equal independent sources,

$$
\beta_N=\beta_1+10\log_{10}N.
$$

Because $I\propto A^2$,

$$
\Delta\beta=20\log_{10}\left(\frac{A_2}{A_1}\right).
$$

**Walkthrough for multiple sources:** convert the question to intensities; add intensities; convert the result back to dB.

**Traps:** never add dB values directly; use $10\log$ for intensity ratios; $20\log$ appears only after substituting an amplitude ratio; doubling intensity adds about $3\ \mathrm{dB}$.

<a id="m5-doppler"></a>
## 16. Doppler Effect

### Family 16A: Identify the role and sign

| Situation | Observed frequency |
|---|---|
| Observer moves toward stationary source | $f'=f_s\dfrac{v+v_o}{v}$ |
| Observer moves away from stationary source | $f'=f_s\dfrac{v-v_o}{v}$ |
| Source moves toward stationary observer | $f'=f_s\dfrac{v}{v-v_s}$ |
| Source moves away from stationary observer | $f'=f_s\dfrac{v}{v+v_s}$ |

Here $v$ is wave speed in the medium, and $v_o,v_s$ are positive magnitudes in the described toward/away roles.

**Walkthrough**

1. Label the source and observer explicitly.
2. Decide whether their separation is increasing or decreasing.
3. Predict higher or lower observed frequency before choosing an equation.
4. Determine any required mechanical speed first.
5. Apply the formula matching the moving role.
6. Check the result against the prediction.

Useful feeder speeds:

$$
u_{\rm free\ fall}=\sqrt{2gd},
$$

$$
u_{\rm circular}=2\pi R\left(\frac{\mathrm{rpm}}{60}\right).
$$

Quiz 3 P4 used free fall to obtain the moving-observer speed before the Doppler step.

### Family 16B: Invert Doppler or apply it twice

**Variants**

- Solve for source/observer speed from an observed frequency.
- Use approaching and receding frequencies as two equations.
- Find highest/lowest frequency from a rotating source.
- Use orbital, circular, or energy-derived speed as the Doppler input.
- Echo: apply Doppler once from a moving source to a wall, then treat the reflected frequency at the wall as the source frequency for the moving receiver.

**Traps:** source and observer formulas are not interchangeable; an object's own emitted frequency is irrelevant when it is acting only as the observer of another source; predict the direction of shift first.

<a id="m5-standing-waves"></a>
## 17. Superposition, Reflection, and Standing Waves

### Family 17A: Pulse superposition and reflection

$$
y_{\rm net}=y_1+y_2.
$$

**Walkthrough:** add signed displacements point by point during overlap; after overlap, each pulse continues with its original shape/direction in the ideal model.

- Fixed-end reflection: inverted, a phase change of $\pi$.
- Free-end reflection: not inverted.
- Crest + crest or trough + trough: constructive.
- Crest + trough: destructive.

### Family 17B: Standing wave on a fixed–fixed string

$$
L=\frac{n\lambda_n}{2},
\qquad
\lambda_n=\frac{2L}{n},
\qquad
f_n=\frac{nv}{2L},
\qquad n=1,2,3,\dots
$$

With $v=\sqrt{T/\mu}$,

$$
f_n=\frac{n}{2L}\sqrt{\frac{T}{\mu}}.
$$

Useful tension inversion:

$$
T=\mu\left(\frac{2Lf_n}{n}\right)^2.
$$

### Family 17C: Standing sound waves in pipes

Open–open and closed–closed pipes have all integer modes:

$$
f_n=\frac{nv}{2L},
\qquad n=1,2,3,\dots
$$

An open–closed pipe has only odd harmonics:

$$
L=\frac{m\lambda_m}{4},
\qquad
f_m=\frac{mv}{4L},
\qquad m=1,3,5,\dots
$$

**Standing-wave setup**

1. Identify displacement boundary conditions: fixed/closed is a node; free/open is an antinode.
2. Sketch the mode.
3. Count half-wavelengths or quarter-wavelengths.
4. Find wave speed from the medium.
5. Use $f=v/\lambda$.
6. Invert for length, tension, harmonic number, or frequency.

Adjacent nodes or adjacent antinodes are separated by $\lambda/2$. A node to its neighboring antinode is $\lambda/4$.

**Traps:** “third harmonic” of an open–closed pipe is $m=3$, but the third allowed mode is $m=5$; use displacement—not pressure—boundary conditions unless the problem explicitly switches representations.

<a id="m5-interference"></a>
## 18. Two-Source Interference and Phase

### Family 18A: Path difference plus initial phase

$$
\Delta\phi=
\frac{2\pi\Delta r}{\lambda}+\Delta\phi_0
=\frac{2\pi f\Delta r}{v}+\Delta\phi_0.
$$

$$
\text{constructive: }\Delta\phi=2\pi n,
$$

$$
\text{destructive: }\Delta\phi=(2n+1)\pi.
$$

**Walkthrough**

1. Determine the source phase difference $\Delta\phi_0$.
2. Compute both geometric path lengths.
3. Form a consistently oriented path difference $\Delta r=r_2-r_1$.
4. Find $\lambda=v/f$ if needed.
5. Add propagation phase and initial phase.
6. Reduce modulo $2\pi$ only if requested.
7. Classify the interference or solve the integer-order condition.

For in-phase sources:

- integer-$\lambda$ path difference is constructive;
- half-integer-$\lambda$ path difference is destructive.

For sources initially $\pi$ out of phase, those rules swap.

### Family 18B: First point or position satisfying interference

1. Write $\Delta r(x)$ from the geometry.
2. Determine how it changes over the allowed region.
3. Insert it into the phase/order condition.
4. Test the smallest reachable integer order consistent with “first point.”
5. Check that the final position lies in the specified interval.

**Traps:** do not omit initial phase; a whole-wavelength path difference preserves an initial out-of-phase relationship; unreduced phase and its modulo-$2\pi$ form are physically equivalent but may not match the requested answer form.

**Beats:** M5-5 says beats were mentioned but not covered in class and would not appear on Quiz 3. The relation is $f_{\rm beat}=|f_1-f_2|$.

[Back to table of contents](#table-of-contents)

---

<a id="module-6"></a>
# Module 6 — Wave Optics

First choose the pattern correctly:

| Pattern | Feature labeled by integer | Governing condition | Small-angle spacing/position |
|---|---|---|---|
| Double slit | bright $m=0,\pm1,\pm2,\dots$ | $d\sin\theta_m=m\lambda$ | $y_m\approx m\lambda L/d$ |
| Diffraction grating | principal bright $m=0,\pm1,\pm2,\dots$ | $d\sin\theta_m=m\lambda$ | Often use exact geometry |
| Single slit | dark $p=1,2,3,\dots$ | $a\sin\theta_p=p\lambda$ | $y_p\approx p\lambda L/a$ |

Here $d$ is slit/grating spacing, $a$ is single-slit width, and $L$ is slit-to-screen distance.

<a id="m6-double-slit"></a>
## 19. Double-Slit Interference

### Family 19A: Bright/dark order and path difference

Bright fringes:

$$
d\sin\theta_m=m\lambda,
\qquad m=0,\pm1,\pm2,\dots
$$

Dark fringes:

$$
d\sin\theta=\left(m+\frac12\right)\lambda,
\qquad m=0,1,2,\dots
$$

**Walkthrough**

1. Identify whether the marked band is bright or dark.
2. Count from the central bright maximum.
3. Translate the order into path difference.
4. Keep the distinction between a signed side label and a positive “nth dark fringe” count.

Examples:

- Second bright fringe: $\Delta r=2\lambda$.
- First dark fringe: $\Delta r=\lambda/2$.
- Third dark fringe: $\Delta r=5\lambda/2$, not $3\lambda$.

### Family 19B: Exact screen geometry

The optical condition uses $\sin\theta$, while the screen geometry uses $\tan\theta$:

$$
y=L\tan\theta.
$$

For a bright fringe,

$$
y_m=L\tan\left[\sin^{-1}\left(\frac{m\lambda}{d}\right)\right].
$$

**Walkthrough**

1. Use the bright/dark condition to relate path difference and angle.
2. Use $\theta=\tan^{-1}(y/L)$ when screen position is given.
3. Solve the optical equation for the requested $\lambda$, $d$, or order.
4. Retain intermediate precision, then round the final answer.

### Family 19C: Small-angle fringe position and graph measurement

For small angles, $\sin\theta\approx\tan\theta\approx y/L$, so

$$
y_m\approx\frac{m\lambda L}{d},
\qquad
\Delta y\approx\frac{\lambda L}{d}.
$$

**Intensity-graph walkthrough**

1. Identify adjacent bright peak centers.
2. Read their separation $\Delta y$ from the axis—not the width of one peak.
3. Convert all lengths to consistent units.
4. Solve
   $$
   \lambda=\frac{\Delta y\,d}{L}.
   $$
5. Convert the final wavelength to nm if requested.

**Variants:** solve slit spacing, wavelength, or screen distance; use nonadjacent peaks and divide their total separation by the number of intervals.

### Family 19D: Qualitative parameter changes and fixed-screen counts

Because

$$
\Delta y\propto\frac{\lambda L}{d},
$$

the pattern spreads out when $\lambda$ or $L$ increases or when $d$ decreases. In vacuum/air, $\lambda=c/f$, so increasing frequency narrows the spacing.

On a fixed-width screen:

- smaller spacing means more fringes fit;
- larger spacing means fewer fringes fit.

**Variants:** change $f$, $\lambda$, $L$, or $d$; ask which change increases fringe spacing versus the number visible.

### Family 19E: Same-angle bright-to-dark transformation

If a point remains at the same angle, equate the two path-difference descriptions.

Example: an $m=2$ bright fringe for spacing $d$ becomes the third dark fringe for spacing $d'$:

$$
d\sin\theta=2\lambda,
$$

$$
d'\sin\theta=\frac52\lambda.
$$

Therefore,

$$
d'=\frac54d.
$$

**Walkthrough:** express both old and new orders as multiples of $\lambda$; use the same $\sin\theta$; divide the equations.

<a id="m6-grating"></a>
## 20. Diffraction Gratings

### Family 20A: Wavelength or spacing from a grating pattern

Principal maxima satisfy

$$
d\sin\theta_m=m\lambda,
\qquad
y_m=L\tan\theta_m.
$$

**Walkthrough**

1. If the given distance is between $+m$ and $-m$, halve it to obtain $|y_m|$.
2. Find the exact angle:
   $$
   \theta_m=\tan^{-1}\left(\frac{y_m}{L}\right).
   $$
3. Solve
   $$
   \lambda=\frac{d\sin\theta_m}{m}
   \quad\text{or}\quad
   d=\frac{m\lambda}{\sin\theta_m}.
   $$
4. Check $|\sin\theta_m|\le1$.

**Variants:** find a higher-order angle from a first-order angle using $\sin\theta_m=m\sin\theta_1$; rank colors because larger $\lambda$ gives larger angle for the same order.

**Trap:** grating angles are often too large for the small-angle approximation; use $y/L=\tan\theta$, not $\sin\theta$.

### Family 20B: Line density

$$
\rho=\frac1d.
$$

**Walkthrough**

1. Determine $d$ from the grating equation.
2. Take the reciprocal with units attached.
3. Convert lines/m to lines/mm by dividing by $1000$.

If a specification is already given as $N$ lines/mm, then

$$
d=\frac{1\ \mathrm{mm}}{N}.
$$

### Family 20C: Maximum physical order and total number of maxima

Because $|\sin\theta|\le1$,

$$
|m|\le\frac{d}{\lambda}.
$$

Thus,

$$
m_{\max}=\left\lfloor\frac{d}{\lambda}\right\rfloor,
\qquad
N_{\rm total}=2m_{\max}+1.
$$

The count includes the central $m=0$ maximum and both signs.

### Family 20D: Maxima visible on a finite screen

Physical existence and screen visibility are separate constraints. For screen half-width $H$,

$$
\theta_{\rm screen}=\tan^{-1}\left(\frac{H}{L}\right).
$$

Then

$$
m_{\max}=\left\lfloor
\min\left(
\frac d\lambda,
\frac{d\sin\theta_{\rm screen}}{\lambda}
\right)
\right\rfloor,
$$

and the symmetric count is $2m_{\max}+1$.

**Walkthrough**

1. Find the physical order limit.
2. Find the screen-edge angle.
3. Convert that angle to an order limit.
4. Take the smaller limit and round down.
5. Count $0$ and both sides.

### Family 20E: Spectroscopy concept

A grating sends different wavelengths to different angles. Longer wavelength appears farther from the center for a fixed order. Atomic emission/absorption lines form element-specific spectral fingerprints.

**Question forms:** identify which color is at the larger angle; distinguish a continuous spectrum from emission or absorption lines; explain why a grating separates wavelengths.

<a id="m6-single-slit"></a>
## 21. Single-Slit Diffraction

### Family 21A: Dark-minimum position

Dark minima satisfy

$$
a\sin\theta_p=p\lambda,
\qquad p=1,2,3,\dots
$$

Exact position:

$$
y_p=L\tan\left[\sin^{-1}\left(\frac{p\lambda}{a}\right)\right].
$$

Small-angle position:

$$
y_p\approx\frac{p\lambda L}{a}.
$$

**Walkthrough**

1. Confirm the marked features are dark minima.
2. Count $p=1$ from the center to the first dark minimum.
3. Decide whether exact or small-angle geometry is appropriate.
4. Solve for $a$, $\lambda$, $L$, or $p$.

**Trap:** single-slit $p$ labels dark minima; double-slit/grating $m$ usually labels bright maxima.

### Family 21B: Slit width from adjacent minima

For small angles, neighboring minima are separated by

$$
\Delta y\approx\frac{\lambda L}{a}.
$$

Therefore,

$$
a\approx\frac{\lambda L}{\Delta y}.
$$

**Graph walkthrough:** measure positions relative to the central maximum; use two neighboring dark minima; do not confuse this regular minimum spacing with the full central bright width.

### Family 21C: Central-maximum width

The central maximum runs from the first minimum on one side to the first minimum on the other:

$$
W_{\rm central}=2y_1
\approx\frac{2\lambda L}{a}.
$$

**Walkthrough:** if given full width, halve it before using the first-minimum equation—or use the full-width formula directly.

**Scaling:** narrower slit, longer wavelength, or farther screen produces a wider diffraction pattern.

### Family 21D: Compare colors or find a separation

At the first minimum under the small-angle approximation,

$$
y_1\approx\frac{\lambda L}{a}.
$$

For two wavelengths,

$$
\Delta y\approx\frac{L(\lambda_2-\lambda_1)}{a}.
$$

Longer wavelength produces a wider pattern.

### Family 21E: Existence of a minimum

For the first minimum,

$$
\sin\theta_1=\frac{\lambda}{a}.
$$

A physical first minimum requires $a\ge\lambda$. If $a<\lambda$, the equation would require $\sin\theta>1$, so no first dark minimum occurs.

### Family 21F: Secondary bright fringe approximation

The course approximation places a secondary maximum halfway between adjacent dark minima. If $q=1$ denotes the first secondary maximum,

$$
y_{{\rm bright},q}\approx
\frac{(q+\tfrac12)\lambda L}{a}.
$$

Thus the second secondary bright fringe is approximately

$$
y_{{\rm bright},2}\approx\frac{2.5\lambda L}{a}.
$$

**Trap:** this $2.5$ coefficient is for the second secondary single-slit bright fringe under the lecture approximation; do not confuse it with the third dark double-slit path difference, which also happens to be $2.5\lambda$.

[Back to table of contents](#table-of-contents)

---

<a id="written-chains"></a>
# Multi-Step Written-Response Chains

Q1 P5, Q2 P4–P5, and Q3 P4–P5 each join two or more familiar moves. The chains below collect those tested combinations and related lecture/homework combinations.

## Chain A: Optics graph → geometry → wavelength or spacing

1. Identify double slit, grating, or single slit.
2. Read bright/dark order or graph spacing correctly.
3. Convert $y$ to $\theta$ with $\tan\theta=y/L$ if exact geometry is needed.
4. Apply $d\sin\theta=m\lambda$ or $a\sin\theta=p\lambda$.
5. Continue to line density, order count, central width, or qualitative scaling.

**Practice changes:** symmetric $+m$ to $-m$ separation; graph coordinates not centered at zero; a finite screen; a different requested variable; geometry that rules out the small-angle shortcut.

## Chain B: Statics → tension → string wave → oscillation amplitude

1. Extended FBD.
2. $\sum\tau=0$ and $\sum\vec F=0$.
3. $\mu=m/L_{\rm actual}$.
4. $v=\sqrt{T/\mu}$.
5. $f=v/\lambda$.
6. $A=u_{\max}/(2\pi f)$ if required.

## Chain C: Circular FBD → radial/tangential components → release

1. Choose inward radial positive.
2. Resolve real forces into $r,t$ components.
3. Find $a_r$, $a_t$, total acceleration, or $v^2=ra_r$.
4. At release, use tangent velocity.
5. Apply projectile kinematics or energy afterward.

## Chain D: Composite body → COM/inertia → rotational result

1. Locate the composite COM.
2. Measure the requested component's radius from that COM.
3. Use $v=\omega r$, or build $I$ with the parallel-axis theorem.
4. Continue with $K=\tfrac12I\omega^2$, $\sum\tau=I\alpha$, or $L=I\omega$.

## Chain E: Gravity geometry → orbital dynamics → period/energy

1. Establish center-based radius, pair separation, and COM radii separately.
2. Vector-sum gravity if more than one source acts.
3. Use gravity as the inward force.
4. Find speed or period.
5. Count all bodies for $K$ and all unique pairs for $U$.

## Chain F: SHM state → event → changed oscillator

1. Read $A,T,\phi$ or $x,v$.
2. Find the state at the event time.
3. Use momentum during a sticking collision.
4. Use energy after the collision for new amplitude.
5. Recompute period with the new mass.

## Chain G: Mechanical motion → Doppler shift

1. Find source/observer speed from free fall, energy, circular motion, or orbit mechanics.
2. Label the Doppler roles.
3. Predict high/low frequency.
4. Apply the correct moving-source or moving-observer equation.

---

<a id="final-checklist"></a>
# Final Error Checklist

## Setup and algebra

- [ ] Draw the diagram/FBD before choosing equations.
- [ ] Keep center-based radius, altitude, path length, and projected length distinct.
- [ ] Use a declared sign convention and retain signs through the algebra.
- [ ] Solve symbolically before substituting numbers.
- [ ] If an unprovided variable remains, identify the additional framework that creates it.
- [ ] Convert rpm, cm, mm, $\mu$m, and nm before substitution.
- [ ] Keep extra digits during intermediate steps; round only the final result.
- [ ] Check units and limiting behavior.

## Circular and rotational mechanics

- [ ] “Centripetal force” is the inward sum of real forces, not a new FBD arrow.
- [ ] At the bottom of a dip, inward is upward; at the top, inspect contact geometry.
- [ ] Set $N=0$ only at contact-loss threshold.
- [ ] Static friction equals $\mu_sN$ only at impending slip.
- [ ] Banked-curve friction opposes the impending sliding direction.
- [ ] Moment of inertia is always about a specified axis.
- [ ] Apply the parallel-axis theorem before adding/subtracting component inertias.
- [ ] A massive pulley generally has unequal tensions.
- [ ] Same rolling shape means mass and radius cancel from ideal speed/acceleration.
- [ ] Sticking conserves momentum/angular momentum during the impact, not mechanical energy.

## Gravity

- [ ] Gravitational force uses $1/r^2$; potential energy uses $1/r$.
- [ ] Count every unordered gravitational pair exactly once.
- [ ] Circular-orbit energy is $E=-GMm/(2r)$.
- [ ] In a binary, use separation $d$ and total mass $M+m$ for the period.
- [ ] Use COM radius for each body's speed, but pair separation for $U$.
- [ ] Geostationary altitude is $h=r-R$.

## Oscillations and waves

- [ ] SHM displacement is measured from equilibrium.
- [ ] Use radians in phase equations.
- [ ] Acceleration satisfies $a=-\omega^2x$; its direction is not determined by velocity.
- [ ] Ideal spring period is independent of amplitude.
- [ ] Physical-pendulum $I$ must be about the actual pivot.
- [ ] Wave propagation direction is not particle-motion direction.
- [ ] For a right-moving snapshot, particle velocity has the opposite sign from local slope.
- [ ] Use actual string length in $\mu=m/L$.
- [ ] Frequency remains constant across a stationary refractive boundary.
- [ ] Add intensities, not decibel values.
- [ ] Classify source/observer roles before choosing Doppler signs.
- [ ] Open–closed pipes contain odd harmonics only.
- [ ] Include initial phase in two-source interference.

## Wave optics

- [ ] Decide double slit, grating, or single slit before choosing the order rule.
- [ ] Use $d$ for slit/grating spacing, $a$ for single-slit width, and $L$ for screen distance.
- [ ] In exact geometry, $\tan\theta=y/L$; the optical equation uses $\sin\theta$.
- [ ] Halve a stated separation between $+m$ and $-m$.
- [ ] Count $m=0$ and both sides in a grating total.
- [ ] Apply both the physical-order and screen-edge limits.
- [ ] The third dark double-slit fringe has path difference $2.5\lambda$.
- [ ] Single-slit central width is $2y_1$.
- [ ] Narrower single slit means a wider diffraction pattern.
- [ ] If $a<\lambda$, a first single-slit minimum cannot exist.

## Final ten-second plausibility check

Ask:

1. Is the direction/sign physically sensible?
2. Is the answer expressed using the actual givens?
3. Do the units reduce correctly?
4. Does increasing the controlling parameter move the result the right way?
5. Did I accidentally use a memorized special-case formula with the wrong geometry?

[Back to table of contents](#table-of-contents)
