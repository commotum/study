# Choosing a Slit Width for Clear Single-Slit Diffraction

<!--
lesson-id: 212-M6-011
topic-code: MTH212.M6.11
-->
## Table of Contents

- [Introduction](#introduction)
- [Test the First Minimum](#test-the-first-minimum)
- [Use the Physical Range of Sine](#use-the-physical-range-of-sine)
- [Connect Slit Width to Pattern Spread](#connect-slit-width-to-pattern-spread)
- [Choose a Practical Slit Width](#choose-a-practical-slit-width)
- [Summary](#summary)

## Prerequisites

- Recognize that $0\leq \sin\theta\leq 1$ for angles from $0^\circ$ to $90^\circ$.
- Use the single-slit minimum condition $a\sin\theta=m\lambda$.
- Evaluate a simple inverse sine in degrees.

---

<a id="introduction"></a>
## Introduction

When a problem compares a slit width $a$ with a wavelength $\lambda$ and asks whether a clear single-slit diffraction pattern appears, test the location of the **first minimum**. Set $m=1$ in

$$
a\sin\theta=m\lambda
$$

to obtain

$$
\sin\theta_1=\frac{\lambda}{a}.
$$

Use two checks:

1. **Existence:** the input to inverse sine, $\lambda/a$, must lie in $[0,1]$. If $\lambda/a>1$, no first minimum exists.
2. **Screen usefulness:** the endpoint $\lambda/a=1$ gives $\theta_1=90^\circ$, so an ordinary forward screen does not show the usual minimum-bounded pattern. If $0<\lambda/a<1$, the first minimum occurs at a non-boundary angle; its size tells how spread out the pattern is.

This turns a qualitative phrase such as “clear diffraction pattern” into a quick numerical test.

---

<a id="test-the-first-minimum"></a>
## Test the First Minimum

**Example:** A slit has width $a=5\lambda$. Where is its first minimum?

**Explanation**

Use the first-minimum condition, keeping wavelength in the numerator:

$$
\sin\theta_1=\frac{\lambda}{a}
=\frac{\lambda}{5\lambda}
=\frac15.
$$

Therefore,

$$
\theta_1=\sin^{-1}\left(\frac15\right)\approx 11.5^\circ.
$$

The first dark minimum occurs at a real, non-boundary angle, so the central maximum is visibly bounded.

```quiz
type: radio
id: problem-1-q1
content: |-
  A slit has width $a=4\lambda$. What is the first step toward locating the first diffraction minimum?
options:
- id: problem-1-q1-a
  content: |-
    Set $\sin\theta_1=\dfrac14$.
  correct: true
  feedback: |-
    The first minimum uses $m=1$, so $\sin\theta_1=\lambda/a=\lambda/(4\lambda)=1/4$. This is physical and gives $\theta_1\approx14.5^\circ$.
- id: problem-1-q1-b
  content: |-
    Set $\sin\theta_1=4$.
  feedback: |-
    This reverses the ratio. The minimum equation gives $\sin\theta_1=\lambda/a$, not $a/\lambda$; here the correct ratio is $1/4$, while $4$ cannot be a sine.
- id: problem-1-q1-c
  content: |-
    Set $\sin\theta_1=\dfrac1{16}$.
  feedback: |-
    The minimum condition contains the first power of $a$, so the width ratio is not squared. Substituting $a=4\lambda$ gives $\lambda/(4\lambda)=1/4$.
- id: problem-1-q1-d
  content: |-
    Set $\sin\theta_1=1$.
  feedback: |-
    A value of $1$ occurs only at the boundary case $a=\lambda$. Because this slit is four wavelengths wide, the first-minimum ratio is $1/4$.
```

---

<a id="use-the-physical-range-of-sine"></a>
## Use the Physical Range of Sine

**Example:** Compare $a=\lambda/2$, $a=\lambda$, and $a=4\lambda$.

**Explanation**

For each width, test $\lambda/a$:

| Slit width | $\lambda/a$ | First-minimum result |
| --- | ---: | --- |
| $\lambda/2$ | $2$ | Impossible because $\sin\theta_1$ cannot exceed $1$ |
| $\lambda$ | $1$ | Boundary minimum at $90^\circ$ |
| $4\lambda$ | $1/4$ | Ordinary minimum at about $14.5^\circ$ |

The key distinction is not simply whether diffraction occurs. It is whether the standard pattern has accessible dark minima that separate its bright regions.

```quiz
type: radio
id: problem-1-q2
content: |-
  Which slit width places the first minimum at an ordinary angle strictly between $0^\circ$ and $90^\circ$?
options:
- id: problem-1-q2-a
  content: |-
    $a=\dfrac{\lambda}{3}$
  feedback: |-
    This gives $\sin\theta_1=3$, outside sine's physical range. The broad diffraction distribution has no first dark minimum at a real angle.
- id: problem-1-q2-b
  content: |-
    $a=\lambda$
  feedback: |-
    This gives $\sin\theta_1=1$, so $\theta_1=90^\circ$. That is the limiting boundary, not an ordinary minimum on a forward screen.
- id: problem-1-q2-c
  content: |-
    $a=3\lambda$
  correct: true
  feedback: |-
    Here $\sin\theta_1=\lambda/(3\lambda)=1/3$, which lies strictly between $0$ and $1$. Thus the first minimum occurs at the ordinary angle $\theta_1\approx19.5^\circ$.
- id: problem-1-q2-d
  content: |-
    All three widths
  feedback: |-
    The sine-range test separates the cases: $a=\lambda/3$ requires an impossible sine of $3$, and $a=\lambda$ puts the minimum only at $90^\circ$. Only $a=3\lambda$ gives $0<\lambda/a<1$.
```

---

<a id="connect-slit-width-to-pattern-spread"></a>
## Connect Slit Width to Pattern Spread

**Example:** Compare slits of width $8\lambda$ and $40\lambda$.

**Explanation**

For a fixed wavelength, $\lambda/a$ varies inversely with slit width: decreasing $a$ increases the first-minimum angle, while increasing $a$ moves the minimum toward the forward direction.

Their first-minimum ratios are

$$
\sin\theta_{1,8}=\frac18,
\qquad
\sin\theta_{1,40}=\frac1{40}.
$$

Because sine increases from $0^\circ$ to $90^\circ$, $1/8>1/40$ means $\theta_{1,8}>\theta_{1,40}$. The narrower slit gives the wider central maximum. A very wide slit can produce minima, but it squeezes them close to the forward direction and makes the pattern harder to resolve.

```quiz
type: radio
id: problem-1-q3
content: |-
  Two slits are illuminated by the same wavelength. Slit A has width $6\lambda$, and slit B has width $30\lambda$. Which statement is correct?
options:
- id: problem-1-q3-a
  content: |-
    Slit A has the wider central maximum because $\lambda/(6\lambda)>\lambda/(30\lambda)$.
  correct: true
  feedback: |-
    The central maximum extends to the first minima, where $\sin\theta_1=\lambda/a$. Slit A has the larger ratio and therefore the larger first-minimum angle, so its central maximum is wider.
- id: problem-1-q3-b
  content: |-
    Slit B has the wider central maximum because it is physically wider.
  feedback: |-
    Physical slit width and angular pattern width vary oppositely. Increasing $a$ reduces $\lambda/a$, moves the first minimum toward $0^\circ$, and narrows the central maximum; therefore slit B's pattern is narrower.
- id: problem-1-q3-c
  content: |-
    The central maxima have the same width because the wavelength is the same.
  feedback: |-
    Wavelength is only one part of the controlling ratio $\lambda/a$. Since the slit widths differ, the first-minimum angles and central-maximum widths also differ.
- id: problem-1-q3-d
  content: |-
    Neither slit has a first minimum because both are wider than one wavelength.
  feedback: |-
    Widths greater than $\lambda$ make $0<\lambda/a<1$, which guarantees a physical first minimum. The no-minimum case occurs for $a<\lambda$, when $\lambda/a>1$.
```

---

<a id="choose-a-practical-slit-width"></a>
## Choose a Practical Slit Width

**Example:** For incident wavelength $\lambda$, choose among $10\lambda$, $\lambda$, and $\lambda/10$ for a clear single-slit pattern.

**Explanation**

Compute the first-minimum test for each option:

$$
\begin{array}{c|c|c}
a & \sin\theta_1=\lambda/a & \text{interpretation} \\
\hline
10\lambda & 0.1 & \theta_1\approx5.7^\circ \\
\lambda & 1 & \theta_1=90^\circ \\
\lambda/10 & 10 & \text{no physical first minimum}
\end{array}
$$

Only $10\lambda$ gives a non-boundary first minimum that can bound a recognizable central maximum on an ordinary screen. In a real experiment, screen distance and detector resolution also affect visibility, but the first-minimum test is enough to distinguish these three choices.

```quiz
type: radio
id: problem-1-q4
shuffle: true
content: |-
  For incident light of wavelength $\lambda$, which slit width would produce a clear single-slit diffraction pattern?
options:
- id: problem-1-q4-a
  content: |-
    $10\lambda$
  correct: true
  feedback: |-
    Single-slit minima satisfy $a\sin\theta=m\lambda$. With $a=10\lambda$, the first minimum has $\sin\theta_1=0.1$, so it occurs at about $5.7^\circ$ and visibly bounds the central maximum.
- id: problem-1-q4-b
  content: |-
    $\lambda$
  feedback: |-
    With $a=\lambda$, the first-minimum condition gives $\sin\theta_1=1$, placing the minimum at $90^\circ$. An ordinary forward screen therefore does not show the usual resolved, minimum-bounded pattern.
- id: problem-1-q4-c
  content: |-
    $\dfrac{\lambda}{10}$
  feedback: |-
    With $a=\lambda/10$, the first-minimum condition would require $\sin\theta_1=10$, which is impossible. The usual dark-minimum structure needed for a clear single-slit pattern is absent.
```

---

<a id="summary"></a>
## Summary

**Cue:** the options compare $a$ directly with $\lambda$ and ask about the visibility or spread of a single-slit pattern.

**Procedure:**

1. Set $m=1$ and compute $\sin\theta_1=\lambda/a$.
2. Reject $\lambda/a>1$: no physical first minimum exists.
3. Treat $\lambda/a=1$ as a boundary case: the first minimum is at $90^\circ$.
4. For $0<\lambda/a<1$, use the angle to judge spread; a smaller slit gives a wider pattern.

**Main trap:** do not reverse the ratio. It is wavelength divided by slit width, $\lambda/a$.

For the given choices, $a=10\lambda$ is the only width with a clear, non-boundary diffraction pattern.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
