# Expanding a Variable Power With Maclaurin Series

## Table of Contents

- [Introduction](#introduction)
- [Rewrite the Variable Power](#rewrite-the-variable-power)
- [Decide How Far to Expand](#decide-how-far-to-expand)
- [Compose and Collect the Series](#compose-and-collect-the-series)
- [Find the First Four Nonzero Terms](#find-the-first-four-nonzero-terms)

## Prerequisites

- Rewrite a positive variable power using $a^b=e^{b\ln a}$.
- Use the standard Maclaurin series for $\ln(1+x)$ and $e^u$.
- Multiply polynomials and combine like powers of $x$.

---

<a id="introduction"></a>
## Introduction

When both the base and the exponent vary, as in $(1+x)^{9x}$, the ordinary binomial expansion does not apply directly. The useful cue is the **variable exponent**.

Rewrite the function as an exponential, expand its exponent first, and then substitute that shorter series into the expansion of $e^u$. Throughout the calculation, keep only terms that can affect the requested powers of $x$.

The two standard series are

$$
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots
$$

and

$$
e^u=1+u+\frac{u^2}{2!}+\frac{u^3}{3!}+\cdots.
$$

---

<a id="rewrite-the-variable-power"></a>
## Rewrite the Variable Power

**Example:** Rewrite $(1+x)^{4x}$ in a form built from $e^u$.

**Explanation**

Near $x=0$, the base $1+x$ is positive. Therefore,

$$
(1+x)^{4x}=e^{\ln((1+x)^{4x})}=e^{4x\ln(1+x)}.
$$

The inner expression

$$
h(x)=4x\ln(1+x)
$$

is the series to expand first.

```quiz
type: radio
id: ohw8-p14-rewrite
content: |-
  Which expression is the correct exponential rewrite of $(1+x)^{7x}$ near $x=0$?
options:
- id: a
  content: |-
    $e^{7x\ln(1+x)}$
  correct: true
- id: b
  content: |-
    $e^{7\ln(1+x)}$
- id: c
  content: |-
    $e^{(1+x)\ln(7x)}$
- id: d
  content: |-
    $7x\,e^{\ln(1+x)}$
- id: e
  content: |-
    $e^{7x}(1+x)$
```

---

<a id="decide-how-far-to-expand"></a>
## Decide How Far to Expand

**Example:** Determine which pieces of the exponential series can affect $(1+x)^{6x}$ through degree $4$.

**Explanation**

First expand the inner exponent. Because it includes a factor of $x$, the logarithm is needed only through its $x^3$ term:

$$
\begin{aligned}
h(x)
&=6x\ln(1+x)\\
&=6x\left(x-\frac{x^2}{2}+\frac{x^3}{3}+O(x^4)\right)\\
&=6x^2-3x^3+2x^4+O(x^5).
\end{aligned}
$$

The key observation is that $h(x)$ starts at degree $2$. Thus,

$$
h(x)^2=O(x^4)
\qquad\text{and}\qquad
h(x)^3=O(x^6).
$$

So only

$$
e^{h(x)}=1+h(x)+\frac{h(x)^2}{2}+O(x^5)
$$

can contribute through degree $4$. The terms $h^3/3!$ and beyond begin too late.

```quiz
type: radio
id: ohw8-p14-order
content: |-
  Suppose $h(x)=3x^2-\frac{3}{2}x^3+x^4+O(x^5)$. Which terms from $e^{h(x)}$ can affect the result through degree $4$?
options:
- id: a
  content: |-
    $1+h(x)$ only
- id: b
  content: |-
    $1+h(x)+\dfrac{h(x)^2}{2}$
  correct: true
- id: c
  content: |-
    $h(x)+\dfrac{h(x)^2}{2}$ only
- id: d
  content: |-
    $1+h(x)+\dfrac{h(x)^2}{2}+\dfrac{h(x)^3}{6}$, with all four pieces contributing
- id: e
  content: |-
    Only $\dfrac{h(x)^2}{2}$
```

---

<a id="compose-and-collect-the-series"></a>
## Compose and Collect the Series

**Example:** Find the expansion of $(1+x)^{2x}$ through degree $4$.

**Explanation**

The inner exponent is

$$
\begin{aligned}
h(x)
&=2x\ln(1+x)\\
&=2x^2-x^3+\frac{2}{3}x^4+O(x^5).
\end{aligned}
$$

Since $h$ begins with $2x^2$, its square through degree $4$ is

$$
h(x)^2=(2x^2)^2+O(x^5)=4x^4+O(x^5).
$$

Now substitute into the exponential series:

$$
\begin{aligned}
(1+x)^{2x}
&=e^{h(x)}\\
&=1+h(x)+\frac{h(x)^2}{2}+O(x^5)\\
&=1+\left(2x^2-x^3+\frac{2}{3}x^4\right)+2x^4+O(x^5)\\
&=1+2x^2-x^3+\frac{8}{3}x^4+O(x^5).
\end{aligned}
$$

The $x^4$ coefficient receives contributions from both $h$ and $h^2/2$.

The same bookkeeping gives a useful check for any constant $c$:

$$
(1+x)^{cx}
=1+cx^2-\frac{c}{2}x^3
+\left(\frac{c}{3}+\frac{c^2}{2}\right)x^4+O(x^5).
$$

This formula is a check on the composition, not a replacement for noticing why the $c^2x^4/2$ term appears.

```quiz
type: radio
id: ohw8-p14-compose
content: |-
  What is the Maclaurin expansion of $(1+x)^{3x}$ through degree $4$?
options:
- id: a
  content: |-
    $1+3x^2-\dfrac{3}{2}x^3+\dfrac{11}{2}x^4+O(x^5)$
  correct: true
- id: b
  content: |-
    $1+3x^2-\dfrac{3}{2}x^3+x^4+O(x^5)$
- id: c
  content: |-
    $1+3x-\dfrac{3}{2}x^2+\dfrac{11}{2}x^3+O(x^4)$
- id: d
  content: |-
    $1+3x^2+\dfrac{3}{2}x^3+\dfrac{11}{2}x^4+O(x^5)$
- id: e
  content: |-
    $1+3x^2-\dfrac{3}{2}x^3+\dfrac{9}{2}x^4+O(x^5)$
```

---

<a id="find-the-first-four-nonzero-terms"></a>
## Find the First Four Nonzero Terms

**Example:** Find the first four nonzero terms of

$$
f(x)=(1+x)^{9x}.
$$

**Explanation**

Rewrite the function and expand its exponent:

$$
\begin{aligned}
f(x)
&=e^{9x\ln(1+x)},\\
h(x)
&=9x\ln(1+x)\\
&=9x^2-\frac{9}{2}x^3+3x^4+O(x^5).
\end{aligned}
$$

Because $h(x)$ starts at degree $2$,

$$
h(x)^2=81x^4+O(x^5),
$$

and no higher power of $h$ affects degree $4$. Therefore,

$$
\begin{aligned}
f(x)
&=1+h(x)+\frac{h(x)^2}{2}+O(x^5)\\
&=1+9x^2-\frac{9}{2}x^3+\left(3+\frac{81}{2}\right)x^4+O(x^5)\\
&=1+9x^2-\frac{9}{2}x^3+\frac{87}{2}x^4+O(x^5).
\end{aligned}
$$

There is no $x$ term, so the first four nonzero terms are the constant, $x^2$, $x^3$, and $x^4$ terms:

$$
\boxed{1+9x^2-\frac{9}{2}x^3+\frac{87}{2}x^4}.
$$

```quiz
type: radio
id: ohw8-p14-final
content: |-
  Find the first four nonzero terms of $(1+x)^{5x}$.
options:
- id: a
  content: |-
    $1+5x^2-\dfrac{5}{2}x^3+\dfrac{85}{6}x^4$
  correct: true
- id: b
  content: |-
    $1+5x^2-\dfrac{5}{2}x^3+\dfrac{5}{3}x^4$
- id: c
  content: |-
    $1+5x-\dfrac{5}{2}x^2+\dfrac{85}{6}x^3$
- id: d
  content: |-
    $1+5x^2+\dfrac{5}{2}x^3+\dfrac{85}{6}x^4$
- id: e
  content: |-
    $5x^2-\dfrac{5}{2}x^3+\dfrac{85}{6}x^4+\dfrac{25}{2}x^5$
```

---

## Summary

For a variable power such as $(1+x)^{cx}$:

1. Rewrite it as $e^{cx\ln(1+x)}$.
2. Expand the inner exponent only as far as the requested degree requires.
3. Note its starting degree: here $cx\ln(1+x)=O(x^2)$, so its square first contributes at $x^4$ and its cube first contributes at $x^6$.
4. Substitute into $e^u$, collect like powers, and count nonzero terms rather than merely counting degrees.

The main trap is dropping $h(x)^2/2$, which changes the coefficient of $x^4$.
