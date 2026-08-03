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
v=\sqrt{\frac{T}{\mu}},
$$

where $T$ is the wire tension and $\mu$ is its linear mass density. In a wall–pulley–block setup, a stationary hanging block of mass $M$ supplies the tension, while the horizontal wire segment's mass $m_w$ and length $L$ determine its linear density:

$$
T=Mg,
\qquad
\mu=\frac{m_w}{L}.
$$

The task is to assign each given quantity to the correct physical role and then evaluate the wave-speed formula.

| Symbol | Physical role |
| --- | --- |
| $M$ | hanging block mass; determines $T=Mg$ |
| $m_w$ | mass of the horizontal vibrating wire segment |
| $L$ | length of that same wire segment |
| $\mu$ | wire mass per unit length, $m_w/L$ |
| $v$ | propagation speed of the transverse wave |

---

<a id="build-tension-and-linear-density"></a>
## Build Tension and Linear Density

Because the hanging block is stationary, its vertical forces balance:

$$
T-Mg=0
\quad\Longrightarrow\quad
T=Mg.
$$

The mass density of the vibrating wire segment is its own mass divided by its length:

$$
\mu=\frac{m_w}{L}.
$$

**Example:** A stationary $0.50\ \mathrm{kg}$ block tensions a wire segment with mass $0.025\ \mathrm{kg}$ and length $2.0\ \mathrm{m}$. Use $g=10\ \mathrm{m/s^2}$. Find $T$ and $\mu$.

**Explanation**

$$
T=Mg=(0.50)(10)=5.0\ \mathrm{N},
$$

and

$$
\mu=\frac{m_w}{L}
=\frac{0.025\ \mathrm{kg}}{2.0\ \mathrm{m}}
=0.0125\ \mathrm{kg/m}.
$$

```quiz
type: radio
id: problem-2-wire-speed-q1
content: |-
  A stationary block of mass $M=0.60\ \mathrm{kg}$ tensions a wire segment with $m_w=0.030\ \mathrm{kg}$ and $L=1.5\ \mathrm{m}$. Use $g=10\ \mathrm{m/s^2}$. Which pair gives the tension and linear mass density?
options:
- id: a
  content: |-
    $T=6.0\ \mathrm{N}$ and $\mu=0.020\ \mathrm{kg/m}$
  correct: true
  feedback: |-
    $T=Mg=(0.60)(10)=6.0\ \mathrm{N}$ and $\mu=m_w/L=0.030/1.5=0.020\ \mathrm{kg/m}$.
- id: b
  content: |-
    $T=0.30\ \mathrm{N}$ and $\mu=0.40\ \mathrm{kg/m}$
  feedback: |-
    This swaps the two masses: $0.030(10)$ uses the wire mass for tension, while $0.60/1.5$ uses the hanging mass for linear density.
- id: c
  content: |-
    $T=6.0\ \mathrm{N}$ and $\mu=0.045\ \mathrm{kg/m}$
  feedback: |-
    The tension is correct, but $0.045$ comes from multiplying $m_wL$; linear density is mass divided by length.
- id: d
  content: |-
    $T=0.60\ \mathrm{N}$ and $\mu=0.020\ \mathrm{kg/m}$
  feedback: |-
    The density is correct, but the tension cannot equal the mass numerically; it is $T=Mg=(0.60)(10)=6.0\ \mathrm N$.
- id: e
  content: |-
    $T=15\ \mathrm{N}$ and $\mu=0.050\ \mathrm{kg/m}$
  feedback: |-
    This assigns length to the tension calculation and hanging mass to the density calculation. Use only $M$ in $Mg$ and only $m_w/L$ for $\mu$.
```

---

<a id="combine-the-ingredients-into-wave-speed"></a>
## Combine the Ingredients Into Wave Speed

Substitute $T=Mg$ and $\mu=m_w/L$ into $v=\sqrt{T/\mu}$:

$$
v
=\sqrt{\frac{Mg}{m_w/L}}
=\sqrt{\frac{MgL}{m_w}}.
$$

