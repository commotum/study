# Compare Frequencies on Identical Springs

<!--
lesson-id: 212-M5-002
topic-code: MTH212.M5.02
-->

## Table of Contents

- [Introduction](#introduction)
- [Read the Mass Dependence](#read-the-mass-dependence)
- [Compare Frequencies With a Ratio](#compare-frequencies-with-a-ratio)
- [Separate Amplitude From Frequency](#separate-amplitude-from-frequency)
- [Match the Source Diagram and Options](#match-the-source-diagram-and-options)
- [Summary](#summary)

## Prerequisites

- Identify which quantities are held constant in a comparison.
- Interpret a variable in the denominator of a square root.
- Distinguish oscillation amplitude from frequency.

---

<a id="introduction"></a>
## Introduction

For an ideal mass–spring oscillator,

$$
f=\frac{1}{2\pi}\sqrt{\frac{k}{m}},
$$

where $k$ is the spring constant and $m$ is the oscillating mass.

When two springs are identical, their spring constants are equal. The frequency comparison then depends only on mass:

$$
f\propto\frac{1}{\sqrt{m}}.
$$

The recognition cue is **identical springs with different masses**. The smaller mass has the higher frequency.

| Quantity changed | Effect on ideal frequency |
| --- | --- |
| larger spring constant $k$ | higher $f$ |
| larger mass $m$ | lower $f$ |
| larger amplitude $A$ | no change in $f$ |

---

<a id="read-the-mass-dependence"></a>
## Read the Mass Dependence

Mass appears in the denominator of the frequency formula. With $k$ fixed:

$$
m\uparrow\quad\Longrightarrow\quad f\downarrow,
$$

and

$$
m\downarrow\quad\Longrightarrow\quad f\uparrow.
$$

**Example:** Identical springs hold masses of $0.20\ \mathrm{kg}$ and $0.80\ \mathrm{kg}$. Which mass oscillates with the higher frequency?

**Explanation**

The spring constants are the same, so compare the masses. Because $0.20\ \mathrm{kg}<0.80\ \mathrm{kg}$,

$$
f_{0.20}>f_{0.80}.
$$

The $0.20\ \mathrm{kg}$ mass has less inertia and reverses its motion more readily.

For the same displacement, identical springs exert the same restoring-force magnitude. The smaller mass then has the larger acceleration magnitude because $a=F/m$, so it completes each oscillation sooner.

```quiz
type: radio
id: problem-2-spring-frequency-q1
content: |-
  Identical springs hold masses of $0.30\ \mathrm{kg}$ and $0.12\ \mathrm{kg}$. Which mass oscillates with the higher frequency?
options:
- id: a
  content: |-
    The $0.30\ \mathrm{kg}$ mass
  feedback: |-
    The larger mass has more inertia and a lower frequency when $k$ is fixed.
- id: b
  content: |-
    The $0.12\ \mathrm{kg}$ mass
  correct: true
  feedback: |-
    With the same $k$, $f\propto1/\sqrt{m}$, so the smaller $0.12\ \mathrm{kg}$ mass has the higher frequency.
- id: c
  content: |-
    They have the same frequency
  feedback: |-
    Identical springs make $k$ equal, but the different masses still give different frequencies.
- id: d
  content: |-
    There is not enough information
  feedback: |-
    The common spring constant need not be known numerically; equal $k$ lets the masses determine the ordering.
```

---

<a id="compare-frequencies-with-a-ratio"></a>
## Compare Frequencies With a Ratio

For two masses on identical springs, the common factors cancel:

$$
\frac{f_1}{f_2}
=\frac{\sqrt{k/m_1}}{\sqrt{k/m_2}}
=\sqrt{\frac{m_2}{m_1}}.
$$

This ratio gives both the ordering and the size of the frequency difference.

The quotient rule for radicals explains the cancellation:

$$
\frac{\sqrt{k/m_1}}{\sqrt{k/m_2}}
=\sqrt{\frac{k/m_1}{k/m_2}}
=\sqrt{\frac{m_2}{m_1}}.
$$

**Example:** Identical springs hold masses of $0.10\ \mathrm{kg}$ and $0.40\ \mathrm{kg}$. Compare their frequencies.

**Explanation**

$$
\frac{f_{0.10}}{f_{0.40}}
=\sqrt{\frac{0.40}{0.10}}
=\sqrt{4}
=2.
$$

The $0.10\ \mathrm{kg}$ mass oscillates twice as frequently as the $0.40\ \mathrm{kg}$ mass.

```quiz
type: radio
id: problem-2-spring-frequency-q2
content: |-
  Identical springs hold masses of $0.20\ \mathrm{kg}$ and $0.80\ \mathrm{kg}$. What is $f_{0.20}/f_{0.80}$?
options:
- id: a
  content: |-
    $\frac14$
  feedback: |-
    This treats the frequency as directly proportional to mass.
- id: b
  content: |-
    $\frac12$
  feedback: |-
    This reverses the frequency ordering; the lighter mass must have the larger frequency.
- id: c
  content: |-
    $1$
  feedback: |-
    Equal spring constants do not cancel the effect of unequal masses.
- id: d
  content: |-
    $2$
  correct: true
  feedback: |-
    $f_{0.20}/f_{0.80}=\sqrt{0.80/0.20}=\sqrt4=2$.
- id: e
  content: |-
    $4$
  feedback: |-
    The mass ratio is $4$, but frequency changes by its square root.
```

---

<a id="separate-amplitude-from-frequency"></a>
## Separate Amplitude From Frequency

The distance a mass is pulled from equilibrium sets its amplitude $A$. For an ideal mass–spring oscillator, amplitude does not appear in

$$
f=\frac{1}{2\pi}\sqrt{\frac{k}{m}}.
$$

Equal pull distances therefore do not make different masses oscillate at the same frequency.

For vertical springs, gravity shifts each mass to its own equilibrium position. Frequency describes oscillation **about** that equilibrium and still depends on $k$ and $m$, not on the equilibrium height or release amplitude.

**Example:** Two identical mass–spring systems have the same $m$ and $k$. One mass is pulled $2.0\ \mathrm{cm}$ from equilibrium and the other is pulled $5.0\ \mathrm{cm}$. Compare their frequencies.

**Explanation**

The amplitudes differ, but both $m$ and $k$ are the same. Their frequencies are equal. Only their maximum displacements differ.

```quiz
type: radio
id: problem-2-spring-frequency-q3
content: |-
  Two identical mass–spring systems have the same mass and spring constant. One is released from an amplitude of $3.0\ \mathrm{cm}$ and the other from $6.0\ \mathrm{cm}$. In the ideal model, which has the higher frequency?
options:
- id: a
  content: |-
    The $3.0\ \mathrm{cm}$ amplitude oscillator
- id: b
  content: |-
    The $6.0\ \mathrm{cm}$ amplitude oscillator
- id: c
  content: |-
    They have the same frequency
  correct: true
  feedback: |-
    The ideal frequency depends on $k$ and $m$, not amplitude. Changing the pull distance alone does not change $f$.
- id: d
  content: |-
    The one released first
```

---

<a id="match-the-source-diagram-and-options"></a>
## Match the Source Diagram and Options

In a diagram, identify the mass labels, confirm that the spring constants match, and treat the equal pull distance as amplitude information rather than frequency information.

**Example:** Identical springs hold $120\ \mathrm{g}$ and $30\ \mathrm{g}$ masses. Both are pulled the same distance downward and released. Which has the higher frequency?

**Explanation**

The springs have the same $k$, and the common pull distance does not enter the frequency formula. Since $30\ \mathrm{g}<120\ \mathrm{g}$, the $30\ \mathrm{g}$ mass has the higher frequency.

For the source masses, the frequency ratio is

$$
\frac{f_{50\ \mathrm{g}}}{f_{100\ \mathrm{g}}}
=\sqrt{\frac{100}{50}}
=\sqrt{2}>1.
$$

This confirms that the $50\ \mathrm{g}$ mass oscillates more frequently.

```quiz
type: radio
id: problem-2-source-check
shuffle: true
content: |-
  **Question 1**

  Two masses hanging from identical springs are pulled the same distance downward and released. Which mass oscillates with the higher frequency? Explain.

  ![](<../Source/Images/identical-springs-different-masses.png>)
options:
- id: a
  content: The $100\ \mathrm{g}$ mass
  feedback: For identical springs, $f=(1/2\pi)\sqrt{k/m}$, so the larger mass has the lower frequency.
- id: b
  content: The $50\ \mathrm{g}$ mass
  correct: true
  feedback: For identical springs, $f=(1/2\pi)\sqrt{k/m}$. The smaller mass therefore has the higher frequency; the equal pull distance changes amplitude, not frequency.
- id: c
  content: They have the same frequency
  feedback: Equal amplitudes do not make the frequencies equal. With the same spring constant, frequency decreases as mass increases.
```

---

<a id="summary"></a>
## Summary

For two ideal mass–spring oscillators:

1. Start with
   $$
   f=\frac{1}{2\pi}\sqrt{\frac{k}{m}}.
   $$
2. If the springs are identical, hold $k$ fixed.
3. Compare the masses using $f\propto1/\sqrt{m}$.
4. Choose the smaller mass for the higher frequency.
5. Use a square-root mass ratio when the size of the difference is requested.
6. Do not use equal pull distance to infer equal frequency; pull distance sets amplitude.

The main traps are treating frequency as proportional to mass and confusing equal amplitude with equal frequency.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
