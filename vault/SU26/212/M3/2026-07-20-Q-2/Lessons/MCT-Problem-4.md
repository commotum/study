# Place an Added Mass to Hit a Target Center of Mass

<!--
lesson-id: 212-M3-040
topic-code: MTH212.M3.40
-->

## Table of Contents

- [Introduction](#introduction)
- [Predict Which Side of the Target](#predict-which-side-of-the-target)
- [Solve the Inverse Weighted Average](#solve-the-inverse-weighted-average)
- [Lecture-Note Bridge: Forward to Inverse](#lecture-note-bridge-forward-to-inverse)
- [Source-Video Problem 2: Place the 10 kg Mass](#source-video-problem-2)
- [Source-Video Truck and Load Problem](#source-video-truck-and-load-problem)
- [Check Physical Feasibility](#check-physical-feasibility)
- [Summary](#summary)

## Prerequisites

- Choose an origin and a positive coordinate direction.
- Use signed coordinates in the one-dimensional center-of-mass formula.
- Isolate one variable in a linear equation.
- Distinguish an object's physical extent from the coordinate of its own center of mass.

---

<a id="introduction"></a>
## Introduction

When a desired center of mass is given and one object's location is unknown, put the target coordinate on the left side of the weighted-average equation.

Let

- $M$ be the mass already present,
- $x_0$ be that existing object's or subsystem's own center-of-mass coordinate,
- $m$ be the added mass,
- $x$ be the added mass's unknown center coordinate, and
- $X$ be the desired center of mass of the combined system.

Then

$$
X=\frac{Mx_0+mx}{M+m}.
$$

Use one operational move:

1. Mark the origin and positive direction.
2. Predict which side of $X$ must contain the added mass.
3. Write $X$ on the left side of the weighted average.
4. Solve for $x$ symbolically, then substitute values.
5. Check the result against the diagram, the allowed interval, and the original equation.

Every coordinate in the equation must come from the same origin. Words such as “behind,” “above,” or “to the left” do not determine a sign until the positive axis has been chosen.

---

<a id="predict-which-side-of-the-target"></a>
## Predict Which Side of the Target

For positive masses, a center of mass lies between the component centers. If the existing center is left of the target, the added mass must be farther to the right than the target:

```text
x0 ---------------- X ---------------- x
existing center     target             added mass
```

Likewise, if $x_0>X$, the added mass must satisfy $x<X$. Placing the new mass between $x_0$ and $X$ cannot pull the combined center all the way to $X$.

```quiz
type: radio
id: mct-p4-side-prediction
shuffle: true
content: |-
  An existing object's center of mass is at $x_0=1.2\,\mathrm m$. A positive mass will be added so that the combined center is at $X=2.0\,\mathrm m$. What must be true of the added mass's center coordinate $x$?
options:
- id: mct-p4-side-prediction-a
  content: |-
    $x>2.0\,\mathrm m$
  correct: true
  feedback: |-
    The target must lie between the existing center and the added mass. Since $1.2<2.0$, the added mass must be on the far side of the target, so $x>2.0\,\mathrm m$.
- id: mct-p4-side-prediction-b
  content: |-
    $1.2\,\mathrm m<x<2.0\,\mathrm m$
  feedback: |-
    Both component centers would then lie below $2.0\,\mathrm m$, so their weighted average would also be below $2.0\,\mathrm m$. The added mass must lie beyond the target.
- id: mct-p4-side-prediction-c
  content: |-
    $x=2.0\,\mathrm m$
  feedback: |-
    Adding mass exactly at the target would move the center toward $2.0\,\mathrm m$ but would not bring it fully there while the existing mass remains centered at $1.2\,\mathrm m$.
- id: mct-p4-side-prediction-d
  content: |-
    $x<1.2\,\mathrm m$
  feedback: |-
    A mass to the left of the existing center would pull the combined center left, away from the target at $2.0\,\mathrm m$.
- id: mct-p4-side-prediction-e
  content: |-
    The side cannot be predicted without knowing the two masses.
  feedback: |-
    The masses determine how far beyond the target the added mass must go, but not which side. Positive weights guarantee that the target lies between the two component centers.
```

---

<a id="solve-the-inverse-weighted-average"></a>
## Solve the Inverse Weighted Average

Start with the target equation and isolate $x$ before inserting numbers:

$$
\begin{aligned}
X&=\frac{Mx_0+mx}{M+m},\\
X(M+m)&=Mx_0+mx,\\
mx&=X(M+m)-Mx_0,\\
\boxed{x&=\frac{X(M+m)-Mx_0}{m}}.
\end{aligned}
$$

An equivalent form makes the side prediction visible:

$$
\boxed{x=X+\frac{M}{m}(X-x_0)}.
$$

The displacement $x-X$ has the same sign as $X-x_0$. A smaller added mass requires a larger placement distance beyond the target.

| Symbol | Meaning |
|---|---|
| $x_0$ | Existing object's own center coordinate |
| $X$ | Desired center of the combined system |
| $x$ | Added object's own center coordinate |
| Allowed interval | Geometric region in which the added object can actually fit |

An extended object is represented by its mass at its own center of mass. Its length does not replace $x_0$ in the numerator.

**Example:** A $6\,\mathrm{kg}$ object has its center at $x_0=1.0\,\mathrm m$. Where should a $3\,\mathrm{kg}$ mass be centered to put the combined center at $X=3.0\,\mathrm m$?

The added mass must lie beyond $3.0\,\mathrm m$. Symbolically,

$$
x=\frac{X(M+m)-Mx_0}{m}.
$$

Substitute only after isolating $x$:

$$
x=\frac{(3.0)(6+3)-(6)(1.0)}{3}
=\frac{27-6}{3}
=7.0\,\mathrm m.
$$

The ordering $1.0<3.0<7.0$ agrees with the prediction.

```quiz
type: radio
id: mct-p4-direct-control
shuffle: true
content: |-
  A $10\,\mathrm{kg}$ object has its center at $x_0=2.0\,\mathrm m$. Where should a $5\,\mathrm{kg}$ mass be centered so that the combined center is $X=4.0\,\mathrm m$?
options:
- id: mct-p4-direct-control-a
  content: |-
    $8.0\,\mathrm m$
  correct: true
  feedback: |-
    Using $x=[X(M+m)-Mx_0]/m$ gives $x=[4(15)-10(2)]/5=40/5=8.0\,\mathrm m$. The target lies between $2.0$ and $8.0\,\mathrm m$, as required.
- id: mct-p4-direct-control-b
  content: |-
    $4.0\,\mathrm m$
  feedback: |-
    This places the added mass at the target. The existing $10\,\mathrm{kg}$ center at $2.0\,\mathrm m$ would keep the combined center below $4.0\,\mathrm m$.
- id: mct-p4-direct-control-c
  content: |-
    $6.0\,\mathrm m$
  feedback: |-
    This does not account for the existing object being twice as massive as the added mass. The added center must be $4+(10/5)(4-2)=8.0\,\mathrm m$.
- id: mct-p4-direct-control-d
  content: |-
    $12.0\,\mathrm m$
  feedback: |-
    This comes from $X(M+m)/m$ and omits the existing moment $Mx_0$. Subtract $10(2)$ before dividing by the added mass.
- id: mct-p4-direct-control-e
  content: |-
    $-8.0\,\mathrm m$
  feedback: |-
    The magnitude matches the required coordinate, but the sign contradicts the axis and the side prediction. A negative placement would pull the center away from the positive target.
```

---

<a id="lecture-note-bridge-forward-to-inverse"></a>
## Lecture-Note Bridge: Forward to Inverse

**Paired lecture-note example:** Two point masses are separated by $L$. The origin is at $m_1$, so $x_1=0$ and $x_2=L$, with $m_1=3m_2$.

The forward calculation gives

$$
X=\frac{m_1(0)+m_2L}{m_1+m_2}
=\frac{m_2L}{3m_2+m_2}
=\frac{L}{4}.
$$

For $L=0.88\,\mathrm m$,

$$
X=\frac{0.88}{4}=0.22\,\mathrm m.
$$

The inverse form runs the same equation in the other direction. If the smaller mass's coordinate is unknown and the desired center is $X$, then

$$
x_2=\frac{X(3m_2+m_2)-(3m_2)(0)}{m_2}=4X.
$$

Thus $X=0.22\,\mathrm m$ requires $x_2=0.88\,\mathrm m$. The forward and inverse answers check one another without changing the origin.

---

<a id="source-video-problem-2"></a>
## Source-Video Problem 2: Place the 10 kg Mass

**Source-video worked Problem 2 (`2uszSnvzBEU`, 2:04–4:19):** An $8\,\mathrm{kg}$ mass is at $y_1=3.0\,\mathrm m$. Where should a $10\,\mathrm{kg}$ mass be placed so that the combined center is $y_{\mathrm{cm}}=4.5\,\mathrm m$?

Before calculating, the unknown mass must be above $4.5\,\mathrm m$ because the existing center at $3.0\,\mathrm m$ lies below the target:

```text
y=3.0 m              y=4.5 m                 y2>4.5 m
8 kg                 target                  10 kg
```

Write the desired center on the left and solve symbolically:

$$
\begin{aligned}
y_{\mathrm{cm}}
&=\frac{m_1y_1+m_2y_2}{m_1+m_2},\\
y_2
&=\frac{y_{\mathrm{cm}}(m_1+m_2)-m_1y_1}{m_2}.
\end{aligned}
$$

Now substitute:

$$
\begin{aligned}
y_2
&=\frac{(4.5)(8+10)-(8)(3)}{10}\\
&=\frac{81-24}{10}\\
&=5.7\,\mathrm m.
\end{aligned}
$$

The result passes both checks:

$$
3.0<4.5<5.7,
$$

and

$$
\frac{(8)(3)+(10)(5.7)}{18}
=\frac{81}{18}
=4.5\,\mathrm m.
$$

```quiz
type: radio
id: mct-p4-signed-mirror
shuffle: true
content: |-
  A $5\,\mathrm{kg}$ object has its center at $x_0=-2.0\,\mathrm m$. Where should a $3\,\mathrm{kg}$ mass be centered so that the combined center is $X=-0.50\,\mathrm m$?
options:
- id: mct-p4-signed-mirror-a
  content: |-
    $+2.0\,\mathrm m$
  correct: true
  feedback: |-
    Keep the signed coordinate: $x=[(-0.50)(8)-5(-2.0)]/3=(-4+10)/3=+2.0\,\mathrm m$. The target $-0.50$ lies between $-2.0$ and $+2.0\,\mathrm m$.
- id: mct-p4-signed-mirror-b
  content: |-
    $-2.0\,\mathrm m$
  feedback: |-
    Placing both centers at $-2.0\,\mathrm m$ would leave the combined center there. The added mass must lie on the positive side of the target to move the center from $-2.0$ to $-0.50\,\mathrm m$.
- id: mct-p4-signed-mirror-c
  content: |-
    $-4.67\,\mathrm m$
  feedback: |-
    This treats $x_0=-2.0\,\mathrm m$ as though it contributed $+10\,\mathrm{kg\,m}$ before subtraction. Its actual weighted term is $5(-2)=-10\,\mathrm{kg\,m}$.
- id: mct-p4-signed-mirror-d
  content: |-
    $+0.50\,\mathrm m$
  feedback: |-
    This changes the sign of the target and does not solve the weighted average. Substitution would give a combined center of $-1.06\,\mathrm m$, not $-0.50\,\mathrm m$.
- id: mct-p4-signed-mirror-e
  content: |-
    $+0.75\,\mathrm m$
  feedback: |-
    This results from dividing the remaining weighted-position numerator by the total mass instead of the added mass. After isolating $3x$, divide by $3\,\mathrm{kg}$.
```

---

<a id="source-video-truck-and-load-problem"></a>
## Source-Video Truck and Load Problem

**Source-video worked problem (`2uszSnvzBEU`, 9:26–12:50):** A $10\,\mathrm m$ long truck has mass $4000\,\mathrm{kg}$ and its own center of mass $4.0\,\mathrm m$ behind the front. Where should a $1400\,\mathrm{kg}$ load be centered so that the combined center is at the truck's midpoint, $5.0\,\mathrm m$ from the front?

Choose the front as $x=0$ and let positive $x$ point toward the rear:

```text
front                                                        rear
x=0        truck COM       target            load              x=10 m
|-------------x=4 m---------x=5 m-------------x=?----------------|
```

The truck's $10\,\mathrm m$ length describes its physical extent. Its $4000\,\mathrm{kg}$ is represented at the truck's own center coordinate, $x_{\mathrm{truck}}=4.0\,\mathrm m$, not at the geometric midpoint.

**Source wording correction:** The narration briefly says the center is “4 meters behind the truck.” The stated problem and its diagram use $4\,\mathrm m$ behind the **front of the truck**, so the correct coordinate is $x_{\mathrm{truck}}=+4.0\,\mathrm m$.

Since the target is behind the truck's current center, the load must be centered farther back than $x=5.0\,\mathrm m$. Solve first, then substitute:

$$
\begin{aligned}
x_{\mathrm{load}}
&=\frac{X(M+m)-Mx_{\mathrm{truck}}}{m}\\
&=\frac{(5.0)(4000+1400)-(4000)(4.0)}{1400}\\
&=\frac{27000-16000}{1400}\\
&=7.857\ldots\,\mathrm m\\
&\approx7.86\,\mathrm m.
\end{aligned}
$$

The load's center should be $7.86\,\mathrm m$ behind the front. This is a positive coordinate because the positive axis points from front to rear. Its center lies within $0\leq x\leq10\,\mathrm m$, so the placement fits the source's point-load model. A load with appreciable length would also need an edge-clearance check.

```quiz
type: radio
id: mct-p4-truck-control
shuffle: true
content: |-
  An $8.0\,\mathrm m$ van has mass $2400\,\mathrm{kg}$ and its own center at $x_0=3.0\,\mathrm m$ from the front. The front is $x=0$, and positive $x$ points toward the rear. Where should an $800\,\mathrm{kg}$ cargo load be centered to put the combined center at $X=3.75\,\mathrm m$?
options:
- id: mct-p4-truck-control-a
  content: |-
    $x=6.0\,\mathrm m$ from the front
  correct: true
  feedback: |-
    The inverse average gives $x=[3.75(3200)-2400(3.0)]/800=(12000-7200)/800=6.0\,\mathrm m$. This lies beyond the target and inside the van.
- id: mct-p4-truck-control-b
  content: |-
    $x=-6.0\,\mathrm m$ from the front
  feedback: |-
    “Toward the rear” is the positive direction, so a load behind the front has a positive coordinate. A negative placement would also pull the center away from the target.
- id: mct-p4-truck-control-c
  content: |-
    $x=3.75\,\mathrm m$ from the front
  feedback: |-
    Placing the load at the target would not overcome the existing van center at $3.0\,\mathrm m$. The added center must lie beyond $3.75\,\mathrm m$.
- id: mct-p4-truck-control-d
  content: |-
    $x=4.5\,\mathrm m$ from the front
  feedback: |-
    This placement is not far enough back for the lighter cargo. It would give $X=[2400(3)+800(4.5)]/3200=3.375\,\mathrm m$.
- id: mct-p4-truck-control-e
  content: |-
    $x=15.0\,\mathrm m$ from the front
  feedback: |-
    This uses $X(M+m)/m$ but omits the van's existing weighted-position term $Mx_0$. Subtract $2400(3.0)$ before dividing by $800$.
```

---

<a id="check-physical-feasibility"></a>
## Check Physical Feasibility

An algebraic coordinate is not automatically a usable placement. Check:

1. **Predicted side:** $X$ must lie between $x_0$ and $x$ for positive masses.
2. **Allowed interval:** The added object's center must lie where the geometry permits it.
3. **Object extent:** If the added object has nonzero length, fitting its center in the interval may not guarantee that the whole object fits.
4. **Origin and sign:** Retain the same origin and positive direction used in the equation.
5. **Forward substitution:** Insert the solved coordinate into the original weighted average and recover $X$.

```quiz
type: radio
id: mct-p4-feasibility
shuffle: true
content: |-
  A platform occupies $0\leq x\leq5.0\,\mathrm m$. A $100\,\mathrm{kg}$ assembly has its center at $x_0=2.0\,\mathrm m$. A $10\,\mathrm{kg}$ component is to be added so that the combined center is $X=2.5\,\mathrm m$. Which conclusion is correct?
options:
- id: mct-p4-feasibility-a
  content: |-
    The equation requires $x=7.5\,\mathrm m$, so the target is impossible if the component's center must stay on the platform.
  correct: true
  feedback: |-
    Solving gives $x=[2.5(110)-100(2.0)]/10=7.5\,\mathrm m$. The algebra is consistent, but $7.5\,\mathrm m$ lies outside the allowed interval $[0,5.0]$.
- id: mct-p4-feasibility-b
  content: |-
    Place the component at $x=2.5\,\mathrm m$ because that is the desired center.
  feedback: |-
    A component at the target cannot fully move the existing center from $2.0$ to $2.5\,\mathrm m$. The combined center would remain below $2.5\,\mathrm m$.
- id: mct-p4-feasibility-c
  content: |-
    Place the component at $x=5.0\,\mathrm m$; any point beyond the target gives the exact desired center.
  feedback: |-
    Being on the correct side is necessary but not sufficient. At $x=5.0\,\mathrm m$, the combined center is $(200+50)/110\approx2.27\,\mathrm m$, not $2.5\,\mathrm m$.
- id: mct-p4-feasibility-d
  content: |-
    The equation requires $x=-7.5\,\mathrm m$, so the target is impossible because the coordinate is negative.
  feedback: |-
    The required coordinate is positive: $[275-200]/10=+7.5\,\mathrm m$. The impossibility comes from exceeding the platform's upper bound, not from a negative sign.
- id: mct-p4-feasibility-e
  content: |-
    No placement can be computed because the assembly has physical extent rather than being a point mass.
  feedback: |-
    An extended assembly is represented by its total mass at its own center coordinate. Its physical extent matters in the final fit check, not in whether the weighted-average equation can be written.
```

---

<a id="summary"></a>
## Summary

- Use one origin and positive direction for the existing center, target, and added center.
- Predict the added mass's side before calculating: the target must lie between the old and added centers.
- Put the desired center on the left:
  $$
  X=\frac{Mx_0+mx}{M+m}.
  $$
- Solve symbolically before substituting:
  $$
  x=\frac{X(M+m)-Mx_0}{m}
  =X+\frac{M}{m}(X-x_0).
  $$
- Use an extended object's own center coordinate, not its total length, in the numerator.
- Check the solved coordinate against the predicted side, the physical interval, and the original weighted average.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
