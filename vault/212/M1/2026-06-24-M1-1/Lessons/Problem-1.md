# Convert Revolutions Per Second to Angular Frequency

<!--
lesson-id: 212-M1-033
topic-code: MTH212.M1.33
-->

## Table of Contents

- [Introduction](#introduction)
- [One Revolution Is \(2\pi\) Radians](#one-revolution-is-2pi-radians)
- [Convert A Rotation Rate](#convert-a-rotation-rate)
- [Round The Angular Frequency](#round-the-angular-frequency)
- [Avoid Leaving Revolutions In The Answer](#avoid-leaving-revolutions-in-the-answer)
- [Summary](#summary)

## Prerequisites

- Know that one full revolution is \(2\pi\) radians.
- Know how to multiply by a unit conversion factor.
- Know how to round a number to a given number of significant figures.

---

<a id="introduction"></a>
## Introduction

Angular frequency \(\omega\) is a rate:

$$
\omega=\frac{\text{angle swept out}}{\text{time}}.
$$

When a problem gives a spinning rate in revolutions per second but asks for \(\omega\) in radians per second, convert the angle unit from revolutions to radians.

The cue is the mismatch between the given unit and the requested unit:

$$
\frac{\text{rev}}{\text{s}} \quad \longrightarrow \quad \frac{\text{rad}}{\text{s}}
$$

Use the conversion

$$
1\text{ rev}=2\pi\text{ rad}
$$

The given rate has \(\text{rev}\) in the numerator, so put \(\text{rev}\) in the denominator of the conversion factor:

$$
\omega=\left(\text{revolutions per second}\right)\left(\frac{2\pi\text{ rad}}{1\text{ rev}}\right).
$$

---

<a id="one-revolution-is-2pi-radians"></a>
## One Revolution Is \(2\pi\) Radians

**Example:** Convert \(4\) revolutions to radians.

**Explanation**

One revolution is one full turn around a circle, and one full turn has angle \(2\pi\) radians.

$$
4\text{ rev}\cdot \frac{2\pi\text{ rad}}{1\text{ rev}}=8\pi\text{ rad}
$$

The revolution units cancel, leaving radians.

```quiz
type: radio
id: q-1
shuffle: true
content: |-
  Convert \(6\) revolutions to radians.
options:
- id: q1-a
  content: |-
    \(6\pi\text{ rad}\)
- id: q1-b
  content: |-
    \(12\pi\text{ rad}\)
  correct: true
- id: q1-c
  content: |-
    \(3\pi\text{ rad}\)
- id: q1-d
  content: |-
    \(6\text{ rad}\)
```

---

<a id="convert-a-rotation-rate"></a>
## Convert A Rotation Rate

**Example:** A wheel spins at \(5\) revolutions per second. Find its angular frequency in radians per second.

**Explanation**

Keep the "per second" part and convert only the revolution part.

$$
\omega=5\frac{\text{rev}}{\text{s}}\cdot \frac{2\pi\text{ rad}}{1\text{ rev}}
$$

Cancel \(\text{rev}\):

$$
\omega=10\pi\frac{\text{rad}}{\text{s}}
$$

So a rate of \(5\) revolutions per second is an angular frequency of \(10\pi\text{ rad/s}\).

```quiz
type: radio
id: q-2
shuffle: true
content: |-
  A disk spins at \(9\) revolutions per second. What is its angular frequency?
options:
- id: q2-a
  content: |-
    \(9\pi\text{ rad/s}\)
- id: q2-b
  content: |-
    \(18\pi\text{ rad/s}\)
  correct: true
- id: q2-c
  content: |-
    \(\frac{9}{2\pi}\text{ rad/s}\)
- id: q2-d
  content: |-
    \(9\text{ rad/s}\)
```

---

<a id="round-the-angular-frequency"></a>
## Round The Angular Frequency

**Example:** A wheel is spinning at \(14\) revolutions per second. What is its angular frequency \(\omega\) in radians per second? Give the answer to \(2\) significant figures.

**Explanation**

First convert exactly:

$$
\omega=14\frac{\text{rev}}{\text{s}}\cdot \frac{2\pi\text{ rad}}{1\text{ rev}}
=28\pi\frac{\text{rad}}{\text{s}}
$$

Then approximate. Keep \(2\pi\) until this step so the final rounding uses the full conversion factor.

$$
28\pi\approx 87.96
$$

To \(2\) significant figures,

$$
\omega\approx 88\text{ rad/s}.
$$

```quiz
type: radio
id: q-3
shuffle: true
content: |-
  A fan spins at \(11\) revolutions per second. What is its angular frequency in radians per second, rounded to \(2\) significant figures?
options:
- id: q3-a
  content: |-
    \(35\text{ rad/s}\)
- id: q3-b
  content: |-
    \(69\text{ rad/s}\)
  correct: true
- id: q3-c
  content: |-
    \(11\text{ rad/s}\)
- id: q3-d
  content: |-
    \(66\text{ rad/s}\)
```

---

<a id="avoid-leaving-revolutions-in-the-answer"></a>
## Avoid Leaving Revolutions In The Answer

**Example:** A turntable spins at \(7\) revolutions per second. Which setup correctly finds \(\omega\) in radians per second?

**Explanation**

The number \(7\) tells how many full turns happen each second. It is not yet in radians per second. Multiply by \(2\pi\text{ rad/rev}\), not by \(\pi\), and do not divide by \(2\pi\).

$$
\omega=7\frac{\text{rev}}{\text{s}}\cdot \frac{2\pi\text{ rad}}{1\text{ rev}}
=14\pi\text{ rad/s}
$$

```quiz
type: radio
id: q-4
shuffle: true
content: |-
  A motor spins at \(3\) revolutions per second. Which value is its angular frequency?
options:
- id: q4-a
  content: |-
    \(3\text{ rad/s}\)
- id: q4-b
  content: |-
    \(3\pi\text{ rad/s}\)
- id: q4-c
  content: |-
    \(6\pi\text{ rad/s}\)
  correct: true
- id: q4-d
  content: |-
    \(\frac{3}{2\pi}\text{ rad/s}\)
```

---

<a id="summary"></a>
## Summary

When a spinning rate is given in revolutions per second and the answer must be in radians per second, use

$$
\omega=\left(\text{rev/s}\right)(2\pi).
$$

The seconds stay in the denominator, and each revolution becomes \(2\pi\) radians. A quick checklist is:

1. Start with the given number in \(\text{rev/s}\).
2. Multiply by \(\frac{2\pi\text{ rad}}{1\text{ rev}}\).
3. Cancel \(\text{rev}\), keep \(\text{rad/s}\), and round only if the problem asks for a rounded answer.

The main trap is to report the revolutions-per-second number as if it were already in radians per second.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
