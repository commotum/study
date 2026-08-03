# Changing Frequency on the Same Taut String

<!--
lesson-id: 212-M5-014
topic-code: MTH212.M5.14
-->

## Table of Contents

- [Introduction](#introduction)
- [Decide Whether the Wave Speed Changes](#decide-whether-the-wave-speed-changes)
- [Use the Wave Equation at Fixed Speed](#use-the-wave-equation-at-fixed-speed)
- [Scale the Wavelength by a Frequency Factor](#scale-the-wavelength-by-a-frequency-factor)
- [Avoid the Frequency-Speed Trap](#avoid-the-frequency-speed-trap)
- [Summary](#summary)

## Prerequisites

- Interpret frequency as cycles per second and wavelength as the length of one cycle.
- Rearrange a multiplication equation and work with simple ratios.

---

<a id="introduction"></a>
## Introduction

When a source vibrates the **same taut string** at a new frequency, first ask what sets the wave speed. For a string,

$$
v=\sqrt{\frac{T}{\mu}},
$$

where $T$ is the tension and $\mu$ is the string's mass per unit length. If the string and its tension stay the same, then $T$ and $\mu$ stay fixed, so the wave speed $v$ stays fixed.

The frequency $f$ and wavelength $\lambda$ must then adjust to satisfy

$$
v=f\lambda.
$$

The reusable move is: **hold $v$ fixed, then make $\lambda$ change inversely with $f$.**

| Quantity | What controls it here? | When the driving frequency doubles |
| --- | --- | --- |
| Wave speed $v$ | The string's $T$ and $\mu$ | Stays the same |
| Frequency $f$ | The driver | Doubles |
| Wavelength $\lambda$ | The constraint $v=f\lambda$ | Is halved |

---

<a id="decide-whether-the-wave-speed-changes"></a>
## Decide Whether the Wave Speed Changes

**Example:** A taut string is driven first at $30\,\mathrm{Hz}$ and then at $60\,\mathrm{Hz}$. The string and its tension are unchanged. What happens to the wave speed?

**Explanation**

The same string means $\mu$ is unchanged, and the unchanged tension means $T$ is unchanged. Therefore,

$$
v=\sqrt{\frac{T}{\mu}}
$$

has the same value before and after the frequency change. The wave speed is unchanged.

```quiz
type: radio
id: p1-speed-q1
content: |-
  A taut string is driven first at $45\,\mathrm{Hz}$ and then at $90\,\mathrm{Hz}$. Its tension and mass per unit length do not change. What happens to the wave speed?
options:
- id: p1-speed-q1-a
  content: |-
    It doubles because the frequency doubles.
- id: p1-speed-q1-b
  content: |-
    It is halved because the frequency doubles.
- id: p1-speed-q1-c
  content: |-
    It is unchanged because $T$ and $\mu$ are unchanged.
  correct: true
- id: p1-speed-q1-d
  content: |-
    It becomes four times as large.
- id: p1-speed-q1-e
  content: |-
    It cannot be determined even though $T$ and $\mu$ are fixed.
```

---

<a id="use-the-wave-equation-at-fixed-speed"></a>
## Use the Wave Equation at Fixed Speed

**Example:** Waves travel along a string at $24\,\mathrm{m/s}$. At $6\,\mathrm{Hz}$, the wavelength is

$$
\lambda_1=\frac{v}{f_1}
=\frac{24}{6}
=4\,\mathrm{m}.
$$

The frequency is doubled to $12\,\mathrm{Hz}$ without changing the string or its tension. Find the new wavelength.

**Explanation**

Because the string conditions are fixed, $v_1=v_2$. Applying $v=f\lambda$ before and after the change gives the constant-product relation

$$
f_1\lambda_1=f_2\lambda_2.
$$

Equivalently, because the speed remains $24\,\mathrm{m/s}$,

$$
\lambda_2=\frac{v}{f_2}
=\frac{24}{12}
=2\,\mathrm{m}.
$$

Doubling the frequency changed the wavelength from $4\,\mathrm{m}$ to $2\,\mathrm{m}$: it was halved.

```quiz
type: radio
id: p1-wave-equation-q1
content: |-
  Waves travel along a fixed string at $18\,\mathrm{m/s}$. The frequency changes from $3\,\mathrm{Hz}$ to $6\,\mathrm{Hz}$ while the string conditions remain fixed. What are the new wave speed and wavelength?
options:
- id: p1-wave-equation-q1-a
  content: |-
    $36\,\mathrm{m/s}$ and $6\,\mathrm{m}$
- id: p1-wave-equation-q1-b
  content: |-
    $36\,\mathrm{m/s}$ and $3\,\mathrm{m}$
- id: p1-wave-equation-q1-c
  content: |-
    $18\,\mathrm{m/s}$ and $6\,\mathrm{m}$
- id: p1-wave-equation-q1-d
  content: |-
    $18\,\mathrm{m/s}$ and $3\,\mathrm{m}$
  correct: true
- id: p1-wave-equation-q1-e
  content: |-
    $9\,\mathrm{m/s}$ and $3\,\mathrm{m}$
```

---

<a id="scale-the-wavelength-by-a-frequency-factor"></a>
## Scale the Wavelength by a Frequency Factor

**Example:** On one unchanged string, the driving frequency becomes three times its original value. If the original wavelength was $0.90\,\mathrm{m}$, what is the new wavelength?

**Explanation**

At fixed speed,

$$
f_1\lambda_1=f_2\lambda_2.
$$

Since $f_2=3f_1$,

$$
\lambda_2
=\frac{f_1}{f_2}\lambda_1
=\frac{1}{3}(0.90\,\mathrm{m})
=0.30\,\mathrm{m}.
$$

Multiplying frequency by $3$ divides wavelength by $3$.

More generally, if the frequency changes by a positive factor $r$,

$$
f_2=rf_1
\qquad\Longrightarrow\qquad
\lambda_2=\frac{\lambda_1}{r}.
$$

| Frequency change | Wavelength change at fixed speed |
| --- | --- |
| Multiply by $2$ | Divide by $2$ |
| Multiply by $3$ | Divide by $3$ |
| Multiply by $\tfrac12$ | Divide by $\tfrac12$, so multiply by $2$ |

```quiz
type: radio
id: p1-scaling-q1
content: |-
  The frequency of waves on an unchanged taut string is reduced to one-half of its original value. What happens to the wave speed and wavelength?
options:
- id: p1-scaling-q1-a
  content: |-
    The speed is halved, and the wavelength is unchanged.
- id: p1-scaling-q1-b
  content: |-
    The speed is unchanged, and the wavelength is halved.
- id: p1-scaling-q1-c
  content: |-
    The speed is unchanged, and the wavelength doubles.
  correct: true
- id: p1-scaling-q1-d
  content: |-
    The speed doubles, and the wavelength is halved.
- id: p1-scaling-q1-e
  content: |-
    The speed and wavelength are both unchanged.
```

---

<a id="avoid-the-frequency-speed-trap"></a>
## Avoid the Frequency-Speed Trap

**Example:** A student says, “If I vibrate the string twice as fast, the waves must travel twice as fast.” Is that correct when the same string remains at the same tension?

**Explanation**

No. The driving frequency tells how many cycles are produced each second, but $T$ and $\mu$ set the propagation speed on the string. With $T$ and $\mu$ fixed, the speed cannot double. Instead, twice as many cycles must fit into the distance traveled each second, so each wavelength is half as long.

```quiz
type: radio
id: p1-homework-q1
content: |-
  If you vibrate a taut string at twice the original frequency, what happens to the wave speed and wavelength?
options:
- id: p1-homework-q1-a
  content: |-
    The speed doubles, and the wavelength is unchanged.
- id: p1-homework-q1-b
  content: |-
    The speed doubles, and the wavelength doubles.
- id: p1-homework-q1-c
  content: |-
    The speed doubles, while the wavelength is halved.
- id: p1-homework-q1-d
  content: |-
    The speed is unchanged, while the wavelength doubles.
- id: p1-homework-q1-e
  content: |-
    The speed is unchanged, while the wavelength is halved.
  correct: true
- id: p1-homework-q1-f
  content: |-
    The speed and wavelength are both unchanged.
```

---

<a id="summary"></a>
## Summary

**Recognition cue:** The problem changes the driving frequency but keeps the same string and tension.

**Invariant:** Unchanged $T$ and $\mu$ mean unchanged $v$, so the product $f\lambda$ remains constant.

**Procedure:**

1. Hold the wave speed fixed.
2. Write $f_1\lambda_1=f_2\lambda_2$.
3. Reverse the frequency factor to get the wavelength factor.

**Main trap:** A higher driving frequency does not make the wave travel faster on an unchanged string; it makes the wavelength shorter. In particular, doubling $f$ leaves $v$ unchanged and halves $\lambda$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
