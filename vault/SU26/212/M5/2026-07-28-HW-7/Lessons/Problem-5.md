# Hearing an Echo as a Moving Observer

<!--
lesson-id: 212-M5-018
topic-code: MTH212.M5.18
-->

## Table of Contents

- [Introduction](#introduction)
- [Keep the Frequency at a Stationary Reflection](#keep-the-frequency-at-a-stationary-reflection)
- [Use the Moving-Observer Factor](#use-the-moving-observer-factor)
- [Use Direction to Choose the Sign](#use-direction-to-choose-the-sign)
- [Apply the Factor to the Hawk's Echo](#apply-the-factor-to-the-hawks-echo)
- [Summary](#summary)

## Prerequisites

- Distinguish a wave's source from the observer who receives it.
- Interpret frequency as the number of wave crests received per second.
- Compare a positive factor with $1$.

---

<a id="introduction"></a>
## Introduction

The key cue is that the sound has already reflected from the stationary canyon wall and is traveling back toward the moving hawk. The wall sends the echo back with frequency $f_1$, so on this return trip the wall acts as a stationary source and the hawk acts as a moving observer.

For motion directly along the wave's path in still air, an observer moving toward the incoming wave uses

$$
f_{\mathrm{obs}}=\frac{v+v_o}{v}f_1,
$$

where

- $f_1$ is the frequency carried through the air on the return stage,
- $f_{\mathrm{obs}}$ is the crest-arrival rate measured by the observer,
- $v$ is the speed of sound, and
- $v_o$ is the observer's positive speed toward the wave, with $0<v_o<v$.

Read the equation as

$$
\text{heard frequency}
=
\frac{\text{crest-meeting speed}}{\text{wave speed}}
\times
\text{wave frequency}.
$$

The task is to identify the hawk as the moving observer and multiply $f_1$ by this factor.

---

<a id="keep-the-frequency-at-a-stationary-reflection"></a>
## Keep the Frequency at a Stationary Reflection

**Example:** A stationary canyon wall receives sound with frequency $600\ \mathrm{Hz}$. What frequency does the reflected wave carry away from the wall?

**Explanation**

A stationary reflector changes the direction of the wave, but it does not change the rate at which crests arrive and leave. The reflected wave therefore carries the same frequency:

$$
f_{\mathrm{reflected}}=600\ \mathrm{Hz}.
$$

In the hawk problem, this means the returning echo begins with frequency $f_1$. Do not apply the outbound Doppler factor a second time at the stationary wall.

```quiz
type: radio
id: q-p5-stationary-reflection
content: |-
  A stationary wall receives a tone of frequency $F$. What frequency does the reflected wave carry through the air?
options:
- id: p5-reflection-a
  content: |-
    $F$
  correct: true
- id: p5-reflection-b
  content: |-
    $\dfrac{v+v_o}{v}F$
- id: p5-reflection-c
  content: |-
    $\dfrac{v}{v-v_o}F$
- id: p5-reflection-d
  content: |-
    $\dfrac{v-v_o}{v}F$
```

---

<a id="use-the-moving-observer-factor"></a>
## Use the Moving-Observer Factor

**Example:** A reflected wave has frequency $680\ \mathrm{Hz}$. An observer moves directly toward it at $v_o=20\ \mathrm{m}/\mathrm{s}$, and $v=340\ \mathrm{m}/\mathrm{s}$. What frequency does the observer hear?

**Explanation**

The wave's wavelength in the air is

$$
\lambda=\frac{v}{f_1}.
$$

Because the observer moves toward the crests, the crests meet the observer at relative speed $v+v_o$. Thus

$$
\begin{aligned}
f_{\mathrm{obs}}
&=\frac{v+v_o}{\lambda} \\
&=\frac{v+v_o}{v}f_1 \\
&=\frac{340+20}{340}(680\ \mathrm{Hz}) \\
&=720\ \mathrm{Hz}.
\end{aligned}
$$

The observer's motion changes the crest-arrival rate, so $v+v_o$ belongs in the numerator.

```quiz
type: radio
id: q-p5-moving-observer-number
content: |-
  A reflected wave has frequency $660\ \mathrm{Hz}$. An observer moves directly toward the wave at $v_o=30\ \mathrm{m}/\mathrm{s}$, and $v=330\ \mathrm{m}/\mathrm{s}$. What frequency does the observer hear?
options:
- id: p5-number-a
  content: |-
    $600\ \mathrm{Hz}$
- id: p5-number-b
  content: |-
    $660\ \mathrm{Hz}$
- id: p5-number-c
  content: |-
    $720\ \mathrm{Hz}$
  correct: true
- id: p5-number-d
  content: |-
    $726\ \mathrm{Hz}$
```

---

<a id="use-direction-to-choose-the-sign"></a>
## Use Direction to Choose the Sign

**Example:** A listener moves toward a stationary source that sends a wave of frequency $F$. Without calculating, decide whether the heard frequency is above or below $F$.

**Explanation**

Moving toward the wave means meeting more crests each second, so the observed frequency must be above $F$. Since $v_o>0$,

$$
\frac{v+v_o}{v}>1,
$$

and therefore

$$
f_{\mathrm{obs}}=\frac{v+v_o}{v}F>F.
$$

This size check separates the two moving-observer cases:

$$
\text{toward: }\frac{v+v_o}{v},
\qquad
\text{away: }\frac{v-v_o}{v}.
$$

A denominator such as $v-v_s$ belongs to a moving-source formula, not to this return trip, where the hawk is the observer.

```quiz
type: radio
id: q-p5-direction-check
content: |-
  A reflected wave of frequency $F$ travels toward a bird, and the bird flies toward the incoming wave at speed $v_o$. Which expression has both the correct role placement and the correct direction?
options:
- id: p5-direction-a
  content: |-
    $\dfrac{v+v_o}{v}F$
  correct: true
- id: p5-direction-b
  content: |-
    $\dfrac{v-v_o}{v}F$
- id: p5-direction-c
  content: |-
    $\dfrac{v}{v+v_o}F$
- id: p5-direction-d
  content: |-
    $\dfrac{v}{v-v_o}F$
```

---

<a id="apply-the-factor-to-the-hawks-echo"></a>
## Apply the Factor to the Hawk's Echo

**Example:** A stationary cliff reflects a wave with frequency $f_1$ toward a falcon that is flying toward the cliff at speed $v_o$. Write the echo frequency heard by the falcon.

**Explanation**

Track the return trip only:

| Stage | Role and change | Frequency after the stage |
|---|---|---|
| Reflection at the cliff | The cliff is stationary, so only the wave's direction changes. | $f_1$ |
| Reception by the falcon | The falcon is an observer moving toward the returning crests. | $\dfrac{v+v_o}{v}f_1$ |

The falcon moves toward the returning crests, so

$$
f_{\mathrm{echo}}=\frac{v+v_o}{v}f_1.
$$

The return-trip factor acts on the result of the preceding stage. The requested answer is in terms of the frequency already received by the reflector, so apply the factor to $f_1$ rather than returning to the falcon's original emitted frequency.

```quiz
type: radio
id: q-5
shuffle: true
content: |-
  Let $v$ denote the speed of sound.

  A hawk at the Grand Canyon produces a pure tone of frequency $f_0$ while flying at constant speed $v_o$ directly towards a climber on the canyon wall. The sound waves echo off the canyon wall and back to the hawk.

  Let your answer to the previous question be $f_1$. According to the hawk, what is the frequency of the hawk's echo off the canyon wall?
options:
- id: a
  content: |-
    $\dfrac{v+v_o}{v}f_1$
  correct: true
- id: b
  content: |-
    $\dfrac{v-v_o}{v}f_1$
- id: c
  content: |-
    $\dfrac{v}{v+v_o}f_1$
- id: d
  content: |-
    $\dfrac{v}{v-v_o}f_1$
```

---

<a id="summary"></a>
## Summary

When a sound reflects from a stationary wall and returns to a moving listener:

1. Keep the frequency unchanged at the reflection, so the returning wave has frequency $f_1$.
2. Identify the moving object on the return trip: the hawk is the observer.
3. For an observer moving toward the wave, use

   $$
   f_{\mathrm{echo}}=\frac{v+v_o}{v}f_1.
   $$

4. Check the result: $(v+v_o)/v>1$, which matches the higher frequency expected when the observer moves toward the crests.

The main trap is putting $v\pm v_o$ in the denominator, which would treat the hawk as a moving source instead of the moving observer it is on the return trip.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
