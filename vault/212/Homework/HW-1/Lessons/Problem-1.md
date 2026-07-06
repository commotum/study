# Converting Revolutions per Minute to Radians per Second

## Table of Contents

- [Introduction](#introduction)
- [Choosing the Conversion Factors](#choosing-the-conversion-factors)
- [Converting With Unit Cancellation](#converting-with-unit-cancellation)
- [Avoiding the Minute-to-Second Trap](#avoiding-the-minute-to-second-trap)
- [Matching the Answer Choices](#matching-the-answer-choices)

## Prerequisites

- $1$ revolution equals $2\pi$ radians
- $1$ minute equals $60$ seconds
- Multiplying by a conversion factor that equals $1$
- Simplifying fractions with $\pi$

---

<a id="introduction"></a>
## Introduction

A wheel spins with an angular speed of $120$ revolutions per minute, and the question asks for radians per second.

The recognition cue is the unit change:

$$
\frac{\mathrm{rev}}{\mathrm{min}}
\quad\longrightarrow\quad
\frac{\mathrm{rad}}{\mathrm{s}}.
$$

Use one conversion factor for revolutions and one conversion factor for minutes:

$$
1\ \mathrm{rev}=2\pi\ \mathrm{rad},
\qquad
1\ \mathrm{min}=60\ \mathrm{s}.
$$

The conversion is

$$
120\ \frac{\mathrm{rev}}{\mathrm{min}}
\cdot
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}
=4\pi\ \frac{\mathrm{rad}}{\mathrm{s}}.
$$

---

<a id="choosing-the-conversion-factors"></a>
## Choosing the Conversion Factors

**Example:** Which product converts $15$ revolutions per minute into radians per second?

**Explanation**

Start with

$$
15\ \frac{\mathrm{rev}}{\mathrm{min}}.
$$

To cancel revolutions, put $\mathrm{rev}$ in the denominator:

$$
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}.
$$

To change minutes in the denominator into seconds in the denominator, put $\mathrm{min}$ in the numerator:

$$
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}.
$$

So the correct setup is

$$
15\ \frac{\mathrm{rev}}{\mathrm{min}}
\cdot
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}.
$$

```quiz
type: radio
id: q-1
content: |-
  Which product correctly sets up the conversion of $30$ revolutions per minute into radians per second?
options:
- id: a
  content: |-
    $30\ \dfrac{\mathrm{rev}}{\mathrm{min}}\cdot\dfrac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}\cdot\dfrac{1\ \mathrm{min}}{60\ \mathrm{s}}$
  correct: true
- id: b
  content: |-
    $30\ \dfrac{\mathrm{rev}}{\mathrm{min}}\cdot\dfrac{1\ \mathrm{rev}}{2\pi\ \mathrm{rad}}\cdot\dfrac{1\ \mathrm{min}}{60\ \mathrm{s}}$
- id: c
  content: |-
    $30\ \dfrac{\mathrm{rev}}{\mathrm{min}}\cdot\dfrac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}\cdot\dfrac{60\ \mathrm{s}}{1\ \mathrm{min}}$
- id: d
  content: |-
    $30\ \dfrac{\mathrm{rev}}{\mathrm{min}}\cdot\dfrac{1\ \mathrm{rad}}{2\pi\ \mathrm{rev}}\cdot\dfrac{60\ \mathrm{s}}{1\ \mathrm{min}}$
```

---

<a id="converting-with-unit-cancellation"></a>
## Converting With Unit Cancellation

**Example:** Convert $60$ revolutions per minute into radians per second.

**Explanation**

Write the full conversion:

$$
60\ \frac{\mathrm{rev}}{\mathrm{min}}
\cdot
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}.
$$

The $\mathrm{rev}$ units cancel, and the $\mathrm{min}$ units cancel:

$$
60\cdot\frac{2\pi}{60}\ \frac{\mathrm{rad}}{\mathrm{s}}.
$$

Simplify:

$$
60\cdot\frac{2\pi}{60}=2\pi.
$$

Therefore,

$$
60\ \frac{\mathrm{rev}}{\mathrm{min}}
=
2\pi\ \frac{\mathrm{rad}}{\mathrm{s}}.
$$

```quiz
type: radio
id: q-2
content: |-
  What is $90$ revolutions per minute in radians per second?
options:
- id: a
  content: |-
    $\pi/2$
- id: b
  content: |-
    $2\pi$
- id: c
  content: |-
    $3\pi$
  correct: true
- id: d
  content: |-
    $90\pi$
```

---

<a id="avoiding-the-minute-to-second-trap"></a>
## Avoiding the Minute-to-Second Trap

**Example:** Convert $180$ revolutions per minute into radians per second.

**Explanation**

First convert revolutions to radians:

$$
180\ \frac{\mathrm{rev}}{\mathrm{min}}
\cdot
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
=
360\pi\ \frac{\mathrm{rad}}{\mathrm{min}}.
$$

This is not finished because the unit is still radians per minute. Divide by $60$ to change minutes to seconds:

$$
360\pi\ \frac{\mathrm{rad}}{\mathrm{min}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}
=
6\pi\ \frac{\mathrm{rad}}{\mathrm{s}}.
$$

The common trap is stopping at $360\pi$. That number has not been converted to seconds.

```quiz
type: radio
id: q-3
content: |-
  A wheel spins at $150$ revolutions per minute. What is its angular speed in radians per second?
options:
- id: a
  content: |-
    $5\pi$
  correct: true
- id: b
  content: |-
    $150\pi$
- id: c
  content: |-
    $300\pi$
- id: d
  content: |-
    $\dfrac{5\pi}{2}$
```

---

<a id="matching-the-answer-choices"></a>
## Matching the Answer Choices

**Example:** A wheel spins with an angular speed of $120$ revolutions per minute. What is its angular speed in radians per second?

**Explanation**

Use the same two conversion factors:

$$
120\ \frac{\mathrm{rev}}{\mathrm{min}}
\cdot
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}.
$$

Cancel units:

$$
120\cdot\frac{2\pi}{60}\ \frac{\mathrm{rad}}{\mathrm{s}}.
$$

Simplify the number:

$$
120\cdot\frac{2\pi}{60}
=
2\cdot2\pi
=
4\pi.
$$

So the angular speed is

$$
\boxed{4\pi\ \mathrm{rad}/\mathrm{s}}.
$$

```quiz
type: radio
id: q-4
content: |-
  A wheel spins with an angular speed of $120$ revolutions per minute.
  
  What is its angular speed in radians per second?
options:
- id: a
  content: |-
    $\pi$
- id: b
  content: |-
    $2\pi$
- id: c
  content: |-
    $4\pi$
  correct: true
- id: d
  content: |-
    $6\pi$
```

---

## Summary

When an angular speed is given in revolutions per minute and the answer should be in radians per second, use

$$
1\ \mathrm{rev}=2\pi\ \mathrm{rad}
\qquad\text{and}\qquad
1\ \mathrm{min}=60\ \mathrm{s}.
$$

Set up the conversion so the old units cancel:

$$
\text{rpm}\cdot
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}.
$$

The main trap is converting revolutions to radians but forgetting to convert minutes to seconds. For $120$ revolutions per minute,

$$
120\cdot\frac{2\pi}{60}=4\pi,
$$

so the answer is $4\pi$ radians per second.
