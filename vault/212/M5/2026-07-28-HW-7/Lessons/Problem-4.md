# Doppler Shift from a Moving Sound Source

<!--
lesson-id: 212-M5-017
topic-code: MTH212.M5.17
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Wavelength in Front of the Source](#find-the-wavelength-in-front-of-the-source)
- [Convert the Wavelength to the Heard Frequency](#convert-the-wavelength-to-the-heard-frequency)
- [Choose the Sign from the Direction of Motion](#choose-the-sign-from-the-direction-of-motion)
- [Keep Source Motion in the Denominator](#keep-source-motion-in-the-denominator)
- [Use Only the Information the Question Needs](#use-only-the-information-the-question-needs)
- [Summary](#summary)

## Prerequisites

- Use the Doppler-specialized wave relation $v=f\lambda$, where $v$ is the speed of sound.
- Interpret frequency as the number of wave crests arriving per unit time.
- Recognize that “toward” decreases a distance while “away” increases it.

---

<a id="introduction"></a>
## Introduction

When a source of sound moves while its listener is stationary, the source changes the spacing between successive wave crests. The sound still travels through the air at speed $v$; it does not travel at $v+v_s$ or $v-v_s$.

For a source moving directly toward a stationary listener at speed $v_s$, the crests in front of the source are closer together. Find that shortened wavelength first, then use $f=v/\lambda$ to determine the frequency heard by the listener. The formulas in this lesson assume direct line-of-sight motion, a stationary listener, and $0\le v_s<v$.

The result is

$$
f_{\mathrm{obs}}=\frac{v}{v-v_s}f_0,
$$

where $f_0$ is the frequency emitted by the source. Because $v-v_s<v$, the factor $v/(v-v_s)$ is greater than $1$, matching the fact that approaching motion raises the observed frequency.

Before choosing a formula, ask:

1. **Who moves?** Here, it is the source.
2. **Which way?** Toward means the wavefront spacing decreases.
3. **Should the answer rise or fall?** Toward means $f_{\mathrm{obs}}>f_0$.

---

<a id="find-the-wavelength-in-front-of-the-source"></a>
## Find the Wavelength in Front of the Source

**Example:** A source emits a tone of frequency $500\ \mathrm{Hz}$ while moving at $20\ \mathrm{m}/\mathrm{s}$ toward a stationary listener. Take the speed of sound to be $340\ \mathrm{m}/\mathrm{s}$. What is the wavelength in front of the source?

**Explanation**

The time between emitted crests is one period:

$$
T=\frac{1}{f_0}=\frac{1}{500\ \mathrm{Hz}}.
$$

During one period, the first crest travels forward a distance $cT$, while the source moves forward a distance $vT$. Their separation is therefore

$$
\begin{aligned}
\lambda_{\mathrm{front}}
&=vT-v_sT\\
&=(v-v_s)T\\
&=\frac{v-v_s}{f_0}\\
&=\frac{340-20}{500}\ \mathrm{m}\\
&=0.64\ \mathrm{m}.
\end{aligned}
$$

Subtracting $v_s$ is appropriate because the source moves toward the crest it just emitted, reducing the space before the next crest.

```quiz
type: radio
id: problem-4-q1
content: |-
  A source emits a $300\ \mathrm{Hz}$ tone while moving at $v_s=30\ \mathrm{m}/\mathrm{s}$ toward a stationary listener. If $v=330\ \mathrm{m}/\mathrm{s}$, what is the wavelength in front of the source?
options:
- id: problem-4-q1-a
  content: |-
    $1.0\ \mathrm{m}$
  correct: true
- id: problem-4-q1-b
  content: |-
    $1.1\ \mathrm{m}$
- id: problem-4-q1-c
  content: |-
    $1.2\ \mathrm{m}$
- id: problem-4-q1-d
  content: |-
    $0.91\ \mathrm{m}$
- id: problem-4-q1-e
  content: |-
    $0.10\ \mathrm{m}$
```

---

<a id="convert-the-wavelength-to-the-heard-frequency"></a>
## Convert the Wavelength to the Heard Frequency

**Example:** For the source in the previous example, find the frequency heard by the stationary listener.

**Explanation**

The crests pass the stationary listener at the sound speed $v$, so use $f=v/\lambda$ with the shortened wavelength:

$$
\begin{aligned}
f_{\mathrm{obs}}
&=\frac{v}{\lambda_{\mathrm{front}}}\\
&=\frac{v}{(v-v_s)/f_0}\\
&=\frac{v}{v-v_s}f_0\\
&=\frac{340}{340-20}(500\ \mathrm{Hz})\\
&=531.25\ \mathrm{Hz}.
\end{aligned}
$$

The source motion changed the wavelength; the sound speed at the listener remains $v$.

The units also check:

$$
\left[\frac{v}{v-v_s}\right]
=\frac{\mathrm{m}/\mathrm{s}}{\mathrm{m}/\mathrm{s}}
=1,
\qquad
[f_{\mathrm{obs}}]=1\cdot\mathrm{Hz}=\mathrm{Hz}.
$$

The Doppler factor is dimensionless, so multiplying by $f_0$ produces another frequency.

```quiz
type: radio
id: problem-4-q2
content: |-
  A source emits a $400\ \mathrm{Hz}$ tone while moving at $v_s=40\ \mathrm{m}/\mathrm{s}$ toward a stationary listener. If $v=360\ \mathrm{m}/\mathrm{s}$, what frequency does the listener hear?
options:
- id: problem-4-q2-a
  content: |-
    $450\ \mathrm{Hz}$
  correct: true
- id: problem-4-q2-b
  content: |-
    $360\ \mathrm{Hz}$
- id: problem-4-q2-c
  content: |-
    $400\ \mathrm{Hz}$
- id: problem-4-q2-d
  content: |-
    $444.4\ \mathrm{Hz}$
- id: problem-4-q2-e
  content: |-
    $355.6\ \mathrm{Hz}$
```

---

<a id="choose-the-sign-from-the-direction-of-motion"></a>
## Choose the Sign from the Direction of Motion

**Example:** A source moves directly away from a stationary listener. Which wavelength and frequency formulas apply?

**Explanation**

When the source moves away, it increases the spacing between successive crests traveling toward the listener:

$$
\lambda_{\mathrm{back}}=\frac{v+v_s}{f_0}.
$$

Consequently,

$$
f_{\mathrm{obs}}
=\frac{v}{\lambda_{\mathrm{back}}}
=\frac{v}{v+v_s}f_0.
$$

Use the physical direction as a sign check:

- approaching source $\Rightarrow$ shorter wavelength $\Rightarrow$ higher frequency $\Rightarrow v-v_s$;
- receding source $\Rightarrow$ longer wavelength $\Rightarrow$ lower frequency $\Rightarrow v+v_s$.

Equivalently, check the size of the multiplier:

$$
\frac{v}{v-v_s}>1
\quad\text{and}\quad
\frac{v}{v+v_s}<1.
$$

```quiz
type: radio
id: problem-4-q3
content: |-
  A source of frequency $f_0$ moves directly away from a stationary listener at speed $v_s$. Which frequency does the listener hear?
options:
- id: problem-4-q3-a
  content: |-
    $\dfrac{v}{v+v_s}f_0$
  correct: true
- id: problem-4-q3-b
  content: |-
    $\dfrac{v}{v-v_s}f_0$
- id: problem-4-q3-c
  content: |-
    $\dfrac{v+v_s}{v}f_0$
- id: problem-4-q3-d
  content: |-
    $\dfrac{v-v_s}{v}f_0$
- id: problem-4-q3-e
  content: |-
    $f_0$
```

---

<a id="keep-source-motion-in-the-denominator"></a>
## Keep Source Motion in the Denominator

**Example:** A source approaches a stationary listener. Why is the factor $v/(v-v_s)$ rather than $(v+v_s)/v$?

**Explanation**

The moving source changes the wavelength at emission:

$$
\lambda_{\mathrm{front}}=\frac{v-v_s}{f_0}.
$$

The stationary listener does not move through the incoming wave, so the crest speed relative to the listener is simply $v$. Thus,

$$
f_{\mathrm{obs}}
=\frac{\text{crest speed at listener}}{\text{crest spacing}}
=\frac{v}{(v-v_s)/f_0}
=\frac{v}{v-v_s}f_0.
$$

A factor such as $(v+v_s)/v$ describes a different setup in which listener motion changes the rate of encountering otherwise unchanged wavefronts. For a **moving source**, put the source-speed adjustment with $v$ in the denominator.

```quiz
type: radio
id: problem-4-q4
content: |-
  A siren moves directly toward a person who is standing still. Which feature identifies the correct Doppler factor?
options:
- id: problem-4-q4-a
  content: |-
    Source motion changes the wavelength, so the term involving source speed appears in the denominator.
  correct: true
- id: problem-4-q4-b
  content: |-
    Source motion changes the speed of sound to $v+v_s$.
- id: problem-4-q4-c
  content: |-
    The listener's stationary position makes the heard frequency equal to $f_0$.
- id: problem-4-q4-d
  content: |-
    Approaching motion always places $v+v_s$ in the numerator.
- id: problem-4-q4-e
  content: |-
    The emitted wavelength remains $v/f_0$ in front of the moving source.
```

---

<a id="use-only-the-information-the-question-needs"></a>
## Use Only the Information the Question Needs

**Example:** A hawk flies directly toward a stationary climber while emitting a tone of frequency $f_0$. Some sound later echoes from the canyon wall. What frequency does the climber hear directly from the approaching hawk?

**Explanation**

For the requested frequency, identify only the source-listener pair:

- source: the hawk, moving toward the climber at speed $v_s$;
- listener: the climber, stationary;
- sound speed: $v$;
- emitted frequency: $f_0$.

The echo does not enter the direct hawk-to-climber frequency. The source approaches, so

$$
f_{\mathrm{climber}}=\frac{v}{v-v_s}f_0.
$$

The factor is greater than $1$, providing a quick direction check.

```quiz
type: radio
id: problem-4-q5
shuffle: true
content: |-
  Let $v$ denote the speed of sound.

  A hawk at the Grand Canyon produces a pure tone of frequency $f_0$ while flying at constant speed $v_s$ directly towards a climber on the canyon wall. Some of the sound echoes off the canyon wall and back to the hawk.

  What is the frequency of the hawk's screech according to the mountain climber?
options:
- id: problem-4-q5-a
  content: |-
    $\dfrac{v+v_s}{v}f_0$
- id: problem-4-q5-b
  content: |-
    $\dfrac{v-v_s}{v}f_0$
- id: problem-4-q5-c
  content: |-
    $\dfrac{v}{v+v_s}f_0$
- id: problem-4-q5-d
  content: |-
    $\dfrac{v}{v-v_s}f_0$
  correct: true
```

---

<a id="summary"></a>
## Summary

For a sound source moving at speed $v_s$ while its listener is stationary:

1. Determine how source motion changes the wavefront spacing:

   $$
   \lambda_{\mathrm{toward}}=\frac{v-v_s}{f_0},
   \qquad
   \lambda_{\mathrm{away}}=\frac{v+v_s}{f_0}.
   $$

2. Use $f_{\mathrm{obs}}=v/\lambda$:

   $$
   f_{\mathrm{toward}}=\frac{v}{v-v_s}f_0,
   \qquad
   f_{\mathrm{away}}=\frac{v}{v+v_s}f_0.
   $$

3. Check the result: approaching must raise the frequency, and receding must lower it.

The main trap is using a moving-listener numerator when the **source** is moving. Source motion changes wavelength, so its speed adjustment appears in the denominator. Extra story details, such as a later echo, matter only if the question asks about that later path.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
