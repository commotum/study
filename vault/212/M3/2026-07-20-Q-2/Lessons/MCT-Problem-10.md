# Solve Particle Equilibrium with Cable Components

<!--
lesson-id: 212-M3-046
topic-code: MTH212.M3.46
-->

## Table of Contents

- [Introduction](#introduction)
- [Read Components from Angles Above the Horizontal](#read-components-from-angles-above-the-horizontal)
- [Support a Sign with One Angled Cable](#support-a-sign-with-one-angled-cable)
- [Solve Two Angled-Cable Tensions](#solve-two-angled-cable-tensions)
- [Check Equilibrium Without Adding a Torque Equation](#check-equilibrium-without-adding-a-torque-equation)
- [Summary](#summary)

## Prerequisites

- Identify sine and cosine in a right triangle.
- Assign signs from a chosen $x$-$y$ coordinate system.
- Solve two linear equations by substitution.
- Use $W=mg$ for an object's weight.

---

<a id="introduction"></a>
## Introduction

When two cables meet at a knot, ring, or small connector and support a stationary load, treat the connector as a particle. Tension pulls away from the connector along each cable. The procedure is:

1. Draw every force from the common point.
2. Resolve each angled tension into signed horizontal and vertical components.
3. Write $\sum F_x=0$ and $\sum F_y=0$.
4. Solve the two equations for the two unknown tensions.

Use $+x$ to the right and $+y$ upward. For the common two-cable geometry, an explicit free-body diagram is

```text
       T_L, θ_L ↖     ↗ T_R, θ_R
                    ●
                    ↓  W = mg
```

Both $\theta_L$ and $\theta_R$ are measured above the horizontal. The recognition cue is that every force is concurrent: all force lines meet at the same point. This is a force-component problem, not a lever-arm problem.

---

<a id="read-components-from-angles-above-the-horizontal"></a>
## Read Components from Angles Above the Horizontal

Because each angle is measured from the horizontal, the horizontal component is adjacent to the angle and uses cosine. The vertical component is opposite the angle and uses sine. Set a calculator to degree mode before evaluating the source angles.

| Force | $x$ component | $y$ component |
| --- | ---: | ---: |
| Right cable, $T_R$ | $+T_R\cos\theta_R$ | $+T_R\sin\theta_R$ |
| Left cable, $T_L$ | $-T_L\cos\theta_L$ | $+T_L\sin\theta_L$ |
| Weight, $W=mg$ | $0$ | $-mg$ |

Equivalently, the signed component vectors are

$$
\vec T_R=\langle T_R\cos\theta_R,\ T_R\sin\theta_R\rangle,
$$

$$
\vec T_L=\langle -T_L\cos\theta_L,\ T_L\sin\theta_L\rangle,
\qquad
\vec W=\langle0,-mg\rangle.
$$

The signs come from the arrows, not from sine or cosine. Copy each arrow's left/right and up/down directions into the signs before doing algebra. Both cable tensions point upward, but their horizontal components point in opposite directions.

The component equations are therefore

$$
\boxed{T_R\cos\theta_R-T_L\cos\theta_L=0},
$$

$$
\boxed{T_R\sin\theta_R+T_L\sin\theta_L-mg=0}.
$$

A horizontal left cable is the special case $\theta_L=0^\circ$, so its components are $(-T_L,0)$.

```quiz
type: radio
id: mct-q2-p10-components
shuffle: true
content: |-
  A left-hand cable pulls on a knot with tension $400\,\mathrm N$ at $35^\circ$ above the horizontal. With $+x$ right and $+y$ up, which pair gives $(T_x,T_y)$?
options:
- id: mct-q2-p10-components-a
  content: |-
    $(-327.7\,\mathrm N,\ +229.4\,\mathrm N)$
  correct: true
  feedback: |-
    The cable points left and up, so $T_x<0$ and $T_y>0$. Since the angle is measured from horizontal, $T_x=-400\cos35^\circ=-327.7\,\mathrm N$ and $T_y=400\sin35^\circ=229.4\,\mathrm N$.
- id: mct-q2-p10-components-b
  content: |-
    $(+327.7\,\mathrm N,\ +229.4\,\mathrm N)$
  feedback: |-
    The component magnitudes are right, but the horizontal sign is not. A left-hand cable pulls the knot toward the left, so its $x$ component is negative.
- id: mct-q2-p10-components-c
  content: |-
    $(-229.4\,\mathrm N,\ +327.7\,\mathrm N)$
  feedback: |-
    This swaps sine and cosine. The angle is measured from the horizontal, so the horizontal component is adjacent and uses cosine; the vertical component uses sine.
- id: mct-q2-p10-components-d
  content: |-
    $(-327.7\,\mathrm N,\ -229.4\,\mathrm N)$
  feedback: |-
    Tension pulls along the cable away from the knot. This cable rises toward its support, so its vertical component points upward and is positive.
- id: mct-q2-p10-components-e
  content: |-
    $(0,\ +400\,\mathrm N)$
  feedback: |-
    These would be the components of a vertical cable. At $35^\circ$ above horizontal, the cable has both a leftward component and an upward component.
```

---

<a id="support-a-sign-with-one-angled-cable"></a>
## Support a Sign with One Angled Cable

**Source-video problem 1 (`qGvFAl5CK_c`, 00:07:47–00:12:30).** A $50\,\mathrm{kg}$ sign is supported at a junction by an angled cable $T_1$ and a horizontal cable $T_2$. In the source frame, $T_1$ rises to the right at $60^\circ$ above the horizontal, while $T_2$ pulls horizontally left.

```text
                         ↗ T₁, 60°
                 T₂ ←  ●
                       ↓  mg
```

The free-body diagram gives

$$
\sum F_y=0:
\qquad
T_1\sin60^\circ-mg=0,
$$

$$
\sum F_x=0:
\qquad
T_1\cos60^\circ-T_2=0.
$$

Solve the vertical equation first because it contains only $T_1$:

$$
T_1=\frac{mg}{\sin60^\circ}
=\frac{(50)(9.8)}{\sin60^\circ}
=565.8\,\mathrm N.
$$

Then use horizontal balance:

$$
T_2=T_1\cos60^\circ
=(565.8)\cos60^\circ
=282.9\,\mathrm N.
$$

The vertical check is $T_1\sin60^\circ=490\,\mathrm N=mg$. The horizontal check is $T_1\cos60^\circ=282.9\,\mathrm N=T_2$.

```quiz
type: radio
id: mct-q2-p10-one-angled
shuffle: true
content: |-
  A $36\,\mathrm{kg}$ sign is held by a cable $T_1$ at $55^\circ$ above the horizontal and a horizontal cable $T_2$ pulling the other way. Using $g=9.8\,\mathrm{m/s^2}$, which tensions keep the junction in equilibrium?
options:
- id: mct-q2-p10-one-angled-a
  content: |-
    $T_1=430.7\,\mathrm N$ and $T_2=247.0\,\mathrm N$
  correct: true
  feedback: |-
    Only $T_1$ supplies vertical support, so $T_1\sin55^\circ=mg=352.8\,\mathrm N$, giving $T_1=430.7\,\mathrm N$. Horizontal balance then gives $T_2=T_1\cos55^\circ=247.0\,\mathrm N$.
- id: mct-q2-p10-one-angled-b
  content: |-
    $T_1=247.0\,\mathrm N$ and $T_2=430.7\,\mathrm N$
  feedback: |-
    This swaps the cable roles. The angled cable must have an upward component equal to the full weight, so its tension must exceed its $247.0\,\mathrm N$ horizontal component.
- id: mct-q2-p10-one-angled-c
  content: |-
    $T_1=352.8\,\mathrm N$ and $T_2=202.4\,\mathrm N$
  feedback: |-
    $352.8\,\mathrm N$ is the weight, not the angled tension. Only $T_1\sin55^\circ$ is vertical, so $T_1$ must be larger than the weight.
- id: mct-q2-p10-one-angled-d
  content: |-
    $T_1=615.1\,\mathrm N$ and $T_2=503.9\,\mathrm N$
  feedback: |-
    These values use cosine for vertical support and sine for horizontal balance. Because the angle is measured from horizontal, vertical support is $T_1\sin55^\circ$ and the horizontal component is $T_1\cos55^\circ$.
- id: mct-q2-p10-one-angled-e
  content: |-
    $T_1=T_2=352.8\,\mathrm N$
  feedback: |-
    Static equilibrium requires opposite horizontal components to match, not the full cable magnitudes. Here $T_2=T_1\cos55^\circ$, so the horizontal cable has the smaller tension.
```

---

<a id="solve-two-angled-cable-tensions"></a>
## Solve Two Angled-Cable Tensions

**Source-video problem 2 (`qGvFAl5CK_c`, 00:12:30–00:17:56).** An $80\,\mathrm{kg}$ mass hangs from two cables. In the source frame, $T_1$ is the right cable at $40^\circ$ above horizontal, and $T_2$ is the left cable at $50^\circ$ above horizontal.

```text
              T₂, 50° ↖     ↗ T₁, 40°
                         ●
                         ↓  mg
```

The horizontal components cancel, while the two vertical components support the weight:

$$
T_1\cos40^\circ-T_2\cos50^\circ=0 \tag{1}
$$

$$
T_1\sin40^\circ+T_2\sin50^\circ=784\,\mathrm N \tag{2}
$$

Equation (1) is easiest to isolate for $T_2$:

$$
T_2=T_1\frac{\cos40^\circ}{\cos50^\circ}
=1.19175\,T_1.
$$

Substitute that expression into equation (2):

$$
T_1\left(\sin40^\circ+
\frac{\cos40^\circ}{\cos50^\circ}\sin50^\circ\right)
=784.
$$

Thus,

$$
T_1=503.945\ldots\,\mathrm N
\approx503.9\,\mathrm N,
$$

$$
T_2=600.579\ldots\,\mathrm N
\approx600.6\,\mathrm N.
$$

The video uses rounded intermediate factors and reports $T_2\approx600.5\,\mathrm N$. Carrying the trigonometric values through the final calculation gives $600.6\,\mathrm N$ to one decimal place.

The unequal angles produce unequal tensions. Equilibrium only requires

$$
T_1\cos40^\circ=T_2\cos50^\circ,
$$

not $T_1=T_2$.

```quiz
type: radio
id: mct-q2-p10-two-angled
shuffle: true
content: |-
  A $60\,\mathrm{kg}$ load is supported by a right cable $T_R$ at $35^\circ$ above horizontal and a left cable $T_L$ at $55^\circ$ above horizontal. Using $g=9.8\,\mathrm{m/s^2}$, which pair is correct?
options:
- id: mct-q2-p10-two-angled-a
  content: |-
    $T_R=337.3\,\mathrm N$ and $T_L=481.7\,\mathrm N$
  correct: true
  feedback: |-
    Horizontal balance gives $T_R\cos35^\circ=T_L\cos55^\circ$. Substitution into $T_R\sin35^\circ+T_L\sin55^\circ=588\,\mathrm N$ gives $T_R=337.3\,\mathrm N$ and $T_L=481.7\,\mathrm N$.
- id: mct-q2-p10-two-angled-b
  content: |-
    $T_R=481.7\,\mathrm N$ and $T_L=337.3\,\mathrm N$
  feedback: |-
    This swaps the tensions between the labeled cables. With $T_R\cos35^\circ=T_L\cos55^\circ$ and $\cos35^\circ>\cos55^\circ$, the left cable must have the larger tension.
- id: mct-q2-p10-two-angled-c
  content: |-
    $T_R=T_L=422.2\,\mathrm N$
  feedback: |-
    Equal cable magnitudes would not cancel horizontally because the cable angles differ. Horizontal equilibrium matches $T_R\cos35^\circ$ to $T_L\cos55^\circ$, so the tensions are unequal.
- id: mct-q2-p10-two-angled-d
  content: |-
    $T_R=34.4\,\mathrm N$ and $T_L=49.1\,\mathrm N$
  feedback: |-
    These values use the numerical mass $60$ as though it were a force. The downward force is the weight $mg=(60)(9.8)=588\,\mathrm N$, so both tensions must be larger by a factor of $9.8$.
- id: mct-q2-p10-two-angled-e
  content: |-
    $T_R=T_L=588\,\mathrm N$
  feedback: |-
    The weight is supported by the sum of the two upward components, not by each full tension separately. Each tension also has a horizontal component that must cancel the other cable's component.
```

---

<a id="check-equilibrium-without-adding-a-torque-equation"></a>
## Check Equilibrium Without Adding a Torque Equation

Use four checks after solving:

1. **Horizontal balance:** the leftward and rightward components have equal magnitudes.
2. **Vertical support:** the upward components add to $mg$.
3. **Units:** every tension and component is measured in newtons.
4. **Component bound:** no component magnitude exceeds the tension from which it was resolved.

The lecture notes state the full static-equilibrium conditions for an extended rigid body:

$$
\sum\vec F=0
\qquad\text{and}\qquad
\sum\tau=0.
$$

For the concurrent-force particle used here, the torque equation adds no independent information. About the knot, every force has zero lever arm. About any other origin, the net torque is

$$
\vec\tau_{\mathrm{net}}
=\vec r\times\sum\vec F
=0
$$

once the force balance is satisfied. Torque becomes necessary when the forces act at different points on an extended object, such as a beam or ladder.

```quiz
type: radio
id: mct-q2-p10-torque-check
shuffle: true
content: |-
  Three cable or weight forces meet at one small knot, and the two component equations give $\sum F_x=0$ and $\sum F_y=0$. Which statement is correct?
options:
- id: mct-q2-p10-torque-check-a
  content: |-
    The knot is in particle equilibrium; a torque equation about the knot reduces to $0=0$ and supplies no third equation.
  correct: true
  feedback: |-
    All forces act through the modeled particle, so their lever arms about the knot are zero. Once both force components balance, rotational equilibrium is automatic for this concurrent-force model.
- id: mct-q2-p10-torque-check-b
  content: |-
    A separate torque equation is still needed to solve the two cable tensions.
  feedback: |-
    The two unknown tensions are already determined by the two independent component equations. Because all force lines pass through the knot, torque about the knot yields only the identity $0=0$.
- id: mct-q2-p10-torque-check-c
  content: |-
    Static equilibrium requires the two cable tensions to have equal magnitudes.
  feedback: |-
    Force balance matches signed components, not necessarily whole magnitudes. Equal tensions follow only from a symmetric cable geometry; unequal angles generally require unequal tensions.
- id: mct-q2-p10-torque-check-d
  content: |-
    Each cable's vertical component must equal $mg/2$.
  feedback: |-
    The two vertical components must add to $mg$, but they split the load equally only in a symmetric geometry. Different cable angles generally give different vertical contributions.
- id: mct-q2-p10-torque-check-e
  content: |-
    Each full cable tension must equal $mg$.
  feedback: |-
    Only the vertical components support the weight, while the horizontal components cancel each other. A full cable tension equals $mg$ only in a special geometry, not as a general equilibrium rule.
```

---

<a id="summary"></a>
## Summary

For a stationary knot or small connector supported by two cables:

1. Draw each tension away from the point along its cable and draw $mg$ downward.
2. If an angle is measured above horizontal, use $T\cos\theta$ horizontally and $T\sin\theta$ vertically.
3. Assign signs from the arrow directions.
4. Write $\sum F_x=0$ and $\sum F_y=0$.
5. Isolate one tension in the simpler equation, substitute into the other, and keep guard digits until the end.
6. Check horizontal cancellation, vertical support of $mg$, and newton units.

Do not assume unequal-angle cables have equal tension. Do not add a torque equation when all forces meet at the modeled point; it gives no new constraint.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
