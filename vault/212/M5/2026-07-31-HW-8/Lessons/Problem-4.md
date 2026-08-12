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
- Use $v_{\mathrm{wave}}=f\lambda$ and $\mu=m_{\mathrm{string}}/L$.
- Square a product or fraction.

---

<a id="introduction"></a>
## Introduction

When a uniform string has nodes at both ends and vibrates at its $m$th harmonic, the string's length contains $m$ half-wavelengths:

$$
L=m\frac{\lambda_m}{2}.
$$

This is the cue to begin with

$$
\lambda_m=\frac{2L}{m}.
$$

The harmonic frequency then gives the wave speed, and the wave speed gives the tension:

$$
v_{\mathrm{wave}}=f_m\lambda_m,
\qquad
\mu=\frac{m_{\mathrm{string}}}{L},
\qquad
v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}}.
$$

The reusable route is

$$
m
\longrightarrow
\lambda_m
\longrightarrow
v_{\mathrm{wave}}
\longrightarrow
F_T.
$$

Combining the four relations gives the rule used throughout this lesson:

$$
\boxed{F_T=\frac{4}{m^2}m_{\mathrm{string}}L f_m^2}.
$$

This rule applies here because the string is uniform and both ends can be treated as nodes.

---

<a id="turn-the-harmonic-number-into-a-wavelength"></a>
## Turn the Harmonic Number into a Wavelength

**Example:** A string of length $1.20\ \mathrm{m}$ has nodes at both ends and vibrates at its fourth harmonic. Find the wavelength.

**Explanation**

For the fourth harmonic, $m=4$. The string contains four half-wavelengths:

$$
L=4\frac{\lambda_4}{2}.
$$

Solve for the wavelength:

$$
\lambda_4=\frac{2L}{4}
=\frac{2(1.20\ \mathrm{m})}{4}
=0.60\ \mathrm{m}.
$$

```quiz
type: radio
id: p4-harmonic-wavelength-q1
content: |-
  A string of length $L$ has nodes at both ends and vibrates at its fifth harmonic. What is its wavelength?
options:
- id: p4-harmonic-wavelength-q1-a
  content: |-
    $\dfrac{L}{5}$
- id: p4-harmonic-wavelength-q1-b
  content: |-
    $\dfrac{2L}{5}$
  correct: true
- id: p4-harmonic-wavelength-q1-c
  content: |-
    $\dfrac{5L}{2}$
- id: p4-harmonic-wavelength-q1-d
  content: |-
    $2L$
- id: p4-harmonic-wavelength-q1-e
  content: |-
    $5L$
```

---

<a id="use-frequency-to-find-wave-speed"></a>
## Use Frequency to Find Wave Speed

**Example:** A $0.90\ \mathrm{m}$ string vibrates at its third harmonic with frequency $120\ \mathrm{Hz}$. Find the wave speed.

**Explanation**

First find the third-harmonic wavelength:

$$
\lambda_3=\frac{2L}{3}
=\frac{2(0.90\ \mathrm{m})}{3}
=0.60\ \mathrm{m}.
$$

Then use $v_{\mathrm{wave}}=f\lambda$:

$$
v_{\mathrm{wave}}=f_3\lambda_3
=(120\ \mathrm{Hz})(0.60\ \mathrm{m})
=72\ \mathrm{m}/\mathrm{s}.
$$

```quiz
type: radio
id: p4-wave-speed-q1
content: |-
  A $1.20\ \mathrm{m}$ string has nodes at both ends and vibrates at its fourth harmonic with frequency $150\ \mathrm{Hz}$. What is the wave speed?
options:
- id: p4-wave-speed-q1-a
  content: |-
    $45\ \mathrm{m}/\mathrm{s}$
- id: p4-wave-speed-q1-b
  content: |-
    $90\ \mathrm{m}/\mathrm{s}$
  correct: true
- id: p4-wave-speed-q1-c
  content: |-
    $180\ \mathrm{m}/\mathrm{s}$
- id: p4-wave-speed-q1-d
  content: |-
    $360\ \mathrm{m}/\mathrm{s}$
- id: p4-wave-speed-q1-e
  content: |-
    $720\ \mathrm{m}/\mathrm{s}$
```

---

<a id="convert-wave-speed-into-tension"></a>
## Convert Wave Speed into Tension

**Example:** A uniform string has mass $0.12\ \mathrm{kg}$, length $0.80\ \mathrm{m}$, and wave speed $40\ \mathrm{m}/\mathrm{s}$. Find its tension.

**Explanation**

The string's linear mass density is its mass per unit length:

$$
\mu=\frac{m_{\mathrm{string}}}{L}
=\frac{0.12\ \mathrm{kg}}{0.80\ \mathrm{m}}
=0.15\ \mathrm{kg}/\mathrm{m}.
$$

Start with the string-speed relation and solve for $F_T$:

$$
\begin{aligned}
v_{\mathrm{wave}}&=\sqrt{\frac{F_T}{\mu}} \\
v_{\mathrm{wave}}^2&=\frac{F_T}{\mu} \\
\mu v_{\mathrm{wave}}^2&=F_T.
\end{aligned}
$$

