# Classifying Two-Source Interference from Path and Starting Phase

<!--
lesson-id: 212-M5-047
topic-code: MTH212.M5.47
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Path Difference](#find-the-path-difference)
- [Turn Path Difference into Phase](#turn-path-difference-into-phase)
- [Include the Starting Phase](#include-the-starting-phase)
- [Recognize the Neither Case](#recognize-the-neither-case)
- [Summary](#summary)

## Prerequisites

- Find the distance between two points on a line.
- Interpret one wavelength as one complete cycle.
- Recognize that one complete cycle is a phase change of $2\pi$.

---

<a id="introduction"></a>
## Introduction

When two coherent sources reach the same point by different paths, two effects determine how their signals line up:

1. the phase difference with which the sources begin, and
2. the phase difference produced by the unequal path lengths.

The reusable procedure is to **find the path difference, convert it to a propagation phase difference, add the initial phase difference, and reduce the result by whole multiples of $2\pi$**.

Use the same phase ledger every time:

$$
\begin{aligned}
\text{initial:}\quad &\Delta\phi_0,\\
\text{propagation:}\quad &\Delta\phi_{\text{path}}
=2\pi\frac{\Delta r}{\lambda},\\
\text{arrival:}\quad &\Delta\phi_{\text{total}}
=\Delta\phi_0+\Delta\phi_{\text{path}}.
\end{aligned}
$$

Then subtract whole cycles of $2\pi$ until the arrival phase is in the interval $[0,2\pi)$.

For equal-amplitude signals:

$$
\Delta\phi_{\text{total}}\equiv 0\pmod{2\pi}
\quad\Longrightarrow\quad
\text{completely constructive},
$$

$$
\Delta\phi_{\text{total}}\equiv \pi\pmod{2\pi}
\quad\Longrightarrow\quad
\text{completely destructive}.
$$

Any other remaining phase difference gives neither complete construction nor complete destruction.

---

<a id="find-the-path-difference"></a>
## Find the Path Difference

**Example:** Two speakers are $12\ \mathrm{m}$ apart. A listener stands between them, $5\ \mathrm{m}$ from speaker A. Find the path difference.

**Explanation**

The two path lengths are

$$
r_A=5\ \mathrm{m},
\qquad
r_B=12\ \mathrm{m}-5\ \mathrm{m}=7\ \mathrm{m}.
$$

The path difference is the absolute difference, not the sum:

$$
\Delta r=|r_B-r_A|=|7-5|\ \mathrm{m}=2\ \mathrm{m}.
$$

```quiz
type: radio
id: pq3-p3-q1
content: |-
  Two sources are $14\ \mathrm{m}$ apart. Point P lies between them, $4\ \mathrm{m}$ from source A. What is the path difference at P?
options:
- id: q1-a
  content: |-
    $4\ \mathrm{m}$
  feedback: |-
    $4\ \mathrm{m}$ is one path length, $r_A$, not the path difference. Since $r_B=14-4=10\ \mathrm{m}$, compare the two paths to get $\Delta r=|10-4|=6\ \mathrm{m}$.
- id: q1-b
  content: |-
    $6\ \mathrm{m}$
  correct: true
  feedback: |-
    Path difference is the absolute difference between the distances traveled. Point P is $4\ \mathrm{m}$ from A and $10\ \mathrm{m}$ from B, so $\Delta r=|10-4|=6\ \mathrm{m}$.
- id: q1-c
  content: |-
    $10\ \mathrm{m}$
  feedback: |-
    $10\ \mathrm{m}=14-4$ is the path from B to P, not the difference between paths. Subtract the $4\ \mathrm{m}$ path from A to obtain $\Delta r=6\ \mathrm{m}$.
- id: q1-d
  content: |-
    $14\ \mathrm{m}$
  feedback: |-
    $14\ \mathrm{m}$ is the distance between the sources. Interference at P depends on the difference between the $4\ \mathrm{m}$ and $10\ \mathrm{m}$ travel distances, which is $6\ \mathrm{m}$.
```

---

<a id="turn-path-difference-into-phase"></a>
## Turn Path Difference into Phase

**Example:** A path difference is $3.0\ \mathrm{m}$ and the wavelength is $2.0\ \mathrm{m}$. Find the phase difference caused by propagation.

**Explanation**

First count how many wavelengths fit in the path difference:

$$
\frac{\Delta r}{\lambda}
=\frac{3.0}{2.0}
=1.5.
$$

Each wavelength contributes $2\pi$ of phase, so

$$
\Delta\phi_{\text{path}}
=2\pi\frac{\Delta r}{\lambda}
=2\pi(1.5)
=3\pi.
$$

Because $3\pi\equiv\pi\pmod{2\pi}$, the unequal paths alone make the arriving signals opposite in phase.

```quiz
type: radio
id: pq3-p3-q2
content: |-
  Two signals have a path difference of $4.5\ \mathrm{m}$ and a wavelength of $3.0\ \mathrm{m}$. What value does $2\pi\Delta r/\lambda$ give before reducing by whole multiples of $2\pi$?
options:
- id: q2-a
  content: |-
    $\pi$
  feedback: |-
    $\pi$ is the phase-equivalent remainder after reducing by one full $2\pi$ cycle. The question asks for the value before reduction, and $2\pi(4.5/3.0)=3\pi$.
- id: q2-b
  content: |-
    $2\pi$
  feedback: |-
    A $2\pi$ path phase corresponds to a path difference of exactly one wavelength. Here $\Delta r/\lambda=1.5$, so the unreduced phase is $2\pi(1.5)=3\pi$.
- id: q2-c
  content: |-
    $3\pi$
  correct: true
  feedback: |-
    Each wavelength of path difference contributes one $2\pi$ phase cycle. The paths differ by $4.5/3.0=1.5$ wavelengths, so the unreduced propagation phase is $3\pi$.
- id: q2-d
  content: |-
    $4.5\pi$
  feedback: |-
    Phase depends on the number of wavelengths in the path difference, so the distance must first be divided by $\lambda$. Using $4.5$ directly ignores the $3.0\ \mathrm{m}$ wavelength; the correct ratio is $1.5$ and the phase is $3\pi$.
```

---

<a id="include-the-starting-phase"></a>
## Include the Starting Phase

**Example:** Whistle A and whistle B are $11\ \mathrm{m}$ apart. Point P is between them, $4.0\ \mathrm{m}$ to the right of A. Both whistles emit wavelength $2.0\ \mathrm{m}$ with equal amplitudes, but they begin completely out of phase. Classify the interference at P.

![](<../Source/PQ3/Images/two-whistles-interference-geometry.png>)

**Explanation**

The path lengths are

$$
r_A=4.0\ \mathrm{m},
\qquad
r_B=11\ \mathrm{m}-4.0\ \mathrm{m}=7.0\ \mathrm{m},
$$

so

$$
\Delta r=|7.0-4.0|\ \mathrm{m}=3.0\ \mathrm{m}=1.5\lambda.
$$

Propagation contributes

$$
\Delta\phi_{\text{path}}=2\pi(1.5)=3\pi.
$$

Completely out-of-phase sources begin with

$$
\Delta\phi_0=\pi.
$$

Therefore,

$$
\Delta\phi_{\text{total}}
=\Delta\phi_0+\Delta\phi_{\text{path}}
=\pi+3\pi
=4\pi
\equiv 0\pmod{2\pi}.
$$

The interference at P is **completely constructive**. The half-integer path difference flips the whistles' original out-of-phase relationship back into alignment.

For complete interference, the shortcut table is:

| $\Delta r/\lambda$ | Sources begin in phase | Sources begin out of phase |
|---|---|---|
| Integer | Constructive | Destructive |
| Half-integer | Destructive | Constructive |

Equivalently, for $n=0,1,2,\ldots$:

$$
\begin{array}{c|cc}
& \text{constructive} & \text{destructive}\\ \hline
\text{begin in phase}
& \Delta r=n\lambda
& \Delta r=\left(n+\frac12\right)\lambda\\
\text{begin out of phase}
& \Delta r=\left(n+\frac12\right)\lambda
& \Delta r=n\lambda
\end{array}
$$

These are repeating families: adding one whole wavelength to the path difference adds $2\pi$ and does not change the classification.

```quiz
type: radio
id: pq3-p3-q3
content: |-
  Two equal-amplitude sources are $16\ \mathrm{m}$ apart and begin completely out of phase. Point P lies between them, $5.0\ \mathrm{m}$ from source A. The wavelength is $4.0\ \mathrm{m}$. What type of interference occurs at P?
options:
- id: q3-a
  content: |-
    Completely constructive interference
  correct: true
  feedback: |-
    The $5\ \mathrm{m}$ and $11\ \mathrm{m}$ paths differ by $1.5\lambda$, which contributes an odd-$\pi$ phase reversal. That reversal cancels the sources' initial out-of-phase relation, so they arrive in phase and interfere completely constructively.
- id: q3-b
  content: |-
    Completely destructive interference
  feedback: |-
    The initial $\pi$ offset alone would be destructive, but the half-integer path difference adds another odd-$\pi$ reversal. Together they give $4\pi\equiv0$, so the signals arrive constructively.
- id: q3-c
  content: |-
    Neither
  feedback: |-
    “Neither” would require a total phase other than $0$ or $\pi$ modulo $2\pi$. Here the initial $\pi$ plus the $3\pi$ path phase equals $4\pi\equiv0$, so the interference is completely constructive.
```

---

<a id="recognize-the-neither-case"></a>
## Recognize the Neither Case

**Example:** Two equal-amplitude sources begin in phase. Their path difference to a point is $5.0\ \mathrm{m}$, and their wavelength is $4.0\ \mathrm{m}$. Classify the interference.

**Explanation**

Here,

$$
\frac{\Delta r}{\lambda}=\frac{5.0}{4.0}=1.25,
$$

so

$$
\Delta\phi_{\text{path}}=2\pi(1.25)=2.5\pi
\equiv\frac{\pi}{2}\pmod{2\pi}.
$$

The sources begin in phase, so $\Delta\phi_0=0$. The total phase difference is therefore $\pi/2$, which is neither $0$ nor $\pi$ modulo $2\pi$. The interference is **neither completely constructive nor completely destructive**.

```quiz
type: radio
id: pq3-p3-q4
content: |-
  Two equal-amplitude sources begin completely out of phase. Their path difference to a point is $3.0\ \mathrm{m}$, and their wavelength is $4.0\ \mathrm{m}$. What type of interference occurs there?
options:
- id: q4-a
  content: |-
    Completely constructive interference
  feedback: |-
    Complete construction requires the arrivals to be in phase, $\Delta\phi\equiv0$. Here $\pi+2\pi(3/4)=5\pi/2\equiv\pi/2$, so the waves are not completely aligned.
- id: q4-b
  content: |-
    Completely destructive interference
  feedback: |-
    Complete destruction requires $\Delta\phi\equiv\pi$, but the $3\pi/2$ path phase changes the initial $\pi$ relation. The total reduces to $\pi/2$, not $\pi$.
- id: q4-c
  content: |-
    Neither
  correct: true
  feedback: |-
    The sources begin with a $\pi$ offset, and the $3/4$-wavelength path difference contributes $3\pi/2$. Their total is $5\pi/2\equiv\pi/2$, which is neither the $0$ for complete construction nor the $\pi$ for complete destruction.
```

---

<a id="summary"></a>
## Summary

When two sources interfere at a point:

1. Find both path lengths.
2. Compute $\Delta r=|r_B-r_A|$.
3. Convert the path difference with
   $$
   \Delta\phi_{\text{path}}=2\pi\frac{\Delta r}{\lambda}.
   $$
4. Add the initial phase difference: $0$ for in-phase sources or $\pi$ for completely out-of-phase sources.
5. Reduce to $[0,2\pi)$ by subtracting whole multiples of $2\pi$:
   - remainder $0$: completely constructive,
   - remainder $\pi$: completely destructive,
   - any other remainder: neither.

The main trap is ignoring the initial phase. A half-integer path difference reverses the usual result when the sources begin completely out of phase.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Finding the First Constructive-Interference Point](../../2026-07-30-M5-5/Lessons/Problem-5.md)

Study guide index: 27/28

---
<!-- lesson-nav:end -->
