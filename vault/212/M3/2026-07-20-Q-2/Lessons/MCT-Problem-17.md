# Conserve Angular Momentum When the System's Inertia Changes

<!--
lesson-id: 212-M3-053
topic-code: MTH212.M3.53
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Initial Angular Momentum](#build-initial-angular-momentum)
- [Source-Video Worked Problem: Box Added to a Platform](#source-video-box-platform)
- [Source-Video Worked Problem: Child Lands on a Merry-Go-Round](#source-video-child-merry-go-round)
- [Source-Video Control: Skater Pulls Inward](#source-video-skater)
- [Lecture-Note Supplement: Rain Sticks in Rotating Cups](#lecture-note-rain-cups)
- [Lecture-Note Contrast: A Tangential Bullet Arrives with Angular Momentum](#lecture-note-tangential-bullet)
- [Summary](#summary)

## Prerequisites

- Calculate a rigid body's moment of inertia about a stated axis.
- Use $I=mr^2$ for a point mass a perpendicular distance $r$ from an axis.
- Use $I=\frac12MR^2$ for a uniform solid disk about its symmetry axis.
- Use $L_z=I\omega$ for a rigid body rotating about a fixed $z$-axis.
- Use the axial component of $\vec L=\vec r\times m\vec v$ for an incoming particle.
- Distinguish angular momentum from rotational kinetic energy.

---

<a id="introduction"></a>
## Introduction

When a rotating system's mass distribution changes, do not begin with $I_i\omega_i=I_f\omega_f$. First choose the system and axis, then decide whether external angular impulse about that axis is negligible during the interaction:

$$
\Delta L_z=\int \tau_{\mathrm{ext},z}\,dt.
$$

Only when the right side is negligible may you write

$$
L_{i,z}=L_{f,z}.
$$

Use this sequence:

1. Choose the system and rotation axis.
2. Check the net external torque about that axis during the interaction.
3. Add every initial angular-momentum contribution, including an incoming object when necessary.
4. Calculate the total final moment of inertia.
5. Set $L_{i,z}=I_f\omega_f$ and solve.
6. Check the direction, units, and expected change in angular speed.

The shortcut

$$
I_i\omega_i=I_f\omega_f
$$

applies when both initial and final angular momentum can be represented by one co-rotating rigid system. An incoming object that is not initially co-rotating needs its own initial term.

For that same-system case, the product $I\omega$ is the invariant, so

$$
\frac{\omega_f}{\omega_i}=\frac{I_i}{I_f}.
$$

This ratio is useful only after the conservation condition and system boundary have been established. Its units also check:

$$
[I\omega]=(\mathrm{kg\,m^2})(\mathrm{s^{-1}})
=\mathrm{kg\,m^2/s},
$$

the units of angular momentum.

---

<a id="build-initial-angular-momentum"></a>
## Build the Initial Angular Momentum

Take the vertical spindle as the $z$-axis. If a platform is initially rotating and an object approaches before sticking, then

$$
L_{i,z}=I_{\mathrm{platform}}\omega_i+L_{\mathrm{object},z}.
$$

For an incoming particle,

$$
L_{\mathrm{object},z}=(\vec r\times m\vec v)_z.
$$

Only the velocity component tangent to a circle about the axis contributes:

$$
\boxed{L_{\mathrm{object},z}=mr v_t}.
$$

- A vertical drop onto a horizontal platform has $v_t=0$, so its incoming $L_z$ is zero.
- A radial approach in the platform's plane also has $v_t=0$.
- A tangential approach has $|L_z|=mrv$; its sign depends on whether it agrees with the platform's rotation.

After the object sticks at radius $r$,

$$
I_f=I_{\mathrm{platform}}+mr^2
$$

for a point-mass model, and

$$
\boxed{
\omega_f=
\frac{I_{\mathrm{platform}}\omega_i+mr v_t}
{I_{\mathrm{platform}}+mr^2}
}.
$$

**Source correction.** The videos describe a straight-down landing as producing “no torque.” The precise statement is that the incoming object has zero initial angular momentum component about the vertical axis, while the external angular impulse about that axis is negligible for the chosen platform-plus-object system. Forces from the spindle can be large, but a force through the spindle has zero torque about that axis.

```quiz
type: radio
id: mct-p17-initial-angular-momentum
shuffle: true
content: |-
  A platform with moment of inertia $I_p$ rotates counterclockwise at $\omega_i$. A small mass $m$ approaches tangentially at speed $v$ and sticks at radius $r$, moving initially in the same rotational sense. External torque about the spindle is negligible. Which expression gives $\omega_f$?
options:
- id: mct-p17-initial-angular-momentum-a
  content: |-
    $\displaystyle \omega_f=\frac{I_p\omega_i+mrv}{I_p+mr^2}$
  correct: true
  feedback: |-
    The rotating platform contributes $I_p\omega_i$, and the tangential mass contributes same-sign angular momentum $mrv$. After sticking, both rotate with inertia $I_p+mr^2$, giving the stated quotient.
- id: mct-p17-initial-angular-momentum-b
  content: |-
    $\displaystyle \omega_f=\frac{I_p\omega_i}{I_p+mr^2}$
  feedback: |-
    This would apply if the incoming mass had zero axial angular momentum, as in a vertical or radial arrival. A same-direction tangential approach contributes the additional term $+mrv$.
- id: mct-p17-initial-angular-momentum-c
  content: |-
    $\displaystyle \omega_f=\frac{I_p\omega_i-mrv}{I_p+mr^2}$
  feedback: |-
    The minus sign belongs to a tangential approach opposite the platform's rotation. Here both angular momenta point in the same axial direction, so they add.
- id: mct-p17-initial-angular-momentum-d
  content: |-
    $\displaystyle \omega_f=\frac{I_p\omega_i+mrv}{I_p}$
  feedback: |-
    This includes the mass's incoming angular momentum but omits its final inertia. Once it sticks at radius $r$, it adds $mr^2$ to the rotating system.
- id: mct-p17-initial-angular-momentum-e
  content: |-
    $\displaystyle \omega_f=\sqrt{\frac{I_p\omega_i^2+mv^2}{I_p+mr^2}}$
  feedback: |-
    This equates kinetic energies across a sticking collision. Sticking is inelastic, so use axial angular momentum—not mechanical energy—as the conserved quantity under the stated torque condition.
```

---

<a id="source-video-box-platform"></a>
## Source-Video Worked Problem: Box Added to a Platform

The source segment `WzjIMuf-yuo` at 3:06-6:19 gives a platform with

$$
I_i=500\,\mathrm{kg\,m^2},
\qquad
\omega_i=2\,\mathrm{rad/s}.
$$

A box is dropped straight down and adds

$$
I_{\mathrm{box}}=100\,\mathrm{kg\,m^2}
$$

after it lands. The chosen axis is the platform's vertical spindle. The box has zero incoming $L_z$, and external torque about this axis is negligible during the landing. Therefore,

$$
L_{i,z}=(500)(2)=1000\,\mathrm{kg\,m^2/s}.
$$

The final inertia is

$$
I_f=500+100=600\,\mathrm{kg\,m^2}.
$$

Conserve axial angular momentum:

$$
\begin{aligned}
(500)(2)&=(600)\omega_f,\\
\omega_f&=\frac{1000}{600},\\
\omega_f&=\boxed{1.67\,\mathrm{rad/s}}.
\end{aligned}
$$

The inertia increased by a factor $600/500=1.2$, so the angular speed decreased by the reciprocal factor $500/600$. Both sides of the conservation equation equal $1000\,\mathrm{kg\,m^2/s}$.

```quiz
type: radio
id: mct-p17-platform-mirror
shuffle: true
content: |-
  A platform has $I_i=300\,\mathrm{kg\,m^2}$ and $\omega_i=4.0\,\mathrm{rad/s}$. An object dropped vertically onto it sticks and adds $100\,\mathrm{kg\,m^2}$ of inertia. External torque about the spindle is negligible. What is the final angular speed?
options:
- id: mct-p17-platform-mirror-a
  content: |-
    $3.0\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    The vertical arrival contributes zero initial $L_z$, so $(300)(4.0)=(300+100)\omega_f$. Thus $\omega_f=1200/400=3.0\,\mathrm{rad/s}$.
- id: mct-p17-platform-mirror-b
  content: |-
    $4.0\,\mathrm{rad/s}$
  feedback: |-
    This keeps angular speed constant even though the final inertia is larger. With fixed axial angular momentum, $I\omega$ stays constant, so $\omega$ must decrease.
- id: mct-p17-platform-mirror-c
  content: |-
    $5.33\,\mathrm{rad/s}$
  feedback: |-
    This multiplies by the inertia ratio $I_f/I_i$. Angular speed changes by the reciprocal ratio: $\omega_f=(I_i/I_f)\omega_i$.
- id: mct-p17-platform-mirror-d
  content: |-
    $12\,\mathrm{rad/s}$
  feedback: |-
    This divides the initial angular momentum by the added inertia alone. The final rotating system contains both the original platform and the object, so $I_f=400\,\mathrm{kg\,m^2}$.
- id: mct-p17-platform-mirror-e
  content: |-
    $2.4\,\mathrm{rad/s}$
  feedback: |-
    This uses $I_f=500\,\mathrm{kg\,m^2}$ by adding the initial inertia twice incorrectly. The actual final inertia is $300+100=400\,\mathrm{kg\,m^2}$.
```

---

<a id="source-video-child-merry-go-round"></a>
## Source-Video Worked Problem: Child Lands on a Merry-Go-Round

Problem 4 in `QghXDDJtJeQ` at 9:25-13:57 models the merry-go-round as a uniform solid disk:

$$
M=500\,\mathrm{kg},
\qquad
R=10\,\mathrm m,
\qquad
\omega_i=0.5\,\mathrm{rad/s}.
$$

A $40\,\mathrm{kg}$ child lands straight down $4\,\mathrm m$ from the axis. The transcript momentarily says $50\,\mathrm{kg}$ and immediately corrects it to the stated $40\,\mathrm{kg}$.

The disk inertia is

$$
I_{\mathrm{disk}}
=\frac12MR^2
=\frac12(500)(10)^2
=\boxed{25{,}000\,\mathrm{kg\,m^2}}.
$$

Treat the child as a point mass at $r=4\,\mathrm m$:

$$
I_{\mathrm{child}}
=mr^2
=(40)(4)^2
=\boxed{640\,\mathrm{kg\,m^2}}.
$$

The straight-down arrival contributes zero initial $L_z$, so

$$
\begin{aligned}
(25{,}000)(0.5)
&=(25{,}000+640)\omega_f,\\
12{,}500
&=25{,}640\omega_f,\\
\omega_f
&=0.4875\ldots\,\mathrm{rad/s},\\
\omega_f
&\approx\boxed{0.488\,\mathrm{rad/s}}.
\end{aligned}
$$

The result is slightly below $0.5\,\mathrm{rad/s}$ because the child's added inertia is small compared with the disk's inertia.

```quiz
type: radio
id: mct-p17-merry-go-round-control
shuffle: true
content: |-
  A disk-like merry-go-round has $M=240\,\mathrm{kg}$, $R=5.0\,\mathrm m$, and $\omega_i=0.80\,\mathrm{rad/s}$. A $30\,\mathrm{kg}$ child lands vertically $3.0\,\mathrm m$ from the axis and remains there. What is $\omega_f$ if external torque about the axis is negligible?
options:
- id: mct-p17-merry-go-round-control-a
  content: |-
    $0.734\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    The disk has $I_i=\frac12(240)(5.0)^2=3000\,\mathrm{kg\,m^2}$, and the child adds $(30)(3.0)^2=270\,\mathrm{kg\,m^2}$. Thus $\omega_f=(3000)(0.80)/3270=0.734\,\mathrm{rad/s}$.
- id: mct-p17-merry-go-round-control-b
  content: |-
    $0.800\,\mathrm{rad/s}$
  feedback: |-
    This ignores the child's added inertia. The child arrives with zero initial $L_z$ but becomes part of the final rotating inertia, so the speed decreases.
- id: mct-p17-merry-go-round-control-c
  content: |-
    $0.766\,\mathrm{rad/s}$
  feedback: |-
    This models the solid disk as a hoop with $I=MR^2$. A disk uses $I=\frac12MR^2$, which makes the child's $270\,\mathrm{kg\,m^2}$ contribution a larger fraction of the initial inertia.
- id: mct-p17-merry-go-round-control-d
  content: |-
    $0.640\,\mathrm{rad/s}$
  feedback: |-
    This places the child at the rim and uses $mr^2=(30)(5.0)^2$. The child lands $3.0\,\mathrm m$ from the axis, so the added inertia is $270\,\mathrm{kg\,m^2}$.
- id: mct-p17-merry-go-round-control-e
  content: |-
    $8.89\,\mathrm{rad/s}$
  feedback: |-
    This divides the initial angular momentum by the child's inertia alone: $2400/270=8.89$. The final system includes the original $3000\,\mathrm{kg\,m^2}$ disk as well as the child.
```

---

<a id="source-video-skater"></a>
## Source-Video Control: Skater Pulls Inward

The same source video at 13:57-15:18 gives a skater with arms extended:

$$
I_i=10\,\mathrm{kg\,m^2},
\qquad
\omega_i=2\,\mathrm{rad/s}.
$$

Her angular momentum is

$$
L_z=I_i\omega_i=(10)(2)=20\,\mathrm{kg\,m^2/s}.
$$

She pulls her arms inward while remaining one system. With negligible external torque, her inertia decreases to

$$
I_f=5\,\mathrm{kg\,m^2}.
$$

Therefore,

$$
\begin{aligned}
(10)(2)&=(5)\omega_f,\\
\omega_f&=\boxed{4\,\mathrm{rad/s}}.
\end{aligned}
$$

The transcript says “four beats per second”; the correct unit is radians per second. Its inverse-change statement is valid here because the skater remains inside the same system:

$$
I\omega=L_z=\text{constant}.
$$

**Source correction.** The video also says that if a child jumps off a merry-go-round, the merry-go-round's inertia decreases and its speed increases. That conclusion is not automatic: after separation, the child may carry away angular momentum. The platform's final speed depends on the child's departure velocity and direction. Pulling arms inward while remaining coupled is the controlled case in which the inverse $I$-$\omega$ relation applies directly.

```quiz
type: radio
id: mct-p17-skater-ratio
shuffle: true
content: |-
  A skater has $I_i=12\,\mathrm{kg\,m^2}$ and $\omega_i=1.5\,\mathrm{rad/s}$. She pulls inward until $I_f=3.0\,\mathrm{kg\,m^2}$. External torque about her spin axis is negligible. What is $\omega_f$?
options:
- id: mct-p17-skater-ratio-a
  content: |-
    $6.0\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    Her angular momentum remains $(12)(1.5)=18\,\mathrm{kg\,m^2/s}$. Dividing by $I_f=3.0\,\mathrm{kg\,m^2}$ gives $\omega_f=6.0\,\mathrm{rad/s}$.
- id: mct-p17-skater-ratio-b
  content: |-
    $0.375\,\mathrm{rad/s}$
  feedback: |-
    This changes angular speed in the same direction as inertia. With fixed $L_z=I\omega$, reducing inertia by a factor of four increases angular speed by a factor of four.
- id: mct-p17-skater-ratio-c
  content: |-
    $4.5\,\mathrm{rad/s}$
  feedback: |-
    This subtracts the inertia change, $12-3=9$, rather than preserving the product $I\omega$. Conservation requires $(12)(1.5)=(3.0)\omega_f$.
- id: mct-p17-skater-ratio-d
  content: |-
    $18\,\mathrm{rad/s}$
  feedback: |-
    The value $18$ is the angular momentum magnitude in $\mathrm{kg\,m^2/s}$, not the angular speed. Divide it by the final inertia to obtain radians per second.
- id: mct-p17-skater-ratio-e
  content: |-
    $1.5\,\mathrm{rad/s}$
  feedback: |-
    This holds angular speed fixed despite the fourfold inertia decrease. With negligible external torque, angular momentum—not angular speed—stays constant.
```

---

<a id="lecture-note-rain-cups"></a>
## Lecture-Note Supplement: Rain Sticks in Rotating Cups

The paired M2-5 lecture problem has two cups, each of mass

$$
m=0.46\,\mathrm{kg},
$$

connected by a negligible-mass rod of length

$$
d=0.68\,\mathrm m.
$$

Each cup lies $d/2$ from the axis, and the initial angular speed is

$$
\omega_0=4.2\,\mathrm{rad/s}.
$$

Rain falls vertically into the cups until each captures an additional water mass $m$. The incoming rain has zero initial angular momentum about the vertical axis, and external torque about that axis is negligible. Initially,

$$
I_i=2m\left(\frac d2\right)^2=\frac12md^2.
$$

Each end mass doubles, so

$$
I_f=2I_i=md^2.
$$

Thus,

$$
\omega_f=\frac{I_i}{I_f}\omega_0
=\frac{\omega_0}{2}
=\boxed{2.1\,\mathrm{rad/s}}.
$$

Angular momentum is conserved, but mechanical energy is not. The water sticks and settles, converting mechanical energy into internal energy. The lecture calculation gives

$$
\begin{aligned}
\Delta E_{\mathrm{lost}}
&=\frac12I_i\omega_0^2-\frac12I_f\omega_f^2,\\
&=\frac{md^2\omega_0^2}{8},\\
&=0.4690\ldots\,\mathrm J,\\
&\approx\boxed{0.47\,\mathrm J}.
\end{aligned}
$$

This does not conflict with angular-momentum conservation: energy and angular momentum have different conservation conditions. For a skater who pulls inward, rotational kinetic energy can instead increase because the skater does internal work.

```quiz
type: radio
id: mct-p17-rain-control
shuffle: true
content: |-
  Two identical cups rotate at $6.0\,\mathrm{rad/s}$. Each cup initially has mass $m$ at the same fixed radius. Vertical rain with zero initial axial angular momentum adds mass $m/2$ to each cup. What is the final angular speed if external torque about the axis is negligible?
options:
- id: mct-p17-rain-control-a
  content: |-
    $4.0\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    Each end mass changes from $m$ to $1.5m$, so $I_f=1.5I_i$. Conserving $I\omega$ gives $\omega_f=(I_i/I_f)(6.0)=6.0/1.5=4.0\,\mathrm{rad/s}$.
- id: mct-p17-rain-control-b
  content: |-
    $9.0\,\mathrm{rad/s}$
  feedback: |-
    This multiplies angular speed by the inertia factor. With constant axial angular momentum, angular speed changes by the reciprocal factor, so it decreases to $4.0\,\mathrm{rad/s}$.
- id: mct-p17-rain-control-c
  content: |-
    $3.0\,\mathrm{rad/s}$
  feedback: |-
    This assumes the inertia doubles. Adding $m/2$ to each original mass $m$ makes each final mass $1.5m$, so the total inertia increases by a factor of $1.5$.
- id: mct-p17-rain-control-d
  content: |-
    $6.0\,\mathrm{rad/s}$
  feedback: |-
    The rain adds no initial axial angular momentum, but it does add final moment of inertia. The same angular momentum spread over a larger inertia gives a lower angular speed.
- id: mct-p17-rain-control-e
  content: |-
    $12\,\mathrm{rad/s}$
  feedback: |-
    This treats the added half-mass as though it removed inertia. Captured rain increases the final inertia, so the angular speed cannot double under the stated conditions.
```

---

<a id="lecture-note-tangential-bullet"></a>
## Lecture-Note Contrast: A Tangential Bullet Arrives with Angular Momentum

The paired M2-5 lecture problem uses a solid uniform cylinder initially at rest:

$$
M=2.6\,\mathrm{kg},
\qquad
R=0.85\,\mathrm m.
$$

A bullet with

$$
m=0.35\,\mathrm{kg},
\qquad
v=3.8\,\mathrm{m/s}
$$

travels tangentially and embeds in the rim. Unlike the vertical rain, the bullet begins with nonzero angular momentum about the spindle:

$$
L_{i,z}=m v R.
$$

After the inelastic collision,

$$
I_f=\frac12MR^2+mR^2.
$$

With negligible external torque about the spindle,

$$
\begin{aligned}
m v R
&=\left(\frac12MR^2+mR^2\right)\omega_f,\\
\omega_f
&=\frac{mv}{R(M/2+m)},\\
&=\frac{(0.35)(3.8)}{(0.85)[(2.6)/2+0.35]},\\
&=0.9483\ldots\,\mathrm{rad/s},\\
&\approx\boxed{0.95\,\mathrm{rad/s}}.
\end{aligned}
$$

The spindle can exert a large external force, so total linear momentum need not be conserved. Because that force acts through the spindle, it produces no torque about the spindle, allowing angular momentum about that axis to remain constant.

```quiz
type: radio
id: mct-p17-tangential-capture
shuffle: true
content: |-
  A uniform solid disk with $M=8.0\,\mathrm{kg}$ and $R=0.50\,\mathrm m$ is initially at rest. A $0.20\,\mathrm{kg}$ clay ball moving tangentially at $5.0\,\mathrm{m/s}$ sticks to the rim. What is the final angular speed if external torque about the spindle is negligible?
options:
- id: mct-p17-tangential-capture-a
  content: |-
    $0.476\,\mathrm{rad/s}$
  correct: true
  feedback: |-
    The clay brings $L_i=m v R=(0.20)(5.0)(0.50)=0.50\,\mathrm{kg\,m^2/s}$. The final inertia is $\frac12(8.0)(0.50)^2+(0.20)(0.50)^2=1.05\,\mathrm{kg\,m^2}$, so $\omega_f=0.50/1.05=0.476\,\mathrm{rad/s}$.
- id: mct-p17-tangential-capture-b
  content: |-
    $0\,\mathrm{rad/s}$
  feedback: |-
    Zero incoming axial angular momentum applies to vertical or radial arrival, not a tangential one. Here the clay contributes $m v R=0.50\,\mathrm{kg\,m^2/s}$.
- id: mct-p17-tangential-capture-c
  content: |-
    $0.500\,\mathrm{rad/s}$
  feedback: |-
    This divides by the disk's inertia alone. After sticking, the clay adds $mR^2=0.05\,\mathrm{kg\,m^2}$, making the final inertia $1.05\,\mathrm{kg\,m^2}$.
- id: mct-p17-tangential-capture-d
  content: |-
    $0.952\,\mathrm{rad/s}$
  feedback: |-
    This uses the clay's linear momentum $mv$ as though it were angular momentum. The lever arm is required: $L_z=m v R$, which is half as large here because $R=0.50\,\mathrm m$.
- id: mct-p17-tangential-capture-e
  content: |-
    $0.244\,\mathrm{rad/s}$
  feedback: |-
    This models the solid disk as a thin hoop with $I=MR^2$. A uniform solid disk about its central axis uses $I=\frac12MR^2$.
```

---

<a id="summary"></a>
## Summary

- Choose the system and axis before writing a conservation equation.
- Conserve $L_z$ only when external angular impulse about that axis is negligible during the interaction.
- Include every initial contribution:
  $$
  L_{i,z}=I\omega+mr v_t.
  $$
- Vertical and radial arrivals have $v_t=0$; tangential arrivals generally have nonzero $L_z$.
- Add all final inertias, then solve
  $$
  \omega_f=\frac{L_{i,z}}{I_f}.
  $$
- When the same closed rotating system keeps constant $L_z$, $I$ and $\omega$ vary inversely.
- A sticking interaction can conserve angular momentum while losing mechanical energy.
- An object that leaves can carry angular momentum away, so removing it does not automatically make the remaining platform speed up.
- Check angular momentum in $\mathrm{kg\,m^2/s}$ and angular speed in $\mathrm{rad/s}$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