Now substitute:

$$
F_T=(0.15\ \mathrm{kg}/\mathrm{m})(40\ \mathrm{m}/\mathrm{s})^2
=240\ \mathrm{N}.
$$

```quiz
type: radio
id: p4-speed-to-tension-q1
content: |-
  A uniform string has mass $0.18\ \mathrm{kg}$, length $0.90\ \mathrm{m}$, and wave speed $30\ \mathrm{m}/\mathrm{s}$. What is its tension?
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

**Example:** Derive the tension of a uniform string of mass $m_{\mathrm{string}}$ and length $L$ when it vibrates at frequency $f_m$ in its $m$th harmonic. Both ends are nodes.

**Explanation**

Begin with the harmonic wavelength and use it in $v_{\mathrm{wave}}=f\lambda$:

$$
\lambda_m=\frac{2L}{m},
\qquad
v_{\mathrm{wave}}=f_m\lambda_m
=\frac{2L f_m}{m}.
$$

The tension is $F_T=\mu v_{\mathrm{wave}}^2$, and $\mu=m_{\mathrm{string}}/L$. Substitute both expressions:

$$
\begin{aligned}
F_T
&=\mu v_{\mathrm{wave}}^2 \\
&=\frac{m_{\mathrm{string}}}{L}\left(\frac{2L f_m}{m}\right)^2 \\
&=\frac{m_{\mathrm{string}}}{L}\frac{4L^2f_m^2}{m^2} \\
&=\boxed{\frac{4}{m^2}m_{\mathrm{string}}L f_m^2}.
\end{aligned}
$$

The square applies to the entire wave-speed expression. In particular,

$$
\left(\frac{2}{m}\right)^2=\frac{4}{m^2},
$$

not $\frac{2}{m}$.

```quiz
type: radio
id: p4-general-tension-q1
content: |-
  A uniform string of mass $m_{\mathrm{string}}$ and length $L$ has nodes at both ends. It vibrates at frequency $f_4$ in its fourth harmonic. Which expression gives its tension?
options:
- id: p4-general-tension-q1-a
  content: |-
    $\dfrac{1}{16}m_{\mathrm{string}}L f_4^2$
- id: p4-general-tension-q1-b
  content: |-
    $\dfrac{1}{4}m_{\mathrm{string}}L f_4^2$
  correct: true
- id: p4-general-tension-q1-c
  content: |-
    $\dfrac{1}{2}m_{\mathrm{string}}L f_4^2$
- id: p4-general-tension-q1-d
  content: |-
    $4m_{\mathrm{string}}L f_4^2$
- id: p4-general-tension-q1-e
  content: |-
    $16m_{\mathrm{string}}L f_4^2$
```

As a quick units check,

$$
[m_{\mathrm{string}}L f_m^2]
=(\mathrm{kg})(\mathrm{m})(\mathrm{s}^{-2})
=\mathrm{N}.
$$

The coefficient $4/m^2$ is unitless, so the combined expression has the units of tension.

```quiz
type: radio
id: p4-homework-q1
shuffle: true
content: |-
  A uniform string of mass $m_{\mathrm{string}}$ and length $L$ is clamped at one end and attached to a wave generator at the other.

  When the wave generator is set to frequency $f_3$, the string vibrates at its third harmonic.

  What is the magnitude of the string's tension?

  Assume that the wave generator can be approximated as a node.
options:
- id: p4-homework-q1-a
  content: |-
    $\dfrac{1}{6}m_{\mathrm{string}}L f_3^2$
- id: p4-homework-q1-b
  content: |-
    $\dfrac{4}{9}m_{\mathrm{string}}L f_3^2$
  correct: true
- id: p4-homework-q1-c
  content: |-
    $\dfrac{3}{8}m_{\mathrm{string}}L f_3^2$
- id: p4-homework-q1-d
  content: |-
    $\dfrac{1}{2}m_{\mathrm{string}}L f_3^2$
```

---

<a id="summary"></a>
## Summary

**Recognition cue:** A uniform string has nodes at both ends, an $m$th-harmonic frequency is given, and the tension is requested.

**Rule chain:**

$$
\lambda_m=\frac{2L}{m},
\qquad
v_{\mathrm{wave}}=f_m\lambda_m,
\qquad
\mu=\frac{m_{\mathrm{string}}}{L},
\qquad
F_T=\mu v_{\mathrm{wave}}^2.
$$

**Combined result:**

$$
\boxed{F_T=\frac{4}{m^2}m_{\mathrm{string}}L f_m^2}.
$$

**Procedure:**

1. Use the harmonic number to find $\lambda_m=2L/m$.
2. Find the wave speed with $v_{\mathrm{wave}}=f_m\lambda_m$.
3. Find the linear density with $\mu=m_{\mathrm{string}}/L$.
4. Compute $F_T=\mu v_{\mathrm{wave}}^2$.

**Main trap:** The harmonic factor is inside the wave speed, so it must be squared when computing tension. For the third harmonic, $(2/3)^2=4/9$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
