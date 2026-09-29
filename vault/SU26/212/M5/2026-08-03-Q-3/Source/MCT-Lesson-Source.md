# MCT Q3 Lesson Source Specification

This file defines the canonical 19-file MCT lesson sequence for Quiz 3. In course order, it moves from M4 simple harmonic motion and pendulums through M5 traveling waves, string speed, intensity, refraction, decibels, Doppler shift, beats, and standing waves. Coverage is limited to the 11 attachment-selected videos and their six paired lecture notes. Duplicate treatments are merged so each lesson owns one reusable decision.

## Scope and method

- Scope is exactly the 11 attachment videos listed below. No `Video-Matches` JSON was used, and no unassigned video was added.
- Every listed SRT was read from beginning to end. Repeating auto-caption cues were normalized into chronological spoken text while retaining cue start times.
- The corresponding six `Source/Lecture-Notes.md` files were read completely.
- When captions depended on an unseen drawing or garbled a value, the matching MP4 was checked at the relevant timestamp. Checks include the $0.40\,\mathrm{kg}$ SHM block, the $0.75\,\mathrm{kg}$ SHM equation prompt, the $0.75\,\mathrm{kg/m}$ string, the rectangular Snell-law geometry, and the first beat-frequency prompt.
- M5-5 has no attachment-selected video. It intentionally contributes no MCT lesson; no content is inferred or invented for it.
- Each target below names one operational decision, preserves every assigned source-video problem as a worked example or controlled variant, and routes overview-only material into brief context rather than standalone lessons.

## Counts

| Lecture label | Exact videos read | Target lessons | Notes |
|---|---:|---:|---|
| M4-1 | 1 | 4 | Spring force/work, energy states, frequency scaling, SHM functions |
| M4-2 | 2 | 2 | Simple and physical pendulums |
| M5-1 | 2 | 4 | Wave graphs, string speed, power/intensity, inverse-square scaling |
| M5-2 | 2 | 4 | Refractive index, Snell geometry, decibel conversion, dB-distance scaling |
| M5-3 | 1 | 1 | Doppler sign selection |
| M5-4 | 3 | 4 | Beats, string modes, resonant string data, pipe modes |
| M5-5 | 0 | 0 | No video; no lesson |
| **Total** | **11** | **19** | Repeated string/harmonic and intensity treatments are merged. |

## Exact source map

### M4-1 — `2026-07-21-M4-1`

- [iubb3eFBQ9U](<../../../M4/2026-07-21-M4-1/Source/mct-Simple Harmonic Motion, Mass Spring System - Amplitude, Frequency, Velocity - Physics Problems/Simple Harmonic Motion, Mass Spring System - Amplitude, Frequency, Velocity - Physics Problems [iubb3eFBQ9U].en.srt>)
- Lecture notes: [Lecture-Notes.md](<../../../M4/2026-07-21-M4-1/Source/Lecture-Notes.md>)

### M4-2 — `2026-07-22-M4-2`

- [1Q15fgz-lUk](<../../../M4/2026-07-22-M4-2/Source/mct-The Simple Pendulum/The Simple Pendulum [1Q15fgz-lUk].en.srt>)
- [scIVIhChL1I](<../../../M4/2026-07-22-M4-2/Source/mct-Physical Pendulum Problems - Moment of Inertia - Physics/Physical Pendulum Problems - Moment of Inertia - Physics [scIVIhChL1I].en.srt>)
- Lecture notes: [Lecture-Notes.md](<../../../M4/2026-07-22-M4-2/Source/Lecture-Notes.md>)

### M5-1 — `2026-07-23-M5-1`

- [qm1hDJrIYwE](<../../2026-07-23-M5-1/Source/mct-Mechanical Waves Physics Practice Problems - Basic Introduction/Mechanical Waves Physics Practice Problems - Basic Introduction [qm1hDJrIYwE].en.srt>)
- [vEzftaDL7fM](<../../2026-07-23-M5-1/Source/mct-Wave Speed on a String - Tension Force, Intensity, Power, Amplitude, Frequency - Inverse Square Law/Wave Speed on a String - Tension Force, Intensity, Power, Amplitude, Frequency - Inverse Square Law [vEzftaDL7fM].en.srt>)
- Lecture notes: [Lecture-Notes.md](<../../2026-07-23-M5-1/Source/Lecture-Notes.md>)

### M5-2 — `2026-07-27-M5-2`

- [ohQheheySDw](<../../2026-07-27-M5-2/Source/mct-Snell's Law & Index of Refraction Practice Problems - Physics/Snell's Law & Index of Refraction Practice Problems - Physics [ohQheheySDw].en.srt>)
- [twppI9Eizp8](<../../2026-07-27-M5-2/Source/mct-Sound Intensity Level in Decibels & Distance - Physics Problems/Sound Intensity Level in Decibels & Distance - Physics Problems [twppI9Eizp8].en.srt>)
- Lecture notes: [Lecture-Notes.md](<../../2026-07-27-M5-2/Source/Lecture-Notes.md>)

### M5-3 — `2026-07-28-M5-3`

- [WiTQxNaKAYA](<../../2026-07-28-M5-3/Source/mct-How To Solve Doppler Effect Physics Problems/How To Solve Doppler Effect Physics Problems [WiTQxNaKAYA].en.srt>)
- Lecture notes: [Lecture-Notes.md](<../../2026-07-28-M5-3/Source/Lecture-Notes.md>)

### M5-4 — `2026-07-29-M5-4`

- [M-OMq4QsPfY](<../../2026-07-29-M5-4/Source/mct-Beat Frequency Physics Problems/Beat Frequency Physics Problems [M-OMq4QsPfY].en.srt>)
- [-8nn8hb0H8o](<../../2026-07-29-M5-4/Source/mct-Standing Waves on a String, Fundamental Frequency, Harmonics, Overtones, Nodes, Antinodes, Physics/Standing Waves on a String, Fundamental Frequency, Harmonics, Overtones, Nodes, Antinodes, Physics [-8nn8hb0H8o].en.srt>)
- [7eyYNNUojEc](<../../2026-07-29-M5-4/Source/mct-Standing Waves In Organ Pipes - Closed & Open Tubes - Physics Problems/Standing Waves In Organ Pipes - Closed & Open Tubes - Physics Problems [7eyYNNUojEc].en.srt>)
- Lecture notes: [Lecture-Notes.md](<../../2026-07-29-M5-4/Source/Lecture-Notes.md>)

