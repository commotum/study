# Combining Equal Independent Sound Sources in Decibels

## Table of Contents

- [Introduction](#introduction)
- [Add Intensities Before Converting to Decibels](#add-intensities-before-converting-to-decibels)
- [Use the Level-Change Formula](#use-the-level-change-formula)
- [Extend the Same Move to More Sources](#extend-the-same-move-to-more-sources)
- [Solve the Given Conversation Problem](#solve-the-given-conversation-problem)
- [Summary](#summary)

## Prerequisites

- Evaluate a base-$10$ logarithm with a calculator.
- Distinguish sound intensity $I$ from sound intensity level $\beta$ in decibels.
- Add the intensities of independent sources.

---

<a id="introduction"></a>
## Introduction

The sound intensity level corresponding to intensity $I$ is

$$
\beta=10\log_{10}\left(\frac{I}{I_0}\right),
$$

where $I_0$ is the reference intensity. Decibels form a logarithmic scale, so independent sources add by intensity, not by decibel level.

**Recognition cue:** Look for several equally loud, independent sources heard at the same location. “Independent” tells you to add their physical intensities; “decibels” tells you to convert that intensity increase through a base-$10$ logarithm.

If $N$ independent sources have equal intensity $I_1$, their total intensity is

$$
I_N=NI_1.
$$

The corresponding level is

$$
\beta_N=\beta_1+10\log_{10}(N).
$$

This shortcut follows directly from subtracting the two level formulas and using the logarithm quotient rule:

$$
\begin{aligned}
\beta_N-\beta_1
&=10\log_{10}\left(\frac{I_N}{I_0}\right)
-10\log_{10}\left(\frac{I_1}{I_0}\right) \\
&=10\log_{10}\left(\frac{I_N}{I_1}\right) \\
&=10\log_{10}(N).
\end{aligned}
$$

Here $\log_{10}$ is the common logarithm, and its argument $N=I_N/I_1$ is a unitless intensity ratio.

Thus, two equally loud independent sources add about $3.010\ \mathrm{dB}$; they do not double the decibel reading.

---

<a id="add-intensities-before-converting-to-decibels"></a>
## Add Intensities Before Converting to Decibels

**Example:** Two independent sources each have sound intensity $I$. What total intensity and sound intensity level change do they produce?

**Explanation**

The physical intensities add:

$$
I_2=I+I=2I.
$$

Keep the two quantities separate:

| Quantity | How two equal independent sources combine |
|---|---|
| intensity $I$ | $I_2=I+I=2I$ |
| intensity level $\beta$ | $\beta_2=\beta_1+10\log_{10}(2)$ |

The level change depends on the intensity ratio:

$$
\Delta\beta
=10\log_{10}\left(\frac{I_2}{I}\right)
=10\log_{10}(2)
=3.010\ldots\ \mathrm{dB}.
$$

On a calculator, enter the entire expression $10\log_{10}(2)$ before rounding.

```quiz
type: radio
id: p4-intensity-before-db
content: |-
  Two independent sources each produce a sound intensity level of $55\ \mathrm{dB}$ at the listener. Which expression gives their combined sound intensity level?
options:
- id: a
  content: |-
    $55\ \mathrm{dB}+10\log_{10}(2)$
  correct: true
  feedback: |-
    Correct. Two equal independent sources double intensity, producing a level increase of $10\log_{10}(2)$.
- id: b
  content: |-
    $2(55\ \mathrm{dB})$
  feedback: |-
    Intensities add, but logarithmic decibel levels do not add directly.
- id: c
  content: |-
    $55\ \mathrm{dB}+2\ \mathrm{dB}$
  feedback: |-
    The number of sources is the intensity ratio inside the logarithm, not the number of decibels added.
- id: d
  content: |-
    $55\ \mathrm{dB}+\log_{10}(2)$
  feedback: |-
    The definition of sound intensity level requires the factor $10$.
- id: e
  content: |-
    $55\ \mathrm{dB}$
  feedback: |-
    Adding a second independent source increases total intensity and therefore the level.
```

---

<a id="use-the-level-change-formula"></a>
## Use the Level-Change Formula

**Example:** One source produces $50\ \mathrm{dB}$. Find the level produced by two equally loud independent sources.

**Explanation**

For two equal sources, use $N=2$:

$$
\begin{aligned}
\beta_2
&=\beta_1+10\log_{10}(2) \\
&=50\ \mathrm{dB}+3.010\ldots\ \mathrm{dB} \\
&=53.010\ldots\ \mathrm{dB} \\
&\approx53\ \mathrm{dB}.
\end{aligned}
$$

```quiz
type: radio
id: p4-two-equal-sources
content: |-
  One source produces $75\ \mathrm{dB}$. What level is produced by two equally loud independent sources?
options:
- id: a
  content: |-
    $72\ \mathrm{dB}$
  feedback: |-
    A second equal source increases, rather than decreases, the level.
- id: b
  content: |-
    $75\ \mathrm{dB}$
  feedback: |-
    This ignores the doubled intensity.
- id: c
  content: |-
    $78\ \mathrm{dB}$
  correct: true
  feedback: |-
    Correct. Doubling intensity adds $3.010\ldots\ \mathrm{dB}$, which rounds to $3\ \mathrm{dB}$.
- id: d
  content: |-
    $85\ \mathrm{dB}$
  feedback: |-
    Doubling intensity does not add $10\ \mathrm{dB}$; a tenfold intensity increase would.
- id: e
  content: |-
    $150\ \mathrm{dB}$
  feedback: |-
    This incorrectly adds the two decibel levels.
```

---

<a id="extend-the-same-move-to-more-sources"></a>
## Extend the Same Move to More Sources

**Example:** One source produces $42\ \mathrm{dB}$. Find the level produced by four equally loud independent sources.

**Explanation**

Four equal sources make the intensity ratio $N=4$:

$$
\begin{aligned}
\beta_4
&=42\ \mathrm{dB}+10\log_{10}(4) \\
&=42\ \mathrm{dB}+6.020\ldots\ \mathrm{dB} \\
&\approx48\ \mathrm{dB}.
\end{aligned}
$$

Four sources are two successive doublings, so an increase of about $2(3\ \mathrm{dB})=6\ \mathrm{dB}$ is a useful check.

```quiz
type: radio
id: p4-four-equal-sources
content: |-
  One source produces $40\ \mathrm{dB}$. What level is produced by four equally loud independent sources?
options:
- id: a
  content: |-
    $43\ \mathrm{dB}$
  feedback: |-
    A $3\ \mathrm{dB}$ increase corresponds to only one doubling, or two equal sources.
- id: b
  content: |-
    $44\ \mathrm{dB}$
  feedback: |-
    The source count is not added directly as a number of decibels.
- id: c
  content: |-
    $46\ \mathrm{dB}$
  correct: true
  feedback: |-
    Correct. Four equal sources are two doublings, giving about $6\ \mathrm{dB}$ of increase.
- id: d
  content: |-
    $50\ \mathrm{dB}$
  feedback: |-
    A $10\ \mathrm{dB}$ increase corresponds to ten times the intensity, not four times.
- id: e
  content: |-
    $160\ \mathrm{dB}$
  feedback: |-
    This incorrectly adds four decibel levels.
```

---

<a id="solve-the-given-conversation-problem"></a>
## Solve the Given Conversation Problem

**Example:** The sound intensity level of a normal conversation is about $60\ \mathrm{dB}$. What is the sound intensity level if two people are talking independently at that level?

**Explanation**

Each person is one equal independent source, so two people double the intensity:

$$
I_2=2I_1.
$$

Therefore,

$$
\begin{aligned}
\beta_2
&=\beta_1+10\log_{10}(2) \\
&=60\ \mathrm{dB}+3.010\ldots\ \mathrm{dB} \\
&=63.010\ldots\ \mathrm{dB} \\
&\approx63\ \mathrm{dB}.
\end{aligned}
$$

The source answer form is: **Enter the intensity level in decibels as a number only.** The correct entry is $63$.

```quiz
type: radio
id: p4-source-check
content: |-
  The sound intensity level of a normal conversation is about $60\ \mathrm{dB}$. What number should be entered for the sound intensity level if two people are talking independently at that level?
options:
- id: a
  content: |-
    $60$
  feedback: |-
    This ignores the second person's contribution to the intensity.
- id: b
  content: |-
    $62$
  feedback: |-
    The number of people is not the number of decibels added.
- id: c
  content: |-
    $63$
  correct: true
  feedback: |-
    Correct. Two independent equal sources double intensity, so the level rises by $3.010\ldots\ \mathrm{dB}$.
- id: d
  content: |-
    $66$
  feedback: |-
    About $6\ \mathrm{dB}$ corresponds to two successive doublings, or four equal sources.
- id: e
  content: |-
    $120$
  feedback: |-
    Decibel levels are logarithmic and must not be added directly.
```

---

<a id="summary"></a>
## Summary

When $N$ equally loud independent sources are present:

1. Add their intensities: $I_N=NI_1$.
2. Convert the intensity ratio into a level change: $\Delta\beta=10\log_{10}(N)$.
3. Add that change to one source's level: $\beta_N=\beta_1+\Delta\beta$.
4. Round only the final value and follow the requested answer form.

For two equal sources, remember the shortcut: doubling intensity adds about $3\ \mathrm{dB}$. The main trap is adding the decibel levels directly.
