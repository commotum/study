# Finding Distance From Sound Intensity

<!--
lesson-id: 212-M5-024
topic-code: MTH212.M5.24
-->

## Table of Contents

- [Introduction](#introduction)
- [Use the Inverse-Square Invariant](#use-the-inverse-square-invariant)
- [Solve for the New Distance](#solve-for-the-new-distance)
- [Keep the Intensity Ratio in the Right Order](#keep-the-intensity-ratio-in-the-right-order)
- [Choose the Physical Root and Round Last](#choose-the-physical-root-and-round-last)
- [Apply the Method to the Speaker](#apply-the-method-to-the-speaker)
- [Summary](#summary)

## Prerequisites

- Substitute values into an equation while keeping subscripts paired.
- Isolate a squared variable and take a square root.
- Round a calculated value to the significant figures supported by measured data.

---

<a id="introduction"></a>
## Introduction

For sound spreading from the same source under the same conditions, intensity $I$ follows an inverse-square relationship with distance $r$:

$$
I\propto\frac{1}{r^2}.
$$

Equivalently, the product of intensity and squared distance stays constant:

$$
Ir^2=\text{constant}.
$$

Comparing two locations eliminates the unknown proportionality constant:

$$
I_1r_1^2=I_2r_2^2.
$$

When the new distance $r_2$ is unknown, isolate it before substituting:

$$
r_2=r_1\sqrt{\frac{I_1}{I_2}}.
$$

The recognition cue is one unchanged speaker with an intensity measured at two locations. Keep each intensity paired with its distance, then use the positive square root because a physical distance cannot be negative.

---

<a id="use-the-inverse-square-invariant"></a>
## Use the Inverse-Square Invariant

**Example:** At $r_1=3.0\ \mathrm{m}$ from a speaker, the intensity is $I_1=200\ \mathrm{W}/\mathrm{m}^2$. At a second location, the intensity is $I_2=50\ \mathrm{W}/\mathrm{m}^2$. Before calculating, should $r_2$ be greater than or less than $3.0\ \mathrm{m}$?

**Explanation**

The measured intensity decreases from $200\ \mathrm{W}/\mathrm{m}^2$ to $50\ \mathrm{W}/\mathrm{m}^2$. Under an inverse-square law, lower intensity means greater distance. Therefore, $r_2$ must be greater than $3.0\ \mathrm{m}$.

This direction check is useful for rejecting an inverted intensity ratio later.

```quiz
type: radio
id: problem-1-direction-q1
content: |-
  A listener moves to a new location relative to the same speaker. The measured sound intensity is greater at the new location. How must the new distance compare with the original distance?
options:
- id: a
  content: |-
    The new distance is greater.
  feedback: |-
    This gives the opposite physical trend. For the same spreading source, intensity decreases as $1/r^2$, so a greater measured intensity means the listener moved closer, not farther away.
- id: b
  content: |-
    The new distance is smaller.
  correct: true
  feedback: |-
    Sound from the same source spreads over more area as distance increases, so $I\propto1/r^2$. A greater intensity therefore means the new distance is smaller.
- id: c
  content: |-
    The new distance is unchanged.
  feedback: |-
    With the source and conditions unchanged, one distance corresponds to one intensity under $I\propto1/r^2$. A greater intensity therefore requires a smaller distance; it cannot occur at the unchanged distance in this model.
```

---

<a id="solve-for-the-new-distance"></a>
## Solve for the New Distance

**Example:** At $r_1=3.0\ \mathrm{m}$ from a speaker, $I_1=200\ \mathrm{W}/\mathrm{m}^2$. Find the new distance when $I_2=50\ \mathrm{W}/\mathrm{m}^2$.

**Explanation**

Start with the two-location invariant and isolate $r_2^2$:

$$
\begin{aligned}
I_1r_1^2&=I_2r_2^2,\\
r_2^2&=r_1^2\frac{I_1}{I_2}.
\end{aligned}
$$

Take the positive square root:

$$
r_2=r_1\sqrt{\frac{I_1}{I_2}}.
$$

Now substitute:

$$
\begin{aligned}
r_2
&=(3.0\ \mathrm{m})\sqrt{\frac{200}{50}}\\
&=(3.0\ \mathrm{m})\sqrt{4}\\
&=6.0\ \mathrm{m}.
\end{aligned}
$$

The intensity fell by a factor of $4$, so the distance increased by a factor of $\sqrt{4}=2$. This agrees with the direction check.

```quiz
type: radio
id: problem-1-distance-q1
content: |-
  At $r_1=4.0\ \mathrm{m}$ from a speaker, $I_1=180\ \mathrm{W}/\mathrm{m}^2$. What is $r_2$ when $I_2=80\ \mathrm{W}/\mathrm{m}^2$?
options:
- id: a
  content: |-
    $2.7\ \mathrm{m}$
  feedback: |-
    This comes from reversing the ratio in $r_2=r_1\sqrt{I_1/I_2}$. Because the intensity fell from $180$ to $80\ \mathrm{W}/\mathrm{m}^2$, the listener must be farther than $4.0\ \mathrm{m}$; the correct distance is $6.0\ \mathrm{m}$.
- id: b
  content: |-
    $6.0\ \mathrm{m}$
  correct: true
  feedback: |-
    For the same source, $Ir^2$ stays constant. The lower second intensity means a larger second distance, and $r_2=(4.0\ \mathrm{m})\sqrt{180/80}=6.0\ \mathrm{m}$.
- id: c
  content: |-
    $9.0\ \mathrm{m}$
  feedback: |-
    This scales distance by the full intensity ratio $180/80=2.25$. Because intensity depends on distance squared, the distance changes by the square root of that factor: $r_2=4.0\sqrt{2.25}=6.0\ \mathrm{m}$.
- id: d
  content: |-
    $4.0\ \mathrm{m}$
  feedback: |-
    This leaves the distance unchanged even though the intensity changed. For the same source, a lower intensity means greater distance; $I_1r_1^2=I_2r_2^2$ gives $r_2=6.0\ \mathrm{m}$.
```

```quiz
type: radio
id: problem-1-distance-q2
content: |-
  At $r_1=5.0\ \mathrm{m}$ from a speaker, $I_1=72\ \mathrm{W}/\mathrm{m}^2$. What is $r_2$ when the measured intensity increases to $I_2=200\ \mathrm{W}/\mathrm{m}^2$?
options:
- id: a
  content: |-
    $3.0\ \mathrm{m}$
  correct: true
  feedback: |-
    For the same source, greater intensity means smaller distance because $Ir^2$ is constant. Thus $r_2=(5.0\ \mathrm{m})\sqrt{72/200}=3.0\ \mathrm{m}$.
- id: b
  content: |-
    $8.3\ \mathrm{m}$
  feedback: |-
    This reverses $I_1/I_2$ under the square root. It also fails the physical check: intensity increased, so the new distance must be less than $5.0\ \mathrm{m}$; the correct value is $3.0\ \mathrm{m}$.
- id: c
  content: |-
    $1.8\ \mathrm{m}$
  feedback: |-
    This multiplies the distance by $I_1/I_2=0.36$ directly. Since intensity varies with inverse distance squared, the distance factor is $\sqrt{0.36}=0.60$, giving $r_2=3.0\ \mathrm{m}$.
- id: d
  content: |-
    $5.0\ \mathrm{m}$
  feedback: |-
    This keeps the distance fixed, which would keep the intensity fixed for the unchanged source. Because the intensity rose from $72$ to $200\ \mathrm{W}/\mathrm{m}^2$, the listener must be closer: $r_2=3.0\ \mathrm{m}$.
```

---

<a id="keep-the-intensity-ratio-in-the-right-order"></a>
## Keep the Intensity Ratio in the Right Order

**Example:** A sound intensity decreases from $I_1=360\ \mathrm{W}/\mathrm{m}^2$ at $r_1=2.0\ \mathrm{m}$ to $I_2=90\ \mathrm{W}/\mathrm{m}^2$. Which ratio belongs under the square root when solving for $r_2$?

**Explanation**

Because the requested quantity is the second distance, start from

$$
I_1r_1^2=I_2r_2^2
$$

and divide by $I_2$:

$$
r_2^2=r_1^2\frac{I_1}{I_2}.
$$

The ratio is therefore $I_1/I_2=360/90$. Since this ratio is greater than $1$, the formula produces $r_2>r_1$, as it should when the intensity decreases.

The square root converts an **intensity scale factor** into a **distance scale factor**:

$$
\frac{r_2}{r_1}=\sqrt{\frac{I_1}{I_2}}.
$$

```quiz
type: radio
id: problem-1-ratio-q1
content: |-
  At a second location, the measured intensity from the same speaker is lower: $I_2<I_1$. Which expression for the second distance has the correct ratio order?
options:
- id: a
  content: |-
    $r_2=r_1\sqrt{\dfrac{I_1}{I_2}}$
  correct: true
  feedback: |-
    The inverse-square invariant is $I_1r_1^2=I_2r_2^2$. Solving for the second distance gives $r_2=r_1\sqrt{I_1/I_2}$; because $I_2<I_1$, this correctly makes $r_2>r_1$.
- id: b
  content: |-
    $r_2=r_1\sqrt{\dfrac{I_2}{I_1}}$
  feedback: |-
    This reverses the ratio obtained by isolating $r_2^2$. It would make $r_2<r_1$ even though a lower intensity from the same source means the listener is farther away.
- id: c
  content: |-
    $r_2=r_1\dfrac{I_1}{I_2}$
  feedback: |-
    This uses the correct ratio order but scales distance linearly with intensity. Since $I\propto1/r^2$, the distance factor is the square root: $r_2/r_1=\sqrt{I_1/I_2}$.
- id: d
  content: |-
    $r_2=r_1\dfrac{I_2}{I_1}$
  feedback: |-
    This has both parts of the scaling wrong: it reverses the isolated ratio and treats the inverse-square law as linear. The lower second intensity requires $r_2=r_1\sqrt{I_1/I_2}>r_1$.
```

---

<a id="choose-the-physical-root-and-round-last"></a>
## Choose the Physical Root and Round Last

**Example:** Algebra gives $r_2^2=20\ \mathrm{m^2}$. What physical distance should be reported to two significant figures?

**Explanation**

Taking square roots algebraically gives $r_2=\pm\sqrt{20}\ \mathrm{m}$, but $r_2$ represents a distance from the speaker. Keep only the positive value:

$$
r_2=\sqrt{20}\ \mathrm{m}=4.472\ldots\ \mathrm{m}.
$$

Round once, at the end, to obtain

$$
r_2=4.5\ \mathrm{m}.
$$

If the answer field requests a number only, enter `4.5`, not the units.

**Watch Out!** The negative algebraic root is not a second physical location in this radial-distance model. The variable $r$ is a nonnegative distance, not a signed coordinate.

```quiz
type: radio
id: problem-1-root-q1
content: |-
  A calculation gives $r_2=3.307\ldots\ \mathrm{m}$. The measured givens have two significant figures, and the answer field requests meters as a number only. What should be entered?
options:
- id: a
  content: |-
    `3.307 m`
  feedback: |-
    The numerical value has not been rounded to the two significant figures supported by the givens, and the field requests no units. Round $3.307\ldots$ once at the end and enter `3.3`.
- id: b
  content: |-
    `3.31`
  feedback: |-
    This is numerically close but retains three significant figures. The first two significant digits are $3$ and $3$, and the next digit is $0$, so the required entry is `3.3`.
- id: c
  content: |-
    `3.3`
  correct: true
  feedback: |-
    Keep guard digits until the end, then match the two significant figures of the measured data. The value $3.307\ldots\ \mathrm{m}$ rounds to $3.3\ \mathrm{m}$, and a number-only field requires `3.3`.
- id: d
  content: |-
    `-3.3`
  feedback: |-
    A radial distance is a nonnegative magnitude, not a signed coordinate. The calculation's physical value is $+3.307\ldots\ \mathrm{m}$, which rounds to the entry `3.3`, not `-3.3`.
```

---

<a id="apply-the-method-to-the-speaker"></a>
## Apply the Method to the Speaker

**Example:** You are $2.5\ \mathrm{m}$ from a speaker and measure a sound intensity of $280\ \mathrm{W}/\mathrm{m}^2$. At a new location, you measure an intensity of $160\ \mathrm{W}/\mathrm{m}^2$. How far are you from the speaker at the new location?

**Explanation**

The intensity decreased, so the new distance should be greater than $2.5\ \mathrm{m}$. Apply the inverse-square invariant:

| Location | Intensity | Distance |
|---|---:|---:|
| 1 | $I_1=280\ \mathrm{W}/\mathrm{m}^2$ | $r_1=2.5\ \mathrm{m}$ |
| 2 | $I_2=160\ \mathrm{W}/\mathrm{m}^2$ | $r_2=?$ |

$$
I_1r_1^2=I_2r_2^2.
$$

Therefore,

$$
\begin{aligned}
r_2
&=r_1\sqrt{\frac{I_1}{I_2}}\\
&=(2.5\ \mathrm{m})\sqrt{\frac{280}{160}}\\
&=3.307\ldots\ \mathrm{m}.
\end{aligned}
$$

The result is greater than $2.5\ \mathrm{m}$, so it passes the direction check. The givens support two significant figures, so $r_2=3.3\ \mathrm{m}$.

```quiz
type: radio
id: m5-3pre-q1
content: |-
  **Question 1**

  You are $2.5\ \mathrm{m}$ from a speaker and measure a sound intensity of $280\ \mathrm{W}/\mathrm{m}^2$. At a new location, you measure an intensity of $160\ \mathrm{W}/\mathrm{m}^2$. How far are you from the speaker at the new location?

  The answer field requires the distance in meters as a number only. What should be entered?
options:
- id: a
  content: |-
    `3.3`
  correct: true
  feedback: |-
    The lower second intensity means the listener is farther away, and the same-source invariant is $I_1r_1^2=I_2r_2^2$. Thus $r_2=(2.5\ \mathrm{m})\sqrt{280/160}=3.307\ldots\ \mathrm{m}$, so the number-only entry is `3.3`.
- id: b
  content: |-
    `3.31`
  feedback: |-
    This keeps three significant figures even though the measured givens support two. Round $3.307\ldots$ once at the end to obtain the number-only entry `3.3`.
- id: c
  content: |-
    `4.4`
  feedback: |-
    This multiplies $2.5\ \mathrm{m}$ by the full ratio $280/160=1.75$. Because intensity follows an inverse-square law, distance scales with the square root of that ratio, giving $3.307\ldots\ \mathrm{m}$ and the entry `3.3`.
- id: d
  content: |-
    `1.9`
  feedback: |-
    This reverses the ratio under the square root. It also contradicts the physical trend: the intensity decreased, so the new distance must exceed $2.5\ \mathrm{m}$; the correct entry is `3.3`.
```

---

<a id="summary"></a>
## Summary

When the same source has intensity measurements at two distances:

1. Pair the data as $(I_1,r_1)$ and $(I_2,r_2)$.
2. Predict the direction: lower intensity means greater distance; higher intensity means smaller distance.
3. Use $I_1r_1^2=I_2r_2^2$.
4. For an unknown second distance, calculate $r_2=r_1\sqrt{I_1/I_2}$.
5. Keep the positive root, round only at the end, and follow the requested answer format.

The main traps are reversing $I_1/I_2$, forgetting the square root, and reporting a negative or over-rounded distance.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Convert an Intensity Ratio into a Decibel Change](../../2026-08-02-PQ-3/Lessons/Problem-2.md)

Study guide index: 17/28

---
<!-- lesson-nav:end -->
