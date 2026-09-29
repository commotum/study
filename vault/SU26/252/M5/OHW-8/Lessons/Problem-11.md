# Integrating a Trigonometric Function of $\ln x$

## Table of Contents

- [Introduction](#introduction)
- [Rewrite the Integral in Terms of $t$](#rewrite-in-t)
- [Use Integration by Parts Twice](#parts-twice)
- [Evaluate the Original Integral](#original-integral)
- [Check the Required $x$-Factor](#check-factor)
- [Summary](#summary)

## Prerequisites

- The substitution $t=\ln x$, so $x=e^t$ and $dx=e^t\,dt$
- Integration by parts: $\int u\,dv=uv-\int v\,du$
- The product rule

---

<a id="introduction"></a>
## Introduction

When an integral contains $\cos(\ln x)$ but does not contain a factor of $1/x$, the substitution $t=\ln x$ does not make the differential disappear by itself. Instead, it changes $dx$ into $e^t\,dt$, revealing an exponential-trigonometric integral:

$$
\int \cos(\ln x)\,dx
=
\int e^t\cos t\,dt.
$$

The useful procedure is to make this substitution, apply integration by parts twice, and solve for the integral that returns.

Because $\ln x$ is defined here for $x>0$, all substitutions and derivative checks in this lesson use $x>0$.

---

<a id="rewrite-in-t"></a>
## Rewrite the Integral in Terms of $t$

**Example:** Rewrite

$$
\int 4\cos(\ln x)\,dx
$$

using $t=\ln x$.

**Explanation**

From $t=\ln x$, we get $x=e^t$ and

$$
dx=e^t\,dt.
$$

The constant stays outside:

$$
\int 4\cos(\ln x)\,dx
=
4\int e^t\cos t\,dt.
$$

The factor $e^t$ is essential. Writing only $dt$ in place of $dx$ would incorrectly treat $dt=dx$, even though $dt=dx/x$.

```quiz
type: radio
id: p11-rewrite-1
content: |-
  After the substitution $t=\ln x$, which integral is equivalent to
  $$
  \int 8\cos(\ln x)\,dx?
  $$
options:
- id: a
  content: |-
    $8\int e^t\cos t\,dt$
  correct: true
- id: b
  content: |-
    $8\int \cos t\,dt$
- id: c
  content: |-
    $8\int t\cos t\,dt$
- id: d
  content: |-
    $8\int e^t\cos(e^t)\,dt$
- id: e
  content: |-
    $8\int e^{-t}\cos t\,dt$
```

---

<a id="parts-twice"></a>
## Use Integration by Parts Twice

**Example:** Evaluate

$$
I=\int e^t\cos t\,dt.
$$

**Explanation**

First choose $u=\cos t$ and $dv=e^t\,dt$. Then $du=-\sin t\,dt$ and $v=e^t$, so

$$
I=e^t\cos t+J,
$$

where

$$
J=\int e^t\sin t\,dt.
$$

For $J$, choose $u=\sin t$ and $dv=e^t\,dt$. Then $du=\cos t\,dt$ and $v=e^t$, giving

$$
J
=
e^t\sin t-\int e^t\cos t\,dt
=
e^t\sin t-I.
$$

Now substitute the equation for $J$ into the equation for $I$:

$$
\begin{aligned}
I&=e^t\cos t+J \\
&=e^t\cos t+e^t\sin t-I.
\end{aligned}
$$

The original integral has returned. Collect the two copies of $I$:

$$
2I=e^t(\cos t+\sin t),
$$

so

$$
I=\frac{e^t}{2}(\cos t+\sin t)+C.
$$

```quiz
type: radio
id: p11-parts-1
content: |-
  Suppose two rounds of integration by parts give
  $$
  J=e^t\sin t-e^t\cos t-J.
  $$
  What is $J$?
options:
- id: a
  content: |-
    $\dfrac{e^t}{2}(\sin t-\cos t)+C$
  correct: true
- id: b
  content: |-
    $e^t(\sin t-\cos t)+C$
- id: c
  content: |-
    $\dfrac{e^t}{2}(\sin t+\cos t)+C$
- id: d
  content: |-
    $\dfrac{e^t}{2}(\cos t-\sin t)+C$
- id: e
  content: |-
    $e^t\sin t-e^t\cos t-J+C$
```

---

<a id="original-integral"></a>
## Evaluate the Original Integral

**Example:** Evaluate

$$
\int 12\cos(\ln x)\,dx.
$$

**Explanation**

Let $t=\ln x$. Because $e^t=x$,

$$
\int 12\cos(\ln x)\,dx
=
12\int e^t\cos t\,dt.
$$

Use the result from the previous section:

$$
12\int e^t\cos t\,dt
=
12\left[\frac{e^t}{2}(\cos t+\sin t)\right]+C.
$$

Substitute $e^t=x$ and $t=\ln x$:

$$
\boxed{6x\bigl(\cos(\ln x)+\sin(\ln x)\bigr)+C}.
$$

```quiz
type: radio
id: p11-original-1
content: |-
  Evaluate
  $$
  \int 10\cos(\ln x)\,dx.
  $$
options:
- id: a
  content: |-
    $5x\bigl(\cos(\ln x)+\sin(\ln x)\bigr)+C$
  correct: true
- id: b
  content: |-
    $10x\bigl(\cos(\ln x)+\sin(\ln x)\bigr)+C$
- id: c
  content: |-
    $5\bigl(\cos(\ln x)+\sin(\ln x)\bigr)+C$
- id: d
  content: |-
    $5x\bigl(\cos(\ln x)-\sin(\ln x)\bigr)+C$
- id: e
  content: |-
    $10\sin(\ln x)+C$
```

---

<a id="check-factor"></a>
## Check the Required $x$-Factor

**Example:** Verify the antiderivative

$$
F(x)=6x\bigl(\cos(\ln x)+\sin(\ln x)\bigr).
$$

**Explanation**

Differentiate using the product rule and $d(\ln x)/dx=1/x$:

$$
\begin{aligned}
F'(x)
&=6\bigl(\cos(\ln x)+\sin(\ln x)\bigr) \\
&\quad+6x\left(-\frac{\sin(\ln x)}{x}+\frac{\cos(\ln x)}{x}\right) \\
&=12\cos(\ln x).
\end{aligned}
$$

The sine terms cancel and the cosine terms combine. This also shows why an answer without the outer factor $x$ cannot be correct.

```quiz
type: radio
id: p11-check-1
content: |-
  Which derivative confirms that
  $$
  3x\bigl(\cos(\ln x)+\sin(\ln x)\bigr)
  $$
  is an antiderivative of the stated integrand?
options:
- id: a
  content: |-
    $6\cos(\ln x)$
  correct: true
- id: b
  content: |-
    $3\cos(\ln x)$
- id: c
  content: |-
    $6\sin(\ln x)$
- id: d
  content: |-
    $\dfrac{6\cos(\ln x)}{x}$
- id: e
  content: |-
    $3\bigl(\cos(\ln x)+\sin(\ln x)\bigr)$
```

---

<a id="summary"></a>
## Summary

For an integral containing $\cos(\ln x)$ without a $1/x$ factor:

1. Let $t=\ln x$, so $x=e^t$ and $dx=e^t\,dt$.
2. Apply integration by parts twice to $\int e^t\cos t\,dt$.
3. When the original integral returns, move it to the other side and divide by $2$.
4. Substitute $e^t=x$ and $t=\ln x$.

The reusable result is

$$
\int \cos(\ln x)\,dx
=
\frac{x}{2}\bigl(\cos(\ln x)+\sin(\ln x)\bigr)+C.
$$

The main trap is losing the factor $e^t$ during substitution, which would also remove the necessary factor $x$ from the final answer.
