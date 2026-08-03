# Finding the Speed in a Three-Mass Equilateral Orbit

<!--
lesson-id: 212-M3-009
topic-code: MTH212.M3.09
-->

## Table of Contents

- [Introduction](#introduction)
- [Combine the Two Gravitational Forces](#combine-the-two-gravitational-forces)
- [Use the Center-to-Corner Radius](#use-the-center-to-corner-radius)
- [Balance Gravity With Centripetal Force](#balance-gravity-with-centripetal-force)
- [Apply the Method to Problem 5](#apply-the-method-to-problem-5)

## Prerequisites

- Newton's law of gravitation: $F=Gm_1m_2/r^2$
- Centripetal force: $F_c=mv^2/R$
- Adding two equal vectors separated by $60^\circ$
- Geometry of an equilateral triangle
- Solving an equation containing $v^2$

---

<a id="introduction"></a>
## Introduction

Three equal masses at the corners of an equilateral triangle can orbit their common center while keeping the triangle's shape. For any one mass, the other two masses pull with equal forces separated by $60^\circ$. Their resultant points toward the triangle's center.

The recognition cue is three equal masses in an equilateral-triangle orbit with side length $L$. Combine the two gravitational forces, use the center-to-corner radius $R=L/\sqrt3$, and set the inward force equal to $mv^2/R$. The geometry factors cancel, leaving

$$
v=\sqrt{\frac{Gm}{L}}.
$$

---

<a id="combine-the-two-gravitational-forces"></a>
## Combine the Two Gravitational Forces

**Example:** Find the net inward force on one mass if each of the other two masses pulls it with magnitude $F$ and the force directions are separated by $60^\circ$.

**Explanation**

The two force vectors have equal magnitudes. Their sideways components cancel, and their components along the angle bisector add. Equivalently, the law of cosines for the vector sum gives

$$
\begin{aligned}
F_{\mathrm{net}}^2
&=F^2+F^2+2F^2\cos60^\circ\\
&=3F^2,
\end{aligned}
$$

so

$$
F_{\mathrm{net}}=\sqrt3F.
$$

For two equal masses separated by $L$,

$$
F=\frac{Gm^2}{L^2},
$$

therefore

$$
F_{\mathrm{net}}=\sqrt3\frac{Gm^2}{L^2}.
$$

```quiz
type: radio
id: p5-resultant-force
content: |-
  Two equal gravitational forces of magnitude $F$ act on one corner mass along the two sides of an equilateral triangle. The force directions are separated by $60^\circ$. What is the magnitude of their resultant?
options:
- id: p5-resultant-a
  content: |-
    $\sqrt3F$
  correct: true
  feedback: |-
    Use the included angle of $60^\circ$: $F_{\mathrm{net}}=\sqrt{F^2+F^2+2F^2\cos60^\circ}=\sqrt3F$. Adding the magnitudes as $2F$ ignores their different directions.
- id: p5-resultant-b
  content: |-
    $2F$
- id: p5-resultant-c
  content: |-
    $F$
- id: p5-resultant-d
  content: |-
    $F/\sqrt3$
- id: p5-resultant-e
  content: |-
    $\sqrt2F$
```

---

<a id="use-the-center-to-corner-radius"></a>
## Use the Center-to-Corner Radius

**Example:** Relate the orbital radius $R$ of each mass to the equilateral triangle's side length $L$.

**Explanation**

An altitude divides the equilateral triangle into two $30^\circ$-$60^\circ$-$90^\circ$ triangles. Its length is

$$
h=\frac{\sqrt3}{2}L.
$$

The center of an equilateral triangle lies two-thirds of the way from a corner along an altitude. Thus the corner-to-center distance is

$$
R=\frac23h
=\frac23\left(\frac{\sqrt3}{2}L\right)
=\frac{L}{\sqrt3}.
$$

The pairwise gravitational distance is $L$, but the circular-orbit radius is $R=L/\sqrt3$. These are not the same distance.

As a quick geometry check,

$$
R=\frac{L}{\sqrt3}\approx0.577L,
$$

so the center-to-corner distance is correctly smaller than the side length.

```quiz
type: radio
id: p5-orbit-radius
content: |-
  Three equal masses occupy the corners of an equilateral triangle of side length $L$ and orbit the triangle's center. What is the orbital radius of each mass?
options:
- id: p5-radius-a
  content: |-
    $R=\dfrac{L}{\sqrt3}$
  correct: true
  feedback: |-
    The orbit radius is the corner-to-center distance, which is two-thirds of the altitude: $R=(2/3)(\sqrt3L/2)=L/\sqrt3$.
- id: p5-radius-b
  content: |-
    $R=L$
- id: p5-radius-c
  content: |-
    $R=\dfrac{L}{2}$
- id: p5-radius-d
  content: |-
    $R=\sqrt3L$
- id: p5-radius-e
  content: |-
    $R=\dfrac{\sqrt3}{2}L$
```

---

<a id="balance-gravity-with-centripetal-force"></a>
## Balance Gravity With Centripetal Force

**Example:** Derive the speed of each mass in terms of $G$, $m$, and $L$.

**Explanation**

The inward gravitational resultant supplies the centripetal force. Substitute both geometry results:

$$
\sqrt3\frac{Gm^2}{L^2}
=\frac{mv^2}{L/\sqrt3}.
$$

The right side simplifies to $\sqrt3mv^2/L$. Cancel the common factors $\sqrt3$, $m$, and one factor of $L$:

$$
\begin{aligned}
\sqrt3\frac{Gm^2}{L^2}
&=\sqrt3\frac{mv^2}{L}\\
\frac{Gm}{L}&=v^2.
\end{aligned}
$$

Velocity may point in different directions around the orbit, but speed is nonnegative. Take the positive square root:

$$
v=\sqrt{\frac{Gm}{L}}.
$$

The units provide a quick check:

$$
\left[\frac{Gm}{L}\right]
=\frac{(\mathrm{N\,m^2/kg^2})(\mathrm{kg})}{\mathrm m}
=\frac{\mathrm{m^2}}{\mathrm{s^2}},
$$

so its square root has units $\mathrm{m/s}$, as a speed should.

```quiz
type: radio
id: p5-isolate-speed
content: |-
  After setting the net gravitational force equal to the centripetal force, the equation simplifies to $v^2=Gm/L$. Which expression gives the orbital speed?
options:
- id: p5-speed-a
  content: |-
    $v=\sqrt{\dfrac{Gm}{L}}$
  correct: true
  feedback: |-
    Isolate $v^2$, then take the nonnegative square root because the requested quantity is speed: $v=\sqrt{Gm/L}$.
- id: p5-speed-b
  content: |-
    $v=\dfrac{Gm}{L}$
- id: p5-speed-c
  content: |-
    $v=\sqrt{\dfrac{GL}{m}}$
- id: p5-speed-d
  content: |-
    $v=\dfrac{Gm}{L^2}$
- id: p5-speed-e
  content: |-
    $v=\sqrt{GmL}$
```

---

<a id="apply-the-method-to-problem-5"></a>
## Apply the Method to Problem 5

**Example:** For the same three equal masses in an equilateral-triangle orbit, find the speed of each mass when $m=2.5\times10^{30}\ \mathrm{kg}$ and $L=1.8\times10^{12}\ \mathrm{m}$.

**Explanation**

The distance from each corner to the triangle's center is $R=L/\sqrt{3}$. Setting the net gravitational force equal to the centripetal force gives

$$
\sqrt{3}\frac{Gm^2}{L^2}
=\frac{mv^2}{L/\sqrt{3}},
$$

so

$$
v=\sqrt{\frac{Gm}{L}}
=9624.9\ldots\ \mathrm{m/s}.
$$

The measured givens have two significant figures, so $v=9.6\times10^3\ \mathrm{m/s}$, entered as `9600`.

The answer choices diagnose common mistakes:

- `9624.9` keeps more digits than the measured givens support.
- `7300` comes from using only one pairwise gravitational force.
- `13000` comes from using $R=L$ instead of $R=L/\sqrt3$.
- `220` carries over the previous problem's force answer instead of calculating a speed.

```quiz
type: radio
id: p5-source-check
content: |-
  **Question 4**

  For the same three equal masses in an equilateral-triangle orbit, find the speed of each mass when $m=2.5\times10^{30}\ \mathrm{kg}$ and $L=1.8\times10^{12}\ \mathrm{m}$.

  Enter the speed in meters per second as a number only:
options:
- id: p5-source-a
  content: |-
    $9600$
  correct: true
  feedback: |-
    The distance from each corner to the triangle's center is $R=L/\sqrt{3}$. Setting the net gravitational force equal to the centripetal force gives

    $$
    \sqrt{3}\frac{Gm^2}{L^2}
    =\frac{mv^2}{L/\sqrt{3}},
    $$

    so

    $$
    v=\sqrt{\frac{Gm}{L}}
    =9624.9\ldots\ \mathrm{m/s}.
    $$

    The measured givens have two significant figures, so $v=9.6\times10^3\ \mathrm{m/s}$, entered as `9600`.
- id: p5-source-b
  content: |-
    $9624.9$
- id: p5-source-c
  content: |-
    $7300$
- id: p5-source-d
  content: |-
    $13000$
- id: p5-source-e
  content: |-
    $220$
```

---

## Summary

- Cue: three equal masses form an equilateral triangle and orbit their common center.
- Combine the two $60^\circ$-separated forces: $F_{\mathrm{net}}=\sqrt3Gm^2/L^2$.
- Use the orbital radius $R=L/\sqrt3$, not the side length $L$.
- Set $F_{\mathrm{net}}=mv^2/R$ and simplify to $v=\sqrt{Gm/L}$.
- Confirm that $Gm/L$ has units $\mathrm{m^2/s^2}$ before taking the square root.
- Check the requested format and round only at the end; for Problem 5, enter `9600`.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
