# Integrating a $\sqrt{x^2+1}$ Radical with Tangent Substitution

## Table of Contents

- [Introduction](#introduction)
- [Choose the Substitution from the Radical](#choose-the-substitution-from-the-radical)
- [Transform Every Factor Before Integrating](#transform-every-factor-before-integrating)
- [Recognize the Reciprocal-Trig Derivative](#recognize-the-reciprocal-trig-derivative)
- [Back-Substitute and Verify](#back-substitute-and-verify)
- [Carry a Scale Through the Full Chain](#carry-a-scale-through-the-full-chain)
- [Summary](#summary)

## Prerequisites

- The identity $1+\tan^2\theta=\sec^2\theta$
- The derivatives $\dfrac{d}{d\theta}(\tan\theta)=\sec^2\theta$ and $\dfrac{d}{d\theta}(\csc\theta)=-\csc\theta\cot\theta$
- Rewriting tangent, secant, cotangent, and cosecant in terms of sine and cosine

---

<a id="introduction"></a>
## Introduction

The radical $\sqrt{x^2+1}$ is the recognition cue for a tangent substitution because $1+\tan^2\theta=\sec^2\theta$. For

$$
\int \frac{dx}{x^2\sqrt{x^2+1}},
$$

choose $x=\tan\theta$, rewrite the radical, $x^2$, and $dx$ in terms of $\theta$, simplify to a familiar trigonometric derivative, and then return the result to $x$.

The reusable chain is

$$
\sqrt{x^2+1}
\;\longrightarrow\;
x=\tan\theta
\;\longrightarrow\;
\csc\theta\cot\theta
\;\longrightarrow\;
-\csc\theta
\;\longrightarrow\;
-\frac{\sqrt{x^2+1}}{x}.
$$

---

<a id="choose-the-substitution-from-the-radical"></a>
## Choose the Substitution from the Radical

**Example:** Choose a trigonometric substitution for $\sqrt{x^2+1}$.

**Explanation**

Set

$$
x=\tan\theta, \qquad -\frac{\pi}{2}<\theta<\frac{\pi}{2}.
$$

On this interval, $\sec\theta>0$, so

$$
\sqrt{x^2+1}
=\sqrt{\tan^2\theta+1}
=\sqrt{\sec^2\theta}
=\sec\theta.
$$

Differentiating the substitution also gives

$$
dx=\sec^2\theta\,d\theta.
$$

```quiz
type: radio
id: p3-choose-substitution
content: |-
  Which substitution turns $\sqrt{t^2+9}$ into a single trigonometric function?
options:
- id: p3-choose-a
  content: |-
    $t=3\tan\phi$
  correct: true
  feedback: |-
    The plus-sign radical matches $1+\tan^2\phi=\sec^2\phi$. With $t=3\tan\phi$, $\sqrt{t^2+9}=3\sqrt{\tan^2\phi+1}=3\sec\phi$ on the standard tangent-substitution interval.
- id: p3-choose-b
  content: |-
    $t=3\sin\phi$
  feedback: |-
    This produces $3\sqrt{1+\sin^2\phi}$, and $1+\sin^2\phi$ is not a Pythagorean identity that becomes one squared trig function. A sum of a variable square and a positive constant calls for tangent here.
- id: p3-choose-c
  content: |-
    $t=3\sec\phi$
  feedback: |-
    Secant substitution would produce $3\sqrt{\sec^2\phi+1}$, which does not simplify to one trig function. The substitution $t=3\sec\phi$ instead naturally matches a difference such as $\sqrt{t^2-9}$.
- id: p3-choose-d
  content: |-
    $t=\tan\phi$
  feedback: |-
    Tangent is the right function, but this choice misses the scale $3$. It leaves $\sqrt{\tan^2\phi+9}$; using $t=3\tan\phi$ factors out $9$ and creates $1+\tan^2\phi$.
- id: p3-choose-e
  content: |-
    $t=3\cos\phi$
  feedback: |-
    This gives $3\sqrt{1+\cos^2\phi}$, not a single trigonometric function. Cosine is useful for expressions built from $1-\sin^2\phi$ or $1-\cos^2\phi$, whereas this plus-sign radical matches tangent.
```

---

<a id="transform-every-factor-before-integrating"></a>
## Transform Every Factor Before Integrating

**Example:** Rewrite $\displaystyle \int \frac{dx}{x^2\sqrt{x^2+1}}$ using $x=\tan\theta$.

**Explanation**

Replace all three changing pieces before simplifying:

| Original piece | Replacement |
| --- | --- |
| $x^2$ | $\tan^2\theta$ |
| $\sqrt{x^2+1}$ | $\sec\theta$ |
| $dx$ | $\sec^2\theta\,d\theta$ |

Therefore,

$$
\begin{aligned}
\int \frac{dx}{x^2\sqrt{x^2+1}}
&=\int \frac{\sec^2\theta}{\tan^2\theta\sec\theta}\,d\theta \\
&=\int \frac{\sec\theta}{\tan^2\theta}\,d\theta \\
&=\int \frac{\cos\theta}{\sin^2\theta}\,d\theta \\
&=\int \csc\theta\cot\theta\,d\theta.
\end{aligned}
$$

The useful cancellation appears only after $dx$ and every factor in the denominator have been transformed.

```quiz
type: radio
id: p3-transform-integrand
content: |-
  After using $u=\tan\phi$ in $\displaystyle\int\frac{du}{u^2\sqrt{u^2+1}}$, which fully simplified trigonometric integral results?
options:
- id: p3-transform-a
  content: |-
    $\displaystyle\int\csc\phi\cot\phi\,d\phi$
  correct: true
  feedback: |-
    The substitution gives $du=\sec^2\phi\,d\phi$, $u^2=\tan^2\phi$, and $\sqrt{u^2+1}=\sec\phi$. Their quotient is $\sec\phi/\tan^2\phi=\cos\phi/\sin^2\phi=\csc\phi\cot\phi$.
- id: p3-transform-b
  content: |-
    $\displaystyle\int\sec\phi\tan\phi\,d\phi$
  feedback: |-
    This derivative pattern would arise from a factor $\sin\phi/\cos^2\phi$. Here the denominator contains $\tan^2\phi$, so simplification gives $\cos\phi/\sin^2\phi$, the cosecant-cotangent pattern instead.
- id: p3-transform-c
  content: |-
    $\displaystyle\int\csc^2\phi\,d\phi$
  feedback: |-
    This drops the remaining factor of $\cos\phi$. In fact, $\sec\phi/\tan^2\phi=\cos\phi/\sin^2\phi$, not $1/\sin^2\phi$.
- id: p3-transform-d
  content: |-
    $\displaystyle\int\cos\phi\,d\phi$
  feedback: |-
    The $\sec^2\phi$ from $du$ cancels only one $\sec\phi$ from the radical. The $\tan^2\phi$ from $u^2$ remains in the denominator, leaving $\cos\phi/\sin^2\phi$ rather than just $\cos\phi$.
- id: p3-transform-e
  content: |-
    $\displaystyle\int\frac{\sin\phi}{\cos^2\phi}\,d\phi$
  feedback: |-
    This reverses the sine and cosine roles. Rewriting $\sec\phi/\tan^2\phi$ gives $(1/\cos\phi)/(\sin^2\phi/\cos^2\phi)=\cos\phi/\sin^2\phi$.
```

---

<a id="recognize-the-reciprocal-trig-derivative"></a>
## Recognize the Reciprocal-Trig Derivative

**Example:** Evaluate $\displaystyle\int\csc\theta\cot\theta\,d\theta$.

**Explanation**

Because

$$
\frac{d}{d\theta}(\csc\theta)=-\csc\theta\cot\theta,
$$

the required antiderivative has a minus sign:

$$
\int\csc\theta\cot\theta\,d\theta=-\csc\theta+C.
$$

```quiz
type: radio
id: p3-recognize-antiderivative
content: |-
  Evaluate $\displaystyle\int\frac{\cos\phi}{\sin^2\phi}\,d\phi$.
options:
- id: p3-recognize-a
  content: |-
    $-\csc\phi+C$
  correct: true
  feedback: |-
    Since $\cos\phi/\sin^2\phi=\csc\phi\cot\phi$ and the derivative of cosecant is $-\csc\phi\cot\phi$, the antiderivative is $-\csc\phi+C$.
- id: p3-recognize-b
  content: |-
    $\csc\phi+C$
  feedback: |-
    Differentiating $\csc\phi$ gives $-\cos\phi/\sin^2\phi$, the negative of the integrand. The antiderivative therefore needs the leading minus sign.
- id: p3-recognize-c
  content: |-
    $\tan\phi+C$
  feedback: |-
    The derivative of tangent is $\sec^2\phi=1/\cos^2\phi$. The given integrand instead has cosine over sine squared, so it matches the cosecant derivative pattern.
- id: p3-recognize-d
  content: |-
    $-\sec\phi+C$
  feedback: |-
    Differentiating $-\sec\phi$ gives $-\sin\phi/\cos^2\phi$. That has the reciprocal sine-cosine arrangement; $\cos\phi/\sin^2\phi$ is tied to cosecant, not secant.
- id: p3-recognize-e
  content: |-
    $-\cot\phi+C$
  feedback: |-
    The derivative of $-\cot\phi$ is $\csc^2\phi=1/\sin^2\phi$, which lacks the numerator factor $\cos\phi$. Keeping that factor leads to $-\csc\phi$ instead.
```

---

<a id="back-substitute-and-verify"></a>
## Back-Substitute and Verify

**Example:** Express $-\csc\theta+C$ in terms of $x$ when $x=\tan\theta$, and finish the original integral.

**Explanation**

Use a ratio rather than introducing $\arctan x$:

$$
\csc\theta
=\frac{\sec\theta}{\tan\theta}
=\frac{\sqrt{x^2+1}}{x}.
$$

Thus, on any interval not containing $x=0$,

$$
\boxed{\int \frac{dx}{x^2\sqrt{x^2+1}}
=-\frac{\sqrt{x^2+1}}{x}+C}.
$$

Differentiate to check the result. If $F(x)=-\sqrt{x^2+1}/x$, then

$$
\begin{aligned}
F'(x)
&=-\left(\frac{1}{\sqrt{x^2+1}}-\frac{\sqrt{x^2+1}}{x^2}\right) \\
&=\frac{1}{x^2\sqrt{x^2+1}},
\end{aligned}
$$

which reproduces the original integrand.

```quiz
type: radio
id: p3-back-substitute
content: |-
  If $u=2\tan\phi$, which expression equals $\csc\phi$ in terms of $u$?
options:
- id: p3-back-a
  content: |-
    $\displaystyle\frac{\sqrt{u^2+4}}{u}$
  correct: true
  feedback: |-
    From $\tan\phi=u/2$ and $\sec\phi=\sqrt{u^2+4}/2$, use $\csc\phi=\sec\phi/\tan\phi$. The factors of $2$ cancel, giving $\csc\phi=\sqrt{u^2+4}/u$.
- id: p3-back-b
  content: |-
    $\displaystyle\frac{u}{\sqrt{u^2+4}}$
  feedback: |-
    This ratio is $\sin\phi$, opposite over hypotenuse. Cosecant is its reciprocal, so the hypotenuse $\sqrt{u^2+4}$ must be over $u$.
- id: p3-back-c
  content: |-
    $\displaystyle\frac{\sqrt{u^2+4}}{2}$
  feedback: |-
    This is $\sec\phi$, hypotenuse over adjacent. Cosecant instead uses the opposite side $u$ in the denominator.
- id: p3-back-d
  content: |-
    $\displaystyle\frac{2}{u}$
  feedback: |-
    This is $\cot\phi$, adjacent over opposite. Cosecant uses the hypotenuse rather than the adjacent side in its numerator.
- id: p3-back-e
  content: |-
    $\displaystyle\frac{\sqrt{u^2-4}}{u}$
  feedback: |-
    The right-triangle relation is $u^2+2^2=(\text{hypotenuse})^2$, so the hypotenuse is $\sqrt{u^2+4}$. A minus sign would not match the tangent substitution $u=2\tan\phi$.
```

---

<a id="carry-a-scale-through-the-full-chain"></a>
## Carry a Scale Through the Full Chain

**Example:** Evaluate $\displaystyle\int\frac{dt}{t^2\sqrt{t^2+9}}$.

**Explanation**

The radical has the form $\sqrt{t^2+3^2}$, so set $t=3\tan\phi$. Then

$$
dt=3\sec^2\phi\,d\phi,
\qquad
t^2=9\tan^2\phi,
\qquad
\sqrt{t^2+9}=3\sec\phi.
$$

Keeping the scale factors visible gives

$$
\begin{aligned}
\int\frac{dt}{t^2\sqrt{t^2+9}}
&=\int\frac{3\sec^2\phi}{(9\tan^2\phi)(3\sec\phi)}\,d\phi \\
&=\frac{1}{9}\int\csc\phi\cot\phi\,d\phi \\
&=-\frac{1}{9}\csc\phi+C.
\end{aligned}
$$

Since $\tan\phi=t/3$, we have $\csc\phi=\sqrt{t^2+9}/t$. Therefore,

$$
\int\frac{dt}{t^2\sqrt{t^2+9}}
=-\frac{\sqrt{t^2+9}}{9t}+C.
$$

```quiz
type: radio
id: p3-scaled-full-chain
content: |-
  Evaluate $\displaystyle\int\frac{du}{u^2\sqrt{u^2+4}}$.
options:
- id: p3-scaled-a
  content: |-
    $\displaystyle-\frac{\sqrt{u^2+4}}{4u}+C$
  correct: true
  feedback: |-
    With $u=2\tan\phi$, the transformed integral is $\frac14\int\csc\phi\cot\phi\,d\phi$. Integrating gives $-\frac14\csc\phi$, and $\csc\phi=\sqrt{u^2+4}/u$, so the result is $-\sqrt{u^2+4}/(4u)+C$.
- id: p3-scaled-b
  content: |-
    $\displaystyle-\frac{\sqrt{u^2+4}}{2u}+C$
  feedback: |-
    This keeps only one factor of the scale $2$. The factors $u^2=4\tan^2\phi$, $\sqrt{u^2+4}=2\sec\phi$, and $du=2\sec^2\phi\,d\phi$ combine to the coefficient $2/(4\cdot2)=1/4$, not $1/2$.
- id: p3-scaled-c
  content: |-
    $\displaystyle\frac{\sqrt{u^2+4}}{4u}+C$
  feedback: |-
    The scale factor $1/4$ is correct, but the antiderivative sign is not. Since $d(\csc\phi)/d\phi=-\csc\phi\cot\phi$, integrating the positive cosecant-cotangent product requires a minus sign.
- id: p3-scaled-d
  content: |-
    $\displaystyle-\frac{\sqrt{u^2+4}}{u}+C$
  feedback: |-
    This is the result for a unit scale and ignores the $2$ in $u=2\tan\phi$. The transformed coefficient is $1/2^2=1/4$, so the back-substituted expression must retain that factor.
- id: p3-scaled-e
  content: |-
    $\displaystyle-\frac{u}{4\sqrt{u^2+4}}+C$
  feedback: |-
    The transformed antiderivative contains $\csc\phi$, but $u/\sqrt{u^2+4}$ represents $\sin\phi$. Cosecant is the reciprocal, $\sqrt{u^2+4}/u$, while the coefficient remains $-1/4$.
```

---

<a id="summary"></a>
## Summary

For $\sqrt{x^2+a^2}$ with $a>0$, choose $x=a\tan\theta$ so the radical becomes $a\sec\theta$. Transform $x^2$, the radical, and $dx$ before canceling; this integrand becomes a constant multiple of $\csc\theta\cot\theta$. Integrate with the required minus sign, use $\csc\theta=\sqrt{x^2+a^2}/x$, and differentiate the final expression to catch a sign or scale-factor error.
