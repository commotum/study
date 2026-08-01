# Finding Wave Speed on a String With a Hanging Mass

## Table of Contents

- [Introduction](#introduction)
- [Find the String's Linear Mass Density](#find-the-strings-linear-mass-density)
- [Find the Tension From the Hanging Ball](#find-the-tension-from-the-hanging-ball)
- [Combine the Quantities in the Wave-Speed Formula](#combine-the-quantities-in-the-wave-speed-formula)
- [Check Units and Round at the End](#check-units-and-round-at-the-end)
- [Apply the Method to the Hanging Ball](#apply-the-method-to-the-hanging-ball)
- [Summary](#summary)

## Prerequisites

- Compute a unit rate by dividing one measured quantity by another.
- Use the weight relation $T\approx mg$ for a stationary hanging object.
- Substitute into a square-root formula and round to significant figures.

---

<a id="introduction"></a>
## Introduction

For a transverse wave on a stretched string, the wave speed is

$$
v=\sqrt{\frac{T}{\mu}},
$$

where $T$ is the string tension and $\mu$ is the string's linear mass density.

When a ball hangs at rest from a string of uniform mass, use

$$
T\approx m_b g
\qquad\text{and}\qquad
\mu=\frac{m_s}{L},
$$

where $m_b$ is the ball's mass, $m_s$ is the string's mass, and $L$ is the string's length. Combining these relations gives

$$
v=\sqrt{\frac{m_b gL}{m_s}}.
$$

The recognition cue is a massive string whose tension is supplied by a stationary hanging object. Keep the ball mass and string mass in their separate roles.

| Given quantity | Use it to find | Relation |
|---|---|---|
| Ball mass $m_b$ | Tension $T$ | $T\approx m_b g$ |
| String mass $m_s$ and length $L$ | Linear density $\mu$ | $\mu=m_s/L$ |
| Tension $T$ and density $\mu$ | Wave speed $v$ | $v=\sqrt{T/\mu}$ |

---

<a id="find-the-strings-linear-mass-density"></a>
## Find the String's Linear Mass Density

**Example:** A uniform string has mass $m_s=0.040\ \mathrm{kg}$ and length $L=2.0\ \mathrm{m}$. Find its linear mass density.

**Explanation**

Linear mass density means mass per unit length:

$$
\begin{aligned}
\mu
&=\frac{m_s}{L}\\
&=\frac{0.040\ \mathrm{kg}}{2.0\ \mathrm{m}}\\
&=0.020\ \mathrm{kg/m}.
\end{aligned}
$$

Thus $0.020\ \mathrm{kg/m}$ means each meter of the uniform string has mass $0.020\ \mathrm{kg}$.

Use the **string's** mass here. The hanging object's mass determines the tension instead.

```quiz
type: radio
id: problem-1-density-q1
content: |-
  A uniform string has mass $0.12\ \mathrm{kg}$ and length $4.0\ \mathrm{m}$. What is its linear mass density $\mu$?
options:
- id: a
  content: |-
    $0.030\ \mathrm{kg/m}$
  correct: true
  feedback: |-
    $\mu=m_s/L=(0.12\ \mathrm{kg})/(4.0\ \mathrm{m})=0.030\ \mathrm{kg/m}$.
- id: b
  content: |-
    $0.48\ \mathrm{kg/m}$
  feedback: |-
    Linear density is mass divided by length, not mass multiplied by length.
- id: c
  content: |-
    $33\ \mathrm{m/kg}$
  feedback: |-
    This reverses the ratio and has the reciprocal units.
- id: d
  content: |-
    $4.1\ \mathrm{kg/m}$
  feedback: |-
    This adds the mass and length, which are unlike quantities.
```

---

<a id="find-the-tension-from-the-hanging-ball"></a>
## Find the Tension From the Hanging Ball

**Example:** A $0.50\ \mathrm{kg}$ ball hangs at rest from the string. Approximate the string tension using $g=9.8\ \mathrm{m/s^2}$.

**Explanation**

Because the ball is stationary, its acceleration is zero. The upward tension balances the downward weight:

$$
\begin{aligned}
T&\approx m_b g\\
&=(0.50\ \mathrm{kg})(9.8\ \mathrm{m/s^2})\\
&=4.9\ \mathrm{N}.
\end{aligned}
$$

In this model, do not use the string's mass in $T\approx m_b g$; it has already been used to find $\mu$.

```quiz
type: radio
id: problem-1-tension-q1
content: |-
  A $0.30\ \mathrm{kg}$ ball hangs stationary from a string. Using $g=9.8\ \mathrm{m/s^2}$, what tension is supplied by the ball's weight?
options:
- id: a
  content: |-
    $2.9\ \mathrm{N}$
  correct: true
  feedback: |-
    $T\approx m_b g=(0.30)(9.8)=2.94\ \mathrm{N}$, which is $2.9\ \mathrm{N}$ to two significant figures.
- id: b
  content: |-
    $0.031\ \mathrm{N}$
  feedback: |-
    This divides the mass by $g$ instead of multiplying.
- id: c
  content: |-
    $9.8\ \mathrm{N}$
  feedback: |-
    The value of $g$ must be multiplied by the ball's mass.
- id: d
  content: |-
    $0.30\ \mathrm{N}$
  feedback: |-
    A mass in kilograms is not numerically equal to its weight in newtons.
```

---

<a id="combine-the-quantities-in-the-wave-speed-formula"></a>
## Combine the Quantities in the Wave-Speed Formula

**Example:** A $0.50\ \mathrm{kg}$ ball hangs from a $2.0\ \mathrm{m}$ string whose mass is $0.040\ \mathrm{kg}$. Using $g=9.8\ \mathrm{m/s^2}$, find the wave speed.

**Explanation**

First calculate the two inputs:

$$
\mu=\frac{0.040\ \mathrm{kg}}{2.0\ \mathrm{m}}
=0.020\ \mathrm{kg/m},
$$

$$
T\approx(0.50\ \mathrm{kg})(9.8\ \mathrm{m/s^2})
=4.9\ \mathrm{N}.
$$

Then substitute into the wave-speed formula:

$$
\begin{aligned}
v
&=\sqrt{\frac{T}{\mu}}\\
&=\sqrt{\frac{4.9\ \mathrm{N}}{0.020\ \mathrm{kg/m}}}\\
&=15.65\ldots\ \mathrm{m/s}\\
&=16\ \mathrm{m/s}
\end{aligned}
$$

to two significant figures.

```quiz
type: radio
id: problem-1-speed-q1
content: |-
  A $0.40\ \mathrm{kg}$ ball hangs from a $2.0\ \mathrm{m}$ string whose mass is $0.050\ \mathrm{kg}$. Use $g=9.8\ \mathrm{m/s^2}$. What is the wave speed to two significant figures?
options:
- id: a
  content: |-
    $13\ \mathrm{m/s}$
  correct: true
  feedback: |-
    $\mu=0.050/2.0=0.025\ \mathrm{kg/m}$, $T=0.40(9.8)=3.92\ \mathrm{N}$, and $v=\sqrt{3.92/0.025}=12.52\ldots\ \mathrm{m/s}\approx13\ \mathrm{m/s}$.
- id: b
  content: |-
    $160\ \mathrm{m/s}$
  feedback: |-
    This is approximately $T/\mu$ before taking the required square root.
- id: c
  content: |-
    $8.9\ \mathrm{m/s}$
  feedback: |-
    Check that the string mass, not the ball mass, is used in $\mu=m_s/L$.
- id: d
  content: |-
    $0.32\ \mathrm{m/s}$
  feedback: |-
    This does not follow the ratio $T/\mu$ inside the square root.
```

---

<a id="check-units-and-round-at-the-end"></a>
## Check Units and Round at the End

**Example:** Show that $\sqrt{T/\mu}$ has units of speed.

**Explanation**

Substitute the units $[T]=\mathrm{N}=\mathrm{kg\,m/s^2}$ and $[\mu]=\mathrm{kg/m}$:

$$
\begin{aligned}
\left[\frac{T}{\mu}\right]
&=\frac{\mathrm{kg\,m/s^2}}{\mathrm{kg/m}}\\
&=\mathrm{m^2/s^2}.
\end{aligned}
$$

Therefore,

$$
[v]=\sqrt{\mathrm{m^2/s^2}}=\mathrm{m/s}.
$$

Keep extra calculator digits in $\mu$, $T$, and $v$ until the last line. Then round using the measured givens and follow the answer field's requested format.

**Watch Out!** Wave speed is a magnitude, so use the positive square root. A negative value would describe neither a second physical speed nor the wave's direction.

```quiz
type: radio
id: problem-1-rounding-q1
content: |-
  A wave-speed calculation gives $v=9.64\ldots\ \mathrm{m/s}$. The measured givens have two significant figures, and the answer field requests meters per second as a number only. What should be entered?
options:
- id: a
  content: |-
    `9.6`
  correct: true
  feedback: |-
    $9.64\ldots$ rounds to $9.6$ at two significant figures, and a number-only field omits units.
- id: b
  content: |-
    `9.64 m/s`
  feedback: |-
    This keeps an extra significant figure and includes units in a number-only field.
- id: c
  content: |-
    `10`
  feedback: |-
    This is only one significant figure.
- id: d
  content: |-
    `9.7`
  feedback: |-
    The hundredths digit is $4$, so the tenths digit stays $6$.
```

---

<a id="apply-the-method-to-the-hanging-ball"></a>
## Apply the Method to the Hanging Ball

**Example:** A $0.26\ \mathrm{kg}$ ball hangs from a $3.5\ \mathrm{m}$ string whose mass is $0.096\ \mathrm{kg}$. The string is plucked and a wave propagates along it. Disregard reflections.

![](<../Source/Images/ball-hanging-from-massive-string.png>)

**Explanation**

Assign each source value to its role before calculating:

| Quantity | Source value | Role |
|---|---:|---|
| Ball mass $m_b$ | $0.26\ \mathrm{kg}$ | Sets $T\approx m_b g$ |
| String length $L$ | $3.5\ \mathrm{m}$ | Denominator of $\mu=m_s/L$ |
| String mass $m_s$ | $0.096\ \mathrm{kg}$ | Numerator of $\mu=m_s/L$ |

The string's linear mass density is

$$
\mu=\frac{0.096\ \mathrm{kg}}{3.5\ \mathrm{m}}
=0.02743\ldots\ \mathrm{kg/m}.
$$

Approximating the tension as the ball's weight gives

$$
\begin{aligned}
v
&=\sqrt{\frac{T}{\mu}}\\
&=\sqrt{\frac{(0.26\ \mathrm{kg})(9.81\ \mathrm{m/s^2})}{0.02743\ldots\ \mathrm{kg/m}}}\\
&=9.64\ldots\ \mathrm{m/s}.
\end{aligned}
$$

The instruction to disregard reflections means only the propagating wave speed is needed. The measured givens have two significant figures, so $v=9.6\ \mathrm{m/s}$.

```quiz
type: radio
id: m5-2pre-q1
content: |-
  **Question 1**

  A $0.26\ \mathrm{kg}$ ball hangs from a $3.5\ \mathrm{m}$ string whose mass is $0.096\ \mathrm{kg}$. The string is plucked and a wave propagates along it. Disregard reflections.

  ![](<../Source/Images/ball-hanging-from-massive-string.png>)

  The answer field requests the wave speed in meters per second as a number only. What should be entered?
options:
- id: a
  content: |-
    `9.6`
  correct: true
  feedback: |-
    $\mu=0.096/3.5=0.02743\ldots\ \mathrm{kg/m}$ and $T\approx(0.26)(9.81)\ \mathrm{N}$, so $v=\sqrt{T/\mu}=9.64\ldots\ \mathrm{m/s}$. To two significant figures, enter `9.6`.
- id: b
  content: |-
    `93`
  feedback: |-
    This is approximately $T/\mu$ before taking the square root.
- id: c
  content: |-
    `5.2`
  feedback: |-
    This results from assigning the ball and string masses to the wrong roles.
- id: d
  content: |-
    `9.64`
  feedback: |-
    The measured givens support two significant figures, not three.
```

---

<a id="summary"></a>
## Summary

For a uniform massive string held taut by a stationary hanging ball:

1. Find the string density: $\mu=m_s/L$.
2. Approximate the tension from the ball: $T\approx m_b g$.
3. Calculate $v=\sqrt{T/\mu}=\sqrt{m_b gL/m_s}$.
4. Check that the units reduce to $\mathrm{m/s}$.
5. Keep full precision until the end, then round and use the requested answer form.

The main trap is swapping the two masses: the **string mass** belongs in $\mu$, while the **ball mass** belongs in $T$.
