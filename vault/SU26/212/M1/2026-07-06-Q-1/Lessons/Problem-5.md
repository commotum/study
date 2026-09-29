# From Linear Velocity to Spool Revolutions

<!--
lesson-id: 212-M1-071
topic-code: MTH212.M1.71
-->
## Table of Contents

- [Introduction](#introduction)
- [Accumulate the Unwound Rope Length](#accumulate-the-unwound-rope-length)
- [Convert Rope Length to Revolutions](#convert-rope-length-to-revolutions)
- [Build the Symbolic Chain](#build-the-symbolic-chain)
- [Apply the Chain and Report the Result](#apply-the-chain-and-report-the-result)
- [Summary](#summary)

## Prerequisites

- Integrate a polynomial term by term with the power rule.
- Use the circumference of a circle, $C=2\pi r$.
- Round a calculated result to a stated number of significant figures.

---

<a id="introduction"></a>
## Introduction

When a rope unwinds from a constant-radius spool without slipping, the rope length pulled away equals the arc length released from the rim. If the linear velocity is given as a function of time and the question asks for revolutions, use this chain:

$$
v(t)
\xrightarrow{\text{integrate over time}}
s
\xrightarrow{\text{divide by }r}
\theta
\xrightarrow{\text{divide by }2\pi}
n_{\mathrm{rev}}.
$$

Here $s$ is the rope length, $\theta$ is the angular displacement in radians, and $n_{\mathrm{rev}}$ is the number of revolutions. Combining the last two steps gives the most useful form:

$$
n_{\mathrm{rev}}=\frac{s}{2\pi r}
=\frac{1}{2\pi r}\int_{t_0}^{t_f}v(t)\,dt.
$$

The recognition cue is the combination of a time-dependent linear velocity, a rope unwinding from a spool, and a requested number of turns. Integrate before converting; the value of $v(t_f)$ is a speed, not a traveled length.

---

<a id="accumulate-the-unwound-rope-length"></a>
## Accumulate the Unwound Rope Length

**Example:** A cord moves away from a spool with

$$
v(t)=At+Bt^2,
$$

where $A=4.0\ \mathrm{m}/\mathrm{s}^2$ and $B=3.0\ \mathrm{m}/\mathrm{s}^3$. How much cord unwinds from $t=0$ to $t=2.0\ \mathrm{s}$?

**Explanation**

Velocity is the rate at which length accumulates, so integrate it over the time interval:

$$
\begin{aligned}
s
&=\int_0^{2.0}(At+Bt^2)\,dt \\
&=\left[\frac{A}{2}t^2+\frac{B}{3}t^3\right]_0^{2.0} \\
&=\frac{4.0}{2}(2.0)^2+\frac{3.0}{3}(2.0)^3 \\
&=16\ \mathrm{m}.
\end{aligned}
$$

Each term of the velocity contributes to the total length. The lower endpoint contributes zero here because the interval starts at $t=0$ and both antiderivative terms contain a power of $t$.

```quiz
type: radio
id: p5-length-from-velocity
content: |-
  A rope moves with $v(t)=2t+3t^2$ in SI units. How much rope is released from $t=0$ to $t=3\ \mathrm{s}$?
options:
- id: p5-length-from-velocity-a
  content: |-
    $36\ \mathrm{m}$
  correct: true
  feedback: |-
    Rope length is the time integral of velocity. Here $s=[t^2+t^3]_0^3=9+27=36\ \mathrm{m}$, so both velocity terms contribute to the accumulated length.
- id: p5-length-from-velocity-b
  content: |-
    $33\ \mathrm{m}$
  feedback: |-
    Substituting $t=3$ directly gives $v(3)=33\ \mathrm{m}/\mathrm{s}$, an instantaneous speed rather than a length. Integrating over time changes the units to meters and gives $36\ \mathrm{m}$.
- id: p5-length-from-velocity-c
  content: |-
    $99\ \mathrm{m}$
  feedback: |-
    This results from raising each power of $t$ without dividing by the new exponent. The power rule requires $\int 2t\,dt=t^2$ and $\int 3t^2\,dt=t^3$, which give $9+27=36\ \mathrm{m}$ at $t=3$.
- id: p5-length-from-velocity-d
  content: |-
    $27\ \mathrm{m}$
  feedback: |-
    This keeps only the contribution from $3t^2$. The $2t$ term also releases rope: its integral contributes $[t^2]_0^3=9\ \mathrm{m}$, raising the total to $36\ \mathrm{m}$.
- id: p5-length-from-velocity-e
  content: |-
    $9\ \mathrm{m}$
  feedback: |-
    This keeps only the contribution from $2t$. The $3t^2$ term contributes $[t^3]_0^3=27\ \mathrm{m}$ as well, so the total released length is $36\ \mathrm{m}$.
```

---

<a id="convert-rope-length-to-revolutions"></a>
## Convert Rope Length to Revolutions

**Example:** A spool has radius $1.5\ \mathrm{m}$ and releases $3\pi\ \mathrm{m}$ of rope. How many revolutions does it make?

**Explanation**

One full revolution releases one circumference of rope:

$$
C=2\pi r=2\pi(1.5)=3\pi\ \mathrm{m}/\mathrm{rev}.
$$

Therefore,

$$
n_{\mathrm{rev}}=\frac{s}{2\pi r}
=\frac{3\pi}{3\pi}
=1\ \mathrm{rev}.
$$

Equivalently, $\theta=s/r=2\pi$ radians, and $n_{\mathrm{rev}}=\theta/(2\pi)=1$. Stopping after $s/r$ gives radians, not revolutions.

```quiz
type: radio
id: p5-length-to-turns
content: |-
  A spool of radius $1.5\ \mathrm{m}$ releases $24\ \mathrm{m}$ of rope without slipping. How many revolutions does it make, to two significant figures?
options:
- id: p5-length-to-turns-a
  content: |-
    $2.5$ revolutions
  correct: true
  feedback: |-
    Each revolution releases one circumference, $2\pi r=3\pi\ \mathrm{m}$. Thus $n_{\mathrm{rev}}=24/(3\pi)=2.546\ldots$, which rounds to $2.5$ revolutions at two significant figures.
- id: p5-length-to-turns-b
  content: |-
    $16$ revolutions
  feedback: |-
    The quotient $s/r=24/1.5=16$ is the angular displacement in radians. One revolution contains $2\pi$ radians, so dividing $16$ by $2\pi$ gives $2.5$ revolutions to two significant figures.
- id: p5-length-to-turns-c
  content: |-
    $8.0$ revolutions
  feedback: |-
    Dividing by $2r$ uses the spool's diameter, not the length released by one complete turn. A turn releases the full circumference $2\pi r$, so the missing factor of $\pi$ must be included.
- id: p5-length-to-turns-d
  content: |-
    $5.1$ revolutions
  feedback: |-
    The denominator $\pi r$ is only half a circumference, so it counts each half-turn as a full revolution and doubles the result. Divide by $2\pi r$ to obtain $2.5$ revolutions.
- id: p5-length-to-turns-e
  content: |-
    $0.39$ revolutions
  feedback: |-
    This reverses the ratio and computes circumference divided by released length. The number of turns is released length divided by length per turn: $n_{\mathrm{rev}}=s/(2\pi r)$.
```

---

<a id="build-the-symbolic-chain"></a>
## Build the Symbolic Chain

**Example:** A rope's velocity is

$$
v(t)=At+Bt^2.
$$

Derive the spool's number of revolutions from $t=0$ to a general final time $t_f$ before inserting any values.

**Explanation**

First accumulate the released rope length:

$$
s(t_f)
=\int_0^{t_f}(At+Bt^2)\,dt
=\frac{A}{2}t_f^2+\frac{B}{3}t_f^3.
$$

Then divide by the rope released per revolution:

$$
\boxed{
n_{\mathrm{rev}}(t_f)
=\frac{\frac12At_f^2+\frac13Bt_f^3}{2\pi r}
}.
$$

The units audit the chain. Since $[A]=\mathrm{m}/\mathrm{s}^2$ and $[B]=\mathrm{m}/\mathrm{s}^3$, both numerator terms have units of length. Dividing by the circumference, also a length per revolution, leaves a number of revolutions.

```quiz
type: radio
id: p5-symbolic-chain
content: |-
  A constant-radius spool unwinds without slipping while the rope has velocity $v(t)=At+Bt^2$. Which expression gives the number of revolutions from $t=0$ to $t=t_f$?
options:
- id: p5-symbolic-chain-a
  content: |-
    $\displaystyle \frac{\frac12At_f^2+\frac13Bt_f^3}{2\pi r}$
  correct: true
  feedback: |-
    Integrating velocity gives the released length $\frac12At_f^2+\frac13Bt_f^3$. One revolution releases $2\pi r$ of rope, so dividing that length by $2\pi r$ gives the number of revolutions.
- id: p5-symbolic-chain-b
  content: |-
    $\displaystyle \frac{At_f+Bt_f^2}{2\pi r}$
  feedback: |-
    The numerator here is the final velocity $v(t_f)$, not accumulated rope length. Dividing speed by circumference gives a revolution rate, with units of inverse time; integrate first to obtain a number of revolutions.
- id: p5-symbolic-chain-c
  content: |-
    $\displaystyle \frac{A+2Bt_f}{2\pi r}$
  feedback: |-
    The numerator is $dv/dt$, the rope's linear acceleration. Acceleration does not measure how much rope has unwound; the required length comes from integrating $v(t)$ over time.
- id: p5-symbolic-chain-d
  content: |-
    $\displaystyle \frac{\frac12At_f^2+\frac13Bt_f^3}{r}$
  feedback: |-
    Dividing arc length by radius gives angular displacement $\theta$ in radians. The question asks for revolutions, so the radian result still must be divided by $2\pi$.
- id: p5-symbolic-chain-e
  content: |-
    $\displaystyle \left(\frac12At_f^2+\frac13Bt_f^3\right)(2\pi r)$
  feedback: |-
    The circumference is the rope length released per revolution, so it must divide the total released length. Multiplying produces units of area and cannot represent a dimensionless turn count.
```

---

<a id="apply-the-chain-and-report-the-result"></a>
## Apply the Chain and Report the Result

**Example:** A $7.27\ \mathrm{kg}$ greyhound pulls a rope from a spool of radius $2.2\ \mathrm{m}$. It starts from rest at the spool and moves straight away with

$$
v(t)=At+Bt^2,
$$

where $A=1.2\ \mathrm{m}/\mathrm{s}^2$ and $B=2.4\ \mathrm{m}/\mathrm{s}^3$. Find the spool's revolutions after $4.5\ \mathrm{s}$.

![](../Source/2026-07-06-Q-1/Images/quiz-1b-q1-greyhound-spool.png)

**Explanation**

Keep the symbolic model intact until the final line:

$$
n_{\mathrm{rev}}(t_f)
=\frac{\frac12At_f^2+\frac13Bt_f^3}{2\pi r}.
$$

Now evaluate the released length with guard digits:

$$
\begin{aligned}
s(4.5)
&=\frac12(1.2)(4.5)^2+\frac13(2.4)(4.5)^3 \\
&=85.05\ \mathrm{m}.
\end{aligned}
$$

Then convert the length to turns:

$$
\begin{aligned}
n_{\mathrm{rev}}
&=\frac{85.05}{2\pi(2.2)} \\
&=6.1528\ldots\ \mathrm{rev} \\
&=\boxed{6.2\ \mathrm{rev}}
\end{aligned}
$$

The final value is reported to two significant figures, matching the least precise inputs. The greyhound's mass is irrelevant because this calculation uses only kinematics and geometry; no force, torque, energy, or momentum equation is needed.

```quiz
type: radio
id: p5-final-audit
content: |-
  A $4.0\ \mathrm{kg}$ animal pulls rope from a spool of radius $1.5\ \mathrm{m}$. The rope velocity is $v(t)=At+Bt^2$, with $A=0.80\ \mathrm{m}/\mathrm{s}^2$ and $B=1.20\ \mathrm{m}/\mathrm{s}^3$. How many revolutions occur by $t=3.0\ \mathrm{s}$? Report two significant figures.
options:
- id: p5-final-audit-a
  content: |-
    $1.5$ revolutions
  correct: true
  feedback: |-
    Integration gives $s=\frac12(0.80)(3.0)^2+\frac13(1.20)(3.0)^3=14.4\ \mathrm{m}$. Dividing by $2\pi(1.5)$ gives $1.527\ldots$ revolutions, which is $1.5$ revolutions to two significant figures; the mass is not part of this kinematic conversion.
- id: p5-final-audit-b
  content: |-
    $1.53$ revolutions
  feedback: |-
    This is a reasonable guard-digit value from the correct model, but it has three significant figures. The requested two-significant-figure result is $1.5$ revolutions because the next digit is $2$.
- id: p5-final-audit-c
  content: |-
    $9.6$ revolutions
  feedback: |-
    The quotient $s/r=14.4/1.5=9.6$ is angular displacement in radians, not revolutions. Dividing by another $2\pi$ converts that angle to $1.5$ revolutions at the requested precision.
- id: p5-final-audit-d
  content: |-
    $3.1$ revolutions
  feedback: |-
    This uses $\pi r$, the length of a half-circumference, as though it were one full turn. A complete revolution releases $2\pi r$ of rope, so the correct count is half this value: $1.5$ revolutions to two significant figures.
- id: p5-final-audit-e
  content: |-
    $6.1$ revolutions
  feedback: |-
    This multiplies the turn count by the $4.0\ \mathrm{kg}$ mass. Mass matters in dynamical equations such as force or torque, but it does not enter $n_{\mathrm{rev}}=s/(2\pi r)$; multiplying by it also introduces kilograms into a dimensionless turn count.
```

---

<a id="summary"></a>
## Summary

For a rope unwinding without slipping from a fixed-radius spool:

1. Integrate the linear velocity to get released rope length:

   $$
   s=\int_{t_0}^{t_f}v(t)\,dt.
   $$

2. Divide by one circumference to get revolutions:

   $$
   n_{\mathrm{rev}}=\frac{s}{2\pi r}.
   $$

3. For $v(t)=At+Bt^2$ starting at $t=0$:

   $$
   n_{\mathrm{rev}}(t_f)=\frac{\frac12At_f^2+\frac13Bt_f^3}{2\pi r}.
   $$

The main traps are substituting the final time into velocity instead of integrating, stopping at radians instead of converting to revolutions, using something other than the full circumference, and rounding before the final step.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
