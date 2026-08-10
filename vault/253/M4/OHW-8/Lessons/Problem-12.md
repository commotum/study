# Summing a Power Series by Integrating a Known Series

## Table of Contents

- [Introduction](#introduction)
- [Recognize the Integrated Logarithm Series](#recognize-the-integrated-logarithm-series)
- [Evaluate the Definite Integral](#evaluate-the-definite-integral)
- [Use the Same Move with a Sign Change](#use-the-same-move-with-a-sign-change)
- [Check the Result](#check-the-result)
- [Include the Endpoints](#include-the-endpoints)

## Prerequisites

- Recognize the power series $\displaystyle -\ln(1-x)=\sum_{k=1}^{\infty}\frac{x^k}{k}$.
- Integrate powers and logarithmic functions.
- Use the Fundamental Theorem of Calculus.

---

<a id="introduction"></a>
## Introduction

The factor $k(k+1)$ in

$$
\sum_{k=1}^{\infty}\frac{x^{k+1}}{k(k+1)}
$$

is a recognition cue. The factor $1/k$ appears in the series for $-\ln(1-x)$, while integrating $x^k$ supplies the extra factor $1/(k+1)$ and raises the power to $x^{k+1}$.

The useful move is therefore to integrate the known logarithm series from $0$ to $x$. Definite integration fixes the constant automatically.

---

<a id="recognize-the-integrated-logarithm-series"></a>
## Recognize the Integrated Logarithm Series

**Example:** Rewrite $\displaystyle \sum_{k=1}^{\infty}\frac{x^{k+1}}{k(k+1)}$ as a definite integral.

**Explanation**

Start with

$$
-\ln(1-t)=\sum_{k=1}^{\infty}\frac{t^k}{k}, \qquad |t|<1.
$$

Use $t$ as the integration variable so that $x$ remains the upper limit. Integrating from $0$ to $x$ gives

$$
\begin{aligned}
\int_0^x-\ln(1-t)\,dt
&=\sum_{k=1}^{\infty}\int_0^x\frac{t^k}{k}\,dt\\
&=\sum_{k=1}^{\infty}\frac{x^{k+1}}{k(k+1)}.
\end{aligned}
$$

```quiz
type: radio
id: ohw8-p12-recognize
content: |-
  Which operation turns $\displaystyle \sum_{k=1}^{\infty}\frac{x^k}{k}$ into $\displaystyle \sum_{k=1}^{\infty}\frac{x^{k+1}}{k(k+1)}$?
options:
- id: a
  content: |-
    Differentiate term by term.
- id: b
  content: |-
    Integrate term by term from $0$ to $x$.
  correct: true
- id: c
  content: |-
    Multiply every term by $x$.
- id: d
  content: |-
    Replace $x$ with $x^2$.
- id: e
  content: |-
    Divide the whole series by $x$.
```

---

<a id="evaluate-the-definite-integral"></a>
## Evaluate the Definite Integral

**Example:** Find an elementary expression for the target series.

**Explanation**

An antiderivative of $-\ln(1-t)$ is

$$
(1-t)\ln(1-t)-(1-t).
$$

Therefore,

$$
\begin{aligned}
\sum_{k=1}^{\infty}\frac{x^{k+1}}{k(k+1)}
&=\int_0^x-\ln(1-t)\,dt\\
&=\left[(1-t)\ln(1-t)-(1-t)\right]_0^x\\
&=x+(1-x)\ln(1-x), \qquad |x|<1.
\end{aligned}
$$

```quiz
type: radio
id: ohw8-p12-evaluate
content: |-
  For $|x|<1$, what is $\displaystyle \int_0^x-\ln(1-t)\,dt$?
options:
- id: a
  content: |-
    $x+(1-x)\ln(1-x)$
  correct: true
- id: b
  content: |-
    $x-(1-x)\ln(1-x)$
- id: c
  content: |-
    $(1-x)\ln(1-x)$
- id: d
  content: |-
    $-x+(1-x)\ln(1-x)$
- id: e
  content: |-
    $x+\ln(1-x)$
```

---

<a id="use-the-same-move-with-a-sign-change"></a>
## Use the Same Move with a Sign Change

**Example:** Find an elementary expression for

$$
\sum_{k=1}^{\infty}\frac{(-1)^{k+1}x^{k+1}}{k(k+1)}.
$$

**Explanation**

The alternating factor points to the companion logarithm series

$$
\ln(1+t)=\sum_{k=1}^{\infty}\frac{(-1)^{k+1}t^k}{k}.
$$

Integrating from $0$ to $x$ performs the same exponent-and-denominator change:

$$
\begin{aligned}
\sum_{k=1}^{\infty}\frac{(-1)^{k+1}x^{k+1}}{k(k+1)}
&=\int_0^x\ln(1+t)\,dt\\
&=(1+x)\ln(1+x)-x.
\end{aligned}
$$

Only the starting logarithm series changed; the integration move did not.

```quiz
type: radio
id: ohw8-p12-sign-variant
content: |-
  For $|x|<1$, what is $\displaystyle \sum_{k=1}^{\infty}\frac{(-1)^{k+1}x^{k+1}}{k(k+1)}$?
options:
- id: a
  content: |-
    $(1+x)\ln(1+x)-x$
  correct: true
- id: b
  content: |-
    $(1-x)\ln(1-x)+x$
- id: c
  content: |-
    $(1+x)\ln(1+x)+x$
- id: d
  content: |-
    $\ln(1+x)-x$
- id: e
  content: |-
    $x-(1+x)\ln(1+x)$
```

---

<a id="check-the-result"></a>
## Check the Result

**Example:** Verify $F(x)=x+(1-x)\ln(1-x)$ without redoing the integration.

**Explanation**

Differentiate the proposed sum:

$$
\begin{aligned}
F'(x)
&=1-\ln(1-x)-1\\
&=-\ln(1-x).
\end{aligned}
$$

Also, $F(0)=0$, matching the integrated series at $x=0$. The derivative and the base value together verify the formula.

```quiz
type: radio
id: ohw8-p12-check
content: |-
  A proposed sum $G(x)$ satisfies $G'(x)=-\ln(1-x)$. What additional fact fixes the integration constant and verifies the target series?
options:
- id: a
  content: |-
    $G(0)=0$
  correct: true
- id: b
  content: |-
    $G(0)=1$
- id: c
  content: |-
    $G'(0)=0$
- id: d
  content: |-
    $G(1)=0$
- id: e
  content: |-
    $G''(0)=0$
```

---

<a id="include-the-endpoints"></a>
## Include the Endpoints

**Example:** Determine whether the target series also converges at $x=-1$ and $x=1$.

**Explanation**

At either endpoint, the absolute values of the terms are

$$
\frac{1}{k(k+1)}=\frac{1}{k}-\frac{1}{k+1}.
$$

This telescoping series converges, so both endpoints belong to the interval of convergence. The elementary formula already gives

$$
F(-1)=-1+2\ln 2.
$$

At $x=1$, interpret the formula by continuity. Since

$$
\lim_{x\to1^-}(1-x)\ln(1-x)=0,
$$

the endpoint sum is $F(1)=1$. Thus the series converges for $-1\le x\le1$, with the displayed logarithmic formula used directly for $-1\le x<1$ and by its limiting value at $x=1$.

```quiz
type: radio
id: ohw8-p12-endpoint
content: |-
  What is $\displaystyle \sum_{k=1}^{\infty}\frac{1}{k(k+1)}$?
options:
- id: a
  content: |-
    $0$
- id: b
  content: |-
    $1$
  correct: true
- id: c
  content: |-
    $\ln 2$
- id: d
  content: |-
    $2$
- id: e
  content: |-
    The series diverges.
```

---

## Summary

When a power series contains $x^{k+1}/[k(k+1)]$, recognize the $1/k$ from the logarithm series and the $1/(k+1)$ as the result of integrating $x^k$. Integrate from $0$ to $x$ to avoid an unknown constant, evaluate the elementary integral, and check both the derivative and the value at $x=0$. The main traps are losing the minus sign in $-\ln(1-x)$, omitting the base value, and forgetting to test the endpoints separately.

$$
\boxed{\displaystyle \sum_{k=1}^{\infty}\frac{x^{k+1}}{k(k+1)}=x+(1-x)\ln(1-x)} \qquad (|x|<1).
$$

The series also converges at $x=-1$ and $x=1$; at $x=1$, the sum is the limiting value $1$.
