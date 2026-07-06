# Finding the Time for One Revolution While Speeding Up

## Table of Contents

- [Introduction](#introduction)
- [Converting a Revolution to Distance](#converting-a-revolution-to-distance)
- [Writing the Distance Equation](#writing-the-distance-equation)
- [Solving the Quadratic for Time](#solving-the-quadratic-for-time)
- [Using Symbols for the Whole Lap](#using-symbols-for-the-whole-lap)
- [Matching the Answer Choices](#matching-the-answer-choices)

## Prerequisites

- One revolution around a circle of radius $r$ covers distance $2\pi r$
- If speed increases at constant rate $a$, then distance traveled after time $t$ is $vt+\dfrac12at^2$
- The quadratic formula
- Time must be positive

---

<a id="introduction"></a>
## Introduction

An object travels along a circular trajectory of radius $r$. At one instant, its speed is $v$ and its speed is increasing at a constant rate $a$.

The recognition cue is that the question asks for the time for one full revolution while the speed is changing. A full revolution gives a distance target:

$$
2\pi r.
$$

Since the speed starts at $v$ and increases at constant rate $a$, the distance traveled after time $t$ is

$$
vt+\frac12at^2.
$$

Set these equal and solve for the positive time:

$$
vt+\frac12at^2=2\pi r.
$$

---

<a id="converting-a-revolution-to-distance"></a>
## Converting a Revolution to Distance

**Example:** An object moves around a circle of radius $6$. How far does it travel in one revolution?

**Explanation**

One revolution means one full circumference. For a circle of radius $r$, the circumference is

$$
2\pi r.
$$

With $r=6$, the distance is

$$
2\pi(6)=12\pi.
$$

So one revolution covers distance $12\pi$.

```quiz
type: radio
id: q-1
content: |-
  An object moves once around a circle of radius $R$. What distance does it travel?
options:
- id: a
  content: |-
    $\pi R$
- id: b
  content: |-
    $2\pi R$
  correct: true
- id: c
  content: |-
    $\dfrac{R}{2\pi}$
- id: d
  content: |-
    $\dfrac{2\pi}{R}$
```

---

<a id="writing-the-distance-equation"></a>
## Writing the Distance Equation

**Example:** An object moves around a circle of radius $4$. Its current speed is $5$, and its speed increases at constant rate $2$. What equation gives the time $t$ for one revolution?

**Explanation**

The distance for one revolution is

$$
2\pi(4)=8\pi.
$$

The distance traveled after time $t$ is

$$
vt+\frac12at^2.
$$

Here $v=5$ and $a=2$, so

$$
vt+\frac12at^2=5t+\frac12(2)t^2=5t+t^2.
$$

Set distance traveled equal to the lap distance:

$$
5t+t^2=8\pi.
$$

```quiz
type: radio
id: q-2
content: |-
  An object moves around a circle of radius $7$. Its current speed is $3$, and its speed increases at constant rate $4$. Which equation gives the time $t$ for one revolution?
options:
- id: a
  content: |-
    $3t+4t^2=14\pi$
- id: b
  content: |-
    $3t+2t^2=14\pi$
  correct: true
- id: c
  content: |-
    $3t+2t^2=7\pi$
- id: d
  content: |-
    $3+4t=14\pi$
- id: e
  content: |-
    $3t+4t^2=7\pi$
```

---

<a id="solving-the-quadratic-for-time"></a>
## Solving the Quadratic for Time

**Example:** An object starts with speed $5$ and speeds up at constant rate $2$. How long does it take to travel distance $30$?

**Explanation**

Use the distance equation:

$$
30=5t+\frac12(2)t^2.
$$

Simplify:

$$
30=5t+t^2.
$$

Move everything to one side:

$$
t^2+5t-30=0.
$$

Apply the quadratic formula:

$$
t=\frac{-5\pm\sqrt{5^2-4(1)(-30)}}{2(1)}
=\frac{-5\pm\sqrt{145}}{2}.
$$

Only the positive root can be a time, so

$$
t=\frac{-5+\sqrt{145}}{2}.
$$

```quiz
type: radio
id: q-3
content: |-
  An object starts with speed $6$ and speeds up at constant rate $4$. How long does it take to travel distance $20$?
options:
- id: a
  content: |-
    $2$
  correct: true
- id: b
  content: |-
    $5$
- id: c
  content: |-
    $\dfrac{-6-\sqrt{196}}{4}$
- id: d
  content: |-
    $\dfrac{6+\sqrt{196}}{4}$
- id: e
  content: |-
    $\dfrac{20}{6}$
```

---

<a id="using-symbols-for-the-whole-lap"></a>
## Using Symbols for the Whole Lap

**Example:** An object has current speed $v$ and speeds up at constant rate $a$. How long does it take to travel distance $L$?

**Explanation**

Start from

$$
L=vt+\frac12at^2.
$$

Move everything to one side:

$$
\frac12at^2+vt-L=0.
$$

Use the quadratic formula with

$$
A=\frac12a,\qquad B=v,\qquad C=-L.
$$

Then

$$
t
=
\frac{-v\pm\sqrt{v^2-4\left(\frac12a\right)(-L)}}{2\left(\frac12a\right)}
=
\frac{-v\pm\sqrt{v^2+2aL}}{a}.
$$

Since $v$, $a$, and $L$ are positive, the root with $-\sqrt{v^2+2aL}$ is negative. The time is

$$
t=\frac{-v+\sqrt{v^2+2aL}}{a}.
$$

```quiz
type: radio
id: q-4
content: |-
  An object has current speed $v$ and speeds up at constant rate $a$. How long does it take to travel distance $L$?
options:
- id: a
  content: |-
    $\dfrac{-v-\sqrt{v^2+2aL}}{a}$
- id: b
  content: |-
    $\dfrac{-v+\sqrt{v^2+2aL}}{a}$
  correct: true
- id: c
  content: |-
    $\dfrac{v+\sqrt{v^2+2aL}}{a}$
- id: d
  content: |-
    $\dfrac{-v+\sqrt{v^2+aL}}{a}$
- id: e
  content: |-
    $\dfrac{L}{v+a}$
```

---

<a id="matching-the-answer-choices"></a>
## Matching the Answer Choices

**Example:** An object travels along a circular trajectory of radius $r$. At one instant, the particle's speed is $v$ and increasing at a constant rate $a$. Assuming the object speeds up at this same rate, how much time will it take to complete one revolution?

**Explanation**

For one revolution, the distance is

$$
L=2\pi r.
$$

Substitute this into the symbolic distance result:

$$
t=\frac{-v+\sqrt{v^2+2aL}}{a}.
$$

Since $L=2\pi r$,

$$
t
=
\frac{-v+\sqrt{v^2+2a(2\pi r)}}{a}
=
\frac{-v+\sqrt{v^2+4\pi ar}}{a}.
$$

The main trap is choosing the root with $-\sqrt{v^2+4\pi ar}$. That root has a negative numerator, so it gives a negative time.

```quiz
type: radio
id: q-5
content: |-
  An object travels along a circular trajectory of radius $r$. At one instant, the particle's speed is $v$ and increasing at a constant rate $a$.
  
  Assuming the object speeds up at this same rate, how much time will it take to complete one revolution?
  
  Hint: $r$, $v$, and $a$ are all positive.
options:
- id: a
  content: |-
    $\dfrac{-v-\sqrt{v^2+4\pi ar}}{a}$
- id: b
  content: |-
    $\dfrac{-v+\sqrt{v^2+4\pi ar}}{a}$
  correct: true
- id: c
  content: |-
    $\dfrac{v}{a}$
- id: d
  content: |-
    $\dfrac{v+\sqrt{v^2+4\pi ar}}{a}$
- id: e
  content: |-
    $\dfrac{v+\sqrt{v^2+4\pi ar}}{ar}$
```

---

## Summary

For one revolution around a circle of radius $r$, use the distance $2\pi r$. If the current speed is $v$ and speed increases at constant rate $a$, then the distance traveled after time $t$ is

$$
vt+\frac12at^2.
$$

Set the distance equal to one lap:

$$
vt+\frac12at^2=2\pi r.
$$

Solving this quadratic gives

$$
t=\frac{-v\pm\sqrt{v^2+4\pi ar}}{a}.
$$

Choose the plus sign before the square root:

$$
\boxed{t=\frac{-v+\sqrt{v^2+4\pi ar}}{a}}.
$$

The other root is negative, so it cannot be the elapsed time.