### M5-5 — `2026-07-30-M5-5`

- No attachment-selected MCT video. No MCT target is generated.

---

## Canonical lesson targets

## Problem 1

### Lesson 1 — Recover Spring Force, Stiffness, and Work from Extension Data

Lecture label: **M4-1**

Target file: `../Lessons/MCT-Problem-1.md`

**Operational core move:** Convert displacement to compatible units, infer $k=F/x$ when necessary, then choose $F=kx$ for an instantaneous force or $W=\tfrac12kx^2$ for work/elastic energy.

**Recognition cues:** “force required,” “same spring,” “spring constant,” “work required to stretch/compress,” or a linear force-versus-displacement situation.

**Exact transcript and timestamps:** `iubb3eFBQ9U`, 00:05:08–00:08:25 and 00:08:37–00:13:36.

**Source-video material to preserve:**

- $k=300\,\mathrm{N/m}$ and $x=25\,\mathrm{cm}$ give $F=75\,\mathrm N$; the same spring under $150\,\mathrm N$ compresses $50\,\mathrm{cm}$.
- $200\,\mathrm N$ stretches a spring $40\,\mathrm{cm}$; at $120\,\mathrm{cm}$ the force is $600\,\mathrm N$. Infer $k=500\,\mathrm{N/m}$ and find the work to $1.20\,\mathrm m$: $360\,\mathrm J$.

**Required content:** restoring-force sign versus requested force magnitude; proportional reasoning for one spring; why $Fx$ is wrong when the spring force ramps from zero and why the integral/triangle gives $\tfrac12kx^2$.

**Exclusions:** do not turn this into a general calculus lesson or duplicate the later oscillator energy-state lesson.

**Merged/supplemental section:** use the M4-1 lecture notes only for the sign convention and the identity $U=\tfrac12kx^2$.

## Problem 2

### Lesson 2 — Find Spring Speed and the Energy Split at a Displacement

Lecture label: **M4-1**

Target file: `../Lessons/MCT-Problem-2.md`

**Operational core move:** Set the conserved total energy from the amplitude, $E=\tfrac12kA^2$, subtract $U(x)=\tfrac12kx^2$, and use the remainder for $K$, $v$, force, or acceleration.

**Recognition cues:** a frictionless oscillator; release from maximum stretch/compression; “at $x=\dots$ from equilibrium”; maximum speed/acceleration; or kinetic, potential, and mechanical energy.

**Exact transcript and timestamps:** `iubb3eFBQ9U`, 00:32:28–00:34:57, 00:35:03–00:42:22, 00:42:25–00:51:16, 00:51:16–00:58:11, and the energy portions of 01:33:54–01:43:35.

**Source-video material to preserve:**

- If $A$ doubles, $E\propto A^2$ quadruples while $v_{\max}\propto A$ and $a_{\max}\propto A$ double.
- Frame-verified horizontal spring: $k=300\,\mathrm{N/m}$, $m=0.40\,\mathrm{kg}$, $A=0.30\,\mathrm m$. Find $v_{\max}=8.22\,\mathrm{m/s}$, $a_{\max}=225\,\mathrm{m/s^2}$, and at $x=0.20\,\mathrm m$, $v=6.12\,\mathrm{m/s}$, $F=-60\,\mathrm N$, $a=-150\,\mathrm{m/s^2}$.
- Vertical spring: a $2.0\,\mathrm{kg}$ mass produces a $0.40\,\mathrm m$ equilibrium stretch, then is pulled an additional $0.20\,\mathrm m$. Find $k=49\,\mathrm{N/m}$, $A=0.20\,\mathrm m$, $a_{\max}=4.9\,\mathrm{m/s^2}$, $v_{\max}=0.99\,\mathrm{m/s}$, and at $x=0.10\,\mathrm m$, $U=0.245\,\mathrm J$, $K=0.735\,\mathrm J$, $E=0.980\,\mathrm J$.
- A spring compressed $0.35\,\mathrm m$ by $500\,\mathrm N$ launches a $0.25\,\mathrm{kg}$ block: $k\approx1429\,\mathrm{N/m}$, release speed $26.5\,\mathrm{m/s}$, and $K\approx87.5\,\mathrm J$. Preserve the triangular-area check on the force-displacement graph.
- Frame-verified $m=0.75\,\mathrm{kg}$ and $x(t)=0.60\cos(9.2t)\,\mathrm m$: after extracting $k\approx63.5\,\mathrm{N/m}$, preserve $E\approx11.42\,\mathrm J$ and the $x=0$, $0.20$, and $0.60\,\mathrm m$ energy states. At $0.20\,\mathrm m$, $U\approx1.27\,\mathrm J$ and $K\approx10.15\,\mathrm J$.

**Required content:** measure vertical displacement from the shifted equilibrium; distinguish equilibrium stretch used to infer $k$ from oscillation amplitude; include $v(x)=\pm\sqrt{(k/m)(A^2-x^2)}$ with direction determined separately.

**Exclusions:** no damping, driving, or resonance; the M4-2 notes explicitly exclude these from Quiz 3. Do not repeat the time-law extraction taught in Problem 4 beyond the $A,\omega\to k$ handoff.

**Merged/supplemental section:** add the M4-1 lecture maximum-speed energy example, $v_{\max}\approx8.8\,\mathrm{m/s}$, as an alternate derivation rather than a new lesson.

## Problem 3

### Lesson 3 — Infer and Scale a Mass–Spring Frequency

Lecture label: **M4-1**

Target file: `../Lessons/MCT-Problem-3.md`

**Operational core move:** Build or compare $f=(2\pi)^{-1}\sqrt{k/m}$, deriving $k$ from a static force/displacement when it is not supplied.

**Recognition cues:** “frequency/period of vibration,” a static compression/stretch followed by oscillation, the same mass with a different spring, or the same spring with a different mass.

**Exact transcript and timestamps:** `iubb3eFBQ9U`, 01:09:22–01:12:06, 01:12:20–01:14:45, 01:14:50–01:20:50, 01:20:55–01:22:40, and 01:22:55–01:24:23.

**Source-video material to preserve:**

