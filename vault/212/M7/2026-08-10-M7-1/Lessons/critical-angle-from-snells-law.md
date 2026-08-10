# Critical Angle from Snell's Law

<!--
lesson-id: 212-M7-015
topic-code: MTH212.M7.15
-->

## Table of Contents

- [Introduction](#introduction)
- [Recognize When a Critical Angle Exists](#recognize-when-a-critical-angle-exists)
- [Derive the Critical-Angle Formula](#derive-the-critical-angle-formula)
- [Evaluate the Inverse Sine in Degrees](#evaluate-the-inverse-sine-in-degrees)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Apply Snell's law, $n_1\sin\theta_1=n_2\sin\theta_2$.
- Measure ray angles from the normal to the boundary.
- Use $\sin90^\circ=1$.
- Evaluate an inverse sine with a calculator in degree mode.

---

<a id="introduction"></a>
## Introduction

Total internal reflection can occur when light tries to cross from a higher-index medium into a lower-index medium. As the incident angle increases, the transmitted ray bends farther from the normal. At one special incident angle, the transmitted ray just follows the boundary:

$$
\theta_2=90^\circ.
$$

That incident angle is the **critical angle** $\theta_c$.

The source represents the limiting geometry this way:

![[../Source/Images/totalinternalreflection.jpg]]

Read every angle relative to the dashed normal:

- $\theta_1$ is the incident angle in medium 1,
- at the limiting case, $\theta_1=\theta_c$,
- $\theta_2$ is the transmitted angle in medium 2, and
- at the limiting case, $\theta_2=90^\circ$ because the transmitted ray lies along the surface.

The recognition cue is the phrase **critical angle** together with light traveling from $n_1$ into a smaller $n_2$. The calculation is

$$
n_1\sin\theta_c=n_2\sin90^\circ
\qquad\Longrightarrow\qquad
\theta_c=\sin^{-1}\left(\frac{n_2}{n_1}\right),
$$

provided that $n_1>n_2$.

---

<a id="recognize-when-a-critical-angle-exists"></a>
## Recognize When a Critical Angle Exists

**Example:** Can light traveling from a medium with $n_1=1.60$ into a medium with $n_2=1.20$ reach a critical angle?

**Explanation**

Yes. The light starts in the higher-index medium:

$$
n_1=1.60>1.20=n_2.
$$

Snell's law then allows the transmitted ray to bend away from the normal until its angle reaches $90^\circ$. If the direction were reversed, the transmitted ray would bend toward the normal and could not reach $90^\circ$.

The ratio test says the same thing:

$$
\sin\theta_c=\frac{n_2}{n_1}.
$$

An inverse sine requires a ratio between $0$ and $1$. This happens here because $n_2<n_1$.

```quiz
type: radio
id: critical-angle-existence-condition
shuffle: true
content: |-
  In which situation can a critical angle and total internal reflection occur?
options:
- id: high-to-low-index
  content: |-
    Light travels from $n_1=1.50$ into $n_2=1.00$.
  correct: true
  feedback: |-
    A critical angle requires light to start in the higher-index medium. Here $n_1>n_2$, so the ray can bend away from the normal until the transmitted angle reaches $90^\circ$.
- id: low-to-high-index
  content: |-
    Light travels from $n_1=1.00$ into $n_2=1.50$.
  feedback: |-
    Moving into the higher-index medium bends the ray toward the normal. The ratio $n_2/n_1=1.50$ also lies outside the sine range, confirming that no critical angle exists in this direction.
- id: equal-index
  content: |-
    Light crosses between two media that both have $n=1.40$.
  feedback: |-
    Equal indices do not bend the transmitted ray away from the normal. Snell's law gives the same angle on both sides, so there is no finite incident angle below $90^\circ$ that creates the critical geometry.
- id: either-direction
  content: |-
    A critical angle exists in either direction whenever the indices are different.
  feedback: |-
    Different indices are not enough; direction matters. The incident medium must have the larger index so the transmitted ray bends away from the normal toward $90^\circ$.
- id: depends-only-on-frequency
  content: |-
    A critical angle exists only when the light frequency is high enough, regardless of the indices.
  feedback: |-
    Material indices may depend somewhat on frequency, but the deciding condition for a given pair of indices is $n_1>n_2$. Frequency alone cannot create total internal reflection in the low-to-high direction.
```

---

<a id="derive-the-critical-angle-formula"></a>
## Derive the Critical-Angle Formula

**Example:** Derive a formula for the critical angle when light travels from $n_1$ into $n_2$ with $n_1>n_2$.

**Explanation**

Start with Snell's law:

$$
n_1\sin\theta_1=n_2\sin\theta_2.
$$

At the critical condition, substitute $\theta_1=\theta_c$ and $\theta_2=90^\circ$:

$$
n_1\sin\theta_c=n_2\sin90^\circ.
$$

Since $\sin90^\circ=1$,

$$
n_1\sin\theta_c=n_2.
$$

Divide by $n_1$, then undo the sine with inverse sine:

$$
\begin{aligned}
\sin\theta_c&=\frac{n_2}{n_1},\\
\theta_c&=\sin^{-1}\left(\frac{n_2}{n_1}\right).
\end{aligned}
$$

Keep the index order tied to the ray direction: transmitted index over incident index.

The high-to-low condition also provides an immediate inverse-trig check:

$$
0<\frac{n_2}{n_1}<1
\qquad\Longrightarrow\qquad
0^\circ<\theta_c<90^\circ.
$$

Thus the principal value returned by $\sin^{-1}$ is the acute incident angle required by the diagram.

```quiz
type: radio
id: critical-angle-formula-choice
shuffle: true
content: |-
  Light travels from $n_1$ into a lower index $n_2$. Which expression gives the critical angle measured from the normal?
options:
- id: inverse-sine-n2-over-n1
  content: |-
    $\theta_c=\sin^{-1}\left(\dfrac{n_2}{n_1}\right)$
  correct: true
  feedback: |-
    At the critical condition the transmitted angle is $90^\circ$. Snell's law becomes $n_1\sin\theta_c=n_2$, so isolating and undoing the sine gives $\theta_c=\sin^{-1}(n_2/n_1)$.
- id: inverse-sine-n1-over-n2
  content: |-
    $\theta_c=\sin^{-1}\left(\dfrac{n_1}{n_2}\right)$
  feedback: |-
    This reverses the index ratio. Because $n_1>n_2$, it would ask for the inverse sine of a number above $1$. Snell's law instead gives transmitted index over incident index, $n_2/n_1$.
- id: sine-without-inverse
  content: |-
    $\theta_c=\sin\left(\dfrac{n_2}{n_1}\right)$
  feedback: |-
    Dividing Snell's law isolates $\sin\theta_c$, not $\theta_c$. Recovering an angle from its sine requires the inverse operation $\sin^{-1}$, not another sine.
- id: inverse-cosine-ratio
  content: |-
    $\theta_c=\cos^{-1}\left(\dfrac{n_2}{n_1}\right)$
  feedback: |-
    Snell's law uses sines of angles measured from the normal. Inverse cosine would produce the complementary angle measured from the surface, not the requested critical angle from the normal.
- id: inverse-sine-difference
  content: |-
    $\theta_c=\sin^{-1}(n_1-n_2)$
  feedback: |-
    Snell's law relates each index by multiplication with a sine, so isolating $\sin\theta_c$ requires a ratio. The difference of the indices does not follow from the equation.
```

---

<a id="evaluate-the-inverse-sine-in-degrees"></a>
## Evaluate the Inverse Sine in Degrees

**Example:** Find the critical angle for light traveling from water $(n_1=1.33)$ into air $(n_2=1.00)$.

**Explanation**

The direction is higher index to lower index, so a critical angle exists. Substitute the indices in the correct order:

$$
\begin{aligned}
\theta_c
&=\sin^{-1}\left(\frac{1.00}{1.33}\right)\\
&=\sin^{-1}(0.751879\ldots)\\
&=48.75\ldots^\circ.
\end{aligned}
$$

Thus,

$$
\theta_c\approx48.8^\circ,
$$

or $49^\circ$ to the nearest degree.

Use degree mode because the requested angle is in degrees. A calculator in radian mode returns about $0.851$, which is the same angle in radians but is not a degree answer.

If a calculator does return radians, convert rather than attaching a degree sign:

$$
(0.8509\ldots\ \mathrm{rad})
\left(\frac{180^\circ}{\pi\ \mathrm{rad}}\right)
=48.75\ldots^\circ.
$$

Angles in Snell's law are measured from the normal. An angle measured from the surface is the complement and is not $\theta_c$.

```quiz
type: radio
id: critical-angle-water-to-air
shuffle: true
content: |-
  Find the critical angle for light traveling from water $(n_1=1.33)$ into air $(n_2=1.00)$. Choose the nearest whole degree.
options:
- id: forty-nine-degrees
  content: |-
    $49^\circ$
  correct: true
  feedback: |-
    The critical ray refracts at $90^\circ$, so $\theta_c=\sin^{-1}(1.00/1.33)=48.75\ldots^\circ$. Rounding to the nearest degree gives $49^\circ$.
- id: zero-eight-five-degrees
  content: |-
    $0.85^\circ$
  feedback: |-
    The value near $0.85$ is the inverse-sine result in radians, not degrees. Using degree mode or converting radians gives $48.75\ldots^\circ$, which rounds to $49^\circ$.
- id: forty-one-degrees
  content: |-
    $41^\circ$
  feedback: |-
    This is approximately the complementary angle measured from the surface. Snell's-law angles are measured from the normal, giving $\theta_c=48.75\ldots^\circ\approx49^\circ$.
- id: ninety-degrees
  content: |-
    $90^\circ$
  feedback: |-
    At the critical condition, $90^\circ$ is the transmitted angle along the boundary. The incident critical angle is smaller and equals $\sin^{-1}(1.00/1.33)\approx49^\circ$.
- id: no-critical-angle
  content: |-
    No critical angle exists.
  feedback: |-
    Water has the larger index, $1.33>1.00$, so light traveling from water into air can reach the critical condition. The ratio $1.00/1.33$ is within the inverse-sine domain.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the source problem in its original one-slot numerical form before selecting the check below.

> **Question 4**
>
> Calculate the critical angle for light traveling from glass $(n=1.5)$ into air $(n=1.0)$. Enter degrees: ______

The response slot expects one whole-number degree value.

**Explanation**

Glass is the higher-index incident medium, so a critical angle exists. At the critical condition, the refracted ray is at $90^\circ$:

$$
1.5\sin\theta_c=1.0\sin90^\circ.
$$

Therefore,

$$
\begin{aligned}
\sin\theta_c&=\frac{1.0}{1.5},\\
\theta_c&=\sin^{-1}\left(\frac{1.0}{1.5}\right)\\
&=41.81\ldots^\circ.
\end{aligned}
$$

Rounded to the requested whole degree, the value entered is

$$
\boxed{42^\circ}.
$$

```quiz
type: radio
id: khadley-snells-law-q4
shuffle: true
content: |-
  Which value belongs in the source problem's single degree-response slot?
options:
- id: forty-two-degrees
  content: |-
    $42^\circ$
  correct: true
  feedback: |-
    At the critical condition, $1.5\sin\theta_c=1.0\sin90^\circ$. Thus $\theta_c=\sin^{-1}(1.0/1.5)=41.8\ldots^\circ$, which rounds to the required entry $42^\circ$.
- id: zero-seven-three-degrees
  content: |-
    $0.73^\circ$
  feedback: |-
    The value near $0.73$ is the inverse-sine result in radians, not degrees. The source requests degrees, so $0.7297\ldots\ \mathrm{rad}=41.8\ldots^\circ$, which rounds to $42^\circ$.
- id: forty-eight-degrees
  content: |-
    $48^\circ$
  feedback: |-
    This is the complement measured from the surface rather than the critical angle measured from the normal. Snell's law gives $41.8\ldots^\circ$ from the normal, so the slot receives $42$.
- id: ninety-degrees
  content: |-
    $90^\circ$
  feedback: |-
    At the critical condition, the transmitted ray has angle $90^\circ$. The requested incident critical angle is $\sin^{-1}(1.0/1.5)=41.8\ldots^\circ$, not $90^\circ$.
- id: no-solution
  content: |-
    No critical angle exists.
  feedback: |-
    Glass has the larger index and the light travels into lower-index air, so the required high-to-low condition is satisfied. The ratio $1.0/1.5$ is valid and gives $42^\circ$.
```

---

<a id="summary"></a>
## Summary

- A critical angle exists only when light travels from a higher index $n_1$ into a lower index $n_2$.
- At the critical condition, the transmitted ray lies along the boundary: $\theta_2=90^\circ$.
- Substitute that condition into Snell's law and isolate the incident angle:
  $$
  \theta_c=\sin^{-1}\left(\frac{n_2}{n_1}\right).
  $$
- Keep the ratio in the order transmitted index over incident index; reversing it produces an invalid value above $1$.
- Use inverse sine, not sine, and use degree mode when the requested answer is in degrees.
- Measure $\theta_c$ from the normal, not from the surface.
- Round only after evaluating the inverse sine with guard digits.
