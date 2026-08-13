# Recover Spring Force, Stiffness, and Work from Extension Data

<!--
lesson-id: 212-M5-059
topic-code: MTH212.M5.59
-->

## Table of Contents

- [Introduction](#introduction)
- [Separate Restoring Force from Required Force](#force-sign)
- [Source-Video Problem 1: Force and Extension for One Spring](#source-video-force-extension)
- [Recover the Spring Constant from One Data Pair](#recover-spring-constant)
- [Source-Video Problem 2: Force, Stiffness, and Work](#source-video-work)
- [Lecture Transfer: Spring Potential Energy](#lecture-transfer)
- [Summary](#summary)

## Prerequisites

- Convert centimeters to meters using $1\ \mathrm m=100\ \mathrm{cm}$.
- Rearrange a formula for one requested variable.
- Use direct proportionality and interpret a slope.
- Find the area of a triangle.
- Distinguish a signed vector component from its magnitude.

---

<a id="introduction"></a>
## Introduction

The phrases **same spring**, **force required**, **spring constant**, and **work required to stretch or compress** point to one linear spring model:

$$
F_s=-kx.
$$

Here $x$ is displacement from the spring's unstretched equilibrium position, $k$ is its spring constant, and $F_s$ is the force exerted by the spring. Within Hooke's-law range, use this sequence:

1. Put extension or compression in units compatible with $k$.
2. If $k$ is unknown, recover it from a force–extension pair:
   $$
   k=\frac{F}{|x|}.
   $$
3. Decide what the question requests:
   $$
   \text{endpoint force magnitude:}\quad F_{\mathrm{req}}=k|x|,
   $$
   $$
   \text{work from equilibrium:}\quad W_{\mathrm{req}}=\frac12kx^2.
   $$

The same data may support both calculations, but force and work are different outputs. Force uses the endpoint of the linear relation; work uses the accumulated area under it.

---

<a id="force-sign"></a>
## Separate Restoring Force from Required Force

Choose rightward displacement as positive. Hooke's law for the **spring's force** is

$$
\boxed{F_s=-kx}.
$$

The minus sign says that the spring pulls or pushes toward equilibrium, opposite the displacement. For example, if $x>0$, then $F_s<0$.

If a problem asks how much external force is required to hold the spring at rest at that displacement, equilibrium gives

$$
F_{\mathrm{ext}}+F_s=0,
$$

so

$$
F_{\mathrm{ext}}=+kx
$$

for positive $x$. If the question asks only for the amount or magnitude,

$$
\boxed{F_{\mathrm{req}}=k|x|}.
$$

The source video says to ignore the negative sign while calculating the force required. That is valid for the requested magnitude, but the sign still matters when the spring's own force or a direction is requested.

```quiz
type: radio
id: mct-p1-force-sign
shuffle: true
content: |-
  A spring with $k=240\ \mathrm{N/m}$ is stretched $0.30\ \mathrm m$ to the right and held at rest. Right is positive. Which pair gives the spring force and the required external holding force?
options:
- id: mct-p1-force-sign-a
  content: |-
    $F_s=-72\ \mathrm N$ and $F_{\mathrm{ext}}=+72\ \mathrm N$
  correct: true
  feedback: |-
    A spring's force points opposite its displacement, so $F_s=-kx=-(240)(0.30)=-72\ \mathrm N$. Holding the spring at rest requires the equal opposite force $F_{\mathrm{ext}}=+72\ \mathrm N$.
- id: mct-p1-force-sign-b
  content: |-
    $F_s=+72\ \mathrm N$ and $F_{\mathrm{ext}}=-72\ \mathrm N$
  feedback: |-
    This reverses both directions. A spring stretched right pulls left, so its force is negative; the external holding force must point right and be positive.
- id: mct-p1-force-sign-c
  content: |-
    $F_s=-800\ \mathrm N$ and $F_{\mathrm{ext}}=+800\ \mathrm N$
  feedback: |-
    The value $800$ comes from dividing $240/0.30$, which would not calculate force and has the wrong units here. Endpoint force is $k|x|=(240)(0.30)=72\ \mathrm N$.
- id: mct-p1-force-sign-d
  content: |-
    $F_s=-36\ \mathrm N$ and $F_{\mathrm{ext}}=+36\ \mathrm N$
  feedback: |-
    The factor $1/2$ belongs to work or spring energy, not the instantaneous endpoint force. Hooke's law gives the force magnitude directly as $k|x|=72\ \mathrm N$.
- id: mct-p1-force-sign-e
  content: |-
    Both forces are zero because the spring is held at rest.
  feedback: |-
    Rest means the net force is zero, not that every force is zero. The nonzero spring and external forces cancel: $-72\ \mathrm N+72\ \mathrm N=0$.
```

---

<a id="source-video-force-extension"></a>
## Source-Video Problem 1: Force and Extension for One Spring

The source segment `iubb3eFBQ9U` from 00:05:08–00:08:25 first gives

$$
k=300\ \mathrm{N/m},
\qquad
x=25\ \mathrm{cm}.
$$

Write the conversion factor so the unwanted length unit cancels:

$$
x=25\ \mathrm{cm}
\left(\frac{1\ \mathrm m}{100\ \mathrm{cm}}\right)
=0.25\ \mathrm m.
$$

The requested force magnitude is

$$
F_{\mathrm{req}}=k|x|
=(300\ \mathrm{N/m})(0.25\ \mathrm m)
=75\ \mathrm N.
$$

The same source problem then asks how far a $150\ \mathrm N$ force compresses the same spring. Solve Hooke's-law magnitude relation for the amount of compression:

$$
|x|=\frac{F_{\mathrm{req}}}{k}
=\frac{150\ \mathrm N}{300\ \mathrm{N/m}}
=0.50\ \mathrm m
=50\ \mathrm{cm}.
$$

This also follows by direct proportionality. The same spring means the same $k$, so doubling the force from $75\ \mathrm N$ to $150\ \mathrm N$ doubles the displacement magnitude from $25\ \mathrm{cm}$ to $50\ \mathrm{cm}$.

Thus the first source problem gives

$$
\boxed{75\ \mathrm N\text{ at }25\ \mathrm{cm}},
\qquad
\boxed{150\ \mathrm N\text{ at }50\ \mathrm{cm}}.
$$

```quiz
type: radio
id: mct-p1-same-spring-scale
shuffle: true
content: |-
  A force of $90\ \mathrm N$ stretches a spring $15\ \mathrm{cm}$. Within Hooke's-law range, how far will $210\ \mathrm N$ stretch the same spring?
options:
- id: mct-p1-same-spring-scale-a
  content: |-
    $35\ \mathrm{cm}$
  correct: true
  feedback: |-
    For one spring, $F=kx$, so force and extension have the same scale factor. Since $210/90=7/3$, the new extension is $(7/3)(15\ \mathrm{cm})=35\ \mathrm{cm}$.
- id: mct-p1-same-spring-scale-b
  content: |-
    $6.43\ \mathrm{cm}$
  feedback: |-
    This uses the force ratio backward, multiplying by $90/210$. A larger force on the same spring must produce a larger extension, so use the new-to-old ratio $210/90$.
- id: mct-p1-same-spring-scale-c
  content: |-
    $23.3\ \mathrm{cm}$
  feedback: |-
    This adds the force ratio $210/90$ to the original extension. Direct proportionality requires multiplication by that ratio: $(210/90)(15)=35\ \mathrm{cm}$.
- id: mct-p1-same-spring-scale-d
  content: |-
    $81.7\ \mathrm{cm}$
  feedback: |-
    This squares the force ratio. Hooke's law is linear in extension, $F\propto x$, so the displacement ratio equals the first power of the force ratio.
- id: mct-p1-same-spring-scale-e
  content: |-
    $15\ \mathrm{cm}$
  feedback: |-
    The spring constant stays fixed for the same spring, but the extension does not. Raising the force from $90\ \mathrm N$ to $210\ \mathrm N$ raises the extension in the same ratio.
```

---

<a id="recover-spring-constant"></a>
## Recover the Spring Constant from One Data Pair

If a force–extension pair is given instead of $k$, isolate the constant of proportionality:

$$
F=k|x|
\qquad\Longrightarrow\qquad
\boxed{k=\frac{F}{|x|}}.
$$

Convert the displacement before dividing if $k$ is required in newtons per meter. For instance, suppose $180\ \mathrm N$ stretches a spring $60\ \mathrm{cm}$:

$$
60\ \mathrm{cm}=0.60\ \mathrm m,
$$

$$
k=\frac{180\ \mathrm N}{0.60\ \mathrm m}
=300\ \mathrm{N/m}.
$$

Geometrically, $k$ is the slope of the straight force-magnitude versus extension graph:

```text
F
│          ● (x, F)
│        /
│      /     slope = F/x = k
│    /
│  /
└──────────────── x
```

The line passes through the origin for an ideal Hooke's-law spring. One nonzero point therefore fixes its slope.

```quiz
type: radio
id: mct-p1-recover-k
shuffle: true
content: |-
  A force of $320\ \mathrm N$ stretches an ideal spring $20\ \mathrm{cm}$. What is the spring constant?
options:
- id: mct-p1-recover-k-a
  content: |-
    $1600\ \mathrm{N/m}$
  correct: true
  feedback: |-
    Convert $20\ \mathrm{cm}=0.20\ \mathrm m$, then use the slope $k=F/x$. Thus $k=(320\ \mathrm N)/(0.20\ \mathrm m)=1600\ \mathrm{N/m}$.
- id: mct-p1-recover-k-b
  content: |-
    $16\ \mathrm{N/m}$
  feedback: |-
    This divides by the numerical value $20$ while leaving it in centimeters. To obtain newtons per meter, first use $x=0.20\ \mathrm m$, then divide.
- id: mct-p1-recover-k-c
  content: |-
    $64\ \mathrm{N/m}$
  feedback: |-
    This multiplies the force by $0.20\ \mathrm m$. The spring constant is force per extension, $k=F/x$, not the product $Fx$.
- id: mct-p1-recover-k-d
  content: |-
    $80\ \mathrm{N/m}$
  feedback: |-
    The factor $1/2$ does not belong in the slope of a Hooke's-law graph. It enters the triangular area used for work; stiffness remains $k=F/x$.
- id: mct-p1-recover-k-e
  content: |-
    $6.25\times10^{-4}\ \mathrm{m/N}$
  feedback: |-
    This is the reciprocal $x/F$, called compliance, and its units are meters per newton. Stiffness is the inverse ratio $F/x=1600\ \mathrm{N/m}$.
```

---

<a id="source-video-work"></a>
## Source-Video Problem 2: Force, Stiffness, and Work

The source segment `iubb3eFBQ9U` from 00:08:37–00:13:36 gives one spring data pair:

$$
F_1=200\ \mathrm N,
\qquad
x_1=40\ \mathrm{cm}=0.40\ \mathrm m.
$$

It asks for the endpoint force at $x_2=120\ \mathrm{cm}$, the spring constant, and the work required to reach that extension.

### Endpoint force

The displacement is tripled:

$$
\frac{x_2}{x_1}=\frac{120\ \mathrm{cm}}{40\ \mathrm{cm}}=3.
$$

For the same spring, force magnitude is directly proportional to extension, so

$$
F_2=3F_1=3(200\ \mathrm N)=600\ \mathrm N.
$$

### Spring constant

Use either data pair after converting to meters:

$$
k=\frac{F_1}{x_1}
=\frac{200\ \mathrm N}{0.40\ \mathrm m}
=500\ \mathrm{N/m}.
$$

**Transcript correction.** The captions say that $40\ \mathrm{cm}$ becomes “$4\ \mathrm m$,” but the video frame near 10:36 shows the correct denominator $0.4\ \mathrm m$. The stated $500\ \mathrm{N/m}$ result also requires $0.40\ \mathrm m$.

### Work to $1.20\ \mathrm m$

The shortcut $W=Fx$ applies to a constant force. A spring's required external force rises linearly from $0$ to $kx$ while it is stretched quasistatically:

```text
F
│          ● (x, kx)
│         /|
│        / |
│       /  |    work = triangular area
│      /   |         = 1/2 (x)(kx)
│     /    |
└──────────┴──────── x
0          x
```

Therefore,

$$
W_{\mathrm{req}}
=\int_0^x kx'\,dx'
=\frac12kx^2.
$$

The graph gives the same result without making integration a separate lesson: work is the triangular area under the force–extension line. With $x=120\ \mathrm{cm}=1.20\ \mathrm m$,

$$
\begin{aligned}
W_{\mathrm{req}}
&=\frac12(500\ \mathrm{N/m})(1.20\ \mathrm m)^2\\
&=360\ \mathrm{N\,m}\\
&=360\ \mathrm J.
\end{aligned}
$$

Equivalently, the average required force over this interval is half the endpoint force:

$$
F_{\mathrm{avg}}=\frac{0+600}{2}=300\ \mathrm N,
$$

$$
W_{\mathrm{req}}=F_{\mathrm{avg}}x
=(300\ \mathrm N)(1.20\ \mathrm m)
=360\ \mathrm J.
$$

Using the endpoint force for the entire distance would give $Fx=(600)(1.20)=720\ \mathrm J$, twice the correct work.

**Caption clarification.** At 12:13–12:34, the transcript renders “one-half” as “12.” The frame and derivation show $\tfrac12kx^2$.

Thus the second source problem gives

$$
\boxed{F(1.20\ \mathrm m)=600\ \mathrm N},
\qquad
\boxed{k=500\ \mathrm{N/m}},
\qquad
\boxed{W_{\mathrm{req}}=360\ \mathrm J}.
$$

```quiz
type: radio
id: mct-p1-force-versus-work
shuffle: true
content: |-
  A force of $150\ \mathrm N$ stretches an ideal spring from equilibrium to $25\ \mathrm{cm}$. How much work is required for this stretch?
options:
- id: mct-p1-force-versus-work-a
  content: |-
    $18.75\ \mathrm J$
  correct: true
  feedback: |-
    The required force rises linearly from $0$ to $150\ \mathrm N$, so its average is $75\ \mathrm N$. With $x=0.25\ \mathrm m$, $W=F_{\mathrm{avg}}x=(75)(0.25)=18.75\ \mathrm J$.
- id: mct-p1-force-versus-work-b
  content: |-
    $37.5\ \mathrm J$
  feedback: |-
    This uses the final $150\ \mathrm N$ over the entire $0.25\ \mathrm m$. The spring force ramps from zero, so the average force is half the endpoint value and the work is half this result.
- id: mct-p1-force-versus-work-c
  content: |-
    $600\ \mathrm J$
  feedback: |-
    This is the spring constant $k=F/x=150/0.25=600\ \mathrm{N/m}$ with energy units attached. Stiffness is not work; substitute it into $W=\tfrac12kx^2$.
- id: mct-p1-force-versus-work-d
  content: |-
    $9.375\ \mathrm J$
  feedback: |-
    This applies the factor $1/2$ twice. The triangular-area formula $W=\tfrac12Fx$ already accounts for the force rising from zero to its endpoint value.
- id: mct-p1-force-versus-work-e
  content: |-
    $3750\ \mathrm J$
  feedback: |-
    This multiplies by the numerical value $25$ before converting centimeters. Work in joules requires meters: $25\ \mathrm{cm}=0.25\ \mathrm m$.
```

---

<a id="lecture-transfer"></a>
## Lecture Transfer: Spring Potential Energy

The M4-1 lecture notes keep the restoring-force sign in

$$
F_s=-kx
$$

and relate force to potential energy through

$$
F_s=-\frac{dU}{dx}.
$$

It follows that

$$
\frac{dU}{dx}=kx,
$$

so, taking $U=0$ at $x=0$,

$$
\boxed{U_s(x)=\frac12kx^2}.
$$

For a slow stretch or compression from equilibrium with no change in kinetic energy, the external work becomes spring potential energy:

$$
W_{\mathrm{ext}}=\Delta U_s=\frac12kx^2.
$$

Because $x$ is squared, equal-magnitude stretches and compressions store the same energy. Their restoring forces point in opposite directions, but their endpoint force magnitudes are both $k|x|$.

```quiz
type: radio
id: mct-p1-stretch-compress
shuffle: true
content: |-
  An ideal spring is slowly moved from equilibrium first to $x=+0.20\ \mathrm m$ and, in a separate trial, to $x=-0.20\ \mathrm m$. Which comparison is correct?
options:
- id: mct-p1-stretch-compress-a
  content: |-
    The restoring forces point in opposite directions, while the force magnitudes and stored energies are equal.
  correct: true
  feedback: |-
    Hooke's law $F_s=-kx$ reverses the force direction when $x$ changes sign. The magnitudes $k|x|$ are equal, and $U_s=\tfrac12kx^2$ gives the same stored energy for $+0.20\ \mathrm m$ and $-0.20\ \mathrm m$.
- id: mct-p1-stretch-compress-b
  content: |-
    The restoring forces and stored energies both change sign.
  feedback: |-
    Restoring force is signed because it has direction, but stored elastic energy depends on $x^2$ and is nonnegative relative to the equilibrium reference. Only the force reverses sign.
- id: mct-p1-stretch-compress-c
  content: |-
    The restoring forces point in the same direction, while the stored energies are equal.
  feedback: |-
    The energy comparison is right, but $F_s=-kx$ points left for positive displacement and right for negative displacement. The forces point toward equilibrium from opposite sides.
- id: mct-p1-stretch-compress-d
  content: |-
    Compression stores no energy because $x<0$.
  feedback: |-
    The sign of $x$ sets the force direction; it does not remove stored energy. Squaring the compression gives $U_s=\tfrac12k(-0.20)^2=\tfrac12k(0.20)^2$.
- id: mct-p1-stretch-compress-e
  content: |-
    Stretching stores twice as much energy as equal-magnitude compression.
  feedback: |-
    The ideal spring model is symmetric about equilibrium. Equal $|x|$ gives equal $x^2$, so extension and compression store the same energy within Hooke's-law range.
```

---

<a id="summary"></a>
## Summary

- Measure $x$ from the spring's unstretched equilibrium and use units compatible with $k$. For $k$ in $\mathrm{N/m}$, convert centimeters to meters.
- The spring's signed restoring force is
  $$
  F_s=-kx.
  $$
  A required external holding-force magnitude is $F_{\mathrm{req}}=k|x|$.
- If $k$ is unknown, a nonzero Hooke's-law data pair gives
  $$
  k=\frac{F}{|x|}.
  $$
- For the same spring, $F\propto|x|$. A force ratio produces the same displacement-magnitude ratio.
- Endpoint force and work are different. Use
  $$
  F_{\mathrm{req}}=k|x|
  $$
  for the force at one displacement, but
  $$
  W_{\mathrm{req}}=\frac12kx^2
  $$
  for a slow stretch or compression from equilibrium.
- The factor $1/2$ is the triangular area under the linear force–extension graph. Using the endpoint force in $Fx$ makes the work twice too large.
- The same expression gives stored spring energy:
  $$
  U_s=\frac12kx^2.
  $$

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../Study-Guide.md)

---
<!-- lesson-nav:end -->