This direct formula uses the hanging mass, wire mass, wire length, and gravitational acceleration.

The units confirm that the expression produces speed:

$$
\left[\frac{MgL}{m_w}\right]
=\frac{(\mathrm{kg})(\mathrm{m/s^2})(\mathrm{m})}
{\mathrm{kg}}
=\mathrm{m^2/s^2}.
$$

Taking the square root gives $\mathrm{m/s}$.

**Example:** Use $M=0.50\ \mathrm{kg}$, $m_w=0.025\ \mathrm{kg}$, $L=2.0\ \mathrm{m}$, and $g=10\ \mathrm{m/s^2}$.

**Explanation**

Keep the whole quotient beneath the radical:

$$
v
=\sqrt{\frac{(0.50)(10)(2.0)}{0.025}}
=\sqrt{400}
=20\ \mathrm{m/s}.
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
  A stationary block with $M=0.60\ \mathrm{kg}$ tensions a wire segment with $m_w=0.040\ \mathrm{kg}$ and $L=1.5\ \mathrm{m}$. Use $g=10\ \mathrm{m/s^2}$. What is the transverse wave speed?
options:
- id: a
  content: |-
    $3.9\ \mathrm{m/s}$
  feedback: |-
    The correctly grouped radicand is $MgL/m_w=225$; a value near $3.9$ indicates that the division or radical was applied to only part of that quotient.
- id: b
  content: |-
    $9.0\ \mathrm{m/s}$
  feedback: |-
    This is the numerator $MgL$, not the wave speed.
- id: c
  content: |-
    $15\ \mathrm{m/s}$
  correct: true
  feedback: |-
    $v=\sqrt{(0.60)(10)(1.5)/0.040}=\sqrt{225}=15\ \mathrm{m/s}$.
- id: d
  content: |-
    $150\ \mathrm{m/s}$
  feedback: |-
    This is $Mg/m_w=150$, which omits the wire length and the square root required by $v=\sqrt{MgL/m_w}$.
- id: e
  content: |-
    $225\ \mathrm{m/s}$
  feedback: |-
    This is the value inside the radical; the wave speed is its square root.
```

---

<a id="keep-the-two-masses-in-their-own-roles"></a>
## Keep the Two Masses in Their Own Roles

The two masses are not interchangeable:

- $M$ is the hanging block mass, so it sets the tension $T=Mg$.
- $m_w$ is the mass of the vibrating wire segment, so it sets $\mu=m_w/L$.

Thus,

$$
v=\sqrt{\frac{MgL}{m_w}}.
$$

A larger hanging mass raises the speed by raising the tension. A larger wire mass lowers the speed by raising the linear density.

The square root controls the size of these changes:

$$
M\text{ multiplied by }k
\Longrightarrow v\text{ multiplied by }\sqrt{k},
$$

while

$$
m_w\text{ multiplied by }k
\Longrightarrow v\text{ divided by }\sqrt{k}.
$$

**Example:** For $M=0.90\ \mathrm{kg}$, $m_w=0.030\ \mathrm{kg}$, $L=1.2\ \mathrm{m}$, and $g=10\ \mathrm{m/s^2}$, choose the correct setup.

**Explanation**

Place $M$ in the numerator through $Mg$ and place $m_w$ in the denominator:

$$
v=\sqrt{\frac{(0.90)(10)(1.2)}{0.030}}.
$$

```quiz
type: radio
id: problem-2-wire-speed-q3
content: |-
  For $M=0.80\ \mathrm{kg}$, $m_w=0.020\ \mathrm{kg}$, $L=1.5\ \mathrm{m}$, and $g=10\ \mathrm{m/s^2}$, which expression correctly gives the transverse wave speed?
options:
- id: a
  content: |-
    $\displaystyle \sqrt{\frac{(0.80)(10)(1.5)}{0.020}}$
  correct: true
  feedback: |-
    The hanging mass belongs in $T=Mg$, while the wire mass belongs in $\mu=m_w/L$, giving $v=\sqrt{MgL/m_w}$.
