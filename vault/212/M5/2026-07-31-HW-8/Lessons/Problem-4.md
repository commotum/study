# Finding String Tension from a Harmonic Frequency

<!--
lesson-id: 212-M5-044
topic-code: MTH212.M5.44
-->

## Table of Contents

- [Introduction](#introduction)
- [Turn the Harmonic Number into a Wavelength](#turn-the-harmonic-number-into-a-wavelength)
- [Use Frequency to Find Wave Speed](#use-frequency-to-find-wave-speed)
- [Convert Wave Speed into Tension](#convert-wave-speed-into-tension)
- [Chain the Relations Without Dropping the Square](#chain-the-relations-without-dropping-the-square)
- [Summary](#summary)

## Prerequisites

- Recognize that a string fixed at both ends has a node at each end.
- Use $v=f\lambda$ and $\mu=m/l$.
- Square a product or fraction.

---

<a id="introduction"></a>
## Introduction

When a uniform string has nodes at both ends and vibrates at its $n$th harmonic, the string's length contains $n$ half-wavelengths:

$$
l=n\frac{\lambda_n}{2}.
$$

This is the cue to begin with

$$
\lambda_n=\frac{2l}{n}.
$$

The harmonic frequency then gives the wave speed, and the wave speed gives the tension:

$$
v=f_n\lambda_n,
\qquad
\mu=\frac{m}{l},
\qquad
v=\sqrt{\frac{T}{\mu}}.
$$

The reusable route is

$$
n
\longrightarrow
\lambda_n
\longrightarrow
v
\longrightarrow
T.
$$

Combining the four relations gives the rule used throughout this lesson:

$$
\boxed{T=\frac{4}{n^2}mlf_n^2}.
$$

This rule applies here because the string is uniform and both ends can be treated as nodes.

---

<a id="turn-the-harmonic-number-into-a-wavelength"></a>
## Turn the Harmonic Number into a Wavelength

**Example:** A string of length $1.20\ \mathrm{m}$ has nodes at both ends and vibrates at its fourth harmonic. Find the wavelength.

**Explanation**

For the fourth harmonic, $n=4$. The string contains four half-wavelengths:

$$
l=4\frac{\lambda_4}{2}.
$$

Solve for the wavelength:

$$
\lambda_4=\frac{2l}{4}
=\frac{2(1.20\ \mathrm{m})}{4}
=0.60\ \mathrm{m}.
$$

```quiz
type: radio
id: p4-harmonic-wavelength-q1
content: |-
  A string of length $l$ has nodes at both ends and vibrates at its fifth harmonic. What is its wavelength?
options:
- id: p4-harmonic-wavelength-q1-a
  content: |-
    $\dfrac{l}{5}$
- id: p4-harmonic-wavelength-q1-b
  content: |-
    $\dfrac{2l}{5}$
  correct: true
- id: p4-harmonic-wavelength-q1-c
  content: |-
    $\dfrac{5l}{2}$
- id: p4-harmonic-wavelength-q1-d
  content: |-
    $2l$
- id: p4-harmonic-wavelength-q1-e
  content: |-
    $5l$
```

---

<a id="use-frequency-to-find-wave-speed"></a>
## Use Frequency to Find Wave Speed

**Example:** A $0.90\ \mathrm{m}$ string vibrates at its third harmonic with frequency $120\ \mathrm{Hz}$. Find the wave speed.

**Explanation**

First find the third-harmonic wavelength:

$$
\lambda_3=\frac{2l}{3}
=\frac{2(0.90\ \mathrm{m})}{3}
=0.60\ \mathrm{m}.
$$

Then use $v=f\lambda$:

$$
v=f_3\lambda_3
=(120\ \mathrm{Hz})(0.60\ \mathrm{m})
=72\ \mathrm{m/s}.
$$

```quiz
type: radio
id: p4-wave-speed-q1
content: |-
  A $1.20\ \mathrm{m}$ string has nodes at both ends and vibrates at its fourth harmonic with frequency $150\ \mathrm{Hz}$. What is the wave speed?
options:
- id: p4-wave-speed-q1-a
  content: |-
    $45\ \mathrm{m/s}$
- id: p4-wave-speed-q1-b
  content: |-
    $90\ \mathrm{m/s}$
  correct: true
- id: p4-wave-speed-q1-c
  content: |-
    $180\ \mathrm{m/s}$
- id: p4-wave-speed-q1-d
  content: |-
    $360\ \mathrm{m/s}$
- id: p4-wave-speed-q1-e
  content: |-
    $720\ \mathrm{m/s}$
```

---

<a id="convert-wave-speed-into-tension"></a>
## Convert Wave Speed into Tension

**Example:** A uniform string has mass $0.12\ \mathrm{kg}$, length $0.80\ \mathrm{m}$, and wave speed $40\ \mathrm{m/s}$. Find its tension.

**Explanation**

The string's linear mass density is its mass per unit length:

$$
\mu=\frac{m}{l}
=\frac{0.12\ \mathrm{kg}}{0.80\ \mathrm{m}}
=0.15\ \mathrm{kg/m}.
$$

Start with the string-speed relation and solve for $T$:

$$
\begin{aligned}
v&=\sqrt{\frac{T}{\mu}} \\
v^2&=\frac{T}{\mu} \\
\mu v^2&=T.
\end{aligned}
$$

Now substitute:

$$
T=(0.15\ \mathrm{kg/m})(40\ \mathrm{m/s})^2
=240\ \mathrm{N}.
$$

```quiz
type: radio
id: p4-speed-to-tension-q1
content: |-
  A uniform string has mass $0.18\ \mathrm{kg}$, length $0.90\ \mathrm{m}$, and wave speed $30\ \mathrm{m/s}$. What is its tension?
options:
- id: p4-speed-to-tension-q1-a
  content: |-
    $6\ \mathrm{N}$
- id: p4-speed-to-tension-q1-b
  content: |-
    $162\ \mathrm{N}$
- id: p4-speed-to-tension-q1-c
  content: |-
    $180\ \mathrm{N}$
  correct: true
- id: p4-speed-to-tension-q1-d
  content: |-
    $900\ \mathrm{N}$
- id: p4-speed-to-tension-q1-e
  content: |-
    $4500\ \mathrm{N}$
```

---

<a id="chain-the-relations-without-dropping-the-square"></a>
## Chain the Relations Without Dropping the Square

**Example:** Derive the tension of a uniform string of mass $m$ and length $l$ when it vibrates at frequency $f_n$ in its $n$th harmonic. Both ends are nodes.

**Explanation**

Begin with the harmonic wavelength and use it in $v=f\lambda$:

$$
\lambda_n=\frac{2l}{n},
\qquad
v=f_n\lambda_n
=\frac{2lf_n}{n}.
$$

The tension is $T=\mu v^2$, and $\mu=m/l$. Substitute both expressions:

$$
\begin{aligned}
T
&=\mu v^2 \\
&=\frac{m}{l}\left(\frac{2lf_n}{n}\right)^2 \\
&=\frac{m}{l}\frac{4l^2f_n^2}{n^2} \\
&=\boxed{\frac{4}{n^2}mlf_n^2}.
\end{aligned}
$$

The square applies to the entire wave-speed expression. In particular,

$$
\left(\frac{2}{n}\right)^2=\frac{4}{n^2},
$$

not $\frac{2}{n}$.

```quiz
type: radio
id: p4-general-tension-q1
content: |-
  A uniform string of mass $m$ and length $l$ has nodes at both ends. It vibrates at frequency $f_4$ in its fourth harmonic. Which expression gives its tension?
options:
- id: p4-general-tension-q1-a
  content: |-
    $\dfrac{1}{16}mlf_4^2$
- id: p4-general-tension-q1-b
  content: |-
    $\dfrac{1}{4}mlf_4^2$
  correct: true
- id: p4-general-tension-q1-c
  content: |-
    $\dfrac{1}{2}mlf_4^2$
- id: p4-general-tension-q1-d
  content: |-
    $4mlf_4^2$
- id: p4-general-tension-q1-e
  content: |-
    $16mlf_4^2$
```

As a quick units check,

$$
[mlf_n^2]
=(\mathrm{kg})(\mathrm{m})(\mathrm{s}^{-2})
=\mathrm{N}.
$$

The coefficient $4/n^2$ is unitless, so the combined expression has the units of tension.

```quiz
type: radio
id: p4-homework-q1
shuffle: true
content: |-
  A uniform string of mass $m$ and length $l$ is clamped at one end and attached to a wave generator at the other.

  When the wave generator is set to frequency $f_3$, the string vibrates at its third harmonic.

  What is the magnitude of the string's tension?

  Assume that the wave generator can be approximated as a node.
options:
- id: p4-homework-q1-a
  content: |-
    $\dfrac{1}{6}mlf_3^2$
- id: p4-homework-q1-b
  content: |-
    $\dfrac{4}{9}mlf_3^2$
  correct: true
- id: p4-homework-q1-c
  content: |-
    $\dfrac{3}{8}mlf_3^2$
- id: p4-homework-q1-d
  content: |-
    $\dfrac{1}{2}mlf_3^2$
```

---

<a id="summary"></a>
## Summary

**Recognition cue:** A uniform string has nodes at both ends, an $n$th-harmonic frequency is given, and the tension is requested.

**Rule chain:**

$$
\lambda_n=\frac{2l}{n},
\qquad
v=f_n\lambda_n,
\qquad
\mu=\frac{m}{l},
\qquad
T=\mu v^2.
$$

**Combined result:**

$$
\boxed{T=\frac{4}{n^2}mlf_n^2}.
$$

**Procedure:**

1. Use the harmonic number to find $\lambda_n=2l/n$.
2. Find the wave speed with $v=f_n\lambda_n$.
3. Find the linear density with $\mu=m/l$.
4. Compute $T=\mu v^2$.

**Main trap:** The harmonic factor is inside the wave speed, so it must be squared when computing tension. For the third harmonic, $(2/3)^2=4/9$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
