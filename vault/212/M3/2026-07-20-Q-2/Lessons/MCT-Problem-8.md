# Find the Acceleration of a Falling Mass Driving a Massive Pulley

<!--
lesson-id: 212-M3-044
topic-code: MTH212.M3.44
-->

## Table of Contents

- [Introduction](#introduction)
- [Write One Equation for Each Motion](#write-one-equation-for-each-motion)
- [Reduce the Pulley to an Effective Inertia](#reduce-the-pulley-to-an-effective-inertia)
- [Carry the Constant Acceleration into Kinematics](#carry-the-constant-acceleration-into-kinematics)
- [Check the Same Endpoint with Energy](#check-the-same-endpoint-with-energy)
- [Separate Force Balance from Torque Balance at a Fixed Spindle](#separate-force-balance-from-torque-balance-at-a-fixed-spindle)
- [Summary](#summary)

## Prerequisites

- Draw separate free-body diagrams for a translating block and a rotating pulley.
- Use $\sum F=ma$ and $\sum\tau=I\alpha$ with a declared sign convention.
- Use the no-slip relations $a=\alpha R$ and $v=\omega R$.
- Apply constant-acceleration kinematics from rest.

---

<a id="introduction"></a>
## Introduction

A hanging block does not fall at $g$ when it must spin a massive pulley. The string tension supplies the pulley's torque and, on the block, reduces the net downward force. The reusable move is to connect three equations and eliminate the internal variables $T$ and $\alpha$:

$$
mg-T=ma,
\qquad
TR=I\alpha,
\qquad
a=\alpha R.
$$

Use $m$ for the hanging block's mass, $M$ for the pulley's mass when its shape is specified, $R$ for the pulley's radius, and $I$ for the pulley's moment of inertia about its fixed axle. Take the block's downward direction and the pulley's unwinding direction as positive.

This model fits a single block unwinding a light, inextensible string from a pulley whose center remains fixed. The string does not slip, the axle friction is negligible, and the pulley's rotational inertia is not negligible. A system with a block on each side needs two translational equations and is a different setup.

---

<a id="write-one-equation-for-each-motion"></a>
## Write One Equation for Each Motion

For the falling block, weight points in the positive direction and tension opposes the fall:

$$
mg-T=ma.
$$

For the pulley, take torques about the axle. The tangential string tension has moment arm $R$:

$$
TR=I\alpha.
$$

The string and rim share the same tangential acceleration when there is no slip:

$$
a=\alpha R.
$$

Keep the three statements in separate rows until their roles are clear:

| Part of the model | Governing statement | Equation |
| --- | --- | --- |
| Falling block | Downward weight minus upward tension gives the block's acceleration | $mg-T=ma$ |
| Fixed-axis pulley | Tension at radius $R$ gives the pulley's angular acceleration | $TR=I\alpha$ |
| String-rim contact | No slip ties the two accelerations together | $a=\alpha R$ |

**Source correction: forces are not the same as torques.** The M2-3 video says that tension is the only force acting on the disk. Gravity and the axle's support force also act on a fixed pulley. About the central axle, however, those forces have zero moment arm; tension is the only force in this model that produces torque about that axis.

The block equation also shows why $T\ne mg$. If $T=mg$, then $a=0$, so neither the block nor the pulley could begin accelerating. During the fall, $0<T<mg$.

```quiz
type: radio
id: mct-q2-p8-equation-set
shuffle: true
content: |-
  A block of mass $m$ falls while a light string unwinds without slipping from a massive pulley of radius $R$ and moment of inertia $I$. Downward motion and the unwinding rotation are positive. Which equation set models the system?
options:
- id: mct-q2-p8-equation-set-a
  content: |-
    $mg-T=ma$, $TR=I\alpha$, and $a=\alpha R$
  correct: true
  feedback: |-
    Weight drives the block downward while tension opposes it, tension supplies the pulley's torque, and no slip makes the block's linear acceleration equal to the rim's tangential acceleration. These give $mg-T=ma$, $TR=I\alpha$, and $a=\alpha R$.
- id: mct-q2-p8-equation-set-b
  content: |-
    $mg+T=ma$, $TR=I\alpha$, and $a=\alpha R$
  feedback: |-
    Tension points upward on the block, opposite the chosen positive direction. It must subtract from $mg$, so the block equation is $mg-T=ma$.
- id: mct-q2-p8-equation-set-c
  content: |-
    $mg-T=ma$, $mgR=I\alpha$, and $a=\alpha R$
  feedback: |-
    The block's weight acts on the block, not tangentially at the pulley's rim. Tension is the force exerted on the pulley by the string, so the pulley torque is $TR$.
- id: mct-q2-p8-equation-set-d
  content: |-
    $mg-T=ma$, $TR=I\alpha$, and $a=\alpha/R$
  feedback: |-
    Angular acceleration times radius has units of linear acceleration. The no-slip relation is $a=\alpha R$; dividing by $R$ is both dimensionally and physically incorrect.
- id: mct-q2-p8-equation-set-e
  content: |-
    $T=mg$, $TR=I\alpha$, and $a=\alpha R$
  feedback: |-
    Setting $T=mg$ is a translational equilibrium condition. This block accelerates, so its net force is nonzero and $T=mg-ma<mg$.
```

---

<a id="reduce-the-pulley-to-an-effective-inertia"></a>
## Reduce the Pulley to an Effective Inertia

Use $\alpha=a/R$ in the pulley equation:

$$
TR=I\frac{a}{R}
\qquad\Longrightarrow\qquad
T=\frac{I}{R^2}a.
$$

Substitute this tension into the block equation and factor the one remaining unknown:

$$
\begin{aligned}
mg-\frac{I}{R^2}a&=ma,\\
mg&=a\left(m+\frac{I}{R^2}\right).
\end{aligned}
$$

This is the useful factoring line: every term containing the target $a$ has been collected into one coefficient. Keep it symbolic until this point; early numerical substitution hides the $I/R^2$ reduction and makes unit errors harder to see.

Therefore,

$$
\boxed{a=\frac{mg}{m+I/R^2}},
\qquad
\boxed{\alpha=\frac{a}{R}=\frac{mgR}{I+mR^2}}.
$$

The quantity $I/R^2$ has units of mass and records how strongly the pulley's rotational inertia resists the string's linear acceleration. It is an **effective-inertia term**, not literal material added to the hanging block.

For $m>0$, $R>0$, and $I\ge 0$, the denominator $m+I/R^2$ is positive, so the chosen downward acceleration satisfies $a>0$.

For a uniform solid disk,

$$
I=\frac12MR^2
\qquad\Longrightarrow\qquad
\frac{I}{R^2}=\frac{M}{2},
$$

so

$$
\boxed{a=\frac{mg}{m+M/2}}.
$$

Two quick checks expose common setup errors. If $I\to0$, then $a\to g$, as for an ideal massless pulley. If $I>0$, the denominator exceeds $m$, so $a<g$.

```quiz
type: radio
id: mct-q2-p8-effective-inertia
shuffle: true
content: |-
  A $5.0\,\mathrm{kg}$ block unwinds a pulley with $I=0.80\,\mathrm{kg\,m^2}$ and $R=0.40\,\mathrm m$. Using $g=9.8\,\mathrm{m/s^2}$, what is the block's downward acceleration?
options:
- id: mct-q2-p8-effective-inertia-a
  content: |-
    $4.9\,\mathrm{m/s^2}$
  correct: true
  feedback: |-
    The pulley's effective-inertia term is $I/R^2=0.80/(0.40)^2=5.0\,\mathrm{kg}$. Thus $a=mg/(m+I/R^2)=49/(5.0+5.0)=4.9\,\mathrm{m/s^2}$ downward.
- id: mct-q2-p8-effective-inertia-b
  content: |-
    $9.8\,\mathrm{m/s^2}$
  feedback: |-
    This treats the pulley as rotationally massless. Because $I/R^2=5.0\,\mathrm{kg}>0$, some of the driving weight accelerates the pulley and the block's acceleration is less than $g$.
- id: mct-q2-p8-effective-inertia-c
  content: |-
    $8.45\,\mathrm{m/s^2}$
  feedback: |-
    This numerically adds $I$ directly to $m$, but $I$ has units of $\mathrm{kg\,m^2}$ and cannot be added to a mass. Divide by $R^2$ first; the denominator is $5.0+5.0=10.0\,\mathrm{kg}$.
- id: mct-q2-p8-effective-inertia-d
  content: |-
    $2.45\,\mathrm{m/s^2}$
  feedback: |-
    This counts the pulley's $I/R^2$ contribution twice. The reduction already converts the pulley equation to $T=(I/R^2)a$, so the denominator contains one term $I/R^2$.
```

---

<a id="carry-the-constant-acceleration-into-kinematics"></a>
## Carry the Constant Acceleration into Kinematics

**Source-video problem (M2-3, `dbvr-L5rxdg`, 00:00:01–00:09:44).** A $10\,\mathrm{kg}$ block hangs from a string wrapped around a $20\,\mathrm{kg}$ uniform solid-disk pulley of radius $2\,\mathrm m$. The block is released from rest.

Keep the two masses distinct:

$$
m=10\,\mathrm{kg},
\qquad
M=20\,\mathrm{kg}.
$$

The pulley's moment of inertia and effective-inertia term are

$$
I=\frac12MR^2
=\frac12(20)(2)^2
=40\,\mathrm{kg\,m^2},
\qquad
\frac{I}{R^2}=10\,\mathrm{kg}.
$$

The block and pulley accelerations are

$$
a=\frac{(10)(9.8)}{10+10}
=4.9\,\mathrm{m/s^2},
$$

$$
\alpha=\frac{a}{R}
=\frac{4.9}{2}
=2.45\,\mathrm{rad/s^2}.
$$

Back-substitution gives $T=m(g-a)=49\,\mathrm N$, not the block's $98\,\mathrm N$ weight. It also checks the rotational equation:

$$
TR=(49)(2)=98\,\mathrm{N\,m}
=I\alpha=(40)(2.45).
$$

Because the givens and ideal model are constant, $a$ is constant. After $t=8.0\,\mathrm s$,

$$
v=at=(4.9)(8.0)=39.2\,\mathrm{m/s}
$$

downward, and the fall distance is

$$
\Delta y=\frac12at^2
=\frac12(4.9)(8.0)^2
=156.8\,\mathrm m.
$$

These kinematics results assume the string remains taut and enough string and vertical clearance exist for the full interval.

```quiz
type: radio
id: mct-q2-p8-mirrored-chain
shuffle: true
content: |-
  A $6.0\,\mathrm{kg}$ block unwinds a $18\,\mathrm{kg}$ uniform solid-disk pulley of radius $0.60\,\mathrm m$. The block starts from rest. Using $g=9.8\,\mathrm{m/s^2}$, which line correctly gives $(a,\alpha,v)$ after $2.5\,\mathrm s$?
options:
- id: mct-q2-p8-mirrored-chain-a
  content: |-
    $(3.92\,\mathrm{m/s^2},\ 6.53\,\mathrm{rad/s^2},\ 9.80\,\mathrm{m/s})$
  correct: true
  feedback: |-
    For a solid disk, $I/R^2=M/2=9.0\,\mathrm{kg}$. Thus $a=(6.0)(9.8)/(6.0+9.0)=3.92\,\mathrm{m/s^2}$, $\alpha=a/R=6.53\,\mathrm{rad/s^2}$, and $v=at=9.80\,\mathrm{m/s}$.
- id: mct-q2-p8-mirrored-chain-b
  content: |-
    $(9.80\,\mathrm{m/s^2},\ 16.3\,\mathrm{rad/s^2},\ 24.5\,\mathrm{m/s})$
  feedback: |-
    This ignores the pulley's rotational inertia and lets the block free-fall. The positive term $M/2$ belongs in the effective denominator, reducing $a$ below $g$.
- id: mct-q2-p8-mirrored-chain-c
  content: |-
    $(2.45\,\mathrm{m/s^2},\ 4.08\,\mathrm{rad/s^2},\ 6.13\,\mathrm{m/s})$
  feedback: |-
    This uses the pulley's full mass $M$ in the denominator. A uniform solid disk contributes $I/R^2=M/2$, so the correct denominator is $m+M/2=15\,\mathrm{kg}$, not $m+M=24\,\mathrm{kg}$.
- id: mct-q2-p8-mirrored-chain-d
  content: |-
    $(3.92\,\mathrm{m/s^2},\ 2.35\,\mathrm{rad/s^2},\ 9.80\,\mathrm{m/s})$
  feedback: |-
    The linear acceleration and speed are consistent, but the no-slip conversion is reversed. Since $a=\alpha R$, angular acceleration is $\alpha=a/R$, not $aR$.
- id: mct-q2-p8-mirrored-chain-e
  content: |-
    $(0,\ 0,\ 0)$
  feedback: |-
    This would require $T=mg$, which is equilibrium. The falling block has $mg-T=ma>0$, so it and the pulley accelerate.
```

---

<a id="check-the-same-endpoint-with-energy"></a>
## Check the Same Endpoint with Energy

**Source-video extension (M2-5, `REIP2mf6sIQ`, 00:07:00–00:18:13).** The same $10\,\mathrm{kg}$ block and $20\,\mathrm{kg}$ solid-disk pulley are used, but the block begins $500\,\mathrm m$ above the ground. The video solves the endpoint both by energy and by the Newton/torque route above.

Energy is a compact endpoint check, not a second procedure for finding the system's forces or tension. With $v=\omega R$,

$$
\begin{aligned}
mgh
&=\frac12mv^2+\frac12I\omega^2\\
&=\frac12mv^2+\frac12\frac{I}{R^2}v^2\\
&=\frac12\left(m+\frac{I}{R^2}\right)v^2.
\end{aligned}
$$

Thus,

$$
v=\sqrt{\frac{2mgh}{m+I/R^2}}.
$$

For the source values, $m+I/R^2=20\,\mathrm{kg}$, so

$$
v=\sqrt{\frac{2(10)(9.8)(500)}{20}}
=\sqrt{4900}
=70\,\mathrm{m/s}.
$$

The dynamics result gives the same endpoint:

$$
v^2=2a h=2(4.9)(500)=4900.
$$

The M2-5 case uses the same effective denominator, so it is an endpoint check of the same move rather than a separate procedure.

```quiz
type: radio
id: mct-q2-p8-energy-check
shuffle: true
content: |-
  A $4.0\,\mathrm{kg}$ block starts from rest and falls $80\,\mathrm m$ while unwinding a uniform solid-disk pulley of mass $8.0\,\mathrm{kg}$. Neglect axle friction. Which energy ledger and endpoint speed are correct?
options:
- id: mct-q2-p8-energy-check-a
  content: |-
    $mgh=\frac12(m+M/2)v^2$, so $v=28\,\mathrm{m/s}$.
  correct: true
  feedback: |-
    A solid disk contributes $I/R^2=M/2=4.0\,\mathrm{kg}$ to the kinetic-energy coefficient. Therefore $v=\sqrt{2mgh/(m+M/2)}=\sqrt{784}=28\,\mathrm{m/s}$.
- id: mct-q2-p8-energy-check-b
  content: |-
    $mgh=\frac12mv^2$, so $v=39.6\,\mathrm{m/s}$.
  feedback: |-
    This assigns all lost potential energy to the block's translation. The pulley also has rotational kinetic energy, so the positive $M/2$ term must appear in the kinetic-energy coefficient and the speed is lower.
- id: mct-q2-p8-energy-check-c
  content: |-
    $mgh=(m+M/2)v^2$, so $v=19.8\,\mathrm{m/s}$.
  feedback: |-
    Both translational and rotational kinetic energies carry the factor $1/2$. Dropping that common factor halves $v^2$; the correct ledger is $mgh=\frac12(m+M/2)v^2$.
- id: mct-q2-p8-energy-check-d
  content: |-
    $mgh=\frac12(m+M)v^2$, so $v=22.9\,\mathrm{m/s}$.
  feedback: |-
    A solid disk does not contribute its full mass to the reduced coefficient. Since $I=\frac12MR^2$, its effective term is $I/R^2=M/2$.
```

---

<a id="separate-force-balance-from-torque-balance-at-a-fixed-spindle"></a>
## Separate Force Balance from Torque Balance at a Fixed Spindle

**M2-3 lecture transfer: fixed-spindle spool.** A cord is pulled tangentially with constant tension $F_T$ around a uniform solid-cylinder spool of mass $M_s$ and radius $R$. The spindle prevents the spool's center from translating.

The spindle can exert a nonzero support force to maintain translational equilibrium. Its torque about the spindle is still zero because it acts at the chosen pivot. Only the tangential tension enters the torque equation:

$$
F_T R=I\alpha
=\frac12M_sR^2\alpha.
$$

Therefore,

$$
\boxed{\alpha=\frac{2F_T}{M_sR}}.
$$

This is a neighboring fixed-axis case, not another hanging-block denominator. There is no translating block and no equation $mg-T=ma$ to couple to the rotation.

```quiz
type: radio
id: mct-q2-p8-fixed-spindle
shuffle: true
content: |-
  A horizontal, tangential $3.0\,\mathrm N$ tension pulls the rim of a fixed-spindle uniform solid-disk spool with mass $4.0\,\mathrm{kg}$ and radius $0.25\,\mathrm m$. Which statement is correct?
options:
- id: mct-q2-p8-fixed-spindle-a
  content: |-
    The spindle can supply a $3.0\,\mathrm N$ horizontal support-force component while exerting zero torque about itself, and $\alpha=6.0\,\mathrm{rad/s^2}$.
  correct: true
  feedback: |-
    The support force balances translation but acts at zero lever arm about the spindle. Tension supplies torque, so $\alpha=2F_T/(M_sR)=2(3.0)/(4.0\cdot0.25)=6.0\,\mathrm{rad/s^2}$.
- id: mct-q2-p8-fixed-spindle-b
  content: |-
    The spindle force must be zero because its torque is zero, and $\alpha=6.0\,\mathrm{rad/s^2}$.
  feedback: |-
    Zero torque does not imply zero force. The spindle force can be nonzero while its line of action passes through the pivot, giving it zero moment arm.
- id: mct-q2-p8-fixed-spindle-c
  content: |-
    The spindle balances the tension, so the net torque and angular acceleration are both zero.
  feedback: |-
    Force balance controls translation, while torque about the spindle controls rotation. The support force has zero lever arm, so it cannot cancel the tangential tension's torque.
- id: mct-q2-p8-fixed-spindle-d
  content: |-
    $\alpha=3.0\,\mathrm{rad/s^2}$ because $I=M_sR^2$.
  feedback: |-
    $I=M_sR^2$ is the central-axis inertia of a thin hoop. A uniform solid disk has $I=\frac12M_sR^2$, which doubles the angular acceleration relative to this choice.
- id: mct-q2-p8-fixed-spindle-e
  content: |-
    $\alpha=24\,\mathrm{rad/s^2}$ because $F_T=I\alpha$.
  feedback: |-
    Force is not torque. The rotational equation is $F_TR=I\alpha$; omitting the lever arm gives the wrong dimensions and the wrong acceleration.
```

---

<a id="summary"></a>
## Summary

For one falling block driving a fixed massive pulley:

1. Keep the block and pulley masses distinct.
2. Write $mg-T=ma$ for the block and $TR=I\alpha$ for the pulley.
3. Use no slip: $a=\alpha R$.
4. Replace tension by $T=(I/R^2)a$ and factor $a$.
5. Use
   $$
   a=\frac{mg}{m+I/R^2}.
   $$
6. For a solid disk, replace $I/R^2$ by $M/2$.
7. Use the resulting constant $a$ in kinematics. Use energy only as an endpoint check when tension is not requested.

The fastest error checks are $a<g$ for $I>0$, $T<mg$ during the fall, and $[I/R^2]=\mathrm{kg}$. A support force may be nonzero even when its torque about the axle is zero.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
