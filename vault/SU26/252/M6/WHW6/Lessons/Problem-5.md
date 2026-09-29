# Integrating Rational Functions with Two-Term Partial Fractions

## Table of Contents

- [Introduction](#introduction)
- [Factor the Denominator and Write the Template](#factor-the-denominator-and-write-the-template)
- [Use Factor Roots to Find the Constants](#use-factor-roots-to-find-the-constants)
- [Integrate the Reciprocal Terms](#integrate-the-reciprocal-terms)
- [Apply the Full Method](#apply-the-full-method)
- [Summary](#summary)

## Prerequisites

- Factor a monic quadratic into two linear factors.
- Substitute values into a polynomial identity.
- Use the sum and constant-multiple rules for indefinite integrals.
- Recall that $\displaystyle \int \frac{1}{x-r}\,dx=\ln|x-r|+C$.

---

<a id="introduction"></a>
## Introduction

When a proper rational function has a quadratic denominator that factors into two distinct linear factors, partial fractions can turn one difficult-looking fraction into two reciprocal linear terms.

Use this method when all three cues are present:

- the numerator has lower degree than the denominator;
- the denominator factors into two distinct linear factors;
- the goal is to integrate the rational function.

If the numerator's degree is at least the denominator's degree, polynomial division must come first. That case is outside this lesson.

For a denominator $(x-r_1)(x-r_2)$, write

$$
\frac{P(x)}{(x-r_1)(x-r_2)}
=
\frac{A}{x-r_1}+\frac{B}{x-r_2}.
$$

Then clear the denominators, choose the two factor roots to find $A$ and $B$, and integrate the two simpler terms. The main traps are pairing a constant with the wrong factor, losing a sign when substituting a root, and omitting absolute values or $C$ from the antiderivative.

---

<a id="factor-the-denominator-and-write-the-template"></a>
## Factor the Denominator and Write the Template

**Example:** Set up the partial-fraction form for

$$
\frac{2x+7}{x^2-x-6}.
$$

**Explanation**

Factor the denominator:

$$
x^2-x-6=(x-3)(x+2).
$$

Each distinct linear factor gets one constant numerator, so the correct template is

$$
\frac{2x+7}{(x-3)(x+2)}
=
\frac{A}{x-3}+\frac{B}{x+2}.
$$

The denominator under each constant is one of the original linear factors.

```quiz
type: radio
id: p5-factor-template
content: |-
  Which partial-fraction template is correct for
  $$
  \frac{4x+1}{x^2+x-12}?
  $$
options:
- id: p5-factor-a
  content: |-
    $\displaystyle \frac{A}{x+4}+\frac{B}{x-3}$
  correct: true
  feedback: |-
    A quadratic with two distinct linear factors gets one constant over each factor. Since $x^2+x-12=(x+4)(x-3)$, the required template is $A/(x+4)+B/(x-3)$.
- id: p5-factor-b
  content: |-
    $\displaystyle \frac{A}{x-4}+\frac{B}{x+3}$
  feedback: |-
    This reverses both signs in the factors. The numbers must multiply to $-12$ and add to $1$, so the denominator factors are $(x+4)(x-3)$, not $(x-4)(x+3)$.
- id: p5-factor-c
  content: |-
    $\displaystyle \frac{Ax+B}{x+4}+\frac{C}{x-3}$
  feedback: |-
    A linear numerator is reserved for an irreducible quadratic factor. Here both denominator factors are linear, so each partial fraction needs only a constant numerator.
- id: p5-factor-d
  content: |-
    $\displaystyle \frac{A}{(x+4)^2}+\frac{B}{x-3}$
  feedback: |-
    The squared denominator would represent a repeated factor, but $(x+4)$ occurs only once in the factorization. Use $A/(x+4)$ rather than $A/(x+4)^2$.
- id: p5-factor-e
  content: |-
    $\displaystyle \frac{Ax+B}{(x+4)(x-3)}$
  feedback: |-
    This keeps the original combined denominator and therefore does not decompose the rational function. Partial fractions must separate the two linear factors into two terms.
```

---

<a id="use-factor-roots-to-find-the-constants"></a>
## Use Factor Roots to Find the Constants

**Example:** Decompose

$$
\frac{5x-1}{(x+1)(x-2)}.
$$

**Explanation**

Start with

$$
\frac{5x-1}{(x+1)(x-2)}
=
\frac{A}{x+1}+\frac{B}{x-2}.
$$

Multiplying by $(x+1)(x-2)$ gives the identity

$$
5x-1=A(x-2)+B(x+1).
$$

After the denominators are cleared, this is a polynomial identity, so it holds at the factor roots as well. That lets us choose values strategically. At $x=-1$, the $B$ term vanishes:

$$
-6=A(-3),
\qquad A=2.
$$

At $x=2$, the $A$ term vanishes:

$$
9=B(3),
\qquad B=3.
$$

Therefore,

$$
\frac{5x-1}{(x+1)(x-2)}
=
\frac{2}{x+1}+\frac{3}{x-2}.
$$

```quiz
type: radio
id: p5-find-constants
content: |-
  Which decomposition is correct?
  $$
  \frac{5x+4}{(x-1)(x+2)}
  $$
options:
- id: p5-constants-a
  content: |-
    $\displaystyle \frac{3}{x-1}+\frac{2}{x+2}$
  correct: true
  feedback: |-
    Clearing denominators gives $5x+4=A(x+2)+B(x-1)$. Substituting $x=1$ gives $9=3A$, so $A=3$, and substituting $x=-2$ gives $-6=-3B$, so $B=2$.
- id: p5-constants-b
  content: |-
    $\displaystyle \frac{2}{x-1}+\frac{3}{x+2}$
  feedback: |-
    This swaps the constants between the factors. In $A(x+2)+B(x-1)$, the root $x=1$ isolates the constant over $x-1$, giving $A=3$, not $2$.
- id: p5-constants-c
  content: |-
    $\displaystyle -\frac{3}{x-1}+\frac{2}{x+2}$
  feedback: |-
    The sign of the first constant is incorrect. At $x=1$, both the numerator $5(1)+4=9$ and the surviving multiplier $1+2=3$ are positive, so $A=9/3=3$.
- id: p5-constants-d
  content: |-
    $\displaystyle \frac{3}{x-1}-\frac{2}{x+2}$
  feedback: |-
    The sign of the second constant is incorrect. At $x=-2$, the equation is $-6=B(-3)$, and dividing two negative values gives $B=2$.
- id: p5-constants-e
  content: |-
    $\displaystyle \frac{5}{x-1}+\frac{4}{x+2}$
  feedback: |-
    The coefficients $5$ and $4$ from the original numerator are not automatically the partial-fraction constants. The constants must satisfy the cleared identity, which gives $A=3$ and $B=2$.
```

---

<a id="integrate-the-reciprocal-terms"></a>
## Integrate the Reciprocal Terms

**Example:** Evaluate

$$
\int\left(\frac{3}{x+1}-\frac{2}{x-4}\right)\,dx.
$$

**Explanation**

Integrate term by term and keep each constant multiplier:

$$
\begin{aligned}
\int\left(\frac{3}{x+1}-\frac{2}{x-4}\right)\,dx
&=3\int\frac{1}{x+1}\,dx-2\int\frac{1}{x-4}\,dx\\
&=3\ln|x+1|-2\ln|x-4|+C.
\end{aligned}
$$

More generally,

$$
\int \frac{c}{ax+b}\,dx=\frac{c}{a}\ln|ax+b|+C,
$$

because the derivative of the denominator is $a$. Every factor in the assigned problem is monic, so $a=1$. The absolute values are part of the reciprocal antiderivative, and one arbitrary constant is added after integrating the sum.

```quiz
type: radio
id: p5-integrate-terms
content: |-
  Evaluate
  $$
  \int\left(\frac{2}{x+5}+\frac{1}{x-3}\right)\,dx.
  $$
options:
- id: p5-integrate-a
  content: |-
    $\displaystyle 2\ln|x+5|+\ln|x-3|+C$
  correct: true
  feedback: |-
    Each reciprocal linear term integrates to a logarithm while its numerator stays as a multiplier. Thus $2/(x+5)$ gives $2\ln|x+5|$, $1/(x-3)$ gives $\ln|x-3|$, and an arbitrary constant is required.
- id: p5-integrate-b
  content: |-
    $\displaystyle 2\ln|x+5|-\ln|x-3|+C$
  feedback: |-
    A denominator of $x-3$ does not create a negative coefficient because its derivative is $1$. The original second term is positive, so its antiderivative is $+\ln|x-3|$.
- id: p5-integrate-c
  content: |-
    $\displaystyle \frac{1}{2}\ln|x+5|+\ln|x-3|+C$
  feedback: |-
    The constant-multiple rule keeps the numerator coefficient $2$; it does not invert it. Only a nonunit coefficient multiplying $x$ inside the denominator would introduce a reciprocal chain-rule factor.
- id: p5-integrate-d
  content: |-
    $\displaystyle 2\ln(x+5)+\ln(x-3)+C$
  feedback: |-
    Without absolute values, these logarithms are undefined on intervals where a linear factor is negative. The reciprocal rule is $\int 1/(x-r)\,dx=\ln|x-r|+C$ on every interval avoiding the pole.
- id: p5-integrate-e
  content: |-
    $\displaystyle 2\ln|x+5|+\ln|x-3|$
  feedback: |-
    The logarithmic terms differentiate correctly, but an indefinite integral represents an entire family of antiderivatives. The missing $+C$ omits that arbitrary constant.
```

---

<a id="apply-the-full-method"></a>
## Apply the Full Method

**Example:** Evaluate the assigned integral

$$
\int \frac{3x}{x^2+2x-8}\,dx.
$$

**Explanation**

Factor the denominator:

$$
x^2+2x-8=(x+4)(x-2).
$$

Set up the decomposition and clear the denominators:

$$
\frac{3x}{(x+4)(x-2)}
=
\frac{A}{x+4}+\frac{B}{x-2}
$$

$$
3x=A(x-2)+B(x+4).
$$

At $x=-4$,

$$
-12=-6A,
\qquad A=2.
$$

At $x=2$,

$$
6=6B,
\qquad B=1.
$$

Therefore,

$$
\frac{3x}{x^2+2x-8}
=
\frac{2}{x+4}+\frac{1}{x-2},
$$

so

$$
\boxed{\int \frac{3x}{x^2+2x-8}\,dx
=2\ln|x+4|+\ln|x-2|+C.}
$$

Differentiate to check the entire chain:

$$
\begin{aligned}
\frac{d}{dx}\left(2\ln|x+4|+\ln|x-2|+C\right)
&=\frac{2}{x+4}+\frac{1}{x-2}\\
&=\frac{2(x-2)+(x+4)}{(x+4)(x-2)}\\
&=\frac{3x}{x^2+2x-8}.
\end{aligned}
$$

The derivative reproduces the original integrand, including its numerator and denominator.

This antiderivative formula is valid on any interval that does not cross either pole, $x=-4$ or $x=2$.

```quiz
type: radio
id: p5-full-method
content: |-
  Evaluate
  $$
  \int\frac{5x+10}{x^2+x-6}\,dx.
  $$
options:
- id: p5-full-a
  content: |-
    $\displaystyle \ln|x+3|+4\ln|x-2|+C$
  correct: true
  feedback: |-
    Since $x^2+x-6=(x+3)(x-2)$, clearing $A/(x+3)+B/(x-2)$ gives $5x+10=A(x-2)+B(x+3)$. The roots give $A=1$ and $B=4$, so termwise integration yields $\ln|x+3|+4\ln|x-2|+C$.
- id: p5-full-b
  content: |-
    $\displaystyle 4\ln|x+3|+\ln|x-2|+C$
  feedback: |-
    This swaps the constants between the two factors. Substituting $x=-3$ isolates the constant over $x+3$ and gives $A=1$; substituting $x=2$ isolates the constant over $x-2$ and gives $B=4$.
- id: p5-full-c
  content: |-
    $\displaystyle -\ln|x+3|+4\ln|x-2|+C$
  feedback: |-
    The first coefficient should be positive. At $x=-3$, the cleared identity gives $-5=A(-5)$, so $A=1$; the two negative values cancel rather than produce $-1$.
- id: p5-full-d
  content: |-
    $\displaystyle \frac{5}{2}\ln|x^2+x-6|+C$
  feedback: |-
    A single logarithm of the denominator would require the numerator to be a constant multiple of its derivative $2x+1$. The numerator $5x+10$ is not such a multiple, so partial fractions are needed.
- id: p5-full-e
  content: |-
    $\displaystyle \ln|x+3|+4\ln|x-2|$
  feedback: |-
    The decomposition and logarithmic coefficients are correct, but the result lacks $+C$. An indefinite integral must include an arbitrary constant because all vertical shifts have the same derivative.
```

---

<a id="summary"></a>
## Summary

**Recognition cue:** the integrand is proper and its denominator splits into two distinct linear factors.

**Procedure:**

1. Factor the denominator.
2. Put one constant numerator over each linear factor.
3. Clear denominators to form a polynomial identity.
4. Substitute each factor root to isolate one constant at a time.
5. Integrate each reciprocal term as a logarithm with absolute values.
6. Include one arbitrary constant $C$.

**Main trap:** the coefficient over one factor is found by substituting the root of that same factor. After denominators are cleared, that coefficient survives while every other term contains the zero factor. Keep the factor-constant pairing visible.

**Check:** either recombine the partial fractions or differentiate the final antiderivative. The result must reproduce the original integrand exactly.
