# Center of Mass from a Linear Density

## Table of Contents

- [Introduction](#introduction)
- [Turn Density into a First Moment](#turn-density-into-a-first-moment)
- [Integrate a Power Density](#integrate-a-power-density)
- [Distinguish Mass from Moment](#distinguish-mass-from-moment)
- [Check the Location](#check-the-location)
- [Summary](#summary)

## Prerequisites

- Interpret a linear density $\lambda(x)$ as mass per unit length.
- Integrate a power: $\int x^n\,dx=\dfrac{x^{n+1}}{n+1}+C$ for $n\ne -1$.
- Use definite integrals on an interval $[a,b]$.

---

<a id="introduction"></a>
## Introduction

When a rod's density changes with position, its center of mass is not generally the midpoint. The cue is a position-dependent linear density $\lambda(x)$ together with a request for the center of mass. Think of the result as a mass-weighted average of position.

For a rod on $[a,b]$ with total mass $m$,

$$
x_{\mathrm{cm}}=\frac{1}{m}\int_a^b x\lambda(x)\,dx.
$$

The factor $x\lambda(x)$ forms the **first moment density**. Integrate it over the rod, then normalize by dividing by the total mass.

---

<a id="turn-density-into-a-first-moment"></a>
## Turn Density into a First Moment

Multiply the density by the position before integrating. Integrating $\lambda(x)$ alone gives mass, not center of mass.

**Example:** A rod lies on $0\le x\le L$, has total mass $M$, and has density $\lambda(x)=kx$. Find its center of mass in terms of the given quantities.

**Explanation**

The first moment about the origin is

$$
\int_0^L x\lambda(x)\,dx
=\int_0^L x(kx)\,dx
=k\int_0^L x^2\,dx
=\frac{kL^3}{3}.
$$

Divide by the total mass:

$$
x_{\mathrm{cm}}=\frac{kL^3}{3M}.
$$

```quiz
type: radio
id: p4-q1
content: |-
  A rod on $0\le x\le b$ has total mass $M$ and density $\lambda(x)=Ax^3$. Which integral correctly gives its $x$-coordinate of center of mass?
options:
- id: p4-q1-a
  content: |-
    $\displaystyle \frac{1}{M}\int_0^b Ax^3\,dx$
- id: p4-q1-b
  content: |-
    $\displaystyle \frac{1}{M}\int_0^b Ax^4\,dx$
  correct: true
- id: p4-q1-c
  content: |-
    $\displaystyle M\int_0^b Ax^4\,dx$
- id: p4-q1-d
  content: |-
    $\displaystyle \frac{1}{M}\int_0^b x\,dx$
- id: p4-q1-e
  content: |-
    $\displaystyle \frac{1}{M}\int_0^b Ax^2\,dx$
```

---

<a id="integrate-a-power-density"></a>
## Integrate a Power Density

If $\lambda(x)=cx^n$ on $[0,l]$, multiplying by $x$ raises the power by one:

$$
x\lambda(x)=cx^{n+1}.
$$

Therefore,

$$
x_{\mathrm{cm}}
=\frac{1}{m}\int_0^l cx^{n+1}\,dx
=\frac{c}{m}\left[\frac{x^{n+2}}{n+2}\right]_0^l
=\frac{cl^{n+2}}{(n+2)m}.
$$

**Example:** A thin rod of mass $m$ lies on $0\le x\le l$ and has $\lambda(x)=cx^2$. Find $x_{\mathrm{cm}}$.

**Explanation**

Here $n=2$, so the moment integrand is $cx^3$:

$$
x_{\mathrm{cm}}
=\frac{1}{m}\int_0^l cx^3\,dx
=\frac{c}{m}\left[\frac{x^4}{4}\right]_0^l
=\frac{c}{m}\left(\frac{l^4}{4}-\frac{0^4}{4}\right)
=\boxed{\frac{cl^4}{4m}}.
$$

The bracket means **upper value minus lower value**. The lower endpoint contributes zero here, but it is still part of the definite-integral calculation.

```quiz
type: radio
id: p4-q2
content: |-
  A rod of mass $M$ lies on $0\le x\le a$ and has $\lambda(x)=kx^4$. What is its $x$-coordinate of center of mass?
options:
- id: p4-q2-a
  content: |-
    $\displaystyle \frac{ka^5}{5M}$
- id: p4-q2-b
  content: |-
    $\displaystyle \frac{ka^6}{6M}$
  correct: true
- id: p4-q2-c
  content: |-
    $\displaystyle \frac{ka^4}{4M}$
- id: p4-q2-d
  content: |-
    $\displaystyle \frac{6M}{ka^6}$
- id: p4-q2-e
  content: |-
    $\displaystyle \frac{ka^6}{5M}$
```

---

<a id="distinguish-mass-from-moment"></a>
## Distinguish Mass from Moment

The two relevant integrals have different jobs:

$$
m=\int_a^b \lambda(x)\,dx,
\qquad
\text{first moment}=\int_a^b x\lambda(x)\,dx.
$$

If the total mass is already supplied as $m$, use it in the denominator. If it is not supplied, calculate it from the density.

**Example:** For the density $\lambda(x)=cx^2$ on $[0,l]$, suppose the mass is not separately given. Express the center of mass using only $l$.

**Explanation**

First calculate the mass:

$$
m=\int_0^l cx^2\,dx=\frac{cl^3}{3}.
$$

The first moment is $cl^4/4$, so

$$
x_{\mathrm{cm}}
=\frac{cl^4/4}{cl^3/3}
=\frac{3l}{4}.
$$

This agrees with $cl^4/(4m)$ after substituting $m=cl^3/3$.

```quiz
type: radio
id: p4-q3
content: |-
  A rod lies on $0\le x\le L$ with density $\lambda(x)=kx^3$, and its total mass is not otherwise given. Which ratio gives $x_{\mathrm{cm}}$?
options:
- id: p4-q3-a
  content: |-
    $\displaystyle \frac{\int_0^L kx^3\,dx}{\int_0^L kx^4\,dx}$
- id: p4-q3-b
  content: |-
    $\displaystyle \frac{\int_0^L kx^4\,dx}{\int_0^L kx^3\,dx}$
  correct: true
- id: p4-q3-c
  content: |-
    $\displaystyle \frac{1}{L}\int_0^L kx^3\,dx$
- id: p4-q3-d
  content: |-
    $\displaystyle \int_0^L x\,dx$
- id: p4-q3-e
  content: |-
    $\displaystyle \frac{1}{L}\int_0^L kx^4\,dx$
```

---

<a id="check-the-location"></a>
## Check the Location

A center of mass must lie within the rod. Its position should also shift toward the denser end. Units provide another quick check: if $\lambda$ has units of mass per length, then

$$
[x\lambda(x)\,dx]
=(\text{length})\left(\frac{\text{mass}}{\text{length}}\right)(\text{length})
=\text{mass}\cdot\text{length}.
$$

Dividing the first moment by mass leaves a length, as a coordinate should.

**Example:** A rod on $[0,l]$ has density $\lambda(x)=cx^2$ with $c>0$. Is $x_{\mathrm{cm}}=3l/4$ reasonable?

**Explanation**

Yes. The density increases as $x$ increases, so more mass lies near $x=l$. The value $3l/4$ is inside $[0,l]$ and lies to the right of the midpoint $l/2$.

```quiz
type: radio
id: p4-q4
content: |-
  A rod occupies $0\le x\le 10$ cm, and its density increases with $x$. Which proposed center of mass is the only reasonable one?
options:
- id: p4-q4-a
  content: |-
    $-2$ cm
- id: p4-q4-b
  content: |-
    $3$ cm
- id: p4-q4-c
  content: |-
    $7$ cm
  correct: true
- id: p4-q4-d
  content: |-
    $12$ cm
- id: p4-q4-e
  content: |-
    $5$ cm
```

---

<a id="summary"></a>
## Summary

When a rod has position-dependent density and the question asks for its center of mass:

1. Use the rod's actual bounds.
2. Form the first moment by multiplying density by position: $x\lambda(x)$.
3. Integrate the first moment and divide by total mass:

   $$
   x_{\mathrm{cm}}=\frac{1}{m}\int_a^b x\lambda(x)\,dx.
   $$

4. If mass is not supplied, calculate $m=\int_a^b\lambda(x)\,dx$.
5. Check that the answer has units of length, lies on the rod, and shifts toward the denser end.

The main trap is integrating $\lambda(x)$ alone in the numerator; that produces mass, not the first moment.
