# Ranking Rolling Objects Down an Incline

<!--
lesson-id: 212-M2-054
topic-code: MTH212.M2.54
-->

## Table of Contents

- [Introduction](#introduction)
- [Normalize the Rotational Inertia](#normalize-the-rotational-inertia)
- [Reverse the Inertia Ranking](#reverse-the-inertia-ranking)
- [Separate Shape from Mass and Radius](#separate-shape-from-mass-and-radius)
- [Match the Source Diagram](#match-the-source-diagram)
- [Summary](#summary)

## Prerequisites

- Use the rolling-without-slipping relation $v=R\omega$.
- Recognize $K_{\mathrm{trans}}=\dfrac12mv^2$ and $K_{\mathrm{rot}}=\dfrac12I\omega^2$.
- Compare positive fractions.

---

<a id="introduction"></a>
## Introduction

When rigid objects roll without slipping from rest down the same incline, their race is controlled by how strongly each shape resists rotation relative to its mass and radius. Define the dimensionless inertia factor

$$
k=\frac{I}{mR^2}.
$$

Using $I=kmR^2$ and $\omega=v/R$, conservation of energy gives

$$
mgh
=\frac12mv^2+\frac12I\omega^2
=\frac12mv^2(1+k).
$$

The corresponding speed and acceleration are

$$
v=\sqrt{\frac{2gh}{1+k}},
\qquad
a=\frac{g\sin\theta}{1+k}.
$$

The recognition cue is a same-slope race between objects rolling without slipping. Rank their $k$ values first, then reverse that ranking: the smallest $k$ gives the largest acceleration and reaches the bottom first. This ideal result assumes enough static friction to maintain rolling and neglects rolling resistance and air drag.

---

<a id="normalize-the-rotational-inertia"></a>
## Normalize the Rotational Inertia

Dividing $I$ by $mR^2$ removes the common mass and radius and leaves the shape factor that controls the motion.

For three standard shapes,

$$
\begin{array}{c|c|c}
\text{shape} & I & k=I/(mR^2) \\
\hline
\text{hoop} & mR^2 & 1 \\
\text{uniform solid cylinder} & \frac12mR^2 & \frac12 \\
\text{uniform solid sphere} & \frac25mR^2 & \frac25
\end{array}
$$

For the two close fractions, use a common denominator:

$$
\frac25=\frac4{10}<\frac5{10}=\frac12<1.
$$

**Example:** A hoop and a uniform solid cylinder have equal masses and radii. Which has the smaller dimensionless inertia?

**Explanation**

The hoop has $k=1$, while the solid cylinder has $k=1/2$. Therefore, the solid cylinder has the smaller dimensionless inertia and will accelerate faster on the same incline.

```quiz
type: radio
id: rolling-normalize-inertia
shuffle: true
content: |-
  A uniform solid sphere and a uniform solid cylinder roll without slipping from rest down the same incline. Which object has the larger acceleration?
options:
- id: rolling-normalize-inertia-sphere
  content: |-
    The solid sphere
  correct: true
  feedback: |-
    Rolling acceleration is $a=g\sin\theta/(1+k)$. The sphere has $k=2/5$, which is smaller than the cylinder's $k=1/2$, so its denominator is smaller and its acceleration is larger.
- id: rolling-normalize-inertia-cylinder
  content: |-
    The solid cylinder
  feedback: |-
    The cylinder's $k=1/2$ is larger than the sphere's $k=2/5$. A larger dimensionless inertia puts more of the gravitational energy into rotation and produces a smaller center-of-mass acceleration.
- id: rolling-normalize-inertia-tie
  content: |-
    They have the same acceleration
  feedback: |-
    A tie requires equal dimensionless inertia factors. Here $2/5\ne1/2$, so the sphere and cylinder divide their energy differently and do not accelerate equally.
- id: rolling-normalize-inertia-mass-needed
  content: |-
    Their masses are needed to decide
  feedback: |-
    For ideal rolling, mass cancels from $a=g\sin\theta/(1+I/(mR^2))$. The standard shape factors $2/5$ and $1/2$ are enough to decide that the sphere accelerates faster.
```

---

<a id="reverse-the-inertia-ranking"></a>
## Reverse the Inertia Ranking

Because $k$ appears in the positive denominator $1+k$, increasing $k$ decreases the acceleration. Use the comparison chain

$$
\text{smaller }k
\;\Longrightarrow\;
\text{smaller }(1+k)
\;\Longrightarrow\;
\text{larger }a
\;\Longrightarrow\;
\text{shorter arrival time}.
$$

Order the fractions from smallest to largest, then reverse that order to rank arrival times.

**Example:** Rolling objects $A$, $B$, and $C$ have $k_A=3/4$, $k_B=1/3$, and $k_C=1/2$. Rank them from first to last at the bottom of the same incline.

**Explanation**

The inertia factors satisfy

$$
\frac13<\frac12<\frac34.
$$

Smaller $k$ means larger acceleration, so the arrival order is

$$
B,\ C,\ A.
$$

```quiz
type: radio
id: rolling-reverse-ranking
shuffle: true
content: |-
  Three objects roll without slipping from rest down the same incline. Their dimensionless inertia factors are $k_P=2/3$, $k_Q=1/4$, and $k_R=3/5$. What is their arrival order from first to last?
options:
- id: rolling-reverse-ranking-qrp
  content: |-
    $Q,\ R,\ P$
  correct: true
  feedback: |-
    The factors satisfy $1/4<3/5<2/3$. Since $a=g\sin\theta/(1+k)$ decreases as $k$ increases, the smallest factor arrives first and the order is $Q,R,P$.
- id: rolling-reverse-ranking-qpr
  content: |-
    $Q,\ P,\ R$
  feedback: |-
    This correctly places $Q$ first but reverses the last two fractions. Using fifteenths, $3/5=9/15$ and $2/3=10/15$, so $R$ has the smaller factor and must arrive before $P$.
- id: rolling-reverse-ranking-rqp
  content: |-
    $R,\ Q,\ P$
  feedback: |-
    The factor $1/4$ for $Q$ is smaller than $3/5$ for $R$. Because the smaller denominator factor produces the larger acceleration, $Q$ must arrive before $R$.
- id: rolling-reverse-ranking-prq
  content: |-
    $P,\ R,\ Q$
  feedback: |-
    This follows the inertia factors from largest to smallest. Arrival order is the reverse: a larger $k$ enlarges $1+k$ and reduces acceleration, so $P$ is last rather than first.
- id: rolling-reverse-ranking-tie
  content: |-
    They arrive together
  feedback: |-
    Equal arrival times require equal $k$ values under the same rolling conditions. The three given factors are distinct, so their accelerations and arrival times are distinct.
```

---

<a id="separate-shape-from-mass-and-radius"></a>
## Separate Shape from Mass and Radius

Raw moment of inertia $I$ is not the quantity to rank. The motion depends on the ratio $I/(mR^2)=k$. For objects of the same shape, changing mass or radius changes $I$ but leaves $k$ unchanged.

**Example:** Two uniform solid cylinders have different masses and radii but start from rest at the same point on an incline. Both roll without slipping. Which arrives first in the ideal model?

**Explanation**

Every uniform solid cylinder has

$$
k=\frac{\frac12mR^2}{mR^2}=\frac12.
$$

Both therefore have the same acceleration $g\sin\theta/(1+1/2)$ and arrive together. Their different raw values of $I$ do not change the ratio that controls the race.

```quiz
type: radio
id: rolling-shape-not-size
shuffle: true
content: |-
  Cylinder $A$ is a uniform solid cylinder with twice the mass and three times the radius of uniform solid cylinder $B$. They start together and roll without slipping down the same incline. In the ideal model, which arrives first?
options:
- id: rolling-shape-not-size-heavier
  content: |-
    Cylinder $A$, because it is heavier
  feedback: |-
    Mass cancels from the rolling acceleration. Both cylinders have $k=I/(mR^2)=1/2$, so the greater mass of $A$ does not give it a larger acceleration.
- id: rolling-shape-not-size-larger
  content: |-
    Cylinder $A$, because it has the larger radius
  feedback: |-
    Radius also cancels inside $I/(mR^2)$. Although $A$ has a larger raw moment of inertia, its dimensionless factor remains $1/2$, the same as $B$.
- id: rolling-shape-not-size-smaller
  content: |-
    Cylinder $B$, because it has the smaller radius
  feedback: |-
    A smaller radius does not give an ideal rolling object of the same shape a larger acceleration. Both cylinders have the same $k=1/2$, independent of their individual radii.
- id: rolling-shape-not-size-tie
  content: |-
    They arrive together
  correct: true
  feedback: |-
    For the same shape, $I=kmR^2$ with the same $k$. Both solid cylinders have $k=1/2$, so $a=g\sin\theta/(1+k)$ is identical and they arrive together.
- id: rolling-shape-not-size-insufficient
  content: |-
    There is not enough information to decide
  feedback: |-
    The ideal-model conditions and shapes are sufficient. Same incline, same start, no slip, and equal shape factors determine equal accelerations even though the masses and radii differ.
```

---

<a id="match-the-source-diagram"></a>
## Match the Source Diagram

For a same-slope race, list each $k=I/(mR^2)$ and choose the smallest value.

**Example:** A thin spherical shell $(k=2/3)$, a uniform solid cylinder $(k=1/2)$, and a hoop $(k=1)$ roll down the same incline. Which arrives first?

**Explanation**

The solid cylinder has the smallest factor:

$$
\frac12<\frac23<1.
$$

It therefore has the largest acceleration and arrives first.

For the three shapes in the source problem, direct substitution gives

$$
a_{\mathrm{sphere}}=\frac57g\sin\theta,
\qquad
a_{\mathrm{cylinder}}=\frac23g\sin\theta,
\qquad
a_{\mathrm{hoop}}=\frac12g\sin\theta.
$$

Because $5/7>2/3>1/2$, the acceleration comparison agrees with the reversed-$k$ ranking.

```quiz
type: radio
id: khadley-rolling-q1
shuffle: true
content: |-
  **Question 1**

  A hoop, uniform solid cylinder, and uniform solid sphere have equal masses and radii and roll without slipping from rest down the same slope. Which reaches the bottom first?

  ![](<../Source/Images/12-45-figure.jpg>)
options:
- id: hoop
  content: Hoop
  feedback: |-
    A hoop has the largest dimensionless inertia $I/(mR^2)=1$, so more gravitational energy goes into rotation and its center accelerates least.
- id: cylinder
  content: Solid cylinder
  feedback: |-
    The cylinder's $I/(mR^2)=1/2$ is smaller than the hoop's but larger than the sphere's, so its acceleration is intermediate.
- id: sphere
  content: Solid sphere
  correct: true
  feedback: |-
    Rolling acceleration increases as $I/(mR^2)$ decreases. The solid sphere has the smallest value, $2/5$, so it reaches the bottom first.
```

---

<a id="summary"></a>
## Summary

To rank objects rolling without slipping from rest down the same incline:

1. Compute or identify $k=I/(mR^2)$ for each shape.
2. Compare the positive $k$ values, using common denominators when needed.
3. Substitute into $a=g\sin\theta/(1+k)$ or reverse the $k$ order.
4. Translate the acceleration order into first-to-last arrival order.

For the standard shapes,

$$
\frac25\ \text{(solid sphere)}
<
\frac12\ \text{(solid cylinder)}
<
1\ \text{(hoop)},
$$

so the arrival order is solid sphere, solid cylinder, hoop. The main trap is ranking raw $I$ values or declaring a tie from equal masses, radii, and starting heights. The dimensionless shape factor controls the ideal rolling race.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
