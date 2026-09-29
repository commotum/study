# Physics 212: Wave Optics, Double-Slit Interference, and Diffraction Gratings

Welcome back to Physics 212.

# Course Announcements

Quiz 3 has concluded and is currently being graded. There will not be a Quiz 3X assignment because there is not enough time remaining in the term.

Yesterday’s class was canceled because of a power outage. The remaining lecture schedule has therefore been adjusted slightly.

## Remaining Lecture Schedule

Chapter 33 covers wave optics. Two class periods should provide enough time to cover the principal topics.

The tentative schedule is:

- Today: double-slit interference and an introduction to diffraction gratings
- Tomorrow: diffraction gratings and single-slit diffraction
- Monday: Snell’s law and refraction
- Tuesday: plane mirrors and thin converging lenses
- Wednesday: no lecture
- Thursday: final exam

We will not cover diverging lenses.

There will be no class on Wednesday because the asynchronous final exam will already be open. Introducing new material while the final exam is in progress would not be appropriate.

# Final Exam Information

The final exam is cumulative.

Approximately one-third to one-half of the exam will likely cover the new material from Chapters 33 and 34. The remaining questions will cover material from earlier in the course.

Practice problems will be posted for the new topics, although there will not be a complete practice final exam.

## Final Exam Schedule

The Proctorio version will:

- Open Tuesday at 5:00 p.m.
- Close Thursday at 5:00 p.m.

Live Zoom-proctored sessions will be offered Thursday at:

- 11:00 a.m.
- 6:00 p.m.

## Final Exam Structure

The final exam will contain three required parts.

### Part A

Part A will contain:

- Three multiple-choice questions
- One short written-response question

You will have:

- $20$ minutes to complete the questions
- $5$ additional minutes to upload your written work

### Part B

Part B will contain one longer written-response problem.

You will have:

- $20$ minutes to complete the problem
- $5$ additional minutes to upload your written work

### Part C

Part C will contain several multiple-choice questions.

You will have:

- $20$ minutes to complete the questions
- No additional upload period

Because the final has three parts, the 11:00 a.m. Zoom session will finish at approximately 12:20 p.m.

You may mix the available proctoring methods. For example, you may complete Parts A and B during the 11:00 a.m. Zoom session and complete Part C through Proctorio.

However:

- You must complete all three parts.
- You may attempt each part only once.

## Final Exam Note Sheet

A handwritten note sheet is required for the final exam.

It should include relevant material from Chapters 33 and 34 in addition to material from the earlier units. Upload the completed note sheet to the Final Notes assignment before beginning the exam.

This is a good time to begin adding the new wave-optics equations to your note sheet.

# Capstone Laboratory Deadline

The final day of the term is Friday. The Capstone Lab group report must therefore be submitted by Friday of Week 8 at the latest.

The usual Saturday laboratory deadline does not apply because Saturday falls after the end of the term.

# Introduction to Wave Optics

We now begin Chapter 33 and the study of **wave optics**.

Historically, physicists debated whether light should be understood as a particle or as a wave. Modern physics shows that light exhibits both particle-like and wave-like behavior, depending on the experiment being performed.

In this chapter, we will focus on experiments that demonstrate the wave nature of light.

# Particle and Wave Predictions for a Double Slit

Consider a barrier containing two narrow slits, with a detection screen placed behind it.

## Particle Prediction

Imagine firing paintballs randomly toward the barrier.

Some paintballs pass through the upper slit, while others pass through the lower slit. On the screen, we would expect two broad concentrations of paint:

- One aligned with the upper slit
- One aligned with the lower slit

A graph of the number of paintballs striking each position would contain two broad peaks.

This is the pattern expected from ordinary particles traveling along localized paths.

## Wave Prediction

Now imagine a plane wave approaching the same two slits.

When the wave reaches each narrow opening, the opening acts approximately like a new point source. Waves spread outward from both slits and overlap.

Where the waves arrive in phase, they interfere constructively.

Where the waves arrive out of phase, they interfere destructively.

The screen therefore displays alternating bright and dark bands rather than two simple peaks.

These bands are called **interference fringes**:

