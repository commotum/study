# Convert Between Sound Intensity and Decibels

<!--
lesson-id: 212-M5-071
topic-code: MTH212.M5.71
-->

## Table of Contents

- [Introduction](#introduction)
- [Source-Video Worked Problem: Intensity to Decibels](#source-intensity-to-decibels)
- [Source-Video Worked Problem: Decibels to Intensity](#source-decibels-to-intensity)
- [Paired-Lecture Worked Example: Normal Conversation](#lecture-normal-conversation)
- [Paired-Lecture Worked Example: Two Equal Talkers](#lecture-equal-talkers)
- [Controlled Variation: Use a Decibel Difference](#decibel-difference)
- [Summary](#summary)

## Prerequisites

- Evaluate a common logarithm, written $\log_{10}$ or $\log$ on most calculators.
- Convert between $\log_{10}(x)=y$ and $10^y=x$.
- Use exponent rules for powers of $10$.
- Recognize sound intensity as power per area, measured in $\mathrm{W/m^2}$.

---

<a id="introduction"></a>
## Introduction

Sound intensity $I$ is a physical power-per-area measurement. Sound intensity level $\beta$ records that intensity on a logarithmic decibel scale:

$$
\boxed{\beta=10\log_{10}\!\left(\frac{I}{I_0}\right)},
\qquad
I_0=1.0\times10^{-12}\,\mathrm{W/m^2}.
$$

The reference $I_0$ is the threshold-of-hearing intensity used by the source. Because $I$ and $I_0$ have the same units, their ratio is dimensionless. A logarithm must act on a dimensionless number; expressions such as $\log_{10}(I)$ with $I$ still carrying $\mathrm{W/m^2}$ are not valid here.

Use one conversion move in either direction: locate the unknown, then undo the operations that separate it from the given quantity.

| Given | Route | Result |
|---|---|---|
| intensity $I$ | divide by $I_0$, take $\log_{10}$, multiply by $10$ | level $\beta$ |
| level $\beta$ | divide by $10$, raise $10$ to that power, multiply by $I_0$ | intensity $I$ |

The second form comes from isolating the logarithm before exponentiating:

$$
\frac{\beta}{10}
=\log_{10}\!\left(\frac{I}{I_0}\right)
\quad\Longleftrightarrow\quad
10^{\beta/10}=\frac{I}{I_0}.
$$

Then multiply by $I_0$. The logarithm is base $10$, not the natural logarithm.

For several independent sources at the same listener, add their intensities first. Do not add their decibel levels:

$$
I_{\text{total}}=I_1+I_2+\cdots,
\qquad
\beta_{\text{total}}
=10\log_{10}\!\left(\frac{I_{\text{total}}}{I_0}\right).
$$

---

<a id="source-intensity-to-decibels"></a>
## Source-Video Worked Problem: Intensity to Decibels

The first worked problem in `twppI9Eizp8` at 0:00:07-0:01:15 gives

$$
I=4.0\times10^{-5}\,\mathrm{W/m^2}
$$

and asks for the sound intensity level. Here $I$ is known, so substitute into the logarithmic form:

$$
\begin{aligned}
\beta
&=10\log_{10}\!\left(
\frac{4.0\times10^{-5}\,\mathrm{W/m^2}}
{1.0\times10^{-12}\,\mathrm{W/m^2}}
\right)\\
&=10\log_{10}(4.0\times10^7)\\
&=10(7.60206)\\
&=76.0206\,\mathrm{dB}.
\end{aligned}
$$

Thus the source's rounded result is

$$
\boxed{\beta\approx76\,\mathrm{dB}}.
$$

The ratio $I/I_0=4.0\times10^7$ is greater than $10^7$, so a level just above $70\,\mathrm{dB}$ is a quick check on the result. Notice the two separate factors of $10$: $10^{-12}$ belongs to the reference intensity, while the coefficient $10$ outside the logarithm defines the decibel scale.

```quiz
type: radio
id: mct-p13-intensity-to-decibels
shuffle: true
content: |-
  A sound has intensity $I=2.5\times10^{-6}\,\mathrm{W/m^2}$. What is its sound intensity level, to the nearest tenth of a decibel?
options:
- id: mct-p13-intensity-to-decibels-a
  content: |-
    $64.0\,\mathrm{dB}$
  correct: true
  feedback: |-
    The dimensionless ratio is $(2.5\times10^{-6})/(1.0\times10^{-12})=2.5\times10^6$. Therefore $\beta=10\log_{10}(2.5\times10^6)=63.979\,\mathrm{dB}$, which rounds to $64.0\,\mathrm{dB}$.
- id: mct-p13-intensity-to-decibels-b
  content: |-
    $6.4\,\mathrm{dB}$
  feedback: |-
    This is $\log_{10}(I/I_0)$ without the coefficient that defines decibels. After evaluating the logarithm, multiply by $10$.
- id: mct-p13-intensity-to-decibels-c
  content: |-
    $-64.0\,\mathrm{dB}$
  feedback: |-
    This sign comes from reversing the ratio. The definition uses $I/I_0$; because this sound is more intense than the reference, its level must be positive.
- id: mct-p13-intensity-to-decibels-d
  content: |-
    $-56.0\,\mathrm{dB}$
  feedback: |-
    This takes the logarithm of the numerical intensity alone. First divide by $I_0$ so the logarithm's argument is dimensionless.
- id: mct-p13-intensity-to-decibels-e
  content: |-
    $25.0\,\mathrm{dB}$
  feedback: |-
    The leading number $2.5$ is not multiplied directly by the decibel coefficient. Form $I/I_0$, take its base-$10$ logarithm, and then multiply the result by $10$.
```

---

<a id="source-decibels-to-intensity"></a>
## Source-Video Worked Problem: Decibels to Intensity

The source continues at 0:01:18-0:04:51 by reversing the conversion. Starting from

$$
\beta=10\log_{10}\!\left(\frac{I}{I_0}\right),
$$

divide by $10$, undo the common logarithm with a power of $10$, and multiply by $I_0$:

$$
\boxed{I=I_0\,10^{\beta/10}}.
$$

### Source case: $50\,\mathrm{dB}$

$$
\begin{aligned}
I_{50}
&=(1.0\times10^{-12}\,\mathrm{W/m^2})10^{50/10}\\
&=(1.0\times10^{-12}\,\mathrm{W/m^2})10^5\\
&=\boxed{1.0\times10^{-7}\,\mathrm{W/m^2}}.
\end{aligned}
$$

### Source case: $60\,\mathrm{dB}$

$$
\begin{aligned}
I_{60}
&=(1.0\times10^{-12}\,\mathrm{W/m^2})10^{60/10}\\
&=(1.0\times10^{-12}\,\mathrm{W/m^2})10^6\\
&=\boxed{1.0\times10^{-6}\,\mathrm{W/m^2}}.
\end{aligned}
$$

**Source corrections.** During the comparison, the narration first says $10^{-6}$ for the $50\,\mathrm{dB}$ value and immediately corrects it to $10^{-7}$. The latter is the value supported by the displayed work. A later caption also shortens $10^{-6}\,\mathrm{W/m^2}$ to “watts”; intensity must retain the area denominator, so the correct unit is $\mathrm{W/m^2}$.

The $10\,\mathrm{dB}$ increase multiplies intensity by $10$:

$$
\frac{I_{60}}{I_{50}}
=\frac{10^{-6}}{10^{-7}}
=10.
$$

This is a statement about physical intensity. It does not mean the sound is perceived as ten times as loud.

```quiz
type: radio
id: mct-p13-decibels-to-intensity
shuffle: true
content: |-
  What intensity corresponds to a sound intensity level of $35\,\mathrm{dB}$?
options:
- id: mct-p13-decibels-to-intensity-a
  content: |-
    $3.50\times10^{-12}\,\mathrm{W/m^2}$
  feedback: |-
    Dividing $35$ by $10$ gives an exponent, not a multiplier. Use $10^{3.5}$, then multiply by $I_0$.
- id: mct-p13-decibels-to-intensity-b
  content: |-
    $3.16\times10^{-9}\,\mathrm{W/m^2}$
  correct: true
  feedback: |-
    Invert the logarithm: $I=I_0 10^{\beta/10}=(1.0\times10^{-12})10^{3.5}=3.16\times10^{-9}\,\mathrm{W/m^2}$.
- id: mct-p13-decibels-to-intensity-c
  content: |-
    $1.0\times10^{23}\,\mathrm{W/m^2}$
  feedback: |-
    This uses $10^{35}$ before multiplying by $10^{-12}$. The coefficient in the decibel formula requires the exponent $\beta/10=3.5$, not $\beta=35$.
- id: mct-p13-decibels-to-intensity-d
  content: |-
    $3.16\times10^3\,\mathrm{W/m^2}$
  feedback: |-
    This is $10^{3.5}$ without the threshold intensity. The inverse formula is $I=I_0 10^{\beta/10}$, so multiply by $10^{-12}\,\mathrm{W/m^2}$.
- id: mct-p13-decibels-to-intensity-e
  content: |-
    $-3.16\times10^{-9}\,\mathrm{W/m^2}$
  feedback: |-
    A positive or negative decibel level can correspond to a positive intensity; intensity itself is not made negative by the logarithmic scale. The exponential $10^{\beta/10}$ is positive.
```

---

<a id="lecture-normal-conversation"></a>
## Paired-Lecture Worked Example: Normal Conversation

The M5-3 lecture notes list normal conversation as about $60\,\mathrm{dB}$. Applying the same inverse conversion gives

$$
\begin{aligned}
I
&=I_0 10^{\beta/10}\\
&=(1.0\times10^{-12}\,\mathrm{W/m^2})10^{60/10}\\
&=\boxed{1.0\times10^{-6}\,\mathrm{W/m^2}}.
\end{aligned}
$$

This matches the video's $60\,\mathrm{dB}$ case in the lecture's physical context. Here $\beta/10=6$ is the exponent, while $I_0$ supplies the intensity unit.

---

<a id="lecture-equal-talkers"></a>
## Paired-Lecture Worked Example: Two Equal Talkers

The M5-3 lecture then considers two similar talkers, each producing $60\,\mathrm{dB}$ at the listener. Under the lecture's independent-source model, each contributes

$$
I_1=I_2=1.0\times10^{-6}\,\mathrm{W/m^2}.
$$

Add the time-averaged intensities:

$$
I_{\text{total}}
=I_1+I_2
=2.0\times10^{-6}\,\mathrm{W/m^2}.
$$

Now convert that total intensity back to a level:

$$
\begin{aligned}
\beta_{\text{total}}
&=10\log_{10}\!\left(
\frac{2.0\times10^{-6}}{1.0\times10^{-12}}
\right)\\
&=10\log_{10}(2.0\times10^6)\\
&=63.0103\,\mathrm{dB}\\
&\approx\boxed{63\,\mathrm{dB}}.
\end{aligned}
$$

The combined level is about $63\,\mathrm{dB}$, not $120\,\mathrm{dB}$. Decibels encode a logarithm of intensity, so the physical quantities to add are the intensities.

For $N$ independent equal sources, this calculation compresses to

$$
\boxed{\beta_{\text{total}}=\beta_1+10\log_{10}N}.
$$

```quiz
type: radio
id: mct-p13-equal-sources
shuffle: true
content: |-
  Four independent equal sources each produce a $55\,\mathrm{dB}$ level at one listener. What combined level does the equal-source model predict?
options:
- id: mct-p13-equal-sources-a
  content: |-
    $220\,\mathrm{dB}$
  feedback: |-
    This adds decibel levels. Add the four equal intensities instead, which is equivalent to adding $10\log_{10}(4)$ to one source's level.
- id: mct-p13-equal-sources-b
  content: |-
    $55.0\,\mathrm{dB}$
  feedback: |-
    The combined intensity is four times one source's intensity, so the level must increase. The increase is $10\log_{10}(4)$.
- id: mct-p13-equal-sources-c
  content: |-
    $59.0\,\mathrm{dB}$
  feedback: |-
    The number of sources is not added directly as a number of decibels. Four times the intensity changes the level by $10\log_{10}(4)=6.02\,\mathrm{dB}$.
- id: mct-p13-equal-sources-d
  content: |-
    $61.0\,\mathrm{dB}$
  correct: true
  feedback: |-
    Four equal sources give $I_{\text{total}}=4I_1$, so $\beta_{\text{total}}=55+10\log_{10}(4)=61.02\,\mathrm{dB}$, or $61.0\,\mathrm{dB}$.
- id: mct-p13-equal-sources-e
  content: |-
    $49.0\,\mathrm{dB}$
  feedback: |-
    Adding independent sources increases total intensity, so the combined level cannot be below $55\,\mathrm{dB}$. Add $10\log_{10}(4)$ rather than subtracting it.
```

---

<a id="decibel-difference"></a>
## Controlled Variation: Use a Decibel Difference

When a problem asks only for an intensity factor, the reference intensity cancels. For two sounds,

$$
\begin{aligned}
\beta_2-\beta_1
&=10\log_{10}\!\left(\frac{I_2}{I_0}\right)
-10\log_{10}\!\left(\frac{I_1}{I_0}\right)\\
&=10\log_{10}\!\left(\frac{I_2}{I_1}\right).
\end{aligned}
$$

Therefore,

$$
\boxed{\frac{I_2}{I_1}=10^{(\beta_2-\beta_1)/10}}.
$$

No new conversion is needed: the level difference $\beta_2-\beta_1$ takes the place of $\beta$. Divide it by $10$, then undo the base-$10$ logarithm.

```quiz
type: radio
id: mct-p13-decibel-difference
shuffle: true
content: |-
  A sound level rises from $42\,\mathrm{dB}$ to $72\,\mathrm{dB}$. By what factor does the physical intensity increase?
options:
- id: mct-p13-decibel-difference-a
  content: |-
    $30$
  feedback: |-
    The $30\,\mathrm{dB}$ difference is logarithmic, not the intensity factor itself. Convert it with $10^{\Delta\beta/10}$.
- id: mct-p13-decibel-difference-b
  content: |-
    $3$
  feedback: |-
    Dividing the decibel difference by $10$ gives the exponent $3$, not the final factor. Exponentiate base $10$.
- id: mct-p13-decibel-difference-c
  content: |-
    $1000$
  correct: true
  feedback: |-
    The level change is $72-42=30\,\mathrm{dB}$, so $I_2/I_1=10^{30/10}=10^3=1000$.
- id: mct-p13-decibel-difference-d
  content: |-
    $10^{30}$
  feedback: |-
    The coefficient $10$ in the decibel definition must be removed first. The exponent is $\Delta\beta/10=3$, not $30$.
- id: mct-p13-decibel-difference-e
  content: |-
    $1/1000$
  feedback: |-
    This is the ratio for the reverse comparison, $I_{42}/I_{72}$. Because the level rises, use $I_{72}/I_{42}=10^{30/10}$.
```

---

<a id="summary"></a>
## Summary

- For a known intensity, form the dimensionless ratio $I/I_0$ and use
  $$
  \beta=10\log_{10}\!\left(\frac{I}{I_0}\right).
  $$
- For a known level, isolate the logarithm and invert it with base $10$:
  $$
  I=I_0 10^{\beta/10}.
  $$
- The reference intensity is $I_0=1.0\times10^{-12}\,\mathrm{W/m^2}$.
- A $10\,\mathrm{dB}$ increase means ten times the physical intensity. It is not a claim that perceived loudness is ten times greater.
- For an intensity ratio, use $I_2/I_1=10^{(\beta_2-\beta_1)/10}$.
- For independent sources, add intensities first. Two equal $60\,\mathrm{dB}$ sources give about $63\,\mathrm{dB}$, not $120\,\mathrm{dB}$.
- Keep intensity units as $\mathrm{W/m^2}$; a caption that shortens an intensity to watts has dropped the required area denominator.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
