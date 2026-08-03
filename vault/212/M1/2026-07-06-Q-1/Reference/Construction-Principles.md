# Construction Principles

The cheat sheet can be reconstructed as:

> Lecture takeaway equations → repeatedly exercised relationships → expensive symbolic endpoints → one-page compression

It was probably not produced by simply counting formulas in the homework. The lecture summaries appear to be the primary source; quizzes and homework then determined which formulas were worth retaining.

One limitation: the file is currently untracked, so there is no Git history showing its actual creation sequence. What follows is a forensic reconstruction from content alignment.

## Governing Constraints

The lecture sequence establishes the intended workflow:

- Students create their own equation sheets, which may contain equations, diagrams, labels, and notes: [[212/M1/2026-06-23-M1-00/Source/Lecture-Notes|M1-00 Lecture Notes]].
- The Quiz 1 note sheet must be handwritten and between half a page and one page: [[212/M1/2026-07-02-M1-5/Source/Lecture-Notes|M1-5 Lecture Notes]].
- Students are told to emphasize symbolic setup rather than early numerical substitution: [[212/M1/2026-06-29-M1-3/Source/Lecture-Notes|M1-3 Lecture Notes]].
- Quiz questions are described as class examples modified by approximately one step: [[212/M1/2026-07-02-M1-5/Source/Lecture-Notes|M1-5 Lecture Notes]].

Those constraints explain the cheat sheet’s peculiar form: complete symbolic equations, almost no prose, and several formulas copied from the endpoint of lecture derivations.

## Equation-by-Equation Reconstruction

### 1. Angular Derivative and Integral Chain

$$
\omega=\frac{d\theta}{dt},\qquad
\alpha=\frac{d\omega}{dt},\qquad
\theta=\int \omega\,dt,\qquad
\omega=\int \alpha\,dt
$$

This is the first row of [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

**Where it originates**

- Introduced explicitly in [[212/M1/2026-06-23-M1-00/Source/Lecture-Notes|M1-00 Lecture Notes]] as angular derivatives and inverse integrals.
- Repeated almost verbatim in [[212/M1/2026-06-24-M1-1/Source/Lecture-Notes|M1-1 Lecture Notes]].
- Reviewed again immediately before Quiz 1 in [[212/M1/2026-07-02-M1-5/Source/Lecture-Notes|M1-5 Lecture Notes]].

**Assessment appearances**

- [[2026-06-23-M1-00]] P1 finds when $\omega(t)$ reaches zero; P2 integrates $\omega(t)$ to obtain angular displacement.
- [[2026-06-25-M1-2]] PRE P1 differentiates a given $\theta(t)$ to find angular speed.
- [[2026-06-25-M1-2]] LEC P7 again integrates angular velocity until reversal.
- [[2026-06-28-HW-1]] P4 integrates $\alpha(t)$ to get $\omega(t)$; P5 integrates again to get $\theta(t)$.
- [[2026-06-28-HW-1]] P14 and P15 ask for angular-velocity and angular-acceleration graphs corresponding to an angular-position graph.

**Why included:** this is the operator grammar of rotational kinematics. It generates many answers rather than solving only one scenario.

---

### 2. Linear–Angular Conversion Chain

$$
s=r\theta,\qquad v=r\omega,\qquad a_t=r\alpha
$$

This row in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]] is copied directly from the first lecture’s main physics takeaways in [[212/M1/2026-06-23-M1-00/Source/Lecture-Notes|M1-00 Lecture Notes]].

**Assessment appearances**

- The [[2026-06-25-M1-2]] rotating-disk/bullet sequence uses the parallel relationships $d=v\Delta t$ and $\theta=\omega\Delta t$ across P2–P5.
- [[2026-06-29-M1-3]] LEC P2 directly asks for Ferris-wheel rim speed from $r$ and $\omega$.
- [[2026-06-28-HW-1]] P8 asks whether $v=r\omega$; P12 checks the same relation in nonuniform circular motion.
- [[212/M1/2026-07-06-Q-1/2026-07-06-Q-1|Quiz 1]] version 1B’s greyhound-and-spool problem requires finding linear distance from $v(t)$, then converting that unwound distance into spool angle and revolutions using $s=r\theta$.

**Why included:** these three equations are the conversion bridge between ordinary motion and rotational motion. They also cover Quiz 1B with very little space.

---

### 3. Constant-Angular-Acceleration Equations

$$
\omega_f=\omega_0+\alpha t
$$

$$
\theta_f=\theta_0+\omega_0t+\frac12\alpha t^2
$$

$$
\omega_f^2=\omega_0^2+2\alpha\Delta\theta
$$

