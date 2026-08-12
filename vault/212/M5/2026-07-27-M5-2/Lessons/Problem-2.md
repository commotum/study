# Wave Speed in a Wire Tensioned by a Hanging Mass

<!--
lesson-id: 212-M5-009
topic-code: MTH212.M5.09
-->

## Table of Contents

- [Introduction](#introduction)
- [Build Tension and Linear Density](#build-tension-and-linear-density)
- [Combine the Ingredients Into Wave Speed](#combine-the-ingredients-into-wave-speed)
- [Keep the Two Masses in Their Own Roles](#keep-the-two-masses-in-their-own-roles)
- [Match the Diagram and Answer Form](#match-the-diagram-and-answer-form)
- [Summary](#summary)

## Prerequisites

- Use equilibrium to identify the tension supplied by a stationary hanging mass.
- Compute mass per unit length.
- Evaluate a quotient inside a square root.

---

<a id="introduction"></a>
## Introduction

For a transverse wave on a stretched wire,

$$
v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}},
$$

where $F_T$ is the wire tension and $\mu$ is its linear mass density. In a wall–pulley–block setup, a stationary hanging block of mass $M$ supplies the tension, while the horizontal wire segment's mass $m_w$ and length $L$ determine its linear density:

$$
F_T=Mg,
\qquad
\mu=\frac{m_w}{L}.
$$

The task is to assign each given quantity to the correct physical role and then evaluate the wave-speed formula.

| Symbol | Physical role |
| --- | --- |
| $M$ | hanging block mass; determines $F_T=Mg$ |
| $m_w$ | mass of the horizontal vibrating wire segment |
| $L$ | length of that same wire segment |
| $\mu$ | wire mass per unit length, $m_w/L$ |
| $v_{\mathrm{wave}}$ | propagation speed of the transverse wave |

---

<a id="build-tension-and-linear-density"></a>
## Build Tension and Linear Density

Because the hanging block is stationary, its vertical forces balance:

$$
F_T-Mg=0
\quad\Longrightarrow\quad
F_T=Mg.
$$

The mass density of the vibrating wire segment is its own mass divided by its length:

$$
\mu=\frac{m_w}{L}.
$$

**Example:** A stationary $0.50\ \mathrm{kg}$ block tensions a wire segment with mass $0.025\ \mathrm{kg}$ and length $2.0\ \mathrm{m}$. Use $g=10\ \mathrm{m}/\mathrm{s}^2$. Find $F_T$ and $\mu$.

**Explanation**

$$
F_T=Mg=(0.50)(10)=5.0\ \mathrm{N},
$$

and

$$
\mu=\frac{m_w}{L}
=\frac{0.025\ \mathrm{kg}}{2.0\ \mathrm{m}}
=0.0125\ \mathrm{kg}/\mathrm{m}.
$$

```quiz
type: radio
id: problem-2-wire-speed-q1
content: |-
  A stationary block of mass $M=0.60\ \mathrm{kg}$ tensions a wire segment with $m_w=0.030\ \mathrm{kg}$ and $L=1.5\ \mathrm{m}$. Use $g=10\ \mathrm{m}/\mathrm{s}^2$. Which pair gives the tension and linear mass density?
options:
- id: a
  content: |-
    $F_T=6.0\ \mathrm{N}$ and $\mu=0.020\ \mathrm{kg}/\mathrm{m}$
  correct: true
  feedback: |-
    Because the hanging block is stationary, the wire tension balances its weight: $F_T=Mg=6.0\ \mathrm{N}$. Linear density belongs to the wire segment itself, so $\mu=m_w/L=0.020\ \mathrm{kg}/\mathrm{m}$.
- id: b
  content: |-
    $F_T=0.30\ \mathrm{N}$ and $\mu=0.40\ \mathrm{kg}/\mathrm{m}$
  feedback: |-
    This swaps the objects' physical roles. The hanging mass $M=0.60\ \mathrm{kg}$ supplies the tension through $Mg$, while the wire's own mass $m_w=0.030\ \mathrm{kg}$ is spread over $L$ and determines $\mu$.
- id: c
  content: |-
    $F_T=6.0\ \mathrm{N}$ and $\mu=0.045\ \mathrm{kg}/\mathrm{m}$
  feedback: |-
    The tension correctly balances the hanging weight, but the density multiplies wire mass by length. Linear density means mass per unit length, so $\mu=0.030/1.5=0.020\ \mathrm{kg}/\mathrm{m}$ rather than $0.045\ \mathrm{kg}/\mathrm{m}$.
- id: d
  content: |-
    $F_T=0.60\ \mathrm{N}$ and $\mu=0.020\ \mathrm{kg}/\mathrm{m}$
  feedback: |-
    The density is correct, but this reports the block's mass value as a force. Tension balances weight, so the mass must be multiplied by $g$: $F_T=(0.60)(10)=6.0\ \mathrm{N}$, not $0.60\ \mathrm{N}$.
- id: e
  content: |-
    $F_T=15\ \mathrm{N}$ and $\mu=0.050\ \mathrm{kg}/\mathrm{m}$
  feedback: |-
    Neither value respects the quantities' roles: $15$ comes from $gL$, although length does not set the hanging weight, and $0.050$ is not the wire mass per length. Use $F_T=Mg=6.0\ \mathrm{N}$ and $\mu=m_w/L=0.020\ \mathrm{kg}/\mathrm{m}$.
```

---

<a id="combine-the-ingredients-into-wave-speed"></a>
## Combine the Ingredients Into Wave Speed

Substitute $F_T=Mg$ and $\mu=m_w/L$ into $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$:

$$
v_{\mathrm{wave}}
=\sqrt{\frac{Mg}{m_w/L}}
=\sqrt{\frac{MgL}{m_w}}.
$$

This direct formula uses the hanging mass, wire mass, wire length, and gravitational acceleration.

The units confirm that the expression produces speed:

$$
\left[\frac{MgL}{m_w}\right]
=\frac{(\mathrm{kg})(\mathrm{m}/\mathrm{s}^2)(\mathrm{m})}
{\mathrm{kg}}
=\mathrm{m}^2/\mathrm{s}^2.
$$

Taking the square root gives $\mathrm{m}/\mathrm{s}$.

**Example:** Use $M=0.50\ \mathrm{kg}$, $m_w=0.025\ \mathrm{kg}$, $L=2.0\ \mathrm{m}$, and $g=10\ \mathrm{m}/\mathrm{s}^2$.

**Explanation**

Keep the whole quotient beneath the radical:

$$
v_{\mathrm{wave}}
=\sqrt{\frac{(0.50)(10)(2.0)}{0.025}}
=\sqrt{400}
=20\ \mathrm{m}/\mathrm{s}.
$$

Evaluate in the same order shown by the formula:

1. Multiply $MgL$.
2. Divide by $m_w$.
3. Take the square root.
4. Round only the final speed.

This keeps the entire quotient inside the radical.

```quiz
type: radio
id: problem-2-wire-speed-q2
content: |-
  A stationary block with $M=0.60\ \mathrm{kg}$ tensions a wire segment with $m_w=0.040\ \mathrm{kg}$ and $L=1.5\ \mathrm{m}$. Use $g=10\ \mathrm{m}/\mathrm{s}^2$. What is the transverse wave speed?
options:
- id: a
  content: |-
    $3.9\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This is approximately $\sqrt{gL}=\sqrt{15}$, which drops both masses and therefore ignores tension and wire density. Using $F_T=Mg$ and $\mu=m_w/L$ gives the full radicand $MgL/m_w=225$ and speed $15\ \mathrm{m}/\mathrm{s}$.
- id: b
  content: |-
    $9.0\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This stops at the numerator $MgL=9.0$ and does not account for the wire mass or square-root dependence. Wave speed is $\sqrt{MgL/m_w}=\sqrt{225}=15\ \mathrm{m}/\mathrm{s}$.
- id: c
  content: |-
    $15\ \mathrm{m}/\mathrm{s}$
  correct: true
  feedback: |-
    The stationary block sets $F_T=Mg$, and the wire segment sets $\mu=m_w/L$, so $v_{\mathrm{wave}}=\sqrt{F_T/\mu}=\sqrt{MgL/m_w}$. The given values make the radicand $225\ \mathrm{m}^2/\mathrm{s}^2$ and the speed $15\ \mathrm{m}/\mathrm{s}$.
- id: d
  content: |-
    $150\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This divides the hanging weight factor by wire mass but omits the length needed to turn wire mass into linear density. It also stops before the square root; the complete expression is $v_{\mathrm{wave}}=\sqrt{MgL/m_w}=15\ \mathrm{m}/\mathrm{s}$.
- id: e
  content: |-
    $225\ \mathrm{m}/\mathrm{s}$
  feedback: |-
    This reports $MgL/m_w=225$, which has units of speed squared. The wave-speed formula is $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$, so the requested speed is the positive square root, $15\ \mathrm{m}/\mathrm{s}$.
```

---

<a id="keep-the-two-masses-in-their-own-roles"></a>
## Keep the Two Masses in Their Own Roles

The two masses are not interchangeable:

- $M$ is the hanging block mass, so it sets the tension $F_T=Mg$.
- $m_w$ is the mass of the vibrating wire segment, so it sets $\mu=m_w/L$.

Thus,

$$
v_{\mathrm{wave}}=\sqrt{\frac{MgL}{m_w}}.
$$

A larger hanging mass raises the speed by raising the tension. A larger wire mass lowers the speed by raising the linear density.

The square root controls the size of these changes:

$$
M\text{ multiplied by }k
\Longrightarrow v_{\mathrm{wave}}\text{ multiplied by }\sqrt{k},
$$

while

$$
m_w\text{ multiplied by }k
\Longrightarrow v_{\mathrm{wave}}\text{ divided by }\sqrt{k}.
$$

**Example:** For $M=0.90\ \mathrm{kg}$, $m_w=0.030\ \mathrm{kg}$, $L=1.2\ \mathrm{m}$, and $g=10\ \mathrm{m}/\mathrm{s}^2$, choose the correct setup.

**Explanation**

Place $M$ in the numerator through $Mg$ and place $m_w$ in the denominator:

$$
v_{\mathrm{wave}}=\sqrt{\frac{(0.90)(10)(1.2)}{0.030}}.
$$

```quiz
type: radio
id: problem-2-wire-speed-q3
content: |-
  For $M=0.80\ \mathrm{kg}$, $m_w=0.020\ \mathrm{kg}$, $L=1.5\ \mathrm{m}$, and $g=10\ \mathrm{m}/\mathrm{s}^2$, which expression correctly gives the transverse wave speed?
options:
- id: a
  content: |-
    $\displaystyle \sqrt{\frac{(0.80)(10)(1.5)}{0.020}}$
  correct: true
  feedback: |-
    The hanging block supplies $F_T=Mg$, while the vibrating wire's own mass and length supply $\mu=m_w/L$. Substituting those roles into $v_{\mathrm{wave}}=\sqrt{F_T/\mu}$ gives exactly $\sqrt{(0.80)(10)(1.5)/0.020}$.
- id: b
  content: |-
    $\displaystyle \sqrt{\frac{(0.020)(10)(1.5)}{0.80}}$
  feedback: |-
    This lets the wire's small mass generate the tension and spreads the hanging block's mass along the wire. Those roles are reversed: $M$ belongs in $F_T=Mg$ and $m_w$ belongs in $\mu=m_w/L$, so the correct ratio is $MgL/m_w$.
- id: c
  content: |-
    $\displaystyle \frac{(0.80)(10)(1.5)}{0.020}$
  feedback: |-
    This expression is $F_T/\mu$, which has units of speed squared, not speed. The propagation speed is the positive square root of that ratio, so the entire quotient must remain under the radical.
- id: d
  content: |-
    $\displaystyle \sqrt{\frac{(0.80)(0.020)}{(10)(1.5)}}$
  feedback: |-
    This multiplies the two masses and divides by $gL$, losing both the tension-over-density structure and the units of speed. Substituting $F_T=Mg$ and $\mu=m_w/L$ places $MgL$ in the numerator and $m_w$ alone in the denominator.
- id: e
  content: |-
    $\displaystyle \sqrt{\frac{(0.80)(10)}{(0.020)(1.5)}}$
  feedback: |-
    This treats linear density as though it were $m_wL$. Since $\mu=m_w/L$, dividing by $\mu$ means multiplying by $L/m_w$, so $L$ moves to the numerator and the radicand is $MgL/m_w$.
```

---

<a id="match-the-diagram-and-answer-form"></a>
## Match the Diagram and Answer Form

Read the diagram as a physical map: $L$ labels the horizontal vibrating wire segment, $m_w$ is that segment's mass, and the hanging block $M$ supplies the tension.

**Example:** A block of mass $M$ hangs from a wire over a pulley. The wire segment between the wall and pulley has length $L$ and mass $m_w$. Find the speed at which a transverse wave propagates along the wire. Assume the hanging block is stationary, so the wire tension is $F_T=Mg$.

Use $M=0.82\ \mathrm{kg}$, $m_w=0.018\ \mathrm{kg}$, $L=1.4\ \mathrm{m}$, and $g=9.8\ \mathrm{m}/\mathrm{s}^2$.

![](<../Source/Images/wire-pulley-hanging-mass.png>)

Enter the wave speed in meters per second as a number only.

**Explanation**

The wire's linear mass density is $\mu=m_w/L$, and the stationary block makes $F_T=Mg$. Therefore,

$$
\begin{aligned}
v_{\mathrm{wave}}
&=\sqrt{\frac{F_T}{\mu}}\\
&=\sqrt{\frac{MgL}{m_w}}\\
&=\sqrt{\frac{(0.82)(9.8)(1.4)}{0.018}}\\
&=24.999\ldots\ \mathrm{m}/\mathrm{s}.
\end{aligned}
$$

The measured givens have two significant figures, so $v_{\mathrm{wave}}=25\ \mathrm{m}/\mathrm{s}$. Enter $25$.

```quiz
type: radio
id: problem-2-wire-speed-q4
content: |-
  A stationary hanging block has $M=0.50\ \mathrm{kg}$. The horizontal wire segment has $m_w=0.020\ \mathrm{kg}$ and $L=1.6\ \mathrm{m}$. Use $g=10\ \mathrm{m}/\mathrm{s}^2$. The answer field accepts the wave speed in meters per second as a number only. Which number should be entered?
options:
- id: a
  content: |-
    $5$
  feedback: |-
    This reports the wire tension's numerical value, $F_T=Mg=5\ \mathrm{N}$, as though it were a speed. Tension is only one input; combining it with $\mu=m_w/L$ gives $v_{\mathrm{wave}}=20\ \mathrm{m}/\mathrm{s}$.
- id: b
  content: |-
    $16$
  feedback: |-
    This multiplies gravity by length but omits how the hanging mass sets tension and the wire mass sets density. The complete relation is $v_{\mathrm{wave}}=\sqrt{MgL/m_w}$, which gives $20\ \mathrm{m}/\mathrm{s}$.
- id: c
  content: |-
    $20$
  correct: true
  feedback: |-
    The hanging block supplies tension and the wire segment supplies linear density, so $v_{\mathrm{wave}}=\sqrt{MgL/m_w}$. The values give $\sqrt{400}=20\ \mathrm{m}/\mathrm{s}$; because the field requests a number only, enter `20`.
- id: d
  content: |-
    $40$
  feedback: |-
    This does not equal the square root of the required tension-to-density ratio. The grouped radicand is $MgL/m_w=400\ \mathrm{m}^2/\mathrm{s}^2$, whose positive square root is $20\ \mathrm{m}/\mathrm{s}$, so the entry is `20`.
- id: e
  content: |-
    $400$
  feedback: |-
    This reports the radicand $MgL/m_w=400$, which represents speed squared. The wave speed is its positive square root, $20\ \mathrm{m}/\mathrm{s}$, so the number-only entry is `20`.
```

---

<a id="summary"></a>
## Summary

For a stationary block tensioning a wire over a pulley:

1. Use $F_T=Mg$ for the tension.
2. Use $\mu=m_w/L$ for the wire's linear mass density.
3. Substitute into
   $$
   v_{\mathrm{wave}}=\sqrt{\frac{F_T}{\mu}}
   =\sqrt{\frac{MgL}{m_w}}.
   $$
4. Keep the quotient beneath the square root.
5. Check that the units reduce to $\mathrm{m}/\mathrm{s}$.
6. Round only at the end and follow the requested answer format.

The main trap is swapping the hanging mass $M$, which sets tension, with the wire mass $m_w$, which sets linear density.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Maximum Transverse Particle Speed on a Tensioned Wire](Problem-3.md)

Study guide index: 11/28

---
<!-- lesson-nav:end -->
