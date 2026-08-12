# Normal Force at the Top of a Ferris Wheel

<!--
lesson-id: 212-M1-018
topic-code: MTH212.M1.18
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Inward Direction at the Top](#find-the-inward-direction-at-the-top)
- [Write the Top-Position Force Balance](#write-the-top-position-force-balance)
- [Calculate the Seat Force](#calculate-the-seat-force)
- [Compare with the Bottom of the Wheel](#compare-with-the-bottom-of-the-wheel)
- [Summary](#summary)

## Prerequisites

- Radial acceleration points toward the center of circular motion.
- For constant angular speed, radial acceleration has magnitude $a_r=r\omega^2$.
- Newton's second law in one direction is $\sum F=ma$.
- Near Earth's surface, weight has magnitude $mg$.

---

<a id="introduction"></a>
## Introduction

Riders often feel lighter at the top of a Ferris wheel and heavier at the bottom, even though their mass and the force of gravity have not changed. What changes is how strongly the seat pushes on them.

Moving in a circle requires an acceleration toward the center. At the top of the wheel, that acceleration is downward. Gravity still pulls downward with the same force, but the seat does not push upward as strongly as it would if the rider were at rest. The weaker upward force from the seat makes the rider feel lighter. This supporting force—the normal force—is what determines the rider’s apparent weight.

![](<../Source/Images/ferris-wheel-top-bottom-normal-force.png>)

Now consider a $68\ \mathrm{kg}$ rider seated at the top of a Ferris wheel with radius $42\ \mathrm{m}$ rotating at a constant angular speed of $0.16\ \mathrm{rad}/\mathrm{s}$. How strongly does the seat push upward on the rider?

---

<a id="find-the-inward-direction-at-the-top"></a>
## Find the Inward Direction at the Top

**Example:** A person rides at the top of a Ferris wheel. Which direction is inward?

**Explanation**

Inward always means "toward the center of the circle." At the top of the wheel, the center is below the rider, so inward is downward.

Along the inward axis, Newton's second law is

$$
\sum F_r=m a_r=m\frac{v^2}{r}=m\omega^2 r.
$$

```quiz
type: radio
id: q-top-inward-direction
shuffle: true
content: |-
  At the top of a vertical Ferris wheel, which direction is the required inward net force?
options:
- id: a
  content: |-
    Upward, away from the center
- id: b
  content: |-
    Downward, toward the center
  correct: true
- id: c
  content: |-
    Forward, tangent to the motion
- id: d
  content: |-
    Zero, because the angular speed is constant
```

---

<a id="write-the-top-position-force-balance"></a>
## Write the Top-Position Force Balance

**Example:** At the top of the wheel, write the vertical force balance for a rider of mass $m$ if the seat pushes upward with normal force $N$.

**Explanation**

At the top:

- Weight $mg$ points downward, so it points inward.
- The normal force $N$ from the seat points upward, so it points outward.

Before doing any algebra, predict the comparison: gravity already supplies part of the required inward force, so the seat should push less strongly than it would at rest. The result must satisfy $N<mg$.

Using inward as positive gives

$$
mg-N=m a_r=m\omega^2 r.
$$

Solving for the normal force gives

$$
N=mg-m\omega^2 r.
$$

```quiz
type: radio
id: q-top-force-balance
shuffle: true
content: |-
  A rider is at the top of a vertical circle. Inward is downward, weight is $mg$, and the seat's normal force is $N$ upward. Which force balance is correct?
options:
- id: a
  content: |-
    $N-mg=m a_r=m\omega^2 r$
- id: b
  content: |-
    $mg-N=m a_r=m\omega^2 r$
  correct: true
- id: c
  content: |-
    $N+mg=0$
- id: d
  content: |-
    $N=m\omega^2 r$
```

---

<a id="calculate-the-seat-force"></a>
## Calculate the Seat Force

**Example:** A Ferris wheel has radius $42\ \mathrm{m}$ and angular speed $0.16\ \mathrm{rad}/\mathrm{s}$. Find the normal force on a $68\ \mathrm{kg}$ rider at the top.

**Explanation**

At the top,

$$
N=mg-m\omega^2 r.
$$

The symbolic form $N=m(g-\omega^2 r)$ keeps the expected subtraction visible. Using $g=9.8\ \mathrm{m}/\mathrm{s}^2$, now substitute the rider's mass and the wheel's radius and angular speed:

$$
\begin{aligned}
N&=(68)(9.8)-(68)(0.16)^2(42)\\
&=666.4-73.1136\\
&=593.2864\ \mathrm{N}.
\end{aligned}
$$

To two significant figures, this is

$$
N\approx 5.9\times10^2\ \mathrm{N}=590\ \mathrm{N}.
$$

```quiz
type: radio
id: q-top-substitute
shuffle: true
content: |-
  A $50\ \mathrm{kg}$ rider is at the top of a Ferris wheel with $r=20\ \mathrm{m}$ and $\omega=0.30\ \mathrm{rad}/\mathrm{s}$. Using $g=9.8\ \mathrm{m}/\mathrm{s}^2$, what is the normal force?
options:
- id: a
  content: |-
    $400\ \mathrm{N}$
  correct: true
- id: b
  content: |-
    $490\ \mathrm{N}$
- id: c
  content: |-
    $580\ \mathrm{N}$
- id: d
  content: |-
    $90\ \mathrm{N}$
```

---

<a id="compare-with-the-bottom-of-the-wheel"></a>
## Compare with the Bottom of the Wheel

**Example:** Why is the top-position normal force smaller than the rider's weight?

**Explanation**

At the top, gravity already points inward. Gravity supplies part of the required inward force, so the seat does not need to push as hard as it would if the wheel were not rotating.

Because the normal force is the rider's apparent weight, the smaller value corresponds to feeling lighter. It does not imply a separate upward force: the rider tends to continue along the instantaneous tangent while the wheel curves downward beneath them.

That is why the formula is

$$
N=mg-m\omega^2 r.
$$

At the bottom, inward is upward, so the force balance would be different:

$$
N-mg=m a_r=m\omega^2 r.
$$

At the bottom, the seat must support the rider's weight and still produce an upward net force. Its normal force is therefore larger than $mg$, while the normal force at the top is smaller than $mg$.

```quiz
type: radio
id: q-top-bottom-trap
shuffle: true
content: |-
  A student solves the top-of-wheel problem by using $N=mg+m\omega^2 r$. What mistake did they make?
options:
- id: a
  content: |-
    They used the bottom-position force balance for a top-position rider.
  correct: true
- id: b
  content: |-
    They forgot that weight points downward at the top.
- id: c
  content: |-
    They treated angular speed as zero.
- id: d
  content: |-
    They computed the rider's mass instead of the normal force.
```

---

<a id="summary"></a>
## Summary

At the top of an upright Ferris-wheel gondola, the center is below the rider. Weight points inward while the seat's normal force points outward, so

$$
mg-N=m a_r=m\omega^2 r.
$$

Solving for the seat force gives

$$
N=mg-m\omega^2 r.
$$

Because $m\omega^2 r$ is positive, $N<mg$: the seat pushes less strongly than it would at rest, and the rider feels lighter. At the bottom, inward is upward and the directions reverse, giving $N-mg=m a_r=m\omega^2 r$ instead.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Comparing Normal Force and Weight at the Top of a Hill](../../2026-07-05-PQ-1/Lessons/Problem-3.md)

Study guide index: 19/35

---
<!-- lesson-nav:end -->