- $m=0.25\,\mathrm{kg}$ and a $200\,\mathrm N$ force stretching $0.25\,\mathrm m$: $k=800\,\mathrm{N/m}$, $f\approx9.0\,\mathrm{Hz}$, $T\approx0.111\,\mathrm s$.
- A $70\,\mathrm{kg}$ person adds $2\,\mathrm{cm}$ compression to a $1200\,\mathrm{kg}$ car: infer $k=34300\,\mathrm{N/m}$, use moving mass $1270\,\mathrm{kg}$, and obtain $f\approx0.83\,\mathrm{Hz}$.
- Frame-verified insect/web: $0.25\,\mathrm g$ at $20\,\mathrm{Hz}$ gives $k\approx3.95\,\mathrm{N/m}$; a $0.10\,\mathrm g$ insect gives $f\approx31.6\,\mathrm{Hz}$.
- The same block has $k_1=200\,\mathrm{N/m}$ and $f_1=15\,\mathrm{Hz}$; with $k_2=500\,\mathrm{N/m}$, find $f_2=23.7\,\mathrm{Hz}$.
- Cycle-accounting capstone: $A=0.40\,\mathrm m$ over eight full periods gives total distance $8(4A)=12.8\,\mathrm m$.

**Required content:** square-root rather than linear scaling; total moving mass in the car; grams-to-kilograms conversion; $T=1/f$; one complete cycle has path length $4A$.

**Exclusions:** do not use the hanging weight $mg$ as the oscillator restoring force after displacement; gravity only locates equilibrium.

**Merged/supplemental section:** include the M4-1 lecture graph $A=2.5\,\mathrm{cm}$, $T=4.0\,\mathrm s$, $f=0.25\,\mathrm{Hz}$, $\omega=\pi/2\,\mathrm{rad/s}$, $v_{\max}=3.9\,\mathrm{cm/s}$, plus the M5-1 notes' qualitative $f\propto\sqrt{k}$ and $f\propto1/\sqrt m$.

## Problem 4

### Lesson 4 — Translate an SHM State into $x(t)$, $v(t)$, and $a(t)$

Lecture label: **M4-1**

Target file: `../Lessons/MCT-Problem-4.md`

**Operational core move:** Read $A$ and $\omega$, choose sine/cosine and its sign from the initial position/direction, then differentiate without changing the phase argument.

**Recognition cues:** a supplied sinusoidal $x(t)$; a request for $v(t)$, $a(t)$, $k$, or phase; or an initial state specified as equilibrium/top/bottom and a velocity direction.

**Exact transcript and timestamps:** `iubb3eFBQ9U`, 01:33:54–01:37:02, 01:43:43–01:51:16, and 01:51:24–01:58:00.

**Source-video material to preserve:**

- Frame-verified $m=0.75\,\mathrm{kg}$, $x=0.60\cos(9.2t)$: $A=0.60\,\mathrm m$, $f=9.2/(2\pi)=1.464\,\mathrm{Hz}$, $T=0.683\,\mathrm s$, and $k=m\omega^2\approx63.5\,\mathrm{N/m}$.
- Frame-verified $m=0.55\,\mathrm{kg}$, $x=1.5\cos(12.4t)$: $v=-18.6\sin(12.4t)$, $a=-230.64\cos(12.4t)$, and $k=84.568\,\mathrm{N/m}$. The displayed prompt asks for values at $x=0.5\,\mathrm m$, but the narration substitutes $t=0.5\,\mathrm s$. If interpreted as $t=0.5\,\mathrm s$, the source values are $v\approx+1.545\,\mathrm{m/s}$, $a\approx-229.84\,\mathrm{m/s^2}$, and $F\approx-126.4\,\mathrm N$. If interpreted literally as $x=0.5\,\mathrm m$, the correct values are $a=-76.88\,\mathrm{m/s^2}$, $F=-42.28\,\mathrm N$, and $|v|\approx17.54\,\mathrm{m/s}$, with the sign of $v$ undetermined by position alone.
- $k=300\,\mathrm{N/m}$, $m=0.35\,\mathrm{kg}$, $A=0.45\,\mathrm m$, and $\omega=29.28\,\mathrm{rad/s}$: crossing equilibrium with positive velocity gives $x=0.45\sin(29.28t)$; starting at the lowest point gives $x=-0.45\cos(29.28t)$.

**Required content:** a four-state phase table; $v=dx/dt$ and $a=dv/dt=-\omega^2x$; radians; and a clear distinction between “at time” and “at position.” Include the source discrepancy above as a worked diagnostic.

**Exclusions/correction:** never reproduce the video's $x=0.5$ / $t=0.5$ dimensional mismatch as a valid solution. Skip the post-01:58 damping/resonance overview.

**Merged/supplemental section:** add the M4-1 lecture example with $x_{eq}=0.35\,\mathrm m$, release at $0.48\,\mathrm m$, 12 cycles in $7.0\,\mathrm s$, evaluated at $3.9\,\mathrm s$: relative $x=-0.051\,\mathrm m$, $v=+1.3\,\mathrm{m/s}$; emphasize the equilibrium reference and motion direction.

## Problem 5

### Lesson 5 — Solve a Simple-Pendulum Target from Period Data

Lecture label: **M4-2**

Target file: `../Lessons/MCT-Problem-5.md`

**Operational core move:** Translate cycle counts into $T$ or $f$, then rearrange $T=2\pi\sqrt{L/g}$ for the single requested variable.

**Recognition cues:** a point mass on a light string, a small angle, clock timing, an oscillation count, a change of planet/gravity, or an irrelevant bob mass.

**Exact transcript and timestamps:** `1Q15fgz-lUk`, 00:00:00–00:05:14, 00:05:15–00:10:14, 00:10:16–00:15:04, 00:15:05–00:19:07, 00:19:08–00:21:25, 00:21:26–00:25:19, and 00:25:21–00:26:24.

**Source-video material to preserve:**

- $L=0.70\,\mathrm m$: Earth $g=9.8\,\mathrm{m/s^2}$ gives $T\approx1.68\,\mathrm s$ and $f\approx0.60\,\mathrm{Hz}$; Moon $g\approx1.6\,\mathrm{m/s^2}$ gives $T\approx4.16\,\mathrm s$ and $f\approx0.24\,\mathrm{Hz}$.
- $42$ cycles in $63\,\mathrm s$ gives $T=1.50\,\mathrm s$, $f=0.667\,\mathrm{Hz}$, and $L\approx0.559\,\mathrm m$.
- $L=0.80\,\mathrm m$ and $28$ swings in $45\,\mathrm s$ on an unknown planet gives $T=1.607\,\mathrm s$ and $g\approx12.2\,\mathrm{m/s^2}\approx1.24g_E$.
- A grandfather-clock second from tick to tock is half a cycle, so $T=2.0\,\mathrm s$ and $L\approx0.993\,\mathrm m$.
- The same pendulum has $T_1=1.7\,\mathrm s$, $g_1=9.8\,\mathrm{m/s^2}$, and $g_2=15\,\mathrm{m/s^2}$: $T_2=T_1\sqrt{g_1/g_2}\approx1.37\,\mathrm s$.
- Replacing $m$ by $2m$ leaves $T$ unchanged.

