# Physics 212: Superposition, Standing Waves, and Harmonics

Welcome back to Physics 212.
[View Notes](Lecture-Notes.md)

## Announcements

Quiz 2 scores have been posted, and the optional Quiz 2X assignment is available. Quiz 2X is due next Tuesday at 6:00 p.m.

Quiz 3 will be available through Proctorio beginning Saturday at 5:00 p.m. The Zoom-proctored versions will be administered Monday during the regular class period and again at 6:00 p.m.

Continue preparing your handwritten note sheet for Quiz 3.

# The Principle of Superposition

When two or more waves occupy the same region of a linear medium, their displacements combine according to the **principle of superposition**.

At every position and instant, the displacement of the medium is the algebraic sum of the displacements that the individual waves would produce:

$$
\boxed{
y_{\mathrm{net}}(x,t)
=
y_1(x,t)
+
y_2(x,t)
+
\cdots
}.
$$

The displacements must be added point by point. An upward displacement is positive, while a downward displacement is negative.

After the waves overlap, they continue traveling through one another. The temporary combined shape does not prevent either original wave from continuing through the medium.

## Example: Ripples on a Pond

Suppose two raindrops strike a pond at different locations. Each drop produces circular ripples that spread outward.

When the two sets of ripples overlap, the surface displacement at each point is determined by adding the displacement produced by each ripple. In some places the ripples reinforce one another, while in other places they partially or completely cancel.

This combination of overlapping waves is called **interference**.

# Interference

Interference is the pattern produced when waves overlap and superpose. The nature of the interference depends on the relative phase of the waves.

## Complete Constructive Interference

Consider two identical sinusoidal waves with the same amplitude, frequency, wavelength, and phase:

$$
y_1(x,t)
=
A\sin(kx-\omega t)
$$

and

$$
y_2(x,t)
=
A\sin(kx-\omega t).
$$

Because the waves are in phase, their crests align with crests and their troughs align with troughs.

Using superposition,

$$
y_{\mathrm{net}}
=
y_1+y_2,
$$

so

$$
y_{\mathrm{net}}(x,t)
=
2A\sin(kx-\omega t).
$$

The resulting amplitude is

$$
\boxed{
A_{\mathrm{net}}=2A
}.
$$

This is **complete constructive interference**.

The amplitude doubles, but the frequency and wavelength remain unchanged.

## Complete Destructive Interference

Now consider two otherwise identical waves that are exactly $180^\circ$, or $\pi$ radians, out of phase.

If

$$
y_1(x,t)
=
A\sin(kx-\omega t),
$$

then the second wave may be written as

$$
y_2(x,t)
=
A\sin(kx-\omega t+\pi).
$$

Because

$$
\sin(\phi+\pi)=-\sin\phi,
$$

the second wave becomes

$$
y_2(x,t)
=
-A\sin(kx-\omega t).
$$

The net displacement is therefore

$$
y_{\mathrm{net}}
=
y_1+y_2
=
0.
$$

Thus,

$$
\boxed{
y_{\mathrm{net}}=0
}.
$$

This is **complete destructive interference**. Each crest coincides with an equal-magnitude trough, so the waves cancel while they overlap.

Complete cancellation requires equal amplitudes and a phase difference of exactly $\pi$ radians.

# Beats

When two waves have slightly different frequencies, their relative phase continually changes.

At some times, the waves are nearly in phase and interfere constructively. At other times, they are nearly out of phase and interfere destructively.

The result is an oscillation whose amplitude repeatedly increases and decreases. This slowly varying amplitude forms an **envelope** around the faster oscillations.

This periodic variation in amplitude is called **beats**.

During each beat cycle:

- Constructive interference produces a maximum in the resultant amplitude.
- Destructive interference produces a minimum in the resultant amplitude.
- The waves then drift back into phase, and the pattern repeats.

# Reflection of Waves

A traveling wave may reflect when it reaches the end of a medium. The phase of the reflected wave depends on the boundary condition.

## Reflection from a Fixed End

At a fixed or hard boundary, the end of the medium cannot move.

The reflected wave is inverted relative to the incident wave. A crest returns as a trough, and a trough returns as a crest.

This inversion corresponds to a phase change of

$$
\boxed{
\Delta\phi=\pi\ \mathrm{rad}
}
$$

