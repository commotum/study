# Eliminating a Density Constant in a Rod-Inertia Integral

## Table of Contents

- [Introduction](#introduction)
- [Use Total Mass to Find the Density Constant](#use-total-mass-to-find-the-density-constant)
- [Build the Moment-of-Inertia Integral](#build-the-moment-of-inertia-integral)
- [Eliminate the Constant Before Substituting](#eliminate-the-constant-before-substituting)
- [Apply the Method to the Nonuniform Rod](#apply-the-method-to-the-nonuniform-rod)
- [Summary](#summary)

## Prerequisites

- Evaluate definite integrals with the power rule.
- Use $dm=\lambda(x)\,dx$ for a linear mass density.
- Use $I=\int x^2\,dm$ for moment of inertia about the origin.

---

<a id="introduction"></a>
## Introduction

A density such as $\lambda(x)=cx$ contains an unknown constant $c$. If the rod's total mass is known, the mass integral determines that constant:

$$
m=\int_0^l\lambda(x)\,dx.
$$

The same density then appears in the moment-of-inertia integral:

$$
I=\int_0^l x^2\lambda(x)\,dx.
$$

Keep the two jobs separate:

| Goal | Integral | Meaning |
|---|---|---|
| Normalize the density | $m=\int_0^l\lambda(x)\,dx$ | Add the mass elements |
| Find rotational inertia | $I=\int_0^l x^2\lambda(x)\,dx$ | Weight each mass element by $x^2$ |

**Recognition cue:** When a nonuniform density contains an unknown constant but total mass is given, normalize the density with the mass integral before evaluating the requested weighted integral.

---

<a id="use-total-mass-to-find-the-density-constant"></a>
## Use Total Mass to Find the Density Constant

**Example:** A rod occupies $0\le x\le2.0\ \mathrm{m}$ and has density $\lambda(x)=cx$. Its total mass is $6.0\ \mathrm{kg}$. Find $c$.

**Explanation**

Integrate the density over the whole rod:

$$
\begin{aligned}
m
&=\int_0^l cx\,dx\\
&=c\int_0^l x\,dx\\
&=c\left[\frac{x^2}{2}\right]_0^l\\
&=\frac{cl^2}{2}.
\end{aligned}
$$

Therefore,

$$
c=\frac{2m}{l^2}
=\frac{2(6.0)}{(2.0)^2}
=3.0\ \mathrm{kg/m^2}.
$$

The units confirm the normalization: because $\lambda=cx$ has units $\mathrm{kg/m}$, the constant $c$ must have units $\mathrm{kg/m^2}$.

```quiz
type: radio
id: p3-density-constant
content: |-
  A rod occupies $0\le x\le4.0\ \mathrm{m}$ and has $\lambda(x)=cx$. Its total mass is $8.0\ \mathrm{kg}$. What is $c$?
options:
- id: p3-density-constant-a
  content: |-
    $0.50\ \mathrm{kg/m^2}$
- id: p3-density-constant-b
  content: |-
    $1.0\ \mathrm{kg/m^2}$
  correct: true
- id: p3-density-constant-c
  content: |-
    $2.0\ \mathrm{kg/m^2}$
- id: p3-density-constant-d
  content: |-
    $4.0\ \mathrm{kg/m^2}$
```

---

<a id="build-the-moment-of-inertia-integral"></a>
## Build the Moment-of-Inertia Integral

**Example:** A rod on $0\le x\le l$ has $\lambda(x)=cx$. Write and evaluate its moment-of-inertia integral about the origin in terms of $c$ and $l$.

**Explanation**

A small mass element is $dm=\lambda(x)\,dx=cx\,dx$. Its contribution to rotational inertia is $x^2dm$, so

$$
x^2\lambda(x)=x^2(cx)=cx^3.
$$

For both integrals, the needed definite-integral pattern is

$$
\int_0^l x^n\,dx
=\left[\frac{x^{n+1}}{n+1}\right]_0^l
=\frac{l^{n+1}}{n+1}.
$$

Apply it with $n=3$:

$$
\begin{aligned}
I
&=\int_0^l x^2\,dm\\
&=\int_0^l x^2(cx)\,dx\\
&=c\int_0^l x^3\,dx\\
&=c\left[\frac{x^4}{4}\right]_0^l\\
&=\frac{cl^4}{4}.
\end{aligned}
$$

The extra factor $x^2$ is essential: the mass integral totals mass, while the inertia integral weights each mass element by its squared distance from the axis.

```quiz
type: radio
id: p3-inertia-integrand
content: |-
  A rod lies on $0\le x\le l$ with $\lambda(x)=kx$. Which integral gives its moment of inertia about the origin?
options:
- id: p3-inertia-integrand-a
  content: |-
    $\displaystyle\int_0^l kx\,dx$
- id: p3-inertia-integrand-b
  content: |-
    $\displaystyle\int_0^l kx^2\,dx$
- id: p3-inertia-integrand-c
  content: |-
    $\displaystyle\int_0^l kx^3\,dx$
  correct: true
- id: p3-inertia-integrand-d
  content: |-
    $\displaystyle\int_0^l kx^4\,dx$
```

---

<a id="eliminate-the-constant-before-substituting"></a>
## Eliminate the Constant Before Substituting

**Example:** Express the moment of inertia of a rod with $\lambda(x)=cx$ in terms of only its total mass $m$ and length $l$.

**Explanation**

The mass integral gave

$$
c=\frac{2m}{l^2},
$$

and the inertia integral gave

$$
I=\frac{cl^4}{4}.
$$

Substitute the first result into the second:

$$
I
=\frac14\left(\frac{2m}{l^2}\right)l^4
=\frac12ml^2.
$$

The units reduce correctly:

$$
[I]=[m][l^2]=\mathrm{kg\,m^2}.
$$

This simplified formula is valid for a rod that begins at the origin and has the specific density $\lambda(x)=cx$.

```quiz
type: radio
id: p3-eliminate-c
content: |-
  A rod has mass $0.80\ \mathrm{kg}$, length $1.5\ \mathrm{m}$, and density $\lambda(x)=cx$ on $0\le x\le l$. What is its moment of inertia about the origin?
options:
- id: p3-eliminate-c-a
  content: |-
    $0.30\ \mathrm{kg\,m^2}$
- id: p3-eliminate-c-b
  content: |-
    $0.60\ \mathrm{kg\,m^2}$
- id: p3-eliminate-c-c
  content: |-
    $0.90\ \mathrm{kg\,m^2}$
  correct: true
- id: p3-eliminate-c-d
  content: |-
    $1.8\ \mathrm{kg\,m^2}$
```

---

<a id="apply-the-method-to-the-nonuniform-rod"></a>
## Apply the Method to the Nonuniform Rod

**Source problem**

The same rod has mass $m=0.65\ \mathrm{kg}$, length $l=1.8\ \mathrm{m}$, and density $\lambda(x)=cx$. Find its moment of inertia about the origin.

![](<../Source/Images/rod-with-linearly-increasing-density.png>)

Enter the moment of inertia in kilogram square meters as a number only.

**Explanation**

First use the total mass to eliminate $c$:

$$
m=\int_0^l cx\,dx=\frac{cl^2}{2},
\qquad
c=\frac{2m}{l^2}.
$$

Then

$$
\begin{aligned}
I
&=\int_0^l x^2\lambda(x)\,dx\\
&=\int_0^l cx^3\,dx\\
&=\frac{cl^4}{4}\\
&=\frac12ml^2.
\end{aligned}
$$

Substitution gives

$$
I
=\frac12(0.65\ \mathrm{kg})(1.8\ \mathrm{m})^2
=1.053\ \mathrm{kg\,m^2}.
$$

The coefficient also passes a magnitude check. Since the density increases toward the far end, this rod has more inertia than a uniform rod about its end, $\tfrac13ml^2$, but less than the limiting value $ml^2$ obtained if all mass were at $x=l$:

$$
\frac13ml^2<\frac12ml^2<ml^2.
$$

The measured givens have two significant figures, so the number-only answer is

$$
\boxed{1.1}.
$$

```quiz
type: radio
id: p3-source-check
content: |-
  Which number should be entered for the source problem?
options:
- id: p3-source-check-a
  content: |-
    $0.35$
- id: p3-source-check-b
  content: |-
    $0.59$
- id: p3-source-check-c
  content: |-
    $1.1$
  correct: true
- id: p3-source-check-d
  content: |-
    $2.1$
```

---

<a id="summary"></a>
## Summary

For a rod on $0\le x\le l$ with $\lambda(x)=cx$:

1. Normalize the density: $m=\int_0^l cx\,dx$, so $c=2m/l^2$.
2. Weight the density by squared distance: $I=\int_0^l x^2(cx)\,dx$.
3. Eliminate $c$ to obtain $I=\tfrac12ml^2$.
4. Substitute the measured values and round only at the end.

The main trap is using the mass integral again for inertia and forgetting the distance-squared factor $x^2$. Check that the final units are $\mathrm{kg\,m^2}$ and that $\tfrac13ml^2<I<ml^2$ for this linearly increasing density.
