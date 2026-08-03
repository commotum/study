## Finding Maximum SHM Speed From a Position-Time Graph

To find maximum speed from a sinusoidal position-time graph:

1. Read $A$ from the equilibrium line to one extreme, not from trough to peak.
2. Read $T$ between consecutive maxima, consecutive minima, or another same-phase pair.
3. Use $\omega=2\pi/T$.
4. Compute $v_{\max}=A\omega=2\pi A/T$.
5. Preserve the graph's distance unit, divide by seconds, and round only the final value.

## Finding Instantaneous SHM Velocity From Cycle Data

For a block released from rest at maximum positive displacement:

1. Find amplitude from the setup: $A=|x_f-x_0|$.
2. Convert the cycle count to frequency: $f=N/\Delta t$.
3. Convert to angular frequency: $\omega=2\pi f$.
4. Use $x(t)=A\cos(\omega t)$ and $v(t)=-A\omega\sin(\omega t)$.
5. Evaluate in radian mode, keep guard digits, and round only the final result.
6. Interpret the velocity sign using the stated positive direction.

The main traps are treating $x_f$ as the amplitude, omitting $2\pi$ or the chain-rule factor $\omega$, and reporting speed instead of signed velocity.

## Ranking Acceleration Magnitudes from an SHM Position Graph

When a single SHM position graph asks for a ranking of acceleration magnitudes:

1. At each requested time, move vertically to the curve and read the signed position $x$.
2. Convert each position to its distance from equilibrium by taking $|x|$.
3. Rank those distances from least to greatest.
4. Use the same order for the acceleration magnitudes because $|a|=\omega^2|x|$.

Do not rank signed positions, and do not use the graph's slope. Equal distances on opposite sides of equilibrium produce equal acceleration magnitudes.

## Deciding Whether an SHM Oscillator Is Speeding Up or Slowing Down

When an SHM problem gives the signs of displacement and velocity and asks whether the oscillator is speeding up or slowing down:

1. Use $a=-\omega^2x$ to make the acceleration sign opposite the displacement sign.
2. Compare velocity with acceleration.
3. Same signs of $v$ and $a$ mean **speeding up**.
4. Opposite signs of $v$ and $a$ mean **slowing down**.

For nonzero $x$ and $v$, this also gives a quick check:

$$
xv<0 \Rightarrow \text{moving toward equilibrium and speeding up},
$$

$$
xv>0 \Rightarrow \text{moving away from equilibrium and slowing down}.
$$

The main trap is treating the sign of $x$ as the direction of motion. Position tells which side of equilibrium the oscillator occupies; velocity tells which way it moves.

## Speed of a Spring Oscillator at a Given Position

When an ideal, frictionless spring oscillator has amplitude $A$ and is observed at position $x$:

1. Freeze the system at the requested instant. An object that has not landed yet is not part of the oscillating mass.
2. Write $\frac12kA^2=\frac12Mv^2+\frac12kx^2$.
3. Solve for the nonnegative speed:

   $$
   v=\sqrt{\frac{k}{M}\left(A^2-x^2\right)}.
   $$

4. Square the entire position. If $x=rA$, then $x^2=r^2A^2$.
5. Do not attach a direction sign to speed; positions $x$ and $-x$ have the same speed.
6. Check the endpoints: $v=A\sqrt{k/M}$ at $x=0$ and $v=0$ at $|x|=A$.

## Deciding What Changes a Pendulum's Frequency

When a pendulum parameter changes:

1. Start with $f=\dfrac{1}{2\pi}\sqrt{\dfrac{g}{L}}$.
2. Check whether the changed parameter appears in the formula.
3. If it is absent, changing it alone does not change the frequency predicted by the model.
4. If it appears, translate its change factor through the square root or use the frequency ratio.

$$
\frac{f_2}{f_1}
=\sqrt{\frac{g_2}{g_1}\frac{L_1}{L_2}}.
$$

| Change | Frequency multiplier |
| --- | ---: |
| $m\to km$ | $1$ |
| $g\to kg$ | $\sqrt{k}$ |
| $L\to kL$ | $1/\sqrt{k}$ |

Mass is absent because the gravitational restoring force and the bob's inertia both scale with $m$ and cancel. The result assumes an ideal pendulum oscillating through small angles.

