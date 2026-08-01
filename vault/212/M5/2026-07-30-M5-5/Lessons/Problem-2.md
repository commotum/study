# Finding Complete Constructive Interference in a Crest Diagram

## Table of Contents

- [Introduction](#introduction)
- [Read One Wavefront Family](#read-one-wavefront-family)
- [Require a Crest From Both Sources](#require-a-crest-from-both-sources)
- [Avoid the One-Crest Trap](#avoid-the-one-crest-trap)
- [Check Every Labeled Point](#check-every-labeled-point)
- [Summary](#summary)

## Prerequisites

- Recognize a wave crest.
- Know that waves arriving crest with crest are in phase and interfere constructively.

---

<a id="introduction"></a>
## Introduction

When a diagram shows circular wave crests from two sources, each circle belongs to one source. Complete constructive interference occurs where the two waves arrive in phase:

$$
\text{crest from source 1}+\text{crest from source 2}
\longrightarrow \text{complete constructive interference}.
$$

In a crest-only diagram, the visible cue is a point shared by a crest circle from source 1 and a crest circle from source 2. The curves must pass through the same point; being close is not enough.

Use this test on each candidate point:

1. **Trace:** Decide which source each circle is centered on.
2. **Pair:** Check whether one crest from each source passes through the same point.
3. **Select:** Choose the point only when both crests pass through it.

This is a two-condition test, like finding an element that belongs to both of two sets.

---

<a id="read-one-wavefront-family"></a>
## Read One Wavefront Family

**Example:** A source is surrounded by several blue circles. What does one blue circle represent?

**Explanation**

The problem states that the blue circles represent wave crests. Each circle is therefore the set of positions reached by one crest from that source. To identify its family, follow the circle around and note whether it is centered on source 1 or source 2. The space between drawn circles is not another drawn crest.

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
- id: b
  content: |-
    A position that must be a trough from that source
- id: c
  content: |-
    A position where two sources must already interfere constructively
- id: d
  content: |-
    The location of the wave source
```

---

<a id="require-a-crest-from-both-sources"></a>
## Require a Crest From Both Sources

**Example:** A candidate point lies where one crest circle centered on source 1 crosses one crest circle centered on source 2. Classify the interference there.

**Explanation**

At the crossing, both sources contribute a crest at the same place. Crest plus crest means the waves arrive in phase, so their positive displacements add. The point is a position of complete constructive interference. This conclusion depends on the two curves belonging to different source families.

```quiz
type: radio
id: p2-two-crest-test
content: |-
  A labeled point lies exactly at the crossing of a crest circle from each of two sources. What does the diagram show at that point?
options:
- id: a
  content: |-
    Complete constructive interference
  correct: true
- id: b
  content: |-
    Complete destructive interference
- id: c
  content: |-
    Complete constructive interference only if the two curves belong to the same source
- id: d
  content: |-
    The location of a third source
```

---

<a id="avoid-the-one-crest-trap"></a>
## Avoid the One-Crest Trap

**Example:** A point lies on a crest circle from source 1, but no crest circle from source 2 passes through it. Should it be marked as a crest–crest position?

**Explanation**

No. One visible crest is only half of the test. Complete constructive interference in this diagram requires the same point to lie on one crest from each source. A nearby circle does not count; both curves must pass through the point.

```quiz
type: radio
id: p2-one-crest-trap
content: |-
  Point $X$ lies on a crest circle from source 2. The nearest crest circle from source 1 passes beside $X$ but not through it. Should $X$ be selected as a crest–crest position?
options:
- id: a
  content: |-
    Yes, because one crest reaches $X$
- id: b
  content: |-
    Yes, because the other crest is nearby
- id: c
  content: |-
    No, because a crest from each source must pass through the same point
  correct: true
- id: d
  content: |-
    No, because circular waves cannot interfere
```

---

<a id="check-every-labeled-point"></a>
## Check Every Labeled Point

**Example:** Assume the blue circles in the diagram represent wave crests. Test each labeled point separately.

![](<../Source/Images/two-source-wave-crests-interference.png>)

**Explanation**

- At $P$, a crest from source 1 crosses a crest from source 2, so $P$ is complete constructive interference.
- At $Q$, a crest from source 1 also crosses a crest from source 2, so $Q$ is complete constructive interference.
- At $R$, the point is not at a crest–crest intersection, so the diagram does not identify $R$ as complete constructive interference.

The same two-condition test organizes the decisions:

| Point | Shared by a crest from each source? | Decision |
|---|---:|---|
| $P$ | Yes | Select |
| $Q$ | Yes | Select |
| $R$ | No | Do not select |

Thus the correct selections are $P$ and $Q$.

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
  feedback: P is constructive, but Q is also at a crest–crest intersection.
- id: q
  content: |-
    $Q$ only
  feedback: Q is constructive, but P is also at a crest–crest intersection.
- id: r
  content: |-
    $R$ only
  feedback: R is not at a crest–crest intersection.
- id: pq
  content: |-
    $P$ and $Q$
  correct: true
  feedback: P and Q each lie at a crest–crest intersection, so the two waves arrive in phase at both points.
- id: pqr
  content: |-
    $P$, $Q$, and $R$
  feedback: P and Q qualify, but R is not at a crest–crest intersection.
```

---

<a id="summary"></a>
## Summary

For a diagram in which the circles represent crests, use **trace → pair → select**:

1. **Trace** each circle to its source family.
2. **Pair** one crest from each source at the same labeled point.
3. **Select** the point only when both crests pass through it.

The main trap is choosing a point that lies on only one crest or merely sits near a crossing. In the assigned diagram, $P$ and $Q$ pass the two-crest test; $R$ does not.
