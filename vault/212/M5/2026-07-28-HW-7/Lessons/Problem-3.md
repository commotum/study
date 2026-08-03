# Counting Wavelengths in a Refractive Medium

<!--
lesson-id: 212-M5-016
topic-code: MTH212.M5.16
-->

## Table of Contents

- [Introduction](#introduction)
- [Count Wavelengths Across a Distance](#count-wavelengths-across-a-distance)
- [Rewrite the Count Using Frequency](#rewrite-the-count-using-frequency)
- [Account for Refractive Index](#account-for-refractive-index)
- [Subtract the Two Counts](#subtract-the-two-counts)
- [Summary](#summary)

## Prerequisites

- Use the wave relation $v=f\lambda$.
- Use the refractive-index relation $n=c/v$.
- Factor a common symbolic multiplier from a difference.

---

<a id="introduction"></a>
## Introduction

When a wave travels a distance and the question asks how many wavelengths fit in that distance, start with

$$
N=\frac{d}{\lambda}.
$$

Here,

- $N$ is the number of wavelengths,
- $d$ is the distance traveled,
- $\lambda$ is the wavelength in the medium,
- $f$ is the frequency,
- $v$ is the wave speed in the medium,
- $n$ is the refractive index, and
- $c$ is the speed of light in vacuum.

The recognition cue is the combination of a path length, a wave frequency, and a request for a **number of wavelengths**. Use $v=f\lambda$ to replace the wavelength:

$$
\lambda=\frac{v}{f}
\qquad\Longrightarrow\qquad
N=\frac{d}{v/f}=\frac{df}{v}.
$$

For light in a medium with refractive index $n$, the speed is $v=c/n$. Therefore,

$$
N=\frac{df}{c/n}=\frac{ndf}{c}.
$$

The frequency stays unchanged when light enters the medium; the speed and wavelength change. This same count formula can therefore be written once for each stated frequency and then subtracted.

---

<a id="count-wavelengths-across-a-distance"></a>
## Count Wavelengths Across a Distance

**Example:** A wave has wavelength $3\ \mathrm{m}$ and spans a distance of $18\ \mathrm{m}$. How many wavelengths fit in that distance?

**Explanation**

Each wavelength occupies $3\ \mathrm{m}$, so divide the total distance by the length of one wavelength:

$$
N=\frac{d}{\lambda}
=\frac{18\ \mathrm{m}}{3\ \mathrm{m}}
=6.
$$

The result is a count, so it has no physical unit.

```quiz
type: radio
id: problem-3-q1
content: |-
  A wave has wavelength $4\ \mathrm{m}$. How many wavelengths fit in a distance of $24\ \mathrm{m}$?
options:
- id: problem-3-q1-a
  content: |-
    $6$
  correct: true
- id: problem-3-q1-b
  content: |-
    $96$
- id: problem-3-q1-c
  content: |-
    $20$
- id: problem-3-q1-d
  content: |-
    $28$
- id: problem-3-q1-e
  content: |-
    $\dfrac{1}{6}$
```

---

<a id="rewrite-the-count-using-frequency"></a>
## Rewrite the Count Using Frequency

**Example:** A wave travels at $12\ \mathrm{m/s}$ with frequency $3\ \mathrm{Hz}$. How many wavelengths fit in a distance of $20\ \mathrm{m}$?

**Explanation**

The wavelength is

$$
\lambda=\frac{v}{f}
=\frac{12\ \mathrm{m/s}}{3\ \mathrm{s}^{-1}}
=4\ \mathrm{m}.
$$

Substituting this into $N=d/\lambda$ gives

$$
N=\frac{d}{v/f}
=\frac{df}{v}
=\frac{(20\ \mathrm{m})(3\ \mathrm{s}^{-1})}{12\ \mathrm{m/s}}
=5.
$$

The units cancel, as they must for a wavelength count.

```quiz
type: radio
id: problem-3-q2
content: |-
  A wave travels at $18\ \mathrm{m/s}$ with frequency $6\ \mathrm{Hz}$. How many wavelengths fit in a distance of $12\ \mathrm{m}$?
options:
- id: problem-3-q2-a
  content: |-
    $4$
  correct: true
- id: problem-3-q2-b
  content: |-
    $3$
- id: problem-3-q2-c
  content: |-
    $2$
- id: problem-3-q2-d
  content: |-
    $72$
- id: problem-3-q2-e
  content: |-
    $\dfrac{1}{4}$
```

---

<a id="account-for-refractive-index"></a>
## Account for Refractive Index

**Example:** Light of frequency $f$ crosses a distance $d$ in a material with refractive index $n$. Express the number of wavelengths in terms of $n$, $d$, $f$, and the vacuum speed of light $c$.

**Explanation**

The refractive-index definition gives

$$
n=\frac{c}{v}
\qquad\Longrightarrow\qquad
v=\frac{c}{n}.
$$

Insert this medium speed into $N=df/v$:

$$
N=\frac{df}{c/n}
=df\left(\frac{n}{c}\right)
=\frac{ndf}{c}.
$$

The important algebraic trap is the fraction in the denominator: dividing by $c/n$ multiplies by $n/c$. Thus, for fixed $d$ and $f$, a larger $n$ produces more wavelengths across the same distance.

```quiz
type: radio
id: problem-3-q3
content: |-
  Light of frequency $f$ travels a distance $d$ through a medium of refractive index $n$. Which expression gives the number of wavelengths traversed?
options:
- id: problem-3-q3-a
  content: |-
    $\dfrac{ndf}{c}$
  correct: true
- id: problem-3-q3-b
  content: |-
    $\dfrac{df}{nc}$
- id: problem-3-q3-c
  content: |-
    $\dfrac{cdf}{n}$
- id: problem-3-q3-d
  content: |-
    $\dfrac{ndc}{f}$
- id: problem-3-q3-e
  content: |-
    $\dfrac{df}{c}$
```

---

<a id="subtract-the-two-counts"></a>
## Subtract the Two Counts

**Example:** Two waves with frequencies $f_A$ and $f_B$ cross the same distance $d$ in a medium with refractive index $n$. Find $N_A-N_B$.

**Explanation**

Because the two waves share the same $n$ and $d$, each count has the same multiplier:

$$
N_A=\frac{ndf_A}{c},
\qquad
N_B=\frac{ndf_B}{c}.
$$

Subtract in the requested order and factor the common multiplier:

$$
\begin{aligned}
N_A-N_B
&=\frac{ndf_A}{c}-\frac{ndf_B}{c}\\
&=\frac{nd}{c}(f_A-f_B).
\end{aligned}
$$

As a quick check, $nd/c$ has units of time and $f_A-f_B$ has units of inverse time, so their product is a dimensionless count.

There are also two useful direction checks:

- The higher-frequency wave must fit more wavelengths into the same distance.
- Increasing either $n$ or $d$ must increase the count difference, so both factors belong in the numerator.

```quiz
type: radio
id: problem-3-q4
shuffle: true
content: |-
  Green light of frequency $f_g$ and red light of frequency $f_r$ traverse a distance of $d$ within a piece of glass having refractive index $n$.

  What is the difference between the numbers of wavelengths traversed by the two colors?

  Consider the speed of light in vacuum $c$ to be a given quantity.
options:
- id: problem-3-q4-a
  content: |-
    $0$
- id: problem-3-q4-b
  content: |-
    $\dfrac{c}{nd}(f_g-f_r)$
- id: problem-3-q4-c
  content: |-
    $\dfrac{nd}{c}(f_g-f_r)$
  correct: true
- id: problem-3-q4-d
  content: |-
    $\dfrac{c}{d}(f_g-f_r)$
- id: problem-3-q4-e
  content: |-
    $\dfrac{d}{nc}(f_g-f_r)$
```

---

<a id="summary"></a>
## Summary

When a problem asks for the number of wavelengths across a distance:

1. Start with $N=d/\lambda$.
2. Use $\lambda=v/f$ to obtain $N=df/v$.
3. In a medium, substitute $v=c/n$ to obtain $N=ndf/c$.
4. For two frequencies in the same medium and over the same distance, subtract the counts and factor:

$$
\Delta N=\frac{nd}{c}(f_1-f_2).
$$

The main trap is dividing by $c/n$ incorrectly. Since $c/n$ is the medium speed, it belongs in the denominator of $df/v$, so the final count is multiplied by $n$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
