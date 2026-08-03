# Combining Path and Starting Phase Differences

<!--
lesson-id: 212-M5-039
topic-code: MTH212.M5.39
-->

## Table of Contents

- [Introduction](#introduction)
- [Measure the Path Difference](#measure-the-path-difference)
- [Convert Path Difference to Phase](#convert-path-difference-to-phase)
- [Include the Initial Phase Offset](#include-the-initial-phase-offset)
- [Match the Requested Phase Form](#match-the-requested-phase-form)
- [Complete the Two-Flute Calculation](#complete-the-two-flute-calculation)
- [Summary](#summary)

## Prerequisites

- Find the hypotenuse of a right triangle with the Pythagorean theorem.
- Use $\lambda=v/f$ and recognize that one cycle is $2\pi$ radians.
- Evaluate square roots while preserving extra calculator digits until the final answer.

---

<a id="introduction"></a>
## Introduction

When two coherent sources reach the same detector by different paths, two effects determine their phase difference:

1. the phase offset they had when they started, and
2. the phase accumulated because one wave traveled farther.

Choose one order and keep it throughout the calculation. Taking wave B relative to wave A,

$$
\Delta r=r_B-r_A
$$

and

$$
\Delta\phi
=\Delta\phi_0+\frac{2\pi f\Delta r}{v}.
$$

Use this calculation map:

| Quantity | Meaning | How to find it |
| --- | --- | --- |
| $r_A,r_B$ | source-to-detector path lengths | distance formula |
| $\Delta r$ | signed path difference | $r_B-r_A$ |
| $\Delta\phi_{\text{path}}$ | phase added by unequal paths | $2\pi f\Delta r/v$ |
| $\Delta\phi$ | total phase difference | $\Delta\phi_0+\Delta\phi_{\text{path}}$ |

The recognition cue is a problem that gives source locations, a detector location, frequency, wave speed, and an initial phase relationship. The task is to find both path lengths, subtract them in the chosen order, convert that distance difference to radians, and add the initial phase offset.

---

<a id="measure-the-path-difference"></a>
## Measure the Path Difference

**Example:** Source A is at $(-9,0)$, source B is at $(16,0)$, and the detector is at $(0,12)$. Find $\Delta r=r_B-r_A$.

**Explanation**

Each source and the detector form a right triangle. Because distances are always nonnegative,

$$
\begin{aligned}
r_A&=\sqrt{(-9-0)^2+(0-12)^2}=15,\\
r_B&=\sqrt{(16-0)^2+(0-12)^2}=20.
\end{aligned}
$$

Therefore,

$$
\Delta r=r_B-r_A=20-15=5.
$$

Do not subtract the source $x$-coordinates directly. The waves travel along the diagonal source-to-detector paths.

```quiz
type: radio
id: p4-path-difference
content: |-
  Source A is at $(-5,0)$, source B is at $(16,0)$, and a detector is at $(0,12)$. Using $\Delta r=r_B-r_A$, what is the path difference?
options:
- id: p4-path-a
  content: |-
    $7$
  correct: true
- id: p4-path-b
  content: |-
    $33$
- id: p4-path-c
  content: |-
    $-7$
- id: p4-path-d
  content: |-
    $21$
- id: p4-path-e
  content: |-
    $11$
```

---

<a id="convert-path-difference-to-phase"></a>
## Convert Path Difference to Phase

**Example:** A sound has frequency $343\ \mathrm{Hz}$, travels at $343\ \mathrm{m/s}$, and has path difference $0.75\ \mathrm{m}$. Find the phase difference caused by the paths.

**Explanation**

The wavelength is $\lambda=v/f=1\ \mathrm{m}$, so the path difference is $0.75$ of a cycle. Equivalently,

$$
\begin{aligned}
\Delta\phi_{\text{path}}
&=\frac{2\pi f\Delta r}{v}\\
&=\frac{2\pi(343)(0.75)}{343}\\
&=\frac{3\pi}{2}\ \mathrm{rad}.
\end{aligned}
$$

The factor $2\pi$ converts cycles to radians. Leaving it out gives a number of cycles, not a phase in radians.

```quiz
type: radio
id: p4-path-to-phase
content: |-
  A wave has $f=686\ \mathrm{Hz}$, $v=343\ \mathrm{m/s}$, and $\Delta r=0.25\ \mathrm{m}$. What is $\Delta\phi_{\text{path}}$?
options:
- id: p4-phase-a
  content: |-
    $\pi\ \mathrm{rad}$
  correct: true
- id: p4-phase-b
  content: |-
    $\frac{\pi}{2}\ \mathrm{rad}$
- id: p4-phase-c
  content: |-
    $2\pi\ \mathrm{rad}$
- id: p4-phase-d
  content: |-
    $0.5\ \mathrm{rad}$
- id: p4-phase-e
  content: |-
    $4\pi\ \mathrm{rad}$
```

---

<a id="include-the-initial-phase-offset"></a>
## Include the Initial Phase Offset

**Example:** Two sources begin $\pi$ radians out of phase, and their path difference contributes $3\pi/2$ radians. Find the unreduced phase difference.

**Explanation**

Use the same B-relative-to-A convention for both terms:

$$
\begin{aligned}
\Delta\phi
&=\Delta\phi_0+\Delta\phi_{\text{path}}\\
&=\pi+\frac{3\pi}{2}\\
&=\frac{5\pi}{2}\ \mathrm{rad}.
\end{aligned}
$$

The word **unreduced** means to keep the complete accumulated value. Do not subtract $2\pi$ unless the question asks for a one-cycle or equivalent phase.

```quiz
type: radio
id: p4-add-initial-phase
content: |-
  Two sources begin $\pi$ radians out of phase. Their path difference contributes $4\pi$ radians. What is the unreduced phase difference?
options:
- id: p4-initial-a
  content: |-
    $5\pi\ \mathrm{rad}$
  correct: true
- id: p4-initial-b
  content: |-
    $4\pi\ \mathrm{rad}$
- id: p4-initial-c
  content: |-
    $3\pi\ \mathrm{rad}$
- id: p4-initial-d
  content: |-
    $\pi\ \mathrm{rad}$
- id: p4-initial-e
  content: |-
    $8\pi\ \mathrm{rad}$
```

---

<a id="match-the-requested-phase-form"></a>
## Match the Requested Phase Form

**Example:** A calculation gives $\Delta\phi=13\pi/2\ \mathrm{rad}$. Distinguish its unreduced value, one-cycle representation, and smallest unsigned separation.

**Explanation**

The unreduced phase is the value produced by the full calculation:

$$
\Delta\phi_{\text{unreduced}}=\frac{13\pi}{2}\ \mathrm{rad}.
$$

For a one-cycle representation, subtract whole turns of $2\pi$:

$$
\frac{13\pi}{2}-3(2\pi)=\frac{\pi}{2}\ \mathrm{rad}.
$$

Because $\pi/2$ is already no larger than $\pi$, it is also the smallest unsigned angular separation. These answer forms describe the same phase relation, but they are not interchangeable when a prompt specifies one form.

```quiz
type: radio
id: p4-phase-form
content: |-
  A calculation gives an unreduced phase of $17\pi/3\ \mathrm{rad}$. What is its one-cycle representation in $[0,2\pi)$?
options:
- id: p4-form-a
  content: |-
    $\frac{5\pi}{3}\ \mathrm{rad}$
  correct: true
- id: p4-form-b
  content: |-
    $\frac{17\pi}{3}\ \mathrm{rad}$
- id: p4-form-c
  content: |-
    $\frac{\pi}{3}\ \mathrm{rad}$
- id: p4-form-d
  content: |-
    $\frac{2\pi}{3}\ \mathrm{rad}$
- id: p4-form-e
  content: |-
    $\frac{11\pi}{3}\ \mathrm{rad}$
```

---

<a id="complete-the-two-flute-calculation"></a>
## Complete the Two-Flute Calculation

**Example:** Flute A is at $x=-13\ \mathrm{m}$, flute B is at $x=+27\ \mathrm{m}$, and point P is at $(0,61\ \mathrm{m})$. Both flutes emit an $830\ \mathrm{Hz}$ note, the sound speed is $343\ \mathrm{m/s}$, and the flutes begin $\pi$ radians out of phase. Find the phase difference at P.

![](<../Source/Images/two-flute-source-geometry.png>)

**Explanation**

The source-to-point distances are

$$
\begin{aligned}
r_A&=\sqrt{13^2+61^2}=62.3699\ldots\ \mathrm{m},\\
r_B&=\sqrt{27^2+61^2}=66.7083\ldots\ \mathrm{m}.
\end{aligned}
$$

Using $\Delta r=r_B-r_A$,

$$
\Delta r=4.33846\ldots\ \mathrm{m}.
$$

Now include both the propagation phase and the initial $\pi$-radian offset:

$$
\begin{aligned}
\Delta\phi
&=\pi+\frac{2\pi(830)(4.3384558\ldots)}{343}\\
&=69.1044\ldots\ \mathrm{rad}.
\end{aligned}
$$

The coordinate data support about two significant figures, so the requested unreduced result is

$$
\boxed{69\ \mathrm{rad}}.
$$

If a one-cycle representation were requested instead, the result would be $6.27\ \mathrm{rad}$ modulo $2\pi$. The smallest unsigned separation is $0.0107\ \mathrm{rad}$, but it points in the opposite orientation. These are equivalent physical phase relations, not the requested unreduced answer.

```quiz
type: radio
id: p4-answer-convention
content: |-
  For the two-flute data above, which value matches the requested **unreduced** phase difference to about two significant figures?
options:
- id: p4-convention-a
  content: |-
    $69\ \mathrm{rad}$
  correct: true
- id: p4-convention-b
  content: |-
    $6.27\ \mathrm{rad}$
- id: p4-convention-c
  content: |-
    $0.0107\ \mathrm{rad}$
- id: p4-convention-d
  content: |-
    $66\ \mathrm{rad}$
- id: p4-convention-e
  content: |-
    $72\ \mathrm{rad}$
```

---

<a id="summary"></a>
## Summary

When source positions, a detector position, frequency, wave speed, and an initial phase offset are given:

1. Find the full path lengths $r_A$ and $r_B$.
2. Choose and keep a subtraction order, such as $\Delta r=r_B-r_A$.
3. Convert distance difference to phase with $\Delta\phi_{\text{path}}=2\pi f\Delta r/v$.
4. Add the initial offset: $\Delta\phi=\Delta\phi_0+\Delta\phi_{\text{path}}$.
5. Reduce modulo $2\pi$ only if the requested answer convention calls for it.

The main traps are subtracting source coordinates instead of path lengths, dropping the factor $2\pi$, forgetting the initial phase offset, and reporting a reduced phase when an unreduced value was requested.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
