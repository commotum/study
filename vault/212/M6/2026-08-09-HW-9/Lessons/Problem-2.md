# Finding Slit Width from the Central Diffraction Maximum

<!--
lesson-id: 212-M6-012
topic-code: MTH212.M6.12
-->
## Table of Contents

- [Introduction](#introduction)
- [Build the Full-Width Formula](#build-the-full-width-formula)
- [Solve from the Width Ratio](#solve-from-the-width-ratio)
- [Distinguish Full Width from Half-Width](#distinguish-full-width-from-half-width)
- [Check with the Inverse-Variation Invariant](#check-with-the-inverse-variation-invariant)
- [Summary](#summary)

## Prerequisites

- The first-minimum condition for a single slit: $a\sin\theta_1=\lambda$
- The small-angle screen relation: $y_1\approx L\sin\theta_1$
- Converting a percentage to a decimal
- Solving a formula for a variable in the denominator

---

<a id="introduction"></a>
## Introduction

When a problem gives the **full width** $W$ of a single-slit central maximum as a fraction of the screen distance $L$, first connect the two first minima to the slit width. In the far-screen, small-angle approximation, each first minimum is about $L\lambda/a$ from the center, so the full central maximum is twice that distance:

$$
W\approx \frac{2L\lambda}{a}.
$$

The reusable move is to divide by $L$, write the given fraction as $W/L$, and solve

$$
\frac{W}{L}\approx \frac{2\lambda}{a}
\qquad\Longrightarrow\qquad
\frac{a}{\lambda}\approx \frac{2}{W/L}.
$$

The two dimensionless ratios form an inverse-variation pair:

$$
\left(\frac{W}{L}\right)\left(\frac{a}{\lambda}\right)\approx2.
$$

A narrower central maximum therefore means a wider slit. The most common mistake is to forget that $W$ spans both sides of the center and omit the factor of $2$.

---

<a id="build-the-full-width-formula"></a>
## Build the Full-Width Formula

**Example:** A slit has width $a=25\lambda$. What fraction of $L$ is the full central-maximum width?

**Explanation**

The first minima occur symmetrically at $y=\pm y_1$, where

$$
y_1\approx \frac{L\lambda}{a}.
$$

The distance from $-y_1$ to $+y_1$ is $W=2y_1$. Therefore,

$$
\frac{W}{L}\approx \frac{2\lambda}{a}
=\frac{2\lambda}{25\lambda}
=0.08.
$$

Thus the full central maximum is about $0.08L$, or $8\%$ of the screen distance.

```quiz
type: radio
id: p2-q1
content: |-
  A single slit has width $a=50\lambda$. Approximately what is the full central-maximum width $W$?
options:
- id: p2-q1-a
  content: |-
    $W=0.02L$
  feedback: |-
    The value $0.02L=L\lambda/a$ is the center-to-first-minimum distance $y_1$. The full maximum runs from $-y_1$ to $+y_1$, so its width is twice this value.
- id: p2-q1-b
  content: |-
    $W=0.04L$
  correct: true
  feedback: |-
    A full central maximum spans both first-minimum distances, so $W/L=2\lambda/a=2/50=0.04$. Therefore $W=0.04L$.
- id: p2-q1-c
  content: |-
    $W=0.50L$
  feedback: |-
    The denominator must contain the slit width measured in wavelengths: $W/L=2/(a/\lambda)$. Using $a/\lambda=50$ gives $2/50$, not a decimal made by moving the digits in $50$.
- id: p2-q1-d
  content: |-
    $W=25L$
  feedback: |-
    This makes the pattern width grow with the slit width, but the relationship is inverse: $(W/L)(a/\lambda)=2$. With $a/\lambda=50$, the width ratio must be $2/50=0.04$, not $25$.
```

---

<a id="solve-from-the-width-ratio"></a>
## Solve from the Width Ratio

**Example:** The full central maximum has width $W=0.10L$. Find $a$ in terms of $\lambda$.

**Explanation**

Let $c=W/L=0.10$. Then

$$
c=\frac{2\lambda}{a}.
$$

Multiply by $a$, then divide by $c$:

$$
ac=2\lambda,
\qquad
a=\frac{2\lambda}{c}
=\frac{2\lambda}{0.10}
=20\lambda.
$$

```quiz
type: radio
id: p2-q2
content: |-
  In a single-slit experiment, the full central maximum has width $W=0.04L$. Approximately what is the slit width $a$?
options:
- id: p2-q2-a
  content: |-
    $a=0.02\lambda$
  feedback: |-
    This multiplies the width ratio by the half-width factor even though $a$ is in the denominator of $W/L=2\lambda/a$. Isolating $a$ requires division: $a/\lambda=2/(W/L)$.
- id: p2-q2-b
  content: |-
    $a=25\lambda$
  feedback: |-
    The value $25\lambda$ comes from $\lambda/(W/L)$ and therefore treats the given full width as a one-sided distance. Because $W=2y_1$, the numerator must be $2\lambda$.
- id: p2-q2-c
  content: |-
    $a=50\lambda$
  correct: true
  feedback: |-
    For the full central width, $a/\lambda=2/(W/L)$. Substituting $W/L=0.04$ gives $a/\lambda=2/0.04=50$, so $a=50\lambda$.
- id: p2-q2-d
  content: |-
    $a=100\lambda$
  feedback: |-
    A slit of $100\lambda$ would give $W/L=2/100=0.02$, only half the stated width. The ratio $0.04$ instead requires $a/\lambda=50$.
```

---

<a id="distinguish-full-width-from-half-width"></a>
## Distinguish Full Width from Half-Width

**Example:** A first minimum is $0.025L$ from the center. Find the slit width, and then state the full central width.

**Explanation**

Here $0.025L$ is the one-sided distance $y_1$, not the full width. Use

$$
\frac{y_1}{L}\approx\frac{\lambda}{a}.
$$

Then

$$
\frac{a}{\lambda}\approx\frac{1}{y_1/L}
=\frac{1}{0.025}
=40.
$$

Thus $a=40\lambda$. The full central width is

$$
W=2y_1=0.050L.
$$

```quiz
type: radio
id: p2-q3
content: |-
  The full central maximum is $0.08L$ wide. What is the distance $y_1$ from the center to either first minimum, and what slit width does it imply?
options:
- id: p2-q3-a
  content: |-
    $y_1=0.04L$ and $a=25\lambda$
  correct: true
  feedback: |-
    The central maximum extends equally on both sides, so $y_1=W/2=0.04L$. Then $y_1/L=\lambda/a$ gives $a/\lambda=1/0.04=25$.
- id: p2-q3-b
  content: |-
    $y_1=0.08L$ and $a=12.5\lambda$
  feedback: |-
    This treats the full width as though it were the center-to-minimum distance. Since the full maximum spans two equal sides, first halve $0.08L$ to get $y_1=0.04L$ before solving for $a$.
- id: p2-q3-c
  content: |-
    $y_1=0.04L$ and $a=12.5\lambda$
  feedback: |-
    The half-width $y_1=0.04L$ is correct, but $a$ is inversely related to $y_1/L$. The relation is $a/\lambda=1/0.04=25$, not $0.5/0.04=12.5$.
- id: p2-q3-d
  content: |-
    $y_1=0.16L$ and $a=6.25\lambda$
  feedback: |-
    Doubling the given full width moves farther than either boundary of the central maximum. The one-sided distance is half of $W$, and that corrected distance leads to $a=25\lambda$.
```

---

<a id="check-with-the-inverse-variation-invariant"></a>
## Check with the Inverse-Variation Invariant

**Example:** Suppose $W=0.05L$. Estimate $a$ in terms of $\lambda$ and verify the result.

**Explanation**

Convert the percentage to a decimal, then form the dimensionless ratio:

$$
5\%=\frac{5}{100}=0.05,
\qquad
\frac{W}{L}=0.05.
$$

Then

$$
\frac{a}{\lambda}
=\frac{2}{W/L}
=\frac{2}{0.05}
=40,
$$

so $a=40\lambda$. The invariant checks both the algebra and the factor of two:

$$
\left(\frac{W}{L}\right)\left(\frac{a}{\lambda}\right)
=(0.05)(40)=2.
$$

Equivalently, substitution returns the observed ratio:

$$
\frac{W}{L}\approx\frac{2\lambda}{40\lambda}=0.05.
$$

The trend also makes sense: a slit tens of wavelengths wide produces a central maximum that is only a small fraction of $L$.

```quiz
type: radio
id: p2-q4
shuffle: true
content: |-
  In a single-slit diffraction experiment, the width $W$ of the central bright maximum is $5\%$ of the distance $L$ between the slit and the screen:

  $$
  W=0.05L.
  $$

  Approximately how wide is the slit $a$, expressed in terms of the wavelength $\lambda$?
options:
- id: p2-q4-a
  content: |-
    $10\lambda$
  feedback: |-
    A slit width of $10\lambda$ gives $W/L=2\lambda/a=2/10=0.20$, four times the stated ratio. Because a narrower pattern requires a wider slit, $a$ must exceed $10\lambda$.
- id: p2-q4-b
  content: |-
    $20\lambda$
  feedback: |-
    The value $20\lambda$ results from using the one-sided relation $y_1/L=\lambda/a$ on the full width $W$. Since $W=2y_1$, the correct numerator is $2\lambda$, which doubles the required slit width.
- id: p2-q4-c
  content: |-
    $25\lambda$
  feedback: |-
    Substituting $a=25\lambda$ gives $W/L=2/25=0.08$, not $0.05$. The reciprocal ratio must be evaluated as $2/0.05=40$.
- id: p2-q4-d
  content: |-
    $40\lambda$
  correct: true
  feedback: |-
    The full-width relation is $W/L=2\lambda/a$. With $W/L=0.05$, solving gives $a/\lambda=2/0.05=40$, and substitution returns the stated width ratio.
```

---

<a id="summary"></a>
## Summary

- Cue: the **full** central-maximum width $W$ is given relative to the screen distance $L$.
- Rule: $W\approx2L\lambda/a$, because the maximum spans from one first minimum to the other.
- Procedure: compute $c=W/L$, then use $a/\lambda=2/c$.
- Check: verify $(W/L)(a/\lambda)\approx2$ and confirm that a wider slit gives a narrower pattern.
- Main trap: $L\lambda/a$ is only the center-to-first-minimum distance; omitting the factor of $2$ halves the slit-width answer.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 4 Study Guide](../../../M7/2026-08-13-Q-4/Study-Guide.md)
Next: End of Quiz 4 Study Guide.

Study guide index: 11/11

---

<!-- lesson-nav:end -->
