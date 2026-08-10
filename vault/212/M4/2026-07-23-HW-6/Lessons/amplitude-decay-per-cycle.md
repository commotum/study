# Calculating Amplitude Decay per Cycle

<!--
lesson-id: 212-M4-032
topic-code: MTH212.M4.32
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert the Loss to a Retention Factor](#convert-the-loss-to-a-retention-factor)
- [Apply the Factor Once per Cycle](#apply-the-factor-once-per-cycle)
- [Avoid the Linear-Decay Trap](#avoid-the-linear-decay-trap)
- [Evaluate and Round the Amplitude](#evaluate-and-round-the-amplitude)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Convert a percentage to a decimal.
- Interpret an exponent as repeated multiplication.
- Evaluate a power while keeping guard digits.
- Round a measured result to an appropriate number of significant figures.

---

<a id="introduction"></a>
## Introduction

When an oscillator **loses the same percentage of its amplitude during each cycle**, each cycle keeps the same fraction of the amplitude from the cycle before it. That makes the decay multiplicative rather than linear.

If the fractional loss per cycle is $p$, then the fraction retained per cycle is

$$
r=1-p.
$$

Starting from amplitude $A_0$, after $n$ cycles the amplitude is

$$
\boxed{A(n)=A_0(1-p)^n=A_0r^n}.
$$

The parts of this model have distinct roles:

- $A_0$ is the initial amplitude.
- $p$ is the decimal loss rate per cycle.
- $r=1-p$ is the decay factor, with $0<r<1$ for genuine decay.
- $n$ is the number of completed cycles.
- $A(n)$ is the amplitude remaining after those cycles.

The recognition cues are a **percentage loss per cycle** and a request for the amplitude **after a number of cycles**. Convert the percentage loss to a decimal, subtract it from $1$, raise the retained fraction to the number of cycles, and multiply by the initial amplitude.

A reliable workflow is to write the model $A(n)$ first and only then substitute the requested cycle count. This keeps the initial amplitude out of the exponent and makes the meaning of every number visible.

---

<a id="convert-the-loss-to-a-retention-factor"></a>
## Convert the Loss to a Retention Factor

**Example:** An oscillator loses $5.0\%$ of its amplitude during each cycle. Find the factor that multiplies its amplitude from one cycle to the next.

**Explanation**

First convert the loss percentage to a decimal:

$$
p=\frac{5.0}{100}=0.050.
$$

The oscillator loses $0.050$ of its current amplitude, so it retains

$$
r=1-p=1-0.050=0.950.
$$

Thus every completed cycle multiplies the current amplitude by $0.950$. The loss fraction $0.050$ is not the multiplier that remains.

```quiz
type: radio
id: amplitude-decay-retention-factor
shuffle: true
content: |-
  An oscillator loses $8.0\%$ of its amplitude during each cycle. What is its amplitude-retention factor per cycle?
options:
- id: retain-0920
  content: |-
    $0.920$
  correct: true
  feedback: |-
    A percentage loss must be subtracted from the whole. Since $8.0\%=0.080$, the retained fraction is $1-0.080=0.920$, so each cycle multiplies the current amplitude by $0.920$.
- id: lose-0080
  content: |-
    $0.080$
  feedback: |-
    The decimal $0.080$ is the fraction lost during a cycle, not the fraction that remains. Subtract it from $1$ to obtain the retention factor $0.920$.
- id: growth-1080
  content: |-
    $1.080$
  feedback: |-
    A factor greater than $1$ represents growth. Because the amplitude loses $8.0\%$, the correct multiplier is $1-0.080=0.920$, not $1+0.080$.
- id: retain-0800
  content: |-
    $0.800$
  feedback: |-
    This treats $8.0\%$ as $0.20$ lost. Dividing by $100$ gives $0.080$, so the retained fraction is $0.920$.
- id: retain-0992
  content: |-
    $0.992$
  feedback: |-
    This effectively converts $8.0\%$ to $0.008$. The correct decimal conversion is $8.0/100=0.080$, which leaves the factor $0.920$.
```

---

<a id="apply-the-factor-once-per-cycle"></a>
## Apply the Factor Once per Cycle

**Example:** An oscillator starts with amplitude $0.40\ \mathrm m$ and loses $5.0\%$ per cycle. Write and evaluate its amplitude after $4$ cycles.

**Explanation**

The retention factor is $1-0.050=0.950$. Apply that factor once for every completed cycle:

$$
\begin{aligned}
A(1)&=(0.40\ \mathrm m)(0.950),\\
A(2)&=(0.40\ \mathrm m)(0.950)(0.950)
     =(0.40\ \mathrm m)(0.950)^2,\\
A(3)&=(0.40\ \mathrm m)(0.950)^3.
\end{aligned}
$$

The pattern compresses one repeated factor per cycle into the exponent. Therefore,

$$
\begin{aligned}
A(4)
&=(0.40\ \mathrm m)(0.950)^4\\
&=0.3258\ldots\ \mathrm m.
\end{aligned}
$$

The exponent is the cycle count because $(0.950)^4$ means four successive multiplications by the same retention factor. The units come from $A_0$; the retention factor and cycle count are dimensionless.

Two quick checks support the model: $A(0)=A_0$, and a base between $0$ and $1$ makes $A(n)$ decrease as $n$ increases.

```quiz
type: radio
id: amplitude-decay-cycle-exponent
shuffle: true
content: |-
  An oscillator has initial amplitude $A_0$ and loses $6.0\%$ of its amplitude per cycle. Which expression gives its amplitude after $12$ cycles?
options:
- id: a0-times-094-power-12
  content: |-
    $A_0(0.940)^{12}$
  correct: true
  feedback: |-
    A $6.0\%$ loss leaves the factor $1-0.060=0.940$ each cycle. Applying that same factor through $12$ cycles gives $A_{12}=A_0(0.940)^{12}$.
- id: a0-times-006-power-12
  content: |-
    $A_0(0.060)^{12}$
  feedback: |-
    The number $0.060$ is the fraction lost, not the fraction retained. The repeated multiplier is $0.940$, so the power must be applied to $0.940$.
- id: a0-times-106-power-12
  content: |-
    $A_0(1.060)^{12}$
  feedback: |-
    The factor $1.060$ models $6.0\%$ growth per cycle. A loss requires subtraction from $1$, giving the factor $0.940$.
- id: a0-times-094-times-12
  content: |-
    $A_0(0.940)(12)$
  feedback: |-
    Multiplying by $12$ does not repeat the decay operation. One factor of $0.940$ is needed for each cycle, which is represented by $(0.940)^{12}$.
- id: a0-times-one-minus-12p
  content: |-
    $A_0(1-12(0.060))$
  feedback: |-
    This subtracts the same fraction of the initial amplitude in every cycle. Percentage decay instead removes $6.0\%$ of the current amplitude, so the changes compound as $A_0(0.940)^{12}$.
```

---

<a id="avoid-the-linear-decay-trap"></a>
## Avoid the Linear-Decay Trap

**Example:** An oscillator begins at $1.00\ \mathrm m$ and loses $10\%$ of its amplitude per cycle. Compare the correct amplitude after two cycles with a linear subtraction.

**Explanation**

After the first cycle, the amplitude is

$$
A_1=(1.00)(0.90)=0.90\ \mathrm m.
$$

The second cycle loses $10\%$ of the new amplitude, not $10\%$ of the original amplitude:

$$
A_2=(0.90)(0.90)=1.00(0.90)^2=0.81\ \mathrm m.
$$

Subtracting $0.10\ \mathrm m$ twice would give $0.80\ \mathrm m$, but that is a fixed amount lost per cycle. The stated process is a fixed percentage lost per cycle, so the amount removed becomes smaller as the amplitude decreases.

```quiz
type: radio
id: amplitude-decay-not-linear
shuffle: true
content: |-
  An oscillator starts with amplitude $0.50\ \mathrm m$ and loses $20\%$ of its amplitude per cycle. What is its amplitude after $2$ cycles?
options:
- id: amplitude-032
  content: |-
    $0.32\ \mathrm m$
  correct: true
  feedback: |-
    A $20\%$ loss leaves $0.80$ of the current amplitude each cycle. Therefore $A_2=(0.50)(0.80)^2=0.32\ \mathrm m$.
- id: amplitude-030
  content: |-
    $0.30\ \mathrm m$
  feedback: |-
    This subtracts $0.10\ \mathrm m$, which is $20\%$ of the initial amplitude, in both cycles. The second loss is instead $20\%$ of the reduced amplitude, so repeated multiplication gives $0.32\ \mathrm m$.
- id: amplitude-002
  content: |-
    $0.02\ \mathrm m$
  feedback: |-
    This uses the loss fraction as the repeated multiplier: $(0.50)(0.20)^2$. The oscillator retains $0.80$ per cycle, so the correct multiplier is $0.80^2$.
- id: amplitude-048
  content: |-
    $0.48\ \mathrm m$
  feedback: |-
    Subtracting $0.20^2=0.04$ from the initial amplitude does not model successive percentage changes. Apply the retained fraction twice: $(0.50)(0.80)^2=0.32\ \mathrm m$.
- id: amplitude-072
  content: |-
    $0.72\ \mathrm m$
  feedback: |-
    This value is larger than the initial $0.50\ \mathrm m$, so it cannot result from amplitude loss. A retention factor below $1$ must reduce the amplitude to $0.32\ \mathrm m$.
```

---

<a id="evaluate-and-round-the-amplitude"></a>
## Evaluate and Round the Amplitude

**Example:** An oscillator begins with amplitude $0.40\ \mathrm m$ and loses $2.0\%$ per cycle. Find its amplitude after $25$ cycles and report it to two significant figures.

**Explanation**

Keep the full calculator value until the last step:

$$
\begin{aligned}
A_{25}
&=(0.40\ \mathrm m)(1-0.020)^{25}\\
&=(0.40\ \mathrm m)(0.980)^{25}\\
&=0.2413\ldots\ \mathrm m.
\end{aligned}
$$

Rounded to two significant figures,

$$
\boxed{A_{25}=0.24\ \mathrm m}.
$$

Do not round the retention factor more coarsely than the stated percentage before raising it to a large power. Repeated multiplication can magnify premature rounding error.

```quiz
type: radio
id: amplitude-decay-rounding
shuffle: true
content: |-
  An oscillator starts with amplitude $0.60\ \mathrm m$ and loses $4.0\%$ per cycle. What is its amplitude after $20$ cycles, reported to two significant figures?
options:
- id: rounded-027
  content: |-
    $0.27\ \mathrm m$
  correct: true
  feedback: |-
    The retained factor is $0.960$, so $A_{20}=(0.60)(0.960)^{20}=0.2652\ldots\ \mathrm m$. Rounding once at the end to two significant figures gives $0.27\ \mathrm m$.
- id: truncated-026
  content: |-
    $0.26\ \mathrm m$
  feedback: |-
    The unrounded value is $0.2652\ldots\ \mathrm m$. The next digit is $5$, so two-significant-figure rounding raises the hundredths digit and gives $0.27\ \mathrm m$ rather than truncating to $0.26\ \mathrm m$.
- id: unrounded-02652
  content: |-
    $0.2652\ \mathrm m$
  feedback: |-
    This retains more precision than the two-significant-figure answer form requests. The calculation is useful as a guard-digit value, but the reported result is $0.27\ \mathrm m$.
- id: linear-012
  content: |-
    $0.12\ \mathrm m$
  feedback: |-
    This applies the total $80\%$ loss linearly as $1-20(0.040)$. Each cycle instead retains $0.960$ of the current amplitude, producing $0.2652\ldots\ \mathrm m$ before rounding.
- id: loss-factor-near-zero
  content: |-
    Approximately $0\ \mathrm m$
  feedback: |-
    This results from repeatedly multiplying by the lost fraction $0.040$. The oscillator retains $0.960$ each cycle, so a substantial amplitude, $0.27\ \mathrm m$, remains after $20$ cycles.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the original one-blank numerical problem before checking the choices.

**Explanation**

> **Question 1**
>
> A lightly damped oscillator loses $3.0\%$ of its amplitude during each cycle. If its initial amplitude is $0.25\ \mathrm m$, what is the amplitude after $30$ cycles? Enter meters: ______

The source asks for one numerical entry in meters. Use $p=0.030$, retain the factor $0.970$ per cycle, keep guard digits through the power, and then report the result to the two significant figures supported by the givens.

Map the givens into the decay model before evaluating:

$$
A_0=0.25\ \mathrm m,\qquad
p=0.030,\qquad
r=1-p=0.970,\qquad
n=30.
$$

Thus the model is $A(n)=(0.25\ \mathrm m)(0.970)^n$, and the requested quantity is its output at $n=30$.

```quiz
type: radio
id: khadley-damping-q1
shuffle: true
content: |-
  Which value belongs in the original problem's “Enter meters” blank?
options:
- id: original-010
  content: |-
    $0.10$
  correct: true
  feedback: |-
    Each cycle retains $1-0.030=0.970$ of the current amplitude. Thus $A_{30}=(0.25)(0.970)^{30}=0.1003\ldots\ \mathrm m$, which rounds to the requested entry $0.10$.
- id: original-01003
  content: |-
    $0.1003$
  feedback: |-
    This is a useful guard-digit value, but it reports more precision than the $3.0\%$ and $0.25\ \mathrm m$ givens support. Rounded to two significant figures, the blank should contain $0.10$.
- id: original-0025
  content: |-
    $0.025$
  feedback: |-
    This subtracts a total of $30(3.0\%)=90\%$ from the initial amplitude as though the same fixed amount were lost each cycle. The loss is a percentage of the current amplitude, so it compounds to $0.1003\ldots\ \mathrm m$.
- id: original-024
  content: |-
    $0.24$
  feedback: |-
    This applies the $0.970$ retention factor only once. The oscillator completes $30$ cycles, so the factor must be raised to the $30$th power.
- id: original-near-zero
  content: |-
    Approximately $0$
  feedback: |-
    This follows from using the lost fraction $0.030$ as the repeated multiplier. The oscillator retains $0.970$ each cycle, leaving $0.10\ \mathrm m$ to two significant figures after $30$ cycles.
```

---

<a id="summary"></a>
## Summary

When an oscillator loses the same percentage of its amplitude during every cycle:

1. Convert the percentage loss to a decimal fraction $p$.
2. Find the retained fraction $r=1-p$.
3. Check that $0<r<1$ for a decay model.
4. Write the model, then evaluate it at the requested cycle count:
   $$
   A(n)=A_0r^n=A_0(1-p)^n.
   $$
5. Keep guard digits while evaluating the power.
6. Round once at the end and include the amplitude unit.

The main traps are treating repeated percentage loss as linear subtraction, using the loss rate $p$ as the base, or raising the initial amplitude instead of the retention factor. A constant percentage is taken from the current amplitude each cycle, so the decay compounds exponentially.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
