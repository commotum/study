# Physics 212 — Phase Difference and Two-Source Interference

## Course Announcements

Welcome back to Physics 212.

Quiz 2 scores have been posted, and Quiz 2X is now open. Because the assignment was not available by Monday, Quiz 2X will remain open until Tuesday at $6{:}00\text{ PM}$.

We are also preparing for Quiz 3, which covers all of the wave material presented since Quiz 2, including today’s lecture. You should begin preparing your Quiz 3 note sheet.

The Quiz 3 schedule is:

- Proctorio version opens Saturday at $5{:}00\text{ PM}$.
- Proctorio version closes Monday at $5{:}00\text{ PM}$.
- Zoom-proctored sessions are Monday at $11{:}00\text{ AM}$ and $6{:}00\text{ PM}$.

We briefly introduced beats during our discussion of superposition. However, beating will not be covered further in class and will not appear on Quiz 3.

## Review of Superposition and Interference

Yesterday, we began discussing the addition of waves and the formation of standing waves. Today, we will develop the idea of **phase difference**, which allows us to determine whether two waves interfere constructively, destructively, or somewhere between those two extremes.

The principle of superposition states that when waves overlap, their displacements add:

$$
D_{\text{total}}=D_1+D_2.
$$

If the crest of one wave overlaps the crest of another, their displacements reinforce one another. This is **constructive interference**.

If the crest of one wave overlaps the trough of another, their displacements oppose one another. This is **destructive interference**.

## Interference from Two Sound Sources

Consider two identical speakers driven in phase. Being in phase means that both speaker cones move outward at the same time and inward at the same time.

As the speakers oscillate, each produces alternating regions of compression and rarefaction:

- A compression may be represented by a light-colored wavefront.
- A rarefaction may be represented by a dark-colored wavefront.
- The undisturbed or equilibrium pressure may be represented by gray.

Where a compression from one speaker overlaps a compression from the other, the waves interfere constructively. The same is true when two rarefactions overlap.

Where a compression overlaps a rarefaction, the waves interfere destructively.

The resulting interference pattern contains alternating lines of constructive and destructive interference. Increasing the frequency decreases the wavelength, causing more of these interference regions to appear within the same area.

A point of complete constructive interference is not always at a compression or always at a rarefaction. Instead, the air at that point undergoes the maximum possible pressure oscillation. At one instant it may be strongly compressed, at another strongly rarefied, and at another passing through equilibrium.

Similarly, a line of complete destructive interference is a nodal line where the two pressure variations cancel.

## Identifying Interference Graphically

Suppose circular blue lines represent crests traveling outward from two coherent sources. The troughs are located halfway between successive crest lines.

For the points shown in the example:

- At point $P$, a crest from one source overlaps a crest from the other. Therefore, $P$ is a point of complete constructive interference.
- At point $R$, a trough from one source overlaps a trough from the other. Therefore, $R$ is also a point of complete constructive interference.
- At point $Q$, a crest overlaps a trough. Therefore, $Q$ is a point of complete destructive interference.

Other points may have phase differences that produce only partial constructive or destructive interference.

## Phase of a Sinusoidal Wave

Consider a sinusoidal traveling wave:

$$
D(x,t)=A\sin(kx-\omega t+\phi_0).
$$

The quantities are:

- $A$: amplitude
- $k$: wave number
- $\omega$: angular frequency
- $\phi_0$: initial phase

The complete argument of the sine function is the phase:

$$
\phi(x,t)=kx-\omega t+\phi_0.
$$

The initial phase $\phi_0$ describes the phase at $x=0$ and $t=0$. The full phase $\phi(x,t)$ describes the state of the oscillation at any position and time.

The wave number is related to wavelength by:

$$
k=\frac{2\pi}{\lambda}.
$$

## Phase Difference Between Two Positions on One Wave

Choose two positions, $x_1$ and $x_2$, on the same wave. At a particular time $t$, the phases at those positions are:

$$
\phi_1=kx_1-\omega t+\phi_0
$$

and

$$
\phi_2=kx_2-\omega t+\phi_0.
$$

The phase difference is:

$$
\Delta\phi=\phi_2-\phi_1.
$$

Substituting the two phases gives:

$$
\Delta\phi
=
\left(kx_2-\omega t+\phi_0\right)
-
\left(kx_1-\omega t+\phi_0\right).
$$

The time-dependent terms and initial phases cancel:

$$
\Delta\phi=kx_2-kx_1.
$$

Therefore:

