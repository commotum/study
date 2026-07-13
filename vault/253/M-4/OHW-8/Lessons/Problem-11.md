# Summing an Alternating Rational Series with the Arctangent Series

## Table of Contents

- [Introduction](#introduction)
- [Encode the Pattern](#encode-the-pattern)
- [Split the Adjacent Factors](#split-the-adjacent-factors)
- [Rewrite the Shifted Tail](#rewrite-the-shifted-tail)
- [Recognize the Arctangent Series](#recognize-the-arctangent-series)
- [Assemble the Exact Sum](#assemble-the-exact-sum)

## Prerequisites

- Write a patterned series in sigma notation.
- Decompose a rational expression with two distinct linear factors.
- Reindex a series by replacing $n$ with $m-1$.
- Use the exact value $\arctan(1)=\dfrac{\pi}{4}$.

---

<a id="introduction"></a>
## Introduction

Consider a series whose denominators contain consecutive odd factors:

$$
\frac{1}{1\cdot3}-\frac{1}{3\cdot5}+\frac{1}{5\cdot7}-\frac{1}{7\cdot9}+\cdots.
$$

The recognition cue is the pair $(2n+1)(2n+3)$ together with alternating signs. Decompose each coefficient into a difference of two odd reciprocals, rewrite the second reciprocal series as a shifted tail of the first, and then identify the first series as the Maclaurin series for $\arctan(1)$.

The signs matter: after reindexing, the shifted tail is $1-A$, not $A-1$.

---

<a id="encode-the-pattern"></a>
## Encode the Pattern

**Example:** Write the series from the introduction in sigma notation.

**Explanation**

Let the first term correspond to $n=0$. The alternating sign is $(-1)^n$, and the two denominator factors are $2n+1$ and $2n+3$. Thus

$$
S=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)(2n+3)}.
$$

A quick check with $n=0,1,2$ gives

$$
\frac{1}{1\cdot3},\qquad
-\frac{1}{3\cdot5},\qquad
+\frac{1}{5\cdot7},
$$

so the formula has the correct factors and signs.

```quiz
type: radio
id: ohw8-p11-q1
content: |-
  Which sigma notation represents

  $$
  \frac{1}{3\cdot5}-\frac{1}{5\cdot7}+\frac{1}{7\cdot9}-\cdots?
  $$
options:
- id: a
  content: |-
    $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+3)(2n+5)}$
  correct: true
- id: b
  content: |-
    $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^{n+1}}{(2n+3)(2n+5)}$
- id: c
  content: |-
    $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{(2n+3)(2n+5)}$
- id: d
  content: |-
    $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)(2n+3)}$
```

---

<a id="split-the-adjacent-factors"></a>
## Split the Adjacent Factors

**Example:** Decompose $\dfrac{1}{(2n+1)(2n+3)}$ into partial fractions.

**Explanation**

For any nonzero $u$ and $u+2$, the adjacent-factor identity is

$$
\frac{1}{u(u+2)}
=\frac12\left(\frac1u-\frac{1}{u+2}\right).
$$

Here $u=2n+1$. The factors differ by $2$, so subtracting their reciprocals produces a numerator of $2$:

$$
\frac{1}{2n+1}-\frac{1}{2n+3}
=\frac{(2n+3)-(2n+1)}{(2n+1)(2n+3)}
=\frac{2}{(2n+1)(2n+3)}.
$$

Therefore,

$$
\frac{1}{(2n+1)(2n+3)}
=\frac12\left(\frac{1}{2n+1}-\frac{1}{2n+3}\right).
$$

Applying this identity term by term gives

$$
S=\frac12\left[
\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}
-
\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+3}
\right].
$$

Both component series converge by the alternating series test, so the sum and constant-multiple rules justify this split.

```quiz
type: radio
id: ohw8-p11-q2
content: |-
  Which decomposition is correct?

  $$
  \frac{1}{(2n+3)(2n+5)}=\;?
  $$
options:
- id: a
  content: |-
    $\dfrac12\left(\dfrac{1}{2n+3}-\dfrac{1}{2n+5}\right)$
  correct: true
- id: b
  content: |-
    $\dfrac12\left(\dfrac{1}{2n+3}+\dfrac{1}{2n+5}\right)$
- id: c
  content: |-
    $2\left(\dfrac{1}{2n+3}-\dfrac{1}{2n+5}\right)$
- id: d
  content: |-
    $\dfrac{1}{2n+3}-\dfrac{1}{2n+5}$
```

---

<a id="rewrite-the-shifted-tail"></a>
## Rewrite the Shifted Tail

**Example:** Express the shifted series

$$
B=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+3}
$$

in terms of

$$
A=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}.
$$

**Explanation**

