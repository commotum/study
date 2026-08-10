# Angular Speed After a Radial Mass Change

<!--
lesson-id: 212-M2-052
topic-code: MTH212.M2.52
-->

## Table of Contents

- [Introduction](#introduction)
- [Square the Radial Scale Factor](#square-the-radial-scale-factor)
- [Invert the Inertia Factor](#invert-the-inertia-factor)
- [Handle an Inward Radial Move](#handle-an-inward-radial-move)
- [Apply the Rule to Two Equal Masses](#apply-the-rule-to-two-equal-masses)
- [Summary](#summary)

## Prerequisites

- Use $I=\sum mr^2$ for point masses about a specified rotation axis.
- Use $L=I\omega$ for a rigidly rotating system.
- Square a multiplicative scale factor and solve a one-step symbolic equation.

---

<a id="introduction"></a>
## Introduction

When a problem states that angular momentum is conserved while point masses move closer to or farther from the rotation axis, change the moment of inertia **before** solving for the new angular speed.

For point masses,

$$
I=\sum mr^2.
$$

The scaling shortcut applies when the same masses remain in the system and every radius changes by the same factor $k$. Under those conditions,

$$
r_f=kr_i
\quad\Longrightarrow\quad
\frac{I_f}{I_i}=k^2.
$$

With negligible net external torque, angular momentum is conserved:

$$
I_i\omega_i=I_f\omega_f.
$$

First isolate the requested variable, treating the moments of inertia as known coefficients:

$$
\omega_f=\frac{I_i}{I_f}\omega_i
=\frac{1}{k^2}\omega_i.
$$

The factor chain is

| Quantity | Final-to-initial factor |
|---|---:|
| Radius $r$ | $k$ |
| Moment of inertia $I$ | $k^2$ |
| Angular speed $\omega$ | $1/k^2$ |

Use this sequence: find the radial factor, square it to get the inertia factor, then invert that factor to get the angular-speed factor. If only some masses move or different masses receive different radial factors, return to $I=\sum mr^2$ and calculate the two sums rather than using one global $k^2$.

---

<a id="square-the-radial-scale-factor"></a>
## Square the Radial Scale Factor

**Example:** Several unchanged point masses all move from radius $r_i$ to radius $r_f=3r_i$. By what factor does their total moment of inertia change?

**Explanation**

Each term in $I=\sum mr^2$ contains the square of its radius:

$$
m(3r_i)^2=9mr_i^2.
$$

Every term gains the same factor of $9$, so the whole sum does too:

$$
I_f=9I_i.
$$

The number of masses does not create another scale factor because the same masses appear in both the initial and final sums.

Equivalently, compare the two states directly:

$$
\frac{I_f}{I_i}
=\left(\frac{r_f}{r_i}\right)^2
=3^2=9.
$$

```quiz
type: radio
id: radial-mass-inertia-factor
shuffle: true
content: |-
  Three identical point masses remain in the system while each one's distance from the rotation axis changes from $r$ to $4r$. By what factor does the total moment of inertia change?
options:
- id: factor-16
  content: |-
    It becomes $16$ times as large.
  correct: true
  feedback: |-
    Each point-mass term is $mr^2$, so replacing $r$ by $4r$ multiplies it by $4^2=16$. Because all three unchanged masses receive the same factor, the total moment of inertia becomes $I_f=16I_i$.
- id: factor-4
  content: |-
    It becomes $4$ times as large.
  feedback: |-
    A factor of $4$ treats moment of inertia as linear in radius. The radius is squared in $mr^2$, so a fourfold radius change produces the factor $4^2=16$.
- id: factor-12
  content: |-
    It becomes $12$ times as large.
  feedback: |-
    Multiplying the radial factor $4$ by the three masses counts the mass total only in the final state. The same three masses are present initially, so their count cancels in the ratio and the remaining factor is $4^2=16$.
- id: factor-64
  content: |-
    It becomes $64$ times as large.
  feedback: |-
    A factor of $64=4^3$ incorrectly uses the number of masses as an exponent. The exponent comes from the $r^2$ in each point-mass term, so the correct factor is $4^2=16$.
- id: factor-1
  content: |-
    It is unchanged.
  feedback: |-
    The masses are unchanged, but their distances from the axis are not. Moment of inertia depends on mass placement through $r^2$, so moving every mass from $r$ to $4r$ changes $I$ by a factor of $16$.
```

---

<a id="invert-the-inertia-factor"></a>
## Invert the Inertia Factor

**Example:** A rotating system has no net external torque, and its moment of inertia changes to $I_f=4I_i$. Express $\omega_f$ in terms of $\omega_i$.

**Explanation**

No net external torque means angular momentum remains constant:

$$
I_i\omega_i=I_f\omega_f.
$$

Substitute $I_f=4I_i$ and cancel $I_i$:

$$
I_i\omega_i=4I_i\omega_f
\quad\Longrightarrow\quad
\omega_f=\frac{\omega_i}{4}.
$$

The angular-speed factor is the reciprocal of the inertia factor. A larger $I$ requires a smaller $\omega$ so that their product stays fixed.

In ratio form,

$$
\frac{\omega_f}{\omega_i}
=\frac{I_i}{I_f}.
$$

This is an inverse variation: the product $I\omega=L$ stays constant.

```quiz
type: radio
id: angular-speed-from-inertia-factor
shuffle: true
content: |-
  A system experiences negligible net external torque and changes from $I_i$ to $I_f=5I_i$. Which expression gives its final angular speed?
options:
- id: omega-over-5
  content: |-
    $\omega_f=\dfrac{\omega_i}{5}$
  correct: true
  feedback: |-
    Angular momentum conservation keeps $I\omega$ constant. Since $I_f$ is five times $I_i$, $\omega_f$ must be one-fifth of $\omega_i$, giving $\omega_f=\omega_i/5$.
- id: five-omega
  content: |-
    $\omega_f=5\omega_i$
  feedback: |-
    Multiplying both $I$ and $\omega$ by $5$ would make angular momentum $25$ times larger. To keep $I\omega$ fixed, the fivefold inertia increase requires the reciprocal angular-speed factor $1/5$.
- id: omega-same
  content: |-
    $\omega_f=\omega_i$
  feedback: |-
    Zero external torque conserves angular momentum, not angular speed by itself. Because the moment of inertia changes, $\omega$ must compensate so that $I_i\omega_i=I_f\omega_f$.
- id: omega-over-25
  content: |-
    $\omega_f=\dfrac{\omega_i}{25}$
  feedback: |-
    The given factor $5$ already describes the full change in moment of inertia. Squaring it again is not part of angular momentum conservation; simply invert $5$ to obtain $\omega_i/5$.
- id: omega-over-sqrt5
  content: |-
    $\omega_f=\dfrac{\omega_i}{\sqrt{5}}$
  feedback: |-
    A square-root relation would arise from holding rotational kinetic energy $\tfrac12I\omega^2$ fixed. Here angular momentum $I\omega$ is conserved, so angular speed varies inversely with $I$ and becomes $\omega_i/5$.
```

---

<a id="handle-an-inward-radial-move"></a>
## Handle an Inward Radial Move

**Example:** Every point mass moves from radius $r_i$ to $r_f=r_i/3$ while angular momentum is conserved. Express $\omega_f$ in terms of $\omega_i$.

**Explanation**

The radial factor is $k=1/3$, so the moment-of-inertia factor is

$$
\frac{I_f}{I_i}=k^2=\left(\frac13\right)^2=\frac19.
$$

Angular speed changes by the reciprocal factor:

$$
\omega_f=9\omega_i.
$$

Moving mass inward lowers $I$, so the system spins faster. This direction check helps catch a factor that was inverted the wrong way.

```quiz
type: radio
id: angular-speed-after-inward-radius-change
shuffle: true
content: |-
  All point masses in a rotating system move from radius $r_i$ to $r_f=r_i/2$. With angular momentum conserved, what is the final angular speed?
options:
- id: four-omega
  content: |-
    $\omega_f=4\omega_i$
  correct: true
  feedback: |-
    Halving every radius makes $I_f=(1/2)^2I_i=I_i/4$. Angular momentum conservation then requires the reciprocal factor, so $\omega_f=4\omega_i$.
- id: two-omega
  content: |-
    $\omega_f=2\omega_i$
  feedback: |-
    A factor of $2$ accounts for the radial change but misses the square in $I=\sum mr^2$. Halving radius quarters $I$, so conservation raises angular speed by a factor of $4$.
- id: omega-over-2
  content: |-
    $\omega_f=\dfrac{\omega_i}{2}$
  feedback: |-
    Moving mass inward reduces moment of inertia, so angular speed must increase rather than decrease when angular momentum is fixed. Including the square gives the increase $\omega_f=4\omega_i$.
- id: omega-over-4
  content: |-
    $\omega_f=\dfrac{\omega_i}{4}$
  feedback: |-
    The inertia does become one-fourth as large, but angular speed changes inversely with inertia. Applying the same one-fourth factor to $\omega$ would reduce angular momentum instead of conserving it.
- id: omega-unchanged
  content: |-
    $\omega_f=\omega_i$
  feedback: |-
    The mass values are unchanged, but their radial placement changes $I$. With $I_f=I_i/4$, angular speed cannot remain fixed if the product $I\omega$ is conserved.
```

---

<a id="apply-the-rule-to-two-equal-masses"></a>
## Apply the Rule to Two Equal Masses

**Example:** Two equal point masses remain at opposite ends of a massless rod. If each distance from the axis becomes $3/2$ of its initial value and angular momentum is conserved, express $\omega_f$ in terms of $\omega_i$.

**Explanation**

The initial and final moments of inertia are

$$
I_i=2mr_i^2,
\qquad
I_f=2m\left(\frac32r_i\right)^2
=\frac94I_i.
$$

The common factor $2m$ cancels between the two states. Conserving angular momentum gives

$$
I_i\omega_i=\frac94I_i\omega_f
\quad\Longrightarrow\quad
\omega_f=\frac49\omega_i.
$$

**Target problem — solve symbolically before using the self-check:**

**Question 2**

Two equal point masses are connected by a massless rod. If their distance from the rotation axis doubles while angular momentum is conserved, find $\omega_f$ in terms of $\omega_i$.

![](<../Source/Images/angmosystem.jpg>)

```quiz
type: radio
id: khadley-angular-momentum-q2
shuffle: true
content: |-
  Which expression correctly checks the symbolic result for Question 2?
options:
- id: omega-quarter
  content: |-
    $\omega_f=\dfrac{\omega_i}{4}$
  correct: true
  feedback: |-
    The axis passes through the rod's midpoint, so each mass's radius is half the displayed rod length; doubling each distance gives $r_f=2r_i$. Thus $I_f=2m(2r_i)^2=4I_i$, and conservation of $I\omega$ requires $\omega_f=\omega_i/4$.
- id: omega-half
  content: |-
    $\omega_f=\dfrac{\omega_i}{2}$
  feedback: |-
    This treats moment of inertia as linear in radius. Because each point-mass term contains $r^2$, doubling the distance makes $I$ four times as large, not twice as large, so $\omega_f=\omega_i/4$.
- id: twice-omega
  content: |-
    $\omega_f=2\omega_i$
  feedback: |-
    Moving the masses outward increases moment of inertia, so angular speed must decrease when angular momentum is fixed. The squared radius gives a fourfold inertia increase and therefore a one-fourth speed factor.
- id: four-omega
  content: |-
    $\omega_f=4\omega_i$
  feedback: |-
    The factor $4$ belongs to the increase in moment of inertia. Angular speed must take the reciprocal factor so that $I_f\omega_f=I_i\omega_i$, giving $\omega_i/4$.
- id: same-omega
  content: |-
    $\omega_f=\omega_i$
  feedback: |-
    Conserved angular momentum does not mean conserved angular speed. The doubled radii change the moment of inertia, so $\omega$ must change inversely to keep $I\omega$ constant.
```

---

<a id="summary"></a>
## Summary

For unchanged point masses that all move by the same radial factor $k$:

1. Write $k=r_f/r_i$.
2. Square the factor: $I_f/I_i=k^2$.
3. Isolate the target: $\omega_f/\omega_i=I_i/I_f$.
4. Combine the ratios: $\omega_f=\omega_i/k^2$.

The main trap is using $k$ instead of $k^2$. A quick direction check is that moving mass outward slows the rotation, while moving it inward speeds the rotation, provided the net external torque is negligible. Use the ratio shortcut only when all unchanged masses share the same radial factor; otherwise compare the full initial and final inertia sums.
