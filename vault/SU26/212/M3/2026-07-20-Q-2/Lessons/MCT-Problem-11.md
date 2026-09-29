# Choose a Pivot to Solve Unknown Support Reactions

<!--
lesson-id: 212-M3-047
topic-code: MTH212.M3.47
-->

## Table of Contents

- [Introduction](#introduction)
- [Separate Weight from Contact Force](#separate-weight-from-contact-force)
- [Source-Video Worked Problem: Balanced Seesaw](#source-video-balanced-seesaw)
- [Make One Support Reaction Disappear](#make-one-support-reaction-disappear)
- [Source-Video Worked Problem: Supported Beam](#source-video-supported-beam)
- [Use the Reactions as a Physical Check](#use-reactions-as-a-check)
- [Lecture-Note Contrast: The Tipping Boundary](#lecture-note-tipping-boundary)
- [Summary](#summary)

## Prerequisites

- Draw an extended free-body diagram that shows where each force acts.
- Use $W=mg$ and distinguish an object's weight from a contact force.
- Place the weight of a uniform beam or plank at its center.
- Apply $\sum F_y=0$ and $\sum\tau=0$ in static equilibrium.
- Compute torque with the perpendicular lever arm.
- Solve a two-equation linear system by substitution or elimination.

---

<a id="introduction"></a>
## Introduction

A stationary beam on two supports usually has two unknown upward reactions. The vertical-force equation gives their sum, but not their individual values:

$$
R_L+R_R=\text{total downward load}.
$$

The second equation comes from torque equilibrium. Choose one support as the torque pivot. That support's reaction then has zero lever arm, so its torque vanishes and the other reaction can be found directly.

Use this sequence:

1. Draw the beam's extended free-body diagram.
2. Write $\sum F_y=0$ to relate the two reactions to the total load.
3. Take torques about one support, eliminating the reaction at that support.
4. Solve for the opposite reaction.
5. Return to the vertical-force equation for the remaining reaction.
6. Check that the reactions add to the total load. For an otherwise symmetric beam, the nearer support carries more of an added off-center load.

The chosen pivot is a point about which torques are calculated. The beam does not need to rotate about that point.

---

<a id="separate-weight-from-contact-force"></a>
## Separate Weight from Contact Force

Suppose a box of mass $m$ rests on a beam. Gravity exerts the box's weight $mg$ downward **on the box**. The beam pushes upward on the box with a normal force $N_{B\to b}$. Because the box has no vertical acceleration,

$$
N_{B\to b}-mg=0,
$$

so $N_{B\to b}=mg$ in magnitude. Newton's third law gives the force that belongs on the beam's diagram:

$$
N_{b\to B}=N_{B\to b}=mg,
$$

directed downward on the beam. The contact force and the weight have equal magnitudes here, but they are different forces acting on different objects.

If the beam, box, and any riders are treated as one combined system, their internal normal forces cancel. Then the external weights may be placed directly on the combined-system diagram. State which system you chose before writing equations.

For a uniform beam of mass $M$ and length $L$, its weight $Mg$ acts at its center, $L/2$ from either end.

```quiz
type: radio
id: mct-p11-contact-force
shuffle: true
content: |-
  A $12.0\,\mathrm{kg}$ crate rests motionless on a horizontal beam. Which force due to the crate belongs on a free-body diagram of the beam? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p11-contact-force-a
  content: |-
    A downward normal force exerted by the crate, with magnitude $117.6\,\mathrm N$
  correct: true
  feedback: |-
    The crate is vertically at rest, so the beam's upward normal on the crate equals $mg=117.6\,\mathrm N$. By Newton's third law, the crate exerts an equal downward normal force on the beam.
- id: mct-p11-contact-force-b
  content: |-
    The crate's downward gravitational force, with magnitude $117.6\,\mathrm N$
  feedback: |-
    Gravity exerts that weight on the crate, not on the beam. The force transmitted to the beam is the crate's downward normal contact force; its magnitude happens to equal $mg$ because the crate is vertically at rest.
- id: mct-p11-contact-force-c
  content: |-
    An upward normal force exerted by the crate, with magnitude $117.6\,\mathrm N$
  feedback: |-
    The beam pushes upward on the crate. The third-law partner acting on the beam points downward, so the crate's force on the beam is not upward.
- id: mct-p11-contact-force-d
  content: |-
    A downward normal force exerted by the crate, with magnitude $12.0\,\mathrm N$
  feedback: |-
    The mass is $12.0\,\mathrm{kg}$, but force requires multiplication by $g$. Static vertical equilibrium gives $N=mg=(12.0)(9.8)=117.6\,\mathrm N$.
- id: mct-p11-contact-force-e
  content: |-
    No force, because the crate is not accelerating
  feedback: |-
    Zero acceleration means the forces on the crate balance; it does not mean the contact force is zero. The crate still presses downward on the beam with $117.6\,\mathrm N$.
```

---

<a id="source-video-balanced-seesaw"></a>
## Source-Video Worked Problem: Balanced Seesaw

The source video `qGvFAl5CK_c` at 2:08-7:47 uses:

- a $40\,\mathrm{kg}$ child $3\,\mathrm m$ to the left of the pivot,
- a $30\,\mathrm{kg}$ child an unknown distance $x$ to the right,
- a uniform $10\,\mathrm{kg}$ bar centered on the pivot, and
- an upward reaction $N$ at the pivot.

```text
       40 kg             10 kg bar              30 kg
         ↓                  ↓                      ↓
---------|------------------▲----------------------|---------
       x=-3 m            pivot, x=0              x=+x
                            ↑ N
```

For the combined bar-and-children system, vertical equilibrium gives

$$
\begin{aligned}
\sum F_y&=0,\\
N-(40+30+10)g&=0,\\
N&=(80)(9.8)=\boxed{784\,\mathrm N}.
\end{aligned}
$$

Choose the central support as the torque pivot. Both $N$ and the uniform bar's weight act at the pivot, so neither produces torque. Taking counterclockwise as positive,

$$
(40g)(3)-(30g)x=0.
$$

Cancel $g$ and solve:

$$
\begin{aligned}
120&=30x,\\
x&=\boxed{4.0\,\mathrm m}.
\end{aligned}
$$

**Source corrections.** The video calls the downward force from a child on the bar the child's weight. More precisely, it is the child's normal contact force on the bar; its magnitude equals the child's weight while the child is vertically at rest. The narration also says “30 over 40” before calling the ratio $4/3$. The ratio used in the correct calculation is $40/30=4/3$, which gives $x=4\,\mathrm m$.

```quiz
type: radio
id: mct-p11-seesaw-mirror
shuffle: true
content: |-
  A $36\,\mathrm{kg}$ child sits $2.50\,\mathrm m$ left of a seesaw pivot. A $24\,\mathrm{kg}$ child sits a distance $x$ to the right. The uniform $12\,\mathrm{kg}$ bar is centered on the pivot. Where must the second child sit for balance?
options:
- id: mct-p11-seesaw-mirror-a
  content: |-
    $x=3.75\,\mathrm m$
  correct: true
  feedback: |-
    The centered bar and pivot reaction have zero lever arms. Torque balance gives $(36g)(2.50)=(24g)x$, so $x=(36/24)(2.50)=3.75\,\mathrm m$.
- id: mct-p11-seesaw-mirror-b
  content: |-
    $x=1.67\,\mathrm m$
  feedback: |-
    This reverses the mass ratio. The lighter child needs the longer lever arm, so the correct relation is $x=(36/24)(2.50)$, not $(24/36)(2.50)$.
- id: mct-p11-seesaw-mirror-c
  content: |-
    $x=2.50\,\mathrm m$
  feedback: |-
    Equal distances balance only equal force magnitudes. The right child is lighter, so that child must sit farther than $2.50\,\mathrm m$ from the pivot.
- id: mct-p11-seesaw-mirror-d
  content: |-
    $x=5.00\,\mathrm m$
  feedback: |-
    This assigns the centered bar's entire mass to the left torque. Its weight acts at the pivot, so its lever arm and torque are zero.
- id: mct-p11-seesaw-mirror-e
  content: |-
    $x=0$
  feedback: |-
    A force at the pivot makes no torque. Placing the second child at $x=0$ cannot balance the nonzero torque from the child on the left.
```

---

<a id="make-one-support-reaction-disappear"></a>
## Make One Support Reaction Disappear

Consider a beam supported at $x=0$ and $x=L$. Let $R_L$ and $R_R$ be the upward support reactions, and let downward loads $W_i$ act at positions $x_i$ measured from the left support.

Vertical equilibrium gives the first equation:

$$
\boxed{R_L+R_R=\sum_i W_i}. \tag{1}
$$

Take torques about the left support. The reaction $R_L$ is not zero, but its lever arm is zero. With counterclockwise positive,

$$
R_R L-\sum_i W_i x_i=0,
$$

so

$$
\boxed{R_R=\frac{\sum_i W_i x_i}{L}}. \tag{2}
$$

Then use equation (1):

$$
\boxed{R_L=\sum_i W_i-R_R}. \tag{3}
$$

Choosing the right support instead gives the same reactions. To find $R_R$ directly, pivot at the left support; to find $R_L$ directly, pivot at the right support.

```quiz
type: radio
id: mct-p11-pivot-equation
shuffle: true
content: |-
  A beam of length $L$ has upward reactions $R_L$ at $x=0$ and $R_R$ at $x=L$. Downward loads $W_1$ and $W_2$ act at $x_1$ and $x_2$. Which torque equation about the left support correctly eliminates $R_L$?
options:
- id: mct-p11-pivot-equation-a
  content: |-
    $R_R L-W_1x_1-W_2x_2=0$
  correct: true
  feedback: |-
    About the left support, $R_L$ has zero lever arm. The right reaction turns counterclockwise, while both downward loads to the right turn clockwise, giving $R_R L-W_1x_1-W_2x_2=0$.
- id: mct-p11-pivot-equation-b
  content: |-
    $R_L L+R_R L-W_1x_1-W_2x_2=0$
  feedback: |-
    The left reaction acts at the chosen pivot, so its lever arm is $0$, not $L$. Its torque term disappears even though $R_L$ itself is generally nonzero.
- id: mct-p11-pivot-equation-c
  content: |-
    $R_R L+W_1x_1+W_2x_2=0$
  feedback: |-
    The right reaction and the downward loads turn the beam in opposite senses about the left support. Their torque terms must have opposite signs.
- id: mct-p11-pivot-equation-d
  content: |-
    $R_L+R_R-W_1-W_2=0$
  feedback: |-
    This is the vertical-force equation, not a torque equation. It supplies the total reaction but cannot determine either reaction alone.
- id: mct-p11-pivot-equation-e
  content: |-
    $R_R-W_1-W_2=0$
  feedback: |-
    Dropping $R_L$ from the force balance is not valid. Pivot choice removes $R_L$ only from the torque equation because its lever arm is zero.
```

---

<a id="source-video-supported-beam"></a>
## Source-Video Worked Problem: Supported Beam

The second source segment, `qGvFAl5CK_c` at 17:56-24:20, has:

- a uniform $100\,\mathrm{kg}$ beam,
- supports $10\,\mathrm m$ apart at the beam's ends,
- the beam's weight at its center, $5\,\mathrm m$ from the left support, and
- a $20\,\mathrm{kg}$ box $8\,\mathrm m$ from the left support.

Call the upward reactions $F_1$ on the left and $F_2$ on the right.

```text
             beam weight 980 N       box contact 196 N
                       ↓                       ↓
      ↑ F1             |                       |       ↑ F2
------▲----------------|-----------------------|-------▲------
     x=0 m            x=5 m                  x=8 m   x=10 m
```

The box exerts a downward normal force on the beam. Because the box is at rest, that contact force has magnitude $(20)(9.8)=196\,\mathrm N$. The uniform beam's own weight is $(100)(9.8)=980\,\mathrm N$.

First use vertical equilibrium:

$$
\begin{aligned}
F_1+F_2-980-196&=0,\\
F_1+F_2&=\boxed{1176\,\mathrm N}. \tag{4}
\end{aligned}
$$

Now choose the left support as the pivot. Its unknown reaction $F_1$ makes no torque:

$$
(10)F_2-(5)(980)-(8)(196)=0.
$$

Therefore,

$$
\begin{aligned}
10F_2&=4900+1568,\\
F_2&=\boxed{646.8\,\mathrm N}.
\end{aligned}
$$

Return to equation (4):

$$
\begin{aligned}
F_1&=1176-646.8,\\
F_1&=\boxed{529.2\,\mathrm N}.
\end{aligned}
$$

The two checks agree with the geometry:

$$
529.2+646.8=1176\,\mathrm N,
$$

$$
(646.8)(10)=(980)(5)+(196)(8)=6468\,\mathrm{N\,m},
$$

and the right reaction is larger because the added box is closer to the right support. The reactions therefore satisfy both original equilibrium equations, not just the equation used last.

```quiz
type: radio
id: mct-p11-beam-control
shuffle: true
content: |-
  A uniform $80.0\,\mathrm{kg}$ beam is supported at both ends, $12.0\,\mathrm m$ apart. A $24.0\,\mathrm{kg}$ crate rests $9.0\,\mathrm m$ from the left support. What are the left and right reactions $(R_L,R_R)$? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p11-beam-control-a
  content: |-
    $(450.8\,\mathrm N,\ 568.4\,\mathrm N)$
  correct: true
  feedback: |-
    About the left support, $12R_R=(784)(6)+(235.2)(9)$, so $R_R=568.4\,\mathrm N$. The force sum is $1019.2\,\mathrm N$, giving $R_L=1019.2-568.4=450.8\,\mathrm N$.
- id: mct-p11-beam-control-b
  content: |-
    $(509.6\,\mathrm N,\ 509.6\,\mathrm N)$
  feedback: |-
    Equal reactions would require symmetric loading. The crate is right of center, so torque balance shifts more of its load to the right support.
- id: mct-p11-beam-control-c
  content: |-
    $(568.4\,\mathrm N,\ 450.8\,\mathrm N)$
  feedback: |-
    These values are reversed. A load at $x=9.0\,\mathrm m$ on a $12.0\,\mathrm m$ beam lies closer to the right support, so the right reaction must be the larger one.
- id: mct-p11-beam-control-d
  content: |-
    $(784.0\,\mathrm N,\ 235.2\,\mathrm N)$
  feedback: |-
    These are the separate downward load magnitudes, not the support reactions. Each support shares both loads according to their lever arms.
- id: mct-p11-beam-control-e
  content: |-
    $(1019.2\,\mathrm N,\ 568.4\,\mathrm N)$
  feedback: |-
    The first value treats the total load as the left reaction without subtracting the right reaction. Support reactions must add to $1019.2\,\mathrm N$, so $R_L=450.8\,\mathrm N$.
```

---

<a id="use-reactions-as-a-check"></a>
## Use the Reactions as a Physical Check

For an otherwise symmetric beam, an added point load increases the nearer support reaction by more than it increases the farther reaction. For example, place a $15\,\mathrm{kg}$ box $2.0\,\mathrm m$ from the left end of a uniform $60\,\mathrm{kg}$, $8.0\,\mathrm m$ beam. About the left support,

$$
8R_R=(588)(4)+(147)(2),
$$

so

$$
R_R=330.75\,\mathrm N,
\qquad
R_L=735-330.75=404.25\,\mathrm N.
$$

Here $R_L>R_R$, as expected because the box is left of center. This directional check can catch a swapped lever arm or reaction label.

The same equations can locate an unknown load. Use the measured reaction opposite the chosen pivot, write the torque balance, and solve for the load's position.

```quiz
type: radio
id: mct-p11-inverse-load
shuffle: true
content: |-
  A uniform $50.0\,\mathrm{kg}$ beam is supported at both ends, $10.0\,\mathrm m$ apart. A $20.0\,\mathrm{kg}$ crate rests at an unknown position $x$ from the left support. The measured reactions are $R_L=294\,\mathrm N$ and $R_R=392\,\mathrm N$. Where is the crate? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p11-inverse-load-a
  content: |-
    $x=7.50\,\mathrm m$
  correct: true
  feedback: |-
    About the left support, $(392)(10)=(490)(5)+(196)x$. Solving gives $196x=1470$, so the crate is $7.50\,\mathrm m$ from the left support.
- id: mct-p11-inverse-load-b
  content: |-
    $x=5.00\,\mathrm m$
  feedback: |-
    The beam's own weight acts at $5.00\,\mathrm m$, but the unequal reactions show that the crate is not centered. Since $R_R>R_L$, the crate must lie right of center.
- id: mct-p11-inverse-load-c
  content: |-
    $x=2.50\,\mathrm m$
  feedback: |-
    This is the crate's distance from the right support, $10.0-7.50=2.50\,\mathrm m$. The question asks for distance from the left support.
- id: mct-p11-inverse-load-d
  content: |-
    $x=20.0\,\mathrm m$
  feedback: |-
    This omits the beam's $2450\,\mathrm{N\,m}$ torque and assigns all right-reaction torque to the crate. The beam's centered weight must remain in the torque equation.
- id: mct-p11-inverse-load-e
  content: |-
    $x=10.0\,\mathrm m$
  feedback: |-
    A crate at the right support would put all $196\,\mathrm N$ of its added load on that support, giving reactions $245\,\mathrm N$ and $441\,\mathrm N$. The measured values instead place it at $7.50\,\mathrm m$.
```

---

<a id="lecture-note-tipping-boundary"></a>
## Lecture-Note Contrast: The Tipping Boundary

The paired M2-4 lecture notes use a tipping example only to mark the boundary of the ordinary two-support method. Support $A$ is at $L/5$ from the plank's left end, and support $B$ is at $2L/3$. Before tipping, both support reactions may be positive. At the instant the plank begins to tip about support $B$, it loses contact with support $A$, so

$$
N_A=0.
$$

The remaining support $B$ is then the natural pivot. For the lecture's uniform plank, support $B$ lies at $2L/3$ while the center of mass lies at $L/2$, a distance $L/6$ to the left. A box of mass $m$ sits a distance $x$ to the right of $B$. At the threshold,

$$
mgx=Mg\frac{L}{6},
$$

so

$$
x=\frac{ML}{6m}.
$$

With $M=2.4\,\mathrm{kg}$, $m=1.6\,\mathrm{kg}$, and $L=1.4\,\mathrm m$, the notes obtain

$$
x=0.35\,\mathrm m.
$$

Do not set a support reaction to zero in an ordinary supported-beam problem. That condition applies only when the problem states or implies loss of contact at the tipping threshold.

---

<a id="summary"></a>
## Summary

- Put only forces acting on the chosen system in its free-body diagram.
- A resting object pushes on a beam through a normal contact force; its magnitude equals $mg$ only because the object is vertically at rest.
- Put a uniform beam's weight at its center.
- Start with
  $$
  R_L+R_R=\text{total downward load}.
  $$
- Choose one support as the torque pivot. Its reaction has zero torque because its lever arm is zero, not because the reaction itself is zero.
- Solve the opposite reaction from torque equilibrium, then use the force sum to find the reaction at the pivot.
- Substitute the reactions into both the force and torque equations; a solution must satisfy both.
- Check that both reactions sum to the total load. With otherwise symmetric loading, the larger reaction lies nearer an added off-center load.
- Set a support reaction to zero only at a stated loss-of-contact or tipping boundary.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