**Required content:** small-angle qualification; mass cancellation; distinguish a one-way clock swing from a complete oscillation; proportional comparison as an alternative to full substitution.

**Exclusions:** no large-angle correction and no physical-pendulum inertia in this lesson.

**Merged/supplemental section:** use the M4-2 lecture notes for the torque rationale and the $11^\circ$ “small enough” example; do not make the derivation a separate overview lesson.

## Problem 6

### Lesson 6 — Assemble $I_p$ and Center of Mass for a Physical Pendulum

Lecture label: **M4-2**

Target file: `../Lessons/MCT-Problem-6.md`

**Operational core move:** About the actual pivot, sum component inertias and compute the assembly's center-of-mass distance before using $T=2\pi\sqrt{I_p/(Mg\ell)}$.

**Recognition cues:** an extended rigid body, rod/disk/composite, pivot away from the center, or moment of inertia rather than a point-mass string.

**Exact transcript and timestamps:** `scIVIhChL1I`, 00:00:03–00:02:36 and 00:02:39–00:08:22. The 00:08:24–00:10:34 simple-pendulum limiting-case derivation is merged context, not a standalone lesson.

**Source-video material to preserve:**

- Uniform rod $L=1.5\,\mathrm m$, $M=0.60\,\mathrm{kg}$, pivot at one end: $I_p=\tfrac13ML^2=0.45\,\mathrm{kg\,m^2}$, $\ell=L/2=0.75\,\mathrm m$, and $T\approx2.0\,\mathrm s$.
- Uniform rod $L=1.2\,\mathrm m$, $m_r=0.50\,\mathrm{kg}$ plus a $2.0\,\mathrm{kg}$ point mass at the end: $I_{tot}=\tfrac13m_rL^2+m_pL^2=3.12\,\mathrm{kg\,m^2}$, $\ell=1.08\,\mathrm m$, $M=2.5\,\mathrm{kg}$, and $T\approx2.16\,\mathrm s$.

**Required content:** $\ell$ is pivot-to-center-of-mass distance, not object length; parallel-axis theorem; total mass in the gravitational torque; and a component-by-component inertia ledger.

**Exclusions:** do not treat a disk as a point mass or use $I_{cm}$ without shifting it to the pivot.

**Merged/supplemental section:** use the M4-2 lecture variants: end-pivot rod, $T\approx1.6\,\mathrm s$; rod pivoted $L/6$ from an end, $\ell=L/3$, $I_p=7ML^2/36$, $T\approx1.3\,\mathrm s$; rod plus point mass, $T\approx2.0\,\mathrm s$; and rod plus disk including both $\tfrac12m_dR^2$ and $m_d(L+R)^2$, $T\approx2.5\,\mathrm s$.

## Problem 7

### Lesson 7 — Read a Wave Graph Before Using $v=f\lambda$

Lecture label: **M5-1**

Target file: `../Lessons/MCT-Problem-7.md`

**Operational core move:** First decide whether the horizontal axis is position or time; extract $\lambda$ from spatial cycles or $T$ from temporal cycles, then use $f=1/T$ and $v=f\lambda$.

**Recognition cues:** a wave snapshot, crest/trough graph, offset midline, “crest passes every…,” or a request mixing period, frequency, wavelength, and speed.

**Exact transcript and timestamps:** `qm1hDJrIYwE`, 00:00:00–00:01:18, 00:01:19–00:02:31, 00:02:33–00:04:30, and 00:04:31–00:05:18; `vEzftaDL7fM`, 00:12:56–00:14:47.

**Source-video material to preserve:**

- Spatial graph: amplitude $3\,\mathrm m$ and three complete cycles across $10\,\mathrm m$, so $\lambda=10/3=3.33\,\mathrm m$.
- Time graph: $A=10\,\mathrm m$ and the first quarter-cycle at $5\,\mathrm s$, so $T=20\,\mathrm s$ and $f=0.05\,\mathrm{Hz}$.
- Offset time graph: high $12\,\mathrm m$, low $4\,\mathrm m$, so midline $8\,\mathrm m$ and $A=4\,\mathrm m$; three-quarters of a cycle in $6\,\mathrm s$ gives $T=8\,\mathrm s$ and $f=0.125\,\mathrm{Hz}$.
- $v=125\,\mathrm{m/s}$ and $f=250\,\mathrm{Hz}$ give $\lambda=0.50\,\mathrm m$.
- A water crest passes every $2.5\,\mathrm s$ and adjacent crests are $10\,\mathrm m$ apart: $T=2.5\,\mathrm s$, $f=0.40\,\mathrm{Hz}$, $\lambda=10\,\mathrm m$, and $v=4.0\,\mathrm{m/s}$.

**Required content:** amplitude is half peak-to-trough when the midline is offset; the graph's axis decides whether a horizontal interval is time or distance; count complete rather than partial cycles.

**Exclusions:** skip the videos' generic transverse/longitudinal overview and the M5-1 notes' monopole, dipole, and quadrupole survey.

**Merged/supplemental section:** add the M5-1 lecture distinction between a $y(x)$ snapshot and a $y(t)$ particle history, plus the “shift a right-moving profile” check as a brief recognition aid.

## Problem 8

### Lesson 8 — Turn a String Description into Wave Speed

Lecture label: **M5-1**

Target file: `../Lessons/MCT-Problem-8.md`

**Operational core move:** Identify the vibrating string's $\mu=m_{string}/L$ and its actual tension, compute $v=\sqrt{F_T/\mu}$, then chain only the requested $v=f\lambda$ or travel-time step.

**Recognition cues:** string/wire mass and length, applied or hanging tension, travel from one end to another, requested tension, wavelength, or frequency.

