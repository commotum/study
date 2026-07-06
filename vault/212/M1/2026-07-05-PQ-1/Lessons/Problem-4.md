# Finding the Minimum Period Before a Coin Slips

<!--
lesson-id: 212-M1-015
topic-code: MTH212.M1.15
-->

## Table of Contents

- [Introduction](#introduction)
- [Draw the Forces on the Coin](#draw-the-forces-on-the-coin)
- [Use Static Friction as the Radial Force](#use-static-friction-as-the-radial-force)
- [Convert the Speed Limit to a Period](#convert-the-speed-limit-to-a-period)
- [Read "Smallest Period" as a Threshold](#read-smallest-period-as-a-threshold)
- [Summary](#summary)

## Prerequisites

- Know that circular motion needs inward radial acceleration $a_r=v^2/r$.
- Know that static friction can have any size up to $f_{s,\max}=\mu_s N$.
- Know that period and speed are related by $v=2\pi r/T$.
- Be able to write Newton's second law separately in vertical and radial directions.

---

<a id="introduction"></a>
## Introduction

A coin sits on a horizontal turntable at radius $r$ while the table spins at constant angular speed.

![](<../Source/Images/problem-4-turntable.png>)

The cue is that the coin is moving in a circle but is not sliding across the turntable. The only horizontal contact force available is static friction, so static friction must point inward and supply the centripetal force.

To find the smallest period that avoids slipping, use the threshold case:

$$
f_s=f_{s,\max}.
$$

Then connect that maximum friction force to circular motion and solve for $T$.

Use this order:

1. Draw $N$, $mg$, and inward $f_s$.
2. Use vertical balance to get $N=mg$.
3. Set the required radial force equal to the maximum static friction at the threshold.
4. Substitute $v=2\pi r/T$.
5. Interpret the result as the smallest allowed period.

---

<a id="draw-the-forces-on-the-coin"></a>
## Draw the Forces on the Coin

**Example:** A coin is resting on a horizontal turntable and moving in a circle at constant height. What forces belong on the free-body diagram?

**Explanation**

Use one vertical axis and one radial axis:

- $N$ points upward.
- $mg$ points downward.
- $f_s$ points radially inward, toward the center of the turntable.

There is no outward force on the coin. "Outward" is the direction the coin would fail to stay with the turntable if friction were not large enough, but the force causing circular motion is inward.

Because the coin has no vertical acceleration,

$$
\sum F_y=0=N-mg,
$$

so

$$
N=mg.
$$

A consistent free-body diagram has $N$ and $mg$ with equal vertical lengths, and the static-friction vector along the inward radial axis.

![](<../Source/Images/problem-4-free-body-diagram.png>)

```quiz
type: radio
id: p4-fbd-forces
shuffle: true
content: |-
  A coin rides without slipping on a horizontal turntable. Which force list and direction choice matches the free-body diagram?
options:
- id: p4-fbd-forces-a
  content: |-
    $N$ up, $mg$ down, and $f_s$ inward toward the center
  correct: true
  feedback: |-
    Static friction is the only horizontal force, so it supplies the inward radial force.
- id: p4-fbd-forces-b
  content: |-
    $N$ up, $mg$ down, and $f_s$ outward away from the center
  feedback: |-
    Outward is the slipping tendency, not the direction of the real static-friction force.
- id: p4-fbd-forces-c
  content: |-
    $N$ up, $mg$ down, and no horizontal force
  feedback: |-
    Circular motion requires a nonzero inward net force.
- id: p4-fbd-forces-d
  content: |-
    $N$ up, $mg$ down, $f_s$ inward, and an extra outward centripetal force
  feedback: |-
    Centripetal force is not an extra force. It is the inward net force.
```

---

<a id="use-static-friction-as-the-radial-force"></a>
## Use Static Friction as the Radial Force

**Example:** A coin of mass $m$ moves at speed $v$ in a circle of radius $r$ on a horizontal turntable. The coefficient of maximum static friction is $\mu_s$. Write the radial force equation at the slipping threshold.

**Explanation**

The radial direction is inward. Static friction is the only radial force, so

$$
\sum F_r=f_s=\frac{mv^2}{r}.
$$

At the threshold of slipping, static friction has reached its maximum possible value:

$$
f_s=f_{s,\max}=\mu_s N.
$$

From the vertical balance, $N=mg$. Substitute that into the maximum-friction expression:

$$
f_{s,\max}=\mu_s mg.
$$

At the threshold,

$$
\frac{mv^2}{r}=\mu_s mg.
$$

The mass cancels, leaving

$$
v^2=\mu_s g r.
$$

```quiz
type: radio
id: p4-threshold-equation
shuffle: true
content: |-
  A coin is just about to slip on a horizontal turntable. Which threshold equation correctly connects static friction to circular motion?
options:
- id: p4-threshold-equation-a
  content: |-
    $\dfrac{mv^2}{r}=\mu_s mg$
  correct: true
  feedback: |-
    Static friction is at its maximum, and $N=mg$ on a horizontal surface.
- id: p4-threshold-equation-b
  content: |-
    $\dfrac{mv^2}{r}=mg$
  feedback: |-
    This uses weight as the radial force, but weight is vertical.
- id: p4-threshold-equation-c
  content: |-
    $\dfrac{mv^2}{r}=\mu_s m$
  feedback: |-
    The maximum static-friction force is $\mu_s N$, not $\mu_s m$.
- id: p4-threshold-equation-d
  content: |-
    $\dfrac{mv}{r}=\mu_s mg$
  feedback: |-
    The centripetal acceleration is $v^2/r$, not $v/r$.
```

```quiz
type: radio
id: p4-friction-limit
shuffle: true
content: |-
  Before a coin slips, which statement best describes the relationship between the required radial force and static friction?
options:
- id: p4-friction-limit-a
  content: |-
    The required radial force is $mv^2/r$, static friction supplies it, and slipping begins when $mv^2/r=\mu_s mg$.
  correct: true
  feedback: |-
    Static friction adjusts up to its maximum value, then the threshold is reached.
- id: p4-friction-limit-b
  content: |-
    Static friction is always equal to $\mu_s mg$, even at slow speeds.
  feedback: |-
    Static friction is only equal to its maximum value at the slipping threshold.
- id: p4-friction-limit-c
  content: |-
    The required radial force is $\mu_s mg$, and static friction is $mv^2/r$ only after slipping starts.
  feedback: |-
    This reverses the roles. The required radial force is $mv^2/r$.
- id: p4-friction-limit-d
  content: |-
    The required radial force is zero because the coin has constant speed.
  feedback: |-
    Constant speed still has inward acceleration when the direction of velocity changes.
```

---

<a id="convert-the-speed-limit-to-a-period"></a>
## Convert the Speed Limit to a Period

**Example:** Use $v^2=\mu_s g r$ to find the period at the slipping threshold.

**Explanation**

First take the positive speed:

$$
v=\sqrt{\mu_s g r}.
$$

For one full circle in one period,

$$
v=\frac{2\pi r}{T}.
$$

Set the threshold speed equal to the circular-motion speed:

$$
\frac{2\pi r}{T}=\sqrt{\mu_s g r}.
$$

Solve for $T$:

$$
T=\frac{2\pi r}{\sqrt{\mu_s g r}}.
$$

Simplify the factor of $r$:

$$
T=2\pi\sqrt{\frac{r}{\mu_s g}}.
$$

```quiz
type: radio
id: p4-period-expression
shuffle: true
content: |-
  A coin at radius $r$ is at the slipping threshold on a horizontal turntable. If $v=\sqrt{\mu_s g r}$ and $v=2\pi r/T$, what is the threshold period?
options:
- id: p4-period-expression-a
  content: |-
    $T=2\pi\sqrt{\dfrac{r}{\mu_s g}}$
  correct: true
  feedback: |-
    Solve $2\pi r/T=\sqrt{\mu_s g r}$ for $T$.
- id: p4-period-expression-b
  content: |-
    $T=2\pi\sqrt{\dfrac{\mu_s g}{r}}$
  feedback: |-
    This inverts the fraction inside the square root.
- id: p4-period-expression-c
  content: |-
    $T=\dfrac{\sqrt{\mu_s g r}}{2\pi r}$
  feedback: |-
    This is $1/T$, not $T$.
- id: p4-period-expression-d
  content: |-
    $T=2\pi\sqrt{\dfrac{m r}{\mu_s g}}$
  feedback: |-
    The mass cancels from the force equation.
```

---

<a id="read-smallest-period-as-a-threshold"></a>
## Read "Smallest Period" as a Threshold

**Example:** Why does the answer use equality if the question asks for the smallest period that avoids slipping?

**Explanation**

Smaller period means faster rotation:

$$
v=\frac{2\pi r}{T}.
$$

Faster rotation requires more inward force:

$$
\frac{mv^2}{r}.
$$

The coin does not slip as long as the required radial force is no larger than the maximum static friction:

$$
\frac{mv^2}{r}\le \mu_s mg.
$$

Substitute $v=2\pi r/T$:

$$
\frac{m}{r}\left(\frac{2\pi r}{T}\right)^2\le \mu_s mg.
$$

Cancel $m$ and simplify:

$$
\frac{4\pi^2 r}{T^2}\le \mu_s g.
$$

Solving gives

$$
T^2\ge \frac{4\pi^2 r}{\mu_s g},
$$

so

$$
T\ge 2\pi\sqrt{\frac{r}{\mu_s g}}.
$$

The smallest allowed period is the boundary value:

$$
T_{\min}=2\pi\sqrt{\frac{r}{\mu_s g}}.
$$

```quiz
type: radio
id: p4-minimum-period
shuffle: true
content: |-
  For a coin not to slip on a turntable, which statement correctly describes the allowed periods?
options:
- id: p4-minimum-period-a
  content: |-
    $T\ge 2\pi\sqrt{\dfrac{r}{\mu_s g}}$, so the smallest allowed period is $2\pi\sqrt{\dfrac{r}{\mu_s g}}$
  correct: true
  feedback: |-
    Periods smaller than this require too much inward force.
- id: p4-minimum-period-b
  content: |-
    $T\le 2\pi\sqrt{\dfrac{r}{\mu_s g}}$, so any faster spin is safe
  feedback: |-
    Smaller $T$ means larger speed and a larger required friction force.
- id: p4-minimum-period-c
  content: |-
    $T=2\pi\sqrt{\dfrac{\mu_s g}{r}}$, because friction increases the period directly
  feedback: |-
    The fraction is inverted. Greater $\mu_s$ allows a smaller period.
- id: p4-minimum-period-d
  content: |-
    There is no minimum period because static friction always adjusts to whatever value is needed
  feedback: |-
    Static friction adjusts only up to $f_{s,\max}=\mu_s N$.
```

---

<a id="summary"></a>
## Summary

For a coin on a horizontal turntable, use the circular path as the cue: static friction points inward and supplies the centripetal force. The vertical forces balance, so

$$
N=mg.
$$

At the slipping threshold,

$$
\frac{mv^2}{r}=f_{s,\max}=\mu_s N=\mu_s mg.
$$

Cancel $m$, use $v=2\pi r/T$, and solve:

$$
T_{\min}=2\pi\sqrt{\frac{r}{\mu_s g}}.
$$

The main trap is the word "smallest." Smaller period means larger speed, so the no-slip condition is $T\ge T_{\min}$, not $T\le T_{\min}$.

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Comparing Ferris Wheel Normal Forces](<../../2026-06-29-M1-3/Lessons/Problem-1.md>)

Study guide index: 15/30

<!-- study-guide-nav:end -->
