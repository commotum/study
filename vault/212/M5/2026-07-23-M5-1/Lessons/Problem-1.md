# Reading Particle Motion From a Displacement-Time Graph

## Table of Contents

- [Introduction](#introduction)
- [Read the Local Slope From Left to Right](#read-the-local-slope-from-left-to-right)
- [Separate Displacement From Velocity](#separate-displacement-from-velocity)
- [Use the Tangent at the Marked Instant](#use-the-tangent-at-the-marked-instant)
- [Separate Particle Motion From Wave Propagation](#separate-particle-motion-from-wave-propagation)
- [Apply the Rule to the Marked Particle](#apply-the-rule-to-the-marked-particle)
- [Summary](#summary)

## Prerequisites

- Identify the horizontal and vertical axes of a graph.
- Recognize positive, negative, and zero slope.
- Distinguish a transverse particle's vertical motion from a wave's horizontal propagation.

---

<a id="introduction"></a>
## Introduction

On a graph of displacement $D$ versus time $t$, the slope at an instant is the particle's vertical velocity:

$$
v_y=\frac{dD}{dt}.
$$

Read the curve from left to right, because time increases to the right.

- If the graph is rising, $dD/dt>0$, so the particle is moving **up**.
- If the graph is falling, $dD/dt<0$, so the particle is moving **down**.
- If the graph is locally horizontal, $dD/dt=0$, so the particle is momentarily **not moving vertically**.

The recognition cue is a marked instant on a displacement-versus-time graph. Use the curve's local slope, not the wave's propagation arrow or the sign of the displacement.

| Local graph behavior as $t$ increases | Sign of $dD/dt$ | Particle motion |
|---|---:|---|
| Rising | Positive | Up |
| Falling | Negative | Down |
| Horizontal | Zero | Momentarily stopped vertically |

---

<a id="read-the-local-slope-from-left-to-right"></a>
## Read the Local Slope From Left to Right

**Example:** At a marked instant, a particle's displacement-time curve rises as time increases. Which direction is the particle moving?

**Explanation**

Because the horizontal axis is time, follow the curve from left to right. A rising curve has positive slope:

$$
\frac{dD}{dt}>0.
$$

Positive vertical velocity means the particle is moving upward.

```quiz
type: radio
id: problem-1-slope-q1
content: |-
  At a marked instant, a displacement-versus-time graph is falling as time increases. What is the particle's vertical motion?
options:
- id: a
  content: |-
    It is moving up.
  feedback: |-
    Upward motion corresponds to a positive slope on a displacement-time graph.
- id: b
  content: |-
    It is moving down.
  correct: true
  feedback: |-
    A falling displacement-time curve has $dD/dt<0$, so the vertical velocity is downward.
- id: c
  content: |-
    It is not moving.
  feedback: |-
    The particle is momentarily stopped only when the local slope is zero.
```

---

<a id="separate-displacement-from-velocity"></a>
## Separate Displacement From Velocity

**Example:** A particle is at $D=0$, and its displacement-time graph is crossing the axis with a negative slope. Is the particle stopped?

**Explanation**

No. The value $D=0$ tells where the particle is: at its equilibrium displacement. The slope tells how it is moving.

Since the curve has negative slope,

$$
D=0
\qquad\text{but}\qquad
v_y=\frac{dD}{dt}<0.
$$

The particle is passing through equilibrium while moving downward.

```quiz
type: radio
id: problem-1-displacement-q1
content: |-
  A displacement-time curve crosses $D=0$ with positive slope. Which statement is correct at that instant?
options:
- id: a
  content: |-
    The particle is at equilibrium and moving up.
  correct: true
  feedback: |-
    Zero displacement gives the position, while positive slope gives upward velocity.
- id: b
  content: |-
    The particle is at equilibrium and stopped.
  feedback: |-
    A zero displacement does not imply zero velocity.
- id: c
  content: |-
    The particle is above equilibrium and moving down.
  feedback: |-
    The curve is at $D=0$, not above equilibrium, and its positive slope means upward motion.
```

---

<a id="use-the-tangent-at-the-marked-instant"></a>
## Use the Tangent at the Marked Instant

**Example:** At the top of a displacement-time crest, what is the particle's instantaneous vertical motion?

**Explanation**

At the crest, the tangent to the graph is horizontal. Its instantaneous slope is zero:

$$
v_y=\frac{dD}{dt}=0.
$$

The particle is momentarily stopped before reversing from upward to downward motion. The slopes elsewhere on the curve do not replace the local slope at the marked instant.

**Watch Out!** The question asks for instantaneous motion. Use the tangent slope at the marked point, not an average slope between two distant points on the curve.

```quiz
type: radio
id: problem-1-tangent-q1
content: |-
  A marked point lies at the bottom of a trough on a displacement-versus-time graph. What is the particle doing at that instant?
options:
- id: a
  content: |-
    Moving up
  feedback: |-
    It will move upward just after the trough, but exactly at the trough the tangent is horizontal.
- id: b
  content: |-
    Moving down
  feedback: |-
    It moved downward just before the trough, but its instantaneous slope at the trough is zero.
- id: c
  content: |-
    Momentarily not moving vertically
  correct: true
  feedback: |-
    The tangent at the trough is horizontal, so $dD/dt=0$.
```

---

<a id="separate-particle-motion-from-wave-propagation"></a>
## Separate Particle Motion From Wave Propagation

**Example:** A transverse wave propagates to the right while a marked particle's displacement-time graph has negative slope. Does the particle move right or down?

**Explanation**

The rightward arrow describes the motion of the **wave pattern** along the string. A particle of the string moves transversely, which here means vertically.

The particle's direction comes from

$$
v_y=\frac{dD}{dt}<0,
$$

so the particle moves down even while the wave travels right.

```quiz
type: radio
id: problem-1-wave-q1
content: |-
  A transverse wave travels left while a marked particle's displacement-time graph has positive slope. Which direction is the particle moving?
options:
- id: a
  content: |-
    Up
  correct: true
  feedback: |-
    Positive $dD/dt$ means upward particle motion, independent of the pattern's leftward propagation.
- id: b
  content: |-
    Left
  feedback: |-
    Left describes the wave pattern's propagation, not the transverse particle motion.
- id: c
  content: |-
    Down
  feedback: |-
    Downward motion would require a negative displacement-time slope.
```

---

<a id="apply-the-rule-to-the-marked-particle"></a>
## Apply the Rule to the Marked Particle

**Example:** The graph shows displacement versus time for a particle in a string while a wave propagates to the right. At the marked instant, which direction is the particle moving?

![](<../Source/Images/wave-particle-displacement-time-graph.png>)

**Explanation**

Read the graph's roles before interpreting the mark:

| Graph feature | Meaning |
|---|---|
| Horizontal axis | Time $t$ |
| Vertical axis | Displacement $D$ |
| Local slope | $dD/dt$, vertical velocity |
| Slope at the mark | Negative |

Because the horizontal axis is time $t$, inspect the curve from left to right at the marked instant. The curve is falling there, which means its local slope is negative:

$$
v_y=\frac{dD}{dt}<0.
$$

Therefore, the particle is moving down. The rightward arrow gives the propagation direction of the wave, not the motion direction of the string particle.

```quiz
type: radio
id: m5-1pre-q1
shuffle: true
content: |-
  **Question 1**

  The graph shows displacement versus time for a particle in a string while a wave propagates to the right. At the marked instant, which direction is the particle moving?

  ![](<../Source/Images/wave-particle-displacement-time-graph.png>)
options:
- id: a
  content: Up
- id: b
  content: Down
  correct: true
  feedback: The slope of the displacement-versus-time graph is negative at the marked instant, so $v_y=dD/dt<0$ and the particle is moving downward.
- id: c
  content: Right
- id: d
  content: Left
- id: e
  content: It is not moving
```

---

<a id="summary"></a>
## Summary

For a displacement-versus-time graph:

1. Confirm that the horizontal axis is time.
2. Read the local slope at the marked instant from left to right.
3. Positive slope means up, negative slope means down, and zero slope means momentarily stopped vertically.
4. Do not use the displacement value alone to decide motion.
5. Keep transverse particle motion separate from the wave pattern's propagation direction.

The main trap is choosing “right” from the propagation arrow instead of choosing “down” from the negative displacement-time slope.