**Exact transcript and timestamps:** `qm1hDJrIYwE`, 00:05:23–00:07:32; `vEzftaDL7fM`, 00:10:09–00:12:43, 00:14:55–00:17:15, and 00:17:24–00:20:06.

**Source-video material to preserve:**

- $L=2.0\,\mathrm m$, $m=0.10\,\mathrm{kg}$, $F_T=500\,\mathrm N$: $\mu=0.050\,\mathrm{kg/m}$, $v=100\,\mathrm{m/s}$; at $\lambda=0.25\,\mathrm m$, $f=400\,\mathrm{Hz}$.
- $F_T=1500\,\mathrm N$, $m=0.50\,\mathrm{kg}$, $L=10\,\mathrm m$, $\lambda=0.15\,\mathrm m$: $\mu=0.050\,\mathrm{kg/m}$, $v=173.2\,\mathrm{m/s}$, $f=1154.7\,\mathrm{Hz}$.
- Frame-verified $\lambda=15\,\mathrm{cm}$, $f=13\,\mathrm{Hz}$, and $\mu=0.75\,\mathrm{kg/m}$: $v=1.95\,\mathrm{m/s}$ and $F_T=\mu v^2\approx2.85\,\mathrm N$.
- An $85\,\mathrm m$ wire with mass $5.0\,\mathrm{kg}$ under $300\,\mathrm N$: $\mu=0.05882\,\mathrm{kg/m}$, $v=71.4\,\mathrm{m/s}$, and end-to-end time $1.19\,\mathrm s$.

**Required content:** the string mass belongs in $\mu$; a separate hanging mass would set $F_T\approx Mg$; maintain dimensional checks; distinguish propagation speed from a string particle's transverse speed.

**Exclusions:** do not let source frequency determine string wave speed in a fixed medium; standing-wave boundary conditions are reserved for Problems 17–18.

**Merged/supplemental section:** add the M5-2 lecture chain $F_T=Mg\to v=\sqrt{MgL/m_w}$, whose lecture result is $25\,\mathrm{m/s}$, and particle maximum speed $u_{max}=2\pi fA=(2\pi A/\lambda)v$, whose lecture result is about $200\,\mathrm{m/s}$.

## Problem 9

### Lesson 9 — Chain Energy, Power, Area, and Intensity

Lecture label: **M5-1**

Target file: `../Lessons/MCT-Problem-9.md`

**Operational core move:** Convert energy rate to power and divide or multiply by the physically illuminated area appropriate to the question.

**Recognition cues:** energy “every $t$ seconds,” an isotropic point source, watts per square meter, a receiver/plot area, or energy collected over time.

**Exact transcript and timestamps:** `vEzftaDL7fM`, 00:30:33–00:32:06 and 00:33:51–00:39:04.

**Source-video material to preserve:**

- A lamp emits $500\,\mathrm J$ every $4\,\mathrm s$: $P=125\,\mathrm W$ and, at $r=1.0\,\mathrm m$, $I=P/(4\pi r^2)=9.95\,\mathrm{W/m^2}$.
- Frame-verified sunlight $I=1200\,\mathrm{W/m^2}$ on a $30\,\mathrm m\times40\,\mathrm m$ plot: receiving area $1200\,\mathrm{m^2}$, power $1.44\times10^6\,\mathrm W$; for a 30-day month, $t=2.592\times10^6\,\mathrm s$ and energy $3.73\times10^{12}\,\mathrm J$.

**Required content:** $P=E/t$ and $I=P/A$; use $4\pi r^2$ only for isotropic spherical spreading, not for the rectangular receiver; show unit cancellation.

**Exclusions:** do not claim every source is isotropic; leave distance ratios to Problem 10.

**Merged/supplemental section:** route the lamp's $2\,\mathrm m$ and $3\,\mathrm m$ parts to Problem 10 and reference the $1\,\mathrm m$ result without reworking it.

## Problem 10

### Lesson 10 — Rescale Wave Intensity or Amplitude with Distance

Lecture label: **M5-1**

Target file: `../Lessons/MCT-Problem-10.md`

**Operational core move:** For the same isotropic source, apply the correct exponent: $I_2/I_1=(r_1/r_2)^2$, while amplitude scales as $A_2/A_1=r_1/r_2$.

**Recognition cues:** the same source at two distances, no source power requested, “twice/three times as far,” or amplitude rather than intensity.

**Exact transcript and timestamps:** `vEzftaDL7fM`, 00:21:35–00:26:59, 00:27:03–00:30:26, 00:32:07–00:33:43, 00:39:10–00:41:46, and 00:42:13–00:44:21.

**Source-video material to preserve:**

- $I_1=900\,\mathrm{W/m^2}$ at $1\,\mathrm m$ gives $I(2\,\mathrm m)=225\,\mathrm{W/m^2}$ and $I(3\,\mathrm m)=100\,\mathrm{W/m^2}$.
- The Problem 9 lamp has $9.95\,\mathrm{W/m^2}$ at $1\,\mathrm m$, $2.49\,\mathrm{W/m^2}$ at $2\,\mathrm m$, and $1.1\,\mathrm{W/m^2}$ at $3\,\mathrm m$.
- $48\,\mathrm{W/m^2}$ at $30\,\mathrm{cm}$ becomes $192\,\mathrm{W/m^2}$ at $15\,\mathrm{cm}$; centimeters cancel in the ratio.
- Amplitude $30$ at $2\,\mathrm{cm}$ becomes $60$ at $1\,\mathrm{cm}$, $15$ at $4\,\mathrm{cm}$, and $10$ at $6\,\mathrm{cm}$.

**Required content:** predict increase/decrease before calculating; distinguish $1/r^2$ intensity from $1/r$ amplitude; state the same-source, unchanged-power assumption.

**Exclusions:** skip the 00:44:32–00:50:09 full intensity-frequency derivation and the 00:50:16-onward superposition overview; retain only $I\propto A^2$ when needed to justify amplitude scaling.

**Merged/supplemental section:** include the M5-3 lecture speaker check $I_1=240\to I_2=60\,\mathrm{W/m^2}$ when distance doubles.

## Problem 11

### Lesson 11 — Convert Light Speed and Wavelength with Refractive Index

Lecture label: **M5-2**

Target file: `../Lessons/MCT-Problem-11.md`

**Operational core move:** Hold frequency fixed across a boundary and use $n=c/v$ or $n_1\lambda_1=n_2\lambda_2$ according to whether the unknown is speed/index or wavelength.

