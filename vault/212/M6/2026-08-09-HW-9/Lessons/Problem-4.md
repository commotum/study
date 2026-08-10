# Predicting Changes in Double-Slit Fringe Spacing

<!--
lesson-id: 212-M6-014
topic-code: MTH212.M6.14
-->
## Table of Contents

- [Introduction](#introduction)
- [Read the Fringe-Spacing Formula](#read-the-fringe-spacing-formula)
- [Translate a Frequency Change](#translate-a-frequency-change)
- [Change the Screen Distance](#change-the-screen-distance)
- [Change the Slit Separation](#change-the-slit-separation)
- [Combine Several Changes](#combine-several-changes)
- [Summary](#summary)

## Prerequisites

- Recognize the double-slit bright-maximum relation $y_m\approx m\lambda L/d$ in the far-screen, small-angle approximation.
- Use the wave relation $v=f\lambda$ and treat $v$ as constant when the medium does not change.
- Compare quantities with multiplicative factors such as “twice” or “one-half.”

---

<a id="introduction"></a>
## Introduction

When a question asks about the distance between **neighboring bright fringes** in a double-slit pattern, use the fringe-spacing formula

$$
\Delta y\approx \frac{\lambda L}{d},
$$

where

- $\Delta y$ is the distance between neighboring bright fringes,
- $\lambda$ is the wavelength,
- $L$ is the distance from the slits to the screen, and
- $d$ is the separation between the slits.

The formula is a direction map. A quantity in the numerator has a **direct** effect: increasing it increases $\Delta y$. A quantity in the denominator has an **inverse** effect: increasing it decreases $\Delta y$.

Frequency needs one extra translation. In a fixed medium,

$$
\lambda=\frac{v}{f},
$$

so lowering $f$ increases $\lambda$ and therefore increases the fringe spacing. The main trap is to treat frequency as though it appears directly in the numerator of the spacing formula.

Substituting $\lambda=v/f$ gives the equivalent fixed-medium form

$$
\Delta y\approx\frac{vL}{fd}.
$$

This version makes the direction check immediate: $L$ is direct, while both $f$ and $d$ are inverse.

---

<a id="read-the-fringe-spacing-formula"></a>
## Read the Fringe-Spacing Formula

**Example:** The wavelength changes from $500\ \mathrm{nm}$ to $600\ \mathrm{nm}$ while $L$ and $d$ remain fixed. How does the fringe spacing change?

**Explanation**

Wavelength is in the numerator, so compare the new and old spacings with

$$
\frac{\Delta y'}{\Delta y}
=\frac{\lambda'}{\lambda}
=\frac{600}{500}
=1.20.
$$

The new spacing is $1.20$ times the old spacing, so the bright fringes are $20\%$ farther apart.

```quiz
type: radio
id: problem-4-q1
content: |-
  The wavelength is doubled while the screen distance and slit separation remain fixed. What happens to the distance between neighboring bright fringes?
options:
- id: problem-4-q1-a
  content: |-
    It doubles.
  correct: true
  feedback: |-
    Fringe spacing is directly proportional to wavelength because $\lambda$ is in the numerator of $\Delta y\approx\lambda L/d$. With $L$ and $d$ fixed, doubling $\lambda$ doubles $\Delta y$.
- id: problem-4-q1-b
  content: |-
    It is cut in half.
  feedback: |-
    Halving would describe an inverse dependence, but wavelength is in the numerator rather than the denominator. With the other quantities fixed, a factor of $2$ in $\lambda$ produces the same factor of $2$ in $\Delta y$.
- id: problem-4-q1-c
  content: |-
    It does not change.
  feedback: |-
    Wavelength determines the path-difference scale of the interference pattern, so it is not irrelevant to fringe spacing. The formula $\Delta y\approx\lambda L/d$ shows that doubling $\lambda$ doubles the spacing.
- id: problem-4-q1-d
  content: |-
    It becomes four times as large.
  feedback: |-
    A factor of $4$ would follow from a squared wavelength dependence. Here $\lambda$ appears only to the first power, so doubling it changes $\Delta y$ by a factor of $2$, not $2^2$.
```

---

<a id="translate-a-frequency-change"></a>
## Translate a Frequency Change

**Example:** In the same medium, the light frequency decreases from $6.0\times10^{14}\ \mathrm{Hz}$ to $4.5\times10^{14}\ \mathrm{Hz}$. The geometry does not change. How does the fringe spacing change?

**Explanation**

Frequency is inversely related to wavelength:

$$
\lambda=\frac{v}{f}.
$$

Because $v$ is fixed, the wavelength factor is

$$
\frac{\lambda'}{\lambda}
=\frac{v/f'}{v/f}
=\frac{f}{f'}
=\frac{6.0}{4.5}
=\frac43.
$$

Fringe spacing is directly proportional to wavelength, so $\Delta y$ also grows by a factor of $4/3$. Lower frequency means longer wavelength and wider fringes.

```quiz
type: radio
id: problem-4-q2
content: |-
  The frequency of the light is doubled without changing the medium or the double-slit geometry. What happens to the fringe spacing?
options:
- id: problem-4-q2-a
  content: |-
    It doubles.
  feedback: |-
    This treats frequency as though it were wavelength. In a fixed medium, $\lambda=v/f$, so doubling $f$ halves $\lambda$; since $\Delta y\propto\lambda$, the spacing is halved.
- id: problem-4-q2-b
  content: |-
    It is cut in half.
  correct: true
  feedback: |-
    A fixed wave speed gives $\lambda=v/f$, so doubling frequency halves wavelength. Because $\Delta y\approx\lambda L/d$, the distance between neighboring bright fringes is also cut in half.
- id: problem-4-q2-c
  content: |-
    It becomes four times as large.
  feedback: |-
    Neither relation contains a squared frequency factor. Frequency first changes wavelength inversely, $\lambda\propto1/f$, and spacing then follows wavelength directly, so doubling $f$ makes $\Delta y$ one-half as large.
- id: problem-4-q2-d
  content: |-
    It does not change.
  feedback: |-
    The geometry stays fixed, but the interference scale also depends on wavelength. Doubling $f$ in the same medium halves $\lambda$, which halves $\Delta y$.
```

---

<a id="change-the-screen-distance"></a>
## Change the Screen Distance

**Example:** A screen is moved from $L=1.5\ \mathrm{m}$ to $L'=2.4\ \mathrm{m}$ while the light and slit separation stay fixed. Find the spacing factor.

**Explanation**

Screen distance is in the numerator, so

$$
\frac{\Delta y'}{\Delta y}
=\frac{L'}{L}
=\frac{2.4}{1.5}
=1.6.
$$

The pattern spreads across a longer propagation distance. The new neighboring-fringe spacing is $1.6$ times the old spacing.

```quiz
type: radio
id: problem-4-q3
content: |-
  The screen is moved from $2.0\ \mathrm{m}$ to $3.0\ \mathrm{m}$ from the slits. Wavelength and slit separation stay fixed. What is the new fringe spacing compared with the old spacing?
options:
- id: problem-4-q3-a
  content: |-
    $\Delta y'=1.5\Delta y$
  correct: true
  feedback: |-
    Fringe spacing is directly proportional to screen distance. The distance factor is $L'/L=3.0/2.0=1.5$, so $\Delta y'=1.5\Delta y$.
- id: problem-4-q3-b
  content: |-
    $\Delta y'=\dfrac23\Delta y$
  feedback: |-
    The factor $2/3$ reverses the screen-distance ratio as though $L$ were in the denominator. Since $L$ is in the numerator of $\Delta y\approx\lambda L/d$, use $L'/L=3/2$, not $L/L'$.
- id: problem-4-q3-c
  content: |-
    $\Delta y'=\Delta y$
  feedback: |-
    The screen distance controls how far a fixed angular separation spreads across the screen. Increasing $L$ from $2.0$ m to $3.0$ m multiplies the linear spacing by $3/2$, so it cannot remain unchanged.
- id: problem-4-q3-d
  content: |-
    $\Delta y'=2.25\Delta y$
  feedback: |-
    The factor $2.25=(3/2)^2$ incorrectly squares the distance ratio. Screen distance appears to the first power, so the correct factor is $3/2=1.5$.
```

---

<a id="change-the-slit-separation"></a>
## Change the Slit Separation

**Example:** The slit separation increases from $d=0.20\ \mathrm{mm}$ to $d'=0.50\ \mathrm{mm}$ while $\lambda$ and $L$ stay fixed. How does the spacing change?

**Explanation**

Slit separation is in the denominator. Therefore the new-to-old spacing ratio uses the **old** separation over the **new** separation:

$$
\frac{\Delta y'}{\Delta y}
=\frac{d}{d'}
=\frac{0.20}{0.50}
=0.40.
$$

The new fringe spacing is $40\%$ of the old spacing. Increasing $d$ makes the neighboring bright fringes closer together.

```quiz
type: radio
id: problem-4-q4
content: |-
  The slit separation is reduced to one-half its original value while wavelength and screen distance remain fixed. What happens to the fringe spacing?
options:
- id: problem-4-q4-a
  content: |-
    It is cut in half.
  feedback: |-
    This follows the change in $d$ directly, but $d$ is in the denominator. Replacing $d$ by $d/2$ gives $\Delta y'=\lambda L/(d/2)=2\lambda L/d$, so the spacing doubles.
- id: problem-4-q4-b
  content: |-
    It doubles.
  correct: true
  feedback: |-
    Fringe spacing varies inversely with slit separation. Halving the denominator in $\Delta y\approx\lambda L/d$ doubles the result, so neighboring bright fringes become twice as far apart.
- id: problem-4-q4-c
  content: |-
    It becomes four times as large.
  feedback: |-
    A factor of $4$ would require an inverse-square dependence on $d$. The formula contains $d$ only to the first power, so halving $d$ increases the spacing by a factor of $2$.
- id: problem-4-q4-d
  content: |-
    It does not change.
  feedback: |-
    Slit separation sets how quickly the path difference changes with angle, so it directly affects the pattern scale. Because $d$ is halved in the denominator, $\Delta y$ doubles.
```

---

<a id="combine-several-changes"></a>
## Combine Several Changes

**Example:** The frequency is halved, the screen distance is multiplied by $3/2$, and the slit separation is tripled. The medium stays the same. What is the net change in fringe spacing?

**Explanation**

For simultaneous changes, compare the new and old formulas:

$$
\frac{\Delta y'}{\Delta y}
=\frac{\lambda'}{\lambda}
\frac{L'}{L}
\frac{d}{d'}.
$$

When the medium is fixed, replace the wavelength ratio by $\lambda'/\lambda=f/f'$:

$$
\frac{\Delta y'}{\Delta y}
=\frac{f}{f'}
\frac{L'}{L}
\frac{d}{d'}.
$$

Halving frequency doubles wavelength, so

$$
\frac{\Delta y'}{\Delta y}
=(2)\left(\frac32\right)\left(\frac13\right)
=1.
$$

The changes cancel, and the fringe spacing stays the same. This ratio method also provides a compact self-check: numerator factors widen the pattern, while the reciprocal slit-separation factor narrows it.

```quiz
type: radio
id: problem-4-q5
shuffle: true
content: |-
  Which pair contains two changes that would each increase the distance between neighboring bright fringes in a double-slit interference pattern?
options:
- id: problem-4-q5-a
  content: |-
    Lowering the frequency of the light and increasing the distance from the slits to the screen
  correct: true
  feedback: |-
    In a fixed medium, lowering $f$ increases $\lambda=v/f$, and wavelength is in the numerator of $\Delta y\approx\lambda L/d$. Screen distance $L$ is also in the numerator, so both changes independently increase the neighboring-fringe spacing.
- id: problem-4-q5-b
  content: |-
    Increasing the frequency of the light and increasing the distance from the slits to the screen
  feedback: |-
    Increasing $L$ does widen the pattern, but increasing $f$ decreases $\lambda=v/f$ and therefore narrows it. Because the pair does not contain two individually spacing-increasing changes, it does not satisfy the question.
- id: problem-4-q5-c
  content: |-
    Lowering the frequency of the light and increasing the separation between the slits
  feedback: |-
    Lowering frequency lengthens the wavelength and widens the pattern, but increasing slit separation $d$ reduces $\Delta y\approx\lambda L/d$. The second change acts in the opposite direction, so both members of this pair do not increase spacing.
- id: problem-4-q5-d
  content: |-
    Increasing the frequency of the light and increasing the separation between the slits
  feedback: |-
    Both changes narrow the pattern: increasing $f$ shortens $\lambda=v/f$, and increasing denominator $d$ further decreases $\Delta y\approx\lambda L/d$. This pair makes neighboring fringes closer together rather than farther apart.
```

---

<a id="summary"></a>
## Summary

For neighboring bright fringes, start with

$$
\Delta y\approx\frac{\lambda L}{d}.
$$

- A larger wavelength $\lambda$ makes the spacing larger.
- A larger screen distance $L$ makes the spacing larger.
- A larger slit separation $d$ makes the spacing smaller.
- In a fixed medium, $\lambda=v/f$, so lower frequency means longer wavelength and larger spacing.

For several changes at once, use

$$
\frac{\Delta y'}{\Delta y}
=\frac{\lambda'}{\lambda}
\frac{L'}{L}
\frac{d}{d'}.
$$

The main trap is reversing an inverse relationship: frequency is inverse to wavelength, and slit separation is inverse to fringe spacing.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 4 Study Guide](../../../M7/2026-08-13-Q-4/Study-Guide.md)
Next: [Finding Wavelength From a Double-Slit Intensity Graph](../../2026-08-05-M6-1/Lessons/Problem-4.md)

Study guide index: 05/11

---

<!-- lesson-nav:end -->