$$
\Delta\phi=k(x_2-x_1).
$$

Defining

$$
\Delta x=x_2-x_1,
$$

we obtain:

$$
\Delta\phi=k\Delta x.
$$

Using $k=2\pi/\lambda$:

$$
\boxed{\Delta\phi=\frac{2\pi\Delta x}{\lambda}}.
$$

This result makes physical sense:

- Points separated by one wavelength have a phase difference of $2\pi$.
- Points separated by half a wavelength have a phase difference of $\pi$.
- Points separated by one-quarter wavelength have a phase difference of $\pi/2$.

## Phase Difference Between Waves from Two Sources

Now consider two sources producing waves with the same frequency and wavelength. They therefore have the same values of $k$ and $\omega$, but they may have different initial phases.

Let $r_1$ and $r_2$ be the distances traveled by the two waves before reaching an observation point. Their displacements at that point may be written as:

$$
D_1(r_1,t)
=
A\sin(kr_1-\omega t+\phi_{1,0})
$$

and

$$
D_2(r_2,t)
=
A\sin(kr_2-\omega t+\phi_{2,0}).
$$

The phases are:

$$
\phi_1=kr_1-\omega t+\phi_{1,0}
$$

and

$$
\phi_2=kr_2-\omega t+\phi_{2,0}.
$$

The phase difference is:

$$
\Delta\phi=\phi_2-\phi_1.
$$

Substitution gives:

$$
\Delta\phi
=
\left(kr_2-\omega t+\phi_{2,0}\right)
-
\left(kr_1-\omega t+\phi_{1,0}\right).
$$

The time-dependent terms cancel:

$$
\Delta\phi
=
k(r_2-r_1)
+
(\phi_{2,0}-\phi_{1,0}).
$$

Define the path difference as:

$$
\Delta r=r_2-r_1,
$$

and the difference between the sources’ initial phases as:

$$
\Delta\phi_0=\phi_{2,0}-\phi_{1,0}.
$$

The general phase-difference equation is therefore:

$$
\Delta\phi=k\Delta r+\Delta\phi_0.
$$

Using $k=2\pi/\lambda$:

$$
\boxed{
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}
+
\Delta\phi_0
}.
$$

Two factors determine the final phase difference:

1. The difference in the distances traveled by the waves
2. The initial phase difference between the sources

## Initial Phase Difference

If the sources begin in phase, then:

$$
\Delta\phi_0=0.
$$

If the sources begin completely out of phase, then:

$$
\Delta\phi_0=\pi.
$$

More generally, the initial phase difference may have any value between these cases.

## Conditions for Constructive Interference

Complete constructive interference occurs when the waves arrive in phase. Their final phase difference must be an integer multiple of $2\pi$:

$$
\boxed{\Delta\phi=2\pi m},
$$

where:

$$
m=0,\pm1,\pm2,\ldots
$$

Examples include:

$$
\Delta\phi=0,\ 2\pi,\ 4\pi,\ldots
$$

These phase differences all represent equivalent points in an oscillation cycle.

For sources that begin in phase, $\Delta\phi_0=0$, so:

$$
\frac{2\pi\Delta r}{\lambda}=2\pi m.
$$

Canceling $2\pi$ gives the familiar constructive-interference condition:

$$
\boxed{\Delta r=m\lambda}.
$$

Thus, waves from in-phase sources interfere constructively when their path difference is an integer multiple of the wavelength.

## Conditions for Destructive Interference

Complete destructive interference occurs when the waves arrive $180^\circ$ out of phase. The final phase difference must be an odd multiple of $\pi$:

$$
\boxed{\Delta\phi=(2m+1)\pi}.
$$

Equivalently:

$$
\boxed{
\Delta\phi
=
2\pi\left(m+\frac{1}{2}\right)
}.
$$

Examples include:

$$
\Delta\phi=\pi,\ 3\pi,\ 5\pi,\ldots
$$

For sources that begin in phase:

$$
\frac{2\pi\Delta r}{\lambda}=(2m+1)\pi.
$$

The corresponding path-difference condition is:

$$
\boxed{
\Delta r
=
\left(m+\frac{1}{2}\right)\lambda
}.
$$

Thus, waves from in-phase sources interfere destructively when their path difference is a half-integer multiple of the wavelength.

If the sources begin completely out of phase, the constructive and destructive path-difference conditions are reversed.

## Example 1: Two Out-of-Phase Radio Antennas

Consider two radio antennas separated by:

$$
d=600\text{ m}.
$$

An observation point $P$ is located:

