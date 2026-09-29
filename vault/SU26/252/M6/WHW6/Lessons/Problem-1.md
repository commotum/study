# Integrating $1/\sqrt{1+k^2x^2}$ by Trigonometric Substitution

## Table of Contents

- [Introduction](#introduction)
- [Match the Sum-of-Squares Pattern](#match-the-sum-of-squares-pattern)
- [Transform the Entire Integral](#transform-the-entire-integral)
- [Return the Antiderivative to $x$](#return-the-antiderivative-to-x)
- [Do Not Drop the Square Root](#do-not-drop-the-square-root)
- [Summary](#summary)

## Prerequisites

- Recognize the identity $1+\tan^2\theta=\sec^2\theta$.
- Use $\frac{d}{d\theta}(\tan\theta)=\sec^2\theta$ and $\int\sec\theta\,d\theta=\ln|\sec\theta+\tan\theta|+C$.
- Use a substitution to rewrite both an expression and its differential.

---

<a id="introduction"></a>
## Introduction

When a denominator contains a radical of the form

$$
\sqrt{1+(kx)^2},
$$

the sum $1+(kx)^2$ is the cue for a tangent substitution. Set $kx=\tan\theta$ so the identity

$$
1+\tan^2\theta=\sec^2\theta
$$

turns the radical into a single trigonometric factor. Then rewrite $dx$, integrate in $\theta$, and convert every trigonometric quantity back to $x$.

---

<a id="match-the-sum-of-squares-pattern"></a>
## Match the Sum-of-Squares Pattern

**Example:** Choose a trigonometric substitution for

$$
\int\frac{dx}{\sqrt{1+4x^2}}.
$$

**Explanation**

First expose the squared linear quantity:

$$
1+4x^2=1+(2x)^2.
$$

The identity $1+\tan^2\theta=\sec^2\theta$ matches this pattern exactly, so choose

$$
2x=\tan\theta.
$$

The coefficient belongs inside the substitution. Choosing only $x=\tan\theta$ would leave $1+4\tan^2\theta$, which is not a Pythagorean identity.

```quiz
type: radio
id: whw6-p1-recognize
content: |-
  Which substitution is designed to simplify $\sqrt{1+16x^2}$ by the identity $1+\tan^2\theta=\sec^2\theta$?
options:
- id: recognize-tan
  content: |-
    $4x=\tan\theta$
  correct: true
  feedback: |-
    The radicand is $1+(4x)^2$. Matching $4x$ with $\tan\theta$ changes it to $1+\tan^2\theta=\sec^2\theta$, so the radical simplifies to $\sec\theta$ on the standard substitution interval.
- id: recognize-wrong-scale
  content: |-
    $16x=\tan\theta$
  feedback: |-
    The squared quantity in the radicand is $4x$, not $16x$, because $16x^2=(4x)^2$. This choice would turn the radicand into $1+\tan^2\theta/16$, so it would not produce the needed identity.
- id: recognize-sine
  content: |-
    $4x=\sin\theta$
  feedback: |-
    Sine is useful for a difference such as $1-(4x)^2$, since $1-\sin^2\theta=\cos^2\theta$. Here the plus sign calls for tangent, giving $1+\tan^2\theta=\sec^2\theta$.
- id: recognize-unscaled
  content: |-
    $x=\tan\theta$
  feedback: |-
    This misses the scale inside the square. It produces $1+16\tan^2\theta$, whereas setting the whole quantity $4x$ equal to $\tan\theta$ produces the exact secant-tangent identity.
- id: recognize-secant
  content: |-
    $4x=\sec\theta$
  feedback: |-
    The identity relates $1+\tan^2\theta$ to $\sec^2\theta$; there is no corresponding simplification for $1+\sec^2\theta$. The squared term must be matched with tangent.
```

---

<a id="transform-the-entire-integral"></a>
## Transform the Entire Integral

**Example:** Rewrite and evaluate the trigonometric integral obtained from

$$
\int\frac{dx}{\sqrt{1+4x^2}}.
$$

**Explanation**

From $2x=\tan\theta$,

$$
2\,dx=\sec^2\theta\,d\theta
\qquad\Longrightarrow\qquad
dx=\frac12\sec^2\theta\,d\theta.
$$

Choose $-\pi/2<\theta<\pi/2$, where $\sec\theta>0$. Then

$$
\sqrt{1+4x^2}
=\sqrt{1+\tan^2\theta}
=\sqrt{\sec^2\theta}
=\sec\theta.
$$

Substitute both pieces before canceling:

$$
\begin{aligned}
\int\frac{dx}{\sqrt{1+4x^2}}
&=\int\frac{\frac12\sec^2\theta\,d\theta}{\sec\theta}\\
&=\frac12\int\sec\theta\,d\theta\\
&=\frac12\ln\left|\sec\theta+\tan\theta\right|+C.
\end{aligned}
$$

```quiz
type: radio
id: whw6-p1-transform
content: |-
  For $\displaystyle\int\frac{dx}{\sqrt{1+25x^2}}$, let $5x=\tan\theta$. What integral remains after rewriting $dx$ and simplifying the radical?
options:
- id: transform-correct
  content: |-
    $\displaystyle\frac15\int\sec\theta\,d\theta$
  correct: true
  feedback: |-
    Differentiating $5x=\tan\theta$ gives $dx=\frac15\sec^2\theta\,d\theta$, while the radical becomes $\sec\theta$. Dividing leaves $\frac15\int\sec\theta\,d\theta$.
- id: transform-reciprocal
  content: |-
    $\displaystyle5\int\sec\theta\,d\theta$
  feedback: |-
    The factor from the differential is reciprocal: $5\,dx=\sec^2\theta\,d\theta$ means $dx=\frac15\sec^2\theta\,d\theta$. The secant cancellation is right, but the scale must be $1/5$, not $5$.
- id: transform-no-cancel
  content: |-
    $\displaystyle\frac15\int\sec^2\theta\,d\theta$
  feedback: |-
    The $\sec^2\theta$ comes from $dx$, but the denominator contributes one factor of $\sec\theta$. Their quotient is $\sec\theta$, so one secant factor must cancel.
- id: transform-overcancel
  content: |-
    $\displaystyle\frac15\int 1\,d\theta$
  feedback: |-
    The radical is $\sec\theta$, not $\sec^2\theta$. Thus $\sec^2\theta/\sec\theta=\sec\theta$; canceling both powers removes one factor too many.
- id: transform-forgot-scale
  content: |-
    $\displaystyle\int\sec\theta\,d\theta$
  feedback: |-
    Simplifying the trigonometric factors gives $\sec\theta$, but differentiating $5x=\tan\theta$ also contributes $1/5$ through $dx=\frac15\sec^2\theta\,d\theta$.
```

---

<a id="return-the-antiderivative-to-x"></a>
## Return the Antiderivative to $x$

**Example:** Evaluate the assigned integral

$$
\int\frac{dx}{\sqrt{1+9x^2}}
$$

and express the answer in terms of $x$.

**Explanation**

Write $1+9x^2=1+(3x)^2$ and set

$$
3x=\tan\theta,
\qquad
dx=\frac13\sec^2\theta\,d\theta.
$$

As in the previous example,

$$
\int\frac{dx}{\sqrt{1+9x^2}}
=\frac13\int\sec\theta\,d\theta
=\frac13\ln\left|\sec\theta+\tan\theta\right|+C.
$$

Now use $\tan\theta=3x$. The identity also gives

$$
\sec\theta=\sqrt{1+\tan^2\theta}=\sqrt{1+9x^2}.
$$

Therefore,

$$
\boxed{
\int\frac{dx}{\sqrt{1+9x^2}}
=\frac13\ln\left(\sqrt{1+9x^2}+3x\right)+C
}.
$$

The logarithm's argument is positive because $\sqrt{1+9x^2}>|3x|$, so absolute-value bars are optional after back-substitution.

Differentiate to check the result. Let $s=\sqrt{1+9x^2}$. Then

$$
\begin{aligned}
\frac{d}{dx}\left[\frac13\ln(s+3x)\right]
&=\frac13\frac{9x/s+3}{s+3x}\\
&=\frac13\frac{3(3x+s)}{s(s+3x)}\\
&=\frac1s
=\frac{1}{\sqrt{1+9x^2}}.
\end{aligned}
$$

```quiz
type: radio
id: whw6-p1-back-substitute
content: |-
  If $2x=\tan\theta$ and the transformed antiderivative is $\frac12\ln|\sec\theta+\tan\theta|+C$, which expression is entirely in terms of $x$?
options:
- id: back-correct
  content: |-
    $\displaystyle\frac12\ln\left(\sqrt{1+4x^2}+2x\right)+C$
  correct: true
  feedback: |-
    The substitution gives $\tan\theta=2x$, and the identity gives $\sec\theta=\sqrt{1+4x^2}$. Replacing both trigonometric terms while retaining the factor $1/2$ gives the stated logarithm.
- id: back-incomplete-tangent
  content: |-
    $\displaystyle\frac12\ln\left(\sqrt{1+4x^2}+x\right)+C$
  feedback: |-
    The secant conversion is correct, but the substitution says $\tan\theta=2x$, not $x$. Back-substitution must replace each trigonometric term using the original scaled equation.
- id: back-missing-factor
  content: |-
    $\displaystyle\ln\left(\sqrt{1+4x^2}+2x\right)+C$
  feedback: |-
    The logarithm has been converted correctly, but the factor $1/2$ came from $dx=\frac12\sec^2\theta\,d\theta$ and remains outside the antiderivative.
- id: back-arctangent
  content: |-
    $\displaystyle\frac12\arctan(2x)+C$
  feedback: |-
    Arctangent differentiates to a multiple of $1/(1+4x^2)$, without a square root. Here the transformed integral is $\int\sec\theta\,d\theta$, whose antiderivative is logarithmic.
- id: back-missing-tangent
  content: |-
    $\displaystyle\frac12\ln\left(\sqrt{1+4x^2}\right)+C$
  feedback: |-
    The antiderivative of secant contains the sum $\sec\theta+\tan\theta$. Converting only the secant term drops $\tan\theta=2x$ and changes the derivative.
```

---

<a id="do-not-drop-the-square-root"></a>
## Do Not Drop the Square Root

**Example:** Compare the two denominator patterns

$$
I_1=\int\frac{dx}{\sqrt{1+9x^2}}
\qquad\text{and}\qquad
I_2=\int\frac{dx}{1+9x^2}.
$$

**Explanation**

The exponent on the denominator decides the antiderivative family. The radical in $I_1$ leads, through tangent substitution, to an integral of secant and therefore a logarithm:

$$
I_1=\frac13\ln\left(\sqrt{1+9x^2}+3x\right)+C.
$$

The denominator of $I_2$ has no square root. With $u=3x$, it matches $\int du/(1+u^2)$ and therefore gives arctangent:

$$
I_2=\frac13\arctan(3x)+C.
$$

The two integrands differ only by the denominator power, but that difference cannot be ignored.

```quiz
type: radio
id: whw6-p1-radical-trap
content: |-
  Evaluate $\displaystyle\int\frac{dx}{\sqrt{1+36x^2}}$ in terms of $x$.
options:
- id: trap-log-correct
  content: |-
    $\displaystyle\frac16\ln\left(\sqrt{1+36x^2}+6x\right)+C$
  correct: true
  feedback: |-
    The radical has the pattern $\sqrt{1+(6x)^2}$, so $6x=\tan\theta$ leaves $\frac16\int\sec\theta\,d\theta$. Integrating secant and back-substituting gives the stated logarithm.
- id: trap-arctangent
  content: |-
    $\displaystyle\frac16\arctan(6x)+C$
  feedback: |-
    Differentiating this expression gives $1/(1+36x^2)$, which has no square root in its denominator. The radical pattern transforms to secant, so its antiderivative is logarithmic instead.
- id: trap-missing-reciprocal
  content: |-
    $\displaystyle\ln\left(\sqrt{1+36x^2}+6x\right)+C$
  feedback: |-
    The logarithmic form is right, but $6x=\tan\theta$ gives $dx=\frac16\sec^2\theta\,d\theta$. Omitting $1/6$ makes the derivative six times the requested integrand.
- id: trap-flipped-reciprocal
  content: |-
    $\displaystyle6\ln\left(\sqrt{1+36x^2}+6x\right)+C$
  feedback: |-
    The coefficient from rewriting $dx$ is the reciprocal of $6$, not $6$. Because $6\,dx=\sec^2\theta\,d\theta$, the antiderivative must carry a factor of $1/6$.
- id: trap-log-radicand
  content: |-
    $\displaystyle\frac16\ln(1+36x^2)+C$
  feedback: |-
    A logarithm of the radicand would differentiate to a rational expression with an $x$ in the numerator. Integrating secant instead produces $\ln|\sec\theta+\tan\theta|$, so back-substitution requires the sum $\sqrt{1+36x^2}+6x$.
```

---

<a id="summary"></a>
## Summary

For an integral with $\sqrt{1+(kx)^2}$ in the denominator:

1. Match the squared quantity: set $kx=\tan\theta$.
2. Rewrite the differential: $dx=\frac1k\sec^2\theta\,d\theta$.
3. Use $\sqrt{1+\tan^2\theta}=\sec\theta$ on $-\pi/2<\theta<\pi/2$.
4. Integrate the remaining secant and replace $\tan\theta$ and $\sec\theta$ with expressions in $x$.

For $k>0$, the reusable result is

$$
\int\frac{dx}{\sqrt{1+k^2x^2}}
=\frac1k\ln\left(\sqrt{1+k^2x^2}+kx\right)+C.
$$

The main traps are missing the reciprocal factor $1/k$, failing to cancel exactly one secant, stopping with $\theta$ still in the answer, and using the arctangent rule after overlooking the square root.