or

$$
\boxed{
\Delta\phi=180^\circ
}.
$$

## Reflection from a Free End

At a free or soft boundary, the end of the medium is allowed to move.

The reflected wave is not inverted. A crest returns as a crest, and a trough returns as a trough.

More complicated boundaries may involve both reflection and transmission, but the detailed behavior at such discontinuities is outside the present course scope.

# Standing Waves

A **standing wave** can form when two waves with the same frequency and amplitude travel in opposite directions through the same medium.

The waves continuously superpose. At certain resonant frequencies, their interference produces a stable spatial pattern rather than a pattern that appears to travel through the medium.

## Nodes

A **node** is a position where the displacement is always zero:

$$
\boxed{
y_{\mathrm{node}}=0
}.
$$

The two traveling waves interfere destructively at every node.

## Antinodes

An **antinode** is a position where the oscillation has its maximum amplitude.

The two traveling waves interfere constructively at each antinode.

Thus, a standing wave contains alternating nodes and antinodes whose positions remain fixed.

## Standing Waves on a Driven String

Consider a driver oscillating one end of a string while the other end is fixed.

The driver sends a wave along the string. When the wave reaches the fixed end, it reflects and returns inverted. The incident and reflected waves then travel in opposite directions and overlap.

At an arbitrary driving frequency, the resulting motion may appear complicated and does not form a simple, stable pattern of nodes and antinodes.

At a resonant frequency, however, the incident and reflected waves interfere in a way that produces a stable standing-wave pattern.

Wave speed, wavelength, and frequency are related by

$$
\boxed{
v=\lambda f
}.
$$

For a particular string, the wave speed is determined by the properties of the medium, including the string’s tension and linear mass density.

The oscillator determines the driving frequency. Once $v$ and $f$ are fixed, the wavelength is

$$
\boxed{
\lambda=\frac{v}{f}
}.
$$

The string also has a fixed length and specific boundary conditions. A stable standing wave forms only when the wavelength fits those conditions. Therefore, only particular driving frequencies produce resonance.

# Standing Waves on a String Fixed at Both Ends

For a string fixed at both ends, each end must be a displacement node.

The string’s length must contain an integer number of half-wavelengths:

$$
L
=
m\frac{\lambda_m}{2},
$$

where

$$
m=1,2,3,\ldots
$$

is the mode number or harmonic number.

Solving for the wavelength gives

$$
\boxed{
\lambda_m=\frac{2L}{m}
}.
$$

The mode number counts the number of half-wavelength segments that fit along the string.

Because

$$
v=f\lambda,
$$

the frequency of mode $m$ is

$$
f_m
=
\frac{v}{\lambda_m}.
$$

Substituting the allowed wavelength,

$$
f_m
=
\frac{v}{2L/m},
$$

so

$$
\boxed{
f_m=\frac{mv}{2L}
}.
$$

## Fundamental Frequency

The lowest-frequency standing-wave pattern is the **fundamental mode**, also called the **first harmonic**.

It has:

- Nodes at the two fixed ends
- One antinode
- One-half of a wavelength along the string

Therefore,

$$
L=\frac{\lambda_1}{2},
$$

so

$$
\boxed{
\lambda_1=2L
}.
$$

The fundamental frequency is

$$
\boxed{
f_1=\frac{v}{2L}
}.
$$

## Second Harmonic

The second harmonic has:

- Nodes at the two fixed ends
- One interior node
- Two antinodes
- One complete wavelength along the string

Therefore,

$$
L=\lambda_2,
$$

so

$$
\boxed{
\lambda_2=L
}.
$$

Its frequency is

$$
f_2=\frac{v}{L}.
$$

Comparing this with the fundamental frequency,

$$
\boxed{
f_2=2f_1
}.
$$

## Third Harmonic

The third harmonic has:

- Nodes at the two fixed ends
- Two interior nodes
- Three antinodes
- Three half-wavelengths along the string

Therefore,

$$
L=\frac{3\lambda_3}{2}.
$$

Solving for the wavelength gives

$$
\boxed{
\lambda_3=\frac{2L}{3}
}.
$$

The corresponding frequency is

$$
f_3
=
\frac{v}{\lambda_3}
=
\frac{3v}{2L}.
$$

