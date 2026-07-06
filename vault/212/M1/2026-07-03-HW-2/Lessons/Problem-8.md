# Finding Uphill Friction on a Banked Curve

## Table of Contents

- [Introduction](#introduction)
- [Choose Components from the Given Friction Direction](#choose-components-from-the-given-friction-direction)
- [Write the Radial and Vertical Force Equations](#write-the-radial-and-vertical-force-equations)
- [Eliminate the Normal Force](#eliminate-the-normal-force)
- [Match the Formula to the Answer Choices](#match-the-formula-to-the-answer-choices)
- [Summary](#summary)

## Prerequisites

- Resolve a force into components parallel to vertical and radial directions.
- Use $a_r=\dfrac{v^2}{r}$ for uniform circular motion.
- Solve two linear force equations for an unknown force.

---

<a id="introduction"></a>
## Introduction

The cue in this problem is a car moving in a circle on a banked track, with the direction of static friction already given. That means the useful axes are vertical, where the car has no acceleration, and radial inward, where the net force must equal $\dfrac{mv^2}{r}$.

Determine the static friction force by resolving the normal force and the given uphill friction force into vertical and radial components, writing one force equation in each direction, and eliminating the normal force.

Use $f_s$ for the magnitude of static friction. Since the problem says friction points up the track, the final expression should be positive under the stated motion. If the algebra produced a negative value for a different situation, that would mean the assumed friction direction was wrong.

---

<a id="choose-components-from-the-given-friction-direction"></a>
## Choose Components from the Given Friction Direction

**Example:** A car moves on a circular track banked at angle $\theta$ from the horizontal. The normal force has magnitude $N$, and static friction of magnitude $f_s$ points up the track. With radial inward chosen as positive, write the vertical and radial components of $N$ and $f_s$.

**Explanation**

The normal force is perpendicular to the banked surface. For a bank angle $\theta$, the normal force tilts inward by $\theta$ from vertical, so

$$
N_y=N\cos\theta
$$

and

$$
N_r=N\sin\theta
$$

Friction points up the track. In the side view, up the track is upward and outward, so its vertical component is positive but its radial-inward component is negative:

$$
(f_s)_y=f_s\sin\theta
$$

$$
(f_s)_r=-f_s\cos\theta
$$

The sign checklist is:

- Normal force: up and inward.
- Uphill friction: up and outward.
- Radial inward is positive, so outward friction gets a minus sign.

```quiz
type: radio
id: p8-q1-components
content: |-
  A banked track has angle $\theta$ from the horizontal. Static friction points up the track. If radial inward is positive, which components are correct?
options:
- id: p8-q1-a
  content: |-
    $N_y=N\cos\theta$, $N_r=N\sin\theta$, $(f_s)_y=f_s\sin\theta$, $(f_s)_r=-f_s\cos\theta$
  correct: true
- id: p8-q1-b
  content: |-
    $N_y=N\sin\theta$, $N_r=N\cos\theta$, $(f_s)_y=f_s\cos\theta$, $(f_s)_r=-f_s\sin\theta$
- id: p8-q1-c
  content: |-
    $N_y=N\cos\theta$, $N_r=-N\sin\theta$, $(f_s)_y=f_s\sin\theta$, $(f_s)_r=f_s\cos\theta$
- id: p8-q1-d
  content: |-
    $N_y=N$, $N_r=0$, $(f_s)_y=0$, $(f_s)_r=f_s$
```

---

<a id="write-the-radial-and-vertical-force-equations"></a>
## Write the Radial and Vertical Force Equations

**Example:** Using the same banked-track setup, write the two force equations before solving for $f_s$.

**Explanation**

The car has radial acceleration inward:

$$
a_r=\dfrac{v^2}{r}
$$

So the inward force equation is

$$
N\sin\theta-f_s\cos\theta=\dfrac{mv^2}{r}
\tag{1}
$$

The car does not accelerate vertically, so the vertical forces balance:

$$
N\cos\theta+f_s\sin\theta-mg=0
$$

or

$$
N\cos\theta+f_s\sin\theta=mg
\tag{2}
$$

The main sign to check is the friction term in the radial equation. Because friction points outward when it points up the track, it subtracts from the inward centripetal force.

```quiz
type: radio
id: p8-q2-equations
content: |-
  For a car on a banked curve with friction pointing up the track, which pair of equations matches radial inward and vertical directions?
options:
- id: p8-q2-a
  content: |-
    $N\sin\theta-f_s\cos\theta=\dfrac{mv^2}{r}$ and $N\cos\theta+f_s\sin\theta=mg$
  correct: true
- id: p8-q2-b
  content: |-
    $N\sin\theta+f_s\cos\theta=\dfrac{mv^2}{r}$ and $N\cos\theta-f_s\sin\theta=mg$
- id: p8-q2-c
  content: |-
    $N\cos\theta-f_s\sin\theta=\dfrac{mv^2}{r}$ and $N\sin\theta+f_s\cos\theta=mg$
- id: p8-q2-d
  content: |-
    $N-f_s=\dfrac{mv^2}{r}$ and $N+f_s=mg$
```

---

<a id="eliminate-the-normal-force"></a>
## Eliminate the Normal Force

**Example:** Solve the two equations

$$
N\sin\theta-f_s\cos\theta=\dfrac{mv^2}{r}
$$

and

$$
N\cos\theta+f_s\sin\theta=mg
$$

for $f_s$.

**Explanation**

Treat every symbol except $f_s$ as known while solving. The goal is to remove $N$, just as you would isolate one variable in a many-variable equation.

Start with the vertical equation:

$$
N\cos\theta=mg-f_s\sin\theta
$$

Divide by $\cos\theta$:

$$
N=\dfrac{mg-f_s\sin\theta}{\cos\theta}
$$

Substitute this into the radial equation:

$$
\left(\dfrac{mg-f_s\sin\theta}{\cos\theta}\right)\sin\theta-f_s\cos\theta=\dfrac{mv^2}{r}
$$

Use $\tan\theta=\dfrac{\sin\theta}{\cos\theta}$:

$$
mg\tan\theta-f_s\dfrac{\sin^2\theta}{\cos\theta}-f_s\cos\theta=\dfrac{mv^2}{r}
$$

The two $f_s$ terms combine because

$$
\dfrac{\sin^2\theta}{\cos\theta}+\cos\theta
=\dfrac{\sin^2\theta+\cos^2\theta}{\cos\theta}
=\dfrac{1}{\cos\theta}
$$

So

$$
mg\tan\theta-\dfrac{f_s}{\cos\theta}=\dfrac{mv^2}{r}
$$

Now solve:

$$
\dfrac{f_s}{\cos\theta}=mg\tan\theta-\dfrac{mv^2}{r}
$$

$$
f_s=mg\sin\theta-\dfrac{mv^2}{r}\cos\theta
$$

```quiz
type: radio
id: p8-q3-eliminate
content: |-
  If $N\sin\theta-f_s\cos\theta=\dfrac{mv^2}{r}$ and $N\cos\theta+f_s\sin\theta=mg$, what is $f_s$?
options:
- id: p8-q3-a
  content: |-
    $mg\sin\theta-\dfrac{mv^2}{r}\cos\theta$
  correct: true
- id: p8-q3-b
  content: |-
    $mg\sin\theta+\dfrac{mv^2}{r}\cos\theta$
- id: p8-q3-c
  content: |-
    $mg\cos\theta-\dfrac{mv^2}{r}\sin\theta$
- id: p8-q3-d
  content: |-
    $mg-\dfrac{mv^2}{r}\cos\theta$
```

---

<a id="match-the-formula-to-the-answer-choices"></a>
## Match the Formula to the Answer Choices

**Example:** The original problem asks for the magnitude of static friction on an F1 car of mass $m$ moving with constant speed $v$ on a circular track of radius $r$, banked at angle $\theta$ from the horizontal. Friction points up the track. Choose the matching expression.

**Explanation**

From the force equations, the friction magnitude is

$$
f_s=mg\sin\theta-\dfrac{mv^2}{r}\cos\theta
$$

This expression has two useful checks:

- The $mg$ term must include $\sin\theta$, because only part of gravity's effect along the tilted geometry contributes to friction.
- The centripetal term is subtracted, because uphill friction points outward and therefore opposes the inward radial acceleration.

```quiz
type: radio
id: p8-q4-variant
content: |-
  A cart of mass $M$ moves at speed $u$ around a circular banked track of radius $R$. The bank angle is $\phi$, and friction points up the track. Which expression gives the static friction magnitude?
options:
- id: p8-q4-a
  content: |-
    $Mg\sin\phi-\dfrac{Mu^2}{R}\cos\phi$
  correct: true
- id: p8-q4-b
  content: |-
    $Mg\sin\phi+\dfrac{Mu^2}{R}\cos\phi$
- id: p8-q4-c
  content: |-
    $Mg\cos\phi-\dfrac{Mu^2}{R}\sin\phi$
- id: p8-q4-d
  content: |-
    $Mg-\dfrac{Mu^2}{R}\cos\phi$
```

```quiz
type: radio
id: p8-q5-original
content: |-
  The figure below shows an F1 sports car of mass $m$ traversing a circular track banked at angle $\theta$ from the horizontal with constant speed $v$. The track has radius $r$, and friction points up the track in the side-view. What is the magnitude of the static frictional force on the car?

  ![](<../Source/Images/banked-track-car-diagram.png>)
options:
- id: p8-q5-a
  content: |-
    $mg+\dfrac{mv^2}{r}\cos\theta$
- id: p8-q5-b
  content: |-
    $mg-\dfrac{mv^2}{r}\cos\theta$
- id: p8-q5-c
  content: |-
    $mg\sin\theta+\dfrac{mv^2}{r}\cos\theta$
- id: p8-q5-d
  content: |-
    $mg\sin\theta-\dfrac{mv^2}{r}\cos\theta$
  correct: true
```

---

## Summary

For a banked curve with friction pointing up the track:

1. Choose vertical and radial-inward axes.
2. Use $N_y=N\cos\theta$, $N_r=N\sin\theta$, $(f_s)_y=f_s\sin\theta$, and $(f_s)_r=-f_s\cos\theta$.
3. Write the two force equations:

$$
N\sin\theta-f_s\cos\theta=\dfrac{mv^2}{r}
$$

$$
N\cos\theta+f_s\sin\theta=mg
$$

4. Eliminate $N$ to get

$$
f_s=mg\sin\theta-\dfrac{mv^2}{r}\cos\theta
$$

The main trap is the sign of the radial friction component: uphill friction points outward on the bank, so it subtracts from the inward centripetal-force equation.
