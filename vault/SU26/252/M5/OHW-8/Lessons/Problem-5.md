# Integrating Powers of $\ln(10x)$ by Parts

## Table of Contents

- [Introduction](#introduction)
- [Reveal the Implicit Factor and Choose Parts](#reveal-the-implicit-factor-and-choose-parts)
- [Build a Reduction Formula](#build-a-reduction-formula)
- [Unwind Until the Power Reaches Zero](#unwind-until-the-power-reaches-zero)
- [Evaluate the Fourth Power](#evaluate-the-fourth-power)
- [Differentiate to Check the Pattern](#differentiate-to-check-the-pattern)
- [Summary](#summary)

## Prerequisites

- Use integration by parts: $\int u\,dv=uv-\int v\,du$.
- Differentiate $\ln(kx)$ for a positive constant $k$: $\dfrac{d}{dx}\ln(kx)=\dfrac1x$ on $x>0$.
- Apply the power and chain rules.

---

<a id="introduction"></a>
## Introduction

The recognition cue is a positive integer power of a logarithm **without** a matching $1/x$ factor. If $1/x$ were present, substitution with the logarithm could work directly. Here it is absent, so reveal the implicit factor $1$:

$$
\int(\ln(10x))^n\,dx
=\int(\ln(10x))^n\cdot 1\,dx.
$$

Then choose

$$
u=(\ln(10x))^n,\qquad dv=dx.
$$

Integration by parts creates a factor $x$ by integrating $1$; that $x$ cancels the $1/x$ produced when the logarithm is differentiated. The result is the same kind of integral with its logarithmic exponent lowered by one. Repeating that same choice eventually reaches $\int 1\,dx$. The key derivative is

$$
\frac{d}{dx}\ln(10x)=\frac{10}{10x}=\frac1x,
$$

so there is no extra factor of $10$ in the reduction.

---

<a id="reveal-the-implicit-factor-and-choose-parts"></a>
## Reveal the Implicit Factor and Choose Parts

**Example:** Set up integration by parts for

$$
\int(\ln(4x))^2\,dx.
$$

**Explanation**

First write the integrand as $(\ln(4x))^2\cdot1$. Choose the logarithmic power as $u$ and the implicit factor $1$ as $dv$:

$$
u=(\ln(4x))^2,\qquad dv=dx.
$$

Then

$$
du=2\ln(4x)\frac1x\,dx,\qquad v=x.
$$

The factor $x$ from $v$ cancels the factor $1/x$ in $du$:

$$
\int(\ln(4x))^2\,dx
=x(\ln(4x))^2-2\int\ln(4x)\,dx.
$$

The new integral has the same form, but its logarithmic power has dropped from $2$ to $1$.

```quiz
type: radio
id: p5-q1
content: |-
  Which integration-by-parts setup lowers the logarithmic power in $\int(\ln(3x))^3\,dx$?
options:
- id: p5-q1-a
  content: |-
    $u=1$ and $dv=(\ln(3x))^3\,dx$
- id: p5-q1-b
  content: |-
    $u=(\ln(3x))^3$ and $dv=dx$
  correct: true
- id: p5-q1-c
  content: |-
    $u=x$ and $dv=(\ln(3x))^3\,dx$
- id: p5-q1-d
  content: |-
    $u=\ln(3x)$ and $dv=(\ln(3x))^2\,dx$
- id: p5-q1-e
  content: |-
    $u=3x$ and $dv=(\ln(3x))^3\,dx$
```

---

<a id="build-a-reduction-formula"></a>
## Build a Reduction Formula

Let

$$
I_n=\int(\ln(kx))^n\,dx,
$$

where $k>0$ and $n$ is a positive integer. With

$$
u=(\ln(kx))^n,\qquad dv=dx,
$$

we have

$$
du=n(\ln(kx))^{n-1}\frac1x\,dx,\qquad v=x.
$$

Substitution into integration by parts gives the reusable reduction formula

$$
\boxed{I_n=x(\ln(kx))^n-nI_{n-1}}.
$$

**Example:** Reduce $I_4=\int(\ln(2x))^4\,dx$ by one power.

**Explanation**

The parts choice is still

$$
u=(\ln(2x))^4,\qquad du=4(\ln(2x))^3\frac1x\,dx,
$$

and

$$
dv=dx,\qquad v=x.
$$

Equivalently, insert $n=4$ into the reduction formula:

$$
I_4=x(\ln(2x))^4-4I_3.
$$

Only the exponent and its multiplier change; the same logarithm $\ln(2x)$ remains.

```quiz
type: radio
id: p5-q2
content: |-
  If $I_n=\int(\ln(8x))^n\,dx$, which equation correctly reduces $I_5$?
options:
- id: p5-q2-a
  content: |-
    $I_5=x(\ln(8x))^5-5I_4$
  correct: true
- id: p5-q2-b
  content: |-
    $I_5=x(\ln(8x))^5-I_4$
- id: p5-q2-c
  content: |-
    $I_5=x(\ln(8x))^5+5I_4$
- id: p5-q2-d
  content: |-
    $I_5=x(\ln(8x))^4-5I_4$
- id: p5-q2-e
  content: |-
    $I_5=8x(\ln(8x))^5-5I_4$
```

---

<a id="unwind-until-the-power-reaches-zero"></a>
## Unwind Until the Power Reaches Zero

Each reduction produces a simpler integral because the exponent drops by one. Continue until the reduction reaches

$$
I_0=\int 1\,dx=x.
$$

**Example:** Evaluate $\int(\ln(5x))^3\,dx$.

**Explanation**

Apply the same reduction repeatedly:

$$
\begin{aligned}
I_3
&=x(\ln(5x))^3-3I_2\\
&=x(\ln(5x))^3-3\left[x(\ln(5x))^2-2I_1\right]\\
&=x(\ln(5x))^3-3x(\ln(5x))^2+6I_1.
\end{aligned}
$$

Since

$$
I_1=x\ln(5x)-I_0=x\ln(5x)-x,
$$

we get

$$
\int(\ln(5x))^3\,dx
=x\left[(\ln(5x))^3-3(\ln(5x))^2+6\ln(5x)-6\right]+C.
$$

The signs alternate because each reduction subtracts the next lower integral. The coefficients accumulate as $1$, $3$, $3\cdot2$, and $3\cdot2\cdot1$. Only the final antiderivative needs an arbitrary constant; any constants introduced while evaluating the nested integrals are absorbed into that final $C$.

```quiz
type: radio
id: p5-q3
content: |-
  Which expression is an antiderivative of $(\ln(9x))^2$?
options:
- id: p5-q3-a
  content: |-
    $x\left[(\ln(9x))^2-2\ln(9x)+2\right]+C$
  correct: true
- id: p5-q3-b
  content: |-
    $x\left[(\ln(9x))^2-\ln(9x)+1\right]+C$
- id: p5-q3-c
  content: |-
    $x\left[(\ln(9x))^2+2\ln(9x)+2\right]+C$
- id: p5-q3-d
  content: |-
    $x\left[(\ln(9x))^2-2\ln(9x)\right]+C$
- id: p5-q3-e
  content: |-
    $9x\left[(\ln(9x))^2-2\ln(9x)+2\right]+C$
```

---

<a id="evaluate-the-fourth-power"></a>
## Evaluate the Fourth Power

**Example:** Evaluate the assigned integral

$$
\int(\ln(10x))^4\,dx.
$$

**Explanation**

Write $L=\ln(10x)$ temporarily. Then

$$
\begin{aligned}
I_4
&=xL^4-4I_3\\
&=xL^4-4\left(xL^3-3I_2\right)\\
&=xL^4-4xL^3+12\left(xL^2-2I_1\right)\\
&=xL^4-4xL^3+12xL^2-24\left(xL-x\right).
\end{aligned}
$$

Therefore,

$$
\boxed{
\int(\ln(10x))^4\,dx
=x\left[(\ln(10x))^4-4(\ln(10x))^3+12(\ln(10x))^2-24\ln(10x)+24\right]+C
}.
$$

```quiz
type: radio
id: p5-q4
content: |-
  Which expression is an antiderivative of $(\ln(6x))^4$?
options:
- id: p5-q4-a
  content: |-
    $x\left[(\ln(6x))^4-4(\ln(6x))^3+12(\ln(6x))^2-24\ln(6x)+24\right]+C$
  correct: true
- id: p5-q4-b
  content: |-
    $x\left[(\ln(6x))^4-4(\ln(6x))^3+12(\ln(6x))^2-24\ln(6x)\right]+C$
- id: p5-q4-c
  content: |-
    $x\left[(\ln(6x))^4+4(\ln(6x))^3+12(\ln(6x))^2+24\ln(6x)+24\right]+C$
- id: p5-q4-d
  content: |-
    $x\left[(\ln(6x))^4-4(\ln(6x))^3+8(\ln(6x))^2-24\ln(6x)+24\right]+C$
- id: p5-q4-e
  content: |-
    $6x\left[(\ln(6x))^4-4(\ln(6x))^3+12(\ln(6x))^2-24\ln(6x)+24\right]+C$
```

---

<a id="differentiate-to-check-the-pattern"></a>
## Differentiate to Check the Pattern

**Example:** Check

$$
F(x)=x\left[(\ln(4x))^2-2\ln(4x)+2\right].
$$

**Explanation**

Let $L=\ln(4x)$, so $L'=1/x$. The product rule gives

$$
\begin{aligned}
F'(x)
&=(L^2-2L+2)+x(2L-2)\frac1x\\
&=L^2-2L+2+2L-2\\
&=L^2\\
&=(\ln(4x))^2.
\end{aligned}
$$

The lower-power terms cancel. This cancellation is a quick way to detect a missing coefficient, a wrong sign, or a false extra factor from differentiating $\ln(kx)$.

```quiz
type: radio
id: p5-q5
content: |-
  When differentiating $\ln(10x)$ as part of the check, what derivative should be used?
options:
- id: p5-q5-a
  content: |-
    $\dfrac1x$
  correct: true
- id: p5-q5-b
  content: |-
    $\dfrac{10}{x}$
- id: p5-q5-c
  content: |-
    $\dfrac1{10x}$
- id: p5-q5-d
  content: |-
    $10$
- id: p5-q5-e
  content: |-
    $\ln(10)$
```

---

<a id="summary"></a>
## Summary

For $\int(\ln(kx))^n\,dx$ with $k>0$ and positive integer $n$:

1. Look for a logarithmic power with no matching $1/x$ factor, and reveal the implicit factor $1$.
2. Choose $u=(\ln(kx))^n$ and $dv=dx$.
3. Use $\dfrac{d}{dx}\ln(kx)=1/x$; the constant $k$ does not leave an extra factor.
4. Apply $I_n=x(\ln(kx))^n-nI_{n-1}$ repeatedly.
5. Stop at $I_0=x$, include one final $C$, and differentiate to check that the lower powers cancel.

For the assigned fourth power, the coefficient and sign pattern is

$$
x\left[L^4-4L^3+12L^2-24L+24\right]+C,
\qquad L=\ln(10x).
$$