Writing out the first few terms makes the shift visible:

$$
A=1-\frac13+\frac15-\frac17+\cdots
$$

and

$$
B=\frac13-\frac15+\frac17-\cdots.
$$

The tail of $A$ after its leading $1$ is

$$
A-1=-\frac13+\frac15-\frac17+\cdots.
$$

This has the opposite sign from $B$, so

$$
B=-(A-1)=1-A.
$$

The same conclusion follows directly by setting $m=n+1$:

$$
\begin{aligned}
B
&=\sum_{m=1}^{\infty}\frac{(-1)^{m-1}}{2m+1} \\
&=-\sum_{m=1}^{\infty}\frac{(-1)^m}{2m+1} \\
&=-(A-1)=1-A.
\end{aligned}
$$

This sign reversal is the main trap. The split series do not telescope in the usual same-sign way.

```quiz
type: radio
id: ohw8-p11-q3
content: |-
  Let

  $$
  A=1-\frac13+\frac15-\frac17+\cdots
  $$

  and

  $$
  C=\frac15-\frac17+\frac19-\cdots.
  $$

  Which expression equals $C$?
options:
- id: a
  content: |-
    $A-\dfrac23$
  correct: true
- id: b
  content: |-
    $\dfrac23-A$
- id: c
  content: |-
    $1-A$
- id: d
  content: |-
    $A+\dfrac23$
```

---

<a id="recognize-the-arctangent-series"></a>
## Recognize the Arctangent Series

**Example:** Find the exact value of $A$.

**Explanation**

The Maclaurin series for arctangent is

$$
\arctan x
=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{2n+1}
=x-\frac{x^3}{3}+\frac{x^5}{5}-\frac{x^7}{7}+\cdots.
$$

At $x=1$, this becomes

$$
A=1-\frac13+\frac15-\frac17+\cdots
=\arctan(1)
=\frac{\pi}{4}.
$$

```quiz
type: radio
id: ohw8-p11-q4
content: |-
  What is the exact value of

  $$
  \sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}?
  $$
options:
- id: a
  content: |-
    $\dfrac{\pi}{2}$
- id: b
  content: |-
    $\dfrac{\pi}{4}$
  correct: true
- id: c
  content: |-
    $1-\dfrac{\pi}{4}$
- id: d
  content: |-
    $\ln 2$
```

---

<a id="assemble-the-exact-sum"></a>
## Assemble the Exact Sum

**Example:** Find the exact sum of

$$
\frac{1}{1\cdot3}-\frac{1}{3\cdot5}+\frac{1}{5\cdot7}-\frac{1}{7\cdot9}+\cdots.
$$

**Explanation**

From the partial-fraction split,

$$
S=\frac12(A-B).
$$

Using $B=1-A$ gives

$$
S=\frac12\bigl(A-(1-A)\bigr)
=A-\frac12.
$$

Finally, substitute $A=\dfrac{\pi}{4}$:

$$
\boxed{S=\frac{\pi}{4}-\frac12=\frac{\pi-2}{4}}.
$$

This is the exact sum of the original power series when $x=1$.

As a quick check,

$$
\frac{\pi-2}{4}\approx0.2854,
$$

which lies between the first two alternating partial sums $\dfrac13$ and $\dfrac13-\dfrac1{15}=\dfrac4{15}$.

```quiz
type: radio
id: ohw8-p11-q5
content: |-
  Use the same method to evaluate

  $$
  \frac{1}{3\cdot5}-\frac{1}{5\cdot7}+\frac{1}{7\cdot9}-\cdots.
  $$

  Which exact value is correct?
options:
- id: a
  content: |-
    $\dfrac{\pi}{4}-\dfrac12$
- id: b
  content: |-
    $\dfrac56-\dfrac{\pi}{4}$
  correct: true
- id: c
  content: |-
    $1-\dfrac{\pi}{4}$
- id: d
  content: |-
    $\dfrac{\pi}{4}-\dfrac16$
```

---

## Summary

When an alternating series contains adjacent odd factors $(2n+1)(2n+3)$:

1. Write the pattern with $(-1)^n$.
2. Split the coefficient:

   $$
   \frac{1}{(2n+1)(2n+3)}
   =\frac12\left(\frac{1}{2n+1}-\frac{1}{2n+3}\right).
   $$

3. Let $A=1-\dfrac13+\dfrac15-\cdots$ and rewrite the shifted series as $1-A$.
4. Use $A=\arctan(1)=\dfrac{\pi}{4}$.
5. Keep the sign reversal visible: the shifted tail is $1-A$, not $A-1$.

For the assigned series at $x=1$, the exact sum is

$$
\boxed{\frac{\pi-2}{4}}.
$$
