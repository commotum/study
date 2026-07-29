# Integrating a Radical Times an Odd Cosine Power

## Table of Contents

- [Introduction](#introduction)
- [Save One Cosine Factor](#save-cosine)
- [Integrate the Fractional Powers](#fractional-powers)
- [Evaluate the Original Integral](#original-integral)
- [Check by Differentiation](#check)
- [Summary](#summary)

## Prerequisites

- The identity $\cos^2x=1-\sin^2x$
- Substitution in indefinite integrals
- The power rule for antiderivatives

---

<a id="introduction"></a>
## Introduction

When an integrand contains an odd positive power of cosine and the other factor is built from sine, save one cosine factor. Rewrite the remaining even cosine power with

$$
\cos^2x=1-\sin^2x.
$$

Then the substitution

$$
u=\sin x,
\qquad
du=\cos x\,dx
$$

turns the integrand into powers of $u$. A square root becomes a fractional exponent:

$$
\sqrt{\sin x}=(\sin x)^{1/2}=u^{1/2}.
$$

For a real-valued antiderivative, work on an interval where $\sin x\geq 0$; the differentiation check is direct where $\sin x>0$.

---

<a id="save-cosine"></a>
## Save One Cosine Factor

**Example:** Rewrite

$$
(\sin x)^{3/2}\cos^3x
$$

in a form prepared for $u=\sin x$.

**Explanation**

Split the odd cosine power:

$$
\cos^3x=\cos^2x\cos x.
$$

Use $\cos^2x=1-\sin^2x$:

$$
(\sin x)^{3/2}\cos^3x
=
(\sin x)^{3/2}(1-\sin^2x)\cos x.
$$

Everything except the saved $\cos x$ is now a power or polynomial in $\sin x$.

```quiz
type: radio
id: whw5-p4-rewrite-1
content: |-
  Which rewrite prepares
  $$
  \sqrt{\sin x}\cos^5x
  $$
  for the substitution $u=\sin x$?
options:
- id: a
  content: |-
    $\sqrt{\sin x}(1-\sin^2x)^2\cos x$
  correct: true
- id: b
  content: |-
    $\sqrt{\sin x}(1+\sin^2x)^2\cos x$
- id: c
  content: |-
    $\sqrt{\sin x}(1-\sin x)^2\cos x$
- id: d
  content: |-
    $\sqrt{\sin x}(1-\cos^2x)^2\sin x$
- id: e
  content: |-
    $\sqrt{\sin x}(1-\sin^2x)\cos x$
```

---

<a id="fractional-powers"></a>
## Integrate the Fractional Powers

**Example:** Evaluate

$$
\int(\sin x)^{3/2}\cos^3x\,dx.
$$

**Explanation**

Save one cosine factor and rewrite the other two:

$$
\int(\sin x)^{3/2}(1-\sin^2x)\cos x\,dx.
$$

Let $u=\sin x$, so $du=\cos x\,dx$. Then

$$
\begin{aligned}
\int(\sin x)^{3/2}\cos^3x\,dx
&=\int u^{3/2}(1-u^2)\,du \\
&=\int\left(u^{3/2}-u^{7/2}\right)\,du \\
&=\frac{2}{5}u^{5/2}-\frac{2}{9}u^{9/2}+C.
\end{aligned}
$$

Before applying the power rule, check that every variable factor is written in terms of $u$ and that the saved $\cos x\,dx$ has become $du$. No $x$-dependent factor should remain.

Substitute $u=\sin x$:

$$
\int(\sin x)^{3/2}\cos^3x\,dx
=
\frac{2}{5}(\sin x)^{5/2}
-\frac{2}{9}(\sin x)^{9/2}+C.
$$

```quiz
type: radio
id: whw5-p4-powers-1
content: |-
  Evaluate
  $$
  \int(\sin x)^{5/2}\cos^3x\,dx.
  $$
options:
- id: a
  content: |-
    $\dfrac{2}{7}(\sin x)^{7/2}-\dfrac{2}{11}(\sin x)^{11/2}+C$
  correct: true
- id: b
  content: |-
    $\dfrac{2}{7}(\sin x)^{7/2}+\dfrac{2}{11}(\sin x)^{11/2}+C$
- id: c
  content: |-
    $\dfrac{7}{2}(\sin x)^{7/2}-\dfrac{11}{2}(\sin x)^{11/2}+C$
- id: d
  content: |-
    $\dfrac{2}{5}(\sin x)^{5/2}-\dfrac{2}{9}(\sin x)^{9/2}+C$
- id: e
  content: |-
    $\dfrac{2}{7}(\cos x)^{7/2}-\dfrac{2}{11}(\cos x)^{11/2}+C$
```

---

<a id="original-integral"></a>
## Evaluate the Original Integral

**Example:** Evaluate

$$
\int\sqrt{\sin x}\,\cos^3x\,dx.
$$

**Explanation**

Save one cosine factor and rewrite $\cos^2x$:

$$
\begin{aligned}
\int\sqrt{\sin x}\,\cos^3x\,dx
&=\int(\sin x)^{1/2}\cos^2x\cos x\,dx \\
&=\int(\sin x)^{1/2}(1-\sin^2x)\cos x\,dx.
\end{aligned}
$$

Let $u=\sin x$, so $du=\cos x\,dx$:

$$
\begin{aligned}
\int(\sin x)^{1/2}(1-\sin^2x)\cos x\,dx
&=\int u^{1/2}(1-u^2)\,du \\
&=\int\left(u^{1/2}-u^{5/2}\right)\,du \\
&=\frac{2}{3}u^{3/2}-\frac{2}{7}u^{7/2}+C.
\end{aligned}
$$

Substitute back:

$$
\boxed{
\frac{2}{3}(\sin x)^{3/2}
-\frac{2}{7}(\sin x)^{7/2}+C
}.
$$

```quiz
type: radio
id: whw5-p4-original-1
content: |-
  Evaluate
  $$
  \int 3\sqrt{\sin x}\,\cos^3x\,dx.
  $$
options:
- id: a
  content: |-
    $2(\sin x)^{3/2}-\dfrac{6}{7}(\sin x)^{7/2}+C$
  correct: true
- id: b
  content: |-
    $\dfrac{2}{3}(\sin x)^{3/2}-\dfrac{2}{7}(\sin x)^{7/2}+C$
- id: c
  content: |-
    $2(\sin x)^{3/2}+\dfrac{6}{7}(\sin x)^{7/2}+C$
- id: d
  content: |-
    $\dfrac{9}{2}(\sin x)^{3/2}-\dfrac{21}{2}(\sin x)^{7/2}+C$
- id: e
  content: |-
    $2(\cos x)^{3/2}-\dfrac{6}{7}(\cos x)^{7/2}+C$
```

---

<a id="check"></a>
## Check by Differentiation

**Example:** Verify

$$
F(x)
=
\frac{2}{3}(\sin x)^{3/2}
-\frac{2}{7}(\sin x)^{7/2}.
$$

**Explanation**

Differentiate with the chain rule:

$$
\begin{aligned}
F'(x)
&=\frac{2}{3}\cdot\frac{3}{2}(\sin x)^{1/2}\cos x
-\frac{2}{7}\cdot\frac{7}{2}(\sin x)^{5/2}\cos x \\
&=(\sin x)^{1/2}\cos x-(\sin x)^{5/2}\cos x \\
&=(\sin x)^{1/2}(1-\sin^2x)\cos x \\
&=\sqrt{\sin x}\,\cos^3x.
\end{aligned}
$$

This derivative check, or the same check entered in a computer algebra system, restores the original integrand.

```quiz
type: radio
id: whw5-p4-check-1
content: |-
  What is the derivative of
  $$
  \frac{2}{5}(\sin x)^{5/2}-\frac{2}{9}(\sin x)^{9/2}?
  $$
options:
- id: a
  content: |-
    $(\sin x)^{3/2}\cos^3x$
  correct: true
- id: b
  content: |-
    $(\sin x)^{3/2}\cos x$
- id: c
  content: |-
    $(\sin x)^{3/2}\sin^3x$
- id: d
  content: |-
    $-(\sin x)^{3/2}\cos^3x$
- id: e
  content: |-
    $(\cos x)^{3/2}\sin^3x$
```

---

<a id="summary"></a>
## Summary

For an integrand with an odd cosine power and remaining factors built from sine:

1. Save one factor of $\cos x$.
2. Rewrite the remaining even cosine power using $\cos^2x=1-\sin^2x$.
3. Let $u=\sin x$, so $du=\cos x\,dx$.
4. Confirm that the transformed integral contains only $u$ and $du$.
5. Rewrite radicals as fractional powers and apply the power rule.
6. Substitute $u=\sin x$ back into the antiderivative.

For the original problem,

$$
\int\sqrt{\sin x}\,\cos^3x\,dx
=
\frac{2}{3}(\sin x)^{3/2}
-\frac{2}{7}(\sin x)^{7/2}+C.
$$

The main traps are using $1+\sin^2x$, failing to save one cosine factor, or subtracting exponents instead of adding $1$ in the power rule.
