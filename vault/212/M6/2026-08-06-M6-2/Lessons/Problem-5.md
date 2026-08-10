# Estimating Secondary Bright Fringes in Single-Slit Diffraction

<!--
lesson-id: 212-M6-010
topic-code: MTH212.M6.10
-->
## Table of Contents

- [Introduction](#introduction)
- [Match a Bright Fringe to Its Neighboring Minima](#match-a-bright-fringe-to-its-neighboring-minima)
- [Estimate the Midpoint](#estimate-the-midpoint)
- [Use the Compact Bright-Fringe Formula](#use-the-compact-bright-fringe-formula)
- [Convert Units and Report the Distance](#convert-units-and-report-the-distance)
- [Variant: Solve the Bright-Fringe Relation Backward](#variant-solve-the-bright-fringe-relation-backward)
- [Summary](#summary)

## Prerequisites

- Use the small-angle location of the $m$th single-slit dark minimum: $y_m\approx m\lambda L/a$.
- Convert nanometers and millimeters to meters: $1\ \mathrm{nm}=10^{-9}\ \mathrm{m}$ and $1\ \mathrm{mm}=10^{-3}\ \mathrm{m}$.
- Find the midpoint of two positions by averaging them.
- Round a calculated measurement to a requested number of significant figures.

---

<a id="introduction"></a>
## Introduction

When a single-slit problem asks for a **secondary bright fringe** rather than a dark minimum, first identify the two neighboring dark minima. In the approximation used here, the bright fringe lies halfway between them.

For the $n$th secondary bright fringe, count $n=1,2,3,\ldots$ outward from the central maximum. It lies between dark minima $m=n$ and $m=n+1$. Therefore,

$$
y_{\text{bright},n}
\approx \frac{y_n+y_{n+1}}{2}
=\left(n+\frac12\right)\frac{\lambda L}{a}.
$$

This is a midpoint approximation for small diffraction angles; secondary maxima are not exactly halfway between minima. Use it when the course or problem specifies this approximation.

---

<a id="match-a-bright-fringe-to-its-neighboring-minima"></a>
## Match a Bright Fringe to Its Neighboring Minima

**Example:** Which dark minima bracket the third secondary bright fringe?

**Explanation**

The $n$th secondary bright fringe lies between dark minima $m=n$ and $m=n+1$. Setting $n=3$ gives the pair $m=3$ and $m=4$, so the third secondary bright fringe lies between $y_3$ and $y_4$.

The central maximum is not the first secondary bright fringe. The secondary-fringe count starts after the first dark minimum.

| Secondary bright fringe | Neighboring dark minima | Midpoint multiplier |
| ---: | ---: | ---: |
| $n=1$ | $y_1$ and $y_2$ | $1.5$ |
| $n=2$ | $y_2$ and $y_3$ | $2.5$ |
| $n=3$ | $y_3$ and $y_4$ | $3.5$ |

The lower dark-minimum index, the bright-fringe number, and the whole-number part of the multiplier all match.

```quiz
type: radio
id: p5-indexing-q1
content: |-
  Which pair of dark minima brackets the fourth secondary bright fringe?
options:
- id: p5-indexing-q1-a
  content: |-
    $y_3$ and $y_4$
  feedback: |-
    This pair brackets the third secondary bright fringe. The fringe number matches the lower dark-minimum index, so the fourth secondary bright fringe instead begins with $y_4$.
- id: p5-indexing-q1-b
  content: |-
    $y_4$ and $y_5$
  correct: true
  feedback: |-
    The $n$th secondary bright fringe lies between $y_n$ and $y_{n+1}$. With $n=4$, the neighboring dark minima are $y_4$ and $y_5$.
- id: p5-indexing-q1-c
  content: |-
    $y_5$ and $y_6$
  feedback: |-
    This pair brackets the fifth secondary bright fringe. Starting at $y_5$ shifts both bounding minima one interval too far from the center; the fourth fringe starts at $y_4$.
- id: p5-indexing-q1-d
  content: |-
    $y_1$ and $y_4$
  feedback: |-
    A secondary maximum is bracketed by consecutive dark minima, not by all minima counted up to its index. The consecutive pair for $n=4$ is $y_4$ and $y_5$.
- id: p5-indexing-q1-e
  content: |-
    The central maximum and $y_4$
  feedback: |-
    The central maximum is a broad bright region, not a dark minimum that bounds the fourth secondary fringe. That fringe occupies the single interval between dark minima $y_4$ and $y_5$.
```

---

<a id="estimate-the-midpoint"></a>
## Estimate the Midpoint

**Example:** A slit produces its second and third dark minima at $y_2=0.780\ \mathrm{cm}$ and $y_3=1.170\ \mathrm{cm}$. Estimate the position of the second secondary bright fringe.

**Explanation**

The second secondary bright fringe lies in the interval from $y_2$ to $y_3$. Average the endpoints:

$$
y_{\text{bright},2}
\approx \frac{0.780\ \mathrm{cm}+1.170\ \mathrm{cm}}{2}
=0.975\ \mathrm{cm}.
$$

The midpoint is an absolute position measured from the central maximum. It is not merely half the separation between the two minima.

```quiz
type: radio
id: p5-midpoint-q1
content: |-
  The third and fourth dark minima occur at $1.20\ \mathrm{cm}$ and $1.60\ \mathrm{cm}$ from the central maximum. Using the midpoint approximation, where is the third secondary bright fringe?
options:
- id: p5-midpoint-q1-a
  content: |-
    $0.20\ \mathrm{cm}$
  feedback: |-
    This is half the separation between the minima, but it omits their position relative to the center. Add that half-separation to $1.20\ \mathrm{cm}$, or average the two positions directly.
- id: p5-midpoint-q1-b
  content: |-
    $0.40\ \mathrm{cm}$
  feedback: |-
    This is the full spacing between the neighboring minima. The question asks for the bright fringe's position from the central maximum, so average $1.20\ \mathrm{cm}$ and $1.60\ \mathrm{cm}$.
- id: p5-midpoint-q1-c
  content: |-
    $1.20\ \mathrm{cm}$
  feedback: |-
    This is the lower bounding dark minimum $y_3$, where the intensity is minimal. The nearby bright fringe is halfway from this minimum to $y_4$.
- id: p5-midpoint-q1-d
  content: |-
    $1.40\ \mathrm{cm}$
  correct: true
  feedback: |-
    The secondary maximum is approximated by the midpoint of its two neighboring minima. Averaging $1.20\ \mathrm{cm}$ and $1.60\ \mathrm{cm}$ gives $1.40\ \mathrm{cm}$.
- id: p5-midpoint-q1-e
  content: |-
    $1.60\ \mathrm{cm}$
  feedback: |-
    This is the upper bounding dark minimum $y_4$, not the bright fringe between the minima. The midpoint must lie strictly between $1.20\ \mathrm{cm}$ and $1.60\ \mathrm{cm}$.
```

---

<a id="use-the-compact-bright-fringe-formula"></a>
## Use the Compact Bright-Fringe Formula

**Example:** Light of wavelength $500\ \mathrm{nm}$ passes through a slit of width $0.250\ \mathrm{mm}$. A screen is $2.00\ \mathrm{m}$ away. Estimate the distance from the center to the third secondary bright fringe.

**Explanation**

Because the third secondary bright fringe lies halfway between $y_3$ and $y_4$, its multiplier is $3+\tfrac12=3.5$. First calculate the spacing between consecutive dark minima:

$$
\begin{aligned}
\Delta y_{\text{dark}}
&=\frac{\lambda L}{a} \\
&=\frac{(500\times10^{-9}\ \mathrm{m})(2.00\ \mathrm{m})}
{0.250\times10^{-3}\ \mathrm{m}} \\
&=0.00400\ \mathrm{m}=0.400\ \mathrm{cm}.
\end{aligned}
$$

Then apply the bright-fringe multiplier:

$$
y_{\text{bright},3}
\approx 3.5\Delta y_{\text{dark}}
=3.5(0.400\ \mathrm{cm})
=1.40\ \mathrm{cm}.
$$

Separating spacing from indexing makes the roles clear: $\lambda$, $L$, and $a$ determine the scale, while $n+\tfrac12$ selects the fringe. The integer factors $n$ and $n+1$ instead locate the neighboring dark minima.

```quiz
type: radio
id: p5-formula-q1
content: |-
  Light of wavelength $600\ \mathrm{nm}$ passes through a $0.300\ \mathrm{mm}$ slit, and the screen is $1.00\ \mathrm{m}$ away. Estimate the distance to the second secondary bright fringe.
options:
- id: p5-formula-q1-a
  content: |-
    $0.200\ \mathrm{cm}$
  feedback: |-
    This is the one-minimum spacing $\lambda L/a$. The second secondary bright fringe is farther out, between minima $m=2$ and $m=3$, so this spacing must be multiplied by $2.5$.
- id: p5-formula-q1-b
  content: |-
    $0.400\ \mathrm{cm}$
  feedback: |-
    Multiplying by $2$ gives the second dark minimum $y_2$. The second secondary bright fringe is halfway from $y_2$ to $y_3$, so its multiplier is $2.5$.
- id: p5-formula-q1-c
  content: |-
    $0.500\ \mathrm{cm}$
  correct: true
  feedback: |-
    The second secondary bright fringe uses the factor $2.5$. Since $\lambda L/a=0.200\ \mathrm{cm}$ here, $y_{\text{bright},2}\approx2.5(0.200\ \mathrm{cm})=0.500\ \mathrm{cm}$.
- id: p5-formula-q1-d
  content: |-
    $0.600\ \mathrm{cm}$
  feedback: |-
    Multiplying the minimum spacing by $3$ gives the third dark minimum $y_3$. The bright fringe is halfway between $y_2$ and $y_3$, so use $2.5$ rather than $3$.
- id: p5-formula-q1-e
  content: |-
    $1.00\ \mathrm{cm}$
  feedback: |-
    This uses a factor of $5$ instead of $5/2$. The midpoint average includes division by $2$, giving the second-fringe multiplier $2.5$ and a result half this large.
```

---

<a id="convert-units-and-report-the-distance"></a>
## Convert Units and Report the Distance

**Example:** A $633\ \mathrm{nm}$ laser illuminates a single slit of width $0.145\ \mathrm{mm}$. The screen is $1.28\ \mathrm{m}$ away. Find the distance from the central maximum to the second secondary bright fringe in centimeters, as a number with three significant figures.

**Explanation**

For the second secondary bright fringe, $n=2$ and the multiplier is $2.5$. Use consistent SI units before calculating:

$$
\lambda=633\times10^{-9}\ \mathrm{m},
\qquad
a=0.145\times10^{-3}\ \mathrm{m}.
$$

Then

$$
\begin{aligned}
y_{\text{bright},2}
&\approx \frac{5\lambda L}{2a} \\
&=\frac{5(633\times10^{-9}\ \mathrm{m})(1.28\ \mathrm{m})}
{2(0.145\times10^{-3}\ \mathrm{m})} \\
&=0.0139696\ldots\ \mathrm{m} \\
&=1.39696\ldots\ \mathrm{cm}.
\end{aligned}
$$

The units provide a quick check:

$$
\left[\frac{\lambda L}{a}\right]
=\frac{(\mathrm{m})(\mathrm{m})}{\mathrm{m}}
=\mathrm{m},
$$

so the formula produces a length. The value also lies between the second and third dark minima, $1.11757\ldots\ \mathrm{cm}$ and $1.67636\ldots\ \mathrm{cm}$, as a midpoint must.

The requested distance is a positive magnitude. To three significant figures it is $1.40\ \mathrm{cm}$, so the number-only entry is `1.40`. The trailing zero communicates the requested precision.

```quiz
type: radio
id: p5-reporting-q1
content: |-
  A $488\ \mathrm{nm}$ laser illuminates a slit of width $0.160\ \mathrm{mm}$, with a screen $1.20\ \mathrm{m}$ away. Using the same approximation, what is the distance to the second secondary bright fringe in centimeters, to three significant figures?
options:
- id: p5-reporting-q1-a
  content: |-
    $0.366\ \mathrm{cm}$
  feedback: |-
    This is the base minimum spacing $\lambda L/a$, not the second secondary bright-fringe distance. The second bright fringe requires the factor $2.5$ before rounding.
- id: p5-reporting-q1-b
  content: |-
    $0.732\ \mathrm{cm}$
  feedback: |-
    This is the second dark-minimum position, obtained with the factor $2$. The second secondary maximum lies halfway toward the third minimum, so use the factor $2.5$.
- id: p5-reporting-q1-c
  content: |-
    $0.915\ \mathrm{cm}$
  correct: true
  feedback: |-
    The second secondary bright fringe uses $y\approx2.5\lambda L/a$. Substitution gives $0.00915\ \mathrm{m}$, and multiplying by $100\ \mathrm{cm/m}$ gives $0.915\ \mathrm{cm}$ to three significant figures.
- id: p5-reporting-q1-d
  content: |-
    $1.10\ \mathrm{cm}$
  feedback: |-
    This is the third dark-minimum position, based on the factor $3$. The requested bright fringe lies between the second and third minima, so its factor is $2.5$ and its position must lie between $0.732\ \mathrm{cm}$ and $1.10\ \mathrm{cm}$.
- id: p5-reporting-q1-e
  content: |-
    $91.5\ \mathrm{cm}$
  feedback: |-
    The calculated position is $0.00915\ \mathrm{m}$. Converting meters to centimeters requires one factor of $100$, producing $0.915\ \mathrm{cm}$; this choice applies that conversion factor twice.
```

---

<a id="variant-solve-the-bright-fringe-relation-backward"></a>
## Variant: Solve the Bright-Fringe Relation Backward

If the bright-fringe position is measured and the wavelength is unknown, rearrange the same midpoint approximation instead of changing the fringe index.

```quiz
type: blank
id: khadley-single-slit-q2
input_mode: math
require_exact: true
content: |-
  A single slit of width $0.15\ \mathrm{mm}$ is $5.3\ \mathrm m$ from a screen. The second secondary bright fringe is $6.2\ \mathrm{cm}$ from center. Using the midpoint approximation, find the wavelength in nanometers: ==700==
feedback: |-
  The second secondary maximum lies approximately halfway between minima $p=2$ and $p=3$, so $y\approx2.5\lambda L/a$. Thus $\lambda=ya/(2.5L)=7.0\times10^{-7}\ \mathrm m=7.0\times10^2\ \mathrm{nm}$.
```

---

<a id="summary"></a>
## Summary

When a problem asks for the $n$th secondary bright fringe in the midpoint approximation:

1. Identify its neighboring dark minima: $y_n$ and $y_{n+1}$.
2. Average their positions, or use

   $$
   y_{\text{bright},n}\approx\left(n+\frac12\right)\frac{\lambda L}{a}.
   $$

3. Convert $\lambda$ and $a$ to compatible units before substituting.
4. Convert the final length to the requested unit and round only at the end.
5. Check that the result is a positive length between $n\lambda L/a$ and $(n+1)\lambda L/a$.

The main indexing trap is using $n$ or $n+1$, which gives a dark minimum rather than the bright fringe between them.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
