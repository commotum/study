# Atwood-Machine Acceleration With a Massless Pulley

<!--
lesson-id: 212-M2-051
topic-code: MTH212.M2.51
-->

## Table of Contents

- [Introduction](#introduction)
- [Assign the Shared Motion and Tension](#assign-the-shared-motion-and-tension)
- [Write One Force Equation for Each Mass](#write-one-force-equation-for-each-mass)
- [Add the Equations to Eliminate Tension](#add-the-equations-to-eliminate-tension)
- [Check the Limiting Cases](#check-the-limiting-cases)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Apply Newton's second law along one dimension: $\sum F=ma$.
- Know that a hanging mass $m$ has downward weight $mg$.
- Use the motion constraint of a connected two-mass system: the masses have the same acceleration magnitude in opposite directions.
- Add two linear equations to eliminate a variable with opposite coefficients.

---

<a id="introduction"></a>
## Introduction

Masses $m_1$ and $m_2$ are connected over a massless, frictionless pulley, with $m_2>m_1$. The requested answer is the symbolic acceleration magnitude.

![](<../Source/Images/atwood1.jpg>)

Because $m_2$ is heavier, it accelerates downward while $m_1$ accelerates upward. The connection gives both masses the same acceleration magnitude $a$. The massless, frictionless pulley permits one common tension $T$ on the two sides.

The key move is to choose positive along each mass's motion, write one force equation for each mass, and add the equations. The $+T$ and $-T$ terms then cancel, leaving one equation for $a$.

Use this short elimination routine:

1. Name the two unknowns in the force equations: $T$ and $a$.
2. Check that the common tension has coefficients $-1$ and $+1$.
3. Add the equations without multiplying either one, then isolate $a$.
4. Check that the result is compatible with both original force equations and with $0<a<g$.

---

<a id="assign-the-shared-motion-and-tension"></a>
## Assign the Shared Motion and Tension

**Example:** For $m_2>m_1$, assign the motion direction, acceleration magnitude, and tension label on each side of the pulley.

**Explanation**

The unequal weights drive the heavier mass $m_2$ downward and the lighter mass $m_1$ upward. Since the masses are connected, their acceleration magnitudes match:

$$
|a_1|=|a_2|=a.
$$

Their acceleration vectors point in opposite vertical directions, but the same positive scalar $a$ can appear in both equations when positive is chosen along each mass's own motion. For the massless, frictionless pulley in this problem, use the same tension magnitude $T$ on both sides.

```quiz
type: radio
id: atwood-shared-motion-and-tension
shuffle: true
content: |-
  Masses $M$ and $m$ are connected over a massless, frictionless pulley, with $M>m$. Which description is correct?
options:
- id: heavy-down-light-up-shared
  content: |-
    $M$ accelerates down, $m$ accelerates up, both have magnitude $a$, and both sides have tension $T$.
  correct: true
  feedback: |-
    The larger weight makes $M$ descend and $m$ rise. The connection fixes equal acceleration magnitudes, and the ideal massless pulley permits the same tension $T$ on both sides.
- id: both-down
  content: |-
    Both masses accelerate downward with magnitude $a$, and both sides have tension $T$.
  feedback: |-
    Each mass feels gravity downward, but the connection forces the two ends to move in opposite directions. When the heavier mass descends, the lighter mass must rise with the same acceleration magnitude.
- id: heavy-up-light-down
  content: |-
    $M$ accelerates up and $m$ accelerates down, both with magnitude $a$.
  feedback: |-
    This reverses the direction set by the weight imbalance. With $M>m$, the net gravitational drive is $(M-m)g$ toward the $M$ side, so $M$ moves down and $m$ moves up.
- id: unequal-accelerations
  content: |-
    $M$ accelerates down faster than $m$ accelerates up because $M$ is heavier.
  feedback: |-
    The masses have different forces, but the connection constrains their displacements and therefore their acceleration magnitudes to match. The heavier mass does not move through more cord than the lighter mass.
- id: unequal-tensions
  content: |-
    $M$ accelerates down and $m$ accelerates up with the same magnitude, but the tension is larger on the $m$ side.
  feedback: |-
    Unequal tensions are needed to angularly accelerate a pulley with rotational inertia. This pulley is massless and frictionless, so the problem's ideal model uses one common tension $T$.
```

---

<a id="write-one-force-equation-for-each-mass"></a>
## Write One Force Equation for Each Mass

**Example:** Write Newton's second law for $m_2$ and $m_1$ using positive along each mass's direction of motion.

**Explanation**

For $m_2$, positive is downward. Its weight points positive and tension points negative:

$$
m_2g-T=m_2a \tag{1}
$$

For $m_1$, positive is upward. Tension points positive and weight points negative:

$$
T-m_1g=m_1a \tag{2}
$$

These sign choices make $a$ the same positive magnitude in both equations. Each inertial term must contain the mass belonging to that free-body diagram. Equations (1) and (2) are already arranged for elimination because the coefficients of the same unknown $T$ are opposites.

```quiz
type: radio
id: atwood-two-force-equations
shuffle: true
content: |-
  An ideal Atwood machine has $M>m$. Positive is chosen downward for $M$ and upward for $m$. Which pair of equations is correct?
options:
- id: mg-minus-t-and-t-minus-mg
  content: |-
    $Mg-T=Ma$ and $T-mg=ma$
  correct: true
  feedback: |-
    Along $M$'s downward motion, weight is positive and tension is negative. Along $m$'s upward motion, tension is positive and weight is negative, so both right sides contain the same positive acceleration magnitude $a$.
- id: both-weight-minus-tension
  content: |-
    $Mg-T=Ma$ and $mg-T=ma$
  feedback: |-
    The first equation matches downward-positive for $M$, but the second uses downward-positive forces while keeping $+a$ for a mass that accelerates upward. With upward positive for $m$, its equation is $T-mg=ma$.
- id: directions-reversed
  content: |-
    $T-Mg=Ma$ and $mg-T=ma$
  feedback: |-
    These equations choose positive opposite the actual motion of each mass while still writing a positive $a$. For $M>m$, use downward positive for $M$ and upward positive for $m$.
- id: add-forces
  content: |-
    $Mg+T=Ma$ and $T+mg=ma$
  feedback: |-
    Weight and tension point in opposite directions on each hanging mass, so they cannot both have the same sign in one one-dimensional force equation. The signs must follow the chosen axis.
- id: swapped-inertial-masses
  content: |-
    $Mg-T=ma$ and $T-mg=Ma$
  feedback: |-
    The force equation for each free-body diagram must use that object's own inertial mass. The equation for $M$ ends in $Ma$, while the equation for $m$ ends in $ma$.
```

---

<a id="add-the-equations-to-eliminate-tension"></a>
## Add the Equations to Eliminate Tension

**Example:** Use the two mass equations to find the acceleration magnitude.

**Explanation**

Place the equations together and add corresponding sides:

$$
\begin{aligned}
m_2g-T&=m_2a,\\
T-m_1g&=m_1a.
\end{aligned}
$$

The common tension is internal to the two-mass system, and its coefficients add to zero without any preliminary algebra:

$$
(m_2g-T)+(T-m_1g)=m_2a+m_1a.
$$

Thus $-T+T=0$, and the remaining terms give

$$
(m_2-m_1)g=(m_1+m_2)a.
$$

Now isolate the requested magnitude:

$$
\boxed{a=\frac{(m_2-m_1)g}{m_1+m_2}}.
$$

The difference of the masses sets the gravitational driving force, while the sum of the masses is the total inertia being accelerated.

As a system check, substitute this $a$ into either original equation. Equation (2) gives

$$
T=m_1(g+a)
=\frac{2m_1m_2g}{m_1+m_2},
$$

and equation (1) gives the same tension. Agreement confirms that the acceleration satisfies both free-body equations; tension is only a check here, not an additional requested answer.

```quiz
type: radio
id: atwood-numerical-acceleration
shuffle: true
content: |-
  An ideal Atwood machine has $m_1=2.0\ \mathrm{kg}$ and $m_2=5.0\ \mathrm{kg}$. Using $g=9.8\ \mathrm{m}/\mathrm{s}^2$, what is the acceleration magnitude?
options:
- id: four-point-two
  content: |-
    $4.2\ \mathrm{m}/\mathrm{s}^2$
  correct: true
  feedback: |-
    Adding the two force equations removes the common tension, so $a=(m_2-m_1)g/(m_1+m_2)$. Substitution gives $a=(3.0/7.0)(9.8)=4.2\ \mathrm{m}/\mathrm{s}^2$.
- id: five-point-nine
  content: |-
    $5.9\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    This divides the driving force by $m_2$ alone. Both masses accelerate, so the inertia in the denominator is $m_1+m_2=7.0\ \mathrm{kg}$, not just $5.0\ \mathrm{kg}$.
- id: fourteen-point-seven
  content: |-
    $14.7\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    This divides by $m_1$ alone and even produces an acceleration greater than free fall. The connected system must accelerate both masses, so the denominator is their sum and the result is below $g$.
- id: nine-point-eight
  content: |-
    $9.8\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    The heavier mass is not in free fall because the cord tension pulls upward and also accelerates the lighter mass. Only in the limiting case $m_1\to0$ does the acceleration approach $g$.
- id: twenty-nine-point-four
  content: |-
    $29.4\ \mathrm{m}/\mathrm{s}^2$
  feedback: |-
    The value $(m_2-m_1)g=29.4\ \mathrm{N}$ is the net driving force, not the acceleration. Dividing that force by the total mass $7.0\ \mathrm{kg}$ gives $4.2\ \mathrm{m}/\mathrm{s}^2$.
```

---

<a id="check-the-limiting-cases"></a>
## Check the Limiting Cases

**Example:** Test the acceleration formula when the masses become equal and when the lighter mass approaches zero.

**Explanation**

If the masses are equal, their weights balance:

$$
m_2=m_1
\qquad\Longrightarrow\qquad
a=0.
$$

If the lighter mass approaches zero while $m_2$ remains positive, the heavier side approaches free fall:

$$
m_1\to0
\qquad\Longrightarrow\qquad
a\to g.
$$

For positive masses with $m_2>m_1$, the formula must therefore give

$$
0<a<g.
$$

These checks catch a reversed mass difference, a missing total-mass denominator, or an answer that incorrectly exceeds free-fall acceleration.

```quiz
type: radio
id: atwood-limiting-case-check
shuffle: true
content: |-
  Which statement is a valid check on $a=\dfrac{(m_2-m_1)g}{m_1+m_2}$ for positive masses?
options:
- id: equal-masses-zero
  content: |-
    If $m_2=m_1$, then $a=0$.
  correct: true
  feedback: |-
    Equal masses have equal opposing weights, so there is no gravitational imbalance to drive the system. The numerator becomes zero while the denominator remains positive, giving $a=0$.
- id: light-mass-zero-acceleration
  content: |-
    If $m_1\to0$, then $a\to0$.
  feedback: |-
    Removing the lighter mass does not balance the system; it removes the opposing weight and inertia. The ratio approaches $m_2g/m_2=g$, so the heavier side approaches free fall.
- id: acceleration-exceeds-g
  content: |-
    For sufficiently different masses, $a>g$.
  feedback: |-
    For positive masses, $m_2-m_1$ is always smaller than $m_1+m_2$. Their ratio is therefore below one, so the ideal Atwood acceleration remains below $g$.
- id: massless-means-g
  content: |-
    A massless pulley makes $a=g$ for any unequal pair of masses.
  feedback: |-
    A massless pulley removes rotational inertia, but the lighter mass still opposes the motion and must be accelerated. The result reaches $g$ only as the lighter mass approaches zero.
- id: equal-increase-raises-a
  content: |-
    Adding the same positive mass to both sides, while keeping $m_2-m_1$ fixed, increases $a$.
  feedback: |-
    The driving-force numerator stays fixed, while the total-mass denominator increases. Adding equal mass to both sides therefore decreases the acceleration rather than increasing it.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the original symbolic problem before checking the choices.

**Explanation**

> Masses $m_1$ and $m_2$ are connected over a massless, frictionless pulley, with $m_2>m_1$. Find the acceleration magnitude.

Use the diagram from the problem, assign the heavier side downward and the lighter side upward, and write one force equation for each mass. Keep the answer symbolic in $m_1$, $m_2$, and $g$.

```quiz
type: radio
id: khadley-equilibrium-q3
shuffle: true
content: |-
  Which expression is the acceleration magnitude for the original problem?
options:
- id: difference-over-sum
  content: |-
    $\dfrac{(m_2-m_1)g}{m_1+m_2}$
  correct: true
  feedback: |-
    The ideal pulley gives one common tension, and the connected masses share acceleration magnitude $a$. Adding $m_2g-T=m_2a$ and $T-m_1g=m_1a$ cancels tension and gives $a=(m_2-m_1)g/(m_1+m_2)$.
- id: sum-over-difference
  content: |-
    $\dfrac{(m_1+m_2)g}{m_2-m_1}$
  feedback: |-
    This reverses the roles of driving force and inertia. The weights oppose, so their difference drives the motion, while both masses accelerate, so their sum belongs in the denominator.
- id: difference-over-heavy
  content: |-
    $\dfrac{(m_2-m_1)g}{m_2}$
  feedback: |-
    The numerator correctly represents the gravitational imbalance, but the denominator omits the lighter mass's inertia. The cord accelerates both masses, so the total inertia is $m_1+m_2$.
- id: sum-over-sum
  content: |-
    $\dfrac{(m_2+m_1)g}{m_1+m_2}=g$
  feedback: |-
    The two weights act in opposite directions around the pulley, so they do not add as the driving force. Tension prevents the heavier mass from falling freely unless the lighter mass approaches zero.
- id: reversed-difference
  content: |-
    $\dfrac{(m_1-m_2)g}{m_1+m_2}$
  feedback: |-
    With $m_2>m_1$, this expression is negative, but the question asks for a magnitude. Choosing positive along $m_2$'s downward motion makes the driving difference $m_2-m_1$ and the magnitude positive.
```

---

<a id="summary"></a>
## Summary

For an Atwood machine with $m_2>m_1$ and a massless, frictionless pulley:

1. Assign $m_2$ downward and $m_1$ upward.
2. Use one shared acceleration magnitude $a$ and one common tension $T$.
3. Write
   $$m_2g-T=m_2a$$
   and
   $$T-m_1g=m_1a.$$
4. Add the equations so tension cancels.
5. Divide the driving force by the total accelerating mass:
   $$
   \boxed{a=\frac{(m_2-m_1)g}{m_1+m_2}}.
   $$

The method-selection cue is the opposite pair $-T$ and $+T$: add the equations directly. The numerator is a difference because the weights oppose each other, while the denominator is a sum because both masses accelerate. A correct magnitude satisfies both original force equations, lies in $0<a<g$, becomes zero for equal masses, and approaches $g$ only when the lighter mass approaches zero.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
