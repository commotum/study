# Finding a Decay Constant from Period Counts

## Table of Contents

- [Introduction](#introduction)
- [Solve the Amplitude Ratio for the Decay Constant](#solve-the-amplitude-ratio-for-the-decay-constant)
- [Convert a Number of Periods into Time](#convert-a-number-of-periods-into-time)
- [Build the Full Pendulum Calculation](#build-the-full-pendulum-calculation)
- [Keep the Sign and the Factor of Two](#keep-the-sign-and-the-factor-of-two)
- [Summary](#summary)

## Prerequisites

- Form the dimensionless ratio $A(t)/A_0$.
- Use $\ln(e^x)=x$ and evaluate a natural logarithm.
- Compute a simple pendulum's period with $T=2\pi\sqrt{L/g}$.

---

<a id="introduction"></a>
## Introduction

The recognition cue is an amplitude measured after a stated number of oscillation periods, together with the model

$$
A(t)=A_0e^{-t/(2\tau)}.
$$

The unknown $\tau$ is inside an exponential, so first divide by $A_0$, then use a natural logarithm. If the time is given as a number of periods, convert it to seconds before solving.

Let

$$
R=\frac{A(t)}{A_0}.
$$

Then

$$
\begin{aligned}
R&=e^{-t/(2\tau)},\\
\ln R&=-\frac{t}{2\tau},\\
\tau&=-\frac{t}{2\ln R}.
\end{aligned}
$$

For a decaying amplitude, $0<R<1$, so $\ln R<0$. The two minus signs make $\tau$ positive.

Use this sequence:

1. **Find time:** compute $t=NT$ if the observation occurs after $N$ periods.
2. **Form the ratio:** write $R=A(t)/A_0$.
3. **Solve:** evaluate $\tau=-t/(2\ln R)$.

---

<a id="solve-the-amplitude-ratio-for-the-decay-constant"></a>
## Solve the Amplitude Ratio for the Decay Constant

**Example:** An oscillator's amplitude is half its initial value after $100\ \mathrm{s}$. Find $\tau$ for the model $A(t)=A_0e^{-t/(2\tau)}$.

**Explanation**

Here $R=1/2$ and $t=100\ \mathrm{s}$. Substitute these into the ratio form:

$$
\frac{1}{2}=e^{-100/(2\tau)}.
$$

Take the natural logarithm and solve:

$$
\begin{aligned}
\ln\left(\frac{1}{2}\right)&=-\frac{100}{2\tau},\\
\tau&=-\frac{100}{2\ln(1/2)}\\
&=\frac{100}{2\ln 2}\\
&\approx 72.1\ \mathrm{s}.
\end{aligned}
$$

The half-amplitude shortcut for this particular model is

$$
\boxed{\tau=\frac{t_{\text{half}}}{2\ln 2}}.
$$

```quiz
type: radio
id: p13-q1
content: |-
  For $A(t)=A_0e^{-t/(2\tau)}$, the amplitude is half its initial value after $60\ \mathrm{s}$. What is $\tau$?
options:
- id: p13-q1-a
  content: |-
    about $21.6\ \mathrm{s}$
- id: p13-q1-b
  content: |-
    about $43.3\ \mathrm{s}$
  correct: true
- id: p13-q1-c
  content: |-
    about $60.0\ \mathrm{s}$
- id: p13-q1-d
  content: |-
    about $86.6\ \mathrm{s}$
- id: p13-q1-e
  content: |-
    about $-43.3\ \mathrm{s}$
```

---

<a id="convert-a-number-of-periods-into-time"></a>
## Convert a Number of Periods into Time

**Example:** A pendulum has period $T=8.00\ \mathrm{s}$. Its amplitude is halved after $N=600$ periods. Find $\tau$.

**Explanation**

The exponent requires elapsed time, not a count of cycles. Convert first:

$$
t=NT=(600)(8.00\ \mathrm{s})=4800\ \mathrm{s}.
$$

Now use the half-amplitude formula:

$$
\begin{aligned}
\tau
&=\frac{NT}{2\ln 2}\\
&=\frac{4800\ \mathrm{s}}{2\ln 2}\\
&\approx 3.46\times 10^3\ \mathrm{s}.
\end{aligned}
$$

The period count $N$ has no units, so $NT$ and $\tau$ both have units of seconds.

```quiz
type: radio
id: p13-q2
content: |-
  A pendulum with period $T=5.00\ \mathrm{s}$ reaches half its initial amplitude after $400$ periods. What is its decay constant?
options:
- id: p13-q2-a
  content: |-
    about $290\ \mathrm{s}$
- id: p13-q2-b
  content: |-
    about $720\ \mathrm{s}$
- id: p13-q2-c
  content: |-
    about $1440\ \mathrm{s}$
  correct: true
- id: p13-q2-d
  content: |-
    about $2000\ \mathrm{s}$
- id: p13-q2-e
  content: |-
    about $2890\ \mathrm{s}$
```

---

<a id="build-the-full-pendulum-calculation"></a>
## Build the Full Pendulum Calculation

**Example:** A simple pendulum has length $L=19.62\ \mathrm{m}$. Using $g=9.81\ \mathrm{m/s^2}$, its amplitude is halved after $500$ periods. Find $\tau$.

**Explanation**

First compute one period:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{L}{g}}\\
&=2\pi\sqrt{\frac{19.62\ \mathrm{m}}{9.81\ \mathrm{m/s^2}}}\\
&\approx 8.89\ \mathrm{s}.
\end{aligned}
$$

Then combine the period count and the half-amplitude formula:

$$
\begin{aligned}
t&=NT=(500)(8.89\ \mathrm{s})\approx 4.44\times10^3\ \mathrm{s},\\
\tau&=\frac{t}{2\ln2}\approx 3.20\times10^3\ \mathrm{s}.
\end{aligned}
$$

For the assigned pendulum below, the simple-pendulum model uses $L=27\ \mathrm{m}$ and $g=9.81\ \mathrm{m/s^2}$. The cable mass, bob mass, and bob radius do not enter this ideal model's period formula.

```quiz
type: radio
id: p13-q3
content: |-
  In Portland at the Oregon Convention Center is one of the longest pendulums in the world (in terms of both cable length and oscillation period).

  It has a cable of length $L=27\ \mathrm{m}$ (about as tall as a building with 8 floors) and a spherical bob of mass $m=100\ \mathrm{kg}$ and radius $r=1.5\ \mathrm{m}$ attached to the end of the cable of mass $M=400\ \mathrm{kg}$.

  For this problem you can again model the pendulum as a simple pendulum but now experiencing a linear drag force.

  After 1,000 periods, it is found that the amplitude of the pendulum's motion has reached half of its initial value.

  What is the decay constant of the pendulum?

  Hint: The decay constant is the $\tau$ such that the time-dependent amplitude is $A(t)=A_0e^{-t/(2\tau)}$.
options:
- id: p13-q3-a
  content: |-
    about 5,500 seconds
- id: p13-q3-b
  content: |-
    about 7,500 seconds
  correct: true
- id: p13-q3-c
  content: |-
    about 11,000 seconds
- id: p13-q3-d
  content: |-
    about 15,000 seconds
```

For this pendulum,

$$
\begin{aligned}
T&=2\pi\sqrt{\frac{27}{9.81}}\approx 10.42\ \mathrm{s},\\
t&=(1000)T\approx 1.042\times10^4\ \mathrm{s},\\
\tau&=\frac{t}{2\ln2}\approx 7.52\times10^3\ \mathrm{s}.
\end{aligned}
$$

Thus the matching choice is **about 7,500 seconds**.

---

<a id="keep-the-sign-and-the-factor-of-two"></a>
## Keep the Sign and the Factor of Two

**Example:** The amplitude is $40\%$ of its initial value after $600\ \mathrm{s}$. Find $\tau$.

**Explanation**

Use the remaining fraction, $R=0.40$, rather than the fraction lost:

$$
\begin{aligned}
\tau
&=-\frac{600\ \mathrm{s}}{2\ln(0.40)}\\
&\approx 327\ \mathrm{s}.
\end{aligned}
$$

Two checks catch the main errors:

- Because $\ln(0.40)<0$, the leading minus sign is needed to make $\tau>0$.
- Because the model contains $2\tau$ in the denominator, the solved formula must contain the factor $2$.

```quiz
type: radio
id: p13-q4
content: |-
  An oscillator has $A(800\ \mathrm{s})=A_0/4$ and follows $A(t)=A_0e^{-t/(2\tau)}$. Which expression correctly gives $\tau$?
options:
- id: p13-q4-a
  content: |-
    $\tau=-\dfrac{800\ \mathrm{s}}{2\ln(1/4)}$
  correct: true
- id: p13-q4-b
  content: |-
    $\tau=-\dfrac{800\ \mathrm{s}}{\ln(1/4)}$
- id: p13-q4-c
  content: |-
    $\tau=\dfrac{800\ \mathrm{s}}{2\ln(1/4)}$
- id: p13-q4-d
  content: |-
    $\tau=-\dfrac{2(800\ \mathrm{s})}{\ln(1/4)}$
- id: p13-q4-e
  content: |-
    $\tau=-\dfrac{800\ \mathrm{s}}{2\ln(3/4)}$
```

---

<a id="summary"></a>
## Summary

When an amplitude ratio is reported after several periods:

1. Compute one period if needed: $T=2\pi\sqrt{L/g}$.
2. Convert the cycle count to time: $t=NT$.
3. Form the remaining-amplitude ratio: $R=A(t)/A_0$.
4. Solve

$$
\boxed{\tau=-\frac{t}{2\ln R}}.
$$

For half the initial amplitude, this becomes

$$
\boxed{\tau=\frac{NT}{2\ln2}}.
$$

The main trap is copying the familiar form $e^{-t/\tau}$ instead of reading the given exponent $e^{-t/(2\tau)}$. That mistake doubles the result.