These appear as a complete family in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

**Where they originate**

- Introduced together in [[212/M1/2026-06-23-M1-00/Source/Lecture-Notes|M1-00 Lecture Notes]].
- Repeated in [[212/M1/2026-06-24-M1-1/Source/Lecture-Notes|M1-1 Lecture Notes]].
- Reviewed again in [[212/M1/2026-06-29-M1-3/Source/Lecture-Notes|M1-3 Lecture Notes]] and immediately before Quiz 1 in [[212/M1/2026-07-02-M1-5/Source/Lecture-Notes|M1-5 Lecture Notes]].

**Assessment appearances**

- [[2026-06-24-M1-1]] LEC P2 uses $\omega_f=\omega_0+\alpha t$ to find stopping acceleration.
- [[2026-06-24-M1-1]] LEC P4 uses the no-time equation to find angular displacement before stopping.
- [[212/M1/2026-06-24-M1-1/Source/Lecture-Notes|M1-1 Lecture Notes]] explicitly select $\omega_f^2=\omega_0^2+2\alpha\Delta\theta$ for that problem.

**Why included:** even though later homework emphasizes variable acceleration and calculus, the three equations form a standard decision set. Preserving the complete family lets the user choose based on which variable is missing.

---

### 4. Translational–Rotational Analogy

$$
x\leftrightarrow\theta,\qquad
v\leftrightarrow\omega,\qquad
a\leftrightarrow\alpha
$$

This is not a computational equation. It is a transfer rule in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

It appears explicitly in the concluding summaries of [[212/M1/2026-06-23-M1-00/Source/Lecture-Notes|M1-00 Lecture Notes]] and [[212/M1/2026-06-24-M1-1/Source/Lecture-Notes|M1-1 Lecture Notes]].

It supports:

- Translating known Physics 211 kinematics into rotational form.
- HW1 derivative, integral, and graph questions.
- The rotating-disk/bullet problem, which runs translational and rotational equations in parallel.
- Quiz 1B, where the sheet does not list $x=\int v\,dt$, but expects the user to infer it from $\theta=\int\omega\,dt$ and this correspondence.

**Why included:** it replaces several additional translational equations. This is one of the sheet’s most efficient compression devices.

---

### 5. Radial, Tangential, and Total Acceleration

$$
a_r=\frac{v^2}{r}=r\omega^2,\qquad
a_t=\frac{dv}{dt}=r\alpha,\qquad
|\vec a|=\sqrt{a_r^2+a_t^2}
$$

This is the conceptual center of the module in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

**Where it originates**

- $a_r=v^2/r$ is derived from the changing velocity vector in [[212/M1/2026-06-25-M1-2/Source/Lecture-Notes|M1-2 Lecture Notes]].
- $a_r=r\omega^2$ follows by substituting $v=r\omega$.
- Total acceleration is introduced for nonuniform circular motion.
- $a_t=dv/dt=r\alpha$ is reviewed immediately before Quiz 1 in [[212/M1/2026-07-02-M1-5/Source/Lecture-Notes|M1-5 Lecture Notes]].

**Assessment appearances**

- [[2026-06-25-M1-2]] LEC P6 ranks radial accelerations.
- [[2026-06-28-HW-1]] P9 states the exact identity $v^2/r=\omega^2r$.
- [[2026-06-28-HW-1]] P11 and P13 test nonuniform acceleration direction and radial-plus-tangential composition.
- [[2026-07-02-M1-5]] PRE/LEC P1–P5 progress from net-force direction to $a_r$, $a_t$, and total acceleration.
- [[2026-07-05-PQ-1]] P1 and P2 test radial-acceleration magnitude and net-force direction.
- [[212/M1/2026-07-06-Q-1/2026-07-06-Q-1|Quiz 1]] version 1A Q1 tests uniform-circular-motion acceleration; Q4 asks for total acceleration.

**Why included:** this row alone covers most conceptual and quantitative circular-motion questions.

---

### 6. Frequency, Period, Angular Speed, and Orbital Speed

$$
f=\frac1T,\qquad
\omega=2\pi f=\frac{2\pi}{T},\qquad
v=\frac{2\pi r}{T}
$$

This row appears in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

**Where it originates**

- The full $f$–$T$–$\omega$ chain appears in the rotating-disk lecture: [[212/M1/2026-06-25-M1-2/Source/Lecture-Notes|M1-2 Lecture Notes]].
- $v=2\pi r/T$ is then stated in the M1-3 review: [[212/M1/2026-06-29-M1-3/Source/Lecture-Notes|M1-3 Lecture Notes]].

