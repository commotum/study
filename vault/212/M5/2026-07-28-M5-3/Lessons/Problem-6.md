# Choosing Source Motion for a Doppler Shift

## Table of Contents

- [Introduction](#introduction)
- [Compare the Two Frequencies First](#compare-the-two-frequencies-first)
- [Match the Shift to the Source's Direction](#match-the-shift-to-the-sources-direction)
- [Explain the Shift With Wavefront Spacing](#explain-the-shift-with-wavefront-spacing)
- [Keep Frequency Separate From Loudness](#keep-frequency-separate-from-loudness)
- [Apply the Rule to the Bat](#apply-the-rule-to-the-bat)
- [Summary](#summary)

## Prerequisites

- Compare two frequencies written in the same unit.
- Recognize that a higher frequency means a higher pitch and a lower frequency means a lower pitch.
- Recognize wavefront spacing as wavelength.

---

<a id="introduction"></a>
## Introduction

When a moving sound source must produce a particular heard frequency, compare the target heard frequency $f'$ with the emitted frequency $f_s$ before choosing a direction.

- If $f'>f_s$, the listener needs an **upshift**, so the source must move **toward** the listener.
- If $f'<f_s$, the listener needs a **downshift**, so the source must move **away from** the listener.
- If $f'=f_s$, no Doppler shift is required.

This lesson assumes the listener is stationary and the sound source is the object whose direction must be chosen.

| Frequency comparison | Required shift | Source motion |
|---|---|---|
| $f'>f_s$ | Upshift | Toward the listener |
| $f'<f_s$ | Downshift | Away from the listener |
| $f'=f_s$ | No shift | No relative source motion is needed |

---

<a id="compare-the-two-frequencies-first"></a>
## Compare the Two Frequencies First

**Example:** A buzzer emits $18\ \mathrm{kHz}$, but a stationary listener needs to hear $15\ \mathrm{kHz}$. Is an upshift or a downshift required?

**Explanation**

Write the comparison directly:

$$
f'=15\ \mathrm{kHz}<18\ \mathrm{kHz}=f_s.
$$

The heard frequency must be lower than the emitted frequency, so a **downshift** is required. Do this comparison before thinking about the direction of motion.

```quiz
type: radio
id: problem-6-compare-q1
content: |-
  A sound source emits $30\ \mathrm{kHz}$, and the target heard frequency is $24\ \mathrm{kHz}$. What kind of frequency shift is required?
options:
- id: a
  content: |-
    An upshift
  feedback: |-
    An upshift would make the heard frequency greater than $30\ \mathrm{kHz}$.
- id: b
  content: |-
    A downshift
  correct: true
  feedback: |-
    Since $24\ \mathrm{kHz}<30\ \mathrm{kHz}$, the heard frequency must decrease.
- id: c
  content: |-
    No shift
  feedback: |-
    The target and emitted frequencies are not equal.
```

---

<a id="match-the-shift-to-the-sources-direction"></a>
## Match the Shift to the Source's Direction

**Example:** A horn emits $400\ \mathrm{Hz}$. A stationary listener must hear a frequency below $400\ \mathrm{Hz}$. Should the horn move toward or away from the listener?

**Explanation**

The requested heard frequency is below the emitted frequency, so the sound needs a downshift. For a moving source and stationary listener:

$$
\text{downshift}\longrightarrow\text{source moves away}.
$$

The horn must move away from the listener.

**Watch Out!** “Away from the listener” describes the source's motion. Sound emitted behind the receding source still travels back to the listener; those wavefronts are simply farther apart.

```quiz
type: radio
id: problem-6-direction-q1
content: |-
  A whistle emits $500\ \mathrm{Hz}$, but a stationary listener must hear $540\ \mathrm{Hz}$. Which source motion produces the required shift?
options:
- id: a
  content: |-
    The whistle moves toward the listener.
  correct: true
  feedback: |-
    The target frequency is higher, and an approaching source produces an upshift.
- id: b
  content: |-
    The whistle moves away from the listener.
  feedback: |-
    A receding source produces a downshift, but $540\ \mathrm{Hz}$ is above $500\ \mathrm{Hz}$.
- id: c
  content: |-
    The whistle remains stationary.
  feedback: |-
    A stationary source would not produce the required Doppler shift.
```

---

<a id="explain-the-shift-with-wavefront-spacing"></a>
## Explain the Shift With Wavefront Spacing

**Example:** Why does a source moving away from a stationary listener produce a lower heard frequency?

**Explanation**

As the source recedes, each new wavefront is emitted farther from the listener than the previous one. The wavefronts traveling back toward the listener are spread farther apart, so their wavelength is longer.

For a fixed sound speed $v$ in the air,

$$
f'=\frac{v}{\lambda'}.
$$

A longer observed wavelength $\lambda'$ produces a lower observed frequency $f'$. Thus,

$$
\text{source moves away}
\longrightarrow
\text{wavefronts spread out}
\longrightarrow
\lambda'\text{ increases}
\longrightarrow
f'\text{ decreases}.
$$

```quiz
type: radio
id: problem-6-wavefront-q1
content: |-
  Which explanation correctly describes the sound from a source moving toward a stationary listener?
options:
- id: a
  content: |-
    The wavefronts are compressed, so the listener hears a higher frequency.
  correct: true
  feedback: |-
    A shorter wavelength at the same sound speed corresponds to a higher frequency.
- id: b
  content: |-
    The wavefronts are spread out, so the listener hears a higher frequency.
  feedback: |-
    Spread-out wavefronts have a longer wavelength and produce a lower frequency.
- id: c
  content: |-
    The wavefront spacing is unchanged, so the listener hears a lower frequency.
  feedback: |-
    A moving source changes the wavefront spacing in front of and behind it.
```

---

<a id="keep-frequency-separate-from-loudness"></a>
## Keep Frequency Separate From Loudness

**Example:** A source moves away and becomes quieter. Is becoming quieter the reason its heard frequency decreases?

**Explanation**

No. Loudness is related to sound intensity, while pitch is related to frequency. The Doppler downshift occurs because receding motion stretches the spacing of the wavefronts that reach the listener.

When the question asks about a value in $\mathrm{kHz}$, it is asking about frequency. Compare the frequency values and ignore changes in loudness.

```quiz
type: radio
id: problem-6-pitch-q1
content: |-
  A siren must shift from $22\ \mathrm{kHz}$ to $19\ \mathrm{kHz}$ for a stationary listener. Which reasoning is relevant?
options:
- id: a
  content: |-
    The sound must become quieter, so the source should move away.
  feedback: |-
    The question specifies frequency, not intensity or loudness.
- id: b
  content: |-
    The heard frequency must decrease, so the source should move away.
  correct: true
  feedback: |-
    Since $19\ \mathrm{kHz}<22\ \mathrm{kHz}$, a Doppler downshift is required.
- id: c
  content: |-
    The heard frequency must increase, so the source should move toward the listener.
  feedback: |-
    The target $19\ \mathrm{kHz}$ is lower than the emitted $22\ \mathrm{kHz}$.
```

---

<a id="apply-the-rule-to-the-bat"></a>
## Apply the Rule to the Bat

**Example:** A bat chirps at $25\ \mathrm{kHz}$. To hear the chirp at the upper threshold of human hearing, $20\ \mathrm{kHz}$, would the bat need to fly toward you or away from you? Explain.

**Explanation**

First translate the words into labeled quantities:

| Quantity | Value |
|---|---:|
| Emitted frequency | $f_s=25\ \mathrm{kHz}$ |
| Target heard frequency | $f'=20\ \mathrm{kHz}$ |

Now compare the target heard frequency with the emitted frequency:

$$
20\ \mathrm{kHz}<25\ \mathrm{kHz}.
$$

The frequency must decrease. A source moving away from an observer lowers the observed frequency, so the bat must fly away from you.

The full decision chain is

$$
20\ \mathrm{kHz}<25\ \mathrm{kHz}
\longrightarrow
f'<f_s
\longrightarrow
\text{downshift}
\longrightarrow
\text{away from you}.
$$

```quiz
type: radio
id: m5-3lec-q5
shuffle: true
content: |-
  **Question 5**

  A bat chirps at $25\ \mathrm{kHz}$. To hear the chirp at the upper threshold of human hearing, $20\ \mathrm{kHz}$, would the bat need to fly toward you or away from you? Explain.
options:
- id: a
  content: Toward you
  feedback: A source moving toward an observer raises the observed frequency, but the frequency must decrease from $25\ \mathrm{kHz}$ to $20\ \mathrm{kHz}$.
- id: b
  content: Away from you
  correct: true
  feedback: A source moving away from an observer lowers the observed frequency, which is required to shift $25\ \mathrm{kHz}$ down to $20\ \mathrm{kHz}$.
```

---

<a id="summary"></a>
## Summary

Use this decision routine for a moving source and stationary listener:

1. Label the emitted frequency $f_s$ and target heard frequency $f'$.
2. Compare them before choosing a direction.
3. If $f'>f_s$, choose **toward** for an upshift.
4. If $f'<f_s$, choose **away** for a downshift.
5. Explain the choice with wavefront spacing: compressed means higher frequency; spread out means lower frequency.

The main traps are reversing the direction rule and confusing a change in frequency with a change in loudness.
