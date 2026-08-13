# Build the Moment of Inertia of Discrete Masses About a Chosen Axis

<!--
lesson-id: 212-M3-042
topic-code: MTH212.M3.42
-->

## Table of Contents

- [Introduction](#introduction)
- [Measure Perpendicular Distance to the Axis](#measure-perpendicular-distance-to-the-axis)
- [Build a Distance Ledger](#build-a-distance-ledger)
- [Source-Video Example: Two 10 kg Blocks](#source-video-two-blocks)
- [Source-Video Example: Four 4 kg Blocks](#source-video-four-blocks)
- [Lecture-Note Extension: Rod and Point Mass](#lecture-note-rod-and-point-mass)
- [Checks and Common Traps](#checks-and-common-traps)
- [Summary](#summary)

## Prerequisites

- Identify a rotation axis in a diagram.
- Find the shortest distance from a point to a line.
- Evaluate squares before multiplying and adding.
- Read and expand sigma notation.
- Use the supplied formula $I_{\mathrm{rod,end}}=\frac13ML^2$ for a uniform thin rod about one end.

---

<a id="introduction"></a>
## Introduction

For point masses rotating about one specified axis, moment of inertia is

$$
\boxed{I=\sum_i m_i r_{\perp,i}^{,2}}.
$$

The subscript $\perp$ matters: $r_{\perp,i}$ is the shortest, perpendicular distance from mass $i$ to the rotation axis. It is not automatically the distance between two masses or the distance to the center of the picture.

Use one procedure:

1. Mark the rotation axis.
2. Measure each point mass's perpendicular distance $r_{\perp,i}$ from that axis.
3. Square every distance.
4. Form each contribution $m_i r_{\perp,i}^2$.
5. Add the contributions, grouping equal terms only after the distances are verified.

The axis is part of the definition. The same collection of masses can have a different $I$ about a different axis. The SI unit is

$$
[I]=\mathrm{kg\,m^2}.
$$

---

<a id="measure-perpendicular-distance-to-the-axis"></a>
## Measure Perpendicular Distance to the Axis

The relevant distance meets the axis at a right angle:

```text
point mass ●────────────┤ rotation axis
            r_perp      ⟂
```

A rotation axis is a line in space. If a flat diagram marks an axis pointing into or out of the page at a point $O$, then $r_\perp$ appears as the in-page distance from the mass to $O$. If the axis itself is drawn as a line in the page, drop a perpendicular from the mass to that line.

For a vertical, $y$-parallel axis $x=a$, a point mass at $(x_i,y_i)$ has

$$
r_{\perp,i}=|x_i-a|.
$$

The $y$-coordinate does not affect the shortest distance to that vertical axis. If a point mass lies on the axis, then $r_\perp=0$ and its contribution is zero:

$$
m(0)^2=0.
$$

**Example:** A $3\,\mathrm{kg}$ point mass is at $(4\,\mathrm m,2\,\mathrm m)$, and the rotation axis is the vertical line $x=1\,\mathrm m$. Its perpendicular distance and contribution are

$$
r_\perp=|4-1|=3\,\mathrm m,
$$

$$
I_1=(3)(3^2)=27\,\mathrm{kg\,m^2}.
$$

```quiz
type: radio
id: mct-p6-perpendicular-distance
shuffle: true
content: |-
  A $5\,\mathrm{kg}$ point mass is at $(6\,\mathrm m,-2\,\mathrm m)$. The rotation axis is the vertical, $y$-parallel line $x=2\,\mathrm m$. What is this mass's contribution to the moment of inertia?
options:
- id: mct-p6-perpendicular-distance-a
  content: |-
    $80\,\mathrm{kg\,m^2}$
  correct: true
  feedback: |-
    The perpendicular distance to $x=2$ is $|6-2|=4\,\mathrm m$. Thus $mr_\perp^2=(5)(4^2)=80\,\mathrm{kg\,m^2}$.
- id: mct-p6-perpendicular-distance-b
  content: |-
    $200\,\mathrm{kg\,m^2}$
  feedback: |-
    This uses the point's distance from the origin, since $6^2+(-2)^2=40$ and $5(40)=200$. The origin is not the axis; use the shortest distance to the line $x=2$.
- id: mct-p6-perpendicular-distance-c
  content: |-
    $20\,\mathrm{kg\,m^2}$
  feedback: |-
    This multiplies $m$ by $r_\perp$ without squaring the distance. Moment of inertia uses $mr_\perp^2$, so the contribution is $5(4^2)$.
- id: mct-p6-perpendicular-distance-d
  content: |-
    $16\,\mathrm{kg\,m^2}$
  feedback: |-
    This is $r_\perp^2$ alone. The point mass is $5\,\mathrm{kg}$, so its squared distance must also be multiplied by $5$.
- id: mct-p6-perpendicular-distance-e
  content: |-
    $320\,\mathrm{kg\,m^2}$
  feedback: |-
    This squares the coordinate difference and then introduces another factor of $4$. There is only one distance-square factor: $5|6-2|^2=80\,\mathrm{kg\,m^2}$.
```

---

<a id="build-a-distance-ledger"></a>
## Build a Distance Ledger

Write the summation as a row-by-row ledger before using symmetry:

| Mass | $m_i$ | $r_{\perp,i}$ | $r_{\perp,i}^2$ | $m_i r_{\perp,i}^2$ |
|---|---:|---:|---:|---:|
| 1 | $2\,\mathrm{kg}$ | $0\,\mathrm m$ | $0\,\mathrm{m^2}$ | $0\,\mathrm{kg\,m^2}$ |
| 2 | $5\,\mathrm{kg}$ | $2\,\mathrm m$ | $4\,\mathrm{m^2}$ | $20\,\mathrm{kg\,m^2}$ |
| 3 | $1\,\mathrm{kg}$ | $3\,\mathrm m$ | $9\,\mathrm{m^2}$ | $9\,\mathrm{kg\,m^2}$ |

Therefore,

$$
I=0+20+9=29\,\mathrm{kg\,m^2}.
$$

The first mass is still part of the system even though its contribution about this axis is zero.

```quiz
type: radio
id: mct-p6-ledger-control
shuffle: true
content: |-
  Three point masses have the following perpendicular distances from one axis: $4\,\mathrm{kg}$ at $0\,\mathrm m$, $2\,\mathrm{kg}$ at $3\,\mathrm m$, and $3\,\mathrm{kg}$ at $2\,\mathrm m$. What is the system's moment of inertia?
options:
- id: mct-p6-ledger-control-a
  content: |-
    $30\,\mathrm{kg\,m^2}$
  correct: true
  feedback: |-
    The ledger gives $4(0^2)+2(3^2)+3(2^2)=0+18+12=30\,\mathrm{kg\,m^2}$. The mass on the axis contributes zero.
- id: mct-p6-ledger-control-b
  content: |-
    $12\,\mathrm{kg\,m^2}$
  feedback: |-
    This uses $\sum mr$ instead of $\sum mr^2$: $2(3)+3(2)=12$. Square each perpendicular distance before multiplying by its mass.
- id: mct-p6-ledger-control-c
  content: |-
    $34\,\mathrm{kg\,m^2}$
  feedback: |-
    This assigns a nonzero contribution of $4\,\mathrm{kg\,m^2}$ to the mass on the axis. Its perpendicular distance is zero, so its term is $4(0^2)=0$.
- id: mct-p6-ledger-control-d
  content: |-
    $45\,\mathrm{kg\,m^2}$
  feedback: |-
    This treats both off-axis masses as though they were $3\,\mathrm m$ from the axis. The $3\,\mathrm{kg}$ mass is only $2\,\mathrm m$ away and contributes $3(2^2)=12$.
- id: mct-p6-ledger-control-e
  content: |-
    $0\,\mathrm{kg\,m^2}$
  feedback: |-
    Only the $4\,\mathrm{kg}$ mass lies on the axis. The other two masses have nonzero perpendicular distances and contribute $18$ and $12\,\mathrm{kg\,m^2}$.
```

---

<a id="source-video-two-blocks"></a>
## Source-Video Example: Two 10 kg Blocks

**Source-video worked example (`JrkimXqnCLw`, 0:02–2:45):** Two $10\,\mathrm{kg}$ point masses are separated by $10\,\mathrm m$. Calculate the moment of inertia about two different axes.

**Source-language precision:** The video calls $r$ the distance “between the axis of rotation and the mass.” More precisely, $r_\perp$ is the shortest perpendicular distance from the point mass to the axis. The two coincide in the source diagram.

### Case A: Axis Through the Midpoint

The equal masses put the system's center at the midpoint, so each mass is $5\,\mathrm m$ from the axis:

```text
10 kg ●──── 5 m ────┤──── 5 m ────● 10 kg
                    axis
```

| Mass | $m_i$ | $r_{\perp,i}$ | $m_i r_{\perp,i}^2$ |
|---|---:|---:|---:|
| left | $10\,\mathrm{kg}$ | $5\,\mathrm m$ | $250\,\mathrm{kg\,m^2}$ |
| right | $10\,\mathrm{kg}$ | $5\,\mathrm m$ | $250\,\mathrm{kg\,m^2}$ |

Thus

$$
I_{\mathrm{mid}}
=2(10)(5^2)
=500\,\mathrm{kg\,m^2}.
$$

### Case B: Axis Through the Left Mass

Moving the axis to the left mass changes the two distances to $0$ and $10\,\mathrm m$:

```text
axis
  ┤● 10 kg ─────────── 10 m ─────────── ● 10 kg
```

$$
\begin{aligned}
I_{\mathrm{left}}
&=(10)(0^2)+(10)(10^2)\\
&=0+1000\\
&=1000\,\mathrm{kg\,m^2}.
\end{aligned}
$$

The first mass contributes zero because it lies on the axis. The second mass uses its distance to the axis, which happens to equal the full separation in this case.

```quiz
type: radio
id: mct-p6-two-block-mirror
shuffle: true
content: |-
  Two $6\,\mathrm{kg}$ point masses are separated by $8.0\,\mathrm m$. What are their moments of inertia (1) about the midpoint axis and (2) about an axis through the right mass?
options:
- id: mct-p6-two-block-mirror-a
  content: |-
    $(192,\ 384)\,\mathrm{kg\,m^2}$
  correct: true
  feedback: |-
    About the midpoint, both radii are $4\,\mathrm m$, so $I=2(6)(4^2)=192$. About the right mass, the radii are $8$ and $0\,\mathrm m$, so $I=6(8^2)=384\,\mathrm{kg\,m^2}$.
- id: mct-p6-two-block-mirror-b
  content: |-
    $(384,\ 192)\,\mathrm{kg\,m^2}$
  feedback: |-
    These results are assigned to the wrong axes. The midpoint radius is only $4\,\mathrm m$ for each mass, while the end axis leaves one mass the full $8\,\mathrm m$ away.
- id: mct-p6-two-block-mirror-c
  content: |-
    $(96,\ 384)\,\mathrm{kg\,m^2}$
  feedback: |-
    The end-axis value is correct, but the midpoint calculation includes two masses. One contributes $6(4^2)=96$, so both contribute $192\,\mathrm{kg\,m^2}$.
- id: mct-p6-two-block-mirror-d
  content: |-
    $(192,\ 192)\,\mathrm{kg\,m^2}$
  feedback: |-
    The axis change alters the radii. About the right mass, one radius becomes zero and the other becomes the full $8\,\mathrm m$, giving $384\,\mathrm{kg\,m^2}$.
- id: mct-p6-two-block-mirror-e
  content: |-
    $(48,\ 48)\,\mathrm{kg\,m^2}$
  feedback: |-
    These values use $mr$ instead of $mr^2$. Both calculations must square the respective $4\,\mathrm m$ or $8\,\mathrm m$ distances.
```

---

<a id="source-video-four-blocks"></a>
## Source-Video Example: Four 4 kg Blocks

**Source-video worked example (`JrkimXqnCLw`, 4:20–7:45):** Four $4\,\mathrm{kg}$ point masses form two symmetric pairs. Each mass is initially $5\,\mathrm m$ from the central axis.

### Case A: Central Axis

All four ledger rows have the same mass and distance:

$$
I_{\mathrm{center}}
=4(4)(5^2)
=400\,\mathrm{kg\,m^2}.
$$

The factor of $4$ counts the four masses; the other $4$ is the mass of each block.

### Case B: Axis Shifted 9 m Left

Rebuild the distance ledger about the new axis. The two masses in the left pair are

$$
9-5=4\,\mathrm m
$$

from it, while the two masses in the right pair are

$$
9+5=14\,\mathrm m
$$

from it:

| Pair | Number of masses | Mass of each | $r_\perp$ | Pair contribution |
|---|---:|---:|---:|---:|
| nearer | $2$ | $4\,\mathrm{kg}$ | $4\,\mathrm m$ | $2(4)(4^2)=128\,\mathrm{kg\,m^2}$ |
| farther | $2$ | $4\,\mathrm{kg}$ | $14\,\mathrm m$ | $2(4)(14^2)=1568\,\mathrm{kg\,m^2}$ |

Therefore,

$$
I_{\mathrm{shifted}}
=128+1568
=1696\,\mathrm{kg\,m^2}.
$$

**Source-caption corrections:** In this segment, “five minutes” means $5\,\mathrm m$; “new center of mass” means the new **rotation axis**, since the masses and their center of mass did not move; and “40 meters” means $14\,\mathrm m$, as confirmed by $5+9=14$ and the video's $14^2$ calculation.

This result comes directly from $\sum m_i r_{\perp,i}^2$. No axis-shift shortcut is needed.

```quiz
type: radio
id: mct-p6-four-block-control
shuffle: true
content: |-
  Four $2\,\mathrm{kg}$ point masses form two equal pairs about one axis. Two masses are $3\,\mathrm m$ from the axis, and two are $7\,\mathrm m$ from it. What is the total moment of inertia?
options:
- id: mct-p6-four-block-control-a
  content: |-
    $232\,\mathrm{kg\,m^2}$
  correct: true
  feedback: |-
    The two grouped contributions are $2(2)(3^2)=36$ and $2(2)(7^2)=196\,\mathrm{kg\,m^2}$. Their sum is $232\,\mathrm{kg\,m^2}$.
- id: mct-p6-four-block-control-b
  content: |-
    $116\,\mathrm{kg\,m^2}$
  feedback: |-
    This includes only one mass at each radius: $2(3^2)+2(7^2)=116$. Each radius is shared by two masses, so both contributions must be doubled.
- id: mct-p6-four-block-control-c
  content: |-
    $40\,\mathrm{kg\,m^2}$
  feedback: |-
    This uses unsquared distances: $2(2)(3)+2(2)(7)=40$. Moment of inertia weights each mass by the square of its perpendicular distance.
- id: mct-p6-four-block-control-d
  content: |-
    $200\,\mathrm{kg\,m^2}$
  feedback: |-
    This replaces the two distinct radii by their average, $5\,\mathrm m$, and computes $4(2)(5^2)$. Because squaring is nonlinear, the radii must be squared before their terms are combined.
- id: mct-p6-four-block-control-e
  content: |-
    $464\,\mathrm{kg\,m^2}$
  feedback: |-
    This doubles the multiplicity twice. The factors $2(2)$ in each grouped term already account for two masses of $2\,\mathrm{kg}$.
```

---

<a id="lecture-note-rod-and-point-mass"></a>
## Lecture-Note Extension: Rod and Point Mass

**Paired lecture-note example:** A uniform thin rod has mass $M$ and length $L$. A point mass $3M$ is attached at the far end, and the composite rotates about the rod's opposite end.

Keep the two types of contribution distinct:

- The rod is extended, so use its intrinsic end-axis result:
  $$
  I_{\mathrm{rod}}=\frac13ML^2.
  $$
- The attached object is modeled as a point mass a perpendicular distance $L$ from the axis:
  $$
  I_{\mathrm{point}}=(3M)L^2=3ML^2.
  $$

Add them:

$$
\begin{aligned}
I_{\mathrm{total}}
&=I_{\mathrm{rod}}+I_{\mathrm{point}}\\
&=\frac13ML^2+3ML^2\\
&=\frac{10}{3}ML^2.
\end{aligned}
$$

Do not replace the rod by a point mass at its end or midpoint. Its mass is spread continuously, and that distribution is already contained in $I_{\mathrm{rod}}=\frac13ML^2$.

```quiz
type: radio
id: mct-p6-composite-control
shuffle: true
content: |-
  A uniform thin rod has mass $2.0\,\mathrm{kg}$ and length $3.0\,\mathrm m$. It rotates about one end. A $4.0\,\mathrm{kg}$ point mass is attached at the far end. What is the composite moment of inertia? Use $I_{\mathrm{rod,end}}=\frac13ML^2$.
options:
- id: mct-p6-composite-control-a
  content: |-
    $42\,\mathrm{kg\,m^2}$
  correct: true
  feedback: |-
    The rod contributes $(1/3)(2)(3^2)=6$, and the point mass contributes $(4)(3^2)=36\,\mathrm{kg\,m^2}$. Adding the distinct terms gives $42\,\mathrm{kg\,m^2}$.
- id: mct-p6-composite-control-b
  content: |-
    $36\,\mathrm{kg\,m^2}$
  feedback: |-
    This is only the point-mass contribution $4(3^2)$. The rod also contributes $6\,\mathrm{kg\,m^2}$ about the end axis.
- id: mct-p6-composite-control-c
  content: |-
    $54\,\mathrm{kg\,m^2}$
  feedback: |-
    This treats the entire rod as a $2\,\mathrm{kg}$ point mass at the far end, adding $2(3^2)$ to $4(3^2)$. The rod's distributed-mass term is only $(1/3)(2)(3^2)=6$.
- id: mct-p6-composite-control-d
  content: |-
    $40.5\,\mathrm{kg\,m^2}$
  feedback: |-
    This treats the rod as a point mass at its midpoint, giving $2(1.5^2)=4.5$. A uniform rod's end-axis moment is not obtained by collapsing it to one point; use the supplied $\frac13ML^2$ formula.
- id: mct-p6-composite-control-e
  content: |-
    $18\,\mathrm{kg\,m^2}$
  feedback: |-
    This applies the rod formula to the total $6\,\mathrm{kg}$ mass as though the point mass were spread uniformly along the rod. The rod and attached point mass require separate terms.
```

---

<a id="checks-and-common-traps"></a>
## Checks and Common Traps

- **Axis first:** A distance is meaningless until the rotation axis is identified.
- **Perpendicular distance:** Measure the shortest distance to the axis, not a diagonal or a mass-to-mass separation unless the geometry makes them equal.
- **Zero term:** A point mass on the axis contributes $m(0)^2=0$; it does not make every other term zero.
- **Square before grouping:** Equal masses may have unequal radii. Build the distance ledger before compressing repeated terms.
- **Axis change:** When the axis moves, recompute every $r_\perp$ from the new axis.
- **Dominance check:** A mass twice as far from the axis contributes four times as much if its mass is unchanged.
- **Units:** Each term $mr_\perp^2$ and the final sum have units $\mathrm{kg\,m^2}$.
- **Composite bodies:** Add each component's moment about the same axis, keeping intrinsic rigid-body formulas separate from point-mass terms.

---

<a id="summary"></a>
## Summary

For discrete masses about a chosen axis,

$$
I=\sum_i m_i r_{\perp,i}^2.
$$

1. Mark the axis.
2. Measure each shortest perpendicular distance from that axis.
3. Make a ledger of $m_i$, $r_{\perp,i}$, $r_{\perp,i}^2$, and $m_i r_{\perp,i}^2$.
4. Sum every contribution, including explicit zero terms for masses on the axis.
5. Use symmetry only after confirming which masses share a radius.
6. Rebuild the ledger whenever the axis changes.
7. Report the result in $\mathrm{kg\,m^2}$ and check that farther masses dominate through the $r^2$ weighting.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
