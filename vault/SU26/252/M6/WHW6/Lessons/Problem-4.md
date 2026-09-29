# Decomposing a Rational Function with Two Linear Factors

## Table of Contents

- [Introduction](#introduction)
- [Choose One Fraction per Factor](#choose-one-fraction-per-factor)
- [Use Factor Zeros to Find the Coefficients](#use-factor-zeros-to-find-the-coefficients)
- [Keep Signs and Denominators Together](#keep-signs-and-denominators-together)
- [Verify by Recombining](#verify-by-recombining)
- [Summary](#summary)

## Prerequisites

- Add rational expressions using a common denominator.
- Evaluate a linear expression at a given value of $x$.
- Solve a one-step linear equation.

---

<a id="introduction"></a>
## Introduction

When a proper rational function has two distinct linear factors in its denominator, it can be split into one simpler fraction for each factor. The recognition cue is a denominator such as $(x-a)(x-b)$ together with a prompt asking for a sum or difference of simpler rational expressions.

This process reverses fraction addition: instead of combining two fractions over a common denominator, recover the two fractions from their combined form.

For constants $A$ and $B$, use the template

$$
\frac{P(x)}{(x-a)(x-b)}
=
\frac{A}{x-a}+\frac{B}{x-b}.
$$

Here $a\ne b$, and $A$ and $B$ are chosen so the two sides agree everywhere the original rational function is defined. The main procedure is: write the template, clear the denominators, substitute the zero of each factor to isolate one coefficient, and then recombine the result to check it.

---

<a id="choose-one-fraction-per-factor"></a>
## Choose One Fraction per Factor

**Example:** Set up the partial-fraction form of

$$
\frac{2x-1}{(x-4)(x+3)}.
$$

**Explanation**

The denominator has the distinct linear factors $x-4$ and $x+3$. Put one constant numerator over each factor:

$$
\frac{2x-1}{(x-4)(x+3)}
=
\frac{A}{x-4}+\frac{B}{x+3}.
$$

A linear denominator gets a constant numerator. No repeated-factor term or polynomial term is needed because the factors are distinct and the original rational function is proper.

Factoring identifies the denominators in the template. It does not permit canceling a denominator factor unless that same factor multiplies the entire numerator.

```quiz
type: radio
id: whw6-p4-template
content: |-
  Which is the standard partial-fraction template, with no redundant terms, for
  $$
  \frac{3x+7}{(x-5)(x+1)}\,?
  $$
options:
- id: whw6-p4-template-a
  content: |-
    $\dfrac{A}{x-5}+\dfrac{B}{x+1}$
  correct: true
  feedback: |-
    Each distinct linear factor receives one constant numerator. The factors are $x-5$ and $x+1$, so the minimal template is $A/(x-5)+B/(x+1)$.
- id: whw6-p4-template-b
  content: |-
    $\dfrac{Ax+B}{x-5}+\dfrac{C}{x+1}$
  feedback: |-
    A linear numerator is used over an irreducible quadratic factor, not over a linear factor. Here each denominator factor is linear, so each numerator should be a single constant.
- id: whw6-p4-template-c
  content: |-
    $\dfrac{A}{(x-5)^2}+\dfrac{B}{x+1}$
  feedback: |-
    The squared denominator term is required only when $x-5$ is repeated in the original denominator. It occurs once here, so the denominator should be $x-5$, not $(x-5)^2$.
- id: whw6-p4-template-d
  content: |-
    $\dfrac{A}{x-5}+\dfrac{B}{(x-5)(x+1)}$
  feedback: |-
    This keeps the full product in one term instead of separating the original factors. Partial fractions assign one term to $x-5$ and one term to $x+1$.
- id: whw6-p4-template-e
  content: |-
    $C+\dfrac{A}{x-5}+\dfrac{B}{x+1}$
  feedback: |-
    A polynomial term is needed only after dividing an improper rational function. Since the numerator has lower degree than the denominator, no extra constant term belongs in the standard form.
```

---

<a id="use-factor-zeros-to-find-the-coefficients"></a>
## Use Factor Zeros to Find the Coefficients

**Example:** Decompose

$$
\frac{7}{(x-2)(x+1)}.
$$

**Explanation**

Start with

$$
\frac{7}{(x-2)(x+1)}
=
\frac{A}{x-2}+\frac{B}{x+1}.
$$

Multiply by the common denominator $(x-2)(x+1)$:

$$
7=A(x+1)+B(x-2).
$$

Each coefficient is multiplied by the *other* factor: clearing $A/(x-2)$ leaves $A(x+1)$, while clearing $B/(x+1)$ leaves $B(x-2)$. This is a polynomial identity, so choose the zero of one factor at a time:

$$
\begin{aligned}
x=2:&\qquad 7=3A &&\Longrightarrow\quad A=\frac{7}{3},\\
x=-1:&\qquad 7=-3B &&\Longrightarrow\quad B=-\frac{7}{3}.
\end{aligned}
$$

Therefore,

$$
\frac{7}{(x-2)(x+1)}
=
\frac{7}{3(x-2)}-\frac{7}{3(x+1)}.
$$

Although $x=2$ and $x=-1$ are excluded from the original rational function, the cleared polynomials agree for every allowed $x$ and therefore are identical. The identity may be evaluated at those factor zeros.

```quiz
type: radio
id: whw6-p4-factor-zeros
content: |-
  Express
  $$
  \frac{8}{(x-1)(x+3)}
  $$
  as a sum or difference of two simpler rational expressions.
options:
- id: whw6-p4-factor-zeros-a
  content: |-
    $\dfrac{2}{x-1}-\dfrac{2}{x+3}$
  correct: true
  feedback: |-
    Clearing denominators gives $8=A(x+3)+B(x-1)$. At $x=1$, $A=2$; at $x=-3$, $B=-2$. Keeping each value with its original denominator gives $2/(x-1)-2/(x+3)$.
- id: whw6-p4-factor-zeros-b
  content: |-
    $-\dfrac{2}{x-1}+\dfrac{2}{x+3}$
  feedback: |-
    These signs are reversed. Substituting $x=1$ into $8=A(x+3)+B(x-1)$ gives $8=4A$, so the coefficient over $x-1$ must be $+2$, not $-2$.
- id: whw6-p4-factor-zeros-c
  content: |-
    $\dfrac{2}{x-1}+\dfrac{2}{x+3}$
  feedback: |-
    The second coefficient is not positive. At $x=-3$, the surviving factor is $x-1=-4$, so $8=-4B$ and $B=-2$.
- id: whw6-p4-factor-zeros-d
  content: |-
    $\dfrac{8}{x-1}-\dfrac{8}{x+3}$
  feedback: |-
    Clearing the denominators does not make the original numerator the value of both coefficients. Each coefficient is the numerator divided by the surviving factor; here the factor separation is $4$, giving magnitudes of $2$.
- id: whw6-p4-factor-zeros-e
  content: |-
    $\dfrac{2}{x-1}-\dfrac{8}{x+3}$
  feedback: |-
    The first coefficient is isolated correctly, but the same isolation is required for the second. At $x=-3$, $8=B(-4)$, so the coefficient over $x+3$ is $-2$, not $-8$.
```

---

<a id="keep-signs-and-denominators-together"></a>
## Keep Signs and Denominators Together

**Example:** Express the rational function from Problem 4 as two simpler fractions:

$$
\frac{1}{(x-3)(x-2)}.
$$

**Explanation**

Attach $A$ to $x-3$ and $B$ to $x-2$:

$$
\frac{1}{(x-3)(x-2)}
=
\frac{A}{x-3}+\frac{B}{x-2}.
$$

After clearing denominators,

$$
1=A(x-2)+B(x-3).
$$

Now use the factor zeros:

$$
\begin{aligned}
x=3:&\qquad 1=A(1) &&\Longrightarrow\quad A=1,\\
x=2:&\qquad 1=B(-1) &&\Longrightarrow\quad B=-1.
\end{aligned}
$$

Thus,

$$
\boxed{\frac{1}{(x-3)(x-2)}
=
\frac{1}{x-3}-\frac{1}{x-2}}.
$$

The negative sign comes from the surviving value $2-3=-1$. Record a coefficient as soon as it is found and keep it attached to the denominator used in the template.

```quiz
type: radio
id: whw6-p4-labels
content: |-
  Express
  $$
  \frac{x+5}{(x-1)(x+2)}
  $$
  as a sum or difference of two simpler rational expressions.
options:
- id: whw6-p4-labels-a
  content: |-
    $\dfrac{2}{x-1}-\dfrac{1}{x+2}$
  correct: true
  feedback: |-
    From $x+5=A(x+2)+B(x-1)$, substituting $x=1$ gives $A=2$, and substituting $x=-2$ gives $B=-1$. Those coefficients stay with $x-1$ and $x+2$, respectively.
- id: whw6-p4-labels-b
  content: |-
    $-\dfrac{1}{x-1}+\dfrac{2}{x+2}$
  feedback: |-
    This swaps the solved coefficients between the denominators. The value found by setting $x+2=0$ isolates $B$, which belongs over $x+2$; it does not move to the $x-1$ term.
- id: whw6-p4-labels-c
  content: |-
    $\dfrac{2}{x-1}+\dfrac{1}{x+2}$
  feedback: |-
    The sign of $B$ is lost. At $x=-2$, the identity gives $3=B(-3)$, so $B=-1$ and the second fraction must be subtracted.
- id: whw6-p4-labels-d
  content: |-
    $\dfrac{1}{x-1}+\dfrac{2}{x+2}$
  feedback: |-
    The numbers in the numerator are not themselves the partial-fraction coefficients. The coefficients come from the cleared identity; $x=1$ gives $A=2$, while $x=-2$ gives $B=-1$.
- id: whw6-p4-labels-e
  content: |-
    $\dfrac{2}{x-1}-\dfrac{1}{x-2}$
  feedback: |-
    The zero of $x+2$ is $-2$, but the denominator factor itself remains $x+2$. Replacing it with $x-2$ changes the poles and cannot reproduce the original denominator.
```

---

<a id="verify-by-recombining"></a>
## Verify by Recombining

**Example:** Check the decomposition from Problem 4.

**Explanation**

Add the two proposed fractions over their common denominator:

$$
\begin{aligned}
\frac{1}{x-3}-\frac{1}{x-2}
&=\frac{x-2}{(x-3)(x-2)}-\frac{x-3}{(x-3)(x-2)}\\
&=\frac{(x-2)-(x-3)}{(x-3)(x-2)}\\
&=\frac{1}{(x-3)(x-2)}.
\end{aligned}
$$

This check catches swapped coefficients and sign errors: the recombined numerator must simplify to the original numerator.

```quiz
type: radio
id: whw6-p4-recombine
content: |-
  Which decomposition of
  $$
  \frac{1}{(x+4)(x+1)}
  $$
  recombines to the original numerator $1$?
options:
- id: whw6-p4-recombine-a
  content: |-
    $-\dfrac{1}{3(x+4)}+\dfrac{1}{3(x+1)}$
  correct: true
  feedback: |-
    Recombining gives $[-(x+1)+(x+4)]/[3(x+4)(x+1)]=3/[3(x+4)(x+1)]$. The numerator reduces to $1$, so this is the required decomposition.
- id: whw6-p4-recombine-b
  content: |-
    $\dfrac{1}{3(x+4)}-\dfrac{1}{3(x+1)}$
  feedback: |-
    Recombining these terms gives $[(x+1)-(x+4)]/3=-1$ in the numerator. The signs produce the negative of the target rational function.
- id: whw6-p4-recombine-c
  content: |-
    $\dfrac{1}{3(x+4)}+\dfrac{1}{3(x+1)}$
  feedback: |-
    Adding with both coefficients positive produces the numerator $[(x+1)+(x+4)]/3=(2x+5)/3$, which is variable rather than the required constant $1$.
- id: whw6-p4-recombine-d
  content: |-
    $-\dfrac{1}{x+4}+\dfrac{1}{x+1}$
  feedback: |-
    The signs are oriented correctly, but the coefficients omit division by the distance between the factor zeros. Recombination produces numerator $3$, so both coefficients must be divided by $3$.
- id: whw6-p4-recombine-e
  content: |-
    $-\dfrac{1}{3(x+4)}+\dfrac{1}{3(x-1)}$
  feedback: |-
    A decomposition must preserve the original denominator factors. The zero of $x+1$ is $-1$, but the factor remains $x+1$; using $x-1$ creates a different rational function.
```

---

<a id="summary"></a>
## Summary

For a proper rational function with two distinct linear denominator factors:

1. Write one constant-over-linear fraction for each factor.
2. Multiply by the full denominator to create a polynomial identity.
3. Substitute each factor's zero so one coefficient remains.
4. Keep every coefficient, including its sign, attached to its template denominator.
5. Recombine the fractions; the numerator must simplify to the original numerator.

For Problem 4, the factor zeros give $A=1$ and $B=-1$, so

$$
\frac{1}{(x-3)(x-2)}
=
\frac{1}{x-3}-\frac{1}{x-2}.
$$
