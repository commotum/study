# Convert an Intensity Ratio into a Decibel Change

## Table of Contents

- [Introduction](#introduction)
- [Use the Intensity Ratio](#use-the-intensity-ratio)
- [Add the Change to an Existing Level](#add-the-change-to-an-existing-level)
- [Keep the Ratio in the Correct Order](#keep-the-ratio-in-the-correct-order)
- [Summary](#summary)

## Prerequisites

- Distinguish wave intensity $I$ from intensity level $\beta$ in decibels.
- Evaluate a base-$10$ logarithm.
- Interpret phrases such as “doubles” as an intensity ratio.

---

<a id="introduction"></a>
## Introduction

When a problem says that a wave's **intensity is multiplied** and asks what happens to its **intensity level**, convert the multiplier into an additive decibel change:

$$
\boxed{
\Delta\beta
=\beta_2-\beta_1
=(10\ \mathrm{dB})\log_{10}\left(\frac{I_2}{I_1}\right)
}.
$$

This change formula follows from the intensity-level definition

$$
\beta=(10\ \mathrm{dB})\log_{10}\left(\frac{I}{I_0}\right).
$$

Subtract the initial level from the final level and use the logarithm quotient rule:

$$
\begin{aligned}
\beta_2-\beta_1
&=(10\ \mathrm{dB})
\left[
\log_{10}\left(\frac{I_2}{I_0}\right)
-\log_{10}\left(\frac{I_1}{I_0}\right)
\right] \\
&=(10\ \mathrm{dB})\log_{10}\left(\frac{I_2}{I_1}\right).
\end{aligned}
$$

The reference intensity $I_0$ cancels, leaving only the **final-to-initial** intensity ratio.

**Recognition cue:** Look for a comparison such as “twice the intensity,” “ten times the intensity,” or “half the intensity,” together with an answer in decibels.

The logarithm acts on the unitless ratio $I_2/I_1$. A multiplicative change in intensity therefore becomes an additive change in intensity level.

---

<a id="use-the-intensity-ratio"></a>
## Use the Intensity Ratio

**Example:** A wave's intensity becomes ten times its original value. Find the change in intensity level.

**Explanation**

“Ten times” means

$$
\frac{I_2}{I_1}=10.
$$

Substitute the ratio, not either intensity separately:

$$
\begin{aligned}
\Delta\beta
&=(10\ \mathrm{dB})\log_{10}(10) \\
&=10\ \mathrm{dB}.
\end{aligned}
$$

The level **increases by** $10\ \mathrm{dB}$. It does not become ten times its previous decibel value.

This exact result uses the base-$10$ identity $\log_{10}(10^n)=n$. Keep these benchmarks nearby:

| Intensity ratio $I_2/I_1$ | Decibel change $\Delta\beta$ |
| ---: | ---: |
| $1/10$ | $-10\ \mathrm{dB}$ |
| $1/2$ | $-3.01\ldots\ \mathrm{dB}$ |
| $1$ | $0\ \mathrm{dB}$ |
| $2$ | $+3.01\ldots\ \mathrm{dB}$ |
| $10$ | $+10\ \mathrm{dB}$ |

Before calculating, predict the sign: a ratio above $1$ gives an increase, while a ratio below $1$ gives a decrease. Powers of $10$ are exact; ratios such as $2$ usually require a calculator or a remembered approximation.

```quiz
type: radio
id: pq3-p2-doubling
content: |-
  If the intensity of a wave doubles, what happens to its intensity level?
options:
- id: a
  content: |-
    It doubles.
  feedback: |-
    Intensity level is logarithmic, so an intensity multiplier does not multiply the decibel value.
- id: b
  content: |-
    It increases by a factor of ten.
  feedback: |-
    The factor $10$ belongs outside the logarithm; it is not the level change for every ratio.
- id: c
  content: |-
    It decreases by a factor of ten.
  feedback: |-
    Doubling gives a ratio greater than $1$, so the logarithm and the level change are positive.
- id: d
  content: |-
    It increases by $2\ \mathrm{dB}$.
  feedback: |-
    The intensity multiplier $2$ goes inside the logarithm; it is not added directly as decibels.
- id: e
  content: |-
    It increases by $3\ \mathrm{dB}$.
  correct: true
  feedback: |-
    Correct. $(10\ \mathrm{dB})\log_{10}(2)=3.01\ldots\ \mathrm{dB}$.
- id: f
  content: |-
    It increases by $10\ \mathrm{dB}$.
  feedback: |-
    A $10\ \mathrm{dB}$ increase corresponds to ten times the intensity, not twice the intensity.
```

---

<a id="add-the-change-to-an-existing-level"></a>
## Add the Change to an Existing Level

**Example:** A sound has an initial intensity level of $50\ \mathrm{dB}$. Its intensity doubles. Find the new intensity level.

**Explanation**

First find the level change:

$$
\Delta\beta
=(10\ \mathrm{dB})\log_{10}(2)
=3.01\ldots\ \mathrm{dB}.
$$

Then add that change to the initial level:

$$
\begin{aligned}
\beta_2
&=\beta_1+\Delta\beta \\
&=50\ \mathrm{dB}+3.01\ldots\ \mathrm{dB} \\
&\approx53\ \mathrm{dB}.
\end{aligned}
$$

The $3\ \mathrm{dB}$ benchmark for doubling is independent of the starting level.

```quiz
type: radio
id: pq3-p2-new-level
content: |-
  A sound has an intensity level of $70\ \mathrm{dB}$. Its physical intensity doubles. What is its new intensity level, to the nearest decibel?
options:
- id: a
  content: |-
    $67\ \mathrm{dB}$
  feedback: |-
    Doubling intensity increases the level; it does not decrease it.
- id: b
  content: |-
    $70\ \mathrm{dB}$
  feedback: |-
    This ignores the change in physical intensity.
- id: c
  content: |-
    $72\ \mathrm{dB}$
  feedback: |-
    The multiplier $2$ is placed inside $10\log_{10}(2)$; it is not added directly.
- id: d
  content: |-
    $73\ \mathrm{dB}$
  correct: true
  feedback: |-
    Correct. Doubling adds $3.01\ldots\ \mathrm{dB}$, so the new level is approximately $73\ \mathrm{dB}$.
- id: e
  content: |-
    $140\ \mathrm{dB}$
  feedback: |-
    This incorrectly doubles the logarithmic decibel level.
```

---

<a id="keep-the-ratio-in-the-correct-order"></a>
## Keep the Ratio in the Correct Order

**Example:** A wave's intensity falls to one-half its original value. Find the change in intensity level.

**Explanation**

Final intensity belongs in the numerator:

$$
\frac{I_2}{I_1}=\frac{1}{2}.
$$

Therefore,

$$
\begin{aligned}
\Delta\beta
&=(10\ \mathrm{dB})\log_{10}\left(\frac{1}{2}\right) \\
&=-3.01\ldots\ \mathrm{dB}.
\end{aligned}
$$

The negative sign is a useful check: a decrease in intensity must produce a decrease in intensity level. Reversing the ratio would incorrectly make the change positive.

```quiz
type: radio
id: pq3-p2-decrease
content: |-
  A wave's intensity decreases to one-tenth its original value. What is the change in its intensity level?
options:
- id: a
  content: |-
    $-10\ \mathrm{dB}$
  correct: true
  feedback: |-
    Correct. $(10\ \mathrm{dB})\log_{10}(1/10)=-10\ \mathrm{dB}$.
- id: b
  content: |-
    $-3\ \mathrm{dB}$
  feedback: |-
    A $-3\ \mathrm{dB}$ change corresponds to halving the intensity, not reducing it by a factor of ten.
- id: c
  content: |-
    $-1\ \mathrm{dB}$
  feedback: |-
    The ratio $1/10$ is not used as a decibel change directly.
- id: d
  content: |-
    $+3\ \mathrm{dB}$
  feedback: |-
    The sign must be negative because the final intensity is smaller than the initial intensity.
- id: e
  content: |-
    $+10\ \mathrm{dB}$
  feedback: |-
    This results from reversing the ratio to $I_1/I_2$.
```

---

<a id="summary"></a>
## Summary

When intensity changes from $I_1$ to $I_2$:

1. Translate the wording into the ratio $I_2/I_1$.
2. Compute $\Delta\beta=(10\ \mathrm{dB})\log_{10}(I_2/I_1)$.
3. If a new level is requested, use $\beta_2=\beta_1+\Delta\beta$.
4. Check the sign: increasing intensity gives $\Delta\beta>0$; decreasing intensity gives $\Delta\beta<0$.

Useful benchmarks are

$$
\boxed{
2\times I\ \longrightarrow\ +3\ \mathrm{dB},
\qquad
10\times I\ \longrightarrow\ +10\ \mathrm{dB}
}.
$$

The main trap is treating the decibel scale as linear. Doubling intensity adds about $3\ \mathrm{dB}$; it does not double the intensity level.
