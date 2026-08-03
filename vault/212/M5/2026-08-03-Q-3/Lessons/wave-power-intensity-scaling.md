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
- id: q3-wpis-amplitude-b
  content: |-
    $1/3$
- id: q3-wpis-amplitude-c
  content: |-
    $3$
- id: q3-wpis-amplitude-d
  content: |-
    $6$
- id: q3-wpis-amplitude-e
  content: |-
    $9$
  correct: true
  feedback: |-
    Correct. At fixed frequency and area, $I_2/I_1=(A_2/A_1)^2=3^2=9$.
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
- id: q3-wpis-two-b
  content: |-
    $1/2$
- id: q3-wpis-two-c
  content: |-
    $1$
  correct: true
  feedback: |-
    Correct. The factors cancel after squaring: $2^2(1/2)^2=1$.
- id: q3-wpis-two-d
  content: |-
    $2$
- id: q3-wpis-two-e
  content: |-
    $4$
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
- id: q3-wpis-reverse-b
  content: |-
    $1/9$
- id: q3-wpis-reverse-c
  content: |-
    $1/3$
  correct: true
  feedback: |-
    Correct. Since $I_2/I_1=(f_2/f_1)^2$, the positive frequency ratio is $\sqrt{1/9}=1/3$.
- id: q3-wpis-reverse-d
  content: |-
    $3$
- id: q3-wpis-reverse-e
  content: |-
    $9$
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
- id: q3-wpis-area-b
  content: |-
    $2/5$
  correct: true
  feedback: |-
    Correct. Use $I=P_{\mathrm{avg}}/A_s$: the power contributes a factor of $2$ and the area contributes a factor of $1/5$.
- id: q3-wpis-area-c
  content: |-
    $1/2$
- id: q3-wpis-area-d
  content: |-
    $5/2$
- id: q3-wpis-area-e
  content: |-
    $10$
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

---

<!-- lesson-nav:end -->