Therefore,

$$
\boxed{
f_3=3f_1
}.
$$

## General Harmonic Relationships

For a string fixed at both ends,

$$
\boxed{
\lambda_m=\frac{2L}{m}
}
$$

and

$$
\boxed{
f_m=\frac{mv}{2L}=mf_1
}.
$$

Thus, the allowed frequencies are integer multiples of the fundamental frequency:

$$
f_1,\ 2f_1,\ 3f_1,\ 4f_1,\ldots
$$

The mode numbered $m$ has:

- $m$ antinodes
- $m-1$ interior nodes
- $m+1$ total nodes when the fixed endpoints are included

As the harmonic number increases, the wavelength decreases and the frequency increases.

# Standing-Wave Simulation

In the simulation, the second harmonic occurred at approximately

$$
f_2\approx0.88\ \mathrm{Hz}.
$$

Because

$$
f_2=2f_1,
$$

the predicted fundamental frequency was

$$
f_1=\frac{f_2}{2}.
$$

Therefore,

$$
f_1
=
\frac{0.88\ \mathrm{Hz}}{2}
=
0.44\ \mathrm{Hz}.
$$

Thus,

$$
\boxed{
f_1\approx0.44\ \mathrm{Hz}
}.
$$

The third-harmonic frequency can be found from

$$
f_3=3f_1.
$$

Substituting the fundamental frequency,

$$
f_3
=
3(0.44\ \mathrm{Hz})
=
1.32\ \mathrm{Hz}.
$$

Equivalently,

$$
\frac{f_3}{f_2}=\frac{3}{2},
$$

so

$$
f_3
=
\frac{3}{2}f_2
=
\frac{3}{2}(0.88\ \mathrm{Hz})
=
1.32\ \mathrm{Hz}.
$$

The simulated node and antinode patterns agreed with the predicted harmonic numbers:

- The fundamental had one antinode.
- The second harmonic had two antinodes and one interior node.
- The third harmonic had three antinodes and two interior nodes.

Frequencies that were not harmonics of the fundamental did not produce stable standing-wave patterns.

# Wave Speed on a String

The speed of a transverse wave on a stretched string is

$$
\boxed{
v=\sqrt{\frac{T}{\mu}}
},
$$

where:

- $T$ is the string tension.
- $\mu$ is the string’s linear mass density.

Linear mass density is mass per unit length:

$$
\boxed{
\mu=\frac{m_{\mathrm{wire}}}{L}
}.
$$

A larger tension produces a greater wave speed, while a larger linear mass density produces a smaller wave speed.

Combining the wave-speed equation with the harmonic-frequency equation gives

$$
f_m
=
\frac{m}{2L}
\sqrt{\frac{T}{\mu}}.
$$

Using

$$
\mu=\frac{m_{\mathrm{wire}}}{L},
$$

we obtain

$$
\boxed{
f_m
=
\frac{m}{2}
\sqrt{
\frac{T}{
m_{\mathrm{wire}}L
}
}
}.
$$

For the fundamental mode,

$$
\boxed{
f_1
=
\frac{1}{2}
\sqrt{
\frac{T}{
m_{\mathrm{wire}}L
}
}
}.
$$

# Worked Example: Fundamental Frequency of a Stretched Wire

A wire has length

$$
L=0.85\ \mathrm{m},
$$

tension

$$
T=52\ \mathrm{N},
$$

and mass

$$
m_{\mathrm{wire}}=0.0022\ \mathrm{kg}.
$$

Determine its fundamental frequency.

## 1. Find the Linear Mass Density

The linear mass density is

$$
\mu
=
\frac{m_{\mathrm{wire}}}{L}.
$$

Substituting the given values,

$$
\mu
=
\frac{
0.0022\ \mathrm{kg}
}{
0.85\ \mathrm{m}
}.
$$

Therefore,

$$
\mu
\approx
2.59\times10^{-3}\ \mathrm{kg/m}.
$$

## 2. Find the Wave Speed

The wave speed is

$$
v=\sqrt{\frac{T}{\mu}}.
$$

Substituting,

$$
v
=
\sqrt{
\frac{
52\ \mathrm{N}
}{
2.59\times10^{-3}\ \mathrm{kg/m}
}
}.
$$

This gives

