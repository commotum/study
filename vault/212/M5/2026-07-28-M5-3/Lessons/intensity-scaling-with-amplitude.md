# Scaling Wave Intensity With Amplitude

<!--
lesson-id: 212-M5-055
topic-code: MTH212.M5.55
-->

## Table of Contents

- [Introduction](#introduction)
- [Turn the Proportionality Into a Ratio](#turn-the-proportionality-into-a-ratio)
- [Square the Amplitude Scale Factor](#square-the-amplitude-scale-factor)
- [Handle Amplitude Decreases](#handle-amplitude-decreases)
- [Convert Percentage Changes to Scale Factors](#convert-percentage-changes-to-scale-factors)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Interpret a ratio as a multiplicative comparison.
- Square integers, decimals, and fractions.
- Use the exponent rule $\left(\frac{x}{y}\right)^2=\frac{x^2}{y^2}$.
- Evaluate a direct-variation relationship while holding other physical conditions fixed.

---

<a id="introduction"></a>
## Introduction

For two versions of the same kind of wave, with frequency and the properties of the medium unchanged, intensity is proportional to the square of amplitude:

$$
I\propto A^2.
$$

Equivalently,

$$
I=kA^2,
$$

where $k$ collects the unchanged physical properties of the wave and medium. This means that intensity does not scale linearly with amplitude. If the amplitude changes by the factor

$$
s=\frac{A_2}{A_1},
$$

then the intensity changes by the factor $s^2$.

The recognition cue is a comparison of two amplitudes followed by a request for an intensity ratio. Use

$$
\boxed{\frac{I_2}{I_1}
=\left(\frac{A_2}{A_1}\right)^2}.
$$

The ratio $I_2/I_1$ is dimensionless. It tells how many times as intense wave $2$ is compared with wave $1$; it is not itself an intensity in $\mathrm{W/m^2}$.

For a nonzero reference wave, a compact two-line template is

$$
s=\frac{A_2}{A_1},
\qquad
\frac{I_2}{I_1}=s^2.
$$

---

<a id="turn-the-proportionality-into-a-ratio"></a>
## Turn the Proportionality Into a Ratio

**Example:** Derive an equation for comparing two intensities when only the amplitude changes.

**Explanation**

Write the same proportionality constant $k$ for both waves:

$$
I_1=kA_1^2,
\qquad
I_2=kA_2^2.
$$

Divide the second equation by the first:

$$
\begin{aligned}
\frac{I_2}{I_1}
&=\frac{kA_2^2}{kA_1^2}\\
&=\frac{A_2^2}{A_1^2}\\
&=\left(\frac{A_2}{A_1}\right)^2.
\end{aligned}
$$

The constant cancels because the comparison keeps the other wave conditions fixed. Squaring the whole amplitude ratio is the reusable step.

Here $I_2/I_1$ is the subject of the calculation. Treat $k$, $A_1$, and $A_2$ as the supplied quantities, substitute them into one fraction, and simplify numerator and denominator in matching order.

```quiz
type: radio
id: intensity-amplitude-ratio-law
shuffle: true
content: |-
  Two waves differ only in amplitude. Which equation correctly relates their intensity ratio to their amplitude ratio?
options:
- id: squared-amplitude-ratio
  content: |-
    $\dfrac{I_2}{I_1}=\left(\dfrac{A_2}{A_1}\right)^2$
  correct: true
  feedback: |-
    Intensity varies directly with amplitude squared. Dividing $I_2=kA_2^2$ by $I_1=kA_1^2$ cancels the common $k$ and gives $I_2/I_1=(A_2/A_1)^2$.
- id: linear-amplitude-ratio
  content: |-
    $\dfrac{I_2}{I_1}=\dfrac{A_2}{A_1}$
  feedback: |-
    This treats intensity as directly proportional to amplitude. The governing relationship is $I\propto A^2$, so the amplitude ratio must be squared.
- id: inverted-squared-ratio
  content: |-
    $\dfrac{I_2}{I_1}=\left(\dfrac{A_1}{A_2}\right)^2$
  feedback: |-
    This reverses the comparison. Because the requested numerator is $I_2$, the matching amplitude $A_2$ must also appear in the numerator before the ratio is squared.
- id: square-numerator-only
  content: |-
    $\dfrac{I_2}{I_1}=\dfrac{A_2^2}{A_1}$
  feedback: |-
    Both intensities contain an amplitude squared: $I_2=kA_2^2$ and $I_1=kA_1^2$. Dividing them leaves $A_2^2/A_1^2$, not a first power of $A_1$.
- id: intensity-ratio-squared
  content: |-
    $\left(\dfrac{I_2}{I_1}\right)^2=\dfrac{A_2}{A_1}$
  feedback: |-
    The square belongs to the amplitude ratio because intensity depends on $A^2$. Squaring the intensity ratio instead reverses the power relationship.
```

---

<a id="square-the-amplitude-scale-factor"></a>
## Square the Amplitude Scale Factor

**Example:** Wave $2$ has amplitude $A_2=2.5A_1$. Find $I_2/I_1$.

**Explanation**

Let the amplitude scale factor be $s$, so $A_2=sA_1$. The power rule applies to the entire product:

$$
A_2^2=(sA_1)^2=s^2A_1^2.
$$

Therefore the common $A_1^2$ cancels from the intensity ratio, leaving $I_2/I_1=s^2$. For this example, first identify $s$:

$$
\frac{A_2}{A_1}
=\frac{2.5A_1}{A_1}
=2.5.
$$

Then square that factor:

$$
\frac{I_2}{I_1}
=\left(2.5\right)^2
=6.25.
$$

Wave $2$ is therefore $6.25$ times as intense as wave $1$. The factor $2.5$ belongs inside the square; the amplitude itself is not the requested ratio.

```quiz
type: radio
id: intensity-amplitude-growth-factor
shuffle: true
content: |-
  A wave's amplitude becomes $3$ times its original amplitude while the other wave conditions stay fixed. By what factor does its intensity change?
options:
- id: factor-nine
  content: |-
    $9$
  correct: true
  feedback: |-
    Intensity scales with amplitude squared. An amplitude factor of $3$ therefore produces an intensity factor of $3^2=9$.
- id: factor-three
  content: |-
    $3$
  feedback: |-
    This applies a linear scaling rule. Amplitude changes by $3$, but intensity depends on the square of amplitude and changes by $3^2=9$.
- id: factor-six
  content: |-
    $6$
  feedback: |-
    Doubling the amplitude factor is not the same as squaring it. The intensity factor is $3\times3=9$, not $2\times3$.
- id: factor-twenty-seven
  content: |-
    $27$
  feedback: |-
    This cubes the amplitude factor. The physical relationship uses $A^2$, so the correct exponent is $2$ and the factor is $9$.
- id: factor-one-third
  content: |-
    $\dfrac13$
  feedback: |-
    An amplitude increase cannot reduce intensity under $I\propto A^2$. The ratio uses new amplitude over original amplitude, $3$, and squaring gives $9$.
```

---

<a id="handle-amplitude-decreases"></a>
## Handle Amplitude Decreases

**Example:** Wave $2$ has one-third the amplitude of wave $1$. Find $I_2/I_1$.

**Explanation**

Translate “one-third the amplitude” directly into the amplitude ratio:

$$
\frac{A_2}{A_1}=\frac13.
$$

Square the entire fraction:

$$
\frac{I_2}{I_1}
=\left(\frac13\right)^2
=\frac19.
$$

Wave $2$ has one-ninth the intensity of wave $1$. Both the numerator and denominator are squared, so an amplitude reduction produces an even stronger intensity reduction.

```quiz
type: radio
id: intensity-amplitude-decrease-factor
shuffle: true
content: |-
  A sound wave's amplitude is reduced to one-half of its original value. What is the ratio of the new intensity to the original intensity?
options:
- id: ratio-one-fourth
  content: |-
    $\dfrac14$
  correct: true
  feedback: |-
    The new-to-original amplitude ratio is $1/2$. Since intensity scales with amplitude squared, the new-to-original intensity ratio is $(1/2)^2=1/4$.
- id: ratio-one-half
  content: |-
    $\dfrac12$
  feedback: |-
    This uses the amplitude factor without squaring it. Intensity responds quadratically, so halving amplitude reduces intensity to one-fourth.
- id: ratio-two
  content: |-
    $2$
  feedback: |-
    This inverts the new-to-original amplitude comparison and also omits the square. The new amplitude is smaller, so the new intensity ratio must be below $1$, specifically $1/4$.
- id: ratio-four
  content: |-
    $4$
  feedback: |-
    The factor $4$ describes original intensity divided by new intensity. The question asks for new divided by original, so the correct ratio is the reciprocal, $1/4$.
- id: ratio-one-eighth
  content: |-
    $\dfrac18$
  feedback: |-
    This cubes the one-half amplitude factor. Intensity is proportional to the second power of amplitude, so the required ratio is $(1/2)^2=1/4$.
```

---

<a id="convert-percentage-changes-to-scale-factors"></a>
## Convert Percentage Changes to Scale Factors

**Example:** A wave's amplitude increases by $40\%$. Find the factor by which its intensity changes.

**Explanation**

An increase of $40\%$ makes the new amplitude

$$
A_2=(1+0.40)A_1=1.40A_1.
$$

Therefore,

$$
\frac{I_2}{I_1}
=\left(\frac{1.40A_1}{A_1}\right)^2
=(1.40)^2
=1.96.
$$

The intensity becomes $1.96$ times the original intensity, which is a $96\%$ increase. Do not square the percentage $40\%$ by itself; first convert the change into the full amplitude scale factor $1.40$.

```quiz
type: radio
id: intensity-amplitude-percent-change
shuffle: true
content: |-
  A wave's amplitude decreases by $20\%$, with frequency and medium unchanged. What is the ratio of the new intensity to the original intensity?
options:
- id: ratio-064
  content: |-
    $0.64$
  correct: true
  feedback: |-
    A $20\%$ amplitude decrease leaves the scale factor $1-0.20=0.80$. Squaring that factor gives the new-to-original intensity ratio $(0.80)^2=0.64$.
- id: ratio-080
  content: |-
    $0.80$
  feedback: |-
    The value $0.80$ is the amplitude ratio after the decrease. Intensity scales with the square of that ratio, so its ratio is $0.64$.
- id: ratio-004
  content: |-
    $0.04$
  feedback: |-
    This squares the lost fraction $0.20$. The intensity that remains is controlled by the retained amplitude factor $0.80$, whose square is $0.64$.
- id: ratio-144
  content: |-
    $1.44$
  feedback: |-
    This uses the growth factor $1.20$ even though the amplitude decreases. The correct amplitude factor is $0.80$, so the intensity ratio is below $1$.
- id: ratio-060
  content: |-
    $0.60$
  feedback: |-
    Subtracting twice the $20\%$ change treats the square law as a linear $40\%$ decrease. The correct quadratic calculation is $(0.80)^2=0.64$.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the original one-blank ratio problem before checking the choices.

**Explanation**

> **Question 1**
>
> If a sound wave's amplitude doubles, what is $I_2/I_1$? ______

The source requests one dimensionless numerical entry. “Doubles” means $A_2/A_1=2$; apply the square law to that amplitude ratio.

```quiz
type: radio
id: khadley-intensity-q1
shuffle: true
content: |-
  Which value belongs in the original problem's $I_2/I_1$ blank?
options:
- id: original-four
  content: |-
    $4$
  correct: true
  feedback: |-
    Wave intensity is proportional to amplitude squared. Since the amplitude ratio is $A_2/A_1=2$, the intensity ratio is $I_2/I_1=2^2=4$.
- id: original-two
  content: |-
    $2$
  feedback: |-
    This makes intensity scale linearly with amplitude. The given doubling supplies the amplitude ratio $2$, but the intensity ratio requires its square, $4$.
- id: original-one-half
  content: |-
    $\dfrac12$
  feedback: |-
    This reverses the amplitude comparison and omits the square. Wave $2$ has the larger amplitude, so $I_2/I_1$ must exceed $1$ and equals $4$.
- id: original-one-fourth
  content: |-
    $\dfrac14$
  feedback: |-
    This is the inverse ratio $I_1/I_2$. The prompt asks for second intensity over first intensity, matching the doubled ratio $A_2/A_1=2$, so the answer is $4$.
- id: original-eight
  content: |-
    $8$
  feedback: |-
    This cubes the amplitude factor. Intensity follows an amplitude-squared law, so doubling amplitude gives $2^2=4$, not $2^3$.
```

---

<a id="summary"></a>
## Summary

When two waves differ only in amplitude:

1. Write the new-to-original amplitude ratio $A_2/A_1$.
2. Call that scale factor $s$ and use the same new-to-original order for the intensity ratio:
   $$
   s=\frac{A_2}{A_1},
   \qquad
   \frac{I_2}{I_1}
   =s^2
   =\left(\frac{A_2}{A_1}\right)^2.
   $$
3. Square the entire amplitude factor, including both parts of a fraction.
4. Check the direction: $s>1$ must give $I_2/I_1>1$, while $0<s<1$ must give $I_2/I_1<1$.

The main traps are applying a linear rule, reversing the ratio, or squaring only the stated percentage rather than the full amplitude scale factor. For the original doubled-amplitude case, $I_2/I_1=2^2=4$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