- Bright fringes correspond to constructive interference.
- Dark fringes correspond to destructive interference.

When light is sent through a double slit, it produces this interference pattern. The result demonstrates that light behaves as a wave in this experiment.

# Reflection, Refraction, and Diffraction

Several optical phenomena should be distinguished.

## Reflection

**Reflection** occurs when light encounters a surface and travels back into its original medium.

In ordinary language, the light bounces from the surface.

## Refraction

**Refraction** is the change in direction that occurs when light enters a medium in which its wave speed is different.

## Diffraction

**Diffraction** is the spreading of a wave as it passes through a narrow opening or around an obstacle.

When a plane wave reaches a narrow slit, the transmitted wave spreads beyond the opening rather than continuing only in a narrow straight line.

In a double-slit experiment, light diffracts through both slits. The two diffracted waves then overlap and interfere.

# The Double-Slit Interference Pattern

Suppose coherent laser light illuminates two narrow slits.

A laser produces light with a well-defined frequency and stable phase relationship. The light reaching the two slits is therefore coherent.

The waves emerging from the two slits have:

- The same frequency
- The same wavelength
- A constant relative phase

On the screen, the overlapping waves produce:

- A central bright fringe
- Additional bright fringes on both sides
- Dark fringes between consecutive bright fringes

The central bright fringe is called the **central maximum** and is assigned the order

$$
m=0.
$$

The next bright fringes are the first-order maxima:

$$
m=\pm1.
$$

The next pair are the second-order maxima:

$$
m=\pm2.
$$

The pattern continues symmetrically above and below the central maximum.

# Effect of Moving the Screen

Suppose the screen is moved farther from the double slit.

The same bright fringes occur at approximately the same angles, but the larger screen distance allows those angles to extend across greater vertical distances.

Therefore,

$$
\boxed{
\text{Increasing the screen distance spreads the fringes farther apart.}
}
$$

Moving the screen closer causes the fringes to move closer together.

We will derive this result mathematically.

# Phase Difference from the Two Slits

The waves reaching a point $P$ on the screen may be written as

$$
D_1(P,t)
=
A\sin(kr_1-\omega t+\phi_{1,0})
$$

and

$$
D_2(P,t)
=
A\sin(kr_2-\omega t+\phi_{2,0}),
$$

where:

- $r_1$ is the path length from slit 1 to point $P$,
- $r_2$ is the path length from slit 2 to point $P$,
- $k$ is the wave number,
- $\omega$ is the angular frequency, and
- $\phi_{1,0}$ and $\phi_{2,0}$ are the initial phases.

The phase difference at point $P$ is

$$
\Delta\phi
=
\left(
kr_2-\omega t+\phi_{2,0}
\right)
-
\left(
kr_1-\omega t+\phi_{1,0}
\right).
$$

The time terms cancel:

$$
\Delta\phi
=
k(r_2-r_1)
+
\left(
\phi_{2,0}-\phi_{1,0}
\right).
$$

For coherent light passing through a double slit, the two slits are illuminated in phase:

$$
\phi_{1,0}=\phi_{2,0}.
$$

Therefore,

$$
\phi_{2,0}-\phi_{1,0}=0.
$$

Define the path difference as

$$
\boxed{
\Delta r=r_2-r_1
}.
$$

The phase difference is then

$$
\Delta\phi=k\Delta r.
$$

Using

$$
\boxed{
k=\frac{2\pi}{\lambda}
},
$$

we obtain

$$
\boxed{
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}
}.
$$

# Conditions for Constructive and Destructive Interference

## Constructive Interference

Complete constructive interference occurs when the waves arrive with a phase difference equal to an integer multiple of $2\pi$:

$$
\Delta\phi=2\pi m,
$$

where

$$
m=0,\pm1,\pm2,\ldots
$$

Substituting the path-dependent phase difference gives

$$
2\pi m
=
\frac{2\pi\Delta r}{\lambda}.
$$

Canceling $2\pi$ produces

$$
\boxed{
\Delta r=m\lambda
}.
$$

Therefore, a bright fringe occurs whenever the path difference is an integer number of wavelengths.

## Destructive Interference

Complete destructive interference occurs when the waves arrive with an odd multiple of $\pi$ phase difference:

