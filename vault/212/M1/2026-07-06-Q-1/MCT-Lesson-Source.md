# MCT Rotational Motion Lesson Source

This file defines the five-topic lesson sequence distilled from the three MCT video transcripts paired with the first rotational-motion lecture. Lesson 5 is intentionally divided into Parts A and B so each generated file keeps one equation-selection procedure.

## Shared Sources

- [Rotational Motion Physics transcript](<../2026-06-23-M1-00/Source/mct-Rotational Motion Physics, Basic Introduction, Angular Velocity & Tangential Acceleration/Rotational Motion Physics, Basic Introduction, Angular Velocity & Tangential Acceleration [WQ9AH2S8B6Y].en.srt>)
- [Angular Velocity Physics Problems transcript](<../2026-06-23-M1-00/Source/mct-Angular Velocity Physics Problems, Linear Speed, Frequency & Period/Angular Velocity Physics Problems, Linear Speed, Frequency & Period [d5VXZGinKSk].en.srt>)
- [Rotational Kinematics Physics Problems transcript](<../2026-06-23-M1-00/Source/mct-Rotational Kinematics Physics Problems, Basic Introduction, Equations & Formulas/Rotational Kinematics Physics Problems, Basic Introduction, Equations & Formulas [0El-DqrCTZM].en.srt>)

Use the transcripts as source material, but correct imprecise wording rather than repeating it. In particular:

- Radius is conventionally a length, not literally a quantity with units of meters per radian; the radian is dimensionless, although writing the conversion factor as $r\,\mathrm{m/rad}$ can help track units.
- Angular velocity carries a sign or direction; angular speed is its magnitude.
- $a_t=r\alpha$ gives tangential acceleration, not radial or total acceleration.
- Constant-angular-acceleration equations may be used only when $\alpha$ is constant.

Each generated lesson must follow the core-move-lesson structure: a fast recognition cue, minimal prerequisites, a canonical worked example, controlled variants, misconception-based radio practice with response-specific feedback, and a concise summary.

---

## Problem 1

### Lesson 1 — Angular Position, Displacement, and Average Angular Velocity

Target file: `Lessons/MCT-Problem-1.md`

Preserve the source-video worked problem in which a disk turns through $5000\,\mathrm{rad}$ in $10\,\mathrm{min}$, including the conversion to $600\,\mathrm{s}$ and the result $8.33\,\mathrm{rad/s}$. Label it as a source-video example, then add original mirrored practice.

Primary source segments:

- Rotational Motion Physics, 0:27–3:39.
- Angular Velocity Physics Problems, 7:51–8:55.

Core move: **Compute a rotating object's signed angular displacement or average angular velocity by identifying its initial angle, final angle, and elapsed time.**

Recognition cues:

- The prompt gives an initial and final angular position.
- The prompt describes an angle swept during a time interval.
- The requested result is angular displacement or average angular velocity.

Required content:

1. Distinguish angular position $\theta$ from angular displacement $\Delta\theta$.
2. Apply $\Delta\theta=\theta_f-\theta_i$ with a stated sign convention.
3. Apply $\omega_{\mathrm{avg}}=\Delta\theta/\Delta t$.
4. Interpret radians and radians per second correctly.
5. Include a controlled conversion between revolutions and radians using $1\,\mathrm{rev}=2\pi\,\mathrm{rad}$ when the displacement is reported in revolutions.

Keep instantaneous derivatives, constant-angular-acceleration equations, period/frequency, and tangential speed out of this lesson except for brief prerequisite links.

---

## Problem 2

### Lesson 2 — Connecting Angular and Linear Motion at a Radius

Target file: `Lessons/MCT-Problem-2.md`

Preserve the source-video worked examples for $7200\,\mathrm{rad}$ at $r=2\,\mathrm m$, $25\,\mathrm{rad/s}$ at $r=30\,\mathrm{cm}$, $8.33\,\mathrm{rad/s}$ with a $20\,\mathrm{cm}$ diameter, and the two-points-on-one-wheel comparison. Label them as source-video examples, then add original mirrored practice.

