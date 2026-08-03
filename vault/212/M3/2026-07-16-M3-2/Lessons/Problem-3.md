# Finding the Orbital Period of a Binary Star System

<!--
lesson-id: 212-M3-007
topic-code: MTH212.M3.07
-->

## Table of Contents

- [Introduction](#introduction)
- [Use the Total Mass](#use-the-total-mass)
- [Evaluate the Formula From the Inside Out](#evaluate-the-formula-from-the-inside-out)
- [Convert Seconds to Earth Years](#convert-seconds-to-earth-years)
- [Apply the Method to Problem 3](#apply-the-method-to-problem-3)

## Prerequisites

- Evaluating powers and square roots
- Scientific notation
- Converting between units of time
- Newton's gravitational constant: $G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$

---

<a id="introduction"></a>
## Introduction

For two stars in circular orbits about their common center of mass, the orbital period depends on their **full separation** $d$ and their **total mass** $m_1+m_2$:

$$
T=2\pi\sqrt{\frac{d^3}{G(m_1+m_2)}}.
$$

The recognition cue is a binary system whose two masses and separation are given and whose orbital period is requested. Add the masses, cube the separation, evaluate everything under the radical, multiply by $2\pi$, and then convert the resulting seconds to the requested time unit.

---

<a id="use-the-total-mass"></a>
## Use the Total Mass

**Example:** A binary system has masses $1.0\times10^{30}\ \mathrm{kg}$ and $3.0\times10^{30}\ \mathrm{kg}$ separated by $1.0\times10^{12}\ \mathrm m$. Write the correct numerical setup for its period.

**Explanation**

The gravitational motion involves both stars, so the denominator contains their sum:

$$
m_1+m_2
=1.0\times10^{30}+3.0\times10^{30}
=4.0\times10^{30}\ \mathrm{kg}.
$$

The distance $d$ is the full star-to-star separation. The setup is therefore

$$
T=2\pi\sqrt{
\frac{(1.0\times10^{12}\ \mathrm m)^3}
{(6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2})(4.0\times10^{30}\ \mathrm{kg})}
}.
$$

```quiz
type: radio
id: p3-total-mass-setup
content: |-
  A circular binary has masses $2.0\times10^{30}\ \mathrm{kg}$ and $6.0\times10^{30}\ \mathrm{kg}$ separated by $2.0\times10^{12}\ \mathrm m$. Which setup correctly gives its orbital period?
options:
- id: p3-setup-a
  content: |-
    $T=2\pi\sqrt{\dfrac{(2.0\times10^{12})^3}{G(8.0\times10^{30})}}$
  correct: true
  feedback: |-
    Add both masses to obtain $8.0\times10^{30}\ \mathrm{kg}$, and cube the full separation $d=2.0\times10^{12}\ \mathrm m$.
- id: p3-setup-b
  content: |-
    $T=2\pi\sqrt{\dfrac{(2.0\times10^{12})^3}{G(6.0\times10^{30})}}$
- id: p3-setup-c
  content: |-
    $T=2\pi\sqrt{\dfrac{2.0\times10^{12}}{G(8.0\times10^{30})}}$
- id: p3-setup-d
  content: |-
    $T=2\pi\sqrt{\dfrac{(2.0\times10^{12})^2}{G(8.0\times10^{30})}}$
- id: p3-setup-e
  content: |-
    $T=2\pi\sqrt{\dfrac{(8.0\times10^{30})^3}{G(2.0\times10^{12})}}$
```

---

<a id="evaluate-the-formula-from-the-inside-out"></a>
## Evaluate the Formula From the Inside Out

**Example:** Evaluate the period setup for $m_1=1.0\times10^{30}\ \mathrm{kg}$, $m_2=3.0\times10^{30}\ \mathrm{kg}$, and $d=1.0\times10^{12}\ \mathrm m$.

**Explanation**

Treat the radical as a set of parentheses. Evaluate its numerator and denominator before taking the square root:

1. Add the two masses.
2. Cube the full separation.
3. Multiply $G$ by the mass sum.
4. Divide inside the radical.
5. Take the square root.
6. Multiply by the outside factor $2\pi$.

$$
d^3=(1.0\times10^{12})^3=1.0\times10^{36}\ \mathrm{m^3},
$$

and

$$
G(m_1+m_2)
=(6.67\times10^{-11})(4.0\times10^{30})
=2.668\times10^{20}\ \mathrm{m^3/s^2}.
$$

The units verify that the radicand is a time squared:

$$
\left[\frac{d^3}{G(m_1+m_2)}\right]
=\frac{\mathrm{m^3}}{(\mathrm{N\,m^2/kg^2})(\mathrm{kg})}
=\frac{\mathrm{m^3}}{\mathrm{m^3/s^2}}
=\mathrm{s^2}.
$$

Therefore its square root has units of seconds. The factor $2\pi$ is unitless.

Now evaluate the quotient, the square root, and finally the outside factor $2\pi$:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{1.0\times10^{36}}{2.668\times10^{20}}}\\
&=2\pi\sqrt{3.7481\times10^{15}\ \mathrm{s^2}}\\
&=3.8467\times10^8\ \mathrm s.
\end{aligned}
$$

```quiz
type: radio
id: p3-evaluate-period
content: |-
  Use $G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$. What period in seconds results for $m_1=2.0\times10^{30}\ \mathrm{kg}$, $m_2=6.0\times10^{30}\ \mathrm{kg}$, and $d=2.0\times10^{12}\ \mathrm m$?
options:
- id: p3-evaluate-a
  content: |-
    $7.69\times10^8\ \mathrm s$
  correct: true
  feedback: |-
    The complete evaluation is $T=2\pi\sqrt{(2.0\times10^{12})^3/[G(8.0\times10^{30})]}=7.69\times10^8\ \mathrm s$. The outside factor $2\pi$ is applied after the square root.
- id: p3-evaluate-b
  content: |-
    $1.22\times10^8\ \mathrm s$
- id: p3-evaluate-c
  content: |-
    $9.42\times10^7\ \mathrm s$
- id: p3-evaluate-d
  content: |-
    $1.54\times10^9\ \mathrm s$
- id: p3-evaluate-e
  content: |-
    $2.44\times10^1\ \mathrm s$
```

---

<a id="convert-seconds-to-earth-years"></a>
## Convert Seconds to Earth Years

**Example:** Convert $3.8467\times10^8\ \mathrm s$ to Earth years.

**Explanation**

Using $1\ \mathrm{yr}=365.25\times24\times60\times60\ \mathrm s=3.15576\times10^7\ \mathrm s$, choose the conversion factor so seconds cancel:

$$
\begin{aligned}
T
&=(3.8467\times10^8\ \mathrm s)
\left(\frac{1\ \mathrm{yr}}{3.15576\times10^7\ \mathrm s}\right)\\
&=12.19\ \mathrm{yr}.
\end{aligned}
$$

Dividing by seconds per year converts the smaller unit, seconds, to the larger unit, years.

```quiz
type: radio
id: p3-convert-years
content: |-
  A binary-star calculation gives $T=7.6934\times10^8\ \mathrm s$. Using $1\ \mathrm{yr}=3.15576\times10^7\ \mathrm s$, what is the period in Earth years?
options:
- id: p3-convert-a
  content: |-
    $24.38\ \mathrm{yr}$
  correct: true
  feedback: |-
    Multiply by $1\ \mathrm{yr}/(3.15576\times10^7\ \mathrm s)$ so seconds cancel: $(7.6934\times10^8)/(3.15576\times10^7)=24.38\ \mathrm{yr}$.
- id: p3-convert-b
  content: |-
    $2.43\times10^{16}\ \mathrm{yr}$
- id: p3-convert-c
  content: |-
    $0.0410\ \mathrm{yr}$
- id: p3-convert-d
  content: |-
    $7.6934\times10^8\ \mathrm{yr}$
- id: p3-convert-e
  content: |-
    $2.11\times10^6\ \mathrm{yr}$
```

---

<a id="apply-the-method-to-problem-3"></a>
## Apply the Method to Problem 3

**Example:** The same binary star system has masses $2.5\times10^{30}\ \mathrm{kg}$ and $5.0\times10^{30}\ \mathrm{kg}$ separated by $3.0\times10^{12}\ \mathrm{m}$. Find its orbital period.

**Explanation**

First add the two masses:

$$
m_1+m_2=7.5\times10^{30}\ \mathrm{kg}.
$$

For a circular binary system with separation $d$,

$$
T=2\pi\sqrt{\frac{d^3}{G(m_1+m_2)}}.
$$

Using $G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$ gives

$$
T=1.4597\times10^9\ \mathrm{s}
=46.2556\ldots\ \mathrm{yr}.
$$

The measured masses and separation have two significant figures, so $T=46\ \mathrm{yr}$. The requested answer is a number only: **46**.

The answer choices diagnose common mistakes:

- $1.5\times10^9$ is the period in seconds, not the requested Earth years.
- $57$ results from using only the larger star's mass instead of $m_1+m_2$.
- $80$ results from using only the smaller star's mass.
- $7.4$ omits the outside factor $2\pi$.

```quiz
type: radio
id: p3-source-check
content: |-
  **Question 2**

  The same binary star system has masses $2.5\times10^{30}\ \mathrm{kg}$ and $5.0\times10^{30}\ \mathrm{kg}$ separated by $3.0\times10^{12}\ \mathrm{m}$. Find its orbital period.

  Enter the period in Earth years as a number only:
options:
- id: p3-source-a
  content: |-
    $46$
  correct: true
  feedback: |-
    For a circular binary system with separation $d$,

    $$
    T=2\pi\sqrt{\frac{d^3}{G(m_1+m_2)}}.
    $$

    Using $G=6.67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$ gives

    $$
    T=1.4597\times10^9\ \mathrm{s}
    =46.2556\ldots\ \mathrm{yr}.
    $$

    The measured masses and separation have two significant figures, so $T=46\ \mathrm{yr}$.
- id: p3-source-b
  content: |-
    $1.5\times10^9$
- id: p3-source-c
  content: |-
    $57$
- id: p3-source-d
  content: |-
    $80$
- id: p3-source-e
  content: |-
    $7.4$
```

---

## Summary

- Cue: a circular binary's two masses and full separation are given, and its period is requested.
- Add the masses and use $T=2\pi\sqrt{d^3/[G(m_1+m_2)]}$.
- Evaluate in the order: mass sum, cube, products and quotient under the radical, square root, then $2\pi$.
- Use units to check that the radicand is in $\mathrm{s^2}$ and the period is in seconds.
- Convert seconds to Earth years with a factor whose seconds cancel, and round only at the end.
- Main traps: using only one mass, failing to cube $d$, omitting $2\pi$, or reporting the answer in seconds.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 2 Study Guide](../../2026-07-20-Q-2/Study-Guide.md)
Next: [Scaling Kinetic Energy in a Circular Orbit](../../2026-07-17-HW-5/Lessons/Problem-6.md)

Study guide index: 17/20

---

<!-- lesson-nav:end -->
