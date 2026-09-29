# Sound Intensity at a New Distance

<!--
lesson-id: 212-M5-025
topic-code: MTH212.M5.25
-->

## Table of Contents

- [Introduction](#introduction)
- [Recognize the Inverse-Square Change](#recognize-the-inverse-square-change)
- [Use the Distance-Ratio Formula](#use-the-distance-ratio-formula)
- [Keep the Ratio Direction Correct](#keep-the-ratio-direction-correct)
- [Match the Number-Only Answer Form](#match-the-number-only-answer-form)
- [Summary](#summary)

## Prerequisites

- Square a whole number or fraction.
- Substitute values into a fraction and simplify.
- Recognize sound intensity units of $\mathrm{W}/\mathrm{m}^2$.

---

<a id="introduction"></a>
## Introduction

For a point source radiating the same power in all directions, the sound spreads over a spherical area proportional to $r^2$. Its intensity therefore follows

$$
I\propto\frac{1}{r^2}.
$$

When the same speaker is measured at two distances, compute the new intensity by multiplying the known intensity by the **square** of the old-distance-to-new-distance ratio:

$$
I_2=I_1\left(\frac{r_1}{r_2}\right)^2.
$$

The cue is a fixed source, one known intensity $I_1$, two distances $r_1$ and $r_2$, and a request for the intensity $I_2$ at the new location.

Before using the law, confirm that the speaker's power has not changed. Then label the known location with subscript $1$ and the new location with subscript $2$. For the same source,

$$
Ir^2=\text{constant},
$$

so $I_1r_1^2=I_2r_2^2$.

---

<a id="recognize-the-inverse-square-change"></a>
## Recognize the Inverse-Square Change

If the distance is multiplied by a factor $k$, the intensity is multiplied by $1/k^2$. In particular:

$$
\text{double the distance}\Longrightarrow\frac{1}{2^2}=\frac14
\text{ of the intensity}.
$$

This gives a fast prediction before any detailed substitution. Moving farther must lower the answer, and a distance factor of $k$ produces an intensity factor of $1/k^2$, not $1/k$.

**Example:** A sound intensity is $320\ \mathrm{W}/\mathrm{m}^2$ at $6.0\ \mathrm{m}$ from a speaker. What is the intensity at $12\ \mathrm{m}$?

**Explanation**

The distance doubles, so the intensity becomes one fourth as large:

$$
I_2=\frac{320\ \mathrm{W}/\mathrm{m}^2}{4}
=80\ \mathrm{W}/\mathrm{m}^2.
$$

```quiz
type: radio
id: problem-2-intensity-q1
content: |-
  A sound intensity is $180\ \mathrm{W}/\mathrm{m}^2$ at $5.0\ \mathrm{m}$ from a point source. What is the intensity at $15\ \mathrm{m}$?
options:
- id: a
  content: |-
    $20\ \mathrm{W}/\mathrm{m}^2$
  correct: true
  feedback: |-
    The distance triples, so the intensity is multiplied by $1/3^2=1/9$: $180/9=20\ \mathrm{W}/\mathrm{m}^2$.
- id: b
  content: |-
    $60\ \mathrm{W}/\mathrm{m}^2$
- id: c
  content: |-
    $180\ \mathrm{W}/\mathrm{m}^2$
- id: d
  content: |-
    $540\ \mathrm{W}/\mathrm{m}^2$
- id: e
  content: |-
    $1620\ \mathrm{W}/\mathrm{m}^2$
```

---

<a id="use-the-distance-ratio-formula"></a>
## Use the Distance-Ratio Formula

The inverse-square law can be written as

$$
I_1r_1^2=I_2r_2^2.
$$

Solving for the requested intensity gives

$$
I_2
=I_1\frac{r_1^2}{r_2^2}
=I_1\left(\frac{r_1}{r_2}\right)^2.
$$

**Example:** The intensity is $162\ \mathrm{W}/\mathrm{m}^2$ at $8.0\ \mathrm{m}$. Find the intensity at $12\ \mathrm{m}$.

**Explanation**

Substitute the old distance in the numerator and the new distance in the denominator:

$$
\begin{aligned}
I_2
&=(162\ \mathrm{W}/\mathrm{m}^2)
\left(\frac{8.0}{12}\right)^2\\
&=(162\ \mathrm{W}/\mathrm{m}^2)
\left(\frac23\right)^2\\
&=(162\ \mathrm{W}/\mathrm{m}^2)\frac49\\
&=72\ \mathrm{W}/\mathrm{m}^2.
\end{aligned}
$$

The exponent applies to the whole fraction:

$$
\left(\frac{r_1}{r_2}\right)^2
=\frac{r_1}{r_2}\cdot\frac{r_1}{r_2}
=\frac{r_1^2}{r_2^2}.
$$

Because the meters in the distance ratio cancel, this factor is unitless; $I_2$ keeps the units $\mathrm{W}/\mathrm{m}^2$ from $I_1$.

```quiz
type: radio
id: problem-2-intensity-q2
content: |-
  A speaker produces an intensity of $200\ \mathrm{W}/\mathrm{m}^2$ at $6.0\ \mathrm{m}$. What intensity is measured at $10\ \mathrm{m}$?
options:
- id: a
  content: |-
    $40\ \mathrm{W}/\mathrm{m}^2$
  feedback: |-
    This does not use the squared distance ratio $({6.0}/{10})^2$.
- id: b
  content: |-
    $72\ \mathrm{W}/\mathrm{m}^2$
  correct: true
  feedback: |-
    $I_2=200(6.0/10)^2=200(0.36)=72\ \mathrm{W}/\mathrm{m}^2$.
- id: c
  content: |-
    $120\ \mathrm{W}/\mathrm{m}^2$
  feedback: |-
    This uses the linear ratio $6.0/10$ instead of squaring it.
- id: d
  content: |-
    $333\ \mathrm{W}/\mathrm{m}^2$
  feedback: |-
    This reverses the ratio and does not square it. Moving farther cannot increase the intensity.
- id: e
  content: |-
    $556\ \mathrm{W}/\mathrm{m}^2$
  feedback: |-
    This squares the reversed ratio. Since the new location is farther away, an increased intensity is impossible.
```

---

<a id="keep-the-ratio-direction-correct"></a>
## Keep the Ratio Direction Correct

The ratio in the formula is always

$$
\frac{\text{distance where the intensity is known}}
{\text{distance where the intensity is wanted}}
=\frac{r_1}{r_2}.
$$

Before calculating, predict whether the answer should rise or fall. Moving farther away must lower the intensity; moving closer must raise it.

A reliable substitution order is:

1. Write the known pair $(I_1,r_1)$.
2. Write the new distance $r_2$.
3. Substitute all three values into $I_2=I_1(r_1/r_2)^2$.
4. Simplify the ratio, square it, and multiply by $I_1$.

**Example:** The intensity is $50\ \mathrm{W}/\mathrm{m}^2$ at $18\ \mathrm{m}$. What is the intensity at $9.0\ \mathrm{m}$?

**Explanation**

The new location is closer, so the result must be greater than $50\ \mathrm{W}/\mathrm{m}^2$. The old-to-new distance ratio is $18/9.0=2$:

$$
I_2
=(50\ \mathrm{W}/\mathrm{m}^2)
\left(\frac{18}{9.0}\right)^2
=(50\ \mathrm{W}/\mathrm{m}^2)(4)
=200\ \mathrm{W}/\mathrm{m}^2.
$$

```quiz
type: radio
id: problem-2-intensity-q3
content: |-
  A sound intensity of $32\ \mathrm{W}/\mathrm{m}^2$ is measured $15\ \mathrm{m}$ from a speaker. Which expression gives the intensity at $6.0\ \mathrm{m}$?
options:
- id: a
  content: |-
    $\displaystyle 32\left(\frac{15}{6.0}\right)^2=200\ \mathrm{W}/\mathrm{m}^2$
  correct: true
  feedback: |-
    The known-distance-to-new-distance ratio is $15/6.0$. Because the new location is closer, the resulting intensity is larger than $32\ \mathrm{W}/\mathrm{m}^2$.
- id: b
  content: |-
    $\displaystyle 32\left(\frac{6.0}{15}\right)^2=5.12\ \mathrm{W}/\mathrm{m}^2$
  feedback: |-
    The ratio is reversed. This predicts a decrease even though the new location is closer.
- id: c
  content: |-
    $\displaystyle 32\left(\frac{15}{6.0}\right)=80\ \mathrm{W}/\mathrm{m}^2$
  feedback: |-
    The ratio direction is correct, but the inverse-square law requires squaring it.
- id: d
  content: |-
    $\displaystyle 32\left(\frac{6.0}{15}\right)=12.8\ \mathrm{W}/\mathrm{m}^2$
  feedback: |-
    This both reverses the ratio and omits the square.
- id: e
  content: |-
    $32\ \mathrm{W}/\mathrm{m}^2$
  feedback: |-
    The intensity stays unchanged only if the distance stays unchanged.
```

---

<a id="match-the-number-only-answer-form"></a>
## Match the Number-Only Answer Form

Carry the units through the work, then follow the requested response format at the end.

**Example:** You are $12\ \mathrm{m}$ from a speaker and measure a sound intensity of $240\ \mathrm{W}/\mathrm{m}^2$. You then move to $24\ \mathrm{m}$ from the speaker. What intensity do you measure?

Enter the intensity in watts per square meter as a number only.

**Explanation**

The new distance is twice the old distance, so the intensity should be one fourth as large:

$$
\begin{aligned}
I_2
&=I_1\left(\frac{r_1}{r_2}\right)^2\\
&=(240\ \mathrm{W}/\mathrm{m}^2)
\left(\frac{12}{24}\right)^2\\
&=(240\ \mathrm{W}/\mathrm{m}^2)\left(\frac12\right)^2\\
&=60\ \mathrm{W}/\mathrm{m}^2.
\end{aligned}
$$

To show two significant figures in polished notation, write $6.0\times10^1\ \mathrm{W}/\mathrm{m}^2$. Because the answer field requests a number only, enter $60$.

```quiz
type: radio
id: problem-2-intensity-q4
content: |-
  A sound intensity is $144\ \mathrm{W}/\mathrm{m}^2$ at $10\ \mathrm{m}$. You move to $30\ \mathrm{m}$, and the response field accepts a number in watts per square meter with no unit. Which number should you enter?
options:
- id: a
  content: |-
    $4$
- id: b
  content: |-
    $16$
  correct: true
  feedback: |-
    $I_2=144(10/30)^2=144/9=16\ \mathrm{W}/\mathrm{m}^2$, so enter $16$.
- id: c
  content: |-
    $48$
- id: d
  content: |-
    $144$
- id: e
  content: |-
    $1296$
```

---

<a id="summary"></a>
## Summary

When the same point source is measured at two distances:

1. Identify the known pair $(I_1,r_1)$ and the new distance $r_2$.
2. Use
   $$
   I_2=I_1\left(\frac{r_1}{r_2}\right)^2.
   $$
3. Square the entire distance ratio.
4. Check the invariant $I_1r_1^2=I_2r_2^2$ and the units $\mathrm{W}/\mathrm{m}^2$.
5. Check direction: farther means lower intensity; closer means higher intensity.
6. Report the result in $\mathrm{W}/\mathrm{m}^2$, or omit the unit only when the response field explicitly asks for a number.

The main traps are using a linear distance ratio and reversing the old-to-new distance ratio.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
