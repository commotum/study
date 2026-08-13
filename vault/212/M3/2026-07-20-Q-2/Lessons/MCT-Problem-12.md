# Solve a Hinged Beam Supported by a Cable

<!--
lesson-id: 212-M3-048
topic-code: MTH212.M3.48
-->

## Table of Contents

- [Introduction](#introduction)
- [Draw the Extended Free-Body Diagram](#draw-the-extended-free-body-diagram)
- [Solve the Horizontal Source-Video Beam](#solve-the-horizontal-source-video-beam)
- [Use the Supplied Perpendicular Arm](#use-the-supplied-perpendicular-arm)
- [Return to Force Balance](#return-to-force-balance)
- [Summary](#summary)

## Prerequisites

- Resolve a force into horizontal and vertical components.
- Use $\tau=Fd_\perp$ or $\tau=rF\sin\theta$ with a consistent sign convention.
- Place the weight of a uniform beam at its midpoint.
- Apply $\sum F_x=0$, $\sum F_y=0$, and $\sum\tau=0$ in static equilibrium.

---

<a id="introduction"></a>
## Introduction

A hinged beam held by a cable has three unknown force quantities: the cable tension $T$ and the hinge-reaction components $H_x$ and $H_y$. Choosing the hinge as the torque pivot removes both hinge components from the torque equation, leaving an equation for $T$.

Use this order:

1. Draw an extended free-body diagram, including where every force acts.
2. Choose the hinge as the pivot.
3. Write $\sum\tau_{\mathrm{hinge}}=0$ and solve for $T$.
4. Return to $\sum F_x=0$ and $\sum F_y=0$ to solve $H_x$ and $H_y$.

This order isolates one set of unknowns at a time:

| Equation | Unknown solved first | Why |
| --- | --- | --- |
| $\sum\tau_{\mathrm{hinge}}=0$ | $T$ | Both hinge components act through the pivot |
| $\sum F_x=0$ | $H_x$ | $T$ is now known |
| $\sum F_y=0$ | $H_y$ | $T$ is now known |

For each torque, use either the perpendicular distance from the pivot to the force's line of action,

$$
\tau=Fd_\perp,
$$

or the equivalent angle form,

$$
\tau=rF\sin\theta.
$$

Here $\theta$ is the angle between the position vector $\vec r$ and the force $\vec F$. Do not switch meanings halfway through a torque ledger.

The moment arm $d_\perp$ is the shortest perpendicular distance from the hinge to the force's entire line of action. It is not generally the distance from the hinge to the force's attachment point.

The M2-4 lecture note states that a force whose line of action passes through the chosen pivot has zero torque about that pivot, but the force itself need not be zero. The hinge can exert horizontal and vertical forces even though neither appears in $\sum\tau_{\mathrm{hinge}}=0$.

---

<a id="draw-the-extended-free-body-diagram"></a>
## Draw the Extended Free-Body Diagram

For a uniform horizontal beam of length $L$ with a sign at its far end and a cable making angle $\phi$ above the beam, the extended free-body diagram has this structure:

```text
                          ↖ T
                            \  phi
H_y ↑                        \
    ●───────────────┬─────────●
    → H_x           ↓         ↓
                   W_b       W_s
 hinge             L/2        L
```

- The hinge supplies two independent components, $H_x$ and $H_y$; it is not a single force with a known direction.
- The uniform beam's weight $W_b=M_bg$ acts at $L/2$.
- The sign's weight $W_s=m_sg$ acts at its attachment point.
- The cable pulls along itself toward its anchor.

Taking counterclockwise torque as positive, the cable's vertical component produces positive torque. Its horizontal component acts along the horizontal beam, so its line of action passes through the hinge and its torque is zero. The torque equation is

$$
(T\sin\phi)L-W_sL-W_b\frac L2=0.
$$

```quiz
type: radio
id: mct-p12-pivot-ledger
shuffle: true
content: |-
  A uniform horizontal beam of length $L$ and mass $M$ is hinged at its left end. A sign of mass $m$ hangs from the right end, where a cable at angle $\phi$ above the beam is also attached. With counterclockwise torque positive, which equation is the correct torque balance about the hinge?
options:
- id: mct-p12-pivot-ledger-a
  content: |-
    $(T\sin\phi)L-mgL-Mg\dfrac L2=0$
  correct: true
  feedback: |-
    About the hinge, only the cable's perpendicular component produces counterclockwise torque. The sign acts at $L$ and the uniform beam's weight at $L/2$, so the balance is $(T\sin\phi)L-mgL-Mg(L/2)=0$.
- id: mct-p12-pivot-ledger-b
  content: |-
    $(T\sin\phi)L-mgL-MgL=0$
  feedback: |-
    This places the uniform beam's entire weight at its far end. A uniform beam's center of mass is at its midpoint, so its weight has lever arm $L/2$, while only the sign has lever arm $L$.
- id: mct-p12-pivot-ledger-c
  content: |-
    $(T\cos\phi)L-mgL-Mg\dfrac L2=0$
  feedback: |-
    For a horizontal beam, the cable's vertical component is perpendicular to the beam and creates torque. $T\cos\phi$ is horizontal, so its line of action passes through the hinge and gives zero torque here.
- id: mct-p12-pivot-ledger-d
  content: |-
    $H_yL+(T\sin\phi)L-mgL-Mg\dfrac L2=0$
  feedback: |-
    $H_y$ acts at the hinge, so its moment arm about the hinge is zero rather than $L$. The hinge force can be nonzero, but it contributes no term to this torque equation.
- id: mct-p12-pivot-ledger-e
  content: |-
    $(T\sin\phi)L-mgL=0$
  feedback: |-
    This omits the beam's own weight. Because the beam is massive and uniform, $Mg$ acts at $L/2$ and must appear in the torque ledger.
```

---

<a id="solve-the-horizontal-source-video-beam"></a>
## Solve the Horizontal Source-Video Beam

**Source-video worked problem (`qGvFAl5CK_c`, 00:24:20–00:31:58):** A horizontal uniform beam is $2.0\,\mathrm m$ long and has mass $30\,\mathrm{kg}$. A $200\,\mathrm{kg}$ sign hangs from the far end. A cable attached at that same end makes a $30^\circ$ angle above the beam.

**Frame check (24:45):** The video frame shows the hinge at the left end, the $2.0\,\mathrm m$ horizontal beam, and both the cable and sign attached at the far end. The beam's $30\,\mathrm{kg}$ label is centered on the beam.

The weights are

$$
W_s=(200)(9.8)=1960\,\mathrm N,
\qquad
W_b=(30)(9.8)=294\,\mathrm N.
$$

Take torques about the hinge. The cable's vertical component acts at $2.0\,\mathrm m$, the sign acts at $2.0\,\mathrm m$, and the beam's weight acts at its midpoint, $1.0\,\mathrm m$:

$$
(T\sin30^\circ)(2.0)-(1960)(2.0)-(294)(1.0)=0.
$$

Therefore,

$$
T\sin30^\circ=2107\,\mathrm N,
\qquad
\boxed{T=4214\,\mathrm N}.
$$

Now return to force balance. The cable pulls left and up, so the hinge must push right. Horizontally,

$$
H_x-T\cos30^\circ=0,
$$

which gives

$$
\boxed{H_x=3649.4\,\mathrm N\ \text{to the right}}.
$$

Vertically,

$$
H_y+T\sin30^\circ-1960-294=0,
$$

so

$$
\boxed{H_y=147\,\mathrm N\ \text{upward}}.
$$

The cable supports $2107\,\mathrm N$ of the total $2254\,\mathrm N$ weight. The hinge supplies the remaining $147\,\mathrm N$; zero hinge torque did not mean zero hinge force.

```quiz
type: radio
id: mct-p12-horizontal-mirrored
shuffle: true
content: |-
  A uniform horizontal beam is $3.0\,\mathrm m$ long and has mass $20\,\mathrm{kg}$. An $80\,\mathrm{kg}$ sign and a supporting cable are attached at the far end. The cable is $40^\circ$ above the beam. Using $g=9.8\,\mathrm{m/s^2}$, what is the cable tension?
options:
- id: mct-p12-horizontal-mirrored-a
  content: |-
    $1.37\times10^3\,\mathrm N$
  correct: true
  feedback: |-
    Pivoting at the hinge gives $(T\sin40^\circ)(3.0)=(784)(3.0)+(196)(1.5)$. Thus $T\sin40^\circ=882\,\mathrm N$ and $T=1372\,\mathrm N\approx1.37\times10^3\,\mathrm N$.
- id: mct-p12-horizontal-mirrored-b
  content: |-
    $882\,\mathrm N$
  feedback: |-
    This is the cable's vertical component, $T\sin40^\circ$, not the cable's full tension. Divide $882\,\mathrm N$ by $\sin40^\circ$ to obtain $T\approx1372\,\mathrm N$.
- id: mct-p12-horizontal-mirrored-c
  content: |-
    $1.22\times10^3\,\mathrm N$
  feedback: |-
    This balances only the sign's torque and omits the $20\,\mathrm{kg}$ beam. The beam's $196\,\mathrm N$ weight acts at $1.5\,\mathrm m$ and raises the required tension to about $1372\,\mathrm N$.
- id: mct-p12-horizontal-mirrored-d
  content: |-
    $1.52\times10^3\,\mathrm N$
  feedback: |-
    This treats the beam's weight as though it acts at the far end. A uniform beam's weight acts at its midpoint, so its torque is $(196)(1.5)$ rather than $(196)(3.0)$.
- id: mct-p12-horizontal-mirrored-e
  content: |-
    $980\,\mathrm N$
  feedback: |-
    The total weight is not the cable tension because only $T\sin40^\circ$ supports vertically, and the beam and sign have different lever arms. Torque balance, not a direct equality between $T$ and total weight, gives $T\approx1372\,\mathrm N$.
```

---

<a id="use-the-supplied-perpendicular-arm"></a>
## Use the Supplied Perpendicular Arm

**Source-video worked problem (`qGvFAl5CK_c`, 00:31:58–00:44:07):** A uniform $10\,\mathrm m$ beam of mass $20\,\mathrm{kg}$ is inclined $30^\circ$ above horizontal. A $15\,\mathrm{kg}$ sign hangs from the far end. A horizontal cable pulls left on the beam, and its line of action is $4.0\,\mathrm m$ above the hinge.

**Frame check (32:55):** The cable is horizontal, the beam is inclined, and the $4.0\,\mathrm m$ label is vertical from the hinge to the cable's line of action. It is the cable's perpendicular moment arm, not the distance along the beam and not the full $10\,\mathrm m$ beam length.

The horizontal cable produces counterclockwise torque $T(4.0)$. A position vector along the beam points $30^\circ$ above horizontal, while each weight points $90^\circ$ below horizontal. Their vector separation is $120^\circ$, and

$$
\sin120^\circ=\sin60^\circ=\cos30^\circ.
$$

Thus the perpendicular arms of the sign and beam weights are their horizontal distances, $10\cos30^\circ=10\sin60^\circ$ and $5\cos30^\circ=5\sin60^\circ$. The sign is $10\,\mathrm m$ from the hinge, while the uniform beam's weight acts $5.0\,\mathrm m$ from the hinge. The torque ledger is

$$
4T-[147(10)\sin60^\circ]-[196(5)\sin60^\circ]=0.
$$

The two clockwise torque magnitudes are

$$
1470\sin60^\circ=1273.0\,\mathrm{N\,m},
$$

and

$$
980\sin60^\circ=848.7\,\mathrm{N\,m}.
$$

**Source correction:** The captions state $2221.7$ while the written terms are being added. The correct sum is

$$
1273.0+848.7=2121.7\,\mathrm{N\,m}.
$$

Therefore,

$$
\boxed{T=\frac{2121.7}{4}=530.4\,\mathrm N}.
$$

The angle form gives the same cable torque without changing the geometry. The attachment point is $4/\sin30^\circ=8\,\mathrm m$ along the beam, and the angle between its position vector and the leftward cable force is $150^\circ$:

$$
rT\sin\theta=(8)T\sin150^\circ=4T.
$$

The supplied $4.0\,\mathrm m$ arm makes that detour unnecessary. Never replace a labeled perpendicular arm with the beam's total length.

Because the cable is horizontal, force balance gives

$$
\boxed{H_x=530.4\,\mathrm N\ \text{to the right}},
\qquad
\boxed{H_y=147+196=343\,\mathrm N\ \text{upward}}.
$$

```quiz
type: radio
id: mct-p12-inclined-controlled
shuffle: true
content: |-
  A uniform $8.0\,\mathrm m$ beam of mass $10\,\mathrm{kg}$ is inclined $30^\circ$ above horizontal. A $12\,\mathrm{kg}$ sign hangs from its far end. A horizontal cable has a supplied perpendicular moment arm of $3.0\,\mathrm m$ about the hinge. With counterclockwise torque positive, which torque equation is correct? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p12-inclined-controlled-a
  content: |-
    $3T-[117.6(8)\sin60^\circ]-[98(4)\sin60^\circ]=0$
  correct: true
  feedback: |-
    The horizontal cable uses its supplied $3.0\,\mathrm m$ perpendicular arm. The sign acts at $8.0\,\mathrm m$, and the uniform beam's $98\,\mathrm N$ weight acts at $4.0\,\mathrm m$. Each weight is separated from the beam direction by $120^\circ$, and $\sin120^\circ=\sin60^\circ$.
- id: mct-p12-inclined-controlled-b
  content: |-
    $8T-[117.6(8)\sin60^\circ]-[98(4)\sin60^\circ]=0$
  feedback: |-
    This uses the entire beam length as the cable's moment arm. Torque uses the perpendicular distance to the cable's horizontal line of action, which the prompt supplies as $3.0\,\mathrm m$.
- id: mct-p12-inclined-controlled-c
  content: |-
    $3T-[117.6(8)\sin30^\circ]-[98(4)\sin30^\circ]=0$
  feedback: |-
    The angle in $rF\sin\theta$ is between the inclined position vector and each downward weight. That angle is $120^\circ$, whose sine equals $\sin60^\circ$, not $\sin30^\circ$.
- id: mct-p12-inclined-controlled-d
  content: |-
    $3T-[117.6(8)\sin60^\circ]-[98(8)\sin60^\circ]=0$
  feedback: |-
    This places the uniform beam's weight at the far end. Its center of mass is halfway along the $8.0\,\mathrm m$ beam, so the correct position magnitude is $4.0\,\mathrm m$.
- id: mct-p12-inclined-controlled-e
  content: |-
    $3T-[117.6(8)\sin60^\circ]=0$
  feedback: |-
    The beam is massive, so its own $98\,\mathrm N$ weight contributes clockwise torque from the midpoint. Omitting that term understates the required cable tension.
```

---

<a id="return-to-force-balance"></a>
## Return to Force Balance

Do not guess the direction of the hinge reaction. Draw $H_x$ and $H_y$ in convenient positive directions, solve the signed component equations, and reverse any component whose answer is negative.

For a horizontal beam with a cable pulling up and left at angle $\phi$,

| Force | $x$-component | $y$-component |
| --- | ---: | ---: |
| Hinge on beam | $+H_x$ | $+H_y$ |
| Cable on beam | $-T\cos\phi$ | $+T\sin\phi$ |
| Combined weight | $0$ | $-W_{\mathrm{total}}$ |

Adding each component column separately gives

$$
H_x=T\cos\phi,
\qquad
H_y=W_{\mathrm{total}}-T\sin\phi.
$$

For example, if $T=800\,\mathrm N$, $\phi=30^\circ$, and the combined downward weight is $500\,\mathrm N$, then

$$
H_x=(800)\cos30^\circ=692.8\,\mathrm N
$$

to the right, and

$$
H_y=500-(800)\sin30^\circ=100\,\mathrm N
$$

upward. If the cable's vertical component exceeded the total weight, $H_y$ would be negative, meaning the hinge pushes downward on the beam.

```quiz
type: radio
id: mct-p12-hinge-components
shuffle: true
content: |-
  A cable pulls up and left on a horizontal hinged beam with tension $900\,\mathrm N$ at $35^\circ$ above the beam. The beam and its load have a combined weight of $600\,\mathrm N$. Which hinge-reaction components satisfy force balance?
options:
- id: mct-p12-hinge-components-a
  content: |-
    $H_x=737\,\mathrm N$ right and $H_y=83.8\,\mathrm N$ up
  correct: true
  feedback: |-
    The hinge opposes the cable's leftward component, so $H_x=900\cos35^\circ=737\,\mathrm N$ right. Vertically, $H_y=600-900\sin35^\circ=83.8\,\mathrm N$ upward.
- id: mct-p12-hinge-components-b
  content: |-
    $H_x=737\,\mathrm N$ left and $H_y=83.8\,\mathrm N$ up
  feedback: |-
    The cable already pulls left with $900\cos35^\circ=737\,\mathrm N$. Horizontal equilibrium requires the hinge component to point right, opposite the cable's horizontal component.
- id: mct-p12-hinge-components-c
  content: |-
    $H_x=737\,\mathrm N$ right and $H_y=1116\,\mathrm N$ up
  feedback: |-
    This adds the cable's upward component to the total weight. The cable already supports $900\sin35^\circ=516\,\mathrm N$, so the hinge supplies only the remaining $600-516=83.8\,\mathrm N$ upward.
- id: mct-p12-hinge-components-d
  content: |-
    $H_x=900\,\mathrm N$ right and $H_y=83.8\,\mathrm N$ up
  feedback: |-
    The full tension is directed along the angled cable. Only its horizontal component, $T\cos35^\circ=737\,\mathrm N$, must be balanced by $H_x$.
- id: mct-p12-hinge-components-e
  content: |-
    $H_x=737\,\mathrm N$ right and $H_y=600\,\mathrm N$ up
  feedback: |-
    This makes the hinge support all the weight and ignores the cable's upward component. Vertical equilibrium requires $H_y+T\sin35^\circ=600\,\mathrm N$, giving $H_y=83.8\,\mathrm N$.
```

---

<a id="summary"></a>
## Summary

For a static beam held by a hinge and cable:

1. Draw an extended free-body diagram. Put a uniform beam's weight at its midpoint.
2. Resolve the hinge reaction into independent components $H_x$ and $H_y$.
3. Pivot at the hinge so both hinge-force terms have zero moment arm.
4. Build one signed torque ledger using either $Fd_\perp$ or $rF\sin\theta$.
5. Solve the torque equation for $T$ before using force balance.
6. Use $\sum F_x=0$ and $\sum F_y=0$ to find the signed hinge components.

The main traps are treating a zero-torque hinge force as a zero force, putting the beam's weight at an end, using an along-beam distance when a perpendicular arm is supplied, and assuming the hinge reaction has a known direction. Check torque units in $\mathrm{N\,m}$ and force results in $\mathrm N$.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