$$
r_1=800\text{ m}
$$

from the first antenna. The path from the second antenna to $P$ forms the hypotenuse of a right triangle:

$$
r_2=\sqrt{r_1^2+d^2}.
$$

The antennas emit radio waves with frequency:

$$
f=3.0\times10^6\text{ Hz}.
$$

Because radio waves are electromagnetic waves, they travel at approximately the speed of light:

$$
c=3.0\times10^8\text{ m/s}.
$$

The antennas are completely out of phase, so:

$$
\Delta\phi_0=\pi.
$$

We want to determine whether point $P$ experiences constructive interference, destructive interference, or neither.

### Determine the Wavelength

The wave-speed relationship is:

$$
c=\lambda f.
$$

Therefore:

$$
\lambda=\frac{c}{f}.
$$

Substituting:

$$
\lambda
=
\frac{3.0\times10^8\text{ m/s}}
{3.0\times10^6\text{ Hz}}.
$$

Thus:

$$
\lambda=100\text{ m}.
$$

### Determine the Path Difference

The second path length is:

$$
r_2
=
\sqrt{(800\text{ m})^2+(600\text{ m})^2}.
$$

Therefore:

$$
r_2=1000\text{ m}.
$$

The path difference is:

$$
\Delta r=r_2-r_1.
$$

Thus:

$$
\Delta r=1000\text{ m}-800\text{ m}=200\text{ m}.
$$

This is equal to two wavelengths:

$$
\frac{\Delta r}{\lambda}
=
\frac{200\text{ m}}{100\text{ m}}
=
2.
$$

### Determine the Phase Difference

Use:

$$
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}
+
\Delta\phi_0.
$$

Substituting:

$$
\Delta\phi
=
2\pi\left(\frac{200}{100}\right)+\pi.
$$

Therefore:

$$
\Delta\phi=4\pi+\pi=5\pi.
$$

Because $5\pi$ is an odd multiple of $\pi$, the waves undergo complete destructive interference:

$$
\boxed{\text{Point }P\text{ is a point of complete destructive interference.}}
$$

It is important to include the initial phase difference. If we forgot the additional $\pi$, we would incorrectly obtain $4\pi$ and conclude that the interference was constructive.

## Example 2: Phase Difference Between Two Flutes

Two flutes emit the same note at:

$$
f=830\text{ Hz}.
$$

The flutes are in phase, so:

$$
\Delta\phi_0=0.
$$

Because these are sound waves in air, use:

$$
v=343\text{ m/s}.
$$

Suppose flute $A$ and flute $B$ are located on opposite sides of the $y$-axis. An observation point $P$ lies on the $y$-axis.

Let the horizontal distances of the flutes from the $y$-axis be $x_1$ and $x_2$, and let the vertical coordinate of $P$ be $y$. The two path lengths are:

$$
r_1=\sqrt{x_1^2+y^2}
$$

and

$$
r_2=\sqrt{x_2^2+y^2}.
$$

The path difference is:

$$
\Delta r=r_2-r_1.
$$

Therefore:

$$
\Delta r
=
\sqrt{x_2^2+y^2}
-
\sqrt{x_1^2+y^2}.
$$

Since:

$$
\lambda=\frac{v}{f},
$$

we have:

$$
\frac{1}{\lambda}=\frac{f}{v}.
$$

The phase difference becomes:

$$
\Delta\phi
=
\frac{2\pi f}{v}\Delta r+\Delta\phi_0.
$$

Because $\Delta\phi_0=0$:

$$
\Delta\phi
=
\frac{2\pi f}{v}
\left(
\sqrt{x_2^2+y^2}
-
\sqrt{x_1^2+y^2}
\right).
$$

Substituting the coordinates from the diagram, along with $f=830\text{ Hz}$ and $v=343\text{ m/s}$, gives:

$$
\boxed{\Delta\phi\approx66\text{ rad}}.
$$

A phase difference may also be reduced modulo $2\pi$. Since phases that differ by an integer number of complete cycles are equivalent:

$$
66\text{ rad}\pmod{2\pi}
\approx3.17\text{ rad}.
$$

The unreduced value of $66\text{ rad}$ and the equivalent phase of approximately $3.17\text{ rad}$ describe the same relative phase.

## Example 3: First Position of Maximum Sound Intensity

Speaker $A$ is located at the origin:

$$
A=(0,0).
$$

Speaker $B$ is located a distance $y$ below the origin:

$$
B=(0,-y).
$$

