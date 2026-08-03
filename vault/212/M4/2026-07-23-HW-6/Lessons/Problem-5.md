
# Ranking Acceleration Magnitudes from an SHM Position Graph

<!--
lesson-id: 212-M4-020
topic-code: MTH212.M4.20
-->

## Table of Contents

- [Introduction](#introduction)
- [Acceleration Magnitude Follows Distance from Equilibrium](#acceleration-magnitude-follows-distance-from-equilibrium)
- [Ignore the Sign of Position](#ignore-the-sign-of-position)
- [Do Not Rank by the Graph's Slope](#do-not-rank-by-the-graphs-slope)
- [Apply the Rule to the Homework Graph](#apply-the-rule-to-the-homework-graph)
- [Summary](#summary)

## Prerequisites

- Read a position value from a position-versus-time graph.
- Identify the equilibrium line $x=0$.
- Compare absolute values.

---

<a id="introduction"></a>
## Introduction

When one object is undergoing simple harmonic motion and a problem asks you to compare acceleration magnitudes at several times, read the object's distance from the equilibrium line $x=0$ at each time. The signed acceleration in simple harmonic motion is

$$
a=-\omega^2x.
$$

Taking the absolute value gives

$$
|a|=|-\omega^2x|=\omega^2|x|.
$$

The factor $\omega^2$ is the same positive number at every time for the same oscillator, so it cannot change the order. Thus, ranking the acceleration magnitudes is exactly the same as ranking the distances $|x|$ from equilibrium. In the rankings below, symbols such as $a_P$ denote acceleration magnitudes.

---

<a id="acceleration-magnitude-follows-distance-from-equilibrium"></a>
## Acceleration Magnitude Follows Distance from Equilibrium

**Example:** At one instant, an oscillator is at $x_P=0.30\ \mathrm{m}$. At another instant, it is at $x_Q=-1.10\ \mathrm{m}$. Compare the acceleration magnitudes $a_P$ and $a_Q$.

**Explanation**

Compare the absolute positions:

$$
|x_P|=0.30\ \mathrm{m},
\qquad
|x_Q|=1.10\ \mathrm{m}.
$$

Because $0.30<1.10$, multiplying both values by the same positive factor $\omega^2$ preserves the order:

$$
a_P<a_Q.
$$

You do not need to know $\omega$ to make this comparison.

```quiz
type: radio
id: p5-distance-q1
content: |-
  The same oscillator is at $x_R=0.20\ \mathrm{m}$, $x_S=-0.75\ \mathrm{m}$, and $x_T=1.25\ \mathrm{m}$ at three different times. Let $a_R,a_S,a_T$ be the corresponding acceleration magnitudes. Which ranking is correct?
options:
- id: p5-distance-q1-a
  content: |-
    $a_R<a_S<a_T$
  correct: true
  feedback: |-
    For one oscillator, acceleration magnitude grows with distance from equilibrium: $|a|=\omega^2|x|$. The distances are $0.20\ \mathrm{m}<0.75\ \mathrm{m}<1.25\ \mathrm{m}$, so $a_R<a_S<a_T$.
- id: p5-distance-q1-b
  content: |-
    $a_S<a_R<a_T$
  feedback: |-
    This lets the negative sign of $x_S$ make its magnitude seem smaller. Magnitude uses distance from equilibrium: $|x_S|=0.75\ \mathrm{m}>|x_R|=0.20\ \mathrm{m}$, so $a_S>a_R$, while $T$ remains greatest.
- id: p5-distance-q1-c
  content: |-
    $a_T<a_S<a_R$
  feedback: |-
    This reverses the distance-from-equilibrium ranking. Since $|a|=\omega^2|x|$, the farthest point $T$ has the greatest magnitude and the nearest point $R$ has the least: $a_R<a_S<a_T$.
- id: p5-distance-q1-d
  content: |-
    $a_R<a_T<a_S$
  feedback: |-
    This correctly places $R$ first but swaps $S$ and $T$. Point $T$ is farther from equilibrium because $|x_T|=1.25\ \mathrm{m}>|x_S|=0.75\ \mathrm{m}$, so $a_T>a_S$.
```

---

<a id="ignore-the-sign-of-position"></a>
## Ignore the Sign of Position

**Example:** An oscillator is at $x_U=+0.90\ \mathrm{m}$ and later at $x_V=-0.90\ \mathrm{m}$. Compare its acceleration magnitudes.

**Explanation**

The accelerations point in opposite directions because $a=-\omega^2x$, but their magnitudes are equal:

$$
a_U=\omega^2|+0.90\ \mathrm{m}|
=\omega^2|-0.90\ \mathrm{m}|=a_V.
$$

For a magnitude ranking, positions equally far above and below $x=0$ tie.

```quiz
type: radio
id: p5-sign-q1
content: |-
  At three times, an oscillator has positions $x_L=-0.60\ \mathrm{m}$, $x_M=+0.20\ \mathrm{m}$, and $x_N=+0.60\ \mathrm{m}$. Let $a_L,a_M,a_N$ be the acceleration magnitudes. Which ranking is correct?
options:
- id: p5-sign-q1-a
  content: |-
    $a_L<a_M<a_N$
  feedback: |-
    This copies the order of the signed positions instead of comparing magnitudes. Acceleration magnitude depends on $|x|$: $M$ is only $0.20\ \mathrm{m}$ from equilibrium, while $L$ and $N$ are both $0.60\ \mathrm{m}$ away, so $a_M<a_L=a_N$.
- id: p5-sign-q1-b
  content: |-
    $a_M<a_L=a_N$
  correct: true
  feedback: |-
    Acceleration magnitude depends on distance from equilibrium, not side: $|a|=\omega^2|x|$. Point $M$ is closest, while $L$ and $N$ are equally far away on opposite sides, so $a_M<a_L=a_N$.
- id: p5-sign-q1-c
  content: |-
    $a_L=a_M<a_N$
  feedback: |-
    A tie requires equal distances from equilibrium. Points $L$ and $M$ are $0.60\ \mathrm{m}$ and $0.20\ \mathrm{m}$ away, so they do not tie; the equal-distance pair is $L$ and $N$, giving $a_M<a_L=a_N$.
- id: p5-sign-q1-d
  content: |-
    $a_N<a_M<a_L$
  feedback: |-
    This ranks signed accelerations rather than their magnitudes. Although the accelerations at $L$ and $N$ point in opposite directions, both positions are $0.60\ \mathrm{m}$ from equilibrium, so $a_L=a_N$; point $M$ has the smaller magnitude.
- id: p5-sign-q1-e
  content: |-
    $a_L<a_N<a_M$
  feedback: |-
    This makes the nearest point largest and separates two equal distances. Point $M$ is closest to equilibrium, so its acceleration magnitude is smallest; $|x_L|=|x_N|$, so the corrected ranking is $a_M<a_L=a_N$.
```

---

<a id="do-not-rank-by-the-graphs-slope"></a>
## Do Not Rank by the Graph's Slope

**Example:** Compare the acceleration magnitude at an equilibrium crossing with the acceleration magnitude at a turning point.

**Explanation**

At an equilibrium crossing, $x=0$, so

$$
|a|=\omega^2|0|=0.
$$

At a turning point, $|x|=A$, so

$$
|a|=\omega^2A,
$$

its maximum value. The position graph is steepest near equilibrium and flat at a turning point, but that slope describes velocity, not acceleration magnitude. For this comparison, use the vertical distance from the $x=0$ line.

| Location on the position graph | Distance from equilibrium | Acceleration magnitude |
| --- | ---: | ---: |
| Equilibrium crossing | $0$ | $0$ |
| Intermediate point | $d$, where $0<d<A$ | $\omega^2d$ |
| Either turning point | $A$ | $\omega^2A$, the maximum |

```quiz
type: radio
id: p5-slope-q1
content: |-
  Point $E$ is an equilibrium crossing, point $H$ has $|x|=0.4A$, and point $J$ is a turning point of the same SHM position graph. Let $a_E,a_H,a_J$ be the acceleration magnitudes. Which ranking is correct?
options:
- id: p5-slope-q1-a
  content: |-
    $a_J<a_H<a_E$
  feedback: |-
    This is the ranking of speed magnitudes inferred from the graph's slope: speed is greatest at equilibrium and zero at a turning point. Acceleration magnitude instead follows the graph's vertical distance from $x=0$, so $a_E<a_H<a_J$.
- id: p5-slope-q1-b
  content: |-
    $a_E<a_J<a_H$
  feedback: |-
    This correctly makes the equilibrium crossing least but swaps $H$ and $J$. The turning point is $A$ from equilibrium, farther than $H$ at $0.4A$, so $a_J>a_H$.
- id: p5-slope-q1-c
  content: |-
    $a_E<a_H<a_J$
  correct: true
  feedback: |-
    On a position graph, acceleration magnitude follows vertical distance from equilibrium, not slope. The distances at $E$, $H$, and $J$ are $0$, $0.4A$, and $A$, so $a_E<a_H<a_J$.
- id: p5-slope-q1-d
  content: |-
    $a_H<a_E<a_J$
  feedback: |-
    This fails to make the equilibrium crossing the minimum. At $E$, the graph's value is $x=0$, so $a_E=0$ even though the graph's slope—and therefore speed—is greatest there; thus $a_E<a_H<a_J$.
- id: p5-slope-q1-e
  content: |-
    $a_E=a_H=a_J$
  feedback: |-
    Angular frequency is constant, but acceleration magnitude is not. Since $|a|=\omega^2|x|$, the different vertical distances $0$, $0.4A$, and $A$ produce $a_E<a_H<a_J$, not a tie.
```

---

<a id="apply-the-rule-to-the-homework-graph"></a>
## Apply the Rule to the Homework Graph

**Example:** On the graph below, compare the acceleration magnitudes at $t=1\ \mathrm{s}$, $4\ \mathrm{s}$, and $7\ \mathrm{s}$.

![](<../Source/2026-07-23-HW-6/Images/simple-harmonic-motion-position-time-graph.png>)

**Explanation**

For each time, move vertically from the time axis to the red curve, then read the position from the vertical axis. Record the signed position first and take its absolute value second.

| Time            |   Position read from the graph |               Distance from equilibrium |
| --------------- | -----------------------------: | --------------------------------------: |
| $1\ \mathrm{s}$ |  $x(1)\approx 1.3\ \mathrm{m}$ | $\lvert x(1)\rvert\approx 1.3\ \mathrm{m}$ |
| $4\ \mathrm{s}$ | $x(4)\approx -0.7\ \mathrm{m}$ | $\lvert x(4)\rvert\approx 0.7\ \mathrm{m}$ |
| $7\ \mathrm{s}$ | $x(7)\approx -0.2\ \mathrm{m}$ | $\lvert x(7)\rvert\approx 0.2\ \mathrm{m}$ |

Their distances from equilibrium satisfy

$$
|x(7)|<|x(4)|<|x(1)|.
$$

Therefore, the acceleration magnitudes have the same order:

$$
a_7<a_4<a_1.
$$

```quiz
type: radio
id: p5-homework-q1
shuffle: true
content: |-
  The plot below shows the $x$-component of the position of a block undergoing simple harmonic motion.

  Let $a_2$, $a_5$, $a_8$ denote the magnitudes of the accelerations of the block at $t=2\ \mathrm{s}$, $5\ \mathrm{s}$, $8\ \mathrm{s}$ respectively.

  Which of the following is the correct ranking of these magnitudes from least to greatest?

  ![](<../Source/2026-07-23-HW-6/Images/simple-harmonic-motion-position-time-graph.png>)
options:
- id: p5-homework-q1-a
  content: |-
    $a_2<a_5<a_8$
  correct: true
  feedback: |-
    Acceleration magnitude follows the graph's vertical distance from the equilibrium line: $|a|=\omega^2|x|$. The curve is closest to $x=0$ at $2\ \mathrm{s}$, farther away at $5\ \mathrm{s}$, and farthest away at $8\ \mathrm{s}$, so $a_2<a_5<a_8$.
- id: p5-homework-q1-b
  content: |-
    $a_2<a_8<a_5$
  feedback: |-
    This correctly places $2\ \mathrm{s}$ first but swaps the other two times. The graph's value at $8\ \mathrm{s}$ is farther from $x=0$ than its value at $5\ \mathrm{s}$, so $a_8>a_5$.
- id: p5-homework-q1-c
  content: |-
    $a_5<a_2<a_8$
  feedback: |-
    This swaps the first two times. The graph's value at $2\ \mathrm{s}$ is closer to the $x=0$ line than its value at $5\ \mathrm{s}$, so $a_2<a_5$; time $8\ \mathrm{s}$ is still greatest.
- id: p5-homework-q1-d
  content: |-
    $a_5<a_8<a_2$
  feedback: |-
    This places $2\ \mathrm{s}$ last even though the curve is closest to equilibrium there. Because acceleration magnitude follows vertical distance from $x=0$, $a_2$ must be least; the full ranking is $a_2<a_5<a_8$.
- id: p5-homework-q1-e
  content: |-
    $a_8<a_2<a_5$
  feedback: |-
    This copies the order of the signed graph values, $x(8)<x(2)<x(5)$, instead of comparing magnitudes. Acceleration magnitudes ignore which side of equilibrium a point lies on and use $|x|$, giving $a_2<a_5<a_8$.
- id: p5-homework-q1-f
  content: |-
    $a_8<a_5<a_2$
  feedback: |-
    This reverses the graph's distance-from-equilibrium order. The curve is closest to $x=0$ at $2\ \mathrm{s}$ and farthest away at $8\ \mathrm{s}$, so acceleration magnitude must increase as $a_2<a_5<a_8$.
```

---

<a id="summary"></a>
## Summary

When a single SHM position graph asks for a ranking of acceleration magnitudes:

1. At each requested time, move vertically to the curve and read the signed position $x$.
2. Convert each position to its distance from equilibrium by taking $|x|$.
3. Rank those distances from least to greatest.
4. Use the same order for the acceleration magnitudes because $|a|=\omega^2|x|$.

Do not rank signed positions, and do not use the graph's slope. Equal distances on opposite sides of equilibrium produce equal acceleration magnitudes.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../../M5/2026-08-03-Q-3/Study-Guide.md)
Next: [Deciding Whether an SHM Oscillator Is Speeding Up or Slowing Down](../../../M5/2026-08-03-Q-3/Lessons/shm-speeding-up-or-slowing-down.md)

Study guide index: 03/28

---
<!-- lesson-nav:end -->
