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

**Example:** At $r_1=3.0\ \mathrm{m}$ from a speaker, the intensity is $I_1=200\ \mathrm{W/m^2}$. At a second location, the intensity is $I_2=50\ \mathrm{W/m^2}$. Before calculating, should $r_2$ be greater than or less than $3.0\ \mathrm{m}$?

**Explanation**

The measured intensity decreases from $200\ \mathrm{W/m^2}$ to $50\ \mathrm{W/m^2}$. Under an inverse-square law, lower intensity means greater distance. Therefore, $r_2$ must be greater than $3.0\ \mathrm{m}$.

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
    Greater distance would reduce the intensity under an inverse-square law.
- id: b
  content: |-
    The new distance is smaller.
  correct: true
  feedback: |-
    Greater intensity means the listener is closer to the same source.
- id: c
  content: |-
    The new distance is unchanged.
  feedback: |-
    An unchanged distance would give the same intensity under the stated conditions.
```

---

<a id="solve-for-the-new-distance"></a>
## Solve for the New Distance

**Example:** At $r_1=3.0\ \mathrm{m}$ from a speaker, $I_1=200\ \mathrm{W/m^2}$. Find the new distance when $I_2=50\ \mathrm{W/m^2}$.

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
  At $r_1=4.0\ \mathrm{m}$ from a speaker, $I_1=180\ \mathrm{W/m^2}$. What is $r_2$ when $I_2=80\ \mathrm{W/m^2}$?
options:
- id: a
  content: |-
    $2.7\ \mathrm{m}$
  feedback: |-
    This result comes from reversing the intensity ratio and also fails the direction check.
- id: b
  content: |-
    $6.0\ \mathrm{m}$
  correct: true
  feedback: |-
    $r_2=(4.0\ \mathrm{m})\sqrt{180/80}=(4.0\ \mathrm{m})(1.5)=6.0\ \mathrm{m}$.
- id: c
  content: |-
    $9.0\ \mathrm{m}$
  feedback: |-
    This uses the intensity ratio directly instead of taking its square root.
- id: d
  content: |-
    $4.0\ \mathrm{m}$
  feedback: |-
    A lower measured intensity requires a greater distance from the same source.
```

```quiz
type: radio
id: problem-1-distance-q2
content: |-
  At $r_1=5.0\ \mathrm{m}$ from a speaker, $I_1=72\ \mathrm{W/m^2}$. What is $r_2$ when the measured intensity increases to $I_2=200\ \mathrm{W/m^2}$?
options:
- id: a
  content: |-
    $3.0\ \mathrm{m}$
  correct: true
  feedback: |-
    $r_2=(5.0\ \mathrm{m})\sqrt{72/200}=(5.0\ \mathrm{m})(0.60)=3.0\ \mathrm{m}$.
- id: b
  content: |-
    $8.3\ \mathrm{m}$
  feedback: |-
    This reverses the ratio and gives a greater distance even though the intensity increased.
- id: c
  content: |-
    $1.8\ \mathrm{m}$
  feedback: |-
    This uses $I_1/I_2$ directly instead of its square root.
- id: d
  content: |-
    $5.0\ \mathrm{m}$
  feedback: |-
    A changed intensity from the same source requires a changed distance under this model.
```

---

<a id="keep-the-intensity-ratio-in-the-right-order"></a>
## Keep the Intensity Ratio in the Right Order

**Example:** A sound intensity decreases from $I_1=360\ \mathrm{W/m^2}$ at $r_1=2.0\ \mathrm{m}$ to $I_2=90\ \mathrm{W/m^2}$. Which ratio belongs under the square root when solving for $r_2$?

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
    Since $I_1/I_2>1$, this expression correctly gives $r_2>r_1$.
- id: b
  content: |-
    $r_2=r_1\sqrt{\dfrac{I_2}{I_1}}$
  feedback: |-
    This would give $r_2<r_1$ even though the measured intensity decreased.
- id: c
  content: |-
    $r_2=r_1\dfrac{I_1}{I_2}$
  feedback: |-
    The distance is related to the square root of the intensity ratio.
- id: d
  content: |-
    $r_2=r_1\dfrac{I_2}{I_1}$
  feedback: |-
    This both reverses the ratio and omits the square root.
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
    This keeps too many significant figures and includes units in a number-only field.
- id: b
  content: |-
    `3.31`
  feedback: |-
    This has three significant figures rather than two.
- id: c
  content: |-
    `3.3`
  correct: true
  feedback: |-
    $3.307\ldots$ rounds to $3.3$ at two significant figures, entered without units.
- id: d
  content: |-
    `-3.3`
  feedback: |-
    A physical distance from the speaker is nonnegative.
```

---

<a id="apply-the-method-to-the-speaker"></a>
## Apply the Method to the Speaker

**Example:** You are $2.5\ \mathrm{m}$ from a speaker and measure a sound intensity of $280\ \mathrm{W/m^2}$. At a new location, you measure an intensity of $160\ \mathrm{W/m^2}$. How far are you from the speaker at the new location?

**Explanation**

The intensity decreased, so the new distance should be greater than $2.5\ \mathrm{m}$. Apply the inverse-square invariant:

| Location | Intensity | Distance |
|---|---:|---:|
| 1 | $I_1=280\ \mathrm{W/m^2}$ | $r_1=2.5\ \mathrm{m}$ |
| 2 | $I_2=160\ \mathrm{W/m^2}$ | $r_2=?$ |

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

  You are $2.5\ \mathrm{m}$ from a speaker and measure a sound intensity of $280\ \mathrm{W/m^2}$. At a new location, you measure an intensity of $160\ \mathrm{W/m^2}$. How far are you from the speaker at the new location?

  The answer field requires the distance in meters as a number only. What should be entered?
options:
- id: a
  content: |-
    `3.3`
  correct: true
  feedback: |-
    Sound intensity follows $I_1r_1^2=I_2r_2^2$, so $r_2=(2.5\ \mathrm{m})\sqrt{280/160}=3.307\ldots\ \mathrm{m}$. To two significant figures, enter `3.3`.
- id: b
  content: |-
    `3.31`
  feedback: |-
    This keeps three significant figures, but the givens support two.
- id: c
  content: |-
    `4.4`
  feedback: |-
    This uses the intensity ratio without the required square root.
- id: d
  content: |-
    `1.9`
  feedback: |-
    This reverses the intensity ratio and predicts a smaller distance even though the intensity decreased.
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

Study guide index: 12/20

---

<!-- lesson-nav:end -->
