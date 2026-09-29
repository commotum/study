# How Screen Distance Changes Double-Slit Fringe Spacing

<!--
lesson-id: 212-M6-002
topic-code: MTH212.M6.02
-->
## Table of Contents

- [Introduction](#introduction)
- [Read the Screen-Distance Dependence](#read-the-screen-distance-dependence)
- [Scale the Spacing Without Recalculating](#scale-the-spacing-without-recalculating)
- [Separate Fringe Angle from Screen Position](#separate-fringe-angle-from-screen-position)
- [Apply the Cue to the Laboratory Pattern](#apply-the-cue-to-the-laboratory-pattern)
- [Summary](#summary)

## Prerequisites

- Recognize direct proportionality: if $q\propto L$, multiplying $L$ by a factor multiplies $q$ by the same factor.
- Identify the wavelength $\lambda$, slit separation $d$, and slit-to-screen distance $L$ in a double-slit setup.

---

<a id="introduction"></a>
## Introduction

When a question changes only the distance from a double slit to the screen, look at the **linear spacing on the screen**, not just the angles of the bright fringes. For small angles, adjacent bright fringes are separated by

$$
\Delta y\approx \frac{\lambda L}{d},
$$

where $\lambda$ is the wavelength, $L$ is the slit-to-screen distance, and $d$ is the slit separation. If the same light and slits are used, then $\lambda$ and $d$ stay fixed, so

$$
\Delta y\propto L.
$$

Equivalently, the spacing per unit screen distance is constant for a fixed light source and slit pair:

$$
\frac{\Delta y}{L}\approx \frac{\lambda}{d}=\text{constant}.
$$

> **Recognition cue:** If the problem changes the screen distance but keeps the light and slits the same, compare $L$ directly. A larger $L$ gives a larger $\Delta y$.

The practical rule is simple: moving the screen farther away spreads the fringes farther apart; moving it closer packs them closer together.

---

<a id="read-the-screen-distance-dependence"></a>
## Read the Screen-Distance Dependence

**Example:** A double-slit pattern has fringe spacing $\Delta y_1$ when the screen is $1.2\ \mathrm{m}$ from the slits. The screen is moved to $1.8\ \mathrm{m}$ while the light and slits remain unchanged. How does the spacing change?

**Explanation**

With $\lambda$ and $d$ fixed, write the spacing ratio in the same new-to-old order as the distance ratio:

$$
\frac{\Delta y_2}{\Delta y_1}=\frac{L_2}{L_1}
=\frac{1.8}{1.2}=1.5.
$$

The new fringe spacing is $1.5$ times the original spacing. Because the screen distance increased, the fringes are farther apart.

```quiz
type: radio
id: p2-screen-distance-direction
content: |-
  A double-slit setup uses the same wavelength and the same slits before and after a change. The screen distance increases from $2.0\ \mathrm{m}$ to $3.0\ \mathrm{m}$. What happens to the fringe spacing on the screen?
options:
- id: p2-screen-distance-direction-a
  content: |-
    It becomes $\tfrac{2}{3}$ as large.
  feedback: |-
    The factor $2/3$ reverses the ratio. Since $\Delta y\propto L$ for fixed $\lambda$ and $d$, the new-to-old spacing ratio is $L_2/L_1=3.0/2.0=3/2$, not $2/3$.
- id: p2-screen-distance-direction-b
  content: |-
    It stays the same.
  feedback: |-
    The wavelength and slit separation are fixed, but the screen distance is part of $\Delta y\approx \lambda L/d$. A larger $L$ therefore changes the linear spacing even though the apparatus uses the same light and slits.
- id: p2-screen-distance-direction-c
  content: |-
    It becomes $\tfrac{3}{2}$ as large.
  correct: true
  feedback: |-
    Fringe spacing is directly proportional to screen distance when $\lambda$ and $d$ are fixed. Here $L_2/L_1=3.0/2.0=3/2$, so the new fringe spacing is $3/2$ as large.
- id: p2-screen-distance-direction-d
  content: |-
    It becomes $\left(\tfrac{3}{2}\right)^2$ as large.
  feedback: |-
    Squaring the distance factor would require a dependence on $L^2$. The double-slit relation contains only the first power of $L$, so the spacing changes by $3/2$, not by $(3/2)^2$.
```

---

<a id="scale-the-spacing-without-recalculating"></a>
## Scale the Spacing Without Recalculating

**Example:** The fringe spacing is $4.0\ \mathrm{mm}$ at screen distance $L$. The screen is moved to $1.5L$, with $\lambda$ and $d$ unchanged. Find the new spacing.

**Explanation**

The distance is multiplied by $1.5$, so direct proportionality multiplies the spacing by the same factor:

$$
\Delta y_2=1.5\Delta y_1
=1.5(4.0\ \mathrm{mm})
=6.0\ \mathrm{mm}.
$$

This ratio method is enough; the separate values of $\lambda$ and $d$ are not needed.

The scaling pattern can be read directly:

| Screen distance | Fringe spacing |
| --- | --- |
| $L$ | $\Delta y$ |
| $cL$ | $c\Delta y$ |
| $\frac{1}{2}L$ | $\frac{1}{2}\Delta y$ |

Whatever positive factor multiplies $L$ also multiplies $\Delta y$.

```quiz
type: radio
id: p2-scale-known-spacing
content: |-
  A double-slit pattern has adjacent bright fringes $3.0\ \mathrm{mm}$ apart at screen distance $L$. If the screen is moved to $2L$ while the wavelength and slit separation stay fixed, what is the new spacing?
options:
- id: p2-scale-known-spacing-a
  content: |-
    $1.5\ \mathrm{mm}$
  feedback: |-
    Halving $3.0\ \mathrm{mm}$ treats spacing as inversely proportional to $L$. In fact $\Delta y\propto L$, so doubling $L$ doubles rather than halves the spacing.
- id: p2-scale-known-spacing-b
  content: |-
    $3.0\ \mathrm{mm}$
  feedback: |-
    Keeping $\Delta y$ unchanged ignores the factor of $L$ in $\Delta y\approx \lambda L/d$. With $\lambda$ and $d$ fixed, doubling $L$ must change the on-screen spacing.
- id: p2-scale-known-spacing-c
  content: |-
    $6.0\ \mathrm{mm}$
  correct: true
  feedback: |-
    With the wavelength and slit separation fixed, $\Delta y$ scales by the same factor as $L$. The screen distance doubles, so the new spacing is $2(3.0\ \mathrm{mm})=6.0\ \mathrm{mm}$.
- id: p2-scale-known-spacing-d
  content: |-
    $12.0\ \mathrm{mm}$
  feedback: |-
    A value of $12.0\ \mathrm{mm}$ applies the doubling factor twice. Because $L$ appears only to the first power, apply the factor once: $2(3.0\ \mathrm{mm})=6.0\ \mathrm{mm}$.
```

---

<a id="separate-fringe-angle-from-screen-position"></a>
## Separate Fringe Angle from Screen Position

**Example:** A screen is moved farther from a fixed double slit. Do the bright-fringe angles change, and do the bright-fringe positions on the screen change?

**Explanation**

Separate the pattern's **directions** from its projection onto a screen. The direction of the $m$th bright fringe is set by

$$
d\sin\theta_m=m\lambda.
$$

If $d$ and $\lambda$ do not change, then each angle $\theta_m$ stays the same. However, the screen coordinate is

$$
y_m=L\tan\theta_m\approx L\theta_m.
$$

Increasing $L$ makes the same angular separation cover a larger distance on the screen. The noncentral fringes move farther from the center, while the central fringe remains at $y=0$.

```quiz
type: radio
id: p2-angle-versus-position
content: |-
  The same monochromatic light illuminates the same double slit, but the screen is moved farther away. Which statement correctly compares the new pattern with the old one?
options:
- id: p2-angle-versus-position-a
  content: |-
    The fringe angles increase, but the spacing on the screen stays fixed.
  feedback: |-
    The equation $d\sin\theta_m=m\lambda$ fixes each fringe angle when $d$ and $\lambda$ are unchanged. It is the screen coordinate $y_m=L\tan\theta_m$, not the angle, that grows when $L$ increases.
- id: p2-angle-versus-position-b
  content: |-
    The fringe angles stay fixed, and the spacing on the screen increases.
  correct: true
  feedback: |-
    Fixed $d$ and $\lambda$ keep each order at the same angle through $d\sin\theta_m=m\lambda$. A larger $L$ turns that unchanged angular separation into a larger linear separation because $y_m=L\tan\theta_m$.
- id: p2-angle-versus-position-c
  content: |-
    Both the fringe angles and the spacing on the screen stay fixed.
  feedback: |-
    The angles do stay fixed, but equal angles do not imply equal screen coordinates at different distances. Since $y_m=L\tan\theta_m$, increasing $L$ moves every noncentral fringe farther from the center and increases the spacing.
- id: p2-angle-versus-position-d
  content: |-
    The fringe angles stay fixed, and the spacing on the screen decreases.
  feedback: |-
    Fixed angles are projected onto a more distant screen through $y_m=L\tan\theta_m$. Increasing $L$ enlarges that projection, so the on-screen spacing increases rather than decreases.
```

---

<a id="apply-the-cue-to-the-laboratory-pattern"></a>
## Apply the Cue to the Laboratory Pattern

**Example:** A laboratory double-slit pattern is projected on a screen. The screen is moved farther from the slits, with no change to the light source or slit geometry. Decide whether the fringes become closer together, stay in the same positions, or become farther apart.

**Explanation**

The cue is that only $L$ changes. Because $\Delta y\approx \lambda L/d$ and the fixed apparatus keeps $\lambda$ and $d$ constant, increasing $L$ increases $\Delta y$. The fringes become farther apart.

```quiz
type: radio
id: p2-assignment-transfer
shuffle: true
content: |-
  A laboratory experiment produces a double-slit interference pattern on a screen. If the screen is moved farther away from the slits, the fringes will be _____.

  ![](<../Source/Images/double-slit-fringe-spacing-pattern.png>)
options:
- id: p2-assignment-transfer-a
  content: |-
    Closer together
  feedback: |-
    Closer fringes would follow from decreasing $L$ or from increasing $d$ while the other quantities stay fixed. Here the screen is moved farther away, and $\Delta y\approx \lambda L/d$ therefore increases.
- id: p2-assignment-transfer-b
  content: |-
    In the same positions
  feedback: |-
    The fringe orders remain at the same angles, not at the same screen coordinates. Since $y_m=L\tan\theta_m$, increasing $L$ moves each noncentral fringe farther from the center.
- id: p2-assignment-transfer-c
  content: |-
    Farther apart
  correct: true
  feedback: |-
    Double-slit fringe spacing is directly proportional to screen distance: $\Delta y\approx \lambda L/d$. With the wavelength and slit separation fixed, increasing $L$ increases $\Delta y$, so the fringes are farther apart.
```

---

<a id="summary"></a>
## Summary

When only the screen distance changes in a double-slit experiment:

1. Identify $L$ as the slit-to-screen distance.
2. Hold the unchanged wavelength $\lambda$ and slit separation $d$ fixed.
3. Use $\Delta y\approx \lambda L/d$, so $\Delta y\propto L$.
4. Scale the spacing by $L_2/L_1$.

The main trap is confusing angle with screen position. The fringe angles stay fixed when $\lambda$ and $d$ stay fixed, but a farther screen turns those same angles into larger distances, so the fringes spread farther apart.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
