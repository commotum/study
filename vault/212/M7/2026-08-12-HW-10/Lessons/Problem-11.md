# Solving the Thin-Lens Equation for Image Distance

## Table of Contents

- [Introduction](#introduction)
- [Isolate the Image-Distance Reciprocal](#isolate-the-image-distance-reciprocal)
- [Combine the Reciprocal Difference](#combine-the-reciprocal-difference)
- [Invert the Entire Fraction](#invert-the-entire-fraction)
- [Check the Sign and Focal-Point Boundary](#check-the-sign-and-focal-point-boundary)
- [Apply the Formula to the Ray Diagram](#apply-the-formula-to-the-ray-diagram)
- [Summary](#summary)

## Prerequisites

- Recognize $d_0$ as the object distance, $d_1$ as the image distance, and $f_1$ as the signed focal length of Lens 1.
- Rearrange an equation by applying the same operation to both sides.
- Subtract fractions with unlike denominators and take the reciprocal of a nonzero fraction.

---

<a id="introduction"></a>
## Introduction

When a thin-lens problem gives the object distance and focal length but asks for the image distance, begin with

$$
\frac{1}{f_1}=\frac{1}{d_0}+\frac{1}{d_1}.
$$

The cue is that the unknown, $d_1$, appears in a denominator. Do not try to move $d_1$ directly. First isolate its reciprocal, combine the other two reciprocals into one fraction, and only then invert:

$$
\frac{1}{d_1}
=\frac{1}{f_1}-\frac{1}{d_0}
=\frac{d_0-f_1}{d_0f_1}
\quad\Longrightarrow\quad
d_1=\frac{d_0f_1}{d_0-f_1}.
$$

The subtraction order $d_0-f_1$ is the main sign trap.

Treat $d_0$ and $f_1$ as constants while making $d_1$ the subject. The three algebra moves are always the same:

$$
\boxed{\text{isolate }1/d_1}
\;\longrightarrow\;
\boxed{\text{make one fraction}}
\;\longrightarrow\;
\boxed{\text{take its reciprocal}}.
$$

---

<a id="isolate-the-image-distance-reciprocal"></a>
## Isolate the Image-Distance Reciprocal

**Example:** Starting from

$$
\frac{1}{F}=\frac{1}{P}+\frac{1}{Q},
$$

solve first for the reciprocal $1/Q$.

**Explanation**

Treat $F$ and $P$ as known constants. Subtract $1/P$ from both sides:

$$
\frac{1}{F}-\frac{1}{P}
=\frac{1}{P}+\frac{1}{Q}-\frac{1}{P},
$$

so

$$
\frac{1}{Q}=\frac{1}{F}-\frac{1}{P}.
$$

At this stage the left side is still $1/Q$, not $Q$.

```quiz
type: radio
id: p11-isolate-reciprocal
content: |-
  The equation $\dfrac{1}{a}=\dfrac{1}{b}+\dfrac{1}{x}$ is to be solved for $x$. Which line correctly isolates the reciprocal of the unknown?
options:
- id: a-minus-b
  content: |-
    $\dfrac{1}{x}=\dfrac{1}{a}-\dfrac{1}{b}$
  correct: true
  feedback: |-
    The unknown reciprocal is added to $1/b$, so subtracting $1/b$ from both sides isolates it. Therefore $1/x=1/a-1/b$.
- id: b-minus-a
  content: |-
    $\dfrac{1}{x}=\dfrac{1}{b}-\dfrac{1}{a}$
  feedback: |-
    This reverses the subtraction. The term removed from the right side is $1/b$, so it must be subtracted from the left side as well: $1/x=1/a-1/b$.
- id: x-not-reciprocal
  content: |-
    $x=\dfrac{1}{a}-\dfrac{1}{b}$
  feedback: |-
    Subtracting $1/b$ isolates the term that was present in the equation, namely $1/x$. The result must remain $1/x=1/a-1/b$ until the right side has been combined and reciprocated.
- id: keep-plus
  content: |-
    $\dfrac{1}{x}=\dfrac{1}{a}+\dfrac{1}{b}$
  feedback: |-
    Keeping the plus sign does not remove $1/b$ from the side containing the unknown. Use the inverse operation, subtraction, to obtain $1/x=1/a-1/b$.
```

---

<a id="combine-the-reciprocal-difference"></a>
## Combine the Reciprocal Difference

**Example:** Combine

$$
\frac{1}{F}-\frac{1}{P}
$$

into one fraction.

**Explanation**

Use the common denominator $FP$. The first numerator must be multiplied by $P$, and the second by $F$:

$$
\frac{1}{F}-\frac{1}{P}
=\frac{P}{FP}-\frac{F}{FP}
=\frac{P-F}{FP}.
$$

Because the original operation was subtraction, the new numerator is $P-F$, in that order.

```quiz
type: radio
id: p11-combine-difference
content: |-
  Which single fraction is equal to $\dfrac{1}{u}-\dfrac{1}{v}$?
options:
- id: v-minus-u
  content: |-
    $\dfrac{v-u}{uv}$
  correct: true
  feedback: |-
    The common denominator is $uv$: $1/u=v/(uv)$ and $1/v=u/(uv)$. Subtracting the numerators gives $(v-u)/(uv)$.
- id: u-minus-v
  content: |-
    $\dfrac{u-v}{uv}$
  feedback: |-
    This numerator belongs to the reversed difference $1/v-1/u$. For $1/u-1/v$, the converted numerators are $v$ then $u$, so the result is $(v-u)/(uv)$.
- id: denominator-difference
  content: |-
    $\dfrac{1}{u-v}$
  feedback: |-
    Fractions cannot be subtracted by subtracting their denominators. Rewrite both terms over the common denominator $uv$, which gives the numerator difference $v-u$.
- id: numerator-two
  content: |-
    $\dfrac{2}{uv}$
  feedback: |-
    The numerators are not both $1$ after the denominators are made common. They become $v$ and $u$, so subtraction gives $v-u$, not $2$.
```

---

<a id="invert-the-entire-fraction"></a>
## Invert the Entire Fraction

**Example:** Finish solving when

$$
\frac{1}{Q}=\frac{P-F}{PF}.
$$

**Explanation**

Both sides are reciprocals, so invert the entire right-hand fraction:

$$
Q=\frac{PF}{P-F}.
$$

The complete numerator $PF$ and complete denominator $P-F$ exchange places. Keep the difference grouped; $PF/(P-F)$ is not the same as $PF/P-F$.

```quiz
type: radio
id: p11-invert-expression
content: |-
  For a thin lens, $\dfrac{1}{f}=\dfrac{1}{s}+\dfrac{1}{s'}$. Which expression correctly solves for $s'$?
options:
- id: product-over-difference
  content: |-
    $s'=\dfrac{sf}{s-f}$
  correct: true
  feedback: |-
    Isolating gives $1/s'=1/f-1/s=(s-f)/(sf)$. Reciprocating that entire fraction gives $s'=sf/(s-f)$.
- id: reversed-difference
  content: |-
    $s'=\dfrac{sf}{f-s}$
  feedback: |-
    This reverses the denominator and therefore changes the sign. Since $1/s'=1/f-1/s=(s-f)/(sf)$, the reciprocal has denominator $s-f$.
- id: sum-denominator
  content: |-
    $s'=\dfrac{sf}{s+f}$
  feedback: |-
    The image reciprocal is isolated by subtracting $1/s$ from $1/f$, not adding it. The common numerator is therefore $s-f$, so $s'=sf/(s-f)$.
- id: uninverted
  content: |-
    $s'=\dfrac{s-f}{sf}$
  feedback: |-
    The fraction $(s-f)/(sf)$ equals $1/s'$, not $s'$. Taking the reciprocal of the whole fraction gives $s'=sf/(s-f)$.
```

---

<a id="check-the-sign-and-focal-point-boundary"></a>
## Check the Sign and Focal-Point Boundary

**Example:** A converging lens has $f=10\ \mathrm{cm}$, and a real object is placed at $d_o=30\ \mathrm{cm}$. Find the image distance and check its sign.

**Explanation**

Substitute into the solved form:

$$
d_i=\frac{d_of}{d_o-f}
=\frac{(30\ \mathrm{cm})(10\ \mathrm{cm})}{30\ \mathrm{cm}-10\ \mathrm{cm}}
=15\ \mathrm{cm}.
$$

The result is positive, as it must be for the real image on the opposite side shown by converging rays. It also satisfies $d_i>f$, so the image lies beyond the far focal point.

The formula carries two useful boundary checks:

- If $d_o=f$, then $d_o-f=0$. The outgoing rays are parallel, so there is no image at a finite distance.
- If $d_o$ is very large, then $d_o-f\approx d_o$ and $d_i\approx f$. A very distant object's image forms near the far focal point.

Thus the finite-distance formula assumes $d_o\ne f$.

```quiz
type: radio
id: p11-sign-check
content: |-
  A converging lens has $f=12\ \mathrm{cm}$, and a real object is placed at $d_o=36\ \mathrm{cm}$. What image distance follows from the thin-lens equation?
options:
- id: positive-eighteen
  content: |-
    $d_i=18\ \mathrm{cm}$
  correct: true
  feedback: |-
    For a real object outside a converging lens's focal point, $d_i=d_of/(d_o-f)$. Substitution gives $(36)(12)/(36-12)=18\ \mathrm{cm}$, positive for an image on the opposite side.
- id: negative-eighteen
  content: |-
    $d_i=-18\ \mathrm{cm}$
  feedback: |-
    This sign comes from reversing the denominator to $f-d_o$. The isolated reciprocal is $1/f-1/d_o$, so the correct denominator is $d_o-f=24\ \mathrm{cm}$ and the real far-side image has $d_i=+18\ \mathrm{cm}$.
- id: positive-nine
  content: |-
    $d_i=9\ \mathrm{cm}$
  feedback: |-
    This value results from using $d_o+f$ in the denominator. Isolating $1/d_i$ requires subtraction, so $(36)(12)/(36-12)=18\ \mathrm{cm}$ rather than $(36)(12)/(36+12)$.
- id: positive-twenty-four
  content: |-
    $d_i=24\ \mathrm{cm}$
  feedback: |-
    The difference $d_o-f=24\ \mathrm{cm}$ is only the denominator of the solved formula, not the image distance itself. The numerator $d_of$ must remain, giving $d_i=(36)(12)/24=18\ \mathrm{cm}$.
```

---

<a id="apply-the-formula-to-the-ray-diagram"></a>
## Apply the Formula to the Ray Diagram

**Example:** In the diagram, Lens 1 forms an image on the opposite side from an object placed a distance $d_0$ away.

![](<../Source/2026-08-12-HW-10/Images/thin-lens-ray-trace-distances.png>)

**Explanation**

The symbols map directly onto the thin-lens equation:

$$
\frac{1}{f_1}=\frac{1}{d_0}+\frac{1}{d_1}.
$$

Isolate, combine, and invert:

$$
\begin{aligned}
\frac{1}{d_1}
&=\frac{1}{f_1}-\frac{1}{d_0}\\[4pt]
&=\frac{d_0-f_1}{d_0f_1},
\end{aligned}
$$

so

$$
d_1=\frac{d_0f_1}{d_0-f_1}.
$$

The actual rays meet on the opposite side, so $d_1>0$. Lens 1 is converging, so its signed focal length satisfies $f_1=|f_1|>0$, and the diagram places the object outside the focal point, $d_0>f_1$. The solved expression has exactly that positive sign because $d_0-f_1>0$.

```quiz
type: radio
id: p11-homework-check
content: |-
  An object is placed a distance $d_0$ from Lens 1, and its image forms a distance $d_1$ on the opposite side. In terms of the indicated quantities, what is $d_1$?

  ![](<../Source/2026-08-12-HW-10/Images/thin-lens-ray-trace-distances.png>)
options:
- id: d0f-over-d0-minus-f
  content: |-
    $\dfrac{d_0f_1}{d_0-f_1}$
  correct: true
  feedback: |-
    The thin-lens equation gives $1/d_1=1/f_1-1/d_0=(d_0-f_1)/(d_0f_1)$. Reciprocating the complete fraction yields $d_1=d_0f_1/(d_0-f_1)$, which is positive here because the object lies outside the positive focal length.
- id: d0f-over-f-minus-d0
  content: |-
    $\dfrac{d_0f_1}{f_1-d_0}$
  feedback: |-
    Reversing the denominator changes the sign of the result. Isolating $1/d_1$ requires $1/f_1-1/d_0$, whose common numerator is $d_0-f_1$, not $f_1-d_0$.
- id: d0f-over-sum
  content: |-
    $\dfrac{d_0f_1}{d_0+f_1}$
  feedback: |-
    The object-distance reciprocal is subtracted when $1/d_1$ is isolated. Thus $1/d_1=(d_0-f_1)/(d_0f_1)$, so the final denominator is $d_0-f_1$ rather than a sum.
```

---

<a id="summary"></a>
## Summary

When a thin-lens question asks for image distance:

1. Start with $1/f=1/d_o+1/d_i$.
2. Isolate the unknown reciprocal: $1/d_i=1/f-1/d_o$.
3. Use a common denominator: $1/d_i=(d_o-f)/(d_of)$.
4. Invert the entire fraction: $d_i=d_of/(d_o-f)$.
5. Keep the subtraction order and parentheses. Reversing $d_o-f$ reverses the sign of the image distance.
6. Check the physics: $d_o>f>0$ gives a positive real-image distance, $d_o=f$ gives no finite image, and $d_o\gg f$ gives $d_i\approx f$.
