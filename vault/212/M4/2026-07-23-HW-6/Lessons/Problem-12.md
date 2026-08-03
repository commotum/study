# Period of an Ideal Simple Pendulum

<!--
lesson-id: 212-M4-027
topic-code: MTH212.M4.27
-->

## Table of Contents

- [Introduction](#introduction)
- [Compute the Period from Length](#compute-the-period-from-length)
- [Use Only the Quantities Kept by the Model](#use-only-the-quantities-kept-by-the-model)
- [Match the Period to a Time Range](#match-the-period-to-a-time-range)
- [Summary](#summary)

## Prerequisites

- Substitute values into a formula.
- Evaluate a square root.
- Recognize that $\sqrt{\mathrm{s}^2}=\mathrm{s}$.

---

<a id="introduction"></a>
## Introduction

When a pendulum is modeled as a **simple pendulum**, its cable is treated as massless and its bob as a point mass. For small oscillations, the period is

$$
T=2\pi\sqrt{\frac{L}{g}},
$$

where $L$ is the pendulum length and $g$ is gravitational acceleration.

The recognition cue is the phrase *modeled as a simple pendulum*. Under that model, compute the period from $L$ and $g$ only. Extra information about the cable mass, bob mass, or bob radius does not enter the formula.

Use this three-part procedure:

1. **Filter:** keep $L$ and $g$; discard the mass and size data excluded by the model.
2. **Substitute:** evaluate $2\pi\sqrt{L/g}$, including the factor $2\pi$.
3. **Classify:** compare the decimal period with the endpoints of the requested range.

---

<a id="compute-the-period-from-length"></a>
## Compute the Period from Length

**Example:** Find the period of an ideal simple pendulum with $L=9.81\ \mathrm{m}$ and $g=9.81\ \mathrm{m/s^2}$.

**Explanation**

Substitute the length and gravitational acceleration:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{9.81\ \mathrm{m}}{9.81\ \mathrm{m/s^2}}}\\
&=2\pi\sqrt{1\ \mathrm{s^2}}\\
&=2\pi(1.000\ \mathrm{s})\\
&\approx 6.28\ \mathrm{s}.
\end{aligned}
$$

The ratio $L/g$ has units of $\mathrm{s^2}$, so its square root has units of seconds.

```quiz
type: radio
id: p12-q1
content: |-
  An ideal simple pendulum has $L=19.62\ \mathrm{m}$. Using $g=9.81\ \mathrm{m/s^2}$, what is its period?
options:
- id: p12-q1-a
  content: |-
    $1.41\ \mathrm{s}$
  feedback: |-
    This is only $\sqrt{L/g}$; the factor $2\pi$ is still needed.
- id: p12-q1-b
  content: |-
    $6.28\ \mathrm{s}$
- id: p12-q1-c
  content: |-
    $8.89\ \mathrm{s}$
  correct: true
- id: p12-q1-d
  content: |-
    $12.57\ \mathrm{s}$
  feedback: |-
    This uses $L/g=2$ without taking its square root.
- id: p12-q1-e
  content: |-
    $19.62\ \mathrm{s}$
  feedback: |-
    The length is an input to the period formula, not the period itself.
```

---

<a id="use-only-the-quantities-kept-by-the-model"></a>
## Use Only the Quantities Kept by the Model

**Example:** A pendulum has a $12\ \mathrm{m}$ cable of mass $5\ \mathrm{kg}$ and a spherical bob of mass $50\ \mathrm{kg}$ and radius $0.4\ \mathrm{m}$. It is modeled as a simple pendulum. Which data determine its ideal period?

**Explanation**

The model replaces the real cable by a massless cable and the real bob by a point mass. Sort the data before substituting:

- Keep $L=12\ \mathrm{m}$ and the local value of $g$.
- Discard the cable mass, bob mass, and bob radius.

The setup is therefore

$$
T=2\pi\sqrt{\frac{12\ \mathrm{m}}{g}}.
$$

The masses do not cancel out of a longer formula; they never enter this model's period formula.

```quiz
type: radio
id: p12-q2
content: |-
  A pendulum with cable length $L=20\ \mathrm{m}$ has cable mass $M=80\ \mathrm{kg}$ and a bob of mass $m=30\ \mathrm{kg}$ and radius $r=0.6\ \mathrm{m}$. It is modeled as a simple pendulum. Which setup gives its period?
options:
- id: p12-q2-a
  content: |-
    $T=2\pi\sqrt{\dfrac{20}{9.81}}$
  correct: true
- id: p12-q2-b
  content: |-
    $T=2\pi\sqrt{\dfrac{20+0.6}{9.81}}$
- id: p12-q2-c
  content: |-
    $T=2\pi\sqrt{\dfrac{20(30)}{9.81}}$
- id: p12-q2-d
  content: |-
    $T=2\pi\sqrt{\dfrac{20(80+30)}{9.81}}$
- id: p12-q2-e
  content: |-
    $T=2\pi\sqrt{\dfrac{30}{9.81}}$
```

---

<a id="match-the-period-to-a-time-range"></a>
## Match the Period to a Time Range

**Example:** The Oregon Convention Center pendulum has $L=27\ \mathrm{m}$, bob mass $m=100\ \mathrm{kg}$, bob radius $r=1.5\ \mathrm{m}$, and cable mass $M=400\ \mathrm{kg}$. If it is modeled as a simple pendulum, use $g=9.81\ \mathrm{m/s^2}$ to choose its period range.

**Explanation**

Keep $L$ and $g$ and discard the mass and radius data:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{27\ \mathrm{m}}{9.81\ \mathrm{m/s^2}}}\\
&\approx 2\pi(1.659\ \mathrm{s})\\
&\approx 10.42\ \mathrm{s}.
\end{aligned}
$$

Since $10<10.42<11$, the period is **about 10–11 seconds**. A result near $1.66\ \mathrm{s}$ means the factor $2\pi$ was omitted.

Equivalently, the computed value satisfies the requested interval condition

$$
10\ \mathrm{s}\leq T<11\ \mathrm{s}.
$$

```quiz
type: radio
id: p12-q3
content: |-
  A very long pendulum is modeled as a simple pendulum with $L=32\ \mathrm{m}$. Using $g=9.81\ \mathrm{m/s^2}$, which range contains its period?
options:
- id: p12-q3-a
  content: |-
    about 9–10 seconds
- id: p12-q3-b
  content: |-
    about 10–11 seconds
- id: p12-q3-c
  content: |-
    about 11–12 seconds
  correct: true
- id: p12-q3-d
  content: |-
    about 12–13 seconds
```

---

<a id="summary"></a>
## Summary

When the problem says to use the simple-pendulum model, remember **filter, substitute, classify**:

1. Keep only the pendulum length $L$ and gravitational acceleration $g$.
2. Compute $T=2\pi\sqrt{L/g}$.
3. Check that $\sqrt{L/g}$ has units of seconds and that the factor $2\pi$ is present.
4. Compare the decimal period with the endpoints of the requested time ranges.

Mass and bob radius are real physical details, but the stated ideal model excludes them.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
