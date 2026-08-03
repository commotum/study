# Finding Centripetal Force From Radius and Period

<!--
lesson-id: 212-M1-059
topic-code: MTH212.M1.59
-->

## Table of Contents

- [Introduction](#introduction)
- [Turn Period Into Speed](#turn-period-into-speed)
- [Substitute Speed Into Centripetal Force](#substitute-speed-into-centripetal-force)
- [Match the Formula to the Answer Choices](#match-the-formula-to-the-answer-choices)
- [Check How the Period Affects the Force](#check-how-the-period-affects-the-force)
- [Summary](#summary)

## Prerequisites

- Circumference of a circle: $2\pi r$
- Speed is distance divided by time
- Centripetal force magnitude: $F_c=\dfrac{mv^2}{r}$
- Period $T$ means the time for one complete revolution

---

<a id="introduction"></a>
## Introduction

In a conical-pendulum problem, the bob moves in a horizontal circle while the string stays tilted.

![](<../Source/Images/conical-pendulum-diagram.png>)

The cue in this problem is that the question asks for centripetal force, but it gives the period $T$ instead of the speed $v$.

Use one full revolution to build the speed:

$$
v=\dfrac{2\pi r}{T}.
$$

Then substitute that speed into

$$
F_c=\dfrac{mv^2}{r}.
$$

The radius in the force formula is the circular path radius $r$. The string length $L$ and angle $\theta$ can help find $r$ in other questions, but this answer is written directly in terms of $r$.

---

<a id="turn-period-into-speed"></a>
## Turn Period Into Speed

**Example:** An object moves at constant speed in a circle of radius $R$. Its period is $P$. What is its speed?

**Explanation**

In one full revolution, the object travels one circumference:

$$
\text{distance in one revolution}=2\pi R.
$$

The time for one revolution is the period $P$. Since speed is distance divided by time,

$$
v=\dfrac{2\pi R}{P}.
$$

```quiz
type: radio
id: p3-q1
shuffle: true
content: |-
  A bob moves in a circle of radius $r$ with period $T$. Which expression gives its speed?
options:
- id: p3-q1-a
  content: |-
    $\dfrac{2\pi r}{T}$
  correct: true
- id: p3-q1-b
  content: |-
    $\dfrac{2\pi T}{r}$
- id: p3-q1-c
  content: |-
    $\dfrac{r}{T}$
- id: p3-q1-d
  content: |-
    $\dfrac{4\pi^2r}{T^2}$
- id: p3-q1-e
  content: |-
    $2\pi rT$
```

---

<a id="substitute-speed-into-centripetal-force"></a>
## Substitute Speed Into Centripetal Force

**Example:** A mass $m$ moves at constant speed in a circle of radius $r$ with period $T$. Find the magnitude of its centripetal force.

**Explanation**

Start with the centripetal force formula:

$$
F_c=\dfrac{mv^2}{r}.
$$

From the period,

$$
v=\dfrac{2\pi r}{T}.
$$

Substitute that whole expression for $v$:

$$
F_c=\dfrac{m}{r}\left(\dfrac{2\pi r}{T}\right)^2.
$$

Now square the numerator and denominator:

$$
F_c=\dfrac{m}{r}\cdot \dfrac{4\pi^2r^2}{T^2}.
$$

One factor of $r$ cancels:

$$
F_c=\dfrac{4\pi^2mr}{T^2}.
$$

```quiz
type: radio
id: p3-q2
shuffle: true
content: |-
  A mass $M$ moves in a circle of radius $R$ with period $P$. Which expression gives the centripetal force magnitude?
options:
- id: p3-q2-a
  content: |-
    $\dfrac{4\pi^2MR}{P^2}$
  correct: true
- id: p3-q2-b
  content: |-
    $\dfrac{2\pi MR}{P^2}$
- id: p3-q2-c
  content: |-
    $\dfrac{4\pi^2MR^2}{P^2}$
- id: p3-q2-d
  content: |-
    $\dfrac{4\pi^2M}{RP^2}$
- id: p3-q2-e
  content: |-
    $\dfrac{MR}{P^2}$
```

---

<a id="match-the-formula-to-the-answer-choices"></a>
## Match the Formula to the Answer Choices

**Example:** A bob of mass $m$ attached to a light string traverses a circular trajectory. The circular path has radius $r$, and the period of the circular motion is $T$. Which answer matches the centripetal force magnitude?

**Explanation**

The period gives the speed:

$$
v=\dfrac{2\pi r}{T}.
$$

Substituting into $F_c=\dfrac{mv^2}{r}$ gives

$$
F_c
=\dfrac{m}{r}\left(\dfrac{2\pi r}{T}\right)^2
=\dfrac{4\pi^2mr}{T^2}.
$$

So the matching answer is the one with $4\pi^2$, one factor of $r$, and $T^2$ in the denominator.

```quiz
type: radio
id: p3-q3
shuffle: true
content: |-
  The figures below show a bob of mass $m$ attached to a light string of length $L$ which traverses a circular trajectory when viewed from above/below.

  The string makes an angle $\theta$ with the horizontal and the period of the circular motion is $T$ (constant).

  What is the magnitude of the object's centripetal force?

  ![](<../Source/Images/conical-pendulum-diagram.png>)
options:
- id: p3-q3-a
  content: |-
    $\dfrac{4\pi^2mr}{T^2}$
  correct: true
- id: p3-q3-b
  content: |-
    $\dfrac{2\pi mr}{T^2}$
- id: p3-q3-c
  content: |-
    $\dfrac{mr}{T^2}$
- id: p3-q3-d
  content: |-
    $\dfrac{mr}{2\pi T^2}$
- id: p3-q3-e
  content: |-
    $\dfrac{mr}{4\pi T^2}$
```

---

<a id="check-how-the-period-affects-the-force"></a>
## Check How the Period Affects the Force

**Example:** Two bobs have the same mass and circular-path radius. Bob A has period $T$, and Bob B has period $2T$. How does Bob B's centripetal force compare with Bob A's?

**Explanation**

The force formula from period is

$$
F_c=\dfrac{4\pi^2mr}{T^2}.
$$

If the period doubles, then $T^2$ becomes $(2T)^2=4T^2$. The force becomes one fourth as large:

$$
F_{c,B}=\dfrac{4\pi^2mr}{(2T)^2}
=\dfrac{1}{4}\cdot \dfrac{4\pi^2mr}{T^2}.
$$

This check confirms that $T$ must be squared in the denominator. A longer period means a lower speed, and the force depends on speed squared.

```quiz
type: radio
id: p3-q4
shuffle: true
content: |-
  Two objects have the same mass and circular-path radius. If the second object's period is $3$ times as large as the first object's period, what happens to the centripetal force magnitude?
options:
- id: p3-q4-a
  content: |-
    It becomes $9$ times as large.
- id: p3-q4-b
  content: |-
    It becomes $3$ times as large.
- id: p3-q4-c
  content: |-
    It stays the same because the radius did not change.
- id: p3-q4-d
  content: |-
    It becomes $\dfrac{1}{3}$ as large.
- id: p3-q4-e
  content: |-
    It becomes $\dfrac{1}{9}$ as large.
  correct: true
```

---

## Summary

When centripetal force is requested but period is given, first convert one revolution into speed:

$$
v=\dfrac{2\pi r}{T}.
$$

Then substitute into the force formula:

$$
F_c=\dfrac{mv^2}{r}
=\dfrac{m}{r}\left(\dfrac{2\pi r}{T}\right)^2
=\dfrac{4\pi^2mr}{T^2}.
$$

The main traps are forgetting to square $2\pi$, forgetting to square $T$, or leaving $r^2$ after one factor of $r$ should cancel.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