**Assessment appearances**

- [[2026-06-24-M1-1]] PRE P1 converts revolutions per second to radians per second.
- [[2026-06-25-M1-2]] LEC P2–P5 use period in the rotating-disk/bullet sequence.
- [[2026-06-28-HW-1]] P1 converts rpm to rad/s.
- [[2026-07-03-HW-2]] P1 uses constant period to identify uniform circular motion; P3 asks for centripetal force using radius and period; P5 uses period in a conical-pendulum derivation.
- [[2026-07-05-PQ-1]] P4 asks for a limiting turntable period; P5 asks for orbital period.

**Why included:** it is another conversion hub. It links language such as rpm, frequency, period, and one revolution to the variables used in the force equations.

---

### 7. Newton’s Second Law in Circular Coordinates

$$
\sum F_r=ma_r=m\frac{v^2}{r}=m\omega^2r,\qquad
\sum F_t=ma_t
$$

This is the master setup equation for the second half of the module.

It is:

- Previewed at the end of M1-2.
- Used throughout the Ferris-wheel and turntable lecture.
- Used for flat and banked curves.
- Used for conical pendulums.
- Used for vertical-circle motion.

The final instructions in [[212/M1/2026-06-29-M1-3/Source/Lecture-Notes|M1-3 Lecture Notes]] are essentially: draw the free-body diagram, point $+r$ inward, write $\sum F_r=ma_r$, and substitute $a_r=v^2/r=\omega^2r$.

**Assessment appearances**

- [[2026-06-29-M1-3]] P1 and P3–P6.
- [[2026-06-30-M1-4]] P2–P7.
- [[2026-07-02-M1-5]] P1–P5.
- [[2026-07-03-HW-2]] P3–P13.
- [[2026-07-05-PQ-1]] P2–P5.
- [[212/M1/2026-07-06-Q-1/2026-07-06-Q-1|Quiz 1]] version 1A Q2–Q4.

**Why included:** it is the generative force template. Most later scenario formulas can be reconstructed from this row plus a free-body diagram.

---

### 8. Static Friction, Flat Curves, and Turntables

$$
f_{s,\max}=\mu_sN,\qquad
\mu_{s,\text{flat}}=\frac{v^2}{rg},\qquad
\omega_{\max,\text{turntable}}=\sqrt{\frac{\mu_sg}{r}}
$$

This row contains one general law and two derived endpoints.

**Where it originates**

- The turntable derivation in [[212/M1/2026-06-29-M1-3/Source/Lecture-Notes|M1-3 Lecture Notes]]: friction supplies radial force, reaches $\mu_sN$, and yields the critical $\omega$.
- The flat-curve derivation in [[212/M1/2026-06-30-M1-4/Source/Lecture-Notes|M1-4 Lecture Notes]] yields $\mu_s=v^2/(rg)$.

**Assessment appearances**

- [[2026-06-29-M1-3]] LEC P6 asks for the turntable slipping threshold.
- [[2026-06-30-M1-4]] LEC P3 asks for the required flat-curve coefficient.
- [[2026-06-30-M1-4]] P5–P6 extend the same friction law to a bank.
- [[2026-07-05-PQ-1]] P4 asks for minimum period before a coin slips, which is a period-form variant of the turntable equation.

**Why included:** the row preserves both the reusable law and the two likely final-answer forms. This eliminates repeated threshold algebra under exam pressure.

---

### 9. Banked Curves

$$
v_{\text{banked}}=\sqrt{rg\tan\theta}
$$

$$
v_{\max,\text{banked}}=
\sqrt{
rg\frac{\sin\theta+\mu_s\cos\theta}
{\cos\theta-\mu_s\sin\theta}
}
$$

These formulas appear in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

**Where they originate**

- The frictionless formula is derived from $N\cos\theta=mg$ and $N\sin\theta=mv^2/r$ in [[212/M1/2026-06-30-M1-4/Source/Lecture-Notes|M1-4 Lecture Notes]].
- The maximum-speed expression is the endpoint of a much longer friction-component derivation in the same lecture.

**Assessment appearances**

- [[2026-06-30-M1-4]] P1 tests the free-body diagram.
- [[2026-06-30-M1-4]] P4 asks for the no-friction speed.
- [[2026-06-30-M1-4]] P5 asks for friction direction.
- [[2026-06-30-M1-4]] P6 asks for the maximum speed.
- [[2026-07-03-HW-2]] P6–P9 repeatedly test banked-track force components, friction magnitude, and friction direction.

**Why included:** the no-friction formula is common; the frictional formula is algebraically expensive and sign-sensitive. The latter is exactly the kind of endpoint worth storing rather than re-deriving during a timed quiz.