## Period of a Uniform Rod as a Physical Pendulum

1. Recognize a rigid body swinging through a small angle as a physical pendulum.
2. Use quantities measured from the pivot: $I=\frac13mL^2$ and $d=L/2$ for a uniform rod pivoted at one end.
3. Substitute symbolically, expose the common factors, and simplify to $T=2\pi\sqrt{2L/(3g)}$.
4. Check that mass cancels and the remaining units reduce to seconds.
5. Evaluate the radicand, take the square root, multiply by $2\pi$, and round only the final answer.

## Finding the Period of a Rod–Disk Physical Pendulum

For a rod–disk physical pendulum:

1. Locate the centers: $d_r=L/2$ and $d_d=L+r$.
2. Add pivot-axis inertias:

   - use an inertia formula unchanged if it is already about the pivot;
   - use $I_{\mathrm{pivot}}=I_{\mathrm{cm}}+Md^2$ if the known formula is about a parallel center-of-mass axis.

   $$
   I_{\mathrm{pivot}}
   =\frac13m_rL^2+\frac12m_dr^2+m_d(L+r)^2.
   $$

3. Add mass–distance terms:

   $$
   \sum m_id_i=m_r\left(\frac{L}{2}\right)+m_d(L+r).
   $$

4. Substitute into

   $$
   T=2\pi\sqrt{\frac{I_{\mathrm{pivot}}}{g\sum m_id_i}}
   $$

   Check that the radical has units of $\mathrm{s^2}$, then round only the final period.

**Main trap:** use squared distances in the parallel-axis inertia terms, but first-power distances in the gravitational torque terms.

## Inferring Particle Motion From a Traveling-Wave Snapshot

For a right-moving transverse wave:

1. Keep the marked particle at the same horizontal position.
2. Read the snapshot's local slope from left to right.
3. Reverse that sign to get the particle's vertical motion.

$$
\boxed{\text{positive slope}\to\text{down},\quad
\text{negative slope}\to\text{up},\quad
\text{zero slope}\to\text{momentary rest}}
$$

## Finding Wave Speed from a Traveling-Wave Equation

When a traveling wave is written as $y=A\sin(kx\pm\omega t+\phi)$ or with cosine:

1. Look inside the sine or cosine.
2. Read $k$ from the coefficient of $x$.
3. Read $\omega$ from the magnitude of the coefficient of $t$.
4. Compute $v=\omega/k$.
5. Check that $(\mathrm{rad/s})/(\mathrm{rad/m})$ simplifies to $\mathrm{m/s}$.

Do not use the amplitude, reverse the quotient, or let sine versus cosine or a constant phase shift distract you. The sign between the phase terms affects direction, not the speed's magnitude.

## Wave Speed in a Wire Tensioned by a Hanging Mass

For a stationary block tensioning a wire over a pulley:

1. Use $T=Mg$ for the tension.
2. Use $\mu=m_w/L$ for the wire's linear mass density.
3. Substitute into
   $$
   v=\sqrt{\frac{T}{\mu}}
   =\sqrt{\frac{MgL}{m_w}}.
   $$
4. Keep the quotient beneath the square root.
5. Check that the units reduce to $\mathrm{m/s}$.
6. Round only at the end and follow the requested answer format.

The main trap is swapping the hanging mass $M$, which sets tension, with the wire mass $m_w$, which sets linear density.

## Maximum Transverse Particle Speed on a Tensioned Wire

For a sinusoidal wave on a wire tensioned by a stationary hanging mass:

1. Compute $T=Mg$ and $\mu=m_w/L$.
2. Find $v_{\mathrm{wave}}=\sqrt{T/\mu}=\sqrt{MgL/m_w}$.
3. Use $\omega=2\pi v_{\mathrm{wave}}/\lambda$.
4. Find $v_{\mathrm{particle,max}}=A\omega=(2\pi A/\lambda)v_{\mathrm{wave}}$.
5. Keep $A$ and $\lambda$ in matching length units, retain unrounded intermediate values, and round only the final result.

The main trap is reporting $v_{\mathrm{wave}}$ instead of the maximum transverse particle speed.

## Deriving Wave Speed on a Load-Bearing Wire

This synthesis contains eight core moves:

