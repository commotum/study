# Use Torque Balance to Trade Force for Lever Arm

<!--
lesson-id: 212-M3-038
topic-code: MTH212.M3.38
-->

## Table of Contents

- [Introduction](#introduction)
- [Balance Opposing Torques](#balance-opposing-torques)
- [Separate Ideal and Actual Mechanical Advantage](#separate-ideal-and-actual-mechanical-advantage)
- [Change One Lever Arm](#change-one-lever-arm)
- [Account for the Distance Tradeoff](#account-for-the-distance-tradeoff)
- [Locate a Balance Support](#locate-a-balance-support)
- [Summary](#summary)

## Prerequisites

- Identify a pivot and the perpendicular moment arm of a force.
- Compute a torque magnitude with $\tau=Fd_\perp$.
- Use a clockwise/counterclockwise sign convention.
- Solve a one-step equation for an unknown force or distance.

---

<a id="introduction"></a>
## Introduction

A lever is at rest, and one force or lever arm is unknown. That is the cue to choose one pivot and set the opposing torque magnitudes equal:

$$
F_{\mathrm{in}}d_{\mathrm{in}}
=
F_{\mathrm{out}}d_{\mathrm{out}}.
$$

Both distances must be measured from the same pivot. More precisely, each $d$ is the perpendicular distance from that pivot to the corresponding force's line of action. When the forces are perpendicular to the lever, these are the familiar distances along the lever.

Use one procedure:

1. Mark the pivot and the two perpendicular arms.
2. Decide which force tends to rotate the lever clockwise and which tends to rotate it counterclockwise.
3. Write $\sum\tau=0$, or equate the two opposing torque magnitudes.
4. Solve the single unknown.
5. If requested, form the output-to-input force ratio and identify whether it is ideal or measured.

The equality compares torques on the lever. An upward force that the lever exerts on a load has an equal downward reaction force on the lever; that reaction belongs in the lever's torque ledger.

| Symbol | Role in the balance |
| --- | --- |
| $d_{\mathrm{in}}$ | Perpendicular distance from the pivot to the input force's line of action |
| $d_{\mathrm{out}}$ | Perpendicular distance from the same pivot to the output force's line of action |
| $F_{\mathrm{out}}$ | Useful force exerted by the lever on the load; its reaction on the lever has the opposite direction |

---

<a id="balance-opposing-torques"></a>
## Balance Opposing Torques

**Source-video Problem 1: Ideal seesaw.** A $300\,\mathrm N$ input force acts downward $6\,\mathrm m$ to the left of the fulcrum. The lever's output point is $3\,\mathrm m$ to the right.

**Explanation**

Take counterclockwise torque as positive. The downward input on the left gives

$$
\tau_{\mathrm{in}}=+(300\,\mathrm N)(6\,\mathrm m)
=+1800\,\mathrm{N\,m}.
$$

The desired output is an upward force on the load. The load therefore pushes downward on the right side of the lever with the same magnitude $F_{\mathrm{out}}$. That reaction produces the opposing clockwise torque:

$$
\tau_{\mathrm{load\ on\ lever}}
=-F_{\mathrm{out}}(3\,\mathrm m).
$$

Set the net torque to zero:

$$
\begin{aligned}
+1800\,\mathrm{N\,m}-F_{\mathrm{out}}(3\,\mathrm m)&=0,\\
F_{\mathrm{out}}&=600\,\mathrm N.
\end{aligned}
$$

Back-substitution gives $(600\,\mathrm N)(3\,\mathrm m)=1800\,\mathrm{N\,m}$, matching the input torque. The answer also passes a direction check: the output arm is half as long, so the output force must be twice as large.

**Source correction: torque signs.** The two contributions in the equilibrium ledger have opposite signs. The source video describes both sides as “positive torque,” but that cannot be the free-body torque balance for the lever. The upward output arrow is the force **by the lever on the load**; the force **by the load on the lever** points downward and supplies the opposing torque.

```quiz
type: radio
id: mct-q2-p2-balance-force
shuffle: true
content: |-
  A lever is in equilibrium. A $240\,\mathrm N$ input force acts downward $1.5\,\mathrm m$ to the left of the pivot. The lever lifts a load at an output arm of $0.30\,\mathrm m$ to the right. Which statement correctly describes the torque balance and ideal output-force magnitude?
options:
- id: mct-q2-p2-balance-force-a
  content: |-
    The torques on the lever oppose, and $F_{\mathrm{out}}=1200\,\mathrm N$.
  correct: true
  feedback: |-
    Static equilibrium requires opposite signed torques with equal magnitudes. Thus $(240\,\mathrm N)(1.5\,\mathrm m)=F_{\mathrm{out}}(0.30\,\mathrm m)$, which gives $F_{\mathrm{out}}=1200\,\mathrm N$.
- id: mct-q2-p2-balance-force-b
  content: |-
    The torques on the lever act in the same direction, and $F_{\mathrm{out}}=1200\,\mathrm N$.
  feedback: |-
    The numerical magnitude follows the equal-torque equation, but two same-sign torques would not give equilibrium. The load's downward reaction on the right side opposes the downward input applied on the left.
- id: mct-q2-p2-balance-force-c
  content: |-
    The torques oppose, and $F_{\mathrm{out}}=48\,\mathrm N$.
  feedback: |-
    This reverses the arm ratio. The shorter output arm requires the larger force: $F_{\mathrm{out}}=F_{\mathrm{in}}d_{\mathrm{in}}/d_{\mathrm{out}}$, not $F_{\mathrm{in}}d_{\mathrm{out}}/d_{\mathrm{in}}$.
- id: mct-q2-p2-balance-force-d
  content: |-
    The torques oppose, and $F_{\mathrm{out}}=360\,\mathrm N$.
  feedback: |-
    $(240)(1.5)=360$ is the input torque magnitude in $\mathrm{N\,m}$, not an output force. Divide that torque by the $0.30\,\mathrm m$ output arm to obtain $1200\,\mathrm N$.
- id: mct-q2-p2-balance-force-e
  content: |-
    No output force can balance the lever because both applied forces point downward on the lever.
  feedback: |-
    Force direction alone does not determine torque direction; the side of the pivot also matters. A downward force left of the pivot and a downward force right of it rotate the lever in opposite directions, so they can balance.
```

---

<a id="separate-ideal-and-actual-mechanical-advantage"></a>
## Separate Ideal and Actual Mechanical Advantage

For an ideal lever, the torque-balance equation can be rearranged into a force ratio:

$$
\frac{F_{\mathrm{out,ideal}}}{F_{\mathrm{in}}}
=
\frac{d_{\mathrm{in}}}{d_{\mathrm{out}}}.
$$

Keep the ratio orientation fixed: output goes over input for a force ratio, while the input arm goes over the output arm for the ideal geometry ratio.

| Quantity | Compute it from | What it describes |
| --- | --- | --- |
| $\displaystyle \mathrm{IMA}=\frac{d_{\mathrm{in}}}{d_{\mathrm{out}}}$ | Lever geometry | Ideal force multiplication |
| $\displaystyle \mathrm{AMA}=\frac{F_{\mathrm{out,actual}}}{F_{\mathrm{in}}}$ | Measured forces | Performance of the actual setup |

**Source correction: ideal versus actual.** For the source seesaw,

$$
\mathrm{IMA}=\frac{6\,\mathrm m}{3\,\mathrm m}=2,
\qquad
\frac{F_{\mathrm{out,ideal}}}{F_{\mathrm{in}}}
=\frac{600\,\mathrm N}{300\,\mathrm N}=2.
$$

Those ratios agree because $600\,\mathrm N$ comes from the ideal torque model. If the measured output were $580\,\mathrm N$, then

$$
\mathrm{AMA}=\frac{580}{300}\approx1.93,
$$

while the geometry would still give $\mathrm{IMA}=2$. Geometry alone gives IMA; call a force ratio AMA only when the input and output forces are measured for the actual setup.

```quiz
type: radio
id: mct-q2-p2-ideal-actual
shuffle: true
content: |-
  A lever has $d_{\mathrm{in}}=0.90\,\mathrm m$ and $d_{\mathrm{out}}=0.15\,\mathrm m$. With a $160\,\mathrm N$ input, its measured output force is $864\,\mathrm N$. What are its ideal and actual mechanical advantages?
options:
- id: mct-q2-p2-ideal-actual-a
  content: |-
    $\mathrm{IMA}=6$ and $\mathrm{AMA}=5.4$
  correct: true
  feedback: |-
    Ideal advantage comes from the arm ratio, $0.90/0.15=6$. Actual advantage comes from the measured force ratio, $864/160=5.4$.
- id: mct-q2-p2-ideal-actual-b
  content: |-
    $\mathrm{IMA}=5.4$ and $\mathrm{AMA}=6$
  feedback: |-
    This swaps the definitions. Geometry sets IMA, while the measured output-to-input force ratio sets AMA; therefore the values are $6$ and $5.4$, respectively.
- id: mct-q2-p2-ideal-actual-c
  content: |-
    $\mathrm{IMA}=6$ and $\mathrm{AMA}=6$
  feedback: |-
    The ideal output would be $(6)(160\,\mathrm N)=960\,\mathrm N$, but the measured output is only $864\,\mathrm N$. The actual ratio is therefore $5.4$, not $6$.
- id: mct-q2-p2-ideal-actual-d
  content: |-
    $\mathrm{IMA}=1/6$ and $\mathrm{AMA}=5.4$
  feedback: |-
    This reverses the ideal arm ratio. For force multiplication, divide the longer input arm by the shorter output arm: $d_{\mathrm{in}}/d_{\mathrm{out}}=6$.
- id: mct-q2-p2-ideal-actual-e
  content: |-
    $\mathrm{IMA}=6$ and $\mathrm{AMA}=0.185$
  feedback: |-
    $160/864\approx0.185$ is the input-to-output force ratio. Actual mechanical advantage is defined in the opposite order, $F_{\mathrm{out,actual}}/F_{\mathrm{in}}=5.4$.
```

---

<a id="change-one-lever-arm"></a>
## Change One Lever Arm

**Source-video Problem 2: Shovel.** The input force is $200\,\mathrm N$, the input arm is $1.0\,\mathrm m$, and the output arm at the blade is $0.10\,\mathrm m$. The forces in the source diagram are perpendicular to their arms, so

$$
\begin{aligned}
(200\,\mathrm N)(1.0\,\mathrm m)
&=F_{\mathrm{out}}(0.10\,\mathrm m),\\
F_{\mathrm{out}}&=2000\,\mathrm N,\\
\mathrm{IMA}&=\frac{1.0}{0.10}=10.
\end{aligned}
$$

**Source-video controlled variation: Move the input hand to the midpoint.** The effective input arm becomes $0.50\,\mathrm m$ while the input force and output arm stay fixed:

$$
F_{\mathrm{out}}
=\frac{(200\,\mathrm N)(0.50\,\mathrm m)}{0.10\,\mathrm m}
=1000\,\mathrm N,
\qquad
\mathrm{IMA}=5.
$$

**Source correction: midpoint wording.** Halving the input arm halves the ideal output force and the ideal mechanical advantage. The source phrase “reduced by two” means **reduced by a factor of two**, from $10$ to $5$.

| Input arm | Input torque | Ideal output force | IMA |
| ---: | ---: | ---: | ---: |
| $1.0\,\mathrm m$ | $200\,\mathrm{N\,m}$ | $2000\,\mathrm N$ | $10$ |
| $0.50\,\mathrm m$ | $100\,\mathrm{N\,m}$ | $1000\,\mathrm N$ | $5$ |

Only the input arm changes. After the hand moves, use the second row; reusing $1.0\,\mathrm m$ would also reuse the original $200\,\mathrm{N\,m}$ input torque.

```quiz
type: radio
id: mct-q2-p2-arm-change
shuffle: true
content: |-
  A lever has $F_{\mathrm{in}}=180\,\mathrm N$ and $d_{\mathrm{out}}=0.12\,\mathrm m$. The input point is moved from $0.84\,\mathrm m$ to $0.42\,\mathrm m$ from the pivot. What are the new ideal output force and IMA?
options:
- id: mct-q2-p2-arm-change-a
  content: |-
    $F_{\mathrm{out}}=630\,\mathrm N$ and $\mathrm{IMA}=3.5$
  correct: true
  feedback: |-
    With the new arm, $F_{\mathrm{out}}=(180)(0.42)/(0.12)=630\,\mathrm N$. The same geometry gives $\mathrm{IMA}=0.42/0.12=3.5$.
- id: mct-q2-p2-arm-change-b
  content: |-
    $F_{\mathrm{out}}=1260\,\mathrm N$ and $\mathrm{IMA}=7$
  feedback: |-
    These are the values for the original $0.84\,\mathrm m$ input arm. The question asks for the result after that arm is halved to $0.42\,\mathrm m$.
- id: mct-q2-p2-arm-change-c
  content: |-
    $F_{\mathrm{out}}=90\,\mathrm N$ and $\mathrm{IMA}=0.5$
  feedback: |-
    Halving the arm halves the input torque, not the applied $180\,\mathrm N$ force. Use the new arm in $F_{\mathrm{in}}d_{\mathrm{in}}=F_{\mathrm{out}}d_{\mathrm{out}}$.
- id: mct-q2-p2-arm-change-d
  content: |-
    $F_{\mathrm{out}}=630\,\mathrm N$ and $\mathrm{IMA}=7$
  feedback: |-
    The output force uses the new arm correctly, but IMA must use that same geometry. Since $0.42/0.12=3.5$, the force and arm ratios cannot give different ideal advantages.
- id: mct-q2-p2-arm-change-e
  content: |-
    $F_{\mathrm{out}}=51.4\,\mathrm N$ and $\mathrm{IMA}=0.286$
  feedback: |-
    This reverses both ratios. A longer input arm than output arm multiplies force, so both $F_{\mathrm{out}}/F_{\mathrm{in}}$ and $d_{\mathrm{in}}/d_{\mathrm{out}}$ must exceed $1$ in the ideal model.
```

---

<a id="account-for-the-distance-tradeoff"></a>
## Account for the Distance Tradeoff

A larger ideal output force does not mean that the lever creates energy. If a rigid lever turns through a small angle $\Delta\phi$, a point at distance $d$ from the pivot travels an arc length $s=d\Delta\phi$. Therefore,

$$
\frac{s_{\mathrm{in}}}{s_{\mathrm{out}}}
=
\frac{d_{\mathrm{in}}}{d_{\mathrm{out}}}
=
\frac{F_{\mathrm{out,ideal}}}{F_{\mathrm{in}}}.
$$

For the source shovel, the ideal mechanical advantage is $10$. The input point must travel ten times as far as the blade's output point for the same rotation. In the ideal model,

$$
F_{\mathrm{in}}s_{\mathrm{in}}
=
F_{\mathrm{out}}s_{\mathrm{out}}.
$$

The lever exchanges a smaller force over a longer distance for a larger force over a shorter distance.

```quiz
type: radio
id: mct-q2-p2-distance-tradeoff
shuffle: true
content: |-
  An ideal lever has $d_{\mathrm{in}}=0.75\,\mathrm m$ and $d_{\mathrm{out}}=0.15\,\mathrm m$. During one motion, the output point rises $4.0\,\mathrm{cm}$. Which pair is consistent with the same lever rotation?
options:
- id: mct-q2-p2-distance-tradeoff-a
  content: |-
    The input point moves $20\,\mathrm{cm}$, and $F_{\mathrm{out}}=5F_{\mathrm{in}}$.
  correct: true
  feedback: |-
    Both ratios equal the arm ratio: $0.75/0.15=5$. The input point travels $5(4.0\,\mathrm{cm})=20\,\mathrm{cm}$ while the ideal output force is five times the input force.
- id: mct-q2-p2-distance-tradeoff-b
  content: |-
    The input point moves $4.0\,\mathrm{cm}$, and $F_{\mathrm{out}}=5F_{\mathrm{in}}$.
  feedback: |-
    Points at different distances from the pivot do not travel equal arc lengths through the same angle. The longer input arm travels five times the output distance, or $20\,\mathrm{cm}$.
- id: mct-q2-p2-distance-tradeoff-c
  content: |-
    The input point moves $20\,\mathrm{cm}$, and $F_{\mathrm{out}}=F_{\mathrm{in}}/5$.
  feedback: |-
    The distance ratio is correct, but the force ratio is reversed. A longer input arm produces a larger ideal output force at the shorter arm: $F_{\mathrm{out}}=5F_{\mathrm{in}}$.
- id: mct-q2-p2-distance-tradeoff-d
  content: |-
    The input point moves $0.8\,\mathrm{cm}$, and $F_{\mathrm{out}}=5F_{\mathrm{in}}$.
  feedback: |-
    This divides the output motion by the arm ratio. The input point is farther from the pivot, so it travels farther, not less far, through the same rotation.
- id: mct-q2-p2-distance-tradeoff-e
  content: |-
    The input point moves $20\,\mathrm{cm}$, and $F_{\mathrm{out}}=25F_{\mathrm{in}}$.
  feedback: |-
    The arm ratio enters once, not once for force and again for distance. The factor of $5$ in force is paired with a factor of $5$ in opposite-direction distance tradeoff, preserving ideal work.
```

---

<a id="locate-a-balance-support"></a>
## Locate a Balance Support

**M2-1 lecture transfer: Support at the center of mass.** Two masses lie $0.88\,\mathrm m$ apart, with $m_1=3m_2$. Let the support be a distance $x$ from the heavier mass $m_1$. The lever arms about the support are $x$ and $0.88\,\mathrm m-x$.

![](<../../../M2/2026-07-07-M2-1/Source/Images/two-mass-balance.png>)

Both weights point downward, but they act on opposite sides of the support, so their torques oppose. Balance gives

$$
\begin{aligned}
m_1gx&=m_2g(0.88\,\mathrm m-x),\\
3m_2x&=m_2(0.88\,\mathrm m-x),\\
4x&=0.88\,\mathrm m,\\
x&=0.22\,\mathrm m.
\end{aligned}
$$

After canceling the common $g$, this is the lecture-note condition

$$
m_1r_1=m_2r_2.
$$

The support lies closer to the larger mass. Supporting the system at this balance point—its center of mass—makes the net gravitational torque zero.

```quiz
type: radio
id: mct-q2-p2-balance-support
shuffle: true
content: |-
  Two point masses are $1.25\,\mathrm m$ apart, with $m_1=4m_2$. Where should a massless support be placed, measured from the heavier mass $m_1$, so the system balances?
options:
- id: mct-q2-p2-balance-support-a
  content: |-
    $0.25\,\mathrm m$
  correct: true
  feedback: |-
    If $x$ is measured from $m_1$, balance requires $4m_2x=m_2(1.25-x)$. Thus $5x=1.25\,\mathrm m$ and $x=0.25\,\mathrm m$, closer to the heavier mass.
- id: mct-q2-p2-balance-support-b
  content: |-
    $1.00\,\mathrm m$
  feedback: |-
    This is the distance from the lighter mass to the balance point, not the requested distance from the heavier mass. The two distances sum to $1.25\,\mathrm m$.
- id: mct-q2-p2-balance-support-c
  content: |-
    $0.3125\,\mathrm m$
  feedback: |-
    Dividing the full separation by the mass ratio alone omits the lighter mass's nonzero lever arm. The arms are $x$ and $1.25-x$, so the equation is $4x=1.25-x$.
- id: mct-q2-p2-balance-support-d
  content: |-
    $0.625\,\mathrm m$
  feedback: |-
    The midpoint balances equal masses. Here $m_1$ is four times heavier, so the support must lie closer to $m_1$ than the midpoint does.
- id: mct-q2-p2-balance-support-e
  content: |-
    $0.20\,\mathrm m$
  feedback: |-
    The support divides the separation into a $1:4$ arm ratio, but $0.20\,\mathrm m$ would make the total separation $1.00\,\mathrm m$. For a $1.25\,\mathrm m$ separation, the shorter arm is $1.25/5=0.25\,\mathrm m$.
```

---

<a id="summary"></a>
## Summary

For a balanced lever:

1. Measure both perpendicular arms from the same pivot.
2. Put clockwise and counterclockwise torques on opposite sides of the ledger:
   $$
   F_{\mathrm{in}}d_{\mathrm{in}}
   =F_{\mathrm{out}}d_{\mathrm{out}}.
   $$
3. Solve the one unknown force or arm.
4. Use $d_{\mathrm{in}}/d_{\mathrm{out}}$ for ideal mechanical advantage and a measured $F_{\mathrm{out}}/F_{\mathrm{in}}$ for actual mechanical advantage.
5. Remember that force multiplication is paired with extra input travel, not extra energy.

For weights on opposite sides of a support, the same move becomes $m_1r_1=m_2r_2$. A larger force or mass needs a shorter arm to balance a smaller one.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
