# Minimum Speed and Tension in a Vertical Circle

<!--
lesson-id: 212-M1-074
topic-code: MTH212.M1.74
-->

## Table of Contents

- [Introduction](#introduction)
- [Write the Inward Radial Equations](#write-the-inward-radial-equations)
- [Use the Minimum-Speed Boundary at the Top](#use-the-minimum-speed-boundary-at-the-top)
- [Carry the Speed Relation to the Bottom](#carry-the-speed-relation-to-the-bottom)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Apply Newton's second law along a chosen axis: $\sum F_r=ma_r$.
- Use the inward radial acceleration $a_r=v^2/L$ for motion on a circle of radius $L$.
- Know that string tension pulls along the string and that weight $mg$ points downward.
- Solve a symbolic equation for a nonnegative speed.

---

<a id="introduction"></a>
## Introduction

A ball of mass $m$ on the end of a massless string of length $L$ is swung in a vertical circle. The problem asks for two symbolic results:

1. the minimum possible speed at the top of the circle;
2. the tension at the bottom when the bottom speed is twice that minimum top speed.

The recognition cues are **minimum speed at the top** and **tension at the bottom**. At each position, point the radial axis inward, write only the real radial forces, and set their sum equal to $mv^2/L$. The word *minimum* supplies a boundary condition at the top; the stated factor of two must be squared when it enters $v^2$.

Use the same three-move routine every time:

1. Choose inward as positive and write $\sum F_r=mv^2/L$ at the named position.
2. Translate a limiting word such as *minimum* into the physical boundary $T=0$.
3. Substitute any speed relation, square it, and isolate the requested variable.

![](<../Source/Images/ballstring-2.jpg>)

---

<a id="write-the-inward-radial-equations"></a>
## Write the Inward Radial Equations

**Example:** Write the radial force equation at the top and at the bottom while choosing the direction toward the circle's center as positive at each position.

**Explanation**

At the top, inward is downward. Both tension and weight point inward, so

$$
T_T+mg=m\frac{v_T^2}{L}.
$$

At the bottom, inward is upward. Tension points inward, but weight points away from the center, so

$$
T_B-mg=m\frac{v_B^2}{L}.
$$

The positive direction changes between the two locations. There is no extra "centripetal force" to add; $mv^2/L$ is the required inward net force.

```quiz
type: radio
id: vertical-circle-radial-equations
shuffle: true
content: |-
  Inward is chosen as positive at both the top and bottom of a vertical circle. Which pair of radial equations is correct?
options:
- id: top-plus-bottom-minus
  content: |-
    $T_T+mg=m\dfrac{v_T^2}{L}$ and $T_B-mg=m\dfrac{v_B^2}{L}$
  correct: true
  feedback: |-
    Inward points downward at the top, so both $T_T$ and $mg$ are positive there. Inward points upward at the bottom, so $T_B$ is positive and $mg$ is negative, giving the stated pair.
- id: top-minus-bottom-plus
  content: |-
    $T_T-mg=m\dfrac{v_T^2}{L}$ and $T_B+mg=m\dfrac{v_B^2}{L}$
  feedback: |-
    This treats weight as though it pointed outward at the top and inward at the bottom. Weight always points downward: it is inward at the top but outward at the bottom.
- id: both-minus
  content: |-
    $T_T-mg=m\dfrac{v_T^2}{L}$ and $T_B-mg=m\dfrac{v_B^2}{L}$
  feedback: |-
    The bottom sign is correct, but the top sign is not. With inward chosen separately at each position, downward weight is positive at the top and negative at the bottom.
- id: both-plus
  content: |-
    $T_T+mg=m\dfrac{v_T^2}{L}$ and $T_B+mg=m\dfrac{v_B^2}{L}$
  feedback: |-
    The top sign is correct, but weight does not point inward at the bottom. At the bottom the center is above the ball while weight points downward, so the bottom equation needs $-mg$.
```

---

<a id="use-the-minimum-speed-boundary-at-the-top"></a>
## Use the Minimum-Speed Boundary at the Top

**Example:** Find the minimum possible speed at the top for the ball of mass $m$ on a massless string of length $L$.

**Explanation**

A string can pull but cannot push, so its tension cannot be negative. As the top speed decreases, less inward force is required. The smallest speed that still permits the circular path occurs at the boundary where the string is just about to go slack:

$$
T_T=0.
$$

Apply that boundary to the top equation:

$$
0+mg=m\frac{v_{T,\min}^2}{L}.
$$

Cancel $m$ and solve for the nonnegative speed:

$$
v_{T,\min}^2=gL
\qquad\Longrightarrow\qquad
\boxed{v_{T,\min}=\sqrt{gL}}.
$$

Only the positive square root is kept because speed is a magnitude.

```quiz
type: radio
id: vertical-circle-minimum-top-speed
shuffle: true
content: |-
  A ball on a massless string of length $R$ barely maintains the circular path at the top. What is its speed there?
options:
- id: square-root-gr
  content: |-
    $\sqrt{gR}$
  correct: true
  feedback: |-
    At the limiting top speed the string tension is zero, so gravity alone provides the inward force: $mg=mv^2/R$. Canceling $m$ gives $v^2=gR$, hence the speed is $\sqrt{gR}$.
- id: gr
  content: |-
    $gR$
  feedback: |-
    The force equation gives $v^2=gR$, not $v=gR$. Taking the positive square root is required, and it also changes the units from speed squared to speed.
- id: square-root-two-gr
  content: |-
    $\sqrt{2gR}$
  feedback: |-
    The top radial equation uses the radius $R$ in $v^2/R$; it does not introduce a factor of two. A $2R$ height change belongs to an energy comparison between positions, not this local minimum-force condition.
- id: zero
  content: |-
    $0$
  feedback: |-
    Zero tension does not mean zero inward net force. At the boundary, gravity still supplies $mg$ inward, which requires the nonzero speed $\sqrt{gR}$.
- id: square-root-gr-over-m
  content: |-
    $\sqrt{\dfrac{gR}{m}}$
  feedback: |-
    Mass multiplies both sides of $mg=mv^2/R$ and cancels. The limiting speed is independent of $m$, so no mass remains under the square root.
```

---

<a id="carry-the-speed-relation-to-the-bottom"></a>
## Carry the Speed Relation to the Bottom

**Example:** Find the bottom tension if the bottom speed is twice the minimum top speed.

**Explanation**

Use the result from the top and the stated speed relation:

$$
v_B=2v_{T,\min}=2\sqrt{gL}.
$$

The radial force equation contains the square of the speed, so

$$
v_B^2=\left(2\sqrt{gL}\right)^2=4gL.
$$

Substitute into the bottom equation and solve for tension:

$$
\begin{aligned}
T_B-mg&=m\frac{v_B^2}{L} \\
T_B-mg&=m\frac{4gL}{L}=4mg \\
T_B&=\boxed{5mg}.
\end{aligned}
$$

The same substitution can be compressed into a reusable ratio rule. If

$$
v_B=k\,v_{T,\min},
$$

then $v_B^2=k^2gL$, so the bottom equation becomes

$$
T_B-mg=k^2mg
\qquad\Longrightarrow\qquad
T_B=(k^2+1)mg.
$$

For the stated factor $k=2$, this gives $T_B=(2^2+1)mg=5mg$. The square on $k$ accounts for the radial net force, and the added $1$ accounts for the ball's outward weight at the bottom.

```quiz
type: radio
id: vertical-circle-bottom-tension-ratio
shuffle: true
content: |-
  At the bottom of a vertical circle, a ball has speed $v_B=3\sqrt{gL}$. What is the string tension there?
options:
- id: ten-mg
  content: |-
    $10mg$
  correct: true
  feedback: |-
    At the bottom, $T_B-mg=mv_B^2/L$. Here $v_B^2=9gL$, so the required inward net force is $9mg$ and the tension must be $9mg+mg=10mg$.
- id: nine-mg
  content: |-
    $9mg$
  feedback: |-
    This is the required inward net force $mv_B^2/L$, not the tension. Because weight points outward at the bottom, tension must exceed the net inward force by $mg$, giving $10mg$.
- id: eight-mg
  content: |-
    $8mg$
  feedback: |-
    This follows from adding weight on the left as though gravity pointed inward. At the bottom gravity points away from the center, so $T_B-mg=9mg$ and $T_B=10mg$.
- id: four-mg
  content: |-
    $4mg$
  feedback: |-
    The factor of $3$ multiplies speed, but radial force depends on $v^2$, so it contributes $3^2=9$, not $3$. After adding the weight term, the tension is $10mg$.
- id: three-mg
  content: |-
    $3mg$
  feedback: |-
    Tension is not proportional to speed itself. The radial requirement is proportional to $v^2$, and the bottom tension must also overcome the outward weight, so the result is $10mg$.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Complete the original two-part problem without looking back at the worked steps.

**Explanation**

Write two symbolic answers, in order, before checking a choice below:

> A ball of mass $m$ on the end of a massless string of length $L$ is swung in a vertical circle.
>
> 1. Find the minimum possible speed at the top of the circle.
> 2. Find the tension at the bottom if the bottom speed is twice the minimum top speed.

First apply the zero-tension boundary at the top. Then carry that speed into the bottom equation, remembering both the square on the speed ratio and the direction of weight.

```quiz
type: radio
id: khadley-circular-example-q1
shuffle: true
content: |-
  Which ordered pair gives (minimum top speed, bottom tension) for the original problem?
options:
- id: square-root-gl-five-mg
  content: |-
    $\left(\sqrt{gL},\ 5mg\right)$
  correct: true
  feedback: |-
    At the top, $T_T=0$ makes $mg=mv_T^2/L$, so $v_{T,\min}=\sqrt{gL}$. Then $v_B^2=(2\sqrt{gL})^2=4gL$ and $T_B-mg=4mg$, giving $T_B=5mg$.
- id: square-root-gl-three-mg
  content: |-
    $\left(\sqrt{gL},\ 3mg\right)$
  feedback: |-
    The top result is correct, but $3mg$ comes from treating the factor of two in speed as a factor of two in radial force. Because radial force depends on $v^2$, the factor becomes four and the bottom tension is $5mg$.
- id: square-root-two-gl-five-mg
  content: |-
    $\left(\sqrt{2gL},\ 5mg\right)$
  feedback: |-
    The bottom result matches the stated speed relation, but the local top boundary has no factor of two: $mg=mv_T^2/L$. The factor $2L$ is a height difference used in an energy comparison, not in the top radial-force equation.
- id: square-root-gl-four-mg
  content: |-
    $\left(\sqrt{gL},\ 4mg\right)$
  feedback: |-
    The value $4mg$ is the required inward net force $mv_B^2/L$, not the string tension. At the bottom weight points outward, so tension must supply both that net force and another $mg$, giving $5mg$.
- id: zero-one-mg
  content: |-
    $\left(0,\ mg\right)$
  feedback: |-
    The limiting condition sets top tension to zero, not top speed. Gravity alone must still provide the inward acceleration at the top, so $v_{T,\min}=\sqrt{gL}$; carrying the stated bottom speed then gives $T_B=5mg$.
```

---

<a id="summary"></a>
## Summary

When a vertical-circle problem asks for a minimum top speed and a bottom tension:

1. Choose inward as positive at each location.
2. At the top, write $T_T+mg=mv_T^2/L$ and use the limiting condition $T_T=0$.
3. Keep the nonnegative speed, $v_{T,\min}=\sqrt{gL}$.
4. Apply the stated speed relation before squaring it.
5. At the bottom, write $T_B-mg=mv_B^2/L$ and solve for the actual tension.

For the given relation $v_B=2v_{T,\min}$, the results are

$$
\boxed{v_{T,\min}=\sqrt{gL}},
\qquad
\boxed{T_B=5mg}.
$$

The units provide a quick check:

$$
[\sqrt{gL}]
=\sqrt{\left(\frac{\mathrm{m}}{\mathrm{s}^2}\right)(\mathrm{m})}
=\frac{\mathrm{m}}{\mathrm{s}},
\qquad
[5mg]=\mathrm{N}.
$$

For a general stated ratio $v_B=k\,v_{T,\min}$, the same work gives $T_B=(k^2+1)mg$.

The main traps are treating $mv^2/L$ as an extra force, using one fixed sign for weight at both positions, forgetting that a speed multiplier is squared, or setting speed to zero when the limiting tension is zero.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
