# Scaling Wave Power and Intensity with Frequency and Amplitude

<!--
lesson-id: 212-M5-051
topic-code: MTH212.M5.51
-->

## Table of Contents

- [Introduction](#introduction)
- [Scale With Amplitude](#scale-with-amplitude)
- [Scale Frequency and Amplitude Together](#scale-frequency-and-amplitude-together)
- [Recover a Frequency or Amplitude Ratio](#recover-a-frequency-or-amplitude-ratio)
- [Keep Wave Amplitude Separate From Area](#keep-wave-amplitude-separate-from-area)
- [Summary](#summary)

## Prerequisites

- Form and simplify ratios.
- Square a ratio and take a positive square root.
- Recognize frequency $f$ and wave amplitude $A$.

---

<a id="introduction"></a>
## Introduction

When two sinusoidal waves travel in the same linear medium, the cue **compare their power or intensity from changes in frequency and amplitude** signals a square-law ratio.

For fixed properties of the medium,

$$
P_{\mathrm{avg}}\propto f^2A^2.
$$

If the waves are also compared through the same surface area, then

$$
I\propto f^2A^2.
$$

The reusable ratio is

$$
\frac{P_{\mathrm{avg},2}}{P_{\mathrm{avg},1}}
=
\left(\frac{f_2}{f_1}\right)^2
\left(\frac{A_2}{A_1}\right)^2.
$$

At equal comparison areas, the same right-hand side gives $I_2/I_1$. The core habit is to form each **new-to-old ratio first**, then square it.

Here $A$ means wave amplitude. A surface area will be written $A_s$ so the two quantities do not get confused.

---

<a id="scale-with-amplitude"></a>
## Scale With Amplitude

**Example:** Two waves have the same frequency and travel in the same medium. Wave 2 has $2.5$ times the amplitude of wave 1. Compare their average powers and their intensities through equal areas.

**Explanation**

Because the frequency ratio is $1$,

$$
\frac{P_{\mathrm{avg},2}}{P_{\mathrm{avg},1}}
=
(1)^2(2.5)^2
=6.25.
$$

The comparison areas are equal, so the intensity ratio is also

$$
\frac{I_2}{I_1}=6.25.
$$

Increasing amplitude by a factor of $2.5$ increases power and fixed-area intensity by a factor of $6.25$, not $2.5$.

```quiz
type: radio
id: q3-wpis-amplitude-ratio
content: |-
  Two sinusoidal waves have the same frequency, travel in the same medium, and are compared through equal areas. Wave 2 has three times the amplitude of wave 1. What is $I_2/I_1$?
options:
- id: q3-wpis-amplitude-a
  content: |-
    $1/9$
  feedback: |-
    This reverses the new-to-old comparison. Wave 2 has the larger amplitude, and intensity grows with amplitude squared, so $I_2/I_1=3^2=9>1$.
- id: q3-wpis-amplitude-b
  content: |-
    $1/3$
  feedback: |-
    This both reverses the ratio and treats amplitude linearly. For equal frequency and area, intensity scales as $A^2$, so tripling amplitude makes $I_2/I_1=9$.
- id: q3-wpis-amplitude-c
  content: |-
    $3$
  feedback: |-
    This treats intensity as proportional to amplitude. Wave energy, and therefore fixed-area intensity, scales with amplitude squared, so the factor is $3^2=9$.
- id: q3-wpis-amplitude-d
  content: |-
    $6$
  feedback: |-
    This doubles the amplitude factor, but the dependence is quadratic rather than “twice the factor.” With $A_2/A_1=3$, the intensity ratio is $3^2=9$.
- id: q3-wpis-amplitude-e
  content: |-
    $9$
  correct: true
  feedback: |-
    At fixed frequency and comparison area, intensity scales with the square of wave amplitude. Since $A_2/A_1=3$, $I_2/I_1=3^2=9$.
```

---

<a id="scale-frequency-and-amplitude-together"></a>
## Scale Frequency and Amplitude Together

**Example:** Wave 2 has half the frequency and three times the amplitude of wave 1. The medium and comparison area do not change. Find $I_2/I_1$.

**Explanation**

Square both changes:

$$
\begin{aligned}
\frac{I_2}{I_1}
&=
\left(\frac{1}{2}\right)^2(3)^2 \\
&=\frac{1}{4}\cdot9 \\
&=\frac{9}{4}.
\end{aligned}
$$

The reduced frequency lowers the ratio, while the larger amplitude raises it. Multiplying the two squared effects gives a net intensity increase by a factor of $9/4$.

```quiz
type: radio
id: q3-wpis-two-changes
content: |-
  Wave 2 has twice the frequency and half the amplitude of wave 1. The waves travel in the same medium and are compared through equal areas. What is $P_{\mathrm{avg},2}/P_{\mathrm{avg},1}$?
options:
- id: q3-wpis-two-a
  content: |-
    $1/4$
  feedback: |-
    This includes only the halved amplitude's factor, $(1/2)^2=1/4$. The doubled frequency independently contributes $2^2=4$, so the two effects cancel and the full ratio is $1$.
- id: q3-wpis-two-b
  content: |-
    $1/2$
  feedback: |-
    This keeps only a linear amplitude factor. Average power scales as $f^2A^2$, so the new-to-old factors are $2^2$ and $(1/2)^2$; their product is $1$.
- id: q3-wpis-two-c
  content: |-
    $1$
  correct: true
  feedback: |-
    Average power scales as $f^2A^2$. Doubling frequency contributes $2^2=4$, while halving amplitude contributes $(1/2)^2=1/4$, so $P_{\mathrm{avg},2}/P_{\mathrm{avg},1}=1$.
- id: q3-wpis-two-d
  content: |-
    $2$
  feedback: |-
    This does not combine both quadratic effects. Frequency raises the ratio by $2^2=4$, but amplitude lowers it by $(1/2)^2=1/4$; multiplying gives $1$, not $2$.
- id: q3-wpis-two-e
  content: |-
    $4$
  feedback: |-
    This keeps the doubled frequency's $2^2=4$ effect but omits the amplitude change. Halving amplitude supplies $(1/2)^2=1/4$, which exactly cancels that increase.
```

---

<a id="recover-a-frequency-or-amplitude-ratio"></a>
## Recover a Frequency or Amplitude Ratio

**Example:** Two waves have the same frequency and are compared in the same medium through equal areas. Wave 2 has $16$ times the intensity of wave 1. Find $A_2/A_1$.

**Explanation**

With the frequency ratio equal to $1$,

$$
16=\left(\frac{A_2}{A_1}\right)^2.
$$

Amplitude is a nonnegative magnitude, so take the positive square root:

$$
\frac{A_2}{A_1}=\sqrt{16}=4.
$$

The main reverse-scaling trap is to report $16$ as the amplitude factor instead of undoing the square.

```quiz
type: radio
id: q3-wpis-reverse-ratio
content: |-
  Two waves have the same amplitude, travel in the same medium, and are compared through equal areas. If $I_2/I_1=1/9$, what is $f_2/f_1$?
options:
- id: q3-wpis-reverse-a
  content: |-
    $1/81$
  feedback: |-
    This squares the already-squared effect again. Because $I_2/I_1=(f_2/f_1)^2$, recovering the positive frequency ratio requires a square root: $f_2/f_1=\sqrt{1/9}=1/3$.
- id: q3-wpis-reverse-b
  content: |-
    $1/9$
  feedback: |-
    This copies the intensity ratio as though intensity scaled linearly with frequency. The frequency ratio is squared in intensity, so $f_2/f_1=\sqrt{1/9}=1/3$.
- id: q3-wpis-reverse-c
  content: |-
    $1/3$
  correct: true
  feedback: |-
    With amplitude, medium, and area unchanged, intensity scales as $f^2$. Therefore the positive frequency ratio is $f_2/f_1=\sqrt{I_2/I_1}=\sqrt{1/9}=1/3$.
- id: q3-wpis-reverse-d
  content: |-
    $3$
  feedback: |-
    This takes the square root after reversing the comparison. Since $I_2/I_1=1/9<1$, wave 2 must also have the smaller frequency, so $f_2/f_1=1/3$, not $3$.
- id: q3-wpis-reverse-e
  content: |-
    $9$
  feedback: |-
    This reverses $I_2/I_1$ and does not undo the square-law relation. Keep the new-to-old order and take the positive square root: $f_2/f_1=\sqrt{1/9}=1/3$.
```

---

<a id="keep-wave-amplitude-separate-from-area"></a>
## Keep Wave Amplitude Separate From Area

**Example:** The same average power passes through a surface whose area becomes four times as large. What happens to the intensity?

**Explanation**

This is an area change, not a wave-amplitude change. Use the definition

$$
I=\frac{P_{\mathrm{avg}}}{A_s}.
$$

Therefore,

$$
\frac{I_2}{I_1}
=
\frac{P_{\mathrm{avg},2}}{P_{\mathrm{avg},1}}
\frac{A_{s,1}}{A_{s,2}}
=
(1)\left(\frac{1}{4}\right)
=\frac{1}{4}.
$$

Wave amplitude $A$ appears squared in $P_{\mathrm{avg}}\propto f^2A^2$. Surface area $A_s$ instead divides the power. Do not square an area ratio merely because both quantities use the letter $A$ in some textbooks.

```quiz
type: radio
id: q3-wpis-area-definition
content: |-
  Average wave power doubles while the surface area carrying that power becomes five times as large. What is $I_2/I_1$?
options:
- id: q3-wpis-area-a
  content: |-
    $2/25$
  feedback: |-
    This treats surface area like wave amplitude and squares its factor. Surface area appears only to the first power in $I=P_{\mathrm{avg}}/A_s$, so the ratio is $2/5$, not $2/25$.
- id: q3-wpis-area-b
  content: |-
    $2/5$
  correct: true
  feedback: |-
    Intensity is power distributed per unit area. Doubling the power contributes a factor of $2$, while spreading it over five times the area contributes $1/5$, so $I_2/I_1=2/5$.
- id: q3-wpis-area-c
  content: |-
    $1/2$
  feedback: |-
    This uses the reciprocal of the power factor and omits the area factor. The power doubles while the area grows fivefold, so $I_2/I_1=2(1/5)=2/5$.
- id: q3-wpis-area-d
  content: |-
    $5/2$
  feedback: |-
    This puts the fivefold area increase in the numerator, as though spreading power over more area increased intensity. Area divides power, so $I_2/I_1=2/5$.
- id: q3-wpis-area-e
  content: |-
    $10$
  feedback: |-
    This multiplies the power and area factors, but a larger area spreads the power out. Since $I=P_{\mathrm{avg}}/A_s$, the correct new-to-old ratio is $2/5$.
```

---

<a id="summary"></a>
## Summary

Use this decision routine:

1. For two sinusoidal waves in the same linear medium, write
   $$
   \frac{P_{\mathrm{avg},2}}{P_{\mathrm{avg},1}}
   =
   \left(\frac{f_2}{f_1}\right)^2
   \left(\frac{A_2}{A_1}\right)^2.
   $$
2. If the comparison area is unchanged, the intensity has the same ratio.
3. Square both the frequency ratio and the wave-amplitude ratio.
4. When solving backward, take the positive square root.
5. If surface area changes, apply
   $$
   I=\frac{P_{\mathrm{avg}}}{A_s}
   $$
   separately.

The main trap is confusing wave amplitude $A$ with surface area $A_s$. Wave amplitude is squared in the power scaling; surface area divides power in the definition of intensity.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../Study-Guide.md)
Next: [Finding Distance From Sound Intensity](../../2026-07-28-M5-3/Lessons/Problem-1.md)

Study guide index: 16/28

---
<!-- lesson-nav:end -->