**Recognition cues:** the same light in two media, a given $n$, speed in a material, or wavelength “in air/glass/diamond.”

**Exact transcript and timestamps:** `ohQheheySDw`, 00:00:12–00:01:13, 00:01:16–00:02:20, 00:02:23–00:03:14, and 00:03:18–00:05:04.

**Source-video material to preserve:**

- Water $n=1.33$: $v=3.00\times10^8/1.33=2.256\times10^8\,\mathrm{m/s}$.
- Diamond $v=1.24\times10^8\,\mathrm{m/s}$: $n=2.42$.
- Vacuum wavelength $600\,\mathrm{nm}$ and glass $n=1.5$: $\lambda_{glass}=400\,\mathrm{nm}$.
- $\lambda_{glass}=450\,\mathrm{nm}$, $n_{glass}=1.5$, and $n_{diamond}=2.42$: $\lambda_{diamond}\approx279\,\mathrm{nm}$.

**Required content:** frequency is source-set and unchanged at the interface; larger $n$ means lower speed and shorter wavelength; ratios preserve units.

**Exclusions:** no ray-bending angles here; those belong to Problem 12.

**Merged/supplemental section:** use the M5-2 lecture wavelength ranking $n_B>n_A>n_C$ and the slide example with $\lambda_{air}=650\,\mathrm{nm}$ and $n_{glass}=1.5$, giving about 3230 wavelengths across the supplied slide width.

## Problem 12

### Lesson 12 — Carry a Ray through One or More Refracting Boundaries

Lecture label: **M5-2**

Target file: `../Lessons/MCT-Problem-12.md`

**Operational core move:** Draw the normal at each surface, measure every angle from that normal, then apply $n_1\sin\theta_1=n_2\sin\theta_2$ boundary by boundary, canceling intermediate parallel layers only when their normals are parallel.

**Recognition cues:** an incident/refracted ray, angle “with the normal,” multiple interfaces, a rectangular block, or a changed surface orientation.

**Exact transcript and timestamps:** `ohQheheySDw`, 00:05:07–00:08:05, 00:08:07–00:14:15, and 00:14:17–00:17:32.

**Source-video material to preserve:**

- Air-to-water, $\theta_i=30^\circ$, $n_1=1$, $n_2=1.33$: $\theta_r\approx22^\circ$, bending toward the normal.
- Parallel air/glass/diamond layers: $\theta_{air}=60^\circ$, $n_g=1.5$, $n_d=2.42$; $\theta_g=35.3^\circ$ and $\theta_d\approx21^\circ$. Show both two-step work and the endpoint shortcut $n_1\sin\theta_1=n_3\sin\theta_3$.
- Frame-verified rectangular $n=1.2$ block in air: the ray enters a vertical face at $70^\circ$ to its horizontal normal and refracts to $51.5^\circ$; at the perpendicular top face its new incidence angle is $90^\circ-51.5^\circ=38.45^\circ$, then it exits at $x=48.3^\circ$ to the vertical normal.

**Required content:** low-to-high $n$ bends toward the normal and high-to-low bends away; the angle transmitted from one boundary is reused unchanged only when normals are parallel; take a complement when surfaces are perpendicular.

**Exclusions:** do not measure angles from the surface or use the parallel-layer shortcut for the rectangular-block turn.

**Merged/supplemental section:** use the M5-2 notes' $n\lambda=\text{constant}$ only as a physical check, not a second solution path.

## Problem 13

### Lesson 13 — Convert Between Sound Intensity and Decibels

Lecture label: **M5-2**

Target file: `../Lessons/MCT-Problem-13.md`

**Operational core move:** Decide which side of $\beta=10\log_{10}(I/I_0)$ is unknown, use $I_0=10^{-12}\,\mathrm{W/m^2}$, and invert the logarithm when solving for $I$.

**Recognition cues:** decibels paired with $\mathrm{W/m^2}$, threshold of hearing, or a comparison of equal source counts.

**Exact transcript and timestamps:** `twppI9Eizp8`, 00:00:07–00:01:15 and 00:01:18–00:04:51.

**Source-video material to preserve:**

- $I=4\times10^{-5}\,\mathrm{W/m^2}$ gives $\beta=76\,\mathrm{dB}$.
- The frame-verified prompt asks for intensities of $50\,\mathrm{dB}$ and $60\,\mathrm{dB}$ sounds: $I_{50}=10^{-7}\,\mathrm{W/m^2}$ and $I_{60}=10^{-6}\,\mathrm{W/m^2}$; an increase of $10\,\mathrm{dB}$ means ten times the intensity.

**Required content:** base-10 logarithm; $I=I_0\,10^{\beta/10}$; dimensional role of the ratio; distinguish adding intensities from adding decibel values.

**Exclusions:** do not imply that an increase of $10\,\mathrm{dB}$ means ten times the perceived loudness; perception is outside the source scope.

**Merged/supplemental section:** add the M5-3 lecture examples: normal conversation $60\,\mathrm{dB}\leftrightarrow10^{-6}\,\mathrm{W/m^2}$; two equal $60\,\mathrm{dB}$ talkers have double the intensity and a combined level about $63\,\mathrm{dB}$, not $120\,\mathrm{dB}$.

## Problem 14

### Lesson 14 — Update a Sound Level after the Listener Moves

Lecture label: **M5-2**

Target file: `../Lessons/MCT-Problem-14.md`

**Operational core move:** Combine inverse-square intensity with the logarithmic scale to use $\beta_2=\beta_1+20\log_{10}(r_1/r_2)$.

**Recognition cues:** the same sound source, an initial dB level at one distance, and a new distance with no power change.

**Exact transcript and timestamps:** `twppI9Eizp8`, 00:04:55–00:11:51.

**Source-video material to preserve:** a sound level of $40\,\mathrm{dB}$ at $2\,\mathrm m$ becomes
$$
\beta_2=40+20\log_{10}\left(\frac{2}{4}\right)=33.98\,\mathrm{dB}
$$
at $4\,\mathrm m$, a decrease of about $6.02\,\mathrm{dB}$.

**Required content:** keep distance order paired with $\beta_2-\beta_1$; doubling distance reduces intensity by four and level by about $6\,\mathrm{dB}$; predict the sign first.

**Exclusions:** do not apply the linear $I\propto1/r^2$ ratio directly to decibel values.

