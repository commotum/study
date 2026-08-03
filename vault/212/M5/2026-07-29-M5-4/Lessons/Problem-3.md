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
    Correct. The hanging mass gives $T=Mg$, while the wire mass divided by length gives $\mu=m_w/L$.
- id: b
  content: |-
    $T=3.0\ \mathrm{N}$ and $\mu=0.0050\ \mathrm{kg/m}$
  feedback: |-
    The hanging mass is not itself the tension; multiply it by $g$.
- id: c
  content: |-
    $T=29.4\ \mathrm{N}$ and $\mu=0.020\ \mathrm{kg/m}$
  feedback: |-
    Linear mass density is wire mass divided by wire length, not their product.
- id: d
  content: |-
    $T=0.098\ \mathrm{N}$ and $\mu=1.5\ \mathrm{kg/m}$
  feedback: |-
    Both quantities use the wrong mass-length relationship.
- id: e
  content: |-
    $T=29.4\ \mathrm{N}$ and $\mu=1.5\ \mathrm{kg/m}$
  feedback: |-
    The tension is right, but $\mu$ must use the wire's mass, not the hanging mass.
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
    This is the fundamental frequency; the requested third harmonic needs the factor $3$.
- id: b
  content: |-
    $31.3\ \mathrm{Hz}$
  feedback: |-
    This introduces an extra factor of $2$ in the denominator.
- id: c
  content: |-
    $62.5\ \mathrm{Hz}$
  correct: true
  feedback: |-
    Correct. Here $v=100\ \mathrm{m/s}$, so $f_3=3v/(2L)=62.5\ \mathrm{Hz}$.
- id: d
  content: |-
    $125\ \mathrm{Hz}$
  feedback: |-
    This omits the factor $2$ in the fixed-end formula's denominator.
- id: e
  content: |-
    $6.25\ \mathrm{Hz}$
  feedback: |-
    This is smaller by a factor of $10$; recheck the decimal placement after substitution.
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
    Dividing the fundamental by $3$ moves in the wrong direction.
- id: b
  content: |-
    $42\ \mathrm{Hz}$
  feedback: |-
    This is still the fundamental frequency, so the harmonic factor was omitted.
- id: c
  content: |-
    $84\ \mathrm{Hz}$
  feedback: |-
    This is the second harmonic, not the third.
- id: d
  content: |-
    $126\ \mathrm{Hz}$
  correct: true
  feedback: |-
    Correct. For the same wire, $f_3=3f_1=3(42\ \mathrm{Hz})$.
- id: e
  content: |-
    $378\ \mathrm{Hz}$
  feedback: |-
    This multiplies by the harmonic number twice.
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
    This is the fundamental frequency; the factor $n=3$ was omitted.
- id: b
  content: |-
    $80$
  feedback: |-
    This is close to the tension in newtons, not the frequency in hertz.
- id: c
  content: |-
    $130$
  correct: true
  feedback: |-
    Correct. The unrounded result is $129.156\ldots\ \mathrm{Hz}$, which becomes the number-only entry $130$ at two significant figures.
- id: d
  content: |-
    $260$
  feedback: |-
    This omits the factor $2$ in the denominator of $f_n=nv/(2L)$.
- id: e
  content: |-
    $390$
  feedback: |-
    This applies the third-harmonic factor twice.
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

Study guide index: 16/20

---

<!-- lesson-nav:end -->