$$
v\approx142\ \mathrm{m/s}.
$$

## 3. Find the Fundamental Frequency

For a string fixed at both ends,

$$
f_1=\frac{v}{2L}.
$$

Therefore,

$$
f_1
=
\frac{
142\ \mathrm{m/s}
}{
2(0.85\ \mathrm{m})
}.
$$

Thus,

$$
\boxed{
f_1\approx83.4\ \mathrm{Hz}
}.
$$

The same result follows directly from

$$
f_1
=
\frac{1}{2}
\sqrt{
\frac{T}{
m_{\mathrm{wire}}L
}
}.
$$

# Worked Example: Third Harmonic with a Hanging Mass

Consider a wire of vibrating length $L$ and mass $m_{\mathrm{wire}}$. A hanging mass $M$ supplies the tension, and the system is in equilibrium.

Determine the third-harmonic frequency.

## 1. Determine the Tension

Because the hanging mass is in equilibrium, its acceleration is zero. The upward tension balances its downward weight:

$$
T-Mg=0.
$$

Therefore,

$$
\boxed{
T=Mg
}.
$$

## 2. Determine the Linear Mass Density

For a uniform wire,

$$
\boxed{
\mu=\frac{m_{\mathrm{wire}}}{L}
}.
$$

## 3. Use the Third-Harmonic Frequency

For the third harmonic,

$$
f_3=\frac{3v}{2L}.
$$

The wave speed is

$$
v=\sqrt{\frac{T}{\mu}}.
$$

Therefore,

$$
f_3
=
\frac{3}{2L}
\sqrt{\frac{T}{\mu}}.
$$

Substituting the tension and linear mass density,

$$
f_3
=
\frac{3}{2L}
\sqrt{
\frac{
Mg
}{
m_{\mathrm{wire}}/L
}
}.
$$

Simplifying,

$$
\boxed{
f_3
=
\frac{3}{2}
\sqrt{
\frac{
Mg
}{
m_{\mathrm{wire}}L
}
}
}.
$$

Using the numerical quantities supplied in the lecture diagram gives

$$
\boxed{
f_3\approx130\ \mathrm{Hz}
}.
$$

# Standing Sound Waves in Pipes

Air columns can support standing sound waves when a traveling sound wave reflects from the ends of a pipe and interferes with itself.

Because sound is longitudinal, the standing-wave pattern describes the longitudinal displacement of air particles. The permitted wavelengths are determined by the displacement boundary condition at each end of the pipe.

## Boundary Conditions

At a closed end, air cannot move through the wall. A closed end is therefore a **displacement node**:

$$
\boxed{
\text{closed end}
\longrightarrow
\text{displacement node}
}.
$$

At an open end, air can move freely. An open end is therefore a **displacement antinode**:

$$
\boxed{
\text{open end}
\longrightarrow
\text{displacement antinode}
}.
$$

These assignments apply when the standing-wave diagram represents air displacement.

For pressure variations, the pattern is reversed:

- A displacement node is a pressure antinode.
- A displacement antinode is a pressure node.

Thus, a closed end is a pressure antinode, while an open end is a pressure node.

# Pipes with the Same Boundary Condition at Both Ends

A pipe that is open at both ends and a pipe that is closed at both ends have different displacement patterns, but they permit the same set of wavelengths and frequencies.

## Closed–Closed Pipe

A pipe closed at both ends must have a displacement node at each end.

For the fundamental mode, one-half wavelength fits inside the pipe:

$$
L=\frac{\lambda_1}{2}.
$$

Therefore,

$$
\boxed{
\lambda_1=2L
}.
$$

## Open–Open Pipe

A pipe open at both ends must have a displacement antinode at each end.

The fundamental mode also contains one-half wavelength:

$$
L=\frac{\lambda_1}{2},
$$

so

$$
\boxed{
\lambda_1=2L
}.
$$

Although the locations of the displacement nodes and antinodes differ from those in a closed–closed pipe, the permitted wavelengths are the same.

## Harmonics for Open–Open and Closed–Closed Pipes

For either type of pipe, the length contains an integer number of half-wavelengths:

$$
L=m\frac{\lambda_m}{2},
\qquad
m=1,2,3,\ldots
$$

Solving for wavelength gives

$$
\boxed{
\lambda_m=\frac{2L}{m}
}.
$$

