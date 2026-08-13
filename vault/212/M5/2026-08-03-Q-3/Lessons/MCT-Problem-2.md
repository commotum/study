# Find Spring Speed and the Energy Split at a Displacement

<!--
lesson-id: 212-M5-060
topic-code: MTH212.M5.60
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Energy Ledger](#energy-ledger)
- [Source-Video Horizontal Spring and Lecture Supplement](#source-horizontal)
- [Source-Video Vertical Spring](#source-vertical)
- [Source-Video Spring Launch](#source-launch)
- [Source-Video Energy States from a Time Law](#source-time-law)
- [Summary](#summary)

## Prerequisites

- Measure spring displacement from the oscillator's equilibrium position.
- Use Hooke's law, $F=-kx$, and Newton's second law, $a=F/m$.
- Use $K=\tfrac12mv^2$ and $U=\tfrac12kx^2$.
- Solve a squared equation by taking a square root.
- Convert centimeters to meters before combining a displacement with $k$ in $\mathrm{N/m}$.

---

<a id="introduction"></a>
## Introduction

For an ideal spring oscillator with no nonconservative work, the amplitude fixes the total mechanical energy. At a specified displacement, part of that total is spring potential energy and the rest is kinetic energy.

The operational move is one subtraction:

$$
\boxed{E=\frac12kA^2},
\qquad
\boxed{U(x)=\frac12kx^2},
\qquad
\boxed{K(x)=E-U(x)}.
$$

Once $K$ is known, speed follows from $K=\tfrac12mv^2$. The restoring force and acceleration at that same position are

$$
F=-kx,
\qquad
a=-\frac{k}{m}x.
$$

The cues are a frictionless oscillator released from maximum stretch or compression, a request for a quantity "at $x$ from equilibrium," or a request for maximum speed, maximum acceleration, kinetic energy, potential energy, or total energy.

This lesson assumes an ideal undamped oscillator. Driving, damping, and resonance are outside this move.

---

<a id="energy-ledger"></a>
## Build the Energy Ledger

At a turning point, $|x|=A$ and $v=0$, so the total energy is

$$
E=\frac12kA^2.
$$

At a general position $x$, subtract the stored spring energy:

$$
\begin{aligned}
K(x)
&=\frac12kA^2-\frac12kx^2\\
&=\frac12k\left(A^2-x^2\right).
\end{aligned}
$$

Keep the two displacements in separate rows before substituting numbers:

| Ledger row | Displacement to use | Energy |
| --- | --- | ---: |
| Fixed total | amplitude $A$ | $E=\tfrac12kA^2$ |
| Stored now | current position $x$ | $U=\tfrac12kx^2$ |
| Moving now | subtract the rows | $K=\tfrac12k(A^2-x^2)$ |

This layout prevents the two common substitutions: using the current $x$ to set the total, or using the amplitude $A$ to compute the potential energy at an interior point.

Equating this remainder to $\tfrac12mv^2$ gives

$$
\boxed{v(x)=\pm\sqrt{\frac{k}{m}\left(A^2-x^2\right)}}.
$$

Solving the squared energy equation gives two algebraic signs. The radical itself is the speed; the velocity sign must come from the stated direction of motion. The displacement $x$ alone does not tell whether the mass is traveling left or right. A real speed also requires $|x|\le A$.

The radicand has the right units for speed squared:

$$
\left[\frac{k}{m}(A^2-x^2)\right]
=\frac{\mathrm{N/m}}{\mathrm{kg}}\,\mathrm{m^2}
=\mathrm{m^2/s^2}.
$$

Because $x$ is squared, $+x$ and $-x$ have the same $U$, $K$, and speed. Their restoring forces have opposite signs because $F=-kx$ is linear in $x$.

At equilibrium, $x=0$, so all the energy is kinetic:

$$
v_{\max}=A\sqrt{\frac{k}{m}}.
$$

At a turning point, the restoring acceleration has its largest magnitude:

$$
|a|_{\max}=\frac{kA}{m}.
$$

### Source-video scaling case — `iubb3eFBQ9U`, 00:32:28–00:34:57

The source holds $k$ and $m$ fixed and doubles the amplitude. The three scaling results are

$$
E\propto A^2,
\qquad
v_{\max}\propto A,
\qquad
|a|_{\max}\propto A.
$$

Therefore, doubling $A$ quadruples $E$ but only doubles $v_{\max}$ and $|a|_{\max}$.

```quiz
type: radio
id: mct-p2-amplitude-scaling
shuffle: true
content: |-
  An ideal mass–spring oscillator keeps the same $k$ and $m$, but its amplitude is reduced from $A$ to $A/2$. How do $E$, $v_{\max}$, and $|a|_{\max}$ change?
options:
- id: mct-p2-amplitude-scaling-a
  content: |-
    $E$ becomes $E/4$, while $v_{\max}$ and $|a|_{\max}$ each become one-half as large.
  correct: true
  feedback: |-
    Total energy contains $A^2$, so replacing $A$ by $A/2$ multiplies $E$ by $(1/2)^2=1/4$. Both $v_{\max}=A\sqrt{k/m}$ and $|a|_{\max}=kA/m$ are linear in $A$, so each is halved.
- id: mct-p2-amplitude-scaling-b
  content: |-
    All three quantities become one-half as large.
  feedback: |-
    This treats all three formulas as linear in amplitude. Maximum speed and acceleration are linear in $A$, but $E=\tfrac12kA^2$ is quadratic and falls to one-quarter.
- id: mct-p2-amplitude-scaling-c
  content: |-
    All three quantities become one-quarter as large.
  feedback: |-
    The one-quarter factor belongs only to the squared-amplitude energy. Neither $v_{\max}=A\sqrt{k/m}$ nor $|a|_{\max}=kA/m$ contains $A^2$.
- id: mct-p2-amplitude-scaling-d
  content: |-
    $E$ becomes $E/2$, while $v_{\max}$ and $|a|_{\max}$ each become one-quarter as large.
  feedback: |-
    The powers have been reversed. Energy is quadratic in $A$ and therefore gets the quarter factor; maximum speed and acceleration are linear and get the half factor.
- id: mct-p2-amplitude-scaling-e
  content: |-
    None of the three quantities changes because $k$ and $m$ are unchanged.
  feedback: |-
    Holding $k$ and $m$ fixed does not hold the motion's energy or extrema fixed. Each relevant formula still contains the changed amplitude $A$.
```

---

<a id="source-horizontal"></a>
## Source-Video Horizontal Spring and Lecture Supplement

### Source-video worked case — `iubb3eFBQ9U`, 00:35:03–00:42:22

The frame shows

$$
k=300\ \mathrm{N/m},
\qquad
m=0.40\ \mathrm{kg},
\qquad
A=0.30\ \mathrm m.
$$

The maximum speed and acceleration magnitude are

$$
v_{\max}
=A\sqrt{\frac{k}{m}}
=(0.30)\sqrt{\frac{300}{0.40}}
=8.22\ \mathrm{m/s},
$$

$$
|a|_{\max}
=\frac{kA}{m}
=\frac{(300)(0.30)}{0.40}
=225\ \mathrm{m/s^2}.
$$

At $x=+0.20\ \mathrm m$, the ledger gives

$$
\begin{aligned}
E&=\frac12(300)(0.30)^2=13.5\ \mathrm J,\\
U&=\frac12(300)(0.20)^2=6.00\ \mathrm J,\\
K&=13.5-6.00=7.50\ \mathrm J.
\end{aligned}
$$

Thus the speed is

$$
|v|=\sqrt{\frac{2K}{m}}
=\sqrt{\frac{2(7.50)}{0.40}}
=6.12\ \mathrm{m/s}.
$$

The source asks for speed, so $6.12\ \mathrm{m/s}$ is sufficient. If velocity were requested, its sign would depend on whether the block was moving toward or away from equilibrium. At this positive displacement,

$$
F=-kx=-(300)(0.20)=-60\ \mathrm N,
$$

$$
a=\frac{F}{m}=\frac{-60}{0.40}=-150\ \mathrm{m/s^2}.
$$

**Frame correction.** The automatic captions drop the decimal and repeatedly render the mass as $4\ \mathrm{kg}$. The displayed problem and the arithmetic use $0.40\ \mathrm{kg}$. The captions also omit the minus sign while first stating the direct acceleration formula; the completed source solution repairs it to $a=-kx/m$.

### M4-1 lecture supplement: maximum speed by endpoint energy

The paired lecture uses $m=0.86\ \mathrm{kg}$, $k=78\ \mathrm{N/m}$, and $A=0.92\ \mathrm m$. Equating the turning-point energy with the equilibrium kinetic energy gives

$$
\frac12kA^2=\frac12mv_{\max}^2,
$$

$$
v_{\max}=A\sqrt{\frac{k}{m}}
=(0.92)\sqrt{\frac{78}{0.86}}
=8.8\ \mathrm{m/s}.
$$

This is the same energy ledger evaluated at $x=0$, not a separate method.

```quiz
type: radio
id: mct-p2-horizontal-ledger
shuffle: true
content: |-
  A $0.50\ \mathrm{kg}$ block on a frictionless horizontal surface is attached to a spring with $k=180\ \mathrm{N/m}$. It is released from $A=0.25\ \mathrm m$. Later it is at $x=-0.15\ \mathrm m$ and moving right. Which set is correct?
options:
- id: mct-p2-horizontal-ledger-a
  content: |-
    $K=3.60\ \mathrm J$, $v=+3.79\ \mathrm{m/s}$, and $F=+27.0\ \mathrm N$
  correct: true
  feedback: |-
    The ledger gives $K=\tfrac12(180)[(0.25)^2-(0.15)^2]=3.60\ \mathrm J$, so $|v|=\sqrt{2K/0.50}=3.79\ \mathrm{m/s}$. The block is moving right, making $v$ positive, and $F=-kx=-180(-0.15)=+27.0\ \mathrm N$.
- id: mct-p2-horizontal-ledger-b
  content: |-
    $K=2.03\ \mathrm J$, $v=+2.85\ \mathrm{m/s}$, and $F=+27.0\ \mathrm N$
  feedback: |-
    The value $2.03\ \mathrm J$ is $U=\tfrac12kx^2$, not the kinetic remainder. Subtract it from $E=\tfrac12kA^2=5.625\ \mathrm J$ before using $K=\tfrac12mv^2$.
- id: mct-p2-horizontal-ledger-c
  content: |-
    $K=5.63\ \mathrm J$, $v=+4.74\ \mathrm{m/s}$, and $F=+27.0\ \mathrm N$
  feedback: |-
    The value $5.63\ \mathrm J$ is the total energy. At $x=-0.15\ \mathrm m$, some of that total remains potential, so using all of $E$ as kinetic overstates the speed.
- id: mct-p2-horizontal-ledger-d
  content: |-
    $K=3.60\ \mathrm J$, $v=-3.79\ \mathrm{m/s}$, and $F=+27.0\ \mathrm N$
  feedback: |-
    The energy and force are correct, but the velocity sign contradicts the stated motion. The square-root calculation gives the magnitude; "moving right" selects the positive sign.
- id: mct-p2-horizontal-ledger-e
  content: |-
    $K=3.60\ \mathrm J$, $v=+3.79\ \mathrm{m/s}$, and $F=-27.0\ \mathrm N$
  feedback: |-
    The restoring force has the sign opposite $x$. Because the block is left of equilibrium at $x=-0.15\ \mathrm m$, $F=-kx$ points right and is positive.
```

---

<a id="source-vertical"></a>
## Source-Video Vertical Spring

### Source-video worked case — `iubb3eFBQ9U`, 00:42:25–00:51:16

A $2.0\ \mathrm{kg}$ mass first stretches a vertical spring by

$$
\Delta_{\mathrm{eq}}=0.40\ \mathrm m.
$$

Static balance at the new equilibrium determines the spring constant:

$$
k\Delta_{\mathrm{eq}}=mg,
$$

$$
k=\frac{mg}{\Delta_{\mathrm{eq}}}
=\frac{(2.0)(9.8)}{0.40}
=49\ \mathrm{N/m}.
$$

The mass is then pulled an additional $0.20\ \mathrm m$ from that shifted equilibrium and released. Therefore,

$$
A=0.20\ \mathrm m,
$$

not $0.40\ \mathrm m$ and not $0.60\ \mathrm m$. The equilibrium stretch finds $k$; the additional release displacement is the oscillation amplitude.

The source obtains

$$
|a|_{\max}=\frac{kA}{m}=4.9\ \mathrm{m/s^2},
$$

$$
v_{\max}=A\sqrt{\frac{k}{m}}=0.99\ \mathrm{m/s}.
$$

At $x=0.10\ \mathrm m$ from the shifted equilibrium,

$$
\begin{aligned}
E&=\frac12(49)(0.20)^2=0.980\ \mathrm J,\\
U&=\frac12(49)(0.10)^2=0.245\ \mathrm J,\\
K&=0.980-0.245=0.735\ \mathrm J.
\end{aligned}
$$

This corresponds to $|v|=0.857\ \mathrm{m/s}$.

**Coordinate correction.** For the vertical oscillator, $x$ in the compact ledger is measured from the gravity-shifted equilibrium, not from the spring's natural length. In that shifted coordinate, the changing spring and gravitational potential energies combine to $\tfrac12kx^2$ plus a constant. Using the total stretch from the natural length inside $\tfrac12kx^2$ while omitting gravitational potential would mix two energy references.

```quiz
type: radio
id: mct-p2-vertical-equilibrium
shuffle: true
content: |-
  A $1.5\ \mathrm{kg}$ mass stretches a vertical spring $0.30\ \mathrm m$ to its equilibrium position. It is pulled an additional $0.12\ \mathrm m$ downward and released. Take $g=9.8\ \mathrm{m/s^2}$. At $x=+0.05\ \mathrm m$ from the shifted equilibrium, which setup and result are correct?
options:
- id: mct-p2-vertical-equilibrium-a
  content: |-
    $k=49\ \mathrm{N/m}$, $A=0.12\ \mathrm m$, $K=0.292\ \mathrm J$, and $|v|=0.623\ \mathrm{m/s}$
  correct: true
  feedback: |-
    Static stretch gives $k=mg/0.30=49\ \mathrm{N/m}$, while the additional pull gives $A=0.12\ \mathrm m$. Then $K=\tfrac12k(A^2-x^2)=0.29155\ \mathrm J$ and $|v|=\sqrt{2K/m}=0.623\ \mathrm{m/s}$.
- id: mct-p2-vertical-equilibrium-b
  content: |-
    $k=122.5\ \mathrm{N/m}$, $A=0.30\ \mathrm m$, $K=5.36\ \mathrm J$, and $|v|=2.67\ \mathrm{m/s}$
  feedback: |-
    This uses the additional $0.12\ \mathrm m$ pull to infer $k$ and the equilibrium stretch as the amplitude. Those lengths have different roles: $0.30\ \mathrm m$ balances the weight, while $0.12\ \mathrm m$ is measured from equilibrium at release.
- id: mct-p2-vertical-equilibrium-c
  content: |-
    $k=49\ \mathrm{N/m}$, $A=0.30\ \mathrm m$, $K=2.14\ \mathrm J$, and $|v|=1.69\ \mathrm{m/s}$
  feedback: |-
    The spring constant is correct, but $0.30\ \mathrm m$ is the equilibrium stretch from natural length, not the oscillator's amplitude. The amplitude is the additional $0.12\ \mathrm m$ release displacement.
- id: mct-p2-vertical-equilibrium-d
  content: |-
    $k=49\ \mathrm{N/m}$, $A=0.12\ \mathrm m$, and $K=\tfrac12k[(0.12)^2-(0.35)^2]<0$
  feedback: |-
    The $0.35\ \mathrm m$ total stretch from natural length cannot replace $x=0.05\ \mathrm m$ in the shifted-coordinate ledger. The negative result is also a warning: a valid oscillator position must satisfy $|x|\le A$ and therefore $K\ge0$.
- id: mct-p2-vertical-equilibrium-e
  content: |-
    $k=49\ \mathrm{N/m}$, $A=0.42\ \mathrm m$, $K=4.26\ \mathrm J$, and $|v|=2.38\ \mathrm{m/s}$
  feedback: |-
    Adding the equilibrium stretch and the additional pull gives the total extension from natural length, not amplitude about equilibrium. Gravity shifts the equilibrium; the oscillation extends only $0.12\ \mathrm m$ to either side of that point.
```

---

<a id="source-launch"></a>
## Source-Video Spring Launch

### Source-video worked case — `iubb3eFBQ9U`, 00:51:16–00:58:11

A spring is held $0.35\ \mathrm m$ compressed against a $0.25\ \mathrm{kg}$ block by a $500\ \mathrm N$ applied force. At maximum compression,

$$
k=\frac{F_{\max}}{A}
=\frac{500}{0.35}
=1429\ \mathrm{N/m}.
$$

When the spring returns to its natural length and the unattached block loses contact, the spring energy has become kinetic energy:

$$
K=\frac12kA^2
=\frac12(1429)(0.35)^2
=87.5\ \mathrm J.
$$

Therefore,

$$
v=\sqrt{\frac{2K}{m}}
=\sqrt{\frac{2(87.5)}{0.25}}
=26.5\ \mathrm{m/s}.
$$

The source also checks this with the force-displacement graph. Because the force magnitude obeys $|F|=k|x|$, it falls linearly from $500\ \mathrm N$ to zero. Its work is the triangular area

$$
W=\frac12(0.35\ \mathrm m)(500\ \mathrm N)=87.5\ \mathrm J.
$$

The factor $1/2$ comes from the area under a linearly varying force, or equivalently from its average value of $250\ \mathrm N$. Using $F_{\max}A$ would incorrectly treat the force as constant.

**Wording correction.** At the literal instant the holding force is removed, the block starts from rest. The source's requested "release speed" is the speed when the spring reaches its natural length and ceases to push the unattached block.

```quiz
type: radio
id: mct-p2-launch-area
shuffle: true
content: |-
  A $0.32\ \mathrm{kg}$ block is held against a spring compressed $0.24\ \mathrm m$. The required holding force at that compression is $360\ \mathrm N$. On a frictionless surface, what kinetic energy and speed does the block have when the spring reaches natural length and loses contact?
options:
- id: mct-p2-launch-area-a
  content: |-
    $K=43.2\ \mathrm J$ and $v=16.4\ \mathrm{m/s}$
  correct: true
  feedback: |-
    The spring force falls linearly from $360\ \mathrm N$ to zero, so its work is the triangular area $K=\tfrac12(0.24)(360)=43.2\ \mathrm J$. Then $v=\sqrt{2K/0.32}=16.4\ \mathrm{m/s}$.
- id: mct-p2-launch-area-b
  content: |-
    $K=86.4\ \mathrm J$ and $v=23.2\ \mathrm{m/s}$
  feedback: |-
    This uses $F_{\max}A$ as though the spring exerted $360\ \mathrm N$ throughout the motion. Hooke's-law force decreases to zero, so the force-displacement area is a triangle and needs the factor $1/2$.
- id: mct-p2-launch-area-c
  content: |-
    $K=43.2\ \mathrm J$ and $v=11.6\ \mathrm{m/s}$
  feedback: |-
    The energy is correct, but $11.6\ \mathrm{m/s}$ comes from $v=\sqrt{K/m}$. Since $K=\tfrac12mv^2$, solving for speed requires $v=\sqrt{2K/m}$.
- id: mct-p2-launch-area-d
  content: |-
    $K=0$ and $v=0$ because the block is released from rest.
  feedback: |-
    The block is indeed at rest when the holder first lets go, but the question asks for the later state at natural length. During that motion, $43.2\ \mathrm J$ of spring energy becomes kinetic energy.
- id: mct-p2-launch-area-e
  content: |-
    $K=360\ \mathrm J$ and $v=47.4\ \mathrm{m/s}$
  feedback: |-
    A force measured in newtons is not an energy measured in joules. Energy is the area under the force-displacement graph: $\tfrac12F_{\max}A$, with the displacement in meters.
```

---

<a id="source-time-law"></a>
## Source-Video Energy States from a Time Law

### Source-video worked case — `iubb3eFBQ9U`, 01:33:54–01:43:35

The displayed source data are

$$
m=0.75\ \mathrm{kg},
\qquad
x(t)=0.60\cos(9.2t)\ \mathrm m.
$$

For this handoff only, read $A=0.60\ \mathrm m$ and $\omega=9.2\ \mathrm{rad/s}$. Since $\omega^2=k/m$,

$$
k=m\omega^2
=(0.75)(9.2)^2
=63.5\ \mathrm{N/m}.
$$

The energy ledger then gives

$$
E=\frac12kA^2
=\frac12(63.48)(0.60)^2
=11.42\ \mathrm J.
$$

The source compares three positions:

| Position | Spring potential energy $U$ | Kinetic energy $K$ |
| --- | ---: | ---: |
| $x=0$ | $0$ | $11.42\ \mathrm J$ |
| $x=0.20\ \mathrm m$ | $1.27\ \mathrm J$ | $10.15\ \mathrm J$ |
| $x=0.60\ \mathrm m$ | $11.42\ \mathrm J$ | $0$ |

At $x=0.20\ \mathrm m$ specifically,

$$
U=\frac12(63.48)(0.20)^2=1.27\ \mathrm J,
$$

$$
K=11.42-1.27=10.15\ \mathrm J.
$$

At $x=0$, the oscillator is fastest. At $|x|=A=0.60\ \mathrm m$, it is momentarily at rest. Energy depends on $x^2$, so the split at $x=-0.20\ \mathrm m$ is the same as at $x=+0.20\ \mathrm m$, even though force and acceleration reverse direction.

**Frame correction.** The automatic captions suppress decimal points, rendering the data as $75\ \mathrm{kg}$, amplitude $6\ \mathrm m$, and intermediate position $2\ \mathrm m$. The problem frame confirms $0.75\ \mathrm{kg}$, $0.60\ \mathrm m$, and $0.20\ \mathrm m$; the displayed numerical results also require those values.

```quiz
type: radio
id: mct-p2-time-law-handoff
shuffle: true
content: |-
  A $0.80\ \mathrm{kg}$ oscillator follows $x(t)=0.45\cos(8.0t)\ \mathrm m$. At an instant when $x=-0.15\ \mathrm m$, which statement is correct?
options:
- id: mct-p2-time-law-handoff-a
  content: |-
    $k=51.2\ \mathrm{N/m}$, $U=0.576\ \mathrm J$, $K=4.61\ \mathrm J$, and $|v|=3.39\ \mathrm{m/s}$; the sign of $v$ needs separate direction information.
  correct: true
  feedback: |-
    Here $A=0.45\ \mathrm m$ and $\omega=8.0\ \mathrm{rad/s}$, so $k=m\omega^2=51.2\ \mathrm{N/m}$ and $E=\tfrac12kA^2=5.184\ \mathrm J$. At $|x|=0.15\ \mathrm m$, $U=0.576\ \mathrm J$, $K=4.608\ \mathrm J$, and $|v|=\sqrt{2K/m}=3.39\ \mathrm{m/s}$.
- id: mct-p2-time-law-handoff-b
  content: |-
    $k=51.2\ \mathrm{N/m}$, $U=4.61\ \mathrm J$, $K=0.576\ \mathrm J$, and $|v|=1.20\ \mathrm{m/s}$.
  feedback: |-
    This reverses the potential and kinetic parts. Spring potential uses the current displacement, $U=\tfrac12kx^2=0.576\ \mathrm J$; the larger remainder of the $5.184\ \mathrm J$ total is kinetic.
- id: mct-p2-time-law-handoff-c
  content: |-
    $k=51.2\ \mathrm{N/m}$, $E=0.576\ \mathrm J$, and $K=0$ because $|x|=0.15\ \mathrm m$ is the amplitude.
  feedback: |-
    The amplitude is the coefficient of cosine, $A=0.45\ \mathrm m$, not the position in this snapshot. Since $|x|<A$, the oscillator is between equilibrium and a turning point and has nonzero kinetic energy.
- id: mct-p2-time-law-handoff-d
  content: |-
    $k=6.4\ \mathrm{N/m}$, $U=0.072\ \mathrm J$, $K=0.576\ \mathrm J$, and $|v|=1.20\ \mathrm{m/s}$.
  feedback: |-
    This uses $k=m\omega$ instead of $k=m\omega^2$. The mass–spring relation is $\omega^2=k/m$, so the angular frequency must be squared before building the energy ledger.
- id: mct-p2-time-law-handoff-e
  content: |-
    $k=51.2\ \mathrm{N/m}$, $U=0.576\ \mathrm J$, $K=4.61\ \mathrm J$, and $v=+3.39\ \mathrm{m/s}$ because $x<0$.
  feedback: |-
    The energy values and speed magnitude are correct, but negative displacement does not determine the direction of motion. The oscillator passes the same position once moving left and once moving right; a phase or direction statement is needed to choose the sign of $v$.
```

---

<a id="summary"></a>
## Summary

For an ideal spring oscillator released from amplitude $A$:

1. Set the fixed total energy with $E=\tfrac12kA^2$.
2. At the requested displacement from equilibrium, compute $U=\tfrac12kx^2$.
3. Subtract to get $K=E-U=\tfrac12k(A^2-x^2)$.
4. Use $|v|=\sqrt{2K/m}$. Choose the sign of $v$ from the direction of motion, not from $x$.
5. At that same position, use $F=-kx$ and $a=-kx/m$.

The endpoint checks are

$$
x=0:\quad U=0,\ K=E,\ |v|=v_{\max},
$$

$$
|x|=A:\quad U=E,\ K=0,\ v=0.
$$

For a vertical spring, measure the oscillation coordinate from the shifted equilibrium. Use the static equilibrium stretch to find $k$, but use the additional release displacement as $A$. For a launch by an unattached spring, the energy delivered by a linearly decreasing force is the triangular area under the force-displacement graph.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
