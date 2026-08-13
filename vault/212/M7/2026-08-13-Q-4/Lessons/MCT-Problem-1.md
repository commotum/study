# Choose the Angular or Screen-Position Form for Double-Slit Maxima

<!--
lesson-id: 212-M7-017
topic-code: MTH212.M7.17
-->

## Table of Contents

- [Introduction](#introduction)
- [Label a Bright Fringe by Its Path Difference](#bright-order)
- [Move from an Angle to a Screen Position](#angle-to-screen)
- [Use the Small-Angle Position Only After Checking](#small-angle-position)
- [Change the Wavelength Inside a Material](#material-wavelength)
- [Read Adjacent-Fringe Spacing](#fringe-spacing)
- [Summary](#summary)

## Prerequisites

- Use sine and tangent in a right triangle.
- Solve a multivariable equation for one requested symbol.
- Convert nanometers, millimeters, and centimeters to meters.
- Distinguish constructive from destructive interference.

---

<a id="introduction"></a>
## Introduction

For double-slit bright fringes, first label the order $m$. Then connect the interference condition to the screen geometry:

$$
\boxed{\Delta r=m\lambda}
\quad\longrightarrow\quad
\boxed{d\sin\theta_m=m\lambda}
\quad\longrightarrow\quad
\boxed{y_m=L\tan\theta_m}.
$$

Here,

| Symbol | Meaning |
|---|---|
| $d$ | center-to-center separation of the two slits |
| $L$ | distance from the slits to the screen |
| $y_m$ | signed screen position measured from the central maximum |
| $\theta_m$ | angle from the central axis to bright order $m$ |

The central bright fringe has $m=0$. Bright fringes on opposite sides use $m=\pm1,\pm2,\ldots$. If a question asks for a distance from the center, use the magnitude $|y_m|$.

The exact trigonometric route within the far-field double-slit model is

$$
\boxed{\theta_m=\sin^{-1}\left(\frac{m\lambda}{d}\right)},
\qquad
\boxed{y_m=L\tan\theta_m}.
$$

Choose the route from the requested quantity:

| Given and requested | Route |
|---|---|
| angle $\theta_m$; find $d$ or $\lambda$ | isolate it in $d\sin\theta_m=m\lambda$ |
| screen position $y_m$; exact trigonometry | $\theta_m=\tan^{-1}(y_m/L)$, then use the maximum condition |
| $d$, $\lambda$, and $m$; find $y_m$ exactly | $\theta_m=\sin^{-1}(m\lambda/d)$, then $y_m=L\tan\theta_m$ |
| screen position; small angle verified | $y_m\approx Lm\lambda/d$ |

Only after confirming that $|\theta_m|$ is small may the two steps collapse to

$$
\boxed{y_m\approx\frac{Lm\lambda}{d}}.
$$

The approximation uses $\sin\theta\approx\theta$ and $\tan\theta\approx\theta$ with $\theta$ in radians. Radian measure is necessary but does not by itself make an angle small.

When $d$, $\lambda$, and $m$ are given, the dimensionless value $q=|m|\lambda/d$ provides the check. A real bright-fringe angle requires $q\le1$; if $q$ is not much smaller than $1$, keep the exact trigonometric route. For a noncentral fringe, the small-angle magnitude $Lq=L|\sin\theta_m|$ is slightly below the exact magnitude $L|\tan\theta_m|$.

Before substituting, convert $\lambda$ and $d$ to the same length unit so that $m\lambda/d$ is dimensionless. Keep $L$ in the unit wanted for $y_m$.

---

<a id="bright-order"></a>
## Label a Bright Fringe by Its Path Difference

### M6-1 lecture worked case — second bright fringe

At a bright fringe, the two paths differ by an integer number of wavelengths:

$$
\Delta r=m\lambda.
$$

The second bright fringe away from the center has $|m|=2$, so the magnitude of the path difference is

$$
|\Delta r|=2\lambda.
$$

Half-integer path differences such as $1.5\lambda$ or $2.5\lambda$ belong to dark fringes, not bright fringes.

```quiz
type: radio
id: mct-p1-bright-path-difference
shuffle: true
content: |-
  What is the magnitude of the path difference at the third bright fringe away from the central maximum?
options:
- id: mct-p1-bright-path-difference-a
  content: |-
    $3\lambda$
  correct: true
  feedback: |-
    Bright fringes satisfy $|\Delta r|=|m|\lambda$. The third bright fringe has $|m|=3$, so its path-difference magnitude is $3\lambda$.
- id: mct-p1-bright-path-difference-b
  content: |-
    $0.5\lambda$
  feedback: |-
    A half-wavelength path difference gives the first dark fringe. Bright fringes require an integer multiple of $\lambda$; the third bright fringe requires $3\lambda$.
- id: mct-p1-bright-path-difference-c
  content: |-
    $2\lambda$
  feedback: |-
    This is the path difference at the second bright fringe. The order counts outward from $m=0$, so the third bright fringe has $|m|=3$.
- id: mct-p1-bright-path-difference-d
  content: |-
    $2.5\lambda$
  feedback: |-
    A half-integer multiple produces destructive interference. The third bright fringe is constructive and therefore uses the integer multiple $3\lambda$.
- id: mct-p1-bright-path-difference-e
  content: |-
    $4\lambda$
  feedback: |-
    Counting the central maximum as the first bright fringe shifts every order by one. The center is order $m=0$, so the third fringe away from it is $|m|=3$, not $4$.
```

---

<a id="angle-to-screen"></a>
## Move from an Angle to a Screen Position

### Source-video worked case 1 — `xaAthgG0o8o`, 00:00:01–00:07:31 and 00:07:33–00:10:42

A first-order bright fringe occurs at $1.5^\circ$ for light of wavelength $600\ \mathrm{nm}$. Find the slit separation. Then place a screen $4.5\ \mathrm m$ from the slits and find the first bright fringe's distance from the center.

The phrase *first-order bright fringe* gives $m=1$. Convert the wavelength:

$$
600\ \mathrm{nm}
\left(\frac{10^{-9}\ \mathrm m}{1\ \mathrm{nm}}\right)
=6.00\times10^{-7}\ \mathrm m.
$$

For the requested slit separation, isolate $d$ before substituting:

$$
d\sin\theta_1=\lambda
\quad\Longrightarrow\quad
d=\frac{\lambda}{\sin\theta_1}.
$$

Thus,

$$
d
=\frac{6.00\times10^{-7}}{\sin(1.5^\circ)}
=2.29\times10^{-5}\ \mathrm m
=0.0229\ \mathrm{mm}.
$$

The screen triangle has $\tan\theta_1=y_1/L$:

$$
y_1=L\tan\theta_1
=(4.5)\tan(1.5^\circ)
=0.11784\ \mathrm m
\approx0.118\ \mathrm m
=11.8\ \mathrm{cm}.
$$

**Approximation correction.** The video also calculates $y_1$ from $y_md=Lm\lambda$ and writes that relation with an equals sign. It should be $y_md\approx Lm\lambda$. Here $1.5^\circ=0.0262\ \mathrm{rad}$ is small, so the approximate and exact positions both round to $0.118\ \mathrm m$.

```quiz
type: radio
id: mct-p1-angle-to-spacing
shuffle: true
content: |-
  A second-order bright fringe appears at $2.4^\circ$ when $520\ \mathrm{nm}$ light passes through a double slit. What is the slit separation?
options:
- id: mct-p1-angle-to-spacing-a
  content: |-
    $0.0248\ \mathrm{mm}$
  correct: true
  feedback: |-
    Bright order $m=2$ satisfies $d\sin\theta_2=2\lambda$. Converting $520\ \mathrm{nm}=5.20\times10^{-7}\ \mathrm m$ gives $d=2(5.20\times10^{-7})/\sin(2.4^\circ)=2.48\times10^{-5}\ \mathrm m=0.0248\ \mathrm{mm}$.
- id: mct-p1-angle-to-spacing-b
  content: |-
    $0.0124\ \mathrm{mm}$
  feedback: |-
    This uses the first-order numerator $\lambda$. The marked fringe is second order, so the constructive path difference is $2\lambda$ and the slit separation is twice this value.
- id: mct-p1-angle-to-spacing-c
  content: |-
    $24.8\ \mathrm{mm}$
  feedback: |-
    This is a factor-of-$1000$ conversion error. The calculation gives $2.48\times10^{-5}\ \mathrm m$; multiplying meters by $1000\ \mathrm{mm/m}$ gives $0.0248\ \mathrm{mm}$, not $24.8\ \mathrm{mm}$.
- id: mct-p1-angle-to-spacing-d
  content: |-
    $0.0000436\ \mathrm{mm}$
  feedback: |-
    This multiplies by $\sin\theta_2$ instead of dividing. Since $d\sin\theta_2=2\lambda$, isolating $d$ requires $d=2\lambda/\sin\theta_2$.
- id: mct-p1-angle-to-spacing-e
  content: |-
    $0.0497\ \mathrm{mm}$
  feedback: |-
    This applies the order factor twice. The factor $m=2$ appears once in $d=m\lambda/\sin\theta_m$, giving $0.0248\ \mathrm{mm}$.
```

---

<a id="small-angle-position"></a>
## Use the Small-Angle Position Only After Checking

### Source-video worked case 2 — `xaAthgG0o8o`, 00:10:45–00:13:08

Light of wavelength $650\ \mathrm{nm}$ passes through slits separated by $0.050\ \mathrm{mm}$. A screen is $8.5\ \mathrm m$ away. Find the third-order bright fringe's distance from the center.

Normalize the units and label the order:

$$
\lambda=6.50\times10^{-7}\ \mathrm m,
\qquad
d=5.0\times10^{-5}\ \mathrm m,
\qquad
m=3.
$$

Check the dimensionless angle input:

$$
\frac{m\lambda}{d}
=\frac{3(6.50\times10^{-7})}{5.0\times10^{-5}}
=0.039.
$$

The exact angle is

$$
\theta_3=\sin^{-1}(0.039)=2.235^\circ,
$$

so the exact screen position is

$$
y_3=(8.5)\tan(2.235^\circ)
=0.33175\ \mathrm m.
$$

Because the angle is small, the source uses

$$
y_3\approx\frac{Lm\lambda}{d}
=\frac{(8.5)(3)(6.50\times10^{-7})}{5.0\times10^{-5}}
=0.3315\ \mathrm m
=33.15\ \mathrm{cm}.
$$

The approximation is about $0.076\%$ below the exact value here, so the source's small-angle result is justified at its reported precision.

```quiz
type: radio
id: mct-p1-exact-screen-position
shuffle: true
content: |-
  A double slit has $d=5.0\ \mu\mathrm m$ and is illuminated with $500\ \mathrm{nm}$ light. A screen is $1.2\ \mathrm m$ away. Find the third bright fringe's distance from the center without assuming a small angle.
options:
- id: mct-p1-exact-screen-position-a
  content: |-
    $0.377\ \mathrm m$
  correct: true
  feedback: |-
    Here $m\lambda/d=3(500\ \mathrm{nm})/(5.0\ \mu\mathrm m)=0.300$. The exact route gives $\theta_3=\sin^{-1}(0.300)=17.46^\circ$ and $y_3=(1.2)\tan(17.46^\circ)=0.377\ \mathrm m$.
- id: mct-p1-exact-screen-position-b
  content: |-
    $0.360\ \mathrm m$
  feedback: |-
    This is the small-angle value $Lm\lambda/d$. The exact angle is $17.46^\circ$, and the prompt says not to assume it is small; using $L\tan[\sin^{-1}(m\lambda/d)]$ gives $0.377\ \mathrm m$.
- id: mct-p1-exact-screen-position-c
  content: |-
    $0.121\ \mathrm m$
  feedback: |-
    This uses $m=1$ and finds the first bright fringe. The question asks for the third bright fringe, so the angle input must be $3\lambda/d=0.300$.
- id: mct-p1-exact-screen-position-d
  content: |-
    $0.250\ \mathrm m$
  feedback: |-
    This divides the angle input by $L$. Screen geometry says $y=L\tan\theta$, so the screen distance multiplies the tangent after $\theta=\sin^{-1}(m\lambda/d)$ is found.
- id: mct-p1-exact-screen-position-e
  content: |-
    $3.82\ \mathrm m$
  feedback: |-
    This uses $L/\tan\theta$ instead of $L\tan\theta$. From the screen triangle, $\tan\theta=y/L$, so $y=L\tan\theta$.
```

---

<a id="material-wavelength"></a>
## Change the Wavelength Inside a Material

### Source-video worked case 3 — `xaAthgG0o8o`, 00:13:11–00:16:22

Light has wavelength $550\ \mathrm{nm}$ in air and passes through two slits in water, whose refractive index is $1.33$. The screen is $3.6\ \mathrm m$ away, and the fourth bright fringe is $4.5\ \mathrm{mm}$ from the center. Find the slit separation.

Crossing into water changes the light's speed and wavelength, but not its frequency. Taking $n_{\text{air}}\approx1$,

$$
\lambda_{\text{water}}
=\frac{\lambda_{\text{air}}}{n_{\text{water}}}
=\frac{550\ \mathrm{nm}}{1.33}
=413.5\ \mathrm{nm}.
$$

For the exact route, use the screen geometry first:

$$
\theta_4
=\tan^{-1}\left(\frac{y_4}{L}\right)
=\tan^{-1}\left(\frac{4.5\times10^{-3}}{3.6}\right)
=0.0716^\circ.
$$

Then isolate the slit separation:

$$
d
=\frac{m\lambda_{\text{water}}}{\sin\theta_4}
=\frac{4(413.5\times10^{-9})}{\sin(0.0716^\circ)}
=1.32\times10^{-3}\ \mathrm m
=1.32\ \mathrm{mm}.
$$

The angle is very small, so the video's approximate calculation

$$
d\approx\frac{Lm\lambda_{\text{water}}}{y_4}
$$

also gives $1.32\ \mathrm{mm}$.

```quiz
type: radio
id: mct-p1-material-wavelength
shuffle: true
content: |-
  Light has wavelength $600\ \mathrm{nm}$ in air and passes through a double slit in glass with $n=1.50$. A screen is $4.0\ \mathrm m$ away, and the second bright fringe is $6.0\ \mathrm{mm}$ from the center. The angle is small. What is the slit separation?
options:
- id: mct-p1-material-wavelength-a
  content: |-
    $0.533\ \mathrm{mm}$
  correct: true
  feedback: |-
    Frequency stays fixed while the glass wavelength becomes $600/1.50=400\ \mathrm{nm}$. With $m=2$, the small-angle relation gives $d\approx Lm\lambda/y=(4.0)(2)(400\times10^{-9})/(6.0\times10^{-3})=0.533\ \mathrm{mm}$.
- id: mct-p1-material-wavelength-b
  content: |-
    $0.800\ \mathrm{mm}$
  feedback: |-
    This uses the $600\ \mathrm{nm}$ air wavelength in the slit equation. The interference occurs in glass, where the wavelength is $600/1.50=400\ \mathrm{nm}$.
- id: mct-p1-material-wavelength-c
  content: |-
    $0.267\ \mathrm{mm}$
  feedback: |-
    This omits the bright-fringe order. The second bright fringe has $m=2$, so the numerator is $Lm\lambda$, not merely $L\lambda$.
- id: mct-p1-material-wavelength-d
  content: |-
    $1.20\ \mathrm{mm}$
  feedback: |-
    This multiplies the air wavelength by the refractive index. Wavelength decreases in the higher-index material: $\lambda_{\text{glass}}=\lambda_{\text{air}}/n=400\ \mathrm{nm}$.
- id: mct-p1-material-wavelength-e
  content: |-
    $0.000533\ \mathrm{mm}$
  feedback: |-
    The numerical value $0.000533$ is the slit separation in meters. Converting meters to millimeters multiplies by $1000$, giving $0.533\ \mathrm{mm}$.
```

---

<a id="fringe-spacing"></a>
## Read Adjacent-Fringe Spacing

### M6-1 lecture worked case — intensity graph

An intensity graph shows adjacent bright peaks separated by

$$
\Delta y=1.0\ \mathrm{cm}.
$$

The screen distance is $L=0.85\ \mathrm m$, and the slit separation is $d=0.062\ \mathrm{mm}$. For small angles, adjacent bright orders differ by one, so

$$
\Delta y\approx\frac{\lambda L}{d}.
$$

Convert the measured lengths:

$$
\Delta y=1.0\times10^{-2}\ \mathrm m,
\qquad
d=6.2\times10^{-5}\ \mathrm m.
$$

Isolate and evaluate the wavelength:

$$
\lambda
\approx\frac{\Delta y\,d}{L}
=\frac{(1.0\times10^{-2})(6.2\times10^{-5})}{0.85}
=7.29\times10^{-7}\ \mathrm m
\approx730\ \mathrm{nm}.
$$

Within the small-angle model,

$$
\Delta y\propto\frac{\lambda L}{d}:
$$

larger wavelength or screen distance spreads the fringes apart, while larger slit separation pulls them closer together.

```quiz
type: radio
id: mct-p1-fringe-spacing
shuffle: true
content: |-
  Adjacent peaks in a double-slit intensity graph are $9.0\ \mathrm{mm}$ apart. The screen is $1.2\ \mathrm m$ from slits separated by $0.080\ \mathrm{mm}$. Assume small angles. What is the wavelength, and what happens to the peak spacing if only the screen distance is doubled?
options:
- id: mct-p1-fringe-spacing-a
  content: |-
    $600\ \mathrm{nm}$; the spacing becomes $18\ \mathrm{mm}$
  correct: true
  feedback: |-
    Adjacent spacing gives $\lambda\approx\Delta y d/L=(9.0\times10^{-3})(8.0\times10^{-5})/1.2=6.0\times10^{-7}\ \mathrm m=600\ \mathrm{nm}$. Since $\Delta y\propto L$, doubling only $L$ doubles the spacing to $18\ \mathrm{mm}$.
- id: mct-p1-fringe-spacing-b
  content: |-
    $600\ \mathrm{nm}$; the spacing becomes $4.5\ \mathrm{mm}$
  feedback: |-
    The wavelength is correct, but the screen-distance trend is reversed. Fringe spacing is directly proportional to $L$, so doubling $L$ doubles $9.0\ \mathrm{mm}$ to $18\ \mathrm{mm}$.
- id: mct-p1-fringe-spacing-c
  content: |-
    $600\ \mathrm{nm}$; the spacing remains $9.0\ \mathrm{mm}$
  feedback: |-
    The bright orders stay at the same angles, but their positions on the screen obey $y=L\tan\theta$. Doubling $L$ therefore doubles the adjacent screen spacing.
- id: mct-p1-fringe-spacing-d
  content: |-
    $60\ \mathrm{nm}$; the spacing becomes $18\ \mathrm{mm}$
  feedback: |-
    This converts $0.080\ \mathrm{mm}$ as $8.0\times10^{-6}\ \mathrm m$ instead of $8.0\times10^{-5}\ \mathrm m$. Correct unit cancellation gives $600\ \mathrm{nm}$.
- id: mct-p1-fringe-spacing-e
  content: |-
    $6000\ \mathrm{nm}$; the spacing becomes $18\ \mathrm{mm}$
  feedback: |-
    This converts $9.0\ \mathrm{mm}$ as $9.0\times10^{-2}\ \mathrm m$ instead of $9.0\times10^{-3}\ \mathrm m$. Using the correct meter conversion gives $600\ \mathrm{nm}$.
```

---

<a id="summary"></a>
## Summary

For a double-slit bright fringe:

1. Label the order: $m=0,\pm1,\pm2,\ldots$, with $|\Delta r|=|m|\lambda$.
2. Convert the wavelength and slit separation to compatible units.
3. Use $d\sin\theta_m=m\lambda$ to find an angle or slit separation.
4. Use $y_m=L\tan\theta_m$ to move between the angle and the screen.
5. Replace the exact two-stage route with $y_m\approx Lm\lambda/d$ only after the angle is known to be small.
6. If light enters a material, use the wavelength in that material; the frequency does not change.

For adjacent bright peaks at small angles, $\Delta y\approx\lambda L/d$. The main traps are using a half-integer dark-fringe condition, confusing $d$, $L$, and $y_m$, mixing length units, or treating the small-angle formula as exact.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
