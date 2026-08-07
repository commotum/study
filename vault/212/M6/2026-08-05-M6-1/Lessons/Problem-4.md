# Finding Wavelength From a Double-Slit Intensity Graph

## Table of Contents

- [Introduction](#introduction)
- [Read the Spacing Between Bright Peaks](#read-the-spacing-between-bright-peaks)
- [Use Several Intervals When Helpful](#use-several-intervals-when-helpful)
- [Convert Every Length Before Substitution](#convert-every-length-before-substitution)
- [Apply the Full Graph-to-Wavelength Chain](#apply-the-full-graph-to-wavelength-chain)
- [Summary](#summary)

## Prerequisites

- Read horizontal coordinates and distances from a graph.
- Convert centimeters and millimeters to meters.
- Isolate a variable in a multiplication-and-division formula.

---

<a id="introduction"></a>
## Introduction

When a double-slit problem gives intensity as a function of position on a screen, the centers of the bright peaks mark constructive-interference maxima. Under the small-angle approximation, neighboring bright peaks are separated by

$$
\Delta x=\frac{\lambda L}{d},
$$

where $\lambda$ is the wavelength, $L$ is the slit-to-screen distance, and $d$ is the distance between the slit centers. Solving for the requested wavelength gives

$$
\boxed{\lambda=\frac{\Delta x\,d}{L}}.
$$

The graph cue is **horizontal peak-to-peak spacing**. Peak height describes intensity, so neither the height of a peak nor the width of the broad envelope is $\Delta x$.

---

<a id="read-the-spacing-between-bright-peaks"></a>
## Read the Spacing Between Bright Peaks

**Example:** An intensity graph has consecutive bright-peak centers at $x=-1.2\ \mathrm{cm}$, $0$, and $1.2\ \mathrm{cm}$. Find the fringe spacing.

**Explanation**

Subtract the horizontal coordinates of any two neighboring peak centers:

$$
\Delta x=1.2\ \mathrm{cm}-0=1.2\ \mathrm{cm}.
$$

The three peaks may have different heights because of a diffraction envelope, but their horizontal separation is still the quantity used in the double-slit spacing formula.

```quiz
type: radio
id: p4-adjacent-spacing
content: |-
  Consecutive bright-peak centers occur at $x=-2.0$, $-0.5$, $1.0$, and $2.5\ \mathrm{cm}$. What is the fringe spacing $\Delta x$?
options:
- id: p4-adjacent-spacing-a
  content: |-
    $4.5\ \mathrm{cm}$
  feedback: |-
    $4.5\ \mathrm{cm}$ is the full distance from the first peak to the fourth peak. That span contains three equal peak-to-peak intervals, so the fringe spacing is $4.5/3=1.5\ \mathrm{cm}$.
- id: p4-adjacent-spacing-b
  content: |-
    $1.125\ \mathrm{cm}$
  feedback: |-
    This divides the $4.5\ \mathrm{cm}$ span by four peak centers. Four peaks create only three gaps; fringe spacing is distance divided by the number of gaps, giving $4.5/3=1.5\ \mathrm{cm}$.
- id: p4-adjacent-spacing-c
  content: |-
    $1.5\ \mathrm{cm}$
  correct: true
  feedback: |-
    Fringe spacing is the horizontal distance between neighboring bright-peak centers. For example, $1.0-(-0.5)=1.5$, so $\Delta x=1.5\ \mathrm{cm}$.
- id: p4-adjacent-spacing-d
  content: |-
    $0.5\ \mathrm{cm}$
  feedback: |-
    $0.5\ \mathrm{cm}$ is the magnitude of one peak's coordinate, not the distance between two peaks. Subtract neighboring coordinates: $1.0-(-0.5)=1.5\ \mathrm{cm}$.
- id: p4-adjacent-spacing-e
  content: |-
    $3.0\ \mathrm{cm}$
  feedback: |-
    A $3.0\ \mathrm{cm}$ difference skips one bright peak and covers two fringe intervals. Dividing by two gives the adjacent-peak spacing $\Delta x=1.5\ \mathrm{cm}$.
```

---

<a id="use-several-intervals-when-helpful"></a>
## Use Several Intervals When Helpful

**Example:** Five consecutive bright peaks extend from $x=-3.0\ \mathrm{cm}$ to $x=3.0\ \mathrm{cm}$. Find their average spacing.

**Explanation**

The full span is $|3.0-(-3.0)|=6.0\ \mathrm{cm}$. Five peaks create four intervals, so

$$
\Delta x=\frac{6.0\ \mathrm{cm}}{4}=1.5\ \mathrm{cm}.
$$

Measuring across several intervals can reduce graph-reading uncertainty. Count **gaps**, not peaks.

```quiz
type: radio
id: p4-multiple-intervals
content: |-
  Six consecutive bright-peak centers run from $x=-4.8\ \mathrm{cm}$ to $x=3.2\ \mathrm{cm}$. What average fringe spacing do these peaks give?
options:
- id: p4-multiple-intervals-a
  content: |-
    $8.0\ \mathrm{cm}$
  feedback: |-
    $8.0\ \mathrm{cm}$ is the entire first-to-last span. Six consecutive peaks make five equal gaps, so the adjacent spacing is $8.0/5=1.6\ \mathrm{cm}$.
- id: p4-multiple-intervals-b
  content: |-
    $1.33\ \mathrm{cm}$
  feedback: |-
    This divides by the six peak centers instead of the five intervals between them. The correct count is one fewer gap than peaks, so $\Delta x=8.0/5=1.6\ \mathrm{cm}$.
- id: p4-multiple-intervals-c
  content: |-
    $1.6\ \mathrm{cm}$
  correct: true
  feedback: |-
    The endpoint separation is $|3.2-(-4.8)|=8.0\ \mathrm{cm}$, and six peaks form five gaps. Therefore $\Delta x=8.0/5=1.6\ \mathrm{cm}$.
- id: p4-multiple-intervals-d
  content: |-
    $3.2\ \mathrm{cm}$
  feedback: |-
    $3.2\ \mathrm{cm}$ spans two adjacent gaps in this pattern. Fringe spacing measures one gap, so divide that two-gap distance by two to obtain $1.6\ \mathrm{cm}$.
- id: p4-multiple-intervals-e
  content: |-
    $0.80\ \mathrm{cm}$
  feedback: |-
    This halves the one-gap spacing. The measured $8.0\ \mathrm{cm}$ span contains five, not ten, intervals, so $\Delta x=8.0/5=1.6\ \mathrm{cm}$.
```

---

<a id="convert-every-length-before-substitution"></a>
## Convert Every Length Before Substitution

**Example:** A pattern has $\Delta x=0.80\ \mathrm{cm}$, slit separation $d=0.050\ \mathrm{mm}$, and screen distance $L=1.0\ \mathrm{m}$. Find the wavelength.

**Explanation**

Convert the two smaller lengths to meters so every factor uses the same base unit. Write each conversion factor so the starting unit visibly cancels:

$$
\Delta x
=(0.80\ \mathrm{cm})\left(\frac{10^{-2}\ \mathrm{m}}{1\ \mathrm{cm}}\right)
=8.0\times10^{-3}\ \mathrm{m},
\qquad
d
=(0.050\ \mathrm{mm})\left(\frac{10^{-3}\ \mathrm{m}}{1\ \mathrm{mm}}\right)
=5.0\times10^{-5}\ \mathrm{m}.
$$

Then

$$
\lambda
=\frac{\Delta x\,d}{L}
=\frac{(8.0\times10^{-3}\ \mathrm{m})(5.0\times10^{-5}\ \mathrm{m})}{1.0\ \mathrm{m}}
=4.0\times10^{-7}\ \mathrm{m}
=400\ \mathrm{nm}.
$$

The units reduce to meters, as a wavelength should: $(\mathrm{m})(\mathrm{m})/\mathrm{m}=\mathrm{m}$.

```quiz
type: radio
id: p4-convert-lengths
content: |-
  Before using $\lambda=\Delta x d/L$, which pair correctly converts $\Delta x=1.2\ \mathrm{cm}$ and $d=0.040\ \mathrm{mm}$ to meters?
options:
- id: p4-convert-lengths-a
  content: |-
    $\Delta x=1.2\times10^{-1}\ \mathrm{m}$ and $d=4.0\times10^{-4}\ \mathrm{m}$
  feedback: |-
    Both decimal shifts are one place too small. A centimeter is $10^{-2}\ \mathrm{m}$ and a millimeter is $10^{-3}\ \mathrm{m}$, so the values are $1.2\times10^{-2}\ \mathrm{m}$ and $4.0\times10^{-5}\ \mathrm{m}$.
- id: p4-convert-lengths-b
  content: |-
    $\Delta x=1.2\times10^{-2}\ \mathrm{m}$ and $d=4.0\times10^{-2}\ \mathrm{m}$
  feedback: |-
    The centimeter conversion is correct, but $0.040\ \mathrm{mm}$ is much smaller than a centimeter. Multiplying $0.040$ by $10^{-3}\ \mathrm{m/mm}$ gives $4.0\times10^{-5}\ \mathrm{m}$.
- id: p4-convert-lengths-c
  content: |-
    $\Delta x=1.2\times10^{-2}\ \mathrm{m}$ and $d=4.0\times10^{-5}\ \mathrm{m}$
  correct: true
  feedback: |-
    Since $1\ \mathrm{cm}=10^{-2}\ \mathrm{m}$ and $1\ \mathrm{mm}=10^{-3}\ \mathrm{m}$, $1.2\ \mathrm{cm}=1.2\times10^{-2}\ \mathrm{m}$ and $0.040\ \mathrm{mm}=4.0\times10^{-5}\ \mathrm{m}$.
- id: p4-convert-lengths-d
  content: |-
    $\Delta x=1.2\times10^{-3}\ \mathrm{m}$ and $d=4.0\times10^{-5}\ \mathrm{m}$
  feedback: |-
    The slit conversion is correct, but this treats centimeters as though they were millimeters. Because $1\ \mathrm{cm}=10^{-2}\ \mathrm{m}$, the spacing is $1.2\times10^{-2}\ \mathrm{m}$.
- id: p4-convert-lengths-e
  content: |-
    $\Delta x=1.2\times10^{-2}\ \mathrm{m}$ and $d=4.0\times10^{-8}\ \mathrm{m}$
  feedback: |-
    The spacing conversion is correct, but converting millimeters to meters contributes $10^{-3}$, not $10^{-6}$. Thus $0.040\times10^{-3}=4.0\times10^{-5}\ \mathrm{m}$.
```

---

<a id="apply-the-full-graph-to-wavelength-chain"></a>
## Apply the Full Graph-to-Wavelength Chain

**Example:** A double slit has center-to-center separation $d=0.062\ \mathrm{mm}$ and is $L=0.85\ \mathrm{m}$ from the screen. Use the intensity graph to find the wavelength in nanometers.

![](<../Source/Images/double-slit-intensity-position-graph.png>)

**Explanation**

The central bright peak is centered at $x=0$, and the next bright peak is centered at $x=1.0\ \mathrm{cm}$ (the peak at $x=-1.0\ \mathrm{cm}$ gives the same spacing). The peak heights vary, but their horizontal centers remain one fringe apart. Therefore,

$$
\Delta x=1.0\ \mathrm{cm}=1.0\times10^{-2}\ \mathrm{m},
\qquad
d=0.062\ \mathrm{mm}=6.2\times10^{-5}\ \mathrm{m}.
$$

Substitute into the wavelength formula:

$$
\begin{aligned}
\lambda
&=\frac{\Delta x\,d}{L} \\
&=\frac{(1.0\times10^{-2}\ \mathrm{m})(6.2\times10^{-5}\ \mathrm{m})}{0.85\ \mathrm{m}} \\
&=7.294\ldots\times10^{-7}\ \mathrm{m} \\
&=729.4\ldots\ \mathrm{nm}.
\end{aligned}
$$

The measured values have two significant figures, so the wavelength is $7.3\times10^2\ \mathrm{nm}$. Entered as a number only, the answer is **730**.

```quiz
type: radio
id: p4-full-chain
content: |-
  A double-slit intensity graph has adjacent bright peaks $0.75\ \mathrm{cm}$ apart. The slit separation is $0.080\ \mathrm{mm}$, and the screen is $1.20\ \mathrm{m}$ away. What is the wavelength?
options:
- id: p4-full-chain-a
  content: |-
    $50\ \mathrm{nm}$
  feedback: |-
    This results if $0.75\ \mathrm{cm}$ is made ten times too small. The correct spacing is $7.5\times10^{-3}\ \mathrm{m}$; then $\lambda=(7.5\times10^{-3})(8.0\times10^{-5})/1.20=5.0\times10^{-7}\ \mathrm{m}=500\ \mathrm{nm}$.
- id: p4-full-chain-b
  content: |-
    $5000\ \mathrm{nm}$
  feedback: |-
    This results if $0.080\ \mathrm{mm}$ is converted as $8.0\times10^{-4}\ \mathrm{m}$, ten times too large. The correct slit spacing is $8.0\times10^{-5}\ \mathrm{m}$, which gives $500\ \mathrm{nm}$.
- id: p4-full-chain-c
  content: |-
    $500\ \mathrm{nm}$
  correct: true
  feedback: |-
    Adjacent bright peaks give $\Delta x=7.5\times10^{-3}\ \mathrm{m}$, and $d=8.0\times10^{-5}\ \mathrm{m}$. Thus $\lambda=\Delta x d/L=5.0\times10^{-7}\ \mathrm{m}=500\ \mathrm{nm}$.
- id: p4-full-chain-d
  content: |-
    $0.500\ \mathrm{nm}$
  feedback: |-
    The formula gives $5.0\times10^{-7}\ \mathrm{m}$, but meters convert to nanometers by multiplying by $10^9$, not $10^6$. Therefore the wavelength is $500\ \mathrm{nm}$.
- id: p4-full-chain-e
  content: |-
    $5.0\times10^{-7}\ \mathrm{nm}$
  feedback: |-
    $5.0\times10^{-7}$ is the numerical value when the unit is meters. Relabeling it as nanometers changes the physical length; multiplying by $10^9\ \mathrm{nm/m}$ gives $500\ \mathrm{nm}$.
```

---

<a id="summary"></a>
## Summary

When a double-slit intensity graph and the distances $d$ and $L$ are given:

1. Read $\Delta x$ as the **horizontal distance between adjacent bright-peak centers**; ignore peak height.
2. If you measure across several peaks, divide the total span by the number of gaps, which is one fewer than the number of peaks.
3. Convert $\Delta x$, $d$, and $L$ to compatible units.
4. Compute $\lambda=\Delta x d/L$ and check that the units reduce to a length.
5. Convert meters to nanometers with $1\ \mathrm{m}=10^9\ \mathrm{nm}$, then round to the precision supported by the data.