$$
\Delta\phi
=
(2m+1)\pi.
$$

Substituting the phase-difference equation gives

$$
\boxed{
\Delta r
=
\left(
m+\frac{1}{2}
\right)\lambda
}.
$$

Therefore, a dark fringe occurs whenever the path difference is a half-integer number of wavelengths.

# Double-Slit Geometry

Let:

- $d$ be the distance between the centers of the two slits,
- $L$ be the distance from the slits to the screen,
- $y_m$ be the position of the $m$th bright fringe relative to the center, and
- $\theta_m$ be the angle from the central axis to that fringe.

Because the screen is much farther from the slits than the slits are from one another, the two paths to point $P$ are nearly parallel.

The resulting geometry gives

$$
\boxed{
\Delta r=d\sin\theta
}.
$$

For a bright fringe,

$$
\Delta r=m\lambda.
$$

Combining these equations gives the exact angular condition for a double-slit maximum:

$$
\boxed{
d\sin\theta_m=m\lambda
}.
$$

This equation determines the angle of each bright fringe.

The screen geometry gives

$$
\boxed{
\tan\theta_m=\frac{y_m}{L}
}.
$$

Without a small-angle approximation, the fringe position is

$$
\boxed{
y_m
=
L\tan
\left[
\sin^{-1}
\left(
\frac{m\lambda}{d}
\right)
\right]
}.
$$

# Small-Angle Approximation

In a typical double-slit experiment,

$$
L\gg d,
$$

and the fringes of interest are located at relatively small angles.

For a small angle measured in radians,

$$
\sin\theta\approx\theta
$$

and

$$
\tan\theta\approx\theta.
$$

Therefore,

$$
\sin\theta_m
\approx
\tan\theta_m
\approx
\theta_m.
$$

Starting with

$$
d\sin\theta_m=m\lambda,
$$

we use

$$
\sin\theta_m\approx\theta_m
$$

to obtain

$$
d\theta_m\approx m\lambda.
$$

Thus,

$$
\theta_m
\approx
\frac{m\lambda}{d}.
$$

From the screen geometry,

$$
\tan\theta_m=\frac{y_m}{L}.
$$

Using

$$
\tan\theta_m\approx\theta_m,
$$

we obtain

$$
\frac{y_m}{L}
\approx
\frac{m\lambda}{d}.
$$

Therefore, the approximate position of the $m$th bright fringe is

$$
\boxed{
y_m
\approx
\frac{m\lambda L}{d}
}.
$$

This is a linear relationship in $m$, so the bright fringes are approximately evenly spaced.

# Fringe Spacing

The distance between two adjacent bright fringes is

$$
\Delta y
=
y_{m+1}-y_m.
$$

Using

$$
y_m
\approx
\frac{m\lambda L}{d},
$$

we obtain

$$
y_{m+1}
\approx
\frac{(m+1)\lambda L}{d}.
$$

Therefore,

$$
\Delta y
=
\frac{(m+1)\lambda L}{d}
-
\frac{m\lambda L}{d}.
$$

The $m$ terms cancel:

$$
\boxed{
\Delta y
\approx
\frac{\lambda L}{d}
}.
$$

The approximate fringe spacing depends on three quantities:

- Increasing the wavelength $\lambda$ increases the fringe spacing.
- Increasing the screen distance $L$ increases the fringe spacing.
- Increasing the slit separation $d$ decreases the fringe spacing.

This confirms the earlier prediction that moving the screen farther from the slits moves the fringes farther apart.

## Positions of the Dark Fringes

Under the same small-angle approximation, the dark fringes occur at

$$
\boxed{
y_m^{(\mathrm{dark})}
\approx
\left(
m+\frac{1}{2}
\right)
\frac{\lambda L}{d}
}.
$$

Each dark fringe lies halfway between two consecutive bright fringes.

# Example: Path Difference at the Second Bright Fringe

Consider a point on the screen located at the second bright fringe.

The central maximum is

$$
m=0.
$$

The next bright fringe is

$$
m=1,
$$

and the second bright fringe is

$$
m=2.
$$

For a bright fringe,

