# Evaluating Claims About Infinite-Series Properties

## Table of Contents

- [Introduction](#introduction)
- [Read a Theorem in Its Guaranteed Direction](#read-a-theorem-in-its-guaranteed-direction)
- [Reject a False Converse With a Counterexample](#reject-a-false-converse-with-a-counterexample)
- [Separate a Finite Prefix From the Infinite Tail](#separate-a-finite-prefix-from-the-infinite-tail)
- [Use Terms and Partial Sums to Detect Divergence](#use-terms-and-partial-sums-to-detect-divergence)
- [Apply the Checklist to a Mixed Set of Claims](#apply-the-checklist-to-a-mixed-set-of-claims)
- [Summary](#summary)

## Prerequisites

- [[Infinite Series and Partial Sums - 981]]
- [[Convergent and Divergent Infinite Series - 982]]
- [[Properties of Infinite Series - 983]]
- [[Further Properties of Infinite Series - 4052]]
- [[The Nth Term Test for Divergence - 743]]

---

<a id="introduction"></a>
## Introduction

When a problem asks which statements about infinite series are true, treat every statement as a separate implication:

1. Identify exactly what is given.
2. Identify what the statement claims must follow.
3. Match that direction to a valid theorem.
4. If the direction is not a theorem, try to build one counterexample.

The key word is **must**. A universal claim is false as soon as one example satisfies its hypothesis but not its conclusion.

The most common trap is reversing a valid theorem. For example, if both $\sum a_k$ and $\sum b_k$ converge, then $\sum(a_k+b_k)$ converges. This does not automatically make the converse true.

---

<a id="read-a-theorem-in-its-guaranteed-direction"></a>
## Read a Theorem in Its Guaranteed Direction

For convergent series, linearity says that if

$$
\sum_{k=1}^{\infty}a_k=A
\qquad\text{and}\qquad
\sum_{k=1}^{\infty}b_k=B,
$$

then, for constants $r$ and $s$,

$$
\sum_{k=1}^{\infty}(ra_k+sb_k)=rA+sB.
$$

The hypotheses come first: the component series must be known to converge. A constant multiple therefore preserves convergence, and its sum is multiplied by the same constant.

**Example:** Suppose $\sum a_k=4$. Determine whether

$$
\sum_{k=1}^{\infty}(-3a_k)=-12
$$

is guaranteed.

**Explanation**

Yes. The given component series converges, so the constant-multiple rule applies directly:

$$
\sum_{k=1}^{\infty}(-3a_k)
=-3\sum_{k=1}^{\infty}a_k
=-3(4)
=-12.
$$

```quiz
type: radio
id: ohw4-p1-linearity
content: |-
  Suppose $\displaystyle\sum_{k=1}^{\infty}u_k=2$ and $\displaystyle\sum_{k=1}^{\infty}v_k=-5$. Which conclusion is guaranteed?
options:
- id: a
  content: |-
    $\displaystyle\sum_{k=1}^{\infty}(3u_k-2v_k)=4$
- id: b
  content: |-
    $\displaystyle\sum_{k=1}^{\infty}(3u_k-2v_k)=16$
  correct: true
- id: c
  content: |-
    $\displaystyle\sum_{k=1}^{\infty}(3u_k-2v_k)=-4$
- id: d
  content: |-
    The combined series must diverge because one given sum is negative.
- id: e
  content: |-
    There is not enough information because $u_k$ and $v_k$ are not given explicitly.
```

---

<a id="reject-a-false-converse-with-a-counterexample"></a>
## Reject a False Converse With a Counterexample

The valid sum rule is

$$
\left(\sum a_k\text{ converges and }\sum b_k\text{ converges}\right)
\Longrightarrow
\sum(a_k+b_k)\text{ converges}.
$$

Reversing the arrow gives a different claim. To test that converse, look for **cancellation** between two divergent component series.

**Example:** Decide whether convergence of $\sum(a_k+b_k)$ forces both $\sum a_k$ and $\sum b_k$ to converge.

**Explanation**

Let

$$
a_k=1
\qquad\text{and}\qquad
b_k=-1.
$$

Then $a_k+b_k=0$, so

$$
\sum_{k=1}^{\infty}(a_k+b_k)=\sum_{k=1}^{\infty}0=0
$$

converges. However, the partial sums of $\sum a_k$ are $1,2,3,\ldots$, and the partial sums of $\sum b_k$ are $-1,-2,-3,\ldots$. Both component series diverge.

Thus the combined series can converge because divergent pieces cancel. The converse is false.

```quiz
type: radio
id: ohw4-p1-counterexample
content: |-
  Which choice is a counterexample to the claim “If $\sum(x_k+y_k)$ converges, then both $\sum x_k$ and $\sum y_k$ converge”?
options:
- id: a
  content: |-
    $x_k=2^{-k}$ and $y_k=3^{-k}$
- id: b
  content: |-
    $x_k=2$ and $y_k=-2$
  correct: true
- id: c
  content: |-
    $x_k=2$ and $y_k=2$
- id: d
  content: |-
    $x_k=0$ and $y_k=1/k$
- id: e
  content: |-
    $x_k=0$ and $y_k=(-1)^k$
```

---

<a id="separate-a-finite-prefix-from-the-infinite-tail"></a>
## Separate a Finite Prefix From the Infinite Tail

Changing, adding, or removing finitely many terms changes a series by only a finite amount. It can change the value of a convergent sum, but it cannot change whether the series converges.

**Example:** Two series have different terms for $1\le k\le100$ but have identical terms for every $k\ge101$. Must they have the same convergence behavior?

**Explanation**

Write each series as

$$
\text{finite prefix}+\sum_{k=101}^{\infty}t_k.
$$

Their infinite tails are identical. Each finite prefix is an ordinary finite number, so either both full series converge or both diverge. If they converge, their sums need not be equal because their finite prefixes may have different sums.

```quiz
type: radio
id: ohw4-p1-finite-prefix
content: |-
  Series $P$ and $Q$ may differ in their first $50$ terms, but their terms agree from the $51$st term onward. Which statement is guaranteed?
options:
- id: a
  content: |-
    $P$ and $Q$ have equal sums.
- id: b
  content: |-
    $P$ converges exactly when $Q$ converges.
  correct: true
- id: c
  content: |-
    Both series converge because their tails agree.
- id: d
  content: |-
    Both series diverge because their first $50$ terms differ.
- id: e
  content: |-
    The first $50$ terms alone determine convergence.
```

---

<a id="use-terms-and-partial-sums-to-detect-divergence"></a>
## Use Terms and Partial Sums to Detect Divergence

Two quick checks settle many claims:

- If the terms $a_k$ do not approach $0$, then $\sum a_k$ diverges.
- If $a_k>0$, then the partial sums increase. An unbounded increasing sequence of partial sums cannot approach a finite limit, so the series diverges to $+\infty$.

These are one-way tests. Terms approaching $0$ do not by themselves guarantee convergence.

**Example:** Determine whether $\sum_{k=1}^{\infty}k^3$ converges.

**Explanation**

Its terms do not approach $0$:

$$
\lim_{k\to\infty}k^3=\infty.
$$

Therefore, the series diverges. Equivalently, its positive partial sums are increasing and unbounded.

```quiz
type: radio
id: ohw4-p1-partial-sums
content: |-
  A series has $a_k>0$ for every $k$, and its sequence of partial sums is unbounded. What must be true?
options:
- id: a
  content: |-
    The series converges because all terms are positive.
- id: b
  content: |-
    The series could converge or diverge.
- id: c
  content: |-
    The series diverges to $+\infty$.
  correct: true
- id: d
  content: |-
    The series oscillates.
- id: e
  content: |-
    The terms must eventually be negative.
```

---

<a id="apply-the-checklist-to-a-mixed-set-of-claims"></a>
## Apply the Checklist to a Mixed Set of Claims

**Example:** Apply the theorem-direction and counterexample checklist to the following claims.

1. If $\sum(a_k+b_k)$ converges, then both component series converge.
2. Two series that differ only in their first $100$ terms have the same convergence behavior.
3. If $\sum a_k=S$ and $c\ne0$, then $\sum(ca_k)=cS$.
4. The series $\sum k^3$ diverges.
5. A positive-term series with unbounded partial sums could converge or diverge.

**Explanation**

- Claim 1 is false: $a_k=1$ and $b_k=-1$ give a convergent combined series but divergent components.
- Claim 2 is true: a finite prefix cannot change convergence behavior.
- Claim 3 is true by the constant-multiple rule.
- Claim 4 is true because $k^3\not\to0$.
- Claim 5 is false: positive, unbounded partial sums increase without a finite limit.

Therefore, exactly Claims 2, 3, and 4 are true.

```quiz
type: radio
id: ohw4-p1-mixed-claims
content: |-
  Select the set containing every true claim from the example above.
options:
- id: a
  content: |-
    Claims 1, 2, and 3 only
- id: b
  content: |-
    Claims 2, 3, and 4 only
  correct: true
- id: c
  content: |-
    Claims 2 and 4 only
- id: d
  content: |-
    Claims 1, 3, and 5 only
- id: e
  content: |-
    All five claims
```

---

<a id="summary"></a>
## Summary

For each claim about infinite series:

1. Mark the hypothesis and conclusion.
2. Check that a known theorem runs in that exact direction.
3. If the claim reverses a theorem, test it with a counterexample; opposite divergent series can cancel.
4. Ignore finite prefixes when deciding convergence, though they can change a convergent sum.
5. Use term behavior and partial sums for quick divergence checks.

The central trap is assuming that a convergent combined series must have convergent components. Cancellation shows that it need not.
