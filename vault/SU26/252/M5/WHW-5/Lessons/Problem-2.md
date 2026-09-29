# Cyclic Integration by Parts for Sine of a Logarithm

## Table of Contents

- [Introduction](#introduction)
- [Create the Companion Integral](#create-the-companion-integral)
- [Close the Cycle](#close-the-cycle)
- [Solve the Integral Equation](#solve-the-integral-equation)
- [Evaluate Problem 2](#evaluate-problem-2)
- [Summary](#summary)

## Prerequisites

- Use $\int u\,dv=uv-\int v\,du$.
- Differentiate $\ln(ax)$ as $\dfrac{1}{x}$ on an interval where $ax>0$.
- Differentiate sine and cosine with the chain rule.
- Solve a linear equation in an unknown integral.

---

<a id="introduction"></a>
## Introduction

An integral such as

$$
\int\sin\left(\ln(ax)\right)\,dx
$$

has a useful cyclic structure. Treat the integrand as

$$
\sin\left(\ln(ax)\right)\cdot 1
$$

and choose $dv=dx$. Then $v=x$, while differentiating the trigonometric factor produces $\dfrac{1}{x}$. These factors cancel, leaving a companion cosine integral. Applying integration by parts again returns the original sine integral, so the cycle can be solved algebraically.

For real-valued $\ln(2x)$, Problem 2 is considered on intervals with $x>0$.

---

<a id="create-the-companion-integral"></a>
## Create the Companion Integral

**Example:** Apply integration by parts once to $\displaystyle I=\int\sin(\ln x)\,dx$.

**Explanation**

Choose

$$
u=\sin(\ln x),
\qquad
dv=dx.
$$

Then

$$
du=\frac{\cos(\ln x)}{x}\,dx,
\qquad
v=x.
$$

Apply the formula:

$$
\begin{aligned}
I
&=x\sin(\ln x)-\int x\frac{\cos(\ln x)}{x}\,dx\\
&=x\sin(\ln x)-\int\cos(\ln x)\,dx.
\end{aligned}
$$

The factor $x$ from $v$ cancels the $\dfrac{1}{x}$ created by differentiating the logarithm.

```quiz
type: radio
id: p2-first-parts
content: |-
  Let $I=\displaystyle\int\sin(\ln(3x))\,dx$. Which equation results after one application of integration by parts?
options:
- id: a
  content: |-
    $I=x\sin(\ln(3x))-\displaystyle\int\cos(\ln(3x))\,dx$
  correct: true
- id: b
  content: |-
    $I=x\sin(\ln(3x))+\displaystyle\int\cos(\ln(3x))\,dx$
- id: c
  content: |-
    $I=x\sin(\ln(3x))-3\displaystyle\int\cos(\ln(3x))\,dx$
- id: d
  content: |-
    $I=\sin(\ln(3x))-x\displaystyle\int\cos(\ln(3x))\,dx$
- id: e
  content: |-
    $I=x\sin(\ln(3x))-\displaystyle\int\frac{\cos(\ln(3x))}{x}\,dx$
```

---

<a id="close-the-cycle"></a>
## Close the Cycle

**Example:** Evaluate the companion integral $\displaystyle J=\int\cos(\ln x)\,dx$ far enough to recover $I=\int\sin(\ln x)\,dx$.

**Explanation**

Use integration by parts again:

$$
u=\cos(\ln x),
\qquad
dv=dx,
$$

so

$$
du=-\frac{\sin(\ln x)}{x}\,dx,
\qquad
v=x.
$$

Therefore,

$$
\begin{aligned}
J
&=x\cos(\ln x)-\int x\left(-\frac{\sin(\ln x)}{x}\right)\,dx\\
&=x\cos(\ln x)+\int\sin(\ln x)\,dx\\
&=x\cos(\ln x)+I.
\end{aligned}
$$

The plus sign is essential: the subtraction in integration by parts acts on the negative derivative of cosine.

```quiz
type: radio
id: p2-close-cycle
content: |-
  Let $J=\displaystyle\int\cos(\ln(5x))\,dx$ and $I=\displaystyle\int\sin(\ln(5x))\,dx$. Which relation is correct?
options:
- id: a
  content: |-
    $J=x\cos(\ln(5x))+I$
  correct: true
- id: b
  content: |-
    $J=x\cos(\ln(5x))-I$
- id: c
  content: |-
    $J=\cos(\ln(5x))+xI$
- id: d
  content: |-
    $J=5x\cos(\ln(5x))+I$
- id: e
  content: |-
    $J=x\cos(\ln(5x))+\dfrac{I}{x}$
```

---

<a id="solve-the-integral-equation"></a>
## Solve the Integral Equation

**Example:** Evaluate $\displaystyle I=\int\sin(\ln(3x))\,dx$.

**Explanation**

The two applications of integration by parts give

$$
I=x\sin(\ln(3x))-J
$$

and

$$
J=x\cos(\ln(3x))+I.
$$

Substitute the second relation into the first:

$$
\begin{aligned}
I
&=x\sin(\ln(3x))-\left(x\cos(\ln(3x))+I\right)\\
2I
&=x\sin(\ln(3x))-x\cos(\ln(3x)).
\end{aligned}
$$

Divide by $2$ and include the constant of integration:

$$
I=\frac{x}{2}\left(\sin(\ln(3x))-\cos(\ln(3x))\right)+C.
$$

```quiz
type: radio
id: p2-solve-cycle
content: |-
  Evaluate $\displaystyle\int\sin(\ln(7x))\,dx$.
options:
- id: a
  content: |-
    $\dfrac{x}{2}\left(\sin(\ln(7x))-\cos(\ln(7x))\right)+C$
  correct: true
- id: b
  content: |-
    $x\left(\sin(\ln(7x))-\cos(\ln(7x))\right)+C$
- id: c
  content: |-
    $\dfrac{x}{2}\left(\sin(\ln(7x))+\cos(\ln(7x))\right)+C$
- id: d
  content: |-
    $\dfrac{1}{2x}\left(\sin(\ln(7x))-\cos(\ln(7x))\right)+C$
- id: e
  content: |-
    $\dfrac{x}{2}\left(\sin(\ln x)-\cos(\ln x)\right)+C$
```

---

<a id="evaluate-problem-2"></a>
## Evaluate Problem 2

**Example:** Evaluate $\displaystyle\int\sin\left(\ln(2x)\right)\,dx$.

**Explanation**

Let

$$
I=\int\sin\left(\ln(2x)\right)\,dx
\qquad\text{and}\qquad
J=\int\cos\left(\ln(2x)\right)\,dx.
$$

The constant $2$ cancels in the logarithmic derivative:

$$
\frac{d}{dx}\ln(2x)
=\frac{1}{2x}\cdot 2
=\frac{1}{x}.
$$

Therefore, two applications of integration by parts give

$$
I=x\sin\left(\ln(2x)\right)-J
$$

and

$$
J=x\cos\left(\ln(2x)\right)+I.
$$

Substitute for $J$ and solve:

$$
\begin{aligned}
I
&=x\sin\left(\ln(2x)\right)-\left(x\cos\left(\ln(2x)\right)+I\right)\\
2I
&=x\left(\sin\left(\ln(2x)\right)-\cos\left(\ln(2x)\right)\right)\\
I
&=\frac{x}{2}\left(\sin\left(\ln(2x)\right)-\cos\left(\ln(2x)\right)\right)+C.
\end{aligned}
$$

To verify the result, let $L=\ln(2x)$, so $L'=\dfrac{1}{x}$. Then

$$
\begin{aligned}
\frac{d}{dx}\left[\frac{x}{2}\left(\sin L-\cos L\right)\right]
&=\frac{1}{2}\left(\sin L-\cos L\right)
+\frac{x}{2}\left(\cos L+\sin L\right)\frac{1}{x}\\
&=\frac{1}{2}\left(\sin L-\cos L+\cos L+\sin L\right)\\
&=\sin L\\
&=\sin\left(\ln(2x)\right).
\end{aligned}
$$

```quiz
type: radio
id: p2-final-answer
content: |-
  Which is an antiderivative of $\sin(\ln(2x))$?
options:
- id: a
  content: |-
    $\dfrac{x}{2}\left(\sin(\ln(2x))-\cos(\ln(2x))\right)+C$
  correct: true
- id: b
  content: |-
    $x\left(\sin(\ln(2x))-\cos(\ln(2x))\right)+C$
- id: c
  content: |-
    $\dfrac{x}{2}\left(\sin(\ln(2x))+\cos(\ln(2x))\right)+C$
- id: d
  content: |-
    $\dfrac{1}{2x}\left(\sin(\ln(2x))-\cos(\ln(2x))\right)+C$
- id: e
  content: |-
    $\dfrac{x}{2}\left(\sin(\ln x)-\cos(\ln x)\right)+C$
```

---

<a id="summary"></a>
## Summary

For $\displaystyle I=\int\sin(\ln(ax))\,dx$:

1. Use $dv=dx$ so $v=x$ cancels the derivative factor $\dfrac{1}{x}$.
2. Name the resulting cosine integral $J$.
3. Apply integration by parts to $J$; the original integral returns.
4. Substitute the relation for $J$, collect the two copies of $I$, and divide by $2$.

The reusable result is

$$
\int\sin(\ln(ax))\,dx
=\frac{x}{2}\left(\sin(\ln(ax))-\cos(\ln(ax))\right)+C,
$$

on intervals where $ax>0$.
