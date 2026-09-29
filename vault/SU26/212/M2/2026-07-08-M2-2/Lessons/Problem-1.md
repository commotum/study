# Comparing Moment of Inertia From Mass Distribution

<!--
lesson-id: 212-M2-007
topic-code: MTH212.M2.07
-->

## Table of Contents

- [Introduction](#introduction)
- [Measure Distance From the Rotation Axis](#measure-distance-from-the-rotation-axis)
- [Use the Squared-Distance Effect](#use-the-squared-distance-effect)
- [Cancel Identical Contributions](#cancel-identical-contributions)
- [Apply the Comparison to the Barbells](#apply-the-comparison-to-the-barbells)
- [Summary](#summary)

## Prerequisites

- Identify the rotation axis and the perpendicular distance from a mass to that axis.
- Square positive distances.
- Compare sums term by term.
- Recognize which parts of two configurations are identical.

---

<a id="introduction"></a>
## Introduction

Moment of inertia measures how strongly a mass distribution resists angular acceleration about a chosen axis. For point masses,

$$
I=\sum_i m_i r_{\perp,i}^2,
$$

where $r_{\perp,i}$ is the perpendicular distance from mass $m_i$ to the rotation axis.

When two objects contain the same masses and differ only in where those masses are placed, compare their $r_\perp^2$ terms. Moving mass closer to the axis decreases the moment of inertia; moving it farther away increases the moment of inertia.

---

<a id="measure-distance-from-the-rotation-axis"></a>
## Measure Distance From the Rotation Axis

**Example:** Two equal point masses lie on opposite sides of an axis. Each mass is $0.40\ \mathrm{m}$ from the axis. Write their combined moment-of-inertia contribution.

**Explanation**

Both masses are the same perpendicular distance from the axis, so

$$
I_{\mathrm{masses}}
=m(0.40)^2+m(0.40)^2
=2m(0.40)^2.
$$

Use distance from the axis, not the full distance between the two masses. Here, the masses are $0.80\ \mathrm{m}$ apart, but each individual $r_\perp$ is $0.40\ \mathrm{m}$.

```quiz
type: radio
id: m2-2-p1-axis-distance
shuffle: true
content: |-
  Two equal point masses lie symmetrically on a bar and are $1.20\ \mathrm{m}$ apart. The rotation axis passes through the midpoint. What distance $r_\perp$ belongs in each term of $I=\sum_i m_i r_{\perp,i}^2$?
options:
- id: a
  content: |-
    $0.30\ \mathrm{m}$
- id: b
  content: |-
    $0.60\ \mathrm{m}$
  correct: true
  feedback: |-
    The midpoint axis is halfway between the masses, so each mass is $1.20/2=0.60\ \mathrm{m}$ from the axis.
- id: c
  content: |-
    $1.20\ \mathrm{m}$
- id: d
  content: |-
    $2.40\ \mathrm{m}$
- id: e
  content: |-
    Zero
```

---

<a id="use-the-squared-distance-effect"></a>
## Use the Squared-Distance Effect

**Example:** The two equal masses in one configuration are each at distance $d$ from the axis. In a second configuration, each is at distance $d/2$. Compare only the masses' contributions.

**Explanation**

For the first configuration,

$$
I_1=2md^2.
$$

For the second,

$$
I_2
=2m\left(\frac d2\right)^2
=2m\left(\frac{d^2}{4}\right)
=\frac14 I_1.
$$

Halving every relevant distance makes that part of the moment of inertia one-fourth as large. The distance is squared, so this is not a linear change.

More generally, for unchanged mass,

$$
r_{\perp,\mathrm{new}}=kr_{\perp,\mathrm{old}}
\quad\Longrightarrow\quad
I_{\mathrm{new}}=k^2I_{\mathrm{old}}.
$$

| Distance scale factor $k$ | Contribution scale factor $k^2$ |
|---:|---:|
| $\frac12$ | $\frac14$ |
| $2$ | $4$ |
| $3$ | $9$ |

Predict the squared scale factor first, then evaluate the numerical contributions. This makes it harder to mistake the relationship for direct linear proportionality.

```quiz
type: radio
id: m2-2-p1-square-effect
shuffle: true
content: |-
  Identical masses are moved from perpendicular distance $r_\perp$ to distance $3r_\perp$ from the same rotation axis. By what factor does each mass's $m r_\perp^2$ contribution change?
options:
- id: a
  content: |-
    It becomes one-third as large.
- id: b
  content: |-
    It becomes three times as large.
- id: c
  content: |-
    It becomes six times as large.
- id: d
  content: |-
    It becomes nine times as large.
  correct: true
  feedback: |-
    Replacing $r_\perp$ with $3r_\perp$ gives $m(3r_\perp)^2=9m r_\perp^2$.
- id: e
  content: |-
    It does not change.
```

---

<a id="cancel-identical-contributions"></a>
## Cancel Identical Contributions

**Example:** Two barbell sets have the same center bar with moment of inertia $I_{\mathrm{bar}}$ and the same two weights of mass $m$. Set X places each weight at distance $d_X$; Set Y places each at the smaller distance $d_Y$.

**Explanation**

Their total moments of inertia can be written as

$$
I_X=I_{\mathrm{bar}}+2md_X^2,
\qquad
I_Y=I_{\mathrm{bar}}+2md_Y^2.
$$

The center-bar term is identical in both totals. Because $d_Y<d_X$ and distances are nonnegative,

$$
d_Y^2<d_X^2,
$$

so

$$
I_Y<I_X.
$$

The same conclusion holds for finite-size weights: each identical weight has the same moment of inertia about its own center, while the placement contribution $md^2$ is smaller when its center is closer to the axis.

```quiz
type: radio
id: m2-2-p1-common-parts
shuffle: true
content: |-
  Two rotating assemblies have identical hubs and identical pairs of masses. Assembly P places each mass $0.30\ \mathrm{m}$ from the axis, while Assembly Q places each mass $0.50\ \mathrm{m}$ from the axis. Which statement is correct?
options:
- id: a
  content: |-
    P has the smaller moment of inertia because its masses are closer to the axis.
  correct: true
  feedback: |-
    The identical hub contributions are equal. For the masses, $2m(0.30)^2<2m(0.50)^2$, so P has the smaller total moment of inertia.
- id: b
  content: |-
    Q has the smaller moment of inertia because its masses are farther apart.
- id: c
  content: |-
    They have equal moments of inertia because their total masses are equal.
- id: d
  content: |-
    They have equal moments of inertia because their hubs are identical.
- id: e
  content: |-
    Their moments of inertia cannot be compared without knowing the angular speed.
```

---

<a id="apply-the-comparison-to-the-barbells"></a>
## Apply the Comparison to the Barbells

**Example:** Compare the two sets in the given diagram about the center-of-mass axis.

**Explanation**

The weights and center bars are identical, so mass and the bar's contribution do not decide the comparison. Set B places both weights closer to the center-of-mass axis. Its two $mr^2$ contributions are therefore smaller, making its total moment of inertia smaller.

| Contribution | Set A versus Set B | Effect on comparison |
|---|---|---|
| Center bar | Identical | Cancels from the ranking |
| Two weight masses | Identical | Cancels from the ranking |
| Weight distances $r_\perp$ | Larger in A | Makes the weight terms larger in A |
| Squared-distance sum | $\sum r_{\perp,A}^2>\sum r_{\perp,B}^2$ | Therefore $I_A>I_B$ |

```quiz
type: radio
id: m2-2pre-q1
shuffle: true
content: |-
  **Question 1**

  Two sets of barbells with identical weights and identical center bars are configured as shown.

  Which set has the smaller moment of inertia about its center of mass?

  ![](<../Source/Images/barbell-mass-distribution.png>)
options:
- id: a
  content: |-
    Set A
- id: b
  content: |-
    Set B
  correct: true
  feedback: |-
    Moment of inertia depends on the distance of each mass from the rotation axis:

    $$
    I=\sum_i m_i r_{\perp,i}^2.
    $$

    In Set B, the weights are closer to the center of mass, so their $r_\perp$ values are smaller. The identical center bars contribute the same moment of inertia, making Set B's total moment of inertia smaller.
- id: same
  content: |-
    They have the same moment of inertia
```

---

<a id="summary"></a>
## Summary

- Identify the rotation axis and measure each mass's perpendicular distance $r_\perp$ from it.
- Use $I=\sum_i m_i r_{\perp,i}^2$ and compare squared distances, not just total mass or overall length.
- Equal masses moved to a fraction $k$ of their old distance contribute a fraction $k^2$ as much.
- Ignore contributions that are identical in both configurations; they cannot change which total is larger.
- The main trap is assuming equal total mass means equal moment of inertia. Distribution relative to the axis matters.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../../M3/2026-07-20-Q-2/Study-Guide.md)
Next: [Finding Torque from a Force at an Angle](../../2026-07-09-M2-3/Lessons/Problem-3.md)

Study guide index: 03/20

---
<!-- lesson-nav:end -->
