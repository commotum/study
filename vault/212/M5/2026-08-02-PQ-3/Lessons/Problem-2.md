# Convert an Intensity Ratio into a Decibel Change

<!--
lesson-id: 212-M5-046
topic-code: MTH212.M5.46
-->

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
    This treats the decibel scale as linear. Intensity level is logarithmic, so doubling physical intensity adds $10\log_{10}2\approx3\ \mathrm{dB}$ rather than doubling the level.
- id: b
  content: |-
    It increases by a factor of ten.
  feedback: |-
    This confuses the coefficient in the definition with the effect of doubling. The change is additive and equals $(10\ \mathrm{dB})\log_{10}2\approx3\ \mathrm{dB}$, not a factor of ten.
- id: c
  content: |-
    It decreases by a factor of ten.
  feedback: |-
    This reverses the direction and treats a decibel change as a multiplicative factor. Decibel changes are additive: doubling gives $I_2/I_1=2$, so $\Delta\beta=10\log_{10}2\approx+3\ \mathrm{dB}$.
- id: d
  content: |-
    It increases by $2\ \mathrm{dB}$.
  feedback: |-
    This copies the intensity multiplier directly into decibels. The multiplier belongs inside the logarithm: $\Delta\beta=(10\ \mathrm{dB})\log_{10}2=3.01\ldots\ \mathrm{dB}$.
- id: e
  content: |-
    It increases by $3\ \mathrm{dB}$.
  correct: true
  feedback: |-
    A multiplicative intensity change becomes an additive decibel change. For a doubling, $\Delta\beta=(10\ \mathrm{dB})\log_{10}2=3.01\ldots\ \mathrm{dB}$, or about $3\ \mathrm{dB}$.
- id: f
  content: |-
    It increases by $10\ \mathrm{dB}$.
  feedback: |-
    A $10\ \mathrm{dB}$ increase requires $I_2/I_1=10$ because $\log_{10}10=1$. Here the ratio is only $2$, which produces an increase of about $3\ \mathrm{dB}$.
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
    Doubling makes $I_2/I_1>1$, so the decibel change is positive, not negative. It adds about $3\ \mathrm{dB}$ to $70\ \mathrm{dB}$, giving $73\ \mathrm{dB}$.
- id: b
  content: |-
    $70\ \mathrm{dB}$
  feedback: |-
    This assumes the level is unchanged even though the physical intensity doubled. A doubling adds $10\log_{10}2\approx3\ \mathrm{dB}$, so the new level is about $73\ \mathrm{dB}$.
- id: c
  content: |-
    $72\ \mathrm{dB}$
  feedback: |-
    This adds the intensity multiplier $2$ directly to the decibel value. Because the scale is logarithmic, doubling adds $10\log_{10}2=3.01\ldots\ \mathrm{dB}$, which rounds the new level to $73\ \mathrm{dB}$.
- id: d
  content: |-
    $73\ \mathrm{dB}$
  correct: true
  feedback: |-
    Doubling physical intensity always adds $10\log_{10}2=3.01\ldots\ \mathrm{dB}$ to the intensity level. Starting from $70\ \mathrm{dB}$ therefore gives $73.01\ldots\ \mathrm{dB}$, or $73\ \mathrm{dB}$.
- id: e
  content: |-
    $140\ \mathrm{dB}$
  feedback: |-
    This doubles the decibel number as though intensity level were linear. The physical intensity doubles, so the logarithmic level increases by only about $3\ \mathrm{dB}$, from $70$ to $73\ \mathrm{dB}$.
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
    A tenfold intensity decrease gives the final-to-initial ratio $I_2/I_1=1/10$. Therefore $\Delta\beta=(10\ \mathrm{dB})\log_{10}(1/10)=-10\ \mathrm{dB}$.
- id: b
  content: |-
    $-3\ \mathrm{dB}$
  feedback: |-
    A change near $-3\ \mathrm{dB}$ corresponds to $I_2/I_1=1/2$. Here the ratio is $1/10$, whose base-$10$ logarithm is $-1$, so the change is $-10\ \mathrm{dB}$.
- id: c
  content: |-
    $-1\ \mathrm{dB}$
  feedback: |-
    This turns the exponent $-1$ in $1/10=10^{-1}$ directly into decibels and omits the $10\ \mathrm{dB}$ coefficient. The full change is $(10\ \mathrm{dB})(-1)=-10\ \mathrm{dB}$.
- id: d
  content: |-
    $+3\ \mathrm{dB}$
  feedback: |-
    The magnitude $3\ \mathrm{dB}$ describes a factor-of-two change, not a factor of ten, and the sign is also wrong. Since $I_2/I_1=1/10$, the correct change is $-10\ \mathrm{dB}$.
- id: e
  content: |-
    $+10\ \mathrm{dB}$
  feedback: |-
    This uses the reciprocal ratio $I_1/I_2=10$, which describes a tenfold increase. The requested final-to-initial ratio is $I_2/I_1=1/10$, so the level change is $-10\ \mathrm{dB}$.
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

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Doppler Shift for a Moving Observer](../../2026-07-28-M5-3/Lessons/Problem-5.md)

Study guide index: 18/28

---
<!-- lesson-nav:end -->
