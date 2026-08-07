# Physics 212: Diffraction Gratings and Single-Slit Diffraction

Welcome back to Physics 212.

# Course Announcements

This is the next-to-last week of the term. The final day of the course is next Friday, and no work will be accepted after that date.

Make sure all outstanding assignments are submitted before the course ends.

## Laboratory Requirement

Pay particular attention to the laboratory requirements. To pass the course, you must:

- Submit every required laboratory report
- Earn a laboratory average of at least $70\%$

No laboratory score is dropped.

If you are missing a laboratory assignment, contact your laboratory TA immediately. Explain that you are completing the missing work and intend to submit it shortly.

You should also inspect the Canvas gradebook. If you submitted a laboratory report but do not see a score, email your TA and ask them to verify that the report was received and graded.

## Dropped Scores

The following scores have already been dropped according to the course policy:

- The lowest quiz score
- Three pre-lecture scores
- Three participation scores
- One homework score

Laboratory assignments are not dropped.

## Final Exam

The final exam is required and does not replace the lowest quiz score. It is a separate, cumulative assessment.

The Proctorio version will:

- Open Tuesday at 5:00 p.m.
- Close Thursday at 5:00 p.m.

Zoom-proctored versions will be offered Thursday at:

- 11:00 a.m.
- 6:00 p.m.

# Review: Double-Slit Interference

Wave optics is fundamentally concerned with interference.

Consider coherent laser light incident on a double slit. The incoming laser beam may be treated as a plane wave.

Because the light is coherent:

- The waves have the same frequency.
- They have the same wavelength in the same medium.
- They maintain a constant phase relationship.

The two narrow slits act approximately as coherent point sources. The waves emerging from them overlap and produce an interference pattern on a distant screen.

## Double-Slit Geometry

Let:

- $d$ be the distance between the centers of the slits,
- $L$ be the distance from the slits to the screen,
- $\theta_m$ be the angle to the $m$th bright fringe,
- $y_m$ be the position of the $m$th bright fringe on the screen, and
- $\lambda$ be the wavelength of the light.

The condition for a bright fringe is

$$
\boxed{
d\sin\theta_m=m\lambda
},
$$

where

$$
m=0,\pm1,\pm2,\ldots
$$

The screen geometry gives

$$
\boxed{
\tan\theta_m=\frac{y_m}{L}
}.
$$

These two equations are the general geometric relationships used for both double slits and diffraction gratings.

## Small-Angle Approximation for a Double Slit

For a typical double-slit experiment, the screen is far from the slits and the diffraction angles are small.

For a small angle measured in radians,

$$
\sin\theta_m
\approx
\tan\theta_m
\approx
\theta_m.
$$

Combining the two double-slit equations gives

$$
\boxed{
y_m
\approx
\frac{m\lambda L}{d}
}.
$$

Therefore, the bright fringes in a double-slit pattern are approximately evenly spaced.

The spacing between adjacent bright fringes is

$$
\boxed{
\Delta y
\approx
\frac{\lambda L}{d}
}.
$$

For diffraction gratings, the angles may be too large for this approximation. Unless the angle is known to be small, retain the exact sine and tangent relationships.

# Diffraction Gratings

A **diffraction grating** contains a large number of equally spaced narrow slits or lines.

When coherent light illuminates the grating, each opening acts as a source of diffracted light. The waves from all the openings interfere.

A diffraction grating produces:

- Narrow principal maxima
- Large dark regions between the maxima
- Better separation of nearby wavelengths than a double slit

The positions of the principal maxima satisfy

$$
\boxed{
d\sin\theta_m=m\lambda
}.
$$

The corresponding screen positions satisfy

$$
\boxed{
\tan\theta_m=\frac{y_m}{L}
}.
$$

The exact angle is therefore

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

The wavelength can then be determined from

$$
\boxed{
\lambda
=
\frac{d\sin\theta_m}{m}
}.
$$

Combining the equations gives

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

# Line Density and Grating Spacing

Suppose a diffraction grating contains $N$ slits across a width $W$.

If the distance between adjacent slits is $d$, then approximately

$$
W=Nd.
$$

Therefore,

$$
\boxed{
\frac{N}{W}=\frac{1}{d}
}.
$$

The quantity $N/W$ is the grating’s **line density**, often expressed in lines or slits per millimeter.

A smaller slit spacing corresponds to a larger line density.

# Worked Example: Finding the Number of Slits per Millimeter

A helium-neon laser with wavelength

$$
\lambda=633\ \mathrm{nm}
$$

illuminates a diffraction grating.

The screen is located

