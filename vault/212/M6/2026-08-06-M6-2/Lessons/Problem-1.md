# Finding Slit Width from Adjacent Single-Slit Minima

<!--
lesson-id: 212-M6-006
topic-code: MTH212.M6.06
-->
## Table of Contents

- [Introduction](#introduction)
- [Turn Two Minima into One Spacing](#turn-two-minima-into-one-spacing)
- [Isolate the Slit Width](#isolate-the-slit-width)
- [Calculate with One Unit System](#calculate-with-one-unit-system)
- [Distinguish Adjacent Minima from the Central Width](#distinguish-adjacent-minima-from-the-central-width)
- [Summary](#summary)

## Prerequisites

- Rearranging a one-step formula
- Converting among nanometers, millimeters, and meters
- Subtracting two positions measured from the same origin

---

<a id="introduction"></a>
## Introduction

For a slit of width $a$, dark single-slit minima obey

$$
a\sin\theta_m=m\lambda,
$$

where $m=1,2,3,\ldots$. When the diffraction angles are small,
$y_m\approx L\sin\theta_m$, so the position of the $m$th minimum is

$$
y_m\approx \frac{m\lambda L}{a}.
$$

The recognition cue is a measured distance between neighboring dark minima. Subtracting their positions cancels the order number:

$$
\Delta y=y_{m+1}-y_m\approx\frac{\lambda L}{a}.
$$

More generally, minima $m$ and $n$ on the same side span $|n-m|$ equal gaps. The spacing of one gap is

$$
\Delta y
=\frac{|y_n-y_m|}{|n-m|}
\approx\frac{\lambda L}{a}.
$$

For the first and second minima, $|2-1|=1$, so their measured separation is already one $\Delta y$.

Therefore, the slit width is

$$
\boxed{a\approx\frac{\lambda L}{\Delta y}}.
$$

This small-angle relation applies when the fringe displacement is much smaller than the screen distance. In Problem 1, $\lambda=633\ \mathrm{nm}$, $L=1.50\ \mathrm{m}$, and the given $5.75\ \mathrm{mm}$ is already the spacing between the first and second minima. The requested output is $a$ in millimeters.

---

<a id="turn-two-minima-into-one-spacing"></a>
## Turn Two Minima into One Spacing

**Example:** On one side of the central maximum, the first two dark minima are at $y_1=8.2\ \mathrm{mm}$ and $y_2=12.3\ \mathrm{mm}$. Find their spacing.

**Explanation**

Spacing is a difference of positions, not their sum and not either position by itself:

$$
\Delta y=y_2-y_1=12.3\ \mathrm{mm}-8.2\ \mathrm{mm}=4.1\ \mathrm{mm}.
$$

Before using a separation as $\Delta y$, count the order gaps. These minima are adjacent, so $m$ changes by exactly $1$ and no extra divisor remains. If the first and third minima had been measured instead, their total separation would span two equal gaps and would need to be divided by $2$.

```quiz
type: radio
id: m6-2-p1-spacing
content: |-
  Two adjacent dark minima on the same side of the center are at $y_1=7.2\ \mathrm{mm}$ and $y_2=10.8\ \mathrm{mm}$. What spacing belongs in $a=\lambda L/\Delta y$?
options:
- id: m6-2-p1-spacing-a
  content: |-
    $3.6\ \mathrm{mm}$
  correct: true
  feedback: |-
    Adjacent-minimum spacing is the difference of positions measured from the same origin. Thus $\Delta y=y_2-y_1=10.8-7.2=3.6\ \mathrm{mm}$.
- id: m6-2-p1-spacing-b
  content: |-
    $18.0\ \mathrm{mm}$
  feedback: |-
    Adding the two coordinates gives their combined distance from the origin, not the distance between them. Use $|y_2-y_1|$, which gives $3.6\ \mathrm{mm}$ here.
- id: m6-2-p1-spacing-c
  content: |-
    $7.2\ \mathrm{mm}$
  feedback: |-
    $7.2\ \mathrm{mm}$ is the first minimum's position relative to the center. The formula needs the gap between the two minima, $10.8-7.2=3.6\ \mathrm{mm}$.
- id: m6-2-p1-spacing-d
  content: |-
    $10.8\ \mathrm{mm}$
  feedback: |-
    $10.8\ \mathrm{mm}$ locates the second minimum relative to the center; it is not the adjacent gap. Subtract the first position to obtain $3.6\ \mathrm{mm}$.
- id: m6-2-p1-spacing-e
  content: |-
    $1.8\ \mathrm{mm}$
  feedback: |-
    Halving the difference is unnecessary for two adjacent minima on the same side. The full gap is $10.8-7.2=3.6\ \mathrm{mm}$; halving is used only when converting a central-maximum width into its one-sided distance.
```

---

<a id="isolate-the-slit-width"></a>
## Isolate the Slit Width

**Example:** Rearrange $\Delta y=\lambda L/a$ to solve for $a$.

**Explanation**

Multiply both sides by $a$, then divide both sides by $\Delta y$:

$$
a\Delta y=\lambda L
\qquad\Longrightarrow\qquad
a=\frac{\lambda L}{\Delta y}.
$$

This form also encodes an inverse relationship: with $\lambda$ and $L$ fixed, a larger fringe spacing comes from a narrower slit.

```quiz
type: radio
id: m6-2-p1-rearrange
content: |-
  Given $\Delta y=\lambda L/a$, which expression correctly isolates the slit width $a$?
options:
- id: m6-2-p1-rearrange-a
  content: |-
    $\dfrac{\lambda L}{\Delta y}$
  correct: true
  feedback: |-
    Multiplying by $a$ gives $a\Delta y=\lambda L$, and dividing by $\Delta y$ gives $a=\lambda L/\Delta y$. This also preserves the inverse relation between slit width and fringe spacing.
- id: m6-2-p1-rearrange-b
  content: |-
    $\dfrac{\Delta y}{\lambda L}$
  feedback: |-
    This is the reciprocal of the required width. From $a\Delta y=\lambda L$, $\Delta y$ must divide $\lambda L$, so $a=\lambda L/\Delta y$.
- id: m6-2-p1-rearrange-c
  content: |-
    $\dfrac{\lambda\Delta y}{L}$
  feedback: |-
    This swaps the roles of $L$ and $\Delta y$. The product already opposite $a$ is $\lambda L$, so that product stays in the numerator and $\Delta y$ becomes the divisor.
- id: m6-2-p1-rearrange-d
  content: |-
    $\dfrac{L\Delta y}{\lambda}$
  feedback: |-
    Dividing by $\lambda$ does not follow from $a\Delta y=\lambda L$. Isolating $a$ requires division by its factor $\Delta y$, giving $a=\lambda L/\Delta y$.
- id: m6-2-p1-rearrange-e
  content: |-
    $\lambda L\Delta y$
  feedback: |-
    Multiplying by $\Delta y$ leaves the factor attached to $a$ instead of removing it. Divide $a\Delta y=\lambda L$ by $\Delta y$ to isolate $a$.
```

---

<a id="calculate-with-one-unit-system"></a>
## Calculate with One Unit System

**Example:** Light of wavelength $520\ \mathrm{nm}$ produces adjacent minima $4.50\ \mathrm{mm}$ apart on a screen $1.80\ \mathrm{m}$ away. Find $a$ in millimeters.

**Explanation**

One reliable choice is to convert every length to millimeters before substituting:

$$
\begin{aligned}
520\ \mathrm{nm}
&=520\ \mathrm{nm}
\left(\frac{1\ \mathrm{mm}}{10^6\ \mathrm{nm}}\right)
=0.000520\ \mathrm{mm},\\
1.80\ \mathrm{m}
&=1.80\ \mathrm{m}
\left(\frac{1000\ \mathrm{mm}}{1\ \mathrm{m}}\right)
=1800\ \mathrm{mm}.
\end{aligned}
$$

Each conversion factor equals $1$ physically, and its orientation makes the unwanted unit cancel.

Then the units cancel directly to millimeters:

$$
a
=\frac{(0.000520\ \mathrm{mm})(1800\ \mathrm{mm})}{4.50\ \mathrm{mm}}
=0.208\ \mathrm{mm}.
$$

The units provide an immediate check:

$$
[a]=\frac{(\mathrm{mm})(\mathrm{mm})}{\mathrm{mm}}=\mathrm{mm}.
$$

Using meters for all three lengths gives the same result after converting the final answer to millimeters. A second check is the inverse trend: with $\lambda$ and $L$ fixed, a larger measured spacing must produce a smaller value of $a$.

```quiz
type: radio
id: m6-2-p1-units
content: |-
  A laser has $\lambda=600\ \mathrm{nm}$. Adjacent minima are $4.00\ \mathrm{mm}$ apart on a screen $1.20\ \mathrm{m}$ away. What is the slit width in millimeters?
options:
- id: m6-2-p1-units-a
  content: |-
    $0.180\ \mathrm{mm}$
  correct: true
  feedback: |-
    Use one unit system: $600\ \mathrm{nm}=0.000600\ \mathrm{mm}$ and $1.20\ \mathrm{m}=1200\ \mathrm{mm}$. Then $a=(0.000600)(1200)/4.00=0.180\ \mathrm{mm}$.
- id: m6-2-p1-units-b
  content: |-
    $1.80\times10^{-4}\ \mathrm{mm}$
  feedback: |-
    $1.80\times10^{-4}$ is the numerical width in meters, not millimeters. Since $1\ \mathrm{m}=1000\ \mathrm{mm}$, the converted result is $0.180\ \mathrm{mm}$.
- id: m6-2-p1-units-c
  content: |-
    $180\ \mathrm{mm}$
  feedback: |-
    This results from treating $600\ \mathrm{nm}$ as $0.600\ \mathrm{mm}$. A nanometer is $10^{-6}$ millimeters, so $600\ \mathrm{nm}=0.000600\ \mathrm{mm}$ and the width is $0.180\ \mathrm{mm}$.
- id: m6-2-p1-units-d
  content: |-
    $1.80\times10^5\ \mathrm{mm}$
  feedback: |-
    This treats the numerical value $600$ as though it were already in millimeters. The wavelength must first become $0.000600\ \mathrm{mm}$; otherwise the result is too large by a factor of $10^6$.
- id: m6-2-p1-units-e
  content: |-
    $2.00\times10^{-6}\ \mathrm{mm}$
  feedback: |-
    This comes from using $\lambda\Delta y/L$, which divides by the screen distance instead of multiplying by it. The minima relation requires $a=\lambda L/\Delta y$, producing $0.180\ \mathrm{mm}$.
```

---

<a id="distinguish-adjacent-minima-from-the-central-width"></a>
## Distinguish Adjacent Minima from the Central Width

**Example:** The distance from the first minimum on the left to the first minimum on the right is $10.0\ \mathrm{mm}$. If $\lambda=500\ \mathrm{nm}$ and $L=1.00\ \mathrm{m}$, find $a$.

**Explanation**

The measured $10.0\ \mathrm{mm}$ spans the whole central maximum. It is twice the one-sided first-minimum distance and twice an adjacent-minimum spacing:

$$
W_{\text{central}}=2\Delta y.
$$

This is another gap-counting problem: traveling from the left first minimum to the right first minimum crosses two one-sided gaps, one on each side of the center.

Therefore,

$$
a=\frac{\lambda L}{W_{\text{central}}/2}
=\frac{2\lambda L}{W_{\text{central}}}
=0.100\ \mathrm{mm}.
$$

Do not introduce this factor of $2$ when the prompt already gives the distance between the first and second minima on the same side.

```quiz
type: radio
id: m6-2-p1-central-width
content: |-
  For $\lambda=650\ \mathrm{nm}$ and $L=1.50\ \mathrm{m}$, the two first minima on opposite sides of the center are $6.50\ \mathrm{mm}$ apart. What is the slit width?
options:
- id: m6-2-p1-central-width-a
  content: |-
    $0.300\ \mathrm{mm}$
  correct: true
  feedback: |-
    The given distance is the full central width, so $\Delta y=6.50/2=3.25\ \mathrm{mm}$. Thus $a=\lambda L/\Delta y=2\lambda L/W_{\text{central}}=0.300\ \mathrm{mm}$.
- id: m6-2-p1-central-width-b
  content: |-
    $0.150\ \mathrm{mm}$
  feedback: |-
    This treats the full distance between the two first minima as one adjacent spacing. That span crosses both sides of the center, so it equals $2\Delta y$; halving it gives $a=0.300\ \mathrm{mm}$.
- id: m6-2-p1-central-width-c
  content: |-
    $0.600\ \mathrm{mm}$
  feedback: |-
    This applies the central-width factor twice. Either halve $W_{\text{central}}$ and use $a=\lambda L/\Delta y$, or use $a=2\lambda L/W_{\text{central}}$, but not both.
- id: m6-2-p1-central-width-d
  content: |-
    $3.00\times10^{-4}\ \mathrm{mm}$
  feedback: |-
    $3.00\times10^{-4}$ is the numerical value in meters. Converting meters to millimeters multiplies by $1000$, so the requested width is $0.300\ \mathrm{mm}$.
- id: m6-2-p1-central-width-e
  content: |-
    $3.33\ \mathrm{mm}$
  feedback: |-
    This inverts the calculated slit width. Width follows $a=2\lambda L/W_{\text{central}}$; taking the reciprocal changes both the dimensions and the physical inverse relationship.
```

---

<a id="summary"></a>
## Summary

- Cue: the prompt gives two neighboring dark minima in a small-angle single-slit pattern.
- If positions are given, compute $\Delta y=|y_{m+1}-y_m|$.
- If the minima are not adjacent, divide their total separation by the number of order gaps, $|n-m|$.
- Use $\Delta y\approx\lambda L/a$, then isolate $a\approx\lambda L/\Delta y$.
- Convert $\lambda$, $L$, and $\Delta y$ to one length unit before substituting, orienting each conversion factor so unwanted units cancel.
- Check dimensions: length times length divided by length must leave a length for $a$.
- Check the trend: wider fringe spacing means a narrower slit.
- Main trap: the full central-maximum width is $2\Delta y$, but the spacing between the first and second minima on one side is already $\Delta y$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 4 Study Guide](../../../M7/2026-08-13-Q-4/Study-Guide.md)
Next: [Finding Slit Width from the Central Diffraction Maximum](../../2026-08-09-HW-9/Lessons/Problem-2.md)

Study guide index: 10/11

---

<!-- lesson-nav:end -->