- id: b
  content: |-
    $\displaystyle \sqrt{\frac{(0.020)(10)(1.5)}{0.80}}$
  feedback: |-
    This swaps the block mass and wire mass.
- id: c
  content: |-
    $\displaystyle \frac{(0.80)(10)(1.5)}{0.020}$
  feedback: |-
    This omits the square root from $v=\sqrt{T/\mu}$.
- id: d
  content: |-
    $\displaystyle \sqrt{\frac{(0.80)(0.020)}{(10)(1.5)}}$
  feedback: |-
    The wire mass belongs alone in the denominator after substituting $\mu=m_w/L$.
- id: e
  content: |-
    $\displaystyle \sqrt{\frac{(0.80)(10)}{(0.020)(1.5)}}$
  feedback: |-
    Since $\mu=m_w/L$, dividing by $\mu$ moves $L$ into the numerator, not the denominator.
```

---

<a id="match-the-diagram-and-answer-form"></a>
## Match the Diagram and Answer Form

Read the diagram as a physical map: $L$ labels the horizontal vibrating wire segment, $m_w$ is that segment's mass, and the hanging block $M$ supplies the tension.

**Example:** A block of mass $M$ hangs from a wire over a pulley. The wire segment between the wall and pulley has length $L$ and mass $m_w$. Find the speed at which a transverse wave propagates along the wire. Assume the hanging block is stationary, so the wire tension is $T=Mg$.

Use $M=0.82\ \mathrm{kg}$, $m_w=0.018\ \mathrm{kg}$, $L=1.4\ \mathrm{m}$, and $g=9.8\ \mathrm{m/s^2}$.

![](<../Source/Images/wire-pulley-hanging-mass.png>)

Enter the wave speed in meters per second as a number only.

**Explanation**

The wire's linear mass density is $\mu=m_w/L$, and the stationary block makes $T=Mg$. Therefore,

$$
\begin{aligned}
v
&=\sqrt{\frac{T}{\mu}}\\
&=\sqrt{\frac{MgL}{m_w}}\\
&=\sqrt{\frac{(0.82)(9.8)(1.4)}{0.018}}\\
&=24.999\ldots\ \mathrm{m/s}.
\end{aligned}
$$

The measured givens have two significant figures, so $v=25\ \mathrm{m/s}$. Enter $25$.

```quiz
type: radio
id: problem-2-wire-speed-q4
content: |-
  A stationary hanging block has $M=0.50\ \mathrm{kg}$. The horizontal wire segment has $m_w=0.020\ \mathrm{kg}$ and $L=1.6\ \mathrm{m}$. Use $g=10\ \mathrm{m/s^2}$. The answer field accepts the wave speed in meters per second as a number only. Which number should be entered?
options:
- id: a
  content: |-
    $5$
  feedback: |-
    This is the tension value $T=Mg=5\ \mathrm N$, not the propagation speed obtained after dividing by $\mu$ and taking a square root.
- id: b
  content: |-
    $16$
  feedback: |-
    This is the product $gL=16$ and ignores both mass roles and the square root in $v=\sqrt{MgL/m_w}$.
- id: c
  content: |-
    $20$
  correct: true
  feedback: |-
    $v=\sqrt{(0.50)(10)(1.6)/0.020}=\sqrt{400}=20\ \mathrm{m/s}$, so enter $20$.
- id: d
  content: |-
    $40$
  feedback: |-
    The grouped radicand is $400$, but its positive square root is $20$, not $40$.
- id: e
  content: |-
    $400$
  feedback: |-
    This is $MgL/m_w$, the value inside the radical; the requested speed is $\sqrt{400}=20\ \mathrm{m/s}$.
```

---

<a id="summary"></a>
## Summary

For a stationary block tensioning a wire over a pulley:

1. Use $T=Mg$ for the tension.
2. Use $\mu=m_w/L$ for the wire's linear mass density.
3. Substitute into
   $$
   v=\sqrt{\frac{T}{\mu}}
   =\sqrt{\frac{MgL}{m_w}}.
   $$
4. Keep the quotient beneath the square root.
5. Check that the units reduce to $\mathrm{m/s}$.
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
