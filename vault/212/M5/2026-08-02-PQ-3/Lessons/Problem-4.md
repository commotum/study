# Deriving Wave Speed on a Load-Bearing Wire

<!--
lesson-id: 212-M5-048
topic-code: MTH212.M5.48
-->

## Table of Contents

- [Introduction](#introduction)
- [Transfer the Hanging Load to the Shelf](#transfer-the-hanging-load-to-the-shelf)
- [Use Torque Balance to Find the Wire Tension](#use-torque-balance-to-find-the-wire-tension)
- [Use the Wire Geometry to Find Linear Density](#use-the-wire-geometry-to-find-linear-density)
- [Combine the Static and Wave Models](#combine-the-static-and-wave-models)
- [Separate Medium Data from Wave Data](#separate-medium-data-from-wave-data)
- [Summary](#summary)

## Prerequisites

- Draw free-body and extended free-body diagrams.
- Use $\sum\tau=0$ for static equilibrium.
- Use $\tau=rF\sin\phi$ and the center of mass of a uniform shelf.
- Use right-triangle trigonometry and $\mu=m/L$.
- Recognize $v=\sqrt{T/\mu}$ for a transverse wave on a taut wire.

---

<a id="introduction"></a>
## Introduction

When a support wire also carries a traveling wave, its wave speed comes from the wire's **tension** and **linear mass density**:

$$
v=\sqrt{\frac{T}{\mu}}.
$$

The recognition cue is that neither $T$ nor $\mu$ is given directly. The static shelf determines $T$, while the wire's mass and geometry determine $\mu$.

Use this chain:

$$
\text{free-body diagrams}
\longrightarrow T
\longrightarrow L_w
\longrightarrow \mu
\longrightarrow v.
$$

At each stage, name the quantity you are trying to find, write the relationship that contains it, and then isolate it:

$$
\begin{aligned}
T &: &&\sum \tau_{\text{hinge}}=0,\\
L_w &: &&\cos\theta=\frac{L}{L_w},\\
\mu &: &&\mu=\frac{m_w}{L_w},\\
v &: &&v=\sqrt{\frac{T}{\mu}}.
\end{aligned}
$$

This lesson uses the model stated by the problem: the wire is straight, its tension is treated as uniform, and its mass enters through its linear density.

---

<a id="transfer-the-hanging-load-to-the-shelf"></a>
## Transfer the Hanging Load to the Shelf

**Example:** A stationary block of mass $m_2$ hangs from a massless vertical string attached to the end of a shelf. What downward force does that string exert on the shelf?

**Explanation**

The block has upward string tension $T_s$ and downward weight $m_2g$. Because the block is stationary,

$$
\sum F_y=0
\quad\Longrightarrow\quad
T_s-m_2g=0,
$$

so

$$
T_s=m_2g.
$$

By Newton's third law, the same string pulls **downward** on the shelf with magnitude $m_2g$. Keep this string tension $T_s$ distinct from the diagonal support-wire tension $T$.

![](<../Source/PQ3/Images/shelf-block-free-body-diagrams.png>)

```quiz
type: radio
id: pq3-p4-q1
content: |-
  A stationary block of mass $m$ hangs from a massless vertical string attached to the end of a shelf. Which force from the string belongs on the shelf's extended free-body diagram?
options:
- id: q1-a
  content: |-
    An upward force $mg$ at the shelf's end
  feedback: |-
    This reverses the Newton's-third-law pair. The string pulls upward on the block, but the force asked for is the string's force on the shelf, which points downward at the attachment point.
- id: q1-b
  content: |-
    A downward force $mg$ at the shelf's end
  correct: true
  feedback: |-
    Because the block is stationary, the string tension balances its weight, so $T_s=mg$. That same string pulls downward on the shelf at its end with magnitude $mg$.
- id: q1-c
  content: |-
    A downward force $mg/2$ at the shelf's center
  feedback: |-
    The block's full weight is transmitted as string tension, not halved. This force acts where the string attaches at the end; the force at the shelf's center is the shelf's own weight.
- id: q1-d
  content: |-
    No force, because the block is stationary
  feedback: |-
    Stationary means the block's net force is zero, not that each force is zero. Its weight is balanced by a nonzero string tension, and the string therefore exerts a downward force on the shelf.
```

---

<a id="use-torque-balance-to-find-the-wire-tension"></a>
## Use Torque Balance to Find the Wire Tension

**Example:** A uniform shelf has mass $m_1$ and length $L$. A block of mass $m_2$ hangs at its outer end. A support wire pulls at that end with tension $T$ at angle $\theta$ above the shelf. Find $T$.

**Explanation**

Take torques about the wall pivot. The unknown hinge force has zero lever arm, so it produces no torque about that point.

The target variable in this stage is $T$; treat the masses, $g$, $L$, and $\theta$ as known constants while isolating it.

The support wire contributes only its component perpendicular to the shelf, $T\sin\theta$. The shelf's weight acts at $L/2$, and the hanging load acts at $L$:

$$
TL\sin\theta-m_1g\frac{L}{2}-m_2gL=0.
$$

Cancel $L$ and solve for $T$:

$$
T\sin\theta=\frac{m_1g}{2}+m_2g,
$$

$$
T=\frac{(m_1+2m_2)g}{2\sin\theta}.
$$

```quiz
type: radio
id: pq3-p4-q2
content: |-
  A uniform shelf of mass $M$ supports a hanging mass $m$ at its end. A wire attached at the same end makes angle $\alpha$ above the shelf. Which expression gives the wire tension?
options:
- id: q2-a
  content: |-
    $\dfrac{(M+2m)g}{2\sin\alpha}$
  correct: true
  feedback: |-
    About the hinge, only the wire's perpendicular component $T\sin\alpha$ produces its counterclockwise torque. Balancing it against the shelf weight at $L/2$ and the hanging weight at $L$ gives $TL\sin\alpha=Mg(L/2)+mgL$, so $T=(M+2m)g/(2\sin\alpha)$.
- id: q2-b
  content: |-
    $\dfrac{(M+m)g}{\sin\alpha}$
  feedback: |-
    This gives both weights the full lever arm $L$. A uniform shelf's weight acts at its center, so its torque uses $L/2$; only the hanging mass uses $L$.
- id: q2-c
  content: |-
    $\dfrac{(M+2m)g}{2\cos\alpha}$
  feedback: |-
    This uses the component of tension parallel to the shelf. A parallel force has no torque about the hinge; the perpendicular component is $T\sin\alpha$, so the denominator must contain $\sin\alpha$.
- id: q2-d
  content: |-
    $\dfrac{(2M+m)g}{2\sin\alpha}$
  feedback: |-
    This gives the half-length lever arm to the wrong mass. The shelf's weight $Mg$ acts at $L/2$, while the hanging weight $mg$ acts at $L$, producing the mass combination $M/2+m$, not $M+m/2$.
```

---

<a id="use-the-wire-geometry-to-find-linear-density"></a>
## Use the Wire Geometry to Find Linear Density

**Example:** The shelf's horizontal length is $L$. The support wire makes angle $\theta$ with the shelf and has mass $m_w$. Find the wire's linear mass density.

**Explanation**

The wire is the hypotenuse of a right triangle whose adjacent horizontal side is $L$. Therefore,

$$
\cos\theta=\frac{L}{L_w}
\quad\Longrightarrow\quad
L_w=\frac{L}{\cos\theta}.
$$

For a uniform wire,

$$
\mu=\frac{m_w}{L_w}
=\frac{m_w}{L/\cos\theta}
=\frac{m_w\cos\theta}{L}.
$$

The common trap is to use the shelf length $L$ as though it were the wire length.

```quiz
type: radio
id: pq3-p4-q3
content: |-
  A straight wire of mass $m$ spans a horizontal distance $d$ while making angle $\beta$ with the horizontal. What is its linear mass density?
options:
- id: q3-a
  content: |-
    $\dfrac{m}{d}$
  feedback: |-
    This treats the horizontal span $d$ as the wire's full length. The slanted wire is the hypotenuse, $L_w=d/\cos\beta>d$, so its density is smaller than $m/d$.
- id: q3-b
  content: |-
    $\dfrac{m}{d\cos\beta}$
  feedback: |-
    This divides by $d\cos\beta$, which would make the wire shorter than its horizontal span. The wire length is $d/\cos\beta$, so dividing $m$ by that length multiplies by $\cos\beta$.
- id: q3-c
  content: |-
    $\dfrac{m\cos\beta}{d}$
  correct: true
  feedback: |-
    The wire is the hypotenuse, so its length is $L_w=d/\cos\beta$. Linear density is mass per actual wire length; therefore $\mu=m/L_w=m\cos\beta/d$.
- id: q3-d
  content: |-
    $\dfrac{m\sin\beta}{d}$
  feedback: |-
    The known horizontal span $d$ is adjacent to $\beta$, so it is related to the hypotenuse by cosine. Sine would be appropriate if the vertical rise, rather than the horizontal span, were given.
```

---

<a id="combine-the-static-and-wave-models"></a>
## Combine the Static and Wave Models

**Example:** A block of mass $m_2$ hangs from the end of a uniform shelf of mass $m_1$ and length $L$. A uniform support wire of mass $m_w$ makes angle $\theta$ with the shelf. Find the speed of a traveling transverse wave on the wire.

![](<../Source/PQ3/Images/shelf-block-support-wire.png>)

**Explanation**

The static-equilibrium result is

$$
T=\frac{(m_1+2m_2)g}{2\sin\theta},
$$

and the wire-geometry result is

$$
\mu=\frac{m_w\cos\theta}{L}.
$$

Substitute both into $v=\sqrt{T/\mu}$:

$$
v
=\sqrt{
\frac{(m_1+2m_2)g}{2\sin\theta}
\frac{L}{m_w\cos\theta}
}.
$$

Thus,

$$
\boxed{
v=\sqrt{
\frac{(m_1+2m_2)gL}
{2m_w\cos\theta\sin\theta}
}
}.
$$

A unit check confirms that this expression has the dimensions of speed. The trigonometric factors and the factor of $2$ are dimensionless, while

$$
\frac{(\mathrm{kg})(\mathrm{m/s^2})(\mathrm{m})}{\mathrm{kg}}
=\frac{\mathrm{m^2}}{\mathrm{s^2}}.
$$

Taking the square root gives $\mathrm{m/s}$. The formula also has the expected trends: more supported mass raises the tension and the wave speed, while more wire mass raises $\mu$ and lowers the speed.

```quiz
type: radio
id: pq3-p4-q4
content: |-
  A $4.0\ \mathrm{kg}$ uniform shelf is $3.0\ \mathrm{m}$ long and supports a $2.0\ \mathrm{kg}$ block at its end. A $1.5\ \mathrm{kg}$ support wire makes a $30^\circ$ angle with the shelf. Using $g=9.8\ \mathrm{m/s^2}$, what is the traveling-wave speed on the wire?
options:
- id: q4-a
  content: |-
    $6.7\ \mathrm{m/s}$
  feedback: |-
    This value does not follow from the tension and density of the given wire. Torque balance gives $T=78.4\ \mathrm{N}$ and the slanted length gives $\mu=0.433\ \mathrm{kg/m}$; their ratio must then be square-rooted, giving $13.5\ \mathrm{m/s}$.
- id: q4-b
  content: |-
    $9.8\ \mathrm{m/s}$
  feedback: |-
    This reuses the numerical value of $g$, but acceleration due to gravity is not the wave speed. Gravity helps determine the wire tension; the requested speed is then $v=\sqrt{T/\mu}=13.5\ \mathrm{m/s}$.
- id: q4-c
  content: |-
    $13.5\ \mathrm{m/s}$
  correct: true
  feedback: |-
    The shelf and block set the support tension: $T=78.4\ \mathrm{N}$. The wire's actual slanted length sets $\mu=(1.5\cos30^\circ)/3.0=0.433\ \mathrm{kg/m}$, so $v=\sqrt{T/\mu}=13.5\ \mathrm{m/s}$.
- id: q4-d
  content: |-
    $19.6\ \mathrm{m/s}$
  feedback: |-
    This is larger than $\sqrt{T/\mu}$ for the stated wire. The wire is longer than the shelf, so $\mu=m_w\cos30^\circ/L=0.433\ \mathrm{kg/m}$; using $T=78.4\ \mathrm{N}$ gives $13.5\ \mathrm{m/s}$, not $19.6\ \mathrm{m/s}$.
```

---

<a id="separate-medium-data-from-wave-data"></a>
## Separate Medium Data from Wave Data

**Example:** The support wire is plucked with amplitude $A$ and wavelength $\lambda$. Are either needed to determine the speed once $T$ and $\mu$ are known?

**Explanation**

No. For the ideal traveling-wave model,

$$
v=\sqrt{\frac{T}{\mu}}.
$$

The amplitude does not set the wave speed. Wavelength can be used with frequency through $v=f\lambda$, but neither one is needed when the properties of the medium already determine $v$.

The statement that there are no reflections also tells you not to impose standing-wave conditions such as $L_w=n\lambda/2$.

```quiz
type: radio
id: pq3-p4-q5
content: |-
  In the ideal traveling-wave model, which change increases the wave speed on a given wire while its linear density stays fixed?
options:
- id: q5-a
  content: |-
    Doubling the wave amplitude
  feedback: |-
    Amplitude controls the wave's displacement scale and, in the ideal model, its energy and power. Speed is controlled by the medium through $v=\sqrt{T/\mu}$, so doubling amplitude leaves it unchanged.
- id: q5-b
  content: |-
    Doubling the wavelength while leaving the medium unchanged
  feedback: |-
    Wavelength does not set the speed of an unchanged nondispersive wire. Its frequency adjusts so that $f\lambda=\sqrt{T/\mu}$, so doubling $\lambda$ alone does not increase $v$.
- id: q5-c
  content: |-
    Doubling the wire tension
  correct: true
  feedback: |-
    Wave speed on a wire grows with the square root of tension. With $\mu$ fixed, doubling $T$ makes $v'=\sqrt{2T/\mu}=\sqrt2\,v$, so the speed increases.
- id: q5-d
  content: |-
    Shifting the wave's phase by $\pi$
  feedback: |-
    Phase identifies where the oscillation is in its cycle; it does not change the wire's tension or linear density. Shifting phase by $\pi$ therefore leaves $v=\sqrt{T/\mu}$ unchanged.
```

---

<a id="summary"></a>
## Summary

For a load-bearing wire that carries a traveling wave:

1. Use the hanging block's equilibrium to replace its string tension with $m_2g$.
2. Take shelf torques about the hinge to eliminate the hinge force and find
   $$
   T=\frac{(m_1+2m_2)g}{2\sin\theta}.
   $$
3. Use the right triangle to find $L_w=L/\cos\theta$ and then
   $$
   \mu=\frac{m_w\cos\theta}{L}.
   $$
4. Substitute into $v=\sqrt{T/\mu}$.

The main traps are confusing the two tensions, putting the shelf's weight at $L$ instead of $L/2$, using $T$ instead of $T\sin\theta$ in the torque, and using the shelf length instead of the support-wire length in $\mu$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Locate a Listener on a Circular Wavefront](../../2026-07-27-M5-2/Lessons/Problem-4.md)

Study guide index: 13/28

---
<!-- lesson-nav:end -->