The permitted frequencies are

$$
\boxed{
f_m=\frac{mv}{2L}=mf_1,
\qquad
m=1,2,3,\ldots
}
$$

with

$$
\boxed{
f_1=\frac{v}{2L}
}.
$$

All positive-integer harmonics are permitted:

$$
f_1,\ 2f_1,\ 3f_1,\ 4f_1,\ldots
$$

This is the same harmonic sequence produced by a string fixed at both ends.

# Pipe Closed at One End and Open at the Other

A closed–open pipe has unlike boundary conditions:

- The closed end is a displacement node.
- The open end is a displacement antinode.

The shortest standing-wave pattern connecting a node to an antinode contains one-quarter wavelength.

## Fundamental Mode

For the fundamental,

$$
L=\frac{\lambda_1}{4}.
$$

Therefore,

$$
\boxed{
\lambda_1=4L
}.
$$

The fundamental frequency is

$$
\boxed{
f_1=\frac{v}{4L}
}.
$$

For the same length and wave speed, the fundamental frequency of a closed–open pipe is one-half that of an open–open or closed–closed pipe.

## Higher Modes

The next standing-wave pattern that satisfies a node at one end and an antinode at the other contains three-quarters of a wavelength:

$$
L=\frac{3\lambda_3}{4}.
$$

Therefore,

$$
\lambda_3=\frac{4L}{3}.
$$

The following allowed mode contains five-quarters of a wavelength:

$$
L=\frac{5\lambda_5}{4},
$$

so

$$
\lambda_5=\frac{4L}{5}.
$$

In general,

$$
L=m\frac{\lambda_m}{4},
\qquad
m=1,3,5,\ldots
$$

Therefore,

$$
\boxed{
\lambda_m=\frac{4L}{m},
\qquad
m=1,3,5,\ldots
}
$$

and

$$
\boxed{
f_m=\frac{mv}{4L}=mf_1,
\qquad
m=1,3,5,\ldots
}.
$$

Only the odd harmonics are permitted:

$$
\boxed{
f_1,\ 3f_1,\ 5f_1,\ 7f_1,\ldots
}.
$$

The third harmonic is the **second allowed resonance**, and the fifth harmonic is the **third allowed resonance**. There are no second or fourth harmonics in the ideal closed–open pipe.

# Speed of Sound

For sound waves in air under typical conditions, use

$$
\boxed{
v\approx343\ \mathrm{m/s}
}.
$$

The speed of sound varies with temperature and other properties of the medium, but $343\ \mathrm{m/s}$ is the value used in these examples.

# Worked Example: Third Harmonic of a Closed–Open Pipe

Consider a pipe that is closed at one end and open at the other, with length

$$
L=0.85\ \mathrm{m}.
$$

Find the frequency of the third harmonic.

For a closed–open pipe,

$$
f_m=\frac{mv}{4L}
$$

for odd values of $m$.

Using $m=3$,

$$
f_3
=
\frac{3v}{4L}.
$$

Substituting the known values,

$$
f_3
=
\frac{
3(343\ \mathrm{m/s})
}{
4(0.85\ \mathrm{m})
}.
$$

Therefore,

$$
f_3
\approx
302.6\ \mathrm{Hz}.
$$

To the appropriate precision,

$$
\boxed{
f_3\approx3.0\times10^2\ \mathrm{Hz}
}.
$$

The corresponding fundamental frequency is

$$
f_1
=
\frac{
343\ \mathrm{m/s}
}{
4(0.85\ \mathrm{m})
}
\approx100.9\ \mathrm{Hz},
$$

which confirms that

$$
f_3=3f_1.
$$

# Worked Example: Fifth Harmonic of the Same Pipe

For the fifth harmonic,

$$
f_5
=
\frac{5v}{4L}.
$$

Substituting,

$$
f_5
=
\frac{
5(343\ \mathrm{m/s})
}{
4(0.85\ \mathrm{m})
}.
$$

Therefore,

$$
f_5
\approx504.4\ \mathrm{Hz}.
$$

Thus,

$$
\boxed{
f_5\approx5.0\times10^2\ \mathrm{Hz}
}.
$$

Because

$$
f_3=3f_1
$$

and

$$
f_5=5f_1,
$$

