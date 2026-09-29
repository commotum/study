# Recover a Single-Slit Width or Central-Maximum Width

<!--
lesson-id: 212-M7-019
topic-code: MTH212.M7.19
-->

## Table of Contents

- [Introduction](#introduction)
- [Use the First Minima as the Central Boundaries](#use-the-first-minima-as-the-central-boundaries)
- [Reject the Small-Angle Shortcut When the Angle Is Large](#reject-the-small-angle-shortcut-when-the-angle-is-large)
- [Recover the Slit Width From a Measured Central Band](#recover-the-slit-width-from-a-measured-central-band)
- [Solve for the Screen Distance](#solve-for-the-screen-distance)
- [Predict Width Changes and Keep Minima Separate From Maxima](#predict-width-changes-and-keep-minima-separate-from-maxima)
- [Summary](#summary)

## Prerequisites

- Convert nanometers, millimeters, and centimeters to meters.
- Use sine, tangent, and their inverse functions in degree mode.
- Distinguish a one-sided distance from a full symmetric width.
- Rearrange a one-equation formula for one unknown.

---

<a id="introduction"></a>
## Introduction

The recognition cue is a **single slit** followed by a broad central bright band and dark minima. For the ideal Fraunhofer (far-field) pattern used in these problems, a slit of width $a$ has dark minima at

$$
a\sin\theta_p=p\lambda,
\qquad p=1,2,3,\ldots
$$

The integer $p$ labels dark minima. There is no $p=0$ dark fringe: at $\theta=0$, the waves form the central maximum instead. This differs from the double-slit or grating equation, where an integer order labels bright maxima.

Write the one-slit width as $a$. The source video writes it as $d$, but that symbol usually denotes the spacing between two slits or neighboring grating lines.

Screen position and angle are related by

$$
\tan\theta_p=\frac{y_p}{L}.
$$

The first dark minima lie at $-y_1$ and $+y_1$. They bound the central maximum, so

$$
\boxed{w=2y_1},
\qquad
\boxed{\Theta_{\text{central}}=2\theta_1}.
$$

Before substituting, decide whether the prompt gives a half-width or a full width. A stated central width must be halved before it is used as $y_1$; a calculated $y_1$ must be doubled to report the full width.

When $a$ and $\lambda$ are known, calculate in this order:

$$
\theta_1=\sin^{-1}\!\left(\frac{\lambda}{a}\right),
\qquad
y_1=L\tan\theta_1,
\qquad
w=2y_1.
$$

When $\lambda/a\ll1$, $\sin\theta_1\approx\tan\theta_1\approx\theta_1$ and the workflow reduces to

$$
\boxed{w\approx\frac{2\lambda L}{a}}.
$$

The approximation is controlled by the angle, not by the fact that the setup uses one slit.

Source material: [single-slit video transcript](<../../../M6/2026-08-06-M6-2/Source/mct-Single Slit Diffraction - Physics Problems/Single Slit Diffraction - Physics Problems [9hCrhllI0ck].en.srt>) and [paired M6-2 lecture notes](<../../../M6/2026-08-06-M6-2/Source/Lecture-Notes.md>).

---

<a id="use-the-first-minima-as-the-central-boundaries"></a>
## Use the First Minima as the Central Boundaries

**Example:** The first dark minima occur $2.4\,\mathrm{cm}$ above and below the center of a single-slit pattern. Find the width of the central maximum.

**Explanation**

The given $2.4\,\mathrm{cm}$ is the one-sided distance $y_1$. The bright central band runs from $-y_1$ to $+y_1$, so

$$
w=2y_1=2(2.4\,\mathrm{cm})=4.8\,\mathrm{cm}.
$$

The first minima are labeled $p=1$ on either side. They are two symmetric locations for the same minimum order, not $p=1$ and $p=2$.

```quiz
type: radio
id: mct-q4-p3-boundaries
shuffle: true
content: |-
  In a single-slit pattern, the first dark minima are at $y=-1.8\,\mathrm{cm}$ and $y=+1.8\,\mathrm{cm}$. What is the full width of the central maximum?
options:
- id: mct-q4-p3-boundaries-a
  content: |-
    $3.6\,\mathrm{cm}$
  correct: true
  feedback: |-
    The central maximum spans the distance between the two first minima. Its width is $+1.8-(-1.8)=3.6\,\mathrm{cm}$, equivalently $w=2y_1$.
- id: mct-q4-p3-boundaries-b
  content: |-
    $1.8\,\mathrm{cm}$
  feedback: |-
    This is the half-width $y_1$, measured from the center to one first minimum. The requested band includes both halves, so it is twice this distance.
- id: mct-q4-p3-boundaries-c
  content: |-
    $7.2\,\mathrm{cm}$
  feedback: |-
    This doubles the separation after both sides have already been included. The distance from $-1.8\,\mathrm{cm}$ to $+1.8\,\mathrm{cm}$ is $3.6\,\mathrm{cm}$.
- id: mct-q4-p3-boundaries-d
  content: |-
    $0\,\mathrm{cm}$
  feedback: |-
    Adding the signed coordinates gives zero, but width is the distance between them. Subtract the lower coordinate from the upper coordinate, or use $2|y_1|$.
```

---

<a id="reject-the-small-angle-shortcut-when-the-angle-is-large"></a>
## Reject the Small-Angle Shortcut When the Angle Is Large

**Example (source video, frame verified at 03:27):** Light with wavelength $680\,\mathrm{nm}$ passes through a single slit of width $a=2.0\times10^{-6}\,\mathrm m$. A screen is $L=1.4\,\mathrm m$ away. Find the full angular width and full linear width of the central maximum.

**Explanation**

Convert the wavelength and use the first-minimum condition:

$$
\lambda=680\times10^{-9}\,\mathrm m,
$$

$$
\sin\theta_1
=\frac{\lambda}{a}
=\frac{680\times10^{-9}}{2.0\times10^{-6}}
=0.34.
$$

Therefore,

$$
\theta_1=\sin^{-1}(0.34)=19.8769^\circ.
$$

This is the half-angle. The full angular width is

$$
\Theta_{\text{central}}
=2\theta_1
=39.7537^\circ
\approx39.75^\circ.
$$

An angle near $20^\circ$ is too large for the small-angle shortcut. Use exact screen geometry:

$$
y_1=L\tan\theta_1
=(1.4\,\mathrm m)\tan(19.8769^\circ)
=0.5062\,\mathrm m.
$$

The full linear width is

$$
w=2y_1=1.0123\,\mathrm m\approx1.01\,\mathrm m.
$$

The shortcut would give $w\approx2\lambda L/a=0.952\,\mathrm m$, about $6\%$ low. The exact calculation is required here.

```quiz
type: radio
id: mct-q4-p3-exact-large-angle
shuffle: true
content: |-
  Light with $\lambda=600\,\mathrm{nm}$ passes through one slit of width $a=2.0\,\mu\mathrm m$. The screen is $1.2\,\mathrm m$ away. Which pair gives the full angular and linear widths of the central maximum using exact geometry?
options:
- id: mct-q4-p3-exact-large-angle-a
  content: |-
    $34.9^\circ$ and $0.755\,\mathrm m$
  correct: true
  feedback: |-
    The first minimum obeys $\sin\theta_1=\lambda/a=0.300$, so $\theta_1=17.46^\circ$. Doubling the angle and $y_1=1.2\tan(17.46^\circ)=0.377\,\mathrm m$ gives $34.9^\circ$ and $0.755\,\mathrm m$.
- id: mct-q4-p3-exact-large-angle-b
  content: |-
    $17.5^\circ$ and $0.377\,\mathrm m$
  feedback: |-
    These are the half-angle $\theta_1$ and half-width $y_1$. The central maximum extends from the first minimum on one side to the first minimum on the other, so both must be doubled.
- id: mct-q4-p3-exact-large-angle-c
  content: |-
    $34.9^\circ$ and $0.720\,\mathrm m$
  feedback: |-
    The angular width is doubled correctly, but $0.720\,\mathrm m$ comes from the small-angle formula. Since $\theta_1=17.46^\circ$ is not small, exact tangent geometry gives $0.755\,\mathrm m$.
- id: mct-q4-p3-exact-large-angle-d
  content: |-
    $17.5^\circ$ and $0.755\,\mathrm m$
  feedback: |-
    The linear width includes both halves, but $17.5^\circ$ is only the angle from the centerline to one first minimum. The full angular width is $2\theta_1=34.9^\circ$.
```

---

<a id="recover-the-slit-width-from-a-measured-central-band"></a>
## Recover the Slit Width From a Measured Central Band

**Example (source video):** Light with $\lambda=570\,\mathrm{nm}$ passes through a single slit. The screen is $L=7.5\,\mathrm m$ away, and the measured central-maximum width is $w=3.2\,\mathrm{cm}$. Find the slit width.

**Explanation**

The stated $3.2\,\mathrm{cm}$ is a full width. Halve it and convert to meters:

$$
y_1=\frac{w}{2}=1.6\,\mathrm{cm}=0.016\,\mathrm m.
$$

Use the screen triangle to find the half-angle:

$$
\theta_1
=\tan^{-1}\!\left(\frac{y_1}{L}\right)
=\tan^{-1}\!\left(\frac{0.016}{7.5}\right)
=0.12223^\circ.
$$

The caption calls $0.122$ “meters,” but an inverse tangent returns an angle; the correct unit is degrees.

Now solve the first-minimum condition for $a$:

$$
a=\frac{\lambda}{\sin\theta_1}
=\frac{570\times10^{-9}\,\mathrm m}{\sin(0.12223^\circ)}
=2.6719\times10^{-4}\,\mathrm m
=0.2672\,\mathrm{mm}.
$$

The video rounds the angle to $0.122^\circ$ before substitution and reports $2.68\times10^{-4}\,\mathrm m=0.268\,\mathrm{mm}$. Retaining guard digits gives $0.2672\,\mathrm{mm}$; the two results differ only because of intermediate rounding.

Since the angle is small, the shortcut is appropriate:

$$
a\approx\frac{2\lambda L}{w}
=\frac{2(570\times10^{-9})(7.5)}{0.032}
=2.671875\times10^{-4}\,\mathrm m
\approx0.267\,\mathrm{mm}.
$$

```quiz
type: radio
id: mct-q4-p3-recover-slit
shuffle: true
content: |-
  A $500\,\mathrm{nm}$ laser produces a central maximum $2.0\,\mathrm{cm}$ wide on a screen $4.0\,\mathrm m$ from one slit. The angle is small. What is the slit width?
options:
- id: mct-q4-p3-recover-slit-a
  content: |-
    $0.200\,\mathrm{mm}$
  correct: true
  feedback: |-
    The measured width is $w$, so $a\approx2\lambda L/w$. Substitution gives $2(500\times10^{-9})(4.0)/0.020=2.00\times10^{-4}\,\mathrm m=0.200\,\mathrm{mm}$.
- id: mct-q4-p3-recover-slit-b
  content: |-
    $0.100\,\mathrm{mm}$
  feedback: |-
    This treats the full $2.0\,\mathrm{cm}$ width as the one-sided distance $y_1$. Because $y_1=w/2$, the equivalent formula contains the factor $2\lambda L/w$.
- id: mct-q4-p3-recover-slit-c
  content: |-
    $0.400\,\mathrm{mm}$
  feedback: |-
    This inserts an extra factor of two after the width has already been handled. Starting from $w\approx2\lambda L/a$ and solving once for $a$ gives $0.200\,\mathrm{mm}$.
- id: mct-q4-p3-recover-slit-d
  content: |-
    $200\,\mathrm{mm}$
  feedback: |-
    The numerical coefficient $0.200$ belongs to millimeters. Since $2.00\times10^{-4}\,\mathrm m$ is multiplied by $10^3$ to convert meters to millimeters, it becomes $0.200\,\mathrm{mm}$, not $200\,\mathrm{mm}$.
```

---

<a id="solve-for-the-screen-distance"></a>
## Solve for the Screen Distance

**Example (source lecture):** A $633\,\mathrm{nm}$ laser illuminates a slit of width $a=0.15\,\mathrm{mm}$. The first dark minimum is $y_1=2.0\,\mathrm{cm}$ from the center. Find the slit-to-screen distance.

**Explanation**

Here $2.0\,\mathrm{cm}$ is already the center-to-minimum distance, not a full central width. Convert all lengths to meters:

$$
a=1.5\times10^{-4}\,\mathrm m,
\qquad
y_1=2.0\times10^{-2}\,\mathrm m.
$$

The exact first-minimum angle is

$$
\theta_1
=\sin^{-1}\!\left(\frac{633\times10^{-9}}{1.5\times10^{-4}}\right)
=0.2418^\circ.
$$

Then

$$
L=\frac{y_1}{\tan\theta_1}
=4.739\,\mathrm m
\approx4.7\,\mathrm m.
$$

The small-angle calculation gives the same rounded result:

$$
L\approx\frac{y_1a}{\lambda}
=\frac{(2.0\times10^{-2})(1.5\times10^{-4})}{633\times10^{-9}}
=4.739\,\mathrm m.
$$

```quiz
type: radio
id: mct-q4-p3-screen-distance
shuffle: true
content: |-
  A $520\,\mathrm{nm}$ laser illuminates one slit of width $0.20\,\mathrm{mm}$. The full central maximum is $3.0\,\mathrm{cm}$ wide. Approximately how far is the screen from the slit?
options:
- id: mct-q4-p3-screen-distance-a
  content: |-
    $5.77\,\mathrm m$
  correct: true
  feedback: |-
    First use $y_1=w/2=0.015\,\mathrm m$. With $a=2.0\times10^{-4}\,\mathrm m$, $L\approx y_1a/\lambda=(0.015)(2.0\times10^{-4})/(520\times10^{-9})=5.77\,\mathrm m$.
- id: mct-q4-p3-screen-distance-b
  content: |-
    $11.5\,\mathrm m$
  feedback: |-
    This uses the full $3.0\,\mathrm{cm}$ band as $y_1$. The screen triangle reaches from the center to one first minimum, so its opposite side is the half-width $1.5\,\mathrm{cm}$.
- id: mct-q4-p3-screen-distance-c
  content: |-
    $2.88\,\mathrm m$
  feedback: |-
    This halves the one-sided distance twice. Once $3.0\,\mathrm{cm}$ has been converted to $y_1=1.5\,\mathrm{cm}$, use that value directly in $L\approx y_1a/\lambda$.
- id: mct-q4-p3-screen-distance-d
  content: |-
    $5.77\times10^{-3}\,\mathrm m$
  feedback: |-
    This leaves a millimeter-to-meter factor in the result. Convert $0.20\,\mathrm{mm}$ to $2.0\times10^{-4}\,\mathrm m$ before substitution; the resulting screen distance is measured in meters.
```

---

<a id="predict-width-changes-and-keep-minima-separate-from-maxima"></a>
## Predict Width Changes and Keep Minima Separate From Maxima

**Example:** In the small-angle regime, the wavelength and screen distance stay fixed while the slit width is halved. How does the central-maximum width change?

**Explanation**

From

$$
w\approx\frac{2\lambda L}{a},
$$

$w$ varies inversely with $a$. Replacing $a$ with $a/2$ gives

$$
w_{\text{new}}
\approx\frac{2\lambda L}{a/2}
=2w_{\text{old}}.
$$

A narrower slit produces a broader central diffraction maximum. Increasing $\lambda$ or $L$ also broadens the pattern.

```quiz
type: radio
id: mct-q4-p3-width-scaling
shuffle: true
content: |-
  Two small-angle single-slit setups use the same wavelength and screen distance. The second slit is three times as wide as the first. How do their central-maximum widths compare?
options:
- id: mct-q4-p3-width-scaling-a
  content: |-
    The second central maximum is one-third as wide.
  correct: true
  feedback: |-
    At fixed $\lambda$ and $L$, $w\approx2\lambda L/a$ is inversely proportional to slit width. Replacing $a$ by $3a$ divides the central width by $3$.
- id: mct-q4-p3-width-scaling-b
  content: |-
    The second central maximum is three times as wide.
  feedback: |-
    This treats $w$ as directly proportional to $a$. Slit width is in the denominator: making the opening wider reduces the diffraction angle and narrows the central band.
- id: mct-q4-p3-width-scaling-c
  content: |-
    The two central maxima have the same width.
  feedback: |-
    Keeping wavelength and screen distance fixed does not remove the dependence on slit width. The factor $1/a$ makes a threefold increase in $a$ produce a threefold decrease in $w$.
- id: mct-q4-p3-width-scaling-d
  content: |-
    The second central maximum is nine times as wide.
  feedback: |-
    No square of the slit width appears in the small-angle relation. The dependence is $w\propto1/a$, so the change is a factor of $1/3$, not $3^2$.
```

The equation $a\sin\theta_p=p\lambda$ locates dark minima. Secondary bright maxima lie between those minima, but they are not exactly at the midpoints. A midpoint estimate is only an introductory approximation; in a more exact treatment, noncentral maxima satisfy $\tan\beta=\beta$. Do not use the dark-minimum equation as though it gave an exact secondary-maximum location.

---

<a id="summary"></a>
## Summary

For a single slit, use this sequence:

1. Label dark minima with $p=1,2,3,\ldots$ in $a\sin\theta_p=p\lambda$. There is no $p=0$ dark fringe.
2. Translate the width statement before calculating: $y_1=w/2$ and $\theta_1=\Theta_{\text{central}}/2$.
3. Use exact geometry through $\theta_1=\sin^{-1}(\lambda/a)$ and $y_1=L\tan\theta_1$ unless the angle is demonstrably small.
4. In the small-angle regime, use $w\approx2\lambda L/a$ and keep the factor of two attached to the full central width.
5. Keep units consistent and retain guard digits until the final reported result.

The main traps are using the full width as $y_1$, reporting a half-width as the answer, labeling a single-slit minimum as a bright order, or using the small-angle shortcut at a large angle.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
