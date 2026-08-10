# Fitting More Double-Slit Fringes on a Fixed Screen

<!--
lesson-id: 212-M6-015
topic-code: MTH212.M6.15
-->
## Table of Contents

- [Introduction](#introduction)
- [Translate Fringe Count Into Fringe Spacing](#translate-fringe-count-into-fringe-spacing)
- [Follow a Frequency Change Through Wavelength](#follow-a-frequency-change-through-wavelength)
- [Read the Geometry Factors](#read-the-geometry-factors)
- [Combine Changes With Scale Factors](#combine-changes-with-scale-factors)
- [Summary](#summary)

## Prerequisites

- Recognize direct and inverse dependence in a formula.
- Use the wave relation $c=f\lambda$ in a fixed medium.
- Know the small-angle double-slit fringe-spacing relation $\Delta y\approx \lambda L/d$.

---

<a id="introduction"></a>
## Introduction

When the screen width is fixed, a question about fitting **more bright fringes** is really a question about making the neighboring-fringe spacing $\Delta y$ **smaller**. If the usable screen width is $W$, then the number of fringe spacings that fit is approximately proportional to

$$
N\propto \frac{W}{\Delta y}.
$$

For a double slit at small angles,

$$
\Delta y\approx \frac{\lambda L}{d},
$$

where $\lambda$ is the wavelength, $L$ is the slit-to-screen distance, and $d$ is the slit separation. With $W$ and the wave speed $c$ fixed,

$$
N\propto \frac{1}{\Delta y}
\propto \frac{d}{\lambda L}
=\frac{fd}{cL}.
$$

This last form gives the whole decision rule: increasing $f$ or $d$ tends to fit more fringes, while increasing $L$ tends to fit fewer.

The actual count is an integer and can differ by one when a screen edge passes through a maximum. That endpoint detail does not change any of the increase/decrease conclusions below.

---

<a id="translate-fringe-count-into-fringe-spacing"></a>
## Translate Fringe Count Into Fringe Spacing

**Example:** Two interference patterns are shown on screens of the same width. Pattern A has neighboring bright fringes $6\ \mathrm{mm}$ apart, while pattern B has neighboring bright fringes $10\ \mathrm{mm}$ apart. Which screen fits more bright fringes?

**Explanation**

The screen widths are the same, so compare how much width each fringe interval uses. Pattern A uses only $6\ \mathrm{mm}$ per interval, while pattern B uses $10\ \mathrm{mm}$. The smaller spacing packs the fringes more densely, so pattern A fits more bright fringes.

```quiz
type: radio
id: p5-spacing-count
shuffle: true
content: |-
  Two double-slit patterns occupy screens of the same width. Pattern P has fringe spacing $4\ \mathrm{mm}$, and pattern Q has fringe spacing $8\ \mathrm{mm}$. Which statement is correct?
options:
- id: p5-spacing-count-a
  content: |-
    Pattern P fits more bright fringes.
  correct: true
  feedback: |-
    On a fixed-width screen, fringe count is inversely related to neighboring-fringe spacing. Pattern P uses half as much width per fringe interval, so it fits about twice as many intervals and therefore more bright fringes.
- id: p5-spacing-count-b
  content: |-
    Pattern Q fits more bright fringes.
  feedback: |-
    The larger $8\ \mathrm{mm}$ spacing spreads neighboring maxima farther apart; it does not pack them more tightly. Because the screen width is fixed, pattern Q fits fewer bright fringes than the $4\ \mathrm{mm}$ pattern.
- id: p5-spacing-count-c
  content: |-
    The two patterns fit the same number of bright fringes.
  feedback: |-
    Equal counts on equal-width screens would require equal spacing, apart from endpoint effects. Here Q's spacing is twice P's, so their fringe densities are not equal.
- id: p5-spacing-count-d
  content: |-
    The fringe brightness is needed before the count can be compared.
  feedback: |-
    Brightness controls how intense a maximum appears, whereas spacing controls how many maxima fit across a fixed width. The stated $4\ \mathrm{mm}$ and $8\ \mathrm{mm}$ spacings are enough to compare the counts.
```

---

<a id="follow-a-frequency-change-through-wavelength"></a>
## Follow a Frequency Change Through Wavelength

**Example:** The light frequency doubles while $d$, $L$, the medium, and the screen width remain fixed. How does the approximate fringe count change?

**Explanation**

Frequency does not appear directly in $\Delta y\approx \lambda L/d$, so first use

$$
\lambda=\frac{c}{f}.
$$

Doubling $f$ halves $\lambda$. That halves $\Delta y$, and halving the spacing lets approximately twice as many bright fringes fit on the fixed-width screen. Equivalently, $N\propto f$ under these fixed conditions.

```quiz
type: radio
id: p5-frequency-factor
shuffle: true
content: |-
  The light frequency is reduced to $\tfrac{3}{4}$ of its original value. The medium, slit separation, slit-to-screen distance, and screen width stay fixed. What happens to the approximate number of bright fringes that fit?
options:
- id: p5-frequency-factor-a
  content: |-
    It becomes $\tfrac{3}{4}$ of the original count.
  correct: true
  feedback: |-
    In a fixed medium, $\lambda=c/f$, and a fixed-width fringe count satisfies $N\propto 1/\lambda\propto f$. Multiplying the frequency by $3/4$ therefore multiplies the approximate fringe count by $3/4$.
- id: p5-frequency-factor-b
  content: |-
    It becomes $\tfrac{4}{3}$ of the original count.
  feedback: |-
    The factor $4/3$ correctly describes the wavelength change, since wavelength is inverse to frequency. Fringe count is inverse to wavelength, however, so it changes in the same direction as frequency and becomes $3/4$ of its original value.
- id: p5-frequency-factor-c
  content: |-
    It becomes $\tfrac{9}{16}$ of the original count.
  feedback: |-
    No square law applies to double-slit fringe count here. Because $N\propto f$ when the other quantities are fixed, the frequency factor $3/4$ enters once, not as $(3/4)^2$.
- id: p5-frequency-factor-d
  content: |-
    It stays unchanged.
  feedback: |-
    Changing frequency changes the wavelength through $\lambda=c/f$. The reduced frequency increases the wavelength and the fringe spacing, so fewer fringes fit; the count does not remain fixed.
```

---

<a id="read-the-geometry-factors"></a>
## Read the Geometry Factors

**Example:** The slit separation increases from $d$ to $\tfrac{3}{2}d$, while $\lambda$, $L$, and the screen width stay fixed. How does the approximate fringe count change?

**Explanation**

Slit separation is in the denominator of the spacing formula:

$$
\Delta y\approx \frac{\lambda L}{d}.
$$

Multiplying $d$ by $3/2$ multiplies $\Delta y$ by $2/3$. Because count is inverse to spacing, the approximate count is multiplied by $3/2$. A larger slit separation makes the fringes closer together.

Screen distance acts in the opposite direction. Since $L$ is in the numerator of $\Delta y$, increasing $L$ spreads the fringes farther apart and fits fewer on the same screen.

```quiz
type: radio
id: p5-screen-distance
shuffle: true
content: |-
  The slit-to-screen distance is doubled while the wavelength, slit separation, and screen width stay fixed. What happens to the approximate number of bright fringes that fit?
options:
- id: p5-screen-distance-a
  content: |-
    It is halved.
  correct: true
  feedback: |-
    Fringe spacing is directly proportional to screen distance: $\Delta y\propto L$. Doubling $L$ doubles the spacing, and a fixed screen then fits about half as many fringe intervals, so the approximate fringe count is halved.
- id: p5-screen-distance-b
  content: |-
    It doubles.
  feedback: |-
    A more distant screen makes each angular separation occupy more linear distance, so the fringes spread out rather than crowd together. Doubling $L$ doubles $\Delta y$ and therefore halves, rather than doubles, the approximate count.
- id: p5-screen-distance-c
  content: |-
    It stays unchanged.
  feedback: |-
    The angular locations are set by interference, but the question asks how many fit across a screen of fixed linear width. Increasing $L$ increases the linear spacing $\Delta y\approx\lambda L/d$, so the count decreases.
- id: p5-screen-distance-d
  content: |-
    It is reduced to one fourth.
  feedback: |-
    The double-slit spacing is linear in $L$, not proportional to $L^2$. Doubling $L$ therefore doubles the spacing and gives a count factor of $1/2$, not $1/4$.
```

---

<a id="combine-changes-with-scale-factors"></a>
## Combine Changes With Scale Factors

After the one-factor cases are clear, collect their directions in one map:

| Quantity increased | Effect on $\Delta y$ | Effect on fringe count |
| --- | --- | --- |
| $f$ | Decreases because $\lambda=c/f$ decreases | Increases |
| $d$ | Decreases because $d$ is in the denominator | Increases |
| $L$ | Increases because $L$ is in the numerator | Decreases |

**Example:** The frequency is halved, the slit separation is tripled, and the screen distance is multiplied by $3/2$. What happens to the approximate fringe count?

**Explanation**

In the same medium and on the same screen,

$$
N\propto \frac{fd}{L}.
$$

Therefore,

$$
\frac{N'}{N}
=\frac{f'}{f}\frac{d'}{d}\frac{L}{L'}
=\left(\frac{1}{2}\right)(3)\left(\frac{2}{3}\right)
=1.
$$

The changes cancel, so the approximate count stays the same. For a question with several proposed changes, apply this dependence to each change independently before choosing the set that contains all and only the changes that work.

```quiz
type: radio
id: p5-source-check
shuffle: true
content: |-
  **Question 5**

  A double-slit interference pattern is displayed on a screen of fixed width. Which option lists **all and only** the changes that would increase the number of bright fringes that fit on the screen?
options:
- id: p5-source-check-a
  content: |-
    Increasing the frequency of the light and increasing the slit separation
  correct: true
  feedback: |-
    Increasing $f$ decreases $\lambda=c/f$, and increasing $d$ places a larger quantity in the denominator of $\Delta y\approx\lambda L/d$. Each change therefore decreases the spacing, so each increases the number of bright fringes on the fixed-width screen.
- id: p5-source-check-b
  content: |-
    Decreasing the frequency of the light and increasing the slit separation
  feedback: |-
    Increasing $d$ does decrease the fringe spacing, but decreasing $f$ increases $\lambda=c/f$ and therefore increases the spacing. Because decreasing frequency would fit fewer fringes, this pair does not contain only count-increasing changes.
- id: p5-source-check-c
  content: |-
    Increasing the frequency of the light and increasing the distance from the slits to the screen
  feedback: |-
    Increasing frequency does reduce the spacing through $\lambda=c/f$, but increasing $L$ enlarges $\Delta y\approx\lambda L/d$. A greater slit-to-screen distance spreads the fringes out, so this pair includes a change that fits fewer fringes.
- id: p5-source-check-d
  content: |-
    Decreasing the frequency of the light and increasing the distance from the slits to the screen
  feedback: |-
    Both changes enlarge the fringe spacing: decreasing $f$ increases the wavelength, and increasing $L$ directly increases $\Delta y$. Wider spacing fits fewer bright fringes, so neither change belongs in the requested set.
```

---

<a id="summary"></a>
## Summary

When a fixed-width screen must fit more bright fringes:

1. Translate **more fringes** into **smaller $\Delta y$**.
2. Use $\Delta y\approx\lambda L/d$.
3. If frequency changes, use $\lambda=c/f$ before deciding the direction.
4. Under fixed-medium conditions, remember $N\propto fd/L$: increasing $f$ or $d$ increases the count, while increasing $L$ decreases it.
5. When several changes are proposed, test every one independently before choosing the complete set.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
