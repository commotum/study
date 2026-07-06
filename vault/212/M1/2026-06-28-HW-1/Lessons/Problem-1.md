# Converting Revolutions per Minute to Radians per Second

## Table of Contents

- [Introduction](#introduction)
- [Choosing the Conversion Factors](#choosing-the-conversion-factors)
- [Checking the Remaining Units](#checking-the-remaining-units)
- [Simplifying the Number](#simplifying-the-number)
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

The cue is the unit change:

$$
\frac{\mathrm{rev}}{\mathrm{min}}
\quad\longrightarrow\quad
\frac{\mathrm{rad}}{\mathrm{s}}.
$$

Convert the numerator unit and the denominator unit separately:

$$
1\ \mathrm{rev}=2\pi\ \mathrm{rad},
\qquad
1\ \mathrm{min}=60\ \mathrm{s}.
$$

For any angular speed $R$ in revolutions per minute,

$$
R\ \frac{\mathrm{rev}}{\mathrm{min}}
\cdot
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}
=
\frac{R\pi}{30}\ \frac{\mathrm{rad}}{\mathrm{s}}.
$$

The important part is not the shortcut. The important part is arranging the conversion factors so the old units cancel.

---

<a id="choosing-the-conversion-factors"></a>
## Choosing the Conversion Factors

**Example:** Which product converts $15$ revolutions per minute into radians per second?

**Explanation**

Start with

$$
15\ \frac{\mathrm{rev}}{\mathrm{min}}.
$$

The unit $\mathrm{rev}$ is in the numerator, so put $\mathrm{rev}$ in the denominator of the conversion factor:

$$
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}.
$$

The unit $\mathrm{min}$ is in the denominator, so put $\mathrm{min}$ in the numerator of the conversion factor:

$$
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}.
$$

The setup is

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
shuffle: true
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

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  Which conversion factor should be used to change the denominator from minutes to seconds in a rate measured in $\mathrm{rev}/\mathrm{min}$?
options:
- id: a
  content: |-
    $\dfrac{60\ \mathrm{s}}{1\ \mathrm{min}}$
- id: b
  content: |-
    $\dfrac{1\ \mathrm{min}}{60\ \mathrm{s}}$
  correct: true
- id: c
  content: |-
    $\dfrac{60\ \mathrm{min}}{1\ \mathrm{s}}$
- id: d
  content: |-
    $\dfrac{1\ \mathrm{s}}{60\ \mathrm{min}}$
```

---

<a id="checking-the-remaining-units"></a>
## Checking the Remaining Units

**Example:** After setting up

$$
45\ \frac{\mathrm{rev}}{\mathrm{min}}
\cdot
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}},
$$

what units remain?

**Explanation**

The $\mathrm{rev}$ unit appears once in the numerator and once in the denominator, so those cancel. The same is true for $\mathrm{min}$:

$$
\frac{\mathrm{rev}}{\mathrm{min}}
\cdot
\frac{\mathrm{rad}}{\mathrm{rev}}
\cdot
\frac{\mathrm{min}}{\mathrm{s}}
=
\frac{\mathrm{rad}}{\mathrm{s}}.
$$

So the setup has the correct final units.

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  After simplifying the units in
  $75\ \dfrac{\mathrm{rev}}{\mathrm{min}}\cdot\dfrac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}\cdot\dfrac{1\ \mathrm{min}}{60\ \mathrm{s}},$
  which units remain?
options:
- id: a
  content: |-
    $\mathrm{rad}/\mathrm{s}$
  correct: true
- id: b
  content: |-
    $\mathrm{rad}/\mathrm{min}$
- id: c
  content: |-
    $\mathrm{rev}/\mathrm{s}$
- id: d
  content: |-
    $\mathrm{rad}\cdot\mathrm{s}/\mathrm{min}^2$
```

---

<a id="simplifying-the-number"></a>
## Simplifying the Number

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

After the units cancel, simplify the number:

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
id: q-4
shuffle: true
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

```quiz
type: radio
id: q-5
shuffle: true
content: |-
  What is $45$ revolutions per minute in radians per second?
options:
- id: a
  content: |-
    $\dfrac{\pi}{2}$
- id: b
  content: |-
    $\dfrac{3\pi}{2}$
  correct: true
- id: c
  content: |-
    $3\pi$
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

This is not finished because the unit is still radians per minute. Convert the denominator from minutes to seconds:

$$
360\pi\ \frac{\mathrm{rad}}{\mathrm{min}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}
=
6\pi\ \frac{\mathrm{rad}}{\mathrm{s}}.
$$

The common trap is stopping at $360\pi$. That number has the wrong time unit.

```quiz
type: radio
id: q-6
shuffle: true
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

Simplify:

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
id: q-7
shuffle: true
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

When an angular speed is given in revolutions per minute and the answer should be in radians per second, convert both parts of the rate:

$$
\mathrm{rev}\to\mathrm{rad}
\qquad\text{and}\qquad
\mathrm{min}\to\mathrm{s}.
$$

Use

$$
1\ \mathrm{rev}=2\pi\ \mathrm{rad},
\qquad
1\ \mathrm{min}=60\ \mathrm{s},
$$

and arrange the factors so the old units cancel:

$$
R\ \frac{\mathrm{rev}}{\mathrm{min}}
\cdot
\frac{2\pi\ \mathrm{rad}}{1\ \mathrm{rev}}
\cdot
\frac{1\ \mathrm{min}}{60\ \mathrm{s}}
=
\frac{R\pi}{30}\ \frac{\mathrm{rad}}{\mathrm{s}}.
$$

The main trap is converting revolutions to radians but leaving the answer in radians per minute. For $120$ revolutions per minute,

$$
120\cdot\frac{2\pi}{60}=4\pi,
$$

so the answer is $4\pi$ radians per second.
