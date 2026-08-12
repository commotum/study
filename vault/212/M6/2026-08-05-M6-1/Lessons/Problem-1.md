# Screen Distance and Double-Slit Fringe Spacing

<!--
lesson-id: 212-M6-001
topic-code: MTH212.M6.01
-->
## Table of Contents

- [Introduction](#introduction)
- [Read the Fringe-Spacing Law](#read-the-fringe-spacing-law)
- [Compare Two Screen Distances](#compare-two-screen-distances)
- [Keep Angle and Position Separate](#keep-angle-and-position-separate)
- [Apply the Screen-Distance Cue](#apply-the-screen-distance-cue)
- [Variant: Change Wavelength Instead](#variant-change-wavelength-instead)
- [Summary](#summary)

## Prerequisites

- Identify $\lambda$ as wavelength, $d$ as slit separation, and $L$ as the slit-to-screen distance.
- Read direct proportionality from a formula.
- Compare two values by forming a ratio.

---

<a id="introduction"></a>
## Introduction

When a double-slit setup keeps the wavelength $\lambda$ and slit separation $d$ fixed, the cue “move the screen” means that only the screen distance $L$ changes. In the usual far-field, small-angle model, adjacent bright fringes are separated by

$$
\Delta y\approx \frac{\lambda L}{d}.
$$

Treat the fixed ratio $C=\lambda/d$ as one constant. Then

$$
\Delta y\approx CL
\qquad\text{and}\qquad
\frac{\Delta y}{L}\approx C.
$$

The output $\Delta y$ is therefore directly proportional to the input $L$. Determine how the linear fringe spacing changes by applying the same scale factor to both quantities: a closer screen has a smaller $L$, so the bright fringes land closer together.

---

<a id="read-the-fringe-spacing-law"></a>
## Read the Fringe-Spacing Law

**Example:** Light with wavelength $600\ \text{nm}$ passes through slits separated by $0.30\ \text{mm}$. Find the fringe spacing on a screen $2.0\ \text{m}$ away.

**Explanation**

Use SI units in $\Delta y\approx \lambda L/d$:

$$
\Delta y
\approx
\frac{(600\times 10^{-9}\ \text{m})(2.0\ \text{m})}
{0.30\times 10^{-3}\ \text{m}}
=4.0\times 10^{-3}\ \text{m}
=4.0\ \text{mm}.
$$

The ratio $\lambda/d$ is a dimensionless constant for this setup, so the equation has the direct-variation form $\Delta y=CL$. Increasing $L$ increases the spacing, while decreasing $L$ decreases the spacing.

```quiz
type: radio
id: m6-1-p1-fringe-law
content: |-
  In $\Delta y\approx \lambda L/d$, wavelength and slit separation stay fixed. Which relationship correctly isolates the effect of screen distance?
options:
- id: direct
  content: |-
    $\Delta y\propto L$
  correct: true
  feedback: |-
    With $\lambda$ and $d$ fixed, their ratio is constant and $L$ is the remaining factor in the numerator. Therefore the linear fringe spacing changes by the same factor as $L$: $\Delta y\propto L$.
- id: inverse
  content: |-
    $\Delta y\propto 1/L$
  feedback: |-
    An inverse dependence would require $L$ in the denominator. Here $L$ multiplies $\lambda/d$, so a smaller $L$ produces a smaller—not larger—$\Delta y$.
- id: quadratic
  content: |-
    $\Delta y\propto L^2$
  feedback: |-
    The spacing law contains one factor of $L$, not $L^2$. Squaring the change in screen distance would exaggerate the change in $\Delta y$.
- id: independent
  content: |-
    $\Delta y$ is independent of $L$
  feedback: |-
    The bright-fringe angles are independent of $L$ when $\lambda$ and $d$ are fixed, but linear spacing on the screen includes the factor $L$. Thus changing $L$ changes $\Delta y$.
```

---

<a id="compare-two-screen-distances"></a>
## Compare Two Screen Distances

**Example:** A pattern has fringe spacing $5.0\ \text{mm}$ at $L_1=2.5\ \text{m}$. The screen moves to $L_2=1.0\ \text{m}$ without changing the light or slits. Find the new spacing.

**Explanation**

Because $\lambda/d$ is unchanged, take a ratio instead of recalculating from the full formula:

$$
\frac{\Delta y_2}{\Delta y_1}=\frac{L_2}{L_1}.
$$

First identify the scale factor:

$$
f=\frac{L_2}{L_1}=\frac{1.0}{2.5}=0.40.
$$

Since $f<1$, the new spacing must be smaller. Now apply the factor:

$$
\Delta y_2=(5.0\ \text{mm})\frac{1.0}{2.5}=2.0\ \text{mm}.
$$

The screen distance became $0.40$ of its original value, so the spacing also became $0.40$ of its original value.

```quiz
type: radio
id: m6-1-p1-distance-ratio
content: |-
  A double-slit pattern has fringe spacing $3.6\ \text{mm}$ on a screen $2.4\ \text{m}$ from the slits. If the screen is moved to $1.2\ \text{m}$ and everything else remains fixed, what is the new spacing?
options:
- id: half
  content: |-
    $1.8\ \text{mm}$
  correct: true
  feedback: |-
    Fringe spacing scales directly with screen distance. Since $L$ is multiplied by $1.2/2.4=1/2$, the spacing is also halved: $\Delta y_2=(3.6\ \text{mm})(1/2)=1.8\ \text{mm}$.
- id: double
  content: |-
    $7.2\ \text{mm}$
  feedback: |-
    This applies the distance factor backward, as though spacing were inversely proportional to $L$. Because $\Delta y\propto L$, halving $L$ halves the spacing rather than doubling it.
- id: unchanged
  content: |-
    $3.6\ \text{mm}$
  feedback: |-
    The wavelength and slit separation stay fixed, but the linear fringe spacing does not: $L$ appears in $\Delta y\approx \lambda L/d$. Halving $L$ changes the spacing from $3.6\ \text{mm}$ to $1.8\ \text{mm}$.
- id: squared
  content: |-
    $0.90\ \text{mm}$
  feedback: |-
    This squares the factor $1/2$. The spacing law is linear in $L$, so the spacing receives one factor of $1/2$, not $(1/2)^2$.
```

---

<a id="keep-angle-and-position-separate"></a>
## Keep Angle and Position Separate

**Example:** Consider the first bright fringe before and after moving the screen closer while leaving $\lambda$ and $d$ unchanged.

**Explanation**

The bright-fringe condition is

$$
d\sin\theta_m=m\lambda.
$$

It fixes each bright fringe's angle $\theta_m$, so moving the screen does not change those angles. The screen coordinate is instead

$$
y_m=L\tan\theta_m.
$$

At the same angle, a smaller $L$ gives a smaller $|y_m|$. The central fringe is the boundary case: $m=0$ gives $\theta_0=0$ and $y_0=0$, so it stays at the center. Every noncentral fringe moves inward, and the linear image is compressed on the closer screen.

```quiz
type: radio
id: m6-1-p1-angle-position
content: |-
  The wavelength and slit separation are fixed while the screen moves closer to a double slit. Which description is correct?
options:
- id: same-angle-closer-position
  content: |-
    The bright-fringe angles stay the same, and the bright-fringe positions move closer to the center of the screen.
  correct: true
  feedback: |-
    The interference condition $d\sin\theta_m=m\lambda$ fixes the angles, while $y_m=L\tan\theta_m$ maps those angles to screen positions. Decreasing $L$ leaves $\theta_m$ unchanged but decreases every $|y_m|$, so the fringes move closer together.
- id: same-angle-same-position
  content: |-
    The bright-fringe angles and positions both stay the same.
  feedback: |-
    Fixed $\lambda$ and $d$ do keep each angle $\theta_m$ the same, but position also depends on screen distance through $y_m=L\tan\theta_m$. A smaller $L$ therefore moves each noncentral fringe toward the center.
- id: smaller-angle-same-position
  content: |-
    The bright-fringe angles become smaller, but their screen positions stay the same.
  feedback: |-
    Screen distance does not appear in $d\sin\theta_m=m\lambda$, so it cannot change the allowed angles. Instead, the unchanged angles map to smaller screen positions because $L$ decreases.
- id: larger-angle-farther-position
  content: |-
    The bright-fringe angles become larger, and the fringes move farther from the center.
  feedback: |-
    Larger angles would require changing $\lambda$ or $d$, not merely moving the screen. With the angles fixed, reducing $L$ reduces $|y_m|$, so the fringes move inward rather than outward.
```

---

<a id="apply-the-screen-distance-cue"></a>
## Apply the Screen-Distance Cue

**Example:** If a screen is shifted from $L$ to $0.70L$ while the light and slits remain unchanged, then

$$
\Delta y_{\text{new}}=0.70\Delta y_{\text{old}}.
$$

**Explanation**

Before doing any arithmetic, ask what changed. Here only $L$ changed, and $\Delta y\propto L$. A factor smaller than $1$ means the pattern is compressed; a factor larger than $1$ means it is spread out.

```quiz
type: radio
id: m6-1-p1-source-application
shuffle: true
content: |-
  **Question 1**

  Laser light illuminates a double slit, producing a pattern of fringes on a screen. What happens if the screen is moved closer to the slits, keeping all else the same?
options:
- id: a
  content: |-
    The fringes are spaced farther apart
  feedback: |-
    This reverses the direct dependence on screen distance. Since $\Delta y\approx \lambda L/d$, moving the screen closer decreases $L$ and therefore decreases—not increases—the spacing.
- id: b
  content: |-
    The fringes are spaced closer together
  correct: true
  feedback: |-
    Double-slit fringe spacing obeys $\Delta y\approx \lambda L/d$. With wavelength and slit separation unchanged, decreasing the screen distance $L$ decreases $\Delta y$, so the fringes are spaced closer together.
- id: c
  content: |-
    The spacing between the fringes does not change
  feedback: |-
    The bright-fringe angles remain fixed, but their linear screen positions satisfy $y_m=L\tan\theta_m$. A smaller $L$ brings each noncentral fringe closer to the center, so the linear spacing decreases.
```

---

<a id="variant-change-wavelength-instead"></a>
## Variant: Change Wavelength Instead

The same fringe-spacing law also compares wavelengths. With $L$ and $d$ fixed, closer fringes require a smaller $\lambda$.

```quiz
type: radio
id: khadley-wave-optics-q1
shuffle: true
content: |-
  Light of wavelength $\lambda_1$ produces double-slit fringes. Under otherwise identical conditions, wavelength $\lambda_2$ produces closer fringes. Which statement is true?
options:
- id: shorter
  content: $\lambda_2<\lambda_1$
  correct: true
  feedback: |-
    Double-slit spacing is $\Delta y=\lambda L/d$. With $L$ and $d$ unchanged, closer fringes require the shorter wavelength $\lambda_2$.
- id: longer
  content: $\lambda_2>\lambda_1$
  feedback: |-
    A longer wavelength increases $\Delta y=\lambda L/d$, so it would spread the fringes farther apart rather than bring them closer.
- id: indeterminate
  content: It cannot be determined.
  feedback: |-
    The slit spacing and screen distance are fixed, leaving wavelength as the only changing factor in the fringe-spacing equation.
```

---

<a id="summary"></a>
## Summary

1. **Recognize the cue:** The wavelength and slit separation stay fixed, and only the screen distance changes.
2. **Write the rule:** $\Delta y\approx (\lambda/d)L$, so $\Delta y\propto L$.
3. **Apply one scale factor:** $f=L_2/L_1$ gives $\Delta y_2=f\Delta y_1$.
4. **Check the direction:** If the screen moves closer, then $f<1$ and the fringes must be closer together.

**Main trap:** Fixed bright-fringe angles do not mean fixed screen positions. The central fringe remains at $y_0=0$, while every noncentral position $y_m=L\tan\theta_m$ moves toward the center as $L$ decreases.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
