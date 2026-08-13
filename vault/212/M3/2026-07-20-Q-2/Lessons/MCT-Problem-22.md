# Add Vectors with a Signed Component Ledger

<!--
lesson-id: 212-M3-058
topic-code: MTH212.M3.58
-->

## Table of Contents

- [Introduction](#introduction)
- [Build and Close the Signed Ledger](#signed-ledger)
- [Source-Video Controls: Collinear Vectors](#source-collinear)
- [Source-Video Worked Problems: Perpendicular Vectors and Quadrants](#source-perpendicular)
- [Source-Video Worked Problem: An Arbitrary-Angle Vector](#source-arbitrary)
- [Source-Video Gravity Problems 5 and 6](#source-gravity)
- [Lecture Application: Symmetric Gravitational Forces](#lecture-symmetry)
- [Summary](#summary)

## Prerequisites

- Interpret east and right as positive $x$, and north and up as positive $y$, unless another axis convention is stated.
- Use $F_x=F\cos\theta$ and $F_y=F\sin\theta$ when $\theta$ is measured counterclockwise from $+x$.
- Apply the Pythagorean theorem.
- Use inverse tangent in degree mode.
- Calculate a gravitational-force magnitude with $F_g=Gm_1m_2/r^2$.

---

<a id="introduction"></a>
## Introduction

A vector sum is easiest to control when every direction is turned into a sign before any arithmetic begins. Choose axes, record each vector's signed components, add down the columns, and reconstruct the resultant only after the ledger is closed:

$$
\boxed{
F_x=\sum_i F_{ix},
\qquad
F_y=\sum_i F_{iy},
\qquad
F=\sqrt{F_x^2+F_y^2},
\qquad
\theta=\operatorname{atan2}(F_y,F_x)
}.
$$

If `atan2` returns a negative angle and the problem asks for a standard direction in $0^\circ\leq\theta<360^\circ$, add $360^\circ$. If a calculator has only ordinary $\tan^{-1}(F_y/F_x)$, first identify the quadrant from the signs of $(F_x,F_y)$ and then place the reference angle in that quadrant.

A negative **component** says that the resultant points partly toward a negative axis. A magnitude such as $F=\sqrt{F_x^2+F_y^2}$ is never negative.

---

<a id="signed-ledger"></a>
## Build and Close the Signed Ledger

Use the same four entries for every vector:

| Vector | Magnitude and direction | $x$ component | $y$ component |
|---|---:|---:|---:|
| $\vec F_1$ | $F_1$ at $\theta_1$ | $F_1\cos\theta_1$ | $F_1\sin\theta_1$ |
| $\vec F_2$ | $F_2$ at $\theta_2$ | $F_2\cos\theta_2$ | $F_2\sin\theta_2$ |
| **Sum** |  | $F_x$ | $F_y$ |

In component notation, closing the two columns is exactly vector addition:

$$
\sum_i\langle F_{ix},F_{iy}\rangle
=\left\langle\sum_iF_{ix},\sum_iF_{iy}\right\rangle
=\langle F_x,F_y\rangle.
$$

Before calculating, check each sign against the drawing or direction words:

| Direction of a component | Sign |
|---|---:|
| right or east | $+$ in $x$ |
| left or west | $-$ in $x$ |
| up or north | $+$ in $y$ |
| down or south | $-$ in $y$ |

Then close the ledger in this order:

1. Add the $x$ column and the $y$ column separately.
2. Read the signs of $(F_x,F_y)$ to predict the quadrant or axis.
3. Calculate the nonnegative magnitude $F$.
4. Use `atan2` for the direction and verify that its quadrant matches step 2.

Use the final signs as a direction checksum:

| Signs of $(F_x,F_y)$ | Location of resultant |
|---|---|
| $(+,+)$ | quadrant I |
| $(-,+)$ | quadrant II |
| $(-,-)$ | quadrant III |
| $(+,-)$ | quadrant IV |
| one component is zero | on an axis; assign $0^\circ$, $90^\circ$, $180^\circ$, or $270^\circ$ by inspection |

This order separates direction decisions from arithmetic. It also prevents the common mistake of adding vector magnitudes when the vectors do not point in the same direction.

---

<a id="source-collinear"></a>
## Source-Video Controls: Collinear Vectors

The opening controls in `xS-gdFgZel0` at 0:00-2:22 use one-dimensional ledgers. With east as $+x$,

| Source case | Signed sum | Result |
|---|---:|---:|
| $100$ east and $50$ east | $100+50=+150$ | $150$ east |
| $200$ east and $120$ west | $200-120=+80$ | $80$ east |
| $60$ east and $90$ west | $60-90=-30$ | $30$ west |

With north as $+y$,

$$
80\ \text{north}+120\ \text{south}
=80-120=-40,
$$

so the result is $40$ south.

The negative signs in the last two calculations encode west and south. They do not create negative vector magnitudes.

**Source correction.** Parallel vectors do not always have magnitudes that can be added. Magnitudes add directly only when parallel vectors point in the same direction. Antiparallel vectors require a signed sum, as the three opposite-direction cases above show.

```quiz
type: radio
id: mct-p22-collinear-ledger
shuffle: true
content: |-
  Take east as positive $x$. A cart undergoes a $140\,\mathrm N$ force west and an $85\,\mathrm N$ force east. What is the net force?
options:
- id: mct-p22-collinear-ledger-a
  content: |-
    $55\,\mathrm N$ west
  correct: true
  feedback: |-
    The signed ledger is $F_x=-140+85=-55\,\mathrm N$. The negative component means west, while the force magnitude is the nonnegative value $55\,\mathrm N$.
- id: mct-p22-collinear-ledger-b
  content: |-
    $55\,\mathrm N$ east
  feedback: |-
    The magnitude $55\,\mathrm N$ is correct, but the sign is not. The larger force points west, so $F_x=-55\,\mathrm N$ and the direction is west.
- id: mct-p22-collinear-ledger-c
  content: |-
    $225\,\mathrm N$ west
  feedback: |-
    Adding the magnitudes ignores that the forces are antiparallel. Use the signed sum $-140+85$, not $-(140+85)$.
- id: mct-p22-collinear-ledger-d
  content: |-
    $225\,\mathrm N$ east
  feedback: |-
    The forces do not point in the same direction, so their magnitudes cannot be added. The west force is also larger than the east force, ruling out an eastward result.
- id: mct-p22-collinear-ledger-e
  content: |-
    $-55\,\mathrm N$ west
  feedback: |-
    The ledger component is $-55\,\mathrm N$, but a magnitude is not negative. Report $55\,\mathrm N$ west.
```

---

<a id="source-perpendicular"></a>
## Source-Video Worked Problems: Perpendicular Vectors and Quadrants

The next three problems in `xS-gdFgZel0` at 2:22-10:17 use perpendicular vectors.

### Source problem: $30$ east and $40$ north

$$
(F_x,F_y)=(30,40)\ \mathrm N.
$$

Thus

$$
F=\sqrt{30^2+40^2}=\boxed{50\ \mathrm N},
$$

and

$$
\theta=\operatorname{atan2}(40,30)=\boxed{53.1^\circ}.
$$

Both components are positive, so the first-quadrant angle is consistent with the ledger.

### Source problem: $50$ west and $120$ south

$$
(F_x,F_y)=(-50,-120)\ \mathrm N,
$$

so

$$
F=\sqrt{(-50)^2+(-120)^2}=\boxed{130\ \mathrm N}.
$$

The component pair lies in quadrant III. A reference-angle calculation gives $67.4^\circ$, and placing it in quadrant III gives

$$
\theta=180^\circ+67.4^\circ=\boxed{247.4^\circ}.
$$

Equivalently, `atan2(-120,-50)` gives $-112.6^\circ$, which normalizes to $247.4^\circ$.

### Source problem: $45$ east and $60$ south

$$
(F_x,F_y)=(45,-60)\ \mathrm N,
$$

and therefore

$$
F=\sqrt{45^2+(-60)^2}=\boxed{75\ \mathrm N}.
$$

This pair lies in quadrant IV. Its reference angle is $53.1^\circ$, so

$$
\theta=360^\circ-53.1^\circ=\boxed{306.9^\circ}.
$$

**Source refinement.** Memorized quadrant patches work, but `atan2(F_y,F_x)` is safer because it reads both component signs. Ordinary $\tan^{-1}(F_y/F_x)$ can return the same reference angle for resultants in different quadrants.

```quiz
type: radio
id: mct-p22-perpendicular-quadrant
shuffle: true
content: |-
  Take east as $+x$ and north as $+y$. Add a $24\,\mathrm N$ vector west to a $7\,\mathrm N$ vector north. Give the resultant as a magnitude and standard direction measured counterclockwise from $+x$.
options:
- id: mct-p22-perpendicular-quadrant-a
  content: |-
    $25\,\mathrm N$ at $163.7^\circ$
  correct: true
  feedback: |-
    The ledger closes at $(F_x,F_y)=(-24,7)\,\mathrm N$. Its magnitude is $\sqrt{24^2+7^2}=25\,\mathrm N$, and `atan2(7,-24)` gives the quadrant-II direction $163.7^\circ$.
- id: mct-p22-perpendicular-quadrant-b
  content: |-
    $25\,\mathrm N$ at $16.3^\circ$
  feedback: |-
    $16.3^\circ$ is only the reference angle. Because $F_x<0$ and $F_y>0$, the resultant is in quadrant II, so the standard direction is $180^\circ-16.3^\circ$.
- id: mct-p22-perpendicular-quadrant-c
  content: |-
    $31\,\mathrm N$ at $163.7^\circ$
  feedback: |-
    The direction uses the correct quadrant, but $24+7$ is not the magnitude of perpendicular components. Use $\sqrt{24^2+7^2}=25\,\mathrm N$.
- id: mct-p22-perpendicular-quadrant-d
  content: |-
    $25\,\mathrm N$ at $196.3^\circ$
  feedback: |-
    This angle lies in quadrant III, where both components would be negative. The northward component is positive, so the resultant must lie in quadrant II.
- id: mct-p22-perpendicular-quadrant-e
  content: |-
    $17\,\mathrm N$ at $163.7^\circ$
  feedback: |-
    Subtracting the perpendicular magnitudes does not reconstruct the resultant. Once the components are known, use the Pythagorean theorem.
```

---

<a id="source-arbitrary"></a>
## Source-Video Worked Problem: An Arbitrary-Angle Vector

The worked problem in `xS-gdFgZel0` at 10:17-15:18 adds a $100\,\mathrm N$ eastward vector and a $150\,\mathrm N$ vector at $30^\circ$ above $+x$. Put the calculator in degree mode and fill the ledger before summing:

| Vector | $x$ component | $y$ component |
|---|---:|---:|
| $100\,\mathrm N$ east | $100$ | $0$ |
| $150\,\mathrm N$ at $30^\circ$ | $150\cos30^\circ=129.9$ | $150\sin30^\circ=75.0$ |
| **Sum** | $F_x=229.9$ | $F_y=75.0$ |

Now reconstruct the resultant:

$$
F=\sqrt{(229.9)^2+(75.0)^2}
=241.8\ \mathrm N,
$$

$$
\theta=\operatorname{atan2}(75.0,229.9)
=18.1^\circ.
$$

Therefore,

$$
\boxed{\vec F_{\mathrm{net}}=241.8\ \mathrm N\text{ at }18.1^\circ}.
$$

The component pair $(+,+)$ predicts quadrant I before the inverse tangent is evaluated. A displayed result near $0.316$ instead of $18.1$ warns that the calculator is reporting radians, while the sign check catches a direction placed in the wrong quadrant.

```quiz
type: radio
id: mct-p22-arbitrary-components
shuffle: true
content: |-
  A $120\,\mathrm N$ vector points at $0^\circ$, and a $90\,\mathrm N$ vector points at $210^\circ$. Angles are measured counterclockwise from $+x$. What is their resultant, to the nearest tenth?
options:
- id: mct-p22-arbitrary-components-a
  content: |-
    $61.6\,\mathrm N$ at $313.1^\circ$
  correct: true
  feedback: |-
    The ledger gives $F_x=120+90\cos210^\circ=42.1\,\mathrm N$ and $F_y=90\sin210^\circ=-45.0\,\mathrm N$. Thus $F=61.6\,\mathrm N$, and `atan2(-45.0,42.1)` gives $-46.9^\circ$, or $313.1^\circ$ in standard form.
- id: mct-p22-arbitrary-components-b
  content: |-
    $61.6\,\mathrm N$ at $46.9^\circ$
  feedback: |-
    This uses the reference-angle magnitude but loses the negative $y$ component. Since $(F_x,F_y)=(+,-)$, the resultant belongs in quadrant IV.
- id: mct-p22-arbitrary-components-c
  content: |-
    $61.6\,\mathrm N$ at $226.9^\circ$
  feedback: |-
    This direction lies in quadrant III, which would require both summed components to be negative. The ledger's $x$ sum is positive.
- id: mct-p22-arbitrary-components-d
  content: |-
    $210\,\mathrm N$ at $105.0^\circ$
  feedback: |-
    Adding magnitudes and averaging angles treats vectors like scalars. Resolve each vector, add the signed component columns, and reconstruct only from the sums.
- id: mct-p22-arbitrary-components-e
  content: |-
    $203.0\,\mathrm N$ at $12.8^\circ$
  feedback: |-
    This treats the $210^\circ$ vector as though it were at $30^\circ$, making both of its components positive. At $210^\circ$, both cosine and sine are negative; preserve those signs in the ledger.
```

---

<a id="source-gravity"></a>
## Source-Video Gravity Problems 5 and 6

The gravitational applications in `Ep1jIhHdf2A` at 10:00-19:27 use the same component ledger after each force magnitude has been found from

$$
F_g=G\frac{m_1m_2}{r^2}.
$$

### Source-video Problem 5: Moon between the Sun and Earth

The prompt uses

$$
\begin{aligned}
m_M&=7.35\times10^{22}\ \mathrm{kg},
&m_E&=5.97\times10^{24}\ \mathrm{kg},\\
m_S&=1.99\times10^{30}\ \mathrm{kg},
&r_{ME}&=3.84\times10^8\ \mathrm m,\\
&&r_{SM}&=1.492\times10^{11}\ \mathrm m.
\end{aligned}
$$

The Sun, Moon, and Earth are collinear, with the Moon between the other two bodies. Choose $+x$ from the Moon toward Earth. Then the Earth pulls in $+x$ while the Sun pulls in $-x$:

$$
F_E
=G\frac{m_Em_M}{r_{ME}^2}
=1.985\times10^{20}\ \mathrm N,
$$

$$
F_S
=G\frac{m_Sm_M}{r_{SM}^2}
=4.383\times10^{20}\ \mathrm N.
$$

| Force on the Moon | $F_x$ | $F_y$ |
|---|---:|---:|
| Earth on Moon | $+1.985\times10^{20}$ | $0$ |
| Sun on Moon | $-4.383\times10^{20}$ | $0$ |
| **Sum** | $-2.398\times10^{20}$ | $0$ |

The negative component points toward the Sun under this axis choice. The requested magnitude and direction are

$$
\boxed{F_{\mathrm{net}}=2.398\times10^{20}\ \mathrm N\text{ toward the Sun}}.
$$

Subtracting works here because the ledger has established that the two forces are collinear and opposite. It is not a general rule for gravitational-force magnitudes.

### Source-video Problem 6: the same forces at right angles

Problem 6 keeps the two magnitudes but places the force directions at $90^\circ$. Choose a local $+x$ axis along the Sun's pull and $+y$ along Earth's pull:

| Force on the Moon | $F_x$ | $F_y$ |
|---|---:|---:|
| Sun on Moon | $4.383\times10^{20}$ | $0$ |
| Earth on Moon | $0$ | $1.985\times10^{20}$ |
| **Sum** | $4.383\times10^{20}$ | $1.985\times10^{20}$ |

Therefore,

$$
\begin{aligned}
F_{\mathrm{net}}
&=\sqrt{(4.383\times10^{20})^2+(1.985\times10^{20})^2}\\
&=\boxed{4.812\times10^{20}\ \mathrm N}.
\end{aligned}
$$

The resultant lies between the two force arrows and closer to the larger Sun-force component. Relative to the Sun-force direction, it is

$$
\tan^{-1}\!\left(\frac{1.985}{4.383}\right)=24.4^\circ
$$

toward the Earth-force direction. This is a relative angle, not a compass bearing. A global standard angle cannot be assigned without the diagram's orientation.

**Source correction.** The narration briefly says “Earth” when concluding Problem 6 and immediately corrects itself. The ledger and resultant here describe the net force **on the Moon**.

```quiz
type: radio
id: mct-p22-gravity-geometry
shuffle: true
content: |-
  A moon experiences a $9.0\times10^{20}\,\mathrm N$ pull toward a star and a $4.0\times10^{20}\,\mathrm N$ pull toward a planet. The force directions are perpendicular, but no compass orientation is supplied. Which conclusion is supported?
options:
- id: mct-p22-gravity-geometry-a
  content: |-
    The net force is $9.85\times10^{20}\,\mathrm N$, between the two pulls and closer to the starward direction.
  correct: true
  feedback: |-
    Perpendicular components give $F=\sqrt{9.0^2+4.0^2}\times10^{20}=\sqrt{97}\times10^{20}=9.85\times10^{20}\,\mathrm N$. The resultant lies closer to the larger starward component; no compass bearing follows without an oriented diagram.
- id: mct-p22-gravity-geometry-b
  content: |-
    The net force is $13.0\times10^{20}\,\mathrm N$ toward the star.
  feedback: |-
    The magnitudes cannot be added because the forces are perpendicular. Treat them as separate component entries and reconstruct with the Pythagorean theorem.
- id: mct-p22-gravity-geometry-c
  content: |-
    The net force is $5.0\times10^{20}\,\mathrm N$ toward the star.
  feedback: |-
    Subtracting magnitudes is valid only for opposite collinear forces. These pulls are perpendicular, so their resultant magnitude is larger than either component alone.
- id: mct-p22-gravity-geometry-d
  content: |-
    The net force is $9.85\times10^{20}\,\mathrm N$ at a standard direction of $24.0^\circ$.
  feedback: |-
    The magnitude and relative reference angle are available, but a standard direction measured from a global $+x$ axis is not. The prompt gives no compass orientation for either force arrow.
- id: mct-p22-gravity-geometry-e
  content: |-
    The larger pull completely cancels the smaller pull, leaving $9.0\times10^{20}\,\mathrm N$ toward the star.
  feedback: |-
    Perpendicular forces do not cancel. Cancellation requires equal components on the same axis with opposite signs.
```

---

<a id="lecture-symmetry"></a>
## Lecture Application: Symmetric Gravitational Forces

The M3-2 lecture places three identical masses at the vertices of an equilateral triangle of side $L$. On one mass, the other two exert equal forces of magnitude

$$
F_0=\frac{Gm^2}{L^2}.
$$

Choose $+x$ inward, toward the triangle's center, and $+y$ tangential. The two force arrows lie at $+30^\circ$ and $-30^\circ$ from the inward axis:

| Force | Inward component $F_x$ | Tangential component $F_y$ |
|---|---:|---:|
| force at $+30^\circ$ | $F_0\cos30^\circ$ | $+F_0\sin30^\circ$ |
| force at $-30^\circ$ | $F_0\cos30^\circ$ | $-F_0\sin30^\circ$ |
| **Sum** | $2F_0\cos30^\circ$ | $0$ |

The equal tangential components cancel because their signs are opposite. The equal inward components add because their signs match:

$$
\begin{aligned}
F_{\mathrm{net}}
&=2F_0\cos30^\circ\\
&=2\left(\frac{Gm^2}{L^2}\right)\frac{\sqrt3}{2}\\
&=\boxed{\sqrt3\frac{Gm^2}{L^2}}.
\end{aligned}
$$

For the lecture values $m=2.5\times10^{30}\,\mathrm{kg}$ and $L=1.8\times10^{12}\,\mathrm m$, this is approximately

$$
2.2\times10^{26}\ \mathrm N=220\ \mathrm{YN},
$$

directed inward. The subsequent orbital-speed calculation belongs with circular-orbit dynamics, and the system-energy calculation is outside this vector-addition lesson.

```quiz
type: radio
id: mct-p22-symmetry-components
shuffle: true
content: |-
  Two equal $46\,\mathrm N$ forces act symmetrically at $+35^\circ$ and $-35^\circ$ from an inward axis. What is their net force, to the nearest tenth?
options:
- id: mct-p22-symmetry-components-a
  content: |-
    $75.4\,\mathrm N$ inward
  correct: true
  feedback: |-
    The transverse entries $\pm46\sin35^\circ$ cancel, while the inward entries add: $F_{\mathrm{net}}=2(46)\cos35^\circ=75.4\,\mathrm N$ inward.
- id: mct-p22-symmetry-components-b
  content: |-
    $92.0\,\mathrm N$ inward
  feedback: |-
    This adds the full magnitudes as though both forces lay on the inward axis. Only each inward component, $46\cos35^\circ$, contributes to the net force.
- id: mct-p22-symmetry-components-c
  content: |-
    $52.8\,\mathrm N$ inward
  feedback: |-
    This doubles the sine component. The sine components are transverse and cancel; the matching inward components are the cosine components.
- id: mct-p22-symmetry-components-d
  content: |-
    $0\,\mathrm N$
  feedback: |-
    Symmetry cancels only the equal components with opposite signs. Both inward components have the same sign, so they add.
- id: mct-p22-symmetry-components-e
  content: |-
    $46.0\,\mathrm N$ inward
  feedback: |-
    The net is not one of the original forces. Both forces contribute an inward component, so add $46\cos35^\circ$ twice.
```

---

<a id="summary"></a>
## Summary

- Choose and label signed axes before resolving any vector.
- Enter every vector as a row in a component ledger; then add the $x$ and $y$ columns separately.
- Directly add magnitudes only for collinear vectors pointing in the same direction. Use signed components for all other cases.
- Reconstruct the resultant with
  $$
  F=\sqrt{F_x^2+F_y^2}.
  $$
  A component may be negative, but this magnitude is nonnegative.
- Predict the quadrant from the signs of $(F_x,F_y)$, then use
  $$
  \theta=\operatorname{atan2}(F_y,F_x).
  $$
- Keep the calculator in degree mode when directions are stated in degrees, and normalize a negative `atan2` result by adding $360^\circ$ when a standard angle is required.
- Symmetric components cancel only when they lie on the same axis with equal magnitude and opposite signs. Same-sign components add.
- For gravitational forces, calculate each magnitude first, assign its direction from the geometry, and then place it in the same signed ledger.
- Without an oriented diagram, report direction relative to the known force arrows rather than inventing a compass bearing.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
