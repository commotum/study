# Comparing Heard Frequencies for a Moving Sound Source

## Table of Contents

- [Introduction](#introduction)
- [Read the Direction of Motion](#read-the-direction-of-motion)
- [Compare Each Listener With the Source](#compare-each-listener-with-the-source)
- [Keep Pitch Separate From Loudness](#keep-pitch-separate-from-loudness)
- [Apply the Rule to the Fire Engine](#apply-the-rule-to-the-fire-engine)
- [Summary](#summary)

## Prerequisites

- Frequency determines pitch: a higher frequency means a higher pitch.
- Sound travels as successive compressions, which can be pictured as wavefronts.
- A sound source has an emitted frequency set by how often it produces wavefronts.

---

<a id="introduction"></a>
## Introduction

When a problem describes a moving sound source and asks which listener hears a higher, lower, or equal frequency, first track the source's motion relative to each listener.

- A source moving **toward** a listener crowds the wavefronts in front of it. The listener encounters a shorter wavelength and hears a **higher frequency**.
- A source moving **away from** a listener spreads the wavefronts behind it. The listener encounters a longer wavelength and hears a **lower frequency**.
- A listener moving with the source keeps the same position relative to it and hears approximately the source's **emitted frequency**.

The key is to make a separate comparison for each listener before comparing what they hear.

Let $f_s$ denote the siren's emitted frequency. For the situations in this lesson, use this direction map:

| Source-listener situation | Wavefront cue | Frequency heard |
|---|---|---|
| Source moves toward a stationary listener | Compressed in front | $f_{\text{heard}}>f_s$ |
| Source moves away from a stationary listener | Spread out behind | $f_{\text{heard}}<f_s$ |
| Listener moves with the source | Same source-listener position | $f_{\text{heard}}\approx f_s$ |

---

<a id="read-the-direction-of-motion"></a>
## Read the Direction of Motion

**Example:** An ambulance with its siren sounding moves toward a cyclist who is standing beside the road. How does the frequency heard by the cyclist compare with the siren's emitted frequency?

**Explanation**

The recognition cue is **moves toward**. Between one emitted wavefront and the next, the ambulance advances toward the cyclist. The wavefronts reaching the cyclist are therefore closer together.

For sound traveling through the same air at speed $v$,

$$
f=\frac{v}{\lambda}.
$$

A shorter wavelength $\lambda$ means a higher observed frequency $f$. The cyclist hears a higher frequency than the siren emits.

```quiz
type: radio
id: problem-1-direction-q1
content: |-
  A train is moving toward a pedestrian while its whistle sounds. How does the frequency heard by the pedestrian compare with the whistle's emitted frequency?
options:
- id: a
  content: |-
    The pedestrian hears a higher frequency.
  correct: true
  feedback: |-
    The approaching source compresses the wavefronts that reach the pedestrian.
- id: b
  content: |-
    The pedestrian hears a lower frequency.
  feedback: |-
    A lower frequency occurs behind a source moving away, where the wavefronts are spread out.
- id: c
  content: |-
    The pedestrian hears the emitted frequency.
  feedback: |-
    The pedestrian is not moving with the whistle; the train is approaching the pedestrian.
```

```quiz
type: radio
id: problem-1-direction-q2
content: |-
  An approaching sound source compresses the wavefronts that reach a stationary listener. Which comparison follows?
options:
- id: a
  content: |-
    The wavelength is shorter, so the heard frequency is higher than the emitted frequency.
  correct: true
  feedback: |-
    With the sound speed fixed, $f=v/\lambda$: decreasing $\lambda$ increases $f$.
- id: b
  content: |-
    The wavelength is shorter, so the heard frequency is lower than the emitted frequency.
  feedback: |-
    Wavelength and frequency vary in opposite directions when the sound speed is fixed.
- id: c
  content: |-
    The wavelength is unchanged, so the heard frequency equals the emitted frequency.
  feedback: |-
    An approaching source compresses the wavefronts in front of it.
```

---

<a id="compare-each-listener-with-the-source"></a>
## Compare Each Listener With the Source

**Example:** A car with a sounding horn moves away from a person at a crosswalk. A passenger rides in the car. Who hears the higher frequency?

**Explanation**

Treat the listeners one at a time.

| Listener | Motion relative to the horn | What the listener hears |
|---|---|---|
| Person at the crosswalk | Horn moves away | Below the emitted frequency |
| Passenger | Moves with the horn | Approximately the emitted frequency |

Therefore, the passenger hears the higher frequency of the two.

**Watch Out!** A rider or driver moving with the source is not in the same situation as a stationary listener in front of the source. Classify the two listeners separately.

```quiz
type: radio
id: problem-1-listeners-q1
content: |-
  A motorcycle with its horn sounding moves away from you. How does the frequency you hear compare with the frequency heard by the rider?
options:
- id: a
  content: |-
    You hear a higher frequency than the rider does.
  feedback: |-
    The motorcycle is receding, so the wavefronts reaching you are spread out rather than compressed.
- id: b
  content: |-
    You hear a lower frequency than the rider does.
  correct: true
  feedback: |-
    You hear a Doppler-shifted lower frequency, while the co-moving rider hears approximately the emitted frequency.
- id: c
  content: |-
    You hear the same frequency as the rider does.
  feedback: |-
    The rider is co-moving with the horn, but the horn is moving away from you.
```

---

<a id="keep-pitch-separate-from-loudness"></a>
## Keep Pitch Separate From Loudness

**Example:** An approaching siren sounds louder as it gets closer. Is getting louder the reason its pitch is higher?

**Explanation**

No. Loudness concerns sound intensity, while pitch concerns frequency. The approaching siren's pitch is higher because its forward wavefronts are compressed, not merely because the siren is closer or louder.

When a question asks about **frequency**, follow the spacing of the wavefronts:

$$
\text{compressed wavefronts}\longrightarrow\text{shorter }\lambda
\longrightarrow\text{higher }f.
$$

```quiz
type: radio
id: problem-1-pitch-q1
content: |-
  Why does a stationary listener hear a higher pitch from a siren that is moving toward the listener?
options:
- id: a
  content: |-
    The source emits sound faster because it is moving.
  feedback: |-
    The source's emission rate is not the reason for the observed shift.
- id: b
  content: |-
    The source is closer, so greater loudness creates a higher frequency.
  feedback: |-
    Loudness and frequency are different sound properties.
- id: c
  content: |-
    The source compresses the wavefronts in front of it, shortening their spacing.
  correct: true
  feedback: |-
    With the sound speed fixed, a shorter wavelength corresponds to a higher frequency.
```

---

<a id="apply-the-rule-to-the-fire-engine"></a>
## Apply the Rule to the Fire Engine

**Example:** A fire engine is racing toward you with its siren sounding. How does the frequency you hear compare with the frequency heard by the fire engine's driver?

**Explanation**

For you, the fire engine is approaching. The wavefronts in front of the siren are compressed, so you hear a frequency higher than the emitted frequency.

The driver moves with the siren and hears approximately its emitted frequency. Therefore, you hear a higher frequency than the driver does.

In comparison form,

$$
f_{\text{you}}>f_s\approx f_{\text{driver}}.
$$

```quiz
type: radio
id: m5-4pre-q1
shuffle: true
content: |-
  **Question 1**

  A fire engine is racing toward you with its siren sounding. How does the frequency you hear compare with the frequency heard by the fire engine's driver?
options:
- id: a
  content: |-
    You hear a higher frequency than the driver does.
  correct: true
  feedback: |-
    Correct. Because the fire engine is moving toward you, the wavefronts ahead of it are compressed and you observe a higher frequency. The driver moves with the siren and hears approximately its emitted frequency.
- id: b
  content: |-
    You hear a lower frequency than the driver does.
  feedback: |-
    An approaching source compresses the wavefronts ahead of it, so you hear a higher—not lower—frequency than the driver.
- id: c
  content: |-
    You hear the same frequency as the driver does.
  feedback: |-
    The driver hears approximately the siren's emitted frequency, but the approaching motion compresses the wavefronts that reach you, so you hear a higher frequency.
```

---

<a id="summary"></a>
## Summary

Use this comparison routine:

1. Identify the source and each listener.
2. Decide whether the source is approaching, receding from, or co-moving with each listener.
3. Translate the motion into wavefront spacing: compressed means higher frequency, spread out means lower frequency, and co-moving means approximately the emitted frequency.
4. Compare the listeners only after classifying what each one hears.

The main trap is confusing frequency with loudness. **Toward** means higher frequency because the wavefront spacing is shorter—not simply because the sound is louder.