Primary source segments:

- Rotational Motion Physics, 3:40–5:49.
- Angular Velocity Physics Problems, 3:43–7:50 and 8:55–10:26.
- Rotational Kinematics Physics Problems, 3:24–4:08 and 6:03–7:33.

Core move: **Choose $s=r\theta$ or $v=r\omega$ to convert an angular amount or angular rate into the corresponding arc length or tangential speed at a specified radius.**

Recognition cues:

- A point lies at a stated distance from a rotation axis.
- The prompt pairs angle with arc length or angular speed with tangential speed.
- Two points share a rigid rotating object but lie at different radii.

Required content:

1. Build $s=r\theta$ from the radian definition and require $\theta$ in radians.
2. Use $v=r\omega$ in both forward and rearranged forms.
3. Compare two points on the same rigid body: common $\omega$, but $v$ proportional to $r$.
4. Convert diameter to radius and centimeters to meters before substitution.
5. Use units as a self-check without claiming that radius is intrinsically measured in meters per radian.

Do not turn this into a period/frequency lesson or an acceleration lesson.

---

## Problem 3

### Lesson 3 — Period, Frequency, and Angular Speed

Target file: `Lessons/MCT-Problem-3.md`

Preserve the source-video worked examples for a $30\,\mathrm{Hz}$ wheel, conversion of $8.33\,\mathrm{rad/s}$ to RPM, and the $45\,\mathrm{rpm}$, $1.4\,\mathrm m$ rim-speed conversion to miles per hour. Label them as source-video examples, then add original mirrored practice.

Primary source segments:

- Rotational Motion Physics, 5:50–7:22.
- Angular Velocity Physics Problems, 0:00–3:43 and 10:26–14:50.

Core move: **Translate cycle-based language into period, frequency, or angular speed and select the shortest relationship that connects the given quantity to the requested quantity.**

Recognition cues:

- “Time for one revolution” identifies the period $T$.
- “Cycles or revolutions per second” identifies the frequency $f$.
- “Radians per second” identifies angular speed $\omega$.
- RPM must be converted from revolutions per minute before using an SI result.

Required content:

1. Establish $T=t/N$ and $f=N/t$ from units before using $T=1/f$.
2. Connect one cycle to $2\pi$ radians and derive
   $$
   T=\frac1f,\qquad \omega=2\pi f,\qquad \omega=\frac{2\pi}{T}.
   $$
3. Translate short word problems into the correct equation before calculating.
4. Convert among Hz, RPM, rad/s, and period using cancellation factors.
5. Include reverse problems that ask for $T$ or $f$ from $\omega$.

The lesson may end with one mixed bridge to $v=r\omega$, but linear speed must not become its second instructional spine.

---

## Problem 4

### Lesson 4 — Radial, Tangential, and Net Acceleration

Target file: `Lessons/MCT-Problem-4.md`

Preserve the source-video vector-component illustration and the disk that changes from $20$ to $40\,\mathrm{rad/s}$ in $5\,\mathrm s$ at $r=0.30\,\mathrm m$. Label them as source-video examples, then add original mirrored practice.

Primary source segments:

- Rotational Motion Physics, 7:23–11:27.
- Rotational Kinematics Physics Problems, 14:24–15:51.

Core move: **Determine which perpendicular acceleration components are present in circular motion, calculate each component, and combine them when the speed changes.**

Recognition cues:

- Any motion along a curved circular path has inward radial acceleration.
- Changing speed adds tangential acceleration.
- A request for total acceleration requires a vector combination, not scalar addition.

Required content:

