# Trigonometric Substitution for $\sqrt{x^2-a^2}/x$

## Table of Contents

- [Introduction](#introduction)
- [Choose the Secant Substitution](#choose-the-secant-substitution)
- [Convert Every Factor](#convert-every-factor)
- [Integrate the Tangent Square](#integrate-the-tangent-square)
- [Return to the Original Variable](#return-to-the-original-variable)
- [Verify the Antiderivative](#verify-the-antiderivative)
- [Summary](#summary)

## Prerequisites

- The identity $1+\tan^2\theta=\sec^2\theta$
- The antiderivatives $\int \sec^2\theta\,d\theta=\tan\theta+C$ and $\int 1\,d\theta=\theta+C$
- Right-triangle definitions of secant and tangent

---

<a id="introduction"></a>
## Introduction

The expression

$$
\int \frac{\sqrt{x^2-25}}{x}\,dx
$$

contains the recognition cue $\sqrt{x^2-a^2}$ with $a=5$. Choose $x=a\sec\theta$ so that the difference of squares becomes a tangent square. Then rewrite every factor, integrate in $\theta$, and convert the result completely back to $x$.

The whole route is

$$
\sqrt{x^2-a^2}
\xrightarrow{x=a\sec\theta}
a\tan\theta,
\qquad
\int\frac{\sqrt{x^2-a^2}}{x}\,dx
\longrightarrow
a\int\tan^2\theta\,d\theta
\longrightarrow
a(\tan\theta-\theta)+C.
$$

Because the integrand is real on the two domain components $x\le -5$ and $x\ge 5$, an indefinite integral is handled on one interval at a time. We first carry out the substitution on $x>5$, then write a final form that differentiates correctly on both open intervals.

---

<a id="choose-the-secant-substitution"></a>
## Choose the Secant Substitution

**Example:** Choose a substitution for $\sqrt{x^2-25}$.

**Explanation**

Set

$$
x=5\sec\theta.
$$

On the positive branch, take $0\le\theta<\pi/2$. Then

$$
\begin{aligned}
x^2-25
&=25\sec^2\theta-25\\
&=25(\sec^2\theta-1)\\
&=25\tan^2\theta,
\end{aligned}
$$

so

$$
\sqrt{x^2-25}=5\tan\theta.
$$

A complete change of variables leaves no $x$ or $dx$ in the transformed integral.

This is why secant, rather than sine or tangent, is the useful substitution for a radical of the form $\sqrt{x^2-a^2}$.

```quiz
type: radio
id: p2-substitution-cue
content: |-
  Which substitution directly turns $\sqrt{x^2-36}$ into a constant multiple of $\tan\theta$?
options:
- id: sec-six
  content: |-
    $x=6\sec\theta$
  correct: true
  feedback: |-
    The radical has the pattern $\sqrt{x^2-a^2}$ with $a=6$. Substituting $x=6\sec\theta$ gives $\sqrt{36(\sec^2\theta-1)}=6\tan\theta$ on the standard positive-branch angle interval.
- id: tan-six
  content: |-
    $x=6\tan\theta$
  feedback: |-
    A tangent substitution naturally simplifies $a^2+x^2$, because $1+\tan^2\theta=\sec^2\theta$. Here the minus sign requires $\sec^2\theta-1=\tan^2\theta$, so use $x=6\sec\theta$.
- id: sin-six
  content: |-
    $x=6\sin\theta$
  feedback: |-
    A sine substitution fits $\sqrt{a^2-x^2}$ through $1-\sin^2\theta=\cos^2\theta$. The order here is $x^2-a^2$, so $x=6\sec\theta$ matches the radicand.
- id: sec-thirty-six
  content: |-
    $x=36\sec\theta$
  feedback: |-
    The scale $a$ is the square root of the constant term: $a=\sqrt{36}=6$. Using $36$ does not factor the radicand as $36(\sec^2\theta-1)$; use $x=6\sec\theta$.
- id: sec-scaled-angle
  content: |-
    $x=\sec(6\theta)$
  feedback: |-
    The constant $6$ must scale the secant value, not its angle. Only $x=6\sec\theta$ makes $x^2-36=36(\sec^2\theta-1)$.
```

---

<a id="convert-every-factor"></a>
## Convert Every Factor

**Example:** Rewrite the assigned integral using $x=5\sec\theta$.

**Explanation**

Differentiate the substitution and record all three replacements:

$$
x=5\sec\theta,
\qquad
dx=5\sec\theta\tan\theta\,d\theta,
\qquad
\sqrt{x^2-25}=5\tan\theta.
$$

Now substitute into the entire integrand:

$$
\begin{aligned}
\int \frac{\sqrt{x^2-25}}{x}\,dx
&=\int
\frac{5\tan\theta}{5\sec\theta}
\left(5\sec\theta\tan\theta\right)d\theta\\
&=5\int \tan^2\theta\,d\theta.
\end{aligned}
$$

The secant factor from $dx$ cancels the secant in the denominator. One tangent comes from the radical and the other comes from $dx$.

```quiz
type: radio
id: p2-convert-factors
content: |-
  With $x=3\sec\theta$, which integral is equivalent to $\displaystyle\int\frac{\sqrt{x^2-9}}{x}\,dx$?
options:
- id: three-tan-squared
  content: |-
    $\displaystyle 3\int\tan^2\theta\,d\theta$
  correct: true
  feedback: |-
    Here $\sqrt{x^2-9}=3\tan\theta$, $dx=3\sec\theta\tan\theta\,d\theta$, and $x=3\sec\theta$. Substitution and cancellation leave $3\int\tan^2\theta\,d\theta$.
- id: tan-squared
  content: |-
    $\displaystyle \int\tan^2\theta\,d\theta$
  feedback: |-
    The secant factors cancel, but one factor of $3$ remains: $(3\tan)/(3\sec)$ times $(3\sec\tan)$ equals $3\tan^2$. Keep that surviving scale factor.
- id: nine-tan-squared
  content: |-
    $\displaystyle 9\int\tan^2\theta\,d\theta$
  feedback: |-
    Multiplying the two factors of $3$ from the radical and $dx$ gives $9$, but the denominator $x=3\sec\theta$ cancels one factor of $3$ along with the secant. The remaining coefficient is $3$.
- id: three-sec-squared
  content: |-
    $\displaystyle 3\int\sec^2\theta\,d\theta$
  feedback: |-
    The radical supplies $\tan\theta$, not $\sec\theta$, and $dx$ supplies another tangent. After the secants cancel, the power is $\tan^2\theta$.
- id: three-sec-tan
  content: |-
    $\displaystyle 3\int\sec\theta\tan\theta\,d\theta$
  feedback: |-
    This keeps the secant from $dx$ but overlooks its cancellation with the denominator $x=3\sec\theta$. The two tangent factors remain, giving $3\tan^2\theta$.
```

---

<a id="integrate-the-tangent-square"></a>
## Integrate the Tangent Square

**Example:** Evaluate the transformed integral $5\int\tan^2\theta\,d\theta$.

**Explanation**

There is no basic antiderivative rule that sends $\tan^2\theta$ directly to $\tan\theta$. Select the identity containing $\tan^2\theta$, then solve that identity for the exact power appearing in the integral:

$$
1+\tan^2\theta=\sec^2\theta
\qquad\Longrightarrow\qquad
\tan^2\theta=\sec^2\theta-1.
$$

Therefore,

$$
\begin{aligned}
5\int\tan^2\theta\,d\theta
&=5\int(\sec^2\theta-1)\,d\theta\\
&=5\tan\theta-5\theta+C.
\end{aligned}
$$

```quiz
type: radio
id: p2-integrate-tan-square
content: |-
  What is $\displaystyle 4\int\tan^2\theta\,d\theta$?
options:
- id: tan-minus-theta
  content: |-
    $4\tan\theta-4\theta+C$
  correct: true
  feedback: |-
    Use $\tan^2\theta=\sec^2\theta-1$. Integrating both terms and keeping the factor $4$ gives $4(\tan\theta-\theta)+C=4\tan\theta-4\theta+C$.
- id: tan-only
  content: |-
    $4\tan\theta+C$
  feedback: |-
    This treats $\tan^2\theta$ as though it were $\sec^2\theta$. Since $\tan^2\theta=\sec^2\theta-1$, integrating the missing $-1$ contributes the required term $-4\theta$.
- id: sec-minus-theta
  content: |-
    $4\sec\theta-4\theta+C$
  feedback: |-
    The antiderivative of $\sec^2\theta$ is $\tan\theta$, whereas $\sec\theta$ differentiates to $\sec\theta\tan\theta$. After rewriting, the first term must be $4\tan\theta$.
- id: tan-plus-theta
  content: |-
    $4\tan\theta+4\theta+C$
  feedback: |-
    Rearranging $1+\tan^2\theta=\sec^2\theta$ gives $\tan^2\theta=\sec^2\theta-1$, not $\sec^2\theta+1$. The constant term therefore integrates to $-4\theta$.
- id: missing-four
  content: |-
    $\tan\theta-\theta+C$
  feedback: |-
    The identity and antiderivatives are correct here, but the outside factor $4$ must multiply both terms. The result is $4\tan\theta-4\theta+C$.
```

---

<a id="return-to-the-original-variable"></a>
## Return to the Original Variable

**Example:** Convert $5\tan\theta-5\theta+C$ back to $x$.

**Explanation**

From $x=5\sec\theta$, we have $\sec\theta=x/5$. A right triangle on the positive branch can use adjacent side $5$, hypotenuse $x$, and opposite side $\sqrt{x^2-25}$. Hence

$$
\tan\theta=\frac{\sqrt{x^2-25}}{5},
\qquad
5\tan\theta=\sqrt{x^2-25}.
$$

Also, $\theta=\operatorname{arcsec}(x/5)$ on $x>5$. Equivalently on that interval,

$$
\theta=\arctan\left(\frac{\sqrt{x^2-25}}{5}\right).
$$

Because antiderivatives are considered separately on the two disconnected domain intervals, replacing the inverse-secant argument by $|x|/5$ gives one formula whose derivative works on both intervals.

```quiz
type: radio
id: p2-triangle-back-substitution
content: |-
  On the interval $x>7$, suppose $x=7\sec\theta$. Which pair correctly converts both terms of $7\tan\theta-7\theta$ back to $x$?
options:
- id: p2-triangle-correct-pair
  content: |-
    $7\tan\theta=\sqrt{x^2-49}$ and $\theta=\operatorname{arcsec}(x/7)$
  correct: true
  feedback: |-
    Since $\sec\theta=x/7$, a right triangle has adjacent side $7$, hypotenuse $x$, and opposite side $\sqrt{x^2-49}$. Thus $7\tan\theta=\sqrt{x^2-49}$ and the substitution itself gives $\theta=\operatorname{arcsec}(x/7)$.
- id: p2-triangle-extra-seven
  content: |-
    $7\tan\theta=7\sqrt{x^2-49}$ and $\theta=\operatorname{arcsec}(x/7)$
  feedback: |-
    The triangle gives $\tan\theta=\sqrt{x^2-49}/7$. Multiplying by $7$ cancels that denominator, so $7\tan\theta$ is one radical, not seven radicals.
- id: p2-triangle-inverted-arcsec
  content: |-
    $7\tan\theta=\sqrt{x^2-49}$ and $\theta=\operatorname{arcsec}(7/x)$
  feedback: |-
    From $x=7\sec\theta$, divide by $7$ to get $\sec\theta=x/7$. The ratio $7/x$ is $\cos\theta$, so the inverse-secant argument must be $x/7$.
- id: p2-triangle-reciprocal-tangent
  content: |-
    $7\tan\theta=\sqrt{x^2-49}$ and $\theta=\arctan\left(7/\sqrt{x^2-49}\right)$
  feedback: |-
    The ratio $7/\sqrt{x^2-49}$ is adjacent over opposite, so it is $\cot\theta$. Tangent is opposite over adjacent, giving $\theta=\arctan(\sqrt{x^2-49}/7)$.
- id: p2-triangle-plus-radical
  content: |-
    $7\tan\theta=\sqrt{x^2+49}$ and $\theta=\operatorname{arcsec}(x/7)$
  feedback: |-
    The right triangle satisfies $x^2=7^2+(\text{opposite})^2$, so the opposite side is $\sqrt{x^2-49}$. The plus sign would not satisfy the Pythagorean relation.
```

Thus the assigned integral is

$$
\boxed{
\int \frac{\sqrt{x^2-25}}{x}\,dx
=\sqrt{x^2-25}
-5\operatorname{arcsec}\left(\frac{|x|}{5}\right)+C
}.
$$

```quiz
type: radio
id: p2-back-substitution
content: |-
  An identical calculation with $x=4\sec\theta$ ends at $4\tan\theta-4\theta+C$. Which branch-safe expression is entirely in terms of $x$?
options:
- id: correct-branch-safe
  content: |-
    $\sqrt{x^2-16}-4\operatorname{arcsec}\left(\dfrac{|x|}{4}\right)+C$
  correct: true
  feedback: |-
    The triangle gives $4\tan\theta=\sqrt{x^2-16}$. Using $\theta=\operatorname{arcsec}(|x|/4)$ preserves the derivative on both $x>4$ and $x<-4$, so the full expression is branch-safe.
- id: missing-absolute
  content: |-
    $\sqrt{x^2-16}-4\operatorname{arcsec}\left(\dfrac{x}{4}\right)+C$
  feedback: |-
    This matches the positive branch $x>4$, but the standard derivative of arcsec contains an absolute value and this form does not produce the integrand on $x<-4$. Use $|x|/4$ for a single expression covering both components.
- id: wrong-sign
  content: |-
    $\sqrt{x^2-16}+4\operatorname{arcsec}\left(\dfrac{|x|}{4}\right)+C$
  feedback: |-
    The transformed antiderivative is $4\tan\theta-4\theta$, so the inverse-secant term keeps a minus sign. Changing it to plus makes its derivative add instead of canceling the extra radical derivative term.
- id: scaled-radical
  content: |-
    $4\sqrt{x^2-16}-4\operatorname{arcsec}\left(\dfrac{|x|}{4}\right)+C$
  feedback: |-
    Since $\tan\theta=\sqrt{x^2-16}/4$, the product $4\tan\theta$ equals one copy of the radical, not four copies. Only the inverse-secant term retains coefficient $4$.
- id: missing-angle-scale
  content: |-
    $\sqrt{x^2-16}-\operatorname{arcsec}\left(\dfrac{|x|}{4}\right)+C$
  feedback: |-
    Replacing $\theta$ by an inverse secant does not remove its coefficient. The term $-4\theta$ becomes $-4\operatorname{arcsec}(|x|/4)$.
```

---

<a id="verify-the-antiderivative"></a>
## Verify the Antiderivative

**Example:** Differentiate the final answer.

**Explanation**

Let $R=\sqrt{x^2-25}$. On either open domain interval, $|x|>5$,

$$
\frac{d}{dx}R=\frac{x}{R}
$$

and

$$
\frac{d}{dx}\left[5\operatorname{arcsec}\left(\frac{|x|}{5}\right)\right]
=\frac{25}{xR}.
$$

Therefore,

$$
\begin{aligned}
\frac{d}{dx}\left[R-5\operatorname{arcsec}\left(\frac{|x|}{5}\right)\right]
&=\frac{x}{R}-\frac{25}{xR}\\
&=\frac{x^2-25}{xR}\\
&=\frac{R}{x}\\
&=\frac{\sqrt{x^2-25}}{x}.
\end{aligned}
$$

Differentiation recovers the original integrand, including its sign on the negative domain component.

```quiz
type: radio
id: p2-derivative-check
content: |-
  For $|x|>a>0$, let $R=\sqrt{x^2-a^2}$ and $F(x)=R-a\operatorname{arcsec}(|x|/a)$. Which derivative confirms the antiderivative pattern?
options:
- id: radical-over-x
  content: |-
    $F'(x)=\dfrac{R}{x}$
  correct: true
  feedback: |-
    Differentiation gives $F'(x)=x/R-a^2/(xR)=(x^2-a^2)/(xR)=R/x$. Since $R=\sqrt{x^2-a^2}$, this exactly reproduces the target integrand.
- id: x-over-radical
  content: |-
    $F'(x)=\dfrac{x}{R}$
  feedback: |-
    The derivative $x/R$ comes only from the radical. The inverse-secant term contributes $-a^2/(xR)$, and combining the two terms simplifies to $R/x$.
- id: radical-over-absolute-x
  content: |-
    $F'(x)=\dfrac{R}{|x|}$
  feedback: |-
    The absolute value belongs inside the inverse-secant argument to handle both branches, but the original denominator is still $x$. Its sign must remain, so the derivative is $R/x$, not $R/|x|$.
- id: plus-correction
  content: |-
    $F'(x)=\dfrac{x}{R}+\dfrac{a^2}{xR}$
  feedback: |-
    The inverse-secant term is subtracted in $F$, so its derivative contributes $-a^2/(xR)$. The minus sign is what changes $x^2$ to $x^2-a^2$ in the numerator.
- id: reciprocal-target
  content: |-
    $F'(x)=\dfrac{x}{R^2}$
  feedback: |-
    Combining the derivative terms uses the common denominator $xR$, not $R^2$. Since $x^2-a^2=R^2$, the result is $R^2/(xR)=R/x$.
```

---

<a id="summary"></a>
## Summary

For an integral of the form

$$
\int\frac{\sqrt{x^2-a^2}}{x}\,dx,
$$

use this checklist:

1. Recognize $\sqrt{x^2-a^2}$ and set $x=a\sec\theta$.
2. Replace the radical, denominator, and differential: $\sqrt{x^2-a^2}=a\tan\theta$ and $dx=a\sec\theta\tan\theta\,d\theta$.
3. Cancel before integrating to obtain $a\int\tan^2\theta\,d\theta$.
4. Rewrite $\tan^2\theta=\sec^2\theta-1$, giving $a\tan\theta-a\theta+C$.
5. Back-substitute both terms, using a right triangle for $a\tan\theta$ and an inverse trigonometric function for $\theta$.

The main traps are dropping the $-1$ in $\tan^2\theta=\sec^2\theta-1$, stopping while $\theta$ remains, and forgetting the branch issue. As a final check, differentiate: the result must simplify to $\sqrt{x^2-a^2}/x$, including the denominator's sign.

In branch-safe form,

$$
\int\frac{\sqrt{x^2-a^2}}{x}\,dx
=\sqrt{x^2-a^2}
-a\operatorname{arcsec}\left(\frac{|x|}{a}\right)+C,
\qquad |x|>a.
$$