$$
L=2.4\ \mathrm{m}
$$

from the grating.

The distance between the two first-order bright fringes is

$$
2y_1=1.70\ \mathrm{m}.
$$

Determine the number of slits in a grating width of

$$
W=1.0\ \mathrm{mm}.
$$

## 1. Find the Position of One First-Order Fringe

The pattern is symmetric about the central maximum, so

$$
y_1
=
\frac{1.70\ \mathrm{m}}{2}.
$$

Therefore,

$$
\boxed{
y_1=0.85\ \mathrm{m}
}.
$$

## 2. Find the First-Order Angle

The screen geometry gives

$$
\tan\theta_1
=
\frac{y_1}{L}.
$$

Thus,

$$
\theta_1
=
\tan^{-1}
\left(
\frac{0.85\ \mathrm{m}}{2.4\ \mathrm{m}}
\right).
$$

Therefore,

$$
\theta_1\approx19.5^\circ.
$$

## 3. Relate the Grating Spacing to the Wavelength

For the first-order maximum,

$$
m=1.
$$

The grating equation is

$$
d\sin\theta_1=\lambda.
$$

Solving for $1/d$ gives

$$
\frac{1}{d}
=
\frac{\sin\theta_1}{\lambda}.
$$

Because

$$
\frac{N}{W}=\frac{1}{d},
$$

we have

$$
\frac{N}{W}
=
\frac{\sin\theta_1}{\lambda}.
$$

Solving for $N$ gives

$$
\boxed{
N
=
\frac{
W\sin\theta_1
}{
\lambda
}
}.
$$

## 4. Substitute the Values

Convert the wavelength and grating width to meters:

$$
\lambda
=
633\ \mathrm{nm}
=
633\times10^{-9}\ \mathrm{m},
$$

$$
W
=
1.0\ \mathrm{mm}
=
1.0\times10^{-3}\ \mathrm{m}.
$$

Then

$$
N
=
\frac{
\left(
1.0\times10^{-3}\ \mathrm{m}
\right)
\sin(19.5^\circ)
}{
633\times10^{-9}\ \mathrm{m}
}.
$$

Therefore,

$$
N\approx527.
$$

To two significant figures,

$$
\boxed{
N\approx5.3\times10^2\ \text{slits per millimeter}
}.
$$

Thus, the diffraction grating contains approximately

$$
\boxed{
530\ \text{slits/mm}
}.
$$

# Maximum Possible Diffraction Order

The diffraction-grating equation is

$$
d\sin\theta_m=m\lambda.
$$

Solving for the sine gives

$$
\sin\theta_m
=
\frac{m\lambda}{d}.
$$

A physical angle can exist only if

$$
-1
\leq
\sin\theta_m
\leq
1.
$$

Therefore,

$$
\left|
\frac{m\lambda}{d}
\right|
\leq1.
$$

For nonnegative diffraction orders,

$$
m\leq\frac{d}{\lambda}.
$$

The greatest possible order is therefore

$$
\boxed{
m_{\max}
=
\left\lfloor
\frac{d}{\lambda}
\right\rfloor
},
$$

where the floor function means the greatest integer no larger than $d/\lambda$.

This limit is a property of the diffraction geometry. Increasing the size of the screen cannot create an order for which

$$
\frac{m\lambda}{d}>1.
$$

Such an order would require

$$
\sin\theta_m>1,
$$

which is impossible.

# Worked Example: Number of Principal Maxima

A diffraction grating has spacing

$$
d=1.8\times10^{-6}\ \mathrm{m}
$$

and is illuminated by light with wavelength

$$
\lambda=633\times10^{-9}\ \mathrm{m}.
$$

Determine the total number of possible principal maxima.

## 1. Find the First Two Diffraction Angles

For the first-order maximum,

$$
\theta_1
=
\sin^{-1}
\left(
\frac{\lambda}{d}
\right).
$$

Substituting,

$$
\theta_1
=
\sin^{-1}
\left(
\frac{
633\times10^{-9}
}{
1.8\times10^{-6}
}
\right).
$$

Therefore,

$$
\boxed{
\theta_1\approx20.6^\circ
}.
$$

For the second-order maximum,

$$
\theta_2
=
\sin^{-1}
\left(
\frac{2\lambda}{d}
\right).
$$

Therefore,

$$
\boxed{
\theta_2\approx44.7^\circ
}.
$$

For the third-order maximum,

$$
\frac{3\lambda}{d}
=
\frac{
3(633\times10^{-9})
}{
1.8\times10^{-6}
}
\approx1.06.
$$

Because this is greater than $1$, the quantity

