# Deciding What Changes a Pendulum's Frequency

## Table of Contents

- [Introduction](#introduction)
- [Read the Dependency Formula](#read-the-dependency-formula)
- [Compare a Variable That Does Matter](#compare-a-variable-that-does-matter)
- [Reject a False Mass Dependence](#reject-a-false-mass-dependence)
- [Summary](#summary)

## Prerequisites

- Read which variables appear in a formula.
- Compare quantities using a ratio.
- Simplify square roots such as $\sqrt{1/4}=1/2$.

---

<a id="introduction"></a>
## Introduction

For a simple pendulum undergoing small oscillations, the frequency is

$$
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}},
$$

where $g$ is the gravitational-field strength and $L$ is the pendulum length. When a question changes one feature of the pendulum, first check whether that feature appears in this formula. If it does not appear, changing it alone cannot change the frequency predicted by this model.

Holding the other quantities fixed, the formula gives this dependency map:

$$
f\propto \sqrt{g},
\qquad
f\propto \frac{1}{\sqrt{L}},
\qquad
f\text{ is independent of }m.
$$

---

<a id="read-the-dependency-formula"></a>
## Read the Dependency Formula

**Example:** Two bobs have masses $0.20\ \mathrm{kg}$ and $0.80\ \mathrm{kg}$. Each hangs from a string of the same length in the same location. Compare their oscillation frequencies.

**Explanation**

The formula contains $g$ and $L$, but not the bob mass $m$. Both pendulums have the same $g$ and $L$, so they have the same frequency:

$$
f_{0.20}=f_{0.80}.
$$

The larger mass changes forces such as the bob's weight, but mass cancels from the equation of motion and does not remain in the frequency formula.

```quiz
type: radio
id: pq3-p1-mass-tripled
content: |-
  A simple pendulum has frequency $f$. Its bob is replaced by another bob with three times the mass while the string length and location remain unchanged. What is the new frequency?
options:
- id: pq3-p1-mass-tripled-a
  content: |-
    $f/3$
- id: pq3-p1-mass-tripled-b
  content: |-
    $f/\sqrt{3}$
- id: pq3-p1-mass-tripled-c
  content: |-
    $f$
  correct: true
  feedback: |-
    Mass does not appear in $f=\frac{1}{2\pi}\sqrt{g/L}$, so changing only the mass leaves $f$ unchanged.
- id: pq3-p1-mass-tripled-d
  content: |-
    $\sqrt{3}f$
- id: pq3-p1-mass-tripled-e
  content: |-
    $3f$
```

---

<a id="compare-a-variable-that-does-matter"></a>
## Compare a Variable That Does Matter

**Example:** A pendulum's length changes from $L$ to $4L$ while $g$ stays fixed. Find the new frequency in terms of the original frequency $f$.

**Explanation**

For any two simple pendulums described by this model,

$$
\frac{f_2}{f_1}
=\sqrt{\frac{g_2}{g_1}\frac{L_1}{L_2}}.
$$

This ratio contains changes in $g$ and $L$, but no mass factor. Here $g_2=g_1$ and $L_2=4L_1$, so

$$
\frac{f_{\mathrm{new}}}{f}
=\sqrt{\frac{L}{4L}}
=\frac{1}{2}.
$$

Therefore,

$$
f_{\mathrm{new}}=\frac{f}{2}.
$$

This contrast is useful: changing $L$ matters because $L$ appears under the square root, while changing $m$ does not matter because $m$ is absent.

```quiz
type: radio
id: pq3-p1-length-reduced
content: |-
  A simple pendulum has frequency $f$. Its length is changed from $L$ to $L/9$ while its location stays fixed. What is the new frequency?
options:
- id: pq3-p1-length-reduced-a
  content: |-
    $f/9$
- id: pq3-p1-length-reduced-b
  content: |-
    $f/3$
- id: pq3-p1-length-reduced-c
  content: |-
    $f$
- id: pq3-p1-length-reduced-d
  content: |-
    $3f$
  correct: true
  feedback: |-
    Since $f\propto 1/\sqrt{L}$, reducing the length by a factor of $9$ increases the frequency by $\sqrt{9}=3$.
- id: pq3-p1-length-reduced-e
  content: |-
    $9f$
```

---

<a id="reject-a-false-mass-dependence"></a>
## Reject a False Mass Dependence

**Example:** A student argues that doubling the bob's mass must reduce the frequency because a heavier object is harder to accelerate. Identify the error.

**Explanation**

The student is reasoning from mass alone instead of reading the pendulum model. After the mass changes from $m$ to $2m$, the right-hand side of the frequency formula is still

$$
\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
$$

Therefore,

$$
f_{\mathrm{new}}
=\frac{1}{2\pi}\sqrt{\frac{g}{L}}
=f.
$$

Doubling $m$ changes no symbol on the right-hand side. There is no valid place to insert a factor of $2$, $1/2$, or $1/\sqrt{2}$.

```quiz
type: radio
id: pq3-p1-original-check
shuffle: true
content: |-
  A bob of mass $m$ swings as a pendulum on a massless string with frequency $f$. If the bob's mass is doubled, what happens to the oscillation frequency?
options:
- id: pq3-p1-original-check-a
  content: |-
    The new frequency is one-fourth the original frequency.
- id: pq3-p1-original-check-b
  content: |-
    The new frequency is one-half the original frequency.
- id: pq3-p1-original-check-c
  content: |-
    The new frequency is the same as the original frequency.
  correct: true
  feedback: |-
    The mass is absent from the simple-pendulum frequency formula, so doubling it does not change the frequency.
- id: pq3-p1-original-check-d
  content: |-
    The new frequency is twice the original frequency.
- id: pq3-p1-original-check-e
  content: |-
    The new frequency is four times the original frequency.
```

---

<a id="summary"></a>
## Summary

When a pendulum parameter changes:

1. Start with $f=\dfrac{1}{2\pi}\sqrt{\dfrac{g}{L}}$.
2. Hold the other quantities fixed and check whether the changed parameter appears.
3. Translate its change factor through the formula.

| Change | Frequency multiplier |
| --- | ---: |
| $m\to km$ | $1$ |
| $g\to kg$ | $\sqrt{k}$ |
| $L\to kL$ | $1/\sqrt{k}$ |

The main trap is inventing a mass dependence that the simple-pendulum formula does not contain.
