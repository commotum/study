# Calculating the Frequency of a Simple Pendulum

<!--
lesson-id: 212-M4-011
topic-code: MTH212.M4.11
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Frequency Formula and Relevant Data](#choose-the-frequency-formula-and-relevant-data)
- [Substitute Length and Track the Units](#substitute-length-and-track-the-units)
- [Distinguish Frequency, Period, and Angular Frequency](#distinguish-frequency-period-and-angular-frequency)
- [Apply the Procedure to the Given Pendulum](#apply-the-procedure-to-the-given-pendulum)
- [Summary](#summary)

## Prerequisites

- Evaluate a square root with a calculator.
- Use order of operations in a formula.
- Recognize that \(1\ \mathrm{Hz}=1\ \mathrm{s^{-1}}\).

---

<a id="introduction"></a>
## Introduction

When a problem gives a **simple pendulum**, specifies the **small-angle approximation**, and asks for **frequency**, use

$$
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
$$

Here \(L\) is the pendulum length and \(g\) is gravitational acceleration. The bob's mass and the release angle do not appear in this small-angle frequency formula.

The reusable move is to select \(L\), substitute \(g=9.81\ \mathrm{m/s^2}\), evaluate the entire expression, and round only the final result.

**Recognition cue:** The requested unit identifies the output. Hertz means ordinary frequency \(f\); seconds means period \(T\); radians per second means angular frequency \(\omega\).

---

<a id="choose-the-frequency-formula-and-relevant-data"></a>
## Choose the Frequency Formula and Relevant Data

**Example:** A simple pendulum of length \(0.40\ \mathrm{m}\) has bob mass \(0.020\ \mathrm{kg}\) and is released from a small angle. Which given quantities determine its frequency?

**Explanation**

Under the small-angle approximation,

$$
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
$$

Only \(L\) and \(g\) enter the formula. The bob mass does not affect the frequency, and the small release angle establishes that the approximation may be used rather than becoming a substituted variable.

```quiz
type: radio
id: problem-2-formula-q1
content: |-
  Which formula gives the frequency of a simple pendulum under the small-angle approximation?
options:
- id: a
  content: |-
    \(f=2\pi\sqrt{\dfrac{L}{g}}\)
  feedback: |-
    This is the period formula \(T=2\pi\sqrt{L/g}\), not the frequency formula.
- id: b
  content: |-
    \(f=\dfrac{1}{2\pi}\sqrt{\dfrac{g}{L}}\)
  correct: true
  feedback: |-
    Simple-pendulum frequency depends on \(g\) and \(L\): \(f=(1/2\pi)\sqrt{g/L}\).
- id: c
  content: |-
    \(f=\dfrac{1}{2\pi}\sqrt{\dfrac{L}{g}}\)
  feedback: |-
    The ratio inside the square root is inverted; this expression also does not have units of frequency.
- id: d
  content: |-
    \(f=\dfrac{1}{2\pi}\sqrt{\dfrac{mg}{L}}\)
  feedback: |-
    The bob mass cancels from the small-angle pendulum equation.
- id: e
  content: |-
    \(f=\dfrac{1}{2\pi}\sqrt{\dfrac{g\theta}{L}}\)
  feedback: |-
    The small release angle is a condition for the approximation, not an input to this formula.
```

---

<a id="substitute-length-and-track-the-units"></a>
## Substitute Length and Track the Units

**Example:** Find the frequency of a simple pendulum with \(L=0.40\ \mathrm{m}\).

**Explanation**

Substitute the length into the frequency formula:

$$
\begin{aligned}
f
&=\frac{1}{2\pi}\sqrt{\frac{g}{L}}\\
&=\frac{1}{2\pi}
\sqrt{\frac{9.81\ \mathrm{m/s^2}}{0.40\ \mathrm{m}}}\\
&=\frac{1}{2\pi}\sqrt{24.525\ \mathrm{s^{-2}}}\\
&=0.7881\ldots\ \mathrm{s^{-1}}\\
&\approx 0.79\ \mathrm{Hz}.
\end{aligned}
$$

The meter units cancel under the radical. Taking the square root of \(\mathrm{s^{-2}}\) gives \(\mathrm{s^{-1}}\), which is hertz.

Enter the formula with explicit grouping:

$$
\frac{\sqrt{9.81/0.40}}{2\pi}.
$$

Evaluate the ratio under the square root first, then the square root, then divide by \(2\pi\). Do not move the \(2\pi\) factor under the radical.

```quiz
type: radio
id: problem-2-substitution-q1
content: |-
  Using \(g=9.81\ \mathrm{m/s^2}\), what is the frequency of a simple pendulum with \(L=0.80\ \mathrm{m}\), rounded to two significant figures?
options:
- id: a
  content: |-
    \(0.56\ \mathrm{Hz}\)
  correct: true
  feedback: |-
    \(f=(1/2\pi)\sqrt{9.81/0.80}=0.5573\ldots\ \mathrm{Hz}\), which rounds to \(0.56\ \mathrm{Hz}\).
- id: b
  content: |-
    \(3.5\ \mathrm{Hz}\)
  feedback: |-
    This is approximately \(\sqrt{g/L}\); the factor \(1/(2\pi)\) is still required.
- id: c
  content: |-
    \(1.8\ \mathrm{Hz}\)
  feedback: |-
    \(1.8\) is approximately the period in seconds, not the frequency in hertz.
- id: d
  content: |-
    \(0.080\ \mathrm{Hz}\)
  feedback: |-
    The length belongs inside the ratio \(g/L\); it is not a separate multiplier.
```

---

<a id="distinguish-frequency-period-and-angular-frequency"></a>
## Distinguish Frequency, Period, and Angular Frequency

**Example:** For \(L=0.60\ \mathrm{m}\), identify the pendulum's angular frequency, ordinary frequency, and period.

**Explanation**

These three quantities are related but are not interchangeable:

$$
\omega=\sqrt{\frac{g}{L}},
\qquad
f=\frac{\omega}{2\pi},
\qquad
T=\frac{1}{f}.
$$

| Quantity | Formula | Unit |
|---|---|---|
| Angular frequency | \(\omega=\sqrt{g/L}\) | \(\mathrm{rad/s}\) |
| Ordinary frequency | \(f=\omega/(2\pi)\) | \(\mathrm{Hz}\) |
| Period | \(T=1/f\) | \(\mathrm{s}\) |

For this pendulum,

$$
\omega=4.0435\ldots\ \mathrm{rad/s},
$$

so

$$
f=\frac{4.0435\ldots}{2\pi}
=0.6435\ldots\ \mathrm{Hz},
\qquad
T=1.5538\ldots\ \mathrm{s}.
$$

If the question asks for frequency in hertz, report \(f\), not \(\omega\) or \(T\).

```quiz
type: radio
id: problem-2-output-q1
content: |-
  A small-angle pendulum with \(L=0.47\ \mathrm{m}\) gives \(\sqrt{g/L}=4.5686\ldots\ \mathrm{s^{-1}}\). What frequency should be reported to two significant figures?
options:
- id: a
  content: |-
    \(4.6\ \mathrm{Hz}\)
  feedback: |-
    \(4.5686\ldots\) is the angular-frequency factor \(\sqrt{g/L}\); divide by \(2\pi\).
- id: b
  content: |-
    \(0.73\ \mathrm{Hz}\)
  correct: true
  feedback: |-
    \(f=4.5686\ldots/(2\pi)=0.7271\ldots\ \mathrm{Hz}\), which rounds to \(0.73\ \mathrm{Hz}\).
- id: c
  content: |-
    \(1.4\ \mathrm{Hz}\)
  feedback: |-
    \(1.4\) is approximately the period in seconds, not the frequency in hertz.
- id: d
  content: |-
    \(0.7271\ \mathrm{Hz}\)
  feedback: |-
    This has not been rounded to the requested two significant figures.
```

---

<a id="apply-the-procedure-to-the-given-pendulum"></a>
## Apply the Procedure to the Given Pendulum

**Example:** For the pendulum shown below, sort the givens by their role before calculating.

![](<../Source/Images/simple-pendulum.png>)

**Explanation**

| Given | Role |
|---|---|
| \(L=0.35\ \mathrm{m}\) | Substitute into the formula |
| \(g=9.81\ \mathrm{m/s^2}\) | Substitute into the formula |
| \(m=0.026\ \mathrm{kg}\) | Does not affect simple-pendulum frequency |
| \(\theta=14^\circ\) | The problem directs us to use the small-angle approximation |

Now evaluate and keep extra digits until the end:

$$
\begin{aligned}
f
&=\frac{1}{2\pi}\sqrt{\frac{9.81\ \mathrm{m/s^2}}{0.35\ \mathrm{m}}}\\
&=0.8426\ldots\ \mathrm{Hz}\\
&=0.84\ \mathrm{Hz}
\quad\text{to two significant figures.}
\end{aligned}
$$

The unrounded value is kept through the calculation. Since the measured length \(0.35\ \mathrm{m}\) has two significant figures, round the final frequency—not an intermediate square root—to two significant figures.

```quiz
type: radio
id: m4-2lec-q1
content: |-
  **Question 1**

  A simple pendulum has length $0.35\ \mathrm{m}$ and bob mass $0.026\ \mathrm{kg}$. It is released from rest at an angle of $14^\circ$. Using the small-angle approximation, what is its frequency of oscillation?

  ![](<../Source/Images/simple-pendulum.png>)

  Enter the frequency in hertz as a number only:
options:
- id: a
  content: 0.84
  correct: true
  feedback: |-
    For a simple pendulum at small angle,

    $$
    f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
    $$

    Therefore,

    $$
    f=\frac{1}{2\pi}\sqrt{\frac{9.81\ \mathrm{m/s^2}}{0.35\ \mathrm{m}}}
    =0.8426\ldots\ \mathrm{Hz}.
    $$

    The measured length has two significant figures, so $f=0.84\ \mathrm{Hz}$. The bob's mass does not affect the frequency.
- id: b
  content: 5.3
  feedback: |-
    This is approximately \(\sqrt{g/L}\), the angular frequency. Divide by \(2\pi\) to obtain ordinary frequency.
- id: c
  content: 1.2
  feedback: |-
    This is approximately the period in seconds. Frequency is its reciprocal.
- id: d
  content: 0.13
  feedback: |-
    This results from applying an extra factor of \(2\pi\). Use \(f=\sqrt{g/L}/(2\pi)\) once.
- id: e
  content: 0.026
  feedback: |-
    This is the bob's mass. Mass does not enter the small-angle simple-pendulum frequency formula.
```

---

<a id="summary"></a>
## Summary

For a simple pendulum under the small-angle approximation:

1. Use \(f=(1/2\pi)\sqrt{g/L}\).
2. Substitute the length \(L\); do not insert the bob mass or angle.
3. Group and evaluate \(g/L\), take the square root, then divide by \(2\pi\).
4. Check for \(\mathrm{s^{-1}}=\mathrm{Hz}\), keep guard digits, and round only the final frequency.

**Main trap:** \(2\pi\sqrt{L/g}\) gives the period \(T\), while \(\sqrt{g/L}\) gives angular frequency \(\omega\). The requested frequency is \(f=\omega/(2\pi)=1/T\).

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
