# Normal Force at the Top of a Ferris Wheel

<!--
lesson-id: 212-M1-018
topic-code: MTH212.M1.18
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Inward Direction at the Top](#find-the-inward-direction-at-the-top)
- [Write the Top-Position Force Balance](#write-the-top-position-force-balance)
- [Substitute Angular Speed into the Force Balance](#substitute-angular-speed-into-the-force-balance)
- [Avoid the Bottom-Position Sign Error](#avoid-the-bottom-position-sign-error)
- [Summary](#summary)

## Prerequisites

- Centripetal acceleration points toward the center of circular motion.
- For constant angular speed, centripetal acceleration has magnitude $a_c=\omega^2r$.
- Newton's second law in one direction is $\sum F=ma$.
- Near Earth's surface, weight has magnitude $mg$.

---

<a id="introduction"></a>
## Introduction

When a rider is at the top of a Ferris wheel, the center of the circle is below the rider. That means the required centripetal force points downward. The useful move is to choose inward as positive, put every vertical force into that direction, and solve the force balance for the normal force.

![](<../Source/Images/ferris-wheel-top-bottom-normal-force.png>)

For the assignment problem, the given values are

$$
r=42\ \mathrm{m},\qquad \omega=0.16\ \mathrm{rad}/\mathrm{s},\qquad m=68\ \mathrm{kg}.
$$

The target is the magnitude of the normal force from the seat at the top.

---

<a id="find-the-inward-direction-at-the-top"></a>
## Find the Inward Direction at the Top

**Example:** A person rides at the top of a Ferris wheel. Which direction is inward?

**Explanation**

Inward always means "toward the center of the circle." At the top of the wheel, the center is below the rider, so inward is downward.

That direction matters because the net inward force must equal $m\omega^2r$:

$$
\sum F_{\text{inward}}=m\omega^2r.
$$

```quiz
type: radio
id: q-top-inward-direction
shuffle: true
content: |-
  At the top of a vertical Ferris wheel, which direction is the required centripetal force?
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

Using inward as positive gives

$$
mg-N=m\omega^2r.
$$

Solving for the normal force gives

$$
N=mg-m\omega^2r.
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
    $N-mg=m\omega^2r$
- id: b
  content: |-
    $mg-N=m\omega^2r$
  correct: true
- id: c
  content: |-
    $N+mg=0$
- id: d
  content: |-
    $N=m\omega^2r$
```

---

<a id="substitute-angular-speed-into-the-force-balance"></a>
## Substitute Angular Speed into the Force Balance

**Example:** A Ferris wheel has radius $42\ \mathrm{m}$ and angular speed $0.16\ \mathrm{rad}/\mathrm{s}$. Find the normal force on a $68\ \mathrm{kg}$ rider at the top.

**Explanation**

Start with the top-position formula:

$$
N=mg-m\omega^2r.
$$

Summarize the known values before substituting:

- $m=68\ \mathrm{kg}$
- $g=9.8\ \mathrm{m}/\mathrm{s}^2$
- $\omega=0.16\ \mathrm{rad}/\mathrm{s}$
- $r=42\ \mathrm{m}$

Now substitute:

$$
\begin{aligned}
N&=(68)(9.8)-(68)(0.16)^2(42)\\
&=666.4-73.1136\\
&=593.2864\ \mathrm{N}.
\end{aligned}
$$

Rounded to the requested whole-newton answer, this is about

$$
N\approx 590\ \mathrm{N}.
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

<a id="avoid-the-bottom-position-sign-error"></a>
## Avoid the Bottom-Position Sign Error

**Example:** Why is the top-position normal force smaller than the rider's weight?

**Explanation**

At the top, gravity already points inward. Gravity supplies part of the required inward force, so the seat does not need to push as hard as it would if the wheel were not rotating.

That is why the formula is

$$
N=mg-m\omega^2r.
$$

At the bottom, inward is upward, so the force balance would be different:

$$
N-mg=m\omega^2r.
$$

The common mistake is to use the bottom equation at the top. That adds the centripetal term instead of subtracting it.

```quiz
type: radio
id: q-top-bottom-trap
shuffle: true
content: |-
  A student solves the top-of-wheel problem by using $N=mg+m\omega^2r$. What mistake did they make?
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

At the top of a Ferris wheel, inward is downward. Write the inward force balance as

$$
mg-N=m\omega^2r.
$$

Then solve:

$$
N=mg-m\omega^2r.
$$

Use this subtraction only because the rider is at the top. The main trap is using the bottom-position equation $N-mg=m\omega^2r$, which would make the normal force too large.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Comparing Normal Force and Weight at the Top of a Hill](../../2026-07-05-PQ-1/Lessons/Problem-3.md)

Study guide index: 18/30

---
<!-- lesson-nav:end -->