**Merged/supplemental section:** refer back to Problem 10 for inverse-square reasoning and Problem 13 for logarithms; do not duplicate either derivation as a separate lesson.

## Problem 15

### Lesson 15 — Choose Doppler Signs from Toward/Away Motion

Lecture label: **M5-3**

Target file: `../Lessons/MCT-Problem-15.md`

**Operational core move:** Put observer motion in the numerator and source motion in the denominator of
$$
f_o=f_s\frac{v\pm v_o}{v\mp v_s},
$$
choosing each sign so approaching raises and separating lowers the predicted frequency.

**Recognition cues:** a moving siren/source, moving listener/observer, two moving objects, detected pitch/frequency, or toward/away language.

**Exact transcript and timestamps:** `WiTQxNaKAYA`, 00:05:02–00:15:51, 00:15:54–00:21:06, 00:21:08–00:25:54, and 00:25:59–00:30:18.

**Source-video material to preserve:**

- Ambulance $f_s=800\,\mathrm{Hz}$, source speed $30\,\mathrm{m/s}$, stationary observer, and $v=343\,\mathrm{m/s}$: toward gives $877\,\mathrm{Hz}$; away gives $736\,\mathrm{Hz}$.
- Stationary ambulance $f_s=1200\,\mathrm{Hz}$ and observer speed $25\,\mathrm{m/s}$: toward gives $1287\,\mathrm{Hz}$; away gives $1113\,\mathrm{Hz}$.
- A police car/source moves west at $20\,\mathrm{m/s}$ toward a driver/observer moving east at $25\,\mathrm{m/s}$, with $f_s=900\,\mathrm{Hz}$: both approach and $f_o\approx1025\,\mathrm{Hz}$.

**Required content:** qualitative prediction before sign choice; a stationary variable is zero; source and observer motions are physically different; use $v\approx343\,\mathrm{m/s}$ unless temperature is supplied.

**Exclusions:** skip the long generic wavefront overview as a standalone section; do not use one memorized global plus/minus pattern without checking the expected frequency shift.

**Merged/supplemental section:** add the M5-3 lecture variants: a bat observer flies toward an $880\,\mathrm{Hz}$ singer at $35\,\mathrm{m/s}$ and hears about $970\,\mathrm{Hz}$; a bat source would need to fly away at about $86\,\mathrm{m/s}$ to shift $25\,\mathrm{kHz}$ to $20\,\mathrm{kHz}$, an implausibly high speed.

## Problem 16

### Lesson 16 — Resolve Beat-Frequency Ambiguity

Lecture label: **M5-4**

Target file: `../Lessons/MCT-Problem-16.md`

**Operational core move:** Use $f_b=|f_1-f_2|$; when one frequency is unknown, generate both $f_{known}\pm f_b$ candidates and use any second comparison to select the common candidate.

**Recognition cues:** “beats per second,” two nearby tones, tuning an unknown fork, or two beat measurements against references.

**Exact transcript and timestamps:** `M-OMq4QsPfY`, 00:00:01–00:00:44, 00:00:46–00:02:11, and 00:02:14–00:03:36.

**Source-video material to preserve:**

- Frame-verified $425\,\mathrm{Hz}$ and $436\,\mathrm{Hz}$ tones: $f_b=11\,\mathrm{Hz}$.
- A $360\,\mathrm{Hz}$ tone produces $32$ beats in $4\,\mathrm s$: $f_b=8\,\mathrm{Hz}$, so the fork could be $352\,\mathrm{Hz}$ or $368\,\mathrm{Hz}$.
- An unknown fork makes $5\,\mathrm{Hz}$ beats with $415\,\mathrm{Hz}$ and $6\,\mathrm{Hz}$ beats with $426\,\mathrm{Hz}$: candidate intersections select $420\,\mathrm{Hz}$.

**Required content:** beat rate is an absolute difference, not an average; convert beat count/time first; retain both inverse candidates until another fact resolves them.

**Exclusions:** no full trigonometric beat-envelope derivation.

**Merged/supplemental section:** use the M5-4 lecture notes' constructive/destructive alternation only as a short mechanism explanation.

## Problem 17

### Lesson 17 — Translate a Fixed-End Standing-Wave Mode

Lecture label: **M5-4**

Target file: `../Lessons/MCT-Problem-17.md`

**Operational core move:** Convert the pictured or named mode into harmonic number $n$, then keep matching subscripts in $\lambda_n=2L/n$, $f_n=nf_1=nv/(2L)$, nodes $n+1$, and antinodes $n$.

**Recognition cues:** a string fixed at both ends, loops, nodes/antinodes, harmonic/overtone, a supplied $f_n$ or $\lambda_n$, or mixed harmonic subscripts.

**Exact transcript and timestamps:** `qm1hDJrIYwE`, 00:07:34–00:12:23; `-8nn8hb0H8o`, 00:13:38–00:14:37, 00:14:46–00:17:28, 00:17:36–00:22:25, 00:22:37–00:24:50, and 00:36:39–00:40:05.

**Source-video material to preserve:**

- `qm1hDJrIYwE`: $v=130\,\mathrm{m/s}$ and $L=2.5\,\mathrm m$ give $f_1=26\,\mathrm{Hz}$ and $f_3=78\,\mathrm{Hz}$. The third mode has four nodes and three antinodes; fifth overtone is $f_6=156\,\mathrm{Hz}$; third overtone is $\lambda_4=1.25\,\mathrm m$.
- Five loops give six nodes and five antinodes.
- $f_1=175\,\mathrm{Hz}$ gives the first four harmonics $175$, $350$, $525$, and $700\,\mathrm{Hz}$.
- $f_7=280\,\mathrm{Hz}$ gives $f_1=40\,\mathrm{Hz}$, $f_4=160\,\mathrm{Hz}$, and $f_9=360\,\mathrm{Hz}$.
- $L=2.0\,\mathrm m$, three loops, and $v=45\,\mathrm{m/s}$ give $\lambda_3=4/3\,\mathrm m$, $f_3=33.75\,\mathrm{Hz}$, $f_1=11.25\,\mathrm{Hz}$, and $\lambda_1=4.0\,\mathrm m$.
- $\lambda_1=12\,\mathrm m$ gives the first five wavelengths $12$, $6$, $4$, $3$, and $2.4\,\mathrm m$.
- $\lambda_5=1.8\,\mathrm m$ gives $\lambda_1=9.0\,\mathrm m$ and $\lambda_9=1.0\,\mathrm m$.
- Mixed data $f_4=300\,\mathrm{Hz}$ and $\lambda_2=2.3\,\mathrm m$: convert both to a common harmonic and obtain $v=345\,\mathrm{m/s}$.

