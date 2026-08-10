# Substitute, Factor, and Decompose a Trigonometric Integral

## Table of Contents

- [Introduction](#introduction)
- [Choose the Substitution from the Differential Cue](#choose-the-substitution-from-the-differential-cue)
- [Factor Before Setting Up Partial Fractions](#factor-before-setting-up-partial-fractions)
- [Track Both Chain-Rule Signs](#track-both-chain-rule-signs)
- [Back-Substitute and Verify](#back-substitute-and-verify)
- [Summary](#summary)

## Prerequisites

- Using $u$-substitution and rewriting the differential
- Factoring a difference of squares
- Setting up partial fractions for two distinct linear factors
- Integrating $1/(au+b)$ with a natural logarithm

---

<a id="introduction"></a>
## Introduction

In

$$
\int \frac{\sin x}{1-\cos^2 x}\,dx,
$$

the numerator $\sin x\,dx$ is the negative of $d(\cos x)$, while the denominator is a polynomial in $\cos x$. This is the cue to use $u=\cos x$ and convert the trigonometric integral into a rational one.

The order of the algebra matters:

$$
\boxed{\text{substitute in }u\;\longrightarrow\;\text{factor the polynomial}\;\longrightarrow\;\text{set up partial fractions}.}
$$

In particular, factor the rational denominator before writing the partial-fraction decomposition. The full route is

$$
\int \frac{\sin x}{1-\cos^2x}\,dx
\longrightarrow
-\int\frac{du}{1-u^2}
\longrightarrow
-\int\frac{du}{(1-u)(1+u)}
\longrightarrow
\text{two logarithms}.
$$

At each stage, use a different check:

| Stage | What should be true before moving on? |
| --- | --- |
| Substitute | No $x$ or trigonometric function remains in the integral. |
| Factor | Every denominator factor needed for the decomposition is visible. |
| Decompose | Recombining the partial fractions reproduces the original rational function. |
| Integrate | Differentiating the logarithmic result returns the original integrand. |

---

<a id="choose-the-substitution-from-the-differential-cue"></a>
## Choose the Substitution from the Differential Cue

**Example:** Convert $\displaystyle\int \frac{\sin x}{1-\cos^2x}\,dx$ into an integral in $u$.

**Explanation**

Choose the repeated inner expression in the denominator:

$$
u=\cos x.
$$

Then

$$
du=-\sin x\,dx,
\qquad
\sin x\,dx=-du.
$$

Replace both $\cos x$ and the entire differential factor $\sin x\,dx$:

| Original piece | Replacement |
| --- | --- |
| $\cos x$ | $u$ |
| $\cos^2x$ | $u^2$ |
| $\sin x\,dx$ | $-du$ |

$$
\int \frac{\sin x}{1-\cos^2x}\,dx
=-\int\frac{du}{1-u^2}.
$$

The minus sign belongs to the substitution and must travel through the rest of the calculation.

```quiz
type: radio
id: p6-choose-substitution
content: |-
  Which line correctly converts $\displaystyle\int \frac{\sin x}{1-\cos^2x}\,dx$ into a rational integral?
options:
- id: p6-choose-a
  content: |-
    $u=\cos x$, $du=-\sin x\,dx$, so the integral becomes $\displaystyle-\int\frac{du}{1-u^2}$.
  correct: true
  feedback: |-
    The denominator is a polynomial in $\cos x$, and $d(\cos x)=-\sin x\,dx$. Thus $u=\cos x$ replaces every trigonometric occurrence and contributes the required outside minus sign, giving $-\int du/(1-u^2)$.
- id: p6-choose-b
  content: |-
    $u=\cos x$, $du=\sin x\,dx$, so the integral becomes $\displaystyle\int\frac{du}{1-u^2}$.
  feedback: |-
    This uses the right inner expression but differentiates cosine with the wrong sign. Since $du=-\sin x\,dx$, the transformed integral must have a leading minus sign.
- id: p6-choose-c
  content: |-
    $u=\sin x$, $du=\cos x\,dx$, so the integral becomes $\displaystyle\int\frac{du}{1-u^2}$.
  feedback: |-
    The differential for $u=\sin x$ requires $\cos x\,dx$, which is not the numerator. It also does not directly replace both occurrences of cosine in the denominator; $u=\cos x$ matches the denominator and the numerator differential at once.
- id: p6-choose-d
  content: |-
    $u=\tan x$, $du=\sec^2x\,dx$, so the integral becomes $\displaystyle\int\frac{du}{1-u^2}$.
  feedback: |-
    A tangent substitution needs a $\sec^2x\,dx$ differential, but the numerator supplies $\sin x\,dx$. The direct derivative cue is instead $d(\cos x)=-\sin x\,dx$.
- id: p6-choose-e
  content: |-
    $u=\cos^2x$, $du=-2\sin x\,dx$, so the integral becomes $\displaystyle-\frac12\int\frac{du}{1-u}$.
  feedback: |-
    The stated differential is missing a factor of $\cos x$: actually $d(\cos^2x)=-2\cos x\sin x\,dx$. Because that extra cosine is absent from the integrand, $u=\cos^2x$ does not give the displayed rational integral.
```

---

<a id="factor-before-setting-up-partial-fractions"></a>
## Factor Before Setting Up Partial Fractions

**Example:** Decompose $\displaystyle\frac{1}{1-u^2}$ into partial fractions.

**Explanation**

First factor the difference of squares:

$$
1-u^2=(1-u)(1+u).
$$

Only after the factors are visible do we write

$$
\frac{1}{(1-u)(1+u)}
=\frac{A}{1-u}+\frac{B}{1+u}.
$$

Clearing denominators gives

$$
1=A(1+u)+B(1-u).
$$

Set $u=1$ to obtain $A=\frac12$, and set $u=-1$ to obtain $B=\frac12$. Therefore,

$$
\frac{1}{1-u^2}
=\frac{1}{2(1-u)}+\frac{1}{2(1+u)}.
$$

Recombining verifies the coefficients before any integration:

$$
\frac{1}{2(1-u)}+\frac{1}{2(1+u)}
=\frac{(1+u)+(1-u)}{2(1-u)(1+u)}
=\frac{1}{1-u^2}.
$$

The transformed integral is now

$$
-\frac12\int\left(\frac{1}{1-u}+\frac{1}{1+u}\right)du.
$$

```quiz
type: radio
id: p6-factor-decompose
content: |-
  After factoring $4-v^2$, which partial-fraction decomposition is correct?
options:
- id: p6-factor-a
  content: |-
    $\displaystyle\frac{1}{4-v^2}=\frac{1}{4(2-v)}+\frac{1}{4(2+v)}$
  correct: true
  feedback: |-
    The difference of squares factors as $(2-v)(2+v)$. Writing $A/(2-v)+B/(2+v)$ and substituting $v=2$ and $v=-2$ gives $A=B=1/4$, so the displayed decomposition recombines to $1/(4-v^2)$.
- id: p6-factor-b
  content: |-
    $\displaystyle\frac{1}{4-v^2}=\frac{1}{2(2-v)}+\frac{1}{2(2+v)}$
  feedback: |-
    These coefficients are too large. Recombining the two terms produces $2/(4-v^2)$; at $v=2$, the cleared equation is $1=4A$, so the coefficient must be $A=1/4$, not $1/2$.
- id: p6-factor-c
  content: |-
    $\displaystyle\frac{1}{4-v^2}=\frac{1}{4(2-v)}-\frac{1}{4(2+v)}$
  feedback: |-
    Opposite coefficient signs make the numerator depend on $v$: the right side recombines to $v/[2(4-v^2)]$. Because the original numerator is the constant $1$, the two coefficients must have the same positive sign.
- id: p6-factor-d
  content: |-
    $\displaystyle\frac{1}{4-v^2}=\frac{1}{4(4-v)}+\frac{1}{4(4+v)}$
  feedback: |-
    The factors are incorrect: $(4-v)(4+v)=16-v^2$, not $4-v^2$. The square roots of $4$ are $\pm2$, so the required linear factors are $2-v$ and $2+v$.
- id: p6-factor-e
  content: |-
    $\displaystyle\frac{1}{4-v^2}=\frac{1}{4(v-2)}+\frac{1}{4(v+2)}$
  feedback: |-
    Replacing $2-v$ by $v-2$ changes that factor's sign. With both displayed plus signs, the right side recombines to $v/[2(v^2-4)]$, not $1/(4-v^2)$; using $2-v$ preserves the difference-of-squares factorization used here.
```

---

<a id="track-both-chain-rule-signs"></a>
## Track Both Chain-Rule Signs

**Example:** Integrate $\displaystyle-\frac12\left(\frac{1}{1-u}+\frac{1}{1+u}\right)$.

**Explanation**

There are two different signs to track:

- the outside minus sign came from $du=-\sin x\,dx$;
- $d(1-u)=-du$, while $d(1+u)=du$.

Thus,

$$
\begin{aligned}
-\frac12\int\left(\frac{1}{1-u}+\frac{1}{1+u}\right)du
&=-\frac12\left(-\ln|1-u|+\ln|1+u|\right)+C\\
&=\frac12\ln|1-u|-\frac12\ln|1+u|+C.
\end{aligned}
$$

A quick derivative check of each logarithm is safer than assigning signs from memory.

```quiz
type: radio
id: p6-track-signs
content: |-
  Evaluate $\displaystyle-\frac14\int\left(\frac{1}{2-v}+\frac{1}{2+v}\right)dv$.
options:
- id: p6-signs-a
  content: |-
    $\displaystyle\frac14\ln|2-v|-\frac14\ln|2+v|+C$
  correct: true
  feedback: |-
    Since $d(2-v)=-dv$ and $d(2+v)=dv$, the two inner antiderivatives are $-\ln|2-v|$ and $\ln|2+v|$. Multiplying both by the outside $-1/4$ gives the displayed opposite-sign logarithms.
- id: p6-signs-b
  content: |-
    $\displaystyle-\frac14\ln|2-v|+\frac14\ln|2+v|+C$
  feedback: |-
    This is the negative of the required antiderivative and results from dropping the outside minus sign. Differentiating it gives $+\frac14[1/(2-v)+1/(2+v)]$, whereas the integrand has a leading negative.
- id: p6-signs-c
  content: |-
    $\displaystyle\frac14\ln|2-v|+\frac14\ln|2+v|+C$
  feedback: |-
    The first logarithm has the correct final sign, but the second does not. Because $d(2+v)=dv$, its integral initially has a positive logarithm, which the outside $-1/4$ changes to a negative term.
- id: p6-signs-d
  content: |-
    $\displaystyle-\frac14\ln|2-v|-\frac14\ln|2+v|+C$
  feedback: |-
    This treats both linear denominators as if their derivatives were $+1$. In fact, $d(2-v)=-dv$, so integrating $1/(2-v)$ contributes an extra minus that cancels the outside minus for the first logarithm.
- id: p6-signs-e
  content: |-
    $\displaystyle\ln|2-v|-\ln|2+v|+C$
  feedback: |-
    The logarithm signs reflect the two chain-rule signs, but the common coefficient $1/4$ has been lost. Constants multiplying an integrand remain as coefficients of its antiderivative.
```

---

<a id="back-substitute-and-verify"></a>
## Back-Substitute and Verify

**Example:** Finish $\displaystyle\int \frac{\sin x}{1-\cos^2x}\,dx$ and check the result.

**Explanation**

Return to $x$ by replacing $u$ with $\cos x$:

$$
\begin{aligned}
\int \frac{\sin x}{1-\cos^2x}\,dx
&=\frac12\ln|1-\cos x|-\frac12\ln|1+\cos x|+C\\
&=\frac12\ln\left|\frac{1-\cos x}{1+\cos x}\right|+C.
\end{aligned}
$$

The absolute values are part of the logarithmic antiderivative. The formula is understood on any interval where the original integrand is defined.

To verify, differentiate the combined form:

$$
\begin{aligned}
\frac{d}{dx}\left[\frac12\ln\left|\frac{1-\cos x}{1+\cos x}\right|\right]
&=\frac12\left(\frac{\sin x}{1-\cos x}+\frac{\sin x}{1+\cos x}\right)\\
&=\frac{\sin x}{1-\cos^2x}.
\end{aligned}
$$

```quiz
type: radio
id: p6-complete-chain
content: |-
  Use the same substitution-factor-decomposition chain to evaluate $\displaystyle\int\frac{\sin t}{4-\cos^2t}\,dt$.
options:
- id: p6-chain-a
  content: |-
    $\displaystyle\frac14\ln\left|\frac{2-\cos t}{2+\cos t}\right|+C$
  correct: true
  feedback: |-
    With $v=\cos t$, $dv=-\sin t\,dt$, the integral becomes $-\int dv/[(2-v)(2+v)]$. The decomposition has coefficients $1/4$, and the two linear factors yield opposite-sign logarithms, giving the stated result after back-substitution.
- id: p6-chain-b
  content: |-
    $\displaystyle\frac14\ln\left|\frac{2+\cos t}{2-\cos t}\right|+C$
  feedback: |-
    Reversing the logarithmic ratio negates the antiderivative. That sign would correspond to using $dv=+\sin t\,dt$, but $d(\cos t)=-\sin t\,dt$, so the numerator and denominator of the ratio must appear in the displayed opposite order.
- id: p6-chain-c
  content: |-
    $\displaystyle\frac12\ln\left|\frac{2-\cos t}{2+\cos t}\right|+C$
  feedback: |-
    This has the right logarithmic ratio but twice the required coefficient. Clearing denominators in $1/[(2-v)(2+v)]=A/(2-v)+B/(2+v)$ gives $A=B=1/4$, not $1/2$.
- id: p6-chain-d
  content: |-
    $\displaystyle\frac14\ln|(2-\cos t)(2+\cos t)|+C$
  feedback: |-
    A product inside the logarithm gives the two log terms the same sign. The derivatives of $2-v$ and $2+v$ have opposite signs, so partial-fraction integration produces a logarithmic ratio instead.
- id: p6-chain-e
  content: |-
    $\displaystyle\frac14\ln\left|\frac{2-\sin t}{2+\sin t}\right|+C$
  feedback: |-
    The denominator is a polynomial in $\cos t$, and the numerator is $-d(\cos t)$. Substituting sine would require a $\cos t\,dt$ numerator, so the final back-substitution must contain $\cos t$, not $\sin t$.
```

---

## Summary

When the denominator is a polynomial in $\cos x$ and the numerator supplies $\sin x\,dx$, use this checklist:

1. Set $u=\cos x$ and carry the sign from $du=-\sin x\,dx$.
2. Factor the polynomial in $u$ before writing any partial fractions.
3. Solve the partial-fraction coefficients, then integrate each linear denominator with its own chain-rule sign.
4. Back-substitute, keep absolute values in logarithms, and differentiate to verify.

For the assigned integral,

$$
\boxed{\int \frac{\sin x}{1-\cos^2x}\,dx
=\frac12\ln\left|\frac{1-\cos x}{1+\cos x}\right|+C.}
$$

The main trap is losing one of two minus signs: one comes from the $u$-substitution, and the other appears when integrating $1/(1-u)$.
