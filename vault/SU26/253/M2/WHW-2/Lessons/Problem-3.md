# Convergence and Sum of a Geometric Series in Sigma Notation

## Table of Contents

- [Introduction](#introduction)
- [Read the First Term and Common Ratio](#read-the-first-term-and-common-ratio)
- [Rewrite the Summand in Geometric Form](#rewrite-the-summand-in-geometric-form)
- [Test Convergence Before Summing](#test-convergence-before-summing)
- [Complete the Given Series](#complete-the-given-series)
- [Summary](#summary)

## Prerequisites

- Evaluate an expression at its starting index.
- Use exponent rules to separate a power from a product or quotient.
- Simplify fractions.

---

<a id="introduction"></a>
## Introduction

A series is geometric when each term is obtained by multiplying the previous term by the same number. In sigma notation, the useful target form is

$$
\sum_{n=1}^{\infty} a r^{n-1},
$$

where $a$ is the first term and $r$ is the common ratio. The recognition cue is an index $n$ appearing in an exponent. Rewrite the summand to expose $a$ and $r$, check whether $|r|<1$, and only then use

$$
S=\frac{a}{1-r}.
$$

---

<a id="read-the-first-term-and-common-ratio"></a>
## Read the First Term and Common Ratio

**Example:** Determine the first term and common ratio of

$$
\sum_{n=1}^{\infty} 4\left(\frac{2}{3}\right)^{n-1}.
$$

**Explanation**

The series already has the form $\sum a r^{n-1}$. Therefore,

$$
a=4
\qquad\text{and}\qquad
r=\frac{2}{3}.
$$

You can confirm the first term by substituting $n=1$: the exponent becomes $0$, so the first term is $4(2/3)^0=4$.

```quiz
type: radio
id: p3-read-a-r
content: |-
  For $\displaystyle \sum_{n=1}^{\infty} 7\left(-\frac{1}{4}\right)^{n-1}$, what are the first term $a$ and common ratio $r$?
options:
- id: p3-read-a-r-a
  content: |-
    $a=7$ and $r=-\frac14$
  correct: true
- id: p3-read-a-r-b
  content: |-
    $a=-\frac74$ and $r=-\frac14$
- id: p3-read-a-r-c
  content: |-
    $a=7$ and $r=\frac14$
- id: p3-read-a-r-d
  content: |-
    $a=1$ and $r=-\frac74$
- id: p3-read-a-r-e
  content: |-
    $a=-\frac14$ and $r=7$
```

---

<a id="rewrite-the-summand-in-geometric-form"></a>
## Rewrite the Summand in Geometric Form

**Example:** Rewrite the summand $\dfrac{3\cdot 2^{n-1}}{5^n}$ in the form $a r^{n-1}$.

**Explanation**

The numerator already contains the needed exponent $n-1$. Split one factor of $5$ from the denominator:

$$
5^n=5\cdot 5^{n-1}.
$$

Then group the powers with exponent $n-1$:

$$
\frac{3\cdot 2^{n-1}}{5^n}
=\frac{3\cdot 2^{n-1}}{5\cdot 5^{n-1}}
=\frac35\left(\frac25\right)^{n-1}.
$$

Thus $a=3/5$ and $r=2/5$. A quick check at $n=1$ confirms that the original first term is $3/5$.

```quiz
type: radio
id: p3-rewrite-form
content: |-
  Which expression correctly rewrites $\displaystyle \frac{4\cdot 3^{n-1}}{7^n}$ in the form $a r^{n-1}$?
options:
- id: p3-rewrite-form-a
  content: |-
    $\displaystyle \frac47\left(\frac37\right)^{n-1}$
  correct: true
- id: p3-rewrite-form-b
  content: |-
    $\displaystyle 4\left(\frac37\right)^{n-1}$
- id: p3-rewrite-form-c
  content: |-
    $\displaystyle \frac43\left(\frac37\right)^{n-1}$
- id: p3-rewrite-form-d
  content: |-
    $\displaystyle \frac47\left(\frac73\right)^{n-1}$
- id: p3-rewrite-form-e
  content: |-
    $\displaystyle \frac47\left(\frac37\right)^n$
```

---

<a id="test-convergence-before-summing"></a>
## Test Convergence Before Summing

**Example:** Determine whether

$$
\sum_{n=1}^{\infty} 5\left(-\frac34\right)^{n-1}
$$

converges, and find its sum if it does.

**Explanation**

The ratio is $r=-3/4$. Convergence depends on its absolute value:

$$
|r|=\frac34<1.
$$

The alternating signs do not prevent convergence. Since the convergence test passes,

$$
S=\frac{a}{1-r}
=\frac{5}{1-(-3/4)}
=\frac{5}{7/4}
=\frac{20}{7}.
$$

If $|r|\ge 1$, the series diverges and the sum formula must not be used.

```quiz
type: radio
id: p3-test-convergence
content: |-
  What is the correct conclusion for $\displaystyle \sum_{n=1}^{\infty} 2\left(-\frac54\right)^{n-1}$?
options:
- id: p3-test-convergence-a
  content: |-
    It diverges because $\left|-\frac54\right|>1$.
  correct: true
- id: p3-test-convergence-b
  content: |-
    It converges because the ratio is negative.
- id: p3-test-convergence-c
  content: |-
    It converges to $\frac89$.
- id: p3-test-convergence-d
  content: |-
    It diverges because every alternating series diverges.
- id: p3-test-convergence-e
  content: |-
    It converges to $\frac89$ by using $S=\frac{2}{1-(-5/4)}$.
```

---

<a id="complete-the-given-series"></a>
## Complete the Given Series

**Example:** Determine whether the series converges and, if so, find its sum:

$$
\sum_{n=1}^{\infty} \frac{2\cdot 5^{n-1}}{6^n}.
$$

**Explanation**

Split $6^n$ as $6\cdot 6^{n-1}$:

$$
\frac{2\cdot 5^{n-1}}{6^n}
=\frac{2\cdot 5^{n-1}}{6\cdot 6^{n-1}}
=\frac13\left(\frac56\right)^{n-1}.
$$

Therefore,

$$
a=\frac13,
\qquad
r=\frac56.
$$

Checking consecutive terms confirms both values:

$$
a_1=\frac13,
\qquad
a_2=\frac{5}{18},
\qquad
\frac{a_2}{a_1}
=\frac{5/18}{1/3}
=\frac56.
$$

Because $|r|=5/6<1$, the series converges. Its sum is

$$
S=\frac{a}{1-r}
=\frac{1/3}{1-5/6}
=\frac{1/3}{1/6}
=2.
$$

```quiz
type: radio
id: p3-complete-series
content: |-
  Determine whether $\displaystyle \sum_{n=1}^{\infty}\frac{3\cdot 4^{n-1}}{5^n}$ converges and, if so, find its sum.
options:
- id: p3-complete-series-a
  content: |-
    It converges to $3$.
  correct: true
- id: p3-complete-series-b
  content: |-
    It converges to $15$.
- id: p3-complete-series-c
  content: |-
    It converges to $\frac35$.
- id: p3-complete-series-d
  content: |-
    It diverges because $4^{n-1}$ grows.
- id: p3-complete-series-e
  content: |-
    It diverges because $r=\frac54>1$.
```

---

<a id="summary"></a>
## Summary

When the index appears in an exponent, try to expose the geometric form $a r^{n-1}$.

1. Rewrite powers so every repeated factor has exponent $n-1$.
2. Identify $a$ by evaluating the term at the starting index and identify the common ratio $r$.
3. Test convergence: the series converges exactly when $|r|<1$.
4. Only after the test passes, compute $S=a/(1-r)$.

The main trap is losing the extra denominator factor when changing $b^n$ into $b\cdot b^{n-1}$. For the given series, that factor makes $a=1/3$, not $2$.
