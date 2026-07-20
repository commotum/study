# Finding a Density Constant from Total Mass

## Table of Contents

- [Introduction](#introduction)
- [Turn Density into a Mass Equation](#turn-density-into-a-mass-equation)
- [Integrate a Power-Law Density](#integrate-a-power-law-density)
- [Solve for the Density Constant](#solve-for-the-density-constant)
- [Check the Result](#check-the-result)
- [Summary](#summary)

## Prerequisites

- Interpret linear mass density as mass per unit length.
- Evaluate a definite integral with the power rule.
- Isolate a variable in a one-step equation.

---

<a id="introduction"></a>
## Introduction

When a rod's linear density $\lambda(x)$ varies with position, multiplying one density value by the rod's length does not give the total mass. The cue is a density function together with a known total mass and an unknown coefficient.

Accumulate the density over the entire rod:

$$
m=\int_a^b \lambda(x)\,dx.
$$

Then evaluate the integral and solve the resulting equation for the unknown coefficient.

For the common power-law case $\lambda(x)=kx^n$ on $0\le x\le L$, with $n>-1$, the entire procedure compresses to

$$
M=\int_0^L kx^n\,dx=\frac{kL^{n+1}}{n+1}
\quad\Longrightarrow\quad
k=\frac{(n+1)M}{L^{n+1}}.
$$

Read this as a sequence: **use the endpoints, integrate, then isolate the coefficient**.

---

<a id="turn-density-into-a-mass-equation"></a>
## Turn Density into a Mass Equation

**Example:** A rod occupies $0\le x\le L$ and has density $\lambda(x)=kx$. Write an equation relating its total mass $M$ to $k$ and $L$.

**Explanation**

The rod starts at $x=0$ and ends at $x=L$, so those positions become the limits of integration:

$$
M=\int_0^L \lambda(x)\,dx=\int_0^L kx\,dx.
$$

The left side is the whole mass; the right side adds the mass of all the thin pieces along the rod.

```quiz
type: radio
id: p3-mass-equation
content: |-
  A rod extends from $x=0$ to $x=R$ and has linear density $\lambda(x)=ax^2$. Which equation correctly represents its total mass $M$?
options:
- id: a
  content: |-
    $M=aR^2$
- id: b
  content: |-
    $M=\displaystyle\int_0^R ax^2\,dx$
  correct: true
- id: c
  content: |-
    $M=\displaystyle\int_0^M ax^2\,dx$
- id: d
  content: |-
    $M=\displaystyle\int_0^R a\,dx$
```

---

<a id="integrate-a-power-law-density"></a>
## Integrate a Power-Law Density

**Example:** Evaluate the mass integral for $\lambda(x)=kx^2$ on $0\le x\le L$.

**Explanation**

Because $k$ is constant with respect to $x$, keep it as a factor and apply the power rule:

$$
\begin{aligned}
M&=\int_0^L kx^2\,dx\\
&=k\left[\frac{x^3}{3}\right]_0^L\\
&=k\left(\frac{L^3}{3}-0\right)\\
&=\frac{kL^3}{3}.
\end{aligned}
$$

The exponent on $L$ is $3$ because integrating $x^2$ raises its exponent by one. Since this is a definite integral, evaluating the endpoints produces a number; do not attach a $+C$ to the final mass.

```quiz
type: radio
id: p3-integrate-density
content: |-
  A rod occupies $0\le x\le R$ and has $\lambda(x)=ax^3$. What is its total mass in terms of $a$ and $R$?
options:
- id: a
  content: |-
    $aR^3$
- id: b
  content: |-
    $\dfrac{aR^3}{3}$
- id: c
  content: |-
    $\dfrac{aR^4}{4}$
  correct: true
- id: d
  content: |-
    $4aR^4$
```

---

<a id="solve-for-the-density-constant"></a>
## Solve for the Density Constant

**Example:** A rod of total mass $M$ and length $L$ has $\lambda(x)=kx^2$ on $0\le x\le L$. Find $k$.

**Explanation**

Use the mass relation from the previous section:

$$
M=\frac{kL^3}{3}.
$$

Multiply by $3$ and divide by $L^3$:

$$
k=\frac{3M}{L^3}.
$$

The factor $3$ belongs in the numerator; it comes from undoing the division by $3$ in the integral.

More generally, if $\lambda(x)=ax^n$ on $0\le x\le R$, then

$$
M=\frac{aR^{n+1}}{n+1}
\quad\Longrightarrow\quad
a=\frac{(n+1)M}{R^{n+1}}.
$$

This is the same three-step move, not a new formula to memorize: integrate, evaluate at $R$ and $0$, and isolate $a$.

```quiz
type: radio
id: p3-isolate-constant
content: |-
  A rod of mass $M$ occupies $0\le x\le R$ and has $\lambda(x)=ax^4$. What is $a$?
options:
- id: a
  content: |-
    $\dfrac{M}{5R^5}$
- id: b
  content: |-
    $\dfrac{5M}{R^5}$
  correct: true
- id: c
  content: |-
    $\dfrac{5M}{R^4}$
- id: d
  content: |-
    $\dfrac{MR^5}{5}$
```

---

<a id="check-the-result"></a>
## Check the Result

**Example:** Check whether $k=3M/L^3$ has the correct units when $\lambda(x)=kx^2$.

**Explanation**

Linear density has units of mass per length. Since $x^2$ contributes units of length squared,

$$
[k]=\frac{\text{mass}/\text{length}}{\text{length}^2}
=\frac{\text{mass}}{\text{length}^3}.
$$

The expression $3M/L^3$ has exactly these units. Substitution gives a second check:

$$
\int_0^L \frac{3M}{L^3}x^2\,dx
=\frac{3M}{L^3}\cdot\frac{L^3}{3}
=M.
$$

```quiz
type: radio
id: p3-original-check
content: |-
  A thin rod of mass $m$ and length $l$ lies along the $x$-axis from $x=0$ to $x=l$ and has linear mass density $\lambda(x)=cx^2$. What is $c$ in terms of $m$ and $l$?
options:
- id: a
  content: |-
    $\dfrac{m}{6l^3}$
- id: b
  content: |-
    $\dfrac{3m}{l^3}$
  correct: true
```

---

<a id="summary"></a>
## Summary

When a density function contains an unknown constant and the total mass is known:

1. Use the rod's endpoints as the limits in $m=\int_a^b\lambda(x)\,dx$.
2. Pull out coefficients that are constant with respect to position, then integrate the density over the entire rod.
3. Solve the resulting equation for the constant.
4. Check that the units fit the density and that substituting the constant reproduces the total mass.

For $\lambda(x)=cx^2$ on $0\le x\le l$, the main traps are using only the endpoint density $cl^2$, forgetting that $\int_0^l x^2\,dx=l^3/3$, or leaving the factor $3$ in the denominator when isolating $c$. Thus $m=cl^3/3$ and $c=3m/l^3$.