$$
\sin^{-1}
\left(
\frac{3\lambda}{d}
\right)
$$

is not defined for a real angle.

Therefore, the third-order maximum does not exist.

## 2. Determine the Maximum Order Directly

The maximum-order condition is

$$
m
\leq
\frac{d}{\lambda}.
$$

Substituting,

$$
m
\leq
\frac{
1.8\times10^{-6}
}{
633\times10^{-9}
}.
$$

Thus,

$$
m\leq2.84.
$$

Because $m$ must be an integer,

$$
\boxed{
m_{\max}=2
}.
$$

The permitted orders are

$$
m=-2,-1,0,1,2.
$$

Therefore, the total number of principal maxima is

$$
\boxed{
5
}.
$$

The central maximum contributes one fringe, and each nonzero order appears symmetrically on both sides.

In general, when all allowed orders reach the screen, the total number of principal maxima is

$$
\boxed{
N_{\mathrm{maxima}}
=
2m_{\max}+1
}.
$$

# Why Diffraction Gratings Matter

Different wavelengths satisfy

$$
d\sin\theta_m=m\lambda
$$

at different angles.

A diffraction grating therefore separates light according to wavelength. This makes it possible to analyze the spectrum produced or absorbed by a material.

## Atomic Spectra

Electrons in atoms occupy discrete energy levels.

An electron can absorb energy and move to a higher energy level. When it returns to a lower energy level, it may emit a photon whose energy is

$$
\boxed{
E=hf
}
$$

or equivalently

$$
\boxed{
E=\frac{hc}{\lambda}
}.
$$

Because each element has a distinct set of allowed electron-energy levels, each element absorbs or emits a characteristic set of wavelengths.

These spectral lines form a kind of fingerprint for the element.

## Astronomical Spectroscopy

Light from a star can be separated into its component wavelengths using a diffraction grating.

By comparing the observed spectral lines with laboratory measurements, astronomers can identify the elements present in:

- Stars
- Galaxies
- Interstellar gas
- Other astronomical objects

Light from the hot interior of a star passes through cooler gas in its outer layers. Atoms in that gas absorb particular wavelengths, producing dark absorption lines in the star’s spectrum.

Hot, low-density gas may instead produce bright emission lines.

Spectroscopy is therefore one of the most powerful methods for determining what distant objects are made of.

Because light takes time to travel, observing increasingly distant objects also allows astronomers to study progressively earlier periods in the history of the universe.

# Single-Slit Diffraction

We now turn from multiple slits to a single slit.

At first, it may seem surprising that a single opening can produce an interference pattern. A double slit provides two obvious sources, but a single slit appears to provide only one.

The explanation comes from the **Huygens–Fresnel principle**:

> Every point across a wavefront may be treated as a source of a secondary wavelet.

A slit has a finite width, so light emerging from different positions across the opening travels slightly different distances to a point on the screen.

These contributions interfere with one another and produce a diffraction pattern.

# Appearance of a Single-Slit Pattern

A single-slit diffraction pattern differs significantly from a double-slit pattern.

It contains:

- A broad, bright central maximum
- Dark minima on both sides of the center
- Weaker secondary maxima between consecutive minima
- Progressively weaker intensity farther from the center

The central maximum is approximately twice as wide as each secondary maximum.

We will label the single-slit minima using the integer $p$:

$$
p=1,2,3,\ldots
$$

The first minima occur at

$$
p=\pm1,
$$

the second minima at

$$
p=\pm2,
$$

and so forth.

There is no $p=0$ minimum. The center of the pattern is a maximum.

# Deriving the Single-Slit Minimum Condition

Let the slit width be $a$.

Consider light traveling toward an observation point at angle $\theta$.

For the first minimum, divide the slit into two equal halves. Pair each point in the upper half with a corresponding point in the lower half.

The paired points are separated by

$$
\frac{a}{2}.
$$

The path difference between each pair is

$$
\Delta r
=
\frac{a}{2}\sin\theta.
$$

For complete cancellation, each pair must arrive one-half wavelength out of phase:

$$
\Delta r=\frac{\lambda}{2}.
$$

Therefore,

$$
\frac{a}{2}\sin\theta_1
=
\frac{\lambda}{2}.
$$

Canceling the factor of $1/2$ gives

$$
a\sin\theta_1=\lambda.
$$

The general condition for the single-slit minima is

$$
\boxed{
a\sin\theta_p=p\lambda
},
$$

where

$$
p=\pm1,\pm2,\pm3,\ldots
$$

The value $p=0$ is excluded because the center is a bright maximum rather than a minimum.

Solving for the angle gives

