# Tuning Resonance with Water Glasses

<!--
lesson-id: 212-M5-057
topic-code: MTH212.M5.57
-->

## Table of Contents

- [Introduction](#introduction)
- [Excite a Natural Vibration](#excite-a-natural-vibration)
- [Connect Resonant Frequency to Pitch](#connect-resonant-frequency-to-pitch)
- [Tune the Frequency with Water](#tune-the-frequency-with-water)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Distinguish frequency, which controls pitch, from amplitude, which affects loudness.
- Recognize resonance as a large response when a repeated drive excites a natural vibration mode.
- Use the qualitative oscillator model $f_n\propto\sqrt{k_{\mathrm{eff}}/m_{\mathrm{eff}}}$.
- Compare two systems while holding their other physical properties fixed.

---

<a id="introduction"></a>
## Introduction

A wine glass can act as a musical oscillator. Rubbing a wet finger around its rim creates a repeated frictional drive, the glass responds strongly in one of its natural vibration modes, and the vibration pushes on the air to make sound.

The source associates this demonstration with the problem:

![[../Source/Images/image-4.jpg]]

[Video source](https://www.youtube.com/watch?v=Rlk59xdM_YY)

The reusable explanation is a four-link chain:

$$
\text{wet-finger stick--slip}
\longrightarrow
\text{periodic driving force}
\longrightarrow
\text{glass resonance}
\longrightarrow
\text{sound at a natural frequency}.
$$

Adding water changes the vibrating system's effective inertia. That shifts its natural frequency, so glasses with different water levels can be tuned to different pitches and used to play a melody.

---

<a id="excite-a-natural-vibration"></a>
## Excite a Natural Vibration

**Example:** Explain why steadily sliding a wet finger around a glass rim can produce a sustained tone.

**Explanation**

The finger does not slide perfectly smoothly. Friction makes it alternately stick to the rim and slip forward. Each stick--slip cycle exerts another small tangential force on the glass.

This repeated force supplies energy to a natural vibration mode of the glass. When the timing reinforces that mode, resonance builds an audible vibration. The glass then pushes and pulls on the surrounding air, producing the sustained sound.

The water does not create this repeated drive. The wet finger supplies the drive; the glass is the resonating object.

```quiz
type: radio
id: water-glass-stick-slip-resonance
shuffle: true
content: |-
  Why can rubbing a wet finger steadily around a wine-glass rim produce a sustained tone?
options:
- id: repeated-drive-excites-mode
  content: |-
    Stick--slip friction creates a repeated force that supplies energy to a natural vibration mode of the glass.
  correct: true
  feedback: |-
    A wet finger alternately sticks and slips at the rim, creating a periodic drive. That drive reinforces a natural mode of the glass, so resonance produces a sustained audible vibration.
- id: smooth-slide-no-vibration
  content: |-
    The finger slides without changing force, and the steady force alone becomes a sound wave.
  feedback: |-
    A perfectly steady force would mainly deform the glass rather than sustain an oscillation. The changing force from repeated sticking and slipping supplies energy cycle after cycle to the resonant vibration.
- id: water-splashes-at-pitch
  content: |-
    The water repeatedly splashes the glass at the tone's frequency.
  feedback: |-
    Water affects the tuned system, but splashing is not the sustained drive in this demonstration. The wet finger's stick--slip friction repeatedly forces the glass rim and excites its natural vibration.
- id: finger-is-sound-source-only
  content: |-
    The finger itself vibrates the air at the musical pitch while the glass only makes that sound louder.
  feedback: |-
    The finger provides energy, but the resonating glass selects the strong vibration frequency and radiates the tone. The glass is not merely an amplifier for a pitch already produced by the finger.
- id: beats-create-single-tone
  content: |-
    Two slightly different glass frequencies interfere, and their beat frequency is the sustained pitch of one glass.
  feedback: |-
    Beats require two nearby frequencies and describe a periodic change in loudness. One rubbed glass can sustain a tone because a periodic drive excites its own natural vibration mode.
```

---

<a id="connect-resonant-frequency-to-pitch"></a>
## Connect Resonant Frequency to Pitch

**Example:** Two glasses resonate at $440\ \mathrm{Hz}$ and $523\ \mathrm{Hz}$. Which one has the higher pitch?

**Explanation**

Pitch follows frequency directly: more vibration cycles per second are heard as a higher pitch. Since

$$
523\ \mathrm{Hz}>440\ \mathrm{Hz},
$$

the $523\ \mathrm{Hz}$ glass has the higher pitch.

Amplitude has a different role. A larger vibration amplitude usually sounds louder, but it does not by itself change the note's pitch.

```quiz
type: radio
id: water-glass-frequency-and-pitch
shuffle: true
content: |-
  Glass A resonates at $392\ \mathrm{Hz}$ and glass B resonates at $494\ \mathrm{Hz}$. Which comparison is correct?
options:
- id: b-higher-pitch
  content: |-
    Glass B has the higher pitch because its resonant frequency is higher.
  correct: true
  feedback: |-
    Pitch increases directly with sound frequency. Since $494\ \mathrm{Hz}>392\ \mathrm{Hz}$, glass B completes more vibration cycles each second and has the higher pitch.
- id: a-higher-pitch
  content: |-
    Glass A has the higher pitch because its resonant frequency is lower.
  feedback: |-
    A lower frequency means fewer cycles per second and therefore a lower pitch. Since glass A resonates at $392\ \mathrm{Hz}$, its pitch is below glass B's $494\ \mathrm{Hz}$ pitch.
- id: same-pitch-different-loudness
  content: |-
    The glasses have the same pitch; the frequencies only determine loudness.
  feedback: |-
    Frequency determines pitch, whereas vibration amplitude is the quantity most directly associated with loudness. Different resonant frequencies therefore produce different pitches.
- id: cannot-compare-without-amplitude
  content: |-
    Their pitches cannot be compared without knowing their amplitudes.
  feedback: |-
    Amplitude is useful for comparing loudness, not pitch. The given frequencies alone settle the pitch order: $494\ \mathrm{Hz}$ is higher than $392\ \mathrm{Hz}$.
- id: beat-frequency-is-pitch
  content: |-
    Both glasses have pitch $102\ \mathrm{Hz}$ because that is the difference between their frequencies.
  feedback: |-
    The difference $494-392=102\ \mathrm{Hz}$ would describe a beat rate only when both tones overlap, not the pitch of either glass. Each glass's pitch follows its own resonant frequency.
```

---

<a id="tune-the-frequency-with-water"></a>
## Tune the Frequency with Water

**Example:** Two otherwise identical glasses are rubbed in the same way. One contains more water. Predict how its pitch compares with the glass containing less water.

**Explanation**

The vibrating glass must move some of the water next to its wall. Adding water therefore increases the coupled system's effective inertia. A useful qualitative model is

$$
f_n\approx\frac{1}{2\pi}
\sqrt{\frac{k_{\mathrm{eff}}}{m_{\mathrm{eff}}}}.
$$

For otherwise identical glasses, treat the effective stiffness as approximately fixed. Increasing $m_{\mathrm{eff}}$ then decreases $f_n$:

$$
\text{more water}
\longrightarrow
\text{more effective inertia}
\longrightarrow
\text{lower natural frequency}
\longrightarrow
\text{lower pitch}.
$$

Different water amounts therefore tune the glasses to different notes. The water changes the pitch; it is not merely changing the loudness of one unchanged note.

```quiz
type: radio
id: water-glass-more-water-pitch
shuffle: true
content: |-
  Two otherwise identical wine glasses are rubbed around their rims. Glass A contains more water than glass B. What should happen to glass A's natural frequency and pitch?
options:
- id: lower-frequency-lower-pitch
  content: |-
    Glass A has a lower natural frequency and a lower pitch.
  correct: true
  feedback: |-
    More water increases the effective inertia coupled to the vibrating glass. With the glass's effective stiffness approximately fixed, $f_n\propto1/\sqrt{m_{\mathrm{eff}}}$, so glass A has the lower frequency and pitch.
- id: higher-frequency-higher-pitch
  content: |-
    Glass A has a higher natural frequency and a higher pitch.
  feedback: |-
    This reverses the inertia dependence. Added water makes more mass participate in the motion, and greater effective inertia lowers rather than raises the natural frequency and pitch.
- id: same-frequency-louder
  content: |-
    Glass A has the same natural frequency but sounds louder.
  feedback: |-
    Loudness depends mainly on vibration amplitude, but changing the water level changes the vibrating system itself. The extra coupled inertia shifts its natural frequency downward instead of preserving the same note.
- id: lower-frequency-higher-pitch
  content: |-
    Glass A has a lower natural frequency but a higher pitch.
  feedback: |-
    The predicted frequency change is correct, but pitch follows frequency in the same direction. A lower natural frequency produces a lower, not higher, perceived pitch.
- id: water-only-resonates
  content: |-
    The glass keeps the same pitch because only the water's surface resonates.
  feedback: |-
    The tone comes from a natural vibration of the glass coupled to the water. Because the glass must move nearby water, changing the water amount changes the mode's effective inertia and tunes its pitch.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Answer the source question in its original open-response form before using the multiple-choice check.

> How can a performer make music using wine glasses and different amounts of water?

The answer form calls for a causal explanation, not just the claim that different water levels make different notes.

**Explanation**

A performer rubs a wet finger around each glass rim. Repeated stick--slip friction supplies a periodic force that excites a resonant vibration of the glass. The vibrating glass then produces a sustained sound.

Changing the amount of water changes the effective inertia coupled to each glass and therefore shifts its natural frequency. More water generally lowers the frequency and pitch for otherwise identical glasses. By choosing different water levels, the performer tunes the glasses to different pitches and plays them in sequence to make music.

```quiz
type: radio
id: khadley-wave-beats-q1
shuffle: true
content: |-
  Which explanation correctly answers how a performer can make music using wine glasses and different amounts of water?
options:
- id: stick-slip-resonance-water-tuning
  content: |-
    A wet finger provides a repeated stick--slip drive that excites a glass resonance. Different water amounts change the effective inertia and natural frequency, tuning the glasses to different pitches.
  correct: true
  feedback: |-
    The wet finger supplies a periodic force, resonance sustains a natural vibration of the glass, and the water level changes the coupled inertia. Those frequency shifts tune the glasses to different pitches that can be played as music.
- id: water-amplifies-same-note
  content: |-
    Rubbing excites each glass, while adding water only amplifies the same pitch so the notes become loud enough to form music.
  feedback: |-
    Rubbing does excite the glass, but water is not merely an amplitude control. Changing the water amount changes the system's effective inertia and natural frequency, so the glasses produce different pitches rather than louder versions of one note.
- id: blow-across-air-columns
  content: |-
    The performer blows across every rim, and different water levels tune the lengths of air columns while rim friction plays no role.
  feedback: |-
    Blowing across a container can excite an air resonance, but that is a different technique. In the source demonstration, a wet finger's stick--slip friction drives a vibration of the glass, and water tunes that glass--water system.
- id: beats-are-melody
  content: |-
    Every glass keeps the same natural frequency, but pairs of glasses create different beat frequencies that are heard as the melody.
  feedback: |-
    Beats are slow amplitude modulations produced by two nearby frequencies; they do not replace the individual musical pitches. Different water levels tune the glasses' natural frequencies so the performer has distinct notes to play.
- id: finger-sets-each-pitch
  content: |-
    The performer changes finger speed to impose each musical frequency, while the water only keeps the glasses from moving.
  feedback: |-
    Finger motion supplies repeated energy, but the resonant system selects its natural frequency. Water changes that system's effective inertia, so water level—not merely finger speed—tunes the pitch.
```

---

<a id="summary"></a>
## Summary

- A wet finger alternately sticks and slips at the rim, creating a repeated driving force.
- The drive excites a natural vibration mode of the glass; resonance builds a sustained tone.
- Frequency determines pitch, while amplitude mainly affects loudness.
- For otherwise identical glasses, more water increases effective inertia and lowers the natural frequency and pitch.
- Different water levels tune different glasses to different notes, which a performer can play in sequence as music.
- A complete explanation must identify both how the vibration is sustained and how the water changes the pitch.
