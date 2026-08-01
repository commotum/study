# Scaling Force With an Inverse-Square Law

## Table of Contents

- [Introduction](#introduction)
- [Recognize the Inverse-Square Dependence](#recognize-the-inverse-square-dependence)
- [Replace the Distance by a Scale Factor](#replace-the-distance-by-a-scale-factor)
- [Handle a Decrease in Distance](#handle-a-decrease-in-distance)
- [Apply the Rule to Gravitational Force](#apply-the-rule-to-gravitational-force)
- [Summary](#summary)

## Prerequisites

- Evaluate squares of whole numbers and fractions.
- Substitute an expression such as $2r$ for a variable.
- Simplify a fraction by factoring a constant from its denominator.

---

<a id="introduction"></a>
## Introduction

When the masses stay fixed and only their separation changes, Newton's law of gravitation is an **inverse-square law**. The cue is a statement that the distance becomes some multiple of its original value.

If the distance changes from $r$ to $kr$, replace $r$ by $kr$ everywhere in the denominator. The force then changes by the factor

$$
\boxed{\frac{F_{\text{new}}}{F_{\text{old}}}=\frac{1}{k^2}}.
$$

The square applies to the entire distance scale factor. This lets you compare the forces without knowing either mass or the value of $G$.

Before calculating, predict the direction of the change: increasing $r$ must decrease $F$, while decreasing $r$ must increase $F$. This catches a reversed ratio immediately.

---

<a id="recognize-the-inverse-square-dependence"></a>
## Recognize the Inverse-Square Dependence

**Example:** Two fixed masses are separated by a distance $r$. Identify the part of Newton's law that controls how the force changes when only $r$ changes.

**Explanation**

Newton's law gives

$$
F=\frac{Gm_1m_2}{r^2}.
$$

Because $G$, $m_1$, and $m_2$ do not change, combine them into one constant $K$:

$$
F=\frac{K}{r^2}.
$$

Thus $F$ is proportional to $1/r^2$. A larger distance produces a smaller force, and the exponent $2$ determines the scale factor.

```quiz
type: radio
id: m3-1-p1-recognize-law
content: |-
  The source strength in a physical law stays fixed while a measured quantity $I$ depends on distance $d$ according to $I=K/d^2$. Which statement correctly describes the dependence?
options:
- id: a
  content: |-
    $I$ is inversely proportional to the square of $d$.
  correct: true
- id: b
  content: |-
    $I$ is inversely proportional to $d$.
- id: c
  content: |-
    $I$ is directly proportional to the square of $d$.
- id: d
  content: |-
    $I$ does not depend on $d$.
- id: e
  content: |-
    $I$ is directly proportional to $d$.
feedback: |-
  The variable $d$ is squared in the denominator, so $I\propto 1/d^2$. Do not drop the exponent or reverse the relationship.
```

---

<a id="replace-the-distance-by-a-scale-factor"></a>
## Replace the Distance by a Scale Factor

**Example:** A force has magnitude $F$ at distance $r$. Find the force when the distance becomes $3r$.

**Explanation**

Use the same three-line pattern each time:

1. Write the new distance as $kr$.
2. Substitute the entire expression $kr$ for $r$.
3. Square both factors before simplifying.

Write the old and new forces using the same constant numerator $K$:

$$
F_{\text{old}}=\frac{K}{r^2},
\qquad
F_{\text{new}}=\frac{K}{(3r)^2}.
$$

Square both factors in the product $3r$:

$$
(3r)^2=3^2r^2=9r^2.
$$

Therefore,

$$
F_{\text{new}}
=\frac{K}{9r^2}
=\frac19F_{\text{old}}.
$$

The distance increased, so the smaller force is a useful direction check.

In general, taking the ratio cancels every fixed quantity:

$$
\frac{F_{\text{new}}}{F_{\text{old}}}
=\frac{K/(kr)^2}{K/r^2}
=\frac{1}{k^2}.
$$

| Distance change | $k$ | Force change $1/k^2$ |
|---|---:|---:|
| doubled | $2$ | $1/4$ |
| tripled | $3$ | $1/9$ |
| halved | $1/2$ | $4$ |
| reduced to one-third | $1/3$ | $9$ |

```quiz
type: radio
id: m3-1-p1-scale-increase
content: |-
  A force follows an inverse-square law. If the distance becomes four times as large while all other quantities remain fixed, what is the new force?
options:
- id: a
  content: |-
    $F/16$
  correct: true
- id: b
  content: |-
    $F/4$
- id: c
  content: |-
    $4F$
- id: d
  content: |-
    $16F$
- id: e
  content: |-
    $F$
feedback: |-
  Here $k=4$, so $F_{\text{new}}=F/k^2=F/16$. The distractor $F/4$ comes from forgetting to square the distance factor.
```

---

<a id="handle-a-decrease-in-distance"></a>
## Handle a Decrease in Distance

**Example:** A force has magnitude $F$ at distance $r$. Find the force when the distance becomes $r/2$.

**Explanation**

The new distance is $kr$ with $k=1/2$. Apply the same scale-factor rule:

$$
\begin{aligned}
F_{\text{new}}
&=\frac{1}{(1/2)^2}F\\
&=4F.
\end{aligned}
$$

Decreasing the distance must increase the force. The rule has not changed; only the scale factor is now less than $1$.

```quiz
type: radio
id: m3-1-p1-scale-decrease
content: |-
  A force follows an inverse-square law. If the distance is reduced to one-third of its original value, what is the new force?
options:
- id: a
  content: |-
    $9F$
  correct: true
- id: b
  content: |-
    $3F$
- id: c
  content: |-
    $F/3$
- id: d
  content: |-
    $F/9$
- id: e
  content: |-
    $F$
feedback: |-
  The scale factor is $k=1/3$, so $F_{\text{new}}=F/(1/3)^2=9F$. A shorter distance must produce a larger force.
```

---

<a id="apply-the-rule-to-gravitational-force"></a>
## Apply the Rule to Gravitational Force

**Example:** Two planets move twice as far apart while their masses remain unchanged. Determine the new gravitational force in terms of the original force $F$.

**Explanation**

The distance scale factor is $k=2$. Substitute $2r$ for $r$:

$$
\begin{aligned}
F_{\text{new}}
&=\frac{Gm_1m_2}{(2r)^2}\\
&=\frac{Gm_1m_2}{4r^2}\\
&=\frac14F.
\end{aligned}
$$

The factor $2$ is squared because the full distance appears as $r^2$ in the denominator.

A quick check completes the reasoning: twice the distance is farther away, and $F/4$ is less than $F$. Answers such as $2F$ or $4F$ fail this direction check, while $F/2$ forgets the square.

```quiz
type: radio
id: m3-1pre-q1
shuffle: true
content: |-
  **Question 1**

  Two planets of masses $m_1$ and $m_2$ are separated by a distance $r$ and experience a gravitational force of magnitude $F$. How does the force change if the planets move twice as far apart?
options:
- id: a
  content: The new force is one-fourth the original force
  correct: true
  feedback: Newton's law of gravitation gives $F=Gm_1m_2/r^2$. Replacing $r$ with $2r$ gives $F_{\mathrm{new}}=F/4$.
- id: b
  content: The new force is one-half the original force
- id: c
  content: The new force is the same as the original force
- id: d
  content: The new force is twice the original force
- id: e
  content: The new force is four times the original force
```

---

## Summary

- **Cue:** the masses stay fixed while the separation changes by a scale factor.
- **Rule:** if $r\to kr$, then $F\to F/k^2$.
- **Procedure:** identify $k$, substitute $(kr)^2$ for $r^2$, expand it as $k^2r^2$, and multiply the old force by $1/k^2$.
- **Direction check:** greater distance means less force; smaller distance means greater force.
- **Main trap:** doubling the distance gives $F/4$, not $F/2$.