1. Compute average angular acceleration from $\alpha_{\mathrm{avg}}=\Delta\omega/\Delta t$.
2. Use $a_r=v^2/r=\omega^2r$ and point it toward the center.
3. Use $a_t=r\alpha$ and point it tangent to the path in the direction of increasing speed (opposite the velocity when slowing).
4. Distinguish uniform circular motion from nonuniform circular motion.
5. Combine perpendicular components with
   $$
   |\vec a|=\sqrt{a_r^2+a_t^2}
   $$
   and, when useful, determine the resultant direction.

Keep force diagrams and centripetal-force applications out of this kinematics lesson.

---

## Problem 5

### Lesson 5A — Constant Angular Acceleration When Time Is Known

Target file: `Lessons/MCT-Problem-5A.md`

Preserve the source-video equation mapping, the disk starting from rest with $\alpha=2.5\,\mathrm{rad/s^2}$ for $18\,\mathrm s$, and the disk changing from $20$ to $40\,\mathrm{rad/s}$ in $5\,\mathrm s$. Label them as source-video examples, then add original mirrored practice.

Primary source segments:

- Rotational Kinematics Physics Problems, 0:00–3:24 and 7:33–15:51.

Core move: **Select and apply a constant-angular-acceleration equation when the time interval is known by listing the available variables and choosing the equation containing the target.**

Recognition cues:

- The problem states or implies constant angular acceleration.
- Time is given or requested.
- The known/target list uses $\omega_i$, $\omega_f$, $\alpha$, $t$, and $\Delta\theta$.

Required content:

1. State the constant-$\alpha$ condition before presenting equations.
2. Map the familiar linear variables to rotational variables:
   $$
   x\leftrightarrow\theta,\qquad v\leftrightarrow\omega,\qquad a\leftrightarrow\alpha.
   $$
3. Solve final-speed problems with
   $$
   \omega_f=\omega_i+\alpha t.
   $$
4. Solve time-known displacement problems with
   $$
   \Delta\theta=\omega_i t+\frac12\alpha t^2.
   $$
5. Use
   $$
   \Delta\theta=\frac{\omega_i+\omega_f}{2}t
   $$
   when both endpoint angular velocities and time are known.
6. Interpret “starts from rest,” preserve signs for speeding up or slowing down, and convert radians to revolutions only after solving.

Do not use the no-time equation in this file except to point forward to Lesson 5B.

---

## Problem 6

### Lesson 5B — Constant Angular Acceleration When Time Is Missing

Target file: `Lessons/MCT-Problem-5B.md`

Preserve the complete source-video wheel problem with $80\,\mathrm{cm}$ diameter, $30\to80\,\mathrm{rad/s}$, and $a_t=15\,\mathrm{m/s^2}$, including its path through $r=0.400\,\mathrm m$, $\alpha=37.5\,\mathrm{rad/s^2}$, $\Delta\theta=73.33\,\mathrm{rad}$, and $11.67$ revolutions. Label it as a source-video example, then add original mirrored practice.

Primary source segment:

- Rotational Kinematics Physics Problems, 15:51–18:48.

Core move: **Recognize that time is absent, recover angular acceleration from linked rim data when necessary, and apply the constant-angular-acceleration equation that eliminates time.**

Recognition cues:

- The prompt gives $\omega_i$, $\omega_f$, and $\alpha$ or enough data to find $\alpha$.
- Angular displacement is requested but no time is supplied.
- A tangential rim acceleration and radius may be given in place of $\alpha$.

Required content:

1. Use the missing-time cue to select
   $$
   \omega_f^2=\omega_i^2+2\alpha\Delta\theta.
   $$
2. Rearrange symbolically for $\Delta\theta$ before substituting.
3. Recover $\alpha$ from $a_t=r\alpha$ when tangential acceleration and radius are supplied.
4. Handle negative $\alpha$ consistently for slowing rotation and check that the resulting displacement has a physically consistent sign.
5. Convert the final angular displacement from radians to revolutions when requested.
6. Use dimensional and magnitude checks to catch squaring, radius, and $2\pi$ errors.

Keep time-known equation selection in Lesson 5A; this file should repeatedly reinforce the single cue that time is absent.
