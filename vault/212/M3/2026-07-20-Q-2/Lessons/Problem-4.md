# From Composite Center of Mass to Tangential Speed

## Table of Contents

- [Introduction](#introduction)
- [Represent Each Piece by a Mass and Position](#represent-each-piece-by-a-mass-and-position)
- [Compute the Mass-Weighted Position](#compute-the-mass-weighted-position)
- [Measure Radius from the Rotation Axis](#measure-radius-from-the-rotation-axis)
- [Combine Center of Mass with Tangential Speed](#combine-center-of-mass-with-tangential-speed)
- [Summary](#summary)

## Prerequisites

- Choose an origin and read one-dimensional positions from a diagram.
- Compute a weighted average.
- Recognize that a uniform pole's center of mass is at its midpoint.
- Use the rigid-rotation relation $v=\omega r$.

---

<a id="introduction"></a>
## Introduction

When a composite object rotates about its center of mass, first locate that center with a mass-weighted average. Then measure the selected point's distance from the center of mass and use that distance—not its coordinate from the original origin—in $v=\omega r$.

For the pole in Problem 4, put the origin at the pole's left end:

![](<../Source/2026-07-20-Q-2/Images/problem-4-pole-point-masses.png>)

The three mass-position pairs are

| Piece | Mass | Position from the left end |
|---|---:|---:|
| Uniform pole | $m_p$ | $L/2$ |
| First point mass | $m_1$ | $2L/3$ |
| Right point mass | $m_2$ | $L$ |

The reusable procedure is

$$
x_{\mathrm{cm}}=\frac{\sum_i m_ix_i}{\sum_i m_i},
\qquad
r_i=\left|x_i-x_{\mathrm{cm}}\right|,
\qquad
v_i=\omega r_i.
$$

The recognition cue is a rigid system rotating about its center of mass while the requested point is located relative to some other reference point. The main trap is to insert that original coordinate directly into $v=\omega r$.

---

<a id="represent-each-piece-by-a-mass-and-position"></a>
## Represent Each Piece by a Mass and Position

**Example:** A uniform pole of length $L$ and mass $M$ lies from $x=0$ to $x=L$. A point mass $m$ is attached at $x=3L/4$. What mass-position pairs belong in the center-of-mass sum?

**Explanation**

For a composite center-of-mass calculation, a uniform extended object may be represented by its full mass placed at its own center of mass. Because the pole is uniform and spans $0\le x\le L$, its representative position is $L/2$. The point mass is already localized at $3L/4$. Thus the pairs are

$$
(M,L/2)
\qquad\text{and}\qquad
(m,3L/4).
$$

This replacement preserves the pole's contribution $Mx$ to the one-dimensional mass moment. It would not be valid at $L/2$ for a nonuniform pole unless its own center of mass were known to be there.

```quiz
type: radio
id: p4-represent-pieces
shuffle: true
content: |-
  A uniform pole of mass $m_p$ lies from $x=0$ to $x=L$, and a point mass $m_1$ is attached at $x=2L/3$. Which mass-position pairs should be used in the center-of-mass sum?
options:
- id: p4-represent-pieces-midpoint
  content: |-
    $(m_p,L/2)$ and $(m_1,2L/3)$
  correct: true
  feedback: |-
    A uniform pole's mass moment is represented by placing its full mass at its midpoint, $x=L/2$. The attached point mass remains at its stated coordinate, $x=2L/3$, so these are the two correct pairs.
- id: p4-represent-pieces-right-end
  content: |-
    $(m_p,L)$ and $(m_1,2L/3)$
  feedback: |-
    $L$ is the pole's right endpoint, not the location of its uniformly distributed mass. Replacing the pole by $m_p$ at its midpoint $L/2$ preserves its mass moment; the point mass stays at $2L/3$.
- id: p4-represent-pieces-origin
  content: |-
    $(m_p,0)$ and $(m_1,2L/3)$
  feedback: |-
    Choosing the left end as the coordinate origin does not place the pole's mass there. The pole extends uniformly from $0$ to $L$, so its representative position is $L/2$.
- id: p4-represent-pieces-swap
  content: |-
    $(m_p,2L/3)$ and $(m_1,L/2)$
  feedback: |-
    Each position must stay paired with the piece located there. The pole's midpoint is $L/2$, while the attached point mass—not the pole—is at $2L/3$.
- id: p4-represent-pieces-no-replacement
  content: |-
    The discrete center-of-mass formula cannot include the pole.
  feedback: |-
    A uniform pole can be included in a composite center-of-mass sum by replacing it with its full mass at its own center, $L/2$. An integral is unnecessary because the pole's center is already known.
```

---

<a id="compute-the-mass-weighted-position"></a>
## Compute the Mass-Weighted Position

**Example:** A uniform $2\,\mathrm{kg}$ pole extends from $x=0$ to $x=6\,\mathrm{m}$. Point masses of $1\,\mathrm{kg}$ and $3\,\mathrm{kg}$ are attached at $x=4\,\mathrm{m}$ and $x=6\,\mathrm{m}$. Find the system's center of mass.

**Explanation**

The pole's own center is at $x=3\,\mathrm{m}$. Multiply every position by the mass located there, add those mass moments, and divide by the total mass:

$$
\begin{aligned}
x_{\mathrm{cm}}
&=\frac{(2\,\mathrm{kg})(3\,\mathrm{m})
+(1\,\mathrm{kg})(4\,\mathrm{m})
+(3\,\mathrm{kg})(6\,\mathrm{m})}
{2\,\mathrm{kg}+1\,\mathrm{kg}+3\,\mathrm{kg}} \\
&=\frac{28}{6}\,\mathrm{m}
=\frac{14}{3}\,\mathrm{m}.
\end{aligned}
$$

The result lies inside the system and to the right of the pole's midpoint, as it must because the largest point mass is at the right end.

```quiz
type: radio
id: p4-weighted-center
shuffle: true
content: |-
  A uniform pole of length $L$ has mass $3m$ and extends from $x=0$ to $x=L$. A point mass $m$ is attached at $x=L$. Where is the composite center of mass?
options:
- id: p4-weighted-center-five-eighths
  content: |-
    $x_{\mathrm{cm}}=\dfrac{5L}{8}$
  correct: true
  feedback: |-
    The pole contributes $(3m)(L/2)$ and the point mass contributes $mL$. Dividing their sum by the total mass $4m$ gives $x_{\mathrm{cm}}=[3mL/2+mL]/(4m)=5L/8$.
- id: p4-weighted-center-omit-point
  content: |-
    $x_{\mathrm{cm}}=\dfrac{3L}{8}$
  feedback: |-
    This keeps the total-mass denominator $4m$ but omits the endpoint's mass moment $mL$ from the numerator. Including both pieces gives $[3m(L/2)+mL]/(4m)=5L/8$.
- id: p4-weighted-center-midpoint
  content: |-
    $x_{\mathrm{cm}}=\dfrac{L}{2}$
  feedback: |-
    $L/2$ is the center of the pole alone. Adding positive mass at $x=L$ shifts the composite center to the right, producing $5L/8$.
- id: p4-weighted-center-unweighted
  content: |-
    $x_{\mathrm{cm}}=\dfrac{3L}{4}$ because it is the average of $L/2$ and $L$
  feedback: |-
    Averaging the two positions equally would be valid only if the two pieces had equal mass. Here the pole has mass $3m$, so its position $L/2$ must receive three times the weight of the endpoint position.
- id: p4-weighted-center-divide-three
  content: |-
    $x_{\mathrm{cm}}=\dfrac{5L}{6}$
  feedback: |-
    This divides the combined mass moment by the pole mass $3m$ instead of by the system's total mass. The denominator must include both pieces: $3m+m=4m$.
```

---

<a id="measure-radius-from-the-rotation-axis"></a>
## Measure Radius from the Rotation Axis

**Example:** A rigid object extends from $x=0$ to $x=L$ and rotates about an axis through $x_{\mathrm{cm}}=3L/5$. What is the rotation radius of a point at the right endpoint?

**Explanation**

The radius in $v=\omega r$ is the distance from the rotation axis. For the right endpoint, $x=L$, so

$$
r_{\mathrm{right}}
=\left|L-\frac{3L}{5}\right|
=\frac{2L}{5}.
$$

The coordinate $L$ is measured from the chosen origin, while $2L/5$ is measured from the actual axis. Only the latter is the radius of the circular path.

Every point in a rigid body shares the same angular speed $\omega$, but tangential speed varies directly with axis distance. A point farther from the axis has a larger $v=\omega r$ even though its $\omega$ is unchanged.

```quiz
type: radio
id: p4-axis-distance
shuffle: true
content: |-
  A rigid pole lies along the $x$-axis from $0$ to $L$ and rotates about its center of mass at $x_{\mathrm{cm}}=0.62L$. What is the rotation radius of a point mass attached at $x=L$?
options:
- id: p4-axis-distance-correct
  content: |-
    $0.38L$
  correct: true
  feedback: |-
    Rotation radius is the distance from the axis: $r=|L-0.62L|=0.38L$. The endpoint therefore travels on a circle of radius $0.38L$.
- id: p4-axis-distance-axis-coordinate
  content: |-
    $0.62L$
  feedback: |-
    $0.62L$ locates the rotation axis relative to the left end; it is not the endpoint's distance from that axis. Subtracting coordinates gives $L-0.62L=0.38L$.
- id: p4-axis-distance-full-length
  content: |-
    $L$
  feedback: |-
    $L$ is the endpoint's coordinate relative to the left-end origin. It would be the rotation radius only if the axis were at the left end, but here the axis is at $0.62L$.
- id: p4-axis-distance-add
  content: |-
    $1.62L$
  feedback: |-
    Distances from a shared origin must be subtracted when both the axis and endpoint lie on the same side of that origin. Adding them does not measure their separation; the separation is $0.38L$.
- id: p4-axis-distance-negative
  content: |-
    $-0.38L$
  feedback: |-
    Reversing the subtraction can produce a signed displacement, but a rotation radius is a nonnegative distance. Use $|x-x_{\mathrm{cm}}|=0.38L$.
```

---

<a id="combine-center-of-mass-with-tangential-speed"></a>
## Combine Center of Mass with Tangential Speed

**Example:** A uniform pole of length $\ell$ and mass $M$ has point masses $a$ at $x=\ell/4$ and $b$ at $x=\ell$. The system rotates about its center of mass with angular speed $\Omega$. Find the tangential speed of $b$.

**Explanation**

First locate the axis:

$$
x_{\mathrm{cm}}
=\frac{M(\ell/2)+a(\ell/4)+b\ell}{M+a+b}.
$$

The mass $b$ is at the right endpoint, so its radius is

$$
\begin{aligned}
r_b
&=\ell-x_{\mathrm{cm}} \\
&=\frac{\ell(M+a+b)-\ell(M/2+a/4+b)}{M+a+b} \\
&=\frac{\ell(M/2+3a/4)}{M+a+b}.
\end{aligned}
$$

Therefore,

$$
v_b=\Omega r_b
=\frac{\Omega\ell(M/2+3a/4)}{M+a+b}.
$$

The endpoint mass $b$ cancels from the numerator because its own position is $\ell$, but it remains in the total-mass denominator. Increasing $b$ pulls the axis toward that endpoint and decreases its rotation radius.

Three quick checks support the symbolic result:

- The mass ratio in $r_b$ is dimensionless, so $r_b$ has units of length.
- Multiplying $\Omega$ by a length gives units of tangential speed.
- As $b$ becomes very large, the center of mass approaches $b$ and $r_b$ approaches zero, exactly as the denominator predicts.

```quiz
type: radio
id: p4-combined-result
shuffle: true
content: |-
  A uniform pole of length $L$ and mass $m_p$ has point masses $m_1$ at $x=2L/3$ and $m_2$ at $x=L$. The rigid system rotates about its center of mass with angular speed $\omega$. Which expression gives the tangential speed of $m_2$?
options:
- id: p4-combined-result-correct
  content: |-
    $\displaystyle v_2=\frac{\omega L\left(m_p/2+m_1/3\right)}{m_p+m_1+m_2}$
  correct: true
  feedback: |-
    The axis is at $x_{\mathrm{cm}}=[m_p(L/2)+m_1(2L/3)+m_2L]/(m_p+m_1+m_2)$. Thus $r_2=L-x_{\mathrm{cm}}=L(m_p/2+m_1/3)/(m_p+m_1+m_2)$, and $v_2=\omega r_2$ gives this expression.
- id: p4-combined-result-full-length
  content: |-
    $v_2=\omega L$
  feedback: |-
    This uses the distance from the left-end coordinate origin. The system rotates about its center of mass, so the required radius is $L-x_{\mathrm{cm}}$, which is smaller than $L$ for positive masses.
- id: p4-combined-result-axis-coordinate
  content: |-
    $\displaystyle v_2=\frac{\omega L\left(m_p/2+2m_1/3+m_2\right)}{m_p+m_1+m_2}$
  feedback: |-
    The fraction multiplying $\omega$ here is $x_{\mathrm{cm}}$, the axis's coordinate from the left end. Tangential speed uses the endpoint's distance from that axis, $L-x_{\mathrm{cm}}$, not the axis coordinate itself.
- id: p4-combined-result-cancel-denominator
  content: |-
    $\displaystyle v_2=\frac{\omega L\left(m_p/2+m_1/3\right)}{m_p+m_1}$
  feedback: |-
    Although the $m_2L$ terms cancel while simplifying $L-x_{\mathrm{cm}}$, $m_2$ is still part of the system's total mass. It must remain in the denominator because it shifts the center of mass toward the endpoint.
- id: p4-combined-result-wrong-complement
  content: |-
    $\displaystyle v_2=\frac{\omega L\left(m_p/2+2m_1/3\right)}{m_p+m_1+m_2}$
  feedback: |-
    The $2/3$ coefficient locates $m_1$ from the left end. Measuring the right endpoint's distance from the center replaces that coefficient by its complement, $1-2/3=1/3$; the numerator must contain $m_1/3$.
```

For the same system, the center of mass itself is

$$
x_{\mathrm{cm}}
=\frac{m_p(L/2)+m_1(2L/3)+m_2L}{m_p+m_1+m_2},
$$

which preserves the two requested symbolic results from Problem 4.

---

<a id="summary"></a>
## Summary

For a composite rigid body rotating about its center of mass:

1. Choose a coordinate origin and assign every piece a mass and position.
2. Replace each uniform extended piece by its full mass at its own geometric center.
3. Compute $x_{\mathrm{cm}}=\sum m_ix_i/\sum m_i$ and check that it lies inside the occupied interval, toward the heavier side.
4. Measure the selected point's radius from the axis: $r_i=|x_i-x_{\mathrm{cm}}|$.
5. Use $v_i=\omega r_i$.

For the right-end mass in Problem 4,

$$
r_2=L-x_{\mathrm{cm}}
=\frac{L(m_p/2+m_1/3)}{m_p+m_1+m_2},
$$

so

$$
v_2=\frac{\omega L(m_p/2+m_1/3)}{m_p+m_1+m_2}.
$$

The main trap is to confuse a coordinate measured from the left end with a rotation radius measured from the center-of-mass axis.
