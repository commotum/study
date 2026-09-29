# Changing Slit Separation at a Fixed Fringe Angle

<!--
lesson-id: 212-M6-016
topic-code: MTH212.M6.16
-->
## Table of Contents

- [Introduction](#introduction)
- [Translate Fringe Labels Into Path Differences](#translate-fringe-labels)
- [Compare Conditions at One Angle](#compare-fixed-angle-conditions)
- [Use a Direction Check](#direction-check)
- [Apply the Full Method](#apply-the-method)
- [Summary](#summary)

## Prerequisites

- Distinguish constructive (bright) interference from destructive (dark) interference.
- Simplify fractions and solve a proportion.
- Recognize that the same angle gives the same value of $\sin\theta$.

---

<a id="introduction"></a>
## Introduction

When a double-slit problem changes the slit separation but requires a new fringe to stay at the **same angle**, compare the two path-difference conditions. The important cue is “same angle”: with the wavelength unchanged, it lets the common factors $\sin\theta$ and $\lambda$ cancel.

In the comparison,

- $d$ is the original slit separation,
- $d'$ is the new slit separation,
- $\theta$ is the shared observation angle, and
- $C$ is the numerical multiplier that identifies the named bright or dark fringe in a path difference $C\lambda$.

The procedure is:

1. Translate each named fringe into its path difference in multiples of $\lambda$.
2. Write one condition for the original separation and one for the new separation.
3. Divide the new condition by the original condition.
4. Check whether the resulting change in separation has the right direction.

---

<a id="translate-fringe-labels"></a>
## Translate Fringe Labels Into Path Differences

For double-slit interference, bright maxima satisfy

$$
d\sin\theta=m\lambda,
$$

where the order is $m=0,1,2,\ldots$. Thus a fourth-order bright maximum has path difference $4\lambda$.

Dark fringes lie halfway between bright orders. If $n=1,2,3,\ldots$ counts dark fringes outward from the central maximum on one side, then

$$
d\sin\theta=\left(n-\frac12\right)\lambda.
$$

Equivalently, first translate the fringe label into its multiplier $C$:

| Fringe label | Multiplier in $d\sin\theta=C\lambda$ |
| --- | --- |
| $m$th-order bright maximum | $C=m$ |
| $n$th dark fringe | $C=n-\dfrac12$ |

**Example:** Translate a fourth-order bright maximum and the third dark fringe into path differences.

**Explanation**

For the bright maximum, use $m=4$, giving $4\lambda$. For the third dark fringe, use $n=3$:

$$
\left(3-\frac12\right)\lambda=\frac52\lambda.
$$

The word “third” enters the two formulas differently: bright order $m=3$ gives $3\lambda$, while the third dark fringe gives $5\lambda/2$.

```quiz
type: radio
id: p6-fringe-labels
content: |-
  Which pair correctly gives the path differences for a third-order bright maximum and the fifth dark fringe, respectively?
options:
- id: p6-fringe-labels-a
  content: |-
    $3\lambda$ and $\dfrac{9\lambda}{2}$
  correct: true
  feedback: |-
    A bright maximum of order $m$ has path difference $m\lambda$, so third order gives $3\lambda$. The $n$th dark fringe has path difference $(n-1/2)\lambda$, so the fifth dark fringe gives $(5-1/2)\lambda=9\lambda/2$.
- id: p6-fringe-labels-b
  content: |-
    $3\lambda$ and $\dfrac{11\lambda}{2}$
  feedback: |-
    The bright value is correct, but $11\lambda/2$ comes from adding one-half to the dark-fringe count. The first dark fringe is already at $\lambda/2$, so the fifth is $(5-1/2)\lambda=9\lambda/2$.
- id: p6-fringe-labels-c
  content: |-
    $3\lambda$ and $5\lambda$
  feedback: |-
    Integer multiples of $\lambda$ locate bright maxima. Dark fringes occur at half-integer multiples, so the fifth dark fringe is $9\lambda/2$, not $5\lambda$.
- id: p6-fringe-labels-d
  content: |-
    $2\lambda$ and $\dfrac{9\lambda}{2}$
  feedback: |-
    The dark-fringe value is correct, but bright order is the integer $m$ in $m\lambda$. The central maximum has $m=0$; “third-order” explicitly means $m=3$, so its path difference is $3\lambda$.
```

---

<a id="compare-fixed-angle-conditions"></a>
## Compare Conditions at One Angle

Write each interference condition as a numerical multiplier of the wavelength:

$$
d\sin\theta=C_i\lambda,
\qquad
d'\sin\theta=C_f\lambda.
$$

Here $C_i$ is the original fringe multiplier and $C_f$ is the target fringe multiplier. Keep the comparison in the same order—new over original—on both sides:

$$
\frac{d'\sin\theta}{d\sin\theta}
=
\frac{C_f\lambda}{C_i\lambda}.
$$

For the same nonzero angle and the same wavelength, the common factors cancel:

$$
\frac{d'}{d}=\frac{C_f}{C_i}.
$$

The nonzero-angle condition matters when dividing by $\sin\theta$. In the homework problem, an off-center second-order maximum guarantees $\sin\theta\ne0$.

**Example:** A third-order bright maximum for separation $d$ is to be replaced at the same angle by the second dark fringe. Find $d'$.

**Explanation**

The original multiplier is $C_i=3$. The second dark fringe has multiplier

$$
C_f=2-\frac12=\frac32.
$$

Therefore,

$$
\frac{d'}{d}=\frac{3/2}{3}=\frac12,
\qquad
d'=\frac d2.
$$

```quiz
type: radio
id: p6-fixed-angle-ratio
content: |-
  A first-order bright maximum occurs at angle $\theta$ for slit separation $d$. What new separation $d'$ places the fourth dark fringe at the same angle?
options:
- id: p6-fixed-angle-ratio-a
  content: |-
    $\dfrac{7d}{2}$
  correct: true
  feedback: |-
    First-order bright means $C_i=1$, while the fourth dark fringe has $C_f=4-1/2=7/2$. At the same angle and wavelength, $d'/d=C_f/C_i=(7/2)/1$, so $d'=7d/2$.
- id: p6-fixed-angle-ratio-b
  content: |-
    $\dfrac{2d}{7}$
  feedback: |-
    This inverts the comparison. Dividing the new condition by the original gives $d'/d=C_f/C_i$, not $C_i/C_f$. Since $7/2$ is larger than $1$, the new separation must be larger than $d$.
- id: p6-fixed-angle-ratio-c
  content: |-
    $4d$
  feedback: |-
    This treats the fourth dark fringe as path difference $4\lambda$, but integer multiples locate bright maxima. The fourth dark fringe is at $(4-1/2)\lambda=7\lambda/2$, giving $d'=7d/2$.
- id: p6-fixed-angle-ratio-d
  content: |-
    $d$
  feedback: |-
    Keeping $d'=d$ preserves the original path difference at the fixed angle, so the point remains a first-order bright maximum. Changing the fringe type from multiplier $1$ to $7/2$ requires the separation to change by the same ratio.
```

---

<a id="direction-check"></a>
## Use a Direction Check

Before simplifying the ratio, compare the two fringe multipliers:

- If $C_f>C_i$, then $d'>d$.
- If $C_f<C_i$, then $d'<d$.
- If $C_f=C_i$, then $d'=d$.

This follows directly from $d'/d=C_f/C_i$ and catches a reversed fraction.

**Example:** A fourth-order bright maximum is replaced at the same angle by the second dark fringe.

**Explanation**

The multiplier falls from $4$ to $3/2$, so the new separation must be smaller. The exact ratio confirms the prediction:

$$
\frac{d'}{d}=\frac{3/2}{4}=\frac38.
$$

```quiz
type: radio
id: p6-direction-check
content: |-
  A second-order bright maximum for separation $d$ is to be replaced at the same angle by the fifth dark fringe. Before doing the full calculation, what must be true?
options:
- id: p6-direction-check-a
  content: |-
    $d'>d$
  correct: true
  feedback: |-
    The original multiplier is $2$, while the fifth dark fringe has multiplier $5-1/2=9/2$. Because the target multiplier is larger, $d'/d=(9/2)/2>1$, so $d'>d$.
- id: p6-direction-check-b
  content: |-
    $d'<d$
  feedback: |-
    A smaller separation would produce a smaller path difference at the unchanged angle. Here the target path difference rises from $2\lambda$ to $9\lambda/2$, so the separation must increase, not decrease.
- id: p6-direction-check-c
  content: |-
    $d'=d$
  feedback: |-
    Equal separations would give equal path differences at the same angle. The fringe multipliers are not equal: the condition changes from $2\lambda$ to $9\lambda/2$, so $d'$ cannot equal $d$.
- id: p6-direction-check-d
  content: |-
    The direction cannot be determined without knowing $\theta$.
  feedback: |-
    The numerical angle is unnecessary because the same $\sin\theta$ appears in both conditions and cancels. Comparing the multipliers $2$ and $9/2$ already shows that the new separation must be larger.
```

---

<a id="apply-the-method"></a>
## Apply the Full Method

**Example:** A third-order bright maximum occurs at angle $\theta$ for separation $d$. Find the new separation that puts the fourth dark fringe at the same angle.

**Explanation**

Translate the two fringe labels:

$$
C_i=3,
\qquad
C_f=4-\frac12=\frac72.
$$

Then divide the fixed-angle conditions:

$$
\frac{d'}{d}=\frac{7/2}{3}=\frac76,
\qquad
d'=\frac{7d}{6}.
$$

The target multiplier is slightly larger than the original multiplier, so a result slightly larger than $d$ passes the direction check.

```quiz
type: radio
id: p6-homework-transfer
shuffle: true
content: |-
  A double slit initially has separation $d$. Its second-order bright maximum occurs at angle $\theta$.

  The slit separation is then changed to $d'$. What must $d'$ be so that the **third dark fringe** occurs at the same angle $\theta$?
options:
- id: p6-homework-transfer-a
  content: |-
    $\dfrac{4d}{5}$
  feedback: |-
    This reverses the required ratio. At the shared angle, the original second bright maximum corresponds to $2\lambda$, while the third dark fringe corresponds to $5\lambda/2$. The new separation must therefore be larger, not smaller, than $d$.
- id: p6-homework-transfer-b
  content: |-
    $d$
  feedback: |-
    If the separation remains $d$, then the same angle still satisfies $d\sin\theta=2\lambda$, so it remains the second bright maximum rather than becoming the third dark fringe.
- id: p6-homework-transfer-c
  content: |-
    $\dfrac{5d}{4}$
  correct: true
  feedback: |-
    The original maximum gives $d\sin\theta=2\lambda$. The third dark fringe gives $d'\sin\theta=5\lambda/2$. Dividing the equations at the same angle yields $d'/d=(5/2)/2=5/4$, so $d'=5d/4$.
- id: p6-homework-transfer-d
  content: |-
    $\dfrac{3d}{2}$
  feedback: |-
    With $d'=3d/2$, the shared-angle path difference would be $d'\sin\theta=(3/2)(2\lambda)=3\lambda$. That is a third-order bright maximum, not the third dark fringe.
```

---

<a id="summary"></a>
## Summary

When a fringe must stay at the same angle after the slit separation changes:

1. Use $C_i=m$ for an $m$th-order bright maximum.
2. Use $C_f=n-1/2$ for the $n$th dark fringe.
3. Divide the two conditions to get

   $$
   \frac{d'}{d}=\frac{C_f}{C_i}.
   $$

4. Compare $C_f$ with $C_i$ to check whether $d'$ should be larger or smaller than $d$.

This ratio shortcut assumes the wavelength is unchanged and the shared angle is nonzero.

The main trap is dark-fringe indexing: the first dark fringe is at $\lambda/2$, so the third dark fringe is at $5\lambda/2$, not $3\lambda$ or $7\lambda/2$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