$$
\Delta r=m\lambda.
$$

Therefore, at the second bright fringe,

$$
\Delta r=2\lambda.
$$

Thus,

$$
\boxed{
\text{One path is }2\lambda\text{ longer than the other.}
}
$$

The bright-fringe orders correspond directly to the path differences:

$$
\begin{aligned}
m=0
&\quad\Longrightarrow\quad
\Delta r=0,\\
m=1
&\quad\Longrightarrow\quad
\Delta r=\lambda,\\
m=2
&\quad\Longrightarrow\quad
\Delta r=2\lambda,\\
m=3
&\quad\Longrightarrow\quad
\Delta r=3\lambda.
\end{aligned}
$$

# Intensity as a Function of Screen Position

The interference pattern may be represented by a graph of light intensity versus position on the screen.

Each intensity maximum corresponds to a bright fringe, while each zero or minimum corresponds to a dark fringe.

In an ideal double-slit model with extremely narrow slits, the interference maxima have equal peak intensity. In a real experiment, each slit has a finite width, so the double-slit pattern lies beneath a broader single-slit diffraction envelope. As a result, the central maximum is generally brightest and the outer maxima gradually become weaker.

The distance between neighboring intensity peaks is the fringe spacing $\Delta y$.

# Worked Example: Finding a Laser Wavelength

A double-slit interference pattern appears on a screen located

$$
L=0.85\ \mathrm{m}
$$

from the slits.

The centers of the slits are separated by

$$
d=0.062\ \mathrm{mm}.
$$

The intensity graph shows that adjacent bright fringes are separated by

$$
\Delta y=1.0\ \mathrm{cm}.
$$

Find the wavelength of the laser.

## 1. Convert the Quantities to SI Units

The slit separation is

$$
d
=
0.062\ \mathrm{mm}
=
6.2\times10^{-5}\ \mathrm{m}.
$$

The fringe spacing is

$$
\Delta y
=
1.0\ \mathrm{cm}
=
1.0\times10^{-2}\ \mathrm{m}.
$$

## 2. Use the Fringe-Spacing Equation

For a double slit at small angles,

$$
\Delta y
=
\frac{\lambda L}{d}.
$$

Solving for the wavelength gives

$$
\boxed{
\lambda
=
\frac{\Delta y\,d}{L}
}.
$$

## 3. Substitute the Values

$$
\lambda
=
\frac{
\left(
1.0\times10^{-2}\ \mathrm{m}
\right)
\left(
6.2\times10^{-5}\ \mathrm{m}
\right)
}{
0.85\ \mathrm{m}
}.
$$

Therefore,

$$
\lambda
\approx
7.29\times10^{-7}\ \mathrm{m}.
$$

Because

$$
1\ \mathrm{nm}=10^{-9}\ \mathrm{m},
$$

the wavelength is

$$
\boxed{
\lambda\approx730\ \mathrm{nm}
}.
$$

This wavelength lies near the red edge of the visible spectrum.

# Diffraction Gratings

A **diffraction grating** contains a large number of equally spaced narrow slits.

A typical grating may contain hundreds or thousands of lines per millimeter.

Each slit acts as a coherent source. The waves from all of the slits interfere with one another.

Compared with a two-slit pattern, a diffraction grating produces:

- Much narrower principal maxima
- Sharper, better-defined bright fringes
- Large dark regions between the principal maxima
- Greater ability to separate nearby wavelengths

With many slits, destructive interference suppresses most of the intensity between the allowed principal maxima, while constructive interference concentrates the transmitted light into narrow peaks.

## Grating Spacing

If a diffraction grating contains $N$ lines across a width $W$, the spacing between adjacent lines is

$$
\boxed{
d=\frac{W}{N}
}.
$$

Equivalently, the line density is

$$
\boxed{
\frac{N}{W}=\frac{1}{d}
}.
$$

The units must be handled consistently. For example, if $N/W$ is given in lines per millimeter, the calculated spacing is initially in millimeters.

# Diffraction-Grating Maxima

The principal maxima of a diffraction grating satisfy the same angular condition as the bright fringes of a double slit:

$$
\boxed{
d\sin\theta_m=m\lambda
}.
$$