---

### 10–11. Normal Force at the Top and Bottom

$$
N_{\mathrm{top}}=
m\left(g-\frac{v^2}{r}\right)
=m(g-\omega^2r)
$$

$$
N_{\mathrm{bottom}}=
m\left(g+\frac{v^2}{r}\right)
=m(g+\omega^2r)
$$

These occupy separate rows in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

**Where they originate**

- Fully derived, including sign conventions, in [[212/M1/2026-06-29-M1-3/Source/Lecture-Notes|M1-3 Lecture Notes]].
- Repeated in M1-3’s final takeaways.

**Assessment appearances**

- [[2026-06-29-M1-3]] PRE P1 compares the top and bottom.
- [[2026-06-29-M1-3]] LEC P3 compares them; P4 calculates the bottom; P5 calculates the top.
- [[2026-07-05-PQ-1]] P3 asks whether $N$ is greater than or less than $mg$ at the top of a hill.
- [[2026-07-03-HW-2]] P10–P13 use variants involving loop contact and loss of normal force.
- [[212/M1/2026-07-06-Q-1/2026-07-06-Q-1|Quiz 1]] version 1A Q2 asks for the net-force direction at the bottom of a circular dip.

**Why included:** the plus/minus distinction is a notorious error point. Giving the two cases separate rows makes the spatial cue—top versus bottom—immediately visible.

---

### 12. Conical Pendulum

$$
T\cos\theta=mg,\qquad
T\sin\theta=m\frac{v^2}{r}
$$

This row appears in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

**Where it originates**

- Derived directly from the conical-pendulum free-body diagram in [[212/M1/2026-06-30-M1-4/Source/Lecture-Notes|M1-4 Lecture Notes]].
- [[2026-06-30-M1-4]] P7 asks the student to identify that free-body diagram.

**Assessment appearances**

- [[2026-07-03-HW-2]] P1–P5 form a five-question conical-pendulum sequence: uniform motion, radius geometry, centripetal force, net-force direction, and symbolic angle.
- [[2026-07-05-PQ-1]] P5’s bead on an inverted cone has the same structure: one angled support force supplies vertical balance and radial force.
- [[212/M1/2026-07-06-Q-1/2026-07-06-Q-1|Quiz 1]] version 1A Q3 asks for the free-body diagram of a bead held at an angle on a spinning loop.

**Why included:** the two component equations are more flexible than a single solved formula. They can generate tension, angle, speed, period, or radius depending on what the question asks.

**Caveat:** HW2 defines its angle from the horizontal, while the lecture conical-pendulum equations use an angle from the vertical. The sheet assumes the student notices the diagram’s angle convention and swaps sine/cosine when necessary.

---

### 13. Ball on a Vertical String

$$
a_r=\frac{T_{\text{tens}}}{m}+g\cos\theta,\qquad
a_t=g\sin\theta,\qquad
|\vec a|=\sqrt{a_r^2+a_t^2}
$$

This row appears in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

**Where it originates**

- Derived step by step in [[212/M1/2026-07-02-M1-5/Source/Lecture-Notes|M1-5 Lecture Notes]] from radial and tangential force components.
- Repeated in that lecture’s main physics takeaways.

**Assessment appearances**

- [[2026-07-02-M1-5]] LEC P3 asks for $a_r$.
- [[2026-07-02-M1-5]] LEC P4 asks for $a_t$.
- [[2026-07-02-M1-5]] LEC P5 asks for total acceleration.
- [[2026-07-03-HW-2]] loop-the-loop problems use the same radial-force logic in special positions.
- [[212/M1/2026-07-06-Q-1/2026-07-06-Q-1|Quiz 1]] version 1A Q4 asks for the key’s total acceleration and angular speed from its tension, mass, angle, and string length.

**Why included:** this row is extremely closely aligned with the actual long written quiz question. It is probably the strongest example of a class-example template being selected for the sheet.

---

### 14. Projectile Motion After Release

$$
\Delta y_{\max}
=\frac{v_{0y}^2}{2g}
=\frac{v_0^2\sin^2\theta}{2g},
\qquad
v_{0y}=v_0\sin\theta
$$

This final row appears in [[212/M1/2026-07-06-Q-1/Cheat-Sheet]].

**Where it originates**

- The final M1-5 lecture example cuts the string and turns the circular-motion object into a projectile.
- [[212/M1/2026-07-02-M1-5/Source/Lecture-Notes|M1-5 Lecture Notes]] derive the vertical component and maximum-height equation exactly as written on the sheet.
- [[2026-07-02-M1-5]] LEC P6 asks for the release height using the radial-force result from the preceding questions.

