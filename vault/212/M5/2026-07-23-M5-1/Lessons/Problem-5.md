# Inferring Particle Motion From a Traveling-Wave Snapshot

<!--
lesson-id: 212-M5-005
topic-code: MTH212.M5.05
-->

## Table of Contents

- [Introduction](#introduction)
- [Separate Wave Motion From Particle Motion](#separate-wave-motion-from-particle-motion)
- [Advance the Wave While Holding the Particle Position Fixed](#advance-the-wave-while-holding-the-particle-position-fixed)
- [Use the Local-Slope Rule](#use-the-local-slope-rule)
- [Apply the Move to the Marked Particle](#apply-the-move-to-the-marked-particle)
- [Summary](#summary)

## Prerequisites

- Read whether a graph rises, falls, or is locally horizontal as \(x\) increases.
- Distinguish the motion of a wave pattern from the motion of a string particle.
- Interpret the sign of a velocity.

---

<a id="introduction"></a>
## Introduction

A snapshot \(y\) versus \(x\) shows the string's shape at one instant. It does **not** directly graph a particle's displacement versus time. To predict the particle's next motion, combine:

1. the wave's propagation direction, and
2. the snapshot's local slope at the particle.

For a wave moving right at speed \(v\),

$$
y(x,t)=F(x-vt)
\qquad\Longrightarrow\qquad
\frac{\partial y}{\partial t}=-v\frac{\partial y}{\partial x}.
$$

Because \(v>0\), the vertical velocity and spatial slope have opposite signs.

**Recognition cue:** If the horizontal axis is position \(x\), read a **spatial slope** and combine it with the propagation direction. If the horizontal axis were time \(t\), the graph's slope would already be the particle's velocity.

---

<a id="separate-wave-motion-from-particle-motion"></a>
## Separate Wave Motion From Particle Motion

**Example:** A transverse wave travels to the right along a horizontal string. Does a marked string particle travel to the right with the crest?

**Explanation**

No. The arrow tells how the **wave pattern** propagates. Each marked piece of the idealized string stays at the same horizontal position and moves transversely—up or down.

So horizontal answer choices describe the pattern, not the particle.

```quiz
type: radio
id: problem-5-pattern-particle-q1
content: |-
  A transverse wave travels to the right on a horizontal string. Which motion can a marked particle of the string have at an instant?
options:
- id: a
  content: |-
    Only motion to the right
  feedback: |-
    This assigns the wave pattern's propagation to the material point. “Travels right” tells how the shape advances along the string; a particle in a transverse wave moves vertically and may be moving up, moving down, or momentarily at rest.
- id: b
  content: |-
    Vertical motion or momentary rest
  correct: true
  feedback: |-
    In a transverse wave, each marked string particle moves perpendicular to the horizontal propagation direction. It can therefore move up or down, and at a vertical turning point it can be momentarily at rest.
- id: c
  content: |-
    Only motion to the left
  feedback: |-
    This treats the particle as moving horizontally opposite the wave pattern. Propagation direction and particle motion are different: the pattern moves right, while the marked particle's allowed motion is vertical or momentary rest.
```

---

<a id="advance-the-wave-while-holding-the-particle-position-fixed"></a>
## Advance the Wave While Holding the Particle Position Fixed

**Example:** A right-moving wave has positive slope at a marked horizontal position \(x_0\). In the next instant, does the string at \(x_0\) move up or down?

**Explanation**

Imagine shifting the entire profile a tiny distance to the right, but keep your eye on the same horizontal position \(x_0\). The future height at \(x_0\) is the height that was a little to its left:

$$
y(x_0,t+\Delta t)=y(x_0-v\Delta t,t).
$$

On a positive-slope segment, the point just to the left is lower. That lower value arrives at \(x_0\), so the marked particle moves **down**.

| Keep fixed | Move mentally | Compare |
|---|---|---|
| The particle's horizontal position \(x_0\) | The entire wave profile slightly right | The old height just left of \(x_0\) with the current height at \(x_0\) |

This corresponding-point comparison is the safest visual method: translate the **profile**, then compare heights at one fixed \(x\).

```quiz
type: radio
id: problem-5-shift-q1
content: |-
  A wave profile moves to the right. At a fixed position, the profile has positive spatial slope. Which old part of the profile determines the height there an instant later?
options:
- id: a
  content: |-
    The slightly lower part just to the left
  correct: true
  feedback: |-
    A right-moving profile carries the old shape from left to right, so the new height at a fixed $x$ comes from just to its left. On a positive slope that left-neighbor value is lower, so the marked particle's height decreases and it moves down.
- id: b
  content: |-
    The slightly higher part just to the right
  feedback: |-
    This samples the profile from the wrong side. A value just to the right would arrive at the fixed point only for a left-moving wave; a right-moving wave brings the slightly lower value from the left.
- id: c
  content: |-
    The same part, because no particle can move
  feedback: |-
    This confuses fixed horizontal position with complete rest. The marked particle does remain at the same $x$, but the passing profile changes its vertical displacement; here the incoming lower value makes it move downward.
```

---

<a id="use-the-local-slope-rule"></a>
## Use the Local-Slope Rule

**Example:** At a marked point on a right-moving wave, the snapshot falls as \(x\) increases. Which way is the particle moving?

**Explanation**

The snapshot has negative spatial slope:

$$
\frac{\partial y}{\partial x}<0.
$$

For a right-moving wave,

$$
\frac{\partial y}{\partial t}
=-v\frac{\partial y}{\partial x}>0.
$$

Positive vertical velocity means the particle moves **up**.

| Snapshot slope at the particle | Particle motion for a right-moving wave |
|---|---|
| Positive | Down |
| Negative | Up |
| Zero | Momentarily not moving vertically |

**Watch Out!** Use the slope *at the marked point*, not the particle's height. A point can be above equilibrium and moving either up or down. At a crest or trough the spatial slope is zero, so the particle is momentarily at rest vertically.

```quiz
type: radio
id: problem-5-slope-rule-q1
content: |-
  A right-moving transverse wave has zero spatial slope at a marked particle. What is the particle doing at that instant?
options:
- id: a
  content: |-
    Moving up
  feedback: |-
    For a right-moving profile, vertical velocity has the opposite sign from spatial slope: $\partial y/\partial t=-v\,\partial y/\partial x$. Upward motion requires negative slope, whereas the stated zero slope gives zero vertical velocity.
- id: b
  content: |-
    Moving down
  feedback: |-
    Downward motion occurs where a right-moving wave has positive spatial slope. At the stated point the slope is zero, so $\partial y/\partial t=-v(0)=0$ and the particle is momentarily at rest vertically.
- id: c
  content: |-
    Momentarily not moving vertically
  correct: true
  feedback: |-
    A right-moving wave has vertical particle velocity opposite in sign to its spatial slope. Since the local slope is zero, $\partial y/\partial t=-v(0)=0$, so the particle is momentarily not moving vertically.
```

---

<a id="apply-the-move-to-the-marked-particle"></a>
## Apply the Move to the Marked Particle

**Example:** In the snapshot below, first identify the propagation direction, then read the curve's local slope at the marked point.

![](<../Source/Images/right-moving-wave-marked-particle.png>)

**Explanation**

Use a three-pass scan:

1. **Wave direction:** the profile propagates in the positive \(x\) direction.
2. **Local slope:** the curve rises from left to right at the marked point, so the spatial slope is positive.
3. **Particle direction:** for a right-moving wave, reverse the slope sign.

$$
\frac{\partial y}{\partial x}>0
\qquad\Longrightarrow\qquad
\frac{\partial y}{\partial t}
=-v\frac{\partial y}{\partial x}<0.
$$

The particle therefore moves **down**. It does not move horizontally with the wave pattern.

```quiz
type: radio
id: m5-1lec-q4
shuffle: true
content: |-
  **Question 4**

  A wave on a string propagates in the positive $x$ direction. Which direction will the marked particle move in the next instant?

  ![](<../Source/Images/right-moving-wave-marked-particle.png>)
options:
- id: a
  content: Up
  feedback: |-
    This reverses the slope rule. For a right-moving wave, particle velocity is opposite the local spatial slope; upward motion requires negative slope, but the marked point has positive slope and therefore moves down.
- id: b
  content: Down
  correct: true
  feedback: |-
    As a right-moving profile shifts past a fixed particle, the particle's vertical motion is opposite the profile's local slope. The marked point lies on a positive slope, so $\partial y/\partial t<0$ and the particle moves down.
- id: c
  content: Right
  feedback: |-
    This gives the marked particle the wave pattern's propagation velocity. The shape moves right along the string, but a transverse string particle stays at its horizontal coordinate and moves vertically; here it moves down.
- id: d
  content: Left
  feedback: |-
    This assumes the material particle travels opposite the pattern. A transverse particle does not move along the string in either horizontal direction; its motion is vertical, and the positive slope makes that motion downward here.
- id: e
  content: Up and to the right
  feedback: |-
    This combines two distinct errors. Right describes the pattern's propagation, not the particle's motion, and a positive slope on a right-moving wave gives downward—not upward—vertical velocity.
- id: f
  content: Up and to the left
  feedback: |-
    Neither component matches the particle's motion. A transverse string particle has no leftward horizontal velocity, and for a right-moving profile the marked positive slope corresponds to downward vertical velocity.
- id: g
  content: Down and to the right
  feedback: |-
    The downward component correctly follows from the marked point's positive slope. The added rightward component belongs only to the traveling wave shape; the material particle remains at the same horizontal coordinate.
- id: h
  content: Down and to the left
  feedback: |-
    The downward component is correct, but the leftward component is not. The particle moves transversely while staying at its fixed $x$; it does not travel horizontally with or against the wave pattern.
- id: i
  content: It is not moving
  feedback: |-
    A particle of a traveling wave is momentarily at rest only where the profile's local slope is zero. The marked point has positive slope, so its vertical velocity is nonzero and, for rightward propagation, directed downward.
```

---

<a id="summary"></a>
## Summary

For a right-moving transverse wave:

1. Keep the marked particle at the same horizontal position.
2. Read the snapshot's local slope from left to right.
3. Reverse that sign to get the particle's vertical motion.

$$
\boxed{\text{positive slope}\to\text{down},\quad
\text{negative slope}\to\text{up},\quad
\text{zero slope}\to\text{momentary rest}}
$$

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Finding Wave Speed from a Traveling-Wave Equation](../../2026-07-28-HW-7/Lessons/Problem-10.md)

Study guide index: 09/28

---
<!-- lesson-nav:end -->
