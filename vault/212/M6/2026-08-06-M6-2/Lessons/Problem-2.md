# Finding Diffraction-Grating Line Density from Symmetric Fringes

<!--
lesson-id: 212-M6-007
topic-code: MTH212.M6.07
-->
## Table of Contents

- [Introduction](#introduction)
- [Halve the Symmetric Fringe Separation](#halve-the-symmetric-fringe-separation)
- [Find the Angle from Screen Geometry](#find-the-angle-from-screen-geometry)
- [Convert Grating Spacing to Line Density](#convert-grating-spacing-to-line-density)
- [Apply the Full Chain](#apply-the-full-chain)
- [Summary](#summary)

## Prerequisites

- Recognize opposite-order diffraction maxima as symmetric about the central maximum.
- Use right-triangle trigonometry, especially $\tan\theta=y/L$.
- Use the diffraction-grating maximum condition $d\sin\theta=m\lambda$.
- Convert among nanometers, meters, and millimeters.

---

<a id="introduction"></a>
## Introduction

When a problem gives the distance **between** the $+m$ and $-m$ bright fringes but asks for the grating's slits per millimeter, the measured distance is not the $y$ used in the screen triangle. First halve the symmetric separation to get the distance from the center to one fringe. Then find the diffraction angle, solve the grating equation for the slit spacing $d$, and take its reciprocal to obtain the line density.

The full chain is

$$
y=\frac{S}{2},
\qquad
\theta=\tan^{-1}\!\left(\frac{y}{L}\right),
\qquad
d=\frac{m\lambda}{\sin\theta},
\qquad
N=\frac{1}{d}=\frac{\sin\theta}{m\lambda},
$$

where $S$ is the separation between the two opposite-order fringes. The spacing $d$ is a length per slit, while its reciprocal $N$ is a number of slits per unit length. Keeping those reciprocal roles distinct prevents a correct value of $d$ from being reported as the requested density.

---

<a id="halve-the-symmetric-fringe-separation"></a>
## Halve the Symmetric Fringe Separation

**Example:** The distance from the $m=-1$ bright fringe to the $m=+1$ bright fringe is $1.20\ \mathrm{m}$. Find the distance from the central maximum to either first-order fringe.

**Explanation**

The central maximum lies halfway between the two first-order fringes. Therefore,

$$
y_1=\frac{S}{2}=\frac{1.20\ \mathrm{m}}{2}=0.600\ \mathrm{m}.
$$

The order label tells which pair is being measured; it does not remove the factor of two created by the left-right symmetry.

```quiz
type: radio
id: p2-symmetry-q1
content: |-
  The distance between the $m=-1$ and $m=+1$ bright fringes is $1.50\ \mathrm{m}$. What one-sided displacement $y_1$ belongs in the screen triangle?
options:
- id: p2-symmetry-q1-a
  content: |-
    $0.375\ \mathrm{m}$
  feedback: |-
    This halves the measured separation twice. The central maximum divides the full $1.50\ \mathrm{m}$ separation into two equal one-sided distances, so only one division by two is needed.
- id: p2-symmetry-q1-b
  content: |-
    $0.750\ \mathrm{m}$
  correct: true
  feedback: |-
    Opposite-order fringes are equally far from the center, so their full separation is $S=2y_1$. Thus $y_1=S/2=1.50/2=0.750\ \mathrm{m}$.
- id: p2-symmetry-q1-c
  content: |-
    $1.50\ \mathrm{m}$
  feedback: |-
    This is the full distance from the left first-order fringe to the right first-order fringe. The screen triangle uses the distance from the center to just one fringe, which is half as large.
- id: p2-symmetry-q1-d
  content: |-
    $3.00\ \mathrm{m}$
  feedback: |-
    Doubling would convert a one-sided displacement into a full symmetric separation. Here the full separation is already given, so it must be halved to obtain $y_1$.
```

---

<a id="find-the-angle-from-screen-geometry"></a>
## Find the Angle from Screen Geometry

**Example:** A first-order bright fringe is $0.850\ \mathrm{m}$ from the center of a screen that is $2.40\ \mathrm{m}$ from the grating. Find the diffraction angle.

**Explanation**

The screen distance $L$ is adjacent to the diffraction angle and the one-sided displacement $y_1$ is opposite it. Therefore,

$$
\tan\theta_1=\frac{y_1}{L}=\frac{0.850}{2.40},
$$

so

$$
\theta_1=\tan^{-1}\!\left(\frac{0.850}{2.40}\right)=19.502\ldots^\circ.
$$

Use degree mode on the calculator. Keep guard digits for $\theta_1$ because the next step uses $\sin\theta_1$, and round only the final requested density. At this angle, replacing the geometry with the small-angle approximation would noticeably shift that density.

```quiz
type: radio
id: p2-geometry-q1
content: |-
  A first-order fringe is $0.600\ \mathrm{m}$ from the center of a screen located $2.00\ \mathrm{m}$ from the grating. Which expression and angle are correct?
options:
- id: p2-geometry-q1-a
  content: |-
    $\theta_1=\tan^{-1}(0.600/2.00)=16.7^\circ$
  correct: true
  feedback: |-
    In the screen triangle, $y_1$ is opposite the angle and $L$ is adjacent, so $\tan\theta_1=y_1/L=0.300$. Taking the inverse tangent gives $\theta_1=16.7^\circ$.
- id: p2-geometry-q1-b
  content: |-
    $\theta_1=0.600/2.00=0.300^\circ$
  feedback: |-
    The ratio $y_1/L=0.300$ is $\tan\theta_1$, not the angle in degrees. Apply $\tan^{-1}$ to the ratio to obtain $16.7^\circ$.
- id: p2-geometry-q1-c
  content: |-
    $\theta_1=\tan^{-1}(2.00/0.600)=73.3^\circ$
  feedback: |-
    This reverses opposite and adjacent, producing the complementary angle. Relative to the grating's central axis, the opposite side is $y_1$ and the adjacent side is $L$, so the ratio is $0.600/2.00$.
- id: p2-geometry-q1-d
  content: |-
    $\theta_1=\sin^{-1}(0.600/2.00)=17.5^\circ$
  feedback: |-
    The screen distance $L$ is the adjacent side, not the hypotenuse, so $y_1/L$ is a tangent ratio rather than a sine ratio. Use inverse tangent to get $16.7^\circ$.
```

---

<a id="convert-grating-spacing-to-line-density"></a>
## Convert Grating Spacing to Line Density

**Example:** First-order light with wavelength $500\ \mathrm{nm}$ forms a bright fringe at $\theta_1=30.0^\circ$. Find the grating's line density in slits per millimeter.

**Explanation**

For a grating maximum,

$$
d\sin\theta_m=m\lambda.
$$

Line density is the reciprocal of slit spacing. Make the requested quantity $N=1/d$ the subject before inserting numbers:

$$
N=\frac{\sin\theta_m}{m\lambda}.
$$

Using meters first,

$$
N
=\frac{\sin 30.0^\circ}{(1)(500\times10^{-9}\ \mathrm{m})}
=1.00\times10^6\ \mathrm{slits/m}.
$$

Since one meter contains $1000\ \mathrm{mm}$, use a conversion factor whose meter units cancel:

$$
N
=(1.00\times10^6\ \mathrm{slits/m})
\left(\frac{1\ \mathrm{m}}{1000\ \mathrm{mm}}\right)
=1.00\times10^3\ \mathrm{slits/mm}.
$$

The final unit $\mathrm{slits/mm}$ also checks that the reciprocal was taken in the correct direction.

```quiz
type: radio
id: p2-density-q1
content: |-
  First-order light with wavelength $600\ \mathrm{nm}$ forms a grating maximum at $20.0^\circ$. What is the grating's line density?
options:
- id: p2-density-q1-a
  content: |-
    $570\ \mathrm{slits/mm}$
  correct: true
  feedback: |-
    A grating maximum gives $N=1/d=\sin\theta_1/\lambda$. Substitution gives $5.70\times10^5\ \mathrm{slits/m}$, and dividing by $1000\ \mathrm{mm/m}$ gives $570\ \mathrm{slits/mm}$.
- id: p2-density-q1-b
  content: |-
    $5.70\times10^5\ \mathrm{slits/mm}$
  feedback: |-
    The numerical value $5.70\times10^5$ is the density per meter. A millimeter is a smaller length interval, so the number of slits per millimeter is smaller by a factor of $1000$, giving $570\ \mathrm{slits/mm}$.
- id: p2-density-q1-c
  content: |-
    $1.75\times10^{-3}\ \mathrm{slits/mm}$
  feedback: |-
    The value $1.75\times10^{-3}\ \mathrm{mm}$ is the slit spacing $d=\lambda/\sin\theta_1$, not a line density. Taking its reciprocal gives $N=1/d=570\ \mathrm{slits/mm}$.
- id: p2-density-q1-d
  content: |-
    $1.67\times10^3\ \mathrm{slits/mm}$
  feedback: |-
    This is $1/\lambda$ after expressing the wavelength in millimeters, which would correspond to replacing $\sin20.0^\circ$ by $1$. The measured angle contributes the factor $\sin20.0^\circ=0.342$, reducing the density to $570\ \mathrm{slits/mm}$.
```

---

<a id="apply-the-full-chain"></a>
## Apply the Full Chain

**Example:** A helium-neon laser with wavelength $\lambda=633\ \mathrm{nm}$ illuminates a diffraction grating. A screen is $2.4\ \mathrm{m}$ away, and the distance between the two $m=1$ bright fringes is $170\ \mathrm{cm}$. Find the number of slits per millimeter.

**Explanation**

Convert the full separation and halve it:

$$
S=170\ \mathrm{cm}=1.70\ \mathrm{m},
\qquad
y_1=\frac{S}{2}=0.850\ \mathrm{m}.
$$

Use the one-sided displacement in the screen triangle:

$$
\theta_1
=\tan^{-1}\!\left(\frac{0.850}{2.4}\right)
=19.502\ldots^\circ.
$$

Then use $m=1$ in the grating equation and solve directly for line density:

$$
N
=\frac{\sin\theta_1}{m\lambda}
=\frac{\sin(19.502\ldots^\circ)}{(1)(633\times10^{-9}\ \mathrm{m})}
=5.274\ldots\times10^5\ \mathrm{slits/m}.
$$

Convert from slits per meter to slits per millimeter with the units visible:

$$
N
=(5.274\ldots\times10^5\ \mathrm{slits/m})
\left(\frac{1\ \mathrm{m}}{1000\ \mathrm{mm}}\right)
=527.4\ldots\ \mathrm{slits/mm}.
$$

The measured values support two significant figures, so the requested result is

$$
\boxed{N=5.3\times10^2\ \mathrm{slits/mm}},
$$

entered as `530` when the response requires a number only.

```quiz
type: radio
id: p2-full-chain-q1
content: |-
  A $500\ \mathrm{nm}$ laser illuminates a diffraction grating. A screen is $1.50\ \mathrm{m}$ away, and the distance between the $m=-1$ and $m=+1$ bright fringes is $1.00\ \mathrm{m}$. What is the grating's line density to two significant figures?
options:
- id: p2-full-chain-q1-a
  content: |-
    $330\ \mathrm{slits/mm}$
  feedback: |-
    This results from halving the already one-sided displacement a second time. The full $1.00\ \mathrm{m}$ separation gives $y_1=0.500\ \mathrm{m}$ after exactly one division by two.
- id: p2-full-chain-q1-b
  content: |-
    $630\ \mathrm{slits/mm}$
  correct: true
  feedback: |-
    Symmetry gives $y_1=0.500\ \mathrm{m}$, so $\theta_1=\tan^{-1}(0.500/1.50)$ and $\sin\theta_1=0.3162$. Thus $N=\sin\theta_1/\lambda=6.32\times10^5\ \mathrm{m}^{-1}=630\ \mathrm{slits/mm}$ to two significant figures.
- id: p2-full-chain-q1-c
  content: |-
    $670\ \mathrm{slits/mm}$
  feedback: |-
    This uses the small-angle replacement $\sin\theta\approx\tan\theta=y_1/L$. Here the exact geometry gives $\sin\theta_1=0.3162$, not $0.3333$, so the exact density rounds to $630\ \mathrm{slits/mm}$.
- id: p2-full-chain-q1-d
  content: |-
    $1.1\times10^3\ \mathrm{slits/mm}$
  feedback: |-
    This treats the full $1.00\ \mathrm{m}$ fringe-to-fringe separation as the one-sided triangle height. The central maximum lies halfway between the two fringes, so using $y_1=0.500\ \mathrm{m}$ gives $630\ \mathrm{slits/mm}$.
- id: p2-full-chain-q1-e
  content: |-
    $6.3\times10^5\ \mathrm{slits/mm}$
  feedback: |-
    The value $6.3\times10^5$ is the density in slits per meter. Converting to slits per millimeter requires dividing by $1000$, producing $6.3\times10^2\ \mathrm{slits/mm}$.
```

---

<a id="summary"></a>
## Summary

When the measurement runs from the $-m$ fringe to the $+m$ fringe, use this checklist:

1. Convert the full separation $S$ to a one-sided displacement: $y=S/2$.
2. Use exact screen geometry: $\theta=\tan^{-1}(y/L)$.
3. Use the correct fringe order in $d\sin\theta=m\lambda$.
4. Solve for line density: $N=1/d=\sin\theta/(m\lambda)$.
5. Convert the rate so the units cancel: $(\mathrm{slits/m})(1\ \mathrm{m}/1000\ \mathrm{mm})=\mathrm{slits/mm}$.
6. Keep guard digits through the trigonometry and round only the final requested density.

The main trap is using the full symmetric separation as $y$. A second common trap is reporting the slit spacing $d$ when the question asks for its reciprocal, the line density $N$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 4 Study Guide](../../../M7/2026-08-13-Q-4/Study-Guide.md)
Next: [Counting Visible Diffraction-Grating Maxima on a Finite Screen](Problem-3.md)

Study guide index: 08/11

---

<!-- lesson-nav:end -->