The speakers are in phase and emit sound with wavelength $\lambda$. We want to find the first position on the positive $x$-axis where the sound intensity is a maximum.

For the numerical example:

$$
y=2.2\text{ m}
$$

and

$$
\lambda=0.50\text{ m}.
$$

Let the observation point be:

$$
P=(x,0).
$$

The distance from speaker $A$ to $P$ is:

$$
r_1=x.
$$

The distance from speaker $B$ to $P$ is:

$$
r_2=\sqrt{x^2+y^2}.
$$

The path difference is therefore:

$$
\Delta r=r_2-r_1.
$$

Thus:

$$
\Delta r=\sqrt{x^2+y^2}-x.
$$

Maximum sound intensity occurs when the waves interfere completely constructively. Because the speakers are in phase:

$$
\Delta r=m\lambda,
$$

where $m$ is a positive integer.

Therefore:

$$
\sqrt{x^2+y^2}-x=m\lambda.
$$

We should keep $m$ in the equation until the geometry has been solved. Different values of $m$ correspond to different interference maxima.

### Solve for the Position

Begin with:

$$
\sqrt{x^2+y^2}-x=m\lambda.
$$

Add $x$ to both sides:

$$
\sqrt{x^2+y^2}=m\lambda+x.
$$

Square both sides:

$$
x^2+y^2=(m\lambda+x)^2.
$$

Expand the right side:

$$
x^2+y^2
=
m^2\lambda^2+2m\lambda x+x^2.
$$

Cancel $x^2$:

$$
y^2=m^2\lambda^2+2m\lambda x.
$$

Rearrange:

$$
y^2-m^2\lambda^2=2m\lambda x.
$$

Therefore:

$$
\boxed{
x
=
\frac{y^2-m^2\lambda^2}{2m\lambda}
}.
$$

This can also be written as:

$$
\boxed{
x
=
\frac{y^2}{2m\lambda}
-
\frac{m\lambda}{2}
}.
$$

The value $m=0$ cannot be used in this expression. It would require $\Delta r=0$, but the two paths are unequal at every finite position in this geometry.

### Substitute the Given Values

Using:

$$
y=2.2\text{ m}
$$

and

$$
\lambda=0.50\text{ m},
$$

the position becomes:

$$
x
=
\frac{(2.2\text{ m})^2}
{2m(0.50\text{ m})}
-
\frac{m(0.50\text{ m})}{2}.
$$

Therefore:

$$
x
=
\left(
\frac{4.84}{m}
-
0.25m
\right)\text{m}.
$$

Evaluating the allowed integer values gives:

| $m$ | $x$ |
|---:|---:|
| $1$ | $4.59\text{ m}$ |
| $2$ | $1.92\text{ m}$ |
| $3$ | $0.86\text{ m}$ |
| $4$ | $0.21\text{ m}$ |
| $5$ | $-0.28\text{ m}$ |
| $6$ | $-0.69\text{ m}$ |

We are looking for the first maximum encountered while moving to the right from the origin. This is the smallest positive value of $x$, which occurs for $m=4$:

$$
\boxed{x\approx0.21\text{ m}}.
$$

Values $m\geq5$ produce negative positions and therefore do not lie on the requested positive $x$-axis.

## Summary

The central equation for two-source interference is:

$$
\boxed{
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}
+
\Delta\phi_0
}.
$$

The final phase difference depends on both the path difference and the initial phase difference between the sources.

For complete constructive interference:

$$
\boxed{\Delta\phi=2\pi m}.
$$

For complete destructive interference:

$$
\boxed{\Delta\phi=(2m+1)\pi}.
$$

For sources that begin in phase:

$$
\boxed{\Delta r=m\lambda}
$$

produces constructive interference, while:

$$
\boxed{
\Delta r
=
\left(m+\frac{1}{2}\right)\lambda
}
$$

produces destructive interference.

When solving an interference problem:

1. Draw the source and observer geometry.
2. Calculate the two path lengths.
3. Find the path difference $\Delta r$.
4. Determine the initial phase difference $\Delta\phi_0$.
5. Use the appropriate wave speed to find $\lambda$ if necessary.
6. Calculate the final phase difference.
7. Compare the result with the constructive- and destructive-interference conditions.

Useful wave speeds for the note sheet are:

$$
\boxed{c=3.0\times10^8\text{ m/s}}
$$

for electromagnetic waves in vacuum, and:

$$
\boxed{v_{\text{sound}}\approx343\text{ m/s}}
$$

for sound in air under ordinary conditions.