# Evaluating $\int_0^\pi \sin^4 x\,dx$ by Power Reduction

## Table of Contents

- [Introduction](#introduction)
- [Apply the First Power Reduction](#apply-the-first-power-reduction)
- [Reduce the Remaining Cosine Square](#reduce-the-remaining-cosine-square)
- [Integrate the Reduced Form](#integrate-the-reduced-form)
- [Evaluate the Exact Bounds](#evaluate-the-exact-bounds)
- [Summary](#summary)

## Prerequisites

- Use $\sin^2\theta=\dfrac{1-\cos(2\theta)}2$ and $\cos^2\theta=\dfrac{1+\cos(2\theta)}2$.
- Expand a squared binomial and combine like terms.
- Evaluate an antiderivative at both bounds of a definite integral.

---

<a id="introduction"></a>
## Introduction

The recognition cue is an **even power of sine** with no odd factor available for direct substitution. For the fourth power, write

$$
\sin^4 x=\left(\sin^2 x\right)^2
$$

and apply the sine power-reduction identity:

$$
\sin^2 x=\frac{1-\cos(2x)}2.
$$

Squaring this expression creates a remaining $\cos^2(2x)$ term, so power reduction must be used a second time. The final result is a sum of a constant, $\cos(2x)$, and $\cos(4x)$.

---

<a id="apply-the-first-power-reduction"></a>
## Apply the First Power Reduction

**Example:** Apply one power-reduction step to $\sin^4(2x)$.

**Explanation**

First reduce $\sin^2(2x)$:

$$
\sin^2(2x)=\frac{1-\cos(4x)}2.
$$

Because the original expression is the square of $\sin^2(2x)$, square the entire right-hand side:

$$
\begin{aligned}
\sin^4(2x)
&=\left(\frac{1-\cos(4x)}2\right)^2\\
&=\frac14\left(1-2\cos(4x)+\cos^2(4x)\right).
\end{aligned}
$$

The factor is $1/4$ because the denominator $2$ is also squared.

```quiz
type: radio
id: whw5-p5-q1
content: |-
  Which expression results from applying one power-reduction step to $\sin^4(3x)$?
options:
- id: whw5-p5-q1-a
  content: |-
    $\dfrac14\left(1-2\cos(6x)+\cos^2(6x)\right)$
  correct: true
- id: whw5-p5-q1-b
  content: |-
    $\dfrac12\left(1-2\cos(6x)+\cos^2(6x)\right)$
- id: whw5-p5-q1-c
  content: |-
    $\dfrac14\left(1-\cos(6x)+\cos^2(6x)\right)$
- id: whw5-p5-q1-d
  content: |-
    $\dfrac14\left(1-2\cos(3x)+\cos^2(3x)\right)$
- id: whw5-p5-q1-e
  content: |-
    $\dfrac14\left(1+2\cos(6x)+\cos^2(6x)\right)$
```

---

<a id="reduce-the-remaining-cosine-square"></a>
## Reduce the Remaining Cosine Square

**Example:** Rewrite $\sin^4(2x)$ with no trigonometric powers.

**Explanation**

After the first reduction,

$$
\sin^4(2x)
=\frac14\left(1-2\cos(4x)+\cos^2(4x)\right).
$$

Start with the cosine double-angle identity

$$
\cos(2\phi)=2\cos^2\phi-1.
$$

Solving for the square gives the needed cosine power reduction:

$$
\cos^2\phi=\frac{1+\cos(2\phi)}2.
$$

With $\phi=4x$,

$$
\cos^2(4x)=\frac{1+\cos(8x)}2.
$$

Then combine the constant terms:

$$
\begin{aligned}
\sin^4(2x)
&=\frac14\left(1-2\cos(4x)+\frac{1+\cos(8x)}2\right)\\
&=\frac14\left(\frac32-2\cos(4x)+\frac12\cos(8x)\right)\\
&=\frac38-\frac12\cos(4x)+\frac18\cos(8x).
\end{aligned}
$$

The original angle $2x$ is doubled to $4x$ and then doubled again to $8x$.

```quiz
type: radio
id: whw5-p5-q2
content: |-
  Which identity rewrites $\sin^4(3x)$ with no trigonometric powers?
options:
- id: whw5-p5-q2-a
  content: |-
    $\dfrac38-\dfrac12\cos(6x)+\dfrac18\cos(12x)$
  correct: true
- id: whw5-p5-q2-b
  content: |-
    $\dfrac38-\dfrac12\cos(3x)+\dfrac18\cos(6x)$
- id: whw5-p5-q2-c
  content: |-
    $\dfrac18-\dfrac12\cos(6x)+\dfrac38\cos(12x)$
- id: whw5-p5-q2-d
  content: |-
    $\dfrac38+\dfrac12\cos(6x)+\dfrac18\cos(12x)$
- id: whw5-p5-q2-e
  content: |-
    $\dfrac34-\cos(6x)+\dfrac14\cos(12x)$
```

---

<a id="integrate-the-reduced-form"></a>
## Integrate the Reduced Form

The reusable fourth-power identity is

$$
\sin^4(ax)=\frac38-\frac12\cos(2ax)+\frac18\cos(4ax).
$$

**Example:** Find an antiderivative of $\sin^4 x$.

**Explanation**

Integrate the reduced form term by term:

$$
\begin{aligned}
\int\sin^4 x\,dx
&=\int\left(\frac38-\frac12\cos(2x)+\frac18\cos(4x)\right)\,dx\\
&=\frac{3x}{8}-\frac{\sin(2x)}4+\frac{\sin(4x)}{32}+C.
\end{aligned}
$$

The reciprocal chain factors $1/2$ and $1/4$ multiply the cosine coefficients.

```quiz
type: radio
id: whw5-p5-q3
content: |-
  Which expression is an antiderivative of $\sin^4(2x)$?
options:
- id: whw5-p5-q3-a
  content: |-
    $\dfrac{3x}{8}-\dfrac{\sin(4x)}8+\dfrac{\sin(8x)}{64}+C$
  correct: true
- id: whw5-p5-q3-b
  content: |-
    $\dfrac{3x}{8}-\dfrac{\sin(2x)}4+\dfrac{\sin(4x)}{32}+C$
- id: whw5-p5-q3-c
  content: |-
    $\dfrac{3x}{8}-\dfrac{\sin(4x)}2+\dfrac{\sin(8x)}8+C$
- id: whw5-p5-q3-d
  content: |-
    $\dfrac{3x}{8}+\dfrac{\sin(4x)}8+\dfrac{\sin(8x)}{64}+C$
- id: whw5-p5-q3-e
  content: |-
    $\dfrac{3x}{4}-\dfrac{\sin(4x)}8+\dfrac{\sin(8x)}{32}+C$
```

---

<a id="evaluate-the-exact-bounds"></a>
## Evaluate the Exact Bounds

**Example:** Evaluate the assigned integral

$$
\int_0^\pi\sin^4 x\,dx.
$$

**Explanation**

Use

$$
F(x)=\frac{3x}{8}-\frac{\sin(2x)}4+\frac{\sin(4x)}{32}.
$$

The Fundamental Theorem of Calculus gives

$$
\int_0^\pi\sin^4 x\,dx
=\left.F(x)\right|_0^\pi
=F(\pi)-F(0).
$$

At the upper bound,

$$
F(\pi)=\frac{3\pi}{8}-\frac{\sin(2\pi)}4+\frac{\sin(4\pi)}{32}
=\frac{3\pi}{8}.
$$

At the lower bound,

$$
F(0)=0-\frac{\sin(0)}4+\frac{\sin(0)}{32}=0.
$$

Therefore,

$$
\boxed{
\int_0^\pi\sin^4 x\,dx
=F(\pi)-F(0)
=\frac{3\pi}{8}
}.
$$

Both oscillating sine terms vanish at both endpoints, but the constant term contributes the nonzero value.

No arbitrary constant is needed in the definite answer because the same constant would cancel in $F(\pi)-F(0)$. As a quick check, $0\leq\sin^4x\leq1$ on an interval of length $\pi$, so $3\pi/8$ lies in the required range from $0$ to $\pi$.

```quiz
type: radio
id: whw5-p5-q4
content: |-
  What is $\displaystyle\int_0^{\pi/2}\sin^4 x\,dx$?
options:
- id: whw5-p5-q4-a
  content: |-
    $\dfrac{3\pi}{16}$
  correct: true
- id: whw5-p5-q4-b
  content: |-
    $\dfrac{3\pi}{8}$
- id: whw5-p5-q4-c
  content: |-
    $\dfrac{\pi}{16}$
- id: whw5-p5-q4-d
  content: |-
    $\dfrac{\pi}{4}$
- id: whw5-p5-q4-e
  content: |-
    $\dfrac38$
```

---

<a id="summary"></a>
## Summary

For a fourth power of sine:

1. Write $\sin^4\theta=(\sin^2\theta)^2$.
2. Substitute $\sin^2\theta=\dfrac{1-\cos(2\theta)}2$ and square the entire expression.
3. Reduce the remaining cosine square with $\cos^2\phi=\dfrac{1+\cos(2\phi)}2$.
4. Use
   $\sin^4\theta=\dfrac38-\dfrac12\cos(2\theta)+\dfrac18\cos(4\theta)$.
5. Integrate term by term and evaluate the upper bound minus the lower bound.

The main traps are forgetting to square the factor $1/2$, stopping before reducing $\cos^2(2\theta)$, and evaluating only one endpoint.