1. Translate static into $\sum\vec F=0$ and, for the shelf, $\sum\tau=0$.
2. Isolate the block and derive $T_s=m_2g$.
3. Transfer the downward force $T_s$ to the shelf's extended FBD.
4. Choose the hinge as pivot and build every signed torque term.
5. Solve the torque equation for
   $$
   T=\frac{(m_1+2m_2)g}{2\sin\theta}.
   $$
   If the hinge reaction is requested, return to $\sum F_x=0$ and $\sum F_y=0$ after finding $T$; these give the components needed to reconstruct the single force $F_p$ and its direction.
6. Use the right triangle to derive
   $$
   L_w=\frac{L}{\cos\theta}.
   $$
7. Convert wire mass to
   $$
   \mu=\frac{m_w\cos\theta}{L}.
   $$
8. Substitute both derived inputs into $v=\sqrt{T/\mu}$.

The final result is

$$
\boxed{
v=\sqrt{
\frac{(m_1+2m_2)gL}
{2m_w\sin\theta\cos\theta}
}
}.
$$

On a graded page, show the following rather than writing only the boxed result:

- the block FBD and the shelf's labeled extended FBD;
- $0=T_s-m_2g$;
- the complete hinge-torque equation;
- the symbolic algebra leading to $T$;
- $\cos\theta=L/L_w$ and the derivation of $\mu$;
- the unsimplified substitution into $v=\sqrt{T/\mu}$;
- a unit check and numbers only at the end.

The main traps are confusing $T_s$ with $T$, forgetting that static means both force and torque balance for the shelf, putting $m_1g$ at $L$ instead of $L/2$, using $T\cos\theta$ instead of $T\sin\theta$ in the torque, and using shelf length instead of actual wire length in $\mu$.

## Locate a Listener on a Circular Wavefront

When two $x$-axis listeners detect the same circular wavefront simultaneously:

1. Find the source:
   $$
   x_s=\frac{x_1+x_2}{2}.
   $$
2. Find the radius $r$ from the source to either listener.
3. For a third listener at $(0,y)$, use
   $$
   y=\sqrt{r^2-|x_s|^2}.
   $$
4. Choose the positive square root for the positive $y$-axis.
5. Keep the exact radical until the final numerical approximation.
6. Round only the final coordinate and follow the requested answer format.

The main traps are mishandling the negative coordinate, using the full listener separation as the radius, and adding the squared legs instead of subtracting the known leg from $r^2$.

## Counting Wavelengths Inside a Material

Use the chain

$$
\boxed{\text{medium wavelength}\ \longrightarrow\ \text{matching units}\ \longrightarrow\ \text{count}\ \longrightarrow\ \text{final rounding}}.
$$

In symbols:

1. Find $\lambda_{\text{material}}=\lambda_{\text{air}}/n$.
2. Convert the thickness and wavelength to the same length unit.
3. Count with $N=d/\lambda_{\text{material}}$, or equivalently $N=nd/\lambda_{\text{air}}$.
4. Confirm that the length units cancel and that $n>1$ makes the in-material wavelength shorter.
5. Round only at the end and use the requested answer form.

## Scaling Wave Power and Intensity with Frequency and Amplitude

Use this decision routine:

1. For two sinusoidal waves in the same linear medium, write
   $$
   \frac{P_{\mathrm{avg},2}}{P_{\mathrm{avg},1}}
   =
   \left(\frac{f_2}{f_1}\right)^2
   \left(\frac{A_2}{A_1}\right)^2.
   $$
2. If the comparison area is unchanged, the intensity has the same ratio.
3. Square both the frequency ratio and the wave-amplitude ratio.
4. When solving backward, take the positive square root.
5. If surface area changes, apply
   $$
   I=\frac{P_{\mathrm{avg}}}{A_s}
   $$
   separately.

The main trap is confusing wave amplitude $A$ with surface area $A_s$. Wave amplitude is squared in the power scaling; surface area divides power in the definition of intensity.

## Finding Distance From Sound Intensity

When the same source has intensity measurements at two distances:

1. Pair the data as $(I_1,r_1)$ and $(I_2,r_2)$.
2. Predict the direction: lower intensity means greater distance; higher intensity means smaller distance.
3. Use $I_1r_1^2=I_2r_2^2$.
4. For an unknown second distance, calculate $r_2=r_1\sqrt{I_1/I_2}$.
5. Keep the positive root, round only at the end, and follow the requested answer format.

