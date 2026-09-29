# Convert Diffraction-Grating Line Density into an Exact Maximum

<!--
lesson-id: 212-M7-018
topic-code: MTH212.M7.18
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Line Density to Spacing](#density-to-spacing)
- [Solve for an Unknown Wavelength](#unknown-wavelength)
- [Recover Line Density from a Maximum](#recover-density)
- [Use Exact Screen Geometry](#exact-screen-geometry)
- [Find the Maximum Possible Order](#maximum-order)
- [Summary](#summary)

## Prerequisites

- Convert centimeters, millimeters, micrometers, and nanometers to meters.
- Use reciprocal units.
- Evaluate inverse sine and inverse tangent in degree mode.
- Recognize that an interference order $m$ is an integer.

---

<a id="introduction"></a>
## Introduction

Look for a diffraction grating, a line density such as lines per centimeter or millimeter, and a principal bright maximum. Use one chain:

$$
\boxed{
\text{line density }N
\longrightarrow
d=\frac{1}{N}
\longrightarrow
d\sin\theta_m=m\lambda
}.
$$

Here $d$ is the center-to-center spacing between neighboring grating lines. Convert $N$ to lines per meter before taking its reciprocal, so $d$ comes out in meters. Convert the wavelength to meters as well.

Rearrange the grating equation to match the requested quantity:

$$
\theta_m=\sin^{-1}\left(\frac{m\lambda}{d}\right),
\qquad
\lambda=\frac{d\sin\theta_m}{m},
\qquad
d=\frac{m\lambda}{\sin\theta_m},
\qquad
N=\frac{1}{d}.
$$

Before taking inverse sine, enforce its domain:

$$
\boxed{\left|\frac{m\lambda}{d}\right|\leq1}.
$$

Use this ledger to catch a setup error before calculating:

| Stage | Required check |
|---|---|
| convert density | the stated denominator cancels, leaving lines/m |
| invert density | reciprocal units become m/line, the spacing $d$ |
| form $m\lambda/d$ | the ratio is dimensionless |
| apply inverse sine | the ratio lies in $[-1,1]$ |

Use exact sine for grating-sized angles. The approximation $\sin\theta\approx\tan\theta\approx\theta$ is only justified when the angle is small.

**Source correction.** The narration in `gf7j2fumz70` repeatedly says “diffraction gradient.” The device is a **diffraction grating**. It also describes $d$ loosely as a slit width; in the grating equation, $d$ is the spacing between adjacent lines.

---

<a id="density-to-spacing"></a>
## Convert Line Density to Spacing

Line density and spacing are reciprocals. Their units reverse as well:

$$
N\left(\frac{\text{lines}}{\mathrm m}\right)
\quad\Longleftrightarrow\quad
d=\frac1N\left(\frac{\mathrm m}{\text{line}}\right).
$$

Direction check: more lines per unit length means a smaller spacing.

For common density units,

| Stated density | Density in lines per meter |
|---|---:|
| $A\ \text{lines/cm}$ | $100A\ \text{lines/m}$ |
| $A\ \text{lines/mm}$ | $1000A\ \text{lines/m}$ |

### Source-video worked case — `gf7j2fumz70`, 00:00:01–00:04:23

A grating has $5000\ \text{lines/cm}$. Convert the density with the units visible:

$$
N
=5000\frac{\text{lines}}{\mathrm{cm}}
\left(100\frac{\mathrm{cm}}{\mathrm m}\right)
=5.00\times10^5\frac{\text{lines}}{\mathrm m}.
$$

Invert it:

$$
d=\frac1N
=\frac{1}{5.00\times10^5\ \text{lines/m}}
=2.00\times10^{-6}\ \mathrm m.
$$

For a second-order maximum, $m=2$, with $\lambda=650\ \mathrm{nm}=650\times10^{-9}\ \mathrm m$:

$$
\sin\theta_2
=\frac{m\lambda}{d}
=\frac{2(650\times10^{-9})}{2.00\times10^{-6}}
=0.650.
$$

Therefore,

$$
\boxed{\theta_2=\sin^{-1}(0.650)=40.5^\circ}.
$$

```quiz
type: radio
id: mct-p2-density-to-angle
shuffle: true
content: |-
  A diffraction grating has $4000\ \text{lines/cm}$. Light of wavelength $600\ \mathrm{nm}$ illuminates it. What is the exact second-order maximum angle?
options:
- id: mct-p2-density-to-angle-a
  content: |-
    $28.7^\circ$
  correct: true
  feedback: |-
    Convert the density first: $N=4000(100)=4.00\times10^5\ \text{lines/m}$, so $d=2.50\times10^{-6}\ \mathrm m$. Then $\sin\theta_2=2(600\times10^{-9})/d=0.480$, giving $\theta_2=28.7^\circ$.
- id: mct-p2-density-to-angle-b
  content: |-
    $13.9^\circ$
  feedback: |-
    This uses $m=1$. The requested maximum is second order, so the inverse-sine argument is $2\lambda/d=0.480$, not $\lambda/d=0.240$.
- id: mct-p2-density-to-angle-c
  content: |-
    $0.275^\circ$
  feedback: |-
    This inverts $4000$ as though the density were already in lines per meter. Convert lines per centimeter to lines per meter by multiplying by $100$ before taking the reciprocal.
- id: mct-p2-density-to-angle-d
  content: |-
    $27.5^\circ$
  feedback: |-
    This treats $0.480$ as the angle in radians, using the small-angle approximation. The exact angle is $\sin^{-1}(0.480)=28.7^\circ$; the difference is large enough to matter.
- id: mct-p2-density-to-angle-e
  content: |-
    $0.480^\circ$
  feedback: |-
    The value $0.480$ is $\sin\theta_2$, not the angle in degrees. Apply inverse sine in degree mode to recover the angle.
```

---

<a id="unknown-wavelength"></a>
## Solve for an Unknown Wavelength

When line density and a maximum angle are given, convert and invert the density before solving

$$
\lambda=\frac{d\sin\theta_m}{m}.
$$

Keep guard digits until the final conversion and rounding.

### Source-video worked case — `gf7j2fumz70`, 00:04:28–00:07:01

The grating has $10000\ \text{lines/cm}$, so

$$
N=1.00\times10^6\ \text{lines/m},
\qquad
d=1.00\times10^{-6}\ \mathrm m.
$$

A third-order maximum occurs at $25^\circ$, so

$$
\begin{aligned}
\lambda
&=\frac{d\sin25^\circ}{3}\\
&=\frac{(1.00\times10^{-6})\sin25^\circ}{3}\\
&=1.4087\ldots\times10^{-7}\ \mathrm m\\
&=140.87\ldots\ \mathrm{nm}\\
&\approx141\ \mathrm{nm}.
\end{aligned}
$$

```quiz
type: radio
id: mct-p2-unknown-wavelength
shuffle: true
content: |-
  A grating has $8000\ \text{lines/cm}$. Its second-order maximum is at $30.0^\circ$. What wavelength produced the maximum?
options:
- id: mct-p2-unknown-wavelength-a
  content: |-
    $312.5\ \mathrm{nm}$
  correct: true
  feedback: |-
    The density is $8.00\times10^5\ \text{lines/m}$, so $d=1.25\times10^{-6}\ \mathrm m$. Then $\lambda=d\sin30.0^\circ/2=3.125\times10^{-7}\ \mathrm m=312.5\ \mathrm{nm}$.
- id: mct-p2-unknown-wavelength-b
  content: |-
    $625\ \mathrm{nm}$
  feedback: |-
    This computes $d\sin30.0^\circ$ but does not divide by the order. Since $d\sin\theta_m=m\lambda$ and $m=2$, divide by $2$.
- id: mct-p2-unknown-wavelength-c
  content: |-
    $1250\ \mathrm{nm}$
  feedback: |-
    This multiplies by the order instead of dividing by it. Solve the maximum condition for wavelength: $\lambda=d\sin\theta_m/m$.
- id: mct-p2-unknown-wavelength-d
  content: |-
    $31.25\ \mathrm{nm}$
  feedback: |-
    This uses a line density ten times too large. Converting from lines per centimeter to lines per meter contributes a factor of $100$, not $1000$.
- id: mct-p2-unknown-wavelength-e
  content: |-
    $3.125\times10^{-7}\ \mathrm{nm}$
  feedback: |-
    The numerical value $3.125\times10^{-7}$ is in meters. Since $1\ \mathrm{nm}=10^{-9}\ \mathrm m$, that length is $312.5\ \mathrm{nm}$, not $3.125\times10^{-7}\ \mathrm{nm}$.
```

---

<a id="recover-density"></a>
## Recover Line Density from a Maximum

To work in the reverse direction, solve for spacing and then invert:

$$
d=\frac{m\lambda}{\sin\theta_m},
\qquad
N=\frac1d.
$$

Convert the final density to the requested “per length” unit. A density in lines per meter is divided by $100$ to obtain lines per centimeter and by $1000$ to obtain lines per millimeter.

### Source-video worked case — `gf7j2fumz70`, 00:07:05–00:10:03

A second-order maximum is at $18^\circ$ for $\lambda=540\ \mathrm{nm}$. Thus,

$$
d
=\frac{2(540\times10^{-9}\ \mathrm m)}{\sin18^\circ}
=3.495\times10^{-6}\ \mathrm m.
$$

Then

$$
N=\frac1d
=2.86\times10^5\ \text{lines/m}
=2861\ \text{lines/cm}.
$$

### M6-2 lecture worked case

A $633\ \mathrm{nm}$ laser produces first-order peaks separated by $1.70\ \mathrm m$ on a screen $2.4\ \mathrm m$ away. Symmetry gives $y_1=0.85\ \mathrm m$, so

$$
\theta_1=\tan^{-1}\left(\frac{0.85}{2.4}\right)=19.5^\circ.
$$

The line density is

$$
N
=\frac{\sin\theta_1}{\lambda}
=5.274\ldots\times10^5\ \text{lines/m}
=527.4\ldots\ \text{lines/mm}
\approx5.3\times10^2\ \text{lines/mm}.
$$

```quiz
type: radio
id: mct-p2-recover-density
shuffle: true
content: |-
  Light with wavelength $600\ \mathrm{nm}$ makes a first-order grating maximum at $30.0^\circ$. What is the grating line density in lines per centimeter?
options:
- id: mct-p2-recover-density-a
  content: |-
    $8.33\times10^3\ \text{lines/cm}$
  correct: true
  feedback: |-
    First find $d=\lambda/\sin30.0^\circ=1.20\times10^{-6}\ \mathrm m$. Its reciprocal is $8.33\times10^5\ \text{lines/m}$, which is $8.33\times10^3\ \text{lines/cm}$.
- id: mct-p2-recover-density-b
  content: |-
    $8.33\times10^5\ \text{lines/cm}$
  feedback: |-
    This correctly finds the numerical density per meter but relabels it as per centimeter. Divide a lines-per-meter density by $100$ to express it in lines per centimeter.
- id: mct-p2-recover-density-c
  content: |-
    $83.3\ \text{lines/cm}$
  feedback: |-
    This divides by the meter-to-centimeter factor twice. After finding $8.33\times10^5\ \text{lines/m}$, divide by $100$ once.
- id: mct-p2-recover-density-d
  content: |-
    $1.20\times10^{-6}\ \text{lines/cm}$
  feedback: |-
    The value $1.20\times10^{-6}\ \mathrm m$ is the line spacing $d$, not the line density. Invert the spacing and then convert the reciprocal units.
- id: mct-p2-recover-density-e
  content: |-
    $3.33\times10^4\ \text{lines/cm}$
  feedback: |-
    This uses $d=\lambda\sin\theta$ instead of $d=\lambda/\sin\theta$. The maximum condition places $d$ with the sine on the left, so solving for $d$ requires division by $\sin\theta$.
```

---

<a id="exact-screen-geometry"></a>
## Use Exact Screen Geometry

If a screen position is given, find the angle from the right triangle first:

$$
\theta_m=\tan^{-1}\left(\frac{y_m}{L}\right).
$$

Then use that angle in $d\sin\theta_m=m\lambda$. At large angles, do not replace both trigonometric functions with the same small-angle value. The exact screen position is

$$
y_m
=L\tan\left[\sin^{-1}\left(\frac{m\lambda}{d}\right)\right],
$$

which is not generally linear in $m$; grating peaks need not be evenly spaced on the screen.

### M6-1 lecture worked case

The grating spacing is $d=3.0\ \mu\mathrm m$, the screen distance is $L=1.8\ \mathrm m$, and the third-order peak is at $y_3=1.20\ \mathrm m$. Exact geometry gives

$$
\theta_3
=\tan^{-1}\left(\frac{1.20}{1.8}\right)
=33.7^\circ.
$$

Therefore,

$$
\lambda
=\frac{(3.0\times10^{-6})\sin33.7^\circ}{3}
=5.55\times10^{-7}\ \mathrm m
\approx550\ \mathrm{nm}.
$$

The small-angle formula would give about $670\ \mathrm{nm}$, so it is not acceptable at $33.7^\circ$.

```quiz
type: radio
id: mct-p2-exact-screen-geometry
shuffle: true
content: |-
  A grating with spacing $d=2.5\ \mu\mathrm m$ produces its second-order maximum $1.0\ \mathrm m$ from center on a screen $2.0\ \mathrm m$ away. What wavelength is predicted by exact geometry?
options:
- id: mct-p2-exact-screen-geometry-a
  content: |-
    $559\ \mathrm{nm}$
  correct: true
  feedback: |-
    Exact geometry gives $\theta_2=\tan^{-1}(1.0/2.0)=26.565\ldots^\circ$. Then $\lambda=d\sin\theta_2/2=5.590\ldots\times10^{-7}\ \mathrm m=559\ \mathrm{nm}$.
- id: mct-p2-exact-screen-geometry-b
  content: |-
    $625\ \mathrm{nm}$
  feedback: |-
    This uses the small-angle formula $\lambda\approx yd/(mL)$. The actual angle is $26.6^\circ$, so use $\theta=\tan^{-1}(y/L)$ followed by the exact sine.
- id: mct-p2-exact-screen-geometry-c
  content: |-
    $1118\ \mathrm{nm}$
  feedback: |-
    This computes $d\sin\theta_2$ but omits division by the order. For the second-order peak, $d\sin\theta_2=2\lambda$.
- id: mct-p2-exact-screen-geometry-d
  content: |-
    $280\ \mathrm{nm}$
  feedback: |-
    This divides by the order twice. The factor $m=2$ appears once in $\lambda=d\sin\theta_m/m$.
- id: mct-p2-exact-screen-geometry-e
  content: |-
    $599\ \mathrm{nm}$
  feedback: |-
    This treats the ratio $y/L=0.5$ as the angle in radians. That ratio is $\tan\theta$, so first calculate $\theta=\tan^{-1}(0.5)$ before taking its sine.
```

---

<a id="maximum-order"></a>
## Find the Maximum Possible Order

A real maximum angle requires

$$
\left|\frac{m\lambda}{d}\right|\leq1.
$$

Because $m$ is an integer,

$$
\boxed{m_{\max}=\left\lfloor\frac{d}{\lambda}\right\rfloor}.
$$

Do not round $d/\lambda$ to the nearest integer or round up. If both sides of the pattern are intercepted, the allowed orders are

$$
-m_{\max},\ldots,-1,0,1,\ldots,m_{\max},
$$

so the total number of principal maxima is $2m_{\max}+1$.

### M6-2 lecture worked case

For $d=1.8\times10^{-6}\ \mathrm m$ and $\lambda=633\ \mathrm{nm}$,

$$
\frac{d}{\lambda}
=\frac{1.8\times10^{-6}}{633\times10^{-9}}
=2.84\ldots.
$$

Thus $m_{\max}=2$. The allowed orders are

$$
m=-2,-1,0,1,2,
$$

for five total maxima. A proposed third-order maximum would require

$$
\frac{3\lambda}{d}=1.055\ldots>1,
$$

so no real angle exists for it.

```quiz
type: radio
id: mct-p2-maximum-order
shuffle: true
content: |-
  A grating has spacing $d=2.2\ \mu\mathrm m$ and is illuminated by $500\ \mathrm{nm}$ light. Assuming all physically allowed directions reach the screen, what is the highest order and how many principal maxima are possible?
options:
- id: mct-p2-maximum-order-a
  content: |-
    $m_{\max}=4$ and $9$ total maxima
  correct: true
  feedback: |-
    The order limit is $d/\lambda=2.2\times10^{-6}/(500\times10^{-9})=4.4$. Since $m$ is an integer and cannot exceed $4.4$, $m_{\max}=4$; orders $-4$ through $+4$ give $2(4)+1=9$ maxima.
- id: mct-p2-maximum-order-b
  content: |-
    $m_{\max}=5$ and $11$ total maxima
  feedback: |-
    This rounds $4.4$ to an unavailable order. For $m=5$, the inverse-sine argument would exceed $1$, so take the greatest integer no larger than $4.4$: $m_{\max}=4$.
- id: mct-p2-maximum-order-c
  content: |-
    $m_{\max}=4$ and $8$ total maxima
  feedback: |-
    Eight counts the four positive and four negative orders but omits the central maximum. Order $m=0$ is also a principal maximum, making the total $9$.
- id: mct-p2-maximum-order-d
  content: |-
    $m_{\max}=4$ and $5$ total maxima
  feedback: |-
    Five counts only the nonnegative orders $0,1,2,3,4$. The grating also has symmetric negative orders, so the full count is $2m_{\max}+1=9$.
- id: mct-p2-maximum-order-e
  content: |-
    $m_{\max}=4$ and $4$ total maxima
  feedback: |-
    The maximum order is not the number of peaks. Include both signs and the central order: $-4,-3,-2,-1,0,1,2,3,4$.
```

---

<a id="summary"></a>
## Summary

For a diffraction-grating principal maximum:

1. Convert the line density to lines per meter.
2. Invert it to obtain the adjacent-line spacing $d=1/N$ in meters.
3. Convert wavelength to meters and identify the integer order $m$.
4. Use the exact condition
   $$
   d\sin\theta_m=m\lambda.
   $$
5. If screen coordinates are given, use $\theta_m=\tan^{-1}(y_m/L)$ before the grating equation.
6. Check $|m\lambda/d|\leq1$; an inverse-sine argument outside $[-1,1]$ means that order cannot exist.

More lines per unit length means smaller $d$. For fixed $m$ and $\lambda$, that moves the maximum to a larger angle until the physical order limit is reached. The main traps are inverting before converting the density, mixing length units, using a small-angle shortcut at a large angle, and counting an impossible order.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