the fifth and third harmonics are related by

$$
\frac{f_5}{f_3}
=
\frac{5f_1}{3f_1}
=
\frac{5}{3}.
$$

Therefore,

$$
\boxed{
f_5=\frac{5}{3}f_3
}.
$$

# Strategy for Standing-Wave Problems

## 1. Identify the Boundary Conditions

Determine whether each end must be a displacement node or antinode.

- A fixed string end is a node.
- A closed pipe end is a displacement node.
- An open pipe end is a displacement antinode.

## 2. Sketch the Requested Mode

Draw the simplest standing-wave pattern that satisfies the boundary conditions, then add the required number of additional segments for the requested harmonic.

## 3. Relate the Length to the Wavelength

For a fixed–fixed string, open–open pipe, or closed–closed pipe:

$$
\lambda_m=\frac{2L}{m},
\qquad
m=1,2,3,\ldots
$$

For a closed–open pipe:

$$
\lambda_m=\frac{4L}{m},
\qquad
m=1,3,5,\ldots
$$

## 4. Determine the Wave Speed

For a string,

$$
v=\sqrt{\frac{T}{\mu}}.
$$

For sound in air under typical conditions,

$$
v\approx343\ \mathrm{m/s}.
$$

## 5. Calculate the Frequency

Use

$$
f_m=\frac{v}{\lambda_m}.
$$

## 6. Check the Result

Confirm that:

- The answer has units of hertz.
- Higher harmonics have higher frequencies.
- The node and antinode pattern satisfies the boundary conditions.
- A closed–open pipe contains only odd harmonics.

# Summary

When waves overlap in a linear medium, their displacements add:

$$
\boxed{
y_{\mathrm{net}}
=
\sum_i y_i
}.
$$

In-phase waves interfere constructively. Equal waves separated by $\pi$ radians interfere destructively.

A reflection from a fixed end is inverted, while a reflection from a free end is not inverted.

A standing wave contains fixed nodes and antinodes. It forms only when the wavelength and boundary conditions permit a resonant mode.

For a string fixed at both ends,

$$
\boxed{
\lambda_m=\frac{2L}{m}
}
$$

and

$$
\boxed{
f_m=\frac{mv}{2L}=mf_1,
\qquad
m=1,2,3,\ldots
}.
$$

The wave speed on a string is

$$
\boxed{
v=\sqrt{\frac{T}{\mu}}
}
$$

with

$$
\boxed{
\mu=\frac{m_{\mathrm{wire}}}{L}
}.
$$

For open–open and closed–closed pipes,

$$
\boxed{
\lambda_m=\frac{2L}{m}
}
$$

and

$$
\boxed{
f_m=\frac{mv}{2L}=mf_1,
\qquad
m=1,2,3,\ldots
}.
$$

For a closed–open pipe,

$$
\boxed{
\lambda_m=\frac{4L}{m}
}
$$

and

$$
\boxed{
f_m=\frac{mv}{4L}=mf_1,
\qquad
m=1,3,5,\ldots
}.
$$

Closed–open pipes support only odd harmonics.

The principal standing-wave relationships are:

| System | End conditions | Allowed $m$ | Wavelengths | Frequencies |
|---|---|---:|---|---|
| Fixed–fixed string | Node–node | $1,2,3,\ldots$ | $\lambda_m=\dfrac{2L}{m}$ | $f_m=\dfrac{mv}{2L}$ |
| Open–open pipe | Antinode–antinode | $1,2,3,\ldots$ | $\lambda_m=\dfrac{2L}{m}$ | $f_m=\dfrac{mv}{2L}$ |
| Closed–closed pipe | Node–node | $1,2,3,\ldots$ | $\lambda_m=\dfrac{2L}{m}$ | $f_m=\dfrac{mv}{2L}$ |
| Closed–open pipe | Node–antinode | $1,3,5,\ldots$ | $\lambda_m=\dfrac{4L}{m}$ | $f_m=\dfrac{mv}{4L}$ |

---

Up Next: [Phase Difference and Two-Source Interference](../../2026-07-30-M5-5/Source/Lecture-Transcript.md)
Previous: [Sound Intensity, Decibels, and the Doppler Effect](../../2026-07-28-M5-3/Source/Lecture-Transcript.md)

---
