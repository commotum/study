# Resolving a Tilted Support Force in Horizontal Circular Motion

<!--
lesson-id: 212-M1-084
topic-code: MTH212.M1.84
-->

## Table of Contents

- [Introduction](#introduction)
- [Build the Shared Component Equations](#build-the-shared-component-equations)
- [Solve the Frictionless-Bank Design Problem](#solve-the-frictionless-bank-design-problem)
- [Reuse the Geometry for a Tetherball](#reuse-the-geometry-for-a-tetherball)
- [Know When the Tension Approximation Is Safe](#know-when-the-tension-approximation-is-safe)
- [Summary](#summary)

## Prerequisites

- Draw weight, normal force, and tension as real interaction forces.
- Identify opposite, adjacent, and hypotenuse relative to a stated angle.
- Use inverse tangent and the Pythagorean theorem in a right triangle.
- Use $a_r=v^2/r$ for horizontal circular motion.

---

<a id="introduction"></a>
## Introduction

A frictionless banked turn and a tetherball look different, but they give the same force-component problem. In each case:

- weight $mg$ points downward;
- one tilted support force points upward and inward;
- vertical acceleration is zero;
- radial acceleration points horizontally inward.

Call the tilted support magnitude $S$, where $S=N$ for the bank and $S=T_{\mathrm{tens}}$ for the tetherball. If $\theta$ is the angle between $S$ and the vertical, then

$$
S\cos\theta=mg,
\qquad
S\sin\theta=\frac{mv^2}{r}.
$$

Divide the inward equation by the vertical equation:

$$
\frac{S\sin\theta}{S\cos\theta}
=
\frac{mv^2/r}{mg}
\quad\Longrightarrow\quad
\boxed{\tan\theta=\frac{v^2}{rg}}.
$$

The division removes both $S$ and $m$. For either setting, use vertical and inward axes, write the two component equations, and divide them before solving for speed or angle. Do not draw a separate centripetal-force arrow; the inward component $S\sin\theta$ is the real force contribution that produces $mv^2/r$.

---

<a id="build-the-shared-component-equations"></a>
## Build the Shared Component Equations

**Source-video derivation:** A car travels around an icy, frictionless banked curve. The road is banked at angle $\theta$ above horizontal, so the normal force is tilted inward by the same angle $\theta$ from vertical.

**Explanation**

Only two forces act on the car: weight $mg$ downward and normal force $N$ perpendicular to the road. Choose vertical and horizontal-inward axes rather than axes along the road. Then

$$
N_y=N\cos\theta,
\qquad
N_r=N\sin\theta.
$$

Relative to the angle measured from vertical, the vertical component is the adjacent leg of the force triangle and the inward component is the opposite leg. Label those roles before choosing cosine or sine.

The car does not accelerate vertically, so

$$
N\cos\theta-mg=0
\quad\Longrightarrow\quad
\boxed{N=\frac{mg}{\cos\theta}}.
$$

This is not the familiar $N=mg\cos\theta$ from a block resting on an ordinary incline. On that incline, $N$ balances only the component of weight perpendicular to the surface. On the frictionless bank, the **vertical component of $N$** must balance the full weight while the other component points inward. Therefore $N>mg$ whenever $0^\circ<\theta<90^\circ$.

The inward equation is

$$
N\sin\theta=\frac{mv^2}{r}.
$$

Dividing this equation by $N\cos\theta=mg$ gives the shared bank-and-tetherball relation

$$
\tan\theta=\frac{v^2}{rg}.
$$

```quiz
type: radio
id: mct-p10-component-pair
shuffle: true
content: |-
  An object moves in a horizontal circle while one support force $S$ is tilted inward by angle $\theta$ from the vertical. Which pair of equations correctly describes its vertical balance and inward radial motion?
options:
- id: mct-p10-component-pair-a
  content: |-
    $S\cos\theta=mg$ and $S\sin\theta=mv^2/r$
  correct: true
  feedback: |-
    The angle is measured from vertical, so the adjacent component $S\cos\theta$ is vertical and balances weight. The opposite component $S\sin\theta$ points inward and equals the required radial net force $mv^2/r$.
- id: mct-p10-component-pair-b
  content: |-
    $S\sin\theta=mg$ and $S\cos\theta=mv^2/r$
  feedback: |-
    This swaps the components for an angle measured from vertical. The vertical leg is adjacent to $\theta$, so it uses cosine; the inward leg is opposite $\theta$, so it uses sine.
- id: mct-p10-component-pair-c
  content: |-
    $S=mg\cos\theta$ and $S\sin\theta=mv^2/r$
  feedback: |-
    The support magnitude is the hypotenuse of its component triangle, not a component of weight. Vertical balance gives $S\cos\theta=mg$, hence $S=mg/\cos\theta$, while its inward component is $S\sin\theta$.
- id: mct-p10-component-pair-d
  content: |-
    $S\cos\theta-mg=mv^2/r$ and $S\sin\theta=0$
  feedback: |-
    Radial acceleration is horizontal inward, not vertical. The vertical sum is zero, $S\cos\theta-mg=0$, while the nonzero inward component satisfies $S\sin\theta=mv^2/r$.
- id: mct-p10-component-pair-e
  content: |-
    $S\cos\theta=mg$ and $S\sin\theta+F_c=mv^2/r$
  feedback: |-
    This adds a separate centripetal force that is not a physical interaction. The inward component $S\sin\theta$ already supplies the net radial force $mv^2/r$.
```

---

<a id="solve-the-frictionless-bank-design-problem"></a>
## Solve the Frictionless-Bank Design Problem

**Source-video worked problem 1(a):** A frictionless curve has radius $r=200\,\mathrm m$ and bank angle $\theta=15^\circ$. Find the speed at which a car does not slide up or down the bank. Use $g=9.8\,\mathrm{m/s^2}$.

**Explanation**

The two force equations are

$$
N\cos\theta=mg,
\qquad
N\sin\theta=\frac{mv^2}{r}.
$$

Divide them and solve for speed:

$$
\begin{aligned}
\tan\theta&=\frac{v^2}{rg},\\
v^2&=rg\tan\theta,\\
v&=\sqrt{rg\tan\theta}.
\end{aligned}
$$

Substitute the source values:

$$
\begin{aligned}
v
&=\sqrt{(200\,\mathrm m)(9.8\,\mathrm{m/s^2})\tan15^\circ}\\
&=22.9168\,\mathrm{m/s}\\
&\approx\boxed{22.9\,\mathrm{m/s}}.
\end{aligned}
$$

This is the frictionless **design speed**. The car's mass cancels because both the vertical balance and radial requirement scale with $m$.

**Source-video worked problem 1(b):** Keep $r=200\,\mathrm m$, but require the design speed to be $30\,\mathrm{m/s}$. Find the bank angle.

Rearrange before substituting:

$$
\boxed{\theta=\tan^{-1}\left(\frac{v^2}{rg}\right)}.
$$

The video reports $24.62^\circ$ and then rounds the design angle to $24.7^\circ$. Evaluating its displayed numbers gives

$$
\theta
=\tan^{-1}\left(\frac{30^2}{(200)(9.8)}\right)
=24.6638\ldots^\circ
\approx24.7^\circ.
$$

The reported $24.62^\circ$ is not the direct evaluation of the displayed inputs, but the video's final one-decimal result is consistent with them.

Choose the final equation from the requested unknown:

$$
\text{speed target: }v=\sqrt{rg\tan\theta},
\qquad
\text{angle target: }\theta=\tan^{-1}\left(\frac{v^2}{rg}\right).
$$

Use degree mode for the trigonometric calculation and keep guard digits until the final rounding step.

At 14:18, the source reverses the high-speed direction once. Relative to the $22.9\,\mathrm{m/s}$ design speed:

- a faster car, including one traveling at $30$ or $50\,\mathrm{m/s}$, tends **up the bank and outward**;
- a slower car, such as one traveling at $15\,\mathrm{m/s}$, tends **down the bank and inward**.

The source briefly says that $50\,\mathrm{m/s}$ would tend down the bank, contradicting both its earlier explanation and the force requirement. The comparison here identifies only the direction of the no-friction sliding tendency.

```quiz
type: radio
id: mct-p10-banked-speed
shuffle: true
content: |-
  An icy frictionless curve has radius $80.0\,\mathrm m$ and bank angle $20.0^\circ$. Using $g=9.8\,\mathrm{m/s^2}$, what is its design speed?
options:
- id: mct-p10-banked-speed-a
  content: |-
    $16.9\,\mathrm{m/s}$
  correct: true
  feedback: |-
    Dividing the inward and vertical equations gives $v=\sqrt{rg\tan\theta}$. Thus $v=\sqrt{(80.0)(9.8)\tan20.0^\circ}=16.9\,\mathrm{m/s}$; mass and the normal-force magnitude cancel.
- id: mct-p10-banked-speed-b
  content: |-
    $285\,\mathrm{m/s}$
  feedback: |-
    The value $rg\tan\theta=285$ has units of $\mathrm{m^2/s^2}$ and equals $v^2$, not $v$. Taking its square root gives $16.9\,\mathrm{m/s}$.
- id: mct-p10-banked-speed-c
  content: |-
    $46.4\,\mathrm{m/s}$
  feedback: |-
    This inverts the tangent factor and uses $\sqrt{rg/\tan\theta}$. Dividing the component equations gives $v^2/(rg)=\tan\theta$, so tangent belongs in the numerator.
- id: mct-p10-banked-speed-d
  content: |-
    $8.45\,\mathrm{m/s}$
  feedback: |-
    This divides the correct result by two, but no factor of two appears in the component equations. The radial acceleration is $v^2/r$, and solving $v^2=rg\tan\theta$ requires only the square root.
- id: mct-p10-banked-speed-e
  content: |-
    The speed cannot be found without the car's mass.
  feedback: |-
    Mass appears in both $N\cos\theta=mg$ and $N\sin\theta=mv^2/r$. Dividing the equations cancels both $N$ and $m$, leaving a design speed determined by $r$, $g$, and $\theta$.
```

```quiz
type: radio
id: mct-p10-banked-angle
shuffle: true
content: |-
  A frictionless banked curve has radius $150\,\mathrm m$ and design speed $25.0\,\mathrm{m/s}$. Using $g=9.8\,\mathrm{m/s^2}$, what bank angle is required?
options:
- id: mct-p10-banked-angle-a
  content: |-
    $23.0^\circ$
  correct: true
  feedback: |-
    For an angle target, use $\theta=\tan^{-1}(v^2/(rg))$ in degree mode. Here $\theta=\tan^{-1}(25.0^2/((150)(9.8)))=\tan^{-1}(0.42517)=23.0^\circ$.
- id: mct-p10-banked-angle-b
  content: |-
    $0.425^\circ$
  feedback: |-
    The value $0.425$ is the dimensionless tangent ratio $v^2/(rg)$, not the angle. Apply inverse tangent in degree mode to that ratio to obtain $23.0^\circ$.
- id: mct-p10-banked-angle-c
  content: |-
    $67.0^\circ$
  feedback: |-
    This uses the reciprocal ratio $rg/v^2$ and produces the complementary angle. The bank angle satisfies $\tan\theta=v^2/(rg)$, so the required angle is $23.0^\circ$.
- id: mct-p10-banked-angle-d
  content: |-
    $0.974^\circ$
  feedback: |-
    This uses $v$ instead of $v^2$ in the tangent ratio. Radial acceleration depends on speed squared, so the numerator must be $(25.0)^2=625$.
- id: mct-p10-banked-angle-e
  content: |-
    $76.5^\circ$
  feedback: |-
    This omits $g$ from the denominator and applies inverse tangent to $v^2/r$. The dimensionless ratio is $v^2/(rg)$; including $g$ gives $23.0^\circ$.
```

---

<a id="reuse-the-geometry-for-a-tetherball"></a>
## Reuse the Geometry for a Tetherball

**Source-video worked problem 1(a-b):** A $2\,\mathrm{kg}$ tetherball moves in a horizontal circle of radius $1.5\,\mathrm m$ at $3.5\,\mathrm{m/s}$. Find the angle the rope makes with the vertical and the total tension.

**Explanation**

Only weight and rope tension act on the ball. With $\theta$ measured from vertical, resolve the tension into an inward component $T_r$ and an upward component $T_y$:

$$
T_r=\frac{mv^2}{r},
\qquad
T_y=mg.
$$

For the source values,

$$
\begin{aligned}
T_r
&=\frac{(2)(3.5)^2}{1.5}
=16.33\,\mathrm N,\\
T_y
&=(2)(9.8)
=19.6\,\mathrm N.
\end{aligned}
$$

Because the angle is measured from vertical,

$$
\tan\theta=\frac{T_r}{T_y}
=\frac{16.33}{19.6},
$$

so

$$
\boxed{\theta=\tan^{-1}\left(\frac{16.33}{19.6}\right)=39.8^\circ}.
$$

The total tension is the hypotenuse of the component triangle:

$$
\begin{aligned}
T_{\mathrm{tens}}
&=\sqrt{T_r^2+T_y^2}\\
&=\sqrt{(16.33)^2+(19.6)^2}\\
&=\boxed{25.51\,\mathrm N}.
\end{aligned}
$$

Take the positive square root because tension here is a magnitude. The same value follows from $T_{\mathrm{tens}}=mg/\cos\theta$. The quantity $T_r=mv^2/r$ is one component of tension, not a second centripetal force.

```quiz
type: radio
id: mct-p10-tetherball-mirrored
shuffle: true
content: |-
  A $1.50\,\mathrm{kg}$ tetherball moves in a horizontal circle of radius $0.800\,\mathrm m$ at $4.00\,\mathrm{m/s}$. Using $g=9.8\,\mathrm{m/s^2}$, which pair gives the rope's angle from vertical and its total tension?
options:
- id: mct-p10-tetherball-mirrored-a
  content: |-
    $\theta=63.9^\circ$ and $T_{\mathrm{tens}}=33.4\,\mathrm N$
  correct: true
  feedback: |-
    The inward and vertical components are $T_r=mv^2/r=30.0\,\mathrm N$ and $T_y=mg=14.7\,\mathrm N$. Thus $\theta=\tan^{-1}(30.0/14.7)=63.9^\circ$ from vertical and $T_{\mathrm{tens}}=\sqrt{30.0^2+14.7^2}=33.4\,\mathrm N$.
- id: mct-p10-tetherball-mirrored-b
  content: |-
    $\theta=26.1^\circ$ and $T_{\mathrm{tens}}=33.4\,\mathrm N$
  feedback: |-
    The tension magnitude is correct, but $26.1^\circ$ is the complementary angle measured from horizontal. The prompt measures from vertical, so use $\tan\theta=T_r/T_y$ to obtain $63.9^\circ$.
- id: mct-p10-tetherball-mirrored-c
  content: |-
    $\theta=63.9^\circ$ and $T_{\mathrm{tens}}=30.0\,\mathrm N$
  feedback: |-
    The value $30.0\,\mathrm N$ is only the inward component $mv^2/r$. Total tension must also have the $14.7\,\mathrm N$ upward component, so its magnitude is $\sqrt{30.0^2+14.7^2}=33.4\,\mathrm N$.
- id: mct-p10-tetherball-mirrored-d
  content: |-
    $\theta=63.9^\circ$ and $T_{\mathrm{tens}}=44.7\,\mathrm N$
  feedback: |-
    This adds perpendicular components as scalars, $30.0+14.7$. Tension is the hypotenuse of the component triangle, so combine the components with the Pythagorean theorem instead.
- id: mct-p10-tetherball-mirrored-e
  content: |-
    $\theta=45.0^\circ$ and $T_{\mathrm{tens}}=14.7\,\mathrm N$
  feedback: |-
    A $45^\circ$ angle would require equal inward and vertical components, but here $30.0\,\mathrm N\ne14.7\,\mathrm N$. The value $14.7\,\mathrm N$ is only the vertical component that balances weight, not the total tension.
```

**Source-video continuation:** The video continues by finding $T_{\mathrm{period}}=2.69\,\mathrm s$ and $f=0.371\,\mathrm{Hz}$. Those calculations appear in [Period, Frequency, and Angular Speed](MCT-Problem-3.md); they are not used in this tilted-force lesson.

---

<a id="know-when-the-tension-approximation-is-safe"></a>
## Know When the Tension Approximation Is Safe

**Source-video approximation:** For a fast tetherball whose rope is nearly horizontal, the video approximates total tension with $mv^2/r$.

**Explanation**

The exact magnitude is

$$
T_{\mathrm{tens}}
=\sqrt{\left(\frac{mv^2}{r}\right)^2+(mg)^2}.
$$

The approximation

$$
T_{\mathrm{tens}}\approx\frac{mv^2}{r}
$$

is justified only when

$$
\frac{mv^2}{r}\gg mg
\quad\Longleftrightarrow\quad
\frac{v^2}{r}\gg g.
$$

Then the inward component is much larger than the vertical component and $\theta$ is close to $90^\circ$ from vertical. The source's $3.5\,\mathrm{m/s}$ tetherball does not satisfy that condition: $T_r=16.33\,\mathrm N$ is smaller than $T_y=19.6\,\mathrm N$, and replacing $25.51\,\mathrm N$ by $16.33\,\mathrm N$ would be a large underestimate.

```quiz
type: radio
id: mct-p10-tension-approximation
shuffle: true
content: |-
  A conical pendulum has inward tension component $T_r=196\,\mathrm N$ and vertical component $T_y=19.6\,\mathrm N$. Which statement correctly assesses the approximation $T_{\mathrm{tens}}\approx T_r$?
options:
- id: mct-p10-tension-approximation-a
  content: |-
    It is reasonable: $T_r$ is ten times $T_y$, and the exact magnitude is about $197\,\mathrm N$.
  correct: true
  feedback: |-
    The approximation applies when the inward component dominates the vertical component. Here $\sqrt{196^2+19.6^2}=196.98\,\mathrm N$, so using $196\,\mathrm N$ is low by only about $0.5\%$.
- id: mct-p10-tension-approximation-b
  content: |-
    It is never reasonable unless $T_y=0$.
  feedback: |-
    An approximation need not make the smaller component exactly zero. It is accurate when $T_y/T_r$ is small; here that ratio is $0.10$, and the exact magnitude differs from $T_r$ by only about $1\,\mathrm N$.
- id: mct-p10-tension-approximation-c
  content: |-
    It is reasonable because the exact magnitude is $196+19.6=215.6\,\mathrm N$.
  feedback: |-
    The components are perpendicular, so they do not add as scalars. The exact magnitude is $\sqrt{196^2+19.6^2}=196.98\,\mathrm N$, which is why $T_r$ alone is a close approximation.
- id: mct-p10-tension-approximation-d
  content: |-
    It is not reasonable because the exact magnitude is $\sqrt{196^2-19.6^2}$.
  feedback: |-
    The total tension is the hypotenuse of a right triangle, so the component squares add rather than subtract. That gives $196.98\,\mathrm N$, close to the $196\,\mathrm N$ inward component.
- id: mct-p10-tension-approximation-e
  content: |-
    It is reasonable because the string angle must be close to $0^\circ$ from vertical.
  feedback: |-
    A dominant inward component makes the string nearly horizontal, so its angle from vertical is close to $90^\circ$, not $0^\circ$. The approximation is justified by $T_r\gg T_y$, not by a nearly vertical string.
```

---

<a id="summary"></a>
## Summary

When one tilted support force holds an object up and bends its path into a horizontal circle:

1. Draw only weight and the real tilted support force.
2. Use vertical and horizontal-inward axes.
3. If $\theta$ is measured from vertical, write $S\cos\theta=mg$ and $S\sin\theta=mv^2/r$.
4. Divide the equations to obtain $\tan\theta=v^2/(rg)$.
5. Solve $v=\sqrt{rg\tan\theta}$ for design speed or $\theta=\tan^{-1}(v^2/(rg))$ for angle.
6. For a tetherball, recover total tension from $T_{\mathrm{tens}}=\sqrt{T_r^2+T_y^2}$.

The main traps are swapping sine and cosine when the angle is measured from vertical, using $N=mg\cos\theta$ for a banked curve, drawing an extra centripetal-force arrow, and replacing total tension by $mv^2/r$ when weight is not negligible.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