**Why included:** it is the endpoint of the last major worked example before Quiz 1. The actual recorded quiz does not use it, but the instructor explicitly warns that quiz questions may modify class examples by one step. This looks like insurance against an alternate version of the vertical-string problem.

## How Well the Sheet Predicts the Actual Quiz

The alignment is striking:

| Quiz problem | Cheat-sheet support |
|---|---|
| 1A Q1: acceleration in uniform circular motion | $a_r=v^2/r$; radial-versus-tangential distinction |
| 1A Q2: net force at bottom of dip | $\sum F_r=ma_r$; bottom normal-force template |
| 1A Q3: bead on spinning loop FBD | Conical-pendulum component model |
| 1A Q4: vertical key, total acceleration and angular speed | Vertical-string row plus $a_r=v^2/r$ |
| 1B Q1: greyhound unwinds spool | Derivative/integral analogy plus $s=r\theta$ |

This does not prove that the sheet was written after seeing the quiz—the files have no usable history—but it shows that it was very well targeted to the course’s announced quiz archetypes.

## What Was Deliberately Excluded

The omissions reveal that the sheet was not intended to be comprehensive.

### Right-Hand Rule and Cross Products

The lecture explicitly includes:

$$
\vec v=\vec\omega\times\vec r
$$

It even repeats this relationship in the [[212/M1/2026-06-24-M1-1/Source/Lecture-Notes|M1-1 Lecture Notes]] summary, but it is absent from the cheat sheet.

**Likely reason:** the quiz questions use diagrammatic direction reasoning rather than vector-component cross-product calculations. The author expects the right-hand rule to be remembered.

### General Translational Kinematics

The lecture reviews the full $x$–$v$–$a$ constant-acceleration family, but the sheet only includes rotational kinematics and one projectile-height formula.

**Likely reason:** translational kinematics is Physics 211 prerequisite knowledge. The correspondence row lets the user reconstruct it without spending space duplicating equations.

### Energy Conservation and Loop-the-Loop Formulas

[[2026-07-03-HW-2]] explicitly tests:

- Conservation of mechanical energy.
- $N=0$ at contact loss.
- Minimum loop-entry speed $\sqrt{5gr}$.
- The igloo critical-angle calculation.

None of these appears explicitly on the sheet.

This is important evidence: homework frequency alone did not determine inclusion. These were probably omitted because:

- Energy conservation was considered prerequisite knowledge.
- The special final answers are derivable from energy plus $\sum F_r=ma_r$.
- They did not match the principal Quiz 1 class-example set as closely as the vertical-string problem did.

### Free-Body Diagrams and Sign Conventions

The instructor repeatedly emphasizes diagrams, radial axes, and sign choices. The sheet has none.

That means the author chose to spend the one-page allowance on equations and assumed the user could reconstruct diagrams and signs from memory.

### Units, Definitions, and Verbal Conditions

The sheet omits:

- Radians-versus-revolutions conversion labels.
- Units.
- Constant-$\alpha$ conditions.
- Inward-positive conventions.
- Friction direction rules.
- Angle-definition warnings.
- Cases where normal force becomes zero.

Again, it assumes conceptual familiarity and uses the sheet only for retrieval.

## Most Likely Construction Process

The evidence suggests this sequence:

1. **Start with early lecture summaries.** The first several rows closely reproduce the main physics takeaways from M1-00 and M1-1.
2. **Add the general circular-motion backbone.** Include radial/tangential acceleration, period conversions, and Newton’s second law in $r$–$t$ coordinates.
3. **Extract symbolic endpoints from each later lecture.** Ferris-wheel normal forces, turntable threshold, banked-curve speeds, conical-pendulum components, vertical-string acceleration, and release height all come directly from worked lecture derivations.
4. **Check against PRE/LEC questions and homework.** Repeatedly exercised relationships are retained; question-specific numbers and intermediate algebra are discarded.
5. **Prioritize class examples likely to receive a one-step quiz modification.** The vertical-string and projectile rows strongly reflect the instructor’s quiz-preparation advice.
6. **Compress to the one-page constraint.** Chain equivalent forms with equals signs, use subscripts as labels, remove prose, and avoid duplicating formulas that can be reconstructed through the analogy row.
7. **Assume prior conceptual competence.** Omit diagrams, units, sign conventions, energy formulas, and applicability conditions.

So the cheat sheet was probably made less by asking, “What formulas appeared most often?” and more by asking:

> What compact set of equations will let me reconstruct the symbolic setup for every major class-example archetype likely to appear on Quiz 1?
