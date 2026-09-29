# Reflections at Fixed and Free Ends

<!--
lesson-id: 212-M5-052
topic-code: MTH212.M5.52
-->

## Table of Contents

- [Introduction](#introduction)
- [Invert at a Fixed End](#invert-at-a-fixed-end)
- [Preserve Orientation at a Free End](#preserve-orientation-at-a-free-end)
- [Separate Travel Direction From Inversion](#separate-travel-direction-from-inversion)
- [Recognize the Scope Boundary](#recognize-the-scope-boundary)
- [Summary](#summary)

## Prerequisites

- Read upward and downward displacement from equilibrium.
- Recognize that a reflected pulse travels back toward its source.
- Interpret a phase shift of $\pi$ radians as an inversion.

---

<a id="introduction"></a>
## Introduction

When a pulse reaches the end of a string, the cue **fixed end or free end** determines the reflected pulse's orientation and phase shift.

| Boundary | Other name | Reflected orientation | Phase shift |
| --- | --- | --- | --- |
| Fixed end | Hard end | Inverted | $\pi$ radians |
| Free end | Soft end | Not inverted | $0$ radians |

The boundary type—not the incoming pulse's direction—selects the rule. First identify the end, then decide whether to flip the displacement.

---

<a id="invert-at-a-fixed-end"></a>
## Invert at a Fixed End

**Example:** An upward pulse travels right and reaches a string end tied rigidly to a wall. Describe the reflected pulse.

**Explanation**

A tied end cannot move, so it is a fixed or hard boundary. The reflected pulse travels left and is inverted:

$$
\text{upward incident pulse}
\longrightarrow
\text{downward reflected pulse}.
$$

The inversion corresponds to

$$
\Delta\phi_{\mathrm{reflection}}=\pi.
$$

```quiz
type: radio
id: q3-ffer-fixed-end
content: |-
  A downward pulse reaches the fixed end of a string. Which description of the reflected pulse is correct?
options:
- id: q3-ffer-fixed-a
  content: |-
    It is downward with a $0$-radian phase shift.
  feedback: |-
    A reflected pulse keeps its orientation with zero phase shift only at a free end. A fixed end inverts the downward pulse, so it returns upward with a $\pi$ phase shift.
- id: q3-ffer-fixed-b
  content: |-
    It is downward with a $\pi$-radian phase shift.
  feedback: |-
    The stated phase shift and orientation contradict each other: a $\pi$ reflection shift means inversion. Thus a downward incident pulse must return upward, not downward.
- id: q3-ffer-fixed-c
  content: |-
    It is upward with a $0$-radian phase shift.
  feedback: |-
    Changing the pulse from downward to upward is an inversion. At a fixed end that inversion corresponds to a $\pi$ phase shift, not a zero phase shift.
- id: q3-ffer-fixed-d
  content: |-
    It is upward with a $\pi$-radian phase shift.
  correct: true
  feedback: |-
    A fixed end forces the displacement to remain zero, so the reflected pulse is inverted. The downward incident pulse therefore returns upward with a $\pi$ phase shift.
- id: q3-ffer-fixed-e
  content: |-
    It disappears because a fixed end cannot move.
  feedback: |-
    The fixed endpoint stays at zero displacement because the incident and inverted reflected waves cancel there. In the ideal model, the pulse reflects upward rather than disappearing.
```

---

<a id="preserve-orientation-at-a-free-end"></a>
## Preserve Orientation at a Free End

**Example:** An upward pulse reaches a ring that can slide freely on a vertical rod. Describe the reflected pulse.

**Explanation**

The sliding ring makes the boundary free or soft. The pulse returns without inversion:

$$
\text{upward incident pulse}
\longrightarrow
\text{upward reflected pulse}.
$$

There is no reflection phase reversal:

$$
\Delta\phi_{\mathrm{reflection}}=0.
$$

```quiz
type: radio
id: q3-ffer-free-end
content: |-
  A downward pulse reaches a free end. Which description of the reflected pulse is correct?
options:
- id: q3-ffer-free-a
  content: |-
    It is downward with a $0$-radian phase shift.
  correct: true
  feedback: |-
    A free end reflects a pulse without inversion. The downward pulse therefore remains downward, corresponding to a zero reflection phase shift.
- id: q3-ffer-free-b
  content: |-
    It is downward with a $\pi$-radian phase shift.
  feedback: |-
    The downward orientation describes a noninverted reflection, but a $\pi$ phase shift describes inversion. At a free end the consistent pair is downward with a zero phase shift.
- id: q3-ffer-free-c
  content: |-
    It is upward with a $0$-radian phase shift.
  feedback: |-
    Changing downward to upward would invert the pulse. A free end preserves orientation, so a downward incident pulse returns downward with zero phase shift.
- id: q3-ffer-free-d
  content: |-
    It is upward with a $\pi$-radian phase shift.
  feedback: |-
    Upward with a $\pi$ shift is the fixed-end result because both indicate inversion. A free end produces neither, so this pulse returns downward with zero phase shift.
- id: q3-ffer-free-e
  content: |-
    It continues through the end without reflecting.
  feedback: |-
    A free end means the string terminates but its endpoint can move; it does not mean the wave has another string to enter. The boundary still reflects the pulse, without inversion.
```

---

<a id="separate-travel-direction-from-inversion"></a>
## Separate Travel Direction From Inversion

**Example:** Two identical upward pulses travel right. One reaches a fixed end and the other reaches a free end. Compare the reflected pulses.

**Explanation**

Both reflected pulses reverse their **travel direction** and move left. Only the fixed-end pulse reverses its **displacement orientation**:

| Boundary | Reflected travel | Reflected displacement |
| --- | --- | --- |
| Fixed | Left | Downward |
| Free | Left | Upward |

Travel-direction reversal happens in both cases. It is not what the word **inverted** means here; inversion refers to the sign of the displacement.

```quiz
type: radio
id: q3-ffer-direction-vs-inversion
content: |-
  An upward pulse travels left toward a boundary. After reflection it travels right and is still upward. What boundary behavior does this show?
options:
- id: q3-ffer-direction-a
  content: |-
    A fixed-end reflection with a $\pi$ phase shift
  feedback: |-
    Reflection always reverses the direction of travel, but a fixed end also reverses the displacement. Because this pulse remains upward, it shows a free-end reflection with zero phase shift.
- id: q3-ffer-direction-b
  content: |-
    A free-end reflection with zero phase shift
  correct: true
  feedback: |-
    Reflection reverses the pulse's travel direction, while a free end preserves its displacement orientation. The pulse returns rightward but stays upward, so the phase shift is zero.
- id: q3-ffer-direction-c
  content: |-
    A fixed-end reflection with zero phase shift
  feedback: |-
    A fixed end cannot produce a noninverted zero-shift reflection. The unchanged upward orientation identifies a free end, while the rightward motion simply shows that reflection reversed the travel direction.
- id: q3-ffer-direction-d
  content: |-
    A free-end reflection with a $\pi$ phase shift
  feedback: |-
    The preserved upward orientation does identify a free end, but preservation corresponds to a zero phase shift. A $\pi$ shift would invert the pulse to downward.
- id: q3-ffer-direction-e
  content: |-
    No reflection, because the pulse remains upward
  feedback: |-
    The change from leftward to rightward travel is exactly the evidence that reflection occurred. Remaining upward says the reflection was noninverting, which identifies the free-end rule.
```

---

<a id="recognize-the-scope-boundary"></a>
## Recognize the Scope Boundary

**Example:** A pulse traveling on one string reaches a junction with a different string. Can the fixed/free-end rules alone determine the reflected pulse's orientation and the transmitted amplitude?

**Explanation**

No. A junction between different media is not simply a fixed end or a free end. It can produce both a reflected wave and a transmitted wave, and the detailed result depends on the media.

For this lesson—and for the stated quiz scope—stop at the boundary:

- **Included:** reflection from an explicitly fixed/hard end.
- **Included:** reflection from an explicitly free/soft end.
- **Excluded:** detailed reflection and transmission at a change from one medium to another.

Do not invent a fixed- or free-end label for a material junction.

```quiz
type: radio
id: q3-ffer-scope-boundary
content: |-
  A pulse reaches a junction between a light string and a heavier string. Using only the fixed/free-end rules in this lesson, what can you conclude about the reflected pulse?
options:
- id: q3-ffer-scope-a
  content: |-
    It must invert and acquire a phase shift of $\pi$.
  feedback: |-
    A heavier second string is not an immovable fixed endpoint; it can carry a transmitted wave. Whether and how the reflection inverts must be analyzed with junction rules, not assumed from the fixed-end rule alone.
- id: q3-ffer-scope-b
  content: |-
    It must remain upright with zero phase shift.
  feedback: |-
    A free end has no continuing medium, whereas this junction connects to another string that supports transmission. The free-end zero-shift rule therefore cannot be applied directly.
- id: q3-ffer-scope-c
  content: |-
    It cannot reflect because the string continues.
  feedback: |-
    Continuing into a different medium does not prevent reflection. A junction can split the incident wave into reflected and transmitted parts, so “the string continues” is not enough to rule reflection out.
- id: q3-ffer-scope-d
  content: |-
    Its detailed behavior cannot be determined from the fixed/free-end rules.
  correct: true
  feedback: |-
    Fixed- and free-end rules apply to terminating boundaries. A light-to-heavy junction is a different boundary problem with both reflection and transmission, so those two rules alone do not determine its detailed behavior.
- id: q3-ffer-scope-e
  content: |-
    Its reflected and transmitted amplitudes must be equal.
  feedback: |-
    A junction divides the wave according to the two media's properties; no fixed/free-end rule requires equal reflected and transmitted amplitudes. Their values need a junction analysis.
```

---

<a id="summary"></a>
## Summary

Use this boundary check:

1. Identify the end before looking at the pulse orientation.
2. At a **fixed/hard end**, flip the displacement and assign a phase shift of $\pi$.
3. At a **free/soft end**, preserve the displacement and assign a phase shift of $0$.
4. In both cases, the reflected pulse reverses its travel direction.
5. Do not apply these two rules to a junction between different media; detailed reflection and transmission there are excluded.

The main trap is confusing reversal of travel direction with inversion. Every reflected pulse travels back, but only a fixed-end reflection flips upward to downward or downward to upward.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../Study-Guide.md)
Next: [Third-Harmonic Frequency of a Wire Tensioned by a Hanging Mass](../../2026-07-29-M5-4/Lessons/Problem-3.md)

Study guide index: 22/28

---
<!-- lesson-nav:end -->
