# Approximating a Constant by Combining Gregory Partial Sums

## Table of Contents

- [Introduction](#introduction)
- [Write the Requested Gregory Partial Sum](#write-the-requested-gregory-partial-sum)
- [Evaluate Each Input Exactly](#evaluate-each-input-exactly)
- [Apply the Identity to the Partial Sums](#apply-the-identity-to-the-partial-sums)
- [Combine the Fractions and Scale](#combine-the-fractions-and-scale)
- [Avoid the Two Main Traps](#avoid-the-two-main-traps)

## Prerequisites

- Substituting rational numbers into a polynomial
- Evaluating positive integer powers of fractions
- Adding and reducing exact fractions
- Interpreting the first $N$ terms of a series as a partial sum

---

<a id="introduction"></a>
## Introduction

When a problem gives an identity that rewrites a difficult constant using function values at smaller inputs, approximate each function value with the **same requested partial sum**, combine those partial sums according to the identity, and simplify only with exact arithmetic.

**Recognition cue:** the prompt supplies both a function identity and a requested number of terms from a known series. That means the identity tells you how to combine partial sums; it does not change how many terms belong in each one.

Gregory's series is

$$
\tan^{-1}(x)
=x-\frac{x^3}{3}+\frac{x^5}{5}-\frac{x^7}{7}+\cdots
=\sum_{k=0}^{\infty}(-1)^k\frac{x^{2k+1}}{2k+1}.
$$

Its first four terms form the partial sum

$$
S_4(x)=x-\frac{x^3}{3}+\frac{x^5}{5}-\frac{x^7}{7}.
$$

The reusable procedure is:

1. Write $S_4(x)$ before substituting.
2. Evaluate $S_4$ at every input in the given identity.
3. Replace each inverse tangent by its partial-sum value.
4. Apply any factor outside the identity to the entire combined result.
5. Reduce the final fraction.

---

<a id="write-the-requested-gregory-partial-sum"></a>
## Write the Requested Gregory Partial Sum

**Example:** Write the first four terms of Gregory's series evaluated at $x=\dfrac{2}{5}$.

**Explanation**

The summation begins at $k=0$, so four terms correspond to $k=0,1,2,3$. Substitute $x=\dfrac25$ into all four terms of $S_4(x)$:

$$
S_4\!\left(\frac25\right)
=\frac25-\frac{(2/5)^3}{3}+\frac{(2/5)^5}{5}-\frac{(2/5)^7}{7}.
$$

The signs alternate $+,-,+,-$, the powers are $1,3,5,7$, and the denominators match those odd powers.

Although $S_4(x)$ has degree $7$, it contains four nonzero terms. The subscript counts terms, not the highest exponent.

```quiz
type: radio
id: ohw10-p15-q1
content: |-
  Which expression is the first four-term Gregory partial sum $S_4(x)$?
options:
- id: a
  content: |-
    $x-\dfrac{x^2}{2}+\dfrac{x^3}{3}-\dfrac{x^4}{4}$
- id: b
  content: |-
    $x-\dfrac{x^3}{3}+\dfrac{x^5}{5}-\dfrac{x^7}{7}$
  correct: true
- id: c
  content: |-
    $x+\dfrac{x^3}{3}+\dfrac{x^5}{5}+\dfrac{x^7}{7}$
- id: d
  content: |-
    $1-x+\dfrac{x^3}{3}-\dfrac{x^5}{5}$
- id: e
  content: |-
    $x-\dfrac{x^3}{3}+\dfrac{x^5}{5}-\dfrac{x^7}{7}+\dfrac{x^9}{9}$
```

---

<a id="evaluate-each-input-exactly"></a>
## Evaluate Each Input Exactly

**Example:** Evaluate $S_4\!\left(\dfrac12\right)$ as an exact fraction.

**Explanation**

Substitute first, then simplify one term at a time:

$$
\begin{aligned}
S_4\!\left(\frac12\right)
&=\frac12-\frac{(1/2)^3}{3}+\frac{(1/2)^5}{5}-\frac{(1/2)^7}{7}\\
&=\frac12-\frac1{24}+\frac1{160}-\frac1{896}\\
&=\frac{6229}{13440}.
\end{aligned}
$$

Keeping the expression fractional prevents rounding error from entering before the two approximations are combined.

```quiz
type: radio
id: ohw10-p15-q2
content: |-
  Evaluate $S_4\!\left(\dfrac13\right)$ exactly.
options:
- id: a
  content: |-
    $\dfrac{24628}{76545}$
  correct: true
- id: b
  content: |-
    $\dfrac{391}{1215}$
- id: c
  content: |-
    $\dfrac{25515}{76545}$
- id: d
  content: |-
    $\dfrac{26428}{76545}$
- id: e
  content: |-
    $\dfrac{24633}{76545}$
```

---

<a id="apply-the-identity-to-the-partial-sums"></a>
## Apply the Identity to the Partial Sums

**Example:** Use

$$
\tan^{-1}(1)=\tan^{-1}\!\left(\frac12\right)+\tan^{-1}\!\left(\frac13\right)
$$

to set up a four-term approximation of $\pi$.

**Explanation**

Because $\tan^{-1}(1)=\dfrac{\pi}{4}$, multiply the entire identity by $4$:

$$
\pi=4\left[\tan^{-1}\!\left(\frac12\right)+\tan^{-1}\!\left(\frac13\right)\right].
$$

Now replace both inverse tangent values by the same four-term Gregory partial sum:

$$
\pi\approx4\left[S_4\!\left(\frac12\right)+S_4\!\left(\frac13\right)\right].
$$

The factor $4$ applies to the sum of both partial-sum values.

```quiz
type: radio
id: ohw10-p15-q3
content: |-
  Given $\dfrac{\pi}{4}=\tan^{-1}\!\left(\dfrac12\right)+\tan^{-1}\!\left(\dfrac13\right)$, which expression correctly uses four terms of Gregory's series to approximate $\pi$?
options:
- id: a
  content: |-
    $S_4\!\left(\dfrac12\right)+S_4\!\left(\dfrac13\right)$
- id: b
  content: |-
    $4S_4\!\left(\dfrac12\right)+S_4\!\left(\dfrac13\right)$
- id: c
  content: |-
    $4\left[S_4\!\left(\dfrac12\right)+S_4\!\left(\dfrac13\right)\right]$
  correct: true
- id: d
  content: |-
    $\dfrac14\left[S_4\!\left(\dfrac12\right)+S_4\!\left(\dfrac13\right)\right]$
- id: e
  content: |-
    $4\left[S_4\!\left(\dfrac12\right)-S_4\!\left(\dfrac13\right)\right]$
```

---

<a id="combine-the-fractions-and-scale"></a>
## Combine the Fractions and Scale

**Example:** Finish the exact approximation using

$$
S_4\!\left(\frac12\right)=\frac{6229}{13440}
\qquad\text{and}\qquad
S_4\!\left(\frac13\right)=\frac{24628}{76545}.
$$

**Explanation**

Add the two fractions before applying the outer factor:

$$
\begin{aligned}
S_4\!\left(\frac12\right)+S_4\!\left(\frac13\right)
&=\frac{6229}{13440}+\frac{24628}{76545}\\
&=\frac{4540941}{9797760}+\frac{3152384}{9797760}\\
&=\frac{7693325}{9797760}\\
&=\frac{1538665}{1959552}.
\end{aligned}
$$

Then scale the entire sum by $4$ and reduce:

$$
\pi\approx4\left(\frac{1538665}{1959552}\right)
=\boxed{\frac{1538665}{489888}}.
$$

The decimal value $3.140850\ldots$ is useful as a reasonableness check, but the requested answer remains the exact fraction. Because each four-term alternating partial sum ends with a negative term of decreasing magnitude, the approximation should lie slightly below the true value of $\pi$; it does.

```quiz
type: radio
id: ohw10-p15-q4
content: |-
  Suppose $C=3[\tan^{-1}(p)+\tan^{-1}(q)]$, and a chosen partial sum gives $S(p)=\dfrac{7}{15}$ and $S(q)=\dfrac{2}{9}$. What exact fraction approximates $C$?
options:
- id: a
  content: |-
    $\dfrac{31}{45}$
- id: b
  content: |-
    $\dfrac{31}{15}$
  correct: true
- id: c
  content: |-
    $\dfrac{11}{15}$
- id: d
  content: |-
    $\dfrac{31}{5}$
- id: e
  content: |-
    $\dfrac{7}{5}$
```

---

<a id="avoid-the-two-main-traps"></a>
## Avoid the Two Main Traps

**Example:** Explain why the last term of $S_4(x)$ is $-\dfrac{x^7}{7}$ rather than $+\dfrac{x^9}{9}$.

**Explanation**

Count terms from the beginning of the series:

$$
\underbrace{x}_{1\text{st}}
-\underbrace{\frac{x^3}{3}}_{2\text{nd}}
+\underbrace{\frac{x^5}{5}}_{3\text{rd}}
-\underbrace{\frac{x^7}{7}}_{4\text{th}}.
$$

The $x^9/9$ term would be the fifth term. A separate common error is to distribute the outside factor to only one of the two partial sums; brackets prevent that mistake.

```quiz
type: radio
id: ohw10-p15-q5
content: |-
  Which calculation correctly respects both “first four terms” and the outer factor in $K=5[\tan^{-1}(a)+\tan^{-1}(b)]$?
options:
- id: a
  content: |-
    $5S_5(a)+S_5(b)$
- id: b
  content: |-
    $5[S_4(a)+S_4(b)]$
  correct: true
- id: c
  content: |-
    $S_4(5a)+S_4(b)$
- id: d
  content: |-
    $5[S_3(a)+S_3(b)]$
- id: e
  content: |-
    $S_4(a)+S_4(b)+5$
```

---

## Summary

When an identity rewrites a constant using several inverse tangent values:

1. Translate “first four terms” into
   $$
   S_4(x)=x-\frac{x^3}{3}+\frac{x^5}{5}-\frac{x^7}{7}.
   $$
2. Evaluate $S_4$ separately at every given input using exact fractions.
3. Substitute those partial sums into the identity.
4. Apply any outside factor to the entire bracketed combination.
5. Reduce the result, using a decimal only as a final check.

The main traps are including five terms instead of four, breaking the alternating sign pattern, or applying the outside factor to only one partial sum.