$$
\boxed{
\sin\theta_p
=
\frac{p\lambda}{a}
}.
$$

# Positions of Single-Slit Minima

The screen geometry gives

$$
\boxed{
\tan\theta_p=\frac{y_p}{L}
},
$$

where:

- $y_p$ is the position of the $p$th minimum,
- $L$ is the distance from the slit to the screen, and
- $a$ is the width of the slit.

For small angles,

$$
\sin\theta_p
\approx
\tan\theta_p.
$$

Therefore,

$$
\frac{y_p}{L}
\approx
\frac{p\lambda}{a}.
$$

Solving for $y_p$ gives

$$
\boxed{
y_p
\approx
\frac{p\lambda L}{a}
}.
$$

This equation locates the **dark fringes** of a single-slit diffraction pattern.

That distinction is essential:

- In a double-slit pattern, $m$ commonly labels bright fringes.
- In this single-slit treatment, $p$ labels dark fringes.

Although the equations have similar forms, they identify different features of the patterns.

# Width of the Central Maximum

The first minima occur at

$$
y_{+1}
\approx
\frac{\lambda L}{a}
$$

and

$$
y_{-1}
\approx
-\frac{\lambda L}{a}.
$$

The central maximum extends from the first minimum on one side to the first minimum on the other.

Its width is therefore

$$
w_{\mathrm{central}}
=
y_{+1}-y_{-1}.
$$

Thus,

$$
\boxed{
w_{\mathrm{central}}
\approx
\frac{2\lambda L}{a}
}.
$$

The distance from the center of the pattern to either first minimum is

$$
\boxed{
y_1
\approx
\frac{\lambda L}{a}
}.
$$

# Worked Example: Finding the Screen Distance

A laser with wavelength

$$
\lambda=633\ \mathrm{nm}
$$

illuminates a single slit of width

$$
a=0.15\ \mathrm{mm}.
$$

The first minimum is located

$$
y_1=2.0\ \mathrm{cm}
$$

from the central maximum.

Determine the distance $L$ from the slit to the screen.

## 1. Convert to SI Units

The wavelength is

$$
\lambda
=
633\ \mathrm{nm}
=
633\times10^{-9}\ \mathrm{m}.
$$

The slit width is

$$
a
=
0.15\ \mathrm{mm}
=
1.5\times10^{-4}\ \mathrm{m}.
$$

The first-minimum position is

$$
y_1
=
2.0\ \mathrm{cm}
=
2.0\times10^{-2}\ \mathrm{m}.
$$

## 2. Use the First-Minimum Equation

For $p=1$,

$$
y_1
=
\frac{\lambda L}{a}.
$$

Solving for $L$ gives

$$
\boxed{
L
=
\frac{y_1a}{\lambda}
}.
$$

## 3. Substitute the Values

$$
L
=
\frac{
\left(
2.0\times10^{-2}\ \mathrm{m}
\right)
\left(
1.5\times10^{-4}\ \mathrm{m}
\right)
}{
633\times10^{-9}\ \mathrm{m}
}.
$$

Therefore,

$$
L\approx4.74\ \mathrm{m}.
$$

To two significant figures,

$$
\boxed{
L\approx4.7\ \mathrm{m}
}.
$$

# Approximate Positions of the Secondary Maxima

The exact secondary maxima of a single-slit pattern are not located perfectly halfway between consecutive minima. Finding their exact positions requires analyzing the single-slit intensity function.

For the level of approximation used here, however, a secondary maximum may be treated as lying approximately halfway between two adjacent minima.

The first secondary maximum lies approximately between the $p=1$ and $p=2$ minima:

$$
y_{\mathrm{bright},1}
\approx
\frac{y_1+y_2}{2}.
$$

The second secondary maximum lies approximately between the $p=2$ and $p=3$ minima:

$$
y_{\mathrm{bright},2}
\approx
\frac{y_2+y_3}{2}.
$$

Because

$$
y_p
\approx
\frac{p\lambda L}{a},
$$

the second secondary maximum is approximately

$$
y_{\mathrm{bright},2}
\approx
\frac{
2\lambda L/a
+
3\lambda L/a
}{
2
}.
$$

Therefore,

$$
\boxed{
y_{\mathrm{bright},2}
\approx
\frac{5\lambda L}{2a}
}.
$$

# Worked Example: Position of the Second Secondary Maximum

A laser illuminates a single slit of width $a$, producing a diffraction pattern on a screen located

$$
L=1.2\ \mathrm{m}
$$

away.

Determine the approximate distance from the central maximum to the second secondary bright fringe.

The second secondary maximum lies approximately halfway between the second and third minima:

$$
y_{\mathrm{bright},2}
\approx
\frac{y_2+y_3}{2}.
$$

Using

$$
y_p
\approx
\frac{p\lambda L}{a},
$$

we obtain

$$
y_{\mathrm{bright},2}
\approx
\frac{
2\lambda L/a
+
3\lambda L/a
}{
2
}.
$$

Thus,

$$
\boxed{
y_{\mathrm{bright},2}
\approx
\frac{5\lambda L}{2a}
}.
$$

Substituting the wavelength and slit width supplied in the problem gives

$$
y_{\mathrm{bright},2}
\approx
0.0139\ \mathrm{m}.
$$

Therefore,

$$
\boxed{
y_{\mathrm{bright},2}
\approx
0.014\ \mathrm{m}
}
$$

or

$$
\boxed{
y_{\mathrm{bright},2}
\approx
1.4\ \mathrm{cm}
}.
$$

# Comparing Double-Slit and Single-Slit Patterns

| Feature | Double slit | Single slit |
|---|---|---|
| Relevant dimension | Slit separation $d$ | Slit width $a$ |
| Primary cause | Interference between waves from two slits | Interference among waves from different parts of one slit |
| Bright-fringe condition | $d\sin\theta_m=m\lambda$ | Secondary maxima require a more detailed intensity analysis |
| Dark-fringe condition | $d\sin\theta=(m+\tfrac12)\lambda$ | $a\sin\theta_p=p\lambda$ |
| Small-angle position commonly used | $y_m\approx m\lambda L/d$ for bright fringes | $y_p\approx p\lambda L/a$ for dark fringes |
| Central maximum | Similar width to adjacent ideal interference fringes | Approximately twice as wide as the secondary maxima |
| Intensity away from center | Modified by a diffraction envelope | Secondary maxima rapidly become weaker |

The equations can look very similar, so always identify whether the integer labels a maximum or a minimum.

# Strategy for Diffraction Problems

## 1. Identify the Optical System

Determine whether the problem involves:

- A double slit
- A diffraction grating
- A single slit

The governing equations depend on the system.

## 2. Identify the Relevant Dimension

For a double slit or diffraction grating, use the slit spacing:

$$
d.
$$

For a single slit, use the slit width:

$$
a.
$$

Do not interchange these quantities.

## 3. Identify What the Order Number Represents

For a double slit or grating,

$$
d\sin\theta_m=m\lambda
$$

locates bright fringes.

For a single slit,

$$
a\sin\theta_p=p\lambda
$$

locates dark fringes.

## 4. Decide Whether the Small-Angle Approximation Is Appropriate

The exact screen geometry is

$$
\tan\theta=\frac{y}{L}.
$$

Use the small-angle approximation only when

$$
\theta\ll1\ \mathrm{rad}.
$$

Then

$$
\sin\theta
\approx
\tan\theta
\approx
\theta.
$$

Do not automatically use the small-angle double-slit formula for a diffraction grating.

## 5. Convert All Quantities to Consistent Units

Useful conversions include

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

## 6. Check Whether the Requested Order Can Exist

For a diffraction grating,

$$
\left|
\frac{m\lambda}{d}
\right|
\leq1.
$$

For a single slit,

$$
\left|
\frac{p\lambda}{a}
\right|
\leq1.
$$

An order that would require the magnitude of a sine to exceed $1$ cannot exist.

# Summary

For a double slit or diffraction grating, the bright fringes satisfy

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
}.
$$

A diffraction grating’s line density is related to its spacing by

$$
\boxed{
\frac{N}{W}=\frac{1}{d}
}.
$$

The largest possible diffraction order is

$$
\boxed{
m_{\max}
=
\left\lfloor
\frac{d}{\lambda}
\right\rfloor
}.
$$

When all allowed orders reach the screen, the total number of principal maxima is

$$
\boxed{
N_{\mathrm{maxima}}
=
2m_{\max}+1
}.
$$

For a single slit of width $a$, the dark fringes satisfy

$$
\boxed{
a\sin\theta_p=p\lambda
},
$$

where

$$
p=\pm1,\pm2,\pm3,\ldots
$$

At small angles, the positions of the single-slit minima are

$$
\boxed{
y_p
\approx
\frac{p\lambda L}{a}
}.
$$

The width of the single-slit central maximum is

$$
\boxed{
w_{\mathrm{central}}
\approx
\frac{2\lambda L}{a}
}.
$$

Double-slit equations commonly locate bright interference fringes, while the basic single-slit equation locates dark diffraction minima. Keeping that distinction clear is essential.