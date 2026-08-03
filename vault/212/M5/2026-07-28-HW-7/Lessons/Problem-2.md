# Wave Speed on a String Supporting a Hanging Mass

<!--
lesson-id: 212-M5-015
topic-code: MTH212.M5.15
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Total String Mass to Linear Density](#convert-total-string-mass-to-linear-density)
- [Use the Hanging Block to Find the Tension](#use-the-hanging-block-to-find-the-tension)
- [Substitute Both String Properties](#substitute-both-string-properties)
- [Keep the Two Masses in Their Roles](#keep-the-two-masses-in-their-roles)
- [Summary](#summary)

## Prerequisites

- Recognize the weight of a mass $M$ as $Mg$.
- Interpret linear mass density as mass per unit length.
- Simplify a fraction whose denominator is itself a fraction.

---

<a id="introduction"></a>
## Introduction

When a heavy block hangs from a uniform light string, the block and the string play different roles in the wave speed:

$$
v=\sqrt{\frac{T}{\mu}}.
$$

The hanging block supplies the tension $T$, while the string's mass and length supply the linear mass density $\mu$.

| Given information | Quantity it determines |
| --- | --- |
| Hanging-block mass $M$ | $T\approx Mg$ |
| String mass $m$ and length $l$ | $\mu=m/l$ |

The words **heavy block** and **light string** tell us to neglect the string's weight when finding the tension. Thus, the tension is approximately constant and set by the block. Within this approximation, use $T=Mg$. The reusable procedure is:

$$
M\longrightarrow T,
\qquad
(m,l)\longrightarrow\mu,
\qquad
(T,\mu)\longrightarrow v.
$$

---

<a id="convert-total-string-mass-to-linear-density"></a>
## Convert Total String Mass to Linear Density

**Example:** A uniform string has total mass $0.30\,\mathrm{kg}$ and length $1.5\,\mathrm{m}$. Find its linear mass density.

**Explanation**

Linear mass density is the string's mass per unit length:

$$
\mu=\frac{m_{\text{string}}}{L}
=\frac{0.30\,\mathrm{kg}}{1.5\,\mathrm{m}}
=0.20\,\mathrm{kg/m}.
$$

The total mass is not itself $\mu$. Dividing by the length converts the total mass into the inertia per unit length that appears in the wave-speed formula.

```quiz
type: radio
id: p2-density-q1
content: |-
  A uniform string has total mass $s$ and length $L$. Which expression is its linear mass density?
options:
- id: p2-density-q1-a
  content: |-
    $\mu=\dfrac{s}{L}$
  correct: true
- id: p2-density-q1-b
  content: |-
    $\mu=\dfrac{L}{s}$
- id: p2-density-q1-c
  content: |-
    $\mu=sL$
- id: p2-density-q1-d
  content: |-
    $\mu=s$
- id: p2-density-q1-e
  content: |-
    $\mu=\dfrac{s}{L^2}$
```

---

<a id="use-the-hanging-block-to-find-the-tension"></a>
## Use the Hanging Block to Find the Tension

**Example:** A stationary block of mass $6\,\mathrm{kg}$ hangs from a light string. Take $g=9.8\,\mathrm{m/s^2}$. What tension should be used to model waves on the string?

**Explanation**

The stationary block has zero acceleration, so the upward tension balances its downward weight:

$$
T-Mg=0
\qquad\Longrightarrow\qquad
T=Mg.
$$

Numerically,

$$
T=(6\,\mathrm{kg})(9.8\,\mathrm{m/s^2})
=58.8\,\mathrm{N}.
$$

Because the string is light compared with the block, its own weight does not appreciably change the tension along its length.

```quiz
type: radio
id: p2-tension-q1
content: |-
  A stationary heavy block of mass $H$ hangs from a light string of mass $s$. Which tension should be used in $v=\sqrt{T/\mu}$ under the light-string approximation?
options:
- id: p2-tension-q1-a
  content: |-
    $T=Hg$
  correct: true
- id: p2-tension-q1-b
  content: |-
    $T=sg$
- id: p2-tension-q1-c
  content: |-
    $T=(H+s)g$
- id: p2-tension-q1-d
  content: |-
    $T=\dfrac{Hg}{s}$
- id: p2-tension-q1-e
  content: |-
    $T=0$
```

---

<a id="substitute-both-string-properties"></a>
## Substitute Both String Properties

**Example:** A $4.0\,\mathrm{kg}$ block hangs from a uniform light string with mass $0.20\,\mathrm{kg}$ and length $2.0\,\mathrm{m}$. Find the wave speed using $g=9.8\,\mathrm{m/s^2}$.

**Explanation**

First find the two inputs to the speed formula:

$$
T=Mg=(4.0)(9.8)=39.2\,\mathrm{N},
$$

$$
\mu=\frac{m}{l}
=\frac{0.20}{2.0}
=0.10\,\mathrm{kg/m}.
$$

Then substitute:

$$
\begin{aligned}
v
&=\sqrt{\frac{T}{\mu}} \\
&=\sqrt{\frac{39.2}{0.10}} \\
&=\sqrt{392} \\
&\approx 19.8\,\mathrm{m/s}.
\end{aligned}
$$

A units check confirms that the square root produces a speed:

$$
\frac{\mathrm{N}}{\mathrm{kg/m}}
=\frac{\mathrm{kg\,m/s^2}}{\mathrm{kg/m}}
=\frac{\mathrm{m^2}}{\mathrm{s^2}}.
$$

```quiz
type: radio
id: p2-substitute-q1
content: |-
  A heavy block of mass $H$ hangs from a uniform light string of mass $s$ and length $L$. Which substitution into the string-wave formula is correct?
options:
- id: p2-substitute-q1-a
  content: |-
    $\displaystyle v=\sqrt{\frac{Hg}{s/L}}$
  correct: true
- id: p2-substitute-q1-b
  content: |-
    $\displaystyle v=\sqrt{\frac{sg}{H/L}}$
- id: p2-substitute-q1-c
  content: |-
    $\displaystyle v=\sqrt{\frac{Hg}{sL}}$
- id: p2-substitute-q1-d
  content: |-
    $\displaystyle v=\sqrt{\frac{s/L}{Hg}}$
- id: p2-substitute-q1-e
  content: |-
    $\displaystyle v=\sqrt{\frac{(H+s)g}{s/L}}$
```

---

<a id="keep-the-two-masses-in-their-roles"></a>
## Keep the Two Masses in Their Roles

**Example:** A heavy block has mass $M$, and the uniform light string supporting it has mass $m$ and length $l$. Derive the wave speed in the string.

**Explanation**

Keep the two masses attached to their physical roles:

$$
\underbrace{T=Mg}_{\text{block sets tension}},
\qquad
\underbrace{\mu=\frac{m}{l}}_{\text{string sets linear density}}.
$$

Therefore,

$$
\begin{aligned}
v
&=\sqrt{\frac{T}{\mu}} \\
&=\sqrt{\frac{Mg}{m/l}} \\
&=\sqrt{\frac{Mgl}{m}}.
\end{aligned}
$$

Dividing by $m/l$ multiplies by its reciprocal $l/m$. Do not interchange $M$ and $m$, and do not use $M+m$ in the tension under the stated light-string approximation.

The variable dependence gives a quick answer check:

| Change while the other quantities stay fixed | Effect on $v$ |
| --- | --- |
| Increase the block mass $M$ | $v$ increases because the tension increases |
| Increase the string mass $m$ | $v$ decreases because the linear density increases |
| Increase the string length $l$ | $v$ increases because the same string mass is spread over more length |

Only $\sqrt{Mgl/m}$ has all three of these dependencies.

```quiz
type: radio
id: p2-homework-q1
content: |-
  A heavy block of mass $M$ is hung from a uniform light string of mass $m$ and length $l$ whose opposite end is attached to the ceiling.

  If the string is plucked, what will be the speed of the wave(s) generated in the string?
options:
- id: p2-homework-q1-a
  content: |-
    $\sqrt{\dfrac{Mgl}{m}}$
  correct: true
- id: p2-homework-q1-b
  content: |-
    $\sqrt{\dfrac{mgl}{M}}$
- id: p2-homework-q1-c
  content: |-
    $\sqrt{\dfrac{(M+m)gl}{m}}$
- id: p2-homework-q1-d
  content: |-
    $\sqrt{\dfrac{mgl}{m+M}}$
```

---

<a id="summary"></a>
## Summary

**Recognition cue:** A hanging block supplies the tension in a uniform light string whose total mass and length are given.

**Procedure:**

1. Under the light-string approximation, use the block mass for the tension: $T=Mg$.
2. Use the string mass and length for the linear density: $\mu=m/l$.
3. Substitute into $v=\sqrt{T/\mu}$.
4. Simplify division by $m/l$ by multiplying by $l/m$.

Thus,

$$
\boxed{v=\sqrt{\frac{Mgl}{m}}}.
$$

**Main trap:** $M$ and $m$ are not interchangeable. The hanging mass $M$ determines the tension, while the string mass $m$ determines the linear mass density.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
