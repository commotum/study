# Finding a Linear-Density Coefficient From Total Mass

<!--
lesson-id: 212-M2-006
topic-code: MTH212.M2.06
-->

## Table of Contents

- [Introduction](#introduction)
- [Turn Linear Density Into Total Mass](#turn-linear-density-into-total-mass)
- [Integrate and Isolate the Coefficient](#integrate-and-isolate-the-coefficient)
- [Substitute Values and Track Units](#substitute-values-and-track-units)
- [Apply the Method to the Rod](#apply-the-method-to-the-rod)
- [Summary](#summary)

## Prerequisites

- Interpret linear density as mass per unit length.
- Use the power rule for integration.
- Evaluate a definite integral from $0$ to the rod length.
- Solve a one-step equation for an unknown coefficient.

---

<a id="introduction"></a>
## Introduction

Linear density $\lambda(x)$ tells how much mass is packed into each unit of length near position $x$. The total mass of a rod occupying $0\le x\le L$ is

$$
M=\int_0^L\lambda(x)\,dx.
$$

When $\lambda(x)=cx$ and the total mass and length are known, integrate the density, set the result equal to the given mass, and solve for $c$. The main traps are treating the density as uniform, forgetting the factor from integrating $x$, or substituting numbers before isolating $c$.

The reusable sequence is:

| Stage | Action | Result for $\lambda(x)=cx$ |
|---|---|---|
| Build | Integrate density over the rod | $M=\int_0^Lcx\,dx$ |
| Evaluate | Apply the power rule and bounds | $M=cL^2/2$ |
| Solve | Isolate the coefficient | $c=2M/L^2$ |

---

<a id="turn-linear-density-into-total-mass"></a>
## Turn Linear Density Into Total Mass

**Example:** A rod occupies $0\le x\le L$ and has density $\lambda(x)=cx$. Write an equation relating its total mass $M$ to $c$ and $L$.

**Explanation**

A small segment of width $dx$ has mass

$$
dM=\lambda(x)\,dx.
$$

Add the masses of all such segments from the left end to the right end:

$$
M=\int_0^L dM
=\int_0^L\lambda(x)\,dx
=\int_0^L cx\,dx.
$$

The limits must cover the whole rod. Do not replace the varying density $cx$ by a single constant value.

```quiz
type: radio
id: problem-6-build-mass-integral-q1
content: |-
  A rod occupies $0\le x\le b$ and has linear density $\lambda(x)=kx^2$. Which equation correctly relates its total mass $M$ to the density?
options:
- id: a
  content: |-
    $M=\displaystyle\int_0^b kx^2\,dx$
  correct: true
  feedback: |-
    Total mass is the integral of the linear density over the full rod.
- id: b
  content: |-
    $M=\displaystyle\int_0^b kx\,dx$
  feedback: |-
    This changes the given density from $kx^2$ to $kx$.
- id: c
  content: |-
    $M=\displaystyle\int_0^b x(kx^2)\,dx$
  feedback: |-
    The extra factor of $x$ would compute a first moment, not total mass.
- id: d
  content: |-
    $M=kb^2$
  feedback: |-
    This evaluates the density at the endpoint instead of integrating it over the rod.
- id: e
  content: |-
    $M=\displaystyle\int_0^M kx^2\,dx$
  feedback: |-
    The integration bounds are positions, so the upper bound must be the rod length $b$.
```

---

<a id="integrate-and-isolate-the-coefficient"></a>
## Integrate and Isolate the Coefficient

**Example:** Starting from $M=\int_0^L cx\,dx$, solve symbolically for $c$.

**Explanation**

The power rule raises the exponent of $x$ from $1$ to $2$ and divides by the new exponent:

$$
\int cx\,dx=c\frac{x^2}{2}.
$$

Now evaluate the antiderivative as the upper endpoint minus the lower endpoint:

$$
\begin{aligned}
M
&=\int_0^L cx\,dx\\
&=c\left[\frac{x^2}{2}\right]_0^L\\
&=c\left(\frac{L^2}{2}-\frac{0^2}{2}\right)\\
&=\frac{cL^2}{2}.
\end{aligned}
$$

Now isolate $c$. Multiply by $2$ and divide by $L^2$:

$$
\boxed{c=\frac{2M}{L^2}}.
$$

Deriving this formula before inserting numbers keeps the factor $2$ and the square on $L$ visible.

```quiz
type: radio
id: problem-6-isolate-coefficient-q1
content: |-
  A rod on $0\le x\le L$ has density $\lambda(x)=kx^2$ and total mass $M$. Which expression gives $k$?
options:
- id: a
  content: |-
    $\dfrac{3M}{L^3}$
  correct: true
  feedback: |-
    $M=\int_0^Lkx^2\,dx=kL^3/3$, so $k=3M/L^3$.
- id: b
  content: |-
    $\dfrac{2M}{L^2}$
  feedback: |-
    This is the coefficient formula for density proportional to $x$, not $x^2$.
- id: c
  content: |-
    $\dfrac{M}{L^3}$
  feedback: |-
    This omits the factor $3$ produced when isolating $k$ from $kL^3/3$.
- id: d
  content: |-
    $\dfrac{L^3}{3M}$
  feedback: |-
    This inverts the correct relationship.
- id: e
  content: |-
    $\dfrac{3M}{L^2}$
  feedback: |-
    Integrating $x^2$ produces $L^3$, not $L^2$.
```

---

<a id="substitute-values-and-track-units"></a>
## Substitute Values and Track Units

**Example:** A rod with $\lambda(x)=cx$ has total mass $M=0.90\ \mathrm{kg}$ and length $L=1.5\ \mathrm{m}$. Find $c$.

**Explanation**

Insert both values into the symbolic formula:

$$
\begin{aligned}
c
&=\frac{2M}{L^2}\\
&=\frac{2(0.90\ \mathrm{kg})}{(1.5\ \mathrm{m})^2}\\
&=\frac{1.8\ \mathrm{kg}}{2.25\ \mathrm{m^2}}\\
&=0.80\ \mathrm{kg/m^2}.
\end{aligned}
$$

The square applies to both the number and the meter unit. These units are also required by $\lambda(x)=cx$: multiplying $\mathrm{kg/m^2}$ by $x$ in meters gives linear density in $\mathrm{kg/m}$.

Equivalently, substitute units into the solved formula:

$$
[c]
=\frac{[M]}{[L]^2}
=\frac{\mathrm{kg}}{\mathrm{m}^2}.
$$

There is also a symbolic reconstruction check. Substituting $c=2M/L^2$ back into the mass integral returns the given mass:

$$
\int_0^L\left(\frac{2M}{L^2}\right)x\,dx
=\frac{2M}{L^2}\cdot\frac{L^2}{2}
=M.
$$

```quiz
type: radio
id: problem-6-substitute-units-q1
content: |-
  A rod with $\lambda(x)=cx$ has total mass $M=0.72\ \mathrm{kg}$ and length $L=1.2\ \mathrm{m}$. What is $c$?
options:
- id: a
  content: |-
    $1.0\ \mathrm{kg/m^2}$
  correct: true
  feedback: |-
    $c=2(0.72\ \mathrm{kg})/(1.2\ \mathrm{m})^2=1.0\ \mathrm{kg/m^2}$.
- id: b
  content: |-
    $0.50\ \mathrm{kg/m^2}$
  feedback: |-
    This omits the factor $2$ in $c=2M/L^2$.
- id: c
  content: |-
    $0.60\ \mathrm{kg/m}$
  feedback: |-
    This uses the uniform-density calculation $M/L$ and has the wrong units for $c$.
- id: d
  content: |-
    $1.2\ \mathrm{kg/m^2}$
  feedback: |-
    This fails to square the rod length in the denominator.
- id: e
  content: |-
    $1.0\ \mathrm{kg/m}$
  feedback: |-
    The numerical value is right, but $c$ must have units $\mathrm{kg/m^2}$ so that $cx$ has units $\mathrm{kg/m}$.
```

---

<a id="apply-the-method-to-the-rod"></a>
## Apply the Method to the Rod

**Example:** A rod has mass $m=0.65\ \mathrm{kg}$, length $l=1.8\ \mathrm{m}$, and density $\lambda(x)=cx$. Find $c$.

**Explanation**

Integrating the density gives

$$
m=\int_0^l cx\,dx=\frac{cl^2}{2}.
$$

Solve first and then substitute:

$$
\begin{aligned}
c
&=\frac{2m}{l^2}\\
&=\frac{2(0.65\ \mathrm{kg})}{(1.8\ \mathrm{m})^2}\\
&=\frac{1.30}{3.24}\ \mathrm{kg/m^2}\\
&\approx0.40\ \mathrm{kg/m^2}.
\end{aligned}
$$

```quiz
type: radio
id: m2-1lec-q5
content: |-
  **Question 5**

  A rod of mass $m$ and length $l$ has linear mass density $\lambda(x)=cx$. Find $c$ when $m=0.65\ \mathrm{kg}$ and $l=1.8\ \mathrm{m}$. Enter your answer in $\mathrm{kg/m^2}$.

  ![](<../Source/Images/rod-with-linearly-increasing-density.png>)

  Enter $c$ in $\mathrm{kg/m^2}$ as a number only:
options:
- id: a
  content: |-
    $0.40$
  correct: true
  feedback: |-
    Integrate the density over the rod to obtain its total mass:

    $$
    m=\int_0^l\lambda(x)\,dx
    =\int_0^l cx\,dx
    =\frac{cl^2}{2}.
    $$

    Hence,

    $$
    c=\frac{2m}{l^2}
    =\frac{2(0.65\ \mathrm{kg})}{(1.8\ \mathrm{m})^2}
    \approx0.40\ \mathrm{kg/m^2}.
    $$
- id: b
  content: |-
    $0.20$
  feedback: |-
    This omits the factor $2$ that appears when solving $m=cl^2/2$ for $c$.
- id: c
  content: |-
    $0.36$
  feedback: |-
    This uses $m/l$, which would apply to a uniform density rather than $\lambda(x)=cx$.
- id: d
  content: |-
    $0.72$
  feedback: |-
    This uses $2m/l$ and fails to square the rod length.
- id: e
  content: |-
    $2.49$
  feedback: |-
    This inverts the relationship and computes $l^2/(2m)$.
```

---

<a id="summary"></a>
## Summary

When a rod's varying linear density contains an unknown coefficient:

1. Write total mass as $M=\int_0^L\lambda(x)\,dx$.
2. Integrate over the full rod.
3. Isolate the coefficient before substituting numbers.
4. Square the entire length, including its unit.
5. Check that the coefficient's units make $\lambda(x)$ a mass per length.

For $\lambda(x)=cx$,

$$
\boxed{c=\frac{2M}{L^2}},
\qquad
[c]=\mathrm{kg/m^2}.
$$

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
