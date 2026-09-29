# Largest Displacement When Two Pulses Overlap

<!--
lesson-id: 212-M5-036
topic-code: MTH212.M5.36
-->

## Table of Contents

- [Introduction](#introduction)
- [Read Each Signed Pulse Height](#read-each-signed-pulse-height)
- [Add Displacements at the Same Point](#add-displacements-at-the-same-point)
- [Find the Largest Displacement During the Passage](#find-the-largest-displacement-during-the-passage)
- [Report the Requested Value](#report-the-requested-value)
- [Summary](#summary)

## Prerequisites

- Read a vertical displacement from a graph.
- Treat upward displacement as positive and downward displacement as negative.
- Add signed decimals with the same units.

---

<a id="introduction"></a>
## Introduction

When two pulses overlap on the same string, the string has one net displacement at each point. The **principle of superposition** says to add the two signed displacements at that point:

$$
y_{\mathrm{net}}=y_1+y_2.
$$

If a problem shows two upward pulses approaching each other and asks for the largest displacement while they pass through each other, look for the instant when their peaks completely overlap. Then add the two positive peak heights.

Use this sequence:

1. Read each peak's vertical displacement and assign its sign.
2. Add the displacements that occupy the same point at the same time.
3. For the largest displacement of two upward pulses, align the peaks and add their heights.
4. Report the resulting value in the requested units and answer form.

---

<a id="read-each-signed-pulse-height"></a>
## Read Each Signed Pulse Height

Displacement is measured vertically from the equilibrium line. A crest above equilibrium has positive displacement; a trough below equilibrium has negative displacement. Read this value from the $y$-axis. The $x$-coordinate tells where the pulse is, not how far the string is displaced.

An arrow showing that a pulse travels left or right also does not set the displacement's sign. Motion direction is horizontal; displacement sign comes from whether the string is above or below equilibrium.

**Example:** One pulse has a crest $1.4\ \mathrm{cm}$ above equilibrium. Another pulse has a trough $0.6\ \mathrm{cm}$ below equilibrium. Write their signed peak displacements.

**Explanation**

The crest is upward, so its displacement is $+1.4\ \mathrm{cm}$. The trough is downward, so its displacement is $-0.6\ \mathrm{cm}$.

```quiz
type: radio
id: p1-read-signed-height
content: |-
  A pulse peak is $0.9\ \mathrm{cm}$ below equilibrium. What is its signed displacement?
options:
- id: a
  content: |-
    $+0.9\ \mathrm{cm}$
  feedback: |-
    Positive displacement points above equilibrium, not below it. Since the peak is $0.9\ \mathrm{cm}$ below equilibrium, its signed displacement is $-0.9\ \mathrm{cm}$.
- id: b
  content: |-
    $-0.9\ \mathrm{cm}$
  correct: true
  feedback: |-
    Signed displacement records which side of equilibrium the string occupies. Below equilibrium is negative, so the peak is at $-0.9\ \mathrm{cm}$.
- id: c
  content: |-
    $0\ \mathrm{cm}$
  feedback: |-
    Zero displacement occurs on the equilibrium line. This peak is $0.9\ \mathrm{cm}$ below that line, so its displacement is nonzero and negative.
- id: d
  content: |-
    Its sign is determined by the pulse's direction of travel.
  feedback: |-
    Travel direction tells how the pulse moves along the string; it does not tell which side of equilibrium the string occupies. Being below equilibrium fixes the displacement as $-0.9\ \mathrm{cm}$ regardless of travel direction.
```

---

<a id="add-displacements-at-the-same-point"></a>
## Add Displacements at the Same Point

Superposition is point-by-point addition. Add displacements only when the two parts of the pulses occupy the same point on the string at the same time.

**Example:** At one instant, two upward pulse segments overlap. Their displacements at the same point are $0.8\ \mathrm{cm}$ and $1.3\ \mathrm{cm}$. Find the net displacement.

**Explanation**

Both displacements are positive, so

$$
y_{\mathrm{net}}=0.8\ \mathrm{cm}+1.3\ \mathrm{cm}=2.1\ \mathrm{cm}.
$$

```quiz
type: radio
id: p1-add-overlapping-displacements
content: |-
  At the same point and time, two upward pulse segments have displacements $0.7\ \mathrm{cm}$ and $1.6\ \mathrm{cm}$. What is the net displacement?
options:
- id: a
  content: |-
    $0.9\ \mathrm{cm}$
  feedback: |-
    This subtracts the two heights, but superposition adds signed displacements. Subtraction would describe opposite-signed contributions; both contributions are upward, so they add to $2.3\ \mathrm{cm}$.
- id: b
  content: |-
    $1.6\ \mathrm{cm}$
  feedback: |-
    A point in the overlap contains both pulses' displacements. Keeping only $1.6\ \mathrm{cm}$ omits the additional upward $0.7\ \mathrm{cm}$, so the net is $2.3\ \mathrm{cm}$.
- id: c
  content: |-
    $2.3\ \mathrm{cm}$
  correct: true
  feedback: |-
    Superposition adds the signed displacements at the same point. Both are upward, so $y_{\mathrm{net}}=0.7+1.6=2.3\ \mathrm{cm}$.
- id: d
  content: |-
    $1.12\ \mathrm{cm}$
  feedback: |-
    Multiplication does not describe wave superposition and even gives the wrong units. At one point, the string displacement is the sum $0.7+1.6=2.3\ \mathrm{cm}$.
- id: e
  content: |-
    $0\ \mathrm{cm}$
  feedback: |-
    Zero net displacement requires equal contributions on opposite sides of equilibrium. Both segments point upward here, so they reinforce to give $2.3\ \mathrm{cm}$.
```

If one displacement is downward, keep its negative sign inside the sum. For example,

$$
1.4\ \mathrm{cm}+(-0.6\ \mathrm{cm})=0.8\ \mathrm{cm}.
$$

```quiz
type: radio
id: p1-add-opposite-signed-displacements
content: |-
  At the same point and time, one pulse contributes $+1.3\ \mathrm{cm}$ and another contributes $-0.5\ \mathrm{cm}$. What is the net displacement?
options:
- id: a
  content: |-
    $+0.8\ \mathrm{cm}$
  correct: true
  feedback: |-
    Superposition adds signed displacements. The negative contribution partly cancels the larger positive one, leaving $+1.3+(-0.5)=+0.8\ \mathrm{cm}$.
- id: b
  content: |-
    $+1.8\ \mathrm{cm}$
  feedback: |-
    Adding magnitudes treats both pulses as upward. The second contribution is downward, so its minus sign must remain in the sum: $1.3-0.5=+0.8\ \mathrm{cm}$.
- id: c
  content: |-
    $-0.8\ \mathrm{cm}$
  feedback: |-
    The difference has magnitude $0.8\ \mathrm{cm}$, but its sign follows the larger-magnitude contribution. Since $+1.3\ \mathrm{cm}$ outweighs $-0.5\ \mathrm{cm}$, the net is $+0.8\ \mathrm{cm}$.
- id: d
  content: |-
    $+1.3\ \mathrm{cm}$
  feedback: |-
    The net displacement must include both overlapping pulses. The $-0.5\ \mathrm{cm}$ contribution partially cancels $+1.3\ \mathrm{cm}$, leaving $+0.8\ \mathrm{cm}$ rather than $+1.3\ \mathrm{cm}$.
- id: e
  content: |-
    $-1.8\ \mathrm{cm}$
  feedback: |-
    Opposite-signed contributions partially cancel, so their magnitudes should be subtracted, not added. The larger contribution is positive, making the result $+0.8\ \mathrm{cm}$ rather than $-1.8\ \mathrm{cm}$.
```

---

<a id="find-the-largest-displacement-during-the-passage"></a>
## Find the Largest Displacement During the Passage

For two upward pulses, every overlapping pair of displacements is positive. The largest possible net displacement occurs when the largest displacement of one pulse lies at the same point as the largest displacement of the other pulse. In other words, the peaks must overlap.

The **largest displacement** is the resulting vertical value. The point and instant of complete overlap tell where and when that value occurs, but they are not the requested answer.

**Example:** Two upward pulses have peak displacements $2.4\ \mathrm{cm}$ and $0.7\ \mathrm{cm}$. What is the largest displacement while they pass through each other?

**Explanation**

At complete peak overlap,

$$
y_{\max}=2.4\ \mathrm{cm}+0.7\ \mathrm{cm}=3.1\ \mathrm{cm}.
$$

The answer is not $2.4\ \mathrm{cm}$: that is only the taller pulse by itself. It is not $1.7\ \mathrm{cm}$ either, because subtraction would describe opposite-signed displacements.

```quiz
type: radio
id: p1-largest-overlap
content: |-
  Two upward pulses have peak displacements $1.1\ \mathrm{cm}$ and $1.5\ \mathrm{cm}$. What is the largest displacement while they pass through each other?
options:
- id: a
  content: |-
    $0.4\ \mathrm{cm}$
  feedback: |-
    Taking the difference would model one crest and one trough. Both peaks are upward, so complete overlap produces constructive addition: $1.1+1.5=2.6\ \mathrm{cm}$.
- id: b
  content: |-
    $1.5\ \mathrm{cm}$
  feedback: |-
    $1.5\ \mathrm{cm}$ is only the taller pulse's peak. At complete overlap, the string carries both upward displacements, so the maximum is $2.6\ \mathrm{cm}$.
- id: c
  content: |-
    $1.65\ \mathrm{cm}$
  feedback: |-
    Multiplying pulse heights is not superposition and would produce area units. The vertical displacements add at the overlap, giving $2.6\ \mathrm{cm}$.
- id: d
  content: |-
    $2.6\ \mathrm{cm}$
  correct: true
  feedback: |-
    The maximum occurs when the two upward peaks occupy the same point. Superposition then gives $y_{\max}=1.1+1.5=2.6\ \mathrm{cm}$.
- id: e
  content: |-
    $0\ \mathrm{cm}$
  feedback: |-
    Complete cancellation requires equal-magnitude displacements with opposite signs. These are two upward peaks, so their complete overlap is constructive, not zero.
```

---

<a id="report-the-requested-value"></a>
## Report the Requested Value

**Example:** Two upward pulses on a string approach each other as shown. What is the largest displacement from equilibrium measured while the pulses pass through each other?

![](<../Source/Images/approaching-positive-pulses.png>)

**Explanation**

The graph gives positive peak displacements of $1.2\ \mathrm{cm}$ and $1.8\ \mathrm{cm}$. At complete overlap,

$$
y_{\max}=1.2\ \mathrm{cm}+1.8\ \mathrm{cm}=3.0\ \mathrm{cm}.
$$

Both heights are given to the nearest tenth of a centimeter, so retain the tenths place. Because the requested entry is a number in centimeters, the answer to enter is **$3.0$**.

```quiz
type: radio
id: p1-report-number-only
content: |-
  Two upward pulses have peak displacements $0.8\ \mathrm{cm}$ and $1.7\ \mathrm{cm}$. The answer box asks for centimeters as a number only. What should be entered for the largest displacement?
options:
- id: a
  content: |-
    $0.9$
  feedback: |-
    Subtraction would apply to opposite-signed overlap. Both peaks are upward, so the largest displacement is their sum, $2.5\ \mathrm{cm}$.
- id: b
  content: |-
    $1.7$
  feedback: |-
    The maximum includes both peaks at complete overlap. Reporting $1.7$ keeps only the taller pulse and omits the other $0.8\ \mathrm{cm}$, so the entry should be $2.5$.
- id: c
  content: |-
    $2.5$
  correct: true
  feedback: |-
    At complete overlap, the two upward peaks add to $2.5\ \mathrm{cm}$. Because the box already specifies centimeters and requests a number only, enter $2.5$.
- id: d
  content: |-
    $2.5\ \mathrm{cm}$
  feedback: |-
    $2.5\ \mathrm{cm}$ is the correct physical quantity, but the box asks for a number only and already supplies the unit. Enter $2.5$ without unit text.
- id: e
  content: |-
    $25$
  feedback: |-
    Both heights are already expressed in centimeters, so no conversion factor is needed. Their sum is $2.5\ \mathrm{cm}$, making the number-only entry $2.5$, not $25$.
```

---

<a id="summary"></a>
## Summary

When two pulses overlap, use this checklist:

- **Cue:** two pulses occupy the same string and pass through one another.
- **Read:** take signed heights from the vertical axis; do not use horizontal peak locations or travel arrows as displacement signs.
- **Combine:** add displacements at the same point, $y_{\mathrm{net}}=y_1+y_2$.
- **Maximize:** for two upward pulses, align their peaks and add the two positive peak heights.
- **Report:** give the maximum vertical value, not its location, and follow the requested units and number format.

The governing equation is

$$
y_{\mathrm{net}}=y_1+y_2.
$$

For the given pulses,

$$
1.2\ \mathrm{cm}+1.8\ \mathrm{cm}=3.0\ \mathrm{cm},
$$

so the number-only entry is **$3.0$**.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Reflections at Fixed and Free Ends](../../2026-08-03-Q-3/Lessons/fixed-free-end-reflection.md)

Study guide index: 21/28

---
<!-- lesson-nav:end -->
