# Third-Harmonic Frequency of a Wire Tensioned by a Hanging Mass

<!--
lesson-id: 212-M5-033
topic-code: MTH212.M5.33
-->

## Table of Contents

- [Introduction](#introduction)
- [Translate the Setup Into Quantities](#translate-the-setup-into-quantities)
- [Build the Harmonic-Frequency Formula](#build-the-harmonic-frequency-formula)
- [Keep the Harmonic Number](#keep-the-harmonic-number)
- [Solve the Given Wire-and-Pulley Problem](#solve-the-given-wire-and-pulley-problem)
- [Summary](#summary)

## Prerequisites

- Use $T=Mg$ for the tension supplied by a stationary hanging mass.
- Compute linear mass density with $\mu=m_w/L$.
- Recognize that a wire fixed at both ends has $f_n=\dfrac{n}{2L}\sqrt{\dfrac{T}{\mu}}$.
- Round a calculated result to the significant figures allowed by the measured givens.

---

<a id="introduction"></a>
## Introduction

When a horizontal wire passes over a pulley to a stationary hanging mass, the diagram supplies more than geometry: the hanging mass determines the tension, and the vibrating length helps determine the wire's linear mass density. The reusable procedure is to read the two masses and the vibrating length, calculate $T$ and $\mu$, and then substitute them into the fixed-end harmonic formula.

**Recognition cue:** Look for a fixed-end wire, a stationary hanging mass, the wire's own mass, and a request for a particular harmonic. That combination calls for the chain

$$
(M,m_w,L)\longrightarrow(T,\mu)\longrightarrow v\longrightarrow f_n.
$$

Use different symbols for the two masses:

- $M$: hanging mass, used in $T=Mg$
- $m_w$: mass of the vibrating wire, used in $\mu=m_w/L$

Mixing up these masses is the main trap.

---

<a id="translate-the-setup-into-quantities"></a>
## Translate the Setup Into Quantities

**Example:** A $3.0\ \mathrm{m}$ vibrating wire has mass $0.012\ \mathrm{kg}$ and is tensioned by a stationary $5.0\ \mathrm{kg}$ hanging mass. Use $g=9.8\ \mathrm{m/s^2}$. Find $T$ and $\mu$.

**Explanation**

Use the hanging mass only for the tension:

$$
T=Mg=(5.0\ \mathrm{kg})(9.8\ \mathrm{m/s^2})=49\ \mathrm{N}.
$$

Use the wire mass and vibrating length for the density:

$$
\mu=\frac{m_w}{L}
=\frac{0.012\ \mathrm{kg}}{3.0\ \mathrm{m}}
=0.0040\ \mathrm{kg/m}.
$$

```quiz
type: radio
id: p3-translate-setup
content: |-
  A $2.0\ \mathrm{m}$ wire has mass $0.010\ \mathrm{kg}$ and is tensioned by a stationary $3.0\ \mathrm{kg}$ hanging mass. Use $g=9.8\ \mathrm{m/s^2}$. Which pair gives the tension $T$ and linear mass density $\mu$?
options:
- id: a
  content: |-
    $T=29.4\ \mathrm{N}$ and $\mu=0.0050\ \mathrm{kg/m}$
  correct: true
  feedback: |-
    The two masses have different roles: the hanging mass sets $T=Mg$, while the wire's own mass sets $\mu=m_w/L$. Thus $T=(3.0)(9.8)=29.4\ \mathrm{N}$ and $\mu=0.010/2.0=0.0050\ \mathrm{kg/m}$.
- id: b
  content: |-
    $T=3.0\ \mathrm{N}$ and $\mu=0.0050\ \mathrm{kg/m}$
  feedback: |-
    $3.0\ \mathrm{kg}$ is the hanging mass, not a force. Because the mass is stationary, its weight sets the tension: $T=Mg=29.4\ \mathrm{N}$; the stated $\mu$ is correct.
- id: c
  content: |-
    $T=29.4\ \mathrm{N}$ and $\mu=0.020\ \mathrm{kg/m}$
  feedback: |-
    Linear mass density means mass per unit length, so divide the wire mass by its length. The tension is correct, but $\mu=0.010/2.0=0.0050\ \mathrm{kg/m}$, not $0.020\ \mathrm{kg/m}$.
- id: d
  content: |-
    $T=0.098\ \mathrm{N}$ and $\mu=1.5\ \mathrm{kg/m}$
  feedback: |-
    This swaps the masses' physical roles. The $3.0\ \mathrm{kg}$ hanging mass supplies $T=29.4\ \mathrm{N}$, while the $0.010\ \mathrm{kg}$ wire supplies $\mu=0.0050\ \mathrm{kg/m}$.
- id: e
  content: |-
    $T=29.4\ \mathrm{N}$ and $\mu=1.5\ \mathrm{kg/m}$
  feedback: |-
    The hanging mass correctly gives $T=29.4\ \mathrm{N}$, but it does not give the wire's linear density. Use the wire mass: $\mu=0.010\ \mathrm{kg}/2.0\ \mathrm{m}=0.0050\ \mathrm{kg/m}$.
```

---

<a id="build-the-harmonic-frequency-formula"></a>
## Build the Harmonic-Frequency Formula

**Example:** A $3.0\ \mathrm{m}$ wire has $T=49\ \mathrm{N}$ and $\mu=0.0040\ \mathrm{kg/m}$. Find its third-harmonic frequency.

**Explanation**

The transverse-wave speed is

$$
v=\sqrt{\frac{T}{\mu}}.
$$

For a wire fixed at both ends, $f_n=\dfrac{nv}{2L}$. Combining the two formulas and setting $n=3$ gives

$$
f_3=\frac{3}{2L}\sqrt{\frac{T}{\mu}}.
$$

Now substitute:

$$
\begin{aligned}
v
&=\sqrt{\frac{49\ \mathrm{N}}{0.0040\ \mathrm{kg/m}}} \\
&=110.68\ldots\ \mathrm{m/s}, \\
f_3
&=\frac{3(110.68\ldots\ \mathrm{m/s})}{2(3.0\ \mathrm{m})} \\
&=55.34\ldots\ \mathrm{Hz} \\
&=55\ \mathrm{Hz}.
\end{aligned}
$$

The units provide a built-in check:

$$
\frac{[T]}{[\mu]}
=\frac{\mathrm{kg\,m/s^2}}{\mathrm{kg/m}}
=\mathrm{m^2/s^2},
$$

so $v$ has units $\mathrm{m/s}$, and dividing $v$ by a length gives $\mathrm{s^{-1}}=\mathrm{Hz}$.

```quiz
type: radio
id: p3-build-frequency
content: |-
  A $2.4\ \mathrm{m}$ wire has tension $60\ \mathrm{N}$ and linear mass density $0.0060\ \mathrm{kg/m}$. What is its third-harmonic frequency?
options:
- id: a
  content: |-
    $20.8\ \mathrm{Hz}$
  feedback: |-
    $20.8\ \mathrm{Hz}=v/(2L)$ is the fundamental. On a fixed-end wire, $f_n=nf_1$, so the third harmonic is $3(20.8\ldots)=62.5\ \mathrm{Hz}$.
- id: b
  content: |-
    $31.3\ \mathrm{Hz}$
  feedback: |-
    This is half the required result, as if the fixed-end factor of $2$ were applied twice. With $v=100\ \mathrm{m/s}$, use $f_3=3v/(2L)=62.5\ \mathrm{Hz}$.
- id: c
  content: |-
    $62.5\ \mathrm{Hz}$
  correct: true
  feedback: |-
    Tension and linear density set the wave speed: $v=\sqrt{T/\mu}=100\ \mathrm{m/s}$. A fixed-end wire's third harmonic has $f_3=3v/(2L)=62.5\ \mathrm{Hz}$.
- id: d
  content: |-
    $125\ \mathrm{Hz}$
  feedback: |-
    A fixed-end fundamental fits half a wavelength, which produces the denominator $2L$. Omitting that $2$ doubles $62.5\ \mathrm{Hz}$ to $125\ \mathrm{Hz}$.
- id: e
  content: |-
    $6.25\ \mathrm{Hz}$
  feedback: |-
    The third harmonic must be three times the fundamental, which is $100/(2\cdot2.4)=20.8\ldots\ \mathrm{Hz}$. Therefore $6.25\ \mathrm{Hz}$ cannot be the third harmonic; the correct value is $62.5\ \mathrm{Hz}$.
```

---

<a id="keep-the-harmonic-number"></a>
## Keep the Harmonic Number

**Example:** A fixed-end wire has fundamental frequency $f_1=18\ \mathrm{Hz}$. Find its third-harmonic frequency.

**Explanation**

For the same wire under the same tension, harmonic frequencies are integer multiples of the fundamental:

$$
f_n=nf_1.
$$

Therefore,

$$
f_3=3f_1=3(18\ \mathrm{Hz})=54\ \mathrm{Hz}.
$$

If a calculation for the third harmonic equals the fundamental frequency, the factor $n=3$ was omitted.

```quiz
type: radio
id: p3-harmonic-number
content: |-
  A fixed-end wire has a fundamental frequency of $42\ \mathrm{Hz}$. What is its third-harmonic frequency?
options:
- id: a
  content: |-
    $14\ \mathrm{Hz}$
  feedback: |-
    Harmonic number multiplies the fundamental: $f_n=nf_1$. Dividing $42\ \mathrm{Hz}$ by $3$ produces a subharmonic, whereas the third harmonic is $126\ \mathrm{Hz}$.
- id: b
  content: |-
    $42\ \mathrm{Hz}$
  feedback: |-
    $42\ \mathrm{Hz}$ is $f_1$. The third harmonic has three times that frequency, so retaining $42\ \mathrm{Hz}$ omits $n=3$ and the answer should be $126\ \mathrm{Hz}$.
- id: c
  content: |-
    $84\ \mathrm{Hz}$
  feedback: |-
    $84\ \mathrm{Hz}=2f_1$, so it corresponds to the second harmonic. The requested third harmonic is $3f_1=126\ \mathrm{Hz}$.
- id: d
  content: |-
    $126\ \mathrm{Hz}$
  correct: true
  feedback: |-
    On the same fixed-end wire, harmonic frequencies are integer multiples of the fundamental. Thus $f_3=3f_1=3(42\ \mathrm{Hz})=126\ \mathrm{Hz}$.
- id: e
  content: |-
    $378\ \mathrm{Hz}$
  feedback: |-
    $378\ \mathrm{Hz}=9f_1$, so the factor $3$ has been applied twice. Apply the harmonic number once: $f_3=3(42\ \mathrm{Hz})=126\ \mathrm{Hz}$.
```

---

<a id="solve-the-given-wire-and-pulley-problem"></a>
## Solve the Given Wire-and-Pulley Problem

**Example:** The wire between the wall and pulley has a mass of $0.0035\ \mathrm{kg}$. What is the frequency of its third harmonic? Assume the hanging mass is stationary and use $g=9.81\ \mathrm{m/s^2}$.

![](<../Source/Images/wire-pulley-hanging-mass.png>)

**Explanation**

Sort each given by its role before calculating:

| Given | Symbol | Role |
|---|---:|---|
| vibrating span $3.1\ \mathrm{m}$ | $L$ | wire length |
| hanging mass $8.2\ \mathrm{kg}$ | $M$ | supplies tension |
| wire mass $0.0035\ \mathrm{kg}$ | $m_w$ | supplies linear density |
| $9.81\ \mathrm{m/s^2}$ | $g$ | converts $M$ to tension |
| third harmonic | $n=3$ | selects $f_3$ |

First calculate the two derived quantities:

$$
T=Mg=(8.2\ \mathrm{kg})(9.81\ \mathrm{m/s^2})=80.442\ \mathrm{N}
$$

and

$$
\mu=\frac{m_w}{L}
=\frac{0.0035\ \mathrm{kg}}{3.1\ \mathrm{m}}
=0.001129\ldots\ \mathrm{kg/m}.
$$

Continue one substitution at a time without rounding the intermediate values:

$$
\begin{aligned}
v
&=\sqrt{\frac{T}{\mu}} \\
&=\sqrt{\frac{80.442\ \mathrm{N}}{0.0035\ \mathrm{kg}/(3.1\ \mathrm{m})}} \\
&=266.924\ldots\ \mathrm{m/s}, \\
f_1
&=\frac{v}{2L} \\
&=43.052\ldots\ \mathrm{Hz}, \\
f_3
&=3f_1 \\
&=129.156\ldots\ \mathrm{Hz}.
\end{aligned}
$$

The check $f_3=3f_1$ confirms that the requested harmonic factor was included. The measured masses and length have two significant figures, so the answer is $1.3\times10^2\ \mathrm{Hz}$, entered as the number $130$.

**Source answer form:** Enter the third-harmonic frequency in hertz as a number only.

```quiz
type: radio
id: p3-source-check
content: |-
  The wire between the wall and pulley has a mass of $0.0035\ \mathrm{kg}$. What is the frequency of its third harmonic? Assume the hanging mass is stationary and use $g=9.81\ \mathrm{m/s^2}$.

  ![](<../Source/Images/wire-pulley-hanging-mass.png>)

  The source response field asks for the frequency in hertz as a number only. Which number should be entered?
options:
- id: a
  content: |-
    $43$
  feedback: |-
    $43\ \mathrm{Hz}$ is the wire's fundamental, $f_1=v/(2L)$. The question asks for $f_3=3f_1\approx129\ \mathrm{Hz}$, which rounds to the number-only entry $130$.
- id: b
  content: |-
    $80$
  feedback: |-
    The value near $80$ comes from $T=Mg=80.442\ \mathrm{N}$, so it is a force rather than a frequency. Tension first determines $v$, and the resulting third-harmonic frequency rounds to $130\ \mathrm{Hz}$.
- id: c
  content: |-
    $130$
  correct: true
  feedback: |-
    The hanging mass sets $T$, the wire mass sets $\mu$, and $f_3=\dfrac{3}{2L}\sqrt{T/\mu}=129.156\ldots\ \mathrm{Hz}$. At two significant figures in a number-only field, enter $130$.
- id: d
  content: |-
    $260$
  feedback: |-
    A wire fixed at both ends uses $f_n=nv/(2L)$ because its fundamental contains half a wavelength. Omitting the $2$ doubles the correct value from about $130\ \mathrm{Hz}$ to about $260\ \mathrm{Hz}$.
- id: e
  content: |-
    $390$
  feedback: |-
    $390$ is about $3(130)$, so it treats the already computed third harmonic as though it were the fundamental and multiplies by $3$ again. The single factor $n=3$ gives the entry $130$.
```

---

<a id="summary"></a>
## Summary

For a fixed-end wire tensioned by a stationary hanging mass:

1. Read $L$ and $M$ from the diagram and $m_w$ from the prompt.
2. Compute $T=Mg$ and $\mu=m_w/L$.
3. Compute $v=\sqrt{T/\mu}$, then use $f_n=nv/(2L)$ with the requested harmonic number.
4. Check that the units reduce to hertz and that $f_n=nf_1$.
5. Keep unrounded intermediate values, then round the final frequency and follow the requested answer format.

The main trap is using the wrong mass: $M$ determines tension, while $m_w$ determines linear density.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Matching Fundamental Frequencies of Open and Closed Tubes](../../2026-07-31-HW-8/Lessons/Problem-2.md)

Study guide index: 23/28

---
<!-- lesson-nav:end -->
