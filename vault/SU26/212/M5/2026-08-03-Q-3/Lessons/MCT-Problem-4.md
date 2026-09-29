# Translate an SHM State into $x(t)$, $v(t)$, and $a(t)$

<!--
lesson-id: 212-M5-062
topic-code: MTH212.M5.62
-->

## Table of Contents

- [Introduction](#introduction)
- [Source-Video Worked Problem: Read an SHM Position Function](#source-read-function)
- [Source-Video Worked Problem: Differentiate Without Changing Phase](#source-differentiate)
- [Source Correction: Separate “At Time” from “At Position”](#source-time-vs-position)
- [Source-Video Worked Problem: Choose the Initial Phase](#source-initial-phase)
- [Lecture Application: Measure from Equilibrium](#lecture-equilibrium)
- [Summary](#summary)

## Prerequisites

- Recognize the basic sine and cosine values at phase $0$.
- Differentiate sine and cosine using the chain rule.
- Convert between angular frequency, frequency, and period.
- Use $\omega=\sqrt{k/m}$ for an ideal mass–spring oscillator.
- Interpret the signs of position and velocity on a chosen axis.

---

<a id="introduction"></a>
## Introduction

An ideal simple harmonic oscillator can be written as

$$
x(t)=A\cos(\omega t+\phi),
$$

where $x$ is measured from equilibrium, $A$ is the amplitude, $\omega$ is the angular frequency, and $\phi$ fixes the state at $t=0$. The argument $\omega t+\phi$ is a phase measured in radians.

Once the position function is fixed, differentiate it without changing that phase argument:

$$
\boxed{
\begin{aligned}
x(t)&=A\cos(\omega t+\phi),\\
v(t)&=-A\omega\sin(\omega t+\phi),\\
a(t)&=-A\omega^2\cos(\omega t+\phi)
      =-\omega^2x(t).
\end{aligned}}
$$

The chain rule contributes one factor of $\omega$ to $v$ and a second factor to $a$:

| Quantity | Outer function | Coefficient | Phase argument |
|---|---|---|---|
| $x$ | $\cos$ | $A$ | $\omega t+\phi$ |
| $v$ | $-\sin$ | $A\omega$ | $\omega t+\phi$ |
| $a$ | $-\cos$ | $A\omega^2$ | $\omega t+\phi$ |

Only the outer function and coefficient change under differentiation; the phase argument is copied intact.

The restoring relation $a=-\omega^2x$ also gives

$$
F=ma=-m\omega^2x=-kx.
$$

Use this order:

1. Define the positive axis and measure $x$ from equilibrium.
2. Read or calculate $A$ and $\omega$.
3. Choose sine, cosine, and the leading sign from the initial state.
4. Differentiate while keeping the phase argument intact.
5. Decide whether the requested condition is a time $t$ or a position $x$ before substituting.

---

<a id="source-read-function"></a>
## Source-Video Worked Problem: Read an SHM Position Function

The frame-verified problem in `iubb3eFBQ9U` at 1:33:54-1:37:02 gives

$$
m=0.75\,\mathrm{kg},
\qquad
x(t)=0.60\cos(9.2t)\,\mathrm m.
$$

Match the function to $A\cos(\omega t)$:

$$
A=\boxed{0.60\,\mathrm m},
\qquad
\omega=\boxed{9.2\,\mathrm{rad/s}}.
$$

The coefficient of $t$ is angular frequency, not ordinary frequency. Therefore,

$$
f=\frac{\omega}{2\pi}
=\frac{9.2}{2\pi}
=\boxed{1.464\,\mathrm{Hz}},
$$

and

$$
T=\frac1f
=\boxed{0.683\,\mathrm s}.
$$

For a mass–spring oscillator, $\omega^2=k/m$, so

$$
k=m\omega^2
=(0.75)(9.2)^2
=63.48\,\mathrm{N/m}
\approx\boxed{63.5\,\mathrm{N/m}}.
$$

The source continues into oscillator energy, which belongs to the energy-state lesson. Here the time law supplies only $A$, $\omega$, $f$, $T$, and $k$.

```quiz
type: radio
id: mct-p4-read-time-law
shuffle: true
content: |-
  A $0.50\,\mathrm{kg}$ block follows $x(t)=0.35\cos(8.0t)\,\mathrm m$. Which set of oscillator values is correct?
options:
- id: mct-p4-read-time-law-a
  content: |-
    $A=0.35\,\mathrm m$, $f=1.27\,\mathrm{Hz}$, $T=0.785\,\mathrm s$, and $k=32\,\mathrm{N/m}$
  correct: true
  feedback: |-
    The cosine coefficient is $A=0.35\,\mathrm m$, while the coefficient of $t$ is $\omega=8.0\,\mathrm{rad/s}$. Thus $f=\omega/(2\pi)=1.27\,\mathrm{Hz}$, $T=1/f=0.785\,\mathrm s$, and $k=m\omega^2=32\,\mathrm{N/m}$.
- id: mct-p4-read-time-law-b
  content: |-
    $A=0.35\,\mathrm m$, $f=8.0\,\mathrm{Hz}$, $T=0.125\,\mathrm s$, and $k=32\,\mathrm{N/m}$
  feedback: |-
    The coefficient $8.0$ is angular frequency in radians per second, not cycles per second. Divide it by $2\pi$ to obtain $f$, then invert $f$ for the period.
- id: mct-p4-read-time-law-c
  content: |-
    $A=0.70\,\mathrm m$, $f=1.27\,\mathrm{Hz}$, $T=0.785\,\mathrm s$, and $k=32\,\mathrm{N/m}$
  feedback: |-
    The peak-to-peak span is $2A=0.70\,\mathrm m$, but amplitude is the maximum displacement from equilibrium. The coefficient of cosine gives $A=0.35\,\mathrm m$.
- id: mct-p4-read-time-law-d
  content: |-
    $A=0.35\,\mathrm m$, $f=1.27\,\mathrm{Hz}$, $T=0.785\,\mathrm s$, and $k=4.0\,\mathrm{N/m}$
  feedback: |-
    This uses $k=m\omega$. The mass–spring relation is $\omega^2=k/m$, so isolating stiffness gives $k=m\omega^2=(0.50)(8.0)^2=32\,\mathrm{N/m}$.
- id: mct-p4-read-time-law-e
  content: |-
    $A=0.35\,\mathrm m$, $f=0.125\,\mathrm{Hz}$, $T=8.0\,\mathrm s$, and $k=32\,\mathrm{N/m}$
  feedback: |-
    This treats angular frequency as a period. The phase $8.0t$ advances $8.0$ radians each second; one $2\pi$-radian cycle takes $T=2\pi/8.0=0.785\,\mathrm s$.
```

---

<a id="source-differentiate"></a>
## Source-Video Worked Problem: Differentiate Without Changing Phase

The next frame-verified problem in `iubb3eFBQ9U` at 1:43:43-1:49:07 gives

$$
m=0.55\,\mathrm{kg},
\qquad
x(t)=1.5\cos(12.4t)\,\mathrm m.
$$

Here $A=1.5\,\mathrm m$ and $\omega=12.4\,\mathrm{rad/s}$. Differentiate once:

$$
\begin{aligned}
v(t)
&=\frac{dx}{dt}\\
&=-1.5(12.4)\sin(12.4t)\\
&=\boxed{-18.6\sin(12.4t)\,\mathrm{m/s}}.
\end{aligned}
$$

Differentiate again:

$$
\begin{aligned}
a(t)
&=-18.6(12.4)\cos(12.4t)\\
&=\boxed{-230.64\cos(12.4t)\,\mathrm{m/s^2}}.
\end{aligned}
$$

The same angular frequency gives the spring constant directly:

$$
k=m\omega^2
=(0.55)(12.4)^2
=\boxed{84.568\,\mathrm{N/m}}.
$$

Three checks expose common derivative errors:

- The phase argument remains $12.4t$ in all three functions.
- The velocity amplitude is $A\omega=18.6\,\mathrm{m/s}$.
- The acceleration always points toward equilibrium because $a=-\omega^2x$.

```quiz
type: radio
id: mct-p4-differentiate-time-law
shuffle: true
content: |-
  An oscillator has $x(t)=0.40\sin(5.0t)\,\mathrm m$. Which pair gives its velocity and acceleration functions?
options:
- id: mct-p4-differentiate-time-law-a
  content: |-
    $v(t)=2.0\cos(5.0t)\,\mathrm{m/s}$ and $a(t)=-10.0\sin(5.0t)\,\mathrm{m/s^2}$
  correct: true
  feedback: |-
    Differentiating sine gives cosine and the chain rule contributes $5.0$; differentiating again contributes another $5.0$ and a minus sign. The original phase $5.0t$ stays unchanged.
- id: mct-p4-differentiate-time-law-b
  content: |-
    $v(t)=-2.0\cos(5.0t)\,\mathrm{m/s}$ and $a(t)=10.0\sin(5.0t)\,\mathrm{m/s^2}$
  feedback: |-
    The derivative of sine is positive cosine, so the first derivative does not acquire a minus sign. The restoring acceleration does: $a=-\omega^2x=-10.0\sin(5.0t)$.
- id: mct-p4-differentiate-time-law-c
  content: |-
    $v(t)=0.40\cos(5.0t)\,\mathrm{m/s}$ and $a(t)=-0.40\sin(5.0t)\,\mathrm{m/s^2}$
  feedback: |-
    This changes the trig functions but omits the chain-rule factors. Each differentiation of a function with phase $5.0t$ contributes a factor of $5.0$.
- id: mct-p4-differentiate-time-law-d
  content: |-
    $v(t)=2.0\cos(5.0t)\,\mathrm{m/s}$ and $a(t)=-2.0\sin(5.0t)\,\mathrm{m/s^2}$
  feedback: |-
    The velocity is correct, but the second derivative needs a second factor of $5.0$. Acceleration amplitude is $A\omega^2=(0.40)(5.0)^2=10.0\,\mathrm{m/s^2}$.
- id: mct-p4-differentiate-time-law-e
  content: |-
    $v(t)=2.0\cos(t)\,\mathrm{m/s}$ and $a(t)=-10.0\sin(t)\,\mathrm{m/s^2}$
  feedback: |-
    Differentiation changes the outer trig function and coefficient, not the inner phase. The argument must remain $5.0t$ in both derivatives.
```

---

<a id="source-time-vs-position"></a>
## Source Correction: Separate “At Time” from “At Position”

The displayed prompt for the $1.5\cos(12.4t)$ problem asks for the state at

$$
x=0.5\,\mathrm m,
$$

but the narration at 1:49:14-1:51:16 substitutes

$$
t=0.5\,\mathrm s.
$$

Those are different conditions and cannot be exchanged.

### If the intended condition is $t=0.5\,\mathrm s$

Evaluate the time functions in radian mode because $\omega t$ is in radians:

$$
\begin{aligned}
v(0.5)
&=-18.6\sin[12.4(0.5)]\\
&\approx\boxed{+1.545\,\mathrm{m/s}},\\[4pt]
a(0.5)
&=-230.64\cos[12.4(0.5)]\\
&\approx\boxed{-229.84\,\mathrm{m/s^2}},\\[4pt]
F(0.5)
&=ma\\
&\approx\boxed{-126.4\,\mathrm N}.
\end{aligned}
$$

These are the source's narrated numerical results. At this time the position is actually

$$
x(0.5)=1.5\cos(6.2)\approx1.495\,\mathrm m,
$$

not $0.5\,\mathrm m$.

### If the displayed condition $x=0.5\,\mathrm m$ is used literally

Position fixes acceleration and force without finding a time:

$$
a=-\omega^2x
=-(12.4)^2(0.5)
=\boxed{-76.88\,\mathrm{m/s^2}},
$$

$$
F=-kx
=-(84.568)(0.5)
=\boxed{-42.28\,\mathrm N}.
$$

The speed at a position follows from the SHM identity

$$
v^2=\omega^2(A^2-x^2).
$$

$$
|v|
=12.4\sqrt{1.5^2-0.5^2}
\approx\boxed{17.54\,\mathrm{m/s}}.
$$

The oscillator passes through $x=0.5\,\mathrm m$ twice per cycle, once in each direction. Position alone therefore gives $v=\pm17.54\,\mathrm{m/s}$; a direction or a time is needed to choose its sign.

```quiz
type: radio
id: mct-p4-at-position
shuffle: true
content: |-
  A $0.40\,\mathrm{kg}$ oscillator follows $x(t)=1.2\cos(6.0t)\,\mathrm m$. What can be concluded when the oscillator is at $x=+0.30\,\mathrm m$?
options:
- id: mct-p4-at-position-a
  content: |-
    $a=-10.8\,\mathrm{m/s^2}$, $F=-4.32\,\mathrm N$, and $v=\pm6.97\,\mathrm{m/s}$ depending on direction
  correct: true
  feedback: |-
    Position fixes the restoring quantities: $a=-\omega^2x=-(6.0)^2(0.30)=-10.8\,\mathrm{m/s^2}$ and $F=ma=-4.32\,\mathrm N$. It fixes speed through $|v|=\omega\sqrt{A^2-x^2}=6.97\,\mathrm{m/s}$, but not the velocity sign.
- id: mct-p4-at-position-b
  content: |-
    $a=-10.8\,\mathrm{m/s^2}$, $F=-4.32\,\mathrm N$, and $v=+6.97\,\mathrm{m/s}$
  feedback: |-
    The acceleration and force are correct, but $x=+0.30\,\mathrm m$ occurs once while moving positive and once while moving negative. Position alone fixes $|v|$, not the sign of $v$.
- id: mct-p4-at-position-c
  content: |-
    $a=+10.8\,\mathrm{m/s^2}$, $F=+4.32\,\mathrm N$, and $v=\pm6.97\,\mathrm{m/s}$
  feedback: |-
    A positive displacement lies on the positive side of equilibrium, so the restoring acceleration and force point in the negative direction: $a=-\omega^2x$ and $F=-kx$.
- id: mct-p4-at-position-d
  content: |-
    $a=+9.82\,\mathrm{m/s^2}$, $F=+3.93\,\mathrm N$, and $v=-7.01\,\mathrm{m/s}$
  feedback: |-
    These values come from substituting $t=0.30\,\mathrm s$ into the time functions. The prompt specifies the position $x=0.30\,\mathrm m$, not the time $t=0.30\,\mathrm s$.
- id: mct-p4-at-position-e
  content: |-
    Only the velocity is determined; acceleration and force require the time
  feedback: |-
    The roles are reversed. In SHM, $a=-\omega^2x$ and $F=-kx$, so position determines acceleration and force directly; the direction of travel is what position alone cannot distinguish.
```

---

<a id="source-initial-phase"></a>
## Source-Video Worked Problem: Choose the Initial Phase

The source problem in `iubb3eFBQ9U` at 1:51:24-1:58:00 gives

$$
k=300\,\mathrm{N/m},
\qquad
m=0.35\,\mathrm{kg},
\qquad
A=0.45\,\mathrm m.
$$

First calculate the angular frequency:

$$
\omega=\sqrt{\frac{k}{m}}
=\sqrt{\frac{300}{0.35}}
=29.277\ldots\,\mathrm{rad/s}
\approx\boxed{29.28\,\mathrm{rad/s}}.
$$

For an axis on which upward or rightward is positive, the four zero-phase starting states are:

| State at $t=0$ | Position function |
|---|---|
| $x(0)=+A$, released from the positive turning point | $x(t)=+A\cos(\omega t)$ |
| $x(0)=0$, crossing with $v(0)=+A\omega$ | $x(t)=+A\sin(\omega t)$ |
| $x(0)=-A$, released from the negative turning point | $x(t)=-A\cos(\omega t)$ |
| $x(0)=0$, crossing with $v(0)=-A\omega$ | $x(t)=-A\sin(\omega t)$ |

After choosing a row, substitute $t=0$ into both $x(t)$ and $v(t)$. This check is safer than relying on words such as “top” or “bottom” unless the positive axis has been stated.

The source first asks for a mass crossing equilibrium with positive velocity. Its initial position is zero and its initial slope is positive, so

$$
\boxed{x(t)=0.45\sin(29.28t)\,\mathrm m}.
$$

The controlled source variant starts at the lowest point, which is $x(0)=-A$ under the source's upward-positive convention. Therefore,

$$
\boxed{x(t)=-0.45\cos(29.28t)\,\mathrm m}.
$$

**Source correction.** At a turning point the instantaneous velocity is zero. From the lowest point, the positive acceleration makes the mass move upward immediately after release; it does not have positive velocity at the exact release instant. The negative sign in the second position function is required by $x(0)=-0.45\,\mathrm m$, even though the closing captions omit it.

```quiz
type: radio
id: mct-p4-initial-state
shuffle: true
content: |-
  An oscillator has amplitude $0.22\,\mathrm m$ and angular frequency $10\,\mathrm{rad/s}$. At $t=0$ it crosses equilibrium with velocity in the negative direction. Which position function matches this state?
options:
- id: mct-p4-initial-state-a
  content: |-
    $x(t)=-0.22\sin(10t)\,\mathrm m$
  correct: true
  feedback: |-
    Crossing equilibrium requires a sine form because $x(0)=0$. Its derivative is $v(t)=-2.2\cos(10t)$, so $v(0)=-2.2\,\mathrm{m/s}$ matches the stated negative direction.
- id: mct-p4-initial-state-b
  content: |-
    $x(t)=+0.22\sin(10t)\,\mathrm m$
  feedback: |-
    This starts at equilibrium, but $v(0)=+2.2\,\mathrm{m/s}$. It represents a crossing in the positive direction rather than the stated negative direction.
- id: mct-p4-initial-state-c
  content: |-
    $x(t)=+0.22\cos(10t)\,\mathrm m$
  feedback: |-
    Positive cosine starts at $x(0)=+A$, a turning point with zero velocity. The prompt places the mass at equilibrium with nonzero velocity.
- id: mct-p4-initial-state-d
  content: |-
    $x(t)=-0.22\cos(10t)\,\mathrm m$
  feedback: |-
    Negative cosine starts at $x(0)=-A$, also a turning point with zero velocity. Use a sine form for an equilibrium crossing.
- id: mct-p4-initial-state-e
  content: |-
    $x(t)=-0.22\sin(t)\,\mathrm m$
  feedback: |-
    The sign and sine family match the initial state, but the phase must advance at the given angular frequency. The argument is $10t$, not $t$.
```

---

<a id="lecture-equilibrium"></a>
## Lecture Application: Measure from Equilibrium

The M4-1 lecture uses an equilibrium coordinate and a release coordinate:

$$
X_{\mathrm{eq}}=0.35\,\mathrm m,
\qquad
X_{\mathrm{release}}=0.48\,\mathrm m.
$$

The SHM function uses displacement **relative** to equilibrium. Define

$$
y=X-X_{\mathrm{eq}}.
$$

Then the amplitude is

$$
A=|X_{\mathrm{release}}-X_{\mathrm{eq}}|
=0.13\,\mathrm m,
$$

not $0.48\,\mathrm m$. The oscillator is released from the positive turning point, so cosine matches the initial state.

It completes $12$ cycles in $7.0\,\mathrm s$:

$$
f=\frac{12}{7.0}\,\mathrm{Hz},
\qquad
\omega=2\pi f=\frac{24\pi}{7}\,\mathrm{rad/s}.
$$

Thus

$$
y(t)=0.13\cos\left(\frac{24\pi}{7}t\right)\,\mathrm m,
$$

$$
v(t)=-0.13\left(\frac{24\pi}{7}\right)
\sin\left(\frac{24\pi}{7}t\right)\,\mathrm{m/s}.
$$

At $t=3.9\,\mathrm s$,

$$
y\approx\boxed{-0.051\,\mathrm m},
\qquad
v\approx\boxed{+1.3\,\mathrm{m/s}}.
$$

The negative relative position and positive velocity mean that the block is on the negative side of equilibrium and moving toward equilibrium. If the absolute coordinate is needed, add the equilibrium coordinate:

$$
X=X_{\mathrm{eq}}+y
\approx0.35-0.051
=0.299\,\mathrm m.
$$

```quiz
type: radio
id: mct-p4-equilibrium-reference
shuffle: true
content: |-
  A block's equilibrium coordinate is $X_{\mathrm{eq}}=0.40\,\mathrm m$. It is released from rest at $X=0.52\,\mathrm m$ and completes $6$ cycles in $4.0\,\mathrm s$. What is its state at $t=1.0\,\mathrm s$?
options:
- id: mct-p4-equilibrium-reference-a
  content: |-
    Relative position $y=-0.12\,\mathrm m$, absolute position $X=0.28\,\mathrm m$, and $v=0$
  correct: true
  feedback: |-
    The amplitude is measured from equilibrium: $A=0.52-0.40=0.12\,\mathrm m$. Since $f=6/4=1.5\,\mathrm{Hz}$, one second is $1.5$ cycles, placing the block at the opposite turning point: $y=-A$, $X=0.40-0.12=0.28\,\mathrm m$, and $v=0$.
- id: mct-p4-equilibrium-reference-b
  content: |-
    Relative position $y=-0.52\,\mathrm m$, absolute position $X=-0.12\,\mathrm m$, and $v=0$
  feedback: |-
    This uses the release coordinate as the amplitude. SHM displacement is measured from equilibrium, so $A=|0.52-0.40|=0.12\,\mathrm m$, not $0.52\,\mathrm m$.
- id: mct-p4-equilibrium-reference-c
  content: |-
    Relative position $y=+0.12\,\mathrm m$, absolute position $X=0.52\,\mathrm m$, and $v=0$
  feedback: |-
    This returns to the starting point after an integer number of cycles. At $t=1.0\,\mathrm s$ the oscillator has completed $1.5$ cycles, so it is at the opposite turning point.
- id: mct-p4-equilibrium-reference-d
  content: |-
    Relative position $y=0$, absolute position $X=0.40\,\mathrm m$, with maximum positive velocity
  feedback: |-
    An equilibrium crossing occurs after a quarter-cycle offset from a turning point. After $1.5$ cycles, the block is at the opposite turning point, where velocity is zero.
- id: mct-p4-equilibrium-reference-e
  content: |-
    Relative position $y=-0.12\,\mathrm m$, absolute position $X=0.28\,\mathrm m$, with maximum negative velocity
  feedback: |-
    The positions are correct, but a turning point has zero instantaneous velocity. Speed is maximum at equilibrium, not at maximum displacement.
```

---

<a id="summary"></a>
## Summary

- Measure oscillator position from equilibrium before writing an SHM function.
- Read $A$ from the outer coefficient and $\omega$ from the coefficient of $t$ inside the phase:
  $$
  f=\frac{\omega}{2\pi},
  \qquad
  T=\frac{2\pi}{\omega},
  \qquad
  k=m\omega^2.
  $$
- Choose the zero-phase function from the initial state: $+\cos$ at $+A$, $-\cos$ at $-A$, $+\sin$ at equilibrium with positive velocity, and $-\sin$ at equilibrium with negative velocity.
- Differentiate with the chain rule and preserve the phase argument:
  $$
  v=\frac{dx}{dt},
  \qquad
  a=\frac{dv}{dt}=-\omega^2x.
  $$
- Use radians when evaluating $\sin(\omega t+\phi)$ or $\cos(\omega t+\phi)$ because the phase is in radians.
- “At time $t$” means substitute into the time functions. “At position $x$” means use $a=-\omega^2x$, $F=-kx$, and $|v|=\omega\sqrt{A^2-x^2}$.
- A position usually occurs twice per cycle. Without a time or direction, position determines speed but not the sign of velocity.
- At a turning point, $v=0$ and $|a|$ is maximum. At equilibrium, $a=0$ and $|v|$ is maximum.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