The main traps are reversing $I_1/I_2$, forgetting the square root, and reporting a negative or over-rounded distance.

## Convert an Intensity Ratio into a Decibel Change

When intensity changes from $I_1$ to $I_2$:

1. Translate the wording into the ratio $I_2/I_1$.
2. Compute $\Delta\beta=(10\ \mathrm{dB})\log_{10}(I_2/I_1)$.
3. If a new level is requested, use $\beta_2=\beta_1+\Delta\beta$.
4. Check the sign: increasing intensity gives $\Delta\beta>0$; decreasing intensity gives $\Delta\beta<0$.

Useful benchmarks are

$$
\boxed{
2\times I\ \longrightarrow\ +3\ \mathrm{dB},
\qquad
10\times I\ \longrightarrow\ +10\ \mathrm{dB}
}.
$$

The main trap is treating the decibel scale as linear. Doubling intensity adds about $3\ \mathrm{dB}$; it does not double the intensity level.

## Doppler Shift for a Moving Observer

For a stationary sound source and a moving observer:

1. Label $f_0$ as the emitted frequency, $f'$ as the heard frequency, $c_s$ as sound speed, and $v_o$ as the positive line-of-sight observer speed.
2. Use
   $$
   f'=f_0\left(1\pm\frac{v_o}{c_s}\right).
   $$
3. Choose plus for motion toward the source and minus for motion away.
4. Evaluate the unitless factor $1\pm v_o/c_s$ before multiplying by $f_0$.
5. Check the direction: toward means $f'>f_0$; away means $f'<f_0$.
6. Round only the final frequency and follow the requested answer format.

The main traps are treating observer motion as source motion, choosing the wrong sign, and rounding before the final step.

## Extreme Doppler Frequencies from a Rotating Source

For a rotating sound source and a stationary listener:

1. Convert rpm to hertz: $f_{\mathrm{rot}}=\mathrm{rpm}/60$.
2. Find source speed: $v_s=2\pi Lf_{\mathrm{rot}}$.
3. Use toward motion for the highest frequency: $f_{\mathrm{high}}=f_0v/(v-v_s)$.
4. Use away motion for the lowest frequency: $f_{\mathrm{low}}=f_0v/(v+v_s)$.
5. Check that $f_{\mathrm{high}}>f_0>f_{\mathrm{low}}$.

The main traps are treating rpm as hertz, omitting $2\pi$, and swapping the Doppler signs.

## Largest Displacement When Two Pulses Overlap

When two pulses overlap, use this checklist:

- **Cue:** two pulses occupy the same string and pass through one another.
- **Read:** take signed heights from the vertical axis; do not use horizontal peak locations or travel arrows as displacement signs.
- **Combine:** add displacements at the same point, $y_{\text{net}}=y_1+y_2$.
- **Maximize:** for two upward pulses, align their peaks and add the two positive peak heights.
- **Report:** give the maximum vertical value, not its location, and follow the requested units and number format.

The governing equation is

$$
y_{\text{net}}=y_1+y_2.
$$

For the given pulses,

$$
1.2\ \mathrm{cm}+1.8\ \mathrm{cm}=3.0\ \mathrm{cm},
$$

so the number-only entry is **$3.0$**.

## Reflections at Fixed and Free Ends

Use this boundary check:

1. Identify the end before looking at the pulse orientation.
2. At a **fixed/hard end**, flip the displacement and assign a phase shift of $\pi$.
3. At a **free/soft end**, preserve the displacement and assign a phase shift of $0$.
4. In both cases, the reflected pulse reverses its travel direction.
5. Do not apply these two rules to a junction between different media; detailed reflection and transmission there are excluded.

The main trap is confusing reversal of travel direction with inversion. Every reflected pulse travels back, but only a fixed-end reflection flips upward to downward or downward to upward.

## Third-Harmonic Frequency of a Wire Tensioned by a Hanging Mass

For a fixed-end wire tensioned by a stationary hanging mass:

1. Read $L$ and $M$ from the diagram and $m_w$ from the prompt.
2. Compute $T=Mg$ and $\mu=m_w/L$.
3. Compute $v=\sqrt{T/\mu}$, then use $f_n=nv/(2L)$ with the requested harmonic number.
4. Check that the units reduce to hertz and that $f_n=nf_1$.
5. Keep unrounded intermediate values, then round the final frequency and follow the requested answer format.

The main trap is using the wrong mass: $M$ determines tension, while $m_w$ determines linear density.

## Matching Fundamental Frequencies of Open and Closed Tubes

When two tubes in the same medium have equal fundamental frequencies:

1. Identify the end conditions.
2. Write $f_{\mathrm{oo}}=v/(2\ell_{\mathrm{oo}})$ and $f_{\mathrm{co}}=v/(4\ell_{\mathrm{co}})$.
3. Set the frequencies equal and cancel the common wave speed.
4. Solve to get

$$
\boxed{\ell_{\mathrm{co}}=\frac{\ell_{\mathrm{oo}}}{2}}.
$$

In ratio form, $\ell_{\mathrm{co}}:\ell_{\mathrm{oo}}=1:2$. The main trap is setting the physical lengths equal. Equal frequency and equal wave speed give the same wavelength, but the two boundary conditions fit different fractions of that wavelength into the tubes.

## Third Harmonic of an Open–Closed Pipe

For an open–closed pipe, displacement is a node at the closed end and an antinode at the open end. The third-harmonic pattern is N–A–N–A, so three quarter wavelengths fit in the pipe:

$$
L=\frac{3\lambda_3}{4},
\qquad
\lambda_3=\frac{4L}{3},
\qquad
f_3=\frac{3v}{4L}.
$$

The reusable procedure is:

1. Mark a displacement node at the closed end and an antinode at the open end.
2. Draw N–A–N–A and count three quarter-wavelength intervals.
3. Write $L=3\lambda_3/4$, then use $f_3=v/\lambda_3=3v/(4L)$.
4. Check that the units reduce to hertz and that increasing $L$ would decrease $f_3$.
5. Keep full calculator precision and round only the reported answer.

The main trap is using the fundamental relation $L=\lambda/4$ for the third harmonic. For the assigned values, the unrounded result is $302.647\ldots\ \mathrm{Hz}$ and the required number-only answer is $300$.

## Finding Complete Constructive Interference in a Crest Diagram

For a diagram in which the circles represent crests, use **trace → label → compare**:

1. **Trace** each circle to its source family.
2. **Label** each source's phase at the point: on a circle is a crest; halfway between adjacent circles is a trough.
3. **Compare** the phases: crest–crest and trough–trough are constructive; crest–trough is destructive.

The main trap is treating drawn crest-circle intersections as the only constructive locations. In the assigned diagram, $P$ is crest–crest and $R$ is trough–trough, so both are constructive; $Q$ is crest–trough and is destructive.

## Classifying Two-Source Interference from Path and Starting Phase

When two sources interfere at a point:

1. Find both path lengths.
2. Compute $\Delta r=|r_B-r_A|$.
3. Convert the path difference with
   $$
   \Delta\phi_{\text{path}}=2\pi\frac{\Delta r}{\lambda}.
   $$
4. Add the initial phase difference: $0$ for in-phase sources or $\pi$ for completely out-of-phase sources.
5. Reduce to $[0,2\pi)$ by subtracting whole multiples of $2\pi$:
   - remainder $0$: completely constructive,
   - remainder $\pi$: completely destructive,
   - any other remainder: neither.

The main trap is ignoring the initial phase. A half-integer path difference reverses the usual result when the sources begin completely out of phase.

## Finding the First Constructive-Interference Point

For two in-phase sources and a listener on the positive $x$-axis:

1. Compute $\lambda=v/f$.
2. Write $\Delta r=\sqrt{x^2+d^2}-x$.
3. Notice that $\Delta r$ starts at $d$ and decreases as $x$ increases.
4. Choose the largest integer order with $m\lambda<d$. Equivalently, use $m=\lfloor d/\lambda\rfloor$ unless $d/\lambda$ is an integer, in which case use one order lower.
5. Set $L=m\lambda$, solve $x=(d^2-L^2)/(2L)$, require $x>0$, and check the result in the original path-difference equation.

The main trap is choosing the next higher integer multiple of $\lambda$. That value cannot be reached because the path difference decreases as the listener moves right.
