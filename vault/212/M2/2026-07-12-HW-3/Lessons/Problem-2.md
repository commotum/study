# Combining Center of Mass and Moment of Inertia

<!--
lesson-id: 212-M2-018
topic-code: MTH212.M2.18
-->

## Table of Contents

- [Introduction](#introduction)
- [Classify the Quantity Before Combining](#classify-the-quantity-before-combining)
- [Combine Center-of-Mass Positions](#combine-center-of-mass-positions)
- [Add Moments of Inertia About the Same Axis](#add-moments-of-inertia-about-the-same-axis)
- [Reject the Weighted-Inertia Trap](#reject-the-weighted-inertia-trap)
- [Summary](#summary)

## Prerequisites

- Interpret center of mass as a position weighted by mass.
- Interpret moment of inertia as a sum of contributions of the form $r^2\,dm$.
- Distinguish a quantity's value from the mass of the object that has that value.

---

<a id="introduction"></a>
## Introduction

When two objects are treated as one system, the cue is the quantity being combined. A **location**, such as $x_{\mathrm{cm}}$, must be averaged with mass as the weight. An **accumulated contribution**, such as moment of inertia about one specified axis, is added.

For two objects,

$$
x_{\mathrm{cm}}=
\frac{m_1x_{\mathrm{cm},1}+m_2x_{\mathrm{cm},2}}{m_1+m_2},
$$

while, about the same axis,

$$
I=I_1+I_2.
$$

The formulas look different because they answer different questions: *Where is the system centered?* versus *How much rotational inertia does the system have about this axis?*

Use this decision test:

1. If the result is a representative **location**, form the weighted contributions and divide by the total weight.
2. If the result is the **total accumulated contribution** of all components, add the component contributions.

---

<a id="classify-the-quantity-before-combining"></a>
## Classify the Quantity Before Combining

**Example:** Two objects form one system. Which description tells you to divide by the total mass: finding the system's center-of-mass position or finding its moment of inertia about an axis already shared by both given inertias?

**Explanation**

Divide by total mass only for the center-of-mass position. It is a mass-weighted average:

$$
x_{\mathrm{cm}}=
\frac{\text{total mass-position contribution}}{\text{total mass}}.
$$

Moment of inertia is already an accumulated quantity. If $I_1$ and $I_2$ are measured about the same axis, no extra averaging is needed.

```quiz
type: radio
id: p2-classify-quantity
content: |-
  Two objects are combined into one system. Which quantity requires division by $m_1+m_2$?
options:
- id: p2-classify-a
  content: |-
    The center-of-mass position
  correct: true
- id: p2-classify-b
  content: |-
    The total moment of inertia about the same axis
- id: p2-classify-c
  content: |-
    Both quantities
- id: p2-classify-d
  content: |-
    Neither quantity
```

---

<a id="combine-center-of-mass-positions"></a>
## Combine Center-of-Mass Positions

**Example:** Object 1 has mass $2\,\mathrm{kg}$ and center at $x_{\mathrm{cm},1}=1\,\mathrm{m}$. Object 2 has mass $3\,\mathrm{kg}$ and center at $x_{\mathrm{cm},2}=6\,\mathrm{m}$. Find the combined center of mass.

**Explanation**

Multiply each position by its mass, add those contributions, and divide by the total mass:

| Object | Mass | Position | Mass-position contribution |
| --- | ---: | ---: | ---: |
| 1 | $2\,\mathrm{kg}$ | $1\,\mathrm{m}$ | $2\,\mathrm{kg\,m}$ |
| 2 | $3\,\mathrm{kg}$ | $6\,\mathrm{m}$ | $18\,\mathrm{kg\,m}$ |

The numerator is the total mass-position contribution, $20\,\mathrm{kg\,m}$, and the denominator is the total mass, $5\,\mathrm{kg}$:

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{m_1x_{\mathrm{cm},1}+m_2x_{\mathrm{cm},2}}{m_1+m_2}\\
&=\frac{(2)(1)+(3)(6)}{2+3}\\
&=\frac{20}{5}\\
&=4\,\mathrm{m}.
\end{aligned}
$$

The answer lies between $1\,\mathrm{m}$ and $6\,\mathrm{m}$ and is closer to the heavier object's position, which is a useful check.

```quiz
type: radio
id: p2-center-of-mass
content: |-
  Object 1 has mass $4\,\mathrm{kg}$ and $x_{\mathrm{cm},1}=0\,\mathrm{m}$. Object 2 has mass $6\,\mathrm{kg}$ and $x_{\mathrm{cm},2}=5\,\mathrm{m}$. What is the combined center-of-mass position?
options:
- id: p2-com-a
  content: |-
    $2.5\,\mathrm{m}$
- id: p2-com-b
  content: |-
    $3\,\mathrm{m}$
  correct: true
- id: p2-com-c
  content: |-
    $5\,\mathrm{m}$
- id: p2-com-d
  content: |-
    $30\,\mathrm{m}$
- id: p2-com-e
  content: |-
    $9\,\mathrm{m}$
```

---

<a id="add-moments-of-inertia-about-the-same-axis"></a>
## Add Moments of Inertia About the Same Axis

**Example:** Object 1 has moment of inertia $I_1=2\,\mathrm{kg\,m^2}$ and object 2 has $I_2=5\,\mathrm{kg\,m^2}$, both measured about the same axis. Find the system's moment of inertia about that axis.

**Explanation**

Each given inertia already contains the object's full contribution relative to the specified axis. Add the contributions:

$$
I=I_1+I_2=2+5=7\,\mathrm{kg\,m^2}.
$$

The axis is part of the definition of each $I_i$, so the phrase **about the same axis** is essential. If the quoted inertias use different axes, first express them about one common axis; direct addition is not yet valid.

```quiz
type: radio
id: p2-add-inertias
content: |-
  Two components have moments of inertia $I_1=4\,\mathrm{kg\,m^2}$ and $I_2=9\,\mathrm{kg\,m^2}$ about the same axis. What is the combined moment of inertia about that axis?
options:
- id: p2-inertia-a
  content: |-
    $5\,\mathrm{kg\,m^2}$
- id: p2-inertia-b
  content: |-
    $6.5\,\mathrm{kg\,m^2}$
- id: p2-inertia-c
  content: |-
    $13\,\mathrm{kg\,m^2}$
  correct: true
- id: p2-inertia-d
  content: |-
    $36\,\mathrm{kg\,m^2}$
- id: p2-inertia-e
  content: |-
    More information about the masses is required.
```

---

<a id="reject-the-weighted-inertia-trap"></a>
## Reject the Weighted-Inertia Trap

**Example:** For two objects, consider these three statements:

1. $x_{\mathrm{cm}}=\dfrac{m_1x_{\mathrm{cm},1}+m_2x_{\mathrm{cm},2}}{m_1+m_2}$.
2. If $I_1$ and $I_2$ are about the same axis, then $I=I_1+I_2$.
3. If $I_1$ and $I_2$ are about the same axis, then $I=\dfrac{m_1I_1+m_2I_2}{m_1+m_2}$.

Which statements are true?

**Explanation**

Statements 1 and 2 are true. Statement 3 incorrectly treats moment of inertia as though it were a location or an average. The masses have already been accounted for inside $I_1$ and $I_2$.

A units check alone does not expose this mistake because both the correct sum and the weighted average have units of $\mathrm{kg\,m^2}$. Instead, use a scaling check. If two identical components each have inertia $I_0$ about the same axis, the combined system must contain twice the contribution:

$$
I=I_0+I_0=2I_0.
$$

The weighted-inertia expression would return only $I_0$ for equal masses and equal inertias. It therefore describes an average of the inertia values, not the accumulated inertia of both objects.

```quiz
type: radio
id: p2-original-logic
content: |-
  Two objects have center-of-mass positions $x_{\mathrm{cm},1}$ and $x_{\mathrm{cm},2}$ and moments of inertia $I_1$ and $I_2$ about the same axis. Which pair of rules is correct for the combined system?
options:
- id: p2-logic-a
  content: |-
    $x_{\mathrm{cm}}=\dfrac{x_{\mathrm{cm},1}+x_{\mathrm{cm},2}}{2}$ and $I=I_1+I_2$
- id: p2-logic-b
  content: |-
    $x_{\mathrm{cm}}=\dfrac{m_1x_{\mathrm{cm},1}+m_2x_{\mathrm{cm},2}}{m_1+m_2}$ and $I=I_1+I_2$
  correct: true
- id: p2-logic-c
  content: |-
    $x_{\mathrm{cm}}=x_{\mathrm{cm},1}+x_{\mathrm{cm},2}$ and $I=\dfrac{I_1+I_2}{2}$
- id: p2-logic-d
  content: |-
    $x_{\mathrm{cm}}=\dfrac{m_1x_{\mathrm{cm},1}+m_2x_{\mathrm{cm},2}}{m_1+m_2}$ and $I=\dfrac{m_1I_1+m_2I_2}{m_1+m_2}$
```

---

<a id="summary"></a>
## Summary

- **Cue:** Two objects are being treated as one system.
- **Location average:** for center-of-mass position, multiply each position by its mass, add, then divide by total mass.
- **Accumulated total:** for moment of inertia, add the component inertias when they are about the same axis.
- **Main trap:** do not mass-weight $I_1$ and $I_2$ again; each moment of inertia already contains its object's mass contribution.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