The screen geometry is

$$
\boxed{
\tan\theta_m=\frac{y_m}{L}
}.
$$

For diffraction gratings, the higher-order maxima may occur at angles too large for the small-angle approximation to be accurate.

The exact trigonometric relationships should therefore be used unless the angle has been shown to be small.

From the screen geometry,

$$
\boxed{
\theta_m
=
\tan^{-1}
\left(
\frac{y_m}{L}
\right)
}.
$$

The wavelength is then

$$
\boxed{
\lambda
=
\frac{d\sin\theta_m}{m}
}.
$$

Combining these equations gives

$$
\boxed{
\lambda
=
\frac{d}{m}
\sin
\left[
\tan^{-1}
\left(
\frac{y_m}{L}
\right)
\right]
}.
$$

Because

$$
\sin
\left[
\tan^{-1}
\left(
\frac{y_m}{L}
\right)
\right]
=
\frac{y_m}{
\sqrt{L^2+y_m^2}
},
$$

the wavelength may also be written as

$$
\boxed{
\lambda
=
\frac{d\,y_m}{
m\sqrt{L^2+y_m^2}
}
}.
$$

# Why the Grating Maxima Are Not Evenly Spaced

The angular maxima satisfy

$$
\sin\theta_m=\frac{m\lambda}{d}.
$$

Therefore,

$$
\theta_m
=
\sin^{-1}
\left(
\frac{m\lambda}{d}
\right).
$$

The corresponding screen positions are

$$
y_m
=
L\tan\theta_m.
$$

Thus,

$$
\boxed{
y_m
=
L\tan
\left[
\sin^{-1}
\left(
\frac{m\lambda}{d}
\right)
\right]
}.
$$

This is not a linear function of $m$. Consequently, the exact fringe spacing increases as the maxima move farther from the center.

Near the central maximum, where the angles are small, the spacing may be approximately uniform. At larger angles, the nonlinearity becomes important.

# Worked Example: Wavelength from a Diffraction Grating

A laser illuminates a diffraction grating with line spacing

$$
d=3.0\ \mu\mathrm{m}.
$$

The diffraction pattern appears on a screen located

$$
L=1.8\ \mathrm{m}
$$

from the grating.

The center of the third bright fringe is located

$$
y_3=120\ \mathrm{cm}
$$

from the central maximum.

Find the wavelength of the laser.

## 1. Convert the Quantities to SI Units

The grating spacing is

$$
d
=
3.0\ \mu\mathrm{m}
=
3.0\times10^{-6}\ \mathrm{m}.
$$

The fringe position is

$$
y_3
=
120\ \mathrm{cm}
=
1.20\ \mathrm{m}.
$$

Because this is the third bright fringe,

$$
m=3.
$$

## 2. Find the Diffraction Angle

Use

$$
\tan\theta_3
=
\frac{y_3}{L}.
$$

Therefore,

$$
\theta_3
=
\tan^{-1}
\left(
\frac{1.20\ \mathrm{m}}{1.8\ \mathrm{m}}
\right).
$$

Thus,

$$
\theta_3
\approx
33.7^\circ.
$$

This is not a small angle, so the small-angle approximation should not be used.

## 3. Find the Wavelength

The grating equation is

$$
d\sin\theta_3=3\lambda.
$$

Solving for $\lambda$ gives

$$
\lambda
=
\frac{d\sin\theta_3}{3}.
$$

Substituting,

$$
\lambda
=
\frac{
\left(
3.0\times10^{-6}\ \mathrm{m}
\right)
\sin(33.7^\circ)
}{
3
}.
$$

Therefore,

$$
\lambda
\approx
5.55\times10^{-7}\ \mathrm{m}.
$$

To the appropriate precision,

$$
\boxed{
\lambda\approx550\ \mathrm{nm}
}.
$$

This wavelength lies within the visible spectrum.

## Why the Small-Angle Approximation Fails

If the double-slit small-angle equation were used incorrectly,

$$
y_m
\approx
\frac{m\lambda L}{d},
$$

then

$$
\lambda
\approx
\frac{y_m d}{mL}.
$$

Substituting the values would give

