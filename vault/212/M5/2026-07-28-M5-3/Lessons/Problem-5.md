# Doppler Shift for a Moving Observer

<!--
lesson-id: 212-M5-028
topic-code: MTH212.M5.28
-->

## Table of Contents

- [Introduction](#introduction)
- [Identify the Moving Observer Case](#identify-the-moving-observer-case)
- [Evaluate the Frequency Factor](#evaluate-the-frequency-factor)
- [Choose the Sign and Check the Direction](#choose-the-sign-and-check-the-direction)
- [Match the Number-Only Answer Form](#match-the-number-only-answer-form)
- [Summary](#summary)

## Prerequisites

- Distinguish the source of a sound from the observer who hears it.
- Substitute values into a fraction and evaluate parentheses first.
- Round a final measured result to the required significant figures.

---

<a id="introduction"></a>
## Introduction

When a sound source is stationary and the **observer** moves through the sound wave, use

$$
f'=f\left(\frac{v\pm v_o}{v}\right),
$$

where $f$ is the emitted frequency, $f'$ is the observed frequency, $v$ is the speed of sound, and $v_o$ is the observer's speed.

Use the plus sign when the observer moves **toward** the source and the minus sign when the observer moves **away**. The recognition cue is that the listener moves while the sound-producing source stays fixed.

| Symbol | Meaning |
| --- | --- |
| $f$ | frequency emitted by the stationary source |
| $f'$ | frequency heard by the moving observer |
| $v$ | speed of sound through the medium |
| $v_o$ | observer's speed relative to the medium |

---

<a id="identify-the-moving-observer-case"></a>
## Identify the Moving Observer Case

Before substituting numbers, identify who produces the sound and who hears it. If the observer approaches a stationary source, wavefronts reach the observer more frequently, so the observed frequency must be higher than the emitted frequency.

**Example:** A stationary siren emits $500\ \mathrm{Hz}$. A cyclist moves toward it at $17\ \mathrm{m/s}$. Use $340\ \mathrm{m/s}$ for the speed of sound. Which setup gives the frequency heard by the cyclist?

**Explanation**

The cyclist is the moving observer, so $v_o=17\ \mathrm{m/s}$. The cyclist approaches the siren, so use the plus sign:

$$
f'=(500\ \mathrm{Hz})
\left(\frac{340+17}{340}\right).
$$

The source-moving Doppler formula is not appropriate because the siren is stationary.

```quiz
type: radio
id: problem-5-doppler-q1
content: |-
  A stationary tuning fork emits $680\ \mathrm{Hz}$. An observer moves toward it at $20\ \mathrm{m/s}$ while sound travels at $340\ \mathrm{m/s}$. Which expression gives the observed frequency?
options:
- id: a
  content: |-
    $\displaystyle 680\left(\frac{340+20}{340}\right)$
  correct: true
  feedback: |-
    The observer moves toward a stationary source, so use $f'=f(v+v_o)/v$.
- id: b
  content: |-
    $\displaystyle 680\left(\frac{340-20}{340}\right)$
  feedback: |-
    The minus sign describes an observer moving away, not toward.
- id: c
  content: |-
    $\displaystyle 680\left(\frac{340}{340-20}\right)$
  feedback: |-
    Putting the motion term in the denominator is the structure for a moving source. Here the source is stationary.
- id: d
  content: |-
    $\displaystyle 680\left(\frac{340}{340+20}\right)$
  feedback: |-
    This is a moving-source structure and also predicts a lower frequency for approaching motion.
- id: e
  content: |-
    $\displaystyle 680\left(\frac{20}{340}\right)$
  feedback: |-
    The observer-speed fraction modifies $1$; the required factor is $1+v_o/v$.
```

---

<a id="evaluate-the-frequency-factor"></a>
## Evaluate the Frequency Factor

For an approaching observer, the multiplier

$$
\frac{v+v_o}{v}
=1+\frac{v_o}{v}
$$

is greater than $1$. Multiply the emitted frequency by this factor.

Call this multiplier the frequency factor $M$:

$$
M=\frac{v+v_o}{v}.
$$

Both $v$ and $v_o$ have units $\mathrm{m/s}$, so $M$ is unitless. Therefore $f'=fM$ keeps the frequency unit $\mathrm{Hz}$. For approaching motion, $M>1$ provides a quick check before multiplication.

**Example:** A stationary source emits $720\ \mathrm{Hz}$. An observer approaches at $34\ \mathrm{m/s}$, and the sound speed is $340\ \mathrm{m/s}$. Find the observed frequency.

**Explanation**

Substitute all values before simplifying:

$$
\begin{aligned}
f'
&=(720\ \mathrm{Hz})
\left(\frac{340+34}{340}\right)\\
&=(720\ \mathrm{Hz})(1.10)\\
&=792\ \mathrm{Hz}.
\end{aligned}
$$

Evaluate in the displayed order: add $v+v_o$, divide by $v$, and only then multiply by $f$. Keeping the numerator grouped prevents the motion term from being applied to the wrong part of the expression.

```quiz
type: radio
id: problem-5-doppler-q2
content: |-
  A stationary source emits $480\ \mathrm{Hz}$. An observer approaches it at $20\ \mathrm{m/s}$. If sound travels at $320\ \mathrm{m/s}$, what frequency does the observer hear?
options:
- id: a
  content: |-
    $30\ \mathrm{Hz}$
  feedback: |-
    This is only the size of the frequency increase, not the total observed frequency.
- id: b
  content: |-
    $450\ \mathrm{Hz}$
  feedback: |-
    This is below the emitted frequency and therefore contradicts approaching motion.
- id: c
  content: |-
    $480\ \mathrm{Hz}$
  feedback: |-
    The observer hears the emitted frequency only when $v_o=0$.
- id: d
  content: |-
    $510\ \mathrm{Hz}$
  correct: true
  feedback: |-
    $f'=480(320+20)/320=480(1.0625)=510\ \mathrm{Hz}$.
- id: e
  content: |-
    $544\ \mathrm{Hz}$
  feedback: |-
    This does not result from the grouped factor $(v+v_o)/v$.
```

---

<a id="choose-the-sign-and-check-the-direction"></a>
## Choose the Sign and Check the Direction

The sign describes the observer's motion relative to the source:

$$
\begin{aligned}
\text{toward:}\quad
f'&=f\left(\frac{v+v_o}{v}\right)>f,\\
\text{away:}\quad
f'&=f\left(\frac{v-v_o}{v}\right)<f.
\end{aligned}
$$

This comparison catches a wrong sign before it becomes a final answer.

Use this decision sequence:

1. Identify whether the source or observer moves.
2. Decide whether the distance between them is closing or opening.
3. Choose the corresponding formula and sign.
4. Confirm the resulting factor predicts the correct increase or decrease.

**Example:** A stationary source emits $600\ \mathrm{Hz}$, and an observer moves toward it at $30\ \mathrm{m/s}$. The sound speed is $330\ \mathrm{m/s}$. Find $f'$.

**Explanation**

Because the observer approaches, the answer must exceed $600\ \mathrm{Hz}$:

$$
f'
=(600\ \mathrm{Hz})
\left(\frac{330+30}{330}\right)
=654.545\ldots\ \mathrm{Hz}.
$$

The minus sign would predict a lower frequency and contradict the motion.

```quiz
type: radio
id: problem-5-doppler-q3
content: |-
  A stationary speaker emits $750\ \mathrm{Hz}$. A listener moves toward it at $22\ \mathrm{m/s}$ while sound travels at $330\ \mathrm{m/s}$. Which value is the physically reasonable observed frequency?
options:
- id: a
  content: |-
    $50\ \mathrm{Hz}$
  feedback: |-
    This is only the Doppler increase, $750(22/330)=50\ \mathrm{Hz}$. The observed frequency is the emitted $750\ \mathrm{Hz}$ plus that increase.
- id: b
  content: |-
    $700\ \mathrm{Hz}$
  feedback: |-
    This uses the minus sign, $750(330-22)/330$, which describes a listener moving away. An approaching listener must hear a frequency above $750\ \mathrm{Hz}$.
- id: c
  content: |-
    $750\ \mathrm{Hz}$
  feedback: |-
    This assumes no observer motion. Since the listener approaches at $22\ \mathrm{m/s}$, the arrival rate of wavefronts increases.
- id: d
  content: |-
    $800\ \mathrm{Hz}$
  correct: true
  feedback: |-
    $f'=750(330+22)/330=800\ \mathrm{Hz}$, which is greater than the emitted frequency as an approaching observer requires.
- id: e
  content: |-
    $11\,250\ \mathrm{Hz}$
  feedback: |-
    This inverts the speed ratio and multiplies by $v/v_o=15$. Observer motion modifies the frequency by the near-unity factor $(v+v_o)/v$, not by $v/v_o$.
```

---

<a id="match-the-number-only-answer-form"></a>
## Match the Number-Only Answer Form

Keep extra digits through the calculation, apply the required precision at the end, and omit the unit only when the answer field explicitly requests a number.

**Example:** A singer produces an $880\ \mathrm{Hz}$ note. A bat flies toward the singer at $35\ \mathrm{m/s}$. What frequency does the bat hear? Use $343\ \mathrm{m/s}$ for the speed of sound.

Enter the frequency in hertz as a number only.

**Explanation**

The bat is the moving observer and approaches the stationary singer:

$$
\begin{aligned}
f'
&=f\left(\frac{v+v_o}{v}\right)\\
&=(880\ \mathrm{Hz})
\left(\frac{343+35}{343}\right)\\
&=969.8\ldots\ \mathrm{Hz}.
\end{aligned}
$$

The limiting measured speed has two significant figures, so the result is $9.7\times10^2\ \mathrm{Hz}$. Enter $970$.

```quiz
type: radio
id: problem-5-doppler-q4
content: |-
  A stationary source emits $600\ \mathrm{Hz}$. An observer moves toward it at $34\ \mathrm{m/s}$, and sound travels at $340\ \mathrm{m/s}$. The answer field accepts the frequency in hertz as a number only. Which number should be entered?
options:
- id: a
  content: |-
    $60$
  feedback: |-
    This is only the increase $600(34/340)=60\ \mathrm{Hz}$. Add it to the emitted frequency, or evaluate the full factor $(340+34)/340$.
- id: b
  content: |-
    $540$
  feedback: |-
    This uses $v-v_o$ and therefore models an observer moving away. Toward motion requires the plus sign and a result above $600\ \mathrm{Hz}$.
- id: c
  content: |-
    $600$
  feedback: |-
    This ignores the observer's motion. A nonzero approaching speed makes the multiplier greater than $1$.
- id: d
  content: |-
    $660$
  correct: true
  feedback: |-
    $f'=600(340+34)/340=660\ \mathrm{Hz}$, so enter $660$.
- id: e
  content: |-
    $6000$
  feedback: |-
    This multiplies by the inverted ratio $v/v_o=10$. The correct dimensionless factor is $(v+v_o)/v=1.10$.
```

---

<a id="summary"></a>
## Summary

For a stationary sound source and a moving observer:

1. Label $f$ as the emitted frequency, $f'$ as the heard frequency, $v$ as sound speed, and $v_o$ as observer speed.
2. Use
   $$
   f'=f\left(\frac{v\pm v_o}{v}\right).
   $$
3. Choose plus for motion toward the source and minus for motion away.
4. Evaluate the unitless factor $(v\pm v_o)/v$ before multiplying by $f$.
5. Check the direction: toward means $f'>f$; away means $f'<f$.
6. Round only the final frequency and follow the requested answer format.

The main traps are treating observer motion as source motion, choosing the wrong sign, and rounding before the final step.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Extreme Doppler Frequencies from a Rotating Source](../../2026-08-02-PQ-3/Lessons/Problem-5.md)

Study guide index: 19/28

---
<!-- lesson-nav:end -->
