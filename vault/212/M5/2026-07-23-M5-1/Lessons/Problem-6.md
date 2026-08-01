# Finding Where a Wave Particle Moves Fastest

## Table of Contents

- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Read Particle Speed From Local Slope](#read-particle-speed-from-local-slope)
- [Separate Height From Speed](#separate-height-from-speed)
- [Separate Direction From Speed](#separate-direction-from-speed)
- [Apply the Slope Test to Problem 6](#apply-the-slope-test-to-problem-6)
- [Summary](#summary)

## Prerequisites

- Interpret the sign and magnitude of a graph's local slope.
- Distinguish the motion of a wave pattern from the motion of a particle in the medium.
- Recognize crests, troughs, and equilibrium crossings on a wave snapshot.

---

<a id="introduction"></a>
## Introduction

**Recognition cue:** A problem shows a snapshot of a traveling wave and asks which labeled particle of the medium is moving fastest at that instant.

**Single move:** Compare the magnitudes of the local slopes at the labeled points. The point with the steepest tangent has the greatest transverse particle speed; displacement height and slope sign do not determine speed.

---

<a id="read-particle-speed-from-local-slope"></a>
## Read Particle Speed From Local Slope

**Recognition cue:** The problem shows a snapshot of a traveling wave and asks where a particle of the string is moving fastest.

For a wave traveling to the right with speed $v_{\mathrm{wave}}$,

$$
v_y=-v_{\mathrm{wave}}\frac{\partial y}{\partial x}.
$$

The particle's **speed** is the magnitude of its vertical velocity:

$$
|v_y|=v_{\mathrm{wave}}\left|\frac{\partial y}{\partial x}\right|.
$$

Because $v_{\mathrm{wave}}$ is the same at every labeled point, compare only the magnitude of the local slope. The steepest point has the greatest particle speed.

Use the **tiny tangent test** at each labeled point:

1. Imagine a short tangent line touching the curve at the point.
2. Ignore whether it rises or falls and compare its steepness.
3. Choose the point whose tangent is farthest from horizontal.

This is a local test. Do not average the slope over an entire hump of the wave.

**Example:** At one instant, three points on a wave have local slopes $0$, $+2$, and $-5$. The point with slope $-5$ is moving fastest because $|-5|$ is greatest.

**Explanation**

Speed depends on slope magnitude, so the sign of the slope does not matter for this comparison.

```quiz
type: radio
id: p6-largest-slope
content: |-
  Four points on the same traveling wave have local slopes $-1$, $0$, $+4$, and $-3$. At which point is the particle speed greatest?
options:
- id: p6-largest-slope-a
  content: |-
    The point with slope $-1$
- id: p6-largest-slope-b
  content: |-
    The point with slope $0$
- id: p6-largest-slope-c
  content: |-
    The point with slope $+4$
  correct: true
- id: p6-largest-slope-d
  content: |-
    The point with slope $-3$
feedback: |-
  Compare absolute values: $1$, $0$, $4$, and $3$. The greatest is $4$, so the point with slope $+4$ has the greatest particle speed. The sign changes direction, not speed.
```

---

<a id="separate-height-from-speed"></a>
## Separate Height From Speed

The graph shows the string's displacement $y$ at each horizontal position $x$. It does **not** directly show particle speed.

At a smooth crest or trough, the graph is locally horizontal:

$$
\frac{\partial y}{\partial x}=0
\quad\Longrightarrow\quad
|v_y|=0.
$$

For a sinusoidal wave, the slope magnitude is greatest at an equilibrium crossing. That is where particles move fastest at that instant.

The graph-reading contrast is

| Feature of the snapshot | Displacement magnitude $|y|$ | Slope magnitude $|\partial y/\partial x|$ | Particle speed |
| --- | --- | --- | --- |
| Smooth crest or trough | Greatest | $0$ | $0$ |
| Steep equilibrium crossing | $0$ | Greatest | Greatest |

**Example:** Compare a particle at a crest with a particle at a steep equilibrium crossing. The crest particle has maximum displacement but zero instantaneous speed. The particle at the steep crossing has zero displacement but maximum speed.

**Explanation**

Maximum displacement and maximum speed occur at different places in the snapshot.

```quiz
type: radio
id: p6-height-trap
content: |-
  In a sinusoidal-wave snapshot, which point is instantaneously at rest?
options:
- id: p6-height-trap-a
  content: |-
    A point at a crest
  correct: true
- id: p6-height-trap-b
  content: |-
    A point at a steep equilibrium crossing
- id: p6-height-trap-c
  content: |-
    Every point below the equilibrium line
- id: p6-height-trap-d
  content: |-
    Every point where the displacement is zero
feedback: |-
  A smooth crest or trough has a horizontal tangent, so $\partial y/\partial x=0$ and the particle is instantaneously at rest. A zero-displacement crossing is usually steep, so it is not at rest.
```

---

<a id="separate-direction-from-speed"></a>
## Separate Direction From Speed

The sign in

$$
v_y=-v_{\mathrm{wave}}\frac{\partial y}{\partial x}
$$

determines the particle's vertical direction for a right-moving wave:

| Local slope | Particle velocity $v_y$ |
| --- | --- |
| Positive | Negative: downward |
| Negative | Positive: upward |
| Zero | Zero: instantaneously at rest |

Direction uses the sign of the slope; speed uses its magnitude.

The units also check the relationship:

$$
[v_y]
=\left[ v_{\mathrm{wave}}\frac{\partial y}{\partial x}\right]
=\frac{\mathrm{length}}{\mathrm{time}}
\frac{\mathrm{length}}{\mathrm{length}}
=\frac{\mathrm{length}}{\mathrm{time}}.
$$

**Example:** Two points have slopes $+3$ and $-3$. Their particles move in opposite vertical directions, but their speeds are equal because the slope magnitudes are equal.

**Explanation**

Do not choose the most negative slope automatically. Compare absolute values when the question asks for speed.

```quiz
type: radio
id: p6-direction-versus-speed
content: |-
  On a right-moving wave, point $P$ has slope $+2$ and point $Q$ has slope $-2$. Which statement is correct?
options:
- id: p6-direction-versus-speed-a
  content: |-
    $P$ and $Q$ have equal particle speeds but opposite vertical velocities.
  correct: true
- id: p6-direction-versus-speed-b
  content: |-
    $Q$ has the greater particle speed because its slope is negative.
- id: p6-direction-versus-speed-c
  content: |-
    $P$ has the greater particle speed because its slope is positive.
- id: p6-direction-versus-speed-d
  content: |-
    Both particles are instantaneously at rest.
feedback: |-
  The equal slope magnitudes give equal speeds. For a right-moving wave, the minus sign makes the positive-slope point move downward and the negative-slope point move upward.
```

---

<a id="apply-the-slope-test-to-problem-6"></a>
## Apply the Slope Test to Problem 6

**Example:** A wave propagates to the right along the string shown. At which labeled position is a particle moving fastest?

![](<../Source/Images/right-moving-wave-labeled-points.png>)

**Explanation**

Compare the magnitude of the graph's slope at the four labeled points:

- At $B$, the wave is at a crest, so the slope and particle speed are zero.
- At $A$ and $D$, the graph is sloped, so those particles are moving.
- At $C$, the graph has the greatest slope magnitude among the labeled points.

Equivalently, imagining a tiny tangent at each point shows that $C$ has the tangent farthest from horizontal. Its negative slope determines upward motion for this right-moving wave, but only its slope magnitude determines that it is fastest.

Therefore, the particle at **C** is moving fastest. For this speed comparison, the arrow showing that the wave moves right is not needed; it would be needed to determine whether a particle moves up or down.

```quiz
type: radio
id: p6-source-check
shuffle: true
content: |-
  **Question 5**

  A wave propagates to the right along the string shown. At which labeled position is a particle moving fastest?

  ![](<../Source/Images/right-moving-wave-labeled-points.png>)
options:
- id: p6-source-check-a
  content: A
- id: p6-source-check-b
  content: B
- id: p6-source-check-c
  content: C
  correct: true
  feedback: For a right-moving wave, $|v_y|=v_{\mathrm{wave}}|\partial y/\partial x|$. Point C lies where the magnitude of the slope is greatest, so its particle speed is greatest.
- id: p6-source-check-d
  content: D
```

---

## Summary

- Cue: a traveling-wave snapshot asks for a particle's speed.
- Rule: compare $|\partial y/\partial x|$ because $|v_y|=v_{\mathrm{wave}}|\partial y/\partial x|$.
- Procedure: imagine a tiny tangent at each labeled point, compare absolute slopes, and choose the tangent farthest from horizontal.
- Fastest point: the labeled point where the graph is locally steepest.
- Stationary point: a smooth crest or trough, where the slope is zero.
- Main trap: do not confuse greatest displacement with greatest particle speed.
