# Doppler Shift for a Moving Observer

<!--
lesson-id: 212-M5-028
topic-code: MTH212.M5.28
-->

## Table of Contents

- [Introduction](#introduction)
- [Decode the Reduced Cheat-Sheet Block](#decode-the-cheat-sheet-block)
- [Identify the Moving Observer Case](#identify-the-moving-observer-case)
- [Evaluate the Doppler Multiplier](#evaluate-the-doppler-multiplier)
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
f_{\mathrm{obs}}=f_0\left(1\pm\frac{v_o}{v}\right)
=f_0\left(\frac{v\pm v_o}{v}\right),
$$

where $f_0$ is the emitted frequency, $f_{\mathrm{obs}}$ is the observed frequency, $v$ is the speed of sound, and $v_o$ is the observer's speed along the line joining the observer and source.

Use the plus sign when the observer moves **toward** the source and the minus sign when the observer moves **away**. The recognition cue is that the listener moves while the sound-producing source stays fixed.

| Symbol | Meaning |
| --- | --- |
| $f_0$ (“$f$ naught”) | original frequency emitted by the source |
| $f_{\mathrm{obs}}$ (“$f$ prime”) | frequency heard by the moving observer |
| $v$ (“$c$ sub $s$”) | speed of sound through the medium; use $343\ \mathrm{m}/\mathrm{s}$ for ordinary air unless another value is given |
| $v_o$ | positive magnitude of the observer's line-of-sight speed relative to the medium |
| $v_s$ | positive magnitude of the source's line-of-sight speed relative to the medium |
| $\mathrm{LOS}$ | **line of sight**: the straight line joining source and observer |

---

<a id="decode-the-cheat-sheet-block"></a>
## Decode the Reduced Cheat-Sheet Block

The reduced sheet compresses all four one-moving-object Doppler cases into

$$
\mathrm{LOS},\ v_s<v:\qquad
\begin{array}{c|cc}
&\text{toward }(f_{\mathrm{obs}}>f_0)&\text{away }(f_{\mathrm{obs}}<f_0)\\
\mathrm O&f_{\mathrm{obs}}=f_0(1+v_o/v)&f_{\mathrm{obs}}=f_0(1-v_o/v)\\
\mathrm S&f_{\mathrm{obs}}=f_0/(1-v_s/v)&f_{\mathrm{obs}}=f_0/(1+v_s/v)
\end{array}.
$$

Read the shorthand as follows:

- $\mathrm{LOS}$ says to use motion **along the line of sight**. Motion perpendicular to that line does not make the source–observer distance close or open at that instant.
- $\mathrm O$ means the **observer moves** while the source is stationary. Use the observer row.
- $\mathrm S$ means the **source moves** while the observer is stationary. Use the source row.
- “Toward” means their separation is decreasing, so the heard frequency is higher: $f_{\mathrm{obs}}>f_0$.
- “Away” means their separation is increasing, so the heard frequency is lower: $f_{\mathrm{obs}}<f_0$.
- $v_s<v$ says these source formulas assume a source moving slower than sound.

This compact table assumes that only one party moves at a time. Choose the toward or away column separately; do not give $v_o$ or $v_s$ a negative value and then apply another sign from the table.

The location of the motion term tells you which row you are using:

$$
\boxed{
\begin{aligned}
\text{observer moves:}&\quad v_o\text{ appears in the numerator},\\
\text{source moves:}&\quad v_s\text{ appears in the denominator}.
\end{aligned}
}
$$

This lesson uses only the $\mathrm O$ row. Its two entries can also be written

$$
\begin{aligned}
\text{observer toward:}\quad
f_{\mathrm{obs}}&=f_0\left(1+\frac{v_o}{v}\right)
=f_0\left(\frac{v+v_o}{v}\right),\\
\text{observer away:}\quad
f_{\mathrm{obs}}&=f_0\left(1-\frac{v_o}{v}\right)
=f_0\left(\frac{v-v_o}{v}\right).
\end{aligned}
$$

The two notational forms are algebraically identical. The first matches the reduced cheat sheet; the second can be easier when substituting numerical speeds.

---

<a id="identify-the-moving-observer-case"></a>
## Identify the Moving Observer Case

Before substituting numbers, identify who produces the sound and who hears it. If the observer approaches a stationary source, wavefronts reach the observer more frequently, so the observed frequency must be higher than the emitted frequency.

**Example:** A stationary siren emits $500\ \mathrm{Hz}$. A cyclist moves toward it at $17\ \mathrm{m}/\mathrm{s}$. Use $340\ \mathrm{m}/\mathrm{s}$ for the speed of sound. Which setup gives the frequency heard by the cyclist?

**Explanation**

The cyclist is the moving observer, so $v_o=17\ \mathrm{m}/\mathrm{s}$. The cyclist approaches the siren, so use the plus sign:

$$
f_{\mathrm{obs}}=(500\ \mathrm{Hz})
\left(\frac{340+17}{340}\right).
$$

The source-moving Doppler formula is not appropriate because the siren is stationary.

```quiz
type: radio
id: problem-5-doppler-q1
content: |-
  A stationary tuning fork emits $680\ \mathrm{Hz}$. An observer moves toward it at $20\ \mathrm{m}/\mathrm{s}$ while sound travels at $340\ \mathrm{m}/\mathrm{s}$. Which expression gives the observed frequency?
options:
- id: a
  content: |-
    $\displaystyle 680\left(\frac{340+20}{340}\right)$
  correct: true
  feedback: |-
    A moving observer changes how quickly stationary-source wavefronts arrive. Because the observer moves toward the source, use the plus sign in the numerator: $f_{\mathrm{obs}}=680(340+20)/340$.
- id: b
  content: |-
    $\displaystyle 680\left(\frac{340-20}{340}\right)$
  feedback: |-
    The minus sign lowers the wavefront arrival rate and applies when the observer moves away. Here the observer approaches, so the numerator must be $v+v_o=340+20$.
- id: c
  content: |-
    $\displaystyle 680\left(\frac{340}{340-20}\right)$
  feedback: |-
    This puts the motion term in the denominator, which changes the wavefront spacing and is the moving-source structure. The source is stationary; observer motion changes the arrival rate through the numerator $(v+v_o)/v$.
- id: d
  content: |-
    $\displaystyle 680\left(\frac{340}{340+20}\right)$
  feedback: |-
    This uses a moving-source denominator even though the tuning fork is stationary. It also makes the factor less than $1$, contradicting the higher frequency heard by an approaching observer.
- id: e
  content: |-
    $\displaystyle 680\left(\frac{20}{340}\right)$
  feedback: |-
    This keeps only the fractional Doppler increase $v_o/v$ and discards the original emitted frequency contribution. The full observer factor is $1+v_o/v=(v+v_o)/v$.
```

---

<a id="evaluate-the-doppler-multiplier"></a>
## Evaluate the Doppler Multiplier

For an approaching observer, the multiplier

$$
1+\frac{v_o}{v}
=\frac{v+v_o}{v}
$$

is greater than $1$. Multiply the emitted frequency $f_0$ by this dimensionless Doppler multiplier.

Both $v$ and $v_o$ have units $\mathrm{m}/\mathrm{s}$, so $v_o/v$ is unitless. Therefore multiplying $f_0$ by the Doppler multiplier keeps the frequency unit $\mathrm{Hz}$. For approaching motion, a multiplier greater than $1$ provides a quick check before multiplication.

**Example:** A stationary source emits $720\ \mathrm{Hz}$. An observer approaches at $34\ \mathrm{m}/\mathrm{s}$, and the sound speed is $340\ \mathrm{m}/\mathrm{s}$. Find the observed frequency.

**Explanation**

Substitute all values before simplifying:

$$
\begin{aligned}
f_{\mathrm{obs}}
&=(720\ \mathrm{Hz})
\left(\frac{340+34}{340}\right)\\
&=(720\ \mathrm{Hz})(1.10)\\
&=792\ \mathrm{Hz}.
\end{aligned}
$$

Evaluate in the displayed order: add $v+v_o$, divide by $v$, and only then multiply by $f_0$. Keeping the numerator grouped prevents the motion term from being applied to the wrong part of the expression.

```quiz
type: radio
id: problem-5-doppler-q2
content: |-
  A stationary source emits $480\ \mathrm{Hz}$. An observer approaches it at $20\ \mathrm{m}/\mathrm{s}$. If sound travels at $320\ \mathrm{m}/\mathrm{s}$, what frequency does the observer hear?
options:
- id: a
  content: |-
    $30\ \mathrm{Hz}$
  feedback: |-
    This is only the added frequency, $480(20/320)=30\ \mathrm{Hz}$. The observer also hears the original $480\ \mathrm{Hz}$ contribution, so the total is $480+30=510\ \mathrm{Hz}$.
- id: b
  content: |-
    $450\ \mathrm{Hz}$
  feedback: |-
    This is the result for the minus sign: it predicts fewer wavefront arrivals than the source emits. An approaching observer meets wavefronts more quickly, so the frequency must exceed $480\ \mathrm{Hz}$ and equals $510\ \mathrm{Hz}$.
- id: c
  content: |-
    $480\ \mathrm{Hz}$
  feedback: |-
    This ignores the observer's motion. The observed and emitted frequencies match only when the radial observer speed is zero; here approaching motion raises the factor to $(320+20)/320$ and gives $510\ \mathrm{Hz}$.
- id: d
  content: |-
    $510\ \mathrm{Hz}$
  correct: true
  feedback: |-
    An approaching observer encounters wavefronts faster, so the observed frequency must exceed $480\ \mathrm{Hz}$. Using the moving-observer factor gives $f_{\mathrm{obs}}=480(320+20)/320=510\ \mathrm{Hz}$.
- id: e
  content: |-
    $544\ \mathrm{Hz}$
  feedback: |-
    The moving-observer factor is fixed by the given speeds: $(v+v_o)/v=(320+20)/320=1.0625$. Multiplying $480\ \mathrm{Hz}$ by that factor gives $510\ \mathrm{Hz}$, so $544\ \mathrm{Hz}$ does not satisfy the Doppler relation.
```

---

<a id="choose-the-sign-and-check-the-direction"></a>
## Choose the Sign and Check the Direction

The sign describes the observer's motion relative to the source:

$$
\begin{aligned}
\text{toward:}\quad
f_{\mathrm{obs}}&=f_0\left(1+\frac{v_o}{v}\right)>f_0,\\
\text{away:}\quad
f_{\mathrm{obs}}&=f_0\left(1-\frac{v_o}{v}\right)<f_0.
\end{aligned}
$$

This comparison catches a wrong sign before it becomes a final answer.

Use this decision sequence:

1. Identify whether the source or observer moves.
2. Decide whether the distance between them is closing or opening.
3. Choose the corresponding formula and sign.
4. Confirm the resulting factor predicts the correct increase or decrease.

**Example:** A stationary source emits $600\ \mathrm{Hz}$, and an observer moves toward it at $30\ \mathrm{m}/\mathrm{s}$. The sound speed is $330\ \mathrm{m}/\mathrm{s}$. Find $f_{\mathrm{obs}}$.

**Explanation**

Because the observer approaches, the answer must exceed $600\ \mathrm{Hz}$:

$$
f_{\mathrm{obs}}
=(600\ \mathrm{Hz})
\left(\frac{330+30}{330}\right)
=654.545\ldots\ \mathrm{Hz}.
$$

The minus sign would predict a lower frequency and contradict the motion.

```quiz
type: radio
id: problem-5-doppler-q3
content: |-
  A stationary speaker emits $750\ \mathrm{Hz}$. A listener moves toward it at $22\ \mathrm{m}/\mathrm{s}$ while sound travels at $330\ \mathrm{m}/\mathrm{s}$. Which value is the physically reasonable observed frequency?
options:
- id: a
  content: |-
    $50\ \mathrm{Hz}$
  feedback: |-
    This is only the extra wavefront-arrival rate, $750(22/330)=50\ \mathrm{Hz}$. The observed frequency includes the original $750\ \mathrm{Hz}$ plus that increase, giving $800\ \mathrm{Hz}$.
- id: b
  content: |-
    $700\ \mathrm{Hz}$
  feedback: |-
    This uses $v-v_o$, which lowers the frequency for a listener moving away. Here the listener approaches and encounters wavefronts faster, so $f_{\mathrm{obs}}$ must exceed $750\ \mathrm{Hz}$ and equals $800\ \mathrm{Hz}$.
- id: c
  content: |-
    $750\ \mathrm{Hz}$
  feedback: |-
    This is the no-radial-motion result. Since the listener approaches at $22\ \mathrm{m}/\mathrm{s}$, wavefronts arrive more frequently and the observed frequency rises to $750(330+22)/330=800\ \mathrm{Hz}$.
- id: d
  content: |-
    $800\ \mathrm{Hz}$
  correct: true
  feedback: |-
    An approaching observer meets the source's wavefronts more rapidly, so the observed frequency must be higher than $750\ \mathrm{Hz}$. The factor $(330+22)/330$ gives $f_{\mathrm{obs}}=800\ \mathrm{Hz}$.
- id: e
  content: |-
    $11\,250\ \mathrm{Hz}$
  feedback: |-
    This multiplies by $v/v_o=15$, but that ratio is not the wavefront-arrival factor. Observer motion modifies the emitted frequency by the near-unity factor $(v+v_o)/v=352/330$, giving $800\ \mathrm{Hz}$.
```

---

<a id="match-the-number-only-answer-form"></a>
## Match the Number-Only Answer Form

Keep extra digits through the calculation, apply the required precision at the end, and omit the unit only when the answer field explicitly requests a number.

**Example:** A singer produces an $880\ \mathrm{Hz}$ note. A bat flies toward the singer at $35\ \mathrm{m}/\mathrm{s}$. What frequency does the bat hear? Use $343\ \mathrm{m}/\mathrm{s}$ for the speed of sound.

Enter the frequency in hertz as a number only.

**Explanation**

The bat is the moving observer and approaches the stationary singer:

$$
\begin{aligned}
f_{\mathrm{obs}}
&=f_0\left(1+\frac{v_o}{v}\right)\\
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
  A stationary source emits $600\ \mathrm{Hz}$. An observer moves toward it at $34\ \mathrm{m}/\mathrm{s}$, and sound travels at $340\ \mathrm{m}/\mathrm{s}$. The answer field accepts the frequency in hertz as a number only. Which number should be entered?
options:
- id: a
  content: |-
    $60$
  feedback: |-
    This is only the Doppler increase $600(34/340)=60\ \mathrm{Hz}$. The full observed frequency includes the emitted $600\ \mathrm{Hz}$, so it is $660\ \mathrm{Hz}$.
- id: b
  content: |-
    $540$
  feedback: |-
    This uses $v-v_o$, which describes an observer moving away and produces a lower frequency. The observer moves toward the source, so wavefronts arrive faster and the result must be above $600\ \mathrm{Hz}$: $660\ \mathrm{Hz}$.
- id: c
  content: |-
    $600$
  feedback: |-
    This assumes zero radial observer speed. Here the observer approaches, so the multiplier is $(340+34)/340=1.10>1$ and the observed frequency is $660\ \mathrm{Hz}$.
- id: d
  content: |-
    $660$
  correct: true
  feedback: |-
    Approaching motion increases the wavefront arrival rate, so use the plus sign: $f_{\mathrm{obs}}=600(340+34)/340=660\ \mathrm{Hz}$. Because the field requests a number only, enter $660$.
- id: e
  content: |-
    $6000$
  feedback: |-
    This multiplies by $v/v_o=10$, which is not the moving-observer factor. The correct near-unity factor is $(v+v_o)/v=(340+34)/340=1.10$, giving the entry $660$.
```

---

<a id="summary"></a>
## Summary

For a stationary sound source and a moving observer:

1. Label $f_0$ as the emitted frequency, $f_{\mathrm{obs}}$ as the heard frequency, $v$ as sound speed, and $v_o$ as the positive line-of-sight observer speed.
2. Use
   $$
   f_{\mathrm{obs}}=f_0\left(1\pm\frac{v_o}{v}\right).
   $$
3. Choose plus for motion toward the source and minus for motion away.
4. Evaluate the unitless factor $1\pm v_o/v$ before multiplying by $f_0$.
5. Check the direction: toward means $f_{\mathrm{obs}}>f_0$; away means $f_{\mathrm{obs}}<f_0$.
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