$$
\lambda
\approx
6.7\times10^{-7}\ \mathrm{m}
=
670\ \mathrm{nm}.
$$

This differs substantially from the more accurate result:

$$
550\ \mathrm{nm}.
$$

The error occurs because

$$
\theta_3\approx33.7^\circ
$$

is too large for

$$
\sin\theta\approx\tan\theta\approx\theta
$$

to be accurate.

# Strategy for Double-Slit Problems

## 1. Identify the Known Quantities

Typical quantities include:

- Wavelength $\lambda$
- Slit separation $d$
- Screen distance $L$
- Fringe order $m$
- Fringe position $y_m$
- Adjacent fringe spacing $\Delta y$

## 2. Determine Whether the Small-Angle Approximation Applies

If the double-slit pattern is observed near the center of a distant screen, use

$$
\boxed{
y_m
\approx
\frac{m\lambda L}{d}
}
$$

or

$$
\boxed{
\Delta y
\approx
\frac{\lambda L}{d}
}.
$$

If the angle is not small, use the exact equations:

$$
d\sin\theta_m=m\lambda
$$

and

$$
\tan\theta_m=\frac{y_m}{L}.
$$

## 3. Keep the Variables Distinct

Do not confuse:

- $d$: slit separation
- $L$: distance from the slits to the screen
- $y_m$: position on the screen
- $\lambda$: wavelength
- $\Delta r$: path difference
- $\Delta y$: spacing between adjacent fringes

## 4. Convert All Values to Consistent Units

Common conversions include

$$
1\ \mathrm{mm}=10^{-3}\ \mathrm{m},
$$

$$
1\ \mu\mathrm{m}=10^{-6}\ \mathrm{m},
$$

and

$$
1\ \mathrm{nm}=10^{-9}\ \mathrm{m}.
$$

## 5. Check the Physical Meaning

For visible light, the wavelength should generally be within approximately

$$
400\ \mathrm{nm}
\lesssim
\lambda
\lesssim
750\ \mathrm{nm}.
$$

Also verify that:

- Increasing $L$ spreads the fringes apart.
- Increasing $\lambda$ spreads the fringes apart.
- Increasing $d$ moves the fringes closer together.
- The central maximum corresponds to $m=0$.
- The $m$th bright fringe has path difference $m\lambda$.
- A large angle requires exact trigonometric relationships.

# Summary

A double-slit experiment demonstrates the wave nature of light by producing alternating bright and dark interference fringes.

The path difference between the waves arriving at a point is

$$
\boxed{
\Delta r=r_2-r_1
}.
$$

For coherent sources, the phase difference is

$$
\boxed{
\Delta\phi
=
\frac{2\pi\Delta r}{\lambda}
}.
$$

Constructive interference occurs when

$$
\boxed{
\Delta r=m\lambda
}.
$$

Destructive interference occurs when

$$
\boxed{
\Delta r
=
\left(
m+\frac{1}{2}
\right)\lambda
}.
$$

For slits separated by distance $d$, the path difference is

$$
\boxed{
\Delta r=d\sin\theta
}.
$$

The angular condition for a bright fringe is

$$
\boxed{
d\sin\theta_m=m\lambda
}.
$$

The screen geometry is

$$
\boxed{
\tan\theta_m=\frac{y_m}{L}
}.
$$

For a double slit at small angles,

$$
\boxed{
y_m
\approx
\frac{m\lambda L}{d}
}
$$

and the adjacent bright-fringe spacing is

$$
\boxed{
\Delta y
\approx
\frac{\lambda L}{d}
}.
$$

A diffraction grating uses many equally spaced slits. Its principal maxima satisfy

$$
\boxed{
d\sin\theta_m=m\lambda
},
$$

but the exact trigonometric relationships should be retained when the diffraction angles are not small.

For a grating pattern measured on a screen,

$$
\boxed{
\theta_m
=
\tan^{-1}
\left(
\frac{y_m}{L}
\right)
}
$$

and

$$
\boxed{
\lambda
=
\frac{d\sin\theta_m}{m}
}.
$$

Double slits produce a broad interference pattern, while diffraction gratings produce much narrower and more sharply defined principal maxima.
