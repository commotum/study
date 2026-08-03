
# Finding Complete Constructive Interference in a Crest Diagram

<!--
lesson-id: 212-M5-037
topic-code: MTH212.M5.37
-->

## Table of Contents

- [Introduction](#introduction)
- [Read One Wavefront Family](#read-one-wavefront-family)
- [Recognize Both In-Phase Combinations](#recognize-both-in-phase-combinations)
- [Reject a Crest–Trough Pair](#reject-a-cresttrough-pair)
- [Check Every Labeled Point](#check-every-labeled-point)
- [Summary](#summary)

## Prerequisites

- Recognize wave crests and troughs.
- Know that waves with the same phase interfere constructively.

---

<a id="introduction"></a>
## Introduction

When a diagram shows circular wave crests from two sources, each circle belongs to one source. The troughs are halfway between adjacent crest circles from the same source. Complete constructive interference occurs wherever the two waves arrive in phase:

$$
\begin{aligned}
\text{crest}+\text{crest}&\longrightarrow\text{constructive},\\
\text{trough}+\text{trough}&\longrightarrow\text{constructive}.
\end{aligned}
$$

The drawn circles locate crests directly, but complete constructive interference is not limited to circle intersections. A point halfway between adjacent crest circles can mark a trough. Two troughs meeting are just as in phase as two crests meeting.

Use this test on each candidate point:

1. **Trace:** Decide which source each circle is centered on.
2. **Label:** For each source, decide whether the point is on a crest circle or halfway between neighboring crest circles at a trough.
3. **Compare:** Select crest–crest and trough–trough; reject crest–trough.

The key question is whether the two sources have the same phase at the point, not merely whether two drawn lines cross there.

---

<a id="read-one-wavefront-family"></a>
## Read One Wavefront Family

**Example:** A source is surrounded by several blue circles. What does one blue circle represent?

**Explanation**

The problem states that the blue circles represent wave crests. Each circle is therefore the set of positions occupied by one crest from that source. To identify its family, follow the circle around and note whether it is centered on source 1 or source 2. A trough from that source lies halfway between two adjacent crest circles.

```quiz
type: radio
id: p2-read-crest-family
content: |-
  In a diagram where blue circles represent wave crests, what does a point on one blue circle mark?
options:
- id: a
  content: |-
    A position occupied by a crest from that circle's source
  correct: true
  feedback: |-
    Each blue circumference is a crest wavefront, so every point on it has crest phase from that source.
- id: b
  content: |-
    A position that must be a trough from that source
  feedback: |-
    The diagram explicitly assigns the blue circles to crests; troughs lie between adjacent crest circles.
- id: c
  content: |-
    A position where two sources must already interfere constructively
  feedback: |-
    One crest circle identifies only one source's phase; the phase arriving from the second source must also be checked.
- id: d
  content: |-
    The location of the wave source
  feedback: |-
    The source is at the common center of its circular wavefronts, not at every point on a circumference.
```

---

<a id="recognize-both-in-phase-combinations"></a>
## Recognize Both In-Phase Combinations

**Example:** Compare a point where two crests meet with a point where two troughs meet. Classify the interference at each point.

**Explanation**

At the first point, the two positive displacements add. At the second point, the two negative displacements add. Both pairs have zero relative phase difference, so both points are positions of complete constructive interference. Crest–crest produces the largest positive displacement at that instant, while trough–trough produces the largest negative displacement.

```quiz
type: radio
id: p2-two-crest-test
content: |-
  Which pair of arrivals represents complete constructive interference?
options:
- id: a
  content: |-
    Crest–crest or trough–trough
  correct: true
  feedback: |-
    Equal phases add: two positive crest displacements reinforce, and two negative trough displacements reinforce.
- id: b
  content: |-
    Crest–trough only
  feedback: |-
    A crest and trough have opposite displacement signs, so their overlap is destructive rather than constructive.
- id: c
  content: |-
    Crest–crest only; trough–trough is destructive
  feedback: |-
    Two troughs are also in phase; their negative displacements add to a deeper trough.
- id: d
  content: |-
    Any point lying on one visible crest circle
  feedback: |-
    Complete interference depends on both arrivals, so one source's crest phase is insufficient.
```

---

<a id="reject-a-cresttrough-pair"></a>
## Reject a Crest–Trough Pair

**Example:** A point lies on a crest circle from source 1 and halfway between adjacent crest circles from source 2. Classify the interference there.

**Explanation**

The first source contributes a crest while the second contributes a trough. Their phases differ by $\pi$, so this is complete destructive interference, not constructive interference.

```quiz
type: radio
id: p2-one-crest-trap
content: |-
  Point $X$ lies on a crest circle from source 2 and halfway between adjacent crest circles from source 1. What occurs at $X$?
options:
- id: a
  content: |-
    Complete constructive interference because one crest reaches $X$
  feedback: |-
    One crest does not determine the result; halfway between source 1's crests corresponds to a trough from source 1.
- id: b
  content: |-
    Complete constructive interference because $X$ lies between two other crests
  feedback: |-
    Halfway between adjacent crests is trough phase, not another crest.
- id: c
  content: |-
    Complete destructive interference because a crest meets a trough
  correct: true
  feedback: |-
    Source 2 supplies a crest while source 1 supplies the trough halfway between its crest circles, so the arrivals are opposite in phase.
- id: d
  content: |-
    Neither, because the drawn circles do not cross at $X$
  feedback: |-
    Crest-circle crossings mark crest–crest points, but an implied trough between circles can still meet a crest and produce complete destruction.
```

---

<a id="check-every-labeled-point"></a>
## Check Every Labeled Point

**Example:** Assume the blue circles in the diagram represent wave crests. Test each labeled point separately.

![](<../Source/Images/two-source-wave-crests-interference.png>)

**Explanation**

- At $P$, a crest from source 1 meets a crest from source 2, so $P$ is complete constructive interference.
- At $Q$, a crest from one source meets a trough from the other, so $Q$ is complete destructive interference.
- At $R$, a trough from source 1 meets a trough from source 2, so $R$ is complete constructive interference.

The phase comparison organizes the decisions:

| Point | One source | Other source | Decision |
|---|---|---|---|
| $P$ | Crest | Crest | Select: constructive |
| $Q$ | Crest | Trough | Do not select: destructive |
| $R$ | Trough | Trough | Select: constructive |

Thus the correct selections are $P$ and $R$.

```quiz
type: radio
id: p2-original-check
shuffle: true
content: |-
  The original problem asks: Assume the blue circles in the diagram represent wave crests. Which labeled points are positions of complete constructive interference? Select all correct answers and explain.

  Which complete selection is correct?

  ![](<../Source/Images/two-source-wave-crests-interference.png>)
options:
- id: p
  content: |-
    $P$ only
  feedback: P is constructive, but R is also constructive because two troughs meet there.
- id: q
  content: |-
    $Q$ only
  feedback: Q is destructive because a crest meets a trough there.
- id: r
  content: |-
    $R$ only
  feedback: R is constructive, but P is also constructive because two crests meet there.
- id: pq
  content: |-
    $P$ and $Q$
  feedback: P is constructive, but Q is destructive; this choice also omits constructive point R.
- id: pr
  content: |-
    $P$ and $R$
  correct: true
  feedback: P is crest–crest and R is trough–trough, so the two waves arrive in phase at both points.
- id: pqr
  content: |-
    $P$, $Q$, and $R$
  feedback: P and R are constructive, but Q is destructive because a crest meets a trough there.
```

---

<a id="summary"></a>
## Summary

For a diagram in which the circles represent crests, use **trace → label → compare**:

1. **Trace** each circle to its source family.
2. **Label** each source's phase at the point: on a circle is a crest; halfway between adjacent circles is a trough.
3. **Compare** the phases: crest–crest and trough–trough are constructive; crest–trough is destructive.

The main trap is treating drawn crest-circle intersections as the only constructive locations. In the assigned diagram, $P$ is crest–crest and $R$ is trough–trough, so both are constructive; $Q$ is crest–trough and is destructive.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Classifying Two-Source Interference from Path and Starting Phase](../../2026-08-02-PQ-3/Lessons/Problem-3.md)

Study guide index: 26/28

---
<!-- lesson-nav:end -->
