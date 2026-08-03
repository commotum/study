# Deciding What Changes a Pendulum's Frequency

<!--
lesson-id: 212-M5-045
topic-code: MTH212.M5.45
-->

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
  feedback: |-
    This assumes that tripling the bob's mass makes the pendulum three times slower. For a simple pendulum, the greater gravitational force and greater inertia scale together, so mass cancels; with $g$ and $L$ unchanged, the frequency remains $f$.
- id: pq3-p1-mass-tripled-b
  content: |-
    $f/\sqrt{3}$
  feedback: |-
    This imports the spring-oscillator dependence $f\propto 1/\sqrt m$ into a pendulum. Bob mass affects a mass-spring frequency, but a simple pendulum is controlled by $g$ and $L$, so tripling $m$ does not introduce a factor of $1/\sqrt3$.
- id: pq3-p1-mass-tripled-c
  content: |-
    $f$
  correct: true
  feedback: |-
    A heavier pendulum bob has proportionally more weight and inertia, so mass cancels from its small-angle motion. Since $f=(2\pi)^{-1}\sqrt{g/L}$ and neither $g$ nor $L$ changes, the new frequency is $f$.
- id: pq3-p1-mass-tripled-d
  content: |-
    $\sqrt{3}f$
  feedback: |-
    The factor $\sqrt3$ would follow if the gravitational field $g$ tripled, because $f\propto\sqrt g$. Here only the bob mass triples, and mass is absent from the pendulum frequency, so the multiplier is $1$.
- id: pq3-p1-mass-tripled-e
  content: |-
    $3f$
  feedback: |-
    This treats frequency as directly proportional to bob mass. Increasing mass increases both the restoring torque and rotational inertia by the same factor, leaving $f=(2\pi)^{-1}\sqrt{g/L}$ and therefore the frequency unchanged.
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
  feedback: |-
    This gives frequency the same change factor as length. Pendulum frequency varies inversely with the square root of length, so shortening $L$ to $L/9$ makes the oscillation faster rather than nine times slower.
- id: pq3-p1-length-reduced-b
  content: |-
    $f/3$
  feedback: |-
    This uses the correct square-root factor but applies it in the wrong direction. Because $L$ is in the denominator of $f=(2\pi)^{-1}\sqrt{g/L}$, reducing the length to $L/9$ increases the frequency by $\sqrt9=3$.
- id: pq3-p1-length-reduced-c
  content: |-
    $f$
  feedback: |-
    Unlike bob mass, length controls a simple pendulum's frequency. A shorter pendulum has a shorter time scale; changing $L$ to $L/9$ multiplies $f$ by $\sqrt{L/(L/9)}=3$, so it does not remain $f$.
- id: pq3-p1-length-reduced-d
  content: |-
    $3f$
  correct: true
  feedback: |-
    A shorter simple pendulum oscillates more rapidly, with $f\propto 1/\sqrt L$. Reducing the length from $L$ to $L/9$ therefore increases the frequency by $\sqrt9=3$, giving $f_{\mathrm{new}}=3f$.
- id: pq3-p1-length-reduced-e
  content: |-
    $9f$
  feedback: |-
    This correctly predicts an increase but treats frequency as inversely proportional to length. The dependence is inverse square root, so a factor-of-$9$ decrease in $L$ produces only a factor-of-$3$ increase: $f_{\mathrm{new}}=3f$.
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
  feedback: |-
    This invents an inverse-square dependence on bob mass. Mass increases the pendulum's gravitational restoring torque and its rotational inertia by the same factor, so it cancels; doubling $m$ leaves the frequency at $f$, not $f/4$.
- id: pq3-p1-original-check-b
  content: |-
    The new frequency is one-half the original frequency.
  feedback: |-
    This assumes that doubling the bob mass doubles the period and halves the frequency. In the simple-pendulum model, bob mass cancels and only $g$ and $L$ control the frequency, so changing $m$ alone leaves it unchanged.
- id: pq3-p1-original-check-c
  content: |-
    The new frequency is the same as the original frequency.
  correct: true
  feedback: |-
    A simple pendulum's small-angle frequency is $f=(2\pi)^{-1}\sqrt{g/L}$ because mass cancels between restoring force and inertia. Doubling only the bob mass leaves $g$ and $L$ unchanged, so the new frequency is still $f$.
- id: pq3-p1-original-check-d
  content: |-
    The new frequency is twice the original frequency.
  feedback: |-
    This treats bob mass as a direct frequency multiplier. Mass is not a control variable in $f=(2\pi)^{-1}\sqrt{g/L}$; with the same length and location, doubling $m$ leaves the frequency at $f$ rather than $2f$.
- id: pq3-p1-original-check-e
  content: |-
    The new frequency is four times the original frequency.
  feedback: |-
    This both introduces a mass dependence and squares the change factor. Bob mass cancels entirely from the simple-pendulum motion, so neither a factor of $2$ nor $4$ belongs in the frequency; it remains $f$.
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

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Period of a Uniform Rod as a Physical Pendulum](../../../M4/2026-07-22-M4-2/Lessons/Problem-3.md)

Study guide index: 06/28

---
<!-- lesson-nav:end -->
