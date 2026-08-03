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
- id: q3-ffer-fixed-b
  content: |-
    It is downward with a $\pi$-radian phase shift.
- id: q3-ffer-fixed-c
  content: |-
    It is upward with a $0$-radian phase shift.
- id: q3-ffer-fixed-d
  content: |-
    It is upward with a $\pi$-radian phase shift.
  correct: true
  feedback: |-
    Correct. A fixed end inverts the displacement, so downward becomes upward and the reflection adds a phase shift of $\pi$.
- id: q3-ffer-fixed-e
  content: |-
    It disappears because a fixed end cannot move.
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
    Correct. A free end preserves the displacement orientation and adds no phase reversal.
- id: q3-ffer-free-b
  content: |-
    It is downward with a $\pi$-radian phase shift.
- id: q3-ffer-free-c
  content: |-
    It is upward with a $0$-radian phase shift.
- id: q3-ffer-free-d
  content: |-
    It is upward with a $\pi$-radian phase shift.
- id: q3-ffer-free-e
  content: |-
    It continues through the end without reflecting.
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
- id: q3-ffer-direction-b
  content: |-
    A free-end reflection with zero phase shift
  correct: true
  feedback: |-
    Correct. The pulse reverses travel direction but keeps its upward displacement, so it is not inverted.
- id: q3-ffer-direction-c
  content: |-
    A fixed-end reflection with zero phase shift
- id: q3-ffer-direction-d
  content: |-
    A free-end reflection with a $\pi$ phase shift
- id: q3-ffer-direction-e
  content: |-
    No reflection, because the pulse remains upward
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
- id: q3-ffer-scope-b
  content: |-
    It must remain upright with zero phase shift.
- id: q3-ffer-scope-c
  content: |-
    It cannot reflect because the string continues.
- id: q3-ffer-scope-d
  content: |-
    Its detailed behavior cannot be determined from the fixed/free-end rules.
  correct: true
  feedback: |-
    Correct. A change of medium is a separate discontinuity problem, explicitly outside this lesson's scope.
- id: q3-ffer-scope-e
  content: |-
    Its reflected and transmitted amplitudes must be equal.
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

---

<!-- lesson-nav:end -->
