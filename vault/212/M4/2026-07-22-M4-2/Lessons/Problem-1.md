# Comparing Pendulum Periods When Bob Mass Changes

## Table of Contents

- [Introduction](#introduction)
- [Translate One Oscillation Into Period](#translate-one-oscillation-into-period)
- [Inspect the Variables in the Period Formula](#inspect-the-variables-in-the-period-formula)
- [Compare Two Pendulums Directly](#compare-two-pendulums-directly)
- [Separate Mass Changes From Length Changes](#separate-mass-changes-from-length-changes)
- [Apply the Test to the Two Pendulums](#apply-the-test-to-the-two-pendulums)
- [Summary](#summary)

## Prerequisites

- Recognize the period $T$ as the time for one full oscillation.
- Use the small-angle simple-pendulum formula $T=2\pi\sqrt{L/g}$.
- Compare two formulas after identifying which quantities are the same and which differ.

---

<a id="introduction"></a>
## Introduction

For a simple pendulum undergoing small oscillations, the period is

$$
T=2\pi\sqrt{\frac{L}{g}},
$$

where $L$ is the pendulum length and $g$ is the gravitational acceleration.

When two pendulums differ in one property, use this test:

1. Translate the requested time into the period $T$.
2. Identify the property that changed.
3. Check whether that property appears in the period formula.
4. Compare the quantities that do appear.

The bob mass $m$ does not appear in the formula. Therefore, changing only the bob mass does not change the small-angle period.

Use the symbols as a quick dependency audit:

| Given quantity | Role in this comparison |
|---|---|
| Length $L$ | Controls $T$ and is the same for both pendulums |
| Gravity $g$ | Controls $T$ and is the same for both pendulums |
| Bob mass $m$ | Differs, but is absent from the formula |
| Release angle $\theta$ | Establishes the shared small-angle setup |

---

<a id="translate-one-oscillation-into-period"></a>
## Translate One Oscillation Into Period

**Example:** A pendulum is released, swings across its equilibrium position, reaches the opposite side, and returns to its starting position. What time interval has elapsed?

**Explanation**

The pendulum has completed one full cycle and returned to the same position moving in the same direction. The elapsed time is one **period**, denoted by $T$.

Thus, asking which pendulum “completes one full oscillation in less time” is the same as asking which pendulum has the smaller period.

Position alone is not enough to identify a full cycle. A pendulum passes the equilibrium point twice per cycle, but it completes a period only when its entire motion state repeats.

```quiz
type: radio
id: problem-1-period-q1
content: |-
  Two pendulums begin at their leftmost positions. Which measurement is the time until each pendulum next returns to its leftmost position with the same direction of motion?
options:
- id: a
  content: |-
    The period
  correct: true
  feedback: |-
    One return to the same state completes one full oscillation, so the elapsed time is the period.
- id: b
  content: |-
    Half the period
  feedback: |-
    After half a period, the pendulum is at the opposite extreme rather than back at its starting state.
- id: c
  content: |-
    The frequency
  feedback: |-
    Frequency counts oscillations per unit time; it is not the time for one oscillation.
```

---

<a id="inspect-the-variables-in-the-period-formula"></a>
## Inspect the Variables in the Period Formula

**Example:** A pendulum's bob is replaced by a heavier bob without changing the pendulum length. What happens to its small-angle period?

**Explanation**

Write the governing formula before reasoning from intuition:

$$
T=2\pi\sqrt{\frac{L}{g}}.
$$

The formula contains $L$ and $g$, but it does not contain the bob mass $m$. At the same location, $g$ is fixed, and the problem says the length is unchanged. Therefore, the value of $T$ is unchanged.

A useful substitution check is to ask, “Where would I insert the changed value?” There is no place to substitute $m$ into $2\pi\sqrt{L/g}$. This is direct evidence that changing $m$ alone cannot change the formula's output.

**Watch Out!** A heavier bob has greater weight, but “greater force” alone does not imply a shorter period. The pendulum's resistance to acceleration increases by the same mass factor, leaving mass absent from the final period formula.

```quiz
type: radio
id: problem-1-formula-q1
content: |-
  A small-angle simple pendulum keeps the same length but receives a bob with twice the mass. What happens to its period?
options:
- id: a
  content: |-
    It doubles.
  feedback: |-
    Bob mass does not appear in $T=2\pi\sqrt{L/g}$.
- id: b
  content: |-
    It is cut in half.
  feedback: |-
    A heavier bob does not make the small-angle pendulum complete a cycle sooner.
- id: c
  content: |-
    It stays the same.
  correct: true
  feedback: |-
    With $L$ and $g$ unchanged, the period formula gives the same value.
```

---

<a id="compare-two-pendulums-directly"></a>
## Compare Two Pendulums Directly

**Example:** Pendulums $P$ and $Q$ have equal lengths and swing at the same location, but $m_P>m_Q$. Compare their periods.

**Explanation**

Write one expression for each pendulum:

$$
T_P=2\pi\sqrt{\frac{L_P}{g}}
\qquad\text{and}\qquad
T_Q=2\pi\sqrt{\frac{L_Q}{g}}.
$$

Because the pendulums have equal lengths,

$$
L_P=L_Q.
$$

They are also at the same location, so they have the same $g$. Their period expressions are therefore identical:

$$
T_P=T_Q.
$$

The inequality $m_P>m_Q$ never enters the comparison because neither period expression contains mass.

```quiz
type: radio
id: problem-1-compare-q1
content: |-
  Pendulums $C$ and $D$ have the same length and are released through small angles at the same location. If $m_C<m_D$, which relation is correct?
options:
- id: a
  content: |-
    $T_C<T_D$
  feedback: |-
    The lighter bob does not have a different period when length and gravity match.
- id: b
  content: |-
    $T_C=T_D$
  correct: true
  feedback: |-
    The two values of $L$ and $g$ are equal, and mass is absent from the period formula.
- id: c
  content: |-
    $T_C>T_D$
  feedback: |-
    The mass inequality does not create a period inequality.
```

---

<a id="separate-mass-changes-from-length-changes"></a>
## Separate Mass Changes From Length Changes

**Example:** Which change can alter a simple pendulum's small-angle period: doubling its bob mass or doubling its length?

**Explanation**

Use the formula as a dependency map:

| Quantity changed | Appears in $T=2\pi\sqrt{L/g}$? | Effect on period |
|---|---:|---|
| Bob mass $m$ | No | No effect |
| Length $L$ | Yes | A larger $L$ gives a larger $T$ |
| Gravitational acceleration $g$ | Yes | A larger $g$ gives a smaller $T$ |

The square-root function is increasing for positive inputs. Therefore, increasing $L$ increases $T$, although the period grows by the square root of the length factor rather than by the full factor.

Doubling the bob mass leaves $T$ unchanged. Doubling the length multiplies the period by $\sqrt{2}$:

$$
\frac{T_2}{T_1}=\sqrt{\frac{L_2}{L_1}}=\sqrt{2}.
$$

This contrast prevents the rule “identical pendulums have equal periods” from becoming too broad. Their periods are equal here because the quantities that control the period—$L$ and $g$—match.

```quiz
type: radio
id: problem-1-length-q1
content: |-
  Pendulums $X$ and $Y$ are at the same location. Their bob masses differ, and $L_X=4L_Y$. How do their small-angle periods compare?
options:
- id: a
  content: |-
    $T_X=2T_Y$
  correct: true
  feedback: |-
    Period scales as $\sqrt{L}$, so $T_X/T_Y=\sqrt{4}=2$; the different bob masses do not affect the result.
- id: b
  content: |-
    $T_X=4T_Y$
  feedback: |-
    Period depends on the square root of length, not directly on length.
- id: c
  content: |-
    $T_X=T_Y$
  feedback: |-
    Mass does not matter, but the unequal lengths do.
```

---

<a id="apply-the-test-to-the-two-pendulums"></a>
## Apply the Test to the Two Pendulums

**Example:** Pendulums A and B are identical except that $m_A>m_B$. They start at the same angle. Which completes one full oscillation in less time?

![](<../Source/Images/identical-pendulums-different-masses.png>)

**Explanation**

One full oscillation takes one period. The pendulums have the same length and are at the same location, so

$$
T_A=2\pi\sqrt{\frac{L}{g}}
\qquad\text{and}\qquad
T_B=2\pi\sqrt{\frac{L}{g}}.
$$

The common starting angle gives the same small-angle setup, while the unequal masses do not appear in the formula. Hence,

$$
T_A=T_B.
$$

Neither pendulum completes the oscillation first; they take the same amount of time.

```quiz
type: radio
id: m4-2pre-q1
shuffle: true
content: |-
  **Question 1**

  Pendulums A and B are identical except that $m_A>m_B$. They are raised to the same angle $\theta$ and released simultaneously. Which pendulum completes one full oscillation in less time?

  ![](<../Source/Images/identical-pendulums-different-masses.png>)
options:
- id: a
  content: Pendulum A
- id: b
  content: Pendulum B
- id: c
  content: They oscillate in the same amount of time
  correct: true
  feedback: For small oscillations, $T=2\pi\sqrt{L/g}$. The period depends on pendulum length and gravitational acceleration, not the bob's mass, so the two periods are equal.
```

---

<a id="summary"></a>
## Summary

When comparing the time for one full pendulum oscillation:

1. Interpret that time as the period $T$.
2. Write $T=2\pi\sqrt{L/g}$ for small oscillations.
3. Check which given differences actually appear in the formula.
4. If $L$ and $g$ match, the periods match even when the bob masses differ.
5. Do not infer a shorter period from the heavier bob's larger weight.

Changing only the bob mass does not change a simple pendulum's small-angle period.
