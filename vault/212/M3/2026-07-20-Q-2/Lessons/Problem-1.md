# Ranking Forces in a Massive-Pulley Atwood Machine

## Table of Contents

- [Introduction](#introduction)
- [Compare Tension and Weight on Each Block](#compare-tension-and-weight-on-each-block)
- [Use Pulley Torque to Compare the Tensions](#use-pulley-torque-to-compare-the-tensions)
- [Link the Comparisons into One Ranking](#link-the-comparisons-into-one-ranking)
- [Know When the Tensions Can Be Equal](#know-when-the-tensions-can-be-equal)
- [Summary](#summary)

## Prerequisites

- Identify weight $mg$ and string tension $T$ on a hanging block.
- Use the direction of acceleration to determine the direction of net force.
- Recognize that an angularly accelerating pulley needs a nonzero net torque.

---

<a id="introduction"></a>
## Introduction

When two blocks accelerate on opposite sides of a massive pulley, rank the four forces by building three local comparisons rather than guessing the entire chain at once.

For the pictured system, the larger solid iron block is $m_2$, so $m_2>m_1$. It accelerates downward while $m_1$ accelerates upward. The useful comparisons come from

1. the net force on $m_1$,
2. the net force on $m_2$, and
3. the net torque on the pulley.

The pulley being **massive** is essential: an angularly accelerating pulley with nonzero rotational inertia requires different tensions on its two sides.

Use this comparison map before looking at a full ranking:

| Object | Motion cue | Required comparison |
|---|---|---|
| Rising block $m_1$ | Net force is upward | $T_1>m_1g$ |
| Descending block $m_2$ | Net force is downward | $m_2g>T_2$ |
| Massive pulley | Angular acceleration follows side 2 | $T_2>T_1$ |

Each row settles only one pair. The final ranking comes from joining the pairs that share a force.

---

<a id="compare-tension-and-weight-on-each-block"></a>
## Compare Tension and Weight on Each Block

**Example:** A hanging block of mass $m$ accelerates upward with magnitude $a$. Compare its upward tension $T$ with its downward weight $mg$.

**Explanation**

The acceleration points upward, so the net force must point upward. Taking upward as positive gives

$$
T-mg=ma.
$$

Because $a>0$, the right-hand side is positive. Therefore,

$$
T>mg.
$$

If a block accelerates downward, the same reasoning reverses the comparison: its weight must exceed its tension.

```quiz
type: radio
id: q2a-p1-force-pair
shuffle: true
content: |-
  A hanging block of mass $m$ accelerates upward with magnitude $a>0$. Its only vertical forces are upward tension $T$ and downward weight $mg$. Which comparison is required?
options:
- id: q2a-p1-force-pair-a
  content: |-
    $T>mg$
  correct: true
  feedback: |-
    An upward acceleration requires an upward net force. Since $T-mg=ma>0$, the tension must exceed the weight: $T>mg$.
- id: q2a-p1-force-pair-b
  content: |-
    $T=mg$
  feedback: |-
    Equal upward and downward forces would give zero net force and therefore zero acceleration. Here the block accelerates upward, so $T$ must be greater than $mg$.
- id: q2a-p1-force-pair-c
  content: |-
    $T<mg$
  feedback: |-
    If $T<mg$, the net force would point downward because weight would win. The stated acceleration is upward, so the required relation is $T>mg$.
- id: q2a-p1-force-pair-d
  content: |-
    $T=ma$
  feedback: |-
    The quantity $ma$ equals the net force, not the tension alone. The force equation is $T-mg=ma$, so $T=m(g+a)>mg$.
- id: q2a-p1-force-pair-e
  content: |-
    The forces cannot be compared without knowing the block's speed.
  feedback: |-
    Force comparison depends on acceleration, not speed. The upward acceleration already fixes the net-force direction, so $T>mg$ even though the speed is not given.
```

---

<a id="use-pulley-torque-to-compare-the-tensions"></a>
## Use Pulley Torque to Compare the Tensions

**Example:** In a two-block system, $m_2$ descends and turns a pulley of radius $R$ and moment of inertia $I>0$. Compare $T_2$ with $T_1$.

**Explanation**

The two tensions pull on opposite sides of the pulley. In the direction of the pulley's angular acceleration,

$$
(T_2-T_1)R=I\alpha.
$$

The string does not slip, so $alpha=a/R$. Since the system accelerates, $a>0$, and therefore

$$
T_2-T_1=rac{I}{R^2}a>0.
$$

Thus,

$$
T_2>T_1.
$$

```quiz
type: radio
id: q2a-p1-pulley-torque
shuffle: true
content: |-
  A string does not slip on a pulley with $I>0$. Block $m_2$ accelerates downward, turning the pulley in that direction. Which tension relation supplies the required pulley torque?
options:
- id: q2a-p1-pulley-torque-a
  content: |-
    $T_2>T_1$
  correct: true
  feedback: |-
    The pulley needs net torque in the direction caused by the descending $m_2$ side. With $(T_2-T_1)R=I\alpha>0$, the required relation is $T_2>T_1$.
- id: q2a-p1-pulley-torque-b
  content: |-
    $T_2=T_1$
  feedback: |-
    Equal tensions would give zero net torque on the pulley. That can fit an ideal massless pulley or zero angular acceleration, but not this pulley with $I>0$ and $\alpha\ne0$.
- id: q2a-p1-pulley-torque-c
  content: |-
    $T_2<T_1$
  feedback: |-
    This difference would torque the pulley opposite the rotation produced by $m_2$ descending. The stated angular acceleration requires $(T_2-T_1)R>0$, so $T_2>T_1$.
- id: q2a-p1-pulley-torque-d
  content: |-
    $T_2=m_2g$
  feedback: |-
    If $T_2=m_2g$, block $m_2$ would have zero net force and zero acceleration. Because it accelerates downward, $m_2g-T_2=m_2a>0$, so $T_2<m_2g$; the pulley equation separately gives $T_2>T_1$.
- id: q2a-p1-pulley-torque-e
  content: |-
    The tensions cannot be compared unless $I$ and $R$ are known numerically.
  feedback: |-
    Numerical values are unnecessary for the ordering. Since $I>0$, $R>0$, and $\alpha$ has the direction driven by side 2, $(T_2-T_1)R=I\alpha$ fixes $T_2>T_1$.
```

---

<a id="link-the-comparisons-into-one-ranking"></a>
## Link the Comparisons into One Ranking

**Example:** A string passing over a massive pulley connects two solid iron blocks, causing the system to accelerate. Assume there is no friction or air resistance. Rank $m_1g$, $T_1$, $m_2g$, and $T_2$ for the system shown.

![](<../Source/2026-07-20-Q-2/Images/problem-1-massive-pulley-atwood-machine.png>)

**Explanation**

The larger block $m_2$ descends, so its downward weight exceeds its upward tension:

$$
m_2g>T_2.
$$

The smaller block $m_1$ rises, so its upward tension exceeds its downward weight:

$$
T_1>m_1g.
$$

The massive pulley accelerates in the direction driven by side 2, so

$$
T_2>T_1.
$$

The comparisons share endpoints and link directly:

$$
\boxed{m_2g>T_2>T_1>m_1g}.
$$

To test a proposed ranking, check its adjacent claims one at a time:

1. Does it place $m_2g$ above $T_2$?
2. Does it place $T_2$ above $T_1$?
3. Does it place $T_1$ above $m_1g$?

A choice that fails even one check cannot describe the system. Once all three checks pass, write the chain from greatest to least.

```quiz
type: radio
id: q2a-p1-full-ranking
shuffle: true
content: |-
  **Question 1**

  A string passing over a massive pulley connects two solid iron blocks, causing the system to accelerate. Assume there is no friction or air resistance. Rank the four forces in the system.

  ![](<../Source/2026-07-20-Q-2/Images/problem-1-massive-pulley-atwood-machine.png>)
options:
- id: q2a-p1-full-ranking-a
  content: |-
    $m_1g=T_1=m_2g=T_2$
  feedback: |-
    Making every force equal would give zero net force on both blocks and zero net torque on the pulley. The system accelerates, so the block force pairs and the two tensions cannot all be equal.
- id: q2a-p1-full-ranking-b
  content: |-
    $T_2>m_2g>T_1>m_1g$
  feedback: |-
    This reverses the force comparison on the descending block. Since $m_2$ accelerates downward, $m_2g-T_2=m_2a>0$, so $m_2g>T_2$, not $T_2>m_2g$.
- id: q2a-p1-full-ranking-c
  content: |-
    $T_2=T_1>m_2g>m_1g$
  feedback: |-
    A massive pulley with angular acceleration needs a nonzero torque, so its tensions cannot be equal. Also, downward acceleration of $m_2$ requires $m_2g>T_2$, whereas this choice places $T_2$ above $m_2g$.
- id: q2a-p1-full-ranking-d
  content: |-
    $m_2g>m_1g>T_1=T_2$
  feedback: |-
    The rising block requires $T_1-m_1g=m_1a>0$, so $T_1>m_1g$, not $m_1g>T_1$. Equal tensions would also leave the massive accelerating pulley with no net torque.
- id: q2a-p1-full-ranking-e
  content: |-
    $m_2g>T_2>T_1>m_1g$
  correct: true
  feedback: |-
    Downward acceleration of $m_2$ gives $m_2g>T_2$, pulley angular acceleration gives $T_2>T_1$, and upward acceleration of $m_1$ gives $T_1>m_1g$. Linking those comparisons yields $m_2g>T_2>T_1>m_1g$.
- id: q2a-p1-full-ranking-f
  content: |-
    $m_2g>T_2=T_1>m_1g$
  feedback: |-
    The block comparisons are consistent with the motion, but $T_2=T_1$ would give zero net pulley torque. This equality is the massless-pulley limit; the stated massive pulley needs $T_2>T_1$ while it accelerates.
- id: q2a-p1-full-ranking-g
  content: |-
    $m_2g>T_2>m_1g>T_1$
  feedback: |-
    This places the rising block's weight above its tension. Upward acceleration instead requires $T_1-m_1g=m_1a>0$, so $T_1>m_1g$; together with $T_2>T_1$, both tensions lie above $m_1g$.
- id: q2a-p1-full-ranking-h
  content: |-
    $m_2g>m_1g>T_2>T_1$
  feedback: |-
    Since $m_1$ accelerates upward, $T_1>m_1g$. Because the pulley also requires $T_2>T_1$, it follows that $T_2>T_1>m_1g$, so $m_1g$ cannot lie above either tension.
```

---

<a id="know-when-the-tensions-can-be-equal"></a>
## Know When the Tensions Can Be Equal

**Example:** Replace the massive pulley with an ideal massless, frictionless pulley while the same two blocks accelerate. How does the ranking change?

**Explanation**

The block equations do not change:

$$
m_2g>T_2
\qquad\text{and}\qquad
T_1>m_1g.
$$

For an ideal massless pulley, however, no tension difference is needed to produce angular acceleration. A massless string over that pulley has one common tension:

$$
T_2=T_1.
$$

The limiting-case ranking is therefore

$$
m_2g>T_2=T_1>m_1g.
$$

The word **frictionless** alone does not make the tensions equal. A frictionless pulley can still be massive and require net torque.

```quiz
type: radio
id: q2a-p1-massless-limit
shuffle: true
content: |-
  Blocks $m_2>m_1$ accelerate on a massless string over an ideal massless, frictionless pulley, with $m_2$ descending. Which ranking is correct?
options:
- id: q2a-p1-massless-limit-a
  content: |-
    $m_2g>T_2=T_1>m_1g$
  correct: true
  feedback: |-
    The descending block gives $m_2g>T_2$, the rising block gives $T_1>m_1g$, and an ideal massless pulley gives $T_2=T_1$. Thus $m_2g>T_2=T_1>m_1g$.
- id: q2a-p1-massless-limit-b
  content: |-
    $m_2g>T_2>T_1>m_1g$
  feedback: |-
    Unequal tensions supply torque to a pulley with rotational inertia. Here the pulley is ideal and massless, so the string tension is the same on both sides: $T_2=T_1$.
- id: q2a-p1-massless-limit-c
  content: |-
    $m_2g>m_1g>T_2=T_1$
  feedback: |-
    The rising block must have upward net force, so $T_1>m_1g$. This choice puts its weight above the common tension and would make $m_1$ accelerate downward.
- id: q2a-p1-massless-limit-d
  content: |-
    $m_2g=T_2=T_1=m_1g$
  feedback: |-
    Equal force pairs on both blocks would mean zero acceleration. The pulley is massless, so the tensions match each other, but the descending and rising blocks still require $m_2g>T$ and $T>m_1g$.
- id: q2a-p1-massless-limit-e
  content: |-
    $T_2=T_1>m_2g>m_1g$
  feedback: |-
    A descending $m_2$ requires its downward weight to exceed the upward tension: $m_2g>T_2$. The massless pulley makes the tensions equal but does not reverse this block-force comparison.
```

---

<a id="summary"></a>
## Summary

For a two-block system with $m_2$ descending and $m_1$ rising:

1. Descending block: $m_2g>T_2$.
2. Rising block: $T_1>m_1g$.
3. Massive accelerating pulley: $T_2>T_1$.
4. Link the shared quantities: $m_2g>T_2>T_1>m_1g$.

The main trap is carrying over $T_1=T_2$ from an ideal massless pulley. A frictionless axle removes resisting axle torque; it does not remove the rotational inertia of a massive pulley.
