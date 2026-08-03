# Finding the First Constructive-Interference Point

<!--
lesson-id: 212-M5-040
topic-code: MTH212.M5.40
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Frequency to Wavelength](#convert-frequency-to-wavelength)
- [Write the Path Difference](#write-the-path-difference)
- [Choose the First Constructive Path Difference](#choose-the-first-constructive-path-difference)
- [Solve the Path-Difference Equation](#solve-the-path-difference-equation)
- [Apply the Full Procedure](#apply-the-full-procedure)
- [Summary](#summary)

## Prerequisites

- Use the wave relation $v=f\lambda$.
- Find a distance in the coordinate plane with the Pythagorean theorem.
- Solve a radical equation by isolating the square root, squaring, and checking the result.

---

<a id="introduction"></a>
## Introduction

When two in-phase sources emit the same frequency, a maximum occurs wherever their path difference is a whole-number multiple of the wavelength:

$$
\Delta r=m\lambda,\qquad m=0,1,2,\ldots
$$

For sources at $(0,0)$ and $(0,-d)$ and a listener at $(x,0)$ with $x>0$, the two path lengths are

$$
r_A=x,
\qquad
r_B=\sqrt{x^2+d^2},
$$

so

$$
\Delta r=r_B-r_A=\sqrt{x^2+d^2}-x.
$$

Here, let $x$ be the positive coordinate the problem asks us to find, and let $d$ be the fixed separation between the sources. The recognition cue is the phrase **in phase** together with a request for the **first maximum** along an axis. Convert frequency to wavelength, model the path difference, select the first reachable whole-number multiple of $\lambda$, and solve for $x$.

---

<a id="convert-frequency-to-wavelength"></a>
## Convert Frequency to Wavelength

**Example:** A sound wave travels at $343\ \mathrm{m/s}$ and has frequency $686\ \mathrm{Hz}$. Find its wavelength.

**Explanation**

Use $v=f\lambda$ and solve for $\lambda$:

$$
\lambda=\frac{v}{f}
=\frac{343\ \mathrm{m/s}}{686\ \mathrm{s^{-1}}}
=0.500\ \mathrm{m}.
$$

The speed is divided by the frequency. The product $vf$ does not have units of length.

```quiz
type: radio
id: problem-5-q1
content: |-
  A wave travels at $360\ \mathrm{m/s}$ and has frequency $800\ \mathrm{Hz}$. What is its wavelength?
options:
- id: problem-5-q1-a
  content: |-
    $0.45\ \mathrm{m}$
  correct: true
  feedback: |-
    $\lambda=v/f=360/800=0.45\ \mathrm{m}$.
- id: problem-5-q1-b
  content: |-
    $2.22\ \mathrm{m}$
  feedback: |-
    This reverses the ratio and computes $f/v$.
- id: problem-5-q1-c
  content: |-
    $1.25\ \mathrm{m}$
  feedback: |-
    This does not use $\lambda=v/f$.
- id: problem-5-q1-d
  content: |-
    $800\ \mathrm{m}$
  feedback: |-
    Frequency is not wavelength.
- id: problem-5-q1-e
  content: |-
    $288{,}000\ \mathrm{m}$
  feedback: |-
    This multiplies $v$ and $f$ instead of dividing.
```

---

<a id="write-the-path-difference"></a>
## Write the Path Difference

**Example:** Source A is at $(0,0)$, source B is at $(0,-3.0\ \mathrm{m})$, and the listener is at $(x,0)$ for $x>0$. Write the path difference.

**Explanation**

The route from A to the listener lies along the $x$-axis, so $r_A=x$. The route from B is the hypotenuse of a right triangle with legs $x$ and $3.0\ \mathrm{m}$:

$$
r_B=\sqrt{x^2+(3.0\ \mathrm{m})^2}.
$$

Because $r_B>r_A$,

$$
\Delta r=r_B-r_A=\sqrt{x^2+(3.0\ \mathrm{m})^2}-x.
$$

```quiz
type: radio
id: problem-5-q2
content: |-
  Source A is at $(0,0)$, source B is at $(0,-2.6\ \mathrm{m})$, and a listener is at $(x,0)$ with $x>0$. Which expression gives the path difference $\Delta r=r_B-r_A$?
options:
- id: problem-5-q2-a
  content: |-
    $\sqrt{x^2+(2.6\ \mathrm{m})^2}-x$
  correct: true
  feedback: |-
    The farther path is the hypotenuse; subtract the direct path $x$.
- id: problem-5-q2-b
  content: |-
    $\sqrt{x^2+(2.6\ \mathrm{m})^2}+x$
  feedback: |-
    This adds the path lengths instead of taking their difference.
- id: problem-5-q2-c
  content: |-
    $x-\sqrt{x^2+(2.6\ \mathrm{m})^2}$
  feedback: |-
    This reverses $r_B-r_A$ and gives a negative value.
- id: problem-5-q2-d
  content: |-
    $\sqrt{x^2+2.6\ \mathrm{m}}-x$
  feedback: |-
    Both legs must be squared inside the distance formula.
- id: problem-5-q2-e
  content: |-
    $2.6\ \mathrm{m}-x$
  feedback: |-
    The diagonal path from B must be found with the Pythagorean theorem.
```

---

<a id="choose-the-first-constructive-path-difference"></a>
## Choose the First Constructive Path Difference

**Example:** The source separation is $d=2.2\ \mathrm{m}$ and the wavelength is $0.500\ \mathrm{m}$. Which constructive path difference is encountered first as the listener moves right from the origin?

**Explanation**

At $x=0$, the path difference is $\Delta r=d=2.2\ \mathrm{m}=4.4\lambda$. As $x$ increases, $\Delta r=\sqrt{x^2+d^2}-x$ decreases. Therefore, the first constructive value reached is the next lower whole-number multiple:

$$
\Delta r=4\lambda=4(0.500\ \mathrm{m})=2.00\ \mathrm{m}.
$$

Using $5\lambda$ would require the path difference to increase from $4.4\lambda$, so that maximum is not reached on the positive $x$-axis.

If $d$ is already an integer multiple $n\lambda$, then $x=0$ is a maximum but is not on the positive $x$-axis. In that special case, the first maximum with $x>0$ uses the next lower order, $(n-1)\lambda$.

```quiz
type: radio
id: problem-5-q3
content: |-
  At $x=0$, two sources are separated by $1.85\ \mathrm{m}$. Their wavelength is $0.400\ \mathrm{m}$, and the path difference decreases as $x$ increases. What is the first constructive path difference reached for $x>0$?
options:
- id: problem-5-q3-a
  content: |-
    $1.60\ \mathrm{m}$
  correct: true
  feedback: |-
    Since $1.85/0.400=4.625$, the next lower integer order is $m=4$, giving $4\lambda=1.60\ \mathrm{m}$.
- id: problem-5-q3-b
  content: |-
    $2.00\ \mathrm{m}$
  feedback: |-
    This is $5\lambda$, which is above the starting path difference and cannot be reached as $\Delta r$ decreases.
- id: problem-5-q3-c
  content: |-
    $1.85\ \mathrm{m}$
  feedback: |-
    The source separation is the starting path difference, but it is not an integer multiple of $\lambda$.
- id: problem-5-q3-d
  content: |-
    $1.20\ \mathrm{m}$
  feedback: |-
    This is a later maximum at $3\lambda$, not the first one.
- id: problem-5-q3-e
  content: |-
    $0.400\ \mathrm{m}$
  feedback: |-
    This is $1\lambda$, a much later constructive point.
```

---

<a id="solve-the-path-difference-equation"></a>
## Solve the Path-Difference Equation

**Example:** Solve for $x>0$ when the source separation is $d=3.0\ \mathrm{m}$ and the required path difference is $L=2.5\ \mathrm{m}$.

**Explanation**

Set the geometric path difference equal to $L$:

$$
\sqrt{x^2+d^2}-x=L.
$$

Isolate the radical, square, and solve:

$$
\begin{aligned}
\sqrt{x^2+d^2}&=x+L,\\
x^2+d^2&=(x+L)^2,\\
d^2&=2Lx+L^2,\\
x&=\frac{d^2-L^2}{2L}.
\end{aligned}
$$

For a positive coordinate, the selected constructive path difference must satisfy $0<L<d$. Squaring can introduce an invalid root, so the computed value must also be checked in the original radical equation.

For $d=3.0\ \mathrm{m}$ and $L=2.5\ \mathrm{m}$,

$$
x=\frac{(3.0)^2-(2.5)^2}{2(2.5)}=0.55\ \mathrm{m}.
$$

Substitution gives $\sqrt{0.55^2+3.0^2}-0.55=2.50\ \mathrm{m}$, so the solution satisfies the original radical equation.

```quiz
type: radio
id: problem-5-q4
content: |-
  A geometry gives $d=2.6\ \mathrm{m}$ and a required path difference $L=2.4\ \mathrm{m}$. Solve $\sqrt{x^2+d^2}-x=L$ for $x>0$.
options:
- id: problem-5-q4-a
  content: |-
    $0.21\ \mathrm{m}$
  correct: true
  feedback: |-
    $x=(d^2-L^2)/(2L)=(2.6^2-2.4^2)/(4.8)=0.208\ldots\ \mathrm{m}$.
- id: problem-5-q4-b
  content: |-
    $0.42\ \mathrm{m}$
  feedback: |-
    This omits the factor of $2$ in the denominator.
- id: problem-5-q4-c
  content: |-
    $2.40\ \mathrm{m}$
  feedback: |-
    This reports the required path difference rather than the coordinate.
- id: problem-5-q4-d
  content: |-
    $0.20\ \mathrm{m}$
  feedback: |-
    This uses $d-L$ rather than solving the radical equation.
- id: problem-5-q4-e
  content: |-
    $2.81\ \mathrm{m}$
  feedback: |-
    This comes from adding rather than subtracting the squared lengths.
```

---

<a id="apply-the-full-procedure"></a>
## Apply the Full Procedure

**Example:** Two speakers are in phase and emit a $686\ \mathrm{Hz}$ tone. Speaker A is at the origin, and speaker B is at $(0,-2.2\ \mathrm{m})$. Where is the first point on the positive $x$-axis where you hear maximum sound intensity? Use $343\ \mathrm{m/s}$ for the speed of sound. Enter the $x$-coordinate in meters as a number only.

**Explanation**

First find the wavelength:

$$
\lambda=\frac{343\ \mathrm{m/s}}{686\ \mathrm{Hz}}=0.500\ \mathrm{m}.
$$

At $(x,0)$, the path difference is

$$
\Delta r=\sqrt{x^2+(2.2\ \mathrm{m})^2}-x.
$$

At the origin, $\Delta r=2.2\ \mathrm{m}=4.4\lambda$. Since the path difference decreases as $x$ increases, the first constructive value is

$$
L=4\lambda=2.00\ \mathrm{m}.
$$

Now solve:

$$
\begin{aligned}
\sqrt{x^2+2.2^2}-x&=2.0,\\
x&=\frac{2.2^2-2.0^2}{2(2.0)}\\
&=0.21\ \mathrm{m}.
\end{aligned}
$$

Checking in the original geometry,

$$
\sqrt{0.21^2+2.2^2}-0.21=1.999\ldots\ \mathrm{m}\approx2.00\ \mathrm{m}=4\lambda.
$$

Thus the requested number-only $x$-coordinate is $\boxed{0.21}$.

```quiz
type: radio
id: problem-5-q5
content: |-
  Two in-phase speakers are at $(0,0)$ and $(0,-2.6\ \mathrm{m})$. They emit a $680\ \mathrm{Hz}$ tone in air where the sound speed is $340\ \mathrm{m/s}$. What is the first positive $x$-coordinate where the intensity is maximum?
options:
- id: problem-5-q5-a
  content: |-
    $0.10\ \mathrm{m}$
  correct: true
  feedback: |-
    $\lambda=0.500\ \mathrm{m}$, the first order is $L=5\lambda=2.50\ \mathrm{m}$, and $x=(2.6^2-2.5^2)/(2\cdot2.5)=0.102\ \mathrm{m}$.
- id: problem-5-q5-b
  content: |-
    $0.05\ \mathrm{m}$
  feedback: |-
    This uses the gap $d-L$ as the coordinate.
- id: problem-5-q5-c
  content: |-
    $0.50\ \mathrm{m}$
  feedback: |-
    This reports the wavelength instead of solving for $x$.
- id: problem-5-q5-d
  content: |-
    $2.50\ \mathrm{m}$
  feedback: |-
    This reports the constructive path difference instead of the coordinate.
- id: problem-5-q5-e
  content: |-
    $0.55\ \mathrm{m}$
  feedback: |-
    This uses the wrong geometric values in the path-difference equation.
```

---

<a id="summary"></a>
## Summary

For two in-phase sources and a listener on the positive $x$-axis:

1. Compute $\lambda=v/f$.
2. Write $\Delta r=\sqrt{x^2+d^2}-x$.
3. Notice that $\Delta r$ starts at $d$ and decreases as $x$ increases.
4. Choose the largest integer order with $m\lambda<d$. Equivalently, use $m=\lfloor d/\lambda\rfloor$ unless $d/\lambda$ is an integer, in which case use one order lower.
5. Set $L=m\lambda$, solve $x=(d^2-L^2)/(2L)$, require $x>0$, and check the result in the original path-difference equation.

The main trap is choosing the next higher integer multiple of $\lambda$. That value cannot be reached because the path difference decreases as the listener moves right.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: End of Quiz 3 Study Guide.

Study guide index: 20/20

---

<!-- lesson-nav:end -->