**Required content:** one loop is half a wavelength; overtone number is harmonic number minus one for fixed-fixed strings; never multiply $f_n\lambda_m$ unless $n=m$; wave speed remains the same across modes of one string.

**Exclusions:** do not duplicate the long 00:00–00:13 derivation; closed-open pipe overtone mapping is different and belongs to Problem 19.

**Merged/supplemental section:** merge the shorter `qm1hDJrIYwE` treatment into the complete `-8nn8hb0H8o` progression. Use the M5-4 lecture simulation values $f_1\approx0.44$, $f_2\approx0.88$, and $f_3\approx1.32\,\mathrm{Hz}$ only as a ratio check.

## Problem 18

### Lesson 18 — Chain String Material Data into a Resonant Mode

Lecture label: **M5-4**

Target file: `../Lessons/MCT-Problem-18.md`

**Operational core move:** Compute $\mu$ and $v=\sqrt{F_T/\mu}$, impose the selected fixed-end mode, then solve for the requested $L$, $F_T$, $\lambda_n$, or $f_n$.

**Recognition cues:** a standing wave plus string mass/tension/length, a specified number of loops, or a requested tension for a resonance.

**Exact transcript and timestamps:** `-8nn8hb0H8o`, 00:24:56–00:29:49 and 00:29:57–00:36:35.

**Source-video material to preserve:**

- $v=30\,\mathrm{m/s}$, five loops, and $f_5=250\,\mathrm{Hz}$ give $\lambda_5=0.12\,\mathrm m$ and $L=0.30\,\mathrm m=30\,\mathrm{cm}$. If the string mass is $40\,\mathrm g$, the required tension is $F_T=(m/L)v^2=120\,\mathrm N$.
- $F_T=300\,\mathrm N$, $m=0.75\,\mathrm{kg}$, $L=5.0\,\mathrm m$, and five loops give $\mu=0.15\,\mathrm{kg/m}$, $v=44.72\,\mathrm{m/s}$, $\lambda_5=2.0\,\mathrm m$, $f_5=22.36\,\mathrm{Hz}$, $f_1=4.472\,\mathrm{Hz}$, and first three overtones $8.944$, $13.41$, and $17.88\,\mathrm{Hz}$.

**Required content:** keep string mass distinct from a possible hanging tension mass; convert grams; apply the boundary equation only after identifying $n$.

**Exclusions:** do not recompute the full harmonic catalog taught in Problem 17.

**Merged/supplemental section:** add the M5-4 lecture examples: wire $L=0.85\,\mathrm m$, $m=0.0022\,\mathrm{kg}$, $F_T=52\,\mathrm N$ gives $f_1\approx83.4\,\mathrm{Hz}$; the hanging-mass third-harmonic chain $F_T=Mg$ has lecture result $f_3\approx130\,\mathrm{Hz}$.

## Problem 19

### Lesson 19 — Map Pipe Boundaries, Harmonics, and Overtones

Lecture label: **M5-4**

Target file: `../Lessons/MCT-Problem-19.md`

**Operational core move:** Classify the pipe first: open-open or closed-closed uses all integers with $2L$; closed-open uses only odd $n$ with $4L$. Only then translate overtone number and apply $f_n=nv/(2L)$ or $f_n=nv/(4L)$.

**Recognition cues:** an organ pipe/tube, open or closed ends, harmonic versus overtone, successive resonances, or temperature-dependent sound speed.

**Exact transcript and timestamps:** `7eyYNNUojEc`, 00:00:00–00:04:23, 00:04:26–00:09:01, and 00:09:03–00:11:43.

**Source-video material to preserve:**

- Open-open $L=0.85\,\mathrm m$ at $15^\circ\mathrm C$, so $v=331+0.6T=340\,\mathrm{m/s}$: $f_1=200\,\mathrm{Hz}$, $f_4=800\,\mathrm{Hz}$, fifth overtone $=f_6=1200\,\mathrm{Hz}$, and second overtone $=n=3$ with $\lambda_3=0.567\,\mathrm m$.
- Closed-open $L=0.50\,\mathrm m$ at $15^\circ\mathrm C$: $f_1=170\,\mathrm{Hz}$; third overtone $=n=7$ gives $f_7=1190\,\mathrm{Hz}$; second overtone $=n=5$ gives $\lambda_5=0.40\,\mathrm m$ and $f_5=850\,\mathrm{Hz}$.
- Successive resonances $750\,\mathrm{Hz}$ and $1050\,\mathrm{Hz}$ have spacing $300\,\mathrm{Hz}$ and reveal the odd-only sequence $150$, $450$, $750$, $1050\,\mathrm{Hz}$. Therefore the pipe is closed-open, $f_1=150\,\mathrm{Hz}$, and with $v=340\,\mathrm{m/s}$, $L=0.567\,\mathrm m$.

**Required content:** displacement node at a closed end and antinode at an open end; pressure boundary conditions are reversed; open-open overtone $q$ maps to $n=q+1$, closed-open overtone $q$ maps to $n=2q+1$; successive allowed closed-open frequencies are separated by $2f_1$.

**Exclusions/correction:** at 00:08:14 the narration says wavelength is speed “times” frequency while the written and numerical work correctly uses $\lambda=v/f$; teach only division and flag the spoken slip. Do not add end correction.

**Merged/supplemental section:** add the M5-4 lecture closed-open example $L=0.85\,\mathrm m$, $v=343\,\mathrm{m/s}$: $f_3\approx303\,\mathrm{Hz}$ (rounded 300) and $f_5\approx500\,\mathrm{Hz}$, plus the displacement-versus-pressure boundary warning.

## Coverage audit

- Problems 1–19 map uniquely to `../Lessons/MCT-Problem-1.md` through `../Lessons/MCT-Problem-19.md`.
- All 11 exact Q3 transcript IDs occur in the source map and in at least one timestamped lesson entry.
- Repeated treatment is intentionally consolidated: `qm1hDJrIYwE` standing waves merge into Problem 17; `vEzftaDL7fM` power and distance scaling split only at the distinct area-versus-ratio decision; lecture examples remain supplements rather than new targets.
- M5-5 has no video and no generated lesson.
