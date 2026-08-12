# Fundamental Frequency of a Tensioned Wire

<!--
lesson-id: 212-M5-032
topic-code: MTH212.M5.32
-->

## Table of Contents

- [Introduction](#introduction)
- [Connect the Fundamental Mode to Wave Speed](#connect-the-fundamental-mode-to-wave-speed)
- [Combine the Wire Data Into One Formula](#combine-the-wire-data-into-one-formula)
- [Keep Total Mass and Linear Density Distinct](#keep-total-mass-and-linear-density-distinct)
- [Match the Required Answer Form](#match-the-required-answer-form)
- [Summary](#summary)

## Prerequisites

- Evaluate a square root with a calculator.
- Substitute values into a formula while keeping the denominator grouped.
- Recognize $\mathrm{Hz}=\mathrm{s}^{-1}$ and round a final result to the requested precision.

---

<a id="introduction"></a>
## Introduction

When a wire fixed at both ends is described by its length $L$, total mass $m$, and tension $F_T$, and the question asks for its **fundamental frequency**, use the fundamental standing-wave length together with the wave speed on the wire:

$$
\lambda_1=2L,
\qquad
v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}},
\qquad
\mu=\frac{m}{L}.
$$

The task is to turn the total mass into linear mass density, find the wave speed, and divide that speed by the fundamental wavelength. The result must be a frequency in hertz.

Before calculating, make three checks:

- **Boundary condition:** the wire is fixed at both ends.
- **Mode:** the requested frequency is the fundamental, so the wavelength is $2L$.
- **Mass quantity:** the given mass is the total wire mass, so first use $\mu=m/L$ or use the equivalent total-mass formula directly.

---

<a id="connect-the-fundamental-mode-to-wave-speed"></a>
## Connect the Fundamental Mode to Wave Speed

For the fundamental mode, one half-wavelength fits along the wire, so $\lambda_1=2L$. Since $f=v_{\mathrm{wave}}/\lambda$,

$$
f_1=\frac{v_{\mathrm{wave}}}{2L}.
$$

**Example:** A wire fixed at both ends has $L=2.0\ \mathrm{m}$, total mass $m=0.080\ \mathrm{kg}$, and tension $F_T=16\ \mathrm{N}$. Find its fundamental frequency.

**Explanation**

First convert total mass to mass per unit length:

$$
\mu=\frac{m}{L}=\frac{0.080\ \mathrm{kg}}{2.0\ \mathrm{m}}
=0.040\ \mathrm{kg}/\mathrm{m}.
$$

Then find the wave speed and use $\lambda_1=2L$:

$$
v_{\mathrm{wave}}=\sqrt{\frac{16}{0.040}}=20\ \mathrm{m}/\mathrm{s},
\qquad
f_1=\frac{20}{2(2.0)}=5.0\ \mathrm{Hz}.
$$

```quiz
type: radio
id: problem-2-fundamental-q1
content: |-
  A wire fixed at both ends has $L=1.5\ \mathrm{m}$, total mass $m=0.060\ \mathrm{kg}$, and tension $F_T=36\ \mathrm{N}$. What is its fundamental frequency?
options:
- id: a
  content: |-
    $5.0\ \mathrm{Hz}$
- id: b
  content: |-
    $10\ \mathrm{Hz}$
  correct: true
  feedback: |-
    $\mu=0.040\ \mathrm{kg}/\mathrm{m}$, $v_{\mathrm{wave}}=30\ \mathrm{m}/\mathrm{s}$, and $f_1=v_{\mathrm{wave}}/(2L)=10\ \mathrm{Hz}$.
- id: c
  content: |-
    $20\ \mathrm{Hz}$
- id: d
  content: |-
    $30\ \mathrm{Hz}$
- id: e
  content: |-
    $40\ \mathrm{Hz}$
```

---

<a id="combine-the-wire-data-into-one-formula"></a>
## Combine the Wire Data Into One Formula

If the problem gives the wire's **total mass** rather than $\mu$, substitute $\mu=m/L$ into the fundamental-frequency formula:

$$
f_1
=\frac{1}{2L}\sqrt{\frac{F_T}{m/L}}
=\frac12\sqrt{\frac{F_T}{mL}}.
$$

This compact form uses the three given quantities directly.

The units provide a quick check:

$$
\left[\frac{F_T}{mL}\right]
=\frac{\mathrm{N}}{\mathrm{kg}\cdot\mathrm{m}}
=\frac{\mathrm{kg}\cdot\mathrm{m}/\mathrm{s}^2}
{\mathrm{kg}\cdot\mathrm{m}}
=\mathrm{s}^{-2}.
$$

Taking the square root gives $\mathrm{s}^{-1}=\mathrm{Hz}$, as a frequency should.

**Example:** A wire has $L=0.80\ \mathrm{m}$, $m=0.0050\ \mathrm{kg}$, and $F_T=40\ \mathrm{N}$. Find $f_1$.

**Explanation**

Keep the product $mL$ together in the denominator:

$$
f_1
=\frac12\sqrt{\frac{40}{(0.0050)(0.80)}}
=\frac12\sqrt{10\,000}
=50\ \mathrm{Hz}.
$$

On a calculator, evaluate in the same visible order as the formula:

1. Compute $mL$.
2. Compute $F_T/(mL)$.
3. Take the square root.
4. Multiply by $1/2$.

This keeps the entire quotient inside the radical and prevents premature rounding.

```quiz
type: radio
id: problem-2-fundamental-q2
content: |-
  A wire has $L=1.25\ \mathrm{m}$, total mass $m=0.0080\ \mathrm{kg}$, and tension $F_T=36\ \mathrm{N}$. What is its fundamental frequency?
options:
- id: a
  content: |-
    $15\ \mathrm{Hz}$
- id: b
  content: |-
    $30\ \mathrm{Hz}$
  correct: true
  feedback: |-
    $f_1=\frac12\sqrt{36/[(0.0080)(1.25)]}=30\ \mathrm{Hz}$.
- id: c
  content: |-
    $36\ \mathrm{Hz}$
- id: d
  content: |-
    $60\ \mathrm{Hz}$
- id: e
  content: |-
    $75\ \mathrm{Hz}$
```

---

<a id="keep-total-mass-and-linear-density-distinct"></a>
## Keep Total Mass and Linear Density Distinct

The symbol $m$ is the mass of the whole vibrating wire, measured in kilograms. The symbol $\mu$ is mass per unit length, measured in kilograms per meter. They are related by $\mu=m/L$, but they cannot be inserted into the same formula as though they were interchangeable.

**Example:** For $L=0.90\ \mathrm{m}$, $m=0.0030\ \mathrm{kg}$, and $F_T=27\ \mathrm{N}$, choose a correct direct setup.

**Explanation**

Because the given mass is total mass, use

$$
f_1=\frac12\sqrt{\frac{27}{(0.0030)(0.90)}}.
$$

The factor $1/2$ comes from $\lambda_1=2L$. Omitting it returns twice the fundamental frequency. Using $m$ directly in $f_1=(1/2L)\sqrt{F_T/\mu}$ treats kilograms as though they were kilograms per meter.

```quiz
type: radio
id: problem-2-fundamental-q3
content: |-
  A wire fixed at both ends has $L=1.10\ \mathrm{m}$, total mass $m=0.0040\ \mathrm{kg}$, and tension $F_T=44\ \mathrm{N}$. Which expression correctly gives its fundamental frequency?
options:
- id: a
  content: |-
    $\displaystyle \frac12\sqrt{\frac{44}{(0.0040)(1.10)}}$
  correct: true
  feedback: |-
    This is $f_1=\frac12\sqrt{F_T/(mL)}$, the direct formula when total wire mass is given.
- id: b
  content: |-
    $\displaystyle \sqrt{\frac{44}{(0.0040)(1.10)}}$
  feedback: |-
    This omits the factor $1/2$ supplied by the fundamental wavelength $\lambda_1=2L$.
- id: c
  content: |-
    $\displaystyle \frac{1}{2(1.10)}\sqrt{\frac{44}{0.0040}}$
  feedback: |-
    This inserts total mass $m$ where the linear mass density $\mu$ belongs.
- id: d
  content: |-
    $\displaystyle \frac12\sqrt{\frac{(0.0040)(1.10)}{44}}$
  feedback: |-
    This reverses the tension-to-mass-length quotient.
- id: e
  content: |-
    $\displaystyle \frac12\sqrt{\frac{44(1.10)}{0.0040}}$
  feedback: |-
    After substituting $\mu=m/L$, the length belongs with $m$ in the denominator: $mL$.
```

---

<a id="match-the-required-answer-form"></a>
## Match the Required Answer Form

Carry extra calculator digits until the end. Then round using the precision of the measured givens and follow the requested response format.

**Example:** A wire is $0.85\ \mathrm{m}$ long, has a mass of $0.0022\ \mathrm{kg}$, and is under $52\ \mathrm{N}$ of tension. What is its fundamental frequency?

Enter the fundamental frequency in hertz as a number only.

**Explanation**

$$
f_1
=\frac12\sqrt{\frac{52\ \mathrm{N}}
{(0.0022\ \mathrm{kg})(0.85\ \mathrm{m})}}
=83.377\ldots\ \mathrm{Hz}.
$$

The measured values have two significant figures, so $f_1=83\ \mathrm{Hz}$. Because the response must be a number only, enter $83$.

Keep those two stages distinct: $83.377\ldots\ \mathrm{Hz}$ is the calculator result, while $83$ is the requested number-only response.

```quiz
type: radio
id: problem-2-fundamental-q4
content: |-
  A wire has $L=0.60\ \mathrm{m}$, total mass $m=0.0030\ \mathrm{kg}$, and tension $F_T=30\ \mathrm{N}$. Its fundamental frequency must be entered in hertz as a number only. Which number should be entered?
options:
- id: a
  content: |-
    $32$
- id: b
  content: |-
    $64$
- id: c
  content: |-
    $64.549$
- id: d
  content: |-
    $65$
  correct: true
  feedback: |-
    The calculator value is $64.549\ldots\ \mathrm{Hz}$. Round only at the end to two significant figures and enter $65$.
- id: e
  content: |-
    $130$
```

---

<a id="summary"></a>
## Summary

For a wire fixed at both ends, the phrase **fundamental frequency** signals $\lambda_1=2L$. If the givens are tension $F_T$, total wire mass $m$, and length $L$:

1. Use $\mu=m/L$ and $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$, or go directly to
   $$
   f_1=\frac12\sqrt{\frac{F_T}{mL}}.
   $$
2. Keep $mL$ grouped beneath the fraction and keep the factor $1/2$.
3. Check that the units reduce to $\mathrm{s}^{-1}$, or hertz.
4. Round only the final frequency, then enter it in the requested form.

The main trap is confusing total mass $m$ with linear mass density $\mu$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
